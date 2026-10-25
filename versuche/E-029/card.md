# E-029: E-003M plus eine Marktzeile je Fenster mit der BTC-Dominanz (CRYPTOCAP:BTC.D): Veraenderung ueber 4 und 13 Wochen in Prozentpunkten auf 0,5 gerundet und Perzentil des letzten Werts unter den Tageswerten der letzten 180 Tage, Stand Vortag der Entscheidung; kein Niveau; prompt.md erklaert die Zeile in zwei Saetzen ohne Handelsregel

- Achse: daten
- Basis: E-003M
- Daten: custom, 180 Tage
- Modell: claude-opus-5-5
- Werkzeug: f2794e9 versuche.py@764f343a01
- Thread: https://claude.ai/code/project/chan_01VH1Un8SQtbifKwzD9jDguD?thread=cmsg_01VH1Un8SQtbifKwzD9jDguDXVHsf8WEZWPGrD37YfmWyU

## Änderung zum Prompt der Basis
```diff
--- E-003M
+++ E-029
@@ -4,6 +4,7 @@
 Horizon is weeks to months; you do not need to trade often.
 
 Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
+Each window starts with one line `bitcoin dominance 4w Cpp, 13w Cpp, pct P` (or `bitcoin dominance not available`): the change of Bitcoin's share of the total crypto market capitalisation over the last 4 and the last 13 weeks, in percentage points rounded to 0.5, and the percentile from 0 to 100 of its latest daily value among its daily values over the last 180 days, all measured up to the day before the decision day. The line is market-wide and identical in every window; it gauges whether money in the crypto market has been shifting toward Bitcoin or away from it.
 Judge every window on its own. Do not compare windows with each other.
 
 Before the weights, write out your analysis:
```

## Prompt
```
# T-001 baseline trader prompt

You decide the position for an asset over the next week: a number from 0 (flat) to 1 (fully long).
Horizon is weeks to months; you do not need to trade often.

Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
Each window starts with one line `bitcoin dominance 4w Cpp, 13w Cpp, pct P` (or `bitcoin dominance not available`): the change of Bitcoin's share of the total crypto market capitalisation over the last 4 and the last 13 weeks, in percentage points rounded to 0.5, and the percentile from 0 to 100 of its latest daily value among its daily values over the last 180 days, all measured up to the day before the decision day. The line is market-wide and identical in every window; it gauges whether money in the crypto market has been shifting toward Bitcoin or away from it.
Judge every window on its own. Do not compare windows with each other.

Before the weights, write out your analysis:
1. Strategy: in 2 to 3 sentences, the rule you will apply to every window.
2. Then for each window, under its id: your read of the market (trend, structure, key levels as prices on the 100 scale), your weight and why, and the price on the 100 scale that would make you change your mind.
3. End with one JSON object mapping each window id to its weight, e.g. {"a1b2c3d4e5": 0.0, "f6a7b8c9d0": 1.0}. Nothing after it.
```

