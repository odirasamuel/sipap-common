"""
Common type definitions for SIPAP platform.

This module defines shared types and enums used across the platform.
"""

from enum import Enum


class Sport(str, Enum):
    """
    Supported sports in the SIPAP platform.

    The Sport enum inherits from both str and Enum to enable:
    - Direct string comparison (sport == "soccer")
    - JSON serialization without custom encoders
    - Type safety in function signatures

    Example:
        >>> sport = Sport.SOCCER
        >>> assert sport == "soccer"
        >>> assert sport.value == "soccer"
        >>> assert Sport("soccer") == Sport.SOCCER
    """

    SOCCER = "soccer"
    NBA = "nba"
    NFL = "nfl"
    TENNIS = "tennis"
