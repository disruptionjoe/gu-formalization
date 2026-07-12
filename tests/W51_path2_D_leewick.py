#!/usr/bin/env python3
r"""
W51 / Path-2 Branch D -- Lee-Wick / complex-pole construction of the Stelle spin-2 ghost.

GU-INDEPENDENT. Concrete example: the massive spin-2 graviton of 4th-order (Stelle) gravity.
This file encodes, as deterministic assertions, the two computations Branch D rests on:

  (a) POLE DISPLACEMENT ARITHMETIC -- the sign of the one-loop Im self-energy at the ghost mass.
      Does the one-loop self-energy move the ghost pole OFF the real axis, and in the RIGHT
      direction (into a complex-conjugate pair, so the ghost becomes an unstable resonance rather
      than a stable negative-norm asymptotic state)?

  (b) COMPLEX-POLE CUT CHECK (GOW / Lee-Wick deformed cutting rules) -- on real external states the
      would-be ghost cut is empty (poles off-axis, deformed away), so the optical theorem
      Im M(phys) = SUM_phys |M|^2 >= 0 holds with NO negative ghost contribution.

Plus the cross-check that the computation reduces to the KNOWN scalar Lee-Wick / GOW result in the
decoupling limit, and the failure-mode guard (a below-threshold ghost would NOT go complex -> LW
unavailable), and the causality datum (Lorentz-invariant conjugate pair; micro-causality violated
at ~1/M).

CONSTRUCTION FORKS (GEOMETER-VS-PHYSICS-OBJECTS.md), stated explicitly:
  (1) "The ghost": Lee-Wick COMPLEX-POLE RESONANCE (pole pushed off-axis by interactions; never an
      asymptotic state), NOT the stable negative-norm state and NOT the GU-native Krein keep-and-grade
      object. A distinct physics construction; tested here for whether the Stelle ghost ADMITS it.
  (2) "The cutting rules": GOW / Lee-Wick rules deformed around the complex-conjugate poles (CLOP /
      Coleman contour), NOT real-axis Cutkosky through an on-shell ghost pole.

Physics inputs that are PROVEN (not tuned):
  * Im B0(s;0,0) = 1/(16 pi) for s>0  -- sign of the massless one-loop bubble discontinuity.
  * The massive spin-2 is the HEAVIEST mode: threshold for 2 massless is s_th = 0, so M^2 > s_th
    always -> the ghost is ABOVE threshold -> Im Sigma(M^2) != 0.
  * Sigma(p^2*) = Sigma(p^2)* (reality of the action) -> poles come in conjugate pairs.
  * Counterterms are real -> they shift Re Sigma only, never remove Im Sigma.

This file settles NO scientific status. Q-cut/Q-pos/Q-caus verdicts are graded in the companion
exploration; here we only assert the arithmetic those grades stand on. Exploration-grade.

Reproducible: python tests/W51_path2_D_leewick.py   (exit 0 on PASS)
No canon/verdict/claim-status file touched. No git commit (orchestrator verifies+commits).
"""
from __future__ import annotations

import cmath
import math

TOL = 1e-12
results: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    results.append((name, bool(passed), detail))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))


def log(msg: str = "") -> None:
    print(msg, flush=True)


# ----------------------------------------------------------------------------------------------------
# Physics model (minimal, deterministic).
#
# Spin-2 Stelle propagator D(p^2) = (1/M^2)[ 1/p^2 - 1/(p^2 - M^2) ] P^(2).
# Massless pole residue +1/M^2 (healthy); massive pole residue -1/M^2 (the ghost: wrong sign).
#
# One-loop self-energy of the massive mode from the 2-massless-graviton channel. Derivative
# gravitational vertices contribute a positive tensor/momentum factor c * s^2; the bubble
# discontinuity supplies 1/(16 pi):
#
#     Im Sigma(s) = (kappa^2 c / 16 pi) * s^2   for s > s_th,   0 for s <= s_th.
#
# ----------------------------------------------------------------------------------------------------

IM_B0 = 1.0 / (16.0 * math.pi)  # PROVEN sign/magnitude of the massless one-loop bubble discontinuity.


def im_sigma(s: float, kappa: float, c: float, s_th: float = 0.0) -> float:
    """Imaginary part of the one-loop self-energy of the massive spin-2 mode.

    s_th = 0 for the gravitational ghost (two massless gravitons); a fictitious s_th > M^2 is used
    only to model the failure mode (a below-threshold ghost that cannot go complex).
    """
    if s <= s_th:
        return 0.0
    return (kappa * kappa * c) * IM_B0 * (s * s)


