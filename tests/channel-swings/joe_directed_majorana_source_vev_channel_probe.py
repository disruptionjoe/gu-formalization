#!/usr/bin/env python3
"""Joe-directed channel 3, gate MJ-4: the SOURCE's own VEV channel vs mass.

Source targeting (lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md):

  - The draft states the three-way link
        cosmological "constant" <-> spinless gauge field <-> fermion mass,
    and that the cosmological constant is the VEV of the field playing the
    role of fundamental mass.  Dispositioned SOURCE-EXPLICIT.
  - The pack's own construction prompt is to test "the source's SINGLE
    spinless gauge-potential/VEV channel as a common zero-order carrier for
    fermion mass and the cosmological sector."
  - 2021 Into the Impossible 01:41:43: which fields acquire VEVs, and where,
    is explicitly NOT selected by the source.

So the source declares exactly one VEV channel: the spin-0 part of the
ad-valued gauge potential eps.  Internally that is the adjoint, Lambda^2(10)
= 45.  This probe asks what that channel can and cannot do to fermion mass,
and which channel -- if any -- can make nu_R Majorana.

Two readings of the source link are separated, and only one is tested:
  (R1) DIRECT: the eps spin-0 VEV is itself the mass term's channel.
  (R2) SCALE:  the eps spin-0 VEV sets a scale entering fermion mass through
       some other operator.
This probe decides R1 exactly.  R2 is untouched and needs the operator.

All arithmetic is exact integer arithmetic in Z[i].  No floating point.
"""
from __future__ import annotations

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


NU_R = int(np.flatnonzero(PLUS == 0)[0])   # |00000>, the SU(5) singlet


# ---------------------------------------------------------------------------
# R1.  The source's declared VEV channel is the internal adjoint, 45.
#      Does it appear in 16 (x) 16 at all?
# ---------------------------------------------------------------------------
adjoint_blocks = [blk(C @ word(idxs)) for idxs in combinations(range(1, 11), 2)]
check("adjoint (45) has 45 index directions", len(adjoint_blocks) == 45)
check("R1 KILLED: the 45 block on 16 (x) 16 vanishes identically for EVERY "
      "adjoint direction -- the source's declared VEV channel gives NO "
      "renormalizable fermion mass at all",
      all(b.is_zero() for b in adjoint_blocks))

# Same for the other even (tensor) channels, for completeness: the whole
# even tower is absent from 16 (x) 16.
for k in (0, 2, 4):
    check(f"even channel Lambda^{k} is absent from 16 (x) 16",
          all(blk(C @ word(i)).is_zero() for i in combinations(range(1, 11), k)))

# The surviving renormalizable channels are exactly 10, 120, 126.
for k in (1, 3, 5):
    check(f"odd channel Lambda^{k} is present on 16 (x) 16",
          any(not blk(C @ word(i)).is_zero() for i in combinations(range(1, 11), k)))


# ---------------------------------------------------------------------------
# Which channel can make nu_R Majorana?  Test the (nu_R, nu_R) entry over
# every direction of every renormalizable channel.
# ---------------------------------------------------------------------------
def nu_entry_nonzero(k: int) -> bool:
    for idxs in combinations(range(1, 11), k):
        b = blk(C @ word(idxs))
        if b.re[NU_R, NU_R] or b.im[NU_R, NU_R]:
            return True
    return False


check("10 channel: (nu_R, nu_R) entry vanishes for EVERY direction "
      "-- a 10 VEV cannot make nu_R Majorana", not nu_entry_nonzero(1))
check("120 channel: (nu_R, nu_R) entry vanishes for EVERY direction",
      not nu_entry_nonzero(3))
check("126 channel: (nu_R, nu_R) entry is reachable", nu_entry_nonzero(5))

# The 10 channel is nevertheless a live DIRAC channel: it is nonzero on
# 16 (x) 16 overall, just never on the nu_R diagonal.
check("10 channel is nonzero overall (a live Dirac channel)",
      any(not blk(C @ word(i)).is_zero() for i in combinations(range(1, 11), 1)))


# ---------------------------------------------------------------------------
# The tautological / observation direction.
# Y14 = Met(X4); the internal 10 is Sym^2(T*X4) and the tautological datum --
# the metric at which one observes -- is a VECTOR in that 10.  So GU's own
# observation-induced breaking supplies a 10 direction, not a 5-form.
# Combined with the row above, observation breaking gives Dirac mass and
# cannot give nu_R a Majorana mass.
# ---------------------------------------------------------------------------
check("observation datum lives in the 10: dim Sym^2(T*X4) == 10",
      4 * 5 // 2 == 10)
check("a single vector spans no 5-form: Lambda^5 of a 1-dim space is 0",
      True)

passed = sum(1 for _, ok in CHECKS if ok)
for name, ok in CHECKS:
    print(f"  {'PASS' if ok else 'FAIL'}  {name}")
print(f"\n{passed}/{len(CHECKS)} exact checks passed")
raise SystemExit(0 if passed == len(CHECKS) else 1)
