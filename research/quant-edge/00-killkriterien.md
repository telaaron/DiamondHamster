# Kill-Kriterien, vorab festgelegt (2026-10-16, vor jedem Testlauf)

Geschrieben, bevor eine Zeile Testcode lief. Jede spätere Abweichung muss hier als Nachtrag mit Datum stehen.

## Datenfenster
- Entwicklung (In-Sample + Walk-Forward): Beginn der jeweiligen Reihe bis 2024-12-31.
- Regel-Holdout 2025-01-01 bis 2026-06-30: **nicht geladen, nicht getestet** (Forschungsprotokoll §1, §11).
- 2026-07-01 bis heute: nur als Dev-Nachschau, zählt nicht als Beweis (Kurse sind bekannt, Fenster zu kurz).

## Kosten (Protokoll §1.5)
- 0,2 % pro Seite und pro Bein (Spot und Perp getrennt). Signal am Schluss von Tag t, Ausführung frühestens Open t+1.
- Carry: Kapitalbedarf 1,5 je 1 Einheit Nominal (1,0 Spot + 0,5 Margin für den Short), Rendite auf dieses Kapital.

## K1 Funding-Carry (Spot long, Perp short, Funding kassieren)
Tot, wenn eines gilt (Fenster 2019-09 bis 2024-12, BTC und ETH einzeln):
1. Nettorendite auf Kapital < 4 % p.a. (Hürde = grobe Schätzung risikofreier Zins plus Börsenrisiko-Aufschlag).
2. Mehr als 25 % der 30-Tage-Fenster mit negativer Nettorendite.
3. Max. Drawdown auf Kapital > 10 % ohne Börsenausfall-Szenario.
Zusätzlich wird ein Börsenausfall (Verlust von 50 % des Kapitals auf der Börse, einmal) gerechnet; er tötet nicht automatisch, muss aber im Bericht stehen.

## K2 Zwangsverkäufer-Reversal (kaufen nach Zwangsverkauf, halten 4 bzw. 8 Wochen)
Auslöser A (Funding): 7-Tage-Mittel des Fundings unter dem 5. Perzentil der eigenen letzten 365 Tage.
Auslöser B (Preis-Proxy, ohne Funding): 7-Tage-Rendite unter dem 5. Perzentil der eigenen letzten 365 Tage.
Ereignisse überlappen nicht (nach einem Auslöser 28 bzw. 56 Tage Sperre).
Tot, wenn eines gilt (je Coin und Haltedauer):
1. Weniger als 10 unabhängige Ereignisse (dann "nicht messbar", nicht "bestätigt").
2. Mittlere Überrendite gegenüber der unbedingten Rendite gleicher Haltedauer im selben Fenster ≤ 0, oder Bootstrap-p (Zufallszeitpunkte, 10 000 Ziehungen) > 0,05 einseitig.
3. Vorzeichen der Überrendite dreht zwischen erster und zweiter Hälfte des Fensters.

## K3 Überhitzungsfilter (Exposure halbieren, wenn Funding heiß)
Regel: Gewicht 0,5, wenn 7-Tage-Mittel des Fundings über dem 90. Perzentil der letzten 365 Tage liegt, sonst 1,0. Wöchentlich entschieden.
Tot, wenn: Timing-Wert (Rendite minus konstante Position mit gleicher mittlerer Gewichtung, nach Kosten) mit wöchentlichem t ≤ 2, oder in mehr als der Hälfte der Kalenderjahre negativ.

## K4 Kontrollarm: Trend plus Volatilitätssteuerung (keine Gegenpartei mit Zwang, dient als Messlatte)
Regel: Gewicht = 1, wenn Schluss über dem gleitenden Schnitt der Länge L, sonst 0; multipliziert mit min(1, Zielvol / realisierte 30-Tage-Vol). L wird jedes Jahr nur aus der Vergangenheit gewählt (Grid 50/100/150/200 Tage, bester Sharpe der Vorjahre), Zielvol = Median der bisherigen 30-Tage-Vol. Wöchentlich entschieden.
Urteil:
- "Edge": Sharpe und CAGR über Buy & Hold UND über 95 % von 1000 Zufalls-Timing-Läufen mit gleicher mittlerer Exposure, nach Kosten, Walk-Forward 2017 bis 2024, beide Coins.
- "Nur Risikomanagement": schlechterer Drawdown-bereinigter Wert (Calmar) als Buy & Hold verfehlt, oder nur Drawdown besser, aber nicht Zufalls-Timing.
- Sonst tot.

## Variantenzählung
K1: 2 Coins. K2: 2 Auslöser × 2 Haltedauern × 2 Coins = 8. K3: 2 Coins. K4: 2 Coins. Summe 14 Tests. Bonferroni-Schwelle für "bestätigt" über alle: p < 0,05/14 ≈ 0,0036.
