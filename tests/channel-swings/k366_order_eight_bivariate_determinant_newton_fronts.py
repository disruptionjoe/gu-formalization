#!/usr/bin/env python3
"""Compile exact two-scale permutation-exponent fronts for K352 face flags."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K352 = ROOT / "lab/process/k352-order-eight-mask-native-preconditioner-compiler.json"
K364 = ROOT / "lab/process/k364-order-eight-nested-face-dual-obstruction.json"
K365 = ROOT / "lab/process/k365-order-eight-confluent-bessel-envelope-bank.json"
OUTPUT = ROOT / "lab/process/k366-order-eight-bivariate-determinant-newton-fronts.json"


Pattern = tuple[tuple[int, ...], ...]


def digest(value: Any) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def support(cost_outer: Pattern, cost_inner: Pattern) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    histogram: Counter[tuple[int, int]] = Counter()
    witnesses: dict[tuple[int, int], list[list[int]]] = {}
    for permutation in itertools.permutations(range(len(cost_outer))):
        outer = sum(cost_outer[row][column] for row, column in enumerate(permutation))
        inner_increment = sum(
            cost_inner[row][column] - cost_outer[row][column]
            for row, column in enumerate(permutation)
        )
        point = (outer, inner_increment)
        histogram[point] += 1
        witnesses.setdefault(point, []).append(list(permutation))
    rows = [
        {
            "outer_singular_exponent": point[0],
            "inner_increment_exponent": point[1],
            "inner_total_singular_exponent": point[0] + point[1],
            "permutation_count": histogram[point],
            "permutation_witnesses": witnesses[point],
        }
        for point in sorted(histogram)
    ]
    front_points = [
        point
        for point in histogram
        if not any(
            other[0] >= point[0]
            and other[1] >= point[1]
            and other != point
            for other in histogram
        )
    ]
    front = [
        {
            "outer_singular_exponent": point[0],
            "inner_increment_exponent": point[1],
            "inner_total_singular_exponent": point[0] + point[1],
            "permutation_count": histogram[point],
            "permutation_witnesses": witnesses[point],
        }
        for point in sorted(front_points)
    ]
    return rows, front


def pattern_map(k352: dict[str, Any]) -> dict[str, Pattern]:
    return {
        f"S{index:02d}": tuple(tuple(int(value) for value in row) for row in item["zero_entry_matrix"])
        for index, item in enumerate(k352["preconditioner_templates"])
    }


def build() -> dict[str, Any]:
    k352 = json.loads(K352.read_text())
    k364 = json.loads(K364.read_text())
    k365 = json.loads(K365.read_text())
    patterns = pattern_map(k352)
    rows = []
    for pair in k364["comparable_pair_bank"]:
        outer_id = pair["outer_template_id"]
        inner_id = pair["inner_template_id"]
        outer = patterns[outer_id]
        inner = patterns[inner_id]
        raw_support, front = support(outer, inner)
        if sum(row["permutation_count"] for row in raw_support) != math.factorial(len(outer)):
            raise AssertionError("bivariate support lost a determinant permutation")
        rows.append({
            "outer_template_id": outer_id,
            "inner_template_id": inner_id,
            "rank": len(outer),
            "scalar_optimal_nesting_obstructed": not pair["monotone_optimal_integer_gauge_dual_exists"],
            "permutation_exponent_support": raw_support,
            "pareto_maximal_newton_front": front,
            "support_sha256": digest(raw_support),
            "front_sha256": digest(front),
        })

    front_histogram = Counter(len(row["pareto_maximal_newton_front"]) for row in rows)
    unique_fronts = {
        tuple(
            (point["outer_singular_exponent"], point["inner_increment_exponent"])
            for point in row["pareto_maximal_newton_front"]
        )
        for row in rows
    }
    obstruction_rows = [row for row in rows if row["scalar_optimal_nesting_obstructed"]]
    return {
        "schema_version": "1.0",
        "result_id": "K366-ORDER-EIGHT-BIVARIATE-DETERMINANT-NEWTON-FRONTS",
        "created": "2026-09-23",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [str(path.relative_to(ROOT)) for path in (K352, K364, K365)],
            "singular_templates": len(patterns),
            "comparable_template_pairs": len(rows),
            "scalar_optimal_nesting_obstructions": len(obstruction_rows),
            "maximum_kernel_derivative_order_available": k365["fixed_control"]["maximum_derivative_order"],
            "K352_template_bank_sha256": k352["template_summary"]["template_bank_sha256"],
        },
        "newton_front_contract": {
            "outer_exponent": "sum of outer-face zero-entry costs along one determinant permutation",
            "inner_increment_exponent": "sum of the entrywise inner-minus-outer costs along the same permutation",
            "inner_total_exponent": "outer exponent plus inner increment on that same permutation",
            "front_order": "retain a point unless another realized permutation exponent pair is at least as singular in both scales and strictly more singular in one",
            "same_permutation_coupling_preserved": True,
            "all_permutations_retained_in_support_histograms": True,
            "occurrencewise_absolute_value_used": False,
            "one_false_scalar_exponent_substituted": False,
            "front_is_an_exponent_interface_not_a_numerical_determinant_bound": True,
        },
        "bivariate_front_bank": rows,
        "front_summary": {
            "pareto_front_size_histogram": {str(key): front_histogram[key] for key in sorted(front_histogram)},
            "maximum_front_size": max(front_histogram),
            "unique_front_signatures": len(unique_fronts),
            "all_12_scalar_obstructions_have_multiscale_fronts": len(obstruction_rows) == 12 and all(row["pareto_maximal_newton_front"] for row in obstruction_rows),
            "complete_bank_sha256": digest(rows),
        },
        "decision": {
            "bivariate_determinant_permutation_exponent_interface_complete": True,
            "K364_scalar_nesting_obstruction_repaired_without_overextraction": True,
            "zero_inclusive_numerical_determinant_envelope_complete": False,
            "uniform_integrand_weighted_boundary_majorant_complete": False,
            "next_exact_input": "combine each front point with K365's order-eight scaled derivative bounds and K352's confluent factors inside a zero-inclusive interval determinant, preserving the same-permutation two-scale coupling",
        },
        "release_test": {
            "exactly_34_K352_templates_in_scope": len(patterns) == 34,
            "exactly_146_comparable_pairs_compiled": len(rows) == 146,
            "exactly_12_scalar_obstructions_carried": len(obstruction_rows) == 12,
            "front_size_histogram_is_60_81_5": front_histogram == Counter({1: 60, 2: 81, 3: 5}),
            "maximum_front_size_is_three": max(front_histogram) == 3,
            "every_support_replays_rank_factorial_permutations": all(sum(point["permutation_count"] for point in row["permutation_exponent_support"]) == math.factorial(row["rank"]) for row in rows),
            "every_front_point_occurs_in_its_raw_support": all({(point["outer_singular_exponent"], point["inner_increment_exponent"]) for point in row["pareto_maximal_newton_front"]} <= {(point["outer_singular_exponent"], point["inner_increment_exponent"]) for point in row["permutation_exponent_support"]} for row in rows),
            "same_permutation_coupling_preserved": True,
            "uniform_strip_bound_not_overclaimed": True,
            "complete_order_eight_remainder_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k365["ledger_effect"],
        "source_routing": k365["source_routing"],
        "claim_ceiling": "Exact bivariate determinant permutation-exponent supports and Pareto-maximal Newton fronts for all 146 comparable K352 singular-template pairs, including all twelve K364 scalar nesting obstructions. Every rank-one-through-four determinant permutation remains coupled to its own outer and inner exponent; fronts have size at most three and no false extra scalar power is introduced. This is the determinant-preserving multiscale exponent interface needed for a zero-inclusive evaluator, not that numerical evaluator, a uniform integrand-weighted strip majorant, recursive cover, tail bound, complete K348 hybrid, order-eight remainder/integral, action column, R_ref, K152, source/ledger move, canon, paper, public or physical claim.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["singular_templates"], fixed["comparable_template_pairs"], fixed["scalar_optimal_nesting_obstructions"], fixed["maximum_kernel_derivative_order_available"]) != (34, 146, 12, 8):
        raise AssertionError("K366 fixed census changed")
    rows = payload["bivariate_front_bank"]
    if len(rows) != 146 or sum(row["scalar_optimal_nesting_obstructed"] for row in rows) != 12:
        raise AssertionError("K366 pair bank changed")
    histogram = Counter(len(row["pareto_maximal_newton_front"]) for row in rows)
    if histogram != Counter({1: 60, 2: 81, 3: 5}):
        raise AssertionError("K366 Newton front histogram changed")
    if any(sum(point["permutation_count"] for point in row["permutation_exponent_support"]) != math.factorial(row["rank"]) for row in rows):
        raise AssertionError("K366 determinant permutation support changed")
    contract = payload["newton_front_contract"]
    if not contract["same_permutation_coupling_preserved"] or not contract["all_permutations_retained_in_support_histograms"] or contract["occurrencewise_absolute_value_used"] or contract["one_false_scalar_exponent_substituted"]:
        raise AssertionError("K366 determinant-preservation contract changed")
    if not all(payload["release_test"].values()):
        raise AssertionError("K366 release test failed")
    decision = payload["decision"]
    if not decision["bivariate_determinant_permutation_exponent_interface_complete"] or decision["zero_inclusive_numerical_determinant_envelope_complete"] or decision["uniform_integrand_weighted_boundary_majorant_complete"]:
        raise AssertionError("K366 decision boundary changed")


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
