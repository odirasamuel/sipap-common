"""Tests for sipap_common.utils.json_utils module."""

from datetime import UTC, datetime
from decimal import Decimal
from enum import Enum

from sipap_common.utils.json_utils import safe_json_dumps, safe_json_loads


def test_safe_json_loads_valid_json() -> None:
    """Test parsing valid JSON string."""
    json_str = '{"name": "Arsenal", "points": 75}'
    result = safe_json_loads(json_str)

    assert result == {"name": "Arsenal", "points": 75}


def test_safe_json_loads_invalid_json_returns_default() -> None:
    """Test that invalid JSON returns default value."""
    json_str = "{invalid json"
    result = safe_json_loads(json_str, default={})

    assert result == {}


def test_safe_json_loads_invalid_json_returns_none() -> None:
    """Test that invalid JSON returns None by default."""
    json_str = "not json at all"
    result = safe_json_loads(json_str)

    assert result is None


def test_safe_json_loads_empty_string() -> None:
    """Test parsing empty string returns default."""
    result = safe_json_loads("", default={})

    assert result == {}


def test_safe_json_loads_null() -> None:
    """Test parsing JSON null."""
    result = safe_json_loads("null")

    assert result is None


def test_safe_json_loads_with_nested_objects() -> None:
    """Test parsing nested JSON structures."""
    json_str = '''
    {
        "match": {
            "id": "12345",
            "teams": ["Arsenal", "Chelsea"]
        },
        "predictions": [
            {"outcome": "home_win", "confidence": 0.75}
        ]
    }
    '''
    result = safe_json_loads(json_str)

    assert result["match"]["id"] == "12345"
    assert result["predictions"][0]["confidence"] == 0.75


def test_safe_json_dumps_basic_types() -> None:
    """Test serializing basic Python types."""
    data = {
        "string": "text",
        "integer": 42,
        "float": 3.14,
        "boolean": True,
        "null": None,
        "list": [1, 2, 3],
    }

    result = safe_json_dumps(data)
    parsed = safe_json_loads(result)

    assert parsed == data


def test_safe_json_dumps_with_datetime() -> None:
    """Test serializing datetime objects."""
    dt = datetime(2026, 6, 8, 12, 30, 45, tzinfo=UTC)
    data = {"timestamp": dt, "event": "match_start"}

    result = safe_json_dumps(data)
    parsed = safe_json_loads(result)

    # Datetime should be serialized as ISO 8601 string
    assert "2026-06-08T12:30:45" in parsed["timestamp"]
    assert parsed["event"] == "match_start"


def test_safe_json_dumps_with_enum() -> None:
    """Test serializing enum values."""

    class Sport(Enum):
        SOCCER = "soccer"
        BASKETBALL = "basketball"

    data = {"sport": Sport.SOCCER, "league": "Premier League"}

    result = safe_json_dumps(data)
    parsed = safe_json_loads(result)

    # Enum should be serialized as its value
    assert parsed["sport"] == "soccer"


def test_safe_json_dumps_with_decimal() -> None:
    """Test serializing Decimal values."""
    data = {"odds": Decimal("1.75"), "stake": Decimal("100.00")}

    result = safe_json_dumps(data)
    parsed = safe_json_loads(result)

    # Decimals should be serialized as floats
    assert parsed["odds"] == 1.75
    assert parsed["stake"] == 100.0


def test_safe_json_dumps_with_sets() -> None:
    """Test serializing set objects."""
    data = {"tags": {"sports", "soccer", "premier-league"}}

    result = safe_json_dumps(data)
    parsed = safe_json_loads(result)

    # Set should be serialized as list
    assert isinstance(parsed["tags"], list)
    assert len(parsed["tags"]) == 3
    assert "soccer" in parsed["tags"]


def test_safe_json_dumps_pretty_print() -> None:
    """Test pretty-printing JSON with indentation."""
    data = {"match": {"home": "Arsenal", "away": "Chelsea"}}

    result = safe_json_dumps(data, pretty=True)

    # Should have indentation (multiple lines)
    assert "\n" in result
    assert "  " in result  # Indentation spaces


