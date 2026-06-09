"""Tests for sipap_common.database.manager module."""

from collections.abc import Generator
from unittest.mock import Mock, patch

import pytest
from sqlalchemy.exc import IntegrityError, OperationalError, SQLAlchemyError
from sqlalchemy.orm import Session

from sipap_common.database.manager import DatabaseManager
from sipap_common.exceptions import DatabaseError


@pytest.fixture
def database_url() -> str:
    """Return test database URL."""
    return "postgresql+psycopg2://test_user:test_pass@localhost:5432/test_db"


@pytest.fixture
def mock_engine() -> Mock:
    """Create mock SQLAlchemy engine."""
    engine = Mock()
    engine.dispose = Mock()
    return engine


@pytest.fixture
def mock_session() -> Mock:
    """Create mock SQLAlchemy session."""
    session = Mock(spec=Session)
    session.commit = Mock()
    session.rollback = Mock()
    session.close = Mock()
    session.execute = Mock()
    session.query = Mock()
    return session


@pytest.fixture
def mock_session_maker(mock_session: Mock) -> Mock:
    """Create mock sessionmaker that returns mock session."""
    maker = Mock(return_value=mock_session)
    return maker


@pytest.fixture
def db_manager(
    database_url: str, mock_engine: Mock, mock_session_maker: Mock
) -> Generator[DatabaseManager, None, None]:
    """Create DatabaseManager with mocked engine and session."""
    with patch("sipap_common.database.manager.create_engine", return_value=mock_engine):
        with patch(
            "sipap_common.database.manager.sessionmaker", return_value=mock_session_maker
        ):
            manager = DatabaseManager(database_url)
            yield manager


# ========================================
# Initialization Tests
# ========================================


def test_database_manager_initialization(database_url: str) -> None:
    """Test DatabaseManager initializes with correct parameters."""
    with patch("sipap_common.database.manager.create_engine") as mock_create_engine:
        with patch("sipap_common.database.manager.sessionmaker"):
            DatabaseManager(database_url)

            # Verify engine created with correct URL
            mock_create_engine.assert_called_once()
            call_args = mock_create_engine.call_args
            assert call_args[0][0] == database_url

            # Verify pooling parameters
            assert call_args[1]["pool_size"] == 20
            assert call_args[1]["max_overflow"] == 10
            assert call_args[1]["pool_timeout"] == 30
            assert call_args[1]["pool_recycle"] == 3600
            assert call_args[1]["pool_pre_ping"] is True
            assert call_args[1]["echo"] is False


def test_database_manager_custom_pool_config(database_url: str) -> None:
    """Test DatabaseManager accepts custom pool configuration."""
    with patch("sipap_common.database.manager.create_engine") as mock_create_engine:
        with patch("sipap_common.database.manager.sessionmaker"):
            DatabaseManager(
                database_url,
                pool_size=50,
                max_overflow=20,
                pool_timeout=60,
                pool_recycle=7200,
                echo=True,
            )

            call_args = mock_create_engine.call_args
            assert call_args[1]["pool_size"] == 50
            assert call_args[1]["max_overflow"] == 20
            assert call_args[1]["pool_timeout"] == 60
            assert call_args[1]["pool_recycle"] == 7200
            assert call_args[1]["echo"] is True


def test_database_manager_null_pool_mode(database_url: str) -> None:
    """Test DatabaseManager can use NullPool for serverless environments."""
    with patch("sipap_common.database.manager.create_engine") as mock_create_engine:
        with patch("sipap_common.database.manager.sessionmaker"):
            with patch("sipap_common.database.manager.NullPool") as mock_null_pool:
                DatabaseManager(database_url, use_pool=False)

                call_args = mock_create_engine.call_args
                assert call_args[1]["poolclass"] == mock_null_pool


# ========================================
# Session Lifecycle Tests
# ========================================


def test_get_session_returns_session(
    db_manager: DatabaseManager, mock_session: Mock
) -> None:
    """Test get_session returns a session context manager."""
    with db_manager.get_session() as session:
        assert session == mock_session


