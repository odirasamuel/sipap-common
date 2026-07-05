"""
Example: Exception-Carried Telemetry

Demonstrates how to:
1. Attach telemetry records to exceptions for failure tracking
2. Preserve telemetry on all code paths (success + failure)
3. Extract telemetry from caught exceptions for publishing

This pattern ensures complete observability even when errors occur,
enabling comprehensive error forensics and SLA tracking.
"""

from sipap_common.exceptions import (
    CacheError,
    DatabaseError,
    SIPAPException,
    ValidationError,
)
from sipap_common.telemetry import TelemetryRecord, now_iso, calculate_processing_time_ms


def example_exception_with_telemetry():
    """Example: Raise and catch exception with telemetry."""
    print("=" * 60)
    print("Example 1: Exception with Telemetry")
    print("=" * 60)

    start_ts = now_iso()

    # Simulate processing before error
    import time
    time.sleep(0.05)

    end_ts = now_iso()

    # Create telemetry record for the failed operation
    telemetry = TelemetryRecord(
        session_id="session_error_123",
        start_ts=start_ts,
        end_ts=end_ts,
        processing_time_ms=calculate_processing_time_ms(start_ts, end_ts),
        status="error",
        prediction_type="1X2",
        match_id="match_error",
        confidence_score=0.0,
        sources_used=["api-football"],
        error_type="cache_timeout"
    )

    try:
        # Raise exception with telemetry attached
        raise CacheError(
            "Redis connection timeout",
            telemetry_record=telemetry
        )
    except CacheError as e:
        print(f"❌ Error caught: {e}")
        print(f"   Has telemetry: {e.has_telemetry()}")

        # Extract telemetry for publishing
        if e.has_telemetry():
            record = e.get_telemetry()
            print(f"   Session ID: {record.session_id}")
            print(f"   Error Type: {record.error_type}")
            print(f"   Processing Time: {record.processing_time_ms}ms")

            # Publish telemetry (fire-and-forget)
            # from sipap_common.aws.dynamodb import SIPAPTelemetryPublisher
            # publisher = SIPAPTelemetryPublisher()
            # publisher.publish(record)
            print("\n✅ Telemetry extracted and ready for publishing")


def example_validation_error_with_context():
    """Example: ValidationError carrying detailed context."""
    print("\n" + "=" * 60)
    print("Example 2: ValidationError with Context")
    print("=" * 60)

    start_ts = now_iso()
    import time
    time.sleep(0.02)
    end_ts = now_iso()

    # Validation failed - attach context via telemetry
    telemetry = TelemetryRecord(
        session_id="session_validation",
        start_ts=start_ts,
        end_ts=end_ts,
        processing_time_ms=calculate_processing_time_ms(start_ts, end_ts),
        status="error",
        prediction_type="BTTS",
        match_id="invalid_match",
        error_type="validation_failed",
        sources_used=[]  # No sources used before validation
    )

    try:
        raise ValidationError(
            "Invalid match_id format",
            telemetry_record=telemetry
        )
    except ValidationError as e:
        print(f"❌ Validation Error: {e}")

        if e.has_telemetry():
            record = e.get_telemetry()
            print(f"   Error occurred in: {record.prediction_type} prediction")
            print(f"   Invalid match_id: {record.match_id}")

            print("\n✅ Validation error context preserved")


def example_database_error_preserving_partial_results():
    """Example: DatabaseError with partial results preserved."""
    print("\n" + "=" * 60)
    print("Example 3: DatabaseError with Partial Results")
    print("=" * 60)

    start_ts = now_iso()

    # Simulate partial processing before database failure
    sources_completed = ["api-football", "the-odds-api"]
    import time
    time.sleep(0.08)

    end_ts = now_iso()

    telemetry = TelemetryRecord(
        session_id="session_db_error",
        start_ts=start_ts,
        end_ts=end_ts,
        processing_time_ms=calculate_processing_time_ms(start_ts, end_ts),
        status="error",
        prediction_type="Over/Under",
        match_id="match_db",
        confidence_score=0.0,
        sources_used=sources_completed,  # Partial results before error
        error_type="database_timeout"
    )

    try:
        raise DatabaseError(
            "Query timeout after 5 seconds",
            telemetry_record=telemetry
        )
    except DatabaseError as e:
        print(f"❌ Database Error: {e}")

        if e.has_telemetry():
            record = e.get_telemetry()
            print(f"   Sources completed before error: {', '.join(record.sources_used)}")
            print(f"   Processing time: {record.processing_time_ms}ms")

            print("\n✅ Partial results preserved despite error")


def example_exception_without_telemetry():
    """Example: Exception without telemetry (backward compatible)."""
    print("\n" + "=" * 60)
    print("Example 4: Exception Without Telemetry (Backward Compatible)")
    print("=" * 60)

    try:
        # Old-style exception without telemetry
        raise SIPAPException("Generic error message")
    except SIPAPException as e:
        print(f"❌ Error caught: {e}")
        print(f"   Has telemetry: {e.has_telemetry()}")

        # Safe to check for telemetry (returns None if not present)
        telemetry = e.get_telemetry()
        if telemetry is None:
            print("   No telemetry attached (backward compatible)")

        print("\n✅ Backward compatibility maintained")


def example_telemetry_in_exception_hierarchy():
    """Example: Telemetry works with entire exception hierarchy."""
    print("\n" + "=" * 60)
    print("Example 5: Telemetry in Exception Hierarchy")
    print("=" * 60)

    start_ts = now_iso()
    import time
    time.sleep(0.03)
    end_ts = now_iso()

    telemetry = TelemetryRecord(
        session_id="session_hierarchy",
        start_ts=start_ts,
        end_ts=end_ts,
        processing_time_ms=calculate_processing_time_ms(start_ts, end_ts),
        status="error",
        prediction_type="1X2",
        match_id="match_hierarchy",
        error_type="unknown"
    )

    try:
        # Can be any SIPAPException subclass
        raise ValidationError("Error", telemetry_record=telemetry)
    except SIPAPException as e:  # Catch base exception
        # Telemetry still accessible
        print(f"❌ Caught as SIPAPException: {e}")
        print(f"   Actual type: {type(e).__name__}")
        print(f"   Has telemetry: {e.has_telemetry()}")

        print("\n✅ Telemetry preserved across exception hierarchy")


if __name__ == "__main__":
    print("\nException-Carried Telemetry Examples")
    print("=" * 60)

    example_exception_with_telemetry()
    example_validation_error_with_context()
    example_database_error_preserving_partial_results()
    example_exception_without_telemetry()
    example_telemetry_in_exception_hierarchy()

    print("\n" + "=" * 60)
    print("All examples completed successfully!")
    print("=" * 60)
    print("\nKey Takeaways:")
    print("- Exceptions can carry telemetry for complete observability")
    print("- Use has_telemetry() to check before extracting")
    print("- get_telemetry() returns None if not present (safe)")
    print("- Works with entire exception hierarchy")
    print("- Backward compatible (telemetry is optional)")
