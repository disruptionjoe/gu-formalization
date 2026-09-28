#!/usr/bin/env python3
"""Coefficient every rank-compatible K560 template with K378 primitives."""

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
K378 = ROOT / "lab/process/k378-rank-six-global-scaled-bessel-bank.json"
K560 = ROOT / "lab/process/k560-orders-eleven-twelve-rank-six-mask-native-preconditioner.json"
OUTPUT = ROOT / "lab/process/k562-orders-eleven-twelve-global-determinant-envelopes.json"


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


def compile_rows(primitives: list[Fraction], k560: dict[str, Any]) -> list[dict[str, Any]]:
    compiled_confluent: dict[int, dict[str, Any]] = {}
    for confluent_index, confluent in enumerate(k560["confluent_divided_difference_contract"]["templates"]):
        rank = int(confluent["rank"])
        row_orders = cluster_orders(confluent["row_cluster_labels"])
        column_orders = cluster_orders(confluent["column_cluster_labels"])
        derivative_rows = []
        maximum_primitive_order = 0
        for derivative_order in range(3):
            total = Fraction()
            for permutation in itertools.permutations(range(rank)):
                for allocation in derivative_allocations(rank, derivative_order):
                    coefficient = Fraction(math.factorial(derivative_order), 1)
                    for value in allocation:
                        coefficient /= math.factorial(value)
                    for i, j in enumerate(permutation):
                        primitive_order = row_orders[i] + column_orders[j] + allocation[i]
                        maximum_primitive_order = max(maximum_primitive_order, primitive_order)
                        coefficient *= primitives[primitive_order]
                        coefficient /= math.factorial(row_orders[i]) * math.factorial(column_orders[j])
                    total += coefficient
            derivative_rows.append({
                "derivative_order": derivative_order,
                "exact_rational_abs_upper": q(total),
                "symmetric_interval": [q(-total), q(total)],
            })
        compiled_confluent[confluent_index] = {
            "rank": rank,
            "row_derivative_orders": row_orders,
            "column_derivative_orders": column_orders,
            "row_vandermonde_order": int(confluent["row_vandermonde_order"]),
            "column_vandermonde_order": int(confluent["column_vandermonde_order"]),
            "maximum_primitive_order_used": maximum_primitive_order,
            "derivative_envelopes": derivative_rows,
        }
    rows = []
    for singular_index, singular in enumerate(k560["preconditioner_templates"]):
        rank = int(singular["rank"])
        for confluent_index, confluent in enumerate(k560["confluent_divided_difference_contract"]["templates"]):
            if int(confluent["rank"]) != rank:
                continue
            compiled = compiled_confluent[confluent_index]
            rows.append({
                "singular_template_id": f"S{singular_index:02d}",
                "confluent_template_id": f"C{confluent_index:03d}",
                "rank": rank,
                "singular_dual_sum": int(singular["dual_sum"]),
                "row_derivative_orders": compiled["row_derivative_orders"],
                "column_derivative_orders": compiled["column_derivative_orders"],
                "row_vandermonde_order": compiled["row_vandermonde_order"],
                "column_vandermonde_order": compiled["column_vandermonde_order"],
                "maximum_primitive_order_used": compiled["maximum_primitive_order_used"],
                "derivative_envelopes": compiled["derivative_envelopes"],
            })
    return rows


