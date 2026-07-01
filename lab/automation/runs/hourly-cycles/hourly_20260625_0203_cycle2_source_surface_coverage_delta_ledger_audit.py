#!/usr/bin/env python3
"""Audit SourceSurfaceCoverageDeltaLedger_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "explorations"
    / "hourly-20260625-0203-cycle2-source-surface-coverage-delta-ledger.md"
)

EXPECTED_HEADINGS = [
    "## 1. Verdict",
    "## 2. Direct Source Derivations",
    "## 3. Pre-cycle Baseline",
    "## 4. Cycle 1 Coverage Deltas By Source Surface",
    "## 5. Remaining Coverage Holes And Whether Each Is Parallel-safe Or Sequential",
    "## 6. Strongest Positive Result",
    "## 7. First Exact Obstruction",
    "## 8. GU Claim Impact And Forbidden Promotions",
    "## 9. Machine-readable JSON summary",
]

EXPECTED_SURFACES = {
    "oxford_portal",
    "ucsd_transcript",
    "jre_transcripts",
    "keating_toe_modern",
    "author_manuscript_release",
}

EXPECTED_ARTIFACTS = {
    "OxfordPortalReceiptMiningPacket_V1",
    "UCSDTranscriptReceiptMiningPacket_V1",
    "JRETranscriptReceiptMiningPacket_V1",
    "KeatingTOEModernReceiptMiningPacket_V1",
    "AuthorManuscriptReceiptAvailabilityPacket_V1",
}

REQUIRED_REMAINING_HOLES = {
    "transcript_extraction",
    "exact_locator_pass",
    "visual_slide_capture",
    "manuscript_acquisition",
    "target_import_guard",
}

REQUIRED_CYCLE3_HOLES = {
    "TranscriptExtractionBatch_V1",
    "OxfordPortalExactLocatorBatch_V1",
    "UCSDVisualSlideCaptureBatch_V1",
    "AuthorManuscriptAcquisitionRow_V1",
    "TargetImportGuardReceiptAudit_V1",
}


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 9\. Machine-readable JSON summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing SourceSurfaceCoverageDeltaLedger_V1 JSON block")
    return json.loads(match.group(1))


class SourceSurfaceCoverageDeltaLedgerAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_required_sections_present(self) -> None:
        for heading in EXPECTED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_artifact_identity(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "SourceSurfaceCoverageDeltaLedger_V1",
        )
        self.assertEqual(self.summary["run"], "hourly-20260625-0203")
        self.assertEqual(self.summary["cycle"], 2)
        self.assertEqual(self.summary["lane"], 5)
        self.assertEqual(
            self.summary["verdict"],
            "BLOCKED_SURFACE_COVERAGE_IMPROVED_ACCEPTED_RECEIPT_DELTA_ZERO",
        )
        identity = self.summary["artifact_identity"]
        self.assertEqual(
            identity["owned_path"],
            "explorations/hourly-20260625-0203-cycle2-source-surface-coverage-delta-ledger.md",
        )
        self.assertEqual(
            identity["companion_audit"],
            "tests/hourly_20260625_0203_cycle2_source_surface_coverage_delta_ledger_audit.py",
        )

    def test_baseline_is_previous_availability_ledger(self) -> None:
        baseline = self.summary["baseline"]
        self.assertEqual(baseline["artifact"], "PrimaryGUSourceReceiptAvailabilityLedger_V1")
        self.assertEqual(
            baseline["path"],
            "explorations/hourly-20260625-0103-cycle2-primary-gu-source-receipt-availability-ledger.md",
        )
        self.assertEqual(
            baseline["verdict"],
            "BLOCKED_NO_FAMILY_HAS_PRIMARY_SOURCE_RECEIPT",
        )
        self.assertEqual(
            baseline["first_missing_global_object"],
            "RepoLocalPrimaryGUSourceReceiptMap_V1",
        )
        self.assertEqual(baseline["accepted_receipt_count"], 0)

    def test_five_cycle1_surfaces_represented(self) -> None:
        surfaces = self.summary["cycle1_surfaces"]
        self.assertEqual(len(surfaces), 5)
        self.assertEqual({row["surface"] for row in surfaces}, EXPECTED_SURFACES)
        self.assertEqual({row["artifact"] for row in surfaces}, EXPECTED_ARTIFACTS)
        for row in surfaces:
            self.assertTrue(row["surface_represented_before_cycle1"], row["surface"])
            self.assertTrue(row["surface_represented_after_cycle1"], row["surface"])
            self.assertIn("representation_delta", row)
            self.assertIsInstance(row["source_ids"], list)
            self.assertGreaterEqual(len(row["source_ids"]), 1)

    def test_surface_representation_is_distinguished_from_accepted_receipts(self) -> None:
        for row in self.summary["cycle1_surfaces"]:
            self.assertTrue(row["surface_represented_after_cycle1"], row["surface"])
            self.assertFalse(row["accepted_receipt_found"], row["surface"])
            self.assertEqual(row["accepted_receipt_count"], 0, row["surface"])

        delta = self.summary["coverage_delta"]
        self.assertEqual(delta["surface_groups_represented_before_cycle1"], 5)
        self.assertEqual(delta["surface_groups_represented_after_cycle1"], 5)
        self.assertEqual(delta["surface_groups_with_protocol_shaped_cycle1_rows"], 5)
        self.assertEqual(delta["accepted_receipts_before_cycle1"], 0)
        self.assertEqual(delta["accepted_receipts_after_cycle1"], 0)
        self.assertEqual(delta["accepted_receipt_delta"], 0)
        self.assertIn("surface represented", delta["distinction"])
        self.assertIn("accepted source-emitted family receipts", delta["distinction"])

    def test_remaining_holes_include_required_quality_holes(self) -> None:
        holes = {row["id"]: row for row in self.summary["remaining_holes"]}
        self.assertEqual(set(holes), REQUIRED_REMAINING_HOLES)
        self.assertEqual(holes["transcript_extraction"]["parallelization"], "parallel_safe")
        self.assertEqual(
            holes["exact_locator_pass"]["parallelization"],
            "parallel_safe_after_capture",
        )
        self.assertEqual(
            holes["visual_slide_capture"]["parallelization"],
            "parallel_safe_with_disjoint_source_ids",
        )
        self.assertEqual(
            holes["manuscript_acquisition"]["parallelization"],
            "sequential_for_manuscript_gate",
        )
        self.assertEqual(
            holes["target_import_guard"]["parallelization"],
            "sequential_at_intake_reusable_as_audit",
        )
        for row in holes.values():
            self.assertTrue(row["blocks_accepted_receipt"])

    def test_cycle3_candidate_holes_listed(self) -> None:
        self.assertEqual(set(self.summary["cycle3_candidate_holes"]), REQUIRED_CYCLE3_HOLES)
        self.assertIn(
            "cycle 3",
            self.summary["next_decision"],
        )
        self.assertIn(
            "source capture",
            self.summary["next_decision"],
        )

    def test_no_claim_promotions_and_first_obstruction(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(
            obstruction["id"],
            "RepoLocalPrimaryGUSourceReceiptMap_V1.accepted_PrimarySourceReceiptInstance_V1",
        )
        self.assertTrue(obstruction["missing"])

        promotions = self.summary["no_claim_promotions"]
        for key, value in promotions.items():
            self.assertFalse(value, msg=f"{key} should not be promoted")
        self.assertIn("target_data_as_source_selector", self.summary["forbidden_promotions"])
        self.assertIn(
            "downstream_proof_restart_before_intake_acceptance",
            self.summary["forbidden_promotions"],
        )


if __name__ == "__main__":
    unittest.main()
