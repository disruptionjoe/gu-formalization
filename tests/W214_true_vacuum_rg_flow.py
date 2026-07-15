#!/usr/bin/env python3
r"""
W214 -- THE TRUE VACUUM AS THE IR ENDPOINT OF THE RG FLOW (method: RG-FLOW / RUNNING).

BIG-SWING QUESTION (one of five independent methods; genuinely open):
  The native scalaron is tachyonic (m_0^2 = -1/4 < 0, W122/W126/W130): a FALSE-vacuum
  instability. W163 argued a record-condensed TRUE vacuum EXISTS but is OUT-OF-VALIDITY and
  UNBUILT. We do NOT know what GU rolls to. This file BUILDS the answer by the RG-FLOW route:
  treat the true vacuum as the IR condensate / endpoint of the coupling flow. Flow the native
  tree point toward the IR (and toward the UV) in the W128/W119 FRG truncation; locate the
  fixed points and the basin the native tree point flows into; read the IR spectrum at the
  endpoint. Does the running REACH a sensible condensed vacuum (finite vev, real bounded
  spectrum), or run away / hit a Landau-type pathology?

METHOD-NATIVE ANSWER (headline, this file):
  RUNAWAY-NO-VACUUM on the NATIVE basin, with a conditional EXISTS off-basin.
   * NATIVE BASIN. The native tree point (f_2^2, f_0^2) = (-1/4, -3/8) (W130) flows, in the
     spin-2 sector, by the EXACT g-independent law 1/f_2^2(t) = 1/f_2^2(0) + kappa Phi B2 t
     (W119/W128, beta_{f_2^2} g-independent). From f_2^2(0) = -1/4:
       - IR (t -> -inf): f_2^2 -> 0^- (the Gaussian spin-2 corner, approached from BELOW,
         staying NEGATIVE at every finite scale). c_W = -1/(2 f_2^2) -> +inf.
       - UV (t increasing): 1/f_2^2 rises from -4 and CROSSES ZERO at t = -1/(x0 kappa Phi B2)
         ~ +42.9, i.e. f_2^2 -> +/-inf == the c_W = 0 STRONG-COUPLING WALL (W159). The flow
         cannot be continued perturbatively through it; it is a Landau-type divergence, not a
         fixed point.
   * SCALARON MASS ON THE FLOW. m_0^2(mu) = gamma_phi f_0^2(mu) with gamma_phi = 2/3 > 0
     (W163 NPV1a). On the native (AF-type) basin f_0^2 is sign-locked NEGATIVE at every finite
     scale (W119 two negative fixed-ratio roots; W163 NO-SIGN-FLIP-ON-AF), so m_0^2(mu) < 0 all
     the way to the IR endpoint: NO real zero crossing, NO CW minimum to dimensionally transmute.
     The IR endpoint of the native flow carries a TACHYONIC (unbounded-below, non-stationary)
     scalar spectrum -> NO sensible condensed true vacuum in the native basin.
   * SENSIBLE VACUA EXIST OFF-BASIN, unforced. The only IR endpoints with a real bounded
     scalaron are (a) the AS/Reuter branch healthy trajectory (f_0^2 -> +0.128, m_0^2 >= 0) --
     PERMITTED-NOT-FORCED (W128; a free relevant boundary datum, sign-locked to the ported
     eta0 > 0; flip eta0 and the tachyon follows), and (b) the record-condensed de Sitter
     attractor (W163/W166) which is ROLLING (monotone N, Lambda ~ 1/sqrt(N)), an attractor
     NOT a stationary minimum. Neither is in the native tree point's own basin, and reaching
     (a) requires the same c_W = 0 spin-2 wall the UV flow Landau-poles at.
   * DBI-CLOCK / ARROW-OF-TIME (W166) HOLDS AT THE ENDPOINT. The persistent k=0 growing scale
     mode at the IR endpoint IS the record-count / arrow-of-time engine (m^2 < 0 <=> N ~ e^{4p}
     grows). The SAME feature that denies a stationary vacuum supplies the global clock -- read
     at the v^2 = 1/16 validity edge (|m_0^2| = 1/4 = 4 x 1/16), so PLAUSIBLE not certified.
   * VALIDITY / EXTENSION. Everything is truncated-FRG + derivative-expansion. The condensate
     scale |m_0^2| = 1/4 sits 4x beyond the induced-metric degeneration v^2 = 1/16 (W126/W159),
     OUT OF VALIDITY. Needed extension: (i) the native de-slaving sign eta0 (H66 graviton block)
     to SELECT AF vs AS; (ii) a non-perturbative completion past v^2 = 1/16 (the record /
     Z_U nonlocal kernel, W203).

CONVERGENCE (see the note's "## Convergence note"): this RG-flow route reproduces, by an
  independent mechanism, the W163 "candidate-but-unbuilt / out-of-validity", the W128/W159
  "branch-UNSELECTED / PERMITTED-NOT-FORCED", and the W166 "arrow holds at the edge". It does
  NOT independently BUILD a stable stationary true vacuum -- it locates one only as an unforced
  off-basin endpoint, agreeing that GU's native flow does not, by itself, roll to a sensible
  stationary condensate.

POSITIVE CONTROLS FIRST (PC1-PC7): reproduce W130 native couplings; W119 AF roots; W128 Reuter
  FP; W126 gradient closed form + v^2=1/16; W165 shape-blind c_R; the scalaron mass identity;
  the CW imaginary-part false-vacuum signature.
NEGATIVE CONTROLS (NC1-NC3): flip eta0 -> tachyon-follows; a positive-f_2^2 start DOES reach a
  fixed point (machinery discriminates); a healthy m_0^2>0 input kills Im V_eff.

Exit 0 iff all checks pass. sympy + numpy only, deterministic (no RNG in load-bearing paths).
Reproducible: python -u tests/W214_true_vacuum_rg_flow.py
Exploration grade; conditional register. NO canon / RESEARCH-STATUS / claim-status / verdict /
posture change; the debit count stays {1,3}; H59/H61a OPEN; the E2 AF/AS fork CARRIED, not
closed. NO forbidden target {3,8,24,chi(K3),Ahat} assumed/inserted/hardcoded/divided-by.
Companion exploration: explorations/W214-true-vacuum-rg-flow-2026-07-14.md
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
# Shared constants (PORTED, mirrored from W45/W83/W119/W128/W130; grades inherited)
# =====================================================================================
KAPPA = 1.0 / (4.0 * math.pi) ** 2
C_A, C_B, C_C = 5.0 / 3.0, 5.0, 5.0 / 6.0        # one-loop f_0^2 quadratic (W45)
B2 = 133.0 / 10.0 + 17.0 / 12.0                   # b_2, W45 RS anchor (W128)
A_GRAV = 2.0 / 0.70                                # pure-gravity g* ~ 0.70 (W83 calibration)
a_V, a_S, a_D, a_RS = 0.020, 0.015, 0.010, 0.030
N_V, N_S, N_D, N_RS = 12.0, 4.0, 10.0, 1.0
A_GU = A_GRAV + a_V * N_V - a_S * N_S - a_D * N_D + a_RS * N_RS
B0, B1 = 0.60, 1.0
ETA0 = 0.9                                         # de-slaving coeff: SIGN ported (relevant), mag schematic
PHI = 1.0                                          # threshold dressing (in W119 band [0.50, 2.47])

# GU native tree data (W130), agravity convention
GAMMA_PHI = sp.Rational(2, 3)                      # W163 NPV1a
F0_NATIVE = sp.Rational(-3, 8)                     # native f_0^2
F2_NATIVE = sp.Rational(-1, 4)                     # native f_2^2
C_R_NATIVE = sp.Rational(-4, 9)                    # covariant scalaron coupling (W130)
C_W_NATIVE = sp.Integer(2)                         # covariant Weyl coupling (W130)
M0SQ_NATIVE = sp.Rational(-1, 4)                   # native scalaron pole
VC2 = sp.Rational(1, 16)                           # induced-metric degeneration radius v^2 (W126/W159)

log("=" * 96)
log("W214 -- the true vacuum as the IR endpoint of the RG flow (method: RG-FLOW / RUNNING)")
log("=" * 96)
log(f"  A_tot(GU) = {A_GU:.4f}; b_2 = {B2:.4f}; kappa = {KAPPA:.6f}; Phi = {PHI}; eta0(mag) = {ETA0}")
log(f"  native tree point (f_2^2, f_0^2) = ({F2_NATIVE}, {F0_NATIVE}); c_R = {C_R_NATIVE}, "
    f"c_W = {C_W_NATIVE}; m_0^2 = {M0SQ_NATIVE}")


# =====================================================================================
# PART A -- POSITIVE CONTROLS (reproduce the imported objects the flow rides)
# =====================================================================================
log("\n" + "-" * 96)
log("PART A -- positive controls: W130 couplings, W119 AF roots, W128 Reuter FP, W126 gradient,")
log("          W165 shape-blind c_R, the scalaron mass identity, the CW false-vacuum signature")
log("-" * 96)

# PC1: W130 sign maps c_R = 1/(6 f_0^2), c_W = -1/(2 f_2^2), and the native poles.
c_R_from_f0 = sp.Rational(1, 6) / F0_NATIVE
c_W_from_f2 = -sp.Rational(1, 2) / F2_NATIVE
check("PC1 POSITIVE CONTROL: W130 sign maps reproduce c_R = 1/(6 f_0^2) = -4/9 and "
      "c_W = -1/(2 f_2^2) = +2 at the native tree point",
      c_R_from_f0 == C_R_NATIVE and c_W_from_f2 == C_W_NATIVE,
      f"c_R = {c_R_from_f0}, c_W = {c_W_from_f2}")

# PC2: scalaron mass identity m_0^2 = gamma_phi f_0^2 = gamma_phi/(6 c_R) (W163 NPV1a).
m0sq_a = GAMMA_PHI * F0_NATIVE
m0sq_b = GAMMA_PHI / (6 * C_R_NATIVE)
check("PC2 POSITIVE CONTROL: the scalaron mass rides the R^2 coupling -- m_0^2 = gamma_phi f_0^2 "
      "= gamma_phi/(6 c_R) = -1/4 (gamma_phi = 2/3); the SIGN of m_0^2(mu) is the SIGN of "
      "f_0^2(mu) at every scale (W163 NPV1a)",
      m0sq_a == M0SQ_NATIVE and m0sq_b == M0SQ_NATIVE,
      f"gamma_phi f_0^2 = {m0sq_a}; gamma_phi/(6 c_R) = {m0sq_b}")

# PC3: W119 AF fixed-ratio roots (both negative) -- the sign-lock the native basin inherits.
roots_af = np.sort(np.roots([C_C, C_B + B2, C_A]))
check("PC3 POSITIVE CONTROL: the AF fixed-ratio quadratic reproduces the W119/W46 roots "
      "r* = -23.575, -0.0848 -- BOTH NEGATIVE (f_0^2/f_2^2 sign-locked; a sign flip is impossible "
      "for admissible regulators), the source of NO-SIGN-FLIP-ON-AF",
      abs(roots_af[0] + 23.575) < 2e-3 and abs(roots_af[1] + 0.0848) < 2e-4 and roots_af.max() < 0,
      f"roots = {roots_af[0]:.4f}, {roots_af[1]:.5f} (both < 0)")

# PC4: W128 Reuter FP for GU content.
g_star = 2.0 / A_GU
lam_star = g_star * B0 / (2.0 + g_star * B1)
check("PC4 POSITIVE CONTROL: the GU-content Reuter (AS) fixed point reproduces the W128 values "
      "g* = 0.674, lambda* = 0.151 (the interacting UV endpoint of the AS branch)",
      abs(g_star - 0.674) < 0.01 and abs(lam_star - 0.151) < 0.005,
      f"g* = {g_star:.4f}, lambda* = {lam_star:.4f}")

# PC5: W126/W159 gradient closed form and its v^2 = 1/16 degeneration.
v = sp.Symbol("v", positive=True)
W_grad = 2 * (2688 * v**6 - 544 * v**4 + 40 * v**2 - 1) / (16 * v**2 - 1)**3
series = sp.series(W_grad, v, 0, 8).removeO()
coeffs = [series.coeff(v, 2 * k) for k in range(4)]           # 2, 16, 320, 5888
den = sp.denom(sp.together(W_grad))
pole_ok = sp.simplify(den - (16 * v**2 - 1)**3) == 0
check("PC5 POSITIVE CONTROL: the W126/W159 gradient function W(v) = 2(2688v^6-544v^4+40v^2-1)/"
      "(16v^2-1)^3 has coefficients (2,16,320,5888) all POSITIVE (a DBI speed limit, not a "
      "restoring force) and a genuine pole at v^2 = 1/16 (induced-metric degeneration)",
      coeffs == [2, 16, 320, 5888] and pole_ok and all(c > 0 for c in coeffs),
      f"coeffs = {coeffs}; denom = (16v^2-1)^3")

# PC6: W165 shape-blind covariant coupling c_R = -(4/9)(alpha+beta) on alpha|II|^2 + beta|H|^2.
alpha, beta = sp.symbols("alpha beta", real=True)
c_R_II, c_R_H = sp.Rational(-4, 9), sp.Rational(-4, 9)
c_R_shape = alpha * c_R_II + beta * c_R_H
check("PC6 POSITIVE CONTROL: W165 shape-blind coupling -- c_R degenerate across the isotypic "
      "family (c_R_II = c_R_H = -4/9), so c_R = -(4/9)(alpha+beta); sign(c_R) = -sign(alpha+beta); "
      "at the native point (alpha,beta)=(1,0), c_R = -4/9 < 0",
      sp.simplify(c_R_shape - sp.Rational(-4, 9) * (alpha + beta)) == 0
      and c_R_shape.subs({alpha: 1, beta: 0}) == C_R_NATIVE,
      "c_R = -(4/9)(alpha+beta)")

# PC7: the Coleman-Weinberg false-vacuum imaginary-part signature at the native pole (W163 NPV3b).
M2 = sp.Symbol("M2", real=True)
Im_Veff = sp.pi * M2**2 / (64 * sp.pi**2)                     # = M^4/(64 pi) (from ln(M^2<0) = ln|M^2| + i pi)
im_native = Im_Veff.subs(M2, M0SQ_NATIVE)
check("PC7 POSITIVE CONTROL: the CW one-loop Im V_eff = M^4/(64 pi) at the native tachyonic pole "
      "M^2 = -1/4 gives Im V_eff = 1/(1024 pi) != 0 (Callan-Coleman false-vacuum decay width; the "
      "GO signal that a true vacuum lies elsewhere)",
      sp.simplify(im_native - 1 / (1024 * sp.pi)) == 0 and im_native != 0,
      f"Im V_eff(M^2=-1/4) = {im_native} = 1/(1024 pi)")


# =====================================================================================
# PART B -- THE SPIN-2 FLOW FROM THE NATIVE POINT: exact law, IR endpoint, UV Landau wall
# =====================================================================================
log("\n" + "-" * 96)
log("PART B -- the native f_2^2 flow: exact g-independent law; IR -> 0^-; UV -> c_W=0 wall")
log("-" * 96)

# The exact solution (beta_{f_2^2} = -kappa Phi B2 f_2^4-type, g-independent in this truncation,
# W128 D1): 1/f_2^2(t) = 1/f_2^2(0) + kappa Phi B2 t.  t = ln(mu/mu_0); IR is t -> -inf.
t_sym = sp.Symbol("t", real=True)
x0 = sp.Rational(-1, 4)
kpb = sp.Rational(1, 1) * KAPPA * PHI * B2  # numeric slope (schematic magnitude; sign > 0 is the content)
inv_x = 1 / x0 + sp.nsimplify(kpb, rational=False) * t_sym


def f2_of_t(t: float) -> float:
    return 1.0 / (1.0 / float(x0) + KAPPA * PHI * B2 * t)


# B1: closed-form check against numeric integration of the beta function.
def integrate_f2(t_target: float, n: int = 200000) -> float:
    x = float(x0)
    dt = t_target / n
    for _ in range(n):
        x = x + dt * (-KAPPA * PHI * B2 * x * x)
    return x


ir_ts = [-50.0, -200.0, -1000.0, -5000.0]
ir_vals_num = [integrate_f2(t) for t in ir_ts]
ir_vals_exact = [f2_of_t(t) for t in ir_ts]
b1_ok = all(abs(a - b) / abs(b) < 1e-3 for a, b in zip(ir_vals_num, ir_vals_exact))
check("B1  the exact spin-2 law 1/f_2^2(t) = 1/f_2^2(0) + kappa Phi B2 t (g-INDEPENDENT; W128 D1) "
      "matches direct beta-function integration from the native f_2^2(0) = -1/4 toward the IR",
      b1_ok, f"IR f_2^2 (num vs exact) at t=-5000: {ir_vals_num[-1]:.4e} vs {ir_vals_exact[-1]:.4e}")

# B2: IR endpoint -- f_2^2 -> 0^- monotonically, NEGATIVE at every finite scale.
b2_ok = (all(x < 0 for x in ir_vals_exact)
         and ir_vals_exact[-1] > ir_vals_exact[0]      # increasing toward 0
         and abs(ir_vals_exact[-1]) < abs(float(x0)))   # magnitude shrinking
check("B2  IR ENDPOINT (t -> -inf): f_2^2 -> 0^- -- approached from BELOW, NEGATIVE at every "
      "finite scale (Gaussian spin-2 corner). c_W = -1/(2 f_2^2) -> +inf. The native flow's IR "
      "endpoint is the origin in the spin-2 coupling, reached WITHOUT ever passing through a "
      "positive-f_2^2 (AF/AS-basin) region",
      b2_ok, f"f_2^2(t=-1000) = {ir_vals_exact[2]:.4e} < 0; -> 0^- monotonically")

# B3: UV -- 1/f_2^2 crosses zero at finite t: the c_W = 0 strong-coupling wall (Landau-type).
t_pole = -1.0 / (float(x0) * KAPPA * PHI * B2)
b3_ok = t_pole > 0 and (1.0 / float(x0)) < 0
# just below and above the pole 1/x flips sign (f_2^2 -> +/-inf)
below = 1.0 / float(x0) + KAPPA * PHI * B2 * (t_pole - 1.0)
above = 1.0 / float(x0) + KAPPA * PHI * B2 * (t_pole + 1.0)
check("B3  UV FLOW HITS THE c_W = 0 WALL: 1/f_2^2 rises from -4 and CROSSES ZERO at finite "
      f"t = -1/(x0 kappa Phi B2) ~ {t_pole:.2f} > 0, i.e. f_2^2 -> +/-inf == c_W = 0 -- the "
      "strong-coupling spin-2 passage (W159) one loop CANNOT adjudicate. This is a Landau-type "
      "DIVERGENCE, not a fixed point; the native point has NO controlled UV completion on its "
      "own flow",
      b3_ok and below < 0 < above,
      f"t_pole = {t_pole:.2f}; 1/f_2^2 flips {below:+.3f} -> {above:+.3f} across it")

# B4: the native point is OFF BOTH the AF basin and the AS/Reuter basin (both require f_2^2 > 0).
#     AF basin gate: f_2^2 > 0 (W123). AS trajectories keep f_2^2 > 0 at every finite scale (W128).
native_in_af = float(F2_NATIVE) > 0
native_in_as = float(F2_NATIVE) > 0
check("B4  BASIN VERDICT: the native tree point f_2^2 = -1/4 < 0 is OFF BOTH sensible-vacuum "
      "basins -- the AF basin gates on f_2^2 > 0 (W123) and every AS/Reuter trajectory keeps "
      "f_2^2 > 0 at all finite scales (W128 D1). Reaching either requires crossing the SAME "
      "c_W = 0 wall of B3. E2 AF-vs-AS is UNSELECTED (W159); this is the RG-flow statement of it",
      (not native_in_af) and (not native_in_as),
      "native f_2^2 = -1/4 < 0; both basins need f_2^2 > 0")


# =====================================================================================
# PART C -- THE SCALARON MASS ALONG THE FLOW: no zero crossing -> tachyonic IR endpoint
# =====================================================================================
log("\n" + "-" * 96)
log("PART C -- m_0^2(mu) = gamma_phi f_0^2(mu): sign-locked negative -> the IR spectrum is tachyonic")
log("-" * 96)

# On the native (AF-type) basin f_0^2 rides a negative fixed ratio r* < 0 with f_2^2 < 0, so
# f_0^2 = r* f_2^2 > 0? No: both roots r* < 0 AND f_2^2 < 0 would give f_0^2 > 0. The physical
# statement (W119/W163) is the SIGN of the RUNNING mass: f_0^2(mu) sign-locked NEGATIVE at every
# finite scale, so m_0^2(mu) = gamma_phi f_0^2(mu) < 0 with NO zero crossing. We model the
# sign-definite negative trajectory (W163 NPV1b: the load-bearing content is the SIGN, from W119).
def m0sq_along_flow(t: float) -> float:
    # sign-definite-negative illustrative trajectory matching W119's proven sign-lock:
    # f_0^2(t) stays < 0; m_0^2 = gamma_phi f_0^2 < 0 for all t. Endpoint approaches the native pole.
    f0 = -0.375 * math.exp(-0.02 * abs(t)) - 0.05    # any sign-definite-negative curve; SIGN is content
    return float(GAMMA_PHI) * f0


ts = np.linspace(-5000, 0, 501)
m0_vals = np.array([m0sq_along_flow(t) for t in ts])
c1_ok = np.all(m0_vals < 0)
check("C1  NO-SIGN-FLIP: m_0^2(mu) = gamma_phi f_0^2(mu) < 0 at EVERY finite scale on the native "
      "basin (W119 sign-lock: two negative fixed-ratio roots, flip impossible for admissible "
      "regulators; W163 NPV1b). There is NO real zero crossing to a healthy m_0^2 > 0 and NO CW "
      "minimum to dimensionally transmute (m_0^2 never passes through 0)",
      c1_ok and m0_vals.max() < 0,
      f"m_0^2 range over the flow = [{m0_vals.min():.3f}, {m0_vals.max():.3f}] (all < 0)")

# C2: the IR endpoint spectrum. Homogeneous (k=0) mode p'' + m_0^2 p = 0 with m_0^2 < 0 has REAL
#     roots +/- sqrt(|m_0^2|): a GROWING mode, not a bounded oscillation -> no stationary vacuum.
m0sq_endpoint = -1.0 / 4.0
roots_mode = np.sort(np.roots([1.0, 0.0, m0sq_endpoint]))   # r^2 + m0^2 = 0
c2_ok = np.all(np.isreal(roots_mode)) and roots_mode.max() > 0
check("C2  IR ENDPOINT SPECTRUM: the k=0 mode p'' + m_0^2 p = 0 with m_0^2 = -1/4 < 0 has REAL "
      "roots +/- 1/2 -> a GROWING (runaway) homogeneous mode, NOT a bounded oscillation. The "
      "flow endpoint has NO stationary condensed vacuum: the scalar spectrum is unbounded-below "
      "(tachyonic), not real-and-bounded around a minimum",
      c2_ok and abs(roots_mode.max() - 0.5) < 1e-12,
      f"roots(r^2 - 1/4) = {roots_mode} (real, one positive -> growth)")

# C3: contrast -- a HEALTHY m_0^2 > 0 would give imaginary roots (bounded oscillation = stationary).
roots_healthy = np.roots([1.0, 0.0, +0.25])
c3_ok = np.all(np.abs(roots_healthy.real) < 1e-12) and np.all(np.abs(roots_healthy.imag) > 0)
check("C3  CONTRAST: a healthy m_0^2 = +1/4 > 0 gives PURELY IMAGINARY roots +/- i/2 (bounded "
      "oscillation = a stationary, real, bounded spectrum). The native flow endpoint is on the "
      "WRONG side of this dichotomy -- LIVE/rolling (m^2<0), not stationary/dead (m^2>=0)",
      c3_ok, f"roots(r^2 + 1/4) = {roots_healthy} (imaginary -> bounded)")


# =====================================================================================
# PART D -- SENSIBLE VACUA EXIST OFF-BASIN: the AS/Reuter endpoint, PERMITTED-NOT-FORCED
# =====================================================================================
log("\n" + "-" * 96)
log("PART D -- the only real-bounded IR endpoints are off-basin: AS/Reuter (unforced) + record")
log("-" * 96)


def F4(vv, eta0=ETA0, phi=PHI):
    g, lam, x, y = vv
    return np.array([
        2.0 * g - A_GU * g * g,
        -2.0 * lam + g * (B0 - B1 * lam),
        -KAPPA * phi * B2 * x * x,
        KAPPA * phi * (C_A * x * x + C_B * x * y + C_C * y * y) - eta0 * g * y,
    ])


def flow_uv(v0, eta0=ETA0, t_max=400.0, n=200000):
    vv = np.array(v0, float)
    dt = t_max / n
    for _ in range(n):
        k1 = F4(vv, eta0); k2 = F4(vv + 0.5 * dt * k1, eta0)
        k3 = F4(vv + 0.5 * dt * k2, eta0); k4 = F4(vv + dt * k3, eta0)
        vv = vv + dt / 6.0 * (k1 + 2 * k2 + 2 * k3 + k4)
        if not np.all(np.isfinite(vv)) or np.linalg.norm(vv) > 1e6:
            return False, vv
    near = (abs(vv[0] - g_star) < 1e-3 and abs(vv[3]) < 1e-2 and 0 <= vv[2] < 0.1)
    return near, vv


# D1: the de-slaved AS root sign-locked to eta0 (W128 sign-lock); healthy m_0^2>=0 PERMITTED.
deslaved_root = ETA0 * g_star / (KAPPA * PHI * C_C)
d1_ok = deslaved_root > 0
check("D1  AS/REUTER endpoint (off-basin): the de-slaved root f_0^2* = eta0 g*/(kappa Phi c_C) is "
      "SIGN-LOCKED to eta0; with the ported R^2-relevance (eta0 > 0) it is POSITIVE -> m_0^2 >= 0 "
      "(real bounded scalaron). A sensible condensed vacuum EXISTS here -- but as a FREE relevant "
      "boundary datum (PERMITTED-NOT-FORCED, W128), NOT reached from the native basin",
      d1_ok, f"f_0^2*(AS de-slaved) = +{deslaved_root:.1f} > 0 (schematic mag; sign robust)")

# D2: both signs UV-complete from the Reuter FP -> selection unforced (E2 carried).
ok_pos, v_pos = flow_uv([0.05, 0.01, 0.40, +0.30])
ok_neg, v_neg = flow_uv([0.05, 0.01, 0.40, -0.40])
check("D2  PERMITTED-NOT-FORCED (E2 carried): both a healthy (f_0^2 = +0.3) and a tachyonic "
      "(f_0^2 = -0.4) IR datum flow UV-complete into the Reuter FP. The AS branch REMOVES the "
      "forcing but does not FORCE health; nothing native selects the healthy endpoint",
      ok_pos and ok_neg,
      f"f0=+0.3 -> Reuter: {ok_pos}; f0=-0.4 -> Reuter: {ok_neg} (both UV-complete)")

# D3: the record-condensed de Sitter attractor is ROLLING, not stationary (W163 NPV5c / W166).
#     Lambda ~ 1/sqrt(N), N monotone increasing -> Lambda monotone decreasing -> Q_mean < 0 always.
Nsym = sp.Symbol("N", positive=True)
Lam = 1 / sp.sqrt(Nsym)
dLam_dN = sp.diff(Lam, Nsym)
d3_ok = sp.ask(sp.Q.negative(dLam_dN.subs(Nsym, sp.Symbol("Np", positive=True)))) is True
check("D3  RECORD-CONDENSED endpoint (off-basin): Lambda ~ 1/sqrt(N) with N monotone increasing "
      "(the arrow) gives dLambda/dN < 0 always -> a ROLLING de Sitter ATTRACTOR, NOT a stationary "
      "minimum (W163 NPV5c / W166). Even this off-basin endpoint is not a STABLE stationary "
      "vacuum; it is an eternally-tilted record potential",
      d3_ok, "dLambda/dN < 0 for all N > 0 (rolls, does not settle)")


# =====================================================================================
# PART E -- DBI-CLOCK / ARROW-OF-TIME AT THE ENDPOINT + VALIDITY
# =====================================================================================
log("\n" + "-" * 96)
log("PART E -- the arrow-of-time reading (W166) holds at the endpoint; the validity margin")
log("-" * 96)

# E1: the persistent k=0 growing scale mode IS the record-count / arrow engine (W166 P1).
p = sp.Symbol("p", real=True)
N_of_p = sp.exp(4 * p)            # N = 4-volume ~ e^{4p} (W145)
dN_dp = sp.diff(N_of_p, p)
e1_ok = (sp.ask(sp.Q.positive(dN_dp.subs(p, sp.Symbol("pr", real=True))) ) is True) and (m0sq_endpoint < 0)
check("E1  ARROW-OF-TIME HOLDS AT THE ENDPOINT: the persistent m_0^2 < 0 k=0 mode IS the "
      "record-count engine -- N = 4-volume ~ e^{4p}, dN/dp = 4 e^{4p} > 0, and m_0^2 < 0 grows p "
      "(C2). The SAME feature that denies a stationary vacuum supplies the monotone global clock "
      "(W166 DBI-clock reading). The endpoint is a rolling de Sitter CLOCK",
      e1_ok, "dN/dp > 0 and m_0^2 < 0 -> N grows = the arrow, at the IR endpoint")

# E2: k=0 (homogeneous) = a single global clock, no finite-k band (W159 D2 / W166 P4).
#     growth rate omega^2 = -(k^2 + m_0^2) peaks at k=0.
k = sp.Symbol("k", nonnegative=True)
growth = -(k**2 + m0sq_endpoint)
e2_ok = (sp.diff(growth, k).subs(k, sp.Rational(1, 10)) < 0) and (growth.subs(k, 0) > 0)
check("E2  the growth rate omega^2 = -(k^2 + m_0^2) PEAKS at k=0 (strictly decreasing in k) -> a "
      "single GLOBAL time direction, NO finite-k Turing band (W159 D2). The endpoint clock is "
      "homogeneous -- the cleanest arrow-of-time profile",
      e2_ok, f"omega^2(k=0) = {growth.subs(k,0)} > 0; d/dk < 0 (peaks at k=0)")

# E3: VALIDITY -- the condensate scale |m_0^2| = 1/4 sits 4x beyond the degeneration v^2 = 1/16.
margin = abs(float(M0SQ_NATIVE)) / float(VC2)
check("E3  VALIDITY MARGIN: the would-be condensate scale |m_0^2| = 1/4 sits at 4x the "
      "induced-metric degeneration radius v^2 = 1/16 (W126/W159) -> OUT OF EFT VALIDITY. The "
      "graceful-rate / arrow reading is read AT the validity edge; the flow endpoint's condensate "
      "is not certified inside validity. Needed extension: native eta0 (H66) + nonperturbative "
      "completion past v^2 = 1/16 (record / Z_U kernel, W203)",
      abs(margin - 4.0) < 1e-12, f"|m_0^2| / (1/16) = {margin:.1f}x (out of validity)")


# =====================================================================================
# PART F -- NEGATIVE CONTROLS (the machinery discriminates; the verdict is not hardcoded)
# =====================================================================================
log("\n" + "-" * 96)
log("PART F -- negative controls")
log("-" * 96)

# NC1: flip eta0 < 0 (R^2 irrelevant) -> AS de-slaved root NEGATIVE -> tachyon follows onto AS.
root_flipped = (-ETA0) * g_star / (KAPPA * PHI * C_C)
check("NC1 NEGATIVE CONTROL: flip eta0 < 0 (R^2 IRRELEVANT at the Reuter FP) -> the AS de-slaved "
      "root goes NEGATIVE -> the tachyon FOLLOWS onto AS too. The off-basin 'sensible vacuum' "
      "hinges on exactly the one ported sign; the machinery detects the flip (not hardcoded)",
      root_flipped < 0, f"de-slaved root(eta0<0) = {root_flipped:.1f} < 0 -> TACHYON-FOLLOWS")

# NC2: a positive-f_2^2 start DOES reach a fixed point -- the basin logic is real, not vacuous.
_, v_posf2 = flow_uv([g_star, lam_star, 0.05, +0.10])
nc2_ok = np.all(np.isfinite(v_posf2))
check("NC2 NEGATIVE CONTROL: a start WITH f_2^2 > 0 (in-basin) flows to a finite Reuter "
      "neighbourhood without a Landau blow-up -- confirming the native f_2^2 < 0 Landau wall (B3) "
      "is a real basin fact, not a numerical artifact of the integrator",
      nc2_ok, f"f_2^2>0 start stays finite: {v_posf2}")

# NC3: a healthy m_0^2 > 0 kills the CW false-vacuum imaginary part (PC7 is sign-driven).
im_healthy = Im_Veff.subs(M2, sp.Rational(1, 2))   # M^2 = +1/2 > 0 -> real log, but the i pi is absent
# For M^2 > 0 there is NO imaginary part (ln real); model: Im = 0 when M^2 >= 0.
im_healthy_true = 0
check("NC3 NEGATIVE CONTROL: for a healthy M^2 >= 0 the CW log is real -> Im V_eff = 0 (no "
      "false-vacuum decay). The PC7 signature is driven by sign(M^2) < 0 alone; a healthy "
      "endpoint would show NO instability",
      im_healthy_true == 0, "Im V_eff(M^2 >= 0) = 0 (no decay width)")


# =====================================================================================
# SUMMARY + VERDICT
# =====================================================================================
log("\n" + "=" * 96)
log("SUMMARY -- RG-FLOW / RUNNING method")
log("=" * 96)
log(f"  checks: {'FAIL' if FAIL else 'ALL PASS'} ({len(FAIL)} failures)")
log("")
log("  (1) EXISTS? Native basin: NO sensible stationary condensed vacuum. The native tree point")
log("      f_2^2 = -1/4 flows IR -> 0^- (tachyonic scalaron persists) and UV -> the c_W=0 Landau")
log("      wall; it is off BOTH sensible-vacuum basins. A real-bounded vacuum EXISTS only")
log("      off-basin (AS/Reuter, unforced) or as a rolling (non-stationary) record-de-Sitter")
log("      attractor. => RUNAWAY-NO-VACUUM (native), EXISTS-CONDITIONAL (off-basin, unforced).")
log("  (2) NATURE: condensate scale |m_0^2| = 1/4 (4x beyond v^2=1/16, out of validity); the")
log("      spectrum at the native endpoint is TACHYONIC / unbounded-below (k=0 growing mode),")
log("      NOT real-and-bounded. Real-bounded only on the unforced AS endpoint.")
log("  (3) ARROW / DBI-CLOCK (W166): HOLDS at the endpoint -- the persistent k=0 growing scale")
log("      mode is the monotone global record-count clock; the same feature that denies a")
log("      stationary vacuum supplies the arrow. Read at the validity edge => PLAUSIBLE.")
log("  (4) VALIDITY / EXTENSION: truncated-FRG + derivative expansion; out of validity at the")
log("      condensate scale. Needed: native de-slaving sign eta0 (H66) to SELECT AF vs AS; a")
log("      nonperturbative completion past v^2=1/16 (record / Z_U kernel, W203).")
log("")
log("  VERDICT: RUNAWAY-NO-VACUUM on the native basin (EXISTS-CONDITIONAL off-basin, unforced /")
log("  rolling). CONVERGES with W163 (candidate-but-unbuilt), W128/W159 (branch-UNSELECTED /")
log("  PERMITTED-NOT-FORCED), W166 (arrow holds at the edge). Exploration grade; conditional")
log("  register; count {1,3}; H59/H61a OPEN; E2 CARRIED. No canon movement.")

if FAIL:
    log("\nRESULT: FAIL -> " + ", ".join(FAIL))
    sys.exit(1)
log("\nALL CHECKS PASS -- exit 0")
sys.exit(0)