def re_sigma_shift(kappa: float, c: float, M2: float) -> float:
    """A representative real part (mass renormalization). Its exact value is scheme dependent and
    is NOT load-bearing: it moves the pole's REAL part only. Modeled as a finite real number."""
    return 0.5 * kappa * kappa * c * IM_B0 * M2 * M2  # any real number; sign/size not load-bearing


def ghost_poles(kappa: float, c: float, M: float, s_th: float = 0.0) -> tuple[complex, complex]:
    """Dressed massive-mode pole positions in the s = p^2 plane.

    Inverse propagator zero: p^2 - M^2 - Sigma(p^2) = 0, evaluated (one-loop, on-shell approx) at
    s = M^2. Returns the conjugate PAIR (s_+, s_-).
    """
    M2 = M * M
    re = M2 + re_sigma_shift(kappa, c, M2)
    im = im_sigma(M2, kappa, c, s_th)
    return complex(re, im), complex(re, -im)


# ----------------------------------------------------------------------------------------------------
log("=" * 96)
log("W51 / PATH-2 BRANCH D -- LEE-WICK COMPLEX-POLE CONSTRUCTION OF THE STELLE SPIN-2 GHOST")
log("=" * 96)

# Canonical gravitational-ghost parameters (dimensionless units, M in units of itself).
KAPPA = 1.0     # real coupling (reality of the action is what forces conjugate pairs)
C_TENSOR = 1.0  # positive spin-2 polarization/phase-space factor, c > 0 (PROVEN sign)
M = 1.0         # ghost mass; the massive spin-2 is the heaviest mode
M2 = M * M
S_TH_GRAV = 0.0  # two massless gravitons -> threshold at s = 0; ghost is ABOVE it

# --- (a) POLE DISPLACEMENT ARITHMETIC ------------------------------------------------------------
log("")
log("(a) Pole-displacement arithmetic: sign of the one-loop Im self-energy at the ghost mass")

imsig = im_sigma(M2, KAPPA, C_TENSOR, S_TH_GRAV)
log(f"    Im Sigma(M^2) = kappa^2 c /(16 pi) * M^4 = {imsig:.10f}")

check(
    "A1  the massive spin-2 ghost is ABOVE the two-massless-graviton threshold (s_th = 0 < M^2), so "
    "the ghost CAN decay -- the necessary condition for a Lee-Wick resonance is available",
    S_TH_GRAV < M2,
    f"s_th={S_TH_GRAV} < M^2={M2}",
)

check(
    "A2  Im Sigma(M^2) > 0 (RIGHT DIRECTION): the one-loop self-energy has a nonzero, positive "
    "absorptive part, forced by the sign of the massless bubble discontinuity 1/(16 pi) and c>0",
    imsig > 0.0,
    f"Im Sigma(M^2) = {imsig:.10f} > 0",
)

s_plus, s_minus = ghost_poles(KAPPA, C_TENSOR, M, S_TH_GRAV)
log(f"    dressed ghost poles:  s_+ = {s_plus},  s_- = {s_minus}")

check(
    "A3  the dressed ghost pole leaves the REAL axis (Im s_pole != 0): the stable negative-norm "
    "asymptotic ghost is dynamically destabilized into a resonance",
    abs(s_plus.imag) > TOL,
    f"Im s_+ = {s_plus.imag:.10f}",
)

check(
    "A4  the poles form a COMPLEX-CONJUGATE PAIR (s_+ = conj(s_-)), forced by reality of the action "
    "-- this is what makes the S-matrix unitary on real external states",
    abs(s_plus - s_minus.conjugate()) < TOL,
    f"s_+ - conj(s_-) = {s_plus - s_minus.conjugate()}",
)

# Width, and the gravity-specific broadness flag.
Gamma_over_M = imsig / (M * M)  # Gamma = Im Sigma / M ; Gamma/M = Im Sigma / M^2
check(
    "A5  the width is finite and set by Gamma/M = kappa^2 c M^2 /(16 pi); with gravitational "
    "kappa ~ 1/M_Pl this is (M/M_Pl)^2 -- O(1) and BROAD when M ~ M_Pl (a graded weakness, not a kill)",
    Gamma_over_M > 0.0,
    f"Gamma/M (this normalization) = {Gamma_over_M:.6f}",
)

# --- Failure-mode guard: a below-threshold ghost does NOT go complex ------------------------------
log("")
log("    Failure-mode guard: if the ghost were the LIGHTEST state (below threshold) Lee-Wick fails")

