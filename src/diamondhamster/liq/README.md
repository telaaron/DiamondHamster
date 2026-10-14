# Liquidations-Engine ("eigenes Hyblock"), Teilprojekt 1

Schätzt aus öffentlichen Börsendaten, bei welchen Kursen wie viele Wetten zwangsweise geschlossen würden
(Liquidationen), getrennt nach Long (Wetten auf steigend) und Short (auf fallend). Design und Begriffe:
[`docs/superpowers/specs/2026-10-14-liq-engine-design.md`](../../../docs/superpowers/specs/2026-10-14-liq-engine-design.md).

## Befehle

```bash
# künstlicher Markt mit bekannter Lösung (14 Tage Vorlauf + 20 Tage Daten)
PYTHONPATH=src python -m diamondhamster.liq simulate --seed 1 --days 20 --out /tmp/sim
# Snapshots erzeugen (ohne --at: Zeitpunkte aus ats.json); --model baseline = feste Hebel 10/25/50/100x
PYTHONPATH=src python -m diamondhamster.liq run --events /tmp/sim --out /tmp/snap
PYTHONPATH=src python -m diamondhamster.liq run --events /tmp/sim --at 2026-01-20T00:00:00Z --out /tmp/snap
# gegen das wahre Buch bewerten (nur mit truth.csv, also Simulator, später Hyperliquid)
PYTHONPATH=src python -m diamondhamster.liq score --events /tmp/sim --snapshots /tmp/snap
```

## Was im Snapshot steht

| Feld | Bedeutung |
|---|---|
| `levels.long` / `levels.short` | Preisbänder mit viel wartender Liquidation, größtes zuerst: Band `from`–`to`, Abstand zum Kurs in % (`dist_pct`), Volumen in USD, Anteil, der aus mehrdeutigem Handel geschätzt ist (`share_ambiguous`), mittleres Alter in Tagen |
| `summary.*_usd_within` | USD-Volumen, das innerhalb von 5/10/20 % unter (Long) bzw. über (Short) dem Kurs liquidiert würde |
| `summary.asymmetry_10` | (Short − Long) / (Short + Long) innerhalb ±10 %; positiv = mehr wartende Short-Liquidationen darüber |
| `quality` | `warmup` (erste 14 Tage, Startverteilung noch geraten), `seed_share`, `max_drift`, Lücken, `reseeds`, Anteil außerhalb des Gitters |
| `provenance` | Modellversion, Parameter-Hash, Datenstand |

Nur Events mit Zeitstempel ≤ `at` gehen ein (kein Blick in die Zukunft).

## Stand und Grenzen

- Geprüft nur im Simulator. Der Simulator folgt den Annahmen des Modells; ein Sieg dort zeigt, dass richtig gerechnet
  wird, nicht dass die Karte die Realität trifft.
- Ergebnis 2026-10-14 (Überlappung der Verteilungen auf 0,1-%-Buckets, 1 = identisch, 5 Seeds, je 20 Tage):
  Engine mit wahren Parametern 0,38–0,41, mit Standardparametern 0,31–0,34, feste Hebel (Baseline) 0,21–0,25.
- Tier-Tabelle ist illustrativ, keine Börsendaten. Echte Tiers und Binance-Archiv folgen in Teilprojekt 2,
  Hyperliquid als echte Wahrheitsquelle in Teilprojekt 3.
