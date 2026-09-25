#!/usr/bin/env python3
"""K480 exact quotient-basis completion theorem for a three-term complex."""

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


def rank(values: list[list[Fraction]]) -> int:
    a = [row[:] for row in values]
    if not a:
        return 0
    rows, cols = len(a), len(a[0])
    pivot_row = 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if a[r][col]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        scale = a[pivot_row][col]
        a[pivot_row] = [value / scale for value in a[pivot_row]]
        for r in range(rows):
            if r != pivot_row and a[r][col]:
                factor = a[r][col]
                a[r] = [x - factor * y for x, y in zip(a[r], a[pivot_row])]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def matmul(left: list[list[Fraction]], right: list[list[Fraction]]) -> list[list[Fraction]]:
    if not left or not right or len(left[0]) != len(right):
        raise ValueError("matrix product shape mismatch")
    return [[sum(left[i][k] * right[k][j] for k in range(len(right)))
             for j in range(len(right[0]))] for i in range(len(left))]


def assess_complex(n2: int, n1: int, n0: int, d2_values, d1_values) -> dict:
    if min(n2, n1, n0) < 0:
        raise ValueError("nonnegative dimensions required")
    d2 = matrix(d2_values, n1, n2)
    d1 = matrix(d1_values, n0, n1)
    product = matmul(d1, d2) if n0 and n1 and n2 else [[Fraction(0)]]
    nilpotent = all(value == 0 for row in product for value in row)
    r2, r1 = rank(d2), rank(d1)
    homology = [n2 - r2, n1 - r2 - r1, n0 - r1]
    quotient_dim = n1 - r2
    euler_zero = n2 - n1 + n0 == 0
    exact = nilpotent and homology == [0, 0, 0]
    return {
        "dimensions_C2_C1_C0": [n2, n1, n0],
        "ranks_D2_D1": [r2, r1],
        "D1_D2_zero": nilpotent,
        "euler_characteristic_zero": euler_zero,
        "quotient_dimension_C1_mod_image_D2": quotient_dim,
        "target_dimension_C0": n0,
        "homology_dimensions_H2_H1_H0": homology,
        "D1_descends_to_quotient_isomorphism": exact,
        "acyclic": exact,
    }


def demo() -> dict:
    d2 = [[1, 0], [0, 1], [0, 0], [0, 0]]
    left_null_basis = [[0, 0, 1, 0], [0, 0, 0, 1]]
    change = [[2, 1], [1, 1]]
    d1 = [[0, 0, 2, 1], [0, 0, 1, 1]]  # A times the quotient basis
    exact = assess_complex(2, 4, 2, d2, d1)
    defect = assess_complex(2, 4, 2, d2, [[0, 0, 1, 0], [0, 0, 0, 0]])
    return {
        "schema_version": "1.0",
        "result_id": "K480-K77-QUOTIENT-BASIS-COMPLETION",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "observed_to_native",
        "theorem": {
            "fixed_D2": "If D2 has full column rank, nilpotence makes D1 descend through C1/im(D2).",
            "euler_zero": "When n1-n2=n0, acyclicity is equivalent to the descended D1 being an isomorphism.",
            "construction": "Choose a basis L of the annihilator of im(D2) and any invertible A; D1=A L gives exactness.",
            "ceiling": "The theorem constructs coefficient families only after D2 is supplied; it does not select action coefficients or a physical domain.",
        },
        "exact_control": exact,
        "rank_defect_control": defect,
        "construction_control": {
            "D2": d2,
            "left_null_basis_L": left_null_basis,
            "invertible_change_A": change,
            "D1_equals_A_times_L": d1,
            "det_A": 1,
        },
        "K77_application": {
            "dimensions_C2_C1_C0": [10752, 46592, 35840],
            "quotient_dimension_after_full_rank_D2": 35840,
            "required_descended_D1_rank": 35840,
            "native_D2_present": False,
            "native_D1_present": False,
            "physical_cohomology_emitted": False,
        },
    }


def main() -> int:
    argparse.ArgumentParser().parse_args()
    print(json.dumps(demo(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
