import numpy as np
import pytest

from diamondhamster.liq.attribution import Deposit
from diamondhamster.liq.book import Book
from diamondhamster.liq.grid import Grid


def dep(side, mode, prices, qtys):
    return Deposit(side, mode, np.asarray(prices, float), np.asarray(qtys, float))


def book():
    return Book(Grid(100, 10), max_cohorts=3, start_day=0)


def at(b, side, price):
    return b.distribution(side)[b.grid.index(price)]


def test_sweep_only_crossed():
    b = book()
    b.add(dep("long", "isolated", [90, 80], [1.0, 2.0]), cohort=1, ambiguous_frac=0)
    b.add(dep("short", "cross", [120], [1.5]), cohort=1, ambiguous_frac=0)
    swept = b.sweep(mark_low=85, mark_high=110)
    assert swept["long"] == pytest.approx(1.0) and swept["short"] == 0
    assert at(b, "long", 80) == pytest.approx(2.0) and at(b, "long", 90) == 0
    assert b.total("short") == pytest.approx(1.5)


def test_close_beta_zero_proportional():
    b = book()
    b.add(dep("long", "isolated", [90], [1.0]), cohort=1, ambiguous_frac=0)
    b.add(dep("long", "cross", [80], [3.0]), cohort=2, ambiguous_frac=0)
    b.close("long", 2.0, today=5, beta=0.0)
    assert at(b, "long", 90) == pytest.approx(0.5) and at(b, "long", 80) == pytest.approx(1.5)


def test_close_beta_positive_prefers_old():
    b = book()
    b.add(dep("long", "isolated", [90], [1.0]), cohort=1, ambiguous_frac=0)
    b.add(dep("long", "isolated", [80], [1.0]), cohort=5, ambiguous_frac=0)
    b.close("long", 1.0, today=5, beta=0.5)
    assert at(b, "long", 90) < at(b, "long", 80)


def test_close_never_negative():
    b = book()
    b.add(dep("long", "isolated", [90], [1.0]), cohort=1, ambiguous_frac=0)
    b.add(dep("long", "isolated", [80], [0.01]), cohort=5, ambiguous_frac=0)
    b.close("long", 5.0, today=5, beta=3.0)
    assert b.total("long") == 0 and (b.distribution("long") >= 0).all()
    b.add(dep("long", "isolated", [90, 80], [1.0, 1.0]), cohort=1, ambiguous_frac=0)
    b.close("long", 1.9, today=60, beta=3.0)  # Wasserfüllung: alte Kohorte voll, Rest neu
    assert (b.distribution("long") >= -1e-12).all() and b.total("long") == pytest.approx(0.1)


def test_funding_shifts_isolated_only():
    b = book()
    b.add(dep("long", "isolated", [90], [1.0]), cohort=1, ambiguous_frac=0)
    b.add(dep("long", "cross", [90], [1.0]), cohort=1, ambiguous_frac=0)
    i = b.grid.index(90)
    b.apply_funding(0.003)
    d = b.distribution("long")
    assert d[i + 3] == pytest.approx(1.0) and d[i] == pytest.approx(1.0)


def test_scale_and_total():
    b = book()
    b.add(dep("short", "isolated", [110, 120], [1.0, 3.0]), cohort=1, ambiguous_frac=0)
    b.scale("short", 0.5)
    assert b.total("short") == pytest.approx(2.0) and b.total("long") == 0


def test_merge_old_keeps_mass():
    b = book()
    for c in range(1, 6):
        b.add(dep("long", "isolated", [90], [1.0]), cohort=c, ambiguous_frac=0)
    b.apply_funding(0.002)
    b.merge_old(today=6)
    assert len(b.cohorts()) == 3 and b.total("long") == pytest.approx(5.0)


def test_ambiguous_tracks_add_and_close():
    b = book()
    b.add(dep("long", "isolated", [90], [2.0]), cohort=1, ambiguous_frac=0.25)
    assert b.ambiguous_distribution("long").sum() == pytest.approx(0.5)
    b.close("long", 1.0, today=1, beta=0.0)
    assert b.ambiguous_distribution("long").sum() == pytest.approx(0.25)


def test_seed_share_and_age():
    b = Book(Grid(100, 10), max_cohorts=10, start_day=10)
    b.add(dep("long", "isolated", [90], [1.0]), cohort=Book.SEED, ambiguous_frac=0)
    b.add(dep("long", "isolated", [90], [3.0]), cohort=14, ambiguous_frac=0)
    assert b.seed_share() == pytest.approx(0.25)
    assert b.age_distribution("long", today=14)[b.grid.index(90)] == pytest.approx(1.0)  # (4·1 + 0·3)/4


def test_out_of_range_share():
    b = book()
    b.add(dep("long", "isolated", [1.0, 90], [1.0, 3.0]), cohort=1, ambiguous_frac=0)
    assert b.out_of_range_share() == pytest.approx(0.25)


def test_merge_old_never_merges_into_seed():
    b = Book(Grid(100, 10), max_cohorts=3, start_day=0)
    b.add(dep("long", "isolated", [90], [1.0]), cohort=Book.SEED, ambiguous_frac=0)
    for c in (1, 2, 3):
        b.add(dep("long", "isolated", [90], [1.0]), cohort=c, ambiguous_frac=0)
    b.merge_old(today=4)
    assert len(b.cohorts()) == 3 and b.seed_share() == pytest.approx(0.25)


def test_out_of_range_mass_stays_at_edge_under_funding():
    b = book()
    b.add(dep("long", "isolated", [1.0], [1.0]), cohort=1, ambiguous_frac=0)
    b.apply_funding(0.01)
    assert b.distribution("long")[0] == pytest.approx(1.0) and b.out_of_range_share() == pytest.approx(1.0)


def test_edge_mass_swept_when_price_leaves_grid_under_funding():
    b = book()
    b.add(dep("short", "isolated", [1000.0], [1.0]), cohort=1, ambiguous_frac=0)
    b.add(dep("short", "isolated", [380.0], [1.0]), cohort=1, ambiguous_frac=0)
    b.apply_funding(0.01)
    swept = b.sweep(mark_low=500, mark_high=1000)
    assert swept["short"] == pytest.approx(2.0) and b.total("short") == 0
