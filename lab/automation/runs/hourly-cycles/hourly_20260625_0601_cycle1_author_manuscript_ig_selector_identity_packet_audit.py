#!/usr/bin/env python3
"""Audit AuthorManuscriptIGSelectorIdentityPacket_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0601-cycle1-author-manuscript-ig-selector-identity-packet.md"
)

EXACT_FIRST_OBSTRUCTION = (
    "missing source-emitted representation-theory/Bianchi selection rule identifying "
    "the displayed Shiab codomain with SourceForcedCodomainSelectorForK_IG"
)


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing AuthorManuscriptIGSelectorIdentityPacket_V1 JSON")
    return json.loads(match.group(1))


class AuthorManuscriptIGSelectorIdentityPacketAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity_and_verdict(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "AuthorManuscriptIGSelectorIdentityPacket_V1",
        )
        self.assertEqual(self.summary["run_id"], "hourly-20260625-0601")
        self.assertEqual(self.summary["cycle"], 1)
        self.assertEqual(self.summary["lane"], 1)
        self.assertEqual(self.summary["verdict_class"], "blocked")
        identity = self.summary["artifact_identity"]
        self.assertEqual(
            identity["artifact_id"],
            "AuthorManuscriptIGSelectorIdentityPacket_V1",
        )
        self.assertEqual(
            identity["owned_path"],
            "explorations/hourly-20260625-0601-cycle1-author-manuscript-ig-selector-identity-packet.md",
        )

    def test_source_and_required_object_are_exact(self) -> None:
        self.assertEqual(self.summary["source_id"], "GU-MEDIA-2021-DRAFT-RELEASE")
        self.assertEqual(
            self.summary["manuscript_object_id"],
            "AcquiredAuthorManuscriptObject_V1:GU-MEDIA-2021-DRAFT-RELEASE",
        )
        self.assertEqual(
            self.summary["manuscript_sha256"],
            "3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4",
        )
        self.assertEqual(self.summary["family"], "IG")
        self.assertEqual(
            self.summary["required_object"],
            "SourceForcedCodomainSelectorForK_IG",
        )

    def test_candidate_is_quarantined_not_accepted(self) -> None:
        row = self.summary["candidate_row"]
        self.assertEqual(
            row["id"],
            "ManuscriptIGShiabCodomainCandidate_Sections5_8_9_Summary_V1",
        )
        self.assertEqual(row["status"], "quarantined_strong_candidate")
        self.assertTrue(row["candidate_is_source_emitted"])
        self.assertFalse(row["selector_is_source_forced"])
        self.assertFalse(row["accepted_receipt"])
        locators = " ".join(row["candidate_locators"])
        self.assertIn("Section 5.3-5.4", locators)
        self.assertIn("Section 8", locators)
        self.assertIn("Section 9.1", locators)
        self.assertIn("Summary", locators)

    def test_receipt_counts_and_restart_gate(self) -> None:
        self.assertEqual(self.summary["accepted_receipts"], [])
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertEqual(self.summary["family_identity_checks_passed"], 0)
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])
        self.assertFalse(self.summary["global_no_go_established"])
        forbidden = self.summary["forbidden_promotions"]
        self.assertFalse(forbidden["proof_restart"])
        self.assertFalse(forbidden["K_IG_selected_by_manuscript"])

    def test_first_obstruction_is_exact(self) -> None:
        self.assertEqual(self.summary["first_exact_obstruction"], EXACT_FIRST_OBSTRUCTION)
        self.assertIn(f"first_exact_obstruction: {EXACT_FIRST_OBSTRUCTION}", self.text)
        obstruction = self.summary["first_exact_obstruction_object"]
        self.assertEqual(
            obstruction["id"],
            "ManuscriptRepresentationTheoryBianchiSelectorForShiab_V1",
        )
        self.assertTrue(obstruction["missing"])
        self.assertEqual(obstruction["obstruction_type"], "missing_source_object")
        required = set(obstruction["required_fields"])
        self.assertIn("Bianchi_identity_selection_criterion", required)
        self.assertIn("family_identity_to_SourceForcedCodomainSelectorForK_IG", required)

    def test_normalization_rejects_family_identity(self) -> None:
        normalization = self.summary[
            "normalization_against_SourceForcedCodomainSelectorForK_IG"
        ]
        self.assertEqual(
            normalization["selected_domain_status"],
            "partially_typed_as_Omega^2_Y_ad_for_displayed_Shiab_input",
        )
        self.assertEqual(
            normalization["selected_codomain_status"],
            "typed_as_Omega^{d-1}_Y_ad_for_displayed_Shiab_output",
        )
        self.assertEqual(normalization["projection_loss_behavior_status"], "missing")
        self.assertEqual(normalization["rival_eliminators_status"], "missing")
        self.assertFalse(normalization["family_identity_to_required_object"])

    def test_impact_if_closed_does_not_promote_physics(self) -> None:
        impact = self.summary["impact_if_closed"]
        self.assertEqual(impact["accepted_receipt_count_would_be"], 1)
        self.assertEqual(impact["family_identity_checks_passed_would_be"], 1)
        self.assertTrue(impact["proof_restart_possible_only_after_receipt_and_identity"])
        self.assertFalse(impact["downstream_physics_promoted_by_packet_alone"])
        self.assertIn("re-extract Section 8", self.summary["next_meaningful_step"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
