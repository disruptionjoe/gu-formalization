#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
HQW-NOTE (H10) -- confirming test for the SHAPE-BLIND c_R lemma.

Standalone re-derivation and point-checks of the lemma registered in
explorations/HQW-NOTE-shape-blind-cR-lemma-2026-07-14.md.  This does NOT replace
the primary machine check (tests/W165_universal_property_and_sign.py, exit 0); it
is a small, independent confirmation using the same verbatim W126 Route-1
machinery, with positive controls first and a negative control.

LEMMA (GU-independent higher-derivative-gravity fact).  For the induced
conformal-graph functional on the shape family  F = alpha|II|^2 + beta|H|^2,
the covariant scalaron (R^2-channel) coupling is
        c_R(alpha, beta) = -(4/9) (alpha + beta),
so it is SHAPE-BLIND (depends only on the total weight alpha+beta, never on the
alpha:beta ratio), and  sign(c_R) = -sign(alpha + beta).

WHY it holds: both pure invariants share the same covariant coupling,
        c_R(|II|^2) = c_R(|H|^2) = -4/9  (W130, W159),
and c_R is linear in (alpha, beta); linearity of a shared value collapses to the
total weight.  The independent W159 coordinate a1 = (alpha + 4 beta)/3 does vary
with shape -- so shape freedom is real but lives entirely in a1, not in c_R.

CHECKS (deterministic sympy; positive controls first):
  PC1  reproduce W126 |II|^2 slice decomposition (2, 1/3, 8/9, -4).
  PC2  reproduce W130 covariant c_R(|II|^2) = a2s + a3s/3 = -4/9 (< 0, tachyonic).
  PC3  reproduce W159 |H|^2 slice decomposition (-1, 4/3, -4/9, 0), c_R(|H|^2) = -4/9.
  L1   the shape family collapses: c_R(alpha,beta) = -(4/9)(alpha+beta) exactly.
  L2   c_R is shape-blind: d c_R / d alpha == d c_R / d beta (no ratio dependence),
       while a1(alpha,beta) = (alpha + 4 beta)/3 is NOT shape-blind (W159 det = 4/9).
  L3   point-checks at named (alpha,beta), incl. GU (1,0) and healthy (-2,1):
         (1,0) GU pure-|II|^2 : c_R = -4/9 < 0 (tachyonic)
         (0,1) pure-|H|^2     : c_R = -4/9 < 0
         (1,1) positive cone  : c_R = -8/9 < 0
         (3,1)                : c_R = -16/9 < 0
         (-2,1) healthy       : c_R = +4/9 > 0  (needs alpha+beta < 0)
         (1,-1) trace-free-ish: c_R = 0        (the sign boundary alpha+beta=0)
       sign(c_R) = -sign(alpha+beta) at every point.
  NC1  negative control: a HYPOTHETICAL functional with c_R_II != c_R_H does NOT
       collapse to a function of alpha+beta -- so the collapse is a real, load-bearing
       degeneracy of GU's induced action, not automatic for any degree-2 F.

Run:  python -u tests/HQW_NOTE_shape_blind_cR.py    (exit 0 iff all PASS).

Binding: exploration grade; GU-independent higher-derivative-gravity fact; honest
grading; no canon change; no external action; zero em dashes in paper-facing text.
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
# MACHINERY -- verbatim W126 Route-1 ii-s Convention-B B^V + normal lift, exactly
# as used by W157/W159/W165.  Signature (1,3).  Regression-pinned by PC1-PC3.
# ===========================================================================
DIM = 4
eta = sp.diag(-1, 1, 1, 1)
pairs = [(a, b) for a in range(DIM) for b in range(a, DIM)]
xs = [sp.Symbol(f'x{i}', real=True) for i in range(DIM)]
p = sp.Symbol('p', real=True)
E0 = sp.Symbol('E0', positive=True)
ssym = {(i, j): sp.Symbol(f's{i}{j}', real=True) for (i, j) in pairs}


