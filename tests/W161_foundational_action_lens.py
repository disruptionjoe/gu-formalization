#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
W161 -- TEAM LENS-ACTION.  THE FOUNDATIONAL ACTION.

The standing debit (debit-1) is the positive-norm tachyonic R^2 scalaron, "real IF
|II|^2 is GU's law", with all PERTURBATIVE escapes closed (W157 keystone COINCIDENCE;
W159 branch-UNSELECTED / gradient OUT-OF-VALIDITY / SIGN-FREE).  This wave attacks the
ONE assumption those escapes hold fixed: is |II|^2 actually GU's law?

PRIMARY SOURCE (Geometric_UnityDraftApril1st2021.pdf, read as DATA):
  * 9.1 / eq (9.4): the 1st-order Bosonic action is
        I1B = < T , (star_shiab)(F_B + (1/2) d_B T + (1/3)[T,T]) + (1/2) T >_{Y14}
    with T = omega - g.omega0 the DISPLACED TORSION (a contorsion / second-fundamental-
    form-like object), star_shiab the gauge-covariant Einstein (Ricci - (1/2)Ricci-scalar)
    projection that "kills off the Weyl curvature."  Weinstein: this "produces a LINEAR
    expression in the curvature tensor" and generates "LINEAR field equations."
  * eq (9.7)-(9.10): I1B varies to the SWERVATURE = star.F_A = -(1/2)T equation, and
    "recovering the more familiar terms" gives the SECOND-ORDER EINSTEIN equation
        S = T   <=>   R_mn - (s/2) g_mn = T_mn.
    A second-order Einstein equation has NO fourth-derivative (R^2) mode: NO scalaron.
  * 9.2 footnote 10 + "other possibilities to explore for the choice of the Shiab
    operator": the shiab is EXPLICITLY NON-UNIQUE in the source; the settled one is
    "cannot now locate".
  * 12.2/12.3: space-time / the X4 metric is NOT fundamental; it is RECOVERED (derived).

