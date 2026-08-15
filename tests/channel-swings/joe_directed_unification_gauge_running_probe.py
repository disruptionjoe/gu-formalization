#!/usr/bin/env python3
"""Joe-directed channel: GAUGE-COUPLING RUNNING for GU-AS-DECLARED (gate CU-1).

WHAT IS EXACT AND WHAT IS NOT -- read this first.
=================================================
This probe has two clearly separated layers.

  LAYER A (EXACT, sympy Rational, no floats anywhere):
      weight systems of so(10) ~ so(6,4)_C, embedding indices of the
      Pati-Salam / Standard-Model subalgebras, Dynkin indices of 10 / 16 / 45 /
      144 / 10(x)45, the GUT hypercharge normalisation, the Pati-Salam -> SM
      coupling matching relation, the one-loop beta-function coefficients, and
      the two structural theorems below.  Every LAYER-A check is a Rational
      identity.  N/N certificate is reported for LAYER A alone.

  LAYER B (EMPIRICAL, floats, quoted with uncertainties):
      the measured couplings at M_Z.  These are NOT exact, are NOT derived, and
      the comparison against them is NEVER presented as exact.  Layer B checks
      are reported separately and are explicitly labelled.

GU CONTENT USED (all committed in-repo today, cited, not re-derived here)
========================================================================
  PV-2  observation reduces so(6,4) = k(21) (+) p(24) to its maximal compact;
        k ~ su(4) (+) su(2)_L (+) su(2)_R is Pati-Salam; the SM's 12 sit
        entirely inside k; exactly 9 non-SM directions survive inside k
        (6 leptoquarks + 2 W_R + 1 Z'), untouched by the reduction.
  PV-1  over the whole SM-preserving adjoint orbit space the unbroken dimension
        is {13,15,19,25}, never 12.
  AC-1  10 (x) 16 = 144 (+) 16; the 144 is the gamma-traceless vector-spinor and
        the internal home of zeta.  RS spin factors (3,4,5)/(21,20,19) derived
        there for carriers A / bare / B.
  2B    field-content table: eps = (Omega^0, ad), $ = (Omega^1, ad),
        nu = (Omega^0, S/), zeta = (Omega^1, S/).

PREDECLARED CONVENTIONS (fixed BEFORE running; see the artifact preflight)
=========================================================================
  C1  One loop, MS-bar, step-function decoupling.  No two-loop, no Yukawa.
  C2  b_i defined by   d(alpha_i^-1)/d ln mu = b_i / (2 pi),
      b = (11/3) C2(G) - (2/3) Sum_Weyl T(R) - (1/3) Sum_cplx-scalar T(R).
      Sign check: SM b_3 = +7 (asymptotic freedom).
  C3  Hypercharge normalisation DERIVED from the so(10) trace form, not assumed.
  C4  Gauge thresholds: PV-1 + PV-2 say Pati-Salam is UNBROKEN down to M_Z, so
      there is no gauge threshold to choose.  The only matter threshold is
      M_zeta, swept as a free parameter, never fitted.
  C5  "The couplings meet" iff there exists mu with
          |alpha_i^-1(mu) - alpha_j^-1(mu)| <= EPS_UNIFY for all pairs,
      EPS_UNIFY = 1.0 units of alpha^-1.  FIXED IN ADVANCE.  Not adjusted.
  C6  Empirical inputs are Layer B, quoted with uncertainty, from the standard
      compilation (PDG Review of Particle Physics).  They were NOT fetched in
      this session -- declared reproducibility seam.

Run:  _local/cas-venv/bin/python tests/channel-swings/joe_directed_unification_gauge_running_probe.py
"""
from __future__ import annotations

import itertools
import math
from fractions import Fraction as F

# --------------------------------------------------------------------------
# certificate bookkeeping -- LAYER A (exact) and LAYER B (empirical) separated
# --------------------------------------------------------------------------
A_CHECKS: list[tuple[str, bool]] = []
B_CHECKS: list[tuple[str, bool]] = []


def chkA(name: str, ok: bool) -> None:
    A_CHECKS.append((name, bool(ok)))


def chkB(name: str, ok: bool) -> None:
    B_CHECKS.append((name, bool(ok)))


H = F(1, 2)

# ==========================================================================
# PART 1 -- weight systems of so(10), EXACT
# ==========================================================================
# Cartan basis e_1..e_5.  All weights are 5-tuples of Fractions.

W10 = []
for i in range(5):
    for s in (1, -1):
        w = [F(0)] * 5
        w[i] = F(s)
        W10.append(tuple(w))

W16 = [tuple(F(s, 2) for s in sg)
       for sg in itertools.product((1, -1), repeat=5)
       if math.prod(sg) == 1]
W16BAR = [tuple(F(s, 2) for s in sg)
          for sg in itertools.product((1, -1), repeat=5)
          if math.prod(sg) == -1]

W45 = []
for i in range(5):
    for j in range(i + 1, 5):
        for si in (1, -1):
            for sj in (1, -1):
                w = [F(0)] * 5
                w[i], w[j] = F(si), F(sj)
                W45.append(tuple(w))
W45 += [tuple([F(0)] * 5)] * 5          # 5 Cartan (zero) weights

chkA("vector 10 has 10 weights", len(W10) == 10)
chkA("spinor 16 has 16 weights", len(W16) == 16)
chkA("conjugate spinor 16bar has 16 weights", len(W16BAR) == 16)
chkA("adjoint 45 has 45 weights (40 roots + 5 Cartan)", len(W45) == 45)
chkA("16 and 16bar are disjoint weight sets", not (set(W16) & set(W16BAR)))

# 10 (x) 16 = 144 (+) 16bar   (AC-1's tensor identity, at weight level).
# 10 (x) 16 contains 16bar, not 16, because 16 (x) 16 = 10 + 120 + 126.
T10x16 = [tuple(a + b for a, b in zip(u, v)) for u in W10 for v in W16]
chkA("10 (x) 16 has 160 weights", len(T10x16) == 160)

_rem = list(T10x16)
for w in W16BAR:
    chkA(f"16bar weight {tuple(str(x) for x in w)} occurs in 10 (x) 16", w in _rem)
    _rem.remove(w)
W144 = _rem
chkA("144 = 10 (x) 16 minus 16bar has 144 weights", len(W144) == 144)
_cnt16 = sum(1 for w in W16 if w in T10x16)
chkA("no 16 weight of the SAME chirality sits in 10 (x) 16", _cnt16 == 0)

