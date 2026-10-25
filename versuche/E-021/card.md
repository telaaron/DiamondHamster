# E-021: Seltener entscheiden: Prompt von E-003M unveraendert, die KI entscheidet nur in Woche 1, 5, 9 und 13, dazwischen bleibt ihr Gewicht stehen

- Achse: format
- Basis: E-003M
- Daten: candles, 180 Tage
- Modell: claude-opus-5-5
- Werkzeug: f2794e9 versuche.py@2a621dd441
- Thread: https://claude.ai/code/project/chan_01VH1Un8SQtbifKwzD9jDguD?thread=cmsg_01VH1Un8SQtbifKwzD9jDguDGE69ZuoqZSaFvT3aVgogE7

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
| A (10) | 13 | 130 | 0.015 % | -0.244 % | 0.26 % | 0.73 | -0.049 % (ohne 2026-08-16) | 6/13 | 0.395 (Basis 0.463) | 0.025 |

**Urteil: kein messbarer Unterschied**

Verbrauch: 4 Claude-Aufrufe, 240k Zeichen, Listenpreis 1.65 USD (zählt gegen Aarons Limit, keine Rechnung)

## Was die KI gedacht hat (Beispiel: Entscheidung 2026-07-05)

Alle Wochen: [denken.md](denken.md)

````
## Strategy
I am long only when the structure has turned up: a higher low after the capitulation leg, and the price back above the post-crash swing high. In a downtrend I hold a small or zero position. When the long-term trend is down, which it is in every window here (roughly 180 to 250 falling to 100), the weight is capped near 0.5 however good the short-term setup looks, and I grade below that cap on how clean the reversal is.

## 253e4599e3 (AVAX)
**Read:** A long downtrend from 210 to 100, with crash legs around day -150 and day -30. The day -16 flush to 82 came on 3× volume and looks like capitulation. Since then the lows have risen (86, 92, 98) and price has climbed back to 100. It is now testing resistance at 102 (the day -20 high). The breakdown shelf at 108 to 116 sits above that, and price is still well below the 128 to 135 range it held before the crash.
**Weight:** 0.30. The base is constructive, but price hasn't cleared 102 and the larger trend is still down.
**Change mind:** Below 92 I go flat. A close above 103 lets me add toward 0.5.

## 0ecca0d400 (ADA)
**Read:** The crash ran to 73 (day -10), followed by a near-vertical rally from 76 to 105.5 in four days on about 2× volume. Day 0 rejected 105 and closed at 100. The 97 to 100 resistance area (day -21/-20 highs) is being tested. The move is a strong V-reversal but very extended in the short term.
**Weight:** 0.35. The momentum is real, but chasing a 30% four-day pop under heavy overhead supply is poor risk/reward.
**Change mind:** Below 92 (gap-fill area) I go flat. Holding above 105 lets me raise toward 0.55.

## 71256881a0 (LINK)
**Read:** A rally to 134 (day -56) failed and the decline resumed. Lows at 86.8 (day -29) and 86.9 (day -10) form a double bottom. Price is at 100, just under resistance at 101.5 to 106.7. Volume on the bounce is light.
**Weight:** 0.30. The double bottom is valid but unconfirmed, and the low volume makes it less convincing.
**Change mind:** Below 95 I cut. Above 107 I raise to 0.5.

## c5f1d3be99 (SOL)
**Read:** The low was 73.7 (day -29), the next swing high 93.3 (day -20), and the next low 78.5 (day -10), which is higher than the first. Price has now reached 102.9, above that 93.3 swing high. That gives a clean higher-high/higher-low sequence. Price sits about at or above the 50-day average (around 95). The next resistance is 106 to 110, then 120.
**Weight:** 0.55. This is the clearest reversal structure of all ten windows.
**Change mind:** Below 94 the breakout has failed. Below 88 I am flat.

## 7b7c926a15 (DOGE)
**Read:** A failed rally peaked at 152 (day -52), then the decline continued. The day -5 low of 89.3 undercut the day -29 low of 99.7, so the lows are still falling. Lower highs at 118.7 and 114 cap the price. The bounce to 100 is on thin volume.
**Weight:** 0.15. The downtrend is intact.
**Change mind:** I would go higher above 108, which would retake the post-crash range.

