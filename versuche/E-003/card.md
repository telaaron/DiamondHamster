# E-003: Sichtbares Denken: erst Strategie, dann pro Fenster Marktlesart, Gewicht mit Begründung und Kipp-Preis, zuletzt das JSON

- Achse: prompt
- Basis: E-000
- Daten: candles, 180 Tage
- Modell: claude-opus-5-5
- Thread: https://claude.ai/code/project/chan_01VH1Un8SQtbifKwzD9jDguD?thread=cmsg_01VH1Un8SQtbifKwzD9jDguDPqfqsXbf1uUjcQYGgzfjDy

## Änderung zum Prompt der Basis
```diff
--- E-000
+++ E-003
@@ -6,4 +6,7 @@
 Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
 Judge every window on its own. Do not compare windows with each other.
 
-Answer with one JSON object only, mapping each window id to its weight, e.g. {"a1b2c3d4e5": 0.0, "f6a7b8c9d0": 1.0}.
+Before the weights, write out your analysis:
+1. Strategy: in 2 to 3 sentences, the rule you will apply to every window.
+2. Then for each window, under its id: your read of the market (trend, structure, key levels as prices on the 100 scale), your weight and why, and the price on the 100 scale that would make you change your mind.
+3. End with one JSON object mapping each window id to its weight, e.g. {"a1b2c3d4e5": 0.0, "f6a7b8c9d0": 1.0}. Nothing after it.
```

## Prompt
```
# T-001 baseline trader prompt

You decide the position for an asset over the next week: a number from 0 (flat) to 1 (fully long).
Horizon is weeks to months; you do not need to trade often.

Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
Judge every window on its own. Do not compare windows with each other.

Before the weights, write out your analysis:
1. Strategy: in 2 to 3 sentences, the rule you will apply to every window.
2. Then for each window, under its id: your read of the market (trend, structure, key levels as prices on the 100 scale), your weight and why, and the price on the 100 scale that would make you change your mind.
3. End with one JSON object mapping each window id to its weight, e.g. {"a1b2c3d4e5": 0.0, "f6a7b8c9d0": 1.0}. Nothing after it.
```

## Bewertung gegen E-000

| Coins | Wochen | Entscheidungen | Timing-Wert/Woche | Basis | Differenz | t | ohne beste Woche | Wochen besser | Exposure | Rank-IC |
|---|---|---|---|---|---|---|---|---|---|---|
| A (10) | 13 | 130 | -0.151 % | -0.235 % | 0.084 % | 1.04 | 0.049 % (ohne 2026-09-13) | 9/13 | 0.457 (Basis 0.453) | 0.076 |
| B+C (20) | 13 | 260 | -0.566 % | -0.304 % | -0.262 % | -1.23 | -0.304 % (ohne 2026-09-27) | 6/13 | 0.377 (Basis 0.373) | -0.029 |

**Urteil: kein messbarer Unterschied**

Verbrauch: 39 Claude-Aufrufe, 2351k Zeichen, Listenpreis 16.07 USD (zählt gegen Aarons Limit, keine Rechnung)

## Was die KI gedacht hat (Beispiel: Entscheidung 2026-07-05)

Alle Wochen: [denken.md](denken.md)

````
## Strategy

I follow trend, but give extra weight to swing structure since the last major low. A window earns a meaningful long weight only if it has made a **higher low** after the capitulation drop around days -33 to -29, or broken above the **interim high near day -20**. If it is still making lower lows below a falling lower-high, it stays mostly flat, with only a small allocation for the current bounce. Weights run from about 0.2 (downtrend intact, bounce into resistance) to about 0.65 (higher low plus higher high confirmed).

All ten windows share the same broad shape: a crash around day -150, a recovery to a peak near day -60/-55, a lower high, a sharp drop at days -33 to -30, a second leg into days -10 to -4, and a 4-day bounce back to 100. The difference between them is how the second leg compares with the first low.

---

### 03372af42d (BTC)
- **Read:** The peak was ~130 (day -60), followed by a steady downtrend. The capitulation low was 92.9 (day -30), and the second leg made a **lower low** at 90.8 (day -4). Price has bounced back to 100 on fading volume (0.46). Resistance sits at 103–105.7 (the day -20 high), with 110+ above that.
- **Weight: 0.25.** The lower-low structure is intact, and the bounce is unconfirmed on light volume.
- **Change mind:** A close above 105.7 would raise the weight toward 0.5. A close below 90.8 would take it to 0.

### 7fd1b39af6 (DOGE)
- **Read:** The peak was 152 (day -52), with a capitulation low of 99.7 (day -29). The second leg made a clear **lower low** at 89.3 (day -5). The bounce to 100 is on below-average volume. Resistance is at 105–116.8 (the day -20 high).
- **Weight: 0.2.** This is the weakest structure. The day -29 low has turned into overhead supply right here at ~100–105.
- **Change mind:** Above 106 would raise the weight. Below 89.3 would take it to 0.

### 02c1b54fa0 (ADA)
- **Read:** This one crashed hardest: it went from ~149 to 78.4 (day -29) and then made a lower low of 72.9 (day -10). It then ripped +30% in 4 sessions on heavy volume (2.08 and 2.22) to a high of 105.5, which **took out the day -20 high of 100.3**. Today's pullback to 100 is on lighter volume. That pattern is a high-momentum reversal: a V-bottom followed by a break of the lower-high sequence.
- **Weight: 0.55.** The structure has turned, and volume confirms it. I'm holding back from a larger weight because a vertical move like this can retrace a large part of the gain toward 85–90.
- **Change mind:** Holding above 105.5 would raise the weight to 0.75. A close below 92 means the breakout failed, and the weight goes to 0.15.

