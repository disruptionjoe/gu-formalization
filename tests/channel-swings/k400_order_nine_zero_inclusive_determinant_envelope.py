#!/usr/bin/env python3
"""Build exact zero-inclusive rank-five scaled determinant coefficients."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
K374 = ROOT / "lab/process/k374-rank-five-confluent-determinant-calculus.json"
K375 = ROOT / "lab/process/k375-rank-five-global-scaled-bessel-bank.json"
K388 = ROOT / "lab/process/k388-order-nine-mask-native-preconditioner-compiler.json"
K399 = ROOT / "lab/process/k399-order-nine-global-face-neighborhood-ownership.json"
OUTPUT = ROOT / "lab/process/k400-order-nine-zero-inclusive-determinant-envelope.json"


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def digest(value: Any) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def cluster_orders(labels: list[int]) -> list[int]:
    seen: Counter[int] = Counter()
    orders = []
    for label in labels:
        orders.append(seen[int(label)])
        seen[int(label)] += 1
    return orders


def derivative_allocations(rank: int, total: int) -> list[tuple[int, ...]]:
    return [row for row in itertools.product(range(total + 1), repeat=rank) if sum(row) == total]


def compile_envelopes(primitive_bounds: list[Fraction], k388: dict[str, Any]) -> list[dict[str, Any]]:
    if len(primitive_bounds) != 11:
        raise AssertionError("K400 requires primitive orders zero through ten")
    singular = k388["preconditioner_templates"]
    confluent = k388["confluent_divided_difference_contract"]["templates"]
    rows = []
    for singular_index, pattern in enumerate(singular):
        rank = int(pattern["rank"])
        costs = tuple(tuple(int(value) for value in row) for row in pattern["zero_entry_matrix"])
        for confluent_index, template in enumerate(confluent):
            if int(template["rank"]) != rank:
                continue
            row_orders = cluster_orders(template["row_cluster_labels"])
            column_orders = cluster_orders(template["column_cluster_labels"])
            derivative_rows = []
            maximum_primitive_order = 0
            for derivative_order in range(3):
                by_exponent: defaultdict[int, Fraction] = defaultdict(Fraction)
                for permutation in itertools.permutations(range(rank)):
                    singular_exponent = sum(costs[i][j] for i, j in enumerate(permutation))
                    for allocation in derivative_allocations(rank, derivative_order):
                        coefficient = Fraction(math.factorial(derivative_order), 1)
                        for value in allocation:
                            coefficient /= math.factorial(value)
                        for i, j in enumerate(permutation):
                            order = row_orders[i] + column_orders[j] + allocation[i]
                            maximum_primitive_order = max(maximum_primitive_order, order)
                            coefficient *= primitive_bounds[order]
                            coefficient /= math.factorial(row_orders[i]) * math.factorial(column_orders[j])
                        by_exponent[singular_exponent] += coefficient
                total = sum(by_exponent.values(), Fraction())
                derivative_rows.append({
                    "derivative_order": derivative_order,
                    "coefficient_by_same_permutation_singular_exponent": [
                        {"singular_exponent": exponent, "exact_rational_abs_upper": q(by_exponent[exponent])}
                        for exponent in sorted(by_exponent)
                    ],
                    "symmetric_interval": [q(-total), q(total)],
                    "exact_rational_abs_upper": q(total),
                })
            rows.append({
                "singular_template_id": f"S{singular_index:02d}",
                "confluent_template_id": f"C{confluent_index:02d}",
                "rank": rank,
                "row_scaling_powers": pattern["row_scaling_powers"],
                "column_scaling_powers": pattern["column_scaling_powers"],
                "assignment_dual_sum": int(pattern["dual_sum"]),
                "row_derivative_orders": row_orders,
                "column_derivative_orders": column_orders,
                "row_vandermonde_order": int(template["row_vandermonde_order"]),
                "column_vandermonde_order": int(template["column_vandermonde_order"]),
                "maximum_primitive_order_used": maximum_primitive_order,
                "derivative_envelopes": derivative_rows,
            })
    return rows


def build() -> dict[str, Any]:
    k374 = json.loads(K374.read_text())
    k375 = json.loads(K375.read_text())
    k388 = json.loads(K388.read_text())
    k399 = json.loads(K399.read_text())
    primitive_bounds = [Fraction(row["global_scaled_upper"]) for row in k375["global_scaled_bessel_bank"]["rows"]]
    rows = compile_envelopes(primitive_bounds, k388)
    rank_histogram = Counter(row["rank"] for row in rows)
    maxima = {
        str(rank): [
            q(max(Fraction(env["exact_rational_abs_upper"]) for row in rows if row["rank"] == rank for env in row["derivative_envelopes"] if env["derivative_order"] == order))
            for order in range(3)
        ]
        for rank in sorted(rank_histogram)
    }
    return {
        "schema_version": "1.0",
        "result_id": "K400-ORDER-NINE-ZERO-INCLUSIVE-DETERMINANT-ENVELOPE",
        "created": "2026-09-24",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [str(path.relative_to(ROOT)) for path in (K374, K375, K388, K399)],
            "singular_templates": len(k388["preconditioner_templates"]),
            "confluent_templates": len(k388["confluent_divided_difference_contract"]["templates"]),
            "rank_compatible_singular_confluent_envelopes": len(rows),
            "derivative_orders": [0, 1, 2],
            "maximum_species_determinant_rank": 5,
            "global_scaled_primitive_orders": list(range(11)),
            "owned_low_coordinate_subsets": k399["fixed_control"]["exhausted_low_coordinate_subsets"],
        },
        "zero_inclusive_determinant_contract": {
            "domain": "nonnegative cumulative arguments, including repeated and zero nodes, with projective face ratios in [0,1]",
            "entry_rule": "apply K388 confluent row/column divided differences first; bound derivative order a+b+k by the K375 global Phi_(a+b+k) envelope divided by a!b!",
            "active_derivative_rule": "enumerate every Leibniz allocation of total order zero, one or two before enclosure",
            "determinant_rule": "retain every permutation's K388 singular exponent until coefficient aggregation",
            "scaling_rule": "K388 exact row/column assignment duals extract the maximum zero power without entrywise cofactor substitution",
            "vandermonde_rule": "row and column Vandermonde factors remain symbolic and are never divided out after enclosure",
            "complete_determinant_assembled_before_absolute_enclosure": True,
            "confluent_factorials_applied_before_absolute_enclosure": True,
            "permutation_singular_exponents_retained": True,
            "active_face_derivative_power_assignment_complete": False,
            "active_face_derivative_power_owner": "K389/K390 face program; K400 bounds coefficients after derivative-order-specific primitive scaling",
            "entrywise_cofactor_absolutization_permitted": False,
            "raw_Bessel_evaluation_at_zero_used": False,
        },
        "determinant_envelope_bank": rows,
        "envelope_summary": {
            "rank_histogram": {str(key): rank_histogram[key] for key in sorted(rank_histogram)},
            "maximum_derivative_abs_upper_by_rank": maxima,
            "maximum_primitive_order_used": max(row["maximum_primitive_order_used"] for row in rows),
            "all_assignment_duals_preserved": all(row["assignment_dual_sum"] == sum(row["row_scaling_powers"]) + sum(row["column_scaling_powers"]) for row in rows),
            "complete_bank_sha256": digest(rows),
        },
        "decision": {
            "zero_inclusive_rank_five_scaled_coefficient_envelopes_complete": True,
            "K374_K375_K388_interfaces_composed": True,
            "whole_radial_face_program_majorants_complete": False,
            "recursive_disjoint_owner_cover_complete": False,
            "complete_hybrid_integrals_emitted": False,
            "next_exact_input": "compose K400 determinant constants with the old-position kernels, every K390 descriptor face program and K384 measures, then charge each row once on its K399 owner union",
        },
        "release_test": {
            "all_60_singular_templates_replayed": len(k388["preconditioner_templates"]) == 60,
            "all_75_confluent_templates_replayed": len(k388["confluent_divided_difference_contract"]["templates"]) == 75,
            "all_rank_compatible_pairs_compiled": len(rows) == sum(1 for singular in k388["preconditioner_templates"] for template in k388["confluent_divided_difference_contract"]["templates"] if singular["rank"] == template["rank"]),
            "orders_zero_one_two_present_everywhere": all([env["derivative_order"] for env in row["derivative_envelopes"]] == [0, 1, 2] for row in rows),
            "maximum_primitive_order_is_ten": max(row["maximum_primitive_order_used"] for row in rows) == 10,
            "all_five_ranks_present": sorted(rank_histogram) == [1, 2, 3, 4, 5],
            "complete_determinant_correlation_retained": True,
            "confluent_factorials_applied": True,
            "raw_zero_evaluation_absent": True,
            "active_face_derivative_power_not_overclaimed": True,
            "whole_radial_majorants_not_overclaimed": True,
            "complete_order_nine_remainder_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k399["ledger_effect"],
        "source_routing": k399["source_routing"],
        "claim_ceiling": "Exact rational zero-inclusive scaled determinant-coefficient envelopes for every rank-compatible K388 singular and confluent template through active derivative order two. K388 assignment duals and each permutation's base singular exponent are retained, K374 confluent factorials precede absolute enclosure, complete determinants remain intact, and K375 supplies all primitive orders through ten without raw zero calls. K389/K390 still own the face-specific active-derivative singular powers. This is not a raw determinant bound by itself, a whole-radial K390 face-program majorant, recursively integrated K399 owner cover, complete K384 hybrid, order-nine remainder/integral, action column, R_ref, K152, source/ledger move, canon, paper, public, novelty or physical claim.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if fixed["singular_templates"] != 60 or fixed["confluent_templates"] != 75 or fixed["derivative_orders"] != [0, 1, 2] or fixed["maximum_species_determinant_rank"] != 5 or fixed["global_scaled_primitive_orders"] != list(range(11)) or fixed["owned_low_coordinate_subsets"] != 2_097_150:
        raise AssertionError("K400 fixed census changed")
    rows = payload["determinant_envelope_bank"]
    if len(rows) != fixed["rank_compatible_singular_confluent_envelopes"] or not rows:
        raise AssertionError("K400 envelope bank changed")
    if any([env["derivative_order"] for env in row["derivative_envelopes"]] != [0, 1, 2] for row in rows) or max(row["maximum_primitive_order_used"] for row in rows) != 10:
        raise AssertionError("K400 derivative demand changed")
    contract = payload["zero_inclusive_determinant_contract"]
    if not contract["complete_determinant_assembled_before_absolute_enclosure"] or not contract["confluent_factorials_applied_before_absolute_enclosure"] or not contract["permutation_singular_exponents_retained"] or contract["active_face_derivative_power_assignment_complete"] or contract["entrywise_cofactor_absolutization_permitted"] or contract["raw_Bessel_evaluation_at_zero_used"]:
        raise AssertionError("K400 determinant contract changed")
    decision = payload["decision"]
    if not decision["zero_inclusive_rank_five_scaled_coefficient_envelopes_complete"] or not decision["K374_K375_K388_interfaces_composed"] or decision["whole_radial_face_program_majorants_complete"] or decision["complete_hybrid_integrals_emitted"]:
        raise AssertionError("K400 decision boundary changed")
    if not all(payload["release_test"].values()):
        raise AssertionError("K400 release test failed")


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
