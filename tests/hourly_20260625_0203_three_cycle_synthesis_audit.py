#!/usr/bin/env python3
"""Audit the hourly 20260625 0203 three-cycle synthesis.

The audit verifies the closeout-level invariants for the 3-1-5-4 run: exactly
fifteen quality holes, no GU claim promotion, no accepted receipts, no proof
restart, cycle commit references, and concrete next-frontier source gates.
"""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0203-three-cycle-fifteen-hole-synthesis.md"
)

EXPECTED_FRONTIER_OBJECTS = {
    "AcquiredAuthorManuscriptObject_V1",
    "OxfordPortalExactLocatorRow_V1",
    "UCSDVisualSlideCaptureRow_V1",
    "TranscriptExtractionRow_V1",
    "PrimarySourceReceiptInstance_V1",
}


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing synthesis artifact: {DOC}") from exc


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary")
    return json.loads(match.group(1))


class ThreeCycleSynthesisAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_identity_and_verdict(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "Hourly20260625_0203_ThreeCycleFifteenHoleSynthesis_V1",
        )
        self.assertEqual(
            self.summary["verdict"],
            "FIFTEEN_QUALITY_HOLES_RUN_SOURCE_RECEIPT_GATES_NO_GU_CLAIM_PROMOTED",
        )
        self.assertIn("no GU mathematical or", self.text)
        self.assertIn("physics claim promotion", self.text)

    def test_fifteen_holes_present(self) -> None:
        self.assertEqual(self.summary["target_quality_holes"], 15)
        self.assertEqual(self.summary["actual_quality_holes"], 15)
        holes = self.summary["holes"]
        self.assertEqual(len(holes), 15)
        cycles = [hole["cycle"] for hole in holes]
        self.assertEqual(cycles.count(1), 5)
        self.assertEqual(cycles.count(2), 5)
        self.assertEqual(cycles.count(3), 5)

    def test_no_claim_promotion_or_restart(self) -> None:
        self.assertIs(self.summary["major_gu_claim_promoted"], False)
        self.assertIs(self.summary["global_no_go_promoted"], False)
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertIs(self.summary["proof_restart_allowed"], False)

    def test_cycle_commits_recorded(self) -> None:
        commits = self.summary["cycle_commits"]
        self.assertEqual(commits["cycle_1"], "9d8bb98")
        self.assertEqual(commits["cycle_2"], "992e10c")
        self.assertEqual(commits["cycle_3"], "pending_at_synthesis_write")

    def test_audit_counts_recorded(self) -> None:
        counts = self.summary["focused_audit_counts"]
        self.assertEqual(counts["cycle_1"], 38)
        self.assertEqual(counts["cycle_2"], 40)
        self.assertEqual(counts["cycle_3_lanes"], 40)

    def test_next_frontier_objects_are_source_gates(self) -> None:
        self.assertEqual(set(self.summary["next_frontier_objects"]), EXPECTED_FRONTIER_OBJECTS)
        self.assertIn("accepted receipt plus family identity check", self.text)
        self.assertIn("source execution gates", self.summary["material_change_to_next_five_goals"])

    def test_sequential_and_parallel_guidance_present(self) -> None:
        sequential = self.summary["sequential_before_proof_restart"]
        self.assertEqual(
            sequential,
            [
                "source_acquisition",
                "exact_locator_or_capture",
                "receipt_intake",
                "target_import_guard",
                "family_identity_check",
            ],
        )
        parallel = set(self.summary["parallel_safe_next_lanes"])
        self.assertIn("independent_transcript_extraction_by_source_id", parallel)
        self.assertIn("UCSD_visual_capture_by_timestamp_window", parallel)
        self.assertIn("target_import_guard_audit_hardening", parallel)


if __name__ == "__main__":
    unittest.main()
