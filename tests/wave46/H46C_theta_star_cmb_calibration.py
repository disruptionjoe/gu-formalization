#!/usr/bin/env python3
r"""H46C -- GU's OWN CMB-calibrated amplitude via the acoustic scale theta_star.
Discharges (or fails) blocker B1 of Wave 45 (H46B).

WHAT B1 IS.  H46 (tests/wave29) showed the backreacted GU H(z) is EXCLUDED on the raw
DESI DR2 BAO likelihood at the CMB-fixed amplitude (dAIC = +21.58 vs LCDM) but mildly
better than LCDM once the distance amplitude A = (c/H0)/r_d is freed for both
(dAIC = -3.17).  The freed-amplitude comparison rested on a FAIRNESS ARGUMENT (fixed
Om + the Planck amplitude).  B1 = compute GU's OWN CMB-calibrated amplitude the same
way LCDM's is fixed: impose the Planck acoustic angular scale theta_star on GU's own
H(z), with early physics unchanged, and recompute the likelihood table.

THE CALIBRATION (standard late-time-model procedure; every approximation named).
  Planck pins the ANGLE theta_star = r_star / D_M(z_star) essentially model-
  independently (100 theta_star = 1.04110 +/- 0.00031, a 0.03% measurement).  For a
  model that modifies ONLY late-time physics (GU's theta field turns on below
  z_start = 30; above it the field is frozen on the slow-roll attractor, w = -1,
  density negligible vs matter), the early universe is unchanged, so:
    * r_star (144.43 Mpc), z_star (1089.92), r_drag (147.09 Mpc), z_drag: FIXED at
      Planck values.  Legitimacy: the sound horizons depend on pre-recombination
      physics (omega_b h^2, omega_m h^2, N_eff), which GU does not touch; this is the
      standard move for late-time dark-energy models (same logic DESI applies when
      fitting w0waCDM with a CMB theta_star prior).  LIMIT: it fails for models that
      change early physics; GU-theta does not (checked: rho_theta(z=30)/rho_m(z=30)
      is asserted small below).
    * omega_m h^2 = 0.1430: FIXED (CMB-pinned).  The free parameter is h; the
      fractional Om = omega_m h^2 / h^2 floats with h.
    * Solve theta_star(h; model) = theta_star(Planck) for h.  The result is the
      model's own CMB-calibrated H0, hence its own amplitude A = (c/H0)/r_drag.
  APPROXIMATIONS (named):
    A1. Radiation is added additively, E^2 -> E^2 + Or*((1+z)^4 - 1), keeping
        E(0) = 1 exactly; the O(Or ~ 9e-5) renormalization of today's budget is
        neglected.  omega_r = omega_gamma * (1 + 0.2271*3.046), omega_gamma =
        2.4728e-5 (T0 = 2.7255 K).
    A2. The Planck base-LCDM 0.06 eV neutrino is treated as fully matter-like at all
        z (it is inside omega_m); at z ~ z_star it is semi-relativistic.  Effect on
        D_M(z_star) is ~0.1%, SHARED by the LCDM and GU pipelines.
    A3. To cancel A1/A2 pipeline systematics, the GU amplitude is reported RATIO-
        CORRECTED: the same pipeline is run for LCDM (positive control PC2 recovers
        h ~ 0.6736), and GU's calibrated h is rescaled by (0.6736 / h_LCDM_pipeline).
        Shared systematics cancel in the ratio; the residual is second order.
    A4. For z > z_start the theta density is held at its frozen z_start value
        (w = -1 attractor).  Exactly continuous with the backreacted solve at z_start
        by construction; its size vs matter at z_start is asserted < 1e-3.
    A5. The shared ABSOLUTE scale uncertainty from r_star/r_drag (~0.18%) and
        100 theta_star (~0.03%) is common to both models; central values are used and
        a +/-0.2% amplitude sensitivity band is reported for the verdict row.
    A6. omega_m h^2 sensitivity: the Planck omega_m h^2 = 0.1430 +/- 0.0011 prior is
        scanned at +/-1 and +/-2 sigma with r_star and r_drag rescaled by
        (omega_m h^2 / 0.1430)^(-0.25) (the standard sound-horizon scaling; z_star
        drift neglected).  This answers the referee question "could the omega_m h^2
        prior width rescue the calibrated point?".

WHY THE CALIBRATED SHIFT IS LARGE (the physics, pre-empting the "bug?" reading).
  theta_star is famously INSENSITIVE to h at fixed omega_m h^2 (this pipeline
  measures dln theta_star / dln h ~ 0.19 for LCDM).  GU's theta component adds
  dark-energy density in the past (matter-like <w> = 0 below z_osc ~ 1.85, frozen
  above), raising E(z) at z < ~5 and shrinking D_M(z_star) by ~1%.  Rematching the
  0.03%-measured angle therefore requires Delta ln h ~ -(1%)/0.19 ~ -5 to -6%: the
  weak lever arm AMPLIFIES a percent-level late-time deformation into a several-
  percent H0 shift.  This is the same mechanism by which theta_star anchors
  w0waCDM fits.  The Wave 45 expectation "shift < 1%" was WRONG, and the direction
  of the error matters: the calibration overshoots the amplitude the BAO data
  prefer, so GU's own CMB calibration makes the raw-BAO fit WORSE, not better.

PROVENANCE of the three NEW Planck digits (all others already repo-verified, Wave 45).
  arXiv:1807.06209 Table 2, base-LCDM, TT,TE,EE+lowE+lensing 68% column (the SAME
  column as the repo's verified H0/Om/r_drag/omega_m h^2).  Extracted 2026-07-13 from
  the arXiv PDF by direct text extraction (pypdf), lines quoted verbatim:
    "z*  . . .  1089.92 +/- 0.25"       (column 5 of the Table 2 grid, page 16)
    "r* [Mpc] . . .  144.43 +/- 0.26"
    "100theta* . . .  1.04110 +/- 0.00031"
    "rdrag [Mpc] . . .  147.09 +/- 0.26"   (matches the repo's verified value)
  Cross-check: the paper's abstract quotes 100theta* = 1.0411 +/- 0.0003.  NOTE the
  team brief said 1.04109; that is the TT,TE,EE+lowE (no lensing) column, Eq. (9) of
  the paper.  The +lensing column value 1.04110 is used, consistent with every other
  Planck digit in the repo; the difference (1e-5, 0.03 sigma) is far below A5.

THREE-WAY COMPARISON (the deliverable).  AIC = chi^2 + 2k, dAIC = AIC_GU - AIC_LCDM:
  Row 1  CMB-fixed Planck amplitude on both (H46 row, reproduced):   k = (0,0)
  Row 2  EACH model's OWN theta_star-calibrated amplitude (NEW):     k = (0,0)
         (LCDM's theta_star calibration IS the Planck point, PC2; GU's is solved here)
  Row 3  amplitude freed for both (H46 row, reproduced):             k = (1,1)
  Row 4  f0 refit on BAO with per-f0 CMB calibration (envelope):     k = (1,0)
  No double counting: theta_star enters ONLY through the amplitude; no CMB chi^2
  term is added to the BAO likelihood.

Run: python -u tests/wave46/H46C_theta_star_cmb_calibration.py   (exit 0 iff all PASS)
"""
from __future__ import annotations
import os
import sys
import importlib.util
import numpy as np
from scipy.optimize import brentq
from scipy.integrate import cumulative_trapezoid

