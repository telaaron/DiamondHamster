# E-022: Veto auf eine langsamere Regel: wie E-014, aber das Signal ist Schluss ueber dem 20-Wochen-Schnitt (Mittel der letzten 20 Wochenschluesse) statt ueber dem 50-Tage-Schnitt; Prompt und Signalzeile nennen den 20-Wochen-Schnitt

- Achse: prompt
- Basis: E-003M
- Daten: custom, 180 Tage
- Modell: claude-opus-5-5
- Werkzeug: f2794e9 versuche.py@2a621dd441
- Thread: https://claude.ai/code/project/chan_01VH1Un8SQtbifKwzD9jDguD?thread=cmsg_01VH1Un8SQtbifKwzD9jDguDJyFcf7n7Txzc5UyoievpPG

## Änderung zum Prompt der Basis
```diff
--- E-003M
+++ E-022
@@ -1,6 +1,7 @@
-# T-001 baseline trader prompt
+# T-001 baseline trader prompt, veto role
 
-You decide the position for an asset over the next week: a number from 0 (flat) to 1 (fully long).
+You check the position a fixed rule sets for an asset over the next week. The rule: invested (weight 1) when the close is above its 20-week average, otherwise flat (weight 0). The first line of each window shows the rule's signal for today.
+You may only confirm the signal or veto it: if the signal is 1, your weight is 1 (confirm) or 0 (veto, you judge it a false signal); if the signal is 0, your weight is 0. No other weights.
 Horizon is weeks to months; you do not need to trade often.
 
 Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
```

## Prompt
```
# T-001 baseline trader prompt, veto role

You check the position a fixed rule sets for an asset over the next week. The rule: invested (weight 1) when the close is above its 20-week average, otherwise flat (weight 0). The first line of each window shows the rule's signal for today.
You may only confirm the signal or veto it: if the signal is 1, your weight is 1 (confirm) or 0 (veto, you judge it a false signal); if the signal is 0, your weight is 0. No other weights.
Horizon is weeks to months; you do not need to trade often.

Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
Judge every window on its own. Do not compare windows with each other.

Before the weights, write out your analysis:
1. Strategy: in 2 to 3 sentences, the rule you will apply to every window.
2. Then for each window, under its id: your read of the market (trend, structure, key levels as prices on the 100 scale), your weight and why, and the price on the 100 scale that would make you change your mind.
3. End with one JSON object mapping each window id to its weight, e.g. {"a1b2c3d4e5": 0.0, "f6a7b8c9d0": 1.0}. Nothing after it.
```

## Datenaufbereitung (render.py)
```python
"""E-022: the champion's 180-day daily table plus one line with a fixed rule and its signal today.

Rule: invested (1) when the decision-day close is above the 20-week average, otherwise 0. The 20-week average is
the mean of the last 20 weekly closes, taken every 7th daily close counting back from the decision day (decision
days are Sundays, so these are the weekly closes; the decision day is included). It is computed from the full
candle history up to the decision day and shown on the window's 100 scale. Only change against E-014: the
signal's average (50 daily closes -> 20 weekly closes).
"""

import pandas as pd

from diamondhamster import ai

WEEKS = 20


def signal(df: pd.DataFrame) -> tuple[float, int]:
    weekly = df["close"].iloc[::-7].head(WEEKS)
    sma = weekly.mean()
    return sma, int(df["close"].iloc[-1] > sma)


def render(df: pd.DataFrame, lookback: int) -> str:
    sma, sig = signal(df)
    sma100 = sma * 100 / df["close"].iloc[-1]
    state = "1 (invested)" if sig else "0 (flat)"
    rule = f"rule: close {100:.1f} vs 20-week average {sma100:.1f} -> signal {state}"
    return rule + "\n" + ai.compact(ai.window(df, df.index[-1], lookback))
```

## Bewertung gegen E-003M

| Coins | Wochen | Entscheidungen | Timing-Wert/Woche | Basis | Differenz | t | ohne beste Woche | Wochen besser | Exposure | Rank-IC |
|---|---|---|---|---|---|---|---|---|---|---|
| A (10) | 13 | 130 | -0.09 % | -0.244 % | 0.154 % | 0.44 | -0.067 % (ohne 2026-09-20) | 7/13 | 0.292 (Basis 0.463) | -0.057 |

**Urteil: kein messbarer Unterschied**

Verbrauch: 13 Claude-Aufrufe, 797k Zeichen, Listenpreis 5.31 USD (zählt gegen Aarons Limit, keine Rechnung)

## Was die KI gedacht hat (Beispiel: Entscheidung 2026-07-05)

Alle Wochen: [denken.md](denken.md)

````
# Analysis

**1. Strategy:** I can only veto a signal of 1, never override a 0. Every window here has signal 0, so every weight is 0. For each one I still give my read of the market and the level that would flip the rule back to 1. At that point I would decide whether to confirm or veto, based on whether price closes above the 20-week average with structure behind it (higher lows, holding support) or only spikes there on a short-covering bounce.

**2. Windows**

