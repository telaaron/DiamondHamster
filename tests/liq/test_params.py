import shutil

import numpy as np
import pytest

from diamondhamster.liq import params as P
from diamondhamster.liq.params import load_params, size_class, with_overrides


def test_defaults_loaded():
    p = load_params()
    assert (p.bucket_bp, p.alpha, p.cross_share, p.cross_kappa, p.beta) == (10, 0.5, 0.3, 2.0, 0.0)
    assert (p.max_cohorts, p.warmup_days, p.drift_warn, p.cluster_min_share, p.top_n) == (90, 14, 0.05, 0.002, 10)
    assert set(p.leverage_weights) == {"small", "mid", "large"}
    assert all(w.sum() == pytest.approx(1) and len(w) == len(P.LEVERAGES) for w in p.leverage_weights.values())
    assert len(p.tiers) == 4 and len(p.params_hash) == 16


def test_size_class_thresholds():
    assert list(size_class(np.array([9_999, 10_000, 999_999, 1_000_000]))) == ["small", "mid", "mid", "large"]


def test_hash_changes_with_file(tmp_path):
    src = P.DEFAULT_PARAMS_PATH
    shutil.copytree(src.parent.parent / "tiers", tmp_path / "tiers")
    (tmp_path / "params").mkdir()
    dst = tmp_path / "params" / "v002.toml"
    dst.write_text(src.read_text().replace("alpha = 0.5", "alpha = 0.6"))
    p2 = load_params(dst)
    assert p2.alpha == 0.6 and p2.params_hash != load_params().params_hash


def test_with_overrides_marks_hash():
    p = with_overrides(load_params(), alpha=0.0)
    assert p.alpha == 0.0 and p.params_hash.endswith("+override")


def test_override_hash_depends_on_values():
    from diamondhamster.liq.baseline import baseline_params
    from diamondhamster.liq.sim import DEFAULT_TRUTH, truth_params
    base = load_params()
    assert baseline_params(base).params_hash != truth_params(base, DEFAULT_TRUTH).params_hash
    assert with_overrides(base, alpha=0.1).params_hash != with_overrides(base, alpha=0.2).params_hash


def test_negative_weight_rejected(tmp_path):
    src = P.DEFAULT_PARAMS_PATH
    shutil.copytree(src.parent.parent / "tiers", tmp_path / "tiers")
    (tmp_path / "params").mkdir()
    dst = tmp_path / "params" / "neg.toml"
    dst.write_text(src.read_text().replace("small = [2, 3,", "small = [-2, 3,"))
    with pytest.raises(ValueError, match="non-negative"):
        load_params(dst)
