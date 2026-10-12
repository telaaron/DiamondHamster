# E-006: Weniger Historie: 60 statt 180 Tage Tageskerzen pro Fenster; im Prompt nur die Angabe '180 days' auf '60 days' angepasst, damit sie zu den Daten passt

- Achse: daten
- Basis: E-003
- Daten: candles, 60 Tage
- Modell: claude-opus-5-5
- Thread: https://claude.ai/code/project/chan_01VH1Un8SQtbifKwzD9jDguD?thread=cmsg_01VH1Un8SQtbifKwzD9jDguDKHQMpHebko568V85GKVMRu

## Änderung zum Prompt der Basis
```diff
--- E-003
+++ E-006
@@ -3,7 +3,7 @@
 You decide the position for an asset over the next week: a number from 0 (flat) to 1 (fully long).
 Horizon is weeks to months; you do not need to trade often.
 
-Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
+Each window is daily OHLCV for the last 60 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
 Judge every window on its own. Do not compare windows with each other.
 
 Before the weights, write out your analysis:
```

## Prompt
```
# T-001 baseline trader prompt

You decide the position for an asset over the next week: a number from 0 (flat) to 1 (fully long).
Horizon is weeks to months; you do not need to trade often.

Each window is daily OHLCV for the last 60 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
Judge every window on its own. Do not compare windows with each other.

Before the weights, write out your analysis:
1. Strategy: in 2 to 3 sentences, the rule you will apply to every window.
2. Then for each window, under its id: your read of the market (trend, structure, key levels as prices on the 100 scale), your weight and why, and the price on the 100 scale that would make you change your mind.
3. End with one JSON object mapping each window id to its weight, e.g. {"a1b2c3d4e5": 0.0, "f6a7b8c9d0": 1.0}. Nothing after it.
```

## Bewertung gegen E-003

| Coins | Wochen | Entscheidungen | Timing-Wert/Woche | Basis | Differenz | t | ohne beste Woche | Wochen besser | Exposure | Rank-IC |
|---|---|---|---|---|---|---|---|---|---|---|
| A (10) | 13 | 130 | -0.381 % | -0.151 % | -0.231 % | -1.41 | -0.283 % (ohne 2026-07-12) | 4/13 | 0.474 (Basis 0.457) | 0.115 |

**Urteil: kein messbarer Unterschied**

Verbrauch: 13 Claude-Aufrufe, 264k Zeichen, Listenpreis 2.5 USD (zählt gegen Aarons Limit, keine Rechnung)

## Was die KI gedacht hat (Beispiel: Entscheidung 2026-07-05)

Alle Wochen: [denken.md](denken.md)

````
## Strategy

I go long only when the structure since the capitulation low has turned up, meaning higher lows and a reclaimed bounce high. I stay small when the window is still making lower lows below heavy overhead supply. Weight scales with how much of the post-crash damage has been repaired. A clean break of the nearest resistance or support would change my view.

## 4c87bf8629 (LTC)
- **Read:** The trend is down from 132.3 to the crash low of 88.4 (day -29). The bounce stalled at 101.2, then the price made a lower low at 85.7 (days -11/-10). It has rallied back to 100, at the top of the 85.7–101.2 range. The longer trend is still lower highs.
- **Weight: 0.35.** Price is testing range resistance without a break, so this is a modest, momentum-only long.
- **Change mind:** A close above 101.5 would make me add. A close below 95 would make me go flat.

## a9e7988263 (DOGE)
- **Read:** The decline runs from 152.3 to 99.7, with a bounce to 118.7. The price then made a lower low at 89.3 (day -5). It is now at 100, with resistance at 106–114 overhead. Volume is fading on this rally (0.54).
- **Weight: 0.2.** The structure is still lower highs and lower lows, and the rally is on thin volume.
- **Change mind:** A close above 106 would make me add. A close below 96.7 would make me go to 0.

## bcc99bc412 (AVAX)
- **Read:** A crash from 151.5 reached 89.9, followed by a capitulation flush to 82.0 on 3.2x volume (day -16). Since then the price has made a sequence of higher lows: 86.0, 90.6, 92.2, 95.5. It is now pressing the 102–103 resistance.
- **Weight: 0.45.** The washout and higher lows are constructive, but resistance has not yet been cleared.
- **Change mind:** A close above 103 would make me add. A close below 95.5 would make me reduce.

