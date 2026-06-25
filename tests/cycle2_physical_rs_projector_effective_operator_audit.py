#!/usr/bin/env python3
"""Audit the Cycle 2 physical RS/effective-operator certificate artifact.

This audit checks the contract around the physical RS projector, not the GU
generation count. It enforces that the artifact does not make a positive
three-generation claim, does not promote the raw complex rank 96, names the
required physical/effective certificate fields, and emits machine-readable
verdict and rollback conditions.
"""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest

import numpy as np

from rs_clifford_projector_model import (
    euclidean_gamma_matrices,
    kernel_projector,
    matrix_rank,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "cycle2-physical-rs-projector-effective-operator-certificate-2026-06-24.md"
)


REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. Raw Projector Result And Why It Is Insufficient",
    "## 3. Certificate Definition For `Pi_RS^phys` And `E_RS^eff`",
    "## 4. Required Quotient/BRST, H-Trace, Background, And Bridge Data",
    "## 5. Branch Outcomes If Rank 4 Or Rank 8 Later Closes",
    "## 6. First Exact Obstruction",
    "## 7. Impact For Generation-Count Claims",
    "## 8. Next Meaningful Computation",
    "## 9. Machine-Readable JSON Summary",
]

REQUIRED_TEXT_TERMS = [
    "Pi_RS^phys",
    "E_RS^eff",
    "quotient/BRST",
    "H-linear trace",
    "F/ch2",
    "K3/Y14",
    "same-operator",
    "INVALID_TARGET_DIVISION",
]

REQUIRED_CERTIFICATE_FIELDS = {
    "source_operator",
    "common_right_H_module",
    "Pi_RS_phys",
    "E_RS_eff",
    "quotient_or_BRST",
    "H_linear_trace",
    "F_ch2_background",
    "K3_Y14_same_operator_bridge",
}

REQUIRED_ROLLBACK_CONDITIONS = {
    "claims_three_generations_before_source_derived_RS_rank",
    "promotes_raw_rank_96C_to_effective_APS_rank",
    "claims_rank_4_from_8_divided_by_Ahat_K3",
    "claims_rank_8_without_Pi_RS_phys_and_E_RS_eff_certificate",
    "omits_quotient_or_BRST_while_claiming_physical_RS_rank",
    "converts_complex_rank_to_H_rank_without_H_linear_trace",
    "assumes_F_ch2_background_without_source_selection",
    "uses_K3_control_without_same_operator_Y14_bridge_or_APS_corrections",
}

FORBIDDEN_POSITIVE_PATTERNS = [
    r"\bthree generations\s+(is|are|were|have been|has been)\s+derived\b",
    r"\bthree-generation claim\s+(is|has been)\s+proved\b",
    r"\bgeneration count\s+(is|has been)\s+derived\b",
    r"\brank_H\(E_RS\^eff\)\s*=\s*4\s+(is|has been)\s+derived\b",
    r"\bind_H\(D_RS\)\s*=\s*8\s+(is|has been)\s+proved\b",
]


def artifact_text() -> str:
    return ARTIFACT.read_text(encoding="utf-8")


def extract_summary(text: str) -> dict[str, object]:
    for block in re.findall(r"```json\s*(.*?)\s*```", text, re.DOTALL):
        data = json.loads(block)
        if data.get("artifact") == "CYCLE2_PHYSICAL_RS_PROJECTOR_EFFECTIVE_OPERATOR_CERTIFICATE":
            return data
    raise AssertionError("Cycle 2 physical RS certificate JSON summary not found")


def raw_direct_projector_rank() -> dict[str, int | float]:
    gammas = euclidean_gamma_matrices()
    internal_rank_c = 16
    internal_identity = np.eye(internal_rank_c, dtype=complex)

    gamma_trace_blocks = [np.kron(gamma, internal_identity) for gamma in gammas]
    gamma_trace_full = np.hstack(gamma_trace_blocks)
    pi_raw = kernel_projector(gamma_trace_full)

    chirality_plus = np.diag([0, 0, 1, 1]).astype(complex)
    e_plus = np.kron(np.eye(4, dtype=complex), np.kron(chirality_plus, internal_identity))
    composite = pi_raw @ e_plus @ pi_raw

    return {
        "domain_dim_C": gamma_trace_full.shape[1],
        "gamma_trace_rank_C": matrix_rank(gamma_trace_full),
        "pi_raw_rank_C": matrix_rank(pi_raw),
        "e_plus_rank_C": matrix_rank(e_plus),
        "composite_rank_C": matrix_rank(composite),
        "idempotent_error": float(np.max(np.abs(composite @ composite - composite))),
        "hermitian_error": float(np.max(np.abs(composite - composite.conj().T))),
    }


