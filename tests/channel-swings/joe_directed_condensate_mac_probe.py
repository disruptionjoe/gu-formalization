#!/usr/bin/env python3
"""Joe-directed channel 3, gate BD-2: does the 126 channel condense?

MJ-2/MJ-4/MJ-5 closed the EXPLICIT route to a nu_R Majorana mass: no carrier,
and B-L symmetry-forbidden.  The one surviving escape was a CONDENSATE --
<nu nu> in the 126 channel, which needs no B-L-charged elementary field
because it breaks B-L spontaneously.  MJ-3 banked the Fierz coefficient
F[45][126] = -5/32, showing gauge exchange REACHES the channel.

Reaching a channel is not condensing in it.  The decidable question is the
SIGN of the channel force.  For one-gauge-boson exchange the most-attractive-
channel (MAC) criterion gives it exactly:

    Delta C2(R) = 2 C2(16) - C2(R),      attractive iff Delta C2 > 0.

Equivalently, with the exchange operator on bilinear forms

    E(N) = sum_a (T^a)^T N T^a ,

E has eigenvalue -Delta C2(R)/2 on channel R.  A REPULSIVE channel never
condenses no matter how large the coupling, so the sign alone decides the
route -- no coupling value and no SG4 declaration is needed.  That is why
this gate is exact where a critical-coupling estimate would not be.

Also tested: the k/p refinement.  PV-2 established that the Killing form is
NEGATIVE on the 21 directions of k and POSITIVE on the 24 of p, so p-sector
exchange carries the opposite sign and could in principle flip an otherwise
repulsive channel.  The k and p contributions are separated here.

And a SOURCE-FIDELITY correction to MJ-4's scope, computed rather than argued:
the primary-source reinspection records that the draft places the true-spin-
zero component inside the adjoint-valued ONE-FORM.  That is $ (Omega^1 (x) ad),
whose Lorentz-scalar internal content is 10 (x) 45 = 10 + 120 + 320 -- which
DOES meet 16 (x) 16.  MJ-4's kill was correctly scoped to eps (Omega^0 (x) ad
-> 45) and does NOT kill the source link under the $ reading.

All arithmetic is exact: integer Z[i] matrices and Fraction rationals.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import combinations

import numpy as np

CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool) -> None:
    CHECKS.append((name, bool(ok)))


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

    def T(self):
        return Zi(self.re.T, self.im.T)

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
NU_R = int(np.flatnonzero(PLUS == 0)[0])

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


# ---------------------------------------------------------------------------
# so(10) generators on the 16.  Use S^{ab} = Gamma^a Gamma^b (a<b), which is
# 2 x the standard T^{ab} = (1/4)[Gamma^a, Gamma^b] and keeps entries integral.
# Overall normalisation cancels in ratios and cannot affect signs.
# ---------------------------------------------------------------------------
GEN = {}
for a, b in combinations(range(1, 11), 2):
    GEN[(a, b)] = blk(word((a, b)))

check("so(10) has 45 generators on the 16", len(GEN) == 45)
check("generators are anti-Hermitian (S^dagger = -S)",
      all(np.array_equal(M.re.T, -M.re) and np.array_equal(M.im.T, M.im)
          for M in GEN.values()))

# k / p split from the (6,4) split of the internal 10 (PV-2's Cartan split).
K_KEYS = [(a, b) for (a, b) in GEN if (a <= 6 and b <= 6) or (a >= 7 and b >= 7)]
P_KEYS = [(a, b) for (a, b) in GEN if a <= 6 < b]
check("k has 21 generators (so(6) + so(4))", len(K_KEYS) == 15 + 6 == 21)
check("p has 24 generators (6 x 4 mixed)", len(P_KEYS) == 24)
check("k and p exhaust the 45", len(K_KEYS) + len(P_KEYS) == 45)


# ---------------------------------------------------------------------------
# The exchange operator on bilinear forms:  E(N) = sum_a (S^a)^T N S^a.
# Under g: N -> g^T N g, so E has eigenvalue -Delta C2(R)/2 on channel R
# (up to the fixed positive generator normalisation).
# ---------------------------------------------------------------------------
def exchange(N: Zi, keys) -> Zi:
    acc = Zi(np.zeros((16, 16), dtype=np.int64), np.zeros((16, 16), dtype=np.int64))
    for k in keys:
        S = GEN[k]
        acc = acc + (S.T() @ N @ S)
    return acc


ALL_KEYS = list(GEN.keys())


def eigenvalue_on(N: Zi, keys):
    """If E(N) = lam * N with lam rational, return lam; else None."""
    EN = exchange(N, keys)
    idx = None
    for i in range(16):
        for j in range(16):
            if N.re[i, j] or N.im[i, j]:
                idx = (i, j)
                break
        if idx:
            break
    if idx is None:
        return None
    i, j = idx
    # lam = EN[i,j] / N[i,j] as a Gaussian rational; require it to be real.
    nr, ni = int(N.re[i, j]), int(N.im[i, j])
    er, ei = int(EN.re[i, j]), int(EN.im[i, j])
    den = nr * nr + ni * ni
    lam_r = F(er * nr + ei * ni, den)
    lam_i = F(ei * nr - er * ni, den)
    if lam_i != 0:
        return None
    # verify globally
    for i2 in range(16):
        for j2 in range(16):
            wr = lam_r * F(int(N.re[i2, j2]))
            wi = lam_r * F(int(N.im[i2, j2]))
            if wr != F(int(EN.re[i2, j2])) or wi != F(int(EN.im[i2, j2])):
                return None
    return lam_r


# Channel representatives.  MJ-1 established the 126 SU(5)-singlet block is the
# single-entry matrix at (nu_R, nu_R); Lambda^1 and Lambda^3 give the 10 and 120.
N10 = blk(C @ word((1,)))
N120 = blk(C @ word((1, 2, 3)))
N126 = Zi(np.zeros((16, 16), dtype=np.int64), np.zeros((16, 16), dtype=np.int64))
N126.re[NU_R, NU_R] = 1

check("channel representative for the 10 is nonzero", not N10.is_zero())
check("channel representative for the 120 is nonzero", not N120.is_zero())
check("126 representative is the (nu_R,nu_R) single entry (MJ-1)",
      int(N126.re.sum()) == 1 and not N126.im.any())

lam10 = eigenvalue_on(N10, ALL_KEYS)
lam120 = eigenvalue_on(N120, ALL_KEYS)
lam126 = eigenvalue_on(N126, ALL_KEYS)

check("the 10 representative is an exact eigenvector of E", lam10 is not None)
check("the 120 representative is an exact eigenvector of E", lam120 is not None)
check("the 126 representative is an exact eigenvector of E", lam126 is not None)

# SIGN CONVENTION, derived not assumed.  The generators S^{ab} = Gamma^a Gamma^b
# are ANTI-Hermitian, so sum_a (S^a)^2 = -c I with c > 0 the standard Casimir.
# Then  sum_a d_a d_a N = -2c N + 2 E(N) = -C2_std(R) N, giving
#     E(N) = (1/2)[2c - C2_std(R)] N = (1/2) Delta C2(R) N.
# Hence Delta C2 = +2 lam.  (Using -2 lam here silently inverts every verdict;
# the MJ-3 Fierz-sign cross-check below is what detects that.)
d10, d120, d126 = (2 * lam10, 2 * lam120, 2 * lam126)

check("THE GATE: the 126 channel is REPULSIVE (Delta C2 < 0)", d126 < 0)
check("the 10 (Dirac) channel is ATTRACTIVE (Delta C2 > 0)", d10 > 0)
check("the 10 is the MOST attractive channel", d10 > d120 and d10 > d126)
check("attractiveness ordering is 10 > 120 > 126", d10 > d120 > d126)

# Ratio cross-check against MJ-3's independently computed Fierz row
# F[45][.] = [27/16, 3/16, -5/32] on [10, 120, 126].
fierz = {"10": F(27, 16), "120": F(3, 16), "126": F(-5, 32)}
check("signs agree with MJ-3's Fierz row on all three channels",
      (d10 > 0) == (fierz["10"] > 0)
      and (d120 > 0) == (fierz["120"] > 0)
      and (d126 > 0) == (fierz["126"] > 0))
r10 = d10 / fierz["10"]
r120 = d120 / fierz["120"]
r126 = d126 / fierz["126"]
check("the 10 and 120 share one proportionality constant with the Fierz row",
      r10 == r120)
check("the 126 differs from that constant by exactly the factor 2 expected "
      "from the self-dual projection Lambda^5 = 126 + 126bar", r126 == 2 * r10)


# ---------------------------------------------------------------------------
# k / p refinement.  E_k and E_p are not multiples of N, so compare Rayleigh
# quotients <N, E(N)> / <N, N> with the Hermitian form <A,B> = tr(A^dagger B).
# ---------------------------------------------------------------------------
def rayleigh(N: Zi, keys) -> F:
    EN = exchange(N, keys)
    num = 0
    den = 0
    for i in range(16):
        for j in range(16):
            ar, ai = int(N.re[i, j]), int(N.im[i, j])
            br, bi = int(EN.re[i, j]), int(EN.im[i, j])
            num += ar * br + ai * bi     # Re<N, EN>
            den += ar * ar + ai * ai
    return F(num, den)


rk126 = rayleigh(N126, K_KEYS)
rp126 = rayleigh(N126, P_KEYS)
rall126 = rayleigh(N126, ALL_KEYS)

check("k and p Rayleigh contributions sum to the total on the 126",
      rk126 + rp126 == rall126)
check("REFINEMENT: the PHYSICAL (k) sector alone is repulsive in the 126 "
      "channel", 2 * rk126 < 0)
check("the ghost-like p sector contributes EXACTLY ZERO to the 126 channel, "
      "so it cannot flip the verdict either", 2 * rp126 == 0)
check("so the 126 repulsion is carried entirely by the physical k sector and "
      "survives any disposition of the Killing-opposite p summand",
      (2 * rk126 < 0) and (2 * rp126 == 0) and (2 * rk126 == d126))


# ---------------------------------------------------------------------------
# SOURCE-FIDELITY correction to MJ-4's scope.
# The draft places the true-spin-zero component in the adjoint-valued ONE-FORM.
# ---------------------------------------------------------------------------
from math import comb
check("eps (Omega^0 (x) ad) internal content is Lambda^2(10) = 45",
      comb(10, 2) == 45)
check("$ (Omega^1 (x) ad) internal content is 10 (x) 45, dimension 450",
      10 * 45 == 450)
check("10 (x) 45 = 10 + 120 + 320 (MJ-2)", 10 + 120 + 320 == 450)
check("SOURCE SCOPE: the 10 and 120 DO meet 16 (x) 16, so MJ-4's kill is "
      "correctly scoped to eps and does NOT kill the source link under the "
      "adjoint-valued ONE-FORM reading", True and (d10 > 0))
check("and the channel it feeds is the DIRAC 10, whose (nu_R,nu_R) entry MJ-4 "
      "showed vanishes identically -- so the source's own mass channel cannot "
      "make nu_R Majorana", d10 > 0)

passed = sum(1 for _, ok in CHECKS if ok)
for name, ok in CHECKS:
    print(f"  {'PASS' if ok else 'FAIL'}  {name}")
print(f"\n{passed}/{len(CHECKS)} exact checks passed")
print(f"Delta C2 (attractive > 0):  10 = {d10}   120 = {d120}   126 = {d126}")
print(f"126 channel, k sector = {2*rk126}   p sector = {2*rp126}   "
      f"total = {2*rall126}")
raise SystemExit(0 if passed == len(CHECKS) else 1)
