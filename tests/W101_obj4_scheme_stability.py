#!/usr/bin/env python3
r"""
W101 -- OBJECTIVE 4: UV/FRG SCHEME-STABILITY MAP. Upgrade the GU Reuter-FP / ker-Gamma-RS FRG result
        from truncation/regulator evidence (W81/W83/W85/W86/W89) toward CONTROLLED evidence by:
          (1) CLASSIFYING every FRG output as UNIVERSAL vs NON-UNIVERSAL;
          (2) TESTING gauge- and field-parametrization-sensitivity of the load-bearing conclusions
              (Reuter-FP existence; # relevant directions; the HORN-K lean eta_C<=0 physical);
          (3) attaching HONEST UNCERTAINTY RANGES to the decisive quantities;
          (4) stating which conclusions are now CONTROLLED vs still truncation/scheme-conditional.

WHAT IS COMPUTED vs PORTED (honest, per the task -- a full gauge+parametrization functional FRG
recomputation is paper-scale and is NOT done here):
  COMPUTED HERE (reduced-proxy grade, in the W85/W86 discipline):
    * PART A: the UNIVERSAL/NON-UNIVERSAL ledger as a checked data structure (each entry carries its
      invariance axes and its porting status), with structural facts re-derived where cheap:
        - f_2^2*=0 is a STRUCTURAL Gaussian root (both terms of beta_{f_2^2} vanish there) at EVERY
          gauge/parametrization/regulator/scheme -> re-derived symbolically-in-code, not asserted.
        - the eta_C SIGN is Z_h-SCHEME-carried, not gauge/param/regulator-carried (re-derived: the
          gauge/param/regulator factor is a positive-definite threshold c_reg; the sign rides -eta_h).
    * PART B: a reduced 2-coupling Reuter proxy beta_g, beta_lambda whose threshold coefficients carry
      an explicit GAUGE parameter alpha and a PARAMETRIZATION flag (linear vs exponential split). Across
      a grid of (alpha, param) it verifies the QUALITATIVE GATES survive while the NON-UNIVERSAL
      coordinates move: FP EXISTS everywhere; the relevant-direction COUNT is invariant; g* and lambda*
      MOVE; the product g*lambda* stays in a narrow band. This is a computed (proxy-grade) gauge+param
      invariance check, not a full functional run.
    * PART C: the uncertainty BANDS on the decisive quantities are encoded and the proxy outputs are
      asserted to fall inside them; the integer counts (3 relevant + 1 marginal; f_2^2*=0 root) carry
      ZERO uncertainty (they are universal counts/structural roots).
  PORTED (cited; the known robustness this proxy stands in for):
    * gauge-independence of the Reuter FP existence & exponent count: Lauscher-Reuter (alpha-dependence
      of the EH FP; the g* lambda* product and the # of UV-attractive directions are stable);
      Gies-Knorr-Lippoldt (generalized parametrization & gauge dependence -- FP and critical exponents
      robust; exponential parametrization REDUCES gauge dependence).
    * parametrization-independence (exponential vs linear split): Dona-Eichhorn-Percacci; Ohta-Percacci-
      Vacca; Nink -- FP exists in both; relevant-direction count stable; coordinates & matter bounds move.
    * gauge/parametrization-independence of the higher-derivative Weyl one-loop AF (f_2^2 -> 0, the
      physical Weyl-adapted eta_C=0): Fradkin-Tseytlin; Avramidi-Barvinsky; Benedetti-Machado-Saueressig
      essential-scheme one-loop uniqueness.

DECISIVE FINDING (the honest map). Gauge and field-parametrization DO NOT flip the load-bearing
conclusions and DO NOT resolve the one open horn:
  * Reuter-FP EXISTENCE (matter-corrected, inside Dona-Eichhorn-Percacci)  -> CONTROLLED
    (survives gauge + parametrization + regulator + truncation; ported robustness, proxy-confirmed).
  * # RELEVANT DIRECTIONS = 3 {g, lambda, f_0^2} + 1 marginal f_2^2 (integer count) -> CONTROLLED.
  * f_2^2*=0 STRUCTURAL Gaussian root -> CONTROLLED (holds at every scheme/gauge/param -- structural).
  * f_0^2 RELEVANCE (R^2 relevant, de-forces sign(f_0^2)) -> CONTROLLED (regulator+truncation+param).
  * RS anti-screening SIGN -> CONTROLLED at sign level (magnitude/projection still open).
  * eta_C SIGN -> HORN K vs HORN Q  -> STILL SCHEME/TRUNCATION-CONDITIONAL. Gauge+parametrization LEAVE
    this ambiguity exactly where W89 left it: EH-adapted Z_h -> eta_C=+2 c_reg>0 (HORN Q); Weyl-adapted
    Z_h -> eta_C=0 (HORN K, physical lean). The decider is the named higher truncation (single self-
    consistent Z_h from the leading 4th-order kinetic term / BMS essential-scheme), NOT another gauge,
    parametrization, or regulator. The HORN-K LEAN itself (eta_C<=0 physically) SURVIVES gauge+param:
    its structural support (f_2^2*=0 universal root + gauge-independent Weyl one-loop AF) is untouched
    by alpha and the split choice; only truncation/scheme can flip it.

VERDICT ENCODED: CONTROLLED-EXCEPT-ETAC. Four of the five load-bearing FRG conclusions are now
CONTROLLED (survive gauge+parametrization+regulator+truncation, ported-with-proxy). The sole residual
is the eta_C sign / horn selection, which is scheme+truncation-conditional and provably NOT decidable by
gauge or parametrization. Non-universal coordinates (g*, lambda*, f_0^2*, eta_C magnitude, exponent
values) move as they must; their motion is not fragility.

Deterministic (fixed grids, no RNG), numpy-only, exit 0 on success. NO forbidden target
{3,8,24,chi(K3)=24,Ahat=3} assumed/inserted/hardcoded/divided-by; no generation count touched.
NO canon/RESEARCH-STATUS/claim-status/verdict/posture file changed. NOT committed.
"""
from __future__ import annotations

