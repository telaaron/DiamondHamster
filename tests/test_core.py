import io
import zipfile

import numpy as np
import pandas as pd
import pytest

from diamondhamster import backtest, baselines, data, metrics, quality


def synthetic(n=800, start="2020-01-01", seed=1):
    rng = np.random.default_rng(seed)
    idx = pd.date_range(start, periods=n, freq="D", tz="UTC", name="date")
    close = 100 * np.exp(np.cumsum(rng.normal(0, 0.03, n)))
    open_ = np.r_[100, close[:-1]]
    return pd.DataFrame({"open": open_, "high": np.maximum(open_, close) * 1.01, "low": np.minimum(open_, close) * 0.99, "close": close, "volume": 1.0}, index=idx)


def test_no_lookahead_perfect_foresight_signal_is_delayed():
    df = synthetic()
    # A signal that peeks at tomorrow's open-to-open return must not earn it: the position starts a day later.
    peek = (df["open"].shift(-1) > df["open"]).astype(float)
    res = backtest.run(df, peek, cost_per_side=0.0)
    fwd = df["open"].shift(-1) / df["open"] - 1
    assert res["position"].iloc[1:].equals(peek.shift(1).iloc[1:].reindex(res.index[1:]))
    perfect = (fwd.clip(lower=0)).loc[res.index].sum()
    assert res["ret"].sum() < 0.5 * perfect


def test_weights_change_only_after_signal_day():
    df = synthetic(10)
    w = pd.Series(0.0, index=df.index)
    w.iloc[3] = 1.0
    res = backtest.run(df, w, cost_per_side=0.0)
    assert res["position"].iloc[3] == 0.0 and res["position"].iloc[4] == 1.0


def test_costs_charged_on_turnover():
    df = synthetic(10)
    df["open"] = 100.0
    w = pd.Series([1, 1, 0, 0, 1, 1, 1, 1, 1, 1], index=df.index, dtype=float)
    res = backtest.run(df, w, cost_per_side=0.01)
    assert res["turnover"].sum() == pytest.approx(3.0)
    assert res["equity"].iloc[-1] == pytest.approx(0.99 ** 3)


def test_buy_and_hold_matches_price():
    df = synthetic()
    res = backtest.run(df, pd.Series(1.0, index=df.index), cost_per_side=0.0)
    assert res["equity"].iloc[-1] == pytest.approx(df["open"].iloc[-1] / df["open"].iloc[1])


def test_holdout_is_cut_and_unlock_is_logged(tmp_path, monkeypatch):
    monkeypatch.setattr(data, "HOLDOUT_LOG", tmp_path / "holdout.log")
    df = synthetic(2000, start="2020-01-01")
    locked = data.apply_holdout(df)
    assert locked.index.max() < data.HOLDOUT_START
    full = data.apply_holdout(df, unlock_holdout="final test H-001")
    assert full.index.max() >= data.HOLDOUT_START
    assert "final test H-001" in (tmp_path / "holdout.log").read_text()


def test_save_never_overwrites_and_hash_verifies(tmp_path, monkeypatch):
    monkeypatch.setattr(data, "RAW", tmp_path / "raw")
    monkeypatch.setattr(data, "MANIFEST", tmp_path / "manifest.json")
    df = synthetic(50)
    path = data.save(df, "test", "X")
    data.verify(path)
    pd.testing.assert_frame_equal(data.read(path), df, check_freq=False, atol=1e-6)
    with pytest.raises(FileExistsError):
        data.save(df, "test", "X")
    path.write_text(path.read_text().replace("1.0", "2.0", 1))
    with pytest.raises(ValueError):
        data.verify(path)


def test_parse_binance_ms_and_us_timestamps():
    ms = "1704067200000,42000,43000,41000,42500,10,1704153599999,0,0,0,0,0\n"
    us = "1735689600000000,93000,95000,92000,94000,5,1735775999999999,0,0,0,0,0\n"
    df = data.parse_binance_klines((ms + us).encode())
    assert [str(d.date()) for d in df.index] == ["2024-01-01", "2025-01-01"]
    assert df["close"].tolist() == [42500, 94000]


def test_quality_flags_gaps_and_bad_ohlc():
    df = synthetic(20).drop(pd.Timestamp("2020-01-05", tz="UTC"))
    df.iloc[3, df.columns.get_loc("high")] = 1
    rep = quality.report(df)
    assert rep["missing_days"] == ["2020-01-05"] and rep["inconsistent_ohlc"] == 1


def test_dca_constant_price_returns_capital_minus_cost():
    df = synthetic(365)
    df[["open", "high", "low", "close"]] = 100.0
    r = baselines.dca(df, amount=100, cost_per_side=0.0)
    assert r["multiple"] == pytest.approx(1.0) and r["irr"] == pytest.approx(0.0, abs=1e-6)


def test_random_weights_hit_target_exposure():
    idx = pd.date_range("2015-01-01", periods=4000, freq="D", tz="UTC")
    w = baselines.random_weights(idx, 0.3, 20, np.random.default_rng(0))
    assert abs(w.mean() - 0.3) < 0.08


def test_regime_split_runs():
    df = synthetic(2200, start="2017-01-01")
    out = metrics.by_regime(baselines.buy_and_hold(df))
    assert {"bear_2018", "bull_2020_21"} <= set(out.index)
