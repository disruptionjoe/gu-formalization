#!/usr/bin/env python3
"""Joe-directed channel 3, gate MJ-3: does GU's gauge sector reach the 126?

MJ-1: the nu (x) nu bilinear reaches the 126 with an exact, symmetric,
rank-one, SM-preserving block on nu_R.
MJ-2: no elementary GU field can carry a 126 VEV.

So the surviving route is a CONDENSATE.  A dynamical <nu nu> in the 126
direction needs a four-fermion operator in that pairing channel.  GU already
has one candidate source: exchange of its own ad-valued gauge bosons, which is
the ADJOINT (45) channel.  The question is whether adjoint exchange, Fierz-
rearranged into the pairing basis, has a nonzero 126 component.

THE TWO BASES.  For the 16 of so(10),

    16 (x) 16bar = 1 + 45 + 210        (annihilation / current channel)
    16 (x) 16    = 10 + 120 + 126      (pairing / diquark channel)

Both give a basis for the SAME 3-dimensional space of so(10)-invariant
four-index tensors.  The change of basis is the Fierz matrix F:

    A_a = sum_b F[a][b] P_b,    a in {0,2,4},  b in {1,3,5}

and the number that decides this gate is F[45][126].

EXACTNESS.  Tensors are built in exact Z[i] integer arithmetic.  F is solved
in exact rationals (sympy, over Q(i)) from three chosen components, then
VERIFIED on all 16^4 = 65536 components with denominators cleared, so the
identity is checked exactly and globally rather than fitted.
"""
from __future__ import annotations

from itertools import combinations

import numpy as np
import sympy as sp

CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool) -> None:
    CHECKS.append((name, bool(ok)))


# --------------------------------------------------------------------------
# Exact Z[i] matrices (re, im) as int64 pairs -- same discipline as MJ-1.
# --------------------------------------------------------------------------
class Zi:
    __slots__ = ("re", "im")

    def __init__(self, re, im):
        self.re = np.asarray(re, dtype=np.int64)
        self.im = np.asarray(im, dtype=np.int64)

    @staticmethod
    def eye(n):
        return Zi(np.eye(n, dtype=np.int64), np.zeros((n, n), dtype=np.int64))

    def __matmul__(self, o):
        return Zi(self.re @ o.re - self.im @ o.im, self.re @ o.im + self.im @ o.re)

    def __add__(self, o):
        return Zi(self.re + o.re, self.im + o.im)

    def scaled(self, a, b=0):
        return Zi(a * self.re - b * self.im, a * self.im + b * self.re)

    def equals(self, o):
        return bool(np.array_equal(self.re, o.re) and np.array_equal(self.im, o.im))

    def is_zero(self):
        return bool(not self.re.any() and not self.im.any())

    def sub(self, r, c):
        return Zi(self.re[np.ix_(r, c)], self.im[np.ix_(r, c)])


def kron(a, b):
    return Zi(np.kron(a.re, b.re) - np.kron(a.im, b.im),
              np.kron(a.re, b.im) + np.kron(a.im, b.re))


I2 = Zi.eye(2)
SX = Zi([[0, 1], [1, 0]], [[0, 0], [0, 0]])
SY = Zi([[0, 0], [0, 0]], [[0, -1], [1, 0]])
SZ = Zi([[1, 0], [0, -1]], [[0, 0], [0, 0]])

NQ, DIM = 5, 32


def site(j, op):
    out = Zi.eye(1)
    for k in range(1, NQ + 1):
        out = kron(out, SZ if k < j else (op if k == j else I2))
    return out


G = []
for j in range(1, NQ + 1):
    G.append(site(j, SX))
    G.append(site(j, SY))

two_I, zero = Zi.eye(DIM).scaled(2), Zi.eye(DIM).scaled(0)
check("Clifford relations exact",
      all((G[a] @ G[b] + G[b] @ G[a]).equals(two_I if a == b else zero)
          for a in range(10) for b in range(10)))

prod = Zi.eye(DIM)
for g in G:
    prod = prod @ g
CHI = prod.scaled(0, -1)
PLUS = np.flatnonzero(CHI.re.diagonal() == 1)
check("dim S+ == 16", len(PLUS) == 16)

C = Zi.eye(DIM)
for a in range(2, 11, 2):
    C = C @ G[a - 1]