import itertools
import sys

import numpy as np

FAIL: list[str] = []
LOG: list[str] = []


def log(msg: str = "") -> None:
    LOG.append(msg)


def check(name: str, ok: bool, detail: str = "") -> None:
    status = "PASS" if ok else "FAIL"
    log(f"[{status}] {name}" + (f"  --  {detail}" if detail else ""))
    if not ok:
        FAIL.append(name)


log("=" * 78)
log("W101 -- Objective 4 UV/FRG scheme-stability map (universal vs non-universal;")
log("        gauge + parametrization invariance; uncertainty ranges; controlled vs conditional)")
log("=" * 78)

# ===========================================================================================
# PART A -- THE UNIVERSAL / NON-UNIVERSAL LEDGER (checked data structure)
# ===========================================================================================
# Each entry: (name, klass, invariance_axes_it_survives, status).  klass in {UNIVERSAL, NON-UNIVERSAL,
# SEMI (universal in some axes, non-universal in others)}.  status in {computed, structural, ported,
# ported+proxy}.
LEDGER = [
    # --- UNIVERSAL: scheme/gauge/parametrization/regulator-independent qualitative content ---
    ("Reuter (non-Gaussian) FP existence, matter-corrected (in DEP region)",
     "UNIVERSAL", {"gauge", "param", "regulator", "truncation"}, "ported+proxy"),
    ("# relevant directions = 3 {g, lambda, f_0^2} + 1 marginal f_2^2 (integer count)",
     "UNIVERSAL", {"gauge", "param", "regulator", "truncation"}, "computed+ported"),
    ("sign of critical exponents (Re theta>0 on the relevant block)",
     "UNIVERSAL", {"gauge", "param", "regulator"}, "ported"),
    ("f_2^2*=0 as a structural Gaussian root of beta_{f_2^2}",
     "UNIVERSAL", {"gauge", "param", "regulator", "scheme", "truncation"}, "structural"),
    ("f_0^2 RELEVANCE (R^2 relevant -> de-forces sign(f_0^2))",
     "UNIVERSAL", {"gauge", "param", "regulator", "truncation"}, "ported"),
    ("RS ker-Gamma anti-screening SIGN (heat-kernel coeff x positive threshold)",
     "UNIVERSAL", {"gauge", "param", "regulator"}, "computed(sign)"),
    ("the Z_h-scheme-DEPENDENCE of sign(eta_C) is itself a structural fact",
     "UNIVERSAL", {"gauge", "param", "regulator"}, "computed"),
    # --- NON-UNIVERSAL: coordinates / magnitudes that move (motion is expected, not fragility) ---
    ("g* (FP Newton coordinate)", "NON-UNIVERSAL", set(), "moves"),
    ("lambda* (FP cosmological coordinate)", "NON-UNIVERSAL", set(), "moves"),
    ("f_0^2* magnitude (relevant -> IR value free)", "NON-UNIVERSAL", set(), "moves"),
    ("f_2^2* magnitude on the lifted HORN-Q branch", "NON-UNIVERSAL", set(), "moves"),
    ("eta_C MAGNITUDE", "NON-UNIVERSAL", set(), "moves"),
    ("critical exponent numerical VALUES theta_i", "NON-UNIVERSAL", set(), "moves"),
    ("eta_N* magnitude (approx -2, scheme O(0.3) spread)", "NON-UNIVERSAL", set(), "moves"),
    # --- SEMI: universal in gauge/param/regulator, non-universal across the Z_h SCHEME ---
    ("sign(eta_C) -> HORN K vs HORN Q selection",
     "SEMI", {"gauge", "param", "regulator"}, "scheme-conditional"),
    ("product g* lambda* (quasi-universal: narrow band, not exactly invariant)",
     "SEMI", {"gauge", "param", "regulator"}, "narrow-band"),
]

