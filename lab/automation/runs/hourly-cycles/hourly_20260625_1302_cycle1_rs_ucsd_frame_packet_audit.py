#!/usr/bin/env python3
"""Audit RSUCSDFramePacket_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-1302-cycle1-rs-ucsd-frame-packet.md"
)


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing RS UCSD frame packet artifact: {DOC}") from exc


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class RSUCSDFramePacketAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity(self) -> None:
        self.assertEqual(self.summary["artifact"], "RSUCSDFramePacket_V1")
        self.assertEqual(self.summary["run_id"], "hourly-20260625-1302")
        self.assertEqual(self.summary["cycle"], 1)
        self.assertEqual(self.summary["lane"], 4)
        self.assertEqual(self.summary["verdict_class"], "blocked")

    def test_transcript_window_present_but_frame_sequence_absent(self) -> None:
        self.assertIs(self.summary["transcript_window_present"], True)
        self.assertEqual(self.summary["transcript_window"], "[00:32:07]-[00:37:41]")
        self.assertIs(self.summary["frame_sequence_present"], False)
        self.assertEqual(self.summary["frame_sequence_artifacts"], [])
        self.assertIs(self.summary["visual_material_captured"], False)
        self.assertEqual(self.summary["source_scope"]["frame_or_slide_sources_found"], [])
        self.assertIs(self.summary["source_scope"]["external_video_fetch_performed"], False)

    def test_transcript_language_not_accepted_as_typed_pure_rs_operator(self) -> None:
        status = self.summary["transcript_hosted_language_status"]
        self.assertIs(status["accepted_as_typed_pure_rs_operator"], False)
        self.assertIs(status["accepted_as_rs_minus_one_receipt"], False)
        positive = self.summary["strongest_positive_result"]
        self.assertEqual(positive["status"], "transcript_hosted_aggregate_operator_shape")
        self.assertIs(positive["accepted_as_typed_pure_rs_operator"], False)

    def test_typed_operator_fields_truthfully_block_population(self) -> None:
        fields = self.summary["typed_operator_fields"]
        self.assertIs(fields["source_surface"]["transcript_timestamp_present"], True)
        self.assertIs(fields["source_surface"]["slide_or_frame_locator_present"], False)
        self.assertIs(fields["domain"]["pure_rs_domain_present"], False)
        self.assertIs(fields["codomain"]["pure_rs_codomain_present"], False)
        self.assertIs(fields["degree_or_slot"]["minus_one_slot_present"], False)
        self.assertIs(fields["RS_only_purity"]["pure_rs_rule_present"], False)
        self.assertIs(fields["family_identity"]["P_RS_or_quotient_present"], False)
        self.assertIs(fields["family_identity"]["family_certificate_present"], False)
        self.assertIs(self.summary["ucsd_typed_rs_minus_one_operator_populatable"], False)

    def test_receipt_count_and_restarts_are_false(self) -> None:
        self.assertEqual(self.summary["accepted_rs_receipt_count"], 0)
        self.assertEqual(self.summary["accepted_rs_proof_restart_count"], 0)
        self.assertIs(self.summary["proof_restart_allowed"], False)
        self.assertIs(self.summary["generation_count_restart_allowed"], False)
        self.assertIs(self.summary["claim_promotion_allowed"], False)

    def test_forbidden_promotions_include_rollup_firewall(self) -> None:
        forbidden = set(self.summary["forbidden_promotions"])
        self.assertIn("UCSD_rollup_as_d_RS_minus_1_receipt", forbidden)
        self.assertIn("transcript_hosted_language_as_typed_pure_RS_operator", forbidden)
        self.assertIn("generation_count_restart_allowed", forbidden)
        self.assertIn("two_plus_one_generation_language_as_index_proof", forbidden)

    def test_no_promotional_phrases_present(self) -> None:
        lower = self.text.lower()
        prohibited_phrases = [
            "ucsd rollup is d_rs,-1",
            "ucsd roll-up is d_rs,-1",
            "ucsd rolled operator is d_rs,-1",
            "accepted rs receipt count: 1",
            "proof_restart_allowed: true",
            "generation_count_restart_allowed: true",
            "rs family identity passed",
            "two plus one generation language proves",
        ]
        for phrase in prohibited_phrases:
            self.assertNotIn(phrase, lower)

    def test_next_object_is_frame_sequence_before_typed_operator(self) -> None:
        next_object = self.summary["constructive_next_object"]
        self.assertEqual(next_object["id"], "UCSDFrameSequenceForRolledOperatorWindow_V1")
        self.assertIs(next_object["would_remove_or_test_obstruction"], True)
        self.assertIn("capture_locator", next_object["required_fields"])
        self.assertIn("visible_symbol_transcription", next_object["required_fields"])
        self.assertIn("rs_projection_or_quotient", next_object["required_fields"])


if __name__ == "__main__":
    unittest.main()
