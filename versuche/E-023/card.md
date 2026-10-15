# E-023: E-003M plus eine Zeile je Fenster mit der Perp-Basis: 7-Tage-Mittel von Close(BINANCE:<COIN>USDT.P)/Close(Spot)-1 als Perzentil der eigenen letzten 180 Tage; prompt.md erklaert die Zeile in zwei Saetzen ohne Handelsregel

- Achse: daten
- Basis: E-003M
- Daten: custom, 180 Tage
- Modell: claude-opus-5-5
- Werkzeug: f2794e9 versuche.py@e913634cff
- Thread: https://claude.ai/code/project/chan_01VH1Un8SQtbifKwzD9jDguD?thread=cmsg_01VH1Un8SQtbifKwzD9jDguDCR15K2Dcgphwu4Y7Xyto3E

## Änderung zum Prompt der Basis
```diff
--- E-003M
+++ E-023
@@ -4,6 +4,7 @@
 Horizon is weeks to months; you do not need to trade often.
 
 Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
+Each window starts with one line `basis pct N` (or `basis pct not available`): the premium of the perpetual futures price over the spot price, averaged over the last 7 days, as a percentile from 0 to 100 of its own values over the last 180 days. A high value means traders holding leveraged long positions pay more than usual relative to spot, a low value means they pay less than usual.
 Judge every window on its own. Do not compare windows with each other.
 
 Before the weights, write out your analysis:
```

## Prompt
```
# T-001 baseline trader prompt

You decide the position for an asset over the next week: a number from 0 (flat) to 1 (fully long).
Horizon is weeks to months; you do not need to trade often.

Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
Each window starts with one line `basis pct N` (or `basis pct not available`): the premium of the perpetual futures price over the spot price, averaged over the last 7 days, as a percentile from 0 to 100 of its own values over the last 180 days. A high value means traders holding leveraged long positions pay more than usual relative to spot, a low value means they pay less than usual.
Judge every window on its own. Do not compare windows with each other.

Before the weights, write out your analysis:
1. Strategy: in 2 to 3 sentences, the rule you will apply to every window.
2. Then for each window, under its id: your read of the market (trend, structure, key levels as prices on the 100 scale), your weight and why, and the price on the 100 scale that would make you change your mind.
3. End with one JSON object mapping each window id to its weight, e.g. {"a1b2c3d4e5": 0.0, "f6a7b8c9d0": 1.0}. Nothing after it.
```

## Datenaufbereitung (render.py)
```python
"""E-023: the champion's 180-day daily table plus one line with the perp basis (backlog #36).

basis_frozen.csv (daten/) holds daily closes of BINANCE:<COIN>USDT.P from the TradingView connector
(raw tool results in daten/raw/, unchanged) next to the spot closes from tournament/candles.
Only rows up to and including the decision day are used (README §3 rule 5).

- B = close_perp / close_spot - 1, per day.
- B7 = mean of B over the last 7 days.
- Shown: percentile of today's B7 among the B7 values of the last 180 days (0 to 100), the
  scale-free form backlog #36 asks for. Fewer than 180 values or no series: "not available".

render(df, lookback) does not receive the coin. The coin is found by matching the spot closes of the
last 30 days in df against basis_frozen.csv; this needs exactly one match, else it raises.
"""

from pathlib import Path

import pandas as pd

from diamondhamster import ai

DATA = pd.read_csv(Path(__file__).parent / "daten" / "basis_frozen.csv", parse_dates=["date"])
DATA["date"] = DATA["date"].dt.tz_localize("UTC")
WINDOW, AVG = 180, 7


def coin_of(df: pd.DataFrame) -> str | None:
    tail = df["close"].astype(float).tail(30)
    hits = []
    for c, g in DATA.groupby("coin"):
        s = g.set_index("date")["close_spot"].reindex(tail.index)
        if s.notna().all() and ((s - tail).abs() <= 1e-9 * tail.abs()).all():
            hits.append(c)
    if len(hits) > 1:
        raise ValueError(f"window matches several coins: {hits}")
    return hits[0] if hits else None


def percentile(df: pd.DataFrame) -> int | None:
    c = coin_of(df)
    if c is None:
        return None
    g = DATA[(DATA.coin == c) & (DATA.date <= df.index[-1])].set_index("date").sort_index()
    if g.empty or g.index[-1] != df.index[-1]:
        return None
    b7 = (g.close_perp / g.close_spot - 1).rolling(AVG).mean().dropna().tail(WINDOW)
    if len(b7) < WINDOW:
        return None
    return int(round(100 * (b7 <= b7.iloc[-1]).mean()))


def line(df: pd.DataFrame) -> str:
    p = percentile(df)
    return "basis pct not available" if p is None else f"basis pct {p}"


def render(df: pd.DataFrame, lookback: int) -> str:
    return line(df) + "\n" + ai.compact(ai.window(df, df.index[-1], lookback))
```

