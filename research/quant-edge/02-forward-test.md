# Forward-Test (Paper, kein Geld), vorab festgelegt 2026-10-16

Der einzige Holdout, der nicht verbrennt: Daten, die es heute noch nicht gibt. Regeln, Schwellen und Laufzeit stehen hier, bevor der erste Tag des Fensters existiert. Änderungen nur als datierter Nachtrag; ein Nachtrag nach Fensterbeginn macht den betroffenen Test zur Hypothese.

Alle Größen sind aus öffentlichen historischen Daten nachträglich exakt berechenbar (Binance-/Hyperliquid-Funding und Kerzen haben Historie). Es muss also nichts live mitgeschrieben werden; nicht nachträglich messbar ist nur echte Ausführungs-Slippage.

## F1 Funding-Carry (K1) bei heutiger Funding-Lage
- **Fenster:** 2026-10-17 00:00 UTC bis 2027-04-16 23:59 UTC (26 Wochen). Auswertung ab 2027-04-17.
- **Varianten (4):** BTC und ETH, Short-Bein auf Binance-USDT-Perp bzw. Hyperliquid-Perp, Spot-Bein Binance-Spot. Mechanik exakt wie `r2/q4_ev.py::carry_net` bzw. `r2/k1_hl_posthoc.py` (Kapital 1,5, Pflege, 0,2 % pro Seite und Bein, Ein- und Ausstieg gezählt). Für Hyperliquid werden bei der Auswertung echte HL-Perp-Kurse geladen.
- **Hürde:** Mittel der 3-Monats-T-Bill (FRED DTB3) im Fenster + 1 Prozentpunkt + erwarteter Ausfallverlust zentral 0,7 % p.a. (p 2,3 % × LGD 0,3, Q4).
- **Bestanden:** für BTC **und** ETH auf mindestens einer Börse Nettorendite p.a. über der Hürde und Max-DD > −5 %.
- **Nicht bestanden:** K1 gilt "bei aktueller Lage tot" und wird geparkt. Wiedervorlage nur, wenn das 30-Tage-Funding auf Binance > 10 % p.a. steigt (Zustand, keine Prognose).

## F2 Crash-Reversal 4 h (Hypothese H-Q5)
- **Regel exakt wie `r2/q5_intraday.py`, Familie price_only, aber L = 1:** Binance-USDT-Perp, 15-Minuten-Bar mit Rendite unter dem 0,2-%-Quantil der vorigen 2880 Bars → kaufen zum Open zwei Bars später (L = 1), 16 Bars halten. Entclustert wie dort. BTC und ETH.
- **Fenster:** ab 2026-10-17 00:00 UTC, bis je Coin 60 Ereignisse erreicht sind, längstens 2027-10-16. Schwellen-Vorlauf (30 Tage) darf aus 2026-09-17..10-16 kommen (Dev-Nachschau, kein Holdout).
- **Messung:** Überrendite brutto je Trade gegen alle Bars gleicher Haltedauer im Fenster, einseitiger t-Test über Ereignisse.
- **"Erntbar mit Taker-Kosten":** mittlere Brutto-Überrendite > 0,10 % (2 × 0,05 %) und t > 2, beide Coins.
- **"Erntbar mit Protokoll-Kosten":** > 0,40 % und t > 2, beide Coins.
- **Sonst tot.** Slippage in Crash-Bars ist nachträglich nicht messbar; ein Bestehen von "Taker" macht es zum Kandidaten für einen kleinen Echtgeld-Test mit gemessener Ausführung, nicht zum Cheatcode.

## Zählung
F1 4 + F2 2 = 6 Forward-Tests. Sie zählen in eine eigene Forward-Familie (Fenster nicht überlappend mit irgendeinem Dev-Test), Schwelle je Test wie oben, ohne Bonferroni über die Dev-Historie.
