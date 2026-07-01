#!/usr/bin/env python3
"""Audit RS_UCSD_FRAME_ACQUISITION_CONTRACT."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-1302-cycle2-rs-ucsd-frame-acquisition-contract.md"
)


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing RS UCSD frame acquisition contract: {DOC}") from exc


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class RSUCSDFrameAcquisitionContractAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity(self) -> None:
        self.assertEqual(self.summary["artifact"], "RS_UCSD_FRAME_ACQUISITION_CONTRACT")
        self.assertEqual(self.summary["run_id"], "hourly-20260625-1302")
        self.assertEqual(self.summary["cycle"], 2)
        self.assertEqual(self.summary["lane"], 4)
        self.assertEqual(self.summary["verdict_class"], "blocked")

    def test_required_frame_windows_are_exact_and_complete(self) -> None:
        windows = self.summary["required_frame_windows"]
        self.assertEqual(len(windows), 5)
        expected = [
            ("ucsd_rs_context_y14", "00:32:07", "00:32:46"),
            ("ucsd_rs_generation_pullback", "00:32:46", "00:34:27"),
            ("ucsd_rs_complex_middle_map", "00:34:27", "00:35:30"),
            ("ucsd_rs_coupled_derivative", "00:35:30", "00:36:13"),
            ("ucsd_rs_rolled_symbol", "00:36:13", "00:37:41"),
        ]
        actual = [(w["id"], w["start"], w["end"]) for w in windows]
        self.assertEqual(actual, expected)
        for window in windows:
            self.assertIn("required_capture_density", window)
            self.assertGreaterEqual(len(window["required_fields"]), 3)

    def test_contract_has_required_fields_checksums_and_transcriptions(self) -> None:
        fields = set(self.summary["required_frame_or_slide_fields"])
        required = {
            "source_id",
            "source_kind",
            "capture_method",
            "timestamp_window",
            "frame_timestamp",
            "artifact_path",
            "crop_paths",
            "sha256_full_frame",
            "sha256_crop",
            "ocr_text_raw",
            "transcription_normalized",
            "visible_operator_name",
            "visible_domain",
            "visible_codomain",
            "visible_degree_or_slot",
            "visible_rs_projection_or_quotient",
            "intake_decision",
        }
        self.assertTrue(required.issubset(fields))
        checksums = self.summary["checksum_requirements"]
        self.assertIs(checksums["full_frame_sha256_required"], True)
        self.assertIs(checksums["crop_sha256_required"], True)
        self.assertIs(checksums["raw_ocr_retained"], True)
        self.assertIs(checksums["normalized_transcription_retained"], True)

    def test_transcript_is_not_promoted_to_typed_operator(self) -> None:
        self.assertIs(self.summary["transcript_window_present"], True)
        self.assertEqual(self.summary["transcript_window"], "[00:32:07]-[00:37:41]")
        self.assertIs(self.summary["transcript_only_promotion_rejected"], True)
        decisions = self.summary["acceptance_decisions"]
        self.assertIs(decisions["rejected_transcript_only_promotion"]["current_decision"], True)
        typed = self.summary["typed_operator_status"]
        self.assertIs(typed["ucsd_typed_operator_exists"], False)
        self.assertIs(typed["accepted_as_typed_operator"], False)
        self.assertIs(typed["accepted_as_rs_minus_one_receipt"], False)

    def test_frame_acquisition_remains_missing_unless_sequence_present(self) -> None:
        self.assertIs(self.summary["frame_sequence_present"], False)
        self.assertEqual(self.summary["frame_sequence_artifacts"], [])
        first_missing = self.summary["first_missing_source_object"]
        self.assertEqual(first_missing["id"], "UCSDFrameSequenceForRolledOperatorWindow_V1")
        self.assertIs(first_missing["exists"], False)
        self.assertIs(self.summary["acceptance_decisions"]["missing"]["current_decision"], True)

    def test_scoped_demotion_is_not_overclaimed_from_transcript_only_evidence(self) -> None:
        self.assertIs(self.summary["scoped_ucsd_demotion_justified"], False)
        self.assertEqual(
            self.summary["scoped_ucsd_demotion_scope"],
            "not_justified_for_full_ucsd_visual_route_until_frame_sequence_is_acquired_or_documented_unavailable",
        )
        self.assertIs(self.summary["transcript_only_demote_to_motivation"], True)
        forbidden = set(self.summary["forbidden_promotions"])
        self.assertIn("ucsd_route_demoted_without_frame_acquisition_or_documented_unavailability", forbidden)

    def test_receipt_restart_and_generation_claims_are_blocked(self) -> None:
        self.assertEqual(self.summary["accepted_rs_receipt_count"], 0)
        self.assertIs(self.summary["proof_restart_allowed"], False)
        self.assertIs(self.summary["generation_restart_allowed"], False)
        self.assertIs(self.summary["generation_count_promotion_allowed"], False)
        typed = self.summary["typed_operator_status"]
        self.assertIs(typed["pure_rs_domain_present"], False)
        self.assertIs(typed["pure_rs_codomain_present"], False)
        self.assertIs(typed["minus_one_slot_present"], False)
        self.assertIs(typed["rs_projection_or_quotient_present"], False)
        self.assertIs(typed["family_identity_runnable"], False)

    def test_acceptance_requires_frame_backed_typed_operator_fields(self) -> None:
        acceptance = self.summary["acceptance_decisions"]["accepted_for_typed_operator_test"]
        required = set(acceptance["requires"])
        self.assertIn("source_surface_with_frame_or_slide_locator", required)
        self.assertIn("visible_domain", required)
        self.assertIn("visible_codomain", required)
        self.assertIn("visible_degree_or_slot", required)
        self.assertIn("visible_rs_projection_or_quotient_or_family_certificate", required)
        self.assertIn("checksummed_full_frame_and_crop", required)
        self.assertEqual(acceptance["effect"], "candidate_receipt_pending_family_identity")

    def test_ucsd_to_d_rs_promotion_phrases_absent(self) -> None:
        prohibited_patterns = [
            r"\bUCSD\s+(?:rollup|roll-up|rolled operator|transcript)\s+is\s+d_RS,-1\b",
            r"\bUCSD\s+transcript\s+derives\s+d_RS,-1\b",
            r"\bUCSD\s+visual\s+route\s+has\s+failed\b",
            r"\baccepted_rs_receipt_count:\s*[1-9]\d*\b",
            r'"accepted_rs_receipt_count"\s*:\s*[1-9]\d*',
            r"\bproof_restart_allowed:\s*true\b",
            r'"proof_restart_allowed"\s*:\s*true',
            r"\bgeneration_restart_allowed:\s*true\b",
            r'"generation_restart_allowed"\s*:\s*true',
            r"\bRS\s+family\s+identity\s+passed\b",
            r"\btwo-plus-one\s+generation\s+language\s+proves\b",
            r"\btwo plus one\s+generation\s+language\s+proves\b",
        ]
        for pattern in prohibited_patterns:
            with self.subTest(pattern=pattern):
                self.assertIsNone(re.search(pattern, self.text, flags=re.IGNORECASE))


if __name__ == "__main__":
    unittest.main()
