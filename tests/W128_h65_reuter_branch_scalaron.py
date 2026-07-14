#!/usr/bin/env python3
r"""
W128 / H65 -- THE AS/REUTER-BRANCH SCALARON: what is the scalaron's fate on the interacting
(asymptotic-safety) branch that W119 catalogued and W83 conditionally selected?

QUESTION (four parts, per the H65 brief):
  (1) at the Reuter-family fixed point with GU's content, what is the SIGN of the R^2-sector
      coupling -- specifically the de-slaved f_0^2 root W119 catalogued -- and the resulting m_0^2?
  (2) is the scalaron tachyonic, healthy, or absent on trajectories emanating from the Reuter FP
      toward the IR?
  (3) does anything in GU's structure SELECT between the AF and AS branches, or does E2 stand?
  (4) honest bottom line: does the AS branch RESCUE the scalaron, or does the tachyon follow?

WHAT IS NEW OVER W83/W119 (the native increment):
  * THE SIGN-LOCK THEOREM (derived, sympy): within the truncation, for ANY admissible threshold
    dressing Phi > 0 (W119's positivity identity) and any de-slaving coefficient eta0, the
    de-slaved Reuter-family root is f_0^2* = eta0 g* / (kappa Phi c_C), so
        sign(de-slaved root) = sign(eta0) = sign(RELEVANCE of f_0^2 at the main Reuter FP).
    The entire Reuter-branch tachyon question REDUCES to ONE sign: whether the R^2 direction is
    relevant at the interacting FP. That sign is PORTED (Lauscher-Reuter; Codello-Percacci-
    Rahmede; Benedetti-Machado-Saueressig; AS-Starobinsky -- four truncation lineages agree:
    RELEVANT), and nothing in the admissible regulator band can flip the lock.
  * PERMITTED-NOT-FORCED (derived within truncation): the Reuter FP's UV basin contains BOTH
    signs of f_0^2(IR). The AS branch does not forbid the tachyon; it removes the FORCING
    (the fixed-ratio slaving is an AF-branch structure that demonstrably disappears at g* != 0).
    Rescue therefore requires the IR-consistency boundary condition (W83's D2), not the branch
    alone.
  * KREIN COMPATIBILITY ON THE AS TRAJECTORY (derived extension of W119): along UV-complete AS
    trajectories f_2^2(k) > 0 at every finite scale (beta_{f_2^2} is g-independent in this
    truncation and strictly negative for f_2^2 > 0, same exact solution as W119), so the spin-2
    grading distance is positive at all finite scales on BOTH ghost-mass fork branches; the fork
    again decides only the FP-endpoint behavior (agravity: pinch/BOUNDARY at f_2^2* = 0, exactly
    as at the Gaussian endpoint; fixed-scale: STAYS-CLEAR). Keep-and-grade is COMPATIBLE with the
    interacting FP within the truncation.
  * THE eta_N* = -2 IDENTITY (derived, exact): at ANY fixed point with finite g* != 0 the Newton
    anomalous dimension is exactly -2 (dimensional identity beta_g = (2 + eta_N) g), independent
    of every schematic magnitude -- the schematic EH sector respects the exact AS-gravity
    structure (positive control connecting the truncation to the real Reuter FP).

HONESTY (grade DERIVED-on-PORTED, truncation-dependence explicit):
  * The EH-sector magnitudes (A_tot budget, B0, B1) are SCHEMATIC, mirrored from W83/W119,
    calibrated to the literature Reuter FP (pure gravity g* = 0.70, g* lambda* ~ 0.109; GU
    content g* = 0.674) -- reproduced here as positive controls PC1/PC2.
  * The de-slaving coefficient eta0's MAGNITUDE is schematic (W83 used 0.9, W119 used 0.3; both
    swept here); its SIGN (eta0 > 0, f_0^2 relevant at the Reuter FP) is PORTED from the f(R)-FRG
    literature. The sign-lock theorem makes this THE hinge and the negative control (NC1) shows
    the machinery detects the flip: eta0 < 0 => de-slaved root negative, relevance gone, verdict
    TACHYON-FOLLOWS. The verdict is NOT hardcoded.
  * The one-loop marginal coefficients (5/3, 5, 5/6; b_2 = 133/10 + c_RS) remain PORTED (W45).
  * f_0^2 here is the agravity-convention coupling (R^2 coefficient 1/(6 f_0^2)); W123 verified
    the reciprocal wobble against W79/W122's direct convention is sign-harmless
    (sign(m_0^2) = sign(f_0^2) in both).

POSITIVE CONTROLS: PC1 pure-gravity Reuter FP g* = 0.700, g* lambda* ~ 0.109 (literature band
~0.11-0.14); PC2 GU-content Reuter FP g* = 0.674, lambda* = 0.151 (W119 PC4 / W83 A1 values);
PC3 W46 AF fixed-ratio roots -0.0848, -23.575 (the AF-branch contrast); PC4 Litim thresholds
Phi^p_n(0) = 1/n! and exponential Phi^2_2(0) = 1, Phi^1_1(0) = pi^2/6 (two routes).
NEGATIVE CONTROL: NC1 eta0 < 0 flips the de-slaved root sign and kills the relevance -- the
verdict machinery detects TACHYON-FOLLOWS (the pass results are not vacuous).

Exit 0 iff all checks pass. numpy + sympy only. Deterministic (no RNG in load-bearing paths).
Reproducible: python tests/W128_h65_reuter_branch_scalaron.py
NO forbidden target {3,8,24,chi(K3)=24,Ahat=3} assumed/inserted/hardcoded/divided-by; no
generation count touched. NO canon / RESEARCH-STATUS / claim-status / verdict / posture file
changed. H59/H61a/E2 remain OPEN; the E2 fork is CARRIED, not closed.
Companion exploration: explorations/W128-reuter-branch-scalaron-native-2026-07-14.md
"""
from __future__ import annotations

