#!/usr/bin/env python3
"""DE amplitude audit probe -- Lane 2 DE-AMP-DIAGNOSTIC executed per the portfolio
spec, everything load-bearing RECOMPUTED FROM SCRATCH (fresh solver, fresh
calibration, fresh likelihood assembly; no cosmology imported from the H44/H46
modules -- they are imported ONLY to verify that this probe's embedded data
arrays are bitwise identical to the H46B-verified official DESI DR2 inputs).

CHANNEL: Lane 2 / DE-AMP-DIAGNOSTIC ("Audit the CMB-calibrated dark-energy
         amplitude"; next_swing: re-solve theta_star with GU's own full
         D_M(z_star) including the high-redshift tail, then return a blind
         official-H46B likelihood adjudication).
AXIOM:   lab/process/boundary-adapter-standing-axiom.md
DESIGN:  explorations/de-amplitude-audit-2026-07-20.md
EXTENDS: tests/wave46/H46C_theta_star_cmb_calibration.py (prior execution)
         tests/W129_oq2_m2_band_sweep.py (band scope, cited)
         tests/channel-swings/bb_p1_sign_covariance_probe.py (sign conventions)
STATUS:  exploration tier; diagnostic; no claim, canon, or posture movement.

DISCIPLINE (per the DE-AMP-DIAGNOSTIC forbidden_shortcut and archaeology item 9):
  * Only H46B-verified likelihood inputs seed the calculation. The 13-dim DESI
    DR2 BAO mean/covariance and the Planck 2018 digits are embedded verbatim and
    cross-checked bitwise against the repo's H46B-verified modules ([T]).
  * NOTHING is trusted from cache: the backreacted background, the theta_star
    calibration, the 4.229-class coefficient d ln rho_B/dz|_0 (the quantity the
    historical hard-coded-3 bug corrupted -- DARK-ENERGY-03), and the canon
    Result-2 coefficient C (w_0 = -1 + C f_0) are all recomputed from scratch
    by an independent implementation ([E]).
  * CONFRONTATION SEPARATION: the COSMO-A1 bracket rho_DE ~ (2.24 meV)^4 and
    the DESI data vector are CONFRONTATION data. The calibration pipeline is
    structurally blind to them; check F1 executes the blindness (perturbing the
    DESI vector does not move the calibrated h by one part in 1e12), and the
    meV bracket constant is not defined until every calibration output has been
    computed and frozen in AUDIT_OUT. Calibration leakage = automatic invalidity.
  * This is data hygiene and compatibility testing, not a decisive or
    distinctive GU prediction (portfolio forbidden_shortcut, quoted).

CONSTRUCTIONS USED (GEOMETER-VS-PHYSICS-OBJECTS discipline, named):
  * GU side: the PROGRAM-NATIVE two-component dark-energy background --
    DeWitt-Lambda (w = -1) plus the theta magnitude mode as a linear KG field
    with M^2 in the root-system band {3, 7, 8} H0^2 (reconstruction grade,
    OQ2 open; NOT a tuned mass parameter). The scale structure is the native
    RATIO-ONLY one (H24 / PRED-NORM-RANK): the geometry fixes dimensionless
    ratios; NO absolute amplitude is GU-derivable at the current grade; checks
    E10/E11 exhibit this ratio-only structure computationally.
  * Observational side: the STANDARD late-time likelihood apparatus (Planck
    theta_star calibration, DESI DR2 BAO Gaussian likelihood), used because the
    diagnostic asks whether the CMB-calibrated amplitude leg survives official
    likelihood inputs. Using it does not convert anything into a GU-native
    derivation; the amplitude A = (c/H0)/r_d is built ENTIRELY from imported
    quantities. The one construction slot where an absolute scale could enter
    GU is the B.5 global datum (P5 dossier Element 2, spectral-section cut
    scale): a native-shaped SLOT with a pure empirical IMPORT for its value.

HIGH-REDSHIFT TAIL (the spec's "full D_M(z_star)"): two treatments are run.
  R-A: the H46C treatment (additive radiation keeping E(0) = 1 exactly;
       frozen theta density above z_start = 30).
  R-B: exact-budget treatment (radiation as a genuine component Or a^-4 in
       BOTH H^2 and the KG friction, flat closure OL = 1 - Om - Or, so the
       high-z tail is the full component sum with no additive bookkeeping).
  The verdict must be tail-robust (E7): if the two treatments disagreed
  materially the H46C conclusion would inherit a tail systematic.

Run: python -u tests/channel-swings/de_amplitude_audit_probe.py
Exit 0 iff every check passes. HEADLINE line printed last.
"""
from __future__ import annotations

import importlib.util
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = []


def check(tag, name, ok, detail=""):
    RESULTS.append((tag, name, bool(ok)))
    line = f"[{tag}] {'PASS' if ok else 'FAIL'}  {name}"
    if detail:
        line += f"   ({detail})"
    print(line, flush=True)
    return bool(ok)


def log(m=""):
    print(m, flush=True)


