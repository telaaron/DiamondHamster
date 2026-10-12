# Forschungsprotokoll: eigene Trading-Methode

Stand: 2026-10-11 · Scope: nur Research, kein Live-Trading, keine Exchange-Keys · Assets: BTC, ETH (bis Aaron anderes sagt) · Horizont: Wochen bis Monate

## 1. Was "nicht auf Sand" konkret heißt

Die meisten selbstgebauten Strategien scheitern nicht an der Idee, sondern am Prozess: man testet 200 Varianten, nimmt die beste, und die "Edge" war Zufall. Fundament = ein Prozess, der genau das verhindert.

Regeln, die ab Tag 1 gelten:

1. **Holdout wird eingefroren.** Daten ab 2025-01-01 bis 2026-06-30 (siehe Abschnitt 11) werden nicht angeschaut, nicht geplottet, nicht getestet. Einmaliger Test am Ende einer Methode. Wer einmal reinschaut, hat ihn verbrannt.
2. **Jeder Versuch wird geloggt, auch die gescheiterten.** Die Anzahl der Versuche ist Teil des Ergebnisses (Multiple-Testing-Korrektur, z. B. Deflated Sharpe Ratio). Ohne Log ist kein Ergebnis bewertbar.
3. **Hypothese vor Test.** Erst aufschreiben: Was erwarte ich, warum (Mechanismus), was würde es widerlegen. Dann testen. Nachträgliche Story-Erfindung zählt nicht.
4. **Immer gegen Baselines.** Buy & Hold, monatlicher DCA, zufälliges Timing mit gleicher Exposure. Eine Methode muss diese *nach Kosten* schlagen, sonst ist sie keine.
5. **Kosten und Realismus von Anfang an.** Gebühren + Slippage (konservativ 0,2 % pro Seite), Signal an Tag t, Ausführung frühestens Open t+1. Kein Lookahead.
6. **Regime-Abdeckung.** Ergebnis muss in Bull (2017, 2020/21), Bear (2018, 2022) und Seitwärts (2019, 2023 H1) einzeln betrachtet werden. Funktioniert nur in einem Regime = Regime-Wette, keine Methode.
7. **Einfach vor komplex.** Wenige Parameter. Jeder Parameter mehr = mehr Möglichkeiten, Rauschen zu fitten.

## 2. Ehrliche Einschränkung (wichtig)

Bei einem Horizont von Wochen bis Monaten gibt es wenig unabhängige Datenpunkte. BTC hat seit ~2013 brauchbare Daten, ETH seit 2015/2017. Das sind grob 130 bis 160 nicht-überlappende Monate. Daraus folgt:

- Statistische Signifikanz ist schwer zu erreichen. Eine Methode mit 20 Trades in 10 Jahren ist fast nicht von Glück unterscheidbar.
- Gegenmittel: Methode auf mehreren Assets testen (BTC, ETH, ggf. weitere Majors) und Robustheit über Parameter-Nachbarschaften prüfen statt eines Optimums.
- Annahme, die wir machen: dass Muster aus 2013 bis 2024 überhaupt noch gelten. Der Markt hat sich strukturell verändert (ETFs, Institutionelle, Derivate-Volumen). Das ist ein Bias-Risiko, das wir nur durch Forward-Testing auflösen.

"Neue Methode" heißt realistisch: eine eigene, verstandene Kombination aus Beobachtungen mit klarem Mechanismus, die den Prozess oben überlebt. Nicht ein Indikator, den noch nie jemand gesehen hat.

## 3. Pipeline einer Idee

