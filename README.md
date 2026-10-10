# diamondHamster

Research codebase for a self-developed crypto trading method (BTC, ETH; horizon weeks to months).
Research only: no live trading, no exchange keys.

The process rules live in [docs/PROTOKOLL.md](docs/PROTOKOLL.md). Short version:

- Data from 2025-01-01 onward is the holdout. The loader refuses to return it unless explicitly unlocked, and every unlock is recorded.
- Every experiment run is appended to `experiments/log.csv`, including failures.
- Hypotheses are written down in `hypotheses/` before they are tested.
- Every method is compared against buy & hold, DCA and random timing, after costs.
