# E-016: Traegheit mit Gedaechtnis: die KI sieht Gewicht und Kipp-Preis der Vorwoche und aendert nur, wenn der Kipp-Preis gebrochen ist

- Achse: prompt
- Basis: E-003M
- Daten: candles, 180 Tage
- Modell: claude-opus-5-5
- Werkzeug: f2794e9 versuche.py@e913634cff
- Thread: https://claude.ai/code/project/chan_01VH1Un8SQtbifKwzD9jDguD?thread=cmsg_01VH1Un8SQtbifKwzD9jDguDSRBJxoU6KX3yUnwJPrGnU5

## Änderung zum Prompt der Basis
```diff
--- E-003M
+++ E-016
@@ -6,7 +6,9 @@
 Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
 Judge every window on its own. Do not compare windows with each other.
 
+Each window starts with a line about your decision on this asset one week ago: `last week: weight W, flip price F on today's scale`, or `last week: no decision`. Keep last week's weight unless the close has broken the flip price since then; only then decide a new weight. With no decision last week, decide freely.
+
 Before the weights, write out your analysis:
 1. Strategy: in 2 to 3 sentences, the rule you will apply to every window.
 2. Then for each window, under its id: your read of the market (trend, structure, key levels as prices on the 100 scale), your weight and why, and the price on the 100 scale that would make you change your mind.
-3. End with one JSON object mapping each window id to its weight, e.g. {"a1b2c3d4e5": 0.0, "f6a7b8c9d0": 1.0}. Nothing after it.
+3. End with one JSON object mapping each window id to its weight and flip price, e.g. {"a1b2c3d4e5": {"weight": 0.0, "flip": 104.5}, "f6a7b8c9d0": {"weight": 1.0, "flip": 91.0}}. Nothing after it.
```

## Prompt
```
# T-001 baseline trader prompt

You decide the position for an asset over the next week: a number from 0 (flat) to 1 (fully long).
Horizon is weeks to months; you do not need to trade often.

Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
Judge every window on its own. Do not compare windows with each other.

Each window starts with a line about your decision on this asset one week ago: `last week: weight W, flip price F on today's scale`, or `last week: no decision`. Keep last week's weight unless the close has broken the flip price since then; only then decide a new weight. With no decision last week, decide freely.

