"""Tests for sipap_common.cache.redis_adapter module."""

import json
from unittest.mock import Mock, patch

import pytest

from sipap_common.cache.redis_adapter import RedisCache, cache_result
from sipap_common.exceptions import CacheError


@pytest.fixture
def mock_redis():
    """Create mock Redis client."""
    return Mock()


@pytest.fixture
def redis_cache(mock_redis):
    """Create RedisCache with mocked client."""
    return RedisCache(redis_client=mock_redis)


def test_redis_cache_initializes_with_defaults() -> None:
    """Test that RedisCache initializes with default configuration."""
    with patch("sipap_common.cache.redis_adapter.redis.Redis") as mock_redis_class:
        cache = RedisCache()
        assert cache.default_ttl == 300
        assert cache.redis_client is not None
        mock_redis_class.assert_called_once()


def test_redis_cache_initializes_with_custom_ttl() -> None:
    """Test that RedisCache respects custom default TTL."""
    with patch("sipap_common.cache.redis_adapter.redis.Redis"):
        cache = RedisCache(default_ttl=600)
        assert cache.default_ttl == 600


def test_redis_cache_accepts_mock_client(mock_redis) -> None:
    """Test that RedisCache accepts injected client for testing."""
    cache = RedisCache(redis_client=mock_redis)
    assert cache.redis_client == mock_redis


def test_set_success(redis_cache, mock_redis) -> None:
    """Test successful cache set operation."""
    mock_redis.setex.return_value = True

    redis_cache.set("test_key", {"data": "value"}, ttl=60)

    mock_redis.setex.assert_called_once()
    call_args = mock_redis.setex.call_args
    assert call_args[0][0] == "test_key"
    assert call_args[0][1] == 60
    # Value should be JSON serialized
    assert "data" in call_args[0][2]


def test_set_with_default_ttl(redis_cache, mock_redis) -> None:
    """Test cache set uses default TTL when not specified."""
    mock_redis.setex.return_value = True

    redis_cache.set("test_key", {"data": "value"})

    call_args = mock_redis.setex.call_args
    assert call_args[0][1] == 300  # Default TTL


def test_set_handles_redis_error(redis_cache, mock_redis) -> None:
    """Test that set raises CacheError on Redis failure."""
    mock_redis.setex.side_effect = Exception("Redis connection failed")

    with pytest.raises(CacheError, match="Failed to set cache"):
        redis_cache.set("test_key", {"data": "value"})


def test_get_success(redis_cache, mock_redis) -> None:
    """Test successful cache get operation."""
    cached_data = {"result": "cached_value", "count": 42}
    mock_redis.get.return_value = json.dumps(cached_data).encode("utf-8")

    result = redis_cache.get("test_key")

    assert result == cached_data
    mock_redis.get.assert_called_once_with("test_key")


def test_get_cache_miss(redis_cache, mock_redis) -> None:
    """Test cache miss returns None."""
    mock_redis.get.return_value = None

    result = redis_cache.get("missing_key")

    assert result is None


def test_get_invalid_json_returns_none(redis_cache, mock_redis) -> None:
    """Test that invalid JSON in cache returns None."""
    mock_redis.get.return_value = b"invalid json{{"

    result = redis_cache.get("bad_key")

    assert result is None


def test_get_handles_redis_error(redis_cache, mock_redis) -> None:
    """Test that get raises CacheError on Redis failure."""
    mock_redis.get.side_effect = Exception("Redis connection failed")

    with pytest.raises(CacheError, match="Failed to get cache"):
        redis_cache.get("test_key")


def test_delete_success(redis_cache, mock_redis) -> None:
    """Test successful cache delete operation."""
    mock_redis.delete.return_value = 1  # 1 key deleted

    redis_cache.delete("test_key")

    mock_redis.delete.assert_called_once_with("test_key")


def test_delete_handles_redis_error(redis_cache, mock_redis) -> None:
    """Test that delete raises CacheError on Redis failure."""
    mock_redis.delete.side_effect = Exception("Redis connection failed")

    with pytest.raises(CacheError, match="Failed to delete cache"):
        redis_cache.delete("test_key")


def test_exists_returns_true(redis_cache, mock_redis) -> None:
    """Test exists returns True for existing key."""
    mock_redis.exists.return_value = 1

    result = redis_cache.exists("test_key")

    assert result is True
    mock_redis.exists.assert_called_once_with("test_key")


def test_exists_returns_false(redis_cache, mock_redis) -> None:
    """Test exists returns False for missing key."""
    mock_redis.exists.return_value = 0

    result = redis_cache.exists("missing_key")

    assert result is False


def test_clear_success(redis_cache, mock_redis) -> None:
    """Test successful cache clear operation."""
    mock_redis.flushdb.return_value = True

    redis_cache.clear()

    mock_redis.flushdb.assert_called_once()


def test_get_cache_stats(redis_cache, mock_redis) -> None:
    """Test cache statistics retrieval."""
    mock_redis.dbsize.return_value = 42
    mock_redis.info.return_value = {"used_memory_human": "1.5M"}

    stats = redis_cache.get_stats()

    assert stats["keys_count"] == 42
    assert stats["memory_usage"] == "1.5M"
    assert "default_ttl" in stats


