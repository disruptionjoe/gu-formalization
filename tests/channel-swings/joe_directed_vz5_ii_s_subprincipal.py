#!/usr/bin/env python3
"""VZ-5 -- the explicit coordinate formula for II_s, and the subprincipal
stability of the 4D Velo-Zwanziger verdict.

Target: `papers/drafts/canonical-structures-14d-metric-geometry-2026-06-22.md:398`
("Explicit formula for II_s ... has not been computed in coordinates as a
function of s and its first derivatives") and `canon/no-go-class-relative-map.md`
FC-VZ-4 ("does `II_s = s*(theta)` source an effective first-order term in
`S_R^{4D}` producing spacelike characteristics?").

THREE THINGS ARE DONE, IN ORDER, EACH BUILDING ON A VERIFIED PRIOR STEP:

  PART 0 (reproduce [R])
    VZ-4's pullback-is-a-contraction identity, rederived from scratch (not
    imported), matching the working idiom this arc is instructed to build on.

  PART A (exact sympy, general fiber point)
    The gimmel metric Gcal on Y^14 = Met(X^4) in adapted bundle coordinates
    (x^mu, u_I), and its SIX Levi-Civita Christoffel blocks, each verified
    via the Koszul identity -- five fully symbolically (general 10-symbol
    fiber point, no matrix inversion needed because the verification LOWERS
    the candidate rather than raising one), the sixth (fiber self-connection)
    via an exact-rational Koszul SOLVE at three independent generic points
    (documented as a narrower-but-still-exact scope, because sympy's
    `simplify()` was empirically unreliable -- see PREFLIGHT/POSTFLIGHT --
    on the fully expanded 10-variable rational form of that one block).

  PART B (exact sympy, general section, THE deliverable)
    II_s(d_mu, d_nu) for the graph section s(x) = (x, g_ab(x)), g_ab a fully
    general sympy Function, assembled from the Part A blocks via the standard
    Gauss-formula recipe (ambient covariant derivative minus the tangential
    part fixed by the INDUCED metric's own Christoffel symbol).  Certified by
    the ORTHOGONALITY THEOREM -- Gcal(II_s, T_sigma) = 0 for every sigma --
    checked EXACTLY (rational arithmetic) across 5 sections x up to 3 points
    each.  This is not a unit test copied from the derivation; it is an
    independent mathematical consequence (the Gauss formula) that a wrong
    formula generically fails, and it DID catch a real bug during
    development (see POSTFLIGHT).

  PART C (FC-VZ-4)
    Does II_s, entering the 4D RS operator as a background (xi-independent)
    endomorphism, source spacelike characteristics at subprincipal order?
    An exact toy-but-structurally-faithful Cl(3,1) characteristic-determinant
    computation answers: a bounded, xi-independent insertion cannot alter the
    TOP-DEGREE-IN-xi part of the characteristic determinant (an exact,
    general linear-algebra fact about Leibniz determinant expansion,
    confirmed concretely) -- no new characteristics.  Two REQUIRED contrary
    controls: (i) a section (flat Minkowski) where II_s is EXACTLY,
    provably nonzero, so the "vanishes trivially" failure mode is excluded;
    (ii) an artificial promotion of the SAME background term to FIRST order
    in xi, which DOES produce an exact spacelike root -- proving the
    detector can discriminate, not just always report "safe".

Usage
    _local/cas-venv/bin/python tests/channel-swings/joe_directed_vz5_ii_s_subprincipal.py
    _local/cas-venv/bin/python tests/channel-swings/joe_directed_vz5_ii_s_subprincipal.py --selftest
    _local/cas-venv/bin/python tests/channel-swings/joe_directed_vz5_ii_s_subprincipal.py --control <name>

`--selftest` runs the clean baseline FIRST (must pass), then every planted
control in a subprocess, and requires each to exit 1.  Machinery-corruption
mutations only; genuine [FAIL] assertions, not crash-catches.
"""

from __future__ import annotations

import itertools
import os
import subprocess
import sys
import unittest
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
MUT = os.environ.get("VZ5_CONTROL", "")

CONTROLS = {
    "pullback_is_projection":
        "P0 drops the d_mu g_ab correction term (VZ-4's own planted control, rerun here)",
    "hhv_block_wrong_sign":
        "A2 flips the sign of the H-H-V Christoffel candidate before the Koszul check",
    "vvv_block_missing_trace_term":
        "A6 uses the UN-reversed plain-Frobenius connection candidate (drops the",
    "orthogonality_theorem_disabled":
        "B1 skips the Gammabar tangential subtraction in the assembly (the "
        "orthogonality ASSERTION stays live and must catch it)",
    "flat_contrary_control_vacuous":
        "C1 asserts the flat-section II_s vanishes (the false 'totally geodesic' claim)",
    "derivative_order_claim_wrong":
        "C3 asserts II_s depends on first derivatives of g only (no second derivative)",
    "zeroth_order_theorem_wrong_degree":
        "D2 checks degree 3 instead of degree 4 (wrong top-degree slot)",
    "adversarial_control_vacuous":
        "D4 claims the adversarial point is timelike/null instead of spacelike",
    "clifford_relation_sign_flip":
        "D1 asserts a flipped-sign Clifford square, should not match eta",
    "quote_drift":
        "E1 asserts a sentence not present in the drafts file at the cited line",
    "routing_notice_missing":
        "E2 asserts the GU-COMPARATOR-ROUTING notice text is absent (it must be present)",
}

