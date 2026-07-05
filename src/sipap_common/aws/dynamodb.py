"""
DynamoDB telemetry publisher for SIPAP.

Provides fire-and-forget telemetry publishing to DynamoDB with:
- Async publishing (doesn't block predictions)
- Graceful error handling (logs errors, doesn't raise)
- Batch operations for efficiency
- Opt-in via environment variable
"""

import logging
import os
from decimal import Decimal
from typing import Any

import boto3

from sipap_common.telemetry import TelemetryRecord

logger = logging.getLogger(__name__)


def serialize_for_dynamodb(data: dict[str, Any]) -> dict[str, Any]:
    """
    Serialize dict for DynamoDB by converting floats to Decimal.

    DynamoDB requires Decimal type for numeric values with fractional parts.
    This function recursively converts all floats in the data structure.

    Args:
        data: Dict to serialize

    Returns:
        Dict with floats converted to Decimal

    Example:
        >>> serialize_for_dynamodb({"score": 0.85, "count": 10})
        {'score': Decimal('0.85'), 'count': 10}
    """
    result: dict[str, Any] = {}
    for key, value in data.items():
        if isinstance(value, float):
            result[key] = Decimal(str(value))
        elif isinstance(value, dict):
            result[key] = serialize_for_dynamodb(value)
        elif isinstance(value, list):
            result[key] = [
                Decimal(str(v)) if isinstance(v, float) else v
                for v in value
            ]
        else:
            result[key] = value
    return result


class SIPAPTelemetryPublisher:
    """
    Fire-and-forget telemetry publisher to DynamoDB.

    Architecture:
    - Never blocks predictions (async publish, error suppression)
    - Respects SIPAP_TELEMETRY_ENABLED environment variable
    - Uses batch operations for efficiency
    - Logs errors but doesn't raise exceptions

    Usage:
        publisher = SIPAPTelemetryPublisher()

        # Single record
        publisher.publish(telemetry_record)

        # Batch records
        publisher.publish_batch([record1, record2, record3])

    Environment Variables:
        SIPAP_TELEMETRY_ENABLED: "true" (default) or "false"
        AWS_REGION: AWS region (default: us-east-1)
    """

    def __init__(
        self,
        table_name: str = "SIPAPTelemetry",
        dynamodb_client: Any | None = None,
        enabled: bool | None = None,
    ):
        """
        Initialize DynamoDB telemetry publisher.

        Args:
            table_name: DynamoDB table name (default: "SIPAPTelemetry")
            dynamodb_client: boto3 DynamoDB client (default: creates new client)
            enabled: Override telemetry enabled flag (default: from env var)
        """
        self.table_name = table_name

        # Check if telemetry is enabled
        if enabled is not None:
            self.enabled = enabled
        else:
            env_enabled = os.environ.get("SIPAP_TELEMETRY_ENABLED", "true").lower()
            self.enabled = env_enabled == "true"

        # Create DynamoDB client if not provided
        if dynamodb_client is not None:
            self.dynamodb_client = dynamodb_client
        else:
            region = os.environ.get("AWS_REGION", "us-east-1")
            self.dynamodb_client = boto3.client("dynamodb", region_name=region)

    def publish(self, record: TelemetryRecord) -> None:
        """
        Publish single telemetry record to DynamoDB (fire-and-forget).

        Args:
            record: TelemetryRecord to publish

        Note:
            Errors are logged but not raised to ensure predictions never block.
        """
        if not self.enabled:
            return

        try:
            # Serialize record to DynamoDB item
            item = record.to_dynamodb_item()

            # Serialize for DynamoDB (convert floats to Decimal)
            item = serialize_for_dynamodb(item)

            # Publish to DynamoDB
            self.dynamodb_client.put_item(
                TableName=self.table_name,
                Item=item
            )

            logger.debug(
                "Published telemetry record",
                extra={
                    "session_id": record.session_id,
                    "status": record.status,
                    "prediction_type": record.prediction_type
                }
            )

        except Exception as e:
            logger.error(
                f"Failed to publish telemetry record: {e}",
                extra={
                    "session_id": record.session_id,
                    "error": str(e)
                },
                exc_info=True
            )

    def publish_batch(self, records: list[TelemetryRecord]) -> None:
        """
        Publish batch of telemetry records to DynamoDB (fire-and-forget).

        Args:
            records: List of TelemetryRecord to publish

        Note:
            Errors are logged but not raised to ensure predictions never block.
            DynamoDB batch_write_item supports up to 25 items per request.
        """
        if not self.enabled or not records:
            return

        try:
            # Serialize records to DynamoDB items
            items = []
            for record in records:
                item = record.to_dynamodb_item()
                item = serialize_for_dynamodb(item)
                items.append({"PutRequest": {"Item": item}})

            # Batch write to DynamoDB (max 25 items per request)
            batch_size = 25
            for i in range(0, len(items), batch_size):
                batch = items[i:i + batch_size]
                self.dynamodb_client.batch_write_item(
                    RequestItems={
                        self.table_name: batch
                    }
                )

            logger.debug(
                f"Published {len(records)} telemetry records in batch",
                extra={"record_count": len(records)}
            )

        except Exception as e:
            logger.error(
                f"Failed to publish telemetry batch: {e}",
                extra={
                    "record_count": len(records),
                    "error": str(e)
                },
                exc_info=True
            )
