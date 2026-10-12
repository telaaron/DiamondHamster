# E-005: returns instead of prices

You decide the position for an asset over the next week: a number from 0 (flat) to 1 (fully long).
Horizon is weeks to months; you do not need to trade often.

Each window is the last 180 days, one line per day: `day ret range v`. Day 0 is the decision day, -1 the day before; ret is the close-to-close change in % against the previous day; range is high minus low in % of the previous close; volume is relative to the window average. There are no price levels.
Judge every window on its own. Do not compare windows with each other.

Before the weights, write out your analysis:
1. Strategy: in 2 to 3 sentences, the rule you will apply to every window.
2. Then for each window, under its id: your read of the market (trend, structure, key levels as % from the last close), your weight and why, and the move from the last close, in %, that would make you change your mind.
3. End with one JSON object mapping each window id to its weight, e.g. {"a1b2c3d4e5": 0.0, "f6a7b8c9d0": 1.0}. Nothing after it.
