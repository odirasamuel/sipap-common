"""League Reference with API-Football IDs.

Auto-generated from API-Football data on 2026-08-16.
All IDs verified against API-Football API.

Coverage: Top leagues from major footballing nations + international tournaments.

Usage:
    from sipap_common.data.league_reference import (
        resolve_league_query,
        get_league_by_id,
        get_leagues_for_country_by_id,
        LEAGUE_REFERENCE,
    )
"""

from typing import Any


# Master league reference with API-Football IDs
LEAGUE_REFERENCE: list[dict[str, Any]] = [
    # ============================================================
    # ENGLAND
    # ============================================================
    {
        "id": 39,
        "name": "Premier League",
        "country": "England",
        "type": "league",
        "tier": 1,
        "aliases": ["EPL", "English Premier League", "England Premier League", "PL", "Prem", "English league"],
        "default_for_ambiguous": True,
    },
    {
        "id": 40,
        "name": "Championship",
        "country": "England",
        "type": "league",
        "tier": 1,
    },
    {
        "id": 41,
        "name": "League One",
        "country": "England",
        "type": "league",
        "tier": 2,
    },
    {
        "id": 42,
        "name": "League Two",
        "country": "England",
        "type": "league",
        "tier": 2,
    },
    {
        "id": 43,
        "name": "National League",
        "country": "England",
        "type": "league",
        "tier": 3,
    },
    {
        "id": 45,
        "name": "FA Cup",
        "country": "England",
        "type": "cup",
        "tier": 3,
    },
    {
        "id": 48,
        "name": "League Cup",
        "country": "England",
        "type": "cup",
        "tier": 3,
    },
    {
        "id": 46,
        "name": "EFL Trophy",
        "country": "England",
        "type": "cup",
        "tier": 3,
    },
    {
        "id": 47,
        "name": "FA Trophy",
        "country": "England",
        "type": "cup",
        "tier": 3,
    },
    {
        "id": 528,
        "name": "Community Shield",
        "country": "England",
        "type": "cup",
        "tier": 3,
    },
    # ============================================================
    # SPAIN
    # ============================================================
    {
        "id": 140,
        "name": "La Liga",
        "country": "Spain",
        "type": "league",
        "tier": 1,
        "aliases": ["LaLiga", "Spanish La Liga", "Spanish LaLiga", "Spanish league", "La Liga Santander"],
        "default_for_ambiguous": True,
    },
    {
        "id": 141,
        "name": "Segunda División",
        "country": "Spain",
        "type": "league",
        "tier": 1,
    },
    {
        "id": 143,
        "name": "Copa del Rey",
        "country": "Spain",
        "type": "cup",
        "tier": 2,
    },
    {
        "id": 556,
        "name": "Super Cup",
        "country": "Spain",
        "type": "cup",
        "tier": 2,
    },
    {
        "id": 142,
        "name": "Primera División Femenina",
        "country": "Spain",
        "type": "league",
        "tier": 3,
    },
    # ============================================================
    # ITALY
    # ============================================================
    {
        "id": 135,
        "name": "Serie A",
        "country": "Italy",
        "type": "league",
        "tier": 1,
        "aliases": ["Italian Serie A", "Serie A TIM", "Italy Serie A", "Italian league"],
        "default_for_ambiguous": True,
    },
    {
        "id": 136,
        "name": "Serie B",
        "country": "Italy",
        "type": "league",
        "tier": 1,
    },
    {
        "id": 137,
        "name": "Coppa Italia",
        "country": "Italy",
        "type": "cup",
        "tier": 2,
    },
    {
        "id": 547,
        "name": "Super Cup",
        "country": "Italy",
        "type": "cup",
        "tier": 2,
    },
    {
        "id": 138,
        "name": "Serie C - Girone A",
        "country": "Italy",
        "type": "league",
        "tier": 3,
    },
    {
        "id": 942,
        "name": "Serie C - Girone B",
        "country": "Italy",
        "type": "league",
        "tier": 3,
    },
    {
        "id": 943,
        "name": "Serie C - Girone C",
        "country": "Italy",
        "type": "league",
        "tier": 3,
    },
    # ============================================================
    # GERMANY
    # ============================================================
    {
        "id": 78,
        "name": "Bundesliga",
        "country": "Germany",
        "type": "league",
        "tier": 1,
        "aliases": ["German Bundesliga", "German league"],
        "default_for_ambiguous": True,
    },
    {
        "id": 79,
        "name": "2. Bundesliga",
        "country": "Germany",
        "type": "league",
        "tier": 1,
    },
    {
        "id": 81,
        "name": "DFB Pokal",
        "country": "Germany",
        "type": "cup",
        "tier": 2,
    },
    {
        "id": 529,
        "name": "Super Cup",
        "country": "Germany",
        "type": "cup",
        "tier": 2,
    },
    {
        "id": 80,
        "name": "3. Liga",
        "country": "Germany",
        "type": "league",
        "tier": 3,
    },
    # ============================================================
    # FRANCE
    # ============================================================
    {
        "id": 61,
        "name": "Ligue 1",
        "country": "France",
        "type": "league",
        "tier": 1,
        "aliases": ["French Ligue 1", "French league"],
        "default_for_ambiguous": True,
    },
    {
        "id": 62,
        "name": "Ligue 2",
        "country": "France",
        "type": "league",
        "tier": 1,
    },
    {
        "id": 66,
        "name": "Coupe de France",
        "country": "France",
        "type": "cup",
        "tier": 2,
    },
    {
        "id": 526,
        "name": "Trophée des Champions",
        "country": "France",
        "type": "cup",
        "tier": 2,
    },
    {
        "id": 65,
        "name": "Coupe de la Ligue",
        "country": "France",
        "type": "cup",
        "tier": 3,
    },
    # ============================================================
    # PORTUGAL
    # ============================================================
    {
        "id": 94,
        "name": "Primeira Liga",
        "country": "Portugal",
        "type": "league",
        "tier": 1,
        "aliases": ["Primeira Liga", "Liga Portugal", "Portuguese league"],
    },
    {
        "id": 95,
        "name": "Segunda Liga",
        "country": "Portugal",
        "type": "league",
        "tier": 1,
    },
    {
        "id": 96,
        "name": "Taça de Portugal",
        "country": "Portugal",
        "type": "cup",
        "tier": 2,
    },
    {
        "id": 550,
        "name": "Super Cup",
        "country": "Portugal",
        "type": "cup",
        "tier": 2,
    },
    {
        "id": 97,
        "name": "Taça da Liga",
        "country": "Portugal",
        "type": "cup",
        "tier": 3,
    },
    # ============================================================
    # NETHERLANDS
    # ============================================================
    {
        "id": 88,
        "name": "Eredivisie",
        "country": "Netherlands",
        "type": "league",
        "tier": 1,
        "aliases": ["Eredivisie", "Dutch league"],
    },
    {
        "id": 89,
        "name": "Eerste Divisie",
        "country": "Netherlands",
        "type": "league",
        "tier": 1,
    },
    {
        "id": 90,
        "name": "KNVB Beker",
        "country": "Netherlands",
        "type": "cup",
        "tier": 2,
    },
    {
        "id": 543,
        "name": "Super Cup",
        "country": "Netherlands",
        "type": "cup",
        "tier": 2,
    },
    {
        "id": 91,
        "name": "Eredivisie Women",
        "country": "Netherlands",
        "type": "league",
        "tier": 3,
    },
    # ============================================================
    # BELGIUM
    # ============================================================
    {
        "id": 144,
        "name": "Jupiler Pro League",
        "country": "Belgium",
        "type": "league",
        "tier": 1,
        "aliases": ["Belgian Pro League", "Jupiler League", "Belgian league"],
    },
    {
        "id": 145,
        "name": "Challenger Pro League",
        "country": "Belgium",
        "type": "league",
        "tier": 1,
    },
    {
        "id": 147,
        "name": "Cup",
        "country": "Belgium",
        "type": "cup",
        "tier": 2,
    },
    {
        "id": 146,
        "name": "Super League Women",
        "country": "Belgium",
        "type": "league",
        "tier": 2,
    },
    # ============================================================
    # SCOTLAND
    # ============================================================
    {
        "id": 179,
        "name": "Premiership",
        "country": "Scotland",
        "type": "league",
        "tier": 1,
        "aliases": ["Scottish Premiership", "SPL", "Scottish league"],
    },
    {
        "id": 180,
        "name": "Championship",
        "country": "Scotland",
        "type": "league",
        "tier": 1,
    },
    {
        "id": 181,
        "name": "FA Cup",
        "country": "Scotland",
        "type": "cup",
        "tier": 2,
    },
    {
        "id": 185,
        "name": "League Cup",
        "country": "Scotland",
        "type": "cup",
        "tier": 2,
    },
    {
        "id": 183,
        "name": "League One",
        "country": "Scotland",
        "type": "league",
        "tier": 3,
    },
    {
        "id": 184,
        "name": "League Two",
        "country": "Scotland",
        "type": "league",
        "tier": 3,
    },
    # ============================================================
    # TURKEY
    # ============================================================
    {
        "id": 203,
        "name": "Süper Lig",
        "country": "Turkey",
        "type": "league",
        "tier": 1,
        "aliases": ["Turkish Super Lig", "Turkish league"],
    },
    {
        "id": 204,
        "name": "1. Lig",
        "country": "Turkey",
        "type": "league",
        "tier": 1,
    },
    {
        "id": 205,
        "name": "2. Lig",
        "country": "Turkey",
        "type": "league",
        "tier": 2,
    },
    {
        "id": 551,
        "name": "Super Cup",
        "country": "Turkey",
        "type": "cup",
        "tier": 2,
    },
    # ============================================================
    # GREECE
    # ============================================================
    {
        "id": 197,
        "name": "Super League 1",
        "country": "Greece",
        "type": "league",
        "tier": 1,
    },
    {
        "id": 198,
        "name": "Football League",
        "country": "Greece",
        "type": "league",
        "tier": 1,
    },
    # ============================================================
    # RUSSIA
    # ============================================================
    {
        "id": 235,
        "name": "Premier League",
        "country": "Russia",
        "type": "league",
        "tier": 1,
    },
    {
        "id": 236,
        "name": "First League",
        "country": "Russia",
        "type": "league",
        "tier": 1,
    },
    {
        "id": 237,
        "name": "Cup",
        "country": "Russia",
        "type": "cup",
        "tier": 2,
    },
    # ============================================================
    # UKRAINE
    # ============================================================
    {
        "id": 333,
        "name": "Premier League",
        "country": "Ukraine",
        "type": "league",
        "tier": 1,
    },
    {
        "id": 334,
        "name": "Persha Liga",
        "country": "Ukraine",
        "type": "league",
        "tier": 1,
    },
    {
        "id": 335,
        "name": "Cup",
        "country": "Ukraine",
        "type": "cup",
        "tier": 2,
    },
    # ============================================================
    # POLAND
    # ============================================================
    {
        "id": 106,
        "name": "Ekstraklasa",
        "country": "Poland",
        "type": "league",
        "tier": 1,
    },
    {
        "id": 107,
        "name": "I Liga",
        "country": "Poland",
        "type": "league",
        "tier": 1,
    },
    {
        "id": 108,
        "name": "Cup",
        "country": "Poland",
        "type": "cup",
        "tier": 2,
    },
    {
        "id": 109,
        "name": "II Liga - East",
        "country": "Poland",
        "type": "league",
        "tier": 2,
    },
    # ============================================================
    # AUSTRIA
    # ============================================================
    {
        "id": 218,
        "name": "Bundesliga",
        "country": "Austria",
        "type": "league",
        "tier": 1,
    },
    {
        "id": 219,
        "name": "2. Liga",
        "country": "Austria",
        "type": "league",
        "tier": 1,
    },
    {
        "id": 220,
        "name": "Cup",
        "country": "Austria",
        "type": "cup",
        "tier": 2,
    },
    # ============================================================
    # SWITZERLAND
    # ============================================================
    {
        "id": 207,
        "name": "Super League",
        "country": "Switzerland",
        "type": "league",
        "tier": 1,
    },
    {
        "id": 208,
        "name": "Challenge League",
        "country": "Switzerland",
        "type": "league",
        "tier": 1,
    },
    {
        "id": 209,
        "name": "Schweizer Cup",
        "country": "Switzerland",
        "type": "cup",
        "tier": 2,
    },
    # ============================================================
    # DENMARK
    # ============================================================
    {
        "id": 119,
        "name": "Superliga",
        "country": "Denmark",
        "type": "league",
        "tier": 1,
        "aliases": ["Danish Superliga", "Danish league"],
    },
    {
        "id": 120,
        "name": "1. Division",
        "country": "Denmark",
        "type": "league",
        "tier": 1,
    },
    {
        "id": 121,
        "name": "DBU Pokalen",
        "country": "Denmark",
        "type": "cup",
        "tier": 2,
    },
    # ============================================================
    # SWEDEN
    # ============================================================
    {
        "id": 113,
        "name": "Allsvenskan",
        "country": "Sweden",
        "type": "league",
        "tier": 1,
        "aliases": ["Allsvenskan", "Swedish league"],
    },
    {
        "id": 114,
        "name": "Superettan",
        "country": "Sweden",
        "type": "league",
        "tier": 1,
    },
    {
        "id": 115,
        "name": "Svenska Cupen",
        "country": "Sweden",
        "type": "cup",
        "tier": 2,
    },
    # ============================================================
    # NORWAY
    # ============================================================
    {
        "id": 103,
        "name": "Eliteserien",
        "country": "Norway",
        "type": "league",
        "tier": 1,
        "aliases": ["Eliteserien", "Norwegian league"],
    },
    {
        "id": 104,
        "name": "1. Division",
        "country": "Norway",
        "type": "league",
        "tier": 1,
    },
    {
        "id": 105,
        "name": "NM Cupen",
        "country": "Norway",
        "type": "cup",
        "tier": 2,
    },
    # ============================================================
    # BRAZIL
    # ============================================================
    {
        "id": 71,
        "name": "Serie A",
        "country": "Brazil",
        "type": "league",
        "tier": 1,
        "aliases": ["Brasileirao", "Brazilian Serie A", "Brazil Serie A", "Brazilian league"],
        "default_for_ambiguous": True,
    },
    {
        "id": 72,
        "name": "Serie B",
        "country": "Brazil",
        "type": "league",
        "tier": 1,
    },
    {
        "id": 73,
        "name": "Copa Do Brasil",
        "country": "Brazil",
        "type": "cup",
        "tier": 2,
    },
    {
        "id": 75,
        "name": "Serie C",
        "country": "Brazil",
        "type": "league",
        "tier": 2,
    },
    {
        "id": 74,
        "name": "Brasileiro Women",
        "country": "Brazil",
        "type": "league",
        "tier": 3,
    },
    {
        "id": 475,
        "name": "Paulista - A1",
        "country": "Brazil",
        "type": "league",
        "tier": 3,
    },
    {
        "id": 476,
        "name": "Paulista - A2",
        "country": "Brazil",
        "type": "league",
        "tier": 3,
    },
    {
        "id": 477,
        "name": "Gaúcho - 1",
        "country": "Brazil",
        "type": "league",
        "tier": 3,
    },
    {
        "id": 478,
        "name": "Gaúcho - 2",
        "country": "Brazil",
        "type": "league",
        "tier": 3,
    },
    # ============================================================
    # ARGENTINA
    # ============================================================
    {
        "id": 128,
        "name": "Liga Profesional Argentina",
        "country": "Argentina",
        "type": "league",
        "tier": 1,
        "aliases": ["Argentine Primera Division", "Argentine league"],
        "default_for_ambiguous": True,
    },
    {
        "id": 129,
        "name": "Primera Nacional",
        "country": "Argentina",
        "type": "league",
        "tier": 1,
    },
    {
        "id": 130,
        "name": "Copa Argentina",
        "country": "Argentina",
        "type": "cup",
        "tier": 2,
    },
    {
        "id": 131,
        "name": "Primera B Metropolitana",
        "country": "Argentina",
        "type": "league",
        "tier": 2,
    },
    {
        "id": 132,
        "name": "Primera C",
        "country": "Argentina",
        "type": "league",
        "tier": 3,
    },
    # ============================================================
    # MEXICO
    # ============================================================
    {
        "id": 262,
        "name": "Liga MX",
        "country": "Mexico",
        "type": "league",
        "tier": 1,
        "aliases": ["Liga MX", "Mexican league"],
    },
    {
        "id": 263,
        "name": "Liga de Expansión MX",
        "country": "Mexico",
        "type": "league",
        "tier": 1,
    },
    {
        "id": 264,
        "name": "Copa MX",
        "country": "Mexico",
        "type": "cup",
        "tier": 2,
    },
    {
        "id": 265,
        "name": "Primera División",
        "country": "Chile",
        "type": "league",
        "tier": 2,
    },
    # ============================================================
    # USA
    # ============================================================
    {
        "id": 253,
        "name": "Major League Soccer",
        "country": "USA",
        "type": "league",
        "tier": 1,
        "aliases": ["MLS", "US Soccer League", "American league"],
    },
    {
        "id": 254,
        "name": "NWSL Women",
        "country": "USA",
        "type": "league",
        "tier": 1,
    },
    {
        "id": 255,
        "name": "USL Championship",
        "country": "USA",
        "type": "league",
        "tier": 2,
    },
    {
        "id": 256,
        "name": "USL League Two",
        "country": "USA",
        "type": "league",
        "tier": 2,
    },
    {
        "id": 257,
        "name": "US Open Cup",
        "country": "USA",
        "type": "cup",
        "tier": 3,
    },
    # ============================================================
    # JAPAN
    # ============================================================
    {
        "id": 98,
        "name": "J1 League",
        "country": "Japan",
        "type": "league",
        "tier": 1,
        "aliases": ["J-League", "Japanese league"],
    },
    {
        "id": 99,
        "name": "J2 League",
        "country": "Japan",
        "type": "league",
        "tier": 1,
    },
    {
        "id": 100,
        "name": "J3 League",
        "country": "Japan",
        "type": "league",
        "tier": 2,
    },
    {
        "id": 101,
        "name": "J-League Cup",
        "country": "Japan",
        "type": "cup",
        "tier": 2,
    },
    {
        "id": 102,
        "name": "Emperor Cup",
        "country": "Japan",
        "type": "cup",
        "tier": 3,
    },
    # ============================================================
    # CHINA
    # ============================================================
    {
        "id": 169,
        "name": "Super League",
        "country": "China",
        "type": "league",
        "tier": 1,
    },
    {
        "id": 170,
        "name": "League One",
        "country": "China",
        "type": "league",
        "tier": 1,
    },
    # ============================================================
    # AUSTRALIA
    # ============================================================
    {
        "id": 188,
        "name": "A-League",
        "country": "Australia",
        "type": "league",
        "tier": 1,
    },
    {
        "id": 189,
        "name": "Capital Territory NPL",
        "country": "Australia",
        "type": "league",
        "tier": 1,
    },
    {
        "id": 190,
        "name": "A-League Women",
        "country": "Australia",
        "type": "league",
        "tier": 2,
    },
    # ============================================================
    # WORLD
    # ============================================================
    {
        "id": 1,
        "name": "World Cup",
        "country": "World",
        "type": "cup",
        "tier": 1,
        "aliases": ["World Cup", "FIFA World Cup"],
    },
    {
        "id": 2,
        "name": "UEFA Champions League",
        "country": "World",
        "type": "cup",
        "tier": 1,
        "aliases": ["UCL", "Champions League", "European Champions League"],
    },
    {
        "id": 3,
        "name": "UEFA Europa League",
        "country": "World",
        "type": "cup",
        "tier": 2,
        "aliases": ["UEL", "Europa League", "European League"],
    },
    {
        "id": 4,
        "name": "Euro Championship",
        "country": "World",
        "type": "cup",
        "tier": 2,
        "aliases": ["Euros", "European Championship", "UEFA Euro"],
    },
    {
        "id": 5,
        "name": "UEFA Nations League",
        "country": "World",
        "type": "cup",
        "tier": 3,
    },
    {
        "id": 6,
        "name": "Africa Cup of Nations",
        "country": "World",
        "type": "cup",
        "tier": 3,
        "aliases": ["Africa Cup", "AFCON", "African Cup of Nations"],
    },
    {
        "id": 7,
        "name": "Asian Cup",
        "country": "World",
        "type": "cup",
        "tier": 3,
    },
    {
        "id": 9,
        "name": "Copa America",
        "country": "World",
        "type": "cup",
        "tier": 3,
        "aliases": ["Copa America"],
    },
    {
        "id": 10,
        "name": "Friendlies",
        "country": "World",
        "type": "cup",
        "tier": 3,
    },
    {
        "id": 15,
        "name": "FIFA Club World Cup",
        "country": "World",
        "type": "cup",
        "tier": 3,
    },
    {
        "id": 848,
        "name": "UEFA Europa Conference League",
        "country": "World",
        "type": "cup",
        "tier": 3,
        "aliases": ["UECL", "Conference League", "Europa Conference League"],
    },
    {
        "id": 531,
        "name": "UEFA Super Cup",
        "country": "World",
        "type": "cup",
        "tier": 3,
    },
    {
        "id": 32,
        "name": "World Cup - Qualification Europe",
        "country": "World",
        "type": "cup",
        "tier": 3,
        "aliases": ["Club World Cup", "FIFA Club World Cup"],
    },
    {
        "id": 34,
        "name": "World Cup - Qualification South America",
        "country": "World",
        "type": "cup",
        "tier": 3,
    },
    {
        "id": 37,
        "name": "World Cup - Qualification Intercontinental Play-offs",
        "country": "World",
        "type": "cup",
        "tier": 3,
    },
    {
        "id": 38,
        "name": "UEFA U21 Championship",
        "country": "World",
        "type": "cup",
        "tier": 3,
    },
]


