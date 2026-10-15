# E-036: E-003M plus eine Zeile je Fenster mit der realisierten Volatilitaet ueber 7, 30 und 90 Tage (annualisiert, ganze Prozent), berechnet aus den eigenen Kerzen des Fensters bis zum Entscheidungstag; prompt.md erklaert die Zeile in zwei Saetzen ohne Handelsregel

- Achse: daten
- Basis: E-003M
- Daten: custom, 180 Tage
- Modell: claude-opus-5-5
- Werkzeug: f2794e9 versuche.py@764f343a01
- Thread: https://claude.ai/code/project/chan_01VH1Un8SQtbifKwzD9jDguD?thread=cmsg_01VH1Un8SQtbifKwzD9jDguDKqwJruejf8azSbxGK5KpQd

## Änderung zum Prompt der Basis
```diff
--- E-003M
+++ E-036
@@ -4,6 +4,7 @@
 Horizon is weeks to months; you do not need to trade often.
 
 Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
+Each window starts with one line `volatility (annualized) 7d A%, 30d B%, 90d C%` (or `volatility not available`): the standard deviation of daily close-to-close log returns over the last 7, 30 and 90 days up to the decision day, annualized and in percent. It measures how strongly the price has been swinging, not in which direction.
 Judge every window on its own. Do not compare windows with each other.
 
 Before the weights, write out your analysis:
```

## Prompt
```
# T-001 baseline trader prompt

You decide the position for an asset over the next week: a number from 0 (flat) to 1 (fully long).
Horizon is weeks to months; you do not need to trade often.

Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
Each window starts with one line `volatility (annualized) 7d A%, 30d B%, 90d C%` (or `volatility not available`): the standard deviation of daily close-to-close log returns over the last 7, 30 and 90 days up to the decision day, annualized and in percent. It measures how strongly the price has been swinging, not in which direction.
Judge every window on its own. Do not compare windows with each other.

Before the weights, write out your analysis:
1. Strategy: in 2 to 3 sentences, the rule you will apply to every window.
2. Then for each window, under its id: your read of the market (trend, structure, key levels as prices on the 100 scale), your weight and why, and the price on the 100 scale that would make you change your mind.
3. End with one JSON object mapping each window id to its weight, e.g. {"a1b2c3d4e5": 0.0, "f6a7b8c9d0": 1.0}. Nothing after it.
```

## Datenaufbereitung (render.py)
```python
"""E-036: the champion's 180-day daily table plus one volatility line per window (backlog #13).

Computed only from the window's own candles up to and including the decision day (no external data):
- daily log returns of the close, ln(c_t / c_{t-1});
- vol_N = standard deviation (ddof 1) of the last N returns, annualized with sqrt(365) (crypto trades 7 days),
  in percent, rounded to whole percent; N = 7, 30, 90.
- Missing history (fewer than N + 1 closes): "volatility not available".
Scale-free, so it reveals no price level, date or coin.
"""

import numpy as np
import pandas as pd

from diamondhamster import ai

PERIODS = (7, 30, 90)


def line(df: pd.DataFrame) -> str:
    c = df["close"].astype(float)
    if len(c) < max(PERIODS) + 1:
        return "volatility not available"
    r = np.log(c / c.shift(1)).dropna()
    parts = [f"{n}d {round(100 * r.tail(n).std(ddof=1) * np.sqrt(365))}%" for n in PERIODS]
    return "volatility (annualized) " + ", ".join(parts)


def render(df: pd.DataFrame, lookback: int) -> str:
    return line(df) + "\n" + ai.compact(ai.window(df, df.index[-1], lookback))
```

## Bewertung gegen E-003M

| Coins | Wochen | Entscheidungen | Timing-Wert/Woche | Basis | Differenz | t | ohne beste Woche | Wochen besser | Exposure | Rank-IC |
|---|---|---|---|---|---|---|---|---|---|---|
| A (10) | 13 | 130 | -0.334 % | -0.244 % | -0.089 % | -1.41 | -0.11 % (ohne 2026-07-12) | 6/13 | 0.447 (Basis 0.463) | 0.037 |

**Urteil: kein messbarer Unterschied**

Verbrauch: 13 Claude-Aufrufe, 795k Zeichen, Listenpreis 5.36 USD (zählt gegen Aarons Limit, keine Rechnung)

