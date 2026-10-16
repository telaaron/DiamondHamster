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
  Engine mit wahren Parametern 0,73–0,79, mit Standardparametern 0,66–0,73, feste Hebel (Baseline) 0,49–0,56.
- Verlässt der Kurs das Gitter (±4× um den Startpreis), wird die betroffene Seite jedes Intervall neu gesetzt
  (`quality.reseeds` steigt, `out_of_range_share` hoch). Diese Seite ist dann bedeutungslos; ein mitwanderndes Gitter
  kommt mit echten Daten (Teilprojekt 2).
- Tier-Tabelle ist illustrativ, keine Börsendaten. Echte Tiers und Binance-Archiv folgen in Teilprojekt 2,
  Hyperliquid als echte Wahrheitsquelle in Teilprojekt 3.

## Hyperliquid-Sammler (Teilprojekt 3)

Hyperliquid ist eine Börse, deren Konten öffentlich sind. Der Sammler lernt aktive Konten aus dem Trade-Strom
(jeder Trade nennt Käufer- und Verkäufer-Adresse), fragt deren Positionen reihum ab und speichert alle 15 Minuten
das echte Liquidationsbuch. Das ist die Wahrheit, gegen die die Engine geprüft wird. Nur öffentliche Endpunkte,
kein Schlüssel, keine Orders. Läuft auf dem Mac, weil die Cloud Hyperliquid blockt.

```bash
python3 -m venv ~/.diamondhamster-venv
~/.diamondhamster-venv/bin/pip install '.[collector]'      # im Repo-Ordner; kopiert den Code in die venv
~/.diamondhamster-venv/bin/python -m diamondhamster.liq hl-collect --data ~/diamondhamster-data   # Vordergrund, Strg+C stoppt
~/.diamondhamster-venv/bin/python -m diamondhamster.liq hl-service install --data ~/diamondhamster-data
~/.diamondhamster-venv/bin/python -m diamondhamster.liq hl-service status --data ~/diamondhamster-data
```

Der Dienst startet nach Absturz und Neuanmeldung von selbst und hält den Mac im Leerlauf wach. Zugeklappt ohne
Netzteil schläft der Mac trotzdem; das steht dann als Lücke in `hl/gaps.jsonl`. Nach einem Code-Update die
`pip install`-Zeile wiederholen und `hl-service install` erneut ausführen.

`status.json`: `users` (bekannte Konten), `users_with_pos`, `coverage` (Anteil des OI, den wir kennen, je Seite;
ab etwa 0,8 taugt das Buch als Wahrheit), `polls_last_min`, `lateness_s` (wie weit der Planer hinterherhinkt),
`errors`, `ws_connected`.
