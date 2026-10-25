# E-034: E-001 mit Analyse: E-003M plus eine Zeile mit 19 Indikatoren je Fenster (Formatsatz und Legende aus E-001/prompt.md)

- Achse: daten
- Basis: E-003M
- Daten: indicators, 180 Tage
- Modell: claude-opus-5-5
- Werkzeug: f2794e9 versuche.py@764f343a01
- Thread: https://claude.ai/code/project/chan_01VH1Un8SQtbifKwzD9jDguD?thread=cmsg_01VH1Un8SQtbifKwzD9jDguDB5ePCgT1XjDU5TihTiVgug

## Änderung zum Prompt der Basis
```diff
--- E-003M
+++ E-034
@@ -3,7 +3,20 @@
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
 
 Before the weights, write out your analysis:
```

## Prompt
```
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
```

## Bewertung gegen E-003M

| Coins | Wochen | Entscheidungen | Timing-Wert/Woche | Basis | Differenz | t | ohne beste Woche | Wochen besser | Exposure | Rank-IC |
|---|---|---|---|---|---|---|---|---|---|---|
| A (10) | 13 | 130 | -0.069 % | -0.244 % | 0.175 % | 1.4 | 0.086 % (ohne 2026-09-13) | 10/13 | 0.324 (Basis 0.463) | 0.088 |

**Urteil: kein messbarer Unterschied**

Verbrauch: 13 Claude-Aufrufe, 839k Zeichen, Listenpreis 5.67 USD (zählt gegen Aarons Limit, keine Rechnung)

## Was die KI gedacht hat (Beispiel: Entscheidung 2026-07-05)

Alle Wochen: [denken.md](denken.md)

````
**Strategy:** Long-term trend sets the base weight. If price is far below the 200-day EMA and the Gaussian midline is falling, the base is near flat. Short-term strength adds a small amount only when price is near or above the 50-day EMA and is making higher lows. Every window here is a bounce inside a large downtrend, so all weights stay small. The window with the clearest structural repair gets the most.

## be729cc7e6 (DOT)
- **Read:** A severe downtrend from about 250 to about 90, sitting at 6% of its 180-day range. Price is 42.7% below the 200-day EMA, and the Gaussian slope is steeply negative at −3.4%. The last 7 days bounced from 90 to 100, but price is still under the 50-day EMA (about 114). Overhead supply sits at 103–111, where the breakdown happened. Support is at 90–91.
- **Weight:** 0.05. This is a counter-trend bounce with no structural change.
- **Change my mind:** A close above 114 (reclaiming the 50-day EMA) would raise the weight. A break below 90 confirms flat.

## fc5e68cc76 (LINK)
- **Read:** A downtrend with a bounce from 87 to 100. Price is just under the 50-day EMA (about 101.5) and 20.5% below the 200-day EMA, and the Gaussian slope is falling. The 30-day return is positive. Resistance is at 101–107, with the day −20 high at 106.7. Support is at 87.
- **Weight:** 0.15. Momentum is improving, but the primary trend is still down.
- **Change my mind:** A close above 107 would raise the weight. A close below 87 would take it to 0.

## e2ea539810 (SOL)
- **Read:** The strongest structure in this set. The 30-day return is +28%, and price is above both the 50-day EMA (+7%) and the Gaussian midline. Lows are rising: 73.7, then 78.5, then 97.7. Price is still 15.5% below the 200-day EMA (about 118), and the Gaussian slope is negative. Resistance is at 103–107 and then 112–120. Support is at 86–88.
- **Weight:** 0.35. This is a genuine repair, but it is not yet a confirmed uptrend.
- **Change my mind:** A close above 107 would raise the weight. A close below 86 would cut it to about 0.1.

## 2b11dd5516 (DOGE)
- **Read:** A deep downtrend at 10% of its 180-day range. Price is below the 50-day EMA (about 110) and 28.8% below the 200-day EMA. ADX is 36, meaning a strong trend, and here that trend is down. The bounce from 89 to 100 is running into the 101–110 breakdown zone. Support is at 89–92.
- **Weight:** 0.05.
- **Change my mind:** A close above 111 would raise the weight. A break below 89 confirms flat.

## 4bd18fb5a0 (LTC)
- **Read:** A downtrend with a bounce from 86 to 100. Price is right at the 50-day EMA (about 101.3) and at the upper half of the Bollinger band. The latest low at 85.7 was lower than the low near 88. Resistance is at 101 and 106. Support is at 86–89.
- **Weight:** 0.15.
- **Change my mind:** A close above 106 would raise the weight. A close below 89 would cut it.

## 2bd805f85f (BTC)
- **Read:** A quieter downtrend with ATR at 3.4%. The low at 90.8 was below the earlier 92.9, so lows are still falling. Price is under the 50-day EMA (about 103.4). Resistance is at 104–106, and support is at 90–91.
- **Weight:** 0.10.
- **Change my mind:** A close above 106 would raise the weight. A close below 90 would take it to 0.

## 4eaefc5884 (ETH)
- **Read:** A double bottom formed at 84.3 and 84.7. Price is up 13.6% over 7 days and sits just under the 50-day EMA (about 101.2). The 200-day EMA is 21% above price, and the Gaussian slope is −3%. Resistance is at 103.6, the day −20 high. Support is at 84–88.
- **Weight:** 0.20. The defined base helps, but the trend is still down.
- **Change my mind:** A close above 104 would raise the weight. A close below 84 would take it to 0.