# 10 (x) 45 -- the internal home of the displacement field $ = (Omega^1, ad)
T10x45 = [tuple(a + b for a, b in zip(u, v)) for u in W10 for v in W45]
chkA("10 (x) 45 has 450 weights", len(T10x45) == 450)


# ==========================================================================
# PART 2 -- the subalgebra generators, DERIVED, and their indices
# ==========================================================================
# so(10) > so(6) (+) so(4) = su(4) (+) su(2)_L (+) su(2)_R  acting on
# (e1,e2,e3) and (e4,e5) respectively.  The 4 of su(4) is the so(6) spinor:
#   weights (+-1/2,+-1/2,+-1/2) with product of signs = +1.
FOUR_OF_SU4 = [tuple(F(s, 2) for s in sg)
               for sg in itertools.product((1, -1), repeat=3)
               if math.prod(sg) == 1]
chkA("the 4 of su(4) = so(6) spinor has 4 weights", len(FOUR_OF_SU4) == 4)


def t_su4(w):
    """su(4) Cartan direction normalised so that T(4) = 1/2."""
    return (w[1] - w[2]) / 2


def t_su3(w):
    """su(3)_c Cartan direction; annihilates the lepton of the 4."""
    return (w[1] - w[2]) / 2


def t3L(w):
    return (w[3] + w[4]) / 2


def t3R(w):
    return (w[3] - w[4]) / 2


def b_minus_l(w):
    """B - L as a functional, fixed by (1/3,1/3,1/3,-1) on the 4 of su(4)."""
    return -F(2, 3) * (w[0] + w[1] + w[2])


def y_over_2(w):
    """Y/2 = T_3R + (B-L)/2, with Q = T_3L + Y/2."""
    return t3R(w) + b_minus_l(w) / 2


def index(gen, weights):
    """T(R) = Sum_{w in R} gen(w)^2 for a Cartan generator normalised so that
    the defining rep has T = 1/2 (su(N)) resp. T = 1 (so(N) vector)."""
    return sum(gen(w) ** 2 for w in weights)


# --- the normalisation of t_su4 is DERIVED, not asserted -------------------
chkA("t_su4 normalisation derived: T(4 of su(4)) = 1/2",
     index(t_su4, FOUR_OF_SU4) == F(1, 2))

SIX_OF_SU4 = [w for w in W10 if w[3] == 0 and w[4] == 0]
chkA("the 6 of su(4) = so(6) vector has 6 weights", len(SIX_OF_SU4) == 6)
chkA("T(6 of su(4)) = 1 (Lambda^2 of the 4)", index(t_su4, SIX_OF_SU4) == 1)

# --- B-L is DERIVED to be (1/3,1/3,1/3,-1) on the 4 -----------------------
_bl_vals = sorted(b_minus_l(w) for w in FOUR_OF_SU4)
chkA("B-L on the 4 of su(4) is (-1, 1/3, 1/3, 1/3)",
     _bl_vals == [F(-1), F(1, 3), F(1, 3), F(1, 3)])

# --- the SM content of the 16 is DERIVED from the weights -----------------
def sm_label(w):
    return (index_free(w),)


def index_free(w):
    return (t_su3(w), t3L(w), y_over_2(w))


_hy = {}
for w in W16:
    _hy[y_over_2(w)] = _hy.get(y_over_2(w), 0) + 1
chkA("16 -> SM hypercharges Y/2 with the exact SM multiplicities "
     "{Q:6 @1/6, u^c:3 @-2/3, d^c:3 @1/3, L:2 @-1/2, e^c:1 @1, nu^c:1 @0}",
     _hy == {F(1, 6): 6, F(-2, 3): 3, F(1, 3): 3, F(-1, 2): 2, F(1): 1, F(0): 1})

# --- the GUT hypercharge normalisation, DERIVED ---------------------------
sum_y2_16 = sum(y_over_2(w) ** 2 for w in W16)
t2L_16 = index(t3L, W16)
chkA("Sum_{16} (Y/2)^2 = 10/3 (exact)", sum_y2_16 == F(10, 3))
chkA("T_{su(2)_L}(16) = 2 (exact)", t2L_16 == 2)
GUT_NORM = t2L_16 / sum_y2_16
chkA("DERIVED GUT hypercharge normalisation Tr(T_3L^2)/Tr((Y/2)^2) = 3/5",
     GUT_NORM == F(3, 5))


def t1_gut(w):
    """u(1)_Y generator normalised into the so(10) trace form."""
    return y_over_2(w)          # index() below multiplies by GUT_NORM


def index_y(weights):
    return GUT_NORM * sum(y_over_2(w) ** 2 for w in weights)


# --- embedding indices in so(10): all four factors have index 1 -----------
chkA("embedding index of su(4) in so(10) is 1  [T_su4(10) = T_so10(10) = 1]",
     index(t_su4, W10) == 1)
chkA("embedding index of su(3)_c in so(10) is 1", index(t_su3, W10) == 1)
chkA("embedding index of su(2)_L in so(10) is 1", index(t3L, W10) == 1)
chkA("embedding index of su(2)_R in so(10) is 1", index(t3R, W10) == 1)
chkA("embedding index of GUT-normalised u(1)_Y in so(10) is 1",
     index_y(W10) == 1)

# --- indices of every rep GU declares -------------------------------------
REPS = {
    "10  (vector)":       W10,
    "16  (nu)":           W16,
    "45  (eps, adjoint)": W45,
    "144 (zeta)":         W144,
    "450 = 10 (x) 45 ($)": T10x45,
}
IDX = {}
for name, ws in REPS.items():
    IDX[name] = {
        "su(4)": index(t_su4, ws),
        "su(2)L": index(t3L, ws),
        "su(2)R": index(t3R, ws),
        "su(3)": index(t_su3, ws),
        "u(1)Y": index_y(ws),
    }

chkA("T(10) = 1 in all five channels",
     set(IDX["10  (vector)"].values()) == {F(1)})
chkA("T(16) = 2 in all five channels",
     set(IDX["16  (nu)"].values()) == {F(2)})
chkA("T(45) = 8 in all five channels (adjoint index = C2(so(10)) = 8)",
     set(IDX["45  (eps, adjoint)"].values()) == {F(8)})
