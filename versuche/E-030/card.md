# E-030: Gegenrede: je Fenster nach der Marktlage eine Zeile "Against:" mit dem staerksten Argument gegen die eigene Einschaetzung, erst danach das Gewicht (ein Satz vor der Vorlage, Vorlage aus Paragraph 4a unveraendert)

- Achse: prompt
- Basis: E-003M
- Daten: candles, 180 Tage
- Modell: claude-opus-5-5
- Werkzeug: f2794e9 versuche.py@764f343a01
- Thread: https://claude.ai/code/project/chan_01VH1Un8SQtbifKwzD9jDguD?thread=cmsg_01VH1Un8SQtbifKwzD9jDguD8nhGvDh6cqAnZEUGoThamg

## Änderung zum Prompt der Basis
```diff
--- E-003M
+++ E-030
@@ -5,6 +5,7 @@
 
 Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
 Judge every window on its own. Do not compare windows with each other.
+For each window, after your read of the market, write the strongest argument against that read in a line starting "Against:", and set the weight only after that.
 
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
For each window, after your read of the market, write the strongest argument against that read in a line starting "Against:", and set the weight only after that.

Before the weights, write out your analysis:
1. Strategy: in 2 to 3 sentences, the rule you will apply to every window.
2. Then for each window, under its id: your read of the market (trend, structure, key levels as prices on the 100 scale), your weight and why, and the price on the 100 scale that would make you change your mind.
3. End with one JSON object mapping each window id to its weight, e.g. {"a1b2c3d4e5": 0.0, "f6a7b8c9d0": 1.0}. Nothing after it.
```

## Bewertung gegen E-003M

| Coins | Wochen | Entscheidungen | Timing-Wert/Woche | Basis | Differenz | t | ohne beste Woche | Wochen besser | Exposure | Rank-IC |
|---|---|---|---|---|---|---|---|---|---|---|
| A (10) | 13 | 130 | -0.288 % | -0.244 % | -0.043 % | -0.51 | -0.072 % (ohne 2026-07-26) | 8/13 | 0.437 (Basis 0.463) | 0.108 |

**Urteil: kein messbarer Unterschied**

Verbrauch: 13 Claude-Aufrufe, 787k Zeichen, Listenpreis 5.58 USD (zählt gegen Aarons Limit, keine Rechnung)

## Was die KI gedacht hat (Beispiel: Entscheidung 2026-07-05)

Alle Wochen: [denken.md](denken.md)

````
**Strategy:** In every window I weigh the 180-day trend (lower highs and lower lows below the old trading range) against the most recent 30-day base. I stay mostly flat while the long-term structure is a downtrend. I add exposure, up to about 0.5, only when the recent base shows a higher low or reclaims the swing high from day -20. The stop level is the most recent swing low.

---

### b316b7a94b (AVAX)
**Read:** The long-term downtrend runs from 211 to 100. Price traded in a 125–150 range until day -33, then broke down hard to 97. It made a lower low at 82 on day -16 on a 3x volume flush. Since then it has climbed steadily with higher lows (86 → 92 → 95.5 → 98) and is now at 100. Resistance sits at 101.8–102.2 (days -20 and -19), then 110–116, where the breakdown gap is. Support is 92, then 82.
**Against:** The flush to 82 and the orderly recovery look like capitulation, and a break above 102 would complete a double-bottom reversal.
**Weight 0.3:** The bounce is real but sits under resistance inside a primary downtrend.
**Change mind:** Above 103 I add. Below 92 I go flat.

### 827c6a9412 (XRP)
**Read:** The trend runs from 199 to 100. Price broke out of a 113–128 range on day -33. It bottomed at 90.7, rallied to 111.8 on day -20, failed, and made a lower low at 87.2 on day -9. The rally of the last 4 days to 100–102 brings it to the day -21 breakout level. The day -20 spike to 111.8 is the next ceiling.
**Against:** The rally from 88 to 100 came on modest volume, and the lower low below 90.7 shows sellers still in control.
**Weight 0.3**
**Change mind:** Above 104 I add. Below 93 I go flat.

### 193978a793 (DOT)
**Read:** This is the steepest decline in the set, from 254 to 100. The 135–160 range broke on days -33 to -30. The bounce failed at 118.8 on day -20, and then came a grinding series of lower lows down to 90.2 on day -7. Price is now 100 after a 5-day bounce. Resistance is 102, then 111–119. Support is 93, then 90.
**Against:** This is the cleanest lower-high/lower-low staircase of any window. The current bounce is no bigger than the failed one from day -29 to day -20.
**Weight 0.2**
**Change mind:** Above 112 I add. Below 93 I go flat.

### 9a19cf0043 (ADA)
**Read:** The trend runs from 221 to 100. Price crashed from the 125–135 range to 82.7 on day -30 at 3.9x volume, then made a lower low at 72.9 on day -10. It then went vertical, rising from 76 to 105.5 in 4 days on about 2x volume. Day 0 pulled back to a close of 100 after a high of 103. Former support at 112–122 is now overhead. The breakaway area at 85–92 is the support to watch.
**Against:** A 30% move in 4 days into the day -20 high of 100.3 is overextended. Day 0's reversal off 103 may mark an exhaustion top that retraces toward 85.
**Weight 0.3:** Volume-backed momentum, but I respect how stretched it is.
**Change mind:** If it holds above 97 and clears 106, I add. Below 92 I go flat.

### 170a317de6 (BTC)
**Read:** This window has the mildest decline, from 147 to 100. The 115–128 range broke on day -33. Price made roughly a double bottom at 92.9 (day -30) and 90.8 (day -4); the second low is slightly lower. It has now risen to 100 on fading volume. Resistance is 101.7 (day -22), then 105.7 (day -20). Support is 91.
**Against:** The second low undercut the first, and the recovery came on 0.46x volume. This could be a weak bear rally into resistance.
**Weight 0.35**
**Change mind:** Above 106 I add. Below 93 I go flat.