def S(i, j):
    return ssym[(i, j)] if i <= j else ssym[(j, i)]


def at0(expr):
    e = expr.subs({xi: 0 for xi in xs})
    e = e.subs(p, sp.log(E0) / 2)
    return sp.expand(sp.powsimp(e, force=True))


def Vg_of(Gi, k, l):
    A = Gi * k
    B = Gi * l
    return sp.trace(A * B) - sp.Rational(1, 2) * sp.trace(A) * sp.trace(B)


def route1_W(svals, want_H=False):
    ph = p + sp.Rational(1, 2) * sum(S(i, j) * xs[i] * xs[j] for i in range(DIM) for j in range(DIM))
    E = sp.exp(2 * ph)
    G = sp.Matrix(DIM, DIM, lambda i, j: E * eta[i, j])
    subs_num = {ssym[ij]: svals[ij] for ij in pairs}
    G = G.subs(subs_num)
    dG = [sp.diff(G, xs[m]) for m in range(DIM)]
    ddG = [[sp.diff(dG[m], xs[n]) for n in range(DIM)] for m in range(DIM)]
    Gi_x = sp.Matrix(DIM, DIM, lambda i, j: eta[i, j] / E.subs(subs_num))
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
            _, Hv = route1_W(svals, want_H=True)
            Wv = sp.nsimplify(Hv.subs(E0, 1))
        else:
            Wv = sp.nsimplify(route1_W(svals, want_H=False).subs(E0, 1))
        args = [svals[ij] for ij in pairs]
        eqs.append(a0 + a1 * _Rf(*args) + a2s * _Rf(*args)**2 + a3s * _Rif(*args) - Wv)
    s0 = sp.solve(eqs, [a0, a1, a2s, a3s], dict=True)[0]
    return s0[a0], s0[a1], s0[a2s], s0[a3s]


Q = sp.Rational

# ===========================================================================
log("=" * 78)
log("HQW-NOTE (H10) -- SHAPE-BLIND c_R lemma: c_R(alpha,beta) = -(4/9)(alpha+beta)")
log("Positive controls first.")
log("=" * 78)

# --- POSITIVE CONTROLS ------------------------------------------------------
a0v, a1v, a2sv, a3sv = slice_decomp(want_H=False)
c_R_II = a2sv + a3sv * Q(1, 3)
check("PC1: |II|^2 slice decomposition reproduces W126 (2, 1/3, 8/9, -4)",
      (a0v, a1v, a2sv, a3sv) == (sp.Integer(2), Q(1, 3), Q(8, 9), sp.Integer(-4)),
      f"got ({a0v}, {a1v}, {a2sv}, {a3sv})")
check("PC2: covariant c_R(|II|^2) = a2s + a3s/3 = -4/9 (W130), tachyonic (< 0)",
      c_R_II == Q(-4, 9) and c_R_II < 0, f"c_R(|II|^2) = {c_R_II}")
a0H, a1H, a2sH, a3sH = slice_decomp(want_H=True)
c_R_H = a2sH + a3sH * Q(1, 3)
check("PC3: |H|^2 slice decomposition reproduces W159 (-1, 4/3, -4/9, 0), c_R(|H|^2) = -4/9",
      (a0H, a1H, a2sH, a3sH) == (sp.Integer(-1), Q(4, 3), Q(-4, 9), sp.Integer(0))
      and c_R_H == Q(-4, 9), f"|H|^2 = ({a0H},{a1H},{a2sH},{a3sH}), c_R(|H|^2) = {c_R_H}")

# --- LEMMA ------------------------------------------------------------------
log("\n--- LEMMA: shape-family collapse and shape-blindness ---")
alpha, beta = sp.symbols('alpha beta', real=True)
cR_fam = sp.expand(alpha * c_R_II + beta * c_R_H)
a1_fam = sp.expand(alpha * a1v + beta * a1H)
check("L1: c_R(alpha,beta) = -(4/9)(alpha+beta) exactly (the two shared -4/9 couplings collapse "
      "to the total weight)",
      sp.simplify(cR_fam - Q(-4, 9) * (alpha + beta)) == 0, f"c_R_fam = {cR_fam}")
