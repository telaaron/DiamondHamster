# Versuche und Learnings

Chronologisch, inklusive aller Fehlschläge. Die Zahlen stammen aus `experiments/log.csv`, `docs/PROTOKOLL.md` §12 und den Versuchskarten des Spielplatzes. Alles hier sind **Entwicklungsdaten** (Jul bis Okt 2026). Beweiskraft hat nur das [Zukunfts-Turnier](../tournament/README.md).

*Stand: 2026-10-11.*

## Kurzfassung

| # | Datum | Was | Ergebnis | Urteil |
|---|---|---|---|---|
| T-001 | 10.10. | Nulllinien-Prompt: 180 Tageskerzen, ein Gewicht pro Woche (BTC, ETH) | BTC +12 % vs. Buy & Hold +36 %; schlägt nur 46 % (ETH 40 %) der Zufalls-Timings mit gleicher Exposure | kein Können gezeigt |
| T-001b | 11.10. | Dieselben Antworten gegen konstante Position in Höhe des KI-Durchschnitts | BTC: KI +12 % (Sharpe 2,1) vs. konstant +18 % (Sharpe 3,1). ETH: +19 % vs. +29 % | Umschichten kostet Rendite |
| H-002 | 11.10. | QS-Zyklen-Indikator (Quersummen-Tage seit Bärenmarkt-Tiefs, Pine-Script über Fynn) | Lift 1,18, p = 0,078 gegen alle 36⁴ Klassenpaare; 2023/24 Lift 0,98; als Filter senkt er die Sharpe einer einfachen Regel von 0,86 auf 0,60 | **verworfen** (in-sample, Holdout nicht geöffnet) |
| T-002 | 11.10. | T-001 plus eine Zeile mit 19 Indikatoren | zuerst scheinbar schlechter; Lauf hatte einen Leak (siehe unten) | ersetzt durch E-001 |
| E-000 | 11.10. | Referenz im Spielplatz: T-001 sauber neu gerechnet, 30 Coins | Timing-Wert −0,24 %/Woche (Set A), −0,30 % (B+C) | Referenz / Dev-Champion |
| E-001 | 11.10. | T-002 sauber: plus 19 Indikatoren | A +0,12 %/Woche vs. Referenz (t 1,7), ohne beste Woche +0,08 %; B+C −0,06 % | kein messbarer Unterschied |
| E-002 | 11.10. | "Ruhe als Standard": mittleres Gewicht halten, nur bei klarer Evidenz abweichen | A +0,06 % (t 0,3), ohne beste Woche −0,04 %; Streuung der Gewichte halbiert, die verbliebenen Bewegungen verlieren trotzdem | kein messbarer Unterschied |
| E-003 | 11.10. | "Sichtbares Denken": erst Strategie, dann pro Coin Lesart, Gewicht, Kipp-Preis, zuletzt JSON | A +0,08 % (t 1,0, 9 von 13 Wochen besser); B+C −0,26 % (t −1,2) | kein messbarer Unterschied; Format wird trotzdem Standard |

*Timing-Wert-Differenz = Versuch minus Referenz, gepaart über dieselben 13 Wochen und Coins. Set A = 10 große Coins (Filter), B+C = 20 weitere (Gegenprobe).*

## Learnings

1. **Die KI ist ein Trendfolger.** Ihr Gewicht entspricht fast nur der Lage im 180-Tage-Bereich (Korrelation 0,97 zwischen T-001 und T-002). Oben investiert, unten draußen. Das kostet gegenüber einer festen Position.
2. **Mehr Daten ≠ besser.** 19 Indikatoren zusätzlich haben das Verhalten kaum verändert. Die KI liest dieselbe Information schon aus den Kerzen.
3. **"Sei ruhig" macht ruhiger, aber nicht besser.** E-002 halbierte die Umschichtung, die restlichen Bewegungen waren aber genauso falsch getimt.
4. **Laut denken lassen verbessert nicht messbar, macht aber nachvollziehbar.** E-003 zeigt eine klare, sinnvoll klingende Swing-Logik (höhere Tiefs, Ausbruch über das letzte Zwischenhoch). Dass sie überzeugend klingt, heißt nicht, dass sie Geld bringt. Deshalb ist ab E-003 die schriftliche Überlegung Standard: Man sieht, *welche* Logik versagt.
5. **Leaks verstecken sich im Aufbau, nicht im Prompt.** Die ersten Dev-Läufe von T-001 und T-002 schickten aufeinanderfolgende Wochen desselben Coins im selben Batch: das spätere Fenster zeigte, was nach dem früheren passierte. Seitdem werden Batches pro Woche quer über Coins gebaut, und jedes Fenster wird vor dem Versand auf Jahreszahlen, Monatsnamen und Ticker geprüft.
6. **Eine Woche kann alles entscheiden.** Bei T-002 hing fast das ganze Ergebnis an einer Woche (16.08.). Deshalb wird jedes Ergebnis auch ohne die beste Woche berichtet.
7. **Zahlenmystik hält dem Test nicht stand.** Der QS-Indikator wirkte im Chart überzeugend, lag aber im Rauschen der zufällig gewählten Klassenpaare. Hauptrisiko war Auswahl nach Augenmaß.
8. **Kleine Stichprobe.** 13 Wochen sind sehr wenig. Für einen starken Effekt braucht es grob Jahre an Wochen; darum vorwärts im Turnier mit 30 Coins.

## Was als Nächstes getestet wird

Aus dem Backlog, je eine Änderung gegen den Champion:

1. **Relativ statt absolut:** "Du siehst 10 Märkte derselben Woche, verteile mehr auf die stärksten." Cross-Section ist oft leichter als Timing.
2. **Renditen statt Preise:** Tageszeilen als %-Änderung statt o/h/l/c auf 100.
3. **Weniger Daten:** 60 statt 180 Tage. Gegenprobe: 365 Tage.
4. **Verdichtet:** letzte 30 Tage täglich, davor Wochenkerzen.
5. **Marktkontext:** dasselbe Fenster für den Gesamtmarkt (BTC, anonym) daneben.
6. **Erst Regime benennen** (Trend auf, ab, seitwärts), dann Gewicht.
7. **Gegen den Strich:** "Hohe Kurse nach starkem Anstieg sind kein Kaufgrund an sich."
8. **Nur Kennzahlen,** keine Kerzentabelle.
9. Ohne Volumen; kurzer Prompt ohne Erklärungen; Volatilitäts-Zeile; Open Interest und Funding; M2 als Makro-Zeile.

Offene Hypothese **H-003** (Fynns Zeitstruktur: Wendepunkte bei Kurs und RSI ab dem Tief 2022-11-21, nach festen Regeln) wartet auf genaue Definitionen. Weil H-002 die QS-Tage schon getestet hat, liegt die Schwelle für jeden weiteren QS-Test höher.

Eigene Idee? → [CONTRIBUTING.md](../CONTRIBUTING.md)

## Wo die Rohdaten liegen

- `experiments/log.csv` und `experiments/runs/`: jede Anfrage und jede Antwort der KI aus den T-001/T-002-Läufen.
- `tournament/`: eingefrorene Prompts mit Hash, Kerzen, Runden, Wertung.
- Spielplatz-Versuche (E-NNN): Karten mit vollem Prompt, Diff zur Basis, Bewertung und der kompletten schriftlichen Überlegung der KI liegen im Projektordner unter `research/versuche/`. Sie werden noch nicht ins Repo gespiegelt.
