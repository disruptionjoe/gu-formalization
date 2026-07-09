#!/usr/bin/env python3
"""Audit public issue templates for contributor-intake discipline.

This is a documentation/process gate, not a mathematical certificate. It keeps
issue templates aligned with the repo's bounded-problem, source-provenance, and
falsification-test intake expectations.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ISSUE_TEMPLATE_DIR = ROOT / ".github" / "ISSUE_TEMPLATE"
EXPECTED_TEMPLATES = {
    "media-claim-mining.yml",
    "open-problem.yml",
    "reference-pointer.yml",
    "specification-proposal.yml",
}


def read_template(name: str) -> str:
    return (ISSUE_TEMPLATE_DIR / name).read_text(encoding="utf-8")


def template_names() -> set[str]:
    return {path.name for path in ISSUE_TEMPLATE_DIR.glob("*.yml")}


def stale_root_source_paths(text: str) -> list[str]:
    return re.findall(r"(?<!lab/)sources/[A-Za-z0-9._/-]+", text)


class IssueTemplateValidationAudit(unittest.TestCase):
    def test_expected_templates_are_accounted_for(self) -> None:
        self.assertEqual(EXPECTED_TEMPLATES, template_names())

    def test_issue_templates_do_not_point_at_retired_root_sources(self) -> None:
        stale: list[str] = []
        for name in sorted(EXPECTED_TEMPLATES):
            stale.extend(f"{name}: {match}" for match in stale_root_source_paths(read_template(name)))

        self.assertEqual([], stale)

    def test_media_claim_template_uses_live_lab_source_surfaces(self) -> None:
        text = read_template("media-claim-mining.yml")

        for rel in ["lab/sources/media-index.md", "lab/sources/claim-ledger.md"]:
            self.assertIn(rel, text)
            self.assertTrue((ROOT / rel).is_file(), rel)

        self.assertIn("They are not mathematical evidence by themselves", text)

    def test_open_problem_template_preserves_bounded_closure_framing(self) -> None:
        text = read_template("open-problem.yml")

        self.assertIn("bounded research tasks", text)
        self.assertIn("specific object, obstruction, or test", text)
        self.assertIn("Acceptance criteria", text)
        self.assertIn("progress, refutation, or clean closure", text)

    def test_specification_template_preserves_six_axis_and_falsification_fields(self) -> None:
        text = read_template("specification-proposal.yml")

        for phrase in [
            "Six-axis specification",
            "Lossy reduction map",
            "Candidate invariant",
            "First falsification tests",
        ]:
            self.assertIn(phrase, text)

    def test_reference_template_preserves_claim_gap_path_routing(self) -> None:
        text = read_template("reference-pointer.yml")

        self.assertIn("Reference pointer", text)
        self.assertIn("What claim, gap, or path does this reference affect?", text)
        self.assertIn("No-go theorem", text)
        self.assertIn("Evasion / counterexample", text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
