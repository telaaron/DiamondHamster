from pathlib import Path

import numpy as np
import pytest

from diamondhamster.liq.margin import liq_price_cross, liq_price_isolated, load_tiers, tier_for

TIERS_PATH = Path(__file__).parents[2] / "src/diamondhamster/liq/tiers/illustrativ.toml"


def test_long_short_isolated_by_hand():
    assert liq_price_isolated("long", 100.0, 10, 0.004, 0.0, 1.0) == pytest.approx(90.0 / 0.996)
    assert liq_price_isolated("short", 100.0, 10, 0.004, 0.0, 1.0) == pytest.approx(110.0 / 1.004)


def test_maint_amount_moves_liq_away():
    a = liq_price_isolated("long", 100.0, 20, 0.01, 0.0, 1.0)
    b = liq_price_isolated("long", 100.0, 20, 0.01, 5.0, 1.0)
    assert b < a  # Wartungsbetrag senkt die nötige Marge, Long-Liq rückt weiter weg
    s0 = liq_price_isolated("short", 100.0, 20, 0.01, 0.0, 1.0)
    s1 = liq_price_isolated("short", 100.0, 20, 0.01, 5.0, 1.0)
    assert s1 > s0


def test_cross_is_farther():
    iso = liq_price_isolated("long", 100.0, 10, 0.004, 0.0, 1.0)
    assert liq_price_cross("long", 100.0, iso, 2.0) == pytest.approx(100 - 2 * (100 - iso))
    assert liq_price_cross("long", 100.0, 1.0, 5.0) > 0
    iso_s = liq_price_isolated("short", 100.0, 10, 0.004, 0.0, 1.0)
    assert liq_price_cross("short", 100.0, iso_s, 2.0) == pytest.approx(100 + 2 * (iso_s - 100))


def test_tier_lookup_vectorized():
    tiers = load_tiers(TIERS_PATH)
    lev, mmr, k = tier_for(tiers, np.array([1_000, 50_000, 60_000, 1e9]))
    assert list(lev) == [125, 125, 100, 20] and mmr[-1] == 0.025 and k[2] == 50
