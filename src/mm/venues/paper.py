from __future__ import annotations
from .base import Venue
from ..models import Quote
from ..simulator import SimpleMidSim

class PaperVenue(Venue):
    def __init__(self, sim: SimpleMidSim):
        self.sim = sim
        self._last_quote: Quote | None = None
        self._pending: list[tuple[str, float, float]] = []

    def get_mid(self) -> float:
        return self.sim.step()

    def place_quote(self, quote: Quote) -> None:
        self._last_quote = quote
        fills = self.sim.match(quote)
        self._pending.extend([(f.side, f.px, f.sz) for f in fills])

    def poll_fills(self) -> list[tuple[str, float, float]]:
        out = self._pending
        self._pending = []
        return out
