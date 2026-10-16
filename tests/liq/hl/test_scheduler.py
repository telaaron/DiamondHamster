from diamondhamster.liq.hl.scheduler import Scheduler

MIN = 60_000
DAY = 86_400_000


def test_trade_makes_due_now():
    s = Scheduler(0)
    s.seen_in_trade("a", 1000)
    assert s.take(10, 1000) == ["a"]
    assert s.take(10, 1000) == []  # genommen = in Arbeit, nicht doppelt


def test_interval_by_notional():
    s = Scheduler(0)
    for user, notional, has in [("big", 2e6, True), ("mid", 2e5, True), ("small", 50, True), ("none", 0, False)]:
        s.polled(user, notional, has, 0)
    assert s.next_due("big") == 2 * MIN
    assert s.next_due("mid") == 10 * MIN
    assert s.next_due("small") == 30 * MIN
    assert s.next_due("none") == 6 * 60 * MIN


def test_take_respects_n_and_order():
    s = Scheduler(0)
    s.polled("late", 50, True, 0)       # fällig 30 min
    s.polled("early", 2e6, True, 0)     # fällig 2 min
    s.seen_in_trade("now", 5)           # fällig sofort
    assert s.take(2, 31 * MIN) == ["now", "early"]
    assert s.take(5, 31 * MIN) == ["late"]


def test_trade_moves_scheduled_user_forward():
    s = Scheduler(0)
    s.polled("a", 0, False, 0)
    s.seen_in_trade("a", MIN)
    assert s.take(5, MIN) == ["a"]


def test_drop_after_3_days_without_pos_and_trade():
    s = Scheduler(0)
    s.seen_in_trade("a", 0)
    s.polled("a", 0, False, 0)
    s.polled("b", 1e5, True, 0)
    assert s.drop_stale(3 * DAY + 1) == 1
    assert len(s) == 1 and s.take(5, 10 * DAY) == ["b"]


def test_keep_if_trade_recent():
    s = Scheduler(0)
    s.polled("a", 0, False, 0)
    s.seen_in_trade("a", 3 * DAY)
    s.polled("a", 0, False, 3 * DAY)
    assert s.drop_stale(3 * DAY + 10) == 0


def test_lateness():
    s = Scheduler(0)
    s.seen_in_trade("a", 0)
    s.seen_in_trade("b", 0)
    assert s.lateness_ms(10_000) == 10_000
    assert Scheduler(0).lateness_ms(5) == 0.0


def test_state_roundtrip():
    s = Scheduler(0)
    s.polled("a", 2e6, True, 0)
    s.seen_in_trade("b", 7)
    t = Scheduler.from_state(s.to_state())
    assert len(t) == 2 and t.next_due("a") == 2 * MIN and t.take(5, 7) == ["b"]


def test_trade_during_poll_requeues_immediately():
    s = Scheduler(0)
    s.seen_in_trade("a", 0)
    assert s.take(5, 0) == ["a"]
    s.seen_in_trade("a", 10)
    s.polled("a", 50, True, 20)
    assert s.take(5, 20) == ["a"]


def test_failed_retries_after_a_minute():
    s = Scheduler(0)
    s.seen_in_trade("a", 0)
    s.take(5, 0)
    s.failed("a", 0)
    assert s.take(5, MIN - 1) == [] and s.take(5, MIN) == ["a"]