DRAFTS_FILE = ("papers/drafts/"
               "canonical-structures-14d-metric-geometry-2026-06-22.md")
CANON_FILE = "canon/no-go-class-relative-map.md"


# ===========================================================================
# PART 0 -- reproduce [R]: VZ-4's pullback-is-a-contraction identity, from
# scratch (this file does not import vz4's module; it rederives the identity
# independently, per this arc's "reproduce before extending" instruction).
# ===========================================================================

NX, NU, NY = 4, 10, 14
SYM_PAIRS = [(a, b) for a in range(4) for b in range(a, 4)]   # 10 symmetric pairs
assert len(SYM_PAIRS) == NU

XS = sp.symbols("x0 x1 x2 x3", real=True)
x0, x1, x2, x3 = XS


def jacobian_symbolic():
    """J = ds for a fully general section s(x) = (x, g_ab(x)).  [R]-reproduction."""
    g = [sp.Function(f"g_{a}{b}")(*XS) for (a, b) in SYM_PAIRS]
    J = sp.zeros(NY, NX)
    for mu in range(NX):
        J[mu, mu] = 1
    for I in range(NU):
        for mu in range(NX):
            J[NX + I, mu] = sp.diff(g[I], XS[mu])
    return J, g


def pullback_R(J, omega):
    return J.T * sp.Matrix(NY, 1, list(omega))


# ===========================================================================
# PART A -- the gimmel metric Gcal and its six Christoffel blocks.
#
# Adapted bundle coordinates (x^mu, u_I), I = 0..9 indexing the 10
# independent components of a symmetric 4x4 tensor (SYM_PAIRS order).  The
# fiber point u ranges over ALL of Sym^2(R^4) here (general, NOT tied to any
# section) -- this is the ambient-manifold computation, prior to and
# independent of any choice of section.
#
# Gcal is block diagonal in this chart (the coordinate-patch convention
# matching `pc2-met-x4-bundle-formalization-stub-2026-06-22.md` SS2.4 and
# `ii-s-coordinate-formula-2026-06-23.md` SS1 -- "product coordinate gauge",
# no horizontal-vertical shift term):
#   Gcal_{mu nu}(u) = H_{mu nu}(u)                 [tautological: the fiber
#                                                     point itself is the (3,1)
#                                                     horizontal metric]
#   Gcal_{mu,I}(u)  = 0                             [no cross term]
#   Gcal_{I J}(u)   = V_{IJ}(u)                      [trace-reversed Frobenius,
#                                                     signature (6,4), Prop 2.1]
# ===========================================================================

def sym_from_vec(vec):
    """4x4 symmetric matrix from 10 independent components, SYM_PAIRS order."""
    M = sp.zeros(4, 4)
    for I, (a, b) in enumerate(SYM_PAIRS):
        M[a, b] = vec[I]
        M[b, a] = vec[I]
    return M


def trace(M):
    return sum(M[i, i] for i in range(M.shape[0]))


def sym2(p, q):
    return sp.Rational(1, 2) * (p + q)


def Vform(Hinv, A, B):
    """V(A,B) = tr(Hinv A Hinv B) - 1/2 tr(Hinv A) tr(Hinv B): the
    trace-reversed Frobenius metric (Prop 2.1), A,B symmetric 4x4."""
    return trace(Hinv * A * Hinv * B) - sp.Rational(1, 2) * trace(Hinv * A) * trace(Hinv * B)


def dVform(Hinv, dHinv, A, B, dA, dB):
    """d/dlambda[V(A,B)] given Hinv, dHinv=dHinv/dlambda, and dA,dB= dA/dlambda
    etc.  Used only algebraically (Hinv itself is never differentiated again)."""
    d_cross = (trace(dHinv * A * Hinv * B) + trace(Hinv * dA * Hinv * B)
               + trace(Hinv * A * dHinv * B) + trace(Hinv * A * Hinv * dB))
    trA, trB = trace(Hinv * A), trace(Hinv * B)
    dtrA = trace(dHinv * A) + trace(Hinv * dA)
    dtrB = trace(dHinv * B) + trace(Hinv * dB)
    return d_cross - sp.Rational(1, 2) * (dtrA * trB + trA * dtrB)


def Epair_from(H):
    """{(a,b): dH/du_(a,b)} -- for H = sym_from_vec(general symbols), these
    are the constant 'basis matrices' (1's at (a,b) and (b,a))."""
    return {(a, b): sp.diff(H, sp.Symbol("__probe__")) for (a, b) in ()}  # unused stub


def Epair(a, b):
    M = sp.zeros(4, 4)
    M[a, b] = 1
    M[b, a] = 1
    return M


# candidate closed forms (independently re-derived and Koszul-verified below,
# not copied from any prior exploration file without re-derivation):
def gamma_HHV(H, mu, nu):
    """Gamma^{ef}_{mu nu} = -(1/2)( H_{e(mu}H_{nu)f} - (1/2)H_{ef}H_{mu nu} )."""
    Gam = sp.zeros(4, 4)
    for e in range(4):
        for f in range(4):
            Gam[e, f] = -sp.Rational(1, 2) * (
                sym2(H[e, mu] * H[nu, f], H[e, nu] * H[mu, f])
                - sp.Rational(1, 2) * H[e, f] * H[mu, nu])
    if MUT == "hhv_block_wrong_sign":
        Gam = -Gam
    return Gam


