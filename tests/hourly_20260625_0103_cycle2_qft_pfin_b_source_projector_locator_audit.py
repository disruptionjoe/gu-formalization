#!/usr/bin/env python3
"""Audit the Cycle 2 P_fin^b source-projector locator artifact.

This structural audit parses the machine-readable JSON summary, requires
source locator statuses, checks forbidden import guards, refuses QFT/CHSH
promotion, and verifies the first obstruction and next constructive object.
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
    / "hourly-20260625-0103-cycle2-qft-pfin-b-source-projector-locator.md"
)

EXPECTED_HEADINGS = [
    "## 1. Verdict",
    "## 2. Direct Source Derivations",
    "## 3. Strongest Positive Result",
    "## 4. First Exact Obstruction",
    "## 5. Constructive Next Object",
    "## 6. GU Claim Impact",
    "## 7. Next Proof Step",
    "## 8. Machine-Readable JSON Summary",
]

REQUIRED_DIRECT_DERIVATIONS = {
    "Mission_A_posture_and_no_target_smuggling_guardrails",
    "five_lane_decision_grade_worker_contract",
    "Cycle1_single_mode_certificate_blocks_at_missing_P_fin_b",
    "Cycle3_validator_blocks_at_source_projector_step_4",
    "Cycle2_packet_contract_is_specified_but_uninhabited",
    "Mission_A_places_covariance_rho_AB_CHSH_downstream",
    "claim_ledger_is_provenance_template_not_formal_evidence",
    "media_claim_mining_report_supplies_no_projector_data",
    "repo_local_search_found_only_required_or_missing_projector_mentions",
}

REQUIRED_LOCATOR_SOURCES = {
    "RESEARCH-POSTURE.md": "guardrail_only",
    "process/runbooks/five-lane-frontier-run.md": "process_only",
    "explorations/hourly-20260625-0103-cycle1-qft-single-mode-source-extraction-certificate.md": "blocked_certificate",
    "explorations/hourly-cycle3-qft-source-mode-packet-validator-2026-06-25.md": "validator_only",
    "explorations/hourly-cycle2-qft-effect-typed-source-mode-packet-2026-06-25.md": "contract_only",
    "explorations/mission-a-qft-state-space-extraction-2026-06-24.md": "downstream_state_pipeline",
    "sources/claim-ledger.md": "provenance_template",
    "sources/media-claim-mining-report-v1.md": "process_report",
    "repo_local_rg_search": "locator_search",
}

REQUIRED_FORBIDDEN_IMPORTS = {
    "ordinary_Pati_Salam_labels_as_source_data",
    "identity_Gram_as_GU_derivation",
    "Bell_state_as_GU_state",
    "Pauli_controls_as_GU_observables",
    "standard_free_vacuum_as_GU_source",
    "Hadamard_or_Fock_vacuum_as_GU_source",
    "target_fitted_covariance_or_CHSH_state",
    "direct_sum_K_b_as_tensor_product_rho_AB_without_reduction_map",
    "ordinary_SM_or_Pati_Salam_labels_as_physical_Gram",
    "media_claim_as_formal_projector",
}

FORBIDDEN_POSITIVE_CLAIMS = [
    r"\bP_fin\^b is constructed\b",
    r"\bsource projector is supplied\b",
    r"\bpositive finite seed is promoted\b",
    r"\bQFT recovery is closed\b",
    r"\bQFT recovery is promoted\b",
    r"\bsource covariance is promoted\b",
    r"\brho_AB is supplied\b",
    r"\bCHSH violation is derived\b",
    r"\bBell violation is derived\b",
    r"\bmatrix positivity is established\b",
    r"\bpositivity closure is established\b",
]


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing P_fin^b source-projector locator artifact: {DOC}") from exc


def extract_summary(text: str) -> dict[str, Any]:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class PFinBSourceProjectorLocatorAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_required_sections_are_present(self) -> None:
        for heading in EXPECTED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_verdict_and_no_promotions(self) -> None:
        self.assertEqual(self.summary["artifact"], "PFinBSourceProjectorLocator_V1")
        self.assertEqual(
            self.summary["verdict"],
            "ABSENT_PROJECTOR_REPRESENTATION_LABELS_AND_CONTROL_DATA_ONLY",
        )
        self.assertEqual(self.summary["status"], "blocked")
        self.assertIs(self.summary["projector_found"], False)
        self.assertIs(self.summary["credible_extraction_rule_found"], False)
        self.assertIs(self.summary["accepted_source_projector_exists"], False)
        for key in [
            "positive_finite_seed_promoted",
            "qft_recovered",
            "covariance_promoted",
            "rho_AB_supplied",
            "chsh_promoted",
            "bell_violation_claimed",
            "positivity_closure_claimed",
        ]:
            self.assertIs(self.summary[key], False, key)
        self.assertIs(self.summary["not_a_qft_or_chsh_promotion"], True)
        for pattern in FORBIDDEN_POSITIVE_CLAIMS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                f"forbidden positive claim matched: {pattern}",
            )

    def test_target_projector_and_carrier_are_machine_readable(self) -> None:
        projector = self.summary["target_projector"]
        self.assertEqual(projector["id"], "source_projector_P_fin_b")
        self.assertEqual(projector["domain"], "F_phys^b(O)")
        self.assertEqual(projector["codomain"], "K_b")
        self.assertEqual(projector["required_provenance"], "gu-derived")
        self.assertEqual(projector["current_status"], "missing")

        carrier = self.summary["carrier"]
        self.assertEqual(carrier["formula"], "K_b=V_L direct_sum V_R")
        self.assertEqual(carrier["V_L"], "(4,2,1)")
        self.assertEqual(carrier["V_R"], "(4bar,1,2)")
        self.assertEqual(carrier["dim_C_V_L"], 8)
        self.assertEqual(carrier["dim_C_V_R"], 8)
        self.assertEqual(carrier["dim_C_K_b"], 16)
        self.assertEqual(carrier["status"], "representation_carrier_only")

    def test_direct_source_derivations_are_declared(self) -> None:
        self.assertTrue(
            REQUIRED_DIRECT_DERIVATIONS.issubset(
                set(self.summary["derived_directly_from_sources"])
            )
        )

    def test_source_locator_statuses_are_present_and_all_nonprojector(self) -> None:
        statuses = {
            entry["source"]: entry
            for entry in self.summary["source_locator_statuses"]
        }
        self.assertEqual(set(statuses), set(REQUIRED_LOCATOR_SOURCES))
        for source, expected_status in REQUIRED_LOCATOR_SOURCES.items():
            entry = statuses[source]
            self.assertEqual(entry["status"], expected_status)
            self.assertIs(entry["contains_projector"], False)
            self.assertIs(entry["contains_extraction_rule"], False)
            self.assertTrue(entry["decision"])

    def test_classification_splits_labels_controls_and_absence(self) -> None:
        classification = self.summary["classification"]
        self.assertIs(classification["current_sources_contain_projector"], False)
        self.assertIs(classification["current_sources_contain_only_representation_labels"], True)
        self.assertIs(classification["current_sources_contain_import_or_control_data"], True)
        self.assertIs(classification["current_sources_contain_credible_extraction_rule"], False)
        for basis in [
            "K_b_and_V_L_V_R_are_named_as_representation_carrier",
            "packet_and_validator_files_require_P_fin_b_but_mark_it_missing",
            "state_and_CHSH_files_are_downstream_or_control_surfaces",
            "media_files_are_provenance_or_process_not_formal_projector_data",
        ]:
            self.assertIn(basis, classification["classification_basis"])

    def test_current_supply_blocks_before_local_modes_and_matrix_positivity(self) -> None:
        supply = self.summary["current_repo_supply"]
        self.assertEqual(supply["sector_id"], "available")
        self.assertEqual(supply["carrier_K_b"], "available_as_representation_carrier_only")
        self.assertEqual(supply["representation_labels"], "available_as_labels_only")
        self.assertEqual(supply["source_projector_P_fin_b"], "missing")
        self.assertEqual(supply["credible_source_extraction_rule"], "missing")
        self.assertEqual(supply["local_mode_records"], "not_reachable_before_P_fin_b")
        self.assertEqual(supply["raw_representatives"], "not_reachable_before_P_fin_b")
        self.assertEqual(supply["H_raw"], "not_reachable_before_local_source_records")
        self.assertEqual(supply["H_phys"], "not_computable")
        self.assertEqual(supply["positivity_certificate"], "not_reachable")
        self.assertEqual(supply["CHSH"], "control_only_not_promoted")

    def test_first_obstruction_is_projector_before_modes_and_positivity(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(obstruction["id"], "source_projector_P_fin_b")
        self.assertEqual(
            obstruction["formal_name"],
            "P_fin^b_from_F_phys_b_O_to_K_b_with_gu_derived_provenance",
        )
        self.assertEqual(obstruction["current_status"], "missing")
        for blocked in [
            "exactly_16_local_mode_records",
            "raw_representatives",
            "local_support_or_local_algebra_inclusion",
            "H_raw",
            "Q_b",
            "H_phys",
            "matrix_positivity",
            "covariance",
            "rho_AB",
            "CHSH",
        ]:
            self.assertIn(blocked, obstruction["blocks_before"])
        self.assertIn(
            "without_P_fin_b_the_16_slots_are_representation_labels_not_source_mode_images",
            obstruction["why_first"],
        )

    def test_forbidden_imports_are_explicit(self) -> None:
        self.assertEqual(set(self.summary["forbidden_imports"]), REQUIRED_FORBIDDEN_IMPORTS)

    def test_constructive_next_object_is_projector_rule_not_chsh(self) -> None:
        next_object = self.summary["constructive_next_object"]
        self.assertEqual(next_object["id"], "PFinBSourceProjectorExtractionRule_V1")
        self.assertEqual(next_object["then"], "EffectTypedSourceProjectorPFinBWithLocalModeRecords_V1")
        for required in [
            "F_phys_b_O_definition_after_quotients",
            "P_fin_b_from_F_phys_b_O_to_K_b",
            "exact_map_data_or_exact_extraction_rule",
            "gu_derived_projector_provenance",
            "one_pilot_local_representative",
            "local_support_or_local_algebra_inclusion",
            "exact_image_in_K_b",
            "effect_type",
            "projection_status",
            "finality_status",
            "loss_status",
        ]:
            self.assertIn(required, next_object["must_emit"])
        for forbidden in [
            "PositiveFiniteOneParticleSeed_K_b",
            "quasifree_covariance",
            "QFT_state",
            "rho_AB",
            "CHSH_violation",
            "Bell_violation",
        ]:
            self.assertIn(forbidden, next_object["does_not_promote_by_itself"])

    def test_gu_impact_and_next_step_are_exact(self) -> None:
        self.assertEqual(
            self.summary["GU_claim_impact"],
            "QFT_finite_source_branch_open_but_blocked_at_missing_P_fin_b",
        )
        self.assertEqual(
            self.summary["next_proof_step"],
            "Build_or_refute_PFinBSourceProjectorExtractionRule_V1_before_local_mode_records_and_matrix_positivity",
        )


def audit_summary() -> dict[str, Any]:
    text = read_doc()
    summary = extract_summary(text)
    return {
        "document": str(DOC.relative_to(REPO_ROOT)),
        "verdict": summary["verdict"],
        "status": summary["status"],
        "projector_found": summary["projector_found"],
        "credible_extraction_rule_found": summary["credible_extraction_rule_found"],
        "first_exact_obstruction": summary["first_exact_obstruction"]["id"],
        "next_proof_step": summary["next_proof_step"],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Audit the P_fin^b source-projector locator artifact."
    )
    parser.add_argument("--json", action="store_true", help="Print audit summary as JSON.")
    args, _remaining = parser.parse_known_args(argv)

    if args.json:
        print(json.dumps(audit_summary(), indent=2, sort_keys=True))
        return 0

    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(PFinBSourceProjectorLocatorAudit)
    )
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
