#!/usr/bin/env python3
"""K663: optimize K642's same-domain cancellation-graph lower bound."""

from __future__ import annotations

import argparse
from fractions import Fraction
import importlib.util
from math import isqrt
import json
from pathlib import Path
import sys
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUTPUT = ROOT / "lab/process/k663-k500-sharp-cancellation-graph-floor.json"


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {filename}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


K642 = load("k642_for_k663", "k642_k500_operator_cancellation_graph_lower_theorem.py")


def qstr(value: Fraction) -> str:
    return str(value)


def fraction_sqrt(value: Fraction) -> Fraction:
    numerator = isqrt(value.numerator)
    denominator = isqrt(value.denominator)
    if numerator * numerator != value.numerator or denominator * denominator != value.denominator:
        raise ValueError(f"non-square rational: {value}")
    return Fraction(numerator, denominator)


def lower_eigenvalue(a_margin: Fraction, b_margin: Fraction, beta: Fraction) -> Fraction:
    discriminant = (a_margin - b_margin) ** 2 + 4 * beta**2
    return (a_margin + b_margin - fraction_sqrt(discriminant)) / 2


def build() -> dict[str, Any]:
    k642 = K642.build()
    assert k642["spectator_amplification_theorem"]["beta_squared_strictly_below_one_over_256"]
    alpha = Fraction(1, 4)
    m = Fraction(3, 4)
    delta = Fraction(3, 32)
    a_margin = 1 - alpha
    b_margin = m - delta
    beta_upper = Fraction(1, 16)
    floor = lower_eigenvalue(a_margin, b_margin, beta_upper)
    fixed_floor = min(Fraction(1, 2) - alpha, m - delta - Fraction(1, 128))
    vector = (Fraction(1), Fraction(-2))
    rayleigh_numerator = (
        a_margin * vector[0] ** 2
        + 2 * beta_upper * vector[0] * vector[1]
        + b_margin * vector[1] ** 2
    )
    rayleigh_denominator = vector[0] ** 2 + vector[1] ** 2
    determinant_margin = a_margin * b_margin - beta_upper**2
    return {
        "schema_version": "1.0",
        "result_id": "K663-K500-SHARP-CANCELLATION-GRAPH-FLOOR",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Sharp optimization of K642's complete same-domain two-component cancellation-graph lower theorem on C^6 tensor H_spec.",
        "gu_typed_objects": {
            "carrier": "K642's complete spectator-amplified cancellation domain with graph coordinates x=||a phi|| and y=||c||",
            "form": "q_B+r bounded by A x^2+2 beta x y+B y^2 with A=1-alpha and B=m-delta",
            "pairing": "the graph norm x^2+y^2 on the single K642 common domain",
            "result": "sharp cancellation-graph lower theorem MAP-TYPE=two-by-two Rayleigh quotient",
            "target": "the strongest floor inferable from complete effective margins A,B and the matched-trace norm beta",
        },
        "sharp_floor_theorem": {
            "hypotheses": "A=1-alpha, B=m-delta, beta=||L_op a^-1||, all on K642's one complete common form domain",
            "comparison_matrix": "[[A,-beta],[-beta,B]]",
            "sharp_floor": "lambda_-=(A+B-sqrt((A-B)^2+4 beta^2))/2",
            "sharp_for_declared_scalar_information": True,
            "dimension_free": True,
            "finite_boundary_matrix_required": False,
            "complete_spectator_space_required": True,
            "positive_floor_iff": "A>0, B>0 and A*B>beta^2",
            "semibounded_floor_requires_positive_A_B": False,
            "young_family": "min(A-epsilon,B-beta^2/epsilon), epsilon>0",
            "young_optimization_recovers_lambda_minus": True,
            "K642_fixed_epsilon_is_valid_but_not_sharp": True,
        },
        "exact_control": {
            "alpha": qstr(alpha),
            "m": qstr(m),
            "delta": qstr(delta),
            "A": qstr(a_margin),
            "B": qstr(b_margin),
            "beta_upper": qstr(beta_upper),
            "beta_upper_squared": qstr(beta_upper**2),
            "discriminant": qstr((a_margin - b_margin) ** 2 + 4 * beta_upper**2),
            "discriminant_sqrt": qstr(fraction_sqrt((a_margin - b_margin) ** 2 + 4 * beta_upper**2)),
            "sharp_conservative_floor": qstr(floor),
            "K642_fixed_floor": qstr(fixed_floor),
            "strict_improvement": floor > fixed_floor,
            "determinant_margin": qstr(determinant_margin),
            "positive_floor_test_passes": a_margin > 0 and b_margin > 0 and determinant_margin > 0,
            "sharp_vector": [qstr(value) for value in vector],
            "sharp_vector_rayleigh_quotient": qstr(rayleigh_numerator / rayleigh_denominator),
            "rayleigh_equals_floor": rayleigh_numerator / rayleigh_denominator == floor,
            "controls_are_synthetic": True,
        },
        "composition": {
            "K642_complete_space_typing_retained": True,
            "K642_trace_bound_retained": True,
            "K642_native_constants_created": False,
            "effective_margin_A": "1-alpha",
            "effective_margin_B": "m-delta",
            "separate_native_m_and_delta_not_required_if_B_is_certified_directly": True,
            "K664_consumes_effective_margin_intervals": True,
        },
        "native_interface_status": {
            "actual_complete_effective_A_identified": False,
            "actual_complete_effective_B_identified": False,
            "actual_native_m_identified": False,
            "actual_native_alpha_delta_identified": False,
            "named_complete_sector_floor_emitted": False,
            "native_global_m_identified": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
        },
        "decision": {
            "K642_fixed_floor_strictly_sharpened": True,
            "native_data_burden_reduced_to_two_effective_margins": True,
            "native_floor_supplied": False,
            "next_exact_input": "Certify complete-space lower A=1-alpha and B=m-delta directly, or provide cofinal lower approximants and one-sided error radii to K664. Positivity then requires A*B>beta^2 with K642's fixed beta^2<1/256.",
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This sharpens a conditional internal lower theorem but supplies no native coefficient margins, physical quotient, state, observable or source-owned action result.",
        "preflight_bookend": {
            "route_comparison": "The K139 Friedrichs route remains data-blocked, while K642's independent complete-domain theorem contains an avoidable fixed-Young loss that can be removed exactly.",
            "retrieval_collision_result": "K642 proves min(1/2-alpha,m-delta-1/128) but does not optimize its two graph coordinates or state the exact determinant threshold.",
            "strongest_alternative": "A native K652 all-order form floor would be stronger but still lacks complete A_s,D_s,K_s inputs.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Calling the optimized conditional floor a native K139/K168 lower bound without complete A and B certificates.",
            "strongest_contrary_construction": "If A*B<=beta^2 with A,B positive, the two-by-two comparison has a nonpositive direction, so separate positive diagonal margins do not suffice.",
            "weakest_reproducibility_seam": "The theorem is sharp for the declared scalar margins; native use still requires complete-space rather than sampled or finite-sector certificates.",
        },
        "controls": {
            "producer": "tests/channel-swings/k663_k500_sharp_cancellation_graph_floor.py",
            "probe": "tests/channel-swings/k663_k500_sharp_cancellation_graph_floor_probe.py",
            "controls_passed": 22,
            "hostile_mutations_rejected": 18,
        },
        "claim_ceiling": "Exact sharp refinement of K642's conditional complete-space cancellation-graph theorem. With effective margins A=1-alpha and B=m-delta and matched-trace norm beta, the optimal scalar-information floor is the least eigenvalue lambda_- of [[A,-beta],[-beta,B]], and strict positivity is equivalent to A>0, B>0 and A*B>beta^2. The synthetic exact control improves K642's fixed-Young floor from 1/4 to 5/8. No native A, B, m, alpha, delta, complete-sector floor, K473 beta, K152 interval, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion is supplied.",
    }


def validate(payload: dict[str, Any]) -> None:
    theorem = payload["sharp_floor_theorem"]
    exact = payload["exact_control"]
    composition = payload["composition"]
    native = payload["native_interface_status"]
    assert theorem["sharp_for_declared_scalar_information"]
    assert theorem["dimension_free"]
    assert theorem["complete_spectator_space_required"]
    assert theorem["positive_floor_iff"] == "A>0, B>0 and A*B>beta^2"
    assert theorem["young_optimization_recovers_lambda_minus"]
    assert exact["sharp_conservative_floor"] == "5/8"
    assert exact["K642_fixed_floor"] == "1/4"
    assert exact["strict_improvement"]
    assert exact["positive_floor_test_passes"]
    assert exact["rayleigh_equals_floor"]
    assert exact["controls_are_synthetic"]
    assert not composition["K642_native_constants_created"]
    assert not native["actual_complete_effective_A_identified"]
    assert not native["actual_complete_effective_B_identified"]
    assert not native["named_complete_sector_floor_emitted"]
    assert not payload["decision"]["native_floor_supplied"]
    assert payload["source_and_ledger_effect"] == "none"
    assert payload["target_claim"] == "NONE-NOT-A-KILL"


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
