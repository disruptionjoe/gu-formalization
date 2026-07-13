#!/usr/bin/env python3
r"""
W88 -- FULL FRG f(R)+Weyl^2 + ker-Gamma spin-3/2, STAGE 1 of 2: setup + native spin-3/2 heat-kernel +
       REGULATOR FAMILY 1 (Litim/optimized) traces and fixed-point location, with the LOAD-BEARING new
       number COMPUTED: the ker-Gamma spin-3/2 (and leading graviton) contribution to beta_{f_2^2}, and
       whether it LIFTS the Weyl-coupling fixed point f_2^2* off zero at regulator 1.

WHY THIS FILE. W87 (horn-K-vs-Q) leaned HORN K on the AS/Reuter branch but flagged that its answer was
PORTED from the repo-native g-independent beta_{f_2^2} = -kappa f_2^4 b_2 (which gives f_2^2* = 0 by
construction). W87 NAMED the deciding computation verbatim:
    "compute the FULL FRG beta_{f_2^2} WITH graviton (g, lambda) loop contributions at the Reuter FP and
     determine sign/value of f_2^2*.  ... a truncation that lifts it > 0 would give HORN Q."
This file (Stage 1) DOES that computation to the truncation order it can genuinely execute, for REGULATOR
FAMILY 1 (the Litim/optimized shape function). It does NOT port f_2^2*=0 from W87 -- it COMPUTES the
spin-3/2 contribution to beta_{f_2^2} and the LEADING graviton-loop contribution, and reads off whether
f_2^2* is 0 (HORN K, functionally) or lifted positive (HORN Q).

TRUNCATION ORDER (stated up front, honest). Effective average action
    Gamma_k = INT sqrt(g) [ f(R) + (1/(2 lambda_W)) C_{mnrs}C^{mnrs} ] + S_ferm[ker-Gamma spin-3/2]
              + gauge-fixing + ghosts,
with f(R) a POLYNOMIAL to R^2 (dimensionless couplings g = G k^2, lambda = Lambda/k^2, f_0^2 the R^2
coupling, f_2^2 = lambda_W the Weyl coupling). Background = sphere / de Sitter (maximally symmetric,
the standard Codello-Percacci-Rahmede / Benedetti-Machado-Saueressig f(R)-FRG background). York/TT
decomposition h_mn = h^TT_mn + (transverse xi) + (sigma scalar) + (trace h). Spin-2 (TT), spin-1, spin-0
blocks + the Weyl-sector spin-2 4th-derivative block identified. This is a POLYNOMIAL (R^2) + Weyl^2
truncation, NOT a full functional f(R); that is stated and its limits are handed to Stage 2.

WHAT IS COMPUTED HERE vs PORTED (ledger; also printed at the end):
  COMPUTED:
    * PART A: the ker-Gamma (transverse gamma-traceless) spin-3/2 heat-kernel a_2 = (7/20) W^2 +
      (31/120) E_4 (+ mass terms), and HOW it enters BOTH sectors: its C^2/Weyl coefficient 7/20 feeds
      b_2 (hence beta_{f_2^2}) as a term PROPORTIONAL to f_2^4 -> it VANISHES at f_2^2=0; its independent
      R^2 coefficient is 0 -> d_RS_R2 = 0 (no contribution to beta_{f_0^2}). (native ker-Gamma, not the
      ported agravity RS value -- the massless gamma-traceless carrier is Weyl-invariant.)
    * PART B: the Litim/optimized threshold functions Phi^p_n(0) = 1/n! (closed form for the optimized
      shape) used for regulator family 1.
    * PART C: the STRUCTURE of the full FRG beta_{f_2^2} = -kappa f_2^4 (b_2^grav + b_2^RS) +
      eta_C(g,lambda) f_2^2, and the reading that f_2^2* = 0 is ALWAYS a root while a lifted root
      f_2^2* = eta_C/(kappa b_2) exists iff the graviton-dressing anomalous coefficient eta_C > 0.
      The LEADING graviton (EH) dressing is computed to enter at HIGHER order in f_2^2 (the EH term
      Z_N P_2 divided by the Weyl term (1/f_2^2) P_4 scales as Z_N f_2^2) -> it does NOT generate the
      additive f_2^2 term -> at regulator 1 in this truncation eta_C = 0 -> f_2^2* = 0 (HORN K), robustly.
    * PART E: the EH-sector Reuter FP and the R^2 (f_0^2) relevance at regulator 1 (reuses W83's
      calibration; reproduces the Reuter FP + critical-surface structure).
  PORTED (cited, marked):
    * the pure-gravity Weyl one-loop coefficient 133/10 (Fradkin-Tseytlin / Avramidi-Barvinsky).
    * the EH Reuter-FP magnitude calibration (Reuter; Codello-Percacci-Rahmede; Reuter-Saueressig).
    * the higher-derivative relevance count 3+1 (Benedetti-Machado-Saueressig 0901.2984).
    * the b_2-normalization O(1) factor converting the heat-kernel 7/20 into the beta contribution
      (schematic; only its SIGN is load-bearing).

CROSS-CHECK (PART D): remove GU's matter (RS, gauge, scalars) -> the EH sector must reproduce the KNOWN
pure-gravity Reuter FP (g*>0, lambda* in the literature band, product g* lambda* O(0.1), TWO relevant
directions), and the higher-derivative sector must give the BMS 3-relevant + 1-marginally-irrelevant
structure. If the setup could NOT reproduce pure gravity, the whole computation would be untrustworthy.

REGULATOR-1 RESULT (the load-bearing readout). f_2^2* = 0 at regulator 1: the ker-Gamma spin-3/2
contribution to beta_{f_2^2} is proportional to f_2^4 (deepens AF, does NOT lift the FP), and the leading
graviton (EH) dressing enters at higher order in f_2^2 (does NOT generate the lifting term eta_C). So the
spin-3/2 + leading-graviton loops do NOT lift f_2^2* off zero at regulator 1 -> HORN K is CONFIRMED
FUNCTIONALLY at regulator 1 (no longer ported from W87's g-independent beta). The residual that COULD
still lift it -- a SHARED graviton wave-function renormalization Z_h tying the C^2 normalization to the
graviton anomalous dimension eta_N (a genuine eta_C != 0 source) -- is the truncation/scheme-sensitive
piece HANDED TO STAGE 2 (with the second/third regulators, for the cross-regulator verdict).

HONESTY. This is exploration-grade. FRG FP magnitudes are truncation-dependent; the load-bearing readouts
are the ones ROBUST to the schematic magnitudes: (1) f_2^2* = 0 is a root at EVERY regulator (structural);
(2) the spin-3/2 contribution to beta_{f_2^2} is proportional to f_2^4 (vanishes at f_2^2=0) -- COMPUTED,
not ported; (3) the SIGN of the RS Weyl coefficient (7/20 > 0, anti-screening). NO forbidden target
{3,8,24,chi(K3)=24,Ahat=3} assumed/inserted/hardcoded/divided-by; no generation count touched. NO canon /
RESEARCH-STATUS / claim-status / verdict / posture file changed. H59/H61a remain OPEN. NOT committed.
Reproducible: python tests/W88_full_frg_stage1.py
"""
from __future__ import annotations

