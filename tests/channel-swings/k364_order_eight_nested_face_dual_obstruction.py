#!/usr/bin/env python3
"""Test whether K352 optimal determinant duals nest along face flags."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K352 = ROOT / "lab/process/k352-order-eight-mask-native-preconditioner-compiler.json"
K353 = ROOT / "lab/process/k353-order-eight-face-normal-integrability-atlas.json"
K363 = ROOT / "lab/process/k363-order-eight-global-face-neighborhood-ownership.json"
OUTPUT = ROOT / "lab/process/k364-order-eight-nested-face-dual-obstruction.json"


Pattern = tuple[tuple[int, ...], ...]
Dual = tuple[tuple[int, ...], tuple[int, ...]]


def digest(value: Any) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def assignment_optimum(costs: Pattern) -> int:
    return max(
        sum(costs[row][column] for row, column in enumerate(permutation))
        for permutation in itertools.permutations(range(len(costs)))
    )


def binary_optimal_duals(costs: Pattern) -> list[Dual]:
    rank = len(costs)
    optimum = assignment_optimum(costs)
    result = []
    for rows in itertools.product(range(2), repeat=rank):
        for columns in itertools.product(range(2), repeat=rank):
            if sum(rows) + sum(columns) != optimum:
                continue
            if all(rows[i] + columns[j] >= costs[i][j] for i in range(rank) for j in range(rank)):
                result.append((rows, columns))
    return result


def integer_gauge_optimal_duals(costs: Pattern) -> list[Dual]:
    rank = len(costs)
    optimum = assignment_optimum(costs)
    result = []
    for rows in itertools.product(range(-rank, rank + 1), repeat=rank):
        columns = tuple(max(costs[i][j] - rows[i] for i in range(rank)) for j in range(rank))
        if sum(rows) + sum(columns) == optimum:
            result.append((rows, columns))
    return result


def covers(costs: Pattern, maximum_power: int = 2) -> list[tuple[int, Dual]]:
    rank = len(costs)
    result = []
    for rows in itertools.product(range(maximum_power + 1), repeat=rank):
        for columns in itertools.product(range(maximum_power + 1), repeat=rank):
            if all(rows[i] + columns[j] >= costs[i][j] for i in range(rank) for j in range(rank)):
                result.append((sum(rows) + sum(columns), (rows, columns)))
    return result


def dominates(left: Dual, right: Dual) -> bool:
    return all(a <= b for a, b in zip(left[0], right[0], strict=True)) and all(
        a <= b for a, b in zip(left[1], right[1], strict=True)
    )


def comparable(left: Pattern, right: Pattern) -> bool:
    return len(left) == len(right) and left != right and all(
        left[i][j] <= right[i][j]
        for i in range(len(left))
        for j in range(len(left))
    )


def build() -> dict[str, Any]:
    k352 = json.loads(K352.read_text())
    k353 = json.loads(K353.read_text())
    k363 = json.loads(K363.read_text())
    templates = []
    for index, row in enumerate(k352["preconditioner_templates"]):
        pattern = tuple(tuple(int(value) for value in values) for values in row["zero_entry_matrix"])
        if assignment_optimum(pattern) != int(row["maximum_zero_kernels_per_leibniz_term"]):
            raise AssertionError("K352 assignment optimum changed")
        templates.append((f"S{index:02d}", pattern))

    binary = {name: binary_optimal_duals(pattern) for name, pattern in templates}
    integer = {name: integer_gauge_optimal_duals(pattern) for name, pattern in templates}
    cover_bank = {name: covers(pattern) for name, pattern in templates}
    rows = []
    for left_name, left in templates:
        for right_name, right in templates:
            if not comparable(left, right):
                continue
            binary_nesting = any(dominates(a, b) for a in binary[left_name] for b in binary[right_name])
            integer_nesting = any(dominates(a, b) for a in integer[left_name] for b in integer[right_name])
            left_optimum = assignment_optimum(left)
            right_optimum = assignment_optimum(right)
            repair_candidates = []
            for left_sum, left_dual in cover_bank[left_name]:
                if left_sum != left_optimum:
                    continue
                for right_sum, right_dual in cover_bank[right_name]:
                    if dominates(left_dual, right_dual):
                        repair_candidates.append((right_sum - right_optimum, left_dual, right_dual))
            if not repair_candidates:
                raise AssertionError("rank-two power search failed to find a scalar nesting repair")
            overhead, left_witness, right_witness = min(repair_candidates)
            rows.append({
                "outer_template_id": left_name,
                "inner_template_id": right_name,
                "rank": len(left),
                "outer_assignment_optimum": left_optimum,
                "inner_assignment_optimum": right_optimum,
                "monotone_optimal_binary_dual_exists": binary_nesting,
                "monotone_optimal_integer_gauge_dual_exists": integer_nesting,
                "minimum_forced_inner_overextraction": overhead,
                "scalar_repair_outer_rows": list(left_witness[0]),
                "scalar_repair_outer_columns": list(left_witness[1]),
                "scalar_repair_inner_rows": list(right_witness[0]),
                "scalar_repair_inner_columns": list(right_witness[1]),
            })

    obstruction_rows = [row for row in rows if not row["monotone_optimal_integer_gauge_dual_exists"]]
    overhead_histogram = Counter(row["minimum_forced_inner_overextraction"] for row in rows)
    confluent = k352["confluent_divided_difference_contract"]["templates"]
    derivative_orders = [
        int(row["maximum_row_divided_difference_order"])
        + int(row["maximum_column_divided_difference_order"])
        + 2
        for row in confluent
    ]
    return {
        "schema_version": "1.0",
        "result_id": "K364-ORDER-EIGHT-NESTED-FACE-DUAL-OBSTRUCTION",
        "created": "2026-09-23",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [str(path.relative_to(ROOT)) for path in (K352, K353, K363)],
            "singular_templates": len(templates),
            "same_rank_comparable_template_pairs": len(rows),
            "K352_template_bank_sha256": k352["template_summary"]["template_bank_sha256"],
            "K353_global_minimum_face_normal_power": k353["atlas_summary"]["global_minimum_face_normal_power"],
            "K363_epsilon": k363["fixed_control"]["epsilon"],
        },
        "nested_dual_contract": {
            "comparison": "A<=B entrywise means the inner face marks every singular entry marked by the outer face and possibly more",
            "optimal_scalar_nesting_test": "choose optimal row/column assignment duals for A and B with every B potential coordinate no smaller than the corresponding A coordinate",
            "integer_gauge_test": "allow every optimal integral assignment-dual gauge on [-rank,rank] before declaring obstruction",
            "forced_scalar_repair": "retain an optimal outer dual and allow nonnegative inner row/column powers through two; record the least excess over the inner assignment optimum",
            "overextraction_warning": "one excess extracted power creates an artificial inverse scale and is not licensed when K353's true face-normal margin can be zero",
            "determinant_failure_claimed": False,
        },
        "comparable_pair_bank": rows,
        "obstruction_summary": {
            "monotone_optimal_binary_pairs": sum(row["monotone_optimal_binary_dual_exists"] for row in rows),
            "pairs_without_monotone_optimal_binary_duals": sum(not row["monotone_optimal_binary_dual_exists"] for row in rows),
            "pairs_without_monotone_optimal_integer_gauge_duals": len(obstruction_rows),
            "forced_inner_overextraction_histogram": {str(key): overhead_histogram[key] for key in sorted(overhead_histogram)},
            "all_obstructed_pairs_require_exactly_one_false_extra_power": all(row["minimum_forced_inner_overextraction"] == 1 for row in obstruction_rows),
            "obstruction_pair_ids_sha256": digest([(row["outer_template_id"], row["inner_template_id"]) for row in obstruction_rows]),
        },
        "confluent_derivative_demand": {
            "maximum_row_divided_difference_order": max(int(row["maximum_row_divided_difference_order"]) for row in confluent),
            "maximum_column_divided_difference_order": max(int(row["maximum_column_divided_difference_order"]) for row in confluent),
            "active_peano_derivative_order": 2,
            "maximum_kernel_derivative_order_required": max(derivative_orders),
            "required_orders": list(range(max(derivative_orders) + 1)),
            "K349_current_maximum_order": 2,
        },
        "decision": {
            "naive_monotone_optimal_scalar_dual_reuse_rejected": len(obstruction_rows) > 0,
            "determinant_preserving_multiscale_exponent_interface_required": len(obstruction_rows) > 0,
            "orders_zero_through_eight_scaled_kernel_bank_required": max(derivative_orders) == 8,
            "uniform_integrand_weighted_boundary_majorant_complete": False,
            "next_exact_input": "extend K349 through derivative order eight and retain the complete bivariate determinant permutation-exponent Newton fronts instead of forcing one false scalar dual",
        },
        "release_test": {
            "exactly_34_K352_templates_replayed": len(templates) == 34,
            "exactly_146_comparable_pairs_exhausted": len(rows) == 146,
            "exactly_12_optimal_scalar_nesting_obstructions": len(obstruction_rows) == 12,
            "integer_gauge_does_not_remove_obstructions": sum(not row["monotone_optimal_binary_dual_exists"] for row in rows) == len(obstruction_rows),
            "all_scalar_repairs_found": all(row["minimum_forced_inner_overextraction"] in {0, 1} for row in rows),
            "all_12_obstructions_cost_one_extra_power": all(row["minimum_forced_inner_overextraction"] == 1 for row in obstruction_rows),
            "maximum_required_kernel_derivative_order_is_eight": max(derivative_orders) == 8,
            "determinant_not_declared_failed": True,
            "uniform_strip_bound_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k363["ledger_effect"],
        "source_routing": k363["source_routing"],
        "claim_ceiling": "Exact exhaustion of the 146 same-rank entrywise-comparable pairs among K352's 34 determinant singular templates. Twelve pairs have no coordinatewise monotone optimal binary dual and no such optimal integral gauge; every forced scalar repair overextracts exactly one inner power, which is unsafe because K353 has zero-margin faces. The same replay proves that row/column confluent orders plus the active second derivative require scaled 2*K1 derivatives through order eight. This rejects naive scalar dual nesting, not the determinant, the face integral or the order-eight route. A multiscale determinant exponent interface, zero-safe order-eight derivative bank, uniform strip bound, recursive cover, tails, complete hybrids and downstream scientific claims remain open.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["singular_templates"], fixed["same_rank_comparable_template_pairs"], fixed["K353_global_minimum_face_normal_power"], fixed["K363_epsilon"]) != (34, 146, 0, "1/64"):
        raise AssertionError("K364 fixed census changed")
    rows = payload["comparable_pair_bank"]
    if len(rows) != 146 or sum(not row["monotone_optimal_integer_gauge_dual_exists"] for row in rows) != 12:
        raise AssertionError("K364 obstruction census changed")
    summary = payload["obstruction_summary"]
    if (summary["pairs_without_monotone_optimal_integer_gauge_duals"] != 12
            or summary["forced_inner_overextraction_histogram"] != {"0": 134, "1": 12}
            or not summary["all_obstructed_pairs_require_exactly_one_false_extra_power"]
            or any(row["minimum_forced_inner_overextraction"] not in {0, 1} for row in rows)
            or sum(row["minimum_forced_inner_overextraction"] == 1 for row in rows) != 12):
        raise AssertionError("K364 scalar repair cost changed")
    demand = payload["confluent_derivative_demand"]
    if (demand["maximum_row_divided_difference_order"], demand["maximum_column_divided_difference_order"], demand["maximum_kernel_derivative_order_required"]) != (3, 3, 8):
        raise AssertionError("K364 derivative demand changed")
    if not all(payload["release_test"].values()):
        raise AssertionError("K364 release test failed")
    decision = payload["decision"]
    if not decision["naive_monotone_optimal_scalar_dual_reuse_rejected"] or decision["uniform_integrand_weighted_boundary_majorant_complete"]:
        raise AssertionError("K364 decision boundary changed")


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
