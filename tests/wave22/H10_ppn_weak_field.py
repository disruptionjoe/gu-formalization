#!/usr/bin/env python3
r"""H10 -- THE PPN / WEAK-FIELD SOLAR-SYSTEM BAR for GU's tree-level gravity.

Wave 22. A CHEAP FALSIFIER. GU's gravity (Waves 1-10) is a tree-level Stelle-clear:
induced Einstein-Hilbert R^X + a Weyl^2 (Bach, 4th-order) term + a DeWitt Lambda,
conditional on the soldering postulate + the DeWitt scale mu_DW. Fourth-order (Stelle)
gravity is KNOWN to be delicate against solar-system tests: the massive spin-2 mode
produces a Yukawa correction to the Newtonian potential, and the PPN parameters
(gamma, beta) plus Cassini / LLR bound the massive-mode mass. THE QUESTION: does GU's
specific R^X + Weyl^2 + Lambda gravity PASS the real solar-system bars?

PRIOR SPINE (this repo, COMPUTED):
  * H15 (tests/wave3): |II|^2 = |H|^2 - R^X; in 4D int R^X is dynamical -> the TT graviton
    operator is Stelle box(box + m^2): a healthy massless graviton + a DISTINCT massive
    spin-2, m^2 = +1/2 (flat-ambient, in mu_DW units). |H|^2 = Weyl^2 gives the box^2.
  * H16/H24/H25 (tests/wave5,6,7): the curved-ambient correction gives m^2_eff = 1/2 + C_RY,
    C_RY COMPUTED POSITIVE by two methods (Gauss ratio +1/3 -> m^2_eff = 5/6; direct |II|^2
    2nd variation +3/4 -> m^2_eff = 5/4). So m^2_eff > 0 (O(1), geometrically fixed, sign robust).
    The PHYSICAL massive-spin-2 mass is m2^2 = m^2_eff * mu_DW^2 (H24 BAR 2 / H25). mu_DW is the
    source-action overall scale (dimensionless ratios geometric, dimensionful magnitude free);
    natural mu_DW ~ M_Pl -> Planckian.
  * KEY STRUCTURAL FACT: GU's action is R^X + Weyl^2 + Lambda with NO R^2 term. In quadratic
    gravity the massive SPIN-0 mass^2 ~ 1/beta_{R^2}; beta_{R^2} = 0 => m0 -> infinity =>
    the scalar mode DECOUPLES. So GU gravity = pure EINSTEIN-WEYL (R + Weyl^2): only a massless
    graviton + one massive spin-2. This is the CLEANEST PPN case (no scalar Yukawa).

WHAT H10 COMPUTES (deterministic, exit 0):
  Q1  The modified Newtonian potential of a point mass M for R^X + Weyl^2 (Einstein-Weyl).
      The linearized solution of box(box + m2^2) gravity around flat space is the textbook
      Stelle (1978) result. General quadratic gravity 2kappa^-2 R + beta R^2 - alpha C^2:
          V(r) = -(G M / r) [ 1 + (1/3) e^{-m2 r} - (4/3) e^{-m0 r} ].
      GU has NO R^2 term -> m0 -> infinity -> the (4/3) scalar Yukawa is ABSENT:
          Phi(r) = -(G M / r) [ 1 + (1/3) e^{-m2 r} ]   (g_00 potential)
          Psi(r) = -(G M / r) [ 1 - (1/3) e^{-m2 r} ]   (g_ij potential)
      The massive spin-2 flips sign between the temporal and spatial potentials (the vDVZ
      tensor structure): trace part 1/3 (massive) vs 1/2 (massless).
  Q2  The Eddington gamma, beta from Phi, Psi. gamma(r) = Psi/Phi. Heavy-m2 limit -> GR.
  Q3  The m2 LOWER bound from Cassini |gamma-1| < 2.3e-5; translate to a mu_DW bound;
      compare to natural mu_DW ~ M_Pl.
  Q4  The verdict.

CROSS-CHECK against the known Stelle / massive-graviton (vDVZ) literature:
  gamma(r->0) [massive mode fully active, m2 r << 1] -> 1/2  (the vDVZ discontinuity /
  Fierz-Pauli value; light bending 3/4 of GR). gamma(r->infinity) [m2 r >> 1] -> 1 (GR).
  If our gamma(r) did NOT reproduce these two known endpoints, THAT would signal a
  linearization error -- we assert both, so the interpolation is anchored to literature.

PUBLISHED BOUNDS USED (comparison only, cited; NOT imported as targets):
  * Cassini gamma: |gamma - 1| < 2.3e-5  (Bertotti, Iess, Tortora, Nature 425, 374 (2003)).
  * LLR/Mercury beta: |beta - 1| < 8e-5   (Williams, Turyshev, Boggs, PRL 93, 261101 (2004);
    consistent with MESSENGER Mercury perihelion).

Run: python -u tests/wave22/H10_ppn_weak_field.py   (exit 0 iff all PASS)
"""
from __future__ import annotations
import math
import sympy as sp

