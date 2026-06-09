"""Tests for sipap_common.exceptions module."""

import pytest

from sipap_common.exceptions import (
    AWSServiceError,
    CacheError,
    ConfigurationError,
    DatabaseError,
    SIPAPException,
    ValidationError,
)


class TestSIPAPException:
    """Tests for base SIPAPException."""

    def test_sipap_exception_is_exception(self):
        """Verify SIPAPException inherits from Exception."""
        assert issubclass(SIPAPException, Exception)

    def test_sipap_exception_can_be_raised(self):
        """Verify SIPAPException can be raised with a message."""
        with pytest.raises(SIPAPException, match="Test error"):
            raise SIPAPException("Test error")

    def test_sipap_exception_str_representation(self):
        """Verify SIPAPException has correct string representation."""
        exc = SIPAPException("Test error message")
        assert str(exc) == "Test error message"


class TestConfigurationError:
    """Tests for ConfigurationError."""

    def test_configuration_error_inherits_from_sipap_exception(self):
        """Verify ConfigurationError inherits from SIPAPException."""
        assert issubclass(ConfigurationError, SIPAPException)

    def test_configuration_error_can_be_raised(self):
        """Verify ConfigurationError can be raised."""
        with pytest.raises(ConfigurationError, match="Invalid config"):
            raise ConfigurationError("Invalid config")

    def test_configuration_error_caught_as_sipap_exception(self):
        """Verify ConfigurationError can be caught as SIPAPException."""
        with pytest.raises(SIPAPException):
            raise ConfigurationError("Config error")


class TestAWSServiceError:
    """Tests for AWSServiceError."""

    def test_aws_service_error_inherits_from_sipap_exception(self):
        """Verify AWSServiceError inherits from SIPAPException."""
        assert issubclass(AWSServiceError, SIPAPException)

    def test_aws_service_error_can_be_raised(self):
        """Verify AWSServiceError can be raised."""
        with pytest.raises(AWSServiceError, match="AWS call failed"):
            raise AWSServiceError("AWS call failed")


class TestCacheError:
    """Tests for CacheError."""

    def test_cache_error_inherits_from_sipap_exception(self):
        """Verify CacheError inherits from SIPAPException."""
        assert issubclass(CacheError, SIPAPException)

    def test_cache_error_can_be_raised(self):
        """Verify CacheError can be raised."""
        with pytest.raises(CacheError, match="Cache operation failed"):
            raise CacheError("Cache operation failed")


class TestDatabaseError:
    """Tests for DatabaseError."""

    def test_database_error_inherits_from_sipap_exception(self):
        """Verify DatabaseError inherits from SIPAPException."""
        assert issubclass(DatabaseError, SIPAPException)

    def test_database_error_can_be_raised(self):
        """Verify DatabaseError can be raised."""
        with pytest.raises(DatabaseError, match="DB query failed"):
            raise DatabaseError("DB query failed")


class TestValidationError:
    """Tests for ValidationError."""

    def test_validation_error_inherits_from_sipap_exception(self):
        """Verify ValidationError inherits from SIPAPException."""
        assert issubclass(ValidationError, SIPAPException)

    def test_validation_error_can_be_raised(self):
        """Verify ValidationError can be raised."""
        with pytest.raises(ValidationError, match="Invalid data"):
            raise ValidationError("Invalid data")


class TestExceptionHierarchy:
    """Tests for exception hierarchy."""

    def test_all_exceptions_caught_by_base_exception(self):
        """Verify all custom exceptions can be caught by SIPAPException."""
        exceptions_to_test = [
            ConfigurationError("test"),
            AWSServiceError("test"),
            CacheError("test"),
            DatabaseError("test"),
            ValidationError("test"),
        ]

        for exc in exceptions_to_test:
            with pytest.raises(SIPAPException):
                raise exc

    def test_exception_with_detailed_message(self):
        """Verify exceptions can carry detailed error messages."""
        detailed_message = "Failed to load config from /path/to/config.yml: File not found"
        exc = ConfigurationError(detailed_message)
        assert str(exc) == detailed_message
