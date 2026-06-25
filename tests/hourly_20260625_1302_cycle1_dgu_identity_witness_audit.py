#!/usr/bin/env python3
"""Audit ActualDGU01IdentityWitnessSearch_V1.

This audit enforces the lane decision that bosonic, Oxford visual, UCSD hosted,
or reconstruction-grade anchors cannot be promoted into an actual
D_GU^epsilon 0/1 identity witness or VZ replay permission.
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
    / "hourly-20260625-1302-cycle1-dgu-identity-witness.md"
)

REQUIRED_FIELDS = {
    "sector",
    "domain",
    "codomain",
    "coefficient_convention",
    "epsilon_0_1_meaning",
    "Q_projector_relation",
    "principal_symbol_or_first_order_data",
    "family_identity",
    "source_locator",
}

FORBIDDEN_PROMOTIONS = {
    "actual_operator_identity_from_bosonic_or_oxford_anchors_alone",
    "accepted_certificate_fields_from_hosted_or_visual_anchors",
    "VZ_backend_replay",
    "FC_VZ_1_closed",
    "FC_VZ_4_closed",
    "VZ_evasion_established",
    "hyperbolicity_or_causality_claim",
    "dark_energy_recovery_claim",
    "three_family_recovery_claim",
    "proof_restart",
}

PROMOTION_PHRASES = [
    r"actual identity witness present:\s*true",
    r"actual operator identity from (?:bosonic|Oxford|UCSD).*accepted",
    r"accepted certificate fields?:\s*[1-9]",
    r"accepted_identity_field_count:\s*[1-9]",
    r"VZ replay allowed:\s*true",
    r"VZ evasion (?:is |has been )?(?:proved|established|closed)",
    r"FC-VZ-1 (?:is |has been )?closed",
    r"FC-VZ-4 (?:is |has been )?closed",
    r"proof restart allowed:\s*true",
]


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. Machine-readable JSON summary\.\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing section-8 machine-readable JSON summary")
    return json.loads(match.group(1))


class ActualDGU01IdentityWitnessAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = DOC.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity(self) -> None:
        self.assertEqual(self.summary["artifact"], "ActualDGU01IdentityWitnessSearch_V1")
        self.assertEqual(self.summary["run_id"], "hourly-20260625-1302")
        self.assertEqual(self.summary["cycle"], 1)
        self.assertEqual(self.summary["lane"], 3)
        self.assertEqual(
            self.summary["owned_path"],
            "explorations/hourly-20260625-1302-cycle1-dgu-identity-witness.md",
        )
        self.assertEqual(
            self.summary["companion_audit"],
            "tests/hourly_20260625_1302_cycle1_dgu_identity_witness_audit.py",
        )

    def test_required_fields_are_declared_and_unaccepted(self) -> None:
        self.assertEqual(set(self.summary["required_fields"]), REQUIRED_FIELDS)
        self.assertEqual(self.summary["required_identity_field_count"], len(REQUIRED_FIELDS))
        self.assertEqual(self.summary["accepted_fields"], [])
        self.assertEqual(self.summary["accepted_identity_field_count"], 0)
        rows = self.summary["field_matrix"]
        self.assertEqual({row["field"] for row in rows}, REQUIRED_FIELDS)
        for row in rows:
            self.assertFalse(row["accepted"], row["field"])
            self.assertIn(row["source_status"], {"missing", "adjacent_only"})
        self.assertEqual(
            {row["field"] for row in rows if row["source_status"] == "adjacent_only"},
            {"source_locator"},
        )

    def test_actual_identity_witness_is_not_promoted_from_anchors(self) -> None:
        self.assertFalse(self.summary["actual_identity_witness_present"])
        self.assertFalse(
            self.summary["actual_operator_promotion_from_bosonic_or_oxford_anchors_allowed"]
        )
        derived = self.summary["derived_directly_from_repo_sources"]
        self.assertTrue(derived["oxford_bosonic_visual_anchors_present"])
        self.assertTrue(derived["manuscript_bosonic_action_EL_and_slash_D_omega_adjacency_present"])
        self.assertTrue(derived["ucsd_rolled_up_family_context_present"])
        self.assertTrue(derived["reconstruction_grade_D_GU_notes_present"])
        self.assertFalse(derived["actual_source_clean_D_GU_epsilon_0_1_identity_witness_present"])
        attempt = self.summary["strongest_positive_result"]
        self.assertFalse(attempt["accepted_as_identity_witness"])
        self.assertIn("without_source_clean_identity_witness", attempt["failure_mode"])

    def test_certificate_and_vz_replay_are_disallowed(self) -> None:
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["vz_replay_allowed"])
        self.assertFalse(self.summary["certificate_acceptance_allowed"])
        replay = self.summary["dgu_vz_replay"]
        self.assertFalse(replay["allowed"])
        self.assertEqual(
            replay["reason"],
            "actual_identity_witness_absent_and_zero_certificate_fields_accepted",
        )
        self.assertEqual(replay["not_next"], "VZ_replay_or_physical_recovery_promotion")

    def test_obstruction_blocks_downstream_promotions(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(
            obstruction["id"],
            "missing_source_clean_actual_D_GU_epsilon_0_1_identity_witness",
        )
        self.assertEqual(obstruction["missing_object"], "ActualDGU01IdentityWitness_V1")
        for blocked in [
            "ActualDGU01OperatorCertificateInstance_V1",
            "DGU_symbol_certificate",
            "DGU_VZ_replay",
            "FC_VZ_1_closure",
            "FC_VZ_4_closure",
            "VZ_evasion_promotion",
            "physical_recovery_promotion",
            "proof_restart",
        ]:
            self.assertIn(blocked, obstruction["blocks"])

    def test_next_object_has_complete_minimum_packet(self) -> None:
        next_object = self.summary["constructive_next_object"]
        self.assertEqual(next_object["id"], "ActualDGU01IdentityWitness_V1")
        self.assertEqual(
            set(next_object["minimum_packet"]),
            {
                "source_locator_for_actual_operator_action_EL",
                "sector_rule",
                "domain",
                "codomain",
                "epsilon_0_1_meaning",
                "coefficient_convention_a_b_lambda_d",
                "Q_in_Q_out_I_Q_in_P_Q_out_or_source_equivalent",
                "sigma_1_D_GU_epsilon_or_sufficient_first_order_data",
                "family_identity_to_DGU_VZ",
                "positive_target_import_screen",
            },
        )

    def test_forbidden_promotions_are_all_true_as_guards(self) -> None:
        forbidden = self.summary["forbidden_promotions"]
        self.assertEqual(set(forbidden), FORBIDDEN_PROMOTIONS)
        for key, value in forbidden.items():
            self.assertTrue(value, key)

    def test_no_actual_operator_promotion_phrases(self) -> None:
        for pattern in PROMOTION_PHRASES:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                f"forbidden promotion phrase matched: {pattern}",
            )

    def test_required_deliverable_sections_present(self) -> None:
        for heading in [
            "## 1. Verdict: underdefined / blocked.",
            "## 2. What was derived directly from repo sources.",
            "## 3. The strongest positive result.",
            "## 4. The first exact obstruction or missing proof/source object.",
            "## 5. The constructive next object that would remove or test the obstruction.",
            "## 6. What this means for DGU/VZ replay and certificate fields.",
            "## 7. Next meaningful proof/source computation step.",
            "## 8. Machine-readable JSON summary.",
        ]:
            self.assertIn(heading, self.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
