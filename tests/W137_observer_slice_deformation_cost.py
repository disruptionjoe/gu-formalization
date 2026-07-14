#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
W137 -- The per-observer-slice structure: the DEFORMATION-COST bookkeeping of a
        section (the GU-side shadow of "observers consume issuance to create
        records"), computed EXACTLY at the constant section.

Question (W137 brief, item 3): does creating/extending a section (a "record" in
the observer reading) have a well-defined GU-side energy bookkeeping in the
pointwise |II|^2 cost density?  Answer, computed here:

  YES the bookkeeping is well-defined (the cost of any 2-jet deformation is an
  EXACT rational polynomial in the jet data -- no regularization, no truncation),
  but it is NOT a positive ledger:

  (D1) The constant section is NOT a critical point of the pointwise cost:
       along the MSS direction sigma = u*eta the cost is
       W(u) = 2 - 8u - 64u^2 exactly (the W126 interpolant, re-derived here),
       so the first-order term is -8u != 0.  "Creating a record" exchanges cost
       with the Lambda-channel constant a0 = 2 at FIRST order (the Einstein
       channel a1 = 1/3 with R = -24u gives exactly -8u; double-routed below).
  (D2) The second-order cost form is INDEFINITE, graded by the Lorentzian jet
       structure: exact directions with positive AND negative second-order cost
       are exhibited (traceless pair: +32 vs -32; MSS: -64; gradient sector:
       timelike -16 vs spacelike +16, i.e. consistent with 16 eta(dphi, dphi)
       on the two computed axes).  So "record creation COSTS issuance" is
       FALSE as a sign-definite statement pointwise; the surviving GU-side form
       is SIGNED bookkeeping.
  (D3) One exact point each way:  sigma = (1/10) eta  gives  W = 14/25
       (cost -36/25 relative to a0 = 2);  s_01 = 1/10 (mixed time-space,
       traceless) gives  W = 58/25  (cost +8/25).

Machinery: the pinned ii-s Convention-B literal-graph |II|^2 evaluator on the
conformal family g = e^{2 phi} eta, copied from the verified W126 Route-1 code
(tests/W126_beyond4th_conformal_iisq.py) with a regression check against the
W126 slice decomposition W = 2 + R/3 + (8/9) R^2 - 4 Ric^2 before any new
number is extracted.  Everything exact sympy; no floats; deterministic.

Run:  python -u tests/W137_observer_slice_deformation_cost.py   (exit 0 iff all PASS)
"""
from __future__ import annotations

import sys

import sympy as sp

FAIL = []


def check(name, ok, detail=""):
    print(("PASS" if ok else "FAIL") + " :: " + name + (("  --  " + detail) if detail else ""), flush=True)
    if not ok:
        FAIL.append(name)


def log(msg=""):
    print(msg, flush=True)


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
    """trace-reversed Frobenius (DeWitt/gimmel fiber) form V_h(k,l)."""
    A = Gi * k
    B = Gi * l
    return sp.trace(A * B) - sp.Rational(1, 2) * sp.trace(A) * sp.trace(B)


def route1_W(with_v, vvals=None, svals=None):
    """Exact W = |II|^2 at x=0 for the conformal jet (W126 Route 1, Convention B,
    vertical representative + normal lift; verbatim structure)."""
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
    return sp.expand(sp.simplify(sp.expand(W)))


def zero_s():
    return {ij: 0 for ij in pairs}


# ===========================================================================
# PART 0 -- positive controls: flat constant and the W126 slice decomposition
# ===========================================================================
log("=" * 78)
log("PART 0 -- controls: flat section constant a0 and the W126 slice regression")
log("=" * 78)

Wflat = route1_W(with_v=False, vvals=[0] * 4, svals=zero_s()).subs(E0, 1)
check("PC0: constant-section pointwise cost |II|^2(eta) = 2 exactly (a0 = 2, the "
      "DeWitt-Lambda / issuance constant; W126 control reproduced)",
      sp.simplify(Wflat - 2) == 0, f"W(eta) = {sp.simplify(Wflat)}")

# curvature pin (from scratch, W126 Part-0 conventions): R and Ricci at the jet
def curvature_of_conformal():
    ph = phi_jet(False)
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
    Rsc = sp.expand(sum(eta[m, m] * Ric[m, m] for m in range(DIM)) / E0)
    return Ric, Rsc


Ric0, R0 = curvature_of_conformal()
trs = sum(eta[i, i] * S(i, i) for i in range(DIM))
check("PC1: curvature convention pinned from scratch: R = -6 e^{-2p} tr_eta(s)",
      sp.simplify(R0 + 6 * trs / E0) == 0)


def W_slice_predicted(svals):
    """W126 slice decomposition W = 2 + R/3 + (8/9)R^2 - 4 Ric^2 at E0 = 1."""
    subs = {ssym[ij]: svals[ij] for ij in pairs}
    R = sp.expand(R0.subs(subs).subs(E0, 1))
    Ric = Ric0.subs(subs).subs(E0, 1)
    RicSq = sp.expand(sum(eta[a, a] * eta[b, b] * Ric[a, b]**2
                          for a in range(DIM) for b in range(DIM)))
    return sp.expand(2 + R / 3 + sp.Rational(8, 9) * R**2 - 4 * RicSq)


# ===========================================================================
# PART 1 -- D1: the MSS direction, linear term (the flat section is NOT a
#           pointwise critical point of the cost density)
# ===========================================================================
log()
log("=" * 78)
log("PART 1 -- MSS direction sigma = u*eta: W(u) exact; linear term = -8u")
log("=" * 78)

u = sp.Symbol('u', real=True)
sv_mss = {ij: (u * eta[ij[0], ij[1]] if ij[0] == ij[1] else 0) for ij in pairs}
W_mss = sp.expand(route1_W(with_v=False, vvals=[0] * 4, svals=sv_mss).subs(E0, 1))
check("D1a: W(u) = 2 - 8u - 64u^2 EXACTLY on the MSS direction (W126 interpolant "
      "re-derived by direct evaluation)",
      sp.expand(W_mss - (2 - 8 * u - 64 * u**2)) == 0, f"W(u) = {W_mss}")
check("D1b: dW/du(0) = -8 != 0 -- the constant section is NOT a critical point of "
      "the pointwise cost density: record-creating deformation exchanges cost at "
      "FIRST order (Einstein channel a1 = 1/3 with R = -24u)",
      sp.diff(W_mss, u).subs(u, 0) == -8)
check("D1c: double route: the W126 slice decomposition predicts the same W(u)",
      sp.expand(W_slice_predicted(sv_mss) - W_mss) == 0)

# ===========================================================================
# PART 2 -- D2: indefiniteness of the second-order cost form (curvature slice)
# ===========================================================================
log()
log("=" * 78)
log("PART 2 -- indefinite second-order cost: exact positive and negative directions")
log("=" * 78)

w = sp.Symbol('w', real=True)

# direction A: mixed time-space, traceless: s_01 = w only
sv_A = {ij: (w if ij == (0, 1) else 0) for ij in pairs}
W_A = sp.expand(route1_W(with_v=False, vvals=[0] * 4, svals=sv_A).subs(E0, 1))
check("D2a: traceless mixed (0,1) direction: W = 2 + 32 w^2 exactly -- POSITIVE "
      "second-order cost",
      sp.expand(W_A - (2 + 32 * w**2)) == 0, f"W = {W_A}")
check("D2a': double route (slice decomposition agrees; Ric^2 = -8w^2 there, so "
      "-4 Ric^2 = +32 w^2)",
      sp.expand(W_slice_predicted(sv_A) - W_A) == 0)

# direction B: purely spatial traceless diag(0, w, -w, 0)
sv_B = {ij: 0 for ij in pairs}
sv_B[(1, 1)] = w
sv_B[(2, 2)] = -w
W_B = sp.expand(route1_W(with_v=False, vvals=[0] * 4, svals=sv_B).subs(E0, 1))
check("D2b: traceless spatial diag(0,w,-w,0) direction: W = 2 - 32 w^2 exactly -- "
      "NEGATIVE second-order cost (same magnitude, opposite sign: indefiniteness "
      "INSIDE the traceless sector)",
      sp.expand(W_B - (2 - 32 * w**2)) == 0, f"W = {W_B}")
check("D2b': double route (slice decomposition agrees)",
      sp.expand(W_slice_predicted(sv_B) - W_B) == 0)

# ===========================================================================
# PART 3 -- D2 continued: the gradient (record-extension) sector, per axis
# ===========================================================================
log()
log("=" * 78)
log("PART 3 -- gradient sector: timelike vs spacelike dphi, exact quadratic costs")
log("=" * 78)

W_t = sp.simplify(route1_W(with_v=True, vvals=[w, 0, 0, 0], svals=zero_s()).subs(E0, 1))
W_x = sp.simplify(route1_W(with_v=True, vvals=[0, w, 0, 0], svals=zero_s()).subs(E0, 1))
ser_t = sp.series(W_t, w, 0, 6).removeO()
ser_x = sp.series(W_x, w, 0, 6).removeO()
q_t = ser_t.coeff(w, 2)
q_x = ser_x.coeff(w, 2)
log(f"  W(timelike v) series  = {sp.expand(ser_t)}")
log(f"  W(spacelike v) series = {sp.expand(ser_x)}")
check("D2c: gradient sector, TIMELIKE dphi: quadratic cost coefficient is NEGATIVE",
      q_t.is_number and q_t < 0, f"coeff = {q_t}")
check("D2d: gradient sector, SPACELIKE dphi: quadratic cost coefficient is POSITIVE "
      "-- the gradient sector is ALSO indefinite, graded by the causal character "
      "of the deformation gradient", q_x.is_number and q_x > 0, f"coeff = {q_x}")
check("D2e: spacelike gradient reproduces the W126 gradient-sector series "
      "2 + 16 v^2 + 320 v^4 + ... at its first two orders",
      ser_x.coeff(w, 0) == 2 and ser_x.coeff(w, 2) == 16 and
      ser_x.coeff(w, 4) == 320)

# ===========================================================================
# PART 4 -- D3: one exact point each way (the wave's exact-point deliverable)
# ===========================================================================
log()
log("=" * 78)
log("PART 4 -- exact-point costs relative to the issuance constant a0 = 2")
log("=" * 78)

W_pt_neg = W_mss.subs(u, sp.Rational(1, 10))
check("D3a: sigma = (1/10) eta:  W = 14/25 exactly; cost = W - a0 = -36/25 "
      "(the deformation RELEASES pointwise cost)",
      sp.simplify(W_pt_neg - sp.Rational(14, 25)) == 0
      and sp.simplify(W_pt_neg - 2 + sp.Rational(36, 25)) == 0,
      f"W = {W_pt_neg}")
W_pt_pos = W_A.subs(w, sp.Rational(1, 10))
check("D3b: s_01 = 1/10:  W = 58/25 exactly; cost = +8/25 (this deformation PAYS)",
      sp.simplify(W_pt_pos - sp.Rational(58, 25)) == 0
      and sp.simplify(W_pt_pos - 2 - sp.Rational(8, 25)) == 0,
      f"W = {W_pt_pos}")

# ===========================================================================
log()
log("=" * 78)
if FAIL:
    log(f"RESULT: {len(FAIL)} FAILURES: {FAIL}")
    sys.exit(1)
log("RESULT: ALL CHECKS PASS (exit 0).  The deformation-cost bookkeeping is exact "
    "and well-defined; it is SIGNED (indefinite), with a nonzero first-order "
    "exchange against the a0 = 2 issuance constant.")
sys.exit(0)