def test_cache_result_decorator_cache_miss() -> None:
    """Test @cache_result decorator on cache miss."""
    mock_redis = Mock()
    mock_redis.get.return_value = None  # Cache miss
    mock_redis.setex.return_value = True

    @cache_result(redis_client=mock_redis, ttl=60)
    def expensive_function(x: int, y: int) -> int:
        return x + y

    result = expensive_function(5, 3)

    assert result == 8
    # Should have tried to get from cache
    mock_redis.get.assert_called_once()
    # Should have set result in cache
    mock_redis.setex.assert_called_once()


def test_cache_result_decorator_cache_hit() -> None:
    """Test @cache_result decorator on cache hit."""
    mock_redis = Mock()
    cached_result = json.dumps({"result": 8}).encode("utf-8")
    mock_redis.get.return_value = cached_result

    call_count = 0

    @cache_result(redis_client=mock_redis, ttl=60)
    def expensive_function(x: int, y: int) -> int:
        nonlocal call_count
        call_count += 1
        return x + y

    result = expensive_function(5, 3)

    assert result == 8
    # Function should NOT have been called (cache hit)
    assert call_count == 0
    mock_redis.get.assert_called_once()


def test_cache_result_decorator_key_generation() -> None:
    """Test that decorator generates unique keys for different arguments."""
    mock_redis = Mock()
    mock_redis.get.return_value = None
    mock_redis.setex.return_value = True

    @cache_result(redis_client=mock_redis, ttl=60)
    def test_func(a: int, b: str) -> str:
        return f"{a}:{b}"

    test_func(1, "x")
    test_func(2, "y")

    # Should have called get twice with different keys
    assert mock_redis.get.call_count == 2
    call_keys = [call[0][0] for call in mock_redis.get.call_args_list]
    assert call_keys[0] != call_keys[1]  # Different args = different keys


def test_cache_result_decorator_with_key_prefix() -> None:
    """Test decorator with custom key prefix."""
    mock_redis = Mock()
    mock_redis.get.return_value = None
    mock_redis.setex.return_value = True

    @cache_result(redis_client=mock_redis, ttl=60, key_prefix="sports")
    def get_matches(league: str) -> list:
        return [{"id": 1, "league": league}]

    get_matches("premier_league")

    # Key should start with custom prefix
    cache_key = mock_redis.get.call_args[0][0]
    assert cache_key.startswith("sports:")


def test_cache_result_decorator_graceful_degradation() -> None:
    """Test that decorator continues working if Redis unavailable."""
    mock_redis = Mock()
    mock_redis.get.side_effect = Exception("Redis down")
    mock_redis.setex.side_effect = Exception("Redis down")

    call_count = 0

    @cache_result(redis_client=mock_redis, ttl=60, fail_silently=True)
    def important_function(x: int) -> int:
        nonlocal call_count
        call_count += 1
        return x * 2

    result = important_function(5)

    # Function should execute despite Redis failure
    assert result == 10
    assert call_count == 1


def test_cache_result_decorator_without_graceful_degradation() -> None:
    """Test that decorator raises error if fail_silently=False."""
    mock_redis = Mock()
    mock_redis.get.side_effect = Exception("Redis down")

    @cache_result(redis_client=mock_redis, ttl=60, fail_silently=False)
    def function_that_needs_cache(x: int) -> int:
        return x * 2

    with pytest.raises(CacheError):
        function_that_needs_cache(5)


def test_redis_cache_with_connection_pool() -> None:
    """Test RedisCache initialization with connection pool."""
    with patch("sipap_common.cache.redis_adapter.redis.ConnectionPool") as mock_pool_class:
        with patch("sipap_common.cache.redis_adapter.redis.Redis"):
            RedisCache(
                host="redis.example.com",
                port=6380,
                db=1,
                password="secret",
                max_connections=50,
            )

            # Should create connection pool
            mock_pool_class.assert_called_once()
            pool_kwargs = mock_pool_class.call_args[1]
            assert pool_kwargs["host"] == "redis.example.com"
            assert pool_kwargs["port"] == 6380
            assert pool_kwargs["db"] == 1
            assert pool_kwargs["password"] == "secret"
            assert pool_kwargs["max_connections"] == 50


def test_cache_serialization_handles_complex_types(redis_cache, mock_redis) -> None:
    """Test that cache handles complex nested data structures."""
    complex_data = {
        "match": {"id": "12345", "teams": ["Arsenal", "Chelsea"]},
        "predictions": [
            {"outcome": "home_win", "confidence": 0.75},
            {"outcome": "draw", "confidence": 0.15},
        ],
        "metadata": {"timestamp": "2026-06-08T12:00:00Z", "version": 1},
    }

    mock_redis.setex.return_value = True
    redis_cache.set("complex_key", complex_data)

    # Should successfully serialize
    call_args = mock_redis.setex.call_args
    serialized = call_args[0][2]
    # Should be able to deserialize back
    deserialized = json.loads(serialized)
    assert deserialized == complex_data
