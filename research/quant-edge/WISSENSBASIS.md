# Quant-Edge Wissensbasis (WB)

Stand: Runde 1 übernommen (2026-10-16). Wird jede Runde vollständig fortgeschrieben.
Kennzeichnung: (G) gerechnet, (S) geschätzt mit Herleitung, (L) Literatur mit Quelle.

**Cheatcode-Definition:** Rendite nach Kosten, die (1) einen benannten Zwang oder eine Vorliebe einer Gegenpartei als Quelle hat, (2) in einem echten Forward-Test hält, (3) bei realistischer Größe skaliert, (4) keinen unmodellierten Totalverlust-Tail hat. Fehlt eines, ist es eine Hypothese.

## 1. Befunde

| ID | Aussage | Zahl | Kz. | Datum | Status |
|---|---|---|---|---|---|
| B1-01 | Rendite unter perfekter Information = Bezahlung fürs Tragen (Risiko, Hebel, Sofortigkeit, Versicherung, Zwangsfluss), nicht fürs Wissen | – | L (Grossman/Stiglitz 1980, Shleifer/Vishny 1997) | 2026-10-16 | lebt (Rahmen) |
| B1-02 | K1 Funding-Carry (Spot long, Perp short) BTC, Rendite auf 1,5-faches Kapital nach Kosten | +8,4 % p.a., DD −1,8 %, 2019-09..2024-12 | G | 2026-10-16 | lebt (Dev) |
| B1-03 | K1 ETH dito | +10,2 % p.a., DD −1,8 % | G | 2026-10-16 | lebt (Dev) |
| B1-04 | K1 mit einem Börsenausfall (50 % Kapital weg) | BTC −4,9 %, ETH −3,8 % p.a. | G | 2026-10-16 | lebt (Risiko) |
| B1-05 | Funding BTC brutto annualisiert schrumpft | 30,6 % (2021) → 11,9 % (2024) → 5,9 % (2026-07..10) | G | 2026-10-16 | offen (Ursache) |
| B1-06 | Break-even Funding brutto für 4 % auf Kapital | ≈ 8 % p.a. | S aus G | 2026-10-16 | lebt |
| B1-07 | Break-even Börsenausfallrate (50 % Verlust) für K1 BTC | ≈ 9 % p.a. | S aus G | 2026-10-16 | offen (Basisrate fehlt) |
| B1-08 | K1 auf 12 Coins gleichgewichtet | +6,5 % p.a., Sharpe 3,5, DD −6,6 %; SOL −5,6 % p.a. (DD −38 %), BNB −1,6 % | G | 2026-10-16 | lebt (Robustheit, nicht vorab) |
| B1-09 | Crowd-Schock: SOL-Carry in FTX-Woche 2022-11 | −31 % in ~2 Wochen | G | 2026-10-16 | lebt (Risiko) |
| B1-10 | Dreitägiger Börsen-Ausfall hätte ETH-Short bei 2× Hebel im März 2020 liquidiert (Last-Price-Wick +203 %) | – | G (Last-Price), S (Mark-Price kleiner) | 2026-10-16 | offen |
| B1-11 | K2 Kaufen nach Zwangsverkauf (4/8 Wochen): keine von 8 Varianten besteht, ETH schlechter als Zufall | beste p 0,44 | G | 2026-10-16 | tot |
| B1-12 | Zwangsverkaufs-Prämie gepoolt 12 Coins auf Tageskerzen, vor 0,4 % Kosten | 1 T +0,20 %, 7 T +0,35 %, 14 T +0,66 %, 28 T −2,6 % | G (nachträglich) | 2026-10-16 | offen ("lebt intraday" ist ungetestete Vermutung) |
| B1-13 | K3 Exposure halbieren bei heißem Funding | t −0,18 / −0,60 | G | 2026-10-16 | tot |
| B1-14 | K4 Trend + Vol-Steuerung: Sharpe unter Buy & Hold; feste halbe Position gleich gut mit kleinerem DD | BTC Sharpe 1,13 vs 1,15 | G | 2026-10-16 | tot (als Edge) |
| B1-15 | Positionsgröße schlägt Timing (auch 37 KI-Versuche) | – | G | 2026-10-16 | lebt |
| B1-16 | Marktimpact-Faustregel: Impact ≈ σ_Tag × √(Q/Volumen); bei 1 % BTC-Perp-Tagesvolumen ≈ 0,28 % | σ 2,8 %, Vol 16,2 Mrd USD (2024) | G (Inputs), S (Formel), L (Tóth et al. 2011) | 2026-10-16 | lebt |

## 2. Tote Wege (nicht nochmal testen ohne neuen Mechanismus)

| Was | Warum tot | Test |
|---|---|---|
| Spot kaufen nach extrem negativem Funding oder 7-Tage-Absturz, 4/8 Wochen halten | Überrendite ≤ 0 oder p > 0,05, ETH fallendes Messer | K2, Runde 1 |
| Exposure halbieren, wenn 7-Tage-Funding > 90. Perzentil | Timing-Wert t < 0 | K3, Runde 1 |
| Trendfilter (MA 50–200) plus Vol-Ziel als Edge | Sharpe < B&H, feste Position gleich gut | K4, Runde 1 |
| Carry nur an, wenn 7-Tage-Funding > 10 % p.a. | schlechter als immer an (BTC 4,5 %, ETH 6,7 %) | K1-Variante nachträglich, Runde 1 |
| KI-Prompt-Timing auf Wochen (E-002..E-036, Datenzeilen) | nichts schlägt E-003M messbar | Versuchsreihe, research/versuche/ |

## 3. Offene Fragen (priorisiert, siehe Bericht Runde 2 Phase B)

1. Q4 Börsenausfall-Basisrate (wichtigste Einzelzahl für K1)
2. Q1 Ist niedriges Funding Regime oder Zyklus?
3. Q2 Coin-Ausschlussregel gegen Crowd-Schocks, mehrere Börsen
4. Q3 Laufzeit-Futures statt Perp, gegen T-Bill-Hürde
5. Q5 Zwangsfluss intraday

## 4. Test-Zähler

Kumulativ, alle je gerechneten Varianten der Quant-Edge-Reihe (ohne die 37 KI-Prompt-Versuche, eigene Familie).

| Runde | Varianten | Herleitung | kumulativ |
|---|---|---|---|
| 1 | 66 | 14 vorab (K1 2, K2 8, K3 2, K4 2) + 1 K1-Variante nachträglich + 10 K1 weitere Coins + 1 K1-12-Coin-Portfolio + 20 K2 weitere Coins + 10 K3 weitere Coins + 4 K3-Ablation + 6 Diagnose-Horizonte | 66 |

Korrektur: Bonferroni α = 0,05 / N_kumulativ für p-Werte; Deflated Sharpe Ratio (Bailey/López de Prado 2014) für Sharpe-Aussagen, N = N_kumulativ.

## 5. Holdout-Register

| Zeitraum | Status | Wer/was hat ihn berührt |
|---|---|---|
| bis 2024-12-31 | Entwicklung, frei | Runde 1 |
| 2025-01-01 .. 2026-06-30 | **reserviert**, von Quant-Edge nie geladen | Runde 1: 0 Zeilen (geprüft). Projektweit: Binance-Archiv des Hyblock-Threads ab 2025-01 (Befund B-21 Methodik-Wächter), nicht von Quant-Edge benutzt |
| 2026-07-01 .. heute | Dev-Nachschau, kein Beweis (Kurse bekannt, kurz) | Runde 1 |
| ab heute vorwärts | einziger unverbrennbarer Holdout: Paper-Forward-Test | – |
