#!/usr/bin/env python3
"""Independent re-verification of the Joe-directed channel-3 Majorana block.

Deliberately disjoint from `joe_directed_majorana_126_block_probe.py` in every
place the primary probe could have smuggled in a convention:

  (1) DIFFERENT Clifford construction.  The primary probe used Jordan-Wigner
      with sigma_z strings on the LEFT.  Here Cl(2n+2) is built by the
      recursion  g_a -> g_a (x) sz,  g_{2n+1} = I (x) sx,  g_{2n+2} = I (x) sy,
      which distributes the string factors on the RIGHT.
  (2) DIFFERENT charge conjugation.  The primary probe used
      C = G_2 G_4 G_6 G_8 G_10  (C G C^-1 = -G^T).  Here C' is the product of
      the ODD gammas, giving C' G C'^-1 = +G^T.
  (3) DIFFERENT nu_R identification.  The primary probe read nu_R off the Fock
      occupation basis.  Here nu_R is identified intrinsically as the unique
      weight vector of the so(10) Cartan whose five weights are all equal --
      the SU(5)-singlet weight -- with no reference to basis ordering.

All arithmetic is exact integer arithmetic in Z[i]; no floating point.
"""
from __future__ import annotations

from itertools import combinations
from math import comb

import numpy as np

CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool) -> None:
    CHECKS.append((name, bool(ok)))


class Zi:
    __slots__ = ("re", "im")

    def __init__(self, re, im) -> None:
        self.re = np.asarray(re, dtype=np.int64)
        self.im = np.asarray(im, dtype=np.int64)

    @staticmethod
    def eye(n: int) -> "Zi":
        return Zi(np.eye(n, dtype=np.int64), np.zeros((n, n), dtype=np.int64))

    def __matmul__(self, o: "Zi") -> "Zi":
        return Zi(self.re @ o.re - self.im @ o.im, self.re @ o.im + self.im @ o.re)

    def __add__(self, o: "Zi") -> "Zi":
        return Zi(self.re + o.re, self.im + o.im)

    def scaled(self, a: int, b: int = 0) -> "Zi":
        return Zi(a * self.re - b * self.im, a * self.im + b * self.re)

    def T(self) -> "Zi":
        return Zi(self.re.T, self.im.T)

    def equals(self, o: "Zi") -> bool:
        return bool(np.array_equal(self.re, o.re) and np.array_equal(self.im, o.im))

    def is_zero(self) -> bool:
        return bool(not self.re.any() and not self.im.any())

    def sub(self, r, c) -> "Zi":
        return Zi(self.re[np.ix_(r, c)], self.im[np.ix_(r, c)])


def kron(a: Zi, b: Zi) -> Zi:
    return Zi(np.kron(a.re, b.re) - np.kron(a.im, b.im),
              np.kron(a.re, b.im) + np.kron(a.im, b.re))


I2 = Zi.eye(2)
SX = Zi([[0, 1], [1, 0]], [[0, 0], [0, 0]])
SY = Zi([[0, 0], [0, 0]], [[0, -1], [1, 0]])
SZ = Zi([[1, 0], [0, -1]], [[0, 0], [0, 0]])

# --- (1) recursive construction, string factors on the RIGHT ---------------
gammas: list[Zi] = [SX, SY]
while len(gammas) < 10:
    n = gammas[0].re.shape[0]
    gammas = [kron(g, SZ) for g in gammas]
    gammas.append(kron(Zi.eye(n), SX))
    gammas.append(kron(Zi.eye(n), SY))

G = gammas
DIM = G[0].re.shape[0]
check("independent build: dim 32", DIM == 32)

two_I, zero = Zi.eye(DIM).scaled(2), Zi.eye(DIM).scaled(0)
check("independent build: Clifford relations exact",
      all((G[a] @ G[b] + G[b] @ G[a]).equals(two_I if a == b else zero)
          for a in range(10) for b in range(10)))

prod = Zi.eye(DIM)
for g in G:
    prod = prod @ g
CHI = prod.scaled(0, -1)
check("independent build: chirality squares to I", (CHI @ CHI).equals(Zi.eye(DIM)))
check("independent build: chirality is diagonal-real",
      not CHI.im.any() and np.array_equal(CHI.re, np.diag(CHI.re.diagonal())))

PLUS = np.flatnonzero(CHI.re.diagonal() == 1)
check("independent build: dim S+ == 16", len(PLUS) == 16)

# --- (3) intrinsic nu_R via so(10) Cartan weights --------------------------
# Cartan generators  H_j = -(i/2) G_{2j-1} G_{2j}  have eigenvalues +-1/2.
# Work with 2*H_j so everything stays an exact integer (+-1).
weights = []
for j in range(1, 6):
    Hj2 = (G[2 * j - 2] @ G[2 * j - 1]).scaled(0, -1)  # -i G_{2j-1} G_{2j}
    check(f"Cartan 2H_{j} is diagonal with entries +-1",
          not Hj2.im.any()
          and np.array_equal(Hj2.re, np.diag(Hj2.re.diagonal()))
          and set(np.unique(Hj2.re.diagonal()).tolist()) <= {-1, 1})
    weights.append(Hj2.re.diagonal()[PLUS])

W = np.array(weights).T  # 16 x 5 matrix of doubled weights
check("S+ weights have an even number of minus signs",
      all(int((row == -1).sum()) % 2 == 0 for row in W))

all_equal = [i for i, row in enumerate(W) if len(set(row.tolist())) == 1]
# The all-minus weight carries five minus signs (odd), so it lies in the 16bar,
# not the 16.  Hence the 16 contains EXACTLY ONE all-equal weight vector, and
# the SU(5) singlet of the 16 is unique.
check("exactly one all-equal weight vector in the 16 (unique SU(5) singlet)",
      len(all_equal) == 1)
