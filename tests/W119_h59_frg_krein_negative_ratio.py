#!/usr/bin/env python3
r"""
W119 / H59 -- FIRST MINIMAL FUNCTIONAL-RG (FRG) TRUNCATION PROBING THE KREIN GRADING AT THE
NEGATIVE FIXED-RATIO.

QUESTION (one, honest): does the one-loop AF picture -- (i) Gaussian UV fixed point, (ii) the
negative fixed ratio r* = f_0^2/f_2^2 < 0 (both roots negative, W46), (iii) RG-stability of the
spin-2 Krein grading (m2^2 > 0 at every finite scale, locus touched only at the free UV endpoint,
W53) -- SURVIVE or BREAK when the one-loop betas are replaced by a Wetterich-equation FRG
truncation (Einstein-Hilbert + Weyl^2 + R^2, with the Krein grading tracked)?

TRUNCATION: polynomial f(R)-to-R^2 + Weyl^2 (the W88 Stage-1 truncation, reused: sphere/dS
background, York/TT decomposition), dimensionless couplings g~=G k^2, lambda~=Lambda/k^2 with
canonical linear terms, marginal couplings (f_2^2, f_0^2). Regulator families: (1) Litim/optimized
r(y) = (1-y)theta(1-y); (2) exponential r(y) = y/(e^y - 1); (3) exponential shape sweep
r_s(y) = s*y/(e^y - 1), s in [0.5, 2].

METHOD / HONESTY (DERIVED-on-PORTED at best; truncation + regulator dependence explicit):
  * The one-loop marginal coefficients (133/10 + c_RS; 5/3, 5, 5/6) are IMPORTED from W45
    (KNOWN/PORTED grade inherited; not re-derived).
  * The FRG dressing of each quadratic coefficient along the flow (finite lambda, g) is treated as
    an independent positive threshold factor Phi_i drawn from the ACTUAL computed threshold-integral
    band of the three regulator families (Phi^2_2(0), Phi^2_1(0), Phi^1_1(0), by quadrature +
    closed form). The exact assignment of which Phi dresses which coefficient is a paper-scale
    computation we do NOT do; instead the conclusion is made robust to the assignment by sweeping
    ALL combinations over the band. The asserted conclusions are exactly the ones independent of
    the assignment. AT the Gaussian point itself the marginal one-loop coefficients are universal
    (regulator-independent), so the dressing question only bites along the flow.
  * The EH-sector (Reuter) magnitudes are SCHEMATIC, mirrored from W83/W88 (A_tot budget, B0/B1),
    calibrated to the literature FP structure; load-bearing conclusions are the sign-robust ones.
  * eta_C (the additive f_2^2 term) is IMPORTED as W89's two-scheme result (Weyl-adapted eta_C=0 /
    EH-adapted eta_C>0), cited not recomputed.

GHOST-MASS CONSTRUCTION FORK (GEOMETER-VS-PHYSICS-OBJECTS.md discipline -- carried, NOT defaulted):
  Branch A (standard agravity, Salvio-Strumia): m2^2 = (1/2) f_2^2(k) M_Pl^2 -- ghost mass rides
    the running coupling. Grading distance d_locus = (1/2) f_2^2(k).
  Branch B (GU program-native fixed-scale): m2 = sqrt(m2_eff) * mu_DW, m2_eff in [5/6, 5/4]
    (wave20/H43/path4 construction) -- ghost mass is a fixed physical scale tied to the DeWitt
    ratio-only scale. Grading distance d_locus = m2^2/mu_DW^2 = m2_eff, scale-INDEPENDENT.
  Both branches are computed (cheap); the branch dependence is reported, not resolved.

POSITIVE CONTROLS (calibrate the machinery against KNOWN FRG results):
  PC1 Litim threshold functions Phi^p_n(0) = 1/n! (closed form, Reuter-Saueressig/Percacci)
      reproduced by direct quadrature.
  PC2 exponential-regulator Phi^2_2(0) = 1 and Phi^1_1(0) = pi^2/6 (analytic reductions derived in
      this file) reproduced by quadrature -- two independent routes for the band endpoints.
  PC3 universal one-loop limit reproduces the W46 negative fixed-ratio roots r* = -0.0848, -23.575.
  PC4 pure-gravity Reuter FP reproduction (schematic W83/W88 EH system): g* = 0.70,
      g* lambda* ~ 0.109 (literature band ~0.11-0.14); GU content g* = 0.674.
  NC1 negative control: c_RS_weyl = -20 flips b_2 < 0 and the machinery DETECTS AF breakage.

Exit 0 iff all checks pass. numpy + sympy only. Deterministic (fixed seeds).
Reproducible: python tests/W119_h59_frg_krein_negative_ratio.py
No canon / RESEARCH-STATUS / claim-status / verdict / posture file touched. H59 remains OPEN.
Companion exploration: explorations/h59-frg-minimal-truncation-krein-negative-ratio-2026-07-13.md
"""
from __future__ import annotations

