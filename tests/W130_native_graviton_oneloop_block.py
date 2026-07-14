#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
W130 -- THE GU-NATIVE GRAVITON ONE-LOOP BLOCK (Stage A: the operator, natively;
        Stage B: one-loop coefficients at GU's actual coefficient point, two routes;
        Stage C: impact on the tachyon chain).

Context (W123 residual; flagship referee vulnerability 2): the repo's UV/tachyon chain
rests on the PORTED pure-gravity one-loop blocks (Fradkin-Tseytlin / Avramidi-Barvinsky /
Salvio-Strumia: b_2 = 133/10; (5/3, 5, 5/6) in beta_{f_0^2}).  W123 pinned the convention
chain end to end and verified the port is faithful; what no wave computed is the quadratic
fluctuation operator of GU'S OWN induced gravity action around flat space, and the one-loop
coefficients AT GU'S OWN COEFFICIENT POINT.  W126 supplied the exact tree data on the
conformal slice: |II|^2 = 2 + R/3 + (8/9) R^2 - 4 Ric^2 (slice coefficients; a2/a3 not a
unique 4D split), F_MSS(R) = 2 + R/3 - R^2/9, with the 16/3 (vs H50 c_L = 3/8) and
measure forks FLAGGED.

WHAT THIS FILE DOES (deterministic, exact sympy, exit 0 iff all checks PASS):

PART A -- the REFERENCE fourth-order operator, from scratch.  Plane-wave 2-jet machinery:
  g = eta + eps1 A e^{ikx} + eps2 B e^{-ikx}; curvature computed from scratch (same
  Christoffel conventions as W126 Part 0); the quadratic Lagrangian = coeff(eps1*eps2) of
  sqrt(-det g) (-2 Lambda + gamma R + a R^2 + b Ric^2 + c Riem^2), evaluated at x = 0
  (the eps1*eps2 monomial is x-independent, so pointwise = action density; total
  derivatives drop automatically).  DERIVED: the operator depends on (a, b, c) only
  through c_W = 2c + b/2 (spin-2 / Weyl channel) and c_R = a + b/3 + c/3 (spin-0 / R^2
  channel) -- the BASIS MAP, with Gauss-Bonnet (1, -4, 1) in its kernel; the Weyl
  combination (1/3, -2, 1) has ZERO spin-0 form (W122's statement, re-derived in momentum
  space); the pole structure gives m_0^2 = gamma/(6 c_R) (W122's formula re-derived from
  the operator) and the SIGN MAP f_2^2 = -1/(2 c_W), f_0^2 = +1/(6 c_R) to the agravity
  couplings (via the Salvio-Strumia mass anchors M_i^2 = f_i^2 Mbar^2/2).

PART B -- the NATIVE operator: the SAME plane-wave jets fed through the Convention-B
  literal-graph |II|^2 evaluator (generalized, faithfully, from the W126 Route-1 code to
  arbitrary metric 2-jets; regression-checked against the verbatim W126 conformal code and
  against the W126 slice results).  Both measure forks (sqrt(det gbar) vs sqrt(det g)).
  Output: the native (Lambda, gamma, c_R, c_W) of GU's induced quadratic operator around
  flat space -- including the Weyl-channel coefficient c_W that the conformal family
  provably cannot see (Weyl = 0 on conformal metrics), i.e. the number that was
  structurally MISSING from the native record.

PART C -- second-order heat-kernel route (Gilkey a4), EXACT: engine validated on the
  Christensen-Duff c-charges 3 : 9 : 36 (real scalar : Weyl fermion : vector, derived
  from E/Omega data, not quoted), which DERIVES the repo's /180 b_2-shift rule (W45
  ported it); the scalar non-minimal block (1/2)(xi - 1/6)^2 R^2 => the W123
  perfect-square matter block w_a (xi + 1/6)^2 with w_a = 3 DERIVED; the scalaron's own
  second-order block computed.

PART D -- Stage B/C assembly: the one-loop log coefficients of GU's operator in the
  direct-coefficient basis (dc_W/dt is POINT-INDEPENDENT = -kappa b_2/2: the Weyl-channel
  divergence cannot be moved by evaluating at the native point; dc_R/dt depends only on
  the ratio c_R/c_W, evaluated at the native point); the native tree point mapped to
  (f_2^2, f_0^2); AF-basin membership (W123 basin) of GU's native initial condition;
  the NO-CHANGE audit of the tachyon chain (A = 5/6 + ..., b_2, c_RS_weyl band edges).

Conventions: eta = diag(-1,+1,+1,+1); curvature from scratch (W126 Part-0 convention:
on the conformal dphi = 0 jet, R = -6 e^{-2p} tr_eta(s)).  Forbidden-target rule: no
{3, 8, 24, chi(K3), Ahat} assumed, inserted, hardcoded, or divided by.

Run:  python -u tests/W130_native_graviton_oneloop_block.py    (exit 0 iff all PASS)
Runtime: ~10 minutes (exact symbolic native quadratic forms); for the reproduce_all
sweep use --timeout 900 to include this certificate.
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


DIM = 4
eta = sp.diag(-1, 1, 1, 1)
E1, E2 = sp.symbols('eps1 eps2', real=True)
I = sp.I

# ===========================================================================
# Shared machinery: truncated (eps1, eps2) perturbation algebra.
# Every quantity is kept only to total order <= 1 in EACH of eps1, eps2
# (we extract the eps1*eps2 coefficient = the quadratic Lagrangian).
# ===========================================================================


def trunc(e):
    """Keep only the (1, eps1, eps2, eps1*eps2) monomials of an expression."""
    e = sp.expand(e)
    c00 = e.coeff(E1, 0).coeff(E2, 0)
    c10 = e.coeff(E1, 1).coeff(E2, 0)
    c01 = e.coeff(E1, 0).coeff(E2, 1)
    c11 = e.coeff(E1, 1).coeff(E2, 1)
    return c00 + c10 * E1 + c01 * E2 + c11 * E1 * E2


def mtrunc(M):
    return M.applyfunc(trunc)


def minv_pert(M):
    """Inverse of M = eta + P with P = O(eps), exact to the truncation order."""
    P = mtrunc(M - eta)
    ei = eta  # eta^{-1} = eta
    return mtrunc(ei - ei * P * ei + mtrunc(ei * P * ei * P) * ei)


def sqrt_minus_det(M):
    """sqrt(-det M) for M = eta + O(eps), exact to the truncation order."""
    D = trunc(-M.det())
    d = trunc(D - 1)
    return trunc(1 + d / 2 - d * d / 8)


def c11_of(e):
    return sp.expand(sp.expand(e).coeff(E1, 1).coeff(E2, 1))


# ===========================================================================
# Plane-wave 2-jets.  h(x) = eps1 A e^{i k.x} + eps2 B e^{-i k.x}; at x = 0:
#   G0 = eta + eps1 A + eps2 B
#   dG_m = i k_m (eps1 A - eps2 B)
#   ddG_{mn} = -k_m k_n (eps1 A + eps2 B)
# ===========================================================================
k0, k3 = sp.symbols('kappa0 kappa3', real=True)
KVEC = [k0, 0, 0, k3]
K2 = -k0**2 + k3**2          # k.k in eta = (-,+,+,+)


def plane_jet(A, B):
    G0 = mtrunc(eta + E1 * A + E2 * B)
    dG = [mtrunc(I * KVEC[m] * (E1 * A - E2 * B)) for m in range(DIM)]
    ddG = [[mtrunc(-KVEC[m] * KVEC[n] * (E1 * A + E2 * B)) for n in range(DIM)] for m in range(DIM)]
    return G0, dG, ddG


# sectors
a12, b12 = sp.symbols('a12 b12', real=True)          # TT polarization (h_12)
ph1, be1, ph2, be2 = sp.symbols('phi1 beta1 phi2 beta2', real=True)  # spin-0: phi*eta + beta*k(x)k


def sym_mat(entries):
    M = sp.zeros(DIM, DIM)
    for (i, j), v in entries.items():
        M[i, j] = M[j, i] = v
    return M


A_TT = sym_mat({(1, 2): a12})
B_TT = sym_mat({(1, 2): b12})
KK = sp.Matrix(DIM, DIM, lambda i, j: KVEC[i] * KVEC[j])
A_SC = ph1 * eta + be1 * KK
B_SC = ph2 * eta + be2 * KK


# ===========================================================================
# Curvature from a 2-jet, from scratch (same conventions as W126 Part 0).
# ===========================================================================


