"""Port of the "Harms BTC - QS-Klassen je Zyklus" Pine indicator (indicators/qs_zyklen.pine).

Pure calendar arithmetic: days since the active bear-market anchor, reduced to its iterated digit sum
(1..9), and a hit when that sum equals one of the two classes assigned to the cycle. Uses no prices.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

ANCHORS = {
    1: pd.Timestamp("2011-11-17", tz="UTC"),
    2: pd.Timestamp("2015-08-18", tz="UTC"),
    3: pd.Timestamp("2018-12-15", tz="UTC"),
    4: pd.Timestamp("2022-11-21", tz="UTC"),
}
ANCHOR_2015_ALT = pd.Timestamp("2015-01-14", tz="UTC")
CLASSES = {1: (4, 6), 2: (6, 3), 3: (3, 5), 4: (5, 9)}
PAIRS = [(a, b) for a in range(1, 10) for b in range(a + 1, 10)]  # the 36 possible class pairs


def qs(n: np.ndarray) -> np.ndarray:
    """Iterated digit sum of a positive day count; 0 at the anchor itself."""
    n = np.asarray(n)
    return np.where(n > 0, 1 + (n - 1) % 9, 0)


def calendar(index: pd.DatetimeIndex, anchors: dict[int, pd.Timestamp] = ANCHORS) -> pd.DataFrame:
    """Cycle, days since anchor and QS for each UTC calendar day in `index` (0 / NaN before the first anchor)."""
    days = index.normalize()
    cycle = np.zeros(len(days), dtype=int)
    for c in sorted(anchors):
        cycle[days >= anchors[c]] = c
    anchor = pd.DatetimeIndex([anchors[c] if c else pd.NaT for c in cycle])
    n = np.where(cycle > 0, (days - anchor).days, -1)
    return pd.DataFrame({"cycle": cycle, "days": n, "qs": np.where(cycle > 0, qs(n), 0)}, index=index)


def hits(cal: pd.DataFrame, classes: dict[int, tuple[int, int]] = CLASSES) -> pd.Series:
    """True on days whose QS equals class A or B of the active cycle. The anchor day never hits."""
    a = cal["cycle"].map(lambda c: classes.get(c, (0, 0))[0])
    b = cal["cycle"].map(lambda c: classes.get(c, (0, 0))[1])
    return (cal["cycle"] > 0) & (cal["days"] > 0) & ((cal["qs"] == a) | (cal["qs"] == b))
