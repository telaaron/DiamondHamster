# Liquidations-Engine Teilprojekt 1: Implementierungsplan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ein Python-Paket `diamondhamster.liq`, das aus Event-Dateien (Trades, OI, Mark, Funding) ein Liquidationsbuch schätzt, point-in-time Snapshots als JSON ausgibt und sich auf einem Simulator mit bekannter Wahrheit gegen eine Fixe-Hebel-Baseline messen lässt.

**Architecture:** Reine Funktionen für Gitter, Liquidationsformel und Attribution; ein `Book` hält den Zustand (Seite × Modus × Kohorte × Bucket); die `Engine` schreitet von OI-Zeitpunkt zu OI-Zeitpunkt und erzwingt Massenerhaltung; `snapshot` macht daraus JSON; `sim` und `score` prüfen gegen eine bekannte Wahrheit. Baseline = dieselbe Engine mit festen Hebeln.

**Tech Stack:** Python ≥ 3.11, numpy, pandas, stdlib `tomllib`/`json`/`argparse`, pytest.

**Spec:** `docs/superpowers/specs/2026-10-14-liq-engine-design.md` (Abschnitt 3 ist maßgeblich; Formeln und Standardwerte dort).

## Global Constraints

- Keine neuen Pflicht-Abhängigkeiten außer numpy, pandas, stdlib. Kein Netzwerkzugriff in Code oder Tests.
- Zeitstempel: UTC, Millisekunden, `int`. Kohorte = UTC-Tag `ts // 86_400_000`.
- Mengen (`qty`, `oi`, Buchmasse) in Basiswährung; USD = Menge × Preis.
- Kein Lookahead: ein Snapshot bei `at` hängt nur von Events mit `ts ≤ at` ab.
- Hebelmenge: `LEVERAGES = (2, 3, 5, 10, 20, 25, 50, 75, 100, 125)`. Größenklassen nach Trade-Notional in USD: `small < 10_000 ≤ mid < 1_000_000 ≤ large`.
- Standardparameter (v001): `bucket_bp=10, max_cohorts=90, alpha=0.5, cross_share=0.3, cross_kappa=2.0, beta=0.0, warmup_days=14, drift_warn=0.05, cluster_min_share=0.002, top_n=10`.
- Gitter: log-Abstand `bucket_bp`, Bereich `[p0·0.25, p0·4]`.
- Snapshot: `schema = "liq-snapshot/1"`, `model_version = "liq/0.1.0"`.
- Tests in `tests/liq/`; langsame Tests mit `@pytest.mark.slow` (Marker in `pyproject.toml` registrieren), laufen aber im Standardlauf mit und bleiben unter 90 s gesamt.

## Review Focus

1. **Preis verlässt das Gitter** (Crash > 75 % oder Anstieg > 4×): kein Absturz; Masse im Randbucket, `quality.out_of_range_share > 0`. Test in Task 8.
2. **`at` vor dem ersten OI-Wert:** klare `ValueError("no data at or before at")`, kein leerer Snapshot. Test in Task 8.
3. **Intervall mit ΔOI ≠ 0, aber ohne Trades:** Opens nutzen den Mark-Schlusskurs als Einstieg; `A = 0`. Test in Task 8.
4. **Ganze Seite weggesweept, OI aber > 0:** Masse neu als Seed beim Mark-Preis einsetzen statt durch null zu teilen; Intervall in `quality.reseeds` zählen. Test in Task 8.
5. **Unsortierte oder doppelte Zeitstempel / negative Preise in CSV:** `EventError` mit Dateiname und Zeilennummer. Doppelte Zeitstempel sind bei `trades` erlaubt, bei `oi` und `mark` nicht. Test in Task 4.

---

### Task 1: Preisgitter

**Files:**
- Create: `src/diamondhamster/liq/__init__.py` (leer bis auf `MODEL_VERSION = "liq/0.1.0"`)
- Create: `src/diamondhamster/liq/grid.py`
- Create: `tests/liq/__init__.py`, `tests/liq/test_grid.py`

**Interfaces:**
- Produces: `class Grid(p0: float, bucket_bp: float, lo_mult: float = 0.25, hi_mult: float = 4.0)` mit Attributen `n: int`, `edges: np.ndarray` (Länge `n+1`, aufsteigend), Methoden `index(price) -> np.ndarray[int]` (geclippt auf `[0, n-1]`, akzeptiert Skalar oder Array), `in_range(price) -> np.ndarray[bool]`, `centers() -> np.ndarray` (geometrische Mitte), `shift_buckets(log_shift: float) -> int` (= `round(log_shift / ln(1 + bucket_bp/1e4))`).

- [ ] **Step 1: Tests schreiben**

