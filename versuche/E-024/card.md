# E-024: E-003M plus eine Zeile je Fenster mit dem Open Interest: 4-Wochen-Veraenderung in Prozent und Perzentil der eigenen letzten 180 Tageswerte (BINANCE:<COIN>USDT.P_OI, in Coins), Stand Vortag der Entscheidung; prompt.md erklaert die Zeile in zwei Saetzen ohne Handelsregel

- Achse: daten
- Basis: E-003M
- Daten: custom, 180 Tage
- Modell: claude-opus-5-5
- Werkzeug: f2794e9 versuche.py@2a621dd441
- Thread: https://claude.ai/code/project/chan_01VH1Un8SQtbifKwzD9jDguD?thread=cmsg_01VH1Un8SQtbifKwzD9jDguDTdYRXudn4CfouaHsrsVs2p

## Änderung zum Prompt der Basis
```diff
--- E-003M
+++ E-024
@@ -4,6 +4,7 @@
 Horizon is weeks to months; you do not need to trade often.
 
 Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
+Each window starts with one line `oi 4w C%, oi pct P` (or `oi not available`): the open interest of the asset's perpetual futures, i.e. the number of open contracts counted in units of the asset, measured up to the day before the decision day; C is its change over the last 4 weeks in percent, P its percentile from 0 to 100 among its own daily values over the last 180 days. A high percentile means more leveraged positions are open than usual for this asset, a low percentile fewer.
 Judge every window on its own. Do not compare windows with each other.
 
 Before the weights, write out your analysis:
```

## Prompt
```
# T-001 baseline trader prompt

You decide the position for an asset over the next week: a number from 0 (flat) to 1 (fully long).
Horizon is weeks to months; you do not need to trade often.

Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
Each window starts with one line `oi 4w C%, oi pct P` (or `oi not available`): the open interest of the asset's perpetual futures, i.e. the number of open contracts counted in units of the asset, measured up to the day before the decision day; C is its change over the last 4 weeks in percent, P its percentile from 0 to 100 among its own daily values over the last 180 days. A high percentile means more leveraged positions are open than usual for this asset, a low percentile fewer.
Judge every window on its own. Do not compare windows with each other.

Before the weights, write out your analysis:
1. Strategy: in 2 to 3 sentences, the rule you will apply to every window.
2. Then for each window, under its id: your read of the market (trend, structure, key levels as prices on the 100 scale), your weight and why, and the price on the 100 scale that would make you change your mind.
3. End with one JSON object mapping each window id to its weight, e.g. {"a1b2c3d4e5": 0.0, "f6a7b8c9d0": 1.0}. Nothing after it.
```

## Datenaufbereitung (render.py)
```python
"""E-024: the champion's 180-day daily table plus one line with open interest (backlog #37).

oi_frozen.csv (daten/) holds the daily close of BINANCE:<COIN>USDT.P_OI from the TradingView connector
(raw tool results in daten/raw/, unchanged; values are open contracts in coins, not USD) next to the
spot closes from tournament/candles.
Cut-off: only OI values up to and including the day BEFORE the decision day are used
(research/wissen/bausteine/open-interest.md par. 7; stricter than README par. 3 rule 5).

- chg = OI(day -1) / OI(day -29) - 1, in percent, rounded to whole percent (4-week change).
- pct = percentile of OI(day -1) among the 180 daily OI values ending at day -1 (0 to 100).
- Fewer than 180 values, a missing day or no series: "oi not available" (never 0).

render(df, lookback) does not receive the coin. The coin is found by matching the spot closes of the
last 30 days in df against oi_frozen.csv (same method as E-023); exactly one match, else it raises.
"""

from pathlib import Path

import pandas as pd

from diamondhamster import ai

DATA = pd.read_csv(Path(__file__).parent / "daten" / "oi_frozen.csv", parse_dates=["date"])
DATA["date"] = DATA["date"].dt.tz_localize("UTC")
WINDOW, WEEKS4 = 180, 28


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


def oi_stats(df: pd.DataFrame) -> tuple[int, int] | None:
    c = coin_of(df)
    if c is None:
        return None
    cutoff = df.index[-1] - pd.Timedelta(days=1)
    oi = DATA[(DATA.coin == c) & (DATA.date <= cutoff)].set_index("date")["oi"].sort_index().dropna()
    if oi.empty or oi.index[-1] != cutoff:
        return None
    win = oi.tail(WINDOW)
    if len(win) < WINDOW or (win.index[-1] - win.index[0]).days != WINDOW - 1:
        return None
    base = oi.get(cutoff - pd.Timedelta(days=WEEKS4))
    if base is None or base <= 0:
        return None
    chg = int(round(100 * (oi.iloc[-1] / base - 1)))
    pct = int(round(100 * (win <= win.iloc[-1]).mean()))
    return chg, pct


def line(df: pd.DataFrame) -> str:
    s = oi_stats(df)
    return "oi not available" if s is None else f"oi 4w {s[0]:+d}%, oi pct {s[1]}"


def render(df: pd.DataFrame, lookback: int) -> str:
    return line(df) + "\n" + ai.compact(ai.window(df, df.index[-1], lookback))
```