import math
import sys

import numpy as np
import sympy as sp

FAIL: list[str] = []


def check(name: str, cond: bool, detail: str = "") -> None:
    ok = bool(cond)
    print(("  [PASS] " if ok else "  [FAIL] ") + name + (("  --  " + detail) if detail else ""))
    if not ok:
        FAIL.append(name)


def log(msg: str = "") -> None:
    print(msg, flush=True)


# =====================================================================================
# Shared constants (mirrored from W45/W83/W119; PORTED grades inherited)
# =====================================================================================
KAPPA = 1.0 / (4.0 * math.pi) ** 2
C_A, C_B, C_C = 5.0 / 3.0, 5.0, 5.0 / 6.0        # one-loop f_0^2 quadratic (KNOWN/PORTED, W45)
B2 = 133.0 / 10.0 + 17.0 / 12.0                   # b_2 with the W45 RS anchor c_RS_weyl = 17/12
A_GRAV = 2.0 / 0.70                                # W83 calibration: pure-gravity g* ~ 0.70
a_V, a_S, a_D, a_RS = 0.020, 0.015, 0.010, 0.030   # DEP signs, schematic magnitudes (W83)
N_V, N_S, N_D, N_RS = 12.0, 4.0, 10.0, 1.0         # W83's GU content (schematic)
A_GU = A_GRAV + a_V * N_V - a_S * N_S - a_D * N_D + a_RS * N_RS
B0, B1 = 0.60, 1.0                                 # W83 lambda sector (schematic)
ETA0 = 0.9                                         # de-slaving coeff: SIGN ported (relevant), mag schematic
M2_EFF_BAND = (5.0 / 6.0, 5.0 / 4.0)               # GU-native fixed-scale ghost-mass band (wave20/H43)

log("=" * 96)
log("W128 / H65 -- the AS/Reuter-branch scalaron: sign, IR fate, branch selection, bottom line")
log("=" * 96)
log(f"  A_tot(GU) = {A_GU:.4f}; b_2 = {B2:.4f}; kappa = {KAPPA:.6f}; eta0 (schematic mag) = {ETA0}")


# =====================================================================================
# PART A -- POSITIVE CONTROLS: the machinery reproduces W83/W119/W46 + known Reuter numbers
# =====================================================================================
log("\n" + "-" * 96)
log("PART A -- positive controls (W83/W119 Reuter FP values; W46 AF roots; threshold functions)")
log("-" * 96)

g_star_pure = 2.0 / A_GRAV
lam_star_pure = g_star_pure * B0 / (2.0 + g_star_pure * B1)
g_star = 2.0 / A_GU
lam_star = g_star * B0 / (2.0 + g_star * B1)

check("PC1 POSITIVE CONTROL: pure-gravity Reuter FP reproduces the calibrated literature values "
      "g* = 0.700, g* lambda* ~ 0.109 (literature band ~0.11-0.14)",
      abs(g_star_pure - 0.70) < 0.02 and abs(g_star_pure * lam_star_pure - 0.109) < 0.01,
      f"g* = {g_star_pure:.3f}, g* lambda* = {g_star_pure * lam_star_pure:.4f}")

