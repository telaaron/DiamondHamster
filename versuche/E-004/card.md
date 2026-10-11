# E-004: Relativ statt absolut: Fenster sind verschiedene Märkte derselben Woche; vergleichen, mehr Gewicht auf die stärksten, weniger auf die schwächsten (ersetzt 'Judge every window on its own')

- Achse: prompt
- Basis: E-003
- Daten: candles, 180 Tage
- Modell: claude-opus-5-5
- Thread: https://claude.ai/code/project/chan_01VH1Un8SQtbifKwzD9jDguD?thread=cmsg_01VH1Un8SQtbifKwzD9jDguD4mK27Xxe67JynWUkCdjmgV

## Änderung zum Prompt der Basis
```diff
--- E-003
+++ E-004
@@ -4,7 +4,7 @@
 Horizon is weeks to months; you do not need to trade often.
 
 Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
-Judge every window on its own. Do not compare windows with each other.
+All windows are different markets over the same period, ending on the same day. Compare them with each other: put more weight on the strongest, less on the weakest.
 
 Before the weights, write out your analysis:
 1. Strategy: in 2 to 3 sentences, the rule you will apply to every window.
```

## Prompt
```
# T-001 baseline trader prompt

You decide the position for an asset over the next week: a number from 0 (flat) to 1 (fully long).
Horizon is weeks to months; you do not need to trade often.

Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
All windows are different markets over the same period, ending on the same day. Compare them with each other: put more weight on the strongest, less on the weakest.

Before the weights, write out your analysis:
1. Strategy: in 2 to 3 sentences, the rule you will apply to every window.
2. Then for each window, under its id: your read of the market (trend, structure, key levels as prices on the 100 scale), your weight and why, and the price on the 100 scale that would make you change your mind.
3. End with one JSON object mapping each window id to its weight, e.g. {"a1b2c3d4e5": 0.0, "f6a7b8c9d0": 1.0}. Nothing after it.
```

## Bewertung gegen E-003

| Coins | Wochen | Entscheidungen | Timing-Wert/Woche | Basis | Differenz | t | ohne beste Woche | Wochen besser | Exposure | Rank-IC |
|---|---|---|---|---|---|---|---|---|---|---|
| A (10) | 13 | 130 | -0.638 % | -0.151 % | -0.487 % | -2.16 | -0.557 % (ohne 2026-07-19) | 4/13 | 0.44 (Basis 0.457) | 0.003 |

**Urteil: schlechter**

Verbrauch: 13 Claude-Aufrufe, 786k Zeichen, Listenpreis 5.39 USD (zählt gegen Aarons Limit, keine Rechnung)

## Was die KI gedacht hat (Beispiel: Entscheidung 2026-07-05)

Alle Wochen: [denken.md](denken.md)

````
**1. Strategy**

All ten markets share one path: a sell-off into a crash low around day -150, a recovery into highs around day -60 to -50, a second break from day -33 to -30, a retest low between day -16 and day -5, and a 3–4 day bounce back to 100. I rank them by the quality of the retest. That means higher lows after day -30, whether price has reclaimed the day -20 swing high, and volume on the bounce. Markets that held their retest and broke above the post-crash range get the most weight. Markets that made clean lower lows and lower highs get the least.

**2. Windows**

**2ae1674212 (BTC)**
- **Read:** Recovered from 98.8 to 129 (day -56), then broke down. The day -30 low of 92.9 was undercut at 90.8 (day -4), a marginal lower low.
- **Now:** The bounce to 100 came on fading volume (0.46). Resistance is 104–105.7, the day -20 high.
- **Weight:** 0.3. The trend is still down and the bounce has no thrust.
- **Change my mind:** above 106 raises it; below 90.8 cuts it to zero.

**2225508141 (DOGE)**
- **Read:** The deepest giveback: from 152 (day -52) down to 89.3 (day -5), a clear lower low under the day -30 low of 101.5.
- **Now:** The bounce to 101.9 is on below-average volume. Overhead resistance sits at 110–114.
- **Weight:** 0.2. This is the weakest structure.
- **Change my mind:** above 114 raises it; below 89 exits.

