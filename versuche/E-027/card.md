# E-027: E-003M plus eine Marktzeile je Fenster mit US-M2 (ECONOMICS:USM2, Monat frueh. 8 Wochen nach Datumsstempel bekannt): YoY in ganzen Prozent und Richtung der annualisierten 3-Monats-Rate mit Seriendauer, keine Niveaus; prompt.md erklaert die Zeile in zwei Saetzen ohne Handelsregel

- Achse: daten
- Basis: E-003M
- Daten: custom, 180 Tage
- Modell: claude-opus-5-5
- Werkzeug: f2794e9 versuche.py@764f343a01
- Thread: https://claude.ai/code/project/chan_01VH1Un8SQtbifKwzD9jDguD?thread=cmsg_01VH1Un8SQtbifKwzD9jDguD5SG2M9jB5Gx3UVqrBtKvi6

## Änderung zum Prompt der Basis
```diff
--- E-003M
+++ E-027
@@ -4,6 +4,7 @@
 Horizon is weeks to months; you do not need to trade often.
 
 Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
+Each window starts with one line `US money supply M2: year-on-year G%, 3-month growth rate rising|falling for N months` (or `US money supply not available`): the growth of the US M2 money supply over the last twelve months in whole percent, and whether its annualised three-month growth rate rose or fell against the month before and for how many months in a row, using only the latest month published at least eight weeks before the decision day. The line is market-wide and identical in every window; it gauges whether the dollar money supply is expanding faster or slower.
 Judge every window on its own. Do not compare windows with each other.
 
 Before the weights, write out your analysis:
```

## Prompt
```
# T-001 baseline trader prompt

You decide the position for an asset over the next week: a number from 0 (flat) to 1 (fully long).
Horizon is weeks to months; you do not need to trade often.

Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
Each window starts with one line `US money supply M2: year-on-year G%, 3-month growth rate rising|falling for N months` (or `US money supply not available`): the growth of the US M2 money supply over the last twelve months in whole percent, and whether its annualised three-month growth rate rose or fell against the month before and for how many months in a row, using only the latest month published at least eight weeks before the decision day. The line is market-wide and identical in every window; it gauges whether the dollar money supply is expanding faster or slower.
Judge every window on its own. Do not compare windows with each other.

Before the weights, write out your analysis:
1. Strategy: in 2 to 3 sentences, the rule you will apply to every window.
2. Then for each window, under its id: your read of the market (trend, structure, key levels as prices on the 100 scale), your weight and why, and the price on the 100 scale that would make you change your mind.
3. End with one JSON object mapping each window id to its weight, e.g. {"a1b2c3d4e5": 0.0, "f6a7b8c9d0": 1.0}. Nothing after it.
```

## Datenaufbereitung (render.py)
```python
"""E-027: the champion's 180-day daily table plus one market line with US M2 money supply (backlog #16).

m2_frozen.csv (daten/) holds monthly ECONOMICS:USM2 from the TradingView connector (raw tool result in
daten/raw/, unchanged), dated by the month it covers. TradingView has no vintages: the history is the
revised one, not what was known at the time (bias noted on the card).
The series is market-wide: every window of a batch gets the identical line.
Point in time: a month counts as known only from its datestamp + 56 days (8 weeks, hinweise-forschung.md),
judged on the day BEFORE the decision day.

- yoy  = M(m) / M(m-12) - 1 for the latest known month m, in whole percent.
- g3   = annualised 3-month growth rate M(m) / M(m-3); its direction vs the month before (rising/falling)
         and for how many consecutive months it has moved that way (capped: "12 or more").
- Any value missing or too short a history: "US money supply not available" (never 0).
Never shows levels or dates.
"""

from pathlib import Path

import pandas as pd

from diamondhamster import ai

DATA = pd.read_csv(Path(__file__).parent / "daten" / "m2_frozen.csv", parse_dates=["month"])
M = DATA.set_index(DATA["month"].dt.tz_localize("UTC"))["value"].astype(float).sort_index()
LAG, CAP = pd.Timedelta(days=56), 12


def stats(cutoff: pd.Timestamp) -> tuple[int, str, int] | None:
    s = M[M.index + LAG <= cutoff]
    if s.empty:
        return None
    m = s.index[-1]
    want = pd.date_range(end=m, periods=len(s), freq="MS")
    if not (s.index == want).all():
        return None
    if len(s) < 13:
        return None
    yoy = 100 * (s.iloc[-1] / s.iloc[-13] - 1)
    g3 = (s / s.shift(3)) ** 4 - 1
    step = g3.diff().dropna()
    if step.empty or step.iloc[-1] == 0:
        return None
    up = step.iloc[-1] > 0
    n = 0
    for v in step.iloc[::-1]:
        if (v > 0) != up or v == 0:
            break
        n += 1
    full = n == len(step)
    if full and n < CAP:
        return None
    return int(round(yoy)), "rising" if up else "falling", min(n, CAP)


def line(df: pd.DataFrame) -> str:
    st = stats(df.index[-1] - pd.Timedelta(days=1))
    if st is None:
        return "US money supply not available"
    months = "12 or more months" if st[2] >= CAP else f"{st[2]} month" + ("s" if st[2] > 1 else "")
    return f"US money supply M2: year-on-year {st[0]:+d}%, 3-month growth rate {st[1]} for {months}"


def render(df: pd.DataFrame, lookback: int) -> str:
    return line(df) + "\n" + ai.compact(ai.window(df, df.index[-1], lookback))
```

