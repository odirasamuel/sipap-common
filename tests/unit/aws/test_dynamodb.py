"""
Tests for DynamoDB telemetry publisher.

Tests fire-and-forget telemetry publishing to DynamoDB with error handling,
batch operations, and opt-in behavior.
"""

from decimal import Decimal
from unittest.mock import MagicMock, patch


class TestSIPAPTelemetryPublisher:
    """Test SIPAPTelemetryPublisher fire-and-forget publishing."""

    def test_create_publisher_with_defaults(self):
        """Test creating publisher with default configuration."""
        from sipap_common.aws.dynamodb import SIPAPTelemetryPublisher

        publisher = SIPAPTelemetryPublisher()

        assert publisher.table_name == "SIPAPTelemetry"
        assert publisher.enabled is True
        assert publisher.dynamodb_client is not None

    def test_create_publisher_with_custom_table(self):
        """Test creating publisher with custom table name."""
        from sipap_common.aws.dynamodb import SIPAPTelemetryPublisher

        publisher = SIPAPTelemetryPublisher(table_name="CustomTelemetry")

        assert publisher.table_name == "CustomTelemetry"

    def test_create_publisher_disabled_via_env_var(self):
        """Test publisher respects SIPAP_TELEMETRY_ENABLED=false."""
        from sipap_common.aws.dynamodb import SIPAPTelemetryPublisher

        with patch.dict("os.environ", {"SIPAP_TELEMETRY_ENABLED": "false"}):
            publisher = SIPAPTelemetryPublisher()

        assert publisher.enabled is False

    def test_publish_record_when_enabled(self):
        """Test publishing telemetry record succeeds when enabled."""
        from sipap_common.aws.dynamodb import SIPAPTelemetryPublisher
        from sipap_common.telemetry import TelemetryRecord

        mock_client = MagicMock()
        publisher = SIPAPTelemetryPublisher(dynamodb_client=mock_client)

        record = TelemetryRecord(
            session_id="session_123",
            start_ts="2026-07-05T12:00:00+00:00",
            end_ts="2026-07-05T12:00:05+00:00",
            processing_time_ms=5000,
            status="resolved",
            prediction_type="1X2",
            match_id="match_123",
            confidence_score=0.85
        )

        publisher.publish(record)

        # Verify put_item was called with correct arguments
        mock_client.put_item.assert_called_once()
        call_args = mock_client.put_item.call_args
        assert call_args[1]["TableName"] == "SIPAPTelemetry"
        assert "Item" in call_args[1]

    def test_publish_record_when_disabled(self):
        """Test publishing is skipped when disabled."""
        from sipap_common.aws.dynamodb import SIPAPTelemetryPublisher
        from sipap_common.telemetry import TelemetryRecord

        mock_client = MagicMock()
        publisher = SIPAPTelemetryPublisher(
            dynamodb_client=mock_client,
            enabled=False
        )

        record = TelemetryRecord(
            session_id="session_123",
            start_ts="2026-07-05T12:00:00+00:00",
            end_ts="2026-07-05T12:00:05+00:00",
            processing_time_ms=5000,
            status="resolved",
            prediction_type="1X2",
            match_id="match_123"
        )

        publisher.publish(record)

        # Verify put_item was NOT called
        mock_client.put_item.assert_not_called()

    def test_publish_handles_dynamodb_errors_gracefully(self):
        """Test publisher logs errors but doesn't raise exceptions."""
        from sipap_common.aws.dynamodb import SIPAPTelemetryPublisher
        from sipap_common.telemetry import TelemetryRecord

        mock_client = MagicMock()
        mock_client.put_item.side_effect = Exception("DynamoDB error")

        publisher = SIPAPTelemetryPublisher(dynamodb_client=mock_client)

        record = TelemetryRecord(
            session_id="session_123",
            start_ts="2026-07-05T12:00:00+00:00",
            end_ts="2026-07-05T12:00:05+00:00",
            processing_time_ms=5000,
            status="resolved",
            prediction_type="1X2",
            match_id="match_123"
        )

        # Should not raise exception (fire-and-forget)
        publisher.publish(record)

    def test_publish_batch_records(self):
        """Test batch publishing multiple records."""
        from sipap_common.aws.dynamodb import SIPAPTelemetryPublisher
        from sipap_common.telemetry import TelemetryRecord

        mock_client = MagicMock()
        publisher = SIPAPTelemetryPublisher(dynamodb_client=mock_client)

        records = [
            TelemetryRecord(
                session_id=f"session_{i}",
                start_ts="2026-07-05T12:00:00+00:00",
                end_ts="2026-07-05T12:00:05+00:00",
                processing_time_ms=5000,
                status="resolved",
                prediction_type="1X2",
                match_id=f"match_{i}"
            )
            for i in range(3)
        ]

        publisher.publish_batch(records)

        # Verify batch_write_item was called
        mock_client.batch_write_item.assert_called_once()
        call_args = mock_client.batch_write_item.call_args
        assert "RequestItems" in call_args[1]
        assert "SIPAPTelemetry" in call_args[1]["RequestItems"]

    def test_publish_batch_when_disabled(self):
        """Test batch publishing is skipped when disabled."""
        from sipap_common.aws.dynamodb import SIPAPTelemetryPublisher
        from sipap_common.telemetry import TelemetryRecord

        mock_client = MagicMock()
        publisher = SIPAPTelemetryPublisher(
            dynamodb_client=mock_client,
            enabled=False
        )

        records = [
            TelemetryRecord(
                session_id="session_1",
                start_ts="2026-07-05T12:00:00+00:00",
                end_ts="2026-07-05T12:00:05+00:00",
                processing_time_ms=5000,
                status="resolved",
                prediction_type="1X2",
                match_id="match_1"
            )
        ]

        publisher.publish_batch(records)

        # Verify batch_write_item was NOT called
        mock_client.batch_write_item.assert_not_called()

    def test_publish_batch_handles_errors_gracefully(self):
        """Test batch publisher logs errors but doesn't raise exceptions."""
        from sipap_common.aws.dynamodb import SIPAPTelemetryPublisher
        from sipap_common.telemetry import TelemetryRecord

        mock_client = MagicMock()
        mock_client.batch_write_item.side_effect = Exception("Batch write error")

        publisher = SIPAPTelemetryPublisher(dynamodb_client=mock_client)

        records = [
            TelemetryRecord(
                session_id="session_1",
                start_ts="2026-07-05T12:00:00+00:00",
                end_ts="2026-07-05T12:00:05+00:00",
                processing_time_ms=5000,
                status="resolved",
                prediction_type="1X2",
                match_id="match_1"
            )
        ]

        # Should not raise exception (fire-and-forget)
        publisher.publish_batch(records)

    def test_record_serialization_to_dynamodb_format(self):
        """Test TelemetryRecord is properly serialized for DynamoDB."""
        from sipap_common.aws.dynamodb import SIPAPTelemetryPublisher
        from sipap_common.telemetry import TelemetryRecord

        mock_client = MagicMock()
        publisher = SIPAPTelemetryPublisher(dynamodb_client=mock_client)

        record = TelemetryRecord(
            session_id="session_123",
            start_ts="2026-07-05T12:00:00+00:00",
            end_ts="2026-07-05T12:00:05+00:00",
            processing_time_ms=5000,
            status="resolved",
            prediction_type="1X2",
            match_id="match_123",
            confidence_score=0.85,
            sources_used=["api-football", "the-odds-api"]
        )

        publisher.publish(record)

        # Verify item structure
        call_args = mock_client.put_item.call_args[1]
        item = call_args["Item"]

        # Check required fields
        assert item["session_id"] == "session_123"
        assert item["status"] == "resolved"
        assert item["prediction_type"] == "1X2"
        assert item["match_id"] == "match_123"
        assert item["prediction_match"] == "1X2#match_123"
        assert item["confidence_score"] == Decimal("0.85")
        assert item["sources_used"] == ["api-football", "the-odds-api"]


class TestDynamoDBHelpers:
    """Test DynamoDB utility functions."""

    def test_serialize_for_dynamodb_converts_floats(self):
        """Test serializer converts floats to Decimal."""
        from sipap_common.aws.dynamodb import serialize_for_dynamodb

        data = {"score": 0.85, "count": 10}
        result = serialize_for_dynamodb(data)

        assert isinstance(result["score"], Decimal)
        assert result["score"] == Decimal("0.85")
        assert result["count"] == 10

    def test_serialize_for_dynamodb_handles_nested_structures(self):
        """Test serializer handles nested dicts and lists."""
        from sipap_common.aws.dynamodb import serialize_for_dynamodb

        data = {
            "metadata": {"score": 0.85, "rank": 1},
            "values": [0.1, 0.2, 0.3]
        }
        result = serialize_for_dynamodb(data)

        assert isinstance(result["metadata"]["score"], Decimal)
        assert isinstance(result["values"][0], Decimal)
        assert result["metadata"]["rank"] == 1
