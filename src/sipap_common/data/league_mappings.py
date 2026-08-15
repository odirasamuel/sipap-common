"""League and Competition Mappings Configuration.

Comprehensive mappings for 380 competitions covering:
- Country-to-leagues mapping
- Competition name aliases and variations
- Partial name matching

Used by orchestrator for interpreting user queries like:
- "Romania matches" → Liga I, Liga II, Cupa României, Supercupa
- "Europa League" → UEFA Europa League
- "EPL" → Premier League
- "Cupa României" → Cupa României (Romania Cup)
"""

# International/continental tournaments (API-Football labels as country="World")
# These should NOT be filtered by host country (e.g., "World Cup in Qatar" → country=None)
INTERNATIONAL_TOURNAMENTS: set[str] = {
    "uefa champions league",
    "uefa europa league",
    "uefa europa conference league",
    "uefa nations league",
    "uefa super cup",
    "uefa youth league",
    "uefa championship - women",
    "uefa championship - women - qualification",
    "uefa europa cup - women",
    "uefa nations league - women",
    "champions league women",
    "world cup",
    "world cup - women",
    "world cup - qualification",
    "world cup - u17",
    "world cup - u20",
    "euro championship",
    "euro championship - qualification",
    "copa america",
    "africa cup of nations",
    "asia cup",
    "asian cup",
    "concacaf gold cup",
    "concacaf nations league",
    "conmebol libertadores",
    "conmebol sudamericana",
    "caf champions league",
    "caf confederation cup",
    "afc champions league",
    "concacaf champions league",
    "fifa club world cup",
    "fifa intercontinental cup",
    "confederations cup",
    "arab cup",
    "friendlies",
    "friendlies clubs",
    "international champions cup",
}

# Country name variants for natural language queries
# Includes adjectives (Spanish, English, French, etc.) for user-friendly queries
# Comprehensive list covering 77 countries
COUNTRY_VARIANTS: dict[str, str] = {
    # Europe
    "albania": "Albania",
    "albanian": "Albania",
    "andorra": "Andorra",
    "andorran": "Andorra",
    "armenia": "Armenia",
    "armenian": "Armenia",
    "austria": "Austria",
    "austrian": "Austria",
    "spanish": "Spain",  # "Spanish LaLiga"
    "english": "England",  # "English Premier League"
    "french": "France",  # "French Ligue 1"
    "german": "Germany",  # "German Bundesliga"
    "italian": "Italy",  # "Italian Serie A"
    "portuguese": "Portugal",  # "Portuguese Liga"
    "dutch": "Netherlands",  # "Dutch Eredivisie"
    "belgian": "Belgium",  # "Belgian Pro League"
    "turkish": "Turkey",  # "Turkish Super Lig"
    "greek": "Greece",  # "Greek Super League"
    "scottish": "Scotland",  # "Scottish Premiership"
    "welsh": "Wales",  # "Welsh Premier League"
    "irish": "Ireland",  # "Irish Premier Division"
    "azerbaijan": "Azerbaijan",
    "belarus": "Belarus",
    "belgium": "Belgium",
    "bosnia": "Bosnia-and-Herzegovina",
    "bosnia-herzegovina": "Bosnia-and-Herzegovina",
    "bulgaria": "Bulgaria",
    "croatia": "Croatia",
    "cyprus": "Cyprus",
    "czech": "Czech-Republic",
    "denmark": "Denmark",
    "england": "England",
    "estonia": "Estonia",
    "faroe": "Faroe-Islands",
    "finland": "Finland",
    "france": "France",
    "georgia": "Georgia",
    "germany": "Germany",
    "gibraltar": "Gibraltar",
    "greece": "Greece",
    "hungary": "Hungary",
    "iceland": "Iceland",
    "ireland": "Ireland",
    "israel": "Israel",
    "italy": "Italy",
    "kosovo": "Kosovo",
    "latvia": "Latvia",
    "liechtenstein": "Liechtenstein",
    "lithuania": "Lithuania",
    "luxembourg": "Luxembourg",
    "malta": "Malta",
    "moldova": "Moldova",
    "montenegro": "Montenegro",
    "netherlands": "Netherlands",
    "norway": "Norway",
    "poland": "Poland",
    "portugal": "Portugal",
    "romania": "Romania",
    "russia": "Russia",
    "san-marino": "San-Marino",
    "scotland": "Scotland",
    "serbia": "Serbia",
    "slovakia": "Slovakia",
    "slovenia": "Slovenia",
    "spain": "Spain",
    "sweden": "Sweden",
    "switzerland": "Switzerland",
    "turkey": "Turkey",
    "ukraine": "Ukraine",
    "wales": "Wales",
    # Americas
    "argentina": "Argentina",
    "argentinian": "Argentina",
    "bolivian": "Bolivia",
    "bolivia": "Bolivia",
    "brazil": "Brazil",
    "brazilian": "Brazil",
    "canada": "Canada",
    "canadian": "Canada",
    "chile": "Chile",
    "chilean": "Chile",
    "colombia": "Colombia",
    "colombian": "Colombia",
    "costa-rica": "Costa-Rica",
    "costa-rican": "Costa-Rica",
    "ecuador": "Ecuador",
    "ecuadorian": "Ecuador",
    "jamaica": "Jamaica",
    "jamaican": "Jamaica",
    "mexico": "Mexico",
    "mexican": "Mexico",
    "paraguay": "Paraguay",
    "paraguayan": "Paraguay",
    "peru": "Peru",
    "peruvian": "Peru",
    "usa": "USA",
    "united-states": "USA",
    "american": "USA",
    "uruguay": "Uruguay",
    "uruguayan": "Uruguay",
    "venezuela": "Venezuela",
    "venezuelan": "Venezuela",
    # Asia
    "australia": "Australia",
    "bahrain": "Bahrain",
    "china": "China",
    "india": "India",
    "indonesia": "Indonesia",
    "iran": "Iran",
    "iraq": "Iraq",
    "japan": "Japan",
    "jordan": "Jordan",
    "kuwait": "Kuwait",
    "malaysia": "Malaysia",
    "qatar": "Qatar",
    "saudi": "Saudi-Arabia",
    "saudi-arabia": "Saudi-Arabia",
    "singapore": "Singapore",
    "south-korea": "South-Korea",
    "korea": "South-Korea",
    "thailand": "Thailand",
    "uae": "UAE",
    "vietnam": "Vietnam",
    # Africa
    "algeria": "Algeria",
    "egypt": "Egypt",
    "ghana": "Ghana",
    "kenya": "Kenya",
    "morocco": "Morocco",
    "nigeria": "Nigeria",
    "south-africa": "South-Africa",
    "tunisia": "Tunisia",
    "uganda": "Uganda",
    "zambia": "Zambia",
    "zimbabwe": "Zimbabwe",
}


