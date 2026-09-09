#!/usr/bin/env python3
"""K171 bath-block action-column identifiability certificates.

K170 determines scalar Neumann-word norms because the K139 boundary map raises
bath number.  For the base action, however, the number-preserving regular core
is followed by the adjoint Neumann series, which lowers bath number.  This
module compiles the exact finite block formula and proves that Gram, Rayleigh,
and reference-shape data do not determine the complete action column.

The finite controls are algebraic witnesses only.  They are not the missing
native continuum K139/K162 action data.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from typing import Any, Sequence


Matrix = list[list[Fraction]]
Vector = list[Fraction]


class CertificateError(ValueError):
    """Raised when a graded action-column certificate is incomplete."""


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


def matrix(rows: Sequence[Sequence[Any]]) -> Matrix:
    result = [[q(value) for value in row] for row in rows]
    if not result or any(len(row) != len(result) for row in result):
        raise CertificateError("matrix must be nonempty and square")
    return result


def identity(size: int) -> Matrix:
    return [[Fraction(i == j) for j in range(size)] for i in range(size)]


def transpose(rows: Matrix) -> Matrix:
    return [list(row) for row in zip(*rows)]


def matmul(left: Matrix, right: Matrix) -> Matrix:
    if not left or not right or len(left[0]) != len(right):
        raise CertificateError("incompatible matrix dimensions")
    return [
        [sum((left[i][k] * right[k][j] for k in range(len(right))), Fraction()) for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def matvec(rows: Matrix, values: Vector) -> Vector:
    if not rows or len(rows[0]) != len(values):
        raise CertificateError("incompatible matrix/vector dimensions")
    return [sum((entry * value for entry, value in zip(row, values, strict=True)), Fraction()) for row in rows]


def add(left: Matrix, right: Matrix) -> Matrix:
    if len(left) != len(right) or any(len(a) != len(b) for a, b in zip(left, right, strict=True)):
        raise CertificateError("incompatible matrix dimensions")
    return [[x + y for x, y in zip(a, b, strict=True)] for a, b in zip(left, right, strict=True)]


def dot(left: Vector, right: Vector) -> Fraction:
    return sum((x * y for x, y in zip(left, right, strict=True)), Fraction())


def inverse(rows: Matrix) -> Matrix:
    size = len(rows)
    work = [row[:] + unit[:] for row, unit in zip(rows, identity(size), strict=True)]
    for column in range(size):
        pivot = next((row for row in range(column, size) if work[row][column]), None)
        if pivot is None:
            raise CertificateError("matrix is singular")
        work[column], work[pivot] = work[pivot], work[column]
        scale = work[column][column]
        work[column] = [value / scale for value in work[column]]
        for row in range(size):
            if row == column or not work[row][column]:
                continue
            factor = work[row][column]
            work[row] = [x - factor * y for x, y in zip(work[row], work[column], strict=True)]
    return [row[size:] for row in work]


def power(rows: Matrix, exponent: int) -> Matrix:
    if exponent < 0:
        raise CertificateError("matrix power must be nonnegative")
    result = identity(len(rows))
    base = rows
    while exponent:
        if exponent & 1:
            result = matmul(result, base)
        base = matmul(base, base)
        exponent //= 2
    return result


def vector_add(*vectors: Vector) -> Vector:
    if not vectors or any(len(vector) != len(vectors[0]) for vector in vectors):
        raise CertificateError("vector sum has incompatible dimensions")
    return [sum((vector[i] for vector in vectors), Fraction()) for i in range(len(vectors[0]))]


def projector(values: Vector, sectors: Sequence[int], sector: int) -> Vector:
    return [value if label == sector else Fraction() for value, label in zip(values, sectors, strict=True)]


def validate_grading(boundary: Matrix, regular_core: Matrix, sectors: Sequence[int]) -> None:
    size = len(boundary)
    if len(regular_core) != size or len(sectors) != size:
        raise CertificateError("grading, boundary, and core dimensions differ")
    if regular_core != transpose(regular_core):
        raise CertificateError("regular core must be exactly Hermitian")
    for row in range(size):
        for column in range(size):
            if boundary[row][column] and sectors[row] != sectors[column] + 1:
                raise CertificateError("G must raise bath number exactly one")
            if regular_core[row][column] and sectors[row] != sectors[column]:
                raise CertificateError("W must preserve bath number")


def graded_action_column(
    *, boundary_rows: Sequence[Sequence[Any]], regular_core_rows: Sequence[Sequence[Any]],
    shifted_free_rows: Sequence[Sequence[Any]], seed_values: Sequence[Any], sectors: Sequence[int],
) -> dict[str, Any]:
    """Compile ``R phi=A phi+S* W S phi`` and its exact number blocks.

    On a finite graded control G is nilpotent.  If ``g_n=G^n phi``, then

      P_k R phi = P_k A phi + sum_{n>=k} P_k (G*)^(n-k) W_n g_n.

    The formula is also the finite truncation of the native limiting column.
    """
    boundary = matrix(boundary_rows)
    regular_core = matrix(regular_core_rows)
    shifted_free = matrix(shifted_free_rows)
    if shifted_free != transpose(shifted_free):
        raise CertificateError("shifted free block must be exactly Hermitian")
    validate_grading(boundary, regular_core, sectors)
    seed = [q(value) for value in seed_values]
    if len(seed) != len(boundary) or not any(seed):
        raise CertificateError("seed dimension mismatch or zero seed")
    if any(value and sectors[index] != 0 for index, value in enumerate(seed)):
        raise CertificateError("K171 seed must lie in bath-number zero")

    max_sector = max(sectors)
    words = [matvec(power(boundary, order), seed) for order in range(max_sector + 1)]
    if any(words[-1]) and any(matvec(boundary, words[-1])):
        raise CertificateError("finite grading does not close at the declared maximum sector")
    neumann = identity(len(boundary))
    for order in range(1, max_sector + 1):
        neumann = add(neumann, power(boundary, order))
    metric = matmul(transpose(neumann), neumann)
    regular = add(shifted_free, matmul(transpose(neumann), matmul(regular_core, neumann)))
    direct = matvec(regular, seed)

    components: list[Vector] = []
    for bath_number in range(max_sector + 1):
        terms = [projector(matvec(shifted_free, seed), sectors, bath_number)]
        for word_number in range(bath_number, max_sector + 1):
            lowered = matvec(
                power(transpose(boundary), word_number - bath_number),
                matvec(regular_core, words[word_number]),
            )
            terms.append(projector(lowered, sectors, bath_number))
        components.append(vector_add(*terms))
    reconstructed = vector_add(*components)
    if reconstructed != direct:
        raise AssertionError("bath-block action-column formula failed")
    return {
        "word_vectors": words,
        "word_norm_sq": [dot(word, word) for word in words],
        "metric": metric,
        "regular_form": regular,
        "action_column": direct,
        "bath_components": components,
        "component_formula_verified": True,
    }


def matched_residual_sq(regular: Matrix, metric: Matrix, seed: Vector) -> tuple[Fraction, Vector, Fraction]:
    metric_norm = dot(seed, matvec(metric, seed))
    rayleigh = dot(seed, matvec(regular, seed)) / metric_norm
    residual = vector_add(matvec(regular, seed), [-rayleigh * value for value in matvec(metric, seed)])
    dual = dot(residual, matvec(inverse(metric), residual))
    return rayleigh, residual, dual


def same_scalar_different_column_control() -> dict[str, Any]:
    sectors = [0, 1, 1, 2]
    boundary = [
        [0, 0, 0, 0],
        ["1/4", 0, 0, 0],
        [0, 0, 0, 0],
        [0, "1/5", 0, 0],
    ]
    shifted_free = [[8, 0, 0, 0], [0, 9, 0, 0], [0, 0, 9, 0], [0, 0, 0, 10]]
    baseline_core = [[-7, 0, 0, 0], [0, 2, 0, 0], [0, 0, 3, 0], [0, 0, 0, 4]]
    rotated_core = [[-7, 0, 0, 0], [0, 2, 1, 0], [0, 1, 3, 0], [0, 0, 0, 4]]
    seed = [1, 0, 0, 0]
    first = graded_action_column(
        boundary_rows=boundary, regular_core_rows=baseline_core,
        shifted_free_rows=shifted_free, seed_values=seed, sectors=sectors,
    )
    second = graded_action_column(
        boundary_rows=boundary, regular_core_rows=rotated_core,
        shifted_free_rows=shifted_free, seed_values=seed, sectors=sectors,
    )
    r1, residual1, dual1 = matched_residual_sq(first["regular_form"], first["metric"], [q(x) for x in seed])
    r2, residual2, dual2 = matched_residual_sq(second["regular_form"], second["metric"], [q(x) for x in seed])
    form1 = dot([q(x) for x in seed], first["action_column"])
    form2 = dot([q(x) for x in seed], second["action_column"])
    if first["word_norm_sq"] != second["word_norm_sq"] or form1 != form2 or r1 != r2:
        raise AssertionError("control failed to preserve scalar input data")
    if first["action_column"] == second["action_column"] or dual1 == dual2:
        raise AssertionError("control failed to separate vector action data")
    return {
        "bath_sectors": sectors,
        "word_norm_sq": [qstr(value) for value in first["word_norm_sq"]],
        "same_physical_Gram": first["metric"] == second["metric"],
        "same_seed_base_form": qstr(form1),
        "same_generalized_rayleigh": qstr(r1),
        "same_reference_shape_data": True,
        "baseline_action_column": [qstr(value) for value in first["action_column"]],
        "rotated_action_column": [qstr(value) for value in second["action_column"]],
        "action_columns_differ": first["action_column"] != second["action_column"],
        "baseline_matched_M_dual_residual_sq": qstr(dual1),
        "rotated_matched_M_dual_residual_sq": qstr(dual2),
        "matched_residuals_differ": residual1 != residual2 and dual1 != dual2,
        "finite_algebraic_control_only": True,
    }


def vector_tail_certificate(
    *, contraction_upper: Any, resolved_block_action_norm_sum: Any,
    unresolved_block_action_norm_sum_upper: Any, native_block_vectors_ref: str | None,
    complete_native_tail_ref: str | None,
) -> dict[str, Any]:
    contraction = q(contraction_upper)
    resolved = q(resolved_block_action_norm_sum)
    tail = q(unresolved_block_action_norm_sum_upper)
    if not 0 <= contraction < 1 or min(resolved, tail) < 0:
        raise CertificateError("contraction and block-action sums have invalid signs")
    if not native_block_vectors_ref:
        raise CertificateError("scalar word norms do not identify vector block actions W_n G^n phi")
    if not complete_native_tail_ref:
        raise CertificateError("a complete native sum of unresolved block-action norms is required")
    return {
        "inverse_adjoint_norm_upper": qstr(1 / (1 - contraction)),
        "resolved_column_norm_upper": qstr(resolved / (1 - contraction)),
        "unresolved_column_tail_upper": qstr(tail / (1 - contraction)),
        "native_block_vectors_ref": native_block_vectors_ref,
        "complete_native_tail_ref": complete_native_tail_ref,
        "complete_action_column_certified": True,
    }


def demo() -> dict[str, Any]:
    control = same_scalar_different_column_control()
    try:
        vector_tail_certificate(
            contraction_upper="3/8", resolved_block_action_norm_sum=1,
            unresolved_block_action_norm_sum_upper="1/100",
            native_block_vectors_ref=None, complete_native_tail_ref=None,
        )
    except CertificateError as exc:
        native_failure = str(exc)
    else:
        raise AssertionError("scalar-only native packet unexpectedly passed")
    positive = vector_tail_certificate(
        contraction_upper="3/8", resolved_block_action_norm_sum="1/2",
        unresolved_block_action_norm_sum_upper="1/64",
        native_block_vectors_ref="control#Wn-gn-vectors",
        complete_native_tail_ref="control#sum-norm-tail",
    )
    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "exact_component_formula": "P_k R0 phi=P_k A phi+sum_(n>=k) P_k (G*)^(n-k) W_n G^n phi",
        "bath_number_roles": {
            "G": "raises exactly one",
            "W": "preserves bath number",
            "Gstar": "lowers exactly one",
            "K170_word_orthogonality_determines_Gram": True,
            "K170_word_orthogonality_diagonalizes_action_column": False,
        },
        "identifiability_control": control,
        "scalar_only_native_release_failure": native_failure,
        "vector_tail_positive_control": positive,
        "native_release_audit": {
            "K170_scalar_word_norms_serialized": True,
            "K170_reference_shape_parity_serialized": True,
            "K156_limiting_normal_ordered_W_exists": True,
            "native_vectors_W_n_Gn_phi_serialized": False,
            "complete_sum_norm_tail_for_those_vectors_serialized": False,
            "complete_R0_action_column_serialized": False,
            "complete_Rref_form_dual_residual_serialized": False,
            "positive_complete_M_orthogonal_complement_or_flux_floor_serialized": False,
            "native_K152_interval_emitted": False,
        },
        "physical_or_source_selection": False,
        "Born_prediction_or_confirmation_credit": False,
        "canon_paper_release_or_public_posture_move": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()
    if not args.demo:
        parser.error("use --demo")
    print(json.dumps(demo(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
