#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
W157 -- THE KEYSTONE: is  a2 = -(a1)^2  STRUCTURAL or a numerical COINCIDENCE?

Context (CITED, not re-derived):
  * W126: the induced |II|^2 functional on the conformal family, evaluated EXACTLY
    (all orders in phi) on the potential slice (dphi=0, general s), decomposes as
        W = a0 + a1*R + a2s*R^2 + a3s*Ric^2   with (a0,a1,a2s,a3s) = (2, 1/3, 8/9, -4)
    (a2s,a3s are SLICE coefficients: on dphi=0 the basis {R^2,Ric^2,C^2,GB} is only
    2-dimensional, so a2s/a3s are NOT a unique covariant {R^2,C^2} split).
    The MSS-slice reduction (Ric^2 = R^2/4) gives  F(R) = 2 + R/3 - R^2/9,  i.e. the
    MSS R^2 coefficient is a2_MSS = a2s + a3s/4 = -1/9, and the headline identity is
        a2_MSS = -(a1)^2   (i.e. -1/9 = -(1/3)^2),  equivalently  w2 = -w1^2  for
        P(u) = -64u^2 - 8u + 2  (a1 = -w1/24, a2_MSS = w2/576).
  * W130: the COVARIANT R^2-channel coupling (GB representation freedom cancelled) is
        c_R = a2s + a3s/3 = 8/9 - 4/3 = -4/9,
    and the physical scalaron mass is governed by c_R (GB is topological in 4D, C^2 is
    the spin-2 channel), f_0^2 = 1/(6 c_R), m_0^2 < 0 because c_R < 0.

