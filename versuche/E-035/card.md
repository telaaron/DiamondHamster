# E-035: Nur die Indikatorzeile (19 Kennzahlen, Formatsatz und Legende aus E-001/E-034) je Fenster, keine Kerzentabelle

- Achse: format
- Basis: E-003M
- Daten: custom, 180 Tage
- Modell: claude-opus-5-5
- Werkzeug: f2794e9 versuche.py@764f343a01
- Thread: https://claude.ai/code/project/chan_01VH1Un8SQtbifKwzD9jDguD?thread=cmsg_01VH1Un8SQtbifKwzD9jDguD7iZtYV9srWQunhgUZLBZV6

## Änderung zum Prompt der Basis
```diff
--- E-003M
+++ E-035
@@ -3,7 +3,20 @@
 You decide the position for an asset over the next week: a number from 0 (flat) to 1 (fully long).
 Horizon is weeks to months; you do not need to trade often.
 
-Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
+Each window is one `indicators` line computed on the decision day's close. Prices are on a scale where the decision day's close is 100.
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
 
 Before the weights, write out your analysis:
```

## Prompt
```
# T-001 baseline trader prompt

You decide the position for an asset over the next week: a number from 0 (flat) to 1 (fully long).
Horizon is weeks to months; you do not need to trade often.

Each window is one `indicators` line computed on the decision day's close. Prices are on a scale where the decision day's close is 100.

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
```

## Datenaufbereitung (render.py)
```python
"""E-035: only the indicator line of the decision day, no candle table (backlog #10)."""
from diamondhamster import features, snapshot


def render(df, lookback):
    return snapshot.snapshot(features.compute(df), df.index[-1])
```

## Bewertung gegen E-003M

| Coins | Wochen | Entscheidungen | Timing-Wert/Woche | Basis | Differenz | t | ohne beste Woche | Wochen besser | Exposure | Rank-IC |
|---|---|---|---|---|---|---|---|---|---|---|
| A (10) | 13 | 130 | -0.26 % | -0.244 % | -0.016 % | -0.12 | -0.063 % (ohne 2026-09-13) | 6/13 | 0.339 (Basis 0.463) | 0.076 |

**Urteil: kein messbarer Unterschied**

Verbrauch: 13 Claude-Aufrufe, 72k Zeichen, Listenpreis 1.33 USD (zählt gegen Aarons Limit, keine Rechnung)

## Was die KI gedacht hat (Beispiel: Entscheidung 2026-07-05)

Alle Wochen: [denken.md](denken.md)

````
## 1. Strategy

I size exposure by long-term trend structure first, using EMA200, the Gaussian midline slope and position in the 180-day range. Then I adjust by whether price has reclaimed EMA50.

- **Below EMA50 in a falling long-term trend:** a short-term bounce gets at most 0.1–0.2.
- **Near or reclaiming EMA50:** 0.25–0.3.
- **Above EMA20, EMA50 and the Gaussian midline:** up to 0.5.

Full exposure needs price back above EMA200 with a rising Gaussian midline.

## 2. Windows

### 2250407a4e (DOT)
- **Read:** Deep downtrend. Price is 42.7% under EMA200 (≈174.5) and sits at 6% of the 180-day range. The Gaussian midline (≈127) is falling fast, and ADX 36.7 says the downtrend is strong. The +8.8% week is a relief bounce that stalled just under EMA20 (≈101.6). EMA50 (≈114) is far overhead, and the 90-day low is ≈90.3.
- **Weight:** 0.1. This is counter-trend with stoch RSI already at 0.97, so there is little room left in the bounce.
- **Change my mind:** a close above 114 (EMA50 reclaimed) raises the weight; a break below 90 takes it to 0.

### ee74e2fb2c (XRP)
- **Read:** Long-term downtrend. EMA200 is ≈129.5 and the Gaussian midline (≈109) is falling. Short term has turned up: price is above EMA20 (≈96.4) and VWAP, MACD histogram is positive, and RSI is 55. Price is testing EMA50 (≈102.5) from below. ADX 22.5 means the trend is weak.
- **Weight:** 0.25. The bounce is constructive but hasn't cleared EMA50, and stoch RSI at 1.0 is stretched.
- **Change my mind:** above 102.5 I'd go to about 0.4; below 96 I'd go to 0.1.

