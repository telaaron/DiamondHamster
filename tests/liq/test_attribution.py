import numpy as np
import pytest

from diamondhamster.liq.attribution import deposits, opens_closes
from diamondhamster.liq.margin import liq_price_isolated
from diamondhamster.liq.params import load_params


def test_opens_closes_cases():
    assert opens_closes(10, 4, 0.5) == pytest.approx((4 + 1.5, 1.5, 1.5))
    assert opens_closes(10, -4, 0.5) == pytest.approx((1.5, 4 + 1.5, 1.5))
    assert opens_closes(2, 5, 0.5) == pytest.approx((5, 0, 0))  # V < |ΔOI|


def test_deposits_conserve_mass():
    p = load_params()
    ds = deposits(np.array([100.0, 101.0]), np.array([1.0, 3.0]), 2.0, p)
    assert len(ds) == 4
    for side in ("long", "short"):
        assert sum(d.qty.sum() for d in ds if d.side == side) == pytest.approx(2.0)
    assert sum(d.qty.sum() for d in ds if d.mode == "cross") == pytest.approx(2 * 2.0 * 0.3)


def test_long_below_short_above():
    ds = deposits(np.array([100.0]), np.array([1.0]), 1.0, load_params())
    assert all((d.liq_price[d.qty > 0] < 100).all() for d in ds if d.side == "long")
    assert all((d.liq_price[d.qty > 0] > 100).all() for d in ds if d.side == "short")


def test_tier_caps_leverage():
    # Notional 5e6 USD → Tier max 20x (mmr 0.025, k 46300): keine Masse näher am Einstieg als bei 20x
    p = load_params()
    ds = deposits(np.array([100_000.0]), np.array([50.0]), 50.0, p)
    long20 = liq_price_isolated("long", 100_000.0, 20, 0.025, 46300.0, 50.0)
    short20 = liq_price_isolated("short", 100_000.0, 20, 0.025, 46300.0, 50.0)
    for d in ds:
        live = d.liq_price[d.qty > 0]
        assert (live <= long20 + 1e-6).all() if d.side == "long" else (live >= short20 - 1e-6).all()


def test_force_class_overrides_size():
    p = load_params()
    a = deposits(np.array([100.0]), np.array([1.0]), 1.0, p, force_class="large")
    iso_long = next(d for d in a if d.side == "long" and d.mode == "isolated")
    # large hat kein Gewicht über 25x
    assert (iso_long.liq_price[iso_long.qty > 0] < 100 * (1 - 1 / 25) + 1).all()


def test_deposits_notional_overrides_class_and_tier():
    # Menge 1 zu 100 USD wäre "small"; mit notional 5 Mio. USD gelten Klasse large und das 20x-Tier
    p = load_params()
    a = deposits(np.array([100.0]), np.array([1.0]), 1.0, p, notionals=np.array([5_000_000.0]))
    b = deposits(np.array([100.0]), np.array([50_000.0]), 1.0, p)  # echtes 5-Mio.-Notional
    for da, db in zip(a, b):
        np.testing.assert_allclose(da.liq_price, db.liq_price)
        np.testing.assert_allclose(da.qty, db.qty)


def test_deposits_without_notionals_unchanged():
    p = load_params()
    a = deposits(np.array([100.0, 101.0]), np.array([1.0, 3.0]), 2.0, p)
    b = deposits(np.array([100.0, 101.0]), np.array([1.0, 3.0]), 2.0, p, notionals=np.array([100.0, 303.0]))
    for da, db in zip(a, b):
        np.testing.assert_allclose(da.liq_price, db.liq_price)
        np.testing.assert_allclose(da.qty, db.qty)
