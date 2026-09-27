#!/usr/bin/env python3
"""Test whether K413 optimal determinant duals nest along face flags."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
K413 = ROOT / "lab/process/k413-order-ten-mask-native-preconditioner-compiler.json"
K414 = ROOT / "lab/process/k414-order-ten-face-normal-integrability-atlas.json"
K545 = ROOT / "lab/process/k545-order-ten-global-face-neighborhood-ownership.json"
OUTPUT = ROOT / "lab/process/k546-order-ten-nested-face-dual-obstruction.json"

spec = importlib.util.spec_from_file_location(
    "k364_helpers", HERE / "k364_order_eight_nested_face_dual_obstruction.py"
)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load K364 helpers")
K364 = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = K364
spec.loader.exec_module(K364)


def digest(value: Any) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def build() -> dict[str, Any]:
    k413 = json.loads(K413.read_text())
    k414 = json.loads(K414.read_text())
    k545 = json.loads(K545.read_text())
    templates = []
    for index, row in enumerate(k413["preconditioner_templates"]):
        pattern = tuple(tuple(int(value) for value in values) for values in row["zero_entry_matrix"])
        if K364.assignment_optimum(pattern) != int(row["maximum_zero_kernels_per_leibniz_term"]):
            raise AssertionError("K413 assignment optimum changed")
        templates.append((f"S{index:02d}", pattern))

    binary = {name: K364.binary_optimal_duals(pattern) for name, pattern in templates}
    integer = {name: K364.integer_gauge_optimal_duals(pattern) for name, pattern in templates}
    cover_bank = {name: K364.covers(pattern) for name, pattern in templates}
    rows = []
    for left_name, left in templates:
        for right_name, right in templates:
            if not K364.comparable(left, right):
                continue
            binary_nesting = any(K364.dominates(a, b) for a in binary[left_name] for b in binary[right_name])
            integer_nesting = any(K364.dominates(a, b) for a in integer[left_name] for b in integer[right_name])
            left_optimum = K364.assignment_optimum(left)
            right_optimum = K364.assignment_optimum(right)
            repair_candidates = []
            for left_sum, left_dual in cover_bank[left_name]:
                if left_sum != left_optimum:
                    continue
                for right_sum, right_dual in cover_bank[right_name]:
                    if K364.dominates(left_dual, right_dual):
                        repair_candidates.append((right_sum - right_optimum, left_dual, right_dual))
            if not repair_candidates:
                raise AssertionError("rank-five power search failed to find a scalar nesting repair")
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
    confluent = k413["confluent_divided_difference_contract"]["templates"]
    derivative_orders = [
        int(row["maximum_row_divided_difference_order"])
        + int(row["maximum_column_divided_difference_order"])
        + 2
        for row in confluent
    ]
    return {
        "schema_version": "1.0",
        "result_id": "K546-ORDER-TEN-NESTED-FACE-DUAL-OBSTRUCTION",
        "created": "2026-09-27",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [str(path.relative_to(ROOT)) for path in (K413, K414, K545)],
            "singular_templates": len(templates),
            "same_rank_comparable_template_pairs": len(rows),
            "K413_template_bank_sha256": k413["template_summary"]["template_bank_sha256"],
            "K414_global_minimum_face_normal_power": k414["atlas_summary"]["global_minimum_face_normal_power"],
            "K545_epsilon": k545["fixed_control"]["epsilon"],
        },
        "nested_dual_contract": {
            "comparison": "A<=B entrywise means the inner face marks every singular entry marked by the outer face and possibly more",
            "optimal_scalar_nesting_test": "choose optimal row/column assignment duals for A and B with every B potential coordinate no smaller than the corresponding A coordinate",
            "integer_gauge_test": "allow every optimal integral assignment-dual gauge on [-rank,rank] before declaring obstruction",
            "forced_scalar_repair": "retain an optimal outer dual and allow nonnegative inner row/column powers through two; record the least excess over the inner assignment optimum",
            "overextraction_warning": "one excess extracted power creates an artificial inverse scale and is not licensed when K414's true face-normal margin can be zero",
            "determinant_failure_claimed": False,
        },
        "comparable_pair_bank": rows,
        "obstruction_summary": {
            "monotone_optimal_binary_pairs": sum(row["monotone_optimal_binary_dual_exists"] for row in rows),
            "pairs_without_monotone_optimal_binary_duals": sum(not row["monotone_optimal_binary_dual_exists"] for row in rows),
            "pairs_without_monotone_optimal_integer_gauge_duals": len(obstruction_rows),
            "forced_inner_overextraction_histogram": {str(key): overhead_histogram[key] for key in sorted(overhead_histogram)},
            "maximum_forced_inner_overextraction": max(row["minimum_forced_inner_overextraction"] for row in obstruction_rows),
            "exactly_two_obstructions_require_two_false_extra_powers": sum(row["minimum_forced_inner_overextraction"] == 2 for row in obstruction_rows) == 2,
            "obstruction_pair_ids_sha256": digest([(row["outer_template_id"], row["inner_template_id"]) for row in obstruction_rows]),
        },
        "confluent_derivative_demand": {
            "maximum_row_divided_difference_order": max(int(row["maximum_row_divided_difference_order"]) for row in confluent),
            "maximum_column_divided_difference_order": max(int(row["maximum_column_divided_difference_order"]) for row in confluent),
            "active_peano_derivative_order": 2,
            "maximum_kernel_derivative_order_required": max(derivative_orders),
            "required_orders": list(range(max(derivative_orders) + 1)),
            "K410_current_maximum_order": 2,
        },
        "decision": {
            "naive_monotone_optimal_scalar_dual_reuse_rejected": len(obstruction_rows) > 0,
            "determinant_preserving_multiscale_exponent_interface_required": len(obstruction_rows) > 0,
            "orders_zero_through_ten_scaled_kernel_bank_required": max(derivative_orders) == 10,
            "uniform_integrand_weighted_boundary_majorant_complete": False,
            "next_exact_input": "extend K410 through derivative order ten and retain complete bivariate determinant permutation-exponent Newton fronts instead of forcing one false scalar dual",
        },
        "release_test": {
            "exactly_60_K413_templates_replayed": len(templates) == 60,
            "exactly_371_same_rank_comparable_pairs_exhausted": len(rows) == 371,
            "exactly_42_optimal_scalar_nesting_obstructions": len(obstruction_rows) == 42,
            "integer_gauge_does_not_remove_obstructions": sum(not row["monotone_optimal_binary_dual_exists"] for row in rows) == len(obstruction_rows),
            "all_scalar_repairs_found": all(row["minimum_forced_inner_overextraction"] in {0, 1, 2} for row in rows),
            "exactly_40_obstructions_cost_one_extra_power": sum(row["minimum_forced_inner_overextraction"] == 1 for row in obstruction_rows) == 40,
            "exactly_2_obstructions_cost_two_extra_powers": sum(row["minimum_forced_inner_overextraction"] == 2 for row in obstruction_rows) == 2,
            "maximum_required_kernel_derivative_order_is_ten": max(derivative_orders) == 10,
            "determinant_not_declared_failed": True,
            "uniform_strip_bound_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k545["ledger_effect"],
        "source_routing": k545["source_routing"],
        "claim_ceiling": "Exact exhaustion of all 371 same-rank entrywise-comparable pairs among K413's 60 determinant singular templates. Forty-two pairs have no coordinatewise monotone optimal binary or integral-gauge dual; forty scalar repairs overextract one power and two overextract two powers. K414's zero face-normal margin makes every false extra power unsafe. The replay also derives the scaled 2*K1 derivative demand through order ten. This rejects naive scalar dual nesting, not the determinant, face integral, or order-ten route; multiscale determinant fronts, a zero-safe derivative bank, uniform boundary bound, recursive cover, tails, complete hybrids, and downstream scientific claims remain open.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["singular_templates"], fixed["K414_global_minimum_face_normal_power"], fixed["K545_epsilon"]) != (60, 0, "1/64"):
        raise AssertionError("K546 fixed census changed")
    rows = payload["comparable_pair_bank"]
    if len(rows) != 371 or fixed["same_rank_comparable_template_pairs"] != 371:
        raise AssertionError("K546 comparable-pair census changed")
    obstruction_rows = [row for row in rows if not row["monotone_optimal_integer_gauge_dual_exists"]]
    summary = payload["obstruction_summary"]
    histogram = Counter(row["minimum_forced_inner_overextraction"] for row in rows)
    if len(obstruction_rows) != 42 or summary["pairs_without_monotone_optimal_integer_gauge_duals"] != 42:
        raise AssertionError("K546 obstruction census changed")
    if summary["forced_inner_overextraction_histogram"] != {str(key): histogram[key] for key in sorted(histogram)}:
        raise AssertionError("K546 repair histogram changed")
    if (summary["maximum_forced_inner_overextraction"] != 2
            or not summary["exactly_two_obstructions_require_two_false_extra_powers"]
            or sum(row["minimum_forced_inner_overextraction"] == 1 for row in obstruction_rows) != 40
            or sum(row["minimum_forced_inner_overextraction"] == 2 for row in obstruction_rows) != 2):
        raise AssertionError("K546 scalar repair cost changed")
    demand = payload["confluent_derivative_demand"]
    if (demand["maximum_row_divided_difference_order"], demand["maximum_column_divided_difference_order"], demand["maximum_kernel_derivative_order_required"]) != (4, 4, 10):
        raise AssertionError("K546 derivative demand changed")
    if not all(payload["release_test"].values()):
        raise AssertionError("K546 release test failed")
    decision = payload["decision"]
    if not decision["naive_monotone_optimal_scalar_dual_reuse_rejected"] or decision["uniform_integrand_weighted_boundary_majorant_complete"]:
        raise AssertionError("K546 decision boundary changed")


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
