# Quant-Edge Runde 2: Wissensbasis erweitern

Stand 2026-10-16. Auftrag: Aarons Prompt "QUANT-EDGE RUNDE N". Vorarbeit: [bericht.md](bericht.md) (Runde 1). Wissensbasis: [WISSENSBASIS.md](WISSENSBASIS.md). Kill-Kriterien vorab: [01-killkriterien-runde2.md](01-killkriterien-runde2.md). Forward-Test vorab: [02-forward-test.md](02-forward-test.md).

Kennzeichnung: (G) gerechnet, (S) geschätzt mit Herleitung, (L) Literatur mit Quelle.

**Annahmen, weil die Eingaben fehlen:** Kapital 25 000 EUR, Börsen Binance, Bybit, Hyperliquid, OÜ nach estnischem Modell (einbehaltener Gewinn steuerfrei). Folge: Steuer verschiebt die Rangfolge "Carry gegen T-Bill" innerhalb der OÜ nicht, beide werden erst bei Ausschüttung besteuert (S). Bei 25 000 EUR ist Marktimpact vernachlässigbar (B1-16: erst bei ≈ 160 Mio USD bindend, S). Mac-Datenstand selbst geprüft (Abschnitt Q5).

---

## Die Antwort vorweg

1. **Kein Cheatcode, und Carry ist heute ökonomisch tot:** Seit Juli bringt Funding-Carry auf Binance netto 3,4 % (BTC) bzw. 2,2 % (ETH) pro Jahr, weniger als die T-Bill mit 3,8 % und noch vor dem Ausfallrisiko (G).
2. **Das Ausfallrisiko ist jetzt eine Zahl statt "unbekannt":** Eine Top-10-Börse fällt mit etwa 2,3 % pro Jahr aus (Spanne 1 bis 5 %, aus 70 Ereignissen seit 2014, S aus L); in heißen Funding-Phasen wie 2019 bis 2024 liegt das drei- bis elfmal unter der Schwelle, ab der es Carry tötet.
3. **Ob das niedrige Funding ein neues Regime ist, lässt sich nicht zeigen:** Es liegt unter dem Marktlage-Modell, aber innerhalb dessen normaler Fehler; der formale "Beweis" (t −4) war ein Messfehler, und Ethena treibt das Funding nicht nach unten, eher folgt USDe dem Funding (G).
4. **Neu und lebendig sind nur Hypothesen:** Hyperliquid zahlt in jeder Phase etwa doppelt so viel Funding wie Binance (G), Laufzeit-Futures nur bei hoher Basis schlagen die T-Bill knapp (G), und nach 15-Minuten-Crashs gibt es eine Rückprall-Prämie von 0,2 bis 0,3 % über 4 Stunden, die Protokoll-Kosten nicht überlebt (G).
5. **Zwei Behauptungen aus Runde 1 kippen:** Die Zwangsverkaufs-Prämie wird nicht "in Minuten" geerntet (sie hält über eine Stunde, und Liquidationen selbst tragen nichts bei), und "die Prämie schrumpft strukturell" ist eine Erzählung, keine Messung.

---

## Phase A: Wissensbasis

Angelegt mit Runde-1-Befunden B1-01..B1-16, toten Wegen, Test-Zähler (Runde 1: 66 Varianten, Herleitung in WB §4) und Holdout-Register. Jetzt vollständig fortgeschrieben, siehe [WISSENSBASIS.md](WISSENSBASIS.md).

## Phase B: Fragenauswahl

Bewertung je 1 bis 5. Score = Erkenntnisgewinn × Testbarkeit ÷ Aufwand. Gewählt nach Unsicherheitsreduktion, nicht nach Edge-Klang.

| Frage | Gewinn | Testbar | Aufwand | Score | gewählt |
|---|---|---|---|---|---|
| Q4 Börsenausfall-Basisrate (+ Stablecoin-Tail) | 5 (Vorzeichen von K1) | 4 (Literatur vollständig) | 2 | **10** | ja |
| Q1 Regime oder Zyklus | 4 (lebt K1 noch?) | 3 (Holdout-Lücke, 3,5 Monate danach) | 2 | **6** | ja |
| Q3 Laufzeit-Futures gegen T-Bill | 3 | 3 (Binance-Quartale via Mac, kein CME) | 2 | **4,5** | ja |
| Q9 Börsen-Spread-Carry (aus WB) | 3 | 3 | 2 | 4,5 | als Teil von Q2 |
| Q2 Funding-Streuung, Ausschlussregel | 3 | 2 (nur 1 bis 2 Crowd-Schocks) | 3 | 2 | ja, zusammen mit Q9 |
| Q5 Intraday-Zwangsfluss | 5 (entscheidet Wert der Liquidations-Engine) | 2 (keine Liquidationsdaten, nur OI-Proxy) | 4 | 2,5 | ja (vor Q8) |
| Q8 Mark-Price-Liquidation des Short-Beins (B1-10) | 2 | 2 | 2 | 2 | nein |
| Q6 Funding-Elastizität eigener Größe | 2 (bei 25 kEUR irrelevant) | 1 | 3 | 0,7 | nein |

