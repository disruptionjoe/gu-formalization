#!/usr/bin/env python3
"""Audit OxfordBosonicTwoAnchorDGU01FamilyIdentityPacket_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0803-cycle1-oxford-dgu01-two-anchor-family-identity-gate.md"
)

REQUIRED_SOURCES = {
    "RESEARCH-POSTURE.md",
    "process/runbooks/five-lane-frontier-run.md",
    "explorations/hourly-20260625-0711-three-cycle-fifteen-hole-synthesis.md",
    "explorations/hourly-20260625-0711-cycle1-oxford-portal-frame-capture-execution.md",
    "explorations/hourly-20260625-0711-cycle1-dgu-bosonic-to-01-identity-rule-search.md",
    "explorations/hourly-20260625-0711-cycle2-oxford-frame-dgu-vz-family-identity-test.md",
    "literature/weinstein-ucsd-2025-04-transcript.md",
}

REQUIRED_ANCHORS = {
    "OxfordPortal_PPT_023510_Swervature": "02:35:10",
    "OxfordPortal_PPT_023612_Displasion": "02:36:12",
}

REQUIRED_MISSING_OBJECTS = {
    "source_clean_sector_rule",
    "actual_D_GU_epsilon_0_1_action_operator_EL_formula",
    "rolled_up_0_1_domain",
    "rolled_up_0_1_codomain",
    "coefficient_packet_a_b_lambda_d",
    "projectors_Q_in_Q_out_I_Q_in_P_Q_out",
    "principal_symbol_or_sufficient_first_order_data",
    "source_clean_identity_witness",
}

REQUIRED_DEMOTION_CONDITIONS = {
    "no_source_emitted_D_GU_epsilon_0_1_sector_rule",
    "no_source_emitted_actual_D_GU_epsilon_0_1_action_operator_EL_formula",
    "no_source_emitted_0_1_domain_codomain",
    "no_source_emitted_coefficient_packet_a_b_lambda_d",
    "no_source_emitted_Q_in_Q_out_import_projector_packet",
    "no_source_emitted_principal_symbol_or_first_order_data",
    "no_source_emitted_family_identity_from_either_Oxford_bosonic_anchor_to_actual_DGU_0_1",
}


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 10\. Machine-readable JSON summary\.\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing section-10 machine-readable JSON summary")
    return json.loads(match.group(1))


class OxfordDGU01TwoAnchorFamilyIdentityGateAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = DOC.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity_and_verdict(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "OxfordBosonicTwoAnchorDGU01FamilyIdentityPacket_V1",
        )
        self.assertEqual(self.summary["run_id"], "hourly-20260625-0803")
        self.assertEqual(self.summary["cycle"], 1)
        self.assertEqual(self.summary["lane"], 3)
        self.assertEqual(
            self.summary["verdict"],
            "UNDERDEFINED_BLOCKED_MISSING_SOURCE_CLEAN_TWO_ANCHOR_DGU_01_FAMILY_IDENTITY",
        )
        self.assertEqual(
            self.summary["owned_path"],
            "explorations/hourly-20260625-0803-cycle1-oxford-dgu01-two-anchor-family-identity-gate.md",
        )
        self.assertIn("underdefined / blocked", self.text)

    def test_required_sources_are_covered(self) -> None:
        sources = set(self.summary["source_surfaces_read_first"])
        self.assertEqual(sources, REQUIRED_SOURCES)
        for source in REQUIRED_SOURCES:
            self.assertIn(source, self.text)

    def test_exact_two_oxford_anchors_are_gated(self) -> None:
        rows = self.summary["oxford_anchor_results"]
        self.assertEqual(len(rows), 2)
        by_id = {row["anchor_id"]: row for row in rows}
        self.assertEqual(set(by_id), set(REQUIRED_ANCHORS))
        for anchor_id, timestamp in REQUIRED_ANCHORS.items():
            row = by_id[anchor_id]
            self.assertEqual(row["timestamp"], timestamp)
            self.assertIn(timestamp, self.text)
            self.assertIn(anchor_id, self.text)
            self.assertIn("verified_official_source_hosted_png", row["source_status"])
            self.assertEqual(row["candidate_family"], "DGU_VZ")
            self.assertFalse(row["accepted_family_identity"])
            self.assertFalse(row["accepted_for_routing"])

    def test_zero_accepted_family_identities_and_receipts(self) -> None:
        self.assertEqual(self.summary["accepted_family_identities"], [])
        self.assertEqual(self.summary["accepted_family_identity_count"], 0)
        self.assertEqual(self.summary["accepted_dgu01_receipts"], [])
        self.assertEqual(self.summary["accepted_dgu01_receipt_count"], 0)
        self.assertEqual(self.summary["accepted_for_routing"], [])
        self.assertEqual(self.summary["accepted_for_routing_count"], 0)
        self.assertIn("accepted_family_identity_count: 0", self.text)
        self.assertIn("accepted_dgu01_receipt_count: 0", self.text)

    def test_identity_fields_are_exactly_missing(self) -> None:
        fields = self.summary["identity_field_status"]
        self.assertEqual(fields["sector_rule"], "missing")
        self.assertEqual(
            fields["actual_D_GU_epsilon_0_1_action_operator_EL_formula"],
            "missing",
        )
        self.assertEqual(fields["domain"], "missing")
        self.assertEqual(fields["codomain"], "missing")
        self.assertEqual(fields["chirality_or_epsilon_convention"], "missing")
        self.assertEqual(
            fields["principal_symbol_or_sufficient_first_order_data"],
            "missing",
        )
        self.assertEqual(fields["identity_witness"], "missing")
        self.assertEqual(fields["family_identity"], "missing")

        coeffs = fields["coefficient_packet"]
        self.assertEqual(coeffs["status"], "missing")
        self.assertEqual(coeffs["a"], "missing")
        self.assertEqual(coeffs["b"], "missing")
        self.assertEqual(coeffs["lambda_d"], "missing")

        projectors = fields["projectors_import_maps"]
        self.assertEqual(projectors["status"], "missing")
        self.assertEqual(projectors["Q_in"], "missing")
        self.assertEqual(projectors["Q_out"], "missing")
        self.assertEqual(projectors["I_Q_in"], "missing")
        self.assertEqual(projectors["P_Q_out"], "missing")

    def test_no_vz_or_physics_promotion(self) -> None:
        controls = self.summary["promotion_controls"]
        self.assertFalse(controls["proof_restart_allowed"])
        self.assertFalse(controls["claim_promotion_allowed"])
        self.assertFalse(controls["vz_or_physics_promotion_allowed"])
        self.assertFalse(controls["target_import_used"])
        self.assertFalse(controls["physics_result_used_as_identity_witness"])
        self.assertTrue(controls["no_vz_promotion"])
        self.assertTrue(controls["no_dark_energy_or_three_family_promotion"])
        self.assertIn("not_next", self.summary["next_meaningful_step"])
        self.assertEqual(
            self.summary["next_meaningful_step"]["not_next"],
            "VZ_replay_or_physics_recovery_promotion",
        )

    def test_direct_derivations_do_not_include_dgu01_identity(self) -> None:
        derived = self.summary["derived_directly_from_sources"]
        self.assertTrue(derived["oxford_two_anchor_bosonic_visual_locators"])
        self.assertTrue(derived["manuscript_bosonic_action_EL_adjacency"])
        self.assertTrue(derived["manuscript_adjacent_fermionic_slash_D_omega_display"])
        self.assertTrue(derived["ucsd_bosonic_fermionic_action_context"])
        self.assertTrue(derived["ucsd_inhomogeneous_gauge_group_context"])
        self.assertTrue(derived["ucsd_rolled_up_family_language"])
        self.assertFalse(derived["source_emitted_DGU01_identity"])

    def test_positive_attempt_is_not_accepted_as_identity(self) -> None:
        attempt = self.summary["strongest_positive_construction_attempt"]
        self.assertIn("Oxford_023510_023612", attempt["route"])
        self.assertEqual(
            attempt["positive_result"],
            "coherent_source_facing_bosonic_locator_construction",
        )
        self.assertFalse(attempt["accepted_as_family_identity"])
        self.assertIn("without_identity_certificate", attempt["failure_mode"])

    def test_first_obstruction_names_required_missing_objects(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(
            obstruction["id"],
            "missing_source_clean_identity_witness_from_either_verified_Oxford_bosonic_anchor_to_actual_D_GU_epsilon_0_1_family_data",
        )
        self.assertEqual(
            obstruction["missing_object"],
            "OxfordBosonicTwoAnchorDGU01FamilyIdentityPacket_V1",
        )
        self.assertEqual(set(obstruction["missing_objects"]), REQUIRED_MISSING_OBJECTS)
        self.assertIn("accepted_DGU_01_receipt", obstruction["blocks"])
        self.assertIn("accepted_family_identity", obstruction["blocks"])
        self.assertIn("VZ_backend_replay", obstruction["blocks"])
        self.assertIn("physics_promotion", obstruction["blocks"])
        self.assertIn("proof_restart", obstruction["blocks"])

    def test_demotion_conditions_are_complete_and_scoped(self) -> None:
        self.assertEqual(
            set(self.summary["falsification_or_demotion_condition"]),
            REQUIRED_DEMOTION_CONDITIONS,
        )
        self.assertEqual(
            self.summary["demotion_candidate_if_full_source_pass_negative"],
            "NegativePrimarySourceReceiptInstance_V1:DGU_01:OXFORD_PORTAL_2013:anchors_023510_023612",
        )
        self.assertIn("scoped negative", self.text)
        self.assertNotIn("global no-go theorem", self.summary["verdict_class"])

    def test_required_deliverable_sections_present(self) -> None:
        for heading in [
            "## 1. Verdict.",
            "## 2. Specific GU claim or bridge under test.",
            "## 3. Owned output path and sources read first.",
            "## 4. What was derived directly from repo sources.",
            "## 5. Strongest positive construction attempt.",
            "## 6. First exact obstruction or missing object.",
            "## 7. Impact if closed.",
            "## 8. Falsification/demotion condition.",
            "## 9. Next meaningful computation or proof/source step.",
            "## 10. Machine-readable JSON summary.",
        ]:
            self.assertIn(heading, self.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
