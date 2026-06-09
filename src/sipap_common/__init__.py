"""
SIPAP Common Utilities

Shared utilities for the Sports Intelligence Platform and Outcome Probability
Assessment Platform (SIPAP).
"""

from sipap_common.aws import (
    EventBridgeClient,
    LambdaClient,
    S3Client,
    SQSClient,
    create_session,
    get_aws_client,
)
from sipap_common.cache import RedisCache, cache_result
from sipap_common.config import load_config
from sipap_common.database import DatabaseManager
from sipap_common.exceptions import (
    AWSServiceError,
    CacheError,
    ConfigurationError,
    DatabaseError,
    SIPAPException,
    ValidationError,
)
from sipap_common.logging import clear_log_context, get_logger, set_log_context
from sipap_common.types import (
    Match,
    OddsData,
    Prediction,
    Sport,
    TeamReference,
)
from sipap_common.utils import (
    add_seconds,
    current_timestamp,
    is_expired,
    parse_iso8601,
    retry_with_backoff,
    safe_json_dumps,
    safe_json_loads,
    subtract_timestamps,
)

__version__ = "0.1.0"

__all__ = [
    # Config
    "load_config",
    # Logging
    "get_logger",
    "set_log_context",
    "clear_log_context",
    # AWS
    "create_session",
    "get_aws_client",
    "LambdaClient",
    "SQSClient",
    "EventBridgeClient",
    "S3Client",
    # Cache
    "RedisCache",
    "cache_result",
    # Database
    "DatabaseManager",
    # Utils
    "retry_with_backoff",
    "current_timestamp",
    "parse_iso8601",
    "add_seconds",
    "subtract_timestamps",
    "is_expired",
    "safe_json_dumps",
    "safe_json_loads",
    # Exceptions
    "SIPAPException",
    "ConfigurationError",
    "AWSServiceError",
    "CacheError",
    "DatabaseError",
    "ValidationError",
    # Types
    "Sport",
    "Match",
    "TeamReference",
    "Prediction",
    "OddsData",
]