# =============================================================================
# Constants: Planck 2018 (arXiv:1807.06209 Table 2, TT,TE,EE+lowE+lensing) --
# repo-verified digits (Wave 45/46). Embedded; cross-checked against the H46C
# module in T3. These are IMPORTS (standard-physics data), not GU quantities.
# =============================================================================
C_KMS = 299792.458
H_PLANCK = 0.6736
OMH2 = 0.1430
RD = 147.09                       # r_drag [Mpc]
RSTAR = 144.43                    # r_star [Mpc]
ZSTAR = 1089.92
THETASTAR_100 = 1.04110
OMEGA_G_H2 = 2.4728e-5            # photons, T0 = 2.7255 K
OMEGA_R_H2 = OMEGA_G_H2 * (1.0 + 0.2271 * 3.046)
A_PLANCK = C_KMS / (H_PLANCK * 100.0 * RD)     # 30.2625...

Z_START = 30.0
M2_BC1 = 8.0                      # BC_1 ground eigenvalue (root system; NOT tuned)
M2_BAND = [3.0, 7.0, 8.0]         # S^3 / A_1 / BC_1 admissible band (OQ2)
F0_CANON = 0.125                  # CPL-tuned reference amplitude (a FIT, not GU)

# =============================================================================
# DESI DR2 BAO official likelihood inputs (Cobaya bao_data desi_bao_dr2/;
# arXiv:2503.14738 Table IV). Embedded verbatim; T1 verifies bitwise equality
# with the repo's H46B-verified module. CONFRONTATION DATA ONLY.
# =============================================================================
DESI_ROWS = [
    (0.295, "DV"),
    (0.510, "DM"), (0.510, "DH"),
    (0.706, "DM"), (0.706, "DH"),
    (0.934, "DM"), (0.934, "DH"),
    (1.321, "DM"), (1.321, "DH"),
    (1.484, "DM"), (1.484, "DH"),
    (2.330, "DH"), (2.330, "DM"),
]
DESI_MEAN = np.array([
    7.94167639,
    13.58758434, 21.86294686,
    17.35069094, 19.45534918,
    21.57563956, 17.64149464,
    27.60085612, 14.17602155,
    30.51190063, 12.81699964,
    8.631545674846294, 38.988973961958784,
])
DESI_COV = np.zeros((13, 13))
DESI_COV[0, 0] = 5.78998687e-03
_blocks = [
    (1, 2, 2.83473742e-02, 1.83928040e-01, -3.26062007e-02),
    (3, 4, 3.23752442e-02, 1.11469198e-01, -2.37445646e-02),
    (5, 6, 2.61732816e-02, 4.04183878e-02, -1.12938006e-02),
    (7, 8, 1.05336516e-01, 5.04233092e-02, -2.90308418e-02),
    (9, 10, 5.83020277e-01, 2.68336193e-01, -1.95215562e-01),
    (11, 12, 1.02136194e-02, 2.82685779e-01, -2.31395216e-02),
]
for i, j, vii, vjj, vij in _blocks:
    DESI_COV[i, i] = vii
    DESI_COV[j, j] = vjj
    DESI_COV[i, j] = DESI_COV[j, i] = vij
DESI_COV_INV = np.linalg.inv(DESI_COV)


