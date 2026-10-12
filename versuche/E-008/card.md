# E-008: Verdichtet: letzte 30 Tage als Tageskerzen, Tage 31 bis 177 davor als 21 Wochenkerzen (aus den Tageskerzen gebaut); im Prompt nur die Beschreibung der Tabelle angepasst

- Achse: format
- Basis: E-003
- Daten: custom, 180 Tage
- Modell: claude-opus-5-5
- Thread: https://claude.ai/code/project/chan_01VH1Un8SQtbifKwzD9jDguD?thread=cmsg_01VH1Un8SQtbifKwzD9jDguDRc5AJXU9i7RvmQh8eGQA1n

## Änderung zum Prompt der Basis
```diff
--- E-003
+++ E-008
@@ -3,7 +3,7 @@
 You decide the position for an asset over the next week: a number from 0 (flat) to 1 (fully long).
 Horizon is weeks to months; you do not need to trade often.
 
-Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
+Each window covers the last 177 days in two parts. First weekly candles for days -176 to -30, one line per week: `day o h l c v`, where day is the last day of that week. Then daily candles for the last 30 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is the average daily volume of the line's days relative to the window average.
 Judge every window on its own. Do not compare windows with each other.
 
 Before the weights, write out your analysis:
```

## Prompt
```
# T-001 baseline trader prompt

You decide the position for an asset over the next week: a number from 0 (flat) to 1 (fully long).
Horizon is weeks to months; you do not need to trade often.

Each window covers the last 177 days in two parts. First weekly candles for days -176 to -30, one line per week: `day o h l c v`, where day is the last day of that week. Then daily candles for the last 30 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is the average daily volume of the line's days relative to the window average.
Judge every window on its own. Do not compare windows with each other.

Before the weights, write out your analysis:
1. Strategy: in 2 to 3 sentences, the rule you will apply to every window.
2. Then for each window, under its id: your read of the market (trend, structure, key levels as prices on the 100 scale), your weight and why, and the price on the 100 scale that would make you change your mind.
3. End with one JSON object mapping each window id to its weight, e.g. {"a1b2c3d4e5": 0.0, "f6a7b8c9d0": 1.0}. Nothing after it.
```

## Datenaufbereitung (render.py)
```python
"""E-008: last 30 days as daily candles, days 31 to 177 before that as weekly candles.

Same 180-day horizon as the champion, condensed: 21 full weeks (days -176 to -30, the 3 oldest days that do not
fill a week are dropped) plus 30 daily rows instead of 180 daily rows. Weekly candles are built from the daily
bars in 7-day blocks counted back from the decision day: open of the first day, max high, min low, close of the
last day. Prices scaled so the last close is 100. Volume is the average daily volume of the row's days relative
to the average daily volume of the whole window, so weekly and daily v are on the same scale.
"""

import pandas as pd

DAILY = 30
WEEKS = 21


def render(df: pd.DataFrame, lookback: int) -> str:
    w = df.tail(DAILY + 7 * WEEKS).copy()
    w.index = pd.RangeIndex(-len(w) + 1, 1)
    scale = 100 / w["close"].iloc[-1]
    w[["open", "high", "low", "close"]] *= scale
    w["volume"] = w["volume"] / w["volume"].mean()
    old, recent = w.iloc[:-DAILY], w.iloc[-DAILY:]
    weekly = [old.iloc[i:i + 7] for i in range(0, len(old), 7)]
    fmt = "{} {:.1f} {:.1f} {:.1f} {:.1f} {:.2f}"
    lines = ["weekly: day o h l c v (day = last day of the week)"]
    lines += [fmt.format(b.index[-1], b["open"].iloc[0], b["high"].max(), b["low"].min(), b["close"].iloc[-1], b["volume"].mean()) for b in weekly]
    lines += ["daily: day o h l c v"]
    lines += [fmt.format(d, r.open, r.high, r.low, r.close, r.volume) for d, r in recent.iterrows()]
    return "\n".join(lines)
```

## Bewertung gegen E-003

| Coins | Wochen | Entscheidungen | Timing-Wert/Woche | Basis | Differenz | t | ohne beste Woche | Wochen besser | Exposure | Rank-IC |
|---|---|---|---|---|---|---|---|---|---|---|
| A (10) | 13 | 130 | -0.272 % | -0.151 % | -0.121 % | -1.16 | -0.163 % (ohne 2026-07-19) | 5/13 | 0.439 (Basis 0.457) | 0.055 |

**Urteil: kein messbarer Unterschied**

Verbrauch: 13 Claude-Aufrufe, 242k Zeichen, Listenpreis 2.24 USD (zählt gegen Aarons Limit, keine Rechnung)

## Was die KI gedacht hat (Beispiel: Entscheidung 2026-07-05)

Alle Wochen: [denken.md](denken.md)

````
**Strategy:** All weights are scaled to trend and structure. A primary downtrend on the weekly chart caps exposure at about 0.3. Within that cap, I add weight when the daily 30-day structure shows higher lows or a reclaim of the post-breakdown range high. I cut weight when the daily structure is still making lower lows and lower highs, and I only go above 0.5 when price has broken out above its 30-day range.

