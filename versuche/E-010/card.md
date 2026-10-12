# E-010: Erst Regime benennen (up, down, sideways), dann Gewicht: ein Satz im Prompt, Analyse je Fenster beginnt mit der Zeile 'Regime: ...'

- Achse: prompt
- Basis: E-003
- Daten: candles, 180 Tage
- Modell: claude-opus-5-5
- Thread: https://claude.ai/code/project/chan_01VH1Un8SQtbifKwzD9jDguD?thread=cmsg_01VH1Un8SQtbifKwzD9jDguD4wx96dyJ8XrdtVv6TxhGkH

## Änderung zum Prompt der Basis
```diff
--- E-003
+++ E-010
@@ -5,6 +5,7 @@
 
 Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
 Judge every window on its own. Do not compare windows with each other.
+For each window, first name its regime as exactly one of up, down or sideways, and set the weight only after that, from the regime. Start each window's analysis with a line "Regime: up", "Regime: down" or "Regime: sideways".
 
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
For each window, first name its regime as exactly one of up, down or sideways, and set the weight only after that, from the regime. Start each window's analysis with a line "Regime: up", "Regime: down" or "Regime: sideways".

Before the weights, write out your analysis:
1. Strategy: in 2 to 3 sentences, the rule you will apply to every window.
2. Then for each window, under its id: your read of the market (trend, structure, key levels as prices on the 100 scale), your weight and why, and the price on the 100 scale that would make you change your mind.
3. End with one JSON object mapping each window id to its weight, e.g. {"a1b2c3d4e5": 0.0, "f6a7b8c9d0": 1.0}. Nothing after it.
```

## Bewertung gegen E-003

| Coins | Wochen | Entscheidungen | Timing-Wert/Woche | Basis | Differenz | t | ohne beste Woche | Wochen besser | Exposure | Rank-IC |
|---|---|---|---|---|---|---|---|---|---|---|
| A (10) | 13 | 130 | -0.347 % | -0.151 % | -0.197 % | -0.64 | -0.333 % (ohne 2026-07-05) | 5/13 | 0.508 (Basis 0.457) | 0.008 |

**Urteil: kein messbarer Unterschied**

Verbrauch: 13 Claude-Aufrufe, 787k Zeichen, Listenpreis 5.59 USD (zählt gegen Aarons Limit, keine Rechnung)

## Was die KI gedacht hat (Beispiel: Entscheidung 2026-07-05)

Alle Wochen: [denken.md](denken.md)

````
**Strategy:** I classify each window by where day 0's close sits relative to the multi-month range it traded in before the breakdown around day -33.
- **Down:** price is still below that range's floor and the window shows lower highs. Weight 0–0.15, with the higher end only when a base is forming.
- **Sideways:** price has climbed back inside the prior range. Weight about 0.4.
- **Up:** price is above the range with higher highs and higher lows. Weight 0.8–1.0.

## aae74fdb4d (XRP)
Regime: down
- **Read:** The window falls from 199 to 100. From day -150 to -34 it ranged 113–128, then broke down at day -33 and bottomed at 87.2 on day -9. The last 4 days bounced to 100 on below-average volume. Resistance is 102.3, then 111.8 (day -20 high), then the old floor near 113.
- **Weight:** 0.1. A bounce inside a downtrend isn't a reversal yet.
- **Change my mind:** a close above 112 means it has reclaimed the old range.

## 8629969c90 (LINK)
Regime: down
- **Read:** The window falls from 174 to 100. It ranged 105–134 before failing at day -33, with a low of 86.9 on day -10. Volume on the current bounce is thin (0.34–0.38). Resistance is 101.5, then 106.7.
- **Weight:** 0.1.
- **Change my mind:** a close above 107.

## 7afeaebb2f (ETH)
Regime: down
- **Read:** The window falls from 185 to 100. The prior range was 112–135, then the breakdown came at day -33. The low is 84.7 on day -9, and it has bounced to 100. Resistance is 101.3, then 103.6 (day -20 high).
- **Weight:** 0.1.
- **Change my mind:** a close above 104, which would also put in a higher high.

