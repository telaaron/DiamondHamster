# CEX failure base rates, 2014-01 to 2026-10

Data file: `events.csv`, 79 rows: 70 core and lender events, plus 9 derivatives or wind-down notes with `category=deriv_note`.

The file adds two columns beyond the requested set:
- `top10_at_time`: 1 if the venue was top-10 by spot or derivatives volume at the time. This is a judgement call (S).
- `category`: core, lender or deriv_note.

Tags used below:
- (L): literature or press figure, with its source.
- (S): my own estimate.

Many `customer_loss_fraction` values for small or old venues are (S) estimates with low confidence. The `loss_basis` column says which ones. Sources for pre-2020 events are mostly standard references such as Wikipedia, cited from memory rather than re-fetched in this session. Sources for 2022-2026 recovery figures were fetched in this session.

## (a) Events per year

This counts core and lender events: failures, frozen withdrawals over 7 days, and hacks including ones the exchange covered. The last column counts only events where customers ended up with a loss greater than 0.

| year | all events | top-10 venue | ultimate customer loss > 0 |
|---|---|---|---|
| 2014 | 3 | 1 | 2 |
| 2015 | 2 | 1 | 1 |
| 2016 | 2 | 1 | 1 |
| 2017 | 2 | 1 | 2 |
| 2018 | 6 | 2 | 4 |
| 2019 | 6 | 3 | 2 |
| 2020 | 3 | 1 | 0 |
| 2021 | 5 | 0 | 2 |
| 2022 | 12 | 2 | 8 |
| 2023 | 6 | 2 | 2 |
| 2024 | 6 | 0 | 2 |
| 2025 | 12 | 3 | 2 |
| 2026 (to Oct) | 5 | 1 | 4 |
| **total** | **70** | **18** | **32** |

Notes on the counts:
- The 2014 row includes Poloniex 2014. Its 12.3% haircut was later repaid, so it is not in the loss column.
- 2026 events: Zondacrypto (BitBay) insolvency, AscendEX shutdown, EXMO's 29.4% sanctions shortfall, Knaken bankruptcy, and the Bitget hack.
- The Bitget hack was $387.5M (L) with customers covered and withdrawals paused for under 7 days.

## (b) Top-10 venues only (18 events)

Events where customers bore a loss or a long freeze:
- **Mt. Gox 2014-02**: insolvency.
- **Bitfinex 2016-08**: 36% haircut, repaid within about 8 months.
- **BTC-e 2017-07**: seizure.
- **FTX 2022-11**: insolvency.
- **Coincheck 2018-01**: freeze of 2-3 weeks, refunded.
- **Bithumb 2018-06**: freeze of about 2 months, covered.
- **OKEx 2020-10**: freeze of about 5.5 weeks, no loss.

Hacks fully covered by the exchange:
- Bitstamp 2015
- Bithumb 2019
- Binance 2019 (SAFU fund)
- Upbit 2019 and 2025
- Crypto.com 2022
- HTX 2023 (two incidents)
- Bybit 2025 ($1.46bn)
- Coinbase 2025 data breach
- Bitget 2026

Only three top-10 events were true failures, meaning insolvency or seizure with balances locked for years: **Mt. Gox, BTC-e and FTX**.

## (c) Academic and industry base rates (L)

