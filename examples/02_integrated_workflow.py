"""Integrated workflow example showing modules working together.

This example demonstrates a realistic workflow:
1. Load configuration
2. Setup structured logging with context
3. Initialize Redis cache
4. Fetch data with caching and retry logic
5. Store data in database with JSON serialization
6. Retrieve and validate data
"""

import os
from sipap_common.config import load_config
from sipap_common.logging import get_logger, set_log_context
from sipap_common.cache import RedisCache, cache_result
from sipap_common.database import DatabaseManager
from sipap_common.types import Match, Sport, TeamReference
from sipap_common.utils import (
    retry_with_backoff,
    current_timestamp,
    safe_json_dumps,
    safe_json_loads
)
from sipap_common.exceptions import DatabaseError, CacheError


# Simulated external API call
call_count = 0


@retry_with_backoff(
    max_attempts=3,
    initial_delay=0.5,
    backoff_factor=2.0,
    retry_exceptions=(ConnectionError,)
)
def fetch_match_from_api(match_id: str) -> Match:
    """Simulate fetching match data from external API with retry logic."""
    global call_count
    call_count += 1

    logger = get_logger("api")
    logger.info("Fetching match from API", match_id=match_id, attempt=call_count)

    # Simulate match data
    match: Match = {
        "match_id": match_id,
        "sport": Sport.SOCCER,
        "competition": "Premier League",
        "home_team": {
            "id": "team-001",
            "name": "Arsenal",
            "short_name": "ARS"
        },
        "away_team": {
            "id": "team-002",
            "name": "Chelsea",
            "short_name": "CHE"
        },
        "scheduled_time": current_timestamp(),
        "venue": "Emirates Stadium",
        "status": "scheduled",
        "metadata": {
            "season": "2025-26",
            "matchday": 15,
            "importance": "high"
        }
    }

    return match


def setup_environment():
    """Setup configuration and logging."""
    print("\n=== Step 1: Setup Environment ===")

    # Set environment variables
    os.environ["APP_ENV"] = "development"
    os.environ["AWS_REGION"] = "us-east-1"
    os.environ["LOG_LEVEL"] = "INFO"

    # Setup logging context
    set_log_context(
        request_id="req-workflow-001",
        sport="soccer",
        component="match-processor"
    )

    logger = get_logger("setup")
    logger.info("Environment configured")

    print("✅ Environment setup complete")


def demonstrate_cache_workflow():
    """Demonstrate cache integration with automatic JSON serialization."""
    print("\n=== Step 2: Cache Workflow ===")

    global call_count
    call_count = 0  # Reset counter

    logger = get_logger("cache")

    try:
        # Note: In real usage, you would use actual Redis
        # For this example, we're showing the API pattern
        print("Note: This example shows the API pattern. In production, use actual Redis.")

        # Example cache decorator usage
        # @cache_result(redis_client=redis_client, ttl=300)
        def get_match_data(match_id: str) -> Match:
            """Fetch match with automatic caching."""
            return fetch_match_from_api(match_id)

        # First call - cache miss, calls API
        logger.info("First call (cache miss)")
        match1 = get_match_data("match-12345")
        print(f"Call count after first call: {call_count}")

        # Second call - would be cache hit in production
        logger.info("Second call (would be cache hit)")
        match2 = get_match_data("match-12345")
        print(f"Call count after second call: {call_count}")

        print("✅ Cache workflow demonstrated (see logs for call counts)")

    except CacheError as e:
        logger.error("Cache error", error=str(e))
        print(f"❌ Cache error: {e}")


