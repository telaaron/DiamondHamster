import pandas as pd

from diamondhamster import qs


def test_qs_digit_sum():
    assert list(qs.qs([0, 1, 9, 10, 18, 19, 216])) == [0, 1, 9, 1, 9, 1, 9]


def test_alternative_2015_anchor_has_same_phase():
    # The script's tooltip: 14.01.2015 lies 216 days earlier, a multiple of 9.
    assert (qs.ANCHORS[2] - qs.ANCHOR_2015_ALT).days == 216


def test_calendar_and_hits_match_pine_rules():
    idx = pd.date_range("2022-11-20", "2022-12-02", freq="D", tz="UTC")
    cal = qs.calendar(idx)
    assert cal.loc["2022-11-20", "cycle"].item() == 3  # day before the new anchor belongs to the old cycle
    assert cal.loc["2022-11-21", "days"].item() == 0 and cal.loc["2022-11-21", "qs"].item() == 0
    h = qs.hits(cal)
    assert not h.loc["2022-11-21"].item()  # anchor is never a hit
    # 2022-11-20 is day 1436 of the 2018 cycle: QS 5, a 2018 class (3 / 5).
    # 2022 cycle classes 5 / 9: day 5 = 2022-11-26, day 9 = 2022-11-30.
    assert list(h[h].index.strftime("%Y-%m-%d")) == ["2022-11-20", "2022-11-26", "2022-11-30"]


def test_before_first_anchor_is_no_cycle():
    cal = qs.calendar(pd.date_range("2011-11-15", periods=3, freq="D", tz="UTC"))
    assert list(cal["cycle"]) == [0, 0, 1]
    assert not qs.hits(cal).iloc[:2].any()