## 421bf4ff56 (DOGE)
Regime: down
- **Read:** The window falls from 193 to 100. A rally to 152 on day -52 failed, followed by a steep slide with a low of 89.3 on day -5. Resistance is 101.9, then 114–118.7.
- **Weight:** 0.1. The lower-high structure is clear.
- **Change my mind:** a close above 115.

## 6f3abbff9d (BTC)
Regime: down
- **Read:** The window falls from 147 to 100. The prior range of 115–130 broke at day -33. The low is 90.8, and price has bounced to 100. Resistance is 100.5, then 105.7 (day -20).
- **Weight:** 0.1.
- **Change my mind:** a close above 106.

## 4ce1e8d799 (AVAX)
Regime: down
- **Read:** The window falls from 211 to 100. The prior range was 125–150. On day -16 it capitulated to 82 on 3x volume. Since then it has made higher lows (86, then 92, then 97.5), which is a tentative base. Resistance is 102.8, then 102.2.
- **Weight:** 0.15. It is still below the prior range, but the base earns a small position.
- **Change my mind:** a close above 103 raises the weight; a close below 86 sends it to 0.

## 0d757fb83a (LTC)
Regime: down
- **Read:** The window falls from 183 to 100. The prior range was 110–130. The low is 85.7 on day -10. Day 0 closed at the top of its range, 100, with resistance just above at 101.2.
- **Weight:** 0.15.
- **Change my mind:** a close above 101.5 that holds; below 89 the trend has resumed.

## d3e1ac11a3 (DOT)
Regime: down
- **Read:** The window falls from 254 to 100. It has made a series of lower highs at 188, 186, 157 and 118.8. The low is 90.2 on day -7. Resistance is 102.2, then 118.8.
- **Weight:** 0.1.
- **Change my mind:** a close above 119.

## 013a92f014 (ADA)
Regime: down
- **Read:** The window falls from 221 to 100. It crashed to 72.9 on day -10. Over the last 4 days it rallied in a V from 76 to a high of 105.5 on about 2x volume, and that is a sharp short-covering-style move. The prior range of 120–140 is far overhead. Resistance is 105.5; support is 92, then 85.
- **Weight:** 0.15. The momentum is real but the regime is still down, and the move is overextended.
- **Change my mind:** a close above 106 that holds; below 92 the rally has failed.

## 178edd3ca2 (SOL)
Regime: sideways
- **Read:** The window falls from 173, but from day -150 onward it ranged roughly 95–120. It broke down to 73.7 on day -29 and then made higher lows (76.4, then 78.5, then 88). Price is now back at 100, inside the old range floor of 98–100. Resistance is 102.9, then 110–113.
- **Weight:** 0.4. The breakdown was reclaimed and price is back in the range.
- **Change my mind:** below 92 makes it down and sends the weight to about 0.1; a close above 110 makes it up.

{"aae74fdb4d (XRP)": 0.1, "8629969c90 (LINK)": 0.1, "7afeaebb2f (ETH)": 0.1, "421bf4ff56 (DOGE)": 0.1, "6f3abbff9d (BTC)": 0.1, "4ce1e8d799 (AVAX)": 0.15, "0d757fb83a (LTC)": 0.15, "d3e1ac11a3 (DOT)": 0.1, "013a92f014 (ADA)": 0.15, "178edd3ca2 (SOL)": 0.4}
````

## Notizen
Backlog #8. Hypothese: E-003 ordnet die Position in der 180-Tage-Spanne fast direkt einem Gewicht zu (Korrelation 0,79). Ein erzwungener Zwischenschritt (Regime-Label) koennte die Zuordnung strukturieren und das Hin- und Herschieben innerhalb eines Regimes senken. Erwartung: weniger Umschichtung als 0,12 und Timing-Wert hoeher als E-003. Falsifiziert, wenn die Differenz zu E-003 auf A nicht t >= 2 erreicht. Daten unveraendert (180 Tage Tageskerzen). Paragraph-4a-Vorlage woertlich unveraendert; das Regime-Label steht nur im Text (Zeile 'Regime: ...'), das JSON bleibt gleich, kein Harness-Eingriff.
