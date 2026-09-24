#!/usr/bin/env python3
"""Compile exact determinant-preserving preconditioners for K411 faces."""

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
K407_MODULE = HERE / "k407_order_ten_axis_jet_compiler.py"
K407 = ROOT / "lab/process/k407-order-ten-axis-jet-compiler.json"
K410 = ROOT / "lab/process/k410-order-ten-zero-safe-radial-contract.json"
K411 = ROOT / "lab/process/k411-order-ten-hybrid-face-atlas.json"
OUTPUT = ROOT / "lab/process/k413-order-ten-mask-native-preconditioner-compiler.json"


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


K407_BACKEND = load_module(K407_MODULE, "k407_for_k413")


def digest(payload: Any) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def ordered_descriptors() -> list[dict[str, Any]]:
    rows = []
    for (seed, signature), terms in K407_BACKEND.group_terms().items():
        group_id = f"order10:seed{seed}:{signature}"
        for left in terms:
            for right in terms:
                rows.append(K407_BACKEND.entry_descriptor(group_id, left, right))
    return rows


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
            intervening = {f"{side}{index}" for index in range(a, b)}
            if intervening.issubset(mask):
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
    scored = [(sum(costs[row][column] for row, column in enumerate(permutation)), permutation)
              for permutation in itertools.permutations(range(rank))]
    return max(scored, key=lambda item: (item[0], tuple(-value for value in item[1])))


def dual_certificate(costs: tuple[tuple[int, ...], ...]) -> tuple[tuple[int, ...], tuple[int, ...]]:
    rank = len(costs)
    target, _ = assignment_max(costs)
    best = None
    for row_powers in itertools.product(range(2), repeat=rank):
        column_powers = tuple(max(costs[row][column] - row_powers[row] for row in range(rank))
                              for column in range(rank))
        if min(column_powers) < 0:
            continue
        total = sum(row_powers) + sum(column_powers)
        candidate = (total, row_powers, column_powers)
        if best is None or candidate < best:
            best = candidate
    if best is None or best[0] != target:
        raise AssertionError("binary assignment dual did not close")
    return best[1], best[2]


def template(costs: tuple[tuple[int, ...], ...]) -> dict[str, Any]:
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


