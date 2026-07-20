#!/usr/bin/env python3
"""PP3 risk-register calculator -- where the OFFICIAL DR2-era w0waCDM
central values sit relative to the frozen PP3 band. Pure arithmetic on
published numbers; no likelihoods, no GU machinery, no solver.

CHANNEL: Lane 2 prediction packaging (PP3 risk register; fan-out from the
         frozen packet).
DESIGN:  explorations/pp3-risk-register-2026-07-20.md
FROZEN PACKET (never touched): explorations/prediction-package-pp3-de-curve-family-2026-07-20.md

ZERO-WEIGHT GUARD. Every published number below is PRE-FREEZE known data
(the DESI DR2 paper is dated March 2025; PP3 froze 2026-07-20 and consumed
the DR2 BAO vector in its construction). Nothing computed here carries
confirmation or kill weight for PP3. This script quantifies RISK EXPOSURE
only: at how many (naively propagated) sigma the published central values
sit from the frozen band, so that when a FUTURE release lands, the register
already says what "the central values held" would mean.

SOURCE OF THE PUBLISHED NUMBERS (fetched 2026-07-20, arXiv:2503.14738v2,
"DESI DR2 Results II: Measurements of Baryon Acoustic Oscillations and
Cosmological Constraints", Section VII, eqs. (25)-(28); significances from
Table 6 of the same paper):

  DESI+CMB            : w0 = -0.42  +/- 0.21 , wa = -1.75 +/- 0.58        (eq. 25, 3.1 sigma)
  DESI+CMB+Pantheon+  : w0 = -0.838 +/- 0.055, wa = -0.62 +0.22 -0.19     (eq. 26, 2.8 sigma)
  DESI+CMB+Union3     : w0 = -0.667 +/- 0.088, wa = -1.09 +0.31 -0.27     (eq. 27, 3.8 sigma)
  DESI+CMB+DESY5      : w0 = -0.752 +/- 0.057, wa = -0.86 +0.23 -0.20     (eq. 28, 4.2 sigma)

The paper quotes NO numeric w0-wa correlation coefficient in Section VII;
the propagation below therefore IGNORES the (known, strong, negative)
w0-wa correlation. Because both partial derivatives of the slope
r = wa/(w0+1) are positive at every central point below (wa < 0), a
negative covariance term would SHRINK sigma_r -- i.e. the uncorrelated
sigma distances printed here likely UNDERSTATE the slope tension. Stated,
not corrected: no correlation value is invented.

FROZEN PP3 CONSTANTS (from the packet, v0.2, 2026-07-20):
  slope band  wa/(w0+1) in [-1.33, -1.00]
  K2 kill band (35% predeclared tolerance): [-1.80, -0.65]
  segment      w0+1 <= 0.054  (CPL convention, image of f0 <= 0.027)
  K3 kill      w0+1  > 0.06

Deterministic; stdlib math only; exit 0.
"""
from __future__ import annotations

import math
import sys

RESULTS = []


def check(tag, name, ok, detail=""):
    RESULTS.append((tag, name, bool(ok)))
    line = f"[{tag}] {'PASS' if ok else 'FAIL'}  {name}"
    if detail:
        line += f"   ({detail})"
    print(line)
    return ok


# ----------------------------------------------------------------------
# Frozen constants: published DR2-era w0waCDM fits (arXiv:2503.14738v2,
# Section VII eqs. 25-28; sigma-preference column from Table 6).
# Fields: (w0, sigma_w0, wa, sigma_wa_plus, sigma_wa_minus, sigma_pref)
# ----------------------------------------------------------------------
COMBOS = {
    "DESI+CMB":           (-0.42,  0.21,  -1.75, 0.58, 0.58, 3.1),
    "DESI+CMB+Pantheon+": (-0.838, 0.055, -0.62, 0.22, 0.19, 2.8),
    "DESI+CMB+Union3":    (-0.667, 0.088, -1.09, 0.31, 0.27, 3.8),
    "DESI+CMB+DESY5":     (-0.752, 0.057, -0.86, 0.23, 0.20, 4.2),
}

