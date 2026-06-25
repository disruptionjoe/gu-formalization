#!/usr/bin/env python3
"""Audit GLOBAL_NEGATIVE_PRECONDITION_MATRIX_1802_C3_L3_V1."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOC = (
    ROOT
    / "explorations"
    / "hourly-20260625-1802-cycle3-global-negative-precondition-matrix.md"
)

EXPECTED_RUN_ID = "hourly-20260625-1802"
EXPECTED_ARTIFACT_PATH = (
    "explorations/hourly-20260625-1802-cycle3-global-negative-precondition-matrix.md"
)


def extract_json_summary(text: str) -> dict:
    blocks = re.findall(r"```json\n(.*?)\n```", text, re.DOTALL)
    if not blocks:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(blocks[-1])


class GlobalNegativePreconditionMatrix1802Audit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = DOC.read_text(encoding="utf-8")
        cls.summary = extract_json_summary(cls.text)

    def test_required_identity_fields(self) -> None:
        self.assertEqual(self.summary["run_id"], EXPECTED_RUN_ID)
        self.assertEqual(self.summary["artifact_path"], EXPECTED_ARTIFACT_PATH)
        self.assertEqual(self.summary["owned_path"], EXPECTED_ARTIFACT_PATH)

    def test_required_non_promotion_flags(self) -> None:
        self.assertIs(self.summary["global_no_go_promoted"], False)
        self.assertIs(self.summary["scoped_blockers_promoted"], False)
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertIs(self.summary["theorem_class_assumptions_complete"], False)
        self.assertIs(self.summary["route_coverage_complete"], False)
        self.assertIs(self.summary["source_proof_completeness"], False)
        self.assertIs(self.summary["branch_closure_complete"], False)
        self.assertIs(self.summary["positive_construction_failure_proved"], False)
        self.assertIs(self.summary["target_import_used"], False)

    def test_precondition_matrix_has_required_size_and_rows(self) -> None:
        rows = self.summary["precondition_rows"]
        self.assertGreaterEqual(len(rows), 6)
        names = {row["precondition"] for row in rows}
        self.assertIn("theorem_class_assumptions", names)
        self.assertIn("route_coverage", names)
        self.assertIn("source_proof_completeness", names)
        self.assertIn("branch_closure", names)
        self.assertIn("positive_construction_failure", names)
        self.assertIn("target_import_guard", names)


if __name__ == "__main__":
    unittest.main()