def test_get_session_commits_on_success(
    db_manager: DatabaseManager, mock_session: Mock
) -> None:
    """Test session commits on successful operation."""
    with db_manager.get_session() as session:
        session.execute("SELECT 1")

    mock_session.commit.assert_called_once()
    mock_session.close.assert_called_once()
    mock_session.rollback.assert_not_called()


def test_get_session_rollsback_on_exception(
    db_manager: DatabaseManager, mock_session: Mock
) -> None:
    """Test session rolls back on exception."""
    with pytest.raises(ValueError):
        with db_manager.get_session():
            raise ValueError("Test error")

    mock_session.rollback.assert_called_once()
    mock_session.close.assert_called_once()
    mock_session.commit.assert_not_called()


def test_get_session_closes_session_even_on_exception(
    db_manager: DatabaseManager, mock_session: Mock
) -> None:
    """Test session is closed even if exception occurs."""
    with pytest.raises(RuntimeError):
        with db_manager.get_session():
            raise RuntimeError("Database error")

    # Session should be closed regardless of exception
    mock_session.close.assert_called_once()


def test_get_session_multiple_operations(
    db_manager: DatabaseManager, mock_session: Mock
) -> None:
    """Test session can perform multiple operations."""
    with db_manager.get_session() as session:
        session.execute("INSERT INTO table VALUES (1)")
        session.execute("INSERT INTO table VALUES (2)")
        session.execute("INSERT INTO table VALUES (3)")

    # All operations should commit together
    mock_session.commit.assert_called_once()
    assert session.execute.call_count == 3


# ========================================
# Error Handling Tests
# ========================================


def test_get_session_wraps_integrity_error(
    db_manager: DatabaseManager, mock_session: Mock
) -> None:
    """Test IntegrityError is wrapped in DatabaseError."""
    mock_session.commit.side_effect = IntegrityError("statement", "params", "orig")

    with pytest.raises(DatabaseError) as exc_info:
        with db_manager.get_session():
            pass

    assert "integrity" in str(exc_info.value).lower()
    mock_session.rollback.assert_called_once()


def test_get_session_wraps_operational_error(
    db_manager: DatabaseManager, mock_session: Mock
) -> None:
    """Test OperationalError is wrapped in DatabaseError."""
    mock_session.commit.side_effect = OperationalError("statement", "params", "orig")

    with pytest.raises(DatabaseError) as exc_info:
        with db_manager.get_session():
            pass

    assert "connection" in str(exc_info.value).lower()
    mock_session.rollback.assert_called_once()


def test_get_session_wraps_generic_sqlalchemy_error(
    db_manager: DatabaseManager, mock_session: Mock
) -> None:
    """Test generic SQLAlchemyError is wrapped in DatabaseError."""
    mock_session.commit.side_effect = SQLAlchemyError("Database error")

    with pytest.raises(DatabaseError) as exc_info:
        with db_manager.get_session():
            pass

    assert "operation failed" in str(exc_info.value).lower()
    mock_session.rollback.assert_called_once()


def test_get_session_preserves_original_exception(
    db_manager: DatabaseManager, mock_session: Mock
) -> None:
    """Test original exception is preserved as cause."""
    original_error = IntegrityError("statement", "params", "orig")
    mock_session.commit.side_effect = original_error

    with pytest.raises(DatabaseError) as exc_info:
        with db_manager.get_session():
            pass

    # Original exception should be preserved in __cause__
    assert exc_info.value.__cause__ == original_error


# ========================================
# Connection Management Tests
# ========================================


def test_close_disposes_engine(db_manager: DatabaseManager, mock_engine: Mock) -> None:
    """Test close() disposes the engine."""
    db_manager.close()

    mock_engine.dispose.assert_called_once()


