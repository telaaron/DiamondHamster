# Runde 3, Phase 1: Literatur-Basisrate (2026-10-16)

Vor eigenen Daten: Wie groß war die Prämie für "öffentlich, aber langsam verarbeitet", wo lebte sie, wie schnell verschwand sie? Alle Zahlen hier sind (L). Herkunft je Zahl in der Detailtabelle unten: Q = im Volltext gesehen, A = Abstract, S = Sekundärquelle, G = Gedächtnis, n.v. = nicht verifiziert. Recherche durch einen Subagent mit Websuche, Zahlen mit Q/A von mir nicht nachgeprüft.

## Ergebnis vorweg

1. Ursprünglich 1 bis 2 % pro Monat vor Kosten (Cohen-Frazzini > 150 bp, Cohen-Lou 95 bis 118 bp, Lazy Prices bis 188 bp; PEAD 8 bis 9 % pro Quartal 1974 bis 1986). Breit und wertgewichtet gemessen eher 30 bis 100 bp pro Monat.
2. Sie lebte fast nur in kleinen, illiquiden Titeln: PEAD 2,43 % pro Monat im illiquidesten Dezil gegen 0,04 % im liquidesten, und Kosten fraßen 70 bis 100 % davon (Chordia u. a. 2009). Das passt zur Schwelle aus Phase 0.
3. Halbwertszeit nach Veröffentlichung kurz: Anomalien verlieren 58 % nach Publikation (McLean-Pontiff 2016); PEAD ist bei Nicht-Microcaps seit ca. 2006 weg, bei Microcaps 2016 bis 2019 (Martineau 2022). Das LLM-Schlagzeilen-Signal fiel von Sharpe 6,5 (Ende 2021) auf 1,2 (Anfang 2024) und ist bei 20 bp Kosten pro Runde unprofitabel (Lopez-Lira/Tang, nach GPT-4-Cutoff gemessen).
4. Pseudonymisierung schützt nicht zuverlässig vor Trainingswissen: GPT-4 erkennt 70 % maskierter Firmen (Sarkar/Vafa). Das bestätigt die Regel aus Phase 0: KI-Leser zählen nur nach dem Cutoff.
5. Krypto: Listing-Effekte (+5,7 % am Tag, Ante 2019) schwächer seit 2023 und drehen nach Tagen; Unlock-Abverkauf ab ~30 Tage vorher, aber nur aus Industrie-Studie eines Market Makers ohne offengelegte Methode (Keyrock 2024). Akademisch fester: knapp angenommene DAO-Abstimmungen +4,7 % Token-Rendite (Lo Monaco u. a. 2025).

**Begründete Erwartung (S):** Etwas ist wahrscheinlich übrig, aber in der Größenordnung unserer Kosten. Für die Kandidaten:

| Kandidat | Literatur-Anker | erwartete Prämie vor Kosten pro Ereignis (S) | unsere Kosten pro Runde (S) | Erwartung netto |
|---|---|---|---|---|
| A1 Unlocks | Keyrock: Team-Unlocks stark negativ, Abfall ab 30 Tage vorher | unbekannt; Industrie-Zahl nicht belastbar. Basisproblem: Token mit Unlocks verlieren auch ohne Unlock (hohe Inflation), Kontrolle = gleicher Token ohne Unlock-Fenster | 0,4 % + 2 × Spread (≈ 0,6 bis 1 %) | offen, einziger historisch testbarer Kandidat |
| A2 Schwer lesbare Dokumente | Lazy Prices 30 bis 188 bp/Monat, DAO-RDD +4,7 %, LLM-News 34 bp/Tag mit schnellem Verfall | 0,5 bis 2 % über 5 bis 20 Tage, nach ≥ 50 % Verfallsabschlag | wie oben | ≈ 0, Spanne −0,5 bis +1 % |
| A3 Querverbindungen | Cohen-Frazzini > 150 bp/Monat (1980 bis 2004), Krypto-Korrelationen sehr schnell | ≤ 0,5 % | wie oben | eher negativ |

