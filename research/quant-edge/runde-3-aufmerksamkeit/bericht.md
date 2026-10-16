# Quant-Edge Runde 3: Aufmerksamkeits-Prämie – Bericht

Stand 2026-10-16. Kennzeichnung: (G) gerechnet, (S) geschätzt mit Herleitung, (L) Literatur.

## Antwort vorweg

1. **Keine erntbare Aufmerksamkeits-Prämie gefunden.** Im einzigen messbaren Test (8-K-Meldungen kleiner US-Firmen, KI liest blind, 5 Tage halten) liegt die Überrendite brutto bei +1,9 % je Trade (p 0,06, n 156), netto nach gemessenem Spread und 0,2 % je Seite bei −0,3 % (G).
2. Die Kosten (≈ 2,2 % pro Runde, davon ⅔ Spread) sind so groß wie die ganze Brutto-Prämie. Das deckt sich mit der Literatur: Die Prämie lebt nur in illiquiden Titeln, und dort frisst der Spread 70 bis 100 % davon (L, Chordia u. a. 2009).
3. Die KI liest korrekt (20 von 20 Belegen wörtlich, 17 von 20 Richtungen inhaltlich begründet), aber ihr Tiefenlesen bringt kein Geld: Trades, die nur aus dem Volltext kamen, liegen bei −1,9 %; die, die schon aus den ersten 50 Wörtern folgen (ATM, Fusion), bei +2,7 % (beides nicht signifikant, G).
4. Krypto-Kandidaten sind nicht messbar: 31 Governance-Abstimmungen in 15 Wochen (nötig ~600), 11 Unlocks mit Point-in-Time-Datum (nötig ~1 300–3 300). Die Engstelle ist die Fallzahl nach dem Modell-Cutoff, nicht der Datenzugang.
5. Ampel **rot** für "KI liest, was der Markt übersieht" als Cheatcode in kleinen Assets bei unseren Kosten; ein Paper-Forward-Test ist billig möglich und als Vorschlag beschrieben, braucht aber Aarons OK.

## Phase 1: Literatur-Basisrate

Details: [01-literatur-basisrate.md](01-literatur-basisrate.md).
- Ursprünglich 1 bis 2 % pro Monat vor Kosten (Cohen-Frazzini, Cohen-Lou, Lazy Prices, PEAD 8–9 % pro Quartal 1974–86) (L).
- Fast nur in illiquiden Titeln, Kosten fressen 70–100 % (Chordia 2009). PEAD bei Nicht-Microcaps seit ~2006 weg, bei Microcaps 2016–19 (Martineau 2022). Nach Publikation −58 % (McLean-Pontiff 2016) (L).
- LLM-Nachrichtensignal: Sharpe 6,5 → 1,2 in gut zwei Jahren, bei 20 bp Kosten unprofitabel (Lopez-Lira/Tang) (L).
- Pseudonymisierung schützt nicht: 70 % Wiedererkennung maskierter Firmen (Sarkar/Vafa) (L). Hier bestätigt (unten).
- Erwartung vorab (S): ≈ 0 netto, Spanne −0,5 bis +1 % je Ereignis. Gemessen: −0,3 %. Die Literatur hatte recht.

## Datenlage (Phase 2)

Details: [02-datenlage.md](02-datenlage.md), Rohdaten `daten/` mit sha256.
- **A1 Unlocks:** kein freier Point-in-Time-Kalender. Nur Wayback-Schnappschüsse 2023 bis Anfang 2024 → 11 Cliff-Unlocks in Insider-Kategorien.
- **A2 Dokumente:** SEC (Annahmezeit sekundengenau von der Index-Seite; das JSON-Feld ist in 6 085 von 11 056 Fällen falsch, G), Snapshot `created`. Kurse: Binance-Stunden inkl. delisteter Paare, US-Tageskerzen (Yahoo) für 4 247 Ticker.
- **A3 Querverbindungen:** Graph nicht point-in-time → nicht gerechnet.
- Holdout 2025-01..2026-06: 0 Kurszeilen (geprüft über 2,79 Mio Zeilen, `daten/holdout_check.txt`).

## Ergebnis je Kandidat

Vorab-Kriterien und Nachträge N1–N3: [03-killkriterien.md](03-killkriterien.md). Machbarkeits-Tor vor dem Rechnen: n_nötig = ((3,39 + 0,84)·σ/2 %)², σ aus Zufallsfenstern ohne Ereignis (G, `ergebnisse/gate.json`).

