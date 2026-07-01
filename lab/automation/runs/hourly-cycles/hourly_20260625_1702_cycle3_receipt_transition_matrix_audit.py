"""Audit the 1702 cycle 3 receipt transition matrix."""

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
    / "hourly-20260625-1702-cycle3-receipt-transition-matrix.md"
)

EXPECTED_ARTIFACT_ID = "RECEIPT_TRANSITION_MATRIX_AFTER_1702_C3_L2_V1"
EXPECTED_RUN_ID = "hourly-20260625-1702"
EXPECTED_OWNED_PATH = (
    "explorations/hourly-20260625-1702-cycle3-receipt-transition-matrix.md"
)
EXPECTED_AUDIT = (
    "tests/hourly_20260625_1702_cycle3_receipt_transition_matrix_audit.py"
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


class ReceiptTransitionMatrixAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_json_summary(cls.text)
        cls.rows = cls.summary["route_rows"]
        cls.rows_by_route = {row["route"]: row for row in cls.rows}

    def test_identity_and_owned_paths(self) -> None:
        self.assertEqual(self.summary["artifact"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.summary["artifact_id"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.summary["run_id"], EXPECTED_RUN_ID)
        self.assertEqual(self.summary["cycle"], 3)
        self.assertEqual(self.summary["lane"], 2)
        self.assertEqual(self.summary["owned_path"], EXPECTED_OWNED_PATH)
        self.assertEqual(self.summary["companion_audit"], EXPECTED_AUDIT)
        self.assertEqual(self.summary["verdict_class"], "blocked")

    def test_exactly_five_route_rows(self) -> None:
        self.assertEqual(self.summary["route_count"], 5)
        self.assertEqual(len(self.rows), 5)
        self.assertEqual(set(self.rows_by_route), EXPECTED_ROUTES)

    def test_zero_transition_counts(self) -> None:
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertEqual(self.summary["accepted_for_routing_count"], 0)
        self.assertEqual(self.summary["proof_ready_count"], 0)
        self.assertTrue(
            self.summary["zero_accepted_receipts_transitioned_to_proof_ready_routes"]
        )

        for row in self.rows:
            with self.subTest(route=row["route"]):
                self.assertEqual(row["cycle1_accepted_receipt_count"], 0)
                self.assertEqual(row["cycle2_accepted_receipt_count"], 0)
                self.assertFalse(row["accepted_for_routing"])
                self.assertFalse(row["proof_ready"])

    def test_no_target_import(self) -> None:
        self.assertFalse(self.summary["target_import_used"])
        for row in self.rows:
            self.assertFalse(row["target_import_used"], row["route"])

        firewall = self.summary["promotion_firewall"]
        self.assertFalse(firewall["proof_restart_allowed"])
        self.assertFalse(firewall["metadata_as_receipt_allowed"])
        self.assertFalse(firewall["schema_as_receipt_allowed"])
        self.assertFalse(firewall["adjacent_positive_as_receipt_allowed"])
        self.assertFalse(firewall["target_physics_as_selector_allowed"])
        self.assertFalse(firewall["global_GU_no_go_promoted"])

    def test_each_route_has_blocker_and_next_transition_object(self) -> None:
        for row in self.rows:
            with self.subTest(route=row["route"]):
                self.assertIsInstance(row["transition_blocker"], str)
                self.assertGreater(len(row["transition_blocker"]), 20)
                self.assertIsInstance(row["first_missing_object_or_field"], str)
                self.assertGreater(len(row["first_missing_object_or_field"]), 10)
                self.assertIsInstance(row["next_receipt_object"], str)
                self.assertGreater(len(row["next_receipt_object"]), 10)
                self.assertIsInstance(row["next_transition_object"], str)
                self.assertGreater(len(row["next_transition_object"]), 10)
                self.assertGreaterEqual(len(row["blocked_downstream_work"]), 3)

    def test_route_specific_next_objects(self) -> None:
        expected_next_receipts = {
            "PTUJ": "PTUJ_BRANCH_FIELD_COMPLETION_RECEIPT",
            "IG": "RawOrFormalD7BranchingTranscriptForShiabHomSpace_V1",
            "DGU/VZ": "SourceEmittedActualDGU01SameOperatorPacket_V1",
            "RS": "UCSDCaptureStackExecutionLedgerForRolledOperatorWindow_V1",
            "QFT": "SourceDefinedRawBranchLocalGaugeGroupoidPacketForRRawBO_V1",
        }
        for route, expected in expected_next_receipts.items():
            self.assertEqual(self.rows_by_route[route]["next_receipt_object"], expected)

        self.assertIn(
            "source_emitted_sector_rule",
            self.rows_by_route["DGU/VZ"]["first_missing_object_or_field"],
        )
        self.assertIn(
            "ProductBFullSummandMultiplicityDimensionTableMissing",
            self.rows_by_route["IG"]["first_missing_object_or_field"],
        )
        self.assertIn(
            "source_bytes_or_lawful_acquisition_route",
            self.rows_by_route["RS"]["first_missing_object_or_field"],
        )
        self.assertIn(
            "source_defined_iota_b_and_typed_R_raw_b_O",
            self.rows_by_route["QFT"]["first_missing_object_or_field"],
        )

    def test_transition_statuses_remain_blocked_or_underdefined(self) -> None:
        for row in self.rows:
            combined = " ".join(
                [
                    row["cycle1_producer_status"],
                    row["cycle2_admission_status"],
                    row["transition_blocker"],
                ]
            )
            self.assertRegex(combined, r"blocked|underdefined")
            self.assertNotRegex(combined, r"\baccepted\b.*\bproof\b")

    def test_text_explicitly_states_zero_proof_ready_transition(self) -> None:
        self.assertIn(
            "zero accepted receipts transitioned into proof-ready routes",
            self.text.lower(),
        )
        self.assertIn("accepted_for_routing_count: 0", self.text)
        self.assertIn("proof_ready_count: 0", self.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