# Country to leagues mapping (all countries with their competitions)
COUNTRY_TO_LEAGUES: dict[str, list[str]] = {
    # A
    "albania": ["Superliga", "Super Cup", "Cup"],
    "algeria": ["Ligue 1", "Ligue 2", "Super Cup", "Coupe de la Ligue", "Coupe Nationale"],
    "andorra": ["1a Divisió", "2a Divisió"],
    "argentina": [
        "Liga Profesional Argentina",
        "Copa de la Liga Profesional",
        "Copa de la Superliga",
        "Copa Argentina",
        "Primera Nacional",
    ],
    "armenia": ["Premier League", "Super Cup", "Cup"],
    "australia": ["A-League"],
    "austria": ["Bundesliga", "2. Liga", "Cup"],
    "azerbaijan": ["Premyer Liqa", "Cup"],

    # B
    "belarus": ["Premier League", "1. Division", "Coppa", "Super Cup"],
    "belgium": ["Jupiler Pro League", "Challenger Pro League", "Cup", "Super Cup"],
    "bolivia": ["Primera División", "Copa de la División Profesional"],
    "bosnia": ["Premijer Liga", "Cup", "Super Cup"],
    "brazil": [
        "Serie A",
        "Serie B",
        "Serie C",
        "Serie D",
        "Supercopa do Brasil",
        "Copa Do Brasil",
    ],
    "bulgaria": ["First League", "Second League", "Cup", "Super Cup"],

    # C
    "canada": ["Canadian Premier League", "Canadian Championship"],
    "chile": [
        "Primera División",
        "Segunda División",
        "Primera B",
        "Copa De La Liga",
        "Copa Chile",
        "Super Cup",
    ],
    "china": ["Super League", "League One", "League Two", "FA Cup", "Super Cup"],
    "colombia": ["Superliga", "Primera A", "Primera B", "Copa Colombia"],
    "costa-rica": ["Primera División", "Copa Costa Rica", "Supercopa"],
    "costa rica": ["Primera División", "Copa Costa Rica", "Supercopa"],
    "croatia": ["HNL", "First NL", "Cup", "Super Cup"],
    "cyprus": ["1. Division", "2. Division", "Cup", "Super Cup"],
    "czech-republic": ["Czech Liga", "FNL", "Cup", "Super Cup"],
    "czech republic": ["Czech Liga", "FNL", "Cup", "Super Cup"],
    "czechia": ["Czech Liga", "FNL", "Cup", "Super Cup"],

    # D
    "denmark": ["Superliga", "1. Division", "DBU Pokalen"],

    # E
    "ecuador": ["Liga Pro", "Liga Pro Serie B", "Copa Ecuador"],
    "egypt": ["Premier League", "Second League", "League Cup", "Cup"],
    "england": [
        "Premier League",
        "Championship",
        "League One",
        "League Two",
        "National League",
        "National League - North",
        "National League - South",
        "Women's Championship",
        "WSL Cup",
        "EFL Trophy",
        "FA Cup",
        "FA Trophy",
        "FA WSL",
        "League Cup",
        "National League Cup",
        "Community Shield",
        "Community Shield Women",
    ],
    "estonia": ["Meistriliiga", "Esiliiga A", "Cup"],

    # F
    "finland": ["Veikkausliiga", "Ykkösliiga", "Suomen Cup", "League Cup"],
    "france": [
        "Ligue 1",
        "Ligue 2",
        "National 1",
        "Coupe de France",
        "Coupe de la Ligue",
        "Feminine Division 1",
        "Trophée des Champions",
    ],

    # G
    "georgia": ["Erovnuli Liga", "Erovnuli Liga 2", "David Kipiani Cup", "Super Cup"],
    "germany": [
        "Bundesliga",
        "2. Bundesliga",
        "3. Liga",
        "DFB Pokal",
        "Super Cup",
        "Frauen Bundesliga",
        "DFB Pokal - Women",
    ],
    "greece": ["Super League 1", "Super League 2", "Super Cup", "Cup"],

    # H
    "honduras": ["Liga Nacional"],
    "hungary": ["NB I", "NB II", "Magyar Kupa"],

    # I
    "iceland": ["1. Deild", "2. Deild", "Cup", "League Cup", "Super Cup"],
    "indonesia": ["Liga 1", "Liga 2"],
    "iran": ["Persian Gulf Pro League", "Azadegan League", "Hazfi Cup", "Super Cup"],
    "ireland": [
        "Premier Division",
        "First Division",
        "League Cup",
        "FAI President's Cup",
        "FAI Cup",
    ],
    "israel": ["Ligat Ha'al", "Liga Leumit", "State Cup", "Super Cup"],
    "italy": [
        "Serie A",
        "Serie B",
        "Serie C - Girone A",
        "Serie C - Girone B",
        "Serie C - Girone C",
        "Coppa Italia",
        "Super Cup",
        "Serie A Women",
        "Serie A Cup Women",
        "Coppa Italia Women",
    ],

    # J
    "japan": ["J1 League", "J2 League", "J-League Cup", "Emperor Cup", "Super Cup"],

    # K
    "kazakhstan": ["Premier League", "1. Division", "Cup", "Super Cup"],
    "kuwait": ["Premier League", "Crown Prince Cup", "Emir Cup", "Super Cup"],

    # L
    "lithuania": ["A Lyga", "1 Lyga", "Cup", "Super Cup"],

    # M
    "malaysia": ["Super League", "Premier League", "Malaysia Cup", "FA Cup"],
    "mexico": ["Liga MX", "Copa por México", "Copa MX", "Campeón de Campeones"],
    "moldova": ["Super Liga", "Cupa"],
    "morocco": ["Botola Pro", "Botola 2", "Cup"],

    # N
    "netherlands": [
        "Eredivisie",
        "Eerste Divisie",
        "KNVB Beker",
        "Super Cup",
        "Eredivisie Women",
        "Super Cup Women",
    ],
    "northern-ireland": ["Premiership", "Championship", "Irish Cup", "League Cup"],
    "northern ireland": ["Premiership", "Championship", "Irish Cup", "League Cup"],
    "norway": ["Eliteserien", "1. Division", "NM Cupen", "Super Cup"],

    # P
    "paraguay": [
        "Division Profesional - Clausura",
        "Division Profesional - Apertura",
        "Copa Paraguay",
        "Supercopa",
    ],
    "peru": [
        "Primera División",
        "Segunda División",
        "Supercopa",
        "Copa De La Liga",
        "Copa Perú",
    ],
    "poland": ["Ekstraklasa", "I Liga", "Cup", "Super Cup"],
    "portugal": [
        "Primeira Liga",
        "Segunda Liga",
        "Taça da Liga",
        "Taça de Portugal",
        "Super Cup",
    ],

    # Q
    "qatar": [
        "Stars League",
        "Second Division",
        "Qatar Cup",
        "QSL Cup",
        "Emir Cup",
        "QFA Cup",
    ],

    # R
    "romania": ["Liga I", "Liga II", "Cupa României", "Supercupa"],
    "russia": ["Premier League", "First League", "Cup", "Super Cup"],

    # S
    "saudi-arabia": [
        "Pro League",
        "Division 1",
        "Crown Prince Cup",
        "Super Cup",
        "King's Cup",
    ],
    "saudi arabia": [
        "Pro League",
        "Division 1",
        "Crown Prince Cup",
        "Super Cup",
        "King's Cup",
    ],
    "scotland": [
        "Premiership",
        "Championship",
        "League One",
        "League Two",
        "FA Cup",
        "League Cup",
        "Challenge Cup",
    ],
    "serbia": ["Super Liga", "Prva Liga", "Cup"],
    "slovakia": ["Super Liga", "2. liga", "Cup"],
    "slovenia": ["1. SNL", "2. SNL", "Cup"],
    "south-africa": ["Premier Soccer League", "League Cup", "8 Cup"],
    "south africa": ["Premier Soccer League", "League Cup", "8 Cup"],
    "south-korea": ["K League 1", "K League 2", "FA Cup"],
    "south korea": ["K League 1", "K League 2", "FA Cup"],
    "korea": ["K League 1", "K League 2", "FA Cup"],
    "spain": [
        "La Liga",
        "Segunda División",
        "Primera División Femenina",
        "Copa del Rey",
        "Super Cup",
        "Supercopa Femenina",
    ],
    "sweden": ["Allsvenskan", "Superettan", "Svenska Cupen"],
    "switzerland": ["Super League", "Challenge League", "Schweizer Cup"],

    # T
    "thailand": ["Thai League 1", "FA Cup", "League Cup"],
    "tunisia": ["Ligue 1", "Ligue 2", "Super Cup", "Cup"],
    "turkey": ["Süper Lig", "1. Lig", "Türkiye Kupası", "Super Cup"],

    # U
    "usa": ["Major League Soccer"],
    "united states": ["Major League Soccer"],
    "ukraine": ["Premier League", "Persha Liga", "Cup", "Super Cup"],
    "united-arab-emirates": ["Pro League", "League Cup", "Super Cup"],
    "united arab emirates": ["Pro League", "League Cup", "Super Cup"],
    "uae": ["Pro League", "League Cup", "Super Cup"],
    "uruguay": [
        "Primera División - Clausura",
        "Primera División - Apertura",
        "Segunda División",
        "Copa Uruguay",
        "Super Copa",
    ],

    # V
    "venezuela": ["Primera División", "Segunda División", "Copa Venezuela", "Supercopa"],

    # W
    "wales": ["Premier League", "League Cup", "Welsh Cup"],
}