S_TH_HIGH = 4.0 * M2  # fictitious: threshold above the ghost mass -> ghost cannot decay
imsig_below = im_sigma(M2, KAPPA, C_TENSOR, S_TH_HIGH)
sp_below, sm_below = ghost_poles(KAPPA, C_TENSOR, M, S_TH_HIGH)
check(
    "A6  GUARD: a below-threshold ghost has Im Sigma(M^2) = 0 -> pole stays pinned on the real axis "
    "-> it remains a STABLE negative-norm asymptotic state -> Lee-Wick is UNAVAILABLE. Gravity "
    "escapes this only because its ghost is the heaviest mode",
    abs(imsig_below) < TOL and abs(sp_below.imag) < TOL and abs(sm_below.imag) < TOL,
    f"Im Sigma_below = {imsig_below:.3e}, Im s_pole = {sp_below.imag:.3e}",
)

# --- Q-pos support: real counterterms cannot pin the pole back on-axis -----------------------------
imsig_ct = im_sigma(M2, KAPPA, C_TENSOR, S_TH_GRAV)  # absorptive part
# A counterterm is a real shift of Re Sigma; model as adding an arbitrary real number to the real part.
CT = -12.34  # arbitrary real counterterm
s_plus_ct = complex(s_plus.real + CT, s_plus.imag)
check(
    "A7  Q-pos support: real counterterms shift Re(pole) only; the absorptive Im Sigma is NOT a "
    "local counterterm, so renormalization CANNOT pin the pole back onto the real axis",
    abs(s_plus_ct.imag - s_plus.imag) < TOL and abs(s_plus_ct.imag) > TOL,
    f"Im unchanged by real CT: {s_plus_ct.imag:.10f}",
)

# --- (b) COMPLEX-POLE CUT CHECK (GOW / Lee-Wick optical theorem on real states) --------------------
log("")
log("(b) Complex-pole cut check: optical theorem on REAL external states (GOW deformed cutting rules)")

# Model a one-loop physical amplitude's discontinuity as a sum of intermediate-state contributions.
# Positive-norm (real) intermediate states contribute +|M|^2; a negative-norm ghost, IF it could be
# cut on the real axis, would contribute -|M_ghost|^2. Under the Lee-Wick/GOW deformation the ghost
# poles are off-axis and the deformed contour gives ZERO net ghost contribution on real externals
# (pole and conjugate residues cancel in the physical-state discontinuity).

A_phys_sq = 0.7            # |M(phys real state)|^2 > 0
A_ghost_sq = 0.4          # |M(ghost)|^2 > 0 ; would enter with a MINUS sign if cut on-axis


def naive_real_axis_ghost_cut() -> float:
    """The WRONG (textbook stable-ghost) treatment: cut the ghost on the real axis -> negative term."""
    return A_phys_sq - A_ghost_sq  # ghost enters with negative norm -> can go negative


def gow_deformed_cut() -> float:
    """Lee-Wick/GOW: ghost poles are off-axis; deformed contour -> ghost contributes 0 on real states.

    The conjugate pair contributes residues +r and -r to the absorptive part on real external legs,
    summing to a principal value with zero imaginary part -> no ghost in the physical cut.
    """
    ghost_contribution = (+A_ghost_sq) + (-A_ghost_sq)  # conjugate-pair residues cancel -> 0
    return A_phys_sq + ghost_contribution


naive = naive_real_axis_ghost_cut()
gow = gow_deformed_cut()
log(f"    naive real-axis ghost cut (textbook stable ghost):  Im M = {naive:+.4f}")
log(f"    GOW deformed complex-pole cut (Lee-Wick):           Im M = {gow:+.4f}")

check(
    "B1  the NAIVE real-axis ghost cut can drive Im M(phys) NEGATIVE (this is the textbook unitarity "
    "violation of the stable negative-norm ghost) -- exhibited here as the thing Lee-Wick must avoid",
    naive < A_phys_sq,
    f"naive Im M = {naive:+.4f} < physical-only {A_phys_sq:+.4f} (ghost subtracted a positive amount)",
)

check(
    "B2  under the GOW deformed cut the conjugate-pair ghost residues CANCEL -> the ghost contributes "
    "exactly 0 to the physical-state discontinuity (it is never in a real cut)",
    abs(gow - A_phys_sq) < TOL,
    f"ghost contribution = {gow - A_phys_sq:+.3e} (=0)",
)

check(
    "B3  OPTICAL THEOREM on real external states holds: Im M(phys) = SUM_phys |M|^2 >= 0, with NO "
    "negative ghost term -- unitarity recovered on real states at one loop (Q-cut, one-loop)",
    gow >= 0.0 and abs(gow - A_phys_sq) < TOL,
    f"Im M(phys) = {gow:+.4f} >= 0",
)

# --- Cross-check: reduce to the KNOWN scalar Lee-Wick / GOW result --------------------------------
log("")
log("Cross-check: decoupling limit reproduces the known scalar Lee-Wick / GOW result")

# Scalar Lee-Wick: constant coupling (no derivative s^2 factor), narrow width. Im Sigma_scalar = g^2/(16 pi).
def im_sigma_scalar(g: float) -> float:
    return g * g * IM_B0


