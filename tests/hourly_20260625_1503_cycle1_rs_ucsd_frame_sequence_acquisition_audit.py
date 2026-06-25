"""Audit UCSDFrameSequenceForRolledOperatorWindow_V1."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_PATH = REPO_ROOT / "explorations" / "hourly-20260625-1503-cycle1-rs-ucsd-frame-sequence-acquisition.md"
EXPECTED_ARTIFACT_ID = "UCSDFrameSequenceForRolledOperatorWindow_V1"
EXPECTED_OWNED_PATH = "explorations/hourly-20260625-1503-cycle1-rs-ucsd-frame-sequence-acquisition.md"
EXPECTED_AUDIT = "tests/hourly_20260625_1503_cycle1_rs_ucsd_frame_sequence_acquisition_audit.py"


def load_json_summary(text: str) -> dict:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        re.DOTALL,
    )
    if not match:
        raise AssertionError("Machine-readable JSON summary block not found")
    return json.loads(match.group(1))


class UCSDFrameSequenceAcquisitionAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT_PATH.read_text(encoding="utf-8")
        cls.summary = load_json_summary(cls.text)

    def test_artifact_exists_and_frontmatter_identity(self) -> None:
        self.assertTrue(ARTIFACT_PATH.exists())
        self.assertTrue(self.text.startswith("---\n"))
        self.assertIn(f'artifact_id: "{EXPECTED_ARTIFACT_ID}"', self.text)
        self.assertIn(
            'verdict: "BLOCKED_REPO_LOCAL_FRAME_SEQUENCE_ABSENT_TRANSCRIPT_AGGREGATE_ONLY_ZERO_RS_RECEIPTS"',
            self.text,
        )
        self.assertIn(f'owned_path: "{EXPECTED_OWNED_PATH}"', self.text)
        self.assertIn(f'companion_audit: "{EXPECTED_AUDIT}"', self.text)

    def test_required_sections_present(self) -> None:
        for section in [
            "## 1. Verdict",
            "## 2. What Was Derived Directly From Repo Sources",
            "## 3. The Strongest Positive Result",
            "## 4. The First Exact Obstruction Or Missing Source Object",
            "## 5. The Constructive Next Object That Would Remove Or Test The Obstruction",
            "## 6. What This Means For RS `d_RS,-1`, RS Quotient, And Generation-Count Restart",
            "## 7. Next Meaningful Source Computation Step",
            "## 8. Machine-Readable JSON Summary",
        ]:
            self.assertIn(section, self.text)

    def test_json_identity_fields(self) -> None:
        self.assertEqual(self.summary["artifact"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.summary["owned_path"], EXPECTED_OWNED_PATH)
        self.assertEqual(self.summary["companion_audit"], EXPECTED_AUDIT)
        self.assertEqual(
            self.summary["verdict"],
            "BLOCKED_REPO_LOCAL_FRAME_SEQUENCE_ABSENT_TRANSCRIPT_AGGREGATE_ONLY_ZERO_RS_RECEIPTS",
        )
        self.assertEqual(self.summary["target_object"], "UCSDTypedRSMinusOneOperator_V1")

    def test_required_explicit_summary_fields(self) -> None:
        required_fields = [
            "transcript_window_present",
            "frame_sequence_present",
            "frame_sequence_artifacts",
            "required_frame_windows",
            "typed_operator_status",
            "accepted_rs_receipt_count",
            "proof_restart_allowed",
            "generation_restart_allowed",
            "target_import_used",
        ]
        for field in required_fields:
            self.assertIn(field, self.summary)

    def test_acquisition_status_blocks_typed_operator(self) -> None:
        self.assertIs(self.summary["transcript_window_present"], True)
        self.assertEqual(self.summary["transcript_window"], "[00:32:07]-[00:37:41]")
        self.assertIs(self.summary["frame_sequence_present"], False)
        self.assertEqual(self.summary["frame_sequence_artifacts"], [])
        self.assertEqual(self.summary["accepted_rs_receipt_count"], 0)
        self.assertIs(self.summary["proof_restart_allowed"], False)
        self.assertIs(self.summary["generation_restart_allowed"], False)
        self.assertIs(self.summary["target_import_used"], False)

    def test_required_frame_windows_are_exact_contract(self) -> None:
        expected = [
            ("ucsd_rs_context_y14", "00:32:07", "00:32:46"),
            ("ucsd_rs_generation_pullback", "00:32:46", "00:34:27"),
            ("ucsd_rs_complex_middle_map", "00:34:27", "00:35:30"),
            ("ucsd_rs_coupled_derivative", "00:35:30", "00:36:13"),
            ("ucsd_rs_rolled_symbol", "00:36:13", "00:37:41"),
        ]
        actual = [
            (row["id"], row["start"], row["end"])
            for row in self.summary["required_frame_windows"]
        ]
        self.assertEqual(actual, expected)

    def test_typed_operator_and_route_decisions_are_guarded(self) -> None:
        typed = self.summary["typed_operator_status"]
        self.assertEqual(typed["status"], "blocked_before_typed_operator")
        self.assertIs(typed["ucsd_typed_operator_exists"], False)
        self.assertIs(typed["accepted_as_typed_operator"], False)
        self.assertIs(typed["accepted_as_rs_minus_one_receipt"], False)
        self.assertIs(typed["pure_rs_domain_present"], False)
        self.assertIs(typed["pure_rs_codomain_present"], False)
        self.assertIs(typed["minus_one_slot_present"], False)
        self.assertIs(typed["operator_formula_present"], False)
        self.assertIs(typed["rs_projection_or_quotient_present"], False)
        self.assertIs(typed["family_identity_runnable"], False)
        self.assertIs(typed["can_proceed_to_UCSDTypedRSMinusOneOperator_V1"], False)

        route = self.summary["route_decision"]
        self.assertEqual(route["ucsd_route_status"], "blocked_at_frame_sequence_acquisition")
        self.assertEqual(route["transcript_branch_status"], "demoted_to_aggregate_motivation_only")
        self.assertIs(route["visual_route_demoted_aggregate_only"], False)
        self.assertIs(route["visual_route_can_proceed_to_typed_operator"], False)


if __name__ == "__main__":
    unittest.main()