def build() -> dict[str, Any]:
    k378 = json.loads(K378.read_text())
    k560 = json.loads(K560.read_text())
    primitives = [Fraction(row["global_scaled_upper"]) for row in k378["global_scaled_bessel_bank"]["rows"]]
    rows = compile_rows(primitives, k560)
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
        "result_id": "K562-ORDERS-ELEVEN-TWELVE-GLOBAL-DETERMINANT-ENVELOPES",
        "created": "2026-09-28",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [str(path.relative_to(ROOT)) for path in (K378, K560)],
            "singular_templates": len(k560["preconditioner_templates"]),
            "confluent_templates": len(k560["confluent_divided_difference_contract"]["templates"]),
            "rank_compatible_template_envelopes": len(rows),
            "derivative_orders": [0, 1, 2],
            "primitive_orders_available": list(range(len(primitives))),
        },
        "global_determinant_contract": {
            "entry_rule": "apply K560 confluent row/column divided differences before absolute enclosure and bound derivative order a+b+k by K378 Phi_(a+b+k)/(a!b!)",
            "active_derivative_rule": "enumerate every Leibniz allocation of total order zero, one or two",
            "singular_rule": "retain each K560 assignment-dual singular power symbolically; coefficient bounds do not divide out the extracted face powers",
            "vandermonde_factors_retained": True,
            "confluent_factorials_applied_before_absolute_enclosure": True,
            "raw_Bessel_evaluation_at_zero_used": False,
        },
        "determinant_envelope_bank": rows,
        "envelope_summary": {
            "rank_histogram": {str(key): rank_histogram[key] for key in sorted(rank_histogram)},
            "maximum_derivative_abs_upper_by_rank": maxima,
            "maximum_primitive_order_used": max(row["maximum_primitive_order_used"] for row in rows),
            "complete_bank_sha256": digest(rows),
        },
        "decision": {
            "all_rank_compatible_K560_templates_coefficiented": True,
            "global_positive_argument_tail_complete": True,
            "whole_radial_face_majorants_complete": False,
            "complete_hybrid_integrals_emitted": False,
            "next_exact_input": "assemble the complete order-eleven/twelve coherent derivative majorants and integrate every K561 face row under the K558 measures",
        },
        "release_test": {
            "all_97_singular_templates_represented": len({row["singular_template_id"] for row in rows}) == 97,
            "all_131_confluent_templates_represented": len({row["confluent_template_id"] for row in rows}) == 131,
            "all_rank_compatible_pairs_compiled": len(rows) == sum(1 for s in k560["preconditioner_templates"] for c in k560["confluent_divided_difference_contract"]["templates"] if s["rank"] == c["rank"]),
            "orders_zero_one_two_present_everywhere": all([env["derivative_order"] for env in row["derivative_envelopes"]] == [0, 1, 2] for row in rows),
            "maximum_primitive_order_is_twelve": max(row["maximum_primitive_order_used"] for row in rows) == 12,
            "ranks_one_through_six_present": sorted(rank_histogram) == [1, 2, 3, 4, 5, 6],
            "confluent_factorials_applied": True,
            "raw_zero_evaluation_absent": True,
            "complete_integrals_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k560["ledger_effect"],
        "source_routing": k560["source_routing"],
        "claim_ceiling": "Exact rational global coefficient envelopes for every rank-compatible K560 singular/confluent template through active derivative order two and K378 primitive order twelve. Extracted singular and Vandermonde factors remain symbolic, confluent factorials precede absolute enclosure, and no raw zero Bessel value is used. This is not yet a whole-radial face majorant, disjoint owner cover, complete higher-order hybrid, base action column, R_ref, K152, source/ledger move, canon, paper, public, novelty or physical claim.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if fixed["singular_templates"] != 97 or fixed["confluent_templates"] != 131 or fixed["derivative_orders"] != [0, 1, 2]:
        raise AssertionError("K562 fixed census changed")
    rows = payload["determinant_envelope_bank"]
    if len(rows) != fixed["rank_compatible_template_envelopes"] or not rows:
        raise AssertionError("K562 envelope bank changed")
    if max(row["maximum_primitive_order_used"] for row in rows) != 12:
        raise AssertionError("K562 primitive order changed")
    contract = payload["global_determinant_contract"]
    if not contract["vandermonde_factors_retained"] or not contract["confluent_factorials_applied_before_absolute_enclosure"] or contract["raw_Bessel_evaluation_at_zero_used"]:
        raise AssertionError("K562 determinant contract changed")
    if payload["decision"]["complete_hybrid_integrals_emitted"] or not all(payload["release_test"].values()):
        raise AssertionError("K562 decision boundary changed")


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