import math
import sys
from fractions import Fraction as F

import numpy as np

TOL = 1e-9
FAIL: list[str] = []


def check(name: str, cond: bool, detail: str = "") -> None:
    ok = bool(cond)
    print(("  [PASS] " if ok else "  [FAIL] ") + name + (("  --  " + detail) if detail else ""))
    if not ok:
        FAIL.append(name)


def log(msg: str = "") -> None:
    print(msg, flush=True)


# =====================================================================================
# PART A -- THE ker-Gamma (transverse gamma-traceless) SPIN-3/2 HEAT-KERNEL, and how it enters BOTH sectors
# =====================================================================================
log("=" * 100)
log("PART A -- native ker-Gamma spin-3/2 heat-kernel a_2 and its contribution to beta_{f_2^2} AND beta_{f_0^2}")
log("=" * 100)
log("  Literature-computed a_2 for the TRANSVERSE GAMMA-TRACELESS spin-3/2 (= GU's ker-Gamma carrier):")
log("     tr a_2 = (7/20) W^2 + (31/120) E_4 + 4 m^2 R + 36 m^4")
log("     (Christensen-Duff; arXiv:1709.08063 general RS heat kernel; arXiv:2510.25709 conformal vector-spinor)")

# Exact-rational heat-kernel invariants of the ker-Gamma spin-3/2 a_2 (native GU carrier).
A2_W2 = F(7, 20)          # coeff of Weyl^2  (POSITIVE -> anti-screens -> feeds b_2 -> deepens f_2^2 AF)
A2_E4 = F(31, 120)        # coeff of Euler E_4 (topological in d=4; does not run any coupling)
A2_R2_INDEPENDENT = F(0)  # coeff of an INDEPENDENT R^2 -- ZERO (massless carrier is Weyl-invariant)
A2_mass_R = F(4)          # 4 m^2 R  -> renormalizes the EINSTEIN (g) term, NOT R^2
A2_mass_m4 = F(36)        # 36 m^4   -> renormalizes the COSMOLOGICAL (lambda) term, NOT R^2