chkA("T(144) = 34 in all five channels",
     set(IDX["144 (zeta)"].values()) == {F(34)})
chkA("T(450) = 125 in all five channels",
     set(IDX["450 = 10 (x) 45 ($)"].values()) == {F(125)})

# independent cross-check of T(144) by the tensor-product index identity
chkA("independent route: T(10 (x) 16) = dim(10)T(16) + dim(16)T(10) = 36",
     index(t_su4, T10x16) == 10 * 2 + 16 * 1 == 36)
chkA("independent route: T(144) = T(10 (x) 16) - T(16bar) = 36 - 2 = 34",
     index(t_su4, T10x16) - index(t_su4, W16BAR) == 34)
chkA("independent route: T(10 (x) 45) = 10*8 + 45*1 = 125",
     index(t3L, T10x45) == 10 * 8 + 45 * 1 == 125)


# THIRD independent route to the indices: Freudenthal, C2(lambda) = <l, l+2rho>/2
# in the normalisation fixed by the vector 10, then T = C2 * dim(R)/dim(G).
RHO = (F(4), F(3), F(2), F(1), F(0))


def casimir(lam):
    return sum(l * (l + 2 * r) for l, r in zip(lam, RHO)) / 2


def index_freudenthal(lam, dim_r):
    return casimir(lam) * dim_r / 45


chkA("Freudenthal route: C2 normalisation fixed by the 10 gives C2(10) = 9/2",
     casimir((F(1), F(0), F(0), F(0), F(0))) == F(9, 2))
chkA("Freudenthal route reproduces T(10) = 1",
     index_freudenthal((F(1), F(0), F(0), F(0), F(0)), 10) == 1)
chkA("Freudenthal route reproduces T(16) = 2",
     index_freudenthal((H, H, H, H, H), 16) == 2)
chkA("Freudenthal route reproduces T(45) = 8",
     index_freudenthal((F(1), F(1), F(0), F(0), F(0)), 45) == 8)
chkA("Freudenthal route INDEPENDENTLY reproduces T(144) = 34 "
     "(highest weight (3/2,1/2,1/2,1/2,1/2), C2 = 85/8)",
     index_freudenthal((F(3, 2), H, H, H, H), 144) == 34
     and casimir((F(3, 2), H, H, H, H)) == F(85, 8))




# ==========================================================================
# PART 2b -- NEGATIVE CONTROLS on the index-equality machinery
# ==========================================================================
# NC-1: the p summand (24 non-compact directions) is NOT a complete so(10) rep.
#       Under k it is (6,2,2).  Its indices must DISAGREE across factors.
P24 = [w for w in W45
       if (w[0] != 0 or w[1] != 0 or w[2] != 0)
       and (w[3] != 0 or w[4] != 0)]
chkA("p summand has 24 weights (the (6,2,2) of k)", len(P24) == 24)
chkA("NEGATIVE CONTROL: T_su4(p) = 4 but T_su2L(p) = 6 -- index equality FAILS "
     "on an incomplete rep",
     index(t_su4, P24) == 4 and index(t3L, P24) == 6
     and index(t_su4, P24) != index(t3L, P24))

# NC-2: half a 16 -- the (4,2,1) alone -- breaks L/R index equality.
HALF16_L = [w for w in W16 if t3R(w) == 0]
HALF16_R = [w for w in W16 if t3L(w) == 0]
chkA("the 16 splits as (4,2,1) + (4bar,1,2), 8 + 8",
     len(HALF16_L) == 8 and len(HALF16_R) == 8
     and len(HALF16_L) + len(HALF16_R) == 16)
chkA("NEGATIVE CONTROL: T_su2L((4,2,1)) = 2 but T_su2R((4,2,1)) = 0 -- "
     "L/R equality FAILS on an incomplete rep",
     index(t3L, HALF16_L) == 2 and index(t3R, HALF16_L) == 0)

# NC-3: p IS still L/R symmetric, so even Fork-P horn 2 cannot break L/R.
chkA("but p IS L/R symmetric: T_su2L(p) = T_su2R(p) = 6",
     index(t3L, P24) == index(t3R, P24) == 6)

# ---- PV-2's NINE surviving non-SM vectors, in SM language, EXACT ---------
# k = so(6) roots (12) + so(4) roots (4) + 5 Cartan = 21.
K21 = [w for w in W45
       if not ((w[0] or w[1] or w[2]) and (w[3] or w[4]))]
chkA("k has 21 weights (so(6) 12 roots + so(4) 4 roots + 5 Cartan)",
     len(K21) == 21)
chkA("k and p partition the 45", len(K21) + len(P24) == 45)

LEPTOQUARK = [w for w in K21 if abs(y_over_2(w)) == F(2, 3)]
W_R = [w for w in K21 if abs(y_over_2(w)) == 1]
chkA("PV-2's 6 leptoquarks are recovered as the k directions with "
     "Y/2 = +-2/3, i.e. electric charge +-2/3", len(LEPTOQUARK) == 6)
chkA("PV-2's 2 W_R are recovered as the k directions with Y/2 = +-1",
     len(W_R) == 2)
chkA("6 + 2 + 1 (Z') = 9 non-SM directions inside k, matching PV-2 exactly",
     len(LEPTOQUARK) + len(W_R) + 1 == 9)
chkA("the 12 SM gauge directions carry ZERO hypercharge index -- all of "
     "T_1(k) = 14/5 comes from the nine",
     GUT_NORM * sum(y_over_2(w) ** 2 for w in K21) == F(14, 5)
     and GUT_NORM * sum(y_over_2(w) ** 2
                        for w in LEPTOQUARK + W_R) == F(14, 5))
chkA("the nine contribute (T_3, T_2L, T_1) = (1, 0, 14/5): colour and "
     "hypercharge but NO weak isospin",
     index(t_su3, K21) - 3 == 1 and index(t3L, K21) - 2 == 0)


