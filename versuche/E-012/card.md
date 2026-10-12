# E-012: Rolle Risikomanager: Ziel kleinster Drawdown bei etwa gleicher Rendite wie eine feste Position, nicht maximale Rendite (zwei Saetze am Anfang des Prompts)

- Achse: prompt
- Basis: E-003M
- Daten: candles, 180 Tage
- Modell: claude-opus-5-5
- Werkzeug: 199dee1 versuche.py@2ff6b1c89b
- Thread: https://claude.ai/code/project/chan_01VH1Un8SQtbifKwzD9jDguD?thread=cmsg_01VH1Un8SQtbifKwzD9jDguDEczCxpNCwsA96V6YQRWWgY

## Änderung zum Prompt der Basis
```diff
--- E-003M
+++ E-012
@@ -1,6 +1,7 @@
 # T-001 baseline trader prompt
 
-You decide the position for an asset over the next week: a number from 0 (flat) to 1 (fully long).
+You are a risk manager. You decide the position for an asset over the next week: a number from 0 (flat) to 1 (fully long).
+Your goal is not the highest return. Your goal is the smallest drawdown for about the same return as holding a steady position: keep the exposure while the risk of a deep loss is low, and cut it when that risk is high.
 Horizon is weeks to months; you do not need to trade often.
 
 Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
```

