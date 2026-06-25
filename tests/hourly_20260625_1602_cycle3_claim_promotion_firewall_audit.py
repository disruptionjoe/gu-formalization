#!/usr/bin/env python3
"""Audit ClaimPromotionFirewallAfter1602_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-1602-cycle3-claim-promotion-firewall.md"
)


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 7\. Machine-readable JSON summary\.\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary")
    return json.loads(match.group(1))


class ClaimPromotionFirewallAfter1602Audit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity(self) -> None:
        self.assertTrue(ARTIFACT.exists())
        self.assertEqual(self.summary["artifact_id"], "ClaimPromotionFirewallAfter1602_V1")
        self.assertEqual(self.summary["run_id"], "hourly-20260625-1602")
        self.assertEqual(self.summary["cycle"], 3)
        self.assertEqual(self.summary["lane"], 4)

    def test_no_promotion_counts_and_booleans(self) -> None:
        self.assertEqual(self.summary["promotions_allowed"], 0)
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["target_import_used"])
        self.assertFalse(self.summary["major_GU_claim_promoted"])
        self.assertFalse(self.summary["global_no_go_promoted"])

    def test_every_promotion_row_is_blocked_with_missing_prerequisite(self) -> None:
        rows = self.summary["promotion_rows"]
        self.assertGreaterEqual(len(rows), 8)
        for row in rows:
            with self.subTest(claim_family=row["claim_family"]):
                self.assertEqual(row["status"], "blocked")
                self.assertFalse(row["promotion_allowed"])
                self.assertIsInstance(row["missing_prerequisite"], str)
                self.assertGreater(len(row["missing_prerequisite"]), 20)
                self.assertTrue(row["next_object"])
                self.assertTrue(row["blocked_bases"])

    def test_rejected_bases_include_required_non_promotion_classes(self) -> None:
        rejected = {str(item).lower() for item in self.summary["rejected_bases"]}
        self.assertIn("locator", rejected)
        self.assertIn("schema", rejected)
        self.assertIn("scoped-negative", rejected)
        self.assertIn("compatibility", rejected)

    def test_required_claim_families_are_present(self) -> None:
        families = {row["claim_family"] for row in self.summary["promotion_rows"]}
        expected = {
            "PTUJ_formula_source_identity",
            "IG_K_IG_selector",
            "DGU_VZ_actual_identity_and_replay",
            "RS_typed_operator_generation_index",
            "QFT_source_branch_quotient_CHSH",
            "dark_energy_generation_major_physics",
            "major_GU_reconstruction",
            "global_no_go",
        }
        self.assertEqual(families, expected)

    def test_no_positive_promotion_literals(self) -> None:
        forbidden_patterns = [
            r'"promotions_allowed"\s*:\s*[1-9]\d*',
            r'"accepted_receipt_count"\s*:\s*[1-9]\d*',
            r'"proof_restart_allowed"\s*:\s*true',
            r'"target_import_used"\s*:\s*true',
            r'"major_GU_claim_promoted"\s*:\s*true',
            r'"global_no_go_promoted"\s*:\s*true',
        ]
        for pattern in forbidden_patterns:
            with self.subTest(pattern=pattern):
                self.assertIsNone(re.search(pattern, self.text, flags=re.IGNORECASE))


if __name__ == "__main__":
    unittest.main(verbosity=2)
