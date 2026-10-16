# Runde 3, Phase 3: Kandidaten und Kill-Kriterien, vorab (2026-10-16, ~17:10 UTC)

Geschrieben, bevor eine Rendite eines Ereignisses angesehen oder ein Dokument von der KI gelesen wurde. Gezählt werden darf vorher nur, *wie viele* Ereignisse es gibt (Machbarkeit), nie wie sie ausgingen. Abweichungen nur als datierter Nachtrag am Ende. Regeln aus [00-abgrenzung.md](00-abgrenzung.md), Runde 1 und Runde 2 gelten unverändert.

## Einordnung in die Meta-Regeln der WISSENSBASIS

- **Regel 1 (Zahlungsstrom vor Richtung):** A1 und A2 sind Richtungs-Kandidaten. Zulässig nur, weil der Mechanismus (begrenzte Aufmerksamkeit bei kleinen Assets, Lesekosten) in keiner toten Familie steckt: K2–K4 und die 37 KI-Versuche nutzten Kurse und Marktdaten, keine Dokumente. Wenn A1/A2 sterben, ist das ein Befund für Regel 1.
- **Regel 2 (Umschlag-Budget):** Ein Ereignis = eine Rundreise = 2 × (0,2 % + halber Spread). Bei 0,2 % halbem Spread ≈ 0,8 % je Ereignis (S). Ein Kandidat braucht vorab plausibel > 0,8 % Brutto-Prämie je Ereignis. Literatur (Phase 1) gibt 0,5 bis 2 %: knapp über Budget, deshalb wird gerechnet, aber mit Machbarkeits-Tor.
- **Regel 3 (Prämie beim Gezwungenen):** Gegenpartei je Kandidat unten benannt.

## Gemeinsame Regeln

- **Universum:** Binance-Spot-USDT-Paare einschließlich später delisteter (Archiv data.binance.vision). Klein = Median des Tages-Quote-Volumens (USD) über die verfügbaren Tage in [t−30, t−1] **< 50 Mio USD** und **> 0,5 Mio USD** (darunter ist der Spread nicht handelbar und die Kerzen unzuverlässig; Untergrenze vorab, (S)). Volumentage aus dem Holdout werden nie geladen; für Ereignisse ab 2026-07-01 zählen nur Tage ab 2026-07-01, mindestens 7.
- **Kein "schneller als":** Einstieg zum Open der ersten vollen Stunde, die ≥ 60 min nach dem Zeitstempel der Erstveröffentlichung beginnt.
- **Rendite:** abnormal = Token-Rendite minus gleichgewichtetes Mittel aller übrigen Universum-Token im selben Fenster (Markt kleiner Token als Benchmark).
- **Kosten:** 0,2 % je Seite plus gemessener halber Spread je Seite. Spread: Median von bookTicker-Schnappschüssen (live, Forward) bzw. Corwin-Schultz-Schätzer aus Stundenkerzen, geeicht an Binance-Futures-bookTicker 2023-05..2024-03 (Rückrechnung, (S)).
- **Statistik:** Mittel der abnormalen Netto-Renditen; p einseitig per Block-Bootstrap über Kalenderwochen (Ereignisse derselben Woche hängen zusammen), 10 000 Ziehungen.
- **Test-Zähler:** 137 aus WISSENSBASIS + 6 vorab hier (A1: 2, A2-K: 2, A2-S: 2) = **143**, Bonferroni α = 0,05 / 143 = **0,00035** (einseitig z ≈ 3,39). Nachträge erhöhen N, bestätigen nie.
- **Machbarkeits-Tor (vor dem Rechnen):** n_nötig(μ) = ((3,39 + 0,84) · σ / μ)², σ = Streuung der abnormalen Rendite über die Haltedauer, gemessen an Zufallsfenstern *ohne* Ereignis derselben Token. Ist n_vorhanden < n_nötig(μ = 2 %), lautet das Urteil **"nicht messbar"** (nicht "tot", nicht "lebt"). Der Kandidat wandert dann direkt in den Forward-Test, die Rückrechnung läuft nur deskriptiv.
- **Urteile:**
  - **lebt:** Netto-Mittel > 0, p < α, gleiches Vorzeichen in erster und zweiter Hälfte der Ereignisse (zeitlich sortiert).
  - **Hinweis:** Netto > 0 und p < 0,05.
  - **tot:** Netto ≤ 0, oder Brutto ≤ 0 (dann tot auch für billigere Ausführung).
  - **"Prämie da, nicht erntbar":** Brutto > 0 mit p < 0,05, netto ≤ 0.

## A1 Token-Unlocks (Regel, keine KI)

