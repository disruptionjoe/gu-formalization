"""Audit the 1802 cycle 3 receipt transition matrix."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "explorations"
    / "hourly-20260625-1802-cycle3-receipt-transition-matrix.md"
)

EXPECTED_RUN_ID = "hourly-20260625-1802"
EXPECTED_ARTIFACT_PATH = (
    "explorations/hourly-20260625-1802-cycle3-receipt-transition-matrix.md"
)
EXPECTED_ROUTES = {"PTUJ", "IG", "DGU/VZ", "RS", "QFT"}


def extract_json_summary(text: str) -> dict[str, Any]:
    match = re.search(
        r"## 6\. Machine-readable JSON summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary")
    return json.loads(match.group(1))


class ReceiptTransitionMatrix1802Audit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_json_summary(cls.text)
        cls.rows = cls.summary["route_rows"]
        cls.rows_by_route = {row["route"]: row for row in cls.rows}

    def test_identity_and_artifact_path(self) -> None:
        self.assertEqual(self.summary["run_id"], EXPECTED_RUN_ID)
        self.assertEqual(self.summary["artifact_path"], EXPECTED_ARTIFACT_PATH)
        self.assertEqual(self.summary["owned_path"], EXPECTED_ARTIFACT_PATH)
        self.assertEqual(self.summary["cycle"], 3)
        self.assertEqual(self.summary["lane"], 2)
        self.assertEqual(self.summary["verdict_class"], "blocked")

    def test_exactly_five_transition_rows(self) -> None:
        self.assertEqual(self.summary["route_count"], 5)
        self.assertEqual(len(self.rows), 5)
        self.assertEqual(set(self.rows_by_route), EXPECTED_ROUTES)

    def test_zero_accepted_counts(self) -> None:
        self.assertEqual(self.summary["accepted_transition_count"], 0)
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertEqual(self.summary["accepted_for_routing_count"], 0)
        self.assertEqual(self.summary["proof_ready_count"], 0)

    def test_no_transition_fired(self) -> None:
        self.assertFalse(self.summary["transition_fired"])
        self.assertTrue(self.summary["no_transition_fired"])
        for row in self.rows:
            with self.subTest(route=row["route"]):
                self.assertFalse(row["accepted_transition"])
                self.assertFalse(row["transition_fired"])
                self.assertFalse(row["accepted_for_routing"])
                self.assertFalse(row["proof_ready"])
                self.assertEqual(row["cycle1_accepted_receipt_count"], 0)
                self.assertEqual(row["cycle2_accepted_receipt_count"], 0)

    def test_every_row_has_missing_witness_and_sequential_edge(self) -> None:
        for row in self.rows:
            with self.subTest(route=row["route"]):
                witness = row.get("missing_transition_witness")
                edge = row.get("sequential_next_edge")
                self.assertIsInstance(witness, str)
                self.assertGreater(len(witness), 10)
                self.assertIsInstance(edge, str)
                self.assertIn("->", edge)
                self.assertGreater(len(edge), 25)

    def test_target_import_used_false_everywhere(self) -> None:
        self.assertFalse(self.summary["target_import_used"])
        for row in self.rows:
            with self.subTest(route=row["route"]):
                self.assertFalse(row["target_import_used"])

        firewall = self.summary["promotion_firewall"]
        self.assertFalse(firewall["proof_restart_allowed"])
        self.assertFalse(firewall["metadata_as_receipt_allowed"])
        self.assertFalse(firewall["schema_as_receipt_allowed"])
        self.assertFalse(firewall["adjacent_positive_as_receipt_allowed"])
        self.assertFalse(firewall["target_physics_as_selector_allowed"])
        self.assertFalse(firewall["global_GU_no_go_promoted"])

    def test_route_specific_missing_witnesses(self) -> None:
        expected_witness_terms = {
            "PTUJ": "SingleCompletePTUJBranchReceipt_V1",
            "IG": "ProductBFullD7SummandMultiplicityDimensionTableReceipt_V1",
            "DGU/VZ": "SourceEmittedDGU01SectorRuleAndSameOperatorReceipt_V1",
            "RS": "RSLawfulSourceAcquisitionRouteOrBrowserCaptureRouteForFBozSSLxFvIWindow_V1",
            "QFT": "QFTSourceDefinedIotaBAndTypedRRawBOReceipt_V1",
        }
        for route, expected in expected_witness_terms.items():
            self.assertIn(expected, self.rows_by_route[route]["missing_transition_witness"])

    def test_text_states_no_transition(self) -> None:
        self.assertIn("zero accepted receipts transitioned into proof-ready routes", self.text.lower())
        self.assertIn("accepted_transition_count: 0", self.text)
        self.assertIn("transition_fired: false", self.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
