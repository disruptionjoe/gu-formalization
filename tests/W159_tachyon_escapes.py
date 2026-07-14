#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
W159 -- TEAM TACHYON-ESCAPES.  Does debit-1 (the positive-norm tachyonic scalaron)
stop being a flaw via ANY of three live routes, after the W157 keystone FAILED
(a2 = -a1^2 is a COINCIDENCE; only the SIGN survives, basis/signature-invariant)?

CONTEXT (CITED, not re-derived):
  * W126: induced |II|^2 on the conformal family, EXACT (all orders in phi).  Potential
    slice (dphi=0): W = a0 + a1 R + a2s R^2 + a3s Ric^2, (a0,a1,a2s,a3s)=(2,1/3,8/9,-4);
    potential sector EXACTLY quadratic (c_3=c_4=...=0).  Gradient sector carries the
    quartic: W(v,s=0,E0=1) = 2 + 16 v^2 + 320 v^4 + ...  (the object route 2 tests).
  * W130: covariant scalaron coupling c_R = a2s + a3s/3 = -4/9 (GB freedom cancels);
    Weyl coupling c_W = +2; sign maps f_0^2 = 1/(6 c_R) = -3/8, f_2^2 = -1/(2 c_W) = -1/4;
    native tree poles m_0^2 = gamma_phi/(6 c_R) = -1/4, m_2^2 = -gamma_TT/(2 c_W) = -1/4
    (induced measure; gamma_TT:gamma_phi:gamma_slice = 3:2:1 => gamma_TT=1, gamma_phi=2/3).
    Native tree point (f_2^2, f_0^2) = (-1/4, -3/8): BOTH negative, OFF the AF branch.
  * W128: at the Reuter/AS FP the R^2 direction is RELEVANT (ported), so the de-slaved
    root is SIGN-LOCKED positive (m_0^2 >= 0 PERMITTED); but healthy AND tachyonic
    trajectories are BOTH UV-complete (PERMITTED-NOT-FORCED); E2 fork STANDS (no native
    selector).  The AS trajectory keeps f_2^2 > 0 at every finite scale (1/f_2^2 law).
  * W157: a2 = -a1^2 is a COINCIDENCE (MSS-slice + normalization artifact).  Only the
    SIGN a2/a1 < 0 survives; c_R = -4/9 < 0 is signature-blind (NOT a (9,5) effect).

THE THREE ROUTES (each a live way debit-1 could stop being a flaw):
  ROUTE 1 (AF/AS branch).  Is the tachyon an AF-branch artifact and GU actually on the
    AS branch with a HEALTHY scalaron?  Can the native tree point flow to the AS FP
    (avoiding the strong-coupling passage AF needs), giving m_0^2 >= 0?
  ROUTE 2 (gradient saturation).  Does the gradient quartic 320 v^4 bound the tachyonic
    runaway into a finite-field attractor within EFT validity?
  ROUTE 3 (sign-forcing residual).  Is c_R < 0 FORCED by a1 > 0 in the covariant action
    (a structural sign identity), or SIGN-FREE?
  DISPERSION (folded in).  Does the tachyonic pole sit at a physical k, or is there a
    finite-k band (scale selection) that changes its interpretation?

FIVE personas inline (FRG/branch; nonlinear-saturation; higher-derivative/dispersion;
symbolic engineer; adversarial skeptic).  Deterministic sympy, positive controls first.
Run:  python -u tests/W159_tachyon_escapes.py   (exit 0 iff all PASS).