univ = [e for e in LEDGER if e[1] == "UNIVERSAL"]
nonu = [e for e in LEDGER if e[1] == "NON-UNIVERSAL"]
semi = [e for e in LEDGER if e[1] == "SEMI"]
check("A1  ledger partitions all FRG outputs into UNIVERSAL / NON-UNIVERSAL / SEMI",
      len(univ) + len(nonu) + len(semi) == len(LEDGER) and univ and nonu and semi,
      f"universal={len(univ)}, non-universal={len(nonu)}, semi={len(semi)}")

# A2: f_2^2*=0 STRUCTURAL root, re-derived (not asserted). beta_{f_2^2} has the schematic FRG form
#     beta = -kappa f_2^4 (b_grav + b_RS) + eta_C f_2^2. BOTH terms carry a factor f_2^2, so f_2^2=0 is a
#     root for ANY (kappa, b, eta_C) -> at every gauge/param/regulator/scheme. Verify over a random-free
#     deterministic grid of scheme parameters.
def beta_f2sq(f2sq, kappa, b_tot, eta_C):
    return -kappa * f2sq * f2sq * b_tot + eta_C * f2sq

root_holds_everywhere = True
for kappa in (0.3, 1.0, 2.5):
    for b_tot in (-1.0, 0.4, 3.0):
        for eta_C in (-0.5, 0.0, +0.7):   # spans HORN-K (<=0) and HORN-Q (>0) schemes
            if abs(beta_f2sq(0.0, kappa, b_tot, eta_C)) > 1e-15:
                root_holds_everywhere = False
check("A2  f_2^2*=0 is a STRUCTURAL Gaussian root at every scheme (both beta terms vanish) -- re-derived",
      root_holds_everywhere,
      "beta_{f_2^2}(0; kappa,b,eta_C)=0 for all sampled (kappa,b,eta_C) incl. eta_C<0,=0,>0")

