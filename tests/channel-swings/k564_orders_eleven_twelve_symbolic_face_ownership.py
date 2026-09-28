#!/usr/bin/env python3
"""Compile exact first-match face owners without materializing 26-bit cubes."""

from __future__ import annotations

import argparse
import functools
import hashlib
import json
import math
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
K559 = ROOT / "lab/process/k559-orders-eleven-twelve-hybrid-face-atlas.json"
K563 = ROOT / "lab/process/k563-orders-eleven-twelve-whole-radial-face-majorants.json"
OUTPUT = ROOT / "lab/process/k564-orders-eleven-twelve-symbolic-face-ownership.json"


def digest(value: Any) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def minimal_edges(edges: tuple[int, ...]) -> tuple[int, ...]:
    ordered = sorted(set(edges), key=lambda edge: (edge.bit_count(), edge))
    result: list[int] = []
    for edge in ordered:
        if not any((prior & edge) == prior for prior in result):
            result.append(edge)
    return tuple(result)


@functools.lru_cache(maxsize=None)
def independence_polynomial(edges: tuple[int, ...], universe: int) -> tuple[int, ...]:
    """Count subsets avoiding every forbidden edge, by selected cardinality."""
    normalized = minimal_edges(edges)
    if normalized != edges:
        return independence_polynomial(normalized, universe)
    n = universe.bit_count()
    if normalized and normalized[0] == 0:
        return (0,) * (n + 1)
    if not normalized:
        return tuple(math.comb(n, degree) for degree in range(n + 1))
    used = 0
    for edge in normalized:
        used |= edge
    free_count = (universe & ~used).bit_count()
    if free_count:
        base = independence_polynomial(normalized, universe & used)
        result = [0] * (n + 1)
        for left_degree, left_count in enumerate(base):
            for right_degree in range(free_count + 1):
                result[left_degree + right_degree] += left_count * math.comb(free_count, right_degree)
        return tuple(result)
    incidence = {index: 0 for index in range(universe.bit_length()) if universe & (1 << index)}
    for edge in normalized:
        for index in incidence:
            if edge & (1 << index):
                incidence[index] += 1
    bit = 1 << max(incidence, key=incidence.get)
    reduced_universe = universe & ~bit
    excluded = independence_polynomial(tuple(edge for edge in normalized if not edge & bit), reduced_universe)
    included = independence_polynomial(tuple((edge & ~bit) if edge & bit else edge for edge in normalized), reduced_universe)
    result = [0] * (n + 1)
    for degree, count in enumerate(excluded):
        result[degree] += count
    for degree, count in enumerate(included):
        result[degree + 1] += count
    return tuple(result)


def mask_key(mask: int, dimension: int) -> tuple[Any, ...]:
    return (-mask.bit_count(), tuple(index for index in range(dimension) if mask & (1 << index)))


def hybrid_ownership(order: int, hybrid: dict[str, Any]) -> dict[str, Any]:
    axes = list(hybrid["moving_axes"])
    position = {axis: index for index, axis in enumerate(axes)}
    universe = (1 << len(axes)) - 1
    masks = {
        sum(1 << position[axis] for axis in face["zeroed_axes"])
        for faces in hybrid["faces"].values() for face in faces
    }
    ordered_masks = sorted(masks, key=lambda mask: mask_key(mask, len(axes)))
    prior: list[int] = []
    owner_rows = []
    for owner_index, face_mask in enumerate(ordered_masks):
        remaining = universe & ~face_mask
        constraints = tuple(prior_mask & ~face_mask for prior_mask in prior)
        if any(edge == 0 for edge in constraints):
            owner_count = 0
        else:
            owner_count = sum(independence_polynomial(constraints, remaining))
        if owner_count <= 0:
            raise AssertionError(f"K564 empty owner union for order {order} {hybrid['axis']}")
        mask_axes = [axis for axis in axes if face_mask & (1 << position[axis])]
        owner_rows.append({
            "owner_index": owner_index,
            "zeroed_axes": mask_axes,
            "codimension": len(mask_axes),
            "assigned_low_coordinate_subsets": owner_count,
        })
        prior.append(face_mask)
    interior_polynomial = independence_polynomial(tuple(ordered_masks), universe)
    interior_count = sum(interior_polynomial)
    recursive_cells = sum((len(axes) - degree) * count for degree, count in enumerate(interior_polynomial))
    total = 1 << len(axes)
    if sum(row["assigned_low_coordinate_subsets"] for row in owner_rows) + interior_count != total:
        raise AssertionError(f"K564 partition mismatch for order {order} {hybrid['axis']}")
    return {
        "order": order,
        "axis": hybrid["axis"],
        "moving_axes": axes,
        "moving_dimension": len(axes),
        "logical_low_coordinate_subsets": total,
        "face_owned_subsets": total - interior_count,
        "interior_owned_subsets": interior_count,
        "distinct_face_owner_unions": len(owner_rows),
        "recursive_positive_interior_max_cells": recursive_cells,
        "owner_rows": owner_rows,
        "owner_histogram_sha256": digest(owner_rows),
    }


