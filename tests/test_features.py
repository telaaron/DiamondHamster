import numpy as np
import pandas as pd

from diamondhamster import features
from test_core import synthetic


def test_no_feature_uses_future_rows():
    df = synthetic(500)
    full = features.compute(df)
    for t in [df.index[260], df.index[333], df.index[-1]]:
        part = features.compute(df.loc[:t])
        pd.testing.assert_series_equal(part.loc[t], full.loc[t], check_names=False, atol=1e-9)


def test_rsi_bounds_and_trend():
    up = pd.Series(np.linspace(100, 200, 100))
    assert features.rsi(up).iloc[-1] > 95
    assert features.rsi(up[::-1].reset_index(drop=True)).iloc[-1] < 5


def test_rci_extremes():
    s = pd.Series(np.arange(30.0))
    assert features.rci(s, 9).iloc[-1] == 100
    assert features.rci(-s, 9).iloc[-1] == -100


def test_moon_age_known_new_moon():
    # New moon on 2024-04-08 18:21 UTC (total solar eclipse)
    age = features.moon_age(pd.DatetimeIndex([pd.Timestamp("2024-04-08 18:21", tz="UTC")])).iloc[0]
    assert min(age, features.SYNODIC_MONTH - age) < 0.6


def test_compute_runs_on_real_shape():
    df = synthetic(400)
    df["volume"] = np.random.default_rng(0).lognormal(0, 0.5, len(df))
    f = features.compute(df)
    assert f.iloc[250:].drop(columns=["div_rsi"]).notna().all().all()