# =============================================================================
# FRESH background solver (independent implementation; physics identical to the
# frozen H44 model spec, code written from scratch). Two-component DE:
# rho_L (w = -1) + linear KG theta mode; self-consistent Friedmann via fixed
# point on H^2(N), N = ln a; deterministic RK4; optional exact radiation.
# =============================================================================
def solve_bg(M2, f0, Om, Or=0.0, z_start=Z_START, npts=700, n_iter=60,
             tol=1e-12, B0=1.0):
    """Returns the self-consistent background on [0, z_start].

    Flat closure: Om + Or + rho_L + rho_theta(0) = 1, with
    rho_L = OL/(1+f0), rho_theta(0) = OL f0/(1+f0), OL = 1 - Om - Or.
    KG (in N): B'' + (3 + H'/H) B' + (M2/H^2) B = 0, slow-roll attractor IC
    at z_start: B = B0, B' = -M2 B0 / (3 H^2). Radiation, when present,
    contributes rho + p = (4/3) rho_r to the friction exactly.
    """
    OL = 1.0 - Om - Or
    rho_L = OL / (1.0 + f0)
    rho_th0 = OL * f0 / (1.0 + f0)
    N0 = np.log(1.0 / (1.0 + z_start))
    N = np.linspace(N0, 0.0, npts)
    hN = N[1] - N[0]
    Nm = 0.5 * (N[:-1] + N[1:])
    a = np.exp(N)
    am = np.exp(Nm)
    rho_m, rho_mm = Om * a ** -3, Om * am ** -3
    rho_r, rho_rm = Or * a ** -4, Or * am ** -4

    H2 = rho_m + rho_r + OL
    rho_th = np.zeros(npts)
    p_th = np.zeros(npts)
    B = np.ones(npts) * B0
    BN = np.zeros(npts)
    dlast = np.inf
    for _ in range(n_iter):
        fric = -1.5 * (rho_m + (4.0 / 3.0) * rho_r + rho_th + p_th) / H2
        H2m = np.interp(Nm, N, H2)
        fricm = np.interp(Nm, N, fric)
        B[0] = B0
        BN[0] = -M2 * B0 / (3.0 * H2[0])
        for i in range(npts - 1):
            b, d = B[i], BN[i]
            k1b = d
            k1d = -(3.0 + fric[i]) * d - (M2 / H2[i]) * b
            b2, d2 = b + 0.5 * hN * k1b, d + 0.5 * hN * k1d
            k2b = d2
            k2d = -(3.0 + fricm[i]) * d2 - (M2 / H2m[i]) * b2
            b3, d3 = b + 0.5 * hN * k2b, d + 0.5 * hN * k2d
            k3b = d3
            k3d = -(3.0 + fricm[i]) * d3 - (M2 / H2m[i]) * b3
            b4, d4 = b + hN * k3b, d + hN * k3d
            k4b = d4
            k4d = -(3.0 + fric[i + 1]) * d4 - (M2 / H2[i + 1]) * b4
            B[i + 1] = b + (hN / 6.0) * (k1b + 2 * k2b + 2 * k3b + k4b)
            BN[i + 1] = d + (hN / 6.0) * (k1d + 2 * k2d + 2 * k3d + k4d)
        Bdot = np.sqrt(H2) * BN
        KE = 0.5 * Bdot ** 2
        PE = 0.5 * M2 * B ** 2
        norm = rho_th0 / (KE[-1] + PE[-1])
        rho_new = norm * (KE + PE)
        p_new = norm * (KE - PE)
        H2_new = rho_m + rho_r + rho_L + rho_new
        dlast = float(np.max(np.abs(H2_new - H2)))
        rho_th, p_th, H2 = rho_new, p_new, H2_new
        if dlast < tol:
            break
    w_th = p_th / rho_th if f0 > 0 else np.zeros(npts)
    return dict(N=N, a=a, z=1.0 / a - 1.0, B=B.copy(), H2=H2, rho_th=rho_th,
                p_th=p_th, w_th=w_th, rho_L=rho_L, OL=OL, delta=dlast)


def w_de(bg):
    """Combined two-component DE EOS (exact identity of the frozen model)."""
    return (-bg["rho_L"] + bg["p_th"]) / (bg["rho_L"] + bg["rho_th"])


# =============================================================================
# FRESH theta_star pipeline: full D_M(z_star) with the high-z tail, two
# radiation treatments; bisection calibration. NO DESI QUANTITY APPEARS HERE.
# =============================================================================
def dm_integral(h, f0, M2=M2_BC1, treatment="A", npts=700, n_iter=50,
                ntail=4000):
    """I = int_0^{z_star} dz / E(z); D_M = (c / (100 h)) * I."""
    Om_h = OMH2 / h ** 2
    Or_h = OMEGA_R_H2 / h ** 2
    if treatment == "A":
        bg = solve_bg(M2, f0, Om_h, Or=0.0, npts=npts, n_iter=n_iter)
        idx = np.argsort(bg["z"])
        zl = bg["z"][idx]
        E2l = bg["H2"][idx] + Or_h * ((1.0 + zl) ** 4 - 1.0)
        rho_f = float(bg["rho_th"][0])
        zt = np.geomspace(Z_START, ZSTAR, ntail)
        E2t = (Om_h * (1.0 + zt) ** 3 + Or_h * ((1.0 + zt) ** 4 - 1.0)
               + bg["rho_L"] + rho_f)
    else:
        bg = solve_bg(M2, f0, Om_h, Or=Or_h, npts=npts, n_iter=n_iter)
        idx = np.argsort(bg["z"])
        zl = bg["z"][idx]
        E2l = bg["H2"][idx]
        rho_f = float(bg["rho_th"][0])
        zt = np.geomspace(Z_START, ZSTAR, ntail)
        E2t = (Om_h * (1.0 + zt) ** 3 + Or_h * (1.0 + zt) ** 4
               + bg["rho_L"] + rho_f)
    Il = np.trapezoid(1.0 / np.sqrt(E2l), zl)
    It = np.trapezoid(1.0 / np.sqrt(E2t), zt)
    frozen_frac = rho_f / (Om_h * (1.0 + Z_START) ** 3) if f0 > 0 else 0.0
    return Il + It, frozen_frac


def theta100(h, f0, **kw):
    I, _ = dm_integral(h, f0, **kw)
    DM = (C_KMS / (100.0 * h)) * I
    return 100.0 * RSTAR / DM


def calibrate(f0, target=THETASTAR_100, lo=0.55, hi=0.80, xtol=2e-6, **kw):
    """Bisection solve of theta100(h) = target (fresh implementation)."""
    flo = theta100(lo, f0, **kw) - target
    fhi = theta100(hi, f0, **kw) - target
    if flo * fhi > 0:
        raise RuntimeError("calibration bracket does not straddle the target")
    while hi - lo > xtol:
        mid = 0.5 * (lo + hi)
        fm = theta100(mid, f0, **kw) - target
        if flo * fm <= 0:
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm
    return 0.5 * (lo + hi)