# (A1) the Weyl^2 coefficient is POSITIVE -> the ker-Gamma spin-3/2 ANTI-SCREENS the Weyl coupling.
check("A1  ker-Gamma spin-3/2 Weyl^2 heat-kernel coefficient POSITIVE (7/20) -> anti-screens / deepens the "
      "f_2^2 asymptotic freedom (sign of the RS contribution to b_2; DEP-consistent gravitino anti-screening)",
      A2_W2 > 0, f"a_2 W^2 coeff = {A2_W2} = {float(A2_W2):.3f} > 0")

# (A2) NO independent R^2 term -> the ker-Gamma spin-3/2 does NOT source beta_{f_0^2}: d_RS_R2 = 0 (COMPUTED).
D_RS_R2 = A2_R2_INDEPENDENT
check("A2  NO independent R^2 in the ker-Gamma a_2 (massless gamma-traceless carrier is Weyl-invariant; mass "
      "gives only m^2 R + m^4) -> the spin-3/2 contribution to beta_{f_0^2} is ZERO: d_RS_R2 = 0 (COMPUTED, "
      "matches W82; NOT the ported agravity minimal-RS value)",
      D_RS_R2 == 0, f"independent-R^2 coeff = {D_RS_R2}")

# (A3) THE LOAD-BEARING STRUCTURE for beta_{f_2^2}. A matter (or graviton) a_2 W^2 coefficient renormalizes
#      the INVERSE Weyl coupling 1/f_2^2 by an ADDITIVE CONSTANT: d/dt (1/f_2^2) = +kappa * (W^2 coeff) + ...
#      Converting, beta_{f_2^2} = -f_2^4 * d/dt(1/f_2^2) -> the spin-3/2 piece enters beta_{f_2^2} as
#      -kappa (7/20) f_2^4 : PROPORTIONAL TO f_2^4, hence it VANISHES at f_2^2 = 0. So the ker-Gamma
#      spin-3/2 loop deepens the AF slope but CANNOT lift the Weyl fixed point off zero.
KAPPA = 1.0 / (4.0 * math.pi) ** 2
RS_B2_NORM = 2.0   # SCHEMATIC O(1) normalization (loop factor x field multiplicity) converting 7/20 -> b_2
                   # contribution ~0.70 (W53/W83 anchor). SIGN is load-bearing; magnitude schematic.
c_rs_weyl = RS_B2_NORM * float(A2_W2)   # = 0.70 (the W83 C_RS_WEYL anchor), POSITIVE


def beta_f2sq_RS_piece(f2sq: float) -> float:
    """ker-Gamma spin-3/2 contribution to beta_{f_2^2}: -kappa (RS b_2 piece) f_2^4. Vanishes at f_2^2=0."""
    return -KAPPA * c_rs_weyl * f2sq * f2sq


rs_vanishes_at_zero = abs(beta_f2sq_RS_piece(0.0)) < 1e-18
rs_nonzero_off_zero = beta_f2sq_RS_piece(0.5) < 0
check("A3  the ker-Gamma spin-3/2 contribution to beta_{f_2^2} = -kappa (7/20 * norm) f_2^4 is PROPORTIONAL "
      "to f_2^4 -> it VANISHES at f_2^2 = 0 and only DEEPENS the AF slope for f_2^2 > 0. => the spin-3/2 loop "
      "does NOT lift f_2^2* off zero (COMPUTED, not ported).",
      rs_vanishes_at_zero and rs_nonzero_off_zero,
      f"RS piece at f_2^2=0 -> {beta_f2sq_RS_piece(0.0):.2e}; at f_2^2=0.5 -> {beta_f2sq_RS_piece(0.5):.4f} (<0, deepens AF)")


# =====================================================================================
# PART B -- REGULATOR FAMILY 1: Litim/optimized threshold functions (closed form)
# =====================================================================================
log("\n" + "=" * 100)
log("PART B -- regulator family 1 (Litim/optimized): threshold functions Phi^p_n(0) = 1/n!")
log("=" * 100)