| Stufe | Was | Abbruchkriterium |
|---|---|---|
| 0 Beobachtung | Aaron oder Daten zeigen ein Muster | keins, nur notieren |
| 1 Hypothese | Karte ausfüllen (siehe 5) | kein plausibler Mechanismus |
| 2 In-Sample-Test | 2013/2017 bis 2022-12 | schlägt Baselines nach Kosten nicht |
| 3 Walk-Forward | rollierend, Parameter nur aus Vergangenheit | bricht außerhalb des Fit-Fensters ein |
| 4 Validierung | 2023-01 bis 2024-12 | Performance-Kollaps vs. In-Sample |
| 5 Holdout | 2025-01 bis 2026-06, **einmal** | verfehlt vorab definierte Schwelle |
| 6 Paper-Forward | live mitlaufen, ohne Geld, min. 3 bis 6 Monate | weicht deutlich vom Backtest ab |
| 7 Bot | erst danach | |

Die Erfolgsschwelle für Stufe 5 wird festgelegt, *bevor* Stufe 5 läuft.

## 4. Daten-Fundament

- Tageskerzen (OHLCV) BTC, ETH. Primär Binance Spot (ab 2017-08), für längere BTC-Historie zusätzlich Bitstamp/Coinbase (ab 2014/2015).
- Später, nur wenn eine Hypothese es braucht: Funding Rates, Open Interest, On-Chain (z. B. aktive Adressen, Exchange-Flows), Makro (DXY, Zinsen).
- Daten werden einmal gezogen, mit Hash versioniert, nie still überschrieben. Datenqualität prüfen: Lücken, Duplikate, Ausreißer, Börsen-Abweichungen.

**Blocker aktuell:** Der Cloud-Container erreicht keine Börsen-APIs (Binance, Coinbase, Kraken, CoinGecko geben Netzwerk-Policy-Ablehnung). GitHub und PyPI gehen.

## 5. Hypothesen-Karte (Vorlage)

```
ID: H-001
Datum:
Beobachtung: was habe ich gesehen?
Hypothese: wenn X, dann über Y Wochen Z (Richtung + Größenordnung)
Mechanismus: warum sollte das so sein? wer ist auf der anderen Seite?
Test: Daten, Zeitraum (nur In-Sample), Metrik
Widerlegt wenn: konkrete Schwelle
Parameter: Liste, mit vorab festgelegten Bereichen
Ergebnis: (erst nach Test)
Anzahl Varianten getestet:
Entscheidung: verwerfen / weiter zu Stufe N
```

## 6. Experiment-Log

Jede Ausführung eine Zeile, append-only: Datum, Hypothesen-ID, Code-Commit, Parameter, Zeitraum, Metriken (CAGR, Max Drawdown, Sharpe, Anzahl Trades, Exposure), Baseline-Vergleich, Notiz.

## 7. Erster konkreter Schritt

**Datenfundament + Baselines.** Bevor irgendeine eigene Idee getestet wird:

1. Saubere Tagesdaten BTC/ETH ziehen und versionieren, Qualitätsreport.
2. Holdout-Grenze im Code erzwingen (Loader gibt Daten ab 2025-01-01 nur mit explizitem Flag heraus).
3. Baselines berechnen: Buy & Hold, DCA, Random-Timing (1000 Läufe) inkl. Drawdowns pro Regime. Das ist die Latte, die jede Methode überspringen muss.

Parallel (Aarons Teil): 3 bis 5 eigene Beobachtungen als Hypothesen-Karten aufschreiben. Die Methode soll aus deinen Ideen kommen, nicht aus meinen.

Tech: Python, pandas, kein Backtest-Framework am Anfang (eigener, kleiner, vollständig verstandener Kern; Frameworks verstecken Lookahead- und Kostenannahmen).

## 8. Neues Ziel (2026-10-10): bester KI-Ansatz statt beste Strategie

Aaron: Wir suchen nicht die beste Strategie, sondern den Ansatz (praktisch: den Prompt), mit dem eine KI aus den Daten nachweislich die besten Ergebnisse holt.

### Was gleich bleibt
Backtest-Kern, Baselines, Kosten, Experiment-Log. Die KI wird nur eine neue Quelle für Positionen (`weights`), bewertet wird exakt gleich.

### Drei Probleme, die vorher gelöst sein müssen

