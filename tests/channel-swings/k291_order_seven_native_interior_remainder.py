#!/usr/bin/env python3
"""K291 composition of K286 with the K290 native rest-factor bank."""

from __future__ import annotations

import argparse
import json
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K284_MANIFEST = ROOT / "lab/process/k284-order-seven-transverse-shape-atlas.json"
K286_MANIFEST = ROOT / "lab/process/k286-order-seven-mixed-shape-derivative-bank.json"
K287_MANIFEST = ROOT / "lab/process/k287-order-seven-tensor-jacobi-remainder.json"
K290_MANIFEST = ROOT / "lab/process/k290-order-seven-native-rest-derivative-bank.json"
OUTPUT = ROOT / "lab/process/k291-order-seven-native-interior-remainder.json"
getcontext().prec = 100


def d(value: Any) -> Decimal:
    return Decimal(str(value))


def build() -> dict[str, Any]:
    k284 = json.loads(K284_MANIFEST.read_text())
    k286 = json.loads(K286_MANIFEST.read_text())
    k287 = json.loads(K287_MANIFEST.read_text())
    k290 = json.loads(K290_MANIFEST.read_text())
    regularizer = [d(k284["transverse_shape_atlas"]["maximum_R_upper"])]
    regularizer += [
        d(k286["mixed_shape_derivative_bank"]["global_componentwise_mixed_derivative_abs_upper"][str(order)])
        for order in range(1, 5)
    ]
    radius = Fraction(k284["fixed_control"]["transverse_shape_radius"])
    h = Decimal(radius.numerator) / Decimal(radius.denominator)
    group_rows = []
    total_fourth = Decimal(0)
    for group in k290["coherent_group_bank"]:
        rest = [d(value) for value in group["componentwise_mixed_derivative_abs_upper"]]
        contributions = [
            Decimal(math_comb(4, split)) * regularizer[split] * rest[4 - split]
            for split in range(5)
        ]
        fourth = sum(contributions)
        total_fourth += fourth
        group_rows.append(
            {
                "group_id": group["group_id"],
                "regularizer_derivative_order_contributions": {
                    str(split): str(value) for split, value in enumerate(contributions)
                },
                "complete_fourth_shape_derivative_abs_upper": str(fourth),
                "dominant_product_rule_split": max(range(5), key=lambda index: contributions[index]),
            }
        )
    one_axis = h**4 * total_fourth / Decimal(270)
    tensor_average = Decimal(6) * one_axis
    shape_volume = (Decimal(2) * h) ** 6
    local_shape_integral = shape_volume * tensor_average
    x_width = Decimal(1) / Decimal(256)
    x_integrated = x_width * local_shape_integral
    factor_rows = k290["derivative_bank"]["factor_componentwise_mixed_derivative_abs_upper"]
    factor_fourths = {name: d(values[4]) for name, values in factor_rows.items()}
    dominant_factor = max(factor_fourths, key=factor_fourths.get)
    return {
        "schema_version": "1.0",
        "result_id": "K291-ORDER-SEVEN-NATIVE-INTERIOR-REMAINDER",
        "created": "2026-09-21",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "tube_manifest": "lab/process/k284-order-seven-transverse-shape-atlas.json",
            "regularizer_derivative_manifest": "lab/process/k286-order-seven-mixed-shape-derivative-bank.json",
            "proxy_remainder_manifest": "lab/process/k287-order-seven-tensor-jacobi-remainder.json",
            "native_rest_manifest": "lab/process/k290-order-seven-native-rest-derivative-bank.json",
            "shape_coordinate_count": 6,
            "maximum_derivative_order": 4,
            "coherent_groups": len(group_rows),
            "transverse_shape_radius": str(radius),
            "nodes_per_axis": 2,
        },
        "composition_rule": {
            "group_product": "D^4(R4*G)=sum_{j=0}^4 binom(4,j) D^j R4 D^(4-j)G with every labelled allocation retained in K286 and K290",
            "group_before_global_absolute_value": True,
            "positive_tensor_telescope": "six times the normalized one-axis two-node Gauss-Legendre remainder h^4*M4/270",
            "native_density_location": "K290 G already includes (2*pi)^-9 exp(-256*x*L) x^15 y(1-y) product(r_i c_i)",
        },
        "coherent_group_composition": group_rows,
        "native_density_remainder": {
            "complete_four_group_fourth_shape_derivative_abs_upper": str(total_fourth),
            "one_axis_normalized_shape_average_abs_upper": str(one_axis),
            "six_axis_normalized_shape_average_abs_upper": str(tensor_average),
            "single_shape_box_volume": str(shape_volume),
            "single_shape_box_integral_abs_upper": str(local_shape_integral),
            "x_interval_width": str(x_width),
            "single_center_box_x_y_u_z_integrated_abs_upper": str(x_integrated),
            "y_u_z_domain_volume": "1",
            "complete_native_tube_integral_emitted": False,
            "reason": "K284 certifies overlapping t-centered shape boxes but does not supply a disjoint native dr dc atlas or multiplicity rule",
        },
        "dominance": {
            "factor_order_four_abs_uppers": {name: str(value) for name, value in factor_fourths.items()},
            "largest_raw_factor_order_four_bound": dominant_factor,
            "group_product_rule_dominant_regularizer_derivative_order": group_rows[0]["dominant_product_rule_split"],
            "interpretation": "This is a dominance diagnosis for the conservative majorant, not a lower bound or proof that a sharper weighted/correlated rule must fail.",
        },
        "comparison_with_k287": {
            "k287_normalized_regularizer_only_six_axis_error": k287["remainder"]["six_axis_normalized_tube_average_abs_upper"],
            "k291_includes_native_density_and_all_four_coherent_groups": True,
            "direct_ratio_meaningful": False,
            "reason": "K287 integrates only R4 against a normalized uniform shape measure, while K291 bounds the complete density-weighted coherent integrand pointwise in x,y,u,z.",
        },
        "decision": {
            "numerical_remainder_valid": False,
            "correction": "Superseded because the K290 pointwise companion derivative bank is not uniform on the native split cube; see K301/K302.",
            "native_density_weighted_local_shape_remainder_serialized": True,
            "complete_native_tube_remainder_serialized": False,
            "action_column_ready": False,
            "next_exact_input": "construct a disjoint native dr dc atlas for the K284 union and replace the dominant endpoint/product majorant by a split-corner weighted rule before radial or projective-gap exterior composition",
        },
        "release_test": {
            "k286_and_k290_complete_fourth_order_product_rule_composed": True,
            "all_four_coherent_groups_composed": len(group_rows) == 4,
            "positive_six_axis_tensor_remainder_applied": True,
            "native_density_included": True,
            "disjoint_native_tube_atlas_serialized": False,
            "complete_arbitrary_gap_ratio_domain_covered": False,
            "complete_base_action_column_evaluated": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k290["ledger_effect"],
        "correction": {
            "id": "K290-SPLIT-BOUNDARY-20260922",
            "status": "superseded",
            "reason": "The inherited K290 pointwise derivative ceiling is invalid at the terminal native split face.",
            "replacement": "lab/process/k302-order-seven-split-weighted-peano-jet.json",
        },
        "claim_ceiling": "Superseded numerical local remainder retained for history only; K301 invalidates its K290 uniform input. K302 repairs the Peano-weighted split jet but does not reinstate this fourth-order two-node number.",
    }


def math_comb(n: int, k: int) -> int:
    result = 1
    for index in range(1, k + 1):
        result = result * (n - index + 1) // index
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