Q2 und Q9 laufen zusammen, weil sie dieselben Daten brauchen. Damit 5 Fragen.

## Phase C: Daten und Regeln

- **Daten (alle über Aarons Mac, Holdout nie übertragen außer DefiLlama-Transit, verworfen):** Bybit- und Hyperliquid-Funding (12 Coins), Binance-Quartals-Futures USDT-M und Coin-M (BTC, ETH), FRED-T-Bill DTB3, Binance-Open-Interest täglich (12 Coins) und 15-minütlich (BTC, ETH), Binance-Perp-15-Minuten-Kerzen (BTC, ETH), USDe-Umlauf. 50 Dateien, sha256 geprüft, 0 Zeilen im Holdout: `research/quant-edge/daten-r2/` (request.json mit 16 238 Requests).
- **Q4-Liste:** 70 Ereignisse plus 9 Derivate-Notizen, `daten-r2/q4/events.csv`, Methode in `daten-r2/q4/notes.md`. Quellen vor 2020 meist Wikipedia aus dem Gedächtnis zitiert, nicht neu abgerufen; Rangangaben "Top-10 zur Zeit" sind Ermessen (S).
- **Datenfehler gefunden:** Binance-OI-Tageswerte 0,0 an drei Tagen (2022-03-07, 2024-07-10, 2024-07-12) → als fehlend behandelt. Kein Binance-Liquidations-Archiv vorhanden (S3-Listing leer, 404).
- **Zähler:** 53 vorab + 18 nachträglich = 71 in dieser Runde, kumulativ **137**, Bonferroni α = **0,000365**. Nachträge N1..N5 mit Zeitpunkt in der Kill-Kriterien-Datei.

---

## Q1 Regimewechsel Carry: nicht unterscheidbar

| | BTC | ETH | Kz. |
|---|---|---|---|
| Stärkster Bruch im Monats-Funding 2019-09..2024-12 | 2021-06: 25,6 → 8,8 % | 2021-06: 38,6 → 8,5 % | G |
| sup-F p (AR(1)-Bootstrap) | 0,23 | 0,07 | G |
| 30-T-Funding 2026-08..10 tatsächlich / Modell (Rendite, Vol) | 6,3 / 11,7 % | 4,7 / 15,5 % | G |
| Residuum, Newey-West-t | −5,4 pp, t −4,2 | −10,8 pp, t −3,5 | G |
| **Gegentest:** gleiches Modell 2023–24 außerhalb Stichprobe | −5,2 pp, t −4,1 | −0,5 pp | G |
| **Empirisches p (Leave-one-year-out-Fenster gleicher Länge)** | **0,47** | **0,17** | G |
| Mit OI-Änderung als Regressor: Residuum, emp. p | −1,8 pp, 0,53 | −5,5 pp, 0,44 | G |
| USDe-Wachstum gegen Residuum (16 Monate) | Korr. +0,61, p 0,006 | +0,33, p 0,07 | G |
| Anteil Zahlungen unter Basiszins 0,01 %/8 h, 2026-H2 (2022) | 86 % (69 %) | – | G |

**Kill-Urteil nach Vorab-Regel:** formal "strukturell niedriger bestätigt" (p < α). **Gegentest kippt es:** Newey-West auf 80 überlappenden Tagen mit starker Persistenz unterschätzt den Fehler; dieselbe Spezifikation lag 2023–24 bei BTC genauso weit daneben. Empirisch liegt 2026-H2 im normalen Fehlerband (p 0,47 / 0,17). **Urteil: nicht unterscheidbar.** Nachträgliche Tests dürfen nicht bestätigen, aber entwerten; hier entwerten sie.

**USDe:** Vorzeichen positiv: USDe wächst, wenn Funding über dem Modell liegt. Das passt zu "USDe ist eine Folge des Fundings" (seine Rendite ist das Funding), nicht zu "USDe drückt das Funding". USDe ist mit 4,7 Mrd USD heute kleiner als Ende 2024 (5,9 Mrd, G). Unter α nicht bestätigt (16 Monate).

**Was bleibt:** Die Zahlungsverteilung 2026-H2 sieht aus wie ein Bärenjahr (fast nie über dem Basiszins), obwohl der Kurs stieg (30-T-Rendite im Mittel +11 % BTC). Das ist der stärkste Hinweis auf ein anderes Regime, aber deskriptiv. Die eigentliche Antwort liegt im reservierten Holdout 2025-01..2026-06, also genau dort, wo der Übergang passiert wäre.

**Folge für K1:** Ob zyklisch oder strukturell, K1 ist heute unter der Hürde (Q4). Die Frage "kommt Funding zurück?" ist eine Prognose, die wir nicht machen. Daher Zustandsregel statt Prognose: Wiedervorlage, wenn 30-T-Funding > 10 % (in F1 festgeschrieben).

## Q2 Funding-Streuung über Coins und Börsen: Regeln tot, eine Hypothese