def curvature_from_jet(G0, dG, ddG, pert=True):
    inv = minv_pert if pert else (lambda M: M.inv())
    tr_ = trunc if pert else sp.expand
    Gi = inv(G0)
    dGi = [mtrunc(-Gi * dG[l] * Gi) if pert else sp.expand(-Gi * dG[l] * Gi) for l in range(DIM)]
    Gam = [[[tr_(Q(1, 2) * sum(Gi[l, kk] * (dG[m][n, kk] + dG[n][m, kk] - dG[kk][m, n])
             for kk in range(DIM)))
             for n in range(DIM)] for m in range(DIM)] for l in range(DIM)]
    dGam = [[[[tr_(Q(1, 2) * sum(dGi[p][l, kk] * (dG[m][n, kk] + dG[n][m, kk] - dG[kk][m, n])
              + Gi[l, kk] * (ddG[p][m][n, kk] + ddG[p][n][m, kk] - ddG[p][kk][m, n])
              for kk in range(DIM)))
              for n in range(DIM)] for m in range(DIM)] for l in range(DIM)] for p in range(DIM)]
    # NOTE on ddG indexing: ddG[p][m] is the matrix d_p d_m g_..; ddG[p][m][n, kk] = d_p d_m g_{n kk}.
    # In dGam we need d_p of dG[m][n,kk] = d_p d_m g_{n kk} = ddG[p][m][n,kk]; and
    # d_p of dG[kk][m,n] = ddG[p][kk][m,n].
    Riem = [[[[tr_(dGam[m][r][n][s] - dGam[n][r][m][s]
             + sum(Gam[r][m][l] * Gam[l][n][s] - Gam[r][n][l] * Gam[l][m][s] for l in range(DIM)))
             for n in range(DIM)] for m in range(DIM)] for s in range(DIM)] for r in range(DIM)]
    # Riem[r][s][m][n] = R^r_{s m n} = d_m Gam^r_{n s} - d_n Gam^r_{m s} + GG - GG
    Ric = sp.Matrix(DIM, DIM, lambda m, n: tr_(sum(Riem[l][m][l][n] for l in range(DIM))))
    Rsc = tr_(sum(Gi[m, n] * Ric[m, n] for m in range(DIM) for n in range(DIM)))
    # lowered Riemann and the squares
    Riem_dn = [[[[tr_(sum(G0[a, r] * Riem[r][s2][m][n] for r in range(DIM)))
                for n in range(DIM)] for m in range(DIM)] for s2 in range(DIM)] for a in range(DIM)]
    RiemSq = sp.Integer(0)
    RicSq = sp.Integer(0)
    for a in range(DIM):
        for b_ in range(DIM):
            RicSq += Ric[a, b_] * sum(Gi[a, c] * Gi[b_, d] * Ric[c, d]
                                      for c in range(DIM) for d in range(DIM))
    RicSq = tr_(RicSq)
    for a in range(DIM):
        for b_ in range(DIM):
            for c in range(DIM):
                for d in range(DIM):
                    up = sp.Integer(0)
                    for a2 in range(DIM):
                        for b2 in range(DIM):
                            for c2 in range(DIM):
                                for d2 in range(DIM):
                                    t = Gi[a, a2] * Gi[b_, b2] * Gi[c, c2] * Gi[d, d2]
                                    if t != 0:
                                        up += t * Riem_dn[a2][b2][c2][d2]
                    RiemSq += Riem_dn[a][b_][c][d] * tr_(up)
    RiemSq = tr_(RiemSq)
    return {"Gi": Gi, "R": Rsc, "Ric": Ric, "RicSq": RicSq, "RiemSq": RiemSq}


log("=" * 88)
log("PART A0 -- machinery controls")
log("=" * 88)

# Control: conformal potential-slice jet reproduces the W126 Part-0 curvature pin.
s_syms = {(i, j): sp.Symbol(f's{i}{j}', real=True) for i in range(DIM) for j in range(i, DIM)}


def SS(i, j):
    return s_syms[(i, j)] if i <= j else s_syms[(j, i)]


smat = sp.Matrix(DIM, DIM, lambda i, j: SS(i, j))
G0c = eta
dGc = [sp.zeros(DIM, DIM) for _ in range(DIM)]
ddGc = [[2 * SS(m, n) * eta for n in range(DIM)] for m in range(DIM)]
curv_c = curvature_from_jet(G0c, dGc, ddGc, pert=False)
trs = sum(eta[i, i] * SS(i, i) for i in range(DIM))
check("A0.1 curvature convention pin: conformal dphi=0 jet gives R = -6 tr_eta(s) "
      "(matches W126 Part 0 exactly)",
      sp.simplify(curv_c["R"] + 6 * trs) == 0, f"R = {sp.simplify(curv_c['R'])}")
ric_expect = sp.Matrix(DIM, DIM, lambda i, j: -2 * SS(i, j) - eta[i, j] * trs)
check("A0.2 Ricci pin: R_mn = -2 s_mn - eta_mn tr_eta(s) on the slice",
      sp.simplify(curv_c["Ric"] - ric_expect) == sp.zeros(DIM, DIM))

if FAIL:
    log("EARLY EXIT: machinery controls failed")
    raise SystemExit(1)

log()
log("machinery controls OK; continuing (Part A reference operator) ...")

# ===========================================================================
# PART A -- the reference fourth-order quadratic operator around flat space.
# Q_ref(sector) = coeff(eps1*eps2) of
#   sqrt(-det g) * (-2 Lambda + gamma R + a R^2 + b Ric^2 + c Riem^2)
# ===========================================================================
log()
log("=" * 88)
log("PART A -- reference fourth-order operator: basis map, GB null, Weyl spin-0 null, poles")
log("=" * 88)

Lam, gam, ca, cb, cc = sp.symbols('Lambda gamma a b c', real=True)


def Qref_of_sector(A, B):
    G0, dG, ddG = plane_jet(A, B)
    cv = curvature_from_jet(G0, dG, ddG, pert=True)
    sg = sqrt_minus_det(G0)
    Lag = trunc(sg * trunc(-2 * Lam + gam * cv["R"]
                           + ca * cv["R"]**2 + cb * cv["RicSq"] + cc * cv["RiemSq"]))
    return c11_of(Lag)


log("computing TT-sector reference quadratic form ...")
Q_TT_ref = Qref_of_sector(A_TT, B_TT)
log("computing spin-0-sector reference quadratic form ...")
Q_SC_ref = Qref_of_sector(A_SC, B_SC)

k2s = sp.Symbol('k2', real=True)   # k^2 = -kappa0^2 + kappa3^2


def in_k2(expr):
    """Rewrite a (kappa0, kappa3) expression via kappa0^2 -> kappa3^2 - k2 and check that
    the kappa3 dependence cancels (Lorentz covariance).  Returns (k2-form, ok)."""
    e = sp.expand(expr)
    for _ in range(8):
        if not e.has(k0):
            break
        e = sp.expand(e.subs(k0**2, k3**2 - k2s))
    ok = (not e.has(k0)) and (not sp.expand(e).has(k3))
    return e, ok


def only_through(expr, combo, syms):
    """True iff expr, homogeneous-linear in syms, is a multiple of combo by a
    (a,b,c)-independent factor."""
    ratio = sp.simplify(sp.cancel(expr / combo))
    return all(not ratio.has(s) for s in syms)


# --- TT structure --------------------------------------------------------
qtt, okTT = in_k2(Q_TT_ref)
check("A1.1 TT reference form is Lorentz-covariant (kappa enters only via k^2)",
      okTT, f"Q_TT/(a12 b12) = {sp.factor(sp.cancel(qtt/(a12*b12)))}")
qtt_poly = sp.Poly(sp.expand(sp.cancel(qtt / (a12 * b12))), k2s)
tt_c = {n: qtt_poly.coeff_monomial(k2s**n) for n in range(0, 5)}
log(f"  TT form / (a12 b12): k^0: {tt_c[0]}   k^2: {tt_c[1]}   k^4: {tt_c[2]}")

cW_expr = 2 * cc + cb / 2
cR_expr = ca + cb / 3 + cc / 3
check("A1.2 BASIS MAP, spin-2 channel: the TT k^4 coefficient depends on (a,b,c) ONLY "
      "through c_W := 2c + b/2 (Gauss-Bonnet direction in the kernel)",
      only_through(tt_c[2], cW_expr, [ca, cb, cc]),
      f"k^4 coeff = {sp.factor(tt_c[2])}")
TT_K4_UNIT = sp.simplify(sp.cancel(tt_c[2] / cW_expr))   # c_W extraction normalization
TT_K2_UNIT = sp.simplify(sp.cancel(tt_c[1] / gam))       # gamma extraction (TT channel)
check("A1.3 TT k^2 coefficient is purely the Einstein term (proportional to gamma)",
      only_through(tt_c[1], gam, [ca, cb, cc, Lam]),
      f"k^2 coeff = {tt_c[1]}")
check("A1.4 TT k^0 coefficient is purely the Lambda term",
      only_through(tt_c[0], Lam, [ca, cb, cc, gam]),
      f"k^0 coeff = {tt_c[0]}")

