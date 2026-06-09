# SIPAP Common - Usage Examples

This directory contains comprehensive examples demonstrating how to use `sipap-common` in various scenarios.

## Prerequisites

```bash
# Install sipap-common
pip install sipap-common

# Or install from source in editable mode
pip install -e .
```

## Examples Overview

### 01_basic_usage.py

**Demonstrates individual module functionality:**
- Config loading with Jinja2 environment variable substitution
- Structured logging with context propagation
- Type definitions (Match, Prediction, Odds)
- Datetime utilities (timestamps, parsing, arithmetic)
- Retry logic with exponential backoff
- JSON serialization (datetime, Decimal, Enum support)

**Run:**
```bash
python examples/01_basic_usage.py
```

**Key Learnings:**
- How to load YAML config with `${ VAR }` syntax
- How to use `set_log_context()` for automatic context injection
- How to create typed data structures
- How to use `@retry_with_backoff` decorator

### 02_integrated_workflow.py

**Demonstrates modules working together:**
- Complete pipeline: Config → Cache → Database → Logging
- Cache decorator for automatic result memoization
- Database session management with context managers
- Error handling across module boundaries
- Retry logic integrated with API calls

**Run:**
```bash
python examples/02_integrated_workflow.py
```

**Key Learnings:**
- How modules integrate seamlessly
- How context propagates through the call stack
- How to structure a complete data processing pipeline
- How to handle errors consistently

### 03_aws_integration.py

**Demonstrates AWS service integrations:**
- Session management
- Lambda client (function invocation)
- SQS client (send/receive/delete messages)
- EventBridge client (event publishing)
- S3 client (object storage)
- Cross-service workflows

**Run:**
```bash
python examples/03_aws_integration.py
```

**Key Learnings:**
- How to create AWS sessions with profiles
- How to use typed client wrappers
- How to structure cross-service workflows
- How to test with moto mocking

## Testing the Examples

### With Mocks (Recommended for Development)

Examples are designed to show API patterns. For actual testing:

```python
# Use moto for AWS mocking
from moto import mock_aws

@mock_aws
def test_lambda_workflow():
    # Your test code here
    pass
```

```python
# Use fakeredis for cache testing
import fakeredis

redis_client = fakeredis.FakeRedis(decode_responses=True)
cache = RedisCache(redis_client)
```

```python
# Use SQLite in-memory for database testing
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool

engine = create_engine(
    "sqlite:///:memory:",
    poolclass=StaticPool
)
```

### With Real Services (Production Patterns)

Set environment variables:

```bash
export AWS_PROFILE=development
export AWS_REGION=us-east-1
export REDIS_HOST=localhost
export REDIS_PORT=6379
export DATABASE_URL=postgresql://user:pass@localhost/sipap
```

Then run examples with real service connections.

## Common Patterns

### Pattern 1: Config-Driven Application

```python
from sipap_common.config import load_config

# Load config with environment substitution
config = load_config("config.yml")

# Access nested values
redis_host = config["redis"]["host"]
db_pool_size = config["database"]["pool_size"]
```

### Pattern 2: Structured Logging Throughout

```python
from sipap_common.logging import get_logger, set_log_context

# Set context once at request entry
set_log_context(request_id=req_id, sport="soccer")

# All subsequent logs include context
logger = get_logger(__name__)
logger.info("Processing match")  # Includes request_id and sport
```

### Pattern 3: Cached Database Queries

```python
from sipap_common.cache import cache_result
from sipap_common.database import DatabaseManager

db = DatabaseManager(database_url)

@cache_result(redis_client=redis, ttl=300)
def get_match_predictions(match_id: str):
    with db.get_session() as session:
        result = session.execute(
            text("SELECT * FROM predictions WHERE match_id = :id"),
            {"id": match_id}
        )
        return result.fetchall()

# First call: database query
predictions = get_match_predictions("match-123")

# Second call: cache hit (no database query)
predictions = get_match_predictions("match-123")
```

### Pattern 4: Resilient External API Calls

```python
from sipap_common.utils import retry_with_backoff
import requests

@retry_with_backoff(
    max_attempts=5,
    initial_delay=1.0,
    backoff_factor=2.0,
    retry_exceptions=(requests.RequestException,)
)
def fetch_odds_data(match_id: str):
    response = requests.get(f"https://api.odds.com/matches/{match_id}")
    response.raise_for_status()
    return response.json()

# Automatically retries with exponential backoff on failure
odds = fetch_odds_data("match-123")
```

### Pattern 5: Event-Driven Workflows

```python
from sipap_common.aws import EventBridgeClient, create_session
from sipap_common.utils import current_timestamp, safe_json_dumps

session = create_session(region="us-east-1")
eventbridge = EventBridgeClient(session)

# Publish event
event = {
    "Source": "sipap.predictions",
    "DetailType": "Prediction Completed",
    "Detail": safe_json_dumps({
        "match_id": "match-123",
        "confidence": 0.85,
        "timestamp": current_timestamp()
    }),
    "EventBusName": "sipap-events"
}

eventbridge.put_events([event])
```

## Error Handling Patterns

### Pattern 1: Specific Exception Handling

```python
from sipap_common.exceptions import (
    ConfigurationError,
    DatabaseError,
    CacheError
)

try:
    config = load_config("config.yml")
except ConfigurationError as e:
    logger.error("Config error", error=str(e))
    # Use default configuration
    config = get_default_config()

try:
    with db.get_session() as session:
        # Database operations
        pass
except DatabaseError as e:
    logger.error("Database error", error=str(e))
    # Retry or fallback
```

### Pattern 2: Context Manager Automatic Cleanup

```python
# Database session automatically commits on success, rolls back on error
with db.get_session() as session:
    result = session.execute(text("INSERT INTO ..."))
    # Automatic commit if no exception
    # Automatic rollback if exception
    # Automatic close always
```

## Performance Considerations

### Cache TTL Selection

```python
# Short TTL for frequently changing data
@cache_result(redis_client=redis, ttl=60)  # 1 minute
def get_live_odds():
    pass

# Long TTL for stable data
@cache_result(redis_client=redis, ttl=3600)  # 1 hour
def get_team_info():
    pass
```

### Database Connection Pooling

```python
# Production HTTP service
db = DatabaseManager(
    database_url,
    pool_size=20,          # Concurrent connections
    max_overflow=10,       # Surge capacity
    pool_recycle=3600      # Recycle every hour
)

# Serverless Lambda
db = DatabaseManager(
    database_url,
    use_pool=False  # No pooling in Lambda
)
```

## Next Steps

1. **Read the main README**: `/README.md` for package overview
2. **Check the tests**: `/tests/` for more usage patterns
3. **Review the API docs**: Generated with Sphinx (if available)
4. **Explore integration tests**: `/tests/integration/` for cross-module examples

## Contributing Examples

To add a new example:

1. Create `examples/XX_descriptive_name.py`
2. Include comprehensive docstrings
3. Demonstrate a specific use case or pattern
4. Add entry to this README
5. Ensure example runs without external dependencies (or document clearly)

## Questions?

- Check `/README.md` for package documentation
- Review tests in `/tests/` for more patterns
- See API reference (if generated)