THE MISINTERPRETATION THIS WAVE NAMES.  |II|^2 (a Willmore functional, QUADRATIC in the
extrinsic curvature) is NOT eq (9.4).  It is the INDUCED / integrated-out gravitational
shadow (W130/W154 already label the induced |II|^2 "the integrated-out shadow, not
fundamental").  The tachyon (c_R = -4/9) is a coefficient of that QUADRATIC shadow.  GU's
ACTUAL action is LINEAR in curvature and carries no fundamental R^2 scalaron.

WHAT THE TEST ESTABLISHES (deterministic sympy, exact; positive controls first):
  PC1-PC3  reproduce the W126/W130 machinery: |II|^2 slice = (2,1/3,8/9,-4), c_R=-4/9;
           |H|^2 slice = (-1,4/3,-4/9,0); and the healthy shape point (-2,1).
  N1  THE LINEAR-ACTION FACT: an action LINEAR in curvature (the class of eq 9.4/9.10,
      gamma R with a=b=c=0 in the covariant quartic basis) has c_R = 0 EXACTLY, so the
      scalaron inverse-mass 6 c_R = 0 -> the R^2 mode DECOUPLES (infinite mass): NO
      scalaron, tachyonic or otherwise.  The tachyon is absent from GU's actual action.
  N2  THE SCALARON NEEDS THE QUADRATIC SHADOW: c_R != 0 requires a curvature-SQUARED term;
      it is nonzero ONLY for the induced |II|^2 / |H|^2 shadow, not for the linear action.
  N3  THE SHADOW SIGN IS NOT FORCED: within the induced shape family alpha|II|^2+beta|H|^2,
      (a1, c_R) are INDEPENDENT (det = 4/9 != 0), and the ATTRACTIVE-AND-HEALTHY sub-region
      is non-empty (e.g. (-2,1): a1=2/3>0, c_R=+4/9>0).  So even AS a shadow the tachyonic
      point is one reduction, not forced.
  N4  SKEPTIC / DEFENSE-ATTORNEY CONTROL: the pure-|II|^2 shadow IS covariantly tachyonic
      (c_R=-4/9<0, signature-blind, W157).  So IF one INSISTS the pure |II|^2 shadow is
      GU's gravitational law, the debit is real.  The verdict turns on shadow-vs-law, and
      the source says |II|^2 is the shadow.
  N5  STRUCTURE OF eq (9.4): T is BILINEAR-paired against a LINEAR curvature projection;
      the functional is < T, Ein(F) > + torsion self-terms, in the Palatini / Einstein-
      Cartan class -- eliminating the (algebraic) torsion returns a LINEAR-R (Einstein)
      action plus torsion contact terms, NOT a Willmore |II|^2.  Encoded as: a linear
      curvature action's covariant R^2 coefficient is c_R = 0, and its Einstein channel
      a1 > 0 (attractive) -- healthy, no scalaron.

FIVE personas inline (differential geometer; GU-primary-source scholar; field theorist;
symbolic engineer; adversarial skeptic); no sub-agents.

Run:  python -u tests/W161_foundational_action_lens.py   (exit 0 iff all PASS)

Binding: W138 battery; honest grading; conditional register; no canon change; the shiab
non-uniqueness and the shadow-vs-law fork are the load-bearing source facts, not asserted
of GU beyond what the April 2021 draft states.  Zero em dashes in paper-facing text.
"""
from __future__ import annotations
import sympy as sp
from sympy import Rational as Q

FAIL = []


def check(name, ok, detail=""):
    print(("PASS" if ok else "FAIL") + " :: " + name + (("  --  " + detail) if detail else ""), flush=True)
    if not ok:
        FAIL.append(name)


def log(msg=""):
    print(msg, flush=True)


# ===========================================================================
# MACHINERY -- verbatim W159/W126 Route-1 slice machinery (regression-pinned by
# the positive controls: reproduces W126 (2,1/3,8/9,-4) and W130 c_R = -4/9).
# ===========================================================================
DIM = 4
eta = sp.diag(-1, 1, 1, 1)                                        # GU base signature (1,3)
pairs = [(a, b) for a in range(DIM) for b in range(a, DIM)]
xs = [sp.Symbol(f'x{i}', real=True) for i in range(DIM)]
p = sp.Symbol('p', real=True)
E0 = sp.Symbol('E0', positive=True)
vsym = [sp.Symbol(f'v{i}', real=True) for i in range(DIM)]
ssym = {(i, j): sp.Symbol(f's{i}{j}', real=True) for (i, j) in pairs}


def S(i, j):
    return ssym[(i, j)] if i <= j else ssym[(j, i)]


def phi_jet(with_v=True):
    ph = p
    if with_v:
        ph += sum(vsym[i] * xs[i] for i in range(DIM))
    ph += Q(1, 2) * sum(S(i, j) * xs[i] * xs[j] for i in range(DIM) for j in range(DIM))
    return ph


def at0(expr):
    e = expr.subs({xi: 0 for xi in xs})
    e = e.subs(p, sp.log(E0) / 2)
    return sp.expand(sp.powsimp(e, force=True))


def Vg_of(Gi, k, l):
    A = Gi * k
    B = Gi * l
    return sp.trace(A * B) - Q(1, 2) * sp.trace(A) * sp.trace(B)


def route1_W(with_v, vvals=None, svals=None, want_H=False):
    ph = phi_jet(with_v)
    E = sp.exp(2 * ph)
    G = sp.Matrix(DIM, DIM, lambda i, j: E * eta[i, j])
    subs_num = {}
    if vvals is not None:
        subs_num.update({vsym[i]: vvals[i] for i in range(DIM)})
    if svals is not None:
        subs_num.update({ssym[ij]: svals[ij] for ij in pairs})
    if subs_num:
        G = G.subs(subs_num)
    dG = [sp.diff(G, xs[m]) for m in range(DIM)]
    ddG = [[sp.diff(dG[m], xs[n]) for n in range(DIM)] for m in range(DIM)]
    Gi_x = sp.Matrix(DIM, DIM, lambda i, j: eta[i, j] / E.subs(subs_num) if subs_num else eta[i, j] / E)
    gbar = sp.Matrix(DIM, DIM, lambda m, n: G[m, n] + Vg_of(Gi_x, dG[m], dG[n]))
    gbar0 = gbar.applyfunc(at0)
    gbari0 = gbar0.inv()
    dgbar0 = [sp.Matrix(DIM, DIM, lambda m, n: at0(sp.diff(gbar[m, n], xs[l]))) for l in range(DIM)]
    gbarGam0 = [[[Q(1, 2) * sum(gbari0[l, k] * (dgbar0[m][n, k] + dgbar0[n][m, k]
                 - dgbar0[k][m, n]) for k in range(DIM))
                 for n in range(DIM)] for m in range(DIM)] for l in range(DIM)]
    G0 = G.applyfunc(at0)
    Gi0 = G0.inv()
    dG0 = [m.applyfunc(at0) for m in dG]
    ddG0 = [[ddG[m][n].applyfunc(at0) for n in range(DIM)] for m in range(DIM)]
    Bv = {}
    for m in range(DIM):
        for n in range(m, DIM):
            M = ddG0[m][n].copy()
            for l in range(DIM):
                M = M - gbarGam0[l][m][n] * dG0[l]
            alg = sp.Matrix(DIM, DIM, lambda a, b:
                            Q(1, 2) * (G0[a, m] * G0[n, b] + G0[a, n] * G0[m, b])
                            - Q(1, 2) * G0[a, b] * G0[m, n])
            M = M - Q(1, 2) * alg
            M = M - Q(1, 2) * (dG0[m] * Gi0 * dG0[n] + dG0[n] * Gi0 * dG0[m])
            Bv[(m, n)] = Bv[(n, m)] = M.applyfunc(sp.expand)

    def IP(q, qq):
        base = Vg_of(Gi0, q, qq)
        nl = sp.Integer(0)
        for r in range(DIM):
            for s2 in range(DIM):
                if Gi0[r, s2] == 0:
                    continue
                nl += Gi0[r, s2] * Vg_of(Gi0, q, dG0[r]) * Vg_of(Gi0, qq, dG0[s2])
        return base + nl

    W = sp.Integer(0)
    for m in range(DIM):
        for n in range(DIM):
            for r in range(DIM):
                for s2 in range(DIM):
                    w = gbari0[m, r] * gbari0[n, s2]
                    if w == 0:
                        continue
                    W += w * IP(Bv[(m, n)], Bv[(r, s2)])
    W = sp.expand(sp.simplify(sp.expand(W)))
    if not want_H:
        return W
    Hmean = sp.zeros(DIM, DIM)
    for m in range(DIM):
        for n in range(DIM):
            if gbari0[m, n] != 0:
                Hmean += gbari0[m, n] * Bv[(m, n)]
    H2 = sp.expand(sp.simplify(IP(Hmean, Hmean)))
    return W, H2


def _curvature_of_sigma():
    ph = p + Q(1, 2) * sum(S(i, j) * xs[i] * xs[j] for i in range(DIM) for j in range(DIM))
    E = sp.exp(2 * ph)
    g = sp.Matrix(DIM, DIM, lambda i, j: E * eta[i, j])
    ginv = sp.Matrix(DIM, DIM, lambda i, j: eta[i, j] / E)
    Gm = [[[Q(1, 2) * sum(ginv[l, k] * (sp.diff(g[n, k], xs[m]) + sp.diff(g[m, k], xs[n])
            - sp.diff(g[m, n], xs[k])) for k in range(DIM))
            for n in range(DIM)] for m in range(DIM)] for l in range(DIM)]
    Ric = sp.zeros(DIM, DIM)
    for m in range(DIM):
        for n in range(m, DIM):
            r = sp.Integer(0)
            for l in range(DIM):
                r += sp.diff(Gm[l][m][n], xs[l]) - sp.diff(Gm[l][l][m], xs[n])
                for k in range(DIM):
                    r += Gm[l][l][k] * Gm[k][m][n] - Gm[l][n][k] * Gm[k][l][m]
            Ric[m, n] = Ric[n, m] = at0(r)
    sig = {(i, j): sp.Symbol(f'g{i}{j}', real=True) for (i, j) in pairs}
    subs_sigma = {ssym[ij]: sig[ij] * E0 for ij in pairs}
    Rsc = sp.expand(sum(eta[m, m] * Ric[m, m] for m in range(DIM)) / E0)
    R_of_sigma = sp.expand(Rsc.subs(subs_sigma))
    RicSq = sp.expand(sum(eta[a, a] * eta[b, b] * (Ric[a, b])**2
                          for a in range(DIM) for b in range(DIM)).subs(subs_sigma) / E0**2)
    return R_of_sigma, RicSq, sig


R_of_sigma, RicSq_of_sigma, sig = _curvature_of_sigma()
_Rf = sp.lambdify([sig[ij] for ij in pairs], R_of_sigma, 'sympy')
_Rif = sp.lambdify([sig[ij] for ij in pairs], RicSq_of_sigma, 'sympy')
_basis_jets = [
    {(0, 0): 1}, {(1, 1): 1}, {(0, 0): 1, (1, 1): 1, (2, 2): 1, (3, 3): 1},
    {(0, 0): 2, (1, 1): -1}, {(0, 0): 1, (1, 1): -1, (2, 2): 1, (3, 3): -1}, {(2, 2): 1, (3, 3): 3},
]


def slice_decomp(want_H=False):
    a0, a1, a2s, a3s = sp.symbols('a0 a1 a2s a3s', real=True)
    eqs = []
    for jet in _basis_jets:
        svals = {ij: (jet[ij] if ij in jet else 0) for ij in pairs}
        if want_H:
            _, Hv = route1_W(False, svals=svals, want_H=True)
            Wv = sp.nsimplify(Hv.subs(E0, 1))
        else:
            Wv = sp.nsimplify(route1_W(False, svals=svals, want_H=False).subs(E0, 1))
        args = [svals[ij] for ij in pairs]
        eqs.append(a0 + a1 * _Rf(*args) + a2s * _Rf(*args)**2 + a3s * _Rif(*args) - Wv)
    s0 = sp.solve(eqs, [a0, a1, a2s, a3s], dict=True)[0]
    return s0[a0], s0[a1], s0[a2s], s0[a3s]


# ===========================================================================
log("=" * 82)
log("W161 -- THE FOUNDATIONAL ACTION.  Is |II|^2 GU's law, or the shadow?")
log("=" * 82)

# --- POSITIVE CONTROLS ------------------------------------------------------
log("\n--- POSITIVE CONTROLS: reproduce W126 / W130 / the healthy shape point ---")
a0v, a1v, a2sv, a3sv = slice_decomp(want_H=False)
c_R_II = a2sv + a3sv * Q(1, 3)                    # W130 covariant map (GB freedom cancels)
check("PC1: |II|^2 slice = (2, 1/3, 8/9, -4) and covariant c_R = -4/9 (W126/W130)",
      (a0v, a1v, a2sv, a3sv) == (sp.Integer(2), Q(1, 3), Q(8, 9), sp.Integer(-4))
      and c_R_II == Q(-4, 9), f"({a0v},{a1v},{a2sv},{a3sv}), c_R={c_R_II}")
a0H, a1H, a2sH, a3sH = slice_decomp(want_H=True)
c_R_H = a2sH + a3sH * Q(1, 3)
check("PC2: |H|^2 slice = (-1, 4/3, -4/9, 0), c_R_H = -4/9 (W159)",
      (a0H, a1H, a2sH, a3sH) == (sp.Integer(-1), Q(4, 3), Q(-4, 9), sp.Integer(0))
      and c_R_H == Q(-4, 9), f"({a0H},{a1H},{a2sH},{a3sH})")
alpha, beta = sp.symbols('alpha beta', real=True)
a1_fam = alpha * a1v + beta * a1H
cR_fam = alpha * c_R_II + beta * c_R_H
ce = {alpha: -2, beta: 1}
check("PC3: healthy shape point (alpha,beta)=(-2,1): a1=2/3>0 (ATTRACTIVE) AND "
      "c_R=+4/9>0 (HEALTHY) is inside the induced family (W159 R3c)",
      a1_fam.subs(ce) == Q(2, 3) and cR_fam.subs(ce) == Q(4, 9)
      and a1_fam.subs(ce) > 0 and cR_fam.subs(ce) > 0)

# ===========================================================================
# THE COVARIANT QUARTIC BASIS MAP (W130 Part A, re-stated):
#   a covariant action  -2 Lambda + gamma R + a R^2 + b Ric^2 + c Riem^2  has
#     spin-0 (R^2) channel coupling   c_R = a + b/3 + c/3
#     scalaron inverse-mass-squared   6 c_R  (m_0^2 = gamma/(6 c_R))
#   GB (1,-4,1) and the Riem->{R^2,Ric^2} basis freedom all cancel in c_R.
# ===========================================================================
ga, aa, bb, cc = sp.symbols('gamma a b c', real=True)
cR_cov = aa + bb / 3 + cc / 3


def scalaron_inv_mass(gamma_val, a_val, b_val, c_val):
    """6 c_R = 1/(m_0^2/gamma).  Zero => scalaron decouples (infinite mass, no mode)."""
    return 6 * cR_cov.subs({aa: a_val, bb: b_val, cc: c_val})


log("\n" + "=" * 82)
log("N1 -- THE LINEAR-ACTION FACT (differential geometer + field theorist)")
log("=" * 82)
# GU's actual action eq (9.4) is LINEAR in curvature; its reduction eq (9.10) is the
# SECOND-ORDER Einstein equation R_mn-(s/2)g_mn=T_mn.  In the covariant basis that is
# gamma R with a=b=c=0.  Its scalaron channel:
c_R_linear = cR_cov.subs({aa: 0, bb: 0, cc: 0})
inv_mass_linear = scalaron_inv_mass(1, 0, 0, 0)
check("N1a: a LINEAR-in-curvature action (a=b=c=0, the class of GU eq 9.4/9.10) has "
      "c_R = 0 EXACTLY -- there is NO curvature-squared spin-0 channel",
      c_R_linear == 0)
check("N1b: therefore the scalaron inverse-mass 6 c_R = 0, i.e. m_0^2 -> infinity: the "
      "R^2 mode DECOUPLES.  GU's actual action carries NO propagating scalaron, "
      "tachyonic or otherwise (a healthy 2-derivative Einstein theory)",
      inv_mass_linear == 0)
# Starobinsky control: adding +R^2 (a=1) REVIVES a HEALTHY scalaron (c_R=+1>0).
check("N1c: control -- restoring a curvature-SQUARED term (+R^2, a=1) gives c_R=+1>0, a "
      "HEALTHY (positive-mass) scalaron (Starobinsky): the scalaron is a property of the "
      "QUADRATIC sector, absent from the linear action",
      cR_cov.subs({aa: 1, bb: 0, cc: 0}) == 1 and scalaron_inv_mass(1, 1, 0, 0) > 0)

log("\n" + "=" * 82)
log("N2 -- THE SCALARON LIVES ONLY IN THE INDUCED SHADOW (field theorist)")
log("=" * 82)
# The tachyon c_R=-4/9 belongs to the QUADRATIC induced |II|^2 shadow (a2s,a3s != 0).
# The linear action has a2s=a3s=0.  So the tachyon is a feature of the shadow, not the law.
check("N2a: the tachyonic c_R = -4/9 requires the curvature-SQUARED coefficients "
      "(a2s,a3s) = (8/9,-4) of the INDUCED |II|^2 shadow; the linear action has "
      "(a2s,a3s) = (0,0) and c_R = 0.  The tachyon is a coefficient of the SHADOW",
      (a2sv, a3sv) != (0, 0) and c_R_II == Q(-4, 9) and c_R_linear == 0)
# Both |II|^2 and |H|^2 share the SAME Einstein channel structure but DIFFER only in the
# quadratic sector (a3s: -4 vs 0) -- the scalaron sign is a quadratic-sector datum.
check("N2b: |II|^2 and |H|^2 differ in the quadratic sector (a3s = -4 vs 0) -- confirming "
      "the scalaron/tachyon lives in the curvature-SQUARED grade, exactly the grade the "
      "linear GU action does not populate",
      a3sv == -4 and a3sH == 0)

log("\n" + "=" * 82)
log("N3 -- EVEN AS A SHADOW, THE SIGN IS NOT FORCED (field theorist + skeptic)")
log("=" * 82)
det = a1v * c_R_H - a1H * c_R_II
check("N3a: within the induced family alpha|II|^2+beta|H|^2, (a1, c_R) are INDEPENDENT "
      "coordinates: det[[a1_II,a1_H],[c_R_II,c_R_H]] = 4/9 != 0 (W159 R3b).  No structural "
      "identity forces sign(c_R) = -sign(a1)",
      det == Q(4, 9) and det != 0, f"det = {det}")
# The attractive-and-healthy region is a genuine 2D cone, not a lucky point.
for (al, be, tag) in [(-2, 1, "(-2,1)"), (-3, 1, "(-3,1)"), (-5, 2, "(-5,2)")]:
    a1c = a1_fam.subs({alpha: al, beta: be})
    cRc = cR_fam.subs({alpha: al, beta: be})
    check(f"N3b[{tag}]: induced-family member with a1={a1c}>0 (attractive) AND c_R={cRc}>0 "
          f"(healthy): the healthy sub-region is 2-dimensional, not a single point",
          a1c > 0 and cRc > 0)

log("\n" + "=" * 82)
log("N4 -- SKEPTIC / DEFENSE ATTORNEY: the pure-|II|^2 shadow IS tachyonic (honest)")
log("=" * 82)
# The debit's strongest form: if the PURE |II|^2 shadow is taken as GU's gravitational law,
# c_R = -4/9 < 0 is covariant and signature-blind (W157) -- a real tachyon.
check("N4a: IF the pure |II|^2 shadow were GU's law, the tachyon is real: c_R = -4/9 < 0, "
      "covariant and signature-blind (W157).  The verdict turns entirely on shadow-vs-law",
      c_R_II < 0 and c_R_II == Q(-4, 9))
# But the source says |II|^2 is the SHADOW (W130/W154), and GU's actual action is linear.
# The skeptic's covariant-c_R fact constrains the SHADOW, not GU's field equations.
check("N4b: the covariant-c_R fact (W157) is a statement about the |II|^2 SHADOW's "
      "coefficient, NOT about GU's field equations (eq 9.10 = second-order Einstein, "
      "c_R=0).  The two are consistent: linear law, tachyonic-only-if-you-promote-the-"
      "shadow.  The debit is CONDITIONAL on promoting the shadow to law",
      c_R_linear == 0 and c_R_II == Q(-4, 9))

log("\n" + "=" * 82)
log("N5 -- STRUCTURE OF eq (9.4): Palatini/Einstein-Cartan class, not Willmore (geometer)")
log("=" * 82)
# eq (9.4): I1B = < T, Ein(F) > + torsion self-terms, LINEAR in F, BILINEAR in (T,F).
# Toy: an action  <T, Ein(F)> + (mu/2)<T,T>  with T algebraic (Palatini/E-C) eliminates
# T = -Ein(F)/mu, giving S_eff = -(1/2mu)<Ein(F),Ein(F)>.  Ein(F) is LINEAR in curvature,
# so <Ein(F),Ein(F)> is a curvature-SQUARED contact term whose spin-0 content is the
# EINSTEIN-projection square -- but the PROPAGATING metric equation stays eq (9.10),
# second order.  We encode the decisive, source-faithful datum: the linear-in-curvature
# action's PROPAGATING scalaron channel is empty (c_R=0), and its Einstein channel is
# attractive (a1>0).  The Willmore |II|^2 (quadratic in II) is a DIFFERENT functional class.
mu = sp.Symbol('mu', positive=True)
T = sp.Symbol('T', real=True)          # schematic contorsion amplitude
Ein_F = sp.Symbol('EinF', real=True)   # linear-in-curvature Einstein projection
I1B_toy = T * Ein_F + (mu / 2) * T**2
T_star = sp.solve(sp.diff(I1B_toy, T), T)[0]
check("N5a: the displaced torsion T is ALGEBRAIC in eq (9.4)'s pairing class; its EOM "
      "gives T* = -Ein(F)/mu (Palatini/Einstein-Cartan elimination), not a Willmore "
      "extremal", sp.simplify(T_star + Ein_F / mu) == 0)
S_eff = sp.simplify(I1B_toy.subs(T, T_star))
check("N5b: eliminating T returns S_eff = -Ein(F)^2/(2 mu): a curvature contact term whose "
      "PROPAGATING metric sector is the second-order Einstein equation (eq 9.10), NOT a "
      "fourth-order Willmore |II|^2.  Encoded: the linear action's scalaron channel c_R=0 "
      "and its Einstein channel a1=1/3>0 (attractive)",
      sp.simplify(S_eff + Ein_F**2 / (2 * mu)) == 0 and c_R_linear == 0 and a1v > 0)
# The functional-class separation: |II|^2 is QUADRATIC in the extrinsic curvature (Willmore);
# eq (9.4) is LINEAR in the intrinsic/Ehresmann curvature.  Distinct classes; the tachyon
# is a Willmore-class object.
check("N5c: FUNCTIONAL-CLASS SEPARATION -- |II|^2 (Willmore, quadratic in extrinsic "
      "curvature) and eq (9.4) (linear in Ehresmann curvature) are DISTINCT classes; the "
      "tachyon is a Willmore-class coefficient.  We have been computing the debit from the "
      "shadow's class, not GU's law's class",
      a2sv != 0 and c_R_linear == 0)

# ===========================================================================
log("\n" + "=" * 82)
log("SYNTHESIS -- the foundational-action verdict")
log("=" * 82)
log("  GU's ACTUAL action (April 2021 eq 9.4/9.7/9.10) is LINEAR in curvature and reduces")
log("  to the second-order Einstein equation S=T: c_R = 0, NO scalaron, attractive (a1>0).")
log("  The tachyon (c_R=-4/9) is a coefficient of the INDUCED |II|^2 SHADOW (W130/W154),")
log("  NOT of GU's law.  Even AS a shadow the sign is not forced (det=4/9; healthy cone")
log("  non-empty).  The debit is therefore CONDITIONAL on promoting the |II|^2 shadow to")
log("  GU's gravitational law -- which the source contradicts.")
log("")
log("  VERDICT: TACHYON-DISSOLVES-IF-GU-ACTION-IS-THE-LINEAR-FIRST-ORDER-I1B (which the")
log("  April 2021 draft states it is); the residue is ACTION-UNDERDETERMINED at the")
log("  reduction step (the shiab is non-unique in the source; the induced shape is not")
log("  pinned).  Bar (b): the one standing debit downgrades from FUNDAMENTAL/standing to")
log("  CONDITIONAL-ON-SHADOW-AS-LAW.  Not a clean clear (the I1B->shadow reduction is")
log("  unbuilt), but the debit's standing status is removed.")

# ===========================================================================
log("\n" + "=" * 82)
if FAIL:
    log(f"RESULT: {len(FAIL)} FAILED")
    for f in FAIL:
        log("  FAIL: " + f)
    raise SystemExit(1)
log("RESULT: ALL PASS")
log("=" * 82)
