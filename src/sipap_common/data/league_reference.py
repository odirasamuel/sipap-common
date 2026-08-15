"""League Reference with API-Football IDs.

This module provides a comprehensive reference of football leagues with their
API-Football IDs for unambiguous entity resolution.

The ID-first approach eliminates string matching brittleness:
- "La Liga" → ID 140 (always Spain)
- "Premier League" + "England" → ID 39
- "Premier League" + "Belarus" → ID 117

Usage:
    from sipap_common.data.league_reference import (
        resolve_league_query,
        get_league_by_id,
        get_leagues_for_country_by_id,
        LEAGUE_REFERENCE,
    )

    # Resolve user query to league IDs
    leagues = resolve_league_query("Spanish LaLiga")
    # Returns: [{"id": 140, "name": "La Liga", "country": "Spain", ...}]
"""

from typing import Any


# Master league reference with API-Football IDs
# Format: id, name, country, type, aliases, priority (for disambiguation)
LEAGUE_REFERENCE: list[dict[str, Any]] = [
    # ============================================================
    # TIER 1: TOP EUROPEAN LEAGUES (Most Common Queries)
    # ============================================================

    # England
    {
        "id": 39,
        "name": "Premier League",
        "country": "England",
        "type": "league",
        "tier": 1,
        "aliases": [
            "EPL", "English Premier League", "English league",
            "England Premier League", "PL", "Prem",
        ],
        "disambiguation": "Top tier English football - world's most watched league",
        "default_for_ambiguous": True,  # If "Premier League" alone, default to this
    },
    {
        "id": 40,
        "name": "Championship",
        "country": "England",
        "type": "league",
        "tier": 2,
        "aliases": ["EFL Championship", "English Championship", "English second division"],
        "disambiguation": "Second tier English football",
    },
    {
        "id": 41,
        "name": "League One",
        "country": "England",
        "type": "league",
        "tier": 3,
        "aliases": ["EFL League One", "English League One", "English third division"],
        "disambiguation": "Third tier English football",
    },
    {
        "id": 42,
        "name": "League Two",
        "country": "England",
        "type": "league",
        "tier": 4,
        "aliases": ["EFL League Two", "English League Two", "English fourth division"],
        "disambiguation": "Fourth tier English football",
    },
    {
        "id": 45,
        "name": "FA Cup",
        "country": "England",
        "type": "cup",
        "tier": 1,
        "aliases": ["English FA Cup", "The FA Cup"],
        "disambiguation": "English domestic cup competition",
    },
    {
        "id": 48,
        "name": "League Cup",
        "country": "England",
        "type": "cup",
        "tier": 2,
        "aliases": ["EFL Cup", "Carabao Cup", "English League Cup"],
        "disambiguation": "English League Cup",
    },

    # Spain
    {
        "id": 140,
        "name": "La Liga",
        "country": "Spain",
        "type": "league",
        "tier": 1,
        "aliases": [
            "LaLiga", "Spanish LaLiga", "Spanish La Liga", "Spanish league",
            "La Liga Santander", "LaLiga EA Sports", "Primera División",
            "Spain league", "Spain La Liga",
        ],
        "disambiguation": "Top tier Spanish football",
        "default_for_ambiguous": True,
    },
    {
        "id": 141,
        "name": "Segunda División",
        "country": "Spain",
        "type": "league",
        "tier": 2,
        "aliases": ["La Liga 2", "Spanish second division", "Segunda"],
        "disambiguation": "Second tier Spanish football",
    },
    {
        "id": 143,
        "name": "Copa del Rey",
        "country": "Spain",
        "type": "cup",
        "tier": 1,
        "aliases": ["Spanish cup", "King's Cup"],
        "disambiguation": "Spanish domestic cup",
    },

    # Italy
    {
        "id": 135,
        "name": "Serie A",
        "country": "Italy",
        "type": "league",
        "tier": 1,
        "aliases": [
            "Italian Serie A", "Italian league", "Italy league",
            "Serie A TIM", "Italy Serie A",
        ],
        "disambiguation": "Top tier Italian football",
        "default_for_ambiguous": True,  # If "Serie A" alone without Brazil context
    },
    {
        "id": 136,
        "name": "Serie B",
        "country": "Italy",
        "type": "league",
        "tier": 2,
        "aliases": ["Italian Serie B", "Italy Serie B", "Italian second division"],
        "disambiguation": "Second tier Italian football",
    },
    {
        "id": 137,
        "name": "Coppa Italia",
        "country": "Italy",
        "type": "cup",
        "tier": 1,
        "aliases": ["Italian Cup", "Italy Cup"],
        "disambiguation": "Italian domestic cup",
    },

    # Germany
    {
        "id": 78,
        "name": "Bundesliga",
        "country": "Germany",
        "type": "league",
        "tier": 1,
        "aliases": [
            "German Bundesliga", "German league", "Germany league",
            "1. Bundesliga",
        ],
        "disambiguation": "Top tier German football",
    },
    {
        "id": 79,
        "name": "2. Bundesliga",
        "country": "Germany",
        "type": "league",
        "tier": 2,
        "aliases": ["German second division", "Zweite Bundesliga"],
        "disambiguation": "Second tier German football",
    },
    {
        "id": 81,
        "name": "DFB Pokal",
        "country": "Germany",
        "type": "cup",
        "tier": 1,
        "aliases": ["German Cup", "Germany Cup", "DFB Cup"],
        "disambiguation": "German domestic cup",
    },

    # France
    {
        "id": 61,
        "name": "Ligue 1",
        "country": "France",
        "type": "league",
        "tier": 1,
        "aliases": [
            "French Ligue 1", "French league", "France league",
            "Ligue 1 Uber Eats", "France Ligue 1",
        ],
        "disambiguation": "Top tier French football",
    },
    {
        "id": 62,
        "name": "Ligue 2",
        "country": "France",
        "type": "league",
        "tier": 2,
        "aliases": ["French Ligue 2", "French second division"],
        "disambiguation": "Second tier French football",
    },
    {
        "id": 66,
        "name": "Coupe de France",
        "country": "France",
        "type": "cup",
        "tier": 1,
        "aliases": ["French Cup", "France Cup"],
        "disambiguation": "French domestic cup",
    },

    # Portugal
    {
        "id": 94,
        "name": "Primeira Liga",
        "country": "Portugal",
        "type": "league",
        "tier": 1,
        "aliases": [
            "Portuguese Primeira Liga", "Portuguese league", "Portugal league",
            "Liga Portugal", "Liga NOS", "Portugal Primeira Liga",
        ],
        "disambiguation": "Top tier Portuguese football",
    },

    # Netherlands
    {
        "id": 88,
        "name": "Eredivisie",
        "country": "Netherlands",
        "type": "league",
        "tier": 1,
        "aliases": [
            "Dutch Eredivisie", "Dutch league", "Netherlands league",
            "Holland league",
        ],
        "disambiguation": "Top tier Dutch football",
    },

    # ============================================================
    # TIER 1: UEFA COMPETITIONS
    # ============================================================
    {
        "id": 2,
        "name": "UEFA Champions League",
        "country": "Europe",
        "type": "cup",
        "tier": 1,
        "aliases": [
            "Champions League", "UCL", "CL", "European Cup",
        ],
        "disambiguation": "Premier European club competition",
    },
    {
        "id": 3,
        "name": "UEFA Europa League",
        "country": "Europe",
        "type": "cup",
        "tier": 1,
        "aliases": [
            "Europa League", "UEL", "EL",
        ],
        "disambiguation": "Secondary European club competition",
    },
    {
        "id": 848,
        "name": "UEFA Europa Conference League",
        "country": "Europe",
        "type": "cup",
        "tier": 2,
        "aliases": [
            "Conference League", "UECL", "Europa Conference",
        ],
        "disambiguation": "Third-tier European club competition",
    },

    # ============================================================
    # TIER 2: KEY LEAGUES WITH DISAMBIGUATION NEEDED
    # ============================================================

    # Belarus (important for disambiguation)
    {
        "id": 117,
        "name": "Premier League",
        "country": "Belarus",
        "type": "league",
        "tier": 1,
        "aliases": [
            "Belarus Premier League", "Belarusian Premier League",
            "Vysshaya Liga", "Belarus league", "Belarusian league",
        ],
        "disambiguation": "Top tier Belarusian football",
    },

    # Wales
    {
        "id": 113,
        "name": "Cymru Premier",
        "country": "Wales",
        "type": "league",
        "tier": 1,
        "aliases": [
            "Wales Premier League", "Welsh Premier League", "Welsh league",
            "Wales league",
        ],
        "disambiguation": "Top tier Welsh football",
    },

    # Scotland
    {
        "id": 179,
        "name": "Premiership",
        "country": "Scotland",
        "type": "league",
        "tier": 1,
        "aliases": [
            "Scottish Premiership", "Scottish Premier League", "SPL",
            "Scotland league", "Scottish league",
        ],
        "disambiguation": "Top tier Scottish football",
    },

    # Belgium
    {
        "id": 144,
        "name": "Jupiler Pro League",
        "country": "Belgium",
        "type": "league",
        "tier": 1,
        "aliases": [
            "Belgian Pro League", "Belgian league", "Belgium league",
            "First Division A",
        ],
        "disambiguation": "Top tier Belgian football",
    },

    # Turkey
    {
        "id": 203,
        "name": "Süper Lig",
        "country": "Turkey",
        "type": "league",
        "tier": 1,
        "aliases": [
            "Turkish Super Lig", "Turkish league", "Turkey league",
            "Super Lig",
        ],
        "disambiguation": "Top tier Turkish football",
    },

    # Greece
    {
        "id": 197,
        "name": "Super League 1",
        "country": "Greece",
        "type": "league",
        "tier": 1,
        "aliases": [
            "Greek Super League", "Greek league", "Greece league",
        ],
        "disambiguation": "Top tier Greek football",
    },

    # ============================================================
    # TIER 2: OTHER TOP LEAGUES
    # ============================================================

    # Brazil (important for Serie A disambiguation)
    {
        "id": 71,
        "name": "Serie A",
        "country": "Brazil",
        "type": "league",
        "tier": 1,
        "aliases": [
            "Brazilian Serie A", "Brasileirão", "Brazilian league",
            "Brazil league", "Brazil Serie A",
        ],
        "disambiguation": "Top tier Brazilian football",
    },

    # Argentina
    {
        "id": 128,
        "name": "Liga Profesional Argentina",
        "country": "Argentina",
        "type": "league",
        "tier": 1,
        "aliases": [
            "Argentine Primera División", "Argentine league",
            "Argentina league", "Liga Argentina",
        ],
        "disambiguation": "Top tier Argentine football",
    },

    # USA
    {
        "id": 253,
        "name": "Major League Soccer",
        "country": "USA",
        "type": "league",
        "tier": 1,
        "aliases": [
            "MLS", "American league", "USA league", "US league",
        ],
        "disambiguation": "Top tier American football",
    },

    # Mexico
    {
        "id": 262,
        "name": "Liga MX",
        "country": "Mexico",
        "type": "league",
        "tier": 1,
        "aliases": [
            "Mexican league", "Mexico league",
        ],
        "disambiguation": "Top tier Mexican football",
    },

    # Saudi Arabia
    {
        "id": 307,
        "name": "Saudi Pro League",
        "country": "Saudi-Arabia",
        "type": "league",
        "tier": 1,
        "aliases": [
            "Saudi league", "Saudi Arabia league", "Roshn Saudi League",
        ],
        "disambiguation": "Top tier Saudi Arabian football",
    },

    # ============================================================
    # INTERNATIONAL COMPETITIONS
    # ============================================================
    {
        "id": 1,
        "name": "World Cup",
        "country": "World",
        "type": "cup",
        "tier": 1,
        "aliases": ["FIFA World Cup", "WC"],
        "disambiguation": "FIFA Men's World Cup",
    },
    {
        "id": 4,
        "name": "Euro Championship",
        "country": "Europe",
        "type": "cup",
        "tier": 1,
        "aliases": ["European Championship", "Euros", "UEFA Euro"],
        "disambiguation": "UEFA European Championship",
    },
    {
        "id": 9,
        "name": "Copa America",
        "country": "South-America",
        "type": "cup",
        "tier": 1,
        "aliases": ["CONMEBOL Copa America"],
        "disambiguation": "South American national team competition",
    },
    {
        "id": 6,
        "name": "Africa Cup of Nations",
        "country": "Africa",
        "type": "cup",
        "tier": 1,
        "aliases": ["AFCON", "African Cup of Nations", "CAN"],
        "disambiguation": "African national team competition",
    },
]

