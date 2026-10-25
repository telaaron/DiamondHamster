"""Pseudonymisierung von Dokumenten vor dem KI-Leser (Runde 3, Phase 4).

Entfernt, was dem Modell Datum, Projekt oder Firma verraten kann: bekannte Namen
(Projekt, Token, Firma, Ticker), URLs, E-Mails, Adressen, Handles, Daten, Jahre,
Monatsnamen. Inhaltliche Zahlen (Prozente, Mengen) bleiben stehen.

Zweite Verteidigungslinie: Wiedererkennung ist trotzdem möglich (Sarkar/Vafa),
deshalb zählen nur Dokumente nach dem Modell-Cutoff.
"""
import re
from collections import Counter

_MONTHS = (r"Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|"
           r"Aug(?:ust)?|Sep(?:t(?:ember)?)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?")

# Reihenfolge zählt: Spezifisches vor Allgemeinem.
_PATTERNS = [
    ("URL", re.compile(r"\bhttps?://\S+|\bwww\.\S+", re.I)),
    ("EMAIL", re.compile(r"\b[\w.+-]+@[\w-]+\.[\w.-]+\b")),
    ("HASH", re.compile(r"\b0x[0-9a-fA-F]{64}\b")),
    ("ADDRESS", re.compile(r"\b0x[0-9a-fA-F]{40}\b")),
    ("ENS", re.compile(r"\b[\w-]+\.eth\b", re.I)),
    ("HANDLE", re.compile(r"(?<![\w@])@\w{2,}")),
    ("DATE", re.compile(r"\b\d{4}-\d{2}-\d{2}(?:[T ][\d:.]+Z?)?\b")),
    ("DATE", re.compile(r"\b\d{1,2}[/.]\d{1,2}[/.]\d{2,4}\b")),
    ("DATE", re.compile(rf"\b(?:{_MONTHS})\.?\s+\d{{1,2}}(?:st|nd|rd|th)?(?:,?\s+\d{{4}})?\b", re.I)),
    ("DATE", re.compile(rf"\b\d{{1,2}}(?:st|nd|rd|th)?\s+(?:{_MONTHS})\b\.?(?:,?\s+\d{{4}})?", re.I)),
    ("TS", re.compile(r"\b1[5-9]\d{8}\b")),
    ("YEAR", re.compile(r"\b(?:19[89]\d|20[0-3]\d)\b")),
    ("MONTH", re.compile(rf"\b(?:{_MONTHS})\b")),
]


def pseudonymize(text: str, entities: dict[str, list[str]]) -> tuple[str, Counter]:
    """Ersetzt Entitäten und Zeit-/Identitätsmerkmale durch Platzhalter wie [PROJECT].

    entities: Platzhalter -> Liste von Namen. Längere Namen werden zuerst ersetzt,
    Treffer nur als ganzes Wort, ohne Groß-/Kleinschreibung (außer kurze Ticker
    in Großbuchstaben); "$NAME" zählt mit.
    """
    counts: Counter = Counter()
    pairs = sorted(((name, label) for label, names in entities.items() for name in names if name.strip()),
                   key=lambda p: -len(p[0]))
    for name, label in pairs:
        # Kurze Ticker (≤ 4 Zeichen, oft echte Wörter wie ONE, GAS) nur in exakter Schreibung.
        flags = 0 if len(name) <= 4 and name.isupper() else re.I
        pat = re.compile(rf"(?<![\w$])\$?{re.escape(name)}(?!\w)", flags)
        text, k = pat.subn(f"[{label}]", text)
        counts[label] += k
    for label, pat in _PATTERNS:
        text, k = pat.subn(f"[{label}]", text)
        counts[label] += k
    return text, counts
