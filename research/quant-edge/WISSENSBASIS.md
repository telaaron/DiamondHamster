# Quant-Edge Wissensbasis (WB)

Stand: nach Runde 2 (2026-10-16). Wird jede Runde vollständig fortgeschrieben. Bericht Runde 2: [bericht-runde2.md](bericht-runde2.md), Runde 1: [bericht.md](bericht.md).
Kennzeichnung: (G) gerechnet, (S) geschätzt mit Herleitung, (L) Literatur mit Quelle.

**Cheatcode-Definition:** Rendite nach Kosten, die (1) einen benannten Zwang oder eine Vorliebe einer Gegenpartei als Quelle hat, (2) in einem echten Forward-Test hält, (3) bei realistischer Größe skaliert, (4) keinen unmodellierten Totalverlust-Tail hat. Fehlt eines, ist es eine Hypothese. **Stand: kein Cheatcode. Zwei Hypothesen laufen als Paper-Forward-Test (F1, F2).**

**Annahmen (bis Aaron antwortet):** Kapital 25 000 EUR, Börsenzugang Binance, Bybit, Hyperliquid, OÜ nach estnischem Modell (einbehaltener Gewinn steuerfrei, Ausschüttung besteuert). Folge: Steuer ändert die Rangfolge Carry gegen T-Bill innerhalb der OÜ nicht, beide werden erst bei Ausschüttung besteuert (S).

## 1. Befunde

### Runde 1 (2026-10-16)
| ID | Aussage | Zahl | Kz. | Status |
|---|---|---|---|---|
| B1-01 | Rendite unter perfekter Information = Bezahlung fürs Tragen (Risiko, Hebel, Sofortigkeit, Versicherung, Zwangsfluss) | – | L (Grossman/Stiglitz 1980, Shleifer/Vishny 1997) | lebt (Rahmen) |
| B1-02 | K1 Funding-Carry BTC (Spot long, Perp short, Kapital 1,5) 2019-09..2024-12 | +8,4 % p.a., DD −1,8 % | G | lebt (Dev) |
| B1-03 | K1 ETH dito | +10,2 % p.a., DD −1,8 % | G | lebt (Dev) |
| B1-04 | K1 mit einmal 50 % Börsenverlust | BTC −4,9 %, ETH −3,8 % p.a. | G | **ersetzt durch B2-12** (Basisrate statt Einmal-Szenario) |
| B1-05 | Funding BTC brutto | 30,6 % (2021) → 11,9 % (2024) → 5,9 % (2026-07..10) | G | Niveaus lebt; "schrumpft strukturell" **nicht belegt** (B2-01) |
| B1-06 | Break-even Funding brutto für 4 % auf Kapital | ≈ 8 % p.a. | S aus G | lebt; Hürde jetzt T-Bill (B2-09) |
| B1-07 | Break-even Börsenausfallrate (50 % Verlust) | ≈ 9 % p.a. | S aus G | ersetzt durch B2-13 |
| B1-08 | K1 12 Coins gleichgewichtet | +6,5 % p.a., DD −6,6 %; SOL −5,6 % | G | lebt (Robustheit); mit Umschichtkosten +6,3 % (Q2-Benchmark) |
| B1-09 | SOL-Carry FTX-Woche 2022-11 | −31 % in ~2 Wochen | G | lebt (Risiko) |
| B1-10 | 3-Tage-Börsen-Ausfall hätte ETH-Short bei 2× im März 2020 liquidiert (Last-Price) | – | G/S | offen |
| B1-11 | K2 Kaufen nach Zwangsverkauf, 4/8 Wochen | beste p 0,44 | G | tot |
| B1-12 | Zwangsverkaufs-Prämie gepoolt auf Tageskerzen | 1 T +0,20 %, 28 T −2,6 % vor Kosten | G | lebt als Beobachtung; "wird in Minuten geerntet" **widerlegt** (B2-17) |
| B1-13 | K3 Exposure halbieren bei heißem Funding | t −0,18 / −0,60 | G | tot |
| B1-14 | K4 Trend + Vol-Steuerung | Sharpe unter B&H | G | tot (als Edge) |
| B1-15 | Positionsgröße schlägt Timing | – | G | lebt |
| B1-16 | Impact ≈ σ_Tag × √(Q/Volumen); 1 % BTC-Perp-Volumen ≈ 0,28 % | – | G/S/L (Tóth 2011) | lebt; bei 25 kEUR irrelevant |