## Bewertung gegen E-003M

| Coins | Wochen | Entscheidungen | Timing-Wert/Woche | Basis | Differenz | t | ohne beste Woche | Wochen besser | Exposure | Rank-IC |
|---|---|---|---|---|---|---|---|---|---|---|
| A (10) | 13 | 130 | -0.418 % | -0.244 % | -0.173 % | -0.63 | -0.231 % (ohne 2026-07-05) | 8/13 | 0.399 (Basis 0.463) | 0.054 |

**Urteil: kein messbarer Unterschied**

Verbrauch: 13 Claude-Aufrufe, 794k Zeichen, Listenpreis 5.47 USD (zählt gegen Aarons Limit, keine Rechnung)

## Was die KI gedacht hat (Beispiel: Entscheidung 2026-07-05)

Alle Wochen: [denken.md](denken.md)

````
**1. Strategy**

I follow the trend and want structure to confirm it. A window gets meaningful weight only if price has made higher lows and reclaimed the level where it broke down. When price sits below a falling medium-term trend and is still making lower lows, I stay mostly flat and keep only a small stake for the bounce. Open interest adjusts the weight: a high percentile with rising OI in a downtrend means crowded leverage, so I cut weight, while low or falling OI means positioning has been flushed, so I allow a bit more.

**2. Windows**

**d878df8da1 (AVAX)**
- **Read:** Long downtrend from about 210. The 125–145 range broke at day -33, with capitulation lows at 82 (day -16, 3x volume).
- **Structure:** Rising lows since then: 86, 92, 95.5. Price has reclaimed 100 and sits just under resistance at 102–103. The next resistance is 112–116.
- **Open interest:** Low at the 22nd percentile and down 9%, so leverage has been flushed.
- **Weight:** 0.3, an early base still below the medium-term trend.
- **Change my mind:** Below 92 I go flat. Above 103 I add.

**c80a06a508 (XRP)**
- **Read:** The 113–128 range broke to 92. The bounce failed at 111.8, then price made a lower low at 87.2 (day -9). It has rallied back to 100.
- **Levels:** Resistance at 102 and 107–112.
- **Open interest:** 94th percentile and up 9%, so leverage is crowded into a downtrend.
- **Weight:** 0.15.
- **Change my mind:** Below 88 I go flat. Above 107 I add.

**61070d3df6 (ETH)**
- **Read:** Double bottom at about 84.5 (days -29 and -9). Price has rallied to 100, under resistance at 103.6. The prior range was 110–120.
- **Open interest:** 88th percentile and flat over 4 weeks.
- **Weight:** 0.2.
- **Change my mind:** Below 87 I go flat. Above 104 I add.

**f6235111be (LINK)**
- **Read:** Double bottom at about 87 (days -29 and -10). Price is at 100, with resistance at 106.7 and the 112–120 breakdown zone above.
- **Open interest:** Neutral at the 48th percentile.
- **Weight:** 0.25.
- **Change my mind:** Below 88 I go flat. Above 107 I add.

**d3a53f8905 (ADA)**
- **Read:** The worst breakdown, 125 to 73, with a lower low on day -10. That was followed by a vertical 35% rally in five days on heavy volume, rejected at 105.5.
- **Levels:** The old breakdown zone, 110–122, is far above.
- **Open interest:** 99th percentile and up 9%, so the rally is leverage-driven and fragile.
- **Weight:** 0.15.
- **Change my mind:** Below 92 I go flat. A close above 106 would raise it.

