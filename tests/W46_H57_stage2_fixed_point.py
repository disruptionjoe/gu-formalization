#!/usr/bin/env python3
r"""
W46 / H57 (Stage 2 of 2) -- FIXED POINT + CRITICAL SURFACE for the GU UV flow.

Consumes Stage 1's assembled beta system (tests/W45_H57_stage1_beta_system.py: BetaSystem,
THEORY_SPACE, STAGE2_HANDOFF) and SETTLES the fixed-point / predictivity questions:

  Q1  Is there a UV fixed point? Is the Gaussian point (0,0) one? Any NON-Gaussian (safety) FP?
  Q2  Critical-surface dimension = # UV-relevant directions = # free parameters. Which physical ones?
  Q3  Robustness: over what range of the named parameter c_RS_weyl does the AF verdict survive?
  Q4  How is the f_0 conformal-mode non-AF resolved (fixed-RATIO analysis)?
  Q5  Critical exponents (stability-matrix eigenvalues) at the FP.

CONSTRUCTION FORKS (GEOMETER-VS-PHYSICS-OBJECTS.md), carried from Stage 1, stated explicitly:
  (1) Gravity action: GU-native INDUCED |II|^2 -> 4th-order Stelle (f_2^2 Weyl, f_0^2 R^2). The
      fixed-point search lives on this truncation; it IS GU's spin-2 + conformal-mode sector.
  (2) RS sector: GU-native ker-Gamma-projected spin-3/2 -> the RS Weyl-beta shift c_RS_weyl is a
      NAMED PARAMETER (anchor 17/12), swept here for robustness (Q3).
  (4) mu_DW: ratio-only free scale. The dimensionful couplings ride the flow as RELEVANT directions;
      only the dimensionless ones hit a fixed point. mu_DW is realized as the Einstein/Newton
      transmutation scale -- one of the counted relevant directions.

OUT OF SCOPE (asserted as an explicit caveat, NOT settled here): Krein loop-POSITIVITY / [P,S]=0
  unitarity. A UV fixed point in the couplings is a statement about the RG FLOW and is INDEPENDENT of
  the separate positivity question. In particular the f_0 fixed-RATIO found below sits at
  f_0^2/f_2^2 < 0 -- whether that sign is admissible is exactly the (out-of-scope) positivity frontier.

VERDICT (this truncation): GU realizes asymptotic FREEDOM (Gaussian UV fixed point), NOT asymptotic
  SAFETY (no interacting fixed point at one loop / 2 couplings). Grade: PORTED + DERIVED-on-ported.

Reproducible: python tests/W46_H57_stage2_fixed_point.py   (exit 0 on PASS)
No git commit (orchestrator verifies+commits). No canon/verdict file touched. Exploration-grade.
"""
from __future__ import annotations
import contextlib
import importlib.util
import io
import math
import os
import sys

import numpy as np

TOL = 1e-9
results: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    results.append((name, bool(passed), detail))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))


def log(msg: str = "") -> None:
    print(msg, flush=True)


# =====================================================================================
# IMPORT STAGE 1 (reuse the betas; do NOT re-derive). The Stage-1 module runs top-level checks
# and ends in `raise SystemExit(0)`; load it via a spec, register in sys.modules (dataclass needs
# it), exec with stdout suppressed, and swallow the SystemExit. All objects are defined BEFORE the
# exit, so BetaSystem / THEORY_SPACE / STAGE2_HANDOFF / KAPPA are all available afterward.
# =====================================================================================
_HERE = os.path.dirname(os.path.abspath(__file__))
_STAGE1 = os.path.join(_HERE, "W45_H57_stage1_beta_system.py")
_spec = importlib.util.spec_from_file_location("W45_stage1", _STAGE1)
S1 = importlib.util.module_from_spec(_spec)
sys.modules["W45_stage1"] = S1
with contextlib.redirect_stdout(io.StringIO()):
    try:
        _spec.loader.exec_module(S1)
    except SystemExit:
        pass

BetaSystem = S1.BetaSystem
THEORY_SPACE = S1.THEORY_SPACE
STAGE2_HANDOFF = S1.STAGE2_HANDOFF

log("=" * 92)
log("W46 / H57 STAGE 2 -- FIXED POINT + CRITICAL SURFACE (consumes W45 Stage-1 beta system)")
log("=" * 92)
check("I1  Stage-1 beta system imported and reusable (BetaSystem, THEORY_SPACE, STAGE2_HANDOFF)",
      BetaSystem is not None and len(THEORY_SPACE) == 9 and "questions_for_stage2" in STAGE2_HANDOFF,
      f"{len(THEORY_SPACE)} couplings; anchor b_2 = {BetaSystem().b2():.5f}")


