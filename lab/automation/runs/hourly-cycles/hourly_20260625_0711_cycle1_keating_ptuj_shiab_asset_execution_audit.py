#!/usr/bin/env python3
"""Audit the 0711 Keating/Pull That Up Jamie Shiab asset execution artifact."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0711-cycle1-keating-ptuj-shiab-asset-execution.md"
)

EXPECTED_OBJECT_IDS = {
    "execution_artifact_id": "KeatingPullThatUpJamieShiabProjectionFormulaAssetPacketExecution_0711_V1",
    "target_packet_id": "KeatingPullThatUpJamieShiabProjectionFormulaAssetPacket_V1",
    "pull_that_up_jamie_asset_id": "PullThatUpJamie_GUForGRGaugeTheory_TzSEvmqxu48",
    "missing_sheet_id": "KeatingRevealed_ShiabProjectionSheet_V1",
    "manuscript_candidate_id": "ManuscriptShiabOperatorFormulaCandidate_V1",
    "manuscript_identity_check_id": "ManuscriptShiabProjectionIdentityCheck_V1",
    "next_frontier_object": "FrameLevelPullThatUpJamieTzSEvmqxu48FormulaCaptureAndManuscriptIdentityCheck_V1",
}

EXPECTED_REQUIRED_SURFACES = {
    "GU-POD-2021-KEATING-REVEALED-1",
    "GU-POD-2021-KEATING-REVEALED-2",
    "GU-MEDIA-2021-PULL-THAT-UP-JAMIE",
    "GU-MEDIA-2021-DRAFT-RELEASE",
}


def extract_json_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. Machine-readable JSON summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary")
    return json.loads(match.group(1))


class KeatingPtujShiabAssetExecutionAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_json_summary(cls.text)

    def test_identity_and_required_object_ids(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "KeatingPullThatUpJamieShiabProjectionFormulaAssetPacketExecution_0711_V1",
        )
        self.assertEqual(self.summary["run_id"], "hourly-20260625-0711")
        self.assertEqual(self.summary["cycle"], 1)
        self.assertEqual(self.summary["lane"], 2)
        self.assertEqual(self.summary["verdict_class"], "blocked")
        self.assertEqual(self.summary["target_packet"], EXPECTED_OBJECT_IDS["target_packet_id"])
        self.assertEqual(self.summary["required_object"], "SourceForcedCodomainSelectorForK_IG")
        self.assertEqual(self.summary["object_ids"], EXPECTED_OBJECT_IDS)

    def test_required_source_surfaces_are_present(self) -> None:
        self.assertEqual(
            set(self.summary["required_source_surfaces"]),
            EXPECTED_REQUIRED_SURFACES,
        )
        observed_source_ids = set()
        for surface in self.summary["source_surfaces"]:
            observed_source_ids.update(surface["source_ids"])
        self.assertTrue(EXPECTED_REQUIRED_SURFACES.issubset(observed_source_ids))
        surface_ids = {surface["surface_id"] for surface in self.summary["source_surfaces"]}
        self.assertIn("KeatingRevealedTranscriptWindow", surface_ids)
        self.assertIn("PullThatUpJamie_GUForGRGaugeTheory_TzSEvmqxu48", surface_ids)
        self.assertIn("AuthorManuscriptPages41To44", surface_ids)

    def test_receipt_counts_and_routing_are_not_accepted(self) -> None:
        receipt_state = self.summary["receipt_state"]
        self.assertEqual(receipt_state["accepted_receipt_count"], 0)
        self.assertEqual(receipt_state["accepted_for_routing_count"], 0)
        self.assertEqual(receipt_state["accepted_receipts"], [])
        self.assertFalse(receipt_state["formula_sheet_frame_captured"])
        self.assertEqual(receipt_state["family_identity_checks_passed"], 0)
        self.assertFalse(receipt_state["SourceForcedCodomainSelectorForK_IG_accepted"])
        for surface in self.summary["source_surfaces"]:
            self.assertFalse(surface["accepted_for_routing"], surface["surface_id"])
        for attempt in self.summary["retrieval_attempts"]:
            self.assertFalse(attempt["accepted_receipt"], attempt["attempt_id"])

    def test_target_import_guard_and_proof_restart_state(self) -> None:
        guard = self.summary["target_import_guard"]
        self.assertEqual(guard["target_data_seen"], [])
        self.assertTrue(guard["target_import_clean"])
        self.assertFalse(guard["target_import_clean_sufficient_for_acceptance"])
        self.assertFalse(guard["target_outcome_used_to_select_or_normalize_source_object"])
        receipt_state = self.summary["receipt_state"]
        self.assertFalse(receipt_state["proof_restart_allowed"])
        self.assertFalse(receipt_state["claim_promotion_allowed"])
        self.assertIn("proof_restart_allowed: false", self.text)

    def test_obstruction_and_next_step_fields_are_specific(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(
            obstruction["id"],
            "NoFormulaBearingFrameSheetAssetOrEquivalenceProof_0711",
        )
        self.assertIn("yt_dlp", obstruction["operational_obstruction"])
        self.assertIn(
            "KeatingRevealed_ShiabProjectionSheet_V1",
            obstruction["source_obstruction"],
        )
        self.assertIn(
            "SourceForcedCodomainSelectorForK_IG",
            obstruction["source_obstruction"],
        )
        self.assertIn(
            "legible_TzSEvmqxu48_formula_frame_sequence",
            obstruction["missing_objects"],
        )
        next_step = self.summary["next_meaningful_acquisition_or_computation_step"]
        self.assertIn("FrameLevelPullThatUpJamieTzSEvmqxu48FormulaCapture", next_step)
        self.assertIn("checksums", next_step)
        self.assertIn("manuscript pages 41-44", next_step)

    def test_forbidden_promotions_remain_false(self) -> None:
        forbidden = self.summary["forbidden_promotions"]
        self.assertTrue(forbidden)
        for key, value in forbidden.items():
            self.assertFalse(value, key)


if __name__ == "__main__":
    unittest.main()
