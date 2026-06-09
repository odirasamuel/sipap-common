"""
Odds-related type definitions.

This module defines TypedDict classes for odds data structures.
"""

from datetime import datetime
from typing import TypedDict


class OddsData(TypedDict):
    """
    Odds data from a bookmaker for a specific market and outcome.

    Represents real-time or historical odds data used for +EV calculations
    and market analysis.

    Attributes:
        bookmaker: Name of the bookmaker (e.g., "Bet365", "Pinnacle")
        market: Betting market type (e.g., "Match Winner", "Over/Under 2.5")
        outcome: Specific outcome (e.g., "Home", "Over", "Yes")
        odds: Decimal odds value (e.g., 2.50 for 3/2)
        timestamp: When the odds were captured

    Example:
        >>> from datetime import datetime, UTC
        >>> odds: OddsData = {
        ...     "bookmaker": "Bet365",
        ...     "market": "Match Winner",
        ...     "outcome": "Home",
        ...     "odds": 2.50,
        ...     "timestamp": datetime.now(UTC)
        ... }
    """

    bookmaker: str
    market: str
    outcome: str
    odds: float
    timestamp: datetime
