# Versuchs-Backlog

Reihenfolge = nächster zuerst. Jeder Eintrag ist eine einzige Änderung gegen den jeweiligen Champion. Wer einen Eintrag nimmt, setzt dahinter die Versuchs-ID; erledigte bleiben stehen (mit Urteil). Gepflegt vom Forschungs-Thread; neue Ideen dürfen alle unten anhängen. Jeder Versuchs-Thread trägt beim Start "E-NNN läuft" in seine Zeile ein und am Ende das Urteil dort und unter "Erledigt".

Leitbefund bisher: Die KI verliert durch Umschichten (Timing-Wert negativ), sie läuft dem Kurs hinterher (Gewicht ≈ Position in der 180-Tage-Spanne).

Umsortiert 2026-10-12 02:00: E-004 bis E-008 (Länge, Format, relativ) änderten nichts Messbares; in jeder Variante bleibt die KI Trendfolger am Spannen-Anker. Länge und Format sind nicht der Hebel. Deshalb kommen jetzt erst Prompt- und Rollen-Versuche (#9, #8, #20 bis #23, #19, #12), danach die Daten-Zeilen.

Umsortiert 2026-10-12 07:00 (Wächter review-002, B-16): Der Prüfstand erkennt nur große Effekte (ab etwa +0,5 %/Woche). Deshalb zuerst Umbauten der Methode (#25 Ensemble, #26 Veto-Rolle, #27 Stufen, #28 Trägheit), danach die Ein-Satz-Änderungen.

| # | Achse | Änderung | Warum / Hypothese | Versuch |
|---|---|---|---|---|
| 1 | prompt | Ruhe als Standard: "Ändere das Gewicht nur bei klarer Evidenz; jede Umschichtung kostet." | Umschichtung kostet ihn heute Geld; weniger Hin und Her sollte Timing-Wert Richtung 0 heben | E-002: kein messbarer Unterschied |
| 2 | prompt | Relativ statt absolut: "Du siehst 10 Märkte derselben Woche. Verteile mehr auf die stärksten, weniger auf die schwächsten." | Cross-Section ist oft leichter als Timing; Rank-IC heute ≈ 0 | E-004: schlechter |
| 3 | format | Renditen statt Preise: Tageszeilen als %-Änderung und Spanne statt o/h/l/c | Gleiche Information, weniger Zahlen, keine Ankerung auf "100" | E-005: kein messbarer Unterschied (A −0,35 %/Woche, t −1,3) |
| 4 | daten | Weniger: 60 statt 180 Tage | Zu viel Daten kann schaden; prüft, ob die lange Historie hilft | E-006: kein messbarer Unterschied (A −0,23 %/Woche vs E-003, t −1,4) |
| 5 | daten | Mehr: 365 statt 180 Tage | Gegenprobe zu 4 | E-007: kein messbarer Unterschied (A −0,04 %/Woche vs E-003, t −0,2) |
| 6 | format | Verdichtet: letzte 30 Tage täglich, davor Wochenkerzen | Lange Historie ohne lange Tabelle | E-008: kein messbarer Unterschied (A −0,12 %/Woche vs E-003, t −1,2) |
| 9 | prompt | Gegen den Strich: "Hohe Kurse nach starkem Anstieg sind kein Kaufgrund an sich" | Testet, ob das Trendfolgen der eigentliche Verlustbringer ist | E-009: kein messbarer Unterschied (A −0,08 %/Woche vs E-003, t −0,7) |
| 8 | prompt | Erst Regime benennen (Trend auf, Trend ab, seitwärts), dann Gewicht | Zwingt zu einem Zwischenschritt statt direkter Zuordnung Spanne → Gewicht | E-010: kein messbarer Unterschied (A −0,20 %/Woche vs E-003, t −0,6) |
| 24 | referenz | E-003 zweimal wiederholen (E-003-w2, E-003-w3); Referenz wird der Mittelwert der drei Läufe (E-003M) | Wächter: alle Versuche seit E-004 schlechter als E-003, also war der eine E-003-Lauf vermutlich Glück | erledigt: E-003M |
| 20 | prompt | Szenarien zuerst: je Fenster Wahrscheinlichkeit für hoch / seitwärts / runter in der nächsten Woche, Gewicht folgt daraus | Zwingt zu einer Prognose statt einer Lage-Beschreibung; macht Kalibrierung messbar | E-011: kein messbarer Unterschied (vs E-003M +0,05 %/Woche, t 0,26; ohne beste Woche −0,08 %). Wahrscheinlichkeiten ohne Aussagekraft (Brier 0,662 vs 0,667 gleichverteilt) |
| 21 | prompt | Rolle Risikomanager: Ziel kleinster Drawdown bei gleicher Rendite, nicht maximale Rendite | Fynns und Aarons Produktidee (ähnliche Rendite, kleinere Drawdowns) als Auftrag | E-012: kein messbarer Unterschied (vs E-003M +0,13 %/Woche, t 0,85; ohne beste Woche +0,01 %) |
| 25 | methode | Ensemble: Prompt E-003M, aber 3 unabhängige Läufe pro Woche, Entscheidung = mittleres Gewicht (`"ensemble": 3` in spec.json) | Wächter B-16: Läufe streuen so stark wie die Effekte; das zufällige Umschichten kostet nachweislich Geld. Kosten etwa 3 × 5,4 USD | |
| 26 | rolle | Veto statt Gewicht: eine feste Regel gibt das Signal (investiert, wenn Schluss über dem 50-Tage-Schnitt, sonst 0), die KI darf es nur auf 0 setzen oder bestätigen (`input: custom`, render.py zeigt die Regel und ihr heutiges Signal) | Wächter B-16: andere Rolle statt anderer Satz; prüft, ob die KI Fehlsignale einer Regel erkennt | |
| 27 | ausgabe | Grobe Stufen: Gewicht nur 0, 0,5 oder 1 | Wächter B-16 (Trägheit, ohne Gedächtnis): weniger kleine Umschichtungen | |
| 28 | ausgabe | Trägheit mit Gedächtnis: die KI sieht ihr Gewicht und ihren Kipp-Preis der Vorwoche und ändert nur, wenn der Kipp-Preis gebrochen ist | Wächter B-16; braucht erst Harness-Unterstützung (Wochen nacheinander entscheiden, Vorwoche als Eingabe), Harness bereit: `"memory": true` in spec.json; der Prompt muss das JSON als {"id": {"weight": w, "flip": Preis}} verlangen; Wochen laufen nacheinander (etwa 8 Minuten) | |
| 22 | prompt | Gegenrede: nach der Analyse je Fenster das stärkste Argument gegen die eigene Einschätzung, dann erst das Gewicht | Prüft, ob Selbstkritik das Hinterherlaufen bremst | |
| 23 | prompt | Feste Startregel (Gewicht 0,5), Abweichung nur mit benanntem Kippunkt, höchstens ±0,25 | Verbindet E-002 (Ruhe) mit der Pflicht-Analyse; begrenzt teure Umschichtung | |
| 19 | prompt | E-002 mit Analyse: Ruhe als Standard, Basis E-003 | Ohne Analyse weniger Streuung, aber kein Timing-Gewinn | |
| 12 | prompt | Kurzer Prompt: nur Aufgabe und Ausgabeformat, ohne Erklärungen | Prüft, ob die lange Anleitung hilft oder lenkt | |
| 7 | daten | Marktkontext: dasselbe Fenster des Gesamtmarkts (BTC, anonym) als zweite Tabelle | Altcoins hängen am Gesamtmarkt; relative Stärke | |
| 18 | daten | E-001 mit Analyse: plus 19 Indikatoren, Basis E-003 | Ohne Analyse kein Unterschied; mit Analyse kann die KI die Kennzahlen anders nutzen | |
| 10 | format | Nur Kennzahlen-Zeile (19 Indikatoren), keine Kerzentabelle | Viel weniger Zeichen; zeigt, ob die Rohkerzen überhaupt etwas beitragen | |
| 13 | daten | Volatilitäts-Zeile: realisierte Vola 7/30/90 Tage | Gewicht nach Risiko statt nach Richtung | |
| 11 | daten | Ohne Volumen | Weglassen-Test: trägt Volumen etwas bei? | |
| 16 | daten | Makro: M2-Veränderung (5 Wochen verzögert) als eine Zeile | Liquiditäts-These aus Fynns Liste | |
| 15 | daten | Open Interest und Funding (Perps, ab 2021 bzw. ab jetzt) | braucht erst Datenimport; Funding historisch nicht verfügbar | |
| 17 | format | Wochentag und Mondphase | geht nicht ohne Datumshinweis (Mond verrät Datum); erst klären, ob anonym möglich | |
| 14 | prompt | Ausgabe mit Begründung in einem Satz vor der Zahl | Denken vor der Zahl; prüft, ob das die Konsistenz ändert | überholt: Analyse vor den Gewichten ist seit E-003 Pflicht |

Erledigt:

| Versuch | Änderung | Urteil |
|---|---|---|
| E-000 | Referenz T-001 | Referenz |
| E-001 | T-002: plus 19 Indikatoren | kein messbarer Unterschied |
| E-002 | Ruhe als Standard (#1) | kein messbarer Unterschied (A +0,06 %/Woche, t 0,3) |
| E-003 | Analyse vor den Gewichten (T-001 + Strategie, Lage, Gewicht, Kippunkt je Fenster) | kein messbarer Unterschied (A +0,08 % t 1,0; B+C −0,26 % t −1,2); seit 2026-10-11 Champion, weil Pflicht (README §4a) |
| E-004 | Relativ statt absolut (#2), Basis E-003 | schlechter (A −0,49 %/Woche, t −2,2; Rank-IC 0,00): die KI verteilt nicht treffsicherer, verliert aber mehr |
| E-005 | Renditen statt Preise (#3), Basis E-003 | kein messbarer Unterschied (A −0,35 %/Woche vs E-003, t −1,3, ohne beste Woche −0,45 %); KI rechnet sich den Kursverlauf aus den Renditen zurück und bleibt Trendfolger |
| E-006 | Weniger: 60 statt 180 Tage (#4), Basis E-003 | kein messbarer Unterschied (A −0,23 %/Woche vs E-003, t −1,4, ohne beste Woche −0,28 %); Korrelation Gewicht zu 180-Tage-Spanne 0,61 statt 0,79, aber mehr Umschichtung (0,15 statt 0,12 je Woche); bleibt Trendfolger, jetzt mit Ausbruchs-Logik |
| E-007 | Mehr: 365 statt 180 Tage (#5), Basis E-003 | kein messbarer Unterschied (A −0,04 %/Woche vs E-003, t −0,2, ohne beste Woche −0,14 %); vorsichtiger (Exposure 0,37 statt 0,46), Anker an der Spanne noch stärker (Korrelation zur 180-Tage-Spanne 0,87 statt 0,79), Umschichtung 0,13 statt 0,12; sieht den Jahres-Abwärtstrend und bleibt Trendfolger. Mit E-006: Länge der Historie ändert nichts Messbares |
| E-008 | Verdichtet: letzte 30 Tage täglich, davor 21 Wochenkerzen (#6), Basis E-003 | kein messbarer Unterschied (A −0,12 %/Woche vs E-003, t −1,2, ohne beste Woche −0,16 %); Korrelation zur 180-Tage-Spanne 0,76 statt 0,79, Umschichtung 0,11 statt 0,12, Kosten 2,24 USD statt etwa 5; Strategie: Wochen-Abwärtstrend deckelt Gewicht bei 0,3, Tagesstruktur entscheidet darunter; bleibt Trendfolger. Gleiche Information in einem Viertel der Zeichen |
| E-009 | Gegen den Strich: "High prices after a strong rise are not a reason to buy in themselves." (#9), Basis E-003 | kein messbarer Unterschied (A −0,08 %/Woche vs E-003, t −0,7, ohne beste Woche −0,11 %; 8/13 Wochen besser); Rank-IC 0,11; Korrelation zur 180-Tage-Spanne 0,74 statt 0,79, Umschichtung 0,12 wie E-003, Exposure 0,43 statt 0,46; kappt Gewichte nach Spikes leicht (größte Abweichungen −0,25), nennt sich in der letzten Woche wieder selbst Trendfolger. Das Verbot allein löst den Anker nicht |
| E-010 | Erst Regime benennen (up, down, sideways), dann Gewicht (#8), Basis E-003 | kein messbarer Unterschied (A −0,20 %/Woche vs E-003, t −0,6, ohne beste Woche −0,33 %; 5/13 Wochen besser); Rank-IC 0,01; Regime 65× up, 37× seitwärts, 28× down, Gewicht folgt fast stufenweise dem Label (down 0,08, seitwärts 0,38, up 0,76 im Mittel); Korrelation zur 180-Tage-Spanne 0,81 statt 0,79, Umschichtung 0,18 statt 0,12 (36 Regimewechsel), Exposure 0,51 statt 0,46. Das Label ist nur eine Stufe derselben Spannen-Zuordnung und macht die Umschichtung teurer |
| E-003-w2, E-003-w3 → E-003M | E-003 zweimal wiederholt (Wächter), Referenz = Mittel der drei Läufe | Timing-Wert A: E-003 −0,15, w2 −0,26, w3 −0,32 %/Woche. Der erste Lauf war Glück; derselbe Prompt schwankt zwischen Läufen um 0,1 bis 0,17 %/Woche, so viel wie die gemessenen Effekte. Gegen E-003M: E-007 +0,05, E-009 +0,01 (beide t < 0,3), E-004 bleibt schlechter (t −2,4). Ab 2026-10-12 Champion und Referenz |
| E-011 | Szenarien zuerst: je Fenster Wahrscheinlichkeit hoch (>103) / seitwärts / runter (<97) am Tag +7, Gewicht folgt daraus (#20), Basis E-003M | kein messbarer Unterschied (A −0,19 %/Woche, vs E-003M +0,05 %, t 0,26, ohne beste Woche −0,08 %; 9/13 Wochen besser); Rank-IC 0,13; Exposure 0,50 statt 0,46, Umschichtung 0,14. Korrelation zur 180-Tage-Spanne nur 0,47 (bisher 0,74 bis 0,87): erster Versuch, der den Anker deutlich lockert, aber ohne Timing-Gewinn. Wahrscheinlichkeiten ohne Aussagekraft: Brier 0,662 vs 0,667 gleichverteilt, Korrelation (up − down) zur Folgewoche −0,07; die stärksten Aufwärts-Einschätzungen liefen am schlechtesten. Die Umrechnung in ein Gewicht erfindet die KI jede Woche neu (Details E-011/kalibrierung.md) |
| E-012 | Rolle Risikomanager: kleinster Drawdown bei etwa gleicher Rendite wie eine feste Position (#21), Basis E-003M | kein messbarer Unterschied (A −0,12 %/Woche, vs E-003M +0,13 %, t 0,85, ohne beste Woche +0,01 %; 9/13 Wochen besser); Rank-IC 0,01; Exposure 0,43 statt 0,46, Umschichtung 0,14. Korrelation zur 180-Tage-Spanne 0,63 statt 0,77 bis 0,79. Nur informativ: Rendite +18,8 % vs +18,7 %, Max Drawdown Portfolio −3,7 % vs −4,2 %, aber eine feste Position in gleicher mittlerer Höhe schafft +20,5 % bei −2,6 %. Die KI kappt nach steilen Spikes ("deep giveback"), die größten Kürzungen (SOL, DOT −0,35 am 13.09.) lagen vor Wochen mit +12 bis +14 % |
