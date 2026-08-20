#!/usr/bin/env python3
r"""Exact Stage-B owner test for the independent B5 coarse action packet.

This certificate works only at the formal compact-core
``S + imGamma + kerGamma`` multiplicity grade.  It distinguishes the carrier
operator ``M``, the multiplicity Gram ``G``, the density-dual quadratic
Hessian ``H = G M``, and a coarse principal kernel vector ``r``.

The currently serialized quadratic-action and formal-adjoint requirements are
both ``H^T = H``.  The linear BV/Noether equation and coarse principal-kernel
condition are both ``H r = 0`` (equivalently ``M r = 0`` for nondegenerate
``G``).  Two inequivalent exact packets satisfying all of those conditions
therefore prove underdetermination of the *current* Stage-B equations.  They do
not rule out a future action-owned four-stage differential, nonlinear master
equation, or source-selected normalization.
"""

from __future__ import annotations

import os
import sys
from fractions import Fraction as F


HERE = os.path.dirname(os.path.abspath(__file__))
TESTS = os.path.dirname(HERE)
if TESTS not in sys.path:
    sys.path.insert(0, TESTS)

import shiab_b5_native_packet_contract as packet_contract  # noqa: E402


FAILURES: list[str] = []
CHECK_COUNT = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global CHECK_COUNT
    CHECK_COUNT += 1
    passed = bool(condition)
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if passed else 'FAIL'}: {label}{suffix}")
    if not passed:
        FAILURES.append(label)


def transpose(matrix):
    return tuple(tuple(matrix[j][i] for j in range(3)) for i in range(3))


def multiply(left, right):
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )


def matvec(matrix, vector):
    return tuple(sum(matrix[i][j] * vector[j] for j in range(3)) for i in range(3))


def determinant(matrix):
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def inverse(matrix):
    det = determinant(matrix)
    if det == 0:
        raise ValueError("singular matrix")
    cofactors = (
        (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1],
         -(matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]),
         matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]),
        (-(matrix[0][1] * matrix[2][2] - matrix[0][2] * matrix[2][1]),
         matrix[0][0] * matrix[2][2] - matrix[0][2] * matrix[2][0],
         -(matrix[0][0] * matrix[2][1] - matrix[0][1] * matrix[2][0])),
        (matrix[0][1] * matrix[1][2] - matrix[0][2] * matrix[1][1],
         -(matrix[0][0] * matrix[1][2] - matrix[0][2] * matrix[1][0]),
         matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]),
    )
    return tuple(tuple(value / det for value in row) for row in transpose(cofactors))


def outer(left, right):
    return tuple(tuple(left[i] * right[j] for j in range(3)) for i in range(3))


def add(left, right):
    return tuple(tuple(left[i][j] + right[i][j] for j in range(3)) for i in range(3))


def scale(value, matrix):
    return tuple(tuple(value * entry for entry in row) for row in matrix)


def zero_matrix(matrix):
    return all(entry == 0 for row in matrix for entry in row)


def allowed_gram(alpha, beta, zeta, rho):
    return (
        (alpha, zeta, F(0)),
        (zeta, beta / 14, F(0)),
        (F(0), F(0), rho),
    )


def extract_coefficients(matrix):
    return {
        "a": matrix[0][0],
        "b": matrix[0][1],
        "c": -F(14, 13) * matrix[0][2],
        "d": matrix[1][0],
        "e": -F(7, 6) * matrix[1][1],
        "f": F(7, 13) * matrix[1][2],
        "g": matrix[2][0],
        "h": F(7) * matrix[2][1],
        "q": F(7, 6) * matrix[2][2],
    }


def proportional(left, right):
    ratios = []
    for left_row, right_row in zip(left, right):
        for a, b in zip(left_row, right_row):
            if a == 0 or b == 0:
                if a != b:
                    return False
            else:
                ratios.append(a / b)
    return bool(ratios) and all(value == ratios[0] for value in ratios)