1. **Das Modell kennt die Geschichte.** Ein LLM wurde auf Texten trainiert, die den BTC-Kurs bis zu seinem Trainings-Cutoff beschreiben. Es "weiß", dass Ende 2017 ein Top war und 2022 ein Bärenmarkt. Ein Backtest auf diesen Jahren misst Erinnerung, nicht Können. Anonymisieren (keine Daten, keine Asset-Namen, normierte Preise) hilft teilweise, aber markante Verläufe (2017-Blase, März-2020-Crash) bleiben erkennbar.
   Folge: Ehrlich messbar ist ein LLM-Trader nur auf Daten **nach** dem Trainings-Cutoff des Modells und live im Forward-Test. Unser Holdout 2025 liegt vor dem Cutoff aktueller Modelle und ist für diesen Zweck wertlos.

2. **Prompt-Suche ist Overfitting mit unendlich vielen Parametern.** Jede Prompt-Variante ist ein Versuch. 50 Prompts testen und den besten nehmen ist dasselbe wie 50 Parameter testen. Versuchszählung und Holdout werden wichtiger, nicht unwichtiger.

3. **Nicht-Determinismus, Modellwechsel, Kosten.** Gleicher Prompt, gleiche Daten, andere Antwort. Jeder Prompt braucht mehrere Läufe. Ergebnisse gelten nur für eine gepinnte Modell-Version. Wöchentliche Entscheidungen über 8 Jahre sind ca. 400 Calls pro Lauf.

### Zwei Rollen für die KI

| | KI als Forscher | KI als Trader |
|---|---|---|
| Was der Prompt tut | schlägt Hypothesen + Code vor, Pipeline testet deterministisch | entscheidet direkt Long/Flat aus einem Datenfenster |
| Leak-Risiko | geringer (Ideen können historisch geprägt sein, Test ist sauberer Code) | hoch auf allen Daten vor Cutoff |
| Messbar auf | Historie mit Walk-Forward | nur Daten nach Cutoff + live |
| Zeit bis Aussage | Tage bis Wochen | Monate |
| Metrik für "bester Prompt" | Anteil Hypothesen, die Stufe 4 überleben, und deren Out-of-Sample-Güte | Out-of-Sample-Rendite vs. Baselines nach Kosten |

### Code-Erweiterungen (nach Entscheidung)
- `prompts/` versioniert, jeder Prompt hat eine ID; Log speichert Prompt-ID + Modell-ID
- Response-Cache (Hash aus Prompt, Input, Modell) für Reproduzierbarkeit und Kosten
- Point-in-time-Fenster: KI sieht an Tag t nur Daten bis Close t (gleicher Vertrag wie Backtest)
- Anonymisierungs-Schicht
- Bewertung über N Wiederholungen pro Prompt, Ergebnis als Verteilung

## 9. Intelligenz-Schicht = Subagents im Projekt, keine API (Aaron, 2026-10-10)

### Was sich ändert
- **Austausch über Dateien statt Funktionsaufruf.** Python schreibt `requests.json` (Prompt + anonymisierte Fenster mit zufälligen IDs, gemischte Reihenfolge), die Session verteilt sie an Subagents, die Antworten landen in `responses.json`. Die Zuordnung ID → Datum liegt in `key.json`, das kein Subagent sieht. Code: `ai.export_requests` / `ai.load_responses`.
- **Modell nicht pinbar.** Es antwortet das Modell, das die Session gerade bedient; das kann wechseln. Jeder Lauf protokolliert das bediente Modell. Ergebnisse verschiedener Modelle werden nicht gemischt.
- **Kein Temperatur-Regler, keine Seeds.** Streuung messen wir nur über Wiederholungen: jeder Prompt mindestens 5 unabhängige Läufe, Ergebnis als Verteilung.
- **Cache = einziges Replay.** Antworten werden committet. Ein Lauf ist reproduzierbar, weil seine Antworten gespeichert sind, nicht weil man ihn neu erzeugen kann.
- **Durchsatz statt Kosten ist der Engpass.** 400 Wochenentscheidungen × 5 Läufe × N Prompts sind tausende Entscheidungen. Deshalb Batches: ein Subagent bekommt viele gemischte Fenster auf einmal. Risiko: er vergleicht Fenster untereinander. Gegenmittel: Fenster einzeln anonymisiert, Reihenfolge zufällig, Batchgröße als Parameter protokolliert.
- **Subagents haben Werkzeuge.** Ein Subagent mit Datei- oder Webzugriff könnte Holdout-Daten oder echte Kurse nachschlagen. Für Entscheidungen bekommt er deshalb nur den Request-Inhalt im Prompt und keinen Repo-Zugriff; das muss technisch abgesichert werden (eigener Agent-Typ ohne Tools), bevor Ergebnisse zählen.
- **Trainings-Cutoff.** Das aktuelle Modell hat Wissen bis ca. Juni 2026. Sauber messbar als Trader sind damit nur Juli 2026 bis heute (ca. 3 Monate) plus Live-Forward. Der Live-Teil passt gut zu einer wöchentlichen Routine in diesem Projekt, die jeden Sonntag eine Entscheidung trifft und loggt.

