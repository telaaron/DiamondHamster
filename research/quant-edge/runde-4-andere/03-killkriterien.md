# Runde 4: Kill-Kriterien, vorab (2026-10-16, ~21:40 UTC)

Geschrieben vor jedem Datenabruf (Mac-Sitzung läuft nur Probe-Aufrufe), vor jedem Transkript und vor jeder Rendite. Abweichungen nur als datierter Nachtrag am Ende. Regeln aus Runde 1–3 und dem Forschungsprotokoll gelten unverändert. Basisraten aus der Literatur: [01-literatur-basisrate.md](01-literatur-basisrate.md).

Kennzeichnung: (G) gerechnet, (S) geschätzt mit Herleitung, (L) Literatur.

## Gemeinsame Regeln

- **Holdout:** 2025-01-01 .. 2026-06-30 wird nicht geladen, weder Kurse noch Optionstrades. Calls aus Videos mit Upload in diesem Fenster werden gezählt (Anzahl, Vagheit), aber nicht bewertet. Fenster: **Dev ≤ 2024-12-31**, **Nachschau 2026-07-01 .. 2026-10-16** (nur deskriptiv bzw. getrennt ausgewiesen).
- **Kosten:** 0,2 % je Seite plus halber gemessener Spread je Seite (Krypto: Corwin-Schultz aus Stundenkerzen wie R3, BTC/ETH pauschal 0,01 %; Aktien: Corwin-Schultz aus Tageskerzen). Empfindlichkeit mit 0,05 % je Seite wird mitberichtet, entscheidet aber nicht.
- **Test-Zähler:** 161 aus WISSENSBASIS + 20 vorab hier (A 9, B1 3, B2 7, B3 1) = **181**. Bonferroni α = 0,05 / 181 = **0,00028**, einseitig z = **3,45**. Nachträge erhöhen N, bestätigen nie.
- **Statistik:** p einseitig per Block-Bootstrap über Kalenderwochen (Ereignisse derselben Woche hängen zusammen), 10 000 Ziehungen.
- **Urteile:** **lebt** = Netto-Mittel > 0, p < α, gleiches Vorzeichen in erster und zweiter Hälfte (zeitlich). **Hinweis** = netto > 0 und p < 0,05. **tot** = netto ≤ 0 oder brutto ≤ 0. **Prämie da, nicht erntbar** = brutto > 0 mit p < 0,05, netto ≤ 0. **nicht messbar** = Machbarkeits-Tor verfehlt (dann nur deskriptiv, kein Urteil).
- **Machbarkeits-Tor (vor dem Rechnen):** n_nötig = ((3,45 + 0,84) · σ / μ)², σ aus der Zufalls-Baseline (gleiche Assets, gleiche Regeln, *ohne* Call-Ergebnisse), μ = vorab genannte ökonomisch relevante Größe je Test.
- **Sharpe > 3** (annualisiert) in irgendeinem Ergebnis: zuerst Fehlersuche (Look-ahead, Zeitstempel, Duplikate, Survivorship), erst dann berichten.

## Arm A: YouTube-Trader-Audit

**Gegenpartei:** Wenn der Kanal gewinnt, zahlen die Marktteilnehmer auf der anderen Seite seiner Trades (Hypothese: Information oder Risikoübernahme des Kanals). Wenn der Fade gewinnt, zahlt das Publikum, das den Calls folgt. Gewinnt keiner, gibt es keine Gegenpartei, nur Rauschen.

### Calls
- **Explizit** = Asset + Richtung + mindestens Einstiegsbereich *oder* Stop *oder* Ziel, als Empfehlung oder eigene Position formuliert. **Vage** = Richtung ohne Niveaus oder Konjunktiv ("könnte drehen", "beobachten") → gezählt, nicht gehandelt. **Vagheitsquote** = vage / (vage + explizit) je Kanal.
- **Extraktion:** Claude-Subagent ohne Werkzeuge und ohne Kurse (Prompt E1), Transkript ohne Upload-Datum und ohne Kanalname. Zweiter Durchlauf mit anderem Prompt (E2). Übereinstimmung je Feld (Cohen-κ für Richtung, Anteil identischer Assets). Gehandelt wird nur, was E1 und E2 gleich extrahieren (Asset und Richtung gleich; Niveaus: Mittel, wenn beide ≤ 2 % auseinander, sonst E1). 30 Fälle prüfe ich von Hand gegen das Transkript.
- **Einstieg:** Open der ersten vollen Stunde nach Upload-Zeit (Binance-Spot-Stundenkerzen, sonst Perp). Liegt ein Einstiegsbereich vor und der Kurs ist innerhalb von 72 h nicht im Bereich, wird der Call als "nicht ausgelöst" gezählt, nicht gehandelt. Ohne Bereich: Markteinstieg.
- **Ausstieg:** Stop oder Ziel, je nachdem was zuerst in Stundenkerzen erreicht wird; beide in derselben Kerze → Stop (konservativ für den Kanal, gegen den Fade). Mehrere Ziele → erstes Ziel. Ohne Horizont: Ausstieg spätestens nach **14 Tagen** (S: Mitte der üblichen Swing-Spanne 3–30 T).
- **R-Vielfaches:** Netto-Rendite / Stop-Abstand vom Einstieg. Calls ohne Stop: R nicht definiert, dann Rendite in % über den Horizont (Nebenmetrik, eigene Variante nicht gezählt, nur deskriptiv).
- **Kosten:** 2 × (0,2 % + halber Spread) je Trade, in R umgerechnet.

