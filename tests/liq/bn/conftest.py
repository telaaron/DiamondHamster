import hashlib
import io
import zipfile
from datetime import date, datetime, timezone

import pytest

from diamondhamster.liq.bn.download import NotFound, url_for

SYM = "BTCUSDT"


def ms(d: date, minute: int = 0) -> int:
    return int(datetime(d.year, d.month, d.day, tzinfo=timezone.utc).timestamp() * 1000) + minute * 60_000


def zipped(name: str, text: str) -> bytes:
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        z.writestr(name, text)
    return buf.getvalue()


def day_files(d: date, header: bool = True, minutes: int = 30) -> dict[str, str]:
    agg = "agg_trade_id,price,quantity,first_trade_id,last_trade_id,transact_time,is_buyer_maker\n" if header else ""
    met = "create_time,symbol,sum_open_interest,sum_open_interest_value\n"
    mk = "open_time,open,high,low,close,volume,close_time,quote_volume,count,taker_buy_volume,taker_buy_quote_volume,ignore\n" if header else ""
    for m in range(minutes):
        t = ms(d, m)
        agg += f"{m},{100000 + m},0.01,{m},{m},{t + 1000},{'true' if m % 2 else 'false'}\n"
        agg += f"{m}0,{100000 + m},20.0,{m},{m},{t + 2000},false\n"
        mk += f"{t},{100000 + m},{100050 + m},{99950 + m},{100000 + m},0,{t + 59999},0,0,0,0,0\n"
        if m % 5 == 0:
            met += f"{datetime.fromtimestamp(t / 1000, tz=timezone.utc):%Y-%m-%d %H:%M:%S},{SYM},{1000 + m},0\n"
    return {"aggTrades": agg, "metrics": met, "markPriceKlines": mk}


class FakeArchive:
    """Fake data.binance.vision: liefert Zip + .CHECKSUM, 404 für unbekannte URLs."""

    def __init__(self):
        self.files: dict[str, bytes] = {}
        self.calls: list[str] = []

    def add(self, url: str, payload: bytes, bad_checksum: bool = False):
        self.files[url] = payload
        digest = "0" * 64 if bad_checksum else hashlib.sha256(payload).hexdigest()
        self.files[url + ".CHECKSUM"] = f"{digest}  {url.rsplit('/', 1)[1]}\n".encode()

    def add_day(self, d: date, header: bool = True, skip=()):
        for kind, text in day_files(d, header).items():
            if kind not in skip:
                url = url_for(kind, SYM, d)
                self.add(url, zipped(url.rsplit("/", 1)[1].replace(".zip", ".csv"), text))

    def add_funding(self, year: int, month: int, rates):
        url = url_for("fundingRate", SYM, date(year, month, 1))
        body = "calc_time,funding_interval_hours,last_funding_rate\n" + "".join(
            f"{ms(date(year, month, 1), 480 * i)},8,{r}\n" for i, r in enumerate(rates))
        self.add(url, zipped(url.rsplit("/", 1)[1].replace(".zip", ".csv"), body))

    def __call__(self, url: str) -> bytes:
        self.calls.append(url)
        if url not in self.files:
            raise NotFound(url)
        return self.files[url]


@pytest.fixture
def archive():
    return FakeArchive()
