"""Tests for sipap_common.types.odds module."""

from datetime import UTC, datetime

from sipap_common.types.odds import OddsData


class TestOddsData:
    """Tests for OddsData TypedDict."""

    def test_odds_data_structure(self):
        """Verify OddsData has correct structure."""
        now = datetime.now(UTC)
        odds: OddsData = {
            "bookmaker": "Bet365",
            "market": "Match Winner",
            "outcome": "Home",
            "odds": 2.50,
            "timestamp": now
        }

        assert odds["bookmaker"] == "Bet365"
        assert odds["market"] == "Match Winner"
        assert odds["outcome"] == "Home"
        assert odds["odds"] == 2.50
        assert odds["timestamp"] == now

    def test_odds_data_required_fields(self):
        """Verify OddsData type annotations."""
        from sipap_common.types.odds import OddsData
        annotations = OddsData.__annotations__

        expected_fields = ["bookmaker", "market", "outcome", "odds", "timestamp"]

        for field in expected_fields:
            assert field in annotations

    def test_odds_data_different_bookmakers(self):
        """Verify OddsData works with different bookmakers."""
        bookmakers = ["Bet365", "William Hill", "Pinnacle", "Betfair"]

        for bookmaker in bookmakers:
            odds: OddsData = {
                "bookmaker": bookmaker,
                "market": "Match Winner",
                "outcome": "Home",
                "odds": 2.00,
                "timestamp": datetime.now(UTC)
            }
            assert odds["bookmaker"] == bookmaker

    def test_odds_data_different_odds_formats(self):
        """Verify OddsData accepts various odds values."""
        odds_values = [1.01, 1.5, 2.0, 3.5, 10.0, 50.0]

        for odds_value in odds_values:
            odds: OddsData = {
                "bookmaker": "Bet365",
                "market": "Match Winner",
                "outcome": "Home",
                "odds": odds_value,
                "timestamp": datetime.now(UTC)
            }
            assert odds["odds"] == odds_value

    def test_odds_data_different_markets(self):
        """Verify OddsData works with different market types."""
        markets = [
            ("Match Winner", "Home"),
            ("Over/Under 2.5", "Over"),
            ("Both Teams to Score", "Yes"),
            ("Asian Handicap -1.5", "Home")
        ]

        for market, outcome in markets:
            odds: OddsData = {
                "bookmaker": "Bet365",
                "market": market,
                "outcome": outcome,
                "odds": 2.00,
                "timestamp": datetime.now(UTC)
            }
            assert odds["market"] == market
            assert odds["outcome"] == outcome
