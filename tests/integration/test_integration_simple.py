"""Simplified integration tests for core module interactions."""

import tempfile
from pathlib import Path

import fakeredis
import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.pool import StaticPool

from sipap_common.cache import RedisCache, cache_result
from sipap_common.config import load_config
from sipap_common.database import DatabaseManager
from sipap_common.exceptions import DatabaseError
from sipap_common.logging import get_logger
from sipap_common.utils import (
    current_timestamp,
    retry_with_backoff,
    safe_json_dumps,
    safe_json_loads,
)


# ========================================
# Config Integration Tests
# ========================================


def test_config_with_env_substitution():
    """Test config loads with environment variable substitution."""
    config_content = """
database:
  host: ${ DB_HOST }
  port: ${ DB_PORT }
"""

    with tempfile.NamedTemporaryFile(mode="w", suffix=".yml", delete=False) as f:
        f.write(config_content)
        config_path = f.name

    try:
        config = load_config(config_path, env_vars={"DB_HOST": "localhost", "DB_PORT": "5432"})
        assert config["database"]["host"] == "localhost"
        assert config["database"]["port"] == 5432
    finally:
        Path(config_path).unlink()


def test_config_with_nested_structure():
    """Test config with complex nested structure."""
    config_content = """
aws:
  region: us-east-1
  services:
    s3:
      bucket: sipap-data

cache:
  enabled: true
  ttl: 300
"""

    with tempfile.NamedTemporaryFile(mode="w", suffix=".yml", delete=False) as f:
        f.write(config_content)
        config_path = f.name

    try:
        config = load_config(config_path)
        assert config["aws"]["region"] == "us-east-1"
        assert config["cache"]["ttl"] == 300
    finally:
        Path(config_path).unlink()


# ========================================
# Cache Integration Tests
# ========================================


@pytest.fixture
def test_cache():
    """Create test cache with fake Redis."""
    fake_redis = fakeredis.FakeRedis(decode_responses=True)
    cache = RedisCache.__new__(RedisCache)
    cache.redis_client = fake_redis
    cache.default_ttl = 300
    cache.fail_silently = False
    return cache


def test_cache_stores_json_data(test_cache):
    """Test cache stores and retrieves JSON data."""
    data = {"match_id": "M001", "score": [2, 1]}

    test_cache.set("match:M001", data)
    result = test_cache.get("match:M001")

    assert result == data


def test_cache_decorator_basic(test_cache):
    """Test cache decorator caches function results."""
    call_count = 0

    @cache_result(redis_client=test_cache.redis_client, ttl=60)
    def expensive_function(x: int) -> int:
        nonlocal call_count
        call_count += 1
        return x * 2

    # First call
    result1 = expensive_function(5)
    assert result1 == 10
    assert call_count == 1

    # Second call - cached
    result2 = expensive_function(5)
    assert result2 == 10
    assert call_count == 1  # Not called again


def test_cache_with_timestamps(test_cache):
    """Test cache stores timestamps correctly."""
    ts = current_timestamp()
    data = {"timestamp": ts}

    test_cache.set("event:1", data)
    result = test_cache.get("event:1")

    assert result["timestamp"] == ts
    assert result["timestamp"].endswith("Z")


# ========================================
# Database Integration Tests
# ========================================


@pytest.fixture
def test_db():
    """Create in-memory test database."""
    engine = create_engine("sqlite:///:memory:", poolclass=StaticPool, connect_args={"check_same_thread": False})

    # Create test table
    with engine.connect() as conn:
        conn.execute(
            text(
                """
            CREATE TABLE predictions (
                id INTEGER PRIMARY KEY,
                match_id TEXT NOT NULL,
                data TEXT NOT NULL
            )
        """
            )
        )
        conn.commit()

    db = DatabaseManager.__new__(DatabaseManager)
    db.engine = engine
    from sqlalchemy.orm import sessionmaker

    db.SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

    yield db

    engine.dispose()


def test_database_insert_and_query(test_db):
    """Test database insert and query operations."""
    # Insert data
    with test_db.get_session() as session:
        session.execute(text("INSERT INTO predictions (match_id, data) VALUES ('M001', 'test_data')"))

    # Query data
    with test_db.get_session() as session:
        result = session.execute(text("SELECT * FROM predictions WHERE match_id = 'M001'")).fetchone()
        assert result is not None
        assert result[1] == "M001"


def test_database_with_json_utils(test_db):
    """Test database stores JSON-serialized data."""
    data = {"outcome": "home_win", "confidence": 0.75}
    json_str = safe_json_dumps(data)

    with test_db.get_session() as session:
        session.execute(text("INSERT INTO predictions (match_id, data) VALUES ('M002', :json_data)"), {"json_data": json_str})

    with test_db.get_session() as session:
        result = session.execute(text("SELECT data FROM predictions WHERE match_id = 'M002'")).scalar()
        retrieved_data = safe_json_loads(result)
        assert retrieved_data["outcome"] == "home_win"


