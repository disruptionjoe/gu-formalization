#!/usr/bin/env python3
"""Build endpoint-safe scaled Bessel jets for the K318 charts.

Raw K_nu evaluation is not legal on an interval containing zero.  The chart
weights supply exactly the powers needed to replace those raw calls by
Phi_m(w)=w^(m+1)*(2*K1)^(m)(w), m=0,1,2.  These functions have continuous
zero limits and can be inserted by row/column scaling before the complete
bordered determinant is enclosed.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Any

from flint import arb, ctx


ROOT = Path(__file__).resolve().parents[2]
K302 = ROOT / "lab/process/k302-order-seven-split-weighted-peano-jet.json"
K315 = ROOT / "lab/process/k315-order-seven-terminal-bordered-adapter.json"
K318 = ROOT / "lab/process/k318-order-seven-weighted-endpoint-blowup-atlas.json"
K319 = ROOT / "lab/process/k319-order-seven-weighted-chart-composition.json"
OUTPUT = ROOT / "lab/process/k320-order-seven-scaled-endpoint-bessel-bank.json"

ctx.dps = 120
ctx.threads = 1


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    total = Fraction(0)
    for permutation in itertools.permutations(range(len(matrix))):
        inversions = sum(
            permutation[i] > permutation[j]
            for i in range(len(permutation))
            for j in range(i + 1, len(permutation))
        )
        term = Fraction(-1 if inversions % 2 else 1)
        for row, column in enumerate(permutation):
            term *= matrix[row][column]
        total += term
    return total


def determinant_scaling_control() -> dict[str, Any]:
    matrix = [
        [Fraction(2), Fraction(3), Fraction(5), Fraction(7), Fraction(11)],
        [Fraction(13), Fraction(17), Fraction(19), Fraction(23), Fraction(29)],
        [Fraction(31), Fraction(37), Fraction(41), Fraction(43), Fraction(47)],
        [Fraction(53), Fraction(59), Fraction(61), Fraction(67), Fraction(71)],
        [Fraction(73), Fraction(79), Fraction(83), Fraction(89), Fraction(97)],
    ]
    lam = Fraction(5, 7)
    omega = Fraction(11, 13)
    base = determinant(matrix)
    left = [row[:] for row in matrix]
    for row in range(5):
        left[row][3] *= lam
        left[row][4] *= omega
    right = [row[:] for row in matrix]
    for column in range(5):
        right[4][column] *= omega
    for row in range(5):
        right[row][3] *= lam
    return {
        "base_determinant": str(base),
        "lambda": str(lam),
        "omega": str(omega),
        "left_column_scaling_exact": determinant(left) == lam * omega * base,
        "right_row_column_scaling_exact": determinant(right) == lam * omega * base,
        "left_rule": "scale terminal column 3 by lambda and left endpoint border column 4 by omega",
        "right_rule": "scale terminal column 3 by lambda and bottom border row 4 by omega",
    }


def scaled_values(w_text: str) -> dict[str, Any]:
    w = arb(w_text)
    k0 = w.bessel_k(0)
    k1 = w.bessel_k(1)
    k2 = w.bessel_k(2)
    k3 = w.bessel_k(3)
    A = w * k1
    B = w * k0
    formulas = [
        2 * A,
        -2 * (A + w * B),
        4 * A + 2 * w * B + 2 * w * w * A,
    ]
    recurrence = [
        w * (2 * k1),
        w * w * (-(k0 + k2)),
        w * w * w * ((3 * k1 + k3) / 2),
    ]
    differences = [left - right for left, right in zip(formulas, recurrence)]
    return {
        "w": w_text,
        "formula_intervals": [str(value) for value in formulas],
        "recurrence_intervals": [str(value) for value in recurrence],
        "identity_differences_contain_zero": [value.contains(0) for value in differences],
        "midpoints": [float(value.mid()) for value in formulas],
    }


def terminal_census(k315: dict[str, Any]) -> tuple[Counter[int], Counter[int]]:
    all_orders: Counter[int] = Counter()
    second_orders: Counter[int] = Counter()
    for family in k315["complete_column_replacement_expansion"]:
        derivative_order = sum(family["column_orders"])
        for order, count in family["terminal_jet_histogram"].items():
            weighted = count * family["outer_multiplicity"]
            all_orders[int(order)] += weighted
            if derivative_order == 2:
                second_orders[int(order)] += weighted
    return all_orders, second_orders


def build() -> dict[str, Any]:
    k302 = json.loads(K302.read_text())
    k315 = json.loads(K315.read_text())
    k318 = json.loads(K318.read_text())
    k319 = json.loads(K319.read_text())
    if not k318["decision"]["sixteen_determinant_preserving_endpoint_charts_implemented"]:
        raise AssertionError("K318 endpoint atlas unavailable")
    if not k319["decision"]["complete_weighted_chart_obligation_compiler_implemented"]:
        raise AssertionError("K319 family compiler unavailable")
    controls = [scaled_values(value) for value in ("1", "1/4", "1/16", "1/256")]
    if not all(all(row["identity_differences_contain_zero"]) for row in controls):
        raise AssertionError("scaled Bessel identities failed")
    limits = [2.0, -2.0, 4.0]
    final_midpoints = controls[-1]["midpoints"]
    if any(abs(value - target) > 0.001 for value, target in zip(final_midpoints, limits)):
        raise AssertionError("scaled endpoint control did not approach its zero limit")
    determinant_control = determinant_scaling_control()
    if not determinant_control["left_column_scaling_exact"] or not determinant_control["right_row_column_scaling_exact"]:
        raise AssertionError("determinant scaling identity failed")
    all_orders, second_orders = terminal_census(k315)
    power_rows = [
        {
            "terminal_jet_order": order,
            "all_weighted_terminal_monomials": all_orders[order],
            "second_family_weighted_terminal_monomials": second_orders[order],
            "remaining_endpoint_power": 2 - order,
            "remaining_power_nonnegative": 2 - order >= 0,
            "aligned_chart_scaled_entry": f"D^{order}*Phi_{order}(w)/H^{order + 1}",
        }
        for order in (0, 1, 2)
    ]

    return {
        "schema_version": "1.0",
        "result_id": "K320-ORDER-SEVEN-SCALED-ENDPOINT-BESSEL-BANK",
        "created": "2026-09-22",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k302-order-seven-split-weighted-peano-jet.json",
                "lab/process/k315-order-seven-terminal-bordered-adapter.json",
                "lab/process/k318-order-seven-weighted-endpoint-blowup-atlas.json",
                "lab/process/k319-order-seven-weighted-chart-composition.json",
            ],
            "arb_decimal_digits": 120,
            "threads": 1,
            "terminal_jet_orders": [0, 1, 2],
            "K318_endpoint_charts": k318["determinant_preserving_endpoint_atlas"]["chart_count"],
        },
        "scaled_bessel_bank": {
            "definition": "Phi_m(w)=w^(m+1)*(2*K1)^(m)(w)",
            "auxiliary_functions": {"A": "w*K1(w)", "B": "w*K0(w)"},
            "exact_formulas": {
                "Phi_0": "2*A",
                "Phi_1": "-2*(A+w*B)",
                "Phi_2": "4*A+2*w*B+2*w^2*A",
            },
            "zero_limits": {"Phi_0": 2, "Phi_1": -2, "Phi_2": 4},
            "limit_basis": "A(w)->1, B(w)->0 and w^2*A(w)->0 as w->0+",
            "positive_argument_arb_controls": controls,
            "every_identity_control_contains_zero": all(all(row["identity_differences_contain_zero"]) for row in controls),
            "smallest_scale_within_one_mill": all(abs(value - target) <= 0.001 for value, target in zip(final_midpoints, limits)),
        },
        "old_endpoint_log_removal": {
            "factor": "F_x(y)=2*y*K1(x*y), w=x*y",
            "exact_second_derivative": "F_x''(y)=2*x*(A(w)-K0(w))",
            "Peano_weighted_identity": "K(y)*F_x''(y)=(w^2*A(w)-w*B(w))/x on y<=1/2",
            "pointwise_logarithm_subtracted": False,
            "scaled_expression_continuous_at_zero": True,
        },
        "determinant_scaling": {
            **determinant_control,
            "aligned_terminal_argument": "w=x*rho*sigma*H with H>=1/2",
            "terminal_row_or_column_scale": "x*rho*sigma^(m+1) for terminal jet order m",
            "weighted_determinant_identity": "x^3*K*J*det(B_m)=x^2*sigma^(2-m)*det(B_m_tilde)/16, with an additional theta^2 on the second aligned Hepp chart",
            "complete_determinant_retained": True,
            "permutation_or_monomial_absolute_values_used": False,
        },
        "terminal_power_census": {
            "rows": power_rows,
            "all_orders_exact": {str(key): value for key, value in sorted(all_orders.items())},
            "second_family_orders_exact": {str(key): value for key, value in sorted(second_orders.items())},
            "all_remaining_endpoint_powers_nonnegative": all(row["remaining_power_nonnegative"] for row in power_rows),
            "K302_role": "domination cross-check only; never multiply B_m by a detached remaining-entry coefficient",
        },
        "decision": {
            "endpoint_safe_scaled_Bessel_bank_implemented": True,
            "raw_Bessel_evaluation_at_zero_required": False,
            "all_terminal_jet_orders_have_continuous_scaled_entries": True,
            "radial_projective_weighted_join_complete": False,
            "complete_chart_determinant_uppers_emitted": False,
            "complete_y_master_constant_emitted": False,
            "five_gap_axis_transfer_released": False,
            "k294_gamma_join_released": False,
            "next_exact_input": "tensor the scaled endpoint entries with K310's r,s compactification and K314's projective face zeros, then implement outward complete-determinant bounds on the weighted charts before summing the y master",
        },
        "release_test": {
            "Phi_limits_exactly_2_minus2_4": True,
            "positive_scale_controls_pass": True,
            "determinant_scaling_exact": determinant_control["left_column_scaling_exact"] and determinant_control["right_row_column_scaling_exact"],
            "K315_all_terminal_histogram_replayed": all_orders == Counter({0: 378, 1: 162, 2: 18}),
            "K315_second_terminal_histogram_replayed": second_orders == Counter({0: 288, 1: 144, 2: 18}),
            "minimum_remaining_endpoint_power": min(row["remaining_endpoint_power"] for row in power_rows),
            "complete_numerical_norm_overclaim": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k319["ledger_effect"],
        "source_routing": k319["source_routing"],
        "claim_ceiling": "Endpoint-safe scaled Bessel bank through terminal jet order two for K318/K319. Phi_0, Phi_1 and Phi_2 have exact A/B formulas and continuous zero limits 2,-2,4; exact determinant row/column scaling keeps the split and Peano powers inside the complete bordered assembly; and every K315 terminal occurrence retains nonnegative endpoint power 2-m. This removes raw zero-touching K_nu evaluation but does not complete the r/s radial-projective join, emit complete chart determinant uppers, a numerical y-master constant, five-axis transfer, K294 join, action-column value, residual, K152 interval, source/ledger, canon, paper, public or physical claim.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    bank = payload["scaled_bessel_bank"]
    if bank["zero_limits"] != {"Phi_0": 2, "Phi_1": -2, "Phi_2": 4}:
        raise AssertionError("scaled Bessel zero limits changed")
    if not bank["every_identity_control_contains_zero"] or not bank["smallest_scale_within_one_mill"]:
        raise AssertionError("scaled Bessel controls failed")
    scaling = payload["determinant_scaling"]
    if not scaling["left_column_scaling_exact"] or not scaling["right_row_column_scaling_exact"]:
        raise AssertionError("determinant scaling identity lost")
    if not scaling["complete_determinant_retained"] or scaling["permutation_or_monomial_absolute_values_used"]:
        raise AssertionError("complete determinant assembly lost")
    census = payload["terminal_power_census"]
    if census["all_orders_exact"] != {"0": 378, "1": 162, "2": 18}:
        raise AssertionError("complete terminal census changed")
    if census["second_family_orders_exact"] != {"0": 288, "1": 144, "2": 18}:
        raise AssertionError("second-family terminal census changed")
    if not census["all_remaining_endpoint_powers_nonnegative"]:
        raise AssertionError("negative endpoint power introduced")
    decision = payload["decision"]
    if decision["raw_Bessel_evaluation_at_zero_required"] or decision["radial_projective_weighted_join_complete"]:
        raise AssertionError("endpoint or radial-projective posture changed")
    if decision["complete_y_master_constant_emitted"] or decision["five_gap_axis_transfer_released"]:
        raise AssertionError("downstream numerical release overclaimed")


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
