from __future__ import annotations
from .models import Quote

def round_to_tick(x: float, tick: float) -> float:
    return round(x / tick) * tick

class InventorySkewMM:
    def __init__(self, tick_size: float, lot_size: float, base_spread_bps: float, inventory_skew: float):
        self.tick = tick_size
        self.lot = lot_size
        self.base_spread_bps = base_spread_bps
        self.k = inventory_skew

    def quote(self, mid: float, position: float) -> Quote:
        spread = mid * (self.base_spread_bps / 10_000.0)
        half = spread / 2.0

        skew = self.k * position

        bid = round_to_tick(mid - half - skew, self.tick)
        ask = round_to_tick(mid + half - skew, self.tick)

        bid_sz = self.lot
        ask_sz = self.lot

        if bid >= ask:  # safety if ticks collapse the book
            ask = bid + self.tick

        return Quote(bid, bid_sz, ask, ask_sz)