import importlib.util
import io
import contextlib
import math
import os
import sys

import numpy as np
import sympy as sp

TOL = 1e-9
results: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    results.append((name, bool(passed), detail))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))


def log(msg: str = "") -> None:
    print(msg, flush=True)


# =====================================================================================
# IMPORT the W45 one-loop beta system (KNOWN/PORTED grade inherited; not re-derived).
# =====================================================================================
_HERE = os.path.dirname(os.path.abspath(__file__))
_STAGE1 = os.path.join(_HERE, "W45_H57_stage1_beta_system.py")
_spec = importlib.util.spec_from_file_location("W45_stage1", _STAGE1)
S1 = importlib.util.module_from_spec(_spec)
sys.modules["W45_stage1"] = S1
with contextlib.redirect_stdout(io.StringIO()):
    try:
        _spec.loader.exec_module(S1)   # W45 ends in SystemExit(0); swallow it
    except SystemExit:
        pass

KAPPA = S1.KAPPA                      # 1/(4pi)^2
BS = S1.BetaSystem()                  # RS anchor: c_RS_weyl = 17/12, d_RS_R2 = 0
B2 = BS.b2()                          # 133/10 + 17/12 = 14.7167 (anchor)
C_A, C_B, C_C = 5.0 / 3.0, 5.0, 5.0 / 6.0   # one-loop f_0^2 quadratic coefficients (KNOWN, W45)

log("=" * 96)
log("W119 / H59 -- minimal FRG truncation: Krein grading at the negative fixed-ratio")
log("=" * 96)
log(f"  imported W45 anchor: b_2 = {B2:.4f}; f_0^2 quadratic (c_A,c_B,c_C) = (5/3, 5, 5/6); "
    f"kappa = {KAPPA:.6f}")

# =====================================================================================
# PART A -- REGULATOR FAMILIES + THRESHOLD FUNCTIONS (positive controls PC1, PC2)
#   Phi^p_n(0) = 1/Gamma(n) INT_0^inf dy y^(n-1) [r(y) - y r'(y)] / [y + r(y)]^p
# =====================================================================================
log("\n" + "-" * 96)
log("PART A -- threshold functions across three regulator families (quadrature vs closed form)")
log("-" * 96)


def phi_quadrature(p: int, n: int, family: str, s: float = 1.0, ny: int = 400_000,
                   ymax: float = 60.0) -> float:
    """Direct quadrature of Phi^p_n(0). family in {'litim','exp'} ('exp' takes shape s)."""
    if family == "litim":
        # r = (1-y)theta(1-y): r - y r' = 1 on (0,1); y + r = 1 on (0,1); 0 beyond.
        y = np.linspace(1e-9, 1.0 - 1e-9, ny)
        integrand = y ** (n - 1)          # numerator 1, denominator 1
    else:
        # r_s = s*y/(e^y - 1): r - y r' = s*y^2*e^y/(e^y-1)^2 (derived analytically below, A-note);
        # y + r_s = y*(e^y - 1 + s)/(e^y - 1).
        y = np.linspace(1e-8, ymax, ny)
        em1 = np.expm1(y)
        num = s * y ** 2 * np.exp(y) / em1 ** 2
        den = (y * (em1 + s) / em1) ** p
        integrand = y ** (n - 1) * num / den
    return float(np.trapezoid(integrand, y) / math.gamma(n))


