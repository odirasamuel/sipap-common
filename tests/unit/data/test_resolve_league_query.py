"""Matching a league named in a user's message.

The matcher used to look for any alias as a raw substring and return the
first hit, so "plays" matched the alias "PL" and "bonus" matched "us".
It now matches whole words, prefers the most specific name, and uses a
country named in the message to choose between leagues that share a name.
"""

import pytest

from sipap_common.data.league_reference import LEAGUE_REFERENCE, resolve_league_query


def ids(query: str) -> list[int]:
    return [league["id"] for league in resolve_league_query(query)]


@pytest.mark.parametrize(
    ("query", "league_id"),
    [
        ("Who plays in La Liga", 140),
        ("please predict Bundesliga", 78),
        ("Scottish Championship", 180),
        ("Austrian Bundesliga", 218),
        ("Premier League", 39),
        ("EPL", 39),
        ("PL picks", 39),
        ("Serie A", 135),
        ("Brazil Serie A", 71),
        ("Championship", 40),
        ("Russian Premier League", 235),
        ("Premier League Egypt", 233),
    ],
)
def test_resolves_to_the_league_meant(query: str, league_id: int) -> None:
    assert ids(query) == [league_id]


def test_a_country_in_the_message_overrides_a_same_named_league_elsewhere() -> None:
    result = resolve_league_query("UAE Pro League")
    assert result
    assert {league["country"] for league in result} == {"United Arab Emirates"}


@pytest.mark.parametrize("query", ["bonus tips", "plays well", "use caution", "focus on value"])
def test_ordinary_words_do_not_name_a_league_or_country(query: str) -> None:
    assert ids(query) == []


def test_a_country_alone_gives_that_countrys_leagues() -> None:
    assert 140 in ids("Spain")
    assert 253 in ids("games in the USA today")
    assert 253 in ids("US fixtures")


def test_every_league_is_found_by_its_own_name_with_its_country() -> None:
    missed = []
    for league in LEAGUE_REFERENCE:
        query = f"{league['country']} {league['name']}"
        if league["id"] not in ids(query):
            missed.append((league["id"], query, ids(query)[:3]))
    assert missed == []


def test_club_world_cup_is_not_world_cup_qualifying() -> None:
    assert ids("Club World Cup") == [15]
    assert ids("FIFA Club World Cup") == [15]
    assert ids("World Cup - Qualification Europe") == [32]


def test_every_league_name_resolves_to_a_league_with_that_name() -> None:
    wrong = []
    for league in LEAGUE_REFERENCE:
        result = resolve_league_query(league["name"])
        # names are compared without case: "2. Liga" and "2. liga" are different countries' leagues
        if not result or result[0]["name"].lower() != league["name"].lower():
            wrong.append((league["name"], [r["name"] for r in result][:2]))
    assert wrong == []


def test_every_alias_resolves_to_its_own_league() -> None:
    wrong = []
    for league in LEAGUE_REFERENCE:
        for alias in league.get("aliases") or []:
            if ids(alias) != [league["id"]]:
                wrong.append((alias, league["id"], ids(alias)))
    assert wrong == []
