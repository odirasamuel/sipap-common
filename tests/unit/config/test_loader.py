"""Tests for sipap_common.config.loader module."""

from pathlib import Path

import pytest

from sipap_common.config import load_config
from sipap_common.exceptions import ConfigurationError


def test_load_config_with_single_variable_substitution(tmp_path: Path) -> None:
    """Test loading config with single Jinja2 variable substitution."""
    config_file = tmp_path / "test.yml"
    config_file.write_text("region: ${ REGION }")

    result = load_config(str(config_file), env_vars={"REGION": "us-east-1"})

    assert result["region"] == "us-east-1"


def test_load_config_with_multiple_variable_substitutions(tmp_path: Path) -> None:
    """Test loading config with multiple Jinja2 variable substitutions."""
    config_file = tmp_path / "test.yml"
    config_content = """
    aws:
      region: ${ AWS_REGION }
      account: ${ AWS_ACCOUNT }
    app:
      name: ${ APP_NAME }
    """
    config_file.write_text(config_content)

    result = load_config(
        str(config_file),
        env_vars={"AWS_REGION": "us-west-2", "AWS_ACCOUNT": "123456", "APP_NAME": "sipap"}
    )

    assert result["aws"]["region"] == "us-west-2"
    assert result["aws"]["account"] == 123456  # YAML parses unquoted numbers as int
    assert result["app"]["name"] == "sipap"


def test_load_config_missing_variable_defaults_to_none(tmp_path: Path) -> None:
    """Test that missing environment variables become None (graceful degradation).

    Unquoted empty values in YAML are parsed as null/None. To get empty string,
    use quoted values: optional: "${ MISSING_VAR }"
    """
    config_file = tmp_path / "test.yml"
    config_file.write_text("optional: ${ MISSING_VAR }")

    result = load_config(str(config_file), env_vars={})

    assert result["optional"] is None  # YAML parses empty unquoted value as null


def test_load_config_missing_variable_with_quoted_value(tmp_path: Path) -> None:
    """Test that missing variables in quoted YAML values become empty strings."""
    config_file = tmp_path / "test.yml"
    config_file.write_text('optional: "${ MISSING_VAR }"')

    result = load_config(str(config_file), env_vars={})

    assert result["optional"] == ""  # Quoted in YAML, so preserved as empty string


def test_load_config_with_nested_yaml_structure(tmp_path: Path) -> None:
    """Test loading config with nested YAML structures."""
    config_file = tmp_path / "test.yml"
    config_content = """
    database:
      host: ${ DB_HOST }
      port: 5432
      credentials:
        username: ${ DB_USER }
        password: ${ DB_PASS }
    """
    config_file.write_text(config_content)

    result = load_config(
        str(config_file),
        env_vars={"DB_HOST": "localhost", "DB_USER": "admin", "DB_PASS": "secret"}
    )

    assert result["database"]["host"] == "localhost"
    assert result["database"]["port"] == 5432
    assert result["database"]["credentials"]["username"] == "admin"
    assert result["database"]["credentials"]["password"] == "secret"


def test_load_config_with_yaml_lists(tmp_path: Path) -> None:
    """Test loading config with YAML lists."""
    config_file = tmp_path / "test.yml"
    config_content = """
    environments:
      - name: dev
        region: ${ DEV_REGION }
      - name: prod
        region: ${ PROD_REGION }
    """
    config_file.write_text(config_content)

    result = load_config(
        str(config_file),
        env_vars={"DEV_REGION": "us-east-1", "PROD_REGION": "us-west-2"}
    )

    assert len(result["environments"]) == 2
    assert result["environments"][0]["name"] == "dev"
    assert result["environments"][0]["region"] == "us-east-1"
    assert result["environments"][1]["name"] == "prod"
    assert result["environments"][1]["region"] == "us-west-2"


def test_load_config_file_not_found_raises_configuration_error(tmp_path: Path) -> None:
    """Test that loading non-existent config file raises ConfigurationError."""
    non_existent_file = tmp_path / "does_not_exist.yml"

    with pytest.raises(ConfigurationError) as exc_info:
        load_config(str(non_existent_file), env_vars={})

    assert "not found" in str(exc_info.value).lower()


def test_load_config_invalid_yaml_raises_configuration_error(tmp_path: Path) -> None:
    """Test that invalid YAML syntax raises ConfigurationError."""
    config_file = tmp_path / "invalid.yml"
    config_file.write_text("invalid: yaml: content: [")

    with pytest.raises(ConfigurationError) as exc_info:
        load_config(str(config_file), env_vars={})

    assert "invalid yaml" in str(exc_info.value).lower()


def test_load_config_empty_file_returns_empty_dict(tmp_path: Path) -> None:
    """Test that loading empty config file returns empty dict."""
    config_file = tmp_path / "empty.yml"
    config_file.write_text("")

    result = load_config(str(config_file), env_vars={})

    assert result == {}


def test_load_config_with_mixed_substitution_and_literals(tmp_path: Path) -> None:
    """Test config with mix of variable substitution and literal values."""
    config_file = tmp_path / "test.yml"
    config_content = """
    service:
      name: sipap-orchestrator
      region: ${ AWS_REGION }
      timeout: 30
      debug: false
    """
    config_file.write_text(config_content)

    result = load_config(str(config_file), env_vars={"AWS_REGION": "eu-west-1"})

    assert result["service"]["name"] == "sipap-orchestrator"
    assert result["service"]["region"] == "eu-west-1"
    assert result["service"]["timeout"] == 30
    assert result["service"]["debug"] is False


def test_load_config_with_no_env_vars_provided(tmp_path: Path) -> None:
    """Test loading config when env_vars parameter is omitted."""
    config_file = tmp_path / "test.yml"
    config_file.write_text("key: value")

    result = load_config(str(config_file))

    assert result["key"] == "value"


def test_load_config_preserves_yaml_data_types(tmp_path: Path) -> None:
    """Test that YAML data types are preserved correctly."""
    config_file = tmp_path / "test.yml"
    config_content = """
    string_val: "hello"
    int_val: 42
    float_val: 3.14
    bool_val: true
    null_val: null
    list_val: [1, 2, 3]
    """
    config_file.write_text(config_content)

    result = load_config(str(config_file), env_vars={})

    assert isinstance(result["string_val"], str)
    assert isinstance(result["int_val"], int)
    assert isinstance(result["float_val"], float)
    assert isinstance(result["bool_val"], bool)
    assert result["null_val"] is None
    assert isinstance(result["list_val"], list)


def test_load_config_with_variable_in_string_context(tmp_path: Path) -> None:
    """Test variable substitution within larger string context."""
    config_file = tmp_path / "test.yml"
    config_file.write_text("url: https://${ HOST }:${ PORT }/api")

    result = load_config(str(config_file), env_vars={"HOST": "localhost", "PORT": "8080"})

    assert result["url"] == "https://localhost:8080/api"


def test_load_config_with_pathlib_path(tmp_path: Path) -> None:
    """Test that load_config accepts pathlib.Path objects."""
    config_file = tmp_path / "test.yml"
    config_file.write_text("key: ${ VALUE }")

    result = load_config(config_file, env_vars={"VALUE": "test"})

    assert result["key"] == "test"
