"""
Exception hierarchy for SIPAP platform.

This module defines all custom exceptions used across the SIPAP platform,
providing a consistent error handling interface.
"""


class SIPAPException(Exception):
    """
    Base exception for all SIPAP errors.

    All custom exceptions in the SIPAP platform should inherit from this class.
    This allows for catching all SIPAP-related errors with a single except clause.

    Example:
        >>> try:
        ...     raise SIPAPException("Something went wrong")
        ... except SIPAPException as e:
        ...     print(f"SIPAP error: {e}")
    """

    pass


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

    pass


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

    pass


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

    pass


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

    pass


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

    pass
