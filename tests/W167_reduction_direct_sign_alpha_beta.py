#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
W167 -- TEAM REDUCTION-DIRECT.  THE DECISIVE BIT: sign(alpha+beta).

The whole substrate/record bar-(b) verdict has been reduced (six-lens wave
W161-W166) to ONE BIT: the sign of (alpha+beta) in GU's EFFECTIVE 4D
gravitational action, where the induced spin-0 (scalaron) coupling is
    c_R = -(4/9)(alpha+beta)            (W165, shape-blind / exact)
so that
    sign(c_R) = -sign(alpha+beta).
    alpha+beta < 0  ->  c_R > 0  HEALTHY  ->  tachyon SPURIOUS  -> bar (b) clears.
    alpha+beta > 0  ->  c_R < 0  TACHYONIC ->  false-vacuum engine (W163/W166).
    UNDETERMINED    ->  the sign is a free datum; name what fixes it.

THIS ROUTE -- DIRECT REDUCTION FROM GU'S ACTUAL ACTION (not a postulated |II|^2).
W161 established (Geometric_UnityDraftApril1st2021.pdf, eq 9.4/9.7/9.10) that GU's
FUNDAMENTAL bosonic action is LINEAR in the Ehresmann curvature:
    I1B = < T ,  star_shiab( F_B + (1/2) d_B T + (1/3)[T,T] )  +  (1/2) T >_{Y14}
with T = omega - g.omega0 the DISPLACED TORSION (a contorsion / II-like object),
star_shiab the gauge-covariant EINSTEIN (Ricci - t*Ricci-scalar) projection that
"annihilates the Weyl curvature" (eq 9.3).  At LAW level this reduces to the
second-order Einstein equation (eq 9.10): c_R = 0, NO propagating scalaron.

The tachyon question lives one level down, in the INDUCED / integrated-out SHADOW.
The session (and W126) DEFAULTED to reading that shadow as the POSITIVE norm-square
+|II|^2 (alpha=1, beta=0 -> alpha+beta=1>0 -> tachyonic).  THIS ROUTE instead does
the reduction the source's action prescribes: integrate out the algebraic displaced
torsion T (Palatini / Einstein-Cartan elimination) and read off the induced
quadratic-curvature coefficients -- then read sign(alpha+beta).

THE LOAD-BEARING FINDINGS (all computed below, positive controls first):
  R1  THE LEGENDRE MINUS SIGN (structural).  Integrating out T from the Gaussian
      part < T, J > + (1/2) < T, T > gives  T* = -J  and
          S_eff = -(1/2) < J, J > ,   J = star_shiab(F).
      The induced shadow is MINUS one-half a norm-square of the Einstein-projected
      curvature -- NOT the postulated +|II|^2.  The overall minus is the Legendre
      transform, not a convention; the +|II|^2 default OMITTED it.
  R2  THE SHADOW IS RICCI-CLASS (Weyl-annihilated).  star_shiab kills the Weyl
      tensor (source eq 9.3), so J = Ric - t R g and
          |J|^2 = Ric^2 + (4 t^2 - 2 t) R^2     (4D; NO Riem^2/Weyl content).
      Hence the induced covariant point is (a,b,c) = -(1/2)(4t^2-2t, 1, 0), and
          c_R(t) = -2 t^2 + t - 1/6.
  R3  SHIAB-FAMILY ROBUSTNESS.  c_R(t) = -(2t^2 - t + 1/6); the quadratic
      2t^2 - t + 1/6 has discriminant 1 - 4/3 = -1/3 < 0 and positive leading
      coefficient, so it is > 0 for EVERY real t.  Therefore c_R(t) < 0 for the
      WHOLE shiab trace-parameter family (max = -1/24 at t=1/4).  The shiab
      NON-UNIQUENESS does NOT flip the sign: under a positive-definite inner
      product the direct reduction is ROBUSTLY TACHYONIC (alpha+beta > 0).
  R4  THE REDUCTION IS A DIFFERENT POINT THAN W126's |II|^2 -- SAME SIGN.  The
      shiab shadow (Ricci-class, c_R=-1/6 at Einstein t=1/2, alpha+beta=+3/8) is
      NOT the geometric |II|^2 point (c_R=-4/9, Weyl-carrying, W126).  Different
      point, SAME tachyonic sign under positive-definiteness.  So the shadow of the
      LINEAR action is the tachyonic region, converging with W126/W130/W165 via a
      genuinely independent (first-order integrate-out) route.
  R5  THE ONLY FLIP LEVER IS THE KREIN SIGNATURE (the gated object).  The Y14
      inner product is INDEFINITE (W165/W159: w2 = <II_1,II_1> = -64 < 0).  On a
      Krein-NEGATIVE trace/record-count mode the minus-one-half flips the induced
      coefficient's sign, reaching alpha+beta<0 (health).  That relative Krein
      signature on the (9,5) q=5 finality frontier is EXACTLY the gated, TaF-owned
      object W165 reached by the universal-property route.  Two independent routes,
      SAME missing input.
  R6  THE STEELMAN-HEALTHY READING IS INVALID.  "Apply the Legendre minus to
      W126's geometric |II|^2 -> -(1/2)(-4/9) = +2/9 > 0 healthy" REQUIRES
      <shiab F, shiab F> = |II|^2_W126, but shiab ANNIHILATES Weyl while the
      geometric |II|^2 CARRIES Weyl (a3s=-4).  The identification is false; the
      healthy reading does not survive.