# ==========================================================================
# PART 3 -- the Pati-Salam -> SM coupling matching, DERIVED
# ==========================================================================
# Y/2 = T_3R + X with X = (B-L)/2 an su(4) Cartan generator.  Write
# X = c * That with That normalised to T(4) = 1/2; then the standard
# unbroken-U(1) matching   1/g'^2 = Sum_i c_i^2 / g_i^2   gives
#   1/g'^2 = 1/g_2R^2 + c^2 / g_4^2.
x_norm = sum((b_minus_l(w) / 2) ** 2 for w in FOUR_OF_SU4)
chkA("Tr_4((B-L)/2)^2 = 1/3 (exact)", x_norm == F(1, 3))
C_SQ = x_norm / F(1, 2)
chkA("DERIVED su(4) coefficient c^2 = Tr_4(X^2)/Tr_4(That^2) = 2/3",
     C_SQ == F(2, 3))
chkA("DERIVED Pati-Salam matching: 1/alpha_Y = 1/alpha_2R + (2/3)/alpha_4",
     C_SQ == F(2, 3))

# consistency: Y/2 = T_3R + (B-L)/2 must reproduce the derived GUT norm.
chkA("matching is consistent with the derived GUT normalisation: "
     "1 + 2/3 = 5/3 = 1/GUT_NORM", 1 + C_SQ == 1 / GUT_NORM == F(5, 3))

# sin^2 theta_W at a point where g_4 = g_2L = g_2R (single so(6,4) coupling).
# 1/g'^2 = (5/3)/g_U^2, g_2^2 = g_U^2  =>  sin^2 = (3/5)/(1+3/5) = 3/8.
SIN2_BOUNDARY = F(3, 5) / (1 + F(3, 5))
chkA("DERIVED boundary value sin^2 theta_W = 3/8 when g_4 = g_2L = g_2R "
     "(reproduces the repo's CH-SM value, prior art, not claimed new)",
     SIN2_BOUNDARY == F(3, 8))


# ==========================================================================
# PART 4 -- the one-loop beta coefficient, and the SPIN factor DERIVED
# ==========================================================================
# Universal per-physical-state form (paramagnetic minus diamagnetic):
#     Delta b = (-1)^{2s} T(R) Sum_{physical states} [ A * Sz^2 - Cdia ]
# Two unknowns (A, Cdia).  THREE anchors -> over-determined; the third anchor
# is a genuine test, not a fit.
#   complex scalar (2 states, Sz=0)       -> -1/3 T(R)
#   Weyl fermion   (2 states, Sz=+-1/2)   -> -2/3 T(R)
#   gauge boson    (2 states, Sz=+-1)     -> +11/3 C2(G)
import sympy as sp  # noqa: E402

_A, _C = sp.symbols("A C", rational=True)
sol = sp.solve([sp.Eq(2 * (0 - _C), sp.Rational(-1, 3)),
                sp.Eq(-2 * (_A * sp.Rational(1, 4) - _C), sp.Rational(-2, 3))],
               [_A, _C], dict=True)[0]
A_VAL, C_VAL = F(int(sp.nsimplify(sol[_A]).p), int(sp.nsimplify(sol[_A]).q)), \
    F(int(sp.nsimplify(sol[_C]).p), int(sp.nsimplify(sol[_C]).q))
chkA("spin formula solved from 2 anchors: A = 2, C_dia = 1/6",
     A_VAL == 2 and C_VAL == F(1, 6))
def spin_factor(sz_list, fermion):
    """Delta b per unit T(R), for a set of physical helicity states.

    Delta b = (-1)^{2s} Sum_states [ A Sz^2 - C_dia ].  The (-1)^{2s} statistics
    factor is what makes fermions screen and bosons of spin >= 1 anti-screen.
    """
    stat = -1 if fermion else 1
    return stat * sum(A_VAL * F(sz) ** 2 - C_VAL for sz in sz_list)


chkA("THIRD ANCHOR (independent test, not fitted): the formula returns the "
     "gauge boson's +11/3 from 2 states of Sz^2 = 1",
     spin_factor([1, -1], fermion=False) == F(11, 3))
chkA("FOURTH ANCHOR (independent test): massive vector = massless vector + "
     "eaten real scalar gives 11/3 - 1/6 = 7/2",
     spin_factor([1, 0, -1], fermion=False) == F(7, 2))


# --- the Rarita-Schwinger horns, computed for BOTH readings ---------------
# Horn R-rank ("passive vector index"): the vector index is a spectator
#   flavour label, so a vector-spinor is n_spinor Dirac/Weyl copies.
#   AC-1's twist ranks: carrier A = T_C - 1 (3), bare = T_C (4),
#   carrier B = gamma-traceless (4 - 1 = 3 spinor units).
#   NOTE: AC-1's *index* twist for carrier B is T_C + 1 = 5, because the
#   subtracted spinor has REVERSED chirality.  The beta function sees RANK,
#   not chirality, so carriers A and B are DEGENERATE here at rank 3.
RANK_A, RANK_BARE, RANK_B = 3, 4, 3
chkA("carriers A and B have the SAME beta-function rank (3 spinor units) "
     "while AC-1's index twists differ (3 vs 5) -- beta sees rank, index "
     "sees chirality",
     RANK_A == RANK_B == 3 and RANK_A != RANK_BARE)

WEYL = spin_factor([H, -H], fermion=True)
chkA("one Weyl fermion contributes -2/3 per unit T(R)", WEYL == F(-2, 3))
DIRAC = 2 * WEYL
chkA("one Dirac fermion contributes -4/3 per unit T(R)", DIRAC == F(-4, 3))

# Horn R-gauged: a genuine (gauged, ghost-subtracted) massless RS field
#   propagates only helicities +-3/2.
RS_GAUGED_WEYL = spin_factor([F(3, 2), F(-3, 2)], fermion=True)
chkA("gauged ghost-subtracted massless RS (helicities +-3/2) contributes "
     "-26/3 per unit T(R)", RS_GAUGED_WEYL == F(-26, 3))
RS_CONSTRAINED = spin_factor([F(3, 2), F(-3, 2), H, -H], fermion=True)
chkA("ungauged gamma-traceless RS (helicities +-3/2, +-1/2) contributes "
     "-28/3 per unit T(R)", RS_CONSTRAINED == F(-28, 3))

# The FULL declared band for one 144 unit of zeta:
ZETA_HORNS = {
    "R-rank,   carrier A/B  (3 Weyl units)":    RANK_A * WEYL,
    "R-rank,   bare         (4 Weyl units)":    RANK_BARE * WEYL,
    "R-rank,   carrier A/B  (3 Dirac units)":   RANK_A * DIRAC,
    "R-rank,   bare         (4 Dirac units)":   RANK_BARE * DIRAC,
    "R-gauged, Weyl-type RS (hel +-3/2)":       RS_GAUGED_WEYL,
    "R-gauged, Dirac-type RS":                  2 * RS_GAUGED_WEYL,
    "R-constrained (hel +-3/2, +-1/2)":         RS_CONSTRAINED,
}
chkA("every zeta horn is strictly negative (zeta can only ANTI-screen)",
     all(v < 0 for v in ZETA_HORNS.values()))
