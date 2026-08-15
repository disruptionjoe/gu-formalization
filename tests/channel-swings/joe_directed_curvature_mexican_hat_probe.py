#!/usr/bin/env python3
"""Joe-directed channel 3, gate SRC-2: is Eric's Mexican hat automatic?

SRC-1 extracted the source mechanism verbatim (primary transcript 00:43:04):

    "If you take the norm square, you also get a term that looks like the
     unperturbed curvature, interproducted with a wedge a, which is a
     quadratic.  So if your curvature is negative, now you start to get a
     Mexican hat potential."

So the mass term for the gauge perturbation `a` is the cross term in ||F||^2
with F = F0 + da + a^a:

    Q(a) = <F0, a^a> = (1/2) F0^{mu nu A} f_{ABC} a_mu^B a_nu^C ,

with f_{ABC} = B(T_A, [T_B, T_C]) the Cartan three-form of so(6,4) and B the
Killing form.  Write M for the quadratic form in the composite index (mu, B).
Eric's condition is that M have a negative direction.

THE POINT OF THIS GATE.  M is symmetric because f and F0 are EACH
antisymmetric, and it is traceless for the same reason.  A nonzero symmetric
traceless form always has both a positive and a negative eigenvalue.  So the
Mexican hat needs no sign condition at all -- only F0 != 0.  That is stronger
than the source's own "if your curvature is negative", and it is exact.

Load-bearing claims here are exact integer arithmetic.  One illustrative
eigenvalue COUNT is computed in floating point and is explicitly labelled
NON-LOAD-BEARING; no verdict depends on it.
"""
from __future__ import annotations

from itertools import combinations

import numpy as np

CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool) -> None:
    CHECKS.append((name, bool(ok)))


P, Q_, N = 6, 4, 10
ETA = np.diag([1] * P + [-1] * Q_).astype(np.int64)

# so(6,4) basis: X = eta A with A antisymmetric integer.
BASIS = []
KIND = []
for i in range(N):
    for j in range(i + 1, N):
        A = np.zeros((N, N), dtype=np.int64)
        A[i, j], A[j, i] = 1, -1
        BASIS.append(ETA @ A)
        KIND.append("k" if (j < P or i >= P) else "p")

NG = len(BASIS)
check("so(6,4) has 45 generators", NG == 45)
check("k has 21 and p has 24", KIND.count("k") == 21 and KIND.count("p") == 24)
check("every basis element solves X^T eta + eta X = 0",
      all(np.array_equal(X.T @ ETA + ETA @ X, np.zeros((N, N), dtype=np.int64))
          for X in BASIS))


def br(X, Y):
    return X @ Y - Y @ X


# ---------------------------------------------------------------------------
# Cartan three-form f_{ABC} = B(T_A, [T_B, T_C]) with B(X,Y) = tr(XY).
# ---------------------------------------------------------------------------
COMM = {}
for b in range(NG):
    for c in range(b + 1, NG):
        COMM[(b, c)] = br(BASIS[b], BASIS[c])

f = np.zeros((NG, NG, NG), dtype=np.int64)
for (b, c), Mbc in COMM.items():
    for a in range(NG):
        v = int(np.trace(BASIS[a] @ Mbc))
        f[a, b, c] = v
        f[a, c, b] = -v

check("Cartan three-form is antisymmetric in its last two indices",
      np.array_equal(f, -np.transpose(f, (0, 2, 1))))
check("Cartan three-form is TOTALLY antisymmetric (swap first two)",
      np.array_equal(f, -np.transpose(f, (1, 0, 2))))
check("the three-form is not identically zero", bool(f.any()))

# k/p selection rule: f vanishes unless the number of p indices is 0 or 2.
viol = 0
nonzero_by_pcount = {0: 0, 1: 0, 2: 0, 3: 0}
for a in range(NG):
    for b in range(NG):
        for c in range(NG):
            if f[a, b, c]:
                pc = [KIND[a], KIND[b], KIND[c]].count("p")
                nonzero_by_pcount[pc] += 1
                if pc in (1, 3):
                    viol += 1
check("SELECTION RULE: f vanishes unless the number of p indices is 0 or 2",
      viol == 0)
check("both allowed classes actually occur (kkk and kpp), so the rule is not "
      "vacuous", nonzero_by_pcount[0] > 0 and nonzero_by_pcount[2] > 0)
check("no f component has one or three p indices",
      nonzero_by_pcount[1] == 0 and nonzero_by_pcount[3] == 0)