### 25ee90315e (SOL)
**Read:** The trend runs from 173 to 100. Price broke down from the 100–108 range to 73.7 on day -29. It then made a **higher low** at 78.5 on day -10, and has now made a **higher high**: it reached 102.9 versus 93.3 at day -20. Price is back inside the old 100–108 range. This is the only window with a clear higher-low/higher-high reversal.
**Against:** Reclaiming the old range is the first test of it. Former support at 100–105 now acts as supply, and the long-term downtrend is unbroken above 120.
**Weight 0.55**
**Change mind:** If it closes above 106, I add. Below 88 I go flat.

### b1e6971155 (ETH)
**Read:** The trend runs from 185 to 100. Price broke from the 112–120 range on day -33. It made a double bottom at 84.3 (day -29) and 84.7 (day -9), essentially equal lows. It has now risen to 100 against the day -20 high of 103.6. Day 0 volume picked up to 0.99. The neckline is 103.6. Support is 92, then 85.
**Against:** Price is still below the 103.6 neckline and well below the 112 breakdown level. A failure here would be a third test of 85.
**Weight 0.4**
**Change mind:** Above 104 I add. Below 92 I go flat.

### 6a2bc57b4e (LTC)
**Read:** The trend runs from 183 to 100. The 113–125 range broke on day -33. Lows were 88.4 (day -29) and 85.7 (day -10), slightly lower. Price closed day 0 at 100, near the 101 high from day -20 and at the top of its daily range. Resistance is 101, then 110–113. Support is 90.
**Against:** The slightly lower low and the cap at 101 leave this a range inside a downtrend, not a confirmed reversal.
**Weight 0.35**
**Change mind:** Above 102 I add. Below 90 I go flat.

### 2cebed8a0c (LINK)
**Read:** The trend runs from 174 to 100. The 112–120 range broke on day -33. Price made a double bottom at 86.8 (day -29) and 86.9 (day -10). It has now reached 100, below the 106.7 high from day -20. Volume is very light (0.34). Support is 89–90.
**Against:** The rally from the second bottom has no volume behind it. Without participation, the move from 87 to 100 can fade straight back.
**Weight 0.35**
**Change mind:** Above 107 I add. Below 89 I go flat.

### 489f750131 (DOGE)
**Read:** The trend runs from 193 to 100. This asset rallied to 152 on day -52, later than the others, then fell from the 125–145 range. It bounced at 99.7 on day -29, with lower highs at 118.7, 116.8 and 114.5. It then made a lower low at 89.3 on day -5 and is now at 100. This is a clean descending structure. Resistance is 102, then 108–114.
**Against:** The lower highs and lower low are intact, and the bounce so far is only 5 days old.
**Weight 0.2**
**Change mind:** Above 108 I add. Below 92 I go flat.

---

{"b316b7a94b (AVAX)": 0.3, "827c6a9412 (XRP)": 0.3, "193978a793 (DOT)": 0.2, "9a19cf0043 (ADA)": 0.3, "170a317de6 (BTC)": 0.35, "25ee90315e (SOL)": 0.55, "b1e6971155 (ETH)": 0.4, "6a2bc57b4e (LTC)": 0.35, "2cebed8a0c (LINK)": 0.35, "489f750131 (DOGE)": 0.2}
````

## Notizen
Backlog #22. Basis E-003M (Champion, sauber). Hypothese: Selbstkritik bremst das Hinterherlaufen. Falsifikator (vor dem Lauf festgelegt, Standard aus dem Auftrag): falsifiziert, ausser Umschichtung UND partieller Anker (werkzeuge/anker.py) liegen beide unter E-003M und der Timing-Wert faellt nicht (Differenz zu E-003M >= 0). Vergleichswerte E-003M: Umschichtung 0,121 (Mittel der drei Laeufe 0,109 / 0,110 / 0,142, mittlere absolute Gewichtsaenderung je Coin und Woche), partieller Anker 0,40. Zusaetzlich berichtet: Anteil Gewichtsaenderungen unter 0,15, Exposure, Rank-IC, und wie oft die Against-Zeile vorkommt (Befolgung). Champion-Regeln B-12/B-13/B-14: bei t >= 2 genau eine Wiederholung auf A, Urteil auf dem Mittel; B+C nur dann. Keine Harness-Option; versuche.py vom Branch claude/project-thread-lupsy0 (README par. 4). Vorlage aus Paragraph 4a woertlich unveraendert.

## Auswertung (Thread)

- Falsifikator (vor dem Lauf): falsifiziert, ausser Umschichtung und partieller Anker liegen beide unter E-003M und der Timing-Wert fällt nicht. Umschichtung 0,116 (E-003M 0,121, knapp darunter), partieller Anker 0,40 (E-003M 0,40, nicht darunter), Timing-Wert −0,04 %/Woche gegen E-003M (gefallen): **falsifiziert**.
- Befolgung: 130 von 130 Fenstern haben eine Against-Zeile.
- Anteil Gewichtsänderungen unter 0,15: 59 % (E-003-Läufe 58 / 55 / 48 %, gleiche Rechnung). 15 von 120 Änderungen sind null.
- Rank-IC 0,108 (E-003M 0,059), Exposure 0,437 (0,463), 8/13 Wochen besser. Der höhere Rank-IC trägt nicht: Differenz ohne beste Woche −0,07 %.
- Keine Wiederholung (t < 2), kein B+C. Champion bleibt E-003M.
