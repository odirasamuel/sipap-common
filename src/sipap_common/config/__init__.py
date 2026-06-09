"""Configuration loading module for SIPAP.

Provides Jinja2-based YAML configuration loading with environment variable substitution.
"""

from sipap_common.config.loader import load_config

__all__ = ["load_config"]
