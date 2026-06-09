"""Type definitions for SIPAP platform."""

from sipap_common.types.common import Sport
from sipap_common.types.match import Match, TeamReference
from sipap_common.types.odds import OddsData
from sipap_common.types.prediction import Prediction

__all__ = [
    "Sport",
    "Match",
    "TeamReference",
    "Prediction",
    "OddsData",
]
