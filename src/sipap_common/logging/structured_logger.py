"""Structured JSON logger with ContextVar-based context propagation.

Provides thread-safe and async-safe logging with automatic context injection.
Adapted from Sentinel's logging pattern.
"""

import json
import logging
from contextvars import ContextVar
from datetime import UTC, datetime
from typing import Any

# ContextVar storage for log context (thread-safe and async-safe)
_log_context: ContextVar[dict[str, Any]] = ContextVar("log_context", default={})


class JSONFormatter(logging.Formatter):
    """Formats log records as JSON with ISO 8601 timestamps."""

    def format(self, record: logging.LogRecord) -> str:
        """Format log record as JSON string.

        Args:
            record: Log record to format

        Returns:
            JSON string representation of log record
        """
        # Build base log data
        log_data: dict[str, Any] = {
            "timestamp": datetime.now(UTC).isoformat().replace("+00:00", "Z"),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }

        # Add context from ContextVar
        context = _log_context.get()
        if context:
            log_data.update(context)

        # Add extra fields from log call
        if hasattr(record, "extra_fields"):
            log_data.update(record.extra_fields)

        # Add exception info if present
        if record.exc_info:
            log_data["exception"] = self.formatException(record.exc_info)

        return json.dumps(log_data)


class ContextFilter(logging.Filter):
    """Logging filter that injects extra fields into log records."""

    def filter(self, record: logging.LogRecord) -> bool:
        """Add extra fields to log record.

        Args:
            record: Log record to modify

        Returns:
            Always True to allow all records through
        """
        # Extract extra fields that aren't standard logging attributes
        standard_attrs = {
            "name", "msg", "args", "created", "filename", "funcName",
            "levelname", "levelno", "lineno", "module", "msecs",
            "message", "pathname", "process", "processName", "relativeCreated",
            "thread", "threadName", "exc_info", "exc_text", "stack_info"
        }

        extra_fields = {}
        for key, value in record.__dict__.items():
            if key not in standard_attrs and not key.startswith("_"):
                extra_fields[key] = value

        if extra_fields:
            record.extra_fields = extra_fields

        return True


def get_logger(name: str) -> logging.Logger:
    """Get a configured logger with JSON formatting and context injection.

    Args:
        name: Logger name (typically __name__ of calling module)

    Returns:
        Configured logging.Logger instance

    Examples:
        >>> logger = get_logger(__name__)
        >>> logger.info("Processing match", extra={"match_id": "12345"})
        {"timestamp":"2026-06-08T12:00:00.000Z","level":"INFO","logger":"mymodule",
         "message":"Processing match","match_id":"12345"}
    """
    logger = logging.getLogger(name)

    # Only configure if not already configured
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(JSONFormatter())
        handler.addFilter(ContextFilter())
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

    return logger


def set_log_context(**kwargs: Any) -> None:
    """Set logging context for current thread/async task.

    Context is stored in ContextVar and automatically injected into all
    subsequent log calls in the same execution context.

    Args:
        **kwargs: Key-value pairs to add to logging context.
                  None values are ignored.

    Examples:
        >>> set_log_context(request_id="req-123", sport="soccer")
        >>> logger.info("Processing")
        {"timestamp":"...","level":"INFO","message":"Processing","request_id":"req-123","sport":"soccer"}
    """
    # Filter out None values
    context = {k: v for k, v in kwargs.items() if v is not None}

    # Update existing context
    current_context = _log_context.get().copy()
    current_context.update(context)
    _log_context.set(current_context)


def clear_log_context() -> None:
    """Clear all logging context for current thread/async task.

    Examples:
        >>> set_log_context(request_id="req-123")
        >>> clear_log_context()
        >>> logger.info("After clear")
        {"timestamp":"...","level":"INFO","message":"After clear"}
    """
    _log_context.set({})
