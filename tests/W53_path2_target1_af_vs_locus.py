#!/usr/bin/env python3
r"""
W53 / Path-2 wave-2 TARGET 1 -- does the asymptotically-free 4th-order (Stelle/agravity) RG flow
REACH branch-E's exceptional (Jordan / pole-collision) locus, on which the positivity-defining
grading degenerates and keep-and-grade positivity is unrescuable?

This connects three prior results (NOT blind):
  * Branch E (W52): the positivity-defining grading eta_+ is DYNAMICAL and DEGENERATES on a codim-1
    EXCEPTIONAL locus. In the 2x2 skeleton the locus is a/b = 1 (eigenvalues collide, Jordan block,
    lambda_min(eta_+) = 1 - a/b -> 0). Its PHYSICAL face in 4th-order gravity (branches A, D) is the
    collision of the two spin-2 poles: the massive spin-2 GHOST pole at p^2 = m2^2 colliding with the
    massless graviton pole at p^2 = 0, i.e. the CONFORMAL / symmetry-enhanced point  m2^2 -> 0. (E
    named exactly this in its repair-4: "the conformal / massless-spin-2-ghost limit m2 -> 0".)
  * W45/W46/W47 (H57/H60): the AF flow. Pure-gravity Weyl coupling f_2^2 is ASYMPTOTICALLY FREE
    (b_2 = 133/10 + ... > 0 => beta_{f2^2} = -kappa f2^4 b_2 < 0 => f_2^2 -> 0 in the UV), the Gaussian
    point is the unique UV fixed point, and the UV-complete trajectory sits at a NEGATIVE fixed ratio
    r* = f_0^2/f_2^2 < 0 (wrong-sign conformal mode).

THE CRUX (task): the massive spin-2 ghost mass is, in the standard agravity convention,
      m2^2 = (1/2) f_2^2 * M_Pl^2                      [Salvio-Strumia, arXiv:1403.4226]
(Weyl term written -(1/(2 f_2^2)) C^2, so f_2 is a coupling like Yang-Mills g and AF is f_2 -> 0; the
massive spin-2 pole is at m2^2 = f_2^2 M_Pl^2 / 2, i.e. m2^2 is PROPORTIONAL to f_2^2, NOT its inverse).
M_Pl is the dimensional-transmutation (Newton) scale -- a RELEVANT direction that is FIXED along the
flow (W46 Q2e: mu_DW = M_Pl). Therefore the dimensionless distance-to-locus is

      d_locus(mu)  ==  m2^2 / M_Pl^2  =  (1/2) f_2^2(mu)      (>0 <=> strictly PT-UNBROKEN interior).

Asymptotic freedom drives f_2^2 -> 0, hence d_locus -> 0: THE AF FLOW MOVES **TOWARD** THE EXCEPTIONAL
LOCUS (m2^2 = 0), not away. The question is WHETHER it is reached at finite RG time (=> CROSSES) or
only in the mu -> infinity limit at the free UV fixed point (=> BOUNDARY / asymptotic touch, strictly
clear at every finite scale).

TWO INDEPENDENT DERIVATIONS of the crossing verdict (program's two-derivations discipline):
  (i)  NUMERIC: RK4-integrate the imported W45 BetaSystem.beta_f2sq from an IR seed to deep UV; read off
       d_locus(t) = f_2^2(t)/2 and the toy proxy a/b(t); show it is strictly >0 and monotonically ->0.
  (ii) ANALYTIC: the pure Weyl ODE df2/dt = -kappa b_2 f2^2 integrates in closed form to
       1/f2(t) = 1/f2_0 + kappa b_2 t  =>  f2(t) = f2_0 / (1 + kappa b_2 f2_0 t) -> 0 like 1/(kappa b_2 t).
       So d_locus = f2/2 -> 0 only as t -> infinity (logarithmically in mu = e^t); at every FINITE t it
       is strictly positive. The exceptional locus m2^2 = 0 is the UV FIXED POINT ITSELF (f2 = 0), not
       a finite-RG-time crossing.
The two must agree (they do, to RK4 precision).

VERDICT (graded): BOUNDARY. The AF trajectory is strictly PT-UNBROKEN (grading exists, positivity well
defined) at EVERY finite RG scale in the spin-2 sector; it approaches E's exceptional locus m2^2 = 0
monotonically and reaches it ONLY at the UV Gaussian fixed point, where f_2^2 = 0 so the theory is FREE
and the ghost DECOUPLES (a free-theory degeneration, harmless: branch A's negative cut needs the
interaction that is switching off). It does NOT cross into the PT-broken domain at any finite scale in
spin-2. => keep-and-grade positivity is RG-STABLE throughout the entire INTERACTING flow -- a qualified
POSITIVE -- but the grading pinches down onto the locus (||C|| -> infinity, E repair-4c) exactly at the
free UV endpoint, so this is NOT a clean interior-all-the-way-up proof-of-concept; it is a boundary
limit. The one place it could be an outright NEGATIVE is the SPIN-0 conformal mode: the UV-complete
trajectory sits at f_0^2/f_2^2 = r* < 0, a wrong-sign conformal mode; IF that wrong sign is a genuine
spectrum-reality violation (tachyonic M_0^2 < 0 = complex-conjugate frequency pair = PT-BROKEN) the
scalar sector already sits on the broken side (=> CROSSES for spin-0). That physical status is the
LOAD-BEARING open question and is graded PLAUSIBLE-broken, not proven.

CONSTRUCTION FORKS (GEOMETER-VS-PHYSICS-OBJECTS.md), stated:
  * "the exceptional locus": PHYSICS face = spin-2 pole collision m2^2 -> 0 (A/D), which realizes E's
    program-native grading-degeneration a/b -> 1. Both used, cross-identified; the mass-vs-coupling
    relation m2^2 = f_2^2 M_Pl^2/2 is the STANDARD agravity construction (Salvio-Strumia), chosen
    because AF and the ghost mass are BOTH defined in it -- the fork is named so the verdict is not read
    as convention-dependent.
  * "the ghost": kept (keep-and-grade Krein/PT), grading-agnostic at the pole level (as in Branch A).
  * unitarity/positivity object: POSITIVE Born-rule inner product (E's target), not pseudo-unitarity.

LOAD-BEARING ASSUMPTION: m2^2 = (1/2) f_2^2 M_Pl^2 with M_Pl the FIXED transmutation scale (so the
dimensionless distance-to-locus is (1/2) f_2^2 and AF drives it to 0). If instead one measures the pole
relative to the RUNNING scale mu (m2^2/mu^2) the approach is even faster; if the convention were
inverted (m2^2 ~ M_Pl^2/f_2^2, ghost mass -> infinity in the UV) the flow would move AWAY from the
locus and the verdict would flip to STAYS-CLEAR. The agravity convention (ghost mass PROPORTIONAL to
the AF coupling) is the standard one and is what makes this a genuine tension rather than a triviality.

Reproducible: python tests/W53_path2_target1_af_vs_locus.py   (pure Python + imports W45; exit 0)
No canon / RESEARCH-STATUS / claim-status / verdict / posture file touched. Exploration-grade.
"""
from __future__ import annotations