**Moore & Christin (2013)**, "Beware the Middleman: Empirical Analysis of Bitcoin-Exchange Risk", Financial Cryptography 2013 (slides at https://tylermoore.ens.utulsa.edu/fc13pres.pdf; press summary at https://www.sciencedaily.com/releases/2013/04/130424161112.htm).
- 40 exchanges were studied; "18 have since closed" (45%).
- Median lifetime was 381 days.
- 9 of the 40 were breached, and 5 of those 9 closed.
- 45% of closed exchanges did not reimburse customers.
- Cox model, log daily volume: hazard ratio 0.840 (p=0.016). Higher volume means a lower closure hazard.
- Cox model, breach: hazard ratio 2.36 (p=0.13, not significant).
- Logistic model: volume raises the odds of a breach, OR 1.672 (p=0.018).
- Quote: "The risk of losing funds stored at exchanges is real but uncertain."

**Moore, Christin & Szurdi (2018)**, "Revisiting the risks of bitcoin currency exchange closure", ACM TOIT 18(4) (doi 10.1145/3155808). These figures are second-hand, via Fantazzini & Calabrese, https://mpra.ub.uni-muenchen.de/110391/1/MPRA_paper_110391.pdf.
- 80 exchanges established 2010-2015; 38 closed (47.5%).
- Of the closed exchanges: 5 refunded customers fully, 5 partially, 6 not at all, and 22 are unknown.
- Panel logit: a breach raises the odds of closure in the same quarter; higher volume lowers it.
- Exchanges with concentrated fiat volume were "91% less likely to close".
- There is a significant negative time trend in closure probability.
- 2FA and AML had no effect.

**Mukherjee & Moore (2022)**, "Cryptocurrency Exchange Closure Revisited (Again)", APWG eCrime 2022 (https://tylermoore.utulsa.edu/ecrime22exchange.pdf).
- 822 exchanges from 2010-2022: "40% of these exchanges subsequently shut down."
- Kaplan-Meier survival: about 75% survive at least 3 years; median survival is about 7 years.
- Crypto-only exchanges (no fiat) have "approximately 60% greater odds of shutting down."
- Exchanges allowing US customers close faster: hazard ratio about 1.5.
- Breach effect on lifetime: hazard ratio about 1.06, not significant. 32 of 822 exchanges were flagged as breached.

**Milunovich & Lee (2021)**, "Cryptocurrency Exchanges: Predicting which Markets will Remain Active" (https://www.mq.edu.au/__data/assets/pdf_file/0005/1170563/cryptoexchange_risks.pdf).
- 238 exchanges: 107 closed (about 45%).
- About 26% had suffered a security breach.
- Median lifetime was 1,035 days.

**Chainalysis, via ForkLog 2025-12-19** (https://forklog.com/en/losses-from-crypto-hacks-reached-3-4bn-in-2025/).
- More than $3.4bn was stolen in 2025.
- Bybit alone was $1.5bn, 44% of the total.
- DPRK-attributed theft was at least $2.02bn.

**Market-implied (L, sentiment only)**: Polymarket put the chance of a "Major CEX insolvent in 2026" (Binance, Coinbase, Bybit, OKX, Kraken) at about 5%. Source: https://financefeeds.com/could-a-top-crypto-exchange-collapse/

All three academic panels agree: about 40-48% of exchanges eventually close. These samples are dominated by small venues, and every study finds volume or size is protective.

## (d) Derived hazard for a top-10 exchange (S)

**Method.** Count failures at venues that were top-10 at the time, divided by exposure.
- Exposure is 10 slots × 12.8 years (2014-01 to 2026-10) = **128 exchange-years** (S).
- Events: k=3 strict failures (Mt. Gox, BTC-e, FTX).
- Point estimate: 3/128 = **2.3% per exchange-year** (S).
- Exact Poisson 95% CI: **0.5%-6.9%** (S).
- Adding the Bitfinex haircut (k=4) gives 3.1% (CI 0.9%-8.0%).
- Counting any event at a top-10 venue with customer loss or a freeze over 7 days (k=7) gives 5.5%.
- Using 2019-2026 only (1 event, FTX, over about 78 exchange-years) gives 1.3%.

**Market-level rate.** 3/12.8 = 0.23 events per year, so P(at least one top-10 failure in a given year) ≈ **21%** (S).

**Range (S):**

| | per exchange-year |
|---|---|
| Low | 1.0% |
| Central | 2.3% |
| High | 5% |

- The low end reflects the post-FTX era of proof of reserves and MiCA licensing, plus the 2019-2026 rate.
- The high end includes haircut and freeze events and the upper confidence band.

**Covered hacks are a separate hazard.** There were 14 hacks at top-10 venues over the period, about **11% per exchange-year** (S). Customer loss was about 0 in 13 of the 14; Bitfinex was the exception, with a temporary haircut.

**LGD given failure (S):**
- **USD-at-petition (fiat claim) basis**: low 0.0, central 0.3, high 0.7.
  - FTX paid about 103-143% of petition-date USD claims (L, Cointelegraph 2026-07: about $10bn distributed; 120% for the convenience class).
  - Mt. Gox's JPY claims were recovered at more than 100%.
  - BTC-e recovered roughly 0.4 (S, low confidence).
  - The central 0.3 adds the time value of 2.3-10 years locked at about 5% per year.
- **In-kind (crypto-denominated) basis**, which is the relevant one for a crypto-collateralised book: low 0.5, central 0.75, high 0.95.
  - Mt. Gox: about 0.79 (L/S); roughly 21% of BTC claims were repaid in kind. 34,689 BTC were still unpaid in Oct 2025 and the deadline was moved to 2026-10-31 (L, Decrypt).
  - FTX: about 0.8, because claims were fixed at BTC ≈ $16.9k in Nov 2022.
- **All-venue failures** (28 insolvency, fraud, seizure, lender or freeze rows): mean LGF 0.57, median 0.60 (S, USD basis).
- **Lenders**:
  - Celsius: 64.9% recovered by 2025-08 (L).
  - Voyager: about 66% (S, built from 35.7% plus about 30%).
  - Vauld: about 60% (L, Kroll).
  - Hodlnaut: 26.92% interim dividend (L, EY 2026-08).
  - BlockFi and Gemini Earn: about 100%.
- **Time to recovery**:
  - Exchange insolvencies took a median of about 2-4 years to a first meaningful distribution; Mt. Gox took 10.4 years.
  - Covered hacks took days to weeks.
  - WazirX took about 15 months.

**Implied expected loss on balances at a top-10 venue (S):** 2.3% × 0.3-0.75 ≈ **0.7-1.7% per year**. The range for low to high hazard is about 0.3-4%.

## Uncertainty and biases

1. **Survivorship and coverage bias.** Pre-2017 exchanges and small or regional exchanges that died quietly are under-represented. Mukherjee & Moore (2022) cite a journalist who tallied 75 closures in 2020 alone; this file has about 3 events for that year. The all-venue counts in (a) are therefore a large undercount. The top-10 counts are much less affected, because top-10 failures are always newsworthy.
2. **Ranks are noisy.** Wash trading in 2018-2020 inflated reported volumes, so "top-10" is a judgement call. Mt. Gox's widely cited "~70%" share is a 2013 peak; it was lower by Feb 2014. Coincheck and BTC-e are borderline top-10.
3. **The loss basis matters more than the hazard.** FTX is either 0% loss (USD basis) or about 80% loss (BTC basis). Pick the basis that matches the strategy's numeraire.
4. **Small-k statistics.** With 3 events, the 95% CI spans more than 10x. The process is non-stationary: regulation, proof of reserves, and concentration in Binance, OKX, Bybit and Coinbase.
5. **Recent events are still open.** Recovery for the 2026 events (Zondacrypto, AscendEX, EXMO, Knaken) is unresolved, and their LGF values are provisional (S).
6. **Not modelled.** Orderly wind-downs (BitMEX 2026-09, BitMart, Gemini's regional exit) and ADL or insurance-fund events (10 Oct 2025: about $19.3bn of liquidations, Hyperliquid's first ADL in more than 2 years) are recorded as deriv_note rows. They are not counted as failures, but they matter for derivatives-venue counterparty and execution risk.