# Competition name aliases and variations
# Maps common abbreviations/variations to canonical competition names
LEAGUE_ALIASES: dict[str, str] = {
    # English Premier League
    "epl": "Premier League",
    "premier league": "Premier League",
    "english premier league": "Premier League",
    "pl": "Premier League",

    # Spanish La Liga
    "laliga": "La Liga",
    "la liga": "La Liga",
    "spanish la liga": "La Liga",
    "primera division": "La Liga",

    # German Bundesliga
    "bundesliga": "Bundesliga",
    "german bundesliga": "Bundesliga",
    "buli": "Bundesliga",

    # Italian Serie A
    "serie a": "Serie A",
    "italian serie a": "Serie A",
    "serie b": "Serie B",

    # French Ligue 1
    "ligue 1": "Ligue 1",
    "ligue 2": "Ligue 2",
    "french ligue 1": "Ligue 1",
    "l1": "Ligue 1",

    # UEFA Competitions
    "champions league": "UEFA Champions League",
    "ucl": "UEFA Champions League",
    "uefa champions league": "UEFA Champions League",
    "europa league": "UEFA Europa League",
    "uel": "UEFA Europa League",
    "uefa europa league": "UEFA Europa League",
    "conference league": "UEFA Europa Conference League",
    "uecl": "UEFA Europa Conference League",
    "uefa europa conference league": "UEFA Europa Conference League",
    "uefa conference league": "UEFA Europa Conference League",
    "nations league": "UEFA Nations League",
    "uefa nations league": "UEFA Nations League",
    "super cup": "UEFA Super Cup",
    "uefa super cup": "UEFA Super Cup",

    # International Tournaments
    "world cup": "World Cup",
    "euro": "Euro Championship",
    "euros": "Euro Championship",
    "euro championship": "Euro Championship",
    "european championship": "Euro Championship",
    "copa america": "Copa America",
    "afcon": "Africa Cup of Nations",
    "africa cup": "Africa Cup of Nations",
    "asian cup": "Asian Cup",
    "gold cup": "CONCACAF Gold Cup",
    "concacaf gold cup": "CONCACAF Gold Cup",

    # Friendlies
    "club friendlies": "Friendlies Clubs",
    "club friendly": "Friendlies Clubs",
    "friendlies clubs": "Friendlies Clubs",
    "international friendlies": "Friendlies",
    "international friendly": "Friendlies",
    "friendlies": "Friendlies",

    # South American Competitions
    "libertadores": "CONMEBOL Libertadores",
    "copa libertadores": "CONMEBOL Libertadores",
    "sudamericana": "CONMEBOL Sudamericana",
    "copa sudamericana": "CONMEBOL Sudamericana",

    # National Cups
    "fa cup": "FA Cup",
    "english fa cup": "FA Cup",
    "coupe de france": "Coupe de France",
    "french cup": "Coupe de France",
    "copa del rey": "Copa del Rey",
    "spanish cup": "Copa del Rey",
    "coppa italia": "Coppa Italia",
    "italian cup": "Coppa Italia",
    "dfb pokal": "DFB Pokal",
    "german cup": "DFB Pokal",
    "romania cup": "Cupa României",
    "romanian cup": "Cupa României",
    "cupa romaniei": "Cupa României",
    "cupa româniei": "Cupa României",
    "turkish cup": "Türkiye Kupası",
    "turkiye kupasi": "Türkiye Kupası",
    "turkey cup": "Türkiye Kupası",
    "egyptian cup": "Cup",  # Egypt
    "belgian cup": "Cup",  # Belgium
    "croatian cup": "Cup",  # Croatia

    # Other Leagues
    "eredivisie": "Eredivisie",
    "dutch league": "Eredivisie",
    "portuguese liga": "Primeira Liga",
    "liga nos": "Primeira Liga",
    "primeira liga": "Primeira Liga",
    "scottish premiership": "Premiership",
    "spfl": "Premiership",
    "mls": "Major League Soccer",
    "liga mx": "Liga MX",
    "mexican league": "Liga MX",
    "j-league": "J1 League",
    "j league": "J1 League",
    "j1": "J1 League",
    "j2": "J2 League",
    "k-league": "K League 1",
    "k league": "K League 1",
    "brazilian serie a": "Serie A",
    "campeonato brasileiro": "Serie A",
    "argentinian primera": "Liga Profesional Argentina",
    "superliga argentina": "Liga Profesional Argentina",
}

