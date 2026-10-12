# E-009: Gegen den Strich: ein Satz im Prompt, 'High prices after a strong rise are not a reason to buy in themselves.'

- Achse: prompt
- Basis: E-003
- Daten: candles, 180 Tage
- Modell: claude-opus-5-5
- Thread: https://claude.ai/code/project/chan_01VH1Un8SQtbifKwzD9jDguD?thread=cmsg_01VH1Un8SQtbifKwzD9jDguDGkgg84HpjwuhViLJyZE7PN

## Änderung zum Prompt der Basis
```diff
--- E-003
+++ E-009
@@ -5,6 +5,7 @@
 
 Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
 Judge every window on its own. Do not compare windows with each other.
+High prices after a strong rise are not a reason to buy in themselves.
 
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
High prices after a strong rise are not a reason to buy in themselves.

Before the weights, write out your analysis:
1. Strategy: in 2 to 3 sentences, the rule you will apply to every window.
2. Then for each window, under its id: your read of the market (trend, structure, key levels as prices on the 100 scale), your weight and why, and the price on the 100 scale that would make you change your mind.
3. End with one JSON object mapping each window id to its weight, e.g. {"a1b2c3d4e5": 0.0, "f6a7b8c9d0": 1.0}. Nothing after it.
```

## Bewertung gegen E-003

| Coins | Wochen | Entscheidungen | Timing-Wert/Woche | Basis | Differenz | t | ohne beste Woche | Wochen besser | Exposure | Rank-IC |
|---|---|---|---|---|---|---|---|---|---|---|
| A (10) | 13 | 130 | -0.234 % | -0.151 % | -0.083 % | -0.72 | -0.11 % (ohne 2026-07-19) | 8/13 | 0.433 (Basis 0.457) | 0.114 |

**Urteil: kein messbarer Unterschied**

Verbrauch: 13 Claude-Aufrufe, 785k Zeichen, Listenpreis 5.39 USD (zählt gegen Aarons Limit, keine Rechnung)

## Was die KI gedacht hat (Beispiel: Entscheidung 2026-07-05)

Alle Wochen: [denken.md](denken.md)

````
**Strategy:** Every window is in a primary downtrend: price has fallen from 150–250 to 100 and is below its multi-month base. So I start defensive. I add weight only where the recent structure shows real repair, meaning higher lows and a reclaim of the last swing high. Lower lows mean small weight, and I cap the weight at about 0.6 while the primary trend is still down.

## eb0b7e58a1 (ADA)
- **Read:** Primary downtrend from 221. The month-long base around 130 broke in a capitulation to 82.7 at day -30 (volume 3.9×). The bounce failed at 100.3, and price made a lower low at 72.9 (day -10). The last four days were a violent rally, +32% on 2× volume, to a 105.5 high. Price is now testing the 100 resistance after a nearly vertical move, so a pullback is likely before any follow-through.
- **Weight: 0.3.** The thrust is strong, but the structure is still lower lows, and the move looks stretched in the short term.
- **Change my mind:** I'd add above 106. I'd exit below 92.

## bb95329899 (LTC)
- **Read:** Price fell from the 132 peak (day -56) to 88.4, bounced to 101.2 (day -20), then made a lower low at 85.7 (day -10). It has now recovered steadily on fading volume and is back at the 100–101 swing high. Above that sits the old base at 113–120.
- **Weight: 0.3.** Price is at resistance, and the higher-low structure is not yet confirmed.
- **Change my mind:** I'd add on a close above 101.5. I'd exit below 94.

## 04c8ebd65f (SOL)
- **Read:** The low was 73.7 (day -29), followed by a higher low at 78.5 (day -10). The rally then cleared the 93.3 swing high and reached 102.9. That gives higher highs and higher lows over the past month. Price is pausing at 100 on low volume, just under the old base at 100–107. The 120 high from day -55 is the larger ceiling.
- **Weight: 0.6.** This is the cleanest repair in the set.
- **Change my mind:** I'd exit below 88, which would mean losing the breakout area.

