# E-013: Ensemble: Prompt E-003M unveraendert, 3 unabhaengige Laeufe pro Woche, entschieden wird mit dem mittleren Gewicht

- Achse: prompt
- Basis: E-003M
- Daten: candles, 180 Tage
- Modell: claude-opus-5-5
- Ensemble: 3 unabhängige Läufe pro Woche, entschieden wird mit ihrem mittleren Gewicht
- Werkzeug: 022ab32 versuche.py@e913634cff
- Thread: https://claude.ai/code/project/chan_01VH1Un8SQtbifKwzD9jDguD?thread=cmsg_01VH1Un8SQtbifKwzD9jDguD1FAEzfSp1ExEC126cZsyuR

## Änderung zum Prompt der Basis
```diff
```

## Prompt
```
# T-001 baseline trader prompt

You decide the position for an asset over the next week: a number from 0 (flat) to 1 (fully long).
Horizon is weeks to months; you do not need to trade often.

Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
Judge every window on its own. Do not compare windows with each other.

Before the weights, write out your analysis:
1. Strategy: in 2 to 3 sentences, the rule you will apply to every window.
2. Then for each window, under its id: your read of the market (trend, structure, key levels as prices on the 100 scale), your weight and why, and the price on the 100 scale that would make you change your mind.
3. End with one JSON object mapping each window id to its weight, e.g. {"a1b2c3d4e5": 0.0, "f6a7b8c9d0": 1.0}. Nothing after it.
```

## Bewertung gegen E-003M

| Coins | Wochen | Entscheidungen | Timing-Wert/Woche | Basis | Differenz | t | ohne beste Woche | Wochen besser | Exposure | Rank-IC |
|---|---|---|---|---|---|---|---|---|---|---|
| A (10) | 13 | 130 | -0.283 % | -0.244 % | -0.039 % | -0.51 | -0.067 % (ohne 2026-07-05) | 8/13 | 0.45 (Basis 0.463) | 0.072 |

**Urteil: kein messbarer Unterschied**

Verbrauch: 39 Claude-Aufrufe, 2354k Zeichen, Listenpreis 16.03 USD (zählt gegen Aarons Limit, keine Rechnung)

## Was die KI gedacht hat (Beispiel: Entscheidung 2026-07-05-e1)

Alle Wochen: [denken.md](denken.md)

````
## Strategy

All ten windows show the same pattern: a long decline from 150–250 down to the ~100 area, a sharp breakdown around day −33 to −30, and a 3–5 day rebound into day 0. My rule is to stay mostly flat while price is below its prior breakdown levels and its ~50-day average. I only add exposure when the post-crash structure shows higher lows and price has reclaimed the bounce high from around day −20. The weight scales with how clean that base looks. Below 0.5 is the ceiling until price is back above the old breakdown shelf.

## 38c89bb8f0 (XRP)
- **Read:** Primary downtrend. The low was 87.5 (day −10), followed by a 4-day bounce to 100 on light volume (~0.75).
  - Resistance is 102–107, with the day −20 spike high at 111.8.
  - The breakdown shelf at 113–118 is far above.
  - Support is 87.5–89.
- **Weight:** 0.2. The bounce is real, but there is no higher-high structure yet.
- **Change my mind:** A close above 107 would move me up. A close below 89 would take me to 0.

## 0f8bd33d5f (AVAX)
- **Read:** There was a capitulation low at 82.0 (day −16) on 3× volume, then a higher low at 86.0 (day −10).
  - Price is now 100, testing the day −20 high of 102.2.
  - Above that, the shelf is at 116–129.
- **Weight:** 0.3. The base looks constructive after the capitulation, but price is still under resistance.
- **Change my mind:** A close above 103 would move me up. A close below 92 would move me down.

## a1126f434c (DOGE)
- **Read:** A rally to 152 (day −52) fully failed, followed by a stair-step decline to a low of 89.3 (day −5).
  - Price is now 100.
  - Overhead is a pattern of lower highs at 107–114.
  - Volume on the bounce is weak (~0.55).
- **Weight:** 0.15. The trend is clearly down, and this looks like a bounce within that trend.
- **Change my mind:** A close above 110 would move me up. A close below 92 would take me to 0.

