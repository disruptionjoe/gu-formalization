#!/usr/bin/env python3
r"""DE-12 -- theta_star-pipeline in-sample consistency check (Wave A-2, item 1).

WHAT THIS CERTIFIES.  Every decisive DE number in the repo (H46 dAIC +21.58, H46C row-2
+35.78, the +19.3 amplitude-marginalised shape gap, the W129 exclusions) is downstream of
ONE pipeline: theta_star calibration at fixed omega_m h^2 (Planck early physics frozen)
feeding the byte-verified DESI DR2 BAO Gaussian likelihood.  That pipeline has LCDM
positive controls (H46C PC1/PC2) but NO dynamical-DE positive control: nothing checks
that a non-LCDM shape selected from the same DESI data is reproduced by this reduced
pipeline.  DE-12 supplies that internal check: push DESI's reported best-fit w0waCDM
(H46B-verified P1_CPL digits, arXiv:2503.14738 Sec. VII) through the machinery.
Because the row is selected using the same data, it is NOT an independent positive
control and cannot by itself certify an unbiased pipeline or C10.

OPERATIONALISATION ("dAIC ~ 0 vs itself").  For a model whose defining property is that
it reconciles the CMB acoustic scale with the DR2 BAO distances, the theta_star-
calibrated amplitude must essentially BE the BAO-preferred amplitude for its own shape:
    dAIC_amp = [chi2(A_cal) + 2*0] - [chi2_marg + 2*1]   (k = (0,1))
This is only an amplitude-fixed versus amplitude-freed diagnostic.  It omits the
selection/complexity cost of obtaining the w0wa shape from the same data and is not
a model-selection AIC comparison between independently specified models.
PASS (preregistered): chi2(A_cal) - chi2_marg < 4 for the DESI+CMB combo (the no-SNe
combo -- the right control for a BAO+theta_star-only pipeline), i.e. amplitude gap
< 2 sigma_A and dAIC_self in (-2, +2).
FAIL (>= 9): the wave45/46/W129 chain is SUSPECT and every exclusion number moves --
report loudly, do not paper over.  4..9: MARGINAL, investigate before certifying.

CONTRAST (context): GU (M^2 = 8, f0 = 0.125) through the identical fresh machinery must
reproduce the H46C overshoot (gap > 3 sigma_A; H46C: +5.74 sigma_A).

Machinery: fresh general-rho_DE(z) integrator with the SAME approximations as H46C
(A1 additive radiation keeping E(0) = 1; A3 ratio correction dividing out the shared
pipeline systematic; early physics frozen at the Planck digits), certified against
H46C's own LCDM numbers before use (PC-F1/PC-F2/PC-F3).  DESI data/covariance and the
chi^2/marginalisation are IMPORTED VERBATIM from tests/wave29 (H46B-verified).

Preregistration: explorations/de-pipeline-certification-and-bridge-test-2026-08-03.md
Section 1.1 (written before this script).  Run:
  PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python -u \
      tests/de-certification/de12_theta_star_positive_control.py
Exit 0 iff the internal-consistency and contrast checks hold.  Exit 0 does not certify
pipeline unbiasedness, C10, or an out-of-sample validation.
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


def _load(rel, name):
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.normpath(os.path.join(here, "..", "..", rel))
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ===========================================================================
# Imports: the byte-verified likelihood + the H46C machinery (VERBATIM).
# ===========================================================================
H46C = _load("tests/wave46/H46C_theta_star_cmb_calibration.py", "H46C_mod")
H46 = H46C.H46
H46B = _load("tests/wave45/H46B_referee_grade_desi_verification.py", "H46B_mod")

bao_vector_from_E = H46.bao_vector_from_E
chi2_of = H46.chi2_of
chi2_marg_amplitude = H46.chi2_marg_amplitude
DESI_COV_INV = H46.DESI_COV_INV

C_KMS = 299792.458
H_PLANCK = H46C.H_PLANCK          # 0.6736
OMH2 = H46C.OMH2                  # 0.1430
RD = H46C.RD                      # 147.09
RSTAR = H46C.RSTAR                # 144.43
ZSTAR = H46C.ZSTAR                # 1089.92
THETASTAR_100 = H46C.THETASTAR_100
OMEGA_R_H2 = H46C.OMEGA_R_H2
A_CMB = H46.A_CMB

CPL = H46B.P1_CPL                 # H46B-verified w0waCDM combos (Sec. VII digits)


# ===========================================================================
# Fresh general-rho_DE(z) machinery (certified against H46C's LCDM below).
# rho_de_ratio(z) = rho_DE(z)/rho_DE(0); CPL closed form.
# ===========================================================================
def rho_cpl(z, w0, wa):
    zp1 = 1.0 + np.asarray(z, dtype=float)
    return zp1 ** (3.0 * (1.0 + w0 + wa)) * np.exp(-3.0 * wa * (zp1 - 1.0) / zp1)


def E2_of(z, h, w0, wa):
    """E^2(z) with A1 additive radiation keeping E(0) = 1 exactly (H46C treatment)."""
    Om = OMH2 / h ** 2
    Or = OMEGA_R_H2 / h ** 2
    zp1 = 1.0 + np.asarray(z, dtype=float)
    return (Om * zp1 ** 3 + Or * (zp1 ** 4 - 1.0)
            + (1.0 - Om) * rho_cpl(z, w0, wa))


def theta100_cpl(h, w0, wa, nlo=3000, nhi=6000):
    zlo = np.linspace(0.0, 30.0, nlo)
    Ilo = cumulative_trapezoid(1.0 / np.sqrt(E2_of(zlo, h, w0, wa)), zlo, initial=0.0)[-1]
    zhi = np.geomspace(30.0, ZSTAR, nhi)
    Ihi = np.trapezoid(1.0 / np.sqrt(E2_of(zhi, h, w0, wa)), zhi)
    DM = (C_KMS / (100.0 * h)) * (Ilo + Ihi)
    return 100.0 * RSTAR / DM


def calibrate_h_cpl(w0, wa):
    return brentq(lambda h: theta100_cpl(h, w0, wa) - THETASTAR_100, 0.50, 0.85, xtol=1e-6)


def bao_grid_cpl(h, w0, wa, zmax=3.0, n=1500):
    zg = np.linspace(0.0, zmax, n)
    return zg, np.sqrt(E2_of(zg, h, w0, wa))


# ===========================================================================
def main():
    log("=" * 78)
    log("DE-12 -- theta_star-pipeline IN-SAMPLE CONSISTENCY CHECK")
    log("         DESI's reported best-fit w0waCDM through the H46C machinery")
    log("=" * 78)
    log(f"  frozen early physics: 100theta* = {THETASTAR_100}, r* = {RSTAR}, z* = {ZSTAR},")
    log(f"  r_drag = {RD}, omega_m h^2 = {OMH2}  (identical to H46C; h floats)")

    # -----------------------------------------------------------------------
    # PC-F -- certify the fresh integrator against H46C's own LCDM numbers.
    # -----------------------------------------------------------------------
    log("\n" + "=" * 78)
    log("PC-F -- machinery certificate (fresh integrator vs H46C, LCDM limit)")
    log("=" * 78)
    th_fresh = theta100_cpl(H_PLANCK, -1.0, 0.0)
    th_h46c = H46C.theta100_of(H_PLANCK, 1e-10)
    H46C._restore_module_cosmology()
    rel = abs(th_fresh - th_h46c) / th_h46c
    log(f"  100theta*(LCDM, h=0.6736): fresh = {th_fresh:.6f}, H46C = {th_h46c:.6f}"
        f"  (rel diff {rel:.2e})")
    check("PC-F1: fresh LCDM theta* matches H46C's to < 1e-4 relative", rel < 1e-4,
          f"rel={rel:.2e}")
    h_lcdm_cal = calibrate_h_cpl(-1.0, 0.0)
    log(f"  fresh LCDM calibration: h = {h_lcdm_cal:.5f}  (Planck 0.6736; offset "
        f"{(h_lcdm_cal/H_PLANCK-1)*100:+.3f}% = shared pipeline systematic, divided out below)")
    check("PC-F2: fresh LCDM calibration recovers h = 0.6736 within 0.2%",
          abs(h_lcdm_cal / H_PLANCK - 1.0) < 2e-3)
    zg, Eg = bao_grid_cpl(H_PLANCK, -1.0, 0.0)
    chi2_lcdm_planck = chi2_of(bao_vector_from_E(zg, Eg, A_CMB))
    log(f"  fresh LCDM chi^2 at the Planck amplitude = {chi2_lcdm_planck:.3f}  (H46: 30.68)")
    # PC-F3 AMENDED (recorded in the exploration note, Section 2.1): the H46 LCDM row
    # is RADIATION-FREE (E_lcdm = sqrt(0.315 a^-3 + 0.685) exactly), while this fresh
    # frame includes the A1 radiation term in EVERY row.  As preregistered, PC-F3
    # compared across frames and failed by the named systematic (-0.57).  The
    # like-for-like certificate is (a); the systematic is bounded and shared in (b).
    zp1 = 1.0 + zg
    E_norad = np.sqrt(0.315 * zp1 ** 3 + 0.685)
    chi2_norad = chi2_of(bao_vector_from_E(zg, E_norad, A_CMB))
    log(f"  fresh RADIATION-FREE LCDM chi^2 (H46 convention) = {chi2_norad:.3f}  (H46: 30.68)")
    check("PC-F3a: fresh radiation-free LCDM chi^2 matches H46's 30.68 to < 0.05",
          abs(chi2_norad - 30.68) < 0.05, f"{chi2_norad:.3f}")
    check("PC-F3b: the A1 radiation-inclusion shift is bounded (|d chi^2| < 1) and is "
          "SHARED by every fresh row (cancels in same-frame comparisons)",
          abs(chi2_lcdm_planck - chi2_norad) < 1.0,
          f"shift={chi2_lcdm_planck - chi2_norad:+.3f}")

    # LCDM through its own calibration (the reference row; = Planck point by PC-F2)
    b_l = bao_vector_from_E(zg, Eg, 1.0)
    chi2m_l, Astar_l = chi2_marg_amplitude(b_l)
    sigA_l = 1.0 / np.sqrt(float(b_l @ DESI_COV_INV @ b_l))
    gap_l = (A_CMB - Astar_l) / sigA_l
    log(f"  LCDM reference: chi2(A_Planck) = {chi2_lcdm_planck:.2f}, chi2_marg = {chi2m_l:.2f},"
        f" amplitude gap = {gap_l:+.2f} sigma_A")
    log(f"  (the known Planck-DESI amplitude tension; DE-07 item 3 quotes +4.0 sigma_A)")

    # -----------------------------------------------------------------------
    # THE CONTROL -- all four H46B-verified w0waCDM combos through the pipeline.
    # -----------------------------------------------------------------------
    log("\n" + "=" * 78)
    log("CONTROL -- DESI DR2 w0waCDM best fits through the identical theta_star pipeline")
    log("=" * 78)
    log("  per combo: calibrate h (theta*), A3-ratio-correct, evaluate the raw BAO")
    log("  likelihood at A_cal, and compare to the same shape's own amplitude optimum.")
    rows = {}
    for name, p in CPL.items():
        w0, wa = p["w0"], p["wa"]
        h_raw = calibrate_h_cpl(w0, wa)
        h_c = h_raw * (H_PLANCK / h_lcdm_cal)            # A3 ratio correction
        Om_c = OMH2 / h_c ** 2
        A_c = C_KMS / (100.0 * h_c) / RD
        zg2, Eg2 = bao_grid_cpl(h_c, w0, wa)
        chi2_cal = chi2_of(bao_vector_from_E(zg2, Eg2, A_c))
        b = bao_vector_from_E(zg2, Eg2, 1.0)
        chi2m, Astar = chi2_marg_amplitude(b)
        sigA = 1.0 / np.sqrt(float(b @ DESI_COV_INV @ b))
        gap = (A_c - Astar) / sigA
        d_self = chi2_cal - chi2m
        daic_self = d_self - 2.0                          # k = (0,1)
        rows[name] = dict(h=h_c, Om=Om_c, A=A_c, chi2_cal=chi2_cal, chi2m=chi2m,
                          Astar=Astar, sigA=sigA, gap=gap, d_self=d_self,
                          daic_self=daic_self)
        log(f"\n  [{name}]  (w0, wa) = ({w0:+.3f}, {wa:+.3f})")
        log(f"     h_cal = {h_c:.5f}  (H0 = {100*h_c:.2f})   Om_cal = {Om_c:.4f}")
        log(f"     A_cal = {A_c:.4f}   BAO-preferred A*(this shape) = {Astar:.4f}"
            f"   gap = {gap:+.2f} sigma_A (sigma_A = {sigA:.4f})")
        log(f"     chi2(A_cal) = {chi2_cal:.3f}   chi2_marg = {chi2m:.3f}"
            f"   dchi2_self = {d_self:+.3f}   dAIC_self = {daic_self:+.3f}")
        log(f"     vs calibrated LCDM: dchi2 = {chi2_cal - chi2_lcdm_planck:+.3f}")

    r1 = rows["DESI+CMB"]
    r2 = rows["DESI+CMB+DESY5"]

    log("\n" + "-" * 78)
    log("  PREREGISTERED NUMERICAL ROWS (scope corrected by hostile review)")
    log("-" * 78)
    check("CONTROL-1 (IN-SAMPLE): reported DESI+CMB shape has a small "
          "amplitude-fixed/freed gap (dchi2_self < 4, gap < 2 sigma_A)",
          r1["d_self"] < 4.0 and abs(r1["gap"]) < 2.0,
          f"dchi2_self={r1['d_self']:+.3f}, gap={r1['gap']:+.2f} sigma_A")
    if not (r1["d_self"] < 4.0):
        log("  *** LOUD FAIL: the in-sample consistency row did not reproduce.  The")
        log("  *** wave45/46/W129 chain is SUSPECT; every exclusion number moves.")
        log("  *** Do not cite the +19.3 / +35.78 / +21.58 chain until resolved.")
    check("CONTROL-2: DESI+CMB+DESY5 (SNe pulls admissible) dchi2_self < 9",
          r2["d_self"] < 9.0, f"dchi2_self={r2['d_self']:+.3f}")
    check("CONTROL-3: calibrated w0waCDM (DESI+CMB) beats calibrated LCDM on raw BAO",
          r1["chi2_cal"] < chi2_lcdm_planck,
          f"{r1['chi2_cal']:.2f} < {chi2_lcdm_planck:.2f}")

    # -----------------------------------------------------------------------
    # CONTRAST -- GU through the SAME fresh reference frame (H46C machinery).
    # -----------------------------------------------------------------------
    log("\n" + "=" * 78)
    log("CONTRAST -- GU (M^2 = 8, f0 = 0.125) for scale (H46C machinery, verbatim)")
    log("=" * 78)
    h_gu_raw = H46C.calibrate_h(H46C.F0_CANON)
    h_gu = h_gu_raw * (H_PLANCK / h_lcdm_cal)
    A_gu = C_KMS / (100.0 * h_gu) / RD
    bg, _ = H46C._gu_background(h_gu, H46C.F0_CANON, npts=1400, n_iter=60)
    H46C._restore_module_cosmology()
    idx = np.argsort(bg["z"])
    zgu, Egu = bg["z"][idx], np.sqrt(bg["H2"][idx])
    chi2_gu_cal = chi2_of(bao_vector_from_E(zgu, Egu, A_gu))
    b_gu = bao_vector_from_E(zgu, Egu, 1.0)
    chi2m_gu, Astar_gu = chi2_marg_amplitude(b_gu)
    sigA_gu = 1.0 / np.sqrt(float(b_gu @ DESI_COV_INV @ b_gu))
    gap_gu = (A_gu - Astar_gu) / sigA_gu
    log(f"  h_cal = {h_gu:.5f}  Om_cal = {OMH2/h_gu**2:.4f}  A_cal = {A_gu:.4f}")
    log(f"  chi2(A_cal) = {chi2_gu_cal:.2f}  chi2_marg = {chi2m_gu:.2f}  "
        f"dchi2_self = {chi2_gu_cal - chi2m_gu:+.2f}  gap = {gap_gu:+.2f} sigma_A")
    check("CONTRAST: GU reproduces the H46C overshoot (gap > 3 sigma_A) in the same "
          "frame where DESI's own model passes", gap_gu > 3.0, f"{gap_gu:+.2f} sigma_A")
    check("CONTRAST guard: GU calibrated h matches H46C's 0.63749 to < 5e-4",
          abs(h_gu - 0.63749) < 5e-4, f"h={h_gu:.5f}")

    # -----------------------------------------------------------------------
    log("\n" + "-" * 78)
    log("DE-12 SUMMARY")
    log("-" * 78)
    log(f"  {'combo':22s} {'H0':>6s} {'Om':>7s} {'gap/sigA':>9s} {'dchi2_self':>11s} {'dAIC_self':>10s}")
    for name, r in rows.items():
        log(f"  {name:22s} {100*r['h']:6.2f} {r['Om']:7.4f} {r['gap']:+9.2f} "
            f"{r['d_self']:+11.3f} {r['daic_self']:+10.3f}")
    log(f"  {'LCDM (reference)':22s} {100*H_PLANCK:6.2f} {OMH2/H_PLANCK**2:7.4f} {gap_l:+9.2f} "
        f"{chi2_lcdm_planck - chi2m_l:+11.3f} {'':>10s}")
    log(f"  {'GU M2=8 f0=0.125':22s} {100*h_gu:6.2f} {OMH2/h_gu**2:7.4f} {gap_gu:+9.2f} "
        f"{chi2_gu_cal - chi2m_gu:+11.3f} {'':>10s}")

    if FAIL:
        log(f"\nFAILED: {FAIL}")
        sys.exit(1)
    log(f"\nexit 0 = DE-12 internal consistency recorded.  DESI+CMB w0waCDM: dchi2_self = "
        f"{r1['d_self']:+.3f}, dAIC_self = {r1['daic_self']:+.3f}, gap = {r1['gap']:+.2f} sigma_A "
        f"-> in-sample reproduction only; pipeline unbiasedness and C10 remain OPEN.")
    sys.exit(0)


if __name__ == "__main__":
    main()
