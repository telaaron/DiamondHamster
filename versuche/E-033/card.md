# E-033: Kurzer Prompt: Erklaerungen gestrichen (Horizont-Zeile, Beschreibung des Datenformats, Satz zur getrennten Beurteilung der Fenster); nur Aufgabe und Vorlage aus Paragraph 4a bleiben, diese unveraendert

- Achse: prompt
- Basis: E-003M
- Daten: candles, 180 Tage
- Modell: claude-opus-5-5
- Werkzeug: f2794e9 versuche.py@764f343a01
- Thread: https://claude.ai/code/project/chan_01VH1Un8SQtbifKwzD9jDguD?thread=cmsg_01VH1Un8SQtbifKwzD9jDguDLDAEDWtmSdqBXwDEAQFeMF

## Änderung zum Prompt der Basis
```diff
--- E-003M
+++ E-033
@@ -1,10 +1,6 @@
 # T-001 baseline trader prompt
 
 You decide the position for an asset over the next week: a number from 0 (flat) to 1 (fully long).
-Horizon is weeks to months; you do not need to trade often.
-
-Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
-Judge every window on its own. Do not compare windows with each other.
 
 Before the weights, write out your analysis:
 1. Strategy: in 2 to 3 sentences, the rule you will apply to every window.
```

## Prompt
```
# T-001 baseline trader prompt

You decide the position for an asset over the next week: a number from 0 (flat) to 1 (fully long).

Before the weights, write out your analysis:
1. Strategy: in 2 to 3 sentences, the rule you will apply to every window.
2. Then for each window, under its id: your read of the market (trend, structure, key levels as prices on the 100 scale), your weight and why, and the price on the 100 scale that would make you change your mind.
3. End with one JSON object mapping each window id to its weight, e.g. {"a1b2c3d4e5": 0.0, "f6a7b8c9d0": 1.0}. Nothing after it.
```

## Bewertung gegen E-003M

| Coins | Wochen | Entscheidungen | Timing-Wert/Woche | Basis | Differenz | t | ohne beste Woche | Wochen besser | Exposure | Rank-IC |
|---|---|---|---|---|---|---|---|---|---|---|
| A (10) | 13 | 130 | -0.415 % | -0.244 % | -0.17 % | -1.21 | -0.219 % (ohne 2026-08-23) | 3/13 | 0.43 (Basis 0.463) | -0.044 |

**Urteil: kein messbarer Unterschied**

Verbrauch: 13 Claude-Aufrufe, 780k Zeichen, Listenpreis 5.34 USD (zählt gegen Aarons Limit, keine Rechnung)

## Was die KI gedacht hat (Beispiel: Entscheidung 2026-07-05)

Alle Wochen: [denken.md](denken.md)

````
## Strategy

All ten windows share one structure. There is a six-month downtrend from 150–250 down to about 100, then a capitulation leg around days −33 to −30, a retest low around days −11 to −5, and a sharp 3–4 day rally into 100. I apply one rule to every window. Because price is below its 50-day trend everywhere, the weight is capped at 0.5. The weight is **0.5** if the close is above the 20-day SMA *and* above the close of the day −20 bounce high, which was the last lower high. It is **0.3** if the close is above the 20-day SMA but still below that lower high. It is **0.0** if the close is below the 20-day SMA.

---

### a5666e1567 (XRP)
- **Read:** Downtrend. The capitulation low was 90.7 (day −29) and the retest low was 87.2, a marginal lower low. The 4-day rally ran from 90 to 100. The 20-day SMA is about 95.7, so price is above it. The day −20 lower high closed at 107.0 (high 111.8), and price has not reclaimed it. Resistance is 102–107; support is 94 and 87.
- **Weight:** 0.3. Price is above the 20-day SMA but below the lower high.
- **Change mind:** A close above 107 raises the weight to 0.5. A close below 95 cuts it to 0.