# Partial name matching patterns (case-insensitive)
# Used for fuzzy matching when user mentions part of competition name
PARTIAL_MATCH_PATTERNS: dict[str, str] = {
    "europa": "UEFA Europa League",
    "conference": "UEFA Europa Conference League",
    "champions": "UEFA Champions League",
    "nations": "UEFA Nations League",
    "libertadores": "CONMEBOL Libertadores",
    "sudamericana": "CONMEBOL Sudamericana",
    "romania": "Cupa României",  # Handles "Romania Cup" → Cupa României
    "turkish": "Türkiye Kupası",
    "magyar": "Magyar Kupa",
}


def get_leagues_for_country(country_name: str) -> list[str]:
    """Get all leagues/competitions for a country.

    Args:
        country_name: Country name (case-insensitive)

    Returns:
        List of league names for that country

    Example:
        >>> get_leagues_for_country("romania")
        ['Liga I', 'Liga II', 'Cupa României', 'Supercupa']
    """
    country_lower = country_name.lower()
    return COUNTRY_TO_LEAGUES.get(country_lower, [])


def resolve_league_alias(league_query: str) -> str:
    """Resolve league alias/abbreviation to canonical name.

    Args:
        league_query: User's league query (e.g., "EPL", "Europa League")

    Returns:
        Canonical league name, or original query if no match

    Example:
        >>> resolve_league_alias("EPL")
        'Premier League'
        >>> resolve_league_alias("Europa League")
        'UEFA Europa League'
    """
    query_lower = league_query.lower()

    # Exact match in aliases
    if query_lower in LEAGUE_ALIASES:
        return LEAGUE_ALIASES[query_lower]

    # Partial match patterns
    for pattern, canonical_name in PARTIAL_MATCH_PATTERNS.items():
        if pattern in query_lower:
            return canonical_name

    # No match - return original
    return league_query


