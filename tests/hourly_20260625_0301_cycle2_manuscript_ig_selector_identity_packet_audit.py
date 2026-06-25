#!/usr/bin/env python3
"""Audit AuthorManuscriptIGSelectorIdentityPacket_V1 for Cycle 2 Lane 1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0301-cycle2-manuscript-ig-selector-identity-packet.md"
)


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary")
    return json.loads(match.group(1))


class ManuscriptIGSelectorIdentityPacketAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity_and_verdict(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "AuthorManuscriptIGSelectorIdentityPacket_V1",
        )
        self.assertEqual(self.summary["run"], "hourly-20260625-0301")
        self.assertEqual(self.summary["cycle"], 2)
        self.assertEqual(self.summary["lane"], 1)
        self.assertEqual(self.summary["verdict_class"], "blocked")
        identity = self.summary["artifact_identity"]
        self.assertEqual(
            identity["owned_path"],
            "explorations/hourly-20260625-0301-cycle2-manuscript-ig-selector-identity-packet.md",
        )
        self.assertEqual(
            identity["companion_audit"],
            "tests/hourly_20260625_0301_cycle2_manuscript_ig_selector_identity_packet_audit.py",
        )

    def test_source_and_required_object(self) -> None:
        source = self.summary["source"]
        self.assertEqual(source["source_id"], "GU-MEDIA-2021-DRAFT-RELEASE")
        self.assertEqual(source["source_kind"], "author_manuscript_or_draft")
        self.assertEqual(source["page_count_observed"], 69)
        self.assertEqual(
            source["sha256"],
            "3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4",
        )
        self.assertEqual(self.summary["family"], "IG")
        self.assertEqual(
            self.summary["required_object"],
            "SourceForcedCodomainSelectorForK_IG",
        )

    def test_selector_fields_are_explicit(self) -> None:
        packet = self.summary["candidate_packet"]
        self.assertTrue(packet["candidate_is_source_emitted"])
        self.assertFalse(packet["selector_is_source_forced"])
        self.assertEqual(
            packet["selected_domain"]["value"],
            "Omega^2(Y^{7,7}, ad)",
        )
        self.assertEqual(
            packet["selected_codomain_or_target"]["value"],
            "Omega^{d-1}(Y^{7,7}, ad)",
        )
        self.assertEqual(packet["selected_domain"]["status"], "source_displayed_candidate")
        self.assertEqual(
            packet["selected_codomain_or_target"]["status"],
            "source_displayed_candidate",
        )
        self.assertFalse(packet["source_forced_selector_rule"]["present"])
        self.assertEqual(packet["source_forced_selector_rule"]["status"], "missing")

    def test_representation_bianchi_and_rival_eliminator_status(self) -> None:
        packet = self.summary["candidate_packet"]
        evidence = packet["representation_bianchi_selection_evidence"]
        self.assertTrue(evidence["present_as_intent"])
        self.assertFalse(evidence["present_as_executable_rule"])
        self.assertEqual(evidence["status"], "selector_adjacent_not_proof")
        rivals = packet["rival_eliminators"]
        self.assertEqual(rivals["status"], "missing")
        self.assertEqual(rivals["source_eliminated_rivals"], [])
        self.assertGreaterEqual(len(rivals["rival_classes_still_live"]), 4)

    def test_family_identity_and_target_import_flags(self) -> None:
        packet = self.summary["candidate_packet"]
        family_identity = packet["family_identity_to_SourceForcedCodomainSelectorForK_IG"]
        self.assertEqual(family_identity["status"], "failed_missing_witness")
        self.assertFalse(family_identity["passed"])
        screen = self.summary["target_import_screen"]
        self.assertEqual(screen["target_data_seen"], [])
        self.assertFalse(screen["target_import_detected"])
        self.assertFalse(screen["DESI_or_dark_energy_used"])
        self.assertFalse(screen["FLRW_coefficients_used"])
        self.assertFalse(screen["VZ_success_used"])
        self.assertFalse(screen["rank_or_generation_counts_used"])
        self.assertFalse(screen["QFT_targets_used"])
        self.assertTrue(screen["target_import_clean"])

    def test_accepted_receipt_count_and_proof_restart_gate(self) -> None:
        decision = self.summary["decision"]
        self.assertEqual(decision["candidate_status"], "quarantined")
        self.assertEqual(decision["selector_identity_status"], "scoped_missing")
        self.assertFalse(decision["accepted_for_routing"])
        self.assertEqual(decision["accepted_receipt_count"], 0)
        self.assertEqual(self.summary["accepted_receipts"], [])
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertEqual(self.summary["family_identity_checks_passed"], 0)
        gate = self.summary["proof_restart_gate"]
        self.assertFalse(gate["source_intake_acceptance_passed"])
        self.assertFalse(gate["family_identity_passed"])
        self.assertFalse(gate["proof_restart_allowed"])
        self.assertIn("accepted_for_routing receipt", gate["restart_blocker"])

    def test_first_obstruction_and_next_object(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(
            obstruction["id"],
            "ManuscriptRepresentationTheoryBianchiSelectorForShiab_V1",
        )
        self.assertEqual(obstruction["status"], "missing")
        self.assertEqual(obstruction["obstruction_type"], "missing_source_object")
        self.assertEqual(
            obstruction["blocks_acceptance_for"],
            "SourceForcedCodomainSelectorForK_IG",
        )
        next_object = self.summary["constructive_next_object"]
        self.assertEqual(
            next_object["id"],
            "ManuscriptRepresentationTheoryBianchiRivalEliminatorForShiab_V1",
        )
        required = set(next_object["required_fields"])
        self.assertIn("rival_eliminators", required)
        self.assertIn("family_identity_to_SourceForcedCodomainSelectorForK_IG", required)

    def test_no_claim_promotions(self) -> None:
        promotions = self.summary["no_claim_promotions"]
        for key, value in promotions.items():
            self.assertFalse(value, key)
        self.assertIn("candidate_status: quarantined", self.text)
        self.assertIn("selector_identity_status: scoped_missing", self.text)
        self.assertIn("accepted_receipt_count: 0", self.text)
        self.assertIn("proof_restart_allowed: false", self.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
