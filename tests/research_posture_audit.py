#!/usr/bin/env python3
"""Audit the repository research posture.

This is a structural documentation audit. It checks that the repo presents the
GU reconstruction hypothesis as the primary mission while preserving proof
discipline, falsification, and independent-math secondary outputs.
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
OVERVIEW = ROOT / "OVERVIEW.md"
CANON = ROOT / "CANON.md"
STATUS = ROOT / "RESEARCH-STATUS.md"
NEXT_STEPS = ROOT / "NEXT-STEPS.md"
CONTRIBUTING = ROOT / "CONTRIBUTING.md"
RUNBOOK = ROOT / "process" / "runbooks" / "five-lane-frontier-run.md"

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
    "advocacy",
    "verdict_inflation",
    "compatibility_as_derivation",
    "optimistic_rescue_of_failed_arguments",
    "failure_redefined_as_success",
    "target_data_hidden_as_reconstruction",
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

    def test_posture_declares_primary_gu_reconstruction_hypothesis(self) -> None:
        self.assertEqual(self.posture["artifact"], "RESEARCH_POSTURE")
        self.assertEqual(self.posture["primary_mission"], "GU_RECONSTRUCTION_PROGRAM")
        self.assertIn("Geometric_Unity_is_substantially_correct", self.posture["working_hypothesis"])
        self.assertEqual(
            self.posture["optimization_target"],
            "information_gain_about_whether_GU_is_true",
        )
        self.assertIn("Geometric Unity is substantially correct", self.posture_text)

    def test_posture_is_not_a_proof_or_advocacy_claim(self) -> None:
        self.assertIn("not a proof claim", self.posture_text)
        self.assertIn("Do not become advocates", self.posture_text)
        self.assertIn("GU_already_proved", self.posture["not_claims"])
        self.assertTrue(REQUIRED_FORBIDDEN.issubset(set(self.posture["forbidden_moves"])))

    def test_discipline_is_preserved(self) -> None:
        self.assertTrue(REQUIRED_DISCIPLINE.issubset(set(self.posture["discipline_preserved"])))
        for phrase in [
            "explicit assumptions",
            "falsification or rollback conditions",
            "correction logs",
            "no-go theorem assumption audits",
        ]:
            self.assertIn(phrase, self.posture_text)

    def test_two_missions_are_declared_and_ordered(self) -> None:
        self.assertEqual(self.posture["mission_a"]["name"], "GU Reconstruction Program")
        self.assertEqual(self.posture["mission_a"]["priority"], "primary")
        self.assertEqual(self.posture["mission_b"]["name"], "Independent Mathematical Contributions")
        self.assertEqual(self.posture["mission_b"]["priority"], "secondary")
        self.assertIn("signed_readout_theorem", self.posture["mission_b"]["examples"])

    def test_success_criteria_are_dual(self) -> None:
        criteria = set(self.posture["success_criteria"])
        self.assertIn("rigorous_GU_reconstruction_deriving_new_physics", criteria)
        self.assertIn("precise_explanation_of_why_GU_reconstruction_cannot_exist", criteria)

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
        self.assertIn("Mission B outputs", contributing)
        self.assertIn("Mission A from `RESEARCH-POSTURE.md`", runbook)
        self.assertIn("what mathematical object, invariant, category", runbook)


if __name__ == "__main__":
    unittest.main(verbosity=2)
