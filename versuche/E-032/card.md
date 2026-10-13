# E-032: Ruhe-Satz aus E-002 (mittleres Gewicht um 0,5 als Standard, Abweichung nur bei klarer Evidenz, jede Umschichtung kostet) nach der Horizont-Zeile eingefuegt, Vorlage aus Paragraph 4a unveraendert

- Achse: prompt
- Basis: E-003M
- Daten: candles, 180 Tage
- Modell: claude-opus-5-5
- Werkzeug: f2794e9 versuche.py@764f343a01
- Thread: https://claude.ai/code/project/chan_01VH1Un8SQtbifKwzD9jDguD?thread=cmsg_01VH1Un8SQtbifKwzD9jDguDBapVnaA5CTC7fjGMempUTr

## Änderung zum Prompt der Basis
```diff
--- E-003M
+++ E-032
@@ -2,6 +2,7 @@
 
 You decide the position for an asset over the next week: a number from 0 (flat) to 1 (fully long).
 Horizon is weeks to months; you do not need to trade often.
+Calm is the default: hold a steady middle weight (around 0.5) and move away from it only on clear evidence. Every change in weight costs money, and small moves on weak signals lose more than they gain.
 
 Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
 Judge every window on its own. Do not compare windows with each other.
```

## Prompt
```
# T-001 baseline trader prompt

You decide the position for an asset over the next week: a number from 0 (flat) to 1 (fully long).
Horizon is weeks to months; you do not need to trade often.
Calm is the default: hold a steady middle weight (around 0.5) and move away from it only on clear evidence. Every change in weight costs money, and small moves on weak signals lose more than they gain.

Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
Judge every window on its own. Do not compare windows with each other.

Before the weights, write out your analysis:
1. Strategy: in 2 to 3 sentences, the rule you will apply to every window.
2. Then for each window, under its id: your read of the market (trend, structure, key levels as prices on the 100 scale), your weight and why, and the price on the 100 scale that would make you change your mind.
3. End with one JSON object mapping each window id to its weight, e.g. {"a1b2c3d4e5": 0.0, "f6a7b8c9d0": 1.0}. Nothing after it.
```

## Bewertung gegen E-003M

| Coins | Wochen | Entscheidungen | Timing-Wert/Woche | Basis | Differenz | t | ohne beste Woche | Wochen besser | Exposure | Rank-IC |
|---|---|---|---|---|---|---|---|---|---|---|
| A (10) | 13 | 130 | -0.143 % | -0.244 % | 0.102 % | 0.53 | -0.039 % (ohne 2026-08-16) | 8/13 | 0.499 (Basis 0.463) | 0.028 |

**Urteil: kein messbarer Unterschied**

Verbrauch: 13 Claude-Aufrufe, 787k Zeichen, Listenpreis 5.29 USD (zählt gegen Aarons Limit, keine Rechnung)

## Was die KI gedacht hat (Beispiel: Entscheidung 2026-07-05)

Alle Wochen: [denken.md](denken.md)

````
**Strategy:** Start from a neutral 0.5. Cut toward 0.4 when the 180-day trend is clearly down and the latest bounce came off a *lower* low that is still under resistance. Edge toward 0.55 only when the recent lows are holding or rising and price has cleared the last swing high. All of these windows have been falling for months, so no window gets much above neutral and none goes flat on a bounce alone.

### fc11a02940 (BTC)
- **Read:** Long downtrend from about 147. The crash low was 92.9 on day -30, and the retest made a slightly lower low at 90.8 on day -4. Price has since bounced to 100 on fading volume, still below the 104–105 swing high from day -20. The broader structure is lower highs (the 130 peak, then 120s, now 100s).
- **Weight:** 0.4. This is a bounce inside a downtrend, with the low not confirmed as holding.
- **Change mind:** A close above 105 brings it back to 0.5. A close below 90.5 cuts it to 0.25.

### 576cc3dc0f (DOT)
- **Read:** Steep decline from about 250. The day -29 low of 100.3 gave way to a lower low at 90.2 on day -7. The rebound to 100 is back into old support from days -24 to -15 (about 104–115), which should now act as resistance.
- **Weight:** 0.4. The trend is down and the most recent low was a lower one.
- **Change mind:** Above 108 → 0.5. Below 90 → 0.25.

### 2cf58f83f2 (DOGE)
- **Read:** Down from about 190. The low was 99.7 on day -29, then a lower low at 89.3 on day -5. Price has bounced to 100. Resistance sits at 110–114, and the 128–130 range from days -40 to -34 is far above.
- **Weight:** 0.4.
- **Change mind:** Above 106 → 0.5. Below 89 → 0.25.

### 630aab2692 (ETH)
- **Read:** Down from about 185. There is a double bottom at 84.3 (day -29) and 84.7 (day -10), so the low held. A three-day rally took price to 100 on above-average volume (0.99 on day 0), just under the day -20 high of 103.6.
- **Weight:** 0.5. The base is holding, but the long-term trend is still down.
- **Change mind:** A close above 104 → 0.6. Below 87 → 0.35.

### 377093ae13 (ADA)
- **Read:** A capitulation drop from about 132 to 82.7 on days -33 to -30. That was followed by a lower low at 72.9 on day -10. Then came a violent V-reversal on heavy volume (about 2.1 on days -2 and -1), from 76 to 105.5. Price now sits at 100, above the 100.3 high from day -20. The move is strong but overextended, and the gap zone around 85–95 is unfilled.
- **Weight:** 0.5. The breakout is real, but the volatility and extension argue against adding.
- **Change mind:** Holding above 106 → 0.6. Below 90 → 0.35.