```python
def test_roundtrip_center_maps_to_own_bucket():
    g = Grid(60_000, 10)
    i = np.arange(g.n)
    assert (g.index(g.centers()) == i).all()

def test_range_and_clip():
    g = Grid(100, 10)
    assert g.edges[0] == pytest.approx(25) and g.edges[-1] >= 400
    assert g.index(1.0) == 0 and g.index(10_000) == g.n - 1
    assert not g.in_range(10_000) and g.in_range(100)

def test_bucket_width_is_10bp():
    g = Grid(100, 10)
    assert g.edges[1] / g.edges[0] == pytest.approx(1.001)

def test_shift_buckets():
    assert Grid(100, 10).shift_buckets(0.0031) == 3
```

- [ ] **Step 2:** `PYTHONPATH=src pytest tests/liq/test_grid.py -v` → FAIL (ImportError)
- [ ] **Step 3:** `Grid` implementieren. `edges = lo · (1+bp/1e4)^k`, `n = ceil(ln(hi/lo)/ln(1+bp/1e4))`; `index = floor(ln(p/lo)/ln(1+bp/1e4))` geclippt.
- [ ] **Step 4:** Tests → PASS
- [ ] **Step 5:** Commit `liq: Preisgitter`

---

### Task 2: Liquidationsformel und Tiers

**Files:**
- Create: `src/diamondhamster/liq/margin.py`
- Create: `src/diamondhamster/liq/tiers/illustrativ.toml`
- Test: `tests/liq/test_margin.py`

**Interfaces:**
- Produces:
  - `@dataclass(frozen=True) class Tier: max_notional: float; max_leverage: int; mmr: float; maint_amount: float`
  - `load_tiers(path: Path) -> tuple[Tier, ...]` (sortiert nach `max_notional`; liest Schlüssel `source` und `[[tier]]`)
  - `tier_for(tiers, notional_usd: np.ndarray) -> (max_leverage: np.ndarray, mmr: np.ndarray, maint_amount: np.ndarray)` (vektorisiert, erstes Tier mit `notional ≤ max_notional`, sonst letztes)
  - `liq_price_isolated(side: str, entry, leverage, mmr, maint_amount, qty) -> np.ndarray` (Formeln aus Spec 3.3 Schritt 3; `side ∈ {"long","short"}`)
  - `liq_price_cross(side: str, entry, iso_price, kappa: float) -> np.ndarray` (Long: `entry − κ·(entry − iso)`, Short: `entry + κ·(iso − entry)`; Long-Ergebnis nach unten auf `entry·1e-6` begrenzt)

Tier-Datei (Werte konsistent: `maint_amount` kumuliert `untergrenze·Δmmr`):

```toml
source = "illustrativ, keine Börsendaten"
[[tier]]
max_notional = 50000
max_leverage = 125
mmr = 0.004
maint_amount = 0
[[tier]]
max_notional = 250000
max_leverage = 100
mmr = 0.005
maint_amount = 50
[[tier]]
max_notional = 3000000
max_leverage = 50
mmr = 0.01
maint_amount = 1300
[[tier]]
max_notional = 1e15
max_leverage = 20
mmr = 0.025
maint_amount = 46300
```

- [ ] **Step 1: Tests schreiben**

```python
def test_long_short_isolated_by_hand():
    assert liq_price_isolated("long", 100.0, 10, 0.004, 0.0, 1.0) == pytest.approx(90.0 / 0.996)
    assert liq_price_isolated("short", 100.0, 10, 0.004, 0.0, 1.0) == pytest.approx(110.0 / 1.004)

def test_maint_amount_moves_liq_away():
    a = liq_price_isolated("long", 100.0, 20, 0.01, 0.0, 1.0)
    b = liq_price_isolated("long", 100.0, 20, 0.01, 5.0, 1.0)
    assert b < a  # Wartungsbetrag senkt die nötige Marge, Long-Liq rückt weiter weg
```

```python
def test_cross_is_farther():
    iso = liq_price_isolated("long", 100.0, 10, 0.004, 0.0, 1.0)
    assert liq_price_cross("long", 100.0, iso, 2.0) == pytest.approx(100 - 2 * (100 - iso))
    assert liq_price_cross("long", 100.0, 1.0, 5.0) > 0

def test_tier_lookup_vectorized(tmp_path):
    tiers = load_tiers(TIERS_PATH)
    lev, mmr, k = tier_for(tiers, np.array([1_000, 50_000, 60_000, 1e9]))
    assert list(lev) == [125, 125, 100, 20] and mmr[-1] == 0.025 and k[2] == 50
```

- [ ] **Step 2:** Tests → FAIL
- [ ] **Step 3:** `margin.py` implementieren (Formeln Spec 3.3 Schritt 3).
- [ ] **Step 4:** Tests → PASS
- [ ] **Step 5:** Commit `liq: Liquidationsformel und Tiers`