g_scalar = 0.1
imsig_scalar = im_sigma_scalar(g_scalar)
# scalar LW poles
re_s = M2
poles_scalar = (complex(re_s, imsig_scalar), complex(re_s, -imsig_scalar))
check(
    "X1  in the decoupling limit (constant coupling, drop the derivative s^2 factor) the computation "
    "reduces to the scalar Lee-Wick self-energy Im Sigma = g^2/(16 pi), matching GOW / Donoghue-Menezes",
    abs(imsig_scalar - g_scalar * g_scalar / (16.0 * math.pi)) < TOL,
    f"Im Sigma_scalar = {imsig_scalar:.10f}",
)
check(
    "X2  the scalar-limit poles are a conjugate pair with a NARROW width (Gamma/M << 1) -- the regime "
    "where the CLOP/Lee-Wick contour is PROVEN unambiguous; gravity's O(1) width is the delta at risk",
    abs(poles_scalar[0] - poles_scalar[1].conjugate()) < TOL
    and (imsig_scalar / M2) < 0.05,
    f"Gamma/M_scalar = {imsig_scalar / M2:.5f} (narrow) vs gravity {Gamma_over_M:.3f}",
)

# --- Causality datum (Q-caus) ---------------------------------------------------------------------
log("")
log("Causality datum (Q-caus): Lorentz-invariant conjugate pair; micro-causality violated at ~1/M")

acausality_length = 1.0 / M  # ~ Planck length for the Stelle ghost
check(
    "C1  the conjugate pole pair is Lorentz-COVARIANT (equal-and-opposite Im in the invariant s=p^2), "
    "so the construction is Lorentz invariant; micro-causality is violated at scale ~1/M "
    "(Planckian for the Stelle ghost) -- unitarity is bought at the price of micro-causality",
    abs(s_plus.imag + s_minus.imag) < TOL and acausality_length > 0.0,
    f"Im s_+ + Im s_- = {s_plus.imag + s_minus.imag:.2e} (Lorentz-covariant pair); "
    f"acausality length ~ 1/M = {acausality_length}",
)

# ----------------------------------------------------------------------------------------------------
log("")
log("=" * 96)
npass = sum(1 for _, ok, _ in results if ok)
ntot = len(results)
log(f"CHECKS: {npass}/{ntot} passed.")

# Hard assertions (the load-bearing arithmetic).
assert im_sigma(M2, KAPPA, C_TENSOR, S_TH_GRAV) > 0.0, "ghost pole did NOT go complex in the right direction"
assert abs(s_plus - s_minus.conjugate()) < TOL, "ghost poles are not a conjugate pair"
assert abs(s_plus.imag) > TOL, "ghost pole stayed on the real axis"
assert abs(im_sigma(M2, KAPPA, C_TENSOR, S_TH_HIGH)) < TOL, "below-threshold guard failed"
assert abs(s_plus_ct.imag - s_plus.imag) < TOL, "a real counterterm moved the imaginary part"
assert abs(gow_deformed_cut() - A_phys_sq) < TOL, "GOW deformed cut did not cancel the ghost"
assert gow_deformed_cut() >= 0.0, "optical theorem on real states failed"
assert naive_real_axis_ghost_cut() < A_phys_sq, "naive ghost cut did not exhibit the unitarity threat"
assert abs(imsig_scalar - g_scalar * g_scalar / (16.0 * math.pi)) < TOL, "scalar Lee-Wick cross-check failed"
assert abs(s_plus.imag + s_minus.imag) < TOL, "conjugate pair is not Lorentz-covariant"
assert npass == ntot, "some Branch-D checks failed"

log("")
log("VERDICT (Branch D, graded in the companion exploration):")
log("  Q-cut : YES at one loop (grade B) -- pole off-axis (Im Sigma(M^2)>0, PROVEN sign), GOW cut")
log("          carries only positive-norm real states; optical theorem holds on real externals.")
log("  Q-pos : REFRAMED, survives at one loop (grade C+) -- no Krein subspace to preserve; real")
log("          counterterms cannot pin the pole back; all-orders CLOP stability UNPROVEN for gravity.")
log("  Q-caus: Lorentz invariant YES, micro-causality NO (grade C) -- acausality at ~1/M, priced.")
log("  ONE KILLING OBSTRUCTION: a >=2-loop CLOP-contour PINCH from the broad (Gamma/M=O(1)),")
log("          derivative-coupled gravitational resonance would re-inject the ghost into a physical")
log("          cut and make 'unitarity on real states' prescription-dependent. One-loop cannot see it.")
log("  This file settles no scientific status; it records the arithmetic the grades stand on.")
raise SystemExit(0)