# =============================================================================
# FRESH BAO likelihood assembly.
# =============================================================================
def bao_vector(zg, Eg, A):
    zint = np.concatenate([[0.0], zg]) if zg[0] > 0 else zg
    Eint = np.concatenate([[1.0], Eg]) if zg[0] > 0 else Eg
    dI = 0.5 * np.diff(zint) * (1.0 / Eint[1:] + 1.0 / Eint[:-1])
    DC = np.concatenate([[0.0], np.cumsum(dI)])
    out = np.empty(len(DESI_ROWS))
    for i, (z, q) in enumerate(DESI_ROWS):
        Ez = np.interp(z, zint, Eint)
        DH = A / Ez
        DM = A * np.interp(z, zint, DC)
        out[i] = (DM if q == "DM"
                  else DH if q == "DH"
                  else (z * DM ** 2 * DH) ** (1.0 / 3.0))
    return out


def chi2_of(vec):
    r = vec - DESI_MEAN
    return float(r @ DESI_COV_INV @ r)


def chi2_marg(base):
    bCb = float(base @ DESI_COV_INV @ base)
    bCd = float(base @ DESI_COV_INV @ DESI_MEAN)
    dCd = float(DESI_MEAN @ DESI_COV_INV @ DESI_MEAN)
    return dCd - bCd ** 2 / bCb, bCd / bCb, 1.0 / np.sqrt(bCb)