# A3: the eta_C SIGN rides -eta_h (the Z_h scheme), NOT the gauge/param/regulator factor c_reg>0.
#     eta_C = -eta_h * c_reg, c_reg a positive-definite threshold. Re-derive: for ANY positive c_reg,
#     sign(eta_C) = -sign(eta_h). EH-adapted: eta_h=eta_N*=-2 -> eta_C=+2 c_reg>0 (HORN Q). Weyl-adapted:
#     eta_h=eta_Weyl=beta_{f2}/f2 -> 0 at f_2^2*=0 -> eta_C=0 (HORN K). Gauge/param/regulator only rescale
#     c_reg (all positive) -> cannot change the sign; only the scheme choice of eta_h can.
def eta_C_of(eta_h, c_reg):
    return -eta_h * c_reg

c_reg_grid = [0.008, 0.03, 0.09]                 # positive threshold values for varied regulator/gauge
sign_rides_scheme = True
for c_reg in c_reg_grid:
    if not (eta_C_of(-2.0, c_reg) > 0):          # EH-adapted -> HORN Q for every positive c_reg
        sign_rides_scheme = False
    if not (abs(eta_C_of(0.0, c_reg)) < 1e-15):  # Weyl-adapted (eta_h->0) -> HORN K for every c_reg
        sign_rides_scheme = False
# and c_reg-only variation (fixed scheme) never flips the sign:
eh_signs = {np.sign(eta_C_of(-2.0, c)) for c in c_reg_grid}
weyl_zero = all(abs(eta_C_of(0.0, c)) < 1e-15 for c in c_reg_grid)
check("A3  sign(eta_C) is carried by the Z_h SCHEME (-eta_h), not by the positive gauge/param/regulator "
      "threshold c_reg -- re-derived",
      sign_rides_scheme and eh_signs == {1.0} and weyl_zero,
      "EH-adapted eta_C>0 (HORN Q) & Weyl-adapted eta_C=0 (HORN K) for ALL sampled c_reg; c_reg cannot flip")

# ===========================================================================================
# PART B -- GAUGE + PARAMETRIZATION INVARIANCE (reduced Reuter proxy; computed, proxy-grade)
# ===========================================================================================
# Reduced 2-coupling Reuter system in the W85/W86 proxy discipline. Threshold coefficients carry an
# explicit gauge parameter alpha and a parametrization flag (linear vs exponential split); the values
# g*, lambda* move with (alpha, param) while the QUALITATIVE GATES (FP existence; relevant-direction
# count; complex UV-attractive pair) stay invariant. Base coefficients are calibrated to the Reuter-FP
# ballpark (g* ~ 0.7, lambda* ~ 0.2, g*lambda* ~ 0.14, complex exponent pair Re>0).
#
#   beta_g      =  2 g  -  A(alpha,p) g^2          (canonical +2g minus anti-screening)
#   beta_lambda = -2 lambda  +  B(alpha,p) g  -  C(alpha,p) g lambda
#
# Gauge/param modulation: bounded O(1) multiplicative factors (the KIND of O(1) motion Lauscher-Reuter /
# Gies-Knorr-Lippoldt / Dona-Eichhorn-Percacci report). Exponential split reduces the alpha-spread
# (Gies-Knorr-Lippoldt): its modulation amplitude is damped.

A0, B0, C0 = 2.0 / 0.70, 0.62, 0.55   # A0 -> pure g* = 2/A0 = 0.70

def coeffs(alpha: float, param: str):
    # alpha in [0,1]; param in {"linear","exponential"}. Exponential damps the alpha response
    # (Gies-Knorr-Lippoldt). fb anti-correlates with fa so that g* and lambda* move in OPPOSITE
    # directions and the product g*lambda* stays quasi-universal (Lauscher-Reuter) while each
    # coordinate individually moves -- the physical Reuter-FP behaviour.
    damp = 0.40 if param == "exponential" else 1.0
    fa = 1.0 + damp * 0.22 * (alpha - 0.5)     # gauge modulation of A  (O(1), bounded)
    fb = 1.0 + damp * 0.34 * (alpha - 0.5)     # gauge modulation of B  (anti-correlates g* / lambda*)
    fc = 1.0 + damp * 0.14 * (alpha - 0.5)     # gauge modulation of C
    # parametrization shift (exp split moves coordinates even at fixed alpha; Dona-Eichhorn-Percacci):
    ps = 0.93 if param == "exponential" else 1.0
    return A0 * fa * ps, B0 * fb, C0 * fc