### af09282c07 (BTC)
- **Read:** Downtrend. EMA200 is ≈118.9, the Gaussian midline ≈110.4 is falling, and ADX 31. Price has bounced above EMA20 (≈98) and is heading toward EMA50 (≈103.4). Bands are tighter (width 12.9%) and volatility is lower. The 90-day low is ≈90.8.
- **Weight:** 0.2. The strong ADX belongs to the prevailing downtrend, and price is still below EMA50.
- **Change my mind:** a close above 103.5 lifts the weight; below 98 cuts it to about 0.05.

### 88dc3ae0d9 (LINK)
- **Read:** Long-term down. EMA200 is ≈125.8 and the Gaussian midline ≈108.3 is falling. Price is up 9.5% over 30 days, above EMA20 (≈96.2) and VWAP, and only 1.5% under EMA50 (≈101.5). The 90-day low is ≈86.7.
- **Weight:** 0.3. This is a reasonable recovery attempt close to reclaiming EMA50.
- **Change my mind:** above 101.5 I'd go to 0.4; below 96 I'd go to 0.1.

### c1928011ff (ADA)
- **Read:** A violent +31.8% week. Price is above the upper Bollinger band (1.02), 13.7% over EMA20 (≈88) and just above EMA50 (≈98.3). It is still far below EMA200 (≈153.6) and the Gaussian midline (≈111), whose slope is steeply negative. ADX 39 shows a strong move, but price is very extended and 14.9% above VWAP. The 90-day low is ≈73.
- **Weight:** 0.25. Momentum is real, but chasing an upper-band blow-off inside a bear trend carries a poor risk/reward.
- **Change my mind:** if price consolidates and holds above 98 I'd add; a fall below 88 means the spike failed, and I'd go to 0.

### 6e321630d1 (LTC)
- **Read:** Downtrend structure. EMA200 is ≈128.5 and the Gaussian midline ≈107.9 is falling. Short term is firm: price is above EMA20 (≈95.9), bollinger_pos is 0.79, ADX 32 and RSI 57. Price is just under EMA50 (≈101.3).
- **Weight:** 0.3. The bounce is constructive and EMA50 is in reach, but this is still below long-term resistance.
- **Change my mind:** above 101.5 I'd go to 0.4; below 96 I'd go to 0.1.

### 74079e2872 (AVAX)
- **Read:** Strong downtrend. Price is 33% under EMA200 (≈150), the Gaussian midline (≈117) is falling at −3.8% per 5 days, and ADX 35.8. The bounce has carried price over EMA20 (≈97.4), but EMA50 (≈106) is still 6% away. The 90-day low is ≈82.
- **Weight:** 0.15. This is counter-trend, with significant overhead resistance.
- **Change my mind:** above 106 raises the weight; below 97 cuts it to 0.05.

### dbf46d879f (SOL)
- **Read:** The strongest of the set. Price is up 28% over 30 days and sits above EMA20 (≈92.3), EMA50 (≈93.5) and the Gaussian midline (≈95.5). The midline slope is still negative but shallow. EMA200 (≈118) and the 90-day high (≈120.6) are the next resistance. Price is somewhat extended, 14.6% above VWAP.
- **Weight:** 0.5. Structure is improving, but this isn't yet a confirmed long-term uptrend, and the extension argues for patience on size.
- **Change my mind:** a loss of 93.5 cuts the weight to 0.2; a close above 118–120 raises it to 0.75 or more.

### 5eb28a66a5 (ETH)
- **Read:** Long-term down. EMA200 is ≈126.6 and the Gaussian midline ≈108.8 is falling. Price is up 13.6% on the week, above EMA20 (≈95) and VWAP, and 1.2% under EMA50 (≈101.2). The 90-day low is ≈84.3.
- **Weight:** 0.3. This is a credible bounce at a key test, while the long-term trend is still negative.
- **Change my mind:** above 101.5 I'd go to 0.4; below 95 I'd go to 0.1.

### 68105f28cd (DOGE)
- **Read:** Strong downtrend. EMA200 is ≈140.4, the Gaussian midline ≈121.5 is falling, and ADX 36.4. The relief bounce is stuck just under EMA20 (≈100.9) and below VWAP. EMA50 (≈110.3) is well above, and the 90-day low is ≈89.3. Stoch RSI at 1.0 suggests the bounce is exhausted.
- **Weight:** 0.1.
- **Change my mind:** above 110 raises the weight; below 89 takes it to 0.

## 3. Weights

