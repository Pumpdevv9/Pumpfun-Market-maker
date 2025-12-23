from __future__ import annotations
import argparse, yaml
from mm.config import AppConfig
from mm.strategy import InventorySkewMM
from mm.risk import RiskManager
from mm.simulator import SimpleMidSim
from mm.venues.paper import PaperVenue

def load_config(path: str) -> AppConfig:
    with open(path, "r", encoding="utf-8") as f:
        raw = yaml.safe_load(f)
    return AppConfig(**raw)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="configs/example.yaml")
    args = ap.parse_args()

    cfg = load_config(args.config)

    sim = SimpleMidSim(cfg.simulator.start_price, cfg.simulator.volatility, cfg.simulator.dt)
    venue = PaperVenue(sim)

    strat = InventorySkewMM(
        tick_size=cfg.tick_size,
        lot_size=cfg.lot_size,
        base_spread_bps=cfg.strategy.base_spread_bps,
        inventory_skew=cfg.strategy.inventory_skew,
    )

    risk = RiskManager(cfg.risk.max_position, cfg.risk.max_notional, cfg.risk.max_daily_loss)

    for i in range(cfg.simulator.steps):
        mid = venue.get_mid()
        if not risk.can_quote(mid):
            print(f"[{i}] risk stop. pos={risk.state.position:.2f} pnl={risk.state.realized_pnl:.2f}")
            break

        q = strat.quote(mid, risk.state.position)
        venue.place_quote(q)

        fills = venue.poll_fills()
        for side, px, sz in fills:
            risk.on_fill(side, px, sz)

        if i % 50 == 0:
            print(f"[{i}] mid={mid:.6f} bid={q.bid_px:.6f} ask={q.ask_px:.6f} pos={risk.state.position:.2f}")

if __name__ == "__main__":
    main()