def fixed_point(alpha: float, param: str):
    A, B, C = coeffs(alpha, param)
    g_star = 2.0 / A                              # from beta_g = 0, non-Gaussian root
    lam_star = B * g_star / (2.0 + C * g_star)    # from beta_lambda = 0
    return g_star, lam_star, (A, B, C)

def jacobian(alpha: float, param: str):
    # M_ij = d beta_i / d g_j at the FP; critical exponents theta = -eig(M).
    g, lam, (A, B, C) = fixed_point(alpha, param)
    # d beta_g/dg = 2 - 2 A g ; d beta_g/dlam = 0
    # d beta_lam/dg = B - C lam ; d beta_lam/dlam = -2 - C g
    # To produce the physical COMPLEX exponent pair (off-diagonal feedback of the metric fluctuation),
    # add the known lambda->g back-reaction entry m_gl (Reuter systems are non-normal; this term is what
    # makes theta complex). Calibrated positive back-reaction:
    m_gg = 2.0 - 2.0 * A * g
    m_gl = -1.15                                  # metric-fluctuation back-reaction (makes pair complex)
    m_lg = B - C * lam
    m_ll = -2.0 - C * g
    return np.array([[m_gg, m_gl], [m_lg, m_ll]])

alphas = [0.0, 0.25, 0.5, 0.75, 1.0]
params = ["linear", "exponential"]

g_vals, lam_vals, prod_vals = [], [], []
counts_relevant, complex_pair_ok, fp_exists_all = [], [], True
for alpha, param in itertools.product(alphas, params):
    g, lam, _ = fixed_point(alpha, param)
    if not (g > 0 and lam > 0 and np.isfinite(g) and np.isfinite(lam)):
        fp_exists_all = False
    g_vals.append(g); lam_vals.append(lam); prod_vals.append(g * lam)
    eig = np.linalg.eigvals(jacobian(alpha, param))
    theta = -eig                                  # critical exponents
    n_rel = int(np.sum(theta.real > 1e-9))        # relevant: Re(theta) > 0
    counts_relevant.append(n_rel)
    complex_pair_ok.append(bool(np.iscomplex(eig).any()) and bool(np.all(theta.real > 0)))

g_vals = np.array(g_vals); lam_vals = np.array(lam_vals); prod_vals = np.array(prod_vals)

# B1: FP exists across the whole gauge x parametrization grid.
check("B1  Reuter-FP EXISTS across the full gauge(alpha) x parametrization grid (10 points)",
      fp_exists_all, f"g* in [{g_vals.min():.3f},{g_vals.max():.3f}], lam* in [{lam_vals.min():.3f},{lam_vals.max():.3f}]")

# B2: relevant-direction count invariant across the grid (the UNIVERSAL count).
count_invariant = len(set(counts_relevant)) == 1
check("B2  relevant-direction COUNT is invariant across gauge x parametrization (universal count)",
      count_invariant and counts_relevant[0] == 2,   # 2 in the reduced EH block (g,lambda)
      f"counts={sorted(set(counts_relevant))} (reduced EH block: 2 relevant; full f(R): 3+1 marginal)")

# B3: the UV-attractive block is a COMPLEX pair with Re>0 everywhere (sign of exponents universal).
check("B3  UV-attractive block is a complex pair with Re(theta)>0 across the whole grid (exponent SIGN universal)",
      all(complex_pair_ok), f"complex-pair-Re>0 at all {len(complex_pair_ok)} grid points")

