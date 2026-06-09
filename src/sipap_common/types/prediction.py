"""
Prediction-related type definitions.

This module defines TypedDict classes for prediction data structures.
"""

from datetime import datetime
from typing import TypedDict


class Prediction(TypedDict):
    """
    Prediction for a specific match and market.

    Represents an AI-generated prediction with probability assessment,
    confidence scoring, and explainable reasoning.

    Attributes:
        id: Unique identifier for the prediction
        match_id: Reference to the match being predicted
        market: Betting market type (e.g., "Match Winner", "Over/Under 2.5")
        outcome: Predicted outcome (e.g., "Home", "Over", "Yes")
        probability: Estimated probability (0.0 to 1.0)
        confidence: Confidence score (0.0 to 10.0)
        reasoning: Human-readable explanation of the prediction
        created_at: Timestamp when prediction was generated

    Example:
        >>> from datetime import datetime, UTC
        >>> prediction: Prediction = {
        ...     "id": "pred-123",
        ...     "match_id": "match-456",
        ...     "market": "Match Winner",
        ...     "outcome": "Home",
        ...     "probability": 0.65,
        ...     "confidence": 7.5,
        ...     "reasoning": "Home team has won 4 of last 5 matches",
        ...     "created_at": datetime.now(UTC)
        ... }
    """

    id: str
    match_id: str
    market: str
    outcome: str
    probability: float
    confidence: float
    reasoning: str
    created_at: datetime
