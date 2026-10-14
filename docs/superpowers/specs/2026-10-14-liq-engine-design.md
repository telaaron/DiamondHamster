# Liquidations-Engine ("eigenes Hyblock"): Design

Stand: 2026-10-14 · Status: zur Prüfung durch Aaron · Ansatz A (Python, Replay zuerst) freigegeben am 2026-10-14

Herkunft: Aarons Entwurf "Hyblock 2.0" im Projekt-Thread, kritisch geprüft in
`research/hyblock/01-entwurf-review-und-designvorschlag.md` (Projektordner). Diese Spec übernimmt das dortige Design
und korrigiert einen Fehler darin (siehe 3.3, Punkt 1).

## 0. In einfachen Worten

- **Liquidation:** Ein Trader wettet mit geliehenem Geld (Hebel). Ist sein Einsatz durch Kursverluste aufgebraucht,
  schließt die Börse die Wette zwangsweise. Der Kurs, bei dem das passiert, ist sein **Liquidationspreis**.
- **Open Interest (OI):** Summe aller offenen Wetten an einer Börse. Jede Long-Wette (auf steigend) hat eine
  Short-Wette (auf fallend) als Gegenüber, deshalb sind beide Seiten immer gleich groß.
- **Mark Price:** Der Referenzkurs, den die Börse für Liquidationen nutzt. Er ist geglättet, ein kurzer Ausreißer im
  gehandelten Kurs löst deshalb oft nichts aus.
- **Isoliert vs. Cross:** Isoliert steht nur der Einsatz dieser einen Wette auf dem Spiel (Liquidationspreis
  berechenbar). Bei Cross haftet das ganze Konto, dessen Guthaben niemand außer der Börse kennt.
- **Tier:** Je größer eine Wette, desto weniger Hebel erlaubt die Börse und desto mehr Sicherheitsmarge
  (Wartungsmarge) verlangt sie. Die Stufen heißen Tiers.
- **Funding:** Alle 8 Stunden zahlt eine Seite der anderen einen kleinen Betrag. Das verschiebt die
  Liquidationspreise langsam.
- **Was die Engine macht:** Sie rekonstruiert, wie ein Datenbank-Zustand ("wer hält welche Wette mit welchem Hebel")
  wohl aussieht, nur aus dem öffentlichen Verkehr (Trades, OI, Kurs). Das tun Hyblock und Coinglass auch; niemand
  außerhalb der Börse sieht die echte Tabelle. Ausnahme: Hyperliquid (Teilprojekt 3), dort ist sie öffentlich.

## 1. Ziel und Nicht-Ziele

**Ziel.** Eine eigene Engine, die aus öffentlichen Börsendaten schätzt, bei welchen Preisen wie viel Positionsvolumen
(Notional) liquidiert würde, getrennt nach Long und Short. Besser als Hyblock/Coinglass in drei Punkten:

1. Keine festen Hebel: Liquidationspreise kommen aus einer Mischverteilung über Hebel, Margin-Modus und Tier-Grenzen,
   deren Gewichte kalibriert werden.
2. Massenerhaltung statt freiem Decay: Die modellierte offene Positionsmasse jeder Seite entspricht jederzeit dem
   echten Open Interest. Phantom-Liquidität kann dadurch nicht entstehen; Decay entscheidet nur, *welche* Positionen
   die beobachteten Schließungen tragen.
3. Für KI gebaut: point-in-time Snapshots als JSON mit Herkunft, Modellversion und Unsicherheitsanteil, ohne
   Lookahead, direkt nutzbar für Prompts und den Prüfstand.

**Nicht-Ziele.** Keine Orders, keine Exchange-Keys, keine privaten Endpunkte, kein L2-Orderbuch, keine
Kursprognose. Kein Realtime-UI, bevor die Kalibrierung (Teilprojekt 4) einen Vorteil gegenüber Baselines zeigt.

## 2. Teilprojekte

