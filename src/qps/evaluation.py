from __future__ import annotations

import re
from typing import Iterable


_NUMBER_RE = re.compile(r"(?<![A-Za-z0-9])[-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?(?![A-Za-z0-9])")


def normalize_text(text: str) -> str:
    """Normalize whitespace/case for human-readable comparisons."""
    return " ".join(text.strip().lower().split())


def extract_candidate_answers(text: str) -> list[str]:
    """Extract plausible final numeric answers from a model response.

    This is intentionally conservative: it extracts standalone numeric tokens,
    while preserving the full response for auditability.
    """
    return _NUMBER_RE.findall(text)


def normalize_answer(text: str) -> str:
    """Normalize a simple expected answer."""
    cleaned = normalize_text(text)
    cleaned = re.sub(r"^answer\s*[:=-]?\s*", "", cleaned)
    return cleaned


def exact_match(text: str, expected: str) -> bool:
    """Exact match after light normalization."""
    return normalize_answer(text) == normalize_answer(expected)


def numeric_answer_match(text: str, expected: str) -> bool:
    """Return True if the expected numeric answer appears as a standalone token."""
    expected_normalized = normalize_answer(expected)
    candidates = extract_candidate_answers(text)
    return expected_normalized in candidates


def evaluate_answer(text: str, expected: str, mode: str = "numeric_token") -> dict:
    """Return auditable evaluation details.

    The pilot uses numeric_token because small models may add harmless prose
    even when the requested answer is correct. Exact match remains available.
    """
    if mode == "exact":
        correct = exact_match(text, expected)
    elif mode == "numeric_token":
        correct = numeric_answer_match(text, expected)
    else:
        raise ValueError(f"Unknown evaluation mode: {mode}")

    return {
        "correct": correct,
        "evaluation_mode": mode,
        "normalized_response": normalize_text(text),
        "candidate_answers": extract_candidate_answers(text),
        "expected_answer": normalize_answer(expected),
    }


def accuracy(values: Iterable[bool]) -> float:
    values = list(values)
    if not values:
        return 0.0
    return sum(values) / len(values)