def word(idxs):
    out = Zi.eye(DIM)
    for a in idxs:
        out = out @ G[a - 1]
    return out


def blk(m):
    return m.sub(PLUS, PLUS)


# --------------------------------------------------------------------------
# The two tensor bases.  Index structure is identical for both:
#   T[i, j, k, l]  with i, j in the 16 and k, l in the 16bar.
# A_a pairs (i,k) with (j,l)   -- current / annihilation channel
# P_b pairs (i,j) with (k,l)   -- pairing / diquark channel
# --------------------------------------------------------------------------
# Slot convention, fixed once and used for BOTH families so they live in the
# same representation:  T[u, v, x, y]  with u, v in the 16 and x, y in the 16bar.
#
#   current:  X_a[u,v,x,y] = sum_{|A|=a} Gamma_A[x,u] * Gamma_A[y,v]
#             Gamma_A in End(S+) = 16 (x) 16bar, so [x,u] pairs one 16bar index
#             with one 16 index.  NO conjugation: sum_A Gamma_A (x) Gamma_A is
#             the Casimir-like invariant of the trace-orthonormal Lambda^a basis.
#
#   pairing:  Y_b[u,v,x,y] = sum_{|B|=b} N_B[u,v] * conj(N_B[x,y])
#             N_B = C.Gamma_B is a FORM on 16 (x) 16, hence lives in
#             16bar (x) 16bar, and conj(N_B) lives in 16 (x) 16.
#
# Putting a conjugation on the current family, or grouping its slots the way the
# pairing family groups them, silently changes the variance; the two families
# then fail to span a common space.  The global checks below catch exactly that.
def current_tensor(a: int):
    tr = np.zeros((16,) * 4, dtype=np.int64)
    ti = np.zeros((16,) * 4, dtype=np.int64)
    for idxs in combinations(range(1, 11), a):
        M = blk(word(idxs))
        if M.is_zero():
            continue
        tr += (np.einsum("xu,yv->uvxy", M.re, M.re)
               - np.einsum("xu,yv->uvxy", M.im, M.im))
        ti += (np.einsum("xu,yv->uvxy", M.re, M.im)
               + np.einsum("xu,yv->uvxy", M.im, M.re))
    return tr, ti


def pairing_tensor(b: int):
    tr = np.zeros((16,) * 4, dtype=np.int64)
    ti = np.zeros((16,) * 4, dtype=np.int64)
    for idxs in combinations(range(1, 11), b):
        N = blk(C @ word(idxs))
        if N.is_zero():
            continue
        tr += (np.einsum("uv,xy->uvxy", N.re, N.re)
               + np.einsum("uv,xy->uvxy", N.im, N.im))
        ti += (np.einsum("uv,xy->uvxy", N.im, N.re)
               - np.einsum("uv,xy->uvxy", N.re, N.im))
    return tr, ti


A = {a: current_tensor(a) for a in (0, 2, 4)}
P = {b: pairing_tensor(b) for b in (1, 3, 5)}

check("current channels 1 / 45 / 210 are all nonzero",
      all(A[a][0].any() or A[a][1].any() for a in (0, 2, 4)))
check("pairing channels 10 / 120 / 126 are all nonzero",
      all(P[b][0].any() or P[b][1].any() for b in (1, 3, 5)))


