"""Q5 post-hoc counter-test (Nachtrag N3): is the price-only 4h reversal a bid-ask-bounce artefact?
If it were, delaying entry by 1 or 4 bars should erase it. 4 extra tests, never confirmation."""
import json
from q5_intraday import OUT, load, run
res = []
for c in ("BTC", "ETH"):
    k = load(c)
    for L in (1, 4):
        r = run(k, "long", 16, L, False); r["coin"] = c; res.append(r)
        print(c, "L", L, "n", r["n_events"], "exG", round(r["excess_gross"] * 100, 3), "net005", round((r["excess_gross"] - 0.001) * 100, 3), "p", r["p_one_sided"], "h1", round(r["excess_gross_2022_23"] * 100, 3), "h2", round(r["excess_gross_2024"] * 100, 3))
json.dump(res, open(OUT / "r2_q5_posthoc.json", "w"), indent=1, default=float)