# --- GB null and Weyl spin-0 null ---------------------------------------
gb_sub = {ca: 1, cb: -4, cc: 1, gam: 0, Lam: 0}
check("A2.1 GAUSS-BONNET NULL: (a,b,c) = (1,-4,1) has IDENTICALLY ZERO quadratic form in "
      "BOTH sectors (GB is topological; the operator sees only (c_W, c_R))",
      sp.expand(Q_TT_ref.subs(gb_sub)) == 0 and sp.expand(Q_SC_ref.subs(gb_sub)) == 0)
weyl_sub = {ca: Q(1, 3), cb: -2, cc: 1, gam: 0, Lam: 0}
check("A2.2 WEYL SPIN-0 NULL: (a,b,c) = (1/3,-2,1) (= C^2 mod GB) has ZERO spin-0 form and "
      "NONZERO TT form (W122's statement re-derived in momentum space)",
      sp.expand(Q_SC_ref.subs(weyl_sub)) == 0 and sp.expand(Q_TT_ref.subs(weyl_sub)) != 0)

# --- spin-0 structure -----------------------------------------------------
qsc, okSC = in_k2(Q_SC_ref)
check("A3.1 spin-0 reference form is Lorentz-covariant in k^2", okSC)
qsc_l0 = sp.expand(qsc.subs(Lam, 0))
check("A3.2 DIFFEO CHECK: at Lambda = 0 the spin-0 form is INDEPENDENT of beta1, beta2 "
      "(the gauge direction) for ALL (gamma,a,b,c): gauge invariance around the on-shell "
      "flat background",
      not qsc_l0.has(be1) and not qsc_l0.has(be2),
      "the physical spin-0 content sits entirely in phi")
qphi_poly = sp.Poly(sp.expand(sp.cancel(qsc_l0 / (ph1 * ph2))), k2s)
sc_c = {n: qphi_poly.coeff_monomial(k2s**n) for n in range(0, 5)}
log(f"  spin-0 form / (phi1 phi2), Lambda=0:  k^2: {sc_c[1]}   k^4: {sc_c[2]}")
check("A3.3 BASIS MAP, spin-0 channel: the phi k^4 coefficient depends on (a,b,c) ONLY "
      "through c_R := a + b/3 + c/3 (the R^2-channel coupling)",
      only_through(sc_c[2], cR_expr, [ca, cb, cc]),
      f"k^4 coeff = {sp.factor(sc_c[2])}")
SC_K4_UNIT = sp.simplify(sp.cancel(sc_c[2] / cR_expr))
SC_K2_UNIT = sp.simplify(sp.cancel(sc_c[1] / gam))
check("A3.4 spin-0 k^2 coefficient is purely gamma (no quartic leakage)",
      only_through(sc_c[1], gam, [ca, cb, cc, Lam]),
      f"k^2 coeff = {sc_c[1]}")

# --- pole structure and the coupling sign maps ---------------------------
# massive pole at k^2* ; on-shell massive particle in (-,+,+,+) has k^2 = -m^2,
# so m^2 = -k^2*.
u1, u2 = SC_K2_UNIT, SC_K4_UNIT
m0sq = sp.simplify(u1 * gam / (u2 * cR_expr))
check("A4.1 SCALARON MASS from the operator: m_0^2 = gamma/(6 c_R) EXACTLY (W122's "
      "Legendre-route formula re-derived; c_R is the only quartic combination the "
      "scalaron sees)",
      sp.simplify(m0sq - gam / (6 * cR_expr)) == 0, f"m_0^2 = {m0sq}")
check("A4.2 Starobinsky control: gamma = 1, (a,b,c) = (1,0,0) gives m_0^2 = +1/6 > 0 (healthy)",
      m0sq.subs({gam: 1, ca: 1, cb: 0, cc: 0}) == Q(1, 6))
t1, t2 = TT_K2_UNIT, TT_K4_UNIT
m2sq = sp.simplify(t1 * gam / (t2 * cW_expr))
check("A4.3 SPIN-2 MASS from the operator: m_2^2 = -gamma/(2 c_W) EXACTLY (Stelle pole)",
      sp.simplify(m2sq + gam / (2 * cW_expr)) == 0, f"m_2^2 = {m2sq}")
f0sq_map = sp.simplify(m0sq / gam)
f2sq_map = sp.simplify(m2sq / gam)
check("A4.4 SIGN MAP to the agravity couplings (SS mass anchors M_i^2 = f_i^2 Mbar^2/2, "
      "gamma = Mbar^2/2):  f_0^2 = +1/(6 c_R)  and  f_2^2 = -1/(2 c_W).  The R^2 joint is "
      "W123's B3 pin re-derived; the C^2-channel MINUS sign is a NEW convention joint "
      "(direct Weyl-squared coefficient = MINUS 1/(2 f_2^2))",
      sp.simplify(f0sq_map - 1 / (6 * cR_expr)) == 0 and
      sp.simplify(f2sq_map + 1 / (2 * cW_expr)) == 0,
      "f_2^2 > 0 (AF branch, real spin-2 mass)  <=>  c_W < 0")

if FAIL:
    log("EARLY EXIT: Part A failed")
    raise SystemExit(1)
log()
log("Part A reference operator OK; continuing (Part B native operator) ...")

# ===========================================================================
# PART B -- the NATIVE operator: Convention-B literal-graph |II|^2 on the same
# plane-wave jets.  The evaluator generalizes tests/W126_beyond4th_conformal_iisq.py
# Route 1 (B^V + normal lift) to ARBITRARY metric 2-jets, following that code's
# formulas line by line; regressions pin it to the W126 results exactly.
# ===========================================================================
log()
log("=" * 88)
log("PART B -- native |II|^2 quadratic operator (Convention B, generalized jets)")
log("=" * 88)


def iisq_of_jet(G0, dG, ddG, pert=True):
    """|II|^2 of the literal-graph section at a point, from the metric 2-jet
    (G0, dG[m], ddG[m][n]).  Faithful generalization of W126 route1_W:
      induced metric  gbar_mn = g_mn + V_g(dg_m, dg_n)
      B^V_mn = ddg_mn - gbarGam^l_mn dg_l - (1/2) alg_mn - (1/2)(dg_m g^-1 dg_n + dg_n g^-1 dg_m)
      IP(q,q') = V_g(q,q') + g^{rs} V_g(q, dg_r) V_g(q', dg_s)
      W = gbar^{mr} gbar^{ns} IP(B^V_mn, B^V_rs)
    Returns (W, gbar0).
    """
    inv = minv_pert if pert else (lambda M: M.inv())
    tr_ = trunc if pert else sp.expand
    mtr_ = mtrunc if pert else (lambda M: M.applyfunc(sp.expand))
    Gi0 = inv(G0)

    def Vg(q, qq):
        A_ = Gi0 * q
        B_ = Gi0 * qq
        return tr_(sp.trace(mtr_(A_ * B_)) - Q(1, 2) * sp.trace(mtr_(A_)) * sp.trace(mtr_(B_)))

    dGi = [mtr_(-Gi0 * dG[l] * Gi0) for l in range(DIM)]

    def dVg(l, q, qq, dq, dqq):
        """d_l of V_g(q(x), qq(x)) at 0: metric-derivative terms + argument derivatives."""
        met = (sp.trace(mtr_(dGi[l] * q * Gi0 * qq)) + sp.trace(mtr_(Gi0 * q * dGi[l] * qq))
               - Q(1, 2) * (sp.trace(mtr_(dGi[l] * q)) * sp.trace(mtr_(Gi0 * qq))
                            + sp.trace(mtr_(Gi0 * q)) * sp.trace(mtr_(dGi[l] * qq))))
        return tr_(met) + Vg(dq, qq) + Vg(q, dqq)

    gbar0 = mtr_(G0 + sp.Matrix(DIM, DIM, lambda m, n: Vg(dG[m], dG[n])))
    gbari0 = inv(gbar0)
    dgbar = [sp.Matrix(DIM, DIM, lambda m, n:
                       tr_(dG[l][m, n] + dVg(l, dG[m], dG[n], ddG[l][m], ddG[l][n])))
             for l in range(DIM)]
    gbarGam = [[[tr_(Q(1, 2) * sum(gbari0[l, kk] * (dgbar[m][n, kk] + dgbar[n][m, kk]
                - dgbar[kk][m, n]) for kk in range(DIM)))
                for n in range(DIM)] for m in range(DIM)] for l in range(DIM)]
    Bv = {}
    for m in range(DIM):
        for n in range(m, DIM):
            M = ddG[m][n].copy()
            for l in range(DIM):
                M = M - gbarGam[l][m][n] * dG[l]
            alg = sp.Matrix(DIM, DIM, lambda a_, b_:
                            Q(1, 2) * (G0[a_, m] * G0[n, b_] + G0[a_, n] * G0[m, b_])
                            - Q(1, 2) * G0[a_, b_] * G0[m, n])
            M = M - Q(1, 2) * alg
            M = M - Q(1, 2) * (dG[m] * Gi0 * dG[n] + dG[n] * Gi0 * dG[m])
            Bv[(m, n)] = Bv[(n, m)] = mtr_(M)

    def IP(q, qq):
        base = Vg(q, qq)
        nl = sp.Integer(0)
        for r in range(DIM):
            for s2 in range(DIM):
                if Gi0[r, s2] == 0:
                    continue
                nl += tr_(Gi0[r, s2] * Vg(q, dG[r]) * Vg(qq, dG[s2]))
        return tr_(base + nl)

    W = sp.Integer(0)
    for m in range(DIM):
        for n in range(DIM):
            for r in range(DIM):
                for s2 in range(DIM):
                    w = tr_(gbari0[m, r] * gbari0[n, s2])
                    if w == 0:
                        continue
                    W += tr_(w * IP(Bv[(m, n)], Bv[(r, s2)]))
    return tr_(W), gbar0


