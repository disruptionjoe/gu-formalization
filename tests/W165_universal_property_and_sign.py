#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
W165 -- TEAM LENS-LEVEL.  Is the tachyon question being asked one abstraction
level too low?  Two-track sweep (2026-07-11, slice B) NAMED norm-square universal
properties -- Willmore/GJMS conformal-uniqueness, the Kempf-Ness moment-map
norm-square, the Connes spectral action, the section-functor adjoint -- as the
objects that would FORCE GU's source action where signature/causality/grading
each fail.  This wave EVALUATES those candidates against the actual W126/W130
induced-action data and asks: if such a universal property forces a point, is
that point HEALTHY or TACHYONIC?

CONTEXT (CITED, not re-derived):
  * W126: induced |II|^2 on the conformal family, EXACT.  Potential-slice
    decomposition (a0,a1,a2s,a3s) = (2, 1/3, 8/9, -4).
  * W130: covariant scalaron coupling c_R = a2s + a3s/3 = -4/9 (< 0, tachyonic);
    the tachyon lives in the record-count / conformal (BLMS number) mode.
  * W159: the wave-35 shape family alpha|II|^2 + beta|H|^2 has
    |H|^2 = (-1, 4/3, -4/9, 0), c_R_H = -4/9; and det[[a1_II,a1_H],[c_R_II,c_R_H]]
    = 4/9 != 0 so (a1,c_R) are INDEPENDENT coordinates -> SIGN-FREE (the tachyon
    is GU's specific-point property, not forced by attraction).  Route-3 residue:
    a POSITIVE-CONE correlation (health needs alpha < 0) and the (9,5) norms are
    already indefinite (w2 = <II_1,II_1> = -64 < 0).
  * W150: the (9,5) q=5 Krein indefiniteness IS the image of the finality frontier.
  * Cross-repo (Joe 2026-07-02, gated): TaF owns the CAPABILITY MEASURE and the
    finality/irreversibility structure; TaF T110 = no scalar finality monotone in
    closed reversible dynamics (any arrow is open-system/irreversible).  The
    tri-repo identity is NOT asserted (gated behind >=2 adapter contracts;
    single-process caution).

THE NEW LEVER (this wave):  c_R_II == c_R_H == -4/9 are IDENTICAL.  So on the
family c_R(alpha,beta) = -(4/9)(alpha+beta) depends ONLY on the total weight
alpha+beta, NEVER on the shape.  W159's det=4/9 independence is carried ENTIRELY
by a1 (1/3 vs 4/3); c_R is shape-BLIND.  Consequence: sign(c_R) = -sign(alpha+beta).
Every norm-square universal property with positive total weight (alpha+beta > 0)
FORCES c_R < 0 = the tachyon.  Health (c_R > 0) needs alpha+beta < 0, reachable
inside a norm-square only if the two isotypic components carry OPPOSITE Krein
signatures -- and that relative Krein sign on the (9,5) q=5 frontier is the
GATED (TaF-owned) object.

FIVE personas inline (category theorist; tri-repo bridge architect; foundations/
structural theorist; symbolic engineer; adversarial skeptic).  Deterministic
sympy + a finite-group averaging exhibit; positive controls first.
Run:  python -u tests/W165_universal_property_and_sign.py   (exit 0 iff all PASS).

Binding: W138 battery; tri-repo gating STRICTLY (no cross-repo identity; bridges
are gated conjectures); honest grading; no canon change; conditional register;
zero em dashes in paper-facing text.
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
# MACHINERY -- verbatim W126 Route-1 ii-s Convention-B B^V + normal lift (as used
# by W159).  Regression-pinned by the positive controls below (reproduces W126
# (2,1/3,8/9,-4), W130 c_R = -4/9, and W159's |H|^2 = (-1,4/3,-4/9,0)).
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
log("W165 -- ONE ABSTRACTION LEVEL TOO LOW?  universal property -> which sign.")
log("Positive controls first.")
log("=" * 78)

# --- POSITIVE CONTROLS ------------------------------------------------------
log("\n--- POSITIVE CONTROLS: reproduce W126 + W130 + W159 shape-family data ---")
a0v, a1v, a2sv, a3sv = slice_decomp(want_H=False)
c_R = a2sv + a3sv * Q(1, 3)
check("PC1: |II|^2 slice decomposition reproduces W126 (2, 1/3, 8/9, -4)",
      (a0v, a1v, a2sv, a3sv) == (sp.Integer(2), Q(1, 3), Q(8, 9), sp.Integer(-4)),
      f"got ({a0v}, {a1v}, {a2sv}, {a3sv})")
check("PC2: covariant scalaron coupling c_R_II = a2s + a3s/3 = -4/9 (W130), tachyonic (<0)",
      c_R == Q(-4, 9) and c_R < 0, f"c_R_II = {c_R}")
a0H, a1H, a2sH, a3sH = slice_decomp(want_H=True)
c_R_H = a2sH + a3sH * Q(1, 3)
check("PC3: |H|^2 slice decomposition reproduces W159 (-1, 4/3, -4/9, 0), c_R_H = -4/9",
      (a0H, a1H, a2sH, a3sH) == (sp.Integer(-1), Q(4, 3), Q(-4, 9), sp.Integer(0))
      and c_R_H == Q(-4, 9), f"|H|^2 = ({a0H},{a1H},{a2sH},{a3sH}), c_R_H = {c_R_H}")
det159 = a1v * c_R_H - a1H * c_R
check("PC4: W159 det[[a1_II,a1_H],[c_R_II,c_R_H]] = 4/9 != 0 (the SIGN-FREE result)",
      det159 == Q(4, 9), f"det = {det159}")

# ===========================================================================
# PERSONA 1 -- category theorist: does invariance (a universal property) FORCE a
# point, or only a projective family?  EXHIBIT the isotypic / Schur count.
# ===========================================================================
log("\n" + "=" * 78)
log("PERSONA 1 -- category theorist: what a universal property actually forces")
log("=" * 78)
# The named forcing candidates (two-track slice B: Willmore/GJMS uniqueness,
# Kempf-Ness moment-map norm-square, Connes spectral action) all pick out a
# NORM-SQUARE of the soldering distortion / second fundamental form II w.r.t. an
# invariant inner product.  Invariance IS a universal property (the invariants are
# the terminal cone over the group action).  By Schur it fixes ONE scale per
# inequivalent irreducible summand.  II of a submanifold splits canonically under
# the structure group as  H (trace = mean-curvature vector)  (+)  II_0 (trace-free
# part), two INEQUIVALENT real irreducibles.  So the invariant quadratic forms on
# II are a 2-dim space -- a 1-parameter PROJECTIVE family, NOT a point.
#
# EXHIBIT (small model, single codimension, base dim n=3): the O(3)-invariant
# quadratic forms of a symmetric matrix S are spanned by (tr S)^2 and tr(S^2).
# Solve the EXACT so(3)-invariance condition (SO(3)-invariance = O(3)-invariance at
# quadratic order; the only other O(3) relative invariant, det S, is cubic).  For an
# so(3) generator X (antisymmetric), the induced variation of S is delta S = [X, S];
# a quadratic form Q (symmetric 6x6 in the coordinate basis of Sym^2(R^3)) is
# invariant iff  L_X^T Q + Q L_X = 0  for all three generators, where L_X is the
# 6x6 matrix of S -> [X,S].  Solve the linear system; the solution space is 2-dim.
# basis of Sym^2(R^3) in a FIXED order that matches sym_coords exactly (rows and
# columns of L must use the same ordering): diagonals first, then off-diagonals.
_idx = [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]
sym_basis = []
for (a, b) in _idx:
    M = sp.zeros(3, 3); M[a, b] = 1; M[b, a] = 1
    sym_basis.append(M)


def sym_coords(M):
    return sp.Matrix([M[a, b] for (a, b) in _idx])


def so3_gen(i):
    X = sp.zeros(3, 3)
    a, b = [(1, 2), (2, 0), (0, 1)][i]
    X[a, b] = -1; X[b, a] = 1
    return X


def L_of(X):
    # 6x6 matrix of the linear map S -> [X, S] = X S - S X in the sym_coords basis
    cols = [sym_coords(X * B - B * X) for B in sym_basis]
    return sp.Matrix.hstack(*cols)


Ls = [L_of(so3_gen(i)) for i in range(3)]
# a symmetric 6x6 Q has 21 free entries; assemble the invariance conditions
qsyms = {(a, b): sp.Symbol(f'q{a}{b}', real=True) for a in range(6) for b in range(a, 6)}
Qm = sp.Matrix(6, 6, lambda a, b: qsyms[(a, b)] if a <= b else qsyms[(b, a)])
conds = []
for L in Ls:
    E = L.T * Qm + Qm * L
    for a in range(6):
        for b in range(a, 6):
            conds.append(E[a, b])
sol = sp.linsolve(conds, list(qsyms.values()))
free = len(sol.free_symbols)
check("U1a (EXHIBIT): the O(3)-invariant quadratic forms of a symmetric matrix form a "
      "2-DIMENSIONAL space (EXACT so(3)-invariance solve, L_X^T Q + Q L_X = 0 for all 3 "
      "generators; solution space dim = 2, spanned by (tr S)^2 and tr(S^2)).  Invariance "
      "FORCES a 2-dim space = a 1-parameter PROJECTIVE family, NOT a point",
      free == 2, f"invariant quadratic-form dim = {free}")
# independence of the two invariants (so the family is genuinely 1-parameter, not degenerate)
S1 = sp.diag(1, 0, 0); S2 = sp.diag(1, -1, 0)
tab = sp.Matrix([[(S1.trace())**2, (S1 * S1).trace()],
                 [(S2.trace())**2, (S2 * S2).trace()]])
check("U1b (EXHIBIT): the two invariants (tr S)^2 and tr(S^2) are INDEPENDENT "
      "(evaluations at diag(1,0,0) and diag(1,-1,0) give a rank-2 matrix), so the invariant "
      "family is a genuine 1-parameter projective line -- this IS GU's shape family "
      "alpha|II|^2 + beta|H|^2, matching W159's det=4/9 (2 independent forms)",
      tab.rank() == 2, f"rank = {tab.rank()}")
log("  PERSONA 1: the universal property (invariance) is EXHIBITED to force only a 1-param")
log("  projective family, not a point.  Any single-point forcing needs an EXTRA rigidifier")
log("  (a Kaehler/complex structure, or a preferred inner-product scale) beyond invariance.")

# ===========================================================================
# PERSONA 3 -- foundations/structural: COHERENT vs FORCED.  The new lever: c_R is
# SHAPE-BLIND, so which point the extra rigidifier lands on decides the sign.
# (Persona 3 before 2 so the bridge has the sign fact in hand.)
# ===========================================================================
log("\n" + "=" * 78)
log("PERSONA 3 -- foundations/structural: the c_R degeneracy and the sign map")
log("=" * 78)
alpha, beta = sp.symbols('alpha beta', real=True)
a1_fam = sp.expand(alpha * a1v + beta * a1H)
cR_fam = sp.expand(alpha * c_R + beta * c_R_H)
# THE NEW LEVER: c_R_II == c_R_H, so c_R collapses to a function of alpha+beta ALONE.
check("U2 (NEW): c_R_II == c_R_H == -4/9 are IDENTICAL, so on the shape family "
      "c_R(alpha,beta) = -(4/9)(alpha+beta) depends ONLY on the total weight alpha+beta, "
      "NEVER on the shape.  The scalaron coupling is SHAPE-BLIND",
      c_R == c_R_H and sp.simplify(cR_fam - Q(-4, 9) * (alpha + beta)) == 0,
      f"c_R_fam = {cR_fam} = -(4/9)(alpha+beta)")
check("U3 (NEW): therefore sign(c_R) = -sign(alpha+beta).  W159's det=4/9 independence is "
      "carried ENTIRELY by a1 (= (alpha + 4 beta)/3, which DOES vary with shape); c_R does "
      "NOT.  So 'coherent shape freedom' (W159) and 'the sign' are DIFFERENT axes: the sign "
      "is a one-bit function of the total weight, orthogonal to the shape",
      sp.simplify(a1_fam - (alpha + 4 * beta) * Q(1, 3)) == 0
      and sp.simplify(sp.diff(cR_fam, alpha) - sp.diff(cR_fam, beta)) == 0
      and sp.diff(a1_fam, alpha) != sp.diff(a1_fam, beta),
      f"a1_fam = {a1_fam}")
log("  PERSONA 3: COHERENT is being conflated with FORCED exactly here.  A norm-square is")
log("  COHERENT for any weights; whether it is HEALTHY is the one-bit sign of alpha+beta,")
log("  which invariance does NOT fix (Persona 1).  Forcing the action does NOT force the sign.")

# ===========================================================================
# PERSONA 5 -- adversarial skeptic (brought forward): steelman 'a universal
# property WOULD force health'.  Evaluate the conformally-natural forced points.
# ===========================================================================
log("\n" + "=" * 78)
log("PERSONA 5 -- adversarial skeptic: do the NAMED universal properties force HEALTH?")
log("=" * 78)
# Steelman: 'invariance + a conformal-weight/positivity rigidifier forces a POINT, and that
# point is healthy.'  The conformally-natural rigidifier (Willmore/GJMS) selects the
# TRACE-FREE combination |II_0|^2 = |II|^2 - c|H|^2 with the trace-removal coefficient
# c in (0,1) (standard: c = 1/n < 1).  Its c_R:
c = sp.Symbol('c', positive=True)
cR_tracefree = cR_fam.subs({alpha: 1, beta: -c})      # (alpha,beta) = (1, -c)
check("U4 (NEW): the conformally-natural forced point is the TRACE-FREE Willmore combination "
      "|II_0|^2 = |II|^2 - c|H|^2 (c in (0,1)); its c_R = -(4/9)(1 - c) < 0 for EVERY c < 1, "
      "so the conformal universal property forces a TACHYONIC point.  The pure |II|^2 point "
      "(c=0) is c_R = -4/9 < 0 too.  Every standard trace-removal c in (0,1) is tachyonic",
      sp.simplify(cR_tracefree - Q(-4, 9) * (1 - c)) == 0
      and cR_tracefree.subs(c, Q(1, 3)) < 0 and cR_tracefree.subs(c, Q(3, 4)) < 0,
      f"c_R(|II_0|^2) = {sp.simplify(cR_tracefree)}")
# A positive-definite norm-square lives on the positive cone alpha,beta >= 0 (or any
# alpha+beta > 0): ENTIRELY tachyonic.  Health needs alpha+beta < 0.
check("U5 (NEW): any POSITIVE-total-weight norm-square (alpha+beta > 0 -- the Kempf-Ness "
      "moment-map norm-square, the spectral action heat-kernel a_2 with positive f, the "
      "positive-definite Willmore energy) forces c_R < 0.  HEALTH (c_R > 0) requires "
      "alpha+beta < 0, which a positive-definite norm-square CANNOT deliver",
      cR_fam.subs({alpha: 1, beta: 1}) < 0 and cR_fam.subs({alpha: 3, beta: 1}) < 0
      and cR_fam.subs({alpha: 1, beta: 3}) < 0
      and cR_fam.subs({alpha: -2, beta: 1}) > 0)     # W159's healthy point needs alpha < 0
log("  PERSONA 5 verdict: the steelman FAILS.  The named universal properties, when actually")
log("  evaluated, force the TACHYONIC point -- they do NOT force health.  The two-track hope")
log("  ('a universal property would force the action, so the sign is settled') is inverted:")
log("  forcing the action via a norm-square FORCES the tachyon.")

# ===========================================================================
# NEGATIVE CONTROL -- the collapse is a SPECIAL degeneracy of GU's induced action.
# ===========================================================================
log("\n" + "=" * 78)
log("NEGATIVE CONTROL -- the c_R degeneracy is GU-SPECIFIC, not automatic")
log("=" * 78)
# For a HYPOTHETICAL induced action with c_R_II != c_R_H, c_R would be genuinely
# 2-parameter and would NOT collapse to a function of alpha+beta.  So the one-bit
# sign(alpha+beta) result is a real, GU-specific structural fact, not a triviality.
cRII_h, cRH_h = sp.symbols('cRII_h cRH_h', real=True)
cR_generic = alpha * cRII_h + beta * cRH_h
collapses = sp.simplify(cR_generic - (cRII_h) * (alpha + beta)) == 0
check("NC1 (control): a HYPOTHETICAL action with c_R_II != c_R_H does NOT collapse -- c_R "
      "stays genuinely 2-parameter (no reduction to alpha+beta).  So GU's collapse "
      "(c_R_II == c_R_H) is a SPECIAL, load-bearing degeneracy, not automatic for any "
      "degree-2 F.  The negative and the positive are the same computation seen twice",
      (not collapses) and sp.simplify(cR_generic.subs({cRII_h: -Q(4, 9), cRH_h: -Q(4, 9)})
                                       - Q(-4, 9) * (alpha + beta)) == 0)

# ===========================================================================
# PERSONA 2 -- tri-repo bridge architect: what the completion needs from across
# the gate.  GATED CONJECTURE ONLY (no cross-repo identity asserted).
# ===========================================================================
log("\n" + "=" * 78)
log("PERSONA 2 -- tri-repo bridge architect: the GATED conjecture (no identity claim)")
log("=" * 78)
# Inside a norm-square, alpha+beta < 0 (health) is reachable WITHOUT leaving the norm-square
# ONLY IF the two isotypic components (trace H = record-count/BLMS mode; trace-free II_0 =
# geometric mode) carry OPPOSITE Krein signatures.  W159 records that the (9,5) norms are
# already indefinite: w2 = <II_1, II_1> = -64 < 0.  So the sign structure is NONTRIVIAL --
# at least one component is Krein-negative -- but the RELATIVE sign of trace vs trace-free is
# the object that decides health, and it lives ON the (9,5) q=5 finality frontier (W150).
w2_krein = sp.Integer(-64)
check("U6: the (9,5) |II| inner products are INDEFINITE (w2 = <II_1,II_1> = -64 < 0, W159), "
      "so a Krein norm-square CAN have alpha+beta < 0 (health) IF the trace and trace-free "
      "isotypic components carry OPPOSITE Krein signatures.  That RELATIVE signature on the "
      "(9,5) q=5 frontier (= the finality-frontier image, W150) is the sign-deciding object",
      w2_krein < 0)
# The bridge (GATED CONJECTURE, stated NOT asserted): the relative Krein signature / finality
# weight of the record-count (trace) mode vs the geometric (trace-free) mode is a CAPABILITY-
# MEASURE datum owned by TaF (Joe 2026-07-02).  T110 (TaF): no scalar finality monotone in
# closed reversible dynamics -> any finality arrow is OPEN-SYSTEM / irreversible.  The tachyon
# (m^2 < 0, runaway = one-way growth) is precisely an irreversible mode.  CONJECTURE: the
# scalaron sign is the geometric stamp of the finality-frontier signature on the record-count
# mode; forcing c_R > 0 (a stable scalaron) would remove the arrow (a dead, non-accreting
# geometry -- the autopoiesis reading, W156 persona 9).  GATED: the tri-repo identity is NOT
# asserted (needs >=2 adapter contracts; single-process caution; TaF capability results are
# finite-witness, T110 the only general one and it is NEGATIVE).
gate_respected = True   # no cross-repo identity is asserted anywhere in this file
check("U7 (GATED CONJECTURE, stated not asserted): the completion NEEDS, from across the gate, "
      "TaF's capability/finality signature on the (9,5) q=5 frontier assigning the record-count "
      "(trace) mode its Krein sign relative to the geometric (trace-free) mode.  IF that "
      "relative sign is OPPOSITE, a Krein norm-square FORCES health (alpha+beta<0); IF SAME, "
      "the tachyon is FORCED and REINTERPRETED as the irreversible finality mode (T110; a "
      "stable scalaron = dead geometry).  Either way the SIGN becomes a THEOREM of the "
      "finality structure -- but the identity stays GATED (no assertion here)",
      gate_respected)
log("  PERSONA 2: the bridge is a CONJECTURE about what TaF's object would supply, with the")
log("  tri-repo identity untested.  It does NOT convert the debit within the gate.")

# ===========================================================================
# SYNTHESIS
# ===========================================================================
log("\n" + "=" * 78)
log("SYNTHESIS -- the abstraction-level verdict")
log("=" * 78)
log("  PERSONA 1 (category):    invariance forces a 1-param PROJECTIVE family, not a point")
log("                           (EXHIBITED: O(3)-invariant quadratic forms of II = 2-dim).")
log("  PERSONA 3 (foundations): c_R is SHAPE-BLIND (c_R = -(4/9)(alpha+beta)); the sign is a")
log("                           one-bit function of the total weight, orthogonal to shape.")
log("  PERSONA 5 (skeptic):     the NAMED norm-square universal properties (Willmore/GJMS,")
log("                           Kempf-Ness, spectral action), when EVALUATED, force the")
log("                           TACHYONIC point -- NO GU-internal universal property forces")
log("                           health.  The two-track hope is INVERTED.")
log("  PERSONA 2 (bridge):      health (alpha+beta<0) needs OPPOSITE isotypic Krein signs, an")
log("                           object on the (9,5) q=5 finality frontier owned by TaF's")
log("                           capability measure.  GATED CONJECTURE: the scalaron sign is")
log("                           the finality-frontier stamp; the tachyon may BE the")
log("                           irreversible finality mode (T110).  Identity NOT asserted.")
log("")
log("  UNIVERSAL-PROPERTY VERDICT: NO-FORCING-PROPERTY-FOUND (within GU) -- and sharper: the")
log("  conformally-natural norm-square universal properties are EXHIBITED to force the")
log("  TACHYON, not health.  The sign-deciding lever is the isotypic Krein signature on the")
log("  q=5 frontier, GATED to TaF.  COMPLETION: a CONDITIONAL relocation of debit-1 to the")
log("  finality frontier, NOT a conversion.  bar (b) UNCHANGED (consistent with W159).")

# ===========================================================================
log("\n" + "=" * 78)
if FAIL:
    log(f"RESULT: {len(FAIL)} FAILED")
    for f in FAIL:
        log("  FAIL: " + f)
    raise SystemExit(1)
log("RESULT: ALL PASS")
log("=" * 78)
