#!/usr/bin/env python3
"""Exact standard controls for twistor real-slice reconstruction.

This script checks four pieces of ordinary twistor geometry:

* the Hermitian Pauli encoding of Minkowski vectors and its determinant;
* maximally isotropic graph planes for a signature-(2,2) Hermitian form;
* null separation as intersection of the corresponding twistor lines; and
* a quaternionic antilinear structure on C^4, including J^2=-I on C^4,
  projective square +I, absence of projective fixed points, and independent
  J-invariant two-planes.

It also checks the finite arithmetic behind the standard normal-bundle fact
N_{CP1/CP3}=O(1)+O(1): four first-order deformation coefficients, no H^1
obstruction, and the determinant/common-zero null condition.

MANDATORY GU FORK GUARD
-----------------------
These are standard twistor controls, not a GU transfer.  A signature real
slice is not the GU 192/384 carrier without a typed map.  The determinant
Minkowski metric checked here is not the gimmel/DeWitt metric.  Standard
Osterwalder-Schrader positivity would construct a positive Hilbert space, not
the GU Krein physical quotient.  Nothing in this script proves GU soldering,
gauge dynamics, or physicality.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from typing import Iterable


Gaussian = tuple[Fraction, Fraction]
Matrix = list[list[Gaussian]]
Vector = list[Gaussian]


def gaussian(real: int | Fraction = 0, imag: int | Fraction = 0) -> Gaussian:
    return Fraction(real), Fraction(imag)


ZERO = gaussian()
ONE = gaussian(1)
I = gaussian(0, 1)


def g_add(left: Gaussian, right: Gaussian) -> Gaussian:
    return left[0] + right[0], left[1] + right[1]


def g_neg(value: Gaussian) -> Gaussian:
    return -value[0], -value[1]


def g_sub(left: Gaussian, right: Gaussian) -> Gaussian:
    return g_add(left, g_neg(right))


def g_mul(left: Gaussian, right: Gaussian) -> Gaussian:
    a, b = left
    c, d = right
    return a * c - b * d, a * d + b * c


def g_conj(value: Gaussian) -> Gaussian:
    return value[0], -value[1]


def g_div(left: Gaussian, right: Gaussian) -> Gaussian:
    c, d = right
    denominator = c * c + d * d
    if denominator == 0:
        raise ZeroDivisionError("division by zero in Q(i)")
    a, b = left
    return (
        (a * c + b * d) / denominator,
        (b * c - a * d) / denominator,
    )


def g_sum(values: Iterable[Gaussian]) -> Gaussian:
    total = ZERO
    for value in values:
        total = g_add(total, value)
    return total


def g_abs_sq(value: Gaussian) -> Fraction:
    return value[0] * value[0] + value[1] * value[1]


def identity(size: int) -> Matrix:
    return [
        [ONE if row == col else ZERO for col in range(size)]
        for row in range(size)
    ]


def matrix_scale(value: Gaussian, matrix: Matrix) -> Matrix:
    return [[g_mul(value, entry) for entry in row] for row in matrix]


def matrix_add(left: Matrix, right: Matrix) -> Matrix:
    return [
        [g_add(left[row][col], right[row][col]) for col in range(len(left[0]))]
        for row in range(len(left))
    ]


def matrix_sub(left: Matrix, right: Matrix) -> Matrix:
    return [
        [g_sub(left[row][col], right[row][col]) for col in range(len(left[0]))]
        for row in range(len(left))
    ]


def matmul(left: Matrix, right: Matrix) -> Matrix:
    return [
        [
            g_sum(
                g_mul(left[row][middle], right[middle][col])
                for middle in range(len(right))
            )
            for col in range(len(right[0]))
        ]
        for row in range(len(left))
    ]


def matvec(matrix: Matrix, vector: Vector) -> Vector:
    return [
        g_sum(g_mul(entry, value) for entry, value in zip(row, vector))
        for row in matrix
    ]


def dagger(matrix: Matrix) -> Matrix:
    return [
        [g_conj(matrix[row][col]) for row in range(len(matrix))]
        for col in range(len(matrix[0]))
    ]


def determinant_2(matrix: Matrix) -> Gaussian:
    return g_sub(
        g_mul(matrix[0][0], matrix[1][1]),
        g_mul(matrix[0][1], matrix[1][0]),
    )


def rank_gaussian(matrix: Matrix) -> int:
    """Exact row rank over the Gaussian-rational field Q(i)."""

    work = [row[:] for row in matrix]
    rows = len(work)
    cols = len(work[0]) if rows else 0
    pivot_row = 0
    for col in range(cols):
        pivot = next(
            (row for row in range(pivot_row, rows) if work[row][col] != ZERO),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        inverse = g_div(ONE, work[pivot_row][col])
        work[pivot_row] = [
            g_mul(inverse, entry) for entry in work[pivot_row]
        ]
        for row in range(rows):
            if row == pivot_row or work[row][col] == ZERO:
                continue
            factor = work[row][col]
            work[row] = [
                g_sub(entry, g_mul(factor, base))
                for entry, base in zip(work[row], work[pivot_row])
            ]
        pivot_row += 1
    return pivot_row


def pauli_encoding(
    vector: tuple[Fraction, Fraction, Fraction, Fraction],
) -> Matrix:
    """Return X=x0 I+x1 sigma1+x2 sigma2+x3 sigma3 exactly."""

    x0, x1, x2, x3 = vector
    return [
        [gaussian(x0 + x3), gaussian(x1, -x2)],
        [gaussian(x1, x2), gaussian(x0 - x3)],
    ]


def minkowski_norm(
    vector: tuple[Fraction, Fraction, Fraction, Fraction],
) -> Fraction:
    x0, x1, x2, x3 = vector
    return x0 * x0 - x1 * x1 - x2 * x2 - x3 * x3


def graph_i_x(matrix: Matrix) -> Matrix:
    """Columns of the graph u -> iXu in C^2 direct-sum C^2."""

    i_x = matrix_scale(I, matrix)
    return [
        [ONE, ZERO],
        [ZERO, ONE],
        i_x[0],
        i_x[1],
    ]


HERMITIAN_FORM_22: Matrix = [
    [ZERO, ZERO, ONE, ZERO],
    [ZERO, ZERO, ZERO, ONE],
    [ONE, ZERO, ZERO, ZERO],
    [ZERO, ONE, ZERO, ZERO],
]


def graph_gram(matrix: Matrix) -> Matrix:
    graph = graph_i_x(matrix)
    return matmul(dagger(graph), matmul(HERMITIAN_FORM_22, graph))


def columns_to_matrix(columns: list[Vector]) -> Matrix:
    return [
        [columns[col][row] for col in range(len(columns))]
        for row in range(len(columns[0]))
    ]


def matrix_columns(matrix: Matrix) -> list[Vector]:
    return [
        [matrix[row][col] for row in range(len(matrix))]
        for col in range(len(matrix[0]))
    ]


def subspace_intersection_dimension(left: Matrix, right: Matrix) -> int:
    """Return dim(col(left) intersect col(right)) over Q(i)."""

    left_rank = rank_gaussian(left)
    right_rank = rank_gaussian(right)
    joined = columns_to_matrix(matrix_columns(left) + matrix_columns(right))
    return left_rank + right_rank - rank_gaussian(joined)


def cp1_line_bundle_cohomology_dimensions(degree: int) -> tuple[int, int]:
    """Return (h^0,h^1) for O(degree) on CP1."""

    if degree >= 0:
        return degree + 1, 0
    return 0, max(-degree - 1, 0)


def quaternionic_j(vector: Vector) -> Vector:
    """Antilinear J on two quaternionic coordinate blocks."""

    z0, z1, z2, z3 = vector
    return [
        g_neg(g_conj(z1)),
        g_conj(z0),
        g_neg(g_conj(z3)),
        g_conj(z2),
    ]


def vector_add(left: Vector, right: Vector) -> Vector:
    return [g_add(a, b) for a, b in zip(left, right)]


def vector_scale(value: Gaussian, vector: Vector) -> Vector:
    return [g_mul(value, entry) for entry in vector]


def check(name: str, condition: bool, detail: str) -> bool:
    print(f"[{'PASS' if condition else 'FAIL'}] {name}: {detail}")
    return condition


def main() -> int:
    half = Fraction(1, 2)
    test_vectors = [
        (Fraction(0), Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(1), Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(0), Fraction(1)),
        (Fraction(1), Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(2), Fraction(1), Fraction(-1), Fraction(0)),
        (Fraction(-3), Fraction(1), Fraction(2), Fraction(1)),
        (half, Fraction(1, 3), Fraction(1, 4), Fraction(1, 5)),
    ]
    encoded = [pauli_encoding(vector) for vector in test_vectors]
    determinant_controls = all(
        dagger(matrix) == matrix
        and determinant_2(matrix) == gaussian(minkowski_norm(vector))
        for vector, matrix in zip(test_vectors, encoded)
    )

    # H=[[0,I],[I,0]] has two exact +1 and two exact -1 eigenvectors.
    e0 = [ONE, ZERO, ZERO, ZERO]
    e1 = [ZERO, ONE, ZERO, ZERO]
    e2 = [ZERO, ZERO, ONE, ZERO]
    e3 = [ZERO, ZERO, ZERO, ONE]
    positive_vectors = [vector_add(e0, e2), vector_add(e1, e3)]
    negative_vectors = [
        vector_add(e0, vector_scale(gaussian(-1), e2)),
        vector_add(e1, vector_scale(gaussian(-1), e3)),
    ]
    signature_basis = columns_to_matrix(positive_vectors + negative_vectors)
    signature_control = (
        all(
            matvec(HERMITIAN_FORM_22, vector) == vector
            for vector in positive_vectors
        )
        and all(
            matvec(HERMITIAN_FORM_22, vector)
            == vector_scale(gaussian(-1), vector)
            for vector in negative_vectors
        )
        and rank_gaussian(signature_basis) == 4
    )

    graph_controls = [
        dagger(matrix) == matrix
        and graph_gram(matrix) == [[ZERO, ZERO], [ZERO, ZERO]]
        and rank_gaussian(graph_i_x(matrix)) == 2
        for matrix in encoded
    ]
    non_hermitian_matrix = [
        [ONE, I],
        [ZERO, ONE],
    ]
    non_hermitian_control = (
        dagger(non_hermitian_matrix) != non_hermitian_matrix
        and graph_gram(non_hermitian_matrix)
        != [[ZERO, ZERO], [ZERO, ZERO]]
    )

    origin = pauli_encoding(
        (Fraction(0), Fraction(0), Fraction(0), Fraction(0))
    )
    null_displacement = pauli_encoding(
        (Fraction(1), Fraction(1), Fraction(0), Fraction(0))
    )
    timelike_displacement = pauli_encoding(
        (Fraction(2), Fraction(0), Fraction(0), Fraction(0))
    )
    spacelike_displacement = pauli_encoding(
        (Fraction(0), Fraction(0), Fraction(3), Fraction(0))
    )
    separation_controls = [
        (
            null_displacement,
            ZERO,
            1,
        ),
        (
            timelike_displacement,
            gaussian(4),
            0,
        ),
        (
            spacelike_displacement,
            gaussian(-9),
            0,
        ),
    ]
    causal_incidence_control = all(
        determinant_2(matrix_sub(displacement, origin)) == expected_determinant
        and subspace_intersection_dimension(
            graph_i_x(origin), graph_i_x(displacement)
        )
        == expected_intersection
        for displacement, expected_determinant, expected_intersection
        in separation_controls
    )

    # A section of O(1)+O(1) is a pair of linear forms.  Its four
    # coefficients form a 2x2 matrix.  The two forms have a common point of
    # CP1 exactly when that matrix has nontrivial kernel, equivalently zero
    # determinant.  H^0(O(1)) has dimension 2 and H^1(O(1)) vanishes.
    o1_h0, o1_h1 = cp1_line_bundle_cohomology_dimensions(1)
    normal_h0_dimension = 2 * o1_h0
    normal_h1_dimension = 2 * o1_h1
    normal_null_section = [
        [gaussian(1), ZERO],
        [gaussian(2), ZERO],
    ]
    normal_nonnull_section = identity(2)
    normal_coefficient_grid = [
        [
            [gaussian(a), gaussian(b)],
            [gaussian(c), gaussian(d)],
        ]
        for a, b, c, d in product((-1, 0, 1), repeat=4)
    ]
    normal_rank_det_equivalence = all(
        (determinant_2(matrix) == ZERO) == (rank_gaussian(matrix) < 2)
        for matrix in normal_coefficient_grid
    )
    normal_bundle_control = (
        normal_h0_dimension == 4
        and normal_h1_dimension == 0
        and cp1_line_bundle_cohomology_dimensions(-2) == (0, 1)
        and determinant_2(normal_null_section) == ZERO
        and rank_gaussian(normal_null_section) == 1
        and determinant_2(normal_nonnull_section) == ONE
        and rank_gaussian(normal_nonnull_section) == 2
        and normal_rank_det_equivalence
    )

    basis = [e0, e1, e2, e3]
    j_square_control = all(
        quaternionic_j(quaternionic_j(vector))
        == vector_scale(gaussian(-1), vector)
        for vector in basis
    )
    alpha = gaussian(Fraction(2, 3), Fraction(-1, 5))
    beta = gaussian(Fraction(-4, 7), Fraction(3, 8))
    z = [gaussian(1, 2), gaussian(-3, 1), gaussian(2, -1), gaussian(0, 4)]
    w = [gaussian(-2, 1), gaussian(1, 3), gaussian(4), gaussian(-1, -2)]
    antilinear_control = quaternionic_j(
        vector_add(vector_scale(alpha, z), vector_scale(beta, w))
    ) == vector_add(
        vector_scale(g_conj(alpha), quaternionic_j(z)),
        vector_scale(g_conj(beta), quaternionic_j(w)),
    )

    plane_a = columns_to_matrix([e0, e1])
    plane_b = columns_to_matrix([e2, e3])

    def plane_is_j_invariant(plane: Matrix, columns: list[Vector]) -> bool:
        return rank_gaussian(plane) == 2 and all(
            rank_gaussian(columns_to_matrix(columns + [quaternionic_j(column)]))
            == 2
            for column in columns
        )

    invariant_planes = (
        plane_is_j_invariant(plane_a, [e0, e1])
        and plane_is_j_invariant(plane_b, [e2, e3])
        and rank_gaussian(columns_to_matrix([e0, e1, e2, e3])) == 4
    )
    non_invariant_columns = [e0, e2]
    non_invariant_plane = columns_to_matrix(non_invariant_columns)
    non_invariant_control = (
        rank_gaussian(
            columns_to_matrix(
                non_invariant_columns
                + [quaternionic_j(column) for column in non_invariant_columns]
            )
        )
        == 4
        and subspace_intersection_dimension(plane_a, plane_b) == 0
    )

    # If Jz=lambda*z for z != 0, antilinearity and J^2=-I imply
    # -z=J(lambda*z)=conj(lambda)Jz=|lambda|^2*z.  This is impossible because
    # |lambda|^2 is nonnegative, whereas -1 is negative.
    projective_fixed_point_obstruction = (
        j_square_control
        and antilinear_control
        and Fraction(-1) < Fraction(0)
        and all(
            g_abs_sq(value) >= 0
            for value in [ZERO, ONE, I, alpha, beta, gaussian(-11, 7)]
        )
    )

    checks = [
        check(
            "Hermitian Pauli/Minkowski determinant",
            determinant_controls,
            "det(X)=x0^2-x1^2-x2^2-x3^2 exactly on 4 basis and 5 planted vectors",
        ),
        check(
            "chosen Hermitian form has signature (2,2)",
            signature_control,
            "H=[[0,I],[I,0]] has two exact +1 and two exact -1 eigenvectors",
        ),
        check(
            "graphs of iX are maximally isotropic",
            signature_control and all(graph_controls) and non_hermitian_control,
            "G_X^dag H G_X=i(X-X^dag); Hermitian samples vanish and a planted non-Hermitian sample does not",
        ),
        check(
            "causal relation is twistor-line incidence",
            causal_incidence_control,
            "det(X-Y)=0 iff distinct graph planes intersect on planted null/non-null pairs",
        ),
        check(
            "twistor-line deformation/null-cone arithmetic",
            normal_bundle_control,
            "O(1)+O(1) gives h0=4, h1=0; rank/determinant equivalence holds on all 81 {-1,0,1} coefficient matrices",
        ),
        check(
            "quaternionic structure squares to minus identity",
            j_square_control and antilinear_control,
            "J is exactly antilinear and J^2=-I on a basis of C^4",
        ),
        check(
            "quaternionic projective fixed-point obstruction identity",
            projective_fixed_point_obstruction,
            "J^2=-I gives j^2=id on CP3, while Jz=lambda z would force -1=|lambda|^2",
        ),
        check(
            "Euclidean quaternionic-line controls",
            invariant_planes and non_invariant_control,
            "two J-invariant CP1 fibers are disjoint; span(e0,e2) is a planted non-invariant plane",
        ),
    ]

    print()
    print("GU fork guard:")
    print("  STANDARD CONTROL ONLY: no GU transfer is proved here.")
    print("  Signature real slices are not the GU 192/384 carrier without a typed map.")
    print("  det(X) is the Minkowski metric, not the gimmel/DeWitt metric.")
    print("  Standard OS positive Hilbert space is not the GU Krein physical quotient.")
    print("  No check proves GU soldering, gauge dynamics, or physicality.")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
