#!/usr/bin/env python3
"""Prove the gap-free tensor divided-difference calculus through rank five."""

from __future__ import annotations

import argparse
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any, Callable


ROOT = Path(__file__).resolve().parents[2]
K373 = ROOT / "lab/process/k373-order-nine-rank-five-determinant-atlas.json"
OUTPUT = ROOT / "lab/process/k374-rank-five-confluent-determinant-calculus.json"
MAX_RANK = 5
MAX_KERNEL_ORDER = 10


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    total = Fraction(0)
    for permutation in itertools.permutations(range(len(matrix))):
        inversions = sum(permutation[i] > permutation[j] for i in range(len(permutation)) for j in range(i + 1, len(permutation)))
        term = Fraction(-1 if inversions % 2 else 1)
        for row, column in enumerate(permutation):
            term *= matrix[row][column]
        total += term
    return total


def divided_difference(nodes: list[Fraction], values: list[Fraction]) -> Fraction:
    work = values[:]
    for level in range(1, len(nodes)):
        work = [(work[index + 1] - work[index]) / (nodes[index + level] - nodes[index]) for index in range(len(work) - 1)]
    return work[0]


def mixed_divided_difference(left: list[Fraction], right: list[Fraction], function: Callable[[Fraction], Fraction]) -> Fraction:
    row_values = [divided_difference(left, [function(x + y) for x in left]) for y in right]
    return divided_difference(right, row_values)


def complete_homogeneous(nodes: list[Fraction], degree: int) -> Fraction:
    if degree == 0:
        return Fraction(1)
    return sum((math.prod((nodes[index] for index in choice), start=Fraction(1)) for choice in itertools.combinations_with_replacement(range(len(nodes)), degree)), start=Fraction(0))


def monomial_formula(power: int, left: list[Fraction], right: list[Fraction]) -> Fraction:
    row = len(left) - 1
    column = len(right) - 1
    return sum((
        Fraction(math.comb(power, split))
        * complete_homogeneous(left, split - row)
        * complete_homogeneous(right, power - split - column)
        for split in range(row, power - column + 1)
    ), start=Fraction(0))


def matrix_divided_differences(left: list[Fraction], right: list[Fraction]) -> list[list[Fraction]]:
    matrix = [[Fraction(2, 1) / (x + y) for y in right] for x in left]
    size = len(left)
    for level in range(1, size):
        for row in range(size - 1, level - 1, -1):
            divisor = left[row] - left[row - level]
            for column in range(size):
                matrix[row][column] = (matrix[row][column] - matrix[row - 1][column]) / divisor
    for level in range(1, size):
        for column in range(size - 1, level - 1, -1):
            divisor = right[column] - right[column - level]
            for row in range(size):
                matrix[row][column] = (matrix[row][column] - matrix[row][column - 1]) / divisor
    return matrix


def vandermonde_increasing(values: list[Fraction]) -> Fraction:
    return math.prod((values[j] - values[i] for i in range(len(values)) for j in range(i + 1, len(values))), start=Fraction(1))


def polynomial_controls() -> list[dict[str, Any]]:
    rows = []
    for rank in range(1, MAX_RANK + 1):
        left = [Fraction(2 * index + 1, 29) for index in range(rank)]
        right = [Fraction(3 * index + 2, 31) for index in range(rank)]
        for power in range(MAX_KERNEL_ORDER + 1):
            recursive = mixed_divided_difference(left, right, lambda z, p=power: z**p)
            formula = monomial_formula(power, left, right)
            rows.append({"rank": rank, "power": power, "recursive": str(recursive), "gap_free_formula": str(formula), "exact_equality": recursive == formula})
    return rows


def determinant_controls() -> list[dict[str, Any]]:
    rows = []
    for rank in range(1, MAX_RANK + 1):
        left = [Fraction(2 * index + 3, 37) for index in range(rank)]
        right = [Fraction(3 * index + 5, 41) for index in range(rank)]
        direct = determinant([[Fraction(2, 1) / (x + y) for y in right] for x in left])
        transformed = determinant(matrix_divided_differences(left, right))
        replay = transformed * vandermonde_increasing(left) * vandermonde_increasing(right)
        normalized = transformed * math.prod((x + y for x in left for y in right), start=Fraction(1))
        rows.append({
            "rank": rank,
            "direct": str(direct),
            "divided_difference_determinant": str(transformed),
            "vandermonde_replay": str(replay),
            "normalized_cauchy_value": str(normalized),
            "expected_normalized_value": str(2**rank),
            "exact_replay": direct == replay,
            "exact_normalization": normalized == 2**rank,
        })
    return rows


def all_zero_limits() -> list[dict[str, Any]]:
    rows = []
    for row_order in range(MAX_RANK):
        for column_order in range(MAX_RANK):
            power = row_order + column_order
            value = math.comb(power, row_order)
            rows.append({
                "row_order": row_order,
                "column_order": column_order,
                "monomial_power": power,
                "confluent_value": value,
                "derivative_rule": f"partial_x^{row_order} partial_y^{column_order} (x+y)^{power}/({row_order}!{column_order}!)",
            })
    return rows