## 877293edcf (XRP)
**Read:** The day -10 low of 87.2 undercut the day -29 low of 90.7, another lower low. Resistance is at 102 to 107 (the day -20 spike to 111.8 faded). Price at 100 is mid-range.
**Weight:** 0.20. The trend is down, and the bounce is only a reflex so far.
**Change mind:** Above 108 I would raise. Below 90 I go flat.

## 0888b4a0e2 (DOT)
**Read:** This window has the steepest overall decline (about 250 down to 100). The day -7 low of 90.2 is well below the day -29 low of 100.3. The lower highs at 118.8 and 114 are intact. The recovery to 100 has come on average volume.
**Weight:** 0.15.
**Change mind:** Above 115 would break the lower-high sequence. Below 90 I am flat.

## 2fc870dfda (ETH)
**Read:** Lows at 84.3 (day -29) and 84.7 (day -9) form a double bottom. Price has rallied to 100, just under the 103.6 neckline (the day -20 high). Day 0 volume ticked up to about 1.0.
**Weight:** 0.30. The base is good but the breakout hasn't happened.
**Change mind:** Above 104 I raise to 0.5. Below 87 I am flat.

## 4564f03d20 (BTC)
**Read:** This is a smaller-amplitude version of the same pattern. The day -10 low of 91.3 slightly undercut the day -30 low of 92.9. Resistance is at 103 to 105.7. Price is at 100, rising steadily on low volume.
**Weight:** 0.25. The base is roughly flat, but the slight lower low leaves the structure only neutral.
**Change mind:** Above 106 I raise. Below 91 I am flat.

## 1d38caa375 (LTC)
**Read:** The day -11/-10 low of 85.7 undercut the day -29 low of 88.4. Price closed day 0 at the high of the day (100), pressing the 101.2 resistance from day -20/-19. The rest of the structure is a slow grind lower from 132.
**Weight:** 0.25. A breakout attempt is in progress, but the lower low argues for caution.
**Change mind:** A close above 102 lets me add toward 0.45. Below 91 I am flat.

{"253e4599e3 (AVAX)": 0.3, "0ecca0d400 (ADA)": 0.35, "71256881a0 (LINK)": 0.3, "c5f1d3be99 (SOL)": 0.55, "7b7c926a15 (DOGE)": 0.15, "877293edcf (XRP)": 0.2, "0888b4a0e2 (DOT)": 0.15, "2fc870dfda (ETH)": 0.3, "4564f03d20 (BTC)": 0.25, "1d38caa375 (LTC)": 0.25}
````

## Notizen
Backlog #29. Hypothese (Review-002, E-013 bis E-015): eine feste Position schlaegt das Umschichten; weniger Entscheidungen senken die Kosten des Hinterherlaufens, ohne den Prompt zu aendern. Falsifiziert, wenn der Timing-Wert gegenueber E-003M auf A nicht positiv ist (Differenz <= 0). Gemessen wird nach B-12/B-14: messbar erst ab t >= 2, dann genau eine Wiederholung auf A. Vergleich: E-003M (Umschichtung ~0,13, partiell 0,40), E-016 (+0,16 t 1,05, 0,04, -0,15), E-020 (+0,25 t 1,38, 0,025, 0,15). Vorlage aus Paragraph 4a unveraendert; versuche.py vom Branch claude/project-thread-lupsy0 (PR #6).

## Zusatzmetriken (Thread)
| | E-003M (3 Läufe) | E-016 | E-020 | E-021 |
|---|---|---|---|---|
| Umschichtung je Woche | 0,118 / 0,120 / 0,154 | 0,037 | 0,025 | 0,040 |
| Anteil Gewichtsänderungen unter 0,15 | 0,63 / 0,61 / 0,52 | 0,88 | 0,90 | 0,85 (nur in Entscheidungswochen: 0,40) |
| Partieller Ankerwert (anker.py) | 0,40 | −0,15 | 0,15 | 0,40 |

Falsifikator: Differenz zum Timing-Wert von E-003M ≤ 0. Ergebnis +0,26 %/Woche, also formal nicht falsifiziert; ohne die beste Woche (16.08., E-003M −3,13 %, E-021 +0,84 %) −0,05 %. Der Vorsprung hängt an einer Woche und zählt nach §2 nicht.