## 10. Beide Rollen (Aaron, 2026-10-10)

- **Trader:** Prompts `prompts/T-*.md`, entschieden vom Subagent-Typ `decider` (`.claude/agents/decider.md`, alle Werkzeuge gesperrt). Bewertung nur auf Daten nach Modell-Cutoff (ab 2026-07) und live über eine wöchentliche Routine. Bis dahin dienen historische Läufe nur zum Debuggen, nicht zur Auswahl.
- **Forscher:** Prompts `prompts/R-*.md`. Ein Subagent liefert Hypothesen-Karte + `weights`-Funktion, die Pipeline testet. Güte eines Forscher-Prompts = Anteil seiner Hypothesen, die Stufe 4 (Validierung 2023/24) überleben, über mindestens 10 Hypothesen pro Prompt.
- **Offen:** Ob der `decider` wirklich keine Werkzeuge hat, wird vor dem ersten zählenden Lauf empirisch geprüft.

## 11. Zukunfts-Turnier ist die Messgrundlage (Aaron, 2026-10-11)

Grundlage: Review 001 des Methodik-Wächters (research/methodik/review-001-2026-10-11.md), Befunde B-01 bis B-07. Aaron hat am 2026-10-11 entschieden: das Turnier gilt, bevor T-002 gebaut wird.

### Trader-Prompts zählen nur noch im Turnier
- Ein Prompt wird mit ID, Hash und Datum eingefroren (`tournament/prompts.json`). Er zählt nur auf Runden **nach** seinem Einfrier-Datum. Text ändern = neue ID.
- Jeden Sonntag (Close, UTC) entscheiden alle aktiven Prompts auf denselben 30 Coins (`tournament/universe.json`), 3 Wiederholungen, frische Claude-Läufe ohne Werkzeuge. Höchstens 4 Prompts gleichzeitig aktiv. Ein neuer Prompt beantwortet eine benannte Frage (z. B. "helfen Indikatoren?").
- Juli bis Oktober 2026 sind ab jetzt Entwicklungsdaten. Ergebnisse dort zählen nicht als Beweis.
- Erste Runde: Sonntag 2026-10-11 (Routine montags 00:23 UTC), T-001 (eingefroren 2026-10-11 vor dem Close) als Nulllinie. Neue Prompts steigen ab 2026-10-18 ein.

### Hauptmetrik: Timing-Wert
- Timing-Wert = Ergebnis der KI-Gewichte minus konstante Position in Höhe ihrer mittleren Gewichtung pro Coin, nach Kosten (0,2 % pro Seite), pro Woche über alle Coins gemittelt.
- t-Statistik über Wochen (nicht über Coins, weil Coins gemeinsam laufen).
- "Nachgewiesen" = Timing-Wert > 0 mit t > 2 auf Turnier-Wochen. Alles darunter heißt "nicht nachgewiesen".
- Nebenwerte: Rank-IC (gewichtet die KI die besseren Coins höher? Das ist Auswahl, nicht Timing), Abstand zu Buy & Hold, Drawdown.