Benchmark: 12-Coin-Carry gleichgewichtet mit Umschichtkosten, 2019-09..2024-12: +6,3 % p.a., DD −6,6 %, Sharpe 3,3 (G).

| Regel | CAGR | Max-DD | Sharpe | SOL vor FTX raus? | ohne Umschichtkosten (N5) | Urteil |
|---|---|---|---|---|---|---|
| R1 > 1/3 negative Zahlungen | 5,0 % | −10,9 % | 2,0 | nein | 8,1 % / −4,7 % | tot |
| R2 7-T-Funding < 0 | 4,2 % | −11,5 % | 1,8 | nein | 9,0 % / −3,7 % | tot |
| R3 OI +30 % und Funding < 0 (ab 2022) | −0,1 % (Bench 0,4 %) | −7,4 % | 0,0 | nein | 6,6 % / −6,2 % | tot |
| R4 Binance-Bybit-Gefälle > 10 pp | 2,7 % | −11,9 % | 1,3 | nein | 6,3 % / −5,6 % | tot |
| **R5 nur Top-4 nach 30-T-Funding** | **6,7 %** | **−2,2 %** | **3,8** | **ja** | 11,4 % / −1,2 % | **Hinweis** (p 0,47, DSR 0,00) |
| X1 Spread-Carry Binance/Bybit | ≈ 0 % | −6,3 % | – | – | – | tot (69 % neg. Fenster) |
| X2 Spread-Carry Binance/Hyperliquid (2023-05+) | 4,0 % | −1,7 % | 3,8 | – | – | tot (49 % neg. Fenster), Obergrenze |

Alles G.

**Kern:** Die Ausschlussregeln haben brutto Signal (ohne Kosten bessere Rendite und kleineren DD), aber sie feuern erst, nachdem der Schock da ist, und schichten zu oft um. **Keine Regel hätte SOL vor dem 2022-11-09 erkannt** außer R5, und R5 nur zufällig, weil SOL-Funding vorher nicht unter den Top 4 war, nicht weil es eine Warnung gab. Ein "SOL-Schock vorab erkennen" ist mit Funding, OI und Börsen-Gefälle auf Tagesbasis nicht gelungen.

**Gegenhypothese R5:** "Top-4-Funding" konzentriert auf die gerade teuersten Hebel-Coins; das sollte das Crowd-Risiko erhöhen, nicht senken. Test: SOL-Episode, DD-Zeitpunkt. Ergebnis: Der DD sinkt, weil Bären-Coins mit negativem Funding (TRX, BNB, DOT) nie dabei sind. Das ist Momentum im Funding, kein Schutz vor Schocks. Sharpe-Differenz nicht signifikant.

**Börsen-Niveaus (Funding brutto p.a., G):**

| | Binance 2024 / 2026-H2 | Bybit 2024 / 2026-H2 | Hyperliquid 2024 / 2026-H2 |
|---|---|---|---|
| BTC | 11,9 / 5,9 % | 12,0 / 4,6 % | **24,1 / 8,7 %** |
| ETH | 13,0 / 4,5 % | 12,5 / 4,2 % | **22,0 / 9,2 %** |
| SOL | 13,6 / 3,4 % | 14,0 / 2,3 % | 28,1 / 7,2 % |

Binance und Bybit sind praktisch derselbe Markt. **Hyperliquid zahlt in jeder Phase etwa das Doppelte.** Plausible Ursache: Dort sitzen Privatanleger ohne Börsenkonto mit Hebel-Vorliebe, und das Arbitrage-Kapital ist durch Venue-Risiko (On-Chain, Vault) gebremst (S). Genau das, was Phase 0 von Runde 1 vorhersagt: Die Prämie sitzt dort, wo der Arbitrageur gefesselt ist.

**Nachtrag N4 (nachträglich, zählt nicht als Bestätigung):** K1 mit Short auf Hyperliquid, Spot auf Binance, ohne Hyperliquid-Kurse (Binance-Perp als Stellvertreter, Basisrisiko nicht modelliert, Obergrenze): 2023-05..2024 BTC +13,0 %, ETH +13,7 % p.a., DD < 1 %; seit 2026-07 Laufrate 5,4 % / 5,4 % (G). Läuft als F1 forward.

## Q3 Laufzeit-Futures statt Perp: knapp über T-Bill, nur mit Bedingung

Fenster 2021-03..2024-12 (USDT-M), 2020-09..2024-12 (Coin-M). Hürde: T-Bill derselben Zeit, Mittel 2,4 % (G).