| Nr. | Inhalt | Läuft wo |
|---|---|---|
| **1** | **Engine-Kern, synthetischer Simulator, fixe-Hebel-Baseline, Snapshot-JSON, CLI** | **Cloud (diese Spec)** |
| 2 | Binance-Archiv-Replay (data.binance.vision: aggTrades, metrics/OI 5 min, markPriceKlines, fundingRate), echte Tier-Tabellen, Parquet | Mac oder freigeschaltete Hosts |
| 3 | Hyperliquid als Wahrheitsquelle: alle Positionen samt Hebel und exaktem Liquidationspreis sind dort öffentlich (Adressen aus dem Trade-Feed, Positionen per `clearinghouseState`; Abrufweg vor Bau prüfen). Liefert echte Bücher statt Schätzungen | Mac (api.hyperliquid.xyz in der Cloud gesperrt, getestet 2026-10-14) |
| 4 | Kalibrierung: Engine auf Hyperliquid-Events gegen das echte Hyperliquid-Buch tunen und messen; danach gegen gemeldete Liquidationen bei Binance/Bybit; Bewertung vs. Baselines, Bericht | Mac + Cloud |
| 5 | Live-Ingest Mac (Binance, Bybit, OKX, Hyperliquid, nur öffentliche WS/REST) | Mac |
| 6 | Visualisierung (Heatmap, Pine-Export) | nach 4 |

Jedes Teilprojekt bekommt eigene Spec-Ergänzung und eigenen Plan. Diese Spec legt Teilprojekt 1 vollständig fest und
die Schnittstellen, die 2 bis 5 später nutzen.

## 3. Teilprojekt 1

### 3.1 Ablage

Paket `src/diamondhamster/liq/` im Repo, Tests in `tests/liq/`. Keine neuen Pflicht-Abhängigkeiten (numpy, pandas,
stdlib `tomllib`). Dateien:

| Datei | Verantwortung |
|---|---|
| `events.py` | Event-Typen und Validierung (Reihenfolge, Lücken) |
| `grid.py` | Log-Preisgitter: Preis ↔ Bucket-Index |
| `margin.py` | Liquidationspreis-Formel, Tier-Tabellen |
| `params.py` | Parametersatz aus TOML laden, Hash berechnen |
| `book.py` | Zustand: Masse je Seite × Margin-Modus × Kohorte × Bucket; Opens, Closes, Sweep, Funding |
| `engine.py` | Schleife über Intervalle, Massenerhaltung, Snapshots auslösen |
| `snapshot.py` | Snapshot-Objekt und JSON-Schema |
| `baseline.py` | Fixe-Hebel-Modell (10/25/50/100x, Coinglass-Stil) über dieselbe Schnittstelle |
| `sim.py` | Synthetischer Markt mit bekannter Wahrheit |
| `score.py` | Vergleich Modell-Buch vs. wahres Buch |
| `__main__.py` | CLI |
| `params/v001.toml` | Standardparameter |
| `tiers/illustrativ.toml` | Tier-Tabelle für Tests, ausdrücklich `source = "illustrativ, keine Börsendaten"` |

### 3.2 Events (Schnittstelle für Teilprojekte 2 und 4)

Alle Zeitstempel UTC in Millisekunden, je Börse und Symbol getrennt. Ein Event-Satz ist ein Verzeichnis mit einer
CSV je Typ (in Teilprojekt 2 Parquet, gleiche Spalten).

| Typ | Spalten | Bedeutung |
|---|---|---|
| `trades` | `ts, price, qty, taker_buy` | ein aggTrade; `qty` in Basiswährung |
| `oi` | `ts, oi` | Open Interest in Basiswährung zum Zeitpunkt `ts` |
| `mark` | `ts, high, low, close` | Mark-Price-Kerze, endet bei `ts` |
| `funding` | `ts, rate` | Funding-Zahlung zum Zeitpunkt `ts`; `rate > 0` heißt Longs zahlen |
| `liquidations` | `ts, side, price, qty` | gemeldete Liquidation (nur Ground Truth, nie Modell-Eingang) |
| `gaps` | `start, end, reason` | bekannte Lücken im Feed |

Validierung: Zeitstempel monoton je Datei; `oi > 0`; `price > 0`; Verstoß → Fehler mit Datei und Zeile.

### 3.3 Modell

**Gitter.** Log-Abstand `bucket_bp` (Standard 10 bp = 0,1 %), Bereich `[p0 · 0,25, p0 · 4]` um den Startpreis.
Liquidationspreise außerhalb landen im Randbucket und werden im Snapshot als `out_of_range` gezählt.

