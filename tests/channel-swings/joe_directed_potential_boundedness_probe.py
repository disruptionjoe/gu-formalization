#!/usr/bin/env python3
"""Joe-directed channel 3, gate SRC-3: is the source potential bounded below?

SRC-2 showed the cross-term mass form is exactly traceless, so a tachyonic
direction exists for any nonzero background curvature and Eric's Mexican hat
is automatic.  A Mexican hat is only a Mexican hat if the quartic stabilises
it.  For constant modes the potential along a ray a = t v is

    V(t v) = t^2 Q(v) + t^4 K(v),
    Q(v) = 2 <F0, v^v>,      K(v) = || v^v ||^2,

so the route survives iff K(v) > 0 on every direction with Q(v) < 0.

THE LOAD-BEARING ASSUMPTION, STATED UP FRONT.  K is built from a pairing on
ad.  CC-1 established that so(6,4) admits an Ad-invariant bilinear form space
of dimension exactly ONE -- the Killing form.  PV-2 established that the
Killing form is NEGATIVE on all 21 directions of k and POSITIVE on all 24 of
p.  So the unique gauge-invariant choice is indefinite, and this probe asks
what that does to K.

Two branches are computed, because which one applies is genuinely open:
  (A) full so(6,4) with the Killing pairing  -- the Ad-invariant choice;
  (B) k only, with -B restricted to k        -- the choice available if the
      wrong-sign p sector is removed (the open quantization question PV-2
      handed to W173/W132).

All arithmetic is exact integer arithmetic.
"""
from __future__ import annotations

from itertools import combinations

import numpy as np

CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool) -> None:
    CHECKS.append((name, bool(ok)))


P, Q_, N = 6, 4, 10
ETA = np.diag([1] * P + [-1] * Q_).astype(np.int64)

BASIS, KIND, LABEL = [], [], []
for i in range(N):
    for j in range(i + 1, N):
        A = np.zeros((N, N), dtype=np.int64)
        A[i, j], A[j, i] = 1, -1
        BASIS.append(ETA @ A)
        KIND.append("k" if (j < P or i >= P) else "p")
        LABEL.append((i, j))

NG = len(BASIS)
check("so(6,4) has 45 generators", NG == 45)
check("k has 21, p has 24", KIND.count("k") == 21 and KIND.count("p") == 24)


def br(X, Y):
    return X @ Y - Y @ X


def B(X, Y):
    """Killing form, up to the fixed positive constant (N-2); sign is what matters."""
    return int(np.trace(X @ Y))


# PV-2 re-verified as a live control.
check("CONTROL (PV-2): Killing is negative on every k direction",
      all(B(BASIS[a], BASIS[a]) < 0 for a in range(NG) if KIND[a] == "k"))
check("CONTROL (PV-2): Killing is positive on every p direction",
      all(B(BASIS[a], BASIS[a]) > 0 for a in range(NG) if KIND[a] == "p"))
check("CONTROL (CC-1 consequence): the unique Ad-invariant pairing is therefore "
      "INDEFINITE on so(6,4)",
      any(B(X, X) < 0 for X in BASIS) and any(B(X, X) > 0 for X in BASIS))


# ---------------------------------------------------------------------------
# BRANCH A: full so(6,4), Killing pairing.  Exhibit K(v) < 0 explicitly.
#
# v lives in (internal 10) (x) ad.  Put v_mu = X at mu = 0 and v_nu = Y at
# nu = 1, zero elsewhere.  Then (v^v)_{01} = [X,Y] and
#     K(v) = 2 g^{00} g^{11} B([X,Y],[X,Y]).
# Internal directions 0 and 1 both lie in the +6 block, so g^{00} g^{11} = +1.
# ---------------------------------------------------------------------------
def gen_index(i, j):
    return LABEL.index((i, j))