## Bewertung gegen E-003M

| Coins | Wochen | Entscheidungen | Timing-Wert/Woche | Basis | Differenz | t | ohne beste Woche | Wochen besser | Exposure | Rank-IC |
|---|---|---|---|---|---|---|---|---|---|---|
| A (10) | 13 | 130 | -0.233 % | -0.244 % | 0.012 % | 0.15 | -0.013 % (ohne 2026-07-26) | 8/13 | 0.398 (Basis 0.463) | 0.054 |

**Urteil: kein messbarer Unterschied**

Verbrauch: 13 Claude-Aufrufe, 791k Zeichen, Listenpreis 5.46 USD (zählt gegen Aarons Limit, keine Rechnung)

## Was die KI gedacht hat (Beispiel: Entscheidung 2026-07-05)

Alle Wochen: [denken.md](denken.md)

````
## 1. Strategy

All ten windows are in a 180-day downtrend, with price roughly halved, a capitulation leg around days -33 to -30, and a bounce back to 100 in the last few days. So the default is a small position.

I add weight when the bounce has built higher lows or reclaimed the post-crash range high. I cut weight when the recent lows are still lower lows or when the basis percentile is high (above about 80), because that means leveraged longs are crowded. I add a little when the basis is low.

## 2. Windows

### 5cd9deec18 (AVAX)
- **Read:** The downtrend runs from 210 to 100. Price crashed from 129 to 97 on days -33 to -30, then flushed to 82 on day -16 on heavy volume. Since then it has made higher lows at 86, 92 and 95.
- **Levels:** Price is now pressing the 102–103 bounce highs. The 50-day average is around 110 and still overhead. Basis is 53, which is neutral.
- **Weight:** 0.25. The base is improving, but the trend is still down.
- **Change my mind:** Below 92 I go to 0. A daily close above 103 adds weight.

### b20d50a3ed (ADA)
- **Read:** This is the deepest fall, from 221 to a low of 73 on day -11. It then had a violent four-day squeeze from 76 to 101 on 2× volume.
- **Levels:** Momentum is strong, but the move is overextended and runs into the 94–97 congestion area from days -21 to -20. Basis is 74, so the rally is already getting crowded.
- **Weight:** 0.3, as a momentum position that I am not chasing.
- **Change my mind:** Below 92 (the gap fill) I exit. Holding above 105.5 adds weight.

### de5b1106b8 (BTC)
- **Read:** The decline is shallower, from 147 to 100. It made a low of 92.9 on day -30 and a retest low of 90.8 on day -4. That is roughly a double bottom.
- **Levels:** Resistance is at 104–106 (day -20). The 50-day average is around 112. Basis is 92, which is crowded.
- **Weight:** 0.2. The structure is acceptable, but the basis is a headwind.
- **Change my mind:** Below 94 I go to 0. Above 106 adds weight.

### 22071d7d55 (LTC)
- **Read:** The downtrend runs from 183 to 100. It made a low of 88.4 on day -29 and a marginally lower low of 85.7 on day -10. Price has now rallied to the top of the post-crash range (100.7 against 101.2 on day -20).
- **Levels:** Basis is 30, which is favorable because longs are not crowded.
- **Weight:** 0.35. A breakout attempt with cheap positioning.
- **Change my mind:** Below 93 I go to 0. A close above 101.5 adds weight.

### abb5f568a0 (LINK)
- **Read:** The downtrend runs from 174 to 100. It has a clean double bottom at 86.8 (day -29) and 86.9 (day -10), with a steady climb since.
- **Levels:** Resistance is at 106.7 (day -20). Basis is 68.
- **Weight:** 0.3.
- **Change my mind:** Below 93 I exit. Above 107 adds weight.

