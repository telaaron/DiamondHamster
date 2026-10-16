import pandas as pd
import pytest

from diamondhamster.liq.trades import compress

M = 60_000


def df(rows):
    return pd.DataFrame(rows, columns=["ts", "price", "qty", "taker_buy"])


def test_compress_sums_and_vwap():
    out = compress(df([(10, 100.0, 1.0, 1), (20, 110.0, 1.0, 1)]))
    assert len(out) == 1
    r = out.iloc[0]
    assert (r.ts, r.price, r.qty, r.notional) == (M, 105.0, 2.0, 105.0)


def test_compress_splits_classes():
    out = compress(df([(10, 100.0, 50.0, 1), (20, 100.0, 500.0, 0)]))  # 5k und 50k USD
    assert list(out.qty) == [50.0, 500.0] and list(out.ts) == [M, M]
    assert list(out.notional) == [5000.0, 50000.0]


def test_compress_ts_is_minute_end():
    out = compress(df([(M, 100.0, 1.0, 1), (2 * M - 1, 100.0, 1.0, 1), (2 * M, 100.0, 1.0, 1)]))
    assert list(out.ts) == [2 * M, 3 * M] and list(out.qty) == [2.0, 1.0]


def test_compress_taker_majority():
    out = compress(df([(1, 100.0, 1.0, 1), (2, 100.0, 3.0, 0)]))
    assert out.taker_buy.iloc[0] == 0


def test_compress_notional_is_qty_weighted_trade_notional():
    out = compress(df([(1, 100.0, 1.0, 1), (2, 100.0, 3.0, 1)]))  # Notionals 100 und 300, Gewichte 1 und 3
    assert out.notional.iloc[0] == pytest.approx((100 * 1 + 300 * 3) / 4)


def test_compress_empty():
    out = compress(df([]))
    assert list(out.columns) == ["ts", "price", "qty", "taker_buy", "notional"] and out.empty
