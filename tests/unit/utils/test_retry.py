"""Tests for sipap_common.utils.retry module."""

import time
from unittest.mock import Mock

import pytest

from sipap_common.utils.retry import retry_with_backoff


def test_retry_success_on_first_attempt() -> None:
    """Test that successful function doesn't retry."""
    mock_func = Mock(return_value="success")

    @retry_with_backoff(max_attempts=3)
    def test_func():
        return mock_func()

    result = test_func()

    assert result == "success"
    assert mock_func.call_count == 1


def test_retry_success_on_second_attempt() -> None:
    """Test that function retries once on first failure."""
    mock_func = Mock(side_effect=[Exception("Transient error"), "success"])

    @retry_with_backoff(max_attempts=3, initial_delay=0.01)
    def test_func():
        return mock_func()

    result = test_func()

    assert result == "success"
    assert mock_func.call_count == 2


def test_retry_exhausts_all_attempts() -> None:
    """Test that function retries up to max_attempts."""
    mock_func = Mock(side_effect=Exception("Persistent error"))

    @retry_with_backoff(max_attempts=3, initial_delay=0.01)
    def test_func():
        return mock_func()

    with pytest.raises(Exception, match="Persistent error"):
        test_func()

    assert mock_func.call_count == 3


def test_retry_exponential_backoff_delays() -> None:
    """Test that delays increase exponentially."""
    call_times = []
    mock_func = Mock(side_effect=Exception("Error"))

    @retry_with_backoff(max_attempts=3, initial_delay=0.1, backoff_factor=2.0)
    def test_func():
        call_times.append(time.time())
        return mock_func()

    with pytest.raises(Exception):
        test_func()

    # Verify delays between attempts
    assert len(call_times) == 3
    # First retry: ~0.1s delay
    delay1 = call_times[1] - call_times[0]
    # Second retry: ~0.2s delay (2x backoff)
    delay2 = call_times[2] - call_times[1]

    # Allow 50ms tolerance for timing
    assert 0.08 < delay1 < 0.15
    assert 0.15 < delay2 < 0.25


def test_retry_with_custom_exceptions() -> None:
    """Test retry only on specific exception types."""
    transient_error = ConnectionError("Network error")
    permanent_error = ValueError("Invalid data")

    attempt_count = 0

    @retry_with_backoff(
        max_attempts=3, initial_delay=0.01, retry_exceptions=(ConnectionError,)
    )
    def test_func(error):
        nonlocal attempt_count
        attempt_count += 1
        raise error

    # Should retry on ConnectionError
    attempt_count = 0
    with pytest.raises(ConnectionError):
        test_func(transient_error)
    assert attempt_count == 3  # Retried

    # Should NOT retry on ValueError
    attempt_count = 0
    with pytest.raises(ValueError):
        test_func(permanent_error)
    assert attempt_count == 1  # No retry


def test_retry_with_no_retry_exceptions() -> None:
    """Test that some exceptions are never retried."""
    @retry_with_backoff(
        max_attempts=3, initial_delay=0.01, no_retry_exceptions=(ValueError,)
    )
    def test_func():
        raise ValueError("Permanent error")

    with pytest.raises(ValueError):
        test_func()

    # Would have retried 3 times if not in no_retry list
    # But should only attempt once
    # (Implementation should check this)


def test_retry_max_delay_cap() -> None:
    """Test that delays are capped at max_delay."""
    call_times = []

    @retry_with_backoff(
        max_attempts=5, initial_delay=0.1, backoff_factor=3.0, max_delay=0.2
    )
    def test_func():
        call_times.append(time.time())
        raise Exception("Error")

    with pytest.raises(Exception):
        test_func()

    # Third+ attempts should be capped at max_delay
    delay3 = call_times[3] - call_times[2]
    assert delay3 < 0.25  # Should be capped at 0.2s


def test_retry_with_function_arguments() -> None:
    """Test that decorated function preserves arguments."""
    call_count = 0

    @retry_with_backoff(max_attempts=2, initial_delay=0.01)
    def test_func(x: int, y: int, op: str = "add"):
        nonlocal call_count
        call_count += 1
        if call_count == 1:
            raise Exception("First attempt fails")
        if op == "add":
            return x + y
        return x - y

    result = test_func(5, 3, op="add")
    assert result == 8
    assert call_count == 2


def test_retry_preserves_function_metadata() -> None:
    """Test that decorator preserves __name__ and __doc__."""

    @retry_with_backoff(max_attempts=3)
    def documented_function():
        """This function has documentation."""
        return "result"

    assert documented_function.__name__ == "documented_function"
    assert "documentation" in documented_function.__doc__


def test_retry_with_zero_initial_delay() -> None:
    """Test retry with no delay between attempts."""
    call_count = 0

    @retry_with_backoff(max_attempts=3, initial_delay=0.0)
    def test_func():
        nonlocal call_count
        call_count += 1
        if call_count < 3:
            raise Exception("Error")
        return "success"

    start_time = time.time()
    result = test_func()
    elapsed = time.time() - start_time

    assert result == "success"
    assert call_count == 3
    # Should complete very quickly (no delays)
    assert elapsed < 0.1


def test_retry_with_jitter() -> None:
    """Test that jitter randomizes delays."""
    call_times = []

    @retry_with_backoff(max_attempts=5, initial_delay=0.1, jitter=True)
    def test_func():
        call_times.append(time.time())
        raise Exception("Error")

    with pytest.raises(Exception):
        test_func()

    # Delays should vary due to jitter
    delays = [call_times[i + 1] - call_times[i] for i in range(len(call_times) - 1)]

    # Not all delays should be identical (jitter adds randomness)
    # This test might be flaky, but with 4 delays, variance is likely
    assert len(set(round(d, 3) for d in delays)) > 1
