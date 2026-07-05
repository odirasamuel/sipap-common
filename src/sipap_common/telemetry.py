"""
Telemetry data model and utilities for SIPAP.

Provides production-grade telemetry tracking for:
- Prediction performance metrics
- API call latency
- Cache hit rates
- Source effectiveness
- Error patterns and forensics

Architecture:
- Fire-and-forget publishing (never blocks predictions)
- DynamoDB storage with GSI for analytics
- Opt-in via environment variable
"""

from dataclasses import dataclass
from datetime import UTC, datetime
from decimal import Decimal
from typing import Any

# Valid prediction statuses that map to non-error telemetry status
_VALID_PREDICTION_STATUSES = frozenset({"success", "pending"})

# DynamoDB single-key type descriptor keys
_DYNAMODB_TYPE_KEYS = frozenset({"S", "N", "B", "BOOL", "NULL", "L", "M", "SS", "NS", "BS"})


def normalize_dynamodb_value(
    value: dict[str, Any] | list[Any] | str | int | float | bool | None,
) -> Any:
    """
    Unwrap a DynamoDB type descriptor dict to its plain Python value.

    DynamoDB uses typed dicts like {"S": "hello"}, {"N": "42"}, {"BOOL": true}
    to represent attribute values. This function strips those wrappers so callers
    receive plain Python scalars, lists, and dicts. Non-DynamoDB values pass
    through unchanged.

    Args:
        value: DynamoDB type descriptor or plain Python value

    Returns:
        Plain Python value

    Examples:
        >>> normalize_dynamodb_value({"S": "hello"})
        'hello'
        >>> normalize_dynamodb_value({"N": "42"})
        '42'
        >>> normalize_dynamodb_value({"BOOL": True})
        True
        >>> normalize_dynamodb_value("plain_string")
        'plain_string'
    """
    if isinstance(value, list):
        return [normalize_dynamodb_value(item) for item in value]
    if not isinstance(value, dict) or len(value) != 1:
        return value
    type_key = next(iter(value))
    if type_key not in _DYNAMODB_TYPE_KEYS:
        return value
    type_val = value[type_key]
    if type_key == "S":
        return str(type_val)
    if type_key == "N":
        return type_val  # keep as string; caller may cast if needed
    if type_key == "BOOL":
        return bool(type_val)
    if type_key == "NULL":
        return None
    if type_key == "L":
        return [normalize_dynamodb_value(item) for item in type_val]
    if type_key == "M":
        return {k: normalize_dynamodb_value(v) for k, v in type_val.items()}
    if type_key in ("SS", "NS", "BS"):
        return list(type_val)
    return value


def prediction_status_to_telemetry(prediction_status: str | None) -> str:
    """
    Map prediction status string to canonical telemetry status.

    Args:
        prediction_status: Prediction status from agent output (may be None or unknown)

    Returns:
        Canonical telemetry status: 'resolved' | 'deferred' | 'error'

    Examples:
        >>> prediction_status_to_telemetry("success")
        'resolved'
        >>> prediction_status_to_telemetry("pending")
        'deferred'
        >>> prediction_status_to_telemetry("failed")
        'error'
        >>> prediction_status_to_telemetry(None)
        'error'
    """
    if prediction_status == "success":
        return "resolved"
    if prediction_status == "pending":
        return "deferred"
    return "error"


def now_iso() -> str:
    """
    Return current UTC time as ISO 8601 string.

    Returns:
        ISO 8601 timestamp with timezone (e.g., "2026-07-05T12:00:00+00:00")

    Example:
        >>> timestamp = now_iso()
        >>> "T" in timestamp
        True
        >>> "+" in timestamp or "Z" in timestamp
        True
    """
    return datetime.now(UTC).isoformat()