- **Gegenpartei:** Privatanleger, die den Vesting-Kalender nicht lesen und vor dem Termin halten oder kaufen. Empfänger (VCs, Team) sind eher die informierte Seite (sie können vorher absichern).
- **Ereignis:** geplanter Unlock ≥ 1 % des Umlaufs, Empfänger Team oder Investoren (nicht "Ecosystem"), sichtbar in einem Wayback-Schnappschuss von token.unlocks.app, der ≥ 35 Tage vor dem Termin liegt (Point-in-Time-Nachweis). Mindestabstand 60 Tage zwischen Ereignissen desselben Tokens.
- **Test A1-a (vor dem Termin):** abnormale Rendite Short von t−30 bis t−1 (Tage). Hypothese: negativ für den Token, also positiv für den Short.
- **Test A1-b (nach dem Termin):** abnormale Rendite Long von t+1 bis t+14. Hypothese: Erholung.
- **Kontrolle (Pflicht, keine eigene Variante):** gleiche Token, Zufallsfenster gleicher Länge ohne Unlock in ±45 Tagen. Gemeldet wird Ereignis minus Kontrolle; Token mit hoher Inflation fallen auch ohne Termin.
- **Fenster:** Entwicklung 2023-03..2024-12. Regel-Holdout 2025-01..2026-06 nur nach Aarons Freigabe als Einmaltest, falls A1 lebt.
- **Datenvorbehalt:** Fehlen PIT-Schnappschüsse für < 30 Ereignisse, ist A1 "nicht messbar mit freien Daten".

## A2-K Governance-Vorschläge Krypto (KI-Leser)

- **Gegenpartei:** Token-Halter kleiner Projekte, die lange technische Vorschläge nicht lesen; Fonds, für die der Token unter der Mindestgröße liegt.
- **Ereignis:** Snapshot-Vorschlag, Zeitstempel `created`, 2026-07-01..2026-09-26 (damit 20 Handelstage vor heute passen), Space-Token als Binance-Spot-Paar im Universum, Text ≥ 300 Wörter ("schwer lesbar"). Mehrere Vorschläge desselben Tokens innerhalb von 5 Tagen: nur der erste.
- **Leser:** isolierter Subagent ohne Werkzeuge (Agent-Typ `decider`), Prompt vor dem ersten Lesen eingefroren und gehasht. Er bekommt nur den pseudonymisierten Text (Namen, Ticker, Projekt-, Personen-, Firmennamen, Daten, URLs, Adressen, Beträge mit Währungsnamen ersetzt) und gibt Richtung −1/0/+1 und Zuversicht 1–3 aus. Keine Kurse, kein Datum.
- **Handel:** Richtung +1 → long, −1 → short; 0 → kein Handel. Haltedauer **A2-K-5: 5 Tage**, **A2-K-20: 20 Tage**.
- **Fenster:** nur nach dem Modell-Cutoff (ab 2026-07-01). Vor dem Cutoff nichts, auch nicht pseudonymisiert (Sarkar/Vafa: 70 % Wiedererkennung).

## A2-S 8-K-Meldungen US-Kleinwerte (KI-Leser)

- **Gegenpartei:** Privatanleger ohne Zeit; Fonds mit Mindestgröße; Indexfonds, die erst beim Rebalancing reagieren.
- **Ereignis:** 8-K mit `acceptanceDateTime` 2026-07-01..2026-09-18, Firma mit mittlerem Tages-Dollarvolumen < 50 Mio und > 0,5 Mio USD (30 Tage vorher, ab 2026-07-01 gemessen), Haupttext ≥ 300 Wörter, ohne reine Exhibit-/Termin-Meldungen (Items 5.07, 7.01, 9.01 allein). Pro Firma höchstens ein Ereignis je 20 Tage.
- **Leser und Handel:** wie A2-K. Haltedauer **A2-S-5: 5 Handelstage**, **A2-S-20: 20 Handelstage**. Benchmark: gleichgewichtetes Mittel der Universum-Aktien.
- **Kosten:** 0,2 % je Seite plus gemessener halber Spread; Short-Leihkosten Kleinwerte pauschal 5 % p.a. (S).
- **Survivorship:** In 15 Wochen delistete Firmen fehlen evtl. in den Kursdaten; Anteil wird gezählt und berichtet.
- **Stichprobe:** Gibt es mehr Ereignisse als nötig, wird vorab per Zufall (Seed 20261016) auf n_nötig(1 %) begrenzt, höchstens 2 000 Dokumente.

## A3 Querverbindungen: vorab nicht gerechnet

Gründe: (1) Der Verknüpfungs-Graph ist nicht point-in-time verfügbar (heutige Partnerschaften ≠ damalige; Phase 2). (2) Literatur-Erwartung ≤ 0,5 % je Ereignis (Phase 1), unter dem Umschlag-Budget (Meta-Regel 2). (3) Krypto-Korrelationen laufen in Minuten nach; der Effekt bräuchte Latenz (Phase 0). Keine Variante, Zähler unverändert.

## Gegenhypothesen, die jedes Ergebnis überleben muss

1. **Trainings-Leck:** Nur Dokumente nach dem Cutoff; zusätzlich fragt ein zweiter Subagent pro Dokument "welches Projekt/welche Firma ist das?". Erkannte Fälle werden getrennt ausgewertet.
2. **Survivorship:** delistete Token/Aktien im Universum zählen; Anteil berichten.
3. **Zusammenfallende Nachrichten:** Ereignisse mit Listing-/Delisting-Ankündigung (Binance-CMS) oder Unlock ± 3 Tage werden markiert und ohne sie neu gerechnet.
4. **Stil statt Inhalt:** 20 zufällige Fälle manuell: steht die Richtung im Inhalt oder nur im Ton? Zusätzlich Kontrolle: derselbe Leser bekommt nur die ersten 50 Wörter.

## Nachträge

(keine)