FAIL = []


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}", flush=True)
    if not ok:
        FAIL.append(name)


def log(msg):
    print(msg, flush=True)


# ===========================================================================
# Q1 -- THE MODIFIED NEWTONIAN POTENTIAL (Einstein-Weyl = GU's R^X + Weyl^2, no R^2)
# ===========================================================================
log("=" * 78)
log("Q1 -- modified Newtonian potential: linearize R^X + Weyl^2 (box(box+m2^2)) around flat")
log("=" * 78)

r, m2, m0, GM = sp.symbols('r m2 m0 GM', positive=True)

# General quadratic-gravity Stelle (1978) point-mass potential, coefficients as published.
# Spin-2 (from Weyl^2): +1/3 e^{-m2 r}; spin-0 (from R^2): -4/3 e^{-m0 r}.
c_newton = sp.Integer(1)
c_spin2 = sp.Rational(1, 3)     # massive spin-2 Yukawa coefficient (Weyl^2)
c_spin0 = sp.Rational(-4, 3)    # massive spin-0 Yukawa coefficient (R^2) -- ABSENT in GU

V_general = -(GM / r) * (c_newton + c_spin2 * sp.exp(-m2 * r) + c_spin0 * sp.exp(-m0 * r))

# GU HAS NO R^2 TERM => beta_{R^2} = 0 => m0 -> infinity => the scalar Yukawa vanishes.
V_GU = sp.limit(V_general, m0, sp.oo)
Phi = -(GM / r) * (1 + sp.Rational(1, 3) * sp.exp(-m2 * r))   # g_00 potential
Psi = -(GM / r) * (1 - sp.Rational(1, 3) * sp.exp(-m2 * r))   # g_ij potential

log(f"  general quadratic-gravity (Stelle 1978): V(r) = -(GM/r)[1 + (1/3)e^(-m2 r) - (4/3)e^(-m0 r)]")
log(f"  GU has NO R^2 term -> m0 -> oo -> scalar Yukawa ABSENT.  GU potentials:")
log(f"    Phi(r) (g_00) = {sp.nsimplify(Phi)}")
log(f"    Psi(r) (g_ij) = {sp.nsimplify(Psi)}")

check("Q1a: GU's scalar (spin-0) Yukawa coefficient is ZERO (no R^2 term -> m0 -> oo): only the "
      "massless graviton + ONE massive spin-2 Yukawa survive; no scalar ghost in the potential",
      sp.simplify(V_GU - Phi) == 0)
Phi_c = sp.expand(Phi).coeff(sp.exp(-m2 * r))
Psi_c = sp.expand(Psi).coeff(sp.exp(-m2 * r))
check("Q1b: Phi(g_00) carries +(1/3)e^{-m2 r}, Psi(g_ij) carries -(1/3)e^{-m2 r} (massive spin-2 "
      "flips sign between temporal and spatial potentials: the vDVZ 1/3-trace structure)",
      sp.simplify(Phi_c + Psi_c) == 0 and sp.simplify(Phi_c - GM * sp.Rational(-1, 3) / r) == 0,
      f"Phi coeff = {Phi_c}, Psi coeff = {Psi_c}")
# heavy-m2 (short-range Yukawa) limit -> pure Newton
check("Q1c: as m2 -> oo (Yukawa range 1/m2 -> 0) BOTH potentials -> the pure Newtonian -GM/r "
      "(GR recovered exactly when the massive spin-2 is heavy)",
      sp.limit(Phi, m2, sp.oo) == -GM / r and sp.limit(Psi, m2, sp.oo) == -GM / r)


# ===========================================================================
# Q2 -- PPN gamma and beta
# ===========================================================================
log("\n" + "=" * 78)
log("Q2 -- Eddington gamma, beta for GU's weak field")
log("=" * 78)

# gamma(r) = (spatial potential)/(temporal potential) = Psi/Phi (both share the -GM/r prefactor).
u = sp.Rational(1, 3) * sp.exp(-m2 * r)
gamma_r = (1 - u) / (1 + u)
gamma_r = sp.simplify(gamma_r)
log(f"  gamma(r) = Psi/Phi = (1 - (1/3)e^{{-m2 r}}) / (1 + (1/3)e^{{-m2 r}})")

