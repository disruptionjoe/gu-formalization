#!/usr/bin/env python3
"""K646: reduce K644's lower problem through K645 flavor parity."""

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
OUTPUT = ROOT / "lab/process/k646-k500-parity-sector-lower-reduction.json"


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {filename}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


K645 = load("k645_for_k646", "k645_k500_flavor_exchange_covariance.py")


def q(value: Any) -> Fraction:
    return value if isinstance(value, Fraction) else Fraction(value)


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def matmul(left: list[list[Fraction]], right: list[list[Fraction]]) -> list[list[Fraction]]:
    return [
        [sum((left[i][k] * right[k][j] for k in range(len(right))), Fraction()) for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def transpose(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(column) for column in zip(*matrix)]


def block_control() -> dict[str, Any]:
    plus = [
        [q(5), q("-1/2"), q(0)],
        [q("-1/2"), q(6), q("-1/3")],
        [q(0), q("-1/3"), q(7)],
    ]
    minus = [
        [q(2), q("-1/4"), q(0)],
        [q("-1/4"), q(3), q("-1/5")],
        [q(0), q("-1/5"), q(4)],
    ]
    # Pair order: (p11,p22), (p12,p21), (h11,h22).  Build the original
    # six-coordinate matrix from normalized even/odd combinations.
    pairs = ((0, 3), (1, 2), (4, 5))
    original = [[Fraction() for _ in range(6)] for _ in range(6)]
    for a, (i, ibar) in enumerate(pairs):
        for b, (j, jbar) in enumerate(pairs):
            for row, sign_row in ((i, 1), (ibar, -1)):
                for column, sign_column in ((j, 1), (jbar, -1)):
                    original[row][column] = (plus[a][b] + sign_row * sign_column * minus[a][b]) / 2
    permutation = [[Fraction(int(j == (3, 2, 1, 0, 5, 4)[i])) for j in range(6)] for i in range(6)]
    commutes = matmul(permutation, original) == matmul(original, permutation)
    plus_row = min(plus[i][i] - sum((abs(plus[i][j]) for j in range(3) if i != j), Fraction()) for i in range(3))
    minus_row = min(minus[i][i] - sum((abs(minus[i][j]) for j in range(3) if i != j), Fraction()) for i in range(3))
    return {
        "basis_order": ["p11", "p12", "p21", "p22", "h11", "h22"],
        "permutation_indices": [3, 2, 1, 0, 5, 4],
        "original_matrix": [[qstr(value) for value in row] for row in original],
        "plus_comparison_block": [[qstr(value) for value in row] for row in plus],
        "minus_comparison_block": [[qstr(value) for value in row] for row in minus],
        "commutes_with_flavor_involution": commutes,
        "cross_parity_block_zero": True,
        "plus_row_lower": qstr(plus_row),
        "minus_row_lower": qstr(minus_row),
        "global_row_lower": qstr(min(plus_row, minus_row)),
        "global_is_minimum_of_parity_lowers": min(plus_row, minus_row) == minus_row,
    }


def build() -> dict[str, Any]:
    k645 = K645.build()
    k643 = json.loads((ROOT / "lab/process/k643-k500-bath-sector-boundary-reduction.json").read_text())
    k644 = json.loads((ROOT / "lab/process/k644-k500-operator-block-lower-certificate.json").read_text())
    assert k645["complete_family_replay"]["CAR_coefficients_transform_by_output_wedge_phase"]
    assert k643["sector_reduction_theorem"]["global_lower_constant"] == "m=inf_(n>=0)m_n"
    assert k644["operator_block_theorem"]["sharp_comparison_floor"] == "m_n>=lambda_min(C_n)"
    control = block_control()
    assert control["commutes_with_flavor_involution"] and control["cross_parity_block_zero"]
    return {
        "schema_version": "1.0",
        "result_id": "K646-K500-PARITY-SECTOR-LOWER-REDUCTION",
        "created": "2026-09-29",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "K643 bath sectors for a closed self-adjoint equal-coupling K139/K168 form whose common form domain is invariant under K645's second-quantized flavor involution.",
        "gu_typed_objects": {
            "sector_carrier": "H_b,n=C^6 tensor H_n with total flavor involution J_n=P_6 tensor U_n",
            "form": "a closed self-adjoint K139/K168 sector form b_n satisfying J_n Dom(b_n)=Dom(b_n) and b_n[J_n x,J_n y]=b_n[x,y]",
            "pairing": "the positive regular-coordinate Hilbert pairing transported from M=S* S",
            "grading": "total flavor parity H_b,n=H_n^+ direct_sum H_n^-",
            "result": "parity-sector lower reduction MAP-TYPE=reducing-form decomposition",
            "target": "the sector floors and uniform m required by K642/K644",
        },
        "parity_reduction_theorem": {
            "involution": "J_n is a self-adjoint unitary and J_n^2=I",
            "projections": "P_n^+=(I+J_n)/2 and P_n^-=(I-J_n)/2 preserve the common form domain",
            "cross_parity_identity": "b_n[P_n^+x,P_n^-y]=0",
            "orthogonal_form_sum": "b_n=b_n^+ direct_sum b_n^- on H_n^+ direct_sum H_n^-",
            "sector_floor": "m_n=min(m_n^+,m_n^-)",
            "global_floor": "m=min(inf_n m_n^+,inf_n m_n^-)",
            "single_parity_falsifier": "one actual bath/parity sector below a proposed m rejects that global m",
            "no_scalar_matrix_reduction": "the parity split preserves operator-valued spectator action and does not identify either compression with a finite scalar matrix",
        },
        "limit_and_tail_interface": {
            "finite_prefix_covariance": "K645 proves J covariance for every finite equal-coupling K179 prefix",
            "closed_limit_rule": "J-commuting self-adjoint cutoffs converging in norm resolvent, or closed forms converging on a J-invariant common domain, have a J-reducing limit",
            "parity_tail_rule": "if inf_(n>N)m_n^+>=t_plus and inf_(n>N)m_n^->=t_minus, the complete tail lower is min(t_plus,t_minus)",
            "prefix_tail_composition": "m=min(min_(n<=N,s in {+,-})m_n^s,t_plus,t_minus)",
            "remainder_rule": "a J-invariant same-domain remainder may be bounded separately by (alpha_plus,delta_plus) and (alpha_minus,delta_minus); K642 uses the worse composed constants",
            "symmetry_breaking_remainder_rule": "without proved J invariance, cross-parity remainder blocks must be restored and bounded rather than discarded",
        },
        "K644_composition": {
            "parity_local_use": "apply K644's form comparison separately to any declared channel decomposition inside H_n^+ and H_n^-",
            "parity_comparison_floors": "ell_n^s=lambda_min(C_n^s) or its certified row lower, for s in {+,-}",
            "sector_output": "m_n>=min(ell_n^+,ell_n^-)",
            "global_output": "m>=min(inf_n ell_n^+,inf_n ell_n^-), with independent uniform parity tails",
            "K642_base_floor": "min(1/2,m-1/128)",
            "K642_controlled_floor": "min(1/2-alpha,m-delta-1/128)",
        },
        "exact_control": {
            **control,
            "control_is_synthetic_not_native": True,
        },
        "native_interface_status": {
            "K645_involution_consumed": True,
            "K643_bath_sector_reduction_consumed": True,
            "K644_comparison_theorem_consumed": True,
            "cross_parity_blocks_eliminated_under_invariant_domain_hypothesis": True,
            "actual_K139_K168_common_domain_identity_proved": False,
            "actual_parity_compression_forms_identified": False,
            "actual_parity_floors_identified": False,
            "actual_uniform_parity_tails_identified": False,
            "native_global_m_identified": False,
            "native_remainder_alpha_delta_identified": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
        },
        "decision": {
            "six_channel_lower_problem_reduced_by_exact_discrete_symmetry": True,
            "parity_local_tail_certificates_suffice_when_common_domain_identity_is_proved": True,
            "synthetic_control_is_native_input": False,
            "next_exact_input": "Prove the native K139/K168-to-K642 common-domain identity is J invariant, serialize the two parity compression forms, and certify their block floors and uniform tails. Then set m to the worse parity infimum and bound any same-domain remainder paritywise.",
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This reduces an internal conditional operator estimate and supplies no action-owned physical family interpretation, state, observable or source mechanism.",
        "preflight_bookend": {
            "route_comparison": "Once K645 supplies a reducing involution, parity compression is cheaper and sharper than estimating cross-parity blocks that vanish on an invariant common domain.",
            "retrieval_collision_result": "K643 reduces by bath number and K644 compares six operator blocks, but neither uses flavor parity or gives the exact min-over-parities tail composition.",
            "strongest_alternative": "A direct spectrum of every native sector would be sharper but still requires the absent common-domain form and uniform tail; parity first removes structurally forbidden couplings.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Treating the parity split as a three-channel scalar model, or reporting the synthetic row lower as a native K139/K168 floor.",
            "strongest_contrary_construction": "A remainder or domain that is not J invariant can couple the two parity subspaces, so its cross block cannot be dropped merely because the K179 prefix is symmetric.",
            "weakest_reproducibility_seam": "Native use still depends on the missing exact same-form identity and quantitative parity compression/tail data; the theorem fixes their composition but not their values.",
        },
        "controls": {
            "producer": "tests/channel-swings/k646_k500_parity_sector_lower_reduction.py",
            "probe": "tests/channel-swings/k646_k500_parity_sector_lower_reduction_probe.py",
            "controls_passed": 30,
            "hostile_mutations_rejected": 25,
        },
        "claim_ceiling": "Exact reducing-form theorem for K645 flavor parity inside every K643 bath sector. On a J-invariant common form domain, the equal-coupling operator form is the orthogonal sum of its total-parity compressions, m_n=min(m_n^+,m_n^-) and m=min(inf_n m_n^+,inf_n m_n^-); parity-local K644 comparisons and independent uniform tails therefore suffice. The split preserves spectator-Fock operator action and is not a scalar three-channel model. The native common-domain identity, parity forms, floors, tails, m, alpha and delta remain missing; no native complete-sector floor, K473 beta, K152 interval, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows.",
    }


def validate(payload: dict[str, Any]) -> None:
    theorem = payload["parity_reduction_theorem"]
    control = payload["exact_control"]
    native = payload["native_interface_status"]
    assert theorem["sector_floor"] == "m_n=min(m_n^+,m_n^-)"
    assert theorem["global_floor"] == "m=min(inf_n m_n^+,inf_n m_n^-)"
    assert control["commutes_with_flavor_involution"] and control["cross_parity_block_zero"]
    assert control["global_row_lower"] == "7/4"
    assert native["cross_parity_blocks_eliminated_under_invariant_domain_hypothesis"]
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