---

### Task 3: Parameter

**Files:**
- Create: `src/diamondhamster/liq/params.py`, `src/diamondhamster/liq/params/v001.toml`
- Modify: `pyproject.toml` (package-data für `*.toml` unter `diamondhamster.liq`; pytest-Marker `slow`)
- Test: `tests/liq/test_params.py`

**Interfaces:**
- Consumes: `Tier`, `load_tiers` (Task 2)
- Produces:
  - `LEVERAGES: tuple[int, ...]`, `SIZE_CLASSES = ("small", "mid", "large")`, `size_class(notional_usd: np.ndarray) -> np.ndarray[str]`
  - `@dataclass(frozen=True) class Params` mit Feldern `bucket_bp, max_cohorts, alpha, cross_share, cross_kappa, beta, warmup_days, drift_warn, cluster_min_share, top_n` (Werte aus Global Constraints), `leverage_weights: dict[str, np.ndarray]` (je Klasse Länge `len(LEVERAGES)`, Summe 1), `tiers: tuple[Tier, ...]`, `params_hash: str`
  - `load_params(path: Path | None = None) -> Params` (None = `v001.toml`; `tiers` ist Pfad relativ zur Params-Datei; Gewichte werden normiert; Hash = SHA-256 über die Bytes der Params-Datei plus der Tier-Datei, hex, erste 16 Zeichen)
  - `with_overrides(p: Params, **kw) -> Params` (`dataclasses.replace`, Hash bekommt Suffix `+override`)

`v001.toml` Hebelgewichte (Reihenfolge wie `LEVERAGES`):
- small: `[2, 3, 8, 20, 20, 12, 15, 7, 10, 3]`
- mid: `[5, 8, 15, 30, 20, 10, 8, 2, 2, 0]`
- large: `[15, 15, 25, 30, 10, 5, 0, 0, 0, 0]`

- [ ] **Step 1: Tests**

```python
def test_defaults_loaded():
    p = load_params()
    assert (p.bucket_bp, p.alpha, p.cross_share, p.cross_kappa, p.beta) == (10, 0.5, 0.3, 2.0, 0.0)
    assert all(w.sum() == pytest.approx(1) for w in p.leverage_weights.values())
    assert len(p.tiers) == 4 and len(p.params_hash) == 16

def test_size_class_thresholds():
    assert list(size_class(np.array([9_999, 10_000, 999_999, 1_000_000]))) == ["small", "mid", "mid", "large"]

def test_hash_changes_with_file(tmp_path): ...  # Kopie von v001 mit alpha=0.6 → anderer Hash
```

- [ ] **Step 2–4:** FAIL → implementieren → PASS
- [ ] **Step 5:** Commit `liq: Parameter v001`

---

### Task 4: Events

**Files:**
- Create: `src/diamondhamster/liq/events.py`
- Test: `tests/liq/test_events.py`

**Interfaces:**
- Produces:
  - `class EventError(ValueError)`
  - `@dataclass class EventSet: exchange: str; symbol: str; trades: pd.DataFrame; oi: pd.DataFrame; mark: pd.DataFrame; funding: pd.DataFrame; liquidations: pd.DataFrame; gaps: pd.DataFrame` (Spalten exakt wie Spec 3.2)
  - `COLUMNS: dict[str, list[str]]` mit den Spalten je Typ
  - `load_events(directory: Path) -> EventSet` (liest `meta.json` mit `exchange`, `symbol` und `<typ>.csv`; fehlende `funding`, `liquidations`, `gaps` → leere Frames; fehlende `trades`, `oi`, `mark` → `EventError`); ruft `validate`
  - `save_events(es: EventSet, directory: Path) -> None`
  - `validate(es: EventSet) -> None`
  - `EventSet.until(ts_ms: int) -> EventSet` (alle Typen auf `ts ≤ ts_ms`; `gaps` auf `start ≤ ts_ms`)

Validierungsregeln: Spalten vorhanden; `ts` monoton nicht fallend (`trades`, `funding`, `liquidations`) bzw. streng steigend (`oi`, `mark`); `price`, `high`, `low`, `close`, `oi` > 0; `qty` > 0; `low ≤ close ≤ high`; `side ∈ {long, short}`. Fehlermeldung enthält `<typ>.csv` und 1-basierte Datenzeile.

- [ ] **Step 1: Tests**

```python
def test_roundtrip(tmp_path): ...  # save → load → frames gleich (pd.testing.assert_frame_equal)
def test_until_filters_everything(tmp_path): ...  # nach until(t) max ts ≤ t in allen Frames
def test_unsorted_oi_names_file_and_row(tmp_path):
    # oi.csv mit ts [1000, 3000, 2000]
    with pytest.raises(EventError, match=r"oi\.csv.*Zeile 3"):
        load_events(d)
def test_duplicate_trade_ts_ok_duplicate_mark_ts_not(tmp_path): ...
def test_negative_price_rejected(tmp_path): ...
```

