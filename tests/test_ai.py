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


def test_export_hides_dates_and_roundtrips(tmp_path, monkeypatch):
    import json
    monkeypatch.setattr(ai, "PROMPTS", tmp_path)
    (tmp_path / "p1.md").write_text("decide")
    df = synthetic(400)
    ai.export_requests(df, "p1", tmp_path / "run", lookback=90)
    req = (tmp_path / "run" / "requests.json").read_text()
    import re
    assert not re.search(r"\d{4}-\d{2}-\d{2}", req)
    key = json.loads((tmp_path / "run" / "key.json").read_text())
    ordered = sorted(key, key=key.get)
    assert list(key) != ordered  # shuffled, order leaks no chronology
    (tmp_path / "run" / "responses.json").write_text(json.dumps({"model": "m", "responses": {i: 1.0 for i in key}}))
    w = ai.load_responses(df, tmp_path / "run")
    first = min(map(pd.Timestamp, key.values()))
    assert w.loc[first:].eq(1.0).all() and w.loc[: first - pd.Timedelta(days=1)].eq(0.0).all()