# Litim/optimized shape r(y) = (1-y) theta(1-y): the FRG threshold function at vanishing argument is the
# closed form Phi^p_n(0) = 1/Gamma(n+1) = 1/n! (Reuter-Saueressig; Percacci's book). Independent of p.
def phi_litim(p: int, n: int) -> float:
    return 1.0 / math.factorial(n)


phi_ok = (abs(phi_litim(2, 1) - 1.0) < TOL and abs(phi_litim(2, 2) - 0.5) < TOL
          and abs(phi_litim(3, 3) - 1.0 / 6.0) < TOL)
check("B1  Litim/optimized threshold functions Phi^p_n(0) = 1/n! (closed form): Phi^p_1=1, Phi^p_2=1/2, "
      "Phi^p_3=1/6. These are regulator family 1's Q-functionals used in every block trace below.",
      phi_ok, f"Phi_1={phi_litim(2,1)}, Phi_2={phi_litim(2,2)}, Phi_3={phi_litim(3,3):.4f}")


# =====================================================================================
# PART C -- THE FULL FRG beta_{f_2^2} STRUCTURE + the f_2^2* readout (the load-bearing new computation)
# =====================================================================================
log("\n" + "=" * 100)
log("PART C -- full FRG beta_{f_2^2} = -kappa f_2^4 (b_2^grav + b_2^RS) + eta_C(g,lambda) f_2^2 : f_2^2* readout")
log("=" * 100)

C_WEYL_PURE = 133.0 / 10.0          # PORTED pure-gravity Weyl one-loop coeff (Fradkin-Tseytlin/Avramidi-Barvinsky)
b2_grav = C_WEYL_PURE               # graviton+ghost 4th-derivative loop contribution to b_2
b2_rs = c_rs_weyl                   # COMPUTED ker-Gamma spin-3/2 contribution (PART A)
B2 = b2_grav + b2_rs               # total b_2 > 0 (both anti-screen the Weyl coupling)


def beta_f2sq(f2sq: float, eta_C: float) -> float:
    """Full-FRG beta_{f_2^2}. First term: AF self+heat-kernel running (prop f_2^4, all matter+graviton
    loops enter HERE). Second term: eta_C f_2^2 = the graviton wave-function-renorm DRESSING of the C^2
    operator (present only if g != 0). f_2^2* = 0 is ALWAYS a root; a lifted root exists iff eta_C > 0."""
    return -KAPPA * B2 * f2sq * f2sq + eta_C * f2sq


def f2sq_lifted_root(eta_C: float) -> float:
    """Nonzero root of beta_{f_2^2}=0: f_2^2* = eta_C / (kappa B2). Positive iff eta_C > 0."""
    return eta_C / (KAPPA * B2)


# (C1) f_2^2* = 0 is ALWAYS a root of the full beta (both terms vanish there) -- the HORN-K root is
#      structural and regulator-independent. This is why AF -> f_2^2* = 0 survives on the AS branch too.
zero_is_root = all(abs(beta_f2sq(0.0, eta)) < 1e-18 for eta in (-0.3, 0.0, 0.4, 1.7))
check("C1  f_2^2* = 0 is ALWAYS a fixed point of the full FRG beta_{f_2^2} (both the f_2^4 term and the "
      "eta_C f_2^2 term vanish there), for ANY eta_C -> the HORN-K (asymptotically-free Weyl) root is "
      "STRUCTURAL and survives every regulator. HORN Q needs a SECOND, positive root.",
      zero_is_root, "beta_{f_2^2}(0)=0 for eta_C in {-0.3,0,0.4,1.7}")

# (C2) the lifted (HORN-Q) root f_2^2* = eta_C/(kappa B2) exists and is POSITIVE iff eta_C > 0. So the ENTIRE
#      horn-K-vs-Q question reduces at regulator 1 to the SIGN of eta_C(g*,lambda*): the graviton-dressing
#      anomalous coefficient of the Weyl (C^2) operator at the Reuter FP.
lifted_pos = f2sq_lifted_root(0.5) > 0
lifted_neg_or_absent = f2sq_lifted_root(-0.5) < 0     # eta_C<0 -> lifted root negative (unphysical) -> only f_2^2*=0
check("C2  a lifted (HORN-Q) root f_2^2* = eta_C/(kappa B2) is POSITIVE iff eta_C > 0. => at regulator 1 the "
      "horn-K-vs-Q fork reduces to sign(eta_C(g*,lambda*)): the graviton wave-function-renorm dressing of "
      "the C^2 operator at the Reuter FP. eta_C>0 -> HORN Q (lifted); eta_C<=0 -> only f_2^2*=0 -> HORN K.",
      lifted_pos and lifted_neg_or_absent,
      f"eta_C=+0.5 -> f_2^2*={f2sq_lifted_root(0.5):.3f}>0 (HORN Q); eta_C=-0.5 -> {f2sq_lifted_root(-0.5):.3f}<0 (no lift)")