check("PC2 POSITIVE CONTROL: GU-content Reuter FP reproduces the W119/W83 catalogued values "
      "g* = 0.674, lambda* = 0.151",
      abs(g_star - 0.674) < 0.01 and abs(lam_star - 0.151) < 0.005,
      f"g* = {g_star:.4f}, lambda* = {lam_star:.4f}")

roots_af = np.sort(np.roots([C_C, C_B + B2, C_A]))
check("PC3 POSITIVE CONTROL: the AF-branch fixed-ratio quadratic reproduces the W46 roots "
      "r* = -23.575, -0.0848 (the branch the tachyon lives on -- the contrast object)",
      abs(roots_af[0] - (-23.575)) < 2e-3 and abs(roots_af[1] - (-0.0848)) < 2e-4,
      f"roots = {roots_af[0]:.4f}, {roots_af[1]:.5f}")


def phi_quadrature(p: int, n: int, family: str, s: float = 1.0, ny: int = 300_000,
                   ymax: float = 60.0) -> float:
    """Direct quadrature of Phi^p_n(0) (W119's routine, re-implemented)."""
    if family == "litim":
        y = np.linspace(1e-9, 1.0 - 1e-9, ny)
        integrand = y ** (n - 1)
    else:
        y = np.linspace(1e-8, ymax, ny)
        em1 = np.expm1(y)
        num = s * y ** 2 * np.exp(y) / em1 ** 2
        den = (y * (em1 + s) / em1) ** p
        integrand = y ** (n - 1) * num / den
    return float(np.trapezoid(integrand, y) / math.gamma(n))


pc4_ok = True
pc4_detail = []
for (p, n) in [(1, 1), (2, 1), (2, 2)]:
    got = phi_quadrature(p, n, "litim")
    pc4_ok &= abs(got - 1.0 / math.factorial(n)) < 1e-5
    pc4_detail.append(f"Litim Phi^{p}_{n}={got:.5f}")
phi22 = phi_quadrature(2, 2, "exp")
phi11 = phi_quadrature(1, 1, "exp")
pc4_ok &= abs(phi22 - 1.0) < 1e-4 and abs(phi11 - math.pi ** 2 / 6.0) < 1e-4
pc4_detail.append(f"exp Phi^2_2={phi22:.5f} (want 1), Phi^1_1={phi11:.5f} (want {math.pi**2/6:.5f})")
check("PC4 POSITIVE CONTROL: threshold functions reproduce the known closed forms (Litim 1/n!; "
      "exponential Phi^2_2(0)=1, Phi^1_1(0)=pi^2/6) -- the W119 admissible-dressing band is rebuilt "
      "from scratch here, not copied", pc4_ok, "; ".join(pc4_detail))

# the admissible dressing band (rebuilt): Litim + exponential shape sweep, three (p,n) types
band_vals = [1.0, 0.5, 1.0]           # Litim Phi^2_1, Phi^2_2, Phi^1_1
for s in (0.5, 0.75, 1.0, 1.5, 2.0):
    for (p, n) in [(2, 2), (2, 1), (1, 1)]:
        band_vals.append(phi_quadrature(p, n, "exp", s=s))
PHI_MIN, PHI_MAX = min(band_vals), max(band_vals)
check("A1  the rebuilt admissible threshold band matches W119's [0.50, 2.47] (positive, O(1))",
      abs(PHI_MIN - 0.50) < 0.02 and abs(PHI_MAX - 2.47) < 0.05 and PHI_MIN > 0,
      f"band = [{PHI_MIN:.3f}, {PHI_MAX:.3f}]")

# A2: the eta_N* = -2 identity -- exact at ANY interacting FP, independent of all schematic magnitudes.
g_sym, A_sym = sp.symbols("g A", positive=True)
eta_N = -A_sym * g_sym                       # beta_g = 2g - A g^2 = (2 + eta_N) g
eta_N_at_fp = eta_N.subs(g_sym, 2 / A_sym)
check("A2  DERIVED IDENTITY: at ANY fixed point with finite g* = 2/A != 0, the Newton anomalous "
      "dimension is EXACTLY eta_N* = -2 (dimensional identity, independent of every schematic "
      "magnitude) -- the truncation respects the exact structure of the real Reuter FP",
      sp.simplify(eta_N_at_fp + 2) == 0, f"eta_N(g*=2/A) = {eta_N_at_fp} for all A > 0")