# Build lookup dictionaries for fast access
_LEAGUE_BY_ID: dict[int, dict[str, Any]] = {
    league["id"]: league for league in LEAGUE_REFERENCE
}

_LEAGUES_BY_COUNTRY: dict[str, list[dict[str, Any]]] = {}
for league in LEAGUE_REFERENCE:
    country = league["country"].lower()
    if country not in _LEAGUES_BY_COUNTRY:
        _LEAGUES_BY_COUNTRY[country] = []
    _LEAGUES_BY_COUNTRY[country].append(league)


# Country name variants mapping
_COUNTRY_VARIANTS: dict[str, str] = {
    "uk": "england",
    "britain": "england",
    "great britain": "england",
    "united kingdom": "england",
    "usa": "usa",
    "us": "usa",
    "america": "usa",
    "united states": "usa",
    "holland": "netherlands",
    "uae": "united-arab-emirates",
    "brasil": "brazil",
}


def get_league_by_id(league_id: int) -> dict[str, Any] | None:
    """Get league info by API-Football ID."""
    return _LEAGUE_BY_ID.get(league_id)


def get_leagues_for_country_by_id(country: str) -> list[dict[str, Any]]:
    """Get all leagues for a country."""
    country_lower = country.lower()
    country_normalized = _COUNTRY_VARIANTS.get(country_lower, country_lower)
    return _LEAGUES_BY_COUNTRY.get(country_normalized, [])


