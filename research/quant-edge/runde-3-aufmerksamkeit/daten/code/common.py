import os, time, threading, datetime, requests
OUT = "/Volumes/SSD 500G/offloaded/home/aaronpfutzner/Dateien - Local/DiamondHamster/r3-daten"
LOG = os.path.join(OUT, "request.log")
_lock = threading.Lock()
_sess = threading.local()
HOLD_START_MS = 1735689600000  # 2025-01-01 00:00 UTC
HOLD_END_MS = 1782863999999    # 2026-06-30 23:59:59.999 UTC
def sess():
    if not hasattr(_sess, "s"):
        _sess.s = requests.Session()
    return _sess.s
def log(url, status, note=""):
    t = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    with _lock:
        with open(LOG, "a") as f:
            f.write(f"{t}\t{status}\t{url}\t{note}\n")
class RateLimiter:
    def __init__(self, per_sec):
        self.iv = 1.0 / per_sec; self.l = threading.Lock(); self.next = 0.0
    def wait(self):
        with self.l:
            now = time.monotonic()
            if self.next > now:
                time.sleep(self.next - now); now = self.next
            self.next = now + self.iv
def get(url, headers=None, params=None, timeout=60, retries=4, limiter=None, method="GET", json=None, ok_statuses=(200, 404)):
    last = None
    for i in range(retries):
        if limiter: limiter.wait()
        try:
            r = sess().request(method, url, headers=headers, params=params, timeout=timeout, json=json)
            full = r.url if method == "GET" else url
            log(full, r.status_code, "" if i == 0 else f"retry{i}")
            if r.status_code in ok_statuses:
                return r
            last = r
            if r.status_code in (429, 418, 403, 500, 502, 503, 504, 520, 522, 524):
                time.sleep(min(60, 2 ** (i + 1) * (5 if r.status_code in (429, 418) else 1)))
                continue
            return r
        except Exception as e:
            log(url, "ERR", repr(e)[:200]); last = e; time.sleep(2 ** (i + 1))
    if isinstance(last, Exception):
        return None
    return last
