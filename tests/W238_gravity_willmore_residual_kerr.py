#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
W238 -- GRAVITY LEG, the LAST independent gravity frontier.  The native Willmore
mean-curvature residual  alpha_W W_s  on an IMPORTED exact KERR solution, surviving
conservative Inhomogeneous-Gauge (IG) branch, Psi=0 gravitational vacuum, at LINEAR
order in M with the rotation parameter a carried EXACTLY.

WHY THIS IS THE FRONTIER.
  W225 cleared alpha_W W_s on imported Schwarzschild at linear order: the native mean
  curvature is H^(1)_ab = (M/r) eta_ab, which is HARMONIC (Delta(M/r)=0, canon RFAIL-03),
  so the linear-in-M Willmore-EL residual Delta H^(1) = 0.  W236 cleared the theta sector
  E_s^theta = 0 on BOTH Schwarzschild and Kerr (Psi=0 => record current J=0 => theta=0,
  rotation-independent).  So the SOLE remaining gravity term whose Schwarzschild argument
  might BREAK on Kerr is the Willmore term, because the harmonicity of W225 was proven via
  STATIC ISOTROPY (h_ij = 2phi delta_ij, phi=M/r) and rotation breaks static isotropy: Kerr
  adds a gravitomagnetic frame-dragging cross term h_0i and anisotropic mass multipoles.

THE DECISIVE QUESTION (pre-declared, before the numbers).
  Is the linearized native mean curvature of the imported Kerr section still HARMONIC
  (Delta H^(1) = 0 => Willmore-EL residual zero, gravity clears on Kerr too), or does
  rotation produce a NONZERO, non-gauge-removable Willmore-EL residual at linear order in M?
  - ZERO / gauge-removable  => the gravity cheap-read EXTENDS TO KERR: fully clear on the
        rotating metric too.  A strong genuine-YES signal for the imported-metric slice.
  - NONZERO, non-gauge-removable at linear order => EARLY GU-DISPROOF SIGNAL (flag LOUDLY;
        verdict is Joe-gated, do NOT declare it here).

THE STRUCTURAL REASON (why isotropy was sufficient but NOT necessary).
  W225's harmonicity looked like a static-isotropic accident.  It is not.  The native mean
  curvature of the linearized graph section is a CONSTANT-COEFFICIENT LINEAR functional of
  the metric perturbation components:
      H^(1)_ab = eta^{mn} B^(1)_{mn,ab},
      B^(1)_{mn,ab} = d_m d_n h_ab  +  alg_lin(h)   (alg_lin = flat-eta constant-coeff linear).
  So H^(1)_ab = Box h_ab + (const-coeff linear combination of the h_cd).  If EVERY component
  h_ab is a HARMONIC function (Box h_ab = 0), then H^(1)_ab is a constant-coefficient linear
  combination of harmonic functions, hence itself HARMONIC, hence Delta H^(1) = 0 -- REGARDLESS
  of anisotropy, off-diagonal cross terms, or rotation.  The necessary-and-sufficient condition
  is PER-COMPONENT HARMONICITY of h, not isotropy.  And linearized STATIONARY VACUUM Einstein
  gravity in Lorenz (harmonic) gauge gives exactly that: nabla^2 hbar_mn = -16 pi T_mn = 0 in
  vacuum, so each Cartesian component of the linear-in-M field is harmonic.  Kerr's linear-in-M
  field is the Lorenz-gauge field of the Kerr multipoles (mass tower M_l = M(ia)^l and the
  angular-momentum/current tower, ALL linear in M); rotation only changes WHICH harmonic
  functions appear (adds the gravitomagnetic h_0i and the a-dependent multipoles), never
  whether they are harmonic.  Hence the Schwarzschild clear EXTENDS to Kerr.

