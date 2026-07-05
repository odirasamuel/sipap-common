"""
Tests for production telemetry system.

Tests TelemetryRecord dataclass and utility functions for tracking
prediction performance, API latency, cache hit rates, and error patterns.
"""

from datetime import datetime
from decimal import Decimal


class TestTelemetryRecord:
    """Test TelemetryRecord dataclass creation and serialization."""

    def test_create_telemetry_record(self):
        """Test creating TelemetryRecord with required fields."""
        from sipap_common.telemetry import TelemetryRecord

        record = TelemetryRecord(
            session_id="session_abc123",
            start_ts="2026-07-05T12:00:00+00:00",
            end_ts="2026-07-05T12:00:05+00:00",
            processing_time_ms=5000,
            status="resolved",
            prediction_type="1X2",
            match_id="match_123"
        )

        assert record.session_id == "session_abc123"
        assert record.processing_time_ms == 5000
        assert record.status == "resolved"

    def test_telemetry_record_to_dynamodb_item(self):
        """Test serializing TelemetryRecord to DynamoDB-compatible dict."""
        from sipap_common.telemetry import TelemetryRecord

        record = TelemetryRecord(
            session_id="session_abc123",
            start_ts="2026-07-05T12:00:00+00:00",
            end_ts="2026-07-05T12:00:05+00:00",
            processing_time_ms=5000,
            status="resolved",
            prediction_type="1X2",
            match_id="match_123",
            confidence_score=0.85,
            sources_used=["api-football", "the-odds-api"]
        )

        item = record.to_dynamodb_item()

        # Verify all fields present
        assert item["session_id"] == "session_abc123"
        assert item["processing_time_ms"] == 5000
        assert item["status"] == "resolved"
        assert item["confidence_score"] == Decimal("0.85")
        assert item["sources_used"] == ["api-football", "the-odds-api"]

    def test_telemetry_record_composite_key(self):
        """Test composite key generation for prediction_match GSI."""
        from sipap_common.telemetry import TelemetryRecord

        record = TelemetryRecord(
            session_id="session_abc123",
            start_ts="2026-07-05T12:00:00+00:00",
            end_ts="2026-07-05T12:00:05+00:00",
            processing_time_ms=5000,
            status="resolved",
            prediction_type="1X2",
            match_id="match_123"
        )

        item = record.to_dynamodb_item()

        # Verify composite key for GSI
        assert item["prediction_match"] == "1X2#match_123"

    def test_telemetry_record_optional_fields(self):
        """Test TelemetryRecord with optional fields missing."""
        from sipap_common.telemetry import TelemetryRecord

        record = TelemetryRecord(
            session_id="session_abc123",
            start_ts="2026-07-05T12:00:00+00:00",
            end_ts="2026-07-05T12:00:05+00:00",
            processing_time_ms=5000,
            status="error",
            prediction_type="1X2",
            match_id="match_123"
        )

        item = record.to_dynamodb_item()

        # Optional fields should have default values
        assert item["confidence_score"] == Decimal("0")
        assert item["sources_used"] == []
        assert item["error_type"] == ""


class TestNormalizeDynamoDBValue:
    """Test DynamoDB type descriptor unwrapping."""

    def test_normalize_string_value(self):
        """Test unwrapping DynamoDB string type descriptor."""
        from sipap_common.telemetry import normalize_dynamodb_value

        result = normalize_dynamodb_value({"S": "hello"})
        assert result == "hello"

    def test_normalize_number_value(self):
        """Test unwrapping DynamoDB number type descriptor."""
        from sipap_common.telemetry import normalize_dynamodb_value

        result = normalize_dynamodb_value({"N": "42"})
        assert result == "42"  # Returns as string (caller casts if needed)

    def test_normalize_boolean_value(self):
        """Test unwrapping DynamoDB boolean type descriptor."""
        from sipap_common.telemetry import normalize_dynamodb_value

        result = normalize_dynamodb_value({"BOOL": True})
        assert result is True

    def test_normalize_null_value(self):
        """Test unwrapping DynamoDB null type descriptor."""
        from sipap_common.telemetry import normalize_dynamodb_value

        result = normalize_dynamodb_value({"NULL": True})
        assert result is None

    def test_normalize_list_value(self):
        """Test unwrapping DynamoDB list type descriptor."""
        from sipap_common.telemetry import normalize_dynamodb_value

        result = normalize_dynamodb_value({"L": [{"S": "a"}, {"S": "b"}]})
        assert result == ["a", "b"]

    def test_normalize_map_value(self):
        """Test unwrapping DynamoDB map type descriptor."""
        from sipap_common.telemetry import normalize_dynamodb_value

        result = normalize_dynamodb_value({
            "M": {
                "key1": {"S": "value1"},
                "key2": {"N": "42"}
            }
        })
        assert result == {"key1": "value1", "key2": "42"}

    def test_normalize_plain_value_passes_through(self):
        """Test plain Python values pass through unchanged."""
        from sipap_common.telemetry import normalize_dynamodb_value

        assert normalize_dynamodb_value("plain_string") == "plain_string"
        assert normalize_dynamodb_value(42) == 42
        assert normalize_dynamodb_value([1, 2, 3]) == [1, 2, 3]