## fb2da8b219 (LINK)
- **Read:** The low was 86.9 (day −10), and the bounce to 100 came on fading volume (0.34 on day 0).
  - Resistance is 101.5–106.7.
  - The prior shelf is at 112–117.
- **Weight:** 0.2.
- **Change my mind:** A close above 107 would move me up. A close below 88 would take me to 0.

## d1d611c6ef (ADA)
- **Read:** This had the deepest crash, to 72.9 (day −10).
  - It then made a violent V-reversal to 105.5, with volume of 2.1–2.2× on days −2 and −1.
  - Price reclaimed the day −20 high of 100.3, but day 0 was an inside/down day.
  - The old shelf at 122–132 is far away.
- **Weight:** 0.35. The momentum and volume confirmation are strong, but price is extended after a +30% move in a week.
- **Change my mind:** A close above 106 would move me up. A close below 92 would mean the reversal failed.

## f71c443096 (BTC)
- **Read:** This is the shallowest version of the pattern.
  - The low was 90.8 (day −4), and price ground back up to 100.
  - Resistance is 103–105.7, with the shelf at 112–121.
- **Weight:** 0.2.
- **Change my mind:** A close above 106 would move me up. A close below 91 would take me to 0.

## 8f7b9bb226 (ETH)
- **Read:** The low was 84.7 (day −9). Price is now 100, just under the day −20 high of 103.6.
  - Volume on day 0 is about 1.0, with no follow-through.
  - The shelf is at 112–120.
- **Weight:** 0.2.
- **Change my mind:** A close above 104 would move me up. A close below 87 would take me to 0.

## a8d1740eff (SOL)
- **Read:** This has the best structure of the set.
  - The crash low was 73.7 (day −29), followed by higher lows at 78.5 (day −10) and 88 (day −5).
  - Price is now 100, well above the post-crash range high of 93.3.
  - It is back near the pre-crash shelf at 99–105, with the day −55 high at 120.6.
- **Weight:** 0.45. It has higher highs and higher lows and has reclaimed the breakdown level.
- **Change my mind:** A close above 106 would move me up. A close below 94 would move me down.

## ff329c0ebe (LTC)
- **Read:** The low was 85.7 (day −10), followed by a steady climb with a higher low at 89.8 (day −4).
  - Day 0 closed at 100, the high close since the crash, and roughly matches the day −20 high of 101.
  - The shelf is at 110–118.
- **Weight:** 0.25.
- **Change my mind:** A close above 102 would move me up. A close below 90 would take me to 0.

## 1b71661967 (DOT)
- **Read:** The decline has gone on for a long time, with lower highs at 163, 151, 118, and 113.
  - The low was 90.2 (day −7), and price is now 100.
  - Resistance is 107–118.
- **Weight:** 0.15. The trend is down, and the bounce has not yet changed the structure.
- **Change my mind:** A close above 114 would move me up. A close below 91 would take me to 0.

{"38c89bb8f0 (XRP)": 0.2, "0f8bd33d5f (AVAX)": 0.3, "a1126f434c (DOGE)": 0.15, "fb2da8b219 (LINK)": 0.2, "d1d611c6ef (ADA)": 0.35, "f71c443096 (BTC)": 0.2, "8f7b9bb226 (ETH)": 0.2, "a8d1740eff (SOL)": 0.45, "ff329c0ebe (LTC)": 0.25, "1b71661967 (DOT)": 0.15}
````

## Notizen
Backlog #25, Waechter B-16. Hypothese: Laeufe desselben Prompts streuen so stark wie die gemessenen Effekte (0,1 bis 0,17 %/Woche); das zufaellige Umschichten kostet Geld. Das Mittel aus 3 Laeufen daempft das Rauschen im Gewicht, senkt die Umschichtung und hebt den Timing-Wert gegen E-003M. Falsifiziert, wenn die Differenz zu E-003M auf A nicht t >= 2 erreicht. Prompt woertlich gleich E-003M (Paragraph-4a-Vorlage unveraendert), Daten unveraendert (180 Tage Tageskerzen). Kosten etwa dreifach.
