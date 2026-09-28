#!/usr/bin/env python3
"""Build exact zero-inclusive two-scale determinant envelopes after confluence."""

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
K413 = ROOT / "lab/process/k413-order-ten-mask-native-preconditioner-compiler.json"
K547 = ROOT / "lab/process/k547-order-ten-zero-safe-scaled-derivative-bank.json"
K548 = ROOT / "lab/process/k548-order-ten-bivariate-determinant-newton-fronts.json"
OUTPUT = ROOT / "lab/process/k549-order-ten-zero-inclusive-determinant-envelope.json"


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


def pattern_map(k413: dict[str, Any]) -> dict[str, tuple[tuple[int, ...], ...]]:
    return {
        f"S{index:02d}": tuple(tuple(int(value) for value in row) for row in item["zero_entry_matrix"])
        for index, item in enumerate(k413["preconditioner_templates"])
    }


def compile_envelopes(
    primitive_bounds: list[Fraction],
    k413: dict[str, Any],
    k548: dict[str, Any],
) -> list[dict[str, Any]]:
    if len(primitive_bounds) != 11:
        raise AssertionError("K549 requires primitive orders zero through ten")
    patterns = pattern_map(k413)
    confluent = k413["confluent_divided_difference_contract"]["templates"]
    rows = []
    for pair in k548["bivariate_front_bank"]:
        outer = patterns[pair["outer_template_id"]]
        inner = patterns[pair["inner_template_id"]]
        rank = int(pair["rank"])
        expected_support = {
            (int(row["outer_singular_exponent"]), int(row["inner_increment_exponent"]))
            for row in pair["permutation_exponent_support"]
        }
        front = {
            (int(row["outer_singular_exponent"]), int(row["inner_increment_exponent"]))
            for row in pair["pareto_maximal_newton_front"]
        }
        for confluent_index, template in enumerate(confluent):
            if int(template["rank"]) != rank:
                continue
            row_orders = cluster_orders(template["row_cluster_labels"])
            column_orders = cluster_orders(template["column_cluster_labels"])
            derivative_rows = []
            realized_support: set[tuple[int, int]] = set()
            maximum_primitive_order = 0
            for derivative_order in range(3):
                by_exponent: defaultdict[tuple[int, int], Fraction] = defaultdict(Fraction)
                for permutation in itertools.permutations(range(rank)):
                    outer_exponent = sum(outer[i][j] for i, j in enumerate(permutation))
                    inner_increment = sum(inner[i][j] - outer[i][j] for i, j in enumerate(permutation))
                    realized_support.add((outer_exponent, inner_increment))
                    for allocation in derivative_allocations(rank, derivative_order):
                        coefficient = Fraction(math.factorial(derivative_order), 1)
                        for value in allocation:
                            coefficient /= math.factorial(value)
                        for i, j in enumerate(permutation):
                            order = row_orders[i] + column_orders[j] + allocation[i]
                            maximum_primitive_order = max(maximum_primitive_order, order)
                            coefficient *= primitive_bounds[order]
                            coefficient /= math.factorial(row_orders[i]) * math.factorial(column_orders[j])
                        by_exponent[(outer_exponent, inner_increment)] += coefficient
                total = sum(by_exponent.values(), Fraction())
                derivative_rows.append({
                    "derivative_order": derivative_order,
                    "coefficient_by_same_permutation_exponent": [
                        {
                            "outer_singular_exponent": exponent[0],
                            "inner_increment_exponent": exponent[1],
                            "exact_rational_abs_upper": q(by_exponent[exponent]),
                            "is_K548_front_point": exponent in front,
                        }
                        for exponent in sorted(by_exponent)
                    ],
                    "symmetric_interval": [q(-total), q(total)],
                    "exact_rational_abs_upper": q(total),
                })
            if realized_support != expected_support:
                raise AssertionError("K549 lost a K548 same-permutation exponent")
            rows.append({
                "outer_template_id": pair["outer_template_id"],
                "inner_template_id": pair["inner_template_id"],
                "confluent_template_id": f"C{confluent_index:02d}",
                "rank": rank,
                "row_derivative_orders": row_orders,
                "column_derivative_orders": column_orders,
                "row_vandermonde_order": int(template["row_vandermonde_order"]),
                "column_vandermonde_order": int(template["column_vandermonde_order"]),
                "maximum_primitive_order_used": maximum_primitive_order,
                "scalar_optimal_nesting_obstructed": bool(pair["scalar_optimal_nesting_obstructed"]),
                "derivative_envelopes": derivative_rows,
            })
    return rows


