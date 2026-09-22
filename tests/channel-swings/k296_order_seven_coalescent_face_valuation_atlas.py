#!/usr/bin/env python3
"""Exact face valuations for the K288 order-seven size-four occurrences."""

from __future__ import annotations

import argparse
import itertools
import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K288 = ROOT / "lab/process/k288-order-seven-native-occurrence-measure.json"
K289 = ROOT / "lab/process/k289-order-seven-common-primitive-composition-boundary.json"
K295 = ROOT / "lab/process/k295-order-seven-exterior-integrability-boundary.json"
OUTPUT = ROOT / "lab/process/k296-order-seven-coalescent-face-valuation-atlas.json"

LEFT = ("r0", "r1", "r2", "y")
RIGHT = ("c0", "c1", "c2", "w")  # w=1-y
GAPS = LEFT[:3] + RIGHT[:3]
ODD = (1, 3, 5, 7)


def labels_between(first: int, second: int, side: tuple[str, ...]) -> frozenset[str]:
    """Pair labels touched by primitive positions first,...,second-1."""
    if first >= second:
        raise ValueError("positions must be increasing")
    return frozenset(side[(primitive - 1) // 2] for primitive in range(first, second))


def vandermonde_valuation(
    positions: tuple[int, ...], scaled: frozenset[str], side: tuple[str, ...]
) -> int:
    """Order when all labels in ``scaled`` are scaled by one epsilon."""
    return sum(
        labels_between(first, second, side) <= scaled
        for first, second in itertools.combinations(positions, 2)
    )


def common_cauchy_valuation(scaled: frozenset[str]) -> int:
    return vandermonde_valuation(ODD, scaled, LEFT) + vandermonde_valuation(
        ODD, scaled, RIGHT
    )


def occurrence_rows() -> list[dict[str, Any]]:
    k288 = json.loads(K288.read_text())
    k289 = json.loads(K289.read_text())
    native = k288["coherent_gram_measure"]["size_four_occurrences"]
    dependencies = k289["dependency_census"]["occurrences"]
    if len(native) != 24 or len(dependencies) != 24:
        raise AssertionError("K288/K289 occurrence census changed")
    dependency_by_index = {int(row["entry_index"]): row for row in dependencies}
    rows = []
    for row in native:
        dependency = dependency_by_index[int(row["entry_index"])]
        factor = row["companion_factors"][0]
        expected = (
            "L" + ",".join(map(str, factor["left_positions"]))
            + "|R" + ",".join(map(str, factor["right_positions"]))
        )
        if dependency["companion_size_three_pattern"] != expected:
            raise AssertionError("K288/K289 companion pattern mismatch")
        rows.append(
            {
                "entry_index": int(row["entry_index"]),
                "group_id": row["group_id"],
                "signed_occurrence_weight": int(row["signed_occurrence_weight"]),
                "left_old_position": int(row["left_old_position"]),
                "right_old_position": int(row["right_old_position"]),
                "left_companion_positions": factor["left_positions"],
                "right_companion_positions": factor["right_positions"],
            }
        )
    return rows


def projective_faces(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    result = []
    for codimension in (1, 2):
        for face in itertools.combinations(GAPS, codimension):
            scaled = frozenset(face)
            common = common_cauchy_valuation(scaled)
            companion = []
            for row in rows:
                value = vandermonde_valuation(
                    tuple(row["left_companion_positions"]), scaled, LEFT
                ) + vandermonde_valuation(
                    tuple(row["right_companion_positions"]), scaled, RIGHT
                )
                companion.append(value)
            result.append(
                {
                    "face": list(face),
                    "codimension": codimension,
                    "native_gap_product_valuation": codimension,
                    "common_size_four_cauchy_valuation": common,
                    "companion_valuation_histogram": {
                        str(key): value for key, value in sorted(Counter(companion).items())
                    },
                    "minimum_native_cauchy_companion_valuation": codimension
                    + common
                    + min(companion),
                }
            )
    return result


def endpoint_joins(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    joins = []
    for face, endpoint, side, key in (
        ("r2", "y", LEFT, "left_companion_positions"),
        ("c2", "w", RIGHT, "right_companion_positions"),
    ):
        scaled = frozenset((face, endpoint))
        values = [
            vandermonde_valuation(tuple(row[key]), scaled, side) for row in rows
        ]
        joins.append(
            {
                "join": [face, endpoint],
                "meaning": "the terminal pair gap and its base endpoint vanish together",
                "native_paired_measure_variables": 2,
                "common_size_four_cauchy_valuation": common_cauchy_valuation(scaled),
                "companion_valuation_histogram": {
                    str(k): v for k, v in sorted(Counter(values).items())
                },
                "occurrences_with_companion_zero": sum(value > 0 for value in values),
                "occurrences_without_companion_zero": sum(value == 0 for value in values),
            }
        )
    return joins


def build() -> dict[str, Any]:
    k295 = json.loads(K295.read_text())
    rows = occurrence_rows()
    faces = projective_faces(rows)
    joins = endpoint_joins(rows)
    one_gap = [row for row in faces if row["codimension"] == 1]
    two_gap = [row for row in faces if row["codimension"] == 2]
    return {
        "schema_version": "1.0",
        "result_id": "K296-ORDER-SEVEN-COALESCENT-FACE-VALUATION-ATLAS",
        "created": "2026-09-22",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k288-order-seven-native-occurrence-measure.json",
                "lab/process/k289-order-seven-common-primitive-composition-boundary.json",
                "lab/process/k295-order-seven-exterior-integrability-boundary.json",
            ],
            "occurrences": len(rows),
            "projective_gap_labels": list(GAPS),
            "left_pair_labels": list(LEFT),
            "right_pair_labels": list(RIGHT),
            "right_endpoint_symbol": "w=1-y",
        },
        "valuation_rule": {
            "primitive_support": "T_i-T_j=sum_{k=i}^{j-1}s_k and U_i-U_j=sum_{k=i}^{j-1}v_k",
            "simultaneous_scaling": "a Vandermonde difference contributes one epsilon iff every pair label in its primitive support is scaled",
            "common_size_four_left_vandermonde": "r0*r1*r2*(r0+r1)*(r1+r2)*(r0+r1+r2)",
            "common_size_four_right_vandermonde": "c0*c1*c2*(c0+c1)*(c1+c2)*(c0+c1+c2)",
            "denominators": "all Cauchy cross sums stay positive on these projective faces away from the separately listed base-endpoint joins",
        },
        "projective_face_atlas": faces,
        "endpoint_joins": joins,
        "occurrence_census": rows,
        "decision": {
            "all_one_gap_faces_have_common_cauchy_zero": all(
                row["common_size_four_cauchy_valuation"] == 1 for row in one_gap
            ),
            "all_one_gap_faces_have_companion_zero": all(
                row["companion_valuation_histogram"] == {"1": 24} for row in one_gap
            ),
            "adjacent_same_side_two_gap_faces_have_cauchy_valuation_three": all(
                next(row for row in two_gap if row["face"] == list(pair))[
                    "common_size_four_cauchy_valuation"
                ]
                == 3
                for pair in (("r0", "r1"), ("r1", "r2"), ("c0", "c1"), ("c1", "c2"))
            ),
            "one_gap_native_plus_cauchy_valuation": 2,
            "companion_zero_is_uniform_on_terminal_endpoint_join": False,
            "next_exact_input": "combine the exact native-plus-Cauchy order two with the endpoint-paired old kernel and classify the omitted-old-position exceptions before any fourth-order global rule",
        },
        "release_test": {
            "k295_true_integrand_divergence_proved": k295["pointwise_majorant_face_audit"]["true_integrand_divergence_proved"],
            "all_24_occurrences_replayed": len(rows) == 24,
            "six_one_gap_faces_serialized": len(one_gap) == 6,
            "fifteen_codimension_two_projective_faces_serialized": len(two_gap) == 15,
            "two_terminal_endpoint_joins_serialized": len(joins) == 2,
            "complete_exterior_integrand_bound_emitted": False,
            "complete_base_action_column_evaluated": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k295["ledger_effect"],
        "claim_ceiling": "Exact one-gap and codimension-two Vandermonde valuation atlas for all 24 K288 size-four occurrences, including the two terminal base-endpoint joins. Every projective one-gap face gains one common Cauchy zero and the native measure adds a second gap power; companion zeros are join- and occurrence-dependent. No fourth-order exterior rule, true-integrand divergence, complete exterior bound, action-column value, residual, native K152 interval, source/ledger move, canon, paper or public claim is established.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    rendered = json.dumps(build(), indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
