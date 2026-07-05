"""
Tests for Jinja2 template factory.

Tests environment variable substitution with ${ VARIABLE } syntax,
graceful degradation for missing variables, and template rendering.
"""


class TestJinja2TemplateFactory:
    """Test create_jinja_env() factory function."""

    def test_create_jinja_env_with_default_config(self):
        """Test creating Jinja2 environment with default configuration."""
        from sipap_common.utils.template import create_jinja_env

        env = create_jinja_env()

        assert env is not None
        assert env.variable_start_string == "${"
        assert env.variable_end_string == "}"

    def test_template_substitutes_environment_variables(self):
        """Test ${VARIABLE} syntax substitutes from env_vars dict."""
        from sipap_common.utils.template import create_jinja_env

        env_vars = {"REGION": "us-east-1", "TABLE_NAME": "MyTable"}
        env = create_jinja_env(env_vars)

        template_str = "region: ${ REGION }, table: ${ TABLE_NAME }"
        template = env.from_string(template_str)
        result = template.render()

        assert result == "region: us-east-1, table: MyTable"

    def test_missing_variable_renders_empty_string(self):
        """Test missing variables render as empty string (graceful degradation)."""
        from sipap_common.utils.template import create_jinja_env

        env_vars = {"REGION": "us-east-1"}
        env = create_jinja_env(env_vars)

        template_str = "region: ${ REGION }, missing: ${ MISSING_VAR }"
        template = env.from_string(template_str)
        result = template.render()

        assert result == "region: us-east-1, missing: "

    def test_template_handles_whitespace_in_variable_names(self):
        """Test ${VARIABLE} works with or without whitespace."""
        from sipap_common.utils.template import create_jinja_env

        env_vars = {"API_KEY": "secret123"}
        env = create_jinja_env(env_vars)

        # With spaces
        template1 = env.from_string("key: ${ API_KEY }")
        result1 = template1.render()
        assert result1 == "key: secret123"

        # Without spaces
        template2 = env.from_string("key: ${API_KEY}")
        result2 = template2.render()
        assert result2 == "key: secret123"

    def test_render_template_helper_function(self):
        """Test render_template() convenience function."""
        from sipap_common.utils.template import render_template

        template_str = "database: ${ DB_NAME }, host: ${ DB_HOST }"
        env_vars = {"DB_NAME": "sipap_prod", "DB_HOST": "localhost"}

        result = render_template(template_str, env_vars)

        assert result == "database: sipap_prod, host: localhost"

    def test_render_template_with_missing_variables(self):
        """Test render_template() handles missing variables gracefully."""
        from sipap_common.utils.template import render_template

        template_str = "api: ${ API_URL }, key: ${ API_KEY }"
        env_vars = {"API_URL": "https://api.example.com"}

        result = render_template(template_str, env_vars)

        assert result == "api: https://api.example.com, key: "

    def test_render_template_with_empty_env_vars(self):
        """Test render_template() with empty env_vars dict."""
        from sipap_common.utils.template import render_template

        template_str = "value: ${ SOME_VAR }"
        result = render_template(template_str, {})

        assert result == "value: "

    def test_template_preserves_literal_braces(self):
        """Test template preserves literal braces not in ${ } format."""
        from sipap_common.utils.template import render_template

        template_str = 'data: {"key": "${ VALUE }"}'
        env_vars = {"VALUE": "test"}

        result = render_template(template_str, env_vars)

        assert result == 'data: {"key": "test"}'

    def test_template_with_complex_yaml_structure(self):
        """Test template rendering with YAML-like structure."""
        from sipap_common.utils.template import render_template

        template_str = """
        database:
          host: ${ DB_HOST }
          port: ${ DB_PORT }
          name: ${ DB_NAME }
        api:
          key: ${ API_KEY }
          url: ${ API_URL }
        """

        env_vars = {
            "DB_HOST": "localhost",
            "DB_PORT": "5432",
            "DB_NAME": "sipap_prod",
            "API_KEY": "secret123",
            "API_URL": "https://api.example.com"
        }

        result = render_template(template_str, env_vars)

        assert "host: localhost" in result
        assert "port: 5432" in result
        assert "name: sipap_prod" in result
        assert "key: secret123" in result
        assert "url: https://api.example.com" in result

    def test_template_undefined_behavior_allows_graceful_degradation(self):
        """Test jinja undefined behavior uses Undefined for graceful degradation."""
        from jinja2 import Undefined

        from sipap_common.utils.template import create_jinja_env

        env_vars = {}
        env = create_jinja_env(env_vars)

        # Check that undefined class is Undefined (not StrictUndefined)
        assert env.undefined == Undefined

    def test_template_with_numeric_values(self):
        """Test template handles numeric values in env_vars."""
        from sipap_common.utils.template import render_template

        template_str = "port: ${ PORT }, timeout: ${ TIMEOUT }"
        env_vars = {"PORT": "8080", "TIMEOUT": "30"}

        result = render_template(template_str, env_vars)

        assert result == "port: 8080, timeout: 30"
