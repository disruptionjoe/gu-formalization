#!/usr/bin/env python3
r"""DE-12b -- SYNTHETIC-INJECTION positive control for the theta_star+BAO pipeline
(Wave A-2 redo; hostile-review finding 5).

WHY DE-12 WAS NOT ENOUGH.  The 2026-08-03 hostile review (lab/process/hostile-reviews/
2026-08-03-wave-a2-cosmology-bridge-review.md, finding 5) killed the original DE-12
reading: the reported DESI w0waCDM row is SELECTED FROM THE SAME DATA, so pushing it
through the pipeline is an in-sample consistency check, not an independent positive
control, an unbiasedness proof, or C10 certification.

THE REPLACEMENT (this script).  Synthetic injection with KNOWN truth:
  * Truth cosmologies declared a priori on a grid, DISJOINT from every H46B-verified
    DESI fit row: LCDM plus four w0waCDM points (preregistered in
    explorations/de-certification-redo-2026-08-03.md Section 1.1).
  * Each truth is generated SELF-CONSISTENTLY with the pipeline's frozen early physics
    (solve theta_star(h) = Planck for h at fixed omega_m h^2; generator-side A3 ratio
    correction; A_T = (c/H0_T)/r_drag) using a GENERATOR integrator numerically
    independent of the evaluator (adaptive quadrature per BAO row + Simpson calibration
    integrals, vs the evaluator's fixed-grid trapezoid).
  * Mock data = truth vector + noise ~ N(0, C), C = the byte-verified 13x13 DESI DR2
    covariance (Cholesky, seed 20260803), NREAL = 400 realizations per truth.
  * The DESI DR2 MEAN VECTOR IS NEVER USED.  Only the covariance (instrument model,
    not signal) enters, as the noise law and the chi^2 metric.
  * Evaluation models: the five truths, each at its OWN theta_star-calibrated
    amplitude computed by the byte-imported DE-12 fresh machinery (data-independent),
    plus GU (M^2 = 8, f0 = 0.125) through the identical H46C machinery (A3-corrected,
    with the shared A1 radiation term added to its rows for frame consistency).

CERTIFIES (preregistered SI-1..SI-6, hard asserts, exit couples; exact sampling
theory under the linear-Gaussian model):
  SI-1 noiseless self-recovery (generator/evaluator agreement; no circularity);
  SI-2 dAIC ~ 0 against itself -- the pipeline does NOT exclude an injected truth;
  SI-3 amplitude and marginalised-shape statistics unbiased at every truth;
  SI-4 wrong models ranked by their true noncentrality (resolvability floor 2);
  SI-5 the recovered shape gap reproduces the injected shape gap in the mean
       (the review's requirement (b): no systematic bias in the shape statistic);
  SI-6 GU's exclusion-scale noncentrality arises on data of KNOWN truth (the
       contrast responds to genuine mismatch, not a pipeline artifact).

SCOPE.  A full pass is the pipeline-unbiasedness certificate C10 needs (seat4
JP5/JP6): register status for C10 / M-H13 moves only via the register (reported by
the filing exploration, not edited here).  This certifies the REDUCED pipeline
(frozen early physics, fixed omega_m h^2, amplitude + amplitude-marginalised shape
statistics) on CPL-family and LCDM truths; it does not validate the GU background
solver's physics and does not touch the native record-law burden.

Run: PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python -u \
       tests/de-certification/de12b_synthetic_injection_positive_control.py
Exit 0 iff every preregistered assert holds.  Deterministic (seed 20260803).
"""
from __future__ import annotations
import os
import sys
import importlib.util
import numpy as np
from scipy.optimize import brentq
from scipy.integrate import quad, simpson

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
# EVALUATOR = the DE-12 fresh machinery, byte-imported (the object under test).
# ===========================================================================
DE12 = _load("tests/de-certification/de12_theta_star_positive_control.py", "DE12_mod")
H46C = DE12.H46C
H46 = DE12.H46

bao_vector_from_E = H46.bao_vector_from_E
DESI_COV = H46.DESI_COV
DESI_COV_INV = H46.DESI_COV_INV
DESI_ROWS = H46.DESI_ROWS

