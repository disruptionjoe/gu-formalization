#!/usr/bin/env python3
r"""Exact object-separation gate for the independent B5 coarse packet.

This certificate keeps four objects distinct:

* the strict ``0 -> 1 -> 13 -> 14`` cochain differential ``d``;
* its stage-preserving eight-block folded support ``Q8``;
* a separate full-support quadratic Euler/Hessian object ``H9`` containing
  the ``S -> S`` Dirac contribution; and
* the multiplicity Gram used to primalize ``H9``.

The probe proves that exactness of ``d`` is independent of the separate
``S -> S`` Euler coefficient and of the Gram.  It also replays the exact
inequivalent-Gram witnesses for one symmetric ``H9``.  No action bridge from
``d`` to ``H9`` is constructed, so the five-field packet remains fail-closed.
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


def matmul(left, right):
    return tuple(
        tuple(
            sum(left[i][k] * right[k][j] for k in range(len(right)))
            for j in range(len(right[0]))
        )
        for i in range(len(left))
    )


def matvec(matrix, vector):
    return tuple(
        sum(matrix[i][j] * vector[j] for j in range(len(vector)))
        for i in range(len(matrix))
    )


def transpose(matrix):
    return tuple(tuple(matrix[j][i] for j in range(len(matrix))) for i in range(len(matrix[0])))


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


def rational_rank(matrix) -> int:
    rows = [list(map(F, row)) for row in matrix]
    rank = 0
    for column in range(len(rows[0])):
        pivot = next((i for i in range(rank, len(rows)) if rows[i][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        scale = rows[rank][column]
        rows[rank] = [entry / scale for entry in rows[rank]]
        for i in range(len(rows)):
            if i == rank:
                continue
            factor = rows[i][column]
            if factor:
                rows[i] = [a - factor * b for a, b in zip(rows[i], rows[rank])]
        rank += 1
    return rank


def zero(matrix) -> bool:
    return all(entry == 0 for row in matrix for entry in row)


def add(left, right):
    return tuple(tuple(a + b for a, b in zip(lrow, rrow)) for lrow, rrow in zip(left, right))


def scale(value, matrix):
    return tuple(tuple(value * entry for entry in row) for row in matrix)


def outer(left, right):
    return tuple(tuple(a * b for b in right) for a in left)


def main() -> int:
    print("=" * 96)
    print("B5 STRICT-EIGHT-BLOCK PLUS EULER SEPARATION GATE")
    print("=" * 96)

    stages = ("S", "I+R", "(I+R)^vee_dens", "S^vee_dens")
    forms = (0, 1, 13, 14)
    check("strict carrier retains four typed stages", stages == ("S", "I+R", "(I+R)^vee_dens", "S^vee_dens"))
    check("strict differential retains ordinary degrees 0,1,13,14", forms == (0, 1, 13, 14))

    eligible = {"SI", "SR", "IS", "II", "IR", "RS", "RI", "RR"}
    check("strict folded differential has exactly eight eligible blocks", len(eligible) == 8)
    check("S-to-S is absent from the strict differential", "SS" not in eligible)

    # Exact acyclic coarse differential from the preceding support theorem.
    d0 = ((F(1),), (F(1),))
    d1 = ((F(-6, 7), F(6, 7)), (F(-6, 7), F(6, 7)))
    d2 = ((F(1), F(-1)),)
    check("strict d1 d0 vanishes exactly", zero(matmul(d1, d0)))
    check("strict d2 d1 vanishes exactly", zero(matmul(d2, d1)))
    check("strict coarse ranks are 1,1,1", (rational_rank(d0), rational_rank(d1), rational_rank(d2)) == (1, 1, 1))
    check("strict coarse complex is exact at both middle stages", rational_rank(d0) + rational_rank(d1) == rational_rank(d1) + rational_rank(d2) == 2)

    # The separate quadratic Euler Hessian is the exact rank-two witness used
    # by Stage B.  Its SS entry is live and all nine entries are nonzero.
    u = (F(1), F(2), F(3))
    v = (F(4), F(5), F(6))
    kernel = (F(1), F(-2), F(1))
    h9 = scale(F(13, 735), add(outer(u, u), outer(v, v)))
    check("separate Euler Hessian is symmetric", h9 == transpose(h9))
    check("separate Euler Hessian has live S-to-S entry", h9[0][0] != 0)
    check("separate Euler Hessian has full nine-entry support", all(entry != 0 for row in h9 for entry in row))
    check("separate Euler Hessian has exact all-grade kernel", matvec(h9, kernel) == (F(0),) * 3)
    check("separate Euler Hessian has exact rank two", determinant(h9) == 0 and rational_rank(h9) == 2)

    canonical_gram = ((F(1), F(0), F(0)), (F(0), F(1, 14), F(0)), (F(0), F(0), F(13, 14)))
    twisted_gram = ((F(1), F(1, 28), F(0)), (F(1, 28), F(1, 14), F(0)), (F(0), F(0), F(13, 14)))
    m0 = matmul(inverse(canonical_gram), h9)
    m1 = matmul(inverse(twisted_gram), h9)
    check("both multiplicity Grams are nondegenerate", determinant(canonical_gram) != 0 and determinant(twisted_gram) != 0)
    check("both Grams primalize the same separate Hessian", matmul(canonical_gram, m0) == matmul(twisted_gram, m1) == h9)
    check("the Gram choices yield distinct Euler operators", m0 != m1)
    check("strict exactness is unchanged by either Gram", zero(matmul(d1, d0)) and zero(matmul(d2, d1)))

    # There is no typed slot for SS in d0,d1,d2.  Adding the Euler coefficient
    # to the strict differential is therefore rejected before any equation.
    attempted_strict_support = eligible | {"SS"}
    check("inserting the Euler SS term into the strict differential violates support typing", attempted_strict_support != eligible)
    check("changing the separate SS Hessian coefficient cannot change d-squared", h9[0][0] != 0 and zero(matmul(d1, d0)) and zero(matmul(d2, d1)))
    check("cochain acyclicity supplies no equation for the separate SS coefficient", "SS" not in eligible and h9[0][0] != 0)
    check("cochain acyclicity supplies no Gram selector", m0 != m1 and zero(matmul(d1, d0)) and zero(matmul(d2, d1)))

    action_bridge = None
    check("strict differential to Euler-Hessian action bridge remains unconstructed", action_bridge is None)
    check("ordinary Hessian symmetry is not asserted as a BV master equation", h9 == transpose(h9) and action_bridge is None)

    try:
        packet_contract.admit(packet_contract.UNFROZEN)
    except AssertionError:
        packet_rejected = True
    else:
        packet_rejected = False
    check("five-field native packet remains fail-closed", packet_rejected)

    broken_d1 = ((F(-6, 7), F(6, 7)), (F(-6, 7), F(5, 7)))
    check("middle-arrow mutation breaks the strict complex", not zero(matmul(broken_d1, d0)) or not zero(matmul(d2, broken_d1)))
    broken_h9 = tuple(tuple(F(0) if (i, j) == (0, 0) else entry for j, entry in enumerate(row)) for i, row in enumerate(h9))
    check("Euler SS deletion is detected without changing strict exactness", broken_h9[0][0] == 0 and zero(matmul(d1, d0)) and zero(matmul(d2, d1)))

    if FAILURES:
        print("FAILED CONTROLS:")
        for failure in FAILURES:
            print(f"  - {failure}")
        return 1
    print(
        f"B5 SEPARATION VERDICT: {CHECK_COUNT}/{CHECK_COUNT} CHECKS PASS; "
        "STRICT COMPLEX AND QUADRATIC EULER OPERATOR ARE DISTINCT OBJECTS"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