## 5b41ace1e3 (LINK)
- **Read:** The weekly trend is down, from 170 to 100. Price spent weeks in a 100–130 range, then broke down from it at -30. On the daily chart the bounce to 106.7 failed, and price made a marginal lower low at 86.9. It has now rallied back to 100, which is the middle of the 87–107 range, on fading volume.
- **Weight:** 0.3. The bounce is real, but the structure is neutral inside a downtrend.
- **Change my mind:** I would add above 107 and go flat below 87.

## c30cac7b9e (DOT)
- **Read:** The weekly decline is steep, from 240 to 100, and the prior range was 135–160. On the daily chart the high was 118.8 at -20. After that, price broke the post-crash low of 100.3 and fell to 90.2, a clear lower low. The rebound to 100 is still below the lower-high zone at 110–115.
- **Weight:** 0.2.
- **Change my mind:** I would add above 115 and go flat below 90.

## 584ec97006 (XRP)
- **Read:** The weekly trend is down, from 180 to 100. On the daily chart a spike to 111.8 failed, and price then made a lower low at 87.2 versus 90.7 earlier. It has recovered to 100, but the range resistance at 102–108 is still overhead.
- **Weight:** 0.3.
- **Change my mind:** I would add above 108 and go flat below 87.

## 91d23865ef (BTC)
- **Read:** Before the drop, price had climbed from 104 to 126 on the weekly chart, so the breakdown at -30 ended an uptrend. On the daily chart the range is 91–106 and the lower low is only shallow, at 91.3 versus 93.5. Price is now at 100 on light volume.
- **Weight:** 0.35.
- **Change my mind:** I would add above 106 and go flat below 91.

## fe2197b9b8 (AVAX)
- **Read:** The weekly trend is down, from 199 to 100. The daily chart shows a capitulation at -16, with a low of 82 on 3x volume. Since then the lows have stepped up: 86, then 90.6, then 92.2. Price is now 100, just under the range high of 102.
- **Weight:** 0.45. The higher-low base after the washout is constructive.
- **Change my mind:** I would add above 103 and cut below 90.

## 4e3059e9d4 (ETH)
- **Read:** The weekly trend is down, from 185 to 100. The daily chart shows a double bottom at 84.3 and 84.7. Price has rallied back to 100, just under the range high of 103.6.
- **Weight:** 0.35.
- **Change my mind:** I would add above 104 and go flat below 84.

## 821a8d8ee1 (LTC)
- **Read:** The weekly trend is down, from 178 to 100. On the daily chart price made a lower low at 85.7 versus 88.4. Since then it has climbed steadily, closing at the day's high of 100, which tests the range top at 101.
- **Weight:** 0.35.
- **Change my mind:** I would add above 101.5 and go flat below 89.

## 48a2205c2b (SOL)
- **Read:** The weekly trend is down, from 177 to 100, but price has now reclaimed the pre-breakdown level near 100.6. The daily chart shows higher lows (73.7, then 78.5, then 85.5) and a breakout above the -20 high of 93.3. The structure is clean: higher highs and higher lows.
- **Weight:** 0.6.
- **Change my mind:** I would cut below 93 and go flat below 85.

## ca0478721a (ADA)
- **Read:** The weekly decline is heavy, from 208 to 100, and the prior range was 122–150. On the daily chart price bottomed at 72.9, then rallied explosively from 76 to 105 in four days on about 2x volume, above the prior high of 100.3. That is a breakout, but it is extended and still far below the weekly range.
- **Weight:** 0.5.
- **Change my mind:** I would cut below 94 if the breakout fails and add above 106.

## 3e2ee9d89e (DOGE)
- **Read:** On the weekly chart a rally to 152 reversed into a breakdown to 100. On the daily chart the high was 118.7 at -23, followed by a steady series of lower highs and lower lows down to 89.3. The bounce to 100 is still beneath resistance at 105–108.
- **Weight:** 0.2.
- **Change my mind:** I would add above 108 and go flat below 89.

{"5b41ace1e3 (LINK)": 0.3, "c30cac7b9e (DOT)": 0.2, "584ec97006 (XRP)": 0.3, "91d23865ef (BTC)": 0.35, "fe2197b9b8 (AVAX)": 0.45, "4e3059e9d4 (ETH)": 0.35, "821a8d8ee1 (LTC)": 0.35, "48a2205c2b (SOL)": 0.6, "ca0478721a (ADA)": 0.5, "3e2ee9d89e (DOGE)": 0.2}
````

## Notizen
Backlog #6. Hypothese: Die KI ankert das Gewicht an der Position in der 180-Tage-Spanne (E-003 Korrelation 0,79) und schichtet Woche fuer Woche nach den letzten Tagen um. Wochenkerzen fuer die aeltere Historie zeigen die grosse Struktur ohne 150 Zeilen Tagesrauschen; 51 statt 180 Zeilen. Erwartung: weniger Umschichtung, Timing-Wert hoeher als E-003. Falsifiziert, wenn die Differenz zu E-003 auf A nicht t >= 2 erreicht. Abweichungen: Fenster 177 statt 180 Tage, weil 150 Tage keine ganzen Wochen ergeben (die 3 aeltesten Tage fallen weg); Volumen als mittleres Tagesvolumen je Zeile relativ zum Fensterschnitt. Die Paragraph-4a-Vorlage ist unveraendert; Kipp-Niveaus bleiben auf der 100-Skala.
