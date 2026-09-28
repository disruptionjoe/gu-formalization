#!/usr/bin/env python3
"""K599 sharp-tail perturbation interface for the three K583 moments."""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k599-k500-sharp-tail-moment-enclosure-interface.json"


def strict(path: str) -> dict:
    return json.loads((ROOT / path).read_text())


def q(x):
    x = Fraction(x)
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def inner(a, b):
    return sum(Fraction(x) * Fraction(y) for x, y in zip(a, b))


def moment_row(name, v, wf, tail, epsilon):
    n = inner(v, v); a = inner(v, wf); beta2 = inner(wf, wf)
    # Controls deliberately use rational square roots, as the production
    # interface accepts outward intervals for sqrt(N) and sqrt(B_F).
    assert n.denominator == 1 and beta2.denominator == 1
    sqrt_n = Fraction(math.isqrt(n.numerator))
    sqrt_b = Fraction(math.isqrt(beta2.numerator))
    assert sqrt_n * sqrt_n == n and sqrt_b * sqrt_b == beta2
    eps = Fraction(epsilon)
    complete = [Fraction(x) + Fraction(y) for x, y in zip(wf, tail)]
    actual_a, actual_b = inner(v, complete), inner(complete, complete)
    a_interval = [a - sqrt_n * eps, a + sqrt_n * eps]
    b_interval = [max(Fraction(), sqrt_b - eps) ** 2, (sqrt_b + eps) ** 2]
    dist0 = Fraction() if a_interval[0] <= 0 <= a_interval[1] else min(abs(a_interval[0]), abs(a_interval[1]))
    leakage_upper = b_interval[1] / n - dist0**2 / n**2
    actual_leakage = actual_b / n - actual_a**2 / n**2
    return {
        "name": name,
        "N": q(n),
        "A_finite": q(a),
        "B_finite": q(beta2),
        "tail_norm": q(Fraction(math.isqrt(inner(tail, tail).numerator), math.isqrt(inner(tail, tail).denominator))),
        "tail_epsilon": q(eps),
        "A_complete_interval": [q(x) for x in a_interval],
        "B_complete_interval": [q(x) for x in b_interval],
        "actual_A_complete": q(actual_a),
        "actual_B_complete": q(actual_b),
        "actual_leakage_square": q(actual_leakage),
        "leakage_square_upper": q(leakage_upper),
        "A_contained": a_interval[0] <= actual_a <= a_interval[1],
        "B_contained": b_interval[0] <= actual_b <= b_interval[1],
        "leakage_contained": Fraction() <= actual_leakage <= leakage_upper,
    }


