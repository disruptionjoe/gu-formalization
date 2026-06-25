#!/usr/bin/env python3
"""Audit KeatingRevealed_ShiabProjectionSheetRetrievalGate_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0502-cycle2-keating-shiab-projection-sheet-retrieval-gate.md"
)

EXPECTED_SURFACES = {
    "ThePortalGroup_KeatingRevealedTranscript",
    "PortalWiki_KeatingConversationTranscriptMirror",
    "PullThatUpJamie_GUForGRGaugeTheory",
    "YouTubeOEmbed_TzSEvmqxu48",
    "AuthorDraft2021_LocalPDF",
}


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 9\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary")
    return json.loads(match.group(1))


class KeatingShiabProjectionSheetRetrievalGateAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "KeatingRevealed_ShiabProjectionSheetRetrievalGate_V1",
        )
        self.assertEqual(self.summary["run"], "hourly-20260625-0502")
        self.assertEqual(self.summary["cycle"], 2)
        self.assertEqual(self.summary["lane"], 5)
        self.assertEqual(self.summary["verdict_class"], "blocked")
        identity = self.summary["artifact_identity"]
        self.assertEqual(
            identity["owned_path"],
            "explorations/hourly-20260625-0502-cycle2-keating-shiab-projection-sheet-retrieval-gate.md",
        )
        self.assertEqual(
            identity["companion_audit"],
            "tests/hourly_20260625_0502_cycle2_keating_shiab_projection_sheet_retrieval_gate_audit.py",
        )

    def test_required_missing_object_id_and_gate_target(self) -> None:
        self.assertEqual(
            self.summary["required_missing_object_id"],
            "KeatingRevealed_ShiabProjectionSheet_V1",
        )
        target = self.summary["retrieval_gate_target"]
        self.assertEqual(
            target["target_object"],
            "yellow-highlighted perforated-printer-paper representation-theory Shiab/projection calculation sheet",
        )
        self.assertFalse(target["target_object_located"])
        self.assertFalse(target["equivalent_visual_frame_located"])
        self.assertTrue(target["pull_that_up_jamie_asset_located"])
        self.assertTrue(target["manuscript_equivalent_formula_candidate_located"])
        self.assertFalse(target["manuscript_equivalence_proved"])

    def test_retrieval_surfaces_checked(self) -> None:
        rows = self.summary["retrieval_surfaces_checked"]
        self.assertEqual({row["surface_id"] for row in rows}, EXPECTED_SURFACES)
        for row in rows:
            with self.subTest(surface=row["surface_id"]):
                self.assertIn("source_ids", row)
                self.assertIn("locator", row)
                self.assertIn("result", row)
                self.assertFalse(row["accepted_for_routing"])

        draft = next(row for row in rows if row["surface_id"] == "AuthorDraft2021_LocalPDF")
        self.assertTrue(draft["formula_or_rule_emitted"])
        self.assertIn("pages 41-44", draft["locator"])
        self.assertEqual(len(draft["checksum_sha256"]), 64)

        pull_that_up = next(
            row for row in rows if row["surface_id"] == "PullThatUpJamie_GUForGRGaugeTheory"
        )
        self.assertEqual(pull_that_up["video_id"], "TzSEvmqxu48")
        self.assertFalse(pull_that_up["formula_or_rule_emitted"])

    def test_target_import_cleanliness(self) -> None:
        guard = self.summary["target_import_guard"]
        self.assertEqual(guard["status"], "enforced")
        self.assertEqual(guard["target_data_seen_for_quarantined_candidate"], [])
        self.assertFalse(guard["target_data_used_to_select_source_object"])
        self.assertFalse(guard["candidate_with_target_data_seen_nonempty_accepted"])
        self.assertFalse(guard["DESI_dark_energy_FLRW_rank_generation_VZ_QFT_targets_used"])
        self.assertEqual(
            guard["target_import_cleanliness"],
            "clean_but_not_sufficient_for_acceptance",
        )

    def test_receipt_counts_and_restart_are_blocked(self) -> None:
        self.assertEqual(self.summary["accepted_receipts"], [])
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertEqual(self.summary["quarantined_candidate_receipt_count"], 1)
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])

        candidate = self.summary["strongest_positive_retrieval_attempt"]
        self.assertEqual(candidate["candidate_id"], "ManuscriptShiabOperatorFormulaCandidate_V1")
        self.assertEqual(candidate["candidate_family"], "IG")
        self.assertTrue(candidate["is_primary_source_receipt_instance_candidate"])
        self.assertEqual(
            candidate["acceptance_status"],
            "quarantined_pending_source_intake_and_identity_check",
        )

    def test_first_obstruction_and_next_object(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(obstruction["id"], "KeatingRevealed_ShiabProjectionSheet_V1")
        self.assertTrue(obstruction["missing"])
        self.assertEqual(
            obstruction["missing_field"],
            "identity_complete_source_formula_or_rule",
        )
        self.assertIn("perforated-printer-paper", obstruction["description"])
        self.assertIn("representation-theory projection", obstruction["description"])

        next_object = self.summary["constructive_next_object"]
        self.assertEqual(next_object["id"], "KeatingRevealed_ShiabProjectionSheet_V1")
        self.assertTrue(next_object["minimum_next_acquisition_object"])
        self.assertIn("manuscript_equivalent_identity_proof", next_object["acceptable_forms"])
        self.assertEqual(
            next_object["fallback_test_object"],
            "ManuscriptShiabProjectionIdentityCheck_V1",
        )

    def test_no_claim_promotions_and_required_sections(self) -> None:
        for key, value in self.summary["no_claim_promotions"].items():
            self.assertFalse(value, key)

        for heading in [
            "## 1. Verdict",
            "## 2. What Was Derived Directly From Repo/Source Surfaces",
            "## 3. Strongest Positive Retrieval Attempt",
            "## 4. First Exact Obstruction or Missing Proof/Source Object",
            "## 5. Constructive Next Object That Would Remove or Test the Obstruction",
            "## 6. GU Claim Impact and Forbidden Promotions",
            "## 7. Next Meaningful Proof/Source Computation",
            "## 9. Machine-Readable JSON Summary",
        ]:
            self.assertIn(heading, self.text)

        self.assertIn("No GU claim is promoted.", self.text)
        self.assertIn("Do **not** restart IG proof work", self.text)


if __name__ == "__main__":
    unittest.main()
