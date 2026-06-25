"""Audit UCSDCaptureStackExecutionLedgerForRolledOperatorWindow_1802_C1_L4_V1."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_PATH = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-1802-cycle1-rs-ucsd-capture-stack-execution-ledger.md"
)
EXPECTED_RUN_ID = "hourly-20260625-1802"
EXPECTED_ARTIFACT_ID = (
    "UCSDCaptureStackExecutionLedgerForRolledOperatorWindow_1802_C1_L4_V1"
)
EXPECTED_OWNED_PATH = (
    "explorations/hourly-20260625-1802-cycle1-rs-ucsd-capture-stack-execution-ledger.md"
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


class UCSDCaptureStackExecutionLedgerAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT_PATH.read_text(encoding="utf-8")
        cls.summary = load_json_summary(cls.text)

    def test_identity_and_path(self) -> None:
        self.assertEqual(self.summary["run_id"], EXPECTED_RUN_ID)
        self.assertEqual(self.summary["artifact_id"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.summary["owned_path"], EXPECTED_OWNED_PATH)
        self.assertEqual(self.summary["cycle"], 1)
        self.assertEqual(self.summary["lane"], 4)

    def test_capture_and_packet_booleans(self) -> None:
        self.assertIs(self.summary["capture_executed"], False)
        self.assertIs(self.summary["frame_packet_admitted"], False)
        self.assertIs(self.summary["visual_unavailability_packet_admitted"], False)
        self.assertEqual(self.summary["accepted_receipt_count"], 0)

    def test_transcript_locator_not_promoted(self) -> None:
        self.assertIs(self.summary["transcript_locator_promoted"], False)
        firewall = self.summary["promotion_firewall"]
        self.assertIs(firewall["transcript_promoted_to_typed_rs"], False)
        self.assertIs(firewall["locator_promoted_to_typed_rs"], False)
        self.assertIs(firewall["transcript_locator_promoted"], False)

    def test_proof_restart_requires_frame_packet(self) -> None:
        if self.summary["proof_restart_allowed"]:
            self.assertIs(self.summary["frame_packet_admitted"], True)
        else:
            self.assertIs(self.summary["proof_restart_allowed"], False)

    def test_missing_capture_fields_nonempty_when_blocked(self) -> None:
        self.assertEqual(self.summary["verdict"], "blocked")
        self.assertGreater(len(self.summary["missing_capture_fields"]), 0)
        self.assertIn(
            "source_bytes_or_lawful_acquisition_route",
            self.summary["missing_capture_fields"],
        )
        self.assertEqual(
            self.summary["first_obstruction"]["field"],
            "source_bytes_or_lawful_acquisition_route",
        )

    def test_packet_tests_match_top_level_decision(self) -> None:
        packet_tests = self.summary["packet_tests"]
        self.assertEqual(
            packet_tests["UCSDFrameSequenceForRolledOperatorWindow_V1"]["admitted"],
            self.summary["frame_packet_admitted"],
        )
        self.assertEqual(
            packet_tests["UCSDVisualUnavailabilityPacketForRolledOperatorWindow_V1"][
                "admitted"
            ],
            self.summary["visual_unavailability_packet_admitted"],
        )


if __name__ == "__main__":
    unittest.main()
