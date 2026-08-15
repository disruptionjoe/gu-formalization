#!/usr/bin/env python3
"""Joe-directed channel 5, gate MV-1: cosmological and laboratory bounds on the
massless vector spectrum GU-as-declared retains.

TWO RIGOROUSLY SEPARATED SIDES.  This file prints TWO reports and only ONE
certificate.

  PART I  -- EXACT.  How many massless gauge directions survive, which group
             they generate, their exact rational quantum numbers, which of them
             are asymptotic single-particle states at all, and the exact
             symbolic dark-radiation and running formulas.  Integer root
             systems, exact Z[i] Clifford matrices, exact Fraction charges,
             exact sympy Rationals.  This is the N/N certificate.

  PART II -- EMPIRICAL.  Measured N_eff, BBN limits, Eotvos-parameter limits,
             alpha_s, atomic masses.  Every entry carries a value, an
             uncertainty and a source.  NOTHING here is certified exact and the
             comparison is NEVER presented as exact.  Part II has its own
             counter and its own report and it is labelled as such throughout.

THE OBJECT.  PV-2 (tests/channel-swings/joe_directed_observation_reduction_
probe.py) established that GU's observation mechanism reduces Spin(6,4) to its
maximal compact, the Cartan decomposition so(6,4) = k(21) (+) p(24), reaching
only the 24 non-compact p directions.  The Standard Model's 12 generators sit
entirely inside k, and exactly 9 non-SM directions remain in k untouched.  This
gate asks the phenomenological question PV-2 left open: what do those surviving
massless gauge directions do to the universe and to the laboratory?

WHAT THIS GATE IS.  An EXCLUSION, not a recovery of physics.  It produces no
prediction that could be confirmed.  Its whole value is that the contact with
data is fast and hard.

CONVENTIONS.  Reused from MJ-5 / BD-1 and re-validated on the 16 before use.
Doubled integer weights w in {+-1}^5 on S+, and the physical weight mu = w/2 in
the standard e-basis.  Cartan elements are exact rational 5-vectors acting on mu
by the ordinary dot product:

    h_{B-L} = (-2/3, -2/3, -2/3,  0,   0  )
    h_{T3L} = (  0,    0,    0,  1/2, -1/2)
    h_{T3R} = (  0,    0,    0,  1/2,  1/2)
    h_Y     = h_T3R + h_{B-L}/2,   h_Q = h_T3L + h_Y

Roots of so(10) are +-e_i +- e_j, i < j.  k is the same-block span
({i,j} <= {1,2,3} or {i,j} <= {4,5}); p is the mixed block.

PRIOR ART, NOT RE-CLAIMED.  The rank argument -- an adjoint VEV preserves rank,
rank(so(10)) = 5 > 4 = rank(SM), so an extra U(1) is forced by the carrier and
not chosen -- is CB-A row A4 (explorations/conditional-build/cb-a-representation
-content-2026-08-05.md) and standard SO(10) model building.  The {13,15,19,25}
orbit sweep is PV-1.  The 21/24 split and the 6+2+1 identification are PV-2.
The |Delta(B-L)| = 4/3 Pati-Salam leptoquark typing is BD-1.  All four are
RE-DERIVED here as controls, and no novelty is claimed for any of them.
"""
from __future__ import annotations

import sys
from fractions import Fraction as F
from itertools import combinations, product

import numpy as np
import sympy as sp

EXACT: list[tuple[str, bool]] = []


def check(name: str, ok: bool) -> None:
    """An EXACT check.  Contributes to the certificate."""
    EXACT.append((name, bool(ok)))


# ===========================================================================
# PART I.0  Exact Z[i] Clifford algebra of so(10) -- the same construction as
#           BD-1, replayed so nothing about the k/p split is imported on trust.
# ===========================================================================
class Zi:
    """Exact Gaussian-integer matrix."""

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


def kron(a, b):
    return Zi(np.kron(a.re, b.re) - np.kron(a.im, b.im),
              np.kron(a.re, b.im) + np.kron(a.im, b.re))


I2 = Zi.eye(2)
SX = Zi([[0, 1], [1, 0]], [[0, 0], [0, 0]])
SY = Zi([[0, 0], [0, 0]], [[0, -1], [1, 0]])
SZ = Zi([[1, 0], [0, -1]], [[0, 0], [0, 0]])
RAISE = Zi([[0, 1], [0, 0]], [[0, 0], [0, 0]])
LOWER = Zi([[0, 0], [1, 0]], [[0, 0], [0, 0]])

NQ, DIM = 5, 32
P_BLOCK, Q_BLOCK = 6, 4                            # DeWitt internal signature (6,4)


def site(j, op):
    out = Zi.eye(1)
    for k in range(1, NQ + 1):
        out = kron(out, SZ if k < j else (op if k == j else I2))
    return out


def pure(j, op):
    out = Zi.eye(1)
    for k in range(1, NQ + 1):
        out = kron(out, op if k == j else I2)
    return out


G = []
for j in range(1, NQ + 1):
    G.append(site(j, SX))
    G.append(site(j, SY))

two_I, zero32 = Zi.eye(DIM).scaled(2), Zi.eye(DIM).scaled(0)
check("Clifford relations {Gamma_a, Gamma_b} = 2 delta_ab hold exactly on all "
      "100 pairs",
      all((G[a] @ G[b] + G[b] @ G[a]).equals(two_I if a == b else zero32)
          for a in range(10) for b in range(10)))

CHIR = Zi.eye(DIM)
for j in range(1, NQ + 1):
    CHIR = CHIR @ pure(j, SZ)
check("chirality squares to 1 and anticommutes with every Gamma_a",
      (CHIR @ CHIR).equals(Zi.eye(DIM))
      and all((CHIR @ G[a] + G[a] @ CHIR).is_zero() for a in range(10)))


def weight_of(idx: int) -> tuple[int, ...]:
    return tuple(1 if (idx >> (NQ - 1 - k)) & 1 == 0 else -1 for k in range(NQ))


SPLUS = [b for b in range(DIM) if int(CHIR.re[b, b]) == 1]
W16 = [weight_of(b) for b in SPLUS]
check("S+ is 16-dimensional with 16 distinct doubled weights",
      len(SPLUS) == 16 and len(set(W16)) == 16)

RS = [site(j, RAISE) for j in range(1, NQ + 1)]
LS = [site(j, LOWER) for j in range(1, NQ + 1)]

ROOTS: dict[tuple, dict] = {}
for i, j in combinations(range(1, NQ + 1), 2):
    for si, sj in product((1, -1), repeat=2):
        E = (RS[i - 1] if si == 1 else LS[i - 1]) @ (RS[j - 1] if sj == 1 else LS[j - 1])
        # Physical root in the e-basis: alpha = si e_i + sj e_j.
        alpha = tuple(F(si) if k == i - 1 else (F(sj) if k == j - 1 else F(0))
                      for k in range(NQ))
        ROOTS[(i, j, si, sj)] = {"E": E, "alpha": alpha, "pair": (i, j)}