**Zustand.** `mass[side, mode, cohort, bucket]` in Basiswährung. `side ∈ {long, short}`, `mode ∈ {isolated, cross}`,
`cohort` = Eröffnungstag (UTC); Kohorten älter als `max_cohorts` (Standard 90) werden in die älteste
zusammengelegt. Je Kohorte und Seite ein `funding_shift` (log-Preis), siehe Schritt 6.

**Intervall.** Die Engine schreitet von OI-Zeitpunkt zu OI-Zeitpunkt: Intervall `(t_{i-1}, t_i]`, darin Volumen
`V = Σ qty`, `ΔOI = oi_i − oi_{i-1}`, Trades mit Preisen, Mark-Hoch/Tief, Funding-Events.

Schritte je Intervall:

1. **Opens und Closes je Seite.** In jedem Trade steht ein Käufer einem Verkäufer gegenüber, zum selben Preis.
   Steigt OI, haben *beide* Seiten im selben Umfang eröffnet; der Taker bestimmt nicht, welche Seite eröffnet.
   (Korrektur gegenüber dem Review-Dokument, das die Opens nach Taker-Richtung aufteilen wollte.)
   Mit `A = max(V − |ΔOI|, 0)` (mehrdeutiges Volumen: Positionsübergaben) und kalibriertem Anteil `α ∈ [0, 1]`:
   - `opens_side  = max(ΔOI, 0) + α · A / 2`
   - `closes_side = max(−ΔOI, 0) + α · A / 2`
   für Long und Short gleich. Bleibt `V < |ΔOI|` (Feed-Fehler), wird das Intervall wie in 3.6 behandelt.
2. **Einstiegspreise.** Opens werden über die Trade-Preise des Intervalls verteilt, proportional zum Volumen je
   Preis-Bucket.
3. **Liquidationspreise.** Für jede Einstiegsmenge `q` bei Preis `E` und Größenklasse `s` (aus dem Notional des
   aggTrades: `small < 10 000 USD ≤ mid < 1 000 000 USD ≤ large`):
   - Hebel `L` aus einer diskreten Mischung über `{2, 3, 5, 10, 20, 25, 50, 75, 100, 125}` mit Gewichten
     `w[s, L]` aus den Parametern; Hebel über dem Tier-Maximum für das Notional fallen weg, Gewichte werden
     renormiert.
   - Isoliert (Anteil `1 − c`), Wartungsmarge `m` und Wartungsbetrag `k` aus der Tier-Tabelle:
     - Long: `P_liq = (E · (1 − 1/L) + k/q) / (1 − m)`
     - Short: `P_liq = (E · (1 + 1/L) − k/q) / (1 + m)`
     (Herleitung: Margin `q·E/L` plus Gewinn/Verlust gleich Wartungsmarge `m·q·P − k`. Gebühren vernachlässigt.)
   - Cross (Anteil `c`): Abstand `|E − P_liq|` des isolierten Falls mal Faktor `κ` (Parameter, Standard 2,0),
     weil Kontoguthaben unbekannt ist und den Abstand vergrößert.
   - Masse `q · w · (1 − c)` bzw. `q · w · c` in den Bucket von `P_liq`, Kohorte = Tag von `t_i`.
4. **Sweep.** Long-Masse mit `P_liq ≥ mark_low` und Short-Masse mit `P_liq ≤ mark_high` (jeweils inkl.
   `funding_shift`) wird entfernt und als `swept_side` gebucht. Mark Price, nicht Last Price.
5. **Closes verteilen.** `rest_side = max(closes_side − swept_side, 0)` wird über die verbleibende Masse der Seite
   verteilt, Gewicht je Kohorte `mass · exp(β · alter_tage)`. `β = 0`: proportional (konstante Rate). `β > 0`:
   alte Positionen schließen eher (Abbau von Geister-Liquidität). `β` wird in Teilprojekt 4 kalibriert, Richtung
   unbekannt, Standard 0. Liquidationen sind Teil der OI-Abnahme, deshalb zählen sie gegen die Closes und nicht
   zusätzlich.