## 85af862477 (ETH)
- **Read:** The price fell from 133.4 to 84.3, bounced to 103.6, and then double-bottomed at 84.7 (day -9). It is now at 100 on above-average volume (1.24). The neckline is at 103.6.
- **Weight: 0.5.** The double bottom is well formed and the price is close to its trigger.
- **Change mind:** A close above 103.6 would take me to full. A close below 94.9 would make me cut.

## 6027606f43 (ADA)
- **Read:** The price fell from 152.3 to 78.4 and bounced to 100.3. It made a lower low at 72.9, then surged 30% in four days on heavy volume (around 2x). It closed above the 100.3 bounce high on day -1, but day 0 rejected from 103 back to 100. The move is strong but extended.
- **Weight: 0.5.** The breakout is real, but this is a chase at extended levels.
- **Change mind:** A close above 105.5 would make me add. A close below 94 would make me go flat, since that would mean the breakout failed.

## f98b10a990 (BTC)
- **Read:** This is a milder crash, from 129.6 to 92.9. The bounce reached 105.7. A double-bottom-type retest followed at 90.8–91.3. The price is now at 100 on low volume, with resistance at 104–105.7.
- **Weight: 0.4.** The base is reasonable, but resistance is overhead and volume is light.
- **Change mind:** A close above 105.7 would make me add. A close below 96 would make me cut.

## cc1bed9ec5 (XRP)
- **Read:** The price fell from 133.9 to 90.7, then a spike bounce reached 111.8. It made a lower low at 87.2 (day -9). It is now at 100, with resistance at 102.6–107.
- **Weight: 0.35.** The low is marginally lower, and supply from the spike is still overhead.
- **Change mind:** A close above 103 would make me add. A close below 97 would make me cut.

## 7fd84d9552 (LINK)
- **Read:** The price fell from 134.8 to 86.8 and bounced to 106.7. It then formed a double bottom at 86.9. It is now at 100, with resistance at 101.5–106.7. Volume is very light (0.39).
- **Weight: 0.4.** The base is fair, but the rally lacks conviction.
- **Change mind:** A close above 102 would make me add. A close below 95.8 would make me cut.

## f0f627624e (DOT)
- **Read:** The decline runs from 163.2 to 100.3, with a bounce to 118.8. The price then made a lower low at 90.2 (day -7). It is now at 100, still well below the 106–118 supply zone. The trend remains down.
- **Weight: 0.2.** The structure is lower lows, and the price is merely back to the old crash level.
- **Change mind:** A close above 106 would make me add. A close below 95 would make me go to 0.

## 689ff0e8f8 (SOL)
- **Read:** The price fell from 120.6 to 73.7, bounced to 93.3, and then made a higher low at 78.5 (day -10). The rally since then cleared 93.3 decisively, a higher high, and is now consolidating around 100–103. Of all the windows, this one shows the clearest trend reversal.
- **Weight: 0.7.** It has a higher low plus a reclaimed bounce high.
- **Change mind:** A close above 103 would take me to full. A close below 94 would make me cut.

{"4c87bf8629 (LTC)": 0.35, "a9e7988263 (DOGE)": 0.2, "bcc99bc412 (AVAX)": 0.45, "85af862477 (ETH)": 0.5, "6027606f43 (ADA)": 0.5, "f98b10a990 (BTC)": 0.4, "cc1bed9ec5 (XRP)": 0.35, "7fd84d9552 (LINK)": 0.4, "f0f627624e (DOT)": 0.2, "689ff0e8f8 (SOL)": 0.7}
````

## Notizen
Backlog #4. Hypothese: zu viel Daten kann schaden. E-003 ordnet das Gewicht stark der Position in der 180-Tage-Spanne zu (Korrelation 0,79). Mit 60 Tagen fehlt die lange Spanne; die KI muss sich auf juengere Struktur stuetzen, und der Prompt ist ein Drittel so lang. Erwartung: anderer Anker (60-Tage-Spanne), Timing-Wert hoeher als E-003. Falsifiziert, wenn die Differenz zu E-003 auf A nicht t >= 2 erreicht. Gegenprobe ist Backlog #5 (365 Tage).
