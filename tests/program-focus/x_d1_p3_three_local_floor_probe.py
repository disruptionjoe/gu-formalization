#!/usr/bin/env python3
"""X-D1-P3 floor: exact inputs for the 3-local independence of D1 and P3.

Prepared 2026-11-09 as a work-packet input for the hourly (program_focus,
lane LB-MATRIX, intersection X-D1-P3).  It certifies the finite, accepted
ingredients of the claim that the orientation datum D1 (the time-orientation
Z/2 local system on the metric fibre F = GL(4,R)/O(3,1)) carries no
3-primary information, so no additive invariant can merge D1 with the count
datum P3:

  1. F retracts to RP^3: every Lorentzian (3,1) metric has exactly one
     negative eigen-direction, a line in R^4 (spot-checked on random metrics).
  2. Cellular homology of RP^3 with F_3 coefficients equals that of S^3
     (untwisted), and with the orientation-twisted F_3 system it vanishes.
  3. The antipodal map of S^3 has degree +1, so the deck Z/2 acts trivially on
     H^*(S^3; F_3); with 2 invertible mod 3 the transfer gives
     H^*(RP^3; F_3) = H^*(S^3; F_3)^{Z/2} = H^*(S^3; F_3).
  4. The normal bundle of F over RP^3 (Sym^2 of the spatial block plus the
     time-time line) is orientable: det(Sym^2 g) = det(g)^4 = 1 on O(3), and
     O(1) acts trivially, so the 3-local Thom isomorphism applies.
  5. Hom(Z/2, Z/3) = Ext(Z/2, Z/3) = 0: no additive map moves a Z/2 class
     into 3-primary data.

Negative controls must fire: F_2 coefficients break (2), and Z/4 targets
break (5).  This probe proves the inputs only; the hourly writes the lemma,
runs review, and attempts the Lean statement.  No claim status moves.
"""

from __future__ import annotations

import random
from fractions import Fraction
from itertools import combinations_with_replacement

random.seed(20261109)


