#!/usr/bin/env python3
"""Audit NEXT-STEPS front-door guardrails.

This is a documentation/process gate, not a research-content check. It keeps
the public contributor roadmap wired to current status discipline, claim-status
workflow routing, and research posture without evaluating any scientific claim.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NEXT_STEPS = ROOT / "NEXT-STEPS.md"
CLAIM_STATUS_WORKFLOW = (
    ROOT / "lab" / "process" / "runbooks" / "claim-status-consistency-quality-workflow.md"
)
RESEARCH_POSTURE = ROOT / "RESEARCH-POSTURE.md"
FIREWALL_BOUNDARY_CANON = ROOT / "canon" / "firewall-boundary-hypothesis.md"


def read_next_steps() -> str:
    return NEXT_STEPS.read_text(encoding="utf-8")


def parse_front_matter(text: str) -> dict[str, str]:
    text = text.removeprefix("\ufeff")
    match = re.match(r"\A---\s*\n(?P<body>.*?)\n---\s*\n", text, flags=re.DOTALL)
    if not match:
        raise AssertionError("NEXT-STEPS.md is missing front matter")

    metadata: dict[str, str] = {}
    for line in match.group("body").splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip().strip('"')
    return metadata


class NextStepsFrontdoorGuardAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_next_steps()
        cls.metadata = parse_front_matter(cls.text)

    def test_document_remains_contributor_roadmap(self) -> None:
        self.assertEqual("Next Steps For Contributors", self.metadata.get("title"))
        self.assertEqual("active_research", self.metadata.get("status"))
        self.assertEqual("roadmap", self.metadata.get("doc_type"))
        self.assertIn("# Next Steps For Contributors", self.text)

    def test_current_front_door_names_steward_portfolio_priority(self) -> None:
        current = self.text.split(
            "[SUPERSEDED as the hourly queue by the steward-maintained portfolio above",
            1,
        )[0]
        required = (
            "THREE PROGRESS LANES PLUS STEWARDSHIP",
            "Lane 1, GU truth testing",
            "Lane 2, prediction extraction and computation",
            "Lane 3, result hardening and publication readiness",
            "Lane A, Stewardship",
            "rerank-next-work",
            "RECOVERY-CERTIFICATION",
            "RECOVERY-CONTRACT",
            "recovery-certification-matrix.json",
            "PRED-FLAVOR-RANK",
            "PRED-NORM-RANK",
            "PROOF-STABLE-KERNELS",
            "DE-F1-TRIPWIRE",
            "GU-002 packages that result",
            "Proposition 1",
            "W235 record bit",
            "no longer allocate W numbers",
        )
        missing = [phrase for phrase in required if phrase not in current]
        self.assertEqual([], missing)

    def test_firewall_boundary_historical_thread_stays_attack_not_defend(self) -> None:
        required = (
            "2026-06-28 (now #2, historical primary): the Firewall-Boundary Hypothesis",
            "primary falsification target",
            "firewall-like BOUNDARY object",
            "canon/firewall-boundary-hypothesis.md",
            "Attack it, do not defend it.",
        )
        missing = [phrase for phrase in required if phrase not in self.text]
        self.assertEqual([], missing)
        self.assertTrue(FIREWALL_BOUNDARY_CANON.is_file())

    def test_status_guard_routes_promotions_through_claim_workflow(self) -> None:
        required = (
            "global status guard",
            "Current source of truth",
            "`ind_H(D_GU)=24` is OPEN",
            "Do not promote older stronger language",
            "lab/process/runbooks/claim-status-consistency-quality-workflow.md",
        )
        missing = [phrase for phrase in required if phrase not in self.text]
        self.assertEqual([], missing)
        self.assertTrue(CLAIM_STATUS_WORKFLOW.is_file())

    def test_contributor_intro_keeps_truth_seeking_scope(self) -> None:
        normalized = " ".join(self.text.split())
        required = (
            "determine whether Geometric Unity can be rigorously reconstructed, extended, or falsified",
            "one construction",
            "clear failure condition",
            "information gain about the central GU hypothesis",
            "RESEARCH-POSTURE.md",
        )
        missing = [phrase for phrase in required if phrase not in normalized]
        self.assertEqual([], missing)
        self.assertTrue(RESEARCH_POSTURE.is_file())


if __name__ == "__main__":
    unittest.main(verbosity=2)