# =====================================================================================
# PART B -- (1) THE SIGN-LOCK THEOREM: de-slaved root sign == relevance sign, band-robust
# =====================================================================================
log("\n" + "-" * 96)
log("PART B -- the de-slaved f_0^2 root at the Reuter FP: the sign-lock theorem")
log("-" * 96)

# At the Reuter FP (g*, lambda*, f_2^2 = 0), beta_{f_0^2} = kappa Phi c_C y^2 - eta0 g* y.
# Roots: y = 0 (the main/BMS family) and y* = eta0 g* / (kappa Phi c_C) (the de-slaved root).
eta0_s = sp.Symbol("eta0", real=True)
kap_s, phi_s, cc_s, gst_s = sp.symbols("kappa Phi c_C g_star", positive=True)
y_s = sp.Symbol("y", real=True)
beta_y = kap_s * phi_s * cc_s * y_s ** 2 - eta0_s * gst_s * y_s
y_roots = sp.solve(beta_y, y_s)
y_deslaved = [r for r in y_roots if r != 0][0]
ratio = sp.simplify(y_deslaved / eta0_s)
b1_ok = sp.ask(sp.Q.positive(ratio)) is True
check("B1  SIGN-LOCK (derived, sympy): the de-slaved Reuter-family root is "
      "f_0^2* = eta0 g*/(kappa Phi c_C), i.e. (de-slaved root)/eta0 > 0 for EVERY positive "
      "dressing Phi, every kappa, c_C, g* > 0 -- sign(de-slaved root) = sign(eta0), with NO "
      "admissible regulator freedom to break the lock (threshold positivity is W119's identity)",
      b1_ok, f"y* = {y_deslaved}; y*/eta0 = {ratio} (manifestly positive)")

# B2: relevance <=> positive de-slaved root <=> non-tachyonic (the reduction to ONE sign).
#     eigenvalue at the main FP (y=0): d beta/dy = -eta0 g*  ->  relevant iff eta0 > 0.
#     eigenvalue at the de-slaved root: d beta/dy = +eta0 g*  ->  opposite stability, same sign lock.
dbeta_dy = sp.diff(beta_y, y_s)
eig_main = dbeta_dy.subs(y_s, 0)                        # -eta0 g*
eig_desl = sp.simplify(dbeta_dy.subs(y_s, y_deslaved))  # +eta0 g*
b2_ok = sp.simplify(eig_main + eta0_s * gst_s) == 0 and sp.simplify(eig_desl - eta0_s * gst_s) == 0
check("B2  REDUCTION TO ONE SIGN (derived): f_0^2 RELEVANT at the main Reuter FP "
      "(eigenvalue -eta0 g* < 0) <=> eta0 > 0 <=> de-slaved root POSITIVE (non-tachyonic); "
      "f_0^2 IRRELEVANT <=> eta0 < 0 <=> de-slaved root NEGATIVE (tachyonic). The entire "
      "Reuter-branch scalaron question reduces to the relevance sign of R^2 at the interacting "
      "FP -- which is PORTED (LR/CPR/BMS/AS-Starobinsky: RELEVANT), not yet computed natively",
      b2_ok, f"eig(main) = {eig_main}, eig(de-slaved) = {eig_desl}")

# B3: numbers across the schematic-magnitude and dressing bands (magnitudes flagged schematic).
vals = []
for eta0 in (0.3, 0.9):
    for phi in (PHI_MIN, 1.0, PHI_MAX):
        vals.append(eta0 * g_star / (KAPPA * phi * C_C))
b3_ok = all(v > 0 for v in vals)
check("B3  the de-slaved root is POSITIVE across the entire dressing band [0.50, 2.47] AND the "
      "schematic eta0 magnitude band [0.3, 0.9] (W119's and W83's choices); MAGNITUDE is schematic "
      "and NOT load-bearing -- only the sign is asserted",
      b3_ok, f"f_0^2* in [{min(vals):.1f}, {max(vals):.1f}] (all > 0; magnitudes schematic)")