# Build lookup indexes for fast access
_LEAGUE_BY_ID: dict[int, dict[str, Any]] = {
    league["id"]: league for league in LEAGUE_REFERENCE
}

_LEAGUES_BY_COUNTRY: dict[str, list[dict[str, Any]]] = {}
for league in LEAGUE_REFERENCE:
    country = league["country"].lower()
    if country not in _LEAGUES_BY_COUNTRY:
        _LEAGUES_BY_COUNTRY[country] = []
    _LEAGUES_BY_COUNTRY[country].append(league)

# Country name variants for normalization
_COUNTRY_VARIANTS: dict[str, str] = {
    "spanish": "spain",
    "english": "england",
    "french": "france",
    "german": "germany",
    "italian": "italy",
    "portuguese": "portugal",
    "dutch": "netherlands",
    "belgian": "belgium",
    "turkish": "turkey",
    "greek": "greece",
    "scottish": "scotland",
    "welsh": "wales",
    "belarusian": "belarus",
    "brazilian": "brazil",
    "argentine": "argentina",
    "argentinian": "argentina",
    "american": "usa",
    "mexican": "mexico",
    "saudi": "saudi-arabia",
}


def get_league_by_id(league_id: int) -> dict[str, Any] | None:
    """Get league details by API-Football ID.

    Args:
        league_id: API-Football league ID

    Returns:
        League dictionary or None if not found

    Example:
        >>> get_league_by_id(140)
        {"id": 140, "name": "La Liga", "country": "Spain", ...}
    """
    return _LEAGUE_BY_ID.get(league_id)


