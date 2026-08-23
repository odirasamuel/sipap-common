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
    # ARMENIA
    # ============================================================
    {
        "id": 342,
        "name": "Premier League",
        "country": "Armenia",
        "type": "league",
        "tier": 1,
    },
    {
        "id": 343,
        "name": "First League",
        "country": "Armenia",
        "type": "league",
        "tier": 2,
    },
    {
        "id": 654,
        "name": "Super Cup",
        "country": "Armenia",
        "type": "cup",
        "tier": 1,
    },
    {
        "id": 709,
        "name": "Cup",
        "country": "Armenia",
        "type": "cup",
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
    # ============================================================
    # ALBANIA
    # ============================================================
    {
        "id": 310,
        "name": "Superliga",
        "country": "Albania",
        "type": "league",
    },
    {
        "id": 708,
        "name": "Super Cup",
        "country": "Albania",
        "type": "cup",
    },
    {
        "id": 707,
        "name": "Cup",
        "country": "Albania",
        "type": "cup",
    },
    # ============================================================
    # ALGERIA
    # ============================================================
    {
        "id": 186,
        "name": "Ligue 1",
        "country": "Algeria",
        "type": "league",
    },
    {
        "id": 187,
        "name": "Ligue 2",
        "country": "Algeria",
        "type": "league",
    },
    {
        "id": 516,
        "name": "Super Cup",
        "country": "Algeria",
        "type": "cup",
    },
    {
        "id": 832,
        "name": "Coupe de la Ligue",
        "country": "Algeria",
        "type": "cup",
    },
    {
        "id": 514,
        "name": "Coupe Nationale",
        "country": "Algeria",
        "type": "cup",
    },
    # ============================================================
    # ANDORRA
    # ============================================================
    {
        "id": 312,
        "name": "1a Divisió",
        "country": "Andorra",
        "type": "league",
    },
    {
        "id": 313,
        "name": "2a Divisió",
        "country": "Andorra",
        "type": "league",
    },
    # ============================================================
    # ARGENTINA (Additional)
    # ============================================================
    {
        "id": 1032,
        "name": "Copa de la Liga Profesional",
        "country": "Argentina",
        "type": "league",
    },
    {
        "id": 483,
        "name": "Copa de la Superliga",
        "country": "Argentina",
        "type": "cup",
    },
    # ============================================================
    # AZERBAIJAN
    # ============================================================
    {
        "id": 419,
        "name": "Premyer Liqa",
        "country": "Azerbaijan",
        "type": "league",
    },
    {
        "id": 420,
        "name": "Cup",
        "country": "Azerbaijan",
        "type": "cup",
    },
    # ============================================================
    # BELARUS
    # ============================================================
    {
        "id": 116,
        "name": "Premier League",
        "country": "Belarus",
        "type": "league",
    },
    {
        "id": 117,
        "name": "1. Division",
        "country": "Belarus",
        "type": "league",
    },
    {
        "id": 486,
        "name": "Coppa",
        "country": "Belarus",
        "type": "cup",
    },
    {
        "id": 812,
        "name": "Super Cup",
        "country": "Belarus",
        "type": "cup",
    },
    # ============================================================
    # BELGIUM (Additional)
    # ============================================================
    {
        "id": 519,
        "name": "Super Cup",
        "country": "Belgium",
        "type": "cup",
    },
    # ============================================================
    # BOLIVIA
    # ============================================================
    {
        "id": 344,
        "name": "Primera División",
        "country": "Bolivia",
        "type": "league",
    },
    {
        "id": 964,
        "name": "Copa de la División Profesional",
        "country": "Bolivia",
        "type": "cup",
    },
    # ============================================================
    # BOSNIA
    # ============================================================
    {
        "id": 315,
        "name": "Premijer Liga",
        "country": "Bosnia",
        "type": "league",
    },
    {
        "id": 314,
        "name": "Cup",
        "country": "Bosnia",
        "type": "cup",
    },
    {
        "id": 1221,
        "name": "Super Cup",
        "country": "Bosnia",
        "type": "cup",
    },
    # ============================================================
    # BRAZIL (Additional)
    # ============================================================
    {
        "id": 76,
        "name": "Serie D",
        "country": "Brazil",
        "type": "league",
    },
    {
        "id": 632,
        "name": "Supercopa do Brasil",
        "country": "Brazil",
        "type": "cup",
    },
    # ============================================================
    # BULGARIA
    # ============================================================
    {
        "id": 172,
        "name": "First League",
        "country": "Bulgaria",
        "type": "league",
    },
    {
        "id": 173,
        "name": "Second League",
        "country": "Bulgaria",
        "type": "league",
    },
    {
        "id": 174,
        "name": "Cup",
        "country": "Bulgaria",
        "type": "cup",
    },
    {
        "id": 656,
        "name": "Super Cup",
        "country": "Bulgaria",
        "type": "cup",
    },
    # ============================================================
    # CANADA
    # ============================================================
    {
        "id": 479,
        "name": "Canadian Premier League",
        "country": "Canada",
        "type": "league",
    },
    {
        "id": 259,
        "name": "Canadian Championship",
        "country": "Canada",
        "type": "cup",
    },
    # ============================================================
    # CHILE (Additional)
    # ============================================================
    {
        "id": 711,
        "name": "Segunda División",
        "country": "Chile",
        "type": "league",
    },
    {
        "id": 266,
        "name": "Primera B",
        "country": "Chile",
        "type": "league",
    },
    {
        "id": 1220,
        "name": "Copa De La Liga",
        "country": "Chile",
        "type": "cup",
    },
    {
        "id": 267,
        "name": "Copa Chile",
        "country": "Chile",
        "type": "cup",
    },
    {
        "id": 527,
        "name": "Super Cup",
        "country": "Chile",
        "type": "cup",
    },
    # ============================================================
    # CHINA (Additional)
    # ============================================================
    {
        "id": 929,
        "name": "League Two",
        "country": "China",
        "type": "league",
    },
    {
        "id": 171,
        "name": "FA Cup",
        "country": "China",
        "type": "cup",
    },
    {
        "id": 972,
        "name": "Super Cup",
        "country": "China",
        "type": "cup",
    },
    # ============================================================
    # COLOMBIA
    # ============================================================
    {
        "id": 713,
        "name": "Superliga",
        "country": "Colombia",
        "type": "cup",
    },
    {
        "id": 239,
        "name": "Primera A",
        "country": "Colombia",
        "type": "league",
    },
    {
        "id": 240,
        "name": "Primera B",
        "country": "Colombia",
        "type": "league",
    },
    {
        "id": 241,
        "name": "Copa Colombia",
        "country": "Colombia",
        "type": "cup",
    },
    # ============================================================
    # COSTA RICA
    # ============================================================
    {
        "id": 162,
        "name": "Primera División",
        "country": "Costa Rica",
        "type": "league",
    },
    {
        "id": 958,
        "name": "Copa Costa Rica",
        "country": "Costa Rica",
        "type": "cup",
    },
    {
        "id": 864,
        "name": "Supercopa",
        "country": "Costa Rica",
        "type": "cup",
    },
    # ============================================================
    # CROATIA
    # ============================================================
    {
        "id": 210,
        "name": "HNL",
        "country": "Croatia",
        "type": "league",
    },
    {
        "id": 211,
        "name": "First NL",
        "country": "Croatia",
        "type": "league",
    },
    {
        "id": 212,
        "name": "Cup",
        "country": "Croatia",
        "type": "cup",
    },
    {
        "id": 1021,
        "name": "Super Cup",
        "country": "Croatia",
        "type": "cup",
    },
    # ============================================================
    # CYPRUS
    # ============================================================
    {
        "id": 318,
        "name": "1. Division",
        "country": "Cyprus",
        "type": "league",
    },
    {
        "id": 319,
        "name": "2. Division",
        "country": "Cyprus",
        "type": "league",
    },
    {
        "id": 321,
        "name": "Cup",
        "country": "Cyprus",
        "type": "cup",
    },
    {
        "id": 852,
        "name": "Super Cup",
        "country": "Cyprus",
        "type": "cup",
    },
    # ============================================================
    # CZECH REPUBLIC
    # ============================================================
    {
        "id": 345,
        "name": "Czech Liga",
        "country": "Czech Republic",
        "type": "league",
    },
    {
        "id": 346,
        "name": "FNL",
        "country": "Czech Republic",
        "type": "league",
    },
    {
        "id": 347,
        "name": "Cup",
        "country": "Czech Republic",
        "type": "cup",
    },
    {
        "id": 925,
        "name": "Super Cup",
        "country": "Czech Republic",
        "type": "cup",
    },
    # ============================================================
    # ECUADOR
    # ============================================================
    {
        "id": 242,
        "name": "Liga Pro",
        "country": "Ecuador",
        "type": "league",
    },
    {
        "id": 243,
        "name": "Liga Pro Serie B",
        "country": "Ecuador",
        "type": "league",
    },
    {
        "id": 917,
        "name": "Copa Ecuador",
        "country": "Ecuador",
        "type": "cup",
    },
    # ============================================================
    # EGYPT
    # ============================================================
    {
        "id": 233,
        "name": "Premier League",
        "country": "Egypt",
        "type": "league",
    },
    {
        "id": 887,
        "name": "Second League",
        "country": "Egypt",
        "type": "league",
    },
    {
        "id": 895,
        "name": "League Cup",
        "country": "Egypt",
        "type": "cup",
    },
    {
        "id": 714,
        "name": "Cup",
        "country": "Egypt",
        "type": "cup",
    },
    # ============================================================
    # ENGLAND (Additional)
    # ============================================================
    {
        "id": 50,
        "name": "National League - North",
        "country": "England",
        "type": "league",
    },
    {
        "id": 51,
        "name": "National League - South",
        "country": "England",
        "type": "league",
    },
    {
        "id": 699,
        "name": "Women's Championship",
        "country": "England",
        "type": "league",
    },
    {
        "id": 697,
        "name": "WSL Cup",
        "country": "England",
        "type": "cup",
    },
    {
        "id": 44,
        "name": "FA WSL",
        "country": "England",
        "type": "league",
    },
    {
        "id": 1156,
        "name": "National League Cup",
        "country": "England",
        "type": "cup",
    },
    {
        "id": 670,
        "name": "Community Shield Women",
        "country": "England",
        "type": "cup",
    },
    # ============================================================
    # ESTONIA
    # ============================================================
    {
        "id": 329,
        "name": "Meistriliiga",
        "country": "Estonia",
        "type": "league",
    },
    {
        "id": 328,
        "name": "Esiliiga A",
        "country": "Estonia",
        "type": "league",
    },
    {
        "id": 657,
        "name": "Cup",
        "country": "Estonia",
        "type": "cup",
    },
    # ============================================================
    # FINLAND
    # ============================================================
    {
        "id": 244,
        "name": "Veikkausliiga",
        "country": "Finland",
        "type": "league",
    },
    {
        "id": 1087,
        "name": "Ykkösliiga",
        "country": "Finland",
        "type": "league",
    },
    {
        "id": 246,
        "name": "Suomen Cup",
        "country": "Finland",
        "type": "cup",
    },
    {
        "id": 899,
        "name": "League Cup",
        "country": "Finland",
        "type": "cup",
    },
    # ============================================================
    # FRANCE (Additional)
    # ============================================================
    {
        "id": 64,
        "name": "Feminine Division 1",
        "country": "France",
        "type": "league",
    },
    {
        "id": 63,
        "name": "National 1",
        "country": "France",
        "type": "league",
    },
    # ============================================================
    # GEORGIA
    # ============================================================
    {
        "id": 327,
        "name": "Erovnuli Liga",
        "country": "Georgia",
        "type": "league",
    },
    {
        "id": 326,
        "name": "Erovnuli Liga 2",
        "country": "Georgia",
        "type": "league",
    },
    {
        "id": 672,
        "name": "David Kipiani Cup",
        "country": "Georgia",
        "type": "cup",
    },
    {
        "id": 530,
        "name": "Super Cup",
        "country": "Georgia",
        "type": "cup",
    },
    # ============================================================
    # GERMANY (Additional)
    # ============================================================
    {
        "id": 82,
        "name": "Frauen Bundesliga",
        "country": "Germany",
        "type": "league",
    },
    {
        "id": 947,
        "name": "DFB Pokal - Women",
        "country": "Germany",
        "type": "cup",
    },
    # ============================================================
    # GREECE (Additional)
    # ============================================================
    {
        "id": 494,
        "name": "Super League 2",
        "country": "Greece",
        "type": "league",
    },
    {
        "id": 1210,
        "name": "Super Cup",
        "country": "Greece",
        "type": "cup",
    },
    {
        "id": 199,
        "name": "Cup",
        "country": "Greece",
        "type": "cup",
    },
    # ============================================================
    # HONDURAS
    # ============================================================
    {
        "id": 234,
        "name": "Liga Nacional",
        "country": "Honduras",
        "type": "league",
    },
    # ============================================================
    # HUNGARY
    # ============================================================
    {
        "id": 271,
        "name": "NB I",
        "country": "Hungary",
        "type": "league",
    },
    {
        "id": 272,
        "name": "NB II",
        "country": "Hungary",
        "type": "league",
    },
    {
        "id": 273,
        "name": "Magyar Kupa",
        "country": "Hungary",
        "type": "cup",
    },
    # ============================================================
    # ICELAND
    # ============================================================
    {
        "id": 165,
        "name": "1. Deild",
        "country": "Iceland",
        "type": "league",
    },
    {
        "id": 166,
        "name": "2. Deild",
        "country": "Iceland",
        "type": "league",
    },
    {
        "id": 167,
        "name": "Cup",
        "country": "Iceland",
        "type": "cup",
    },
    {
        "id": 168,
        "name": "League Cup",
        "country": "Iceland",
        "type": "cup",
    },
    {
        "id": 639,
        "name": "Super Cup",
        "country": "Iceland",
        "type": "cup",
    },
    # ============================================================
    # INDONESIA
    # ============================================================
    {
        "id": 274,
        "name": "Liga 1",
        "country": "Indonesia",
        "type": "league",
    },
    {
        "id": 275,
        "name": "Liga 2",
        "country": "Indonesia",
        "type": "league",
    },
    # ============================================================
    # IRAN
    # ============================================================
    {
        "id": 290,
        "name": "Persian Gulf Pro League",
        "country": "Iran",
        "type": "league",
    },
    {
        "id": 291,
        "name": "Azadegan League",
        "country": "Iran",
        "type": "league",
    },
    {
        "id": 495,
        "name": "Hazfi Cup",
        "country": "Iran",
        "type": "cup",
    },
    {
        "id": 905,
        "name": "Super Cup",
        "country": "Iran",
        "type": "cup",
    },
    # ============================================================
    # IRELAND
    # ============================================================
    {
        "id": 357,
        "name": "Premier Division",
        "country": "Ireland",
        "type": "league",
    },
    {
        "id": 358,
        "name": "First Division",
        "country": "Ireland",
        "type": "league",
    },
    {
        "id": 360,
        "name": "League Cup",
        "country": "Ireland",
        "type": "cup",
    },
    {
        "id": 546,
        "name": "FAI President's Cup",
        "country": "Ireland",
        "type": "cup",
    },
    {
        "id": 359,
        "name": "FAI Cup",
        "country": "Ireland",
        "type": "cup",
    },
    # ============================================================
    # ISRAEL
    # ============================================================
    {
        "id": 383,
        "name": "Ligat Ha'al",
        "country": "Israel",
        "type": "league",
    },
    {
        "id": 382,
        "name": "Liga Leumit",
        "country": "Israel",
        "type": "league",
    },
    {
        "id": 384,
        "name": "State Cup",
        "country": "Israel",
        "type": "cup",
    },
    {
        "id": 659,
        "name": "Super Cup",
        "country": "Israel",
        "type": "cup",
    },
    # ============================================================
    # ITALY (Additional)
    # ============================================================
    {
        "id": 139,
        "name": "Serie A Women",
        "country": "Italy",
        "type": "league",
    },
    {
        "id": 1198,
        "name": "Serie A Cup Women",
        "country": "Italy",
        "type": "cup",
    },
    {
        "id": 1171,
        "name": "Coppa Italia Women",
        "country": "Italy",
        "type": "cup",
    },
    # ============================================================
    # JAPAN (Additional)
    # ============================================================
    {
        "id": 548,
        "name": "Super Cup",
        "country": "Japan",
        "type": "cup",
    },
    # ============================================================
    # KAZAKHSTAN
    # ============================================================
    {
        "id": 389,
        "name": "Premier League",
        "country": "Kazakhstan",
        "type": "league",
    },
    {
        "id": 388,
        "name": "1. Division",
        "country": "Kazakhstan",
        "type": "league",
    },
    {
        "id": 498,
        "name": "Cup",
        "country": "Kazakhstan",
        "type": "cup",
    },
    {
        "id": 818,
        "name": "Super Cup",
        "country": "Kazakhstan",
        "type": "cup",
    },
    # ============================================================
    # KUWAIT
    # ============================================================
    {
        "id": 330,
        "name": "Premier League",
        "country": "Kuwait",
        "type": "league",
    },
    {
        "id": 820,
        "name": "Crown Prince Cup",
        "country": "Kuwait",
        "type": "cup",
    },
    {
        "id": 720,
        "name": "Emir Cup",
        "country": "Kuwait",
        "type": "cup",
    },
    {
        "id": 719,
        "name": "Super Cup",
        "country": "Kuwait",
        "type": "cup",
    },
    # ============================================================
    # LITHUANIA
    # ============================================================
    {
        "id": 362,
        "name": "A Lyga",
        "country": "Lithuania",
        "type": "league",
    },
    {
        "id": 361,
        "name": "1 Lyga",
        "country": "Lithuania",
        "type": "league",
    },
    {
        "id": 661,
        "name": "Cup",
        "country": "Lithuania",
        "type": "cup",
    },
    {
        "id": 839,
        "name": "Super Cup",
        "country": "Lithuania",
        "type": "cup",
    },
    # ============================================================
    # MALAYSIA
    # ============================================================
    {
        "id": 278,
        "name": "Super League",
        "country": "Malaysia",
        "type": "league",
    },
    {
        "id": 279,
        "name": "Premier League",
        "country": "Malaysia",
        "type": "league",
    },
    {
        "id": 499,
        "name": "Malaysia Cup",
        "country": "Malaysia",
        "type": "cup",
    },
    {
        "id": 500,
        "name": "FA Cup",
        "country": "Malaysia",
        "type": "cup",
    },
    # ============================================================
    # MEXICO (Additional)
    # ============================================================
    {
        "id": 662,
        "name": "Copa por México",
        "country": "Mexico",
        "type": "cup",
    },
    {
        "id": 857,
        "name": "Campeón de Campeones",
        "country": "Mexico",
        "type": "cup",
    },
    # ============================================================
    # MOLDOVA
    # ============================================================
    {
        "id": 394,
        "name": "Super Liga",
        "country": "Moldova",
        "type": "league",
    },
    {
        "id": 674,
        "name": "Cupa",
        "country": "Moldova",
        "type": "cup",
    },
    # ============================================================
    # MOROCCO
    # ============================================================
    {
        "id": 200,
        "name": "Botola Pro",
        "country": "Morocco",
        "type": "league",
    },
    {
        "id": 201,
        "name": "Botola 2",
        "country": "Morocco",
        "type": "league",
    },
    {
        "id": 822,
        "name": "Cup",
        "country": "Morocco",
        "type": "cup",
    },
    # ============================================================
    # NETHERLANDS (Additional)
    # ============================================================
    {
        "id": 1190,
        "name": "Super Cup Women",
        "country": "Netherlands",
        "type": "cup",
    },
    # ============================================================
    # NORTHERN IRELAND
    # ============================================================
    {
        "id": 408,
        "name": "Premiership",
        "country": "Northern Ireland",
        "type": "league",
    },
    {
        "id": 407,
        "name": "Championship",
        "country": "Northern Ireland",
        "type": "league",
    },
    {
        "id": 757,
        "name": "Irish Cup",
        "country": "Northern Ireland",
        "type": "cup",
    },
    {
        "id": 559,
        "name": "League Cup",
        "country": "Northern Ireland",
        "type": "cup",
    },
    # ============================================================
    # NORWAY (Additional)
    # ============================================================
    {
        "id": 557,
        "name": "Super Cup",
        "country": "Norway",
        "type": "cup",
    },
    # ============================================================
    # PARAGUAY
    # ============================================================
    {
        "id": 252,
        "name": "Division Profesional - Clausura",
        "country": "Paraguay",
        "type": "league",
    },
    {
        "id": 250,
        "name": "Division Profesional - Apertura",
        "country": "Paraguay",
        "type": "league",
    },
    {
        "id": 501,
        "name": "Copa Paraguay",
        "country": "Paraguay",
        "type": "cup",
    },
    {
        "id": 961,
        "name": "Supercopa",
        "country": "Paraguay",
        "type": "cup",
    },
    # ============================================================
    # PERU
    # ============================================================
    {
        "id": 281,
        "name": "Primera División",
        "country": "Peru",
        "type": "league",
    },
    {
        "id": 282,
        "name": "Segunda División",
        "country": "Peru",
        "type": "league",
    },
    {
        "id": 558,
        "name": "Supercopa",
        "country": "Peru",
        "type": "cup",
    },
    {
        "id": 1232,
        "name": "Copa De La Liga",
        "country": "Peru",
        "type": "cup",
    },
    {
        "id": 503,
        "name": "Copa Perú",
        "country": "Peru",
        "type": "cup",
    },
    # ============================================================
    # POLAND (Additional)
    # ============================================================
    {
        "id": 727,
        "name": "Super Cup",
        "country": "Poland",
        "type": "cup",
    },
    # ============================================================
    # QATAR
    # ============================================================
    {
        "id": 305,
        "name": "Stars League",
        "country": "Qatar",
        "type": "league",
    },
    {
        "id": 306,
        "name": "Second Division",
        "country": "Qatar",
        "type": "league",
    },
    {
        "id": 825,
        "name": "Qatar Cup",
        "country": "Qatar",
        "type": "cup",
    },
    {
        "id": 677,
        "name": "QSL Cup",
        "country": "Qatar",
        "type": "cup",
    },
    {
        "id": 824,
        "name": "Emir Cup",
        "country": "Qatar",
        "type": "cup",
    },
    {
        "id": 841,
        "name": "QFA Cup",
        "country": "Qatar",
        "type": "cup",
    },
    # ============================================================
    # ROMANIA
    # ============================================================
    {
        "id": 283,
        "name": "Liga I",
        "country": "Romania",
        "type": "league",
    },
    {
        "id": 284,
        "name": "Liga II",
        "country": "Romania",
        "type": "league",
    },
    {
        "id": 285,
        "name": "Cupa României",
        "country": "Romania",
        "type": "cup",
    },
    {
        "id": 555,
        "name": "Supercupa",
        "country": "Romania",
        "type": "cup",
    },
    # ============================================================
    # RUSSIA (Additional)
    # ============================================================
    {
        "id": 663,
        "name": "Super Cup",
        "country": "Russia",
        "type": "cup",
    },
    # ============================================================
    # SAUDI ARABIA
    # ============================================================
    {
        "id": 307,
        "name": "Pro League",
        "country": "Saudi Arabia",
        "type": "league",
    },
    {
        "id": 308,
        "name": "Division 1",
        "country": "Saudi Arabia",
        "type": "league",
    },
    {
        "id": 827,
        "name": "Crown Prince Cup",
        "country": "Saudi Arabia",
        "type": "cup",
    },
    {
        "id": 826,
        "name": "Super Cup",
        "country": "Saudi Arabia",
        "type": "cup",
    },
    {
        "id": 504,
        "name": "King's Cup",
        "country": "Saudi Arabia",
        "type": "cup",
    },
    # ============================================================
    # SCOTLAND (Additional)
    # ============================================================
    {
        "id": 182,
        "name": "Challenge Cup",
        "country": "Scotland",
        "type": "cup",
    },
    # ============================================================
    # SERBIA
    # ============================================================
    {
        "id": 286,
        "name": "Super Liga",
        "country": "Serbia",
        "type": "league",
    },
    {
        "id": 287,
        "name": "Prva Liga",
        "country": "Serbia",
        "type": "league",
    },
    {
        "id": 732,
        "name": "Cup",
        "country": "Serbia",
        "type": "cup",
    },
    # ============================================================
    # SLOVAKIA
    # ============================================================
    {
        "id": 332,
        "name": "Super Liga",
        "country": "Slovakia",
        "type": "league",
    },
    {
        "id": 506,
        "name": "2. liga",
        "country": "Slovakia",
        "type": "league",
    },
    {
        "id": 680,
        "name": "Cup",
        "country": "Slovakia",
        "type": "cup",
    },
    # ============================================================
    # SLOVENIA
    # ============================================================
    {
        "id": 373,
        "name": "1. SNL",
        "country": "Slovenia",
        "type": "league",
    },
    {
        "id": 374,
        "name": "2. SNL",
        "country": "Slovenia",
        "type": "league",
    },
    {
        "id": 375,
        "name": "Cup",
        "country": "Slovenia",
        "type": "cup",
    },
    # ============================================================
    # SOUTH AFRICA
    # ============================================================
    {
        "id": 288,
        "name": "Premier Soccer League",
        "country": "South Africa",
        "type": "league",
    },
    {
        "id": 508,
        "name": "League Cup",
        "country": "South Africa",
        "type": "cup",
    },
    {
        "id": 509,
        "name": "8 Cup",
        "country": "South Africa",
        "type": "cup",
    },
    # ============================================================
    # SOUTH KOREA
    # ============================================================
    {
        "id": 292,
        "name": "K League 1",
        "country": "South Korea",
        "type": "league",
    },
    {
        "id": 293,
        "name": "K League 2",
        "country": "South Korea",
        "type": "league",
    },
    {
        "id": 294,
        "name": "FA Cup",
        "country": "South Korea",
        "type": "cup",
    },
    # ============================================================
    # SPAIN (Additional)
    # ============================================================
    {
        "id": 1058,
        "name": "Supercopa Femenina",
        "country": "Spain",
        "type": "cup",
    },
    # ============================================================
    # THAILAND
    # ============================================================
    {
        "id": 296,
        "name": "Thai League 1",
        "country": "Thailand",
        "type": "league",
    },
    {
        "id": 298,
        "name": "FA Cup",
        "country": "Thailand",
        "type": "cup",
    },
    {
        "id": 898,
        "name": "League Cup",
        "country": "Thailand",
        "type": "cup",
    },
    # ============================================================
    # TUNISIA
    # ============================================================
    {
        "id": 202,
        "name": "Ligue 1",
        "country": "Tunisia",
        "type": "league",
    },
    {
        "id": 828,
        "name": "Ligue 2",
        "country": "Tunisia",
        "type": "league",
    },
    {
        "id": 1194,
        "name": "Super Cup",
        "country": "Tunisia",
        "type": "cup",
    },
    {
        "id": 511,
        "name": "Cup",
        "country": "Tunisia",
        "type": "cup",
    },
    # ============================================================
    # TURKEY (Additional)
    # ============================================================
    {
        "id": 206,
        "name": "Türkiye Kupası",
        "country": "Turkey",
        "type": "cup",
    },
    # ============================================================
    # UKRAINE (Additional)
    # ============================================================
    {
        "id": 678,
        "name": "Super Cup",
        "country": "Ukraine",
        "type": "cup",
    },
    # ============================================================
    # UNITED ARAB EMIRATES
    # ============================================================
    {
        "id": 301,
        "name": "Pro League",
        "country": "United Arab Emirates",
        "type": "league",
    },
    {
        "id": 302,
        "name": "League Cup",
        "country": "United Arab Emirates",
        "type": "cup",
    },
    {
        "id": 896,
        "name": "Super Cup",
        "country": "United Arab Emirates",
        "type": "cup",
    },
    # ============================================================
    # URUGUAY (Additional)
    # ============================================================
    {
        "id": 270,
        "name": "Primera División - Clausura",
        "country": "Uruguay",
        "type": "league",
    },
    {
        "id": 269,
        "name": "Segunda División",
        "country": "Uruguay",
        "type": "league",
    },
    {
        "id": 930,
        "name": "Copa Uruguay",
        "country": "Uruguay",
        "type": "cup",
    },
    {
        "id": 842,
        "name": "Super Copa",
        "country": "Uruguay",
        "type": "cup",
    },
    {
        "id": 268,
        "name": "Primera División - Apertura",
        "country": "Uruguay",
        "type": "league",
    },
    # ============================================================
    # VENEZUELA
    # ============================================================
    {
        "id": 299,
        "name": "Primera División",
        "country": "Venezuela",
        "type": "league",
    },
    {
        "id": 300,
        "name": "Segunda División",
        "country": "Venezuela",
        "type": "league",
    },
    {
        "id": 1113,
        "name": "Copa Venezuela",
        "country": "Venezuela",
        "type": "cup",
    },
    {
        "id": 1181,
        "name": "Supercopa",
        "country": "Venezuela",
        "type": "cup",
    },
    # ============================================================
    # WALES
    # ============================================================
    {
        "id": 110,
        "name": "Premier League",
        "country": "Wales",
        "type": "league",
    },
    {
        "id": 738,
        "name": "League Cup",
        "country": "Wales",
        "type": "cup",
    },
    {
        "id": 112,
        "name": "Welsh Cup",
        "country": "Wales",
        "type": "cup",
    },
    # ============================================================
    # WORLD (Additional International)
    # ============================================================
    {
        "id": 807,
        "name": "AFC Challenge Cup",
        "country": "World",
        "type": "cup",
    },
    {
        "id": 1132,
        "name": "AFC Challenge League",
        "country": "World",
        "type": "cup",
    },
    {
        "id": 17,
        "name": "AFC Champions League Elite",
        "country": "World",
        "type": "cup",
    },
    {
        "id": 18,
        "name": "AFC Champions League Two",
        "country": "World",
        "type": "cup",
    },
    {
        "id": 36,
        "name": "Africa Cup of Nations - Qualification",
        "country": "World",
        "type": "cup",
    },
    {
        "id": 922,
        "name": "Africa Cup of Nations - Women",
        "country": "World",
        "type": "cup",
    },
    {
        "id": 768,
        "name": "Arab Club Champions Cup",
        "country": "World",
        "type": "cup",
    },
    {
        "id": 860,
        "name": "Arab Cup",
        "country": "World",
        "type": "cup",
    },
    {
        "id": 35,
        "name": "Asian Cup - Qualification",
        "country": "World",
        "type": "cup",
    },
    {
        "id": 897,
        "name": "Asian Cup Women",
        "country": "World",
        "type": "cup",
    },
    {
        "id": 894,
        "name": "Asian Cup Women - Qualification",
        "country": "World",
        "type": "cup",
    },
    {
        "id": 12,
        "name": "CAF Champions League",
        "country": "World",
        "type": "cup",
    },
    {
        "id": 20,
        "name": "CAF Confederation Cup",
        "country": "World",
        "type": "cup",
    },
    {
        "id": 533,
        "name": "CAF Super Cup",
        "country": "World",
        "type": "cup",
    },
    {
        "id": 1164,
        "name": "CAF Women's Champions League",
        "country": "World",
        "type": "cup",
    },
    {
        "id": 16,
        "name": "CONCACAF Champions League",
        "country": "World",
        "type": "cup",
    },
    {
        "id": 22,
        "name": "CONCACAF Gold Cup",
        "country": "World",
        "type": "cup",
    },
    {
        "id": 858,
        "name": "CONCACAF Gold Cup - Qualification",
        "country": "World",
        "type": "cup",
    },
    {
        "id": 1046,
        "name": "CONCACAF Gold Cup - Qualification - Women",
        "country": "World",
        "type": "cup",
    },
    {
        "id": 1057,
        "name": "CONCACAF Gold Cup - Women",
        "country": "World",
        "type": "cup",
    },
    {
        "id": 767,
        "name": "CONCACAF League",
        "country": "World",
        "type": "cup",
    },
    {
        "id": 536,
        "name": "CONCACAF Nations League",
        "country": "World",
        "type": "cup",
    },
    {
        "id": 808,
        "name": "CONCACAF Nations League - Qualification",
        "country": "World",
        "type": "cup",
    },
    {
        "id": 13,
        "name": "CONMEBOL Libertadores",
        "country": "World",
        "type": "cup",
    },
    {
        "id": 11,
        "name": "CONMEBOL Sudamericana",
        "country": "World",
        "type": "cup",
    },
    {
        "id": 21,
        "name": "Confederations Cup",
        "country": "World",
        "type": "cup",
    },
    {
        "id": 937,
        "name": "Emirates Cup",
        "country": "World",
        "type": "cup",
    },
    {
        "id": 960,
        "name": "Euro Championship - Qualification",
        "country": "World",
        "type": "cup",
    },
    {
        "id": 1186,
        "name": "FIFA Club World Cup - Play-In",
        "country": "World",
        "type": "cup",
    },
    {
        "id": 1168,
        "name": "FIFA Intercontinental Cup",
        "country": "World",
        "type": "cup",
    },
    {
        "id": 667,
        "name": "Friendlies Clubs",
        "country": "World",
        "type": "cup",
    },
    {
        "id": 26,
        "name": "International Champions Cup",
        "country": "World",
        "type": "cup",
    },
    {
        "id": 945,
        "name": "International Champions Cup - Women",
        "country": "World",
        "type": "cup",
    },
    {
        "id": 525,
        "name": "UEFA Champions League Women",
        "country": "World",
        "type": "cup",
    },
    {
        "id": 743,
        "name": "UEFA Championship - Women",
        "country": "World",
        "type": "cup",
    },
    {
        "id": 1083,
        "name": "UEFA Championship - Women - Qualification",
        "country": "World",
        "type": "cup",
    },
    {
        "id": 1191,
        "name": "UEFA Europa Cup - Women",
        "country": "World",
        "type": "cup",
    },
    {
        "id": 1040,
        "name": "UEFA Nations League - Women",
        "country": "World",
        "type": "cup",
    },
    {
        "id": 14,
        "name": "UEFA Youth League",
        "country": "World",
        "type": "league",
    },
    {
        "id": 29,
        "name": "World Cup - Qualification Africa",
        "country": "World",
        "type": "cup",
    },
    {
        "id": 30,
        "name": "World Cup - Qualification Asia",
        "country": "World",
        "type": "cup",
    },
    {
        "id": 31,
        "name": "World Cup - Qualification CONCACAF",
        "country": "World",
        "type": "cup",
    },
    {
        "id": 33,
        "name": "World Cup - Qualification Oceania",
        "country": "World",
        "type": "cup",
    },
    {
        "id": 587,
        "name": "World Cup - U17",
        "country": "World",
        "type": "cup",
    },
    {
        "id": 950,
        "name": "World Cup - U17 - Women",
        "country": "World",
        "type": "cup",
    },
    {
        "id": 490,
        "name": "World Cup - U20",
        "country": "World",
        "type": "cup",
    },
    {
        "id": 920,
        "name": "World Cup - U20 - Women",
        "country": "World",
        "type": "cup",
    },
    {
        "id": 8,
        "name": "World Cup - Women",
        "country": "World",
        "type": "cup",
    },
    {
        "id": 927,
        "name": "World Cup - Women - Qualification Concacaf",
        "country": "World",
        "type": "cup",
    },
    {
        "id": 880,
        "name": "World Cup - Women - Qualification Europe",
        "country": "World",
        "type": "cup",
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

    # Check for exact alias match first (alias found IN query)
    for league in LEAGUE_REFERENCE:
        aliases = league.get("aliases", [])
        # Check if any alias appears in the query (not vice versa)
        if any(a.lower() in query_lower for a in aliases):
            return [league]

    # Check for name match (league name found IN query)
    for league in LEAGUE_REFERENCE:
        if league["name"].lower() in query_lower:
            return [league]

    # Check for partial name match (league name found IN query)
    matches = []
    for league in LEAGUE_REFERENCE:
        if league["name"].lower() in query_lower:
            matches.append(league)

    if matches:
        return matches

    # Check for country name IN query (e.g., "Azerbaijan Today" contains "azerbaijan")
    # Check both _LEAGUES_BY_COUNTRY keys and _COUNTRY_VARIANTS keys
    for country in _LEAGUES_BY_COUNTRY.keys():
        if country in query_lower:
            return _LEAGUES_BY_COUNTRY[country]

    # Check country variants (e.g., "usa", "holland", "uk")
    for variant, normalized in _COUNTRY_VARIANTS.items():
        if variant in query_lower:
            return _LEAGUES_BY_COUNTRY.get(normalized, [])

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