### Varianten (vorab, gezählt)
| ID | Test | μ fürs Tor |
|---|---|---|
| A-K1..K3 | Kanal 1..3: EV je Trade in R nach Kosten > 0 | 0,25 R |
| A-F1..F3 | Fade Kanal 1..3: Gegenposition, gleiche Niveaus gespiegelt (Stop ↔ Ziel), gleiche Kosten | 0,25 R |
| A-KP, A-FP | alle Kanäle gepoolt, Kanal bzw. Fade | 0,15 R |
| A-P | Pump: anormale Rendite 0–24 h nach Upload, nur Assets < 50 Mio USD Tagesvolumen (30-T-Median vorher), Richtung des Calls | 1 % |

### Baselines (nicht gezählt)
- **Zufall:** je Call 10 000 Zufallseinstiege im gleichen Asset (gleiches Kanalfenster, Dev), gleiche relative Stop/Ziel-Abstände, gleicher Horizont, gleiche Richtung. Gemeldet: EV Call − EV Zufall und das Perzentil des Kanal-EV in der Zufallsverteilung.
- **Buy-and-Hold:** gleichgewichtete Haltung der genannten Assets über das Kanalfenster.

### Urteile Arm A
- **Kanal gewinnt:** EV netto > 0, p < α, beide Hälften gleiches Vorzeichen, **Löschquote bekannt und einbezogen** (gelöschte Videos ohne Transkript: Worst-Case-Rechnung, in der jedes gelöschte Video einen Call mit −1 R trägt, in Höhe der durchschnittlichen Calls je Video; das Urteil muss auch dann halten).
- **Fade gewinnt:** dito für die Gegenposition, Worst Case umgekehrt (+1 R je gelöschtem Call für den Kanal).
- Alles andere: tot oder nicht messbar.
- **Löschquote** = Video-IDs aus Wayback-Schnappschüssen und Playlists, die heute fehlen / alle je gesehenen IDs. Ergebnis für sich.

## Arm B1: Form-4-Insider-Käufe

**Gegenpartei:** Verkäufer am freien Markt ohne die Information des Insiders (Liquiditäts- oder Rebalancing-Verkäufer). Zwang: keiner beim Insider, er *muss* aber binnen 2 Werktagen melden (Section 16(a)).
- **Daten:** SEC Insider Transactions Data Sets (Form 3/4/5, quartalsweise). Annahmezeit sekundengenau von der Index-Seite der Akte (Lehre B3-03).
- **Ereignis:** Transaktionscode P (Kauf am freien Markt), erworben, nicht-derivativ; ausgeschlossen: Optionsausübung (M, X), Zuteilung (A), 10b5-1-Häkchen (ab 2023) oder Fußnote mit "10b5-1". Mehrere Käufe desselben Insiders in derselben Akte = 1 Ereignis.
- **Routine/opportunistisch (Cohen/Malloy/Pomorski 2012):** Insider mit Trades in jedem der 3 Vorjahre; hat er in allen 3 Vorjahren im selben Kalendermonat gehandelt → Routine (raus). Sonst opportunistisch. Insider ohne 3 Jahre Vorgeschichte: nicht klassifizierbar, raus aus dem Haupttest.
- **Handel:** Long zum Open des ersten Handelstags nach der Annahmezeit (Annahme nach 9:30 ET → nächster Tag), 20 Handelstage halten.
- **Universum:** nur Aktien mit 21-T-Median-Dollarvolumen > 50 Mio USD vor dem Ereignis. **Benchmark:** gleichgewichteter S&P-500 (RSP) im selben Fenster (S: entspricht etwa dem Universum > 50 Mio). Zweite Kennzahl: gleichgewichtetes Mittel aller Universum-Aktien mit Kursen.
- **Fenster:** Ereignisse 2013-01 .. 2024-12 (Dev). Nachschau 2026-07+ nur deskriptiv, wenn Kurse ohne Holdout reichen.
- **Survivorship:** Kursquelle Yahoo kennt delistete Ticker nicht. Anteil Ereignisse ohne Kurse wird berichtet; Fehlende werden nicht ersetzt.

