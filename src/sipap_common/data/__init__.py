"""Sports Data Module for SIPAP.

Contains sports-related data structures and mappings:
- League and competition mappings (380 competitions across 77 countries)
- Country-to-leagues mappings
- Competition name aliases and variations
- API-Football league ID reference (ID-first architecture)
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

# ID-first architecture: League reference with API-Football IDs
from sipap_common.data.league_reference import (
    LEAGUE_REFERENCE,
    get_country_league_ids,
    get_league_by_id,
    get_league_reference_for_prompt,
    get_leagues_for_country_by_id,
    resolve_league_query,
)

__all__ = [
    # Legacy string-based mappings
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
    # ID-first architecture (API-Football IDs)
    "LEAGUE_REFERENCE",
    "get_country_league_ids",
    "get_league_by_id",
    "get_league_reference_for_prompt",
    "get_leagues_for_country_by_id",
    "resolve_league_query",
]
