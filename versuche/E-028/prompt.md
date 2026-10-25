# T-001 baseline trader prompt

You decide the position for an asset over the next week: a number from 0 (flat) to 1 (fully long).
Horizon is weeks to months; you do not need to trade often.

Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
Each window starts with one line `dollar index 4w C%, 13w C%, pct P` (or `dollar index not available`): the change of the US dollar index, which tracks the dollar against a basket of major currencies, over the last 4 and the last 13 weeks, rounded to 0.5 percent, and the percentile from 0 to 100 of its latest close among its daily closes over the last 180 days, all measured up to the day before the decision day. The line is market-wide and identical in every window; it gauges whether the dollar has been strengthening or weakening against other currencies.
Judge every window on its own. Do not compare windows with each other.

Before the weights, write out your analysis:
1. Strategy: in 2 to 3 sentences, the rule you will apply to every window.
2. Then for each window, under its id: your read of the market (trend, structure, key levels as prices on the 100 scale), your weight and why, and the price on the 100 scale that would make you change your mind.
3. End with one JSON object mapping each window id to its weight, e.g. {"a1b2c3d4e5": 0.0, "f6a7b8c9d0": 1.0}. Nothing after it.