def resolve_league_query(query: str) -> list[dict[str, Any]]:
    """
    Resolve a user query to matching leagues.

    Args:
        query: User input like "La Liga", "Spanish league", "EPL"

    Returns:
        List of matching league dicts with API-Football IDs
    """
    query_lower = query.lower().strip()

    # Check for exact alias match first
    for league in LEAGUE_REFERENCE:
        aliases = league.get("aliases", [])
        if query_lower in [a.lower() for a in aliases]:
            return [league]

    # Check for name match
    for league in LEAGUE_REFERENCE:
        if query_lower == league["name"].lower():
            return [league]

    # Check for partial name match
    matches = []
    for league in LEAGUE_REFERENCE:
        if query_lower in league["name"].lower():
            matches.append(league)

    if matches:
        return matches

    # Check for country match
    country_leagues = get_leagues_for_country_by_id(query_lower)
    if country_leagues:
        return country_leagues

    # Check for "[country] league" pattern
    for country in _LEAGUES_BY_COUNTRY.keys():
        if f"{country} league" in query_lower or f"{country}n league" in query_lower:
            return _LEAGUES_BY_COUNTRY[country]

    return []


def get_country_league_ids(country: str) -> list[int]:
    """
    Get all league IDs for a country.

    Args:
        country: Country name (e.g., "Spain", "England", "Brazil")

    Returns:
        List of API-Football league IDs for the country
    """
    leagues = get_leagues_for_country_by_id(country)
    return [league["id"] for league in leagues]