def test_context_manager_closes_on_exit(
    database_url: str, mock_engine: Mock
) -> None:
    """Test DatabaseManager as context manager closes on exit."""
    with patch("sipap_common.database.manager.create_engine", return_value=mock_engine):
        with patch("sipap_common.database.manager.sessionmaker"):
            with DatabaseManager(database_url):
                pass  # Just enter and exit context

    mock_engine.dispose.assert_called_once()


def test_context_manager_closes_on_exception(
    database_url: str, mock_engine: Mock
) -> None:
    """Test DatabaseManager context manager closes even on exception."""
    with patch("sipap_common.database.manager.create_engine", return_value=mock_engine):
        with patch("sipap_common.database.manager.sessionmaker"):
            with pytest.raises(RuntimeError):
                with DatabaseManager(database_url):
                    raise RuntimeError("Test error")

    # Engine should be disposed even on exception
    mock_engine.dispose.assert_called_once()


# ========================================
# Utility Method Tests
# ========================================


def test_health_check_success(db_manager: DatabaseManager, mock_session: Mock) -> None:
    """Test health_check returns True when database is accessible."""
    mock_result = Mock()
    mock_result.scalar.return_value = 1
    mock_session.execute.return_value = mock_result

    result = db_manager.health_check()

    assert result is True
    mock_session.execute.assert_called_once()


def test_health_check_failure(db_manager: DatabaseManager, mock_session: Mock) -> None:
    """Test health_check returns False on database error."""
    mock_session.execute.side_effect = OperationalError("statement", "params", "orig")

    result = db_manager.health_check()

    assert result is False


def test_execute_raw_sql_success(
    db_manager: DatabaseManager, mock_session: Mock
) -> None:
    """Test execute_raw_sql executes SQL and returns result."""
    mock_result = Mock()
    mock_result.fetchall.return_value = [{"id": 1}, {"id": 2}]
    mock_session.execute.return_value = mock_result

    result = db_manager.execute_raw_sql("SELECT * FROM table")

    assert result == [{"id": 1}, {"id": 2}]
    mock_session.execute.assert_called_once()


def test_execute_raw_sql_with_params(
    db_manager: DatabaseManager, mock_session: Mock
) -> None:
    """Test execute_raw_sql accepts parameters."""
    mock_result = Mock()
    mock_result.fetchall.return_value = []
    mock_session.execute.return_value = mock_result

    db_manager.execute_raw_sql("SELECT * FROM table WHERE id = :id", {"id": 1})

    call_args = mock_session.execute.call_args
    assert "id" in str(call_args)


def test_execute_raw_sql_error_handling(
    db_manager: DatabaseManager, mock_session: Mock
) -> None:
    """Test execute_raw_sql raises DatabaseError on failure."""
    mock_session.execute.side_effect = SQLAlchemyError("Query error")

    with pytest.raises(DatabaseError):
        db_manager.execute_raw_sql("INVALID SQL")


# ========================================
# Thread Safety Tests
# ========================================


def test_multiple_sessions_are_independent(
    db_manager: DatabaseManager, mock_session_maker: Mock
) -> None:
    """Test multiple sessions are independent instances."""
    # Reset call count
    mock_session_maker.reset_mock()

    with db_manager.get_session():
        pass

    with db_manager.get_session():
        pass

    # Should create two separate sessions
    assert mock_session_maker.call_count == 2


# ========================================
# URL Construction Tests
# ========================================


def test_database_url_parsing() -> None:
    """Test database URL is parsed correctly."""
    url = "postgresql+psycopg2://user:pass@host:5432/db"

    with patch("sipap_common.database.manager.create_engine") as mock_create:
        with patch("sipap_common.database.manager.sessionmaker"):
            DatabaseManager(url)

            # Verify URL passed correctly
            assert mock_create.call_args[0][0] == url


def test_database_url_without_password() -> None:
    """Test database URL works without password."""
    url = "postgresql+psycopg2://user@host:5432/db"

    with patch("sipap_common.database.manager.create_engine") as mock_create:
        with patch("sipap_common.database.manager.sessionmaker"):
            DatabaseManager(url)

            assert mock_create.call_args[0][0] == url