## Bewertung gegen E-003M

| Coins | Wochen | Entscheidungen | Timing-Wert/Woche | Basis | Differenz | t | ohne beste Woche | Wochen besser | Exposure | Rank-IC |
|---|---|---|---|---|---|---|---|---|---|---|
| A (10) | 13 | 130 | -0.103 % | -0.244 % | 0.142 % | 1.72 | 0.089 % (ohne 2026-08-16) | 10/13 | 0.454 (Basis 0.463) | 0.048 |

**Urteil: kein messbarer Unterschied**

Verbrauch: 13 Claude-Aufrufe, 802k Zeichen, Listenpreis 5.37 USD (zählt gegen Aarons Limit, keine Rechnung)

## Was die KI gedacht hat (Beispiel: Entscheidung 2026-07-05)

Alle Wochen: [denken.md](denken.md)

````
**Strategy.** I weight each window by its own trend structure. The 180-day downtrend sets a low base weight. I add to it when the bounce off the recent lows has made higher lows or reclaimed the last bounce high, and I cut it when the last low undercut the post-crash low. The M2 line (+5% and accelerating for 4 months) is mildly supportive and the same for every window, so it nudges all weights slightly up but does not separate them.

**90c1c89fcd (BTC)**
- **Read:** Primary downtrend from about 147. It crashed to 92.9 (day -30), bounced to 105.7 (day -20), then made a slightly lower low at 90.8 (day -4). It is now 100, a weak rebound on low volume, and still below the 105–110 range.
- **Weight: 0.3.** The low was lower and the rebound has not yet reclaimed any resistance.
- **Change my mind:** a close above 105.7 means I add; a close below 90.8 means flat.

**8d80589cd8 (SOL)**
- **Read:** It crashed to 73.7 (day -29), then made higher lows at 78.5 (day -10) and 85.5. It broke above the 93.3 bounce high and traded up to 102.9. This is the clearest higher-low, higher-high recovery, though it is still far below the 105–120 range from before the crash.
- **Weight: 0.6.**
- **Change my mind:** below 92 cut; below 85 flat; above 103 add.

**4860e6955a (XRP)**
- **Read:** The low was 90.7 (day -29), and the retest at 87.2 (day -9) undercut it. It has bounced to 100 but is still below the 111.8 spike high from day -20.
- **Weight: 0.35.**
- **Change my mind:** above 107 add; below 87 flat.

**5f94d437ca (ETH)**
- **Read:** A double bottom at 84.3 and 84.7 (days -29 and -9). It is now 100, just under the 103.6 neckline.
- **Weight: 0.45.**
- **Change my mind:** a close above 103.6 means I add; below 84 flat.