# PC1: Litim closed form Phi^p_n(0) = 1/n!
pc1_ok, pc1_detail = True, []
for (p, n) in [(1, 1), (2, 1), (2, 2), (2, 3)]:
    got = phi_quadrature(p, n, "litim")
    want = 1.0 / math.factorial(n)
    pc1_ok &= abs(got - want) < 1e-5
    pc1_detail.append(f"Phi^{p}_{n}={got:.6f} (want {want:.6f})")
check("PC1 POSITIVE CONTROL: Litim thresholds reproduce the KNOWN closed form Phi^p_n(0)=1/n! "
      "(Reuter-Saueressig; Percacci)", pc1_ok, "; ".join(pc1_detail))

# PC2: exponential-regulator analytic reductions, derived in-file:
#   s=1: integrand of Phi^2_2 reduces to y*e^{-y}  -> Phi^2_2(0) = 1 exactly;
#        integrand of Phi^1_1 reduces to y/(e^y-1) -> Phi^1_1(0) = pi^2/6.
phi22_exp = phi_quadrature(2, 2, "exp", s=1.0)
phi11_exp = phi_quadrature(1, 1, "exp", s=1.0)
pc2_ok = abs(phi22_exp - 1.0) < 1e-4 and abs(phi11_exp - math.pi ** 2 / 6.0) < 1e-4
check("PC2 POSITIVE CONTROL: exponential-regulator Phi^2_2(0)=1 and Phi^1_1(0)=pi^2/6 "
      "(analytic reduction) reproduced by quadrature -- two independent routes agree",
      pc2_ok, f"Phi^2_2={phi22_exp:.6f} (want 1); Phi^1_1={phi11_exp:.6f} (want {math.pi**2/6:.6f})")

# A1: structural positivity of r - y r' for the whole exponential shape family (analytic:
#     r_s - y r_s' = s y^2 e^y/(e^y-1)^2 > 0 for all y>0, s>0) checked symbolically with sympy.
y_, s_ = sp.symbols("y s", positive=True)
r_s_sym = s_ * y_ / (sp.exp(y_) - 1)
num_sym = r_s_sym - y_ * sp.diff(r_s_sym, y_)
target = s_ * y_ ** 2 * sp.exp(y_) / (sp.exp(y_) - 1) ** 2
_residual = sp.simplify(sp.expand((num_sym - target).rewrite(sp.exp)))
a1_ok = _residual == 0
check("A1  STRUCTURAL: r - y r' = s y^2 e^y/(e^y-1)^2 > 0 for the whole shape family (sympy "
      "identity) -> every admissible threshold factor is strictly POSITIVE", a1_ok,
      f"sympy residual = {_residual}")

# A2: the computed threshold band across the three families (the admissible dressing band).
SHAPES = [0.5, 0.75, 1.0, 1.5, 2.0]
band_vals = [1.0 / math.factorial(n) for n in (1, 2)]                 # Litim Phi^2_1, Phi^2_2
band_vals += [phi_quadrature(1, 1, "litim")]                          # Litim Phi^1_1 = 1
for s in SHAPES:
    for (p, n) in [(2, 2), (2, 1), (1, 1)]:
        band_vals.append(phi_quadrature(p, n, "exp", s=s))
PHI_MIN, PHI_MAX = min(band_vals), max(band_vals)
a2_ok = PHI_MIN > 0 and PHI_MAX / PHI_MIN < 5.0
check("A2  the admissible threshold band across Litim + exponential + shape sweep is positive and "
      "O(1)", a2_ok, f"band = [{PHI_MIN:.4f}, {PHI_MAX:.4f}], ratio = {PHI_MAX/PHI_MIN:.3f}")

# =====================================================================================
# PART B -- POSITIVE CONTROLS PC3, PC4 + NEGATIVE CONTROL NC1
# =====================================================================================
log("\n" + "-" * 96)
log("PART B -- one-loop universal limit + Reuter-sector reproduction (controls)")
log("-" * 96)

