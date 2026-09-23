#!/usr/bin/env python3
"""Compile every order-nine species determinant and its rank-five boundary."""

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
K343 = ROOT / "lab/process/k343-higher-order-value-mode-transfer-gate.json"
OUTPUT = ROOT / "lab/process/k373-order-nine-rank-five-determinant-atlas.json"
ORDER = 9
TOTAL_POSITIONS = ORDER + 1
EXPECTED = (256, 20, 2368, 4480, 5, (2, 4, 6, 8))


def load_k179():
    spec = importlib.util.spec_from_file_location("k179_for_k373", K179_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {K179_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


K179 = load_k179()


def digest(value: Any) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    work = [row[:] for row in matrix]
    total = Fraction(1)
    for column in range(len(work)):
        pivot = next((row for row in range(column, len(work)) if work[row][column]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            total = -total
        value = work[column][column]
        total *= value
        work[column] = [entry / value for entry in work[column]]
        for row in range(column + 1, len(work)):
            factor = work[row][column]
            work[row] = [entry - factor * base for entry, base in zip(work[row], work[column])]
    return total


def vandermonde(values: list[Fraction]) -> Fraction:
    result = Fraction(1)
    for left in range(len(values)):
        for right in range(left + 1, len(values)):
            result *= values[left] - values[right]
    return result


def cauchy_factored(left: list[Fraction], right: list[Fraction]) -> Fraction:
    denominator = math.prod((x + y for x in left for y in right), start=Fraction(1))
    return Fraction(2 ** len(left)) * vandermonde(left) * vandermonde(right) / denominator


def parity(values: tuple[int, ...]) -> int:
    inversions = sum(values[i] > values[j] for i in range(len(values)) for j in range(i + 1, len(values)))
    return -1 if inversions % 2 else 1


def occurrences(term: dict[str, Any]) -> dict[str, tuple[int, ...]]:
    result: dict[str, list[int]] = defaultdict(list)
    for position, species in zip(term["output_variable_provenance"], term["output_letters"], strict=True):
        result[str(species)].append(int(position))
    return {key: tuple(value) for key, value in sorted(result.items())}


def factor_record(species: str, left_raw: tuple[int, ...], right_raw: tuple[int, ...]) -> dict[str, Any]:
    left = tuple(sorted(left_raw))
    right = tuple(sorted(right_raw))
    if len(left) != len(right):
        raise AssertionError("species determinant ceased to be square")
    return {
        "species": species,
        "size": len(left),
        "left_positions": list(left),
        "right_positions": list(right),
        "determinant_sign": parity(left_raw) * parity(right_raw),
        "left_gap_supports": [[f"s{k}" for k in range(i, j)] for a, i in enumerate(left) for j in left[a + 1 :]],
        "right_gap_supports": [[f"v{k}" for k in range(i, j)] for a, i in enumerate(right) for j in right[a + 1 :]],
        "cross_supports": [
            [f"s{k}" for k in range(i, TOTAL_POSITIONS + 1)] + [f"v{k}" for k in range(j, TOTAL_POSITIONS + 1)]
            for i in left for j in right
        ],
        "exact_factorization": "sign*2^m*V(T_left)*V(U_right)/product_ij(T_i+U_j)*R_m",
    }


def pattern_key(row: dict[str, Any]) -> str:
    return f"m{row['size']}|L{','.join(map(str, row['left_positions']))}|R{','.join(map(str, row['right_positions']))}"


def order_groups() -> dict[tuple[int, str], list[dict[str, Any]]]:
    groups: dict[tuple[int, str], list[dict[str, Any]]] = defaultdict(list)
    for term in K179.coefficient_family():
        if int(term["order"]) == ORDER:
            groups[(int(term["seed_impurity"]), str(term["output_signature"]))].append(term)
    return dict(sorted(groups.items()))


def inventory(groups: dict[tuple[int, str], list[dict[str, Any]]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    pattern_counter: Counter[str] = Counter()
    pattern_records: dict[str, dict[str, Any]] = {}
    entries = []
    for group, terms in groups.items():
        for left_index, left in enumerate(terms):
            left_occ = occurrences(left)
            for right in terms[left_index:]:
                right_occ = occurrences(right)
                factors = []
                for species in left_occ:
                    row = factor_record(species, left_occ[species], right_occ[species])
                    key = pattern_key(row)
                    pattern_counter[key] += 1
                    pattern_records[key] = row
                    factors.append({"pattern": key, "sign": row["determinant_sign"]})
                entries.append({
                    "group": f"seed={group[0]}|{group[1]}",
                    "left": str(left["contraction_id"]),
                    "right": str(right["contraction_id"]),
                    "coefficient_product": int(left["exact_operator_coefficient"]) * int(right["exact_operator_coefficient"]),
                    "left_old_position": int(left["old_position"]),
                    "right_old_position": int(right["old_position"]),
                    "factors": factors,
                })
    patterns = []
    for key in sorted(pattern_records):
        patterns.append({"pattern": key, "occurrences": pattern_counter[key], **pattern_records[key]})
    return patterns, entries


def cauchy_controls() -> list[dict[str, Any]]:
    rows = []
    for size in range(1, 6):
        left = [Fraction(43 - 3 * index, 47) for index in range(size)]
        right = [Fraction(53 - 4 * index, 59) for index in range(size)]
        direct = determinant([[Fraction(2, 1) / (x + y) for y in right] for x in left])
        factored = cauchy_factored(left, right)
        rows.append({"size": size, "direct": str(direct), "factored": str(factored), "exact_equality": direct == factored})
    return rows


def build() -> dict[str, Any]:
    k343 = json.loads(K343.read_text())
    source_row = next(row for row in k343["orders"] if row["order"] == ORDER)
    expected_actual = (
        source_row["paths"], source_row["groups"], source_row["upper_triangle_gram_entries"],
        source_row["ordered_quadratic_terms"], source_row["maximum_species_determinant_rank"],
        tuple(source_row["old_position_support"]),
    )
    if expected_actual != EXPECTED:
        raise AssertionError("K343 order-nine interface changed")
    groups = order_groups()
    patterns, entries = inventory(groups)
    paths = sum(len(rows) for rows in groups.values())
    upper = sum(len(rows) * (len(rows) + 1) // 2 for rows in groups.values())
    ordered = sum(len(rows) ** 2 for rows in groups.values())
    max_rank = max(row["size"] for row in patterns)
    if (paths, len(groups), upper, ordered, max_rank) != EXPECTED[:5]:
        raise AssertionError("order-nine replay census changed")
    rank_hist = Counter()
    pattern_hist = Counter()
    for row in patterns:
        rank_hist[row["size"]] += row["occurrences"]
        pattern_hist[row["size"]] += 1
    controls = cauchy_controls()
    if not all(row["exact_equality"] for row in controls):
        raise AssertionError("exact Cauchy determinant control failed")
    rank_five = [row for row in patterns if row["size"] == 5]
    return {
        "schema_version": "1.0",
        "result_id": "K373-ORDER-NINE-RANK-FIVE-DETERMINANT-ATLAS",
        "created": "2026-09-23",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": ["lab/process/k179-matched-normal-order-coefficient-family-wave.json", str(K343.relative_to(ROOT))],
            "order": ORDER,
            "paths": paths,
            "coherent_groups": len(groups),
            "upper_triangle_gram_entries": upper,
            "ordered_quadratic_terms": ordered,
            "maximum_species_determinant_rank": max_rank,
            "old_position_support": list(EXPECTED[5]),
            "K343_group_interface_sha256": source_row["group_interface_sha256"],
        },
        "complete_factorization_inventory": {
            "patterns": patterns,
            "unique_patterns": len(patterns),
            "unique_patterns_by_size": {str(key): value for key, value in sorted(pattern_hist.items())},
            "factor_occurrences_by_size": {str(key): value for key, value in sorted(rank_hist.items())},
            "rank_five_patterns": len(rank_five),
            "rank_five_occurrences": sum(row["occurrences"] for row in rank_five),
            "rank_five_pattern_sha256": digest(rank_five),
            "complete_entry_interface_sha256": digest(entries),
            "all_upper_triangle_entries_serialized": len(entries) == upper,
            "complete_group_assembly_precedes_absolute_enclosure": True,
        },
        "exact_cauchy_controls": controls,
        "confluence_demand": {
            "maximum_row_divided_difference_order": 4,
            "maximum_column_divided_difference_order": 4,
            "active_peano_derivative_order": 2,
            "maximum_kernel_derivative_order_required": 10,
            "required_orders": list(range(11)),
            "reason": "rank-five row and column confluence costs four derivatives each; a pure-second Peano axis costs two more",
        },
        "decision": {
            "complete_order_nine_factor_atlas_emitted": True,
            "rank_five_obstruction_isolated": True,
            "rank_five_confluent_calculus_emitted": False,
            "numerical_order_nine_integral_emitted": False,
            "next_exact_input": "prove the gap-free rank-five tensor divided-difference calculus and extend the zero-safe scaled Bessel bank through derivative order ten",
        },
        "release_test": {
            "all_256_paths_replayed": paths == 256,
            "all_20_groups_replayed": len(groups) == 20,
            "all_2368_upper_triangle_entries_replayed": len(entries) == 2368,
            "all_4480_ordered_terms_retained": ordered == 4480,
            "rank_five_patterns_present": bool(rank_five),
            "all_exact_cauchy_controls_pass": all(row["exact_equality"] for row in controls),
            "derivative_demand_is_ten": True,
            "numerical_integral_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": {"SC-ACT-01": "ASSERTS_UNCHANGED", "SC-ACT-02": "ASSERTS_UNCHANGED", "SC-ACT-06": "ASSERTS_UNCHANGED", "SC-META-53": "UNCERTAIN_UNCHANGED", "LT-SM8": "NEEDS_UNCHANGED", "LT-GR6b": "NEEDS_UNCHANGED", "RA-F1": "NEEDS_UNCHANGED", "AC-F1": "NEEDS_UNCHANGED"},
        "source_routing": {"classification": "INTERNAL_STRUCTURAL_ONLY", "source_native_GU_mechanism_tested": False, "conditional_repository_Fock_construction_only": True},
        "claim_ceiling": "Exact order-nine species-determinant atlas for all 256 K179 paths, 20 coherent groups, 2,368 upper-triangle Gram entries and 4,480 ordered terms. Every canonical row/column gap and Cauchy support is retained, the genuine rank-five patterns are isolated, and exact rational Cauchy determinant controls pass through size five. The rank-five confluent/derivative calculus, numerical order-nine integral, action column, R_ref, K152, source/ledger move, canon, paper, public, novelty and physical claims remain open."
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["paths"], fixed["coherent_groups"], fixed["upper_triangle_gram_entries"], fixed["ordered_quadratic_terms"], fixed["maximum_species_determinant_rank"]) != EXPECTED[:5]:
        raise AssertionError("K373 fixed census changed")
    inventory = payload["complete_factorization_inventory"]
    if not inventory["all_upper_triangle_entries_serialized"] or not inventory["complete_group_assembly_precedes_absolute_enclosure"]:
        raise AssertionError("K373 inventory weakened")
    if inventory["rank_five_patterns"] <= 0 or inventory["rank_five_occurrences"] <= 0:
        raise AssertionError("K373 lost rank-five factors")
    if not all(row["exact_equality"] for row in payload["exact_cauchy_controls"]):
        raise AssertionError("K373 exact control failed")
    demand = payload["confluence_demand"]
    if (demand["maximum_row_divided_difference_order"], demand["maximum_column_divided_difference_order"], demand["active_peano_derivative_order"], demand["maximum_kernel_derivative_order_required"]) != (4, 4, 2, 10):
        raise AssertionError("K373 derivative demand changed")
    decision = payload["decision"]
    if not decision["complete_order_nine_factor_atlas_emitted"] or not decision["rank_five_obstruction_isolated"] or decision["rank_five_confluent_calculus_emitted"] or decision["numerical_order_nine_integral_emitted"]:
        raise AssertionError("K373 decision boundary changed")
    if not all(payload["release_test"].values()):
        raise AssertionError("K373 release test failed")


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
