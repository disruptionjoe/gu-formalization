#!/usr/bin/env python3
"""Audit the Cycle 3 rendered/manual RS minus-one map transcription packet."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "explorations"
    / "hourly-20260625-0301-cycle3-rendered-rs-minus-one-map-transcription.md"
)

REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. What Was Derived Directly From Repo Sources",
    "## 3. The Strongest Positive Result",
    "## 4. The First Exact Obstruction Or Missing Proof Object",
    "## 5. The Constructive Next Object",
    "## 6. What This Means For The Relevant GU Claim",
    "## 7. Next Meaningful Proof Or Computation Step",
    "## RenderedCriticalDisplayTranscriptionPacket_RS_V1",
    "## Machine-Readable JSON Summary",
]

REQUIRED_PAGES = {46, 47, 48, 62, 65}
REQUIRED_PACKET_FIELDS = {
    "packet_id",
    "page",
    "labels",
    "normalized_transcription_or_paraphrase",
    "rs_field_status",
    "rs_parameter_or_ghost_status",
    "emitted_map_status",
    "source_operator_context",
    "quotient_semantics",
    "identity_status_to_d_RS_minus_1",
    "accepted",
    "first_blocker",
}
FORBIDDEN_ACCEPTED_PATTERNS = [
    r'"accepted_receipt_count"\s*:\s*[1-9]',
    r'"accepted_rendered_rs_minus_one_map"\s*:\s*true',
    r'"accepted_source_differential_for_d_RS_minus_1"\s*:\s*true',
    r'"proof_restart_allowed"\s*:\s*true',
    r'"generation_count_promotion_allowed"\s*:\s*true',
    r"\brendered windows emit d_RS,-1\b",
    r"\bRS generation-count proof restart allowed\b",
]


def extract_summary(text: str) -> dict[str, object]:
    for block in re.findall(r"```json\s*(.*?)\s*```", text, re.DOTALL):
        data = json.loads(block)
        if data.get("artifact") == "RenderedCriticalDisplayTranscriptionPacket_RS_V1":
            return data
    raise AssertionError("RenderedCriticalDisplayTranscriptionPacket_RS_V1 JSON not found")


class RenderedRSMinusOneMapTranscriptionAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_required_sections_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_source_pages_and_methods_are_recorded(self) -> None:
        source = self.summary["source"]
        self.assertEqual(source["path"], "Geometric_UnityDraftApril1st2021.pdf")
        self.assertEqual(set(source["pages_checked"]), REQUIRED_PAGES)
        self.assertEqual(source["text_extraction_method"], "PyMuPDF get_text('text')")
        self.assertIn("PyMuPDF get_pixmap", source["rendering_method"])
        self.assertTrue(source["rendered_manual_inspection_performed"])
        self.assertFalse(source["pdftoppm_available"])
        self.assertFalse(source["rendered_files_retained_in_repo"])

    def test_rendered_records_cover_required_pages_with_labels(self) -> None:
        records = self.summary["rendered_page_records"]
        self.assertEqual({record["page"] for record in records}, REQUIRED_PAGES)
        by_page = {record["page"]: record for record in records}
        for page, label in {
            46: "(9.16)",
            47: "(10.1)",
            48: "(10.7)",
            62: "(12.22)",
            65: "summary viii-x",
        }.items():
            self.assertIn(label, by_page[page]["labels_seen"])
            self.assertRegex(by_page[page]["sha256"], r"^[0-9a-f]{64}$")
            self.assertEqual(by_page[page]["manual_visual_status"], "inspected_readable")

    def test_packet_schema_and_rows_have_required_fields(self) -> None:
        schema = self.summary["packet_schema"]
        self.assertEqual(schema["id"], "RenderedCriticalDisplayTranscriptionPacket_RS_V1")
        self.assertEqual(set(schema["required_fields"]), REQUIRED_PACKET_FIELDS)

        rows = self.summary["packet_rows"]
        self.assertEqual({row["page"] for row in rows}, REQUIRED_PAGES)
        self.assertEqual(len(rows), len(REQUIRED_PAGES))
        for row in rows:
            self.assertEqual(set(row), REQUIRED_PACKET_FIELDS)
            self.assertTrue(row["packet_id"].startswith("RCDT-RS-"))
            self.assertTrue(row["labels"])
            self.assertIn(row["page"], REQUIRED_PAGES)
            self.assertIs(row["accepted"], False, row)
            self.assertTrue(row["first_blocker"], row)

    def test_rs_field_ghost_map_and_identity_statuses_are_negative_or_bounded(self) -> None:
        rows = self.summary["packet_rows"]
        by_page = {row["page"]: row for row in rows}

        self.assertIn("zeta", by_page[46]["normalized_transcription_or_paraphrase"])
        self.assertIn("absent", by_page[46]["rs_parameter_or_ghost_status"])
        self.assertIn("absent_as_minus_one_map", by_page[46]["emitted_map_status"])

        self.assertIn("bosonic", by_page[47]["emitted_map_status"])
        self.assertIn("no_rs_domain_or_codomain", by_page[47]["identity_status_to_d_RS_minus_1"])

        self.assertIn("wrong_type", by_page[48]["rs_parameter_or_ghost_status"])
        self.assertIn("wrong_domain_and_codomain", by_page[48]["identity_status_to_d_RS_minus_1"])
        self.assertIn("bosonic", by_page[48]["quotient_semantics"])

        self.assertIn("present", by_page[62]["rs_field_status"])
        self.assertIn("representation_only", by_page[62]["identity_status_to_d_RS_minus_1"])

        self.assertIn("present_in_prose", by_page[65]["rs_field_status"])
        self.assertIn("summary", by_page[65]["emitted_map_status"])

    def test_zero_accepted_receipts_and_no_proof_restart(self) -> None:
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertFalse(self.summary["accepted_rendered_rs_minus_one_map"])
        self.assertFalse(self.summary["accepted_source_differential_for_d_RS_minus_1"])
        self.assertEqual(
            self.summary["identity_status_to_d_RS_minus_1"],
            "missing_in_checked_windows",
        )
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["generation_count_promotion_allowed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])
        self.assertFalse(self.summary["target_import_used"])

    def test_first_obstruction_and_constructive_next_object_are_specific(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(obstruction["field"], "source_emitted_RS_minus_one_map")
        self.assertEqual(obstruction["status"], "MISSING")
        self.assertIn("RS parameter-or-ghost", obstruction["description"])
        self.assertIn("quotient semantics", obstruction["description"])

        next_object = self.summary["constructive_next_object"]
        self.assertEqual(next_object["id"], "RSSourceMinusOneMapIdentityPacket_V1")
        required = set(next_object["must_supply"])
        self.assertIn("spinorial_or_RS_specific_parameter_or_ghost_domain", required)
        self.assertIn("displayed_map_into_RS_component_of_zeta", required)
        self.assertIn("identity_gate_such_as_delta_omega_2_o_d_RS_minus_1_equals_zero", required)
        self.assertIn("target_import_guard_log", required)

    def test_generation_and_proof_restart_promotions_are_forbidden(self) -> None:
        impact = self.summary["GU_claim_impact"]
        self.assertEqual(impact["current_status"], "live_but_source_origin_blocked")
        forbidden = set(impact["forbidden_promotions"])
        self.assertIn("RS_generation_count_proof_restart", forbidden)
        self.assertIn("page_48_delta_1_is_RS_ghost_to_field_map", forbidden)
        self.assertIn("page_62_branching_supplies_quotient_semantics", forbidden)
        self.assertIn("page_65_elliptic_complex_prose_proves_RS_minus_one_identity", forbidden)

        for pattern in FORBIDDEN_ACCEPTED_PATTERNS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                f"forbidden promotion matched: {pattern}",
            )

    def test_next_step_keeps_gate_order(self) -> None:
        next_step = self.summary["next_meaningful_step"]
        self.assertIn("spinorial/RS gauge parameter", next_step)
        self.assertIn("zeta_RS", next_step)
        self.assertIn("accepted source map plus identity gate", next_step)
        self.assertIn("do not promote generation count", next_step)


if __name__ == "__main__":
    unittest.main(verbosity=2)