FAIL = []


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}", flush=True)
    if not ok:
        FAIL.append(name)


def log(m=""):
    print(m, flush=True)


# ===========================================================================
# Import the H46 (wave29) machinery VERBATIM: DESI data, chi^2, BAO vectors,
# and (through it) the H44 backreacted background.  NOT re-implemented.
# ===========================================================================
_HERE = os.path.dirname(os.path.abspath(__file__))
_H46P = os.path.normpath(os.path.join(_HERE, "..", "wave29", "H46_de_raw_bao_likelihood.py"))
_spec = importlib.util.spec_from_file_location("H46_raw_bao", _H46P)
H46 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(H46)
H44 = H46.H44                        # the backreacted-background module
solve_backreacted = H46.solve_backreacted
bao_vector_from_E = H46.bao_vector_from_E
chi2_of = H46.chi2_of
chi2_marg_amplitude = H46.chi2_marg_amplitude
DESI_COV_INV = H46.DESI_COV_INV
DESI_MEAN = H46.DESI_MEAN

C_KMS = 299792.458
A_CMB = H46.A_CMB                    # 30.2625... = (c/67.36)/147.09
M2_BC1 = H46.M2_BC1                  # 8.0 (BC_1 ground; reconstruction-grade, OQ2-gated)
F0_CANON = H46.F0_CANON              # 0.125 (CPL-tuned, NOT a GU prediction)

# ===========================================================================
# Planck 2018 constants (arXiv:1807.06209 Table 2, TT,TE,EE+lowE+lensing).
# H0/OM/RD/OMH2 were repo-verified in Wave 45; RSTAR/ZSTAR/THETASTAR are
# primary-source-extracted this wave (PDF text extraction, 2026-07-13).
# ===========================================================================
H_PLANCK = 0.6736
OMH2 = 0.1430
RD = 147.09                          # r_drag [Mpc]
RSTAR = 144.43                       # r_star [Mpc]
ZSTAR = 1089.92
THETASTAR_100 = 1.04110              # 100 * theta_star
SIG_THETASTAR_100 = 0.00031
OMEGA_G_H2 = 2.4728e-5               # photons, T0 = 2.7255 K
OMEGA_R_H2 = OMEGA_G_H2 * (1.0 + 0.2271 * 3.046)   # + massless-approx neutrinos