# --------------------------------------------------------------------------
# The invariant space is exactly 3-dimensional, and each set is a basis.
# Rank over F_p with p = 1 mod 4, i |-> s.  Exact integer arithmetic.
# --------------------------------------------------------------------------
PRIME = 998244353
SI = pow(3, (PRIME - 1) // 4, PRIME)
assert (SI * SI) % PRIME == PRIME - 1


def flat_mod(t):
    r, i = t
    return (r.ravel().astype(object) + SI * i.ravel().astype(object)) % PRIME


def rank_mod(vs):
    rows = [list(v) for v in vs]
    ncols, rk = len(rows[0]), 0
    for c in range(ncols):
        piv = next((x for x in range(rk, len(rows)) if rows[x][c] % PRIME), None)
        if piv is None:
            continue
        rows[rk], rows[piv] = rows[piv], rows[rk]
        inv = pow(int(rows[rk][c]), PRIME - 2, PRIME)
        rows[rk] = [(y * inv) % PRIME for y in rows[rk]]
        for x in range(len(rows)):
            if x != rk and rows[x][c] % PRIME:
                f = rows[x][c]
                rows[x] = [(y - f * z) % PRIME for y, z in zip(rows[x], rows[rk])]
        rk += 1
        if rk == len(rows):
            break
    return rk


fa = [flat_mod(A[a]) for a in (0, 2, 4)]
fp = [flat_mod(P[b]) for b in (1, 3, 5)]
check("current basis {1,45,210} is linearly independent", rank_mod(fa) == 3)
check("pairing basis {10,120,126} is linearly independent", rank_mod(fp) == 3)
check("both bases span the SAME 3-dimensional invariant space",
      rank_mod(fa + fp) == 3)


# --------------------------------------------------------------------------
# Solve for the Fierz matrix exactly over Q(i), then verify globally.
# --------------------------------------------------------------------------
def entry(t, idx):
    r, i = t
    return sp.Integer(int(r[idx])) + sp.I * sp.Integer(int(i[idx]))


# Choose three components on which the pairing basis is invertible.
all_idx = [(i, j, k, l)
           for i in range(16) for j in range(16) for k in range(16) for l in range(16)]
chosen, Mp = [], None
for idx in all_idx:
    cand = chosen + [idx]
    if len(cand) > 3:
        break
    trial = sp.Matrix([[entry(P[b], t) for b in (1, 3, 5)] for t in cand])
    if trial.rank() == len(cand):
        chosen = cand
        Mp = trial
check("found three components with an invertible pairing minor",
      len(chosen) == 3 and Mp.det() != 0)

F = {}
for a in (0, 2, 4):
    rhs = sp.Matrix([entry(A[a], t) for t in chosen])
    sol = Mp.solve(rhs)
    F[a] = [sp.nsimplify(sp.simplify(x)) for x in sol]

# Global exact verification: clear denominators and compare integer tensors.
verified = True
for a in (0, 2, 4):
    coeffs = F[a]
    den = sp.ilcm(*[sp.denom(sp.re(c)) for c in coeffs] +
                   [sp.denom(sp.im(c)) for c in coeffs])
    lhs_r = int(den) * A[a][0]
    lhs_i = int(den) * A[a][1]
    acc_r = np.zeros((16,) * 4, dtype=np.int64)
    acc_i = np.zeros((16,) * 4, dtype=np.int64)
    for c, b in zip(coeffs, (1, 3, 5)):
        cr = int(sp.re(c) * den)
        ci = int(sp.im(c) * den)
        pr, pi = P[b]
        acc_r += cr * pr - ci * pi
        acc_i += cr * pi + ci * pr
    if not (np.array_equal(lhs_r, acc_r) and np.array_equal(lhs_i, acc_i)):
        verified = False
check("Fierz identity verified EXACTLY on all 65536 components", verified)

Fmat = sp.Matrix([F[a] for a in (0, 2, 4)])
check("Fierz matrix is invertible (the two bases are genuinely equivalent)",
      sp.simplify(Fmat.det()) != 0)


# --------------------------------------------------------------------------
# THE GATE: the 126 component of adjoint (gauge-boson) exchange.
# --------------------------------------------------------------------------
f_45_126 = F[2][2]  # a = 2 is the adjoint 45 ; b = 5 is the 126
check("GATE: adjoint exchange has a NONZERO 126 component",
      sp.simplify(f_45_126) != 0)

# Report the singlet row too, as a control on normalisation.
f_1_126 = F[0][2]
f_210_126 = F[4][2]

for name, ok in CHECKS:
    print(f"  {'PASS' if ok else 'FAIL'}  {name}")
passed = sum(1 for _, ok in CHECKS if ok)
print(f"\n{passed}/{len(CHECKS)} exact checks passed")
print("\nFierz matrix rows (coefficients on [10, 120, 126]):")
for a, label in ((0, "  1 (singlet) "), (2, " 45 (adjoint) "), (4, "210          ")):
    print(f"  {label}: {[sp.nsimplify(x) for x in F[a]]}")
print(f"\n126 component of adjoint exchange  F[45][126] = {sp.nsimplify(f_45_126)}")
print(f"126 component of singlet exchange  F[1][126]  = {sp.nsimplify(f_1_126)}")
print(f"126 component of 210 exchange      F[210][126]= {sp.nsimplify(f_210_126)}")
raise SystemExit(0 if passed == len(CHECKS) else 1)