| | CAGR auf Kapital | über T-Bill | Max-DD | neg. 30-T-Fenster | Sharpe | Urteil |
|---|---|---|---|---|---|---|
| D1 BTC immer gerollt | 4,7 % | +1,6 pp | −5,7 % | 34 % | 1,1 | tot |
| D1 ETH | 4,4 % | +1,3 pp | −6,7 % | 34 % | 0,8 | tot |
| D2 BTC Coin-M | 3,2 % | +0,2 pp | −5,9 % | 41 % | – | tot |
| D2 ETH Coin-M | 2,4 % | −0,5 pp | −10,5 % | 44 % | – | tot |
| **D3 BTC nur bei Basis > T-Bill + 2 pp** | **5,5 %** | **+2,4 pp** | −5,7 % | 21 % | 1,3 | **lebt (Dev)**, DSR 0,00 |
| **D3 ETH** | **6,1 %** | **+3,0 pp** | −6,7 % | 14 % | 1,1 | **lebt (Dev)**, DSR 0,00 |
| K1 Perp im selben Fenster BTC / ETH | 5,9 / 5,6 % | – | −0,4 / −1,8 % | 10 / 15 % | 8,9 / 6,9 | – |

Alles G. Mittlere Basis beim Rollen ≈ 8,9 % p.a. (G). D3 war bei BTC in 10, bei ETH in 9 von 16 Quartalen drin; 2022 bis Mitte 2023 lag die Basis unter T-Bill + 2 pp (z. B. 2022-12: 1,8 % vs. T-Bill 4,3 %).

**Gegenhypothese:** "Die Kontinuitätsreihe springt am Verfallstag falsch." Test: Preis des neuen Kontrakts am Vortag (NEXT) gegen denselben Kontrakt am Verfallstag (CURRENT) für alle 16 Verfälle; Abweichungen entsprechen der Tagesbewegung, keine Sprünge (G, `r2_q3.json` data_check).

**Warum Laufzeit-Carry schlechter ist als Perp:** Die Basis ist fixiert, aber bis zum Verfall schwankt sie mit dem Markt (Mark-to-Market), daher ein Drittel negative Monate und DD −6 %. Plus 4 Kostenbeine pro Quartal. **Vorteil bleibt real:** kein Funding-Umkehr-Risiko im Quartal. CME-Basis als Vergleich (L): Feb 2024 ≈ 25 %, Ende 2024 15–20 % (CF Benchmarks), Januar 2026 ≈ 4,7–5 % (Bloomberg/Amberdata, Advisor Perspectives 2026-01-22). Die CME-Zahlen stammen aus dem Holdout-Zeitraum, sind Literatur und kein Test; sie zeigen dieselbe Schrumpfung wie das Perp-Funding.

**Urteil:** D1/D2 tot. D3 lebt in der Entwicklung, aber mit Sharpe ≈ 1,2 auf 3,8 Jahren nicht von Glück zu trennen (DSR 0). Kein eigener Forward-Test, weil die Basis heute (≈ 5 % CME, L) unter T-Bill + 2 pp liegt: D3 wäre ohnehin aus.

## Q4 Börsenausfall-Basisrate: 2,3 % pro Jahr, kein Killer in heißen Phasen

**Liste:** 70 Ereignisse 2014..2026-10 (Insolvenzen, Hacks, Betrug, Beschlagnahmen, Auszahlungsstopps > 7 Tage) plus Verleiher (Celsius, Voyager, Vauld, Hodlnaut). 18 trafen eine Top-10-Börse; davon 14 gedeckte Hacks (Kunden ohne Verlust, z. B. Bybit 2025 1,46 Mrd USD) und 3 echte Totalausfälle: **Mt.Gox 2014, BTC-e 2017, FTX 2022** (L, Quellen in events.csv). Bitfinex 2016: 36 % Abschlag, in 8 Monaten zurückgezahlt.

| Größe | niedrig | zentral | hoch | Kz. |
|---|---|---|---|---|
| Ausfallrate Top-10-Börse p.a. | 1,0 % | **2,3 %** (3 / 128 Börsen-Jahre; Poisson-KI 0,5–6,9 %) | 5,0 % | S aus L |
| Verlust bei Ausfall, USD-Forderung | 0 | 0,3 (FTX zahlte 103–143 % der USD-Forderung, aber Jahre gesperrt) | 0,7 | S aus L |
| Verlust bei Ausfall, in Coins | 0,5 | 0,75 (Mt.Gox ≈ 0,79, FTX ≈ 0,8 in BTC) | 0,95 | S aus L |
| Erwarteter Verlust p.a. | 0 % | 0,7 % (USD) / 1,7 % (Coins) | 4,8 % | S |
| Gedeckte Hacks Top-10 | – | ≈ 11 % p.a., Kundenverlust ≈ 0 | – | S aus L |

Literatur (L): Moore/Christin 2013: 18 von 40 Börsen geschlossen, Median-Lebensdauer 381 Tage, höheres Volumen senkt das Schließungsrisiko (HR 0,84). Mukherjee/Moore 2022: 40 % von 822 Börsen geschlossen, Median-Überleben ≈ 7 Jahre, ohne Fiat 60 % höhere Schließungs-Chance. Polymarket Anfang 2026: ≈ 5 % für "große Börse insolvent 2026" (Stimmung, kein Modell).

**K1-Erwartungswert (vorab angemeldete Rechnung):**

