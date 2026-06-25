#!/usr/bin/env python3
"""Audit KeatingPullThatUpJamieShiabProjectionFormulaAssetPacket_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0601-cycle2-keating-shiab-projection-formula-asset-packet-spec.md"
)

EXPECTED_OBJECT_IDS = {
    "packet_id": "KeatingPullThatUpJamieShiabProjectionFormulaAssetPacket_V1",
    "missing_sheet_id": "KeatingRevealed_ShiabProjectionSheet_V1",
    "pull_that_up_jamie_asset_id": "PullThatUpJamie_GUForGRGaugeTheory_TzSEvmqxu48",
    "manuscript_candidate_id": "ManuscriptShiabOperatorFormulaCandidate_V1",
    "manuscript_identity_check_id": "ManuscriptShiabProjectionIdentityCheck_V1",
}


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing Keating/Pull That Up Jamie JSON summary")
    return json.loads(match.group(1))


class KeatingShiabProjectionFormulaAssetPacketSpecAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity_and_verdict(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "KeatingPullThatUpJamieShiabProjectionFormulaAssetPacket_V1",
        )
        self.assertEqual(self.summary["run_id"], "hourly-20260625-0601")
        self.assertEqual(self.summary["cycle"], 2)
        self.assertEqual(self.summary["verdict_class"], "blocked")
        identity = self.summary["artifact_identity"]
        self.assertEqual(
            identity["artifact_id"],
            "KeatingPullThatUpJamieShiabProjectionFormulaAssetPacket_V1",
        )
        self.assertEqual(
            identity["owned_path"],
            "explorations/hourly-20260625-0601-cycle2-keating-shiab-projection-formula-asset-packet-spec.md",
        )

    def test_keating_pull_that_up_jamie_object_ids(self) -> None:
        self.assertEqual(
            self.summary["keating_pull_that_up_jamie_object_ids"],
            EXPECTED_OBJECT_IDS,
        )
        surfaces = {row["surface_id"]: row for row in self.summary["source_surfaces"]}
        self.assertEqual(
            surfaces["PullThatUpJamie_GUForGRGaugeTheory"]["asset_id"],
            "PullThatUpJamie_GUForGRGaugeTheory_TzSEvmqxu48",
        )
        self.assertEqual(
            surfaces["PullThatUpJamie_GUForGRGaugeTheory"]["video_id"],
            "TzSEvmqxu48",
        )
        self.assertIn(
            "01:41:43-01:42:50",
            surfaces["KeatingRevealedTranscriptWindow"]["locator"],
        )

    def test_required_selector_and_identity_fields(self) -> None:
        self.assertEqual(
            self.summary["required_object"],
            "SourceForcedCodomainSelectorForK_IG",
        )
        fields = set(
            self.summary[
                "required_identity_fields_for_SourceForcedCodomainSelectorForK_IG"
            ]
        )
        for required in [
            "parent_momentum_degree",
            "principal_symbol_class",
            "projector_policy",
            "projection_loss_behavior",
            "lower_order_policy",
            "rival_eliminators",
            "family_identity_to_SourceForcedCodomainSelectorForK_IG",
        ]:
            self.assertIn(required, fields)

    def test_zero_accepted_visual_formula_receipts_and_no_restart(self) -> None:
        state = self.summary["current_receipt_state"]
        self.assertEqual(state["accepted_visual_formula_receipt_count"], 0)
        self.assertEqual(state["accepted_receipts"], [])
        self.assertEqual(state["quarantined_candidate_receipt_count"], 1)
        self.assertFalse(state["proof_restart_allowed"])
        self.assertFalse(state["claim_promotion_allowed"])
        self.assertTrue(state["family_identity_blocked"])
        self.assertEqual(state["family_identity_checks_passed"], 0)

    def test_family_identity_remains_blocked(self) -> None:
        manuscript = next(
            row
            for row in self.summary["source_surfaces"]
            if row["surface_id"] == "AuthorManuscriptPages41To44"
        )
        self.assertTrue(manuscript["formula_or_rule_emitted"])
        self.assertFalse(manuscript["identity_to_missing_sheet_proved"])
        self.assertFalse(manuscript["accepted_for_routing"])
        self.assertIn("Omega^2(Y,ad)->Omega^{d-1}(Y,ad)", manuscript["positive_content"])

        guard = self.summary["target_import_guard"]
        self.assertEqual(guard["target_data_seen"], [])
        self.assertTrue(guard["target_import_clean"])
        self.assertFalse(guard["target_import_clean_sufficient_for_acceptance"])
        self.assertFalse(guard["target_outcome_selects_source_object"])

    def test_first_obstruction_and_forbidden_promotions(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(
            obstruction["id"],
            "KeatingPullThatUpJamieShiabProjectionFormulaAssetPacket_V1",
        )
        self.assertTrue(obstruction["missing"])
        self.assertEqual(
            obstruction["obstruction_type"],
            "missing_visual_source_asset_packet",
        )
        self.assertIn("SourceForcedCodomainSelectorForK_IG", obstruction["description"])

        for key, value in self.summary["forbidden_promotions"].items():
            self.assertFalse(value, key)

    def test_required_sections_present(self) -> None:
        for heading in [
            "## 1. Verdict",
            "## 2. Source Facts Read Directly",
            "## 3. Strongest Positive Acquisition/Identity Attempt",
            "## 4. First Exact Obstruction/Missing Visual/Source Object",
            "## 5. Impact If Closed",
            "## 6. Falsification/Demotion Condition",
            "## 7. Next Meaningful Acquisition/Computation Step",
            "## 8. Machine-Readable JSON Summary",
        ]:
            self.assertIn(heading, self.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
