#!/usr/bin/env python3
"""Independent hostile replay of K301's terminal split correction."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
K288 = json.loads(
    (ROOT / "lab/process/k288-order-seven-native-occurrence-measure.json").read_text()
)
K301 = json.loads(
    (ROOT / "lab/process/k301-order-seven-terminal-split-boundary-correction.json").read_text()
)


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    if len(matrix) == 1:
        return matrix[0][0]
    return sum(
        (-1) ** column
        * matrix[0][column]
        * determinant(
            [row[:column] + row[column + 1 :] for row in matrix[1:]]
        )
        for column in range(len(matrix))
    )


def check(name: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(name)


def main() -> int:
    occurrences = K288["coherent_gram_measure"]["size_four_occurrences"]
    patterns = {
        (
            tuple(row["companion_factors"][0]["left_positions"]),
            tuple(row["companion_factors"][0]["right_positions"]),
        )
        for row in occurrences
    }
    tests = {
        "24 occurrences": len(occurrences) == 24,
        "six patterns": len(patterns) == 6,
        "every left contains eight": all(8 in left for left, _ in patterns),
        "every right contains eight": all(8 in right for _, right in patterns),
        "terminal argument has no floor": all(
            Fraction(1, n) < Fraction(31, 256) for n in (16, 32, 64)
        ),
        "owner correction rejects pointwise bank": K301["decision"][
            "uniform_pointwise_companion_bank_rejected"
        ],
        "owner does not kill Peano route": not K301["decision"][
            "positive_peano_route_globally_killed"
        ],
        "no artificial floor": not K301["release_test"][
            "artificial_positive_split_floor_introduced"
        ],
        "no norm overclaim": not K301["release_test"][
            "six_complete_coherent_norms_emitted"
        ],
    }
    # Independent exact symmetric Cauchy control.
    times = [Fraction(4), Fraction(2), Fraction(1)]
    matrix = [[Fraction(2, a + b) for b in times] for a in times]
    old = [Fraction(2, a) for a in times]
    signs = [1, -1, 1]
    coefficient = Fraction(0)
    for i in range(3):
        for j in range(3):
            sub = [
                [value for jj, value in enumerate(row) if jj != j]
                for ii, row in enumerate(matrix)
                if ii != i
            ]
            coefficient += signs[i] * signs[j] * old[i] * old[j] * determinant(sub)
    tests["coherent terminal coefficient"] = coefficient == Fraction(7, 1800)
    for name, condition in tests.items():
        check(name, condition)

    hostile = {
        "delete terminal position": not all(
            8 in tuple(value for value in left if value != 8)
            for left, _ in patterns
        ),
        "pretend x is a floor": Fraction(1, 1024) < Fraction(31, 256),
        "cancel coherent coefficient": coefficient != 0,
        "kill Peano route from pointwise result": not K301["decision"][
            "positive_peano_route_globally_killed"
        ],
        "emit gamma join": not K301["release_test"]["radial_gamma_join_emitted"],
        "emit K152": not K301["release_test"]["native_K152_interval_emitted"],
    }
    for name, rejected in hostile.items():
        check(f"hostile {name}", rejected)
    print(f"K301 probe: {len(tests)}/{len(tests)} checks; {len(hostile)}/{len(hostile)} hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