### 842d7129d6 (SOL)
- **Read:** The capitulation low was 73.7 (day −29) and the retest low was 78.5, a higher low. Price has rallied through the day −20 high (93.3) and the 101–102 area. The 20-day SMA is about 88. This is a double bottom with a breakout. Overhead supply sits at 104–112 (days −50 to −45).
- **Weight:** 0.5. Both conditions are met, and the weight is capped by the long-term trend.
- **Change mind:** A close below 93 (failed breakout) cuts it to 0.3. A close below 88 cuts it to 0.

### 35cf8dfabe (AVAX)
- **Read:** The day −16 flush to 82.0 undercut the day −29 low of 89.9. Price then recovered to 100, above the day −20 close of 98.8 but below its wick at 102.2. The 20-day SMA is about 94. The structure is a reclaim of the range after a bear trap. Resistance is 102 and then 111 (gap-down origin).
- **Weight:** 0.5.
- **Change mind:** A close below 98 cuts it to 0.3. A close below 94 cuts it to 0.

### c317be351c (DOGE)
- **Read:** This window had a much higher post-crash range (105–114, day −21 close 114.2), so its decline into the day −5 low of 89.3 was steeper. The rebound to 100 is still below the 20-day SMA of about 100.6. Resistance is 101–108; support is 92 and 89.
- **Weight:** 0.0. Price is below the 20-day SMA.
- **Change mind:** A close above 102 raises the weight to 0.3. A close above 114 raises it to 0.5.

### b9ea9a000e (DOT)
- **Read:** The pattern matches the previous window. The post-crash range was 108–115 (day −20 close 114.8), and the low was 90.2. The 20-day SMA is about 101.5, so price at 100 is below it. Resistance is 101.5, 106 and 115.
- **Weight:** 0.0.
- **Change mind:** A close above 102 raises the weight to 0.3. A close below 90 confirms the downtrend.

### 15ca0b0427 (LINK)
- **Read:** The capitulation low was 86.8 and the retest low was 86.9 (day −10), a flat double bottom. The 20-day SMA is about 95.5, so price is above it. The day −20 lower high closed at 102.9 (high 106.7), and price has not reclaimed it.
- **Weight:** 0.3.
- **Change mind:** A close above 103 raises the weight to 0.5. A close below 95 cuts it to 0.

### 63279879e7 (BTC)
- **Read:** This is the lowest-volatility window. The low was 90.8 (day −4) after 92.9 on day −30. The 20-day SMA is about 97.5, so price is above it. The day −20 lower high closed at 104.2 and has not been reclaimed. Resistance is 101–104; support is 96 and 91.
- **Weight:** 0.3.
- **Change mind:** A close above 104.5 raises the weight to 0.5. A close below 96 cuts it to 0.

### 49ce2c5978 (ETH)
- **Read:** The capitulation low was 84.3 and the retest low was 84.7, a double bottom. The 20-day SMA is about 94, so price is above it. The day −20 lower high closed at 100.6 (high 103.6), and price at 100.0 is just below it. Day 0 volume (0.99) was elevated with the close at 100.
- **Weight:** 0.3.
- **Change mind:** A close above 101 raises the weight to 0.5. A close below 94 cuts it to 0.

### eaff3a44cd (LTC)
- **Read:** The capitulation low was 88.4. The retest low was 85.7, a slightly lower low, but it was quickly reclaimed. The 20-day SMA is about 95. The day 0 close of 100.0 sits at the session high (100.7) and above the day −20 close of 99.9, so it is a marginal breakout. Resistance is 101 and then 110–114.
- **Weight:** 0.5. This is the weakest of the 0.5 calls.
- **Change mind:** A close below 97 cuts it to 0.3. A close below 95 cuts it to 0.

### 210cd3c051 (ADA)
- **Read:** This was the deepest flush, to 72.9 (day −10), well below the day −29 low of 78.4. It was followed by a V-reversal from 76 to 101 in 4 days on high volume (1.8–2.2). Price has cleared the day −20 high of 100.3 on a close basis (94.2 close). The 20-day SMA is about 87. Momentum is strong but extended, and supply sits at 106–112 (the day −32 to −33 gap).
- **Weight:** 0.5.
- **Change mind:** A close below 94 (failed reclaim) cuts it to 0.3. A close below 87 cuts it to 0.

---