class PhysicalRSEffectiveOperatorCertificateAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = artifact_text()
        cls.summary = extract_summary(cls.text)

    def test_required_deliverable_headings_are_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_required_certificate_terms_appear_in_plain_text(self) -> None:
        for term in REQUIRED_TEXT_TERMS:
            self.assertIn(term, self.text)

    def test_no_positive_three_generation_claim_is_made(self) -> None:
        for pattern in FORBIDDEN_POSITIVE_PATTERNS:
            self.assertIsNone(re.search(pattern, self.text, re.IGNORECASE))
        self.assertFalse(self.summary["positive_three_generation_claim"])
        self.assertFalse(self.summary["three_generations_derived"])
        self.assertFalse(self.summary["promotion_allowed_now"])
        self.assertEqual(self.summary["generation_count_claim_status"], "NOT_DERIVED")

    def test_raw_rank_96_is_recomputed_and_not_promoted(self) -> None:
        raw = raw_direct_projector_rank()
        self.assertEqual(raw["domain_dim_C"], 256)
        self.assertEqual(raw["gamma_trace_rank_C"], 64)
        self.assertEqual(raw["pi_raw_rank_C"], 192)
        self.assertEqual(raw["e_plus_rank_C"], 128)
        self.assertEqual(raw["composite_rank_C"], 96)
        self.assertLessEqual(raw["idempotent_error"], 1.0e-10)
        self.assertLessEqual(raw["hermitian_error"], 1.0e-10)

        raw_summary = self.summary["raw_projector_result"]
        self.assertEqual(raw_summary["rank"], 96)
        self.assertEqual(raw_summary["field"], "C")
        self.assertEqual(raw_summary["status"], "RAW_ONLY_NOT_EFFECTIVE_RANK")
        self.assertFalse(raw_summary["promoted_to_effective_rank"])
        self.assertFalse(raw_summary["promoted_to_generation_claim"])
        self.assertEqual(
            self.summary["rank_status"]["raw_rank_C_Pi_raw_E_plus_Pi_raw"],
            96,
        )
        self.assertEqual(self.summary["rank_status"]["physical_effective_rank"], "UNDERDEFINED")

    def test_required_physical_certificate_fields_are_machine_readable_and_missing(self) -> None:
        required = self.summary["required_certificate"]
        self.assertEqual(set(required), REQUIRED_CERTIFICATE_FIELDS)
        for field in REQUIRED_CERTIFICATE_FIELDS:
            self.assertEqual(required[field], "missing")
        self.assertEqual(
            self.summary["current_decision"],
            "NO_CURRENT_REPO_OBJECT_COMPUTES_EFFECTIVE_RS_RANK",
        )

    def test_verdict_and_rollback_conditions_are_machine_readable(self) -> None:
        self.assertEqual(self.summary["verdict"], "UNDERDEFINED_CERTIFICATE_MISSING")
        self.assertEqual(
            self.summary["rollback_label_for_target_division"],
            "INVALID_TARGET_DIVISION",
        )
        self.assertEqual(set(self.summary["rollback_conditions"]), REQUIRED_ROLLBACK_CONDITIONS)

    def test_rank_4_and_rank_8_are_not_currently_justified(self) -> None:
        rank_status = self.summary["rank_status"]
        self.assertEqual(rank_status["rank_H_E_RS_eff_4"], "NOT_JUSTIFIED")
        self.assertEqual(rank_status["rank_H_E_RS_eff_8"], "NOT_JUSTIFIED")
        outcomes = self.summary["branch_outcomes"]
        self.assertEqual(
            outcomes["if_rank_H_E_RS_eff_4_and_index_H_8_close"],
            "CANDIDATE_A_THREE_GENERATION_COMPARISON_SURVIVES_CONDITIONALLY",
        )
        self.assertEqual(
            outcomes["if_rank_H_E_RS_eff_8_and_index_H_16_close"],
            "CANDIDATE_B_FOUR_GENERATION_COMPARISON_SURVIVES_CONDITIONALLY",
        )
        self.assertEqual(outcomes["if_bridge_missing"], "K3_CONTROL_ONLY")

    def test_first_obstruction_names_common_right_h_domain_and_projectors(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertIn("common source-selected right-H", obstruction)
        self.assertIn("Pi_RS^phys", obstruction)
        self.assertIn("E_RS^eff", obstruction)
        self.assertIn("H-linear idempotents", obstruction)


def main() -> int:
    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(
            PhysicalRSEffectiveOperatorCertificateAuditTests
        )
    )
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
