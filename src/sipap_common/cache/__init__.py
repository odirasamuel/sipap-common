"""Cache module for SIPAP.

Provides Redis cache adapter and caching decorators.
"""

from sipap_common.cache.redis_adapter import RedisCache, cache_result

__all__ = ["RedisCache", "cache_result"]