| Kandidat | Gegenpartei | n | Brutto | Netto | p (Wochen-Bootstrap) | Tor | Urteil |
|---|---|---|---|---|---|---|---|
| **A2-S-5** 8-K, 5 Tage | Kleinanleger, die 8-Ks nicht lesen; Market Maker, der den Spread kassiert | 156 | +1,92 % | −0,26 % | 0,06 / 0,59 | formal verfehlt (n 156 < 381, N3) | **tot** (netto ≤ 0); schließt Netto-Effekte ≥ ~3 % aus |
| A2-S-20 8-K, 20 Tage | dito | 154 | +0,29 % | −2,04 % | 0,51 / 0,70 | nicht messbar | deskriptiv tot |
| A2-K-5 Snapshot, 5 Tage | Token-Halter, die Vorschläge nicht lesen | 9 | – | −2,1 % | 0,64 | nicht messbar | deskriptiv |
| A2-K-20 | dito | 9 | +6,2 % | +5,8 % | 0,31 | nicht messbar | deskriptiv |
| A1-a Short vor Insider-Unlock (t−30..t−1) | Insider/VCs, die nach Cliff verkaufen müssen | 11 | – | +7,6 % (Median +14 %) | 0,23 | nicht messbar | deskriptiv, Richtung wie Literatur |
| A1-b Long nach Unlock | dito | 11 | – | +1,4 % | 0,32 | nicht messbar | deskriptiv |
| A3 | – | – | – | – | – | nicht gerechnet | Graph nicht PIT |

Kosten A2-S (G): 0,4 % Gebühr pro Runde + 2 × halber Spread (Corwin-Schultz, Mittel 0,86 %, Median 0,69 %) + 5 % p.a. Leihgebühr bei Shorts ≈ **2,2 %**.

### Gegenhypothesen A2-S-5 (G, `ergebnisse/a2s_result.json`, `ergebnisse/extra.json`)

| Gegenhypothese | Prüfung | Ergebnis |
|---|---|---|
| Trainings-Leck (Modell kennt die Firma) | Zweiter Subagent rät Firma/Jahr | Firma genannt in 55 % der Dokumente, sicher (3) in 17 %. Erkannte Trades netto −1,4 % (n 84), nicht erkannte +1,1 % (n 72). Das Leck erklärt keinen Gewinn, eher umgekehrt |
| Rest-Leck im Text | Regex auf Jahr/CIK | 10 von 499 Texten (XBRL-Kopf), 2 Trades; ohne sie netto +0,04 % |
| Zeitgleiche Nachrichten | Ohne andere 8-K derselben Firma ±3 Tage | netto −0,48 % (n 120) |
| Stil statt Inhalt | 50-Wörter-Leser | siehe [04-zwanzig-faelle.md](04-zwanzig-faelle.md): Tiefenlesen bringt −1,9 %, Kategorie-Info +2,7 % (beides t < 1,4) |
| Survivorship | 8-K ohne heutigen Ticker | 12,3 % der 8-K-Zeilen (676 CIKs) fallen raus: privat, Anleihe-Emittenten **oder** inzwischen delistet; Anteil delisteter darunter unbekannt. Delistete Firmen hatten eher schlechte Nachrichten → fehlende Short-Gewinne möglich (Richtung des Fehlers: unterschätzt die Short-Seite) |
| Zuversicht | nach Stufe 1/2/3 | −0,1 % / −1,0 % / +1,8 % (n 80/60/16), kein Gradient mit Signifikanz |
| Long gegen Short | getrennt | Long −1,5 % (n 70), Short +0,8 % (n 86) |

Zusatz A2-K: Die Governance-Projekte werden fast alle erkannt (29 von 31 mit Namen, meist Sicherheit 3: Aave, Lido, Arbitrum, Uniswap …). Ein blinder Leser für Krypto-Governance ist mit diesem Modell nicht herstellbar.

## Phase 5: Skalierungs-Ehrlichkeit

- **Realistisch: 0 USD/Jahr.** Netto ≤ 0 bei unseren Kosten, also keine Kapazität.
- Hypothetische Obergrenze (S), falls die Brutto-Prämie von 1,9 % echt wäre **und** man den Spread ganz vermeiden könnte (nur 0,4 % Gebühr, Edge p = 1,5 %): Quadratwurzel-Gesetz mit gemessenem Volumen (Median 4,5 Mio USD/Tag, σ_Tag ≈ 9,2 %/√5 = 4,1 %) → optimale Größe ≈ 66 kUSD je Trade (Median), Gewinn ≈ 330 USD (Median) bzw. 835 USD (Mittel) je Trade, × ≈ 770 Trades/Jahr ≈ **0,64 Mio USD/Jahr**. Das ist die Obergrenze eines unbewiesenen Effekts (t 1,5) unter einer Annahme (spreadfreie Ausführung in Microcaps), die nicht hält.
- Betriebsstunden (S): 770 Dokumente/Jahr lesen kostet ≈ 15 Agent-Läufe/Monat; Orders ≈ 3 pro Handelstag, Shorts leihen in Microcaps oft nicht verfügbar. Grob 150–250 h/Jahr inkl. Datenpflege über den Mac. Bei 25 kEUR Kapital und 0 netto ist das Ergebnis eine Erkenntnis, kein Geschäft.

## Phase 6

### Tote Wege (neu)
- KI liest 8-K kleiner US-Firmen blind, 5/20 Tage halten: netto ≤ 0 bei gemessenem Spread.
- Tiefenlesen über die Kategorie hinaus (Studiendaten, Kreditkonditionen): bringt brutto nichts Messbares.
- Blindes Lesen von Krypto-Governance: Modell erkennt die Projekte, Pseudonymisierung wirkungslos; dazu zu wenige Fälle.

