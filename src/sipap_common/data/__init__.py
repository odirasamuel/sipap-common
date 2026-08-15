"""Sports Data Module for SIPAP.

Contains sports-related data structures and mappings:
- League and competition mappings (380 competitions across 77 countries)
- Country-to-leagues mappings
- Competition name aliases and variations
- API-Football league ID mappings
"""

from sipap_common.data.league_mappings import (
    COUNTRY_TO_LEAGUES,
    COUNTRY_VARIANTS,
    INTERNATIONAL_TOURNAMENTS,
    LEAGUE_ABBREVIATIONS,
    LEAGUE_ALIASES,
    LEAGUE_NAME_TO_DB_SLUG,
    PARTIAL_MATCH_PATTERNS,
    abbreviate_league,
    extract_country_from_query,
    find_league_matches,
    find_similar_leagues,
    get_leagues_for_country,
    is_generic_country_league_query,
    league_name_to_db_slug,
    resolve_league_alias,
)

__all__ = [
    "COUNTRY_TO_LEAGUES",
    "COUNTRY_VARIANTS",
    "INTERNATIONAL_TOURNAMENTS",
    "LEAGUE_ABBREVIATIONS",
    "LEAGUE_ALIASES",
    "LEAGUE_NAME_TO_DB_SLUG",
    "PARTIAL_MATCH_PATTERNS",
    "abbreviate_league",
    "extract_country_from_query",
    "find_league_matches",
    "find_similar_leagues",
    "get_leagues_for_country",
    "is_generic_country_league_query",
    "league_name_to_db_slug",
    "resolve_league_alias",
]
