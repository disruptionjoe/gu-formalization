#!/usr/bin/env python3
"""Audit the three-cycle fifteen-hole frontier-run workflow."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
RUNBOOK = ROOT / "process" / "runbooks" / "three-cycle-fifteen-hole-run.md"
UNIT_RUNBOOK = ROOT / "process" / "runbooks" / "five-lane-frontier-run.md"
PROCESS_README = ROOT / "process" / "README.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def workflow_json(text: str) -> dict[str, Any]:
    match = re.search(
        r"## Machine-Readable Workflow\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable workflow JSON block")
    return json.loads(match.group(1))


class ThreeCycleFifteenHoleRunbookAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read(RUNBOOK)
        cls.workflow = workflow_json(cls.text)

    def test_declares_three_cycles_and_fifteen_quality_holes(self) -> None:
        self.assertEqual(self.workflow["cycles"], 3)
        self.assertEqual(self.workflow["lanes_per_cycle"], 5)
        self.assertEqual(self.workflow["target_quality_holes"], 15)
        self.assertIn("fifteen quality holes", self.text)
        self.assertIn("quality hole is not a small chore", self.text)

    def test_uses_five_lane_runbook_as_unit(self) -> None:
        self.assertEqual(
            self.workflow["unit_runbook"],
            "process/runbooks/five-lane-frontier-run.md",
        )
        self.assertIn("The unit of work is still `five-lane-frontier-run.md`", self.text)
        self.assertIn("three-cycle-fifteen-hole-run.md", read(UNIT_RUNBOOK))

    def test_forbids_padding_weak_lanes(self) -> None:
        self.assertTrue(self.workflow["padding_forbidden"])
        self.assertIn("Do not pad the batch", self.text)
        self.assertIn("run only the quality lanes", self.text)
        self.assertIn("padding_weak_lanes", self.workflow["forbidden_modes"])

    def test_requires_cycle_commit_push_and_sequential_learning(self) -> None:
        self.assertTrue(self.workflow["cycle_commit_required"])
        self.assertTrue(self.workflow["cycle_push_required"])
        self.assertIn("Commit and push the cycle before starting the next cycle", self.text)
        self.assertIn("update_hole_bank_after_each_cycle", self.workflow["sequential_learning_rule"])

    def test_parallel_scopes_must_be_disjoint(self) -> None:
        self.assertIn("disjoint owned artifact path", self.text)
        self.assertIn("parallel_within_cycle_only_after_write_scopes_are_disjoint", self.workflow["parallelism_rule"])
        self.assertIn("overlapping_parallel_write_scopes", self.workflow["forbidden_modes"])

    def test_required_quality_fields_are_decision_grade(self) -> None:
        required = set(self.workflow["quality_hole_required_fields"])
        for key in [
            "specific_claim_or_bridge",
            "strongest_positive_construction_attempt",
            "first_exact_obstruction_or_missing_object",
            "rollback_or_falsification_condition",
            "next_meaningful_computation_or_proof_step",
        ]:
            self.assertIn(key, required)

    def test_process_readme_lists_workflow(self) -> None:
        readme = read(PROCESS_README)
        self.assertIn("three-cycle-fifteen-hole-run.md", readme)
        self.assertIn("fifteen quality holes", readme)


if __name__ == "__main__":
    unittest.main(verbosity=2)
