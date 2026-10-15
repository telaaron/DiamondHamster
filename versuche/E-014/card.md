# E-014: Veto statt Gewicht: eine feste Regel (Schluss ueber 50-Tage-Schnitt = 1, sonst 0) gibt das Signal, die erste Fensterzeile zeigt es; die KI darf ein 1-Signal nur bestaetigen (1) oder per Veto auf 0 setzen, ein 0-Signal bleibt 0

- Achse: prompt
- Basis: E-003M
- Daten: custom, 180 Tage
- Modell: claude-opus-5-5
- Werkzeug: 022ab32 versuche.py@e913634cff
- Thread: https://claude.ai/code/project/chan_01VH1Un8SQtbifKwzD9jDguD?thread=cmsg_01VH1Un8SQtbifKwzD9jDguDLJsu6tSB4T2Gq8pVzx97xX

## Änderung zum Prompt der Basis
```diff
--- E-003M
+++ E-014
@@ -1,6 +1,7 @@
-# T-001 baseline trader prompt
+# T-001 baseline trader prompt, veto role
 
-You decide the position for an asset over the next week: a number from 0 (flat) to 1 (fully long).
+You check the position a fixed rule sets for an asset over the next week. The rule: invested (weight 1) when the close is above its 50-day average, otherwise flat (weight 0). The first line of each window shows the rule's signal for today.
+You may only confirm the signal or veto it: if the signal is 1, your weight is 1 (confirm) or 0 (veto, you judge it a false signal); if the signal is 0, your weight is 0. No other weights.
 Horizon is weeks to months; you do not need to trade often.
 
 Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
```

## Prompt
```
# T-001 baseline trader prompt, veto role

You check the position a fixed rule sets for an asset over the next week. The rule: invested (weight 1) when the close is above its 50-day average, otherwise flat (weight 0). The first line of each window shows the rule's signal for today.
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
"""E-014: the champion's 180-day daily table plus one line with a fixed rule and its signal today.

Rule: invested (1) when the decision-day close is above the simple average of the last 50 daily closes
(decision day included), otherwise 0. The average is computed from the full candle history up to the decision
day, so it exists from the first window day on; it is shown on the window's 100 scale.
"""

import pandas as pd

from diamondhamster import ai

SMA = 50


def signal(df: pd.DataFrame) -> tuple[float, int]:
    sma = df["close"].tail(SMA).mean()
    return sma, int(df["close"].iloc[-1] > sma)


def render(df: pd.DataFrame, lookback: int) -> str:
    sma, sig = signal(df)
    sma100 = sma * 100 / df["close"].iloc[-1]
    state = "1 (invested)" if sig else "0 (flat)"
    rule = f"rule: close {100:.1f} vs 50-day average {sma100:.1f} -> signal {state}"
    return rule + "\n" + ai.compact(ai.window(df, df.index[-1], lookback))
```

## Bewertung gegen E-003M

| Coins | Wochen | Entscheidungen | Timing-Wert/Woche | Basis | Differenz | t | ohne beste Woche | Wochen besser | Exposure | Rank-IC |
|---|---|---|---|---|---|---|---|---|---|---|
| A (10) | 13 | 130 | -0.065 % | -0.244 % | 0.18 % | 0.33 | -0.121 % (ohne 2026-09-13) | 6/13 | 0.462 (Basis 0.463) | -0.018 |

**Urteil: kein messbarer Unterschied**

Verbrauch: 13 Claude-Aufrufe, 797k Zeichen, Listenpreis 5.41 USD (zählt gegen Aarons Limit, keine Rechnung)

## Was die KI gedacht hat (Beispiel: Entscheidung 2026-07-05)

Alle Wochen: [denken.md](denken.md)

````
## Strategy
I confirm a rule signal of 1 only if price has reclaimed its 50-day average with a structure that supports it: higher lows, recovery of a broken level, and buying volume. I veto a 1 that is only a weak bounce stalling under nearby resistance inside an intact pattern of lower highs. A signal of 0 always means weight 0. For those windows I note the level where the rule would turn on.

## 069f88f5b1 (DOT)
- **Read:** Steady downtrend from about 250 to a low of 90.2 on day -7, with lower highs throughout (155 → 115 → 101). A small bounce to 100 is fading on low volume (0.47). Resistance is 107–115; support is 90–92.
- **Weight:** 0. The signal is 0 and price is about 15% below a falling 50-day average.
- **Change of mind:** A close above about 112, reclaiming the 50-day average and the day -20 swing high.

