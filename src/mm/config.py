from __future__ import annotations
from pydantic import BaseModel
from typing import Optional

class StrategyConfig(BaseModel):
    base_spread_bps: float = 80.0
    inventory_skew: float = 0.0
    max_levels: int = 1

class RiskConfig(BaseModel):
    max_position: float = 0.0
    max_notional: float = 0.0
    max_daily_loss: float = 0.0

class SimulatorConfig(BaseModel):
    start_price: float = 1.0
    volatility: float = 0.01
    steps: int = 1000
    dt: float = 1.0

class AppConfig(BaseModel):
    symbol: str
    tick_size: float
    lot_size: float
    strategy: StrategyConfig
    risk: RiskConfig
    simulator: SimulatorConfig
