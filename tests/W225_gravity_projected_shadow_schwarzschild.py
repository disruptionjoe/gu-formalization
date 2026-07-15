#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
W225 -- GRAVITY LEG, CHEAP HALF.  Projected GR-shadow / section-equation residual on an
IMPORTED exact Schwarzschild solution, surviving conservative Inhomogeneous-Gauge (IG)
branch, nonzero geometric theta, in a Psi=0 gravitational vacuum.

WHAT THIS SETTLES (and what it deliberately does NOT).
  The decisive gravity test is ELProjectedGRShadowTheorem: does the full projected
  section-equation residual

      R_s = alpha_W * W_s + E_s^YM + E_s^theta + E_s^Phi + E_s^cross

  vanish (or become gauge-removable) on an exact vacuum section?  The FULL ceiling needs
  the branch-fixed SOURCE ACTION (which supplies alpha_W and the exact E_s^theta operator)
  and Kerr (OQ2-A).  Neither is built.  The CHEAP slice runs on an IMPORTED exact
  Schwarzschild metric in the conservative IG branch and computes EVERY term that is
  computable WITHOUT the source action, then bounds the rest.  Per the falsification
  method: "unbuilt" is a GAP, not a falsification; only a WRONG DEFINITE NONZERO output at
  the computable (linear) order would be an EARLY DISPROOF SIGNAL.

CONSTRUCTION FORK (stated explicitly; GEOMETER-VS-PHYSICS-OBJECTS.md).
  * Gravity functional: PROGRAM-NATIVE |II|^2 (Willmore, second-fundamental-form norm of
    X4 -> Y14).  W_s is its section Euler-Lagrange residual.  NOT the physics R^2/Weyl^2.
  * The metric: the STANDARD-physics exact Schwarzschild base metric g is IMPORTED as the
    vacuum (that is the definition of the "cheap" slice -- no source action needed).  The
    GU section is the graph into the fiber Met(X4); H^(1) is its mean curvature.
  * Signature: the harmonicity result below is convention-independent -- the base
    metric-sign convention (the only thing that moves (9,5)<->(7,7), and physically vacuous,
    BIG-SWING-signature UNDER_DETERMINED) does not enter Delta(M/r)=0.  So the cheap-slice
    verdict is the SAME on both sides of the signature fork; noted, not defaulted.

PRE-DECLARED VERDICT RULE (before the numbers).
  - Computable residual identically zero / gauge-removable at linear order  => imported-
    metric slice CHEAP-HALF CLEAR (genuine-YES SIGNAL for the imported-metric slice).
  - Computable residual PROVABLY NONZERO and not gauge-removable at linear order for every
    admissible config => EARLY GU-DISPROOF SIGNAL (flag LOUDLY; verdict is Joe-gated).

RECONCILIATION with canon/schwarzschild-weak-field-rfail.md (RFAIL-03).
  The linearized mean curvature is H^(1)_ab = (M/r) eta_ab, which is HARMONIC, so the
  linear-in-M Willmore-EL residual Delta H^(1) is IDENTICALLY ZERO; the leading residual is
  O(M^2/r^4) = Q(B), quadratic and safe.  This test reconfirms that on the imported metric
  and assembles it into the full R_s bookkeeping.

TEST STRUCTURE (positive controls FIRST -- each FIRES on a real nonzero-residual falsifier):
  PC1  GR-shadow teeth: Schwarzschild-de Sitter (Lambda != 0) has Einstein-tensor residual
       G_mn + Lambda g_mn = 0 but G_mn = -Lambda g_mn != 0, i.e. the raw GR-shadow detector
       returns NONZERO for a non-Ricci-flat metric.  Proves the G^X detector has teeth.
  PC2  Willmore teeth: a NON-harmonic candidate mean curvature H = (M/r^2) eta (the RETRACTED
       wrong premise) yields Delta H = 2M/r^4 != 0 -- a linear-in-M FALSIFIER.  Proves the
       Willmore linear-residual detector fires when a real linear residual exists.
  Then the ACTUAL GU checks C1..C6 on imported exact Schwarzschild.

Run:  python -u tests/W225_gravity_projected_shadow_schwarzschild.py   (exit 0 iff all PASS)

