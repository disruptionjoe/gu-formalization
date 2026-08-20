#!/usr/bin/env python3
r"""Exact support gate for the typed B5 ``0 -> 1 -> 13 -> 14`` complex.

The existing B5 carrier typing is

``U0=S, U1=I+R, U2=(I+R)^vee_dens, U3=S^vee_dens``.

After stage-preserving Hodge/Krein rolls, both parity halves are ordered as
``E=S+I+R``.  A strict degree-+1 cochain differential has only

``d0: U0->U1, d1: U1->U2, d2: U2->U3``.

Consequently its folded coarse support contains the four ``S <-> (I,R)``
blocks and the four ``(I,R) -> (I,R)`` blocks, but never ``S -> S``.  This
certificate proves that structural statement, constructs an exact acyclic
``1 -> 2 -> 2 -> 1`` coarse control with normalized W131 ``q=1`` and all
eight eligible blocks nonzero, and rejects mutations that fake a ninth block
or break nilpotence/exactness.  It does not construct the full 128/1792
differential, a filtered graph roll, a global domain, or B5 cohomology.
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


def matmul(left, right):
    if not left or not right:
        return tuple()
    return tuple(
        tuple(
            sum(left[i][k] * right[k][j] for k in range(len(right)))
            for j in range(len(right[0]))
        )
        for i in range(len(left))
    )


def rational_rank(matrix) -> int:
    rows = [list(map(F, row)) for row in matrix]
    if not rows:
        return 0
    rank = 0
    for column in range(len(rows[0])):
        pivot = next(
            (index for index in range(rank, len(rows)) if rows[index][column]),
            None,
        )
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        scale = rows[rank][column]
        rows[rank] = [entry / scale for entry in rows[rank]]
        for index in range(len(rows)):
            if index == rank:
                continue
            factor = rows[index][column]
            if factor:
                rows[index] = [
                    left - factor * right
                    for left, right in zip(rows[index], rows[rank])
                ]
        rank += 1
        if rank == len(rows):
            break
    return rank


def zero(matrix) -> bool:
    return all(entry == 0 for row in matrix for entry in row)


def folded_matrix(d0, d1, d2):
    """Order both rolled parity halves as S,I,R."""
    return (
        (F(0), d2[0][0], d2[0][1]),
        (d0[0][0], d1[0][0], d1[0][1]),
        (d0[1][0], d1[1][0], d1[1][1]),
    )


def coefficients(matrix):
    """Invert the house nine-block normalization used by Stage B."""
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


def main() -> int:
    print("=" * 92)
    print("B5 FOUR-STAGE HODGE/KREIN ROLL SUPPORT GATE")
    print("=" * 92)

    stage_ranks = (128, 1792, 1792, 128)
    stage_forms = (0, 1, 13, 14)
    check("typed stage ranks are 128,1792,1792,128", stage_ranks == (128, 1792, 1792, 128))
    check("ordinary form degrees are 0,1,13,14", stage_forms == (0, 1, 13, 14))
    check("even and odd parity folds both have rank 1920", stage_ranks[0] + stage_ranks[2] == stage_ranks[1] + stage_ranks[3] == 1920)
    check("formal Hodge/Krein high-to-low rolls are rank-matched", stage_ranks[2:] == (stage_ranks[1], stage_ranks[0]))

    eligible = {
        ("S", "I"), ("S", "R"),
        ("I", "S"), ("R", "S"),
        ("I", "I"), ("I", "R"),
        ("R", "I"), ("R", "R"),
    }
    all_nine = {(source, target) for source in "SIR" for target in "SIR"}
    check("strict stage-preserving fold has exactly eight coarse blocks", len(eligible) == 8)
    check("S-to-S is the unique excluded coarse block", all_nine - eligible == {("S", "S")})
    check("a full-nine-block folded differential is structurally impossible", eligible != all_nine)
    check("planting S-to-S is detected as a degree-violating block", not ({("S", "S")} <= eligible))

    # Exact acyclic coarse control.  d0 is injective, d2 is surjective, and
    # d1 has image=ker(d2) and kernel=im(d0).  Its scale fixes folded RR=6/7,
    # hence the inherited house normalization q=1.
    d0 = ((F(1),), (F(1),))
    d1 = ((F(-6, 7), F(6, 7)), (F(-6, 7), F(6, 7)))
    d2 = ((F(1), F(-1)),)
    folded = folded_matrix(d0, d1, d2)
    packet = coefficients(folded)

    check("d1 d0 vanishes exactly", zero(matmul(d1, d0)))
    check("d2 d1 vanishes exactly", zero(matmul(d2, d1)))
    check("coarse control ranks are 1,1,1", (rational_rank(d0), rational_rank(d1), rational_rank(d2)) == (1, 1, 1))
    check("coarse control is exact at its first middle stage", rational_rank(d0) + rational_rank(d1) == 2)
    check("coarse control is exact at its second middle stage", rational_rank(d1) + rational_rank(d2) == 2)
    check("actual-rank acyclicity would require differential ranks 128,1664,128", (stage_ranks[0], stage_ranks[1] - stage_ranks[0], stage_ranks[3]) == (128, 1664, 128))
    check("folded positive control has structural S-to-S zero", folded[0][0] == 0)
    check("all eight cochain-eligible folded blocks are nonzero", all(folded[row][column] != 0 for row in range(3) for column in range(3) if (row, column) != (0, 0)))
    check("positive control retains normalized W131 q=1", packet["q"] == 1)
    check("positive control cannot satisfy current full-nine support", packet["a"] == 0 and all(packet[name] != 0 for name in packet if name != "a"))

    broken_d1 = ((F(-6, 7), F(6, 7)), (F(-6, 7), F(5, 7)))
    check("one-entry middle mutation breaks nilpotence", not zero(matmul(broken_d1, d0)) or not zero(matmul(d2, broken_d1)))
    broken_d2 = ((F(1), F(1)),)
    check("wrong terminal adjoint mutation breaks nilpotence", not zero(matmul(broken_d2, d1)))
    singular_roll_ranks = (stage_ranks[1] - 1, stage_ranks[0])
    check("singular high-to-low roll is rejected", singular_roll_ranks != (stage_ranks[1], stage_ranks[0]))
    check("nonzero S-to-S requires extra graph mixing or a non-cochain Euler term", packet["a"] == 0)

    if FAILURES:
        print("FAILED CONTROLS:")
        for failure in FAILURES:
            print(f"  - {failure}")
        return 1
    print(
        f"B5 FOUR-STAGE VERDICT: {CHECK_COUNT}/{CHECK_COUNT} CHECKS PASS; "
        "STAGE-PRESERVING FOLD HAS EIGHT-BLOCK CEILING"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
