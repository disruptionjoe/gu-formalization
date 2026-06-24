#!/usr/bin/env python3
"""
Candidate-state audit for the Pati-Salam CHSH fixture.

This script deliberately separates "strong ansatz" states from the existing
control fixture.  It asks what the repo data can motivate from

    V_L = C^4_color tensor C^2_SU(2)_L,
    V_R = C^4_anticolor tensor C^2_SU(2)_R,

plus an assumed CPT left/right pairing.  It then computes CHSH with the
existing finite-dimensional observables and verifies that the candidates are
not accepted as GU-derived states.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
from typing import List, Sequence

from h3_pati_salam_chsh_correlator import (
    COLOR_DIM,
    QUBIT_DIM,
    TOTAL_DIM,
    DensityCandidate,
    CHSHResult,
    assert_chsh_observable_set,
    assert_close,
    assert_density_candidate,
    basis_index,
    chsh_value,
    control_observables,
    evaluate_gu_candidate,
    vector_projector,
    zeros,
)


Matrix = List[List[complex]]
Vector = List[complex]


@dataclass(frozen=True)
class CandidateAudit:
    candidate: DensityCandidate
    result: CHSHResult
    derived_gate_status: str
    verdict: str


def add_scaled_in_place(target: Matrix, scale: float, source: Matrix) -> None:
    for i in range(TOTAL_DIM):
        for j in range(TOTAL_DIM):
            target[i][j] += scale * source[i][j]


def cpt_color_mixed_su2_phi_ansatz() -> DensityCandidate:
    """Color-neutral mixed ansatz with Bell correlations only in the SU(2) factor.

    This is the strongest conservative state suggested by the representation
    data if one refuses to assume coherent superposition over color.  The color
    sector is classically CPT-paired and maximally mixed; each color block has
    a left/right SU(2) |Phi+> correlation.
    """
    rho = zeros(TOTAL_DIM, TOTAL_DIM)
    for color in range(COLOR_DIM):
        vector = [0j for _ in range(TOTAL_DIM)]
        amplitude = 1.0 / math.sqrt(QUBIT_DIM)
        for qubit in range(QUBIT_DIM):
            vector[basis_index(color, qubit, color, qubit)] = amplitude + 0j
        add_scaled_in_place(rho, 1.0 / COLOR_DIM, vector_projector(vector))

    return DensityCandidate(
        name="rho_ansatz_cpt_color_mixed_su2_phi",
        matrix=rho,
        role="ansatz",
        provenance=(
            "ansatz:pati-salam-left-right-cpt-pairing+"
            "color-classical-mixture+su2-phi-correlations"
        ),
    )


def cpt_pure_rank8_phi_ansatz() -> DensityCandidate:
    """Pure rank-8 CPT-paired Bell ansatz over color and SU(2).

    This is the generalized Bell state one obtains after adding the stronger
    assumption of coherent equal amplitudes over the full V_L/V_R basis.  It is
    intentionally labelled as an ansatz, not a GU zero-mode or two-point result.
    """
    vector: Vector = [0j for _ in range(TOTAL_DIM)]
    amplitude = 1.0 / math.sqrt(COLOR_DIM * QUBIT_DIM)
    for color in range(COLOR_DIM):
        for qubit in range(QUBIT_DIM):
            vector[basis_index(color, qubit, color, qubit)] = amplitude + 0j

    return DensityCandidate(
        name="rho_ansatz_cpt_pure_rank8_phi",
        matrix=vector_projector(vector),
        role="ansatz",
        provenance=(
            "ansatz:pati-salam-left-right-cpt-pairing+"
            "coherent-equal-amplitudes-over-color-and-su2"
        ),
    )


def assert_rejected_by_gu_gate(candidate: DensityCandidate) -> str:
    observables = control_observables()
    try:
        evaluate_gu_candidate(candidate, observables)
    except AssertionError as exc:
        return f"REJECTED_AS_GU_DERIVED: {exc}"
    raise AssertionError(f"{candidate.name} unexpectedly passed the GU-derived gate")


def audit_candidate(candidate: DensityCandidate) -> CandidateAudit:
    observables = control_observables()
    assert_chsh_observable_set(observables)
    assert_density_candidate(candidate)
    result = chsh_value(candidate, observables)
    assert_close(
        abs(result.value),
        2.0 * math.sqrt(2.0),
        f"{candidate.name} absolute CHSH",
    )
    gate_status = assert_rejected_by_gu_gate(candidate)
    return CandidateAudit(
        candidate=candidate,
        result=result,
        derived_gate_status=gate_status,
        verdict="STRONG_ANSATZ_ONLY",
    )


def run_candidate_audit() -> List[CandidateAudit]:
    return [
        audit_candidate(cpt_color_mixed_su2_phi_ansatz()),
        audit_candidate(cpt_pure_rank8_phi_ansatz()),
    ]


def print_audit(audits: Sequence[CandidateAudit]) -> None:
    print("=" * 72)
    print("Pati-Salam CHSH candidate-state audit")
    print("=" * 72)
    print("Input status: Pati-Salam representation + assumed CPT pairing")
    print("Missing input: GU zero-mode/two-point density matrix and measurement postulate")
    print()
    for audit in audits:
        result = audit.result
        print(audit.candidate.name)
        print(f"  provenance = {audit.candidate.provenance}")
        print(f"  role       = {audit.candidate.role}")
        print(f"  CHSH       = {result.value:.12f}")
        print(f"  |CHSH|     = {abs(result.value):.12f}")
        print(f"  GU gate    = {audit.derived_gate_status}")
        print(f"  verdict    = {audit.verdict}")
        print()
    print("Overall verdict: STRONG_ANSATZ_ONLY")
    print("=" * 72)


def main(argv: Sequence[str]) -> int:
    if "--help" in argv or "-h" in argv:
        print("usage: python tests/h3_pati_salam_chsh_candidate_state.py")
        return 0
    assert not argv, f"unknown argument(s): {list(argv)}"
    print_audit(run_candidate_audit())
    return 0


if __name__ == "__main__":
    raise SystemExit(main(__import__("sys").argv[1:]))