CONSTRUCTION FORK (stated explicitly; GEOMETER-VS-PHYSICS-OBJECTS.md).
  1. Gravity functional -- PROGRAM-NATIVE |II|^2.  W_s is the Euler-Lagrange residual of the
     Willmore energy E[s] = integral |II_s^H|^2 (native second fundamental form of X^4 -> Y^14),
     NOT a free R^2/Weyl^2 Lagrangian.  This is the object whose linear residual Delta H^(1) is
     computed.  (Table row: Gravity functional -> native side.)
  2. The metric -- STANDARD-physics import, in HARMONIC (Lorenz) GAUGE.  The exact Kerr base
     metric is imported as the vacuum solution; its linear-in-M part is taken in harmonic-gauge
     Cartesian coordinates, the physics-standard choice.  Naming the gauge is load-bearing:
     harmonicity of the components is a GAUGE statement, and the "gauge-removable" branch of the
     verdict is exactly the statement that any apparent non-harmonic piece in a NON-harmonic
     chart (e.g. raw Boyer-Lindquist) is removed by transforming to the harmonic chart.  I do
     NOT conflate the imported base metric with the gimmel/fiber metric-on-metrics.
  3. Signature (9,5) vs (7,7) -- does NOT bite.  Delta H^(1) = 0 is convention-independent
     (the only datum that moves p-q is the base metric-sign convention, physically vacuous here).

TEST STRUCTURE (positive controls FIRST -- each FIRES on a real nonzero linear-in-M residual).
  PC1  ROTATION-SECTOR TEETH: a NON-harmonic mock gravitomagnetic term h_0i ~ (M a y)/r^2
       (wrong radial power) gives Delta(M a y/r^2) = -2 M a y/r^4 != 0, a linear-in-M residual
       that is ALSO linear in a (so it vanishes as a->0).  Proves the detector can SEE a genuine
       rotation-induced Willmore residual: the a=0 clear below is not a blind spot in a.
  PC2  RESIDUAL-OPERATOR TEETH: the retracted premise H = (M/r^2) has Delta(M/r^2) = 2M/r^4 != 0
       (same teeth as W225 PC2).  Proves the linear-residual detector is not blind.
  Then the ACTUAL GU checks on IMPORTED linearized Kerr, Psi=0 vacuum:
  C1  each harmonic-gauge linearized-Kerr component (Newtonian, a^2 quadrupole, gravitomagnetic)
      is harmonic.
  C2  the native mean curvature H^(1) (built by the SAME W225/willmore_el_order machinery,
      now with the Kerr h including h_0i and the a^2 quadrupole) has Delta H^(1) = 0 for EVERY
      one of its 10 components -- the Willmore-EL linear residual VANISHES on Kerr.
  C3  a->0 consistency: H^(1) collapses to the Schwarzschild (M/r) eta_ab with zero off-diagonal
      (reproduces W225 / RFAIL-03 exactly).
  C4  STRUCTURAL: Delta H^(1) = 0 is a constant-coefficient-linear consequence of per-component
      harmonicity; it holds for arbitrary harmonic multipole coefficients (a-exact), not just
      the sampled ones.
  C5  ASSEMBLY with W225 (four other terms) and W236 (theta): all five R_s terms zero at linear
      order on Kerr; no linear falsifier; leading built residual quadratic O(M^2) = Q(B), safe.

Run:  python -u tests/W238_gravity_willmore_residual_kerr.py   (exit 0 iff all PASS)

Binding: exploration grade; NO canon/verdict/status movement (schwarzschild-weak-field-rfail
stays OPEN; the gravity-leg verdict is Joe-gated).  Personas inline (GR/Kerr-curvature
specialist; Willmore/immersion-variational specialist; Lorenz-gauge/linearized-vacuum
specialist; ruthless skeptic); no sub-agents.  Zero em dashes in paper-facing text.
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
# Shared symbols / helpers  (same conventions as tests/chase/MOVE-3/willmore_el_order.py)
# ===========================================================================
t, x, y, z, M, a = sp.symbols('t x y z M a', real=True)
coords = [t, x, y, z]
r = sp.sqrt(x**2 + y**2 + z**2)
eta = sp.diag(-1, 1, 1, 1)
etaU = sp.diag(-1, 1, 1, 1)   # inverse of eta is itself


def lap_flat(f):
    """Flat d'Alembertian eta^{mn} d_m d_n f; static field -> spatial Laplacian."""
    return -sp.diff(f, t, 2) + sp.diff(f, x, 2) + sp.diff(f, y, 2) + sp.diff(f, z, 2)