Z_START = H44.Z_START                # 30.0 (theta slow-roll IC redshift)


# ===========================================================================
# theta_star(h) for the GU f0-family (f0 -> 0 IS LCDM; guard below).
# ===========================================================================
def _gu_background(h, f0, npts=1200, n_iter=50):
    """Backreacted late-time background at fractional Om = OMH2/h^2 (patching the
    H44 module globals; restored by caller loop -- single-threaded)."""
    Om_h = OMH2 / h ** 2
    H44.Om, H44.OL = Om_h, 1.0 - Om_h
    bg = solve_backreacted(M2_BC1, f0, npts=npts, n_iter=n_iter)
    return bg, Om_h


def _restore_module_cosmology():
    H44.Om, H44.OL = 0.315, 0.685


def dm_integral(h, f0, npts=1200, n_iter=50, ntail=6000):
    """I = int_0^{z_star} dz / E(z)  (so D_M = (c/H0) * I), plus diagnostics.
    z <= Z_START: backreacted solve + additive radiation (A1).
    z >  Z_START: frozen theta density (A4) + matter + radiation."""
    bg, Om_h = _gu_background(h, f0, npts=npts, n_iter=n_iter)
    Or_h = OMEGA_R_H2 / h ** 2
    idx = np.argsort(bg["z"])
    zl = bg["z"][idx]
    E2l = bg["H2"][idx] + Or_h * ((1.0 + zl) ** 4 - 1.0)
    Il = cumulative_trapezoid(1.0 / np.sqrt(E2l), zl, initial=0.0)[-1]
    rho_th_frozen = float(bg["rho_theta"][0])       # grid index 0 = z_start
    rho_L = float(bg["rho_L"])
    zt = np.geomspace(Z_START, ZSTAR, ntail)
    E2t = (Om_h * (1.0 + zt) ** 3 + Or_h * ((1.0 + zt) ** 4 - 1.0)
           + rho_L + rho_th_frozen)
    It = np.trapezoid(1.0 / np.sqrt(E2t), zt)
    frozen_frac = rho_th_frozen / (Om_h * (1.0 + Z_START) ** 3)
    return Il + It, dict(Om=Om_h, frozen_frac=frozen_frac, I_low=Il, I_tail=It)


def theta100_of(h, f0, **kw):
    I, _ = dm_integral(h, f0, **kw)
    DM = (C_KMS / (100.0 * h)) * I
    return 100.0 * RSTAR / DM


def calibrate_h(f0, target=THETASTAR_100, **kw):
    return brentq(lambda h: theta100_of(h, f0, **kw) - target, 0.55, 0.80, xtol=1e-6)


def theta100_of_omh2(h, f0, omh2, **kw):
    """A6 variant: theta_star with a shifted omega_m h^2 and the (omh2)^-0.25
    sound-horizon rescaling applied to r_star."""
    global OMH2
    old = OMH2
    OMH2 = omh2
    try:
        I, _ = dm_integral(h, f0, **kw)
    finally:
        OMH2 = old
    rstar = RSTAR * (omh2 / 0.1430) ** (-0.25)
    DM = (C_KMS / (100.0 * h)) * I
    return 100.0 * rstar / DM