# =====================================================================================
# small dependency-light linear algebra helpers (2x2), plus a finite-difference Jacobian.
# =====================================================================================
def jacobian(bs: "BetaSystem", g: tuple[float, float], h: float = 1e-6) -> np.ndarray:
    """Stability matrix M_ij = d beta_i / d g_j via symmetric finite differences."""
    g = np.asarray(g, dtype=float)
    J = np.zeros((2, 2))
    for j in range(2):
        gp = g.copy(); gp[j] += h
        gm = g.copy(); gm[j] -= h
        bp = np.asarray(bs.beta(tuple(gp)))
        bm = np.asarray(bs.beta(tuple(gm)))
        J[:, j] = (bp - bm) / (2.0 * h)
    return J


def newton_2d(bs: "BetaSystem", g0, iters: int = 200):
    """Multistart Newton root-find for beta(g)=0. Returns converged g or None."""
    g = np.asarray(g0, dtype=float)
    for _ in range(iters):
        F = np.asarray(bs.beta(tuple(g)))
        if np.max(np.abs(F)) < 1e-14:
            return g
        J = jacobian(bs, tuple(g))
        # near the Gaussian point J -> 0 (marginal); regularize so Newton still contracts to (0,0)
        try:
            step = np.linalg.solve(J + 1e-9 * np.eye(2), F)
        except np.linalg.LinAlgError:
            step = F
        g = g - 0.5 * step
        if not np.all(np.isfinite(g)) or np.max(np.abs(g)) > 1e6:
            return None
    F = np.asarray(bs.beta(tuple(g)))
    return g if np.max(np.abs(F)) < 1e-9 else None


# =====================================================================================
# Q1 -- FIXED POINT(S). Analytic structure of the (x,y)=(f_2^2,f_0^2) polynomial system:
#   beta_x = -kappa x^2 b_2                        (vanishes  <=>  x = 0,   since b_2 != 0)
#   beta_y = kappa[(5/3)x^2 + 5xy + (5/6+d)y^2]    (at x=0 => (5/6+d)y^2 = 0  <=>  y = 0)
# => the ONLY fixed point is the GAUSSIAN point (0,0). No non-Gaussian (interacting) FP exists
#    at one loop in this 2-coupling truncation. GU's UV route here is FREEDOM, not SAFETY.
# =====================================================================================
log("\n" + "=" * 92)
log("Q1 -- FIXED POINT SEARCH  (g = (f_2^2, f_0^2), anchor c_RS_weyl=17/12, d_RS_R2=0)")
log("=" * 92)
BS = BetaSystem()

# (a) Gaussian point is a fixed point.
bg = BS.beta((0.0, 0.0))
check("Q1a  the GAUSSIAN point (0,0) is a fixed point of the full flow (beta=0): the asymptotically-"
      "FREE UV fixed point", abs(bg[0]) < TOL and abs(bg[1]) < TOL, f"beta(0,0) = {bg}")

# (b) multistart Newton from a grid of seeds -> every convergent root is (0,0): uniqueness.
seeds = [(a, b) for a in (-0.6, -0.2, 0.2, 0.6, 1.2) for b in (-0.6, -0.2, 0.2, 0.6, 1.2)]
roots = []
for s in seeds:
    r = newton_2d(BS, s)
    if r is not None:
        roots.append(tuple(np.round(r, 8)))
uniq = sorted(set(roots))
# The Gaussian FP is a DEGENERATE (quadratic) zero: beta ~ g^2, so a residual |beta|<1e-9 only pins
# |g| to ~sqrt(1e-9) ~ 3e-5. Newton's achievable precision floor here is ~1e-5, not machine eps.
# All convergent seeds must therefore CLUSTER at the origin within that floor (no second cluster).
NEWTON_FLOOR = 1e-5
max_dev = max((max(abs(x), abs(y)) for (x, y) in uniq), default=0.0)
all_gaussian = max_dev < NEWTON_FLOOR
check("Q1b  multistart Newton (25 seeds) -> every convergent root CLUSTERS at the Gaussian point "
      "within the degenerate-zero precision floor (~1e-5); no second cluster -> no non-Gaussian FP: "
      "GU realizes asymptotic FREEDOM, not SAFETY",
      len(uniq) >= 1 and all_gaussian, f"max deviation from (0,0) = {max_dev:.2e} < {NEWTON_FLOOR:g}")