## Prompt
```
# T-001 baseline trader prompt

You are a risk manager. You decide the position for an asset over the next week: a number from 0 (flat) to 1 (fully long).
Your goal is not the highest return. Your goal is the smallest drawdown for about the same return as holding a steady position: keep the exposure while the risk of a deep loss is low, and cut it when that risk is high.
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
| A (10) | 13 | 130 | -0.117 % | -0.244 % | 0.127 % | 0.85 | 0.014 % (ohne 2026-08-16) | 9/13 | 0.427 (Basis 0.463) | 0.009 |

**Urteil: kein messbarer Unterschied**

Verbrauch: 13 Claude-Aufrufe, 788k Zeichen, Listenpreis 5.42 USD (zählt gegen Aarons Limit, keine Rechnung)

## Was die KI gedacht hat (Beispiel: Entscheidung 2026-07-05)

Alle Wochen: [denken.md](denken.md)

````
**Strategy:** All ten windows share the same shape. Each has a six-month downtrend, roughly halving from the start, then a crash around day -150, a range, a second breakdown around day -33, and a rebound into the decision day. My default is therefore a low weight, because the long-term trend and the overhead supply put deep-loss risk above average. I add exposure only where the recent bounce has a higher low and a higher high (an early reversal). I cut further where the bounce came off a lower low, which means the downtrend is still intact.

### 7a33a16ed9 (XRP)
- **Read:** Price fell from 199 to 100. It ranged between 114 and 128, broke down to 90.7 at day -29, and bounced to 111.8. It then made a lower low at 87.5 on day -10 and has rallied back to 100.
- **Structure:** Lower lows and lower highs, with overhead resistance at 102–108 and support at 87.5.
- **Weight: 0.25.** The trend is down and the bounce is not yet confirmed.
- **Change my mind:** A close above 108 means add. A close below 87 means go flat.

### 2ac640639a (ADA)
- **Read:** Price fell from 221 to 100. It crashed from a 125–150 range to 78 at day -29, then made a lower low at 72.9 on day -10. The last four days show a violent rally of about +32% on heavy volume, up to a 105.5 high.
- **Structure:** The reversal thrust is real, but it runs straight into heavy overhead supply from 105 to 125. Pullback risk after a move this extended is high.
- **Weight: 0.3.**
- **Change my mind:** A close above 106 means add. A close below 92 means cut. A close below 84 means flat.

### 8c76be2375 (LTC)
- **Read:** Price fell from 183 to 100. It broke down from a 112–132 range to 88.4 at day -29 and rebounded to 101. The retest low at 85.7 on day -10 was only marginally lower, and price now sits at its 20-day high.
- **Structure:** Roughly a double bottom near 86–88, testing 101 resistance.
- **Weight: 0.3.**
- **Change my mind:** A close above 102 means raise. A close below 89 means cut. A close below 85.5 means flat.

### 1f82221eca (ETH)
- **Read:** Price fell from 184 to 100. It broke down from a 112–135 range to a low of 84.3 at day -29 and bounced to 103.6. It retested the low at 84.7 on day -9, then rallied to 100.
- **Structure:** A clean double bottom at about 84.5, with the neckline at 103.6.
- **Weight: 0.3.** The pattern is not yet confirmed.
- **Change my mind:** A close above 104 means raise. A close below 88 means cut. A close below 84 means flat.

### afb46a7eb7 (LINK)
- **Read:** Price fell from 174 to 100. It broke down from a 108–134 range to 86.8 and bounced to 106.7. It retested the low at 86.9 on day -10 and is now at 100.
- **Structure:** A double bottom near 87, with the neckline at 106.7. Volume on the bounce is light.
- **Weight: 0.3.**
- **Change my mind:** A close above 107 means raise. A close below 87 means flat.

### 2aa0992b2f (DOT)
- **Read:** This is the steepest decline in the set, from 253 to 100. Price made lower highs through the 135–160 area, crashed to 100.3, bounced to 118.8, and then made a lower low at 90.2 on day -7.
- **Structure:** The downtrend is fully intact. Resistance sits at 102 and 119, support at 90.
- **Weight: 0.2.**
- **Change my mind:** A close above 103, and then above 119, means add. A close below 90 means flat.

### c71f05b662 (BTC)
- **Read:** This is a milder decline, from 147 to 100. Price broke down from a 115–128 range to 92.9, bounced to 105.7, and then made a slightly lower low at 90.8 on day -4. It is now at 100 on low volume.
- **Structure:** Lower lows, though volatility is the lowest in the set.
- **Weight: 0.25.**
- **Change my mind:** A close above 106 means raise. A close below 90.5 means flat.

### 59ea2777a3 (AVAX)
- **Read:** Price fell from 211 to 100. It broke down from a 125–150 range to 89.9. A capitulation flush on day -16 reached 82 on 3x volume, followed by higher lows near 86 and a high of 102.8 on day -1, which is above the day -20 bounce high of 102.2.
- **Structure:** An early higher-low/higher-high sequence after a volume climax.
- **Weight: 0.35.**
- **Change my mind:** A close above 103 means raise toward 0.5. A close below 91 means cut. A close below 86 means flat.

### 12b26170cd (SOL)
- **Read:** Price fell from 173 to 100. It broke down from a 100–120 range to 73.7 at day -29 and bounced to 93.3. It then made a higher low at 78.5 on day -10 and has rallied to 100, clearing the 93.3 bounce high.
- **Structure:** This is the only window with a clear higher low and higher high. Price is now retesting the old breakdown level at about 100.
- **Weight: 0.45.**
- **Change my mind:** A close above 103 means raise. A close below 93 means cut. A close below 85 means flat.

### 10d6cc64a8 (DOGE)
- **Read:** Price fell from 193 to 100. It rallied to 152 at day -52, then failed. It broke down to 99.7, bounced to 118.7, and then made a lower low at 89.3 on day -5.
- **Structure:** A failed rally followed by lower lows, with resistance at 102 and 113–119.
- **Weight: 0.2.**
- **Change my mind:** A close above 103 means add. A close below 89 means flat.

{"7a33a16ed9 (XRP)": 0.25, "2ac640639a (ADA)": 0.3, "8c76be2375 (LTC)": 0.3, "1f82221eca (ETH)": 0.3, "afb46a7eb7 (LINK)": 0.3, "2aa0992b2f (DOT)": 0.2, "c71f05b662 (BTC)": 0.25, "59ea2777a3 (AVAX)": 0.35, "12b26170cd (SOL)": 0.45, "10d6cc64a8 (DOGE)": 0.2}
````

## Notizen
Backlog #21, Fynns und Aarons Produktidee (aehnliche Rendite, kleinere Drawdowns) als Auftrag. Hypothese: Ein Risiko-Auftrag statt Rendite-Auftrag laesst die KI nach Risiko statt nach Spannen-Position gewichten und das teure Hinterherlaufen bremsen. Falsifiziert, wenn die Differenz zu E-003M auf A nicht t >= 2 erreicht. Urteil nur ueber den Standard-Timing-Wert; Max-Drawdown und Rendite gegen E-003M nur informativ auf der Karte. Daten unveraendert (180 Tage Tageskerzen), Paragraph-4a-Vorlage woertlich unveraendert.

## Drawdown und Rendite (nur zur Information, nicht Teil des Urteils)

Gleichgewichtetes Portfolio der 10 Coins aus Set A, 13 Wochen, wöchentlich neu gewichtet, Umschichtung 0,2 % je Seite. Max Drawdown auf Wochenschlüssen. E-003M = Mittel der drei E-003-Läufe.

| | Rendite 13 Wochen | Max Drawdown Portfolio | Max Drawdown je Coin (Mittel) | Exposure |
|---|---|---|---|---|
| E-012 | +18,8 % | −3,7 % | −5,1 % | 0,43 |
| E-003M | +18,7 % | −4,2 % | −5,9 % | 0,46 |
| feste Position in Höhe des E-012-Mittelgewichts | +20,5 % | −2,6 % | −4,2 % | 0,43 |
| Kaufen und Halten (Gewicht 1) | +48,1 % | −6,3 % | | 1,00 |

Gleiche Rendite, etwas kleinerer Drawdown als E-003M, aber bei geringerer Exposure. Eine konstante Position mit derselben mittleren Exposure ist auf beiden Achsen besser. Korrelation Gewicht zur 180-Tage-Spanne 0,63 (E-003-Läufe 0,77 bis 0,79), Umschichtung 0,14 je Woche (E-003-Läufe 0,12 bis 0,15).
