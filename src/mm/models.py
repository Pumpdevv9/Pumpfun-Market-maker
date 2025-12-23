from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class Quote:
    bid_px: float
    bid_sz: float
    ask_px: float
    ask_sz: float