def test_safe_json_dumps_ensure_ascii_false() -> None:
    """Test that Unicode characters are preserved."""
    data = {"team": "São Paulo", "city": "São Paulo"}

    result = safe_json_dumps(data, ensure_ascii=False)

    # Should contain actual Unicode characters
    assert "São" in result
    assert "\\u" not in result  # No escape sequences


def test_safe_json_dumps_ensure_ascii_true() -> None:
    """Test that Unicode characters are escaped."""
    data = {"team": "São Paulo"}

    result = safe_json_dumps(data, ensure_ascii=True)

    # Should contain escape sequences
    assert "\\u" in result


def test_safe_json_dumps_with_custom_object() -> None:
    """Test serializing custom objects falls back to string representation."""

    class Team:
        def __init__(self, name: str):
            self.name = name

        def __str__(self) -> str:
            return f"Team({self.name})"

    data = {"team": Team("Arsenal"), "league": "Premier League"}

    result = safe_json_dumps(data)
    parsed = safe_json_loads(result)

    # Custom object should be serialized as string
    assert "Arsenal" in parsed["team"]


def test_safe_json_dumps_nested_datetimes() -> None:
    """Test serializing nested structures with datetimes."""
    data = {
        "match": {
            "kickoff": datetime(2026, 6, 8, 15, 0, 0, tzinfo=UTC),
            "events": [
                {"time": datetime(2026, 6, 8, 15, 10, 0, tzinfo=UTC), "type": "goal"}
            ],
        }
    }

    result = safe_json_dumps(data)
    parsed = safe_json_loads(result)

    # All datetimes should be serialized
    assert "2026-06-08" in parsed["match"]["kickoff"]
    assert "2026-06-08" in parsed["match"]["events"][0]["time"]


def test_safe_json_dumps_with_bytes() -> None:
    """Test serializing bytes objects."""
    data = {"data": b"binary data"}

    result = safe_json_dumps(data)
    parsed = safe_json_loads(result)

    # Bytes should be decoded to string
    assert parsed["data"] == "binary data"


def test_safe_json_dumps_sort_keys() -> None:
    """Test that keys are sorted for deterministic output."""
    data = {"z": 1, "a": 2, "m": 3}

    result = safe_json_dumps(data, sort_keys=True)

    # Keys should appear in alphabetical order
    assert result.index('"a"') < result.index('"m"') < result.index('"z"')


def test_safe_json_roundtrip() -> None:
    """Test that dump/load roundtrip preserves data."""
    original = {
        "match_id": "12345",
        "teams": ["Arsenal", "Chelsea"],
        "odds": {"home": 1.75, "draw": 3.5, "away": 4.0},
        "active": True,
    }

    json_str = safe_json_dumps(original)
    parsed = safe_json_loads(json_str)

    assert parsed == original


def test_safe_json_loads_with_trailing_content() -> None:
    """Test parsing JSON with trailing non-JSON content."""
    json_str = '{"valid": "json"} extra content'

    # json.loads fails on trailing content, we return default gracefully
    result = safe_json_loads(json_str, default={})

    # Should return default value since JSON is malformed
    assert result == {}


def test_safe_json_dumps_empty_dict() -> None:
    """Test serializing empty dictionary."""
    result = safe_json_dumps({})

    assert result == "{}"


def test_safe_json_dumps_empty_list() -> None:
    """Test serializing empty list."""
    result = safe_json_dumps([])

    assert result == "[]"


def test_safe_json_dumps_none() -> None:
    """Test serializing None value."""
    result = safe_json_dumps(None)

    assert result == "null"


def test_safe_json_loads_array() -> None:
    """Test parsing JSON array."""
    json_str = '[1, 2, 3, "four"]'
    result = safe_json_loads(json_str)

    assert result == [1, 2, 3, "four"]


def test_safe_json_dumps_preserves_float_precision() -> None:
    """Test that float precision is preserved."""
    data = {"odds": 1.8534256}

    result = safe_json_dumps(data)
    parsed = safe_json_loads(result)

    # Should preserve precision
    assert abs(parsed["odds"] - 1.8534256) < 0.0000001
