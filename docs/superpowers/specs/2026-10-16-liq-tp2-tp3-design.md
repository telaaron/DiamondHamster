# Liquidations-Engine, Teilprojekte 2 und 3: Binance-Archiv und Hyperliquid-Wahrheit

Stand 2026-10-16. Baut auf der Spec 2026-10-14-liq-engine-design.md und dem Code aus PR #8 auf. Design von Aaron
freigegeben am 2026-10-16 ("design ist super alles starten"), Entwurf: research/hyblock/03-design-tp2-tp3-entwurf.md.

## 0. Begriffe in einfachen Worten

- **OI (offene Positionen)**: Summe aller laufenden Wetten auf einen Markt, in Coins. Wie die Zeilenzahl einer Tabelle.
- **Mark Price**: fairer Preis, nach dem die Börse Liquidationen auslöst.
- **Funding**: kleine Gebühr, die regelmäßig zwischen Long- und Short-Seite fließt (Binance alle 8 h, Hyperliquid stündlich).
- **Adresse**: Konto-Kennung auf Hyperliquid. Alles, was ein Konto hält, ist öffentlich abfragbar.
- **Abdeckung**: Anteil des OI, den wir aus bekannten Konten kennen.

## 1. Ziel und Erfolgskriterien

1. **TP3, Sammler**: läuft dauerhaft auf Aarons Mac, zeichnet für BTC und ETH Trades, Marktzustand, Funding und die
   Positionen aller bekannten Konten auf. Kriterium: nach 24 h Laufzeit liegt die Abdeckung je Seite bei mindestens
   50 %, nach 7 Tagen wird sie berichtet (Ziel 80 %). Der Dienst überlebt Neustart und Netzausfall ohne Eingriff.
2. **TP3, Adapter und Vergleich**: aus den Rohdaten entstehen ein `EventSet` und eine `truth.csv`; `run` und `score`
   aus TP1 laufen darauf unverändert. Kriterium: ein Bericht nach mindestens 14 Tagen Daten (Warmup) mit Überlappung
   Engine gegen Baseline mit festen Hebeln. Die Zahl wird berichtet, wie sie ist; es gibt kein Bestehen-Kriterium,
   weil genau das die offene Frage ist.
3. **TP2, Binance**: Downloader holt BTCUSDT-Tagesdateien ab 2025-01-01, prüft Prüfsummen, ist fortsetzbar. Adapter
   baut daraus ein `EventSet` unter 200 MB. Kriterium: `run` erzeugt tägliche Snapshots über den ganzen Zeitraum mit
   `max_drift` unter 5 % außerhalb von Lücken.

Nicht in diesem Schritt: Oberfläche, Kalibrierung (TP4), weitere Coins, Binance-Live-Ingest, wanderndes Gitter (siehe 6).

## 2. Gemeinsame Änderung an der Engine: verdichtete Trades

Rohe Trades sind zu groß (Binance BTCUSDT: Millionen pro Tag). Beide Adapter verdichten sie auf **eine Zeile je
Minute und Größenklasse** (small/mid/large wie in `params.size_class`):

- `price` = volumengewichteter Preis der Klasse in dieser Minute, `qty` = Summe der Menge,
  `taker_buy` = 1, wenn die Mehrheit der Menge Käufer-initiiert war, sonst 0,
- neue optionale Spalte `notional` = mengengewichtetes Mittel des Einzel-Trade-Notionals (USD) der Klasse.

`events.py`: `notional` ist optional (fehlt sie, gilt wie bisher `price × qty`); wird beim Speichern mitgeschrieben,
wenn vorhanden, und muss > 0 sein. `attribution.deposits` bekommt ein optionales `notionals`-Array: Größenklasse und
Tier (Maximalhebel, Wartungssatz, Wartungsbetrag) kommen dann aus `notional`, die Positionsmenge für den Term k/q aus
`notional / price`. Die Engine reicht die Spalte durch. Ohne Spalte bleibt jedes Ergebnis aus TP1 bitgleich
(Test: Simulator-Score unverändert).

Funktion `liq.trades.compress(df) -> DataFrame` mit Eingabe `ts, price, qty, taker_buy` und Ausgabe wie oben,
`ts` = Ende der Minute (Punkt-in-Zeit: ein Minuten-Bucket ist erst nach seinem Ende bekannt).

## 3. TP3: Hyperliquid

### 3.1 Quellen (nur öffentlich, kein Schlüssel)

| Was | Wie | Gewicht | Takt |
|---|---|---|---|
| Trades mit Adressen | WebSocket `wss://api.hyperliquid.xyz/ws`, `trades` für BTC, ETH | – | laufend |
| OI, Mark, Funding-Prognose | `POST /info {"type":"metaAndAssetCtxs"}` | 20 | jede Minute |
| Kerzen 1m (Hoch/Tief) | `{"type":"candleSnapshot"}` letzte 10 min | 20+ | alle 5 min |
| Bezahltes Funding | `{"type":"fundingHistory","coin":..,"startTime":..}` | 20+ | stündlich |
| Positionen eines Kontos | `{"type":"clearinghouseState","user":..}` | 2 | Planer, 3.3 |