| ID | Test | μ fürs Tor |
|---|---|---|
| B1-O | opportunistische Käufe, 20 T, netto über RSP | 0,5 % |
| B1-R | Routine-Käufe (Kontrolle; Erwartung ≈ 0) | – (gezählt) |
| B1-C | Cluster: ≥ 2 verschiedene Insider derselben Firma kaufen binnen 10 Kalendertagen; Ereignis = Annahme der Akte, die den Cluster vollständig macht | 0,5 % |

Basisrate und Schrumpfung nach Veröffentlichung (McLean/Pontiff): [01-literatur-basisrate.md](01-literatur-basisrate.md). **Zusatz-Kill:** liegt B1-O netto unter der McLean/Pontiff-geschrumpften Literatur-Erwartung *und* ist p > 0,05, gilt der Effekt als in großen Werten wegarbitriert.

## Arm B2: Dealer-Gamma Deribit (BTC, ETH)

**Gegenpartei:** Hedge-Mandat des Market Makers (Dealer). Software-Analogie: ein Regelkreis mit festem Sollwert. Ist der Dealer "long Gamma", muss er bei steigendem Kurs verkaufen und bei fallendem kaufen (dämpfend); ist er "short Gamma", umgekehrt (verstärkend). Er muss, sonst trägt er ungewolltes Richtungsrisiko.

- **Daten:** alle Optionstrades Deribit BTC/ETH 2022-01 .. 2024-12 (history.deribit.com). Spot-Stundenkerzen Binance.
- **Proxy (Annahme offen markiert, A-1):** Kunden = Taker, Dealer = Maker. Kundenposition je Kontrakt = kumulierte Taker-Käufe − Taker-Verkäufe seit Listing; Dealer-Position = −Kundenposition. Gamma je Kontrakt Black-Scholes (r = 0, IV = letztes Trade-IV des Kontrakts, sonst vorheriger Wert). **GEX** = Σ Dealer-Position × Γ × S² × 1 % (USD je 1 % Kursbewegung), täglich 00:00 UTC.
- **Gegenannahme (A-2, Sensitivität):** "Kunden kaufen Puts, verkaufen Calls" (klassische Annahme vieler Gamma-Dienste): Dealer long Calls, short Puts, Gewicht = offene Kontrakte aus Trades (|Netto| je Kontrakt).
- **Warm-up:** 2022 (Kontrakte, die vor 2023 gelistet wurden, haben dann vollständige Flüsse). Testfenster **2023-01 .. 2024-12**.
- **Regime walk-forward:** Terzile des GEX mit expandierendem Fenster nur aus der Vergangenheit (Start: 2022-H2-Werte).
- **Zielgrößen (nächste 24 h, Stundenrenditen):** realisierte Volatilität RV (Summe quadrierter Stundenrenditen) und Autokorrelation erster Ordnung AC1.
- **Kontrolle:** RV ist persistent. Test auf RV als Regression RV_{t+1} = a + b·RV_t + c·RV_{t−7..t−1} + d·GEX-Rang_t (HAR); getestet wird d.

| ID | Test | Erwartung (L) |
|---|---|---|
| B2-RV-BTC, B2-RV-ETH | d < 0 (positives Gamma → weniger Vol) | Ni et al. 2021 |
| B2-AC-BTC, B2-AC-ETH | AC1 im oberen Terzil < AC1 im unteren Terzil | Baltussen et al. 2021 |
| B2-A2 | B2-RV-BTC mit Gegenannahme A-2 | – |
| B2-T1, B2-T2 | Handelsregel (nur wenn RV- *und* AC-Muster für das Asset halten): unteres Terzil → 24-h-Position in Richtung der letzten 24 h, oberes → dagegen; mittleres flach; je BTC, ETH | – |