## Was die KI gedacht hat (Beispiel: Entscheidung 2026-07-05)

Alle Wochen: [denken.md](denken.md)

````
## Strategy

I follow the trend and wait for the structure to confirm it. A window gets a meaningful long only when the recent swing low held higher than the prior one and price has reclaimed the last swing high. When price is bouncing inside a series of lower highs I hold a small or moderate weight, scaled by how far the bounce has repaired the structure. Very high volatility cuts the weight further.

## 205b321007 (DOGE)
- **Read:** Long-term downtrend from 193. The rally to 148 (day -52) failed, and price fell through 104 to a lower low at 89 (day -5). It has bounced back to 100 on fading volume. The last swing high is 116.8 (day -20) and the 50-day mean is about 115. Lower highs and lower lows remain intact.
- **Weight:** 0.2. This is a bounce inside a downtrend, so only a small position.
- **Change my mind:** a close above 117 would make me add; a break below 89 would take me flat.

## 0a99e5fbcc (SOL)
- **Read:** Price crashed to 73.7 (day -29), and the next low was higher at 78.5 (day -10). The rally since then took out the 93 swing high (day -20) and reached 102. Volume expanded on the up days. This is the cleanest higher-high, higher-low reversal in the set. Resistance sits around 105–108, then 119.
- **Weight:** 0.6. The trend change is confirmed, but price is approaching overhead supply.
- **Change my mind:** a close below 88 (the breakout level) would take me flat; a close above 108 would take me to full.

## 37e76afb30 (ADA)
- **Read:** Price collapsed to 78 (day -29), then made a lower low at 72.9 (day -10). It then ran +32% in four days on heavy volume to 105.5 and closed at 100. That move clears the 100.3 high from day -20. Volatility is extreme (7-day at 85%), and the 50-day mean is about 100. The momentum is strong, but the move is parabolic and could be a squeeze.
- **Weight:** 0.4. The breakout counts, but the volatility and the risk of a give-back cap the size.
- **Change my mind:** a close below 92 would take me flat; holding above 105 for a few days would justify 0.7.

## 9cb567659f (BTC)
- **Read:** Lower volatility than the other windows. Price made a low at 92.9 (day -30) and a marginal lower low at 90.8 (day -4), and is now 100. The swing high is 105.7 (day -20) and the 50-day mean is about 107. The structure is basing but not yet repaired.
- **Weight:** 0.3.
- **Change my mind:** above 106 would take me to 0.6 or more; below 90.8 would take me flat.

## 8243385684 (ETH)
- **Read:** A double bottom at 84.3 / 84.7 (days -29 and -9). Price has rallied to 100 and is just under the neckline at 103.6 (day -20). The larger trend is down from 185, with the 50-day mean around 105.
- **Weight:** 0.4. The double bottom gives some support, but the neckline is not yet broken.
- **Change my mind:** above 104 would take me to 0.7; below 86 would take me flat.

## 32a431fa35 (AVAX)
- **Read:** Price crashed to 89.9 (day -29) and then capitulated to 82 (day -16) on 3x volume. The recovery has been steady with higher lows (86, then 92, then 97.5), and price now sits at 100–101. It is just below the 102.2 swing high. The 7-day volatility has compressed to 37%.
- **Weight:** 0.4. Higher lows are forming after the capitulation.
- **Change my mind:** above 103 would take me to 0.7; below 92 would take me flat.

## a84a31ab90 (LTC)
- **Read:** Price fell to 88.4 (day -29) and made a lower low at 85.7 (day -10). It has climbed steadily to 100, testing the 101 high from day -20. The broader trend is down from 183, and the 50-day mean is about 107.
- **Weight:** 0.35.
- **Change my mind:** above 101.5 would take me to 0.6; below 89 would take me flat.

## 979049badb (LINK)
- **Read:** A double bottom at 86.8 / 86.9 (days -29 and -10). Price is back at 100 on light volume, below the swing high of 106.7 (day -20). The prior rally peaked at 134.8, with lower highs since.
- **Weight:** 0.35. The double bottom gives some support, but the volume is weak and the neckline is still far away.
- **Change my mind:** above 107 would take me to 0.7; below 87 would take me flat.

