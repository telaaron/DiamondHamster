# diamondHamster

Research codebase for a self-developed crypto trading method (BTC, ETH; horizon weeks to months).
Research only: no live trading, no exchange keys.

The process rules live in [docs/PROTOKOLL.md](docs/PROTOKOLL.md). Short version:

- Data from 2025-01-01 onward is the holdout. The loader refuses to return it unless explicitly unlocked, and every unlock is recorded.
- Every experiment run is appended to `experiments/log.csv`, including failures.
- Hypotheses are written down in `hypotheses/` before they are tested.
- Every method is compared against buy & hold, DCA and random timing, after costs.

## Usage

```bash
pip install -e ".[dev]"
pytest -q
python -m diamondhamster fetch       # pulls daily BTC/ETH candles into data/raw, records hashes
python -m diamondhamster baselines   # buy & hold, DCA, random timing on the in-sample period
```

## Layout

- `src/diamondhamster/config.py` fixed periods (in-sample to 2022, validation 2023-2024, holdout from 2025) and costs
- `src/diamondhamster/data.py` download, hash-versioned storage, holdout lock
- `src/diamondhamster/backtest.py` long/flat core: signal at close t, trade at open t+1, costs on turnover
- `src/diamondhamster/baselines.py` the bar every method has to clear
- `src/diamondhamster/experiment.py` append-only run log, refuses runs from uncommitted code
- `src/diamondhamster/ai.py` model harness: point-in-time, anonymized windows, versioned prompts, response cache
- `prompts/` one file per prompt; put prompt id, hash and model id into the run's params
- `.claude/agents/decider.md` tool-less subagent for trader decisions
- `hypotheses/` one card per idea, written before testing
