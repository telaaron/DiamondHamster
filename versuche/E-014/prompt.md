# T-001 baseline trader prompt, veto role

You check the position a fixed rule sets for an asset over the next week. The rule: invested (weight 1) when the close is above its 50-day average, otherwise flat (weight 0). The first line of each window shows the rule's signal for today.
You may only confirm the signal or veto it: if the signal is 1, your weight is 1 (confirm) or 0 (veto, you judge it a false signal); if the signal is 0, your weight is 0. No other weights.
Horizon is weeks to months; you do not need to trade often.

Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
Judge every window on its own. Do not compare windows with each other.

Before the weights, write out your analysis:
1. Strategy: in 2 to 3 sentences, the rule you will apply to every window.
2. Then for each window, under its id: your read of the market (trend, structure, key levels as prices on the 100 scale), your weight and why, and the price on the 100 scale that would make you change your mind.
3. End with one JSON object mapping each window id to its weight, e.g. {"a1b2c3d4e5": 0.0, "f6a7b8c9d0": 1.0}. Nothing after it.