## e5b850c03b (XRP)
- **Read:** The low at 87.2 was below the earlier 90.7. Price bounced to 100 and is under the 50-day EMA (about 102.5). Resistance is at 102–112, with the day −20 spike high at 111.8. Support is at 87.
- **Weight:** 0.10.
- **Change my mind:** A close above 108 would raise the weight. A close below 87 would take it to 0.

## 0447f3e84d (ADA)
- **Read:** A vertical V-shaped rebound of +31.8% in 7 days on heavy volume. Price is at the upper Bollinger band and 13.7% above the 20-day EMA, which is overextended. Price is 34.9% below the 200-day EMA, and the Gaussian slope is the steepest down here at −4.7%. The rebound is pushing into the 95–105 breakdown shelf. The low at 72.9 was below the earlier 78.4.
- **Weight:** 0.10. A chase entry like this has a high risk of retracing.
- **Change my mind:** Holding above 105 or a close above 112 would raise the weight. A close below 85 would take it to 0.

## c783d8e6e5 (AVAX)
- **Read:** A capitulation low at 82 on day −16, followed by higher lows at 86 and then 92. Price is still 5.7% below the 50-day EMA (about 106) and 33% below the 200-day EMA. ADX is 36 within the downtrend. Resistance is at 102–106, and support is at 86.
- **Weight:** 0.10.
- **Change my mind:** A close above 107 would raise the weight. A close below 85 would take it to 0.

{"be729cc7e6 (DOT)": 0.05, "fc5e68cc76 (LINK)": 0.15, "e2ea539810 (SOL)": 0.35, "2b11dd5516 (DOGE)": 0.05, "4bd18fb5a0 (LTC)": 0.15, "2bd805f85f (BTC)": 0.1, "4eaefc5884 (ETH)": 0.2, "e5b850c03b (XRP)": 0.1, "0447f3e84d (ADA)": 0.1, "c783d8e6e5 (AVAX)": 0.1}
````

## Notizen
Backlog #18. Hypothese: ohne Analyse (E-001) kein messbarer Unterschied; mit der Pflicht-Analyse kann die KI die Kennzahlen anders nutzen. Einzige Aenderung gegen E-003M: der Satz zum Datenformat wird durch den aus E-001 ersetzt und die Indikator-Legende aus E-001 eingefuegt; Vorlage aus Paragraph 4a unveraendert. Falsifikator (vor dem Lauf festgelegt): falsifiziert, ausser der Timing-Wert liegt ueber E-003M UND der Rank-IC steigt ueber E-003M (0,059). Weil pos_in_180d_range selbst in der Indikatorzeile steht, wird zusaetzlich berichtet: partieller Anker (E-003M 0,40) und ob die Gewichte pos_in_180d_range enger folgen als bei E-003M (einfache und partielle Korrelation). Ausserdem: Anteil Gewichtsaenderungen unter 0,15, Umschichtung (E-003M 0,121), Exposure, Vergleich mit konstant 0,5. Champion-Regeln B-12/B-13/B-14: bei t >= 2 genau eine Wiederholung auf A, Urteil auf dem Mittel; B+C nur dann. Keine Harness-Option; kein externer Abruf (B-19 entfaellt); versuche.py vom Branch claude/project-thread-lupsy0.

## Auswertung (Thread)

- Änderung: E-003M plus eine `indicators`-Zeile mit 19 Kennzahlen je Fenster (Formatsatz und Legende aus E-001/prompt.md). Vorlage aus §4a unverändert, Titelzeile unverändert.
- Falsifikator (vor dem Lauf): falsifiziert, außer Timing-Wert über E-003M UND Rank-IC über 0,059. Timing-Wert +0,175 %/Woche gegen E-003M (t 1,40, ohne beste Woche +0,086 %, 10/13 Wochen besser), Rank-IC 0,088: **nicht falsifiziert, aber nicht belegt** (t < 2). Keine Wiederholung, kein B+C, Champion bleibt E-003M.
- Anker: partieller Anker 0,67 (E-003M 0,40; bisher höchster Wert, Spanne sonst 0,19 bis 0,48), einfache Korrelation Gewicht ~ Spannenlage 0,88 (E-003M 0,77). Die KI folgt pos_in_180d_range also deutlich enger als E-003M; mit der Zahl vor Augen wird sie noch stärker zum Spannen-Folger.
- Exposure 0,32 (E-003M 0,46), 11 Gewichte 0,0 (E-003-Läufe 0). Woche 1 alle Fenster 0,05 bis 0,35: die KI liest die Abstände zur 200-Tage-EMA und die Gauß-Steigung als Abwärtstrend und bleibt klein.
- Umschichtung 0,100 (E-003M 0,121; E-003-Läufe 0,118 / 0,120 / 0,154). Anteil Gewichtsänderungen unter 0,15: 72 % (E-003-Läufe 63 / 61 / 52 %). Größte Änderungen: BTC +0,35 (08-23), SOL +0,35 (08-30), LTC +0,30 (07-19 und 08-23), LINK +0,30 (07-19), ADA +0,30 (09-27).
- Gegen eine konstante Position 0,5 (gleiche Kosten): −0,64 %/Woche, t −0,91, 7/13 Wochen besser (E-003-Läufe −0,25 / −0,36 / −0,37). Der Abstand kommt vor allem aus der niedrigen Exposure in einem steigenden Quartal; der Timing-Wert ist exposure-neutral.
- Lesart: ruhiger (wie E-017/E-019/E-027) und leicht treffsicherer im Ranking, aber stärker am Spannen-Anker. Ohne Analyse (E-001) war es auf A +0,12 t 1,7, also dieselbe Größenordnung; die Analyse ändert am Effekt der Indikatoren nichts Messbares.