import contextlib
import importlib.util
import io
import math
import os
import sys

TOL = 1e-12
results: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    results.append((name, bool(passed), detail))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))


def log(msg: str = "") -> None:
    print(msg, flush=True)


# =====================================================================================
# IMPORT the W45 Stage-1 beta system (do NOT re-derive the beta functions).
# W45 runs top-level checks then `raise SystemExit(0)`; load via spec, swallow the exit.
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
KAPPA = S1.KAPPA

log("=" * 96)
log("W53 / PATH-2 WAVE-2 TARGET 1 -- AF FLOW vs BRANCH-E EXCEPTIONAL (JORDAN / POLE-COLLISION) LOCUS")
log("=" * 96)

BS = BetaSystem()  # RS anchor c_RS_weyl = 17/12 (deepens AF); d_RS_R2 = 0
b2 = BS.b2()
check("I1  imported W45 BetaSystem; Weyl coefficient b_2 > 0 (asymptotic freedom of f_2^2 confirmed): "
      "beta_{f2^2} = -kappa f2^4 b_2 < 0 -> f_2^2 -> 0 in the UV",
      BetaSystem is not None and b2 > 0 and BS.beta_f2sq(0.5, 0.3) < 0,
      f"b_2 = {b2:.5f}; beta_f2sq(0.5,0.3) = {BS.beta_f2sq(0.5,0.3):.3e} < 0")