- [ ] **Step 2–4:** FAIL → implementieren → PASS
- [ ] **Step 5:** Commit `liq: Event-Format und Validierung`

---

### Task 5: Attribution (Opens, Closes, Liquidationspreis-Ablage)

**Files:**
- Create: `src/diamondhamster/liq/attribution.py`
- Test: `tests/liq/test_attribution.py`

**Interfaces:**
- Consumes: `Params`, `LEVERAGES`, `size_class` (Task 3); `tier_for`, `liq_price_isolated`, `liq_price_cross` (Task 2)
- Produces:
  - `opens_closes(volume: float, d_oi: float, alpha: float) -> tuple[float, float, float]` → `(opens_per_side, closes_per_side, ambiguous_per_side)` mit `A = max(V − |ΔOI|, 0)`, `opens = max(ΔOI,0) + α·A/2`, `closes = max(−ΔOI,0) + α·A/2`, `ambiguous = α·A/2`
  - `@dataclass class Deposit: side: str; mode: str; liq_price: np.ndarray; qty: np.ndarray`
  - `deposits(prices: np.ndarray, qtys: np.ndarray, open_qty: float, params: Params, force_class: str | None = None) -> list[Deposit]` → genau 4 Deposits (`force_class` setzt die Größenklasse für alle Trades, für den Seed) (long/short × isolated/cross). Jeder Trade `i` bekommt `open_qty · qtys[i]/Σqtys` als Einstiegsmenge; Notional für Größenklasse und Tier = `prices[i]·qtys[i]`; Gewichte `leverage_weights[klasse]`, Hebel über `max_leverage` des Tiers auf 0 und je Trade renormiert (bleibt nichts übrig: ganze Menge auf den größten erlaubten Hebel); isoliert × `(1−cross_share)`, cross × `cross_share`, cross mit `cross_kappa`. Ausgabe-Arrays flach (Trades × Hebel).

- [ ] **Step 1: Tests**

```python
def test_opens_closes_cases():
    assert opens_closes(10, 4, 0.5) == pytest.approx((4 + 1.5, 1.5, 1.5))
    assert opens_closes(10, -4, 0.5) == pytest.approx((1.5, 4 + 1.5, 1.5))
    assert opens_closes(2, 5, 0.5) == pytest.approx((5, 0, 0))  # V < |ΔOI|

def test_deposits_conserve_mass():
    p = load_params()
    ds = deposits(np.array([100.0, 101.0]), np.array([1.0, 3.0]), 2.0, p)
    for side in ("long", "short"):
        assert sum(d.qty.sum() for d in ds if d.side == side) == pytest.approx(2.0)
    assert sum(d.qty.sum() for d in ds if d.mode == "cross") == pytest.approx(2 * 2.0 * 0.3)

def test_long_below_short_above():
    ds = deposits(np.array([100.0]), np.array([1.0]), 1.0, load_params())
    assert all((d.liq_price < 100).all() for d in ds if d.side == "long")
    assert all((d.liq_price > 100).all() for d in ds if d.side == "short")

def test_tier_caps_leverage():
    # ein Trade mit Notional 5e6 (Tier max 20x): kein Deposit-Preis näher als 1/20 am Einstieg
```

- [ ] **Step 2–4:** FAIL → implementieren → PASS
- [ ] **Step 5:** Commit `liq: Attribution`

---

### Task 6: Book

**Files:**
- Create: `src/diamondhamster/liq/book.py`
- Test: `tests/liq/test_book.py`