| | Carry netto | T-Bill | nach Ausfall zentral (USD / Coins) | Break-even-Ausfallrate (USD / Coins) | Urteil |
|---|---|---|---|---|---|
| BTC 2019–2024 | 8,3 % | 2,4 % | 7,7 / 6,6 % | 19,7 / 7,9 % p.a. | lebt |
| ETH 2019–2024 | 10,2 % | 2,5 % | 9,5 / 8,5 % | 25,7 / 10,3 % p.a. | lebt |
| BTC seit 2026-07 (Laufrate) | 3,4 % | 3,8 % | 2,7 / 1,7 % | < 0 | **tot heute** |
| ETH seit 2026-07 (Laufrate) | 2,2 % | 3,8 % | 1,5 / 0,5 % | < 0 | **tot heute** |

Alles G (Carry, T-Bill) bzw. S (Ausfallabzug). **Kill-Urteil:** "K1 ökonomisch tot heute": ja, BTC und ETH. "K1 tot in jeder Funding-Lage": nein, in heißen Phasen liegt die Basisrate 3- bis 11-mal unter dem Break-even.

**Widerspruch zu Runde 1 offen:** Runde 1 rechnete einen Börsenausfall als einmaliges −50 %-Ereignis über 5 Jahre (→ −4,9 % p.a.). Das entspricht einer Ausfallrate von ≈ 20 % pro Jahr bei LGD 0,5 und war damit zu pessimistisch. Mit Basisrate statt Einmal-Szenario kostet das Ausfallrisiko 0,7 bis 1,7 % p.a., nicht 13 Prozentpunkte. Umgekehrt war Runde 1 zu optimistisch bei der Nachschau: Ihre Schätzung 2,8 % / 1,5 % netto für 2026-H2 (S) ist gerechnet 3,4 % / 2,2 % Laufrate bzw. 1,5 % / 0,3 % mit Ein- und Ausstieg (G), das Bild bleibt gleich.

**Stablecoin-Tail (Teil von Q4):** USDC fiel im März 2023 kurz auf ≈ 0,88 USD (L, Runde 1). Carry hält Collateral in USDT/USDC; ein Depeg trifft das Margin-Bein. Keine eigene Basisrate gerechnet; offene Frage bleibt.

## Q5 Intraday-Zwangsfluss: Liquidationen tragen nichts, der Crash-Rückprall schon (vor Kosten)

Daten: Binance-Perp 15-Minuten-Kerzen und OI, BTC und ETH, 2022-01..2024-12, ≈ 105 000 Bars je Coin. Ereignisse entclustert, 110 bis 234 je Variante. Überrendite gegen alle Bars gleicher Haltedauer, in Prozent je Trade (G):

| Variante | BTC 1 h | BTC 4 h | BTC 24 h | ETH 1 h | ETH 4 h | ETH 24 h | Urteil |
|---|---|---|---|---|---|---|---|
| Kaskade (Crash + OI-Drop), sofort | −0,05 | +0,15 | −0,09 | −0,05 | −0,13 | −0,14 | tot |
| Short-Squeeze verkaufen | −0,06 | −0,04 | −0,41 | −0,17 | +0,08 | −0,22 | tot |
| Kaskade, 15 min später | +0,10 | +0,15 | +0,05 | −0,02 | −0,01 | +0,04 | tot |
| Kaskade, 1 h später | +0,15 | +0,22 | +0,07 | −0,08 | −0,07 | −0,04 | tot |
| **Nur Preis-Crash, sofort** | +0,03 | **+0,21** (p 0,002) | −0,05 | +0,15 | **+0,29** (p 0,002) | +0,39 | **"existiert, nicht erntbar"** (4 h) |
| Nur Preis-Crash 4 h, 15 min später (N3) | | +0,19 (p 0,006) | | | +0,29 (p 0,0006) | | Gegentest bestanden |
| Nur Preis-Crash 4 h, 1 h später (N3) | | +0,19 (p 0,01) | | | +0,17 (p 0,04) | | Gegentest bestanden |

Nach 0,4 % Rundreise (Protokoll) ist jede Variante negativ. Mit 0,05 % Taker je Seite (Binance VIP0, L) blieben beim Preis-Crash 4 h +0,07 bis +0,19 % je Trade, **vor Slippage im Crash**, die nachträglich nicht messbar ist. Kein p unter α = 0,000365. Beide Hälften (2022–23, 2024) positiv.

**Gegenhypothese 1: Bid-Ask-Bounce** (der Crash-Schluss liegt am Geldkurs, der nächste Kurs springt mechanisch zurück). Test N3: Einstieg 15 min und 1 h später. Die Prämie bleibt (BTC +0,19 / +0,19 %, ETH +0,29 / +0,17 %). Kein Bounce-Artefakt.

**Gegenhypothese 2: Das ist die Liquidationsprämie.** Dann müsste der OI-Drop-Filter (Positionen werden zwangsgeschlossen) die Prämie verstärken. Er löscht sie. **Was zurückprallt, sind Crashs ohne Positionsabbau**, also eher Panik-Verkäufe und dünne Bücher als Liquidationen (S).