- **Signifikanz:** empirische Nullverteilung durch Block-Permutation des GEX gegen die Renditen (Blöcke 30 Tage), 10 000 Ziehungen.
- **Umschlag-Budget (Meta-Regel 2):** Regel handelt höchstens 1× je Tag: bis 365 Rundreisen × 0,4 % ≈ 146 % p.a. Kostenlast bei Volleinsatz (S). Die Regel braucht also brutto deutlich mehr als 0,4 % je Trade; Literatur (Intraday-Momentum) liegt bei Basispunkten. **Vorab-Erwartung: Regel stirbt an Kosten**; gerechnet wird trotzdem, weil Aaron es verlangt.
- **Kill:** Regime-Unterschied nach Korrektur nicht signifikant (p ≥ α) → tot. Handelsregel netto ≤ 0 → tot.

## B3 Kongress-Trades: nur wenn B1 lebt (1 Variante reserviert)

Basisrate vorab in 01-literatur-basisrate.md. Gerechnet nur, wenn B1-O oder B1-C "lebt".

## Gegenhypothesen, die jedes Ergebnis überleben muss

1. **Survivorship (A):** gelöschte Videos → Worst-Case-Rechnung (oben). (B1): delistete Aktien fehlen → Anteil berichten; Mergers sind eher positiv, Pleiten negativ.
2. **Extraktions-Leck (A):** Das Modell kennt die Kurse 2022–2024 aus dem Training und könnte mehrdeutige Calls in Richtung des späteren Kurses lesen. Prüfung: (a) nur Calls, in denen E1 und E2 übereinstimmen; (b) Ergebnis getrennt nach Fällen, die die Prüfer als "eindeutig" markieren; (c) Nachschau 2026-07+ (nach Cutoff) getrennt.
3. **Rosinenpicken des Kanals:** Videos, deren Titel einen früheren Erfolg feiern, zählen nicht als neue Calls (nur Calls mit Zukunftsbezug).
4. **Markt-Beta (A):** Kanal ist fast immer long → EV kommt vom Markt. Deshalb Zufalls-Baseline mit gleicher Richtung und Buy-and-Hold.
5. **Gamma-Proxy falsch (B2):** Wenn Taker ≠ Kunde, ist das Vorzeichen falsch. A-2 als Sensitivität; Deribit-Snapshot heute (echtes OI) gegen die Rekonstruktion abgleichen (Summe |Netto| vs. OI je Kontrakt, Korrelation).
6. **Vol-Persistenz (B2):** HAR-Kontrolle; ohne sie wäre jedes Gamma-Signal nur "hohe Vol folgt hoher Vol".

## Nachträge

**N1 (2026-10-16 ~22:00 UTC, vor jeder Videoliste, jedem Transkript und jeder Rendite):**
- **Kanäle** (Auswahl per Websuche, Social-Blade-Stand Mitte Oktober 2026, Aaron hat keine eigenen genannt):
  - K1 **10xTrading**, Handle @1OxTrading (Ziffer 1 + großes O), UCFP64RzRV_OEzPOa9InjCjg, deutsch, ~39 k Abos, ~2 820 Videos, Betreiber laut About-Text Michael Hübner. Nicht verwechseln mit @10xtrading ("Trader George", 14 Videos), @10x.trading, @10xtrader, 10x Research.
  - K2 **Jaytrading** @jaytrading, UC_lONYOT5HrS1uPaOtGuaSQ, deutsch, ~31 k Abos, ~1 640 Videos, seit 2021, BTC/Altcoins plus Gold/Aktien (bester Größen- und Stil-Match).
  - K3 **CoinCheck TV** @coinchecktv, UCI-Non6k9qxq7iA6_LyldyQ, deutsch, ~108 k Abos (2,7× K1, oberer Rand), ~1 360 Videos, reiner Krypto-Kanal.
  - Verworfen: Biturai (zu wenige Videos 2022–24), Crypto Trading DE (erst ab 2024-05), HKCM (≈ 20× größer).
- **K1 ist kein reiner Krypto-Kanal** (Tesla, Nvidia, DAX, Gold, Silber, BTC, ETH). Deshalb werden **alle** expliziten Calls bewertet, nicht nur Krypto: Krypto mit Binance-Stundenkerzen, alles andere (Aktien, Indizes, Rohstoffe) mit **Tageskerzen** (Yahoo; Stop/Ziel an Tageshoch/-tief, beide am selben Tag → Stop; Einstieg = Open des ersten Handelstags nach Upload). Kosten gleich (0,2 % je Seite + halber Spread). Ergebnis zusätzlich getrennt nach Krypto / Nicht-Krypto (deskriptiv, nicht gezählt).
- **Pump-Test A-P** nur für Krypto-Assets (für Aktien < 50 Mio USD Tagesvolumen fehlen intraday-Daten außerhalb des Holdouts).