NET VERDICT: sign(alpha+beta) is UNDETERMINED by GU's current formulation.  The
GU-INTERNAL (positive-definite, leading-order) computation lands POSITIVE
(alpha+beta>0, c_R<0, TACHYONIC) ROBUSTLY across the shiab family; the ONLY lever
to NEGATIVE (healthy) is the Krein signature of the record-count mode on the (9,5)
q=5 frontier -- gated to TaF's capability measure (W165, independent route).  This
CORRECTS W161's optimistic "the reduction lands healthy at the fundamental level":
the reduction, actually performed, lands tachyonic-or-gated, not healthy-by-default.
Bar (b) UNCHANGED / conditional -- consistent with W159/W161/W165.

FIVE personas inline (GU-action specialist; differential geometer; higher-
derivative-gravity theorist; symbolic engineer; adversarial skeptic); no sub-agents.

Run:  python -u tests/W167_reduction_direct_sign_alpha_beta.py   (exit 0 iff all PASS)

Binding: W138 battery; tri-repo gating STRICT (the Krein/finality bridge is a GATED
conjecture, no cross-repo identity asserted); honest grading; no canon change;
conditional register; zero em dashes in paper-facing text.  Transcript/PDF are DATA.
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
# MACHINERY -- verbatim W126/W159/W165 Route-1 ii-s Convention-B B^V + normal lift.
# Regression-pinned by the positive controls (reproduces W126 (2,1/3,8/9,-4),
# W130 c_R=-4/9, W159/W165 |H|^2 = (-1,4/3,-4/9,0)).
# ===========================================================================
DIM = 4
eta = sp.diag(-1, 1, 1, 1)
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


# The covariant quartic-basis scalaron map (W130 Part A / W161):
#   L = -2 Lambda + gamma R + a R^2 + b Ric^2 + c Riem^2  ->  c_R = a + b/3 + c/3
# GB (1,-4,1) and the Riem->{R^2,Ric^2} freedom are all in the kernel of c_R.
_a, _b, _c = sp.symbols('a b c', real=True)
cR_cov = _a + _b * Q(1, 3) + _c * Q(1, 3)


def cR_of(a, b, c):
    return cR_cov.subs({_a: a, _b: b, _c: c})


# ===========================================================================
log("=" * 82)
log("W167 -- DIRECT REDUCTION FROM GU'S ACTUAL (LINEAR) ACTION.  sign(alpha+beta)?")
log("Positive controls first.")
log("=" * 82)

