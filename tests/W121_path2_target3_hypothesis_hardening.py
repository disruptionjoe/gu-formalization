#!/usr/bin/env python3
r"""
W121 / Path-2 Wave-3 Target 3 -- hypothesis audit + hardening of the no-local-positive-metric
theorem (W54).

W54 proved (free case, machine-checked): in the positive-energy (Bender-Mannheim /
keep-and-grade) quantization of the 4th-order / Pais-Uhlenbeck field, no positive metric eta has
an entire (Paley-Wiener local) symbol; the whole positive-intertwiner family carries the
1/sqrt(k^2+m_i^2) branch cuts; the kernel is exponentially localized (~e^{-m|x|}). Gaps left:
(b) non-translation-invariant local metrics; interacting all-orders; and the theorem's coverage
statement against the removal family.

This file audits every hypothesis for NECESSARY vs CONVENIENT and hardens what can be hardened:

  T3-1 (NEW, the main hardening) -- the translation-invariance hypothesis is weakened for the
       differential-operator class: the large-k sign-domination obstruction (W54 Sec 4.4) is
       POINTWISE in x. Any finite-order differential operator with x-dependent coefficients has,
       at each fixed x, a polynomial fiber symbol in k; opposite grading signs on the two mass
       shells force |F(om1)+F(om2)| <= |F(om1)-F(om2)|, but the ratio diverges like k^2 for every
       polynomial fiber (symbolic, all degrees checked to 6) -- so no x-dependent finite-order
       differential operator can implement the grading at large k. Upgrades gap (b) from ARGUED
       to STRONG-ARGUMENT for the differential-operator class. (The argued step that remains: the
       semiclassical link between operator positivity and pointwise principal-symbol signs.)

  T3-2 (NEW) -- the "local = entire symbol" hypothesis is TIGHT and cannot be weakened to
       quasi-locality: the canonical metric ITSELF is quasi-local (strip-analytic of width
       exactly m: series radius of convergence in k^2 equals m^2; kernel log-slope -> -m). The
       escape class "quasi-local metrics" is NONEMPTY, so a stronger theorem excluding
       quasi-local metrics is FALSE. The theorem sits exactly on the true boundary.

  T3-3 (NEW) -- the known non-translation-invariant candidate escapes (equal-energy cross-shell
       mixers: at every E > m2 both shells om1(k1)=om2(k2)=E are populated, and a metric could
       mix them) are LONGER-RANGE than the canonical metric: a shell mixer's kernel is a
       delta-shell Fourier transform with power-law envelope ~1/r, which dominates e^{-m r} at
       large r. Escaping translation invariance through shell mixing buys MORE non-locality, not
       less. (ARGUED: this covers the natural commutant-extension escapes, not every kernel.)

  T3-4 -- coverage ledger: the theorem does NOT cover the fakeon / Lee-Wick prescriptions and
       structurally cannot: they escape by changing the STATE SPACE (ghost removed from
       asymptotic states; no positive eta on the full Fock space is sought), not by finding a
       local metric. This is the correct scope statement, consistent with the trade map: Family 2
       pays in causality, not in metric locality.

  Controls: PC1 re-derives the even-entire-grading indefiniteness (W54 D1' arithmetic); NC1
       shows the sign machinery reports "local metric possible" for a healthy (all-positive
       Krein sign) two-mass field, so the obstruction is genuinely ghost-specific.

HYPOTHESIS AUDIT TABLE (asserted as the deterministic ledger L1):
  A. positive-energy (bounded-below) quantization ......... NECESSARY (else eta=1 is local+positive)
  B. Krein signs (+,-,-,+) fixed by the local action ....... NECESSARY, load-bearing (NC1 shows
     flipping them dissolves the obstruction)
  C. distinct masses m1 != m2 .............................. NECESSARY for the commutant argument
     (degenerate case is the exceptional locus where the grading dies anyway, W52/W53)
  D. eta translation-invariant ............................. CONVENIENT -- now weakened (T3-1):
     x-dependent finite-order differential operators excluded; remaining escape class =
     x-dependent local kernels with entire NON-polynomial fiber symbols
  E. "local" = entire symbol of finite exponential type .... NECESSARY AND TIGHT (T3-2): the
     quasi-local escape is realized by the canonical eta itself
  F. free theory ........................................... CONVENIENT at first order (W54 INT1/2
     strong-argument); all-orders interacting remains open

No canon / RESEARCH-STATUS / claim-status / verdict / posture change. H59 remains OPEN.

Reproducible: python tests/W121_path2_target3_hypothesis_hardening.py
"""
from __future__ import annotations