**Interfaces:**
- Consumes: `Grid` (Task 1), `Deposit` (Task 5)
- Produces: `class Book(grid: Grid, max_cohorts: int)` mit
  - `SEED = -1` (Kohorten-Schlüssel für Startmasse)
  - `add(deposit: Deposit, cohort: int, ambiguous_frac: float) -> None` (Bucket per `grid.index`, Preise außerhalb zählen in `out_of_range_qty`; `ambiguous_frac` Anteil wird zusätzlich in der parallelen Ambiguous-Matrix gebucht)
  - `sweep(mark_low: float, mark_high: float) -> dict[str, float]` (entfernt Long-Masse mit effektivem Preis ≥ `mark_low`, Short-Masse mit effektivem Preis ≤ `mark_high`; effektiver Preis = Bucket + `shift_buckets(funding_shift)` nur für `isolated`)
  - `close(side: str, qty: float, today: int, beta: float) -> None` (Kohortengewicht `masse·exp(β·(today − kohorte))`, Seed-Alter = `today − start_day`; innerhalb einer Kohorte proportional über Buckets; nie negativ; entfernt `min(qty, total)`)
  - `apply_funding(rate: float) -> None` (`funding_shift[kohorte] += rate` für alle bestehenden Kohorten, wirkt nur auf `isolated`, beide Seiten gleiches Vorzeichen; siehe Spec 3.3 Schritt 6: zahlende Seite rückt hin, empfangende weg, beides ist eine Verschiebung um `+rate` in log-Preis)
  - `total(side: str) -> float`, `scale(side: str, factor: float) -> None`
  - `merge_old(today: int) -> None` (mehr als `max_cohorts` Kohorten → älteste zusammenlegen; Funding-Shift massengewichtet mitteln)
  - `distribution(side: str) -> np.ndarray` (Länge `grid.n`, effektive Buckets, Summe über Modi und Kohorten), `ambiguous_distribution(side) -> np.ndarray`, `age_distribution(side: str, today: int) -> np.ndarray` (massengewichtetes mittleres Alter je Bucket in Tagen)
  - `seed_share() -> float`, `out_of_range_share() -> float`

Hinweis Spec-Abgleich: In Spec 3.3 Schritt 6 steht "zahlende Seite hin, empfangende weg". Bei `rate > 0` zahlen Longs: Long-Liq (unter dem Preis) steigt → hin; Short-Liq (über dem Preis) steigt → weg. Bei `rate < 0` umgekehrt. Beides = `+rate`. Diese Ableitung als Kommentar in `apply_funding`.

- [ ] **Step 1: Tests**

```python
def test_sweep_only_crossed():
    # Long-Masse bei 90 und 80, sweep(mark_low=85, mark_high=110) → entfernt 90, behält 80; Rückgabe long == Masse bei 90
def test_close_beta_zero_proportional():
    # zwei Kohorten 1.0 und 3.0, close 2.0 → 0.5 und 1.5
def test_close_beta_positive_prefers_old(): ...
def test_close_never_negative(): # close mehr als total → total == 0, kein negativer Wert
def test_funding_shifts_isolated_only():
    # isolated und cross je bei 90; apply_funding(+0.003) → isolated-Verteilung 3 Buckets höher, cross unverändert
def test_scale_and_total(): ...
def test_merge_old_keeps_mass(): ...
def test_ambiguous_tracks_add_and_close(): # ambiguous_distribution schrumpft proportional mit close
```

- [ ] **Step 2–4:** FAIL → implementieren → PASS
- [ ] **Step 5:** Commit `liq: Book`

---

### Task 7: Snapshot

**Files:**
- Create: `src/diamondhamster/liq/snapshot.py`
- Test: `tests/liq/test_snapshot.py`

**Interfaces:**
- Consumes: `Book`, `Grid`, `Params`, `MODEL_VERSION`
- Produces:
  - `@dataclass class Snapshot: data: dict; dist: dict[str, np.ndarray]; edges: np.ndarray` mit `to_json() -> str` (sortierte Schlüssel, `indent=2`) und `save(directory: Path) -> None` (schreibt `<at>.json` und `<at>.npz` mit `long`, `short`, `edges`; Dateiname `at` als `YYYYMMDDTHHMMZ`)
  - `build_snapshot(book: Book, params: Params, *, exchange: str, symbol: str, at_ms: int, mark: float, oi: float, quality: dict, sources: list[str], events_until_ms: int) -> Snapshot` (JSON exakt nach Spec 3.4)
  - `find_clusters(dist, amb, ages, grid, mark, side, min_share, top_n) -> list[dict]` (zusammenhängende Buckets mit `dist ≥ min_share·dist.sum()`; Felder `from, to, dist_pct, notional_usd, share_ambiguous, median_age_days`; `dist_pct` vom Mark zur Cluster-Mitte, Long negativ, Short positiv; sortiert nach `notional_usd` absteigend; `median_age_days` = massengewichteter Mittelwert von `ages` im Cluster, Feldname bleibt wie Spec)
  - `validate_snapshot(d: dict) -> None` (prüft Pflichtschlüssel und Typen der Spec 3.4, `AssertionError` sonst)

`summary`: Long-USD mit Liq-Preis in `[mark·(1−x), mark]`, Short in `[mark, mark·(1+x)]` für `x ∈ {0.05, 0.10, 0.20}`, Schlüssel `"5"`, `"10"`, `"20"`; USD = Menge × Bucket-Mitte; `asymmetry_10 = (short − long)/(short + long)`, 0 wenn beide 0. `quality` übernimmt das übergebene Dict und ergänzt `seed_share`, `out_of_range_share`.

- [ ] **Step 1: Tests**