{"a5666e1567 (XRP)": 0.3, "842d7129d6 (SOL)": 0.5, "35cf8dfabe (AVAX)": 0.5, "c317be351c (DOGE)": 0.0, "b9ea9a000e (DOT)": 0.0, "15ca0b0427 (LINK)": 0.3, "63279879e7 (BTC)": 0.3, "49ce2c5978 (ETH)": 0.3, "eaff3a44cd (LTC)": 0.5, "210cd3c051 (ADA)": 0.5}
````

## Notizen
Backlog #12. Hypothese: prueft, ob die Erklaerungen um die Aufgabe helfen oder ablenken. Prompt-Laenge: E-003M 942 Zeichen, E-033 593 Zeichen (-37 %). Die Vorlage aus Paragraph 4a bleibt, weil das Streichen der Analyse eine zweite Aenderung waere; die Fenster tragen weiter ihre Kopfzeile 'day o h l c v'. Falsifikator (vor dem Lauf festgelegt, Standard aus dem Auftrag): die langen Anweisungen 'helfen', wenn E-033 auf dem Timing-Wert schlechter als E-003M ist, und 'lenken ab', wenn E-033 besser ist; falsifiziert (kein Effekt), wenn Timing-Wert (|t| < 2), Umschichtung (E-003M 0,121) und partieller Anker (E-003M 0,40) alle im Rauschen von E-003M bleiben. Als Rauschen fuer Umschichtung und partiellen Anker gilt die Spanne der drei E-003-Laeufe. Zusaetzlich berichtet: Anteil Gewichtsaenderungen unter 0,15, Exposure, Rank-IC, Vergleich mit konstant 0,5. Champion-Regeln B-12/B-13/B-14: bei t >= 2 genau eine Wiederholung auf A, Urteil auf dem Mittel; B+C nur dann. Keine Harness-Option; versuche.py vom Branch claude/project-thread-lupsy0.

## Auswertung (Thread)

- Prompt-Länge: E-003M 942 Zeichen, E-033 593 Zeichen (−37 %). Gestrichen: Horizont-Zeile, Beschreibung des Datenformats, Satz zur getrennten Beurteilung der Fenster. Vorlage aus §4a unverändert.
- Falsifikator (vor dem Lauf): kein Effekt, wenn Timing-Wert, Umschichtung und partieller Anker alle im Rauschen von E-003M bleiben. Timing-Wert −0,17 %/Woche gegen E-003M (t −1,21, ohne beste Woche −0,22 %, 3/13 Wochen besser): im Rauschen, Richtung "die Erklärungen helfen". Umschichtung 0,162 (E-003M 0,121, E-003-Läufe 0,118 / 0,120 / 0,154) und partieller Anker 0,19 (E-003M 0,40, Läufe 0,39 / 0,44 / 0,31) liegen außerhalb der Spanne der drei E-003-Läufe: **nicht falsifiziert, das Verhalten ändert sich, aber nicht belegt** (t < 2).
- Was sich ändert: Ohne die Erklärungen baut die KI mechanischere Regeln (Woche 1: 20-Tage-Schnitt und letztes tieferes Hoch, Stufen 0 / 0,3 / 0,5) und geht häufiger ganz raus (5 Gewichte 0,0; E-003-Läufe 0). Sie hängt weniger an der Spannenlage (einfache Korrelation 0,61 statt 0,77), schichtet dafür mehr um. Größte Änderungen: DOT +0,75 (09-06) und −0,60 (09-13), ADA +0,60 (09-06), LTC +0,55 (07-19), LINK −0,50 (09-13), ADA −0,50 (07-12).
- Anteil Gewichtsänderungen unter 0,15: 58 % (E-003-Läufe 63 / 61 / 52 %).
- Gegen eine konstante Position 0,5 (gleiche Kosten 0,2 % je Umschichtung): −0,61 %/Woche, t −1,25, 5/13 Wochen besser (E-003-Läufe −0,25 / −0,36 / −0,37).
- Rank-IC −0,044 (E-003M 0,059), Exposure 0,43 (0,46).
- Keine Wiederholung (t < 2), kein B+C. Champion bleibt E-003M.