**Widersprüche zu Runde 1:**
- Runde 1 (nachträgliche Diagnose): "Prämie wird in Minuten bis Stunden geerntet, von denen, die im Moment der Liquidation Liquidität stellen." Messung: Mit 1 h Verzögerung bleibt sie fast vollständig, und Liquidationen selbst tragen nichts. **Latenz ist nicht der Engpass, Kosten sind es.**
- Runde 1: "Die Engine kann einen Edge nur intraday haben." Präziser jetzt: Auch intraday zeigt der Liquidations-Proxy (OI-Drop) keinen Edge. Ein Wert der Liquidations-Engine müsste aus etwas kommen, das OI-Drops nicht zeigen (Liquidations-Niveaus vor dem Ereignis, nicht danach). Das ist eine Information für Aarons Entscheidung, keine Empfehlung zum Abbruch.

**Mac-Datenstand:** Hyperliquid-Collector läuft seit 2026-10-16 ≈ 12:17 UTC, 18 von 18 Viertelstunden-Marken bis 16:45 UTC, 17 MB, 10 951 Nutzer verfolgt (6 895 mit Position), Positions-Abdeckung BTC long 6,5 % / short 15,2 %, ETH long 4,2 % / short 15,7 % (G, vom Collector gemeldet). Zu kurz für einen Test. Binance hat kein öffentliches Liquidations-Archiv (S3-Listing leer, 404).

---

## Phase D: Was sich an der Wissensbasis ändert

- **Neu lebendig (Hypothesen):** B2-16/17 Hyperliquid-Carry, B2-10 D3, B2-08 R5, B2-22 Crash-Rückprall.
- **Neu tot:** R1–R4, X1, X2, D1, D2, Kaskaden-Kauf, Squeeze-Verkauf, "USDe drückt Funding".
- **Ersetzt:** B1-04 und B1-07 (Einmal-Ausfall-Szenario) durch B2-12..14 (Basisrate).
- **Herabgestuft:** B1-05 "Prämie schrumpft strukturell" → Niveau gemessen, Ursache offen. B1-12 "wird in Minuten geerntet" → widerlegt.
- **Methodik-Lektion (B2-02):** Newey-West auf kurzen, persistenten Fenstern überschätzt die Signifikanz grob. Künftig immer empirische Nullverteilung gleicher Fensterlänge.

---

## Phase E: Meta-Lernen

### 1. Muster über zwei Runden

| | Zwangsart | Horizont | Kapazität | Ausgang |
|---|---|---|---|---|
| K1 Carry Binance | Hebel-Miete, vertraglich, alle 8 h | laufend | groß | lebt (Dev), heute unter Hürde |
| K1 Carry Hyperliquid | dito, Gegenpartei stärker gefesselt | laufend | mittel | Hypothese |
| D3 Laufzeit-Basis | Hebel-Miete, fixiert | Quartal | groß | lebt (Dev), schwach |
| Crash-Rückprall 4 h | Liquiditäts-Stress, kein Liquidations-Nachweis | Stunden | klein | Prämie da, Kosten zu hoch |
| K2, K3, K4, KI-Prompts | Richtung auf Tagen bis Monaten | Wochen | – | tot |
| R1–R4 | Timing der Coin-Auswahl | Wochen | – | tot an Umschlag |
| Kaskade mit OI-Drop | Liquidation | Stunden | – | tot, auch brutto |

**Lebende Edges haben gemeinsam:** Sie sind ein Zahlungsstrom, den man trägt (kein Kursziel), der Zwang ist vertraglich oder strukturell, und die Prämie ist an der Börse am größten, an der das Arbitrage-Kapital am stärksten gefesselt ist. **Tote haben gemeinsam:** Sie wollen eine Richtung oder einen Zeitpunkt treffen, oder sie schichten so oft um, dass 0,2 % je Seite den Brutto-Edge auffressen.

**Drei Filterregeln (auch in WB §6):**
1. **Zahlungsstrom vor Richtung.** Neue Richtungs-Kandidaten auf Tagen bis Monaten nur mit einem Mechanismus, der in keiner toten Familie steckt.
2. **Umschlag-Budget vorab.** Brutto-Edge p.a. > Umschlag × 0,2 % je Seite und Bein, vor dem Test geschätzt.
3. **Erst die Börse des Gezwungenen finden, dann das Signal.** Die gleiche Prämie ist venue-abhängig doppelt so groß; Ausführungskosten genau dort entscheiden.

### 2. Annäherung an den Cheatcode

Ampel: 🟢 erfüllt, 🟡 teilweise/unsicher, 🔴 fehlt.

