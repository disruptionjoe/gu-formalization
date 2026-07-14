#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
W126 -- Do the BEYOND-4TH-ORDER terms of the induced |II|^2 functional lift the
        tachyonic scalaron vacuum? (W122 escape route #2, run to ground.)

Context: W122 proved the scalaron is a genuine positive-norm tachyon
(m_0^2 = gamma/(6 f_0^2) < 0 on the AF trajectory, f_0^2 < 0) WITHIN the 4th-order
truncation, and named the escape: if the full |II|^2 functional generates higher-order
curvature invariants (R^3, R box R, ...), the scalaron potential V(chi) gains structure
beyond the inverted parabola and the vacuum could shift to a stable minimum.

STAGE A (this file, EXACT): evaluate the induced |II|^2 EXACTLY (all orders in the
conformal factor phi -- no truncation) on the conformal family g = e^{2 phi} eta,
pointwise on 2-jets of phi.  Pinned construction: the ii-s Convention-B literal-graph
second fundamental form (explorations/geometry-curvature-emergence/
ii-s-coordinate-formula-2026-06-23.md, Section 4), the same object H15/H24/H25 used.

  KEY STRUCTURAL CLAIM (proved symbolically below, two routes):
    On the POTENTIAL slice (jets with dphi = 0, general second derivative s_{mu nu}),
    the scalar W = |II|^2 is an EXACT polynomial of total degree 2 in the scale-
    covariant variable sigma = e^{-2 phi} s, with phi-independent coefficients.
    Since R, Ricci on this slice are LINEAR in sigma, the potential-sector effective
    Lagrangian is EXACTLY quadratic in curvature: the cubic and ALL higher potential
    coefficients of the induced functional VANISH IDENTICALLY.  c_3 = c_4 = ... = 0
    is an EXACT statement, not a truncation.
  The same holds for |H|^2 and for the slice-subtracted variant, hence for the whole
  wave-35 shape-dimension-1 family alpha |II|^2 + beta |H|^2 (any alpha, beta).

  ROUTE 1: Convention-B vertical representative B^V + normal-lift inner product
           (the ii-s Section 4/5 formulas), fully symbolic in (p, s_{mu nu}).
  ROUTE 2: independent full-ambient computation (base + fiber components of II via
           the Section-2 ambient Christoffels, tangential subtraction by induced
           Christoffels, contraction with the full block ambient metric), exact
           rationals on sampled jets; cubic/quartic fit residuals must vanish and
           the quadratic coefficients must match Route 1.  A jet with dphi != 0
           checks the two routes against each other where they genuinely differ
           (normal-lift identity).

STAGE B: with c_3 = 0 exact at tree level, the scalaron potential is EXACTLY the
W122 object.  Einstein-frame potential V(R) = (b R^2 + 2 L)/(2 (gamma + 2 b R)^2):
proved below that for b < 0 it has NO minimum (unique finite extremum = the tachyonic
de Sitter/flat point, a MAXIMUM; V -> -oo at the f' -> 0 wall).  RUNAWAY, exact.
For a hypothetical LOOP-generated c R^3 (the only place beyond-4th-order structure
can now come from), the shifted extremum R* = sqrt(gamma/c) exists for c > 0, is
non-ghost + non-tachyonic only for c > b^2/(4 gamma) (for b^2/(9 gamma) < c <
b^2/(4 gamma) it has f'' > 0 but f' < 0: a GHOST vacuum -- a maximum in disguise once
the kinetic sign is tracked).  EFT validity with the W46 AF numbers: R*/mu_DW^2 is
parametrically LARGE on both fixed-ratio branches -- the rescue vacuum, if loop-
induced, sits far above the DeWitt scale.  OUT-OF-VALIDITY.

STAGE C: f''(R) = 2 f_0^2 EXACTLY on the conformal potential sector at tree level
(not approximately): non-constant f'' does NOT arise from the induced geometry.
The f(R) stability condition f'' > 0 fails at every R on the AF trajectory.

Conventions pinned (flag for the W123 convention audit, not resolved here):
  * eta = diag(-1,+1,+1,+1); Riemann/Ricci computed from scratch in Part 0 (no import).
  * literal-graph immersion (Convention B), coordinate product splitting of T(Met X4);
    the keep-vs-subtract slice fork and the sqrt(det gbar)-vs-sqrt(det g) measure fork
    are carried as branches where they can matter (they cannot, for the c_3 = 0 claim:
    at dphi = 0 the two measures agree pointwise and both variants are degree <= 2).

Run:  python -u tests/W126_beyond4th_conformal_iisq.py     (exit 0 iff all PASS)
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
eta = sp.diag(-1, 1, 1, 1)
pairs = [(a, b) for a in range(DIM) for b in range(a, DIM)]     # 10 fiber pairs
xs = [sp.Symbol(f'x{i}', real=True) for i in range(DIM)]
p = sp.Symbol('p', real=True)                                    # phi(0)
E0 = sp.Symbol('E0', positive=True)                              # e^{2p}
vsym = [sp.Symbol(f'v{i}', real=True) for i in range(DIM)]       # dphi(0)
ssym = {(i, j): sp.Symbol(f's{i}{j}', real=True) for (i, j) in pairs}   # dd phi(0)


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
    e = e.subs(p, sp.log(E0) / 2)          # e^{2p} -> E0 exactly (E0 > 0)
    return sp.expand(sp.powsimp(e, force=True))


# ===========================================================================
# PART 0 -- curvature convention pin: R, Ricci of g = e^{2 phi} eta at the jet
#           point, computed FROM SCRATCH (Christoffels of the 4-metric).
# ===========================================================================
log("=" * 78)
log("PART 0 -- conformal curvature pin (direct 4D computation, no imported formula)")
log("=" * 78)


def curvature_of_conformal(with_v):
    ph = phi_jet(with_v)
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


Ric0, R0 = curvature_of_conformal(with_v=False)          # potential slice: dphi = 0
trs = sum(eta[i, i] * S(i, i) for i in range(DIM))       # eta^{mu nu} s_{mu nu}
check("R[e^{2phi}eta] at dphi=0 jet:  R = -6 e^{-2p} tr_eta(s)   (convention PINNED here)",
      sp.simplify(R0 + 6 * trs / E0) == 0, f"R = {sp.simplify(R0)}")
ric_expect = sp.Matrix(DIM, DIM, lambda i, j: -2 * S(i, j) - eta[i, j] * trs)
check("Ricci at dphi=0 jet:  R_{mu nu} = -2 s_{mu nu} - eta_{mu nu} tr_eta(s)",
      sp.simplify(Ric0 - ric_expect) == sp.zeros(DIM, DIM),
      "Einstein check: s ~ eta gives R_{mu nu} = (R/4) g_{mu nu} automatically")
# Ricci^2 invariant on the slice, as a function of sigma := s / E0 (scale-covariant):
sig = {(i, j): sp.Symbol(f'g{i}{j}', real=True) for (i, j) in pairs}


def SG(i, j):
    return sig[(i, j)] if i <= j else sig[(j, i)]


subs_sigma = {ssym[ij]: sig[ij] * E0 for ij in pairs}
trsig = sum(eta[i, i] * SG(i, i) for i in range(DIM))
R_of_sigma = sp.expand(R0.subs(subs_sigma))              # = -6 tr_eta(sigma), E0-free
RicSq_of_sigma = sp.expand(sum(eta[a, a] * eta[b, b] * (Ric0[a, b])**2
                               for a in range(DIM) for b in range(DIM)).subs(subs_sigma) / 1)
# note: Ric_{mu nu} R^{mu nu} = g^{ma} g^{nb} Ric_{mn} Ric_{ab} = E0^{-2} eta eta Ric Ric;
RicSq_of_sigma = sp.expand(RicSq_of_sigma / E0**2)
check("R and Ricci^2 on the slice are E0-free functions of sigma = e^{-2p} s alone",
      (R_of_sigma.has(E0) is False) and (sp.simplify(RicSq_of_sigma).has(E0) is False),
      f"R(sigma) = {R_of_sigma}")


# ===========================================================================
# ROUTE 1 -- Convention-B vertical representative B^V + normal lift (ii-s Sec 4/5),
#            FULLY SYMBOLIC in (p ; s_{mu nu}) on the potential slice, and in
#            (p ; v ; s) for the route-agreement configuration.
# ===========================================================================
log()
log("=" * 78)
log("ROUTE 1 -- ii-s Convention-B B^V + normal lift, exact symbolic")
log("=" * 78)


def Vg_of(Gi, k, l):
    """trace-reversed Frobenius form V_h(k,l) at fiber point with inverse Gi."""
    A = Gi * k
    B = Gi * l
    return sp.trace(A * B) - sp.Rational(1, 2) * sp.trace(A) * sp.trace(B)


def route1_W(with_v, vvals=None, svals=None, want_H=False, subtract_slice=False):
    """Exact W = |II|^2 (and optionally |H|^2) at x=0 for the conformal jet."""
    ph = phi_jet(with_v)
    E = sp.exp(2 * ph)
    G = sp.Matrix(DIM, DIM, lambda i, j: E * eta[i, j])           # fiber value g_ab(x)
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
    # induced metric gbar(x) = g + V_g(dg, dg)
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
    # Convention-B vertical representative
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


# ---- flat-section control -------------------------------------------------
Wflat = route1_W(with_v=False, vvals=[0] * 4, svals={ij: 0 for ij in pairs}).subs(E0, 1)
check("CONTROL: flat-section constant |II|^2(eta) is a POSITIVE pure number (= 2 in this "
      "pinned Convention-B normalization) -- the DeWitt-Lambda-type term, sign matching "
      "H24/H50 direction.  NORMALIZATION FLAG: H50's c_L = 3/8 lives in the horizontal-"
      "sectional normalization chain; the 2 vs 3/8 ratio (16/3) is a convention item for "
      "the W123 audit, not a contradiction (H25 already graded magnitudes normalization-"
      "gated, signs robust)", sp.simplify(Wflat - 2) == 0,
      f"|II|^2(eta) = {sp.simplify(Wflat)}")

# ---- THE MAIN COMPUTATION: potential slice, general s, symbolic p ---------
log()
log("Route 1 main run: dphi = 0, s_{mu nu} fully general (10 symbols), p symbolic ...")
W1, H2_1 = route1_W(with_v=False, want_H=True)
W1s = sp.expand(sp.simplify(W1.subs(subs_sigma)))
H2s = sp.expand(sp.simplify(H2_1.subs(subs_sigma)))
check("STAGE A KEY (i): W = |II|^2 on the potential slice depends on (p, s) ONLY through "
      "sigma = e^{-2p} s  (all conformal-factor powers cancel EXACTLY, all orders in phi)",
      (W1s.has(E0) is False), "W(p,s) = W(sigma) identically")
polyW = sp.Poly(W1s, *[sig[ij] for ij in pairs])
check("STAGE A KEY (ii): W(sigma) is an EXACT polynomial of TOTAL DEGREE 2 -- the induced "
      "|II|^2 generates NO cubic or higher potential-sector invariants: c_3 = c_4 = ... = 0 EXACTLY",
      polyW.total_degree() == 2, f"total degree = {polyW.total_degree()}")
check("|H|^2 (Willmore piece) likewise degree <= 2 and E0-free -> the whole shape-dim-1 "
      "family alpha|II|^2 + beta|H|^2 has EXACTLY quadratic potential sector",
      (H2s.has(E0) is False) and sp.Poly(H2s, *[sig[ij] for ij in pairs]).total_degree() <= 2,
      f"deg |H|^2 = {sp.Poly(H2s, *[sig[ij] for ij in pairs]).total_degree()}")

# subtracted-slice fork (keep-vs-subtract convention): same structural claim
Wsub = route1_W(with_v=False, subtract_slice=True)
Wsub_s = sp.expand(sp.simplify(Wsub.subs(subs_sigma)))
check("FORK carried: slice-SUBTRACTED variant |II - II_ref|^2 also E0-free and degree <= 2 "
      "(keep-vs-subtract cannot resurrect higher potential terms)",
      (Wsub_s.has(E0) is False) and sp.Poly(Wsub_s, *[sig[ij] for ij in pairs]).total_degree() <= 2)

# ---- decompose W on the invariant basis {1, R, R^2, Ric^2} ----------------
c0, c1, c2, c3b = sp.symbols('c0 c1 c2 c3b', real=True)
ansatz = c0 + c1 * R_of_sigma + c2 * R_of_sigma**2 + c3b * RicSq_of_sigma
sol = sp.solve(sp.Poly(sp.expand(W1s - ansatz), *[sig[ij] for ij in pairs]).coeffs(),
               [c0, c1, c2, c3b], dict=True)
check("W(sigma) is EXACTLY spanned by {1, R, R^2, Ric_{mu nu}Ric^{mu nu}} on the slice "
      "(no residual invariant)", len(sol) == 1)
coef = sol[0]
log(f"  Induced potential-sector coefficients (Convention B, literal graph, pinned Part-0 "
    f"curvature convention):")
log(f"    Lambda-sector constant  a0            = {coef[c0]}   (DeWitt-Lambda-type, positive)")
log(f"    Einstein-sector         a1 (coeff R)  = {coef[c1]}   (positive = attractive, H25-consistent)")
log(f"    R^2-sector (slice)      a2            = {coef[c2]}")
log(f"    Ricci^2-sector (slice)  a3            = {coef[c3b]}")
log(f"    R^3 and ALL higher potential terms    = 0   (EXACT, all orders in phi)")
log(f"    NOTE: on the dphi=0 slice, {{R^2, Ric^2, C^2, GB}} project onto a 2D space; a2/a3 "
    f"are slice coefficients, NOT a unique 4D {{R^2, C^2}} split.")
check("a0 == flat-section constant (internal consistency of the decomposition)",
      coef[c0] == sp.simplify(Wflat))
# ---- the MSS-slice effective F(R): the object the vacuum analysis needs ----
Rsym = sp.Symbol('Rv', real=True)
F_mss = sp.expand(W1s.subs({sig[ij]: (-Rsym / 24 * eta[ij[0], ij[1]] if ij[0] == ij[1] else 0)
                            for ij in pairs}))    # sigma = u*eta, R = -24 u  =>  u = -R/24
check("MSS-slice effective Lagrangian is EXACTLY  F(R) = 2 + R/3 - R^2/9  (closed form; "
      "terminates at R^2 -- the Stage-A deliverable in f(R) language)",
      sp.expand(F_mss - (2 + Rsym / 3 - Rsym**2 / 9)) == 0, f"F(R) = {F_mss}")
check("BONUS (W80-direction corroboration, CONVENTION-FLAGGED + ARGUED): the TREE-level "
      "induced scalar-slice R^2 coefficient is NEGATIVE (-1/9) relative to the H25-"
      "calibrated attractive Einstein term (+1/3) -- the same sign the ported one-loop "
      "flow assigns f_0^2 on the AF trajectory.  Tree-level |II|^2 geometry natively "
      "leans tachyonic on the vacuum slice; it does NOT supply a positive-f_0^2 escape",
      sp.diff(F_mss, Rsym, 2) / 2 == -sp.Rational(1, 9) and coef[c1] > 0)
check("Einstein-sector coefficient a1 is NONZERO (the induced EH term is present in the "
      "conformal potential sector) -- sign/magnitude CONVENTION-FLAGGED for the W123 audit",
      coef[c1] != 0, f"a1 = {coef[c1]}")
check("4-derivative sector nonzero (a2, a3 not both 0): the R^2-class landing (H49) is visible "
      "on the slice", (coef[c2] != 0) or (coef[c3b] != 0))

# ===========================================================================
# ROUTE 2 -- independent full-ambient computation (Section-2 Christoffels,
#            base+fiber components, tangential subtraction, block metric).
# ===========================================================================
log()
log("=" * 78)
log("ROUTE 2 -- full-ambient II (base+fiber components), exact rationals on jets")
log("=" * 78)


def d_pair(a, b, m, l):
    return sp.Rational(1, 2) * ((1 if (a == m and b == l) else 0) + (1 if (a == l and b == m) else 0))


def Epair(ab):
    a, b = ab
    M = sp.zeros(DIM, DIM)
    M[a, b] += 1
    M[b, a] += 1
    if a == b:
        M[a, b] = sp.Integer(1)
    return M


def route2_W(E0v, vv, sv):
    """Full-ambient |II|^2 at x=0 for the 2-jet: E(x) with E(0)=E0v, dphi(0)=vv, ddphi(0)=sv.
    Polynomial surrogate section with the same 2-jet (II depends only on the 2-jet)."""
    # E(x) = E0 (1 + 2 v.x + (s_{ij} + 2 v_i v_j) x^i x^j) is a polynomial surrogate with
    # the EXACT 2-jet of e^{2 phi}: dE(0) = 2 E0 v_i, ddE(0) = E0 (2 s_{ij} + 4 v_i v_j).
    Ex = E0v * (1 + 2 * sum(vv[i] * xs[i] for i in range(DIM))
                + sum((sv[(min(i, j), max(i, j))] + 2 * vv[i] * vv[j]) * xs[i] * xs[j]
                      for i in range(DIM) for j in range(DIM)))
    Hx = sp.Matrix(DIM, DIM, lambda i, j: Ex * eta[i, j])
    dH = [sp.diff(Hx, xs[m]) for m in range(DIM)]
    ddH = [[sp.diff(dH[m], xs[n]) for n in range(DIM)] for m in range(DIM)]
    H0 = Hx.applyfunc(lambda e: e.subs({x: 0 for x in xs}))
    dH0 = [m.applyfunc(lambda e: e.subs({x: 0 for x in xs})) for m in dH]
    ddH0 = [[ddH[m][n].applyfunc(lambda e: e.subs({x: 0 for x in xs})) for n in range(DIM)] for m in range(DIM)]
    Hi0 = H0.inv()

    # induced metric and its Christoffels at 0 (x-dependent, then evaluate)
    Hix = Hx.inv()

    def Vg_x(k, l):
        A = Hix * k
        B = Hix * l
        return sp.trace(A * B) - sp.Rational(1, 2) * sp.trace(A) * sp.trace(B)

    gbar = sp.Matrix(DIM, DIM, lambda m, n: Hx[m, n] + Vg_x(dH[m], dH[n]))
    gbar0 = gbar.applyfunc(lambda e: sp.expand(e.subs({x: 0 for x in xs})))
    gbari0 = gbar0.inv()
    dgbar0 = [sp.Matrix(DIM, DIM, lambda m, n: sp.diff(gbar[m, n], xs[l]).subs({x: 0 for x in xs}))
              for l in range(DIM)]
    gbarGam0 = [[[sp.Rational(1, 2) * sum(gbari0[l, k] * (dgbar0[m][n, k] + dgbar0[n][m, k]
                 - dgbar0[k][m, n]) for k in range(DIM))
                 for n in range(DIM)] for m in range(DIM)] for l in range(DIM)]

    # tangents at 0: T_mu = (delta^rho_mu ; dH0[mu]_ab)
    # ambient Christoffels at fiber point H0 (ii-s Section 2):
    #   Ghor[rho][mu][ab-pair]  = (1/2) H^{rho l} delta^{ab}_{mu l}
    #   Gver_bb[ab-pair][mu][nu]= -(1/2)( H_{a(mu}H_{nu)b} - (1/2) H_ab H_mu nu )
    #   Gver_ff[ab][cd][ef]     = -(1/2)( E_cd Hi E_ef + E_ef Hi E_cd )_{ab}
    K = {}       # K[(m,n)] = (base 4-vector, fiber 4x4 symmetric matrix)
    for m in range(DIM):
        for n in range(m, DIM):
            # fiber part
            Mf = ddH0[m][n].copy()
            alg = sp.Matrix(DIM, DIM, lambda a, b:
                            sp.Rational(1, 2) * (H0[a, m] * H0[n, b] + H0[a, n] * H0[m, b])
                            - sp.Rational(1, 2) * H0[a, b] * H0[m, n])
            Mf = Mf - sp.Rational(1, 2) * alg
            Mf = Mf - sp.Rational(1, 2) * (dH0[m] * Hi0 * dH0[n] + dH0[n] * Hi0 * dH0[m])
            for l in range(DIM):
                Mf = Mf - gbarGam0[l][m][n] * dH0[l]
            # base part: Gamma^H(e_mu, dH_nu) + Gamma^H(e_nu, dH_mu) - gbarGam^rho_{mu nu},
            # with Gamma^H(u,k)^rho = (1/2) (H^{-1})^{rho l} k_{l u}  (ii-s Sec 2 mnemonic).
            base = []
            for rho in range(DIM):
                srho = sp.Rational(1, 2) * sum(Hi0[rho, l] * dH0[n][m, l] for l in range(DIM)) \
                    + sp.Rational(1, 2) * sum(Hi0[rho, l] * dH0[m][n, l] for l in range(DIM)) \
                    - gbarGam0[rho][m][n]
                base.append(sp.expand(srho))
            K[(m, n)] = K[(n, m)] = (base, Mf.applyfunc(sp.expand))

    def Vlow(kmat, lmat):
        A = Hi0 * kmat
        B = Hi0 * lmat
        return sp.trace(A * B) - sp.Rational(1, 2) * sp.trace(A) * sp.trace(B)

    def Gdot(K1, K2):
        b1, f1 = K1
        b2, f2 = K2
        s = sp.Integer(0)
        for r in range(DIM):
            for s2 in range(DIM):
                if H0[r, s2] != 0:
                    s += H0[r, s2] * b1[r] * b2[s2]
        s += Vlow(f1, f2)
        return s

    W = sp.Integer(0)
    for m in range(DIM):
        for n in range(DIM):
            for r in range(DIM):
                for s2 in range(DIM):
                    w = gbari0[m, r] * gbari0[n, s2]
                    if w == 0:
                        continue
                    W += w * Gdot(K[(m, n)], K[(r, s2)])
    return sp.nsimplify(sp.expand(W))


# ---- (a) potential-slice jets: fit in u = c/E0, cubic+quartic must vanish --
log("Route 2(a): MSS-type jets s = c*eta at assorted (E0, c); polynomial fit in u = c/E0 ...")
u = sp.Symbol('u', real=True)
fitpts = []
for E0v, cv in [(1, sp.Rational(1, 3)), (1, -sp.Rational(1, 2)), (2, 1), (2, -2),
                (sp.Rational(1, 3), sp.Rational(1, 5)), (3, sp.Rational(7, 2)), (1, 4)]:
    sv = {ij: (cv * eta[ij[0], ij[1]] if ij[0] == ij[1] else 0) for ij in pairs}
    Wv = route2_W(E0v, [0, 0, 0, 0], sv)
    fitpts.append((sp.Rational(cv, E0v), Wv))
uu = [pt[0] for pt in fitpts]
ww = [pt[1] for pt in fitpts]
# exact Lagrange interpolation through 5 points, then test the remaining 2
poly5 = sp.expand(sp.interpolate(list(zip(uu[:5], ww[:5])), u))
check("Route 2: degree of the exact interpolant through 5 MSS points is <= 2 "
      "(cubic AND quartic coefficients vanish identically)",
      sp.degree(poly5, u) <= 2, f"P(u) = {poly5}")
check("Route 2: the 2 held-out points fall ON the quadratic (7-point overdetermination)",
      all(sp.simplify(poly5.subs(u, uu[k]) - ww[k]) == 0 for k in [5, 6]))
# match against Route 1 on the same slice: sigma = u * eta -> R = -6 * tr_eta(u eta) = -24u?
W1_mss = sp.expand(W1s.subs({sig[ij]: (uu[0] * 0 + u * eta[ij[0], ij[1]] if ij[0] == ij[1] else 0)
                             for ij in pairs}))
check("CROSS-ROUTE: Route-2 quadratic == Route-1 W(sigma = u*eta) as polynomials in u "
      "(independent implementations agree EXACTLY)",
      sp.expand(poly5 - W1_mss) == 0, f"Route1 on MSS: {W1_mss}")

# ---- (b) a genuine dphi != 0 jet: normal-lift identity check ---------------
log("Route 2(b): dphi != 0 jet -- full-ambient vs vertical-representative+normal-lift ...")
vv = [0, sp.Rational(1, 3), 0, 0]
svnum = {(0, 0): sp.Rational(1, 2), (1, 1): -sp.Rational(1, 4), (2, 2): 1, (3, 3): sp.Rational(1, 5),
         (0, 1): sp.Rational(1, 7), (0, 2): 0, (0, 3): 0, (1, 2): -sp.Rational(1, 3), (1, 3): 0, (2, 3): sp.Rational(2, 5)}
W2_v = route2_W(1, vv, svnum)
W1_v = route1_W(with_v=True, vvals=vv, svals=svnum).subs(E0, 1)
check("CROSS-ROUTE at dphi != 0: full-ambient |II|^2 == normal-lift vertical-representative "
      "|II|^2 (validates the ii-s Section-5 normal identification on this sector)",
      sp.simplify(W2_v - W1_v) == 0, f"W = {sp.nsimplify(W2_v)}")

# ===========================================================================
# GRADIENT SECTOR (context, not load-bearing): the cubic/quartic-in-phi terms
# live ONLY in derivative structures, never in the potential.
# ===========================================================================
log()
log("=" * 78)
log("GRADIENT SECTOR -- where the beyond-quadratic terms actually live")
log("=" * 78)
vgen = sp.Symbol('vg', real=True)
Wgrad = route1_W(with_v=True, vvals=[0, vgen, 0, 0], svals={ij: 0 for ij in pairs})
Wgrad = sp.simplify(Wgrad)
Wser = sp.series(Wgrad.subs(E0, 1), vgen, 0, 6).removeO()
log(f"  W(|dphi|^2 only, s=0, E0=1):  {sp.simplify(Wgrad.subs(E0,1))}")
log(f"  expansion: {sp.expand(Wser)}")
check("Gradient sector: W depends on dphi (quartic and higher gradient terms EXIST) -- the "
      "beyond-quadratic content of |II|^2 is KINETIC-sector structure, not potential structure",
      sp.simplify(Wgrad.subs(E0, 1) - Wgrad.subs({E0: 1, vgen: 0})) != 0)
check("Gradient terms carry at least one derivative of phi: at dphi=0 they collapse back to "
      "the flat constant (2), so they contribute NOTHING to V(chi) at constant curvature "
      "(no vacuum-lifting channel)",
      sp.simplify(Wgrad.subs(vgen, 0).subs(E0, 1) - 2) == 0)

# ===========================================================================
# STAGE B -- vacuum analysis with the Stage-A result c_3 = 0 (exact).
# ===========================================================================
log()
log("=" * 78)
log("STAGE B -- scalaron effective potential: exact tree analysis + loop-c3 rescue test")
log("=" * 78)
R, gam, b, c, L = sp.symbols('R gamma b c Lambda', real=True)

# --- B1: tree level, EXACT: f = gamma R + b R^2 - 2 Lambda (c3 = 0 is now EXACT) ---
f = gam * R + b * R**2 - 2 * L
fp = sp.diff(f, R)
fpp = sp.diff(f, R, 2)
V = (R * fp - f) / (2 * fp**2)          # Einstein-frame potential as a function of R (M_P = 1 units)
dV = sp.simplify(sp.diff(V, R))
crit = sp.solve(sp.numer(sp.together(dV)), R)
check("B1: the ONLY finite critical point of V is R* = 4 Lambda / gamma (the dS/flat point); "
      "no second extremum exists at tree level -- NOTHING for the vacuum to shift to",
      crit == [4 * L / gam], f"critical set = {crit}")
m2_at = sp.simplify((sp.Rational(1, 3) * (fp / fpp - R)).subs(R, 4 * L / gam))
m2_flat = sp.simplify(m2_at.subs(L, 0))
check("B1 control: Lambda = 0 reproduces W122's m_0^2 = gamma/(6 b) exactly",
      sp.simplify(m2_flat - gam / (6 * b)) == 0, f"m0^2 = {m2_flat}")
# maximum vs minimum: at Lambda=0 the extremum is R*=0 and V''(0) = b exactly:
Vpp_flat = sp.simplify(sp.diff(V, R, 2).subs({R: 0, L: 0, gam: 1}))
check("B1: V''(flat point) = b exactly (gamma=1, Lambda=0 units): b < 0 on the AF "
      "trajectory makes the unique extremum a MAXIMUM of V -- the tachyonic top",
      sp.simplify(Vpp_flat - b) == 0, f"V''(0) = {Vpp_flat}")
# blunt numeric confirmation of MAX + runaway for a representative AF-branch point:
subsn = {gam: 1, b: -sp.Rational(1, 10), L: 0}
Vn = sp.lambdify(R, V.subs(subsn), 'math')
wall = 5.0                               # f' = 0 at R = -gamma/(2b) = +5
samples = [Vn(r) for r in [-3.0, -1.0, -0.3, 0.0, 0.3, 1.0, 3.0, 4.5, 4.9, 4.99]]
check("B1: RUNAWAY confirmed numerically on the positive-norm branch (f' > 0, R < -gamma/2b): "
      "V <= 0 everywhere, V(0) = 0 is the top, V -> -infinity at the f' -> 0 wall",
      samples[3] == 0.0 and samples[-1] < -100 and all(sv <= 0.0 for sv in samples),
      f"V near the wall (R=4.5, 4.9, 4.99): {[round(sv,2) for sv in samples[-3:]]}")
Vst = sp.lambdify(R, V.subs({gam: 1, b: +sp.Rational(1, 10), L: 0}), 'math')
check("B1 positive control (Starobinsky b > 0): V >= 0 with the MINIMUM at the flat point "
      "(healthy scalaron; the machinery distinguishes the two signs)",
      Vst(0.0) == 0.0 and all(Vst(r) > 0 for r in [-1.0, -0.3, 0.3, 1.0, 3.0]))

# --- B2: hypothetical LOOP-generated c R^3 (the only remaining source of f'' variation) ---
f3 = gam * R + b * R**2 + c * R**3 - 2 * L
fp3 = sp.diff(f3, R)
fpp3 = sp.diff(f3, R, 2)
trace3 = sp.expand(2 * f3 - R * fp3)     # dS condition: 2f = R f'
check("B2: dS condition with c R^3 and Lambda=0:  R (gamma - c R^2) = 0  ->  shifted vacua "
      "R* = +/- sqrt(gamma/c) exist iff c > 0",
      sp.expand(trace3.subs(L, 0) - (gam * R - c * R**3)) == 0)
Rstar = sp.sqrt(gam / c)
fpp_at = sp.expand(fpp3.subs(R, Rstar))          # 2b + 6 sqrt(gamma c)
fp_at = sp.expand(fp3.subs(R, Rstar))            # 4 gamma + 2 b sqrt(gamma/c)
# stability windows (b < 0, gamma > 0, c > 0):
bb, gg = sp.symbols('bb gg', positive=True)      # bb = |b|
fpp_cond = sp.solve(sp.Eq((-2 * bb + 6 * sp.sqrt(gg * c)).subs(gg, gam), 0), c)
check("B2: f''(R*) > 0 requires c > b^2/(9 gamma); but NO-GHOST (f'(R*) > 0) requires the "
      "STRONGER c > b^2/(4 gamma).  In between, the 'stabilized' vacuum is a GHOST vacuum "
      "(kinetic sign flipped): a maximum in disguise",
      sp.simplify(fpp_cond[0] - bb**2 / (9 * gam)) == 0
      and sp.simplify(sp.solve(sp.Eq((4 * gam - 2 * bb * sp.sqrt(gam / c)), 0), c)[0]
                      - bb**2 / (4 * gam)) == 0,
      "windows: ghost-vacuum (b^2/9g, b^2/4g); healthy only c > b^2/4g")
m2_shift = sp.simplify(sp.Rational(1, 3) * (fp3 / fpp3 - R)).subs(R, Rstar)
Lam_ind = Rstar / 4
log(f"  IF a healthy shifted minimum existed:  R* = sqrt(gamma/c),  induced Lambda_eff = R*/4,")
log(f"  re-expanded m^2(R*) = {sp.simplify(m2_shift)}")

# --- B3: EFT validity with the W46 AF numbers (mu_DW = 1 units) --------------
log()
log("B3: EFT validity of the rescue, with the actual W46 fixed-ratio data:")
b2coef = sp.Rational(133, 10) + sp.Rational(17, 12)
rquad = sp.Rational(5, 6) * u**2 + (5 + b2coef) * u + sp.Rational(5, 3)
roots = sp.solve(rquad, u)
roots = sorted([sp.nsimplify(r) for r in roots], key=lambda z: float(z))
check("B3 control: W46 ratio quadratic reproduced -- both roots real and NEGATIVE "
      "(r* ~ -23.575, -0.0848); f_2^2 > 0 on the AF branch => f_0^2 < 0 trajectory-wide",
      len(roots) == 2 and all(float(r) < 0 for r in roots),
      f"r* = {[float(r) for r in roots]}")
loop = 1 / (16 * sp.pi**2)
log("  Rescue needs c > b^2/(4 gamma) AND R* = sqrt(gamma/c) inside validity (R* << mu_DW^2 = 1).")
log("  But c is LOOP-GENERATED (Stage A: c_tree = 0 EXACTLY), so |c| <~ k * f^4 / (16 pi^2) in")
log("  mu_DW units with f^2 in {f_0^2, f_2^2} and k = O(1).  Then:")
for rstar_ratio, name in [(roots[1], "small root r* = -0.0848"), (roots[0], "large root r* = -23.575")]:
    f2sq = sp.Rational(1, 10)     # representative finite-scale f_2^2 > 0 (AF: 1/f_2^2 grows linearly)
    f0sq = rstar_ratio * f2sq
    gamma_n = 1                    # gamma = O(1) mu_DW^2 (H25; magnitude convention-flagged)
    c_needed = float((f0sq**2) / (4 * gamma_n))
    c_loop = float(loop * f2sq**2)          # most generous k=1, largest coupling
    Rstar_n = float(sp.sqrt(gamma_n / sp.Float(max(c_loop, 1e-300))))
    log(f"    [{name}]  c_needed = {c_needed:.3e},  c_loop <= {c_loop:.3e},  "
        f"R*(c_loop)/mu^2 = {Rstar_n:.3e}")
    if name.startswith("small"):
        small_ok = Rstar_n > 10     # far above the DeWitt scale
        ratio_small = c_loop / c_needed
    else:
        large_fail = c_loop < c_needed
        Rlarge = Rstar_n
check("B3: on the LARGE-root branch the rescue is parametrically IMPOSSIBLE "
      "(c_loop << c_needed by >= 4 orders) AND R* >> mu_DW^2",
      large_fail and Rlarge > 10)
check("B3: on the SMALL-root branch, even when c_loop ~ c_needed numerically, the shifted "
      "vacuum sits at R* = sqrt(gamma/c) >> mu_DW^2 -- OUTSIDE the validity of the induced-"
      "geometry derivative expansion.  An out-of-range minimum is NOT a rescue",
      small_ok, f"R*/mu^2 ~ {Rstar_n:.1e} on the most generous reading")

# ===========================================================================
# STAGE C -- the f''(R) statement.
# ===========================================================================
log()
log("=" * 78)
log("STAGE C -- f''(R): exact statement")
log("=" * 78)
check("C1: STAGE A => on the conformal potential sector the induced tree functional has "
      "f''(R) = 2 f_0^2 EXACTLY CONSTANT (all orders in phi): non-constant f'' does NOT "
      "arise from the induced |II|^2 geometry",
      polyW.total_degree() == 2)
check("C2: with f_0^2 < 0 trajectory-wide (W46/W119, reproduced above), the f(R) stability "
      "condition f'' > 0 FAILS at EVERY R -- there is no shifted minimum at which to "
      "re-test it.  W122's tachyon verdict STANDS, hardened from truncation-bounded to "
      "exact-at-tree", all(float(r) < 0 for r in roots))

log()
log("=" * 78)
if FAIL:
    log(f"FAILED ({len(FAIL)}): {FAIL}")
    raise SystemExit(1)
log("exit 0 = W126: the induced |II|^2 functional generates NO beyond-4th-order potential-")
log("sector invariants on the conformal family -- c_3 = c_4 = ... = 0 EXACTLY (two routes,")
log("all orders in phi).  The scalaron potential is exactly the W122 inverted structure:")
log("RUNAWAY, no vacuum shift, no Lambda shift.  A loop-generated R^3 rescue is ghost-")
log("infested in (b^2/9g, b^2/4g) and OUT-OF-VALIDITY beyond it on both W46 branches.")
log("W122's tachyon verdict: STANDS (hardened).")