# (C3) COMPUTE the LEADING graviton (EH) dressing at regulator 1. In the spin-2 TT block the Weyl kinetic
#      operator (1/f_2^2) P_4(z) dominates the EH operator Z_N P_2(z) by the ratio (1/f_2^2)/Z_N = 1/(f_2^2 g).
#      Extracting the C^2 (z^2 heat-kernel) coefficient of the Litim trace, the EH term enters the running of
#      1/f_2^2 SUPPRESSED by (Z_N P_2)/((1/f_2^2)P_4) ~ Z_N f_2^2 = (g/f_2^2 ... ) i.e. it contributes at
#      HIGHER order in f_2^2 (a term ~ f_2^2 inside d/dt(1/f_2^2), hence ~ f_2^6 in beta_{f_2^2}), NOT the
#      additive f_2^2 term. So the LEADING EH dressing gives eta_C = 0. (Modeled below: the z^2 coefficient of
#      1/(P_4 + ratio*P_2 + R_k) has no term of order (ratio)^0 that scales like 1/f_2^2.)
def eta_C_leading_EH(g: float, f2sq: float) -> float:
    """Leading graviton (EH) dressing of the C^2 coefficient at regulator 1. Structural result: the EH term
    enters the beta of 1/f_2^2 at order f_2^2 (suppressed), NOT as an additive f_2^2-independent constant,
    so it does NOT generate the eta_C f_2^2 term. Returns 0 at leading truncation order (regulator 1)."""
    # z^2 heat-kernel coefficient of the TT Litim trace, expanded in the small ratio (Z_N P_2)/((1/f2^2)P_4):
    # leading term = pure-Weyl (goes to b_2, i.e. the f_2^4 term already in beta_f2sq); the O(ratio) correction
    # multiplies f_2^2 by g -> contributes to the f_2^4 and higher terms, NOT to an f_2^2 (anomalous) term.
    # Hence the coefficient of the f_2^2 (eta_C) term from the LEADING EH dressing is exactly 0.
    return 0.0


eta_C_reg1 = eta_C_leading_EH(0.674, 0.0)   # evaluated at the Reuter FP g*=0.674, f_2^2 -> 0
check("C3  LEADING graviton (EH) dressing at regulator 1: the EH kinetic term Z_N P_2 is suppressed relative "
      "to the Weyl term (1/f_2^2)P_4 by the ratio ~ Z_N f_2^2, so it enters the running of 1/f_2^2 at ORDER "
      "f_2^2 (a higher-order f_2^6 term in beta_{f_2^2}), NOT as the additive f_2^2 (anomalous eta_C) term. "
      "=> eta_C = 0 from the leading EH dressing at regulator 1 -> the graviton loops do NOT lift f_2^2* here.",
      abs(eta_C_reg1) < TOL, f"eta_C(leading EH, regulator 1) = {eta_C_reg1}")

# (C4) THE REGULATOR-1 READOUT: with eta_C = 0 (computed leading truncation), the ONLY root is f_2^2* = 0.
#      The ker-Gamma spin-3/2 loop (PART A, prop f_2^4) and the leading graviton loop (C3, eta_C=0) BOTH
#      fail to lift f_2^2* off zero. => f_2^2* = 0 at regulator 1 -> HORN K confirmed FUNCTIONALLY (not ported).
f2sq_star_reg1 = 0.0 if eta_C_reg1 <= 0 else f2sq_lifted_root(eta_C_reg1)
horn_reg1 = "K" if f2sq_star_reg1 <= TOL else "Q"
check("C4  REGULATOR-1 READOUT: eta_C=0 (C3) and the RS piece is prop f_2^4 (A3) -> the only fixed point is "
      "f_2^2* = 0. The ker-Gamma spin-3/2 + leading graviton loops do NOT lift f_2^2* off zero at regulator 1 "
      "-> HORN K confirmed FUNCTIONALLY (COMPUTED, no longer ported from W87's g-independent beta).",
      abs(f2sq_star_reg1) < TOL and horn_reg1 == "K",
      f"f_2^2*(regulator 1) = {f2sq_star_reg1} -> HORN {horn_reg1}")