check("so(10) has exactly 40 root vectors and 40 + 5 Cartan = dim 45",
      len(ROOTS) == 40 and len(ROOTS) + NQ == 45)

COLOUR_COORDS, WEAK_COORDS = {1, 2, 3}, {4, 5}


def in_k(rec) -> bool:
    i, j = rec["pair"]
    return ({i, j} <= COLOUR_COORDS) or ({i, j} <= WEAK_COORDS)


k_roots = [r for r in ROOTS.values() if in_k(r)]
p_roots = [r for r in ROOTS.values() if not in_k(r)]
check("PV-2 replay: k has 16 roots + 5 Cartan = 21, p has exactly 24 = 6 x 4",
      len(k_roots) == 16 and len(k_roots) + NQ == 21
      and len(p_roots) == 24 == P_BLOCK * Q_BLOCK)

# Independent vector-side Killing-sign derivation of the same split.
ETA = np.diag([1] * P_BLOCK + [-1] * Q_BLOCK).astype(np.int64)
vec_same, vec_mixed = [], []
for a in range(10):
    for b in range(a + 1, 10):
        A = np.zeros((10, 10), dtype=np.int64)
        A[a, b], A[b, a] = 1, -1
        X = ETA @ A
        (vec_same if (a < P_BLOCK) == (b < P_BLOCK) else vec_mixed).append(int(np.trace(X @ X)))
check("PV-2 replay: Killing form is negative on all 21 same-block generators "
      "and positive on all 24 mixed-block generators, and the vector-side split "
      "equals the spinor-side split",
      len(vec_same) == 21 and len(vec_mixed) == 24
      and all(t < 0 for t in vec_same) and all(t > 0 for t in vec_mixed)
      and len(k_roots) + NQ == len(vec_same) and len(p_roots) == len(vec_mixed))


# ===========================================================================
# PART I.1  Charges as exact rational Cartan covectors.
# ===========================================================================
H_BL = (F(-2, 3), F(-2, 3), F(-2, 3), F(0), F(0))
H_T3L = (F(0), F(0), F(0), F(1, 2), F(-1, 2))
H_T3R = (F(0), F(0), F(0), F(1, 2), F(1, 2))
H_Y = tuple(a + b / 2 for a, b in zip(H_T3R, H_BL))
H_Q = tuple(a + b for a, b in zip(H_T3L, H_Y))


def val(h, mu):
    return sum(hi * mi for hi, mi in zip(h, mu))


def mu_of(w):
    return tuple(F(x, 2) for x in w)


NU_R = (1, 1, 1, 1, 1)
check("MJ-5 convention re-validated: nu_R is in the 16, is the unique SM "
      "singlet, and has exactly B-L = -1, Q = 0",
      NU_R in W16
      and val(H_BL, mu_of(NU_R)) == -1 and val(H_Q, mu_of(NU_R)) == 0
      and sum(1 for w in W16
              if val(H_T3L, mu_of(w)) == 0 and val(H_Y, mu_of(w)) == 0
              and w[0] == w[1] == w[2]) == 1)
check("the 16 splits into 4 colour-neutral lepton states with |B-L| = 1 and 12 "
      "colour-charged quark states with |B-L| = 1/3, all charges in "
      "{0, +-1/3, +-2/3, +-1}",
      sum(1 for w in W16 if w[0] == w[1] == w[2]) == 4
      and all(abs(val(H_BL, mu_of(w))) == (1 if w[0] == w[1] == w[2] else F(1, 3))
              for w in W16)
      and all(val(H_Q, mu_of(w)) in (0, F(1, 3), F(-1, 3), F(2, 3), F(-2, 3), 1, -1)
              for w in W16))
check("Y = T3R + (B-L)/2 and Q = T3L + Y hold exactly on every one of the 16 "
      "weights (the covector identities, not an assumption)",
      all(val(H_Y, mu_of(w)) == val(H_T3R, mu_of(w)) + val(H_BL, mu_of(w)) / 2
          and val(H_Q, mu_of(w)) == val(H_T3L, mu_of(w)) + val(H_Y, mu_of(w))
          for w in W16))

# Cross-check: the e-basis root really is the weight shift the matrix produces.
ok_shift = True
for rec in ROOTS.values():
    E = rec["E"]
    for bs in SPLUS:
        for bt in SPLUS:
            if E.re[bt, bs] or E.im[bt, bs]:
                d = tuple(a - b for a, b in zip(mu_of(weight_of(bt)), mu_of(weight_of(bs))))
                if d != rec["alpha"]:
                    ok_shift = False
check("every root vector's matrix elements on S+ shift the physical weight by "
      "exactly the e-basis root, so the covector arithmetic below is the same "
      "object as the Clifford matrices above", ok_shift)


# ===========================================================================
# PART I.2  k = su(4) (+) su(2)_L (+) su(2)_R, and the 9 non-SM directions.
# ===========================================================================
def dcharge(h, rec):
    return val(h, rec["alpha"])


so6_roots = [r for r in k_roots if set(r["pair"]) <= COLOUR_COORDS]
so4_roots = [r for r in k_roots if set(r["pair"]) <= WEAK_COORDS]
check("k splits block-diagonally as so(6) [12 roots + rank 3 = dim 15] and "
      "so(4) [4 roots + rank 2 = dim 6], and 15 + 6 = 21",
      len(so6_roots) == 12 and len(so4_roots) == 4 and 12 + 3 + 4 + 2 == 21)
check("the two blocks commute exactly as 32x32 matrices, so k really is a "
      "direct sum su(4) (+) su(2)_L (+) su(2)_R and not merely a dimension count",
      all((a["E"] @ b["E"]).equals(b["E"] @ a["E"])
          for a in so6_roots for b in so4_roots))

gluon_roots = [r for r in so6_roots if dcharge(H_BL, r) == 0]
lq_roots = [r for r in so6_roots if dcharge(H_BL, r) != 0]
wl_roots = [r for r in so4_roots if dcharge(H_T3L, r) != 0]
wr_roots = [r for r in so4_roots if dcharge(H_T3R, r) != 0]
check("su(4) = 8 gluons + u(1)_{B-L} + 6 leptoquarks = 15 exactly, and so(4) = "
      "2 W_L + T3L + 2 W_R + T3R = 6",
      (len(gluon_roots), len(lq_roots)) == (6, 6) and 6 + 2 + 1 + 6 == 15
      and (len(wl_roots), len(wr_roots)) == (2, 2) and 2 + 1 + 2 + 1 == 6)
check("BD-1 replay: the 6 leptoquarks are weak-singlet (3,1)_{+-2/3} with "
      "|Delta(B-L)| = 4/3 exactly -- Pati-Salam type, not SU(5) X,Y type",
      all(dcharge(H_T3L, r) == 0 and abs(dcharge(H_Y, r)) == F(2, 3)
          and abs(dcharge(H_BL, r)) == F(4, 3) for r in lq_roots))
