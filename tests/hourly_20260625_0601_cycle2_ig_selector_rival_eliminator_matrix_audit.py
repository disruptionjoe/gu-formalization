#!/usr/bin/env python3
"""Audit IGSelectorRivalEliminatorMatrix_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0601-cycle2-ig-selector-rival-eliminator-matrix.md"
)

EXPECTED_MISSING_OBJECT = "ManuscriptRepresentationTheoryBianchiRivalEliminatorForShiab_V1"
EXPECTED_RIVAL_IDS = {
    "exterior_derivative",
    "scalar_divergence",
    "symmetric_derivative",
    "projected_derivative",
    "lower_order_dressed_classes",
    "displayed_shiab_codomain",
}
EXPECTED_FIRST_OBSTRUCTION = (
    "missing source-emitted representation-theory/Bianchi/projection "
    "rival-eliminator object selecting the displayed Shiab codomain and "
    "eliminating rival codomain/operator classes for "
    "SourceForcedCodomainSelectorForK_IG"
)


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing IGSelectorRivalEliminatorMatrix_V1 JSON")
    return json.loads(match.group(1))


class IGSelectorRivalEliminatorMatrixAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity_and_required_object(self) -> None:
        self.assertEqual(self.summary["artifact"], "IGSelectorRivalEliminatorMatrix_V1")
        self.assertEqual(
            self.summary["object_id"],
            "IGSelectorRivalEliminatorMatrix_V1:GU-MEDIA-2021-DRAFT-RELEASE:IG",
        )
        self.assertEqual(self.summary["run_id"], "hourly-20260625-0601")
        self.assertEqual(self.summary["cycle"], 2)
        self.assertEqual(self.summary["lane"], 1)
        self.assertEqual(self.summary["family"], "IG")
        self.assertEqual(
            self.summary["required_object"],
            "SourceForcedCodomainSelectorForK_IG",
        )
        identity = self.summary["artifact_identity"]
        self.assertEqual(
            identity["owned_path"],
            "explorations/hourly-20260625-0601-cycle2-ig-selector-rival-eliminator-matrix.md",
        )

    def test_receipt_counts_and_restart_are_closed(self) -> None:
        self.assertEqual(self.summary["accepted_receipts"], [])
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertEqual(self.summary["family_identity_checks_passed"], 0)
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])
        self.assertIn("accepted_receipt_count: 0", self.text)
        self.assertIn("proof_restart_allowed: false", self.text)

    def test_all_required_rival_classes_are_present_and_unaccepted(self) -> None:
        rivals = self.summary["rival_classes"]
        self.assertEqual({row["id"] for row in rivals}, EXPECTED_RIVAL_IDS)
        self.assertFalse(self.summary["all_rivals_eliminated_by_source"])
        for row in rivals:
            self.assertFalse(row["manuscript_eliminator_found"], row["id"])
        statuses = {row["id"]: row["status"] for row in rivals}
        self.assertEqual(statuses["displayed_shiab_codomain"], "hosted_candidate_not_selected")
        for rival_id in EXPECTED_RIVAL_IDS - {"displayed_shiab_codomain"}:
            self.assertEqual(statuses[rival_id], "survives")

    def test_exact_missing_eliminator_object(self) -> None:
        self.assertEqual(self.summary["first_exact_obstruction"], EXPECTED_FIRST_OBSTRUCTION)
        missing = self.summary["first_exact_missing_eliminator_object"]
        self.assertEqual(missing["id"], EXPECTED_MISSING_OBJECT)
        self.assertTrue(missing["missing"])
        self.assertEqual(missing["obstruction_type"], "missing_source_object")
        required = set(missing["must_provide"])
        for rival_id in [
            "exterior_derivative_eliminator",
            "scalar_divergence_eliminator",
            "symmetric_derivative_eliminator",
            "projected_derivative_eliminator",
            "lower_order_dressed_class_eliminator",
            "family_identity_to_SourceForcedCodomainSelectorForK_IG",
        ]:
            self.assertIn(rival_id, required)
        self.assertIn(EXPECTED_MISSING_OBJECT, self.text)

    def test_source_facts_and_candidate_stay_hosted_not_selected(self) -> None:
        self.assertEqual(
            self.summary["candidate_row_id"],
            "ManuscriptIGShiabCodomainCandidate_Sections5_8_9_Summary_V1",
        )
        self.assertEqual(
            self.summary["candidate_status"],
            "hosted_strong_candidate_not_selected",
        )
        self.assertEqual(
            self.summary["displayed_shiab_codomain"],
            "Omega^2(Y,ad)->Omega^{d-1}(Y,ad)",
        )
        facts = set(self.summary["source_facts"])
        self.assertIn("prior_receipt_gate_zero_accepted_receipts", facts)
        self.assertIn(
            "prior_identity_packet_missing_source_emitted_representation_theory_Bianchi_selection_rule",
            facts,
        )

    def test_impact_and_next_step_do_not_promote_physics(self) -> None:
        impact = self.summary["impact_if_closed"]
        self.assertEqual(impact["accepted_receipt_count_would_be"], 1)
        self.assertEqual(impact["family_identity_checks_passed_would_be"], 1)
        self.assertTrue(impact["proof_restart_possible_only_after_receipt_and_identity"])
        self.assertFalse(impact["downstream_physics_promoted_by_matrix_alone"])
        self.assertIn("test each rival class", self.summary["next_meaningful_step"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