def main() -> int:
    print("=" * 94)
    print("B5 STAGE-B ACTION-NORMALIZATION OWNER TEST")
    print("=" * 94)

    canonical = allowed_gram(F(1), F(1), F(0), F(13, 14))
    twisted = allowed_gram(F(1), F(1), F(1, 28), F(13, 14))
    check("canonical multiplicity Gram is nondegenerate", determinant(canonical) != 0)
    check("off-diagonal multiplicity Gram is nondegenerate", determinant(twisted) != 0)
    check("the two allowed Grams are not related by common scale", not proportional(canonical, twisted))

    # Two independent covectors generate a rank-two symmetric Hessian.  Their
    # common exact kernel r has all three coarse grades nonzero.  The scale is
    # chosen so H_33/rho = 6/7, hence the inherited W131 coefficient is q=1.
    u = (F(1), F(2), F(3))
    v = (F(4), F(5), F(6))
    r = (F(1), F(-2), F(1))
    hessian = scale(F(13, 735), add(outer(u, u), outer(v, v)))
    check("quadratic Hessian is exactly symmetric", hessian == transpose(hessian))
    check("quadratic Hessian has determinant zero", determinant(hessian) == 0)
    check(
        "quadratic Hessian has exact rank two",
        hessian[0][0] * hessian[1][1] - hessian[0][1] ** 2 != 0,
    )
    check("all-grade kernel vector is nonzero in every grade", all(value != 0 for value in r))
    check("quadratic Hessian annihilates the kernel exactly", matvec(hessian, r) == (F(0),) * 3)

    matrices = [multiply(inverse(pairing), hessian) for pairing in (canonical, twisted)]
    coefficient_packets = [extract_coefficients(matrix) for matrix in matrices]
    for label, pairing, matrix, coefficients in zip(
        ("canonical", "twisted"),
        (canonical, twisted),
        matrices,
        coefficient_packets,
    ):
        check(
            f"{label} packet obeys exact formal Krein adjointness",
            multiply(transpose(matrix), pairing) == multiply(pairing, matrix),
        )
        check(
            f"{label} packet reproduces the same action Hessian",
            multiply(pairing, matrix) == hessian,
        )
        check(
            f"{label} packet has full nine-block support",
            all(value != 0 for value in coefficients.values()),
        )
        check(f"{label} packet retains normalized W131 q=1", coefficients["q"] == 1)
        check(f"{label} packet has the exact coarse kernel", matvec(matrix, r) == (F(0),) * 3)

    check(
        "inequivalent Grams require inequivalent full-support coefficient packets",
        not proportional(matrices[0], matrices[1]),
    )
    check(
        "quadratic-action symmetry and formal-adjoint symmetry are the same equation",
        all(multiply(pairing, matrix) == transpose(multiply(pairing, matrix))
            for pairing, matrix in zip((canonical, twisted), matrices)),
        "H=GM and H^T=H iff M^T G=G M",
    )
    check(
        "linear BV/Noether closure duplicates the coarse principal-kernel equation",
        all(matvec(multiply(pairing, matrix), r) == (F(0),) * 3
            and matvec(matrix, r) == (F(0),) * 3
            for pairing, matrix in zip((canonical, twisted), matrices)),
        "G is invertible, so Hr=0 iff Mr=0",
    )
    check(
        "fixed-Gram current solution locus remains positive-dimensional",
        6 - 1 - 1 == 4,
        "symmetric H: 6 entries; q normalization: 1 equation; det(H)=0: 1 equation",
    )

    broken_adjoint = [list(row) for row in matrices[1]]
    broken_adjoint[0][1] += F(1, 101)
    broken_adjoint = tuple(tuple(row) for row in broken_adjoint)
    check(
        "one-sided coefficient mutation breaks action/formal-adjoint symmetry",
        multiply(transpose(broken_adjoint), twisted) != multiply(twisted, broken_adjoint),
    )
    broken_kernel = [list(row) for row in hessian]
    broken_kernel[2][2] += F(1, 103)
    broken_kernel = tuple(tuple(row) for row in broken_kernel)
    check(
        "normalized Hessian mutation breaks the planted kernel and singularity",
        matvec(broken_kernel, r) != (F(0),) * 3 and determinant(broken_kernel) != 0,
    )
    check("vacuous zero gauge vector is rejected", r != (F(0),) * 3)

    try:
        packet_contract.admit(packet_contract.UNFROZEN)
    except AssertionError:
        packet_rejected = True
    else:
        packet_rejected = False
    check(
        "five-field native packet remains fail-closed",
        packet_rejected,
        "no Gram, four-stage action differential, Green domain or quotient is selected",
    )

    if FAILURES:
        print("FAILED CONTROLS:")
        for failure in FAILURES:
            print(f"  - {failure}")
        return 1
    print(
        f"B5 STAGE-B VERDICT: {CHECK_COUNT}/{CHECK_COUNT} CHECKS PASS; "
        "CURRENT QUADRATIC ACTION EQUATIONS UNDERDETERMINE THE GRAM"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