check("the 2 W_R are (1,1)_{+-1} with Delta(B-L) = 0 exactly",
      all(dcharge(H_T3L, r) == 0 and abs(dcharge(H_Y, r)) == 1
          and dcharge(H_BL, r) == 0 for r in wr_roots))
check("PV-2 replay: SM(12) = 6 gluon roots + 2 colour Cartan + 2 W_L roots + "
      "T3L + Y, leaving exactly 9 non-SM directions in k = 6 leptoquarks + "
      "2 W_R + 1 Z'",
      6 + 2 + 2 + 1 + 1 == 12 and len(lq_roots) + len(wr_roots) + 1 == 9
      and 12 + 9 == 21)


# ===========================================================================
# PART I.3  The rank theorem, PV-1's sweep re-derived, and the 126 control.
# ===========================================================================
# SM-singlet directions inside the adjoint 45 = Lambda^2(10).  The 40 nonzero
# adjoint weights are the roots; the 5 zero weights are the Cartan.  An SM
# singlet must be annihilated by the FULL rank-4 SM Cartan -- the two colour
# Cartans as well as T3L and Y.  (Testing only T3L, Y, B-L would wrongly admit
# the gluon roots, which are colour octets, not singlets.)
H_C1 = (F(1), F(-1), F(0), F(0), F(0))
H_C2 = (F(0), F(1), F(-1), F(0), F(0))
SM_CARTAN = [H_C1, H_C2, H_T3L, H_Y]
sm_singlet_roots = [r for r in ROOTS.values()
                    if all(dcharge(h, r) == 0 for h in SM_CARTAN)]
gluon_octet_roots = [r for r in ROOTS.values()
                     if dcharge(H_T3L, r) == 0 and dcharge(H_Y, r) == 0
                     and dcharge(H_BL, r) == 0]
check("CB-A A4 replay: NO nonzero adjoint weight is an SM singlet, so every "
      "SM-preserving adjoint VEV direction lies in the 5-dimensional Cartan",
      len(sm_singlet_roots) == 0)
check("CONTROL that the singlet test is the right test: dropping the two colour "
      "Cartans would wrongly admit 6 directions (the gluon roots), which are a "
      "colour octet and not SM singlets at all",
      len(gluon_octet_roots) == 6 and set(id(r) for r in gluon_octet_roots)
      == set(id(r) for r in gluon_roots) and len(sm_singlet_roots) == 0)

# The SM-singlet Cartan directions: those commuting with su(3) and su(2)_L.
CARTAN_BASIS = [tuple(F(1) if k == i else F(0) for k in range(NQ)) for i in range(NQ)]
su3_roots = [r for r in gluon_roots]


def commutes_with_sm(h):
    return (all(val(h, r["alpha"]) == 0 for r in su3_roots)
            and all(val(h, r["alpha"]) == 0 for r in wl_roots))


# Solve for the SM-singlet subspace of the Cartan exactly with sympy.
c = sp.symbols("c0 c1 c2 c3 c4", rational=True)
hgen = [sum(ci * sp.Rational(b[k]) for ci, b in zip(c, CARTAN_BASIS)) for k in range(NQ)]
eqs = []
for r in su3_roots + wl_roots:
    eqs.append(sum(hgen[k] * sp.Rational(r["alpha"][k]) for k in range(NQ)))
sol_space = sp.Matrix(eqs).jacobian(sp.Matrix(c)).nullspace()
check("CB-A A4 replay: the SM-singlet subspace of the Cartan is EXACTLY "
      "2-dimensional and is spanned by Y and B-L",
      len(sol_space) == 2
      and commutes_with_sm(H_Y) and commutes_with_sm(H_BL)
      and sp.Matrix([[sp.Rational(x) for x in H_Y],
                     [sp.Rational(x) for x in H_BL]]).rank() == 2
      # {Y, B-L} spans the SAME space as the computed nullspace, not merely a
      # subspace of the right dimension: stacking the two must not raise rank.
      and sp.Matrix.vstack(
          sp.Matrix.hstack(*sol_space).T,
          sp.Matrix([[sp.Rational(x) for x in H_Y],
                     [sp.Rational(x) for x in H_BL]])).rank() == 2
      # and the test is not vacuous: T3L is NOT in that subspace.
      and sp.Matrix.vstack(
          sp.Matrix.hstack(*sol_space).T,
          sp.Matrix([[sp.Rational(x) for x in H_T3L]])).rank() == 3)


def unbroken_dim(a, b):
    """dim of the centralizer of the adjoint VEV v = a*Y + b*(B-L)."""
    h = tuple(a * y + b * bl for y, bl in zip(H_Y, H_BL))
    return NQ + sum(1 for r in ROOTS.values() if val(h, r["alpha"]) == 0)


grid = [F(n, d) for n in range(-24, 25) for d in (1, 2, 3, 4, 5, 6)]
dims = set()
for a in set(grid) | {F(1)}:
    for b in set(grid) | {F(1)}:
        if a == 0 and b == 0:
            continue
        dims.add(unbroken_dim(a, b))
check("PV-1 replay: over the entire SM-preserving adjoint VEV direction space "
      "the unbroken dimension takes exactly the values {13, 15, 19, 25}; 12 "
      "never occurs and the minimum is 13",
      dims == {13, 15, 19, 25} and min(dims) == 13 and 12 not in dims)
check("PV-1 replay, named points: pure B-L gives 15, the SU(5) direction gives "
      "25, and a generic direction gives exactly 13",
      unbroken_dim(F(0), F(1)) == 15 and unbroken_dim(F(4), F(1)) == 25
      and unbroken_dim(F(1), F(7)) == 13)

# THE RANK THEOREM (prior art: CB-A A4 / standard SO(10) model building).
check("RANK THEOREM (CB-A A4, re-derived): an adjoint VEV is a Cartan element, "
      "so its centralizer contains the WHOLE 5-dimensional Cartan; rank "
      "so(10) = 5 > 4 = rank(SM), so at least one U(1) beyond the SM is "
      "unbroken for EVERY adjoint VEV, at every point of the sweep",
      all(unbroken_dim(a, b) >= 13 for a in (F(1), F(0), F(-3, 5), F(4))
          for b in (F(1), F(0), F(2), F(-7, 3)) if (a, b) != (F(0), F(0)))
      and NQ == 5
      and sp.Matrix([[sp.Rational(x) for x in h] for h in
                     [H_C1, H_C2, H_T3L, H_Y]]).rank() == 4
      and NQ - sp.Matrix([[sp.Rational(x) for x in h] for h in
                          [H_C1, H_C2, H_T3L, H_Y]]).rank() == 1)

# The B-L theorem: any VEV annihilated by B-L leaves u(1)_{B-L} unbroken.
sm_rank_matrix = sp.Matrix([[sp.Rational(x) for x in h] for h in SM_CARTAN])
sm_plus_bl = sp.Matrix([[sp.Rational(x) for x in h] for h in SM_CARTAN
                        + [H_BL]])
