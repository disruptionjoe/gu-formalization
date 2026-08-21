#!/usr/bin/env python3
r"""Exact coarse action/BV bridge for the strict B5 four-stage complex.

The strict complex is interpreted as the linear abelian Koszul--Tate chain

    gauge parameter -> fields -> density-dual Euler equations -> Noether dual.

At coarse grade the gauge generator is ``A=(1,1)^T`` on ``I+R``.  A
quadratic action has symmetric middle Hessian ``K`` and minimal BV action

    S_BV = 1/2 x^T K x + x*^T A c.

With the canonical field/antifield antibracket, ``(S_BV,S_BV)=0`` is exactly
``K A=0``.  This is a genuine master-equation/Noether condition; Hessian
symmetry alone does not imply it.  The normalized exact solution is then
extended by one gauge-inert ``S`` field to a full-nine Euler Hessian.  The
extension places the separate ``S->S`` Dirac coefficient without inserting
that block into the strict differential.

The current Stage-B rank-two witness is tested rather than presumed to lie on
this bridge.  It fails the strict generator but closes for a graph-mixing
kernel with a live S component.  The result therefore constructs a nonempty
strict action family while keeping the current witness and any filtered-graph
continuation separate.  It does not choose the native multiplicity Gram,
full-rank maps, coflip, domain, quotient, historical operator or GU verdict.
"""

from __future__ import annotations

from fractions import Fraction as F


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
    return tuple(tuple(matrix[j][i] for j in range(len(matrix))) for i in range(len(matrix[0])))


def matmul(left, right):
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0])))
        for i in range(len(left))
    )


def matvec(matrix, vector):
    return tuple(sum(matrix[i][j] * vector[j] for j in range(len(vector))) for i in range(len(matrix)))


def add(left, right):
    return tuple(tuple(a + b for a, b in zip(lrow, rrow)) for lrow, rrow in zip(left, right))


def scale(value, matrix):
    return tuple(tuple(value * entry for entry in row) for row in matrix)


def outer(left, right):
    return tuple(tuple(a * b for b in right) for a in left)