def find_league_matches(query: str) -> list[str]:
    """Find all possible league matches from user query.

    Checks (in order):
    1. League aliases (e.g., "EPL" → "Premier League")
    2. Country mentions (e.g., "romania" → all Romanian leagues)
    3. Direct competition name mentions (e.g., "Cupa României" matches itself)
    4. Partial matches (e.g., "europa" → "UEFA Europa League")

    Args:
        query: User's query string

    Returns:
        List of matched league names (deduplicated)

    Example:
        >>> find_league_matches("romania matches today")
        ['Liga I', 'Liga II', 'Cupa României', 'Supercupa']
        >>> find_league_matches("europa league fixtures")
        ['UEFA Europa League']
        >>> find_league_matches("EPL results")
        ['Premier League']
        >>> find_league_matches("Cupa româniei results")
        ['Cupa României']
    """
    query_lower = query.lower()
    matched_leagues = []

    # 1. Check league aliases FIRST (e.g., "EPL" → "Premier League", "romanian cup" → "Cupa României")
    # This allows specific competition aliases to take priority over country mentions
    # Sort aliases by length (longest first) to match most specific first
    sorted_aliases = sorted(LEAGUE_ALIASES.items(), key=lambda x: len(x[0]), reverse=True)

    for alias, canonical in sorted_aliases:
        if alias in query_lower and canonical not in matched_leagues:
            matched_leagues.append(canonical)
            # For multi-word aliases or long aliases, return immediately to avoid partial matches
            # e.g., "europa league" should not also match "euro"
            if " " in alias or len(alias) > 6:
                return matched_leagues

    if matched_leagues:
        return matched_leagues  # Return if alias matches found

    # 2. Check country mentions (e.g., "romania" → all Romanian competitions)
    # Use word boundary matching to avoid "romanian" matching "romania"
    import re
    for country, leagues in COUNTRY_TO_LEAGUES.items():
        # Match country as whole word (with word boundaries)
        if re.search(rf'\b{re.escape(country)}\b', query_lower):
            matched_leagues.extend(leagues)
            return matched_leagues  # Return country leagues

    # 3. Check direct competition name mentions (exact or near-exact match)
    # Build list of all competition names from all countries
    all_competitions = set()
    for leagues in COUNTRY_TO_LEAGUES.values():
        all_competitions.update(leagues)

    # Sort by length (longest first) to match most specific names first
    # This prevents "Cup" from matching before "Cupa României"
    sorted_competitions = sorted(all_competitions, key=len, reverse=True)

    for competition in sorted_competitions:
        comp_lower = competition.lower()
        # Match if competition name appears as substring
        # This allows "cupa româniei results" to match "Cupa României"
        if comp_lower in query_lower and competition not in matched_leagues:
            matched_leagues.append(competition)
            # Only take the first (longest) match to avoid multiple Cup matches
            break

    return matched_leagues