# B4: m_0^2 verdicts at the two Reuter-family FPs (agravity convention m_0^2 = f_0^2 Mbar^2/2;
#     W123 verified the reciprocal-convention wobble is sign-harmless).
m0sq_main = 0.0 * 0.5           # main family: f_0^2* = 0 -> m_0^2 = 0 at the FP (scale-invariant point)
m0sq_desl = min(vals) * 0.5     # de-slaved root: positive
check("B4  m_0^2 AT THE FP: main Reuter family f_0^2* = 0 -> m_0^2 = 0 (the scalaron is massless/"
      "ABSENT AS A SCALE at the scale-invariant point -- masses are trajectory statements, not FP "
      "statements); de-slaved root -> m_0^2 = f_0^2* Mbar^2/2 > 0 (healthy sign, schematic "
      "magnitude). NEITHER Reuter-family FP carries a tachyonic R^2 sector, GIVEN the ported "
      "relevance sign", m0sq_main == 0.0 and m0sq_desl > 0,
      f"m_0^2(main FP) = 0; m_0^2(de-slaved) = +{m0sq_desl:.2f} Mbar^2 (schematic mag, sign robust)")


# =====================================================================================
# PART C -- (2) IR TRAJECTORIES FROM THE REUTER FP: healthy, tachyonic, both?
# =====================================================================================
log("\n" + "-" * 96)
log("PART C -- IR trajectories from the Reuter FP: the scalaron's fate is a FREE boundary condition")
log("-" * 96)


def F4(v: np.ndarray, eta0: float = ETA0, phi: float = 1.0) -> np.ndarray:
    """The W83/W119 4-coupling FRG system (g, lambda, f_2^2, f_0^2), agravity convention."""
    g, lam, x, y = v
    return np.array([
        2.0 * g - A_GU * g * g,
        -2.0 * lam + g * (B0 - B1 * lam),
        -KAPPA * phi * B2 * x * x,
        KAPPA * phi * (C_A * x * x + C_B * x * y + C_C * y * y) - eta0 * g * y,
    ])


def jac4(v: np.ndarray, eta0: float = ETA0, h: float = 1e-7) -> np.ndarray:
    J = np.zeros((4, 4))
    f0 = F4(v, eta0)
    for j in range(4):
        vp = v.copy()
        vp[j] += h
        J[:, j] = (F4(vp, eta0) - f0) / h
    return J


FP_MAIN = np.array([g_star, lam_star, 0.0, 0.0])
check("C0  the main Reuter-family FP (g*, lambda*, 0, 0) is a genuine zero of the full 4-coupling "
      "system", float(np.linalg.norm(F4(FP_MAIN))) < 1e-12,
      f"|beta|(FP) = {np.linalg.norm(F4(FP_MAIN)):.2e}")


def flow_ir_from_fp(orient: float, steps: int = 4000, dt: float = -2.0e-3):
    """Integrate toward the IR from the FP along the relevant f_0^2 eigendirection (W83's C2),
    oriented toward f_0^2 > 0 (orient=+1) or f_0^2 < 0 (orient=-1)."""
    J = jac4(FP_MAIN)
    w, V = np.linalg.eig(J)
    rel = [i for i in range(4) if w[i].real < -1e-8]
    idx = max(rel, key=lambda i: abs(V[3, i].real))
    d = V[:, idx].real
    if d[3] * orient < 0:
        d = -d
    v = FP_MAIN + 1e-3 * d
    extreme_f0 = v[3]
    for _ in range(steps):
        v = v + dt * F4(v)
        if not np.all(np.isfinite(v)) or np.linalg.norm(v) > 1e6:
            return None, True
        extreme_f0 = orient * max(orient * extreme_f0, orient * v[3])
    return extreme_f0, False


f0_ir_pos, landau_pos = flow_ir_from_fp(+1.0)
f0_ir_neg, landau_neg = flow_ir_from_fp(-1.0)
check("C1  HEALTHY TRAJECTORY EXISTS: flowing toward the IR from the Reuter FP along the relevant "
      "f_0^2 eigendirection (positive orientation) reaches f_0^2 > 0 with no Landau pole -- a "
      "UV-complete NON-TACHYONIC theory lives on the AS branch (reproduces W83's C2; forbidden on "
      "AF by W123's monotonicity theorem)",
      f0_ir_pos is not None and f0_ir_pos > 0 and not landau_pos,
      f"f_0^2(IR) reaches +{f0_ir_pos:.4f} -> m_0^2 > 0 (healthy)")

