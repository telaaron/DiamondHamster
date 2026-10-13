# Versuche und Learnings

Was wir ausprobiert haben und was dabei rauskam, in einfachen Worten. Auch alles, was nicht funktioniert hat.

*Stand: 12. Oktober 2026. Die genauen Zahlen zu jedem Versuch stehen in der [Tabelle aller Versuche](../versuche/UEBERSICHT.md).*

## Die Messlatte

Jeder Versuch muss gegen dasselbe antreten: **eine feste Menge liegen lassen.** Wer jede Woche umschichtet, zahlt Gebühren und muss richtig liegen, sonst verliert er gegen das Liegenlassen.

Bisher liegt die KI **leicht darunter**: Ihr Hin und Her kostet sie etwa 0,2 bis 0,3 % pro Woche gegenüber dem Liegenlassen.

## Was wir gelernt haben

**1. Die KI läuft dem Kurs hinterher.**
Ist ein Coin nahe seinem Hoch, investiert sie viel. Ist er nahe am Tief, wenig. Damit kauft sie spät und verkauft spät. Das ist der Hauptgrund, warum sie verliert.

**2. Mehr Daten machen sie nicht schlauer.**
19 zusätzliche Indikatoren (RSI, MACD, Bollinger und Co.): kein Unterschied. Weniger Historie (60 statt 180 Tage) oder mehr (365 Tage): auch keiner. Die KI liest offenbar schon alles Wichtige aus den Kursen selbst.

**3. Gut gemeinte Anweisungen wirken nicht.**
"Bleib ruhig und schichte wenig um": Sie schichtet weniger um, aber die übrigen Wechsel sind genauso schlecht getimt. "Hohe Kurse sind kein Kaufgrund": kein Unterschied. "Benenne erst den Trend": kein Unterschied.

**4. Coins miteinander vergleichen macht es schlechter.**
Als die KI die stärksten Coins höher gewichten sollte, wurde das Ergebnis messbar schlechter. Das ist bisher der einzige klare Effekt, leider der falsche.

**5. Die KI denken zu lassen, macht sie nicht besser, aber durchschaubar.**
Seit Versuch E-003 schreibt die KI erst auf, wie sie den Markt liest und ab welchem Preis sie ihre Meinung ändert. Ihre Begründungen klingen überzeugend (Hochs, Tiefs, Ausbrüche). Gute Begründungen heißen aber nicht gute Ergebnisse.

**6. Der Zufall ist groß.**
Wir haben denselben Versuch dreimal laufen lassen. Die Ergebnisse unterschieden sich so stark wie die Effekte, die wir messen wollten. Darum vergleichen wir jetzt gegen den Durchschnitt aus drei Läufen.

**7. Zahlenmystik hält dem Test nicht stand.**
Ein Indikator, der Wendepunkte über Quersummen von Tagen vorhersagen soll (der "QS-Zyklen-Indikator"), wirkte im Chart überzeugend. Im Test auf BTC von 2011 bis 2024 lag er im Bereich des Zufalls. Verworfen.

**8. Fehler verstecken sich im Aufbau.**
In den ersten Tests konnte die KI versehentlich sehen, wie es nach einer Woche weiterging. Das haben wir gefunden, behoben und alles neu gerechnet. Seitdem prüft der Code jedes Datenpaket, bevor die KI es sieht.

## Alle Versuche auf einen Blick

| Versuch | Was wurde geändert? | Ergebnis |
|---|---|---|
| T-001 / E-000 | Ausgangspunkt: nur Kurse der letzten 180 Tage | etwas schlechter als Liegenlassen |
| T-002 / E-001 | plus 19 Indikatoren | kein Unterschied |
| E-002 | "Bleib ruhig, schichte wenig um" | kein Unterschied |
| E-003 | KI schreibt erst ihre Überlegung auf | kein Unterschied, aber ab jetzt Standard |
| E-003 Wdh. 2 + 3 | derselbe Versuch nochmal | zeigt, wie groß der Zufall ist |
| E-004 | Coins untereinander vergleichen | **schlechter** |
| E-005 | Prozent-Änderungen statt Preise | kein Unterschied |
| E-006 | nur 60 Tage Historie | kein Unterschied |
| E-007 | 365 Tage Historie | kein Unterschied |
| E-008 | letzte 30 Tage täglich, davor wöchentlich | kein Unterschied |
| E-009 | "Hohe Kurse sind kein Kaufgrund" | kein Unterschied |
| E-010 | erst Trend benennen, dann entscheiden | kein Unterschied |
| E-011 | erst Wahrscheinlichkeiten für hoch, seitwärts, runter | kein Unterschied |
| E-012 | KI als Risikomanager: Verluste klein halten statt Rendite jagen | läuft |
| H-002 | QS-Zyklen-Indikator (ohne KI) | verworfen |

"Kein Unterschied" heißt: Der Versuch war mal etwas besser, mal etwas schlechter, aber nicht klar genug, um es vom Zufall zu unterscheiden.

## Wie es weitergeht

- **Das Turnier läuft seit dem 11. Oktober.** Jede Woche müssen die eingefrorenen Anleitungen gegen echte, neue Kurse antreten. Nach einigen Wochen gibt es erste belastbare Zahlen.
- **Weitere Versuche** stehen in der [Warteschlange](../versuche/backlog.md), zum Beispiel: den Gesamtmarkt als Vergleich mitgeben, Funding und Open Interest, Geldmenge (M2).
- **Fynns Zeitstruktur-Idee** (Wendepunkte bei Kurs und RSI seit dem Tief im November 2022) wird getestet, sobald die Regeln genau festgelegt sind.

Eigene Idee? 👉 [Idee einreichen](../CONTRIBUTING.md)
