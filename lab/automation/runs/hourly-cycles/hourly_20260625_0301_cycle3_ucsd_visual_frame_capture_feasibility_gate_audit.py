#!/usr/bin/env python3
"""Audit UCSDVisualFrameCaptureFeasibilityGate_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0301-cycle3-ucsd-visual-frame-capture-feasibility-gate.md"
)

EXPECTED_WINDOWS = {
    "[00:02:05]-[00:04:08]",
    "[00:18:03]-[00:24:00]",
    "[00:34:27]-[00:36:13]",
    "[00:48:49]-[00:50:09]",
}

EXPECTED_ROW_PACKETS = {
    "UCSD_VIS_PKT_001_DGU_dark_energy_formula",
    "UCSD_VIS_PKT_002_DGU_theta_double_quotient",
    "UCSD_VIS_PKT_003_IG_RS_shiab_complex",
    "UCSD_VIS_PKT_004_QFT_DGU_unified_field_content",
}


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing UCSD visual frame feasibility artifact: {DOC}") from exc


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 9\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class UCSDVisualFrameCaptureFeasibilityGateAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)
        cls.rows = cls.summary["row_packets"]

    def test_artifact_identity_and_verdict(self) -> None:
        self.assertEqual(self.summary["artifact"], "UCSDVisualFrameCaptureFeasibilityGate_V1")
        self.assertEqual(self.summary["version"], "2026-06-25")
        self.assertEqual(self.summary["run"], "hourly-20260625-0301")
        self.assertEqual(self.summary["cycle"], 3)
        self.assertEqual(self.summary["lane"], 5)
        self.assertEqual(self.summary["verdict_class"], "blocked")
        self.assertIn("BLOCKED_LOCAL_VISUAL_MATERIAL_MISSING", self.summary["verdict"])
        identity = self.summary["artifact_identity"]
        self.assertEqual(
            identity["owned_path"],
            "explorations/hourly-20260625-0301-cycle3-ucsd-visual-frame-capture-feasibility-gate.md",
        )
        self.assertEqual(
            identity["companion_audit"],
            "tests/hourly_20260625_0301_cycle3_ucsd_visual_frame_capture_feasibility_gate_audit.py",
        )

    def test_all_four_windows_have_row_packets(self) -> None:
        self.assertEqual(set(self.summary["timestamp_windows_checked"]), EXPECTED_WINDOWS)
        self.assertEqual({row["transcript_window"] for row in self.rows}, EXPECTED_WINDOWS)
        self.assertEqual({row["row_packet_id"] for row in self.rows}, EXPECTED_ROW_PACKETS)
        self.assertEqual(len(self.rows), 4)

    def test_visual_material_availability_status_is_missing(self) -> None:
        scope = self.summary["scope"]
        availability = self.summary["local_visual_material_availability"]
        self.assertIs(scope["browsing_performed"], False)
        self.assertIs(scope["video_download_performed"], False)
        self.assertIs(scope["frame_capture_performed"], False)
        self.assertIs(scope["visual_material_inspected"], False)
        self.assertIs(scope["visual_material_available"], False)
        self.assertIs(scope["used_unrelated_untracked_outputs"], False)
        self.assertIs(availability["ucsd_video_file_found"], False)
        self.assertIs(availability["ucsd_slide_deck_found"], False)
        self.assertIs(availability["ucsd_screenshot_or_frame_found"], False)
        self.assertIs(availability["stable_visual_locator_found"], False)
        self.assertEqual(availability["availability_status"], "missing_local_visual_material")
        for row in self.rows:
            self.assertEqual(
                row["visual_material_availability_status"],
                "missing_local_visual_material",
                row["row_packet_id"],
            )

    def test_no_visual_formula_or_family_receipt_claims_without_capture(self) -> None:
        self.assertIs(self.summary["visual_frame_receipt_rows_instantiable_now"], False)
        self.assertIs(self.summary["row_packets_instantiable_now"], True)
        for row in self.rows:
            self.assertIs(row["visible_text_or_formula_claimed"], False, row["row_packet_id"])
            self.assertIs(row["displayed_slide_claimed"], False, row["row_packet_id"])
            self.assertIs(row["emitted_family_receipt_claimed"], False, row["row_packet_id"])
            self.assertIs(
                row["visual_frame_receipt_row_instantiated"],
                False,
                row["row_packet_id"],
            )
            self.assertEqual(row["row_schema_status"], "row_packet_only", row["row_packet_id"])
            self.assertEqual(row["acceptance_status"], "missing_visual_material")

    def test_accepted_receipt_count_zero_and_not_routable(self) -> None:
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertEqual(self.summary["accepted_receipts"], [])
        self.assertIn("Accepted receipt count from these row packets: **0**.", self.text)
        for row in self.rows:
            self.assertIs(row["accepted_for_routing"], False, row["row_packet_id"])

    def test_target_import_flags_are_closed_for_current_gate(self) -> None:
        global_flags = self.summary["target_import_global"]
        self.assertEqual(global_flags["target_data_seen"], [])
        self.assertIs(global_flags["target_import_detected"], False)
        self.assertIn("missing_visual_fields", global_flags["target_import_risk"])
        for row in self.rows:
            flags = row["target_import_flags"]
            self.assertEqual(flags["target_data_seen"], [], row["row_packet_id"])
            self.assertIs(flags["target_import_detected"], False, row["row_packet_id"])
            self.assertIs(
                flags["target_import_risk_if_filled_from_reconstruction"],
                True,
                row["row_packet_id"],
            )

    def test_proof_restart_and_promotion_gates_closed(self) -> None:
        self.assertIs(self.summary["proof_restart_allowed"], False)
        self.assertIs(self.summary["family_proof_promotion_allowed"], False)
        self.assertIs(self.summary["claim_promotion_allowed"], False)
        for row in self.rows:
            self.assertEqual(row["proof_restart_gate"], "blocked", row["row_packet_id"])
        for key, value in self.summary["no_claim_promotions"].items():
            self.assertIs(value, False, key)

    def test_constructive_next_object_is_source_safe_visual_packet(self) -> None:
        next_object = self.summary["constructive_next_object"]
        self.assertEqual(next_object["id"], "UCSDSourceSafeVisualArtifactPacket_V1")
        required = set(next_object["acceptance_preconditions"])
        self.assertIn("stable source locator", required)
        self.assertIn("repo-local visual artifact path or immutable archive locator", required)
        self.assertIn("target-import screening", required)


if __name__ == "__main__":
    unittest.main()
