# DiamondHamster

**Kann eine KI aus Marktdaten nachweislich bessere Krypto-Entscheidungen treffen als eine feste Position?**
Dieses Repo ist das offene Labor dazu. Wir suchen nicht die eine Strategie, sondern die *Methode*: welcher Prompt, welche Daten und welche Aufbereitung einer KI die besten Ergebnisse entlocken, gemessen so, dass man sich nicht selbst belügen kann.

> Labor statt Casino. Nur Forschung: kein Live-Trading, keine Exchange-Keys, keine Anlageberatung.

**Schnellzugriff:** [Aktueller Stand](#aktueller-stand) · [Versuche und Learnings](docs/VERSUCHE.md) · [Bester Prompt zum Selbst-Ausprobieren](prompts/ANALYST.md) · [Idee beitragen](CONTRIBUTING.md) · [Regeln](docs/PROTOKOLL.md)

---

## Worum es geht

- **Horizont:** Wochen bis Monate. Kein Daytrading, keine Orders.
- **Keine Kursprognosen, keine Kaufempfehlungen.** Jede Einschätzung ist bedingt ("solange X hält, dann Y") und nennt den Preis, an dem sie falsch wird. "Nichts tun" ist eine gültige Antwort.
- **Die KI als Trader:** Sie bekommt pro Woche und Coin ein anonymisiertes Kursfenster (keine Daten, keine Coin-Namen, Preise auf 100 normiert) und gibt ein Gewicht zwischen 0 (draußen) und 1 (voll investiert) zurück. Sie hat keine Werkzeuge, kein Internet, kein Gedächtnis.
- **Langfristiges Ziel:** ein Bot auf einer selbst erforschten Methode. Zuerst als Indikator, der einen zusätzlichen Hinweis gibt; selbstständig handeln erst viel später.

## Wie wir messen (warum das hier nicht geschönt ist)

1. **Nur Daten nach dem Wissensstand des Modells zählen.** Das Modell kennt Kurse bis etwa Juni 2026. Ein Backtest auf 2021 misst Erinnerung, nicht Können. Gemessen wird deshalb nur ab Juli 2026 und vorwärts.
2. **Hauptmetrik: Timing-Wert.** Ergebnis der KI-Gewichte minus eine *konstante* Position in Höhe ihres eigenen Durchschnittsgewichts, nach Kosten (0,2 % pro Seite). Er beantwortet die eigentliche Frage: Bringt das Hin- und Herschieben überhaupt etwas? Konstant halten = 0.
3. **Zukunfts-Turnier ist der einzige Beweis.** Prompts werden mit Hash eingefroren und entscheiden jeden Sonntag auf 30 Coins über Wochen, die beim Einfrieren noch nicht passiert waren. "Nachgewiesen" heißt: Timing-Wert > 0 mit t > 2 über Turnier-Wochen. Alles darunter heißt "nicht nachgewiesen". Details: [tournament/README.md](tournament/README.md).
4. **Spielplatz für schnelle Versuche.** Jeder Versuch ändert genau eine Sache (Prompt, Daten oder Format) gegen den aktuellen Champion, auf festen 13 Wochen (Jul bis Sep 2026) und 30 Coins. Ein Sieg dort ist nur ein Filter, kein Beweis: wer die Prompts schreibt, kennt diese Wochen.
5. **Jeder Versuch wird geloggt, auch die gescheiterten.** Die Zahl der getesteten Varianten gehört zum Ergebnis. Je mehr Varianten, desto eher ist die beste davon Glück.
6. **Holdout bleibt zu.** Regelbasierte Ideen werden auf Historie bis 2024 entwickelt; 2025-01 bis 2026-06 wird genau einmal am Ende geöffnet. Jeder Zugriff wird in `data/holdout_access.log` protokolliert.

Vollständige Regeln: [docs/PROTOKOLL.md](docs/PROTOKOLL.md).

## Aktueller Stand

*Stand: 2026-10-11.*

| | |
|---|---|
| **Ergebnis bisher** | Noch kein Prompt schlägt eine feste Position. Der Referenz-Prompt T-001 verliert durch sein Umschichten ca. 0,24 % pro Woche gegenüber "konstant halten". |
| **Dev-Champion** | E-000 = T-001 (nur 180 Tageskerzen, kurzer Prompt) |
| **Im Turnier** | T-001 seit Runde 2026-10-11, T-002 ab Runde 2026-10-18. Noch keine ausgewertete Turnierwoche. |
| **Getestete Varianten im Spielplatz** | 3 (E-001 bis E-003), alle "kein messbarer Unterschied" |
| **Neu ab E-003** | Die KI schreibt vor ihren Gewichten ihre Marktlesart, ihre Strategie und ihren Kipp-Preis auf. So sieht man, *warum* sie entscheidet. |
| **Läuft gerade** | Stündliche Versuche aus dem [Backlog](docs/VERSUCHE.md#was-als-nächstes-getestet-wird), wöchentliche Turnierrunde montags 00:23 UTC |

**Wichtigstes Learning bisher:** Die KI läuft dem Kurs hinterher. Ihr Gewicht entspricht fast nur der Lage im 180-Tage-Bereich (Korrelation 0,97): oben viel, unten wenig. Genau dieses Trendfolgen kostet sie gegenüber einer festen Position Geld. Mehr Indikatoren, "bleib ruhig" oder "denk erst laut nach" haben daran bisher nichts Messbares geändert.

Alle Versuche mit Zahlen und Begründung: **[docs/VERSUCHE.md](docs/VERSUCHE.md)**. Live-Tabelle mit jedem Prompt und dem Denken der KI: [versuche/UEBERSICHT.md](versuche/UEBERSICHT.md).

## Bester Prompt

Es gibt zwei Dinge, die man "bester Prompt" nennen kann. Beide stehen offen hier:

1. **Der gemessene Champion** ([prompts/T-001.md](prompts/T-001.md)): der Prompt, der im Spielplatz bisher nicht geschlagen wurde. Er gibt nur Zahlen aus und ist für die Messung gebaut, nicht für Menschen.
2. **Der Analyst-Prompt zum Selbst-Ausprobieren** ([prompts/ANALYST.md](prompts/ANALYST.md)): dieselbe Aufgabe, aber so formuliert, dass du ihn in Claude oder ChatGPT einfügen und mit eigenen Kerzendaten füttern kannst. Er zwingt die KI zu einer bedingten Einschätzung mit Kipp-Preis statt zu einer Prognose. Aufgebaut auf dem Format von E-003.

**Ehrlich dazu:** Kein Prompt hier hat bisher nachgewiesen, dass er eine feste Position schlägt. Der Analyst-Prompt hilft beim strukturierten Denken, er ist kein Signal.

## Mitmachen

Ideen sind ausdrücklich erwünscht: ein Prompt-Kniff, eine Datenquelle, ein Indikator, eine These über Marktzyklen, ein Fehler in unserer Methode.

- **Idee einreichen:** [neues Issue → "Idee für einen Versuch"](../../issues/new/choose)
- **Was mit Ideen passiert und was einen guten Vorschlag ausmacht:** [CONTRIBUTING.md](CONTRIBUTING.md)

Jede Idee wird gleich behandelt: als eine einzelne Änderung gegen den Champion, mit vorher festgelegtem Urteil. Auch eine widerlegte Idee landet im Log und ist ein Ergebnis.

## Aufbau des Repos

| Ordner / Datei | Inhalt |
|---|---|
| `docs/PROTOKOLL.md` | Forschungsprotokoll: alle Regeln, Entscheidungen, Hypothesen-Register |
| `docs/VERSUCHE.md` | Alle Versuche, Ergebnisse, Learnings, Backlog |
| `prompts/` | Jeder Prompt als eigene Datei (`T-*` Trader, `R-*` Forscher, `ANALYST` zum Selbstnutzen). Ein Prompt mit geloggten Läufen wird nie geändert, nur kopiert. |
| `tournament/` | Zukunfts-Turnier: Coin-Universum, eingefrorene Prompts, Kerzen, Runden, Wertung |
| `versuche/` | Spielplatz: je Versuch Prompt, Bewertung und die Überlegung der KI; Übersicht und Backlog |
| `experiments/` | Append-only Log aller Läufe (`log.csv`) mit gespeicherten KI-Antworten |
| `hypotheses/` | Vorlage für Hypothesen-Karten (vor dem Test ausgefüllt) |
| `src/diamondhamster/` | Code: Daten-Loader mit Holdout-Sperre, Backtest-Kern, Baselines, Indikatoren, KI-Harness, Turnier, Spielplatz |
| `.claude/agents/decider.md` | Der werkzeuglose Entscheider-Agent |
| `tests/` | Tests inkl. Lookahead- und Leak-Prüfungen |

## Selbst ausführen

```bash
pip install -e ".[dev]"
pytest -q
python -m diamondhamster baselines                       # Buy & Hold, DCA, Zufalls-Timing
PYTHONPATH=src python -m diamondhamster.tournament score # Turnier-Wertung
```

Die KI-Läufe brauchen die Claude-CLI (`claude -p` ohne Werkzeuge). Ablauf eines Versuchs: Protokoll §13.

## Wer

Aaron ([@telaaron](https://github.com/telaaron)) baut, Fynn ([@kryptofynn](https://x.com/kryptofynn)) bringt die Trading-Praxis und teilt die Reise auf X ("Botupdate #N"). Die Forschungsarbeit läuft mit Claude als Werkzeug.

---

*Keine Anlageberatung. Alle Zahlen sind Forschungsergebnisse auf kleinen Stichproben und können sich mit jeder Turnierwoche ändern.*