### 02b15ab883 (LINK)
- **Read:** Down from about 170. There is a double bottom at 86.8 (day -29) and 86.9 (day -10). Price has bounced to 100, with resistance at the day -20 high of 106.7 and the 112–121 range above that. Volume on the bounce is light.
- **Weight:** 0.5. The base is holding but resistance has not been cleared.
- **Change mind:** Above 107 → 0.6. Below 87 → 0.35.

### cdb771465a (AVAX)
- **Read:** Down from about 210. A capitulation low of 82.0 on day -16 came on 3x volume. Since then the lows have been rising: about 86, then 91.5, then 92. Price at 100 is now just under the day -20 high of 102.2 and day -1 high of 102.8.
- **Weight:** 0.5. The short-term structure is improving, but the window is still in a downtrend.
- **Change mind:** A close above 103 → 0.6. Below 91.5 → 0.35.

### 09de82b4ac (XRP)
- **Read:** Down from about 199. The day -29 low of 90.7 was followed by a lower low at 87.2 on day -9. Price has bounced to 100. Resistance is at 107 and then 111.8, the day -20 spike.
- **Weight:** 0.45.
- **Change mind:** Above 107 → 0.55. Below 88 → 0.3.

### c62c01256f (SOL)
- **Read:** Down from about 173. The low was 73.7 on day -29, then a higher low at 78.5 on day -10. Price then rallied to 100–103, clearing the day -20 high of 93.3, so the short-term pattern is higher highs and higher lows. Overhead, the 100–107 congestion from days -50 to -34 is resistance.
- **Weight:** 0.55. This has the cleanest short-term reversal of the set.
- **Change mind:** Above 107 → 0.65. Below 92 → 0.4.

### 5a7b735e48 (LTC)
- **Read:** Down from about 183. The low was 88.4 on day -29, then a slightly lower low at 85.7 on day -10. Price is now back at 100, roughly level with the day -20 high of about 101. Resistance is at 101 and then the 113–118 shelf.
- **Weight:** 0.45.
- **Change mind:** A close above 102 → 0.55. Below 89 → 0.3.

{"fc11a02940 (BTC)": 0.4, "576cc3dc0f (DOT)": 0.4, "2cf58f83f2 (DOGE)": 0.4, "630aab2692 (ETH)": 0.5, "377093ae13 (ADA)": 0.5, "02b15ab883 (LINK)": 0.5, "cdb771465a (AVAX)": 0.5, "09de82b4ac (XRP)": 0.45, "c62c01256f (SOL)": 0.55, "5a7b735e48 (LTC)": 0.45}
````

## Notizen
Backlog #19 (E-002 mit Analyse, Basis E-003 = E-003M). Hypothese: ohne Analyse brachte der Ruhe-Satz weniger Streuung, aber keinen Timing-Gewinn; mit Pflicht-Analyse koennte die weichere Ruhe-Regel die teure Umschichtung senken, ohne wie E-031 (hartes Band 0,25 bis 0,75) auf konstant 0,5 zu kollabieren. Falsifikator (vor dem Lauf festgelegt, Standard aus dem Auftrag): falsifiziert, ausser der Timing-Wert liegt ueber E-003M (Differenz > 0) UND die Umschichtung liegt unter E-003M (0,121, mittlere absolute Gewichtsaenderung je Coin und Woche). Zusaetzlich berichtet: partieller Anker (werkzeuge/anker.py, E-003M 0,40), Anteil Gewichtsaenderungen unter 0,15, Exposure, Rank-IC, Vergleich mit E-031 und mit einer konstanten Position 0,5 (gleiche Kosten 0,2 % je Umschichtung, Differenz mit t-Wert). Champion-Regeln B-12/B-13/B-14: bei t >= 2 genau eine Wiederholung auf A, Urteil auf dem Mittel; B+C nur dann. Keine Harness-Option; versuche.py vom Branch claude/project-thread-lupsy0 (README par. 4). Vorlage aus Paragraph 4a woertlich unveraendert.

## Auswertung (Thread)

- Falsifikator (vor dem Lauf): falsifiziert, außer der Timing-Wert liegt über E-003M und die Umschichtung unter E-003M. Timing-Wert +0,10 %/Woche gegen E-003M (t 0,53), Umschichtung 0,055 (E-003M 0,121, gleiche Rechnung über 130 Entscheidungen): **nicht falsifiziert, aber nicht belegt**. Der Vorsprung hängt an Woche 2026-08-16 (ohne sie −0,04 %), t < 2.
- Partieller Anker 0,34 (E-003M 0,40, E-031 0,24), einfache Korrelation zur Spannenlage 0,63.
- Ruhe ohne Band: Gewichte 0,30 bis 0,70 (nie außerhalb ±0,2 um 0,5), 41 von 130 genau 0,5 (E-031: 20). Anteil Gewichtsänderungen unter 0,15: 90 % (E-031 85 %, E-003-Läufe 63 / 61 / 52 %); 32 von 120 Änderungen sind null. Größte Änderungen ±0,20 (DOT 09-06, 09-13, 09-20).
- Gegen E-031 (hartes Band): −0,03 %/Woche, t −0,35, 9/13 Wochen besser. Kein messbarer Unterschied zwischen weicher und harter Ruhe-Regel.
- Gegen eine konstante Position 0,5 (gleiche Kosten 0,2 % je Umschichtung): −0,12 %/Woche, t −0,84, 6/13 Wochen besser (E-031 −0,01; E-003-Läufe −0,25 / −0,36 / −0,37). Die Regel halbiert die Umschichtung, aber die verbleibenden Abweichungen von 0,5 kosten noch.
- Rank-IC 0,028 (E-003M 0,059), Exposure 0,50 (0,46).
- Keine Wiederholung (t < 2), kein B+C. Champion bleibt E-003M.