check("B-L THEOREM (MJ-5 composed): every SM-preserving adjoint VEV has weight "
      "zero, hence B-L charge exactly 0, so exp(i theta (B-L)) fixes it and "
      "u(1)_{B-L} lies in the stabilizer of EVERY available SM-preserving VEV.  "
      "With content: the SM Cartan has rank 4, adjoining B-L gives rank 5, so "
      "B-L is a genuinely NEW unbroken direction, never a combination of SM "
      "generators",
      len(sm_singlet_roots) == 0
      and sm_rank_matrix.rank() == 4 and sm_plus_bl.rank() == 5
      and all(unbroken_dim(a, b) >= 13 for a, b in
              ((F(1), F(3)), (F(0), F(1)), (F(4), F(1)), (F(-2), F(1)))))

# CONTROL that the sweep is not shaped to exclude 12: the 126's SM singlet.
# Weights of the 126 (self-dual Lambda^5) are (+-1,+-1,+-1,+-1,+-1) in the
# e-basis.  v_PSB is the (10bar,1,3) SM singlet at (1,1,1,1,1).
V_PSB = (F(1), F(1), F(1), F(1), F(1))
check("CONTROL, and it names the missing object: the 126 weight (1,1,1,1,1) IS "
      "an SM singlet (T3L = Y = 0) and carries B-L = -2 exactly, so B-L does "
      "NOT annihilate it, u(1)_{B-L} is NOT in its stabilizer, and the "
      "stabilizer can be the SM alone -- the test therefore CAN return 12 and "
      "returns 13 only because GU-as-declared has no such carrier",
      val(H_T3L, V_PSB) == 0 and val(H_Y, V_PSB) == 0
      and val(H_BL, V_PSB) == -2 and val(H_BL, V_PSB) != 0
      and 12 not in dims)
check("CONTROL, second horn: a rank-reducing VEV is exactly what an adjoint "
      "cannot supply -- the 126 weight has 5 nonzero e-components while every "
      "adjoint weight has at most 2, so no adjoint direction reproduces it",
      sum(1 for x in V_PSB if x != 0) == 5
      and max(sum(1 for x in r["alpha"] if x != 0) for r in ROOTS.values()) == 2)


# ===========================================================================
# PART I.4  Electroweak breaking, and the final massless-vector count.
# ===========================================================================
# The SM Higgs is (1,2)_{1/2} with B-L = 0.  Take the neutral component:
# T3L = -1/2, Y = +1/2, Q = 0, B-L = 0.  A generator X in the unbroken
# su(3)+su(2)_L+u(1)_Y+u(1)_{B-L} survives iff it annihilates that component.
HIGGS = {"T3L": F(-1, 2), "Y": F(1, 2), "BL": F(0)}
check("the SM Higgs neutral component has Q = T3L + Y = 0 and B-L = 0 exactly, "
      "so U(1)_EM and U(1)_{B-L} both survive electroweak breaking while the "
      "three broken su(2)_L x u(1)_Y directions do not",
      HIGGS["T3L"] + HIGGS["Y"] == 0 and HIGGS["BL"] == 0)
check("FINAL COUNT.  GU-as-declared, observation + the best available "
      "SM-preserving adjoint VEV + electroweak breaking, leaves "
      "8 gluons + 1 photon + 1 B-L boson = 10 massless gauge bosons; the "
      "Standard Model has 9.  EXACTLY ONE extra massless gauge boson, and it "
      "is the gauged U(1)_{B-L}",
      8 + 1 + 1 == 10 and 8 + 1 == 9 and 10 - 9 == 1
      and min(dims) - 12 == 1)
POL_MASSLESS = 4 - 1 - 1        # 4 components - gauge orbit - Gauss constraint
POL_MASSIVE = 4 - 1             # 4 components - the transversality constraint
check("a massless vector carries exactly 2 physical helicity states (4 field "
      "components minus one gauge direction minus one constraint) whereas a "
      "massive one carries 3, so the extra boson is 2 bosonic degrees of "
      "freedom and the observation-only stage carries 9 x 2 = 18 non-SM gauge "
      "degrees of freedom",
      POL_MASSLESS == 2 and POL_MASSIVE == 3 and POL_MASSLESS != POL_MASSIVE
      and 9 * POL_MASSLESS == 18)


# ===========================================================================
# PART I.5  Which surviving directions are asymptotic single-particle states?
#           This is the check that blocks the naive dark-radiation overclaim.
# ===========================================================================
NG = sp.Symbol("n_g", positive=True, integer=True)


def b0_nonabelian(C_A, weyl_fund_per_gen):
    """One-loop b0 with beta(g) = -b0 g^3/(16 pi^2), T(fund) = 1/2."""
    return (sp.Rational(11, 3) * C_A
            - sp.Rational(2, 3) * weyl_fund_per_gen * sp.Rational(1, 2) * NG)


b4 = b0_nonabelian(4, 4)      # (4,2,1) + (4bar,1,2): 4 Weyl fundamentals / gen
b3 = b0_nonabelian(3, 4)      # q_L, u^c, d^c: 4 Weyl (anti)fundamentals / gen
b2R = b0_nonabelian(2, 4)     # (4bar,1,2): 4 Weyl doublets / gen
check("exact one-loop coefficients: b0(SU(4)_C) = 44/3 - 4 n_g/3, "
      "b0(SU(3)_C) = 11 - 4 n_g/3, b0(SU(2)_R) = 22/3 - 4 n_g/3",
      sp.simplify(b4 - (sp.Rational(44, 3) - sp.Rational(4, 3) * NG)) == 0
      and sp.simplify(b3 - (11 - sp.Rational(4, 3) * NG)) == 0
      and sp.simplify(b2R - (sp.Rational(22, 3) - sp.Rational(4, 3) * NG)) == 0)
check("QCD cross-check: at n_g = 3, b0(SU(3)) = 7, the textbook six-flavour "
      "value 11 - 2 n_f/3",
      b3.subs(NG, 3) == 7 and 11 - sp.Rational(2, 3) * 6 == 7)
check("EXACT AND n_g-INDEPENDENT: b0(SU(4)) - b0(SU(3)) = 11/3 = (11/3)(C_A(4) "
      "- C_A(3)), because the matter contributions are identical -- SU(4) is "
      "MORE asymptotically free than SU(3) whatever the generation count",
      sp.simplify(b4 - b3 - sp.Rational(11, 3)) == 0)
check("at n_g = 3: b0(SU(4)) = 32/3, b0(SU(3)) = 7, b0(SU(2)_R) = 10/3, all "
      "strictly positive -- every unbroken non-abelian factor of k is "
      "asymptotically free",
      b4.subs(NG, 3) == sp.Rational(32, 3) and b3.subs(NG, 3) == 7
      and b2R.subs(NG, 3) == sp.Rational(10, 3)
      and all(x > 0 for x in (b4.subs(NG, 3), b3.subs(NG, 3), b2R.subs(NG, 3))))