6. **Funding.** Bei Funding-Event mit Rate `f`: Für isolierte Masse der zahlenden Seite (Long bei `f > 0`) wandert der
   Liquidationspreis um `|f|` relativ Richtung aktueller Preis, für die empfangende Seite um `|f|` weg. Umgesetzt als
   `funding_shift` je Kohorte in log-Preis (kein Umschichten zwischen Buckets). Cross-Masse bleibt unverändert.
7. **Massenerhaltung.** Summe je Seite wird auf `oi_i` skaliert. Die Skalierung `|1 − faktor|` wird je Intervall
   protokolliert; über `drift_warn` (Standard 5 %) ist das ein Warnsignal im Snapshot.

**Start (Warmup).** Beim ersten OI-Wert ist die Verteilung des bestehenden OI unbekannt. Er wird als Kohorte "seed"
zum Startpreis mit der Hebelmischung eingesetzt. Snapshots in den ersten `warmup_days` (Standard 14) tragen
`warmup: true`, und `seed_share` (Anteil Seed-Masse) wird immer ausgegeben.

**Parameter (`params/v001.toml`).** `bucket_bp, max_cohorts, alpha, cross_share, cross_kappa, beta,
leverage_weights[small|mid|large], warmup_days, drift_warn, cluster_min_share, top_n, tiers` (Pfad). `params_hash` = SHA-256 der
kanonisierten Datei.

### 3.4 Snapshot (AI-Schnittstelle)

Erzeugt zu angefragten Zeitpunkten, nur aus Events `≤ at`. JSON:

```json
{
  "schema": "liq-snapshot/1",
  "exchange": "binance", "symbol": "BTCUSDT", "at": "2026-09-01T00:00:00Z",
  "price": {"mark": 0.0},
  "oi": 0.0,
  "levels": {
    "long":  [{"from": 0.0, "to": 0.0, "dist_pct": 0.0, "notional_usd": 0.0, "share_ambiguous": 0.0, "median_age_days": 0.0}],
    "short": []
  },
  "summary": {
    "long_usd_within":  {"5": 0.0, "10": 0.0, "20": 0.0},
    "short_usd_within": {"5": 0.0, "10": 0.0, "20": 0.0},
    "asymmetry_10": 0.0
  },
  "quality": {"warmup": false, "seed_share": 0.0, "max_drift": 0.0, "gaps": [], "out_of_range_share": 0.0},
  "provenance": {"model_version": "liq/0.1.0", "params_hash": "", "events_until": "", "sources": []}
}
```

- `levels`: Cluster = zusammenhängende Buckets mit je mindestens `cluster_min_share` (Standard 0,2 %) der Seitenmasse; Top `top_n` (Standard 10) je
  Seite nach Notional.
- `share_ambiguous`: Anteil der Masse, die aus `α · A` stammt (also geschätzt statt beobachtet).
- `asymmetry_10 = (short − long) / (short + long)` innerhalb ±10 %. Positiv heißt mehr Short-Liquidität oberhalb.
- Unsicherheitsintervalle (80 %) gehören zu Teilprojekt 4, weil sie kalibrierte Parameter-Unsicherheit brauchen.
  Bis dahin steht im Snapshot nur `share_ambiguous`, ausdrücklich keine Scheingenauigkeit.

### 3.5 Simulator und Bewertung

`sim.py` erzeugt einen Markt mit bekannter Wahrheit:

- Preis: geometrische Brownsche Bewegung mit Sprüngen, Mark = Preis plus kleines Rauschen.
- Agenten öffnen und schließen Positionen (Poisson-Prozesse), Hebel aus einer *wahren* Mischung, Margin-Modus aus
  wahrem `c`, Schließ-Rate mit wahrem `β`; Liquidation, wenn Mark den Liquidationspreis kreuzt.
- Ausgabe: Event-Satz (wie 3.2, inkl. `liquidations`) plus wahres Buch `truth.csv` mit Spalten
  `ts, side, mode, price_lo, price_hi, qty` (Buckets des Engine-Gitters) je angefragtem Zeitpunkt.

`score.py` vergleicht Modell- und wahres Buch je Seite:

- `overlap` = Σ min(p_modell, p_wahr) über normierte Bucket-Verteilungen (1 = identisch).
- `liq_corr` = Rangkorrelation zwischen vorhergesagter Masse und tatsächlich liquidierter Masse in den Buckets, die
  der Mark Price im Folgeintervall erreicht hat.