### Zwei Wege für Hypothesen
- **Menschliche Regel-Hypothesen** (Aaron, Fynn): Pipeline aus Abschnitt 3 bleibt. Holdout für sie ist **2025-01-01 bis 2026-06-30**, einmal. Ab 2026-07 sind die Kurse allen bekannt; dort zählt nur noch der Forward-Test. Zusatzfrage pro Idee: ist sie aus Beobachtungen von 2025 oder später entstanden? Dann ist auch dieser Holdout für sie nicht sauber.
- **KI-Hypothesen** (Forscher-Rolle, R-*): das Modell kennt 2023 bis Mitte 2026. Validierung und Holdout prüfen dort nur sein Gedächtnis. KI-Hypothesen zählen deshalb nur auf Zukunftswochen, im Turnier.

### Abbruchregel (offen)
Die Zahlen legen Aaron und Fynn fest. Vorschlag des Wächters: Zeigt nach 26 Turnier-Wochen auf mindestens 20 Coins kein eingefrorener Prompt einen Timing-Wert mit t > 1, bekommt die KI eine andere Rolle (Forscher oder Filter) statt weiterem Prompt-Tuning.

### Kommunikation
Posts nennen nur die Hauptmetrik mit Zahl der Wochen und Entscheidungen.

## 12. Hypothesen-Register

| ID | Datum | Idee | Stand | Nachweis |
|---|---|---|---|---|
| T-001 | 2026-10-10 | Nulllinien-Trader-Prompt, nur Kerzen | eingefroren 2026-10-11, läuft im Turnier | experiments/log.csv, tournament/prompts.json |
| H-002 | 2026-10-11 | QS-Klassen je Zyklus (Pine-Script über Fynn, Anker 2011-11-17, 2015-08-18, 2018-12-15, 2022-11-21; Klassenpaare 4/6, 6/3, 3/5, 5/9) | **verworfen** in-sample: Swing-Wenden k=14 Lift 1,18, p = 0,078 gegen alle 36^4 Klassenpaare; 2023/24 Lift 0,98; QS-Filter senkt Sharpe einer einfachen Einstiegsregel von 0,86 auf 0,60. 7 Läufe geloggt, Holdout nicht geöffnet | research/qs-indikator/H-002-qs-zyklen.md, PR #3 |
| T-002 | 2026-10-11 | T-001 plus 19 Indikatoren (einzige Änderung) | Dev-Fenster Jul bis Okt 2026: Timing-Wert −0,30 %/Woche gegen −0,10 % bei T-001, in allen 3 Wiederholungen schlechter; vorsichtiger (Exposure 0,45 statt 0,56); beide folgen fast nur der Lage im 180-Tage-Bereich (Korrelation 0,97); eine Woche (16.08.) entscheidet fast alles. Kein Beweis (Dev-Daten). **Nachtrag 2026-10-11:** dieser Dev-Lauf (wie der von T-001) hatte einen Überlappungs-Leak: ein Batch enthielt aufeinanderfolgende Wochen eines Coins, spätere Fenster zeigten die Zukunft früherer. Sauber wiederholt als E-001 auf 30 Coins: kein messbarer Unterschied (A +0,12 %/Woche t 1,7; B+C −0,06 %) | experiments/log.csv, experiments/runs/T-002_*, research/versuche/E-001 |
| H-003 | 2026-10-11 | Fynns Zeitstruktur: Wendepunkte und Impulse bei Kurs und RSI ab 2022-11-21 nach festen Regeln, erst ohne QS-Tage, dann Häufung auf QS9/QS5-Tagen, zyklusspezifische RSI-Längen | wartet auf Fynns Definitionen (QS9/QS5, RSI-Länge je Zyklus, Wendepunkt-Regel) | Thread "Forschung neu gestartet" |

