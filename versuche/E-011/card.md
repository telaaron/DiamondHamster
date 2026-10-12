# E-011: Szenarien zuerst: je Fenster Wahrscheinlichkeiten fuer hoch (>103), seitwaerts (97 bis 103), runter (<97) am Tag +7, Gewicht folgt daraus; Analyse je Fenster beginnt mit der Zeile 'Scenarios: up X, sideways Y, down Z'

- Achse: prompt
- Basis: E-003M
- Daten: candles, 180 Tage
- Modell: claude-opus-5-5
- Werkzeug: 199dee1 versuche.py@2ff6b1c89b
- Thread: https://claude.ai/code/project/chan_01VH1Un8SQtbifKwzD9jDguD?thread=cmsg_01VH1Un8SQtbifKwzD9jDguD2rR1bXM6Y5nySDnyYQvXTm

## Änderung zum Prompt der Basis
```diff
--- E-003M
+++ E-011
@@ -5,6 +5,7 @@
 
 Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
 Judge every window on its own. Do not compare windows with each other.
+For each window, first estimate the probabilities that the close on day +7 will be above 103 (up), between 97 and 103 (sideways) or below 97 (down); they must add up to 100. Set the weight only after that, from these probabilities. Start each window's analysis with a line "Scenarios: up X, sideways Y, down Z" with whole percentages.
 
 Before the weights, write out your analysis:
 1. Strategy: in 2 to 3 sentences, the rule you will apply to every window.
```

## Prompt
```
# T-001 baseline trader prompt

You decide the position for an asset over the next week: a number from 0 (flat) to 1 (fully long).
Horizon is weeks to months; you do not need to trade often.

Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
Judge every window on its own. Do not compare windows with each other.
For each window, first estimate the probabilities that the close on day +7 will be above 103 (up), between 97 and 103 (sideways) or below 97 (down); they must add up to 100. Set the weight only after that, from these probabilities. Start each window's analysis with a line "Scenarios: up X, sideways Y, down Z" with whole percentages.

Before the weights, write out your analysis:
1. Strategy: in 2 to 3 sentences, the rule you will apply to every window.
2. Then for each window, under its id: your read of the market (trend, structure, key levels as prices on the 100 scale), your weight and why, and the price on the 100 scale that would make you change your mind.
3. End with one JSON object mapping each window id to its weight, e.g. {"a1b2c3d4e5": 0.0, "f6a7b8c9d0": 1.0}. Nothing after it.
```

## Bewertung gegen E-003M

| Coins | Wochen | Entscheidungen | Timing-Wert/Woche | Basis | Differenz | t | ohne beste Woche | Wochen besser | Exposure | Rank-IC |
|---|---|---|---|---|---|---|---|---|---|---|
| A (10) | 13 | 130 | -0.192 % | -0.244 % | 0.052 % | 0.26 | -0.077 % (ohne 2026-08-16) | 9/13 | 0.499 (Basis 0.463) | 0.126 |

**Urteil: kein messbarer Unterschied**

Verbrauch: 13 Claude-Aufrufe, 789k Zeichen, Listenpreis 5.57 USD (zählt gegen Aarons Limit, keine Rechnung)

## Was die KI gedacht hat (Beispiel: Entscheidung 2026-07-05)

Alle Wochen: [denken.md](denken.md)

````
**Strategy:** Every window has the same backdrop: a long downtrend, a crash at about day -150, a 105–130 range, a second break at about day -33, and a sharp rally into 100. I estimate the day +7 odds from four things: the primary trend, whether the latest swing low was higher or lower, how close price is to resistance, and how stretched the last few days' rally is. Weight = 0.4 + 2 × (P(up) − P(down)), clipped to 0–1 and rounded to 0.05. The base of 0.4 reflects the bearish long-term backdrop.

## baa0c5a433 (ETH)
Scenarios: up 33, sideways 35, down 32

- **Trend:** Primary trend is down, from 185 to 100. The post-crash range of 110–135 broke at day -33.
- **Structure:** Double bottom at 84.3 (day -29) and 84.7 (day -9). Price then rallied five days in a row from 88 to 100 on modest volume.
- **Key levels:** Resistance at 101–103.6 (day -20 high). Support at 94–95, then 85.
- **Weight:** 0.4. The double bottom is constructive, but price is right at resistance inside a downtrend, so the odds are roughly balanced.
- **Change my mind:** a close above 104 (go higher) or below 94 (go flat).

## 572ba8d4d6 (SOL)
Scenarios: up 38, sideways 35, down 27

- **Trend:** Primary trend is down, but this is the strongest recovery of the set.
- **Structure:** Higher low at 78.5 (day -10) versus 73.7 (day -29). Price has already broken above the post-crash high of 93.3 and reached 102.9.
- **Key levels:** Support at 94–97. Old range floor and resistance at about 103–106.
- **Weight:** 0.6. Higher lows plus a breakout above the post-crash range tilt the odds up.
- **Change my mind:** a close below 94.

## 182785967b (BTC)
Scenarios: up 32, sideways 38, down 30

