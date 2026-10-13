# E-025: E-003M plus eine Marktzeile je Fenster mit dem Wachstum der Stablecoin-Menge (CRYPTOCAP:USDT plus CRYPTOCAP:USDC) ueber 4 und 13 Wochen in Prozent, je mit Perzentil der eigenen letzten 180 Tageswerte, Stand Vortag der Entscheidung; in jedem Fenster derselbe Wortlaut; prompt.md erklaert die Zeile in zwei Saetzen ohne Handelsregel

- Achse: daten
- Basis: E-003M
- Daten: custom, 180 Tage
- Modell: claude-opus-5-5
- Werkzeug: f2794e9 versuche.py@764f343a01
- Thread: https://claude.ai/code/project/chan_01VH1Un8SQtbifKwzD9jDguD?thread=cmsg_01VH1Un8SQtbifKwzD9jDguD9gU6kcZ99my55Ki8fc6W4q

## Änderung zum Prompt der Basis
```diff
--- E-003M
+++ E-025
@@ -4,6 +4,7 @@
 Horizon is weeks to months; you do not need to trade often.
 
 Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
+Each window starts with one line `stablecoins 4w G% pct P, 13w G% pct P` (or `stablecoins not available`): the growth of the combined supply of the two largest dollar stablecoins over the last 4 and the last 13 weeks, measured up to the day before the decision day, each followed by its percentile from 0 to 100 among its own daily values over the last 180 days. The line is market-wide and identical in every window; it gauges how much new dollar liquidity is entering or leaving the crypto market as a whole.
 Judge every window on its own. Do not compare windows with each other.
 
 Before the weights, write out your analysis:
```

## Prompt
```
# T-001 baseline trader prompt

You decide the position for an asset over the next week: a number from 0 (flat) to 1 (fully long).
Horizon is weeks to months; you do not need to trade often.

Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
Each window starts with one line `stablecoins 4w G% pct P, 13w G% pct P` (or `stablecoins not available`): the growth of the combined supply of the two largest dollar stablecoins over the last 4 and the last 13 weeks, measured up to the day before the decision day, each followed by its percentile from 0 to 100 among its own daily values over the last 180 days. The line is market-wide and identical in every window; it gauges how much new dollar liquidity is entering or leaving the crypto market as a whole.
Judge every window on its own. Do not compare windows with each other.

Before the weights, write out your analysis:
1. Strategy: in 2 to 3 sentences, the rule you will apply to every window.
2. Then for each window, under its id: your read of the market (trend, structure, key levels as prices on the 100 scale), your weight and why, and the price on the 100 scale that would make you change your mind.
3. End with one JSON object mapping each window id to its weight, e.g. {"a1b2c3d4e5": 0.0, "f6a7b8c9d0": 1.0}. Nothing after it.
```

## Datenaufbereitung (render.py)
```python
"""E-025: the champion's 180-day daily table plus one market line with stablecoin growth (backlog #38).

stable_frozen.csv (daten/) holds the daily close of CRYPTOCAP:USDT and CRYPTOCAP:USDC from the TradingView
connector (raw tool results in daten/raw/, unchanged; market capitalisation, about the circulating supply)
and their sum. The series is market-wide: every window of a batch gets the identical line.
Cut-off: only values up to and including the day BEFORE the decision day are used (as E-024).

- g4  = S(day -1) / S(day -29) - 1, in percent with one decimal (4-week growth of USDT plus USDC).
- g13 = S(day -1) / S(day -92) - 1, in percent with one decimal (13-week growth).
- p4, p13 = percentile of today's g4 / g13 among its own 180 daily values ending at day -1 (0 to 100).
- Any value missing or too short a history: "stablecoins not available" (never 0).
Never shows dollar levels.
"""

from pathlib import Path

import pandas as pd

from diamondhamster import ai

DATA = pd.read_csv(Path(__file__).parent / "daten" / "stable_frozen.csv", parse_dates=["date"])
S = DATA.set_index(DATA["date"].dt.tz_localize("UTC"))["total"].astype(float).sort_index()
WINDOW, W4, W13 = 180, 28, 91


def growth(s: pd.Series, lag: int) -> pd.Series:
    prev = s.reindex(s.index - pd.Timedelta(days=lag))
    return pd.Series(100 * (s.values / prev.values - 1), index=s.index)


def stats(cutoff: pd.Timestamp) -> tuple[float, int, float, int] | None:
    s = S[S.index <= cutoff]
    if s.empty or s.index[-1] != cutoff:
        return None
    out = []
    for lag in (W4, W13):
        g = growth(s, lag).tail(WINDOW)
        if len(g) < WINDOW or g.isna().any() or (g.index[-1] - g.index[0]).days != WINDOW - 1:
            return None
        out += [round(float(g.iloc[-1]), 1), int(round(100 * (g <= g.iloc[-1]).mean()))]
    return tuple(out)


def line(df: pd.DataFrame) -> str:
    st = stats(df.index[-1] - pd.Timedelta(days=1))
    if st is None:
        return "stablecoins not available"
    return f"stablecoins 4w {st[0]:+.1f}% pct {st[1]}, 13w {st[2]:+.1f}% pct {st[3]}"


def render(df: pd.DataFrame, lookback: int) -> str:
    return line(df) + "\n" + ai.compact(ai.window(df, df.index[-1], lookback))
```