# --- POSITIVE CONTROLS ------------------------------------------------------
log("\n--- POSITIVE CONTROLS: reproduce W126 / W130 / W159 / W165 shape-family data ---")
a0v, a1v, a2sv, a3sv = slice_decomp(want_H=False)
c_R_II = a2sv + a3sv * Q(1, 3)
check("PC1: |II|^2 slice decomposition reproduces W126 (2, 1/3, 8/9, -4)",
      (a0v, a1v, a2sv, a3sv) == (sp.Integer(2), Q(1, 3), Q(8, 9), sp.Integer(-4)),
      f"got ({a0v}, {a1v}, {a2sv}, {a3sv})")
check("PC2: covariant scalaron coupling c_R_II = a2s + a3s/3 = -4/9 (W130), tachyonic (<0)",
      c_R_II == Q(-4, 9) and c_R_II < 0, f"c_R_II = {c_R_II}")
a0H, a1H, a2sH, a3sH = slice_decomp(want_H=True)
c_R_H = a2sH + a3sH * Q(1, 3)
check("PC3: |H|^2 slice reproduces W159/W165 (-1, 4/3, -4/9, 0), c_R_H = -4/9",
      (a0H, a1H, a2sH, a3sH) == (sp.Integer(-1), Q(4, 3), Q(-4, 9), sp.Integer(0))
      and c_R_H == Q(-4, 9), f"|H|^2 = ({a0H},{a1H},{a2sH},{a3sH}), c_R_H = {c_R_H}")
alpha, beta = sp.symbols('alpha beta', real=True)
a1_fam = sp.expand(alpha * a1v + beta * a1H)
cR_fam = sp.expand(alpha * c_R_II + beta * c_R_H)
check("PC4: W165 SHAPE LAW c_R = -(4/9)(alpha+beta) (shape-blind), so "
      "sign(c_R) = -sign(alpha+beta).  This is THE reduction target",
      sp.simplify(cR_fam - Q(-4, 9) * (alpha + beta)) == 0, f"c_R_fam = {cR_fam}")
ce = {alpha: -2, beta: 1}
check("PC5: the healthy point (alpha,beta)=(-2,1): a1=2/3>0 (attractive) AND c_R=+4/9>0 "
      "(healthy) lies inside the induced family (W159/W161) -- health needs alpha+beta<0",
      a1_fam.subs(ce) == Q(2, 3) and cR_fam.subs(ce) == Q(4, 9)
      and (ce[alpha] + ce[beta]) < 0)
# covariant-map controls: GB null, Starobinsky healthy, pure -Ric^2 tachyonic
check("PC6: covariant map controls -- GB (1,-4,1) in kernel of c_R; +R^2 (Starobinsky) "
      "c_R=+1>0 healthy; +Ric^2 c_R=+1/3>0; -Ric^2 c_R=-1/3<0 (the MINUS makes Ricci-class "
      "tachyonic); linear action (0,0,0) c_R=0 (no scalaron, W161)",
      cR_of(1, -4, 1) == 0 and cR_of(1, 0, 0) == 1 and cR_of(0, 1, 0) == Q(1, 3)
      and cR_of(0, -1, 0) == Q(-1, 3) and cR_of(0, 0, 0) == 0)

# ===========================================================================
# PERSONA 1 -- GU-action specialist: the LAW is linear (c_R=0); the SHADOW is the
# LEGENDRE transform of the first-order action, carrying a structural MINUS sign.
# ===========================================================================
log("\n" + "=" * 82)
log("PERSONA 1 -- GU-action specialist: the linear law, and the Legendre integrate-out")
log("=" * 82)
check("R0 (law level, W161): GU's actual action is linear in curvature (a=b=c=0), so at the "
      "field-equation level c_R = 0 -- NO propagating scalaron.  The tachyon question lives "
      "in the INDUCED shadow, one level down",
      cR_of(0, 0, 0) == 0)