# Database-specific mappings: League name → Database slug
# Used by sipap-data-mcp for querying the Aurora database
# Maps canonical league names to database league_id column values
LEAGUE_NAME_TO_DB_SLUG: dict[str, str] = {
    # England
    "Premier League": "premier-league",
    "Championship": "championship",
    "League One": "league-one",
    "League Two": "league-two",
    "FA Cup": "fa-cup",
    "League Cup": "league-cup",

    # Spain
    "La Liga": "laliga",
    "Segunda División": "segunda-division",
    "Copa del Rey": "copa-del-rey",

    # Germany
    "Bundesliga": "bundesliga",
    "2. Bundesliga": "2-bundesliga",
    "DFB Pokal": "dfb-pokal",

    # Italy
    "Serie A": "serie-a",
    "Serie B": "serie-b",
    "Coppa Italia": "coppa-italia",

    # France
    "Ligue 1": "ligue-1",
    "Ligue 2": "ligue-2",
    "Coupe de France": "coupe-de-france",

    # Netherlands
    "Eredivisie": "eredivisie",
    "Eerste Divisie": "eerste-divisie",
    "KNVB Beker": "knvb-beker",

    # Portugal
    "Primeira Liga": "liga-portugal",
    "Segunda Liga": "segunda-liga",
    "Taça de Portugal": "taca-de-portugal",

    # Scotland
    "Premiership": "scottish-premiership",

    # Turkey
    "Süper Lig": "super-lig",
    "Türkiye Kupası": "turkish-cup",

    # Belgium
    "Jupiler Pro League": "belgian-pro-league",

    # Sweden
    "Allsvenskan": "allsvenskan",
    "Superettan": "superettan",

    # Romania
    "Liga I": "liga-i",
    "Liga II": "liga-ii",
    "Cupa României": "cupa-romaniei",
    "Supercupa": "supercupa-romaniei",

    # International
    "UEFA Champions League": "uefa-champions-league",
    "UEFA Europa League": "uefa-europa-league",
    "UEFA Europa Conference League": "uefa-europa-conference-league",
    "UEFA Nations League": "uefa-nations-league",
    "Euro Championship": "euro-championship",
    "World Cup": "world-cup",

    # Add more as needed (380 total competitions)
    # TODO: Complete mapping for all 380 competitions
}


def league_name_to_db_slug(league_name: str) -> str | None:
    """Convert league name to database slug for querying.

    Args:
        league_name: Canonical league name (e.g., "Premier League")

    Returns:
        Database slug (e.g., "premier-league") or None if not found

    Example:
        >>> league_name_to_db_slug("Premier League")
        'premier-league'
        >>> league_name_to_db_slug("Cupa României")
        'cupa-romaniei'
    """
    return LEAGUE_NAME_TO_DB_SLUG.get(league_name)