class TestStatusMapping:
    """Test prediction status to telemetry status mapping."""

    def test_success_status_mapped_to_resolved(self):
        """Test 'success' prediction status maps to 'resolved'."""
        from sipap_common.telemetry import prediction_status_to_telemetry

        assert prediction_status_to_telemetry("success") == "resolved"

    def test_pending_status_mapped_to_deferred(self):
        """Test 'pending' prediction status maps to 'deferred'."""
        from sipap_common.telemetry import prediction_status_to_telemetry

        assert prediction_status_to_telemetry("pending") == "deferred"

    def test_failed_status_mapped_to_error(self):
        """Test 'failed' prediction status maps to 'error'."""
        from sipap_common.telemetry import prediction_status_to_telemetry

        assert prediction_status_to_telemetry("failed") == "error"

    def test_unknown_status_mapped_to_error(self):
        """Test unknown prediction status maps to 'error'."""
        from sipap_common.telemetry import prediction_status_to_telemetry

        assert prediction_status_to_telemetry("unknown") == "error"
        assert prediction_status_to_telemetry(None) == "error"

    def test_valid_statuses(self):
        """Test all valid prediction statuses."""
        from sipap_common.telemetry import prediction_status_to_telemetry

        valid_mappings = {
            "success": "resolved",
            "pending": "deferred",
            "failed": "error"
        }

        for prediction_status, expected_telemetry_status in valid_mappings.items():
            assert prediction_status_to_telemetry(prediction_status) == expected_telemetry_status


class TestTimestampHelpers:
    """Test timestamp utility functions."""

    def test_now_iso_returns_utc_timestamp(self):
        """Test now_iso() returns UTC ISO 8601 timestamp."""
        from sipap_common.telemetry import now_iso

        timestamp = now_iso()

        # Verify ISO 8601 format with timezone
        assert "T" in timestamp
        assert "+" in timestamp or "Z" in timestamp

        # Verify parseable as datetime
        dt = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
        assert dt.tzinfo is not None

    def test_calculate_processing_time_ms(self):
        """Test calculating processing time in milliseconds."""
        from sipap_common.telemetry import calculate_processing_time_ms

        start_ts = "2026-07-05T12:00:00+00:00"
        end_ts = "2026-07-05T12:00:05+00:00"

        processing_time = calculate_processing_time_ms(start_ts, end_ts)

        assert processing_time == 5000  # 5 seconds = 5000 ms

    def test_calculate_processing_time_ms_with_milliseconds(self):
        """Test calculating processing time with sub-second precision."""
        from sipap_common.telemetry import calculate_processing_time_ms

        start_ts = "2026-07-05T12:00:00.000+00:00"
        end_ts = "2026-07-05T12:00:00.250+00:00"

        processing_time = calculate_processing_time_ms(start_ts, end_ts)

        assert processing_time == 250  # 250 milliseconds


class TestDecimalConversion:
    """Test float to Decimal conversion for DynamoDB."""

    def test_float_to_decimal_conversion(self):
        """Test converting float confidence score to Decimal."""
        from sipap_common.telemetry import float_to_decimal

        result = float_to_decimal(0.85)

        assert isinstance(result, Decimal)
        assert result == Decimal("0.85")

    def test_none_to_decimal_zero(self):
        """Test None converts to Decimal zero."""
        from sipap_common.telemetry import float_to_decimal

        result = float_to_decimal(None)

        assert isinstance(result, Decimal)
        assert result == Decimal("0")

    def test_int_to_decimal_conversion(self):
        """Test converting int to Decimal."""
        from sipap_common.telemetry import float_to_decimal

        result = float_to_decimal(1)

        assert isinstance(result, Decimal)
        assert result == Decimal("1")