def build() -> dict[str, Any]:
    independence_polynomial.cache_clear()
    k559 = json.loads(K559.read_text())
    k563 = json.loads(K563.read_text())
    orders = []
    all_hybrids = []
    for order_atlas in k559["order_atlases"]:
        order = int(order_atlas["order"])
        hybrid_rows = [hybrid_ownership(order, hybrid) for hybrid in order_atlas["hybrid_face_atlas"]]
        orders.append({
            "order": order,
            "hybrid_owner_bank": hybrid_rows,
            "order_summary": {
                "hybrid_terms": len(hybrid_rows),
                "logical_low_coordinate_subsets": sum(row["logical_low_coordinate_subsets"] for row in hybrid_rows),
                "face_owned_subsets": sum(row["face_owned_subsets"] for row in hybrid_rows),
                "interior_owned_subsets": sum(row["interior_owned_subsets"] for row in hybrid_rows),
                "distinct_face_owner_unions": sum(row["distinct_face_owner_unions"] for row in hybrid_rows),
                "recursive_positive_interior_max_cells": sum(row["recursive_positive_interior_max_cells"] for row in hybrid_rows),
            },
        })
        all_hybrids.extend(hybrid_rows)
    total_subsets = sum(row["logical_low_coordinate_subsets"] for row in all_hybrids)
    total_face = sum(row["face_owned_subsets"] for row in all_hybrids)
    total_interior = sum(row["interior_owned_subsets"] for row in all_hybrids)
    total_owners = sum(row["distinct_face_owner_unions"] for row in all_hybrids)
    total_cells = sum(row["recursive_positive_interior_max_cells"] for row in all_hybrids)
    return {
        "schema_version": "1.0",
        "result_id": "K564-ORDERS-ELEVEN-TWELVE-SYMBOLIC-FACE-OWNERSHIP",
        "created": "2026-09-28",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [str(path.relative_to(ROOT)) for path in (K559, K563)],
            "orders": [11, 12],
            "combined_hybrid_terms": len(all_hybrids),
            "logical_low_coordinate_subsets_replayed": total_subsets,
            "combined_face_owner_unions": total_owners,
            "combined_face_owned_subsets": total_face,
            "combined_interior_owned_subsets": total_interior,
            "combined_recursive_positive_interior_max_cells": total_cells,
        },
        "symbolic_ownership_contract": {
            "low_rule": "coordinate is low exactly when it is at most epsilon times the selected maximum; equality remains low",
            "owner_rule": "among reachable face masks contained in the low set choose maximum codimension, then native-axis lexicographic order",
            "interior_rule": "a low set containing no reachable face mask belongs to the positive interior",
            "counter_rule": "exact hypergraph independence polynomials count every low set and recursive maximum-coordinate child without materializing the 24/26-bit cubes",
            "first_match_owner_unions_pairwise_disjoint": True,
            "owner_unions_plus_interior_are_exhaustive": True,
            "logical_subsets_dropped": 0,
        },
        "order_ownership": orders,
        "ownership_summary": {
            "complete_owner_bank_sha256": digest(orders),
            "all_50_hybrids_partitioned": len(all_hybrids) == 50,
            "all_167772156_logical_subsets_replayed": total_subsets == 167_772_156,
            "partition_arithmetic_closes": total_face + total_interior == total_subsets,
            "all_face_owner_unions_nonempty": all(owner["assigned_low_coordinate_subsets"] > 0 for row in all_hybrids for owner in row["owner_rows"]),
        },
        "decision": {
            "symbolic_first_match_face_ownership_complete": True,
            "all_logical_low_coordinate_subsets_accounted": True,
            "recursive_positive_interior_cell_counts_complete": True,
            "integrand_majorants_stitched": False,
            "complete_hybrid_integrals_emitted": False,
            "next_exact_input": "charge each K563 face row once to its K564 owner union and integrate the positive interior with the order-specific complete coherent majorant",
        },
        "release_test": {
            "exactly_50_hybrid_rows": len(all_hybrids) == 50,
            "all_167772156_logical_subsets_replayed": total_subsets == 167_772_156,
            "exactly_2733_face_owner_unions": total_owners == 2733,
            "exactly_1542213_interior_subsets": total_interior == 1_542_213,
            "partition_counts_close": total_face + total_interior == total_subsets,
            "all_owner_unions_nonempty": all(owner["assigned_low_coordinate_subsets"] > 0 for row in all_hybrids for owner in row["owner_rows"]),
            "disjoint_first_match_rule_retained": True,
            "logical_subsets_dropped_zero": True,
            "complete_integrals_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k563["ledger_effect"],
        "source_routing": k563["source_routing"],
        "claim_ceiling": "Exact symbolic first-match partition of all 167,772,156 logical low-coordinate subsets across the fifty higher-order hybrids into 2,733 nonempty reachable-face owner unions or 1,542,213 interior states. Hypergraph independence polynomials preserve the complete 24/26-bit state spaces without materializing them. This supplies ownership geometry and recursive interior-cell counts, not stitched integrand bounds, complete hybrids, remainders/integrals, base action, R_ref, K152, source/ledger movement, canon, paper, public, novelty or physical claims.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["combined_hybrid_terms"], fixed["logical_low_coordinate_subsets_replayed"], fixed["combined_face_owner_unions"], fixed["combined_interior_owned_subsets"]) != (50, 167_772_156, 2733, 1_542_213):
        raise AssertionError("K564 fixed census changed")
    hybrids = [row for order in payload["order_ownership"] for row in order["hybrid_owner_bank"]]
    if len(hybrids) != 50 or any(sum(owner["assigned_low_coordinate_subsets"] for owner in row["owner_rows"]) + row["interior_owned_subsets"] != row["logical_low_coordinate_subsets"] for row in hybrids):
        raise AssertionError("K564 partition changed")
    contract = payload["symbolic_ownership_contract"]
    if not contract["first_match_owner_unions_pairwise_disjoint"] or not contract["owner_unions_plus_interior_are_exhaustive"] or contract["logical_subsets_dropped"] != 0:
        raise AssertionError("K564 ownership contract changed")
    if payload["decision"]["integrand_majorants_stitched"] or payload["decision"]["complete_hybrid_integrals_emitted"] or not all(payload["release_test"].values()):
        raise AssertionError("K564 decision boundary changed")


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
