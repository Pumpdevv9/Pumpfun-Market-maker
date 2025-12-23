from __future__ import annotations
import numpy as np
from dataclasses import dataclass
from .models import Quote

@dataclass
class Fill:
    side: str  # "buy" means we bought (bid got hit), "sell" means we sold (ask got lifted)
    px: float
    sz: float

class SimpleMidSim:
    """
    Toy simulator:
      - mid follows lognormal-ish random walk
      - if mid crosses our bid/ask, we assume a fill
    """
    def __init__(self, start_price: float, volatility: float, dt: float, seed: int = 7):
        self.mid = start_price
        self.vol = volatility
        self.dt = dt
        self.rng = np.random.default_rng(seed)

    def step(self) -> float:
        shock = self.rng.normal(0.0, self.vol * np.sqrt(self.dt))
        self.mid = float(self.mid * np.exp(shock))
        return self.mid

    def match(self, q: Quote) -> list[Fill]:
        fills: list[Fill] = []
        if self.mid <= q.bid_px:
            fills.append(Fill("buy", q.bid_px, q.bid_sz))
        if self.mid >= q.ask_px:
            fills.append(Fill("sell", q.ask_px, q.ask_sz))
        return fills