```python
def test_schema_valid_and_deterministic(): # zweimal bauen → identischer to_json()
def test_clusters_threshold_and_order(): # zwei Blöcke 3 und 1 Einheiten → 2 Cluster, größter zuerst
def test_summary_within_and_asymmetry(): # Long 1 BTC bei 0.97·mark, Short 2 BTC bei 1.15·mark
    # long_usd_within["5"] ≈ 0.97·mark, short_usd_within["10"] == 0, ["20"] ≈ 2·1.15·mark
def test_save_writes_json_and_npz(tmp_path): ...
```

- [ ] **Step 2–4:** FAIL → implementieren → PASS
- [ ] **Step 5:** Commit `liq: Snapshot-JSON`

---

### Task 8: Engine und Baseline

**Files:**
- Create: `src/diamondhamster/liq/engine.py`, `src/diamondhamster/liq/baseline.py`
- Test: `tests/liq/test_engine.py`

**Interfaces:**
- Consumes: alles aus Tasks 1–7
- Produces:
  - `class Engine(params: Params)` mit `run(events: EventSet, at_ms: list[int]) -> list[Snapshot]`
  - `baseline_params(p: Params) -> Params` = `with_overrides(p, leverage_weights={k: Gewichte 0.25 auf 10/25/50/100, sonst 0}, cross_share=0.0, alpha=0.0)`

Ablauf `run` (Spec 3.3; Reihenfolge verbindlich):
1. `at_ms` sortieren; frühestes `at` vor erstem OI-`ts` → `ValueError("no data at or before at")`.
2. Erster OI-Punkt: `p0` = erster Mark-`close` mit `ts ≤` OI-`ts`, sonst erster Trade-Preis. `Grid(p0, bucket_bp)`, `Book`. Seed: `deposits([p0], [1.0], oi_0, params, force_class="mid")` in Kohorte `Book.SEED`.
3. Je Folge-OI-Punkt `i`: Intervall `(t_{i−1}, t_i]`.
   - Lücke, wenn kein Mark-Event im Intervall oder Überschneidung mit `gaps` → nur Funding anwenden, Intervall in `quality.gaps` als `[start_iso, end_iso]`, weiter.
   - `opens_closes(Σqty, ΔOI, alpha)`; Einstiegspreise = Trades im Intervall, ohne Trades = letzter Mark-`close` mit Menge 1.
   - `book.add(...)` für jedes Deposit mit Kohorte = Tag von `t_i`, `ambiguous_frac = ambiguous/opens` (0 wenn `opens == 0`).
   - `swept = book.sweep(min(low), max(high))` über Mark-Events im Intervall.
   - Je Seite `book.close(side, max(closes − swept[side], 0), tag, beta)`.
   - Funding-Events im Intervall: `book.apply_funding(rate)`.
   - Massenerhaltung: Seite mit `total == 0` und `oi_i > 0` → Seed-Deposit beim letzten Mark-`close` in die aktuelle Kohorte, `quality.reseeds += 1`; sonst `factor = oi_i/total`, `book.scale`, `max_drift = max(max_drift, |1 − factor|)`.
   - `book.merge_old(tag)`.
   - Für jedes `at` mit `t_i ≤ at < t_{i+1}` (bzw. letztes): Snapshot bauen mit `mark` = letzter Mark-`close ≤ at`, `oi = oi_i`, `quality = {"warmup": at < start + warmup_days, "max_drift", "drift_warning": max_drift > drift_warn, "gaps", "reseeds"}`, `sources = [f"{exchange}:{symbol}"]`, `events_until_ms = t_i`.

- [ ] **Step 1: Tests** (Hilfsfunktion `make_events(...)` in `tests/liq/conftest.py` baut kleine `EventSet`s)

```python
def test_mass_equals_oi_after_every_interval(): # über 50 Intervalle mit Zufallstrades, je Snapshot: Σ dist[long]·1 == oi (rel 1e-9), dito short
def test_no_lookahead(): # Snapshot bei at identisch, wenn Events nach at angehängt werden
def test_at_before_first_oi_raises():
    with pytest.raises(ValueError, match="no data at or before at"): Engine(load_params()).run(es, [es.oi.ts.min() - 1])
def test_gap_recorded_and_book_frozen(): # Intervall ohne Mark → quality.gaps nicht leer, dist vor/nach gleich bis auf Funding
def test_no_trades_uses_mark_close(): # ΔOI>0, keine Trades → neue Masse um Mark-close verteilt
def test_price_crash_out_of_range(): # Mark fällt auf 0.2·p0 → kein Fehler, out_of_range_share > 0
def test_full_sweep_reseeds(): # Mark-Spanne deckt alles → quality.reseeds ≥ 1, Masse == OI
def test_baseline_only_four_leverages(): # baseline_params → Gewichte nur bei 10/25/50/100, cross_share 0
```