Herleitung der Prämienspanne A2: Monatsprämie 30 bis 188 bp auf 5 bis 20 Tage skaliert ≈ 0,1 bis 1,8 %; Small-Cap-Faktor ×2 bis ×4 (Chordia, Lopez-Lira); Verfall nach Publikation −50 % (McLean-Pontiff). Grobe Mitte ≈ 1 %.

## Was die Basisrate für die Testbarkeit heißt (G)

Wie viele Ereignisse braucht ein Test, um eine Prämie μ mit t = 2 zu sehen? Rendite-Streuung je Ereignis über 10 Tage bei 5 % Tagesvol: σ ≈ 5 % · √10 ≈ 16 %. Nötige Ereignisse n ≈ (2σ/μ)²:

| μ pro Ereignis | nötige Ereignisse |
|---|---|
| 0,5 % | ~4 000 |
| 1 % | ~1 000 |
| 2 % | ~250 |

Dazu kommt die Korrektur für den kumulativen Test-Zähler (Phase 3, sobald WISSENSBASIS da ist). Für KI-Kandidaten (A2, A3) gibt es nur Dokumente ab 2026-07 (~15 Wochen). Eine 1-%-Prämie ist dort nur messbar, wenn in 15 Wochen ~1 000 unabhängige, verwertbare Ereignisse in kleinen Assets anfallen. Das ist die eigentliche Engstelle der Runde, nicht der Datenzugang.

## Detailtabellen

### 1. PEAD und Anomalie-Verfall

| Quelle | Rendite | Horizont | Cap-Bereich | Zeitraum | Verschwinden/Schrumpfen | verifiziert? |
|---|---|---|---|---|---|---|
| Bernard & Thomas (1989), "Post-earnings-announcement drift: Delayed price response or risk premium?", *J. Accounting Research* 27 (Suppl.), 1–36 | SUE-Dezil 10-1: Spread positiv in 41 von 48 Quartalen. Höhe ca. 4 % über 60 Tage (ca. 18 % p.a.) | 60 Handelstage | stärker bei kleinen Firmen | 1974–1985 | siehe Martineau 2022 | 41/48: **S** (Wikipedia). 4 %/18 %: **G**, n.v. |
| Bernard & Thomas (1990), "Evidence that stock prices do not fully reflect the implications of current earnings for future earnings", *J. Accounting & Economics* 13, 305–340 | Zero-Investment ca. **8–9 % pro Quartal** (ca. 35 % p.a. vor Kosten). 25–30 % des Drifts fallen in die 3-Tage-Fenster der nächsten 3 Announcements | 1–4 Quartale | in allen Größen, stärker bei Small | 1974–1986 | – | **S** (Wikipedia) |
| Chordia, Goyal, G. Sadka, R. Sadka & Shivakumar (2009), "Liquidity and the post-earnings-announcement drift", *Financial Analysts Journal* 65(4), 18–32 | Long-short, VW: **0,04 %/Monat** im liquidesten vs. **2,43 %/Monat** im illiquidesten Dezil. Gesamt ca. 0,9 %/Monat | monatlich | lebt in illiquiden Aktien (Amihud) | 1972–2005 | **Kosten fressen 70–100 % der Papierrendite** | **A**/**S** (IDEAS-Abstract) |
| Martineau (2022), "Rest in Peace Post-Earnings Announcement Drift", *Critical Finance Review* 11(3–4), 613–646 | BHAR[2,60] pro Dezilrang: 0,003*** (1984–90), danach Nicht-Microcaps nicht mehr signifikant (−0,002** in 2016–19). Announcement-Tag-Reaktion steigt von 0,002 auf 0,012 | 60 Tage | **Nicht-Microcaps: weg ab ca. 2006. Microcaps: weg 2016–19** (analystenbasiert). Mit Random-Walk-SUE ist der Effekt bei Microcaps noch 0,003*** in 2016–19, konzentriert auf Tag 2–5 | 1973/1984–2019 | Kernquelle für das Verschwinden | **Q** (PDF, Tab. 3/4) |
| Subrahmanyam (2025, WP, SSRN 5930255), "Keeping it Simple" | t = 2,18 alle Aktien; **t = 1,43 ohne Microcaps** | – | Microcaps machen ca. 3 % des Marktwerts aus | 02/2001–12/2024 | stützt Martineau. Gegenposition: Dickerson/Julliard/Mueller (JFE 2025), Hirshleifer/Peng/Wang (RFS 2025) finden Drift, aber ohne Microcap-Filter | **S** (UCLA Anderson Review) |
| Fink (2021), "A review of the Post-Earnings-Announcement Drift", *J. Behavioral & Experimental Finance* 29, 100446 | Review, keine eigenen Zahlen | – | – | – | keine einzelne Erklärung. Frage nach dem Verfall im Abstract nicht beantwortet | **A** |
| Kettell, McInnis & Zhao (2022) | SUE-Spread ca. 5 % (1980er/90er) auf ≤ 3 % (Ende 2010er) | – | – | – | Schrumpfen | **S** (Wikipedia), n.v. |
| McLean & Pontiff (2016), "Does academic research destroy stock return predictability?", *J. Finance* 71(1), 5–32 | 97 Prädiktoren. In-sample **0,582 %/Monat**, out-of-sample vor Publikation 0,402 %, nach Publikation 0,264 %. **−26 % out-of-sample, −58 % nach Publikation** (also ca. 32 Pp durch Publikation) | monatlich | **Verfall kleiner bei Kosten-/Arbitrage-teuren Portfolios** (hohe idiosynkratische Vola, illiquide, kleine Aktien, breite Spreads) | bis 2013. Ø Post-Publikation 156 Monate | Halbwertszeit ca. Publikationsdatum | **Q**/**A** (PDF + CFA-Digest) |

