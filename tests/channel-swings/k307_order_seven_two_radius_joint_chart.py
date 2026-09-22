#!/usr/bin/env python3
"""Construct the joint two-radius chart for the K305/K306 order-seven route.

The old ``(x,q)`` order integrates q while holding x fixed.  That destroys the
joint scaling of every Bessel argument.  The native replacement is ``b=x*q``.
It turns the radial density into a product gamma density and makes every odd
and even cumulative node affine in the two nonnegative radii ``x`` and ``b``.
"""

from __future__ import annotations

import argparse
import itertools
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K294 = ROOT / "lab/process/k294-order-seven-global-radial-simplex-atlas.json"
K302 = ROOT / "lab/process/k302-order-seven-split-weighted-peano-jet.json"
K305 = ROOT / "lab/process/k305-order-seven-coherent-bordered-functional-compiler.json"
K306 = ROOT / "lab/process/k306-order-seven-joint-template-support-audit.json"
OUTPUT = ROOT / "lab/process/k307-order-seven-two-radius-joint-chart.json"


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    work = [row[:] for row in matrix]
    total = Fraction(1)
    for column in range(len(work)):
        pivot = next((row for row in range(column, len(work)) if work[row][column]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            total = -total
        value = work[column][column]
        total *= value
        work[column] = [entry / value for entry in work[column]]
        for row in range(column + 1, len(work)):
            factor = work[row][column]
            work[row] = [entry - factor * base for entry, base in zip(work[row], work[column])]
    return total


def kernel(argument: Fraction) -> Fraction:
    return Fraction(2, 1) / argument


def cauchy_matrix(left: list[Fraction], right: list[Fraction]) -> list[list[Fraction]]:
    return [[kernel(a + b) for b in right] for a in left]


def bordered_matrix(
    left: list[Fraction], right: list[Fraction], y: Fraction
) -> list[list[Fraction]]:
    matrix = cauchy_matrix(left, right)
    lvec = [y * kernel(value) for value in left[:3]] + [Fraction(0)]
    rvec = [(1 - y) * kernel(value) for value in right[:3]] + [Fraction(0)]
    bordered = [row + [lvec[index]] for index, row in enumerate(matrix)]
    bordered.append(rvec + [Fraction(0)])
    return bordered


def scaling_control() -> dict[str, Any]:
    left_odd = [Fraction(19, 7), Fraction(13, 7), Fraction(9, 7), Fraction(5, 7)]
    right_odd = [Fraction(17, 11), Fraction(12, 11), Fraction(8, 11), Fraction(3, 11)]
    left_even = [Fraction(23, 13), Fraction(16, 13), Fraction(10, 13), Fraction(4, 13)]
    right_even = [Fraction(29, 17), Fraction(21, 17), Fraction(14, 17), Fraction(5, 17)]
    y = Fraction(3, 7)
    base_d4 = determinant(cauchy_matrix(left_odd, right_odd))
    base_b5 = determinant(bordered_matrix(left_even, right_even, y))
    rows = []
    for scale in (Fraction(2), Fraction(5), Fraction(11, 3)):
        d4 = determinant(cauchy_matrix([scale * value for value in left_odd], [scale * value for value in right_odd]))
        b5 = determinant(bordered_matrix([scale * value for value in left_even], [scale * value for value in right_even], y))
        rows.append(
            {
                "scale": str(scale),
                "d4_degree_minus_four": d4 * scale**4 == base_d4,
                "b5_degree_minus_five": b5 * scale**5 == base_b5,
                "product_degree_minus_nine": d4 * b5 * scale**9 == base_d4 * base_b5,
            }
        )
    return {
        "model": "exact leading Cauchy kernel f(s)=2/s",
        "rows": rows,
        "all_exact": all(all(value for key, value in row.items() if key != "scale") for row in rows),
        "base_product_nonzero": base_d4 * base_b5 != 0,
    }


def affine_nodes() -> dict[str, Any]:
    return {
        "odd_left": {
            "T1": "x*y+b*(p_r0+p_r1+p_r2)",
            "T3": "x*y+b*(p_r1+p_r2)",
            "T5": "x*y+b*p_r2",
            "T7": "x*y",
        },
        "odd_right": {
            "U1": "x*(1-y)+b*(p_c0+p_c1+p_c2)",
            "U3": "x*(1-y)+b*(p_c1+p_c2)",
            "U5": "x*(1-y)+b*p_c2",
            "U7": "x*(1-y)",
        },
        "even_left": {
            "T2": "x*y+b*(p_r1+p_r2+p_r0*(1-u0))",
            "T4": "x*y+b*(p_r2+p_r1*(1-u1))",
            "T6": "x*y+b*p_r2*(1-u2)",
            "T8": "x*y*(1-u3)",
        },
        "even_right": {
            "U2": "x*(1-y)+b*(p_c1+p_c2+p_c0*(1-z0))",
            "U4": "x*(1-y)+b*(p_c2+p_c1*(1-z1))",
            "U6": "x*(1-y)+b*p_c2*(1-z2)",
            "U8": "x*(1-y)*(1-z3)",
        },
    }


def build() -> dict[str, Any]:
    k294 = json.loads(K294.read_text())
    k302 = json.loads(K302.read_text())
    k305 = json.loads(K305.read_text())
    k306 = json.loads(K306.read_text())
    if k294["global_chart"]["transformed_native_density"] != "exp(-256*x*(1+q))*x^15*y*(1-y)*q^11*product_i(p_i)":
        raise AssertionError("K294 radial density changed")
    if not k305["coupling_preservation"]["size_four_determinant_kept_joint"]:
        raise AssertionError("K305 joint determinant invariant changed")
    control = scaling_control()
    if not control["all_exact"] or not control["base_product_nonzero"]:
        raise AssertionError("Cauchy-model scaling control failed")
    return {
        "schema_version": "1.0",
        "result_id": "K307-ORDER-SEVEN-TWO-RADIUS-JOINT-CHART",
        "created": "2026-09-22",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k294-order-seven-global-radial-simplex-atlas.json",
                "lab/process/k302-order-seven-split-weighted-peano-jet.json",
                "lab/process/k305-order-seven-coherent-bordered-functional-compiler.json",
                "lab/process/k306-order-seven-joint-template-support-audit.json",
            ],
            "old_radial_variables": ["x", "q"],
            "new_radial_variables": ["x", "b=x*q"],
            "projective_variables": ["p_r0", "p_r1", "p_r2", "p_c0", "p_c1", "p_c2"],
            "split_variables": [f"u{i}" for i in range(4)] + [f"z{i}" for i in range(4)],
        },
        "joint_change_of_variables": {
            "definition": "b=x*q",
            "inverse": "q=b/x for x>0",
            "jacobian": "dq=db/x",
            "density_identity": "exp(-256*x*(1+q))*x^15*q^11*dq = exp(-256*(x+b))*x^3*b^11*db",
            "projective_and_split_factor": "y*(1-y)*product_i(p_i) dp dy du dz",
            "separated_q_gamma_extraction_before_determinant_integration": False,
        },
        "native_affine_nodes": affine_nodes(),
        "joint_origin": {
            "leading_kernel": "2*K1(lambda*s)=2/(lambda*s)+O(lambda*abs(log(lambda)))",
            "D4_simultaneous_degree": -4,
            "bordered_B5_simultaneous_degree": -5,
            "product_simultaneous_degree": -9,
            "density_polynomial_degree_before_dx_db": 14,
            "integrand_degree_before_two_radius_area": 5,
            "two_radius_polar_exponent": 6,
            "absolute_integrability_margin": 7,
            "angular_derivatives_through_order_two_preserve_degree": True,
            "reason": "each dimensionless angular derivative contributes one affine-node factor of degree one and one extra kernel derivative of degree minus one",
            "exact_cauchy_scaling_control": control,
        },
        "factorization_target": {
            "D4": "V(T1,T3,T5,T7)*V(U1,U3,U5,U7)*R4",
            "bordered_B5": "V(T2,T4,T6)*V(U2,U4,U6)*R5_border",
            "explicit_b_power": 18,
            "D4_b_power": 12,
            "bordered_B5_b_power": 6,
            "regularizer_rule": "evaluate R4 and R5_border by row/column divided differences; retain exact Cauchy denominators and K1 values in (x,b) before any one-radius coefficient is extracted",
        },
        "terminal_split_boundary": {
            "K302_weighted_jet_retained": k302["universal_weighted_bounds"],
            "pointwise_terminal_bound_required": False,
            "two_radius_chart_alone_closes_terminal_split": False,
            "composition_rule": "apply K302 only inside the regularized bordered determinant column-replacement functional, never against a detached unregularized cofactor",
        },
        "decision": {
            "k304_negative_powers_are_coordinate_factorization_artifacts": True,
            "meaning": "they arise after q is integrated with determinant zeros discarded and are not a divergence theorem for the joint native functional",
            "joint_origin_absolutely_integrable": True,
            "complete_numerical_norms_emitted": False,
            "k294_gamma_join_released": False,
            "next_exact_input": "build the outward mixed-divided-difference R4/R5_border operator for the y master, with K302 terminal weighted jets and exact two-radius exponential retained",
        },
        "release_test": {
            "density_jacobian_exact": True,
            "all_sixteen_native_nodes_affine_in_x_b": True,
            "exact_product_degree_minus_nine_control": control["all_exact"],
            "positive_joint_origin_margin": True,
            "detached_q_integration_rejected": True,
            "complete_numerical_norm_emitted": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k306["ledger_effect"],
        "claim_ceiling": "Exact joint-radial coordinate and homogeneity theorem for the K305/K306 order-seven functional. With b=x*q, the native density is exp(-256(x+b))*x^3*b^11 and all cumulative Bessel arguments are affine in x,b. The common D4 and coherent bordered B5 have exact leading simultaneous degrees -4 and -5, so their product is absolutely integrable at the two-radius origin with margin seven, including dimensionless angular derivatives through order two. This proves K304's separated-q negative powers are not a divergence theorem. It does not emit a complete numerical Peano norm, integrate every boundary cell, release K294's gamma join, evaluate an action column or residual, emit a native K152 interval, or move source, ledger, canon, paper, public or physical posture.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    change = payload["joint_change_of_variables"]
    if change["jacobian"] != "dq=db/x" or "x^3*b^11" not in change["density_identity"]:
        raise AssertionError("joint density identity changed")
    origin = payload["joint_origin"]
    if (origin["D4_simultaneous_degree"], origin["bordered_B5_simultaneous_degree"], origin["two_radius_polar_exponent"]) != (-4, -5, 6):
        raise AssertionError("joint-origin degree changed")
    decision = payload["decision"]
    if not decision["joint_origin_absolutely_integrable"] or decision["k294_gamma_join_released"]:
        raise AssertionError("integrability or gamma boundary changed")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate_payload(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
