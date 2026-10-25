# E-028: E-003M plus eine Marktzeile je Fenster mit dem US-Dollar-Index (TVC:DXY): Veraenderung ueber 4 und 13 Wochen in Prozent auf 0,5 gerundet und Perzentil des letzten Schlusskurses unter den Schlusskursen der letzten 180 Tage, Stand Vortag der Entscheidung; keine Niveaus; prompt.md erklaert die Zeile in zwei Saetzen ohne Handelsregel

- Achse: daten
- Basis: E-003M
- Daten: custom, 180 Tage
- Modell: claude-opus-5-5
- Werkzeug: f2794e9 versuche.py@764f343a01
- Thread: https://claude.ai/code/project/chan_01VH1Un8SQtbifKwzD9jDguD?thread=cmsg_01VH1Un8SQtbifKwzD9jDguDQrjQpHjXMhYMs39UxPo6LT

## Änderung zum Prompt der Basis
```diff
--- E-003M
+++ E-028
@@ -4,6 +4,7 @@
 Horizon is weeks to months; you do not need to trade often.
 
 Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
+Each window starts with one line `dollar index 4w C%, 13w C%, pct P` (or `dollar index not available`): the change of the US dollar index, which tracks the dollar against a basket of major currencies, over the last 4 and the last 13 weeks, rounded to 0.5 percent, and the percentile from 0 to 100 of its latest close among its daily closes over the last 180 days, all measured up to the day before the decision day. The line is market-wide and identical in every window; it gauges whether the dollar has been strengthening or weakening against other currencies.
 Judge every window on its own. Do not compare windows with each other.
 
 Before the weights, write out your analysis:
```

## Prompt
```
# T-001 baseline trader prompt

You decide the position for an asset over the next week: a number from 0 (flat) to 1 (fully long).
Horizon is weeks to months; you do not need to trade often.

Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
Each window starts with one line `dollar index 4w C%, 13w C%, pct P` (or `dollar index not available`): the change of the US dollar index, which tracks the dollar against a basket of major currencies, over the last 4 and the last 13 weeks, rounded to 0.5 percent, and the percentile from 0 to 100 of its latest close among its daily closes over the last 180 days, all measured up to the day before the decision day. The line is market-wide and identical in every window; it gauges whether the dollar has been strengthening or weakening against other currencies.
Judge every window on its own. Do not compare windows with each other.

Before the weights, write out your analysis:
1. Strategy: in 2 to 3 sentences, the rule you will apply to every window.
2. Then for each window, under its id: your read of the market (trend, structure, key levels as prices on the 100 scale), your weight and why, and the price on the 100 scale that would make you change your mind.
3. End with one JSON object mapping each window id to its weight, e.g. {"a1b2c3d4e5": 0.0, "f6a7b8c9d0": 1.0}. Nothing after it.
```

## Datenaufbereitung (render.py)
```python
"""E-028: the champion's 180-day daily table plus one market line with the US dollar index (backlog #39).

dxy_frozen.csv (daten/) holds the daily close of TVC:DXY from the TradingView connector (raw tool result in
daten/raw/, unchanged). Bars are stamped at the session open of the evening before (21:00 to 00:00 UTC); the
CSV carries the trading day (stamp + 3 hours). Weekdays only. The series is market-wide: every window of a
batch gets the identical line. Cut-off: only closes up to and including the day BEFORE the decision day.

- v   = last close on or before the cut-off.
- c4  = v / (last close on or before cut-off - 28 days) - 1, in percent rounded to 0.5.
- c13 = v / (last close on or before cut-off - 91 days) - 1, in percent rounded to 0.5.
- pct = percentile of v among all closes of the 180 calendar days ending at the cut-off (0 to 100).
- Missing data (no close within 5 days of a reference day, or history shorter than the window):
  "dollar index not available" (never 0).
Never shows index levels.
"""

from pathlib import Path

import pandas as pd

from diamondhamster import ai

DATA = pd.read_csv(Path(__file__).parent / "daten" / "dxy_frozen.csv", parse_dates=["date"])
S = DATA.set_index(DATA["date"].dt.tz_localize("UTC"))["close"].astype(float).sort_index()
WINDOW, W4, W13, MAXGAP = 180, 28, 91, 5


def last_close(day: pd.Timestamp) -> float | None:
    s = S[S.index <= day]
    if s.empty or (day - s.index[-1]).days > MAXGAP:
        return None
    return float(s.iloc[-1])


def half(x: float) -> str:
    r = round(2 * x) / 2
    return "0.0%" if r == 0 else f"{r:+.1f}%"


def stats(cutoff: pd.Timestamp) -> tuple[str, str, int] | None:
    start = cutoff - pd.Timedelta(days=WINDOW - 1)
    if S.empty or S.index[0] > start:
        return None
    v, b4, b13 = last_close(cutoff), last_close(cutoff - pd.Timedelta(days=W4)), last_close(cutoff - pd.Timedelta(days=W13))
    if None in (v, b4, b13):
        return None
    win = S[(S.index >= start) & (S.index <= cutoff)]
    pct = int(round(100 * (win <= v).mean()))
    return half(100 * (v / b4 - 1)), half(100 * (v / b13 - 1)), pct


def line(df: pd.DataFrame) -> str:
    st = stats(df.index[-1].normalize() - pd.Timedelta(days=1))
    if st is None:
        return "dollar index not available"
    return f"dollar index 4w {st[0]}, 13w {st[1]}, pct {st[2]}"


def render(df: pd.DataFrame, lookback: int) -> str:
    return line(df) + "\n" + ai.compact(ai.window(df, df.index[-1], lookback))
```