Budget: höchstens 600 Gewicht pro Minute (Hälfte des Limits 1200). Marktdaten brauchen rund 30/min, der Rest
(rund 285 Positionsabfragen/min) geht an den Planer. Bei HTTP 429 halbiert der Planer sein Tempo für 5 Minuten.
WebSocket: Ping alle 30 s; bei Abbruch neu verbinden mit Backoff 1, 2, 4 … 60 s; jede Unterbrechung wird als Lücke
protokolliert.

### 3.2 Ablage auf dem Mac (`<data>/hl/`, nicht im Repo)

- `raw/trades/<COIN>/YYYY-MM-DD.jsonl.gz`: jeder Trade wie geliefert plus Empfangszeit.
- `raw/ctx/YYYY-MM-DD.jsonl.gz`: Marktzustand je Minute (nur BTC, ETH, plus `maxLeverage` aus `universe`).
- `raw/candles/<COIN>/YYYY-MM-DD.jsonl.gz`, `raw/funding/<COIN>/YYYY-MM-DD.jsonl.gz`.
- `raw/positions/YYYY-MM-DD.jsonl.gz`: jede Positionsabfrage `{t, user, positions:[BTC/ETH-Positionen]}`, auch leere.
- `book/<COIN>/YYYYMMDDTHHMMZ.csv.gz` alle 15 min: Schnappschuss des bekannten Buchs, Spalten
  `user, side, mode, leverage, entry_px, liq_px, qty, polled_at`.
- `gaps.jsonl`: Unterbrechungen (WebSocket, HTTP, Mac schlief).
- `state.json`: Adressliste mit letzter Abfrage und letztem Notional, damit ein Neustart nicht bei null beginnt.
- `status.json` jede Minute: Konten gesamt, Konten mit Position, Abdeckung je Coin und Seite, Abfragen/min,
  letzte Fehler.

gzip wird zeilenweise angehängt (mehrere gzip-Glieder in einer Datei sind gültig); Tageswechsel nach UTC.

### 3.3 Planer für Positionsabfragen

- Jede Adresse aus einem Trade wird sofort fällig (sie hat gerade gehandelt, ihr Stand hat sich geändert).
- Sonst fällig nach Notional der BTC+ETH-Positionen: ≥ 1 Mio. USD alle 2 min, ≥ 100k alle 10 min, > 0 alle 30 min,
  ohne Position alle 6 h. Ohne Position und ohne Trade seit 3 Tagen: Adresse wird verworfen.
- Umsetzung als Prioritätswarteschlange nach Fälligkeitszeit; der Taktgeber holt höchstens so viele, wie das Budget
  erlaubt. Reicht das Budget nicht, steigt die Verspätung; `status.json` meldet die mittlere Verspätung.

### 3.4 Wahrheitsbuch und Abdeckung

Ein Positionseintrag: `side` aus dem Vorzeichen von `szi`, `mode` aus `leverage.type` (`cross`/`isolated`),
`qty = |szi|`, `liq_px = liquidationPx`. Positionen ohne `liquidationPx` (bei sehr kleinem Hebel möglich) zählen in
die Abdeckung, aber nicht ins Wahrheitsbuch; ihr Anteil wird berichtet. Abdeckung je Seite =
Σ bekannte `qty` dieser Seite ÷ `openInterest`. Annahme, beim ersten Lauf zu prüfen: `openInterest` zählt eine Seite
in Coins; falls nicht, wird die Formel angepasst und hier vermerkt.

Staleness: jeder Eintrag trägt `polled_at`; Einträge älter als 60 min fliegen aus dem Schnappschuss.

### 3.5 Adapter

`python -m diamondhamster.liq hl-events --data <data>/hl --coin BTC --out <dir>` schreibt:

- `trades.csv`: verdichtet nach 2 aus den WebSocket-Trades (`side` B = Käufer-initiiert).
- `oi.csv`: je Minute aus `ctx.openInterest`.
- `mark.csv`: je Minute `close = markPx`; `high/low` = Maximum/Minimum aus `markPx` und Kerzen-Hoch/Tief dieser Minute.
- `funding.csv`: bezahlte Raten aus `fundingHistory`.
- `gaps.csv` aus `gaps.jsonl`; `truth.csv` (`ts, side, mode, liq_price, qty`) aus den Buch-Schnappschüssen;
  `ats.json` = Schnappschuss-Zeiten; `meta.json` (exchange `hyperliquid`).
- `tiers.toml`: ein Tier mit `maxLeverage` aus `universe`, Wartungssatz = 1 / (2 × maxLeverage), Betrag 0
  (Hyperliquid-Regel für Positionen unterhalb der Margin-Tabellen-Stufen). Dazu eine Parameterdatei, die auf diese
  Tiers zeigt, sonst wie `v001.toml`.

