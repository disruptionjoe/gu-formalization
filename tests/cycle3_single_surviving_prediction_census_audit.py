"""Audit the Cycle 3 single-surviving-prediction census artifact.

This is a content audit, not a mathematical proof. It checks that the artifact
keeps the OBJ-FALSIFY discipline: enough candidates are ranked, no candidate is
promoted to a current surviving empirical prediction, and every ranked item has
a falsification condition.
"""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "explorations" / "cycle3-single-surviving-prediction-census-2026-06-24.md"


def _artifact_text() -> str:
    assert ARTIFACT.exists(), f"missing artifact: {ARTIFACT}"
    return ARTIFACT.read_text(encoding="utf-8")


def _json_summary(text: str) -> dict:
    marker = "## 8. Machine-Readable JSON Summary"
    assert marker in text, "machine-readable summary heading is missing"
    tail = text.split(marker, 1)[1]
    match = re.search(r"```json\s*(\{.*?\})\s*```", tail, flags=re.DOTALL)
    assert match, "machine-readable JSON block is missing"
    return json.loads(match.group(1))


def test_verdict_and_summary_exist() -> None:
    text = _artifact_text()
    assert "## 1. Verdict" in text
    assert "NO_CURRENT_CONCRETE_SURVIVING_EMPIRICAL_PREDICTION" in text
    summary = _json_summary(text)
    assert summary["verdict"] == "NO_CURRENT_CONCRETE_SURVIVING_EMPIRICAL_PREDICTION"
    assert summary["current_surviving_empirical_prediction_exists"] is False


def test_at_least_five_ranked_candidates_have_required_fields() -> None:
    summary = _json_summary(_artifact_text())
    candidates = summary["ranked_candidates"]
    assert len(candidates) >= 5
    assert summary["candidate_count"] == len(candidates)

    ranks = [candidate["rank"] for candidate in candidates]
    assert ranks == sorted(ranks), "candidates must be sorted by rank"
    assert ranks[0] == 1

    for candidate in candidates:
        assert candidate["id"].startswith("C")
        assert candidate["name"].strip()
        assert 1 <= candidate["nearness_to_decidable"] <= 5
        assert 1 <= candidate["information_gain"] <= 5
        assert candidate["source_dependence"].strip()
        assert candidate["current_status"].strip()


def test_no_current_surviving_empirical_prediction_is_claimed() -> None:
    summary = _json_summary(_artifact_text())
    assert summary["current_surviving_empirical_prediction_exists"] is False
    assert summary["all_current_candidates_reconstruction_grade_or_weaker"] is True

    promoted = [
        candidate
        for candidate in summary["ranked_candidates"]
        if candidate["qualifies_as_concrete_surviving_prediction"] is not False
    ]
    assert promoted == [], f"unexpected promoted candidates: {promoted}"


def test_best_next_candidate_is_explicit_and_ranked_first() -> None:
    text = _artifact_text()
    summary = _json_summary(text)
    assert summary["best_next_candidate_id"] == "C01"
    assert summary["best_next_candidate"].strip()
    assert "Best next candidate: C01" in text
    assert summary["ranked_candidates"][0]["id"] == summary["best_next_candidate_id"]


def test_falsification_conditions_are_present_for_all_ranked_candidates() -> None:
    text = _artifact_text()
    assert "falsification condition" in text.lower()
    summary = _json_summary(text)

    missing = [
        candidate["id"]
        for candidate in summary["ranked_candidates"]
        if not candidate.get("falsification_condition", "").strip()
    ]
    assert missing == [], f"missing falsification conditions: {missing}"