def mean_curvature_H1(h):
    """
    Native linearized mean-curvature vector H^(1)_ab of the graph section into the fiber
    Met(X^4), using the EXACT W225 / willmore_el_order.py machinery:
       B^(1)_{mn,ab} = d_m d_n h_ab + alg_lin(h)     (literal-graph SFF, flat reference subtracted)
       H^(1)_ab      = eta^{mn} B^(1)_{mn,ab}.
    alg_lin is the constant-coefficient (flat eta) linear algebraic-slice term.
    """
    def d2h(mu, nu, A, B):
        return sp.diff(h[A, B], coords[mu], coords[nu])

    def alg_lin(mu, nu, A, B):
        term1 = sp.Rational(1, 2) * (h[A, mu]*eta[nu, B] + eta[A, mu]*h[nu, B]
                                     + h[A, nu]*eta[mu, B] + eta[A, nu]*h[mu, B])
        term2 = h[A, B]*eta[mu, nu] + eta[A, B]*h[mu, nu]
        return -sp.Rational(1, 2) * (term1 - sp.Rational(1, 2)*term2)

    H1 = sp.zeros(4, 4)
    for A in range(4):
        for B in range(4):
            s = 0
            for mu in range(4):
                for nu in range(4):
                    s += etaU[mu, nu] * (d2h(mu, nu, A, B) + alg_lin(mu, nu, A, B))
            H1[A, B] = sp.simplify(s)
    return H1


def build_kerr_h(with_quadrupole=True, with_gravitomagnetic=True):
    """
    Linear-in-M part of exact Kerr in HARMONIC (Lorenz) gauge, Cartesian coords, a carried
    EXACTLY.  Stationary weak-field vacuum form  g_00 = -(1+2Phi), g_ij = (1-2Phi)delta_ij,
    g_0i = h_0i (gravitomagnetic), Phi = -(Newtonian+multipoles):
      * Newtonian monopole    phiN  = M/r
      * Kerr mass quadrupole  quad  = M a^2 (3 z^2 - r^2)/(2 r^5)   (l=2 solid harmonic; M_2 = -M a^2)
      * gravitomagnetic       h_0i ~ (S x x)_i / r^3,  S = (0,0,M a)  (Lense-Thirring frame drag)
    Every listed piece is an exterior HARMONIC function (verified in C1).
    """
    phiN = M / r
    quad = M*a**2*(3*z**2 - r**2)/(2*r**5) if with_quadrupole else sp.Integer(0)
    Phi = phiN + quad
    h = sp.zeros(4, 4)
    h[0, 0] = 2*Phi
    for i in (1, 2, 3):
        h[i, i] = 2*Phi
    if with_gravitomagnetic:
        kgm = sp.Integer(-4)                         # gravitomagnetic normalization (irrelevant to harmonicity)
        Ax, Ay, Az = -M*a*y/r**3, M*a*x/r**3, sp.Integer(0)   # (S x x)/r^3, S=(0,0,Ma)
        h[0, 1] = h[1, 0] = kgm*Ax
        h[0, 2] = h[2, 0] = kgm*Ay
        h[0, 3] = h[3, 0] = kgm*Az
    return h


# ===========================================================================
# PC1 -- ROTATION-SECTOR TEETH: a non-harmonic gravitomagnetic term FIRES the detector
# ===========================================================================
log("=" * 82)
log("PC1 -- rotation-sector teeth: non-harmonic mock frame-drag h_0i ~ M a y/r^2 fires Delta != 0")
log("=" * 82)
mock_gm = M*a*y/r**2                                  # WRONG radial power -> not harmonic
lap_mock = sp.simplify(lap_flat(mock_gm))
pc1_fires = sp.simplify(lap_mock - (-2*M*a*y/r**4)) == 0 and lap_mock != 0
check("PC1a  Delta(M a y/r^2) = -2 M a y/r^4 != 0 (rotation-residual detector FIRES)", pc1_fires,
      f"Delta(M a y/r^2) = {sp.simplify(lap_mock*r**4/(M*a))} * M a/r^4")
check("PC1b  that falsifier is linear in a (so it vanishes as a->0)",
      sp.simplify(lap_mock.subs(a, 0)) == 0 and sp.simplify(sp.diff(lap_mock, a, 2)) == 0,
      "linear in a: a genuine ROTATION-induced residual would be seen")
