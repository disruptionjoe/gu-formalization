"""Audit RSCaptureStackUnavailabilityLedger_1702_C2_L4_V1."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_PATH = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-1702-cycle2-rs-capture-stack-unavailability-ledger.md"
)
EXPECTED_RUN_ID = "hourly-20260625-1702"
EXPECTED_ARTIFACT_ID = "RSCaptureStackUnavailabilityLedger_1702_C2_L4_V1"
EXPECTED_OWNED_PATH = (
    "explorations/hourly-20260625-1702-cycle2-rs-capture-stack-unavailability-ledger.md"
)
EXPECTED_AUDIT = (
    "tests/hourly_20260625_1702_cycle2_rs_capture_stack_unavailability_ledger_audit.py"
)
REQUIRED_LEDGER_ROWS = {
    "official_video_locator_access",
    "exact_window",
    "source_bytes_or_lawful_acquisition_route",
    "frame_extraction_tool",
    "ocr_crop_tool",
    "checksum_output_manifest",
    "visible_operator_fields",
    "archive_slide_inventory",
    "local_inventory",
    "tool_access_failure_records",
}


def load_json_summary(text: str) -> dict:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        re.DOTALL,
    )
    if not match:
        raise AssertionError("Machine-readable JSON summary block not found")
    return json.loads(match.group(1))


class RSCaptureStackUnavailabilityLedgerAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT_PATH.read_text(encoding="utf-8")
        cls.summary = load_json_summary(cls.text)
        cls.rows = {row["row_id"]: row for row in cls.summary["ledger_rows"]}

    def test_identity_and_paths(self) -> None:
        self.assertEqual(self.summary["run_id"], EXPECTED_RUN_ID)
        self.assertEqual(self.summary["artifact_id"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.summary["owned_path"], EXPECTED_OWNED_PATH)
        self.assertEqual(self.summary["companion_audit"], EXPECTED_AUDIT)
        self.assertEqual(self.summary["cycle"], 2)
        self.assertEqual(self.summary["lane"], 4)
        self.assertEqual(self.summary["verdict"], "blocked")

    def test_required_ledger_rows_present(self) -> None:
        self.assertEqual(set(self.rows), REQUIRED_LEDGER_ROWS)
        for row_id in REQUIRED_LEDGER_ROWS:
            self.assertIn("current_evidence", self.rows[row_id])
            self.assertIn("missing_for_acceptance", self.rows[row_id])
            self.assertIn("admission_role", self.rows[row_id])

    def test_neither_visual_nor_full_unavailability_packet_accepted(self) -> None:
        self.assertEqual(self.summary["packet_decision"], "neither")
        self.assertFalse(self.summary["visual_packet_admitted"])
        self.assertFalse(self.summary["full_unavailability_packet_admitted"])
        packet_tests = self.summary["packet_tests"]
        self.assertFalse(packet_tests["UCSDFrameSequenceForRolledOperatorWindow_V1"]["admitted"])
        self.assertFalse(
            packet_tests["UCSDVisualUnavailabilityPacketForRolledOperatorWindow_V1"][
                "admitted"
            ]
        )

    def test_no_proof_restart_target_import_or_typed_rs(self) -> None:
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["generation_restart_allowed"])
        self.assertFalse(self.summary["index_restart_allowed"])
        self.assertFalse(self.summary["target_import_used"])
        self.assertFalse(self.summary["target_import"])
        self.assertFalse(self.summary["typed_rs_operator_admitted"])
        self.assertFalse(self.summary["typed_RS"])

    def test_first_obstruction_and_next_object(self) -> None:
        obstruction = self.summary["first_obstruction"]
        self.assertIn("source_bytes_or_lawful_acquisition_route is missing", obstruction)
        self.assertIn("official locator is reachable", obstruction)
        self.assertIn(
            "source_bytes_or_lawful_acquisition_route",
            self.summary["first_missing_field_set"],
        )
        self.assertEqual(
            self.summary["next_object"],
            "UCSDCaptureStackExecutionLedgerForRolledOperatorWindow_V1",
        )

    def test_ledger_row_decisions(self) -> None:
        self.assertTrue(self.rows["official_video_locator_access"]["present"])
        self.assertTrue(self.rows["exact_window"]["present"])
        self.assertTrue(self.rows["local_inventory"]["present"])
        self.assertFalse(
            self.rows["source_bytes_or_lawful_acquisition_route"]["present"]
        )
        self.assertFalse(self.rows["frame_extraction_tool"]["present"])
        self.assertFalse(self.rows["ocr_crop_tool"]["present"])
        self.assertFalse(self.rows["checksum_output_manifest"]["present"])
        self.assertFalse(self.rows["visible_operator_fields"]["present"])
        self.assertFalse(self.rows["archive_slide_inventory"]["present"])
        self.assertFalse(self.rows["tool_access_failure_records"]["present"])

    def test_no_transcript_or_locator_promotion(self) -> None:
        self.assertTrue(self.summary["no_transcript_locator_promotion"])
        firewall = self.summary["promotion_firewall"]
        self.assertFalse(firewall["transcript_promoted_to_typed_rs"])
        self.assertFalse(firewall["locator_promoted_to_typed_rs"])
        self.assertEqual(
            firewall["transcript_or_locator_to_typed_rs_operator"], "forbidden"
        )
        self.assertTrue(firewall["typed_rs_requires_visible_fields"])
        self.assertFalse(firewall["proof_restart_allowed"])


if __name__ == "__main__":
    unittest.main()