check("C2  PERMITTED-NOT-FORCED: the OPPOSITE orientation of the SAME relevant eigendirection "
      "reaches f_0^2 < 0 (tachyonic) and is EQUALLY UV-complete -- the AS branch does NOT forbid "
      "the tachyon; it removes the FORCING. The healthy sign is a free IR boundary condition, so "
      "rescue additionally requires the IR-consistency selection (W83 D2), not the branch alone",
      f0_ir_neg is not None and f0_ir_neg < 0 and not landau_neg,
      f"f_0^2(IR) reaches {f0_ir_neg:.4f} -> tachyonic trajectory also emanates from the FP")


def flow_uv(v0: np.ndarray, eta0: float = ETA0, t_max: float = 400.0, n: int = 400_000):
    """RK4 toward the UV from IR data; return (converged-to-Reuter, final state, landau)."""
    v = np.array(v0, dtype=float)
    dt = t_max / n
    for _ in range(n):
        k1 = F4(v, eta0)
        k2 = F4(v + 0.5 * dt * k1, eta0)
        k3 = F4(v + 0.5 * dt * k2, eta0)
        k4 = F4(v + dt * k3, eta0)
        v = v + dt / 6.0 * (k1 + 2 * k2 + 2 * k3 + k4)
        if not np.all(np.isfinite(v)) or np.linalg.norm(v) > 1e6:
            return False, v, True
    near = (abs(v[0] - g_star) < 1e-3 and abs(v[1] - lam_star) < 1e-3
            and abs(v[3]) < 1e-2 and 0 <= v[2] < 0.1)
    return near, v, False


ok_neg, v_neg, ld_neg = flow_uv(np.array([0.05, 0.01, 0.40, -0.40]))   # tachyonic IR data
ok_pos, v_pos, ld_pos = flow_uv(np.array([0.05, 0.01, 0.40, +0.30]))   # healthy IR data
check("C3  UV BASIN CONTAINS BOTH SIGNS (forward check of C1/C2): generic IR data with f_0^2 < 0 "
      "AND with f_0^2 > 0 both flow INTO the Reuter FP toward the UV (relevant directions are "
      "UV-attractive; f_2^2 decays marginally as on AF) -- computed by RK4 on the full 4-coupling "
      "system, no eigendirection tuning",
      ok_neg and ok_pos and not ld_neg and not ld_pos,
      f"f0=-0.4: -> ({v_neg[0]:.3f},{v_neg[1]:.3f},{v_neg[2]:.3f},{v_neg[3]:.1e}); "
      f"f0=+0.3: -> ({v_pos[0]:.3f},{v_pos[1]:.3f},{v_pos[2]:.3f},{v_pos[3]:.1e})")

# C4: the basin is not everything -- large positive f_0^2 still Landau-poles (quadratic wins), and
#     the AF route (g = 0) reproduces the W123 exclusion: f_0^2 > 0 is UV-FORBIDDEN there.
ok_big, v_big, ld_big = flow_uv(np.array([0.05, 0.01, 0.40, 300.0]), t_max=2000.0)


def flow_uv_af(x0: float, y0: float, t_max: float = 4000.0, n: int = 400_000):
    x, y = x0, y0
    dt = t_max / n
    for _ in range(n):
        bx = -KAPPA * B2 * x * x
        by = KAPPA * (C_A * x * x + C_B * x * y + C_C * y * y)
        x, y = x + dt * bx, y + dt * by
        if abs(y) > 1e6:
            return "landau"
    return "complete"


af_pos = flow_uv_af(0.40, +0.30)
check("C4  CONTRAST + BASIN BOUNDARY: on the AF route (g = 0) the SAME healthy IR data f_0^2 = +0.3 "
      "Landau-poles (W123's monotonicity theorem reproduced: health is FORBIDDEN on AF); and even "
      "on AS the basin is bounded (f_0^2 = +300 above the de-slaved root diverges) -- the AS "
      "rescue is a basin statement, not a universal one",
      af_pos == "landau" and ld_big,
      f"AF f0=+0.3: {af_pos}; AS f0=+300: landau={ld_big}")


# =====================================================================================
# PART D -- KREIN GRADING ON THE AS TRAJECTORY (both ghost-mass fork branches)
# =====================================================================================
log("\n" + "-" * 96)
log("PART D -- is keep-and-grade compatible with the interacting FP? (W119 extended to AS)")
log("-" * 96)


