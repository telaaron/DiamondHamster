"""Engine: schreitet von OI-Zeitpunkt zu OI-Zeitpunkt und hält das Buch auf dem echten OI (Spec 3.3)."""
from __future__ import annotations

import numpy as np

from .attribution import deposits, opens_closes
from .book import SIDES, Book
from .events import EventSet
from .grid import Grid
from .params import Params
from .snapshot import Snapshot, _iso, build_snapshot

DAY_MS = 86_400_000


def _window(ts: np.ndarray, lo: int, hi: int) -> slice:
    """Index-Bereich mit lo < ts <= hi in sortiertem ts."""
    return slice(int(np.searchsorted(ts, lo, side="right")), int(np.searchsorted(ts, hi, side="right")))


class Engine:
    def __init__(self, params: Params):
        self.params = params

    def run(self, events: EventSet, at_ms: list[int]) -> list[Snapshot]:
        p = self.params
        ats = sorted(int(a) for a in at_ms)
        oi_ts, oi_v = events.oi.ts.to_numpy(np.int64), events.oi.oi.to_numpy(float)
        if not len(oi_ts) or (ats and ats[0] < oi_ts[0]):
            raise ValueError("no data at or before at")
        tr_ts = events.trades.ts.to_numpy(np.int64)
        tr_p, tr_q = events.trades.price.to_numpy(float), events.trades.qty.to_numpy(float)
        mk_ts = events.mark.ts.to_numpy(np.int64)
        mk_hi, mk_lo, mk_c = (events.mark[c].to_numpy(float) for c in ("high", "low", "close"))
        fu_ts, fu_r = events.funding.ts.to_numpy(np.int64), events.funding.rate.to_numpy(float)
        gaps = [(int(s), int(e)) for s, e in zip(events.gaps.start, events.gaps.end)]

        t0 = int(oi_ts[0])
        k = int(np.searchsorted(mk_ts, t0, side="right"))
        p0 = mk_c[k - 1] if k else (tr_p[0] if len(tr_p) else mk_c[0])
        grid = Grid(p0, p.bucket_bp)
        book = Book(grid, p.max_cohorts, start_day=t0 // DAY_MS)
        for d in deposits([p0], [1.0], oi_v[0], p, force_class="mid"):
            book.add(d, Book.SEED, 0.0)
        quality = {"gaps": [], "max_drift": 0.0, "reseeds": 0}
        last_close = p0
        out: list[Snapshot] = []
        pending = list(ats)

        def emit(i: int) -> None:
            nxt = oi_ts[i + 1] if i + 1 < len(oi_ts) else None
            while pending and (nxt is None or pending[0] < nxt):
                at = pending.pop(0)
                j = int(np.searchsorted(mk_ts, at, side="right"))
                mark = mk_c[j - 1] if j else p0
                q = {"warmup": bool(at < t0 + p.warmup_days * DAY_MS), "max_drift": float(quality["max_drift"]),
                     "drift_warning": bool(quality["max_drift"] > p.drift_warn), "gaps": [list(g) for g in quality["gaps"]],
                     "reseeds": quality["reseeds"]}
                out.append(build_snapshot(book, p, exchange=events.exchange, symbol=events.symbol, at_ms=at,
                                          mark=float(mark), oi=float(oi_v[i]), quality=q,
                                          sources=[f"{events.exchange}:{events.symbol}"],
                                          events_until_ms=int(oi_ts[i])))

        emit(0)
        for i in range(1, len(oi_ts)):
            if not pending:
                break
            t_prev, t = int(oi_ts[i - 1]), int(oi_ts[i])
            today = t // DAY_MS
            mw = _window(mk_ts, t_prev, t)
            gap = mw.start == mw.stop or any(s < t and e > t_prev for s, e in gaps)
            if gap:
                quality["gaps"].append([_iso(t_prev), _iso(t)])
            else:
                last_close = mk_c[mw.stop - 1]
                tw = _window(tr_ts, t_prev, t)
                opens, closes, amb = opens_closes(float(tr_q[tw].sum()), oi_v[i] - oi_v[i - 1], p.alpha)
                if opens > 0:
                    prices, qtys = (tr_p[tw], tr_q[tw]) if tw.stop > tw.start else ([last_close], [1.0])
                    for d in deposits(prices, qtys, opens, p):
                        book.add(d, today, amb / opens)
                swept = book.sweep(float(mk_lo[mw].min()), float(mk_hi[mw].max()))
                for side in SIDES:
                    book.close(side, max(closes - swept[side], 0.0), today, p.beta)
            for r in fu_r[_window(fu_ts, t_prev, t)]:
                book.apply_funding(float(r))
            for side in SIDES:
                total = book.total(side)
                if total <= 0:
                    for d in deposits([last_close], [1.0], oi_v[i], p, force_class="mid"):
                        if d.side == side:
                            book.add(d, today, 0.0)
                    quality["reseeds"] += 1
                else:
                    factor = oi_v[i] / total
                    book.scale(side, factor)
                    if not gap:  # in Lücken ist die Abweichung erwartbar und kein Modellfehler
                        quality["max_drift"] = max(quality["max_drift"], abs(1 - factor))
            book.merge_old(today)
            emit(i)
        return out