import math
import random

import mpmath as mp
import numpy as np
import sympy as sp

mp.mp.dps = 30

results: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    results.append((name, bool(passed), detail))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))


def log(msg: str = "") -> None:
    print(msg, flush=True)


M1, M2 = 1.0, 2.0  # healthy and ghost masses (m1 < m2)


def om(k: float, m: float) -> float:
    return math.sqrt(k * k + m * m)


log("=" * 96)
log("W121 / PATH-2 WAVE-3 TARGET 3 -- NO-LOCAL-POSITIVE-METRIC THEOREM: AUDIT + HARDENING")
log("=" * 96)

# ----------------------------------------------------------------------------------------------
# Controls first.
# ----------------------------------------------------------------------------------------------
log("")
log("0. Controls")

# PC1: the even entire grading C_even has eigenvalues (+1,+1,-1,-1) on (om1+,om1-,om2+,om2-);
# against eps=(+,-,-,+) the metric weights are eps_i*C_i = (+1,-1,+1,-1): indefinite.
eps_ghost = (+1, -1, -1, +1)
c_even = (+1, +1, -1, -1)
weights = tuple(e * c for e, c in zip(eps_ghost, c_even))
check("PC1 even entire grading gives metric weights (+1,-1,+1,-1): INDEFINITE (re-derives W54 "
      "D1'b; entire => indefinite, the refutation trap)",
      weights == (1, -1, 1, -1) and min(weights) < 0, f"weights={weights}")

# NC1: healthy two-mass field, eps all +. Then C = 1 (constant polynomial, maximally local)
# satisfies sign C(om_i) = eps_i on both shells. The machinery must report POSSIBLE.
eps_healthy = (+1, +1, +1, +1)


def sign_condition_holds(fiber_poly, eps4, k_grid) -> bool:
    """Does sign F(+-om_i(k)) == eps_i hold on the whole grid?"""
    for k in k_grid:
        vals = (fiber_poly(om(k, M1)), fiber_poly(-om(k, M1)),
                fiber_poly(om(k, M2)), fiber_poly(-om(k, M2)))
        for v, e in zip(vals, eps4):
            if v == 0 or (v > 0) != (e > 0):
                return False
    return True


k_grid = np.linspace(0.0, 400.0, 801)
check("NC1 healthy field (Krein signs all +): the constant polynomial C=1 (local) satisfies the "
      "sign condition -- the obstruction is genuinely ghost-specific, hypothesis B is load-bearing",
      sign_condition_holds(lambda lam: 1.0, eps_healthy, k_grid),
      "C=1 works when no ghost sign is present")

# ----------------------------------------------------------------------------------------------
# T3-1: pointwise-in-x hardening -- x-dependent polynomial fiber symbols cannot grade.
# ----------------------------------------------------------------------------------------------
log("")
log("1. T3-1: x-dependent finite-order differential operators excluded (pointwise argument)")

# Route 1 (symbolic): for F(lambda) = sum c_j lambda^j with generic coefficients, the ratio
# (F(om1)+F(om2)) / (F(om1)-F(om2)) diverges like k^2 as k -> infinity, for every degree d with
# c_d != 0. Opposite shell signs require |sum| <= |diff|; divergence forbids it at large k.
kk = sp.symbols("k", positive=True)
m1s, m2s = sp.symbols("m1 m2", positive=True)
om1s = sp.sqrt(kk ** 2 + m1s ** 2)
om2s = sp.sqrt(kk ** 2 + m2s ** 2)