def get_leagues_for_country_by_id(country: str) -> list[dict[str, Any]]:
    """Get all leagues for a country.

    Args:
        country: Country name (case-insensitive, supports variants)

    Returns:
        List of league dictionaries with IDs

    Example:
        >>> get_leagues_for_country_by_id("Spain")
        [{"id": 140, "name": "La Liga", ...}, {"id": 141, ...}]
    """
    country_lower = country.lower()
    # Normalize country variants
    country_normalized = _COUNTRY_VARIANTS.get(country_lower, country_lower)
    return _LEAGUES_BY_COUNTRY.get(country_normalized, [])


def resolve_league_query(query: str) -> list[dict[str, Any]]:
    """Resolve user query to league(s) with API-Football IDs.

    This function handles:
    1. Direct league names: "La Liga" → ID 140
    2. Country + league: "Spanish La Liga" → ID 140
    3. Aliases: "EPL" → ID 39
    4. Ambiguous names with default: "Premier League" → ID 39 (England)
    5. Country-specific: "Belarus Premier League" → ID 117

    Args:
        query: User's league query (case-insensitive)

    Returns:
        List of matching league dictionaries, empty if no match

    Examples:
        >>> resolve_league_query("La Liga")
        [{"id": 140, "name": "La Liga", "country": "Spain", ...}]

        >>> resolve_league_query("Spanish LaLiga")
        [{"id": 140, "name": "La Liga", "country": "Spain", ...}]

        >>> resolve_league_query("EPL")
        [{"id": 39, "name": "Premier League", "country": "England", ...}]

        >>> resolve_league_query("Belarus Premier League")
        [{"id": 117, "name": "Premier League", "country": "Belarus", ...}]
    """
    query_lower = query.lower().strip()

    # Check for exact alias match first (highest priority)
    for league in LEAGUE_REFERENCE:
        # Check main name
        if league["name"].lower() == query_lower:
            return [league]

        # Check aliases
        for alias in league.get("aliases", []):
            if alias.lower() == query_lower:
                return [league]

    # Check for country + league pattern
    # Extract potential country from query
    detected_country = None
    for variant, normalized in _COUNTRY_VARIANTS.items():
        if variant in query_lower:
            detected_country = normalized
            break
    # Also check direct country names
    for country in _LEAGUES_BY_COUNTRY:
        if country in query_lower:
            detected_country = country
            break

    if detected_country:
        # Country detected - narrow down to that country's leagues
        country_leagues = _LEAGUES_BY_COUNTRY.get(detected_country, [])

        # Check if query contains a league name from this country
        for league in country_leagues:
            if league["name"].lower() in query_lower:
                return [league]
            for alias in league.get("aliases", []):
                if alias.lower() in query_lower:
                    return [league]

        # If country detected but no specific league, return all country leagues
        # This handles "Spanish leagues" or "Belarus league"
        if country_leagues:
            return country_leagues

    # Check for partial matches in league names (for ambiguous cases)
    matches = []
    for league in LEAGUE_REFERENCE:
        if league["name"].lower() in query_lower:
            matches.append(league)
        else:
            for alias in league.get("aliases", []):
                if alias.lower() in query_lower:
                    matches.append(league)
                    break

    if matches:
        # If multiple matches, prefer default_for_ambiguous
        defaults = [m for m in matches if m.get("default_for_ambiguous")]
        if defaults:
            return defaults
        return matches

    return []