| Kandidat | (1) Quelle | (2) Forward-Test | (3) Skalierung (25 kEUR bis ≈ 1 Mio) | (4) Tail modelliert | Nächste Lücke |
|---|---|---|---|---|---|
| K1 Binance BTC/ETH | 🟢 Hebel-Miete | 🔴 läuft ab 2026-10-17 (F1); Nachschau unter Hürde | 🟢 | 🟡 Ausfall jetzt Basisrate, Stablecoin-Depeg nicht | Funding über Hürde in F1 |
| K1 Hyperliquid | 🟢 stärker gefesselte Gegenpartei | 🔴 nachträglich gefunden, F1 | 🟡 HL-Tiefe kleiner | 🔴 HL-Venue-Risiko, Basis HL-Perp/Spot nicht gemessen | HL-Kurse + HL-eigene Ausfallbasis |
| D3 Laufzeit-Basis | 🟢 | 🔴 heute aus (Basis zu klein) | 🟢 | 🟡 MTM-DD −6 % gemessen, Börse wie K1 | mehr Quartale; DSR 0 |
| H-Q5 Crash-Rückprall | 🟡 Stress, aber nicht Liquidation | 🔴 F2 ab 2026-10-17 | 🟡 Crash-Liquidität | 🟡 Slippage unbekannt | echte Ausführungskosten in Crash-Bars |
| R5 Top-4-Funding | 🟡 Funding-Momentum | 🔴 | 🟢 | 🟡 | Signifikanz (p 0,47) |

**Abstand zum Cheatcode:** Kein Kandidat hat mehr als zwei grüne Felder. Die Lücke ist bei allen dieselbe: der Forward-Test. Kein Rechnen auf alten Daten kann sie schließen.

### 3. Forward-Test-Plan (vorab angemeldet, [02-forward-test.md](02-forward-test.md), committed vor Fensterbeginn)

- **F1 Carry heute:** BTC und ETH, Short auf Binance bzw. Hyperliquid, 2026-10-17 bis 2027-04-16. Besteht, wenn für beide Coins auf mindestens einer Börse netto > T-Bill + 1 pp + 0,7 % Ausfallabzug und DD > −5 %. Sonst geparkt bis 30-T-Funding > 10 %.
- **F2 Crash-Rückprall 4 h:** exakt die Regel aus Q5 (Preis-Crash, 15 min Verzögerung), bis 60 Ereignisse je Coin, längstens 2027-10-16. "Erntbar mit Taker": Brutto-Überrendite > 0,10 % und t > 2; "erntbar mit Protokoll-Kosten": > 0,40 %.
- Beides ist aus öffentlichen Historien nachträglich exakt auswertbar, es muss nichts live laufen. Nur Slippage fehlt; F2 wird deshalb höchstens zum Kandidaten für einen kleinen Echtgeld-Test mit gemessener Ausführung.

### 4. Eigene Bias-Prüfung

- **Data Snooping:** Der Hyperliquid-Carry (N4) entstand, nachdem ich die Funding-Niveaus je Börse gesehen hatte. Deshalb nur Hypothese und Forward-Test. Die Basiszins-Verteilung 2026-H2 habe ich vor Nachtrag N1 gesehen (deskriptiv angemeldet, aber ein Blick auf Ergebnisdaten vor einer Spezifikationsänderung).
- **Survivorship:** Unser Börsen-Set (Binance, Bybit, Hyperliquid) sind Überlebende. Die Top-10-Basisrate zählt Börsen, die zur Zeit groß waren, aber die Einstufung ist Ermessen und Wash-Trading verzerrt Ränge. Hyperliquid hat keine lange Geschichte; "noch nie ausgefallen" ist keine Rate. Kleine, früh gestorbene Börsen fehlen in der Liste (eine Zählung fand 75 Schließungen allein 2020, die Liste hat 3).
- **Narrative-Fehlschluss:** "Ethena drückt das Funding" klang gut und war in Runde 1 als plausibler Treiber genannt; das Vorzeichen spricht dagegen. "Die Liquidations-Engine erntet die Intraday-Prämie" klang gut; der OI-Proxy zeigt das Gegenteil.
- **Bestätigung der Runde-1-Story:** Gegenmaßnahme war, jede Runde-1-Behauptung als Hypothese mit Gegentest zu behandeln. Zwei sind gekippt (Minuten-Ernte, strukturelle Schrumpfung), eine ist präzisiert (Ausfallrisiko kleiner als angenommen). Die Kernstory "Edge = Bilanz, Kosten, Risiko" wird bestätigt, und das ist verdächtig bequem: Sie ist so allgemein, dass fast jedes Ergebnis sie stützt.
- **Messinstrument:** Ich hätte Q1 beinahe als "bestätigt" berichtet, weil die Vorab-Regel ein Newey-West-t vorsah. Lektion: Vorab-Kriterien schützen vor Snooping, nicht vor einem schlechten Instrument.
- **Literatur aus dem Holdout:** CME-Basis 2025, Bybit-Hack 2025 und Ereignisse 2025–26 wurden gelesen. Das ist Vorwissen über den reservierten Zeitraum und senkt den Wert eines späteren Holdout-Tests leicht; im Register vermerkt.
- **Agent-Recherche:** Die Q4-Liste stammt von einem Recherche-Agenten; Quellen vor 2020 meist aus dem Gedächtnis zitiert. Die drei Totalausfälle (Mt.Gox, BTC-e, FTX) sind unstrittig; die Spanne ist robust gegen einzelne Fehler, die LGD-Zahlen weniger.

---