**bb8cd5b309 (DOGE)**
- **Read:** It failed from the 152 rally and crashed to 99.7. It bounced to 118.7, then made a lower low at 89.3 (day -5). The sequence of lower highs and lower lows is intact.
- **Weight: 0.25.**
- **Change my mind:** above 108 add; below 89 flat.

**e72e6bf1e3 (LTC)**
- **Read:** Lows at 88.4 (day -29) and then 85.7 (day -10), which is lower. The steady recovery has brought it to 100, right at the 101.2 bounce high.
- **Weight: 0.35.**
- **Change my mind:** a close above 101.2 means I add; below 85.7 flat.

**d73af95893 (AVAX)**
- **Read:** A capitulation low at 82.0 (day -16, on 3× volume). Since then it has made higher lows near 86 and then 92, and it is now 100, testing 102.2. The structure is constructive.
- **Weight: 0.45.**
- **Change my mind:** above 102.8 add; below 91 cut.

**671ff362c4 (ADA)**
- **Read:** It made lower lows at 78.4 and then 72.9 (day -10). It then rose from 76 to 105.5 in four days on 2× volume, a high-volume V-reversal that cleared the 100.3 bounce high. A move that fast can retrace, and 120+ is still far above.
- **Weight: 0.5.**
- **Change my mind:** below 85 flat; holding above 97 with a push through 105.5 means I add.

**a67e086bf6 (DOT)**
- **Read:** It crashed to 100.3, bounced to 118.8 (lower than the earlier ~150 highs), then made a lower low at 90.2 (day -7). It is now 100, and the downtrend structure is intact.
- **Weight: 0.25.**
- **Change my mind:** above 111 add; below 90 flat.

**cf332e3a3d (LINK)**
- **Read:** A double bottom at 86.8 and 86.9 (days -29 and -10). It is now 100, below the 106.7 neckline.
- **Weight: 0.4.**
- **Change my mind:** above 106.7 add; below 86.8 flat.

{"90c1c89fcd (BTC)": 0.3, "8d80589cd8 (SOL)": 0.6, "4860e6955a (XRP)": 0.35, "5f94d437ca (ETH)": 0.45, "bb8cd5b309 (DOGE)": 0.25, "e72e6bf1e3 (LTC)": 0.35, "d73af95893 (AVAX)": 0.45, "671ff362c4 (ADA)": 0.5, "a67e086bf6 (DOT)": 0.25, "cf332e3a3d (LINK)": 0.4}
````

## Notizen
Backlog #16. Basis E-003M (Champion, sauber). Daten: TradingView get_economic_data ECONOMICS:USM2 (monatlich, Datum = Bezugsmonat, liquiditaet-m2.md par. 7), 2023-01-01 bis 2026-10-12, abgerufen 2026-10-12 23:00 UTC; Tool-Antwort unveraendert in daten/raw/USM2.json (aus dem Sitzungsprotokoll extrahiert, nicht abgetippt), Anfrage in daten/raw/USM2.request.json. Eingefroren ab 2025-01 in daten/m2_frozen.csv (20 Monate, Spalten month, value); sha256 7b30a8117918263b994bf1ab739f9e4e20749ffd2b37d336e342f92d31da5b70. Der Abruf reichte bis 2023-01 und damit zwei Jahre weiter zurueck als noetig (Fehler beim Zuschnitt der Anfrage, ein Abruf, kein zweiter); benutzt werden nur die eingefrorenen Monate ab 2025-01: frueheste Entscheidung 2026-07-05 kennt Mai 2026, YoY braucht Mai 2025, Serien-Zaehlung bis 12 Monate braucht die 3-Monats-Rate ab April 2025 und damit Januar 2025. Geloggt per log-fetches (B-19). Point-in-time: ein Monat gilt erst ab Datumsstempel + 56 Tage als bekannt (hinweise-forschung.md, ersetzt die 5 Wochen aus datenplan.md), geprueft am Vortag der Entscheidung. Ergebnis: Juli 5 bis 26 sieht Mai, Aug 2 bis 23 Juni, Aug 30 bis Sep 20 Juli, Sep 27 August. Revisions-Bias: TradingView liefert keine Vintages, die Historie ist die revidierte, nicht die damals bekannte. Darstellung: keine Niveaus, YoY ganze Prozent, Richtung der annualisierten 3-Monats-Rate gegen den Vormonat plus Laenge der Serie (gedeckelt bei 12). Marktzeile in jedem Fenster wiederholt (wie E-025). Zustand expansiv/neutral/restriktiv aus par. 7 weggelassen (Brief: nur YoY und Momentum). Im Pruefzeitraum gibt es nur vier verschiedene Zeilen: +5 % steigend seit 4 / 5 Monaten (8 Wochen), +5 % fallend seit 1 Monat (4 Wochen), +6 % fallend seit 2 Monaten (1 Woche). Hypothese (Liquiditaets-These aus Fynns Liste): Die KI senkt die Exposure, wenn sich das M2-Wachstum abschwaecht, und erhoeht sie bei Beschleunigung; der Timing-Wert steigt. Falsifikator (vor dem Lauf festgelegt): falsifiziert, wenn der Timing-Wert gegenueber E-003M nicht steigt (Differenz <= 0) oder wenn die KI der Zeile nicht folgt: mittlere Exposure-Differenz zu E-003M in den 5 Wochen mit fallender Rate minus dieselbe Differenz in den 8 Wochen mit steigender Rate ist nicht kleiner als -0,05. Champion-Regeln B-12/B-13/B-14: bei t >= 2 genau eine Wiederholung auf A, Urteil auf dem Mittel; B+C nur bei t >= 2. Karte nennt Anteil Gewichtsaenderungen unter 0,15, partiellen Anker (werkzeuge/anker.py), Rank-IC und Exposure. Keine Harness-Aenderung; versuche.py vom Branch claude/project-thread-lupsy0 (README par. 4). Vorlage aus Paragraph 4a unveraendert.

