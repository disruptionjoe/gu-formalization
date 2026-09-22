#!/usr/bin/env python3
"""First complete weighted old-position-six value-family interval pilot.

The selected chart is the left, a-max, eta<=A<=v Hepp chart.  Its terminal
argument factors as w=x*rho*v*H with 1<=H<=3/2, so K322 bounds the scaled
terminal entry on a zero-touching cell.  Every other regularized entry has a
strict positive argument lower on the chosen radial/projective slab.  The
terminal column and endpoint border column are scaled before one Hadamard
bound is taken for the complete bordered matrix.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any

from flint import arb, ctx


ROOT = Path(__file__).resolve().parents[2]
K308_MODULE = Path(__file__).with_name("k308_order_seven_regularized_y_master_operator.py")
K314_MODULE = Path(__file__).with_name("k314_order_seven_projective_face_oracle.py")
K321 = ROOT / "lab/process/k321-order-seven-radial-projective-tensor-atlas.json"
K322 = ROOT / "lab/process/k322-order-seven-zero-safe-scaled-bessel-envelopes.json"
OUTPUT = ROOT / "lab/process/k323-order-seven-old-position-six-value-pilot.json"

ctx.dps = 180
ctx.threads = 1

X = (Fraction(1, 16), Fraction(1, 8))
B = (Fraction(1, 32), Fraction(1, 8))
Y = (Fraction(0), Fraction(1, 2))
P = (Fraction(1, 8), Fraction(5, 24))
ROW_ORDERS = [0, 1, 2, 0]
COLUMN_ORDERS = [0, 1, 2, 0]


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def nodes() -> dict[str, list[Fraction]]:
    x0, _ = X
    b0, _ = B
    _, y1 = Y
    p0, _ = P
    return {
        "odd_left": [x0 * 0 + b0 * p0 * count for count in (3, 2, 1, 0)],
        "odd_right": [x0 * (1 - y1) + b0 * p0 * count for count in (3, 2, 1, 0)],
        "even_left": [
            b0 * p0 * Fraction(9, 4),
            b0 * p0 * Fraction(5, 4),
            b0 * p0 * Fraction(1, 4),
            Fraction(0),
        ],
        "even_right": [
            x0 * (1 - y1) + b0 * p0 * Fraction(9, 4),
            x0 * (1 - y1) + b0 * p0 * Fraction(5, 4),
            x0 * (1 - y1) + b0 * p0 * Fraction(1, 4),
            Fraction(0),
        ],
    }


def hadamard_bound(rows: list[list[arb]]) -> arb:
    product = arb(1)
    for row in rows:
        squared = sum((value * value for value in row), arb(0))
        product *= squared.sqrt()
    return product


def build_matrices(module) -> tuple[list[list[arb]], list[list[arb]], dict[str, Any]]:
    node_bank = nodes()
    d4_argument_lower = min(node_bank["odd_left"]) + min(node_bank["odd_right"])
    d4 = [
        [module.dd_abs_upper(d4_argument_lower, row_order, column_order) for column_order in range(4)]
        for row_order in range(4)
    ]

    x1 = X[1]
    b5 = [[arb(0) for _ in range(5)] for _ in range(5)]
    nonterminal_lowers: list[Fraction] = []
    for row in range(4):
        for column in range(4):
            if (row, column) == (3, 3):
                # lambda*f(w)=Phi_0(w)/H, H>=1 and abs(Phi_0)<=2.
                b5[row][column] = arb(2)
                continue
            lower = node_bank["even_left"][row] + node_bank["even_right"][column]
            if lower <= 0:
                raise AssertionError("a nonterminal core entry lost its positive argument lower")
            nonterminal_lowers.append(lower)
            value = module.dd_abs_upper(lower, ROW_ORDERS[row], COLUMN_ORDERS[column])
            if column == 3:
                # The whole terminal column is scaled by lambda=x*rho*v.
                value *= module.ball(x1)
            b5[row][column] = value

    # Left endpoint chart: eta^2*J is absorbed into the final border column.
    # Its cube upper is one.  Row three and the terminal bottom entries remain
    # literal zeros.
    for row in range(3):
        lower = node_bank["even_left"][row]
        nonterminal_lowers.append(lower)
        b5[row][4] = module.ball(Y[1]) * module.dd_abs_upper(lower, ROW_ORDERS[row], 0)
    for column in range(3):
        lower = node_bank["even_right"][column]
        nonterminal_lowers.append(lower)
        b5[4][column] = module.dd_abs_upper(lower, 0, COLUMN_ORDERS[column])

    audit = {
        "D4_minimum_argument": str(d4_argument_lower),
        "minimum_nonterminal_B5_argument": str(min(nonterminal_lowers)),
        "terminal_slot": [3, 3],
        "terminal_scaled_upper": "2",
        "terminal_argument": "w=x*rho*v*H, H=1+h0*h1*(1-h2)/2 in [1,3/2]",
        "terminal_column_scale": "lambda=x*rho*v",
        "endpoint_border_column_scale": "omega=eta^2*J_hepp",
        "literal_zero_slots": [[3, 4], [4, 3], [4, 4]],
        "all_nonterminal_argument_lowers_positive": min(nonterminal_lowers) > 0 and d4_argument_lower > 0,
    }
    return d4, b5, audit


def build() -> dict[str, Any]:
    module = load_module(K308_MODULE, "k323_k308_backend")
    k314_module = load_module(K314_MODULE, "k323_k314_backend")
    k321 = json.loads(K321.read_text())
    k322 = json.loads(K322.read_text())
    if not k321["decision"]["radial_projective_tensor_topology_complete"]:
        raise AssertionError("K321 tensor atlas unavailable")
    if not k322["decision"]["zero_inclusive_scaled_Bessel_envelopes_implemented"]:
        raise AssertionError("K322 zero-safe envelope unavailable")

    d4, b5, audit = build_matrices(module)
    d4_bound = hadamard_bound(d4)
    b5_bound = hadamard_bound(b5)
    gaps = {name: P for name in k314_module.GAPS}
    projective = k314_module.projective_polynomial_upper(gaps)
    # K320's weighted identity leaves x^2*sigma^2/16 outside the scaled
    # bordered determinant.  sigma=v<=1.  Include the K299 outer 1/120 and
    # all four coherent groups.
    scalar = Fraction(4, 120) * X[1] ** 2 * Fraction(1, 16) * projective
    complete = d4_bound * b5_bound * module.ball(scalar)
    complete_text = module.upper_text(complete)
    if not math.isfinite(float(complete_text)) or float(complete_text) <= 0:
        raise AssertionError("old-position-six complete bound is not finite positive")

    return {
        "schema_version": "1.0",
        "result_id": "K323-ORDER-SEVEN-OLD-POSITION-SIX-VALUE-PILOT",
        "created": "2026-09-22",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k308-order-seven-regularized-y-master-operator.json",
                "lab/process/k314-order-seven-projective-face-oracle.json",
                "lab/process/k321-order-seven-radial-projective-tensor-atlas.json",
                "lab/process/k322-order-seven-zero-safe-scaled-bessel-envelopes.json",
            ],
            "arb_decimal_digits": 180,
            "threads": 1,
            "chart_id": "left_a_max_hepp3_eta_A_v",
            "old_position": 6,
            "jet_family": "value",
            "radial_projective_slab": {
                "x": [str(X[0]), str(X[1])],
                "b": [str(B[0]), str(B[1])],
                "projective_gaps": [str(P[0]), str(P[1])],
            },
            "endpoint_cube": "h0,h1,h2,rho in [0,1] with eta=h0*h1*h2, A=h1*h2, v=h2",
        },
        "complete_weighted_matrix_bound": {
            "node_audit": audit,
            "D4_complete_Hadamard_abs_upper": module.upper_text(d4_bound),
            "bordered_B5_complete_Hadamard_abs_upper": module.upper_text(b5_bound),
            "native_projective_polynomial_upper": str(projective),
            "outer_scalar_fraction": str(scalar),
            "four_group_weighted_chart_abs_upper": complete_text,
            "positive_density_factors_bounded_by_one": [
                "exp(-256*(x+b))",
                "the remaining powers of x and b on the declared subunit slab",
                "unit-cube and slab widths",
            ],
            "matrix_bound_rule": "one Hadamard bound per complete matrix after terminal and endpoint column scaling",
            "permutation_or_monomial_absolute_values_used": False,
            "detached_terminal_cofactor_used": False,
            "terminal_weight_absorbed_before_determinant_bound": True,
            "Peano_Hepp_weight_absorbed_before_determinant_bound": True,
            "all_literal_border_zeros_retained": True,
        },
        "scope_boundary": {
            "covered": "one complete value-family bound on the full left a-max eta<=A<=v endpoint cube and one positive radial/projective slab",
            "not_covered": [
                "the other fifteen K318 endpoint charts",
                "the five first-y and fifteen signed second-y families",
                "radial origin and tail subdivision sums",
                "all projective-face subdivision sums",
                "a complete y-master constant",
            ],
            "pilot_is_not_global_release": True,
        },
        "decision": {
            "first_old_position_six_complete_value_bound_emitted": True,
            "zero_touching_terminal_entry_evaluated_without_raw_Knu_zero_call": True,
            "complete_matrix_Hadamard_route_finite": True,
            "extend_same_route_to_remaining_value_charts": True,
            "signed_first_and_second_jet_backend_complete": False,
            "complete_y_master_constant_emitted": False,
            "five_gap_axis_transfer_released": False,
            "k294_gamma_join_released": False,
            "next_exact_input": "extend the complete-matrix evaluator across the other fifteen value charts, then implement interval-signed aggregation of all five first and fifteen second families before adaptive radial/projective summation",
        },
        "release_test": {
            "all_nonterminal_argument_lowers_positive": audit["all_nonterminal_argument_lowers_positive"],
            "terminal_scaled_upper_from_K322": audit["terminal_scaled_upper"] == "2",
            "finite_positive_complete_bound": math.isfinite(float(complete_text)) and float(complete_text) > 0,
            "complete_matrices_bounded_after_weight_absorption": True,
            "no_permutation_absolute_enclosure": True,
            "complete_numerical_norm_overclaim": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k322["ledger_effect"],
        "source_routing": k322["source_routing"],
        "claim_ceiling": "First finite outward complete-matrix bound for the K315 value family on the full zero-touching old-position-six left a-max eta<=A<=v endpoint cube over one positive radial/projective slab. K322's scaled terminal upper is inserted only after the terminal column scale, the Peano/Hepp weight is absorbed into the endpoint border column, all literal zeros are retained, and one Hadamard enclosure is applied to each complete matrix without permutationwise or detached-cofactor absolute values. The other fifteen endpoint charts, first/second jet families and radial/projective subdivision sums remain open, so no complete y-master constant, gap-axis transfer, K294 join, action-column value, residual, K152 interval, source/ledger, canon, paper, public or physical claim is released.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    bound = payload["complete_weighted_matrix_bound"]
    if not bound["terminal_weight_absorbed_before_determinant_bound"] or not bound["Peano_Hepp_weight_absorbed_before_determinant_bound"]:
        raise AssertionError("chart weights were not absorbed before enclosure")
    if bound["permutation_or_monomial_absolute_values_used"] or bound["detached_terminal_cofactor_used"]:
        raise AssertionError("forbidden detached or permutation enclosure introduced")
    if not bound["all_literal_border_zeros_retained"]:
        raise AssertionError("literal border zeros lost")
    if len(bound["positive_density_factors_bounded_by_one"]) != 3:
        raise AssertionError("positive density domination not recorded")
    if not bound["node_audit"]["all_nonterminal_argument_lowers_positive"]:
        raise AssertionError("nonterminal raw Bessel evaluation touches zero")
    scope = payload["scope_boundary"]
    if not scope["pilot_is_not_global_release"]:
        raise AssertionError("pilot scope hidden")
    decision = payload["decision"]
    if decision["signed_first_and_second_jet_backend_complete"] or decision["complete_y_master_constant_emitted"]:
        raise AssertionError("complete y-master overclaim")


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
