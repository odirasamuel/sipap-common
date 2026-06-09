"""Tests for sipap_common.types.match module."""

from datetime import UTC, datetime

from sipap_common.types.common import Sport
from sipap_common.types.match import Match, TeamReference


class TestTeamReference:
    """Tests for TeamReference TypedDict."""

    def test_team_reference_structure(self):
        """Verify TeamReference has correct structure."""
        team: TeamReference = {
            "id": "team-123",
            "name": "Arsenal"
        }
        assert team["id"] == "team-123"
        assert team["name"] == "Arsenal"

    def test_team_reference_required_fields(self):
        """Verify TeamReference type annotations."""
        # This test validates that the type exists and has the right structure
        # Actual type checking is done by mypy at static analysis time
        from sipap_common.types.match import TeamReference
        annotations = TeamReference.__annotations__
        assert "id" in annotations
        assert "name" in annotations
        assert annotations["id"] is str
        assert annotations["name"] is str


class TestMatch:
    """Tests for Match TypedDict."""

    def test_match_structure(self):
        """Verify Match has correct structure."""
        now = datetime.now(UTC)
        match: Match = {
            "id": "match-456",
            "sport": Sport.SOCCER,
            "league": "Premier League",
            "season": "2025-2026",
            "home_team": {"id": "team-1", "name": "Arsenal"},
            "away_team": {"id": "team-2", "name": "Chelsea"},
            "scheduled_at": now,
            "status": "scheduled"
        }

        assert match["id"] == "match-456"
        assert match["sport"] == Sport.SOCCER
        assert match["league"] == "Premier League"
        assert match["season"] == "2025-2026"
        assert match["home_team"]["id"] == "team-1"
        assert match["away_team"]["id"] == "team-2"
        assert match["scheduled_at"] == now
        assert match["status"] == "scheduled"

    def test_match_required_fields(self):
        """Verify Match type annotations."""
        from sipap_common.types.match import Match
        annotations = Match.__annotations__

        expected_fields = [
            "id", "sport", "league", "season",
            "home_team", "away_team", "scheduled_at", "status"
        ]

        for field in expected_fields:
            assert field in annotations

    def test_match_status_values(self):
        """Verify Match supports different status values."""
        base_match_data = {
            "id": "match-789",
            "sport": Sport.SOCCER,
            "league": "Premier League",
            "season": "2025-2026",
            "home_team": {"id": "team-1", "name": "Arsenal"},
            "away_team": {"id": "team-2", "name": "Chelsea"},
            "scheduled_at": datetime.now(UTC),
        }

        for status in ["scheduled", "live", "completed", "postponed"]:
            match: Match = {**base_match_data, "status": status}  # type: ignore
            assert match["status"] == status

    def test_match_with_different_sports(self):
        """Verify Match works with different sports."""
        for sport in [Sport.SOCCER, Sport.NBA, Sport.NFL, Sport.TENNIS]:
            match: Match = {
                "id": f"match-{sport.value}",
                "sport": sport,
                "league": "Test League",
                "season": "2025-2026",
                "home_team": {"id": "team-1", "name": "Team 1"},
                "away_team": {"id": "team-2", "name": "Team 2"},
                "scheduled_at": datetime.now(UTC),
                "status": "scheduled"
            }
            assert match["sport"] == sport