- [ ] **Step 2–4:** FAIL → implementieren → PASS
- [ ] **Step 5:** Commit `liq: Engine und Fixe-Hebel-Baseline`

---

### Task 9: Simulator

**Files:**
- Create: `src/diamondhamster/liq/sim.py`
- Test: `tests/liq/test_sim.py`

**Interfaces:**
- Consumes: `LEVERAGES`, `size_class`, `Params` (Task 3); `tier_for`, `liq_price_isolated`, `liq_price_cross` (Task 2); `EventSet`, `save_events` (Task 4)
- Produces:
  - `@dataclass(frozen=True) class SimTruth: leverage_weights: dict[str, np.ndarray]; cross_share: float = 0.25; cross_kappa: float = 2.5; beta: float = 0.05; transfer_share: float = 0.5; open_rate: float = 10.0; close_rate: float = 8.0; p_start: float = 60_000.0; daily_vol: float = 0.03; jump_per_day: float = 1.0; jump_size: float = 0.05; qty_mu: float = -1.0; qty_sigma: float = 1.5; funding_abs: float = 0.0001`
  - `DEFAULT_TRUTH: SimTruth` mit Gewichten small `[1, 2, 5, 15, 25, 15, 20, 7, 8, 2]`, mid `[3, 5, 12, 35, 25, 10, 7, 2, 1, 0]`, large `[20, 20, 25, 25, 7, 3, 0, 0, 0, 0]` (bewusst ≠ v001)
  - `truth_params(base: Params, truth: SimTruth) -> Params` (überschreibt `leverage_weights, cross_share, cross_kappa, beta`, `alpha = truth.transfer_share` als Näherung, weil im 5-min-Intervall auch Opens und Closes gegeneinander netten)
  - `simulate(seed: int, days: int, truth: SimTruth = DEFAULT_TRUTH, pre_days: int = 14, snapshot_every_h: int = 24, tiers_path: Path | None = None) -> tuple[EventSet, pd.DataFrame, list[int]]` → Events (nur nach `pre_days`), Wahrheit (`ts, side, mode, liq_price, qty`, je Snapshot-Zeitpunkt alle offenen Positionen), Snapshot-Zeitpunkte
  - `write_sim(directory: Path, events, truth, ats) -> None` (`save_events` + `truth.csv` + `ats.json`)

Ablauf je 5-Minuten-Schritt (bestimmt nicht durch Signaturen, daher hier):
1. Preis: 5 Teilschritte GBM mit `σ = daily_vol/sqrt(288·5)`, Sprung mit Wahrscheinlichkeit `jump_per_day/288` um `±jump_size`; Mark = Preis·(1 + N(0, 1e-4)); Mark-Event `high/low/close` der Teilschritte.
2. Liquidation: offene Positionen, deren Liq-Preis im Mark-Bereich liegt, schließen; Menge als `liquidations`-Event (Seite, Liq-Preis); Gegenseite um dieselbe Menge reduziert (Gewicht nach Hazard, s. 4).
3. Opens: `Poisson(open_rate)` Paare; Menge `lognormal(qty_mu, qty_sigma)`; Long und Short eröffnen dieselbe Menge zum aktuellen Preis; je Position Hebel aus `truth.leverage_weights[size_class]` gekappt durch Tier, Modus cross mit `cross_share`; Liq-Preis über `margin`-Funktionen.
4. Closes je Seite: `Poisson(close_rate)` Ereignisse; Position gewählt mit Gewicht `qty·exp(beta·alter_tage)`; mit Wahrscheinlichkeit `transfer_share` eröffnet derselbe Seite eine neue Position gleicher Menge (ΔOI 0), sonst schließt die Gegenseite dieselbe Menge (Reduktion nie negativ, Summe exakt).
5. Jede Bewegung aus 2–4 erzeugt einen Trade (`ts` gleichverteilt im Schritt, Preis = aktueller Preis, `taker_buy` zufällig).
6. OI-Event am Schrittende = Summe Long (assert == Summe Short).
7. Funding alle 8 h mit `rate = ±funding_abs` (Vorzeichen zufällig); isolierte Liq-Preise aller Positionen ×`exp(rate)`.

- [ ] **Step 1: Tests**

```python
def test_sim_is_deterministic(): # gleicher seed → identische Frames
def test_sim_oi_long_equals_short(): # implizit über assert im Sim; zusätzlich Wahrheit: Σ long == Σ short == letzter OI vor ts
def test_sim_events_validate(): # validate(events) wirft nicht
def test_sim_liquidations_inside_mark_range(): # jede Liquidation liegt in [low, high] eines Mark-Events desselben Schritts
```

- [ ] **Step 2–4:** FAIL → implementieren → PASS (`simulate(1, 3)` unter 5 s)
- [ ] **Step 5:** Commit `liq: Simulator mit bekannter Wahrheit`

