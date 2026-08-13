#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""M-H7 dim-13 restatement probe: exact arithmetic the restatement leans on.

Companion certificate for ``explorations/mh7-dim13-restatement-2026-08-03.md``
(register row M-H7; council seat-3 Q8 decidable half). It certifies, with
exact integer arithmetic and hard asserts, every CHEAP step of the dim-13
restatement of "located, not forced" -- and ONLY those steps. It recomputes
none of the pinned coefficient facts.

CITED INPUTS (Resolver Wave C rebased, 2026-08-03, exact
representation/coefficient-group grade -- cite, do not recompute):
  * Omega_13^fr = pi_13^s = Z/3           [CITED-WAVE-C]
  * Im J_13 = 0                            [CITED-WAVE-C]
  * Omega_13^Spin = 0                      [CITED-WAVE-C]
STANDARD INPUTS (textbook stable stems, Toda; used only as gcd/exponent
bookkeeping, tagged STANDARD):
  * exponents of pi_n^s for n = 1..12 (table below)
  * pi_3^s = Z/24, pi_6^s = Z/2, pi_10^s = Z/6
CITED VALUES from canon/boundary-einvariant-and-the-tangential-fork.md
(dim-3 SPINE data, used only for CRT consistency fences): classes 2 (e_R =
1/12 tangential), 8 (the KO-corrected order-3 carrier 8*nu), 9 (gauge
reading +/-9) in Z/24.

WHAT IS COMPUTED HERE (exact, no floats):
  PART 1  Receptacle purity: Hom(A, Z/3) = 0 = Hom(Z/3, A) for EVERY finite
          abelian 2-group A of order <= 2^8 (exhaustive over partitions);
          2 is invertible mod 3, so the only element of Z/3 killed by a
          power of 2 is 0.  "2-primary blindness" (dim 3) upgrades to a
          group identity (dim 13).
  PART 2  CRT contrast dim 3 vs dim 13: Z/24 = Z/8 (+) Z/3 (two arenas);
          Z/3 has trivial 2-part (one arena).  Consistency of the cited
          spine classes 2, 8, 9 under the 3-part projection.
  PART 3  Product-framing kill: ord(xy) | gcd(exp pi_a^s, exp pi_b^s); over
          all two-factor splits 13 = a + b the ONLY split whose gcd retains
          a factor 3 is 3 + 10 (the alpha1*beta1 site).  Every geometric
          product split the link model offers (6+7, 9+4, 6+3+4 -- any split
          using a closed framed 4- or 5-dim factor) is EXACTLY ZERO.
          This sharpens Wave C's zero control: a nonzero receptacle class
          requires a non-product framing.
  PART 4  Mod-3 homology of the 9-dim fiber-link (the S^6-bundle over the
          RP^3 spine), BOTH orientation branches, via exact F_3 chain
          complexes + certified Serre-SS collapse (index enumeration):
          untwisted branch = mod-3 homology S^3 x S^6 (degrees 0,3,6,9);
          twisted branch  = degrees 0,3 only (no mod-3 fundamental class).
          In both branches H_3(link; F_3) = H_3(RP^3; F_3): the degree-3
          mod-3 content of the link IS the spine's.
  PART 5  Layer-0 "13" homonym fence: the three load-bearing "13"s arise
          from arithmetically DIFFERENT decompositions (13*128 = 1664 =
          14*128 - 128; 13 = 14 - 1; 13 = 3 + 10 = 6 + 3 + 4 = 9 + 4).
          The asserts certify the identities; the HOMONYM typing (these are
          different objects, no artifact relates them) is the fence and is
          restated in the companion note (pack + M-M28).

NO VERDICT MOVEMENT. This is arithmetic support for a restatement note:
unchanged.  Pre-deposit; any decisive downstream use is J5-gated.