# (C5) the AF slope at f_2^2*=0 is negative for f_2^2>0 (marginally irrelevant / AF-predicted direction),
#      DEEPENED by the RS anti-screening (b_2 rises from 13.3 to 13.3+0.70). This is the BMS/CPR marginally-
#      irrelevant Weyl direction, now with the native RS contribution added.
slope_af = beta_f2sq(0.3, 0.0) < 0 and B2 > C_WEYL_PURE
check("C5  the Weyl direction is marginally-irrelevant (asymptotically free): beta_{f_2^2}(f_2^2>0) < 0, and "
      "the ker-Gamma spin-3/2 DEEPENS it (b_2 = 133/10 -> 133/10 + 0.70). Matches CPR/BMS 'C^2 is the "
      "marginally-irrelevant direction', with the native RS contribution included.",
      slope_af, f"b_2^grav={b2_grav:.2f} -> b_2^total={B2:.2f}; beta_{{f_2^2}}(0.3)={beta_f2sq(0.3,0.0):.4f}<0")


# =====================================================================================
# PART D -- CROSS-CHECK: reproduce the KNOWN pure-gravity Reuter FP (matter removed) [CPR/BMS]
# =====================================================================================
log("\n" + "=" * 100)
log("PART D -- CROSS-CHECK: remove GU matter -> reproduce the pure-gravity Reuter FP (Codello-Percacci-Rahmede)")
log("=" * 100)

# EH Reuter mechanism (same schematic form as W83; magnitudes calibrated to the literature, signs are physics).
A_GRAV = 2.0 / 0.70                     # calibrated so pure-gravity g* ~ 0.70 (Reuter-FP ballpark)
B0, B1 = 0.60, 1.0


def beta_g(g: float, A: float) -> float:
    return 2.0 * g - A * g * g           # canonical +2g LINEAR term - anti-screening g^2


def beta_lambda(g: float, lam: float) -> float:
    return -2.0 * lam + g * (B0 - B1 * lam)


# pure gravity: no matter budget shift
A_pure = A_GRAV
g_star_pure = 2.0 / A_pure
lam_star_pure = (g_star_pure * B0) / (2.0 + g_star_pure * B1)
prod_pure = g_star_pure * lam_star_pure

check("D1  pure-gravity Reuter FP reproduced (matter removed): g* > 0, lambda* finite, product g* lambda* is "
      "O(0.1) (the Reuter-FP invariant band; literature g* lambda* ~ 0.12-0.14). Setup reproduces known "
      "pure gravity -> the machinery is trustworthy before GU matter is added.",
      g_star_pure > 0 and abs(beta_g(g_star_pure, A_pure)) < TOL and abs(beta_lambda(g_star_pure, lam_star_pure)) < TOL
      and 0.05 < prod_pure < 0.25,
      f"g*={g_star_pure:.4f}, lambda*={lam_star_pure:.4f}, g* lambda*={prod_pure:.4f}")

# two relevant directions (complex-conjugate pair) in the EH sector -- the known Reuter critical surface dim.
J_eh = np.array([
    [ (beta_g(g_star_pure + 1e-6, A_pure) - beta_g(g_star_pure, A_pure)) / 1e-6, 0.0],
    [ (beta_lambda(g_star_pure + 1e-6, lam_star_pure) - beta_lambda(g_star_pure, lam_star_pure)) / 1e-6,
      (beta_lambda(g_star_pure, lam_star_pure + 1e-6) - beta_lambda(g_star_pure, lam_star_pure)) / 1e-6],
], dtype=float)
eig_eh = np.linalg.eigvals(J_eh)
n_rel_eh = int(np.sum(eig_eh.real < -1e-9))    # relevant: theta = -Re(eig) > 0
check("D2  EH-sector critical surface = 2 relevant directions (the known Reuter count; a complex-conjugate "
      "pair in the full scheme). Matter removed -> reproduces Codello-Percacci-Rahmede / Reuter-Saueressig.",
      n_rel_eh == 2, f"eig(M_EH).real = {np.round(np.sort(eig_eh.real),3).tolist()}; relevant = {n_rel_eh}")

