import pytest

from diamondhamster.liq.hl.known import KnownBook

H = 3_600_000


def pos(coin="BTC", side="long", liq=90.0, qty=1.0, mode="cross"):
    return {"coin": coin, "side": side, "mode": mode, "leverage": 10, "entry_px": 100.0, "liq_px": liq,
            "qty": qty, "notional": qty * 100.0}


def test_update_replaces_not_appends():
    b = KnownBook()
    b.update("a", [pos(qty=1)], 0)
    b.update("a", [pos(qty=2)], 1)
    r = b.rows("BTC", 1)
    assert len(r) == 1 and r.qty.iloc[0] == 2 and r.polled_at.iloc[0] == 1


def test_empty_update_removes_user():
    b = KnownBook()
    b.update("a", [pos()], 0)
    b.update("a", [], 1)
    assert b.rows("BTC", 1).empty and b.notional("a") == 0


def test_stale_entries_dropped_after_60_min():
    b = KnownBook()
    b.update("a", [pos()], 0)
    b.update("b", [pos()], H)
    assert list(b.rows("BTC", H + 1).user) == ["b"]


def test_rows_columns_and_coin_filter():
    b = KnownBook()
    b.update("a", [pos("BTC"), pos("ETH", side="short")], 0)
    r = b.rows("ETH", 0)
    assert list(r.columns) == ["user", "side", "mode", "leverage", "entry_px", "liq_px", "qty", "polled_at"]
    assert list(r.side) == ["short"]


def test_coverage_per_side_and_no_liq_share():
    b = KnownBook()
    b.update("a", [pos(side="long", qty=3), pos(side="short", qty=1, liq=None)], 0)
    b.update("b", [pos(side="short", qty=1)], 0)
    c = b.coverage("BTC", oi=10.0, now=0)
    assert c["long"] == pytest.approx(0.3) and c["short"] == pytest.approx(0.2)
    assert c["no_liq_share"] == pytest.approx(1 / 5)


def test_coverage_zero_oi_and_notional():
    b = KnownBook()
    b.update("a", [pos(qty=2), pos("ETH", qty=1)], 0)
    assert b.coverage("BTC", 0.0, 0) == {"long": 0.0, "short": 0.0, "no_liq_share": 0.0}
    assert b.notional("a") == 300.0
