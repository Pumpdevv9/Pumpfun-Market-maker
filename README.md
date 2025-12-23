# Memecoin Market Maker (Simulator + Paper Trading)

This repo provides a **market making quote engine** designed for microcaps/memecoins with:
- inventory-aware quoting (skew)
- spread control + volatility scaling
- risk limits (position, notional, max loss)
- **simulator/paper venue** (no exchange keys required)

> This project is intended for **legitimate liquidity provision and research**.
> Do not use it for wash trading, spoofing, or manipulation.

## Quickstart

```bash
python -m venv .venv && source .venv/bin/activate  # (Windows: .venv\Scripts\activate)
pip install -e .
cp .env.example .env
python scripts/run_paper.py --config configs/example.yaml