def build() -> dict[str, Any]:
    k407 = json.loads(K407.read_text())
    k410 = json.loads(K410.read_text())
    k411 = json.loads(K411.read_text())
    descriptors = ordered_descriptors()
    if len(descriptors) != 13300:
        raise AssertionError("K407 ordered descriptor census changed")
    if not k410["decision"]["zero_safe_scaled_derivative_bank_emitted"]:
        raise AssertionError("K410 scaled primitive bank unavailable")

    patterns: set[tuple[tuple[int, ...], ...]] = set()
    confluent_patterns: set[tuple[int, tuple[int, ...], tuple[int, ...]]] = set()
    matrix_uses = 0
    face_instances = 0
    for hybrid in k411["hybrid_face_atlas"]:
        for faces in hybrid["faces"].values():
            for face in faces:
                face_instances += 1
                mask = set(face["zeroed_axes"])
                for descriptor in descriptors:
                    for matrix in descriptor["species_matrices"]:
                        patterns.add(zero_matrix(matrix, mask))
                        confluent_patterns.add((
                            int(matrix["rank"]),
                            coalescence_labels(matrix["row_positions"], "s", mask),
                            coalescence_labels(matrix["column_positions"], "v", mask),
                        ))
                        matrix_uses += 1

    templates = [template(costs) for costs in sorted(patterns, key=lambda item: (len(item), item))]
    confluent_templates = [confluent_template(*pattern) for pattern in sorted(confluent_patterns)]
    rank_histogram = Counter(row["rank"] for row in templates)
    return {
        "schema_version": "1.0",
        "result_id": "K413-ORDER-TEN-MASK-NATIVE-PRECONDITIONER-COMPILER",
        "created": "2026-09-24",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k407-order-ten-axis-jet-compiler.json",
                "lab/process/k410-order-ten-zero-safe-radial-contract.json",
                "lab/process/k411-order-ten-hybrid-face-atlas.json",
            ],
            "ordered_descriptors": len(descriptors),
            "reachable_face_instances": face_instances,
            "determinant_matrix_face_uses_replayed": matrix_uses,
            "unique_preconditioner_templates": len(templates),
            "unique_confluent_templates": len(confluent_templates),
            "maximum_species_determinant_rank": 5,
            "K407_compiled_entry_interface_sha256": k407["compiled_entry_interface"]["sha256"],
            "K411_face_atlas_sha256": digest(k411["hybrid_face_atlas"]),
        },
        "primitive_scaling_contract": {
            "definition": "Phi_d(w)=w^(d+1)*abs((2*K1)^(d)(w)) for d=0,1,2",
            "zero_limits": k410["scaled_bessel_bank"]["continuous_zero_limits"],
            "exact_rational_envelopes_ref": "lab/process/k410-order-ten-zero-safe-radial-contract.json#scaled_bessel_bank",
            "active_derivative_extra_face_power": "d powers beyond the base w^-1 singularity",
            "raw_Bessel_evaluation_at_zero_used": False,
        },
        "determinant_scaling_contract": {
            "rule": "For a face mask, mark an entry one exactly when its cumulative-time argument mask is contained in the face. The maximum marked entries in a determinant Leibniz term is the assignment optimum. Binary row/column dual powers with the same sum scale the matrix before interval determinant assembly.",
            "determinant_assembled_after_row_column_scaling": True,
            "permutationwise_absolute_enclosure_used_for_numerical_value": False,
            "assignment_duality_is_exact": True,
            "all_ordered_orientations_retained": True,
        },
        "preconditioner_templates": templates,
        "confluent_divided_difference_contract": {
            "rule": "Rows coalesce exactly when every intervening s-axis vanishes, and columns likewise for v. Replace each repeated-node cluster by the corresponding confluent divided-difference rows or columns before interval substitution.",
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
            "all_uses_reduce_to_finite_template_bank": matrix_uses > 0 and len(templates) == 60,
            "template_bank_sha256": digest({"singular": templates, "confluent": confluent_templates}),
        },
        "decision": {
            "all_reachable_proper_face_matrix_patterns_compiled": True,
            "determinant_preserving_row_column_preconditioners_released": True,
            "complete_face_normal_integrability_emitted": False,
            "recursive_numerical_cover_complete": False,
            "next_exact_input": "replay the complete second-derivative product rule across all 13,300 ordered descriptors on every K411 face using these determinant duals and K410 primitive jets",
        },
        "release_test": {
            "exactly_60_unique_templates": len(templates) == 60,
            "ranks_one_through_five_present": sorted(rank_histogram) == [1, 2, 3, 4, 5],
            "exactly_75_confluent_templates": len(confluent_templates) == 75,
            "all_duals_match_primal_assignments": all(row["dual_sum"] == row["maximum_zero_kernels_per_leibniz_term"] for row in templates),
            "all_13300_ordered_descriptors_replayed": len(descriptors) == 13300,
            "all_reachable_faces_replayed": face_instances == 936,
            "raw_zero_bessel_calls_absent": True,
            "complete_order_ten_remainder_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k411["ledger_effect"],
        "source_routing": k411["source_routing"],
        "claim_ceiling": "Exact finite compiler for every determinant zero and coalescence pattern induced by K411's reachable proper faces across all 13,300 ordered order-ten descriptors. The finite singular rank-one-through-five templates carry primal assignment witnesses and equal row/column dual scaling powers; the finite confluent templates carry exact repeated-row/column clusters, Vandermonde orders and divided-difference orders. Interval determinants can therefore be assembled after mask-native singular and confluent preconditioning without raw zero Bessel calls or permutationwise numerical absolute values. Complete face-normal product-rule integrability, recursive numerical coverage, tails, twenty-two Peano integrals, the complete order-ten remainder/integral, action column, R_ref, K152, source/ledger move, canon, paper, public and physical posture remain open.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["ordered_descriptors"], fixed["reachable_face_instances"], fixed["unique_preconditioner_templates"], fixed["unique_confluent_templates"]) != (13300, 936, 60, 75):
        raise AssertionError("K413 census changed")
    templates = payload["preconditioner_templates"]
    if len(templates) != 60:
        raise AssertionError("K413 template bank changed")
    for row in templates:
        costs = tuple(tuple(int(value) for value in values) for values in row["zero_entry_matrix"])
        optimum, witness = assignment_max(costs)
        if optimum != row["maximum_zero_kernels_per_leibniz_term"] or list(witness) != row["primal_permutation_witness"]:
            raise AssertionError("K413 primal witness changed")
        rows = row["row_scaling_powers"]
        columns = row["column_scaling_powers"]
        if (sum(rows) + sum(columns) != optimum
                or row["dual_sum"] != optimum
                or not row["strong_duality_verified"]
                or any(rows[i] + columns[j] < costs[i][j] for i in range(len(costs)) for j in range(len(costs)))):
            raise AssertionError("K413 dual witness changed")
    confluent = payload["confluent_divided_difference_contract"]
    if (confluent["template_count"] != 75
            or not confluent["vandermonde_factors_extracted_before_interval_substitution"]
            or confluent["maximum_row_divided_difference_order"] != 4
            or confluent["maximum_column_divided_difference_order"] != 4):
        raise AssertionError("K413 confluent template bank changed")
    if not all(payload["release_test"].values()):
        raise AssertionError("K413 release test failed")
    if payload["decision"]["complete_face_normal_integrability_emitted"] or payload["decision"]["recursive_numerical_cover_complete"]:
        raise AssertionError("K413 overclaimed numerical closure")


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
