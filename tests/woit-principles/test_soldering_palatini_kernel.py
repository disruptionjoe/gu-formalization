#!/usr/bin/env python3
"""Exact finite control for the Cartan/Palatini soldering mechanism.

This script does not model the GU action.  It checks the standard geometric
positive control that GU's H27 soldering audit compares against:

    D_omega Sigma^{IJ}
      = T^I wedge e^J - T^J wedge e^I,
    Sigma^{IJ} = e^I wedge e^J.

For a nondegenerate coframe in four dimensions, the linear map

    T in V tensor Lambda^2(V*)  |->  D_omega Sigma

is injective (indeed, a 24-by-24 isomorphism).  Thus the connection equation
from the Palatini action forces zero torsion.  Degenerate coframes are a
planted negative control: injectivity must fail there.

All ranks are computed over Q with the Python standard library.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations


def rank_q(matrix: list[list[int]]) -> int:
    """Return the exact row rank over Q."""

    work = [[Fraction(value) for value in row] for row in matrix]
    if not work:
        return 0
    rows = len(work)
    cols = len(work[0])
    pivot_row = 0
    for col in range(cols):
        pivot = next(
            (row for row in range(pivot_row, rows) if work[row][col] != 0),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][col]
        work[pivot_row] = [value / scale for value in work[pivot_row]]
        for row in range(rows):
            if row == pivot_row or work[row][col] == 0:
                continue
            factor = work[row][col]
            work[row] = [
                value - factor * base
                for value, base in zip(work[row], work[pivot_row])
            ]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def wedge(
    left: tuple[int, ...], right: tuple[int, ...]
) -> tuple[int, tuple[int, ...]] | None:
    """Return sign and ordered basis tuple for an exterior product."""

    if set(left).intersection(right):
        return None
    inversions = sum(a > b for a in left for b in right)
    return (-1 if inversions % 2 else 1), tuple(sorted(left + right))


def torsion_to_dsigma(coframe: list[list[int]]) -> list[list[int]]:
    """Matrix of T -> (T^I ^ e^J - T^J ^ e^I) in dimension four."""

    n = 4
    two_forms = list(combinations(range(n), 2))
    three_forms = list(combinations(range(n), 3))
    internal_pairs = list(combinations(range(n), 2))
    domain = [(internal, form) for internal in range(n) for form in two_forms]
    codomain = [
        (internal_pair, form)
        for internal_pair in internal_pairs
        for form in three_forms
    ]
    row_index = {basis: index for index, basis in enumerate(codomain)}
    matrix = [[0 for _ in domain] for _ in codomain]

    for col, (torsion_internal, torsion_form) in enumerate(domain):
        for i, j in internal_pairs:
            # D Sigma^{IJ} = T^I ^ e^J - T^J ^ e^I.
            if torsion_internal == i:
                for mu, coefficient in enumerate(coframe[j]):
                    product = wedge(torsion_form, (mu,))
                    if coefficient and product is not None:
                        sign, three_form = product
                        matrix[row_index[((i, j), three_form)]][col] += (
                            coefficient * sign
                        )
            if torsion_internal == j:
                for mu, coefficient in enumerate(coframe[i]):
                    product = wedge(torsion_form, (mu,))
                    if coefficient and product is not None:
                        sign, three_form = product
                        matrix[row_index[((i, j), three_form)]][col] -= (
                            coefficient * sign
                        )
    return matrix


def diagonal_coframe(entries: tuple[int, int, int, int]) -> list[list[int]]:
    return [
        [entries[row] if row == col else 0 for col in range(4)]
        for row in range(4)
    ]


def check(name: str, condition: bool, detail: str) -> bool:
    print(f"[{'PASS' if condition else 'FAIL'}] {name}: {detail}")
    return condition


def main() -> int:
    identity_map = torsion_to_dsigma(diagonal_coframe((1, 1, 1, 1)))
    scaled_map = torsion_to_dsigma(diagonal_coframe((2, 3, 5, 7)))
    rank_three_map = torsion_to_dsigma(diagonal_coframe((1, 1, 1, 0)))
    zero_map = torsion_to_dsigma(diagonal_coframe((0, 0, 0, 0)))

    ranks = {
        "identity": rank_q(identity_map),
        "scaled": rank_q(scaled_map),
        "rank_three": rank_q(rank_three_map),
        "zero": rank_q(zero_map),
    }

    checks = [
        check(
            "square Palatini torsion map",
            len(identity_map) == 24 and all(len(row) == 24 for row in identity_map),
            "dim(V tensor Lambda^2 V*) = dim(Lambda^2 V tensor Lambda^3 V*) = 24",
        ),
        check(
            "nondegenerate identity coframe",
            ranks["identity"] == 24,
            f"exact rank {ranks['identity']}/24, hence D Sigma = 0 implies T = 0",
        ),
        check(
            "nondegenerate rescaled coframe",
            ranks["scaled"] == 24,
            f"exact rank {ranks['scaled']}/24 (not a basis-normalization accident)",
        ),
        check(
            "degenerate coframe negative control",
            ranks["rank_three"] < 24,
            f"exact rank {ranks['rank_three']}/24 after one tetrad leg collapses",
        ),
        check(
            "zero coframe negative control",
            ranks["zero"] == 0,
            f"exact rank {ranks['zero']}/24",
        ),
    ]

    print()
    print("Interpretation:")
    print("  Standard construction: Palatini is linear in curvature; delta_omega S")
    print("  gives D_omega(e wedge e)=0, and the nondegenerate tetrad makes the")
    print("  torsion map injective.  This is the mechanism that solders gravity.")
    print("  GU transfer: not implied.  H27 separately shows that the committed")
    print("  |theta|^2=|II|^2 action has a trap-or-family equation instead.")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