---

### Task 10: Bewertung und Erfolgskriterium

**Files:**
- Create: `src/diamondhamster/liq/score.py`
- Test: `tests/liq/test_score.py`

**Interfaces:**
- Consumes: `Snapshot` (Task 7), `Engine`, `baseline_params` (Task 8), `simulate`, `truth_params`, `DEFAULT_TRUTH` (Task 9)
- Produces:
  - `overlap(p: np.ndarray, q: np.ndarray) -> float` (beide normiert, `Σ min`; 0 wenn eine Summe 0)
  - `truth_dist(truth: pd.DataFrame, ts: int, edges: np.ndarray, side: str) -> np.ndarray` (Positionsmengen auf die Kanten binnen, außerhalb in Randbuckets)
  - `liq_corr(snap: Snapshot, events: EventSet, horizon_ms: int = 86_400_000) -> float` (Buckets, die der Mark in `(at, at+horizon]` erreicht hat; Spearman zwischen vorhergesagter Masse und gemeldetem Liquidationsvolumen dort; `nan` bei < 5 Buckets)
  - `score_snapshots(snaps: list[Snapshot], truth: pd.DataFrame, events: EventSet) -> dict` mit `overlap_long, overlap_short, overlap, liq_corr` (Mittel über Snapshots mit `quality.warmup == False`)

- [ ] **Step 1: Tests**

```python
def test_overlap_bounds():
    assert overlap(np.array([1, 0]), np.array([1, 0])) == 1 and overlap(np.array([1, 0]), np.array([0, 1])) == 0

@pytest.mark.slow
def test_engine_beats_fixed_leverage_on_sim():
    base = load_params()
    res = {"true": [], "default": [], "baseline": []}
    for seed in range(1, 6):
        ev, truth, ats = simulate(seed, days=20)
        for name, p in (("true", truth_params(base, DEFAULT_TRUTH)), ("default", base), ("baseline", baseline_params(base))):
            res[name].append(score_snapshots(Engine(p).run(ev, ats), truth, ev)["overlap"])
    assert all(t > b for t, b in zip(res["true"], res["baseline"]))
    assert np.mean(res["default"]) > np.mean(res["baseline"])
```

- [ ] **Step 2–4:** FAIL → implementieren → PASS. **Wenn der langsame Test rot bleibt, obwohl alle Unit-Tests grün sind: nicht an Parametern drehen, bis er grün wird.** Ergebnis notieren (Werte je Seed) und an Aaron berichten (Spec 3.5).
- [ ] **Step 5:** Commit `liq: Bewertung und Simulator-Erfolgskriterium`

---

### Task 11: CLI und Kurzdoku

**Files:**
- Create: `src/diamondhamster/liq/__main__.py`, `src/diamondhamster/liq/README.md`
- Test: `tests/liq/test_cli.py`

**Interfaces:**
- Consumes: alles Vorige
- Produces: `main(argv: list[str] | None = None) -> int` mit Unterbefehlen exakt wie Spec 3.7:
  - `simulate --seed N --days N --out DIR` → `write_sim`
  - `run --events DIR [--params TOML] [--model engine|baseline] --at ISO [--at ISO ...] --out DIR` → je `at` `Snapshot.save`; ohne `--at`, aber mit `ats.json` im Events-Ordner → diese Zeitpunkte
  - `score --events DIR --snapshots DIR` → liest `truth.csv`, `*.npz`, `*.json`; gibt `score_snapshots`-Dict als JSON auf stdout aus; ohne `truth.csv` → Exit 2 mit Meldung "score braucht ein wahres Buch (truth.csv)"

README (Deutsch, kurz, einfache Sprache wie Spec Abschnitt 0): was die Engine tut, die drei Befehle mit Beispiel, was ein Snapshot-Feld bedeutet, Grenzen (nur Simulator geprüft).

- [ ] **Step 1: Test**

```python
def test_cli_end_to_end(tmp_path, capsys):
    assert main(["simulate", "--seed", "1", "--days", "3", "--out", str(tmp_path / "ev")]) == 0
    assert main(["run", "--events", str(tmp_path / "ev"), "--out", str(tmp_path / "snap")]) == 0
    assert list((tmp_path / "snap").glob("*.json"))
    assert main(["score", "--events", str(tmp_path / "ev"), "--snapshots", str(tmp_path / "snap")]) == 0
    assert "overlap" in json.loads(capsys.readouterr().out)
```

- [ ] **Step 2–4:** FAIL → implementieren → PASS
- [ ] **Step 5:** Gesamtlauf `PYTHONPATH=src pytest -q` (alle Tests im Repo, nicht nur `tests/liq`) → alles grün
- [ ] **Step 6:** Commit `liq: CLI und Kurzdoku`
