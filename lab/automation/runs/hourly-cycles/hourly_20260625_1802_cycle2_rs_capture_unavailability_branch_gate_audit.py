"""Audit RSCaptureUnavailabilityBranchGate_1802_C2_L4_V1."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_PATH = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-1802-cycle2-rs-capture-unavailability-branch-gate.md"
)
EXPECTED_RUN_ID = "hourly-20260625-1802"
EXPECTED_ARTIFACT_PATH = (
    "explorations/hourly-20260625-1802-cycle2-rs-capture-unavailability-branch-gate.md"
)


def load_json_summary(text: str) -> dict:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        re.DOTALL,
    )
    if not match:
        raise AssertionError("Machine-readable JSON summary block not found")
    return json.loads(match.group(1))


class RSCaptureUnavailabilityBranchGateAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT_PATH.read_text(encoding="utf-8")
        cls.summary = load_json_summary(cls.text)

    def test_identity_and_artifact_path(self) -> None:
        self.assertEqual(self.summary["run_id"], EXPECTED_RUN_ID)
        self.assertEqual(self.summary["artifact_path"], EXPECTED_ARTIFACT_PATH)
        self.assertEqual(self.summary["owned_path"], EXPECTED_ARTIFACT_PATH)
        self.assertEqual(self.summary["cycle"], 2)
        self.assertEqual(self.summary["lane"], 4)

    def test_no_packet_branch_admitted(self) -> None:
        self.assertIs(self.summary["frame_packet_admitted"], False)
        self.assertIs(self.summary["visual_unavailability_packet_admitted"], False)
        self.assertIs(self.summary["positive_branch"]["admitted"], False)
        self.assertIs(self.summary["negative_branch"]["admitted"], False)
        self.assertEqual(self.summary["branch_gate_decision"], "neither_branch_admitted")

    def test_no_transcript_or_failed_capture_promotion(self) -> None:
        self.assertIs(self.summary["transcript_locator_promoted"], False)
        self.assertIs(
            self.summary["failed_local_capture_counts_as_unavailability"],
            False,
        )
        firewall = self.summary["promotion_firewall"]
        self.assertIs(firewall["transcript_to_frame_packet"], False)
        self.assertIs(firewall["locator_to_frame_packet"], False)
        self.assertIs(firewall["failed_local_capture_to_visual_unavailability"], False)
        self.assertIs(firewall["transcript_or_locator_to_typed_rs"], False)

    def test_locator_reachability_or_status_recorded(self) -> None:
        self.assertIn("current_locator_status", self.summary)
        self.assertTrue(
            self.summary["official_locator_reachable"]
            or bool(self.summary["current_locator_status"])
        )

    def test_zero_receipts_and_no_restart(self) -> None:
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertIs(self.summary["proof_restart_allowed"], False)
        self.assertIs(self.summary["typed_rs_intake_allowed"], False)
        self.assertIs(self.summary["generation_restart_allowed"], False)
        self.assertIs(self.summary["index_restart_allowed"], False)

    def test_next_object_names_lawful_route_or_denial_packet(self) -> None:
        next_object = self.summary["next_object"]
        self.assertRegex(next_object, r"Lawful.*CaptureRoute")
        self.assertRegex(next_object, r"FullVisualDenialPacket")
        self.assertEqual(
            self.summary["positive_branch"]["first_missing_object"],
            "RSLawfulSourceAcquisitionRouteOrBrowserCaptureRouteForFBozSSLxFvIWindow_V1",
        )
        self.assertEqual(
            self.summary["negative_branch"]["first_missing_object"],
            "UCSDFullVisualDenialPacketForRolledOperatorWindow_V1",
        )


if __name__ == "__main__":
    unittest.main()
