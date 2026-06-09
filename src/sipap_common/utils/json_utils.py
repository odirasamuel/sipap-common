"""JSON utilities for SIPAP.

Provides safe JSON serialization/deserialization with custom encoders for
datetime, Decimal, Enum, and other non-standard types.
"""

import json
from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import Any


class CustomJSONEncoder(json.JSONEncoder):
    """Custom JSON encoder for non-standard types.

    Handles:
    - datetime objects (converts to ISO 8601 strings)
    - Decimal objects (converts to float)
    - Enum objects (converts to value)
    - set objects (converts to list)
    - bytes objects (decodes to string)
    - Other objects (converts to string representation)
    """

    def default(self, obj: Any) -> Any:
        """Convert non-serializable objects to JSON-compatible types."""
        # Handle datetime objects
        if isinstance(obj, datetime):
            return obj.isoformat()

        # Handle Decimal (common in financial calculations)
        if isinstance(obj, Decimal):
            return float(obj)

        # Handle Enum objects
        if isinstance(obj, Enum):
            return obj.value

        # Handle sets (convert to list)
        if isinstance(obj, set):
            return list(obj)

        # Handle bytes (decode to string)
        if isinstance(obj, bytes):
            try:
                return obj.decode("utf-8")
            except UnicodeDecodeError:
                return str(obj)

        # Fallback to string representation
        return str(obj)


def safe_json_dumps(
    obj: Any,
    pretty: bool = False,
    sort_keys: bool = False,
    ensure_ascii: bool = False,
) -> str:
    """Safely serialize object to JSON string.

    Args:
        obj: Object to serialize
        pretty: Pretty-print with indentation (default False)
        sort_keys: Sort dictionary keys alphabetically (default False)
        ensure_ascii: Escape non-ASCII characters (default False)

    Returns:
        JSON string

    Examples:
        >>> data = {"team": "Arsenal", "points": 75}
        >>> safe_json_dumps(data)
        '{"team": "Arsenal", "points": 75}'

        >>> from datetime import datetime, timezone
        >>> data = {"timestamp": datetime(2026, 6, 8, 12, 0, 0, tzinfo=timezone.utc)}
        >>> safe_json_dumps(data)
        '{"timestamp": "2026-06-08T12:00:00+00:00"}'
    """
    indent = 2 if pretty else None

    return json.dumps(
        obj,
        cls=CustomJSONEncoder,
        indent=indent,
        sort_keys=sort_keys,
        ensure_ascii=ensure_ascii,
    )


def safe_json_loads(json_str: str, default: Any = None) -> Any:
    """Safely parse JSON string to Python object.

    Args:
        json_str: JSON string to parse
        default: Default value to return on parse error (default None)

    Returns:
        Parsed Python object or default value on error

    Examples:
        >>> safe_json_loads('{"name": "Arsenal"}')
        {'name': 'Arsenal'}

        >>> safe_json_loads('invalid json', default={})
        {}

        >>> safe_json_loads('', default=None)
        None
    """
    if not json_str or not json_str.strip():
        return default

    try:
        return json.loads(json_str)
    except json.JSONDecodeError:
        return default