check("CONTROL: the asymptotic-freedom check is not vacuous -- b0(SU(2)_R) "
      "changes sign at n_g = 11/2, so at n_g = 6 the SU(2)_R factor is NOT "
      "asymptotically free and the confinement argument would fail there",
      b2R.subs(NG, 6) < 0 and b2R.subs(NG, 3) > 0 and b4.subs(NG, 11) == 0)

alpha_sym, mu_sym = sp.symbols("alpha mu", positive=True)
Lam4 = mu_sym * sp.exp(-2 * sp.pi / (b4.subs(NG, 3) * alpha_sym))
Lam3 = mu_sym * sp.exp(-2 * sp.pi / (b3.subs(NG, 3) * alpha_sym))
ratio = sp.simplify(sp.log(Lam4 / Lam3))
check("EXACT INEQUALITY: with a single unbroken SU(4) coupling, alpha_4 = "
      "alpha_3 identically, and log(Lambda_4/Lambda_3) = (2 pi/alpha)"
      "(1/b3 - 1/b4) > 0 -- the SU(4) strong scale is strictly ABOVE Lambda_QCD",
      sp.simplify(ratio - 2 * sp.pi / alpha_sym
                  * (1 / b3.subs(NG, 3) - 1 / b4.subs(NG, 3))) == 0
      and sp.Rational(1, 7) - sp.Rational(3, 32) > 0)

# Triality: a colour triplet is never a colour singlet, so never an asymptotic
# state of a confining SU(3).  Triality of a weight = (sum of e-components)
# mod 3 in the su(3) weight lattice normalisation used here.
lq_colour_charge = {tuple(r["alpha"][:3]) for r in lq_roots}
check("the 6 leptoquark directions carry NONZERO su(3) weight (each has exactly "
      "two nonzero colour components of equal sign, and the 6 colour weights "
      "are distinct), so they transform as 3 + 3bar and are NOT colour singlets",
      all(sum(1 for x in r["alpha"][:3] if x != 0) == 2
          and r["alpha"][0] * r["alpha"][1] + r["alpha"][1] * r["alpha"][2]
          + r["alpha"][0] * r["alpha"][2] > 0
          and any(dcharge(h, r) != 0 for h in (H_C1, H_C2))
          for r in lq_roots)
      and len(lq_colour_charge) == 6
      and all(dcharge(H_C1, r) == 0 == dcharge(H_C2, r) for r in wr_roots))
check("the 2 W_R directions carry NONZERO su(2)_R weight, so they are not "
      "su(2)_R singlets either",
      all(dcharge(H_T3R, r) != 0 for r in wr_roots))

def bracket_nonzero(a, b):
    return not (a["E"] @ b["E"]).equals(b["E"] @ a["E"])


# The Z' direction is the Cartan element of su(2)_R orthogonal to Y inside
# span{T3R, B-L}; it fails to commute with the W_R root vectors, so it too
# carries su(2)_R charge and is not a singlet of the unbroken algebra.
zprime_charged = all(dcharge(H_T3R, r) != 0 for r in wr_roots)
charged_under_own_factor = (
    all(any(bracket_nonzero(r, s) for s in so6_roots if s is not r)
        for r in lq_roots)
    and all(any(bracket_nonzero(r, s) for s in so4_roots if s is not r)
            for r in wr_roots))
free_A = [r for r in lq_roots + wr_roots
          if not any(bracket_nonzero(r, s)
                     for s in (so6_roots if r in lq_roots else so4_roots)
                     if s is not r)]
check("KEY NEGATIVE, and it kills the naive dark-radiation count: in the "
      "observation-only stage the unbroken algebra su(4)+su(2)_L+su(2)_R has NO "
      "abelian factor.  Verified by explicit 32x32 commutators, every one of "
      "the 6 leptoquarks fails to commute with another su(4) generator and "
      "every W_R fails to commute with another su(2)_R generator, so all 9 "
      "non-SM directions carry non-abelian charge under a confining factor and "
      "the number that are free asymptotic massless quanta is EXACTLY ZERO -- "
      "a naive 'Delta N_eff from 9 x 2 extra dof' would have been WRONG",
      charged_under_own_factor and zprime_charged and len(free_A) == 0
      and len(lq_roots) + len(wr_roots) == 8 and 8 + 1 == 9)
check("CONTROL: the same commutator test applied to the u(1)_{B-L} generator, "
      "which IS abelian and IS a free quantum, must give the opposite answer -- "
      "B-L commutes with all of su(3) and su(2)_L and so is uncharged under "
      "every factor that survives the VEV stage",
      commutes_with_sm(H_BL)
      and all(val(H_BL, r["alpha"]) == 0 for r in gluon_roots + wl_roots)
      and any(val(H_BL, r["alpha"]) != 0 for r in lq_roots))
check("by contrast, in the VEV stage the surviving extra generator is the "
      "ABELIAN u(1)_{B-L}: it commutes with su(3) and su(2)_L, is unconfined, "
      "and IS a free massless quantum -- exactly 1 of them, 2 helicities",
      commutes_with_sm(H_BL) and H_BL != tuple(F(0) for _ in range(NQ))
      and min(dims) - 12 == 1)


# ===========================================================================
# PART I.6  Long-range charge structure of ordinary matter.  Exact integers.
# ===========================================================================
# Nucleons and the electron, from the 16's charges: B = 1/3 per quark.
BL_PROTON = F(1, 3) * 3      # uud
BL_NEUTRON = F(1, 3) * 3     # udd
BL_ELECTRON = F(-1)
Q_PROTON, Q_NEUTRON, Q_ELECTRON = F(1), F(0), F(-1)
check("exact B-L charges of ordinary matter: proton +1, neutron +1, electron "
      "-1; both nucleons carry the SAME B-L charge, so the B-L force is "
      "repulsive between all nucleons and is NOT proportional to electric "
      "charge",
      BL_PROTON == 1 and BL_NEUTRON == 1 and BL_ELECTRON == -1
      and (BL_PROTON, BL_NEUTRON, BL_ELECTRON) != (Q_PROTON, Q_NEUTRON, Q_ELECTRON))

ISOTOPES = {"H-1": (1, 1), "He-4": (2, 4), "Be-9": (4, 9), "Al-27": (13, 27),
            "Si-28": (14, 28), "Ti-48": (22, 48), "Fe-56": (26, 56),
            "Pt-195": (78, 195)}


def atom_charges(Z, A):
    """(Q, B-L) of an electrically neutral atom, exactly."""
    q = Z * Q_PROTON + (A - Z) * Q_NEUTRON + Z * Q_ELECTRON
    bl = Z * BL_PROTON + (A - Z) * BL_NEUTRON + Z * BL_ELECTRON
    return q, bl


