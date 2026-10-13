"""E-035: only the indicator line of the decision day, no candle table (backlog #10)."""
from diamondhamster import features, snapshot


def render(df, lookback):
    return snapshot.snapshot(features.compute(df), df.index[-1])