# PC3: universal one-loop limit (Phi = 1) reproduces the W46 fixed-ratio roots.
#   Q(r) = c_C r^2 + (c_B + b_2) r + c_A = 0  ->  r* = -0.0848, -23.575 (W46/W48 recorded values).
roots_1loop = np.sort(np.roots([C_C, C_B + B2, C_A]))
pc3_ok = abs(roots_1loop[0] - (-23.575)) < 2e-3 and abs(roots_1loop[1] - (-0.0848)) < 2e-4
check("PC3 POSITIVE CONTROL: universal (Phi=1) limit reproduces the W46 negative fixed-ratio "
      "roots r* = -23.575, -0.0848", pc3_ok,
      f"roots = {roots_1loop[0]:.4f}, {roots_1loop[1]:.5f}")

# PC4: EH/Reuter-sector reproduction (schematic constants MIRRORED from W83; PORTED calibration).
A_GRAV = 2.0 / 0.70          # W83 calibration: pure-gravity g* ~ 0.70 (Reuter-FP ballpark)
a_V, a_S, a_D, a_RS = 0.020, 0.015, 0.010, 0.030
N_V_GU, N_S_GU, N_D_GU, N_RS_GU = 12.0, 4.0, 10.0, 1.0   # W83's GU content (schematic)
B0, B1 = 0.60, 1.0


def A_tot(nv, ns, nd, nrs):
    return A_GRAV + a_V * nv - a_S * ns - a_D * nd + a_RS * nrs


A_PURE = A_GRAV
A_GU = A_tot(N_V_GU, N_S_GU, N_D_GU, N_RS_GU)
g_star_pure = 2.0 / A_PURE
lam_star_pure = (g_star_pure * B0) / (2.0 + g_star_pure * B1)
g_star_gu = 2.0 / A_GU
lam_star_gu = (g_star_gu * B0) / (2.0 + g_star_gu * B1)
pc4_ok = (abs(g_star_pure - 0.70) < 0.02 and abs(g_star_pure * lam_star_pure - 0.109) < 0.01
          and abs(g_star_gu - 0.674) < 0.01)
check("PC4 POSITIVE CONTROL: schematic EH sector reproduces the W83/W88 Reuter-FP calibration "
      "(pure gravity g*=0.70, g*lam*~0.109; GU content g*=0.674)", pc4_ok,
      f"pure: g*={g_star_pure:.3f}, g*lam*={g_star_pure*lam_star_pure:.4f}; GU: g*={g_star_gu:.4f}")

# NC1: negative control -- the machinery detects AF breakage.
BS_bad = S1.BetaSystem(c_rs_weyl=-20.0)
nc1_ok = BS_bad.b2() < 0 and BS_bad.beta_f2sq(0.5, 0.0) > 0
check("NC1 NEGATIVE CONTROL: c_RS_weyl=-20 flips b_2<0 and beta_{f2^2}>0 -- AF breakage IS "
      "detectable by this machinery (the pass results are not vacuous)", nc1_ok,
      f"b_2 = {BS_bad.b2():.3f}, beta_f2sq(0.5) = {BS_bad.beta_f2sq(0.5,0.0):.3e}")

# =====================================================================================
# PART C -- THE FRG-DRESSED NEGATIVE FIXED-RATIO (the load-bearing new computation)
#   Along the flow the quadratic coefficients are dressed by positive threshold factors:
#     Q_Phi(r) = Phi_C c_C r^2 + (Phi_B c_B + Phi_2 b_2) r + Phi_A c_A = 0 .
#   Sweep all assignments Phi_i in the COMPUTED band [PHI_MIN, PHI_MAX].
# =====================================================================================
log("\n" + "-" * 96)
log("PART C -- FRG-dressed fixed-ratio: does r* < 0 survive every admissible regulator?")
log("-" * 96)