## Zusatz (Thread, nach dem Lauf)
- **Falsifikator: falsifiziert.** Teil 1 hielt: Timing-Wert gegenüber E-003M +0,14 %/Woche (t 1,72, 10/13 Wochen besser, ohne beste Woche +0,09 %). Teil 2 scheiterte: Die KI folgte der Zeile nicht. Mittlere Exposure-Differenz zu E-003M in den 5 Wochen mit fallender Rate −0,004, in den 8 Wochen mit steigender Rate −0,013; Unterschied +0,009 statt der geforderten < −0,05.
- **Nutzung:** In allen 13 Strategien erwähnt, immer als „mildly supportive“, „does not change any weight much“. Auch als die Rate fiel (ab 2026-08-30), blieb die Zeile ein schwacher Rückenwind. Exposure 0,454 (Basis 0,463).
- **Umschichtung** 0,110 je Coin und Woche (E-003-Läufe 0,118 / 0,120 / 0,154). **Anteil der Gewichtsänderungen unter 0,15:** 69 % (E-003-Läufe 63 / 61 / 52 %). Der kleine Vorsprung kommt eher aus ruhigerem Umschichten als aus M2-Timing.
- **Anker (werkzeuge/anker.py):** partiell 0,39 (E-003M 0,40), einfache Korrelation Gewicht zu Spannenlage 0,80, zu Momentum 0,66. Rank-IC 0,048 (E-003M 0,059).
- **Revisions-Bias:** TradingView liefert keine Vintages; gezeigt wurde die heute revidierte Historie, nicht die damals veröffentlichte. YoY auf ganze Prozent gerundet und Richtung der 3-Monats-Rate dämpfen das, schließen es nicht aus.
- **Wenig Variation:** Im Prüfzeitraum nur vier verschiedene Zeilen (+5 % steigend 4 bzw. 5 Monate, +5 % fallend 1 Monat, +6 % fallend 2 Monate). 13 Wochen und ein Monatswert, der sich alle 4 Wochen ändert, können eine Makro-These kaum testen.
- **Leak-Check (§3.4):** Export prüfte alle 130 Fenster und prompt.md (Jahreszahlen, Monatsnamen, Ticker): nichts gefunden. Die Zeile zeigt keine Niveaus und keine Daten.
- Keine Wiederholung, kein B+C (t 1,72 < 2). Champion bleibt E-003M.
