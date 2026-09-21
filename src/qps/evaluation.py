from __future__ import annotations

import re
from typing import Iterable


def normalize_answer(text: str) -> str:
    """Normalize simple final-answer strings for the pilot evaluator."""
    cleaned = text.strip().lower()
    cleaned = re.sub(r"^answer\s*[:=-]?\s*", "", cleaned)
    cleaned = re.sub(r"[^a-z0-9.\-+ ]+", " ", cleaned)
    return " ".join(cleaned.split())


def exact_match(text: str, expected: str) -> bool:
    return normalize_answer(text) == normalize_answer(expected)


def accuracy(values: Iterable[bool]) -> float:
    values = list(values)
    if not values:
        return 0.0
    return sum(values) / len(values)