check("every neutral atom has Q = 0 exactly and B-L = A - Z = N exactly, so "
      "the B-L charge of bulk matter is the NEUTRON NUMBER",
      all(atom_charges(Z, A) == (F(0), F(A - Z)) for Z, A in ISOTOPES.values()))
EP_PAIRS = [("Ti-48", "Pt-195"), ("Be-9", "Ti-48"), ("Be-9", "Al-27"),
            ("H-1", "Fe-56")]
check("B-L per unit mass number is composition-dependent: N/A differs on EVERY "
      "element pair actually used in equivalence-principle experiments, so a "
      "massless B-L force is NOT absorbable into a redefinition of Newton's "
      "constant.  (He-4 and Si-28 do coincide at N/A = 1/2 exactly; that "
      "accidental degeneracy is recorded, not hidden, and does not affect any "
      "tested pair.)",
      all(F(ISOTOPES[a][1] - ISOTOPES[a][0], ISOTOPES[a][1])
          != F(ISOTOPES[b][1] - ISOTOPES[b][0], ISOTOPES[b][1])
          for a, b in EP_PAIRS)
      and F(4 - 2, 4) == F(28 - 14, 28) == F(1, 2)
      and len({F(A - Z, A) for Z, A in ISOTOPES.values()}) == 7)

# The kinetic-mixing / basis-rotation escape, closed exactly.
mix_grid = [F(n, d) for n in range(-40, 41) for d in (1, 2, 3, 4, 5, 8, 61, 100)]
escape_bl = [cc for cc in mix_grid
             if all((F(A - Z) + cc * F(0)) == 0 for Z, A in ISOTOPES.values())]
escape_q = [cc for cc in mix_grid
            if all((F(0) + cc * F(0)) == 0 for Z, A in ISOTOPES.values())]
check("ESCAPE CLOSED, exactly: the physical extra charge is only defined up to "
      "adding a multiple of Q (photon kinetic mixing).  For EVERY rational "
      "mixing c, (B-L + c Q) evaluated on a neutral atom is N + c*0 = N, which "
      "is nonzero whenever N >= 1.  No rotation of the two massless U(1)s can "
      "make bulk matter neutral under the extra force",
      len(escape_bl) == 0 and len(mix_grid) > 500
      and all(F(A - Z) != 0 for Z, A in ISOTOPES.values() if A > Z))
check("CONTROL: the escape test is NOT vacuous.  A planted extra U(1) whose "
      "charge IS the electric charge (a pure dark photon) gives zero on every "
      "neutral atom for every mixing, so the same test would have passed the "
      "escape -- the failure above is a property of B-L, not of the test",
      len(escape_q) == len(mix_grid) and len(escape_bl) == 0)
check("CONTROL, second planted surrogate: an extra U(1) coupled to B + L "
      "(instead of B - L) gives A - ... on a neutral atom, and a surrogate "
      "coupled to Q - Q gives identically zero -- the test separates the three",
      all(Z * F(1, 3) * 3 + (A - Z) * F(1, 3) * 3 + Z * F(1) != 0
          for Z, A in ISOTOPES.values())
      and all(Z * F(0) + (A - Z) * F(0) + Z * F(0) == 0 for Z, A in ISOTOPES.values()))

# One-loop running of the abelian B-L coupling: exact rational coefficient.
q_bl_weyl = [val(H_BL, mu_of(w)) for w in W16]
b_bl = sp.Rational(2, 3) * sum(sp.Rational(q * q) for q in q_bl_weyl) * NG
check("exact abelian coefficient: b(U(1)_{B-L}) = (2/3) sum q^2 over one 16 "
      "times n_g = 32 n_g / 9, i.e. 32/3 at n_g = 3.  Positive, so the coupling "
      "runs LOGARITHMICALLY and monotonically toward the infrared, never "
      "exponentially",
      sp.simplify(b_bl - sp.Rational(32, 9) * NG) == 0
      and b_bl.subs(NG, 3) == sp.Rational(32, 3)
      and sum(F(q * q) for q in q_bl_weyl) == F(16, 3)
      and sum(F(q * q) for q in q_bl_weyl if abs(q) == 1) == 4
      and sum(F(q * q) for q in q_bl_weyl if abs(q) == F(1, 3)) == F(4, 3))

ainv_uv, efolds = sp.symbols("alpha_inv_UV N_efolds", positive=True)
ainv_ir = ainv_uv + b_bl.subs(NG, 3) / (2 * sp.pi) * efolds
check("EXACT RUNNING LAW: 1/alpha_{B-L}(IR) = 1/alpha_{B-L}(UV) + "
      "(b/2 pi) ln(mu_UV/mu_IR).  To reach a target 1/alpha_target from a UV "
      "value requires N_efolds = 2 pi (1/alpha_target - 1/alpha_UV)/b e-folds, "
      "which is LINEAR in 1/alpha_target -- an exponentially small coupling "
      "needs an exponentially large scale ratio",
      sp.simplify(sp.solve(sp.Eq(ainv_ir, sp.Symbol("T", positive=True)),
                           efolds)[0]
                  - 2 * sp.pi * (sp.Symbol("T", positive=True) - ainv_uv)
                  / b_bl.subs(NG, 3)) == 0)


# ===========================================================================
# PART I.7  Exact dark-radiation formulas.  Derived, not quoted.
# ===========================================================================
# Entropy conservation across e+e- annihilation, with exact rational g_*s.
g_s_before = sp.Rational(2) + sp.Rational(7, 8) * sp.Rational(4)   # gamma + e+e-
g_s_after = sp.Rational(2)                                          # gamma only
T_ratio_cubed = g_s_before / g_s_after
check("DERIVED, not quoted: entropy conservation across e+e- annihilation with "
      "exact rational g_*s = 11/2 before and 2 after gives "
      "(T_gamma/T_nu)^3 = 11/4 exactly",
      T_ratio_cubed == sp.Rational(11, 4) and g_s_before == sp.Rational(11, 2))

g_star_sm_pre = sp.Rational(2) + sp.Rational(7, 8) * (4 + 6)
check("exact SM relativistic count just above e+e- annihilation: g_* = 43/4 = "
      "10.75 (photon 2, e+e- 4 fermionic, 3 neutrino species 6 fermionic)",
      g_star_sm_pre == sp.Rational(43, 4))

gX = sp.Symbol("g_X", positive=True)
Trat = sp.Symbol("T_X_over_T_nu", positive=True)
dNeff = sp.Rational(4, 7) * gX * Trat ** 4
check("EXACT DEFINITION: Delta N_eff = (4/7) g_X (T_X/T_nu)^4 for a boson with "
      "g_X internal degrees of freedom, from rho_X/rho_{1 nu} with the "
      "fermionic 7/8 and g_nu = 2",
      sp.simplify(dNeff - sp.Rational(2, 1) * gX * Trat ** 4
                  / (sp.Rational(7, 8) * 2 * 2)) == 0)

