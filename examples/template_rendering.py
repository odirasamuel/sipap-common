"""
Example: Jinja2 Template Rendering for Configuration

Demonstrates how to:
1. Use ${ VARIABLE } syntax for environment variable substitution
2. Render YAML configuration files with Jinja2
3. Handle missing variables gracefully (empty string fallback)
4. Create reusable template environments

This pattern enables flexible configuration management with environment-specific
values substituted at runtime.
"""

from sipap_common.utils.template import create_jinja_env, render_template


def example_basic_template_substitution():
    """Example: Basic template variable substitution."""
    print("=" * 60)
    print("Example 1: Basic Template Substitution")
    print("=" * 60)

    template_str = """
    database:
      host: ${ DB_HOST }
      port: ${ DB_PORT }
      name: ${ DB_NAME }
    """

    env_vars = {
        "DB_HOST": "localhost",
        "DB_PORT": "5432",
        "DB_NAME": "sipap_prod"
    }

    result = render_template(template_str, env_vars)

    print("Template:")
    print(template_str)
    print("\nRendered:")
    print(result)

    print("\n✅ Variables substituted successfully")


def example_missing_variables_graceful_degradation():
    """Example: Missing variables render as empty string."""
    print("\n" + "=" * 60)
    print("Example 2: Graceful Degradation (Missing Variables)")
    print("=" * 60)

    template_str = """
    api:
      url: ${ API_URL }
      key: ${ API_KEY }
      timeout: ${ API_TIMEOUT }
    """

    # Only provide some variables
    env_vars = {
        "API_URL": "https://api.example.com"
        # API_KEY and API_TIMEOUT are missing
    }

    result = render_template(template_str, env_vars)

    print("Template:")
    print(template_str)
    print("\nEnv vars provided:")
    print(f"  API_URL: {env_vars.get('API_URL')}")
    print(f"  API_KEY: <not provided>")
    print(f"  API_TIMEOUT: <not provided>")
    print("\nRendered:")
    print(result)

    print("\n✅ Missing variables rendered as empty string (no errors)")


def example_whitespace_handling():
    """Example: Template handles whitespace in variable names."""
    print("\n" + "=" * 60)
    print("Example 3: Whitespace Handling")
    print("=" * 60)

    # Both formats work: ${ VAR } and ${VAR}
    template_with_spaces = "region: ${ REGION }, table: ${ TABLE }"
    template_without_spaces = "region: ${REGION}, table: ${TABLE}"

    env_vars = {
        "REGION": "us-east-1",
        "TABLE": "SIPAPTelemetry"
    }

    result1 = render_template(template_with_spaces, env_vars)
    result2 = render_template(template_without_spaces, env_vars)

    print("Template with spaces:    ", template_with_spaces)
    print("Template without spaces: ", template_without_spaces)
    print("\nBoth render to:")
    print(f"  {result1}")

    assert result1 == result2
    print("\n✅ Whitespace in variable names handled correctly")


def example_complex_yaml_config():
    """Example: Complete YAML configuration with multiple substitutions."""
    print("\n" + "=" * 60)
    print("Example 4: Complex YAML Configuration")
    print("=" * 60)

    template_str = """
    # SIPAP Configuration
    application:
      name: sipap-prediction-engine
      environment: ${ ENVIRONMENT }
      version: ${ APP_VERSION }

    database:
      aurora:
        host: ${ AURORA_HOST }
        port: ${ AURORA_PORT }
        database: ${ AURORA_DATABASE }
        user: ${ AURORA_USER }

    cache:
      redis:
        host: ${ REDIS_HOST }
        port: ${ REDIS_PORT }
        ttl: ${ REDIS_TTL }

    telemetry:
      enabled: ${ TELEMETRY_ENABLED }
      table: ${ TELEMETRY_TABLE }

    prediction:
      confidence_threshold: ${ CONFIDENCE_THRESHOLD }
      sources:
        - api-football
        - the-odds-api
        - thesportsdb
    """

    env_vars = {
        "ENVIRONMENT": "production",
        "APP_VERSION": "1.0.0",
        "AURORA_HOST": "sipap-prod.cluster-abc123.us-east-1.rds.amazonaws.com",
        "AURORA_PORT": "5432",
        "AURORA_DATABASE": "sipap",
        "AURORA_USER": "sipap_app",
        "REDIS_HOST": "sipap-prod.cache.amazonaws.com",
        "REDIS_PORT": "6379",
        "REDIS_TTL": "3600",
        "TELEMETRY_ENABLED": "true",
        "TELEMETRY_TABLE": "SIPAPTelemetry",
        "CONFIDENCE_THRESHOLD": "0.75"
    }

    result = render_template(template_str, env_vars)

    print("Rendered Configuration:")
    print(result)

    print("\n✅ Complex YAML config rendered successfully")


def example_reusable_environment():
    """Example: Create reusable Jinja2 environment."""
    print("\n" + "=" * 60)
    print("Example 5: Reusable Template Environment")
    print("=" * 60)

    # Create environment once
    env_vars = {
        "SERVICE_NAME": "sipap-data-mcp",
        "AWS_REGION": "us-east-1",
        "LOG_LEVEL": "INFO"
    }

    env = create_jinja_env(env_vars)

    # Use for multiple templates
    template1 = env.from_string("Service: ${ SERVICE_NAME }")
    template2 = env.from_string("Region: ${ AWS_REGION }")
    template3 = env.from_string("Log Level: ${ LOG_LEVEL }")

    print("Multiple templates with same environment:")
    print(f"  {template1.render()}")
    print(f"  {template2.render()}")
    print(f"  {template3.render()}")

    print("\n✅ Environment reused across multiple templates")


def example_preserving_literal_braces():
    """Example: Template preserves literal JSON braces."""
    print("\n" + "=" * 60)
    print("Example 6: Preserving Literal JSON Braces")
    print("=" * 60)

    template_str = '''
    {
      "match_id": "${ MATCH_ID }",
      "prediction_type": "${ PREDICTION_TYPE }",
      "metadata": {
        "confidence": ${ CONFIDENCE },
        "sources": ["api-football", "the-odds-api"]
      }
    }
    '''

    env_vars = {
        "MATCH_ID": "match_12345",
        "PREDICTION_TYPE": "1X2",
        "CONFIDENCE": "0.85"
    }

    result = render_template(template_str, env_vars)

    print("Template (JSON with variables):")
    print(template_str)
    print("\nRendered JSON:")
    print(result)

    # Verify it's valid JSON structure
    import json
    parsed = json.loads(result.strip())
    print(f"\n✅ Valid JSON: {parsed['match_id']}")


if __name__ == "__main__":
    print("\nJinja2 Template Rendering Examples")
    print("=" * 60)

    example_basic_template_substitution()
    example_missing_variables_graceful_degradation()
    example_whitespace_handling()
    example_complex_yaml_config()
    example_reusable_environment()
    example_preserving_literal_braces()

    print("\n" + "=" * 60)
    print("All examples completed successfully!")
    print("=" * 60)
    print("\nKey Takeaways:")
    print("- Use ${ VARIABLE } syntax for substitution")
    print("- Missing variables render as empty string (graceful)")
    print("- Works with YAML, JSON, and any text format")
    print("- Create reusable environments for efficiency")
    print("- Literal braces in JSON/YAML are preserved")