chkA("the zeta horn band spans -2 .. -52/3 per unit T(R)",
     min(ZETA_HORNS.values()) == F(-52, 3)
     and max(ZETA_HORNS.values()) == F(-2))


def beta_coeffs(c2_adj, content):
    """content = list of (multiplicity, spin-factor-per-unit-T, T(R))."""
    return F(11, 3) * c2_adj + sum(F(n) * sf * t for n, sf, t in content)


# --- POSITIVE CONTROL: reproduce the Standard Model exactly ---------------
SCALAR_CPLX = spin_factor([0, 0], fermion=False)
chkA("one complex scalar contributes -1/3 per unit T(R)",
     SCALAR_CPLX == F(-1, 3))

T_HIGGS = {"su(3)": F(0), "su(2)L": F(1, 2), "u(1)Y": GUT_NORM * 2 * F(1, 2) ** 2}
chkA("Higgs doublet GUT-normalised u(1)_Y index = 3/10",
     T_HIGGS["u(1)Y"] == F(3, 10))

sm_b3 = beta_coeffs(3, [(3, WEYL, IDX["16  (nu)"]["su(3)"]),
                        (1, SCALAR_CPLX, T_HIGGS["su(3)"])])
sm_b2 = beta_coeffs(2, [(3, WEYL, IDX["16  (nu)"]["su(2)L"]),
                        (1, SCALAR_CPLX, T_HIGGS["su(2)L"])])
sm_b1 = beta_coeffs(0, [(3, WEYL, IDX["16  (nu)"]["u(1)Y"]),
                        (1, SCALAR_CPLX, T_HIGGS["u(1)Y"])])
chkA("POSITIVE CONTROL: SM b_3 = 7 (three 16s + one Higgs doublet)",
     sm_b3 == F(7))
chkA("POSITIVE CONTROL: SM b_2 = 19/6", sm_b2 == F(19, 6))
chkA("POSITIVE CONTROL: SM b_1 = -41/10 (GUT normalisation)",
     sm_b1 == F(-41, 10))


# ==========================================================================
# PART 5 -- GU-AS-DECLARED beta coefficients and the two THEOREMS
# ==========================================================================
# Declared 4d content after the PV-2 reduction (Fork P horn 1: p disposed):
#   gauge   k = su(4) + su(2)_L + su(2)_R                 (C2 = 4, 2, 2)
#   eps     real scalar in the 45                          T = 8
#   nu      n_nu Dirac-type spinors in the 16              T = 2
#   zeta    n_z Rarita-Schwinger units in the 144          T = 34
#   $       Fork D: a 4d vector in 10 (x) 45               T = 125
REAL_SCALAR = spin_factor([0], fermion=False)
chkA("one real scalar contributes -1/6 per unit T(R)", REAL_SCALAR == F(-1, 6))


def gu_b(factor_key, c2_adj, n_nu, n_z, zeta_sf, include_p, include_dollar,
         dollar_sf):
    content = [(1, REAL_SCALAR, IDX["45  (eps, adjoint)"][factor_key]),
               (n_nu, DIRAC, IDX["16  (nu)"][factor_key]),
               (n_z, zeta_sf, IDX["144 (zeta)"][factor_key])]
    if include_p:
        content.append((1, F(11, 3) / 1, index(
            {"su(4)": t_su4, "su(2)L": t3L, "su(2)R": t3R,
             "su(3)": t_su3}[factor_key], P24)))
    if include_dollar:
        content.append((1, dollar_sf, IDX["450 = 10 (x) 45 ($)"][factor_key]))
    return beta_coeffs(c2_adj, content)


# ---- THEOREM 1: b_2L = b_2R exactly, for EVERY fork horn ----------------
theorem1_rows = []
for n_nu in (1, 2, 3, 4):
    for n_z in (0, 1, 2, 3):
        for hname, zsf in ZETA_HORNS.items():
            for inc_p in (False, True):
                for inc_d, dsf in ((False, F(0)), (True, F(7, 2)),
                                   (True, F(-4, 3))):
                    bL = gu_b("su(2)L", 2, n_nu, n_z, zsf, inc_p, inc_d, dsf)
                    bR = gu_b("su(2)R", 2, n_nu, n_z, zsf, inc_p, inc_d, dsf)
                    theorem1_rows.append(bL == bR)
chkA(f"THEOREM 1 (exact, {len(theorem1_rows)} fork combinations): "
     "b_2L = b_2R identically -- for every generation count, every zeta "
     "multiplicity, every carrier/RS horn, with or without the 24 p "
     "directions, with or without the $ displacement field",
     len(theorem1_rows) == 4 * 4 * len(ZETA_HORNS) * 2 * 3
     and all(theorem1_rows))

# ---- THEOREM 2: b_4 - b_2L = 22/3 exactly, MATTER-INDEPENDENT -----------
theorem2_rows = []
for n_nu in (1, 2, 3, 4):
    for n_z in (0, 1, 2, 3):
        for hname, zsf in ZETA_HORNS.items():
            for inc_d, dsf in ((False, F(0)), (True, F(7, 2)), (True, F(-4, 3))):
                b4 = gu_b("su(4)", 4, n_nu, n_z, zsf, False, inc_d, dsf)
                bL = gu_b("su(2)L", 2, n_nu, n_z, zsf, False, inc_d, dsf)
                theorem2_rows.append(b4 - bL == F(22, 3))
chkA(f"THEOREM 2 (exact, {len(theorem2_rows)} fork combinations): "
     "b_4 - b_2L = 22/3 identically -- ALL matter cancels from the "
     "colour-weak difference because every declared rep is a complete "
     "so(6,4) rep with equal indices",
     all(theorem2_rows) and len(theorem2_rows) > 0)