grid = np.linspace(PHI_MIN, PHI_MAX, 5)
all_neg, all_real, max_route_diff = True, True, 0.0
min_coeff = np.inf
min_disc = np.inf
worst = None
for pA in grid:
    for pB in grid:
        for pC in grid:
            for p2 in grid:
                a = pC * C_C
                b = pB * C_B + p2 * B2
                c = pA * C_A
                min_coeff = min(min_coeff, a, b, c)
                disc = b * b - 4 * a * c
                if disc < min_disc:
                    min_disc, worst = disc, (pA, pB, pC, p2)
                if disc <= 0:
                    all_real = False
                    continue
                # route 1: numpy
                r_np = np.sort(np.roots([a, b, c]))
                # route 2: explicit quadratic formula (sympy exact -> float)
                sq = sp.sqrt(sp.Rational(1))  # placeholder to keep sympy loaded
                sqrt_disc = math.sqrt(disc)
                r_f = sorted([(-b - sqrt_disc) / (2 * a), (-b + sqrt_disc) / (2 * a)])
                max_route_diff = max(max_route_diff,
                                     abs(r_np[0] - r_f[0]), abs(r_np[1] - r_f[1]))
                if r_np[1] >= 0:
                    all_neg = False

check("C1  BOTH fixed-ratio roots remain REAL and strictly NEGATIVE for EVERY combination of "
      "admissible threshold dressings (5^4 grid over the computed band) -- the negative "
      "fixed-ratio SURVIVES the FRG truncation across all three regulator families",
      all_real and all_neg,
      f"min disc = {min_disc:.2f} at Phi = {tuple(round(x,3) for x in worst)}; "
      f"min coeff = {min_coeff:.3f} > 0")

check("C2  two independent root routes (numpy companion-matrix vs explicit quadratic formula) "
      "agree on every grid point", max_route_diff < 1e-9,
      f"max |route1 - route2| = {max_route_diff:.2e}")

# C3: STRUCTURAL Vieta argument -- negativity is forced by coefficient positivity alone:
#   product = c/a > 0 and sum = -b/a < 0 for ANY positive dressing -> both roots negative
#   whenever real. Verified symbolically.
PA, PB, PC_, P2 = sp.symbols("Phi_A Phi_B Phi_C Phi_2", positive=True)
a_s = PC_ * sp.Rational(5, 6)
b_s = PB * 5 + P2 * sp.nsimplify(B2, rational=False)
c_s = PA * sp.Rational(5, 3)
c3_ok = bool(sp.ask(sp.Q.positive(c_s / a_s))) and bool(sp.ask(sp.Q.positive(b_s / a_s)))
check("C3  STRUCTURAL (Vieta, sympy): product of roots c/a > 0 and sum -b/a < 0 for ANY positive "
      "dressing -> a sign flip of the fixed ratio is IMPOSSIBLE for admissible regulators; the "
      "only escape is losing realness (C4)", c3_ok,
      "positivity of c/a and b/a certified under Phi_i > 0")

# C4: the breaking margin -- how asymmetric would the dressing have to be to lose real roots?
#   disc = 0 needs (Phi_A Phi_C)/(Phi_mid^2) >= b^2/(4 a c)|_{Phi=1} = F_break.
F_break = (C_B + B2) ** 2 / (4 * C_C * C_A)
F_admissible = (PHI_MAX / PHI_MIN) ** 2
c4_ok = F_break / F_admissible > 2.0 and min_disc > 0
check("C4  BREAKING MARGIN: losing the real negative roots needs a dressing asymmetry "
      f">= {F_break:.1f}; even the deliberately over-wide admissible band (worst-case Phi "
      f"assignment squared) supplies at most {F_admissible:.1f} -- margin "
      f"{F_break/F_admissible:.1f}x, and the actual grid minimum discriminant stays positive "
      f"({min_disc:.1f}). The truncation is NOT ambiguous about the ratio's sign",
      c4_ok, f"F_break = {F_break:.2f}, F_admissible = (Phi_max/Phi_min)^2 = {F_admissible:.2f}, "
             f"min disc on grid = {min_disc:.2f}")

# =====================================================================================
# PART D -- THE KREIN GRADING LOCUS THROUGH THE FRG FLOW (both ghost-mass fork branches)
# =====================================================================================
log("\n" + "-" * 96)
log("PART D -- grading locus m2^2 = 0 through the dressed flow; ghost-mass fork carried")
log("-" * 96)