Danach laufen `run --model engine|baseline` und `score` aus TP1 unverändert.

### 3.6 Betrieb auf dem Mac

- Abhängigkeit `websockets` als optionales Extra `collector`; sonst nur Standardbibliothek (`urllib`, `asyncio`, `gzip`).
- `python -m diamondhamster.liq hl-collect --data <dir>` läuft im Vordergrund; `hl-service install|uninstall|status`
  schreibt einen launchd-Agenten `com.diamondhamster.hl-collector` (`KeepAlive`, Logs in `<data>/hl/logs/`) und startet
  ihn über `caffeinate -i`, damit der Mac im Leerlauf nicht einschläft. Zugeklappt ohne Netzteil schläft er trotzdem;
  das erscheint als Lücke.
- Keine Orders, keine Schlüssel, keine privaten Endpunkte.

## 4. TP2: Binance-Archiv

### 4.1 Downloader

`python -m diamondhamster.liq bn-download --symbol BTCUSDT --start 2025-01-01 [--end gestern] --data <dir>` lädt von
`https://data.binance.vision/data/futures/um/`:

- täglich: `metrics` (OI alle 5 min), `markPriceKlines/1m`, `aggTrades`;
- monatlich: `fundingRate` (der laufende Monat fehlt im Archiv; wird als Lücke im Funding vermerkt).

Jede Zip-Datei wird gegen ihre `.CHECKSUM` (sha256) geprüft. `aggTrades` werden direkt nach dem Download nach 2
verdichtet und die Zip-Datei gelöscht; die anderen werden als CSV abgelegt. Fortsetzbar: ein Tag mit Marker-Datei
`done/<typ>/<tag>` wird übersprungen. 404 für einen Tag (Archiv lückenhaft) wird in `missing.jsonl` vermerkt, kein
Abbruch. Dateien mit und ohne Kopfzeile werden beide gelesen.

### 4.2 Adapter

`python -m diamondhamster.liq bn-events --data <dir> --symbol BTCUSDT --out <dir>`: `oi.csv` aus
`sum_open_interest`, `mark.csv` aus den 1m-Mark-Kerzen, `trades.csv` aus den verdichteten aggTrades, `funding.csv` aus
`last_funding_rate`, `gaps.csv` aus fehlenden Tagen, `ats.json` = täglich 00:00 UTC.

### 4.3 Echte Tiers

`liq/tiers/binance-btcusdt.toml` mit Quelle und Datum im Kopf. Die API dafür braucht einen Schlüssel; die Werte kommen
von der öffentlichen Binance-Seite "Leverage and Margin" und werden vom Mac aus einmal abgeschrieben. Bis dahin
rechnet TP2 mit `illustrativ.toml`, und der Bericht sagt das.

### 4.4 Grober Abgleich ohne Wahrheit

Liquidationen sind im Archiv nicht zuverlässig vorhanden. Abgleich in TP2 daher nur: Aaron legt für 3 Tage seine
Hyblock-Ansicht neben unsere Snapshots (Bildvergleich, kein Score). `liq_corr` bleibt leer, das ist erwartet.

## 5. Tests (Cloud, ohne Netz)

- Verdichtung: Summen, VWAP, Klassen, Minutengrenzen, Punkt-in-Zeit-`ts`.
- Engine mit `notional`: TP1-Ergebnisse bitgleich ohne Spalte; mit Spalte wirkt die Klasse wie erwartet.
- Hyperliquid: Parser für alle Antworten aus den Doku-Beispielen; Planer (Fälligkeit, Budget, 429-Bremse, Verwerfen);
  Ablage (Tageswechsel, Anhängen, Neustart aus `state.json`); Buch und Abdeckung; Adapter Ende-zu-Ende auf einem
  synthetischen Rohdaten-Ordner, danach `run` und `score` darauf.
- Collector-Schleife mit gefälschtem Transport (WebSocket und HTTP als austauschbare Objekte), inklusive Abbruch und
  Wiederverbindung.
- Binance: Prüfsumme, Fortsetzen, 404, Kopfzeile ja/nein, Adapter Ende-zu-Ende auf Mini-Zips.
- Live-Rauchtest nur auf dem Mac: 10 Minuten `hl-collect`, dann `status.json` lesen.

## 6. Bewusst offen

- Wanderndes Gitter: BTC lag seit 2025 innerhalb von ¼ bis 4× des Startpreises; das feste Gitter reicht für diesen
  Zeitraum. Verlässt der Kurs es, meldet die Engine das schon heute über `out_of_range_share`.
- Konten, die seit Start nicht gehandelt haben, findet der Sammler nicht. Bleibt die Abdeckung unter 80 %, folgt eine
  zweite Quelle für Adressen.
- Hyperliquid-Margin-Tabellen für sehr große Positionen werden in TP3 nicht abgebildet (ein Tier).
