#!/usr/bin/env python3
"""Exact form-dual ground-enclosure certificates for the K139 chart.

This kernel consumes operator-specific form data.  It does not assemble the
native singular IBC form, prove its exterior gap, or estimate its dual
residual.  Those inputs must come from a separate K139-domain construction.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import isqrt
from pathlib import Path
from typing import Any


Matrix = list[list[Fraction]]
Vector = list[Fraction]


class CertificateError(ValueError):
    """Raised when exact inputs do not certify the requested conclusion."""


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


def _swap_congruence(matrix: Matrix, left: int, right: int) -> None:
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
            values = [matrix[i][0] for i in range(1, size)]
            matrix = [
                [matrix[i][j] - values[i - 1] * values[j - 1] / pivot for j in range(1, size)]
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
        left, right = edge
        _swap_congruence(matrix, 0, left)
        if right == 0:
            right = left
        _swap_congruence(matrix, 1, right)
        coupling = matrix[0][1]
        negative += 1
        positive += 1
        tail = range(2, size)
        first = [matrix[k][0] for k in tail]
        second = [matrix[k][1] for k in tail]
        matrix = [
            [
                matrix[row][column]
                - (first[row - 2] * second[column - 2] + second[row - 2] * first[column - 2]) / coupling
                for column in tail
            ]
            for row in tail
        ]
    return negative, zero, positive


def sqrt_upper(value: Any, bits: int = 96) -> Fraction:
    """Return a dyadic rational rigorously above the positive square root."""
    radicand = q(value)
    if radicand < 0:
        raise CertificateError("square-root radicand must be nonnegative")
    if radicand == 0:
        return Fraction(0)
    denominator = 1 << bits
    target = radicand.numerator * denominator * denominator
    quotient, remainder = divmod(target, radicand.denominator)
    numerator = isqrt(quotient)
    if numerator * numerator * radicand.denominator < target or remainder:
        numerator += 1
    result = Fraction(numerator, denominator)
    if result * result < radicand:
        raise AssertionError("internal square-root enclosure failure")
    return result


def rectangular_matrix(rows: Any) -> Matrix:
    if not isinstance(rows, list) or not rows or not isinstance(rows[0], list) or not rows[0]:
        raise CertificateError("matrix must be a nonempty rectangular array")
    matrix = [[q(value) for value in row] for row in rows]
    width = len(matrix[0])
    if any(len(row) != width for row in matrix):
        raise CertificateError("matrix rows have unequal lengths")
    return matrix


def symmetric_matrix(rows: Any) -> Matrix:
    matrix = rectangular_matrix(rows)
    if len(matrix) != len(matrix[0]):
        raise CertificateError("matrix must be square")
    if any(matrix[i][j] != matrix[j][i] for i in range(len(matrix)) for j in range(len(matrix))):
        raise CertificateError("matrix must be exactly symmetric")
    return matrix


def vector(values: Any, size: int) -> Vector:
    if not isinstance(values, list) or len(values) != size:
        raise CertificateError("vector dimension does not match the form pencil")
    return [q(value) for value in values]


def transpose(matrix: Matrix) -> Matrix:
    return [list(row) for row in zip(*matrix)]


def matmul(left: Matrix, right: Matrix) -> Matrix:
    if not left or not right or len(left[0]) != len(right):
        raise CertificateError("incompatible matrix dimensions")
    return [
        [sum((left[i][k] * right[k][j] for k in range(len(right))), Fraction(0)) for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def matvec(matrix: Matrix, values: Vector) -> Vector:
    if not matrix or len(matrix[0]) != len(values):
        raise CertificateError("incompatible matrix/vector dimensions")
    return [sum((entry * value for entry, value in zip(row, values)), Fraction(0)) for row in matrix]


def dot(left: Vector, right: Vector) -> Fraction:
    if len(left) != len(right):
        raise CertificateError("incompatible vector dimensions")
    return sum((x * y for x, y in zip(left, right)), Fraction(0))


def add(left: Matrix, right: Matrix, right_scale: Fraction = Fraction(1)) -> Matrix:
    if len(left) != len(right) or any(len(a) != len(b) for a, b in zip(left, right)):
        raise CertificateError("incompatible matrix dimensions")
    return [
        [value + right_scale * other for value, other in zip(row, other_row)]
        for row, other_row in zip(left, right)
    ]


def congruence(matrix: Matrix, change: Matrix) -> Matrix:
    return matmul(transpose(change), matmul(matrix, change))


def form_pencil(form_rows: Any, gram_rows: Any) -> tuple[Matrix, Matrix]:
    form = symmetric_matrix(form_rows)
    gram = symmetric_matrix(gram_rows)
    if len(form) != len(gram):
        raise CertificateError("form and Gram matrices have different dimensions")
    if inertia(gram) != (0, 0, len(gram)):
        raise CertificateError("Gram matrix must be exactly positive definite")
    return form, gram


def generalized_spectral_count(form: Matrix, gram: Matrix, point: Fraction) -> tuple[int, int]:
    negative, zero, _ = inertia(add(form, gram, -point))
    return negative, zero


def isolate_generalized_eigenvalue(
    form_rows: Any,
    gram_rows: Any,
    index: int,
    lower: Any,
    upper: Any,
    steps: int = 48,
) -> tuple[Fraction, Fraction]:
    """Enclose an ordered symmetric-definite generalized Ritz value."""
    form, gram = form_pencil(form_rows, gram_rows)
    if not 1 <= index <= len(form):
        raise CertificateError("generalized eigenvalue index is outside the pencil")
    lo, hi = q(lower), q(upper)
    if lo >= hi:
        raise CertificateError("search interval must be ordered")
    below_lo, equal_lo = generalized_spectral_count(form, gram, lo)
    below_hi, equal_hi = generalized_spectral_count(form, gram, hi)
    if equal_lo or equal_hi:
        raise CertificateError("search endpoints must not be generalized eigenvalues")
    if below_lo >= index or below_hi < index:
        raise CertificateError("search interval does not bracket the requested generalized eigenvalue")
    for _ in range(steps):
        midpoint = (lo + hi) / 2
        below, equal = generalized_spectral_count(form, gram, midpoint)
        if equal and below < index <= below + equal:
            return midpoint, midpoint
        if below >= index:
            hi = midpoint
        else:
            lo = midpoint
    return lo, hi


def rayleigh_quotient(form_rows: Any, gram_rows: Any, coefficients: Any) -> Fraction:
    form, gram = form_pencil(form_rows, gram_rows)
    values = vector(coefficients, len(form))
    norm_sq = dot(values, matvec(gram, values))
    if norm_sq <= 0:
        raise CertificateError("trial vector must have positive Gram norm")
    return dot(values, matvec(form, values)) / norm_sq


def solve_linear(rows: Matrix, rhs: Vector) -> Vector:
    matrix = [row[:] + [value] for row, value in zip(rows, rhs)]
    size = len(matrix)
    for column in range(size):
        pivot = next((row for row in range(column, size) if matrix[row][column] != 0), None)
        if pivot is None:
            raise CertificateError("matrix is singular")
        matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
        scale = matrix[column][column]
        matrix[column] = [value / scale for value in matrix[column]]
        for row in range(size):
            if row == column:
                continue
            multiple = matrix[row][column]
            if multiple:
                matrix[row] = [
                    value - multiple * pivot_value
                    for value, pivot_value in zip(matrix[row], matrix[column])
                ]
    return [matrix[row][-1] for row in range(size)]


def finite_form_dual_residual_sq(
    form_rows: Any,
    gram_rows: Any,
    coefficients: Any,
    shift: Any,
) -> Fraction:
    """Exact positive-control residual in the shifted finite form metric.

    For a coefficient vector v, this returns
    r^T (A+sM)^-1 r / (v^T M v), where
    r=A v-rho M v.  Native use needs the complete infinite-form dual norm,
    not this finite-core quantity alone.
    """
    form, gram = form_pencil(form_rows, gram_rows)
    values = vector(coefficients, len(form))
    norm_sq = dot(values, matvec(gram, values))
    if norm_sq <= 0:
        raise CertificateError("trial vector must have positive Gram norm")
    rho = dot(values, matvec(form, values)) / norm_sq
    shifted_form = add(form, gram, q(shift))
    if inertia(shifted_form) != (0, 0, len(form)):
        raise CertificateError("shifted finite form metric is not positive definite")
    residual = [a - rho * b for a, b in zip(matvec(form, values), matvec(gram, values))]
    representer = solve_linear(shifted_form, residual)
    result = dot(residual, representer) / norm_sq
    if result < 0:
        raise AssertionError("positive shifted dual norm became negative")
    return result


def dual_temple_ground_enclosure(
    rayleigh: Any,
    dual_residual_sq_upper: Any,
    coercive_shift: Any,
    shifted_form_floor: Any,
    next_distinct_spectrum_lower: Any,
    *,
    bits: int = 96,
) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    """Return a ground interval, correction, and eigenspace projection error.

    Let A+s>=c>0, rho=a[u] for ||u||=1, and
    eps^2=||(A+s)^(-1/2)(A-rho)u||^2.  If all spectrum outside the
    ground eigenspace is at least b>rho, spectral measure gives

      delta=rho-lambda_0
      <= (E+sqrt(E^2+4g^2E))/(2g),
      E=(rho+s)eps^2, g=b-rho.

    It also gives ||P_u-P_0 u/||P_0u|||| <=
    sqrt(eps^2 (b+s)/(b-rho)^2).  Square roots are rounded upward.
    """
    rho = q(rayleigh)
    eps_sq = q(dual_residual_sq_upper)
    shift = q(coercive_shift)
    coercivity = q(shifted_form_floor)
    exterior = q(next_distinct_spectrum_lower)
    if eps_sq < 0:
        raise CertificateError("dual residual square must be nonnegative")
    if coercivity <= 0:
        raise CertificateError("shifted native form requires a positive coercivity floor")
    if rho + shift < coercivity:
        raise CertificateError("Rayleigh value conflicts with the supplied coercivity floor")
    if exterior <= rho:
        raise CertificateError("next distinct spectrum is not separated above the Rayleigh value")
    if exterior + shift <= 0:
        raise CertificateError("shifted exterior spectrum must be positive")
    gap = exterior - rho
    energy = (rho + shift) * eps_sq
    root = sqrt_upper(energy * energy + 4 * gap * gap * energy, bits=bits)
    correction = (energy + root) / (2 * gap)
    lower = rho - correction
    projection_sq = eps_sq * (exterior + shift) / (gap * gap)
    projection = sqrt_upper(projection_sq, bits=bits)
    if projection >= 1:
        raise CertificateError("dual residual does not close the ground-eigenspace projection gap")
    return lower, rho, correction, projection


def form_intertwines(
    source_form_rows: Any,
    source_gram_rows: Any,
    target_form_rows: Any,
    target_gram_rows: Any,
    unitary_rows: Any,
) -> bool:
    source_form, source_gram = form_pencil(source_form_rows, source_gram_rows)
    target_form, target_gram = form_pencil(target_form_rows, target_gram_rows)
    unitary = rectangular_matrix(unitary_rows)
    if len(unitary) != len(target_form) or len(unitary[0]) != len(source_form):
        raise CertificateError("intertwiner dimensions do not match the form pencils")
    return (
        congruence(target_gram, unitary) == source_gram
        and congruence(target_form, unitary) == source_form
    )


def validate_native_contract(native: Any) -> bool:
    if not isinstance(native, dict):
        raise CertificateError("native input contract must be an object")
    claim_native = native.get("claim_native", False)
    if claim_native is not True:
        return False
    charge = native.get("charge_sector")
    if charge not in ([0, 0], [1, 0], [0, 1]):
        raise CertificateError("native charge must be a selected representative or proved flavor partner")
    required = (
        "transformed_common_domain_proof_ref",
        "form_gram_serialization_ref",
        "coercive_shift_proof_ref",
        "dual_residual_proof_ref",
        "exterior_gap_proof_ref",
    )
    if any(not isinstance(native.get(key), str) or not native[key].strip() for key in required):
        raise CertificateError("native claim is missing an operator-specific proof reference")
    if charge == [0, 1] and (
        not isinstance(native.get("signed_flavor_transport_proof_ref"), str)
        or not native["signed_flavor_transport_proof_ref"].strip()
    ):
        raise CertificateError("q=(0,1) native transport requires the signed flavor proof")
    return True


def solve(payload: dict[str, Any]) -> dict[str, Any]:
    form, gram = form_pencil(payload["form_matrix"], payload["gram_matrix"])
    index = int(payload.get("eigenvalue_index", 1))
    if index != 1:
        raise CertificateError("K152 certifies the ground cluster only")
    ritz_lo, ritz_hi = isolate_generalized_eigenvalue(
        form,
        gram,
        index,
        payload["search_interval"][0],
        payload["search_interval"][1],
        int(payload.get("bisection_steps", 48)),
    )
    rho = rayleigh_quotient(form, gram, payload["trial_vector"])
    if rho < ritz_lo:
        raise CertificateError("trial Rayleigh value lies below the certified ground Ritz interval")
    lower, _, correction, projection = dual_temple_ground_enclosure(
        rho,
        payload["dual_residual_sq_upper"],
        payload["coercive_shift"],
        payload["shifted_form_floor"],
        payload["next_distinct_spectrum_lower"],
        bits=int(payload.get("sqrt_bits", 96)),
    )
    native = validate_native_contract(payload.get("native_input", {}))
    return {
        "schema_version": "1.0",
        "arithmetic": "exact_rational_with_outward_dyadic_square_roots",
        "generalized_ritz_interval": [qstr(ritz_lo), qstr(ritz_hi)],
        "trial_rayleigh_quotient": qstr(rho),
        "ground_interval": [qstr(lower), qstr(min(rho, ritz_hi))],
        "dual_temple_correction_upper": qstr(correction),
        "ground_eigenspace_projection_error_upper": qstr(projection),
        "uses_raw_hilbert_coupling_norm": False,
        "native_input_contract_satisfied": native,
        "native_ibc_inputs_assembled_by_solver": False,
    }


DEMO_FORM = [["-1", "0"], ["0", "2"]]
DEMO_GRAM = [["1", "0"], ["0", "1"]]
DEMO_VECTOR = ["1", "1/4"]
DEMO_SHIFT = "2"
DEMO_RESIDUAL_SQ = qstr(
    finite_form_dual_residual_sq(DEMO_FORM, DEMO_GRAM, DEMO_VECTOR, DEMO_SHIFT)
)
DEMO = {
    "form_matrix": DEMO_FORM,
    "gram_matrix": DEMO_GRAM,
    "eigenvalue_index": 1,
    "search_interval": ["-2", "0"],
    "bisection_steps": 32,
    "trial_vector": DEMO_VECTOR,
    "coercive_shift": DEMO_SHIFT,
    "shifted_form_floor": "1",
    "dual_residual_sq_upper": DEMO_RESIDUAL_SQ,
    "next_distinct_spectrum_lower": "2",
    "sqrt_bits": 64,
    "native_input": {"claim_native": False},
}


def main() -> int:
    parser = argparse.ArgumentParser()
    source = parser.add_mutually_exclusive_group()
    source.add_argument("--input", type=Path)
    source.add_argument("--demo", action="store_true")
    args = parser.parse_args()
    try:
        payload = DEMO if args.demo or args.input is None else json.loads(args.input.read_text())
        print(json.dumps(solve(payload), indent=2, sort_keys=True))
    except (CertificateError, KeyError, TypeError, ValueError, json.JSONDecodeError, OSError) as exc:
        print(json.dumps({"certified": False, "error": str(exc)}, sort_keys=True))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
