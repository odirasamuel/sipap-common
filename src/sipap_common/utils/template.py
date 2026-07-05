"""
Jinja2 template factory for SIPAP configuration management.

Provides environment variable substitution with ${ VARIABLE } syntax,
graceful degradation for missing variables, and template rendering.
"""

from jinja2 import Environment, Undefined


def create_jinja_env(env_vars: dict[str, str] | None = None) -> Environment:
    """
    Create Jinja2 environment configured for SIPAP template rendering.

    Configuration:
    - Variable syntax: ${ VARIABLE } (not {% %} or {{ }})
    - Undefined behavior: StrictUndefined (missing vars → empty string via template)
    - Globals: env_vars dict for substitution

    Args:
        env_vars: Dict of environment variables for substitution (default: {})

    Returns:
        Configured Jinja2 Environment

    Example:
        >>> env_vars = {"REGION": "us-east-1", "TABLE": "MyTable"}
        >>> env = create_jinja_env(env_vars)
        >>> template = env.from_string("region: ${ REGION }, table: ${ TABLE }")
        >>> result = template.render()
        >>> print(result)
        region: us-east-1, table: MyTable
    """
    if env_vars is None:
        env_vars = {}

    # Create Jinja2 environment with custom variable delimiters
    # Use default Undefined for graceful degradation (missing vars → empty string)
    env = Environment(
        variable_start_string="${",
        variable_end_string="}",
        undefined=Undefined,  # Not StrictUndefined - allows graceful degradation
    )

    # Add env_vars to globals for substitution
    env.globals.update(env_vars)

    return env


def render_template(template_str: str, env_vars: dict[str, str] | None = None) -> str:
    """
    Render Jinja2 template string with environment variable substitution.

    Convenience function for one-shot template rendering without creating
    an environment manually.

    Args:
        template_str: Template string with ${ VARIABLE } placeholders
        env_vars: Dict of environment variables for substitution (default: {})

    Returns:
        Rendered template string

    Example:
        >>> template = "database: ${ DB_NAME }, host: ${ DB_HOST }"
        >>> env_vars = {"DB_NAME": "sipap_prod", "DB_HOST": "localhost"}
        >>> result = render_template(template, env_vars)
        >>> print(result)
        database: sipap_prod, host: localhost

    Note:
        Missing variables render as empty string (graceful degradation):
        >>> render_template("value: ${ MISSING }", {})
        'value: '
    """
    if env_vars is None:
        env_vars = {}

    env = create_jinja_env(env_vars)
    template = env.from_string(template_str)
    return template.render()