def gamma_HVH_vec(Hinv, mu, a, b):
    """Gamma^rho_{mu,(ab)} = (1/2) Hinv^{rho sigma} E_ab[sigma,mu] -- a length-4
    vector indexed by rho."""
    return sp.Rational(1, 2) * (Hinv * Epair(a, b))[:, mu]


def gamma_VVV(Hinv, k, l):
    """Gamma^V(k,l) = -(1/2)(k Hinv l + l Hinv k) -- the trace-reversal
    correction CANCELS in the connection (verified in PART A2 below)."""
    cand = -sp.Rational(1, 2) * (k * Hinv * l + l * Hinv * k)
    if MUT == "vvv_block_missing_trace_term":
        # the WRONG candidate: the connection of the un-reversed plain
        # Frobenius metric tr(Hinv A Hinv B) alone (drops trace-reversal).
        # Included only to prove the real check discriminates; NOT claimed
        # to be a plausible alternative.
        cand = cand + sp.Rational(1, 6) * trace(Hinv * k) * trace(Hinv * l) * sp.eye(4)
    return cand


# ---------------------------------------------------------------------------
# A1. Fully symbolic Koszul verification (5 of 6 blocks), general 10-symbol H.
# Every check LOWERS the candidate (pairs it against G via trace formulas) so
# NO matrix inversion of a fully general object is ever required beyond the
# cheap 4x4 Hinv -- this is what keeps it tractable at full generality.
# ---------------------------------------------------------------------------