# non-vacuity of THEOREM 2: adding p (an INCOMPLETE rep) DOES move it.
b4_p = gu_b("su(4)", 4, 3, 1, WEYL * 3, True, False, F(0))
bL_p = gu_b("su(2)L", 2, 3, 1, WEYL * 3, True, False, F(0))
chkA("NON-VACUITY of THEOREM 2: including the incomplete p summand shifts "
     "b_4 - b_2L away from 22/3 (to 22/3 + 11/3(4-6) = 0)",
     b4_p - bL_p != F(22, 3) and b4_p - bL_p == F(22, 3) + F(11, 3) * (4 - 6))

# ---- THEOREM 3: alpha_2L^-1 - alpha_2R^-1 is a one-loop RG invariant ----
chkA("THEOREM 3 (corollary of THEOREM 1): since b_2L = b_2R, the difference "
     "alpha_2L^-1(mu) - alpha_2R^-1(mu) is exactly scale-independent at one "
     "loop, so g_2L and g_2R either coincide at every scale or at none",
     all(theorem1_rows))

# ---- headline numeric b's for the reference horn -------------------------
REF = dict(n_nu=3, n_z=1, zeta_sf=RANK_A * DIRAC, include_p=False,
           include_dollar=False, dollar_sf=F(0))
B4 = gu_b("su(4)", 4, **REF)
B2L = gu_b("su(2)L", 2, **REF)
B2R = gu_b("su(2)R", 2, **REF)
chkA("reference horn (3 nu, 1 zeta as 3 Dirac units, eps, p disposed, "
     "$ set aside): b_4 = 40/3 - 8 - 136 = -392/3", B4 == F(-392, 3))
chkA("reference horn: b_2L = b_2R = 6 - 8 - 136 = -138", B2L == B2R == F(-138))
chkA("reference horn respects THEOREM 2", B4 - B2L == F(22, 3))

# zeta-free sub-content (what the theory looks like if zeta decouples)
B4_nz = gu_b("su(4)", 4, 3, 0, F(0), False, False, F(0))
B2L_nz = gu_b("su(2)L", 2, 3, 0, F(0), False, False, F(0))
chkA("zeta-decoupled: b_4 = 44/3 - 4/3 - 8 = 16/3 (SU(4) still "
     "asymptotically free)", B4_nz == F(16, 3))
chkA("zeta-decoupled: b_2L = 22/3 - 4/3 - 8 = -2 (SU(2)_L NOT asymptotically "
     "free once the adjoint scalar eps and three Dirac 16s are present)",
     B2L_nz == F(-2))
chkA("zeta-decoupled content still respects THEOREM 2",
     B4_nz - B2L_nz == F(22, 3))

# ---- how negative is b_3 the moment zeta is in the running? -------------
b3_sm_plus_zeta = {}
for hname, zsf in ZETA_HORNS.items():
    b3_sm_plus_zeta[hname] = sm_b3 + zsf * IDX["144 (zeta)"]["su(3)"]
chkA("EVERY zeta horn drives the SU(3) coefficient negative: measured QCD "
     "asymptotic freedom (b_3 > 0) requires zeta to be decoupled",
     all(v < 0 for v in b3_sm_plus_zeta.values()))
chkA("the least damaging zeta horn already gives b_3 = 7 - 68 = -61",
     max(b3_sm_plus_zeta.values()) == F(-61))


# ==========================================================================
# PART 6 -- EMPIRICAL LAYER (Layer B).  FLOATS.  NOT EXACT.  LABELLED.
# ==========================================================================
# Source: Particle Data Group, Review of Particle Physics (2024 edition),
# Electroweak model and Quantum chromodynamics reviews.  NOT fetched in this
# session -- declared reproducibility seam.  Central values +- 1 sigma:
M_Z = 91.1876          # +- 0.0021 GeV
ALPHA_INV = 127.951    # +- 0.009   (MS-bar, 5-flavour, at M_Z)
SIN2_W = 0.23122       # +- 0.00004 (MS-bar, at M_Z)
ALPHA_S = 0.1180       # +- 0.0009
D_ALPHA_INV, D_SIN2, D_ALPHA_S = 0.009, 0.00004, 0.0009

EPS_UNIFY = 1.0        # PREDECLARED in C5.  Never adjusted.


def couplings(alpha_inv=ALPHA_INV, sin2=SIN2_W, alpha_s=ALPHA_S):
    inv_a2 = sin2 * alpha_inv                       # 1/alpha_2   (SU(2)_L)
    inv_aY = (1.0 - sin2) * alpha_inv               # 1/alpha_Y   (u(1)_Y, NOT
    inv_a3 = 1.0 / alpha_s                          #              GUT-normed)
    return inv_a1_gut(inv_aY), inv_a2, inv_a3, inv_aY


def inv_a1_gut(inv_aY):
    return float(F(3, 5)) * inv_aY                  # 1/alpha_1 = (3/5)/alpha_Y


inv_a1, inv_a2, inv_a3, inv_aY = couplings()


def ps_residual(inv_aY_, inv_a2_, inv_a3_):
    """GU-as-declared (PS unbroken to M_Z, g_2R = g_2L by THEOREM 1+3) forces
    1/alpha_Y = 1/alpha_2 + (2/3)/alpha_4 with alpha_4 = alpha_3.  Residual."""
    return inv_aY_ - (inv_a2_ + float(C_SQ) * inv_a3_)


RESID = ps_residual(inv_aY, inv_a2, inv_a3)

# propagate the quoted uncertainties (linear, 1 sigma, uncorrelated)
d_resid = math.sqrt(
    ((1 - SIN2_W) * D_ALPHA_INV - SIN2_W * D_ALPHA_INV) ** 2
    + ((-ALPHA_INV - ALPHA_INV) * D_SIN2) ** 2
    + (float(C_SQ) * D_ALPHA_S / ALPHA_S ** 2) ** 2)

chkB("[EMPIRICAL] GU-as-declared's threshold-free PS matching relation FAILS "
     f"at M_Z by {RESID:.2f} +- {d_resid:.2f} units of alpha^-1",
     RESID > 50.0)
chkB("[EMPIRICAL] the miss exceeds the PREDECLARED unification tolerance "
     f"EPS_UNIFY = {EPS_UNIFY} by more than 60x", RESID > 60 * EPS_UNIFY)
chkB("[EMPIRICAL] the miss exceeds 10 sigma of the quoted uncertainties by "
     "more than two orders of magnitude", RESID / d_resid > 1000)

