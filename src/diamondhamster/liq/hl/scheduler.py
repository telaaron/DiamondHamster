"""Planer: welche Adresse wird als Nächstes nach ihren Positionen gefragt (Spec 3.3)."""
from __future__ import annotations

import heapq
from dataclasses import asdict, dataclass

MIN = 60_000
DROP_AFTER_MS = 3 * 86_400_000
RETRY_MS = MIN
AGAIN = -1  # due-Markierung: während einer Abfrage gehandelt


def interval_ms(notional: float, has_pos: bool) -> int:
    if not has_pos:
        return 360 * MIN
    if notional >= 1_000_000:
        return 2 * MIN
    if notional >= 100_000:
        return 10 * MIN
    return 30 * MIN


@dataclass
class _User:
    due: int | None = None      # None = gerade in Abfrage
    notional: float = 0.0
    has_pos: bool = False
    last_active: int = 0        # letzter Trade oder letzte Abfrage mit Position


class Scheduler:
    def __init__(self, now_ms: int):
        self._users: dict[str, _User] = {}
        self._heap: list[tuple[int, str]] = []
        self._inflight: set[str] = set()
        self._t0 = now_ms

    def __len__(self) -> int:
        return len(self._users)

    def _set_due(self, user: str, due: int) -> None:
        self._users[user].due = due
        heapq.heappush(self._heap, (due, user))

    def seen_in_trade(self, user: str, now: int) -> None:
        u = self._users.setdefault(user, _User())
        u.last_active = max(u.last_active, now)
        if user in self._inflight:
            u.due = AGAIN  # nach Abschluss der laufenden Abfrage sofort erneut
            return
        if u.due is None or u.due > now:
            self._set_due(user, now)

    def polled(self, user: str, notional: float, has_pos: bool, now: int) -> None:
        u = self._users.setdefault(user, _User())
        again = u.due == AGAIN
        self._inflight.discard(user)
        u.notional, u.has_pos = notional, has_pos
        if has_pos:
            u.last_active = max(u.last_active, now)
        self._set_due(user, now if again else now + interval_ms(notional, has_pos))

    def failed(self, user: str, now: int) -> None:
        self._inflight.discard(user)
        if user in self._users:
            self._set_due(user, now + RETRY_MS)

    def take(self, n: int, now: int) -> list[str]:
        out = []
        while self._heap and len(out) < n and self._heap[0][0] <= now:
            due, user = heapq.heappop(self._heap)
            u = self._users.get(user)
            if u is None or u.due != due:
                continue  # veralteter Eintrag
            u.due = None
            self._inflight.add(user)
            out.append(user)
        return out

    def next_due(self, user: str) -> int | None:
        return self._users[user].due

    def drop_stale(self, now: int) -> int:
        stale = [k for k, u in self._users.items()
                 if not u.has_pos and u.last_active < now - DROP_AFTER_MS and k not in self._inflight]
        for k in stale:
            del self._users[k]
        return len(stale)

    def lateness_ms(self, now: int) -> float:
        late = [now - u.due for u in self._users.values() if u.due is not None and 0 <= u.due <= now]
        return float(sum(late) / len(late)) if late else 0.0

    def notional(self, user: str) -> float:
        u = self._users.get(user)
        return u.notional if u else 0.0

    def to_state(self) -> dict:
        return {"users": {k: asdict(u) for k, u in self._users.items()}}

    @classmethod
    def from_state(cls, d: dict) -> "Scheduler":
        s = cls(0)
        for k, v in d.get("users", {}).items():
            u = _User(**v)
            due = u.due if u.due is not None and u.due != AGAIN else 0  # in Abfrage beim Absturz: sofort fällig
            s._users[k] = u
            s._set_due(k, due)
        return s