{"2250407a4e (DOT)": 0.1, "ee74e2fb2c (XRP)": 0.25, "af09282c07 (BTC)": 0.2, "88dc3ae0d9 (LINK)": 0.3, "c1928011ff (ADA)": 0.25, "6e321630d1 (LTC)": 0.3, "74079e2872 (AVAX)": 0.15, "dbf46d879f (SOL)": 0.5, "5eb28a66a5 (ETH)": 0.3, "68105f28cd (DOGE)": 0.1}
````

## Notizen
Backlog #10. Hypothese: viel weniger Zeichen; zeigt, ob die Rohkerzen ueberhaupt etwas beitragen. Prompt = E-034 (E-003M mit Indikator-Formatsatz und Legende aus E-001), nur der Formatsatz sagt jetzt, dass das Fenster nur aus der Indikatorzeile besteht, plus ein Satz, dass der Schlusskurs des Entscheidungstags 100 ist (damit die Vorlage aus Paragraph 4a mit Preisen auf der 100-Skala sinnvoll bleibt); Vorlage unveraendert. render.py gibt nur snapshot(features.compute(df), t) aus; Indikatoren werden wie bei E-034 aus den Kerzen bis zum Entscheidungstag berechnet. Kein externer Abruf (B-19 entfaellt), keine Harness-Option, versuche.py vom Branch claude/project-thread-lupsy0. Falsifikator (vor dem Lauf festgelegt): die Kerzen tragen etwas bei, wenn E-035 schlechter ist als E-034 (Kerzen + Indikatoren: +0,175 vs E-003M t 1,40, Rank-IC 0,088, partieller Anker 0,67); falsifiziert (Kerzen tragen nichts bei), wenn E-035 auf Timing-Wert UND Rank-IC nicht schlechter ist als E-034. Berichtet: gepaarte Vergleiche gegen E-003M und E-034, Eingabegroesse in Zeichen, partieller Anker (pos_in_180d_range steht in der Zeile), Anteil Gewichtsaenderungen unter 0,15, Umschichtung, Exposure, konstant 0,5. Champion-Regeln B-12/B-13/B-14.

## Zusatzauswertung (Thread)

| Kennzahl | E-035 (nur Indikatoren) | E-034 (Indikatoren + Kerzen) | E-003M (nur Kerzen) |
|---|---|---|---|
| Zeichen je Fenster (Mittel) | 348 | 6.055 | 5.705 |
| Zeichen je Woche, Fenster + Prompt | 3.484 + 1.495 | 60.549 + 1.650 | 57.055 + 942 |
| Timing-Wert/Woche | −0,26 % | −0,07 % | −0,24 % |
| Rank-IC | 0,076 | 0,088 | 0,059 |
| partieller Anker (einfache Korr.) | 0,71 (0,89) | 0,67 (0,88) | 0,40 (0,77) |
| Umschichtung je Coin und Woche | 0,128 | 0,092 | 0,121 |
| Änderungen unter 0,15 | 56 % | 72 % | |
| Gewichte genau 0,0 | 14 | 11 | |
| Exposure | 0,34 | 0,32 | 0,46 |
| gegen konstant 0,5 (%/Woche, t) | −0,78, t −1,09 | −0,63, t −0,90 | |

Gepaart gegen E-034: −0,19 %/Woche, t −2,31, ohne beste Woche −0,23 %, nur 2/13 Wochen besser. Gewichte korrelieren 0,96 mit E-034 (mittlere Abweichung 0,06): dieselbe Regel, aber etwas schlechter getroffen und unruhiger.
Gepaart gegen E-003M: −0,02 %/Woche, t −0,12, 6/13 Wochen besser.

Falsifikator: greift nicht (E-035 ist auf Timing-Wert und Rank-IC schlechter als E-034). Die Kerzen tragen gegenüber der Indikatorzeile allein etwas bei, vor allem Ruhe (Umschichtung 0,092 statt 0,128). Einschränkung: E-034 ist ein einzelner Lauf; derselbe Prompt schwankte bei E-003 zwischen Läufen um 0,1 bis 0,17 %/Woche. Gegen E-003M kein Unterschied, also kein Kandidat (t < 2), keine Wiederholung, kein B+C.

Größte Gewichtsänderungen: BTC 23.08. +0,40 auf 0,55 (Folgewoche −0,1 %); ETH 19.07. +0,40 auf 0,50 (+4,4 %); LTC 19.07. +0,35 auf 0,40 (+1,6 %); LINK 19.07. +0,35 auf 0,45 (+5,2 %); XRP 23.08. +0,35 auf 0,40 (−10,7 %); DOGE 27.09. +0,35 auf 0,60 (−1,0 %).