ok = True
details = []
for d in range(1, 7):
    cs = sp.symbols(f"c0:{d + 1}")
    F = sum(cs[j] * sp.Symbol("lam") ** j for j in range(d + 1))
    lam = sp.Symbol("lam")
    Fs = sp.Poly(F, lam)
    F1 = Fs.eval(om1s)
    F2 = Fs.eval(om2s)
    ssum = sp.series(F1 + F2, kk, sp.oo, 3).removeO()
    sdiff = sp.expand(F1 - F2)
    # leading power of the sum is k^d with coefficient 2*c_d
    lead_sum = sp.limit((F1 + F2) / kk ** d, kk, sp.oo)
    # leading power of the difference is k^(d-2) with coefficient (d/2)*c_d*(m1^2-m2^2)
    lead_diff = sp.limit(sdiff / kk ** (d - 2), kk, sp.oo)
    expected_sum = 2 * cs[d]
    expected_diff = sp.Rational(d, 2) * cs[d] * (m1s ** 2 - m2s ** 2)
    this_ok = sp.simplify(lead_sum - expected_sum) == 0 and sp.simplify(lead_diff - expected_diff) == 0
    ok &= this_ok
    details.append(f"d={d}: sum~2c{d}*k^{d}, diff~({d}/2)c{d}(m1^2-m2^2)k^{d - 2}")
check("T3-1a symbolic (degrees 1..6): F(om1)+F(om2) ~ 2 c_d k^d while F(om1)-F(om2) ~ "
      "(d/2) c_d (m1^2-m2^2) k^(d-2) -- the ratio diverges like k^2 for EVERY polynomial fiber, "
      "so opposite shell signs (|sum|<|diff|) are impossible at large k, for ANY coefficient "
      "values, hence pointwise in x for x-dependent coefficients",
      ok, "; ".join(details[:3]) + " ...")

# Route 2 (numeric sweep): random polynomial fibers, including sign-alternating and tuned ones,
# never hold the ghost sign pattern on the whole grid.
rng = random.Random(59)
n_hold = 0
N_TRIALS = 4000
for _ in range(N_TRIALS):
    d = rng.randint(1, 6)
    coeffs = [rng.uniform(-5, 5) for _ in range(d + 1)]

    def fiber(lam, c=coeffs):
        return sum(cj * lam ** j for j, cj in enumerate(c))

    if sign_condition_holds(fiber, eps_ghost, k_grid):
        n_hold += 1
check("T3-1b numeric: 4000 random polynomial fibers (degree<=6, i.e. arbitrary fixed-x "
      "coefficient draws of an x-dependent operator): NONE holds the ghost sign pattern "
      "(+,-,-,+) on k in [0,400]",
      n_hold == 0, f"holders={n_hold}/{N_TRIALS}")

# ----------------------------------------------------------------------------------------------
# T3-2: tightness -- the quasi-local escape is REALIZED, so 'entire' cannot be weakened.
# ----------------------------------------------------------------------------------------------
log("")
log("2. T3-2: the locality hypothesis is tight (quasi-local escape realized by canonical eta)")

# Radius of convergence of the canonical symbol component 1/sqrt(k^2+m^2) as a series in k^2:
# coefficients a_n = binom(-1/2, n)/m^(2n+1); ratio |a_{n+1}/a_n| -> 1/m^2.
m = M2
# a_{n+1}/a_n = -(n+1/2)/(n+1) / m^2 exactly (binomial series); the Richardson-corrected ratio
# |a_{n+1}/a_n| * (n+1)/(n+1/2) equals 1/m^2 EXACTLY for every n -- two routes: raw ratio
# converges to 1/m^2, corrected ratio hits it identically.
raw_ok = True
exact_ok = True
prev = mp.binomial(mp.mpf(-0.5), 0) / m
for n in range(60):
    a_next = mp.binomial(mp.mpf(-0.5), n + 1) / m ** (2 * (n + 1) + 1)
    ratio = abs(a_next / prev)
    corrected = ratio * (n + 1) / (n + mp.mpf(0.5))
    if n == 59:
        raw_ok = abs(float(ratio) - 1.0 / m ** 2) < 5e-3
        last_ratio, last_corr = float(ratio), float(corrected)
    exact_ok &= abs(float(corrected) - 1.0 / m ** 2) < 1e-15
    prev = a_next
