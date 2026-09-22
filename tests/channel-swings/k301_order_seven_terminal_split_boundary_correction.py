#!/usr/bin/env python3
"""Correct the K290 pointwise split-boundary premise.

Every order-seven size-three companion contains the even cumulative position
eight on both sides.  Its (8,8) entry therefore has argument

    x * (y*(1-u3) + (1-y)*(1-z3)),

which has no positive lower bound on the native split cube.  K290's use of
``x_min`` as an entrywise lower bound is consequently invalid.  This module
records the exact dependency correction without discarding the valid K288/K289
occurrence census or the K292 disjoint atlas.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K288 = ROOT / "lab/process/k288-order-seven-native-occurrence-measure.json"
K289 = ROOT / "lab/process/k289-order-seven-common-primitive-composition-boundary.json"
K290 = ROOT / "lab/process/k290-order-seven-native-rest-derivative-bank.json"
K291 = ROOT / "lab/process/k291-order-seven-native-interior-remainder.json"
K293 = ROOT / "lab/process/k293-order-seven-complete-native-tube-remainder.json"
K300 = ROOT / "lab/process/k300-order-seven-angular-method-selection.json"
OUTPUT = ROOT / "lab/process/k301-order-seven-terminal-split-boundary-correction.json"


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    work = [row[:] for row in matrix]
    total = Fraction(1)
    for column in range(len(work)):
        pivot = next(
            (row for row in range(column, len(work)) if work[row][column]), None
        )
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
            work[row] = [
                entry - factor * base
                for entry, base in zip(work[row], work[column])
            ]
    return total


def minor(matrix: list[list[Fraction]], row: int, column: int) -> Fraction:
    return determinant(
        [
            [entry for j, entry in enumerate(source) if j != column]
            for i, source in enumerate(matrix)
            if i != row
        ]
    )


def rational_coherent_control() -> dict[str, Any]:
    """Exact nonzero terminal coefficient in a symmetric Cauchy control."""
    times = [Fraction(4), Fraction(2), Fraction(1)]
    matrix = [[Fraction(2, left + right) for right in times] for left in times]
    old = [Fraction(2, value) for value in times]
    signs = [1, -1, 1]
    coefficient = sum(
        Fraction(signs[i] * signs[j])
        * old[i]
        * old[j]
        * minor(matrix, i, j)
        for i in range(3)
        for j in range(3)
    )
    return {
        "times": [str(value) for value in times],
        "matrix_determinant": str(determinant(matrix)),
        "terminal_entry_coefficient": str(coefficient),
        "strictly_positive": coefficient > 0,
        "interpretation": "the coherent old-position signs do not identically cancel the terminal companion entry",
    }


def build() -> dict[str, Any]:
    k288 = json.loads(K288.read_text())
    k289 = json.loads(K289.read_text())
    k290 = json.loads(K290.read_text())
    k291 = json.loads(K291.read_text())
    k293 = json.loads(K293.read_text())
    k300 = json.loads(K300.read_text())
    occurrences = k288["coherent_gram_measure"]["size_four_occurrences"]
    patterns: dict[str, int] = {}
    rows = []
    for occurrence in occurrences:
        companion = occurrence["companion_factors"][0]
        left = tuple(int(value) for value in companion["left_positions"])
        right = tuple(int(value) for value in companion["right_positions"])
        key = f"L{','.join(map(str, left))}|R{','.join(map(str, right))}"
        patterns[key] = patterns.get(key, 0) + 1
        rows.append(
            {
                "group_id": occurrence["group_id"],
                "left_old_position": occurrence["left_old_position"],
                "right_old_position": occurrence["right_old_position"],
                "pattern": key,
                "contains_left_position_8": 8 in left,
                "contains_right_position_8": 8 in right,
                "contains_terminal_8_8_entry": 8 in left and 8 in right,
            }
        )
    all_terminal = all(row["contains_terminal_8_8_entry"] for row in rows)
    if not all_terminal:
        raise AssertionError("a K288 companion unexpectedly lost the terminal entry")
    if len(patterns) != 6 or set(patterns.values()) != {4}:
        raise AssertionError("K289 six-pattern companion census changed")
    control = rational_coherent_control()
    return {
        "schema_version": "1.0",
        "result_id": "K301-ORDER-SEVEN-TERMINAL-SPLIT-BOUNDARY-CORRECTION",
        "created": "2026-09-22",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k288-order-seven-native-occurrence-measure.json",
                "lab/process/k289-order-seven-common-primitive-composition-boundary.json",
                "lab/process/k290-order-seven-native-rest-derivative-bank.json",
                "lab/process/k291-order-seven-native-interior-remainder.json",
                "lab/process/k293-order-seven-complete-native-tube-remainder.json",
                "lab/process/k300-order-seven-angular-method-selection.json",
            ],
            "occurrences": len(occurrences),
            "companion_patterns": len(patterns),
            "native_split_variables": ["u3", "z3"],
        },
        "terminal_split_face": {
            "primitive_identity": "s8=x*y*(1-u3); v8=x*(1-y)*(1-z3)",
            "terminal_argument": "s8+v8=x*(y*(1-u3)+(1-y)*(1-z3))",
            "admitted_approach": "u3=z3=1-epsilon with fixed x>0 and 0<y<1, followed by epsilon->0+",
            "kernel_asymptotic": "2*K1(w)~2/w as w->0+",
            "pointwise_consequence": "the (8,8) companion entry is unbounded on the full native split cube",
            "k290_assumed_entry_floor": k290["derivative_bank"]["x_bounds"][0],
            "assumed_floor_is_valid": False,
        },
        "companion_census": {
            "pattern_histogram": dict(sorted(patterns.items())),
            "rows": rows,
            "all_24_contain_terminal_8_8_entry": all_terminal,
            "k289_dependency_rows_replayed": len(k289["dependency_census"]["occurrences"]) == 24,
        },
        "coherent_non_cancellation_control": control,
        "correction": {
            "k290": {
                "survives": [
                    "occurrence census",
                    "factor typing",
                    "endpoint-safe old-kernel method on its proved inputs",
                ],
                "superseded": "uniform pointwise companion determinant value/derivative ceilings on the full y,u,z cube",
            },
            "k291": {
                "survives": ["formal product-rule composition"],
                "superseded": "numerical native-density local remainder ceiling because it consumes K290's invalid uniform companion bank",
                "predecessor_value": k291["native_density_remainder"]["complete_four_group_fourth_shape_derivative_abs_upper"],
            },
            "k293": {
                "survives": ["K292 disjoint tube atlas and exact volume composition"],
                "superseded": "numerical complete native tube remainder because it consumes the K291 ceiling",
                "predecessor_value": k293["complete_native_tube_remainder"]["x_y_u_z_integrated_abs_upper"],
            },
            "k300": {
                "survives": "K296/K297 projective and old-kernel face audit",
                "gap": "the claimed complete boundary cover omitted internal split faces; K302 must supply their Peano-weighted audit",
                "predecessor_qualitative_claim": k300["global_legality"]["qualitative_global_remainder_finite"],
            },
        },
        "decision": {
            "uniform_pointwise_companion_bank_rejected": True,
            "positive_peano_route_globally_killed": False,
            "reason": "pointwise unboundedness does not decide the Peano-kernel-weighted split integral",
            "next_exact_input": "derive split-integrated order-zero through order-two terminal Bessel jet bounds with the K299 y Peano kernel, then compose them with determinant cofactors and the remaining q/x factors",
        },
        "release_test": {
            "all_24_occurrences_replayed": len(rows) == 24,
            "all_six_patterns_replayed": len(patterns) == 6,
            "every_pattern_contains_8_8": all_terminal,
            "exact_nonzero_coherent_control": control["strictly_positive"],
            "artificial_positive_split_floor_introduced": False,
            "six_complete_coherent_norms_emitted": False,
            "radial_gamma_join_emitted": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k300["ledger_effect"],
        "claim_ceiling": "Exact correction of the K290 internal-split boundary premise: every K288 size-three companion contains an unbounded terminal (8,8) Bessel entry, so K290's uniform pointwise companion bank and the K291/K293 numerical remainders that consume it are superseded. Their exact occurrence/dependency and K292 disjoint-atlas results survive. The positive K299 route is not killed; its split-weighted integrability and complete coherent norms remain separate. No gamma join, action-column value, residual, K152 interval, source/ledger move, canon, paper, public or physical claim is established.",
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
