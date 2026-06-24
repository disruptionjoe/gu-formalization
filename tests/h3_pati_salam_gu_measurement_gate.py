#!/usr/bin/env python3
"""
GU-derived Pati-Salam CHSH measurement/state gate.

This script does not supply missing GU data. It audits the measurement
interface that a future GU pass must provide and enforces provenance:
control, symmetry-baseline, and ansatz states are not accepted as GU-derived
states.

Default behavior:
  - run the interface audit;
  - reject known non-GU candidates as GU evidence;
  - skip the live GU gate if the GU rho_AB/observables hooks are still pending.

Use --require-gu to turn the pending GU hooks into a failing gate.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Sequence, Tuple

from h3_pati_salam_chsh_candidate_state import (
    cpt_color_mixed_su2_phi_ansatz,
    cpt_pure_rank8_phi_ansatz,
)
from h3_pati_salam_chsh_correlator import (
    TOTAL_DIM,
    CHSHObservables,
    DensityCandidate,
    PendingGUInput,
    chsh_value,
    control_observables,
    evaluate_gu_candidate,
    maximally_entangled_control_state,
    product_control_state,
    supply_gu_admissible_observables,
    supply_gu_derived_rho_ab,
    zeros,
)


@dataclass(frozen=True)
class InterfaceRequirement:
    key: str
    repo_status: str
    gate_status: str
    evidence: str
    required_for_gu: bool = True


@dataclass(frozen=True)
class GateReport:
    interface: List[InterfaceRequirement]
    rejected_candidates: List[Tuple[str, str]]
    gu_status: str
    gu_message: str


def measurement_interface_audit() -> List[InterfaceRequirement]:
    return [
        InterfaceRequirement(
            key="zero_mode_space",
            repo_status="partial",
            gate_status="missing_finite_gu_basis",
            evidence=(
                "Repo supplies S(6,4) -> (4,2,1)+(4bar,1,2) representation "
                "data and reconstruction-grade zero-mode/index language, but no "
                "basis/covariance for the physical GU zero-mode space."
            ),
        ),
        InterfaceRequirement(
            key="inner_product",
            repo_status="partial",
            gate_status="missing_gu_finite_gram_matrix",
            evidence=(
                "The finite CHSH fixture uses the standard C^8 x C^8 inner "
                "product. GU still needs the induced L2/KK-renormalized inner "
                "product and its finite reduction."
            ),
        ),
        InterfaceRequirement(
            key="density_matrix_extraction",
            repo_status="missing",
            gate_status="missing_rho_ab",
            evidence=(
                "No GU zero-mode, propagator, two-point function, covariance, or "
                "modular state has been reduced to rho_AB in End(V_L tensor V_R)."
            ),
        ),
        InterfaceRequirement(
            key="alice_bob_factorization",
            repo_status="partial",
            gate_status="missing_direct_sum_to_two_system_map",
            evidence=(
                "The fixture defines H_A=V_L and H_B=V_R. The repo supplies the "
                "direct sum V_L+V_R, but not a GU map from that field data to a "
                "two-observer tensor-product state."
            ),
        ),
        InterfaceRequirement(
            key="admissible_observables",
            repo_status="control_only",
            gate_status="missing_measurement_postulate",
            evidence=(
                "Pauli SU(2)_L/SU(2)_R controls are executable, but the repo has "
                "not proved that those noncommuting +/-1 operators are "
                "GU-admissible physical measurements."
            ),
        ),
        InterfaceRequirement(
            key="locality_nac",
            repo_status="conditional",
            gate_status="needs_bridge_proof_for_live_gu_data",
            evidence=(
                "The fixture checks Alice/Bob matrix commutation. GU NAC is argued "
                "from null-cone propagation at reconstruction grade, conditional "
                "on the relevant VZ/Fredholm gates."
            ),
        ),
    ]


def maximally_mixed_symmetry_baseline() -> DensityCandidate:
    rho = zeros(TOTAL_DIM, TOTAL_DIM)
    weight = 1.0 / TOTAL_DIM
    for i in range(TOTAL_DIM):
        rho[i][i] = weight + 0j
    return DensityCandidate(
        name="rho_symmetry_baseline_maximally_mixed",
        matrix=rho,
        role="symmetry_baseline",
        provenance="symmetry-baseline:pati-salam-representation-only",
    )


def candidates_that_must_not_pass_as_gu() -> List[DensityCandidate]:
    return [
        maximally_mixed_symmetry_baseline(),
        maximally_entangled_control_state(),
        product_control_state(),
        cpt_color_mixed_su2_phi_ansatz(),
        cpt_pure_rank8_phi_ansatz(),
    ]


def reject_non_gu_candidates(observables: CHSHObservables) -> List[Tuple[str, str]]:
    rejected: List[Tuple[str, str]] = []
    for candidate in candidates_that_must_not_pass_as_gu():
        result = chsh_value(candidate, observables)
        try:
            evaluate_gu_candidate(candidate, observables)
        except AssertionError as exc:
            rejected.append(
                (
                    candidate.name,
                    f"rejected role={candidate.role!r} CHSH={result.value:.12f}: {exc}",
                )
            )
            continue
        raise AssertionError(f"{candidate.name} unexpectedly passed the GU-derived gate")
    return rejected


def run_live_gu_gate(require_gu: bool) -> Tuple[str, str]:
    try:
        candidate = supply_gu_derived_rho_ab()
        observables = supply_gu_admissible_observables()
    except PendingGUInput as exc:
        if require_gu:
            raise AssertionError(f"GU inputs required but missing: {exc}")
        return "SKIP_MISSING_GU_INPUTS", str(exc)

    result = evaluate_gu_candidate(candidate, observables)
    return "GU_DERIVED_STATE_FOUND", f"CHSH={result.value:.12f}"


def run_gate(require_gu: bool) -> GateReport:
    observables = control_observables()
    rejected = reject_non_gu_candidates(observables)
    gu_status, gu_message = run_live_gu_gate(require_gu=require_gu)
    return GateReport(
        interface=measurement_interface_audit(),
        rejected_candidates=rejected,
        gu_status=gu_status,
        gu_message=gu_message,
    )


def print_report(report: GateReport) -> None:
    print("=" * 72)
    print("GU-derived Pati-Salam CHSH measurement/state gate")
    print("=" * 72)
    print("Interface audit:")
    for item in report.interface:
        print(f"  {item.key}: {item.repo_status} -> {item.gate_status}")
        print(f"    {item.evidence}")
    print()
    print("Rejected non-GU candidates:")
    for name, message in report.rejected_candidates:
        print(f"  {name}: {message}")
    print()
    print(f"Live GU gate: {report.gu_status}")
    print(f"  {report.gu_message}")
    print("=" * 72)


def main(argv: Sequence[str]) -> int:
    if "--help" in argv or "-h" in argv:
        print("usage: python tests/h3_pati_salam_gu_measurement_gate.py [--require-gu]")
        return 0

    require_gu = "--require-gu" in argv
    unknown = [arg for arg in argv if arg != "--require-gu"]
    assert not unknown, f"unknown argument(s): {unknown}"

    report = run_gate(require_gu=require_gu)
    print_report(report)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(__import__("sys").argv[1:]))
    except AssertionError as exc:
        print("=" * 72)
        print(f"FAIL: {exc}")
        print("=" * 72)
        raise SystemExit(1)
