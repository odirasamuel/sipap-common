"""Database connection management for SIPAP.

Provides SQLAlchemy-based PostgreSQL connection management with:
- Connection pooling (configurable)
- Session lifecycle management
- Error handling with DatabaseError
- Health check utilities
- Thread-safe operations
"""

from collections.abc import Generator
from contextlib import contextmanager
from typing import Any, cast

from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from sqlalchemy.exc import IntegrityError, OperationalError, SQLAlchemyError
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import NullPool

from sipap_common.exceptions import DatabaseError


class DatabaseManager:
    """Manages PostgreSQL database connections with SQLAlchemy.

    Provides connection pooling, session management, and error handling
    for PostgreSQL database operations.

    Attributes:
        engine: SQLAlchemy Engine instance
        SessionLocal: sessionmaker factory for creating sessions

    Examples:
        >>> # With connection pooling (production)
        >>> db = DatabaseManager("postgresql+psycopg2://user:pass@localhost/sipap")
        >>> with db.get_session() as session:
        ...     result = session.execute(text("SELECT 1")).scalar()

        >>> # Without pooling (serverless/Lambda)
        >>> db = DatabaseManager(
        ...     "postgresql+psycopg2://user:pass@localhost/sipap",
        ...     use_pool=False
        ... )

        >>> # As context manager
        >>> with DatabaseManager(database_url) as db:
        ...     with db.get_session() as session:
        ...         # Operations here
        ...         pass

        >>> # Health check
        >>> if db.health_check():
        ...     print("Database is accessible")
    """

    def __init__(
        self,
        database_url: str,
        pool_size: int = 20,
        max_overflow: int = 10,
        pool_timeout: int = 30,
        pool_recycle: int = 3600,
        echo: bool = False,
        use_pool: bool = True,
    ) -> None:
        """Initialize database manager with connection pooling.

        Args:
            database_url: SQLAlchemy database URL (e.g.,
                "postgresql+psycopg2://user:pass@host:5432/db")
            pool_size: Number of connections to maintain in pool (default 20)
            max_overflow: Additional connections when pool exhausted (default 10)
            pool_timeout: Seconds to wait for available connection (default 30)
            pool_recycle: Recycle connections after N seconds (default 3600)
            echo: Log all SQL statements (default False)
            use_pool: Use connection pooling (False for Lambda/serverless)

        Examples:
            >>> # Standard configuration
            >>> db = DatabaseManager("postgresql+psycopg2://user:pass@host/db")

            >>> # Custom pool sizing
            >>> db = DatabaseManager(
            ...     "postgresql+psycopg2://user:pass@host/db",
            ...     pool_size=50,
            ...     max_overflow=20
            ... )

            >>> # Lambda/serverless (no pooling)
            >>> db = DatabaseManager(
            ...     "postgresql+psycopg2://user:pass@host/db",
            ...     use_pool=False
            ... )
        """
        engine_kwargs: dict[str, Any] = {
            "echo": echo,
        }

        if use_pool:
            # Production: Use QueuePool with connection pooling
            engine_kwargs.update(
                {
                    "pool_size": pool_size,
                    "max_overflow": max_overflow,
                    "pool_timeout": pool_timeout,
                    "pool_recycle": pool_recycle,
                    "pool_pre_ping": True,  # Validate connections before use
                }
            )
        else:
            # Serverless/Lambda: Use NullPool (no connection persistence)
            engine_kwargs["poolclass"] = NullPool

        self.engine: Engine = create_engine(database_url, **engine_kwargs)

        self.SessionLocal = sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
        )

    @contextmanager
    def get_session(self) -> Generator[Session, None, None]:
        """Get database session with automatic lifecycle management.

        Context manager that ensures proper session lifecycle:
        - Creates new session
        - Commits on success
        - Rolls back on exception
        - Always closes session

        Yields:
            SQLAlchemy Session instance

        Raises:
            DatabaseError: On database operation failures

        Examples:
            >>> with db.get_session() as session:
            ...     result = session.execute(text("SELECT * FROM matches"))
            ...     # Automatically commits and closes

            >>> # On exception, automatically rolls back
            >>> try:
            ...     with db.get_session() as session:
            ...         session.execute(text("INVALID SQL"))
            ... except DatabaseError:
            ...     print("Operation failed and rolled back")
        """
        session = self.SessionLocal()
        try:
            yield session
            session.commit()
        except IntegrityError as e:
            session.rollback()
            raise DatabaseError(
                f"Data integrity violation: {e.orig if hasattr(e, 'orig') else e}"
            ) from e
        except OperationalError as e:
            session.rollback()
            raise DatabaseError(
                f"Database connection failed: {e.orig if hasattr(e, 'orig') else e}"
            ) from e
        except SQLAlchemyError as e:
            session.rollback()
            raise DatabaseError(f"Database operation failed: {e}") from e
        except Exception:
            # Rollback on any exception (not just SQLAlchemy exceptions)
            session.rollback()
            raise
        finally:
            session.close()

    def close(self) -> None:
        """Close database connection pool.

        Disposes all connections in the pool. Should be called when
        application is shutting down or database manager is no longer needed.

        Examples:
            >>> db = DatabaseManager(database_url)
            >>> try:
            ...     # Use database
            ...     pass
            ... finally:
            ...     db.close()
        """
        self.engine.dispose()

    def __enter__(self) -> "DatabaseManager":
        """Enter context manager."""
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """Exit context manager and dispose engine."""
        self.close()

    def health_check(self) -> bool:
        """Check database connectivity.

        Executes simple query to verify database is accessible.

        Returns:
            True if database is accessible, False otherwise

        Examples:
            >>> if db.health_check():
            ...     print("Database is healthy")
            ... else:
            ...     print("Database connection failed")
        """
        try:
            with self.get_session() as session:
                result = session.execute(text("SELECT 1"))
                return result.scalar() == 1
        except (DatabaseError, Exception):
            return False

    def execute_raw_sql(
        self, sql: str, params: dict[str, Any] | None = None
    ) -> list[Any]:
        """Execute raw SQL query and return results.

        WARNING: Use with caution. Prefer ORM queries for type safety.

        Args:
            sql: SQL query string (can use :param syntax for parameters)
            params: Dictionary of parameter values (default None)

        Returns:
            List of result rows

        Raises:
            DatabaseError: On query execution failure

        Examples:
            >>> # Simple query
            >>> results = db.execute_raw_sql("SELECT * FROM matches")

            >>> # Parameterized query
            >>> results = db.execute_raw_sql(
            ...     "SELECT * FROM matches WHERE sport = :sport",
            ...     {"sport": "soccer"}
            ... )
        """
        try:
            with self.get_session() as session:
                result = session.execute(text(sql), params or {})
                return cast(list[Any], result.fetchall())
        except DatabaseError:
            # Re-raise DatabaseError as-is
            raise
        except Exception as e:
            raise DatabaseError(f"Raw SQL execution failed: {e}") from e