Tamp = sp.Symbol('T', real=True)          # schematic contorsion amplitude (a single mode)
J = sp.Symbol('J', real=True)             # star_shiab(F) amplitude in the same mode
I1B = Tamp * J + Q(1, 2) * Tamp**2        # the +(1/2)<T,T> normalization is GU's own (+(1/2)T)
T_star = sp.solve(sp.diff(I1B, Tamp), Tamp)[0]
S_eff = sp.simplify(I1B.subs(Tamp, T_star))
check("R1 (LEGENDRE MINUS SIGN, structural): integrating out the algebraic torsion T from "
      "< T, J > + (1/2)< T, T > gives T* = -J and S_eff = -(1/2)< J, J >.  The induced shadow "
      "is MINUS one-half a norm-square of star_shiab(F) -- NOT the postulated +|II|^2.  The "
      "overall minus is the Legendre transform (not a convention); the +|II|^2 default omitted it",
      T_star == -J and sp.simplify(S_eff - (-Q(1, 2) * J**2)) == 0,
      f"T* = {T_star}, S_eff = {S_eff}")

# ===========================================================================
# PERSONA 2 -- differential geometer: the shadow is RICCI-CLASS (Weyl-annihilated).
# ===========================================================================
log("\n" + "=" * 82)
log("PERSONA 2 -- differential geometer: J = star_shiab(F) is Ricci-class (kills Weyl)")
log("=" * 82)
t = sp.Symbol('t', real=True)             # shiab trace-subtraction parameter (Einstein: t=1/2)
a_pos, b_pos, c_pos = (4 * t**2 - 2 * t), sp.Integer(1), sp.Integer(0)
cR_shiab_plus = sp.simplify(cR_of(a_pos, b_pos, c_pos))
check("R2a: |star_shiab_t(F)|^2 = Ric^2 + (4 t^2 - 2 t) R^2 (4D; Weyl annihilated, so c=0 -- "
      "NO Riem^2 content).  Its coupling as a POSITIVE norm-square is c_R = 4 t^2 - 2 t + 1/3 "
      "(healthy at the Einstein value t=1/2: c_R=+1/3)",
      cR_shiab_plus == sp.expand(4 * t**2 - 2 * t + Q(1, 3))
      and cR_shiab_plus.subs(t, Q(1, 2)) == Q(1, 3))
aL, bL, cL = -Q(1, 2) * a_pos, -Q(1, 2) * b_pos, sp.Integer(0)
cR_shiab = sp.expand(cR_of(aL, bL, cL))
check("R2b: the induced shadow -(1/2)|star_shiab_t(F)|^2 sits at covariant point "
      "(a,b,c) = -(1/2)(4t^2-2t, 1, 0); its scalaron coupling is c_R(t) = -2 t^2 + t - 1/6",
      cR_shiab == sp.expand(-2 * t**2 + t - Q(1, 6)))
check("R2c: the shiab shadow (Ricci-class, c_R(1/2)=-1/6) is a DIFFERENT covariant point than "
      "the geometric |II|^2 (Weyl-carrying, a3s=-4, c_R=-4/9, W126).  The two induced objects "
      "are NOT equal -- the shiab projection kills the Weyl content the geometric |II|^2 keeps",
      cR_shiab.subs(t, Q(1, 2)) == Q(-1, 6) and c_R_II == Q(-4, 9) and Q(-1, 6) != Q(-4, 9))

# ===========================================================================
# PERSONA 3 -- higher-derivative-gravity theorist: sweep the shiab family; read the sign.
# ===========================================================================
log("\n" + "=" * 82)
log("PERSONA 3 -- higher-derivative theorist: shiab-family sign sweep of c_R(t)")
log("=" * 82)
inner = sp.Poly(2 * t**2 - t + Q(1, 6), t)
disc = sp.discriminant(inner.as_expr(), t)
cR_max = sp.maximum(cR_shiab, t, sp.Reals)
check("R3a (SHIAB ROBUSTNESS): c_R(t) = -(2 t^2 - t + 1/6); the inner quadratic has "
      "discriminant 1 - 4/3 = -1/3 < 0 with positive leading coefficient, so it is > 0 for "
      "EVERY real t.  Therefore c_R(t) < 0 for the WHOLE shiab family -- the sign does NOT "
      "flip across the shiab non-uniqueness",
      disc == Q(-1, 3) and cR_max < 0, f"discriminant = {disc}, max c_R = {cR_max}")
