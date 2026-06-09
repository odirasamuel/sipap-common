"""Tests for sipap_common.types.prediction module."""

from datetime import UTC, datetime

from sipap_common.types.prediction import Prediction


class TestPrediction:
    """Tests for Prediction TypedDict."""

    def test_prediction_structure(self):
        """Verify Prediction has correct structure."""
        now = datetime.now(UTC)
        prediction: Prediction = {
            "id": "pred-123",
            "match_id": "match-456",
            "market": "Match Winner",
            "outcome": "Home",
            "probability": 0.65,
            "confidence": 7.5,
            "reasoning": "Home team has strong form",
            "created_at": now
        }

        assert prediction["id"] == "pred-123"
        assert prediction["match_id"] == "match-456"
        assert prediction["market"] == "Match Winner"
        assert prediction["outcome"] == "Home"
        assert prediction["probability"] == 0.65
        assert prediction["confidence"] == 7.5
        assert prediction["reasoning"] == "Home team has strong form"
        assert prediction["created_at"] == now

    def test_prediction_required_fields(self):
        """Verify Prediction type annotations."""
        from sipap_common.types.prediction import Prediction
        annotations = Prediction.__annotations__

        expected_fields = [
            "id", "match_id", "market", "outcome",
            "probability", "confidence", "reasoning", "created_at"
        ]

        for field in expected_fields:
            assert field in annotations

    def test_prediction_probability_range(self):
        """Verify Prediction accepts probability values between 0 and 1."""
        for prob in [0.0, 0.25, 0.5, 0.75, 1.0]:
            prediction: Prediction = {
                "id": "pred-1",
                "match_id": "match-1",
                "market": "Test",
                "outcome": "Test",
                "probability": prob,
                "confidence": 5.0,
                "reasoning": "Test",
                "created_at": datetime.now(UTC)
            }
            assert prediction["probability"] == prob

    def test_prediction_different_markets(self):
        """Verify Prediction works with different market types."""
        markets = ["Match Winner", "Over/Under 2.5", "Both Teams to Score", "Asian Handicap"]

        for market in markets:
            prediction: Prediction = {
                "id": f"pred-{market}",
                "match_id": "match-1",
                "market": market,
                "outcome": "Yes",
                "probability": 0.6,
                "confidence": 6.0,
                "reasoning": f"Prediction for {market}",
                "created_at": datetime.now(UTC)
            }
            assert prediction["market"] == market
