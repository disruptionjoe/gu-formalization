#!/usr/bin/env python3
"""Compile the exact determinant-preserving K299 second-derivative rules.

The compiler stops before numerical enclosure.  It records every outer
product-rule family and keeps determinant derivatives as column-replacement
determinants, so no Cauchy--Vandermonde face zero is discarded by a Leibniz
expansion into raw signed products.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K288 = ROOT / "lab/process/k288-order-seven-native-occurrence-measure.json"
K299 = ROOT / "lab/process/k299-order-seven-positive-peano-simplex-rule.json"
K302 = ROOT / "lab/process/k302-order-seven-split-weighted-peano-jet.json"
OUTPUT = ROOT / "lab/process/k303-order-seven-peano-determinant-compiler.json"


FACTORS = (
    "projective_native_weight",
    "left_endpoint_safe_old_kernel",
    "right_endpoint_safe_old_kernel",
    "size_four_bessel_determinant",
    "size_three_companion_determinant",
)
DETERMINANT_SIZES = {
    "size_four_bessel_determinant": 4,
    "size_three_companion_determinant": 3,
}
AXIS_FACTORS = {
    "t0": FACTORS,
    "t1": FACTORS,
    "t2": FACTORS,
    "t3": (
        "projective_native_weight",
        "right_endpoint_safe_old_kernel",
        "size_four_bessel_determinant",
        "size_three_companion_determinant",
    ),
    "t4": (
        "projective_native_weight",
        "right_endpoint_safe_old_kernel",
        "size_four_bessel_determinant",
        "size_three_companion_determinant",
    ),
    "y": (
        "left_endpoint_safe_old_kernel",
        "right_endpoint_safe_old_kernel",
        "size_three_companion_determinant",
    ),
}


def determinant_first_leaf_count(size: int) -> int:
    return size


def determinant_second_leaf_count(size: int) -> int:
    return size + math.comb(size, 2)


def factor_first_leaf_count(factor: str) -> int:
    return determinant_first_leaf_count(DETERMINANT_SIZES[factor]) if factor in DETERMINANT_SIZES else 1


def factor_second_leaf_count(factor: str) -> int:
    return determinant_second_leaf_count(DETERMINANT_SIZES[factor]) if factor in DETERMINANT_SIZES else 1


def compiled_leaf_count(factors: tuple[str, ...]) -> int:
    pure = sum(factor_second_leaf_count(factor) for factor in factors)
    cross = sum(
        factor_first_leaf_count(left) * factor_first_leaf_count(right)
        for index, left in enumerate(factors)
        for right in factors[index + 1 :]
    )
    return pure + cross


def outer_rows(factors: tuple[str, ...]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for factor in factors:
        rows.append(
            {
                "kind": "pure_second",
                "factors": [factor],
                "coefficient": 1,
                "determinant_preserving_leaves": factor_second_leaf_count(factor),
            }
        )
    for index, left in enumerate(factors):
        for right in factors[index + 1 :]:
            rows.append(
                {
                    "kind": "cross_first_first",
                    "factors": [left, right],
                    "coefficient": 2,
                    "determinant_preserving_leaves": factor_first_leaf_count(left)
                    * factor_first_leaf_count(right),
                }
            )
    return rows


def build() -> dict[str, Any]:
    k288 = json.loads(K288.read_text())
    k299 = json.loads(K299.read_text())
    k302 = json.loads(K302.read_text())
    occurrences = k288["coherent_gram_measure"]["size_four_occurrences"]
    axes = [row["axis"] for row in k299["one_dimensional_factors"]]
    if axes != list(AXIS_FACTORS):
        raise AssertionError("K299 tensor-axis order changed")
    if len(occurrences) != 24:
        raise AssertionError("K288 occurrence census changed")
    groups = Counter(str(row["group_id"]) for row in occurrences)
    if len(groups) != 4 or set(groups.values()) != {6}:
        raise AssertionError("expected four coherent groups of six occurrences")

    axis_rows = []
    all_occurrence_leaves = 0
    for axis in axes:
        factors = AXIS_FACTORS[axis]
        rows = outer_rows(factors)
        leaf_count = compiled_leaf_count(factors)
        if leaf_count != sum(row["determinant_preserving_leaves"] for row in rows):
            raise AssertionError("compiled leaf count disagrees with explicit outer rows")
        all_occurrence_leaves += len(occurrences) * leaf_count
        axis_rows.append(
            {
                "axis": axis,
                "active_factors": list(factors),
                "outer_product_rule_families": len(rows),
                "determinant_preserving_leaves_per_occurrence": leaf_count,
                "determinant_preserving_leaves_all_occurrences": len(occurrences) * leaf_count,
                "outer_rows": rows,
            }
        )

    terminal_patterns = Counter(
        "L"
        + ",".join(map(str, row["companion_factors"][0]["left_positions"]))
        + "|R"
        + ",".join(map(str, row["companion_factors"][0]["right_positions"]))
        for row in occurrences
    )
    if len(terminal_patterns) != 6 or set(terminal_patterns.values()) != {4}:
        raise AssertionError("six-pattern terminal companion census changed")

    return {
        "schema_version": "1.0",
        "result_id": "K303-ORDER-SEVEN-PEANO-DETERMINANT-COMPILER",
        "created": "2026-09-22",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k288-order-seven-native-occurrence-measure.json",
                "lab/process/k299-order-seven-positive-peano-simplex-rule.json",
                "lab/process/k302-order-seven-split-weighted-peano-jet.json",
            ],
            "occurrences": len(occurrences),
            "coherent_groups": len(groups),
            "records_per_group": 6,
            "peano_axes": axes,
            "companion_patterns": len(terminal_patterns),
        },
        "determinant_multilinearity": {
            "first_derivative": "D det(C_1,...,C_m)=sum_j det(C_1,...,D C_j,...,C_m)",
            "second_derivative": "D^2 det(C)=sum_j det(...,D^2 C_j,...)+2 sum_{j<k} det(...,D C_j,...,D C_k,...)",
            "size_four_first_leaves": determinant_first_leaf_count(4),
            "size_four_second_leaves": determinant_second_leaf_count(4),
            "size_three_first_leaves": determinant_first_leaf_count(3),
            "size_three_second_leaves": determinant_second_leaf_count(3),
            "column_order_preserved": True,
            "permutation_expansion_used": False,
        },
        "outer_factorization": {
            "angular_integrand": "A(x,q)*P(p)*L_old(y,u,p)*R_old(y,z,p)*D4(x,q,p)*D3(x,q,p,y,u,z)",
            "angular_independent_scalar": "A=(2*pi)^-9*exp(-256*x*(1+q))*x^15*q^11",
            "projective_factor": "P=product_i p_i; Duffy Jacobian powers remain the one-axis base weights and are not differentiated inside F",
            "endpoint_pairing": "L_old and R_old absorb the native y and (1-y) factors before differentiation",
            "y_independence": ["A", "P", "D4"],
            "late_column_axis_independence": "t3 and t4 move only c-side gaps, so L_old is constant on those directions",
        },
        "axis_compiler": axis_rows,
        "complete_counts": {
            "gap_axis_leaves_all_occurrences": sum(
                row["determinant_preserving_leaves_all_occurrences"]
                for row in axis_rows
                if row["axis"] != "y"
            ),
            "y_axis_leaves_all_occurrences": next(
                row["determinant_preserving_leaves_all_occurrences"]
                for row in axis_rows
                if row["axis"] == "y"
            ),
            "all_six_axes_leaves_all_occurrences": all_occurrence_leaves,
            "coherent_absolute_value_location": "after the six signed occurrence contributions in each group have been assembled for a common leaf functional",
        },
        "terminal_split_usage": {
            "pattern_histogram": dict(sorted(terminal_patterns.items())),
            "terminal_entry": "D3 row/column (8,8)",
            "required_terminal_jet_orders": [0, 1, 2],
            "k302_bounds": k302["universal_weighted_bounds"],
            "safe_use": "only inside the exact y-Peano/split integral, or inside a separately proved joint weighted multiplier bound",
            "unsafe_use": "multiplying B0/B1/B2 by K290's superseded pointwise global companion/cofactor ceiling",
        },
        "decision": {
            "complete_determinant_product_rule_compiled": True,
            "all_six_peano_axes_compiled": True,
            "all_four_coherent_groups_retained": True,
            "numerical_peano_norms_emitted": False,
            "next_exact_input": "audit whether K302's marginal terminal jets can be combined with globally valid cofactor and old-kernel multipliers under each axis's actual Peano measure; otherwise construct the missing joint weighted functionals before any K294 gamma join",
        },
        "release_test": {
            "all_24_occurrences_replayed": len(occurrences) == 24,
            "all_six_axes_replayed": len(axis_rows) == 6,
            "all_six_companion_patterns_replayed": len(terminal_patterns) == 6,
            "all_second_column_cross_terms_carry_factor_two": all(
                row["coefficient"] == 2
                for axis in axis_rows
                for row in axis["outer_rows"]
                if row["kind"] == "cross_first_first"
            ),
            "pointwise_k290_reuse": False,
            "radial_gamma_join_emitted": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k302["ledger_effect"],
        "claim_ceiling": "Exact determinant-preserving second-directional compiler for all six K299 Peano axes, all 24 K288 occurrences and all four coherent groups. It enumerates 6,480 column-replacement leaf families, retains every factor-two cross term and places coherent absolute enclosure only after group assembly. It emits no numerical Peano norm, q/x enclosure, K294 gamma join, exterior action-column value, residual, native K152 interval, source/ledger move, canon, paper, public or physical claim.",
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
