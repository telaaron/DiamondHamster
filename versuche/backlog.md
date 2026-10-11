# Versuchs-Backlog

Reihenfolge = nächster zuerst. Jeder Eintrag ist eine einzige Änderung gegen den jeweiligen Champion. Wer einen Eintrag nimmt, setzt dahinter die Versuchs-ID; erledigte bleiben stehen (mit Urteil). Gepflegt vom Forschungs-Thread; neue Ideen dürfen alle unten anhängen.

Leitbefund bisher: Die KI verliert durch Umschichten (Timing-Wert negativ), sie läuft dem Kurs hinterher (Gewicht ≈ Position in der 180-Tage-Spanne). Die ersten Versuche greifen genau das an.

| # | Achse | Änderung | Warum / Hypothese | Versuch |
|---|---|---|---|---|
| 1 | prompt | Ruhe als Standard: "Ändere das Gewicht nur bei klarer Evidenz; jede Umschichtung kostet." | Umschichtung kostet ihn heute Geld; weniger Hin und Her sollte Timing-Wert Richtung 0 heben | E-002: kein messbarer Unterschied |
| 2 | prompt | Relativ statt absolut: "Du siehst 10 Märkte derselben Woche. Verteile mehr auf die stärksten, weniger auf die schwächsten." | Cross-Section ist oft leichter als Timing; Rank-IC heute ≈ 0 | E-004 läuft |
| 3 | format | Renditen statt Preise: Tageszeilen als %-Änderung und Spanne statt o/h/l/c | Gleiche Information, weniger Zahlen, keine Ankerung auf "100" | |
| 4 | daten | Weniger: 60 statt 180 Tage | Zu viel Daten kann schaden; prüft, ob die lange Historie hilft | |
| 5 | daten | Mehr: 365 statt 180 Tage | Gegenprobe zu 4 | |
| 6 | format | Verdichtet: letzte 30 Tage täglich, davor Wochenkerzen | Lange Historie ohne lange Tabelle | |
| 7 | daten | Marktkontext: dasselbe Fenster des Gesamtmarkts (BTC, anonym) als zweite Tabelle | Altcoins hängen am Gesamtmarkt; relative Stärke | |
| 8 | prompt | Erst Regime benennen (Trend auf, Trend ab, seitwärts), dann Gewicht | Zwingt zu einem Zwischenschritt statt direkter Zuordnung Spanne → Gewicht | |
| 9 | prompt | Gegen den Strich: "Hohe Kurse nach starkem Anstieg sind kein Kaufgrund an sich" | Testet, ob das Trendfolgen der eigentliche Verlustbringer ist | |
| 10 | format | Nur Kennzahlen-Zeile (19 Indikatoren), keine Kerzentabelle | Viel weniger Zeichen; zeigt, ob die Rohkerzen überhaupt etwas beitragen | |
| 11 | daten | Ohne Volumen | Weglassen-Test: trägt Volumen etwas bei? | |
| 12 | prompt | Kurzer Prompt: nur Aufgabe und Ausgabeformat, ohne Erklärungen | Prüft, ob die lange Anleitung hilft oder lenkt | |
| 13 | daten | Volatilitäts-Zeile: realisierte Vola 7/30/90 Tage | Gewicht nach Risiko statt nach Richtung | |
| 14 | prompt | Ausgabe mit Begründung in einem Satz vor der Zahl | Denken vor der Zahl; prüft, ob das die Konsistenz ändert | überholt: Analyse vor den Gewichten ist seit E-003 Pflicht |
| 15 | daten | Open Interest und Funding (Perps, ab 2021 bzw. ab jetzt) | braucht erst Datenimport; Funding historisch nicht verfügbar | |
| 16 | daten | Makro: M2-Veränderung (5 Wochen verzögert) als eine Zeile | Liquiditäts-These aus Fynns Liste | |
| 17 | format | Wochentag und Mondphase | geht nicht ohne Datumshinweis (Mond verrät Datum); erst klären, ob anonym möglich | |
| 18 | daten | E-001 mit Analyse: plus 19 Indikatoren, Basis E-003 | Ohne Analyse kein Unterschied; mit Analyse kann die KI die Kennzahlen anders nutzen | |
| 19 | prompt | E-002 mit Analyse: Ruhe als Standard, Basis E-003 | Ohne Analyse weniger Streuung, aber kein Timing-Gewinn | |

Erledigt:

| Versuch | Änderung | Urteil |
|---|---|---|
| E-000 | Referenz T-001 | Referenz |
| E-001 | T-002: plus 19 Indikatoren | kein messbarer Unterschied |
| E-002 | Ruhe als Standard (#1) | kein messbarer Unterschied (A +0,06 %/Woche, t 0,3) |
| E-003 | Analyse vor den Gewichten (T-001 + Strategie, Lage, Gewicht, Kippunkt je Fenster) | kein messbarer Unterschied (A +0,08 % t 1,0; B+C −0,26 % t −1,2); seit 2026-10-11 Champion, weil Pflicht (README §4a) |