## 6a7d8dcceb (XRP)
- **Read:** Price made a low at 90.7 (day -29) and a lower low at 87.2 (day -10), and is now 100. The swing high is 111.8 (day -20) and the 50-day mean is about 110. Lower highs persist.
- **Weight:** 0.3.
- **Change my mind:** above 108 would take me to 0.6; below 88 would take me flat.

## 800db34099 (DOT)
- **Read:** The steepest decline in the set, from 253 to 100. Price made a low at 100.3 (day -29), then a clear lower low at 90.2 (day -7). It has bounced to 100, with the swing high at 118.8 (day -20). The downtrend is fully intact.
- **Weight:** 0.15.
- **Change my mind:** above 115 would take me to 0.5; below 90 would take me flat.

{"205b321007 (DOGE)": 0.2, "0a99e5fbcc (SOL)": 0.6, "37e76afb30 (ADA)": 0.4, "9cb567659f (BTC)": 0.3, "8243385684 (ETH)": 0.4, "32a431fa35 (AVAX)": 0.4, "a84a31ab90 (LTC)": 0.35, "979049badb (LINK)": 0.35, "6a7d8dcceb (XRP)": 0.3, "800db34099 (DOT)": 0.15}
````

## Notizen
Backlog #13. Hypothese: mit der Volatilitaetszeile gewichtet die KI nach Risiko statt nach Richtung. Daten: kein externer Abruf (B-19 entfaellt); Volatilitaet = Standardabweichung (ddof 1) der taeglichen Log-Renditen der Schlusskurse der letzten 7/30/90 Tage bis einschliesslich Entscheidungstag, mal sqrt(365), in Prozent, ganzzahlig gerundet; skalenfrei, kein Niveau, kein Datum. 'volatility not available' bei weniger als 91 Schlusskursen. Einzige Aenderung gegen E-003M: Zeile vor der Kerzentabelle plus zwei neutrale Saetze in prompt.md; Vorlage aus Paragraph 4a unveraendert. Falsifikator (vor dem Lauf festgelegt): falsifiziert, ausser (a) der Timing-Wert liegt ueber E-003M UND (b) die Gewichte korrelieren negativer mit der 30-Tage-Volatilitaet als bei E-003M. Mass fuer (b): Mittel ueber die 13 Wochen der Spearman-Korrelation Gewicht ~ 30d-Vola quer ueber die 10 Coins der Woche; fuer E-003M das Mittel ueber die drei E-003-Laeufe. Zusaetzlich berichtet: gepoolte Pearson-Korrelation ueber alle 130 Entscheidungen, partieller Anker (werkzeuge/anker.py, E-003M 0,40), Anteil Gewichtsaenderungen unter 0,15, Umschichtung (E-003M 0,121), Exposure, Rank-IC, Vergleich mit konstant 0,5. Champion-Regeln B-12/B-13/B-14: bei t >= 2 genau eine Wiederholung auf A, Urteil auf dem Mittel; B+C nur dann. Keine Harness-Option; versuche.py vom Branch claude/project-thread-lupsy0.

## Auswertung Falsifikator (Thread, nach dem Lauf)

| | E-036 | E-003M (Mittel 3 Läufe) | E-003 / -w2 / -w3 |
|---|---|---|---|
| Spearman Gewicht ~ 30d-Vola, quer je Woche, Mittel 13 Wochen | −0,240 | −0,213 | −0,168 / −0,237 / −0,235 |
| Pearson gepoolt, 130 Entscheidungen | +0,267 | +0,199 | +0,262 / +0,150 / +0,184 |
| Partieller Anker (anker.py) | 0,39 | 0,40 | |
| Änderungen unter 0,15 | 66 % | | 63 / 61 / 52 % |
| Umschichtung | 0,120 | 0,121 | 0,118 / 0,120 / 0,154 |
| Gegen konstant 0,5 (%/Woche, t) | −0,48 (−1,06) | | −0,25 / −0,36 / −0,37 |

(a) Timing-Wert über E-003M: nein (−0,09 %/Woche, t −1,41). (b) negativer als E-003M: knapp (−0,24 vs −0,21), aber innerhalb der Spanne der drei E-003-Läufe. **Falsifiziert.** Die KI gewichtet ruhige Coins schon ohne Zeile etwas höher; die Zahl ändert daran nichts Messbares.
