#!/usr/bin/env python3
"""Audit FiniteLocalQFTExtractionMapSpecGate_V1.

This audit parses the embedded JSON summary and checks that the artifact
attempts a source-facing finite local QFT extraction spec while keeping the
source receipt, proof restart, and downstream QFT recovery gates closed.
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
    / "hourly-20260625-0711-cycle2-qft-finite-local-extraction-spec-gate.md"
)

EXPECTED_HEADINGS = [
    "## 1. Verdict",
    "## 2. What Was Derived Directly From Repo/Manuscript Sources",
    "## 3. Strongest Positive Specification Attempt",
    "## 4. First Exact Obstruction/Missing Object",
    "## 5. Impact if Closed",
    "## 6. Falsification/Demotion Condition",
    "## 7. Next Meaningful Computation/Proof Step",
    "## 8. Machine-Readable JSON Summary",
]

REQUIRED_SPEC_FIELDS = {
    "observation_context",
    "source_space",
    "operation",
    "codomain",
    "naturality",
    "non_import_condition",
    "finite_stability_test",
}

REQUIRED_QFT_OBJECT = "P_fin^b: F_phys^b(O) -> K_b"

FORBIDDEN_PROMOTION_PATTERNS = [
    r"\bsource receipt accepted\b",
    r"\bhas an accepted source receipt\b",
    r"\bemits an accepted source receipt\b",
    r"\bproof restart allowed\b",
    r"\bfinite QFT recovery promoted\b",
    r"\bQFT recovery is promoted\b",
    r"\bCHSH is derived\b",
    r"\bBell violation is derived\b",
]


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing spec gate artifact: {DOC}") from exc


def extract_summary(text: str) -> dict[str, Any]:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class FiniteLocalQFTExtractionMapSpecGateAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_required_sections_present(self) -> None:
        for heading in EXPECTED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_identity_verdict_and_required_object(self) -> None:
        self.assertEqual(
            self.summary["artifact"], "FiniteLocalQFTExtractionMapSpecGate_V1"
        )
        self.assertEqual(
            self.summary["verdict"], "UNDERDEFINED_NOT_VALID_RECONSTRUCTION_SPEC"
        )
        self.assertEqual(self.summary["verdict_class"], "underdefined")
        self.assertEqual(self.summary["required_qft_object"], REQUIRED_QFT_OBJECT)
        self.assertTrue(self.summary["candidate_spec_attempted"])
        self.assertFalse(self.summary["valid_reconstruction_spec"])

    def test_source_receipt_and_restart_are_closed(self) -> None:
        for key in [
            "source_receipt",
            "accepted_for_routing",
            "proof_restart_allowed",
            "finite_qft_recovery_promoted",
            "claim_promotion_allowed",
            "target_import_detected",
        ]:
            self.assertIs(self.summary[key], False, key)

    def test_required_spec_fields_exist_with_statuses(self) -> None:
        spec_fields = self.summary["spec_fields"]
        self.assertEqual(set(spec_fields), REQUIRED_SPEC_FIELDS)
        self.assertEqual(
            spec_fields["observation_context"]["status"], "source_compatible_partial"
        )
        self.assertEqual(spec_fields["source_space"]["status"], "underdefined")
        self.assertEqual(spec_fields["operation"]["status"], "missing")
        self.assertEqual(
            spec_fields["codomain"]["status"],
            "representation_carrier_only_not_source_codomain",
        )
        self.assertEqual(spec_fields["naturality"]["status"], "missing")
        self.assertEqual(spec_fields["non_import_condition"]["status"], "specified")
        self.assertEqual(
            spec_fields["finite_stability_test"]["status"],
            "not_runnable_until_operation_exists",
        )

    def test_non_import_condition_blocks_downstream_qft_targets(self) -> None:
        forbidden = set(
            self.summary["spec_fields"]["non_import_condition"]["forbidden_inputs"]
        )
        for item in [
            "Gram_matrix",
            "free_or_Fock_or_Hadamard_vacuum",
            "Bell_state",
            "Pauli_observables",
            "rho_AB",
            "CHSH_value",
            "target_fit_covariance",
            "ordinary_QFT_recovery_target",
        ]:
            self.assertIn(item, forbidden)

    def test_first_obstruction_is_operation_with_source_codomain_and_naturality(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(
            obstruction["id"], "SourceDefinedFiniteLocalExtractionOperation_V1"
        )
        self.assertEqual(obstruction["required_form"], REQUIRED_QFT_OBJECT)
        self.assertTrue(obstruction["missing"])
        missing = set(obstruction["missing_components"])
        for item in [
            "source_defined_F_phys_b_O_after_physical_quotienting",
            "exact_finite_extraction_or_projector_or_quotient_rule",
            "source_defined_K_b_codomain",
            "naturality_under_pullback_restriction_gauge_observer_change_and_quotient",
            "finite_stability_test",
        ]:
            self.assertIn(item, missing)
        blocked = set(obstruction["blocks_before"])
        for downstream in ["H_raw", "Q_b", "H_phys", "rho_AB", "CHSH", "Bell_violation"]:
            self.assertIn(downstream, blocked)

    def test_positive_attempt_is_uninhabited_and_target_free(self) -> None:
        attempt = self.summary["strongest_positive_specification_attempt"]
        self.assertEqual(attempt["id"], "FiniteLocalQFTExtractionMapSpecCandidate_V1")
        self.assertEqual(attempt["classification"], "uninhabited_specification_shell")
        self.assertTrue(attempt["does_not_use_target_data"])
        self.assertIn("operation_codomain_and_naturality", attempt["why_not_valid"])
        for source_piece in [
            "Observerse_local_observation",
            "pullback_of_Y_native_fields",
            "omega_field_content",
            "H_G_gauge_action_context",
        ]:
            self.assertIn(source_piece, attempt["uses_source_machinery"])

    def test_impact_and_next_step_do_not_skip_to_recovery(self) -> None:
        impact = self.summary["impact_if_closed"]
        self.assertEqual(impact["current_branch_status"], "open_but_underdefined")
        for forbidden_unlock in ["QFT_recovery", "rho_AB", "CHSH", "Bell_violation"]:
            self.assertIn(forbidden_unlock, impact["does_not_unlock_directly"])

        next_step = self.summary["next_meaningful_computation_or_proof_step"]
        self.assertEqual(next_step["id"], "LocalPhysicalFieldQuotientAndNaturalityLemma_V1")
        for before in ["one_mode_image_certificate", "H_raw", "rho_AB", "CHSH"]:
            self.assertIn(before, next_step["required_before"])
        self.assertIn("run_finite_stability_audit", next_step["steps"])
        self.assertIn("import_control", next_step["expected_outcomes"])

    def test_falsification_and_demotion_conditions_are_present(self) -> None:
        condition = self.summary["falsification_or_demotion_condition"]
        self.assertIn("F_phys_b_O_K_b_P_fin_b_naturality", condition["falsified_by"])
        self.assertIn("imports_target_data", condition["demote_to_fail_if"])
        self.assertFalse(condition["global_no_go_promoted"])

    def test_text_avoids_forbidden_promotion_phrases(self) -> None:
        for pattern in FORBIDDEN_PROMOTION_PATTERNS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                f"forbidden promotion phrase matched: {pattern}",
            )


def audit_summary() -> dict[str, Any]:
    text = read_doc()
    summary = extract_summary(text)
    return {
        "document": str(DOC.relative_to(REPO_ROOT)),
        "artifact": summary["artifact"],
        "verdict": summary["verdict"],
        "required_qft_object": summary["required_qft_object"],
        "valid_reconstruction_spec": summary["valid_reconstruction_spec"],
        "source_receipt": summary["source_receipt"],
        "proof_restart_allowed": summary["proof_restart_allowed"],
        "first_exact_obstruction": summary["first_exact_obstruction"]["id"],
        "next_step": summary["next_meaningful_computation_or_proof_step"]["id"],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Audit the finite local QFT extraction spec gate."
    )
    parser.add_argument("--json", action="store_true", help="Print audit summary as JSON.")
    args, _remaining = parser.parse_known_args(argv)

    if args.json:
        print(json.dumps(audit_summary(), indent=2, sort_keys=True))
        return 0

    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(
            FiniteLocalQFTExtractionMapSpecGateAudit
        )
    )
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
