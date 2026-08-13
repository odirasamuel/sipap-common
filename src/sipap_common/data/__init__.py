"""Sports Data Module for SIPAP.

Contains sports-related data structures and mappings:
- League and competition mappings (380 competitions across 77 countries)
- Country-to-leagues mappings
- Competition name aliases and variations
- API-Football league ID mappings
"""

from sipap_common.data.league_mappings import (
    COUNTRY_TO_LEAGUES,
    LEAGUE_ALIASES,
    LEAGUE_NAME_TO_DB_SLUG,
    PARTIAL_MATCH_PATTERNS,
    find_league_matches,
    get_leagues_for_country,
    league_name_to_db_slug,
    resolve_league_alias,
)

__all__ = [
    "COUNTRY_TO_LEAGUES",
    "LEAGUE_ALIASES",
    "LEAGUE_NAME_TO_DB_SLUG",
    "PARTIAL_MATCH_PATTERNS",
    "find_league_matches",
    "get_leagues_for_country",
    "league_name_to_db_slug",
    "resolve_league_alias",
]
