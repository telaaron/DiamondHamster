import numpy as np
import pandas as pd

from diamondhamster import sk


def _df(highs, lows=None):
    highs = np.asarray(highs, dtype=float)
    lows = highs - 1 if lows is None else np.asarray(lows, dtype=float)
    idx = pd.date_range("2020-01-01", periods=len(highs), freq="D", tz="UTC")
    close = (highs + lows) / 2
    return pd.DataFrame({"open": close, "high": highs, "low": lows, "close": close}, index=idx)


def test_pivot_is_known_only_k_bars_later():
    # high at bar 3, k = 2 -> confirmed at bar 5, not earlier
    df = _df([1, 2, 3, 9, 3, 2, 1, 1])
    piv = sk.pivots(df, k=2)
    highs = [p for p in piv if p.kind == "H"]
    assert [(p.i, p.confirmed) for p in highs] == [(3, 5)]


def test_pivots_alternate_and_keep_more_extreme():
    # two highs in a row (bars 2 and 6) without a confirmed low between -> keep the higher one
    df = _df([1, 2, 5, 2, 1.5, 2, 7, 2, 1, 1, 1], lows=[0, 1, 4, 1.4, 1.0, 1.2, 6, 1, 0.5, 0.6, 0.7])
    piv = sk.pivots(df, k=2)
    kinds = [p.kind for p in piv]
    assert all(a != b for a, b in zip(kinds, kinds[1:]))


def _seq_df():
    # 0 low at bar 5 (price 100), A high at bar 15 (200), B low at bar 25 (140: retrace 60 %), then rally
    n = 60
    lows = np.full(n, 150.0)
    highs = np.full(n, 160.0)
    lows[:5] = 120; highs[:5] = 130
    lows[5] = 100; highs[5] = 110
    lows[6:15] = np.linspace(110, 180, 9); highs[6:15] = lows[6:15] + 5
    lows[15] = 190; highs[15] = 200
    lows[16:25] = np.linspace(185, 150, 9); highs[16:25] = lows[16:25] + 5
    lows[25] = 140; highs[25] = 145
    lows[26:] = np.linspace(146, 330, n - 26); highs[26:] = lows[26:] + 5
    return _df(highs, lows)


def test_bullish_sequence_levels_and_entry_after_confirmation():
    df = _seq_df()
    seqs = sk.sequences(df, k=3)
    bull = [s for s in seqs if s.direction == 1]
    assert len(bull) >= 1
    s = bull[0]
    assert (s.p0, s.pa, s.pb) == (100, 200, 140)
    assert s.confirmed == 28  # B at 25 + k
    assert abs(s.target - (140 + 1.618 * 100)) < 1e-9
    assert s.stop == 100


def test_sequence_rejected_when_b_below_zero_point():
    df = _seq_df()
    df.iloc[25, df.columns.get_loc("low")] = 90  # B below 0 -> invalid
    assert not [s for s in sk.sequences(df, k=3) if s.direction == 1 and s.pa == 200]


def test_trade_hits_target_and_r_is_positive():
    df = _seq_df()
    s = [s for s in sk.sequences(df, k=3) if s.direction == 1][0]
    t = sk.simulate(df, s, cost_per_side=0.0)
    assert t.outcome == "target"
    entry = df["open"].iloc[s.confirmed + 1]
    assert t.exit >= s.target  # filled at the target, or at a better open when price gaps through it
    assert abs(t.r - (t.exit - entry) / (entry - s.stop)) < 1e-9


def test_stop_wins_when_both_hit_same_bar():
    df = _seq_df()
    s = [s for s in sk.sequences(df, k=3) if s.direction == 1][0]
    j = s.confirmed + 2
    df.iloc[j, df.columns.get_loc("high")] = 1000
    df.iloc[j, df.columns.get_loc("low")] = 50
    assert sk.simulate(df, s, cost_per_side=0.0).outcome == "stop"


def test_weekly_kl_filter_uses_only_confirmed_weekly_swings():
    df = _seq_df()
    s = [s for s in sk.sequences(df, k=3) if s.direction == 1][0]
    zones = sk.kl_zones(df, k=3)
    # with only ~9 weeks of data no weekly swing is confirmed before bar 28 -> filter says no
    assert not sk.in_kl(s, zones, df.index)


def test_no_lookahead_on_truncated_history():
    # sequences confirmed by bar t must be identical whether or not later bars exist
    rng = np.random.default_rng(1)
    close = 100 * np.exp(np.cumsum(rng.normal(0, 0.03, 600)))
    df = _df(close * 1.01, close * 0.99)
    full = sk.sequences(df, k=5)
    cut = 400
    part = sk.sequences(df.iloc[: cut + 1], k=5)
    assert [s for s in full if s.confirmed <= cut] == part
    zones_full = [z for z in sk.kl_zones(df, k=3) if z[0] <= df.index[cut]]
    assert zones_full == sk.kl_zones(df.iloc[: cut + 1], k=3)[: len(zones_full)]