Zu H-003: H-002 hat die QS-Tage bereits einmal getestet. Jeder weitere QS-Test zählt als zusätzliche Variante derselben Ideenfamilie. Die Schwelle für H-003 liegt deshalb höher (Bonferroni über alle QS-Varianten), und eine Definition, die erst nach Sicht auf das H-002-Ergebnis gewählt wird, ist zu markieren.

## 13. Stündliche Versuche (Aaron, 2026-10-11 20:05)

Die Methode ist Prompt + Daten + Aufbereitung. Sie wird laufend in Einzelversuchen verbessert, je Versuch eine Änderung gegen den Dev-Champion, auf einem festen Prüfstand (13 Sonntage Jul bis Sep 2026, 30 Coins in Set A und Check-Sets B+C, gepaarte Bewertung über den Timing-Wert, Ergebnis auch ohne die beste Woche). Regeln, Ablauf und Anti-Schummel-Regeln: research/versuche/README.md. Übersicht mit Zähler aller getesteten Varianten: research/versuche/UEBERSICHT.md.

- Ein Dev-Sieg ist ein Filter, kein Nachweis. Nachweis bleibt allein das Turnier (§11).
- Höchstens ein neuer Prompt pro Woche wird ins Turnier eingefroren (samstags), und nur ein Dev-Champion, der den besten aktiven Turnier-Prompt auf A und B+C schlägt.
- Ein Versuch läuft genau einmal; Wiederholungen bekommen eine neue ID und zählen als weitere Variante.
- Batches werden pro Entscheidungswoche quer über Coins gebaut (Überlappungs-Leak, siehe §12 T-002).
- Ab E-003 schreibt der Decider vor seinen Gewichten seine Überlegung auf (Aaron, 2026-10-11 20:42). Die volle Antwort wird gespeichert und gezeigt. E-003 (T-001 plus Überlegung) wird danach Referenz und Champion, weil sich das Entscheidungsverhalten damit ändert (README §4a).
- Seit 2026-10-12 (Wächter B-12): ein neuer Dev-Champion muss zusätzlich die feste Referenz E-003 schlagen; ins Turnier nur mit t ≥ 2 auch auf B+C.
- Seit 2026-10-12 04:30: Referenz und Champion ist E-003M, das Mittel aus drei Läufen des E-003-Prompts. Der erste Lauf war zu gut (Timing-Wert A −0,15 gegen −0,26 und −0,32 %/Woche in den Wiederholungen); die Streuung zwischen Läufen desselben Prompts ist so groß wie die bisher gemessenen Effekte.
- Seit 2026-10-12 (Wächter B-14): ein Kandidat (t ≥ 2 auf A) wird genau einmal auf A wiederholt; weiter geht er nur, wenn das Mittel beider Läufe t ≥ 2 hält. Keine weitere Wiederholung. Jedes Ergebnis nennt die Werkzeug-Version (Commit und Datei-Hash).
- Seit 2026-10-12 (Wächter review-002, B-15/B-16): jede Blockade am Turniertag hat eine Standardoption (tournament/README.md), und der Backlog zieht strukturelle Umbauten vor Ein-Satz-Varianten vor. Ensemble (E-013), Veto-Rolle (E-014) und grobe Stufen (E-015) zeigten keinen messbaren Unterschied; als Nächstes Trägheit mit Gedächtnis, seltener entscheiden, Veto auf eine langsamere Regel. Die Abbruchregel (B-17) entscheidet Aaron vor der ersten gewerteten Turnierrunde.
- Seit 2026-10-12 (E-019): Die Spannenlage ist im Prüfstand fast deckungsgleich mit Momentum und dem Abstand zum 100-Tage-Schnitt (Korrelation 0,75 und 0,94). Der Spannen-Anker wird deshalb als partielle Korrelation gemessen, nach Herausrechnen beider Größen (versuche/werkzeuge/anker.py). Nur das Gedächtnis der Vorwoche (E-016) bricht ihn (−0,15 gegen 0,40 bei E-003M).