## Datenaufbereitung (render.py)
```python
"""E-029: the champion's 180-day daily table plus one market line with Bitcoin dominance (backlog #40).

btcd_frozen.csv (daten/) holds the daily close of CRYPTOCAP:BTC.D (Bitcoin's share of total crypto market
capitalisation, in percent) from the TradingView connector (raw tool result in daten/raw/, unchanged). Bars are
stamped 00:00 UTC of their day; the CSV carries that day. 7 days a week. The series is market-wide: every window
of a batch gets the identical line. Cut-off: only closes up to and including the day BEFORE the decision day.

- v   = close on the cut-off day.
- c4  = v - close 28 days earlier, in percentage points rounded to 0.5.
- c13 = v - close 91 days earlier, in percentage points rounded to 0.5.
- pct = percentile of v among all closes of the 180 calendar days ending at the cut-off (0 to 100).
- Missing data (no close within 2 days of a reference day, or history shorter than the window):
  "bitcoin dominance not available" (never 0).
Never shows the dominance level.
"""

from pathlib import Path

import pandas as pd

from diamondhamster import ai

DATA = pd.read_csv(Path(__file__).parent / "daten" / "btcd_frozen.csv", parse_dates=["date"])
S = DATA.set_index(DATA["date"].dt.tz_localize("UTC"))["close"].astype(float).sort_index()
WINDOW, W4, W13, MAXGAP = 180, 28, 91, 2


def last_close(day: pd.Timestamp) -> float | None:
    s = S[S.index <= day]
    if s.empty or (day - s.index[-1]).days > MAXGAP:
        return None
    return float(s.iloc[-1])


def half(x: float) -> str:
    r = round(2 * x) / 2
    return "0.0pp" if r == 0 else f"{r:+.1f}pp"


def stats(cutoff: pd.Timestamp) -> tuple[str, str, int] | None:
    start = cutoff - pd.Timedelta(days=WINDOW - 1)
    if S.empty or S.index[0] > start:
        return None
    v, b4, b13 = last_close(cutoff), last_close(cutoff - pd.Timedelta(days=W4)), last_close(cutoff - pd.Timedelta(days=W13))
    if None in (v, b4, b13):
        return None
    win = S[(S.index >= start) & (S.index <= cutoff)]
    pct = int(round(100 * (win <= v).mean()))
    return half(v - b4), half(v - b13), pct


def line(df: pd.DataFrame) -> str:
    st = stats(df.index[-1].normalize() - pd.Timedelta(days=1))
    if st is None:
        return "bitcoin dominance not available"
    return f"bitcoin dominance 4w {st[0]}, 13w {st[1]}, pct {st[2]}"


def render(df: pd.DataFrame, lookback: int) -> str:
    return line(df) + "\n" + ai.compact(ai.window(df, df.index[-1], lookback))
```

## Bewertung gegen E-003M

| Coins | Wochen | Entscheidungen | Timing-Wert/Woche | Basis | Differenz | t | ohne beste Woche | Wochen besser | Exposure | Rank-IC |
|---|---|---|---|---|---|---|---|---|---|---|
| A (10) | 13 | 130 | -0.268 % | -0.244 % | -0.023 % | -0.16 | -0.098 % (ohne 2026-09-13) | 6/13 | 0.421 (Basis 0.463) | 0.038 |

**Urteil: kein messbarer Unterschied**

Verbrauch: 13 Claude-Aufrufe, 798k Zeichen, Listenpreis 5.36 USD (zählt gegen Aarons Limit, keine Rechnung)

## Was die KI gedacht hat (Beispiel: Entscheidung 2026-07-05)

Alle Wochen: [denken.md](denken.md)

````
**Strategy:** All ten windows share the same shape: a six-month downtrend from roughly 170–250 down to the 100 area, a crash about 30 days ago, a second low 5–11 days ago, and a sharp rebound to 100 in the last four days. My rule:
- Keep a base exposure of about 0.2 while price is below the 50-day breakdown zone, because the major trend is still down.
- Add up to about 0.25 more where the post-crash structure shows higher lows and price has reclaimed the post-crash range high, which is the closest thing to a bottom.
- Bitcoin dominance is falling and sits at the 4th percentile of its 180-day range, so money is rotating toward altcoins. That is a mild tailwind, so I lean slightly up but do not chase.

## 4d6d196175 (ADA)
- **Trend and structure:** Price fell from 221 to 100, crashed from 124 to 83 at day -30, and set a lower low at 72.9 on day -10. It then rallied about 30% in four days on heavy volume (2.1–2.2× average) and reclaimed the day -20 high of 100.3.
- **Levels:** Overhead resistance is the breakdown gap at 105–112.
- **Weight:** Momentum is strong but the price is very extended after a vertical move inside a downtrend, so I take a moderate position.
- **Change my mind:** below 92, where the move would have failed.

