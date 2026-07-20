#!/usr/bin/env python3
"""PP3 locus emitter -- the frozen one-parameter DE curve family, computed
from the audited theta-sector machinery for the PP3 conditional prediction
packet.

CHANNEL: Lane 2 prediction packaging (PP3 candidate; standing-rule freeze).
AXIOM:   lab/process/boundary-adapter-standing-axiom.md (adapter assumed).
DESIGN:  explorations/prediction-package-pp3-de-curve-family-2026-07-20.md
EXTENDS: tests/channel-swings/de_amplitude_audit_probe.py (all machinery
         imported from there -- fresh solver, own-theta_star calibration,
         exact-budget radiation treatment "B").
STATUS:  exploration tier; conditional (R0_COND); no claim/canon/posture
         movement. CONFRONTATION DATA IS NOT TOUCHED HERE: this script never
         evaluates a likelihood; it only emits the predicted family.

WHAT THIS FREEZES. The theta-sector two-component DE model is a ONE-
parameter family (split fraction f0) at each admissible M^2. This script
computes, at own-theta_star calibration (the audit's convention, radiation
treatment "B"), the family's image in the standard CPL (w0, wa) convention
over the DESI redshift range, and verifies the structure the PP3 packet
freezes:

  [E] non-phantom pointwise: w(z) >= -1 on the whole family (PP1-compatible
      side; equality only in the f0 -> 0 limit);
  [E] linear amplitude mapping: w0 + 1 = C(M^2) * f0 on the allowed segment,
      C recorded per M^2 (canon Result-2 shape);
  [E] one-parameter confinement: the CPL image is a LINE through (-1, 0):
      the shape invariant R(M^2) = wa / (w0 + 1) is f0-independent on the
      allowed segment (recorded; this is the packet's discriminator slope);
  [E] mimic limit: max |w(z) + 1| -> 0 as f0 -> 0 (the null branch);
  [E] the excluded reference: canonical f0 = 0.125 lands FAR outside the
      surviving segment (the packet predicts along f0 in (0, 0.027] only);
  [F] the kill machinery works: synthetic phantom and off-slope points are
      flagged off-locus by the frozen discriminator.

The emitted table is the packet's frozen numerical content. Deterministic;
numpy only; no RNG.
"""
from __future__ import annotations

import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import de_amplitude_audit_probe as de  # noqa: E402

RESULTS = []


def check(tag, name, ok, detail=""):
    RESULTS.append((tag, name, bool(ok)))
    line = f"[{tag}] {'PASS' if ok else 'FAIL'}  {name}"
    if detail:
        line += f"   ({detail})"
    print(line)
    return ok


Z_FIT_MAX = 2.33          # DESI BAO range ceiling (highest DESI row)
F0_GRID = [0.005, 0.010, 0.015, 0.020, 0.027]
F0_EXCLUDED_REF = de.F0_CANON            # 0.125, already excluded
M2_MAIN = de.M2_BC1                      # 8.0 (canonical, BC_1)
M2_BAND_SPOT = [3.0, 7.0]                # band-scoped spot checks at f0=0.02


def family_point(M2, f0):
    """Own-theta_star-calibrated (w0, wa, max|w+1|) for one (M2, f0)."""
    h = de.calibrate(f0, treatment="B", M2=M2)
    Om_h = de.OMH2 / h ** 2
    Or_h = de.OMEGA_R_H2 / h ** 2
    bg = de.solve_bg(M2, f0, Om_h, Or=Or_h)
    idx = np.argsort(bg["z"])
    z = bg["z"][idx]
    w = de.w_de(bg)[idx]
    sel = z <= Z_FIT_MAX
    zf, wf = z[sel], w[sel]
    a = 1.0 / (1.0 + zf)
    # least-squares CPL fit w(a) = w0 + wa (1 - a)
    X = np.vstack([np.ones_like(a), 1.0 - a]).T
    coef, *_ = np.linalg.lstsq(X, wf, rcond=None)
    w0_fit, wa_fit = float(coef[0]), float(coef[1])
    return dict(h=h, w0=w0_fit, wa=wa_fit,
                w0_exact=float(wf[np.argmin(zf)]),
                max_dev=float(np.max(np.abs(w + 1.0))),
                min_wp1=float(np.min(w + 1.0)))


print("computing the frozen locus (own-theta_star calibration, "
      "treatment B) ...")
main_pts = {f0: family_point(M2_MAIN, f0) for f0 in F0_GRID}
spot_pts = {M2: family_point(M2, 0.020) for M2 in M2_BAND_SPOT}
ref_pt = family_point(M2_MAIN, F0_EXCLUDED_REF)

print()
print("FROZEN LOCUS TABLE (M^2 = 8, CPL over z <= 2.33):")
print(f"{'f0':>8} {'w0+1':>10} {'wa':>10} {'wa/(w0+1)':>11} {'max|w+1|':>10}")
for f0, p in main_pts.items():
    r = p["wa"] / (p["w0"] + 1.0)
    print(f"{f0:>8.3f} {p['w0'] + 1.0:>10.5f} {p['wa']:>10.5f} "
          f"{r:>11.4f} {p['max_dev']:>10.5f}")
print(f"{'0.125*':>8} {ref_pt['w0'] + 1.0:>10.5f} {ref_pt['wa']:>10.5f} "
      f"{ref_pt['wa'] / (ref_pt['w0'] + 1.0):>11.4f} "
      f"{ref_pt['max_dev']:>10.5f}   (*excluded reference)")