### Runde 2 (2026-10-16)
| ID | Aussage | Zahl | Kz. | Status |
|---|---|---|---|---|
| B2-01 | Funding 2026-07..10 liegt unter dem Marktlage-Modell (30-T-Rendite, 30-T-Vol), aber innerhalb der normalen Modellfehler | BTC −5,4 pp, ETH −10,8 pp; empirisches p 0,47 / 0,17 | G | **offen**: Regime nicht nachweisbar |
| B2-02 | Newey-West-t "bestätigt" denselben Befund formal (t −4,2 / −3,5), ist aber ein Messfehler: dasselbe Modell lag 2023–24 bei BTC ebenso daneben (−5,2 pp, t −4,1) | – | G | lebt (Methodik-Lektion) |
| B2-03 | Mit Open-Interest-Änderung als Regressor schrumpft das BTC-Residuum auf −1,8 pp (p_emp 0,53), ETH −5,5 pp (p_emp 0,44) | – | G | lebt |
| B2-04 | Strukturbruch im Monats-Funding 2019–24: stärkster Sprung 2021-06 (BTC 25,6 → 8,8 %, ETH 38,6 → 8,5 %), aber nicht signifikant bei Persistenz | sup-F p 0,23 / 0,07 | G | lebt |
| B2-05 | USDe-Umlauf wächst, wenn Funding über Modell liegt (nicht umgekehrt); USDe heute 4,7 Mrd USD < Ende 2024 5,9 Mrd | Korr. +0,61 (BTC, p 0,006), +0,33 (ETH, p 0,07), 16 Monate | G | lebt als Hinweis: "Ethena drückt Funding" **nicht gestützt**, eher Folge des Fundings |
| B2-06 | 2026-H2: 86 % der Binance-BTC-Zahlungen unter dem Basiszins 0,01 %/8 h, 0 % darüber (2022 Bärenjahr: 69 % / 0 %) bei steigendem Kurs | – | G | lebt (deskriptiv) |
| B2-07 | Coin-Ausschluss nach negativem Funding (R1, R2), Short-Crowding (R3), Börsen-Gefälle (R4): alle schlechter als ohne Regel, weil Umschichtkosten das Signal fressen | R2 brutto +9,0 % / DD −3,7 % → netto +4,2 % / DD −11,5 % vs. Benchmark +6,3 % / −6,6 % | G | tot |
| B2-08 | R5 nur die 4 Coins mit höchstem 30-T-Funding: DD −2,2 % statt −6,6 %, +6,7 % statt +6,3 %, schloss SOL vor FTX aus | Sharpe-Diff p 0,47, DSR 0,00 | G | **Hypothese** (Hinweis, nicht signifikant) |
| B2-09 | Laufzeit-Futures immer gerollt (D1 USDT-M, D2 Coin-M), 2021–24 | D1 BTC +4,7 % (+1,6 pp über T-Bill), 34 % neg. 30-T-Fenster | G | tot (Kriterium neg. Fenster) |
| B2-10 | D3 Laufzeit-Future nur bei Basis > T-Bill + 2 pp, sonst T-Bills | BTC +5,5 % (+2,4 pp), ETH +6,1 % (+3,0 pp), DD −5,7 / −6,7 %, Sharpe 1,3 / 1,1, DSR 0,00 | G | lebt (Dev), statistisch schwach |
| B2-11 | Perp-Carry im selben Fenster 2021-03..2024 besser als Laufzeit-Carry | K1 BTC +5,9 %, Sharpe 8,9 | G | lebt |
| B2-12 | Basisrate Totalausfall Top-10-Börse (Mt.Gox, BTC-e, FTX in 128 Börsen-Jahren) | 2,3 % p.a. (Poisson-KI 0,5–6,9 %), Spanne 1 / 2,3 / 5 % | S aus L (Liste 70 Ereignisse, daten-r2/q4/) | lebt |
| B2-13 | Verlust bei Ausfall: USD-Forderung 0 / 0,3 / 0,7; in Coins 0,5 / 0,75 / 0,95 (Mt.Gox ≈ 0,79, FTX ≈ 0,8 in BTC) | – | S aus L | lebt |
| B2-14 | Break-even-Ausfallrate K1 im Dev-Regime: BTC 19,7 % (USD) / 7,9 % (Coins), ETH 25,7 % / 10,3 % p.a. gegen T-Bill | Faktor 3–11 über Basisrate | G/S | lebt: Ausfallrisiko tötet K1 in heißen Phasen nicht |
| B2-15 | K1 seit 2026-07 netto (Laufrate ohne Ein-/Ausstieg) unter T-Bill 3,8 % | Binance BTC 3,4 %, ETH 2,2 %; minus Ausfall 0,7 % | G | **K1 heute ökonomisch tot** (vorab-Kriterium) |
| B2-16 | Hyperliquid-Funding ≈ 2× Binance in jeder Phase | BTC 2024 24,1 vs 11,9 %; 2026-H2 8,7 vs 5,9 % | G | lebt |
| B2-17 | K1 mit Short auf Hyperliquid (nachträglich, ohne HL-Kurse, Obergrenze): Dev 2023-05..2024 +13,0 % / +13,7 %; seit 2026-07 Laufrate 5,4 % | – | G (Obergrenze) | Hypothese, Forward F1 |
| B2-18 | Börsen-Spread-Carry Binance gegen Bybit (X1) | ≈ 0 % p.a., 69 % neg. Fenster | G | tot |
| B2-19 | Börsen-Spread-Carry Binance gegen Hyperliquid (X2) | +4,0 % p.a. (Obergrenze), 49 % neg. Fenster | G | tot (Kriterium) |
| B2-20 | Kaskade mit OI-Drop (15 min) kaufen, 1–24 h halten: keine Überrendite, auch vor Kosten | z. B. BTC 1 h −0,05 %, ETH 4 h −0,13 % | G | tot |
| B2-21 | Short-Squeeze-Spiegel verkaufen | negativ in 5 von 6 | G | tot |
| B2-22 | Nur Preis-Crash (0,2-%-Quantil, 15 min) kaufen, 4 h halten: Überrendite brutto BTC +0,21 %, ETH +0,29 %, beide Hälften positiv, bleibt mit 15 min und 1 h Verzögerung (+0,19 / +0,29 / +0,17 %) | p 0,002; nach 0,4 % Kosten −0,19 / −0,11 % | G | **Hypothese H-Q5**: "Prämie existiert, mit Protokoll-Kosten nicht erntbar"; mit 0,05-%-Taker +0,07..+0,19 % je Trade vor Slippage |
| B2-23 | Der OI-Drop-Filter (echte Liquidationen) verschlechtert die Crash-Reversal-Prämie | – | G | lebt: Prämie ist nicht spezifisch Liquidation |
| B2-24 | Binance hat kein öffentliches Liquidations-Archiv; Hyperliquid-Collector seit 2026-10-16 12:17 UTC (4,5 h, 18/18 Marken) | – | G | Datenstand |
| B2-25 | CME-Basis: Feb 2024 ≈ 25 %, Ende 2024 15–20 %, Mai 2025 ≈ 10 %, Jan 2026 ≈ 4,7–5 % annualisiert | – | L (CF Benchmarks; Bloomberg/Amberdata via Advisor Perspectives 2026-01-22) | lebt; Hinweis: Literatur aus dem Holdout-Zeitraum |

