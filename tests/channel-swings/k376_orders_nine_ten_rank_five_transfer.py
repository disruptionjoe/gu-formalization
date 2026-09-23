#!/usr/bin/env python3
"""Bind the accepted rank-five calculus separately to orders nine and ten."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
K179_PATH = HERE / "k179_matched_normal_order_coefficient_family.py"
K343 = ROOT / "lab/process/k343-higher-order-value-mode-transfer-gate.json"
K373 = ROOT / "lab/process/k373-order-nine-rank-five-determinant-atlas.json"
K374 = ROOT / "lab/process/k374-rank-five-confluent-determinant-calculus.json"
K375 = ROOT / "lab/process/k375-rank-five-global-scaled-bessel-bank.json"
OUTPUT = ROOT / "lab/process/k376-orders-nine-ten-rank-five-transfer.json"
ORDERS = (9, 10)
EXPECTED = {9: (256, 20, 2368, 4480, 5, (2, 4, 6, 8)), 10: (480, 28, 6890, 13300, 5, (1, 3, 5, 7, 9))}


def load_k179():
    spec = importlib.util.spec_from_file_location("k179_for_k376", K179_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {K179_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


K179 = load_k179()


def digest(value: Any) -> str:
    return "sha256:" + hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def occurrences(term: dict[str, Any]) -> dict[str, tuple[int, ...]]:
    rows: dict[str, list[int]] = defaultdict(list)
    for position, species in zip(term["output_variable_provenance"], term["output_letters"], strict=True):
        rows[str(species)].append(int(position))
    return {key: tuple(value) for key, value in sorted(rows.items())}


def order_summary(order: int, terms: list[dict[str, Any]]) -> dict[str, Any]:
    groups: dict[tuple[int, str], list[dict[str, Any]]] = defaultdict(list)
    for term in terms:
        if int(term["order"]) == order:
            groups[(int(term["seed_impurity"]), str(term["output_signature"]))].append(term)
    patterns: Counter[str] = Counter()
    entry_interface = []
    for group, paths in sorted(groups.items()):
        for left_index, left in enumerate(paths):
            left_occ = occurrences(left)
            for right in paths[left_index:]:
                right_occ = occurrences(right)
                factors = []
                for species in left_occ:
                    left_positions = tuple(sorted(left_occ[species]))
                    right_positions = tuple(sorted(right_occ[species]))
                    if len(left_positions) != len(right_positions):
                        raise AssertionError("non-square species determinant")
                    key = f"m{len(left_positions)}|L{','.join(map(str, left_positions))}|R{','.join(map(str, right_positions))}"
                    patterns[key] += 1
                    factors.append({"species": species, "pattern": key})
                entry_interface.append({
                    "group": f"seed={group[0]}|{group[1]}",
                    "left": str(left["contraction_id"]),
                    "right": str(right["contraction_id"]),
                    "coefficient_product": int(left["exact_operator_coefficient"]) * int(right["exact_operator_coefficient"]),
                    "factors": factors,
                })
    rank_occurrences: Counter[int] = Counter()
    rank_patterns: Counter[int] = Counter()
    serialized_patterns = []
    for key in sorted(patterns):
        rank = int(key.split("|", 1)[0][1:])
        rank_occurrences[rank] += patterns[key]
        rank_patterns[rank] += 1
        serialized_patterns.append({"pattern": key, "rank": rank, "occurrences": patterns[key]})
    paths = sum(len(value) for value in groups.values())
    upper = sum(len(value) * (len(value) + 1) // 2 for value in groups.values())
    ordered = sum(len(value) ** 2 for value in groups.values())
    positions = tuple(sorted({int(term["old_position"]) for value in groups.values() for term in value}))
    maximum = max(rank_patterns)
    if (paths, len(groups), upper, ordered, maximum, positions) != EXPECTED[order]:
        raise AssertionError(f"order {order} transfer census changed")
    return {
        "order": order,
        "paths": paths,
        "groups": len(groups),
        "upper_triangle_gram_entries": upper,
        "ordered_quadratic_terms": ordered,
        "old_position_support": list(positions),
        "maximum_rank": maximum,
        "positive_time_variables": 2 * (order + 1),
        "native_prefactor": f"(2*pi)^-{order + 2}",
        "unique_patterns_by_rank": {str(key): value for key, value in sorted(rank_patterns.items())},
        "factor_occurrences_by_rank": {str(key): value for key, value in sorted(rank_occurrences.items())},
        "pattern_inventory": serialized_patterns,
        "pattern_inventory_sha256": digest(serialized_patterns),
        "complete_entry_interface_sha256": digest(entry_interface),
    }


def build() -> dict[str, Any]:
    k343 = json.loads(K343.read_text())
    k373 = json.loads(K373.read_text())
    k374 = json.loads(K374.read_text())
    k375 = json.loads(K375.read_text())
    terms = K179.coefficient_family()
    rows = [order_summary(order, terms) for order in ORDERS]
    source = {row["order"]: row for row in k343["orders"]}
    for row in rows:
        old = source[row["order"]]
        if (row["paths"], row["groups"], row["upper_triangle_gram_entries"], row["ordered_quadratic_terms"], row["maximum_rank"], row["old_position_support"]) != (old["paths"], old["groups"], old["upper_triangle_gram_entries"], old["ordered_quadratic_terms"], old["maximum_species_determinant_rank"], old["old_position_support"]):
            raise AssertionError("K343 transfer mismatch")
    order_nine = rows[0]
    k373_rank_five_occurrences = k373["complete_factorization_inventory"]["rank_five_occurrences"]
    if order_nine["factor_occurrences_by_rank"].get("5") != k373_rank_five_occurrences:
        raise AssertionError("K373 rank-five occurrence transfer changed")
    calculus_ready = k374["fixed_control"]["maximum_rank"] == 5 and k375["fixed_control"]["maximum_derivative_order"] == 10
    if not calculus_ready:
        raise AssertionError("rank-five calculus not ready")
    return {
        "schema_version": "1.0",
        "result_id": "K376-ORDERS-NINE-TEN-RANK-FIVE-TRANSFER",
        "created": "2026-09-23",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [str(path.relative_to(ROOT)) for path in (K343, K373, K374, K375)],
            "orders": list(ORDERS),
            "paths": sum(row["paths"] for row in rows),
            "coherent_groups": sum(row["groups"] for row in rows),
            "upper_triangle_gram_entries": sum(row["upper_triangle_gram_entries"] for row in rows),
            "ordered_quadratic_terms": sum(row["ordered_quadratic_terms"] for row in rows),
            "maximum_rank": max(row["maximum_rank"] for row in rows),
        },
        "order_interfaces": rows,
        "calculus_binding": {
            "rank_five_gap_free_confluence": k374["decision"]["rank_five_gap_free_confluent_determinant_calculus_emitted"],
            "global_scaled_derivatives_through_order_ten": k375["decision"]["zero_safe_global_scaled_derivative_bank_complete_through_order_ten"],
            "every_pattern_rank_at_most_five": all(row["maximum_rank"] <= 5 for row in rows),
            "every_required_primitive_order_present": k375["global_scaled_bessel_bank"]["orders"] == list(range(11)),
            "order_specific_counts_retained": True,
            "order_specific_prefactors_retained": [row["native_prefactor"] for row in rows] == ["(2*pi)^-11", "(2*pi)^-12"],
            "order_specific_positive_time_counts_retained": [row["positive_time_variables"] for row in rows] == [20, 22],
            "order_eight_node_or_face_atlas_reused": False,
        },
        "decision": {
            "rank_five_determinant_confluence_derivative_calculus_complete": True,
            "order_nine_interface_bound": True,
            "order_ten_interface_bound": True,
            "numerical_order_nine_integral_emitted": False,
            "numerical_order_ten_integral_emitted": False,
            "rank_six_orders_eleven_twelve_released": True,
            "next_exact_input": "construct the gap-free rank-six determinant calculus and global scaled derivative bank through order twelve, then bind them separately to orders eleven and twelve",
        },
        "release_test": {
            "all_736_paths_replayed": sum(row["paths"] for row in rows) == 736,
            "all_48_groups_replayed": sum(row["groups"] for row in rows) == 48,
            "all_9258_upper_triangle_entries_replayed": sum(row["upper_triangle_gram_entries"] for row in rows) == 9258,
            "all_17780_ordered_terms_replayed": sum(row["ordered_quadratic_terms"] for row in rows) == 17780,
            "K373_rank_five_occurrences_replayed": order_nine["factor_occurrences_by_rank"].get("5") == k373_rank_five_occurrences,
            "all_patterns_bound_to_rank_five_or_lower": all(row["maximum_rank"] <= 5 for row in rows),
            "orders_nine_and_ten_remain_distinct": rows[0]["pattern_inventory_sha256"] != rows[1]["pattern_inventory_sha256"],
            "numerical_integrals_not_overclaimed": True,
            "action_column_not_emitted": True,
            "R_ref_not_emitted": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k375["ledger_effect"],
        "source_routing": k375["source_routing"],
        "claim_ceiling": "Exact transfer of the accepted gap-free rank-five determinant calculus and global zero-safe derivative bank through order ten to every order-nine and order-ten K179 factor. The two orders retain separate path/group/Gram/ordered-term censuses, time dimensions and prefactors; 736 paths, 48 groups, 9,258 upper-triangle entries and 17,780 ordered terms replay. No order-eight node or face atlas is reused. Numerical higher-order integrals, the action column, R_ref, K152, source/ledger move, canon, paper, public, novelty and physical claims remain open."
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["orders"], fixed["paths"], fixed["coherent_groups"], fixed["upper_triangle_gram_entries"], fixed["ordered_quadratic_terms"], fixed["maximum_rank"]) != ([9, 10], 736, 48, 9258, 17780, 5):
        raise AssertionError("K376 fixed census changed")
    rows = payload["order_interfaces"]
    if len(rows) != 2 or [row["order"] for row in rows] != [9, 10] or any(row["maximum_rank"] != 5 for row in rows):
        raise AssertionError("K376 order interface changed")
    binding = payload["calculus_binding"]
    if not all(binding[key] for key in ("rank_five_gap_free_confluence", "global_scaled_derivatives_through_order_ten", "every_pattern_rank_at_most_five", "every_required_primitive_order_present", "order_specific_counts_retained", "order_specific_prefactors_retained", "order_specific_positive_time_counts_retained")) or binding["order_eight_node_or_face_atlas_reused"]:
        raise AssertionError("K376 calculus binding changed")
    decision = payload["decision"]
    if not all(decision[key] for key in ("rank_five_determinant_confluence_derivative_calculus_complete", "order_nine_interface_bound", "order_ten_interface_bound", "rank_six_orders_eleven_twelve_released")) or decision["numerical_order_nine_integral_emitted"] or decision["numerical_order_ten_integral_emitted"]:
        raise AssertionError("K376 decision boundary changed")
    if not all(payload["release_test"].values()):
        raise AssertionError("K376 release test failed")


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
