from __future__ import annotations
from dataclasses import dataclass

@dataclass
class RiskState:
    position: float = 0.0
    realized_pnl: float = 0.0

class RiskManager:
    def __init__(self, max_position: float, max_notional: float, max_daily_loss: float):
        self.max_position = max_position
        self.max_notional = max_notional
        self.max_daily_loss = max_daily_loss
        self.state = RiskState()

    def can_quote(self, mid: float) -> bool:
        if self.max_daily_loss and self.state.realized_pnl <= -abs(self.max_daily_loss):
            return False
        if self.max_notional and abs(self.state.position * mid) >= abs(self.max_notional):
            return False
        if self.max_position and abs(self.state.position) >= abs(self.max_position):
            return False
        return True

    def on_fill(self, side: str, px: float, sz: float):
        # side: "buy" increases position, "sell" decreases
        if side == "buy":
            self.state.position += sz
        else:
            self.state.position -= sz