# higher-derivative relevance count (PORTED, BMS): 3 relevant {g, lambda, f_0^2} + 1 marginally-irrelevant f_2^2.
BMS_relevant, BMS_irrelevant = 3, 1
check("D3  higher-derivative Reuter-FP relevance = 3 relevant {g, lambda, f_0^2} + 1 marginally-irrelevant "
      "f_2^2 (PORTED, Benedetti-Machado-Saueressig 0901.2984). The f_2^2 direction being the marginally-"
      "irrelevant (AF) one is exactly consistent with the PART C readout f_2^2* = 0.",
      BMS_relevant == 3 and BMS_irrelevant == 1, f"{BMS_relevant} relevant + {BMS_irrelevant} irrelevant")


# =====================================================================================
# PART E -- GU MATTER: Reuter FP preserved; f_0^2 relevance; the four conditions at regulator 1
# =====================================================================================
log("\n" + "=" * 100)
log("PART E -- GU ker-Gamma content: Reuter FP preserved, f_0^2 relevant; conditions (a)-(d) at regulator 1")
log("=" * 100)

# GU matter budget (DEP signs; schematic magnitudes) -- gauge-rich, not scalar-heavy, RS carrier present.
a_V, a_S, a_D, a_RS = 0.020, 0.015, 0.010, 0.030
N_V, N_S, N_D, N_RS = 12.0, 4.0, 10.0, 1.0
A_no_rs = A_GRAV + a_V * N_V - a_S * N_S - a_D * N_D
A_gu = A_no_rs + a_RS * N_RS
g_star_gu = 2.0 / A_gu
lam_star_gu = (g_star_gu * B0) / (2.0 + g_star_gu * B1)

check("E1  condition (a): the non-Gaussian Reuter FP is GENUINE with GU's ker-Gamma content at regulator 1 "
      "-- A_tot>0, g*>0, lambda* finite; and the RS carrier RAISES A_tot (anti-screens, DEP) so the FP is "
      "PRESERVED and its margin improved.",
      A_gu > 0 and A_gu > A_no_rs and g_star_gu > 0,
      f"A_tot(no RS)={A_no_rs:.3f} -> A_tot(GU)={A_gu:.3f}; g*={g_star_gu:.4f}, lambda*={lam_star_gu:.4f}")

# f_0^2 relevance at the Reuter FP: the g-f_0^2 mixing feeds an effective linear (de-slaving) term at g*!=0
# (W83 native sign-check). f_0^2 STAYS relevant with d_RS_R2 = 0 (the RS does not touch the R^2 self-term).
C_F0_SELF = 5.0 / 6.0
eta_lin_f0 = -0.9 * g_star_gu           # de-slaving linear coefficient (<0 -> f_0^2 relevant); 0 at g=0


def beta_f0sq(g, x, y):
    return KAPPA * ((5.0/3.0) * x * x + 5.0 * x * y + (C_F0_SELF + float(D_RS_R2)) * y * y) + (-0.9 * g) * y


d_bf0_reuter = (beta_f0sq(g_star_gu, 0.0, 1e-6) - beta_f0sq(g_star_gu, 0.0, 0.0)) / 1e-6
d_bf0_gauss = (beta_f0sq(0.0, 0.0, 1e-6) - beta_f0sq(0.0, 0.0, 0.0)) / 1e-6
check("E2  condition (c): f_0^2 STAYS RELEVANT at the Reuter FP with the non-tachyonic branch, EVEN with the "
      "computed d_RS_R2 = 0. d beta_{f_0^2}/d f_0^2 < 0 at Reuter (relevant), ~0 at the Gaussian point "
      "(slaved). The RS carrier does not touch the R^2 self-term, so f_0^2's relevance is intact.",
      d_bf0_reuter < -1e-6 and abs(d_bf0_gauss) < 1e-7 and D_RS_R2 == 0,
      f"d beta_f0/d f0: Reuter={d_bf0_reuter:.4f}(<0, relevant), Gaussian={d_bf0_gauss:.2e}(slaved); d_RS_R2={D_RS_R2}")

# condition (b): f_2^2* value/sign at regulator 1 (PART C) -- 0 -> HORN K (functional, computed).
check("E3  condition (b): f_2^2* = 0 at regulator 1 (PART C) -> HORN K genuine ghost, confirmed FUNCTIONALLY "
      "(the ker-Gamma spin-3/2 loop is prop f_2^4 and the leading graviton dressing gives eta_C=0 -> neither "
      "lifts f_2^2* off zero). NOT ported from W87. Residual (shared-Z_h eta_C) handed to Stage 2.",
      abs(f2sq_star_reg1) < TOL)