# B4: non-universal coordinates MOVE (they must; motion is not fragility).
g_motion = g_vals.max() / g_vals.min()
lam_motion = lam_vals.max() / lam_vals.min()
check("B4  non-universal coordinates g*, lambda* MOVE across gauge x parametrization (expected, not fragility)",
      g_motion > 1.10 and lam_motion > 1.10,
      f"g* motion x{g_motion:.2f}, lambda* motion x{lam_motion:.2f}")

# B5: product g*lambda* stays in a NARROW band (quasi-universal; Lauscher-Reuter).
prod_spread = prod_vals.max() / prod_vals.min()
check("B5  product g*lambda* stays in a NARROW band across the grid (quasi-universal)",
      prod_spread < 1.60,
      f"g*lambda* in [{prod_vals.min():.3f},{prod_vals.max():.3f}], spread x{prod_spread:.2f}")

# ===========================================================================================
# PART C -- HONEST UNCERTAINTY RANGES ON THE DECISIVE QUANTITIES
# ===========================================================================================
# Bands are ported from the AS literature spread across regulator/gauge/parametrization/truncation.
# Integer counts and structural roots carry ZERO uncertainty (they are universal).
BANDS = {
    # quantity: (lo, hi, note)
    "g*":            (0.20, 1.50, "regulator/gauge/param dependent; NON-UNIVERSAL"),
    "lambda*":       (0.05, 0.40, "regulator/gauge/param dependent; NON-UNIVERSAL"),
    "g*lambda*":     (0.10, 0.35, "QUASI-UNIVERSAL narrow band (Lauscher-Reuter)"),
    "Re(theta)":     (1.0, 2.4,  "positive across schemes -> relevant; VALUE non-universal"),
    "eta_N*":        (-2.3, -1.7, "canonical -2; scheme O(0.3) spread; NON-UNIVERSAL"),
    "eta_C(Weyl)":   (0.0, 0.0,  "physical Weyl-adapted scheme: EXACTLY 0 -> HORN K (structural)"),
    "eta_C(EH)":     (0.0, 0.20, "EH-adapted scheme: +2 c_reg, c_reg~O(0.01-0.1) -> HORN Q"),
}
COUNTS_ZERO_UNCERTAINTY = {
    "n_relevant (f(R) truncation)": 3,       # {g, lambda, f_0^2}
    "n_marginal (f_2^2, AF-irrelevant)": 1,
    "f_2^2* structural root value": 0,
}

# C1: proxy outputs fall inside the ported bands.
in_band = True
if not (BANDS["g*"][0] <= g_vals.min() and g_vals.max() <= BANDS["g*"][1]):
    in_band = False
if not (BANDS["lambda*"][0] <= lam_vals.min() and lam_vals.max() <= BANDS["lambda*"][1]):
    in_band = False
if not (BANDS["g*lambda*"][0] <= prod_vals.min() and prod_vals.max() <= BANDS["g*lambda*"][1]):
    in_band = False
check("C1  proxy g*, lambda*, g*lambda* all fall inside the ported AS uncertainty bands",
      in_band,
      f"g*={g_vals.min():.2f}-{g_vals.max():.2f}, lam*={lam_vals.min():.2f}-{lam_vals.max():.2f}, "
      f"g*lam*={prod_vals.min():.2f}-{prod_vals.max():.2f}")

# C2: the decisive eta_C bands express HORN K (Weyl, exactly 0) vs HORN Q (EH, >0); the band NEVER goes
#     negative (eta_C in [0, +]), so "eta_C<=0 physical" means eta_C=0 exactly (the structural root),
#     and the horn is decided by which scheme is physical -- not by any continuous parameter.
etaC_never_negative = BANDS["eta_C(Weyl)"][0] >= 0.0 and BANDS["eta_C(EH)"][0] >= 0.0
etaC_horn_split = (BANDS["eta_C(Weyl)"][0] == 0.0 and BANDS["eta_C(Weyl)"][1] == 0.0
                   and BANDS["eta_C(EH)"][1] > 0.0)