# (c) analytic confirmation: beta_x=0 forces x=0 (b_2!=0); then beta_y=0 forces y=0 (5/6+d!=0).
#     Probe: on the whole line x=0, beta_y>0 for every y!=0 (no interior zero) -> no FP off origin.
offaxis_ok = all(BS.beta((0.0, y))[1] > 0 for y in (0.05, 0.3, 1.0, 3.0)) and \
             all(abs(BS.beta((x, 0.0))[0]) > 0 for x in (0.05, 0.3, 1.0))
check("Q1c  analytic: beta_x=0 <=> x=0 (b_2!=0), then beta_y=(5/6)y^2>0 for y!=0 -> Gaussian is the "
      "UNIQUE fixed point; no interacting FP", offaxis_ok,
      "beta_x has a double zero only at x=0; beta_y|_{x=0} has no nonzero root")


# =====================================================================================
# Q5 + Q2 -- STABILITY MATRIX / CRITICAL EXPONENTS at the Gaussian FP.
# The one-loop betas are purely QUADRATIC in the marginal couplings (no linear term), so the
# stability matrix M_ij = d beta_i/d g_j VANISHES at (0,0): both f_2^2 and f_0^2 are MARGINAL
# (linear critical exponent theta = 0). Relevance is decided at the nonlinear (log-running) level:
#   f_2^2: beta_x<0 for x>0  -> flows INTO the FP in the UV  -> marginally IRRELEVANT (AF; predicted).
#   f_0^2: beta_y>0 for y>0  -> flows AWAY from the FP in UV -> marginally RELEVANT (the conformal mode).
# =====================================================================================
log("\n" + "=" * 92)
log("Q5/Q2 -- STABILITY MATRIX & CRITICAL EXPONENTS at the Gaussian FP (marginal sector)")
log("=" * 92)
M = jacobian(BS, (0.0, 0.0))
eig = np.linalg.eigvals(M)
log(f"  M_ij(0,0) = {M.round(12).tolist()}")
log(f"  eigenvalues = {eig.round(12)}   -> critical exponents theta = -eig = {(-eig).round(12)}")
check("Q5a  the linear stability matrix at the Gaussian FP is the ZERO matrix: f_2^2 and f_0^2 are "
      "MARGINAL (theta=0 at linear order); relevance is logarithmic",
      np.allclose(M, 0.0, atol=1e-6) and np.allclose(eig, 0.0, atol=1e-6),
      f"eigenvalues {eig.round(9).tolist()}")

# marginal relevance at the nonlinear level (the sign of the quadratic beta along each axis):
f2_marg_irrel = BS.beta((0.3, 0.0))[0] < 0          # flows to 0 in UV -> AF -> irrelevant/predicted
f0_marg_rel = BS.beta((0.0, 0.3))[1] > 0            # flows away in UV -> relevant/free (conformal mode)
check("Q5b  nonlinear classification: f_2^2 is marginally IRRELEVANT (beta<0, AF -> UV value fixed to "
      "0 -> PREDICTED, not free)", f2_marg_irrel,
      f"beta_f2sq(0.3,0)={BS.beta((0.3,0.0))[0]:.3e} < 0")
check("Q5c  nonlinear classification: f_0^2 is marginally RELEVANT (beta>0, grows in UV -> the "
      "conformal-mode direction; one free parameter)", f0_marg_rel,
      f"beta_f0sq(0,0.3)={BS.beta((0.0,0.3))[1]:.3e} > 0")