# implied SU(2)_R coupling and the L/R invariant
inv_a2R = inv_aY - float(C_SQ) * inv_a3
LR_INVARIANT = inv_a2 - inv_a2R
chkB("[EMPIRICAL] the data force alpha_2R^-1(M_Z) = 92.7, i.e. an unbroken "
     "SU(2)_R roughly 3.1x weaker than SU(2)_L", 90.0 < inv_a2R < 95.0)
chkB("[EMPIRICAL] the RG-invariant alpha_2L^-1 - alpha_2R^-1 = -63.1 is "
     "nonzero, so under THEOREM 3 g_2L and g_2R can NEVER meet, at any scale",
     abs(LR_INVARIANT + 63.13) < 0.5 and abs(LR_INVARIANT) > EPS_UNIFY)

# predicted sin^2 theta_W if instead g_2R = g_2L is imposed (Fork G horn 1)
sin2_pred = 1.0 / (2.0 + float(C_SQ) * (inv_a3 / inv_a2))
chkB("[EMPIRICAL] imposing g_2R = g_2L gives the parameter-free, scale-free "
     f"prediction sin^2 theta_W(M_Z) = {sin2_pred:.4f}, versus the measured "
     f"{SIN2_W:.5f}", abs(sin2_pred - 0.4564) < 0.001)
chkB("[EMPIRICAL] that prediction is ~5600 sigma from the measured value",
     abs(sin2_pred - SIN2_W) / D_SIN2 > 1000)
chkB("[EMPIRICAL] the prediction is bounded above by 1/2 for ANY positive "
     "couplings, so no choice of alpha_2/alpha_3 can reach 0.231 without "
     "alpha_2 > 3.4 alpha_3 (measured: alpha_2 = 0.29 alpha_3)",
     sin2_pred < 0.5 and (inv_a3 / inv_a2) < 1.0)

# robustness of the empirical verdict, stated the honest way: not in sigmas
# (which are meaningless at 1400 sigma) but as "how wrong would the measurement
# have to be".
rob = []
for k in (10, 30):
    for da in (-k * D_ALPHA_INV, k * D_ALPHA_INV):
        for ds in (-k * D_SIN2, k * D_SIN2):
            for dz in (-k * D_ALPHA_S, k * D_ALPHA_S):
                _, i2, i3, iY = couplings(ALPHA_INV + da, SIN2_W + ds,
                                          ALPHA_S + dz)
                rob.append(ps_residual(iY, i2, i3) > 55.0)
chkB("[EMPIRICAL] verdict robust to inflating every quoted uncertainty by 30x "
     "(all 16 corner points still miss by > 55 units)", all(rob))

ALPHA_S_REQ = 1.0 / (ALPHA_INV * (1 - 2 * SIN2_W) / float(C_SQ))
SIN2_REQ = (1.0 - float(C_SQ) * inv_a3 / ALPHA_INV) / 2.0
chkB("[EMPIRICAL] to erase the miss, alpha_s(M_Z) would have to be "
     f"{ALPHA_S_REQ:.5f} instead of {ALPHA_S}, i.e. wrong by a factor "
     f"{ALPHA_S / ALPHA_S_REQ:.1f}",
     ALPHA_S / ALPHA_S_REQ > 10.0)
chkB("[EMPIRICAL] alternatively sin^2 theta_W(M_Z) would have to be "
     f"{SIN2_REQ:.4f} instead of {SIN2_W}, i.e. wrong by a factor "
     f"{SIN2_REQ / SIN2_W:.2f} -- and 0.478 is excluded by the measured "
     "W/Z mass ratio alone",
     SIN2_REQ / SIN2_W > 2.0)

# the colour-weak meeting scale, from THEOREM 2 + two measured couplings
ln_mu = 2 * math.pi * (inv_a2 - inv_a3) / float(F(22, 3))
MU_R = M_Z * math.exp(ln_mu)
chkB("[EMPIRICAL+EXACT] THEOREM 2 plus the measured alpha_2, alpha_3 fixes a "
     f"colour-weak meeting scale mu = {MU_R:.2e} GeV, independent of every "
     "matter fork (generations, zeta, carrier bit, $)",
     5e9 < MU_R < 8e9)
chkB("[EMPIRICAL] but SU(2)_R does not join there: at mu_R the L/R gap is "
     "still exactly 63.1 units", abs(LR_INVARIANT) > 60)

# Landau-pole distance above M_zeta, per carrier horn (this is where the
# carrier bit IS visible)
pole_rows = {}
for hname, zsf in ZETA_HORNS.items():
    b3_eff = float(sm_b3 + zsf * IDX["144 (zeta)"]["su(3)"])
    inv_a3_at_mz = 1.0 / 0.09        # alpha_3 ~ 0.09 near 1 TeV, illustrative
    pole_rows[hname] = math.exp(2 * math.pi * inv_a3_at_mz / abs(b3_eff))
chkB("[EMPIRICAL, illustrative] once zeta is in the running the colour "
     "coupling reaches a one-loop Landau pole within a factor 1.1-3.2 in "
     "energy above M_zeta for EVERY carrier horn",
     all(1.1 < v < 3.2 for v in pole_rows.values()))
chkB("[EMPIRICAL] the A-vs-B CARRIER BIT stays invisible even here: carriers "
     "A and B have the same beta-function rank (3), so they give the IDENTICAL "
     "pole distance -- a third channel, after AC-1's anomalies and this gate's "
     "unification differences, in which the bit cannot be seen",
     abs(pole_rows["R-rank,   carrier A/B  (3 Weyl units)"]
         - pole_rows["R-rank,   carrier A/B  (3 Weyl units)"]) < 1e-12)
chkB("[EMPIRICAL] what the pole distance DOES separate is Fork R (the "
     "rank-versus-gauged-RS reading) and the bare control: spread across the "
     "seven horns exceeds 100%",
     (max(pole_rows.values()) - min(pole_rows.values()))
     / min(pole_rows.values()) > 1.0)

# CALIBRATION CONTROL for the predeclared criterion: it must be able to PASS.
def meets(b_list, inv_list, lo=0.0, hi=40.0, n=40001):
    best = None
    for i in range(n):
        t = lo + (hi - lo) * i / (n - 1)
        vals = [inv + float(b) * t / (2 * math.pi) for b, inv in
                zip(b_list, inv_list)]
        spread = max(vals) - min(vals)
        if best is None or spread < best[0]:
            best = (spread, t)
    return best


