"""
Example: Telemetry Tracking and DynamoDB Publishing

Demonstrates how to:
1. Create telemetry records for prediction performance tracking
2. Publish telemetry to DynamoDB using fire-and-forget pattern
3. Handle telemetry for both successful and failed predictions

This example shows production-grade telemetry tracking that never blocks
predictions and provides comprehensive metrics for analysis.
"""

from datetime import UTC, datetime
from decimal import Decimal

from sipap_common.aws.dynamodb import SIPAPTelemetryPublisher
from sipap_common.telemetry import (
    TelemetryRecord,
    calculate_processing_time_ms,
    float_to_decimal,
    now_iso,
    prediction_status_to_telemetry,
)


def example_successful_prediction():
    """Example: Track telemetry for a successful prediction."""
    print("=" * 60)
    print("Example 1: Successful Prediction Telemetry")
    print("=" * 60)

    # Record start time
    start_ts = now_iso()
    print(f"Prediction started at: {start_ts}")

    # Simulate prediction processing
    import time
    time.sleep(0.1)  # Simulate 100ms processing

    # Record end time
    end_ts = now_iso()
    processing_time = calculate_processing_time_ms(start_ts, end_ts)
    print(f"Prediction completed at: {end_ts}")
    print(f"Processing time: {processing_time}ms")

    # Create telemetry record
    record = TelemetryRecord(
        session_id="session_abc123",
        start_ts=start_ts,
        end_ts=end_ts,
        processing_time_ms=processing_time,
        status=prediction_status_to_telemetry("success"),  # Maps to "resolved"
        prediction_type="1X2",
        match_id="match_12345",
        confidence_score=0.85,
        sources_used=["api-football", "the-odds-api"],
        error_type=""
    )

    print(f"\nTelemetry Record:")
    print(f"  Status: {record.status}")
    print(f"  Confidence: {record.confidence_score}")
    print(f"  Sources: {', '.join(record.sources_used)}")

    # Publish to DynamoDB (fire-and-forget)
    # Note: Set SIPAP_TELEMETRY_ENABLED=false in tests to disable actual publishing
    publisher = SIPAPTelemetryPublisher(enabled=False)  # Disabled for example
    publisher.publish(record)

    print("\n✅ Telemetry published successfully (fire-and-forget)")


def example_failed_prediction():
    """Example: Track telemetry for a failed prediction."""
    print("\n" + "=" * 60)
    print("Example 2: Failed Prediction Telemetry")
    print("=" * 60)

    start_ts = now_iso()

    # Simulate prediction failure after some processing
    import time
    time.sleep(0.05)

    end_ts = now_iso()
    processing_time = calculate_processing_time_ms(start_ts, end_ts)

    # Create telemetry record for failure
    record = TelemetryRecord(
        session_id="session_xyz789",
        start_ts=start_ts,
        end_ts=end_ts,
        processing_time_ms=processing_time,
        status=prediction_status_to_telemetry("failed"),  # Maps to "error"
        prediction_type="BTTS",
        match_id="match_67890",
        confidence_score=0.0,  # No confidence for failed predictions
        sources_used=["api-football"],  # Partial sources before failure
        error_type="api_timeout"
    )

    print(f"Telemetry Record (Failed):")
    print(f"  Status: {record.status}")
    print(f"  Error Type: {record.error_type}")
    print(f"  Processing Time: {processing_time}ms")

    publisher = SIPAPTelemetryPublisher(enabled=False)
    publisher.publish(record)

    print("\n✅ Failure telemetry published (for error forensics)")


def example_batch_telemetry():
    """Example: Publish multiple telemetry records in batch."""
    print("\n" + "=" * 60)
    print("Example 3: Batch Telemetry Publishing")
    print("=" * 60)

    # Create multiple records
    records = []
    for i in range(3):
        start_ts = now_iso()
        import time
        time.sleep(0.02)
        end_ts = now_iso()

        record = TelemetryRecord(
            session_id=f"session_{i}",
            start_ts=start_ts,
            end_ts=end_ts,
            processing_time_ms=calculate_processing_time_ms(start_ts, end_ts),
            status="resolved",
            prediction_type="1X2",
            match_id=f"match_{i}",
            confidence_score=0.7 + (i * 0.1)
        )
        records.append(record)

    print(f"Created {len(records)} telemetry records")

    # Publish batch (more efficient than individual publishes)
    publisher = SIPAPTelemetryPublisher(enabled=False)
    publisher.publish_batch(records)

    print(f"\n✅ Batch of {len(records)} records published")


def example_dynamodb_serialization():
    """Example: DynamoDB item serialization with Decimal conversion."""
    print("\n" + "=" * 60)
    print("Example 4: DynamoDB Serialization")
    print("=" * 60)

    record = TelemetryRecord(
        session_id="session_demo",
        start_ts=now_iso(),
        end_ts=now_iso(),
        processing_time_ms=250,
        status="resolved",
        prediction_type="Over/Under",
        match_id="match_demo",
        confidence_score=0.92
    )

    # Convert to DynamoDB-compatible format
    dynamodb_item = record.to_dynamodb_item()

    print("DynamoDB Item Structure:")
    print(f"  session_id: {dynamodb_item['session_id']}")
    print(f"  confidence_score: {dynamodb_item['confidence_score']} (type: {type(dynamodb_item['confidence_score']).__name__})")
    print(f"  prediction_match: {dynamodb_item['prediction_match']}")  # Composite GSI key

    # Verify Decimal conversion for DynamoDB
    assert isinstance(dynamodb_item['confidence_score'], Decimal)
    print("\n✅ Float correctly converted to Decimal for DynamoDB")


if __name__ == "__main__":
    print("\nSIPAP Telemetry Tracking Examples")
    print("=" * 60)

    example_successful_prediction()
    example_failed_prediction()
    example_batch_telemetry()
    example_dynamodb_serialization()

    print("\n" + "=" * 60)
    print("All examples completed successfully!")
    print("=" * 60)