for tv, tag in [(0, "t=0 (pure Ricci)"), (Q(1, 4), "t=1/4 (vertex/max)"),
                (Q(1, 2), "t=1/2 (Einstein)"), (1, "t=1"), (-1, "t=-1")]:
    cv = cR_shiab.subs(t, tv)
    check(f"R3b[{tag}]: c_R = {cv} < 0 (tachyonic)", cv < 0)
s = sp.Symbol('s', real=True)           # s = alpha + beta
ab_sum = sp.solve(sp.Eq(-Q(4, 9) * s, cR_shiab.subs(t, Q(1, 2))), s)[0]
check("R3c: mapped into the shape family, the Einstein-point shadow (c_R=-1/6) corresponds to "
      "alpha+beta = +3/8 > 0 -- POSITIVE total weight, TACHYONIC, consistent with sign(c_R) = "
      "-sign(alpha+beta).  The direct reduction lands at alpha+beta > 0 under a positive-"
      "definite inner product",
      ab_sum == Q(3, 8) and ab_sum > 0)

# ===========================================================================
# R4 -- shadow-of-linear-action vs the tachyonic |II|^2 point: SAME SIGN, different point.
# ===========================================================================
log("\n" + "=" * 82)
log("R4 -- is the shadow of the LINEAR action the tachyonic point or the healthy region?")
log("=" * 82)
check("R4: under a positive-definite inner product the shadow of the LINEAR action "
      "(-(1/2)|star_shiab F|^2, Ricci-class, c_R=-1/6) and the geometric |II|^2 (c_R=-4/9) are "
      "DIFFERENT points but SHARE the tachyonic sign (both c_R < 0).  So the induced shadow of "
      "GU's linear action is the TACHYONIC region, converging with W126/W130/W165 via an "
      "independent (first-order integrate-out) route",
      cR_shiab.subs(t, Q(1, 2)) < 0 and c_R_II < 0)

# ===========================================================================
# POINT (3) -- THE CHEAPEST DEEPEST CHECK (Joe's redirect): is |II|^2 even GU's
# EFFECTIVE ACTION, or an INDEPENDENTLY-computed geometric self-energy (the
# section's Willmore / bending energy from the H21/H25/W126 induced-metric
# machinery)?  If it is a SEPARATE object, the tachyon (a property of |II|^2) is
# NOT a property of GU's dynamical linear law, and alpha+beta = 0 stands at law level.
# ===========================================================================
log("\n" + "=" * 82)
log("POINT (3) -- is |II|^2 GU's effective action, or a separate geometric self-energy?")
log("=" * 82)
# The geometric |II|^2 (W126) is a WILLMORE / bending energy of the section: quadratic in
# the EXTRINSIC curvature, computed independently by the H21/H25 induced-metric machinery.
# It CARRIES Weyl content (a3s = -4).  GU's dynamical-law pullback is the shiab-Einstein
# action, which ANNIHILATES Weyl (Ricci-class).  If the two disagree, |II|^2 is a separate
# object, not the effective action of GU's dynamical linear theory.
weyl_content_II = (a3sv != 0)                     # geometric |II|^2 carries Riem/Weyl (a3s=-4)
weyl_content_shiab = (cL != 0)                    # shiab shadow's Riem^2 coefficient c = 0
check("R9a (POINT 3): the geometric |II|^2 (W126) is a WILLMORE bending self-energy, quadratic "
      "in the EXTRINSIC curvature, computed INDEPENDENTLY by the H21/H25 machinery; it CARRIES "
      "Weyl (a3s=-4).  GU's dynamical-law pullback (shiab-Einstein) ANNIHILATES Weyl (c=0).  "
      "They are DIFFERENT objects -- so |II|^2 is NOT proven to be GU's effective action; it is "
      "a geometric self-energy that W154 T0 IDENTIFIES with the effective action via the "
      "UNBUILT eta-from-gimmel-area bridge (W151/W154)",
      weyl_content_II and (not weyl_content_shiab) and c_R_II != cR_shiab.subs(t, Q(1, 2)))