def get_league_reference_for_prompt() -> str:
    """Generate a Claude-optimized league reference for NLU system prompt.

    Returns a formatted string with critical leagues for Claude to use
    in entity resolution.

    Returns:
        Formatted string for embedding in Claude's system prompt
    """
    lines = [
        "## LEAGUE REFERENCE (API-Football IDs)",
        "",
        "Use these IDs when resolving league mentions:",
        "",
        "### TOP EUROPEAN LEAGUES",
        "| ID | League | Country | Common Aliases |",
        "|----|--------|---------|----------------|",
    ]

    # Add top-tier European leagues
    top_european = [
        l for l in LEAGUE_REFERENCE
        if l.get("tier") == 1 and l["country"] in
        ["England", "Spain", "Italy", "Germany", "France", "Portugal", "Netherlands"]
    ]
    for league in top_european:
        aliases = ", ".join(league.get("aliases", [])[:3])
        lines.append(f"| {league['id']} | {league['name']} | {league['country']} | {aliases} |")

    lines.extend([
        "",
        "### UEFA COMPETITIONS",
        "| ID | Competition | Aliases |",
        "|----|-------------|---------|",
    ])
    uefa = [l for l in LEAGUE_REFERENCE if l["country"] == "Europe"]
    for league in uefa:
        aliases = ", ".join(league.get("aliases", [])[:3])
        lines.append(f"| {league['id']} | {league['name']} | {aliases} |")

    lines.extend([
        "",
        "### DISAMBIGUATION (Same Name, Different Countries)",
        "| League Name | Country | ID |",
        "|-------------|---------|-----|",
        "| Premier League | England | 39 (default) |",
        "| Premier League | Belarus | 117 |",
        "| Serie A | Italy | 135 (default) |",
        "| Serie A | Brazil | 71 |",
        "",
        "### RESOLUTION RULES",
        "1. 'Spanish LaLiga' or 'La Liga' → ID 140",
        "2. 'EPL' or 'English Premier League' → ID 39",
        "3. 'Belarus league' or 'Vysshaya Liga' → ID 117",
        "4. 'Premier League' (no country) → ID 39 (England, ask to clarify if uncertain)",
        "5. '[Country] league' → Return ALL league IDs for that country",
    ])

    return "\n".join(lines)