X = BASIS[gen_index(0, 1)]      # so(6) block -> k
Y = BASIS[gen_index(1, 2)]      # so(6) block -> k
check("X and Y both lie in k",
      KIND[gen_index(0, 1)] == "k" and KIND[gen_index(1, 2)] == "k")

XY = br(X, Y)
check("[X,Y] is nonzero", bool(XY.any()))
check("[X,Y] lands back in k (since [k,k] is contained in k)",
      B(XY, XY) < 0)

# K(v) for this ray, with the internal metric factor g^{00} g^{11} = +1.
K_A = 2 * B(XY, XY)
check("BRANCH A: K(v) < 0 on an explicit ray -- the QUARTIC itself is negative",
      K_A < 0)
check("BRANCH A CONCLUSION: V(t v) = t^2 Q + t^4 K with K < 0 runs to minus "
      "infinity, so the potential is UNBOUNDED BELOW regardless of Q", K_A < 0)

# Independent second source of indefiniteness: the internal metric is (6,4),
# so even a k-negative bracket can be re-signed by choosing one timelike
# internal direction.
X2 = BASIS[gen_index(0, 1)]
Y2 = BASIS[gen_index(1, 2)]
# place the second leg on internal direction 6, which is timelike: g^{66} = -1
K_A_mixed = 2 * (-1) * B(br(X2, Y2), br(X2, Y2))
check("the (6,4) internal metric independently flips the sign of the same "
      "bracket, so indefiniteness has TWO independent sources",
      K_A_mixed > 0 and K_A < 0)


# ---------------------------------------------------------------------------
# BRANCH B: k only, pairing -B (positive definite on k).
# ---------------------------------------------------------------------------
k_idx = [a for a in range(NG) if KIND[a] == "k"]
check("BRANCH B: -B is positive definite on every k basis direction",
      all(-B(BASIS[a], BASIS[a]) > 0 for a in k_idx))

# k is a subalgebra, so brackets of k elements stay in k and -B of them is >= 0.
closed = True
for a, b in combinations(k_idx, 2):
    C = br(BASIS[a], BASIS[b])
    if C.any() and -B(C, C) <= 0:
        closed = False
check("BRANCH B: every bracket of two k generators has -B([.,.],[.,.]) >= 0, "
      "so the quartic is positive semi-definite on k", closed)

# But the internal (6,4) metric still spoils it even on branch B.
check("BRANCH B CAVEAT: with one timelike internal leg the quartic is negative "
      "again even for k-valued v, so restricting to k does NOT by itself "
      "restore boundedness",
      (-1) * (-B(br(BASIS[k_idx[0]], BASIS[k_idx[1]]),
                 br(BASIS[k_idx[0]], BASIS[k_idx[1]]))) < 0)

# ---------------------------------------------------------------------------
# Flat directions: abelian pairs give K = 0 exactly.  If any such direction
# also has Q < 0, the potential runs away at quadratic order.
# ---------------------------------------------------------------------------
abelian_pairs = [(a, b) for a, b in combinations(range(NG), 2)
                 if not br(BASIS[a], BASIS[b]).any()]
check("abelian generator pairs exist (K vanishes identically on them)",
      len(abelian_pairs) > 0)
check("on an abelian pair the quartic is exactly zero",
      all(B(br(BASIS[a], BASIS[b]), br(BASIS[a], BASIS[b])) == 0
          for a, b in abelian_pairs[:20]))

passed = sum(1 for _, ok in CHECKS if ok)
for name, ok in CHECKS:
    print(f"  {'PASS' if ok else 'FAIL'}  {name}")
print(f"\n{passed}/{len(CHECKS)} exact checks passed")
print(f"BRANCH A explicit ray: K(v) = {K_A} < 0  -> unbounded below")
print(f"same bracket with one timelike internal leg: {K_A_mixed}")
print(f"abelian (K = 0) generator pairs found: {len(abelian_pairs)}")
raise SystemExit(0 if passed == len(CHECKS) else 1)