## Bewertung gegen E-003M

| Coins | Wochen | Entscheidungen | Timing-Wert/Woche | Basis | Differenz | t | ohne beste Woche | Wochen besser | Exposure | Rank-IC |
|---|---|---|---|---|---|---|---|---|---|---|
| A (10) | 13 | 130 | -0.407 % | -0.244 % | -0.163 % | -0.67 | -0.259 % (ohne 2026-09-20) | 7/13 | 0.332 (Basis 0.463) | 0.099 |

**Urteil: kein messbarer Unterschied**

Verbrauch: 13 Claude-Aufrufe, 797k Zeichen, Listenpreis 5.42 USD (zählt gegen Aarons Limit, keine Rechnung)

## Was die KI gedacht hat (Beispiel: Entscheidung 2026-07-05)

Alle Wochen: [denken.md](denken.md)

````
**Strategy:** I go long only when price has reclaimed the level where the last breakdown started and is making higher lows. A rebound inside a falling trend gets at most a small position. Contracting stablecoin supply (13-week growth at the 1st percentile, 4-week at the 13th) is a market-wide headwind, so I cap every weight well below full. Sharp 3–4 day bounces off fresh lows count as relief rallies until price clears the prior swing high.

## e39de0cbf1 (ADA)
- **Read:** A long downtrend from about 220 broke the 120–125 range at -33, capitulated to 82.7, and made a lower low at 72.9 (-10).
- **The bounce:** The last 4 days ran about 30% to a 105.5 high on heavy volume (2.1–2.2×). The -1 candle pushed above the -20 swing high (100.3), but day 0 closed back at 100.
- **Levels:** Resistance is 105.5 and then the 120–125 breakdown zone. Support is 92 and then 85.
- **Weight 0.2:** The thrust is strong, but it is unconfirmed and runs against both the trend and liquidity.
- **Change of mind:** I would add on closes above 106 and go flat below 85.

## 1312924976 (SOL)
- **Read:** The 100–104 range broke at -33, bottomed at 73.7 (-29), and made a higher low at 78.5 (-10).
- **Structure:** Price has climbed steadily back to 100–102, which is the old breakdown level. It shows higher lows and above-prior highs, the best structure in the set.
- **Levels:** Resistance is 101–104 (the old range). Support is 93 and then 86.
- **Weight 0.35:** The reclaim is not finished, and liquidity is negative.
- **Change of mind:** I would raise above 105 and cut below 92.

## 09d1bbf9de (LINK)
- **Read:** The 112–114 range broke, with a low of 86.8 (-30) and a double bottom at 86.9 (-10).
- **The bounce:** Price is back at 100–101, which equals the -21/-20 highs (101.5–106.7).
- **Levels:** Resistance is 101.5–106.7 and then 112. Support is 94 and then 87.
- **Weight 0.25:** The double bottom is constructive, but price is still below breakdown.
- **Change of mind:** I would raise above 107 and go flat below 87.

## 61c9c7ee15 (AVAX)
- **Read:** A breakdown from about 129 bottomed at 89.9 (-29) and retested 82 at -16 on high volume.
- **The bounce:** Higher lows followed at 86 and 88.8 (-11/-10), and price has ground up to 100–102.8.
- **Levels:** Resistance is 102.8 and then 116–129. Support is 92 and then 86.
- **Weight 0.25.**
- **Change of mind:** I would raise above 103 on closes and go flat below 86.

## 146bc1579c (LTC)
- **Read:** The 113–118 range broke, with a low of 88.4 (-29) and a slightly lower low at 85.7 (-10).
- **The bounce:** Price recovered to a 100 close, at the day's high, just under the -20/-19 highs of 101.
- **Levels:** Resistance is 101 and then 110–113. Support is 91 and then 86.
- **Weight 0.25.**
- **Change of mind:** I would raise above 102 and cut below 89.

## 4651a9929a (BTC)
- **Read:** The 115–122 range broke, with a low of 92.9 (-30). Lows since then have been shallower (90.8 at -4), and the move ran back to 100.
- **Structure:** The -20 high of 105.7 still caps price, so the highs are lower and the action is choppy.
- **Levels:** Resistance is 104–106 and then 116. Support is 96 and then 91.
- **Weight 0.2.**
- **Change of mind:** I would raise above 106 and go flat below 91.

## 0d03fde4a1 (ETH)
- **Read:** The 112–119 range broke, with a low of 84.3 (-29) and a retest at 84.7 (-9) that formed a double bottom.
- **The bounce:** The rebound reached 101.3, and the -20 high of 103.6 is still above it.
- **Levels:** Resistance is 103.6 and then 112. Support is 93 and then 85.
- **Weight 0.25.**
- **Change of mind:** I would raise above 104 and go flat below 85.

