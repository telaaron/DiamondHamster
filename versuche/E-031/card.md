# E-031: Feste Startregel: jedes Fenster startet bei Gewicht 0,5, Abweichung nur mit benanntem Kipp-Punkt (Preis auf der 100-Skala) und hoechstens 0,25, Gewichte also 0,25 bis 0,75 (ein Satz nach der Horizont-Zeile, Vorlage aus Paragraph 4a unveraendert)

- Achse: prompt
- Basis: E-003M
- Daten: candles, 180 Tage
- Modell: claude-opus-5-5
- Werkzeug: f2794e9 versuche.py@764f343a01
- Thread: https://claude.ai/code/project/chan_01VH1Un8SQtbifKwzD9jDguD?thread=cmsg_01VH1Un8SQtbifKwzD9jDguD3nZ8gvGiqGqPBzMTLhp1p8

## Änderung zum Prompt der Basis
```diff
--- E-003M
+++ E-031
@@ -2,6 +2,7 @@
 
 You decide the position for an asset over the next week: a number from 0 (flat) to 1 (fully long).
 Horizon is weeks to months; you do not need to trade often.
+Start every window at a weight of 0.5. Move away from 0.5 only when you can name the tipping point, a price on the 100 scale, that justifies the move, and never by more than 0.25: every weight stays between 0.25 and 0.75.
 
 Each window is daily OHLCV for the last 180 days, one line per day: `day o h l c v`. Day 0 is the decision day, -1 the day before; prices are scaled so the last close is 100; volume is relative to the window average.
 Judge every window on its own. Do not compare windows with each other.
```