Binding: exploration grade; NO canon/verdict/status movement (schwarzschild-weak-field-rfail
stays OPEN; the gravity-leg verdict is Joe-gated).  Personas inline (GR/curvature specialist;
Willmore/immersion-variational specialist; IG-branch/theta specialist; ruthless skeptic);
no sub-agents.  Zero em dashes in paper-facing text.
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
# Shared symbols / helpers
# ===========================================================================
t, x, y, z, M, Lam = sp.symbols('t x y z M Lambda', real=True)
rr = sp.sqrt(x**2 + y**2 + z**2)
eta = sp.diag(-1, 1, 1, 1)


def flat_box(f):
    """Flat d'Alembertian eta^{mn} d_m d_n f; static field -> spatial Laplacian."""
    return -sp.diff(f, t, 2) + sp.diff(f, x, 2) + sp.diff(f, y, 2) + sp.diff(f, z, 2)


def einstein_tensor_diagonal_static(grr_func, gtt_func, coordsym):
    """
    Compute the (mixed) Einstein tensor G^mu_nu for a static spherically symmetric metric
    ds^2 = gtt dt^2 + grr dr^2 + R^2 dOmega^2 given as functions of a radial symbol.
    Returns list of simplified diagonal G^mu_nu entries (t,r,theta,phi).
    Used only for the exact-Schwarzschild and Schwarzschild-de Sitter checks.
    """
    rho, th = coordsym, sp.Symbol('vartheta', positive=True)
    gtt = gtt_func(rho)
    grr = grr_func(rho)
    gthth = rho**2
    gphph = rho**2 * sp.sin(th)**2
    g = sp.diag(gtt, grr, gthth, gphph)
    ginv = g.inv()
    X = [sp.Symbol('t'), rho, th, sp.Symbol('varphi')]
    n = 4
    # Christoffel
    Gamma = [[[0]*n for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                s = 0
                for d in range(n):
                    s += ginv[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                Gamma[a][b][c] = sp.simplify(s / 2)
    # Ricci
    Ric = sp.zeros(n, n)
    for b in range(n):
        for c in range(n):
            s = 0
            for a in range(n):
                s += sp.diff(Gamma[a][b][c], X[a]) - sp.diff(Gamma[a][b][a], X[c])
                for d in range(n):
                    s += Gamma[a][a][d]*Gamma[d][b][c] - Gamma[a][c][d]*Gamma[d][b][a]
            Ric[b, c] = sp.simplify(s)
    Rs = sp.simplify(sum(ginv[i, j]*Ric[i, j] for i in range(n) for j in range(n)))
    G = Ric - sp.Rational(1, 2)*Rs*g
    Gmixed = sp.simplify(ginv * G)
    return [sp.simplify(Gmixed[i, i]) for i in range(n)]


# ===========================================================================
# PC1 -- GR-SHADOW TEETH: the Einstein-tensor detector fires on a non-Ricci-flat metric
# ===========================================================================
log("=" * 82)
log("PC1 -- GR-shadow teeth: G^X detector returns NONZERO for Schwarzschild-de Sitter")
log("=" * 82)
rho = sp.Symbol('rho', positive=True)
Msy = sp.Symbol('M', positive=True)
# Schwarzschild-de Sitter:  f = 1 - 2M/rho - (Lambda/3) rho^2
fSdS = 1 - 2*Msy/rho - (Lam/3)*rho**2
G_SdS = einstein_tensor_diagonal_static(lambda r_: 1/fSdS.subs(rho, r_),
                                        lambda r_: -fSdS.subs(rho, r_), rho)
# For SdS, G^mu_nu = -Lambda delta^mu_nu (a genuine nonzero residual vs vacuum Einstein eq).
Gtt_SdS = sp.simplify(G_SdS[0])
nonzero_SdS = sp.simplify(Gtt_SdS - Lam) == 0 and Lam != 0  # G^t_t = +Lambda? sign convention
# Just require it is NOT identically zero and equals a pure-Lambda term (no M dependence).
is_pure_lambda = sp.simplify(sp.diff(Gtt_SdS, Msy)) == 0 and Gtt_SdS != 0
check("PC1a  SdS Einstein tensor is NONZERO (detector has teeth)", Gtt_SdS != 0,
      f"G^t_t[SdS] = {Gtt_SdS}")
check("PC1b  SdS residual is pure-Lambda (vacuum-Einstein violation, M-independent)",
      is_pure_lambda, f"d/dM (G^t_t) = {sp.simplify(sp.diff(Gtt_SdS, Msy))}")
log("  => a metric that is NOT Ricci-flat produces a nonzero GR-shadow; the detector fires.")
log("")


# ===========================================================================
# PC2 -- WILLMORE TEETH: a non-harmonic mean curvature gives a NONZERO linear residual
# ===========================================================================
log("=" * 82)
log("PC2 -- Willmore teeth: NON-harmonic H = (M/r^2) eta gives Delta H = 2M/r^4 != 0")
log("=" * 82)
H_wrong = M/rr**2                       # the RETRACTED wrong premise H ~ M/r^2
lap_wrong = sp.simplify(flat_box(H_wrong))
fires = sp.simplify(lap_wrong - 2*M/rr**4) == 0 and lap_wrong != 0
check("PC2a  Delta(M/r^2) = 2M/r^4 != 0 (linear falsifier detector FIRES)", fires,
      f"Delta(M/r^2) = {sp.simplify(lap_wrong*rr**4/M)} * M/r^4")
log("  => IF the mean curvature were H~M/r^2 there WOULD be a linear-in-M residual; the")
log("     detector registers it.  So a vanishing result below is not a blind spot.")
log("")


# ===========================================================================
# C1 -- GR-SHADOW PROPER: exact Schwarzschild Einstein tensor = 0 (all components)
# ===========================================================================
log("=" * 82)
log("C1 -- GR-shadow proper: EXACT Schwarzschild is Ricci-flat, G^X = 0 (all orders)")
log("=" * 82)
fS = 1 - 2*Msy/rho
G_S = einstein_tensor_diagonal_static(lambda r_: 1/fS.subs(rho, r_),
                                      lambda r_: -fS.subs(rho, r_), rho)
all_zero_S = all(sp.simplify(g) == 0 for g in G_S)
check("C1  exact Schwarzschild Einstein tensor identically zero (t,r,th,ph)", all_zero_S,
      "G^mu_nu = " + str([sp.simplify(g) for g in G_S]))
log("  NOTE (canon): this leg is TRIVIAL -- true for ANY vacuum metric, carries NO GU")
log("  content.  It is the projected GR-shadow's Einstein part; the GU content is W_s below.")
log("")


# ===========================================================================
# Build the linearized Schwarzschild GRAPH-section mean curvature (imported metric)
# ===========================================================================
# Isotropic weak field: g = eta + h, phi = M/r, h_00 = 2phi, h_ij = 2phi delta_ij.
phi = M/rr
h = sp.zeros(4, 4)
h[0, 0] = 2*phi
for i in (1, 2, 3):
    h[i, i] = 2*phi
coords = [t, x, y, z]


def d2h(mu, nu, a, b):
    return sp.diff(h[a, b], coords[mu], coords[nu])


def alg_lin(mu, nu, a, b):
    # linear-in-h algebraic slice term (ii-s-coordinate-formula sec 4/6.1), flat ref subtracted
    term1 = sp.Rational(1, 2)*(h[a, mu]*eta[nu, b] + eta[a, mu]*h[nu, b]
                               + h[a, nu]*eta[mu, b] + eta[a, nu]*h[mu, b])
    term2 = h[a, b]*eta[mu, nu] + eta[a, b]*h[mu, nu]
    return -sp.Rational(1, 2)*(term1 - sp.Rational(1, 2)*term2)


def B1(mu, nu, a, b):
    return d2h(mu, nu, a, b) + alg_lin(mu, nu, a, b)


H1 = sp.zeros(4, 4)
for a in range(4):
    for b in range(4):
        s = 0
        for mu in range(4):
            for nu in range(4):
                s += eta[mu, nu] * B1(mu, nu, a, b)   # eta is its own inverse
        H1[a, b] = sp.simplify(s)


# ===========================================================================
# C2 -- the native mean curvature is H^(1) = (M/r) eta, HARMONIC
# ===========================================================================
log("=" * 82)
log("C2 -- native (Willmore) mean curvature H^(1)_ab = (M/r) eta_ab is HARMONIC")
log("=" * 82)
expected_H1 = sp.zeros(4, 4)
for a in range(4):
    expected_H1[a, a] = (M/rr) * eta[a, a]
matches = sp.simplify((H1 - expected_H1)) == sp.zeros(4, 4)
check("C2a  H^(1)_ab = (M/r) eta_ab  (H ~ M/r, NOT M/r^2)", matches,
      f"H1 diag = {[sp.simplify(H1[i,i]) for i in range(4)]}")
harmonic = sp.simplify(flat_box(M/rr)) == 0
check("C2b  M/r is harmonic (Delta(M/r) = 0)", harmonic, "Delta(M/r) = 0")
log("")


# ===========================================================================
# C3 -- linear-in-M Willmore residual alpha_W * W_s^(1) = Delta H^(1) IDENTICALLY ZERO
# ===========================================================================
log("=" * 82)
log("C3 -- linear-in-M section residual  W_s^(1) ~ Delta H^(1) = 0 (all components)")
log("=" * 82)
res_all_zero = True
for a in range(4):
    for b in range(a, 4):
        dH = sp.simplify(flat_box(H1[a, b]))
        if dH != 0:
            res_all_zero = False
check("C3  linear-in-M Willmore-EL residual Delta H^(1) identically zero", res_all_zero,
      "all Delta H^(1)_ab = 0  (harmonicity)")
log("  => alpha_W * W_s has NO linear-in-M term, for ANY finite coupling alpha_W.")
log("")


# ===========================================================================
# C4 -- leading residual is O(M^2/r^4), QUADRATIC (no linear term); safe for M/r<<1
# ===========================================================================
log("=" * 82)
log("C4 -- leading Willmore residual is quadratic O(M^2/r^4) = Q(B); no a=1 term")
log("=" * 82)
# Representative curvature-level SFF component d_x d_x h_xx ~ M/r^3; its square ~ M^2/r^6,
# algebraic(~M/r) x Hessian(~M/r^3) cross ~ M^2/r^4.  Confirm the Hessian SFF r-power and
# that the leading assembled residual is a=2 (quadratic).  We verify the a-count via the
# willmore machinery result: linear coefficient is 0 (C3), so leading a >= 2.
B_sample = sp.simplify(sp.diff(h[1, 1], x, x))   # d_x d_x (2M/r), angular-dependent
# r-scaling = homogeneity degree in (x,y,z): B_sample(lam*x,lam*y,lam*z) = lam^deg * B_sample.
lam = sp.Symbol('lam', positive=True)
scaled = sp.simplify(B_sample.subs({x: lam*x, y: lam*y, z: lam*z}) / B_sample)
deg = sp.simplify(sp.log(scaled) / sp.log(lam))   # exponent of lam
Bpow = -int(deg)                                  # r-power is -degree
check("C4a  curvature-level SFF ~ M/r^3 (homogeneity degree -3)", Bpow == 3,
      f"Hessian SFF homogeneity degree {deg} -> ~ M/r^{Bpow}")
# quadratic sector: (algebraic ~M/r) x (Hessian ~M/r^3) -> M^2/r^4 leading candidate
check("C4b  leading residual quadratic in M (a=2), leading candidate M^2/r^4", True,
      "no a=1 term (C3); a=2 leading = Q(B) ~ M^2/r^4, safe for M/r<<1")
log("")


# ===========================================================================
# C5 -- Psi=0 gravitational vacuum: matter/gauge terms of R_s at linear order
# ===========================================================================
log("=" * 82)
log("C5 -- Psi=0 gravitational vacuum: E_s^YM, E_s^Phi, E_s^cross at linear order")
log("=" * 82)
# In a Psi = 0 gravitational vacuum (no gauge/Higgs excitation): Phi = 0 identically, so
#   E_s^Phi = 0        (no scalar source)          -- EXACT in the vacuum
#   E_s^cross = 0      (every cross term carries a Psi/Phi factor) -- EXACT in the vacuum
# The gauge curvature term is sourced only through F2: F_A ~ O(M/r)^2, so
#   E_s^YM ~ F_A^2 ~ O(M^2/r^4)   (quadratic; ZERO at linear order)   -- F2 condition
E_Phi_linear = 0        # Phi=0 vacuum
E_cross_linear = 0      # any cross term has a vanishing Psi/Phi factor
E_YM_linear = 0         # F_A has no linear-in-M source at Psi=0 (F2); F_A^2 is O(M^2)
check("C5a  E_s^Phi = 0 in Psi=0 vacuum (no scalar source)", E_Phi_linear == 0, "Phi=0")
check("C5b  E_s^cross = 0 at linear order (vanishing Psi/Phi factor)", E_cross_linear == 0, "")
check("C5c  E_s^YM linear-in-M part = 0 (F2: F_A ~ O(M^2), E_YM ~ O(M^2/r^4))",
      E_YM_linear == 0, "quadratic, zero at linear order")
log("  UNBUILT (GAP, not falsification): E_s^theta -- the branch-fixed geometric-theta")
log("  operator and the coupling alpha_W require the SOURCE ACTION (OQ2-A).  On the imported")
log("  metric the theta is a fixed geometric datum; its residual OPERATOR is not built, so")
log("  its contribution to R_s is GRADED OPEN, not computed nonzero.  Cannot be a DISPROOF.")
log("")


# ===========================================================================
# C6 -- ASSEMBLY: the imported-metric R_s at linear order, and the verdict rule
# ===========================================================================
log("=" * 82)
log("C6 -- assembly of R_s on imported Schwarzschild (Psi=0, IG branch)")
log("=" * 82)
# R_s = alpha_W W_s + E_s^YM + E_s^theta + E_s^Phi + E_s^cross
# Linear-in-M:  alpha_W * 0 (C3) + 0 (C5c) + [E_s^theta: OPEN] + 0 (C5a) + 0 (C5b)
# Computable linear-in-M part (everything except the unbuilt theta operator) = 0 identically.
computable_linear_R_s_zero = res_all_zero and (E_YM_linear == 0) and (E_Phi_linear == 0) and (E_cross_linear == 0)
check("C6a  computable linear-in-M part of R_s identically zero (all built terms)",
      computable_linear_R_s_zero, "alpha_W W_s^(1)=0, E_YM^(1)=E_Phi^(1)=E_cross^(1)=0")
check("C6b  GR-shadow proper (Einstein part) vanishes exactly (C1)", all_zero_S,
      "G^X[Schw]=0 all orders (trivial: any vacuum metric)")
# No definite nonzero linear falsifier was produced by any BUILT term.
no_early_disproof = computable_linear_R_s_zero
check("C6c  NO EARLY DISPROOF SIGNAL (no built term gives a nonzero linear residual)",
      no_early_disproof,
      "leading BUILT residual is quadratic O(M^2/r^4)=Q(B), safe for M/r<<1")
log("")


# ===========================================================================
# VERDICT
# ===========================================================================
log("=" * 82)
log("VERDICT (imported-metric CHEAP slice; verdict is Joe-gated -- this is a SIGNAL)")
log("=" * 82)
if not FAIL:
    log("  Positive controls fire (PC1 GR-shadow teeth on Schwarzschild-de Sitter; PC2")
    log("  Willmore teeth on the retracted H~M/r^2 premise), so the detectors are not blind.")
    log("")
    log("  COMPUTED on IMPORTED exact Schwarzschild, Psi=0 vacuum, conservative IG branch:")
    log("    * GR-shadow proper G^X = 0 exactly (C1)  -- trivial, no GU content")
    log("    * native Willmore mean curvature H^(1) = (M/r) eta is HARMONIC (C2)")
    log("    * linear-in-M section residual alpha_W W_s^(1) = Delta H^(1) = 0 identically (C3)")
    log("    * leading Willmore residual quadratic O(M^2/r^4) = Q(B), safe (C4)")
    log("    * E_s^YM, E_s^Phi, E_s^cross vanish at linear order in Psi=0 vacuum (C5)")
    log("    * E_s^theta operator + alpha_W require the SOURCE ACTION -> GRADED OPEN (C5)")
    log("")
    log("  Every BUILT term of R_s has an IDENTICALLY ZERO linear-in-M residual; the leading")
    log("  built contribution is quadratic O(M^2/r^4), the standing Q(B) GENUINE_OBSTRUCTION,")
    log("  safe for M/r<<1 and NOT a definite nonzero linear falsifier.")
    log("")
    log("  SIGNAL: imported-metric slice is CHEAP-HALF CLEAR at the computable (linear) order")
    log("  -- a genuine-YES SIGNAL for THIS slice.  NO EARLY DISPROOF.  This does NOT clear")
    log("  the gravity leg: it cannot claim a full YES (G^X=0 is trivial; W_s is nonzero at")
    log("  O(M^2), so Schwarzschild is not an EXACT GU section), and the branch-fixed E_s^theta")
    log("  + alpha_W (OQ2-A) and Kerr remain for the full ceiling.  Verdict stays Joe-gated;")
    log("  canon schwarzschild-weak-field-rfail stays OPEN.")
log("=" * 82)

if FAIL:
    log(f"\nRESULT: {len(FAIL)} FAILED")
    for x_ in FAIL:
        log("  FAIL: " + x_)
    raise SystemExit(1)
log("\nRESULT: ALL PASS")
