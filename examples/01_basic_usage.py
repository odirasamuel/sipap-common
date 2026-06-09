"""Basic usage examples for sipap-common.

This example demonstrates the core functionality of each module in isolation.
"""

import os
from sipap_common.config import load_config
from sipap_common.logging import get_logger, set_log_context
from sipap_common.types import Sport, Match, TeamReference
from sipap_common.utils import current_timestamp, safe_json_dumps
from sipap_common.exceptions import ConfigurationError


def example_config_loading():
    """Example: Load configuration with environment variable substitution."""
    print("\n=== Config Loading Example ===")

    # Set environment variables
    os.environ["APP_ENV"] = "development"
    os.environ["AWS_REGION"] = "us-east-1"
    os.environ["REDIS_HOST"] = "localhost"

    # Create a temporary config file
    config_content = """
app:
  environment: ${ APP_ENV }
  region: ${ AWS_REGION }

redis:
  host: ${ REDIS_HOST }
  port: 6379
  ttl: 300

database:
  pool_size: 20
  max_overflow: 10
"""

    # Write config to temporary file
    config_path = "/tmp/sipap_config.yml"
    with open(config_path, "w") as f:
        f.write(config_content)

    try:
        # Load config with environment variable substitution
        config = load_config(config_path)

        print(f"Environment: {config['app']['environment']}")
        print(f"Region: {config['app']['region']}")
        print(f"Redis Host: {config['redis']['host']}")
        print(f"Redis Port: {config['redis']['port']}")
        print("✅ Config loaded successfully with env substitution")

    except ConfigurationError as e:
        print(f"❌ Config error: {e}")


def example_structured_logging():
    """Example: Use structured logger with context."""
    print("\n=== Structured Logging Example ===")

    logger = get_logger("example")

    # Log without context
    logger.info("Application started")

    # Set context for all subsequent logs
    set_log_context(
        request_id="req-12345",
        sport="soccer",
        component="prediction"
    )

    # Logs now include context automatically
    logger.info("Processing match data")
    logger.debug("Fetching odds from API")
    logger.warning("High latency detected", latency_ms=1500)

    print("✅ Structured logging with context demonstrated")


def example_type_definitions():
    """Example: Use typed data structures."""
    print("\n=== Type Definitions Example ===")

    # Create team references
    home_team: TeamReference = {
        "id": "team-001",
        "name": "Arsenal",
        "short_name": "ARS"
    }

    away_team: TeamReference = {
        "id": "team-002",
        "name": "Chelsea",
        "short_name": "CHE"
    }

    # Create match
    match: Match = {
        "match_id": "match-12345",
        "sport": Sport.SOCCER,
        "competition": "Premier League",
        "home_team": home_team,
        "away_team": away_team,
        "scheduled_time": current_timestamp(),
        "venue": "Emirates Stadium",
        "status": "scheduled",
        "metadata": {
            "season": "2025-26",
            "matchday": 15
        }
    }

    print(f"Match: {match['home_team']['name']} vs {match['away_team']['name']}")
    print(f"Sport: {match['sport']}")
    print(f"Venue: {match['venue']}")
    print(f"Time: {match['scheduled_time']}")

    # Serialize to JSON
    match_json = safe_json_dumps(match, pretty=True)
    print(f"\nJSON representation:\n{match_json}")

    print("✅ Type definitions and JSON serialization demonstrated")


def example_datetime_utilities():
    """Example: Use datetime utilities for consistent timestamps."""
    print("\n=== Datetime Utilities Example ===")

    from sipap_common.utils import (
        current_timestamp,
        parse_iso8601,
        add_seconds,
        subtract_timestamps,
        is_expired
    )

    # Get current UTC timestamp
    now = current_timestamp()
    print(f"Current time: {now}")

    # Parse ISO 8601 string
    dt = parse_iso8601(now)
    print(f"Parsed datetime: {dt}")

    # Add time
    future = add_seconds(now, 3600)
    print(f"One hour later: {future}")

    # Calculate duration
    duration = subtract_timestamps(future, now)
    print(f"Duration: {duration} seconds")

    # Check expiration
    cached_time = current_timestamp()
    expired = is_expired(cached_time, ttl_seconds=300)
    print(f"Cache expired (TTL=300s): {expired}")

    print("✅ Datetime utilities demonstrated")


def example_retry_logic():
    """Example: Use retry decorator for resilient operations."""
    print("\n=== Retry Logic Example ===")

    from sipap_common.utils import retry_with_backoff

    attempt_count = 0

    @retry_with_backoff(
        max_attempts=3,
        initial_delay=1.0,
        backoff_factor=2.0,
        retry_exceptions=(ConnectionError,)
    )
    def unreliable_operation():
        nonlocal attempt_count
        attempt_count += 1

        if attempt_count < 3:
            print(f"  Attempt {attempt_count}: Simulating failure")
            raise ConnectionError("Network timeout")

        print(f"  Attempt {attempt_count}: Success!")
        return {"status": "ok", "data": "result"}

    try:
        result = unreliable_operation()
        print(f"Result: {result}")
        print("✅ Retry logic with exponential backoff demonstrated")
    except ConnectionError:
        print("❌ Operation failed after retries")


if __name__ == "__main__":
    print("SIPAP Common - Basic Usage Examples")
    print("=" * 50)

    example_config_loading()
    example_structured_logging()
    example_type_definitions()
    example_datetime_utilities()
    example_retry_logic()

    print("\n" + "=" * 50)
    print("✅ All basic examples completed successfully!")
