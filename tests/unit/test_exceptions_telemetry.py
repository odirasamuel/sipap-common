"""
Tests for exception-carried telemetry.

Tests that exceptions can carry partial telemetry data for failed predictions,
enabling metrics capture even when errors occur.
"""


class TestExceptionTelemetry:
    """Test exception-carried telemetry functionality."""

    def test_base_exception_accepts_telemetry_record(self):
        """Test SIPAPException can carry telemetry record."""
        from sipap_common.exceptions import SIPAPException
        from sipap_common.telemetry import TelemetryRecord

        record = TelemetryRecord(
            session_id="session_123",
            start_ts="2026-07-05T12:00:00+00:00",
            end_ts="2026-07-05T12:00:05+00:00",
            processing_time_ms=5000,
            status="error",
            prediction_type="1X2",
            match_id="match_123",
            error_type="prediction_failed"
        )

        exc = SIPAPException("Prediction failed", telemetry_record=record)

        assert exc.telemetry_record is not None
        assert exc.telemetry_record.session_id == "session_123"
        assert exc.telemetry_record.status == "error"

    def test_exception_without_telemetry_record(self):
        """Test exception works without telemetry record (backward compatible)."""
        from sipap_common.exceptions import SIPAPException

        exc = SIPAPException("Something went wrong")

        assert exc.telemetry_record is None

    def test_exception_has_telemetry_helper_method(self):
        """Test has_telemetry() helper method."""
        from sipap_common.exceptions import SIPAPException
        from sipap_common.telemetry import TelemetryRecord

        # Exception without telemetry
        exc_without = SIPAPException("Error without telemetry")
        assert exc_without.has_telemetry() is False

        # Exception with telemetry
        record = TelemetryRecord(
            session_id="session_123",
            start_ts="2026-07-05T12:00:00+00:00",
            end_ts="2026-07-05T12:00:05+00:00",
            processing_time_ms=5000,
            status="error",
            prediction_type="1X2",
            match_id="match_123"
        )
        exc_with = SIPAPException("Error with telemetry", telemetry_record=record)
        assert exc_with.has_telemetry() is True

    def test_derived_exception_inherits_telemetry_support(self):
        """Test derived exceptions inherit telemetry support."""
        from sipap_common.exceptions import ValidationError
        from sipap_common.telemetry import TelemetryRecord

        record = TelemetryRecord(
            session_id="session_123",
            start_ts="2026-07-05T12:00:00+00:00",
            end_ts="2026-07-05T12:00:05+00:00",
            processing_time_ms=2000,
            status="error",
            prediction_type="1X2",
            match_id="match_123",
            error_type="validation_failed"
        )

        exc = ValidationError("Invalid match_id", telemetry_record=record)

        assert exc.has_telemetry() is True
        assert exc.telemetry_record.error_type == "validation_failed"

    def test_exception_telemetry_preserves_error_context(self):
        """Test telemetry record preserves error context."""
        from sipap_common.exceptions import DatabaseError
        from sipap_common.telemetry import TelemetryRecord

        record = TelemetryRecord(
            session_id="session_123",
            start_ts="2026-07-05T12:00:00+00:00",
            end_ts="2026-07-05T12:00:05+00:00",
            processing_time_ms=8000,
            status="error",
            prediction_type="BTTS",
            match_id="match_456",
            error_type="database_timeout",
            sources_used=["postgres", "redis"]
        )

        exc = DatabaseError("Query timeout", telemetry_record=record)

        # Verify all context is preserved
        assert exc.telemetry_record.processing_time_ms == 8000
        assert exc.telemetry_record.prediction_type == "BTTS"
        assert exc.telemetry_record.error_type == "database_timeout"
        assert exc.telemetry_record.sources_used == ["postgres", "redis"]

    def test_exception_str_includes_message_only(self):
        """Test exception string representation doesn't expose telemetry."""
        from sipap_common.exceptions import SIPAPException
        from sipap_common.telemetry import TelemetryRecord

        record = TelemetryRecord(
            session_id="session_123",
            start_ts="2026-07-05T12:00:00+00:00",
            end_ts="2026-07-05T12:00:05+00:00",
            processing_time_ms=5000,
            status="error",
            prediction_type="1X2",
            match_id="match_123"
        )

        exc = SIPAPException("User-friendly error message", telemetry_record=record)

        # String representation should only show message, not telemetry
        assert str(exc) == "User-friendly error message"
        assert "session_123" not in str(exc)

    def test_exception_can_be_raised_and_caught_with_telemetry(self):
        """Test exception with telemetry can be raised and caught."""
        from sipap_common.exceptions import CacheError
        from sipap_common.telemetry import TelemetryRecord

        record = TelemetryRecord(
            session_id="session_123",
            start_ts="2026-07-05T12:00:00+00:00",
            end_ts="2026-07-05T12:00:05+00:00",
            processing_time_ms=3000,
            status="error",
            prediction_type="1X2",
            match_id="match_123",
            error_type="cache_miss"
        )

        try:
            raise CacheError("Cache unavailable", telemetry_record=record)
        except CacheError as e:
            # Verify telemetry is accessible in except block
            assert e.has_telemetry() is True
            assert e.telemetry_record.error_type == "cache_miss"
            assert e.telemetry_record.processing_time_ms == 3000

    def test_get_telemetry_method_returns_record_or_none(self):
        """Test get_telemetry() convenience method."""
        from sipap_common.exceptions import SIPAPException
        from sipap_common.telemetry import TelemetryRecord

        # Exception without telemetry
        exc_without = SIPAPException("Error")
        assert exc_without.get_telemetry() is None

        # Exception with telemetry
        record = TelemetryRecord(
            session_id="session_123",
            start_ts="2026-07-05T12:00:00+00:00",
            end_ts="2026-07-05T12:00:05+00:00",
            processing_time_ms=5000,
            status="error",
            prediction_type="1X2",
            match_id="match_123"
        )
        exc_with = SIPAPException("Error", telemetry_record=record)
        retrieved = exc_with.get_telemetry()
        assert retrieved is not None
        assert retrieved.session_id == "session_123"
