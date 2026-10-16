import numpy as np
import pytest

from diamondhamster.liq.grid import Grid


def test_roundtrip_center_maps_to_own_bucket():
    g = Grid(60_000, 10)
    i = np.arange(g.n)
    assert (g.index(g.centers()) == i).all()


def test_range_and_clip():
    g = Grid(100, 10)
    assert g.edges[0] == pytest.approx(25) and g.edges[-1] >= 400
    assert g.index(1.0) == 0 and g.index(10_000) == g.n - 1
    assert not g.in_range(10_000) and g.in_range(100)


def test_bucket_width_is_10bp():
    g = Grid(100, 10)
    assert g.edges[1] / g.edges[0] == pytest.approx(1.001)


def test_shift_buckets():
    assert Grid(100, 10).shift_buckets(0.0031) == 3
