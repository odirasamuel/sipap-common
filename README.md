# sipap-common

Shared utilities for the SIPAP (Sports Intelligence Platform and Outcome Probability Assessment Platform).

[![Python Version](https://img.shields.io/badge/python-3.12%20%7C%203.13%20%7C%203.14-blue)](https://www.python.org/downloads/)
[![Test Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)](./htmlcov/index.html)
[![Type Checked](https://img.shields.io/badge/type%20checked-mypy-blue)](http://mypy-lang.org/)
[![Code Style](https://img.shields.io/badge/code%20style-ruff-000000)](https://github.com/astral-sh/ruff)

## Overview

`sipap-common` provides core utilities used across all SIPAP components:

- **Config Loader**: Jinja2-based YAML configuration with environment variable substitution
- **Structured Logger**: JSON-formatted logging with ContextVar-based context propagation
- **AWS Clients**: Typed wrappers for Lambda, SQS, EventBridge, S3, and more
- **Cache Adapter**: Redis wrapper with connection pooling and decorators
- **Type Definitions**: TypedDict definitions for Match, Prediction, Odds, etc.
- **Exception Hierarchy**: Domain-specific exception types
- **Utility Functions**: Retry decorators, datetime helpers, JSON serializers

## Requirements

- **Python:** 3.12, 3.13, or 3.14
- **Operating System:** Linux, macOS, Windows

## Installation

### Production

```bash
# Install from wheel
pip install sipap-common

# Or specify version
pip install sipap-common==0.1.0
```

### Development

```bash
# Clone repository
git clone <repo-url>
cd sipap-common

# Create virtualenv
python3.12 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install in editable mode with dev dependencies
pip install -e ".[dev]"
```

**Python Version:** This package requires Python 3.12+ due to `datetime.UTC` and other modern features. See [PYTHON-COMPATIBILITY.md](PYTHON-COMPATIBILITY.md) for details.

## Quick Start

### Config Loading

```python
from sipap_common.config import load_config

config = load_config(
    config_path="config.yml",
    env_vars={"REGION": "us-east-1", "ENV": "production"}
)
```

### Structured Logging

```python
from sipap_common.logging import get_logger, set_log_context

# Set context for current request
set_log_context(
    request_id="req-12345",
    sport="soccer",
    component="orchestrator"
)

logger = get_logger(__name__)
logger.info("Processing match", extra={"match_id": "12345"})
# Output: {"timestamp":"2026-06-08T10:30:00.123Z","level":"INFO","request_id":"req-12345","sport":"soccer","component":"orchestrator","message":"Processing match","match_id":"12345"}
```

### AWS Clients

```python
from sipap_common.aws import get_aws_client

# Get any AWS client with consistent configuration
s3 = get_aws_client('s3', region='us-east-1')
lambda_client = get_aws_client('lambda', region='us-east-1')
```

### Cache

```python
from sipap_common.cache import RedisCache, cache_result

# Direct usage
cache = RedisCache(host='localhost', port=6379)
cache.set('key', {'data': 'value'}, ttl=300)
data = cache.get('key')

# Decorator usage
@cache_result(ttl=300, key_prefix='match')
def get_match_data(match_id: str):
    # Expensive operation
    return fetch_from_db(match_id)
```

### Type Definitions

```python
from sipap_common.types import Match, Prediction, Sport
from sipap_common.utils import current_timestamp

match: Match = {
    'match_id': '12345',
    'sport': Sport.SOCCER,
    'competition': 'Premier League',
    'home_team': {'id': 't1', 'name': 'Arsenal', 'short_name': 'ARS'},
    'away_team': {'id': 't2', 'name': 'Chelsea', 'short_name': 'CHE'},
    'scheduled_time': current_timestamp(),
    'venue': 'Emirates Stadium',
    'status': 'scheduled',
    'metadata': {}
}
```

### Database Connection

```python
from sipap_common.database import DatabaseManager

# Production with connection pooling
db = DatabaseManager(
    "postgresql://user:pass@localhost/sipap",
    pool_size=20,
    max_overflow=10
)

# Serverless (Lambda) without pooling
db_lambda = DatabaseManager(database_url, use_pool=False)

# Context manager for automatic session management
with db.get_session() as session:
    result = session.execute(text("SELECT * FROM matches"))
    # Auto-commits on success, rolls back on exception
```

### Utility Functions

```python
from sipap_common.utils import (
    retry_with_backoff,
    current_timestamp,
    add_seconds,
    safe_json_dumps,
    safe_json_loads
)

# Retry with exponential backoff
@retry_with_backoff(
    max_attempts=5,
    initial_delay=1.0,
    backoff_factor=2.0,
    retry_exceptions=(ConnectionError,)
)
def fetch_data_from_api():
    # Will retry on ConnectionError with exponential backoff
    pass

# ISO 8601 timestamps with Z suffix (CloudWatch compatible)
timestamp = current_timestamp()  # "2026-06-09T10:30:45.123456Z"

# Safe JSON serialization (handles datetime, Decimal, Enum, set, bytes)
json_str = safe_json_dumps({"timestamp": current_timestamp(), "score": Decimal("2.5")})
```

## Examples

Comprehensive examples are available in the [`examples/`](examples/) directory:

- **[01_basic_usage.py](examples/01_basic_usage.py)**: Individual module functionality
  - Config loading with Jinja2
  - Structured logging
  - Type definitions
  - Datetime utilities
  - Retry logic

- **[02_integrated_workflow.py](examples/02_integrated_workflow.py)**: Modules working together
  - Complete pipeline: Config → Cache → Database → Logging
  - Cache decorator for memoization
  - Error handling across boundaries

- **[03_aws_integration.py](examples/03_aws_integration.py)**: AWS service integrations
  - Lambda, SQS, EventBridge, S3 clients
  - Cross-service workflows
  - Session management

Run any example:
```bash
python examples/01_basic_usage.py
```

See [examples/README.md](examples/README.md) for detailed documentation and usage patterns.

## Testing

### Unit Tests

sipap-common includes comprehensive unit tests for all modules:

```bash
# Run all tests
pytest

# Run specific module tests
pytest tests/unit/config/
pytest tests/unit/logging/
pytest tests/unit/aws/

# Run with coverage
pytest --cov=src/sipap_common --cov-report=html
```

### Integration Tests

Integration tests verify cross-module workflows:

```bash
# Run integration tests
pytest tests/integration/

# Specific workflow tests
pytest tests/integration/test_integration_simple.py -v
```

### Testing with Mocks

Use `moto` for AWS mocking and `fakeredis` for Redis:

```python
from moto import mock_aws
import fakeredis

# AWS mocking
@mock_aws
def test_lambda_invoke():
    lambda_client = LambdaClient(create_session())
    # Test code here

# Redis mocking
def test_cache():
    fake_redis = fakeredis.FakeRedis(decode_responses=True)
    cache = RedisCache(redis_client=fake_redis)
    # Test code here
```

### Quality Gates

All code must pass:

```bash
# Type checking (mypy strict mode)
mypy src/sipap_common

# Linting (ruff)
ruff check src/sipap_common

# Tests with 80%+ coverage
pytest --cov=src/sipap_common --cov-report=term --cov-fail-under=80
```

## Development

### Setup

```bash
# Clone repository
git clone <repo-url>
cd sipap-common

# Create virtual environment
python3.12 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install in editable mode with dev dependencies
pip install -e ".[dev]"

# Verify installation
python -c "from sipap_common import get_logger; print('✅ Installation successful')"
```

### Running Tests

```bash
# Run all tests with coverage
pytest --cov=src/sipap_common --cov-report=html

# Run specific test categories
pytest tests/unit/          # Unit tests only
pytest tests/integration/   # Integration tests only

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/unit/config/test_loader.py -v
```

### Code Quality

```bash
# Type checking
mypy src/sipap_common

# Linting
ruff check src/sipap_common

# Auto-fix linting issues
ruff check --fix src/sipap_common

# Format code
ruff format src/sipap_common
```

### Building Package

```bash
# Install build tool
pip install build

# Build wheel and source distribution
python -m build

# Output: dist/sipap_common-0.1.0-py3-none-any.whl
#         dist/sipap_common-0.1.0.tar.gz
```

## Production Deployment

### Docker

```dockerfile
FROM python:3.12-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install sipap-common
COPY dist/sipap_common-0.1.0-py3-none-any.whl .
RUN pip install sipap_common-0.1.0-py3-none-any.whl

# Copy application code
COPY . .

CMD ["python", "app.py"]
```

### AWS Lambda

```python
# layer_builder.sh
#!/bin/bash
pip install sipap-common -t python/
zip -r sipap-common-layer.zip python/

# Upload to Lambda as layer
aws lambda publish-layer-version \
  --layer-name sipap-common \
  --zip-file fileb://sipap-common-layer.zip \
  --compatible-runtimes python3.12
```

### Environment Variables

Required environment variables for production:

```bash
# AWS
export AWS_REGION=us-east-1
export AWS_PROFILE=production  # Optional

# Redis
export REDIS_HOST=cache.example.com
export REDIS_PORT=6379
export REDIS_PASSWORD=secret  # If using AUTH

# Database
export DATABASE_URL=postgresql://user:pass@db.example.com/sipap
export DB_POOL_SIZE=20
export DB_MAX_OVERFLOW=10

# Logging
export LOG_LEVEL=INFO
export LOG_FORMAT=json
```

### Configuration Management

Use Jinja2 templates for environment-specific configs:

```yaml
# config.yml
app:
  environment: ${ APP_ENV }
  region: ${ AWS_REGION }

database:
  url: ${ DATABASE_URL }
  pool_size: ${ DB_POOL_SIZE | 20 }  # Default: 20

redis:
  host: ${ REDIS_HOST }
  port: ${ REDIS_PORT | 6379 }
```

Load with:
```python
from sipap_common.config import load_config
config = load_config("config.yml")
```

## Architecture

This package adopts proven patterns from Sentinel:

1. **ContextVar-Based Logging**: Thread-safe and async-safe context propagation
2. **Jinja2 Template Processing**: `${ VARIABLE }` syntax for environment variables
3. **Graceful Degradation**: Missing config vars default to empty string
4. **Type Safety**: Comprehensive TypedDict definitions for all domain objects

## License

Copyright © 2026 SIPAP Team
