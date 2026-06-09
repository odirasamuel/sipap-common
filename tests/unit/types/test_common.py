"""Tests for sipap_common.types.common module."""

import pytest

from sipap_common.types.common import Sport


class TestSport:
    """Tests for Sport enum."""

    def test_sport_enum_values(self):
        """Verify Sport enum has expected values."""
        assert Sport.SOCCER == "soccer"
        assert Sport.NBA == "nba"
        assert Sport.NFL == "nfl"
        assert Sport.TENNIS == "tennis"

    def test_sport_enum_members(self):
        """Verify Sport enum has all expected members."""
        expected_members = {"SOCCER", "NBA", "NFL", "TENNIS"}
        actual_members = {member.name for member in Sport}
        assert actual_members == expected_members

    def test_sport_string_comparison(self):
        """Verify Sport enum values can be compared with strings."""
        assert Sport.SOCCER == "soccer"
        assert Sport.NBA == "nba"

    def test_sport_value_access(self):
        """Verify Sport enum value property."""
        assert Sport.SOCCER.value == "soccer"
        assert Sport.NBA.value == "nba"

    def test_sport_from_string(self):
        """Verify Sport enum can be created from string."""
        sport = Sport("soccer")
        assert sport == Sport.SOCCER

    def test_sport_invalid_value_raises_error(self):
        """Verify invalid sport value raises ValueError."""
        with pytest.raises(ValueError, match="'invalid' is not a valid Sport"):
            Sport("invalid")

    def test_sport_enum_iteration(self):
        """Verify Sport enum can be iterated."""
        sports = list(Sport)
        assert len(sports) == 4
        assert Sport.SOCCER in sports
        assert Sport.NBA in sports
        assert Sport.NFL in sports
        assert Sport.TENNIS in sports