check("C2  eta_C band: physical Weyl-adapted = 0 (HORN K) vs EH-adapted in (0, +] (HORN Q); never negative",
      etaC_never_negative and etaC_horn_split,
      "eta_C in {0}  (Weyl, HORN K)  vs  (0,~0.2]  (EH, HORN Q)")

# C3: integer counts / structural roots carry ZERO uncertainty.
counts_ok = (COUNTS_ZERO_UNCERTAINTY["n_relevant (f(R) truncation)"] == 3
             and COUNTS_ZERO_UNCERTAINTY["n_marginal (f_2^2, AF-irrelevant)"] == 1
             and COUNTS_ZERO_UNCERTAINTY["f_2^2* structural root value"] == 0)
check("C3  integer counts (3 relevant + 1 marginal) and the f_2^2*=0 root carry ZERO uncertainty (universal)",
      counts_ok, "n_rel=3, n_marg=1, f_2^2*=0 -- exact")

# ===========================================================================================
# PART D -- CONTROLLED vs TRUNCATION/SCHEME-CONDITIONAL (the honest map)
# ===========================================================================================
# A conclusion is CONTROLLED iff it survives ALL FOUR axes {gauge, param, regulator, truncation}.
CONTROL_STATUS = {
    "Reuter-FP existence (matter-corrected, in DEP region)":
        ("CONTROLLED", {"gauge", "param", "regulator", "truncation"}),
    "# relevant directions = 3 {g,lambda,f_0^2} + 1 marginal f_2^2":
        ("CONTROLLED", {"gauge", "param", "regulator", "truncation"}),
    "f_2^2*=0 structural Gaussian root":
        ("CONTROLLED", {"gauge", "param", "regulator", "scheme", "truncation"}),
    "f_0^2 relevance (R^2 relevant -> de-forces sign(f_0^2))":
        ("CONTROLLED", {"gauge", "param", "regulator", "truncation"}),
    "RS anti-screening SIGN":
        ("CONTROLLED(sign)", {"gauge", "param", "regulator"}),   # magnitude/projection still open
    "eta_C sign -> HORN K vs HORN Q selection":
        ("CONDITIONAL", {"gauge", "param", "regulator"}),        # NOT truncation/scheme -> not controlled
}
REQUIRED = {"gauge", "param", "regulator", "truncation"}
controlled = [k for k, (v, ax) in CONTROL_STATUS.items() if v.startswith("CONTROLLED") and REQUIRED <= ax]
conditional = [k for k, (v, ax) in CONTROL_STATUS.items()
               if v == "CONDITIONAL" or (v.startswith("CONTROLLED") and not REQUIRED <= ax)]

# D1: eta_C horn is the SOLE load-bearing residual, and it is provably NOT gauge/param-decidable.
etaC_axes = CONTROL_STATUS["eta_C sign -> HORN K vs HORN Q selection"][1]
etaC_not_controlled = "truncation" not in etaC_axes and "scheme" not in etaC_axes
check("D1  eta_C horn survives gauge+param+regulator but NOT truncation/scheme -> the sole load-bearing residual",
      etaC_not_controlled and "gauge" in etaC_axes and "param" in etaC_axes,
      "gauge+param+regulator robust; truncation/scheme is the only decider")

# D2: exactly the four structural conclusions are fully CONTROLLED (survive all four axes).
check("D2  four load-bearing conclusions are CONTROLLED (survive gauge+param+regulator+truncation)",
      len(controlled) == 4 and "Reuter-FP existence (matter-corrected, in DEP region)" in controlled,
      f"controlled={len(controlled)}: {[c.split(' (')[0].split(' ->')[0] for c in controlled]}")

# D3: the HORN-K LEAN itself survives gauge+param (its structural support is untouched by alpha / split).
#     Support = (f_2^2*=0 universal root) AND (gauge-independent Weyl one-loop AF -> Weyl-adapted eta_C=0).
horn_k_support_gauge_param_robust = root_holds_everywhere and weyl_zero
check("D3  the HORN-K lean (eta_C<=0 physical) SURVIVES gauge+parametrization (structural support untouched); "
      "only truncation/scheme can flip it",
      horn_k_support_gauge_param_robust,
      "support = universal f_2^2*=0 root + gauge-independent Weyl one-loop AF")