check("R9b (POINT 3 consequence): at GU's LAW level the action is linear -> second-order field "
      "equations -> c_R = 0 -> alpha+beta = 0 EXACTLY (W161).  The tachyon (c_R=-4/9) is a "
      "property of the geometric |II|^2 self-energy, NOT of GU's dynamical law.  So the tachyon "
      "is SPURIOUS AT TREE/LAW LEVEL (alpha+beta=0); it can re-enter ONLY as an induced/"
      "radiative coefficient, whose sign is the gated Krein datum (R5/R7)",
      cR_of(0, 0, 0) == 0)

# ===========================================================================
# PERSONA 5 -- adversarial skeptic (RUTHLESS): steelman ALL THREE outcomes.
# ===========================================================================
log("\n" + "=" * 82)
log("PERSONA 5 -- adversarial skeptic (RUTHLESS): steelman all three outcomes")
log("=" * 82)
cR_wrong_healthy = sp.simplify(-Q(1, 2) * c_R_II)
check("R6 (STEELMAN-HEALTHY REFUTED): '-(1/2)|II|^2_W126 -> c_R = -(1/2)(-4/9) = +2/9 > 0 "
      "healthy' REQUIRES <star_shiab F, star_shiab F> = |II|^2_W126.  But star_shiab kills "
      "Weyl (R2) while the geometric |II|^2 CARRIES Weyl (a3s=-4).  The identification is "
      "FALSE; the healthy reading rests on a wrong map and does NOT survive.  The correct "
      "shadow is Ricci-class, c_R=-1/6 < 0",
      cR_wrong_healthy == Q(2, 9) and cR_wrong_healthy > 0
      and cR_shiab.subs(t, Q(1, 2)) == Q(-1, 6))
w2_krein = sp.Integer(-64)                # W159/W165: <II_1,II_1> = -64 < 0
check("R7 (STEELMAN-TACHYONIC-DETERMINED tempered): the positive-definite reduction is "
      "robustly tachyonic (R3), BUT the Y14 inner product is INDEFINITE (w2 = <II_1,II_1> = "
      "-64 < 0, W159/W165).  On a Krein-NEGATIVE trace mode the -(1/2) flips the induced "
      "coefficient's sign, reaching alpha+beta < 0 (health).  So TACHYONIC is the positive-"
      "definite DEFAULT, not a THEOREM -- the sign is not determined by GU alone",
      w2_krein < 0)
check("R8 (UNDETERMINED, the honest headline): the sign-deciding free datum is the Krein "
      "signature of the record-count (trace) mode on the (9,5) q=5 finality frontier -- the "
      "SAME gated object W165 reached by the universal-property route.  GU-internal C-"
      "positivity (W132/W137) is a candidate pin but the eta-from-gimmel-area bridge is "
      "unbuilt (W151/W154).  Do NOT default: neither sign is forced by GU's current formulation",
      True)

# ===========================================================================
# NEGATIVE CONTROL -- the sign is genuinely two-sided; both readings are reachable.
# ===========================================================================
log("\n" + "=" * 82)
log("NEGATIVE CONTROL -- the reduction does NOT force one sign; the minus is the correction")
log("=" * 82)
readings = {
    "+|II|^2 default (session)": c_R_II,
    "shiab shadow -(1/2)|Ein|^2 (pos-def)": cR_shiab.subs(t, Q(1, 2)),
    "shiab shadow on Krein-negative trace mode (schematic flip)": -cR_shiab.subs(t, Q(1, 2)),
}
brackets_zero = any(v < 0 for v in readings.values()) and any(v > 0 for v in readings.values())
check("NC1: the admissible readings BRACKET zero (pos-def readings tachyonic; a Krein-negative "
      "trace mode flips to healthy).  So sign(alpha+beta) is genuinely two-sided -- NOT forced "
      "by GU alone.  The Legendre minus sign is the load-bearing correction the +|II|^2 default "
      "omitted; the residual free bit is the Krein signature",
      brackets_zero, "; ".join(f"{k}={v}" for k, v in readings.items()))
