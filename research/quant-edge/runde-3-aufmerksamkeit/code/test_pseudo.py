import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from pseudo import pseudonymize  # noqa: E402


def test_removes_entities_case_insensitive_and_ticker():
    out, n = pseudonymize("Uniswap DAO proposes that UNI holders and uniswap labs vote. $UNI up?",
                          {"PROJECT": ["Uniswap"], "TOKEN": ["UNI"]})
    assert "uniswap" not in out.lower()
    assert "UNI" not in out.replace("[", " ").split()
    assert out.count("[PROJECT]") == 2 and out.count("[TOKEN]") == 2
    assert n["PROJECT"] == 2


def test_entity_does_not_match_inside_words():
    out, _ = pseudonymize("UNIT tests and community", {"TOKEN": ["UNI"]})
    assert out == "UNIT tests and community"


def test_dates_years_months():
    s = "On 2026-07-15 and 15/07/2026, July 15, 2026, 3 Aug and in Q3 2026; fiscal 2025."
    out, _ = pseudonymize(s, {})
    for bad in ("2026", "2025", "July", "Aug", "15/07"):
        assert bad not in out, (bad, out)


def test_urls_emails_addresses_handles():
    s = ("See https://gov.example.org/t/123 or www.foo.io, mail a@b.com, "
         "send to 0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984, tx 0x" + "a" * 64 +
         ", ping @alice and vitalik.eth")
    out, _ = pseudonymize(s, {})
    for bad in ("https", "www.foo", "a@b.com", "0x1f98", "aaaa", "@alice", "vitalik.eth"):
        assert bad not in out, (bad, out)


def test_keeps_content_numbers():
    out, _ = pseudonymize("Raise the fee from 0.3% to 0.25% and cap at 1,000,000 tokens.", {})
    assert out == "Raise the fee from 0.3% to 0.25% and cap at 1,000,000 tokens."


def test_longer_entity_first():
    out, _ = pseudonymize("Arbitrum Foundation and Arbitrum", {"ORG": ["Arbitrum Foundation"], "PROJECT": ["Arbitrum"]})
    assert out == "[ORG] and [PROJECT]"


def test_short_ticker_case_sensitive():
    out, _ = pseudonymize("ONE holders get one vote; OP and op-code", {"TOKEN": ["ONE", "OP"]})
    assert out == "[TOKEN] holders get one vote; [TOKEN] and op-code"