def get_country_league_ids(country: str) -> list[int]:
    """Get all API-Football league IDs for a country.

    Args:
        country: Country name (case-insensitive)

    Returns:
        List of API-Football league IDs

    Example:
        >>> get_country_league_ids("Spain")
        [140, 141, 143]  # La Liga, Segunda, Copa del Rey
    """
    leagues = get_leagues_for_country_by_id(country)
    return [league["id"] for league in leagues]


def get_sports_context_keywords() -> set[str]:
    """Get all unique keywords for sports context detection.

    Dynamically extracts ALL keywords from LEAGUE_REFERENCE - no hardcoding.
    Returns lowercase keywords for case-insensitive matching.

    Extracts:
    - All league names and their words
    - All country names from the reference
    - All aliases and their words

    Returns:
        Set of lowercase keywords

    Example:
        >>> keywords = get_sports_context_keywords()
        >>> "laliga" in keywords
        True
        >>> "spain" in keywords
        True
    """
    keywords: set[str] = set()

    for league in LEAGUE_REFERENCE:
        # Add league name (full and split into words)
        name = league.get("name", "")
        if name:
            keywords.add(name.lower())
            for word in name.lower().split():
                if len(word) > 2:  # Skip short words like "fc", "de"
                    keywords.add(word)

        # Add country (directly from LEAGUE_REFERENCE - no hardcoded mapping)
        country = league.get("country", "")
        if country:
            keywords.add(country.lower())

        # Add aliases (full and split into words)
        aliases = league.get("aliases", [])
        for alias in aliases:
            if alias:
                keywords.add(alias.lower())
                for word in alias.lower().split():
                    if len(word) > 2:
                        keywords.add(word)

    return keywords


# Export public API
__all__ = [
    "LEAGUE_REFERENCE",
    "get_league_by_id",
    "get_leagues_for_country_by_id",
    "resolve_league_query",
    "get_league_reference_for_prompt",
    "get_country_league_ids",
    "get_sports_context_keywords",
]