def test_database_with_retry(test_db):
    """Test database operations with retry logic."""
    attempt_count = 0

    @retry_with_backoff(max_attempts=3, initial_delay=0.1, retry_exceptions=(DatabaseError,))
    def insert_with_retry():
        nonlocal attempt_count
        attempt_count += 1

        # Fail first 2 attempts
        if attempt_count < 3:
            raise DatabaseError("Transient error")

        with test_db.get_session() as session:
            session.execute(text("INSERT INTO predictions (match_id, data) VALUES ('M003', 'retry_test')"))

    insert_with_retry()
    assert attempt_count == 3


# ========================================
# Logger Integration Tests
# ========================================


def test_logger_basic_operation():
    """Test logger basic operation."""
    logger = get_logger("test-component")
    assert logger.name == "test-component"

    # Log message (should not crash)
    logger.info("Test message")
    logger.error("Error message")
    logger.debug("Debug message")


def test_logger_with_exception():
    """Test logger handles exceptions."""
    logger = get_logger("test-exception")

    try:
        raise ValueError("Test error")
    except ValueError:
        logger.error("Caught exception", exc_info=True)

    # Should not crash
    assert True


# ========================================
# Cross-Module Integration Tests
# ========================================


def test_database_and_cache_integration(test_db, test_cache):
    """Test database query results cached."""
    call_count = 0

    @cache_result(redis_client=test_cache.redis_client, ttl=60)
    def get_prediction(match_id: str) -> dict:
        nonlocal call_count
        call_count += 1

        with test_db.get_session() as session:
            # Insert test data first
            session.execute(text("INSERT OR IGNORE INTO predictions (match_id, data) VALUES (:match_id, :data)"), {"match_id": match_id, "data": "cached_data"})
            session.commit()

            # Query data
            result = session.execute(text("SELECT data FROM predictions WHERE match_id = :match_id"), {"match_id": match_id}).scalar()
            return {"match_id": match_id, "data": result}

    # First call - database hit
    result1 = get_prediction("M004")
    assert call_count == 1

    # Second call - cache hit
    result2 = get_prediction("M004")
    assert call_count == 1  # Not called again
    assert result1 == result2


def test_config_database_logger_workflow():
    """Test config → database → logger workflow."""
    # 1. Load config
    config_content = """
app:
  name: sipap-test
database:
  url: "sqlite:///:memory:"
"""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".yml", delete=False) as f:
        f.write(config_content)
        config_path = f.name

    try:
        config = load_config(config_path)

        # 2. Initialize logger
        logger = get_logger(config["app"]["name"])
        logger.info("Application started")

        # 3. Verify config loaded
        assert config["database"]["url"] == "sqlite:///:memory:"
        assert logger.name == "sipap-test"

    finally:
        Path(config_path).unlink()


def test_json_timestamp_database_workflow(test_db):
    """Test JSON + timestamp + database workflow."""
    # 1. Create data with timestamp
    ts = current_timestamp()
    data = {"event": "match_start", "timestamp": ts, "score": [0, 0]}

    # 2. Serialize to JSON
    json_str = safe_json_dumps(data)

    # 3. Store in database
    with test_db.get_session() as session:
        session.execute(text("INSERT INTO predictions (match_id, data) VALUES ('M005', :data)"), {"data": json_str})

    # 4. Retrieve and deserialize
    with test_db.get_session() as session:
        result_json = session.execute(text("SELECT data FROM predictions WHERE match_id = 'M005'")).scalar()
        result_data = safe_json_loads(result_json)

    # 5. Verify timestamp preserved
    assert result_data["timestamp"] == ts
    assert result_data["timestamp"].endswith("Z")


def test_complete_pipeline(test_db, test_cache):
    """Test complete pipeline: fetch → cache → store → retrieve."""
    logger = get_logger("pipeline")

    # 1. Define cached data fetcher
    @cache_result(redis_client=test_cache.redis_client, ttl=60)
    def fetch_match_data(match_id: str) -> dict:
        logger.info(f"Fetching match data for {match_id}")
        return {"match_id": match_id, "home_team": "Arsenal", "away_team": "Chelsea", "timestamp": current_timestamp()}

    # 2. Fetch data (cache miss)
    match_data = fetch_match_data("M006")

    # 3. Store in database
    with test_db.get_session() as session:
        session.execute(text("INSERT INTO predictions (match_id, data) VALUES (:match_id, :data)"), {"match_id": match_data["match_id"], "data": safe_json_dumps(match_data)})

    # 4. Fetch again (cache hit)
    cached_data = fetch_match_data("M006")
    assert cached_data == match_data

    # 5. Retrieve from database
    with test_db.get_session() as session:
        db_data = session.execute(text("SELECT data FROM predictions WHERE match_id = 'M006'")).scalar()
        db_parsed = safe_json_loads(db_data)

    # 6. Verify all match
    assert db_parsed["match_id"] == match_data["match_id"]
    assert db_parsed["timestamp"].endswith("Z")
