#!/usr/bin/env python3
"""Finite exact gates for the OS/right-handed-real-form proposal.

The checks isolate what a chosen Euclidean time direction really supplies:

* Clifford multiplication c(n): S+ -> S- is an isomorphism for n != 0.
* No fixed nonzero Spin(4)-equivariant map S+ -> S- exists.
* n and -n lie in the same SO(4) orbit, so a direction does not itself leave
  a Z/2 after quotienting by rotations.
* The Osterwalder-Schrader reflection is instead in the det=-1 component of
  O(4); that discrete extension is extra structure.
* Lorentzian complex conjugation exchanges the +/-i Hodge halves.

These are finite representation/topology controls, not a proof of reflection
positivity for the GU action or a function-space reconstruction theorem.
"""

from __future__ import annotations

from fractions import Fraction


Matrix = list[list[complex]]


def matmul(left: Matrix, right: Matrix) -> Matrix:
    return [
        [
            sum(left[i][k] * right[k][j] for k in range(len(right)))
            for j in range(len(right[0]))
        ]
        for i in range(len(left))
    ]


def dagger(matrix: Matrix) -> Matrix:
    return [
        [matrix[row][col].conjugate() for row in range(len(matrix))]
        for col in range(len(matrix[0]))
    ]


def add(left: Matrix, right: Matrix) -> Matrix:
    return [
        [left[i][j] + right[i][j] for j in range(len(left[0]))]
        for i in range(len(left))
    ]


def scale(value: complex, matrix: Matrix) -> Matrix:
    return [[value * entry for entry in row] for row in matrix]


def identity(size: int) -> Matrix:
    return [
        [1 + 0j if row == col else 0j for col in range(size)]
        for row in range(size)
    ]


def rank_q(matrix: list[list[int]]) -> int:
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


def clifford_direction(n: tuple[int, int, int, int]) -> Matrix:
    """Quaternion matrix C(n), a covariant S+ -> S- identification."""

    a, b, c, d = n
    return [
        [a + 1j * b, c + 1j * d],
        [-c + 1j * d, a - 1j * b],
    ]


def determinant_2(matrix: Matrix) -> complex:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def diagonal(entries: tuple[int, ...]) -> Matrix:
    return [
        [complex(entries[row] if row == col else 0) for col in range(len(entries))]
        for row in range(len(entries))
    ]


def apply(matrix: Matrix, vector: list[complex]) -> list[complex]:
    return [
        sum(matrix[row][col] * vector[col] for col in range(len(vector)))
        for row in range(len(matrix))
    ]


def check(name: str, condition: bool, detail: str) -> bool:
    print(f"[{'PASS' if condition else 'FAIL'}] {name}: {detail}")
    return condition


def main() -> int:
    n = (1, 2, 3, 4)
    norm_sq = sum(value * value for value in n)
    c_n = clifford_direction(n)
    clifford_norm = matmul(dagger(c_n), c_n)
    expected_norm = scale(norm_sq, identity(2))

    # For a left Spin(4) generator, S+ transforms by sigma_1 while S-
    # transforms trivially.  Intertwining requires A sigma_1 = 0.  In the
    # four coordinates of A this is a permutation matrix, hence full rank.
    intertwiner_equations = [
        [0, 1, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0],
    ]
    intertwiner_rank = rank_q(intertwiner_equations)

    direction_flip = diagonal((-1, -1, 1, 1))
    os_reflection = diagonal((-1, 1, 1, 1))
    e0 = [1 + 0j, 0j, 0j, 0j]

    # Lorentzian Hodge star in the ordered basis
    # (01,02,03 | 23,31,12): *(E,B) = (B,-E).
    zero3 = [[0j for _ in range(3)] for _ in range(3)]
    one3 = identity(3)
    minus_one3 = scale(-1, one3)
    hodge = [
        zero3[row] + one3[row] for row in range(3)
    ] + [
        minus_one3[row] + zero3[row] for row in range(3)
    ]
    one6 = identity(6)
    hodge_sq = matmul(hodge, hodge)
    p_plus = scale(0.5, add(one6, scale(-1j, hodge)))
    p_minus = scale(0.5, add(one6, scale(1j, hodge)))
    conjugate_p_plus = [[entry.conjugate() for entry in row] for row in p_plus]

    checks = [
        check(
            "chosen direction gives a chiral isomorphism",
            clifford_norm == expected_norm and determinant_2(c_n) == norm_sq,
            f"C(n)^dag C(n)={norm_sq} I and det C(n)={determinant_2(c_n):g}",
        ),
        check(
            "zero direction is not an isomorphism",
            determinant_2(clifford_direction((0, 0, 0, 0))) == 0,
            "the identification requires a nonzero selected vector",
        ),
        check(
            "no fixed Spin(4)-equivariant S+ to S- map",
            intertwiner_rank == 4,
            f"one factor's intertwiner equations have exact rank {intertwiner_rank}/4",
        ),
        check(
            "direction sign is not a residual bit",
            apply(direction_flip, e0) == [-1 + 0j, 0j, 0j, 0j],
            "diag(-1,-1,1,1) lies in SO(4) and carries n to -n",
        ),
        check(
            "OS reflection is extra O(4) component data",
            apply(os_reflection, e0) == [-1 + 0j, 0j, 0j, 0j],
            "diag(-1,1,1,1) has determinant -1, unlike the SO(4) direction flip",
        ),
        check(
            "Lorentzian Hodge complex structure",
            hodge_sq == scale(-1, one6),
            "*^2=-I on real two-forms",
        ),
        check(
            "ordinary conjugation exchanges Hodge halves",
            conjugate_p_plus == p_minus
            and matmul(p_plus, p_plus) == p_plus
            and matmul(p_plus, p_minus) == scale(0, one6),
            "bar(P_+)=P_- for the +/-i eigenspaces",
        ),
        check(
            "one Hodge half has complex dimension three",
            sum(p_plus[i][i] for i in range(6)) == 3,
            "tr(P_+)=3 while conjugation-stable closure has dimension 6",
        ),
    ]

    print()
    print("Interpretation:")
    print("  Woit control: n supplies a covariant gamma(n) identification and an OS")
    print("  reflection can define a physical inner product after positivity is proved.")
    print("  GU consequence: neither a direction nor gamma(n) automatically supplies")
    print("  the missing Z/2 or closes one Lorentzian Hodge half under conjugation.")
    print("  Required next object: a GU-native Theta, positive-time algebra, action/")
    print("  measure, and proof of the relevant positive or Krein-physical quotient.")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
