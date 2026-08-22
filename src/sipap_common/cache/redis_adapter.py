"""Redis cache adapter for SIPAP.

Provides RedisCache class and @cache_result decorator for caching function results
with automatic JSON serialization, TTL support, and graceful degradation.
"""

import functools
import hashlib
import json
from collections.abc import Callable
from typing import Any, TypeVar, cast

import redis

from sipap_common.exceptions import CacheError

# Type variable for decorator
F = TypeVar("F", bound=Callable[..., Any])


class RedisCache:
    """Redis cache adapter with connection pooling and JSON serialization."""

    def __init__(
        self,
        host: str = "localhost",
        port: int = 6379,
        db: int = 0,
        password: str | None = None,
        default_ttl: int = 300,
        max_connections: int = 50,
        redis_client: Any | None = None,
        ssl: bool = False,
    ) -> None:
        """Initialize Redis cache.

        Args:
            host: Redis server hostname
            port: Redis server port
            db: Redis database number
            password: Redis password (optional)
            default_ttl: Default time-to-live in seconds (default 300 = 5 minutes)
            max_connections: Maximum connections in pool
            redis_client: Optional Redis client for testing
            ssl: Enable SSL/TLS connection (required for ElastiCache serverless)

        Raises:
            CacheError: If Redis initialization fails
        """
        self.default_ttl = default_ttl

        if redis_client is not None:
            self.redis_client = redis_client
        else:
            try:
                # Create connection pool for better performance
                pool = redis.ConnectionPool(
                    host=host,
                    port=port,
                    db=db,
                    password=password,
                    max_connections=max_connections,
                    decode_responses=False,  # We'll handle encoding/decoding
                    ssl=ssl,
                )
                self.redis_client = redis.Redis(connection_pool=pool)
            except Exception as e:
                raise CacheError(f"Failed to initialize Redis client: {e}")

    def set(self, key: str, value: Any, ttl: int | None = None) -> None:
        """Set a value in cache with TTL.

        Args:
            key: Cache key
            value: Value to cache (will be JSON serialized)
            ttl: Time-to-live in seconds (uses default_ttl if None)

        Raises:
            CacheError: If cache operation fails

        Examples:
            >>> cache = RedisCache()
            >>> cache.set('match:12345', {'home': 'Arsenal', 'away': 'Chelsea'}, ttl=600)
        """
        try:
            ttl_seconds = ttl if ttl is not None else self.default_ttl
            serialized = json.dumps(value)
            self.redis_client.setex(key, ttl_seconds, serialized)
        except Exception as e:
            raise CacheError(f"Failed to set cache key '{key}': {e}")

    def get(self, key: str) -> Any | None:
        """Get a value from cache.

        Args:
            key: Cache key

        Returns:
            Cached value (deserialized from JSON) or None if not found

        Raises:
            CacheError: If cache operation fails

        Examples:
            >>> cache = RedisCache()
            >>> match = cache.get('match:12345')
            >>> if match:
            ...     print(match['home'])
        """
        try:
            value = self.redis_client.get(key)
            if value is None:
                return None

            # Deserialize JSON
            try:
                return json.loads(value)
            except json.JSONDecodeError:
                # Invalid JSON in cache - treat as miss
                return None

        except Exception as e:
            raise CacheError(f"Failed to get cache key '{key}': {e}")

    def delete(self, key: str) -> None:
        """Delete a value from cache.

        Args:
            key: Cache key

        Raises:
            CacheError: If cache operation fails

        Examples:
            >>> cache = RedisCache()
            >>> cache.delete('match:12345')
        """
        try:
            self.redis_client.delete(key)
        except Exception as e:
            raise CacheError(f"Failed to delete cache key '{key}': {e}")

    def exists(self, key: str) -> bool:
        """Check if a key exists in cache.

        Args:
            key: Cache key

        Returns:
            True if key exists, False otherwise

        Raises:
            CacheError: If cache operation fails

        Examples:
            >>> cache = RedisCache()
            >>> if cache.exists('match:12345'):
            ...     print('Match data cached')
        """
        try:
            return bool(self.redis_client.exists(key))
        except Exception as e:
            raise CacheError(f"Failed to check cache key '{key}': {e}")

    def clear(self) -> None:
        """Clear all keys in current database.

        Warning: This removes ALL keys in the Redis database.

        Raises:
            CacheError: If cache operation fails
        """
        try:
            self.redis_client.flushdb()
        except Exception as e:
            raise CacheError(f"Failed to clear cache: {e}")

    def get_stats(self) -> dict[str, Any]:
        """Get cache statistics.

        Returns:
            Dictionary with cache statistics

        Examples:
            >>> cache = RedisCache()
            >>> stats = cache.get_stats()
            >>> print(f"Cache has {stats['keys_count']} keys")
        """
        try:
            info = self.redis_client.info("memory")
            return {
                "keys_count": self.redis_client.dbsize(),
                "memory_usage": info.get("used_memory_human", "unknown"),
                "default_ttl": self.default_ttl,
            }
        except Exception:
            return {
                "keys_count": 0,
                "memory_usage": "unknown",
                "default_ttl": self.default_ttl,
            }


def cache_result(
    redis_client: Any | None = None,
    ttl: int = 300,
    key_prefix: str = "",
    fail_silently: bool = True,
) -> Callable[[F], F]:
    """Decorator to cache function results in Redis.

    Args:
        redis_client: Redis client instance (creates default if None)
        ttl: Time-to-live in seconds
        key_prefix: Optional prefix for cache keys
        fail_silently: If True, continue execution on cache errors (graceful degradation)

    Returns:
        Decorated function with caching

    Examples:
        >>> @cache_result(ttl=600, key_prefix="matches")
        ... def get_match_data(match_id: str) -> dict:
        ...     # Expensive API call
        ...     return fetch_from_api(match_id)

        >>> # First call - cache miss, executes function
        >>> match = get_match_data("12345")

        >>> # Second call - cache hit, returns cached result
        >>> match = get_match_data("12345")  # Fast!
    """

    def decorator(func: F) -> F:
        # Initialize cache once at decoration time
        if redis_client is None:
            cache = RedisCache(default_ttl=ttl)
            client = cache.redis_client
        else:
            client = redis_client

        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Generate cache key from function name and arguments
            func_name = func.__name__
            # Create deterministic key from args and kwargs
            args_str = json.dumps({"args": args, "kwargs": kwargs}, sort_keys=True)
            args_hash = hashlib.md5(args_str.encode()).hexdigest()

            if key_prefix:
                cache_key = f"{key_prefix}:{func_name}:{args_hash}"
            else:
                cache_key = f"{func_name}:{args_hash}"

            # Try to get from cache
            try:
                cached_value = client.get(cache_key)
                if cached_value is not None:
                    # Cache hit
                    try:
                        result = json.loads(cached_value)
                        return result["result"]
                    except (json.JSONDecodeError, KeyError):
                        # Invalid cache data - continue to function execution
                        pass
            except Exception as e:
                if not fail_silently:
                    raise CacheError(f"Cache get failed for {func_name}: {e}")
                # If fail_silently=True, continue to function execution

            # Cache miss or error - execute function
            result = func(*args, **kwargs)

            # Store result in cache
            try:
                serialized = json.dumps({"result": result})
                client.setex(cache_key, ttl, serialized)
            except Exception as e:
                if not fail_silently:
                    raise CacheError(f"Cache set failed for {func_name}: {e}")
                # If fail_silently=True, return result without caching

            return result

        return cast(F, wrapper)

    return decorator