**2b0414cdc8 (LTC)**
- **Read:** Low at 85.7 (day -10). A grinding recovery is now testing the 100–101 highs from days -20 to -19. Day 0 closed near its high.
- **Levels:** The breakdown range of 110–115 is next.
- **Open interest:** 40th percentile with a modest increase, so positioning is healthy.
- **Weight:** 0.3.
- **Change my mind:** Below 91 I cut. Above 102 I add.

**528ef10d70 (BTC)**
- **Read:** Lows at 92.9, 91.3 and 90.8, so a flat-to-lower base. Price is at 100, under resistance at 104–106. The prior range was 115–128.
- **Open interest:** 95th percentile, crowded.
- **Weight:** 0.15.
- **Change my mind:** Below 90.5 I go flat. Above 106 I add.

**71aa8f728b (DOT)**
- **Read:** A persistent pattern of lower highs and lower lows: 100.3, then 93, then 90.2 (day -7). The bounce to 100 sits well under the lower high at 118.8 (day -20).
- **Open interest:** 66th percentile and up 7%.
- **Weight:** 0.1, the downtrend is intact.
- **Change my mind:** Below 90 I go flat. Above 105 I add.

**4391487662 (SOL)**
- **Read:** The strongest structure here. The low was 73.7 (day -29), followed by a higher low at 78.5 (day -10). Price broke through 93 resistance and is now back at the pre-crash range of about 100–106. It is reclaiming the breakdown level.
- **Open interest:** 73rd percentile and only up 2%, so not building aggressively.
- **Weight:** 0.5.
- **Change my mind:** Below 92 I cut. Holding above 106 lets me add more.

**8d82a8f2bc (DOGE)**
- **Read:** The 125–150 range broke to 99.7. The bounce failed at 118.7, then price made a lower low at 89.3 (day -5). It is back at 100, under resistance at 102–108.
- **Open interest:** Up 16% to the 86th percentile, so leverage is piling into a downtrend.
- **Weight:** 0.1.
- **Change my mind:** Below 89 I go flat. Above 108 I add.

**3. Weights**

{"d878df8da1 (AVAX)": 0.3, "c80a06a508 (XRP)": 0.15, "61070d3df6 (ETH)": 0.2, "f6235111be (LINK)": 0.25, "d3a53f8905 (ADA)": 0.15, "2b0414cdc8 (LTC)": 0.3, "528ef10d70 (BTC)": 0.15, "71aa8f728b (DOT)": 0.1, "4391487662 (SOL)": 0.5, "8d82a8f2bc (DOGE)": 0.1}
````

## Notizen
Backlog #37. Basis E-003M (nicht E-017, sauber statt dev-informiert). Daten: TradingView get_ohlcv 1D BINANCE:<COIN>USDT.P_OI fuer die 10 Coins von Set A, 2025-09-01 bis 2026-09-27, abgerufen 2026-10-12; Tool-Antworten unveraendert in daten/raw/ (aus dem Sitzungsprotokoll extrahiert, nicht abgetippt), eingefroren in daten/oi_frozen.csv mit den Spot-Schlusskursen aus tournament/candles; sha256 f49be69181f10f139a6867e5e2e2b2ba3c04d153546400daa33ddc6db0a7493f. 392 Tage je Coin, keine Luecken. Einheit: Coins, nicht USD (BTC ca. 88k bei Kurs 109k = ca. 9,7 Mrd USD, passt zur Binance-Groessenordnung). Daten-Stichtag: Schlusswert des Vortags der Entscheidung (open-interest.md par. 7; strenger als E-023, das bis zum Entscheidungstag nahm). Format nach Backlog-Zeile (4-Wochen-Veraenderung und 180-Tage-Perzentil), nicht nach par. 7 (mehr Felder); die Zeile gewinnt. Keine Harness-Aenderung; versuche.py vom Branch claude/project-thread-lupsy0 (README par. 4). Hypothese (wie #36, Wissens-Thread): OI misst Gedraenge; die KI senkt das Gewicht bei hohem OI-Perzentil bzw. starkem OI-Anstieg, Rank-IC steigt. Falsifikator: falsifiziert, wenn Rank-IC (E-003M: 0,059) und Timing-Wert (Differenz zu E-003M) nicht steigen. Champion-Regeln B-12/B-13/B-14: bei t >= 2 genau eine Wiederholung auf A, Urteil auf dem Mittel; B+C nur bei t >= 2. Karte nennt Anteil Gewichtsaenderungen unter 0,15, partiellen Anker (werkzeuge/anker.py), Rank-IC und Exposure. Vorlage aus Paragraph 4a unveraendert.