Before the weights, write out your analysis:
1. Strategy: in 2 to 3 sentences, the rule you will apply to every window.
2. Then for each window, under its id: your read of the market (trend, structure, key levels as prices on the 100 scale), your weight and why, and the price on the 100 scale that would make you change your mind.
3. End with one JSON object mapping each window id to its weight and flip price, e.g. {"a1b2c3d4e5": {"weight": 0.0, "flip": 104.5}, "f6a7b8c9d0": {"weight": 1.0, "flip": 91.0}}. Nothing after it.
```

## Bewertung gegen E-003M

| Coins | Wochen | Entscheidungen | Timing-Wert/Woche | Basis | Differenz | t | ohne beste Woche | Wochen besser | Exposure | Rank-IC |
|---|---|---|---|---|---|---|---|---|---|---|
| A (10) | 13 | 130 | -0.083 % | -0.244 % | 0.162 % | 1.05 | 0.061 % (ohne 2026-08-16) | 7/13 | 0.423 (Basis 0.463) | -0.062 |

**Urteil: kein messbarer Unterschied**

Verbrauch: 13 Claude-Aufrufe, 797k Zeichen, Listenpreis 5.41 USD (zählt gegen Aarons Limit, keine Rechnung)

## Was die KI gedacht hat (Beispiel: Entscheidung 2026-07-05)

Alle Wochen: [denken.md](denken.md)

````
**Strategy:** The 180-day trend is down in every window, so I cap exposure well below fully long. Each window has a capitulation low (around day -30) and a relief-rally high (around day -20), and I weight on how price has behaved since then:

- **0.6:** a higher high above the relief high plus a higher low. Flip is below the last higher low.
- **0.3–0.4:** a basing or double bottom that is still under the relief high. Flip is a close above that resistance, which would justify adding.
- **0.2:** lower lows and lower highs still intact. Flip is above the nearest lower high.

**269af209d3 (ETH)**
- **Read:** Long decline from about 138 (-79). Crash low at 84.3 (-29), relief high at 103.6 (-20), then a retest at 84.7 (-9), which forms a double bottom near 85. The 4-day rally into 100 brings price up to the neckline at 101–103.6 on modest volume.
- **Weight 0.3:** the base is constructive but not confirmed.
- **Flip 104:** a close above the neckline would confirm the double bottom.

**362b61613e (AVAX)**
- **Read:** Crash low 89.9, relief high 102.2. The new low at 82.0 (-16) came on 3x volume, which looks like a selling climax. Since then the lows have been rising: 86, 86.1, 90.6, 92.2, 98. Price is 100, just under 102–102.8 resistance.
- **Weight 0.4:** the higher-low sequence is better than most windows here.
- **Flip 103:** a close above resistance would add.

**b0ec489261 (DOT)**
- **Read:** Persistent lower highs from 163 (-53). The crash low of 100.3 failed, and price fell to 90.2 (-7). The bounce to 100 is still below the lower highs at 106–114.
- **Weight 0.2:** the downtrend structure is intact.
- **Flip 106:** a close above that would break the sequence of lower highs.

**bf2a6c7452 (BTC)**
- **Read:** Crash low 92.9, relief high 105.7, slight undercut to 90.8 (-4). This is a 91–106 range, and price is mid-range at 100.
- **Weight 0.3:** no edge in the middle of the range.
- **Flip 106:** a close above the range top.

**474325b554 (ADA)**
- **Read:** Deepest selloff of the group: crash to 78.4, a lower low at 72.9 (-10), then a high-volume V-reversal (-4 to -1, volume around 2x) from 76 to a 105.5 high. That cleared the 100.3 relief high, and price is now holding 100 just above it. The larger trend is still bearish, with overhead supply at 120–130.
- **Weight 0.6:** strong momentum and a breakout.
- **Flip 92:** a close below the -1 low at 92.3 would mean the reversal failed.

**9cb9641d45 (SOL)**
- **Read:** Crash low 73.7, relief high 93.3, higher low at 78.5 (-10). Price is now 100, a clean higher high and higher low. The next resistance is the old 100–110 shelf from -100 to -35.
- **Weight 0.6:** this is the best-confirmed reversal structure.
- **Flip 93:** a close back below the prior relief high.

**12456e51ad (XRP)**
- **Read:** Crash low 90.7, relief high 111.8, lower low at 87.2 (-9). The bounce to 100 is still under 102.6/107/111.8.
- **Weight 0.3:** it is still a lower-low structure, but the bounce is firm.
- **Flip 103:** a close above the first lower high would add.

**84e7fa1707 (LINK)**
- **Read:** Crash low 86.8, relief high 106.7, double bottom at 86.9 (-10). Price is 100, with resistance at 102.9–106.7.
- **Weight 0.3:** a base below the neckline.
- **Flip 104:** a close above it would add.

**673713db86 (LTC)**
- **Read:** Crash low 88.4, relief high 101.2, lower low at 85.7 (-11/-10). Since then the lows have risen gradually, and price has reached 100 right at the 101.2 resistance.
- **Weight 0.3:** testing resistance, not through it.
- **Flip 102:** a close above that would confirm.

**990f5a978f (DOGE)**
- **Read:** Distribution from 152 (-52), crash low 99.7, relief high 118.7, then lower lows down to 89.3 (-5). The bounce to 100 is below the lower highs at 106–114.
- **Weight 0.2:** the downtrend is intact.
- **Flip 106:** a close above that would break the lower highs.

{"269af209d3 (ETH)": {"weight": 0.3, "flip": 104.0}, "362b61613e (AVAX)": {"weight": 0.4, "flip": 103.0}, "b0ec489261 (DOT)": {"weight": 0.2, "flip": 106.0}, "bf2a6c7452 (BTC)": {"weight": 0.3, "flip": 106.0}, "474325b554 (ADA)": {"weight": 0.6, "flip": 92.0}, "9cb9641d45 (SOL)": {"weight": 0.6, "flip": 93.0}, "12456e51ad (XRP)": {"weight": 0.3, "flip": 103.0}, "84e7fa1707 (LINK)": {"weight": 0.3, "flip": 104.0}, "673713db86 (LTC)": {"weight": 0.3, "flip": 102.0}, "990f5a978f (DOGE)": {"weight": 0.2, "flip": 106.0}}
````

## Notizen
Backlog #28, Waechter B-16. Hypothese: Ein Teil des Verlusts von E-003M ist Umschichtung ohne neue Information (Lauf-zu-Lauf-Rauschen der Gewichte). Mit Gedaechtnis und Kipp-Preis-Regel bleibt das Gewicht stehen, bis der selbst genannte Preis bricht. Erwartung: deutlich weniger Umschichtung, Timing-Wert ueber E-003M. Falsifiziert, wenn die Differenz zu E-003M auf A nicht t >= 2 erreicht. Gegenrisiko: Kipp-Preise nah am Kurs brechen fast jede Woche, dann aendert sich nichts. Informativ: Umschichtung, Anteil Wochen mit unveraendertem Gewicht, Regeltreue (Gewicht geaendert ohne Bruch). Vorlage aus Paragraph 4a unveraendert bis auf das JSON-Format, 180 Tage Kerzen.
