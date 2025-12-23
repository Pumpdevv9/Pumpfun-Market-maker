from mm.strategy import InventorySkewMM

def test_quotes_ordered():
    mm = InventorySkewMM(tick_size=0.01, lot_size=1.0, base_spread_bps=100, inventory_skew=0.0)
    q = mm.quote(mid=100.0, position=0.0)
    assert q.bid_px < q.ask_px