## ee9e9bf839 (BTC)
- **Trend and structure:** This was a milder decline from 143. The rally peaked at 129, then a range of 91–105 held since day -32. There is a marginal higher low (90.8 versus 92.9), and the recovery is quiet on low volume.
- **Levels:** Resistance is 104–106.
- **Weight:** Modest.
- **Change my mind:** below 91.

## 79d01e6b3f (DOGE)
- **Trend and structure:** The lower-high sequence is intact (152 down to 118 down to 100). The low was 89.3 on day -5, slightly below the day -29 low of 99.7. That is a lower low, so the bounce is less convincing.
- **Levels:** Resistance is 105–114.
- **Weight:** Modest.
- **Change my mind:** below 92.

## 95eeaef0e6 (ETH)
- **Trend and structure:** There is a double bottom near 84.3–84.7 (days -29 and -9), and price is back at the neckline of 100–103.6.
- **Weight:** Constructive. I would add on a close above 104.
- **Change my mind:** below 88.

## be2bd8ee02 (XRP)
- **Trend and structure:** The low was 87.2 on day -10, with an earlier low of 90.7. Price is now 100, sitting under resistance at 102 and 112 (the day -20 spike high).
- **Weight:** Moderate.
- **Change my mind:** below 90.

## fbb7eceb7d (SOL)
- **Trend and structure:** This has the cleanest structure:
  - The day -29 low was 73.7, followed by a higher low of 78.5 on day -10.
  - Price closed above the day -20 high of 93.3, a break of the post-crash range, giving higher highs and higher lows.
- **Levels:** The next resistance is 100–105, the origin of the breakdown.
- **Weight:** The highest in this set.
- **Change my mind:** below 88.

## b5207ee9c4 (LTC)
- **Trend and structure:** There is a higher low at 85.7 versus 88.4 (wicks), and price is back at the day -20 high of 101. The breakdown zone at 110–114 sits overhead.
- **Weight:** Moderate.
- **Change my mind:** below 89.

## 2cabcb40a8 (LINK)
- **Trend and structure:** There is a double bottom at 86.8–87.0. Price is at 100, with the day -20 high of 106.7 as the next resistance.
- **Weight:** Moderate.
- **Change my mind:** below 89.

## cb9dce71fd (DOT)
- **Trend and structure:** The post-crash structure shows lower lows: 100.3 at day -29, then 90.2 at day -7. The bounce sits well below the day -20 high of 118.8, and the downtrend is cleanest here.
- **Weight:** The lowest in this set.
- **Change my mind:** a break below 92 would take me to flat; a move above 105 would make me add.

## ff1907cbab (AVAX)
- **Trend and structure:** Day -16 looked like a capitulation low at 82 on 3× volume. Since then the lows have stepped up (86.0, then 90.6, then 92.2), and price is now just under the day -20 high of 102.2.
- **Weight:** Constructive.
- **Change my mind:** below 90.

{"4d6d196175 (ADA)": 0.3, "ee9e9bf839 (BTC)": 0.25, "79d01e6b3f (DOGE)": 0.2, "95eeaef0e6 (ETH)": 0.35, "be2bd8ee02 (XRP)": 0.3, "fbb7eceb7d (SOL)": 0.45, "b5207ee9c4 (LTC)": 0.3, "2cabcb40a8 (LINK)": 0.3, "cb9dce71fd (DOT)": 0.2, "ff1907cbab (AVAX)": 0.35}
````

