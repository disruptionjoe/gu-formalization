#!/usr/bin/env python3
"""Audit the Cycle 1 direct RS rank-gate artifact.

This audit checks the proof contract, not the GU generation count. It enforces
that the artifact makes no positive three-generation claim, rejects target
division by 8/Ahat(K3), names the missing physical rank objects, and keeps the
rank 4/8 status machine readable. It also recomputes the closest raw complex
projector composite supported by the existing Cl(4,0) model.
"""

from __future__ import annotations

import json
from pathlib import Path
import re
import sys
import unittest

import numpy as np

from rs_clifford_projector_model import (
    euclidean_gamma_matrices,
    kernel_projector,
    matrix_rank,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = REPO_ROOT / "explorations" / "cycle1-generation-rs-rank-direct-gate-2026-06-24.md"


REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. What Existing Computation/Tests Actually Establish",
    "## 3. Direct-Rank Calculation Attempt Or Why The Physical One Is Not Yet Well-Defined",
    "## 4. Whether Rank 4, Rank 8, Neither, Or Underdefined Is Currently Justified",
    "## 5. First Exact Obstruction Or Missing Proof Object",
    "## 6. Implication For Three-Generation And Four-Generation Candidates",
    "## 7. Next Meaningful Computation",
    "## 8. Machine-Readable JSON Summary",
]


REQUIRED_TERMS = [
    "Pi_RS^phys",
    "Pi_RS^raw",
    "E_RS^eff",
    "physical_DOF_quotient_or_BRST_complex",
    "H_linear_trace_certificate",
    "source_selected_background_F_and_ch2",
    "same_operator_Y14_to_K3_or_APS_bridge",
    "INVALID_TARGET_DIVISION",
]


FORBIDDEN_POSITIVE_PATTERNS = [
    r"\bthree generations\s+(is|are)\s+derived\b",
    r"\bthree-generation candidate\s+(is|has been)\s+promoted\b",
    r"\bgeneration count\s+(is|has been)\s+derived\b",
    r"\brank_H\(E_RS\^eff\)\s*=\s*4\s+is\s+derived\b",
    r"\bind_H\(D_RS\)\s*=\s*8\s+is\s+proved\b",
]


def artifact_text() -> str:
    return ARTIFACT.read_text(encoding="utf-8")


def extract_summary(text: str) -> dict[str, object]:
    for block in re.findall(r"```json\s*(.*?)\s*```", text, re.DOTALL):
        data = json.loads(block)
        if data.get("artifact") == "CYCLE1_GENERATION_RS_RANK_DIRECT_GATE":
            return data
    raise AssertionError("Cycle 1 direct RS rank-gate summary JSON block not found")


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

    idempotent_error = float(np.max(np.abs(composite @ composite - composite)))
    hermitian_error = float(np.max(np.abs(composite - composite.conj().T)))

    return {
        "domain_dim_C": gamma_trace_full.shape[1],
        "gamma_trace_rank_C": matrix_rank(gamma_trace_full),
        "pi_raw_rank_C": matrix_rank(pi_raw),
        "e_plus_rank_C": matrix_rank(e_plus),
        "composite_rank_C": matrix_rank(composite),
        "idempotent_error": idempotent_error,
        "hermitian_error": hermitian_error,
    }


class Cycle1GenerationRSRankGateAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = artifact_text()
        cls.summary = extract_summary(cls.text)

    def test_required_deliverable_headings_are_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_required_missing_objects_are_named(self) -> None:
        for term in REQUIRED_TERMS:
            self.assertIn(term, self.text)

    def test_no_positive_three_generation_claim(self) -> None:
        for pattern in FORBIDDEN_POSITIVE_PATTERNS:
            self.assertIsNone(re.search(pattern, self.text, re.IGNORECASE))
        self.assertFalse(self.summary["positive_three_generation_claim"])
        self.assertFalse(self.summary["three_generations_derived"])
        self.assertEqual(self.summary["generation_count_claim_status"], "NOT_DERIVED")

    def test_target_division_is_rejected_machine_readably(self) -> None:
        target_division = self.summary["target_division_status"]
        self.assertTrue(target_division["forbidden"])
        self.assertEqual(
            target_division["forbidden_formula"],
            "rank_H(E_RS^eff)=ind_H(D_RS)/Ahat(K3)=8/2",
        )
        self.assertEqual(target_division["rollback_label"], "INVALID_TARGET_DIVISION")
        self.assertIn("claims_rank_4_from_8_divided_by_Ahat_K3", self.summary["rollback_conditions"])

    def test_rank_4_and_rank_8_status_is_explicit(self) -> None:
        rank_status = self.summary["rank_status"]
        self.assertEqual(rank_status["rank_4"], "NOT_JUSTIFIED")
        self.assertEqual(rank_status["rank_8"], "NOT_JUSTIFIED")
        self.assertEqual(rank_status["physical_effective_rank"], "UNDERDEFINED")
        self.assertEqual(self.summary["current_decision"], "NO_SOURCE_DERIVED_RANK_4_OR_8")

    def test_missing_objects_cover_projector_background_quotient_trace_and_bridge(self) -> None:
        missing = set(self.summary["missing_objects"])
        expected = {
            "Pi_RS^phys_or_effective_RS_projector",
            "physical_DOF_quotient_or_BRST_complex",
            "effective_coefficient_bundle_E_RS_eff",
            "H_linear_trace_certificate",
            "source_selected_background_F_and_ch2",
            "same_operator_Y14_to_K3_or_APS_bridge",
        }
        self.assertTrue(expected.issubset(missing))
        self.assertIn("Pi_RS^raw", self.summary["first_exact_obstruction"])
        self.assertIn("Pi_RS^phys", self.summary["first_exact_obstruction"])

    def test_candidate_implications_are_open_not_promoted(self) -> None:
        implications = self.summary["candidate_implications"]
        self.assertEqual(implications["candidate_A_three_generations"], "OPEN_NOT_DERIVED")
        self.assertEqual(implications["candidate_B_four_generations"], "OPEN_NOT_DERIVED")
        self.assertEqual(implications["raw_rank_96C"], "DOES_NOT_PROMOTE_EITHER_CANDIDATE")

    def test_raw_direct_projector_composite_rank_is_96_complex_not_4_or_8(self) -> None:
        raw = raw_direct_projector_rank()
        self.assertEqual(raw["domain_dim_C"], 256)
        self.assertEqual(raw["gamma_trace_rank_C"], 64)
        self.assertEqual(raw["pi_raw_rank_C"], 192)
        self.assertEqual(raw["e_plus_rank_C"], 128)
        self.assertEqual(raw["composite_rank_C"], 96)
        self.assertNotIn(raw["composite_rank_C"], {4, 8})
        self.assertLessEqual(raw["idempotent_error"], 1.0e-10)
        self.assertLessEqual(raw["hermitian_error"], 1.0e-10)
        self.assertEqual(self.summary["rank_status"]["raw_rank_C_Pi_raw_E_plus_Pi_raw"], 96)
        self.assertEqual(self.summary["rank_status"]["raw_naive_rank_H_if_halvable"], 48)


def main() -> int:
    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(Cycle1GenerationRSRankGateAuditTests)
    )
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
