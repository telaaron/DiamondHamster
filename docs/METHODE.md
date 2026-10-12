# Methode und Technik

Für alle, die genau wissen wollen, wie gemessen wird und wo was liegt. Die einfache Erklärung steht in der [README](../README.md).

## Wie wir messen (warum das hier nicht geschönt ist)

1. **Nur Daten nach dem Wissensstand des Modells zählen.** Das Modell kennt Kurse bis etwa Juni 2026. Ein Backtest auf 2021 misst Erinnerung, nicht Können. Gemessen wird deshalb nur ab Juli 2026 und vorwärts.
2. **Hauptmetrik: Timing-Wert.** Ergebnis der KI-Gewichte minus eine *konstante* Position in Höhe ihres eigenen Durchschnittsgewichts, nach Kosten (0,2 % pro Seite). Er beantwortet die eigentliche Frage: Bringt das Hin- und Herschieben überhaupt etwas? Konstant halten = 0.
3. **Zukunfts-Turnier ist der einzige Beweis.** Prompts werden mit Hash eingefroren und entscheiden jeden Sonntag auf 30 Coins über Wochen, die beim Einfrieren noch nicht passiert waren. "Nachgewiesen" heißt: Timing-Wert > 0 mit t > 2 über Turnier-Wochen. Alles darunter heißt "nicht nachgewiesen". Details: [tournament/README.md](../tournament/README.md).
4. **Spielplatz für schnelle Versuche.** Jeder Versuch ändert genau eine Sache (Prompt, Daten oder Format) gegen den aktuellen Champion, auf festen 13 Wochen (Jul bis Sep 2026) und 30 Coins. Ein Sieg dort ist nur ein Filter, kein Beweis: wer die Prompts schreibt, kennt diese Wochen.
5. **Jeder Versuch wird geloggt, auch die gescheiterten.** Die Zahl der getesteten Varianten gehört zum Ergebnis. Je mehr Varianten, desto eher ist die beste davon Glück.
6. **Holdout bleibt zu.** Regelbasierte Ideen werden auf Historie bis 2024 entwickelt; 2025-01 bis 2026-06 wird genau einmal am Ende geöffnet. Jeder Zugriff wird in `data/holdout_access.log` protokolliert.

Vollständige Regeln: [docs/PROTOKOLL.md](PROTOKOLL.md).

## Aufbau des Repos

| Ordner / Datei | Inhalt |
|---|---|
| `docs/PROTOKOLL.md` | Forschungsprotokoll: alle Regeln, Entscheidungen, Hypothesen-Register |
| `docs/VERSUCHE.md` | Versuche und Learnings in einfachen Worten |
| `prompts/` | Jeder Prompt als eigene Datei (`T-*` Trader, `R-*` Forscher, `ANALYST` zum Selbstnutzen). Ein Prompt mit geloggten Läufen wird nie geändert, nur kopiert. |
| `tournament/` | Zukunfts-Turnier: Coin-Universum, eingefrorene Prompts, Kerzen, Runden, Wertung |
| [`versuche/`](../versuche/UEBERSICHT.md) | Spielplatz: je Versuch Prompt, Bewertung und die Überlegung der KI; Übersicht und Backlog |
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

