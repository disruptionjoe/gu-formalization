#!/usr/bin/env python3
"""Audit IGRivalEliminatorSourceIdentity_0711_Cycle1_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0711-cycle1-ig-rival-eliminator-source-identity.md"
)

EXPECTED_HASH = "3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4"
EXPECTED_REQUIRED_OBJECT = "SourceForcedCodomainSelectorForK_IG"
EXPECTED_MISSING_OBJECT = "ManuscriptRepresentationTheoryBianchiRivalEliminatorForShiab_V1"
EXPECTED_RIVAL_IDS = {
    "exterior_covariant_derivative",
    "scalar_trace_divergence_coderivative",
    "symmetric_derivative",
    "projected_derivative",
    "lower_order_dressed_class",
    "displayed_shiab_codomain",
}
EXPECTED_CANDIDATE_CLASSES = EXPECTED_RIVAL_IDS | {
    "ManuscriptIGShiabCodomainCandidate_Sections5_8_9_Summary_V1",
}


def extract_json_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary")
    return json.loads(match.group(1))


class IGRivalEliminatorSourceIdentityAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_json_summary(cls.text)

    def test_artifact_identity_and_manuscript_hash(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "IGRivalEliminatorSourceIdentity_0711_Cycle1_V1",
        )
        self.assertEqual(self.summary["run_id"], "hourly-20260625-0711")
        self.assertEqual(self.summary["cycle"], 1)
        self.assertEqual(self.summary["lane"], 3)
        self.assertEqual(self.summary["family"], "IG")
        self.assertEqual(
            self.summary["manuscript_object_id"],
            "AcquiredAuthorManuscriptObject_V1:GU-MEDIA-2021-DRAFT-RELEASE",
        )
        self.assertEqual(self.summary["manuscript_sha256"], EXPECTED_HASH)
        self.assertEqual(self.summary["manuscript_page_count_observed"], 69)
        self.assertIn(EXPECTED_HASH, self.text)

    def test_required_and_missing_objects_are_locked(self) -> None:
        self.assertEqual(self.summary["required_object"], EXPECTED_REQUIRED_OBJECT)
        self.assertEqual(self.summary["searched_missing_object"], EXPECTED_MISSING_OBJECT)
        self.assertFalse(self.summary["searched_missing_object_found"])
        obstruction = self.summary["first_exact_obstruction_object"]
        self.assertEqual(obstruction["id"], EXPECTED_MISSING_OBJECT)
        self.assertTrue(obstruction["missing"])
        self.assertEqual(obstruction["obstruction_type"], "missing_source_object")
        required_fields = set(obstruction["must_provide"])
        for required in [
            "Bianchi_identity_selection_criterion",
            "bridge_to_SourceForcedCodomainSelectorForK_IG",
            "family_identity_to_SourceForcedCodomainSelectorForK_IG",
            "lower_order_dressed_class_eliminator",
        ]:
            self.assertIn(required, required_fields)

    def test_candidate_and_rival_classes_are_present(self) -> None:
        self.assertEqual(
            self.summary["candidate_row_id"],
            "ManuscriptIGShiabCodomainCandidate_Sections5_8_9_Summary_V1",
        )
        self.assertEqual(
            self.summary["candidate_status"],
            "hosted_strong_candidate_not_selected",
        )
        self.assertEqual(
            self.summary["candidate_map"],
            "Omega^2(Y,ad)->Omega^{d-1}(Y,ad)",
        )
        self.assertEqual(set(self.summary["candidate_classes"]), EXPECTED_CANDIDATE_CLASSES)
        rivals = self.summary["rival_classes"]
        self.assertEqual({row["id"] for row in rivals}, EXPECTED_RIVAL_IDS)
        for row in rivals:
            self.assertFalse(row["source_eliminator_found"], row["id"])
        status_by_id = {row["id"]: row["status"] for row in rivals}
        self.assertEqual(
            status_by_id["displayed_shiab_codomain"],
            "hosted_candidate_not_selected",
        )
        for rival_id in EXPECTED_RIVAL_IDS - {"displayed_shiab_codomain"}:
            self.assertEqual(status_by_id[rival_id], "survives")
        self.assertFalse(self.summary["all_rivals_eliminated_by_source"])

    def test_receipt_family_identity_and_restart_stay_blocked(self) -> None:
        self.assertEqual(self.summary["accepted_receipts"], [])
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertEqual(self.summary["family_identity_status"], "failed_missing_witness")
        self.assertEqual(self.summary["family_identity_checks_passed"], 0)
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])
        self.assertFalse(self.summary["source_forced_K_IG_selection"])
        self.assertIn("proof_restart_allowed: false", self.text)

    def test_obstruction_impact_and_next_object_are_decision_grade(self) -> None:
        self.assertIn(
            "missing source-emitted representation-theory/Bianchi rival eliminator",
            self.summary["first_exact_obstruction"],
        )
        impact = self.summary["impact_if_closed"]
        self.assertEqual(impact["accepted_receipt_count_would_be"], 1)
        self.assertEqual(impact["family_identity_status_would_be"], "passed")
        self.assertTrue(impact["proof_restart_possible_only_after_receipt_and_identity"])
        self.assertFalse(impact["downstream_physics_promoted_by_packet_alone"])
        self.assertEqual(
            self.summary["next_object"],
            "PrimarySourceOrRecoveredNotes_BianchiHighestWeightShiabSelectorPacket_V1",
        )
        self.assertIn("highest-weight/Bianchi", self.summary["next_meaningful_step"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
