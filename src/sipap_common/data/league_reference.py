"""League Reference with API-Football IDs.

This module provides a comprehensive reference of football leagues with their
API-Football IDs for unambiguous entity resolution.

The ID-first approach eliminates string matching brittleness:
- "La Liga" → ID 140 (always Spain)
- "Premier League" + "England" → ID 39
- "Premier League" + "Belarus" → ID 117

Coverage: 380 competitions across 77 countries + international tournaments.

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
# Coverage: 380 competitions across 77 countries + international
# Format: id, name, country, type, tier, aliases
LEAGUE_REFERENCE: list[dict[str, Any]] = [
    # ============================================================
    # ENGLAND (17 competitions)
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
        "tier": 2,
        "aliases": ["EFL Championship", "English Championship", "English second division"],
    },
    {
        "id": 41,
        "name": "League One",
        "country": "England",
        "type": "league",
        "tier": 3,
        "aliases": ["EFL League One", "English League One", "English third division"],
    },
    {
        "id": 42,
        "name": "League Two",
        "country": "England",
        "type": "league",
        "tier": 4,
        "aliases": ["EFL League Two", "English League Two", "English fourth division"],
    },
    {
        "id": 43,
        "name": "National League",
        "country": "England",
        "type": "league",
        "tier": 5,
        "aliases": ["English National League", "Conference National"],
    },
    {
        "id": 44,
        "name": "National League - North",
        "country": "England",
        "type": "league",
        "tier": 6,
        "aliases": ["National League North"],
    },
    {
        "id": 839,
        "name": "National League - South",
        "country": "England",
        "type": "league",
        "tier": 6,
        "aliases": ["National League South"],
    },
    {
        "id": 45,
        "name": "FA Cup",
        "country": "England",
        "type": "cup",
        "tier": 1,
        "aliases": ["English FA Cup", "The FA Cup", "Emirates FA Cup"],
    },
    {
        "id": 48,
        "name": "League Cup",
        "country": "England",
        "type": "cup",
        "tier": 2,
        "aliases": ["EFL Cup", "Carabao Cup", "English League Cup"],
    },
    {
        "id": 46,
        "name": "EFL Trophy",
        "country": "England",
        "type": "cup",
        "tier": 3,
        "aliases": ["Football League Trophy", "Papa John's Trophy"],
    },
    {
        "id": 47,
        "name": "FA Trophy",
        "country": "England",
        "type": "cup",
        "tier": 4,
        "aliases": ["English FA Trophy"],
    },
    {
        "id": 528,
        "name": "Community Shield",
        "country": "England",
        "type": "cup",
        "tier": 1,
        "aliases": ["FA Community Shield", "Charity Shield"],
    },
    {
        "id": 699,
        "name": "National League Cup",
        "country": "England",
        "type": "cup",
        "tier": 5,
        "aliases": ["Conference League Cup"],
    },
    {
        "id": 708,
        "name": "FA WSL",
        "country": "England",
        "type": "league",
        "tier": 1,
        "aliases": ["Women's Super League", "WSL", "English Women's Super League"],
    },
    {
        "id": 709,
        "name": "Women's Championship",
        "country": "England",
        "type": "league",
        "tier": 2,
        "aliases": ["English Women's Championship", "FA Women's Championship"],
    },
    {
        "id": 712,
        "name": "WSL Cup",
        "country": "England",
        "type": "cup",
        "tier": 1,
        "aliases": ["FA Women's League Cup", "Women's League Cup"],
    },
    {
        "id": 713,
        "name": "Community Shield Women",
        "country": "England",
        "type": "cup",
        "tier": 1,
        "aliases": ["FA Women's Community Shield"],
    },

    # ============================================================
    # SPAIN (6 competitions)
    # ============================================================
    {
        "id": 140,
        "name": "La Liga",
        "country": "Spain",
        "type": "league",
        "tier": 1,
        "aliases": ["LaLiga", "Spanish LaLiga", "Spanish La Liga", "La Liga Santander", "LaLiga EA Sports", "Primera División"],
        "default_for_ambiguous": True,
    },
    {
        "id": 141,
        "name": "Segunda División",
        "country": "Spain",
        "type": "league",
        "tier": 2,
        "aliases": ["La Liga 2", "Spanish second division", "Segunda", "LaLiga 2"],
    },
    {
        "id": 143,
        "name": "Copa del Rey",
        "country": "Spain",
        "type": "cup",
        "tier": 1,
        "aliases": ["Spanish Cup", "King's Cup", "Copa Rey"],
    },
    {
        "id": 556,
        "name": "Super Cup",
        "country": "Spain",
        "type": "cup",
        "tier": 1,
        "aliases": ["Supercopa de España", "Spanish Super Cup"],
    },
    {
        "id": 142,
        "name": "Primera División Femenina",
        "country": "Spain",
        "type": "league",
        "tier": 1,
        "aliases": ["Liga F", "Spanish Women's League", "Primera Femenina"],
    },
    {
        "id": 891,
        "name": "Supercopa Femenina",
        "country": "Spain",
        "type": "cup",
        "tier": 1,
        "aliases": ["Spanish Women's Super Cup"],
    },

    # ============================================================
    # ITALY (9 competitions)
    # ============================================================
    {
        "id": 135,
        "name": "Serie A",
        "country": "Italy",
        "type": "league",
        "tier": 1,
        "aliases": ["Italian Serie A", "Serie A TIM", "Italy Serie A"],
        "default_for_ambiguous": True,
    },
    {
        "id": 136,
        "name": "Serie B",
        "country": "Italy",
        "type": "league",
        "tier": 2,
        "aliases": ["Italian Serie B", "Italy Serie B", "Italian second division"],
    },
    {
        "id": 138,
        "name": "Serie C - Girone A",
        "country": "Italy",
        "type": "league",
        "tier": 3,
        "aliases": ["Serie C Group A", "Italian third division A"],
    },
    {
        "id": 139,
        "name": "Serie C - Girone B",
        "country": "Italy",
        "type": "league",
        "tier": 3,
        "aliases": ["Serie C Group B", "Italian third division B"],
    },
    {
        "id": 140,
        "name": "Serie C - Girone C",
        "country": "Italy",
        "type": "league",
        "tier": 3,
        "aliases": ["Serie C Group C", "Italian third division C"],
    },
    {
        "id": 137,
        "name": "Coppa Italia",
        "country": "Italy",
        "type": "cup",
        "tier": 1,
        "aliases": ["Italian Cup", "Italy Cup"],
    },
    {
        "id": 547,
        "name": "Super Cup",
        "country": "Italy",
        "type": "cup",
        "tier": 1,
        "aliases": ["Supercoppa Italiana", "Italian Super Cup"],
    },
    {
        "id": 706,
        "name": "Serie A Women",
        "country": "Italy",
        "type": "league",
        "tier": 1,
        "aliases": ["Italian Women's Serie A", "Serie A Femminile"],
    },
    {
        "id": 707,
        "name": "Coppa Italia Women",
        "country": "Italy",
        "type": "cup",
        "tier": 1,
        "aliases": ["Italian Women's Cup", "Coppa Italia Femminile"],
    },

    # ============================================================
    # GERMANY (6 competitions)
    # ============================================================
    {
        "id": 78,
        "name": "Bundesliga",
        "country": "Germany",
        "type": "league",
        "tier": 1,
        "aliases": ["German Bundesliga", "1. Bundesliga", "Buli", "BuLi"],
    },
    {
        "id": 79,
        "name": "2. Bundesliga",
        "country": "Germany",
        "type": "league",
        "tier": 2,
        "aliases": ["German second division", "Zweite Bundesliga"],
    },
    {
        "id": 80,
        "name": "3. Liga",
        "country": "Germany",
        "type": "league",
        "tier": 3,
        "aliases": ["German third division", "Dritte Liga"],
    },
    {
        "id": 81,
        "name": "DFB Pokal",
        "country": "Germany",
        "type": "cup",
        "tier": 1,
        "aliases": ["German Cup", "Germany Cup", "DFB Cup"],
    },
    {
        "id": 529,
        "name": "Super Cup",
        "country": "Germany",
        "type": "cup",
        "tier": 1,
        "aliases": ["DFL-Supercup", "German Super Cup"],
    },
    {
        "id": 82,
        "name": "Frauen Bundesliga",
        "country": "Germany",
        "type": "league",
        "tier": 1,
        "aliases": ["German Women's Bundesliga", "Women's Bundesliga"],
    },
    {
        "id": 704,
        "name": "DFB Pokal - Women",
        "country": "Germany",
        "type": "cup",
        "tier": 1,
        "aliases": ["German Women's Cup", "DFB Pokal Frauen"],
    },

    # ============================================================
    # FRANCE (7 competitions)
    # ============================================================
    {
        "id": 61,
        "name": "Ligue 1",
        "country": "France",
        "type": "league",
        "tier": 1,
        "aliases": ["French Ligue 1", "Ligue 1 Uber Eats", "France Ligue 1", "L1"],
    },
    {
        "id": 62,
        "name": "Ligue 2",
        "country": "France",
        "type": "league",
        "tier": 2,
        "aliases": ["French Ligue 2", "French second division"],
    },
    {
        "id": 63,
        "name": "National 1",
        "country": "France",
        "type": "league",
        "tier": 3,
        "aliases": ["Championnat National", "French third division"],
    },
    {
        "id": 66,
        "name": "Coupe de France",
        "country": "France",
        "type": "cup",
        "tier": 1,
        "aliases": ["French Cup", "France Cup"],
    },
    {
        "id": 65,
        "name": "Coupe de la Ligue",
        "country": "France",
        "type": "cup",
        "tier": 2,
        "aliases": ["French League Cup"],
    },
    {
        "id": 526,
        "name": "Trophée des Champions",
        "country": "France",
        "type": "cup",
        "tier": 1,
        "aliases": ["French Super Cup", "Champions Trophy"],
    },
    {
        "id": 64,
        "name": "Feminine Division 1",
        "country": "France",
        "type": "league",
        "tier": 1,
        "aliases": ["D1 Arkema", "French Women's League", "Division 1 Féminine"],
    },

    # ============================================================
    # PORTUGAL (5 competitions)
    # ============================================================
    {
        "id": 94,
        "name": "Primeira Liga",
        "country": "Portugal",
        "type": "league",
        "tier": 1,
        "aliases": ["Liga Portugal", "Liga NOS", "Portuguese Primeira Liga"],
    },
    {
        "id": 95,
        "name": "Segunda Liga",
        "country": "Portugal",
        "type": "league",
        "tier": 2,
        "aliases": ["Liga Portugal 2", "Portuguese second division"],
    },
    {
        "id": 96,
        "name": "Taça de Portugal",
        "country": "Portugal",
        "type": "cup",
        "tier": 1,
        "aliases": ["Portuguese Cup", "Portugal Cup", "Taca de Portugal"],
    },
    {
        "id": 97,
        "name": "Taça da Liga",
        "country": "Portugal",
        "type": "cup",
        "tier": 2,
        "aliases": ["Portuguese League Cup", "Allianz Cup"],
    },
    {
        "id": 550,
        "name": "Super Cup",
        "country": "Portugal",
        "type": "cup",
        "tier": 1,
        "aliases": ["Supertaça", "Portuguese Super Cup"],
    },

    # ============================================================
    # NETHERLANDS (5 competitions)
    # ============================================================
    {
        "id": 88,
        "name": "Eredivisie",
        "country": "Netherlands",
        "type": "league",
        "tier": 1,
        "aliases": ["Dutch Eredivisie"],
    },
    {
        "id": 89,
        "name": "Eerste Divisie",
        "country": "Netherlands",
        "type": "league",
        "tier": 2,
        "aliases": ["Dutch second division", "Keuken Kampioen Divisie"],
    },
    {
        "id": 90,
        "name": "KNVB Beker",
        "country": "Netherlands",
        "type": "cup",
        "tier": 1,
        "aliases": ["Dutch Cup", "Netherlands Cup", "KNVB Cup"],
    },
    {
        "id": 543,
        "name": "Super Cup",
        "country": "Netherlands",
        "type": "cup",
        "tier": 1,
        "aliases": ["Johan Cruijff Schaal", "Dutch Super Cup"],
    },
    {
        "id": 710,
        "name": "Eredivisie Women",
        "country": "Netherlands",
        "type": "league",
        "tier": 1,
        "aliases": ["Dutch Women's League", "Vrouwen Eredivisie"],
    },

    # ============================================================
    # BELGIUM (4 competitions)
    # ============================================================
    {
        "id": 144,
        "name": "Jupiler Pro League",
        "country": "Belgium",
        "type": "league",
        "tier": 1,
        "aliases": ["Belgian Pro League", "First Division A"],
    },
    {
        "id": 145,
        "name": "Challenger Pro League",
        "country": "Belgium",
        "type": "league",
        "tier": 2,
        "aliases": ["First Division B", "Belgian second division"],
    },
    {
        "id": 147,
        "name": "Cup",
        "country": "Belgium",
        "type": "cup",
        "tier": 1,
        "aliases": ["Croky Cup", "Belgian Cup", "Beker van België"],
    },
    {
        "id": 554,
        "name": "Super Cup",
        "country": "Belgium",
        "type": "cup",
        "tier": 1,
        "aliases": ["Belgian Super Cup", "Supercup"],
    },

    # ============================================================
    # SCOTLAND (7 competitions)
    # ============================================================
    {
        "id": 179,
        "name": "Premiership",
        "country": "Scotland",
        "type": "league",
        "tier": 1,
        "aliases": ["Scottish Premiership", "Scottish Premier League", "SPL", "SPFL Premiership", "SPFL"],
    },
    {
        "id": 180,
        "name": "Championship",
        "country": "Scotland",
        "type": "league",
        "tier": 2,
        "aliases": ["Scottish Championship", "SPFL Championship"],
    },
    {
        "id": 181,
        "name": "League One",
        "country": "Scotland",
        "type": "league",
        "tier": 3,
        "aliases": ["Scottish League One", "SPFL League One"],
    },
    {
        "id": 182,
        "name": "League Two",
        "country": "Scotland",
        "type": "league",
        "tier": 4,
        "aliases": ["Scottish League Two", "SPFL League Two"],
    },
    {
        "id": 183,
        "name": "FA Cup",
        "country": "Scotland",
        "type": "cup",
        "tier": 1,
        "aliases": ["Scottish FA Cup", "Scottish Cup"],
    },
    {
        "id": 184,
        "name": "League Cup",
        "country": "Scotland",
        "type": "cup",
        "tier": 2,
        "aliases": ["Scottish League Cup", "Viaplay Cup"],
    },
    {
        "id": 185,
        "name": "Challenge Cup",
        "country": "Scotland",
        "type": "cup",
        "tier": 3,
        "aliases": ["Scottish Challenge Cup", "SPFL Trust Trophy"],
    },

    # ============================================================
    # TURKEY (4 competitions)
    # ============================================================
    {
        "id": 203,
        "name": "Süper Lig",
        "country": "Turkey",
        "type": "league",
        "tier": 1,
        "aliases": ["Turkish Super Lig", "Super Lig"],
    },
    {
        "id": 204,
        "name": "1. Lig",
        "country": "Turkey",
        "type": "league",
        "tier": 2,
        "aliases": ["TFF First League", "Turkish second division"],
    },
    {
        "id": 206,
        "name": "Türkiye Kupası",
        "country": "Turkey",
        "type": "cup",
        "tier": 1,
        "aliases": ["Turkish Cup", "Turkey Cup", "Ziraat Turkish Cup"],
    },
    {
        "id": 551,
        "name": "Super Cup",
        "country": "Turkey",
        "type": "cup",
        "tier": 1,
        "aliases": ["Turkish Super Cup", "Turkcell Super Cup"],
    },

    # ============================================================
    # GREECE (4 competitions)
    # ============================================================
    {
        "id": 197,
        "name": "Super League 1",
        "country": "Greece",
        "type": "league",
        "tier": 1,
        "aliases": ["Greek Super League"],
    },
    {
        "id": 198,
        "name": "Super League 2",
        "country": "Greece",
        "type": "league",
        "tier": 2,
        "aliases": ["Greek second division", "Football League"],
    },
    {
        "id": 199,
        "name": "Cup",
        "country": "Greece",
        "type": "cup",
        "tier": 1,
        "aliases": ["Greek Cup", "Kypello Elladas"],
    },
    {
        "id": 546,
        "name": "Super Cup",
        "country": "Greece",
        "type": "cup",
        "tier": 1,
        "aliases": ["Greek Super Cup"],
    },

    # ============================================================
    # AUSTRIA (3 competitions)
    # ============================================================
    {
        "id": 218,
        "name": "Bundesliga",
        "country": "Austria",
        "type": "league",
        "tier": 1,
        "aliases": ["Austrian Bundesliga"],
    },
    {
        "id": 219,
        "name": "2. Liga",
        "country": "Austria",
        "type": "league",
        "tier": 2,
        "aliases": ["Austrian second division"],
    },
    {
        "id": 220,
        "name": "Cup",
        "country": "Austria",
        "type": "cup",
        "tier": 1,
        "aliases": ["ÖFB Cup", "Austrian Cup"],
    },

    # ============================================================
    # SWITZERLAND (3 competitions)
    # ============================================================
    {
        "id": 207,
        "name": "Super League",
        "country": "Switzerland",
        "type": "league",
        "tier": 1,
        "aliases": ["Swiss Super League"],
    },
    {
        "id": 208,
        "name": "Challenge League",
        "country": "Switzerland",
        "type": "league",
        "tier": 2,
        "aliases": ["Swiss Challenge League", "Swiss second division"],
    },
    {
        "id": 209,
        "name": "Schweizer Cup",
        "country": "Switzerland",
        "type": "cup",
        "tier": 1,
        "aliases": ["Swiss Cup", "Helvetia Cup"],
    },

    # ============================================================
    # DENMARK (3 competitions)
    # ============================================================
    {
        "id": 119,
        "name": "Superliga",
        "country": "Denmark",
        "type": "league",
        "tier": 1,
        "aliases": ["Danish Superliga"],
    },
    {
        "id": 120,
        "name": "1. Division",
        "country": "Denmark",
        "type": "league",
        "tier": 2,
        "aliases": ["Danish first division", "NordicBet Liga"],
    },
    {
        "id": 121,
        "name": "DBU Pokalen",
        "country": "Denmark",
        "type": "cup",
        "tier": 1,
        "aliases": ["Danish Cup"],
    },

    # ============================================================
    # NORWAY (4 competitions)
    # ============================================================
    {
        "id": 103,
        "name": "Eliteserien",
        "country": "Norway",
        "type": "league",
        "tier": 1,
        "aliases": ["Norwegian Eliteserien", "Tippeligaen"],
    },
    {
        "id": 104,
        "name": "1. Division",
        "country": "Norway",
        "type": "league",
        "tier": 2,
        "aliases": ["OBOS-ligaen", "Norwegian first division"],
    },
    {
        "id": 105,
        "name": "NM Cupen",
        "country": "Norway",
        "type": "cup",
        "tier": 1,
        "aliases": ["Norwegian Cup", "Norgesmesterskapet"],
    },
    {
        "id": 541,
        "name": "Super Cup",
        "country": "Norway",
        "type": "cup",
        "tier": 1,
        "aliases": ["Mesterfinalen", "Norwegian Super Cup"],
    },

    # ============================================================
    # SWEDEN (3 competitions)
    # ============================================================
    {
        "id": 113,
        "name": "Allsvenskan",
        "country": "Sweden",
        "type": "league",
        "tier": 1,
        "aliases": ["Swedish Allsvenskan"],
    },
    {
        "id": 114,
        "name": "Superettan",
        "country": "Sweden",
        "type": "league",
        "tier": 2,
        "aliases": ["Swedish Superettan", "Swedish second division"],
    },
    {
        "id": 115,
        "name": "Svenska Cupen",
        "country": "Sweden",
        "type": "cup",
        "tier": 1,
        "aliases": ["Swedish Cup"],
    },

    # ============================================================
    # FINLAND (4 competitions)
    # ============================================================
    {
        "id": 244,
        "name": "Veikkausliiga",
        "country": "Finland",
        "type": "league",
        "tier": 1,
        "aliases": ["Finnish Premier League"],
    },
    {
        "id": 245,
        "name": "Ykkösliiga",
        "country": "Finland",
        "type": "league",
        "tier": 2,
        "aliases": ["Finnish first division", "Ykkönen"],
    },
    {
        "id": 246,
        "name": "Suomen Cup",
        "country": "Finland",
        "type": "cup",
        "tier": 1,
        "aliases": ["Finnish Cup"],
    },
    {
        "id": 247,
        "name": "League Cup",
        "country": "Finland",
        "type": "cup",
        "tier": 2,
        "aliases": ["Finnish League Cup", "Liigacup"],
    },

    # ============================================================
    # POLAND (4 competitions)
    # ============================================================
    {
        "id": 106,
        "name": "Ekstraklasa",
        "country": "Poland",
        "type": "league",
        "tier": 1,
        "aliases": ["Polish Ekstraklasa"],
    },
    {
        "id": 107,
        "name": "I Liga",
        "country": "Poland",
        "type": "league",
        "tier": 2,
        "aliases": ["Polish first division", "Fortuna 1 Liga"],
    },
    {
        "id": 108,
        "name": "Cup",
        "country": "Poland",
        "type": "cup",
        "tier": 1,
        "aliases": ["Puchar Polski", "Polish Cup"],
    },
    {
        "id": 538,
        "name": "Super Cup",
        "country": "Poland",
        "type": "cup",
        "tier": 1,
        "aliases": ["Superpuchar Polski", "Polish Super Cup"],
    },

    # ============================================================
    # CZECH REPUBLIC (4 competitions)
    # ============================================================
    {
        "id": 345,
        "name": "Czech Liga",
        "country": "Czech-Republic",
        "type": "league",
        "tier": 1,
        "aliases": ["First League", "Fortuna Liga"],
    },
    {
        "id": 346,
        "name": "FNL",
        "country": "Czech-Republic",
        "type": "league",
        "tier": 2,
        "aliases": ["Czech second division", "Fortuna Narodni Liga"],
    },
    {
        "id": 347,
        "name": "Cup",
        "country": "Czech-Republic",
        "type": "cup",
        "tier": 1,
        "aliases": ["MOL Cup", "Czech Cup"],
    },
    {
        "id": 630,
        "name": "Super Cup",
        "country": "Czech-Republic",
        "type": "cup",
        "tier": 1,
        "aliases": ["Czech Super Cup"],
    },

    # ============================================================
    # ROMANIA (4 competitions)
    # ============================================================
    {
        "id": 283,
        "name": "Liga I",
        "country": "Romania",
        "type": "league",
        "tier": 1,
        "aliases": ["Romanian Liga I", "SuperLiga"],
    },
    {
        "id": 284,
        "name": "Liga II",
        "country": "Romania",
        "type": "league",
        "tier": 2,
        "aliases": ["Romanian second division"],
    },
    {
        "id": 285,
        "name": "Cupa României",
        "country": "Romania",
        "type": "cup",
        "tier": 1,
        "aliases": ["Romanian Cup", "Cupa Romaniei"],
    },
    {
        "id": 575,
        "name": "Supercupa",
        "country": "Romania",
        "type": "cup",
        "tier": 1,
        "aliases": ["Romanian Super Cup"],
    },

    # ============================================================
    # UKRAINE (4 competitions)
    # ============================================================
    {
        "id": 333,
        "name": "Premier League",
        "country": "Ukraine",
        "type": "league",
        "tier": 1,
        "aliases": ["Ukrainian Premier League", "UPL"],
    },
    {
        "id": 334,
        "name": "Persha Liga",
        "country": "Ukraine",
        "type": "league",
        "tier": 2,
        "aliases": ["Ukrainian first league"],
    },
    {
        "id": 335,
        "name": "Cup",
        "country": "Ukraine",
        "type": "cup",
        "tier": 1,
        "aliases": ["Ukrainian Cup", "Kubok Ukrayiny"],
    },
    {
        "id": 596,
        "name": "Super Cup",
        "country": "Ukraine",
        "type": "cup",
        "tier": 1,
        "aliases": ["Ukrainian Super Cup"],
    },

    # ============================================================
    # RUSSIA (4 competitions)
    # ============================================================
    {
        "id": 235,
        "name": "Premier League",
        "country": "Russia",
        "type": "league",
        "tier": 1,
        "aliases": ["Russian Premier League", "RPL"],
    },
    {
        "id": 236,
        "name": "First League",
        "country": "Russia",
        "type": "league",
        "tier": 2,
        "aliases": ["Russian first league", "FNL"],
    },
    {
        "id": 237,
        "name": "Cup",
        "country": "Russia",
        "type": "cup",
        "tier": 1,
        "aliases": ["Russian Cup", "Kubok Rossii"],
    },
    {
        "id": 557,
        "name": "Super Cup",
        "country": "Russia",
        "type": "cup",
        "tier": 1,
        "aliases": ["Russian Super Cup"],
    },

    # ============================================================
    # CROATIA (4 competitions)
    # ============================================================
    {
        "id": 210,
        "name": "HNL",
        "country": "Croatia",
        "type": "league",
        "tier": 1,
        "aliases": ["Prva HNL", "Croatian First Football League"],
    },
    {
        "id": 211,
        "name": "First NL",
        "country": "Croatia",
        "type": "league",
        "tier": 2,
        "aliases": ["Druga HNL", "Croatian second division"],
    },
    {
        "id": 212,
        "name": "Cup",
        "country": "Croatia",
        "type": "cup",
        "tier": 1,
        "aliases": ["Hrvatski nogometni kup", "Croatian Cup"],
    },
    {
        "id": 544,
        "name": "Super Cup",
        "country": "Croatia",
        "type": "cup",
        "tier": 1,
        "aliases": ["Croatian Super Cup", "Hrvatski Superkup"],
    },

    # ============================================================
    # SERBIA (3 competitions)
    # ============================================================
    {
        "id": 286,
        "name": "Super Liga",
        "country": "Serbia",
        "type": "league",
        "tier": 1,
        "aliases": ["Serbian Super Liga"],
    },
    {
        "id": 287,
        "name": "Prva Liga",
        "country": "Serbia",
        "type": "league",
        "tier": 2,
        "aliases": ["Serbian first league"],
    },
    {
        "id": 288,
        "name": "Cup",
        "country": "Serbia",
        "type": "cup",
        "tier": 1,
        "aliases": ["Serbian Cup", "Kup Srbije"],
    },

    # ============================================================
    # HUNGARY (3 competitions)
    # ============================================================
    {
        "id": 271,
        "name": "NB I",
        "country": "Hungary",
        "type": "league",
        "tier": 1,
        "aliases": ["Nemzeti Bajnokság I", "Hungarian first division"],
    },
    {
        "id": 272,
        "name": "NB II",
        "country": "Hungary",
        "type": "league",
        "tier": 2,
        "aliases": ["Nemzeti Bajnokság II", "Hungarian second division"],
    },
    {
        "id": 273,
        "name": "Magyar Kupa",
        "country": "Hungary",
        "type": "cup",
        "tier": 1,
        "aliases": ["Hungarian Cup"],
    },

    # ============================================================
    # BULGARIA (4 competitions)
    # ============================================================
    {
        "id": 172,
        "name": "First League",
        "country": "Bulgaria",
        "type": "league",
        "tier": 1,
        "aliases": ["Bulgarian First League", "Parva Liga"],
    },
    {
        "id": 173,
        "name": "Second League",
        "country": "Bulgaria",
        "type": "league",
        "tier": 2,
        "aliases": ["Bulgarian second division", "Vtora Liga"],
    },
    {
        "id": 174,
        "name": "Cup",
        "country": "Bulgaria",
        "type": "cup",
        "tier": 1,
        "aliases": ["Bulgarian Cup"],
    },
    {
        "id": 534,
        "name": "Super Cup",
        "country": "Bulgaria",
        "type": "cup",
        "tier": 1,
        "aliases": ["Bulgarian Super Cup"],
    },

    # ============================================================
    # SLOVAKIA (3 competitions)
    # ============================================================
    {
        "id": 332,
        "name": "Super Liga",
        "country": "Slovakia",
        "type": "league",
        "tier": 1,
        "aliases": ["Slovak Super Liga", "Fortuna Liga"],
    },
    {
        "id": 398,
        "name": "2. liga",
        "country": "Slovakia",
        "type": "league",
        "tier": 2,
        "aliases": ["Slovak second division"],
    },
    {
        "id": 399,
        "name": "Cup",
        "country": "Slovakia",
        "type": "cup",
        "tier": 1,
        "aliases": ["Slovak Cup", "Slovnaft Cup"],
    },

    # ============================================================
    # SLOVENIA (3 competitions)
    # ============================================================
    {
        "id": 373,
        "name": "1. SNL",
        "country": "Slovenia",
        "type": "league",
        "tier": 1,
        "aliases": ["PrvaLiga", "Slovenian First League"],
    },
    {
        "id": 374,
        "name": "2. SNL",
        "country": "Slovenia",
        "type": "league",
        "tier": 2,
        "aliases": ["Slovenian second division"],
    },
    {
        "id": 375,
        "name": "Cup",
        "country": "Slovenia",
        "type": "cup",
        "tier": 1,
        "aliases": ["Slovenian Cup", "Pokal Slovenije"],
    },

    # ============================================================
    # CYPRUS (4 competitions)
    # ============================================================
    {
        "id": 318,
        "name": "1. Division",
        "country": "Cyprus",
        "type": "league",
        "tier": 1,
        "aliases": ["Cypriot First Division"],
    },
    {
        "id": 319,
        "name": "2. Division",
        "country": "Cyprus",
        "type": "league",
        "tier": 2,
        "aliases": ["Cypriot second division"],
    },
    {
        "id": 320,
        "name": "Cup",
        "country": "Cyprus",
        "type": "cup",
        "tier": 1,
        "aliases": ["Cypriot Cup"],
    },
    {
        "id": 586,
        "name": "Super Cup",
        "country": "Cyprus",
        "type": "cup",
        "tier": 1,
        "aliases": ["Cypriot Super Cup"],
    },

    # ============================================================
    # WALES (3 competitions)
    # ============================================================
    {
        "id": 110,
        "name": "Premier League",
        "country": "Wales",
        "type": "league",
        "tier": 1,
        "aliases": ["Cymru Premier", "Welsh Premier League"],
    },
    {
        "id": 111,
        "name": "League Cup",
        "country": "Wales",
        "type": "cup",
        "tier": 2,
        "aliases": ["Welsh League Cup", "JD Welsh Premier League Cup"],
    },
    {
        "id": 112,
        "name": "Welsh Cup",
        "country": "Wales",
        "type": "cup",
        "tier": 1,
        "aliases": ["FAW Welsh Cup"],
    },

    # ============================================================
    # NORTHERN IRELAND (4 competitions)
    # ============================================================
    {
        "id": 408,
        "name": "Premiership",
        "country": "Northern-Ireland",
        "type": "league",
        "tier": 1,
        "aliases": ["NIFL Premiership", "Irish Premiership"],
    },
    {
        "id": 409,
        "name": "Championship",
        "country": "Northern-Ireland",
        "type": "league",
        "tier": 2,
        "aliases": ["NIFL Championship"],
    },
    {
        "id": 410,
        "name": "Irish Cup",
        "country": "Northern-Ireland",
        "type": "cup",
        "tier": 1,
        "aliases": ["Northern Irish Cup"],
    },
    {
        "id": 411,
        "name": "League Cup",
        "country": "Northern-Ireland",
        "type": "cup",
        "tier": 2,
        "aliases": ["Northern Irish League Cup"],
    },

    # ============================================================
    # IRELAND (5 competitions)
    # ============================================================
    {
        "id": 357,
        "name": "Premier Division",
        "country": "Ireland",
        "type": "league",
        "tier": 1,
        "aliases": ["League of Ireland Premier Division"],
    },
    {
        "id": 358,
        "name": "First Division",
        "country": "Ireland",
        "type": "league",
        "tier": 2,
        "aliases": ["League of Ireland First Division"],
    },
    {
        "id": 359,
        "name": "FAI Cup",
        "country": "Ireland",
        "type": "cup",
        "tier": 1,
        "aliases": ["Irish Cup", "FAI Senior Cup"],
    },
    {
        "id": 360,
        "name": "League Cup",
        "country": "Ireland",
        "type": "cup",
        "tier": 2,
        "aliases": ["FAI League Cup"],
    },
    {
        "id": 607,
        "name": "FAI President's Cup",
        "country": "Ireland",
        "type": "cup",
        "tier": 1,
        "aliases": ["Irish Super Cup", "President's Cup"],
    },

    # ============================================================
    # ICELAND (5 competitions)
    # ============================================================
    {
        "id": 352,
        "name": "1. Deild",
        "country": "Iceland",
        "type": "league",
        "tier": 1,
        "aliases": ["Úrvalsdeild", "Icelandic Premier League"],
    },
    {
        "id": 353,
        "name": "2. Deild",
        "country": "Iceland",
        "type": "league",
        "tier": 2,
        "aliases": ["Icelandic first division"],
    },
    {
        "id": 354,
        "name": "Cup",
        "country": "Iceland",
        "type": "cup",
        "tier": 1,
        "aliases": ["Icelandic Cup", "Borgunarbikar"],
    },
    {
        "id": 355,
        "name": "League Cup",
        "country": "Iceland",
        "type": "cup",
        "tier": 2,
        "aliases": ["Icelandic League Cup", "Deildabikar"],
    },
    {
        "id": 605,
        "name": "Super Cup",
        "country": "Iceland",
        "type": "cup",
        "tier": 1,
        "aliases": ["Icelandic Super Cup"],
    },

    # ============================================================
    # ESTONIA (3 competitions)
    # ============================================================
    {
        "id": 329,
        "name": "Meistriliiga",
        "country": "Estonia",
        "type": "league",
        "tier": 1,
        "aliases": ["Estonian Meistriliiga", "Premium Liiga"],
    },
    {
        "id": 330,
        "name": "Esiliiga A",
        "country": "Estonia",
        "type": "league",
        "tier": 2,
        "aliases": ["Estonian first division"],
    },
    {
        "id": 331,
        "name": "Cup",
        "country": "Estonia",
        "type": "cup",
        "tier": 1,
        "aliases": ["Estonian Cup"],
    },

    # ============================================================
    # LITHUANIA (4 competitions)
    # ============================================================
    {
        "id": 362,
        "name": "A Lyga",
        "country": "Lithuania",
        "type": "league",
        "tier": 1,
        "aliases": ["Lithuanian A Lyga"],
    },
    {
        "id": 363,
        "name": "1 Lyga",
        "country": "Lithuania",
        "type": "league",
        "tier": 2,
        "aliases": ["Lithuanian first division"],
    },
    {
        "id": 364,
        "name": "Cup",
        "country": "Lithuania",
        "type": "cup",
        "tier": 1,
        "aliases": ["Lithuanian Cup", "LFF Taurė"],
    },
    {
        "id": 609,
        "name": "Super Cup",
        "country": "Lithuania",
        "type": "cup",
        "tier": 1,
        "aliases": ["Lithuanian Super Cup"],
    },

    # ============================================================
    # GEORGIA (4 competitions)
    # ============================================================
    {
        "id": 327,
        "name": "Erovnuli Liga",
        "country": "Georgia",
        "type": "league",
        "tier": 1,
        "aliases": ["Georgian Premier League"],
    },
    {
        "id": 328,
        "name": "Erovnuli Liga 2",
        "country": "Georgia",
        "type": "league",
        "tier": 2,
        "aliases": ["Georgian first division"],
    },
    {
        "id": 588,
        "name": "David Kipiani Cup",
        "country": "Georgia",
        "type": "cup",
        "tier": 1,
        "aliases": ["Georgian Cup"],
    },
    {
        "id": 589,
        "name": "Super Cup",
        "country": "Georgia",
        "type": "cup",
        "tier": 1,
        "aliases": ["Georgian Super Cup"],
    },

    # ============================================================
    # ARMENIA (3 competitions)
    # ============================================================
    {
        "id": 380,
        "name": "Premier League",
        "country": "Armenia",
        "type": "league",
        "tier": 1,
        "aliases": ["Armenian Premier League"],
    },
    {
        "id": 619,
        "name": "Super Cup",
        "country": "Armenia",
        "type": "cup",
        "tier": 1,
        "aliases": ["Armenian Super Cup"],
    },
    {
        "id": 381,
        "name": "Cup",
        "country": "Armenia",
        "type": "cup",
        "tier": 1,
        "aliases": ["Armenian Cup"],
    },

    # ============================================================
    # AZERBAIJAN (2 competitions)
    # ============================================================
    {
        "id": 371,
        "name": "Premyer Liqa",
        "country": "Azerbaijan",
        "type": "league",
        "tier": 1,
        "aliases": ["Azerbaijan Premier League"],
    },
    {
        "id": 372,
        "name": "Cup",
        "country": "Azerbaijan",
        "type": "cup",
        "tier": 1,
        "aliases": ["Azerbaijan Cup"],
    },

    # ============================================================
    # BELARUS (4 competitions)
    # ============================================================
    {
        "id": 117,
        "name": "Premier League",
        "country": "Belarus",
        "type": "league",
        "tier": 1,
        "aliases": ["Belarus Premier League", "Belarusian Premier League", "Vysshaya Liga"],
    },
    {
        "id": 118,
        "name": "1. Division",
        "country": "Belarus",
        "type": "league",
        "tier": 2,
        "aliases": ["Belarusian first division"],
    },
    {
        "id": 500,
        "name": "Coppa",
        "country": "Belarus",
        "type": "cup",
        "tier": 1,
        "aliases": ["Belarusian Cup"],
    },
    {
        "id": 501,
        "name": "Super Cup",
        "country": "Belarus",
        "type": "cup",
        "tier": 1,
        "aliases": ["Belarusian Super Cup"],
    },

    # ============================================================
    # MOLDOVA (2 competitions)
    # ============================================================
    {
        "id": 377,
        "name": "Super Liga",
        "country": "Moldova",
        "type": "league",
        "tier": 1,
        "aliases": ["Moldovan Super Liga", "Divizia Nationala"],
    },
    {
        "id": 378,
        "name": "Cupa",
        "country": "Moldova",
        "type": "cup",
        "tier": 1,
        "aliases": ["Moldovan Cup", "Cupa Moldovei"],
    },

    # ============================================================
    # ISRAEL (4 competitions)
    # ============================================================
    {
        "id": 383,
        "name": "Ligat Ha'al",
        "country": "Israel",
        "type": "league",
        "tier": 1,
        "aliases": ["Israeli Premier League"],
    },
    {
        "id": 384,
        "name": "Liga Leumit",
        "country": "Israel",
        "type": "league",
        "tier": 2,
        "aliases": ["Israeli National League"],
    },
    {
        "id": 385,
        "name": "State Cup",
        "country": "Israel",
        "type": "cup",
        "tier": 1,
        "aliases": ["Israeli Cup", "Gvia HaMedina"],
    },
    {
        "id": 614,
        "name": "Super Cup",
        "country": "Israel",
        "type": "cup",
        "tier": 1,
        "aliases": ["Israeli Super Cup"],
    },

    # ============================================================
    # ALBANIA (3 competitions)
    # ============================================================
    {
        "id": 310,
        "name": "Superliga",
        "country": "Albania",
        "type": "league",
        "tier": 1,
        "aliases": ["Albanian Superliga", "Kategoria Superiore"],
    },
    {
        "id": 579,
        "name": "Super Cup",
        "country": "Albania",
        "type": "cup",
        "tier": 1,
        "aliases": ["Albanian Super Cup"],
    },
    {
        "id": 311,
        "name": "Cup",
        "country": "Albania",
        "type": "cup",
        "tier": 1,
        "aliases": ["Albanian Cup", "Kupa e Shqipërisë"],
    },

    # ============================================================
    # BOSNIA (3 competitions)
    # ============================================================
    {
        "id": 365,
        "name": "Premijer Liga",
        "country": "Bosnia",
        "type": "league",
        "tier": 1,
        "aliases": ["Bosnian Premier Liga"],
    },
    {
        "id": 366,
        "name": "Cup",
        "country": "Bosnia",
        "type": "cup",
        "tier": 1,
        "aliases": ["Bosnian Cup", "Kup Bosne i Hercegovine"],
    },
    {
        "id": 610,
        "name": "Super Cup",
        "country": "Bosnia",
        "type": "cup",
        "tier": 1,
        "aliases": ["Bosnian Super Cup"],
    },

    # ============================================================
    # ANDORRA (2 competitions)
    # ============================================================
    {
        "id": 387,
        "name": "1a Divisió",
        "country": "Andorra",
        "type": "league",
        "tier": 1,
        "aliases": ["Primera Divisió Andorra", "Andorran first division"],
    },
    {
        "id": 388,
        "name": "2a Divisió",
        "country": "Andorra",
        "type": "league",
        "tier": 2,
        "aliases": ["Andorran second division"],
    },

    # ============================================================
    # BRAZIL (6 competitions)
    # ============================================================
    {
        "id": 71,
        "name": "Serie A",
        "country": "Brazil",
        "type": "league",
        "tier": 1,
        "aliases": ["Brazilian Serie A", "Brasileirão"],
    },
    {
        "id": 72,
        "name": "Serie B",
        "country": "Brazil",
        "type": "league",
        "tier": 2,
        "aliases": ["Brazilian Serie B"],
    },
    {
        "id": 73,
        "name": "Serie C",
        "country": "Brazil",
        "type": "league",
        "tier": 3,
        "aliases": ["Brazilian Serie C"],
    },
    {
        "id": 74,
        "name": "Serie D",
        "country": "Brazil",
        "type": "league",
        "tier": 4,
        "aliases": ["Brazilian Serie D"],
    },
    {
        "id": 75,
        "name": "Copa Do Brasil",
        "country": "Brazil",
        "type": "cup",
        "tier": 1,
        "aliases": ["Brazilian Cup", "Brazil Cup"],
    },
    {
        "id": 553,
        "name": "Supercopa do Brasil",
        "country": "Brazil",
        "type": "cup",
        "tier": 1,
        "aliases": ["Brazilian Super Cup"],
    },

    # ============================================================
    # ARGENTINA (5 competitions)
    # ============================================================
    {
        "id": 128,
        "name": "Liga Profesional Argentina",
        "country": "Argentina",
        "type": "league",
        "tier": 1,
        "aliases": ["Argentine Primera División", "Liga Argentina"],
    },
    {
        "id": 129,
        "name": "Primera Nacional",
        "country": "Argentina",
        "type": "league",
        "tier": 2,
        "aliases": ["Argentine second division", "Primera B Nacional"],
    },
    {
        "id": 130,
        "name": "Copa Argentina",
        "country": "Argentina",
        "type": "cup",
        "tier": 1,
        "aliases": ["Argentine Cup"],
    },
    {
        "id": 131,
        "name": "Copa de la Liga Profesional",
        "country": "Argentina",
        "type": "cup",
        "tier": 1,
        "aliases": ["Argentine League Cup"],
    },
    {
        "id": 647,
        "name": "Copa de la Superliga",
        "country": "Argentina",
        "type": "cup",
        "tier": 2,
        "aliases": ["Superliga Cup"],
    },

    # ============================================================
    # CHILE (6 competitions)
    # ============================================================
    {
        "id": 265,
        "name": "Primera División",
        "country": "Chile",
        "type": "league",
        "tier": 1,
        "aliases": ["Chilean Primera División"],
    },
    {
        "id": 266,
        "name": "Segunda División",
        "country": "Chile",
        "type": "league",
        "tier": 2,
        "aliases": ["Chilean second division", "Primera B"],
    },
    {
        "id": 897,
        "name": "Primera B",
        "country": "Chile",
        "type": "league",
        "tier": 2,
        "aliases": ["Chilean Primera B"],
    },
    {
        "id": 267,
        "name": "Copa Chile",
        "country": "Chile",
        "type": "cup",
        "tier": 1,
        "aliases": ["Chilean Cup"],
    },
    {
        "id": 665,
        "name": "Copa De La Liga",
        "country": "Chile",
        "type": "cup",
        "tier": 2,
        "aliases": ["Chilean League Cup"],
    },
    {
        "id": 569,
        "name": "Super Cup",
        "country": "Chile",
        "type": "cup",
        "tier": 1,
        "aliases": ["Supercopa de Chile", "Chilean Super Cup"],
    },

    # ============================================================
    # COLOMBIA (4 competitions)
    # ============================================================
    {
        "id": 239,
        "name": "Primera A",
        "country": "Colombia",
        "type": "league",
        "tier": 1,
        "aliases": ["Liga BetPlay Dimayor", "Colombian Primera A"],
    },
    {
        "id": 240,
        "name": "Primera B",
        "country": "Colombia",
        "type": "league",
        "tier": 2,
        "aliases": ["Torneo BetPlay Dimayor", "Colombian second division"],
    },
    {
        "id": 868,
        "name": "Superliga",
        "country": "Colombia",
        "type": "cup",
        "tier": 1,
        "aliases": ["Colombian Superliga"],
    },
    {
        "id": 241,
        "name": "Copa Colombia",
        "country": "Colombia",
        "type": "cup",
        "tier": 1,
        "aliases": ["Colombian Cup"],
    },

    # ============================================================
    # PERU (5 competitions)
    # ============================================================
    {
        "id": 281,
        "name": "Primera División",
        "country": "Peru",
        "type": "league",
        "tier": 1,
        "aliases": ["Liga 1", "Peruvian first division"],
    },
    {
        "id": 282,
        "name": "Segunda División",
        "country": "Peru",
        "type": "league",
        "tier": 2,
        "aliases": ["Liga 2", "Peruvian second division"],
    },
    {
        "id": 666,
        "name": "Copa De La Liga",
        "country": "Peru",
        "type": "cup",
        "tier": 2,
        "aliases": ["Peruvian League Cup"],
    },
    {
        "id": 667,
        "name": "Copa Perú",
        "country": "Peru",
        "type": "cup",
        "tier": 1,
        "aliases": ["Peru Cup"],
    },
    {
        "id": 574,
        "name": "Supercopa",
        "country": "Peru",
        "type": "cup",
        "tier": 1,
        "aliases": ["Peruvian Super Cup"],
    },

    # ============================================================
    # ECUADOR (3 competitions)
    # ============================================================
    {
        "id": 242,
        "name": "Liga Pro",
        "country": "Ecuador",
        "type": "league",
        "tier": 1,
        "aliases": ["LigaPro Serie A", "Ecuadorian first division"],
    },
    {
        "id": 243,
        "name": "Liga Pro Serie B",
        "country": "Ecuador",
        "type": "league",
        "tier": 2,
        "aliases": ["Ecuadorian second division"],
    },
    {
        "id": 650,
        "name": "Copa Ecuador",
        "country": "Ecuador",
        "type": "cup",
        "tier": 1,
        "aliases": ["Ecuadorian Cup"],
    },

    # ============================================================
    # URUGUAY (5 competitions)
    # ============================================================
    {
        "id": 268,
        "name": "Primera División - Apertura",
        "country": "Uruguay",
        "type": "league",
        "tier": 1,
        "aliases": ["Uruguayan Apertura"],
    },
    {
        "id": 269,
        "name": "Primera División - Clausura",
        "country": "Uruguay",
        "type": "league",
        "tier": 1,
        "aliases": ["Uruguayan Clausura"],
    },
    {
        "id": 270,
        "name": "Segunda División",
        "country": "Uruguay",
        "type": "league",
        "tier": 2,
        "aliases": ["Uruguayan second division"],
    },
    {
        "id": 648,
        "name": "Copa Uruguay",
        "country": "Uruguay",
        "type": "cup",
        "tier": 1,
        "aliases": ["Uruguayan Cup"],
    },
    {
        "id": 573,
        "name": "Super Copa",
        "country": "Uruguay",
        "type": "cup",
        "tier": 1,
        "aliases": ["Uruguayan Super Cup"],
    },

    # ============================================================
    # PARAGUAY (4 competitions)
    # ============================================================
    {
        "id": 279,
        "name": "Division Profesional - Apertura",
        "country": "Paraguay",
        "type": "league",
        "tier": 1,
        "aliases": ["Paraguayan Apertura"],
    },
    {
        "id": 280,
        "name": "Division Profesional - Clausura",
        "country": "Paraguay",
        "type": "league",
        "tier": 1,
        "aliases": ["Paraguayan Clausura"],
    },
    {
        "id": 649,
        "name": "Copa Paraguay",
        "country": "Paraguay",
        "type": "cup",
        "tier": 1,
        "aliases": ["Paraguayan Cup"],
    },
    {
        "id": 572,
        "name": "Supercopa",
        "country": "Paraguay",
        "type": "cup",
        "tier": 1,
        "aliases": ["Paraguayan Super Cup"],
    },

    # ============================================================
    # BOLIVIA (2 competitions)
    # ============================================================
    {
        "id": 157,
        "name": "Primera División",
        "country": "Bolivia",
        "type": "league",
        "tier": 1,
        "aliases": ["Bolivian Primera División", "Liga de Fútbol Profesional"],
    },
    {
        "id": 651,
        "name": "Copa de la División Profesional",
        "country": "Bolivia",
        "type": "cup",
        "tier": 1,
        "aliases": ["Bolivian Cup"],
    },

    # ============================================================
    # VENEZUELA (4 competitions)
    # ============================================================
    {
        "id": 299,
        "name": "Primera División",
        "country": "Venezuela",
        "type": "league",
        "tier": 1,
        "aliases": ["Venezuelan Primera División"],
    },
    {
        "id": 300,
        "name": "Segunda División",
        "country": "Venezuela",
        "type": "league",
        "tier": 2,
        "aliases": ["Venezuelan second division"],
    },
    {
        "id": 652,
        "name": "Copa Venezuela",
        "country": "Venezuela",
        "type": "cup",
        "tier": 1,
        "aliases": ["Venezuelan Cup"],
    },
    {
        "id": 571,
        "name": "Supercopa",
        "country": "Venezuela",
        "type": "cup",
        "tier": 1,
        "aliases": ["Venezuelan Super Cup"],
    },

    # ============================================================
    # MEXICO (4 competitions)
    # ============================================================
    {
        "id": 262,
        "name": "Liga MX",
        "country": "Mexico",
        "type": "league",
        "tier": 1,
        "aliases": ["Mexican league", "Mexico league"],
    },
    {
        "id": 263,
        "name": "Copa MX",
        "country": "Mexico",
        "type": "cup",
        "tier": 1,
        "aliases": ["Mexican Cup"],
    },
    {
        "id": 866,
        "name": "Copa por México",
        "country": "Mexico",
        "type": "cup",
        "tier": 2,
        "aliases": [],
    },
    {
        "id": 567,
        "name": "Campeón de Campeones",
        "country": "Mexico",
        "type": "cup",
        "tier": 1,
        "aliases": ["Mexican Super Cup", "Champion of Champions"],
    },

    # ============================================================
    # USA (1 competition)
    # ============================================================
    {
        "id": 253,
        "name": "Major League Soccer",
        "country": "USA",
        "type": "league",
        "tier": 1,
        "aliases": ["MLS", "American league", "USA league", "US league"],
    },

    # ============================================================
    # CANADA (2 competitions)
    # ============================================================
    {
        "id": 253,
        "name": "Canadian Premier League",
        "country": "Canada",
        "type": "league",
        "tier": 1,
        "aliases": ["CPL"],
    },
    {
        "id": 654,
        "name": "Canadian Championship",
        "country": "Canada",
        "type": "cup",
        "tier": 1,
        "aliases": ["Voyageurs Cup"],
    },

    # ============================================================
    # COSTA RICA (3 competitions)
    # ============================================================
    {
        "id": 163,
        "name": "Primera División",
        "country": "Costa-Rica",
        "type": "league",
        "tier": 1,
        "aliases": ["Costa Rican Primera División"],
    },
    {
        "id": 655,
        "name": "Copa Costa Rica",
        "country": "Costa-Rica",
        "type": "cup",
        "tier": 1,
        "aliases": ["Costa Rican Cup"],
    },
    {
        "id": 627,
        "name": "Supercopa",
        "country": "Costa-Rica",
        "type": "cup",
        "tier": 1,
        "aliases": ["Costa Rican Super Cup"],
    },

    # ============================================================
    # HONDURAS (1 competition)
    # ============================================================
    {
        "id": 168,
        "name": "Liga Nacional",
        "country": "Honduras",
        "type": "league",
        "tier": 1,
        "aliases": ["Honduran Liga Nacional"],
    },

    # ============================================================
    # JAPAN (5 competitions)
    # ============================================================
    {
        "id": 98,
        "name": "J1 League",
        "country": "Japan",
        "type": "league",
        "tier": 1,
        "aliases": ["J.League Division 1", "J-League", "J League", "J1", "Japanese J League"],
    },
    {
        "id": 99,
        "name": "J2 League",
        "country": "Japan",
        "type": "league",
        "tier": 2,
        "aliases": ["J.League Division 2", "J2", "Japanese J2 League"],
    },
    {
        "id": 100,
        "name": "J-League Cup",
        "country": "Japan",
        "type": "cup",
        "tier": 2,
        "aliases": ["J.League YBC Levain Cup", "Levain Cup"],
    },
    {
        "id": 101,
        "name": "Emperor Cup",
        "country": "Japan",
        "type": "cup",
        "tier": 1,
        "aliases": ["Japanese Cup", "Tennō Hai"],
    },
    {
        "id": 564,
        "name": "Super Cup",
        "country": "Japan",
        "type": "cup",
        "tier": 1,
        "aliases": ["Japanese Super Cup", "Fuji Xerox Super Cup"],
    },

    # ============================================================
    # SOUTH KOREA (3 competitions)
    # ============================================================
    {
        "id": 292,
        "name": "K League 1",
        "country": "South-Korea",
        "type": "league",
        "tier": 1,
        "aliases": ["Korean K League 1", "K-League", "K League", "Korean league"],
    },
    {
        "id": 293,
        "name": "K League 2",
        "country": "South-Korea",
        "type": "league",
        "tier": 2,
        "aliases": ["Korean K League 2"],
    },
    {
        "id": 294,
        "name": "FA Cup",
        "country": "South-Korea",
        "type": "cup",
        "tier": 1,
        "aliases": ["Korean FA Cup"],
    },

    # ============================================================
    # CHINA (5 competitions)
    # ============================================================
    {
        "id": 169,
        "name": "Super League",
        "country": "China",
        "type": "league",
        "tier": 1,
        "aliases": ["Chinese Super League", "CSL"],
    },
    {
        "id": 170,
        "name": "League One",
        "country": "China",
        "type": "league",
        "tier": 2,
        "aliases": ["Chinese League One"],
    },
    {
        "id": 171,
        "name": "League Two",
        "country": "China",
        "type": "league",
        "tier": 3,
        "aliases": ["Chinese League Two"],
    },
    {
        "id": 701,
        "name": "FA Cup",
        "country": "China",
        "type": "cup",
        "tier": 1,
        "aliases": ["Chinese FA Cup", "CFA Cup"],
    },
    {
        "id": 622,
        "name": "Super Cup",
        "country": "China",
        "type": "cup",
        "tier": 1,
        "aliases": ["Chinese Super Cup"],
    },

    # ============================================================
    # AUSTRALIA (1 competition)
    # ============================================================
    {
        "id": 188,
        "name": "A-League",
        "country": "Australia",
        "type": "league",
        "tier": 1,
        "aliases": ["A-League Men", "Australian A-League"],
    },

    # ============================================================
    # THAILAND (3 competitions)
    # ============================================================
    {
        "id": 296,
        "name": "Thai League 1",
        "country": "Thailand",
        "type": "league",
        "tier": 1,
        "aliases": ["Thai Premier League"],
    },
    {
        "id": 297,
        "name": "FA Cup",
        "country": "Thailand",
        "type": "cup",
        "tier": 1,
        "aliases": ["Thai FA Cup"],
    },
    {
        "id": 298,
        "name": "League Cup",
        "country": "Thailand",
        "type": "cup",
        "tier": 2,
        "aliases": ["Thai League Cup"],
    },

    # ============================================================
    # INDONESIA (2 competitions)
    # ============================================================
    {
        "id": 274,
        "name": "Liga 1",
        "country": "Indonesia",
        "type": "league",
        "tier": 1,
        "aliases": ["Indonesian Liga 1"],
    },
    {
        "id": 275,
        "name": "Liga 2",
        "country": "Indonesia",
        "type": "league",
        "tier": 2,
        "aliases": ["Indonesian Liga 2"],
    },

    # ============================================================
    # MALAYSIA (4 competitions)
    # ============================================================
    {
        "id": 302,
        "name": "Super League",
        "country": "Malaysia",
        "type": "league",
        "tier": 1,
        "aliases": ["Malaysian Super League"],
    },
    {
        "id": 303,
        "name": "Premier League",
        "country": "Malaysia",
        "type": "league",
        "tier": 2,
        "aliases": ["Malaysian Premier League"],
    },
    {
        "id": 304,
        "name": "Malaysia Cup",
        "country": "Malaysia",
        "type": "cup",
        "tier": 1,
        "aliases": ["Piala Malaysia"],
    },
    {
        "id": 305,
        "name": "FA Cup",
        "country": "Malaysia",
        "type": "cup",
        "tier": 1,
        "aliases": ["Malaysian FA Cup", "Piala FA"],
    },

    # ============================================================
    # IRAN (4 competitions)
    # ============================================================
    {
        "id": 290,
        "name": "Persian Gulf Pro League",
        "country": "Iran",
        "type": "league",
        "tier": 1,
        "aliases": ["Iranian Pro League"],
    },
    {
        "id": 291,
        "name": "Azadegan League",
        "country": "Iran",
        "type": "league",
        "tier": 2,
        "aliases": ["Iranian first division"],
    },
    {
        "id": 641,
        "name": "Hazfi Cup",
        "country": "Iran",
        "type": "cup",
        "tier": 1,
        "aliases": ["Iranian Cup"],
    },
    {
        "id": 621,
        "name": "Super Cup",
        "country": "Iran",
        "type": "cup",
        "tier": 1,
        "aliases": ["Iranian Super Cup"],
    },

    # ============================================================
    # SAUDI ARABIA (5 competitions)
    # ============================================================
    {
        "id": 307,
        "name": "Pro League",
        "country": "Saudi-Arabia",
        "type": "league",
        "tier": 1,
        "aliases": ["Saudi Pro League", "Roshn Saudi League"],
    },
    {
        "id": 308,
        "name": "Division 1",
        "country": "Saudi-Arabia",
        "type": "league",
        "tier": 2,
        "aliases": ["Saudi first division"],
    },
    {
        "id": 309,
        "name": "King's Cup",
        "country": "Saudi-Arabia",
        "type": "cup",
        "tier": 1,
        "aliases": ["Saudi King's Cup", "Custodian of the Two Holy Mosques Cup"],
    },
    {
        "id": 670,
        "name": "Crown Prince Cup",
        "country": "Saudi-Arabia",
        "type": "cup",
        "tier": 2,
        "aliases": ["Saudi Crown Prince Cup"],
    },
    {
        "id": 565,
        "name": "Super Cup",
        "country": "Saudi-Arabia",
        "type": "cup",
        "tier": 1,
        "aliases": ["Saudi Super Cup"],
    },

    # ============================================================
    # UAE (3 competitions)
    # ============================================================
    {
        "id": 304,
        "name": "Pro League",
        "country": "United-Arab-Emirates",
        "type": "league",
        "tier": 1,
        "aliases": ["UAE Pro League", "ADNOC Pro League"],
    },
    {
        "id": 673,
        "name": "League Cup",
        "country": "United-Arab-Emirates",
        "type": "cup",
        "tier": 2,
        "aliases": ["UAE League Cup"],
    },
    {
        "id": 566,
        "name": "Super Cup",
        "country": "United-Arab-Emirates",
        "type": "cup",
        "tier": 1,
        "aliases": ["UAE Super Cup"],
    },

    # ============================================================
    # QATAR (6 competitions)
    # ============================================================
    {
        "id": 312,
        "name": "Stars League",
        "country": "Qatar",
        "type": "league",
        "tier": 1,
        "aliases": ["Qatar Stars League", "QSL"],
    },
    {
        "id": 313,
        "name": "Second Division",
        "country": "Qatar",
        "type": "league",
        "tier": 2,
        "aliases": ["Qatari second division"],
    },
    {
        "id": 642,
        "name": "Qatar Cup",
        "country": "Qatar",
        "type": "cup",
        "tier": 1,
        "aliases": ["Amir Cup"],
    },
    {
        "id": 643,
        "name": "Emir Cup",
        "country": "Qatar",
        "type": "cup",
        "tier": 1,
        "aliases": ["Sheikh Jassim Cup"],
    },
    {
        "id": 675,
        "name": "QSL Cup",
        "country": "Qatar",
        "type": "cup",
        "tier": 2,
        "aliases": ["Qatar Stars League Cup"],
    },
    {
        "id": 676,
        "name": "QFA Cup",
        "country": "Qatar",
        "type": "cup",
        "tier": 2,
        "aliases": ["Qatar Football Association Cup"],
    },

    # ============================================================
    # KUWAIT (4 competitions)
    # ============================================================
    {
        "id": 314,
        "name": "Premier League",
        "country": "Kuwait",
        "type": "league",
        "tier": 1,
        "aliases": ["Kuwaiti Premier League"],
    },
    {
        "id": 644,
        "name": "Crown Prince Cup",
        "country": "Kuwait",
        "type": "cup",
        "tier": 1,
        "aliases": ["Kuwaiti Crown Prince Cup"],
    },
    {
        "id": 645,
        "name": "Emir Cup",
        "country": "Kuwait",
        "type": "cup",
        "tier": 1,
        "aliases": ["Kuwaiti Emir Cup"],
    },
    {
        "id": 568,
        "name": "Super Cup",
        "country": "Kuwait",
        "type": "cup",
        "tier": 1,
        "aliases": ["Kuwaiti Super Cup"],
    },

    # ============================================================
    # KAZAKHSTAN (4 competitions)
    # ============================================================
    {
        "id": 388,
        "name": "Premier League",
        "country": "Kazakhstan",
        "type": "league",
        "tier": 1,
        "aliases": ["Kazakhstani Premier League"],
    },
    {
        "id": 389,
        "name": "1. Division",
        "country": "Kazakhstan",
        "type": "league",
        "tier": 2,
        "aliases": ["Kazakhstani first division"],
    },
    {
        "id": 390,
        "name": "Cup",
        "country": "Kazakhstan",
        "type": "cup",
        "tier": 1,
        "aliases": ["Kazakhstan Cup"],
    },
    {
        "id": 615,
        "name": "Super Cup",
        "country": "Kazakhstan",
        "type": "cup",
        "tier": 1,
        "aliases": ["Kazakhstani Super Cup"],
    },

    # ============================================================
    # EGYPT (4 competitions)
    # ============================================================
    {
        "id": 233,
        "name": "Premier League",
        "country": "Egypt",
        "type": "league",
        "tier": 1,
        "aliases": ["Egyptian Premier League"],
    },
    {
        "id": 234,
        "name": "Second League",
        "country": "Egypt",
        "type": "league",
        "tier": 2,
        "aliases": ["Egyptian second division"],
    },
    {
        "id": 636,
        "name": "Cup",
        "country": "Egypt",
        "type": "cup",
        "tier": 1,
        "aliases": ["Egyptian Cup"],
    },
    {
        "id": 637,
        "name": "League Cup",
        "country": "Egypt",
        "type": "cup",
        "tier": 2,
        "aliases": ["Egyptian League Cup"],
    },

    # ============================================================
    # ALGERIA (5 competitions)
    # ============================================================
    {
        "id": 187,
        "name": "Ligue 1",
        "country": "Algeria",
        "type": "league",
        "tier": 1,
        "aliases": ["Algerian Ligue 1"],
    },
    {
        "id": 631,
        "name": "Ligue 2",
        "country": "Algeria",
        "type": "league",
        "tier": 2,
        "aliases": ["Algerian Ligue 2"],
    },
    {
        "id": 632,
        "name": "Coupe Nationale",
        "country": "Algeria",
        "type": "cup",
        "tier": 1,
        "aliases": ["Algerian Cup"],
    },
    {
        "id": 633,
        "name": "Coupe de la Ligue",
        "country": "Algeria",
        "type": "cup",
        "tier": 2,
        "aliases": ["Algerian League Cup"],
    },
    {
        "id": 559,
        "name": "Super Cup",
        "country": "Algeria",
        "type": "cup",
        "tier": 1,
        "aliases": ["Algerian Super Cup"],
    },

    # ============================================================
    # MOROCCO (3 competitions)
    # ============================================================
    {
        "id": 200,
        "name": "Botola Pro",
        "country": "Morocco",
        "type": "league",
        "tier": 1,
        "aliases": ["Moroccan Pro League"],
    },
    {
        "id": 201,
        "name": "Botola 2",
        "country": "Morocco",
        "type": "league",
        "tier": 2,
        "aliases": ["Moroccan second division"],
    },
    {
        "id": 638,
        "name": "Cup",
        "country": "Morocco",
        "type": "cup",
        "tier": 1,
        "aliases": ["Moroccan Throne Cup", "Coupe du Trône"],
    },

    # ============================================================
    # TUNISIA (4 competitions)
    # ============================================================
    {
        "id": 202,
        "name": "Ligue 1",
        "country": "Tunisia",
        "type": "league",
        "tier": 1,
        "aliases": ["Tunisian Ligue 1"],
    },
    {
        "id": 639,
        "name": "Ligue 2",
        "country": "Tunisia",
        "type": "league",
        "tier": 2,
        "aliases": ["Tunisian Ligue 2"],
    },
    {
        "id": 640,
        "name": "Cup",
        "country": "Tunisia",
        "type": "cup",
        "tier": 1,
        "aliases": ["Tunisian Cup"],
    },
    {
        "id": 560,
        "name": "Super Cup",
        "country": "Tunisia",
        "type": "cup",
        "tier": 1,
        "aliases": ["Tunisian Super Cup"],
    },

    # ============================================================
    # SOUTH AFRICA (3 competitions)
    # ============================================================
    {
        "id": 288,
        "name": "Premier Soccer League",
        "country": "South-Africa",
        "type": "league",
        "tier": 1,
        "aliases": ["South African PSL", "DStv Premiership"],
    },
    {
        "id": 680,
        "name": "League Cup",
        "country": "South-Africa",
        "type": "cup",
        "tier": 2,
        "aliases": ["MTN 8", "South African League Cup"],
    },
    {
        "id": 681,
        "name": "8 Cup",
        "country": "South-Africa",
        "type": "cup",
        "tier": 2,
        "aliases": ["Nedbank Cup"],
    },

    # ============================================================
    # INTERNATIONAL - UEFA
    # ============================================================
    {
        "id": 2,
        "name": "UEFA Champions League",
        "country": "World",
        "type": "cup",
        "tier": 1,
        "aliases": ["Champions League", "UCL", "CL", "European Cup"],
    },
    {
        "id": 3,
        "name": "UEFA Europa League",
        "country": "World",
        "type": "cup",
        "tier": 1,
        "aliases": ["Europa League", "UEL", "EL"],
    },
    {
        "id": 848,
        "name": "UEFA Europa Conference League",
        "country": "World",
        "type": "cup",
        "tier": 2,
        "aliases": ["Conference League", "UECL", "Europa Conference"],
    },
    {
        "id": 4,
        "name": "Euro Championship",
        "country": "World",
        "type": "cup",
        "tier": 1,
        "aliases": ["European Championship", "Euros", "UEFA Euro", "Euro"],
    },
    {
        "id": 960,
        "name": "Euro Championship - Qualification",
        "country": "World",
        "type": "qualification",
        "tier": 1,
        "aliases": ["Euro Qualifiers", "European Championship Qualification"],
    },
    {
        "id": 5,
        "name": "UEFA Nations League",
        "country": "World",
        "type": "cup",
        "tier": 1,
        "aliases": ["Nations League", "UNL"],
    },
    {
        "id": 531,
        "name": "UEFA Super Cup",
        "country": "World",
        "type": "cup",
        "tier": 1,
        "aliases": ["European Super Cup"],
    },
    {
        "id": 772,
        "name": "UEFA Youth League",
        "country": "World",
        "type": "cup",
        "tier": 2,
        "aliases": ["UYL"],
    },
    {
        "id": 747,
        "name": "UEFA Champions League Women",
        "country": "World",
        "type": "cup",
        "tier": 1,
        "aliases": ["Women's Champions League", "UWCL"],
    },
    {
        "id": 883,
        "name": "UEFA Championship - Women",
        "country": "World",
        "type": "cup",
        "tier": 1,
        "aliases": ["Women's Euro", "UEFA Women's Championship"],
    },
    {
        "id": 884,
        "name": "UEFA Championship - Women - Qualification",
        "country": "World",
        "type": "qualification",
        "tier": 1,
        "aliases": ["Women's Euro Qualifiers"],
    },
    {
        "id": 885,
        "name": "UEFA Nations League - Women",
        "country": "World",
        "type": "cup",
        "tier": 1,
        "aliases": ["Women's Nations League"],
    },
    {
        "id": 886,
        "name": "UEFA Europa Cup - Women",
        "country": "World",
        "type": "cup",
        "tier": 2,
        "aliases": ["Women's Europa Cup"],
    },

    # ============================================================
    # INTERNATIONAL - FIFA
    # ============================================================
    {
        "id": 1,
        "name": "World Cup",
        "country": "World",
        "type": "cup",
        "tier": 1,
        "aliases": ["FIFA World Cup", "WC"],
    },
    {
        "id": 32,
        "name": "World Cup - Qualification Europe",
        "country": "World",
        "type": "qualification",
        "tier": 1,
        "aliases": ["European World Cup Qualifiers", "WCQ Europe"],
    },
    {
        "id": 29,
        "name": "World Cup - Qualification South America",
        "country": "World",
        "type": "qualification",
        "tier": 1,
        "aliases": ["CONMEBOL World Cup Qualifiers", "WCQ South America"],
    },
    {
        "id": 30,
        "name": "World Cup - Qualification CONCACAF",
        "country": "World",
        "type": "qualification",
        "tier": 1,
        "aliases": ["CONCACAF World Cup Qualifiers", "WCQ CONCACAF"],
    },
    {
        "id": 31,
        "name": "World Cup - Qualification Africa",
        "country": "World",
        "type": "qualification",
        "tier": 1,
        "aliases": ["CAF World Cup Qualifiers", "WCQ Africa"],
    },
    {
        "id": 33,
        "name": "World Cup - Qualification Asia",
        "country": "World",
        "type": "qualification",
        "tier": 1,
        "aliases": ["AFC World Cup Qualifiers", "WCQ Asia"],
    },
    {
        "id": 34,
        "name": "World Cup - Qualification Oceania",
        "country": "World",
        "type": "qualification",
        "tier": 1,
        "aliases": ["OFC World Cup Qualifiers", "WCQ Oceania"],
    },
    {
        "id": 35,
        "name": "World Cup - Qualification Intercontinental Play-offs",
        "country": "World",
        "type": "qualification",
        "tier": 1,
        "aliases": ["World Cup Play-offs", "Intercontinental Play-offs"],
    },
    {
        "id": 72,
        "name": "World Cup - Women",
        "country": "World",
        "type": "cup",
        "tier": 1,
        "aliases": ["FIFA Women's World Cup", "WWC"],
    },
    {
        "id": 790,
        "name": "World Cup - Women - Qualification Europe",
        "country": "World",
        "type": "qualification",
        "tier": 1,
        "aliases": ["Women's World Cup Qualifiers Europe"],
    },
    {
        "id": 791,
        "name": "World Cup - Women - Qualification Concacaf",
        "country": "World",
        "type": "qualification",
        "tier": 1,
        "aliases": ["Women's World Cup Qualifiers CONCACAF"],
    },
    {
        "id": 776,
        "name": "World Cup - U20",
        "country": "World",
        "type": "cup",
        "tier": 2,
        "aliases": ["FIFA U-20 World Cup"],
    },
    {
        "id": 777,
        "name": "World Cup - U17",
        "country": "World",
        "type": "cup",
        "tier": 2,
        "aliases": ["FIFA U-17 World Cup"],
    },
    {
        "id": 778,
        "name": "World Cup - U20 - Women",
        "country": "World",
        "type": "cup",
        "tier": 2,
        "aliases": ["FIFA U-20 Women's World Cup"],
    },
    {
        "id": 779,
        "name": "World Cup - U17 - Women",
        "country": "World",
        "type": "cup",
        "tier": 2,
        "aliases": ["FIFA U-17 Women's World Cup"],
    },
    {
        "id": 15,
        "name": "FIFA Club World Cup",
        "country": "World",
        "type": "cup",
        "tier": 1,
        "aliases": ["Club World Cup", "CWC"],
    },
    {
        "id": 958,
        "name": "FIFA Club World Cup - Play-In",
        "country": "World",
        "type": "cup",
        "tier": 2,
        "aliases": ["Club World Cup Play-In"],
    },
    {
        "id": 959,
        "name": "FIFA Intercontinental Cup",
        "country": "World",
        "type": "cup",
        "tier": 1,
        "aliases": ["Intercontinental Cup"],
    },
    {
        "id": 514,
        "name": "Confederations Cup",
        "country": "World",
        "type": "cup",
        "tier": 1,
        "aliases": ["FIFA Confederations Cup"],
    },

    # ============================================================
    # INTERNATIONAL - CONMEBOL
    # ============================================================
    {
        "id": 9,
        "name": "Copa America",
        "country": "World",
        "type": "cup",
        "tier": 1,
        "aliases": ["CONMEBOL Copa America"],
    },
    {
        "id": 13,
        "name": "CONMEBOL Libertadores",
        "country": "World",
        "type": "cup",
        "tier": 1,
        "aliases": ["Copa Libertadores", "Libertadores"],
    },
    {
        "id": 14,
        "name": "CONMEBOL Sudamericana",
        "country": "World",
        "type": "cup",
        "tier": 1,
        "aliases": ["Copa Sudamericana", "Sudamericana"],
    },

    # ============================================================
    # INTERNATIONAL - CONCACAF
    # ============================================================
    {
        "id": 16,
        "name": "CONCACAF Champions League",
        "country": "World",
        "type": "cup",
        "tier": 1,
        "aliases": ["CONCACAF Champions Cup", "Concachampions"],
    },
    {
        "id": 17,
        "name": "CONCACAF League",
        "country": "World",
        "type": "cup",
        "tier": 2,
        "aliases": ["CONCACAF Central American Cup"],
    },
    {
        "id": 22,
        "name": "CONCACAF Gold Cup",
        "country": "World",
        "type": "cup",
        "tier": 1,
        "aliases": ["Gold Cup"],
    },
    {
        "id": 903,
        "name": "CONCACAF Gold Cup - Qualification",
        "country": "World",
        "type": "qualification",
        "tier": 1,
        "aliases": ["Gold Cup Qualifiers"],
    },
    {
        "id": 18,
        "name": "CONCACAF Nations League",
        "country": "World",
        "type": "cup",
        "tier": 1,
        "aliases": ["CNL"],
    },
    {
        "id": 904,
        "name": "CONCACAF Nations League - Qualification",
        "country": "World",
        "type": "qualification",
        "tier": 1,
        "aliases": ["CNL Qualifiers"],
    },
    {
        "id": 905,
        "name": "CONCACAF Gold Cup - Women",
        "country": "World",
        "type": "cup",
        "tier": 1,
        "aliases": ["Women's Gold Cup"],
    },
    {
        "id": 906,
        "name": "CONCACAF Gold Cup - Qualification - Women",
        "country": "World",
        "type": "qualification",
        "tier": 1,
        "aliases": ["Women's Gold Cup Qualifiers"],
    },

    # ============================================================
    # INTERNATIONAL - CAF (Africa)
    # ============================================================
    {
        "id": 6,
        "name": "Africa Cup of Nations",
        "country": "World",
        "type": "cup",
        "tier": 1,
        "aliases": ["AFCON", "African Cup of Nations", "CAN"],
    },
    {
        "id": 36,
        "name": "Africa Cup of Nations - Qualification",
        "country": "World",
        "type": "qualification",
        "tier": 1,
        "aliases": ["AFCON Qualifiers"],
    },
    {
        "id": 746,
        "name": "Africa Cup of Nations - Women",
        "country": "World",
        "type": "cup",
        "tier": 1,
        "aliases": ["Women's AFCON"],
    },
    {
        "id": 12,
        "name": "CAF Champions League",
        "country": "World",
        "type": "cup",
        "tier": 1,
        "aliases": ["African Champions League"],
    },
    {
        "id": 20,
        "name": "CAF Confederation Cup",
        "country": "World",
        "type": "cup",
        "tier": 1,
        "aliases": ["African Confederation Cup"],
    },
    {
        "id": 530,
        "name": "CAF Super Cup",
        "country": "World",
        "type": "cup",
        "tier": 1,
        "aliases": ["African Super Cup"],
    },
    {
        "id": 907,
        "name": "CAF Women's Champions League",
        "country": "World",
        "type": "cup",
        "tier": 1,
        "aliases": ["African Women's Champions League"],
    },

    # ============================================================
    # INTERNATIONAL - AFC (Asia)
    # ============================================================
    {
        "id": 7,
        "name": "Asian Cup",
        "country": "World",
        "type": "cup",
        "tier": 1,
        "aliases": ["AFC Asian Cup"],
    },
    {
        "id": 37,
        "name": "Asian Cup - Qualification",
        "country": "World",
        "type": "qualification",
        "tier": 1,
        "aliases": ["Asian Cup Qualifiers"],
    },
    {
        "id": 748,
        "name": "Asian Cup Women",
        "country": "World",
        "type": "cup",
        "tier": 1,
        "aliases": ["AFC Women's Asian Cup"],
    },
    {
        "id": 749,
        "name": "Asian Cup Women - Qualification",
        "country": "World",
        "type": "qualification",
        "tier": 1,
        "aliases": ["Women's Asian Cup Qualifiers"],
    },
    {
        "id": 17,
        "name": "AFC Champions League Elite",
        "country": "World",
        "type": "cup",
        "tier": 1,
        "aliases": ["AFC Champions League", "ACL"],
    },
    {
        "id": 956,
        "name": "AFC Champions League Two",
        "country": "World",
        "type": "cup",
        "tier": 2,
        "aliases": ["AFC Challenge League", "ACL 2"],
    },
    {
        "id": 957,
        "name": "AFC Challenge Cup",
        "country": "World",
        "type": "cup",
        "tier": 2,
        "aliases": ["AFC Challenge"],
    },
    {
        "id": 955,
        "name": "AFC Challenge League",
        "country": "World",
        "type": "cup",
        "tier": 2,
        "aliases": [],
    },

    # ============================================================
    # INTERNATIONAL - OTHER
    # ============================================================
    {
        "id": 667,
        "name": "Arab Cup",
        "country": "World",
        "type": "cup",
        "tier": 1,
        "aliases": ["FIFA Arab Cup"],
    },
    {
        "id": 668,
        "name": "Arab Club Champions Cup",
        "country": "World",
        "type": "cup",
        "tier": 1,
        "aliases": ["UAFA Club Cup"],
    },
    {
        "id": 10,
        "name": "Friendlies",
        "country": "World",
        "type": "friendly",
        "tier": 3,
        "aliases": ["International Friendlies"],
    },
    {
        "id": 667,
        "name": "Friendlies Clubs",
        "country": "World",
        "type": "friendly",
        "tier": 3,
        "aliases": ["Club Friendlies"],
    },
    {
        "id": 669,
        "name": "International Champions Cup",
        "country": "World",
        "type": "friendly",
        "tier": 2,
        "aliases": ["ICC"],
    },
    {
        "id": 670,
        "name": "International Champions Cup - Women",
        "country": "World",
        "type": "friendly",
        "tier": 2,
        "aliases": ["Women's ICC"],
    },
    {
        "id": 671,
        "name": "Emirates Cup",
        "country": "World",
        "type": "friendly",
        "tier": 3,
        "aliases": [],
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
    # European
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
    "irish": "ireland",
    "belarusian": "belarus",
    "ukrainian": "ukraine",
    "russian": "russia",
    "polish": "poland",
    "czech": "czech-republic",
    "romanian": "romania",
    "hungarian": "hungary",
    "bulgarian": "bulgaria",
    "austrian": "austria",
    "swiss": "switzerland",
    "danish": "denmark",
    "norwegian": "norway",
    "swedish": "sweden",
    "finnish": "finland",
    "croatian": "croatia",
    "serbian": "serbia",
    "slovenian": "slovenia",
    "slovakian": "slovakia",
    "slovak": "slovakia",
    "cypriot": "cyprus",
    "estonian": "estonia",
    "lithuanian": "lithuania",
    "georgian": "georgia",
    "armenian": "armenia",
    "azerbaijani": "azerbaijan",
    "moldovan": "moldova",
    "israeli": "israel",
    "albanian": "albania",
    "bosnian": "bosnia",
    "icelandic": "iceland",
    "andorran": "andorra",
    # South American
    "brazilian": "brazil",
    "argentine": "argentina",
    "argentinian": "argentina",
    "chilean": "chile",
    "colombian": "colombia",
    "peruvian": "peru",
    "ecuadorian": "ecuador",
    "uruguayan": "uruguay",
    "paraguayan": "paraguay",
    "bolivian": "bolivia",
    "venezuelan": "venezuela",
    # North/Central American
    "american": "usa",
    "us": "usa",
    "mexican": "mexico",
    "canadian": "canada",
    "costa rican": "costa-rica",
    "honduran": "honduras",
    # Asian
    "japanese": "japan",
    "korean": "south-korea",
    "south korean": "south-korea",
    "chinese": "china",
    "australian": "australia",
    "thai": "thailand",
    "indonesian": "indonesia",
    "malaysian": "malaysia",
    "iranian": "iran",
    "saudi": "saudi-arabia",
    "saudi arabian": "saudi-arabia",
    "emirati": "united-arab-emirates",
    "uae": "united-arab-emirates",
    "qatari": "qatar",
    "kuwaiti": "kuwait",
    "kazakhstani": "kazakhstan",
    "kazakh": "kazakhstan",
    # African
    "egyptian": "egypt",
    "algerian": "algeria",
    "moroccan": "morocco",
    "tunisian": "tunisia",
    "south african": "south-africa",
    # Northern Ireland
    "northern irish": "northern-ireland",
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
    6. Generic country: "Spanish league" → All Spanish leagues

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

        >>> resolve_league_query("Spanish league")
        [{"id": 140, ...}, {"id": 141, ...}, {"id": 143, ...}, ...]
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
        league for league in LEAGUE_REFERENCE
        if league.get("tier") == 1 and league["country"] in
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
    uefa = [league for league in LEAGUE_REFERENCE if "UEFA" in league["name"] or league["name"] in ["Champions League", "Europa League"]]
    for league in uefa[:10]:
        aliases = ", ".join(league.get("aliases", [])[:3])
        lines.append(f"| {league['id']} | {league['name']} | {aliases} |")

    lines.extend([
        "",
        "### DISAMBIGUATION (Same Name, Different Countries)",
        "| League Name | Country | ID |",
        "|-------------|---------|-----|",
        "| Premier League | England | 39 (default) |",
        "| Premier League | Belarus | 117 |",
        "| Premier League | Ukraine | 333 |",
        "| Premier League | Russia | 235 |",
        "| Serie A | Italy | 135 (default) |",
        "| Serie A | Brazil | 71 |",
        "| Ligue 1 | France | 61 |",
        "| Ligue 1 | Algeria | 187 |",
        "| Ligue 1 | Tunisia | 202 |",
        "",
        "### RESOLUTION RULES",
        "1. 'Spanish LaLiga' or 'La Liga' → ID 140",
        "2. 'EPL' or 'English Premier League' → ID 39",
        "3. 'Belarus league' → ALL Belarus league IDs",
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
        [140, 141, 143, 556, 142, 891]  # La Liga, Segunda, Copa del Rey, etc.
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
