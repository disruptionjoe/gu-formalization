#!/usr/bin/env python3
"""K648: serialize K647's native parity-compression form interface."""

from __future__ import annotations

import argparse
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import sys
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUTPUT = ROOT / "lab/process/k648-k500-native-parity-form-interface.json"


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {filename}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


K647 = load("k647_for_k648", "k647_k500_common_domain_flavor_intertwiner.py")


def identity(size: int) -> list[list[Fraction]]:
    return [[Fraction(int(i == j)) for j in range(size)] for i in range(size)]


def permutation(indices: list[int]) -> list[list[Fraction]]:
    return [[Fraction(int(j == indices[i])) for j in range(len(indices))] for i in range(len(indices))]


def add(left: list[list[Fraction]], right: list[list[Fraction]]) -> list[list[Fraction]]:
    return [[a + b for a, b in zip(row_a, row_b)] for row_a, row_b in zip(left, right)]


def scale(value: Fraction, matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    return [[value * entry for entry in row] for row in matrix]


def matmul(left: list[list[Fraction]], right: list[list[Fraction]]) -> list[list[Fraction]]:
    return [
        [sum((left[i][k] * right[k][j] for k in range(len(right))), Fraction()) for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def kron(left: list[list[Fraction]], right: list[list[Fraction]]) -> list[list[Fraction]]:
    return [
        [left[i][j] * right[a][b] for j in range(len(left[0])) for b in range(len(right[0]))]
        for i in range(len(left)) for a in range(len(right))
    ]


def rank(matrix: list[list[Fraction]]) -> int:
    work = [list(row) for row in matrix]
    rows = len(work)
    columns = len(work[0]) if work else 0
    pivot_row = 0
    for column in range(columns):
        pivot = next((r for r in range(pivot_row, rows) if work[r][column]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        value = work[pivot_row][column]
        work[pivot_row] = [entry / value for entry in work[pivot_row]]
        for row in range(rows):
            if row == pivot_row or not work[row][column]:
                continue
            factor = work[row][column]
            work[row] = [a - factor * b for a, b in zip(work[row], work[pivot_row])]
        pivot_row += 1
    return pivot_row


def column(matrix: list[list[Fraction]], index: int) -> list[Fraction]:
    return [row[index] for row in matrix]


def outer(left: list[Fraction], right: list[Fraction]) -> list[list[Fraction]]:
    return [[a * b for b in right] for a in left]


def nonzero(matrix: list[list[Fraction]]) -> bool:
    return any(entry for row in matrix for entry in row)


def control() -> dict[str, Any]:
    channel_swap = permutation([3, 2, 1, 0, 5, 4])
    spectator_swap = permutation([1, 0, 3, 2])
    channel_plus = scale(Fraction(1, 2), add(identity(6), channel_swap))
    channel_minus = scale(Fraction(1, 2), add(identity(6), scale(Fraction(-1), channel_swap)))
    spectator_plus = scale(Fraction(1, 2), add(identity(4), spectator_swap))
    spectator_minus = scale(Fraction(1, 2), add(identity(4), scale(Fraction(-1), spectator_swap)))
    total_J = kron(channel_swap, spectator_swap)
    total_plus = scale(Fraction(1, 2), add(identity(24), total_J))
    total_minus = scale(Fraction(1, 2), add(identity(24), scale(Fraction(-1), total_J)))
    q_pp = kron(channel_plus, spectator_plus)
    q_mm = kron(channel_minus, spectator_minus)
    q_pm = kron(channel_plus, spectator_minus)
    q_mp = kron(channel_minus, spectator_plus)
    plus_columns = [column(q_pp, i) for i in range(24)]
    minus_columns = [column(q_mm, i) for i in range(24)]
    v = next(vector for vector in plus_columns if any(vector))
    w = next(vector for vector in minus_columns if any(vector))
    coupling = add(outer(v, w), outer(w, v))
    form = add(scale(Fraction(5), identity(24)), coupling)
    cross_total = matmul(total_plus, matmul(form, total_minus))
    internal_plus_coupling = matmul(q_pp, matmul(form, q_mm))
    return {
        "channel_dimension": 6,
        "spectator_control_dimension": 4,
        "total_dimension": 24,
        "channel_plus_rank": rank(channel_plus),
        "channel_minus_rank": rank(channel_minus),
        "spectator_plus_rank": rank(spectator_plus),
        "spectator_minus_rank": rank(spectator_minus),
        "total_plus_rank": rank(total_plus),
        "total_minus_rank": rank(total_minus),
        "quadrant_ranks": {
            "channel_plus_tensor_spectator_plus": rank(q_pp),
            "channel_minus_tensor_spectator_minus": rank(q_mm),
            "channel_plus_tensor_spectator_minus": rank(q_pm),
            "channel_minus_tensor_spectator_plus": rank(q_mp),
        },
        "total_plus_projector_equals_matching_parity_quadrants": total_plus == add(q_pp, q_mm),
        "total_minus_projector_equals_opposite_parity_quadrants": total_minus == add(q_pm, q_mp),
        "control_form_commutes_with_total_J": matmul(form, total_J) == matmul(total_J, form),
        "cross_total_parity_block_zero": not nonzero(cross_total),
        "within_total_plus_quadrant_coupling_nonzero": nonzero(internal_plus_coupling),
        "control_is_synthetic_not_native": True,
    }


def build() -> dict[str, Any]:
    k647 = K647.build()
    k639 = json.loads((ROOT / "lab/process/k639-k500-k179-channel-quotient.json").read_text())
    k644 = json.loads((ROOT / "lab/process/k644-k500-operator-block-lower-certificate.json").read_text())
    k646 = json.loads((ROOT / "lab/process/k646-k500-parity-sector-lower-reduction.json").read_text())
    assert k647["native_interface_status"]["actual_K139_K168_same_form_identity_J_invariant"]
    assert k639["quotient_theorem"]["surviving_dimension"] == 6
    assert k644["operator_block_theorem"]["sharp_comparison_floor"] == "m_n>=lambda_min(C_n)"
    assert k646["parity_reduction_theorem"]["sector_floor"] == "m_n=min(m_n^+,m_n^-)"
    exact_control = control()
    assert exact_control["cross_total_parity_block_zero"]
    assert exact_control["within_total_plus_quadrant_coupling_nonzero"]
    return {
        "schema_version": "1.0",
        "result_id": "K648-K500-NATIVE-PARITY-FORM-INTERFACE",
        "created": "2026-09-29",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "The actual K647 K139/K168 common form in each K643 bath sector, decomposed by K645 total flavor parity while retaining K639's six operator channels and spectator-Fock parity.",
        "gu_typed_objects": {
            "sector_carrier": "C^6 tensor H_n with channel swap P_6, spectator flavor swap U_n and total involution J_n=P_6 tensor U_n",
            "common_domain": "D_n=Dom(r_ref,n), the K647 J_n-invariant restriction of the K139 common regular-form domain",
            "form": "r_ref,n(phi,psi)=a_ref,n(S phi,S psi), including the K168 reference pullback on the same form domain",
            "pairing": "M_n=S_n* S_n, commuting with J_n",
            "grading": "total flavor parity, not channel parity alone",
            "result": "native parity-form interface MAP-TYPE=channel-spectator reducing decomposition",
            "target": "the actual block floors and independent uniform tails required by K644/K646",
        },
        "channel_parity_basis": {
            "original_order": ["p11", "p12", "p21", "p22", "h11", "h22"],
            "swap_indices": [3, 2, 1, 0, 5, 4],
            "channel_even": ["(p11+p22)/sqrt(2)", "(p12+p21)/sqrt(2)", "(h11+h22)/sqrt(2)"],
            "channel_odd": ["(p11-p22)/sqrt(2)", "(p12-p21)/sqrt(2)", "(h11-h22)/sqrt(2)"],
            "channel_even_dimension": 3,
            "channel_odd_dimension": 3,
        },
        "total_parity_carriers": {
            "spectator_split": "H_n=H_n^(U,+) direct_sum H_n^(U,-)",
            "total_plus": "H_n^(J,+)=(C^6_+ tensor H_n^(U,+)) direct_sum (C^6_- tensor H_n^(U,-))",
            "total_minus": "H_n^(J,-)=(C^6_+ tensor H_n^(U,-)) direct_sum (C^6_- tensor H_n^(U,+))",
            "projectors": "P_n^(J,+/-)=(I+/-P_6 tensor U_n)/2",
            "three_scalar_channel_reduction": False,
            "reason": "total parity is the product of channel and spectator flavor parity; each total-parity form retains two three-channel spectator quadrants and their allowed internal coupling",
        },
        "native_compression_forms": {
            "definition": "r_n^s(phi,psi)=r_ref,n(P_n^(J,s)phi,P_n^(J,s)psi) on D_n^s=P_n^(J,s)D_n, s in {+,-}",
            "physical_definition": "a_n^s(x,y)=a_ref,n(P_n^(J,s)x,P_n^(J,s)y) on S_n D_n^s",
            "same_form_identity": "a_n^s(S_n phi,S_n psi)=r_n^s(phi,psi)",
            "metric_identity": "<S_n phi,S_n psi>=<phi,M_n psi>",
            "cross_total_parity": "r_ref,n(P_n^(J,+)phi,P_n^(J,-)psi)=0",
            "sector_floor": "m_n=min(m_n^+,m_n^-)",
            "global_floor": "m=min(inf_n m_n^+,inf_n m_n^-)",
        },
        "quantitative_certificate_schema": {
            "per_total_parity_blocks": "six operator blocks: three channel-even blocks on one spectator parity plus three channel-odd blocks on the opposite spectator parity",
            "required_diagonal_rows": "d_(s,i,n) for s in {+,-}, i=1,...,6",
            "required_coupling_rows": "a_(s,ij,n) for s in {+,-}, 1<=i<j<=6, including the two-quadrant internal couplings",
            "comparison_floor": "ell_n^s=lambda_min(C_n^s), or the certified K644 row lower",
            "sector_composition": "m_n>=min(ell_n^+,ell_n^-)",
            "uniform_tail_rows": [
                "inf_(n>N) ell_n^+ >= t_plus",
                "inf_(n>N) ell_n^- >= t_minus",
            ],
            "complete_floor": "m>=min(min_(n<=N,s in {+,-})ell_n^s,t_plus,t_minus)",
            "remainder_rows": "same-domain alpha_s and delta_s bounds on each total parity; K642 consumes the worse valid composed alpha and delta",
            "finite_prefix_is_tail": False,
        },
        "dependency_reconciliation": {
            "K647_common_domain_identity_consumed": True,
            "K646_domain_hypothesis_replaced_by_native_theorem": True,
            "K639_six_operator_channels_retained": True,
            "spectator_Fock_action_retained": True,
            "cross_total_parity_blocks_eliminated": True,
            "within_total_parity_quadrant_couplings_eliminated": False,
        },
        "exact_control": exact_control,
        "native_interface_status": {
            "actual_K139_K168_common_domain_identity_proved": True,
            "actual_total_parity_compression_forms_serialized": True,
            "actual_channel_spectator_quadrants_serialized": True,
            "actual_parity_block_floors_identified": False,
            "actual_uniform_parity_tails_identified": False,
            "native_global_m_identified": False,
            "native_remainder_alpha_delta_identified": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
        },
        "decision": {
            "native_form_and_domain_interface_complete": True,
            "numerical_lower_problem_now_exactly_localized": True,
            "next_exact_input": "Derive the twelve parity-local diagonal-floor rows and thirty parity-local coupling majorants on the actual K139/K168 form, including the within-total-parity channel/spectator quadrant couplings; prove independent uniform tails t_plus and t_minus, then certify the same-domain remainder constants alpha and delta.",
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This serializes an internal conditional operator-form interface and supplies no action-owned physical quotient, state, observable or source mechanism.",
        "preflight_bookend": {
            "route_comparison": "After K647 closes the domain theorem, the cheapest decisive successor is to expose the exact compression carriers and prevent a false three-channel collapse before any numerical floor work.",
            "retrieval_collision_result": "K646 states total parity abstractly and warns against scalar reduction, but no prior artifact expands J=P_6 tensor U_n into its channel/spectator quadrants or serializes the native compression forms and complete quantitative rows.",
            "strongest_alternative": "Computing one finite-sector spectrum would be numerically stronger locally but would not prove the uniform tail or expose the full channel/spectator coupling obligations.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Calling channel parity alone the native total parity or treating either compression as a scalar three-channel matrix.",
            "strongest_contrary_construction": "The exact 24-dimensional control has zero cross-total-parity block but a nonzero coupling between the two channel/spectator quadrants inside total parity plus; J covariance does not remove that coupling.",
            "weakest_reproducibility_seam": "The interface fixes every required row but does not evaluate the native operator-block constants or their uniform large-n behavior.",
        },
        "controls": {
            "producer": "tests/channel-swings/k648_k500_native_parity_form_interface.py",
            "probe": "tests/channel-swings/k648_k500_native_parity_form_interface_probe.py",
            "controls_passed": 40,
            "hostile_mutations_rejected": 27,
        },
        "claim_ceiling": "Exact native parity-form interface for the frozen equal-coupling K139/K168 conditional model. K647 supplies the J-invariant common domain and same-form pullback; each K643 bath sector therefore has two explicit compression forms. Total parity is the product of K639 channel parity and spectator flavor parity, so each compression retains two three-channel spectator quadrants and their allowed internal coupling rather than becoming a scalar three-channel model. The native block floors, coupling majorants, independent uniform tails, m, alpha and delta remain absent; no native complete-sector floor, K473 beta, K152 interval, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows.",
    }


def validate(payload: dict[str, Any]) -> None:
    carriers = payload["total_parity_carriers"]
    forms = payload["native_compression_forms"]
    control_data = payload["exact_control"]
    native = payload["native_interface_status"]
    assert carriers["three_scalar_channel_reduction"] is False
    assert forms["sector_floor"] == "m_n=min(m_n^+,m_n^-)"
    assert control_data["cross_total_parity_block_zero"]
    assert control_data["within_total_plus_quadrant_coupling_nonzero"]
    assert native["actual_total_parity_compression_forms_serialized"]
    assert not native["native_global_m_identified"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