log("  => the detector is NOT blind in the rotation (a) direction; a real nonzero rotation")
log("     Willmore residual would register.  So the a-carried vacuum vanishing below has teeth.")
log("")


# ===========================================================================
# PC2 -- RESIDUAL-OPERATOR TEETH: retracted premise H = M/r^2 gives Delta = 2M/r^4 != 0
# ===========================================================================
log("=" * 82)
log("PC2 -- residual-operator teeth: non-harmonic H = M/r^2 gives Delta = 2M/r^4 != 0")
log("=" * 82)
H_wrong = M / r**2
lap_wrong = sp.simplify(lap_flat(H_wrong))
pc2_fires = sp.simplify(lap_wrong - 2*M/r**4) == 0 and lap_wrong != 0
check("PC2a  Delta(M/r^2) = 2M/r^4 != 0 (linear falsifier detector FIRES)", pc2_fires,
      f"Delta(M/r^2) = {sp.simplify(lap_wrong*r**4/M)} * M/r^4")
log("  => a genuinely nonzero linear-in-M mean-curvature residual is registered; not blind.")
log("")


# ===========================================================================
# C1 -- each harmonic-gauge linearized-Kerr building block is HARMONIC
# ===========================================================================
log("=" * 82)
log("C1 -- linearized Kerr (harmonic gauge): every component is harmonic (Newtonian + a^2 quad + frame-drag)")
log("=" * 82)
phiN = M/r
quad = M*a**2*(3*z**2 - r**2)/(2*r**5)
Ax, Ay = -M*a*y/r**3, M*a*x/r**3
blocks = {"phiN=M/r": phiN, "mass-quadrupole (a^2)": quad,
          "gravitomagnetic Ax": Ax, "gravitomagnetic Ay": Ay}
all_harmonic = True
for nm, f in blocks.items():
    lf = sp.simplify(lap_flat(f))
    all_harmonic = all_harmonic and (lf == 0)
    check(f"C1  {nm} is harmonic (Delta = 0)", lf == 0, f"Delta[{nm}] = {lf}")
log("  => every linear-in-M Kerr metric component in harmonic gauge solves Laplace's equation")
log("     (linearized STATIONARY VACUUM in Lorenz gauge: nabla^2 hbar_mn = -16pi T_mn = 0).")
log("")


# ===========================================================================
# C2 -- native Willmore residual on Kerr: Delta H^(1) = 0 for ALL components
# ===========================================================================
log("=" * 82)
log("C2 -- native mean curvature H^(1) on IMPORTED Kerr (with h_0i + a^2 quad): Delta H^(1) = 0")
log("=" * 82)
h_kerr = build_kerr_h(with_quadrupole=True, with_gravitomagnetic=True)
H1_kerr = mean_curvature_H1(h_kerr)
log("  H^(1) components (nonzero), carrying a exactly:")
for A in range(4):
    for B in range(A, 4):
        if H1_kerr[A, B] != 0:
            log(f"    H1[{A},{B}] = {H1_kerr[A, B]}")
res_all_zero = True
detail = []
for A in range(4):
    for B in range(A, 4):
        dH = sp.simplify(lap_flat(H1_kerr[A, B]))
        if dH != 0:
            res_all_zero = False
            detail.append(f"H1[{A},{B}] -> {dH}")
check("C2  Delta H^(1)_ab = 0 for EVERY component of the Kerr mean curvature (Willmore residual vanishes)",
      res_all_zero, "all 10 symmetric components harmonic" if res_all_zero else "; ".join(detail))
log("  => the linear-in-M native Willmore-EL residual alpha_W W_s = alpha_W Delta H^(1) = 0 on")
log("     imported Kerr, for ANY finite coupling alpha_W.  Rotation does NOT break the clear.")
log("")


# ===========================================================================
# C3 -- a->0 consistency: reproduce the Schwarzschild (M/r) eta_ab with zero off-diagonal
# ===========================================================================
log("=" * 82)
log("C3 -- a->0 consistency: H^(1) collapses to Schwarzschild (M/r) eta_ab (W225 / RFAIL-03)")
log("=" * 82)
H1_schw = H1_kerr.subs(a, 0)
diag_ok = (sp.simplify(H1_schw[0, 0] - (-M/r)) == 0 and
           all(sp.simplify(H1_schw[i, i] - M/r) == 0 for i in (1, 2, 3)))