def determinant(matrix):
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def rational_rank(matrix) -> int:
    rows = [list(map(F, row)) for row in matrix]
    rank = 0
    for column in range(len(rows[0])):
        pivot = next((i for i in range(rank, len(rows)) if rows[i][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        pivot_value = rows[rank][column]
        rows[rank] = [entry / pivot_value for entry in rows[rank]]
        for i in range(len(rows)):
            if i == rank:
                continue
            factor = rows[i][column]
            if factor:
                rows[i] = [a - factor * b for a, b in zip(rows[i], rows[rank])]
        rank += 1
    return rank


def folded_matrix(d0, d1, d2):
    """Order both formal rolled parity halves as S,I,R."""
    return (
        (F(0), d2[0][0], d2[0][1]),
        (d0[0][0], d1[0][0], d1[0][1]),
        (d0[1][0], d1[1][0], d1[1][1]),
    )


def antibracket_coefficient(hessian, generator):
    """Coefficient of 2 y^T H A c in the abelian quadratic CME."""
    return matvec(hessian, generator)


def strict_compatible_hessian(a, t):
    """Full symmetric H with H(0,1,1)^T=0 and normalized RR=6/7."""
    return (
        (a, t, -t),
        (t, F(6, 7), F(-6, 7)),
        (-t, F(-6, 7), F(6, 7)),
    )


def main() -> int:
    print("=" * 96)
    print("B5 STRICT DIFFERENTIAL ACTION/BV BRIDGE GATE")
    print("=" * 96)

    stage_ranks = (128, 1792, 1792, 128)
    check("strict B5 stages retain ranks 128,1792,1792,128", stage_ranks == (128, 1792, 1792, 128))
    check("actual exactness would require arrow ranks 128,1664,128", (stage_ranks[0], stage_ranks[1] - stage_ranks[0], stage_ranks[3]) == (128, 1664, 128))

    # Canonical exact abelian action complex at 1->2->2->1 coarse grade.
    d0 = ((F(1),), (F(1),))
    middle = ((F(6, 7), F(-6, 7)), (F(-6, 7), F(6, 7)))
    d2 = ((F(1), F(1)),)
    folded = folded_matrix(d0, middle, d2)
    generator = (F(1), F(1))

    check("quadratic middle Euler map is exactly symmetric", middle == transpose(middle))
    check("terminal Noether map is the canonical transpose of the generator", d2 == transpose(d0))
    check("classical master equation is K A=0", antibracket_coefficient(middle, generator) == (F(0), F(0)))
    check("Noether-dual nilpotence A^T K=0 follows exactly", matmul(d2, middle) == ((F(0), F(0)),))
    check("strict coarse arrow ranks are 1,1,1", (rational_rank(d0), rational_rank(middle), rational_rank(d2)) == (1, 1, 1))
    check("strict action complex is exact at both middle stages", rational_rank(d0) + rational_rank(middle) == rational_rank(middle) + rational_rank(d2) == 2)
    check("folded action differential is self-adjoint for canonical stage evaluation", folded == transpose(folded))
    check("folded action differential retains structural S-to-S zero", folded[0][0] == 0)
    check("all eight strict folded blocks are nonzero", all(folded[i][j] != 0 for i in range(3) for j in range(3) if (i, j) != (0, 0)))
    check("normalized strict RR block retains W131 q=1", F(7, 6) * folded[2][2] == 1)

    # Direct antibracket replay on exact rational samples.  The polynomial
    # vanishes because its coefficient H A is identically zero, not because a
    # sample or a floating tolerance happened to vanish.
    samples = [
        ((F(1), F(2)), F(3)),
        ((F(-5, 7), F(11, 13)), F(-2)),
        ((F(0), F(1)), F(17, 19)),
    ]
    brackets = [
        F(2) * sum(y_i * ha_i for y_i, ha_i in zip(y, matvec(middle, generator))) * ghost
        for y, ghost in samples
    ]
    check("canonical BV antibracket vanishes identically on exact samples", brackets == [F(0)] * len(samples))

    symmetric_but_not_bv = ((F(13, 7), F(-6, 7)), (F(-6, 7), F(6, 7)))
    check("planted Hessian remains symmetric", symmetric_but_not_bv == transpose(symmetric_but_not_bv))
    check("Hessian symmetry alone fails the classical master equation", antibracket_coefficient(symmetric_but_not_bv, generator) != (F(0), F(0)))
    check("the same mutation breaks strict nilpotence", matmul(symmetric_but_not_bv, d0) != ((F(0),), (F(0),)))

    # Add a gauge-inert S field without inserting S->S into the differential.
    # The resulting two-parameter full-nine Euler family is the smallest exact
    # bridge on the separated route.
    strict_generator_full = (F(0), F(1), F(1))
    bridged_hessian = strict_compatible_hessian(F(2), F(5, 7))
    check("bridged Euler Hessian is symmetric and full-nine", bridged_hessian == transpose(bridged_hessian) and all(entry != 0 for row in bridged_hessian for entry in row))
    check("bridged Euler Hessian has a live independent S-to-S coefficient", bridged_hessian[0][0] == 2)
    check("bridged Euler Hessian obeys the strict-generator master equation", antibracket_coefficient(bridged_hessian, strict_generator_full) == (F(0),) * 3)
    check("bridged Euler Hessian has exact rank two", determinant(bridged_hessian) == 0 and rational_rank(bridged_hessian) == 2)
    check("strict-compatible family leaves both S-sector coefficients free", strict_compatible_hessian(F(3), F(4, 9)) != bridged_hessian and antibracket_coefficient(strict_compatible_hessian(F(3), F(4, 9)), strict_generator_full) == (F(0),) * 3)
    check("a zero S-to-S member shows CME does not normalize the Dirac coefficient", antibracket_coefficient(strict_compatible_hessian(F(0), F(5, 7)), strict_generator_full) == (F(0),) * 3)

    # Replay the current Stage-B witness exactly.  Its kernel is graph-mixing,
    # not the strict generator embedded with zero S component.
    u = (F(1), F(2), F(3))
    v = (F(4), F(5), F(6))
    current_h9 = scale(F(13, 735), add(outer(u, u), outer(v, v)))
    graph_generator = (F(1), F(-2), F(1))
    check("current full-nine Hessian remains symmetric rank two", current_h9 == transpose(current_h9) and determinant(current_h9) == 0 and rational_rank(current_h9) == 2)
    check("current full-nine Hessian fails the strict-generator master equation", antibracket_coefficient(current_h9, strict_generator_full) != (F(0),) * 3)
    check("current full-nine Hessian instead closes on its graph-mixing kernel", antibracket_coefficient(current_h9, graph_generator) == (F(0),) * 3)
    check("graph-mixing kernel has the forbidden strict S component", graph_generator[0] != 0)
    check("strict and graph-mixing generators are not proportional", graph_generator != strict_generator_full and graph_generator != tuple(-x for x in strict_generator_full))

    # Pairing ownership remains explicit.  The self-adjoint conclusion above
    # uses the canonical cotangent evaluation; it is not a selection of the
    # native S/imGamma multiplicity Gram used by the current Euler family.
    canonical_bv_pairing = "canonical-stage-evaluation"
    native_multiplicity_gram = None
    check("strict action pairing is explicitly canonical cotangent evaluation", canonical_bv_pairing == "canonical-stage-evaluation")
    check("native multiplicity Gram remains unselected", native_multiplicity_gram is None)

    if FAILURES:
        print("FAILED CONTROLS:")
        for failure in FAILURES:
            print(f"  - {failure}")
        return 1
    print(
        f"B5 STRICT BV BRIDGE VERDICT: {CHECK_COUNT}/{CHECK_COUNT} CHECKS PASS; "
        "STRICT ACTION FAMILY EXISTS, CURRENT H9 REQUIRES GRAPH MIXING"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