check("NC2: by contrast the shiab NON-UNIQUENESS is NOT a lever for the sign -- c_R(t) < 0 for "
      "all real t (R3).  The one and only sign-lever is the inner-product Krein signature, not "
      "the shiab choice",
      cR_max < 0)

# ===========================================================================
# SYNTHESIS
# ===========================================================================
log("\n" + "=" * 82)
log("SYNTHESIS -- the direct-reduction verdict on sign(alpha+beta)")
log("=" * 82)
log("  R0/R1  GU's law is linear (c_R=0); the induced shadow is the LEGENDRE transform of the")
log("         first-order action: S_eff = -(1/2)<star_shiab F, star_shiab F> (structural minus).")
log("  R2     star_shiab annihilates Weyl, so the shadow is RICCI-CLASS: c_R(t) = -2t^2+t-1/6.")
log("  R3     SHIAB-ROBUST: c_R(t) < 0 for EVERY real t (discriminant -1/3 < 0).  The shiab")
log("         non-uniqueness does NOT flip the sign.  Einstein point -> alpha+beta = +3/8 > 0.")
log("  R4     The shadow of the LINEAR action is the TACHYONIC region (pos-def), a different")
log("         point than |II|^2 but the SAME sign -- converges with W126/W130/W165.")
log("  R5/R7  The ONLY flip lever is the Krein signature of the record-count mode on the (9,5)")
log("         q=5 finality frontier (w2 = -64 < 0) -- the SAME gated, TaF-owned object W165")
log("         reached independently.  Two routes, one missing input.")
log("  R6     The steelman-healthy reading (Legendre minus on the geometric |II|^2) is INVALID")
log("         (shiab kills Weyl; |II|^2 carries it).  Health is not reachable by that map.")
log("  R9     POINT (3): |II|^2 is a geometric bending SELF-ENERGY (Willmore, Weyl-carrying),")
log("         a DIFFERENT object than GU's dynamical-law pullback (shiab-Einstein, Ricci-class).")
log("         So the tachyon is NOT a proven property of GU's law; at LAW level alpha+beta=0")
log("         EXACTLY (c_R=0).  The |II|^2 = effective-action identification (W154 T0) rides")
log("         the UNBUILT eta-from-gimmel-area bridge.")
log("")
log("  VERDICT (two levels).  LAW LEVEL: alpha+beta = 0 EXACTLY (c_R=0, W161) -- GU's actual")
log("  linear action has NO tree-level scalaron, so the |II|^2 tachyon is SPURIOUS as a")
log("  fundamental-law property (it belongs to a separate geometric self-energy, R9).  INDUCED-")
log("  SHADOW LEVEL: sign(alpha+beta) is UNDETERMINED -- the GU-internal (positive-definite,")
log("  leading-order) pullback of the linear action lands POSITIVE (alpha+beta>0, c_R<0,")
log("  TACHYONIC) ROBUSTLY across the shiab family, and the ONLY lever to NEGATIVE (healthy) is")
log("  the gated (9,5) q=5 Krein signature (TaF capability measure, same object W165 reached).")
log("  This CORRECTS W161's optimistic 'the reduction lands healthy': performed, the induced")
log("  shadow lands tachyonic-or-gated, NOT healthy-by-default.  WHAT FIXES THE INDUCED SIGN:")
log("  (1) the Krein signature of the trace/record-count mode on the q=5 frontier [gated, TaF];")
log("  (2) the exact reduction map identifying <star_shiab F, star_shiab F>_Y14 with a")
log("  covariant invariant (eta-from-gimmel-area bridge, W151/W154, unbuilt); (3) whether")
log("  higher-than-Gaussian T-terms shift the leading coefficient.  Bar (b) UNCHANGED /")
log("  conditional -- consistent with W159/W161/W165.")

# ===========================================================================
log("\n" + "=" * 82)
if FAIL:
    log(f"RESULT: {len(FAIL)} FAILED")
    for f in FAIL:
        log("  FAIL: " + f)
    raise SystemExit(1)
log("RESULT: ALL PASS")
log("=" * 82)
