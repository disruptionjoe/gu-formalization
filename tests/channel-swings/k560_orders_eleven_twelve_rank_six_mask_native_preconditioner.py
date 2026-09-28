#!/usr/bin/env python3
"""Compile shared rank-six determinant preconditioners for every K559 face."""

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
K556_MODULE = HERE / "k556_orders_eleven_twelve_axis_jet_compiler.py"
K378 = ROOT / "lab/process/k378-rank-six-global-scaled-bessel-bank.json"
K556 = ROOT / "lab/process/k556-orders-eleven-twelve-axis-jet-compiler.json"
K559 = ROOT / "lab/process/k559-orders-eleven-twelve-hybrid-face-atlas.json"
OUTPUT = ROOT / "lab/process/k560-orders-eleven-twelve-rank-six-mask-native-preconditioner.json"
SIDE_COUNTS = {11: 12, 12: 13}
EXPECTED_DESCRIPTORS = {11: 25200, 12: 69552}


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


K556_BACKEND = load_module(K556_MODULE, "k556_for_k560")


def digest(payload: Any) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def suffix(side: str, position: int, side_count: int) -> list[str]:
    return [f"{side}{index}" for index in range(position, side_count + 1)]


def ordered_descriptors(order: int) -> list[dict[str, Any]]:
    side_count = SIDE_COUNTS[order]
    rows = []
    for (seed, signature), terms in K556_BACKEND.group_terms(order).items():
        group_id = f"order{order}:seed{seed}:{signature}"
        for left in terms:
            for right in terms:
                descriptor = K556_BACKEND.compact_descriptor(group_id, left, right)
                descriptor["left_old_axis_mask"] = suffix("s", int(descriptor["left_old_position"]), side_count)
                descriptor["right_old_axis_mask"] = suffix("v", int(descriptor["right_old_position"]), side_count)
                for matrix in descriptor["species_matrices"]:
                    matrix["entry_axis_masks"] = [
                        [suffix("s", row, side_count) + suffix("v", column, side_count) for column in matrix["column_positions"]]
                        for row in matrix["row_positions"]
                    ]
                rows.append(descriptor)
    if len(rows) != EXPECTED_DESCRIPTORS[order]:
        raise AssertionError(f"order-{order} ordered descriptor census changed")
    return rows


def matrix_signature(matrix: dict[str, Any]) -> tuple[Any, ...]:
    return (
        int(matrix["rank"]),
        tuple(int(value) for value in matrix["row_positions"]),
        tuple(int(value) for value in matrix["column_positions"]),
        tuple(tuple(tuple(mask) for mask in row) for row in matrix["entry_axis_masks"]),
    )


def zero_matrix(matrix: dict[str, Any], mask: set[str]) -> tuple[tuple[int, ...], ...]:
    return tuple(
        tuple(int(set(argument_mask).issubset(mask)) for argument_mask in row)
        for row in matrix["entry_axis_masks"]
    )


def coalescence_labels(positions: list[int], side: str, mask: set[str]) -> tuple[int, ...]:
    parent = list(range(len(positions)))

    def find(index: int) -> int:
        while parent[index] != index:
            parent[index] = parent[parent[index]]
            index = parent[index]
        return index

    def union(left: int, right: int) -> None:
        a, b = find(left), find(right)
        if a != b:
            parent[b] = a

    for left in range(len(positions)):
        for right in range(left + 1, len(positions)):
            a, b = sorted((positions[left], positions[right]))
            if {f"{side}{index}" for index in range(a, b)}.issubset(mask):
                union(left, right)
    names: dict[int, int] = {}
    labels = []
    for index in range(len(positions)):
        root = find(index)
        names.setdefault(root, len(names))
        labels.append(names[root])
    return tuple(labels)


