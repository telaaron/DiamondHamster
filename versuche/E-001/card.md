# E-001: T-002: plus eine Zeile mit 19 Indikatoren

- Achse: daten
- Basis: E-000
- Daten: indicators, 180 Tage
- Modell: claude-opus-5-5

## Änderung zum Prompt der Basis
```diff
--- E-000
+++ E-001
@@ -1,9 +1,22 @@
-# T-001 baseline trader prompt
+# T-002 trader prompt: T-001 plus indicators
 
 You decide the position for an asset over the next week: a number from 0 (flat) to 1 (fully long).
 Horizon is weeks to months; you do not need to trade often.
 
-Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
+Each window starts with one `indicators` line computed on the decision day's close, then daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
+
+Indicators (percent values are in %):
+- ret_7d_%, ret_30d_%: price change over 7 and 30 days
+- dist_ema20/50/200_%: close vs exponential moving average
+- rsi14, stoch_rsi (0..1), macd_hist_% (MACD histogram as % of price)
+- bollinger_pos (0 = middle band, +1/-1 = upper/lower band), bollinger_width_%
+- atr14_% (average daily range), adx14 (trend strength)
+- dist_vwap30_% (close vs 30-day volume-weighted price)
+- pos_in_180d_range (0 = 180-day low, 1 = 180-day high)
+- dist_gauss144_%, gauss144_slope5d_% (Gaussian channel midline and its slope)
+- rsi_divergence (+1 bullish, -1 bearish, 0 none)
+- dist_90d_high_%, dist_90d_low_%
+
 Judge every window on its own. Do not compare windows with each other.
 
 Answer with one JSON object only, mapping each window id to its weight, e.g. {"a1b2c3d4e5": 0.0, "f6a7b8c9d0": 1.0}.
```

## Prompt
```
# T-002 trader prompt: T-001 plus indicators

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

Answer with one JSON object only, mapping each window id to its weight, e.g. {"a1b2c3d4e5": 0.0, "f6a7b8c9d0": 1.0}.
```

## Bewertung gegen E-000

| Coins | Wochen | Entscheidungen | Timing-Wert/Woche | Basis | Differenz | t | ohne beste Woche | Wochen besser | Exposure | Rank-IC |
|---|---|---|---|---|---|---|---|---|---|---|
| A (10) | 13 | 130 | -0.12 % | -0.235 % | 0.116 % | 1.69 | 0.083 % (ohne 2026-08-30) | 9/13 | 0.363 (Basis 0.453) | 0.066 |
| B+C (20) | 13 | 260 | -0.367 % | -0.304 % | -0.063 % | -0.37 | -0.159 % (ohne 2026-09-13) | 7/13 | 0.313 (Basis 0.373) | -0.041 |

**Urteil: kein messbarer Unterschied**

Verbrauch: 39 Claude-Aufrufe, 2503k Zeichen, Listenpreis 14.81 USD (zählt gegen Aarons Limit, keine Rechnung)

## Was die KI gedacht hat (Beispiel: Entscheidung 2026-07-05)

Alle Wochen: [denken.md](denken.md)

````
{"0207350180 (LTC)": 0.3, "5d779f862f (ETH)": 0.3, "5ba5d8eaec (DOT)": 0.15, "55bdd79730 (XRP)": 0.3, "2302c8a053 (LINK)": 0.3, "9c40dd1628 (DOGE)": 0.2, "8076a6a2c4 (SOL)": 0.5, "0bb3857620 (ADA)": 0.3, "04d0049266 (AVAX)": 0.25, "66dec9e640 (BTC)": 0.3}
````

## Notizen
Identisch mit dem Turnier-Prompt T-002 (Hash 0f0b64ac31a8). Wiederholt den Dev-Test von T-002 ohne den Überlappungs-Leak und auf 30 statt 2 Coins.