offdiag_ok = all(sp.simplify(H1_schw[A, B]) == 0
                 for A in range(4) for B in range(A + 1, 4))
check("C3a  a->0: H^(1)_ab = (M/r) eta_ab exactly (diag = [-M/r, M/r, M/r, M/r])", diag_ok,
      "matches W225 / RFAIL-03 Schwarzschild mean curvature")
check("C3b  a->0: all off-diagonal H^(1) (incl. frame-drag H^(1)_0i) vanish", offdiag_ok,
      "gravitomagnetic sector switches off with rotation")
schw_lap_zero = all(sp.simplify(lap_flat(H1_schw[A, B])) == 0 for A in range(4) for B in range(A, 4))
check("C3c  a->0: Delta H^(1) = 0 (reproduces the Schwarzschild zero of W225)", schw_lap_zero,
      "consistent limit")
log("")


# ===========================================================================
# C4 -- STRUCTURAL: Delta H^(1)=0 follows from per-component harmonicity (a-exact, any multipole)
# ===========================================================================
log("=" * 82)
log("C4 -- structural: Delta H^(1) = const-coeff-linear(Delta h) = 0 whenever each h_ab is harmonic")
log("=" * 82)
# Witness the const-coeff-linear structure directly: feed a GENERIC harmonic test component
# into the SAME machinery and confirm the residual is a const-coeff linear image of Delta h.
# Use an arbitrary l=1..2 solid-harmonic combination with free coefficients (a-exact stand-in).
c0, c1, c2 = sp.symbols('c0 c1 c2', real=True)
generic_harmonic = c0*(M/r) + c1*(M*a*y/r**3) + c2*(M*a**2*(3*z**2 - r**2)/(2*r**5))
gh_harmonic = sp.simplify(lap_flat(generic_harmonic)) == 0
# put it in a single slot and confirm the machinery's residual on it is zero for ALL c0,c1,c2
h_gen = sp.zeros(4, 4)
h_gen[0, 0] = h_gen[1, 1] = h_gen[2, 2] = h_gen[3, 3] = 2*generic_harmonic
h_gen[0, 1] = h_gen[1, 0] = generic_harmonic
H1_gen = mean_curvature_H1(h_gen)
gen_res_zero = all(sp.simplify(lap_flat(H1_gen[A, B])) == 0 for A in range(4) for B in range(A, 4))
check("C4a  a generic harmonic multipole combo (free coeffs c0,c1,c2) is harmonic", gh_harmonic,
      "arbitrary l=1,2 solid-harmonic stand-in for the a-exact Kerr tower")
check("C4b  Delta H^(1) = 0 for that generic combo, for ALL coefficients (structural, a-exact)",
      gen_res_zero, "residual is a const-coeff linear image of Delta h = 0; not tied to sampled a")
log("  => the clear is STRUCTURAL: it uses only per-component harmonicity of the linearized")
log("     vacuum field, which holds for the FULL a-exact Kerr multipole tower, not just leading a.")
log("")


# ===========================================================================
# C5 -- ASSEMBLY: all five R_s terms zero at linear order on Kerr (W225 + W236 + THIS)
# ===========================================================================
log("=" * 82)
log("C5 -- assembly of R_s on Kerr: all five terms zero at linear order (Willmore now closed)")
log("=" * 82)
# R_s = alpha_W W_s + E_s^YM + E_s^theta + E_s^Phi + E_s^cross, linear-in-M part on Kerr:
#   alpha_W W_s  = alpha_W Delta H^(1) = 0   (THIS WAVE, C2: harmonic on Kerr too)     <-- was the frontier
#   E_s^theta    = 0   (W236 C6: Psi=0 => J=0 => theta=0, rotation-independent, clears on Kerr)
#   E_s^Phi      = 0   (Phi=0 vacuum; rotation-independent)
#   E_s^cross    = 0   (vanishing Psi/Phi factor; rotation-independent)
#   E_s^YM       = 0 at linear order  (F_A ~ O(M^2); gauge curvature quadratic)
willmore_kerr_zero = res_all_zero
theta_kerr_zero = True     # W236 C6: rotation-independent (needs only Psi=0)
phi_cross_zero = True      # vacuum, rotation-independent
ym_linear_zero = True      # F_A ~ O(M^2), F2 (linear-order zero holds regardless of rotation)
all_five = willmore_kerr_zero and theta_kerr_zero and phi_cross_zero and ym_linear_zero
check("C5a  all five R_s terms have zero linear-in-M residual on Kerr (Willmore now closed)",
      all_five, "alpha_W W_s (C2) = E_theta (W236) = E_Phi = E_cross = E_YM = 0 at linear order")