## 694ec4b067 (LINK)
- **Read:** Double bottom at 86.8 and 86.9 (days -29 and -10). The neckline is 106.7. Price is at 100, mid-range, with volume drying up (0.34–0.38). Above that sits the old base at 112–120.
- **Weight: 0.4.** The base is constructive but unconfirmed.
- **Change my mind:** I'd add above 107. I'd exit below 87.

## b983b138f7 (XRP)
- **Read:** Price made a low of 90.7, failed at 111.8 (day -20), then made a slightly lower low at 87.2 (day -10). It is now at 100, mid-range. The old base was 113–125.
- **Weight: 0.3.** The structure is still marginally lower lows.
- **Change my mind:** I'd add above 112. I'd exit below 87.

## 0e390dc123 (ETH)
- **Read:** Double bottom at 84.3 and 84.7, with the neckline at 103.6. Price is at 100, and the last bar came with an uptick in volume. Above that sits the old base at 112–130.
- **Weight: 0.4.**
- **Change my mind:** I'd add above 104. I'd exit below 84.

## 57ce4bda32 (BTC)
- **Read:** This is the lowest-volatility window. The low was 92.9, followed by a slightly lower low at 91.3 (day -10). The swing high is 105.7, and price is at 100, mid-range. The old base was 115–128.
- **Weight: 0.35.**
- **Change my mind:** I'd add above 106. I'd exit below 91.

## ef66f6c574 (AVAX)
- **Read:** There was a second capitulation to 82.0 at day -16 (volume 3×). Since then the lows have risen: 86.0, 92.2, 95.5. The high has pushed to 102.8, just above the 102.2 swing high. Above that sits the old base at 130–140.
- **Weight: 0.5.** The higher-low sequence is clear and price is testing a breakout.
- **Change my mind:** I'd exit below 92.

## deb54efd7c (DOT)
- **Read:** The low was 100.3 (day -29) and the bounce failed at 118.8. Price then made a clearly lower low at 90.2 (day -7). It is now a lower high and lower low structure with price at 100. Above that sits the old base at 135–150.
- **Weight: 0.2.** The downtrend is intact.
- **Change my mind:** I'd add above 111, a reclaim of the post-crash range. I'd go flat below 90.

## 7c36d46048 (DOGE)
- **Read:** The peak was 152 (day -52), followed by a crash to 99.7. The bounce stalled at 116.8–118.7, and price made a lower low at 89.3 (day -5). It is now at 100. Volume has been very thin in recent weeks.
- **Weight: 0.2.** The downtrend is intact.
- **Change my mind:** I'd add above 108. I'd go flat below 89.

{"eb0b7e58a1 (ADA)": 0.3, "bb95329899 (LTC)": 0.3, "04c8ebd65f (SOL)": 0.6, "694ec4b067 (LINK)": 0.4, "b983b138f7 (XRP)": 0.3, "0e390dc123 (ETH)": 0.4, "57ce4bda32 (BTC)": 0.35, "ef66f6c574 (AVAX)": 0.5, "deb54efd7c (DOT)": 0.2, "7c36d46048 (DOGE)": 0.2}
````

## Notizen
Backlog #9. Hypothese: Die Verluste kommen vom Trendfolgen (E-003: Gewicht korreliert 0,79 mit der Position in der 180-Tage-Spanne, in allen Varianten E-004 bis E-008 stabil). Ein Satz, der hohe Kurse nach starkem Anstieg ausdruecklich nicht als Kaufgrund gelten laesst, sollte den Anker lockern. Erwartung: Korrelation zur Spanne deutlich unter 0,79 und Timing-Wert hoeher als E-003. Falsifiziert, wenn die Differenz zu E-003 auf A nicht t >= 2 erreicht. Daten unveraendert (180 Tage Tageskerzen); Paragraph-4a-Vorlage unveraendert.
