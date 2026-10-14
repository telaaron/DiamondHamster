import pandas as pd
import pytest

from diamondhamster.liq.events import COLUMNS, EventError, EventSet, load_events, save_events


def small_set() -> EventSet:
    return EventSet(
        exchange="sim", symbol="BTCUSDT",
        trades=pd.DataFrame({"ts": [1000, 1000, 2500], "price": [100.0, 100.5, 101.0], "qty": [1.0, 2.0, 0.5],
                             "taker_buy": [True, False, True]}),
        oi=pd.DataFrame({"ts": [1000, 2000, 3000], "oi": [50.0, 51.0, 50.5]}),
        mark=pd.DataFrame({"ts": [1000, 2000, 3000], "high": [101.0] * 3, "low": [99.0] * 3, "close": [100.0] * 3}),
        funding=pd.DataFrame({"ts": [2000], "rate": [0.0001]}),
        liquidations=pd.DataFrame({"ts": [2500], "side": ["long"], "price": [99.0], "qty": [0.1]}),
        gaps=pd.DataFrame(columns=COLUMNS["gaps"]),
    )


def test_roundtrip(tmp_path):
    es = small_set()
    save_events(es, tmp_path)
    back = load_events(tmp_path)
    assert (back.exchange, back.symbol) == ("sim", "BTCUSDT")
    for name in ("trades", "oi", "mark", "funding", "liquidations"):
        pd.testing.assert_frame_equal(getattr(back, name), getattr(es, name), check_dtype=False)
    assert back.gaps.empty


def test_until_filters_everything():
    es = small_set().until(2000)
    assert es.trades.ts.max() <= 2000 and es.oi.ts.max() == 2000 and es.mark.ts.max() == 2000
    assert es.liquidations.empty and len(es.funding) == 1


def test_unsorted_oi_names_file_and_row(tmp_path):
    es = small_set()
    es.oi = pd.DataFrame({"ts": [1000, 3000, 2000], "oi": [1.0, 1.0, 1.0]})
    save_events(es, tmp_path)
    with pytest.raises(EventError, match=r"oi\.csv.*Zeile 3"):
        load_events(tmp_path)


def test_duplicate_trade_ts_ok_duplicate_mark_ts_not(tmp_path):
    es = small_set()
    save_events(es, tmp_path)
    load_events(tmp_path)  # trades haben doppelten ts 1000: erlaubt
    es.mark = pd.DataFrame({"ts": [1000, 1000], "high": [1.0, 1.0], "low": [1.0, 1.0], "close": [1.0, 1.0]})
    save_events(es, tmp_path)
    with pytest.raises(EventError, match=r"mark\.csv.*Zeile 2"):
        load_events(tmp_path)


def test_negative_price_rejected(tmp_path):
    es = small_set()
    es.trades.loc[1, "price"] = -1.0
    save_events(es, tmp_path)
    with pytest.raises(EventError, match=r"trades\.csv.*Zeile 2"):
        load_events(tmp_path)


def test_missing_required_file(tmp_path):
    save_events(small_set(), tmp_path)
    (tmp_path / "oi.csv").unlink()
    with pytest.raises(EventError, match="oi.csv"):
        load_events(tmp_path)
