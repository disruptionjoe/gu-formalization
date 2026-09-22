#!/usr/bin/env python3
"""Build the exact positive Duffy--Peano rule released by K298."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K294 = ROOT / "lab/process/k294-order-seven-global-radial-simplex-atlas.json"
K298 = ROOT / "lab/process/k298-order-seven-coherent-terminal-corner-obstruction.json"
OUTPUT = ROOT / "lab/process/k299-order-seven-positive-peano-simplex-rule.json"

GAPS = ["r0", "r1", "r2", "c0", "c1", "c2"]


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def duffy_rows() -> list[dict[str, Any]]:
    rows = []
    for index in range(5):
        n = 5 - index
        mean = Fraction(1, n + 1)
        rows.append(
            {
                "axis": f"t{index}",
                "gap_order": GAPS,
                "weight": f"(1-t)^{n - 1}",
                "weight_exponent": n - 1,
                "weight_integral": q(Fraction(1, n)),
                "weighted_mean": q(mean),
                "peano_kernel": {
                    "for_s_le_mean": f"(1-s)^{n + 1}/({n}*{n + 1})-(1/{n})*({q(mean)}-s)",
                    "for_s_ge_mean": f"(1-s)^{n + 1}/({n}*{n + 1})",
                    "nonnegative": True,
                    "endpoint_zero_orders": {"s=0": 2, "s=1": n + 1},
                    "integral": q(Fraction(1, 2 * (n + 1) ** 2 * (n + 2))),
                },
                "maximum_derivative_order": 2,
            }
        )
    rows.append(
        {
            "axis": "y",
            "gap_order": GAPS,
            "weight": "1",
            "weight_exponent": 0,
            "weight_integral": "1",
            "weighted_mean": "1/2",
            "peano_kernel": {
                "for_s_le_mean": "s^2/2",
                "for_s_ge_mean": "(1-s)^2/2",
                "nonnegative": True,
                "endpoint_zero_orders": {"s=0": 2, "s=1": 2},
                "integral": "1/24",
            },
            "maximum_derivative_order": 2,
        }
    )
    return rows


def barycenter() -> list[Fraction]:
    remaining = Fraction(1)
    point = []
    for index in range(5):
        mean = Fraction(1, 6 - index)
        point.append(remaining * mean)
        remaining *= 1 - mean
    point.append(remaining)
    return point


def build() -> dict[str, Any]:
    k294 = json.loads(K294.read_text())
    k298 = json.loads(K298.read_text())
    rows = duffy_rows()
    point = barycenter()
    simplex_weight = Fraction(1)
    for n in range(5, 0, -1):
        simplex_weight *= Fraction(1, n)
    return {
        "schema_version": "1.0",
        "result_id": "K299-ORDER-SEVEN-POSITIVE-PEANO-SIMPLEX-RULE",
        "created": "2026-09-22",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k294-order-seven-global-radial-simplex-atlas.json",
                "lab/process/k298-order-seven-coherent-terminal-corner-obstruction.json",
            ],
            "gap_order": GAPS,
            "simplex_dimension": 5,
            "angular_dimension_with_y": 6,
            "native_projective_weight_kept_inside_integrand": True,
            "maximum_derivative_order": 2,
        },
        "duffy_chart": {
            "definition": "p_j=t_j*product_{i<j}(1-t_i) for j<5; p_5=product_{i<5}(1-t_i)",
            "inverse_order": GAPS,
            "jacobian": "product_{j=0}^4 (1-t_j)^(4-j)",
            "factor_exponents": [4, 3, 2, 1, 0],
            "a.e._bijection": True,
            "measure_zero_tie_boundary": "ordinary Duffy cube boundary",
        },
        "one_dimensional_factors": rows,
        "positive_cubature": {
            "simplex_node": [q(value) for value in point],
            "y_node": "1/2",
            "simplex_weight": q(simplex_weight),
            "angular_weight": q(simplex_weight),
            "node_count": 1,
            "all_weights_strictly_positive": simplex_weight > 0,
            "simplex_volume_replayed": simplex_weight == Fraction(1, 120),
            "barycenter_replayed": point == [Fraction(1, 6)] * 6,
            "separately_affine_exact": True,
        },
        "peano_remainder": {
            "one_axis_identity": "I_n[h]-I_n[1]*h(mu_n)=integral_0^1 K_n(s)*h''(s) ds, with I_n[h]=integral_0^1 (1-t)^(n-1)h(t)dt and mu_n=1/(n+1)",
            "tensor_identity": "I_0...I_5-Q_0...Q_5=sum_j Q_0...Q_(j-1)(I_j-Q_j)I_(j+1)...I_5",
            "absolute_bound": "replace every signed Peano integrand by K_j(s)*abs(partial_j^2 F) and retain the positive earlier-node weights and later-axis integrals",
            "maximum_derivative_order": 2,
            "mixed_derivatives_required": False,
            "duffy_axis_affinity": "each p_i is affine in any one t_j with the other t coordinates fixed, so partial_tj^2 is the corresponding Hessian directional derivative with no second-chart-derivative term",
            "positive_kernel_on_every_axis": all(row["peano_kernel"]["nonnegative"] for row in rows),
        },
        "controls": {
            "constant_integral": q(simplex_weight),
            "sum_p_squared_integral": "1/420",
            "sum_p_squared_rule_value": "1/720",
            "sum_p_squared_error": "1/1008",
            "y_squared_times_simplex_integral": "1/360",
            "y_squared_rule_value": "1/480",
            "y_squared_error": "1/1440",
        },
        "decision": {
            "k298_fourth_derivative_route_reused": False,
            "positive_rule_requires_at_most_third_derivatives": True,
            "positive_rule_actual_maximum_derivative_order": 2,
            "face_integrability_proved": False,
            "complete_global_derivative_norm_computed": False,
            "radial_gamma_composition_released": False,
            "next_exact_input": "push the six exact tensor Peano terms through the complete K296/K297 face atlas, keeping y last, and compare the resulting global second-directional-derivative norm obligation with analytic terminal subtraction",
        },
        "release_test": {
            "k294_simplex_dimension_replayed": len(k294["fixed_control"]["native_gap_coordinates"]) - 1 == 5,
            "k298_requires_method_switch": not k298["decision"]["global_fourth_derivative_jacobi_route_legal"],
            "single_positive_barycentric_node": point == [Fraction(1, 6)] * 6 and simplex_weight > 0,
            "all_peano_kernels_nonnegative": all(row["peano_kernel"]["nonnegative"] for row in rows),
            "derivative_order_below_k298_obstruction": 2 < 4,
            "complete_exterior_integrand_bound_emitted": False,
            "complete_base_action_column_evaluated": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k298["ledger_effect"],
        "claim_ceiling": "Exact positive one-node Duffy cubature and tensor Peano remainder for the K294 five-simplex times y interval, with the complete native projective weight retained inside the integrand. The rule samples the simplex barycenter and y=1/2 with weight 1/120 and requires only six pure second directional derivatives. Face integrability, a numerical global derivative norm, radial gamma composition, exterior action-column value, residual, native K152 interval, source/ledger move, canon, paper or public claim are not established here.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    rendered = json.dumps(build(), indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