# =====================================================================================
# Q2 -- CRITICAL-SURFACE DIMENSION = # relevant directions = # free parameters.
# At a Gaussian (free) UV fixed point, relevance is by CANONICAL scaling: a coupling/parameter with
# positive mass dimension multiplies a relevant (super-renormalizable) operator; the marginal
# (dimensionless) couplings split into marginally relevant/irrelevant by their loop sign (above).
#
# From THEORY_SPACE (Stage 1), the DIMENSIONFUL couplings (dimensionless=False) are the canonical
# relevant directions -- each is one free parameter that must be fixed by measurement:
#   G      (Newton)  -> the Planck/transmutation scale M_Pl  == the ratio-only free scale mu_DW
#   Lambda (cosm.)   -> the cosmological constant
#   m_RS             -> the RS mass  (ker-Gamma sector; GUESS-grade)
#   g4f              -> the four-fermi (RS sector; GUESS-grade)
# PLUS the marginally-relevant marginal coupling f_0^2 (the conformal mode).
# MINUS f_2^2, which AF fixes to 0 in the UV (a PREDICTION, not a free parameter).
# =====================================================================================
log("\n" + "=" * 92)
log("Q2 -- CRITICAL-SURFACE DIMENSION (= # relevant directions = # free parameters)")
log("=" * 92)
dimensionful = [c for c in THEORY_SPACE if not c.dimensionless]
marginal = [c for c in THEORY_SPACE if c.dimensionless]
canonical_relevant = [c.symbol for c in dimensionful]                 # positive-scaling relevant
grav_relevant = [c.symbol for c in dimensionful if c.sector.startswith("gravity")]  # KNOWN subset
log("  canonical RELEVANT (dimensionful) directions : " + ", ".join(canonical_relevant))
log("  of which pure-gravity (KNOWN grade)          : " + ", ".join(grav_relevant))
log("  marginal couplings                           : " + ", ".join(c.symbol for c in marginal))
log("    -> f_2^2 marginally IRRELEVANT (AF; predicted, NOT a free parameter)")
log("    -> f_0^2 marginally RELEVANT (conformal mode; +1 free parameter)")

check("Q2a  canonical relevant (dimensionful) directions number 4: {G->M_Pl, Lambda, m_RS, g4f}",
      len(canonical_relevant) == 4 and set(canonical_relevant) == {"G", "Lambda", "m_RS", "g4f"},
      f"relevant: {canonical_relevant}")
check("Q2b  the KNOWN-grade (pure-gravity) relevant directions are exactly 2: {G->M_Pl, Lambda}",
      set(grav_relevant) == {"G", "Lambda"}, f"gravity-sector relevant: {grav_relevant}")

# The headline critical-surface dimension, by grade:
#   KNOWN gravitational sector : 2 canonical (M_Pl, Lambda) + 1 marginally-relevant f_0^2 = 3
#                                (f_2^2 is AF -> predicted, removed from the count)
#   full truncation (adds ESTIMATED/GUESS RS): + m_RS + g4f = up to 5 (z_B,y_RS marginal-relevance
#                                undetermined at ESTIMATED grade).
grav_free_params = len(grav_relevant) + 1   # + f_0^2
full_dimensionful_plus_f0 = len(canonical_relevant) + 1
check("Q2c  CRITICAL-SURFACE DIMENSION, KNOWN gravitational sector = 3 free parameters "
      "{M_Pl (=mu_DW transmutation scale), Lambda, f_0^2}; f_2^2 is PREDICTED by AF (not counted)",
      grav_free_params == 3, f"gravitational free params = {grav_free_params}")
check("Q2d  full-truncation critical-surface dimension = 5 {M_Pl, Lambda, f_0^2, m_RS, g4f} at "
      "ESTIMATED/GUESS grade for the RS pieces (z_B,y_RS marginal-relevance undetermined)",
      full_dimensionful_plus_f0 == 5, f"full count = {full_dimensionful_plus_f0}")

# mu_DW identification: the free overall scale (falsifiability keystone) IS a relevant direction.
mu_dw_is_relevant = "G" in canonical_relevant   # Newton/M_Pl = the DeWitt transmutation scale
check("Q2e  the free overall scale mu_DW (H24 ratio-only / falsifiability keystone) is realized as "
      "the Einstein/Newton transmutation scale M_Pl -- ONE of the relevant directions",
      mu_dw_is_relevant, "mu_DW = M_Pl is relevant (predicted-to-be-free by the ratio-only geometry)")


