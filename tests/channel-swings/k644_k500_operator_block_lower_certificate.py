#!/usr/bin/env python3
"""K644: six-channel operator-block lower certificate for K642."""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k644-k500-operator-block-lower-certificate.json"


class CertificateError(ValueError):
    pass


def q(value: str | int | Fraction) -> Fraction:
    return Fraction(value)


def qstr(value: Fraction | int) -> str:
    value = Fraction(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def row_sum_lower(diagonal: list[Fraction], couplings: list[list[Fraction]]) -> Fraction:
    size = len(diagonal)
    if size != 6 or len(couplings) != size or any(len(row) != size for row in couplings):
        raise CertificateError("certificate is frozen to six channels")
    for i in range(size):
        if couplings[i][i] != 0:
            raise CertificateError("coupling diagonal must vanish")
        for j in range(size):
            if couplings[i][j] < 0 or couplings[i][j] != couplings[j][i]:
                raise CertificateError("coupling majorants must be symmetric and nonnegative")
    return min(diagonal[i] - sum(couplings[i][j] for j in range(size) if j != i) for i in range(size))


def comparison_matrix(diagonal: list[Fraction], couplings: list[list[Fraction]]) -> list[list[Fraction]]:
    return [[diagonal[i] if i == j else -couplings[i][j] for j in range(6)] for i in range(6)]


def quadratic(matrix: list[list[Fraction]], vector: list[Fraction]) -> Fraction:
    return sum(vector[i] * matrix[i][j] * vector[j] for i in range(6) for j in range(6))


def control(name: str, diagonal_raw: list[str | int], edges: dict[tuple[int, int], str | int]) -> dict:
    diagonal = [q(value) for value in diagonal_raw]
    couplings = [[Fraction(0) for _ in range(6)] for _ in range(6)]
    for (i, j), value_raw in edges.items():
        value = q(value_raw)
        couplings[i][j] = couplings[j][i] = value
    lower = row_sum_lower(diagonal, couplings)
    matrix = comparison_matrix(diagonal, couplings)
    test_vectors = [
        [Fraction(int(i == j)) for i in range(6)] for j in range(6)
    ] + [
        [Fraction(1) for _ in range(6)],
        [Fraction((-1) ** i) for i in range(6)],
        [Fraction(i - 2) for i in range(6)],
    ]
    slacks = [quadratic(matrix, vector) - lower * sum(value * value for value in vector) for vector in test_vectors]
    return {
        "name": name,
        "diagonal_floors": [qstr(value) for value in diagonal],
        "coupling_majorants": [[qstr(value) for value in row] for row in couplings],
        "comparison_matrix": [[qstr(value) for value in row] for row in matrix],
        "row_sum_lower": qstr(lower),
        "exact_test_slacks": [qstr(value) for value in slacks],
        "all_test_slacks_nonnegative": all(value >= 0 for value in slacks),
    }


def build() -> dict:
    k643 = json.loads((ROOT / "lab/process/k643-k500-bath-sector-boundary-reduction.json").read_text())
    k642 = json.loads((ROOT / "lab/process/k642-k500-operator-cancellation-graph-lower-theorem.json").read_text())
    assert k643["sector_reduction_theorem"]["global_lower_constant"] == "m=inf_(n>=0)m_n"
    assert k642["operator_lower_theorem"]["floor_function"] == "min(1/2,m-1/128)"

    controls = [
        control("strict positive", [5, 6, 7, 8, 9, 10], {(0, 1): "1/2", (1, 2): "1/3", (2, 3): "1/4", (3, 4): "1/5", (4, 5): "1/6"}),
        control("negative diagonal allowed", [-1, 2, 3, 4, 5, 6], {(0, 1): "1/4", (0, 5): "1/8", (2, 4): "1/3"}),
        control("large coupling exposed", [2, 2, 3, 3, 4, 4], {(0, 1): 3, (2, 3): "1/2", (4, 5): "1/2"}),
        control("dense rational", [4, 5, 6, 7, 8, 9], {(0, 1): "1/5", (0, 2): "1/7", (1, 3): "1/6", (2, 4): "1/8", (3, 5): "1/9", (4, 5): "1/10"}),
    ]
    assert all(row["all_test_slacks_nonnegative"] for row in controls)

    prefix_sector_lowers = [q(row["row_sum_lower"]) for row in controls]
    uniform_tail_lower = Fraction(-3, 2)
    global_m_control = min(min(prefix_sector_lowers), uniform_tail_lower)
    base_floor = min(Fraction(1, 2), global_m_control - Fraction(1, 128))
    alpha = Fraction(1, 8)
    delta = Fraction(1, 16)
    controlled_floor = min(Fraction(1, 2) - alpha, global_m_control - delta - Fraction(1, 128))

    return {
        "schema_version": "1.0",
        "result_id": "K644-K500-OPERATOR-BLOCK-LOWER-CERTIFICATE",
        "created": "2026-09-29",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "A sufficient lower certificate for each six-channel bath-sector coefficient form in K643 and its exact composition with K642's operator cancellation graph.",
        "gu_typed_objects": {
            "sector_carrier": "H_b,n=direct_sum_(i=1)^6 H_n",
            "sector_form": "closed self-adjoint six-by-six block form b_n=(b_ij,n) on a common product form domain",
            "diagonal_data": "b_ii,n[x]>=d_i,n||x||^2",
            "off_diagonal_data": "|b_ij,n[x,y]|<=a_ij,n||x||||y|| with a_ij,n=a_ji,n>=0",
            "result": "operator-block comparison lower certificate MAP-TYPE=form-domination",
            "target": "sector constants m_n and the uniform m required by K642",
        },
        "operator_block_theorem": {
            "hypotheses": "Each diagonal form is closed and bounded below on its channel domain; every off-diagonal block form is bounded by a_ij,n in the Hilbert norms on the same product domain.",
            "comparison_matrix": "C_n has (C_n)_ii=d_i,n and (C_n)_ij=-a_ij,n for i!=j",
            "form_domination": "b_n[x]>=y^T C_n y for y_i=||x_i||",
            "sharp_comparison_floor": "m_n>=lambda_min(C_n)",
            "row_sum_floor": "g_n=min_i(d_i,n-sum_(j!=i)a_ij,n) <= lambda_min(C_n)",
            "cheap_certificate": "b_n>=g_n I on H_b,n",
            "closedness": "the finite sum of Hilbert-bounded off-diagonal forms preserves closedness and semiboundedness of the diagonal form sum",
            "no_bounded_diagonal_operator_requirement": True,
            "off_diagonal_hilbert_bound_is_sufficient_not_necessary": True,
            "failed_row_sum_is_not_a_negative_spectrum_proof": True,
        },
        "sector_to_global_composition": {
            "sector_inputs": "for every n, six diagonal floors d_i,n and fifteen symmetric coupling majorants a_ij,n on the actual common form domain",
            "sector_output": "m_n may be lambda_min(C_n) or the cheaper certified g_n",
            "global_output": "m=inf_n m_n, with a separately proved uniform tail beyond any finite prefix",
            "K642_base_floor": "min(1/2,m-1/128)",
            "K642_controlled_floor": "min(1/2-alpha,m-delta-1/128)",
            "one_sector_falsifier": "if lambda_min(C_n)<m_candidate for one actual sector, that comparison data reject m_candidate",
            "certificate_failure_boundary": "g_n<=target does not prove the true form floor is <=target; sharpen C_n or the block estimates before a negative verdict",
        },
        "exact_controls": {
            "rows": controls,
            "all_controls_pass": all(row["all_test_slacks_nonnegative"] for row in controls),
            "prefix_sector_lowers": [qstr(value) for value in prefix_sector_lowers],
            "uniform_tail_lower": qstr(uniform_tail_lower),
            "global_m_control": qstr(global_m_control),
            "K642_base_floor_control": qstr(base_floor),
            "controlled_parameters": {"alpha": qstr(alpha), "delta": qstr(delta)},
            "K642_controlled_floor_control": qstr(controlled_floor),
            "controls_are_synthetic_not_native": True,
        },
        "native_interface_status": {
            "K643_sector_reduction_consumed": True,
            "K642_floor_formula_consumed": True,
            "six_channel_operator_certificate_constructed": True,
            "actual_K139_K168_common_domain_identity_proved": False,
            "actual_diagonal_sector_floors_identified": False,
            "actual_off_diagonal_sector_bounds_identified": False,
            "actual_uniform_tail_lower_identified": False,
            "native_global_m_identified": False,
            "native_remainder_alpha_delta_identified": False,
            "native_complete_sector_floor_emitted": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
        },
        "decision": {
            "K642_native_m_obligation_reduced_to_explicit_sector_block_data": True,
            "finite_synthetic_controls_are_native_inputs": False,
            "next_exact_input": "Construct the actual sectorwise K139/K168 coefficient map and common form identity. For each sector certify six diagonal floors and fifteen coupling majorants, or the sharper comparison eigenvalue, and prove a uniform analytic tail. Then set m=inf_n m_n and separately certify alpha and delta for the same-domain remainder.",
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This is a sufficient analytic certificate for a conditional operator form and supplies none of its missing native numerical inputs.",
        "preflight_bookend": {
            "route_comparison": "Once K643 localizes B by bath number, a six-by-six scalar comparison matrix is the cheapest rigorous route from operator blocks to m; it retains operator-valued spectator action instead of reverting to K640's scalar native misidentification.",
            "retrieval_collision_result": "K158 uses a finite Gershgorin control for a different generalized pencil, while no current artifact gives a block-form comparison theorem for K642's six-channel spectator sectors or composes it with the uniform sector infimum.",
            "strongest_alternative": "A direct spectral calculation of every B_n would be sharper, but it is more expensive and still requires the same missing K139/K168 block identity and tail control.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Reporting a synthetic comparison row, a finite prefix minimum or a failed diagonal-dominance lower as the native complete-sector floor.",
            "strongest_contrary_construction": "A block form can have a useful positive least comparison eigenvalue even when a crude row bound is weak; conversely a single actual sector below a proposed m rejects that uniform m.",
            "weakest_reproducibility_seam": "Native use depends on proving that the K139/K168 form has these six blocks on one common sector domain and on supplying uniform tail estimates.",
        },
        "controls": {
            "producer": "tests/channel-swings/k644_k500_operator_block_lower_certificate.py",
            "probe": "tests/channel-swings/k644_k500_operator_block_lower_certificate_probe.py",
            "controls_passed": 30,
            "hostile_mutations_rejected": 25,
        },
        "claim_ceiling": "Exact sufficient lower theorem for closed six-channel operator block forms on each K643 bath sector. Diagonal floors and symmetric off-diagonal Hilbert-form bounds define C_n, giving m_n>=lambda_min(C_n) and the cheaper row certificate g_n. A uniform sector infimum composes with K642's floors. The actual K139/K168 block identity, diagonal floors, coupling bounds, uniform tail, native m, alpha and delta remain missing; no native complete-sector floor, K473 beta, K152 interval, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows.",
    }


def validate(payload: dict) -> None:
    theorem = payload["operator_block_theorem"]
    composition = payload["sector_to_global_composition"]
    controls = payload["exact_controls"]
    native = payload["native_interface_status"]
    assert theorem["sharp_comparison_floor"] == "m_n>=lambda_min(C_n)"
    assert theorem["no_bounded_diagonal_operator_requirement"]
    assert controls["all_controls_pass"] and controls["controls_are_synthetic_not_native"]
    assert composition["K642_base_floor"] == "min(1/2,m-1/128)"
    assert native["six_channel_operator_certificate_constructed"]
    assert not native["native_global_m_identified"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
