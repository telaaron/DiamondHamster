# T-001 baseline trader prompt

You decide the position for an asset over the next week: a number from 0 (flat) to 1 (fully long).
Horizon is weeks to months; you do not need to trade often.

Each window starts with one `indicators` line computed on the decision day's close, then daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.

Indicators (percent values are in %):
- ret_7d_%, ret_30d_%: price change over 7 and 30 days
- dist_ema20/50/200_%: close vs exponential moving average
- rsi14, stoch_rsi (0..1), macd_hist_% (MACD histogram as % of price)
- bollinger_pos (0 = middle band, +1/-1 = upper/lower band), bollinger_width_%
- atr14_% (average daily range), adx14 (trend strength)
- dist_vwap30_% (close vs 30-day volume-weighted price)
- pos_in_180d_range (0 = 180-day low, 1 = 180-day high)
- dist_gauss144_%, gauss144_slope5d_% (Gaussian channel midline and its slope)
- rsi_divergence (+1 bullish, -1 bearish, 0 none)
- dist_90d_high_%, dist_90d_low_%

Judge every window on its own. Do not compare windows with each other.

Before the weights, write out your analysis:
1. Strategy: in 2 to 3 sentences, the rule you will apply to every window.
2. Then for each window, under its id: your read of the market (trend, structure, key levels as prices on the 100 scale), your weight and why, and the price on the 100 scale that would make you change your mind.
3. End with one JSON object mapping each window id to its weight, e.g. {"a1b2c3d4e5": 0.0, "f6a7b8c9d0": 1.0}. Nothing after it.
