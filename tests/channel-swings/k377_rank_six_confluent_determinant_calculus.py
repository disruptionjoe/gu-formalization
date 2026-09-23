#!/usr/bin/env python3
"""Isolate the order-eleven/twelve rank-six factors and prove their calculus."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import sys
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
K179_PATH = HERE / "k179_matched_normal_order_coefficient_family.py"
K374_PATH = HERE / "k374_rank_five_confluent_determinant_calculus.py"
K343 = ROOT / "lab/process/k343-higher-order-value-mode-transfer-gate.json"
K376 = ROOT / "lab/process/k376-orders-nine-ten-rank-five-transfer.json"
OUTPUT = ROOT / "lab/process/k377-rank-six-confluent-determinant-calculus.json"
ORDERS = (11, 12)
MAX_RANK = 6
MAX_KERNEL_ORDER = 12
EXPECTED = {11: (640, 24, 12920, 25200, 6, (2, 4, 6, 8, 10)), 12: (1152, 33, 35352, 69552, 6, (1, 3, 5, 7, 9, 11))}


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


K179 = load_module(K179_PATH, "k179_for_k377")
K374 = load_module(K374_PATH, "k374_for_k377")


def digest(value: Any) -> str:
    return "sha256:" + hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def occurrences(term: dict[str, Any]) -> dict[str, tuple[int, ...]]:
    rows: dict[str, list[int]] = defaultdict(list)
    for position, species in zip(term["output_variable_provenance"], term["output_letters"], strict=True):
        rows[str(species)].append(int(position))
    return {key: tuple(value) for key, value in sorted(rows.items())}


def factor_summary(order: int, terms: list[dict[str, Any]]) -> dict[str, Any]:
    groups: dict[tuple[int, str], list[dict[str, Any]]] = defaultdict(list)
    for term in terms:
        if int(term["order"]) == order:
            groups[(int(term["seed_impurity"]), str(term["output_signature"]))].append(term)
    patterns: Counter[str] = Counter()
    entry_rows = []
    for group, paths in sorted(groups.items()):
        for left_index, left in enumerate(paths):
            left_occ = occurrences(left)
            for right in paths[left_index:]:
                right_occ = occurrences(right)
                factors = []
                for species in left_occ:
                    lpos = tuple(sorted(left_occ[species]))
                    rpos = tuple(sorted(right_occ[species]))
                    key = f"m{len(lpos)}|L{','.join(map(str, lpos))}|R{','.join(map(str, rpos))}"
                    patterns[key] += 1
                    factors.append({"species": species, "pattern": key})
                entry_rows.append({"group": f"seed={group[0]}|{group[1]}", "left": str(left["contraction_id"]), "right": str(right["contraction_id"]), "coefficient_product": int(left["exact_operator_coefficient"]) * int(right["exact_operator_coefficient"]), "factors": factors})
    rank_patterns: Counter[int] = Counter()
    rank_occurrences: Counter[int] = Counter()
    serialized = []
    for key in sorted(patterns):
        rank = int(key.split("|", 1)[0][1:])
        rank_patterns[rank] += 1
        rank_occurrences[rank] += patterns[key]
        serialized.append({"pattern": key, "rank": rank, "occurrences": patterns[key]})
    paths = sum(len(value) for value in groups.values())
    upper = sum(len(value) * (len(value) + 1) // 2 for value in groups.values())
    ordered = sum(len(value) ** 2 for value in groups.values())
    positions = tuple(sorted({int(term["old_position"]) for value in groups.values() for term in value}))
    maximum = max(rank_patterns)
    if (paths, len(groups), upper, ordered, maximum, positions) != EXPECTED[order]:
        raise AssertionError(f"order {order} rank-six census changed")
    rank_six = [row for row in serialized if row["rank"] == 6]
    return {
        "order": order,
        "paths": paths,
        "groups": len(groups),
        "upper_triangle_gram_entries": upper,
        "ordered_quadratic_terms": ordered,
        "old_position_support": list(positions),
        "maximum_rank": maximum,
        "unique_patterns_by_rank": {str(key): value for key, value in sorted(rank_patterns.items())},
        "factor_occurrences_by_rank": {str(key): value for key, value in sorted(rank_occurrences.items())},
        "rank_six_patterns": rank_six,
        "rank_six_pattern_sha256": digest(rank_six),
        "complete_pattern_inventory_sha256": digest(serialized),
        "complete_entry_interface_sha256": digest(entry_rows),
    }


def polynomial_controls() -> list[dict[str, Any]]:
    rows = []
    for rank in range(1, MAX_RANK + 1):
        left = [Fraction(2 * index + 1, 43) for index in range(rank)]
        right = [Fraction(3 * index + 2, 47) for index in range(rank)]
        for power in range(MAX_KERNEL_ORDER + 1):
            recursive = K374.mixed_divided_difference(left, right, lambda z, p=power: z**p)
            formula = K374.monomial_formula(power, left, right)
            rows.append({"rank": rank, "power": power, "recursive": str(recursive), "gap_free_formula": str(formula), "exact_equality": recursive == formula})
    return rows


def determinant_controls() -> list[dict[str, Any]]:
    rows = []
    for rank in range(1, MAX_RANK + 1):
        left = [Fraction(2 * index + 3, 53) for index in range(rank)]
        right = [Fraction(3 * index + 5, 59) for index in range(rank)]
        direct = K374.determinant([[Fraction(2, 1) / (x + y) for y in right] for x in left])
        transformed = K374.determinant(K374.matrix_divided_differences(left, right))
        replay = transformed * K374.vandermonde_increasing(left) * K374.vandermonde_increasing(right)
        normalized = transformed * math.prod((x + y for x in left for y in right), start=Fraction(1))
        rows.append({"rank": rank, "direct": str(direct), "divided_difference_determinant": str(transformed), "exact_replay": direct == replay, "normalized_cauchy_value": str(normalized), "expected_normalized_value": str(2**rank), "exact_normalization": normalized == 2**rank})
    return rows


def build() -> dict[str, Any]:
    k343 = json.loads(K343.read_text())
    k376 = json.loads(K376.read_text())
    if not k376["decision"]["rank_six_orders_eleven_twelve_released"]:
        raise AssertionError("K376 did not release rank six")
    terms = K179.coefficient_family()
    summaries = [factor_summary(order, terms) for order in ORDERS]
    source = {row["order"]: row for row in k343["orders"]}
    for row in summaries:
        old = source[row["order"]]
        if (row["paths"], row["groups"], row["upper_triangle_gram_entries"], row["ordered_quadratic_terms"], row["maximum_rank"], row["old_position_support"]) != (old["paths"], old["groups"], old["upper_triangle_gram_entries"], old["ordered_quadratic_terms"], old["maximum_species_determinant_rank"], old["old_position_support"]):
            raise AssertionError("K343 rank-six transfer mismatch")
    poly = polynomial_controls()
    dets = determinant_controls()
    if not all(row["exact_equality"] for row in poly) or not all(row["exact_replay"] and row["exact_normalization"] for row in dets):
        raise AssertionError("rank-six exact calculus failed")
    zero_limits = [{"row_order": r, "column_order": c, "monomial_power": r + c, "confluent_value": math.comb(r + c, r)} for r in range(6) for c in range(6)]
    return {
        "schema_version": "1.0",
        "result_id": "K377-RANK-SIX-CONFLUENT-DETERMINANT-CALCULUS",
        "created": "2026-09-23",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [str(path.relative_to(ROOT)) for path in (K343, K376)],
            "orders": list(ORDERS),
            "maximum_rank": MAX_RANK,
            "maximum_row_divided_difference_order": 5,
            "maximum_column_divided_difference_order": 5,
            "active_peano_derivative_order": 2,
            "maximum_kernel_derivative_order": MAX_KERNEL_ORDER,
            "polynomial_identity_checks": len(poly),
            "exact_determinant_checks": len(dets),
        },
        "order_factor_boundaries": summaries,
        "gap_free_tensor_divided_difference": {
            "monomial_identity": "[x_0,...,x_r][y_0,...,y_c](x+y)^p=sum_(k=r)^(p-c) binom(p,k) h_(k-r)(x) h_(p-k-c)(y)",
            "complete_homogeneous_polynomials_are_nonnegative_on_nonnegative_nodes": True,
            "explicit_gap_denominators_after_extension": False,
            "repeated_nodes_allowed_by_continuity": True,
            "polynomial_controls": poly,
            "all_zero_controls": zero_limits,
        },
        "determinant_calculus": {
            "cauchy_identity": "det[2/(x_i+y_j)]=2^m*V(x)*V(y)/product_ij(x_i+y_j)",
            "exact_controls": dets,
            "complete_determinant_assembled_before_absolute_enclosure": True,
            "entrywise_cofactor_absolutization_permitted": False,
        },
        "derivative_demand": {"kernel_orders_required": list(range(13)), "rank_six_confluence_maximum": 10, "pure_second_axis_extension": 2, "total_required": 12, "primitive_bank_complete": False},
        "decision": {
            "rank_six_patterns_isolated_for_orders_eleven_twelve": True,
            "rank_six_gap_free_confluent_determinant_calculus_emitted": True,
            "zero_safe_global_primitive_bank_through_order_twelve_emitted": False,
            "numerical_orders_eleven_twelve_integrals_emitted": False,
            "next_exact_input": "extend the global zero-safe scaled 2*K1 bank through derivative order twelve and bind it to the separate order-eleven and order-twelve interfaces",
        },
        "release_test": {
            "all_1792_paths_replayed": sum(row["paths"] for row in summaries) == 1792,
            "all_57_groups_replayed": sum(row["groups"] for row in summaries) == 57,
            "all_48272_upper_triangle_entries_replayed": sum(row["upper_triangle_gram_entries"] for row in summaries) == 48272,
            "all_94752_ordered_terms_replayed": sum(row["ordered_quadratic_terms"] for row in summaries) == 94752,
            "rank_six_patterns_present_in_both_orders": all(row["rank_six_patterns"] for row in summaries),
            "all_78_polynomial_identities_exact": len(poly) == 78 and all(row["exact_equality"] for row in poly),
            "all_six_determinant_ranks_exact": len(dets) == 6 and all(row["exact_replay"] and row["exact_normalization"] for row in dets),
            "all_36_zero_limits_serialized": len(zero_limits) == 36,
            "global_primitive_bank_not_overclaimed": True,
            "numerical_integrals_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k376["ledger_effect"],
        "source_routing": k376["source_routing"],
        "claim_ceiling": "Exact isolation and gap-free confluence calculus for the rank-six species determinants first required by orders eleven and twelve. All 1,792 paths, 57 groups, 48,272 upper-triangle entries and 94,752 ordered terms replay; 78 rational monomial identities, 36 all-zero limits and exact Cauchy determinant replays through size six pass. The zero-safe global primitive bank through order twelve, numerical integrals, action column, R_ref, K152, source/ledger move, canon, paper, public, novelty and physical claims remain open."
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["orders"], fixed["maximum_rank"], fixed["maximum_row_divided_difference_order"], fixed["maximum_column_divided_difference_order"], fixed["active_peano_derivative_order"], fixed["maximum_kernel_derivative_order"], fixed["polynomial_identity_checks"], fixed["exact_determinant_checks"]) != ([11, 12], 6, 5, 5, 2, 12, 78, 6):
        raise AssertionError("K377 fixed control changed")
    summaries = payload["order_factor_boundaries"]
    if [row["order"] for row in summaries] != [11, 12] or any(row["maximum_rank"] != 6 or not row["rank_six_patterns"] for row in summaries):
        raise AssertionError("K377 rank-six boundary changed")
    gap = payload["gap_free_tensor_divided_difference"]
    if gap["explicit_gap_denominators_after_extension"] or not gap["repeated_nodes_allowed_by_continuity"] or not all(row["exact_equality"] for row in gap["polynomial_controls"]):
        raise AssertionError("K377 gap-free calculus changed")
    dets = payload["determinant_calculus"]
    if not dets["complete_determinant_assembled_before_absolute_enclosure"] or dets["entrywise_cofactor_absolutization_permitted"] or not all(row["exact_replay"] and row["exact_normalization"] for row in dets["exact_controls"]):
        raise AssertionError("K377 determinant calculus weakened")
    decision = payload["decision"]
    if not decision["rank_six_gap_free_confluent_determinant_calculus_emitted"] or decision["zero_safe_global_primitive_bank_through_order_twelve_emitted"] or decision["numerical_orders_eleven_twelve_integrals_emitted"]:
        raise AssertionError("K377 decision boundary changed")
    if not all(payload["release_test"].values()):
        raise AssertionError("K377 release test failed")


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