### 274987e703 (XRP)
- **Read:** The downtrend runs from 199 to 100. The lows are 90.7 (day -29) and 87.2 (day -10), a slightly lower low. A wick to 111.8 on day -20 was rejected.
- **Levels:** Price is mid-range at 100. Basis is 36, which is supportive.
- **Weight:** 0.3.
- **Change my mind:** Below 93 I go to 0. Above 103, and later 112, adds weight.

### 98d8a7210f (SOL)
- **Read:** The downtrend runs from 173 to 100. It made a low of 73.7 (day -29) and a clearly higher low of 78.5 (day -10). Price then broke above the post-crash high of 93.3 and has reclaimed the full pre-crash level of about 100 (day -34).
- **Levels:** This is the best structure of the set. The 50-day average is around 103. Basis is 55.
- **Weight:** 0.5.
- **Change my mind:** Below 94 (failed breakout) I cut to 0.2. Above 103 adds weight.

### ce237b240d (ETH)
- **Read:** The downtrend runs from 185 to 100. It has a double bottom at 84.3 and 84.7 and is now near 103.6 resistance (day -20).
- **Levels:** Basis is 99, an extreme reading for longs paying up, so I expect a pullback or squeeze risk.
- **Weight:** 0.15.
- **Change my mind:** Below 94 I go to 0. A close above 104 with the basis cooling adds weight.

### 069b406635 (DOT)
- **Read:** The downtrend runs from 254 to 100 and is still printing lower highs (118.8 on day -20) and lower lows (100.3 on day -29, then 90.2 on day -7).
- **Levels:** The bounce is so far only a lower high in the making. Basis is 86.
- **Weight:** 0.15.
- **Change my mind:** Below 93 I go to 0. Above 105 starts to break the lower-high sequence.

### e09dc87ec9 (DOGE)
- **Read:** A failed recovery: price rallied to 152 (day -52) and then rolled over hard. The lows are 99.7 (day -29) and 89.3 (day -5), a lower low. Price now sits under 105–107 resistance.
- **Levels:** Basis is 88.
- **Weight:** 0.1.
- **Change my mind:** Below 94 I go to 0. Above 107 adds weight.

## 3. Weights

{"5cd9deec18 (AVAX)": 0.25, "b20d50a3ed (ADA)": 0.3, "de5b1106b8 (BTC)": 0.2, "22071d7d55 (LTC)": 0.35, "abb5f568a0 (LINK)": 0.3, "274987e703 (XRP)": 0.3, "98d8a7210f (SOL)": 0.5, "ce237b240d (ETH)": 0.15, "069b406635 (DOT)": 0.15, "e09dc87ec9 (DOGE)": 0.1}
````

## Notizen
Backlog #36. Basis E-003M (nicht E-017, sauber statt dev-informiert). Daten: TradingView get_ohlcv 1D BINANCE:<COIN>USDT.P fuer die 10 Coins von Set A, abgerufen 2026-10-12; Tool-Antworten unveraendert in daten/raw/ (aus dem Sitzungsprotokoll extrahiert, nicht abgetippt), eingefroren in daten/basis_frozen.csv zusammen mit den Spot-Schlusskursen aus tournament/candles. render.py nutzt nur Zeilen bis zum Entscheidungstag und findet den Coin ueber die Spot-Schlusskurse der letzten 30 Tage (genau ein Treffer, sonst Abbruch); keine Harness-Aenderung. Format nach Backlog-Zeile (Perzentil 180 Tage), nicht nach basis.md par. 7 (365 Tage, mehrere Felder). Hypothese (Wissens-Thread, BIS WP 1087): hoher Carry, schwaechere Renditen ueber 1 bis 3 Monate; die KI senkt das Gewicht bei hoher Basis, Rank-IC steigt. Falsifiziert, wenn Rank-IC (E-003M: 0,059) und Timing-Wert (Differenz zu E-003M) nicht steigen. Champion-Regeln B-12/B-13/B-14: bei t >= 2 genau eine Wiederholung auf A, Urteil auf dem Mittel; B+C nur bei t >= 2. Karte nennt Anteil Gewichtsaenderungen unter 0,15, partiellen Anker (werkzeuge/anker.py) und Rank-IC. Vorlage aus Paragraph 4a unveraendert.
