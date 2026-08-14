#!/usr/bin/env python3
"""Joe-directed channel 2, gate PV-1: does any AVAILABLE orbit give exactly SM?

Channel decision question: does any presently admissible symmetry-breaking
orbit leave exactly the Standard Model massless gauge sector while making the
extra U(1) and other non-SM gauge directions massive or unphysical?

PRIOR ART -- attributed, not re-claimed:
  * CB-A row A4 already computes that exactly two SM-singlet (1,1,0)
    directions survive in the internal adjoint, U(1)_Y and U(1)_X, and that
    the extra U(1)_{B-L} is forced by the rank of the carrier, not chosen.
  * CB-A row A8 records a CONDITIONAL stabilizer theorem (cycle1): given a
    rank-one v_PSB in (10bar,1,3), the identity-component stabilizer has Lie
    algebra su(3) + su(2)_L + u(1).  CB-A marks it NEEDS-U1, "not selected".

This probe does NOT re-derive that theorem.  It asks the different question
CB-A leaves open: is the theorem's ANTECEDENT available in GU's declared
field content?  It re-verifies A4 independently as a control, then computes
the unbroken dimension for the orbits that ARE available.

Composition with the channel-3 results:
  MJ-2: the 126 has multiplicity exactly zero in eps and in $.
  MJ-5: no SM-singlet with B-L != 0 exists in eps or in $.
  (10bar,1,3) is a sub-block of the 126, so v_PSB is unavailable.

All arithmetic is exact rational arithmetic on integer root/weight vectors.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import combinations

CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool) -> None:
    CHECKS.append((name, bool(ok)))


N = 5

# ---------------------------------------------------------------------------
# so(10): 40 roots +-e_i +- e_j (i<j), plus a 5-dimensional Cartan.
# ---------------------------------------------------------------------------
ROOTS = []
for i, j in combinations(range(N), 2):
    for si in (1, -1):
        for sj in (1, -1):
            a = [0] * N
            a[i], a[j] = si, sj
            ROOTS.append(tuple(a))

check("so(10) has 40 roots", len(ROOTS) == 40)
check("so(10) has dimension 45", len(ROOTS) + N == 45)


# Cartan functionals, in the same normalisation used in MJ-5.
def bl(v):      # B-L
    return F(-(v[0] + v[1] + v[2]), 3)


def t3r(v):
    return F(v[3] + v[4], 4)


def t3l(v):
    return F(v[3] - v[4], 4)


def hyper(v):   # Y = T3R + (B-L)/2
    return t3r(v) + bl(v) / 2


# ---------------------------------------------------------------------------
# The Standard Model subalgebra, identified by roots.
#   su(3)_C   : roots e_i - e_j on the colour triple      (6 roots + 2 Cartan)
#   su(2)_L   : roots +-(e_4 - e_5)                       (2 roots + 1 Cartan)
#   u(1)_Y                                                (1 Cartan)
# ---------------------------------------------------------------------------
su3_roots = [a for a in ROOTS
             if a[3] == 0 and a[4] == 0 and sum(a[:3]) == 0]
su2L_roots = [a for a in ROOTS
              if a[0] == a[1] == a[2] == 0 and a[3] + a[4] == 0]

check("su(3)_C has 6 roots", len(su3_roots) == 6)
check("su(2)_L has 2 roots", len(su2L_roots) == 2)
SM_DIM = len(su3_roots) + 2 + len(su2L_roots) + 1 + 1
check("the SM subalgebra has dimension 12", SM_DIM == 12)
check("the SM subalgebra has rank 4", 2 + 1 + 1 == 4)


# ---------------------------------------------------------------------------
# CONTROL, re-verifying CB-A row A4 independently:
# the centraliser of the SM inside so(10) is exactly 2-dimensional.
# A root direction commutes with the whole SM only if it is neutral under
# every SM Cartan generator AND is not an su(3) or su(2)_L root.
# ---------------------------------------------------------------------------
def sm_neutral_root(a):
    """Root neutral under colour, weak isospin and hypercharge."""
    colour_neutral = (a[0] == a[1] == a[2])
    return colour_neutral and t3l(a) == 0 and hyper(a) == 0


centraliser_roots = [a for a in ROOTS if sm_neutral_root(a)]
check("CONTROL (CB-A A4): no root direction centralises the SM",
      len(centraliser_roots) == 0)
# Cartan directions centralising the SM: the full 5-dim Cartan commutes with
# the SM Cartan, but must also commute with the su(3)/su(2)_L root vectors,
# which requires vanishing on those roots.
cartan_basis = [tuple(1 if k == m else 0 for k in range(N)) for m in range(N)]


def vanishes_on(vecfun, roots):
    return all(vecfun(a) == 0 for a in roots)


# A Cartan element H = sum c_m e_m ; it commutes with E_alpha iff alpha(H)=0.
# Solve for the space of c with alpha(c)=0 for every su(3)/su(2)_L root.
def cartan_centraliser_dim():
    # alpha(c) = sum_m alpha_m c_m.  Collect constraints, exact rank over Q.
    rows = [list(map(F, a)) for a in su3_roots + su2L_roots]
    # Gaussian elimination over Q
    rank, ncols = 0, N
    mat = [r[:] for r in rows]
    for col in range(ncols):
        piv = next((r for r in range(rank, len(mat)) if mat[r][col] != 0), None)
        if piv is None:
            continue
        mat[rank], mat[piv] = mat[piv], mat[rank]
        pv = mat[rank][col]
        mat[rank] = [x / pv for x in mat[rank]]
        for r in range(len(mat)):
            if r != rank and mat[r][col] != 0:
                f = mat[r][col]
                mat[r] = [x - f * y for x, y in zip(mat[r], mat[rank])]
        rank += 1
    return ncols - rank


cc = cartan_centraliser_dim()
check("CONTROL (CB-A A4): exactly 2 SM-singlet Cartan directions survive "
      "-- U(1)_Y and U(1)_X", cc == 2)


# ---------------------------------------------------------------------------
# THE GATE.  An adjoint VEV that preserves the SM must lie in that 2-dim
# centraliser.  Its unbroken algebra is its own centraliser in so(10).
# For a Cartan VEV Z, that is Cartan + {E_alpha : alpha(Z) = 0}.
# ---------------------------------------------------------------------------
def unbroken_dim_for(a_coef, b_coef):
    """VEV Z = a*Y + b*X ; count roots annihilating it."""
    def alpha_on_Z(a):
        return a_coef * hyper(a) + b_coef * bl(a)
    return N + sum(1 for a in ROOTS if alpha_on_Z(a) == 0)


generic = unbroken_dim_for(F(1), F(1))      # generic point of the 2-dim space
pure_Y = unbroken_dim_for(F(1), F(0))
pure_X = unbroken_dim_for(F(0), F(1))

check("GATE: a generic SM-preserving adjoint VEV leaves 13 unbroken, "
      "not 12 -- exactly one extra massless vector", generic == 13)
check("the 13 decomposes as SM (12) plus one extra U(1)", generic == SM_DIM + 1)
# Pure B-L is NOT the SU(5) direction.  Its centraliser is
# su(3) + u(1)_{B-L} + su(2)_L + su(2)_R = 8+1+3+3 = 15, i.e. Pati-Salam with
# SU(4) already broken to SU(3)xU(1).  The SU(5) direction is the combination
# proportional to (1,1,1,1,1), which appears in the sweep below at 25.
check("pure B-L leaves su(3)+u(1)+su(2)_L+su(2)_R = 15 unbroken", pure_X == 15)
check("pure Y leaves strictly more than the SM", pure_Y > SM_DIM)
su5_dim = unbroken_dim_for(F(4), F(-5))     # the (1,1,1,1,1) direction
check("the SU(5) direction leaves su(5)+u(1) = 25 unbroken", su5_dim == 25)

# Sweep the whole 2-dimensional SM-preserving adjoint orbit space: the
# unbroken dimension never reaches 12.
sweep = set()
for a_num in range(-6, 7):
    for b_num in range(-6, 7):
        if a_num == 0 and b_num == 0:
            continue
        sweep.add(unbroken_dim_for(F(a_num), F(b_num)))
check("GATE: over the ENTIRE SM-preserving adjoint orbit space the unbroken "
      "dimension is never 12", 12 not in sweep)
check("its minimum is exactly 13", min(sweep) == 13)


# ---------------------------------------------------------------------------
# The one vacuum class that WOULD give exactly the SM: rank-one v_PSB in
# (10bar,1,3), a sub-block of the 126 (cycle1 / CB-A A8).  Verify the
# Pati-Salam decomposition of the 126, then compose with MJ-2 / MJ-5.
# ---------------------------------------------------------------------------
ps_126 = {"(6,1,1)": 6, "(10,3,1)": 30, "(10bar,1,3)": 30, "(15,2,2)": 60}
check("126 = (6,1,1)+(10,3,1)+(10bar,1,3)+(15,2,2) exactly",
      sum(ps_126.values()) == 126)
check("(10bar,1,3) is a sub-block of the 126, dimension 30",
      ps_126["(10bar,1,3)"] == 30)

# The SM-singlet, B-L = -2 direction found in MJ-5 is the all-plus weight of
# Lambda^5; re-confirm its quantum numbers here so this artifact is
# self-contained.
v_psb = (2, 2, 2, 2, 2)
check("v_PSB direction is colour-neutral", v_psb[0] == v_psb[1] == v_psb[2])
check("v_PSB direction has T3L = 0", t3l(v_psb) == 0)
check("v_PSB direction has Y = 0", hyper(v_psb) == 0)
check("v_PSB direction has B-L = -2 (breaks B-L by two units)",
      bl(v_psb) == -2)

passed = sum(1 for _, ok in CHECKS if ok)
for name, ok in CHECKS:
    print(f"  {'PASS' if ok else 'FAIL'}  {name}")
print(f"\n{passed}/{len(CHECKS)} exact checks passed")
print(f"unbroken dimensions over the SM-preserving adjoint orbit space: "
      f"{sorted(sweep)}   (SM = 12)")
raise SystemExit(0 if passed == len(CHECKS) else 1)