**Erfolgskriterium Teilprojekt 1.** Auf 5 Simulator-Seeds mit Standard-Wahrheit: Engine mit wahren Parametern hat
höheren mittleren `overlap` als die fixe-Hebel-Baseline auf jedem Seed, und Engine mit Standardparametern (nicht
wahr) liegt im Mittel noch über der Baseline. Wird das verfehlt, ist das ein Ergebnis und wird so berichtet, nicht
weggetunt.

Grenze: Der Simulator folgt den Annahmen des Modells. Ein Sieg dort zeigt, dass die Engine richtig rechnet, nicht dass
sie die Realität trifft. Das prüft erst Teilprojekt 4.

### 3.6 Fehler und Lücken

- Fehlende OI- oder Mark-Daten in einem Intervall: keine Opens/Closes/Sweep; Masse bleibt; Intervall in
  `quality.gaps`.
- `V < |ΔOI|` (OI ändert sich mehr als gehandelt): Opens/Closes mit `A = 0`, Abweichung geloggt.
- Bekannte Lücken aus `gaps`: wie fehlende Daten.
- Nichts wird interpoliert.

### 3.7 CLI

```
python -m diamondhamster.liq simulate --seed 1 --days 30 --out <dir>
python -m diamondhamster.liq run --events <dir> [--params <toml>] [--model engine|baseline] --at <iso> [--at <iso> ...] --out <dir>
python -m diamondhamster.liq score --events <dir> --snapshots <dir>
```

`run` schreibt je `--at` eine JSON-Datei. `score` braucht ein wahres Buch (Simulator, später Hyperliquid).

### 3.8 Tests

- `margin`: Long-/Short-Formel gegen Handrechnung; Grenzfälle `L` = Tier-Maximum, `m = 0`.
- `grid`: Hin- und Rückrechnung Preis ↔ Bucket, Randbuckets.
- `book`: Invariante Masse je Seite = OI nach jedem Intervall; Sweep entfernt nur gekreuzte Buckets; Funding verschiebt
  zahlende Seite hin, empfangende weg; `β = 0` schließt proportional.
- `engine`: kein Lookahead (Snapshot bei `at` ändert sich nicht, wenn Events nach `at` angehängt werden); Lücken
  landen in `quality.gaps`.
- `snapshot`: JSON validiert gegen Schema; deterministisch bei festem Input.
- `sim` + `score`: Erfolgskriterium aus 3.5 als Test (markiert `slow`).

## 4. Schnittstellen für spätere Teilprojekte

- Teilprojekt 2 liefert nur einen Konverter Archiv → Event-Satz (3.2) und echte Tier-Tabellen. Engine unverändert.
- Teilprojekt 3 liefert zusätzlich zum Event-Satz ein wahres Buch im selben Format wie der Simulator; `score` funktioniert
  damit unverändert. Grenze: Hyperliquid-Nutzer verhalten sich nicht zwingend wie Binance-Nutzer; übertragene
  Parameter sind Hypothesen, die an Binance-Liquidationen geprüft werden.
- Teilprojekt 5 schreibt dieselben Event-Dateien laufend fort; die Engine läuft inkrementell darüber.
- Teilprojekt 4 nutzt außerdem `liquidations` aus echten Feeds. Bekannter Bias: Binance `forceOrder` meldet höchstens eine
  Liquidation pro Sekunde und Symbol; daher Bybit dazu und Untererfassung als Bias behandeln.
- Prüfstand: Snapshot-`summary` ist die Kandidaten-Datenzeile (anonymisierbar als Prozentwerte).

## 5. Offene Punkte (bewusst nicht in Teilprojekt 1)

- Ob Binance-Tiers öffentlich abrufbar sind (vermutlich nur signiert): klärt Teilprojekt 2.
- Ob `liquidationSnapshot` im Binance-Archiv noch existiert: klärt Teilprojekt 2.
- Nutzen für den Wochen-Horizont ist unbelegt; erst messbar ab Teilprojekt 4.
- Wie vollständig sich alle Hyperliquid-Positionen abfragen lassen (Rate-Limits, Adressfindung): klärt Teilprojekt 3.