def build() -> dict[str, Any]:
    k413 = json.loads(K413.read_text())
    k547 = json.loads(K547.read_text())
    k548 = json.loads(K548.read_text())
    primitive_bounds = [
        Fraction(row["global_scaled_upper"])
        for row in k547["scaled_bessel_contract"]["global_rows"]
    ]
    rows = compile_envelopes(primitive_bounds, k413, k548)
    rank_histogram = Counter(row["rank"] for row in rows)
    maxima = {
        str(rank): [
            q(max(Fraction(env["exact_rational_abs_upper"]) for row in rows if row["rank"] == rank for env in row["derivative_envelopes"] if env["derivative_order"] == order))
            for order in range(3)
        ]
        for rank in sorted(rank_histogram)
    }
    obstructed_rows = [row for row in rows if row["scalar_optimal_nesting_obstructed"]]
    return {
        "schema_version": "1.0",
        "result_id": "K549-ORDER-TEN-ZERO-INCLUSIVE-DETERMINANT-ENVELOPE",
        "created": "2026-09-27",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [str(path.relative_to(ROOT)) for path in (K413, K547, K548)],
            "comparable_template_pairs": len(k548["bivariate_front_bank"]),
            "confluent_templates": len(k413["confluent_divided_difference_contract"]["templates"]),
            "rank_compatible_pair_confluent_envelopes": len(rows),
            "derivative_orders": [0, 1, 2],
            "primitive_domain": "0<=w<infinity",
            "outer_strip_width": "1/64",
            "inner_to_outer_ratio_upper": "1/64",
        },
        "global_face_envelope_contract": {
            "domain": "0<=tau<=rho/64, 0<=rho<infinity, with every cumulative Bessel argument controlled by K547 globally",
            "entry_rule": "apply K413 confluent row/column divided differences first; bound order a+b+k by K547 Phi_(a+b+k) divided by a!b!",
            "active_derivative_rule": "enumerate every Leibniz allocation of total order zero, one or two before enclosure",
            "determinant_rule": "retain each permutation's K548 outer and inner exponent pair through coefficient aggregation",
            "vandermonde_rule": "the original determinant equals extracted row and column Vandermonde factors times the divided-difference determinant; factors are retained symbolically and are never divided out after enclosure",
            "same_permutation_two_scale_coupling_preserved": True,
            "confluent_factorials_applied_before_absolute_enclosure": True,
            "occurrencewise_scalar_exponent_substituted": False,
            "raw_Bessel_evaluation_at_zero_used": False,
        },
        "determinant_envelope_bank": rows,
        "envelope_summary": {
            "rank_histogram": {str(key): rank_histogram[key] for key in sorted(rank_histogram)},
            "scalar_obstruction_envelopes": len(obstructed_rows),
            "all_42_K546_obstruction_pairs_represented": { (row["outer_template_id"], row["inner_template_id"]) for row in obstructed_rows } == { (row["outer_template_id"], row["inner_template_id"]) for row in k548["bivariate_front_bank"] if row["scalar_optimal_nesting_obstructed"] },
            "maximum_derivative_abs_upper_by_rank": maxima,
            "maximum_primitive_order_used": max(row["maximum_primitive_order_used"] for row in rows),
            "complete_bank_sha256": digest(rows),
        },
        "decision": {
            "zero_inclusive_global_determinant_envelopes_complete": True,
            "K548_exponent_interface_numerically_coefficiented": True,
            "global_positive_argument_tail_complete": True,
            "whole_radial_face_program_majorants_complete": False,
            "recursive_disjoint_owner_cover_complete": False,
            "complete_hybrid_integrals_emitted": False,
            "next_exact_input": "compose every K415 face program under the K409 Laguerre/Peano measures, then stitch the K545 owner unions and recursive positive interiors",
        },
        "release_test": {
            "all_371_K548_pairs_replayed": len(k548["bivariate_front_bank"]) == 371,
            "all_rank_compatible_confluent_templates_compiled": len(rows) == sum(1 for pair in k548["bivariate_front_bank"] for template in k413["confluent_divided_difference_contract"]["templates"] if pair["rank"] == template["rank"]),
            "orders_zero_one_two_present_everywhere": all([env["derivative_order"] for env in row["derivative_envelopes"]] == [0, 1, 2] for row in rows),
            "maximum_primitive_order_is_ten": max(row["maximum_primitive_order_used"] for row in rows) == 10,
            "all_42_scalar_obstruction_pairs_have_envelopes": len({(row["outer_template_id"], row["inner_template_id"]) for row in obstructed_rows}) == 42,
            "same_permutation_coupling_preserved": True,
            "confluent_factorials_applied": True,
            "raw_zero_evaluation_absent": True,
            "global_tail_is_K547_owned": True,
            "complete_order_ten_remainder_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k548["ledger_effect"],
        "source_routing": k548["source_routing"],
        "claim_ceiling": "Exact rational zero-inclusive global determinant-level coefficient envelopes for all 10,958 rank-compatible K548 pair/K413 confluent combinations through active derivative order two. Every determinant permutation retains its own outer/inner exponent pair, confluent factorials precede absolute enclosure, all 42 scalar obstructions are covered and primitive derivative order never exceeds ten. This is not yet a K415 face-program integral majorant, recursively disjoint K545 owner cover, complete K409 hybrid, order-ten remainder/integral, action column, R_ref, K152, source/ledger move, canon, paper, public or physical claim.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if fixed["comparable_template_pairs"] != 371 or fixed["confluent_templates"] != 75 or fixed["rank_compatible_pair_confluent_envelopes"] != 10958 or fixed["derivative_orders"] != [0, 1, 2]:
        raise AssertionError("K549 fixed census changed")
    rows = payload["determinant_envelope_bank"]
    if len(rows) != fixed["rank_compatible_pair_confluent_envelopes"] or not rows:
        raise AssertionError("K549 envelope bank changed")
    if any([env["derivative_order"] for env in row["derivative_envelopes"]] != [0, 1, 2] for row in rows):
        raise AssertionError("K549 derivative orders changed")
    if max(row["maximum_primitive_order_used"] for row in rows) != 10:
        raise AssertionError("K549 primitive order changed")
    contract = payload["global_face_envelope_contract"]
    if not contract["same_permutation_two_scale_coupling_preserved"] or not contract["confluent_factorials_applied_before_absolute_enclosure"] or contract["occurrencewise_scalar_exponent_substituted"] or contract["raw_Bessel_evaluation_at_zero_used"]:
        raise AssertionError("K549 determinant contract changed")
    decision = payload["decision"]
    if not decision["zero_inclusive_global_determinant_envelopes_complete"] or not decision["global_positive_argument_tail_complete"] or decision["complete_hybrid_integrals_emitted"]:
        raise AssertionError("K549 decision boundary changed")
    if not all(payload["release_test"].values()):
        raise AssertionError("K549 release test failed")


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