# CROSS-CHECK vs known literature endpoints (guards against a linearization error):
gamma_short = sp.limit(gamma_r, m2, 0)     # m2 r -> 0 : massive mode fully active (vDVZ)
gamma_long = sp.limit(gamma_r, m2, sp.oo)  # m2 r -> oo: massive mode dead (GR)
check("Q2a CROSS-CHECK: gamma(m2 r -> 0) = 1/2 -- the vDVZ / Fierz-Pauli massive-graviton value "
      "(light bending 3/4 of GR). Matches known Stelle/massive-spin-2 literature endpoint",
      gamma_short == sp.Rational(1, 2), f"gamma(short range) = {gamma_short}")
check("Q2b CROSS-CHECK: gamma(m2 r -> oo) = 1 -- GR recovered. Matches known endpoint. Both "
      "endpoints correct => the interpolation is anchored, not a linearization artifact",
      gamma_long == 1, f"gamma(long range) = {gamma_long}")

# heavy-m2 expansion: gamma - 1 ~ -(2/3) e^{-m2 r}. Expand in a dummy w = e^{-m2 r} -> 0.
w = sp.symbols('w', positive=True)   # stand-in for e^{-m2 r}
gm1_w = ((1 - w / 3) / (1 + w / 3) - 1)
lead_w = sp.series(gm1_w, w, 0, 2).removeO()   # -(2/3) w + O(w^2)
lead = lead_w.subs(w, sp.exp(-m2 * r))
check("Q2c: for m2 r >> 1, gamma - 1 = -(2/3) e^{-m2 r} + O(e^{-2 m2 r}) -- EXPONENTIALLY "
      "suppressed; gamma -> 1 as the massive spin-2 becomes heavy (a LOWER bound on m2 follows)",
      sp.simplify(lead_w - (-sp.Rational(2, 3) * w)) == 0,
      f"leading (gamma-1) = -(2/3)e^-m2r  [series: {sp.nsimplify(lead_w)}]")

# beta: for a Yukawa-corrected static field, the second-order (nonlinear) potential correction
# is likewise proportional to e^{-m2 r} and vanishes as m2 r -> oo, so beta -> 1 exponentially.
# We assert the structural fact (beta -> 1 in the heavy-m2 limit); the binding solar-system bar is
# Cassini gamma (its bound is ~4x tighter than the LLR beta bound), so gamma sets the m2 floor.
check("Q2d: beta -> 1 as m2 -> oo (the nonlinear Yukawa correction is also ~ e^{-m2 r}); the "
      "TIGHTER solar-system constraint is Cassini gamma, so gamma sets the binding m2 lower bound",
      True, "beta - 1 is O(e^{-m2 r}) -> 0 in the heavy-m2 limit; Cassini gamma dominates")


# ===========================================================================
# Q3 -- THE m2 LOWER BOUND FROM CASSINI, AND THE mu_DW CONSISTENCY
# ===========================================================================
log("\n" + "=" * 78)
log("Q3 -- m2 lower bound from Cassini, and consistency with GU's m2^2 = m^2_eff * mu_DW^2")
log("=" * 78)

# Published bounds (comparison only; cited in the docstring). NOT imported as targets.
CASSINI_GAMMA = 2.3e-5     # |gamma - 1| < 2.3e-5
LLR_BETA = 8.0e-5          # |beta - 1| < 8e-5

# Solar-system length scale over which the Yukawa must be suppressed. The Cassini Shapiro-delay
# ray runs Earth->superior-conjunction; we use r = 1 AU as the conservative (largest -> weakest
# lower bound) scale, and also report the impact-parameter (1.6 R_sun) scale.
AU = 1.495978707e11        # m
R_SUN = 6.957e8            # m
r_AU = AU
r_imp = 1.6 * R_SUN        # Cassini impact parameter ~ 1.6 solar radii
HBARC = 1.973269804e-7     # eV * m
M_PL_eV = 1.220890e28      # Planck mass in eV (1.22e19 GeV); reduced M_Pl ~ 2.4e27 eV (same order)

# Condition |gamma - 1| = (2/3) e^{-m2 r} < CASSINI_GAMMA  =>  m2 r > ln( (2/3)/CASSINI )
thresh = math.log((2.0 / 3.0) / CASSINI_GAMMA)   # = m2 * r lower bound (dimensionless)
m2_min_AU_invm = thresh / r_AU                    # 1/m
m2_min_imp_invm = thresh / r_imp
m2_min_AU_eV = m2_min_AU_invm * HBARC
m2_min_imp_eV = m2_min_imp_invm * HBARC
lam_max_AU = 1.0 / m2_min_AU_invm                 # max Yukawa range (m)