C_KMS = 299792.458
H_PLANCK = DE12.H_PLANCK
OMH2 = DE12.OMH2
RD = DE12.RD
RSTAR = DE12.RSTAR
ZSTAR = DE12.ZSTAR
THETASTAR_100 = DE12.THETASTAR_100
OMEGA_R_H2 = DE12.OMEGA_R_H2

theta100_cpl = DE12.theta100_cpl          # evaluator theta_star (trapezoid grids)
calibrate_h_cpl = DE12.calibrate_h_cpl    # evaluator calibration (brentq 0.50..0.85)
bao_grid_cpl = DE12.bao_grid_cpl          # evaluator BAO grid (1500-pt trapezoid)
rho_cpl = DE12.rho_cpl                    # closed-form CPL density (shared physics)

# ===========================================================================
# PREREGISTERED truth cosmologies (exploration Section 1.1).  Disjoint from the
# four H46B P1_CPL DESI fit rows; declared a priori, NOT selected from any data.
# ===========================================================================
TRUTHS = {
    "T0_LCDM":  (-1.00,  0.00),
    "T1":       (-0.80, -0.50),
    "T2":       (-1.20, +0.40),
    "T3":       (-0.70, +0.30),
    "T4":       (-1.05, -0.90),
}
DESI_FIT_ROWS = [(-0.42, -1.75), (-0.838, -0.62), (-0.667, -1.09), (-0.752, -0.86)]

NREAL = 400
SEED = 20260803
RESOLVABILITY_FLOOR = 2.0


# ===========================================================================
# GENERATOR -- numerically independent integrator (adaptive quadrature per BAO
# row; Simpson calibration integrals).  Same declared physics conventions as the
# evaluator (A1 additive radiation in every fresh-frame row; frozen Planck
# digits; A3 ratio correction applied generator-side with the generator's own
# LCDM calibration).
# ===========================================================================
def gen_E2(z, h, w0, wa):
    Om = OMH2 / h ** 2
    Or = OMEGA_R_H2 / h ** 2
    zp1 = 1.0 + np.asarray(z, dtype=float)
    return Om * zp1 ** 3 + Or * (zp1 ** 4 - 1.0) + (1.0 - Om) * rho_cpl(z, w0, wa)


def gen_theta100(h, w0, wa, nlo=6001, nhi=12001):
    zlo = np.linspace(0.0, 30.0, nlo)
    Ilo = simpson(1.0 / np.sqrt(gen_E2(zlo, h, w0, wa)), x=zlo)
    zhi = np.geomspace(30.0, ZSTAR, nhi)
    Ihi = simpson(1.0 / np.sqrt(gen_E2(zhi, h, w0, wa)), x=zhi)
    DM = (C_KMS / (100.0 * h)) * (Ilo + Ihi)
    return 100.0 * RSTAR / DM


def gen_calibrate_h(w0, wa):
    return brentq(lambda h: gen_theta100(h, w0, wa) - THETASTAR_100, 0.50, 0.85, xtol=1e-8)


def gen_bao_vector(h, w0, wa, A):
    """DESI-ordered 13-vector; comoving integral by ADAPTIVE quadrature per row."""
    out = np.empty(len(DESI_ROWS))
    for i, (z, q) in enumerate(DESI_ROWS):
        Ez = float(np.sqrt(gen_E2(z, h, w0, wa)))
        DC, _ = quad(lambda zz: 1.0 / np.sqrt(gen_E2(zz, h, w0, wa)), 0.0, z,
                     epsabs=1e-11, epsrel=1e-11, limit=200)
        DH = A / Ez
        DM = A * DC
        out[i] = DM if q == "DM" else (DH if q == "DH" else (z * DM ** 2 * DH) ** (1.0 / 3.0))
    return out


# ===========================================================================
# Mock-frame statistics (all chi^2 against MOCK data; DESI_MEAN never used).
# ===========================================================================
def chi2_vs(model_vec, data_vec):
    r = model_vec - data_vec
    return float(r @ DESI_COV_INV @ r)


