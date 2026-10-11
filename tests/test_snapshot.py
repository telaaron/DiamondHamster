from diamondhamster import features, snapshot
from test_core import synthetic


def test_snapshot_uses_only_the_past_and_hides_level():
    df = synthetic(400)
    t = df.index[300]
    full = snapshot.snapshot(features.compute(df), t)
    cut = snapshot.snapshot(features.compute(df.loc[:t]), t)
    assert full == cut
    scaled = df.copy()
    scaled[["open", "high", "low", "close"]] *= 37.0
    assert snapshot.snapshot(features.compute(scaled), t) == full
    assert "moon" not in full and "month" not in full and "na" not in full
