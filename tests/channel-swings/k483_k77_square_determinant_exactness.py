#!/usr/bin/env python3
"""K483 square-determinant exactness certificate for an Euler-zero complex."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from typing import Any


def q(value: Any) -> Fraction:
    return value if isinstance(value, Fraction) else Fraction(value)


def matrix(values: list[list[Any]], rows: int, cols: int) -> list[list[Fraction]]:
    if len(values) != rows or any(len(row) != cols for row in values):
        raise ValueError("matrix shape mismatch")
    return [[q(value) for value in row] for row in values]


def transpose(values: list[list[Fraction]]) -> list[list[Fraction]]:
    if not values:
        return []
    return [list(column) for column in zip(*values)]


def matmul(left, right):
    if not left or not right or len(left[0]) != len(right):
        raise ValueError("matrix product shape mismatch")
    return [[sum(left[i][k] * right[k][j] for k in range(len(right)))
             for j in range(len(right[0]))] for i in range(len(left))]


def determinant(values: list[list[Fraction]]) -> Fraction:
    if not values or any(len(row) != len(values) for row in values):
        raise ValueError("nonempty square matrix required")
    a = [row[:] for row in values]
    det = Fraction(1)
    for col in range(len(a)):
        pivot = next((row for row in range(col, len(a)) if a[row][col]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            det = -det
        pivot_value = a[col][col]
        det *= pivot_value
        for row in range(col + 1, len(a)):
            if a[row][col]:
                factor = a[row][col] / pivot_value
                for k in range(col, len(a)):
                    a[row][k] -= factor * a[col][k]
    return det


def assess(n2: int, n1: int, n0: int, d2_values, d1_values) -> dict[str, Any]:
    if min(n2, n1, n0) <= 0 or n1 != n2 + n0:
        raise ValueError("positive Euler-zero dimensions required")
    d2 = matrix(d2_values, n1, n2)
    d1 = matrix(d1_values, n0, n1)
    product = matmul(d1, d2)
    nilpotent = all(value == 0 for row in product for value in row)
    square = [d2[row] + transpose(d1)[row] for row in range(n1)]
    det = determinant(square)
    exact = nilpotent and det != 0
    return {
        "dimensions_C2_C1_C0": [n2, n1, n0],
        "D1_D2_zero": nilpotent,
        "concatenation": "[D2,D1^T]",
        "square_size": n1,
        "determinant": str(det),
        "concatenation_invertible": det != 0,
        "acyclic_certified": exact,
    }


def demo() -> dict[str, Any]:
    d2 = [[1, 0], [0, 1], [0, 0], [0, 0]]
    exact = assess(2, 4, 2, d2, [[0, 0, 2, 1], [0, 0, 1, 1]])
    rank_defect = assess(2, 4, 2, d2, [[0, 0, 1, 0], [0, 0, 0, 0]])
    non_nilpotent = assess(2, 4, 2, d2, [[1, 0, 1, 0], [0, 1, 0, 1]])
    return {
        "schema_version": "1.0",
        "result_id": "K483-K77-SQUARE-DETERMINANT-EXACTNESS",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "observed_to_native",
        "theorem": {
            "criterion": "For an Euler-zero rational complex with D1 D2=0, acyclicity is equivalent to invertibility of the square concatenation [D2,D1^T].",
            "necessity": "Nilpotence is independent and mandatory; an invertible concatenation alone is not a complex.",
            "ceiling": "The determinant certifies supplied finite matrices only and selects no action or physical domain.",
        },
        "exact_control": exact,
        "rank_defect_control": rank_defect,
        "non_nilpotent_control": non_nilpotent,
        "K77_application": {
            "dimensions_C2_C1_C0": [10752, 46592, 35840],
            "square_certificate_size": 46592,
            "native_matrices_present": False,
            "physical_cohomology_emitted": False,
        },
    }


def main() -> int:
    argparse.ArgumentParser().parse_args()
    print(json.dumps(demo(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
