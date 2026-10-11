import json
from datetime import date

import numpy as np
import pandas as pd
import pytest

from diamondhamster import ai, tournament as tm
from test_core import synthetic


def payload(df, layout="rows"):
    t = ((df.index - pd.Timestamp(0, tz="UTC")) // pd.Timedelta(seconds=1)).tolist()
    cols = {"t": t, "o": df["open"].tolist(), "h": df["high"].tolist(), "l": df["low"].tolist(), "c": df["close"].tolist(), "v": df["volume"].tolist()}
    bars = cols if layout == "columns" else [dict(zip(cols, vals)) for vals in zip(*cols.values())]
    summary = {"high": df["high"].max(), "low": df["low"].min(), "last_close": df["close"].iloc[-1], "first_open": df["open"].iloc[0], "total_volume": df["volume"].sum()}
    return {"bars": bars, "summary": summary}


def test_ingest_appends_drops_forming_bar_and_rejects_changes(tmp_path):
    df = synthetic(30, start="2026-09-01")
    today = df.index[-1].date()  # last bar is still forming
    assert tm.ingest("SOL", payload(df.iloc[:20], "columns"), today, tmp_path) == 20
    assert tm.ingest("SOL", payload(df.iloc[15:]), today, tmp_path) == 9
    stored = tm.read_candles("SOL", tmp_path)
    assert stored.index[-1] == df.index[-2]
    np.testing.assert_allclose(stored["close"].values, df["close"].iloc[:-1].values)
    bad = df.iloc[25:].copy()
    bad.iloc[0, bad.columns.get_loc("volume")] = 9.0
    with pytest.raises(ValueError, match="changed"):
        tm.ingest("SOL", payload(bad), today, tmp_path)


def test_check_bars_catches_copy_errors():
    df = synthetic(20)
    assert tm.check_bars(df, payload(df)["summary"]) == []
    typo = df.copy()
    typo.iloc[10, typo.columns.get_loc("close")] *= 1.1  # mis-copied close breaks the next open
    assert any("previous close" in e for e in tm.check_bars(typo))
    p = payload(df)
    p["summary"]["total_volume"] += 1
    assert any("total_volume" in e for e in tm.check_bars(df, p["summary"]))
    assert any("missing days" in e for e in tm.check_bars(df.drop(df.index[5])))


def test_freeze_is_immutable_and_capped(tmp_path, monkeypatch):
    prompts = tmp_path / "prompts"
    prompts.mkdir()
    monkeypatch.setattr(ai, "PROMPTS", prompts)
    reg = tmp_path / "reg.json"
    for i in range(tm.MAX_ACTIVE + 1):
        (prompts / f"P-{i}.md").write_text(f"prompt {i}")
    for i in range(tm.MAX_ACTIVE):
        tm.freeze(f"P-{i}", date(2026, 10, 11 + i), reg)
    with pytest.raises(ValueError, match="already frozen"):
        tm.freeze("P-0", date(2026, 10, 20), reg)
    with pytest.raises(ValueError, match="active prompts"):
        tm.freeze(f"P-{tm.MAX_ACTIVE}", date(2026, 10, 20), reg)
    assert tm.active_prompts(date(2026, 10, 12), reg) == ["P-0", "P-1"]
    (prompts / "P-0.md").write_text("edited")
    with pytest.raises(ValueError, match="changed after freezing"):
        tm.active_prompts(date(2026, 10, 12), reg)


def test_export_round_only_sees_the_past_and_hides_coins(tmp_path, monkeypatch):
    prompts = tmp_path / "prompts"
    prompts.mkdir()
    (prompts / "P-0.md").write_text("decide")
    monkeypatch.setattr(ai, "PROMPTS", prompts)
    reg = tmp_path / "reg.json"
    tm.freeze("P-0", date(2026, 10, 1), reg)
    candles, rounds = tmp_path / "candles", tmp_path / "rounds"
    candles.mkdir()
    decision = date(2026, 10, 18)
    for seed, coin in enumerate(["AAA", "BBB", "CCC"]):
        df = synthetic(300, start="2026-01-01", seed=seed)
        df.loc[:pd.Timestamp(decision, tz="UTC")].to_csv(candles / f"{coin}.csv")
    synthetic(100, start="2026-07-11").to_csv(candles / "NEW.csv")  # too short
    dirs = tm.export_round(decision, ["AAA", "BBB", "CCC", "NEW"], repeats=2, candles=candles, rounds=rounds, registry_path=reg)
    assert len(dirs) == 2
    meta = json.loads((rounds / "2026-10-18" / "round.json").read_text())
    assert meta["coins"] == ["AAA", "BBB", "CCC"] and "NEW" in meta["skipped"]
    req = json.loads((dirs[0] / "requests.json").read_text())
    text = json.dumps(req)
    assert all(c not in text for c in ["AAA", "BBB", "CCC", "2026"])
    assert all(r["window"].splitlines()[-1].startswith("0 ") for r in req["requests"])
    with pytest.raises(ValueError, match="Sunday"):
        tm.export_round(date(2026, 10, 19), ["AAA"], candles=candles, rounds=rounds, registry_path=reg)


def weekly_market(n_weeks=40, coins=10, seed=0):
    rng = np.random.default_rng(seed)
    days = pd.date_range("2026-10-18", periods=n_weeks * 7 + 1, freq="D", tz="UTC")
    common = rng.normal(0, 0.03, len(days))
    closes = {f"C{i}": pd.Series(100 * np.exp(np.cumsum(common + rng.normal(0, 0.02, len(days)))), index=days) for i in range(coins)}
    decisions = days[::7][:-1]
    return closes, decisions


def test_score_rewards_foresight_and_not_constant_exposure():
    closes, decisions = weekly_market()
    rows = []
    for d in decisions:
        for c, s in closes.items():
            r = s[d + pd.Timedelta(days=7)] / s[d] - 1
            rows += [
                {"decision": d, "prompt": "oracle", "coin": c, "weight": 1.0 if r > 0 else 0.0},
                {"decision": d, "prompt": "constant", "coin": c, "weight": 0.5},
            ]
    weekly, summary = tm.score(pd.DataFrame(rows), closes)
    assert summary.loc["oracle", "timing_mean"] > 0 and summary.loc["oracle", "timing_t"] > 3
    assert summary.loc["constant", "timing_mean"] == 0
    assert summary.loc["oracle", "weeks"] == len(decisions)
    assert summary.loc["oracle", "rank_ic_mean"] > 0.3


def test_score_skips_unfinished_week():
    closes, decisions = weekly_market(n_weeks=3)
    late = decisions[-1] + pd.Timedelta(days=7)
    rows = [{"decision": d, "prompt": "p", "coin": "C0", "weight": 0.5} for d in [*decisions, late]]
    weekly, summary = tm.score(pd.DataFrame(rows), closes)
    assert summary.loc["p", "weeks"] == len(decisions)


def test_indicator_prompts_get_the_snapshot_line(tmp_path, monkeypatch):
    prompts = tmp_path / "prompts"
    prompts.mkdir()
    for p in ("P-0", "P-1"):
        (prompts / f"{p}.md").write_text(p)
    monkeypatch.setattr(ai, "PROMPTS", prompts)
    reg = tmp_path / "reg.json"
    tm.freeze("P-0", date(2026, 10, 1), reg)
    tm.freeze("P-1", date(2026, 10, 1), reg, input="indicators")
    candles, rounds = tmp_path / "candles", tmp_path / "rounds"
    candles.mkdir()
    synthetic(400, start="2025-10-01").to_csv(candles / "AAA.csv")
    d0, d1 = tm.export_round(date(2026, 10, 18), ["AAA"], repeats=1, candles=candles, rounds=rounds, registry_path=reg)
    w0 = json.loads((d0 / "requests.json").read_text())["requests"][0]["window"]
    w1 = json.loads((d1 / "requests.json").read_text())["requests"][0]["window"]
    assert w0.startswith("day o h l c v") and w1.startswith("indicators ") and w1.endswith(w0)