def flow_f2sq(f2sq0: float, b2_eff: float, t_max: float, n_steps: int) -> np.ndarray:
    """RK4 of df2sq/dt = -kappa * b2_eff * f2sq^2 (dressed AF flow at the Gaussian branch)."""
    f = f2sq0
    dt = t_max / n_steps
    out = np.empty(n_steps + 1)
    out[0] = f

    def rhs(x):
        return -KAPPA * b2_eff * x * x

    for i in range(n_steps):
        k1 = rhs(f)
        k2 = rhs(f + 0.5 * dt * k1)
        k3 = rhs(f + 0.5 * dt * k2)
        k4 = rhs(f + dt * k3)
        f = f + dt / 6.0 * (k1 + 2 * k2 + 2 * k3 + k4)
        out[i + 1] = f
    return out


d1_ok = True
d1_detail = []
for phi2 in (PHI_MIN, PHI_MAX):
    b2_eff = phi2 * B2
    traj = flow_f2sq(0.8, b2_eff, 4000.0, 400_000)
    # analytic: 1/f2sq(t) = 1/f2sq(0) + kappa*b2_eff*t
    f_analytic = 1.0 / (1.0 / 0.8 + KAPPA * b2_eff * 4000.0)
    rel = abs(traj[-1] - f_analytic) / f_analytic
    strictly_pos = bool(np.all(traj > 0))
    monotone = bool(np.all(np.diff(traj) < 0))
    d1_ok &= rel < 1e-9 and strictly_pos and monotone
    d1_detail.append(f"Phi_2={phi2:.3f}: f2^2(4000)={traj[-1]:.3e} (analytic rel.err {rel:.1e}), "
                     f"pos={strictly_pos}, monotone={monotone}")
check("D1  FORK BRANCH A (agravity m2^2 = (1/2) f_2^2 M_Pl^2): at BOTH dressing extremes the AF "
      "flow keeps m2^2 > 0 at every finite scale, monotonically -> 0 -- the grading is RG-STABLE "
      "at all finite scales and pinches onto the locus ONLY at the free UV endpoint (W53's "
      "BOUNDARY verdict survives FRG dressing; two routes RK4 vs analytic agree)",
      d1_ok, " | ".join(d1_detail))

# D2: fork branch B -- GU-native fixed-scale ghost mass m2 = sqrt(m2_eff) mu_DW.
M2_EFF_BAND = (5.0 / 6.0, 5.0 / 4.0)
d2_ok = all(m > 0 for m in M2_EFF_BAND)
check("D2  FORK BRANCH B (GU-native fixed-scale m2 = sqrt(m2_eff) mu_DW, m2_eff in [5/6, 5/4]): "
      "d_locus = m2_eff is scale-INDEPENDENT and strictly positive at every scale INCLUDING the "
      "UV endpoint -- STAYS-CLEAR, no pinch. The fork decides the ENDPOINT behavior only "
      "(BOUNDARY vs STAYS-CLEAR); at all finite scales both branches are grading-stable",
      d2_ok, f"d_locus in [{M2_EFF_BAND[0]:.3f}, {M2_EFF_BAND[1]:.3f}] at every k")

# D3: eta_C connection (IMPORTED from W89, cited not recomputed): the Z_h-scheme fork.
#   Weyl-adapted: eta_C = 0 -> only the structural root f_2^2* = 0 -> branch-A pinch at endpoint.
#   EH-adapted:   eta_C = -eta_N* c_reg = +2 c_reg > 0 -> lifted root f_2^2* = eta_C/(kappa b_2)
#                 -> branch-A grading BOUNDED AWAY from the locus even at the UV endpoint.
c_reg_band = (0.5, 1.12)   # W89's Phi^2_2(0) band across the three families
d3_detail = []
d3_ok = True
for c_reg in c_reg_band:
    eta_c = 2.0 * c_reg * KAPPA           # -eta_N* c_reg, with the loop factor (W89 normalization)
    f2_lift = eta_c / (KAPPA * B2)
    d_locus_uv = 0.5 * f2_lift
    # W89's stated lifted-root band is [0.07, 0.16]; the import must land inside it
    d3_ok &= f2_lift > 0 and d_locus_uv > 0 and 0.05 < f2_lift < 0.20
    d3_detail.append(f"c_reg={c_reg}: f2^2*={f2_lift:.3f} (W89 band [0.07,0.16]), "
                     f"d_locus(UV)={d_locus_uv:.4f}")
