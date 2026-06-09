"""
Match-related type definitions.

This module defines TypedDict classes for match data structures.
"""

from datetime import datetime
from typing import Literal, TypedDict

from sipap_common.types.common import Sport


class TeamReference(TypedDict):
    """
    Reference to a team with minimal identifying information.

    Used within Match objects to represent home and away teams without
    including full team data.

    Attributes:
        id: Unique identifier for the team
        name: Display name of the team

    Example:
        >>> team: TeamReference = {"id": "arsenal", "name": "Arsenal FC"}
    """

    id: str
    name: str


class Match(TypedDict):
    """
    Complete match information.

    Represents a scheduled, ongoing, or completed match between two teams.

    Attributes:
        id: Unique identifier for the match
        sport: Sport type (soccer, nba, nfl, tennis)
        league: League or competition name (e.g., "Premier League")
        season: Season identifier (e.g., "2025-2026")
        home_team: Home team reference
        away_team: Away team reference
        scheduled_at: Match start time (timezone-aware datetime)
        status: Current match status

    Example:
        >>> from datetime import datetime, UTC
        >>> match: Match = {
        ...     "id": "match-123",
        ...     "sport": Sport.SOCCER,
        ...     "league": "Premier League",
        ...     "season": "2025-2026",
        ...     "home_team": {"id": "arsenal", "name": "Arsenal"},
        ...     "away_team": {"id": "chelsea", "name": "Chelsea"},
        ...     "scheduled_at": datetime.now(UTC),
        ...     "status": "scheduled"
        ... }
    """

    id: str
    sport: Sport
    league: str
    season: str
    home_team: TeamReference
    away_team: TeamReference
    scheduled_at: datetime
    status: Literal["scheduled", "live", "completed", "postponed"]