## e9051d21fa (DOT)
- **Read:** A persistent downtrend from about 250 broke 135, bottomed at 100.3 (-29), then made lower highs (118.8) and lower lows (90.2 at -7).
- **The bounce:** The current move to 100–102 is only a rebound to the first crash low.
- **Levels:** Resistance is 102 and then 113–119. Support is 93 and then 90.
- **Weight 0.15:** The trend is still down.
- **Change of mind:** I would raise above 115 and go flat below 90.

## 53afb5aa84 (DOGE)
- **Read:** The 128–130 range broke, with a low of 99.7 (-29), then lower highs (118.7) and a lower low of 89.3 (-5).
- **The bounce:** The move back to 100–102 has not changed the down structure.
- **Levels:** Resistance is 102 and then 114–119. Support is 92 and then 89.
- **Weight 0.15.**
- **Change of mind:** I would raise above 115 and go flat below 89.

## 650524bde0 (XRP)
- **Read:** The 113–116 range broke, with a low of 90.7 (-29) and a lower low at 87.2 (-9).
- **The bounce:** Price rebounded to 102.3 and closed at 100. The -20 spike high of 111.8 shows a lower-high pattern.
- **Levels:** Resistance is 102.3 and then 107–112. Support is 93 and then 87.
- **Weight 0.2.**
- **Change of mind:** I would raise above 108 and go flat below 87.

{"e39de0cbf1 (ADA)": 0.2, "1312924976 (SOL)": 0.35, "09d1bbf9de (LINK)": 0.25, "61c9c7ee15 (AVAX)": 0.25, "146bc1579c (LTC)": 0.25, "4651a9929a (BTC)": 0.2, "0d03fde4a1 (ETH)": 0.25, "e9051d21fa (DOT)": 0.15, "53afb5aa84 (DOGE)": 0.15, "650524bde0 (XRP)": 0.2}
````

## Notizen
Backlog #38. Basis E-003M (nicht E-017, sauber statt dev-informiert). Daten: TradingView get_ohlcv 1D CRYPTOCAP:USDT und CRYPTOCAP:USDC, 2025-10-01 bis 2026-09-27, abgerufen 2026-10-12 20:51 UTC; Tool-Antworten unveraendert in daten/raw/ (aus dem Sitzungsprotokoll extrahiert, nicht abgetippt), dazu ein Verbindungstest USDT 2026-09-25..10-01 (nicht verwendet). Eingefroren in daten/stable_frozen.csv (Spalten usdt, usdc, total); sha256 eadbe7b754d9d678b91838cc40a8c10755b6186efeef68a89c1fd5e0043ae030. Abstand der Bars geprueft: 362 Tagesbars ohne Luecke (nicht Wochenhistorie wie in boersenfluesse.md vermerkt); 2025-10-24 bis 10-26 drei identische USDT-Schlusswerte (Quelle, unveraendert uebernommen). Rueckblick: frueheste Abfrage 2025-10-07 (Stichtag 2026-07-04 minus 179 Tage Perzentil minus 91 Tage 13-Wochen-Basis), Abruf ab 2025-10-01; geloggt per log-fetches (B-19). Standards, wo Zeile und Quellen abweichen: (1) Marktzeile in jedem Fenster wiederholt statt Harness-Aenderung fuer einen Batch-Kopf; (2) Perzentil ueber 180 Tage laut Backlog-Zeile, nicht 52 Wochen wie boersenfluesse.md par. 7; (3) Stichtag Vortag der Entscheidung wie E-024 (par. 7 nennt den Entscheidungstag; strenger); (4) Prozentwerte mit einer Nachkommastelle zusaetzlich zum Perzentil, weil das Vorzeichen (Netto-Emission oder -Ruecknahme) im Perzentil allein fehlt (par. 7 verlangt es); nie Dollar-Niveaus. Keine Harness-Aenderung; versuche.py vom Branch claude/project-thread-lupsy0 (README par. 4). Hypothese (Wissens-Thread): Die Exposure folgt dem Liquiditaetsregime, der Timing-Wert steigt. Falsifikator (vor dem Lauf festgelegt): falsifiziert, wenn der Timing-Wert gegenueber E-003M nicht steigt (Differenz <= 0) oder die mittlere Exposure je Woche nicht mit der Zeile korreliert (Korrelation mittleres Wochengewicht zu 4w-Perzentil und zu 13w-Perzentil beide unter 0,3). Rank-IC (E-003M 0,059) wird berichtet; die Zeile ist im Querschnitt konstant und kann ihn nur indirekt aendern. Zusaetzlich berichtet: ob die Zeile selbst die mittlere Rendite der Folgewoche ueber die 13 Wochen vorhersagt (nur 13 Punkte, schwach). Champion-Regeln B-12/B-13/B-14: bei t >= 2 genau eine Wiederholung auf A, Urteil auf dem Mittel; B+C nur bei t >= 2. Karte nennt Anteil Gewichtsaenderungen unter 0,15, partiellen Anker (werkzeuge/anker.py), Rank-IC und Exposure. Vorlage aus Paragraph 4a unveraendert.
