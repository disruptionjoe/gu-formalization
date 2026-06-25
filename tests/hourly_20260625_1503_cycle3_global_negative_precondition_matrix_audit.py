#!/usr/bin/env python3
"""Audit GlobalNegativeReceiptBundlePreconditionAfter1503_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-1503-cycle3-global-negative-precondition-matrix.md"
)

EXPECTED_ARTIFACT = "GlobalNegativeReceiptBundlePreconditionAfter1503_V1"
EXPECTED_ROUTES = {"PTUJ", "IG", "DGU", "RS", "QFT"}


def extract_json_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 6\. Machine-readable JSON summary\.\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing section 6 machine-readable JSON summary")
    return json.loads(match.group(1))


class GlobalNegativePreconditionAfter1503Audit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        if not ARTIFACT.exists():
            raise AssertionError(f"artifact missing: {ARTIFACT}")
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_json_summary(cls.text)
        cls.lower_text = cls.text.lower()

    def test_identity_fields_are_exact(self) -> None:
        self.assertEqual(self.summary["artifact"], EXPECTED_ARTIFACT)
        self.assertEqual(self.summary["artifact_id"], EXPECTED_ARTIFACT)
        self.assertEqual(self.summary["run_id"], "hourly-20260625-1503")
        self.assertEqual(self.summary["cycle"], 3)
        self.assertEqual(self.summary["lane"], 3)
        self.assertIn('artifact_id: "GlobalNegativeReceiptBundlePreconditionAfter1503_V1"', self.text)
        self.assertIn('run_id: "hourly-20260625-1503"', self.text)
        self.assertIn("cycle: 3", self.text)
        self.assertIn("lane: 3", self.text)

    def test_required_global_booleans_are_false(self) -> None:
        self.assertFalse(self.summary["global_no_go_promoted"])
        self.assertFalse(self.summary["complete_global_negative_bundle"])
        self.assertFalse(self.summary["complete_global_negative_bundle_present"])
        self.assertFalse(self.summary["scoped_negatives_are_global_negative_receipts"])
        self.assertFalse(self.summary["absence_proves_global_no_go"])
        self.assertIn('"global_no_go_promoted": false', self.text)
        self.assertIn('"complete_global_negative_bundle": false', self.text)

    def test_all_five_routes_are_present(self) -> None:
        routes = self.summary["routes"]
        self.assertEqual({route["route"] for route in routes}, EXPECTED_ROUTES)
        for route in EXPECTED_ROUTES:
            self.assertIn(f"| {route} |", self.text)
        for row in routes:
            self.assertFalse(row["global_no_go_promoted"], row["route"])
            self.assertTrue(row["why_not_global"], row["route"])
            self.assertTrue(row["global_precondition_failed"], row["route"])

    def test_scoped_negative_language_is_explicit(self) -> None:
        required_phrases = [
            "Scoped negatives are not global negative receipts.",
            "route-local blockers",
            "scoped source-window negatives",
            "route-local statements",
            "global no-go blocked; scoped negatives only",
        ]
        for phrase in required_phrases:
            self.assertIn(phrase.lower(), self.lower_text)
        self.assertEqual(self.summary["scoped_negative_count"], 5)
        self.assertEqual(self.summary["scoped_negative_scope"], "route_local_only")

    def test_no_absence_proves_global_no_go_claim(self) -> None:
        forbidden_claims = [
            "absence proves global no-go",
            "absence proves a global no-go",
            "absence proves the global no-go",
            "absence in the current checked scopes proves global no-go",
            "global no-go is promoted",
            "we promote a global no-go",
            "global negative receipt is complete",
            "complete global negative bundle is present",
        ]
        for phrase in forbidden_claims:
            self.assertNotIn(phrase, self.lower_text)
        self.assertIn("cannot support stronger global statements", self.lower_text)
        self.assertIn("absence in the current checked scopes does not prove global no-go", self.lower_text)

    def test_exact_1503_facts_are_recorded(self) -> None:
        self.assertEqual(self.summary["cycle_commits"]["cycle_1"], "b1a2cc5")
        self.assertEqual(self.summary["cycle_commits"]["cycle_2"], "74090c4")
        route_status = {row["route"]: row["current_status"] for row in self.summary["routes"]}
        self.assertIn("source_object_absence", route_status["PTUJ"])
        self.assertIn("missing_D7_transcript_or_proof_object", route_status["IG"])
        self.assertIn("scoped_source_window_negative", route_status["DGU"])
        self.assertIn("locator_present_visual_frames_absent", route_status["RS"])
        self.assertIn("underdefined_source_branch_and_gauge_quotient", route_status["QFT"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
