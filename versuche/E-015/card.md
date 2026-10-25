# E-015: Grobe Stufen: Gewicht nur 0, 0,5 oder 1 statt beliebig zwischen 0 und 1

- Achse: prompt
- Basis: E-003M
- Daten: candles, 180 Tage
- Modell: claude-opus-5-5
- Werkzeug: 022ab32 versuche.py@e913634cff
- Thread: https://claude.ai/code/project/chan_01VH1Un8SQtbifKwzD9jDguD?thread=cmsg_01VH1Un8SQtbifKwzD9jDguDByD9cQxAgykbkNsAyGcmCT

## Änderung zum Prompt der Basis
```diff
--- E-003M
+++ E-015
@@ -1,6 +1,6 @@
 # T-001 baseline trader prompt
 
-You decide the position for an asset over the next week: a number from 0 (flat) to 1 (fully long).
+You decide the position for an asset over the next week: exactly one of three levels, 0 (flat), 0.5 (half) or 1 (fully long). No other values.
 Horizon is weeks to months; you do not need to trade often.
 
 Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
```

## Prompt
```
# T-001 baseline trader prompt

You decide the position for an asset over the next week: exactly one of three levels, 0 (flat), 0.5 (half) or 1 (fully long). No other values.
Horizon is weeks to months; you do not need to trade often.

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
| A (10) | 13 | 130 | -0.407 % | -0.244 % | -0.163 % | -0.32 | -0.499 % (ohne 2026-09-13) | 4/13 | 0.535 (Basis 0.463) | 0.1 |

**Urteil: kein messbarer Unterschied**

Verbrauch: 13 Claude-Aufrufe, 785k Zeichen, Listenpreis 5.6 USD (zählt gegen Aarons Limit, keine Rechnung)

## Was die KI gedacht hat (Beispiel: Entscheidung 2026-07-05)

Alle Wochen: [denken.md](denken.md)

````
**Strategy:** All ten windows share the same shape: a long decline, a sharp breakdown around day -33 to -30, and a rebound to 100. I go fully long (1) only when price has won back the pre-breakdown level and sits above its ~50-day average, with higher lows. I hold half (0.5) when there is a basing pattern (double bottom, or a reclaimed short-term range) but price is still below the breakdown level or the 50-day average. I stay flat (0) when the bounce is still inside a sequence of lower highs and lower lows, well under the 50-day average.

### 02d6fe7c74 (SOL)
- **Read:** Crashed from the ~100–105 range to 73.7 at day -29. Made a clearly higher low at 78.5 on day -10, then a steady advance with higher highs to 100. That puts it back inside the pre-breakdown band of 100–105. The 50-day average is about 92, so price is above it. Resistance is 105–110.
- **Weight:** 1.0. It is a V-shaped recovery with a higher-low structure and the breakdown level has been reclaimed.
- **Change of mind:** a close below 92.

### b610638c0a (LINK)
- **Read:** The breakdown came from ~112–117. It double-bottomed at 86.8 and 86.9, and price is now 100. The neckline is the day -20 high at 106.7, and the 50-day average (~103) is overhead.
- **Weight:** 0.5. The base is constructive, but the trend has not yet been reclaimed.
- **Change of mind:** above 106.7 I would go to 1; below 94 I would go to 0.

### a3feb6f657 (DOGE)
- **Read:** The breakdown came from ~129. It made a low of 99.7, then a lower high at 118.7 and a lower low at 89.3 on day -5. The bounce to 100 sits far below the 50-day average (~113).
- **Weight:** 0. It is still a downtrend of lower highs and lower lows.
- **Change of mind:** a close above 112.

### 6437bffb93 (AVAX)
- **Read:** The breakdown came from ~129. It made a capitulation low at 82.0 on day -16 on heavy volume, then a higher low at 86.0, and is now 100, around the day -20 high of 102. The 50-day average is ~108.
- **Weight:** 0.5. Capitulation followed by a higher low points to a base, but price is under its averages.
- **Change of mind:** above 103 I would go to 1; below 92 I would go to 0.

### b545d15984 (XRP)
- **Read:** The breakdown came from ~115. The lows were 90.7 and then a slightly lower 87.2, and price is now 100. Overhead are the spike high at 111.8 and the 50-day average at ~104.
- **Weight:** 0.5. It is basing but still capped.
- **Change of mind:** above 105 I would go to 1; below 92 I would go to 0.

### 0eab3ad18b (ADA)
- **Read:** The breakdown came from ~124. It made a lower low at 72.9 on day -10, then ran from 76 to 101 in four days on volume of 2x the average. That move broke above the day -20 high (100.3), and price is now roughly at the 50-day average (~101). It is very extended.
- **Weight:** 0.5. The momentum is real, but a vertical move straight into resistance makes the entry poor.
- **Change of mind:** above 105.5 I would go to 1; below 92 I would go to 0.

### 3a657df431 (DOT)
- **Read:** The breakdown came from ~135. It made a low of 100.3, a lower high at 118.8, and a lower low at 90.2. The bounce to 100 is well under the 50-day average (~118).
- **Weight:** 0. The downtrend is intact.
- **Change of mind:** a close above 115.

### b331ee4d10 (BTC)
- **Read:** The breakdown came from ~116. Lows were 92.9 and then 90.8, a rough double bottom, and price is now 100. Overhead are the day -20 high at 105.7 and the 50-day average at ~105.
- **Weight:** 0.5. It is a base, but the trend has not turned.
- **Change of mind:** above 106 I would go to 1; below 93 I would go to 0.

### 20c2f88858 (ETH)
- **Read:** The breakdown came from ~112. It double-bottomed at 84.3 and 84.7, and price is now 100, just under the 103.6 neckline. The 50-day average is ~101.
- **Weight:** 0.5. This is a clean double bottom, but it is not confirmed yet.
- **Change of mind:** above 104 I would go to 1; below 90 I would go to 0.

### 736dd0f2ac (LTC)
- **Read:** The breakdown came from ~113. Lows were 88.4 and then 85.7, and today's close of 100 is the highest close since day -33. The 50-day average is ~101.
- **Weight:** 0.5. It is basing and pressing on the 50-day average.
- **Change of mind:** above 102 I would go to 1; below 91 I would go to 0.

{"02d6fe7c74 (SOL)": 1.0, "b610638c0a (LINK)": 0.5, "a3feb6f657 (DOGE)": 0.0, "6437bffb93 (AVAX)": 0.5, "b545d15984 (XRP)": 0.5, "0eab3ad18b (ADA)": 0.5, "3a657df431 (DOT)": 0.0, "b331ee4d10 (BTC)": 0.5, "20c2f88858 (ETH)": 0.5, "736dd0f2ac (LTC)": 0.5}
````

## Notizen
Backlog #27, Waechter B-16 (Traegheit ohne Gedaechtnis). Hypothese: Ein Teil des Verlusts von E-003M sind kleine Umschichtungen (0,1 bis 0,2 je Woche), die nur Kosten und Rauschen bringen. Mit drei Stufen bleibt das Gewicht stehen, solange die Lesart nicht eine ganze Stufe kippt. Erwartung: weniger Umschichtung, Timing-Wert ueber E-003M. Falsifiziert, wenn die Differenz zu E-003M auf A nicht t >= 2 erreicht. Gegenrisiko: Stufen koennen die Umschichtung auch vergroessern (Spruenge von 0,5 statt 0,1, vgl. E-010 Regime-Label). Informativ: Anteil Werte ausserhalb {0, 0.5, 1} (das Werkzeug erzwingt die Stufen nicht), Umschichtung je Coin und Woche. Paragraph-4a-Vorlage unveraendert, 180 Tage Kerzen.