# Frozen PP3 band (packet v0.2; NOT recomputed here -- copied constants).
BAND_LO, BAND_HI = -1.33, -1.00          # slope band
K2_LO, K2_HI = -1.80, -0.65              # widened kill band (35% tolerance)
SEG_CEIL = 0.054                          # w0+1 segment ceiling (CPL)
K3_CEIL = 0.06                            # K3 amplitude kill threshold


def slope_and_sigma(w0, sw0, wa, swa):
    """Central slope r = wa/(w0+1) and first-order sigma_r, correlation
    ignored (none published). Analytic partials."""
    A = w0 + 1.0
    r = wa / A
    dr_dwa = 1.0 / A
    dr_dw0 = -wa / A ** 2
    sr = math.sqrt((dr_dwa * swa) ** 2 + (dr_dw0 * sw0) ** 2)
    return A, r, sr


def slope_sigma_numerical(w0, sw0, wa, swa, h=1e-7):
    """Independent recompute of sigma_r via numerical partials."""
    def r_of(x, y):
        return y / (x + 1.0)
    dw0 = (r_of(w0 + h, wa) - r_of(w0 - h, wa)) / (2 * h)
    dwa = (r_of(w0, wa + h) - r_of(w0, wa - h)) / (2 * h)
    return math.sqrt((dwa * swa) ** 2 + (dw0 * sw0) ** 2)


rows = {}
print("== PP3 risk register: DR2-era central values vs the frozen band ==")
print(f"{'combo':22s} {'w0+1':>6s} {'slope':>7s} {'sig_r':>6s} "
      f"{'d(band)':>8s} {'d(K2)':>6s} {'dA(seg)':>8s} {'dA(K3)':>7s} {'z_x':>6s}")
for name, (w0, sw0, wa, swa_p, swa_m, _pref) in COMBOS.items():
    swa = 0.5 * (swa_p + swa_m)          # symmetrized (limitation, stated)
    A, r, sr = slope_and_sigma(w0, sw0, wa, swa)
    d_band = (BAND_LO - r) / sr          # sigma below the nearest band edge
    d_k2 = (K2_LO - r) / sr              # sigma below the widened K2 edge
    dA_seg = (A - SEG_CEIL) / sw0        # sigma above the segment ceiling
    dA_k3 = (A - K3_CEIL) / sw0          # sigma above the K3 threshold
    z_x = 1.0 / (1.0 + A / wa) - 1.0     # implied phantom-crossing redshift
    rows[name] = dict(A=A, r=r, sr=sr, swa=swa, d_band=d_band, d_k2=d_k2,
                      dA_seg=dA_seg, dA_k3=dA_k3, z_x=z_x)
    print(f"{name:22s} {A:6.3f} {r:7.3f} {sr:6.3f} "
          f"{d_band:7.2f}s {d_k2:5.2f}s {dA_seg:7.2f}s {dA_k3:6.2f}s {z_x:6.3f}")
print()

# ----------------------------------------------------------------------
# [T] arithmetic self-checks (independent recomputation paths)
# ----------------------------------------------------------------------
ok = True
ok &= check("T", "identity r*(w0+1) == wa for every combo",
            all(abs(rows[n]["r"] * rows[n]["A"] - COMBOS[n][2]) < 1e-12
                for n in COMBOS))

ok &= check("T", "sigma_r: analytic partials == numerical partials (rel 1e-6)",
            all(abs(rows[n]["sr"]
                    - slope_sigma_numerical(COMBOS[n][0], COMBOS[n][1],
                                            COMBOS[n][2], rows[n]["swa"]))
                / rows[n]["sr"] < 1e-6 for n in COMBOS))