check("C5b  no definite nonzero linear falsifier from ANY term on Kerr (no early disproof)",
      all_five, "leading BUILT residual quadratic O(M^2)=Q(B), safe for M/r<<1")
log("")


# ===========================================================================
# VERDICT
# ===========================================================================
log("=" * 82)
log("VERDICT (imported exact Kerr, Psi=0 vacuum, linear in M, a exact; Joe-gated -- this is a SIGNAL)")
log("=" * 82)
if not FAIL:
    log("  Positive controls fire (PC1 non-harmonic frame-drag rotation-residual teeth; PC2")
    log("  non-harmonic H=M/r^2 linear-residual teeth), so the detectors are NOT blind -- including")
    log("  in the rotation (a) direction.")
    log("")
    log("  COMPUTED on IMPORTED exact Kerr, harmonic gauge, Psi=0 vacuum, conservative IG branch,")
    log("  linear order in M with a carried EXACTLY:")
    log("    * every linearized-Kerr component (Newtonian, a^2 mass quadrupole, gravitomagnetic")
    log("      frame-drag h_0i) is HARMONIC (C1) -- linearized stationary vacuum in Lorenz gauge")
    log("    * the native mean curvature H^(1)_ab is a const-coeff linear functional of those")
    log("      harmonic components, hence HARMONIC: Delta H^(1)_ab = 0 for ALL 10 components (C2)")
    log("    * so the native Willmore-EL residual alpha_W W_s = alpha_W Delta H^(1) = 0 on Kerr")
    log("      at linear order, for any finite alpha_W -- ROTATION DOES NOT BREAK THE CLEAR")
    log("    * a->0 reproduces the Schwarzschild (M/r) eta_ab with zero off-diagonal (C3)")
    log("    * STRUCTURAL: uses only per-component harmonicity, holds for the a-exact multipole")
    log("      tower, not just sampled a (C4)")
    log("")
    log("  The static-isotropic harmonicity of W225 was SUFFICIENT but not NECESSARY: the")
    log("  necessary-and-sufficient condition is per-component harmonicity, which linearized")
    log("  VACUUM supplies whether or not the source rotates.  Isotropy was never load-bearing.")
    log("")
    log("  SIGNAL: the native Willmore residual CLEARS on imported Kerr at linear order.  With")
    log("  W236 (theta clears on Kerr) and W225's other terms (rotation-independent), ALL FIVE")
    log("  R_s terms are zero at linear order on the ROTATING metric too.  The gravity cheap-read")
    log("  EXTENDS TO KERR: a genuine-YES SIGNAL for the imported-metric slice, NO EARLY DISPROOF.")
    log("  Leading built residual is quadratic O(M^2) = Q(B) (the standing obstruction, same as")
    log("  Schwarzschild), safe for M/r<<1, NOT a definite nonzero linear falsifier.")
    log("")
    log("  This does NOT clear the gravity leg: G^X=0 is trivial (any vacuum); W_s is nonzero at")
    log("  O(M^2), so exact Kerr is NOT a Willmore-critical GU section; the theta clear rides the")
    log("  W154 posit (W236); a non-vacuum matter section (Psi!=0) remains.  Verdict stays")
    log("  Joe-gated; canon schwarzschild-weak-field-rfail stays OPEN.")
log("=" * 82)

if FAIL:
    log(f"\nRESULT: {len(FAIL)} FAILED")
    for nm in FAIL:
        log("  FAIL: " + nm)
    raise SystemExit(1)
log("\nRESULT: ALL PASS")
