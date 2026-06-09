"""Configuration loader with Jinja2 template processing.

Provides YAML configuration loading with environment variable substitution using Jinja2
template syntax: ${ VARIABLE }

Adapted from Sentinel's template.py pattern.
"""

from pathlib import Path
from typing import Any, cast

import yaml
from jinja2 import Environment, Undefined

from sipap_common.exceptions import ConfigurationError


class SilentUndefined(Undefined):
    """Jinja2 undefined handler that returns empty string for missing variables.

    Enables graceful degradation when environment variables are not provided.
    """

    def __str__(self) -> str:
        """Return empty string for undefined variables."""
        return ""

    def __repr__(self) -> str:
        """Return empty string for undefined variables."""
        return ""


def load_config(
    config_path: str | Path,
    env_vars: dict[str, Any] | None = None
) -> dict[str, Any]:
    """Load YAML configuration with Jinja2 variable substitution.

    Uses Jinja2 template processing with ${ VARIABLE } syntax for environment
    variable substitution. Missing variables gracefully default to empty string.

    Args:
        config_path: Path to YAML configuration file
        env_vars: Dictionary of environment variables for substitution

    Returns:
        Parsed configuration as dictionary

    Raises:
        ConfigurationError: If file not found or YAML parsing fails

    Examples:
        >>> # config.yml contains: region: ${ AWS_REGION }
        >>> config = load_config("config.yml", env_vars={"AWS_REGION": "us-east-1"})
        >>> config["region"]
        'us-east-1'

        >>> # Missing variables default to empty string
        >>> config = load_config("config.yml", env_vars={})
        >>> config["region"]
        ''
    """
    if env_vars is None:
        env_vars = {}

    # Convert to Path object for consistent handling
    config_path = Path(config_path)

    # Check if file exists
    if not config_path.exists():
        raise ConfigurationError(f"Configuration file not found: {config_path}")

    # Read configuration file
    try:
        template_content = config_path.read_text(encoding="utf-8")
    except OSError as e:
        raise ConfigurationError(f"Failed to read configuration file {config_path}: {e}")

    # Create Jinja2 environment with custom settings
    env = Environment(
        variable_start_string="${",
        variable_end_string="}",
        undefined=SilentUndefined,  # Graceful degradation for missing vars
        autoescape=False,           # Don't escape YAML content
        trim_blocks=True,           # Clean up whitespace
        lstrip_blocks=True
    )

    # Render template with environment variables
    try:
        template = env.from_string(template_content)
        rendered_content = template.render(**env_vars)
    except Exception as e:
        raise ConfigurationError(f"Failed to process template in {config_path}: {e}")

    # Parse rendered YAML content
    try:
        result = yaml.safe_load(rendered_content)
        if result is None:
            result = {}
        return cast(dict[str, Any], result)
    except yaml.YAMLError as e:
        raise ConfigurationError(f"Invalid YAML in configuration file {config_path}: {e}")