- **Trend:** A shallower decline than most windows. The 105–128 range broke at day -33.
- **Structure:** Lows at 92.9 (day -30) and 91.3 (day -10), essentially a double bottom. Price rallied into 100 on low volume.
- **Key levels:** Resistance at 103.4–105.7. Support at 94 and 91.
- **Weight:** 0.45. Balanced, with only a slight base forming.
- **Change my mind:** a close above 106 (go higher) or below 94 (go flat).

## f7ab670d14 (XRP)
Scenarios: up 30, sideways 37, down 33

- **Trend:** Down. The low of 87.2 at day -10 undercut the 90.7 low at day -29, a lower low.
- **Structure:** Rally to 100 that stalled at 102.3 on day -1. The day -20 spike to 111.8 failed.
- **Key levels:** Resistance at 102–107. Support at 94, then 87.
- **Weight:** 0.35. The lower low and failed spike lean slightly bearish.
- **Change my mind:** a close above 107.

## 5827c6fa78 (ADA)
Scenarios: up 35, sideways 25, down 40

- **Trend:** Steep downtrend, with a capitulation from 124 to 73 that included a lower low at 72.9 (day -10).
- **Structure:** Explosive rally of about 30% in four days on heavy volume (2.1–2.2× average) to 105.5. Day 0 is an inside, slightly bearish candle.
- **Key levels:** Resistance at 103–105.5. Support at 94–95, then 85.
- **Weight:** 0.3. A move this extended is prone to retrace and makes outcomes very wide, so I keep exposure small.
- **Change my mind:** a close above 106 would confirm a reversal.

## 96aec10a4c (AVAX)
Scenarios: up 34, sideways 38, down 28

- **Trend:** Down. Capitulation to 82 at day -16 on 3× volume.
- **Structure:** Higher lows since the capitulation at 86 and 90.6, then a steady climb to 100.
- **Key levels:** Resistance at 102–103. Support at 94–96.
- **Weight:** 0.5. The higher-low sequence after the volume climax leans mildly up.
- **Change my mind:** a close below 94.

## afb6d57568 (LTC)
Scenarios: up 33, sideways 38, down 29

- **Trend:** Down. The low of 85.7 at day -10 undercut the 88.4 low at day -29.
- **Structure:** Orderly recovery that closed day 0 at the high of the day (100.0, high 100.7).
- **Key levels:** Resistance at 101. A break there opens 105–110. Support at 95–96.
- **Weight:** 0.5. The strong close near resistance leans slightly up.
- **Change my mind:** a close below 95.

## f05bd1120a (DOT)
Scenarios: up 30, sideways 37, down 33

- **Trend:** Strongest downtrend of the set, with lower highs at 118.8 (day -20) and 111 (day -15), and a lower low at 90.2.
- **Structure:** Rally to 100 on falling volume.
- **Key levels:** Resistance at 102–111. Support at 93, then 90.
- **Weight:** 0.35. The downtrend structure is intact.
- **Change my mind:** a close above 111.

## 6a6d8479f5 (LINK)
Scenarios: up 33, sideways 37, down 30

- **Trend:** Down. Double bottom at 86.8 (day -29) and 86.9 (day -10).
- **Structure:** Rally to 100 on very light volume (0.34–0.38× average).
- **Key levels:** Resistance at 101.5–106.7. Support at 94, then 87.
- **Weight:** 0.45. The base is constructive, but the lack of volume undercuts the rally.
- **Change my mind:** a close above 107 (go higher) or below 94 (go flat).

## ddce9ddff2 (DOGE)
Scenarios: up 29, sideways 37, down 34

- **Trend:** Down. Lower highs at 118.7, 116.8 and 109.3, and a lower low at 91.8 (day -10) versus 99.7 (day -29).
- **Structure:** Bounce to 100 on light volume.
- **Key levels:** Resistance at 102–109. Support at 92.
- **Weight:** 0.3. The pattern of lower highs and lower lows argues for little exposure.
- **Change my mind:** a close above 109.

{"baa0c5a433 (ETH)": 0.4, "572ba8d4d6 (SOL)": 0.6, "182785967b (BTC)": 0.45, "f7ab670d14 (XRP)": 0.35, "5827c6fa78 (ADA)": 0.3, "96aec10a4c (AVAX)": 0.5, "afb6d57568 (LTC)": 0.5, "f05bd1120a (DOT)": 0.35, "6a6d8479f5 (LINK)": 0.45, "ddce9ddff2 (DOGE)": 0.3}
````

## Notizen
Backlog #20. Hypothese: Eine erzwungene Prognose (Wahrscheinlichkeiten fuer die Folgewoche) statt einer Lage-Beschreibung loest das Gewicht vom Spannen-Anker und macht die Einschaetzung pruefbar. Falsifiziert, wenn die Differenz zu E-003M auf A nicht t >= 2 erreicht. Daten unveraendert (180 Tage Tageskerzen). Paragraph-4a-Vorlage woertlich unveraendert; die Wahrscheinlichkeiten stehen nur im Text (Zeile 'Scenarios: ...'), das JSON bleibt gleich, kein Harness-Eingriff. Kalibrierung (Brier-Score, Tabelle) wird nachtraeglich aus dem Text gelesen und ist nur informativ.
