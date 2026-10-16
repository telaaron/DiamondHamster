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
        tr_n = events.trades.notional.to_numpy(float) if "notional" in events.trades.columns else None
        mk_ts = events.mark.ts.to_numpy(np.int64)
        mk_hi, mk_lo, mk_c = (events.mark[c].to_numpy(float) for c in ("high", "low", "close"))
        fu_ts, fu_r = events.funding.ts.to_numpy(np.int64), events.funding.rate.to_numpy(float)
        gaps = [(int(s), int(e)) for s, e in zip(events.gaps.start, events.gaps.end)]

        t0 = int(oi_ts[0])
        k = int(np.searchsorted(mk_ts, t0, side="right"))
        if k:
            p0 = mk_c[k - 1]
        elif len(tr_ts) and tr_ts[0] <= t0:
            p0 = tr_p[int(np.searchsorted(tr_ts, t0, side="right")) - 1]
        else:  # kein Startpreis aus der Zukunft: Gitter und Seed dürfen nur auf Daten <= t0 beruhen
            raise ValueError("no mark or trade at or before the first OI timestamp")
        grid = Grid(p0, p.bucket_bp)
        book = Book(grid, p.max_cohorts, start_day=t0 // DAY_MS)
        for d in deposits([p0], [1.0], oi_v[0], p, force_class="mid"):
            book.add(d, Book.SEED, 0.0)
        quality = {"gaps": [], "max_drift": 0.0, "reseeds": 0, "oi_exceeds_volume": 0}
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
                     "reseeds": quality["reseeds"], "oi_exceeds_volume": quality["oi_exceeds_volume"]}
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
                volume, d_oi = float(tr_q[tw].sum()), oi_v[i] - oi_v[i - 1]
                if volume < abs(d_oi):  # Spec 3.6: OI ändert sich mehr als gehandelt, A = 0
                    quality["oi_exceeds_volume"] += 1
                opens, closes, amb = opens_closes(volume, d_oi, p.alpha)
                if opens > 0:
                    if tw.stop > tw.start:
                        prices, qtys, nots = tr_p[tw], tr_q[tw], (tr_n[tw] if tr_n is not None else None)
                    else:
                        prices, qtys, nots = [last_close], [1.0], None
                    for d in deposits(prices, qtys, opens, p, notionals=nots):
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