## 37b814fcce (ADA)
- **Read:** Capitulation from about 124 to 72.9 (day -10), then a sharp four-day reversal to 101.4 on heavy volume (1.8–2.2). Price is pausing at 100, just under the 50-day average of 100.3. Resistance is 105.5 (day -1 high); support is 85 and 76.
- **Weight:** 0 (signal 0).
- **Change of mind:** A close above about 101 flips the rule. I would want it to hold above 97.7.

## 9c30d9a942 (ETH)
- **Read:** Lower highs since about 135. A low of 84.7 (day -9) was followed by a recovery to 100 with a higher low versus 84.3. Resistance is 101–103.6; support is 86–88.
- **Weight:** 0 (signal 0).
- **Change of mind:** A close above about 102 (the 50-day average) flips it.

## fa58290638 (BTC)
- **Read:** A downtrend from 129 bottomed at 90.8–92.9 with a double bottom. Price has risen to 100 on fading volume. Resistance is 101.7–105.7; support is 91.
- **Weight:** 0 (signal 0).
- **Change of mind:** A close above about 105 flips it.

## e10596334f (AVAX)
- **Read:** A crash to 82 (day -16) was followed by higher lows at 86 and 91.5, and price has climbed to 100. The 50-day average of 108.1 is still well above price. Resistance is 102–108; support is 91.5.
- **Weight:** 0 (signal 0).
- **Change of mind:** A close above about 107.

## 8d5fabafcb (DOGE)
- **Read:** A lower high at 152 was followed by a slide to 89.3 (day -5), then a bounce to 100 on light volume. Resistance is 106–114; support is 89.
- **Weight:** 0 (signal 0).
- **Change of mind:** A close above about 111.

## 5cf4d797e7 (SOL)
- **Read:** The longer-term trend is down (about 170 to 100). Price broke from a 100–107 range down to 73.7 (day -29), then built a higher low at 78.5 (day -10). It then rallied on above-average volume (1.2–1.5) back to 100–101, fully reclaiming the breakdown level. That makes it a failed breakdown. The 50-day average of 92.4 is now turning up. Day 0 is a quiet, low-volume pause rather than a rejection. Resistance is 103–107 and then 115–120; support is 94–92.
- **Weight:** 1, confirm. The higher-low structure and the recovery of the whole crash support the signal. Stalling at 101 on light volume is a pause, not a reversal sign.
- **Change of mind:** A close below 92 would mean the 50-day average was lost and the reclaim had failed.

## 1dcf0f37e2 (LINK)
- **Read:** Price is recovering from 86.9 to 100 while the 50-day average of 102.9 slopes down. Resistance is 101.5–106.7; support is 87–88.
- **Weight:** 0 (signal 0).
- **Change of mind:** A close above about 103.

## 07648a7d3c (XRP)
- **Read:** A higher low at 87.2 versus 90.7 was followed by a recovery to 100. A spike high of 111.8 (day -20) sits overhead. Resistance is 102–107; support is 88.
- **Weight:** 0 (signal 0).
- **Change of mind:** A close above about 103.5.

## 01fa3b0a1b (LTC)
- **Read:** Price fell from about 132 to 85.7 (day -10), then made a steady bounce to 100, just under the 50-day average of 101.8. Resistance is 101–103; support is 89–90.
- **Weight:** 0 (signal 0).
- **Change of mind:** A close above about 102.

{"069f88f5b1 (DOT)": 0.0, "37b814fcce (ADA)": 0.0, "9c30d9a942 (ETH)": 0.0, "fa58290638 (BTC)": 0.0, "e10596334f (AVAX)": 0.0, "8d5fabafcb (DOGE)": 0.0, "5cf4d797e7 (SOL)": 1.0, "1dcf0f37e2 (LINK)": 0.0, "07648a7d3c (XRP)": 0.0, "01fa3b0a1b (LTC)": 0.0}
````

## Notizen
Backlog #26, Waechter B-16 (andere Rolle statt anderer Satz). Hypothese: Die KI verliert als freier Gewichtsgeber, weil sie Trend folgt und zu oft umschichtet. Als Veto-Instanz auf einer festen Trendregel kann sie nur Fehlsignale der Regel abfangen. Erkennt sie Fehlsignale, liegt der Timing-Wert ueber E-003M und ueber der Regel allein. Falsifiziert, wenn die Differenz zu E-003M auf A nicht t >= 2 erreicht. Zusaetzlich (nur informativ): Timing-Wert der Regel ohne KI auf denselben Wochen und Coins, Zahl und Trefferquote der Vetos, Regelverstoesse (Gewicht 1 bei Signal 0 oder Zwischenwerte; das Werkzeug erzwingt die Binaeritaet nicht). Achse: Rolle (Prompt plus eine Datenzeile, beides gehoert zur Rolle). Tabelle unveraendert 180 Tage; Paragraph-4a-Vorlage unveraendert.