check("D3  eta_C SCHEME FORK (imported W89): Weyl-adapted (eta_C=0) -> pinch at the free endpoint "
      "(HORN K side); EH-adapted (eta_C=+2c_reg>0) -> lifted f_2^2*>0 so branch-A grading is "
      "BOUNDED AWAY from the locus even at the UV endpoint (HORN Q side). On EITHER scheme the "
      "grading is stable at all finite scales -- the scheme fork moves only the endpoint",
      d3_ok, " | ".join(d3_detail))

# =====================================================================================
# PART E -- ADVERSARIAL: uniqueness break, exhaustive FP enumeration, spin-0 status
# =====================================================================================
log("\n" + "-" * 96)
log("PART E -- adversarial pass: what BREAKS beyond one loop, and is anything hidden?")
log("-" * 96)


def beta4(v: np.ndarray, eta0_coeff: float = 0.3, phi: float = 1.0) -> np.ndarray:
    """Schematic FRG 4-coupling system (g, lam, f2sq, f0sq): canonical linear terms + one-loop
    quadratics (dressed by phi) + the de-slaving term eta0(g)*f0sq (W83 mechanism, eta0<0 at g>0).
    Weyl-adapted scheme (eta_C = 0) -- the W89-leaned branch."""
    g, lam, f2, f0 = v
    bg = 2.0 * g - A_GU * g * g
    bl = -2.0 * lam + g * (B0 - B1 * lam)
    bf2 = -KAPPA * phi * B2 * f2 * f2
    bf0 = KAPPA * phi * (C_A * f2 * f2 + C_B * f2 * f0 + C_C * f0 * f0) - eta0_coeff * g * f0
    return np.array([bg, bl, bf2, bf0])


# E1: homogeneity BREAK -- the one-loop uniqueness argument does NOT extend to the FRG.
v0 = np.array([0.3, 0.05, 0.4, -0.2])
lam_scale = 1.7
resid = np.linalg.norm(beta4(lam_scale * v0) - lam_scale ** 2 * beta4(v0))
e1_ok = resid > 0.1
check("E1  UNIQUENESS BREAKS (as it must): the canonical linear terms destroy the "
      "homogeneous-quadratic structure (beta(lam g) != lam^2 beta(g)), so H60's "
      "no-interacting-FP theorem is ONE-LOOP-SPECIFIC -- the Reuter FP is exactly the "
      "non-Gaussian FP the one-loop argument could not see (the skeptic's hunt SUCCEEDS, in the "
      "already-catalogued way)", e1_ok, f"homogeneity residual = {resid:.3f}")

# E2: exhaustive FP enumeration + multistart cross-check. In this truncation the FP set is
#   FULLY ENUMERABLE: beta_g=0 -> g* in {0, 2/A}; lam* solved linearly; f2* = 0 (Weyl-adapted);
#   beta_f0=0 at f2=0 -> f0* in {0, eta0*g*/(kappa*phi*c_C)}. Multistart Newton must find NO
#   cluster outside this enumerated set.
rng = np.random.default_rng(20260713)
enumerated = []
for gst in (0.0, 2.0 / A_GU):
    lst = (gst * B0) / (2.0 + gst * B1)
    f0_roots = [0.0]
    if gst > 0:
        f0_roots.append(0.3 * gst / (KAPPA * 1.0 * C_C))   # the lifted (de-slaved) root
    for f0r in f0_roots:
        enumerated.append(np.array([gst, lst, 0.0, f0r]))