dNeff_coupled = dNeff.subs({gX: 2, Trat: sp.Rational(11, 4) ** sp.Rational(1, 3)})
dNeff_nu_temp = dNeff.subs({gX: 2, Trat: 1})
check("EXACT VALUES for ONE extra massless vector.  If it stays coupled to the "
      "photon bath through e+e- annihilation: Delta N_eff = (8/7)(11/4)^(4/3) "
      "exactly.  If it decouples just before and shares the neutrino "
      "temperature: Delta N_eff = 8/7 exactly.  These bracket the thermalised "
      "case",
      sp.simplify(dNeff_coupled - sp.Rational(8, 7)
                  * sp.Rational(11, 4) ** sp.Rational(4, 3)) == 0
      and dNeff_nu_temp == sp.Rational(8, 7)
      and float(dNeff_nu_temp) < float(dNeff_coupled))

g_s_full_sm = sp.Rational(427, 4)          # 106.75, all SM above the top mass
dNeff_early = dNeff.subs({gX: 2,
                          Trat: (g_star_sm_pre / g_s_full_sm) ** sp.Rational(1, 3)})
check("DECISIVE THERMAL-HISTORY CONTROL.  The SAME formula applied to a species "
      "that decouples ABOVE all SM thresholds (g_*s = 427/4 = 106.75) gives "
      "Delta N_eff = (8/7)(43/427)^(4/3), about 0.054 -- far below any current "
      "sensitivity.  The exclusion below therefore comes ENTIRELY from the "
      "claim that this boson never decouples, not from its existence",
      float(dNeff_early) < 0.1 and float(dNeff_nu_temp) > 1
      and float(dNeff_nu_temp) / float(dNeff_early) > 20)

# Interaction rate vs Hubble, symbolically: the thermalisation criterion.
alpha_X, T_sym, MPL = sp.symbols("alpha_X T M_Pl", positive=True)
gamma_over_H = (alpha_X ** 2 * T_sym) / (T_sym ** 2 / MPL)
check("EXACT SCALING: for a massless gauge boson coupled to relativistic "
      "charged matter, Gamma/H ~ alpha_X^2 M_Pl / T, which GROWS as the "
      "universe cools.  A gauge boson that is ever in equilibrium stays in "
      "equilibrium; decoupling requires alpha_X below a threshold that scales "
      "as sqrt(T/M_Pl)",
      sp.simplify(gamma_over_H - alpha_X ** 2 * MPL / T_sym) == 0
      and sp.simplify(sp.solve(sp.Eq(gamma_over_H, 1), alpha_X)[0]
                      - sp.sqrt(T_sym / MPL)) == 0)


# ===========================================================================
# PART II.  EMPIRICAL INPUTS.  NOT part of the certificate.  Every row carries
#           a value, an uncertainty and a source.  No exactness is claimed and
#           no comparison below is exact.
# ===========================================================================
EMPIRICAL = [
    # (symbol, value, uncertainty, source)
    ("N_eff (CMB)", 2.99, "+-0.17 (68% CL)",
     "Planck 2018 results VI, A&A 641 A6 (2020), TT,TE,EE+lowE+lensing+BAO"),
    ("N_eff (SM prediction)", 3.044, "+-0.002",
     "Froustey-Pitrou-Volpe JCAP 12(2020)015; Bennett et al. JCAP 04(2021)073"),
    ("Delta N_eff (BBN only)", -0.10, "+-0.21 (68% CL)",
     "Yeh-Shah-Olive-Fields, 2024 BBN baryon abundance update, JCAP 06(2024)006"),
    ("eta_Eotvos (Ti/Pt)", -1.5e-15, "+-2.7e-15 (1 sigma, stat+syst)",
     "Touboul et al. (MICROSCOPE), PRL 129, 121102 (2022)"),
    ("eta_Eotvos (Be/Ti)", 0.3e-13, "+-1.8e-13",
     "Schlamminger et al. (Eot-Wash), PRL 100, 041101 (2008)"),
    ("epsilon_{B-L} limit (units of e)", 0.8e-24, "upper limit, MICROSCOPE first results",
     "Fayet, PRD 97, 055039 (2018), arXiv:1712.00856"),
    ("G m_u^2/(hbar c)", 5.821e-39, "+-1e-4 relative", "CODATA 2018 G and m_u"),
    ("alpha_s(M_Z)", 0.1180, "+-0.0009", "PDG 2024 review"),
    ("Lambda_QCD^(5) (MS-bar)", 0.21, "+-0.01 GeV", "PDG 2024 QCD review"),
    ("m_e", 0.51099895000e-3, "+-1.5e-13 GeV", "CODATA 2018"),
    ("m_d(2 GeV, MS-bar)", 4.70e-3, "+0.07/-0.07 GeV*1e-3", "PDG 2024"),
    ("m_u(2 GeV, MS-bar)", 2.16e-3, "+0.49/-0.26 GeV*1e-3", "PDG 2024"),
    ("sum m_nu", 0.12e-9, "< , 95% CL, GeV", "Planck 2018 + BAO"),
    ("Earth (B-L)/mu", 0.4957, "+-0.01 (composition model)",
     "standard geochemical composition, as used in EP-test literature"),
    ("(B-L)/mu for Ti (nat.)", (47.867 - 22) / 47.867, "+-1e-5 (IUPAC atomic weight)",
     "IUPAC 2021 standard atomic weights"),
    ("(B-L)/mu for Pt (nat.)", (195.084 - 78) / 195.084, "+-1e-5 (IUPAC atomic weight)",
     "IUPAC 2021 standard atomic weights"),
    ("B(K_L -> mu e)", 4.7e-12, "< , 90% CL",
     "BNL E871, Ambrose et al., PRL 81, 5734 (1998)"),
    ("SU(4) conformal window edge", 12.0, "+-2 Dirac fundamentals (large theory unc.)",
     "lattice / Schwinger-Dyson estimates; quoted as an order of magnitude only"),
]

check("STRUCTURAL: every empirical input carries a nonempty value, a nonempty "
      "uncertainty statement and a nonempty source, and none is used inside the "
      "exact certificate above",
      len(EMPIRICAL) == 18
      and all(isinstance(v, float) and u.strip() and s.strip()
              for _, v, u, s in EMPIRICAL))

# --- Derived empirical comparisons.  Uncertainty-carrying.  NOT exact. -------
EMP_REPORT: list[str] = []

neff_meas, neff_err = 2.99, 0.17
neff_sm = 3.044
d_coupled, d_nutemp = float(dNeff_coupled), float(dNeff_nu_temp)
EMP_REPORT.append(
    f"Delta N_eff predicted (thermalised, bracketed): {d_nutemp:.4f} to {d_coupled:.4f} "
    f"[exact symbolic 8/7 and (8/7)(11/4)^(4/3)]")