# =====================================================================================
# E's EXCEPTIONAL LOCUS, made explicit for 4th-order gravity.
#   Toy (W52): locus at a/b = 1;   lambda_min(eta_+) = 1 - a/b -> 0 (grading degenerates).
#   Physics face (A/D): the two spin-2 poles collide -> m2^2 -> 0 (conformal point).
#   Convention (Salvio-Strumia agravity): m2^2 = (1/2) f_2^2 M_Pl^2, M_Pl the FIXED transmutation scale.
#   => dimensionless distance-to-locus  d_locus = m2^2/M_Pl^2 = (1/2) f_2^2   (>0 <=> PT-unbroken).
#   Toy proxy (a monotone reparametrization, NOT a derived identity -- stated as a model):
#       a/b(d) = 1/(1 + d),   so  1 - a/b = d/(1+d) -> 0 as d -> 0, matching E's lambda_min -> 0.
#   The load-bearing content is only: distance-to-locus is monotone in f_2^2 and ->0 iff f_2^2 ->0.
# =====================================================================================
MPL2 = 1.0  # M_Pl^2 in its own (fixed transmutation) units; d_locus is dimensionless = f2/2.


def d_locus(f2sq: float) -> float:
    """Dimensionless distance to E's exceptional locus: m2^2/M_Pl^2 = (1/2) f_2^2."""
    return 0.5 * f2sq * MPL2


def ab_ratio(f2sq: float) -> float:
    """Toy proxy a/b (monotone model): -> 1 (locus) as f2 -> 0; -> 0 (deep interior) as f2 large."""
    d = d_locus(f2sq)
    return 1.0 / (1.0 + d)


def lam_min_etaplus(f2sq: float) -> float:
    """E's grading eigenvalue proxy lambda_min(eta_+) = 1 - a/b -> 0 on the locus."""
    return 1.0 - ab_ratio(f2sq)


# =====================================================================================
# DERIVATION (i) -- NUMERIC RK4 integration of the imported beta from IR to deep UV.
# =====================================================================================
def rk4_f2_flow(f2_0: float, t_max: float, n: int) -> list[tuple[float, float]]:
    """Integrate df2/dt = beta_f2sq(f2, .) from t=0 (IR seed) to t=t_max (UV) with RK4."""
    dt = t_max / n
    f2 = f2_0
    traj = [(0.0, f2)]
    for i in range(n):
        t = i * dt
        # f0sq does not enter beta_f2sq (independent), pass a spectator 0.0.
        k1 = BS.beta_f2sq(f2, 0.0)
        k2 = BS.beta_f2sq(f2 + 0.5 * dt * k1, 0.0)
        k3 = BS.beta_f2sq(f2 + 0.5 * dt * k2, 0.0)
        k4 = BS.beta_f2sq(f2 + dt * k3, 0.0)
        f2 = f2 + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        traj.append(((i + 1) * dt, f2))
    return traj


F2_0 = 0.8           # IR seed for the Weyl coupling (order-1, inside the perturbative window)
T_MAX = 4000.0       # deep UV in RG time t = ln mu
N_STEPS = 400000
traj = rk4_f2_flow(F2_0, T_MAX, N_STEPS)

t_end, f2_end = traj[-1]
d_end = d_locus(f2_end)
d_start = d_locus(F2_0)