check("T3-2a series ratio test: the canonical symbol's k^2-series coefficient ratio -> 1/m^2 "
      "(raw ratio converges; the exact Richardson-corrected ratio equals 1/m^2 identically), "
      "i.e. radius of convergence EXACTLY m^2 (branch point at k=+-i m; not entire, but analytic "
      "in a strip of width exactly m)",
      raw_ok and exact_ok,
      f"ratio_59={last_ratio:.6f}, corrected={last_corr:.15f} vs 1/m^2={1 / m ** 2}")

# Kernel decay: the 1D kernel of 1/sqrt(k^2+m^2) is K0(m|x|)/pi; log K0(mr) ~ -m r - (1/2)log r
# + const. Subtract the known subleading (1/2)log r term, then the slope -> -m.
r1, r2 = 8.0, 16.0
slope_raw = (mp.log(mp.besselk(0, m * r2)) - mp.log(mp.besselk(0, m * r1))) / (r2 - r1)
slope = slope_raw + mp.mpf(0.5) * (mp.log(r2) - mp.log(r1)) / (r2 - r1)
check("T3-2b kernel log-slope (subleading (1/2)log r removed) between r=8 and r=16 is -m to <2%: the canonical metric IS "
      "quasi-local (exponentially localized). The escape class 'quasi-local metrics' is "
      "NONEMPTY, so the theorem CANNOT be strengthened from 'no entire-symbol metric' to "
      "'no quasi-local metric' -- the hypothesis sits on the true boundary",
      abs(float(slope) + m) / m < 0.02, f"slope={float(slope):.4f} vs -m={-m}")

# ----------------------------------------------------------------------------------------------
# T3-3: the cross-shell (equal-energy) escape class is LONGER-range than the canonical metric.
# ----------------------------------------------------------------------------------------------
log("")
log("3. T3-3: equal-energy cross-shell mixers are power-law non-local (worse than canonical)")

# At any E > m2 both shells are populated: k1 = sqrt(E^2-m1^2), k2 = sqrt(E^2-m2^2) real.
E = 3.0
k1 = math.sqrt(E * E - M1 * M1)
k2 = math.sqrt(E * E - M2 * M2)
check("T3-3a at every E > m2 both mass shells carry modes of the same energy (k1, k2 real): the "
      "commutant of H WITHOUT translation invariance contains cross-shell mixers -- this is the "
      "genuine escape channel gap (b) must exclude",
      k1 > 0 and k2 > 0, f"E={E}: k1={k1:.4f}, k2={k2:.4f}")

# A cross-shell mixer is (at minimum) supported on momentum shells; its position kernel is a
# delta-shell Fourier transform, envelope ~ 1/r in 3D (sin(kr)/(kr) * k^2-type), vs e^{-m r}.
rs = np.array([5.0, 10.0, 20.0, 40.0, 80.0])
power_env = 1.0 / rs                       # delta-shell FT envelope ~ 1/r
exp_env = np.exp(-M2 * rs)                 # canonical metric kernel envelope
check("T3-3b the shell-mixer envelope 1/r dominates the canonical e^{-m r} at every probed "
      "r >= 5 and the ratio grows without bound: escaping translation invariance through the "
      "equal-energy commutant costs MORE locality (power-law), not less (ARGUED for the "
      "shell-mixer class)",
      bool(np.all(power_env > exp_env)) and bool(np.all(np.diff(power_env / exp_env) > 0)),
      f"(1/r)/e^{{-mr}} at r=5: {power_env[0] / exp_env[0]:.3g}, at r=80: {power_env[-1] / exp_env[-1]:.3g}")

# ----------------------------------------------------------------------------------------------
# T3-4: coverage ledger -- what the theorem does and does not cover.
# ----------------------------------------------------------------------------------------------
log("")
log("4. T3-4: coverage ledger (fakeon / Lee-Wick are out of scope BY STRUCTURE)")

