# Versuche: Spielplatz für die Methode

Die Methode ist Prompt + Daten + Aufbereitung. Ein Versuch ändert genau eine dieser drei Achsen gegenüber dem aktuellen Dev-Champion und wird auf einem festen Prüfstand bewertet. Wer gewinnt, ist nur ein Kandidat. Bewiesen wird erst im Zukunfts-Turnier (Protokoll §11, §13).

Überblick über alle Versuche: [UEBERSICHT.md](UEBERSICHT.md). Werkzeug: `src/diamondhamster/versuche.py` im Repo (PR #2), Tests in `tests/test_versuche.py`.

## 1. Prüfstand (fest, wird nicht verändert)

| | |
|---|---|
| Entscheidungstage | 13 Sonntage 2026-07-05 bis 2026-09-27 (Tagesschluss UTC), alle nach dem Wissensstand des Modells (ca. Juni 2026) |
| Set A (Filter) | BTC ETH SOL XRP DOGE ADA LINK AVAX DOT LTC |
| Sets B+C (Check) | BNB TRX BCH SHIB UNI NEAR APT SUI ARB OP · ATOM ETC FIL AAVE INJ HBAR XLM ICP PEPE ALGO |
| Kerzen | `tournament/candles/*.csv` (TradingView, Binance-Spot, geprüft) |
| Modell | claude-opus-5-5, frischer `claude -p` ohne Werkzeuge, ohne MCP, ohne Gedächtnis, in leerem Ordner |
| Wiederholungen | 1 (T-001 war über 5 Wiederholungen sehr stabil; Rauschen über Wochen und Coins ist viel größer) |
| Ausgabe | erst die schriftliche Überlegung (Marktlage, Strategie, Grund fürs Gewicht), dann als Letztes ein JSON mit einem Gewicht 0 bis 1 pro Coin (Standard seit 2026-10-11, §4a) |

Ein Batch = eine Entscheidungswoche mit je einem Fenster pro Coin, in zufälliger Reihenfolge und mit zufälligen IDs. Alle Fenster eines Batches enden am selben Tag.

## 2. Bewertung

- **Timing-Wert** pro Entscheidung: (Gewicht − mittleres Gewicht dieses Coins) × Rendite der Folgewoche − Umschichtung × 0,2 %. Er misst nur, ob das Hin- und Herschieben Geld bringt, gegenüber einer festen Position in derselben Höhe. Konstant halten = 0.
- **Gepaart gegen den Champion:** gleiche Coins, gleiche Wochen. Pro Woche Mittel über die Coins, Differenz Versuch minus Champion, t-Wert über die 13 Wochen.
- **Robust:** Die Differenz wird zusätzlich ohne die beste Woche des Versuchs berichtet. Hängt der Vorsprung an einer Woche, zählt er nicht.
- Nebenbei: Rank-IC (gibt er den richtigen Coins mehr?), Exposure, Wochen besser.

**Urteil** (automatisch, `score`):

| Urteil | Bedingung |
|---|---|
| schlechter | t ≤ −2 auf Set A |
| kein messbarer Unterschied | t < 2 auf A, oder ohne beste Woche nicht mehr vorn |
| Kandidat (Wiederholung) | t ≥ 2 auf A und ohne beste Woche vorn → einmal auf A wiederholen (`--set A2`) |
| Kandidat | das Mittel beider A-Läufe hält t ≥ 2 und ohne beste Woche vorn → B+C laufen lassen |
| neuer Dev-Champion | zusätzlich auf B+C (20 Coins): vorn, t ≥ 1, ohne beste Woche vorn; und gegen die feste Referenz E-003 auf A (auch ohne beste Woche) und B+C vorn |
| verworfen: schlägt die feste Referenz nicht | schlägt den Champion, aber nicht E-003 |
| verworfen | Kandidat, hält auf B+C nicht |

Ein neuer Dev-Champion wird Basis für die folgenden Versuche (`champion.json`). Er ist damit noch nicht im Turnier.

**Referenz aus drei Läufen (2026-10-12).** Zwei Wiederholungen von E-003 lagen deutlich unter dem ersten Lauf (Timing-Wert A −0,15 / −0,26 / −0,32 %/Woche): Derselbe Prompt schwankt zwischen Läufen etwa so stark wie die bisher gemessenen Effekte. Champion und Referenz ist deshalb E-003M, das Mittel der drei Läufe (gemittelt wird der Timing-Wert je Woche und Coin, nicht die Gewichte; `"composite"` in spec.json). Neue Versuche kopieren `E-003M/prompt.md` (gleich wie E-003).

**Feste Referenz (B-12, übernommen 2026-10-12).** Bei rund 24 Versuchen am Tag wird ab und zu einer nur durch Glück Champion. Würde er die Messlatte, sähen danach echte Verbesserungen schlechter aus. Deshalb muss jeder neue Champion zusätzlich die feste Referenz E-003M schlagen; `score` prüft das automatisch und schreibt es als `vs_reference` in result.json.

## 3. Anti-Schummel-Regeln

1. **Eine Änderung pro Versuch**, Basis ist der Champion beim Start. Sonst weiß niemand, was gewirkt hat.
2. **Kein Nachwürfeln.** Ein Versuch läuft einmal. `export` und `decide` überspringen Vorhandenes. Antworten löschen oder neu würfeln ist verboten; eine Wiederholung bekommt eine neue ID und zählt als eigene Variante.
3. **Nur der eigene Ordner.** Ein Versuchs-Thread schreibt nur in `E-NNN/`. `champion.json`, `UEBERSICHT.md` und Ordner anderer Versuche ändert nur das Werkzeug bzw. der Forschungs-Thread.
4. **Keine Datums- oder Coin-Hinweise.** Jedes Fenster wird vor dem Versand geprüft: keine Jahreszahl, kein Monatsname, kein Ticker. Preise auf 100 normiert. Treffer bricht den Export ab.
5. **Keine Zukunft im Fenster.** Die Aufbereitung (`render.py`) bekommt nur Kerzen bis zum Entscheidungstag. Batches sind pro Woche quer über Coins gebaut. Der frühere Fehler (Batches mit aufeinanderfolgenden Wochen eines Coins: das spätere Fenster zeigt, was nach dem früheren kam) betrifft die Dev-Läufe von T-001 und T-002 vom 11.10. Hier und im Turnier ist er ausgeschlossen.
6. **Decider ohne Zugriff.** Geprüft am 2026-10-11: keine Werkzeuge, kann keine Dateien lesen, kein Netz. Er kennt das heutige Datum aus seinem Systemprompt; das verrät ihm nicht, welche Woche ein Fenster zeigt.
7. **Kein Holdout.** Der Prüfstand nutzt nur Jul bis Sep 2026. Der Regel-Holdout (2025-01 bis 2026-06) bleibt unberührt.
8. **Wir kennen die Dev-Wochen.** Wer Prompts schreibt, hat den Markt Jul bis Sep gesehen. Das ist der Hauptgrund, warum nur das Turnier zählt.
9. **Zähler.** `UEBERSICHT.md` zeigt, wie viele Varianten getestet wurden. Bei 24 Versuchen am Tag ist der beste fast sicher teils Glück.

## 4. Einen Versuch durchführen

```bash
cd <repo>   # Branch main (git pull origin main vor jedem Versuch)
# Bis PR #5 gemergt ist: git fetch origin claude/project-thread-lupsy0 && git checkout origin/claude/project-thread-lupsy0 -- src/diamondhamster/versuche.py
#   (nötig für die Referenz E-003M und die Referenz-Prüfung)
H=/mnt/project-files/research/versuche
N=E-0XX     # nächste freie Nummer; mkdir reserviert sie (schlägt fehl, wenn vergeben)
mkdir $H/$N
C=$(python -c "import json;print(json.load(open('$H/champion.json'))['id'])")
cp $H/$C/prompt.md $H/$N/ ; [ -f $H/$C/render.py ] && cp $H/$C/render.py $H/$N/
# spec.json schreiben: {"id","parent": Champion,"axis": prompt|daten|format,"change": ein Satz,
#   "input": candles|indicators|custom,"lookback": Tage,"thread": Link zum Thread,"notes": Hypothese}
# genau EINE Sache in prompt.md oder render.py ändern; render(df, lookback) -> str, df endet am Entscheidungstag
PYTHONPATH=src python -m diamondhamster.versuche run $N --set A      # ca. 1 Minute
# bei Urteil "Kandidat: einmal auf A wiederholen": genau EINE Wiederholung, danach zählt das Mittel beider Läufe
PYTHONPATH=src python -m diamondhamster.versuche export $N --set A2 && PYTHONPATH=src python -m diamondhamster.versuche decide $N --set A2
PYTHONPATH=src python -m diamondhamster.versuche score $N
# nur bei Urteil "Kandidat, Check-Sets B+C laufen lassen":
PYTHONPATH=src python -m diamondhamster.versuche export $N --set B && PYTHONPATH=src python -m diamondhamster.versuche decide $N --set B
PYTHONPATH=src python -m diamondhamster.versuche export $N --set C && PYTHONPATH=src python -m diamondhamster.versuche decide $N --set C
PYTHONPATH=src python -m diamondhamster.versuche score $N
PYTHONPATH=src python -m diamondhamster.versuche card $N
PYTHONPATH=src python -m diamondhamster.versuche overview
```

Lesbare Kopie im Repo (Ordner `versuche/`, ohne `runs/`): `python -m diamondhamster.versuche publish`, committet vom Forschungs-Thread.

Weitere Felder in spec.json:
- `"ensemble": k` – k unabhängige Batches pro Woche (eigene Reihenfolge und IDs), entschieden wird mit dem mittleren Gewicht. Kostet k-fach.
- `"memory": true` – die Wochen laufen nacheinander; jedes Fenster beginnt mit `last week: weight W, flip price F on today's scale` (Kipp-Preis der Vorwoche auf die heutige 100-Skala umgerechnet) bzw. `last week: no decision`. Der Prompt verlangt dann das JSON als `{"id": {"weight": w, "flip": Preis}}`. Nicht mit `ensemble` kombinierbar.
- `"composite": [IDs]` – nur für Referenzen: Mittel des Timing-Werts mehrerer Läufe (E-003M).

`card` schreibt auch `E-NNN/denken.md`: die volle Antwort des Deciders für jede Woche, unverändert, mit den Coin-Namen erst nachträglich eingesetzt.

Ergebnis im Thread: der Inhalt von `E-NNN/card.md` (Änderung, Diff zum Prompt der Basis, voller Prompt, Aufbereitung, Bewertung, Urteil, Verbrauch). Bei "neuer Dev-Champion" meldet der Thread das dem Forschungs-Thread; der setzt `champion.json`.

`input: custom` braucht `render.py`. Damit ein solcher Gewinner ins Turnier kann, muss das Turnier-Werkzeug ihn erst unterstützen (Forschungs-Thread).

## 4a. Die KI schreibt ihre Überlegung auf (Standard ab E-003)

Aaron will sehen, was die KI sich gedacht hat, nicht nur die Zahl. Deshalb gilt für jeden Prompt ab E-003:

- Der Decider ist ein frischer Opus-5.5-Lauf ohne Werkzeuge, ohne Projektwissen, ohne Gedächtnis. Er bekommt nur Prompt und Daten.
- Der Prompt verlangt vor dem JSON eine Analyse. Vorlage ist der Schluss von `E-003/prompt.md`:
  ```
  Before the weights, write out your analysis:
  1. Strategy: in 2 to 3 sentences, the rule you will apply to every window.
  2. Then for each window, under its id: your read of the market (trend, structure, key levels as prices on the 100 scale), your weight and why, and the price on the 100 scale that would make you change your mind.
  3. End with one JSON object mapping each window id to its weight, e.g. {"a1b2c3d4e5": 0.0, "f6a7b8c9d0": 1.0}. Nothing after it.
  ```
  Nur diese Vorlage verwenden. Eine ältere Formulierung, die das Modell bat, sein Denken offenzulegen, hat Opus 5.5 in 6 von 13 Wochen abgelehnt (API-Fehler, Schutzfilter). Sie wird hier bewusst nicht zitiert, weil das Zitat Sitzungen stören kann, die diese Datei lesen. Die Vorlage oben lief in 39 von 39 Batches sauber.
- Bricht ein Lauf technisch ab (API-Fehler, keine Antwort), wird er unbewertet nach `E-NNN/abgebrochen-vN/` verschoben und neu gestartet. Das ist kein Nachwürfeln, solange von dem abgebrochenen Lauf kein Ergebnis angesehen wurde.
- Gespeichert wird die komplette Antwort (`runs/<set>/<woche>/responses.json`, Feld `raw`), lesbar in `denken.md`. Der Thread zeigt mindestens eine Woche im Wortlaut und verlinkt `denken.md`.
- Fehlt im JSON ein Fenster, bricht die Bewertung ab, statt still eine Lücke zu werten.

**Neue Referenz.** Eine schriftliche Überlegung ändert, wie die KI entscheidet. E-000 bis E-002 (nur Zahl) sind darum nicht mehr die Messlatte. E-003 (T-001 plus Überlegung, sonst nichts) hat gemessen, was das Aufschreiben allein bewirkt: kein messbarer Unterschied (A +0,08 %/Woche t 1,0; B+C −0,26 % t −1,2). Seit 2026-10-11 ist E-003 Referenz und Champion, weil das Aufschreiben Pflicht ist. Alle folgenden Versuche bauen auf seinem Prompt auf. Backlog-Ideen, die schon ohne Überlegung getestet wurden (E-001, E-002), dürfen mit Überlegung neu laufen und zählen dann als eigene Varianten.

## 5. Vom Dev-Champion ins Turnier

- **Höchstens ein neuer Prompt pro Woche** wird eingefroren, samstags, vor dem Sonntagsschluss. Kandidat ist der zuletzt gekürte Dev-Champion, wenn er nicht schon im Turnier ist.
- Ein Prompt mit Überlegung kann ins Turnier, ohne dass die laufenden Turnier-Prompte (T-001, T-002, nur Zahl) geändert werden; sie bleiben, wie sie eingefroren sind.
- Er muss den aktuell im Turnier laufenden besten Prompt auf dem Prüfstand (A und B+C) schlagen, nicht nur seinen Vorgänger, und zwar auf B+C mit t ≥ 2 (nicht nur t ≥ 1 wie für den Dev-Champion; B-12).
- T-001 bleibt als Grundlinie. Höchstens 4 Prompts gleichzeitig aktiv. Ist das voll, nimmt nur Aaron einen heraus.
- Einfrieren ist eine Protokoll-Handlung mit Datum und Hash (Protokoll §11). Bewertet wird nur, was danach entschieden wurde.

## 6. Verbrauch

Gemessen an E-000 (2026-10-11): ein Versuch auf Set A = 13 Claude-Aufrufe, etwa 0,8 Mio. Zeichen, 4,70 USD Listenpreis, unter einer Minute. Mit B+C für einen Kandidaten insgesamt etwa 14 bis 15 USD. Das geht nicht als Rechnung raus, zählt aber gegen Aarons Claude-Nutzungslimit.

Stündlich nur Set A: etwa 24 × 4,70 = 113 USD Listenpreis am Tag, plus Kandidaten. Ob das in Aarons Limit passt, kann von hier niemand sehen. Regel: Meldet ein Lauf ein Nutzungslimit, setzt der Coordinator den Takt auf alle 3 Stunden und sagt es Aaron. Jede Karte zeigt den Verbrauch, die Übersicht die Summe.

## 7. Vorschläge des Methodik-Wächters (B-09 bis B-11)

| Vorschlag | Übernommen? |
|---|---|
| Dev-Ergebnis nur als Filter, nur das Turnier zählt | ja (§2, §5) |
| Höchstens eine Beförderung ins Turnier pro Woche | ja (§5) |
| B-12: Champion nur, wenn er auch E-003 schlägt; Turnier erst bei t ≥ 2 auf B+C | ja (§2, §5), seit 2026-10-12; Referenz ist inzwischen E-003M |
| B-14: Wiederholung eines Kandidaten vorab festgelegt (eine, Mittel beider Läufe muss t ≥ 2 halten; keine dritte); Werkzeug-Version auf jeder Karte | ja, seit 2026-10-12 (`--set A2`, Feld `tool` in result.json) |
| Sichtbarer Zähler aller getesteten Varianten | ja (UEBERSICHT.md) |
| Ergebnis ohne beste Woche mitberichten | ja, und es entscheidet mit (§2) |
| Jeder Versuch auf allen 30 Coins | teilweise: alle 30 Coins für jeden Kandidaten, aber nicht für jeden Versuch. Grund: das verdreifacht den Verbrauch (14 statt 4,70 USD) für Versuche, die schon auf 10 Coins nichts zeigen. Ein Gewinner muss auf den anderen 20 Coins bestehen, die er nie gesehen hat; das ist strenger als ein Ergebnis über alle 30. |
| Verbrauch pro Versuch protokollieren | ja (Karte und Übersicht) |

## 8. Erste Ergebnisse auf diesem Prüfstand

- **E-000 = T-001**: Timing-Wert −0,24 % pro Woche auf A, −0,30 % auf B+C (t ≈ −0,8 bis −0,9). Das Hin- und Herschieben verliert also auch über 30 Coins leicht gegen eine feste Position. Exposure im Mittel 37 bis 45 %.
- **E-001 = T-002** (plus Indikatoren): auf A besser (+0,12 % pro Woche, t 1,7, 9 von 13 Wochen), auf B+C schlechter (−0,06 %). Urteil: kein messbarer Unterschied. Der frühere Dev-Befund "T-002 schlechter" (2 Coins, mit Überlappungs-Leak) war damit Rauschen in die andere Richtung.