# ---------------------------------------------------------------------------
# The mass form.  Composite index (mu, B) with mu in the internal 10 and B in
# ad, so dim = 10 * 45 = 450 -- exactly the Lorentz-scalar content of $ that
# MJ-2/BD-2 identified.
# ---------------------------------------------------------------------------
DIMA = N * NG
check("composite index dimension is 450 = 10 x 45, matching the Lorentz-scalar "
      "content of $", DIMA == 450)


def build_M(F0):
    """M[(mu,B),(nu,C)] = sum_A F0[mu,nu,A] f[A,B,C]."""
    M = np.zeros((DIMA, DIMA), dtype=np.int64)
    nz = np.argwhere(F0 != 0)
    for mu, nu, A in nz:
        val = F0[mu, nu, A]
        blk = val * f[A]                      # 45 x 45
        M[mu * NG:(mu + 1) * NG, nu * NG:(nu + 1) * NG] += blk
    return M


# A deterministic, nonzero background curvature.  F0 must be antisymmetric in
# (mu,nu); components chosen fixed, not random.
F0 = np.zeros((N, N, NG), dtype=np.int64)


def set_F0(mu, nu, A, val):
    F0[mu, nu, A] += val
    F0[nu, mu, A] -= val


set_F0(0, 1, 0, 1)      # a k-type generator
set_F0(2, 3, 5, 2)
set_F0(0, 7, 30, 1)     # a p-type generator
set_F0(4, 8, 40, 3)

check("chosen F0 is antisymmetric in its form indices",
      np.array_equal(F0, -np.transpose(F0, (1, 0, 2))))
check("chosen F0 is nonzero", bool(F0.any()))

M = build_M(F0)

check("M is nonzero", bool(M.any()))
check("M is SYMMETRIC (f and F0 are each antisymmetric)",
      np.array_equal(M, M.T))
check("THE GATE: M is exactly TRACELESS", int(np.trace(M)) == 0)

# tr(M^2) > 0 certifies M has nonzero real spectrum; with trace 0 that forces
# eigenvalues of BOTH signs.  Integer arithmetic throughout.
tr_M2 = int(np.trace(M @ M))
check("tr(M^2) > 0, so M has a nonzero real spectrum", tr_M2 > 0)
check("CONCLUSION: symmetric + traceless + nonzero forces BOTH a positive and "
      "a negative eigenvalue, so a tachyonic direction always exists",
      int(np.trace(M)) == 0 and tr_M2 > 0 and np.array_equal(M, M.T))

# Structural control: the tracelessness is forced, not an artifact of this F0.
# tr M = sum_{mu,A} F0[mu,mu,A] f[A,B,B]; both factors vanish identically.
check("CONTROL: f[A,B,B] = 0 for every A,B (so the trace vanishes for ANY F0)",
      all(f[a, b, b] == 0 for a in range(NG) for b in range(NG)))
check("CONTROL: F0[mu,mu,A] = 0 for every mu,A by antisymmetry",
      all(F0[mu, mu, A] == 0 for mu in range(N) for A in range(NG)))

# A purely p-valued background gives a mass form with NO k-k or p-p diagonal
# blocks, by the selection rule.
F0p = np.zeros((N, N, NG), dtype=np.int64)
pidx = [i for i, kd in enumerate(KIND) if kd == "p"]
F0p[0, 1, pidx[0]] = 1
F0p[1, 0, pidx[0]] = -1
Mp = build_M(F0p)
kk = pp = 0
for B in range(NG):
    for C in range(NG):
        blkval = int(np.abs(Mp[:, :][np.ix_(
            [mu * NG + B for mu in range(N)],
            [nu * NG + C for nu in range(N)])]).sum())
        if blkval:
            if KIND[B] == "k" and KIND[C] == "k":
                kk += 1
            if KIND[B] == "p" and KIND[C] == "p":
                pp += 1
check("a purely p-valued F0 produces NO k-k and NO p-p ad-blocks -- it couples "
      "only k to p", kk == 0 and pp == 0)
check("and that Mp is itself nonzero (non-vacuous)", bool(Mp.any()))

# NON-LOAD-BEARING illustration only.
evs = np.linalg.eigvalsh(M.astype(np.float64))
neg = int((evs < -1e-8).sum())
pos = int((evs > 1e-8).sum())

passed = sum(1 for _, ok in CHECKS if ok)
for name, ok in CHECKS:
    print(f"  {'PASS' if ok else 'FAIL'}  {name}")
print(f"\n{passed}/{len(CHECKS)} exact checks passed")
print(f"tr(M) = {int(np.trace(M))} (exact)   tr(M^2) = {tr_M2} (exact)")
print(f"[NON-LOAD-BEARING float illustration] negative directions: {neg}, "
      f"positive: {pos}, of {DIMA}")
raise SystemExit(0 if passed == len(CHECKS) else 1)