## Notizen
Backlog #40. Basis E-003M (Champion, sauber). Daten: TradingView get_ohlcv 1D CRYPTOCAP:BTC.D, 2026-01-01 bis 2026-09-26, abgerufen 2026-10-13 00:57 UTC; Tool-Antwort unveraendert in daten/raw/BTCD.json (aus dem Sitzungsprotokoll extrahiert, nicht abgetippt), Anfrage in daten/raw/BTCD.request.json; dazu ein Verbindungstest (3 Bars bis 2026-10-10, ohne date_from, nicht verwendet; log-fetches wertet die fehlende Spanne als 1970..). Eingefroren in daten/btcd_frozen.csv (Spalten date, close; 269 Tagesbars 2026-01-01 bis 2026-09-26 ohne Luecke, Stempel 00:00 UTC = Tag); sha256 8c487abd97706c4836f6b7d1266d9290aa8f1ab27599876b07ef1207702a6a42. Rueckblick: frueheste Entscheidung 2026-07-05, Stichtag 07-04, 180-Tage-Perzentil ab 2026-01-06, 13-Wochen-Basis 2026-04-04; Abruf ab 2026-01-01, geloggt per log-fetches (B-19). Point-in-time: nur Werte bis einschliesslich Vortag der Entscheidung. CRYPTOCAP-Reihen sind nicht streng point-in-time (TradingView kann Marktkapitalisierungen nachtraeglich korrigieren, z. B. beim Aufnehmen oder Entfernen von Coins); keine Vintages verfuegbar. Darstellung laut Backlog-Zeile (geht relative-staerke.md par. 7 mit 30/90 Tagen und 365-Tage-Perzentil vor, wie E-028): Veraenderung 4 und 13 Wochen in Prozentpunkten auf 0,5 gerundet, Perzentil des letzten Werts unter den Tageswerten der 180 Kalendertage bis zum Stichtag; nie das Dominanz-Niveau (verriete den Zyklus); Marktzeile in jedem Fenster gleich (wie E-025/E-028); 'bitcoin dominance not available' bei Luecke > 2 Tage oder zu kurzer Historie. Pruefzeitraum: 4w -1,0 bis +1,0 pp, 13w -2,0 bis +1,0 pp, Perzentil 4 bis 75. Hypothese (Backlog #40): Steigende Dominanz senkt das Gewicht der Altcoins, nicht von BTC; Rank-IC steigt. Falsifikator (vor dem Lauf festgelegt, aus der Backlog-Zeile): falsifiziert, wenn der Rank-IC gegenueber E-003M nicht steigt (E-003M Rank-IC 0,059). Zusaetzlich berichtet: Gewicht BTC getrennt von den Altcoins (Exposure je Woche, Differenz zu E-003M), Korrelation der Differenz mit der 4w/13w-Veraenderung (Erwartung: Altcoins negativ, BTC nicht negativ) und ob die Zeile die Folgewochen-Rendite der Altcoins gegenueber BTC vorhersagt (13 Punkte, schwach). Champion-Regeln B-12/B-13/B-14: bei t >= 2 genau eine Wiederholung auf A, Urteil auf dem Mittel; B+C nur bei t >= 2. Karte nennt Anteil Gewichtsaenderungen unter 0,15, partiellen Anker (werkzeuge/anker.py), Rank-IC und Exposure. Keine Harness-Aenderung; versuche.py vom Branch claude/project-thread-lupsy0 (README par. 4). Vorlage aus Paragraph 4a unveraendert.

## Auswertung (Thread)

- Falsifikator (vor dem Lauf): falsifiziert, wenn der Rank-IC nicht steigt. Rank-IC 0,038 gegen 0,059 bei E-003M: **falsifiziert**.
- BTC getrennt von den Altcoins: Gewicht BTC 0,462 (E-003M 0,527), Altcoins 0,416 (E-003M 0,456). Die Altcoins werden bei steigender 4w-Dominanz nicht gesenkt (Korrelation der Differenz −0,01); BTC wird stärker gesenkt als die Altcoins. Die Fenster sind anonym, die KI kann BTC nicht erkennen und wendet die Zeile auf alle Fenster gleich an. Details: [dominanz.md](dominanz.md).
- Anteil Gewichtsänderungen unter 0,15: 56 % (E-003-Läufe 58 / 56 / 43 %). Umschichtung 0,113. Partieller Anker 0,40 (E-003M 0,40).
- CRYPTOCAP-Reihen sind nicht streng point-in-time (nachträgliche Korrekturen der Marktkapitalisierung möglich, keine Vintages).
- Keine Wiederholung (t < 2), kein B+C. Champion bleibt E-003M.