## Bewertung gegen E-003M

| Coins | Wochen | Entscheidungen | Timing-Wert/Woche | Basis | Differenz | t | ohne beste Woche | Wochen besser | Exposure | Rank-IC |
|---|---|---|---|---|---|---|---|---|---|---|
| A (10) | 13 | 130 | -0.173 % | -0.244 % | 0.071 % | 0.5 | -0.028 % (ohne 2026-08-16) | 7/13 | 0.433 (Basis 0.463) | 0.028 |

**Urteil: kein messbarer Unterschied**

Verbrauch: 13 Claude-Aufrufe, 797k Zeichen, Listenpreis 5.39 USD (zählt gegen Aarons Limit, keine Rechnung)

## Was die KI gedacht hat (Beispiel: Entscheidung 2026-07-05)

Alle Wochen: [denken.md](denken.md)

````
**Strategy:** All ten windows sit in a large downtrend: price fell from 150–250 to about 100, with a sharp leg down around day −30 and a rebound into day 0. I size the position on whether the post-crash structure shows higher lows and a break of the day −20 rebound high, and keep it small where lows are still falling. The dollar is strong (94th percentile, rising), a mild headwind for risk assets, so no weight goes above 0.5 without a confirmed trend reversal.

## 1aa52b2038 (DOGE)
- **Read:** Down from 193 to 100.
  - Crash low 99.7 (day −29), rebound high 114 (day −21).
  - Then a lower low at 89.3 (day −5).
  - The 3-day pop to 100 came on light volume. Lower highs and lower lows are intact.
- **Weight:** 0.2.
- **Change my mind:** a close above 106–108 would raise the weight; a close below 92 would take it to 0.

## 6e0157e226 (BTC)
- **Read:** Down from 147 to 100, but this window has the broadest base.
  - Lows at 94.3 (day −149), 92.9 (day −30) and 90.8 (day −4) form a rough triple-bottom area.
  - The range is roughly 91 to 130.
  - Price has recovered to the day −20 high of 105.7 zone.
- **Weight:** 0.3.
- **Change my mind:** a close above 105.7 would raise it; a close below 90.8 would take it to 0.

## 5cc2eb43bb (DOT)
- **Read:** Down from 253 to 100, the steepest decline.
  - Post-crash high 118.8 (day −20), new low 90.2 (day −7).
  - The bounce to 100 came on fading volume. The trend is clearly down.
- **Weight:** 0.15.
- **Change my mind:** a close above 105 would raise it; a close below 90 would take it to 0.

## cdcc9b0b0f (XRP)
- **Read:** Down from 199 to 100.
  - Lows have stepped down: 96.5 (day −149), 90.7 (day −29), 87.2 (day −9).
  - The day −20 spike high was 111.8.
  - Price rallied from about 89 to 100 in 3 days.
- **Weight:** 0.25.
- **Change my mind:** a close above 112 would raise it; a close below 88 would take it to 0.

## 999458be48 (ADA)
- **Read:** Down from 221 to 100.
  - Capitulation low 72.9 (day −10).
  - Then an explosive rally on high volume (about 2× average) from 76 to a 105.5 high.
  - That clears the day −20 high of 100.3.
  - This looks like a possible reversal thrust, but heavy overhead supply sits at 120–150.
- **Weight:** 0.4.
- **Change my mind:** a close above 105.5 would raise it; a close below 85 would take it to 0.

## bf1694cf1a (SOL)
- **Read:** Down from 173 to 100.
  - Crash low 73.7 (day −29), then a higher low at 78.5 (day −10).
  - Price closed above the day −20 high of 93.3, making a higher high.
  - This is the cleanest early uptrend structure of the ten.
  - Resistance sits at 100–107, the prior mid-window range.
- **Weight:** 0.5.
- **Change my mind:** a close above 103 would raise it; a close below 88 would cut it.

## 2a6c45f1d1 (ETH)
- **Read:** Down from 184 to 100.
  - Double bottom at 84.3 (day −29) and 84.7 (day −10).
  - Price now sits just under the day −20 high of 103.6.
  - Day 0 volume ticked up.
- **Weight:** 0.35.
- **Change my mind:** a close above 103.6 would raise it; a close below 84 would take it to 0.