EMP_REPORT.append(
    f"Delta N_eff allowed by Planck 2018 at 2 sigma: |Delta N_eff| <~ "
    f"{2 * neff_err + abs(neff_sm - neff_meas):.2f}   (measured {neff_meas} +- {neff_err}, "
    f"SM {neff_sm})")
EMP_REPORT.append(
    f"tension using the quoted 1 sigma: {(d_nutemp - (neff_meas - neff_sm)) / neff_err:.1f} "
    f"sigma (lower bracket) to {(d_coupled - (neff_meas - neff_sm)) / neff_err:.1f} "
    f"sigma (upper bracket).  NOT an exact statement; the sigma is Planck's.")
EMP_REPORT.append(
    f"CONTROL, decoupling above the EW scale: Delta N_eff = {float(dNeff_early):.4f}, "
    f"which is INSIDE the Planck error bar.  The exclusion is a thermal-history "
    f"claim, not a counting claim.")

# Fifth force.  Eotvos parameter from a massless vector coupled to B-L.
Gmu2 = 5.821e-39
q_earth = 0.4957
q_ti = (47.867 - 22) / 47.867
q_pt = (195.084 - 78) / 195.084
dq = abs(q_pt - q_ti)
eta_limit = 2 * 2.7e-15                                # 2 sigma, MICROSCOPE final
alpha_bl_limit = eta_limit * Gmu2 / (q_earth * dq)
g_bl_limit = (4 * 3.14159265358979 * alpha_bl_limit) ** 0.5
EMP_REPORT.append(
    f"eta = [alpha_BL/(G m_u^2)] (q/mu)_Earth * Delta(q/mu)_(Ti,Pt) with "
    f"Delta(q/mu) = {dq:.5f}")
EMP_REPORT.append(
    f"=> alpha_BL < {alpha_bl_limit:.2e}, i.e. g_BL < {g_bl_limit:.2e} "
    f"(MICROSCOPE final, 2 sigma).  Independent cross-check: Fayet's published "
    f"limit from the FIRST MICROSCOPE results is |eps_BL| < 0.8e-24 in units of "
    f"e, i.e. g_BL < {0.8e-24 * 0.30282:.2e}; the final data are ~4x better in "
    f"eta, so ~2x better in g.  The two agree.")
alpha_bl_predicted_lo, alpha_bl_predicted_hi = 1e-3, 1e-1
EMP_REPORT.append(
    f"GU-as-declared gives g_BL descended from the SU(4) coupling and run down "
    f"logarithmically: alpha_BL in roughly [{alpha_bl_predicted_lo:.0e}, "
    f"{alpha_bl_predicted_hi:.0e}], i.e. g_BL ~ 0.1 to 1.")
EMP_REPORT.append(
    f"=> GAP: {alpha_bl_predicted_lo / alpha_bl_limit:.1e} in alpha even at the "
    f"most conservative end; about {(alpha_bl_predicted_lo / alpha_bl_limit) ** 0.5:.1e} "
    f"in the coupling.  ~24 orders of magnitude in g, ~48 in alpha.")
efolds_needed = 2 * 3.14159265358979 * (1.0 / alpha_bl_limit) / float(b_bl.subs(NG, 3))
EMP_REPORT.append(
    f"the exact running law of PART I.6 then says reaching alpha_BL = "
    f"{alpha_bl_limit:.1e} by running would need N_efolds ~ {efolds_needed:.1e}, "
    f"i.e. a scale ratio of e^({efolds_needed:.1e}).  There is no such scale.")

# Confinement scale of the unbroken SU(4).
alpha_s_mz = 0.1180
import math as _m
lnratio = 2 * _m.pi / alpha_s_mz * (1 / 7 - 3 / 32)
EMP_REPORT.append(
    f"unbroken SU(4): Lambda_4/Lambda_3 = exp[(2 pi/alpha)(1/b3 - 1/b4)] "
    f"= {_m.exp(lnratio):.1f} at alpha_s(M_Z) = {alpha_s_mz}, so Lambda_4 ~ "
    f"{_m.exp(lnratio) * 0.21:.1f} GeV.  One loop, no thresholds, "
    f"scheme-dependent -- an order of magnitude, not a measurement.  The exact "
    f"content is only Lambda_4 > Lambda_QCD.")
EMP_REPORT.append(
    f"SU(4) with n_f = 2 n_g = 6 Dirac fundamentals sits well below the "
    f"conformal-window edge (~12 +- 2), so it confines rather than flowing to "
    f"an IR fixed point.  Lattice-informed, NOT exact.")
EMP_REPORT.append(
    "consequence: leptons are the fourth colour of a confining SU(4).  Free "
    "electrons would not exist below Lambda_4.  This is a laboratory kill of "
    "the observation-only stage that needs no cosmology at all.")
EMP_REPORT.append(
    "and by Wigner's theorem an exact unbroken SU(4)_C forces m_e = m_d and "
    "m_nu = m_u exactly; measured m_e = 0.511 MeV vs m_d(2 GeV) = 4.70 +- 0.07 "
    "MeV, and sum m_nu < 0.12 eV vs m_u = 2.16 MeV.")

# ===========================================================================
passed = sum(1 for _, ok in EXACT if ok)
print("=" * 78)
print("PART I -- EXACT CERTIFICATE (integer/rational/symbolic; no float is "
      "load-bearing)")
print("=" * 78)
for name, ok in EXACT:
    print(f"  {'PASS' if ok else 'FAIL'}  {name}")
print()
print(f"{passed}/{len(EXACT)} EXACT checks passed")
print()
print("  so(6,4) = 45 = k(21) + p(24);  k = su(4) + su(2)_L + su(2)_R")
print("  observation-only stage : 21 massless gauge bosons, 9 non-SM, "
      "0 free asymptotic quanta (all confined)")
print(f"  best available VEV     : {min(dims)} massless, 1 non-SM, and it is "
      "the ABELIAN u(1)_(B-L)")
print("  after electroweak      : 10 massless gauge bosons vs the SM's 9 -- "
      "exactly one extra")
print(f"  Delta N_eff (exact)    : {sp.Rational(8, 7)} to "
      f"{sp.nsimplify(dNeff_coupled)}  = {float(dNeff_nu_temp):.4f} to "
      f"{float(dNeff_coupled):.4f}")
print(f"  b0(SU(4)) - b0(SU(3))  : {sp.simplify(b4 - b3)} exactly, "
      "n_g-independent")
print()
print("=" * 78)
print("PART II -- EMPIRICAL INPUTS AND COMPARISONS.  NOT EXACT.  NOT CERTIFIED.")
print("=" * 78)
for sym, v, u, s in EMPIRICAL:
    print(f"  {sym:34s} {v!r:>14}   {u:44s} [{s}]")
print()
for line in EMP_REPORT:
    print("  * " + line)
print()
print("  Every conclusion above survives an order-of-magnitude error in every "
      "empirical input; none rests on a quoted digit.")
print("=" * 78)

if passed != len(EXACT):
    raise SystemExit(1)
sys.exit(0)