# =====================================================================================
# Q4 -- f_0 CONFORMAL-MODE RESOLUTION via the fixed-RATIO analysis.
# Since f_2 -> 0 in the UV (AF), the physical UV-complete variable is the ratio r = f_0^2/f_2^2.
#   dr/dt = kappa * x * [ (5/6+d) r^2 + (5 + b_2) r + 5/3 ]
# A UV fixed RATIO r* (bracket = 0) => f_0^2 = r* f_2^2 -> 0 as well: TOTAL asymptotic freedom.
# The quadratic has real roots (large discriminant); BOTH roots are NEGATIVE (product 5/3 / (5/6) > 0,
# sum -(5+b_2)/(5/6) < 0). So the UV-complete trajectory exists but sits at f_0^2/f_2^2 < 0 -- the
# wrong-sign / conformal-factor direction. Whether that sign is admissible is the (out-of-scope)
# POSITIVITY question, not an obstruction to the existence of the asymptotically-free UV limit.
# =====================================================================================
log("\n" + "=" * 92)
log("Q4 -- f_0 CONFORMAL-MODE RESOLUTION (fixed-ratio r = f_0^2/f_2^2)")
log("=" * 92)
d = 0.0
b2 = BS.b2()
A, B, C = (5.0 / 6.0 + d), (5.0 + b2), (5.0 / 3.0)
disc = B * B - 4 * A * C
r_roots = np.roots([A, B, C])
log(f"  ratio ODE bracket: ({A:.4f}) r^2 + ({B:.4f}) r + ({C:.4f}) = 0")
log(f"  discriminant = {disc:.4f} (>0 -> real roots);  r* = {r_roots.round(5).tolist()}")
check("Q4a  a real UV fixed RATIO r*=f_0^2/f_2^2 exists (discriminant>0) -> the flow reaches a Gaussian "
      "UV limit along a fixed-ratio trajectory: TOTAL asymptotic freedom (both f_2,f_0 -> 0)",
      disc > 0 and np.all(np.isreal(r_roots)), f"r* = {r_roots.round(5).tolist()}")
check("Q4b  BOTH fixed ratios are NEGATIVE (f_0^2/f_2^2 < 0): the UV-complete trajectory sits on the "
      "wrong-sign conformal-mode direction -> admissibility of that sign IS the positivity question",
      np.all(np.real(r_roots) < 0), f"r* = {r_roots.round(5).tolist()} (both < 0)")

# verify the ratio flow actually freezes (dr/dt -> 0 as x -> 0) and drives f_0^2 -> 0 with f_2^2:
def dr_dt(bs, r, x):
    y = r * x
    bx, by = bs.beta((x, y))
    return by / x - r * bx / x
froze = abs(dr_dt(BS, r_roots[1].real, 1e-6)) < abs(dr_dt(BS, r_roots[1].real, 1e-1))
check("Q4c  the ratio flow FREEZES as f_2^2 -> 0 (dr/dt ~ kappa*x*bracket -> 0): f_0^2 = r* f_2^2 -> 0, "
      "confirming the conformal mode is carried to zero along the AF trajectory (not a Landau pole "
      "ON the fixed-ratio direction)", froze,
      "dr/dt is proportional to x and vanishes at the FP")


# =====================================================================================
# Q3 -- ROBUSTNESS of the AF verdict to the named parameter c_RS_weyl.
# f_2 asymptotic freedom needs b_2 = 133/10 + (matter) + c_RS_weyl > 0. With no extra matter:
#   b_2 > 0  <=>  c_RS_weyl > -133/10 = -13.3.
# Sweep c_RS_weyl and locate the threshold; confirm the anchor 17/12=+1.4167 is far above it.
# The only mechanism that could push c_RS_weyl below -13.3 is a large negative Krein-ghost trace-
# anomaly contribution -- the out-of-scope positivity fork. => the AF verdict is ROBUST.
# =====================================================================================
log("\n" + "=" * 92)
log("Q3 -- ROBUSTNESS SWEEP of c_RS_weyl (the one genuinely uncertain input)")
log("=" * 92)
grid = np.linspace(-20.0, 20.0, 4001)
af = np.array([BetaSystem(c_rs_weyl=float(c)).b2() > 0 for c in grid])
# threshold = largest c with b_2<=0 boundary
thr_idx = np.where(~af)[0]
threshold = grid[thr_idx.max()] if thr_idx.size else None
anchor = float(BetaSystem().c_rs_weyl)
log(f"  AF (b_2>0) holds for c_RS_weyl > {-133/10:.4f};  numeric sweep threshold ~ {threshold:.4f}")
log(f"  anchor c_RS_weyl = 17/12 = {anchor:.4f}  ->  margin above threshold = {anchor-(-133/10):.4f}")
check("Q3a  AF sign-flip threshold is c_RS_weyl = -133/10 = -13.3 (b_2 crosses 0 there), matching "
      "Stage 1", abs((-133.0/10.0) - (-13.3)) < TOL and threshold is not None
      and abs(threshold - (-13.3)) < 0.02, f"threshold = {threshold:.4f}")
check("Q3b  the standard anchor +1.4167 keeps AF by a wide margin (~14.7); AF survives for the entire "
      "plausible ker-Gamma range c_RS_weyl in [-13.3, +inf)",
      BetaSystem().b2() > 0 and (anchor - (-133.0/10.0)) > 14.0,
      f"margin = {anchor-(-133.0/10.0):.3f}")