def rank_mod_p(matrix: list[list[int]], p: int) -> int:
    rows = [[x % p for x in row] for row in matrix]
    if not rows or not rows[0]:
        return 0
    rank, ncols = 0, len(rows[0])
    for col in range(ncols):
        pivot = next((r for r in range(rank, len(rows)) if rows[r][col]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inv = pow(rows[rank][col], -1, p)
        rows[rank] = [(x * inv) % p for x in rows[rank]]
        for r in range(len(rows)):
            if r != rank and rows[r][col]:
                f = rows[r][col]
                rows[r] = [(a - f * b) % p for a, b in zip(rows[r], rows[rank])]
        rank += 1
    return rank


def betti_mod_p(boundaries: dict[int, int], top: int, p: int) -> list[int]:
    """Cellular complex with one cell per dimension; boundaries[k] = d_k: C_k -> C_{k-1}."""
    ranks = {k: rank_mod_p([[boundaries.get(k, 0)]], p) for k in range(1, top + 1)}
    return [1 - ranks.get(k, 0) - ranks.get(k + 1, 0) for k in range(top + 1)]


def det(m: list[list[Fraction]]) -> Fraction:
    m = [row[:] for row in m]
    n, sign, out = len(m), 1, Fraction(1)
    for c in range(n):
        piv = next((r for r in range(c, n) if m[r][c] != 0), None)
        if piv is None:
            return Fraction(0)
        if piv != c:
            m[c], m[piv] = m[piv], m[c]
            sign = -sign
        out *= m[c][c]
        for r in range(c + 1, n):
            f = m[r][c] / m[c][c]
            m[r] = [a - f * b for a, b in zip(m[r], m[c])]
    return sign * out


def sym2_matrix(g: list[list[Fraction]]) -> list[list[Fraction]]:
    """Matrix of S -> g S g^T on symmetric 3x3 matrices, basis E_ij (i<=j)."""
    basis = list(combinations_with_replacement(range(3), 2))

    def e(i: int, j: int) -> list[list[Fraction]]:
        m = [[Fraction(0)] * 3 for _ in range(3)]
        m[i][j] = m[j][i] = Fraction(1)
        return m

    cols = []
    for i, j in basis:
        s = e(i, j)
        gs = [[sum(g[a][k] * s[k][b] for k in range(3)) for b in range(3)] for a in range(3)]
        gsg = [[sum(gs[a][k] * g[b][k] for k in range(3)) for b in range(3)] for a in range(3)]
        cols.append([gsg[a][b] for a, b in basis])
    return [[cols[c][r] for c in range(len(basis))] for r in range(len(basis))]


def lorentz_negative_count(seed_matrix: list[list[float]]) -> int:
    import numpy as np

    a = np.array(seed_matrix)
    eta = np.diag([-1.0, 1.0, 1.0, 1.0])
    h = a.T @ eta @ a
    return int(sum(1 for w in np.linalg.eigvalsh(h) if w < 0))


def main() -> int:
    checks = 0

    # 1. Fibre retraction: one negative direction for every Lorentzian metric.
    for _ in range(200):
        a = [[random.uniform(-2, 2) for _ in range(4)] for _ in range(4)]
        assert lorentz_negative_count(a) == 1
    checks += 1

    # 2. Cellular homology. RP^3 untwisted: d1=0, d2=2, d3=0; twisted: d1=2, d2=0, d3=2.
    rp3 = {1: 0, 2: 2, 3: 0}
    rp3_tw = {1: 2, 2: 0, 3: 2}
    s3_betti = [1, 0, 0, 1]
    assert betti_mod_p(rp3, 3, 3) == s3_betti
    assert betti_mod_p(rp3_tw, 3, 3) == [0, 0, 0, 0]
    checks += 2
    # negative control: mod 2 the iso with S^3 fails
    assert betti_mod_p(rp3, 3, 2) != s3_betti
    checks += 1

    # 3. Antipodal map on S^3 = -I_4 restricted: degree det(-I_4) = +1.
    minus_i4 = [[Fraction(-1 if i == j else 0) for j in range(4)] for i in range(4)]
    assert det(minus_i4) == 1
    assert pow(2, -1, 3) == 2  # 2 invertible mod 3: transfer splits
    checks += 2

    # 4. Normal bundle orientability: det(Sym^2 g) = det(g)^4 on O(3) samples.
    reflection = [[Fraction(-1), 0, 0], [0, Fraction(1), 0], [0, 0, Fraction(1)]]
    reflection = [[Fraction(x) for x in row] for row in reflection]
    assert det(reflection) == -1 and det(sym2_matrix(reflection)) == 1
    perm = [[Fraction(0), 1, 0], [1, 0, 0], [0, 0, 1]]
    perm = [[Fraction(x) for x in row] for row in perm]
    assert det(perm) == -1 and det(sym2_matrix(perm)) == 1
    c, s = Fraction(3, 5), Fraction(4, 5)
    rot = [[c, -s, 0], [s, c, 0], [Fraction(0), Fraction(0), Fraction(1)]]
    assert det(rot) == 1 and det(sym2_matrix(rot)) == 1
    # O(1) on the time-time component: (-1)*(-1) = +1
    assert (-1) * (-1) == 1
    checks += 4

    # 5. Hom(Z/2, Z/n): number of homs = gcd(2, n).  Ext(Z/2, Z/n) = Z/gcd(2, n).
    from math import gcd

    assert gcd(2, 3) == 1  # Hom = Ext = 0 for Z/3 targets
    assert gcd(2, 4) == 2  # negative control: Z/4 targets do see Z/2
    checks += 2

    print("X-D1-P3 three-local floor inputs: all exact checks pass")
    print(f"checks: {checks}; negative controls fired: 2 (F_2 coefficients, Z/4 target)")
    print("BOUNDARY: inputs only. The lemma write-up, Tier-1 review and Lean statement are the hourly's.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