# ===========================================================================
def main():
    log("=" * 78)
    log("H46C -- theta_star: GU's OWN CMB-calibrated amplitude (Wave 45 blocker B1)")
    log("=" * 78)
    log(f"  Planck 2018 (1807.06209 Table 2, TT,TE,EE+lowE+lensing): 100theta* = {THETASTAR_100}")
    log(f"  +/- {SIG_THETASTAR_100}, r* = {RSTAR} Mpc, z* = {ZSTAR}, r_drag = {RD} Mpc,")
    log(f"  omega_m h^2 = {OMH2} (fixed; h is the calibration unknown, Om = omega_m h^2/h^2)")

    # -----------------------------------------------------------------------
    # PC1 -- positive control: LCDM at the Planck point reproduces theta_star.
    # -----------------------------------------------------------------------
    log("\n" + "=" * 78)
    log("PC1 -- positive control: LCDM (f0 -> 0) at h = 0.6736 reproduces 100theta* = 1.04110")
    log("=" * 78)
    th_lcdm = theta100_of(H_PLANCK, 1e-10)
    resid_pc1 = (th_lcdm - THETASTAR_100) / THETASTAR_100
    log(f"  computed 100theta*(LCDM, h=0.6736) = {th_lcdm:.5f}   (Planck {THETASTAR_100})")
    log(f"  fractional residual = {resid_pc1:+.2e}  (budget: A1 radiation approx + A2 neutrino, ~1e-3)")
    check("PC1: LCDM pipeline reproduces Planck 100theta* to < 0.2%", abs(resid_pc1) < 2e-3,
          f"resid={resid_pc1:+.2e}")

    # grid-convergence guard on the distance integral
    th_hi = theta100_of(H_PLANCK, 1e-10, npts=2000, ntail=12000)
    check("PC1b: theta* grid-converged (doubling grids shifts < 3e-5 relative)",
          abs(th_hi - th_lcdm) / th_lcdm < 3e-5, f"delta={abs(th_hi-th_lcdm)/th_lcdm:.1e}")

    # -----------------------------------------------------------------------
    # PC2 -- calibration control: inverting theta_star for LCDM recovers h = 0.6736.
    # -----------------------------------------------------------------------
    log("\n" + "=" * 78)
    log("PC2 -- calibration control: solve theta*(h) = Planck for LCDM -> recover h = 0.6736")
    log("=" * 78)
    h_lcdm_cal = calibrate_h(1e-10)
    log(f"  h_LCDM(pipeline-calibrated) = {h_lcdm_cal:.5f}   (Planck 0.6736; "
        f"offset {(h_lcdm_cal/H_PLANCK-1)*100:+.3f}% = the shared pipeline systematic)")
    check("PC2: LCDM theta_star calibration recovers h = 0.6736 within 0.2%",
          abs(h_lcdm_cal / H_PLANCK - 1.0) < 2e-3)
    log("  -> LCDM's theta_star-calibrated amplitude IS the Planck point (row 2 LCDM = row 1")
    log("     LCDM); the pipeline offset above is divided out of the GU result (A3).")

    # -----------------------------------------------------------------------
    # Q1 -- THE B1 COMPUTATION: GU's own theta_star-calibrated amplitude, f0 = 0.125.
    # -----------------------------------------------------------------------
    log("\n" + "=" * 78)
    log("Q1 -- GU's own CMB calibration at canonical f0 = 0.125 (M^2 = 8, OQ2-gated)")
    log("=" * 78)
    # the raw miss: GU at the PLANCK h does not reproduce the measured angle
    th_gu_at_planck_h = theta100_of(H_PLANCK, F0_CANON)
    miss_sig = (th_gu_at_planck_h - THETASTAR_100) / SIG_THETASTAR_100
    log(f"  100theta*(GU, f0=0.125, h=0.6736) = {th_gu_at_planck_h:.5f}"
        f"  -> {miss_sig:+.0f} sigma from the measured 1.04110 +/- 0.00031")
    # lever arm: theta_star is weakly h-sensitive at fixed omega_m h^2
    dlnth = (np.log(theta100_of(H_PLANCK * 1.01, 1e-10))
             - np.log(theta100_of(H_PLANCK * 0.99, 1e-10))) / (2 * np.log(1.01))
    log(f"  lever arm dln(theta*)/dln(h) [LCDM] = {dlnth:.3f}  (weak -> percent-level D_M")
    log(f"  deformations force several-percent h shifts; see header physics note)")

    h_gu_raw = calibrate_h(F0_CANON)
    h_gu = h_gu_raw * (H_PLANCK / h_lcdm_cal)          # A3 ratio correction
    Om_gu = OMH2 / h_gu ** 2
    A_gu = C_KMS / (100.0 * h_gu) / RD
    _, diag = dm_integral(h_gu_raw, F0_CANON)
    log(f"  h_GU(raw) = {h_gu_raw:.5f}  ->  h_GU(ratio-corrected) = {h_gu:.5f}"
        f"   (H0_GU = {100*h_gu:.2f} km/s/Mpc; note: AWAY from local H0 ~ 73)")
    log(f"  Om_GU(calibrated) = {Om_gu:.4f}   (source value 0.315; drift {Om_gu-0.315:+.4f})")
    log(f"  A_GU(CMB-calibrated) = {A_gu:.4f}   (Planck/LCDM A = {A_CMB:.4f}; "
        f"shift {(A_gu/A_CMB-1)*100:+.3f}%)")
    log(f"  frozen-theta tail: rho_theta(z=30)/rho_m(z=30) = {diag['frozen_frac']:.2e} (A4 check)")
    log(f"  NOTE the source-Om branch: keeping fractional Om = 0.315 at this h would need")
    log(f"  omega_m h^2 = {0.315*h_gu**2:.4f}, which is {(0.1430-0.315*h_gu**2)/0.0011:.0f} sigma "
        f"below Planck's 0.1430 +/- 0.0011: that branch")
    log(f"  abandons CMB compatibility outright and is not a calibration.")
    check("Q1: frozen-theta density negligible vs matter at z_start (early physics untouched)",
          diag["frozen_frac"] < 1e-3, f"{diag['frozen_frac']:.2e}")
    check("Q1: calibration solved (finite, in bracket) and direction correct "
          "(extra past DE -> smaller D_M -> LOWER calibrated h than LCDM)",
          np.isfinite(h_gu) and 0.55 < h_gu < 0.80 and h_gu < H_PLANCK
          and th_gu_at_planck_h > THETASTAR_100,
          f"h_GU={h_gu:.5f}, miss at Planck h = {miss_sig:+.0f} sigma")
    check("Q1: lever arm is weak (dln theta*/dln h < 0.5), the amplification is real "
          "not a bug", 0.0 < dlnth < 0.5, f"{dlnth:.3f}")
    _restore_module_cosmology()

    # guard: GU pipeline at f0 -> 0 calibrates to the LCDM h (continuity of the family)
    h_00 = calibrate_h(1e-8)
    check("Q1 guard: calibrate_h(f0->0) = h_LCDM_cal to < 1e-4 (family is continuous)",
          abs(h_00 / h_lcdm_cal - 1.0) < 1e-4, f"delta={abs(h_00/h_lcdm_cal-1):.1e}")
    _restore_module_cosmology()

    # -----------------------------------------------------------------------
    # Q2 -- the three-way likelihood table (AIC with explicit k per row).
    # -----------------------------------------------------------------------
    log("\n" + "=" * 78)
    log("Q2 -- three-way comparison on the DESI DR2 BAO likelihood (AIC = chi^2 + 2k)")
    log("=" * 78)

    # Row 1: reproduce H46 exactly (module cosmology Om=0.315, Planck amplitude).
    bg_c = solve_backreacted(M2_BC1, F0_CANON, npts=1400)
    idx = np.argsort(bg_c["z"])
    zc, Ec = bg_c["z"][idx], np.sqrt(bg_c["H2"][idx])
    ac = 1.0 / (1.0 + zc)
    E_l = np.sqrt(0.315 * ac ** -3 + 0.685)
    chi2_gu_r1 = chi2_of(bao_vector_from_E(zc, Ec, A_CMB))
    chi2_l_r1 = chi2_of(bao_vector_from_E(zc, E_l, A_CMB))
    daic1 = chi2_gu_r1 - chi2_l_r1
    check("Row 1 reproduces H46/H46B: chi^2 = 52.26 / 30.68, dAIC = +21.58 (within 0.05)",
          abs(chi2_gu_r1 - 52.26) < 0.05 and abs(chi2_l_r1 - 30.68) < 0.05
          and abs(daic1 - 21.58) < 0.05, f"{chi2_gu_r1:.2f}/{chi2_l_r1:.2f}/{daic1:+.2f}")

    # Row 3: reproduce H46 freed-amplitude row.
    chi2m_gu, Ast_gu = chi2_marg_amplitude(bao_vector_from_E(zc, Ec, 1.0))
    chi2m_l, Ast_l = chi2_marg_amplitude(bao_vector_from_E(zc, E_l, 1.0))
    daic3 = chi2m_gu - chi2m_l                       # k = 1 both, 2k cancels
    check("Row 3 reproduces H46B: chi^2 = 10.99 / 14.15, dAIC = -3.17 (within 0.05)",
          abs(chi2m_gu - 10.99) < 0.05 and abs(chi2m_l - 14.15) < 0.05
          and abs(daic3 + 3.17) < 0.05, f"{chi2m_gu:.2f}/{chi2m_l:.2f}/{daic3:+.2f}")

    # Row 2 (NEW): each model at its OWN theta_star-calibrated amplitude, k = (0,0).
    bg_gu2, _ = _gu_background(h_gu, F0_CANON, npts=1400, n_iter=60)
    idx2 = np.argsort(bg_gu2["z"])
    z2, E2v = bg_gu2["z"][idx2], np.sqrt(bg_gu2["H2"][idx2])
    vec_gu2 = bao_vector_from_E(z2, E2v, A_gu)
    chi2_gu_r2 = chi2_of(vec_gu2)
    _restore_module_cosmology()
    chi2_l_r2 = chi2_l_r1                            # LCDM's CMB calibration = Planck point
    daic2 = chi2_gu_r2 - chi2_l_r2
    # where the calibrated amplitude sits relative to the BAO-preferred one, in A-sigmas
    b2 = bao_vector_from_E(z2, E2v, 1.0)
    bCb = float(b2 @ DESI_COV_INV @ b2)
    sigA = 1.0 / np.sqrt(bCb)
    _, Astar2 = chi2_marg_amplitude(b2)
    log(f"\n  Row 2 detail: GU calibrated A = {A_gu:.4f}; BAO-preferred A*(this shape) = "
        f"{Astar2:.4f}; gap = {(Astar2-A_gu)/sigA:+.2f} sigma_A (sigma_A = {sigA:.4f})")

    # A5 sensitivity band on row 2 (+/-0.2% shared absolute scale).
    chi2_r2_lo = chi2_of(bao_vector_from_E(z2, E2v, A_gu * 0.998))
    chi2_r2_hi = chi2_of(bao_vector_from_E(z2, E2v, A_gu * 1.002))
    band_lo, band_hi = sorted((chi2_r2_lo, chi2_r2_hi))
    if chi2_gu_r2 < band_lo:
        band_lo = chi2_gu_r2

    # Row 4: f0 refit with PER-f0 CMB calibration (k = 1 for GU, 0 for LCDM).
    log("\n  Row 4 scan: per-f0 theta_star calibration (each f0 gets its OWN CMB amplitude):")
    rows4 = []
    for f0 in (0.005, 0.01, 0.02, 0.05, 0.08, 0.125, 0.20, 0.30):
        h_r = calibrate_h(f0, npts=900, n_iter=40)
        h_c = h_r * (H_PLANCK / h_lcdm_cal)
        A_c = C_KMS / (100.0 * h_c) / RD
        bgf, _ = _gu_background(h_c, f0, npts=900, n_iter=40)
        _restore_module_cosmology()
        i4 = np.argsort(bgf["z"])
        c2 = chi2_of(bao_vector_from_E(bgf["z"][i4], np.sqrt(bgf["H2"][i4]), A_c))
        rows4.append((f0, h_c, A_c, c2))
        log(f"     f0={f0:5.3f}: h_cal={h_c:.5f}  A_cal={A_c:.4f}  chi^2={c2:8.3f}"
            f"  (dchi^2 vs LCDM {c2-chi2_l_r1:+8.3f})")
    f0_best, h_best, A_best, chi2_best = min(rows4, key=lambda r: r[3])
    daic4 = (chi2_best + 2.0) - chi2_l_r1            # k = (1, 0)
    ratio_f0 = max(F0_CANON / f0_best, f0_best / F0_CANON)

    log("\n  " + "-" * 74)
    log("  THE THREE-WAY TABLE (+ envelope row).  dAIC = AIC_GU - AIC_LCDM; dAIC > 0")
    log("  disfavors GU.  Conventional read: |dAIC| < 4 not decisive, > 10 decisive.")
    log("  " + "-" * 74)
    log(f"  Row 1  CMB-fixed Planck amplitude   k=(0,0)  chi2 {chi2_gu_r1:6.2f} vs {chi2_l_r1:5.2f}"
        f"   dAIC {daic1:+7.2f}")
    log(f"  Row 2  OWN theta_star calibration   k=(0,0)  chi2 {chi2_gu_r2:6.2f} vs {chi2_l_r2:5.2f}"
        f"   dAIC {daic2:+7.2f}   [band {band_lo:.2f}..{band_hi:.2f} under A5]")
    log(f"  Row 3  amplitude freed on both      k=(1,1)  chi2 {chi2m_gu:6.2f} vs {chi2m_l:5.2f}"
        f"   dAIC {daic3:+7.2f}")
    log(f"  Row 4  f0 refit, per-f0 CMB calib   k=(1,0)  chi2 {chi2_best:6.2f} vs {chi2_l_r1:5.2f}"
        f"   dAIC {daic4:+7.2f}   [f0* = {f0_best}]")

    check("Row 2 computed and the finding is the OVERSHOOT: GU's own CMB calibration "
          "lands > 3 sigma_A ABOVE the BAO-preferred amplitude for its own shape",
          np.isfinite(chi2_gu_r2) and (A_gu - Astar2) / sigA > 3.0,
          f"gap = {(A_gu-Astar2)/sigA:+.2f} sigma_A")
    check("Row 2 sits ABOVE the freed-amplitude minimum (row 3), as it must",
          chi2_gu_r2 > chi2m_gu, f"{chi2_gu_r2:.2f} > {chi2m_gu:.2f}")
    check("no double counting: theta_star used ONLY to set A; no CMB term added to chi^2",
          True, "structural (by construction of every row)")

    # -----------------------------------------------------------------------
    # Q3 -- the f0 dual-observable inconsistency, re-examined under the calibration.
    # -----------------------------------------------------------------------
    log("\n" + "=" * 78)
    log("Q3 -- f0 inconsistency under GU's own CMB calibration")
    log("=" * 78)
    chi2_at_canon = [r[3] for r in rows4 if r[0] == F0_CANON][0]
    c2map = {r[0]: r[3] for r in rows4}
    monotone = all(c2map[a] < c2map[b] for a, b in
                   zip((0.005, 0.01, 0.02, 0.05, 0.08, 0.125, 0.20),
                       (0.01, 0.02, 0.05, 0.08, 0.125, 0.20, 0.30)))
    # dchi^2 = 9 crossing (3-sigma-equivalent, 1 dof) by log-interpolation of the scan
    f0s_scan = np.array([r[0] for r in rows4])
    d_scan = np.array([r[3] for r in rows4]) - chi2_l_r1
    f0_9 = float(np.exp(np.interp(9.0, d_scan, np.log(f0s_scan))))
    log(f"  Wave 45 state (FIXED Planck amplitude): BAO preferred f0 ~ 0.05 vs CPL-tuned")
    log(f"  0.125, factor >= 2, 'no single f0 satisfies both'.")
    log(f"  THIS WAVE (per-f0 CMB calibration, amplitude no longer free): chi^2(f0) is")
    log(f"  MONOTONE INCREASING in f0 over the scan -- the BAO+theta* preferred value is")
    log(f"  the LCDM LIMIT f0 -> 0.  The 'f0 ~ 0.05 fits better than LCDM' rescue was an")
    log(f"  artifact of holding the amplitude at the Planck value while ignoring what the")
    log(f"  model's own calibration does to it: it DISSOLVES, in the direction AGAINST GU.")
    log(f"  chi^2 at canonical f0 = 0.125 under its own CMB calibration = {chi2_at_canon:.2f}")
    log(f"  (vs LCDM {chi2_l_r1:.2f}; dchi^2 = {chi2_at_canon-chi2_l_r1:+.2f})")
    log(f"  dchi^2 = 9 crossing: f0 ~ {f0_9:.3f}  (every f0 above this is excluded at")
    log(f"  > 3 sigma 1-dof-equivalent on the raw BAO likelihood, GIVEN the model's own")
    log(f"  CMB calibration)")
    check("Q3: chi^2(f0) monotone increasing over the scan (BAO+theta* prefers f0 -> 0, "
          "the LCDM limit)", monotone)
    check("Q3: canonical f0 = 0.125 excluded at its own CMB-calibrated amplitude "
          "(dchi^2 > 9 vs LCDM)", chi2_at_canon - chi2_l_r1 > 9.0,
          f"dchi2={chi2_at_canon-chi2_l_r1:+.2f}")
    check("Q3: the CPL-tuned f0 = 0.125 exceeds the 3-sigma-equivalent BAO+theta* bound",
          F0_CANON > f0_9, f"0.125 > {f0_9:.3f}")

    # -----------------------------------------------------------------------
    # Q4 -- A6: omega_m h^2 PROFILED for BOTH models under the Planck prior.
    # A naive fixed-LCDM scan is misleading twice over: shifting omega_m h^2 by
    # n sigma costs the Planck prior n^2 in chi^2, and LCDM may profile the same
    # nuisance (it does: the known Planck-DESI amplitude tension relaxes at low
    # omega_m h^2).  So: total(n) = chi2_BAO(theta_star-calibrated at omega_m h^2
    # shifted n sigma) + n^2, minimized over n for EACH model; equal k, so
    # dAIC = min total(GU) - min total(LCDM).
    # -----------------------------------------------------------------------
    log("\n" + "=" * 78)
    log("Q4 -- omega_m h^2 profiled (Planck prior penalty) for BOTH models (A6)")
    log("=" * 78)

    def profiled_total(f0, nsigs):
        rows = []
        for n in nsigs:
            omh2 = 0.1430 + n * 0.0011
            h_r = brentq(lambda h: theta100_of_omh2(h, f0, omh2, npts=900, n_iter=40)
                         - THETASTAR_100, 0.52, 0.82, xtol=1e-6)
            h_c = h_r * (H_PLANCK / h_lcdm_cal)
            rd_s = RD * (omh2 / 0.1430) ** (-0.25)
            A_c = C_KMS / (100.0 * h_c) / rd_s
            H44.Om, H44.OL = omh2 / h_c ** 2, 1.0 - omh2 / h_c ** 2
            bgs = solve_backreacted(M2_BC1, f0, npts=900, n_iter=40)
            _restore_module_cosmology()
            i5 = np.argsort(bgs["z"])
            c2 = chi2_of(bao_vector_from_E(bgs["z"][i5], np.sqrt(bgs["H2"][i5]), A_c))
            rows.append((n, h_c, A_c, c2, c2 + n * n))
        return rows

    nsigs = np.arange(-5.0, 2.01, 0.5)
    prof_gu = profiled_total(F0_CANON, nsigs)
    prof_l = profiled_total(1e-10, nsigs)
    for tag, rows in (("GU f0=0.125", prof_gu), ("LCDM", prof_l)):
        log(f"  {tag}:")
        for n, h_c, A_c, c2, tot in rows:
            log(f"     n={n:+.1f} sigma: h_cal={h_c:.5f}  A_cal={A_c:.4f}  "
                f"chi2_BAO={c2:8.3f}  total={tot:8.3f}")
    n_gu, _, _, c2bao_gu, tot_gu = min(prof_gu, key=lambda r: r[4])
    n_l, _, _, c2bao_l, tot_l = min(prof_l, key=lambda r: r[4])
    daic_q4 = tot_gu - tot_l
    log(f"\n  profiled minima: GU total = {tot_gu:.2f} at n = {n_gu:+.1f} sigma "
        f"(chi2_BAO {c2bao_gu:.2f}); LCDM total = {tot_l:.2f} at n = {n_l:+.1f} sigma "
        f"(chi2_BAO {c2bao_l:.2f})")
    log(f"  PROFILED dAIC (equal k) = {daic_q4:+.2f}")
    log(f"  (interior minima only count; both must be off the scan edge)")
    check("Q4: profiled minima are interior to the scanned n range (not edge artifacts)",
          nsigs[0] < n_gu < nsigs[-1] and nsigs[0] < n_l < nsigs[-1],
          f"n_GU={n_gu:+.1f}, n_LCDM={n_l:+.1f}")
    check("Q4: f0 = 0.125 stays decisively disfavored (profiled dAIC > 9) with "
          "omega_m h^2 profiled for BOTH models under the Planck prior",
          daic_q4 > 9.0, f"profiled dAIC = {daic_q4:+.2f}")

    # -----------------------------------------------------------------------
    # VERDICT.
    # -----------------------------------------------------------------------
    log("\n" + "-" * 78)
    log("VERDICT (B1)")
    log("-" * 78)
    b1_done = (abs(resid_pc1) < 2e-3 and np.isfinite(A_gu))
    hardened = (monotone and (chi2_at_canon - chi2_l_r1) > 9.0 and daic2 > 9.0
                and daic_q4 > 9.0)
    log(f"  B1 (theta_star re-solve of GU's own CMB amplitude): "
        f"{'COMPUTED' if b1_done else 'NOT COMPUTED'}.")
    log(f"  A_GU(CMB) = {A_gu:.4f} vs Planck/LCDM {A_CMB:.4f}: GU's own calibration shifts the")
    log(f"  amplitude by {(A_gu/A_CMB-1)*100:+.2f}%, OVERSHOOTING the BAO-preferred amplitude for its own")
    log(f"  shape (A* = {Astar2:.2f}) by {(A_gu-Astar2)/sigA:+.1f} sigma_A.  The Wave 45 freed-amplitude shape win")
    log(f"  (row 3, dAIC = -3.17) required an amplitude GU's own CMB calibration cannot supply.")
    if hardened:
        log("  f0-inconsistency status: FALSIFICATION-HARDENED, and the Wave 45 rescue")
        log("  DISSOLVES against GU.  With the amplitude fixed by the model's own theta_star")
        log("  calibration (the fairness argument replaced by the computation it stood in")
        log("  for): (i) the CPL-tuned point f0 = 0.125 is independently excluded on the raw")
        log("  DR2 BAO likelihood (dchi^2 > 9, robust across the omega_m h^2 prior width);")
        log("  (ii) the BAO-preferred amplitude is unreachable, so the 'competitive on shape'")
        log("  reading has no CMB-consistent realization; (iii) the BAO+theta* preferred f0")
        log("  is the LCDM limit f0 -> 0 -- the theta component is an upper limit, not a")
        log("  detection.  SCOPE GUARDS: f0 is a fit parameter, not a GU prediction (H42);")
        log("  M^2 = 8 H0^2 stays reconstruction-grade (OQ2 open) and nothing here promotes")
        log("  it; the falsified object is the theta-sector DE FAMILY AS A CMB-CONSISTENT")
        log("  DISTANCE MODEL at exploration grade, not GU as a whole; the named escape is")
        log("  rejecting the theta_star calibration, i.e. modifying PRE-recombination")
        log("  physics, which the GU theta sector does not do.")
    else:
        log("  f0-inconsistency status: TENSION (some leg of the hardening criteria failed;")
        log("  read the table rows above).")
    log("-" * 78)

    if FAIL:
        log(f"\nFAILED: {FAIL}")
        sys.exit(1)
    log(f"\nexit 0 = H46C recorded.  A_GU(CMB, theta_star) = {A_gu:.4f} "
        f"({(A_gu/A_CMB-1)*100:+.2f}% vs Planck; overshoot {(A_gu-Astar2)/sigA:+.1f} sigma_A), "
        f"row-2 dAIC = {daic2:+.2f}, omh2-profiled dAIC = {daic_q4:+.2f}; f0 verdict "
        f"{'FALSIFICATION-HARDENED (rescue dissolves)' if hardened else 'TENSION'}.")
    sys.exit(0)


if __name__ == "__main__":
    main()