check("L2: c_R is SHAPE-BLIND (d c_R/d alpha == d c_R/d beta), while a1 = (alpha + 4 beta)/3 is "
      "NOT shape-blind (the W159 det=4/9 independence lives entirely in a1)",
      sp.diff(cR_fam, alpha) == sp.diff(cR_fam, beta)
      and sp.simplify(a1_fam - (alpha + 4 * beta) * Q(1, 3)) == 0
      and sp.diff(a1_fam, alpha) != sp.diff(a1_fam, beta),
      f"a1_fam = {a1_fam}, det[[a1_II,a1_H],[c_R_II,c_R_H]] = {sp.nsimplify(a1v*c_R_H - a1H*c_R_II)}")

# --- POINT CHECKS (incl. GU (1,0) and healthy (-2,1)) -----------------------
log("\n--- L3: point-checks, sign(c_R) = -sign(alpha+beta) ---")
points = [((1, 0), "GU pure-|II|^2"), ((0, 1), "pure-|H|^2"), ((1, 1), "positive cone"),
          ((3, 1), "positive cone"), ((-2, 1), "HEALTHY"), ((1, -1), "boundary alpha+beta=0")]
ok_all = True
for (av, bv), tag in points:
    cr = cR_fam.subs({alpha: av, beta: bv})
    expect = Q(-4, 9) * (av + bv)
    ok = (cr == expect) and (sp.sign(cr) == -sp.sign(av + bv))
    ok_all = ok_all and ok
    log(f"  (alpha,beta)=({av:>2},{bv:>2}) {tag:22s}: c_R = {str(cr):>6}   "
        f"sign(c_R)={sp.sign(cr)}  -sign(alpha+beta)={-sp.sign(av+bv)}  [{'OK' if ok else 'MISMATCH'}]")
check("L3: at every named point c_R = -(4/9)(alpha+beta) and sign(c_R) = -sign(alpha+beta); GU "
      "(1,0) and pure-|H|^2 (0,1) and the whole positive cone are tachyonic (c_R < 0); health "
      "(c_R > 0) is reached only for alpha+beta < 0, e.g. the (-2,1) point (c_R = +4/9)",
      ok_all and cR_fam.subs({alpha: 1, beta: 0}) < 0 and cR_fam.subs({alpha: -2, beta: 1}) > 0)

# --- NEGATIVE CONTROL -------------------------------------------------------
log("\n--- NC1: the collapse is a real degeneracy, not automatic ---")
cRII_h, cRH_h = sp.symbols('cRII_h cRH_h', real=True)
cR_generic = alpha * cRII_h + beta * cRH_h
collapses_generic = sp.simplify(cR_generic - cRII_h * (alpha + beta)) == 0
check("NC1: a HYPOTHETICAL functional with c_R(|II|^2) != c_R(|H|^2) stays genuinely 2-parameter "
      "(does NOT reduce to alpha+beta); the collapse requires the EQUALITY c_R(|II|^2) = "
      "c_R(|H|^2) = -4/9, so the shape-blindness is a load-bearing GU degeneracy, not automatic",
      (not collapses_generic)
      and sp.simplify(cR_generic.subs({cRII_h: -Q(4, 9), cRH_h: -Q(4, 9)}) - Q(-4, 9) * (alpha + beta)) == 0)

# ===========================================================================
log("\n" + "=" * 78)
if FAIL:
    log(f"RESULT: {len(FAIL)} FAILED :: {FAIL}")
    raise SystemExit(1)
log("RESULT: ALL PASS -- c_R(alpha,beta) = -(4/9)(alpha+beta) is shape-blind; sign(c_R) = "
    "-sign(alpha+beta); confirms explorations/HQW-NOTE-shape-blind-cR-lemma-2026-07-14.md.")
log("=" * 78)
