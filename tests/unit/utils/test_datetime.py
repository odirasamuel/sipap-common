"""Tests for sipap_common.utils.datetime module."""

from datetime import UTC, datetime

import pytest

from sipap_common.utils.datetime_utils import (
    add_seconds,
    current_timestamp,
    is_expired,
    parse_iso8601,
    subtract_timestamps,
)


def test_current_timestamp_format() -> None:
    """Test that current_timestamp returns ISO 8601 with Z suffix."""
    ts = current_timestamp()

    # Should end with Z
    assert ts.endswith("Z")

    # Should be parseable as ISO 8601
    dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
    assert dt.tzinfo == UTC


def test_current_timestamp_is_utc() -> None:
    """Test that current_timestamp returns UTC time."""
    ts = current_timestamp()
    dt = parse_iso8601(ts)

    # Should be within 1 second of now
    now = datetime.now(UTC)
    diff = abs((now - dt).total_seconds())
    assert diff < 1.0


def test_parse_iso8601_with_z_suffix() -> None:
    """Test parsing ISO 8601 timestamp with Z suffix."""
    ts = "2026-06-08T12:30:45.123456Z"
    dt = parse_iso8601(ts)

    assert dt.year == 2026
    assert dt.month == 6
    assert dt.day == 8
    assert dt.hour == 12
    assert dt.minute == 30
    assert dt.second == 45
    assert dt.microsecond == 123456
    assert dt.tzinfo == UTC


def test_parse_iso8601_with_plus_offset() -> None:
    """Test parsing ISO 8601 timestamp with +00:00 offset."""
    ts = "2026-06-08T12:30:45+00:00"
    dt = parse_iso8601(ts)

    assert dt.year == 2026
    assert dt.tzinfo == UTC


def test_parse_iso8601_without_microseconds() -> None:
    """Test parsing ISO 8601 timestamp without fractional seconds."""
    ts = "2026-06-08T12:30:45Z"
    dt = parse_iso8601(ts)

    assert dt.year == 2026
    assert dt.second == 45
    assert dt.microsecond == 0


def test_add_seconds_positive() -> None:
    """Test adding seconds to timestamp."""
    ts = "2026-06-08T12:00:00Z"
    result = add_seconds(ts, 3600)  # Add 1 hour

    expected = "2026-06-08T13:00:00Z"
    assert result == expected


def test_add_seconds_negative() -> None:
    """Test subtracting seconds from timestamp."""
    ts = "2026-06-08T12:00:00Z"
    result = add_seconds(ts, -3600)  # Subtract 1 hour

    expected = "2026-06-08T11:00:00Z"
    assert result == expected


def test_add_seconds_preserves_z_suffix() -> None:
    """Test that add_seconds preserves Z suffix."""
    ts = "2026-06-08T12:00:00.123456Z"
    result = add_seconds(ts, 60)

    assert result.endswith("Z")


def test_add_seconds_with_microseconds() -> None:
    """Test that add_seconds preserves microseconds."""
    ts = "2026-06-08T12:00:00.500000Z"
    result = add_seconds(ts, 1)

    dt = parse_iso8601(result)
    assert dt.microsecond == 500000


def test_subtract_timestamps_positive_duration() -> None:
    """Test calculating duration between two timestamps."""
    start = "2026-06-08T12:00:00Z"
    end = "2026-06-08T12:05:30Z"

    duration = subtract_timestamps(end, start)

    assert duration == 330.0  # 5 minutes 30 seconds


def test_subtract_timestamps_negative_duration() -> None:
    """Test calculating negative duration (end before start)."""
    start = "2026-06-08T12:05:30Z"
    end = "2026-06-08T12:00:00Z"

    duration = subtract_timestamps(end, start)

    assert duration == -330.0


def test_subtract_timestamps_same_time() -> None:
    """Test duration when timestamps are equal."""
    ts = "2026-06-08T12:00:00Z"

    duration = subtract_timestamps(ts, ts)

    assert duration == 0.0


def test_subtract_timestamps_with_microseconds() -> None:
    """Test precise duration calculation with microseconds."""
    start = "2026-06-08T12:00:00.000000Z"
    end = "2026-06-08T12:00:00.500000Z"

    duration = subtract_timestamps(end, start)

    assert duration == 0.5


def test_is_expired_not_expired() -> None:
    """Test that recent timestamp is not expired."""
    # Timestamp from 30 seconds ago
    ts = add_seconds(current_timestamp(), -30)

    # TTL of 60 seconds - should NOT be expired
    assert is_expired(ts, ttl_seconds=60) is False


def test_is_expired_is_expired() -> None:
    """Test that old timestamp is expired."""
    # Timestamp from 120 seconds ago
    ts = add_seconds(current_timestamp(), -120)

    # TTL of 60 seconds - should be expired
    assert is_expired(ts, ttl_seconds=60) is True


def test_is_expired_exact_boundary() -> None:
    """Test expiration at exact TTL boundary."""
    # Timestamp from exactly TTL seconds ago
    ts = add_seconds(current_timestamp(), -60)

    # Should be expired (boundary is inclusive)
    assert is_expired(ts, ttl_seconds=60) is True


def test_is_expired_future_timestamp() -> None:
    """Test that future timestamp is not expired."""
    # Timestamp 30 seconds in future
    ts = add_seconds(current_timestamp(), 30)

    # Should NOT be expired
    assert is_expired(ts, ttl_seconds=60) is False


def test_is_expired_with_microseconds() -> None:
    """Test expiration check with precise timestamps."""
    # Get very recent timestamp
    ts = current_timestamp()

    # With 1 second TTL, should not be expired yet
    assert is_expired(ts, ttl_seconds=1) is False

    # But with 0 second TTL, should be expired
    assert is_expired(ts, ttl_seconds=0) is True


def test_timestamp_roundtrip() -> None:
    """Test that parsing and formatting preserves timestamp."""
    original = "2026-06-08T12:30:45.123456Z"

    # Parse and format back
    dt = parse_iso8601(original)
    formatted = dt.isoformat().replace("+00:00", "Z")

    assert formatted == original


def test_add_seconds_handles_day_boundaries() -> None:
    """Test that add_seconds correctly handles day changes."""
    ts = "2026-06-08T23:00:00Z"
    result = add_seconds(ts, 7200)  # Add 2 hours

    expected = "2026-06-09T01:00:00Z"
    assert result == expected


def test_add_seconds_handles_month_boundaries() -> None:
    """Test that add_seconds correctly handles month changes."""
    ts = "2026-06-30T23:00:00Z"
    result = add_seconds(ts, 3600)  # Add 1 hour

    expected = "2026-07-01T00:00:00Z"
    assert result == expected


def test_subtract_timestamps_across_days() -> None:
    """Test duration calculation across day boundary."""
    start = "2026-06-08T23:00:00Z"
    end = "2026-06-09T01:00:00Z"

    duration = subtract_timestamps(end, start)

    assert duration == 7200.0  # 2 hours


def test_parse_iso8601_invalid_format() -> None:
    """Test that invalid ISO 8601 format raises error."""
    with pytest.raises(ValueError):
        parse_iso8601("not-a-timestamp")


def test_add_seconds_with_zero() -> None:
    """Test that adding zero seconds returns unchanged timestamp."""
    ts = "2026-06-08T12:00:00Z"
    result = add_seconds(ts, 0)

    assert result == ts