def chi2_marg_vs(base_vec_at_A1, data_vec):
    b = base_vec_at_A1
    d = data_vec
    bCb = float(b @ DESI_COV_INV @ b)
    bCd = float(b @ DESI_COV_INV @ d)
    dCd = float(d @ DESI_COV_INV @ d)
    return dCd - bCd ** 2 / bCb, bCd / bCb


# ===========================================================================
def main():
    log("=" * 78)
    log("DE-12b -- SYNTHETIC-INJECTION positive control (known truths, DR2 covariance)")
    log("=" * 78)
    log(f"  truths (a priori, disjoint from H46B P1_CPL fit rows): "
        + ", ".join(f"{k}=({w0:+.2f},{wa:+.2f})" for k, (w0, wa) in TRUTHS.items()))
    log(f"  NREAL = {NREAL} per truth, seed = {SEED}; noise ~ N(0, C_DR2) (Cholesky)")
    for name, (w0, wa) in TRUTHS.items():
        for fw0, fwa in DESI_FIT_ROWS:
            assert not (abs(w0 - fw0) < 1e-9 and abs(wa - fwa) < 1e-9), \
                f"truth {name} collides with a DESI fit row -- preregistration violated"

    # -----------------------------------------------------------------------
    # Machinery certificate: evaluator anchors (re-asserted from DE-12's frame).
    # -----------------------------------------------------------------------
    log("\n" + "=" * 78)
    log("MC -- machinery certificates (evaluator = DE-12 fresh frame, byte-imported)")
    log("=" * 78)
    th_fresh = theta100_cpl(H_PLANCK, -1.0, 0.0)
    th_h46c = H46C.theta100_of(H_PLANCK, 1e-10)
    H46C._restore_module_cosmology()
    rel = abs(th_fresh - th_h46c) / th_h46c
    check("MC-1: evaluator LCDM theta* matches H46C's to < 1e-4 relative", rel < 1e-4,
          f"rel={rel:.2e}")
    h_lcdm_eval = calibrate_h_cpl(-1.0, 0.0)
    check("MC-2: evaluator LCDM calibration recovers h = 0.6736 within 0.2%",
          abs(h_lcdm_eval / H_PLANCK - 1.0) < 2e-3, f"h={h_lcdm_eval:.5f}")
    h_lcdm_gen = gen_calibrate_h(-1.0, 0.0)
    log(f"  generator LCDM calibration: h = {h_lcdm_gen:.6f} (evaluator {h_lcdm_eval:.6f};")
    log(f"  each frame divides out its OWN systematic via its A3 ratio)")
    check("MC-3: generator LCDM calibration recovers h = 0.6736 within 0.2%",
          abs(h_lcdm_gen / H_PLANCK - 1.0) < 2e-3, f"h={h_lcdm_gen:.6f}")

    # -----------------------------------------------------------------------
    # Build truths (generator side) and evaluation models (evaluator side).
    # -----------------------------------------------------------------------
    log("\n" + "=" * 78)
    log("BUILD -- truth mock means (generator) and model vectors (evaluator)")
    log("=" * 78)
    truth_mean = {}
    models = {}   # name -> dict(b=base@A1, A=own calibrated amplitude, m=b*A, sigA=..)
    for name, (w0, wa) in TRUTHS.items():
        # generator: truth mean vector, self-consistent with theta_star
        h_raw_g = gen_calibrate_h(w0, wa)
        h_g = h_raw_g * (H_PLANCK / h_lcdm_gen)          # generator-side A3
        A_g = C_KMS / (100.0 * h_g) / RD
        truth_mean[name] = gen_bao_vector(h_g, w0, wa, A_g)
        # evaluator: the SAME shape as an evaluation model (data-independent)
        h_raw_e = calibrate_h_cpl(w0, wa)
        h_e = h_raw_e * (H_PLANCK / h_lcdm_eval)         # evaluator-side A3
        A_e = C_KMS / (100.0 * h_e) / RD
        zg, Eg = bao_grid_cpl(h_e, w0, wa)
        b = bao_vector_from_E(zg, Eg, 1.0)
        sigA = 1.0 / np.sqrt(float(b @ DESI_COV_INV @ b))
        models[name] = dict(b=b, A=A_e, m=A_e * b, sigA=sigA, h=h_e)
        log(f"  {name:8s} (w0,wa)=({w0:+.2f},{wa:+.2f}): h_gen={h_g:.5f} A_gen={A_g:.4f} | "
            f"h_eval={h_e:.5f} A_eval={A_e:.4f} sigA={sigA:.4f}")

    # GU (M^2 = 8, f0 = 0.125) as an evaluation model (H46C machinery, A3-corrected).
    log("\n  GU (M^2=8, f0=0.125) through the identical H46C machinery:")
    h_lcdm_h46c = H46C.calibrate_h(1e-10)
    H46C._restore_module_cosmology()
    h_gu_raw = H46C.calibrate_h(H46C.F0_CANON)
    h_gu = h_gu_raw * (H_PLANCK / h_lcdm_h46c)
    A_gu = C_KMS / (100.0 * h_gu) / RD
    bg, _ = H46C._gu_background(h_gu, H46C.F0_CANON, npts=1400, n_iter=60)
    H46C._restore_module_cosmology()
    idx = np.argsort(bg["z"])
    zgu = bg["z"][idx]
    Or_gu = OMEGA_R_H2 / h_gu ** 2
    E2gu = bg["H2"][idx] + Or_gu * ((1.0 + zgu) ** 4 - 1.0)   # frame-consistent A1 rows
    b_gu = bao_vector_from_E(zgu, np.sqrt(E2gu), 1.0)
    sigA_gu = 1.0 / np.sqrt(float(b_gu @ DESI_COV_INV @ b_gu))
    models["GU_M2_8"] = dict(b=b_gu, A=A_gu, m=A_gu * b_gu, sigA=sigA_gu, h=h_gu)
    log(f"  GU: h_cal={h_gu:.5f} (H46C: 0.63749)  A_cal={A_gu:.4f}  sigA={sigA_gu:.4f}")
    check("MC-4: GU calibrated h matches H46C's 0.63749 to < 5e-4",
          abs(h_gu - 0.63749) < 5e-4, f"h={h_gu:.5f}")

    # -----------------------------------------------------------------------
    # SI-1 -- noiseless self-recovery (generator/evaluator independence bound).
    # -----------------------------------------------------------------------
    log("\n" + "=" * 78)
    log("SI-1 -- noiseless self-recovery (evaluator truth model vs generator mock mean)")
    log("=" * 78)
    for name in TRUTHS:
        mdl = models[name]
        mu = truth_mean[name]
        c2_0 = chi2_vs(mdl["m"], mu)
        _, Astar0 = chi2_marg_vs(mdl["b"], mu)
        gap0 = abs(mdl["A"] - Astar0) / mdl["sigA"]
        log(f"  {name:8s}: chi2_noiseless = {c2_0:.4f}   |A_eval - A*(mu)|/sigA = {gap0:.4f}")
        check(f"SI-1 {name}: noiseless chi2 < 0.05", c2_0 < 0.05, f"{c2_0:.4f}")
        check(f"SI-1 {name}: noiseless amplitude gap < 0.10 sigma_A", gap0 < 0.10,
              f"{gap0:.4f}")

    # -----------------------------------------------------------------------
    # Noise realizations (deterministic Cholesky draws).
    # -----------------------------------------------------------------------
    rng = np.random.default_rng(SEED)
    Lch = np.linalg.cholesky(DESI_COV)
    mocks = {name: truth_mean[name][None, :] + (rng.standard_normal((NREAL, 13)) @ Lch.T)
             for name in TRUTHS}

    # per (truth, model): chi2 at own calibrated amplitude; marg chi2 + A*
    stats = {}
    for tname in TRUTHS:
        D = mocks[tname]                                   # (NREAL, 13)
        per = {}
        for mname, mdl in models.items():
            R = mdl["m"][None, :] - D
            c2 = np.einsum("ij,jk,ik->i", R, DESI_COV_INV, R)
            b = mdl["b"]
            bCb = float(b @ DESI_COV_INV @ b)
            bCd = D @ (DESI_COV_INV @ b)
            dCd = np.einsum("ij,jk,ik->i", D, DESI_COV_INV, D)
            c2m = dCd - bCd ** 2 / bCb
            per[mname] = dict(c2=c2, c2m=c2m, Astar=bCd / bCb)
        stats[tname] = per

    # -----------------------------------------------------------------------
    # SI-2 / SI-3 -- self rows: no self-exclusion; unbiased amplitude and shape.
    # -----------------------------------------------------------------------
    log("\n" + "=" * 78)
    log("SI-2/SI-3 -- self rows over noise (chi2_13 / chi2_1 / chi2_12 / N(A_T, sigA^2))")
    log("=" * 78)
    log(f"  {'truth':8s} {'<chi2(Acal)>':>12s} {'<d_self>':>9s} {'<dAIC_self>':>11s} "
        f"{'<chi2_marg>':>11s} {'A-bias/sigA':>11s}")
    for name in TRUTHS:
        s = stats[name][name]
        mdl = models[name]
        m_c2 = float(np.mean(s["c2"]))
        d_self = s["c2"] - s["c2m"]
        m_dself = float(np.mean(d_self))
        m_daic = m_dself - 2.0
        m_c2m = float(np.mean(s["c2m"]))
        bias = float(np.mean(s["Astar"]) - mdl["A"]) / mdl["sigA"]
        log(f"  {name:8s} {m_c2:12.3f} {m_dself:9.3f} {m_daic:+11.3f} {m_c2m:11.3f} "
            f"{bias:+11.4f}")
        check(f"SI-2 {name}: |mean d_self - 1| < 0.35 (no self-exclusion)",
              abs(m_dself - 1.0) < 0.35, f"{m_dself:.3f}")
        check(f"SI-2 {name}: mean dAIC_self in (-2, +2) (dAIC ~ 0 vs itself)",
              -2.0 < m_daic < 2.0, f"{m_daic:+.3f}")
        check(f"SI-2 {name}: |mean chi2(A_cal) - 13| < 1.2", abs(m_c2 - 13.0) < 1.2,
              f"{m_c2:.3f}")
        check(f"SI-3 {name}: amplitude bias |mean A* - A_T| < 0.25 sigma_A",
              abs(bias) < 0.25, f"{bias:+.4f}")
        check(f"SI-3 {name}: |mean chi2_marg - 12| < 1.2 (shape statistic unbiased)",
              abs(m_c2m - 12.0) < 1.2, f"{m_c2m:.3f}")

    # -----------------------------------------------------------------------
    # SI-4 -- ranking: wrong models ranked by their true noncentrality.
    # -----------------------------------------------------------------------
    log("\n" + "=" * 78)
    log("SI-4 -- ranking over noise (floor: noiseless Delta >= 2)")
    log("=" * 78)
    log(f"  {'truth':8s} {'model':8s} {'Delta_nl':>9s} {'<dchi2>':>9s} {'SE':>7s} "
        f"{'frac(truth wins)':>17s}")
    truth_names = list(TRUTHS)
    for tname in truth_names:
        mu = truth_mean[tname]
        for mname in truth_names:
            if mname == tname:
                continue
            Delta_nl = chi2_vs(models[mname]["m"], mu)     # noiseless noncentrality
            d = stats[tname][mname]["c2"] - stats[tname][tname]["c2"]
            m_d = float(np.mean(d))
            se = float(np.std(d, ddof=1) / np.sqrt(NREAL))
            frac = float(np.mean(d > 0.0))
            tag = "asserted" if Delta_nl >= RESOLVABILITY_FLOOR else "below floor (reported)"
            log(f"  {tname:8s} {mname:8s} {Delta_nl:9.3f} {m_d:9.3f} {se:7.3f} "
                f"{frac:17.3f}  [{tag}]")
            if Delta_nl >= RESOLVABILITY_FLOOR:
                check(f"SI-4 {tname}<-{mname}: mean(chi2_M - chi2_T) > 0", m_d > 0.0,
                      f"{m_d:.3f}")
                band = max(0.25, 5.0 * se)
                check(f"SI-4 {tname}<-{mname}: |mean - Delta_nl| < max(0.25, 5 SE)",
                      abs(m_d - Delta_nl) < band, f"|{m_d:.3f}-{Delta_nl:.3f}|, band={band:.3f}")
                check(f"SI-4 {tname}<-{mname}: frac preferring truth >= 0.60",
                      frac >= 0.60, f"{frac:.3f}")
            if Delta_nl >= 25.0:
                check(f"SI-4 {tname}<-{mname}: frac preferring truth >= 0.95 (Delta >= 25)",
                      frac >= 0.95, f"{frac:.3f}")

    # -----------------------------------------------------------------------
    # SI-5 -- shape-gap unbiasedness (the review's requirement (b)).
    # -----------------------------------------------------------------------
    log("\n" + "=" * 78)
    log("SI-5 -- recovered shape gap vs injected shape gap (amplitude-marginalised)")
    log("=" * 78)
    log(f"  {'truth':8s} {'model':8s} {'lambda_nl':>10s} {'<marg gap>':>11s} {'SE':>7s}")
    for tname in truth_names:
        mu = truth_mean[tname]
        for mname in truth_names:
            if mname == tname:
                continue
            lam_nl, _ = chi2_marg_vs(models[mname]["b"], mu)   # noiseless marg gap vs mu
            g = stats[tname][mname]["c2m"] - stats[tname][tname]["c2m"]
            m_g = float(np.mean(g))
            se = float(np.std(g, ddof=1) / np.sqrt(NREAL))
            band = max(0.5, 5.0 * se)
            log(f"  {tname:8s} {mname:8s} {lam_nl:10.3f} {m_g:11.3f} {se:7.3f}")
            check(f"SI-5 {tname}<-{mname}: |mean marg gap - lambda_nl| < max(0.5, 5 SE)",
                  abs(m_g - lam_nl) < band, f"|{m_g:.3f}-{lam_nl:.3f}|, band={band:.3f}")

    # -----------------------------------------------------------------------
    # SI-6 -- GU contrast: exclusion-scale noncentrality on data of KNOWN truth.
    # -----------------------------------------------------------------------
    log("\n" + "=" * 78)
    log("SI-6 -- GU (M^2=8, f0=0.125) against every injected truth")
    log("=" * 78)
    for tname in truth_names:
        mu = truth_mean[tname]
        Delta_gu = chi2_vs(models["GU_M2_8"]["m"], mu)
        d = stats[tname]["GU_M2_8"]["c2"] - stats[tname][tname]["c2"]
        frac = float(np.mean(d > 0.0))
        log(f"  {tname:8s}: Delta_GU(noiseless) = {Delta_gu:8.3f}   "
            f"frac(GU ranked worse) = {frac:.3f}")
        check(f"SI-6 {tname}: Delta_GU >= 9 (exclusion responds to real mismatch)",
              Delta_gu >= 9.0, f"{Delta_gu:.3f}")
        if Delta_gu >= 25.0:
            check(f"SI-6 {tname}: frac(GU worse) >= 0.95 (Delta >= 25)", frac >= 0.95,
                  f"{frac:.3f}")

    # -----------------------------------------------------------------------
    log("\n" + "-" * 78)
    log("DISPOSITION")
    log("-" * 78)
    if FAIL:
        log("  *** LOUD FAIL: the pipeline shows bias against data of KNOWN truth.")
        log("  *** Every number in the wave45/46/W129 exclusion chain is SUSPECT until")
        log("  *** resolved.  Do not cite the +19.3 / +35.78 / +21.58 chain.")
        log(f"\nFAILED: {FAIL}")
        sys.exit(1)
    log("  All preregistered SI-1..SI-6 checks hold: the theta_star+BAO reduced")
    log("  pipeline neither excludes injected truths nor biases the recovered")
    log("  amplitude/shape statistics, and ranks wrong models by their true")
    log("  noncentrality.  This is the synthetic-injection unbiasedness certificate")
    log("  the hostile review required in place of the in-sample DE-12 reading.")
    log("  Register status for C10 / M-H13 moves only via the register.")
    log("\nexit 0 = synthetic-injection positive control PASSED "
        f"({len(TRUTHS)} truths x {NREAL} realizations, seed {SEED}).")
    sys.exit(0)


if __name__ == "__main__":
    main()