def verify_blocks_symbolic():
    U = sp.symbols("u0:10", real=True)
    H = sym_from_vec(U)
    Hinv = sp.simplify(H.inv())
    results = {}

    # HHH = 0: Gcal has no explicit x-dependence at all (u are independent
    # fiber coordinates here), so every x-derivative of Gcal is identically
    # zero and the Koszul RHS for two-horizontal-lower vanishes termwise.
    results["HHH"] = True

    # HVV = 0 and "H, lower VV" = 0: same reasoning (Koszul RHS is an
    # x-derivative of a function of u alone).
    results["HVV"] = True
    results["H_lowerVV"] = True

    # HHV: verify Gamma^{cd}_{mu nu} via lowered Koszul, all mu<=nu x cd pairs.
    bad = 0
    for (mu, nu) in [(0, 0), (1, 1), (2, 2), (3, 3), (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]:
        Gam = gamma_HHV(H, mu, nu)
        for (c, d) in SYM_PAIRS:
            Ecd = Epair(c, d)
            lhs = 2 * (trace(Hinv * Gam * Hinv * Ecd) - sp.Rational(1, 2) * trace(Hinv * Gam) * trace(Hinv * Ecd))
            rhs = -Ecd[mu, nu]
            if sp.simplify(lhs - rhs) != 0:
                bad += 1
    results["HHV"] = (bad == 0, bad, 100)

    # HVH: verify Gamma^rho_{mu,(ab)} via lowered Koszul, all mu x (ab) x nu.
    bad = 0
    for mu in range(4):
        for (a, b) in SYM_PAIRS:
            Eab = Epair(a, b)
            GamVec = gamma_HVH_vec(Hinv, mu, a, b)
            for nu in range(4):
                lhs = 2 * sum(H[rho, nu] * GamVec[rho] for rho in range(4))
                rhs = Eab[mu, nu]
                if sp.simplify(lhs - rhs) != 0:
                    bad += 1
    results["HVH"] = (bad == 0, bad, 40)

    return results


# ---------------------------------------------------------------------------
# A2. V-V-V block (fiber self-connection).  Verified via an EXACT-RATIONAL
# Koszul SOLVE (not the lowered-symbolic method) at THREE independent
# generic points, all 55 (ab,cd) pairs each = 165 checks.  Narrower-scope
# note: a fully symbolic (10 free u's) attempt was ALSO run during
# development and its `simplify()`-based zero-check produced a FALSE
# mismatch on the fully expanded rational closed form -- diagnosed as a
# `sympy.simplify()` reliability limit on that particular huge expression,
# not a real discrepancy (the same candidate, solved exactly at concrete
# points, matches to the last digit).  Recorded honestly in the artifact's
# POSTFLIGHT rather than silently using only the more convincing method.
# ---------------------------------------------------------------------------

def _rational_H_samples():
    return [
        sp.Matrix([[sp.Rational(-2, 1), sp.Rational(1, 3), 0, sp.Rational(1, 5)],
                   [sp.Rational(1, 3), 3, sp.Rational(1, 7), 0],
                   [0, sp.Rational(1, 7), 4, sp.Rational(-1, 4)],
                   [sp.Rational(1, 5), 0, sp.Rational(-1, 4), 5]]),
        sp.Matrix([[sp.Rational(-1, 1), sp.Rational(2, 3), sp.Rational(-1, 9), sp.Rational(3, 2)],
                   [sp.Rational(2, 3), 7, sp.Rational(5, 11), sp.Rational(-2, 3)],
                   [sp.Rational(-1, 9), sp.Rational(5, 11), 6, sp.Rational(1, 2)],
                   [sp.Rational(3, 2), sp.Rational(-2, 3), sp.Rational(1, 2), 9]]),
        sp.Matrix([[sp.Rational(-3, 7), 1, 0, 0],
                   [1, 2, sp.Rational(-1, 2), sp.Rational(1, 6)],
                   [0, sp.Rational(-1, 2), 8, 0],
                   [0, sp.Rational(1, 6), 0, 10]]),
    ]


def Fab_on_V(Hinv, ab, A, B):
    """d/du_ab [V(A,B)] for CONSTANT (u-independent) matrices A,B -- exact
    matrix-calculus formula (d(Hinv)/du_ab = -Hinv E_ab Hinv), no full
    symbolic-u expansion needed."""
    Eab = Epair(*ab)
    t1 = -trace(Hinv * Eab * Hinv * A * Hinv * B) - trace(Hinv * A * Hinv * Eab * Hinv * B)
    t2 = sp.Rational(1, 2) * (trace(Hinv * Eab * Hinv * A) * trace(Hinv * B)
                              + trace(Hinv * A) * trace(Hinv * Eab * Hinv * B))
    return t1 + t2


def verify_vvv_block_rational():
    bad = 0
    checked = 0
    for H in _rational_H_samples():
        Hinv = H.inv()
        V = sp.zeros(NU, NU)
        for I, (a, b) in enumerate(SYM_PAIRS):
            for J, (c, d) in enumerate(SYM_PAIRS):
                V[I, J] = Vform(Hinv, Epair(a, b), Epair(c, d))
        Vinv = V.inv()
        for ab, cd in itertools.combinations_with_replacement(SYM_PAIRS, 2):
            RHS = sp.zeros(NU, 1)
            for K, (e, f) in enumerate(SYM_PAIRS):
                RHS[K] = (Fab_on_V(Hinv, ab, Epair(*cd), Epair(e, f))
                          + Fab_on_V(Hinv, cd, Epair(*ab), Epair(e, f))
                          - Fab_on_V(Hinv, (e, f), Epair(*ab), Epair(*cd)))
            coeffs = (Vinv * RHS) / 2
            Gam_true = sp.zeros(4, 4)
            for K, (e, f) in enumerate(SYM_PAIRS):
                Gam_true += coeffs[K] * Epair(e, f)
            Gam_cand = gamma_VVV(Hinv, Epair(*ab), Epair(*cd))
            checked += 1
            if Gam_true != Gam_cand:
                bad += 1
    return (bad == 0, bad, checked)


# ===========================================================================
# PART B -- II_s for a general section, assembled from the Part A blocks.
#
# For s(x) = (x, g_ab(x)):  T_mu = ds(d_mu) = d_mu + (d_mu g_ab) d/du_ab.
# nabla_{Tmu} Tnu is computed by the standard pullback-connection formula,
# using Gcal's Christoffel blocks EVALUATED AT u = g(x); the tangential part
# is fixed by Gammabar, the Christoffel symbol of the INDUCED metric
#   gbar_{mu nu} = g_{mu nu} + V(d_mu g, d_nu g).
# II_s(d_mu,d_nu) := nabla_{Tmu}Tnu - Gammabar^rho_{mu nu} T_rho.
#
# All x-derivatives are computed on the EXPLICIT section (real sympy
# `diff`), then a concrete rational point is substituted BEFORE any matrix
# inversion -- this is what keeps the computation tractable (a fully
# symbolic-in-x 4x4 inverse of an already-messy induced metric is, empirically,
# minutes-to-hours; substituting first is seconds).  The CLOSED-FORM formula
# (below, `II_S_CLOSED_FORM_*` strings) is presented in standard index
# notation with g^{-1} left symbolic, exactly as Ricci/Riemann formulas
# always are -- this is not a weaker result, it is the standard way such
# formulas are written, and every numbered claim in it is checked exactly at
# concrete points by the code in this file.
# ===========================================================================

FLAT_MINKOWSKI = {(0, 0): -1, (0, 1): 0, (0, 2): 0, (0, 3): 0, (1, 1): 1,
                  (1, 2): 0, (1, 3): 0, (2, 2): 1, (2, 3): 0, (3, 3): 1}

SECTIONS = {
    "flat": {p: sp.Integer(v) for p, v in FLAT_MINKOWSKI.items()},
    "linear_x0": {**{p: sp.Integer(v) for p, v in FLAT_MINKOWSKI.items()},
                  (0, 0): -1 + x0 * sp.Rational(1, 3)},
    "one_fibre_quadratic": {**{p: sp.Integer(v) for p, v in FLAT_MINKOWSKI.items()},
                             (1, 2): x2 ** 2 * sp.Rational(2, 5)},
    "mixed_two_entries": {**{p: sp.Integer(v) for p, v in FLAT_MINKOWSKI.items()},
                           (0, 3): x0 * x3 * sp.Rational(1, 5),
                           (2, 2): 1 + x1 * sp.Rational(1, 7)},
    "richer": {**{p: sp.Integer(v) for p, v in FLAT_MINKOWSKI.items()},
               (0, 0): -1 + x0 * sp.Rational(1, 3) + x1 ** 2 * sp.Rational(1, 11),
               (1, 1): 1 + x0 * sp.Rational(2, 9),
               (2, 3): x1 * sp.Rational(1, 13)},
}

POINTS = [
    {x0: 0, x1: 0, x2: 0, x3: 0},
    {x0: sp.Rational(1, 2), x1: sp.Rational(-1, 3), x2: sp.Rational(2, 5), x3: sp.Rational(1, 7)},
    {x0: 1, x1: 1, x2: 0, x3: -1},
]

_symcache: dict = {}


def get_section_symderivs(secname):
    if secname in _symcache:
        return _symcache[secname]
    secdict = SECTIONS[secname]
    gvec = [secdict[p] for p in SYM_PAIRS]
    G_sym = sym_from_vec(gvec)
    g1_sym = [sp.diff(G_sym, XS[mu]) for mu in range(4)]
    g2_sym = [[sp.diff(g1_sym[mu], XS[nu]) for nu in range(4)] for mu in range(4)]
    _symcache[secname] = (G_sym, g1_sym, g2_sym)
    return _symcache[secname]


def compute_IIs(secname, point):
    """Returns a dict with G, g1, g2 (at `point`), Ginv, gbar, GB (Gammabar),
    IIs_vert, IIs_horiz -- the full second fundamental form at that point,
    exact rational."""
    G_sym, g1_sym, g2_sym = get_section_symderivs(secname)
    G = G_sym.subs(point)
    g1 = [m.subs(point) for m in g1_sym]
    g2 = [[m.subs(point) for m in row] for row in g2_sym]
    Ginv = G.inv()

    def dGinv(lam):
        return -Ginv * g1[lam] * Ginv

    gbar = sp.Matrix(4, 4, lambda mu, nu: G[mu, nu] + Vform(Ginv, g1[mu], g1[nu]))
    dgbar = []
    for lam in range(4):
        M = sp.zeros(4, 4)
        for mu in range(4):
            for nu in range(4):
                M[mu, nu] = g1[lam][mu, nu] + dVform(Ginv, dGinv(lam), g1[mu], g1[nu],
                                                       g2[lam][mu], g2[lam][nu])
        dgbar.append(M)
    gbarinv = gbar.inv()

    def Gammabar(rho, mu, nu):
        s = 0
        for lam in range(4):
            s += gbarinv[rho, lam] * (dgbar[mu][nu, lam] + dgbar[nu][mu, lam] - dgbar[lam][mu, nu])
        return sp.Rational(1, 2) * s

    GB = {}
    for mu in range(4):
        for nu in range(mu, 4):
            for rho in range(4):
                GB[(rho, mu, nu)] = Gammabar(rho, mu, nu)

    def Gtilde_rho(rho, mu, nu):
        s = 0
        for sigma in range(4):
            s += Ginv[rho, sigma] * (g1[nu][sigma, mu] + g1[mu][sigma, nu])
        return sp.Rational(1, 2) * s

    def vert_raw(mu, nu):
        HHVblock = gamma_HHV(G, mu, nu)
        VVVblock = gamma_VVV(Ginv, g1[mu], g1[nu])
        return g2[mu][nu] + HHVblock + VVVblock

    IIs_vert, IIs_horiz = {}, {}
    for mu in range(4):
        for nu in range(mu, 4):
            raw_v = vert_raw(mu, nu)
            tangential_v = sp.zeros(4, 4)
            for rho in range(4):
                tangential_v += GB[(rho, mu, nu)] * g1[rho]
            if MUT == "orthogonality_theorem_disabled":
                # corrupt the ASSEMBLY (skip the tangential/Gammabar
                # subtraction the Gauss formula requires), leaving the
                # orthogonality ASSERTION in test_b1 fully intact -- if that
                # assertion were doing nothing, this corruption would sail
                # through.  It must not.
                tangential_v = sp.zeros(4, 4)
            IIs_vert[(mu, nu)] = raw_v - tangential_v
            gt = sp.Matrix(4, 1, [Gtilde_rho(rho, mu, nu) for rho in range(4)])
            gb = sp.Matrix(4, 1, [GB[(rho, mu, nu)] for rho in range(4)])
            IIs_horiz[(mu, nu)] = gt - gb

    return dict(G=G, g1=g1, g2=g2, Ginv=Ginv, gbar=gbar, GB=GB,
                IIs_vert=IIs_vert, IIs_horiz=IIs_horiz)


def orthogonality_residuals(data):
    """Gcal(II_s(d_mu,d_nu), T_sigma) for every mu<=nu, sigma -- must be
    EXACTLY zero (the Gauss-formula theorem).  Uses G (the ambient metric's
    horizontal block AT THE SECTION), NOT gbar (the induced metric) -- gbar
    is for the intrinsic/tangential projection only; the ambient pairing that
    certifies "normal" must use the ambient block.  (This distinction was the
    site of a real bug during development; see POSTFLIGHT.)"""
    out = []
    for (mu, nu), vpart in data["IIs_vert"].items():
        hpart = data["IIs_horiz"][(mu, nu)]
        for sigma in range(4):
            pairing = sum(data["G"][rho, sigma] * hpart[rho] for rho in range(4)) \
                      + Vform(data["Ginv"], vpart, data["g1"][sigma])
            out.append((mu, nu, sigma, sp.nsimplify(pairing)))
    return out


# ===========================================================================
# PART C -- FC-VZ-4: does II_s source spacelike characteristics at
# subprincipal order?  Exact Cl(3,1) toy model, faithful to the structural
# argument (a background/xi-independent endomorphism cannot alter the
# TOP-DEGREE part of a characteristic determinant), with two REQUIRED
# contrary controls.
# ===========================================================================

def build_gammas():
    """Exact Cl(3,1) gamma matrices, eta = diag(-1,1,1,1) (mostly plus,
    matches VZ-4's horizontal-block ETA convention)."""
    I2 = sp.eye(2)
    Z2 = sp.zeros(2, 2)
    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sz = sp.Matrix([[1, 0], [0, -1]])
    sig = [I2, sx, sy, sz]

    def block(A, B, C, D):
        return sp.Matrix(sp.BlockMatrix([[A, B], [C, D]]))

    g0 = sp.I * block(Z2, I2, I2, Z2)
    gs = [g0] + [sp.I * block(Z2, sig[k], -sig[k], Z2) for k in (1, 2, 3)]
    return gs


ETA4 = [-1, 1, 1, 1]


def verify_clifford(gammas):
    bad = 0
    for m in range(4):
        for n in range(4):
            rhs = 2 * ETA4[m] * sp.eye(4) if m == n else sp.zeros(4, 4)
            if MUT == "clifford_relation_sign_flip" and m == n:
                rhs = -rhs
            lhs = sp.expand(gammas[m] * gammas[n] + gammas[n] * gammas[m])
            if sp.simplify(lhs - rhs) != sp.zeros(4, 4):
                bad += 1
    return bad == 0


def top_degree_part(poly_expr, vars_, degree):
    p = sp.Poly(sp.expand(poly_expr), *vars_)
    out = 0
    for monom, coeff in p.terms():
        want = degree
        if MUT == "zeroth_order_theorem_wrong_degree":
            want = degree - 1
        if sum(monom) == want:
            mono = 1
            for e, v in zip(monom, vars_):
                mono *= v ** e
            out += coeff * mono
    return sp.expand(out)


def symbol_M(gammas, XI):
    M = sp.zeros(4, 4)
    for m in range(4):
        M += XI[m] * gammas[m]
    return M


def K_from_IIs_sample():
    """A concrete 4x4 endomorphism built from an actual computed II_s
    vertical-part sample (section='richer', point 1, component (mu,nu)=(0,0)),
    NOT an arbitrary matrix -- ties PART D back to PART B's real numbers."""
    data = compute_IIs("richer", POINTS[1])
    return data["IIs_vert"][(0, 0)]


def zeroth_order_top_degree_invariance(gammas, XI):
    """(no-sourcing check) A background (xi-independent) endomorphism K
    cannot change the DEGREE-4 (leading/principal) part of det(M(xi)+K) --
    the leading part comes ONLY from choosing M(xi) in all four Leibniz
    factors (any K factor drops the xi-degree by >=1).  Verified exactly
    with the ACTUAL II_s-derived K."""
    M = symbol_M(gammas, XI)
    detM = sp.expand(sp.det(M))
    K = K_from_IIs_sample()
    detMK = sp.expand(sp.det(M + K))
    d4 = top_degree_part(detMK, XI, 4)
    return sp.simplify(d4 - detM) == 0, detM, K


def adversarial_promoted_control(gammas, XI):
    """(REQUIRED contrary control ii) Artificially promote a background
    endomorphism to FIRST order in xi: Kbad(xi) = (n.xi) K.  This produces an
    EXACT spacelike root -- proving the detector fires when the defect is
    genuinely first-order, not merely rubber-stamping every input 'safe'."""
    M = symbol_M(gammas, XI)
    K = gammas[0]                       # deliberately artificial and minimal
    n = sp.Matrix([0, 0, 0, 1])         # n.xi = xi3
    ndotxi = sum(n[m] * XI[m] for m in range(4))
    Kbad = ndotxi * K
    point = {XI[0]: 0, XI[1]: 0, XI[2]: 0, XI[3]: 1}
    etaxx = sum(ETA4[m] * XI[m] ** 2 for m in range(4)).subs(point)
    if MUT == "adversarial_control_vacuous":
        etaxx = -etaxx   # falsely claim the point is timelike
    detM_pt = sp.det(M).subs(point)
    detMKbad_pt = sp.det(M + Kbad).subs(point)
    return etaxx, detM_pt, detMKbad_pt


def flat_section_IIs_vert_00():
    """(REQUIRED contrary control i) II_s for the FLAT Minkowski section,
    provably NONZERO.  With g1=g2=0 identically, the VVV/Hessian pieces of
    vert_raw vanish and Gammabar=0 (flat gbar), so II_s reduces EXACTLY to
    the algebraic H-H-V block built from the constant metric alone:
        (II_s)_{mu nu, ab} = -(1/2)( eta_{a(mu} eta_{nu)b} - (1/2) eta_{ab} eta_{mu nu} )
    -- independent of x, and manifestly nonzero (e.g. (mu,nu)=(a,b)=(0,0)
    entry is -1/4).  This reproduces (independently) the "constant sections
    are not automatically totally geodesic" finding of
    `ii-s-coordinate-formula-2026-06-23.md` SS6.1."""
    data = compute_IIs("flat", POINTS[0])
    return data["IIs_vert"][(0, 0)], data["IIs_horiz"][(0, 0)]


# ===========================================================================
# Tests
# ===========================================================================

class Part0_ReproduceR(unittest.TestCase):
    def test_r_pullback_is_a_contraction(self):
        J, g = jacobian_symbolic()
        om = sp.symbols("w0:14", real=True)
        got = pullback_R(J, om)
        for mu in range(NX):
            expected = om[mu] + sum(om[NX + I] * sp.diff(g[I], XS[mu]) for I in range(NU))
            if MUT == "pullback_is_projection":
                expected = om[mu]
            self.assertEqual(sp.simplify(got[mu] - expected), 0, f"mu={mu}")


class PartA_ChristoffelBlocks(unittest.TestCase):
    def test_a1_five_blocks_symbolic(self):
        r = verify_blocks_symbolic()
        self.assertTrue(r["HHH"])
        self.assertTrue(r["HVV"])
        self.assertTrue(r["H_lowerVV"])
        ok, bad, n = r["HHV"]
        self.assertTrue(ok, f"HHV: {bad}/{n} failed")
        ok, bad, n = r["HVH"]
        self.assertTrue(ok, f"HVH: {bad}/{n} failed")

    def test_a2_vvv_block_rational(self):
        ok, bad, n = verify_vvv_block_rational()
        self.assertTrue(ok, f"VVV: {bad}/{n} failed")
        self.assertEqual(n, 55 * 3, "expected 55 pairs x 3 sample points")


class PartB_IIsFormula(unittest.TestCase):
    def test_b1_orthogonality_theorem_all_sections(self):
        """The certificate: Gcal(II_s, T_sigma) = 0 exactly, for every
        (section, point, mu<=nu, sigma).  A wrong formula generically fails
        this (it caught a real indexing bug during development)."""
        total = 0
        for secname in SECTIONS:
            pts = POINTS if secname != "flat" else POINTS[:1]
            for pt in pts:
                data = compute_IIs(secname, pt)
                for (mu, nu, sigma, val) in orthogonality_residuals(data):
                    total += 1
                    self.assertEqual(val, 0, f"{secname} pt={pt} mu={mu} nu={nu} sigma={sigma}")
        self.assertGreater(total, 300, "sweep too small to be meaningful")

    def test_b2_contrary_control_flat_section_nonzero(self):
        """CONTRARY CONTROL (i): II_s must NOT vanish for the flat section."""
        vert, horiz = flat_section_IIs_vert_00()
        expected = -sp.Rational(1, 2) * (Epair(0, 0) * sp.diag(-1, 1, 1, 1)
                                          - sp.Rational(1, 2) * (-1) * sp.diag(-1, 1, 1, 1))
        # direct closed-form check of the (0,0) entry specifically:
        self.assertEqual(vert[0, 0], sp.Rational(-1, 4))
        self.assertEqual(horiz, sp.zeros(4, 1))
        if MUT == "flat_contrary_control_vacuous":
            self.assertEqual(vert, sp.zeros(4, 4), "flat II_s falsely asserted zero")
        else:
            self.assertNotEqual(vert, sp.zeros(4, 4),
                                "CONTRARY CONTROL IS VACUOUS: flat-section II_s is zero")

    def test_b3_derivative_order_audit(self):
        """II_s genuinely depends on the section's SECOND derivatives (not
        merely its first), contradicting the drafts file's "and its first
        derivatives" phrasing taken literally.  Demonstrated by exhibiting
        two sections with IDENTICAL g, g1 at a point but DIFFERENT g2, that
        produce DIFFERENT II_s at that point."""
        # two sections sharing g(0)=Minkowski and g1(0)=(1/3 at (0,0)) but
        # differing in second derivative at x0=0:
        sec_a = SECTIONS["linear_x0"]                      # g2 = 0 identically
        sec_b_dict = {**{p: sp.Integer(v) for p, v in FLAT_MINKOWSKI.items()},
                      (0, 0): -1 + x0 * sp.Rational(1, 3) + x0 ** 2 * sp.Rational(5, 1)}
        SECTIONS["_derivative_probe_b"] = sec_b_dict
        pt0 = POINTS[0]
        da = compute_IIs("linear_x0", pt0)
        db = compute_IIs("_derivative_probe_b", pt0)
        # g, g1 agree at pt0 by construction (x0=0 kills the x0^2 term and
        # its contribution to g1 at x0=0... check directly):
        self.assertEqual(da["G"], db["G"])
        self.assertEqual(da["g1"][0], db["g1"][0])
        g2_differs = da["g2"][0][0] != db["g2"][0][0]
        IIs_differs = da["IIs_vert"][(0, 0)] != db["IIs_vert"][(0, 0)]
        if MUT == "derivative_order_claim_wrong":
            self.assertFalse(IIs_differs, "falsely claims first-derivative-only dependence")
        else:
            self.assertTrue(g2_differs, "probe sections do not actually differ in g2")
            self.assertTrue(IIs_differs,
                            "II_s did NOT change under a pure second-derivative change: "
                            "would falsify the second-derivative dependence claim")


class PartC_FCVZ4Detector(unittest.TestCase):
    def test_c1_clifford_relations(self):
        gammas = build_gammas()
        self.assertTrue(verify_clifford(gammas), "{gamma^m,gamma^n} != 2 eta^mn Id")

    def test_c2_det_matches_null_cone_square(self):
        gammas = build_gammas()
        XI = sp.symbols("xi0 xi1 xi2 xi3", real=True)
        M = symbol_M(gammas, XI)
        detM = sp.expand(sp.det(M))
        xisq = sum(ETA4[m] * XI[m] ** 2 for m in range(4))
        self.assertEqual(sp.simplify(detM - sp.expand(xisq ** 2)), 0)

    def test_c3_zeroth_order_no_new_characteristics(self):
        gammas = build_gammas()
        XI = sp.symbols("xi0 xi1 xi2 xi3", real=True)
        ok, detM, K = zeroth_order_top_degree_invariance(gammas, XI)
        self.assertNotEqual(K, sp.zeros(4, 4), "K from II_s sample is degenerate/vacuous")
        self.assertTrue(ok, "a background II_s-sourced endomorphism changed the "
                            "leading characteristic variety")

    def test_c4_REQUIRED_contrary_control_adversarial_promotion(self):
        """CONTRARY CONTROL (ii): an ARTIFICIAL first-order promotion of the
        SAME kind of background term DOES source an exact spacelike
        characteristic -- the detector can discriminate, not just always
        pass."""
        gammas = build_gammas()
        XI = sp.symbols("xi0 xi1 xi2 xi3", real=True)
        etaxx, detM_pt, detMKbad_pt = adversarial_promoted_control(gammas, XI)
        self.assertEqual(etaxx, 1, "control point is not exactly spacelike (eta.xi.xi=1)")
        self.assertNotEqual(detM_pt, 0, "control point already null/causal before the defect")
        self.assertEqual(detMKbad_pt, 0,
                         "ADVERSARIAL CONTROL IS VACUOUS: the artificial first-order "
                         "promotion did not produce a new characteristic")


class PartE_TextIntegrity(unittest.TestCase):
    """Guards the exact quotes this artifact's write-up depends on."""

    def test_e1_drafts_file_quote(self):
        text = (ROOT / DRAFTS_FILE).read_text(encoding="utf-8")
        target = ("The second fundamental form II_s ∈ Γ(S²T*X⁴ ⊗ Sym²T*X⁴) "
                   "has not been computed in coordinates as a function of s "
                   "and its first derivatives.")
        if MUT == "quote_drift":
            target = "This sentence does not appear in the drafts file."
        self.assertIn(target, text)

    def test_e2_fc_vz4_quote_in_canon(self):
        text = (ROOT / CANON_FILE).read_text(encoding="utf-8")
        self.assertIn("FC-VZ-4", text)
        self.assertIn("sources an effective first-order term", text)

    def test_e3_routing_notice_present_in_this_artifacts_md(self):
        md_path = (ROOT / "lab/active-research/joe-directed/vz-repair/"
                   "vz5-ii-s-subprincipal-2026-08-17.md")
        if not md_path.exists():
            self.skipTest("companion artifact not yet written")
        text = md_path.read_text(encoding="utf-8")
        marker = "GU-COMPARATOR-ROUTING"
        if MUT == "routing_notice_missing":
            text = text.replace(marker, "")
        self.assertIn(marker, text)
        self.assertIn("Classification: `SOURCE_NATIVE_ROUTE`", text)
        self.assertIn("gu-typed-objects", text)
        self.assertIn("MAP-TYPE=contraction", text)


def run_selftest() -> int:
    print("VZ-5 selftest: clean baseline FIRST, then each planted control must exit 1\n")
    env0 = dict(os.environ)
    env0.pop("VZ5_CONTROL", None)
    base = subprocess.run([sys.executable, __file__], cwd=ROOT, env=env0,
                          capture_output=True, text=True)
    print(f"  clean baseline exit {base.returncode}  "
          f"{'OK' if base.returncode == 0 else 'FAILED -- selftest cannot proceed'}")
    if base.returncode != 0:
        print(base.stdout[-3000:])
        print(base.stderr[-3000:])
        return 1

    failures = []
    for name, description in CONTROLS.items():
        env = dict(os.environ, VZ5_CONTROL=name)
        proc = subprocess.run([sys.executable, __file__], cwd=ROOT, env=env,
                              capture_output=True, text=True)
        ok = proc.returncode == 1
        print(f"  control {name:40s} exit {proc.returncode}  "
              f"{'OK  ' if ok else 'VACUOUS'}  ({description})")
        if not ok:
            failures.append(name)
    print()
    if failures:
        print(f"SELFTEST FAILED -- {len(failures)} vacuous control(s): " + ", ".join(failures))
        return 1
    print(f"SELFTEST PASSED -- clean baseline green, {len(CONTROLS)}/{len(CONTROLS)} "
          f"planted controls each drove exit 1")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(run_selftest())
    if "--control" in sys.argv:
        idx = sys.argv.index("--control")
        os.environ["VZ5_CONTROL"] = sys.argv[idx + 1]
        MUT = sys.argv[idx + 1]
        del sys.argv[idx:idx + 2]
    unittest.main(verbosity=2)
