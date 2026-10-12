# E-018: Wissensblock Kurzfassung: research/wissen/kernregeln-kurz.md (ab Zeile 2) vor der Aufgabe, Laengenkontrolle zu E-017

- Achse: prompt
- Basis: E-003M
- Daten: candles, 180 Tage
- Modell: claude-opus-5-5
- Werkzeug: f2794e9 versuche.py@2a621dd441
- Status: dev-informiert (Wächter B-18): ein Sieg wäre höchstens „Kandidat“, zählt als eine Variante
- Thread: https://claude.ai/code/project/chan_01VH1Un8SQtbifKwzD9jDguD?thread=cmsg_01VH1Un8SQtbifKwzD9jDguDE65qghcumVywxYhuLnuyAp

## Änderung zum Prompt der Basis
```diff
--- E-003M
+++ E-018
@@ -1,4 +1,17 @@
 # T-001 baseline trader prompt
+
+# Wissen für die Wochenentscheidung (Kurzfassung)
+
+Gilt für tägliche Kerzen und Entscheidungen über Wochen bis Monate in Krypto. Schwellen sind Faustwerte.
+
+1. **Belegt** ist in Krypto vor allem Zeitreihen-Momentum über 1 bis 4 Wochen, long-only, und dass Volatilität sich bündelt und vorhersagbar ist. Kerzenmuster, Chartformationen, Fibonacci, Pivots, Divergenzen, Oszillator-Schwellen, Wyckoff und Elliott sind auf Wochensicht nach Kosten nicht belegt.
+2. **Fast alles misst dasselbe.** RSI, Stochastik, %B, Abstand zum Durchschnitt, MACD, RCI, Ichimoku und Kanallage sind Umformungen von vergangener Rendite und Lage in der Spanne. Stimmen mehrere überein, ist das ein Befund.
+3. **Spannenlage ist kein Signal.** Hoch in der Spanne heißt höchstens halten, nicht aufstocken; tief in der Spanne ist ohne Trendwende kein Kaufgrund.
+4. **Zustand statt Abstand.** Ändere das Gewicht nur, wenn sich ein Zustand bestätigt ändert (Regime, Trendbruch, gehaltener Ausbruch über mehrere Wochenschlüsse), nicht wenn ein Indikatorwert größer oder kleiner wird.
+5. **Kosten.** Jede Umschichtung kostet 0,2 %. Änderungen unter etwa 0,15 bringen erwartbar nichts. Wenige große, begründete Änderungen schlagen viele kleine. Ohne belegtes Signal bleibt das Gewicht nahe seinem Mittel.
+6. **Volatilität steuert die Größe, nicht die Richtung.** Hohe oder steigende Volatilität rechtfertigt ein kleineres Gewicht. Komprimierte Volatilität kündigt eine größere Bewegung an, nicht ihre Richtung.
+7. **Seitwärts heißt stillhalten.** Bei unklarem Trend (viele Kreuzungen eines flachen Durchschnitts, gemischte Hoch/Tief-Folge) sind Lage- und Kreuzungssignale Rauschen.
+8. **Wochenebene vor Tagesebene.** Einzelne Tageskerzen und Tagesextreme ändern kein Wochengewicht. Eine einzelne Extremwoche deutet eher auf Gegenbewegung; Momentum erst, wenn 2 bis 4 Wochen in dieselbe Richtung zeigen.
 
 You decide the position for an asset over the next week: a number from 0 (flat) to 1 (fully long).
 Horizon is weeks to months; you do not need to trade often.
```

