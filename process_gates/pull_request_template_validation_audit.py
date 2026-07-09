#!/usr/bin/env python3
"""Audit the public pull-request template for validation discipline.

This is a documentation/process gate, not a mathematical certificate. It keeps
the contributor-facing PR checklist aligned with the repo's claim-grading,
claim-status, and reproduction-harness expectations.
"""

from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PR_TEMPLATE = ROOT / ".github" / "PULL_REQUEST_TEMPLATE.md"


def read_template() -> str:
    return PR_TEMPLATE.read_text(encoding="utf-8")


class PullRequestTemplateValidationAudit(unittest.TestCase):
    def test_template_keeps_claim_grading_discipline(self) -> None:
        text = read_template()

        self.assertIn("RESEARCH-POSTURE.md", text)
        self.assertIn("CONTRIBUTING.md", text)
        self.assertIn("[verified]", text)
        self.assertIn("[reconstruction]", text)
        self.assertIn("[speculation]", text)
        self.assertIn("lab/process/runbooks/claim-status-consistency-quality-workflow.md", text)

    def test_template_names_reproduction_and_process_gate_checks(self) -> None:
        text = read_template()

        self.assertIn("## Validation / reproduction", text)
        self.assertIn("python scripts/reproduce_all.py --quick --tracked-only", text)
        self.assertIn("python process_gates/reproduction_docs_consistency_audit.py", text)
        self.assertIn("python process_gates/process_gate_readme_inventory_audit.py", text)
        self.assertIn("Reported any skipped heavy, full-suite, or Lean checks and why", text)

    def test_template_preserves_non_gate_framing(self) -> None:
        text = read_template()

        self.assertIn("this is a checklist, not a gate", text)
        self.assertNotIn("every pr must run the full certificate suite", text.casefold())


if __name__ == "__main__":
    unittest.main(verbosity=2)