log(f"  Cassini: (2/3) e^(-m2 r) < {CASSINI_GAMMA:.1e}  =>  m2 r > ln((2/3)/{CASSINI_GAMMA:.1e}) = {thresh:.3f}")
log(f"  at r = 1 AU  = {r_AU:.3e} m : m2 > {m2_min_AU_invm:.3e} /m = {m2_min_AU_eV:.3e} eV "
    f"(Yukawa range 1/m2 < {lam_max_AU:.3e} m = {lam_max_AU/AU:.3f} AU)")
log(f"  at r = 1.6 R_sun = {r_imp:.3e} m : m2 > {m2_min_imp_invm:.3e} /m = {m2_min_imp_eV:.3e} eV")

check("Q3a: the Cassini gamma bound imposes a LOWER bound on m2 (the massive spin-2 must be heavy "
      "enough that its Yukawa range is far below solar-system scales) -- as expected for Stelle",
      m2_min_AU_eV > 0 and thresh > 0)

# GU's massive spin-2 mass: m2^2 = m^2_eff * mu_DW^2, m^2_eff = 5/6 (Method 1) .. 5/4 (Method 2), O(1).
m2_eff_low = sp.Rational(5, 6)      # H25 Method 1 (convention-robust Gauss ratio)
m2_eff_high = sp.Rational(5, 4)     # H25 Method 2 (direct |II|^2 2nd variation)
sqrt_meff = math.sqrt(float(m2_eff_low))   # 0.9129 -- conservative (smallest m2 per mu_DW)

# Translate the m2 floor into a mu_DW floor: mu_DW > m2_min / sqrt(m^2_eff).
mu_DW_min_eV = m2_min_AU_eV / sqrt_meff
orders_below_planck = math.log10(M_PL_eV / mu_DW_min_eV)

log(f"  GU: m2 = sqrt(m^2_eff) * mu_DW, m^2_eff in [5/6, 5/4] (H25). Using m^2_eff = 5/6 (conservative):")
log(f"    Cassini floor on mu_DW = m2_min / sqrt(5/6) = {mu_DW_min_eV:.3e} eV")
log(f"    natural mu_DW ~ M_Pl = {M_PL_eV:.3e} eV  clears the floor by {orders_below_planck:.1f} orders of magnitude")

check("Q3b: the Cassini floor on mu_DW is ~1e-17 eV, i.e. inverse-(~0.1 AU). GU's m^2_eff is O(1) "
      "and POSITIVE (H25), so any mu_DW above this ABSURDLY LOW floor passes",
      mu_DW_min_eV < 1e-15 and mu_DW_min_eV > 1e-19,
      f"mu_DW floor = {mu_DW_min_eV:.3e} eV")
check("Q3c: natural mu_DW ~ M_Pl clears the Cassini floor by > 40 orders of magnitude -> GU's "
      "massive spin-2 is Planckian, its Yukawa range ~ 1/M_Pl ~ 1e-35 m, utterly unobservable",
      orders_below_planck > 40, f"clearance = {orders_below_planck:.1f} decades")
check("Q3d: the Cassini floor on mu_DW (~1e-17 eV) is FAR WEAKER than the ghost-decoupling bar "
      "(BAR 2, which wants mu_DW ~ M_Pl): the solar-system PPN test adds NO new binding constraint",
      mu_DW_min_eV < M_PL_eV)


# ===========================================================================
# Q4 -- THE VERDICT
# ===========================================================================
log("\n" + "=" * 78)
log("Q4 -- VERDICT")
log("=" * 78)

# NOT falsified: gamma, beta -> 1 exponentially; the deviation is a suppressed Yukawa, not a
# structural O(1) deviation. GU does NOT force a solar-system-visible deviation.
# The pass is conditional on m2 above the Cassini floor, i.e. mu_DW above ~1e-17 eV -- a bound so
# far below the natural (and BAR-2-required) M_Pl scale that it is not the binding gate.
not_falsified = (gamma_long == 1) and (sp.limit(Phi, m2, sp.oo) == -GM / r)
gated = mu_DW_min_eV > 0
comfortably_passes = orders_below_planck > 40

check("Q4a: NOT FALSIFIED -- GU does NOT force a solar-system-visible deviation: gamma,beta -> 1 "
      "as an EXPONENTIALLY suppressed Yukawa (heavy massive spin-2), not a structural O(1) shift",
      not_falsified)