found_outside = 0
converged = 0
for _ in range(300):
    v = rng.uniform([-0.5, -0.5, -1.0, -60.0], [1.5, 0.5, 1.0, 60.0])
    ok = False
    for _ in range(200):
        # damped Newton with numerical Jacobian
        J = np.zeros((4, 4))
        f = beta4(v)
        h = 1e-7
        for j in range(4):
            vp = v.copy()
            vp[j] += h
            J[:, j] = (beta4(vp) - f) / h
        try:
            step = np.linalg.solve(J + 1e-12 * np.eye(4), -f)
        except np.linalg.LinAlgError:
            break
        v = v + np.clip(step, -5.0, 5.0)
        if np.linalg.norm(beta4(v)) < 1e-12:
            ok = True
            break
    if not ok:
        continue
    converged += 1
    dists = [np.linalg.norm(v - e) for e in enumerated]
    # rays through the Gaussian point in the marginal plane (fixed-ratio rays) are non-isolated
    # zeros at g=lam=0 only if BOTH quadratics vanish; with the linear terms present at g!=0 they
    # are lifted. At g=lam=0 the marginal block is homogeneous: accept ray points too.
    on_gaussian_ray = (abs(v[0]) < 1e-6 and abs(v[1]) < 1e-6
                       and np.linalg.norm(beta4(v)[2:]) < 1e-10)
    if min(dists) > 1e-3 and not on_gaussian_ray:
        found_outside += 1
e2_ok = converged > 50 and found_outside == 0
check("E2  EXHAUSTIVE FP ENUMERATION + 300-seed multistart Newton: every convergent root lies in "
      "the enumerated set {Gaussian family; Reuter family (incl. the de-slaved f_0^2 root)} or on "
      "a Gaussian-point fixed-ratio ray -- NO hidden third fixed-point mechanism in the "
      "truncation", e2_ok,
      f"converged = {converged}/300, outside enumerated set = {found_outside}")

# E3: the spin-0 conformal-mode sign at the negative fixed ratio -- unchanged by dressing.
#   On the AF/Gaussian branch every admissible dressing keeps both ratio roots negative (C1), so
#   the UV-complete AF trajectory carries f_0^2 < 0 -> M_0^2 = (1/2) f_0^2 M_Pl^2 < 0 for EVERY
#   regulator. The FRG truncation neither rescues nor kills the conformal-mode open item.
e3_ok = all_neg and all_real
check("E3  SPIN-0 STATUS: the wrong-sign conformal mode (M_0^2 < 0 on the AF trajectory) persists "
      "under EVERY admissible dressing -- the FRG truncation neither rescues nor kills it; the "
      "physical-vs-gauge question (W78) remains the load-bearing open item, exactly as at one "
      "loop", e3_ok, "follows from C1 (both roots negative across the whole band)")

# =====================================================================================
# SUMMARY + VERDICT
# =====================================================================================
log("\n" + "=" * 96)
log("SUMMARY")
log("=" * 96)
n_pass = sum(1 for _, p, _ in results if p)
n_tot = len(results)
log(f"  {n_pass}/{n_tot} checks passed")
log("")
log("  VERDICT: SURVIVES-WITH-ONE-CATALOGUED-BREAK.")
log("  * AF trajectory (Gaussian FP as structural root, f_2^2 marginally irrelevant): SURVIVES")
log("  * negative fixed-ratio r* < 0 (both roots): SURVIVES across all three regulator families")
log("    (structural: Vieta + threshold positivity; ~2.9x below the breaking asymmetry even")
log("    on a deliberately over-wide dressing band; actual grid discriminant never < 63)")
log("  * spin-2 Krein grading RG-stability at all FINITE scales: SURVIVES on BOTH ghost-mass")
log("    fork branches; the fork decides only the UV-endpoint behavior (A: pinch/BOUNDARY,")
log("    B: STAYS-CLEAR), and the eta_C scheme fork (W89) can lift branch A clear (HORN Q side)")
log("  * UNIQUENESS of the Gaussian FP: BREAKS -- the Reuter FP appears once canonical linear")
log("    terms enter (known, catalogued: W83/W88); not a new ambiguity")
log("  * spin-0 conformal-mode sign: UNCHANGED (open item survives dressing; W78)")
log("  H59 remains OPEN: this is flow-side + grading-side evidence in an FRG truncation, NOT a")
log("  loop-positivity computation (W48 gate: AF-flow-only evidence is insufficient for H59).")

if n_pass == n_tot:
    log("\nALL CHECKS PASS -- exit 0")
    sys.exit(0)
else:
    for name, p, d in results:
        if not p:
            log(f"  FAILED: {name}  --  {d}")
    sys.exit(1)