### 67120412c6 (SOL)
- **Read:** The asset crashed from about 170 to 96 early in the window. It then ranged between 95 and 120, broke down to about 74 around day -29, and has recovered in a choppy way back to 100. This is the window closest to the rule's line: close 100.0 against an average of 100.4.
- **Levels:** resistance 102–103, support 83–85 and then 74.
- **Weight:** 0, because the signal is 0.
- **Change of mind:** a weekly close above about 103 would flip the signal, and I would likely confirm it if it held above 98.

### c52e3684bc (LINK)
- **Read:** The trend is down. Price peaked near 133 at day -56, fell to 87 at day -30, made a lower high near 106 and a retest low around 87. It is now bouncing to 100 on low volume. The average is 109.
- **Levels:** resistance 101.5–107, support 87–88.
- **Weight:** 0.
- **Change of mind:** a sustained close above about 109.

### 7b2fb1c341 (ETH)
- **Read:** The asset is in a decline from about 135 at day -79, with a capitulation leg to 84. The bounce to 100 meets a prior lower high near 103.6. The average is 113.
- **Levels:** resistance 103.6, support 85.
- **Weight:** 0.
- **Change of mind:** a close above about 113.

### b0ed2bbdaf (DOGE)
- **Read:** Price fell from a 152 peak at day -52 to 89 and is now bouncing to 100. It sits well below the average of 120, so the trend is firmly down.
- **Levels:** resistance 102 and then 113–119, support 89–90.
- **Weight:** 0.
- **Change of mind:** a close above about 120.

### 5e5ccc578f (BTC)
- **Read:** The trend is down from 130 at day -60. Price made a low of 91, a lower high at 105.7, and a second low of 91. It is now back at 100. The average is 110.
- **Levels:** resistance 105.7, support 91.
- **Weight:** 0.
- **Change of mind:** a close above about 110.

### 009af2e782 (LTC)
- **Read:** The asset is down from 132 at day -56 to a low of 86. Its recovery to 100 is at the top of a recent range. The average is 113.
- **Levels:** resistance 101, support 86.
- **Weight:** 0.
- **Change of mind:** a close above about 113.

### fc6ddd161a (XRP)
- **Read:** Price fell from 134 to 87. Earlier it was rejected at 111.8 on day -20, and it is now bouncing to 100. The average is 114.
- **Levels:** resistance 102.3 and then 112, support 87.
- **Weight:** 0.
- **Change of mind:** a close above about 114.

### d52c62d3f9 (DOT)
- **Read:** This is a long secular decline from about 250, with a lower high at 163 and a low of 90. It is now bouncing to 100, far below the average of 138.
- **Levels:** resistance 102 and then 119, support 90.
- **Weight:** 0.
- **Change of mind:** a close above about 138.

### 7523652526 (AVAX)
- **Read:** The asset is down from 151 to a high-volume flush to 82 at day -16. It is recovering to 100 under a lower high of 102.8. The average is 123.
- **Levels:** resistance 102–103, support 82–86.
- **Weight:** 0.
- **Change of mind:** a close above about 123.

### 2971f146b7 (ADA)
- **Read:** Price crashed from 152 to a low of 73 at day -10. That was followed by a violent rally of about 30% in four sessions on heavy volume, reaching 105.5 and closing at 100. The move looks like short covering from oversold levels, and price is still far below the average of 122.
- **Levels:** resistance 105.5, support 75 and then 73.
- **Weight:** 0.
- **Change of mind:** a close above about 122.

{"67120412c6 (SOL)": 0.0, "c52e3684bc (LINK)": 0.0, "7b2fb1c341 (ETH)": 0.0, "b0ed2bbdaf (DOGE)": 0.0, "5e5ccc578f (BTC)": 0.0, "009af2e782 (LTC)": 0.0, "fc6ddd161a (XRP)": 0.0, "d52c62d3f9 (DOT)": 0.0, "7523652526 (AVAX)": 0.0, "2971f146b7 (ADA)": 0.0}
````

## Notizen
Backlog #30. Kopiert von E-014 (Veto-Rolle auf der 50-Tage-Regel), einzige Aenderung gegen E-014 ist das Signal; "parent" ist E-003M, damit score wie immer gegen Champion und Referenz misst (wie bei E-014). Der Vergleich gegen E-014 steht in veto.md. Hypothese: Die 50-Tage-Regel kostet allein -0,35 %/Woche, die KI-Vetos verbessern sie um +0,29 %. Eine langsamere Regel wechselt seltener und ist die bessere Basis fuer dieselbe Veto-Rolle. Falsifiziert, wenn (a) die Differenz zu E-003M auf A <= 0 ist oder (b) der Veto-Gewinn gegenueber der nackten 20-Wochen-Regel (gleiche Wochen und Coins, ohne KI) <= 0 ist. Messbar besser erst bei t >= 2 (B-12/B-14: dann genau eine Wiederholung auf A, Urteil auf dem Mittel beider Laeufe; B+C nur bei t >= 2). Informativ wie E-014 (veto.md): Timing-Wert der Regel allein, Zahl und Trefferquote der Vetos, Regelverstoesse, Umschichtung, Anteil Gewichtsaenderungen unter 0,15, partieller Anker (werkzeuge/anker.py). Vorlage aus Paragraph 4a unveraendert; versuche.py vom Branch claude/project-thread-lupsy0 (PR #6).