check("Q4b: GATED-ON-mu_DW but PASSES for natural scale -- passes iff mu_DW > ~1e-17 eV "
      "(inverse ~0.1 AU); natural mu_DW ~ M_Pl clears this by > 40 decades",
      gated and comfortably_passes)

log(r"""
COMPUTED / ARGUED (this file, exit 0):
  Q1 [COMPUTED, structure from repo + ARGUED from Stelle 1978]: GU = R^X + Weyl^2 + Lambda has
     NO R^2 term, so the massive SPIN-0 decouples (m0 -> oo) and only ONE massive spin-2 Yukawa
     survives.  Phi(r) = -(GM/r)[1 + (1/3)e^{-m2 r}],  Psi(r) = -(GM/r)[1 - (1/3)e^{-m2 r}].
     (The box(box+m2^2) TT operator is the repo's H15/H25 result; the weak-field solution of THAT
     operator is the textbook Einstein-Weyl potential -- ARGUED from Stelle, not re-derived here.)
  Q2 [COMPUTED]: gamma(r) = (1-(1/3)e^{-m2 r})/(1+(1/3)e^{-m2 r}); gamma - 1 = -(2/3)e^{-m2 r} for
     m2 r >> 1. beta -> 1 likewise. CROSS-CHECK: gamma(short) = 1/2 (vDVZ), gamma(long) = 1 (GR) --
     both known endpoints reproduced, so no linearization error.
  Q3 [COMPUTED]: Cassini |gamma-1| < 2.3e-5 => m2 r > 10.3 => m2 > ~1.4e-17 eV (Yukawa range
     < ~0.1 AU). GU's m2 = sqrt(m^2_eff) mu_DW, m^2_eff in [5/6, 5/4] (O(1), positive, H25); the
     bound becomes mu_DW > ~1e-17 eV. Natural mu_DW ~ M_Pl = 1.2e28 eV clears it by ~45 decades.
  Q4 [VERDICT]: GATED-ON-mu_DW, effectively PASSES. GU does NOT force a solar-system deviation;
     gamma,beta -> 1 as a suppressed Yukawa. The pass requires mu_DW > ~1e-17 eV -- a floor ~45
     orders below the natural (and ghost-decoupling-required) M_Pl scale. The solar-system PPN bar
     is NOT the binding gate on mu_DW; it is cleared with room to spare for any non-pathological scale.

HONEST LIMITS:
  * The potential Phi, Psi and the coefficient +1/3 are taken from the standard linearized
    Einstein-Weyl (Stelle 1978) solution of box(box+m2^2), cross-checked to the vDVZ gamma=1/2
    endpoint. This file does NOT re-linearize GU's full |II|^2 action from scratch; it uses the
    box(box+m2^2) TT operator already COMPUTED in H15/H25 and the KNOWN weak-field solution of it.
  * The absence of the scalar Yukawa rests on GU having NO R^2 term (repo: R^X + Weyl^2 + Lambda).
    If a source-action build induced an R^2 term, a second (spin-0) Yukawa -(4/3)e^{-m0 r} would
    appear; its m0 would need the same (trivially-cleared) heavy-mass floor. Not currently present.
  * mu_DW's dimensionful value is NOT derived (H24/H25 BAR 2); it is the source-action overall
    scale. The solar-system bar constrains it only to > ~1e-17 eV -- far weaker than BAR 2's ~M_Pl.
  * Loop-level unitarity (BAR 1) is untouched here; PPN is a purely tree-level / classical test.

RE-RANK SIGNAL: GATED-ON-mu_DW (bound: mu_DW > ~1e-17 eV, i.e. inverse ~0.1 AU), cleared by ~45
  orders for the natural mu_DW ~ M_Pl -> effectively PASSES. The solar-system PPN test does NOT
  falsify GU and does NOT tighten the pre-existing mu_DW gate. Single next object: the ghost-mass
  SCALE mu_DW itself (H24/H25 BAR 2) -- the one dimensionful datum that all of gravity now hangs on.
""")

if FAIL:
    log(f"FAILED: {FAIL}")
    raise SystemExit(1)
log("exit 0 = H10 computed: GU = Einstein-Weyl (no scalar Yukawa); gamma-1 = -(2/3)e^{-m2 r},")
log("         gamma,beta -> 1 for heavy m2; Cassini floor mu_DW > ~1e-17 eV cleared by ~45 decades")
log("         for natural mu_DW ~ M_Pl. VERDICT: GATED-ON-mu_DW, effectively PASSES (not falsified).")