## Was ich noch nicht weiß

- Ob 2025-01..2026-06 einen echten Regimewechsel enthält. Die Daten dafür liegen im reservierten Holdout.
- Wie groß das Basisrisiko zwischen Hyperliquid-Perp und Binance-Spot ist und wie hoch Hyperliquids eigene Ausfallrate liegt (On-Chain-Venue, Vault, Auto-Deleveraging).
- Was ein Crash-Bar wirklich an Ausführung kostet (Spread, Slippage, Teilausführung).
- Ob Stablecoin-Collateral (USDT/USDC) eine eigene, relevante Ausfallrate hat.
- Warum Hyperliquid-Longs doppelt so viel zahlen und ob das bleibt, wenn mehr Arbitrage-Kapital kommt.
- Aarons echte Rahmendaten (Kapital, Börsen, Steuer); alle Zahlen hier gelten unter den Annahmen oben.

## Die 3 Fragen für Runde N+1

1. **Hyperliquid-Carry sauber messen.** HL-Perp-Kurse und Mark-Preise laden, Basisrisiko gegen Binance-Spot, Liquidationsabstand des Short-Beins, HL-Ausfall-Basisrate (Incidents seit 2023). *Begründung:* B2-16 ist der einzige Befund dieser Runde, der K1 bei heutiger Lage über die Hürde heben könnte (Laufrate 5,4 % vs. T-Bill 3,8 %), und er ist nachträglich und ohne Basisrisiko gerechnet.
2. **Ausführungskosten im Crash.** Mit dem Orderbuch des Hyperliquid-Collectors und Binance-aggTrades (Dev-Zeitraum) messen, was ein Markt-Kauf in einem 0,2-%-Quantil-Bar wirklich kostet. *Begründung:* H-Q5 hat eine Prämie von 0,2 bis 0,3 %, die genau an den Kosten hängt; das ist die eine Zahl, die Kill oder Kandidat entscheidet.
3. **Holdout-Einmaltest für das Funding-Regime, vorab angemeldet.** Ein einziger Test: Liegt das Binance-BTC/ETH-30-T-Funding 2025-01..2026-06 im Mittel unter dem Marktlage-Modell mit OI (Q1-c-Spezifikation, eingefroren), mit empirischem p aus der Entwicklung? *Begründung:* Q1 kann ohne diesen Zeitraum nicht entschieden werden, und die Antwort entscheidet, ob man auf Funding-Rückkehr warten oder Carry endgültig begraben sollte. Braucht Aarons Freigabe, weil der Holdout dann für diese Frage verbrannt ist.

---

## Anhang: Dateien und Reproduktion

- Code (Repo, Branch `claude/quant-edge-runde-2-os2kdl`, Ordner `research/quant-edge/r2/`): `r2_common.py`, `q1_regime.py`, `q1_empirical_null.py`, `q2_dispersion.py`, `q3_dated.py`, `q4_ev.py`, `q5_intraday.py`, `q5_posthoc.py`, `k1_hl_posthoc.py`, `dsr.py`. Jede Datei beginnt mit dem Look-ahead-Audit. Lauf: `cd research/quant-edge/r2 && python3 q1_regime.py` usw. (pandas, numpy, scipy).
- Ergebnisse JSON: `research/quant-edge/out/r2_*.json`.
- Rohdaten mit sha256: `research/quant-edge/daten-r2/` (Repo und geteilter Ordner), Abrufskript `fetch.py`, alle Requests in `request.json`. Q4-Liste: `daten-r2/q4/`.
- Runde-1-Rohdaten liegen im geteilten Ordner `research/quant-edge/daten/` (sha256.txt), nicht im Repo.

### Literatur (neu in Runde 2)
- Bailey, López de Prado (2014): The Deflated Sharpe Ratio. Journal of Portfolio Management.
- Andrews (1993): Tests for Parameter Instability and Structural Change With Unknown Change Point. Econometrica.
- Moore, Christin (2013): Beware the Middleman: Empirical Analysis of Bitcoin-Exchange Risk. Financial Cryptography.
- Moore, Christin, Szurdi (2018): Revisiting the Risks of Bitcoin Currency Exchange Closure. ACM TOIT 18(4).
- Mukherjee, Moore (2022): Cryptocurrency Exchange Closure Revisited (Again). APWG eCrime.
- Milunovich, Lee (2021): Cryptocurrency Exchanges: Predicting which Markets will Remain Active.
- CF Benchmarks: Revisiting the Bitcoin Basis (Daten bis 2025-09-30), https://blog.cfbenchmarks.com/revisiting-the-bitcoin-basis-how-momentum-sentiment-impact-the-structural-drivers-of-basis-activity
- Bloomberg (S. Shukla), "Wall Street Pulls Back From a Money-Spinning Bitcoin Trade", via Advisor Perspectives 2026-01-22, https://api.advisorperspectives.com/articles/2026/01/22/wall-street-pulls-back-bitcoin-trade
- Einzelquellen der 70 Ausfallereignisse: `daten-r2/q4/events.csv`.
