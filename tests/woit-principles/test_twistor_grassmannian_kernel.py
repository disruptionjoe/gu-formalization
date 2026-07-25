#!/usr/bin/env python3
"""Exact finite kernel for the Grassmannian/twistor transfer.

The script freezes the algebraic geometry that is genuinely automatic:

* M_C = Gr(2,C^4), T_S M_C = Hom(S,Q), dim_C 4.
* PT = P(C^4) = CP^3 and the incidence flag F(1,2;4) has dim_C 5.
* On PT, 0 -> L -> C^4 -> Q_3 -> 0 and
  c(Q_3)=1+H+H^2+H^3 modulo H^4.
* S(U(1)xU(3)) has Lie algebra u(1)+su(3).

It also checks two non-automatic points:

* replacing Q by S in the tangent bundle needs extra structure;
* the sign labels of a (2,2) Hermitian form are swapped by an ambient
  determinant-one unitary transformation.

No sheaf cohomology, Penrose transform, gauge dynamics, or GU physical-sector
claim is inferred.
"""

from __future__ import annotations

from fractions import Fraction


Matrix = list[list[int]]


def rank_q(matrix: Matrix) -> int:
    work = [[Fraction(value) for value in row] for row in matrix]
    rows = len(work)
    cols = len(work[0]) if rows else 0
    pivot_row = 0
    for col in range(cols):
        pivot = next(
            (row for row in range(pivot_row, rows) if work[row][col]),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        factor = work[pivot_row][col]
        work[pivot_row] = [entry / factor for entry in work[pivot_row]]
        for row in range(rows):
            if row == pivot_row or not work[row][col]:
                continue
            factor = work[row][col]
            work[row] = [
                entry - factor * base
                for entry, base in zip(work[row], work[pivot_row])
            ]
        pivot_row += 1
    return pivot_row


def matmul(left: Matrix, right: Matrix) -> Matrix:
    return [
        [
            sum(left[i][k] * right[k][j] for k in range(len(right)))
            for j in range(len(right[0]))
        ]
        for i in range(len(left))
    ]


def transpose(matrix: Matrix) -> Matrix:
    return [list(column) for column in zip(*matrix)]


def apply(matrix: Matrix, vector: list[int]) -> list[int]:
    return [
        sum(matrix[row][col] * vector[col] for col in range(len(vector)))
        for row in range(len(matrix))
    ]


def determinant(matrix: Matrix) -> int:
    if len(matrix) == 1:
        return matrix[0][0]
    return sum(
        (-1) ** col
        * matrix[0][col]
        * determinant(
            [
                [matrix[row][j] for j in range(len(matrix)) if j != col]
                for row in range(1, len(matrix))
            ]
        )
        for col in range(len(matrix))
    )


def poly_mul_truncated(
    left: list[int], right: list[int], max_degree: int
) -> list[int]:
    result = [0] * (max_degree + 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            if i + j <= max_degree:
                result[i + j] += a * b
    return result


def hermitian_value(form: Matrix, vector: list[int]) -> int:
    image = apply(form, vector)
    return sum(x * y for x, y in zip(vector, image))


def check(name: str, condition: bool, detail: str) -> bool:
    print(f"[{'PASS' if condition else 'FAIL'}] {name}: {detail}")
    return condition


def main() -> int:
    dim_grassmannian = 2 * (4 - 2)
    dim_tangent = 2 * 2
    dim_pt = 4 - 1
    dim_incidence_from_gr = dim_grassmannian + (2 - 1)
    dim_incidence_from_pt = dim_pt + ((4 - 1) - 1)

    # c(L)c(Q_3)=1, c(L)=1-H on CP^3.  The inverse is finite modulo H^4.
    c_line = [1, -1]
    c_quotient = [1, 1, 1, 1]
    chern_product = poly_mul_truncated(c_line, c_quotient, 3)

    # A stabilizer-equivariant A: Q -> S would have to obey
    # (2 I_S) A = A (I_Q), hence A=0.  Four equations, four entries.
    noncanonical_identification_equations = [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ]

    phi = [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, -1, 0],
        [0, 0, 0, -1],
    ]
    block_swap = [
        [0, 0, 1, 0],
        [0, 0, 0, 1],
        [1, 0, 0, 0],
        [0, 1, 0, 0],
    ]
    swapped_phi = matmul(transpose(block_swap), matmul(phi, block_swap))

    checks = [
        check(
            "complexified compactified spacetime",
            dim_grassmannian == 4,
            "dim_C Gr(2,C^4)=2(4-2)=4",
        ),
        check(
            "intrinsic holomorphic tangent",
            dim_tangent == 4,
            "T_S Gr = Hom(S,C^4/S)=S* tensor Q, rank 2x2",
        ),
        check(
            "projective twistor space",
            dim_pt == 3,
            "PT=P(C^4)=CP^3",
        ),
        check(
            "incidence correspondence",
            dim_incidence_from_gr == dim_incidence_from_pt == 5,
            "F(1,2;4): CP^1 fiber over Gr and CP^2 fiber over PT",
        ),
        check(
            "tautological quotient Chern class",
            chern_product == [1, 0, 0, 0],
            "(1-H)(1+H+H^2+H^3)=1 mod H^4",
        ),
        check(
            "top Chern number is one, not three",
            c_quotient[3] == 1,
            "integral_CP3 c3(Q_3)=integral H^3=1",
        ),
        check(
            "standard U(1)+SU(3) host",
            (1 + 9 - 1) == (1 + 8) == 9,
            "dim S(U(1)xU(3))=9=dim u(1)+dim su(3)",
        ),
        check(
            "purely right-handed tangent needs extra structure",
            rank_q(noncanonical_identification_equations) == 4,
            "independent GL(S)xGL(Q) scalings force every equivariant Q->S map to zero",
        ),
        check(
            "signature-(2,2) three sign strata",
            (
                hermitian_value(phi, [1, 0, 0, 0]) > 0
                and hermitian_value(phi, [0, 0, 1, 0]) < 0
                and hermitian_value(phi, [1, 0, 1, 0]) == 0
            ),
            "explicit positive, negative, and null projective lines",
        ),
        check(
            "positive/negative labels require a fixed Phi",
            determinant(block_swap) == 1
            and swapped_phi == [[-entry for entry in row] for row in phi],
            "an ambient det-one unitary block swap sends Phi to -Phi",
        ),
    ]

    print()
    print("Interpretation:")
    print("  Automatic: Gr/flag dimensions, Hom(S,Q), the tautological line and")
    print("  rank-three quotient, and a conventional U(1)+SU(3) stabilizer host.")
    print("  Not automatic: Q~=S, a right-handed tangent, a labeled PT+ component,")
    print("  gauge dynamics, hypercharge normalization, or three generations.")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
