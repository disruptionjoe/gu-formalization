#!/usr/bin/env python3
"""Audit QFTPFinBSourceMiningPacket_V1.

This structural audit parses the embedded JSON summary and checks the source
projector target, acceptable evidence, local-mode prerequisites, import controls,
non-promotion rules, and source-first sequence before H_raw/Q_b/positivity.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unittest
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0103-cycle3-qft-pfin-b-source-mining-packet.md"
)

EXPECTED_HEADINGS = [
    "## 1. Verdict",
    "## 2. Direct Source Derivations",
    "## 3. Strongest Positive Packet",
    "## 4. First Exact Obstruction",
    "## 5. Constructive Next Object",
    "## 6. GU Impact",
    "## 7. Next Step",
    "## 8. Machine-Readable JSON Summary",
]

REQUIRED_DERIVATIONS = {
    "Mission_A_posture_no_compatibility_as_derivation",
    "five_lane_decision_grade_worker_contract",
    "Cycle2_QFT_locator_absent_projector_representation_labels_only",
    "Cycle2_primary_source_receipt_ledger_QFT_missing_P_fin_b",
    "media_index_source_surfaces_are_provenance_maps_not_proofs",
    "media_contributor_tasks_require_timestamped_claim_rows_and_caveats",
}

REQUIRED_LOCAL_MODE_FIELDS = {
    "sector_id",
    "source_surface_id",
    "source_locator",
    "source_text_or_formula_reference",
    "source_claim_type",
    "F_phys^b(O)_definition",
    "physical_quotient_policy",
    "gauge_constraint_ghost_null_policy",
    "source_projector_P_fin_b",
    "projector_domain",
    "projector_codomain",
    "projector_well_defined_on_physical_quotient",
    "projector_locality_statement",
    "projector_gu_derived_provenance",
    "target_import_flag_false",
    "selected_slot",
    "raw_or_physical_representative",
    "local_support_or_local_algebra_inclusion",
    "exact_image_in_K_b",
    "source_operator_section_constraint_reference",
    "effect_type",
    "projection_status",
    "finality_status",
    "loss_status",
    "rejection_or_import_control_status",
}

REQUIRED_IMPORT_CONTROLS = {
    "ordinary_Pati_Salam_representation_labels": "representation_label_only",
    "identity_Gram_or_chosen_basis_Gram": "import_control",
    "Bell_state_or_Tsirelson_state": "control_only",
    "Pauli_CHSH_observables": "control_only",
    "standard_free_Fock_or_Hadamard_vacuum": "external_qft_import",
    "target_fitted_covariance_or_density_matrix": "target_smuggling",
    "K_b_direct_sum_as_rho_AB": "category_error",
    "media_paraphrase_without_timestamp_context": "unverified_source_pointer",
    "claim_row_without_rule_or_map_data": "provenance_only",
}

SOURCE_FIRST_SEQUENCE = [
    "mine_primary_GU_source_surface",
    "extract_timestamped_or_manuscript_located_receipt",
    "classify_receipt_kind",
    "define_F_phys_b_O_after_equations_gauge_constraints_ghosts_nulls",
    "define_P_fin_b_from_F_phys_b_O_to_K_b",
    "prove_P_fin_b_gu_derived_and_well_defined_on_physical_quotient",
    "emit_one_local_mode_certificate",
    "emit_exactly_16_local_mode_records",
    "build_H_raw_from_certified_source_representatives",
    "define_removed_representatives_and_Q_b",
    "test_H_phys_equals_Q_star_H_raw_Q_for_PSD_and_nonzero_rank",
    "route_to_covariance_rho_AB_admissible_observables_CHSH",
]

FORBIDDEN_POSITIVE_CLAIMS = [
    r"\bP_fin\^b is found\b",
    r"\bone local source mode is certified\b",
    r"\bthe 16-mode packet is admitted\b",
    r"\bpositive finite one-particle seed is established\b",
    r"\bQFT recovery is promoted\b",
    r"\bcovariance or rho_AB is supplied\b",
    r"\bCHSH or Bell violation is derived from GU\b",
]


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing source-mining packet artifact: {DOC}") from exc


def extract_summary(text: str) -> dict[str, Any]:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class QFTPFinBSourceMiningPacketAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_required_sections_present(self) -> None:
        for heading in EXPECTED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_identity_and_verdict_are_blocked_not_promoted(self) -> None:
        self.assertEqual(self.summary["artifact"], "QFTPFinBSourceMiningPacket_V1")
        self.assertEqual(
            self.summary["verdict"],
            "BLOCKED_SOURCE_FIRST_PACKET_SPECIFIED_NO_PROJECTOR_RECEIPT",
        )
        self.assertEqual(self.summary["status"], "blocked")
        self.assertIs(self.summary["packet_specified"], True)
        self.assertIs(self.summary["projector_receipt_found"], False)
        self.assertIs(self.summary["credible_extraction_rule_found"], False)
        for key in [
            "positive_finite_seed_promoted",
            "qft_recovery_promoted",
            "rho_AB_supplied",
            "chsh_promoted",
            "bell_violation_claimed",
        ]:
            self.assertIs(self.summary[key], False, key)
        for promoted in [
            "P_fin_b",
            "positive_finite_one_particle_seed",
            "QFT_recovery",
            "rho_AB",
            "CHSH",
            "Bell_violation",
        ]:
            self.assertIn(promoted, self.summary["not_promoted"])

    def test_text_does_not_promote_forbidden_qft_or_chsh_claims(self) -> None:
        for pattern in FORBIDDEN_POSITIVE_CLAIMS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                f"forbidden positive claim matched: {pattern}",
            )

    def test_direct_derivations_declared(self) -> None:
        self.assertTrue(
            REQUIRED_DERIVATIONS.issubset(
                set(self.summary["derived_directly_from_sources"])
            )
        )

    def test_target_projector_and_carrier_fields(self) -> None:
        projector = self.summary["target_projector"]
        self.assertEqual(projector["id"], "source_projector_P_fin_b")
        self.assertEqual(projector["domain"], "F_phys^b(O)")
        self.assertEqual(projector["codomain"], "K_b")
        self.assertEqual(projector["required_provenance"], "gu-derived")
        self.assertEqual(projector["current_status"], "absent")
        self.assertEqual(
            set(projector["required_content"]),
            {"exact_formula", "construction_rule", "derivation_cell", "exact_map_data"},
        )

        carrier = self.summary["carrier"]
        self.assertEqual(carrier["formula"], "K_b=V_L direct_sum V_R")
        self.assertEqual(carrier["V_L"], "(4,2,1)")
        self.assertEqual(carrier["V_R"], "(4bar,1,2)")
        self.assertEqual(carrier["dim_C_K_b"], 16)
        self.assertEqual(carrier["status"], "representation_carrier_only")

    def test_acceptable_evidence_is_projector_or_negative_receipt_only(self) -> None:
        evidence = self.summary["acceptable_evidence_kinds"]
        self.assertEqual(
            set(evidence),
            {
                "primary_source_exact_formula",
                "primary_source_construction_rule",
                "repo_local_derivation_from_primary_receipt",
                "exact_map_data_with_source_provenance",
                "explicit_negative_receipt",
            },
        )
        for key, decision in evidence.items():
            if key == "explicit_negative_receipt":
                self.assertIn("keep_blocked", decision)
            else:
                self.assertIn("advance", decision)

    def test_local_mode_prerequisites_include_pfin_before_mode_data(self) -> None:
        fields = self.summary["local_mode_prerequisites"]
        self.assertTrue(REQUIRED_LOCAL_MODE_FIELDS.issubset(set(fields)))
        self.assertLess(fields.index("source_projector_P_fin_b"), fields.index("selected_slot"))
        self.assertLess(
            fields.index("projector_gu_derived_provenance"),
            fields.index("exact_image_in_K_b"),
        )

    def test_import_controls_are_explicit_and_reject_controls(self) -> None:
        self.assertEqual(self.summary["rejection_import_controls"], REQUIRED_IMPORT_CONTROLS)
        controls = self.summary["rejection_import_controls"]
        self.assertEqual(controls["Bell_state_or_Tsirelson_state"], "control_only")
        self.assertEqual(controls["Pauli_CHSH_observables"], "control_only")
        self.assertEqual(controls["target_fitted_covariance_or_density_matrix"], "target_smuggling")
        self.assertEqual(controls["ordinary_Pati_Salam_representation_labels"], "representation_label_only")

    def test_source_first_sequence_precedes_raw_quotient_and_positivity(self) -> None:
        sequence = self.summary["source_first_sequence"]
        self.assertEqual(sequence, SOURCE_FIRST_SEQUENCE)
        self.assertLess(
            sequence.index("define_P_fin_b_from_F_phys_b_O_to_K_b"),
            sequence.index("build_H_raw_from_certified_source_representatives"),
        )
        self.assertLess(
            sequence.index("build_H_raw_from_certified_source_representatives"),
            sequence.index("define_removed_representatives_and_Q_b"),
        )
        self.assertLess(
            sequence.index("define_removed_representatives_and_Q_b"),
            sequence.index("test_H_phys_equals_Q_star_H_raw_Q_for_PSD_and_nonzero_rank"),
        )
        self.assertEqual(
            sequence[-1],
            "route_to_covariance_rho_AB_admissible_observables_CHSH",
        )

    def test_downstream_objects_forbidden_as_projector_evidence(self) -> None:
        forbidden = set(self.summary["forbidden_as_evidence_for_projector"])
        for downstream in [
            "H_raw",
            "Q_b",
            "H_phys",
            "matrix_positivity",
            "covariance",
            "rho_AB",
            "CHSH_value",
            "Bell_violation",
        ]:
            self.assertIn(downstream, forbidden)

    def test_first_obstruction_blocks_before_qb_positivity_and_chsh(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(obstruction["id"], "source_projector_P_fin_b")
        self.assertEqual(
            obstruction["formal_name"],
            "P_fin^b_from_F_phys_b_O_to_K_b_with_gu_derived_provenance",
        )
        self.assertEqual(obstruction["current_status"], "absent")
        blocked = set(obstruction["blocks_before"])
        for item in [
            "exactly_16_local_mode_records",
            "H_raw",
            "Q_b",
            "H_phys",
            "matrix_positivity",
            "rho_AB",
            "admissible_CHSH_observables",
            "CHSH_value",
            "Bell_violation",
        ]:
            self.assertIn(item, blocked)

    def test_constructive_next_object_receipt_row_schema(self) -> None:
        next_object = self.summary["constructive_next_object"]
        self.assertEqual(next_object["id"], "PFinBSourceReceiptRow_V1")
        required = set(next_object["required_fields"])
        for field in [
            "source_surface_id",
            "timestamp_or_manuscript_locator",
            "receipt_kind",
            "emitted_projector_or_rule",
            "emitted_domain",
            "emitted_codomain",
            "gu_provenance_reference",
            "target_import_flag",
            "import_control_result",
            "matrix_stage_unlocked",
            "promotion_allowed",
        ]:
            self.assertIn(field, required)
        self.assertEqual(
            set(next_object["receipt_kinds_that_unlock_one_mode_if_controls_pass"]),
            {"exact_formula", "construction_rule", "derivation_cell", "exact_map_data"},
        )
        self.assertIn(
            "representation_label_only",
            next_object["receipt_kinds_that_do_not_unlock_matrix_stage"],
        )
        self.assertIn(
            "import_control",
            next_object["receipt_kinds_that_do_not_unlock_matrix_stage"],
        )

    def test_source_surfaces_prioritized_and_next_step_is_source_first(self) -> None:
        surfaces = set(self.summary["source_surfaces_prioritized"])
        self.assertIn("GU-MEDIA-2013-OXFORD", surfaces)
        self.assertIn("GU-POD-2020-PORTAL-SPECIAL", surfaces)
        self.assertIn("GU-MEDIA-2021-DRAFT-RELEASE", surfaces)
        self.assertEqual(
            self.summary["GU_impact"],
            "QFT_finite_source_branch_open_but_blocked_before_source_extraction",
        )
        self.assertEqual(
            self.summary["next_step"],
            "Run_PFinBSourceReceiptRow_V1_against_one_primary_source_surface_before_SingleModePFinBImageCertificate_V1",
        )


def audit_summary() -> dict[str, Any]:
    text = read_doc()
    summary = extract_summary(text)
    return {
        "document": str(DOC.relative_to(REPO_ROOT)),
        "artifact": summary["artifact"],
        "verdict": summary["verdict"],
        "status": summary["status"],
        "projector_receipt_found": summary["projector_receipt_found"],
        "first_exact_obstruction": summary["first_exact_obstruction"]["id"],
        "next_step": summary["next_step"],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Audit the QFT P_fin^b source-mining packet."
    )
    parser.add_argument("--json", action="store_true", help="Print audit summary as JSON.")
    args, _remaining = parser.parse_known_args(argv)

    if args.json:
        print(json.dumps(audit_summary(), indent=2, sort_keys=True))
        return 0

    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(QFTPFinBSourceMiningPacketAudit)
    )
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