## Prompt
```
# T-001 baseline trader prompt

# Wissen für die Wochenentscheidung (Kurzfassung)

Gilt für tägliche Kerzen und Entscheidungen über Wochen bis Monate in Krypto. Schwellen sind Faustwerte.

1. **Belegt** ist in Krypto vor allem Zeitreihen-Momentum über 1 bis 4 Wochen, long-only, und dass Volatilität sich bündelt und vorhersagbar ist. Kerzenmuster, Chartformationen, Fibonacci, Pivots, Divergenzen, Oszillator-Schwellen, Wyckoff und Elliott sind auf Wochensicht nach Kosten nicht belegt.
2. **Fast alles misst dasselbe.** RSI, Stochastik, %B, Abstand zum Durchschnitt, MACD, RCI, Ichimoku und Kanallage sind Umformungen von vergangener Rendite und Lage in der Spanne. Stimmen mehrere überein, ist das ein Befund.
3. **Spannenlage ist kein Signal.** Hoch in der Spanne heißt höchstens halten, nicht aufstocken; tief in der Spanne ist ohne Trendwende kein Kaufgrund.
4. **Zustand statt Abstand.** Ändere das Gewicht nur, wenn sich ein Zustand bestätigt ändert (Regime, Trendbruch, gehaltener Ausbruch über mehrere Wochenschlüsse), nicht wenn ein Indikatorwert größer oder kleiner wird.
5. **Kosten.** Jede Umschichtung kostet 0,2 %. Änderungen unter etwa 0,15 bringen erwartbar nichts. Wenige große, begründete Änderungen schlagen viele kleine. Ohne belegtes Signal bleibt das Gewicht nahe seinem Mittel.
6. **Volatilität steuert die Größe, nicht die Richtung.** Hohe oder steigende Volatilität rechtfertigt ein kleineres Gewicht. Komprimierte Volatilität kündigt eine größere Bewegung an, nicht ihre Richtung.
7. **Seitwärts heißt stillhalten.** Bei unklarem Trend (viele Kreuzungen eines flachen Durchschnitts, gemischte Hoch/Tief-Folge) sind Lage- und Kreuzungssignale Rauschen.
8. **Wochenebene vor Tagesebene.** Einzelne Tageskerzen und Tagesextreme ändern kein Wochengewicht. Eine einzelne Extremwoche deutet eher auf Gegenbewegung; Momentum erst, wenn 2 bis 4 Wochen in dieselbe Richtung zeigen.

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
| A (10) | 13 | 130 | -0.12 % | -0.244 % | 0.124 % | 0.81 | 0.049 % (ohne 2026-08-30) | 9/13 | 0.378 (Basis 0.463) | 0.018 |

**Urteil: kein messbarer Unterschied**

Verbrauch: 13 Claude-Aufrufe, 811k Zeichen, Listenpreis 5.47 USD (zählt gegen Aarons Limit, keine Rechnung)

## Was die KI gedacht hat (Beispiel: Entscheidung 2026-07-05)

Alle Wochen: [denken.md](denken.md)

````
# Weekly position decision: 10 windows

## Strategy
The only rule I treat as reliable is time-series momentum over 1 to 4 weeks, long-only. Volatility sets position size, not direction. All ten windows are in a long downtrend that dropped hard around day −33 to −30. Each then made a second low around day −10 and rallied about 8–15 % in the last week. One strong week alone is not momentum, so I only add weight above the low default (about 0.15–0.2) when the 2–4-week picture agrees: higher lows, or a weekly close above the post-crash range high. High volatility caps the size.

## 3c6630209f (DOT)
- **Read:** Downtrend from about 250 to 100, with a clear sequence of lower highs: 163 (−53), 118.8 (−20), now 100.
- **Momentum:** One week is up (+9 % from 91.9), but 2–4 weeks are negative (106.8 / 113.3 / 110.6). The low was 90.2 at day −7.
- **Weight:** 0.15. The bounce is still inside the downtrend.
- **Change my mind:** A weekly close above 115 would make me raise the weight. A break below 90 would take it to 0.

## f3f65489d9 (AVAX)
- **Read:** Low of 82 at day −16, followed by higher lows at 86 (−10) and 90.6 (−7). The 2-week return is positive (88.3 → 100), and 3–4 weeks are flat (about 98).
- **Resistance:** About 102.
- **Weight:** 0.3. The structure is improving, but the longer trend is still down from 147.
- **Change my mind:** Above 103 on a weekly close I would go to about 0.5. Below 90 I would go to 0.1.

## 86d6fb8ba4 (ADA)
- **Read:** A low of 72.9 at day −10, then a vertical rally of +32 % in 4 days on 2× volume (76 → 105.5 high). The 4-week return is +15 %, and the price broke above the 100 range high.
- **Weight:** 0.3. This is a single extreme week with very high volatility, and the breakout has not yet held for even one weekly close. That points more to a pullback than to confirmed momentum.
- **Change my mind:** If price holds above 100 for 2 weekly closes, I would go to about 0.5. Below 90 (the gap zone) I would go to 0.1.

## da84649330 (DOGE)
- **Read:** Lower highs at 152 (−52) and 118.7 (−23). The low was 89.3 at day −5. The 4-week return is negative (110.8 → 100), and only the last week is up.
- **Weight:** 0.15.
- **Change my mind:** Above 114 I would raise the weight. Below 89 I would go to 0.

## 6bc07a03ce (BTC)
- **Read:** Calmer asset. The lows were 92.9 (−30) and 90.8 (−4), roughly flat, so this looks sideways in the 91–105 range. The 4-week return is about 0.
- **Weight:** 0.2. Neutral; this is the range rule.
- **Change my mind:** Above 105 I would raise to about 0.4. Below 90 I would go to 0.05.

## fa51453693 (SOL)
- **Read:** The cleanest base of the ten. The lows rise from 73.7 (−29) to 78.5 (−10) to 85.5 (−7). The price broke above the −20 range high of 93.3 and has closed above it for 4 days, now at about 100.
- **Momentum:** The 4-week return is +23 % (81.5 → 100), and both 1-week and 2-week are positive.
- **Weight:** 0.45. Several weeks agree on direction. The longer trend from 120 is still down, so the weight is not maximal.
- **Change my mind:** Above 106 I would go to about 0.6. A close below 92 would take it back to 0.2.

## 46b1c79d06 (XRP)
- **Read:** Lower highs at 133.9 (−52) and 111.8 (−20). The low was 87.2 at day −10. The 4-week return is about 0, and the 3-week return is negative (102.5).
- **Weight:** 0.2.
- **Change my mind:** Above 108 I would raise the weight. Below 88 I would go to 0.05.

## 35a3a3f47b (LTC)
- **Read:** Lows at 88.4 (−29) and 85.7 (−10), which is a slightly lower low. Today closed at 100, near the −20 high of 101. The 4-week return is +7 %, and the 2–3-week return is flat.
- **Weight:** 0.2. The breakout is not confirmed.
- **Change my mind:** A weekly close above 102 would take me to about 0.4. Below 89 I would go to 0.05.

## c606b09710 (ETH)
- **Read:** A double bottom at 84.3 (−29) and 84.7 (−9). The 4-week return is +5 %. Resistance is the −20 high at 103.6.
- **Weight:** 0.25.
- **Change my mind:** Above 104 on a weekly close I would go to about 0.45. Below 86 I would go to 0.05.

## 50a1cea1fd (LINK)
- **Read:** Lower highs at 134.8 (−56) and 106.7 (−20). The low was 86.8 at day −29 and 86.9 at day −10. The 4-week return is +2 %, and the 3-week return is negative (101.5).
- **Weight:** 0.2.
- **Change my mind:** Above 107 I would raise the weight. Below 87 I would go to 0.05.

{"3c6630209f (DOT)": 0.15, "f3f65489d9 (AVAX)": 0.3, "86d6fb8ba4 (ADA)": 0.3, "da84649330 (DOGE)": 0.15, "6bc07a03ce (BTC)": 0.2, "fa51453693 (SOL)": 0.45, "46b1c79d06 (XRP)": 0.2, "35a3a3f47b (LTC)": 0.2, "c606b09710 (ETH)": 0.25, "50a1cea1fd (LINK)": 0.2}
````

## Notizen
Backlog #34. dev-informiert (Auflagen Waechter B-18): Kurzfassung der Grundsaetze aus trader-wissen.md, mit Kenntnis der Dev-Befunde geschrieben. Ein Sieg gilt hoechstens als Kandidat, zaehlt als eine Variante, bei Sieg folgen Ablationen. Hypothese: Zeigt E-018 dasselbe wie E-017 (Umschichtung -44 %, Timing-Wert +0,30 vs E-003M), liegt es an den Kernregeln, nicht an der Laenge. Platzierung wie E-017 (nach der Titelzeile). Vorlage aus Paragraph 4a unveraendert; versuche.py vom Branch claude/project-thread-lupsy0 (PR #6).

## Nachtrag: Längenkontrolle gegen E-017 (Thread, nachträglich berechnet)

Umschichtung = mittlere absolute Gewichtsänderung je Coin und Woche. Spannenlage = Schluss in der 180-Tage-Spanne (Tief bis Hoch). E-003M = Mittel der drei E-003-Läufe.

| | E-003M | E-017 (langer Block) | E-018 (Kurzfassung) |
|---|---|---|---|
| Timing-Wert vs E-003M, %/Woche | 0 | +0,30 (t 1,57) | +0,12 (t 0,81) |
| ohne beste Woche | | +0,12 | +0,05 |
| Umschichtung | 0,131 | 0,074 (−44 %) | 0,109 (−17 %) |
| Korrelation Gewicht zu Spannenlage | 0,78 | 0,89 | 0,82 |
| innerhalb Coin | 0,72 | 0,87 | 0,79 |
| Änderungen ≥ 0,15 (Anteil) | 42 % (E-003) | 18 % | 38 % |
| Exposure | 0,46 | 0,39 | 0,38 |

Lesart: Die Kurzfassung zeigt die Richtung von E-017 (etwas ruhiger, etwas stärker an die Spanne gebunden), aber deutlich schwächer. Der Beruhigungseffekt von E-017 hängt also zum Teil an der Länge oder den Einzelregeln des langen Blocks, nicht nur an den acht Kernregeln. Alle Unterschiede liegen unter t 2; auch das ist nur ein Hinweis.

