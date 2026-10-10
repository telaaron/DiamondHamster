import pandas as pd

from diamondhamster import ai
from test_core import synthetic


def test_window_has_no_future_rows_and_is_anonymized():
    df = synthetic(300)
    t = df.index[200]
    w = ai.window(df, t, 60)
    assert len(w) == 60 and w.index[-1] == 0
    assert w["close"].iloc[-1] == 100
    raw = ai.window(df, t, 60, anonymize=False)
    assert raw.index.max() == t


def test_decide_series_only_sees_the_past():
    df = synthetic(400)
    seen_last = []

    def decide(w):
        seen_last.append(len(w))
        return 1.0

    raw_last = []

    def decide_raw(w):
        raw_last.append(w.index.max())
        return 1.0

    ai.decide_series(df, decide_raw, lookback=90, anonymize=False)
    w = ai.decide_series(df, decide, lookback=90)
    assert all(n == 90 for n in seen_last)
    rebalance_days = pd.DatetimeIndex(raw_last)
    assert (rebalance_days.dayofweek == 6).all()
    assert w.loc[: rebalance_days[0] - pd.Timedelta(days=1)].eq(0).all()


def test_cache_roundtrip(tmp_path):
    c = ai.ResponseCache(tmp_path)
    k = ai.cache_key("model-x", "abc", "input")
    assert c.get(k) is None
    c.put(k, "0.5", {"model": "model-x"})
    assert c.get(k) == "0.5"
    assert k != ai.cache_key("model-y", "abc", "input")