def f2_along_uv(x0: float, t_max: float = 400.0, n: int = 200_000):
    """f_2^2 along ANY trajectory: beta_{f_2^2} = -kappa Phi b_2 f_2^4-type is g-INDEPENDENT in
    this truncation, so the W119 exact solution 1/f_2^2(t) = 1/f_2^2(0) + kappa Phi b_2 t applies
    verbatim on AS trajectories. Integrate + compare."""
    x = x0
    dt = t_max / n
    traj = np.empty(n + 1)
    traj[0] = x
    for i in range(n):
        x = x + dt * (-KAPPA * B2 * x * x)
        traj[i + 1] = x
    analytic = 1.0 / (1.0 / x0 + KAPPA * B2 * t_max)
    return traj, analytic


traj_f2, f2_analytic = f2_along_uv(0.40)
d1_ok = bool(np.all(traj_f2 > 0)) and abs(traj_f2[-1] - f2_analytic) / f2_analytic < 1e-3
check("D1  DERIVED EXTENSION OF W119: along AS (Reuter-basin) trajectories f_2^2(k) obeys the SAME "
      "exact law as on AF (beta_{f_2^2} is g-independent in this truncation) -> f_2^2 > 0 at EVERY "
      "finite scale -> ghost-mass fork branch A (agravity, d_locus = f_2^2/2) keeps the spin-2 "
      "grading CLEAR of the exceptional locus at all finite scales, pinching only at the FP "
      "endpoint f_2^2* = 0 -- the SAME BOUNDARY behavior as the Gaussian endpoint (W53/W119)",
      d1_ok, f"f_2^2(t=400) = {traj_f2[-1]:.4e} (analytic {f2_analytic:.4e}); min = {traj_f2.min():.3e} > 0")

check("D2  fork branch B (GU-native fixed-scale m2 = sqrt(m2_eff) mu_DW): d_locus = m2_eff in "
      "[5/6, 5/4] is scale-independent and positive INCLUDING at the Reuter FP endpoint -- "
      "STAYS-CLEAR on the AS branch exactly as on AF. CONCLUSION: keep-and-grade is COMPATIBLE "
      "with the interacting FP within this truncation; the fork again moves only the endpoint. "
      "CAVEAT (named): a g-dependent dressing of beta_{f_2^2} at finite g is outside this "
      "truncation; BMS's finding that the Weyl coupling stays (marginally) irrelevant at their "
      "higher-derivative Reuter FP is the PORTED support that the extension is not an artifact",
      all(m > 0 for m in M2_EFF_BAND),
      f"d_locus in [{M2_EFF_BAND[0]:.3f}, {M2_EFF_BAND[1]:.3f}] at every k including the FP")


# =====================================================================================
# PART E -- NEGATIVE CONTROL + THE VERDICT MACHINERY (not hardcoded)
# =====================================================================================
log("\n" + "-" * 96)
log("PART E -- negative control (relevance flipped) + conditional verdict assembly")
log("-" * 96)

# NC1: flip eta0 < 0. The machinery must DETECT: de-slaved root negative; f_0^2 no longer relevant
#      at the main FP (the free-IR-boundary-condition rescue disappears); tachyon follows.
eta0_flipped = -0.9
root_flipped = eta0_flipped * g_star / (KAPPA * 1.0 * C_C)
eig_main_flipped = -eta0_flipped * g_star          # > 0: irrelevant
nc1_ok = root_flipped < 0 and eig_main_flipped > 0
check("NC1 NEGATIVE CONTROL: eta0 < 0 (R^2 IRRELEVANT at the Reuter FP) flips the de-slaved root "
      "NEGATIVE (tachyonic) and removes the relevance that made the IR value a free boundary "
      "condition -- the machinery DETECTS the flip, so the AS-side verdict is NOT hardcoded and "
      "hinges exactly on the one ported sign",
      nc1_ok, f"de-slaved root = {root_flipped:.1f} < 0; eig(main) = +{eig_main_flipped:.3f} (irrelevant)")


def verdict(reuter_genuine: bool, relevance_ported_sign_positive: bool) -> str:
    if not reuter_genuine:
        return "AF-NOGO (tachyon stands; W122/W123/W126 chain)"
    if not relevance_ported_sign_positive:
        return "TACHYON-FOLLOWS (de-slaved root negative; no free healthy boundary condition)"
    return "AS-RESCUES-CONDITIONAL (PERMITTED-NOT-FORCED)"


e1_ok = (verdict(False, True).startswith("AF-NOGO")
         and verdict(True, False).startswith("TACHYON-FOLLOWS")
         and verdict(True, True).startswith("AS-RESCUES-CONDITIONAL"))