check("Q3c  AF fails ONLY for c_RS_weyl < -13.3 (would require a huge NEGATIVE Krein-ghost trace-"
      "anomaly contribution = the out-of-scope positivity fork) -> verdict is ROBUST",
      bool(af[grid > -13.3].all()) and bool((~af[grid < -13.3]).all()),
      "AF holds for all c_RS>-13.3, fails for all c_RS<-13.3")


# =====================================================================================
# POSITIVITY CAVEAT (explicit, asserted-as-documentation): a UV fixed point in the couplings is a
# statement about the RG flow and does NOT establish Krein/loop positivity. The two are INDEPENDENT
# UV conditions. The fixed-ratio sign (f_0^2/f_2^2 < 0) is precisely where the two touch, and it is
# left OPEN.
# =====================================================================================
log("\n" + "=" * 92)
log("POSITIVITY CAVEAT (out of scope -- explicit)")
log("=" * 92)
POSITIVITY_SETTLED_HERE = False   # this flow does NOT settle Krein/loop positivity
AF_INDEPENDENT_OF_POSITIVITY = True
log("  A UV fixed point (asymptotic freedom) is about the FLOW of couplings; it does NOT resolve the")
log("  Krein [P,S]=0 loop-positivity question. The f_0^2/f_2^2<0 fixed ratio is exactly the place the")
log("  two conditions meet, and it is LEFT OPEN. AF verdict stands independent of positivity.")
check("C1  the flow's AF/FP result is stated INDEPENDENT of Krein loop-positivity (not settled here); "
      "the two are distinct UV conditions",
      (POSITIVITY_SETTLED_HERE is False) and (AF_INDEPENDENT_OF_POSITIVITY is True),
      "positivity remains the separate open frontier")


# =====================================================================================
# VERDICT / EXIT
# =====================================================================================
log("\n" + "=" * 92)
npass = sum(1 for _, ok, _ in results if ok)
ntot = len(results)
log(f"CHECKS: {npass}/{ntot} passed.")

# load-bearing asserts (real checks, not prints)
assert abs(BS.beta((0.0, 0.0))[0]) < TOL and abs(BS.beta((0.0, 0.0))[1]) < TOL, \
    "Gaussian point is not a fixed point"
assert all_gaussian, "a non-Gaussian fixed point appeared (would flip AF->AS)"
assert np.allclose(jacobian(BS, (0.0, 0.0)), 0.0, atol=1e-6), \
    "stability matrix at Gaussian FP is not zero (marginal sector expected)"
assert BS.beta((0.3, 0.0))[0] < 0 < BS.beta((0.0, 0.3))[1], \
    "expected f_2^2 marginally irrelevant (AF) and f_0^2 marginally relevant"
assert set([c.symbol for c in THEORY_SPACE if not c.dimensionless]) == {"G", "Lambda", "m_RS", "g4f"}, \
    "canonical relevant (dimensionful) set changed"
assert disc > 0 and np.all(np.real(r_roots) < 0), \
    "expected real, both-negative fixed ratios (conformal-mode direction)"
assert threshold is not None and abs(threshold - (-13.3)) < 0.02, "AF threshold != -13.3"
assert npass == ntot, "some Stage-2 checks FAILED -- see [FAIL] lines"

log("")
log("VERDICT (H57 Stage 2, this truncation):")
log("  * FIXED POINT: the GAUSSIAN point (0,0) is the UNIQUE UV fixed point. No non-Gaussian FP.")
log("    => GU realizes ASYMPTOTIC FREEDOM, not asymptotic SAFETY, in this 2-coupling one-loop model.")
log("  * CRITICAL-SURFACE DIMENSION = 3 (KNOWN gravitational sector): {M_Pl(=mu_DW), Lambda, f_0^2};")
log("    f_2^2 is PREDICTED by AF (removed). Full truncation up to 5 (+ m_RS, + g4f, RS grade GUESS).")
log("  * f_0 CONFORMAL MODE: resolved into a fixed RATIO f_0^2/f_2^2 -> total AF, but at r*<0 (wrong-")
log("    sign); admissibility of that sign IS the positivity question (out of scope).")
log("  * ROBUSTNESS: AF survives for all c_RS_weyl > -13.3; anchor +1.42 is far above. Robust.")
log("  * POSITIVITY: NOT settled here; independent of the AF/FP result.")
log("ALL CHECKS PASS.")
raise SystemExit(0)
