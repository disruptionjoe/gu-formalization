#!/usr/bin/env python3
"""Audit the repository research posture.

This is a structural documentation audit. It checks that the repo presents GU
as a truth-seeking engine and live unifying-fit question while preserving proof
discipline, falsification, and independent-math outputs.
"""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
POSTURE = ROOT / "RESEARCH-POSTURE.md"
README = ROOT / "README.md"
OVERVIEW = ROOT / "docs" / "OVERVIEW.md"
CANON = ROOT / "CANON.md"
STATUS = ROOT / "RESEARCH-STATUS.md"
NEXT_STEPS = ROOT / "NEXT-STEPS.md"
CONTRIBUTING = ROOT / "CONTRIBUTING.md"
RUNBOOK = ROOT / "lab" / "process" / "runbooks" / "five-lane-frontier-run.md"

STALE_ENTRYPOINT_PHRASES = [
    "This repository is a public research map, not a proof of Geometric Unity.",
    "This repository is a first-principles research map, not a proof of Geometric Unity.",
    "The public posture is research-map-first, not proof-first.",
    "This repo should not ask contributors to solve Geometric Unity.",
]

REQUIRED_DISCIPLINE = {
    "explicit_assumptions",
    "falsification_conditions",
    "reconstruction_vs_proof_labeling",
    "correction_logs",
    "dependency_tracking",
    "promotion_criteria",
    "independent_verification",
    "no_go_assumption_audits",
}

REQUIRED_FORBIDDEN = {
    "advocacy_for_or_against_GU",
    "verdict_inflation",
    "compatibility_as_derivation",
    "optimistic_rescue_of_failed_arguments",
    "failure_redefined_as_success",
    "target_data_hidden_as_reconstruction",
    "treating_unforced_data_as_global_GU_failure",
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def extract_posture(text: str) -> dict[str, Any]:
    match = re.search(
        r"## Machine-Readable Posture\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable posture JSON block")
    return json.loads(match.group(1))


class ResearchPostureAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.posture_text = read(POSTURE)
        cls.posture = extract_posture(cls.posture_text)

    def test_posture_declares_truth_seeking_and_unifying_fit(self) -> None:
        self.assertEqual(self.posture["artifact"], "RESEARCH_POSTURE")
        self.assertEqual(
            self.posture["optimization_target"],
            "true_structure_and_a_reliable_truth_seeking_method",
        )
        self.assertEqual(self.posture["guiding_conjecture"]["name"], "Geometric_Unity")
        self.assertEqual(self.posture["guiding_conjecture"]["role"], "generative_test_case")
        self.assertIn("The unifying-fit question", self.posture_text)
        self.assertIn("force three", self.posture_text)

    def test_posture_is_not_a_proof_or_advocacy_claim(self) -> None:
        self.assertIn("not a campaign to prove Geometric Unity", self.posture_text)
        self.assertIn("Do not become advocates", self.posture_text)
        self.assertIn("prove_GU_true", self.posture["not_targets"])
        self.assertTrue(REQUIRED_FORBIDDEN.issubset(set(self.posture["forbidden_moves"])))

    def test_discipline_is_preserved(self) -> None:
        self.assertTrue(REQUIRED_DISCIPLINE.issubset(set(self.posture["discipline_preserved"])))
        for phrase in [
            "explicit assumptions",
            "falsification or rollback conditions",
            "correction logs",
            "no-go-theorem assumption audits",
        ]:
            self.assertIn(phrase, self.posture_text)

    def test_products_are_declared(self) -> None:
        products = set(self.posture["products"])
        self.assertIn("true_structure_at_honest_grade", products)
        self.assertIn("reliable_truth_seeking_method", products)
        self.assertIn("GU-independent results are often the strongest", self.posture_text)

    def test_byproducts_keep_all_verdicts_available(self) -> None:
        byproducts = set(self.posture["byproducts_all_successes"])
        self.assertIn("GU_reconstruction_deriving_new_physics", byproducts)
        self.assertIn("precise_explanation_why_a_reconstruction_cannot_exist", byproducts)
        self.assertIn("GU_independent_mathematics", byproducts)

    def test_entrypoints_reference_research_posture(self) -> None:
        for path in [README, OVERVIEW, CANON, STATUS, NEXT_STEPS]:
            text = read(path)
            self.assertIn("RESEARCH-POSTURE.md", text, str(path))

    def test_old_neutral_map_entrypoint_phrases_are_removed(self) -> None:
        entrypoints = "\n".join(read(path) for path in [README, OVERVIEW, CANON, NEXT_STEPS])
        for phrase in STALE_ENTRYPOINT_PHRASES:
            self.assertNotIn(phrase, entrypoints)

    def test_contributing_and_runbook_follow_new_priority(self) -> None:
        contributing = read(CONTRIBUTING)
        runbook = read(RUNBOOK)
        self.assertIn("can Geometric Unity be rigorously reconstructed", contributing)
        self.assertIn("Results that are valuable independent of GU are co-equal products", contributing)
        self.assertIn("truth-seeking posture in `RESEARCH-POSTURE.md`", runbook)
        self.assertIn("does bare GU force three generations", runbook)
        self.assertIn("what mathematical object, invariant, category", runbook)


if __name__ == "__main__":
    unittest.main(verbosity=2)
