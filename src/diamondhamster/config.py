"""Fixed research periods. Changing these after results are seen invalidates earlier experiments."""

import pandas as pd

IN_SAMPLE_END = pd.Timestamp("2022-12-31", tz="UTC")
VALIDATION_START = pd.Timestamp("2023-01-01", tz="UTC")
VALIDATION_END = pd.Timestamp("2024-12-31", tz="UTC")
HOLDOUT_START = pd.Timestamp("2025-01-01", tz="UTC")

# Round-trip friction is 2x this: fees plus slippage, deliberately conservative.
COST_PER_SIDE = 0.002

# Labelled after the fact, used only to split results; never as a signal input.
REGIMES = {
    "bull_2017": ("2017-01-01", "2017-12-17"),
    "bear_2018": ("2017-12-18", "2018-12-15"),
    "side_2019": ("2018-12-16", "2020-03-31"),
    "bull_2020_21": ("2020-04-01", "2021-11-10"),
    "bear_2022": ("2021-11-11", "2022-12-31"),
}