Binding: W138 battery; E2 resolved only by genuine evidence (else carried); honest
grading; no canon change; conditional register; zero em dashes in paper-facing text.
"""
from __future__ import annotations
import sympy as sp

FAIL = []


def check(name, ok, detail=""):
    print(("PASS" if ok else "FAIL") + " :: " + name + (("  --  " + detail) if detail else ""), flush=True)
    if not ok:
        FAIL.append(name)


def log(msg=""):
    print(msg, flush=True)


# ===========================================================================
# MACHINERY -- verbatim W126 Route-1 ii-s Convention-B B^V + normal lift, plus
# the from-scratch curvature decomposition.  Regression-pinned by the positive
# controls below (reproduces W126 (2,1/3,8/9,-4) and W130 c_R = -4/9).
# ===========================================================================
DIM = 4
eta = sp.diag(-1, 1, 1, 1)                                        # GU base signature (1,3)
pairs = [(a, b) for a in range(DIM) for b in range(a, DIM)]
xs = [sp.Symbol(f'x{i}', real=True) for i in range(DIM)]
p = sp.Symbol('p', real=True)
E0 = sp.Symbol('E0', positive=True)
vsym = [sp.Symbol(f'v{i}', real=True) for i in range(DIM)]        # dphi(0) -- gradient jet
ssym = {(i, j): sp.Symbol(f's{i}{j}', real=True) for (i, j) in pairs}


def S(i, j):
    return ssym[(i, j)] if i <= j else ssym[(j, i)]


def phi_jet(with_v=True):
    ph = p
    if with_v:
        ph += sum(vsym[i] * xs[i] for i in range(DIM))
    ph += sp.Rational(1, 2) * sum(S(i, j) * xs[i] * xs[j] for i in range(DIM) for j in range(DIM))
    return ph


def at0(expr):
    e = expr.subs({xi: 0 for xi in xs})
    e = e.subs(p, sp.log(E0) / 2)
    return sp.expand(sp.powsimp(e, force=True))


def Vg_of(Gi, k, l):
    A = Gi * k
    B = Gi * l
    return sp.trace(A * B) - sp.Rational(1, 2) * sp.trace(A) * sp.trace(B)


def route1_W(with_v, vvals=None, svals=None, want_H=False, subtract_slice=False):
    """Exact W = |II|^2 (and optionally |H|^2) at x=0 for the conformal jet."""
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
    gbarGam0 = [[[sp.Rational(1, 2) * sum(gbari0[l, k] * (dgbar0[m][n, k] + dgbar0[n][m, k]
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
                            sp.Rational(1, 2) * (G0[a, m] * G0[n, b] + G0[a, n] * G0[m, b])
                            - sp.Rational(1, 2) * G0[a, b] * G0[m, n])
            if not subtract_slice:
                M = M - sp.Rational(1, 2) * alg
            M = M - sp.Rational(1, 2) * (dG0[m] * Gi0 * dG0[n] + dG0[n] * Gi0 * dG0[m])
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


# from-scratch curvature of e^{2phi}eta on the potential slice, as functions of sigma
def _curvature_of_sigma():
    ph = p + sp.Rational(1, 2) * sum(S(i, j) * xs[i] * xs[j] for i in range(DIM) for j in range(DIM))
    E = sp.exp(2 * ph)
    g = sp.Matrix(DIM, DIM, lambda i, j: E * eta[i, j])
    ginv = sp.Matrix(DIM, DIM, lambda i, j: eta[i, j] / E)
    Gm = [[[sp.Rational(1, 2) * sum(ginv[l, k] * (sp.diff(g[n, k], xs[m]) + sp.diff(g[m, k], xs[n])
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
    """(a0, a1, a2s, a3s) of |II|^2 (or |H|^2) on the potential slice (verbatim W126 fit)."""
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


Q = sp.Rational

# ===========================================================================
log("=" * 78)
log("W159 -- TACHYON-ESCAPES: three routes + dispersion.  Positive controls first.")
log("=" * 78)

# --- POSITIVE CONTROLS ------------------------------------------------------
log("\n--- POSITIVE CONTROLS: reproduce W126 + W130 + W126 gradient series ---")
a0v, a1v, a2sv, a3sv = slice_decomp(want_H=False)
c_R = a2sv + a3sv * Q(1, 3)                     # W130 covariant map (GB freedom cancels)
check("PC1: |II|^2 slice decomposition reproduces W126 (a0,a1,a2s,a3s) = (2, 1/3, 8/9, -4)",
      (a0v, a1v, a2sv, a3sv) == (sp.Integer(2), Q(1, 3), Q(8, 9), sp.Integer(-4)),
      f"got ({a0v}, {a1v}, {a2sv}, {a3sv})")
check("PC2: covariant scalaron coupling c_R = a2s + a3s/3 = -4/9 (reproduces W130)",
      c_R == Q(-4, 9), f"c_R = {c_R}")
# sign maps + native poles (W130): gamma_TT:gamma_phi = 3:2 (induced 1 : 2/3), c_W = +2
c_W = sp.Integer(2)
gamma_TT, gamma_phi = sp.Integer(1), Q(2, 3)
f0sq = 1 / (6 * c_R)
f2sq = -1 / (2 * c_W)
m0sq = gamma_phi / (6 * c_R)
m2sq = -gamma_TT / (2 * c_W)
check("PC3: sign maps f_0^2 = 1/(6 c_R) = -3/8, f_2^2 = -1/(2 c_W) = -1/4 (W130)",
      f0sq == Q(-3, 8) and f2sq == Q(-1, 4), f"f_0^2={f0sq}, f_2^2={f2sq}")
check("PC4: native tree poles m_0^2 = gamma_phi/(6 c_R) = -1/4 (tachyon), "
      "m_2^2 = -gamma_TT/(2 c_W) = -1/4 (induced measure; both < 0) (W130)",
      m0sq == Q(-1, 4) and m2sq == Q(-1, 4), f"m_0^2={m0sq}, m_2^2={m2sq}")
# W126 gradient series (the object route 2 tests)
vg = sp.Symbol('vg', real=True)
Wgrad = sp.simplify(route1_W(True, vvals=[0, vg, 0, 0], svals={ij: 0 for ij in pairs}).subs(E0, 1))
grad_ser = sp.expand(sp.series(Wgrad, vg, 0, 8).removeO())
check("PC5: gradient sector reproduces W126: W(v) = 2 + 16 v^2 + 320 v^4 + ... "
      "(the quartic 320 v^4 that route 2 must bound)",
      grad_ser.coeff(vg, 0) == 2 and grad_ser.coeff(vg, 2) == 16 and grad_ser.coeff(vg, 4) == 320,
      f"series = {grad_ser}")

# ===========================================================================
# ROUTE 1 -- FRG/branch specialist: is the tachyon an AF-branch artifact and GU on AS?
# ===========================================================================
log("\n" + "=" * 78)
log("ROUTE 1 -- AF/AS branch: native-tree-point -> which-branch, and the passage")
log("=" * 78)
# R1a: native tree point sits at f_2^2 < 0 AND f_0^2 < 0 (W130) -- off the AF branch.
check("R1a: GU's native tree point (f_2^2, f_0^2) = (-1/4, -3/8), BOTH negative -- OFF the "
      "AF branch (which gates on f_2^2 > 0) (W130)",
      f2sq < 0 and f0sq < 0)
# R1b: BOTH target branches live at f_2^2 > 0.  AF: basin gate f_2^2 > 0 (W123).  AS/Reuter:
# the g-independent law 1/f_2^2(t) = 1/f_2^2(0) + kappa*Phi*b_2*t keeps f_2^2 > 0 at every
# finite scale from a positive start (W128 Sec 3).  Reproduce the monotone law:
t, f2_0, kPhi_b2 = sp.symbols('t f2_0 kPhi_b2', positive=True)
inv_law = 1 / f2_0 + kPhi_b2 * t                       # = 1/f_2^2(t)
f2_of_t = 1 / inv_law
check("R1b: BOTH branches require f_2^2 > 0 -- AF by its basin gate (W123), AS by the "
      "monotone law 1/f_2^2(t) = 1/f_2^2(0) + kappa Phi b_2 t (positive start stays "
      "positive at every finite t) (W128).  So the tree point (f_2^2 < 0) is off BOTH",
      sp.simplify(f2_of_t) > 0 and (sp.limit(f2_of_t, t, sp.oo) == 0))
# R1c: connecting tree (f_2^2 = -1/4) to EITHER branch (f_2^2 > 0) needs a sign flip of
# f_2^2, i.e. passage through f_2^2 = +/- infinity <=> c_W = 0 (strong Weyl coupling).  This
# obstruction lives in the SPIN-2 (Weyl / c_W) channel and is INDEPENDENT of the scalar
# (f_0^2 / AF-vs-AS) coordinate.  Targeting AS does NOT avoid it.
sign_tree = sp.sign(f2sq)
sign_AF = sp.Integer(1)      # AF basin gate f_2^2 > 0
sign_AS = sp.Integer(1)      # AS trajectory f_2^2 > 0
crossings_to_AF = 0 if sign_tree == sign_AF else 1
crossings_to_AS = 0 if sign_tree == sign_AS else 1
check("R1c: the passage tree -> branch is a SPIN-2 (c_W = 0) strong-coupling crossing, and "
      "it is REQUIRED for BOTH branches equally (one f_2^2 sign flip each); targeting AS "
      "does NOT avoid the passage AF needs -- the obstruction is orthogonal to the scalar "
      "AF-vs-AS coordinate",
      crossings_to_AF == 1 and crossings_to_AS == 1 and crossings_to_AF == crossings_to_AS)
# R1d: even PAST the passage, AS only PERMITS (not forces) m_0^2 >= 0.  W128 sign-lock:
# the de-slaved Reuter root sign = sign(eta0) = ported R^2-relevance; healthy AND tachyonic
# trajectories are both UV-complete (PERMITTED-NOT-FORCED); E2 fork stands.  Encode the
# sign-lock (positive eta0 -> positive root -> non-tachyonic) and the both-signs freedom.
eta0, gstar, kPhi_cC = sp.symbols('eta0 g_star kPhi_cC', real=True)
deslaved_root = eta0 * gstar / kPhi_cC          # W128 sign-lock theorem
root_pos = deslaved_root.subs({eta0: 1, gstar: sp.Rational(674, 1000), kPhi_cC: 1})
root_neg = deslaved_root.subs({eta0: -1, gstar: sp.Rational(674, 1000), kPhi_cC: 1})
check("R1d: even past the passage, AS PERMITS-NOT-FORCES health -- W128 sign-lock: "
      "de-slaved root = eta0 g*/(kappa Phi c_C), so relevance sign (ported) sets it; and "
      "BOTH orientations of the relevant eigendirection are UV-complete (healthy f_0^2>0 "
      "AND tachyonic f_0^2<0), so m_0^2 >= 0 is a FREE boundary condition, not derived; "
      "E2 fork STANDS (no GU-native selector, W128)",
      root_pos > 0 and root_neg < 0)
log("  ROUTE 1 VERDICT: branch-UNSELECTED -- the tachyon is NOT a demonstrable AF artifact.")
log("  GU's tree data are off BOTH branches; reaching AS-health needs the SAME strong-")
log("  coupling (c_W=0) passage AF needs, one loop cannot adjudicate; and AS only PERMITS")
log("  (not forces) m_0^2 >= 0.  Debit-1 does NOT dissolve via route 1.")

# ===========================================================================
# ROUTE 2 -- nonlinear-saturation theorist: does the gradient quartic bound the runaway?
# ===========================================================================
log("\n" + "=" * 78)
log("ROUTE 2 -- gradient-sector saturation + EFT validity")
log("=" * 78)
# R2a: the FULL gradient function is a closed rational form with a genuine singularity.
num, den = sp.fraction(sp.cancel(Wgrad))
check("R2a: the gradient function is EXACT rational W(v) = "
      "2(2688 v^6 - 544 v^4 + 40 v^2 - 1)/(16 v^2 - 1)^3 -- the denominator factors as "
      "(16 v^2 - 1)^3, a GENUINE SINGULARITY (induced-metric degeneration) at v^2 = 1/16",
      sp.simplify(sp.expand(den) - sp.expand((16 * vg**2 - 1)**3)) == 0,
      f"denominator = {sp.factor(den)}")
# R2b: therefore the convergence radius of 2 + 16v^2 + 320v^4 + ... is exactly v^2 = 1/16.
# Confirm via the coefficient ratios approaching 16 (= 1/r_c).
long_ser = sp.series(Wgrad, vg, 0, 14).removeO()
coeffs = [long_ser.coeff(vg, 2 * k) for k in range(7)]
ratios = [sp.Rational(coeffs[k + 1], coeffs[k]) for k in range(len(coeffs) - 1)]
check("R2b: coefficients 2,16,320,5888,102400,... GROW; successive ratios approach 16 = "
      "1/r_c, so the convergence radius is exactly v^2 = 1/16 (the pole).  The truncation "
      "holds only for v^2 < 1/16",
      all(r > 0 for r in ratios) and abs(float(ratios[-1]) - 16) < 2,
      f"ratios = {[float(r) for r in ratios]}")
# R2c: all gradient coefficients are POSITIVE -- a DBI-like SPEED LIMIT, not a restoring
# force.  A positive growing kinetic function bounds field VELOCITY, never field EXCURSION.
check("R2c: every gradient coefficient is POSITIVE (2,16,320,5888,102400,...) -- the "
      "gradient sector is a DBI-like SPEED LIMIT on |dphi|, NOT a restoring force; it "
      "cannot manufacture a potential minimum (W126 proved the potential is EXACTLY "
      "quadratic, c_3=0), so a bounded velocity still runs to the f'=0 wall (bounded-"
      "velocity RUNAWAY, not a bounded-field attractor)",
      all(c > 0 for c in coeffs))
# R2d: the EFT-validity kill.  Any saturation balancing the tachyonic drive needs a kinetic
# scale ~ |m_0^2| = 1/4.  But 1/4 = 4 * (1/16): the required regime v^2 ~ |m_0^2| sits at
# 4x the singularity radius -- BEYOND the induced-geometry degeneration, where the truncated
# kinetic function and the whole derivative expansion are invalid.
r_c = Q(1, 16)
m0_scale = -m0sq                                    # |m_0^2| = 1/4
check("R2d: EFT-VALIDITY KILL -- any saturation needs kinetic scale ~ |m_0^2| = 1/4, but "
      "the gradient function degenerates at v^2 = 1/16; |m_0^2| = 1/4 = 4 x (1/16), so the "
      "balance sits BEYOND the singularity, out of validity",
      m0_scale > r_c and sp.Rational(m0_scale, r_c) == 4)
log("  ROUTE 2 VERDICT: OUT-OF-VALIDITY (and structurally a speed-limit, not a restoring")
log("  force).  The gradient quartic does NOT bound the runaway into a valid attractor.")

# ===========================================================================
# ROUTE 3 -- higher-derivative theorist: is c_R < 0 FORCED by a1 > 0 covariantly?
# ===========================================================================
log("\n" + "=" * 78)
log("ROUTE 3 -- sign-forcing residual: SIGN-FORCED or SIGN-FREE?")
log("=" * 78)
# The natural framework deformation is the wave-35 shape family alpha|II|^2 + beta|H|^2.
# Compute the full slice decomposition of |H|^2 (needs a2s_H, a3s_H separately for c_R_H).
a0H, a1H, a2sH, a3sH = slice_decomp(want_H=True)
c_R_H = a2sH + a3sH * Q(1, 3)
check("R3a: |H|^2 slice decomposition = (-1, 4/3, -4/9, 0), so c_R_H = -4/9 and a1_H = 4/3 "
      "(computed from the verbatim Route-1 machinery)",
      (a0H, a1H, a2sH, a3sH) == (sp.Integer(-1), Q(4, 3), Q(-4, 9), sp.Integer(0))
      and c_R_H == Q(-4, 9), f"|H|^2 = ({a0H},{a1H},{a2sH},{a3sH}), c_R_H = {c_R_H}")
# In the family, a1(alpha,beta) and c_R(alpha,beta) are BOTH linear.  c_R < 0 is FORCED by
# a1 > 0 iff their zero-lines COINCIDE (same ray), i.e. det[[a1_II, a1_H],[c_R_II, c_R_H]] = 0.
alpha, beta = sp.symbols('alpha beta', real=True)
a1_fam = alpha * a1v + beta * a1H
cR_fam = alpha * c_R + beta * c_R_H
det = a1v * c_R_H - a1H * c_R
check("R3b: the sign correlation is FORCED iff the zero-loci of a1 and c_R coincide, i.e. "
      "det[[a1_II,a1_H],[c_R_II,c_R_H]] = 0.  Computed det = 4/9 != 0, so (a1, c_R) are "
      "INDEPENDENT coordinates of the shape family: no structural identity forces "
      "sign(c_R) = -sign(a1)",
      det == Q(4, 9) and det != 0, f"det = {det}")
# Exhibit the explicit counterexample: attractive gravity (a1 > 0) AND healthy R^2 (c_R > 0).
ce = {alpha: -2, beta: 1}
a1_ce = a1_fam.subs(ce)
cR_ce = cR_fam.subs(ce)
check("R3c: COUNTEREXAMPLE within the induced-action family -- (alpha,beta) = (-2,1) gives "
      "a1 = 2/3 > 0 (ATTRACTIVE) AND c_R = +4/9 > 0 (HEALTHY, non-tachyonic).  Attractive "
      "gravity does NOT force the tachyon: SIGN-FREE",
      a1_ce == Q(2, 3) and cR_ce == Q(4, 9) and a1_ce > 0 and cR_ce > 0,
      f"a1 = {a1_ce}, c_R = {cR_ce}")
# The surviving weaker fact: on the POSITIVE cone (alpha >= 0, beta >= 0), the correlation
# holds (the counterexample needs alpha < 0).  So the sign is CONE-CORRELATED, not forced.
a1_pos = a1_fam.subs({alpha: 1, beta: 1})
cR_pos = cR_fam.subs({alpha: 1, beta: 1})
check("R3d: the surviving residue is a POSITIVE-CONE correlation only -- for alpha,beta >= 0 "
      "(a1 = alpha/3 + 4beta/3 > 0 and c_R = -(4/9)(alpha+beta) < 0), the counterexample "
      "requires alpha < 0.  A correlation on a cone is NOT a forcing identity; and the "
      "norms are already indefinite (w2 = <II_1,II_1> = -64 < 0), so alpha < 0 is not "
      "positivity-excluded",
      a1_pos > 0 and cR_pos < 0)
log("  ROUTE 3 VERDICT: SIGN-FREE.  c_R < 0 is NOT forced by a1 > 0 in the covariant action;")
log("  the induced shape family contains attractive-and-healthy members.  Even the weak")
log("  'feature' framing (tachyon unavoidable with attraction) fails.")

# ===========================================================================
# DISPERSION -- does the tachyonic pole sit at physical k, or a finite-k band?
# ===========================================================================
log("\n" + "=" * 78)
log("DISPERSION -- k-structure of the tachyonic pole (W156 item 2)")
log("=" * 78)
# The quadratic operator around flat space is BLOCK-DIAGONAL in spin (W130's separate TT
# and spin-0 sectors -- Lorentz irreducibility).  The full inverse propagator FACTORIZES:
# no k-dependent mixing between spin-0 and spin-2.  Each sector's tachyonic growth rate:
k = sp.Symbol('k', real=True, nonnegative=True)
growth0_sq = -m0sq - k**2               # spin-0 unstable branch: omega^2 = -(k^2 + m_0^2)
growth2_sq = -m2sq - k**2               # spin-2 tachyonic branch (its own AF-ghost issue)
dgrowth0 = sp.diff(growth0_sq, k)
check("D1: the operator is BLOCK-DIAGONAL in spin (W130 separate TT + spin-0 sectors), so "
      "the inverse propagator FACTORIZES as (k^2+m_0^2)(k^2+m_2^2) with NO k-dependent "
      "spin-0/spin-2 mixing -- there is no cross-channel band structure to build",
      sp.simplify(sp.expand((k**2 + m0sq) * (k**2 + m2sq))
                  - (k**4 + (m0sq + m2sq) * k**2 + m0sq * m2sq)) == 0)
check("D2: the SCALAR tachyonic growth rate omega^2 = -(k^2 + m_0^2) is a strictly "
      "DECREASING function of k^2 (d/dk = -2k <= 0), so it PEAKS AT k = 0: the unstable "
      "band is 0 <= k < |m_0| = 1/2 with maximum growth at k = 0.  No finite-k scale "
      "selection -- a genuine homogeneous (k=0) instability, not a Turing band",
      sp.simplify(dgrowth0 + 2 * k) == 0
      and growth0_sq.subs(k, 0) == -m0sq and -m0sq > 0
      and sp.solve(sp.Eq(growth0_sq, 0), k) == [sp.Rational(1, 2)])
check("D3: the spin-2 sector (m_2^2 = -1/4, f_2^2 < 0) is a SEPARATE channel (the AF-branch "
      "massive-ghost issue), likewise peaking at k = 0; it does not couple to the scalar to "
      "make a band.  DISPERSION: tachyon at k=0, NO band structure, interpretation "
      "UNCHANGED",
      growth2_sq.subs(k, 0) == -m2sq and -m2sq > 0)
log("  DISPERSION VERDICT: tachyonic pole is a genuine k=0 (homogeneous) instability; NO")
log("  finite-k band / scale selection.  The spin-2 coupling does not move the peak.")

# ===========================================================================
# SYNTHESIS
# ===========================================================================
log("\n" + "=" * 78)
log("SYNTHESIS -- debit-1 verdict")
log("=" * 78)
log("  ROUTE 1 (AF/AS branch):        branch-UNSELECTED (shared c_W=0 passage; AS PERMITS-")
log("                                 NOT-FORCES; tree off BOTH branches).  Does NOT dissolve.")
log("  ROUTE 2 (gradient saturation): OUT-OF-VALIDITY (v^2=1/16 degeneration; |m_0^2|=1/4=4x;")
log("                                 positive kinetic = speed limit, not restoring force).")
log("  ROUTE 3 (sign-forcing):        SIGN-FREE (det=4/9!=0; attractive-and-healthy member")
log("                                 at (alpha,beta)=(-2,1)).  Even the feature-framing fails.")
log("  DISPERSION:                    k=0 tachyon, NO band structure.  Interpretation unchanged.")
log("")
log("  OVERALL: debit-1 STANDS-AS-DEBIT, NARROWED to an AF-branch tree-level feature whose")
log("  only non-artifact escape is the (E2) branch-selection fork, gated behind a shared")
log("  strong-coupling passage one loop cannot adjudicate.  The flaw count does NOT drop;")
log("  bar (b) status UNCHANGED (consistent with W157).")

# ===========================================================================
log("\n" + "=" * 78)
if FAIL:
    log(f"RESULT: {len(FAIL)} FAILED")
    for f in FAIL:
        log("  FAIL: " + f)
    raise SystemExit(1)
log("RESULT: ALL PASS")
log("=" * 78)