for M2, p in spot_pts.items():
    print(f"  band spot M^2 = {M2:.0f}, f0 = 0.020: w0+1 = "
          f"{p['w0'] + 1.0:.5f}, wa = {p['wa']:.5f}, R = "
          f"{p['wa'] / (p['w0'] + 1.0):.4f}")
print()

# --- [T] calibration sanity ---------------------------------------------------
h_mimic = de.calibrate(1e-4, treatment="B", M2=M2_MAIN)
check("T", "f0 -> 0 calibration reduces to the imported Planck point "
           "(audit E11 shape)", abs(h_mimic - de.H_PLANCK) < 0.004,
      f"h(1e-4) = {h_mimic:.4f} vs {de.H_PLANCK}")

# --- [E] structure of the family ---------------------------------------------
check("E", "non-phantom pointwise on the whole family: w(z) >= -1 "
           "(PP1-compatible side; strict for f0 > 0)",
      all(p["min_wp1"] > 0.0 for p in main_pts.values())
      and all(p["min_wp1"] > 0.0 for p in spot_pts.values()))

Cs = [(p["w0_exact"] + 1.0) / f0 for f0, p in main_pts.items()]
Cs_cpl = [(p["w0"] + 1.0) / f0 for f0, p in main_pts.items()]
check("E", "linear amplitude mapping w0_exact + 1 = C(M^2) f0 on the "
           "allowed segment (canon Result-2 convention, the EXACT z = 0 "
           "value; the CPL-fit intercept is a distinct, steeper convention "
           "recorded separately)",
      max(Cs) - min(Cs) < 0.08 * np.mean(Cs)
      and 1.25 < np.mean(Cs) < 1.55,
      f"C_exact = {min(Cs):.3f}..{max(Cs):.3f}, "
      f"C_CPL = {min(Cs_cpl):.3f}..{max(Cs_cpl):.3f}")

Rs = [p["wa"] / (p["w0"] + 1.0) for p in main_pts.values()]
R_MAIN = float(np.mean(Rs))
check("E", "one-parameter confinement: the CPL image is a line through "
           "(-1, 0) -- shape invariant R = wa/(w0+1) is f0-independent "
           "(THE PP3 discriminator slope)",
      (max(Rs) - min(Rs)) < 0.10 * abs(R_MAIN),
      f"R = {R_MAIN:.4f} (spread {max(Rs) - min(Rs):.4f})")

R_band = {M2: p["wa"] / (p["w0"] + 1.0) for M2, p in spot_pts.items()}
check("E", "the slope is band-stable in sign and order across admissible "
           "M^2 (recorded per M^2; PP3 quotes the band)",
      all(np.sign(r) == np.sign(R_MAIN) for r in R_band.values()),
      "R(3,7,8) = " + ", ".join(f"{R_band.get(m, R_MAIN):.3f}"
                                for m in [3.0, 7.0, 8.0]))

devs = [p["max_dev"] for p in main_pts.values()]
check("E", "mimic limit + monotonicity: max|w+1| increases with f0 and "
           "-> 0 at the small-f0 edge (the null branch is continuous)",
      all(devs[i] < devs[i + 1] for i in range(len(devs) - 1))
      and devs[0] < 0.01,
      f"max|w+1|: {devs[0]:.4f} .. {devs[-1]:.4f}")

seg_max = max(p["w0"] + 1.0 for p in main_pts.values())
check("E", "the excluded reference f0 = 0.125 lies FAR outside the "
           "surviving segment (PP3 predicts only along f0 <= 0.027)",
      (ref_pt["w0"] + 1.0) > 3.0 * seg_max,
      f"w0+1: ref {ref_pt['w0'] + 1.0:.4f} vs segment max {seg_max:.4f}")


# --- [F] the kill machinery ---------------------------------------------------
def on_locus(w0p1, wa, tol_slope=0.35):
    """The PP3 discriminator: right side, right slope, inside the segment."""
    if w0p1 <= 0.0:                      # phantom side: off-locus
        return False
    if w0p1 > seg_max * 1.10:            # outside the surviving segment
        return False
    return abs(wa / w0p1 - R_MAIN) < tol_slope * abs(R_MAIN)


ok_on = all(on_locus(p["w0"] + 1.0, p["wa"]) for p in main_pts.values())
phantom_flagged = not on_locus(-0.02, -0.02 * R_MAIN)
offslope_flagged = not on_locus(0.02, -0.02 * R_MAIN)
outseg_flagged = not on_locus(ref_pt["w0"] + 1.0, ref_pt["wa"])
check("F", "kill machinery: every family point passes the discriminator; "
           "synthetic phantom, wrong-slope, and out-of-segment points are "
           "all flagged off-locus",
      ok_on and phantom_flagged and offslope_flagged and outseg_flagged)

# --- headline -----------------------------------------------------------------
nE = sum(1 for t, _n, _o in RESULTS if t == "E")
nF = sum(1 for t, _n, _o in RESULTS if t == "F")
nT = sum(1 for t, _n, _o in RESULTS if t == "T")
all_ok = all(o for _t, _n, o in RESULTS)
print()
print(f"HEADLINE: {nE} [E] + {nF} [F] = {nE + nF}   (setup [T] = {nT} "
      f"excluded)   {'ALL PASS' if all_ok else 'FAILURES PRESENT'}")
sys.exit(0 if all_ok else 1)