def extract_country_from_query(query: str) -> str | None:
    """Extract country name from user query.

    Uses comprehensive COUNTRY_VARIANTS mapping (77 countries + adjectives)
    to identify country context in natural language queries.

    Args:
        query: User's query (e.g., "Spanish LaLiga fixtures", "Belarus league results")

    Returns:
        Official country name (e.g., "Spain", "Belarus") or None if not found

    Example:
        >>> extract_country_from_query("Spanish LaLiga fixtures")
        'Spain'
        >>> extract_country_from_query("Belarus league results")
        'Belarus'
        >>> extract_country_from_query("English Premier League")
        'England'
        >>> extract_country_from_query("Show me fixtures")
        None
    """
    query_lower = query.lower()

    # Search for country variants in query
    for variant, official_name in COUNTRY_VARIANTS.items():
        if variant in query_lower:
            return official_name

    return None


def is_generic_country_league_query(query: str) -> tuple[bool, str | None]:
    """Detect if query is asking for ALL leagues in a country vs specific league.

    CRITICAL DISTINCTION:
    - "Spanish League/Leagues" → ALL Spanish competitions (generic)
    - "Spanish La Liga" → ONLY La Liga (specific)
    - "English league" → ALL English competitions (generic)
    - "English Premier League" → ONLY Premier League (specific)

    This applies to ALL 77 countries to provide user-friendly behavior:
    - Casual users: "Show me Spanish league fixtures" → Gets all Spanish leagues
    - Expert users: "Show me La Liga fixtures" → Gets only La Liga

    Args:
        query: User's full query

    Returns:
        Tuple of (is_generic, country_name):
            - (True, "Spain") if generic "Spanish league/leagues" pattern
            - (False, None) if specific league mentioned

    Examples:
        >>> is_generic_country_league_query("Spanish league fixtures")
        (True, "Spain")
        >>> is_generic_country_league_query("Spanish leagues today")
        (True, "Spain")
        >>> is_generic_country_league_query("Spanish La Liga fixtures")
        (False, None)
        >>> is_generic_country_league_query("English league results")
        (True, "England")
        >>> is_generic_country_league_query("English Premier League")
        (False, None)
        >>> is_generic_country_league_query("Belarus league yesterday")
        (True, "Belarus")
    """
    import re

    query_lower = query.lower()

    # Pattern: [country variant] + league/leagues (with no specific league name after)
    # Examples: "spanish league", "english leagues", "german league fixtures"
    # NOT: "spanish la liga", "english premier league"

    # Check each country variant
    for variant, official_name in COUNTRY_VARIANTS.items():
        # Pattern: country word followed by "league" or "leagues" with word boundary
        # Must be followed by non-league-name words (fixtures, results, today, etc.)
        pattern = rf'\b{re.escape(variant)}\s+leagues?\b(?!\s+\w+\s+(league|cup|division|championship))'

        if re.search(pattern, query_lower):
            # Found generic pattern - verify no specific league name follows
            # Extract the part after "league/leagues"
            league_match = re.search(rf'\b{re.escape(variant)}\s+leagues?\s*(.*)$', query_lower)

            if league_match:
                remaining = league_match.group(1).strip()

                # Check if remaining text is just action words (not league names)
                action_words = {
                    'fixtures', 'results', 'matches', 'today', 'tomorrow',
                    'yesterday', 'for', 'on', 'this', 'next', 'last',
                    'week', 'weekend', 'show', 'me', 'get', 'find'
                }

                # If remaining words are ONLY action words, it's generic
                remaining_words = set(remaining.split())
                if not remaining_words or remaining_words.issubset(action_words):
                    return (True, official_name)

    return (False, None)