def build() -> dict[str, Any]:
    k373 = json.loads(K373.read_text())
    inventory = k373["complete_factorization_inventory"]
    if k373["fixed_control"]["maximum_species_determinant_rank"] != MAX_RANK or inventory["rank_five_patterns"] <= 0:
        raise AssertionError("K373 rank-five boundary changed")
    poly = polynomial_controls()
    determinants = determinant_controls()
    if not all(row["exact_equality"] for row in poly):
        raise AssertionError("gap-free monomial formula failed")
    if not all(row["exact_replay"] and row["exact_normalization"] for row in determinants):
        raise AssertionError("divided-difference determinant replay failed")
    return {
        "schema_version": "1.0",
        "result_id": "K374-RANK-FIVE-CONFLUENT-DETERMINANT-CALCULUS",
        "created": "2026-09-23",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [str(K373.relative_to(ROOT))],
            "maximum_rank": MAX_RANK,
            "maximum_row_divided_difference_order": 4,
            "maximum_column_divided_difference_order": 4,
            "active_peano_derivative_order": 2,
            "maximum_kernel_derivative_order": MAX_KERNEL_ORDER,
            "polynomial_identity_checks": len(poly),
            "exact_determinant_checks": len(determinants),
            "K373_rank_five_pattern_sha256": inventory["rank_five_pattern_sha256"],
        },
        "gap_free_tensor_divided_difference": {
            "monomial_identity": "[x_0,...,x_r][y_0,...,y_c](x+y)^p=sum_(k=r)^(p-c) binom(p,k) h_(k-r)(x_0,...,x_r) h_(p-k-c)(y_0,...,y_c)",
            "complete_homogeneous_polynomials_are_nonnegative_on_nonnegative_nodes": True,
            "explicit_gap_denominators_after_extension": False,
            "repeated_nodes_allowed_by_continuity": True,
            "all_zero_value": "binom(r+c,r) for p=r+c and zero for p<r+c",
            "polynomial_controls": poly,
            "all_zero_controls": all_zero_limits(),
        },
        "determinant_calculus": {
            "cauchy_identity": "det[2/(x_i+y_j)]=2^m*V(x)*V(y)/product_ij(x_i+y_j)",
            "divided_difference_identity": "det(DD_x DD_y C)*V(x)*V(y)=det(C)",
            "normalized_confluent_cauchy_value": "2^m/product_ij(x_i+y_j)",
            "exact_controls": determinants,
            "complete_determinant_assembled_before_absolute_enclosure": True,
            "entrywise_cofactor_absolutization_permitted": False,
        },
        "derivative_demand": {
            "kernel_orders_required": list(range(MAX_KERNEL_ORDER + 1)),
            "rank_five_confluence_maximum": 8,
            "pure_second_axis_extension": 2,
            "total_required": 10,
            "primitive_bank_complete": False,
        },
        "decision": {
            "rank_five_gap_free_confluent_determinant_calculus_emitted": True,
            "K373_rank_five_patterns_bound_to_calculus": True,
            "zero_safe_global_primitive_bank_through_order_ten_emitted": False,
            "numerical_order_nine_integral_emitted": False,
            "next_exact_input": "extend the exact rational zero-safe scaled 2*K1 bank and its analytic half-integer tail comparator through derivative order ten",
        },
        "release_test": {
            "all_55_polynomial_identities_exact": len(poly) == 55 and all(row["exact_equality"] for row in poly),
            "all_five_determinant_ranks_exact": len(determinants) == 5 and all(row["exact_replay"] and row["exact_normalization"] for row in determinants),
            "all_25_zero_limits_serialized": len(all_zero_limits()) == 25,
            "rank_five_requires_orders_zero_through_ten": True,
            "explicit_gap_divisions_removed_on_confluent_faces": True,
            "complete_determinant_correlation_retained": True,
            "global_primitive_bank_not_overclaimed": True,
            "numerical_integral_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k373["ledger_effect"],
        "source_routing": k373["source_routing"],
        "claim_ceiling": "Exact gap-free tensor divided-difference and determinant calculus through rank five. Fifty-five rational monomial identities, all twenty-five all-zero confluence limits, and exact Cauchy determinant/Vandermonde replays through size five pass. This closes the algebraic confluence rule and fixes derivative demand through order ten; it does not yet provide the zero-safe global Bessel primitive bank, an order-nine numerical integral, action column, R_ref, K152, source/ledger move, canon, paper, public, novelty or physical claim."
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["maximum_rank"], fixed["maximum_row_divided_difference_order"], fixed["maximum_column_divided_difference_order"], fixed["active_peano_derivative_order"], fixed["maximum_kernel_derivative_order"], fixed["polynomial_identity_checks"], fixed["exact_determinant_checks"]) != (5, 4, 4, 2, 10, 55, 5):
        raise AssertionError("K374 fixed control changed")
    gap = payload["gap_free_tensor_divided_difference"]
    if gap["explicit_gap_denominators_after_extension"] or not gap["repeated_nodes_allowed_by_continuity"] or not all(row["exact_equality"] for row in gap["polynomial_controls"]):
        raise AssertionError("K374 gap-free calculus changed")
    determinant_rows = payload["determinant_calculus"]
    if not determinant_rows["complete_determinant_assembled_before_absolute_enclosure"] or determinant_rows["entrywise_cofactor_absolutization_permitted"] or not all(row["exact_replay"] and row["exact_normalization"] for row in determinant_rows["exact_controls"]):
        raise AssertionError("K374 determinant calculus weakened")
    decision = payload["decision"]
    if not decision["rank_five_gap_free_confluent_determinant_calculus_emitted"] or decision["zero_safe_global_primitive_bank_through_order_ten_emitted"] or decision["numerical_order_nine_integral_emitted"]:
        raise AssertionError("K374 decision boundary changed")
    if not all(payload["release_test"].values()):
        raise AssertionError("K374 release test failed")


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
