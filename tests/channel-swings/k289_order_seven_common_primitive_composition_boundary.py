#!/usr/bin/env python3
"""K289 common-primitive dependency boundary for native K287 composition."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K280_PATH = Path(__file__).with_name("k280_order_seven_bessel_vandermonde_face_atlas.py")
K288_MANIFEST = ROOT / "lab/process/k288-order-seven-native-occurrence-measure.json"
OUTPUT = ROOT / "lab/process/k289-order-seven-common-primitive-composition-boundary.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


K280 = load_module("k280_for_k289", K280_PATH)


def even_position_dependency(position: int, prefix: str) -> str:
    if position not in (2, 4, 6, 8):
        raise ValueError(position)
    pair = position // 2 - 1
    return f"{prefix}{pair}"


def certificate() -> dict[str, Any]:
    k288 = json.loads(K288_MANIFEST.read_text())
    occurrences = k288["coherent_gram_measure"]["size_four_occurrences"]
    dependency_rows = []
    companion_pattern_histogram: Counter[str] = Counter()
    for row in occurrences:
        companion = row["companion_factors"]
        if len(companion) != 1 or companion[0]["size"] != 3:
            raise AssertionError("every K288 size-four record must retain one size-three companion")
        factor = companion[0]
        left_positions = tuple(int(value) for value in factor["left_positions"])
        right_positions = tuple(int(value) for value in factor["right_positions"])
        left_splits = sorted({even_position_dependency(value, "u") for value in left_positions})
        right_splits = sorted({even_position_dependency(value, "z") for value in right_positions})
        old_left = even_position_dependency(int(row["left_old_position"]), "u")
        old_right = even_position_dependency(int(row["right_old_position"]), "z")
        pattern = f"L{','.join(map(str, left_positions))}|R{','.join(map(str, right_positions))}"
        companion_pattern_histogram[pattern] += 1
        dependency_rows.append(
            {
                "entry_index": row["entry_index"],
                "group_id": row["group_id"],
                "left": row["left"],
                "right": row["right"],
                "signed_occurrence_weight": row["signed_occurrence_weight"],
                "size_four_positions": {
                    "left": row["size_four_left_positions"],
                    "right": row["size_four_right_positions"],
                },
                "size_four_regularizer_dependencies": [
                    "x",
                    "r0",
                    "r1",
                    "r2",
                    "c0",
                    "c1",
                    "c2",
                ],
                "size_four_independent_of": [
                    "y",
                    "u0",
                    "u1",
                    "u2",
                    "u3",
                    "z0",
                    "z1",
                    "z2",
                    "z3",
                ],
                "companion_size_three_pattern": pattern,
                "companion_internal_split_dependencies": left_splits + right_splits,
                "old_position_internal_split_dependencies": [old_left, old_right],
            }
        )
    all_companion_split_dependent = all(
        row["companion_internal_split_dependencies"] for row in dependency_rows
    )
    all_old_split_dependent = all(
        len(row["old_position_internal_split_dependencies"]) == 2
        for row in dependency_rows
    )
    old_position_pairs = Counter(
        (
            int(row["left_old_position"]),
            int(row["right_old_position"]),
        )
        for row in occurrences
    )
    return {
        "schema_version": "1.0",
        "result_id": "K289-ORDER-SEVEN-COMMON-PRIMITIVE-COMPOSITION-BOUNDARY",
        "created": "2026-09-21",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "source_manifest": "lab/process/k288-order-seven-native-occurrence-measure.json",
            "size_four_occurrences": len(dependency_rows),
            "native_variables": [
                "x",
                "y",
                "r0",
                "r1",
                "r2",
                "c0",
                "c1",
                "c2",
                "u0",
                "u1",
                "u2",
                "u3",
                "z0",
                "z1",
                "z2",
                "z3",
            ],
            "k284_controlled_variables": ["x", "r0", "r1", "r2", "c0", "c1", "c2"],
            "uncontrolled_internal_variables": [
                "y",
                "u0",
                "u1",
                "u2",
                "u3",
                "z0",
                "z1",
                "z2",
                "z3",
            ],
        },
        "exact_dependency_identity": {
            "odd_cumulative_nodes": {
                "T1": "x*(y+r0+r1+r2)",
                "T3": "x*(y+r1+r2)",
                "T5": "x*(y+r2)",
                "T7": "x*y",
                "U1": "x*((1-y)+c0+c1+c2)",
                "U3": "x*((1-y)+c1+c2)",
                "U5": "x*((1-y)+c2)",
                "U7": "x*(1-y)",
            },
            "size_four_cross_sums": "Every T_(odd)+U_(odd) cancels y and is x times 1 plus a row-gap tail plus a column-gap tail; K284's size-four regularizer therefore depends on x,r,c and not y,u,z.",
            "even_cumulative_nodes": "T_(2k)=x*(sum later pair ratios + current pair ratio*(1-u_(k-1))) and similarly U_(2k) with z; every companion size-three determinant therefore retains internal split variables.",
            "old_position_nodes": "All K288 old positions are 2,4,6, so both old-position K1 factors retain one u or z variable in every occurrence.",
        },
        "dependency_census": {
            "all_size_four_factors_pair_sum_only": all(
                row["size_four_left_positions"] == [1, 3, 5, 7]
                and row["size_four_right_positions"] == [1, 3, 5, 7]
                for row in occurrences
            ),
            "all_companion_size_three_factors_split_dependent": all_companion_split_dependent,
            "all_old_position_kernel_pairs_split_dependent": all_old_split_dependent,
            "unique_companion_patterns": len(companion_pattern_histogram),
            "companion_pattern_histogram": dict(sorted(companion_pattern_histogram.items())),
            "old_position_pair_histogram": {
                f"{left},{right}": count
                for (left, right), count in sorted(old_position_pairs.items())
            },
            "occurrences": dependency_rows,
        },
        "composition_decision": {
            "k287_can_be_used_as_a_uniform_bound_on_the_size_four_factor": True,
            "k287_is_a_native_weighted_occurrence_remainder": False,
            "signed_occurrence_weights_can_be_collapsed_before_integration": False,
            "reason": "The six signed records per group have distinct old-position pairs and companion size-three patterns. K287 bounds only their common size-four factor; it does not bound the shared-primitive rest factor or its derivatives.",
            "minimum_next_common_chart": "(x,y,r0,r1,r2,c0,c1,c2,u0,u1,u2,u3,z0,z1,z2,z3) with the complete six-entry coherent group sum retained before absolute enclosure",
            "first_gate": "On the K284 x/r/c tube, derive outward value and mixed-derivative bounds for each complete rest factor: both old-position K1 kernels, the companion size-three determinant, the exact Cauchy-Vandermonde skeleton and the native measure density. Compose those with K286 at the coherent-group level; only then bound radial and arbitrary-gap exterior pieces.",
            "exterior_partition": {
                "radial": "x outside 31/256<=x<=1/8",
                "projective_gap": "positive r,c outside the K284 ordered tube",
                "internal": "y,u,z are native integration variables inside every radial/projective cell, not an exterior tail",
            },
        },
        "release_test": {
            "all_24_occurrences_dependency_audited": len(dependency_rows) == 24,
            "all_companion_size_three_factors_split_dependent": all_companion_split_dependent,
            "all_old_position_kernel_pairs_split_dependent": all_old_split_dependent,
            "native_weighted_jacobi_remainder_serialized": False,
            "complete_arbitrary_gap_ratio_domain_covered": False,
            "complete_base_action_column_evaluated": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k288["ledger_effect"],
        "claim_ceiling": "Exact common-primitive dependency theorem for the 24 order-seven size-four occurrences. K287 controls the common size-four regularizer on its tube, but every native occurrence retains a split-dependent size-three companion and two split-dependent old-position kernels. No native weighted remainder, arbitrary-gap exterior bound, action-column value, complete residual, native K152 interval, physical state, source/ledger move, canon, paper or public claim.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = certificate()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