def calculate_processing_time_ms(start_ts: str, end_ts: str) -> int:
    """
    Calculate processing time in milliseconds between two ISO 8601 timestamps.

    Args:
        start_ts: Start timestamp (ISO 8601)
        end_ts: End timestamp (ISO 8601)

    Returns:
        Processing time in milliseconds

    Example:
        >>> calculate_processing_time_ms(
        ...     "2026-07-05T12:00:00+00:00",
        ...     "2026-07-05T12:00:05+00:00"
        ... )
        5000
    """
    start_dt = datetime.fromisoformat(start_ts.replace("Z", "+00:00"))
    end_dt = datetime.fromisoformat(end_ts.replace("Z", "+00:00"))
    delta = end_dt - start_dt
    return int(delta.total_seconds() * 1000)


def float_to_decimal(value: float | int | None) -> Decimal:
    """
    Convert float/int to Decimal for DynamoDB storage.

    DynamoDB requires Decimal type for numeric values with fractional parts.
    None converts to Decimal("0").

    Args:
        value: Float, int, or None

    Returns:
        Decimal representation

    Examples:
        >>> float_to_decimal(0.85)
        Decimal('0.85')
        >>> float_to_decimal(None)
        Decimal('0')
        >>> float_to_decimal(1)
        Decimal('1')
    """
    if value is None:
        return Decimal("0")
    return Decimal(str(value))


@dataclass
class TelemetryRecord:
    """
    Telemetry record for a single prediction request.

    Captures comprehensive metrics for prediction performance analysis,
    error forensics, and source effectiveness tracking.

    Fields:
        session_id: UUID5 from request payload (deterministic)
        start_ts: ISO 8601 UTC - when prediction started
        end_ts: ISO 8601 UTC - when prediction completed
        processing_time_ms: Wall-clock prediction time
        status: resolved | deferred | error
        prediction_type: 1X2, BTTS, Over/Under, etc.
        match_id: Unique match identifier
        confidence_score: 0-1 prediction confidence (default: 0)
        sources_used: List of data sources used (default: [])
        error_type: Error classification on failures (default: "")
        prediction_match: Composite key for GSI (prediction_type#match_id)

    DynamoDB Schema:
        Table: SIPAPTelemetry
        Primary Key: session_id (high cardinality, no hot partitions)
        GSI 1: PredictionMatchHistoryIndex (prediction_match + end_ts) - match history
        GSI 2: StatusTrendsIndex (status + end_ts) - outcome analytics
    """

    session_id: str
    start_ts: str
    end_ts: str
    processing_time_ms: int
    status: str
    prediction_type: str
    match_id: str
    confidence_score: float = 0.0
    sources_used: list[str] | None = None
    error_type: str = ""

    def to_dynamodb_item(self) -> dict[str, Any]:
        """
        Serialize TelemetryRecord to DynamoDB-compatible dict.

        Converts floats to Decimal for DynamoDB compatibility.
        Generates composite key for GSI.

        Returns:
            Dict suitable for boto3 put_item()

        Example:
            >>> record = TelemetryRecord(
            ...     session_id="abc123",
            ...     start_ts="2026-07-05T12:00:00+00:00",
            ...     end_ts="2026-07-05T12:00:05+00:00",
            ...     processing_time_ms=5000,
            ...     status="resolved",
            ...     prediction_type="1X2",
            ...     match_id="match_123",
            ...     confidence_score=0.85
            ... )
            >>> item = record.to_dynamodb_item()
            >>> item["confidence_score"]
            Decimal('0.85')
        """
        return {
            "session_id": self.session_id,
            "start_ts": self.start_ts,
            "end_ts": self.end_ts,
            "processing_time_ms": self.processing_time_ms,
            "status": self.status,
            "prediction_type": self.prediction_type,
            "match_id": self.match_id,
            "confidence_score": float_to_decimal(self.confidence_score),
            "sources_used": self.sources_used or [],
            "error_type": self.error_type,
            # Composite key for GSI
            "prediction_match": f"{self.prediction_type}#{self.match_id}",
        }