### e6c03a9dd9 (XRP)
- **Read:** The peak was ~130 (day -56). The day -30 low was 90.7, and the second leg made a **lower low** at 87.2 (day -9). The bounce to 100 runs into resistance at 102.6–111.8 (the day -20 spike high).
- **Weight: 0.3.** The trend is still down, and this is a modest bounce.
- **Change mind:** Above 108 would raise the weight. Below 87.2 would take it to 0.

### b176b1a94c (AVAX)
- **Read:** The day -29 low was 89.9. A capitulation flush at day -16 reached 82.0 on 3x volume, followed by **higher lows** at 86.0, 92.2 and 98.0, with closes stepping up. The day -1 high of 102.8 clipped the day -20 high of 102.2. Overhead resistance is 110–118, then 129.
- **Weight: 0.5.** This is a constructive bottoming pattern: a climactic low, then higher lows, then a tentative break of the swing high.
- **Change mind:** A close above 103 would raise the weight to 0.65. A close below 92 would cut it to 0.2.

### 0201e39b63 (DOT)
- **Read:** The peak was ~157–163 (days -58 to -53). The day -29 low was 100.3, and the second leg made a **lower low** at 90.2 (day -7). Price has bounced back exactly to the old 100 low, which now acts as resistance, with 114–118.8 above that.
- **Weight: 0.2.** This is a lower-low structure with price bouncing into broken support.
- **Change mind:** Above 108 would raise the weight. Below 90.2 would take it to 0.

### 1ec73b88b8 (SOL)
- **Read:** The day -29 low was 73.7. The second leg held at a **higher low** of 78.5 (day -10). The rally has since cleared the day -20 high of 93.3 and reached 102.9: a **higher low plus a higher high**. Volume expanded on the up days (days -9, -6, -4 and -3). The next resistance is 105–110, then 119.
- **Weight: 0.65.** This is the cleanest reversal structure in the set.
- **Change mind:** A close below 88 (the day -5 area and breakout zone) would cut the weight to 0.25. Holding above 103 would let me raise it.

### b011adcbb9 (LINK)
- **Read:** The peak was ~134 (day -56). The day -30 low was 86.8 and the day -10 low was 86.9, forming a **double bottom**. Price has rallied to 100, but the day -20 neckline at 106.7 is not yet broken, and volume on the bounce is light (0.34–0.38).
- **Weight: 0.4.** The base is valid but unconfirmed.
- **Change mind:** A close above 106.7 would raise the weight to 0.65. A close below 86.8 would take it to 0.

### d7b1c29d4e (ETH)
- **Read:** The day -29 low was 84.3 and the day -9 low was 84.7, another **double bottom**. The day -20 high of 103.6 is the trigger level. Day 0 volume ticked up to 0.99. The broader trend from the 135 peak is still down.
- **Weight: 0.4.** It is the same setup as the previous window, with the trigger a little closer to current price.
- **Change mind:** Above 103.6 would raise the weight to 0.65. Below 84.3 would take it to 0.

### 78ef86b0a8 (LTC)
- **Read:** The peak was 132 (day -56). The day -29 low was 88.4, and the second leg made a marginal **lower low** at 85.7 (day -10). Price is now closing at 100, near the day's high and right at the day -20 high of 101.2. The sell-offs in this window are shallower than in most of the others.
- **Weight: 0.35.** The low was a slight undercut, and price is testing the swing high now.
- **Change mind:** A close above 101.2 would raise the weight to 0.55. Below 89 would cut it to 0.1.

---

{"03372af42d (BTC)": 0.25, "7fd1b39af6 (DOGE)": 0.2, "02c1b54fa0 (ADA)": 0.55, "e6c03a9dd9 (XRP)": 0.3, "b176b1a94c (AVAX)": 0.5, "0201e39b63 (DOT)": 0.2, "1ec73b88b8 (SOL)": 0.65, "b011adcbb9 (LINK)": 0.4, "d7b1c29d4e (ETH)": 0.4, "78ef86b0a8 (LTC)": 0.35}
````

## Notizen
Hypothese: E-000 ordnet fast mechanisch Position in der 180-Tage-Spanne einem Gewicht zu (Korrelation 0,97). E-002 zeigte: Ruhe senkt den Verlust, bringt aber kein Timing-Koennen. Begruendung vor der Zahl zwingt zu einer Lesart (Trend, Struktur, Niveaus) und einer Kipp-Bedingung, statt direkt Spanne -> Gewicht. Erwartung: Timing-Wert hoeher als E-000. Falsifiziert, wenn die Differenz zu E-000 auf A nicht t >= 2 erreicht. Nebenzweck auf Aarons Wunsch: die Denkweise der KI sichtbar machen (Rohantworten in runs/*/responses.json, Transkript in transkript.md). Befund: A +0,08 %/Woche vs E-000 (t 1,0, ohne beste Woche +0,05 %), B+C -0,26 %/Woche (t -1,2). Aufschreiben allein bringt kein Timing-Koennen. Die KI nennt sich in allen 13 Wochen selbst Trendfolger und erfindet ihre Regel jede Woche neu (kein Gedaechtnis); Korrelation Gewicht zu Position in der 180-Tage-Spanne 0,79 (E-000 0,83). Hinweis: Prompt v1 ('write the thinking down') wurde vom Opus-5.5-Schutzfilter (reasoning_extraction) in 6/13 Wochen abgewiesen, siehe abgebrochen-v1/; Formulierung 'write out your analysis' laeuft sauber.