**d9ae2edc29 (LTC)**
- **Read:** Bottomed at 85.7 (day -10), made a higher low at 89.8 (day -4), and is now pressing the 101 ceiling (day -20 and day -14 highs). Volume is steady at about 0.8.
- **Weight:** 0.45. The structure is improving but has not broken out yet.
- **Change my mind:** a close above 101.5 raises it; below 89.8 cuts it.

**b1a691bee1 (ADA)**
- **Read:** Had the worst crash, from 152 to 78.4 and then a 72.9 low (day -10). Then came a violent four-day reversal from 76 to 105.5 on 1.8–2.2x volume, clearing the 100.3 range top (day -20).
- **Now:** Day 0 held 97.7.
- **Weight:** 0.5. This is the strongest short-term momentum, discounted because it is a potential squeeze inside a long-term downtrend with heavy overhead at 110–125.
- **Change my mind:** a hold above 97 confirms it; a close below 92 means the breakout failed.

**0b7037d84a (SOL)**
- **Read:** The cleanest base. Lows ran 73.7 (day -29), then 78.5 (day -10), then 88.1 (day -5), a sequence of higher lows.
- **Now:** Price broke the 93.3 day -20 high and has held 98–103 for three days. It now sits at its old day -150 to day -90 range of 95–105.
- **Weight:** 0.6. This is the strongest structure.
- **Change my mind:** below 94 cuts it; above 103 adds to it.

**3b8255ec36 (ETH)**
- **Read:** Double bottom at 84.3 (day -29) and 84.7 (day -9). It rallied to 101.3, but the neckline at 103.6 (day -20) is not yet cleared. Volume picked up on day 0 (0.99).
- **Weight:** 0.4.
- **Change my mind:** above 103.6 raises it; below 94 cuts it.

**5b55cd059b (AVAX)**
- **Read:** Held up best through day -50 to day -34, in the 130s. A capitulation low of 82.0 came on day -16 with 3x volume. Since then the lows have risen: 86.0, 90.6, 92.2, 98.0.
- **Now:** The day -1 high of 102.8 marginally clears the 102.2 day -20 high.
- **Weight:** 0.5.
- **Change my mind:** below 92 cuts it; above 103 confirms it.

**ebc38d3ac0 (LINK)**
- **Read:** Double bottom at 86.8 and 86.9, and price has bounced to 101.4. The neckline is 106.7 (day -20), and the bounce volume is very thin (0.34–0.38).
- **Weight:** 0.35. The volume does not confirm the move.
- **Change my mind:** above 107 raises it; below 88 cuts it.

**4ea4bffb88 (XRP)**
- **Read:** A marginal lower low at 87.2 (day -10) versus 90.7 (day -29), then a bounce to 102.3. Resistance is 107 and 111.8 (the day -20 spike).
- **Weight:** 0.35.
- **Change my mind:** above 107 raises it; below 88 cuts it.

**0f92a5bf9c (DOT)**
- **Read:** A persistent pattern of lower highs: 163 (day -53), then 118.8 (day -20), then 111 (day -13). There is also a lower low at 90.2 (day -7) versus 100.3 (day -29).
- **Now:** It is bouncing into 101–102, which is overhead supply.
- **Weight:** 0.25.
- **Change my mind:** above 112 raises it; below 90 exits.

**3. Weights**

{"2ae1674212 (BTC)": 0.3, "2225508141 (DOGE)": 0.2, "d9ae2edc29 (LTC)": 0.45, "b1a691bee1 (ADA)": 0.5, "0b7037d84a (SOL)": 0.6, "3b8255ec36 (ETH)": 0.4, "5b55cd059b (AVAX)": 0.5, "ebc38d3ac0 (LINK)": 0.35, "4ea4bffb88 (XRP)": 0.35, "0f92a5bf9c (DOT)": 0.25}
````

## Notizen
Backlog #2. Hypothese: Querschnitt (welcher Coin) ist leichter als Timing (wann). E-003 Rank-IC ca. 0. Erwartung: Rank-IC > 0 und Timing-Wert höher als E-003. Falsifiziert, wenn die Differenz zu E-003 auf A nicht t >= 2 erreicht.
