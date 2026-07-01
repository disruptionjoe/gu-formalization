#!/usr/bin/env python3
"""Audit UCSDVisualSlideCaptureBatch_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0203-cycle3-ucsd-visual-slide-capture-batch.md"
)

EXPECTED_TARGETS = {
    "[00:02:05]-[00:04:08]",
    "[00:18:03]-[00:24:00]",
    "[00:34:27]-[00:36:13]",
    "[00:48:49]-[00:50:09]",
}

EXPECTED_FAMILIES = {"IG", "RS", "QFT", "DGU_VZ"}


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing UCSD visual batch artifact: {DOC}") from exc


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 9\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class UCSDVisualSlideCaptureBatchAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity(self) -> None:
        self.assertEqual(self.summary["artifact"], "UCSDVisualSlideCaptureBatch_V1")
        self.assertEqual(self.summary["version"], "2026-06-25")
        self.assertEqual(self.summary["run"], "hourly-20260625-0203")
        self.assertEqual(self.summary["cycle"], 3)
        self.assertEqual(self.summary["lane"], 3)
        identity = self.summary["artifact_identity"]
        self.assertEqual(
            identity["owned_path"],
            "explorations/hourly-20260625-0203-cycle3-ucsd-visual-slide-capture-batch.md",
        )
        self.assertEqual(
            identity["companion_audit"],
            "tests/hourly_20260625_0203_cycle3_ucsd_visual_slide_capture_batch_audit.py",
        )

    def test_includes_required_timestamp_targets(self) -> None:
        targets = {
            target["timestamp_range"] for target in self.summary["timestamp_targets"]
        }
        self.assertEqual(targets, EXPECTED_TARGETS)

    def test_accepted_receipt_count_zero(self) -> None:
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertEqual(self.summary["accepted_receipts"], [])
        self.assertIs(self.summary["capture_scope"]["visual_material_captured"], False)
        self.assertIs(self.summary["capture_scope"]["browsing_performed"], False)
        self.assertIs(self.summary["capture_scope"]["image_capture_performed"], False)

    def test_visual_only_rows_cannot_be_accepted_without_source_context(self) -> None:
        controls = self.summary["visual_receipt_acceptance_controls"]
        self.assertIs(controls["visual_only_rows_can_be_accepted"], False)
        self.assertIs(controls["candidate_receipt_requires_transcript_timebase_tie"], True)
        self.assertIs(controls["candidate_receipt_requires_stable_visual_locator"], True)
        self.assertIs(controls["candidate_receipt_requires_representation_context"], True)
        self.assertIn("source_context_tie", self.summary["row_schema_required_fields"])
        self.assertIn("visual_only", self.summary["row_schema_required_fields"])

    def test_covers_four_families(self) -> None:
        self.assertEqual(set(self.summary["families_covered"]), EXPECTED_FAMILIES)
        self.assertEqual(set(self.summary["family_query_focus"]), EXPECTED_FAMILIES)
        self.assertEqual(
            set(self.summary["required_family_objects_for_acceptance"]),
            EXPECTED_FAMILIES,
        )
        target_family_union = {
            family
            for target in self.summary["timestamp_targets"]
            for family in target["families"]
        }
        self.assertEqual(target_family_union, EXPECTED_FAMILIES)

    def test_proof_restart_disallowed(self) -> None:
        self.assertIs(self.summary["proof_restart_allowed"], False)
        self.assertIn("proof_restart_allowed", self.summary["row_schema_required_fields"])
        self.assertIn("No GU claim is promoted.", self.text)

    def test_no_claim_promotion(self) -> None:
        self.assertIs(self.summary["claim_promotion_allowed"], False)
        self.assertIs(self.summary["no_claim_promotion"], True)
        for key, value in self.summary["no_claim_promotions"].items():
            self.assertIs(value, False, key)
        forbidden = " ".join(self.summary["forbidden_promotions"])
        self.assertIn("Visual-only material is an accepted receipt", forbidden)
        self.assertIn("DGU/VZ actual D_GU^epsilon 0/1 is identified", forbidden)


if __name__ == "__main__":
    unittest.main()