## Prompt
```
# T-001 baseline trader prompt

You decide the position for an asset over the next week: a number from 0 (flat) to 1 (fully long).
Horizon is weeks to months; you do not need to trade often.
Start every window at a weight of 0.5. Move away from 0.5 only when you can name the tipping point, a price on the 100 scale, that justifies the move, and never by more than 0.25: every weight stays between 0.25 and 0.75.

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
| A (10) | 13 | 130 | -0.112 % | -0.244 % | 0.132 % | 0.85 | 0.021 % (ohne 2026-08-16) | 8/13 | 0.522 (Basis 0.463) | -0.041 |

**Urteil: kein messbarer Unterschied**

Verbrauch: 13 Claude-Aufrufe, 787k Zeichen, Listenpreis 5.43 USD (zählt gegen Aarons Limit, keine Rechnung)

## Was die KI gedacht hat (Beispiel: Entscheidung 2026-07-05)

Alle Wochen: [denken.md](denken.md)

````
**Strategy:** All weights start at 0.5. In a long-term downtrend I go underweight (0.40) when the post-crash structure still shows lower lows below the relief-rally high. I stay near neutral (0.45 to 0.50) when there is a double bottom or higher low but the neckline has not broken. I go overweight (0.55 to 0.60) only when price has decisively cleared the first relief-rally high, giving a higher high on top of a higher low.

## 02453b79fc (DOGE)
- **Read:** The trend is down from about 193 to 100. A crash around day -30 hit a low of 99.7. The relief rally topped at 118.7, then price made a lower low at 89.3 (day -5). It is now back at 100 on fading volume.
- **Weight: 0.40.** The lower-high, lower-low sequence is intact, and resistance at 110 to 114 is overhead.
- **Change of mind:** A close above 114 would take me back to 0.50 or higher. A close below 89 would take me to 0.25.

## e1a86ae9be (LTC)
- **Read:** The trend is down from about 183 to 100. The crash low was 88.4, the rally high 101.2, and price then made a lower low at 85.7. It has since made higher lows (89.8) and is pressing the 100 to 101 resistance, but has not cleared it.
- **Weight: 0.45.** This is a modest underweight: the reversal attempt is real but unconfirmed below 101.2.
- **Change of mind:** A close above 102 would take me to 0.60. A close below 89 would take me to 0.30.

## 2575660994 (SOL)
- **Read:** The trend is down from about 173 to 100. The crash low was 73.7, the relief high 93.3, and the next low 78.5 was a higher low. Price then broke above 93 to make a higher high near 102. It is now sitting at the old pre-crash shelf at 100 to 105.
- **Weight: 0.60.** The short-term trend has turned up, with higher highs and higher lows.
- **Change of mind:** A close below 88 would take me to 0.40.

## bba5d84773 (DOT)
- **Read:** The trend is down from about 254 to 100. The crash low was 100.3, the relief high 118.8, and price then made a lower low at 90.2. It is now back at 100, and resistance at 111 to 119 is unbroken.
- **Weight: 0.40.**
- **Change of mind:** A close above 111 would take me to 0.50. A close below 90 would take me to 0.25.

## 4602e3afa2 (AVAX)
- **Read:** The trend is down from about 211 to 100. Price capitulated to 82.0 at day -16 on volume of 3x the average. Since then it has made higher lows (86, 92.2) and is now testing resistance at 102.2 to 102.8.
- **Weight: 0.50.** The constructive base is offset by the overhead resistance.
- **Change of mind:** A close above 103 would take me to 0.60. A close below 92 would take me to 0.35.

## 9122e05d2f (LINK)
- **Read:** The trend is down from about 174 to 100. There is a double bottom at 86.8 and 86.9, with the neckline at 106.7. Price is now at 100 on light volume.
- **Weight: 0.45.**
- **Change of mind:** A close above 107 would take me to 0.60. A close below 86.8 would take me to 0.30.

## 2a9deecd20 (XRP)
- **Read:** The trend is down from about 199 to 100. The crash low was 90.7, the relief high 111.8, and price then made a lower low at 87.2. It is now at 100, with resistance at 107 to 112.
- **Weight: 0.40.** The lower-low structure remains intact.
- **Change of mind:** A close above 112 would take me to 0.55. A close below 87 would take me to 0.25.

## dd31e71229 (BTC)
- **Read:** This is a milder downtrend, from about 147 to 100. The crash low was 92.9, the relief high 105.7, and price then made a marginal lower low at 90.8. The rally to 100 came on shrinking volume.
- **Weight: 0.40.**
- **Change of mind:** A close above 106 would take me to 0.55. A close below 90.8 would take me to 0.25.

## c439413bdd (ETH)
- **Read:** The trend is down from about 185 to 100. There is a double bottom at 84.3 and 84.7, with the neckline at 103.6. Price is now at 100, and day 0 volume was near average.
- **Weight: 0.45.**
- **Change of mind:** A close above 104 would take me to 0.60. A close below 84 would take me to 0.30.

## 561532f282 (ADA)
- **Read:** The trend is down from about 221 to 100. The crash low was 78.4, the relief high 100.3, and price then made a lower low at 72.9. Since then it has had a violent rally from 76 to 101 in four days on volume of 1.8 to 2.2x the average, clearing the 100.3 relief high (the day -1 high was 105.5). Price is extended, and the next resistance is 105 to 112.
- **Weight: 0.60.** This is a momentum breakout with volume confirmation.
- **Change of mind:** A close below 92 would take me to 0.40.

{"02453b79fc (DOGE)": 0.40, "e1a86ae9be (LTC)": 0.45, "2575660994 (SOL)": 0.60, "bba5d84773 (DOT)": 0.40, "4602e3afa2 (AVAX)": 0.50, "9122e05d2f (LINK)": 0.45, "2a9deecd20 (XRP)": 0.40, "dd31e71229 (BTC)": 0.40, "c439413bdd (ETH)": 0.45, "561532f282 (ADA)": 0.60}
````

## Notizen
Backlog #23. Basis E-003M (Champion, sauber). Hypothese: verbindet die Ruhe aus E-002 mit der Pflicht-Analyse und begrenzt teure Umschichtung. Falsifikator (vor dem Lauf festgelegt, Standard aus dem Auftrag): falsifiziert, ausser der Timing-Wert liegt ueber E-003M (Differenz > 0) UND die Umschichtung liegt unter E-003M (0,121, mittlere absolute Gewichtsaenderung je Coin und Woche). Zusaetzlich berichtet: partieller Anker (werkzeuge/anker.py, E-003M 0,40), Anteil Gewichtsaenderungen unter 0,15, Exposure, Rank-IC, Befolgung (Anteil Gewichte in 0,25 bis 0,75, Anteil genau 0,5), und Vergleich mit einer konstanten Position 0,5 (Rendite pro Woche nach Kosten 0,2 % je Umschichtung, Differenz E-031 minus konstant 0,5 mit t-Wert), weil der Timing-Wert nur gegen die eigene mittlere Exposure misst. Champion-Regeln B-12/B-13/B-14: bei t >= 2 genau eine Wiederholung auf A, Urteil auf dem Mittel; B+C nur dann. Keine Harness-Option; versuche.py vom Branch claude/project-thread-lupsy0 (README par. 4). Vorlage aus Paragraph 4a woertlich unveraendert.

## Auswertung (Thread)

- Falsifikator (vor dem Lauf): falsifiziert, außer der Timing-Wert liegt über E-003M und die Umschichtung unter E-003M. Timing-Wert +0,13 %/Woche gegen E-003M (t 0,85), Umschichtung 0,066 (E-003M 0,121, gleiche Rechnung über 130 Entscheidungen): **nicht falsifiziert, aber nicht belegt**. Der Vorsprung hängt an Woche 2026-08-16 (ohne sie +0,02 %), t < 2.
- Partieller Anker 0,24 (E-003M 0,40), einfache Korrelation zur Spannenlage 0,65 (0,77).
- Befolgung: 130 von 130 Gewichten zwischen 0,25 und 0,75 (Spanne 0,30 bis 0,75), 20 genau 0,5. Größte Änderung +0,30 (SOL, 08-30) überschreitet den Abstand 0,25 zur Mitte nicht.
- Anteil Gewichtsänderungen unter 0,15: 85 % (E-003-Läufe 63 / 61 / 52 %). 29 von 120 Änderungen sind null.
- Gegen eine konstante Position 0,5 (gleiche Kosten 0,2 % je Umschichtung): −0,01 %/Woche, t −0,05, 7/13 Wochen besser. Die drei E-003-Läufe liegen dagegen −0,25 / −0,36 / −0,37 %/Woche hinter konstant 0,5. Die Startregel macht die KI also fast so gut wie konstant 0,5, aber nicht besser.
- Rank-IC −0,04 (E-003M 0,059), Exposure 0,52 (0,46).
- Keine Wiederholung (t < 2), kein B+C. Champion bleibt E-003M.