def build() -> dict:
    k574 = strict("lab/process/k574-k176-sharp-post-adjoint-tail-reconciliation.json")
    k583 = strict("lab/process/k583-k500-all-level-tensor-pair-leakage.json")
    k597 = strict("lab/process/k597-k500-action-column-tail-reconciliation.json")
    eps = Fraction(k574["sharp_tail"]["sharp_tail_norm_upper"])
    controls = [
        moment_row("parallel tail", [3, 4], [0, 5], [0, Fraction(1, 4)], Fraction(1, 4)),
        moment_row("orthogonal tail", [3, 4], [0, 5], [Fraction(1, 4), 0], Fraction(1, 4)),
        moment_row("negative cross tail", [4, 3], [5, 0], [Fraction(-1, 4), 0], Fraction(1, 4)),
    ]
    return {
        "schema_version": "1.0",
        "result_id": "K599-K500-SHARP-TAIL-MOMENT-ENCLOSURE-INTERFACE",
        "created": "2026-09-28",
        "status": "working_draft_verified",
        "classification": "INTERNAL_CONDITIONAL_MATHEMATICS",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Rigorous composition of finite K456/K583 moment enclosures with K574's one post-order-12 norm tail for each supported q00/q10 level.",
        "gu_typed_objects": {
            "carrier": "one K500 supported bath level with cyclic vector v_n",
            "finite_action_vector": "w_F,n=(W_n v_n) through exchange order 12",
            "tail": "t_n=(W_n v_n)-w_F,n with ||t_n||<=epsilon_n",
            "pairing": "regular Hilbert pairing transported from M=S* S",
            "result": "sharp-tail moment enclosure MAP-TYPE=orthogonal-block-norm-bound",
            "target": "lambda_n^2=||W_n v_n||^2/||v_n||^2-|<v_n,W_n v_n>|^2/||v_n||^4",
        },
        "theorem": {
            "finite_inputs": ["N=||v||^2", "A_F=<v,w_F>", "B_F=||w_F||^2"],
            "tail_input": "||t||<=epsilon",
            "A_complete": "A in A_F + [-sqrt(N) epsilon,+sqrt(N) epsilon]",
            "B_complete": "B in [max(0,sqrt(B_F)_lower-epsilon)^2,(sqrt(B_F)_upper+epsilon)^2]",
            "leakage_upper": "lambda^2 <= B_upper/N_lower - dist(0,A_interval)^2/N_upper^2, with outward interval arithmetic and consistent N endpoints",
            "tail_charged_once": True,
            "scalar_moment_sign_retained": True,
            "full_operator_matrix_not_required": k583["theorem"]["diagonal_multiplier_not_required"],
        },
        "K574_application": {
            "sharp_tail_norm_upper": q(eps),
            "resolved_through_order": k574["sharp_tail"]["resolved_through_order"],
            "same_post_left_adjoint_location": k574["compatibility_replay"]["same_post_left_adjoint_location"],
            "exact_improvement_factor": k574["sharp_tail"]["exact_improvement_factor"],
            "finite_moments_numerically_enclosed": False,
            "complete_uniform_leakage_emitted": False,
        },
        "exact_controls": {
            "rows": controls,
            "row_count": len(controls),
            "all_A_contained": all(r["A_contained"] for r in controls),
            "all_B_contained": all(r["B_contained"] for r in controls),
            "all_leakage_contained": all(r["leakage_contained"] for r in controls),
            "parallel_orthogonal_and_negative_cross_present": {r["name"] for r in controls} == {"parallel tail", "orthogonal tail", "negative cross tail"},
        },
        "non_substitutability": {
            "K597_three_moments_preserved": k597["composition_theorem"]["minimum_remaining_numeric_payload"],
            "K575_residual_substitution_allowed": False,
            "a_complete_norm_enclosure_without_A_does_not_determine_leakage": True,
            "reason": "The cyclic subtraction depends on the signed interval for <v,Wv>; a norm-only residual interval can share B while producing different leakage.",
        },
        "decision": {
            "sharp_tail_composition_interface_emitted": True,
            "duplicate_tail_charge_forbidden": True,
            "numerical_finite_moment_evaluation_still_required": True,
            "complete_K500_uniform_leakage_emitted": False,
            "native_noncyclic_floor_emitted": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
            "next_exact_input": "For each supported q00/q10 level, outwardly enclose N, A_F and B_F from K456's finite vector integrals, then apply K599 with K574's epsilon once. Prove the resulting leakage upper uniform in level; separately supply the noncyclic floor.",
        },
        "source_and_ledger_effect": "none",
        "preflight_bookend": {
            "route_comparison": "Freeze the exact tail-to-moment formulas before expensive finite quadrature so every integral has a named consumer and the tail is not double counted.",
            "retrieval_collision_result": "K574 supplies a norm tail, K583 supplies the three-moment identity and K597 proves the finite moments remain unevaluated; no predecessor composes them.",
            "strongest_alternative": "Direct tensor-pair quadrature is equivalent but duplicates more cross products and obscures the signed cyclic subtraction.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Calling the moment interface a numerical uniform bound before N, A_F and B_F are enclosed at every supported level.",
            "strongest_contrary_construction": "Equal complete norms with different signed cyclic moments give different leakage, so K575 cannot replace A_F.",
            "weakest_reproducibility_seam": "Production use requires outward square-root endpoints consistent with the finite B_F enclosure.",
        },
        "claim_ceiling": "Exact sharp-tail composition theorem for K583's three moments: finite N, A_F and B_F enclosures plus K574's tail norm produce complete A, B and leakage enclosures with the tail charged once. The theorem supplies the numerical acceptance interface but not the finite moment values, a uniform all-level leakage bound, noncyclic floor, K473 beta, K152 interval, source, ledger, canon, paper, public, novelty or physical conclusion.",
    }


def validate(p: dict) -> None:
    t, k, c, n, d = p["theorem"], p["K574_application"], p["exact_controls"], p["non_substitutability"], p["decision"]
    assert t["tail_charged_once"] and t["scalar_moment_sign_retained"] and t["full_operator_matrix_not_required"]
    assert k["same_post_left_adjoint_location"] and k["exact_improvement_factor"] == "40/3"
    assert not k["finite_moments_numerically_enclosed"] and not k["complete_uniform_leakage_emitted"]
    assert c["row_count"] == 3 and c["all_A_contained"] and c["all_B_contained"] and c["all_leakage_contained"] and c["parallel_orthogonal_and_negative_cross_present"]
    assert not n["K575_residual_substitution_allowed"] and n["a_complete_norm_enclosure_without_A_does_not_determine_leakage"]
    assert d["sharp_tail_composition_interface_emitted"] and d["duplicate_tail_charge_forbidden"] and d["numerical_finite_moment_evaluation_still_required"]
    assert not any(d[k] for k in ("complete_K500_uniform_leakage_emitted", "native_noncyclic_floor_emitted", "K473_released", "native_K152_interval_emitted"))


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--write", action="store_true"); args = parser.parse_args()
    payload = build(); validate(payload); rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write: OUTPUT.write_text(rendered)
    else: print(rendered, end="")
    return 0


if __name__ == "__main__": raise SystemExit(main())