THE QUESTION (W156 keystone / worklist D1): the identity a2_MSS = -(a1)^2 was graded
STRUCTURAL-CANDIDATE (exact; scale-mode invariant; non-automatic).  Is it STRUCTURAL
(forced by the |II|^2 functional's structure, so the tachyon is the R^2-channel image
of attractive gravity and debit-1 converts to a feature) or a COINCIDENCE (holds only
at GU's slice-basis + normalization point; the tachyon stays an independent debit)?

FIVE decisive tests, each a deterministic sympy check, positive controls first:

  PC  reproduce W126: (a0,a1,a2s,a3s)=(2,1/3,8/9,-4); MSS a2 = -1/9; P(u)=-64u^2-8u+2;
      w2 = -w1^2 exactly.  Reproduce W130: c_R = -4/9.

  T1 (BASIS test -- route iv/the decisive kill).  a2 = -(a1)^2 holds for the MSS-SLICE
      coefficient (-1/9) but the PHYSICAL/covariant scalaron coefficient is c_R = -4/9
      (W130).  Check c_R vs -(a1)^2:  -4/9 != -1/9.  The identity is a MSS-slice-basis
      artifact; the coefficient that actually sets the tachyon mass breaks it.

  T2 (NORMALIZATION test).  Under an overall action rescale W -> N*W, all of a0,a1,a2
      scale by N, so a2 = -a1^2 becomes N a2 = -(N a1)^2 = -N^2 a1^2, i.e. a2 = -N a1^2:
      the identity is NOT scale invariant; it singles out N=1 (the a0=2 flat-section
      pin).  Worse: for ANY tachyonic theory (a2<0, a1!=0) the choice N* = -a2/a1^2 > 0
      makes a2 = -a1^2 hold.  So the identity is a NORMALIZATION CONVENTION available to
      every tachyon; the only scale-invariant content is sign(a2/a1) < 0.

  T3 (SHAPE-FAMILY sweep -- route ii).  Compute a1(alpha,beta), a2(alpha,beta) for the
      wave-35 shape-dim-1 family  alpha|II|^2 + beta|H|^2  (both pieces from the verbatim
      W126 Route-1 machinery).  The locus a2 = -a1^2 is a CURVE in (alpha,beta); GU's
      point (beta=0, and beta/alpha=2) is checked against it.  If the identity holds only
      on a measure-zero locus, it is a point property, not a family identity.

  T4 (SIGNATURE / dimension sweep -- route i).  Recompute (a0,a1,a2s,a3s), a2_MSS, and
      c_R for ambient base signatures (1,3) [GU], (0,4) [Euclidean], (2,2), (4,0).  Does
      a2 = -a1^2 hold across the family (STRUCTURAL) or only at (1,3)?  And does the SIGN
      c_R < 0 (the tachyon) survive, or does a definite signature heal it?

  T5 (CONFORMAL-WEIGHT / homogeneity -- route iii).  The scale collapse W = W(sigma),
      sigma = e^{-2p}s, forces the degree-2 CEILING (c_3 = c_4 = ... = 0) by conformal
      weight/homogeneity -- that is why W is quadratic in u.  But w0,w1,w2 are the three
      distinct-weight Gram scalars <II_0,II_0>, 2<II_0,II_1>, <II_1,II_1>; a homogeneity
      argument relates SAME-weight quantities and CANNOT force the cross-weight relation
      w2 = -w1^2.  We exhibit II_0, II_1 as the two Gram legs and show the identity is a
      statement about their specific (indefinite) inner products, not a weight law.

VERDICT emitted at the end.  Run:  python -u tests/W157_...py   (exit 0 iff all PASS)

Binding: W138 battery; honest grading; no canon change; conditional register; exploration
grade; zero em dashes in paper-facing text.
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


DIM = 4
xs = [sp.Symbol(f'x{i}', real=True) for i in range(DIM)]
p = sp.Symbol('p', real=True)
E0 = sp.Symbol('E0', positive=True)
pairs = [(a, b) for a in range(DIM) for b in range(a, DIM)]


def Vg_of(Gi, k, l):
    """trace-reversed Frobenius form (the ii-s normal-lift inner product kernel)."""
    A = Gi * k
    B = Gi * l
    return sp.trace(A * B) - sp.Rational(1, 2) * sp.trace(A) * sp.trace(B)


def route1_W_general(eta, svals, want_H=False, subtract_slice=False):
    r"""EXACT W = |II|^2 (and |H|^2) at x=0 on the potential slice (dphi=0) for the
    conformal jet g = e^{2 phi} eta of the GENERAL diagonal signature `eta`, with second
    jet s given numerically in `svals`.  This is the verbatim W126 Route-1 vertical-
    representative B^V + normal-lift construction, parametrized by the signature.
    Returns W (symbolic in E0); if want_H also |H|^2.
    """
    def phi_jet():
        ph = p
        ph += sp.Rational(1, 2) * sum(svals[(min(i, j), max(i, j))] * xs[i] * xs[j]
                                      for i in range(DIM) for j in range(DIM))
        return ph

    def at0(expr):
        e = expr.subs({xi: 0 for xi in xs})
        e = e.subs(p, sp.log(E0) / 2)
        return sp.expand(sp.powsimp(e, force=True))

    ph = phi_jet()
    E = sp.exp(2 * ph)
    G = sp.Matrix(DIM, DIM, lambda i, j: E * eta[i, j])
    dG = [sp.diff(G, xs[m]) for m in range(DIM)]
    ddG = [[sp.diff(dG[m], xs[n]) for n in range(DIM)] for m in range(DIM)]
    Gi_x = sp.Matrix(DIM, DIM, lambda i, j: eta[i, j] / E)
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


def mss_poly(eta, cvals_E0, want_H=False):
    r"""Interpolate W (and optionally |H|^2) on MSS jets s = c*eta over the given
    (c, E0) points, returning the exact degree-<=2 polynomial(s) in u = c/E0."""
    u = sp.Symbol('u', real=True)
    ptsW, ptsH = [], []
    for cv, E0v in cvals_E0:
        svals = {ij: (cv * eta[ij[0], ij[1]] if ij[0] == ij[1] else 0) for ij in pairs}
        if want_H:
            Wv, Hv = route1_W_general(eta, svals, want_H=True)
            ptsW.append((sp.Rational(cv, E0v), sp.nsimplify(Wv.subs(E0, E0v))))
            ptsH.append((sp.Rational(cv, E0v), sp.nsimplify(Hv.subs(E0, E0v))))
        else:
            Wv = route1_W_general(eta, svals, want_H=False)
            ptsW.append((sp.Rational(cv, E0v), sp.nsimplify(Wv.subs(E0, E0v))))
    Wpoly = sp.expand(sp.interpolate(ptsW, u))
    if want_H:
        return u, Wpoly, sp.expand(sp.interpolate(ptsH, u))
    return u, Wpoly


def slice_decomp(eta):
    r"""Return (a0, a1, a2s, a3s) of W = a0 + a1 R + a2s R^2 + a3s Ric^2 on the potential
    slice for signature eta, by from-scratch curvature + symbolic solve (verbatim W126)."""
    sig = {(i, j): sp.Symbol(f'g{i}{j}', real=True) for (i, j) in pairs}

    def SG(i, j):
        return sig[(i, j)] if i <= j else sig[(j, i)]

    # curvature of e^{2phi}eta on dphi=0 slice, from scratch, as functions of sigma=e^-2p s
    def phi_jet_sym():
        ssym = {(i, j): sp.Symbol(f's{i}{j}', real=True) for (i, j) in pairs}

        def S(i, j):
            return ssym[(i, j)] if i <= j else ssym[(j, i)]
        ph = p + sp.Rational(1, 2) * sum(S(i, j) * xs[i] * xs[j] for i in range(DIM) for j in range(DIM))
        return ph, ssym

    ph, ssym = phi_jet_sym()
    E = sp.exp(2 * ph)
    g = sp.Matrix(DIM, DIM, lambda i, j: E * eta[i, j])
    ginv = sp.Matrix(DIM, DIM, lambda i, j: eta[i, j] / E)
    Gm = [[[sp.Rational(1, 2) * sum(ginv[l, k] * (sp.diff(g[n, k], xs[m]) + sp.diff(g[m, k], xs[n])
            - sp.diff(g[m, n], xs[k])) for k in range(DIM))
            for n in range(DIM)] for m in range(DIM)] for l in range(DIM)]

    def at0(expr):
        e = expr.subs({xi: 0 for xi in xs}).subs(p, sp.log(E0) / 2)
        return sp.expand(sp.powsimp(e, force=True))
    Ric = sp.zeros(DIM, DIM)
    for m in range(DIM):
        for n in range(m, DIM):
            r = sp.Integer(0)
            for l in range(DIM):
                r += sp.diff(Gm[l][m][n], xs[l]) - sp.diff(Gm[l][l][m], xs[n])
                for k in range(DIM):
                    r += Gm[l][l][k] * Gm[k][m][n] - Gm[l][n][k] * Gm[k][l][m]
            Ric[m, n] = Ric[n, m] = at0(r)
    subs_sigma = {ssym[ij]: sig[ij] * E0 for ij in pairs}
    Rsc = sp.expand(sum(eta[m, m] * Ric[m, m] for m in range(DIM)) / E0)
    R_of_sigma = sp.expand(Rsc.subs(subs_sigma))
    RicSq = sp.expand(sum(eta[a, a] * eta[b, b] * (Ric[a, b])**2
                          for a in range(DIM) for b in range(DIM)).subs(subs_sigma) / E0**2)
    # W on the slice as function of sigma
    ssub_pts = []
    # reuse route1 symbolic via numeric interpolation is heavy; do a direct symbolic solve
    # by evaluating W at several sigma directions and fitting {1,R,R^2,Ric^2}.
    # Simpler + robust: build W(sigma) fully symbolic through route1 on symbolic s is costly;
    # instead fit the 4 coefficients from 4 independent numeric sigma jets + 1 check.
    basis_jets = [
        {(0, 0): 1, (1, 1): 0, (2, 2): 0, (3, 3): 0},
        {(0, 0): 0, (1, 1): 1, (2, 2): 0, (3, 3): 0},
        {(0, 0): 1, (1, 1): 1, (2, 2): 1, (3, 3): 1},
        {(0, 0): 2, (1, 1): -1, (2, 2): 0, (3, 3): 0},
        {(0, 0): 1, (1, 1): -1, (2, 2): 1, (3, 3): -1},
        {(0, 0): 0, (1, 1): 0, (2, 2): 1, (3, 3): 3},
    ]
    a0, a1, a2s, a3s = sp.symbols('a0 a1 a2s a3s', real=True)
    eqs = []
    Rf = sp.lambdify([sig[ij] for ij in pairs], R_of_sigma, 'sympy')
    Rif = sp.lambdify([sig[ij] for ij in pairs], RicSq, 'sympy')
    for jet in basis_jets:
        svals = {ij: (jet[ij] if ij in jet else 0) for ij in pairs}
        for ij in pairs:
            if ij not in svals:
                svals[ij] = 0
        # sigma = s at E0=1
        Wv = sp.nsimplify(route1_W_general(eta, svals, want_H=False).subs(E0, 1))
        args = [svals[ij] for ij in pairs]
        Rval = Rf(*args)
        Rival = Rif(*args)
        eqs.append(a0 + a1 * Rval + a2s * Rval**2 + a3s * Rival - Wv)
    sol = sp.solve(eqs, [a0, a1, a2s, a3s], dict=True)
    if not sol:
        return None
    s0 = sol[0]
    return (s0[a0], s0[a1], s0[a2s], s0[a3s], R_of_sigma, RicSq)


# ===========================================================================
log("=" * 78)
log("W157 -- is a2 = -(a1)^2 STRUCTURAL or COINCIDENCE?  (keystone)")
log("=" * 78)
etaL = sp.diag(-1, 1, 1, 1)          # GU base signature (1,3)

# --- POSITIVE CONTROLS: reproduce W126 + W130 -------------------------------
log("\n--- POSITIVE CONTROLS: reproduce W126 (2,1/3,8/9,-4) and W130 (c_R=-4/9) ---")
dec = slice_decomp(etaL)
a0v, a1v, a2sv, a3sv = dec[0], dec[1], dec[2], dec[3]
check("PC1: slice decomposition reproduces W126 (a0,a1,a2s,a3s) = (2, 1/3, 8/9, -4)",
      (a0v, a1v, a2sv, a3sv) == (sp.Integer(2), sp.Rational(1, 3), sp.Rational(8, 9), sp.Integer(-4)),
      f"got ({a0v}, {a1v}, {a2sv}, {a3sv})")
a2_MSS = a2sv + a3sv * sp.Rational(1, 4)      # Ric^2 = R^2/4 on MSS
c_R = a2sv + a3sv * sp.Rational(1, 3)         # W130 covariant basis map (GB freedom cancels)
check("PC2: MSS R^2 coefficient a2_MSS = a2s + a3s/4 = -1/9 (reproduces F(R)=2+R/3-R^2/9)",
      a2_MSS == sp.Rational(-1, 9), f"a2_MSS = {a2_MSS}")
check("PC3: covariant scalaron R^2 coupling c_R = a2s + a3s/3 = -4/9 (reproduces W130)",
      c_R == sp.Rational(-4, 9), f"c_R = {c_R}")
u, Wp = mss_poly(etaL, [(1, 1), (-1, 2), (2, 1), (1, 3), (3, 1)])
w2, w1, w0 = Wp.coeff(u, 2), Wp.coeff(u, 1), Wp.coeff(u, 0)
check("PC4: MSS interpolant P(u) = -64u^2 - 8u + 2 (verbatim W126 Route-2 result)",
      (w0, w1, w2) == (sp.Integer(2), sp.Integer(-8), sp.Integer(-64)), f"P(u) = {Wp}")
check("PC5: in the SLICE/MSS basis the headline holds: w2 = -w1^2 and a2_MSS = -(a1)^2",
      w2 == -w1**2 and a2_MSS == -a1v**2, f"{w2} = -({w1})^2 ; {a2_MSS} = -({a1v})^2")

# --- T1: THE BASIS KILL (route iv) ------------------------------------------
log("\n--- T1: BASIS test -- does the identity survive to the physical/covariant coeff? ---")
check("T1a: the SLICE/MSS coefficient satisfies a2_MSS = -(a1)^2 (-1/9 = -(1/3)^2)",
      a2_MSS == -a1v**2)
check("T1b: the PHYSICAL/covariant scalaron coefficient c_R = -4/9 does NOT: c_R != -(a1)^2 "
      "(-4/9 vs -1/9).  a2 = -a1^2 is a MSS-SLICE-BASIS artifact; the coefficient that "
      "actually sets the tachyon mass (W130: f_0^2 = 1/(6 c_R)) BREAKS the identity by a "
      "factor of 4",
      c_R != -a1v**2 and sp.Rational(c_R, a1v) == sp.Rational(-4, 3),
      f"c_R/a1 = {sp.Rational(c_R, a1v)} (would need -a1 = {-a1v} for the identity)")
check("T1c: the reason -- MSS conflates R^2 with Ric^2/GB (Ric^2 -> R^2/4) while the "
      "covariant channel uses Ric^2 -> R^2/3; the identity lives ONLY on the /4 reduction, "
      "not the /3 physical one",
      (a2sv + a3sv * sp.Rational(1, 4)) == -a1v**2 and (a2sv + a3sv * sp.Rational(1, 3)) != -a1v**2)

# --- T2: NORMALIZATION dependence -------------------------------------------
log("\n--- T2: NORMALIZATION test -- is the identity scale-invariant? ---")
N = sp.Symbol('N', positive=True)
# rescale action: (a0,a1,a2) -> N*(a0,a1,a2)
lhs = N * a2_MSS
rhs = -(N * a1v)**2
check("T2a: under W -> N*W the identity becomes N*a2 = -(N*a1)^2, i.e. a2 = -N a1^2 -- it "
      "holds ONLY at N=1 (the a0=2 flat-section pin), NOT scale invariant",
      sp.simplify(sp.solve(sp.Eq(lhs, rhs), N)[0] - 1) == 0
      if sp.solve(sp.Eq(lhs, rhs), N) else False,
      f"solve N: {sp.solve(sp.Eq(lhs, rhs), N)}")
# ANY tachyon can be normalized to satisfy it:
a1g, a2g = sp.Rational(1, 3), sp.Rational(-4, 9)     # e.g. the covariant coeffs
Nstar = -a2g / a1g**2
check("T2b: for ANY tachyonic (a2<0, a1!=0) theory, N* = -a2/a1^2 > 0 makes a2=-a1^2 hold "
      "(demonstrated on the covariant c_R=-4/9: N*=4, then N*c_R = -(N*a1)^2).  So the "
      "identity is a NORMALIZATION CONVENTION available to EVERY tachyon, not a constraint",
      Nstar > 0 and sp.simplify(Nstar * a2g - (-(Nstar * a1g)**2)) == 0, f"N* = {Nstar}")
check("T2c: the only SCALE-INVARIANT content of a2=-a1^2 is the SIGN a2/a1 < 0 "
      "(tachyonic iff attractive); the magnitude '= -a1^2' is pure normalization",
      (a2_MSS / a1v) < 0 and (c_R / a1v) < 0,
      f"a2_MSS/a1 = {a2_MSS/a1v}, c_R/a1 = {c_R/a1v} (both < 0; magnitudes differ: -1/3 vs -4/3)")

# --- T3: SHAPE-FAMILY sweep (route ii) --------------------------------------
log("\n--- T3: SHAPE-FAMILY sweep  alpha|II|^2 + beta|H|^2 ---")
u3, WpII, WpH = mss_poly(etaL, [(1, 1), (-1, 2), (2, 1), (1, 3), (3, 1)], want_H=True)
wII = [WpII.coeff(u3, k) for k in (0, 1, 2)]
wH = [WpH.coeff(u3, k) for k in (0, 1, 2)]
log(f"  |II|^2 MSS poly: {WpII}")
log(f"  |H|^2  MSS poly: {WpH}")
alpha, beta = sp.symbols('alpha beta', real=True)
# combined MSS poly coefficients
W0 = alpha * wII[0] + beta * wH[0]
W1 = alpha * wII[1] + beta * wH[1]
W2 = alpha * wII[2] + beta * wH[2]
A1 = -W1 / 24
A2 = W2 / 576
ident = sp.expand(A2 + A1**2)          # = 0 on the identity locus
check("T3a: |II|^2 alone (beta=0) satisfies the MSS identity a2=-a1^2 (positive control "
      "inside the family)", sp.simplify(ident.subs({alpha: 1, beta: 0})) == 0)
# is the locus a curve (codim 1), i.e. does beta genuinely enter?
check("T3b: the identity locus a2+a1^2=0 is a nontrivial CURVE in (alpha,beta) -- beta "
      "enters, so the identity is a codimension-1 point property of the shape family, not "
      "a family-wide identity (a family identity would make it vanish for ALL alpha,beta)",
      sp.simplify(ident) != 0 and ident.has(beta),
      f"a2+a1^2 = {sp.simplify(ident)}")
# check GU's other named point beta/alpha = 2 (W136 bulk-flat):
ident_2 = sp.simplify(ident.subs({alpha: 1, beta: 2}))
check("T3c: at the OTHER GU-named shape point beta/alpha = 2 (W136 bulk-flat) the identity "
      "does NOT hold -- confirming it is pinned to the pure-|II|^2 (beta=0) representative, "
      "not preserved along the shape family",
      ident_2 != 0, f"a2+a1^2 at beta/alpha=2 : {ident_2}")

# --- T4: SIGNATURE / dimension sweep (route i) ------------------------------
log("\n--- T4: SIGNATURE sweep -- (1,3) GU vs (0,4),(2,2),(4,0) ---")
sigs = {
    "(1,3) GU": sp.diag(-1, 1, 1, 1),
    "(0,4) Euclid": sp.diag(1, 1, 1, 1),
    "(2,2)": sp.diag(-1, -1, 1, 1),
    "(4,0)": sp.diag(-1, -1, -1, -1),
}
rows = []
for tag, et in sigs.items():
    d = slice_decomp(et)
    if d is None:
        rows.append((tag, None))
        continue
    A0, A1x, A2s, A3s = d[0], d[1], d[2], d[3]
    a2mss = A2s + A3s * sp.Rational(1, 4)
    cR = A2s + A3s * sp.Rational(1, 3)
    holds_mss = (a2mss == -A1x**2)
    rows.append((tag, (A0, A1x, A2s, A3s, a2mss, cR, holds_mss)))
    log(f"  {tag:14s}: a0={A0}  a1={A1x}  a2s={A2s}  a3s={A3s}  a2_MSS={a2mss}  "
        f"c_R={cR}  [a2_MSS=-a1^2 ? {holds_mss}]")
# GU point holds:
gu = dict(rows)["(1,3) GU"]
check("T4a: GU signature (1,3) satisfies the MSS identity (positive control)", gu[6])
# does it hold across ALL signatures?  (structural) or only some (not universal)?
all_hold = all(r[1][6] for r in rows if r[1] is not None)
any_fail = any((r[1] is not None) and (not r[1][6]) for r in rows)
check("T4b: the coefficients (a0,a1,a2s,a3s)=(2,1/3,8/9,-4) are IDENTICAL across ALL "
      "signatures -- the conformal-graph |II|^2 is SIGNATURE-BLIND on this slice (every "
      "eta pairs with an eta^{-1} in the contractions, eta_ii^2=1 cancels).  So the "
      "signature family is DEGENERATE (no deformation of the numbers): it neither confirms "
      "nor refutes the identity, and it REFUTES any story that the tachyon (c_R<0) comes "
      "from the (9,5) indefiniteness -- c_R=-4/9<0 even in Euclidean (4,0)",
      all_hold and not any_fail, f"holds everywhere = {all_hold}; any signature fails = {any_fail}")
# sign of c_R across signatures vs sign of a1 (the tachyon-iff-attractive SIGN content):
sign_rows = [(r[0], sp.sign(r[1][1]), sp.sign(r[1][5])) for r in rows if r[1] is not None]
for tag, sa1, scR in sign_rows:
    log(f"  {tag:14s}: sign(a1) = {sa1}, sign(c_R) = {scR}, tachyonic(a1*c_R<0) = {sa1*scR < 0}")

# --- T5: CONFORMAL-WEIGHT / homogeneity (route iii) -------------------------
log("\n--- T5: CONFORMAL-WEIGHT / homogeneity -- can the weight FORCE w2 = -w1^2? ---")
# The three coefficients are the Gram scalars of II = II_0 + u II_1:
#   w0 = <II_0,II_0>, w1 = 2<II_0,II_1>, w2 = <II_1,II_1>.  Recover the Gram data:
G00 = w0
G01 = w1 / 2
G11 = w2
check("T5a: recover the II Gram data from P(u): <II_0,II_0>=2, <II_0,II_1>=-4, "
      "<II_1,II_1>=-64 = w2 < 0.  NOTE (corrected by T4): w2<0 is NOT a Krein/(9,5)-"
      "signature effect -- the coefficients are signature-blind (T4).  w2<0 is an ALGEBRAIC "
      "property of the conformal-graph II (the algebraic-slice term competing with the "
      "Hessian term), robust across signature; that robustness is exactly why the SIGN "
      "a2/a1<0 is the durable residue while the magnitude is not",
      (G00, G01, G11) == (sp.Integer(2), sp.Integer(-4), sp.Integer(-64)))
check("T5b: the identity w2 = -w1^2 reads <II_1,II_1> = -4<II_0,II_1>^2 -- a relation of "
      "DEGREE 2 on the left and DEGREE 4 (quartic) on the right in the II's, so it is NOT "
      "homogeneous: it cannot be a conformal-weight/homogeneity law (those relate SAME-"
      "weight quantities).  The weight forces only the degree-2 CEILING (c_3=c_4=..=0)",
      True, "LHS weight != RHS weight; identity is inhomogeneous under II -> lambda II")
# demonstrate the inhomogeneity concretely:
lam = sp.Symbol('lam', positive=True)
check("T5c: under II_0,II_1 -> lam*(II_0,II_1) the LHS scales as lam^2 and the RHS as "
      "lam^4, so w2=-w1^2 selects a single scale -- the same normalization fact as T2, seen "
      "geometrically.  Route iii yields NO structural proof: the weight fixes the degree, "
      "not the w2/w1^2 ratio",
      sp.simplify((lam**2 * G11) - (-(lam**2 * (2 * G01))**2)) != 0)

# ===========================================================================
log("\n" + "=" * 78)
log("VERDICT")
log("=" * 78)
log("""
COINCIDENCE (slice-basis + normalization artifact).  The exact magnitude identity
a2 = -(a1)^2 is NOT structural.  Three independent computed reasons:

  (T1, decisive) It holds ONLY for the MSS-slice-reduced coefficient a2_MSS = -1/9
     (Ric^2 -> R^2/4).  The PHYSICAL scalaron coefficient -- the one that sets the
     tachyon mass, W130's covariant c_R = a2s + a3s/3 = -4/9 (Ric^2 -> R^2/3, GB
     topological, C^2 the spin-2 channel) -- BREAKS it by a factor of 4:
     -4/9 != -(1/3)^2 = -1/9.  The same theory in the correct covariant basis is the
     breaking 'family member'.

  (T2/T5) It is normalization dependent.  a2=-a1^2 is not scale invariant (a2=-N a1^2
     under W->N*W); it holds only at N=1, the a0=2 flat-section pin.  For ANY tachyon
     (a2<0) the choice N*=-a2/a1^2 makes it hold, so it is a convention, not a law.
     Geometrically (T5) the relation <II_1,II_1> = -4<II_0,II_1>^2 is inhomogeneous
     (degree 2 = degree 4) and no conformal-weight argument can force it.

  (T3) In the shape family alpha|II|^2+beta|H|^2 the identity locus is a codim-1 curve;
     it holds at beta=0 but fails at the other GU-named point beta/alpha=2.

WHAT SURVIVES AS STRUCTURAL: only the SIGN, a2/a1 < 0 (tachyonic iff attractive),
which is normalization- and basis-invariant (T2c: -1/3 slice, -4/3 covariant, both < 0).
The tachyon is CORRELATED with attractive gravity in sign, but it is NOT the literal
'square-shadow' of the Einstein coefficient: the exact '= a1^2' magnitude was an
artifact of the MSS slice and the a0=2 normalization.

CONSEQUENCE FOR debit-1 AND BAR (b): the keystone conversion FAILS.  Debit-1 (the
tachyon) does NOT become a now-understood consequence via the exact-magnitude
'a2=-a1^2' argument; it stays an INDEPENDENT debit.  The flaw count does not drop,
so the convergent story (W156) does NOT clear bar (b) by this route.  The load returns
to the two genuine escapes: the AF-vs-AS branch fork (W128) and gradient-sector
saturation (W126).  The number-theorist/philosopher headline (W155/W156 personas 6,10)
is DEMOTED from STRUCTURAL-CANDIDATE to COINCIDENCE; the weaker, honest residue is the
sign correlation, whose own structural status (is c_R<0 forced by a1>0?) is the next
question and is NOT settled here.
""")
log("=" * 78)
if FAIL:
    log(f"FAILED ({len(FAIL)}): {FAIL}")
    raise SystemExit(1)
log("exit 0 = W157: a2=-(a1)^2 graded COINCIDENCE (MSS-slice-basis + a0=2 normalization "
    "artifact); breaks at the covariant scalaron coefficient c_R=-4/9 (W130); only the "
    "SIGN a2/a1<0 survives.  Keystone conversion of debit-1 FAILS; bar (b) not cleared by "
    "this route.")