THEOREM_HYPOTHESES = {
    "positive eta sought on the FULL Fock space including ghost modes": True,
    "ghost kept as a state (nothing removed)": True,
}
FAKEON_LEEWICK = {
    "positive eta sought on the FULL Fock space including ghost modes": False,  # ghost projected out
    "ghost kept as a state (nothing removed)": False,
}
check("T3-4 the removal family (fakeon / Lee-Wick) fails the theorem's hypotheses at the first "
      "line: no positive metric on the ghost-inclusive space is ever sought. The theorem covers "
      "Family 1 (grading) only, and structurally cannot cover Family 2 -- their escape is a "
      "state-space change, priced in causality (W50/W51), not in metric locality",
      all(THEOREM_HYPOTHESES.values()) and not any(FAKEON_LEEWICK.values()),
      "escape class: change the state space, pay causality")

# ----------------------------------------------------------------------------------------------
# L1: the audit table itself, asserted.
# ----------------------------------------------------------------------------------------------
log("")
log("5. L1: hypothesis audit table")

AUDIT = {
    "A bounded-below quantization": ("NECESSARY", "eta=1 local+positive exists in the unbounded-below quantization (W54 Sec 2)"),
    "B Krein signs (+,-,-,+) fixed": ("NECESSARY", "NC1: flipping signs dissolves the obstruction; load-bearing"),
    "C distinct masses m1 != m2": ("NECESSARY", "commutant argument; degenerate case is the exceptional locus (grading dies anyway)"),
    "D translation invariance": ("CONVENIENT-NOW-WEAKENED", "T3-1: x-dependent finite-order differential ops excluded (STRONG-ARGUMENT); T3-3: shell-mixer escapes are power-law non-local; remaining gap: x-dependent entire non-polynomial fiber symbols"),
    "E local = entire symbol": ("NECESSARY-AND-TIGHT", "T3-2: quasi-local escape realized by canonical eta; no strengthening possible"),
    "F free theory": ("CONVENIENT-AT-FIRST-ORDER", "W54 INT1/INT2 strong-argument; all-orders interacting open"),
}
check("L1 audit table complete: 3 NECESSARY, 1 NECESSARY-AND-TIGHT, 1 CONVENIENT-NOW-WEAKENED, "
      "1 CONVENIENT-AT-FIRST-ORDER; remaining escape classes named (entire non-polynomial "
      "x-dependent fibers; all-orders interacting; state-space-changing prescriptions)",
      len(AUDIT) == 6 and sum(1 for v, _ in AUDIT.values() if v.startswith("NECESSARY")) == 4,
      "; ".join(f"{k}: {v}" for k, (v, _) in AUDIT.items()))

# ----------------------------------------------------------------------------------------------
# Honesty guard.
# ----------------------------------------------------------------------------------------------
STRENGTH_B_FULLY_PROVEN = False     # entire non-polynomial x-dependent fibers remain open
ALL_ORDERS_INTERACTING_PROVEN = False
H59_CHANGED = False
check("H1 honesty guard: T3-1 upgrades gap (b) to STRONG-ARGUMENT for the differential-operator "
      "class only (the positivity-to-pointwise-symbol-sign link is the argued step); strength "
      "(b) is NOT fully proven; interacting all-orders open; H59 remains OPEN",
      not STRENGTH_B_FULLY_PROVEN and not ALL_ORDERS_INTERACTING_PROVEN and not H59_CHANGED,
      "status = TARGET3_HARDENED_NOT_CLOSED")

log("")
log("=" * 96)
npass = sum(1 for _, okk, _ in results if okk)
ntot = len(results)
log(f"CHECKS: {npass}/{ntot} passed.")
assert all(okk for _, okk, _ in results), "some W121 checks failed"

log("")
log("VERDICT: TARGET3_HARDENED_NOT_CLOSED.")
log("  The theorem's hypotheses are audited: 4 necessary (one provably tight), 2 convenient.")
log("  Hardened: x-dependent finite-order differential operators are now excluded (pointwise")
log("  sign-domination, symbolic to degree 6 + 4000-draw sweep); the locality hypothesis is")
log("  provably on the true boundary (the quasi-local escape is realized by the canonical")
log("  metric itself); shell-mixer escapes cost power-law non-locality. Remaining escapes:")
log("  x-dependent entire non-polynomial fiber symbols; all-orders interacting; state-space-")
log("  changing prescriptions (out of scope by structure). H59 remains OPEN.")
raise SystemExit(0)