ok &= check("T", "sigma_r alt form |r|*sqrt((swa/wa)^2+(sw0/A)^2) agrees (rel 1e-12)",
            all(abs(rows[n]["sr"]
                    - abs(rows[n]["r"]) * math.sqrt(
                        (rows[n]["swa"] / COMBOS[n][2]) ** 2
                        + (COMBOS[n][1] / rows[n]["A"]) ** 2))
                / rows[n]["sr"] < 1e-12 for n in COMBOS))

ok &= check("T", "K2 band reproduces packet rule: [-1.33*1.35, -1.00*0.65] ~ [-1.80, -0.65]",
            abs(-1.33 * 1.35 - (-1.7955)) < 1e-12
            and abs(K2_LO - (-1.7955)) <= 0.005      # packet rounds -1.7955 -> -1.80
            and abs(-1.00 * 0.65 - K2_HI) < 1e-12)

ok &= check("T", "phantom-crossing z solves w0 + wa*(1-a) = -1 (residual < 1e-12)",
            all(abs(COMBOS[n][0]
                    + COMBOS[n][2] * (1.0 - 1.0 / (1.0 + rows[n]["z_x"]))
                    - (-1.0)) < 1e-12 for n in COMBOS))

# ----------------------------------------------------------------------
# [E] exposure facts (the register's content)
# ----------------------------------------------------------------------
ok &= check("E", "all four central slopes are steeper than the frozen band edge -1.33",
            all(rows[n]["r"] < BAND_LO for n in COMBOS),
            "slopes " + ", ".join(f"{rows[n]['r']:.2f}" for n in COMBOS))

ok &= check("E", "all four central slopes are steeper even than the widened K2 edge -1.80",
            all(rows[n]["r"] < K2_LO for n in COMBOS))

ok &= check("E", "slope tension ~1.1-1.8 sigma vs band edge (uncorrelated propagation)",
            all(1.0 < rows[n]["d_band"] < 2.0 for n in COMBOS),
            ", ".join(f"{rows[n]['d_band']:.2f}" for n in COMBOS))

ok &= check("E", "all four central amplitudes exceed the segment ceiling 0.054 AND the K3 threshold 0.06",
            all(rows[n]["A"] > K3_CEIL for n in COMBOS),
            "w0+1 " + ", ".join(f"{rows[n]['A']:.3f}" for n in COMBOS))

ok &= check("E", "amplitude tension ~1.9-3.4 sigma vs segment ceiling (w0 marginal)",
            all(1.8 < rows[n]["dA_seg"] < 3.5 for n in COMBOS),
            ", ".join(f"{rows[n]['dA_seg']:.2f}" for n in COMBOS))

ok &= check("E", "every central CPL curve crosses w = -1 at z ~ 0.35-0.50 (K1-relevant if confirmed pointwise)",
            all(0.35 < rows[n]["z_x"] < 0.50 for n in COMBOS),
            ", ".join(f"{rows[n]['z_x']:.2f}" for n in COMBOS))

n_t = sum(1 for tag, _, r in RESULTS if tag == "T" and r)
n_e = sum(1 for tag, _, r in RESULTS if tag == "E" and r)
n_all = len(RESULTS)
print()
print(f"HEADLINE: {n_t} [T] + {n_e} [E] = {n_all} checks pass; DR2-era "
      f"central values sit OUTSIDE the frozen PP3 band on both axes -- "
      f"slopes -3.0 to -3.8 vs [-1.33, -1.00] (~1.1-1.8 sigma, "
      f"correlation-ignored, likely understated) and amplitudes w0+1 = "
      f"0.16-0.58 vs <= 0.054 (~1.9-3.4 sigma in the w0 marginal); if a "
      f"FUTURE release confirms these central values at >= 3 sigma, K3 and "
      f"K2 fire (K1 too via the implied phantom crossing at z ~ 0.4). "
      f"ZERO confrontation weight: all inputs are pre-freeze known data.")

sys.exit(0 if ok and n_all == n_t + n_e else 1)