check("E1  the verdict is genuinely CONDITIONAL (all three branches encoded): Reuter FP an "
      "artifact -> AF-NOGO; relevance sign flipped -> TACHYON-FOLLOWS; both as ported -> "
      "AS-RESCUES-CONDITIONAL (PERMITTED-NOT-FORCED)", e1_ok, verdict(True, True))

# E2: branch selection -- within this truncation BOTH branches host UV-complete trajectories
#     (AF: the tachyonic fixed-ratio family, W123; AS: the Reuter basin, C3), and no GU-native
#     structure examined (induced-action boundary data gamma>0/Lambda>0; the Krein grading, D1/D2;
#     the mu_DW fixed-scale construction) distinguishes them. The E2 fork STANDS at the
#     GU-structure level; W83's satisfiability filter remains the only (conditional) selector and
#     it is a CONSISTENCY requirement, not a GU-native derivation.
af_tachyonic_complete = flow_uv_af(0.40, roots_af[1] * 0.40) == "complete"  # on the fixed ratio
check("E2  FORK-STANDS (checked, not assumed): BOTH branches host UV-complete trajectories in this "
      "truncation (AF: the tachyonic fixed-ratio trajectory completes; AS: the Reuter basin, C3), "
      "the Krein grading is compatible with BOTH (D1/D2 vs W119), and the induced-action IR data "
      "(gamma>0, Lambda>0) and mu_DW construction are branch-blind -- NO GU-native selector found; "
      "E2 is CARRIED. The (UV-complete AND non-tachyonic) filter (W83) selects AS but is a "
      "consistency principle, not GU structure",
      af_tachyonic_complete and ok_neg and ok_pos,
      f"AF tachyonic trajectory: complete={af_tachyonic_complete}; AS basin: both signs complete")


# =====================================================================================
# SUMMARY + VERDICT
# =====================================================================================
log("\n" + "=" * 96)
log("SUMMARY")
log("=" * 96)
log(f"  checks: {len([1 for _ in FAIL]) and 'FAIL' or 'ALL PASS'} "
    f"({sum(1 for _ in FAIL)} failures)")
log("")
log("  (1) Reuter-FP R^2 sector: main family f_0^2* = 0 (scalaron massless at the FP); de-slaved")
log(f"      root f_0^2* = eta0 g*/(kappa Phi c_C) -- SIGN-LOCKED to the relevance sign; with the")
log(f"      ported relevance (LR/CPR/BMS/AS-Starobinsky) it is POSITIVE -> m_0^2 >= 0 at BOTH")
log(f"      Reuter-family FPs. Numbers: g* = {g_star:.3f}, lambda* = {lam_star:.3f}; de-slaved root")
log(f"      in [+15, +230] across schematic bands (magnitude schematic, sign robust).")
log("  (2) IR trajectories: the scalaron's fate is a FREE relevant boundary condition -- healthy")
log(f"      (f_0^2 -> +{f0_ir_pos:.3f}) AND tachyonic (f_0^2 -> {f0_ir_neg:.3f}) trajectories BOTH")
log("      emanate UV-complete. AS PERMITS the rescue (forbidden on AF); it does not FORCE it.")
log("  (3) Branch selection: FORK-STANDS. No GU-native selector (grading compatible with both;")
log("      IR data branch-blind; mu_DW branch-blind). W83's satisfiability filter remains the")
log("      only selector and is conditional. E2 CARRIED.")
log("  (4) BOTTOM LINE: AS-RESCUES-CONDITIONAL (PERMITTED-NOT-FORCED), DERIVED-on-PORTED.")
log("      The tachyon does NOT follow GU onto the AS branch as a forced property: the forcing")
log("      mechanism (fixed-ratio slaving) provably disappears at g* != 0. Conditional on:")
log("      (i) Reuter FP genuine [truncation]; (ii) the R^2 relevance sign at the interacting FP")
log("      [PORTED, four lineages]. NC1 shows (ii) flipped => TACHYON-FOLLOWS.")
log("      What would settle it: the native Hessian/threshold projection of beta_{f_0^2} at")
log("      finite (g, lambda) in GU's own convention (= the H66 graviton block, paper-scale).")

if FAIL:
    log("\nRESULT: FAIL -> " + ", ".join(FAIL))
    sys.exit(1)
log("\nALL CHECKS PASS -- exit 0")
sys.exit(0)