Links: [Martineau PDF](https://cfr.ivo-welch.org/forthcoming/papers/martineau2021rest.pdf) · [Martineau IDEAS](https://ideas.repec.org/a/now/jnlcfr/104.00000122.html) · [Chordia et al. IDEAS](https://ideas.repec.org/a/taf/ufajxx/v65y2009i4p18-32.html) · [Fink IDEAS](https://ideas.repec.org/a/eee/beexfi/v29y2021ics2214635020303750.html) · [McLean-Pontiff PDF](https://Www.Gwern.net/doc/economics/2016-mclean.pdf) · [CFA-Digest](https://rpc.cfainstitute.org/research/cfa-digest/2016/06/does-academic-research-destroy-stock-return-predictability-digest-summary) · [Wikipedia PEAD](https://en.wikipedia.org/wiki/Post%E2%80%93earnings-announcement_drift) · [UCLA Anderson Review](https://anderson-review.ucla.edu/is-post-earnings-announcement-drift-a-thing-again/)

### 2. Komplexität und Verknüpfungen

| Quelle | Rendite | Horizont | Cap-Bereich | Zeitraum | Verschwinden/Schrumpfen | verifiziert? |
|---|---|---|---|---|---|---|
| Cohen & Lou (2012), "Complicated firms", *J. Financial Economics* 104(2), 383–400 | Long-short Konglomerate: **EW 118 bp/Monat** (t = 5,5), **VW 95 bp** (t = 3,2). 5-Faktor-Alpha 112 bzw. 104 bp. **Netto bei 50 Mio. $/Seite: VW 49 bp (t = 1,6)**, EW 72 bp | Effekt v. a. Monat 1, leichte Drift bis Monat 6, keine Umkehr | gilt in allen Größen, **stärker bei kleinen** | 1977–2009 | kein Post-Publikations-Test gefunden | **Q** (Working-Paper-PDF, DP683). Heft/Seiten **G** |
| Cohen & Frazzini (2008), "Economic links and predictable returns", *J. Finance* 63(4), 1977–2011 | Kunden-Momentum Long-short: **> 150 bp/Monat Alpha** | 1 Monat | stärker bei geringer Aufmerksamkeit (Details n.v.) | 1980–2004 (**G**) | n.v. Bei HXZ (VW, NYSE-Breakpoints) nach Gedächtnis schwach bis insignifikant, n.v. | **A** (Rendite). Zeitraum **G** |
| Menzly & Ozbas (2010), "Market segmentation and cross-predictability of returns", *J. Finance* 65(4), 1555–1580 | Zulieferer-/Kunden-Industrien prognostizieren sich gegenseitig (Höhe n.v.) | monatlich | **schwächer bei hoher Analysten-Coverage und institutionellem Besitz** | n.v. | Effekt sinkt mit der Zahl informierter Investoren | **A** |
| Hou, Xue & Zhang (2020), "Replicating anomalies", *Review of Financial Studies* 33(5), 2019–2133 | 452 Anomalien, **65 % mit t < 1,96**, 82 % mit t < 2,78. 96 % der Trading-Friction-Anomalien fallen durch | – | Microcaps neutralisiert (NYSE-Breakpoints, VW) | 1967–2016 (**G**) | **Zentrale Aussage: vieles lebt nur in Microcaps/EW.** Ergebnisse für Cohen-Frazzini/Cohen-Lou im Einzelnen n.v. | **A** |

Links: [Cohen-Lou DP683 PDF](https://www.fmg.ac.uk/sites/default/files/publications/DP683.pdf) · [Cohen-Frazzini IDEAS](https://ideas.repec.org/a/bla/jfinan/v63y2008i4p1977-2011.html) · [Menzly-Ozbas IDEAS](https://ideas.repec.org/a/bla/jfinan/v65y2010i4p1555-1580.html) · [HXZ IDEAS](https://ideas.repec.org/a/oup/rfinst/v33y2020i5p2019-2133..html)

### 3. Aufmerksamkeit

| Quelle | Rendite | Horizont | Cap-Bereich | Zeitraum | Verschwinden/Schrumpfen | verifiziert? |
|---|---|---|---|---|---|---|
| Da, Engelberg & Gao (2011), "In search of attention", *J. Finance* 66(5), 1461–1499 | SVI-Anstieg → höhere Kurse in den nächsten **2 Wochen**, **Umkehr innerhalb eines Jahres** (Höhe in bp n.v.) | 2 Wochen / 1 Jahr | Russell 3000. Retail-Aufmerksamkeit, eher kleinere Titel (**G**) | 2004–2008 | Umkehr = Preisdruck, kein Info-Signal | **A** |
| DellaVigna & Pollet (2009), "Investor inattention and Friday earnings announcements", *J. Finance* 64(2), 709–749 | Freitags-Announcements: **15 % schwächere Sofortreaktion, 70 % stärkere verzögerte Reaktion** | ca. 60–75 Tage | n.v. | 1984–2006 | n.v. | Zahlen **S** (Alpha Architect zitiert den Abstract). Heft/Seiten **G** |
| Hirshleifer, Lim & Teoh (2009), "Driven to distraction: Extraneous events and underreaction to earnings news", *J. Finance* 64(5), 2289–2325 | Viele gleichzeitige Announcements → schwächere Sofortreaktion, **stärkerer Drift**. Strategie mit "substantial alphas" (Höhe n.v.) | ca. 60 Tage | n.v. | 1995–2004 (**G**) | n.v. | **A** |
| Cohen, Malloy & Nguyen (2020), "Lazy Prices", *J. Finance* 75(3), 1371–1415 | Long Non-Changers / Short Changers (10-K/10-Q-Ähnlichkeit): **bis 188 bp/Monat Alpha (> 22 % p.a.)**, gemessen an Änderungen in der Sektion "Risk Factors". Breite VW-Variante ca. **30–58 bp/Monat** | **kein Announcement-Effekt**, Drift über 6–18 Monate, keine Umkehr | n.v. | 1995–2014 (**G**) | Post-Publikations-Test nicht gefunden | 188 bp: **A**. 30–58 bp und Horizont: **S** (quantt.co.uk) |

Links: [Da et al.](https://academicnewsletter.sufe.edu.cn/info/360414) · [DellaVigna-Pollet NBER](https://www.nber.org/papers/w11683) · [Alpha Architect](https://alphaarchitect.com/pay-attention-to-friday-earnings-announcements/) · [HLT IDEAS](https://ideas.repec.org/a/bla/jfinan/v64y2009i5p2289-2325.html) · [Lazy Prices IDEAS](https://ideas.repec.org/a/bla/jfinan/v75y2020i3p1371-1415.html) · [quantt Lazy Prices](https://www.quantt.co.uk/resources/lazy-prices-snowflake-cortex-ai)

### 4. Krypto-Listing-Effekte

| Quelle | Rendite | Horizont | Cap-Bereich | Zeitraum | Verschwinden/Schrumpfen | verifiziert? |
|---|---|---|---|---|---|---|
| Ante (2019), "Market reaction to exchange listings of cryptocurrencies", BRL Working Paper No. 3 (keine Journal-Version verifiziert) | AR **+5,7 % am Listing-Tag**, **+9,2 % in [−3,+3]**. Bis +25,5 % bei Coins mit wenigen Börsen. Manche Börsen ohne Effekt oder mit negativem Effekt | Tage | 327 Listings, 180 Coins, 22 Börsen | ca. 2018–2019 | – | **A** (BRL-Seite). Eine andere Sekundärquelle nennt 7,4 % für den Listing-Tag (Widerspruch) |
| Coin Metrics (2020), Industrie-Studie "Coinbase-Effekt" | Median **+4 %** 10 Tage nach Listing. Spanne −1 % bis +14 %. 6 von 16 fallen | [−10,+10] Tage | 16 Coinbase-Pro-Listings | bis 06/2020 | "fairly muted" | **S** (Cointelegraph) |
| Li, Luo, Wang & Wei (2025), "Cryptocurrency Exchange Listings", AFT 2025 (LIPIcs), SSRN 4715718 | positive kurzfristige AR, **Coinbase > Binance**. Stärker regulierte Börse → höhere Listing-Rendite. Interessenkonflikt bei VC-Beteiligungen | "short-term" | 80 Börsen | n.v. | n.v. | **A**. Höhe n.v. |
| RockawayX (2025/2024-Daten), Industrie | DiD 7 Tage: Binance/Bybit signifikant bullisch, aber sehr breite Konfidenzintervalle. 30/60 Tage nicht signifikant oder bearish. **Alle Effekte kurzfristig, Umkehr nach wenigen Tagen** | 7/30/60 Tage | Binance-Listings < 100 Mio. $ als einziges Segment mit klarem Trend | 2024 | – | **S** |
| The TIE (2026), Industrie | Run-up vor Tag 0, danach flach oder negativ. Mean-Reversion innerhalb von 2 Wochen. **Kleine Caps: größte Erstreaktion, stärkster späterer Abfall** | D−14 bis D+42 | 1.844 Listings, 7 Börsen | 01/2023–06/2026 | **2023 = Höchststand, 2024–26 schwächer und schneller verblassend**. 2021–22 größer | **S** (keine Zahlen im Text) |

Links: [Ante BRL](https://www.blockchainresearchlab.org/portfolio/market-reaction-to-exchange-listings-of-cryptocurrencies/) · [Coin Metrics via Cointelegraph](https://cointelegraph.com/news/coinmetrics-finds-the-coinbase-effect-is-actually-pretty-lame) · [Li et al. AFT 2025](https://drops.dagstuhl.de/storage/00lipics/lipics-vol354-aft2025/html/LIPIcs.AFT.2025.11/LIPIcs.AFT.2025.11.html) · [RockawayX](https://rockawayx.com/insights/bullish-or-bearish-what-really-happens-when-tokens-list-on-a-cex) · [The TIE](https://www.thetie.io/insights/what-does-an-exchange-listing-actually-deliver-in-2026)

### 5. Token-Unlocks

| Quelle | Rendite | Horizont | Cap-Bereich | Zeitraum | Verschwinden/Schrumpfen | verifiziert? |
|---|---|---|---|---|---|---|
| Keyrock (2024), "From Locked to Liquidity: What 16,000+ Token Unlocks Teach Us" (Industrie; Keyrock ist selbst Market Maker und OTC-Anbieter → Interessenkonflikt) | **90 % der Unlocks mit negativem Preisdruck** (gegenüber ETH). **Team-Unlocks ca. −25 %**, Investoren moderat und langsam, **Ecosystem +1,18 %** nach dem Unlock. Größere Unlocks: 2,4-fach stärkere Drops (Basis unklar). >10 % der Supply nicht schlechter als 5–10 % | **Abfall beginnt ca. 30 Tage vorher**, steilste Phase in der letzten Woche, Stabilisierung ca. 14 Tage danach | 40 Token, ca. 16.000 Events | n.v. | n.v. Antizipation bzw. Hedging vorher heißt: der Effekt ist schon teilweise eingepreist | **S**/Primär-Blog (Methodik und Statistik nicht offengelegt) |
| Messari / The Block Unlock-Studien | nicht verifiziert | – | – | – | – | n.v. |

Links: [Keyrock](https://keyrock.com/from-locked-to-liquidity-what-16000-token-unlocks-teach-us/) · [CryptoSlate-Zusammenfassung](https://cryptoslate.com/90-of-token-unlocks-drive-prices-down-declines-begin-a-month-ahead/)

### 6. LLM-Literatur (Look-ahead)

| Quelle | Rendite | Horizont | Cap-Bereich | Zeitraum | Verschwinden/Schrumpfen | verifiziert? |
|---|---|---|---|---|---|---|
| Lopez-Lira & Tang (2023, arXiv 2304.07619 v6 2025; Journal n.v.), "Can ChatGPT forecast stock price movements? Return predictability and large language models" | GPT-4-Headline-Scores. Overnight-Long-short **34 bp/Tag** vor Kosten (Sharpe 2,97), Intraday 50 bp/Tag. Short-Leg (negative News) 26 bp/Tag vs. Long-Leg 8 bp/Tag. **Kosten: 10 bp Round-Trip → Sharpe ca. 1,3; 20 bp → unprofitabel** | 1 Tag | **Interaktion mit kleinen Firmen ca. 4- bis 5-fach** (0,404 vs. 0,087). Ohne Titel < 5 $ und < NYSE-P20 bleiben > 300 % kumuliert | 10/2021–05/2024, nach dem Knowledge-Cutoff von GPT-4 (09/2021), also echtes Out-of-sample | **Sharpe fällt: 6,54 (Q4/2021) → 3,68 (2022) → 2,33 (2023) → 1,22 (Jan.–Mai 2024)** | **Q** (arXiv-HTML v6) |
| Glasserman & Lin (2023), "Assessing look-ahead bias in stock return predictions generated by GPT sentiment analysis", arXiv 2309.17322 | **anonymisierte Headlines schneiden in-sample besser ab** → der "Distraction Effect" (Vorwissen über die Firma) wiegt schwerer als Look-ahead | Tag | **Distraction stärker bei großen Firmen** | n.v. | Out-of-sample kein Look-ahead, aber Distraction möglich | **A** |
| Kim, Muhn & Nikolaev (2024), "Financial statement analysis with large language models", arXiv 2407.17866 / Chicago BFI WP 2024-65 | Abstract: GPT-4 schlägt Analysten bei der Richtung von Gewinnänderungen. Strategie mit höherem Sharpe und Alpha (Zahlen n.v.) | 1 Jahr | n.v. | n.v. | **Am 20.02.2025 auf arXiv zurückgezogen: "A co-author identified inconsistencies in the data and analyses …"** → Ergebnisse nicht belastbar | **A** (arXiv-Withdrawal-Notiz) |
| Sarkar & Vafa (2024), "Lookahead bias in pretrained language models", WP (NBER-Konferenz; ICML-2025-Bezug **G**) | keine Renditen. Llama-2 nennt "COVID-19" in 6,8 % der Risiko-Prognosen aus Calls von 2019. **Masking scheitert: GPT-4 erkennt maskierte Firmen in 70 % der Fälle** (61 % auch ohne Produktnamen) | – | – | Earnings Calls 09–11/2019. Wahlen 2014–2022 | **Prompting und Anonymisierung beseitigen den Bias nicht** → Modelle mit Training-Cutoff vor der Testperiode nötig | **Q** (NBER-PDF) |

Links: [Lopez-Lira-Tang v6](https://arxiv.org/html/2304.07619v6) · [Glasserman-Lin](https://arxiv.org/abs/2309.17322) · [Kim-Muhn-Nikolaev (withdrawn)](https://arxiv.org/abs/2407.17866v3) · [Sarkar-Vafa PDF](https://conference.nber.org/conf_papers/f205530/f205530.pdf)

### 7. Krypto: Momentum/Aufmerksamkeit, GitHub, Governance

| Quelle | Rendite | Horizont | Cap-Bereich | Zeitraum | Verschwinden/Schrumpfen | verifiziert? |
|---|---|---|---|---|---|---|
| Liu & Tsyvinski (2021), "Risks and returns of cryptocurrency", *Review of Financial Studies* 34(6), 2689–2727 | **starkes Time-Series-Momentum**. **Attention-Proxies (u. a. Google-Suche, G) prognostizieren Renditen stark** (Höhe n.v.) | Tage bis Wochen | BTC, ETH, XRP (**G**) | ca. 2011–2018 (**G**) | n.v. | **A** |
| Liu, Tsyvinski & Wu (2022), "Common risk factors in cryptocurrency", *J. Finance* 77(2), 1133–1177 | 3 Faktoren (Markt, **Size**, Momentum) erklären 10 Long-short-Strategien | Woche | Size-Effekt: kleine Coins rentieren mehr | n.v. | n.v. | **A**. Heft **G** |
| Petryk, Qiu & Pathak (2023), "Impact of open-source community on cryptocurrency market price", *J. Management Information Systems* 40(4), 1237–1270 | Forks +4,3 %, Watches +2,4 %, Issues +4,4 % **jährliche** Preissteigerung. Pull Requests −5 % | 1 Jahr | n.v. | n.v. | Selektionsmechanismus, keine Handelsstrategie | **A** |
| The TIE (ca. 2021), "Does Github activity affect crypto prices?", Industrie | 6 Coins. Commit-Strategie schlägt Zufall nur teilweise | 14 Tage | – | 2020 | Fazit des Autors: "unclear whether Github activity has an effect on price" | **S** |
| CryptoScores (2026), Industrie | GitHub-Follower ρ = +0,28 mit 30-Tage-Rendite. Kombination mit Fees/MCap: Quartil-Spread 23,4 Pp | 30 Tage | Top 300 | ein Fenster Feb./März 2026 | Anekdote, nicht belastbar | **S** |
| Appel & Grennan (2023), "Decentralized governance and asset prices", WP (SIOE 2023) | 10.764 Proposals. Partizipation/Sicherheit → positive AR, Hürden → negative AR | n.v. | – | n.v. | – | **A** |
| Lo Monaco, Momtaz & Vismara (2025), "Distributed governance and value creation in DAOs: Evidence from a regression discontinuity design", *Economics Letters* 248, 112233 | knappe Annahme eines Proposals → **+4,7 % Token-Rendite**. +1 SD Partizipation → +2,2 % | Event | DAO-Token | 2020–2024 | – | **A** |

Links: [Liu-Tsyvinski IDEAS](https://ideas.repec.org/a/oup/rfinst/v34y2021i6p2689-2727..html) · [LTW](https://academicnewsletter.sufe.edu.cn/info/359095) · [Petryk et al. JMIS](https://jmis-web.org/articles/1645) · [The TIE GitHub](https://thetie.io/insights/does-github-activity-affect-crypto-prices) · [CryptoScores](https://www.cryptoscores.com/blog/fundamental-signals-cryptocurrency-performance) · [Appel-Grennan](https://www.sioe.org/conference/2023/program/paper/464-decentralized-governance-and-asset-prices) · [Lo Monaco et al.](https://aisberg.unibg.it/handle/10446/314966)


Hinweis: Kim/Muhn/Nikolaev (2024) wurde 2025 zurückgezogen und zählt nicht. Bei Ante (2019) nennt eine Sekundärquelle 7,4 % statt 5,7 % für den Listing-Tag.
