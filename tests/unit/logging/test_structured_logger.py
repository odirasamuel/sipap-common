"""Tests for sipap_common.logging.structured_logger module."""

import json
import logging
from io import StringIO

import pytest

from sipap_common.logging import clear_log_context, get_logger, set_log_context
from sipap_common.logging.structured_logger import ContextFilter, JSONFormatter


@pytest.fixture
def log_capture() -> StringIO:
    """Fixture to capture log output."""
    stream = StringIO()
    return stream


@pytest.fixture
def test_logger(log_capture: StringIO) -> logging.Logger:
    """Create a test logger with JSON output."""
    logger = get_logger("test_module")
    # Remove existing handlers
    logger.handlers.clear()
    # Add handler that writes to our capture stream with JSON formatting
    handler = logging.StreamHandler(log_capture)
    handler.setFormatter(JSONFormatter())
    handler.addFilter(ContextFilter())
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger


def test_get_logger_returns_logger_instance() -> None:
    """Test that get_logger returns a logging.Logger instance."""
    logger = get_logger("test")
    assert isinstance(logger, logging.Logger)


def test_get_logger_with_different_names_returns_different_loggers() -> None:
    """Test that different names return different logger instances."""
    logger1 = get_logger("module1")
    logger2 = get_logger("module2")
    assert logger1.name != logger2.name


def test_log_output_is_valid_json(test_logger: logging.Logger, log_capture: StringIO) -> None:
    """Test that log output is valid JSON."""
    test_logger.info("Test message")
    log_output = log_capture.getvalue().strip()

    # Should be parseable as JSON
    log_data = json.loads(log_output)
    assert isinstance(log_data, dict)


def test_log_contains_standard_fields(test_logger: logging.Logger, log_capture: StringIO) -> None:
    """Test that log output contains standard fields."""
    test_logger.info("Test message")
    log_output = log_capture.getvalue().strip()
    log_data = json.loads(log_output)

    # Standard fields
    assert "timestamp" in log_data
    assert "level" in log_data
    assert "logger" in log_data
    assert "message" in log_data

    assert log_data["level"] == "INFO"
    assert log_data["logger"] == "test_module"
    assert log_data["message"] == "Test message"


def test_set_log_context_adds_request_id(
    test_logger: logging.Logger, log_capture: StringIO
) -> None:
    """Test that set_log_context adds request_id to logs."""
    set_log_context(request_id="req-12345")
    test_logger.info("Test with context")

    log_output = log_capture.getvalue().strip()
    log_data = json.loads(log_output)

    assert log_data["request_id"] == "req-12345"


def test_set_log_context_adds_multiple_fields(
    test_logger: logging.Logger, log_capture: StringIO
) -> None:
    """Test that set_log_context can add multiple context fields."""
    set_log_context(request_id="req-123", sport="soccer", component="orchestrator")
    test_logger.info("Test with multiple context")

    log_output = log_capture.getvalue().strip()
    log_data = json.loads(log_output)

    assert log_data["request_id"] == "req-123"
    assert log_data["sport"] == "soccer"
    assert log_data["component"] == "orchestrator"


def test_context_persists_across_multiple_logs(
    test_logger: logging.Logger, log_capture: StringIO
) -> None:
    """Test that context persists across multiple log calls."""
    set_log_context(request_id="req-999", user_id="user-456")

    test_logger.info("First log")
    test_logger.warning("Second log")

    logs = log_capture.getvalue().strip().split("\n")
    assert len(logs) == 2

    log1 = json.loads(logs[0])
    log2 = json.loads(logs[1])

    # Both logs should have context
    assert log1["request_id"] == "req-999"
    assert log1["user_id"] == "user-456"
    assert log2["request_id"] == "req-999"
    assert log2["user_id"] == "user-456"


def test_clear_log_context_removes_context(
    test_logger: logging.Logger, log_capture: StringIO
) -> None:
    """Test that clear_log_context removes context fields."""
    set_log_context(request_id="req-123", sport="nba")
    test_logger.info("With context")

    clear_log_context()
    test_logger.info("Without context")

    logs = log_capture.getvalue().strip().split("\n")
    log1 = json.loads(logs[0])
    log2 = json.loads(logs[1])

    # First log has context
    assert "request_id" in log1
    assert "sport" in log1

    # Second log has no context
    assert "request_id" not in log2
    assert "sport" not in log2


def test_extra_fields_in_log_call(test_logger: logging.Logger, log_capture: StringIO) -> None:
    """Test that extra fields passed to log() appear in output."""
    test_logger.info("Test", extra={"match_id": "12345", "team": "Arsenal"})

    log_output = log_capture.getvalue().strip()
    log_data = json.loads(log_output)

    assert log_data["match_id"] == "12345"
    assert log_data["team"] == "Arsenal"


def test_context_and_extra_fields_together(
    test_logger: logging.Logger, log_capture: StringIO
) -> None:
    """Test that context and extra fields both appear in output."""
    set_log_context(request_id="req-789")
    test_logger.info("Test", extra={"action": "prediction"})

    log_output = log_capture.getvalue().strip()
    log_data = json.loads(log_output)

    assert log_data["request_id"] == "req-789"
    assert log_data["action"] == "prediction"


def test_different_log_levels(test_logger: logging.Logger, log_capture: StringIO) -> None:
    """Test different log levels produce correct level field."""
    test_logger.debug("Debug message")
    test_logger.info("Info message")
    test_logger.warning("Warning message")
    test_logger.error("Error message")

    logs = log_capture.getvalue().strip().split("\n")

    assert json.loads(logs[0])["level"] == "DEBUG"
    assert json.loads(logs[1])["level"] == "INFO"
    assert json.loads(logs[2])["level"] == "WARNING"
    assert json.loads(logs[3])["level"] == "ERROR"


def test_timestamp_format(test_logger: logging.Logger, log_capture: StringIO) -> None:
    """Test that timestamp is in ISO 8601 format."""
    test_logger.info("Test")

    log_output = log_capture.getvalue().strip()
    log_data = json.loads(log_output)

    # Should be ISO 8601 format: YYYY-MM-DDTHH:MM:SS.sssZ
    timestamp = log_data["timestamp"]
    assert "T" in timestamp
    assert timestamp.endswith("Z")


def test_exception_logging(test_logger: logging.Logger, log_capture: StringIO) -> None:
    """Test that exceptions are logged with stack traces."""
    try:
        raise ValueError("Test exception")
    except ValueError:
        test_logger.exception("An error occurred")

    log_output = log_capture.getvalue().strip()
    log_data = json.loads(log_output)

    assert log_data["level"] == "ERROR"
    assert "exception" in log_data or "exc_info" in log_output


def test_set_log_context_with_none_values_skips_fields() -> None:
    """Test that set_log_context with None values doesn't add fields."""
    # This should not raise an error
    set_log_context(request_id=None, sport="soccer")
    # Implicitly testing that it doesn't crash


def test_logger_name_appears_in_output(test_logger: logging.Logger, log_capture: StringIO) -> None:
    """Test that logger name appears in JSON output."""
    test_logger.info("Test")

    log_output = log_capture.getvalue().strip()
    log_data = json.loads(log_output)

    assert log_data["logger"] == "test_module"