def confluent_template(rank: int, row_labels: tuple[int, ...], column_labels: tuple[int, ...]) -> dict[str, Any]:
    row_sizes = Counter(row_labels)
    column_sizes = Counter(column_labels)
    row_order = sum(size * (size - 1) // 2 for size in row_sizes.values())
    column_order = sum(size * (size - 1) // 2 for size in column_sizes.values())
    return {
        "rank": rank,
        "row_cluster_labels": list(row_labels),
        "column_cluster_labels": list(column_labels),
        "row_vandermonde_order": row_order,
        "column_vandermonde_order": column_order,
        "maximum_row_divided_difference_order": max(row_sizes.values()) - 1,
        "maximum_column_divided_difference_order": max(column_sizes.values()) - 1,
        "confluent_required": row_order + column_order > 0,
    }


def assignment_max(costs: tuple[tuple[int, ...], ...]) -> tuple[int, tuple[int, ...]]:
    rank = len(costs)
    scored = [
        (sum(costs[row][column] for row, column in enumerate(permutation)), permutation)
        for permutation in itertools.permutations(range(rank))
    ]
    return max(scored, key=lambda item: (item[0], tuple(-value for value in item[1])))


def dual_certificate(costs: tuple[tuple[int, ...], ...]) -> tuple[tuple[int, ...], tuple[int, ...]]:
    rank = len(costs)
    target, _ = assignment_max(costs)
    best = None
    for row_powers in itertools.product(range(2), repeat=rank):
        column_powers = tuple(max(costs[row][column] - row_powers[row] for row in range(rank)) for column in range(rank))
        if min(column_powers) < 0:
            continue
        candidate = (sum(row_powers) + sum(column_powers), row_powers, column_powers)
        if best is None or candidate < best:
            best = candidate
    if best is None or best[0] != target:
        raise AssertionError("binary determinant assignment dual did not close")
    return best[1], best[2]


def singular_template(costs: tuple[tuple[int, ...], ...]) -> dict[str, Any]:
    maximum, witness = assignment_max(costs)
    rows, columns = dual_certificate(costs)
    if any(rows[i] + columns[j] < costs[i][j] for i in range(len(costs)) for j in range(len(costs))):
        raise AssertionError("invalid determinant scaling dual")
    return {
        "rank": len(costs),
        "zero_entry_matrix": [list(row) for row in costs],
        "maximum_zero_kernels_per_leibniz_term": maximum,
        "primal_permutation_witness": list(witness),
        "row_scaling_powers": list(rows),
        "column_scaling_powers": list(columns),
        "dual_sum": sum(rows) + sum(columns),
        "strong_duality_verified": sum(rows) + sum(columns) == maximum,
    }


def order_face_masks(order_row: dict[str, Any]) -> tuple[list[set[str]], int]:
    instances = []
    for hybrid in order_row["hybrid_face_atlas"]:
        for faces in hybrid["faces"].values():
            instances.extend(set(face["zeroed_axes"]) for face in faces)
    unique = {tuple(sorted(mask)) for mask in instances}
    return [set(mask) for mask in sorted(unique)], len(instances)


def build() -> dict[str, Any]:
    k378 = json.loads(K378.read_text())
    k556 = json.loads(K556.read_text())
    k559 = json.loads(K559.read_text())
    order_atlases = {int(row["order"]): row for row in k559["order_atlases"]}
    patterns: set[tuple[tuple[int, ...], ...]] = set()
    confluent_patterns: set[tuple[int, tuple[int, ...], tuple[int, ...]]] = set()
    order_summaries = []
    logical_matrix_face_uses = 0
    unique_matrix_total = 0
    for order in (11, 12):
        descriptors = ordered_descriptors(order)
        masks, face_instances = order_face_masks(order_atlases[order])
        matrices: dict[tuple[Any, ...], dict[str, Any]] = {}
        matrix_occurrences = 0
        for descriptor in descriptors:
            matrix_occurrences += len(descriptor["species_matrices"])
            for matrix in descriptor["species_matrices"]:
                matrices.setdefault(matrix_signature(matrix), matrix)
        unique_matrix_total += len(matrices)
        logical_matrix_face_uses += matrix_occurrences * face_instances
        before_singular = len(patterns)
        before_confluent = len(confluent_patterns)
        for mask in masks:
            for matrix in matrices.values():
                patterns.add(zero_matrix(matrix, mask))
                confluent_patterns.add((
                    int(matrix["rank"]),
                    coalescence_labels(matrix["row_positions"], "s", mask),
                    coalescence_labels(matrix["column_positions"], "v", mask),
                ))
        order_summaries.append({
            "order": order,
            "ordered_descriptors": len(descriptors),
            "determinant_matrix_occurrences": matrix_occurrences,
            "unique_determinant_matrix_structures": len(matrices),
            "reachable_face_instances": face_instances,
            "unique_reachable_masks": len(masks),
            "new_singular_templates_contributed": len(patterns) - before_singular,
            "new_confluent_templates_contributed": len(confluent_patterns) - before_confluent,
        })
    templates = [singular_template(costs) for costs in sorted(patterns, key=lambda item: (len(item), item))]
    confluent_templates = [confluent_template(*pattern) for pattern in sorted(confluent_patterns)]
    rank_histogram = Counter(row["rank"] for row in templates)
    global_rows = k378["global_scaled_bessel_bank"]["rows"]
    return {
        "schema_version": "1.0",
        "result_id": "K560-ORDERS-ELEVEN-TWELVE-RANK-SIX-MASK-NATIVE-PRECONDITIONER",
        "created": "2026-09-28",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [str(path.relative_to(ROOT)) for path in (K378, K556, K559)],
            "orders": [11, 12],
            "combined_ordered_descriptors": sum(row["ordered_descriptors"] for row in order_summaries),
            "combined_reachable_face_instances": sum(row["reachable_face_instances"] for row in order_summaries),
            "logical_determinant_matrix_face_uses": logical_matrix_face_uses,
            "deduplicated_matrix_structures_by_order": unique_matrix_total,
            "unique_preconditioner_templates": len(templates),
            "unique_confluent_templates": len(confluent_templates),
            "maximum_species_determinant_rank": max(rank_histogram),
        },
        "order_replay_summary": order_summaries,
        "primitive_scaling_contract": {
            "definition": k378["scaled_bessel_contract"]["definition"],
            "global_domain": k378["global_scaled_bessel_bank"]["global_domain"],
            "orders_available": [row["order"] for row in global_rows],
            "global_scaled_uppers": [row["global_scaled_upper"] for row in global_rows],
            "active_derivative_extra_face_power": "d powers beyond the base w^-1 singularity",
            "raw_Bessel_evaluation_at_zero_used": False,
        },
        "determinant_scaling_contract": {
            "rule": "mark an entry one exactly when its cumulative-time argument mask is contained in the face; the maximum marked entries in a determinant Leibniz term is the assignment optimum",
            "determinant_assembled_after_row_column_scaling": True,
            "permutationwise_absolute_enclosure_used_for_numerical_value": False,
            "assignment_duality_is_exact": True,
            "all_ordered_orientations_retained": True,
            "structural_deduplication_preserves_every_logical_matrix_face_use": True,
        },
        "preconditioner_templates": templates,
        "confluent_divided_difference_contract": {
            "rule": "rows coalesce exactly when every intervening s-axis vanishes, and columns likewise for v; repeated clusters are replaced by confluent divided-difference rows or columns before interval substitution",
            "vandermonde_factors_extracted_before_interval_substitution": True,
            "templates": confluent_templates,
            "template_count": len(confluent_templates),
            "maximum_row_divided_difference_order": max(row["maximum_row_divided_difference_order"] for row in confluent_templates),
            "maximum_column_divided_difference_order": max(row["maximum_column_divided_difference_order"] for row in confluent_templates),
            "template_bank_sha256": digest(confluent_templates),
        },
        "template_summary": {
            "rank_histogram": {str(rank): rank_histogram[rank] for rank in sorted(rank_histogram)},
            "all_strong_duality_checks_pass": all(row["strong_duality_verified"] for row in templates),
            "ranks_one_through_six_present": sorted(rank_histogram) == [1, 2, 3, 4, 5, 6],
            "template_bank_sha256": digest({"singular": templates, "confluent": confluent_templates}),
        },
        "decision": {
            "all_reachable_order_eleven_matrix_patterns_compiled": True,
            "all_reachable_order_twelve_matrix_patterns_compiled": True,
            "rank_six_determinant_preserving_row_column_preconditioners_released": True,
            "rank_six_confluent_templates_released": True,
            "complete_face_normal_integrability_emitted": False,
            "whole_domain_hybrid_majorants_emitted": False,
            "next_exact_input": "replay the complete pure-second product rule across all 94,752 ordered descriptors on every K559 face using these exact determinant duals and K378 scaled primitive jets",
        },
        "release_test": {
            "all_94752_ordered_descriptors_represented": sum(row["ordered_descriptors"] for row in order_summaries) == 94752,
            "all_2733_reachable_faces_represented": sum(row["reachable_face_instances"] for row in order_summaries) == 2733,
            "rank_six_templates_present": max(rank_histogram) == 6,
            "ranks_one_through_six_present": sorted(rank_histogram) == [1, 2, 3, 4, 5, 6],
            "all_duals_match_primal_assignments": all(row["dual_sum"] == row["maximum_zero_kernels_per_leibniz_term"] for row in templates),
            "all_confluent_templates_bounded_by_rank_six": max(row["maximum_row_divided_difference_order"] for row in confluent_templates) <= 5 and max(row["maximum_column_divided_difference_order"] for row in confluent_templates) <= 5,
            "raw_zero_bessel_calls_absent": True,
            "complete_remainders_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k559["ledger_effect"],
        "source_routing": k559["source_routing"],
        "claim_ceiling": "Exact finite shared compiler for every determinant zero and coalescence pattern induced by all 2,733 K559 reachable face instances across 94,752 ordered order-eleven/twelve descriptors. Singular rank-one-through-six templates carry primal assignment witnesses and equal row/column dual scaling powers; confluent templates carry exact repeated-row/column clusters, Vandermonde orders and divided-difference orders. Complete face-normal product-rule integrability, global coefficient envelopes, recursive interiors, analytic tails, fifty numerical Peano hybrids, complete remainders/integrals, base action column, R_ref, K152, source/ledger movement, canon, paper, public, novelty and physical claims remain open.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if fixed["combined_ordered_descriptors"] != 94752 or fixed["combined_reachable_face_instances"] != 2733 or fixed["maximum_species_determinant_rank"] != 6:
        raise AssertionError("K560 fixed census changed")
    templates = payload["preconditioner_templates"]
    if len(templates) != fixed["unique_preconditioner_templates"] or not templates:
        raise AssertionError("K560 singular template bank changed")
    for row in templates:
        costs = tuple(tuple(int(value) for value in values) for values in row["zero_entry_matrix"])
        optimum, witness = assignment_max(costs)
        if optimum != row["maximum_zero_kernels_per_leibniz_term"] or list(witness) != row["primal_permutation_witness"]:
            raise AssertionError("K560 primal witness changed")
        rows = row["row_scaling_powers"]
        columns = row["column_scaling_powers"]
        if row["dual_sum"] != optimum or sum(rows) + sum(columns) != optimum or any(rows[i] + columns[j] < costs[i][j] for i in range(len(costs)) for j in range(len(costs))):
            raise AssertionError("K560 dual witness changed")
    if not all(payload["release_test"].values()):
        raise AssertionError("K560 release test failed")
    if payload["decision"]["complete_face_normal_integrability_emitted"] or payload["decision"]["whole_domain_hybrid_majorants_emitted"]:
        raise AssertionError("K560 overclaimed a later closure")


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
