"""Database connection management module for SIPAP.

Provides PostgreSQL connection management via SQLAlchemy with connection
pooling, session lifecycle management, and error handling.
"""

from sipap_common.database.manager import DatabaseManager

__all__ = [
    "DatabaseManager",
]