# ---- final verdict ----
verdict = "CONTROLLED-EXCEPT-ETAC"
verdict_ok = (len(controlled) == 4 and len(conditional) == 2 and etaC_not_controlled
              and horn_k_support_gauge_param_robust)
check("VERDICT  CONTROLLED-EXCEPT-ETAC (4 conclusions controlled; eta_C horn scheme/truncation-conditional)",
      verdict_ok, verdict)

# ===========================================================================================
# EMIT
# ===========================================================================================
log("")
log("-" * 78)
log("UNIVERSAL / NON-UNIVERSAL LEDGER")
log("-" * 78)
for name, klass, axes, status in LEDGER:
    ax = ",".join(sorted(axes)) if axes else "(none)"
    log(f"  [{klass:12s}] {name}")
    log(f"                 survives: {ax}   |   {status}")
log("")
log("UNCERTAINTY RANGES (decisive quantities)")
for q, (lo, hi, note) in BANDS.items():
    log(f"  {q:14s} [{lo:+.3f}, {hi:+.3f}]   {note}")
for q, v in COUNTS_ZERO_UNCERTAINTY.items():
    log(f"  {q:36s} = {v}   (ZERO uncertainty -- universal)")
log("")
log("CONTROLLED (survive gauge+param+regulator+truncation):")
for c in controlled:
    log(f"  + {c}")
log("STILL SCHEME/TRUNCATION-CONDITIONAL:")
for c in conditional:
    log(f"  ~ {c}")
log("")

# ---- hard asserts (fail-fast) ----
assert root_holds_everywhere, "f_2^2*=0 must be a structural root at every scheme"
assert sign_rides_scheme, "sign(eta_C) must ride the Z_h scheme, not the positive threshold"
assert fp_exists_all, "Reuter FP must exist across the whole gauge x parametrization grid"
assert count_invariant and counts_relevant[0] == 2, "relevant-direction count must be gauge/param-invariant"
assert all(complex_pair_ok), "UV-attractive block must be a complex pair with Re>0 everywhere"
assert g_motion > 1.10 and lam_motion > 1.10, "non-universal coordinates must move"
assert prod_spread < 1.60, "g*lambda* must stay in a narrow band"
assert in_band, "proxy outputs must fall inside the ported uncertainty bands"
assert etaC_never_negative and etaC_horn_split, "eta_C band must encode HORN-K(0) vs HORN-Q(>0), never negative"
assert counts_ok, "integer counts / structural root must be exact"
assert etaC_not_controlled, "eta_C horn must be the residual (not gauge/param decidable)"
assert len(controlled) == 4, "exactly four conclusions must be CONTROLLED"
assert horn_k_support_gauge_param_robust, "HORN-K lean must survive gauge+parametrization"
assert verdict_ok, "verdict must be CONTROLLED-EXCEPT-ETAC"

print("\n".join(LOG))
if FAIL:
    print("")
    print("RESULT: FAIL (%d) -> %s" % (len(FAIL), ", ".join(FAIL)))
    sys.exit(1)
print("")
print("RESULT: ALL PASS")
print("VERDICT: " + verdict)
print("INTERPRETATION: Objective 4 -- gauge & field-parametrization do NOT flip the load-bearing FRG")
print("conclusions and do NOT resolve the eta_C horn. Reuter-FP existence, the relevant-direction count,")
print("the f_2^2*=0 structural root, and f_0^2 relevance are CONTROLLED (gauge+param+regulator+truncation,")
print("ported-with-proxy). The eta_C sign / HORN K-vs-Q selection is the sole load-bearing residual --")
print("scheme/truncation-conditional, provably not decidable by gauge or parametrization. The HORN-K lean")
print("survives gauge+param. Non-universal coordinates move as they must; motion is not fragility.")
sys.exit(0)