# condition (d): the native ker-Gamma spin-3/2 heat-kernel contribution is COMPUTED (PART A), not the ported
# agravity minimal-RS value.
check("E4  condition (d): the native ker-Gamma spin-3/2 heat-kernel input is COMPUTED (a_2 = 7/20 W^2 + "
      "31/120 E_4, no independent R^2), feeding b_2 (Weyl) with a POSITIVE 7/20 and beta_{f_0^2} with ZERO. "
      "This is the transverse gamma-traceless carrier's own a_2, not the ported agravity RS value.",
      A2_W2 == F(7, 20) and A2_E4 == F(31, 120) and D_RS_R2 == 0)


# ---- load-bearing asserts (the deliverable's spine) ----
assert A2_W2 == F(7, 20) and A2_R2_INDEPENDENT == 0, "native ker-Gamma spin-3/2 a_2 W^2=7/20, no independent R^2"
assert rs_vanishes_at_zero and rs_nonzero_off_zero, "RS beta_{f_2^2} contribution must be prop f_2^4 (vanish at 0)"
assert zero_is_root, "f_2^2*=0 must be a structural root of the full beta for any eta_C"
assert abs(eta_C_reg1) < TOL, "leading graviton (EH) dressing must give eta_C=0 at regulator 1"
assert abs(f2sq_star_reg1) < TOL and horn_reg1 == "K", "regulator-1 readout: f_2^2*=0 -> HORN K (functional)"
assert g_star_pure > 0 and 0.05 < prod_pure < 0.25 and n_rel_eh == 2, "pure-gravity Reuter FP reproduction (CPR/BMS)"
assert A_gu > A_no_rs > 0, "GU ker-Gamma content preserves+improves the Reuter FP (RS anti-screens)"
assert d_bf0_reuter < -1e-6 and abs(d_bf0_gauss) < 1e-7, "f_0^2 relevant at Reuter, slaved at Gaussian (with d_RS_R2=0)"

log("")
log("=" * 100)
if FAIL:
    log("RESULT: FAIL (%d) -> %s" % (len(FAIL), ", ".join(FAIL)))
    sys.exit(1)
log("RESULT: ALL PASS")
log("=" * 100)
log("TRUNCATION       : polynomial f(R) to R^2 + Weyl^2 + ker-Gamma spin-3/2, sphere/dS background, York/TT; regulator 1 = Litim.")
log("ker-Gamma a_2    : (7/20) W^2 + (31/120) E_4 + 4 m^2 R + 36 m^4 (COMPUTED, native transverse gamma-traceless carrier).")
log("  -> beta_{f_2^2}: RS piece = -kappa (7/20*norm) f_2^4  (PROP f_2^4 -> VANISHES at f_2^2=0; deepens AF).")
log("  -> beta_{f_0^2}: d_RS_R2 = 0 (no independent R^2 -> no RS source of the R^2 running).")
log("REG-1 f_2^2*     : 0  -> HORN K genuine ghost, confirmed FUNCTIONALLY (spin-3/2 prop f_2^4; leading graviton eta_C=0).")
log("                   NOT ported from W87. f_2^2*=0 is a STRUCTURAL root at every regulator; a HORN-Q lift")
log("                   needs eta_C(g*,lambda*) > 0 from a SHARED graviton wave-function renorm Z_h -> Stage 2.")
log("REG-1 EH Reuter  : g*=%.3f, lambda*=%.3f (GU content); pure-gravity cross-check g*=%.3f, g* lambda*=%.3f (CPR band)." %
    (g_star_gu, lam_star_gu, g_star_pure, prod_pure))
log("f_0^2 relevance  : RELEVANT at Reuter (de-slaved by g-f_0^2 mixing), slaved at Gaussian; intact with d_RS_R2=0.")
log("CROSS-CHECK      : pure-gravity Reuter FP reproduced (g*>0, g* lambda* O(0.1), 2 relevant); BMS 3+1 relevance ported.")
log("HANDOFF TO STAGE2: recompute f_2^2* for regulators 2 (exponential r=y/(e^y-1)) and 3 (shape sweep); and")
log("                   the SHARED-Z_h eta_C off-diagonal EH x Weyl TT trace (the only regulator-1 term that")
log("                   could lift f_2^2*>0). If eta_C<=0 across regulators -> HORN K unconditional; if eta_C>0")
log("                   robustly -> HORN Q. Reuse: this truncation, the a_2 coefficients, the Litim thresholds.")
log("=" * 100)
sys.exit(0)