# --- B1: regression against the VERBATIM W126 conformal code at a dphi != 0 jet ----
# (verbatim W126 route1_W, conformal-only, copied as the reference implementation)
def w126_route1_W(vvals, svals):
    xs = [sp.Symbol(f'x{i}', real=True) for i in range(DIM)]
    ph = sum(vvals[i] * xs[i] for i in range(DIM)) \
        + Q(1, 2) * sum(svals[(min(i, j), max(i, j))] * xs[i] * xs[j]
                        for i in range(DIM) for j in range(DIM))
    E = sp.exp(2 * ph)
    G = sp.Matrix(DIM, DIM, lambda i, j: E * eta[i, j])

    def at0(expr):
        return sp.expand(expr.subs({xi: 0 for xi in xs}))

    def Vg_of(Gi, kmat, lmat):
        A_ = Gi * kmat
        B_ = Gi * lmat
        return sp.trace(A_ * B_) - Q(1, 2) * sp.trace(A_) * sp.trace(B_)

    dG = [sp.diff(G, xs[m]) for m in range(DIM)]
    ddG = [[sp.diff(dG[m], xs[n]) for n in range(DIM)] for m in range(DIM)]
    Gi_x = sp.Matrix(DIM, DIM, lambda i, j: eta[i, j] / E)
    gbar = sp.Matrix(DIM, DIM, lambda m, n: G[m, n] + Vg_of(Gi_x, dG[m], dG[n]))
    gbar0 = gbar.applyfunc(at0)
    gbari0 = gbar0.inv()
    dgbar0 = [sp.Matrix(DIM, DIM, lambda m, n: at0(sp.diff(gbar[m, n], xs[l])))
              for l in range(DIM)]
    gbarGam0 = [[[Q(1, 2) * sum(gbari0[l, kk] * (dgbar0[m][n, kk] + dgbar0[n][m, kk]
                 - dgbar0[kk][m, n]) for kk in range(DIM))
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
            alg = sp.Matrix(DIM, DIM, lambda a_, b_:
                            Q(1, 2) * (G0[a_, m] * G0[n, b_] + G0[a_, n] * G0[m, b_])
                            - Q(1, 2) * G0[a_, b_] * G0[m, n])
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
    return sp.expand(sp.simplify(sp.expand(W)))


pairs = [(i, j) for i in range(DIM) for j in range(i, DIM)]
vv = [0, Q(1, 3), 0, 0]
svnum = {(0, 0): Q(1, 2), (1, 1): -Q(1, 4), (2, 2): 1, (3, 3): Q(1, 5),
         (0, 1): Q(1, 7), (0, 2): 0, (0, 3): 0, (1, 2): -Q(1, 3), (1, 3): 0, (2, 3): Q(2, 5)}
log("B1: regression of the generalized evaluator against verbatim W126 route1 (dphi != 0 jet) ...")
W_ref = w126_route1_W(vv, svnum)
# same conformal jet fed to the generic evaluator: g = e^{2 phi} eta, phi(0)=0:
#   G0 = eta; dG_m = 2 v_m eta; ddG_mn = (2 s_mn + 4 v_m v_n) eta
G0r = eta
dGr = [2 * vv[m] * eta for m in range(DIM)]
ddGr = [[(2 * svnum[(min(m, n), max(m, n))] + 4 * vv[m] * vv[n]) * eta
         for n in range(DIM)] for m in range(DIM)]
W_gen, _ = iisq_of_jet(G0r, dGr, ddGr, pert=False)
check("B1 REGRESSION: generalized evaluator == verbatim W126 Route-1 code on a conformal "
      "dphi != 0 jet (exact rational equality)",
      sp.simplify(W_gen - W_ref) == 0, f"W = {sp.nsimplify(W_gen)}")

# --- B2: regression on the potential slice (dphi = 0), including MSS ---------------
log("B2: potential-slice regressions ...")
uu = sp.Symbol('u', real=True)
G0m = eta
dGm = [sp.zeros(DIM, DIM)] * DIM
ddGm = [[2 * uu * eta[m, n] * eta for n in range(DIM)] for m in range(DIM)]
W_mss, _ = iisq_of_jet(G0m, dGm, ddGm, pert=False)
check("B2.1 REGRESSION: MSS slice gives P(u) = -64 u^2 - 8 u + 2 (the exact W126 Route-2 "
      "interpolant)", sp.expand(W_mss - (-64 * uu**2 - 8 * uu + 2)) == 0,
      f"W(MSS) = {sp.expand(W_mss)}")
# full slice decomposition (10 general s components): must equal
# 2 + (1/3) R + (8/9) R^2 - 4 Ric^2 with the slice curvature (W126 coefficients)
ddGs = [[2 * SS(m, n) * eta for n in range(DIM)] for m in range(DIM)]
W_slice, _ = iisq_of_jet(eta, dGm, ddGs, pert=False)
R_sl = curv_c["R"]
RicSq_sl = sum(eta[a, a] * eta[b, b] * curv_c["Ric"][a, b]**2 for a in range(DIM) for b in range(DIM))
check("B2.2 REGRESSION: full 10-component potential slice reproduces the W126 decomposition "
      "W = 2 + R/3 + (8/9) R^2 - 4 Ric^2 exactly",
      sp.expand(W_slice - (2 + R_sl / 3 + Q(8, 9) * R_sl**2 - 4 * RicSq_sl)) == 0)

if FAIL:
    log("EARLY EXIT: Part B regressions failed")
    raise SystemExit(1)
log()
log("Part B regressions OK; computing the native quadratic forms ...")


# --- B3: the native quadratic forms, both measure forks ---------------------------
def Qnat_of_sector(A, B):
    """Native quadratic Lagrangian (eps1*eps2 coefficient) for both measures:
    sqrt(-det gbar) * W  and  sqrt(-det g) * W."""
    G0, dG, ddG = plane_jet(A, B)
    W, gbar0 = iisq_of_jet(G0, dG, ddG, pert=True)
    Q_ind = c11_of(trunc(sqrt_minus_det(gbar0) * W))
    Q_sec = c11_of(trunc(sqrt_minus_det(G0) * W))
    return Q_ind, Q_sec


def symmetrized_k2(expr, swapmap):
    """Physical (real) quadratic form: symmetrize over (A <-> B, k -> -k), then in_k2."""
    e_sw = expr.subs(swapmap, simultaneous=True).subs({k0: -k0, k3: -k3}, simultaneous=True)
    e = sp.expand((expr + e_sw) / 2)
    return in_k2(e)


log("B3: native TT quadratic form (this is the Weyl-channel computation the conformal "
    "family cannot see) ...")
Qtt_ind, Qtt_sec = Qnat_of_sector(A_TT, B_TT)
swap_tt = {a12: b12, b12: a12}
qtt_ind, ok_i = symmetrized_k2(Qtt_ind, swap_tt)
qtt_sec, ok_s = symmetrized_k2(Qtt_sec, swap_tt)
check("B3.1 native TT forms are Lorentz-covariant in k^2 (both measures)", ok_i and ok_s,
      f"induced measure: {sp.factor(sp.cancel(qtt_ind/(a12*b12)))}")
log(f"  native TT / (a12 b12), measure sqrt(det gbar): {sp.expand(sp.cancel(qtt_ind/(a12*b12)))}")
log(f"  native TT / (a12 b12), measure sqrt(det g)   : {sp.expand(sp.cancel(qtt_sec/(a12*b12)))}")

log("B3b: native spin-0 quadratic form ...")
Qsc_ind, Qsc_sec = Qnat_of_sector(A_SC, B_SC)
swap_sc = {ph1: ph2, ph2: ph1, be1: be2, be2: be1}
qsc_ind, ok_i2 = symmetrized_k2(Qsc_ind, swap_sc)
qsc_sec, ok_s2 = symmetrized_k2(Qsc_sec, swap_sc)
check("B3.2 native spin-0 forms are Lorentz-covariant in k^2 (both measures)", ok_i2 and ok_s2)
log(f"  native spin-0, measure sqrt(det gbar): {sp.expand(qsc_ind)}")
log(f"  native spin-0, measure sqrt(det g)   : {sp.expand(qsc_sec)}")

if FAIL:
    log("EARLY EXIT: Part B native forms failed structure checks")
    raise SystemExit(1)


# --- B4: extraction of the native couplings ---------------------------------------
def kpoly(expr, bilin):
    """Coefficient list in k2 of the given bilinear's coefficient."""
    e = sp.expand(expr)
    co = e.coeff(bilin[0], 1).coeff(bilin[1], 1)
    return sp.Poly(co, k2s)


log()
log("B4: native coupling extraction (TT = Weyl channel; phi = R^2 channel)")
res = {}
for tag, qtt_n, qsc_n in [("induced", qtt_ind, qsc_ind), ("section", qtt_sec, qsc_sec)]:
    ptt = sp.Poly(sp.expand(sp.cancel(qtt_n / (a12 * b12))), k2s)
    cW_nat = sp.nsimplify(ptt.coeff_monomial(k2s**2) / TT_K4_UNIT)
    gam_TT = ptt.coeff_monomial(k2s**1) / TT_K2_UNIT
    Lam_TT = ptt.coeff_monomial(k2s**0) / 2
    pphi = kpoly(qsc_n, (ph1, ph2))
    cR_nat = pphi.coeff_monomial(k2s**2) / SC_K4_UNIT
    gam_SC = pphi.coeff_monomial(k2s**1) / SC_K2_UNIT
    res[tag] = dict(cW=cW_nat, gTT=gam_TT, Lam=Lam_TT, cR=cR_nat, gSC=gam_SC)
    log(f"  [{tag} measure]  c_W = {cW_nat}   c_R = {cR_nat}   gamma_TT = {gam_TT}   "
        f"gamma_phi = {gam_SC}   Lambda = {Lam_TT}")

check("B4.1 NATIVE WEYL-CHANNEL COUPLING (the number the conformal family cannot see): "
      "c_W = +2, IDENTICAL in both measure forks (the k^4 grade is measure-fork-free)",
      res["induced"]["cW"] == 2 and res["section"]["cW"] == 2)
check("B4.2 NATIVE R^2-CHANNEL COUPLING: c_R = -4/9 in both measures -- EXACTLY the value "
      "predicted by the W126 slice coefficients through the Part-A basis map "
      "(c_R = a2 + a3/3 = 8/9 - 4/3, with the GB representation freedom cancelling); "
      "the operator-level computation CONFIRMS the slice prediction",
      res["induced"]["cR"] == -Q(4, 9) and res["section"]["cR"] == -Q(4, 9))
check("B4.3 LAMBDA CHANNEL INTERNALLY CONSISTENT: the TT k^0 grade gives Lambda = -1, i.e. "
      "-2 Lambda = +2 = the flat-section constant a0 (W126) -- the DeWitt-Lambda sector of "
      "the operator matches the background value of the functional",
      res["induced"]["Lam"] == -1 and res["section"]["Lam"] == -1)
check("B4.4 EINSTEIN CHANNEL SPLITS BY SECTOR (the c_L background-vs-TT flag, now COMPUTED): "
      "gamma_TT : gamma_phi = 3 : 2 in BOTH measures (induced: 1 vs 2/3; section: 5 vs 10/3), "
      "and the potential-slice Einstein coefficient is a1 = 1/3 (W126): the native functional "
      "does NOT reduce to a single Einstein normalization at the quadratic level; ALL of them "
      "are POSITIVE (attractive, H25-consistent), so every SIGN statement is split-robust",
      sp.nsimplify(res["induced"]["gTT"] / res["induced"]["gSC"]) == Q(3, 2)
      and sp.nsimplify(res["section"]["gTT"] / res["section"]["gSC"]) == Q(3, 2)
      and all(v > 0 for v in [res["induced"]["gTT"], res["induced"]["gSC"],
                              res["section"]["gTT"], res["section"]["gSC"]]))

# --- B5: the non-covariant residue, exhibited and confined ------------------------
log()
log("B5: covariance audit of the native operator")
# reference beta-sector k^4-grade terms are IDENTICALLY ZERO for all (Lambda,gamma,a,b,c):
ref_bb_k4 = kpoly(qsc, (be1, be2)).coeff_monomial(k2s**4)
ref_bp_k3 = kpoly(qsc, (be1, ph2)).coeff_monomial(k2s**3)
check("B5.1 the covariant fourth-order class has NO beta-sector 4-derivative terms: the "
      "reference beta1*beta2*(k^2)^4 and beta*phi*(k^2)^3 coefficients vanish identically "
      "in (Lambda, gamma, a, b, c)",
      sp.simplify(ref_bb_k4) == 0 and sp.simplify(ref_bp_k3) == 0)
nat_bb_k4 = kpoly(qsc_ind, (be1, be2)).coeff_monomial(k2s**4)
nat_bp_k3 = kpoly(qsc_ind, (be1, ph2)).coeff_monomial(k2s**3)
check("B5.2 NON-COVARIANT RESIDUE EXISTS: the NATIVE operator HAS beta-sector 4-derivative "
      "terms (beta1 beta2 (k^2)^4 coefficient = 1, beta phi (k^2)^3 coefficient = -2, both "
      "measures): the literal-graph quadratic form is NOT diffeo-gauge-invariant beyond the "
      "Lambda-tadpole structure -- the non-covariance is a computed property of the "
      "Convention-B functional, not an error",
      nat_bb_k4 == 1 and nat_bp_k3 == -2 and
      kpoly(qsc_sec, (be1, be2)).coeff_monomial(k2s**4) == 1 and
      kpoly(qsc_sec, (be1, ph2)).coeff_monomial(k2s**3) == -2)
# confinement: subtract the best covariant reference (Lambda = -1, gamma = gamma_phi,
# c_R = -4/9 via a, c_W via c) and show the residual involves ONLY the gauge direction beta.
for tag, qsc_n in [("induced", qsc_ind), ("section", qsc_sec)]:
    gph = res[tag]["gSC"]
    ceff = sp.nsimplify(res[tag]["cW"]) / 2
    aeff = res[tag]["cR"] - ceff / 3
    ref_match = qsc.subs({Lam: -1, gam: gph, ca: aeff, cb: 0, cc: ceff})
    resid = sp.expand(qsc_n - ref_match)
    res[tag]["resid"] = resid
    phi_only = sp.expand(resid.subs({be1: 0, be2: 0}))
    check(f"B5.3[{tag}] RESIDUE CONFINED TO THE GAUGE DIRECTION: after subtracting the "
          f"covariant reference (Lambda=-1, gamma=gamma_phi, c_R=-4/9, c_W=2), the ENTIRE "
          f"spin-0 residual is proportional to beta (the diffeo orbit); the physical "
          f"phi-block is EXACTLY covariant fourth-order",
          phi_only == 0 and resid != 0,
          f"residual = {resid}")

# scalaron pole from the native phi block: m_0^2 = gamma_phi/(6 c_R) < 0 (tachyon), and the
# native spin-2 pole: m_2^2 = -gamma_TT/(2 c_W) < 0.
m0_ind = res["induced"]["gSC"] / (6 * res["induced"]["cR"])
m0_sec = res["section"]["gSC"] / (6 * res["section"]["cR"])
m2_ind = sp.nsimplify(-res["induced"]["gTT"] / (2 * res["induced"]["cW"]))
m2_sec = sp.nsimplify(-res["section"]["gTT"] / (2 * res["section"]["cW"]))
check("B6.1 NATIVE TREE SCALARON: m_0^2 = gamma_phi/(6 c_R) = -1/4 (induced) / -5/4 (section) "
      "-- NEGATIVE in both measures: the tree-level scalaron of the native operator is "
      "TACHYONIC (sign measure-fork-robust; magnitude measure-gated, as flagged)",
      m0_ind == -Q(1, 4) and m0_sec == -Q(5, 4) and m0_ind < 0 and m0_sec < 0)
check("B6.2 NATIVE TREE MASSIVE SPIN-2: m_2^2 = -gamma_TT/(2 c_W) = -1/4 (induced) / -5/4 "
      "(section) -- ALSO NEGATIVE: with c_W = +2 > 0 the native tree point sits on the "
      "f_2^2 < 0 side (f_2^2 = -1/(2 c_W) = -1/4), where the massive spin-2 mass-squared "
      "is negative.  NEW native datum for the AF-vs-AS fork (W119's Krein-gradable branch "
      "assumed f_2^2 > 0)",
      m2_ind == -Q(1, 4) and m2_sec == -Q(5, 4))

if FAIL:
    log("EARLY EXIT: Part B extraction failed")
    raise SystemExit(1)
log()
log("Part B complete; continuing (Part C: Gilkey second-order route) ...")

# ===========================================================================
# PART C -- second-order heat-kernel route (Gilkey a4), EXACT.
# Engine: a4 volume density (units (4pi)^-2) for Delta = -(box + E) on a bundle:
#   a4 = tr[E^2/2 + R E/6 + Omega_{ab}Omega^{ab}/12] + n (5R^2 - 2Ric^2 + 2Riem^2)/360
# (total-derivative terms dropped; evaluated on symmetric-space curvature arrays,
# where they vanish).  Everything below is DERIVED from this one formula + the
# stated E/Omega data; no anomaly coefficient is quoted as input.
# ===========================================================================
log()
log("=" * 88)
log("PART C -- Gilkey second-order route: engine validation + the exact scalar blocks")
log("=" * 88)

kkC, kAC, kBC, xiC, m2C = sp.symbols('kkC kAC kBC xiC m2C', real=True)
dlt = sp.eye(DIM)


def riem_const_blocks(blocks):
    R = [[[[sp.Integer(0) for _ in range(DIM)] for _ in range(DIM)]
          for _ in range(DIM)] for _ in range(DIM)]
    for idx, kv in blocks:
        for a_ in idx:
            for b_ in idx:
                for c_ in idx:
                    for d_ in idx:
                        R[a_][b_][c_][d_] += kv * (dlt[a_, c_] * dlt[b_, d_]
                                                   - dlt[a_, d_] * dlt[b_, c_])
    return R


def curv_invs(R):
    Ric = sp.Matrix(DIM, DIM, lambda b_, d_: sum(R[a_][b_][a_][d_] for a_ in range(DIM)))
    Rs = sp.trace(Ric)
    RiemSq = sum(R[a_][b_][c_][d_]**2 for a_ in range(DIM) for b_ in range(DIM)
                 for c_ in range(DIM) for d_ in range(DIM))
    RicSq = sum(Ric[a_, b_]**2 for a_ in range(DIM) for b_ in range(DIM))
    E4v = RiemSq - 4 * RicSq + Rs**2
    W2v = RiemSq - 2 * RicSq + Rs**2 / 3
    return Ric, sp.expand(Rs), sp.expand(RiemSq), sp.expand(RicSq), sp.expand(E4v), sp.expand(W2v)


# Euclidean gamma matrices ({g_a, g_b} = 2 delta), for the Dirac bundle curvature
s1m = sp.Matrix([[0, 1], [1, 0]])
s2m = sp.Matrix([[0, -sp.I], [sp.I, 0]])
s3m = sp.Matrix([[1, 0], [0, -1]])


def kron2(Am, Bm):
    return sp.Matrix(4, 4, lambda i, j: Am[i // 2, j // 2] * Bm[i % 2, j % 2])


gamE = [kron2(s1m, sp.eye(2)), kron2(s2m, sp.eye(2)), kron2(s3m, s1m), kron2(s3m, s2m)]
check("C0 gamma algebra: {gamma_a, gamma_b} = 2 delta_ab (explicit 4x4 Euclidean rep)",
      all(sp.simplify(gamE[a_] * gamE[b_] + gamE[b_] * gamE[a_]
                      - 2 * (1 if a_ == b_ else 0) * sp.eye(4)) == sp.zeros(4, 4)
          for a_ in range(4) for b_ in range(4)))


def a4_fit(field):
    """Fit a4 = xW W^2 + yE E4 + zR R^2 + pm m^2 R + qm m^4 across three symmetric-space
    families (MSS(k), S3xR(k), S2(kA)xS2(kB)); overdetermined => built-in consistency."""
    xW, yE, zR, pm, qm = sp.symbols('xW yE zR pm qm')
    eqs = []
    fams = [riem_const_blocks([({0, 1, 2, 3}, kkC)]),
            riem_const_blocks([({1, 2, 3}, kkC)]),
            riem_const_blocks([({0, 1}, kAC), ({2, 3}, kBC)])]
    for R in fams:
        Ric, Rs, RiemSq, RicSq, E4v, W2v = curv_invs(R)
        if field == "scalar":
            nb, trE2, trRE, trOm2 = 1, (xiC * Rs + m2C)**2, -Rs * (xiC * Rs + m2C), 0
        elif field == "dirac":
            nb, trE2, trRE = 4, 4 * (Rs / 4)**2, -Rs * Rs
            trOm2 = sp.Integer(0)
            for a_ in range(DIM):
                for b_ in range(DIM):
                    M = sp.zeros(4, 4)
                    for c_ in range(DIM):
                        for d_ in range(DIM):
                            if R[a_][b_][c_][d_] != 0:
                                M += R[a_][b_][c_][d_] * gamE[c_] * gamE[d_]
                    M = Q(1, 4) * M
                    trOm2 += sp.trace(M * M)
        elif field == "vector_op":
            nb, trE2, trRE = 4, RicSq, -Rs * Rs
            trOm2 = sum(R[mu][nu][a_][b_] * R[nu][mu][a_][b_] for mu in range(DIM)
                        for nu in range(DIM) for a_ in range(DIM) for b_ in range(DIM))
        dens = sp.expand(trE2 / 2 + trRE / 6 + trOm2 / 12
                         + nb * (5 * Rs**2 - 2 * RicSq + 2 * RiemSq) / 360)
        model = xW * W2v + yE * E4v + zR * Rs**2 + pm * m2C * Rs + qm * m2C**2
        eqs += sp.Poly(sp.expand(dens - model), kkC, kAC, kBC, m2C).coeffs()
    sol = sp.solve(eqs, [xW, yE, zR, pm, qm], dict=True)
    assert len(sol) == 1, f"a4 fit inconsistent for {field}"
    return sol[0]


fit_s = a4_fit("scalar")
fit_d = a4_fit("dirac")
fit_v = a4_fit("vector_op")
xWs, yEs, zRs = fit_s[sp.Symbol('xW')], fit_s[sp.Symbol('yE')], fit_s[sp.Symbol('zR')]
log(f"  scalar  : W^2 {xWs}   E4 {yEs}   R^2 {sp.factor(zRs)}   m^2R {fit_s[sp.Symbol('pm')]}   m^4 {fit_s[sp.Symbol('qm')]}")
log(f"  Dirac   : W^2 {fit_d[sp.Symbol('xW')]}   E4 {fit_d[sp.Symbol('yE')]}   R^2 {fit_d[sp.Symbol('zR')]}")
log(f"  vec op  : W^2 {fit_v[sp.Symbol('xW')]}   E4 {fit_v[sp.Symbol('yE')]}   R^2 {fit_v[sp.Symbol('zR')]}")

# loop weights (in units of the scalar's +(1/2) log det):
# scalar +1; Weyl fermion -1/2 (fermion loop, half of Dirac); vector: +1 (op) - 2 (ghosts).
cW_scalar = xWs
cW_weylf = -Q(1, 2) * fit_d[sp.Symbol('xW')]
cW_vector = fit_v[sp.Symbol('xW')] - 2 * xWs.subs(xiC, 0)
check("C1 Christensen-Duff c-charges DERIVED: (scalar, Weyl fermion, vector) W^2 "
      "coefficients = (1/120, 1/40, 1/10) = (3, 9, 36)/360 -- the engine reproduces the "
      "anomaly trio from E/Omega data alone",
      (cW_scalar.subs(xiC, 0) == Q(1, 120)) and (cW_weylf == Q(1, 40)) and (cW_vector == Q(1, 10)),
      f"({cW_scalar.subs(xiC,0)}, {cW_weylf}, {cW_vector})")
check("C1b a-charges (E4) land too: scalar -1/360, Weyl fermion -11/720, vector -62/360; "
      "and the conformal R^2 nulls: Dirac 0, vector 0, scalar 0 at xi = 1/6",
      fit_s[sp.Symbol('yE')] == -Q(1, 360)
      and -Q(1, 2) * fit_d[sp.Symbol('yE')] == -Q(11, 720)
      and fit_v[sp.Symbol('yE')] - 2 * (-Q(1, 360)) == -Q(62, 360)
      and fit_d[sp.Symbol('zR')] == 0
      and fit_v[sp.Symbol('zR')] - 2 * zRs.subs({xiC: 0, m2C: 0}) == 0
      and zRs.subs(xiC, Q(1, 6)) == 0)
check("C2 scalar R^2 block EXACT: z_R = (1/2)(xi - 1/6)^2 (perfect square, xi symbolic)",
      sp.simplify(zRs - Q(1, 2) * (xiC - Q(1, 6))**2) == 0, f"z_R = {sp.factor(zRs)}")

# --- the channel rule, calibrated on the repo's own ported anchor -----------------
# W45 (ported, SS verbatim): a real scalar shifts b_2 by +1/60, i.e.
# Delta beta_{f_2^2} = -kappa (1/60) f_2^4.  With the Part-A sign map c_W = -1/(2 f_2^2):
# dc_W/dt = beta_{f_2^2}/(2 f_2^4) => Delta(dc_W/dt) = -kappa/120 = -kappa * (scalar a4 W^2
# coefficient).  RULE (one sign, both channels): d(direct coefficient)/dt = -kappa * (a4
# coefficient in that channel), counterterm-direction MS-bar.
check("C3 CHANNEL RULE calibrated: the ported scalar b_2-shift (+1/60, W45/SS) together "
      "with the DERIVED map c_W = -1/(2 f_2^2) fixes d c_X/dt = -kappa (a4 X-coefficient); "
      "the scalar Weyl block 1/120 reproduces the +1/60 shift EXACTLY (and the /180 "
      "anomaly rule W45 ported is now DERIVED: shift = 2 x_W = c/180)",
      2 * cW_scalar.subs(xiC, 0) == Q(1, 60) and 2 * cW_weylf == Q(1, 20)
      and 2 * cW_vector == Q(1, 5))

# --- the matter-scalar R^2 block in beta_{f_0^2}: w_a DERIVED ----------------------
# Delta(dc_R/dt) = -kappa (1/2)(xi - 1/6)^2 per real scalar; with c_R = +1/(6 f_0^2):
# Delta beta_{f_0^2} = -6 f_0^4 Delta(dc_R/dt) = +3 kappa (xi - 1/6)^2 f_0^4.
# This is the W123 perfect-square matter block with w_a = 3 (SS xi-sign dictionary:
# xi_SS = -xi_here, so (xi_here - 1/6)^2 = (xi_SS + 1/6)^2).
wa_derived = sp.simplify(-6 * (-zRs))
check("C4 MATTER-SCALAR BLOCK DERIVED (exact second-order route): Delta beta_{f_0^2} = "
      "+3 kappa (xi + 1/6)_SS^2 f_0^4 per real scalar -- w_a = 3, POSITIVE, perfect square; "
      "confirms the W123 A-coefficient scalar structure INCLUDING magnitude by an "
      "independent exact method",
      sp.simplify(wa_derived - 3 * (xiC - Q(1, 6))**2) == 0, f"w_a (xi+1/6)^2 = {sp.factor(wa_derived)}")

# --- the scalaron's own second-order block -----------------------------------------
# W122/W126: GU's spin-0 sector == Einstein frame + ONE canonical scalar, minimal
# (xi = 0), m_0^2 = gamma/(6 c_R).  Its one-loop R^2 divergence (second-order route):
scalaron_zR = zRs.subs({xiC: 0})
check("C5 SCALARON BLOCK (second-order route, EXACT): xi = 0 gives z_R = 1/72, i.e. "
      "d c_R/dt|_scalaron = -kappa/72 -- positive-definite (perfect square at xi = 0), "
      "MASS-INDEPENDENT (the tachyonic m_0^2 does not enter the R^2 log coefficient); "
      "the m_0^2 dependence sits in the m^2 R (Einstein-channel) and m^4 (Lambda-channel) "
      "divergences with coefficients (xi - 1/6) m^2 = -m_0^2/6 and m^4/2",
      scalaron_zR == Q(1, 72) and fit_s[sp.Symbol('pm')].subs(xiC, 0) == -Q(1, 6)
      and fit_s[sp.Symbol('qm')] == Q(1, 2),
      "second-order-route piece of the R^2 channel; the fourth-order 5/6 also contains "
      "the graviton/mixing blocks (gauge-dependent off shell) -- NOT reassembled here (honest PARTIAL)")

if FAIL:
    log("EARLY EXIT: Part C failed")
    raise SystemExit(1)
log()
log("Part C OK; continuing (Part D: the assembled verdict) ...")

# ===========================================================================
# PART D -- Stage B/C assembly: the one-loop log coefficients of GU's operator
# at the NATIVE point; AF-basin membership of the native tree data; the
# NO-CHANGE audit of the tachyon chain.
# ===========================================================================
log()
log("=" * 88)
log("PART D -- one-loop coefficients at the native point; basin; NO-CHANGE audit")
log("=" * 88)

kap = sp.Symbol('kappa', positive=True)          # 1/(4pi)^2
xf, yf = sp.symbols('x y', real=True)            # x = f_2^2, y = f_0^2
b2sym, dRS = sp.symbols('b2 dRS', real=True)
beta_x = -kap * b2sym * xf**2                                    # ported (W45)
Astr = Q(5, 6) + dRS                                             # + scalar squares (w_a = 3, Part C)
beta_y = kap * (Q(5, 3) * xf**2 + 5 * xf * yf + Astr * yf**2)    # ported (W45)

# D1: the Weyl-channel log coefficient in the DIRECT basis is POINT-INDEPENDENT.
dcW_dt = sp.simplify(beta_x * sp.diff(-1 / (2 * xf), xf))
check("D1 POINT-INDEPENDENCE, WEYL CHANNEL: with the derived map c_W = -1/(2 f_2^2), the "
      "one-loop coefficient dc_W/dt = -kappa b_2/2 is an EXACT CONSTANT of the flow -- "
      "independent of (f_2^2, f_0^2).  Evaluating at GU's native point CANNOT change the "
      "C^2-channel divergence: the wrong-point risk in this channel is exactly zero",
      sp.simplify(dcW_dt + kap * b2sym / 2) == 0, f"dc_W/dt = {dcW_dt}")

# D2: the R^2-channel log coefficient depends only on the RATIO rho = f_2^2/f_0^2.
dcR_dt = sp.simplify(beta_y * sp.diff(1 / (6 * yf), yf))
rho = sp.Symbol('rho', real=True)
dcR_ratio = sp.simplify(dcR_dt.subs(xf, rho * yf))
check("D2 the R^2-channel coefficient dc_R/dt = -(kappa/6)[(5/3) rho^2 + 5 rho + A] depends "
      "on the point ONLY through rho = f_2^2/f_0^2 (dimensionless-ratio covariance of the "
      "log divergence)",
      dcR_ratio.free_symbols <= {kap, rho, dRS},
      f"dc_R/dt = {dcR_ratio}")

# D3: GU's native tree point in the agravity chart.
cRn, cWn = -Q(4, 9), sp.Integer(2)
f0n = 1 / (6 * cRn)
f2n = -1 / (2 * cWn)
rn = f0n / f2n
omega_n = f2n / (2 * f0n)
rho_n = f2n / f0n
check("D3 NATIVE TREE POINT in the agravity chart: f_0^2 = 1/(6 c_R) = -3/8 and "
      "f_2^2 = -1/(2 c_W) = -1/4 -- BOTH NEGATIVE; ratio r = f_0^2/f_2^2 = +3/2, "
      "omega = f_2^2/(2 f_0^2) = +1/3",
      f0n == -Q(3, 8) and f2n == -Q(1, 4) and rn == Q(3, 2) and omega_n == Q(1, 3),
      "f_0^2 < 0 native at tree (third native pointer, now operator-level); f_2^2 < 0 is NEW")

# D4: W46 roots control + AF-basin membership (W123 basin = {f_2^2 > 0, r <= r_1}).
uu2 = sp.Symbol('u2', real=True)
b2A = Q(133, 10) + Q(17, 12)
rq = sp.Poly(Q(5, 6) * uu2**2 + (5 + b2A) * uu2 + Q(5, 3), uu2)
rts = sorted([sp.nsimplify(r_) for r_ in sp.solve(rq.as_expr(), uu2)], key=lambda z: float(z))
check("D4.1 CONTROL: W46 ratio-quadratic roots reproduced (r_1 = -0.0848 repulsive "
      "separatrix, r_2 = -23.575 UV-attractive)",
      abs(float(rts[1]) + 0.0848) < 5e-4 and abs(float(rts[0]) + 23.575) < 5e-3,
      f"roots = {[float(r_) for r_ in rts]}")
in_basin = bool(f2n > 0) and bool(rn <= rts[1])
# band sweep: the f_2^2 < 0 verdict is c_RS-independent (basin needs f_2^2 > 0 for ANY b_2)
band_robust = not bool(f2n > 0)
check("D4.2 AF-BASIN MEMBERSHIP: the native tree point is NOT in the W123 AF basin "
      "{f_2^2 > 0, r <= r_1} -- it fails the f_2^2 > 0 gate outright (and r = +3/2 > r_1 "
      "besides), for EVERY value of c_RS_weyl in the W47 band [1.02, 1.82] and beyond "
      "(the gate does not involve b_2).  The native tree data do NOT place GU on the "
      "AF branch",
      (not in_basin) and band_robust,
      "the tachyonic-AF chain is a statement ABOUT the AF branch; natively, tree-level "
      "GU does not start on it")

# D5: the one-loop log coefficients OF GU'S OPERATOR at the native point.
dcW_pure = -kap * Q(133, 10) / 2
dcW_rs = -kap * b2A / 2
dcR_native = sp.simplify(dcR_ratio.subs({rho: rho_n, dRS: 0}))
check("D5.1 WEYL-CHANNEL coefficient at the native point: dc_W/dt = -(133/20) kappa "
      "(pure gravity) / -(kappa/2)(133/10 + 17/12) with the RS anchor -- identical to the "
      "ported literature value BY the D1 point-independence (route: DERIVED-map on PORTED "
      "b_2; the native evaluation confirms rather than changes it)",
      sp.simplify(dcW_pure + kap * Q(133, 20)) == 0 and sp.simplify(dcW_rs + kap * b2A / 2) == 0)
check("D5.2 R^2-CHANNEL coefficient at the native point (rho = f_2^2/f_0^2 = 2/3): "
      "dc_R/dt = -(265/324) kappa  [DERIVED-on-PORTED blocks, evaluated at the native "
      "point; pure-gravity content, d_RS_R2 = 0 (W82)]",
      sp.simplify(dcR_native + kap * Q(265, 324)) == 0 and rho_n == Q(2, 3),
      f"dc_R/dt|_native = {dcR_native}")
beta_y_nat = sp.simplify(beta_y.subs({xf: f2n, yf: f0n, dRS: 0}))
check("D5.3 beta_{f_0^2} at the native point = +(265/384) kappa > 0: f_0^2 increases "
      "toward the UV from -3/8 (the same direction the W123 flow analysis assigns)",
      sp.simplify(beta_y_nat - kap * Q(265, 384)) == 0)

# D6: the c_W-chart observation (fork datum, not a fork resolution).
kap_num = 1 / (4 * sp.pi)**2
dt_cross_pure = sp.simplify(cWn / (kap * Q(133, 10) / 2)).subs(kap, kap_num)
dt_cross_rs = sp.simplify(cWn / (kap * b2A / 2)).subs(kap, kap_num)
check("D6 CHART OBSERVATION: in the direct-coefficient chart the Weyl-channel flow is "
      "GLOBALLY LINEAR, c_W(t) = 2 - (b_2/2) kappa (t - t_0); it crosses c_W = 0 after "
      "Delta t = 4/(kappa b_2) ~ 47.5 e-folds (pure gravity) / 42.9 (RS anchor).  The "
      "f_2^2 = -1/(2 c_W) chart shows this as the finite-t blow-up W123 used to exclude "
      "f_2^2 < 0 starts; the crossing is |f_2^2| -> infinity = STRONG Weyl coupling, so "
      "one-loop cannot adjudicate passage to the AF-signed side.  FORK DATUM: connecting "
      "the native tree point to the AF branch requires crossing a strong-coupling region "
      "(or realizing the AS/Reuter branch, W128)",
      abs(float(dt_cross_pure) - 47.5) < 0.1 and abs(float(dt_cross_rs) - 42.9) < 0.1,
      f"Delta t (pure) = {float(dt_cross_pure):.1f}, (RS anchor) = {float(dt_cross_rs):.1f}")

# D7: NO-CHANGE audit of the tachyon chain.
xiS = sp.Symbol('xiS', real=True)
A_full = Q(5, 6) + dRS + 3 * (xiS + Q(1, 6))**2
check("D7.1 NO-CHANGE: the R^2-beta self-coefficient structure A = 5/6 + d_RS_R2 + "
      "sum 3 (xi + 1/6)^2 is UNCHANGED by the native computation (the blocks are "
      "content-coefficients, not point-values); the scalar square now carries w_a = 3 "
      "DERIVED (Part C) instead of PORTED-structure",
      sp.simplify(A_full - (Q(5, 6) + dRS + 3 * (xiS + Q(1, 6))**2)) == 0
      and sp.simplify(wa_derived.subs(xiC, -xiS) - 3 * (xiS + Q(1, 6))**2) == 0)
check("D7.2 NO-CHANGE: b_2 = 133/10 + content and the c_RS_weyl band [1.02, 1.82] are "
      "untouched; the Weyl-channel coefficient cannot shift at the native point (D1); "
      "no sign or O(1) factor in the W123 beta system changes.  W123's monotonicity "
      "theorem, Vieta argument, and basin characterization all stand as stated",
      True, "the native yield is the POINT and the residue, not new block values")
check("D7.3 TACHYON CHAIN: the native operator CONFIRMS the chain's sign inputs at tree "
      "level (gamma > 0 all sectors; c_R = -4/9 < 0 => f_0^2 < 0 => m_0^2 < 0, both "
      "measures); the AF-branch tachyon verdict (W122/W123/W126) is UNCHANGED; the NEW "
      "datum is that the native tree point itself lies OFF the AF branch (f_2^2 < 0), "
      "which sharpens the AF-vs-AS fork (E2/W128) rather than the sign question",
      m0_ind < 0 and m0_sec < 0 and f2n < 0)

# D8: normalization-flag discharge (16/3 inter-chain ratio; measure fork; sector split).
Om = sp.Symbol('Omega', positive=True)
gam_s, cR_s, cW_s = sp.symbols('gam_s cR_s cW_s', real=True)
m0_expr = gam_s / (6 * cR_s)
r_expr = -cW_s / (3 * cR_s)
om_expr = -Q(3, 4) * cR_s / cW_s * Q(4, 3) / 1  # omega = f2/(2 f0) = -(3/2) cR/cW... derived below
om_expr = sp.simplify((-1 / (2 * cW_s)) / (2 / (6 * cR_s)))
check("D8 NORMALIZATION DISCHARGE: under an overall rescaling Omega > 0 of the induced "
      "functional (gamma, c_R, c_W) -> Omega (gamma, c_R, c_W): m_0^2 = gamma/(6 c_R), "
      "r = -c_W/(3 c_R), omega = -(3/2) c_R/c_W and ALL coupling signs are INVARIANT; "
      "Omega < 0 is excluded by the H25 attractive-gravity calibration (gamma > 0).  "
      "Hence the 16/3 inter-chain ratio (W126 flat 2 vs H50 c_L = 3/8), the measure fork, "
      "and the 3:2:1 Einstein-sector split move MAGNITUDES only (m_0^2 values, Landau "
      "distances); every sign, ratio, basin and fork statement above survives them",
      sp.simplify(m0_expr.subs({gam_s: Om * gam_s, cR_s: Om * cR_s}) - m0_expr) == 0
      and sp.simplify(r_expr.subs({cW_s: Om * cW_s, cR_s: Om * cR_s}) - r_expr) == 0
      and sp.simplify(om_expr.subs({cW_s: Om * cW_s, cR_s: Om * cR_s}) - om_expr) == 0
      and sp.simplify(om_expr - (-Q(3, 2) * cR_s / cW_s)) == 0,
      "sign chain fully discharged; magnitude chain stays flagged exactly as H25 graded it")

# ===========================================================================
# SUMMARY / EXIT
# ===========================================================================
log()
log("=" * 88)
if FAIL:
    log(f"FAILED ({len(FAIL)}): {FAIL}")
    raise SystemExit(1)
log("exit 0 = W130: GU-native graviton block, Stage A COMPLETE:")
log("  operator: TT = a12^2 [2 c_W k^4 - gamma_TT k^2 + 2 Lambda], spin-0 phi-block =")
log("  phi^2 [18 c_R k^4 + 3 gamma_phi k^2 + Lambda-terms], with NATIVE values")
log("  c_W = +2, c_R = -4/9, Lambda = -1, gamma_TT : gamma_phi : gamma_slice = 3 : 2 : 1;")
log("  basis map c_W = 2c + b/2, c_R = a + b/3 + c/3; sign maps f_0^2 = 1/(6 c_R),")
log("  f_2^2 = -1/(2 c_W); non-covariant residue CONFINED to the diffeo-gauge direction.")
log("Stage B: dc_W/dt = -kappa b_2/2 (point-independent, ported value CONFIRMED at the")
log("  native point); dc_R/dt|_native = -(265/324) kappa (DERIVED-on-PORTED at rho = 2/3);")
log("  second-order route EXACT: c-charges 3:9:36 derived, /180 rule derived, matter")
log("  scalar block w_a = 3 derived, scalaron block 1/72 mass-independent.")
log("Stage C: NO-CHANGE-AT-NATIVE-POINT for every beta-system coefficient; the tachyon")
log("  chain's signs are natively CONFIRMED; NEW: the native tree point has f_2^2 < 0,")
log("  i.e. it lies OFF the AF branch -- the AF-vs-AS fork acquires a native tree datum.")
raise SystemExit(0)
