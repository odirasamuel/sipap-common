"""
Exception hierarchy for SIPAP platform.

This module defines all custom exceptions used across the SIPAP platform,
providing a consistent error handling interface with optional telemetry support.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sipap_common.telemetry import TelemetryRecord


class SIPAPException(Exception):
    """
    Base exception for all SIPAP errors with optional telemetry support.

    All custom exceptions in the SIPAP platform should inherit from this class.
    This allows for catching all SIPAP-related errors with a single except clause.

    Telemetry Support:
    - Exceptions can carry partial telemetry data for failed predictions
    - Enables metrics capture even when errors occur
    - Use has_telemetry() to check if telemetry is present
    - Use get_telemetry() to retrieve telemetry record

    Example:
        >>> try:
        ...     raise SIPAPException("Something went wrong")
        ... except SIPAPException as e:
        ...     print(f"SIPAP error: {e}")

    Example with telemetry:
        >>> from sipap_common.telemetry import TelemetryRecord
        >>> record = TelemetryRecord(...)
        >>> raise SIPAPException("Prediction failed", telemetry_record=record)
    """

    def __init__(self, message: str, telemetry_record: "TelemetryRecord | None" = None):
        """
        Initialize exception with optional telemetry record.

        Args:
            message: Error message
            telemetry_record: Optional telemetry record for metrics capture
        """
        super().__init__(message)
        self.telemetry_record = telemetry_record

    def has_telemetry(self) -> bool:
        """
        Check if exception carries telemetry data.

        Returns:
            True if telemetry record is present, False otherwise
        """
        return self.telemetry_record is not None

    def get_telemetry(self) -> "TelemetryRecord | None":
        """
        Get telemetry record from exception.

        Returns:
            TelemetryRecord if present, None otherwise
        """
        return self.telemetry_record


class ConfigurationError(SIPAPException):
    """
    Raised when configuration is invalid or cannot be loaded.

    This includes errors in:
    - YAML parsing
    - Missing required configuration fields
    - Invalid configuration values
    - Environment variable substitution failures

    Example:
        >>> raise ConfigurationError("Missing required field: DATABASE_URL")
    """


class AWSServiceError(SIPAPException):
    """
    Raised when AWS service calls fail.

    This includes errors from:
    - boto3 client operations
    - AWS API rate limiting
    - Permission denied errors
    - Service unavailable errors

    Example:
        >>> raise AWSServiceError("Failed to invoke Lambda function: AccessDenied")
    """


class CacheError(SIPAPException):
    """
    Raised when cache operations fail.

    This includes errors from:
    - Redis connection failures
    - Cache key serialization/deserialization errors
    - TTL expiration issues

    Example:
        >>> raise CacheError("Redis connection timeout")
    """


class DatabaseError(SIPAPException):
    """
    Raised when database operations fail.

    This includes errors from:
    - SQL query execution
    - Connection pool exhaustion
    - Transaction commit/rollback failures
    - Database migration errors

    Example:
        >>> raise DatabaseError("Connection pool exhausted")
    """


class ValidationError(SIPAPException):
    """
    Raised when data validation fails.

    This includes errors from:
    - JSON Schema validation
    - TypedDict validation
    - Input sanitization failures
    - Business rule violations

    Example:
        >>> raise ValidationError("Field 'match_id' is required")
    """


class MCPError(SIPAPException):
    """
    Raised when MCP (Model Context Protocol) calls fail.

    This includes errors from:
    - MCP server connection failures
    - MCP tool execution errors
    - MCP server timeout
    - Invalid MCP responses

    Example:
        >>> raise MCPError("MCP server 'data' failed to respond: timeout")
    """


class AgentError(SIPAPException):
    """
    Raised when AI agent execution fails.

    This includes errors from:
    - Agent initialization failures
    - Agent prediction errors
    - Agent tool execution failures
    - Invalid agent outputs

    Example:
        >>> raise AgentError("Statistical agent failed: invalid prediction format")
    """


class PredictionError(SIPAPException):
    """
    Raised when prediction generation fails.

    This includes errors from:
    - Insufficient context quality
    - Ensemble calculation failures
    - Quality gate failures
    - Expected value calculation errors

    Example:
        >>> raise PredictionError("Ensemble prediction failed: insufficient agent consensus")
    """