### Cheatcode-Ampel
| Kandidat | Ampel | Grund |
|---|---|---|
| A1 Unlocks | grau | nicht messbar (11 Fälle), bezahlter Kalender nötig |
| A2-K Governance | grau/rot | nicht messbar, Blindheit nicht herstellbar |
| A2-S 8-K | **rot** | netto ≤ 0, Kosten = Prämie |
| A3 Querverbindungen | grau | nicht gerechnet |

### Forward-Test-Plan (Vorschlag, nicht gestartet)
- **F3 (A2-S paper):** jeden Montag die 8-Ks kleiner US-Firmen der Vorwoche über den Mac holen, mit dem gefixten Pseudonymisierer (XBRL-Kopf raus) und dem eingefrorenen Leser `prompts/leser-v1.md` lesen, Einstieg nächster Open, 5 Tage, Kosten wie hier. Auswertung bei n ≥ 400 Trades (≈ 2027-04, gleicher Termin wie F1/F2). Kill: netto ≤ 0 oder p ≥ 0,05. Teil-Arm F3b: nur Trades, bei denen schon 50 Wörter dieselbe Richtung geben (hier +2,7 %, n 58).
- A2-K und A1 nicht in den Forward-Test: zu wenige Ereignisse bzw. kein Kalender.
- Aufwand: ein Mac-Lauf + ~2 Agent-Läufe pro Woche. **Braucht Aarons OK**, weil es wöchentlich Mac-Sitzungen startet.

### Bias-Check
- **Gegen mich:** Ich wollte einen KI-Vorteil finden; die Verwerfungsregel stand vorher fest, das Tor wurde nach dem Lesen (aber vor den Renditen) als N3 ergänzt, weil der Leser nur ⅓ der Dokumente handelt. Das ist eine Lockerung zugunsten eines Urteils statt "nicht messbar" und offen markiert.
- **Kosten:** Corwin-Schultz ist für Microcaps verrauscht und kann Spreads überschätzen. Mit nur 0,4 % Gebühr wäre netto ≈ +1,4 % (t ≈ 1,1): immer noch weit von α = 0,00031.
- **Modell-Cutoff:** Der Leser ist dasselbe Modell, das die Firmen zu 55 % erkennt. Erkannte Fälle laufen schlechter, also kein Leck-Gewinn, aber das Testfenster ist für ein blindes Experiment unrein.
- **Benchmark:** gleichgewichtetes Small-Cap-Universum ab Tages-Open; Fehler am Einstiegstag ist Rauschen, kein Vorzeichen-Bias (S).
- **Auswahl:** nur 8-Ks ≥ 300 Wörter Haupttext, ohne reine 5.07/7.01/9.01, eine Meldung je Firma je 20 Tage (vorab). 586 von 1 085 Ereignissen fielen durch den Wortfilter.

## Was ich noch nicht weiß
- Ob die Brutto-Prämie von +1,9 % echt ist (t 1,5). Dafür fehlen ~225 Trades.
- Wie groß der Spread bei Ausführung über Limit-Orders wirklich ist (Corwin-Schultz ist eine Schätzung aus Tageskerzen).
- Wie viele der 676 fehlenden CIKs delistete Firmen sind, und was ihre 8-Ks gebracht hätten.
- Ob ein anderer Leser (kein Wissen über 2026-Firmen) bei Krypto-Governance blind wäre.
- Ob Unlocks (A1-a +7,6 % netto, 9 von 11 positiv) mit einem echten Kalender halten.

## 3 Fragen für die nächste Runde
1. Lohnt ein bezahlter Unlock-Kalender (Tokenomist/Messari) für einen sauberen A1-Test mit ~1 000 Ereignissen ab 2023? Kosten gegen erwarteten Informationswert.
2. Kann man die Kostenseite drehen: als Liquiditätsgeber (Limit-Orders) statt Taker in denselben Microcaps, also den Spread verdienen statt zahlen? Das wäre der Gegenpartei-Gedanke aus Meta-Regel 3.
3. Gibt es in Krypto eine Ereignisklasse mit ≥ 1 000 Fällen pro Quartal nach dem Cutoff (z. B. Binance/Upbit-Listings, Token-Emissionen on-chain), die ohne KI-Blindheit auskommt, weil die Information maschinenlesbar ist?

## Dateien
| Datei | Inhalt |
|---|---|
| 00–04 *.md | Phasen 0–3, Nachträge, 20-Fälle-Prüfung |
| code/ | `pseudo.py` (+Tests), `r3_events.py`, `prep_docs.py`, `agent_prompts.py`, `r3_eval.py`, `r3_extra.py` |
| prompts/ | eingefrorene Leser-/Leck-Prompts mit sha256 |
| lesen/ | pseudonymisierte Batches, Schlüssel, Antworten (Leser, Leck, 50 Wörter) |
| daten/ | Rohdaten mit sha256.txt, request.log, holdout_check.txt |
| ergebnisse/ | events_*.csv, gate.json, *_trades.csv, *_result.json, extra.json |

Nachrechnen: `python3 code/r3_events.py && python3 code/prep_docs.py a2s && python3 code/r3_eval.py a2s && python3 code/r3_extra.py`.