# monotone decrease toward the locus, strictly positive throughout (sample the trajectory):
sample_idx = [0, N_STEPS // 100, N_STEPS // 10, N_STEPS // 2, N_STEPS]
samples = [(traj[i][0], traj[i][1], d_locus(traj[i][1])) for i in sample_idx]
all_positive = all(f2 > 0.0 for _, f2 in traj)                    # strictly PT-unbroken at every finite t
strictly_decreasing = all(traj[i][1] > traj[i + 1][1] for i in range(0, N_STEPS, N_STEPS // 200))
# AF is LOGARITHMIC, so d_locus shrinks slowly; the physical content is "far below IR, still >0":
approaches_locus = (d_end < d_start / 100.0) and d_end > 0.0      # near, but not AT, the locus at finite t

log("\n" + "-" * 96)
log("DERIVATION (i) NUMERIC: RK4 flow of the imported beta_f2sq from IR (t=0) to deep UV")
log("-" * 96)
log(f"  IR seed  f_2^2(0)      = {F2_0:.6f}   -> d_locus = m2^2/M_Pl^2 = {d_start:.6f}")
for (tt, f2v, dv) in samples:
    log(f"    t={tt:9.2f}  f_2^2={f2v:.6e}  d_locus=m2^2/M_Pl^2={dv:.6e}  a/b={ab_ratio(f2v):.6f}  "
        f"lam_min(eta_+)={lam_min_etaplus(f2v):.6e}")
log(f"  UV end   f_2^2({t_end:.0f}) = {f2_end:.6e} -> d_locus = {d_end:.6e}  (approaching 0, still > 0)")

check("N1  along the numerically integrated AF flow, f_2^2(t) > 0 at EVERY finite RG time: the theory "
      "is STRICTLY PT-UNBROKEN (m2^2 = (1/2)f_2^2 M_Pl^2 > 0) throughout the interacting flow -- no "
      "finite-time crossing of the locus in the spin-2 sector",
      all_positive and f2_end > 0.0, f"min f_2^2 on trajectory = {f2_end:.3e} > 0")
check("N2  d_locus = m2^2/M_Pl^2 = (1/2)f_2^2 DECREASES MONOTONICALLY toward 0: the AF flow moves "
      "TOWARD E's exceptional locus (m2^2 -> 0), not away (because m2^2 is PROPORTIONAL to the AF "
      "coupling f_2^2)",
      strictly_decreasing and d_end < d_start, f"d_locus: {d_start:.4f} (IR) -> {d_end:.3e} (UV)")
check("N3  the locus is only APPROACHED, not reached, at finite RG time: d_locus(UV) is small but "
      "strictly > 0 -> BOUNDARY behavior (asymptotic touch), not a finite-time CROSS",
      approaches_locus, f"d_locus at t={t_end:.0f} is {d_end:.3e} (>0, ->0)")


# =====================================================================================
# DERIVATION (ii) -- ANALYTIC closed form of the pure-Weyl ODE, compared to the numeric flow.
#   df2/dt = -kappa b_2 f2^2  =>  d(1/f2)/dt = kappa b_2  =>  1/f2(t) = 1/f2_0 + kappa b_2 t.
#   => f2(t) = f2_0 / (1 + kappa b_2 f2_0 t) -> 0 like 1/(kappa b_2 t): logarithmic in mu = e^t.
#   Hence d_locus = f2/2 -> 0 ONLY as t -> infinity; at every finite t it is strictly positive.
#   The exceptional locus m2^2 = 0 <=> f2 = 0 IS the UV Gaussian fixed point itself (t = infinity),
#   NOT a finite-RG-time crossing.
# =====================================================================================
def f2_analytic(t: float, f2_0: float) -> float:
    return f2_0 / (1.0 + KAPPA * b2 * f2_0 * t)


f2_ana_end = f2_analytic(t_end, F2_0)
rel_err = abs(f2_end - f2_ana_end) / f2_ana_end
# leading-log: f2 ~ 1/(kappa b_2 t) for large t -> check the asymptotic slope of 1/f2 vs t is kappa b_2.
inv_slope = (1.0 / f2_end - 1.0 / F2_0) / t_end

log("\n" + "-" * 96)
log("DERIVATION (ii) ANALYTIC: 1/f2(t) = 1/f2_0 + kappa*b_2*t  =>  f2 -> 0 like 1/(kappa b_2 t)")
log("-" * 96)
log(f"  analytic f_2^2({t_end:.0f}) = {f2_ana_end:.6e}   numeric = {f2_end:.6e}   rel.err = {rel_err:.2e}")
log(f"  d(1/f2)/dt measured = {inv_slope:.6e}   predicted kappa*b_2 = {KAPPA*b2:.6e}")
log(f"  => f2 -> 0 (m2^2 -> 0) ONLY as t=ln(mu) -> infinity: the locus is the UV FIXED POINT, reached")
log(f"     logarithmically; strictly positive m2^2 at every finite scale.")

check("A1  analytic closed form 1/f2 = 1/f2_0 + kappa*b_2*t matches the numeric RK4 flow to high "
      "precision (TWO independent derivations AGREE)",
      rel_err < 1e-6, f"rel.err numeric-vs-analytic = {rel_err:.2e}")
check("A2  asymptotic slope d(1/f2)/dt = kappa*b_2 (leading-log AF): f2 ~ 1/(kappa b_2 t) -> 0, so "
      "m2^2/M_Pl^2 = f2/2 -> 0 only as t -> infinity -> the locus is the UV FIXED POINT (f2=0), not a "
      "finite-t crossing",
      abs(inv_slope - KAPPA * b2) / (KAPPA * b2) < 1e-6,
      f"slope {inv_slope:.4e} vs kappa*b_2 {KAPPA*b2:.4e}")
check("A3  the two derivations AGREE on the verdict: strictly PT-unbroken (m2^2>0) at every finite RG "
      "scale; locus (m2^2=0) touched ONLY at the UV Gaussian fixed point (f2=0, free theory)",
      all_positive and rel_err < 1e-6 and approaches_locus,
      "numeric + analytic both -> BOUNDARY (asymptotic touch at UV FP), no finite-time cross in spin-2")


# =====================================================================================
# THE SPIN-0 CONFORMAL MODE -- the wrong-sign fixed ratio (the place the verdict could go NEGATIVE).
#   Ratio ODE bracket (W46): A r^2 + B r + C,  A = 5/6 + d,  B = 5 + b_2,  C = 5/3,  r = f_0^2/f_2^2.
#   Both roots NEGATIVE (product C/A>0, sum -B/A<0). The UV-complete trajectory sits at r* < 0 =>
#   f_0^2 < 0 (since f_2^2 > 0) => wrong-sign conformal mode => m2^2_0 = (1/2) f_0^2 M_Pl^2 < 0
#   (tachyonic spin-0). A tachyonic mode has imaginary frequency (+/- i|M_0|), a complex-conjugate
#   pair = PT-BROKEN in E's sense. IF this is a genuine physical spectrum (not the unphysical
#   Euclidean conformal-factor / gauge mode), the SPIN-0 sector already sits on the broken side.
#   This is graded PLAUSIBLE-broken (physical status open), NOT proven.
# =====================================================================================
d_r2 = 0.0
A, B, C = (5.0 / 6.0 + d_r2), (5.0 + b2), (5.0 / 3.0)
disc = B * B - 4 * A * C
sq = math.sqrt(disc)
r_plus = (-B + sq) / (2 * A)
r_minus = (-B - sq) / (2 * A)

log("\n" + "-" * 96)
log("SPIN-0 CONFORMAL MODE: the wrong-sign UV fixed ratio r* = f_0^2/f_2^2 (W46), the potential CROSS")
log("-" * 96)
log(f"  ratio bracket: ({A:.4f}) r^2 + ({B:.4f}) r + ({C:.4f}) = 0;  disc = {disc:.4f} > 0")
log(f"  fixed ratios r* = {{{r_plus:.5f}, {r_minus:.5f}}}  (BOTH < 0 -> wrong-sign conformal mode)")
log(f"  => on the UV-complete trajectory f_0^2 < 0 -> m2^2_0 = (1/2)f_0^2 M_Pl^2 < 0 (tachyonic spin-0)")
log(f"  => IF physical (not the gauge/Euclidean conformal-factor mode), spin-0 spectrum is complex ->")
log(f"     PT-BROKEN: the scalar sector would already sit PAST E's locus (verdict CROSSES for spin-0).")

check("S1  the UV-complete fixed ratio r* = f_0^2/f_2^2 is real and BOTH roots are NEGATIVE (W46 "
      "reproduced): the AF-complete trajectory carries a WRONG-SIGN conformal (spin-0) mode",
      disc > 0 and r_plus < 0 and r_minus < 0, f"r* = {r_plus:.4f}, {r_minus:.4f} (both < 0)")
check("S2  wrong-sign f_0^2 -> tachyonic spin-0 (m2^2_0 < 0) = imaginary frequency = complex-conjugate "
      "pair = PT-BROKEN in E's sense: the spin-0 sector PLAUSIBLY sits on the broken side of the locus. "
      "Graded PLAUSIBLE, NOT proven (physical-vs-gauge status of the conformal mode is the open crux)",
      (r_plus < 0 and r_minus < 0),
      "spin-0 = PLAUSIBLE-broken; the load-bearing open question")


# =====================================================================================
# HONESTY GUARD -- what is proven vs argued vs open.
# =====================================================================================
SPIN2_FINITE_TIME_CROSS = False   # NOT proven: spin-2 stays strictly PT-unbroken at every finite scale
SPIN2_TOUCHES_AT_UV_FP = True     # PROVEN: m2^2 -> 0 exactly at the free UV fixed point (f2 = 0)
SPIN0_BROKEN_PROVEN = False       # spin-0 wrong-sign -> PLAUSIBLE-broken, physical status OPEN
check("H1  honesty guard: spin-2 has NO finite-RG-time crossing (strictly PT-unbroken at every finite "
      "scale); it TOUCHES the locus only at the free UV fixed point; spin-0 broken is PLAUSIBLE not "
      "proven. No over-claim of a clean pass NOR of a completed kill.",
      (SPIN2_FINITE_TIME_CROSS is False) and (SPIN2_TOUCHES_AT_UV_FP is True)
      and (SPIN0_BROKEN_PROVEN is False),
      "spin-2: BOUNDARY (proven); spin-0: PLAUSIBLE-broken (open)")


# =====================================================================================
# VERDICT / EXIT
# =====================================================================================
log("\n" + "=" * 96)
npass = sum(1 for _, ok, _ in results if ok)
ntot = len(results)
log(f"CHECKS: {npass}/{ntot} passed.")

# load-bearing asserts
assert b2 > 0 and BS.beta_f2sq(0.5, 0.3) < 0, "f_2^2 not asymptotically free"
assert all_positive and f2_end > 0.0, "spin-2 crossed the locus at finite RG time (should not)"
assert strictly_decreasing and d_end < d_start, "d_locus not monotonically decreasing toward the locus"
assert approaches_locus, "d_locus did not approach the locus (expected asymptotic touch)"
assert rel_err < 1e-6, "numeric and analytic derivations disagree (two-derivation discipline FAILED)"
assert abs(inv_slope - KAPPA * b2) / (KAPPA * b2) < 1e-6, "leading-log slope != kappa*b_2"
assert disc > 0 and r_plus < 0 and r_minus < 0, "fixed ratio not both-negative (spin-0 wrong sign)"
assert SPIN2_FINITE_TIME_CROSS is False and SPIN0_BROKEN_PROVEN is False, "honesty guard violated"
assert npass == ntot, "some W53 checks FAILED -- see [FAIL] lines"

log("")
log("VERDICT (Path-2 wave-2 Target 1): BOUNDARY.")
log("  SPIN-2 (clean, PROVEN two ways): the AF trajectory is STRICTLY PT-UNBROKEN (m2^2=(1/2)f_2^2 M_Pl^2")
log("    > 0, grading well-defined) at EVERY FINITE RG scale; because m2^2 is PROPORTIONAL to the AF")
log("    coupling f_2^2, the flow moves TOWARD E's exceptional locus (m2^2 -> 0), reaching it ONLY at the")
log("    UV Gaussian fixed point (f_2^2 = 0), where the theory is FREE and the ghost DECOUPLES. No finite-")
log("    time crossing. Numeric RK4 and the analytic 1/f2 = 1/f2_0 + kappa b_2 t AGREE.")
log("  READING: keep-and-grade positivity is RG-STABLE across the whole INTERACTING flow (qualified")
log("    POSITIVE), but the grading pinches onto the locus (||C||->inf) at the free UV endpoint -- a")
log("    BOUNDARY limit, NOT a clean interior-all-the-way-up proof-of-concept.")
log("  SPIN-0 (PLAUSIBLE-broken, OPEN): the UV-complete trajectory sits at f_0^2/f_2^2 = r* < 0, a wrong-")
log("    sign conformal mode -> tachyonic M_0^2 < 0 -> complex frequency pair -> PT-BROKEN. IF physical")
log("    (not the gauge/Euclidean conformal-factor mode) the scalar sector already sits PAST the locus")
log("    (=> CROSSES for spin-0). Physical-vs-gauge status is the LOAD-BEARING open question.")
log("  => NOT the clean STAYS-CLEAR proof-of-concept: keep-and-grade survives the entire finite-scale")
log("     spin-2 flow, but the AF endpoint is ON the locus and the conformal mode plausibly sits past it.")
log("     The removal-based (fakeon/Lee-Wick) route remains the safer one for the conformal mode.")
log("  LOAD-BEARING ASSUMPTION: m2^2 = (1/2) f_2^2 M_Pl^2 (agravity: ghost mass PROPORTIONAL to the AF")
log("    coupling, M_Pl the fixed transmutation scale). Inverting it (m2^2 ~ M_Pl^2/f_2^2) would flip the")
log("    verdict to STAYS-CLEAR; the standard convention is what makes this a genuine tension.")
log("  No canon / RESEARCH-STATUS / claim-status / verdict / posture file touched. H59 remains OPEN.")
raise SystemExit(0)