def find_similar_leagues(
    query: str,
    country: str | None = None,
    max_suggestions: int = 5,
) -> list[dict[str, str]]:
    """Find similar league names using fuzzy matching.

    Uses string similarity to suggest leagues when exact match fails.
    Useful for typos, partial names, or alternative phrasings.

    Args:
        query: User's league query (e.g., "spanis liga", "premere league")
        country: Optional country filter to narrow suggestions
        max_suggestions: Maximum number of suggestions to return (default: 5)

    Returns:
        List of suggestions with format and score:
            [
                {"league": "La Liga", "country": "Spain", "score": 85},
                {"league": "Premier League", "country": "England", "score": 75},
                ...
            ]

    Example:
        >>> suggestions = find_similar_leagues("spanis liga")
        >>> suggestions[0]["league"]
        'La Liga'
        >>> suggestions[0]["country"]
        'Spain'
    """
    from difflib import SequenceMatcher

    query_lower = query.lower()
    suggestions = []

    # Score function: simple string similarity
    def similarity_score(s1: str, s2: str) -> int:
        """Calculate similarity score (0-100) between two strings."""
        return int(SequenceMatcher(None, s1.lower(), s2.lower()).ratio() * 100)

    # Search in LEAGUE_ALIASES (comprehensive list of all league names and aliases)
    for alias, canonical in LEAGUE_ALIASES.items():
        alias_lower = alias.lower()

        # Skip if too short to match
        if len(query_lower) < 3 or len(alias_lower) < 3:
            continue

        # Calculate similarity
        score = similarity_score(query_lower, alias_lower)

        # Also check substring matching for phrases like "spanish la liga"
        if query_lower in alias_lower or alias_lower in query_lower:
            score = max(score, 75)  # Boost substring matches

        # Only suggest if similarity >= 60%
        if score >= 60:
            # Determine country for this league (if possible)
            league_country = None
            if country:
                # If country filter provided, only include leagues from that country
                if country.lower() in COUNTRY_TO_LEAGUES:
                    if canonical not in COUNTRY_TO_LEAGUES[country.lower()]:
                        continue  # Skip leagues not in this country
                    league_country = country
            else:
                # Try to find which country this league belongs to
                for c, leagues in COUNTRY_TO_LEAGUES.items():
                    if canonical in leagues:
                        league_country = c.title()
                        break

            suggestions.append({
                "league": canonical,
                "country": league_country or "International",
                "score": score,
                "alias_matched": alias,
            })

    # Sort by score (highest first) and deduplicate by canonical name
    suggestions.sort(key=lambda x: x["score"], reverse=True)

    # Deduplicate: keep only the highest-scoring match for each canonical league
    seen_leagues = set()
    unique_suggestions = []
    for s in suggestions:
        if s["league"] not in seen_leagues:
            seen_leagues.add(s["league"])
            unique_suggestions.append(s)

    # Return top N suggestions
    return unique_suggestions[:max_suggestions]


# League abbreviations for compact display (WhatsApp, mobile, etc.)
# Maps canonical league names to short abbreviations (3-6 chars)
LEAGUE_ABBREVIATIONS: dict[str, str] = {
    # Top European Leagues
    "Premier League": "PL",
    "La Liga": "LaLiga",
    "Serie A": "SerieA",
    "Bundesliga": "BuLi",
    "Ligue 1": "L1",
    "Ligue 2": "L2",
    "Championship": "Champ",
    "Eredivisie": "Erediv",
    "Primeira Liga": "Liga PT",
    "Belgian Pro League": "ProLg",
    "Jupiler Pro League": "ProLg",

    # Second Divisions
    "Segunda División": "LaLiga2",
    "Serie B": "SerieB",
    "2. Bundesliga": "2.BuLi",

    # Cups
    "FA Cup": "FAC",
    "League Cup": "EFL",
    "Copa del Rey": "CDR",
    "Coppa Italia": "CoppaIT",
    "DFB Pokal": "DFB",
    "Coupe de France": "CdF",

    # UEFA Competitions
    "UEFA Champions League": "UCL",
    "UEFA Europa League": "UEL",
    "UEFA Europa Conference League": "UECL",
    "UEFA Conference League": "UECL",
    "UEFA Nations League": "UNL",
    "UEFA Super Cup": "USC",

    # International
    "World Cup": "WC",
    "Euro Championship": "EURO",
    "Copa America": "CopaAm",
    "Africa Cup of Nations": "AFCON",
    "Asian Cup": "AsianC",

    # CONMEBOL
    "CONMEBOL Libertadores": "Libert",
    "CONMEBOL Sudamericana": "Sudam",

    # Other Major Leagues
    "Scottish Premiership": "SPFL",
    "Premiership": "SPFL",
    "Süper Lig": "TurLig",
    "Allsvenskan": "Allsv",
    "A-League": "A-Lg",

    # Eastern Europe
    "Liga I": "L1-RO",  # Romania
    "Premyer Liqa": "PL-AZ",  # Azerbaijan

    # International Friendlies
    "Friendlies": "Friend",
    "Friendlies Clubs": "FriendC",
}


def abbreviate_league(league_name: str, max_length: int = 20) -> str:
    """Get short abbreviation for league name.

    Uses LEAGUE_ABBREVIATIONS mapping for common leagues,
    falls back to truncation for unknown leagues.

    Args:
        league_name: Full league name (e.g., "Premier League", "UEFA Champions League")
        max_length: Maximum length for unknown leagues (default: 20)

    Returns:
        Abbreviated league name (3-20 chars)

    Example:
        >>> abbreviate_league("Premier League")
        'PL'
        >>> abbreviate_league("UEFA Champions League")
        'UCL'
        >>> abbreviate_league("Some Unknown League")
        'Some Unknown League'  # truncated to 20 chars if needed
    """
    # Check if we have a predefined abbreviation
    if league_name in LEAGUE_ABBREVIATIONS:
        return LEAGUE_ABBREVIATIONS[league_name]

    # Fallback: truncate to max_length
    return league_name[:max_length] if len(league_name) > max_length else league_name