# =============================================================================
def main():
    global DESI_MEAN
    log("=" * 78)
    log("DE AMPLITUDE AUDIT PROBE -- Lane 2 DE-AMP-DIAGNOSTIC, recomputed from scratch")
    log("=" * 78)

    # -------------------------------------------------------------------------
    # [T] setup: verify this probe's embedded data == the H46B-verified inputs.
    # -------------------------------------------------------------------------
    log("\n--- [T] setup: seed verification against H46B-verified repo modules ---")
    h46_path = os.path.normpath(os.path.join(
        HERE, "..", "wave29", "H46_de_raw_bao_likelihood.py"))
    h46c_path = os.path.normpath(os.path.join(
        HERE, "..", "wave46", "H46C_theta_star_cmb_calibration.py"))
    try:
        spec = importlib.util.spec_from_file_location("H46_seed_check", h46_path)
        H46 = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(H46)
        same_mean = np.array_equal(DESI_MEAN, H46.DESI_MEAN)
        same_cov = np.array_equal(DESI_COV, H46.DESI_COV)
        check("T", "embedded DESI DR2 13-dim mean and covariance are bitwise "
                   "identical to the H46B-verified repo module (only H46B-verified "
                   "likelihood inputs seed this audit)", same_mean and same_cov)
    except Exception as exc:                                  # pragma: no cover
        check("T", "H46B-verified module cross-check importable", False, repr(exc))

    check("T", "DESI covariance symmetric positive definite (valid likelihood)",
          np.allclose(DESI_COV, DESI_COV.T)
          and bool(np.all(np.linalg.eigvalsh(DESI_COV) > 0)))

    try:
        spec_c = importlib.util.spec_from_file_location("H46C_seed_check", h46c_path)
        H46C = importlib.util.module_from_spec(spec_c)
        spec_c.loader.exec_module(H46C)
        same_planck = (H46C.THETASTAR_100 == THETASTAR_100
                       and H46C.RSTAR == RSTAR and H46C.ZSTAR == ZSTAR
                       and H46C.RD == RD and H46C.OMH2 == OMH2
                       and H46C.OMEGA_R_H2 == OMEGA_R_H2)
        check("T", "embedded Planck 2018 digits identical to the repo-verified "
                   "H46C constants (100theta*, r*, z*, r_drag, omega_m h^2, omega_r)",
              same_planck)
    except Exception as exc:                                  # pragma: no cover
        check("T", "H46C constants cross-check importable", False, repr(exc))

    # fresh solver control: f0 -> 0 reduces to LCDM
    bg0 = solve_bg(M2_BC1, 1e-8, 0.315, npts=700)
    H2err = float(np.max(np.abs(bg0["H2"] - (0.315 * bg0["a"] ** -3 + 0.685))))
    check("T", "fresh solver control: f0 -> 0 background reduces to LCDM "
               "(independent implementation, no ODE bug)", H2err < 1e-6,
          f"max|dH2| = {H2err:.1e}")

    # positive controls: LCDM reproduces the measured angle in both treatments
    thA = theta100(H_PLANCK, 1e-10, treatment="A")
    thB = theta100(H_PLANCK, 1e-10, treatment="B")
    rA = (thA - THETASTAR_100) / THETASTAR_100
    rB = (thB - THETASTAR_100) / THETASTAR_100
    log(f"  PC1: 100theta*(LCDM, h=0.6736): R-A {thA:.5f} ({rA:+.1e}), "
        f"R-B {thB:.5f} ({rB:+.1e}); Planck {THETASTAR_100}")
    check("T", "PC1: LCDM pipeline reproduces Planck 100theta* to < 0.2% in BOTH "
               "tail treatments", abs(rA) < 2e-3 and abs(rB) < 2e-3,
          f"R-A {rA:+.1e}, R-B {rB:+.1e}")

    th_hi = theta100(H_PLANCK, 1e-10, treatment="A", npts=1400, ntail=9000)
    gc = abs(th_hi - thA) / thA
    check("T", "grid convergence: doubling grids shifts theta* < 5e-5 relative",
          gc < 5e-5, f"{gc:.1e}")

    hL_A = calibrate(1e-10, treatment="A")
    hL_B = calibrate(1e-10, treatment="B")
    log(f"  PC2: LCDM calibrated h: R-A {hL_A:.5f}, R-B {hL_B:.5f} (Planck 0.6736)")
    check("T", "PC2: LCDM theta* calibration recovers h = 0.6736 within 0.2% "
               "(both treatments); residual = shared pipeline systematic, divided "
               "out of every GU result below", abs(hL_A / H_PLANCK - 1) < 2e-3
          and abs(hL_B / H_PLANCK - 1) < 2e-3)

    # -------------------------------------------------------------------------
    # [E] recomputations: coefficients first (the bug-class guard).
    # -------------------------------------------------------------------------
    log("\n--- [E] load-bearing coefficients recomputed from scratch ---")
    bg_small = solve_bg(M2_BC1, 0.01, 0.315, npts=1400)
    lnr = np.log(bg_small["rho_th"])
    hN = bg_small["N"][1] - bg_small["N"][0]
    dlnr_dN = (3.0 * lnr[-1] - 4.0 * lnr[-2] + lnr[-3]) / (2.0 * hN)
    dlnr_dz0 = -dlnr_dN            # dN/dz = -1 at z = 0
    log(f"  d ln rho_B/dz|_0 = {dlnr_dz0:+.3f}   (archaeology 4.229; bb-p1 4.307; "
        f"the historical bug hard-coded 3)")
    check("E", "the 4.229-class coefficient recomputed from scratch: "
               "d ln rho_B/dz|_0 in [3.9, 4.7] and NOT the hard-coded 3 "
               "(DARK-ENERGY-03 bug class re-excluded by direct computation)",
          3.9 < dlnr_dz0 < 4.7 and abs(dlnr_dz0 - 3.0) > 0.8,
          f"{dlnr_dz0:+.3f}")

    c_vals = []
    for f0s in (0.01, 0.02):
        bgc = solve_bg(M2_BC1, f0s, 0.315, npts=1400)
        w0_de = float(w_de(bgc)[-1])
        c_vals.append((1.0 + w0_de) * (1.0 + f0s) / f0s)
    log(f"  canon Result-2 coefficient C (w_0 = -1 + C f_0): "
        f"{c_vals[0]:.3f} (f0=0.01), {c_vals[1]:.3f} (f0=0.02)  [canon 1.39, bb-p1 1.438]")
    check("E", "canon Result-2 coefficient recomputed: C in [1.30, 1.50] and "
               "stable in f0 to < 2% (w_0 side is quintessence for C > 0)",
          all(1.30 < c < 1.50 for c in c_vals)
          and abs(c_vals[0] / c_vals[1] - 1) < 0.02,
          f"C = {c_vals[0]:.3f}/{c_vals[1]:.3f}")

    # row 1 reproduction: fixed Planck amplitude on the source-Om background
    bg_c = solve_bg(M2_BC1, F0_CANON, 0.315, npts=1400)
    idx = np.argsort(bg_c["z"])
    zc, Ec = bg_c["z"][idx], np.sqrt(bg_c["H2"][idx])
    E_l = np.sqrt(0.315 * (1.0 + zc) ** 3 + 0.685)
    chi2_gu_r1 = chi2_of(bao_vector(zc, Ec, A_PLANCK))
    chi2_l = chi2_of(bao_vector(zc, E_l, A_PLANCK))
    log(f"  Row 1 (fixed Planck A): chi2_GU = {chi2_gu_r1:.2f}, chi2_LCDM = "
        f"{chi2_l:.2f}, dchi2 = {chi2_gu_r1-chi2_l:+.2f}  [H46 chain: 52.26/30.68/+21.58]")
    check("E", "independent implementation reproduces the H46 chain row 1: "
               "chi2 52.26 / 30.68 within 0.30 (fresh solver + fresh likelihood)",
          abs(chi2_gu_r1 - 52.26) < 0.30 and abs(chi2_l - 30.68) < 0.30,
          f"{chi2_gu_r1:.2f}/{chi2_l:.2f}")

    # -------------------------------------------------------------------------
    # [E] the re-solve: GU's own CMB-calibrated amplitude, full tail, both
    # treatments (the spec's next_swing).
    # -------------------------------------------------------------------------
    log("\n--- [E] GU's own theta_star calibration (full D_M(z_star), both tails) ---")
    hG_A_raw = calibrate(F0_CANON, treatment="A")
    hG_B_raw = calibrate(F0_CANON, treatment="B")
    hG_A = hG_A_raw * (H_PLANCK / hL_A)     # ratio-correct vs own-treatment control
    hG_B = hG_B_raw * (H_PLANCK / hL_B)
    A_gu_A = C_KMS / (100.0 * hG_A) / RD
    A_gu_B = C_KMS / (100.0 * hG_B) / RD
    Om_gu = OMH2 / hG_A ** 2
    _, ffrac = dm_integral(hG_A_raw, F0_CANON, treatment="A")
    log(f"  R-A: h_GU = {hG_A:.5f} (H0 = {100*hG_A:.2f}), A_GU = {A_gu_A:.4f}, "
        f"Om = {Om_gu:.4f}   [H46C: 0.6375 / 63.75 / 31.97 / 0.352]")
    log(f"  R-B: h_GU = {hG_B:.5f} (H0 = {100*hG_B:.2f}), A_GU = {A_gu_B:.4f}")
    log(f"  frozen-theta tail fraction at z_start: {ffrac:.2e} (early physics untouched)")
    check("E", "GU calibration recomputed independently and lands on the H46C "
               "point: |A_GU - 31.97| < 0.15 and h_GU < h_Planck (direction: extra "
               "past DE -> smaller D_M -> lower calibrated h)",
          abs(A_gu_A - 31.97) < 0.15 and hG_A < H_PLANCK,
          f"A_GU = {A_gu_A:.4f}, h_GU = {hG_A:.5f}")
    check("E", "frozen-theta density negligible vs matter at z_start (< 1e-3): "
               "the calibration legitimately fixes r*, z*, r_drag at Planck values",
          ffrac < 1e-3, f"{ffrac:.2e}")
    tail_shift = abs(A_gu_B / A_gu_A - 1.0)
    check("E", "TAIL-ROBUST: the exact-budget high-z treatment (R-B: radiation as "
               "a true component in H^2 AND the KG friction, flat closure) shifts "
               "the ratio-corrected amplitude by < 0.2% -- the H46C verdict does "
               "not carry a tail systematic", tail_shift < 2e-3,
          f"|dA/A| = {tail_shift:.2e}")

    # row 2: own-calibration likelihood adjudication (blind: A fixed upstream)
    bg_g = solve_bg(M2_BC1, F0_CANON, OMH2 / hG_A ** 2, npts=1400)
    ig = np.argsort(bg_g["z"])
    zg, Eg = bg_g["z"][ig], np.sqrt(bg_g["H2"][ig])
    chi2_gu_r2 = chi2_of(bao_vector(zg, Eg, A_gu_A))
    daic2 = chi2_gu_r2 - chi2_l
    _, Astar, sigA = chi2_marg(bao_vector(zg, Eg, 1.0))
    gap = (A_gu_A - Astar) / sigA
    log(f"  Row 2 (own theta* calibration): chi2_GU = {chi2_gu_r2:.2f}, dAIC = "
        f"{daic2:+.2f}  [H46C: 66.46 / +35.78]")
    log(f"  overshoot: A_GU = {A_gu_A:.4f} vs BAO-preferred A* = {Astar:.4f} "
        f"(sigma_A = {sigA:.4f}) -> {gap:+.2f} sigma_A  [H46C: +5.7]")
    check("E", "the calibrated amplitude OVERSHOOTS the BAO-preferred amplitude "
               "for GU's own shape by > 3 sigma_A (recomputed)", gap > 3.0,
          f"{gap:+.2f} sigma_A")
    check("E", "own-calibration likelihood adjudication: dAIC(GU - LCDM) > +25, "
               "decisively disfavored (H46C +35.78 reproduced within implementation "
               "tolerance)", daic2 > 25.0, f"{daic2:+.2f}")

    # per-f0 calibration scan: the honest amplitude statement
    log("\n  per-f0 CMB calibration scan (each f0 pays its own calibration):")
    scan = []
    for f0 in (0.01, 0.02, 0.05, 0.125, 0.25):
        h_r = calibrate(f0, treatment="A", npts=600, n_iter=40)
        h_c = h_r * (H_PLANCK / hL_A)
        A_c = C_KMS / (100.0 * h_c) / RD
        bgf = solve_bg(M2_BC1, f0, OMH2 / h_c ** 2, npts=600, n_iter=40)
        i4 = np.argsort(bgf["z"])
        c2 = chi2_of(bao_vector(bgf["z"][i4], np.sqrt(bgf["H2"][i4]), A_c))
        scan.append((f0, h_c, A_c, c2))
        log(f"    f0={f0:5.3f}: h_cal={h_c:.5f}  A_cal={A_c:.4f}  chi2={c2:8.3f}"
            f"  (dchi2 vs LCDM {c2-chi2_l:+8.3f})")
    c2s = [r[3] for r in scan]
    monotone = all(c2s[i] < c2s[i + 1] for i in range(len(c2s) - 1))
    d_scan = np.array(c2s) - chi2_l
    f0s_scan = np.array([r[0] for r in scan])
    f0_9 = float(np.exp(np.interp(9.0, d_scan, np.log(f0s_scan))))
    log(f"  dchi2 = 9 crossing (3-sigma-equivalent): f0 ~ {f0_9:.3f}  [H46C ~0.027]")
    check("E", "chi2(f0) monotone increasing over the scan: BAO + theta* prefers "
               "the LCDM limit f0 -> 0; the theta amplitude is an UPPER LIMIT, "
               "not a detection", monotone)
    check("E", "3-sigma-equivalent bound recomputed: f0_9 in [0.015, 0.05] "
               "(canonical M^2 = 8; the one-sided split bound COSMO-A1 quotes)",
          0.015 < f0_9 < 0.05, f"{f0_9:.3f}")

    # band scope (M^2 = 3, 7, 8): direction uniform; exclusion strength ordered
    log("\n  M^2-band calibration (the closure audit's named cheap hardening):")
    band = {}
    for M2 in M2_BAND:
        h_r = calibrate(F0_CANON, treatment="A", M2=M2, npts=600, n_iter=40)
        h_c = h_r * (H_PLANCK / hL_A)
        A_c = C_KMS / (100.0 * h_c) / RD
        bgb = solve_bg(M2, F0_CANON, OMH2 / h_c ** 2, npts=600, n_iter=40)
        ib = np.argsort(bgb["z"])
        c2 = chi2_of(bao_vector(bgb["z"][ib], np.sqrt(bgb["H2"][ib]), A_c))
        band[M2] = (h_c, A_c, c2 - chi2_l)
        log(f"    M^2={M2:4.1f}: h_cal={h_c:.5f}  A_cal={A_c:.4f}  "
            f"dchi2 vs LCDM = {c2-chi2_l:+8.3f}")
    check("E", "band direction uniform: at every admissible M^2 in {3, 7, 8} the "
               "calibrated h sits BELOW the LCDM calibration (the overshoot "
               "mechanism is band-generic, as H46C argued but did not scan)",
          all(band[m][0] < H_PLANCK for m in M2_BAND),
          "h_cal = " + ", ".join(f"{band[m][0]:.4f}" for m in M2_BAND))
    check("E", "band exclusion ordered and W129-consistent: dchi2(M2=3) < "
               "dchi2(M2=7) < dchi2(M2=8); M2=3 mild (< 14, the DE-06 honest "
               "softening), M2=8 decisive (> 25)",
          band[3.0][2] < band[7.0][2] < band[8.0][2]
          and band[3.0][2] < 14.0 and band[8.0][2] > 25.0,
          f"dchi2 = {band[3.0][2]:+.1f}/{band[7.0][2]:+.1f}/{band[8.0][2]:+.1f}")

    # ratio-only / scale-free structure (H24, PRED-NORM-RANK), computationally
    log("\n--- [E] ratio-only structure (H24 / PRED-NORM-RANK), exhibited ---")
    bgx = solve_bg(M2_BC1, 0.05, 0.315, npts=700, B0=1.0)
    bgy = solve_bg(M2_BC1, 0.05, 0.315, npts=700, B0=7.3)
    wdiff = float(np.max(np.abs(w_de(bgx) - w_de(bgy))))
    check("E", "KG linearity: rescaling the absolute field amplitude B0 leaves "
               "w_DE(z) identical -- the absolute mode amplitude is UNOBSERVABLE "
               "in the shape; only the dimensionless ratio f0 enters (ratio-only, "
               "H24)", wdiff < 1e-10, f"max|dw| = {wdiff:.1e}")
    h00 = calibrate(1e-8, treatment="A") * (H_PLANCK / hL_A)
    A00 = C_KMS / (100.0 * h00) / RD
    check("E", "f0 -> 0: the calibrated amplitude reduces EXACTLY to the imported "
               "Planck point (A -> 30.26): every GU-native contribution to the "
               "amplitude is the dimensionless calibration ratio; GU supplies NO "
               "absolute scale (PRED-NORM-RANK consistency)",
          abs(A00 / A_PLANCK - 1) < 1e-3, f"A(f0->0) = {A00:.4f} vs {A_PLANCK:.4f}")

    # freeze every calibration output BEFORE any confrontation constant appears
    AUDIT_OUT = dict(h_gu=hG_A, A_gu=A_gu_A, Om_gu=Om_gu, daic2=daic2, gap=gap,
                     f0_bound=f0_9, band=dict(band), tail_shift=tail_shift)

    # -------------------------------------------------------------------------
    # [F] confrontation checks (data-facing; flagged).
    # -------------------------------------------------------------------------
    log("\n--- [F] confrontation (flagged; brackets consumed NOWHERE upstream) ---")

    # F1: executed blindness -- perturbing the DESI vector cannot move the
    # calibration (the calibration never sees it).
    h_before = calibrate(0.05, treatment="A", npts=600, n_iter=40)
    saved = DESI_MEAN.copy()
    DESI_MEAN = DESI_MEAN * 1.10
    h_after = calibrate(0.05, treatment="A", npts=600, n_iter=40)
    DESI_MEAN = saved
    check("F", "NO CALIBRATION LEAKAGE, executed: perturbing the DESI data vector "
               "by 10% changes the calibrated h by exactly zero -- the BAO data "
               "enter ONLY the confrontation, never the calibration",
          h_before == h_after, f"|dh| = {abs(h_before-h_after):.1e}")

    # F2: COSMO-A1 bracket confrontation. CONFRONTATION ONLY -- the meV number
    # is defined HERE, after AUDIT_OUT froze, and is never an input upstream.
    MEV_BRACKET = 2.24          # COSMO-A1: rho_DE^(1/4) ~ 2.24 meV, two-sided <10%
    MPC_KM = 3.0856775814913673e19
    HBAR_EV_S = 6.582119569e-16
    MPL_RED_EV = 2.435e27
    MPL_FULL_EV = 1.220890e28

    def rho14_mev(h100, om):
        H0_ev = (h100 * 100.0 / MPC_KM) * HBAR_EV_S
        return (3.0 * (1.0 - om)) ** 0.25 * np.sqrt(H0_ev * MPL_RED_EV) * 1e3

    r14_planck = rho14_mev(H_PLANCK, 0.3153)
    r14_gu = rho14_mev(AUDIT_OUT["h_gu"], AUDIT_OUT["Om_gu"])
    ratio123 = (r14_planck * 1e-3) ** 4 / MPL_FULL_EV ** 4
    log(f"  rho_DE^(1/4): Planck point {r14_planck:.3f} meV; GU own calibration "
        f"{r14_gu:.3f} meV; bracket {MEV_BRACKET} meV (two-sided < 10%)")
    log(f"  rho_DE / M_Pl^4 = {ratio123:.2e}  (the 1e-123 number, recomputed)")
    check("F", "COSMO-A1 confrontation: the Planck-point total reproduces the "
               "bracket to < 3% and GU's OWN calibrated total sits INSIDE the "
               "two-sided 10% bracket (the ~5% calibration shift is invisible at "
               "bracket resolution -- the bracket does NOT discriminate; the "
               "likelihood row 2 above does)",
          abs(r14_planck / MEV_BRACKET - 1) < 0.03
          and abs(r14_gu / MEV_BRACKET - 1) < 0.10,
          f"{r14_planck:.3f} / {r14_gu:.3f} meV")

    # F3: the spec's kill condition, adjudicated.
    check("F", "KILL CONDITION (portfolio spec): the corrected canonical amplitude "
               "REMAINS strongly disfavored (dAIC > +10 at M^2 = 8 canonical; "
               "band-scoped per DE-06) -> the positive raw-BAO amplitude leg stays "
               "CLOSED; the full-tail correction moved the amplitude by < 0.2% "
               "(reported as a shift, NOT called a prediction)",
          AUDIT_OUT["daic2"] > 10.0 and AUDIT_OUT["tail_shift"] < 2e-3,
          f"dAIC = {AUDIT_OUT['daic2']:+.2f}, tail shift {AUDIT_OUT['tail_shift']:.1e}")

    # F4: the PP1 first-live-read flag (CH-COSMO section 3 ledger note).
    no_pref = (c2s[0] - chi2_l) > -2.0
    check("F", "PP1 first live read: no detected deviation (chi2 minimized at the "
               "f0 -> 0 edge, one-sided bound only; no admissible preference for "
               "f0 > 0) -> the DE background is ORIENTATION-SILENT; PP1 stays "
               "UNTRIGGERED and no sign-consistency datum is available",
          monotone and no_pref,
          f"dchi2(f0=0.01) = {c2s[0]-chi2_l:+.2f}")

    # -------------------------------------------------------------------------
    # verdict + headline.
    # -------------------------------------------------------------------------
    log("\n" + "-" * 78)
    log("AUDIT VERDICT (diagnostic; not a prediction)")
    log("-" * 78)
    log(f"  GU fixes NO absolute dark-energy amplitude (ratio-only, E10/E11).")
    log(f"  GU's own full-D_M theta_star calibration: A_GU = {AUDIT_OUT['A_gu']:.4f} "
        f"(+{(AUDIT_OUT['A_gu']/A_PLANCK-1)*100:.2f}% vs Planck), tail-robust.")
    log(f"  Blind H46B-likelihood adjudication: dAIC = {AUDIT_OUT['daic2']:+.2f} "
        f"(canonical f0, M^2 = 8); overshoot {AUDIT_OUT['gap']:+.2f} sigma_A.")
    log(f"  Surviving object: one-sided split bound f0 <~ {AUDIT_OUT['f0_bound']:.3f} "
        f"(M^2 = 8; band softens to ~0.21 at M^2 = 3 per DE-06/W129).")
    log(f"  Positive raw-BAO amplitude leg: CLOSED (kill condition met).")
    log(f"  PP1: untriggered (orientation-silent).")

    nE = sum(1 for t, _n, _o in RESULTS if t == "E")
    nF = sum(1 for t, _n, _o in RESULTS if t == "F")
    nT = sum(1 for t, _n, _o in RESULTS if t == "T")
    all_ok = all(o for _t, _n, o in RESULTS)
    nfail = sum(1 for _t, _n, o in RESULTS if not o)
    log("")
    log(f"HEADLINE: {nE} [E] + {nF} [F] = {nE + nF}   (setup [T] = {nT} excluded)   "
        f"{'ALL PASS' if all_ok else f'{nfail} FAILURES'}")
    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()