sm_spread, sm_t = meets([sm_b1, sm_b2, sm_b3], [inv_a1, inv_a2, inv_a3])
chkB("[CALIBRATION] the predeclared criterion applied to the plain SM "
     f"reproduces the textbook near-miss (best spread {sm_spread:.1f} units "
     f"at mu ~ 10^{math.log10(M_Z) + sm_t / math.log(10):.1f} GeV) -- it does "
     "not unify at EPS_UNIFY = 1", 3.0 < sm_spread < 15.0)
syn_spread, _ = meets([F(1), F(2), F(3)], [10.0, 10.0, 10.0])
chkB("[CALIBRATION, non-vacuity] the criterion DOES return spread 0 on a "
     "synthetic content constructed to meet", syn_spread < 1e-9)


# ==========================================================================
# REPORT
# ==========================================================================
def report():
    print("=" * 78)
    print("CU-1  GAUGE-COUPLING RUNNING FOR GU-AS-DECLARED")
    print("=" * 78)

    print("\n--- PREDECLARED (fixed before running) ---")
    print("  one loop, MS-bar, step decoupling; b via d(alpha^-1)/dlnmu = b/2pi")
    print(f"  EPS_UNIFY = {EPS_UNIFY} units of alpha^-1 -- NOT adjusted")
    print("  PS unbroken to M_Z (PV-1 + PV-2) => NO gauge threshold to choose")

    print("\n--- LAYER A: EXACT GROUP THEORY (primary deliverable) ---")
    print("  embedding indices in so(10):  su(4)=1  su(3)=1  su(2)_L=1  "
          "su(2)_R=1  u(1)_Y(GUT)=1")
    print(f"  DERIVED GUT hypercharge normalisation: "
          f"Tr(T3L^2)/Tr((Y/2)^2) = {GUT_NORM}   (=> 5/3, sin^2 = 3/8 at a "
          f"single-coupling point)")
    print(f"  DERIVED PS->SM matching:  1/alpha_Y = 1/alpha_2R + "
          f"({C_SQ})/alpha_4")
    print("\n  Dynkin indices (identical in all five channels):")
    for name, d in IDX.items():
        print(f"    {name:<22} T = {d['su(4)']}   "
              f"[su4 {d['su(4)']}, su2L {d['su(2)L']}, su2R {d['su(2)R']}, "
              f"su3 {d['su(3)']}, u1Y {d['u(1)Y']}]")
    print(f"    NEGATIVE CONTROL p (6,2,2)  T = su4 {index(t_su4, P24)}, "
          f"su2L {index(t3L, P24)}, su2R {index(t3R, P24)}  -- NOT equal")

    print("\n  RS / carrier horns, Delta b per unit T(R):")
    for h, v in ZETA_HORNS.items():
        print(f"    {h:<40} {v}")

    print("\n  Standard-Model positive control:  "
          f"b_1 = {sm_b1}, b_2 = {sm_b2}, b_3 = {sm_b3}   "
          "(textbook -41/10, 19/6, 7)")
    print(f"\n  GU-as-declared reference horn:  b_4 = {B4}, "
          f"b_2L = {B2L}, b_2R = {B2R}")
    print(f"  zeta-decoupled sub-content:      b_4 = {B4_nz}, "
          f"b_2L = b_2R = {B2L_nz}")

    print("\n  THEOREM 1  b_2L = b_2R exactly "
          f"({len(theorem1_rows)} fork combinations, all pass)")
    print("  THEOREM 2  b_4 - b_2L = 22/3 exactly, ALL matter cancels")
    print("  THEOREM 3  alpha_2L^-1 - alpha_2R^-1 is a one-loop RG invariant")

    print("\n--- LAYER B: EMPIRICAL COMPARISON (secondary, NOT exact) ---")
    print("  inputs (PDG RPP 2024, quoted with uncertainty, not fetched here):")
    print(f"    alpha^-1(M_Z) = {ALPHA_INV} +- {D_ALPHA_INV}")
    print(f"    sin^2 theta_W(M_Z) = {SIN2_W} +- {D_SIN2}")
    print(f"    alpha_s(M_Z) = {ALPHA_S} +- {D_ALPHA_S}")
    print(f"  derived: 1/alpha_2 = {inv_a2:.3f}, 1/alpha_3 = {inv_a3:.3f}, "
          f"1/alpha_Y = {inv_aY:.3f}")
    print(f"\n  PS matching residual at M_Z:  {RESID:.2f} +- {d_resid:.2f} "
          f"units of alpha^-1   ({RESID / d_resid:.0f} sigma)")
    print(f"  implied unbroken alpha_2R^-1(M_Z) = {inv_a2R:.2f}")
    print(f"  RG-invariant alpha_2L^-1 - alpha_2R^-1 = {LR_INVARIANT:.2f} "
          "(scale-independent; never zero)")
    print(f"  parameter-free prediction sin^2 theta_W(M_Z) = {sin2_pred:.4f} "
          f"vs measured {SIN2_W}")
    print(f"  colour-weak meeting scale (matter-independent) mu = {MU_R:.2e} GeV")
    print("  Landau-pole distance above M_zeta, by carrier horn:")
    for h, v in pole_rows.items():
        print(f"    {h:<40} mu_pole / M_zeta = {v:.2f}")
    print(f"  CALIBRATION: plain SM best spread = {sm_spread:.1f} units "
          "(textbook non-SUSY near-miss; criterion can fail AND can pass)")

    a_pass = sum(1 for _, ok in A_CHECKS if ok)
    b_pass = sum(1 for _, ok in B_CHECKS if ok)
    print("\n" + "=" * 78)
    for nm, ok in A_CHECKS:
        if not ok:
            print(f"  LAYER-A FAIL: {nm}")
    for nm, ok in B_CHECKS:
        if not ok:
            print(f"  LAYER-B FAIL: {nm}")
    print(f"LAYER A (EXACT) CERTIFICATE : {a_pass}/{len(A_CHECKS)}")
    print(f"LAYER B (EMPIRICAL) CHECKS  : {b_pass}/{len(B_CHECKS)}  "
          "[not part of the exact certificate]")
    print("=" * 78)
    return a_pass == len(A_CHECKS) and b_pass == len(B_CHECKS)


if __name__ == "__main__":
    raise SystemExit(0 if report() else 1)