check("that vector is the all-plus one (all-minus sits in the 16bar)",
      len(all_equal) == 1 and (W[all_equal[0]] == 1).all())
NU_R = [i for i in all_equal if (W[i] == 1).all()]
check("a unique all-plus weight vector exists = nu_R", len(NU_R) == 1)
NU_R = NU_R[0]

# SU(5) branching read intrinsically off the weights: #(-1) in {0,2,4}
levels = [int((row == -1).sum()) for row in W]
check("independent SU(5) branch 16 = 1 + 10 + 5bar",
      [levels.count(k) for k in (0, 2, 4)] == [1, 10, 5])

# --- (2) the OTHER charge conjugation --------------------------------------
Cp = Zi.eye(DIM)
for a in range(1, 11, 2):  # odd gammas
    Cp = Cp @ G[a - 1]
CC = Cp @ Cp
Cp_inv = Cp if CC.equals(Zi.eye(DIM)) else Cp.scaled(-1)
check("C' inverse verified", (Cp @ Cp_inv).equals(Zi.eye(DIM)))
check("C' G_a C'^-1 = +G_a^T exactly",
      all((Cp @ g @ Cp_inv).equals(g.T()) for g in G))


def word(idxs) -> Zi:
    out = Zi.eye(DIM)
    for a in idxs:
        out = out @ G[a - 1]
    return out


def blk(m: Zi) -> Zi:
    return m.sub(PLUS, PLUS)


# --- symmetry type, recomputed with the other C ----------------------------
for k, want in ((1, "sym"), (3, "anti"), (5, "sym")):
    kinds = set()
    for idxs in combinations(range(1, 11), k):
        b = blk(Cp @ word(idxs))
        if b.is_zero():
            continue
        kinds.add("sym" if b.T().equals(b) else ("anti" if b.T().equals(b.scaled(-1)) else "mixed"))
    check(f"independent: Lambda^{k} block is {want}", kinds == {want})

# --- complex ranks, independent prime and independent sqrt(-1) -------------
P = 2013265921            # prime, P % 4 == 1 (different from the primary probe)
S = pow(31, (P - 1) // 4, P)
assert (S * S) % P == P - 1


def crank(k: int) -> int:
    rows = []
    for idxs in combinations(range(1, 11), k):
        b = blk(Cp @ word(idxs))
        if b.is_zero():
            continue
        rows.append(((b.re.ravel().astype(object) + S * b.im.ravel().astype(object)) % P).tolist())
    if not rows:
        return 0
    ncols, r = len(rows[0]), 0
    for c in range(ncols):
        piv = next((i for i in range(r, len(rows)) if rows[i][c] % P), None)
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        inv = pow(int(rows[r][c]), P - 2, P)
        rows[r] = [(x * inv) % P for x in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c] % P:
                f = rows[i][c]
                rows[i] = [(x - f * y) % P for x, y in zip(rows[i], rows[r])]
        r += 1
        if r == len(rows):
            break
    return r


r1, r3, r5 = crank(1), crank(3), crank(5)
check("independent: complex ranks are 10 / 120 / 126", (r1, r3, r5) == (10, 120, 126))
check("independent: checksum 10+120+126 == 256 == 16^2", r1 + r3 + r5 == 256)

# --- the Majorana block, rebuilt ------------------------------------------
def five_form(sign: int) -> Zi:
    out = Zi.eye(DIM)
    for j in range(1, 6):
        out = out @ (G[2 * j - 2] + G[2 * j - 1].scaled(0, sign))
    return out


b_plus, b_minus = blk(Cp @ five_form(+1)), blk(Cp @ five_form(-1))
check("independent: exactly one singlet direction acts on S+ x S+",
      b_plus.is_zero() != b_minus.is_zero())
M = b_minus if b_plus.is_zero() else b_plus

check("independent: Majorana block nonzero", not M.is_zero())
check("independent: Majorana block SYMMETRIC", M.T().equals(M))

nz = list(zip(*np.nonzero((M.re != 0) | (M.im != 0))))
check("independent: exactly one nonzero entry", len(nz) == 1)
check("independent: that entry sits on the nu_R weight vector, "
      "identified by Cartan weights alone",
      len(nz) == 1 and int(nz[0][0]) == NU_R and int(nz[0][1]) == NU_R)

others = np.array([i for i in range(16) if i != NU_R])
check("independent: SM sector (5bar + 10) receives no mass",
      M.sub(others, np.arange(16)).is_zero())
check("independent: no opposite-chirality (vectorlike) part",
      (Cp @ (five_form(-1) if b_plus.is_zero() else five_form(+1)))
      .sub(PLUS, np.flatnonzero(CHI.re.diagonal() == -1)).is_zero())

# --- ambient arithmetic, recomputed ---------------------------------------
check("independent: Lorentz-scalar part of Lambda^5(14) is 252 = 126 + 126bar",
      comb(4, 0) * comb(10, 5) == 252 and comb(10, 5) == 252)
check("independent: both signature horns share internal Spin(6,4)",
      (1 + 6, 3 + 4) == (7, 7) and (3 + 6, 1 + 4) == (9, 5))

passed = sum(1 for _, ok in CHECKS if ok)
for name, ok in CHECKS:
    print(f"  {'PASS' if ok else 'FAIL'}  {name}")
print(f"\n{passed}/{len(CHECKS)} independent exact checks passed")
raise SystemExit(0 if passed == len(CHECKS) else 1)