## 2. Tote Wege (nicht nochmal testen ohne neuen Mechanismus)

| Was | Warum tot | Test |
|---|---|---|
| Spot kaufen nach extrem negativem Funding oder 7-Tage-Absturz, 4/8 Wochen | Überrendite ≤ 0 oder p > 0,05 | K2, R1 |
| Exposure halbieren bei 7-T-Funding > 90. Perzentil | t < 0 | K3, R1 |
| Trendfilter + Vol-Ziel als Edge | Sharpe < B&H | K4, R1 |
| Carry nur an, wenn 7-T-Funding > 10 % | schlechter als immer an | R1 nachträglich |
| KI-Prompt-Timing auf Wochen | nichts schlägt E-003M | research/versuche/ |
| Carry-Coins wöchentlich ausschließen nach negativem Funding, OI-Sprung oder Börsen-Gefälle (R1–R4) | Signal brutto da, Umschichtkosten fressen es; Regel feuert erst nach dem Schock | Q2, R2 |
| Börsen-Spread-Carry Binance/Bybit/Hyperliquid wöchentlich | Spread zu klein bzw. zu sprunghaft für 4 Kostenbeine | Q2 X1/X2, R2 |
| Laufzeit-Future immer rollen (ohne Bedingung) | knapp über T-Bill, ein Drittel negative Monate, schlechter als Perp | Q3 D1/D2, R2 |
| Liquidations-Kaskade (Preis + OI-Drop) kaufen oder Squeeze verkaufen, 1–24 h | keine Überrendite, auch vor Kosten | Q5, R2 |
| "Ethena/USDe drückt das Funding" als Erklärung | Vorzeichen falsch (USDe folgt dem Funding) | Q1-d, R2 |

## 3. Offene Fragen (priorisiert)

