#!/usr/bin/env python3
"""Audit the hourly Cycle 3 FR3-GU filtered-readout witness gate.

This is a structural audit, not a sheaf-cohomology computation. It checks that
the artifact names a GU readout, two same-final filtrations, a transient class,
and anti-absorption conditions, while forbidding any GU theorem-transport claim
unless readout sensitivity is actually instantiated.
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
    / "hourly-cycle3-fr3-gu-filtered-readout-witness-gate-2026-06-24.md"
)

EXPECTED_HEADINGS = [
    "## 1. Verdict",
    "## 2. Witness Contract Fields",
    "## 3. What Current FR3/Signed-Readout/QFT Sources Establish",
    "## 4. Strongest Positive Witness Attempt",
    "## 5. First Exact Obstruction or Missing Proof Object",
    "## 6. Park/Pursue/Close Decision for OBJ-TAF",
    "## 7. Rollback/Falsification Conditions",
    "## 8. Machine-Readable JSON Summary",
]

FORBIDDEN_TRANSPORT_CLAIMS = [
    r"\bFR3-GU filtered-readout witness passes\b",
    r"\bGU theorem transport is established\b",
    r"\bOBJ-TAF is promoted\b",
    r"\bFR3 transient implies GU generation readout change\b",
]

REQUIRED_ANTI_ABSORPTION_KEYS = {
    "not_final_H1_absorption",
    "not_rate_or_cadence",
    "not_chosen_channel_or_target_import",
    "qft_import_screen_applied",
    "readout_sensitivity_check",
}

REQUIRED_OBSTRUCTION_PROPERTIES = {
    "typed_domain_codomain",
    "same_final_object_preserved",
    "nonzero_transient_changes_R_GU",
    "source_derived_not_chosen_channel",
    "not_rate_or_cadence_restatement",
    "not_final_Cech_cohomology_only",
    "not_target_fitted",
}

REQUIRED_ROLLBACKS = {
    "missing_named_R_GU_invalid_contract",
    "missing_two_same_final_filtrations_invalid_contract",
    "missing_omega_tau_invalid_contract",
    "omega_tau_only_final_H1_absorbed_by_final_Cech",
    "rate_cadence_deadline_or_latency_absorption",
    "chosen_channel_or_measurement_fixture_import",
    "unchanged_E_GU_w_GU_e_max_implies_R_GU_invariant",
    "noncanonical_Theta_tau_target_fitting",
    "different_final_objects_fail_same_final_condition",
    "clean_source_derived_Theta_tau_with_R_GU_difference_promotes_to_pursue",
}


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing FR3-GU witness gate artifact: {DOC}") from exc


def extract_summary(text: str) -> dict[str, Any]:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class HourlyCycle3FR3GUFilteredReadoutWitnessGateAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_required_sections_are_present(self) -> None:
        for heading in EXPECTED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_verdict_parks_obj_taf_and_makes_no_transport_claim(self) -> None:
        self.assertEqual(
            self.summary["verdict"],
            "PARK_OBJ_TAF_WITNESS_NOT_INSTANTIATED",
        )
        self.assertEqual(self.summary["status"], "park")
        self.assertEqual(self.summary["obj_taf_decision"], "park")
        self.assertIs(self.summary["witness_instantiated"], False)
        self.assertIs(self.summary["readout_sensitivity_instantiated"], False)
        self.assertIs(self.summary["gu_theorem_transport_claim"], False)
        self.assertIs(self.summary["taf_changes_gu_proof_obligation"], False)
        self.assertIs(self.summary["contract_level_attempt_completed"], True)
        for pattern in FORBIDDEN_TRANSPORT_CLAIMS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                f"forbidden theorem-transport claim matched: {pattern}",
            )

    def test_contract_names_a_gu_readout_with_actual_signed_readout_domain(self) -> None:
        readout = self.summary["witness_contract"]["R_GU"]
        self.assertEqual(readout["id"], "R_GU_signed_readout_generation_count")
        self.assertEqual(readout["formal_name"], "R_w^GU-gen")
        self.assertEqual(readout["domain"], "E_GU=N_0^(V_exp)")
        self.assertEqual(readout["codomain"], "Z")
        self.assertEqual(readout["readout_value_if_independent"], 24)
        self.assertIn("named_not_coupled", readout["status"])
        self.assertIn("R_GU", self.text)
        self.assertIn("E_GU", self.text)

    def test_contract_has_two_filtrations_with_the_same_final_object(self) -> None:
        contract = self.summary["witness_contract"]
        self.assertIs(contract["same_final_object"], True)
        final_object = contract["final_object"]
        self.assertEqual(final_object["id"], "F_all_functions_S1_C")
        self.assertEqual(final_object["H1_final"], "0")
        filtrations = contract["two_filtrations"]
        self.assertEqual(len(filtrations), 2)
        self.assertEqual(
            {filtration["final_object"] for filtration in filtrations},
            {"F_all_functions_S1_C"},
        )
        by_id = {filtration["id"]: filtration for filtration in filtrations}
        self.assertEqual(
            by_id["filtration_A_FR3_transient"]["stages"],
            ["C_S1", "F_all_functions_S1_C"],
        )
        self.assertTrue(by_id["filtration_A_FR3_transient"]["has_transient_class"])
        self.assertEqual(
            by_id["filtration_B_same_final_control"]["stages"],
            ["zero_sheaf", "F_all_functions_S1_C"],
        )
        self.assertFalse(by_id["filtration_B_same_final_control"]["has_transient_class"])

    def test_contract_names_omega_tau_and_its_death_in_final_H1(self) -> None:
        omega = self.summary["witness_contract"]["omega_tau"]
        self.assertEqual(omega["id"], "omega_1")
        self.assertEqual(omega["stage"], "tau=1")
        self.assertEqual(omega["group"], "H^1(S^1,C_S1)")
        self.assertIn("nonzero", omega["value"])
        self.assertIs(omega["dies_in_final_H1"], True)
        self.assertEqual(omega["image_in_H1_final"], "0")
        self.assertIn("omega_1", self.text)

    def test_anti_absorption_is_present_but_readout_sensitivity_fails(self) -> None:
        anti = self.summary["witness_contract"]["anti_absorption"]
        self.assertTrue(REQUIRED_ANTI_ABSORPTION_KEYS.issubset(set(anti)))
        self.assertIs(anti["not_final_H1_absorption"], True)
        self.assertIs(anti["not_rate_or_cadence"], True)
        self.assertIs(anti["not_chosen_channel_or_target_import"], True)
        self.assertIs(anti["qft_import_screen_applied"], True)
        self.assertEqual(
            anti["readout_sensitivity_check"],
            "failed_missing_FilteredReadoutCoupling_GU",
        )

    def test_current_sources_separate_fr3_object_from_signed_readout_domain(self) -> None:
        sources = self.summary["current_sources_establish"]
        self.assertIn("transient_filtered_sheaf_class_exists", sources["FR3"])
        self.assertIn("domain_is_E_GU_not_FiltSh", sources["signed_readout"])
        self.assertIn("anti_import_screen", sources["qft_ledger"])
        self.assertIn("no_current_TAF_to_GU_transport", sources["cycle3_taf_gate"])
        self.assertIn("proposed_S_to_FiltSh", sources["reciprocal_bridge"])

    def test_strongest_attempt_keeps_R_GU_equal_for_both_filtrations(self) -> None:
        attempt = self.summary["strongest_positive_witness_attempt"]
        self.assertIs(attempt["final_object_fixed"], True)
        self.assertIs(attempt["filtration_difference_computed"], True)
        self.assertIs(attempt["transient_class_computed"], True)
        self.assertIs(attempt["R_GU_named"], True)
        self.assertEqual(
            attempt["required_connector"],
            "Theta_tau:H^1(X,F_tau)->Input(R_GU)",
        )
        self.assertIs(attempt["connector_supplied_by_current_sources"], False)
        self.assertEqual(attempt["result"], "conditional_schema_only")
        readout = attempt["readout_under_current_inputs"]
        self.assertEqual(readout["filtration_A"], 24)
        self.assertEqual(readout["filtration_B"], 24)
        self.assertIs(readout["different"], False)

    def test_first_obstruction_is_missing_filtered_readout_coupling(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(obstruction["id"], "FilteredReadoutCoupling_GU")
        self.assertEqual(obstruction["type"], "missing_typed_theorem_transport")
        self.assertIn("domain_mismatch", obstruction["why_first"])
        self.assertEqual(
            obstruction["missing_map"],
            "Theta_tau:H^1(X,F_tau)->Input(R_GU)",
        )
        self.assertIn("omega_tau_in_H^1(X,F_tau)", obstruction["input_side"])
        self.assertIn("evidence_state_e_in_E_GU", obstruction["output_side_options"])
        self.assertTrue(
            REQUIRED_OBSTRUCTION_PROPERTIES.issubset(
                set(obstruction["required_properties"])
            )
        )

    def test_obj_taf_decision_names_pursue_and_close_conditions(self) -> None:
        decision = self.summary["obj_taf_decision_detail"]
        self.assertEqual(decision["current_decision"], "park")
        self.assertIn(
            "source_derived_FilteredReadoutCoupling_GU_with_R_GU_difference",
            decision["pursue_condition"],
        )
        self.assertIn("without_Theta_tau", decision["close_condition"])
        for forbidden in [
            "TAF_changes_GU_theorem",
            "FR3_transient_implies_GU_generation_readout_change",
            "observer_finality_bypasses_GU_no_go",
            "chosen_channel_counts_as_theorem_transport",
        ]:
            self.assertIn(forbidden, decision["do_not_claim"])

    def test_rollback_conditions_cover_required_failure_modes(self) -> None:
        rollbacks = set(self.summary["rollback_falsification_conditions"])
        self.assertTrue(REQUIRED_ROLLBACKS.issubset(rollbacks))
        self.assertIn(
            "Bell_Pauli_identity_Gram_free_vacuum_Hadamard_Fock_CHSH_target_Stinespring_CPTP_import",
            rollbacks,
        )
        self.assertEqual(
            self.summary["next_meaningful_object"],
            "FilteredReadoutCoupling_GU",
        )


def audit_summary() -> dict[str, Any]:
    text = read_doc()
    summary = extract_summary(text)
    return {
        "document": str(DOC.relative_to(REPO_ROOT)),
        "verdict": summary["verdict"],
        "status": summary["status"],
        "obj_taf_decision": summary["obj_taf_decision"],
        "witness_instantiated": summary["witness_instantiated"],
        "readout_sensitivity_instantiated": summary["readout_sensitivity_instantiated"],
        "first_exact_obstruction": summary["first_exact_obstruction"]["id"],
        "next_meaningful_object": summary["next_meaningful_object"],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Audit the hourly Cycle 3 FR3-GU filtered-readout witness gate."
    )
    parser.add_argument("--json", action="store_true", help="Print audit summary as JSON.")
    args, _remaining = parser.parse_known_args(argv)

    if args.json:
        print(json.dumps(audit_summary(), indent=2, sort_keys=True))
        return 0

    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(
            HourlyCycle3FR3GUFilteredReadoutWitnessGateAudit
        )
    )
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
