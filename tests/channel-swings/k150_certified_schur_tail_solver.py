#!/usr/bin/env python3
"""Exact rational certificate kernel for K150 Ritz/Schur tail enclosures.

The kernel deliberately does not assemble a native singular-IBC matrix or its
tail constants.  It checks and propagates exact inputs supplied by a separate
operator-specific proof.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import isqrt
from pathlib import Path
from typing import Any


class CertificateError(ValueError):
    """Raised when a requested conclusion is not certified by the inputs."""


def q(value: Any) -> Fraction:
    if isinstance(value, Fraction):
        return value
    if isinstance(value, int):
        return Fraction(value)
    if not isinstance(value, str):
        raise CertificateError("exact inputs must be integers or rational strings")
    try:
        return Fraction(value)
    except (ValueError, ZeroDivisionError) as exc:
        raise CertificateError(f"invalid rational value: {value!r}") from exc


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def symmetric_matrix(rows: Any) -> list[list[Fraction]]:
    if not isinstance(rows, list) or not rows:
        raise CertificateError("matrix must be a nonempty square array")
    matrix = [[q(value) for value in row] for row in rows]
    size = len(matrix)
    if any(len(row) != size for row in matrix):
        raise CertificateError("matrix must be square")
    if any(matrix[i][j] != matrix[j][i] for i in range(size) for j in range(size)):
        raise CertificateError("matrix must be exactly symmetric")
    return matrix


def _swap_congruence(matrix: list[list[Fraction]], left: int, right: int) -> None:
    if left == right:
        return
    matrix[left], matrix[right] = matrix[right], matrix[left]
    for row in matrix:
        row[left], row[right] = row[right], row[left]


def inertia(rows: Any) -> tuple[int, int, int]:
    """Return exact (negative, zero, positive) inertia by congruence pivots."""
    matrix = symmetric_matrix(rows)
    negative = zero = positive = 0
    while matrix:
        size = len(matrix)
        diagonal = next((i for i in range(size) if matrix[i][i] != 0), None)
        if diagonal is not None:
            _swap_congruence(matrix, 0, diagonal)
            pivot = matrix[0][0]
            if pivot > 0:
                positive += 1
            else:
                negative += 1
            vector = [matrix[i][0] for i in range(1, size)]
            matrix = [
                [matrix[i][j] - vector[i - 1] * vector[j - 1] / pivot for j in range(1, size)]
                for i in range(1, size)
            ]
            continue

        edge = next(
            ((i, j) for i in range(size) for j in range(i + 1, size) if matrix[i][j] != 0),
            None,
        )
        if edge is None:
            zero += size
            break
        i, j = edge
        _swap_congruence(matrix, 0, i)
        if j == 0:
            j = i
        _swap_congruence(matrix, 1, j)
        coupling = matrix[0][1]
        negative += 1
        positive += 1
        tail = range(2, size)
        first = [matrix[k][0] for k in tail]
        second = [matrix[k][1] for k in tail]
        matrix = [
            [
                matrix[r][c]
                - (first[r - 2] * second[c - 2] + second[r - 2] * first[c - 2]) / coupling
                for c in tail
            ]
            for r in tail
        ]
    return negative, zero, positive


def shifted(matrix: list[list[Fraction]], point: Fraction) -> list[list[Fraction]]:
    return [
        [value - (point if i == j else 0) for j, value in enumerate(row)]
        for i, row in enumerate(matrix)
    ]


def spectral_count(matrix: list[list[Fraction]], point: Fraction) -> tuple[int, int]:
    negative, zero, _ = inertia(shifted(matrix, point))
    return negative, zero


def isolate_eigenvalue(
    rows: Any,
    index: int,
    lower: Any,
    upper: Any,
    steps: int = 48,
) -> tuple[Fraction, Fraction]:
    """Enclose the one-based ordered eigenvalue using exact inertia bisection."""
    matrix = symmetric_matrix(rows)
    if not 1 <= index <= len(matrix):
        raise CertificateError("eigenvalue index is outside the matrix")
    lo, hi = q(lower), q(upper)
    if lo >= hi:
        raise CertificateError("search interval must be ordered")
    below_lo, equal_lo = spectral_count(matrix, lo)
    below_hi, equal_hi = spectral_count(matrix, hi)
    if equal_lo or equal_hi:
        raise CertificateError("search endpoints must not be eigenvalues")
    if below_lo >= index or below_hi < index:
        raise CertificateError("search interval does not bracket the requested eigenvalue")
    for _ in range(steps):
        mid = (lo + hi) / 2
        below, equal = spectral_count(matrix, mid)
        if equal and below < index <= below + equal:
            return mid, mid
        if below >= index:
            hi = mid
        else:
            lo = mid
    return lo, hi


def sqrt_upper(value: Any, bits: int = 96) -> Fraction:
    """Return a dyadic rational rigorously above sqrt(value)."""
    radicand = q(value)
    if radicand < 0:
        raise CertificateError("square-root radicand must be nonnegative")
    if radicand == 0:
        return Fraction(0)
    denominator = 1 << bits
    target = radicand.numerator * denominator * denominator
    quotient, remainder = divmod(target, radicand.denominator)
    floor_root = isqrt(quotient)
    numerator = floor_root
    if numerator * numerator * radicand.denominator < target:
        numerator += 1
    elif remainder:
        numerator += 1
    result = Fraction(numerator, denominator)
    if result * result < radicand:
        raise AssertionError("internal square-root enclosure failure")
    return result


def schur_tail_enclosure(
    ritz_lower: Any,
    ritz_upper: Any,
    complement_floor: Any,
    coupling_norm_sq_upper: Any,
) -> tuple[Fraction, Fraction, Fraction]:
    """Enclose a full-operator eigenvalue from a conforming Ritz block.

    If A is the Ritz compression, D >= d on its orthogonal complement and
    ||P H (1-P)||^2 <= b2, then the kth full eigenvalue is at least
    (a+d-sqrt((d-a)^2+4b2))/2 and at most the kth Ritz value.  A rational
    upper enclosure of the square root makes the reported lower endpoint
    rigorous.
    """
    a_lo, a_hi = q(ritz_lower), q(ritz_upper)
    floor, coupling_sq = q(complement_floor), q(coupling_norm_sq_upper)
    if a_lo > a_hi:
        raise CertificateError("Ritz interval is reversed")
    if coupling_sq < 0:
        raise CertificateError("coupling norm square must be nonnegative")
    if a_hi >= floor:
        raise CertificateError("Ritz level is not separated from the complement floor")
    root = sqrt_upper((floor - a_lo) ** 2 + 4 * coupling_sq)
    lower = (a_lo + floor - root) / 2
    epsilon = a_lo - lower
    if epsilon < 0:
        raise AssertionError("internal Schur correction failure")
    return lower, a_hi, epsilon


def projection_error(residual_norm_upper: Any, exterior_separation_lower: Any) -> Fraction:
    residual, separation = q(residual_norm_upper), q(exterior_separation_lower)
    if residual < 0 or separation <= 0:
        raise CertificateError("residual and separation bounds must be positive")
    if residual >= separation:
        raise CertificateError("residual does not close the exterior spectral gap")
    return residual / separation


def gram_error(
    projection_error_upper: Any,
    channel_count: int,
    endpoint_norm_upper: Any,
) -> Fraction:
    eta = q(projection_error_upper)
    endpoint = q(endpoint_norm_upper)
    if eta < 0 or channel_count <= 0 or endpoint < 0:
        raise CertificateError("invalid Gram-error inputs")
    return 2 * channel_count * endpoint * endpoint * eta


def unique_first_threshold(intervals: dict[str, list[Any]], candidate: str) -> bool:
    if candidate not in intervals or len(intervals) < 2:
        raise CertificateError("threshold candidate set is incomplete")
    if any(not isinstance(value, list) or len(value) != 2 for value in intervals.values()):
        raise CertificateError("each threshold requires exactly two endpoints")
    parsed = {key: (q(value[0]), q(value[1])) for key, value in intervals.items()}
    if any(lo > hi for lo, hi in parsed.values()):
        raise CertificateError("threshold interval is reversed")
    return parsed[candidate][1] < min(lo for key, (lo, _) in parsed.items() if key != candidate)


def certified_rank(
    gram_rows: Any,
    gram_error_upper: Any,
    structural_kernel_dimension: int = 0,
) -> int:
    matrix = symmetric_matrix(gram_rows)
    size = len(matrix)
    eta = q(gram_error_upper)
    if eta < 0 or not 0 <= structural_kernel_dimension <= size:
        raise CertificateError("invalid rank-certificate inputs")
    negative, _, _ = inertia(matrix)
    if negative:
        raise CertificateError("approximate Gram matrix is not positive semidefinite")
    below, equal = spectral_count(matrix, eta)
    if equal:
        raise CertificateError("Gram margin is exactly zero")
    permitted_small = structural_kernel_dimension
    if below > permitted_small:
        raise CertificateError("positive Gram margin does not close")
    certified = size - permitted_small
    if below < permitted_small:
        raise CertificateError("structural kernel and numerical rank evidence disagree")
    return certified


def solve(payload: dict[str, Any]) -> dict[str, Any]:
    matrix = symmetric_matrix(payload["ritz_matrix"])
    lo, hi = isolate_eigenvalue(
        matrix,
        int(payload["eigenvalue_index"]),
        payload["search_interval"][0],
        payload["search_interval"][1],
        int(payload.get("bisection_steps", 48)),
    )
    full_lo, full_hi, epsilon = schur_tail_enclosure(
        lo,
        hi,
        payload["complement_floor"],
        payload["coupling_norm_sq_upper"],
    )
    eta_projection = projection_error(
        payload["residual_norm_upper"], payload["exterior_separation_lower"]
    )
    eta_gram = gram_error(
        eta_projection,
        int(payload["channel_count"]),
        payload["endpoint_norm_upper"],
    )
    rank = certified_rank(
        payload["approximate_gram"],
        eta_gram,
        int(payload.get("structural_kernel_dimension", 0)),
    )
    first = str(payload["first_threshold_candidate"])
    return {
        "schema_version": "1.0",
        "arithmetic": "exact_rational",
        "ritz_interval": [qstr(lo), qstr(hi)],
        "full_operator_interval": [qstr(full_lo), qstr(full_hi)],
        "schur_correction_upper": qstr(epsilon),
        "projection_error_upper": qstr(eta_projection),
        "gram_error_upper": qstr(eta_gram),
        "first_threshold_candidate": first,
        "first_threshold_certified": unique_first_threshold(payload["threshold_intervals"], first),
        "gram_rank_certified": rank,
        "native_ibc_inputs_assembled_by_solver": False,
    }


DEMO = {
    "ritz_matrix": [["-1", "1/4"], ["1/4", "1/2"]],
    "eigenvalue_index": 1,
    "search_interval": ["-2", "0"],
    "bisection_steps": 32,
    "complement_floor": "3",
    "coupling_norm_sq_upper": "1/16",
    "residual_norm_upper": "1/100",
    "exterior_separation_lower": "1/2",
    "channel_count": 4,
    "endpoint_norm_upper": "1",
    "approximate_gram": [
        ["1/2", "0", "0", "0"],
        ["0", "1/3", "0", "0"],
        ["0", "0", "1/4", "0"],
        ["0", "0", "0", "1/5"],
    ],
    "structural_kernel_dimension": 0,
    "threshold_intervals": {
        "a": ["-3/2", "-7/5"],
        "b": ["-1", "-9/10"],
        "c": ["-1/2", "-2/5"],
    },
    "first_threshold_candidate": "a",
}


def main() -> int:
    parser = argparse.ArgumentParser()
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--input", type=Path)
    source.add_argument("--demo", action="store_true")
    args = parser.parse_args()
    try:
        payload = DEMO if args.demo else json.loads(args.input.read_text())
        print(json.dumps(solve(payload), indent=2, sort_keys=True))
    except (CertificateError, KeyError, TypeError, ValueError, json.JSONDecodeError, OSError) as exc:
        print(json.dumps({"certified": False, "error": str(exc)}, sort_keys=True))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