def get_league_reference_for_prompt() -> str:
    """
    Get formatted league reference for LLM prompts.

    Returns:
        Formatted string listing all leagues by country for prompt injection
    """
    lines = ["Available leagues by country:\n"]

    # Group by country
    for country in sorted(_LEAGUES_BY_COUNTRY.keys()):
        leagues = _LEAGUES_BY_COUNTRY[country]
        league_names = [f"{l['name']} (ID: {l['id']})" for l in leagues]
        lines.append(f"{country.title()}: {', '.join(league_names)}")

    return "\n".join(lines)


def get_sports_context_keywords() -> list[str]:
    """
    Get keywords that indicate sports/football context.

    Returns:
        List of keywords for context detection
    """
    keywords = [
        # Match/fixture related
        "fixture", "fixtures", "match", "matches", "game", "games",
        "result", "results", "score", "scores", "standings", "table",
        # Prediction related
        "prediction", "predictions", "predict", "odds", "bet", "betting",
        # Time related
        "today", "tomorrow", "weekend", "tonight", "this week",
        # Competition types
        "league", "cup", "championship", "tournament", "derby",
        # Actions
        "playing", "plays", "vs", "versus", "against",
    ]

    # Add all league names and aliases
    for league in LEAGUE_REFERENCE:
        keywords.append(league["name"].lower())
        for alias in league.get("aliases", []):
            keywords.append(alias.lower())

    # Add all country names
    keywords.extend(_LEAGUES_BY_COUNTRY.keys())
    keywords.extend(_COUNTRY_VARIANTS.keys())

    return list(set(keywords))

