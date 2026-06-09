"""Datetime utilities for SIPAP.

Provides timezone-aware datetime handling with ISO 8601 UTC-focused design.
All functions use ISO 8601 format with Z suffix for consistency.
"""

from datetime import UTC, datetime, timedelta


def current_timestamp() -> str:
    """Get current UTC timestamp in ISO 8601 format with Z suffix.

    Returns:
        ISO 8601 timestamp string (e.g., "2026-06-08T12:30:45.123456Z")

    Examples:
        >>> ts = current_timestamp()
        >>> ts.endswith('Z')
        True
    """
    return datetime.now(UTC).isoformat().replace("+00:00", "Z")


def parse_iso8601(timestamp: str) -> datetime:
    """Parse ISO 8601 timestamp string to datetime object.

    Args:
        timestamp: ISO 8601 timestamp with Z suffix or +00:00 offset

    Returns:
        Timezone-aware datetime object in UTC

    Raises:
        ValueError: If timestamp format is invalid

    Examples:
        >>> dt = parse_iso8601("2026-06-08T12:30:45Z")
        >>> dt.year
        2026
        >>> dt.tzinfo
        datetime.timezone.utc
    """
    # Replace Z with +00:00 for Python's fromisoformat
    normalized = timestamp.replace("Z", "+00:00")
    return datetime.fromisoformat(normalized)


def add_seconds(timestamp: str, seconds: int) -> str:
    """Add or subtract seconds from an ISO 8601 timestamp.

    Args:
        timestamp: ISO 8601 timestamp string
        seconds: Number of seconds to add (negative to subtract)

    Returns:
        New ISO 8601 timestamp string with Z suffix

    Examples:
        >>> add_seconds("2026-06-08T12:00:00Z", 3600)
        '2026-06-08T13:00:00Z'

        >>> add_seconds("2026-06-08T12:00:00Z", -1800)
        '2026-06-08T11:30:00Z'
    """
    dt = parse_iso8601(timestamp)
    new_dt = dt + timedelta(seconds=seconds)
    return new_dt.isoformat().replace("+00:00", "Z")


def subtract_timestamps(end: str, start: str) -> float:
    """Calculate duration in seconds between two timestamps.

    Args:
        end: End timestamp in ISO 8601 format
        start: Start timestamp in ISO 8601 format

    Returns:
        Duration in seconds (positive if end > start, negative if end < start)

    Examples:
        >>> subtract_timestamps("2026-06-08T12:05:00Z", "2026-06-08T12:00:00Z")
        300.0

        >>> # Microsecond precision
        >>> subtract_timestamps("2026-06-08T12:00:00.500000Z", "2026-06-08T12:00:00.000000Z")
        0.5
    """
    end_dt = parse_iso8601(end)
    start_dt = parse_iso8601(start)
    return (end_dt - start_dt).total_seconds()


def is_expired(timestamp: str, ttl_seconds: int) -> bool:
    """Check if a timestamp has expired based on TTL.

    Args:
        timestamp: ISO 8601 timestamp to check
        ttl_seconds: Time-to-live in seconds

    Returns:
        True if timestamp + TTL is in the past, False otherwise

    Examples:
        >>> # Recent timestamp with 60s TTL
        >>> ts = add_seconds(current_timestamp(), -30)
        >>> is_expired(ts, ttl_seconds=60)
        False

        >>> # Old timestamp with 60s TTL
        >>> ts = add_seconds(current_timestamp(), -120)
        >>> is_expired(ts, ttl_seconds=60)
        True
    """
    creation_dt = parse_iso8601(timestamp)
    expiration_dt = creation_dt + timedelta(seconds=ttl_seconds)
    now_dt = datetime.now(UTC)
    return now_dt >= expiration_dt