Exact arithmetic only. check()-style asserts; exits nonzero on any failure.
"""

from __future__ import annotations

import sys
from itertools import combinations
from math import gcd, prod

FAIL: list[str] = []


def check(name: str, cond: bool, detail: str = "") -> bool:
    tag = "ok  " if cond else "FAIL"
    if not cond:
        FAIL.append(name)
    print(f"  [{tag}] {name}" + (f"  --  {detail}" if detail else ""))
    return cond


def header(s: str) -> None:
    print("\n" + "=" * 78 + f"\n{s}\n" + "=" * 78)


# ---------------------------------------------------------------------------
header("PART 0  --  INPUT TABLES (CITED / STANDARD; not recomputed here)")
# ---------------------------------------------------------------------------
# Pinned by Resolver Wave C rebased (2026-08-03) -- CITED, not recomputed:
ORD_PI13S = 3          # Omega_13^fr = pi_13^s = Z/3          [CITED-WAVE-C]
ORD_IMJ13 = 1          # Im J_13 = 0                           [CITED-WAVE-C]
ORD_OMEGA13SPIN = 1    # Omega_13^Spin = 0                     [CITED-WAVE-C]

# STANDARD (Toda) exponents of the stable stems pi_n^s, n = 1..13, used only
# as annihilator bookkeeping for the product-framing kill.  pi_13^s entry
# repeats the CITED value.
#          n:    1  2   3  4  5  6    7  8  9  10   11  12 13
STEM_EXPONENT = [2, 2, 24, 1, 1, 2, 240, 2, 2,  6, 504,  1, ORD_PI13S]

# STANDARD group orders where they differ from the exponent (elementary
# abelian stems); only used for display, never for the divisibility logic.
STEM_ORDER = [2, 2, 24, 1, 1, 2, 240, 4, 8, 6, 504, 1, ORD_PI13S]

print("  CITED-WAVE-C : |pi_13^s| = 3, Im J_13 = 0, Omega_13^Spin = 0")
print("  STANDARD     : stem exponents n=1..13:", STEM_EXPONENT)
check("cited receptacle is Z/3 (order 3, prime)", ORD_PI13S == 3)
check("cited Im J_13 trivial", ORD_IMJ13 == 1)
check("cited Omega_13^Spin trivial", ORD_OMEGA13SPIN == 1)

# ---------------------------------------------------------------------------
header("PART 1  --  RECEPTACLE PURITY: Hom(2-group, Z/3) = 0 (group identity)")
# ---------------------------------------------------------------------------
# #Hom(Z/m, Z/n) = gcd(m, n).  A finite abelian 2-group is a sum of Z/2^a_i.
# Exhaust all abelian 2-groups of order <= 2**8 via partitions of k <= 8.


def partitions(k: int, mx: int | None = None):
    if k == 0:
        yield ()
        return
    mx = k if mx is None else min(mx, k)
    for first in range(mx, 0, -1):
        for rest in partitions(k - first, first):
            yield (first, *rest)


n_groups = 0
all_trivial_to = True
all_trivial_from = True
for k in range(0, 9):
    for part in partitions(k):
        n_groups += 1
        homs_to_z3 = prod(gcd(2 ** a, 3) for a in part) if part else 1
        homs_from_z3 = prod(gcd(3, 2 ** a) for a in part) if part else 1
        all_trivial_to &= homs_to_z3 == 1
        all_trivial_from &= homs_from_z3 == 1

check(
    f"Hom(A, Z/3) = 0 for ALL {n_groups} abelian 2-groups A with |A| <= 2^8",
    all_trivial_to,
    "#Hom = prod gcd(2^a_i, 3) = 1 (only the zero map)",
)
check(
    f"Hom(Z/3, A) = 0 for ALL {n_groups} abelian 2-groups A with |A| <= 2^8",
    all_trivial_from,
)
check(
    "2 is invertible mod 3 (2*2 = 1 mod 3), so 2z = 0 in Z/3 forces z = 0",
    (2 * 2) % 3 == 1 and all(z == 0 for z in range(3) if (2 * z) % 3 == 0),
)
check(
    "Sylow-2 subgroup of the dim-13 receptacle Z/3 is trivial",
    gcd(ORD_PI13S, 2 ** 10) == 1,
    "dim 13 has NO 2-primary arena at all (contrast dim 3 below)",
)

# ---------------------------------------------------------------------------
header("PART 2  --  CRT CONTRAST: dim-3 surrogate (two arenas) vs dim 13 (one)")
# ---------------------------------------------------------------------------
check("dim-3 surrogate receptacle Z/24 CRT-splits: gcd(8,3)=1, 8*3=24",
      gcd(8, 3) == 1 and 8 * 3 == 24)

# Spine classes (CITED values from canon/boundary-einvariant-...md): the
# arithmetic below is computed; the class values are cited, not derived.
spine_classes = {
    2: ("tangential reading, e_R = 1/12", 2 % 8, 2 % 3),
    8: ("KO-corrected order-3 carrier 8*nu, e_KO = 1/3", 8 % 8, 8 % 3),
    9: ("gauge-coefficient reading, e = +/-3/8", 9 % 8, 9 % 3),
}
for cls, (label, two_part, three_part) in spine_classes.items():
    print(f"    class {cls} in Z/24  ({label}) -> (mod 8, mod 3) = "
          f"({two_part}, {three_part})")
check("cited tangential class 2 has NONZERO 3-part (2 mod 3 = 2)",
      spine_classes[2][2] == 2)
check("cited 8*nu carrier is PURE order 3: CRT (0, 2)",
      spine_classes[8][1] == 0 and spine_classes[8][2] == 2)
check("cited gauge-reading class 9 has ZERO 3-part (9 mod 3 = 0)",
      spine_classes[9][2] == 0)
check(
    "dim-13 contrast: Z/3 is its own 3-part; there is no Z/8 arena to project away",
    ORD_PI13S == 3 and ORD_PI13S % 2 == 1,
)

# ---------------------------------------------------------------------------
header("PART 3  --  PRODUCT-FRAMING KILL: which splits of 13 can carry Z/3")
# ---------------------------------------------------------------------------
# For x in pi_a^s, y in pi_b^s: (exp pi_a^s) * xy = 0 and (exp pi_b^s) * xy
# = 0, so ord(xy) | gcd(exp_a, exp_b).  Nonzero in Z/3 needs 3 | gcd.


def exp_stem(n: int) -> int:
    assert 1 <= n <= 13
    return STEM_EXPONENT[n - 1]


alive_splits = []
for a in range(1, 13):
    b = 13 - a
    if b < 1 or a > b:
        continue
    g = gcd(exp_stem(a), exp_stem(b))
    alive = g % 3 == 0
    if alive:
        alive_splits.append((a, b))
    print(f"    13 = {a:2d} + {b:2d}: gcd(exp={exp_stem(a)}, exp={exp_stem(b)})"
          f" = {g:3d}  -> {'ALIVE (3 | gcd)' if alive else 'dead'}")

check(
    "the ONLY two-factor split of 13 that can carry Z/3 is 3 + 10",
    alive_splits == [(3, 10)],
    "the alpha1(3-stem) * beta1(10-stem) site; every other split is 3-free",
)
check(
    "geometric split 6 + 7 (S^6 x framed X^7) is exactly zero in Z/3",
    gcd(exp_stem(6), exp_stem(7)) % 3 != 0,
    "exp pi_6^s = 2 kills the 3-part: 2(xy)=0 and 2 invertible mod 3",
)
check(
    "geometric split 9 + 4 (fiber-link x framed base X^4) is exactly zero",
    exp_stem(4) == 1,
    "pi_4^s = 0: a closed framed 4-manifold factor is already null-bordant",
)
check(
    "triple geometric split 6 + 3 + 4 is exactly zero (the 4-factor dies)",
    exp_stem(4) == 1,
)
check(
    "5-dim factor also dies (pi_5^s = 0): no 5 + 8 product survives",
    exp_stem(5) == 1 and gcd(exp_stem(5), exp_stem(8)) % 3 != 0,
)
# Consequence (matches Wave C's zero control, sharpened): any external-
# product presentation through the link's OWN geometric factorizations
# (S^6-factor, X^4-factor, or both) is exactly 0 in pi_13^s.  A nonzero
# receptacle class therefore requires a NON-PRODUCT stable framing, and the
# only stem-arithmetic site for a two-factor presentation is 3 + 10.

# ---------------------------------------------------------------------------
header("PART 4  --  MOD-3 HOMOLOGY OF THE 9-DIM FIBER-LINK (both branches)")
# ---------------------------------------------------------------------------
# Exact F_3 linear algebra.  Matrices are entries mod 3; rank by Gaussian
# elimination over the field F_3 (integer arithmetic only).


def rank_f3(rows: list[list[int]]) -> int:
    m = [[x % 3 for x in row] for row in rows]
    rank = 0
    n_rows = len(m)
    n_cols = len(m[0]) if n_rows else 0
    piv_row = 0
    for col in range(n_cols):
        sel = next((r for r in range(piv_row, n_rows) if m[r][col] % 3), None)
        if sel is None:
            continue
        m[piv_row], m[sel] = m[sel], m[piv_row]
        inv = 1 if m[piv_row][col] % 3 == 1 else 2  # inverse in F_3
        m[piv_row] = [(inv * x) % 3 for x in m[piv_row]]
        for r in range(n_rows):
            if r != piv_row and m[r][col] % 3:
                f = m[r][col]
                m[r] = [(m[r][c] - f * m[piv_row][c]) % 3 for c in range(n_cols)]
        rank += 1
        piv_row += 1
    return rank


def homology_dims_f3(dims: list[int], boundaries: dict[int, list[list[int]]]):
    """dims[k] = dim C_k; boundaries[k]: matrix of d_k: C_k -> C_{k-1}
    (shape dims[k-1] x dims[k]).  Returns Betti numbers over F_3."""
    top = len(dims) - 1

    def rank_of(k: int) -> int:
        mat = boundaries.get(k)
        if not mat or k < 1 or k > top or dims[k] == 0 or dims[k - 1] == 0:
            return 0
        return rank_f3(mat)

    # betti_k = dim ker d_k - rank d_{k+1} = dims[k] - rank d_k - rank d_{k+1}
    return [dims[k] - rank_of(k) - rank_of(k + 1) for k in range(top + 1)]


# RP^3 cellular complex from the S^3 double cover as a Z[Z/2]-complex:
# C_k = Z[t]/(t^2-1), d1 = t-1, d2 = t+1, d3 = t-1.  Tensor over Z[Z/2]
# with the coefficient module Z/3:
#   trivial action  t -> +1:  d1 -> 0, d2 -> 2, d3 -> 0
#   sign action     t -> -1:  d1 -> -2 = 1, d2 -> 0, d3 -> 1
betti_rp3_triv = homology_dims_f3(
    [1, 1, 1, 1], {1: [[0]], 2: [[2]], 3: [[0]]})
betti_rp3_sign = homology_dims_f3(
    [1, 1, 1, 1], {1: [[1]], 2: [[0]], 3: [[1]]})
print(f"    H_*(RP^3; F_3 trivial) Betti = {betti_rp3_triv}")
print(f"    H_*(RP^3; F_3 sign)    Betti = {betti_rp3_sign}")
check("H_*(RP^3; F_3) = F_3 in degrees 0 and 3 only (mod-3 homology 3-sphere)",
      betti_rp3_triv == [1, 0, 0, 1],
      "d2 = 2 is invertible mod 3: the 2-torsion of RP^3 is mod-3 invisible")
check("H_*(RP^3; F_3 sign-twisted) = 0 in ALL degrees",
      betti_rp3_sign == [0, 0, 0, 0],
      "t -> -1 makes d1, d3 units mod 3")

# Serre SS collapse for S^6 -> L^9 -> RP^3 with F_3 coefficients:
# E^2_{p,q} = H_p(RP^3; H_q(S^6; F_3)^w), nonzero rows q in {0, 6} only.
# d^r: E^r_{p,q} -> E^r_{p-r, q+r-1}.  Certify no differential connects two
# potentially-nonzero slots, by exhaustive index enumeration.
NONZERO_ROWS = {0, 6}
BASE_RANGE = range(0, 4)          # p in 0..3
crossing = []
for r in range(2, 15):
    for p in BASE_RANGE:
        for q in NONZERO_ROWS:
            tp, tq = p - r, q + r - 1
            if tp in BASE_RANGE and tq in NONZERO_ROWS:
                crossing.append((r, p, q, tp, tq))
check(
    "Serre SS collapses at E^2: NO differential joins nonzero rows q in {0,6}",
    crossing == [],
    "q=0 needs r=7 but p-7 < 0; q=6 targets q >= 7: exhaustively enumerated",
)

# E^2 = E^infty over the field F_3; assemble both orientation branches.
# Branch A (fiber-orientable, w trivial):  q=6 row = H_p(RP^3; F_3).
# Branch B (fiber-orientation twisted):    q=6 row = H_p(RP^3; F_3 sign) = 0.
link_A = [0] * 10
link_B = [0] * 10
for p in BASE_RANGE:
    link_A[p] += betti_rp3_triv[p]           # q = 0 row (always untwisted)
    link_B[p] += betti_rp3_triv[p]
    link_A[p + 6] += betti_rp3_triv[p]       # q = 6 row, branch A
    link_B[p + 6] += betti_rp3_sign[p]       # q = 6 row, branch B
print(f"    branch A (untwisted) H_*(L^9; F_3) Betti = {link_A}")
print(f"    branch B (twisted)   H_*(L^9; F_3) Betti = {link_B}")

# Kunneth control for branch A against the RP^3 x S^6 model:
kunneth = [0] * 10
for i, bi in enumerate(betti_rp3_triv):
    for j, bj in enumerate([1, 0, 0, 0, 0, 0, 1]):
        kunneth[i + j] += bi * bj
check("branch A = Kunneth of RP^3 x S^6 over F_3 (degrees 0,3,6,9)",
      link_A == kunneth and link_A == [1, 0, 0, 1, 0, 0, 1, 0, 0, 1])
check("branch B: mod-3 homology in degrees 0,3 ONLY; H_9(L^9; F_3) = 0",
      link_B == [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
      "twisted branch has NO mod-3 fundamental class (fiber-nonorientable)")
check(
    "BOTH branches: H_3(L^9; F_3) = H_3(RP^3; F_3) = F_3 (spine content only)",
    link_A[3] == 1 and link_B[3] == 1 and betti_rp3_triv[3] == 1,
    "degrees <= 5 of the link see ONLY the spine; the S^6 row starts at 6",
)
check(
    "Euler-characteristic parity control: chi = 0 in both branches (odd dim)",
    sum((-1) ** k * link_A[k] for k in range(10)) == 0
    and sum((-1) ** k * link_B[k] for k in range(10)) == 0,
    "neither branch is excluded by chi; orientability is a real open input",
)

# ---------------------------------------------------------------------------
header("PART 5  --  LAYER-0 '13' HOMONYM FENCE (arithmetic identities only)")
# ---------------------------------------------------------------------------
# THREE load-bearing '13's (pack + M-M28): SAME integer, DIFFERENT objects.
# The identities below are certified; the typing (HOMONYM -- no artifact
# relates them) is the fence, restated in the companion note.
check("13 (RS multiplicity): 1664 = 13 * 128 = 14*128 - 128 (ker Gamma count)",
      13 * 128 == 1664 and 14 * 128 - 128 == 1664)
check("13 (link dimension):  13 = 14 - 1 (link of the Y^14 end)",
      14 - 1 == 13)
check("13 (receptacle stem): 13 = 3 + 10 (alpha1 * beta1 stem site)",
      3 + 10 == 13)
check("geometric splits agree numerically: 6+3+4 = 9+4 = 13 (S^6/RP^3/X^4)",
      6 + 3 + 4 == 13 and 9 + 4 == 13)
print("    FENCE: these are DIFFERENT objects sharing the numeral 13.")
print("    Multiplicity != count; group order != count; dim != multiplicity.")

# ---------------------------------------------------------------------------
header("VERDICT")
# ---------------------------------------------------------------------------
if FAIL:
    print(f"\n  {len(FAIL)} FAILURE(S): {FAIL}")
else:
    print("\n  all checks passed -- the cheap arithmetic layer of the dim-13")
    print("  restatement is certified; every deep step remains CITED or OPEN")
    print("  exactly as itemized in the companion note's gap list.")

assert not FAIL, f"mh7 dim-13 probe failures: {FAIL}"
sys.exit(0)
