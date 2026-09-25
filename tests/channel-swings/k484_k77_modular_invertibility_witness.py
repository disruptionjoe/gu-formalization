#!/usr/bin/env python3
"""K484 modular nonzero-determinant witness for rational K77 matrices."""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from functools import reduce
from typing import Any

from k483_k77_square_determinant_exactness import determinant, matrix


def lcm(a: int, b: int) -> int:
    return abs(a * b) // math.gcd(a, b) if a and b else 0


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    return all(value % divisor for divisor in range(2, int(value ** 0.5) + 1))


def determinant_mod_prime(values: list[list[int]], prime: int) -> int:
    if not is_prime(prime):
        raise ValueError("prime modulus required")
    if not values or any(len(row) != len(values) for row in values):
        raise ValueError("nonempty square matrix required")
    a = [[value % prime for value in row] for row in values]
    det = 1
    for col in range(len(a)):
        pivot = next((row for row in range(col, len(a)) if a[row][col]), None)
        if pivot is None:
            return 0
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            det = -det
        pivot_value = a[col][col]
        det = (det * pivot_value) % prime
        inv = pow(pivot_value, -1, prime)
        for row in range(col + 1, len(a)):
            factor = a[row][col] * inv % prime
            for k in range(col, len(a)):
                a[row][k] = (a[row][k] - factor * a[col][k]) % prime
    return det % prime


def modular_witness(values: list[list[Any]], prime: int, proof_ref: str) -> dict[str, Any]:
    if not isinstance(proof_ref, str) or not proof_ref.strip():
        raise ValueError("nonempty matrix proof reference required")
    rational = matrix(values, len(values), len(values))
    denominator_lcm = reduce(lcm, (entry.denominator for row in rational for entry in row), 1)
    integer_matrix = [[int(entry * denominator_lcm) for entry in row] for row in rational]
    det_mod = determinant_mod_prime(integer_matrix, prime)
    if det_mod == 0:
        raise ValueError("zero modular determinant is inconclusive")
    rational_det = determinant(rational)
    if rational_det == 0:
        raise ValueError("modular witness contradicted exact determinant")
    return {
        "matrix_size": len(rational),
        "denominator_lcm": denominator_lcm,
        "prime": prime,
        "cleared_determinant_mod_prime": det_mod,
        "exact_rational_determinant": str(rational_det),
        "invertibility_certified": True,
        "proof_ref": proof_ref,
    }


def demo() -> dict[str, Any]:
    control_matrix = [
        [Fraction(1, 2), 0, 0, 0],
        [0, Fraction(1, 3), 0, 0],
        [0, 0, 2, 1],
        [0, 0, 1, 1],
    ]
    control = modular_witness(control_matrix, 5, "control#cleared-square-concatenation")
    return {
        "schema_version": "1.0",
        "result_id": "K484-K77-MODULAR-INVERTIBILITY-WITNESS",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "observed_to_native",
        "theorem": {
            "witness": "After one common denominator clears a rational square matrix, a nonzero determinant modulo one prime proves the rational determinant is nonzero.",
            "composition": "Combined with K483 nilpotence and Euler-zero typing, the witness certifies finite acyclicity without expanding a huge rational determinant.",
            "ceiling": "A zero modular determinant is inconclusive, and a nonzero witness supplies neither nilpotence nor action/domain ownership.",
        },
        "exact_control": control,
        "K77_application": {
            "square_certificate_size": 46592,
            "nilpotence_still_required": True,
            "native_matrix_present": False,
            "physical_cohomology_emitted": False,
        },
    }


def main() -> int:
    argparse.ArgumentParser().parse_args()
    print(json.dumps(demo(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