def demonstrate_database_workflow():
    """Demonstrate database integration with JSON serialization."""
    print("\n=== Step 3: Database Workflow ===")

    logger = get_logger("database")

    # Note: This shows the API pattern
    print("Note: This example shows the API pattern. In production, use actual PostgreSQL.")

    try:
        # Example database usage pattern
        # db = DatabaseManager("postgresql://...")

        # Store match data
        match = fetch_match_from_api("match-67890")
        match_json = safe_json_dumps(match)

        logger.info("Would store match in database", match_id=match["match_id"])
        print(f"Match data serialized: {len(match_json)} bytes")

        # Example SQL pattern:
        # with db.get_session() as session:
        #     session.execute(
        #         text("INSERT INTO matches (match_id, data) VALUES (:id, :data)"),
        #         {"id": match["match_id"], "data": match_json}
        #     )

        # Retrieve and deserialize
        retrieved_match = safe_json_loads(match_json)
        print(f"Retrieved: {retrieved_match['home_team']['name']} vs {retrieved_match['away_team']['name']}")

        print("✅ Database workflow demonstrated")

    except DatabaseError as e:
        logger.error("Database error", error=str(e))
        print(f"❌ Database error: {e}")


def demonstrate_complete_pipeline():
    """Demonstrate complete pipeline: Config → Cache → Database → Logging."""
    print("\n=== Step 4: Complete Pipeline ===")

    logger = get_logger("pipeline")

    # 1. Fetch data (with retry logic)
    logger.info("Pipeline started")
    match = fetch_match_from_api("match-99999")

    # 2. Log structured data
    logger.info(
        "Match fetched",
        match_id=match["match_id"],
        home_team=match["home_team"]["name"],
        away_team=match["away_team"]["name"],
        scheduled_time=match["scheduled_time"]
    )

    # 3. Serialize for storage
    match_json = safe_json_dumps(match, pretty=False)
    logger.info("Match serialized", size_bytes=len(match_json))

    # 4. Would cache result
    # cache.set(f"match:{match['match_id']}", match_json, ttl=300)
    logger.info("Match cached (simulated)", ttl_seconds=300)

    # 5. Would store in database
    # with db.get_session() as session:
    #     session.execute(...)
    logger.info("Match stored in database (simulated)")

    print("✅ Complete pipeline demonstrated")


def demonstrate_error_handling():
    """Demonstrate comprehensive error handling."""
    print("\n=== Step 5: Error Handling ===")

    logger = get_logger("error_handling")

    from sipap_common.exceptions import (
        ConfigurationError,
        AWSServiceError,
        CacheError,
        DatabaseError,
        ValidationError
    )

    # Example: Handle configuration error
    try:
        # Simulate configuration error
        raise ConfigurationError("Missing required configuration: database.url")
    except ConfigurationError as e:
        logger.error("Configuration error", error=str(e))
        print(f"Caught ConfigurationError: {e}")

    # Example: Handle database error
    try:
        # Simulate database error
        raise DatabaseError("Connection pool exhausted")
    except DatabaseError as e:
        logger.error("Database error", error=str(e))
        print(f"Caught DatabaseError: {e}")

    # Example: Handle validation error
    try:
        # Simulate validation error
        raise ValidationError("Invalid match_id format")
    except ValidationError as e:
        logger.error("Validation error", error=str(e))
        print(f"Caught ValidationError: {e}")

    print("✅ Error handling demonstrated")


def main():
    """Run all workflow demonstrations."""
    print("=" * 60)
    print("SIPAP Common - Integrated Workflow Example")
    print("=" * 60)

    setup_environment()
    demonstrate_cache_workflow()
    demonstrate_database_workflow()
    demonstrate_complete_pipeline()
    demonstrate_error_handling()

    print("\n" + "=" * 60)
    print("✅ All integrated workflow examples completed!")
    print("\nKey Takeaways:")
    print("  - Config loading with Jinja2 environment substitution")
    print("  - Structured logging with automatic context propagation")
    print("  - Cache decorator for automatic result memoization")
    print("  - Database session management with context managers")
    print("  - JSON serialization handling datetime/Decimal/Enum")
    print("  - Retry logic with exponential backoff")
    print("  - Comprehensive exception hierarchy")
    print("=" * 60)


if __name__ == "__main__":
    main()
