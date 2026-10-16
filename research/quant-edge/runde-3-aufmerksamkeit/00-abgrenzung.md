# Runde 3, Phase 0: Abgrenzung (verbindlich, 2026-10-16)

Geschrieben vor jedem Datenabruf und vor jeder eigenen Rechnung. Abweichungen nur als datierter Nachtrag unten.

Kennzeichnung: (G) gerechnet, (S) geschätzt mit Herleitung, (L) Literatur.

## Hypothese

Alle haben die Information, aber nicht alle verarbeiten sie. In Märkten, die für Profi-Kapazität zu klein sind, wird öffentliche, schwer lesbare Information langsamer eingepreist; eine KI erntet das durch Lesen, nicht durch Schnelligkeit.

Software-Analogie: Der Markt ist ein Cache mit langer Invalidierung. Wer die Quelle (das Dokument) selbst liest, sieht den neuen Wert, bevor der Cache (der Kurs) aktualisiert ist. Lohnend nur dort, wo niemand mit großem Durchsatz den Cache schon invalidiert.

## Nicht getestet (vorab tot)

- Alles, was "schneller als" voraussetzt: Schlagzeilen-Reaktion, Breaking News, Earnings-Sekunden, Listing-Ankündigung in der ersten Minute. Grund aus Runde 1: dort gewinnt Latenz (Axiom 2), wir haben keine.
- Praktische Regel: Einstieg frühestens **eine volle Stunde nach dem Zeitstempel der Erstveröffentlichung**, bei Tagesdaten am Schluss des Folgetags. Was nach dieser Verzögerung nicht mehr da ist, gehört uns nicht.

## Getestet nur, wenn alle drei gelten

1. **Öffentlich:** kostenlos und ohne Login lesbar, mit Zeitstempel der erstmaligen Verfügbarkeit (Phase 2).
2. **Schwer zu lesen oder zu verknüpfen:** langes Dokument, technischer Inhalt, oder die Wirkung liegt bei einem anderen Asset als dem genannten.
3. **Kleines Asset:** mittleres Tagesvolumen (30 Tage vor dem Ereignis, nur Vergangenheit) **unter 50 Mio USD**.

## Schwelle 50 Mio USD/Tag: Herleitung (S)

Frage: Ab welchem Tagesvolumen V lohnt sich ein Ereignis-Edge für einen Profi-Desk nicht mehr, weil sein eigener Markteinfluss den Gewinn frisst?

Wurzelgesetz aus Runde 1: Kosten pro Seite ≈ σ · √(Q/V), σ = Tagesvolatilität, Q = Ordergröße.
Gewinn pro Ereignis bei Prämie p: Q · (p − 2σ√(Q/V)). Maximum bei √(Q/V) = p/(3σ):

- optimale Größe Q* = V · p² / (9σ²)
- maximaler Gewinn pro Ereignis = V · p³ / (27σ²)

Eingesetzt mit p = 2 % (Größenordnung der Drift-Literatur, Phase 1 prüft das) und σ = 5 % Tagesvol (typisch kleiner Token):
Gewinn pro Ereignis ≈ V · 1,2·10⁻⁴. Bei V = 50 Mio: ~5 900 USD pro Ereignis; bei 50 Ereignissen pro Jahr ~0,3 Mio USD/Jahr.

Ein Quant-Team mit Daten, Leuten und Infrastruktur kostet grob 1 bis 2 Mio USD/Jahr (S, Branchenschätzung, nicht gemessen). Unter V ≈ 50 Mio deckt selbst der Optimalfall die Fixkosten nicht; die Schwelle ist damit eher konservativ (bei 100 Ereignissen/Jahr läge der Profi-Break-even erst bei ~125 Mio). 50 Mio bleibt der Startwert, weil kleinere Schwellen die Ereigniszahl zu stark drücken würden.

Für uns: Kapital 25 000 USD (Default aus Runde 2) liegt weit unter Q* (bei V = 50 Mio ≈ 0,9 Mio USD), unser Impact ist also vernachlässigbar, der Spread nicht. Kosten deshalb: gemessener Spread plus 0,2 % pro Seite.

Grenzen der Herleitung: Konstante im Wurzelgesetz = 1 angenommen; Spread nicht in Q* enthalten; Profi-Fixkosten geschätzt.

## Gegenparteien (ohne benannte Gegenpartei kein Test)

| Gegenpartei | Warum begrenzte Aufmerksamkeit | Warum sie das nicht ändern kann |
|---|---|---|
| Privatanleger in kleinen Token | lesen Kalender, Foren, Verträge nicht | Zeit; Lesen kostet Stunden pro Token, ihr Einsatz ist zu klein, um das zu bezahlen |
| Fonds mit Mindestgröße | dürfen/wollen kleine Assets nicht halten | Mandat und Impact: Positionen < Q* lohnen den Analystenaufwand nicht |
| Index- und Korb-Halter | reagieren erst beim Rebalancing | Regelwerk: Gewichte ändern sich nur zu festen Terminen |
| Empfänger mit Vesting (VCs, Team) bei Unlocks | haben Verkaufsdruck nach Termin | Liquiditätsbedarf und Fondslaufzeit; Termin steht im Vertrag |

Warnung zur letzten Zeile: Unlock-Empfänger sind oft die *informierte* Seite (sie können vorher per Perp absichern). Dann ist die Gegenpartei der Privatanleger, der vor dem Termin kauft; das muss Phase 3 klären.

## Look-ahead-Grenze durch das lesende Modell

- Leser = Claude-Subagents in diesem Projekt (kein externes LLM-API). Trainingswissen bis ca. Juni 2026.
- Forschungsprotokoll §6/§11: KI-Tests zählen nur auf Daten **nach** dem Cutoff, also ab 2026-07-01, plus Forward-Test.
- Pseudonymisierung (Namen, Ticker, Daten entfernt) ist Pflicht, aber nur zweite Verteidigungslinie: Ein langes Dokument bleibt oft wiedererkennbar. Vor dem Cutoff gelesene Dokumente zählen höchstens als Diagnose, nie als Beweis.
- Folge: Kandidaten mit KI-Leser (A2, A3) haben nur ~3,5 Monate saubere Historie. Regel-Kandidaten ohne KI (A1 Unlocks) sind historisch testbar, mit Regel-Holdout 2025-01 bis 2026-06 einmalig.

## Datenfenster (wie Runde 1)

- Entwicklung: bis 2024-12-31.
- Regel-Holdout 2025-01-01 bis 2026-06-30: nicht geladen; jeder Abruf, der hineinreicht, wird geloggt (Wächter B-19/B-21).
- Ab 2026-07-01: Dev-Nachschau, für KI-Kandidaten das einzige saubere Fenster.

## Nachträge

(keine)