## e6cc9a1348 (AVAX)
- **Read:** Down from 211 to 100.
  - Climactic low 82.0 (day −16) on 3× volume.
  - Then higher lows at 86.0 (day −10) and 92.2 (day −5).
  - Price is pressing the 102–103 highs.
- **Weight:** 0.35.
- **Change my mind:** a close above 103 would raise it; a close below 86 would take it to 0.

## 0e1ac8d54c (LTC)
- **Read:** Down from 183 to 100.
  - Lows at 88.4 (day −29), then a lower 85.7 (day −10).
  - Price closed at 100, at the day −20 high of 101.2, on average volume.
  - The trend is still down, but this is a test of resistance.
- **Weight:** 0.25.
- **Change my mind:** a close above 101.5 would raise it; a close below 89 would take it to 0.

## e7696b48e8 (LINK)
- **Read:** Down from 174 to 100.
  - Equal lows at 86.8 (day −29) and 86.9 (day −10).
  - The day −20 high was 106.7.
  - The bounce to 100 came on very low volume (0.34).
- **Weight:** 0.25.
- **Change my mind:** a close above 106.7 would raise it; a close below 87 would take it to 0.

{"1aa52b2038 (DOGE)": 0.2, "6e0157e226 (BTC)": 0.3, "5cc2eb43bb (DOT)": 0.15, "cdcc9b0b0f (XRP)": 0.25, "999458be48 (ADA)": 0.4, "bf1694cf1a (SOL)": 0.5, "2a6c45f1d1 (ETH)": 0.35, "e6cc9a1348 (AVAX)": 0.35, "0e1ac8d54c (LTC)": 0.25, "e7696b48e8 (LINK)": 0.25}
````

## Notizen
Backlog #39. Basis E-003M (Champion, sauber). Daten: TradingView get_ohlcv 1D TVC:DXY, 2026-01-01 bis 2026-09-26, abgerufen 2026-10-12 23:57 UTC; Tool-Antwort unveraendert in daten/raw/DXY.json (aus dem Sitzungsprotokoll extrahiert, nicht abgetippt), Anfrage in daten/raw/DXY.request.json; dazu ein Verbindungstest (3 Bars Okt 2026, ohne Datumsbereich in der Anfrage, nicht verwendet; log-fetches wertet die fehlende Spanne als 1970..2100). Eingefroren in daten/dxy_frozen.csv (Spalten date, close; 191 Handelstage 2026-01-02 bis 2026-09-25, nur Mo bis Fr, keine Duplikate); sha256 edd553897494e28834de87b1b548110ac1ed5ba53b80f2106678769ab6391773. Bars tragen den Zeitstempel der Sitzungseroeffnung am Vorabend (21 bis 00 Uhr UTC); Handelstag = Stempel + 3 Stunden. Rueckblick: frueheste Entscheidung 2026-07-05, Stichtag 07-04, 180-Tage-Perzentil ab 2026-01-06, 13-Wochen-Basis 2026-04-04; Abruf ab 2026-01-01, geloggt per log-fetches (B-19). Point-in-time: nur Schlusskurse bis einschliesslich Vortag der Entscheidung (Samstag, also Freitagsschluss). Darstellung (Standard, wo die Zeile offen ist): 4- und 13-Wochen-Veraenderung in Prozent auf 0,5 gerundet, ein Perzentil: Lage des letzten Schlusskurses unter allen Schlusskursen der 180 Kalendertage bis zum Stichtag (Backlog-Zeile nennt ein Perzentil der eigenen 180 Tage; E-025 nahm Perzentile der Veraenderungen); nie Indexniveaus; Marktzeile in jedem Fenster gleich (wie E-025); 'dollar index not available' bei Luecke > 5 Tage oder zu kurzer Historie. Pruefzeitraum: 13 verschiedene Zeilen, 4w von -2,5 bis +1,5 %, 13w von -1,0 bis +3,0 %, Perzentil 26 bis 99. Hypothese (Botupdate #2, marktuebergreifende Daten): Ein steigender Dollar senkt die Exposure, der Timing-Wert steigt. Falsifikator (aus der Backlog-Zeile, vor dem Lauf festgelegt): falsifiziert, wenn Timing-Wert und Rank-IC gegenueber E-003M nicht steigen (beide Differenzen <= 0; E-003M Rank-IC 0,059). Zusaetzlich berichtet: Korrelation der Exposure-Differenz zu E-003M je Woche mit der 4w- und 13w-Veraenderung (Erwartung negativ) und ob die Zeile die mittlere Folgewochenrendite vorhersagt (13 Punkte, schwach). Champion-Regeln B-12/B-13/B-14: bei t >= 2 genau eine Wiederholung auf A, Urteil auf dem Mittel; B+C nur bei t >= 2. Karte nennt Anteil Gewichtsaenderungen unter 0,15, partiellen Anker (werkzeuge/anker.py), Rank-IC und Exposure. Keine Harness-Aenderung; versuche.py vom Branch claude/project-thread-lupsy0 (README par. 4). Vorlage aus Paragraph 4a unveraendert.