1. **F1 läuft:** Lebt Carry bei heutiger Lage forward auf irgendeiner Börse über T-Bill + Ausfall? (Auswertung ab 2027-04-17)
2. **Hyperliquid-Carry sauber:** HL-Perp-Kurse laden, Basisrisiko HL-Perp gegen Binance-Spot messen, HL-eigenes Ausfallrisiko (Vault/ADL/Smart Contract) als Basisrate. Warum zahlen HL-Longs doppelt so viel?
3. **Crash-Reversal-Kosten:** echte Ausführungskosten (Spread, Slippage) in Crash-Bars, mit Orderbuch des HL-Collectors oder Binance-aggTrades; entscheidet H-Q5.
4. Funding-Regime: Nur mit dem Holdout 2025-01..2026-06 wirklich klärbar. Kandidat für den Einmaltest, wenn F1 eine Schwelle braucht.
5. R5 (Top-4-Funding-Coins) mit realistischen Taker-Kosten und mehr Börsen; DSR heute 0.
6. B1-10 Mark-Price-Liquidationsrisiko des Short-Beins mit echten Mark-Preisen (ab 2023-10 vorhanden).

## 4. Test-Zähler

Kumulativ, Quant-Edge-Reihe (ohne die 37 KI-Prompt-Versuche, eigene Familie).

| Runde | Varianten | Herleitung | kumulativ |
|---|---|---|---|
| 1 | 66 | 14 vorab + 1 K1-Variante nachträglich + 10 K1 weitere Coins + 1 K1-12-Portfolio + 20 K2 weitere Coins + 10 K3 weitere Coins + 4 K3-Ablation + 6 Diagnose-Horizonte | 66 |
| 2 | 71 | 53 vorab (Q1 8, Q2 7, Q3 6, Q4 2, Q5 30) + N1 2 + N2 4 + N3 4 + N4 2 + N5 6 (Nachträge in 01-killkriterien-runde2.md) | **137** |
| Forward | 6 | F1 4, F2 2 (eigene Familie, kein Dev-Überlapp) | – |

Korrektur: Bonferroni α = 0,05 / 137 = **0,000365** für p-Werte. Deflated Sharpe Ratio (Bailey/López de Prado 2014) mit N = 135 (vor N4) und der Sharpe-Varianz über 19 Strategie-Reihen dieser Runde: K1 ETH 0,98, K1 BTC 0,88, D3 0,00, R5 0,00 (G). Vorsicht: die Reihen sind verschiedene Strategietypen, die Varianz und damit die Hürde (Sharpe 5,6) ist dadurch sehr hoch; die DSR ist hier eine konservative Grenze.

## 5. Holdout-Register

| Zeitraum | Status | Wer/was hat ihn berührt |
|---|---|---|
| bis 2024-12-31 | Entwicklung, frei | Runde 1, 2 |
| 2025-01-01 .. 2026-06-30 | **reserviert**, von Quant-Edge nie als Kursdaten geladen | R1: 0 Zeilen. R2: 0 Zeilen in 50 Dateien (geprüft, request.json). DefiLlama-USDe lieferte den Zeitraum im Transit, vor dem Speichern verworfen. **Literatur** zum Zeitraum gelesen (CME-Basis 2025, Börsenereignisse 2025–26 wie Bybit-Hack): Vorwissen, kein Test. Projektweit: Binance-Archiv des Hyblock-Threads ab 2025-01 (B-21) |
| 2026-07-01 .. 2026-10-16 | Dev-Nachschau, kein Beweis | R1, R2 (Q1, Q4, N4) |
| ab 2026-10-17 | **Forward F1/F2, vorab angemeldet** ([02-forward-test.md](02-forward-test.md)) | – |

## 6. Meta-Regeln (Filter für künftige Kandidaten)

1. **Zahlungsstrom vor Richtung.** Überlebt hat bisher nur, was einen laufenden Zahlungsstrom trägt (Funding, Basis). Alle Richtungs-Familien auf Tagen bis Monaten sind tot (K2, K3, K4, 37 KI-Versuche, Kaskade mit OI-Drop). Ein neuer Richtungs-Kandidat braucht einen Mechanismus, der in keiner toten Familie steckt.
2. **Umschlag-Budget vorab.** Brutto-Edge pro Jahr muss größer sein als Umschlag × 0,2 % je Seite und Bein. R1–R4 hatten Signal, starben am Umschlag. Den Umschlag vor dem Test schätzen und Kandidaten unter dem Budget gar nicht erst rechnen.
3. **Die Prämie sitzt beim Gezwungenen, nicht beim Mechanismus.** Hyperliquid zahlt doppeltes Funding (dort sitzen die Hebel-Käufer), die Crash-Prämie braucht keinen Liquidations-Nachweis und hält Stunden. Zuerst fragen: wo handelt die Gegenpartei, die nicht Nein sagen kann, und was kostet Ausführung genau dort.
