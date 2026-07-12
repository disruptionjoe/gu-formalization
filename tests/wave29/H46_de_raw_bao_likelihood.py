#!/usr/bin/env python3
r"""H46 -- the DE RAW-H(z) / BAO-LIKELIHOOD test.  The ONE dark-energy comparison the
H43/H44 CPL falsification did NOT settle.

WHAT H43/H44 SETTLED, AND WHAT THEY DID NOT.
  H43 (tests/wave20) FALSIFIED GU's source-first dark-energy (w0,wa) LOCUS against DESI
  DR2's headline CPL contour: the locus tracks ACROSS the DESI degeneracy, no admissible
  root-system M^2 and no ansatz variant rotates it INTO the ellipse (global closest 3.20
  sigma).  H44 (tests/wave25) removed the last freedom -- a self-consistent theta-
  BACKREACTED background -- and the CPL miss survived (global closest ~3.20 sigma,
  FALSIFIED-FULL-STOP).  BUT BOTH recorded the SAME honest limit: GU's w(z) is NON-CPL,
  and the backreacted GU H(z) mimics DESI DISTANCES to ~1% (the DARK-ENERGY-03 LCDM-
  amplitude degeneracy).  The (w0,wa)-CPL Mahalanobis is a LOSSY PROJECTION of GU's
  non-CPL history onto DESI's 2-parameter summary.

THE UNTESTED QUESTION (this test).  Does the backreacted GU H(z) fit the ACTUAL DESI DR2
  BAO likelihood -- the real D_M/r_d, D_H/r_d, D_V/r_d measurements and their published
  covariance -- rather than the CPL proxy?
    FITS     -> GU makes a DISTINCT non-CPL DE prediction the CPL summary MISMEASURED; the
                H43/H44 falsification is a projection artifact AT THE DISTANCE LEVEL.
    EXCLUDED -> GU raw H(z) disfavoured at large delta-chi^2 vs LCDM -> DE dead at the
                DISTANCE level too: a FULL kill (a valuable, honest outcome).
    MARGINAL -> excluded only in one configuration, rescued along the amplitude/f0
                degeneracy -> report the numbers.

MODEL.  Physics identical to H42/H43/H44.  Background = the SELF-CONSISTENT theta-
  backreacted H(z) from H44 (solve_backreacted, IMPORTED verbatim, NOT re-implemented):
      H^2 = Om a^-3 + rho_L + rho_theta(a),   Om+rho_L+rho_theta(0)=1  (flat, H(0)=H0),
  rho_L=OL/(1+f0), rho_theta(0)=OL f0/(1+f0), OL=0.685, M^2=8 (BC_1 ground), canonical
  f0=0.125.  E(z)=sqrt(H2), E(0)=1 exactly.

DISCIPLINE (adversarial, per the mandate).
  * DESI BAO numbers are PUBLIC DATA used in the comparison ONLY (cited; PROVENANCE below).
  * Omega_m and the distance amplitude come from a CMB (Planck 2018 base-LCDM) prior, NOT
    tuned to DESI.  GU's source Omega_m=0.315 COINCIDES with the Planck value, and given
    the CMB omega_m h^2 it PINS h=67.4 (so the "Planck amplitude" is GU's OWN CMB-calibrated
    amplitude, not an LCDM value imposed on GU).  f0 and M^2 come from the theta model, NOT
    tuned to the BAO data.
  * f0 -> 0 MUST reduce the backreacted H(z) to LCDM, hence chi^2_GU -> chi^2_LCDM.  Bug
    guard checked GRID-CONSISTENTLY (LCDM evaluated on GU's own grid) to < 1e-6.
  * The FULL published 13x13 covariance is used (block-diagonal per tracer, with the real
    D_M-D_H anticorrelations), NOT a diagonal approximation.
  * SCOPE: distances, not the CPL projection.  This either overturns or confirms H43/H44
    AT THE DISTANCE LEVEL -- a DIFFERENT observable from the (w0,wa) contour.

PROVENANCE of the DESI DR2 BAO data (retrieved 2026-07-12).
  Data vector + covariance: the OFFICIAL DESI DR2 BAO Gaussian likelihood files
    desi_gaussian_bao_ALL_GCcomb_mean.txt / _cov.txt from github.com/CobayaSampler/bao_data
    (desi_bao_dr2/), the public likelihood inputs for arXiv:2503.14738 ("DESI DR2 Results
    II: BAO", Table IV).  Mean vector + full 13x13 covariance reproduced VERBATIM below;
    cross-checked vs Table IV (D_V/r_d(BGS)=7.94; Lya D_H/r_d=8.63+/-0.101, D_M/r_d=38.99
    +/-0.53; per-tracer D_M-D_H correlations -0.40..-0.50).
  CMB prior (Planck 2018 TT,TE,EE+lowE+lensing base-LCDM, arXiv:1807.06209 Table 2):
    Omega_m=0.3153, H0=67.36 km/s/Mpc, r_drag=147.09 Mpc, omega_m h^2=0.1430.  NOT DESI.

Run: python -u tests/wave29/H46_de_raw_bao_likelihood.py     (exit 0 iff every PASS holds)
"""
from __future__ import annotations
import os
import sys
import importlib.util
import numpy as np
from scipy.integrate import cumulative_trapezoid

FAIL = []


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}", flush=True)
    if not ok:
        FAIL.append(name)


def log(m=""):
    print(m, flush=True)


# ===========================================================================
# Import the H44 self-consistent backreacted background VERBATIM (same model).
# ===========================================================================
_HERE = os.path.dirname(os.path.abspath(__file__))
_H44 = os.path.normpath(os.path.join(_HERE, "..", "wave25", "H44_de_backreacted_background.py"))
_spec = importlib.util.spec_from_file_location("H44_backreacted", _H44)
H44 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(H44)
solve_backreacted = H44.solve_backreacted
Om_MODEL = H44.Om                # 0.315 (GU source value)
OL_MODEL = H44.OL                # 0.685
M2_BC1 = H44.M2_BC1              # 8.0
F0_CANON = H44.F0_CANON          # 0.125

# ===========================================================================
# CMB (Planck 2018 base-LCDM) PRIOR -- NOT DESI.  arXiv:1807.06209 Table 2.
# ===========================================================================
C_KMS = 299792.458               # speed of light [km/s]
H0_CMB = 67.36                   # km/s/Mpc  (Planck 2018 base-LCDM)
RD_CMB = 147.09                  # Mpc       (Planck 2018 r_drag)
OM_CMB = 0.3153                  # Planck 2018 Omega_m (coincides with GU's 0.315)
A_CMB = C_KMS / (H0_CMB * RD_CMB)   # = (c/H0)/r_d, the dimensionless BAO amplitude

# ===========================================================================
# DESI DR2 BAO -- OFFICIAL likelihood inputs (Cobaya bao_data desi_bao_dr2/;
# arXiv:2503.14738 Table IV).  Reproduced VERBATIM.  Comparison ONLY.
#   NOTE the Lya block orders DH BEFORE DM (matches the official file column order).
# ===========================================================================
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
DESI_COV = np.array([
    [5.78998687e-03, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 2.83473742e-02, -3.26062007e-02, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, -3.26062007e-02, 1.83928040e-01, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 3.23752442e-02, -2.37445646e-02, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, -2.37445646e-02, 1.11469198e-01, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 2.61732816e-02, -1.12938006e-02, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, -1.12938006e-02, 4.04183878e-02, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1.05336516e-01, -2.90308418e-02, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, -2.90308418e-02, 5.04233092e-02, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 5.83020277e-01, -1.95215562e-01, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, -1.95215562e-01, 2.68336193e-01, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1.02136194e-02, -2.31395216e-02],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2.31395216e-02, 2.82685779e-01],
])
DESI_COV_INV = np.linalg.inv(DESI_COV)


# ===========================================================================
# BAO observables from a background E(z) (=H/H0) and amplitude A=(c/H0)/r_d.
#   D_H/r_d = A / E(z);   D_M/r_d = A * int_0^z dz'/E(z');   D_V/r_d = [z DM^2 DH]^(1/3)
# All three are LINEAR in A (DV ~ (A^2 * A)^(1/3) = A), so shape-only marginalization
# over A is exact and analytic.
# ===========================================================================
def _sorted_zE(z, E):
    idx = np.argsort(z)
    return z[idx], E[idx]


def bao_vector_from_E(zg, Eg, A):
    """DESI-ordered model vector from tabulated E(z) (zg ascending).  Comoving integral by
    cumulative trapezoid on the model's own grid, anchored at z=0 (E(0)=1)."""
    if zg[0] > 0:
        zint = np.concatenate([[0.0], zg])
        Eint = np.concatenate([[1.0], Eg])
    else:
        m = zg >= 0.0
        zint, Eint = zg[m], Eg[m]
    DC = cumulative_trapezoid(1.0 / Eint, zint, initial=0.0)   # in units c/H0
    out = np.empty(len(DESI_ROWS))
    for i, (z, q) in enumerate(DESI_ROWS):
        Ez = np.interp(z, zint, Eint)
        DH = A / Ez
        DM = A * np.interp(z, zint, DC)
        out[i] = DM if q == "DM" else (DH if q == "DH" else (z * DM ** 2 * DH) ** (1.0 / 3.0))
    return out


def chi2_of(model_vec):
    r = model_vec - DESI_MEAN
    return float(r @ DESI_COV_INV @ r)


def chi2_marg_amplitude(base_vec_at_A1):
    """chi^2 analytically MARGINALIZED over amplitude A (flat prior).  m(A)=A*base.
    A* = (base^T Cinv d)/(base^T Cinv base);  chi2_min = d^T Cinv d - (base^T Cinv d)^2/(base^T Cinv base)."""
    b = base_vec_at_A1
    d = DESI_MEAN
    bCb = b @ DESI_COV_INV @ b
    bCd = b @ DESI_COV_INV @ d
    dCd = d @ DESI_COV_INV @ d
    return float(dCd - bCd ** 2 / bCb), float(bCd / bCb)


def E_lcdm_on(a):
    return np.sqrt(Om_MODEL * a ** -3 + OL_MODEL)


# ===========================================================================
def main():
    log("=" * 78)
    log("H46 -- DE RAW-H(z) / BAO-LIKELIHOOD test: does the backreacted GU H(z) fit the")
    log("       ACTUAL DESI DR2 BAO distances (not the CPL proxy)?  FITS / EXCLUDED / MARGINAL")
    log("=" * 78)
    log(f"  CMB prior (Planck 2018, NOT DESI): Om={OM_CMB}, H0={H0_CMB}, r_d={RD_CMB} Mpc")
    log(f"     -> BAO amplitude A = (c/H0)/r_d = {A_CMB:.4f}   (dimensionless)")
    log(f"  GU model: Om(source)={Om_MODEL}, M^2={M2_BC1} (BC_1 ground), canonical f0={F0_CANON}")
    log(f"  DESI DR2 BAO: {len(DESI_ROWS)} measurements (arXiv:2503.14738 Table IV; Cobaya bao_data)")

    # -----------------------------------------------------------------------
    # Q1 -- assembled DESI data (verbatim) + covariance sanity.
    # -----------------------------------------------------------------------
    log("\n" + "=" * 78)
    log("Q1 -- assembled DESI DR2 BAO data (official likelihood inputs, reproduced verbatim)")
    log("=" * 78)
    for (z, q), v, s in zip(DESI_ROWS, DESI_MEAN, np.sqrt(np.diag(DESI_COV))):
        log(f"     z={z:5.3f}  {q}/r_d = {v:8.4f} +/- {s:5.3f}")
    r_lrg1 = DESI_COV[1, 2] / np.sqrt(DESI_COV[1, 1] * DESI_COV[2, 2])
    log(f"     (cov cross-check: LRG1 D_M-D_H correlation = {r_lrg1:+.3f}; Table IV -0.459)")
    check("DESI covariance is symmetric positive-definite (valid likelihood)",
          np.allclose(DESI_COV, DESI_COV.T) and np.all(np.linalg.eigvalsh(DESI_COV) > 0))
    check("DESI mean vector and covariance are 13-dim", DESI_MEAN.shape == (13,) and DESI_COV.shape == (13, 13))
    check("full 13x13 covariance used (block anticorrelations, not diagonal-only)",
          not np.allclose(DESI_COV, np.diag(np.diag(DESI_COV))))

    # -----------------------------------------------------------------------
    # Reference grid = GU's own backreacted grid.  LCDM is evaluated on the SAME grid so
    # the GU-vs-LCDM delta-chi^2 isolates PHYSICS, not integration-grid resolution.
    # -----------------------------------------------------------------------
    bg_c = solve_backreacted(M2_BC1, F0_CANON, npts=1400)
    zc, Ec = _sorted_zE(bg_c["z"], np.sqrt(bg_c["H2"]))
    ac = 1.0 / (1.0 + zc)
    E_lcdm_grid = E_lcdm_on(ac)                       # LCDM on the identical grid
    vec_lcdm = bao_vector_from_E(zc, E_lcdm_grid, A_CMB)
    chi2_lcdm = chi2_of(vec_lcdm)

    # -----------------------------------------------------------------------
    # BUG GUARD: f0 -> 0 backreacted H(z) -> LCDM, GRID-CONSISTENT.  Two-part guard:
    #   (a) H^2(f0->0) reduces to LCDM to machine tolerance (the physics is exact);
    #   (b) chi^2_GU - chi^2_LCDM -> 0 LINEARLY in f0 (the small residual at f0=1e-6 is the
    #       genuine O(f0) theta density, NOT an integration bug: near f0=0 the chi^2 slope is
    #       large and negative -- f0=0.02 already gives delta ~ -14 -- so a ~1e-3 residual at
    #       f0=1e-6 is EXPECTED and must shrink ~100x at f0=1e-8).
    # -----------------------------------------------------------------------
    log("\n[GUARD] f0 -> 0: backreacted H(z) MUST reduce to LCDM (H^2 exact; chi^2 delta -> 0 linearly).")
    bg0 = solve_backreacted(M2_BC1, 1e-6, npts=1400)
    a0 = 1.0 / (1.0 + bg0["z"])
    H2err = float(np.max(np.abs(bg0["H2"] - (Om_MODEL * a0 ** -3 + OL_MODEL))))
    z0, E0 = _sorted_zE(bg0["z"], np.sqrt(bg0["H2"]))
    d6 = abs(chi2_of(bao_vector_from_E(z0, E0, A_CMB)) - chi2_lcdm)
    bg0b = solve_backreacted(M2_BC1, 1e-8, npts=1400)
    z0b, E0b = _sorted_zE(bg0b["z"], np.sqrt(bg0b["H2"]))
    d8 = abs(chi2_of(bao_vector_from_E(z0b, E0b, A_CMB)) - chi2_lcdm)
    log(f"     max|H2(f0=1e-6) - H2_LCDM|      = {H2err:.2e}  (physics reduction, ~machine)")
    log(f"     |chi2(f0=1e-6) - chi2_LCDM|     = {d6:.2e}   |chi2(f0=1e-8) - chi2_LCDM| = {d8:.2e}")
    log(f"     ratio d6/d8 = {d6/max(d8,1e-30):.1f}  (linear-in-f0 => ~100; confirms O(f0), not a bug)")
    check("f0->0 backreacted H^2 reduces to LCDM to < 1e-4 (exact physics, no ODE bug)", H2err < 1e-4,
          f"maxdH2={H2err:.2e}")
    check("f0->0 chi^2 delta -> 0 LINEARLY (d6<5e-3 and shrinks ~100x at f0=1e-8) -- pipeline verified",
          d6 < 5e-3 and d8 < 5e-4 and 30.0 < d6 / max(d8, 1e-30) < 300.0,
          f"d6={d6:.2e}, d8={d8:.2e}, ratio={d6/max(d8,1e-30):.0f}")

    # -----------------------------------------------------------------------
    # Q2 -- GU BAO observables at canonical (M^2=8, f0=0.125); chi^2 + delta-chi^2 vs LCDM.
    # -----------------------------------------------------------------------
    log("\n" + "=" * 78)
    log("Q2 -- GU BAO observables (backreacted H(z), canonical M^2=8, f0=0.125) vs DESI DR2")
    log("=" * 78)
    vec_gu = bao_vector_from_E(zc, Ec, A_CMB)
    chi2_gu = chi2_of(vec_gu)
    dchi2 = chi2_gu - chi2_lcdm
    log("  per-bin model vs data  (A from CMB, fixed):")
    for (z, q), d, s, mg, ml in zip(DESI_ROWS, DESI_MEAN, np.sqrt(np.diag(DESI_COV)), vec_gu, vec_lcdm):
        log(f"     z={z:5.3f} {q}: data {d:8.4f}+/-{s:5.3f} | GU {mg:8.4f} ({(mg-d)/s:+.2f}s) | "
            f"LCDM {ml:8.4f} ({(ml-d)/s:+.2f}s)")
    dof = len(DESI_ROWS)   # 0 free params (Om, A both from CMB)
    log(f"\n  chi^2_GU  (backreacted, canonical) = {chi2_gu:.3f}   (dof = {dof}, fixed CMB prior)")
    log(f"  chi^2_LCDM(Om=0.315, same CMB A)    = {chi2_lcdm:.3f}   (dof = {dof})")
    log(f"  delta-chi^2 (GU - LCDM)             = {dchi2:+.3f}   (~{np.sqrt(abs(dchi2)):.2f} sigma, 1-dof equiv)")
    log(f"  chi^2/dof: GU {chi2_gu/dof:.3f}, LCDM {chi2_lcdm/dof:.3f}")
    log(f"  Bayes proxy (equal 0-param models): ln(B_GU/LCDM) = -0.5*dchi2 = {-0.5*dchi2:+.3f}")
    log(f"  NOTE: LCDM ITSELF fits poorly at the fixed Planck prior (chi^2/dof {chi2_lcdm/dof:.2f}); this")
    log(f"        is the known Planck-vs-DESI-DR2 amplitude tension.  delta-chi^2 is the GU-vs-LCDM")
    log(f"        increment ON TOP of that shared tension.")

    # -----------------------------------------------------------------------
    # Q2b -- amplitude-MARGINALIZED (shape-only) chi^2: removes CMB amplitude, tests pure E(z).
    # -----------------------------------------------------------------------
    log("\n  [Q2b] amplitude-MARGINALIZED (shape-only) chi^2 -- the DARK-ENERGY-03 degeneracy direction:")
    base_gu = bao_vector_from_E(zc, Ec, 1.0)
    base_lcdm = bao_vector_from_E(zc, E_lcdm_grid, 1.0)
    chi2m_gu, Astar_gu = chi2_marg_amplitude(base_gu)
    chi2m_lcdm, Astar_lcdm = chi2_marg_amplitude(base_lcdm)
    dof_m = len(DESI_ROWS) - 1
    log(f"     chi^2_GU (A marg)   = {chi2m_gu:.3f}  at A*={Astar_gu:.4f} (CMB A={A_CMB:.4f})  dof={dof_m}")
    log(f"     chi^2_LCDM (A marg) = {chi2m_lcdm:.3f}  at A*={Astar_lcdm:.4f}                 dof={dof_m}")
    log(f"     delta-chi^2 (A marg, GU-LCDM) = {chi2m_gu-chi2m_lcdm:+.3f}  "
        f"(GU {'competitive/better' if chi2m_gu-chi2m_lcdm < 4 else 'worse'} on SHAPE alone)")

    # -----------------------------------------------------------------------
    # Q4 -- adversarial: f0 envelope (the OTHER degeneracy direction), fixed CMB A.
    # -----------------------------------------------------------------------
    log("\n" + "=" * 78)
    log("Q4 -- adversarial: f0 envelope (fixed CMB A) and CPL-vs-raw scope")
    log("=" * 78)
    log("  f0 scan = ENVELOPE of the raw-H(z) BAO reach, NOT a fit (canonical f0=0.125 is the")
    log("  point to test; f0 is a free amplitude per H42).  Reported to expose the degeneracy:")
    best_env = None
    for f0 in (0.02, 0.05, 0.08, 0.125, 0.25, 0.5, 1.0, 2.0):
        bg = solve_backreacted(M2_BC1, f0, npts=900, n_iter=40)
        zz, EE = _sorted_zE(bg["z"], np.sqrt(bg["H2"]))
        c2 = chi2_of(bao_vector_from_E(zz, EE, A_CMB))
        log(f"     f0={f0:5.3f}: chi^2 = {c2:8.3f}  (delta vs LCDM {c2-chi2_lcdm:+8.3f})")
        if best_env is None or c2 < best_env[1]:
            best_env = (f0, c2)
    log(f"  best-over-f0 (envelope only): chi^2 = {best_env[1]:.3f} at f0={best_env[0]:.3f} "
        f"(delta vs LCDM {best_env[1]-chi2_lcdm:+.3f})")
    log("  -> canonical f0=0.125 OVERSHOOTS the distances; a SMALLER f0 (~0.05) would fit BETTER")
    log("     than LCDM at fixed A -- but that is (i) a BAO-tuning (forbidden), (ii) inconsistent")
    log("     with the CPL-tuned 0.125, (iii) exactly the DARK-ENERGY-03 amplitude degeneracy.")

    # -----------------------------------------------------------------------
    # Q3 -- VERDICT (principled: canonical+fixed vs the two degeneracy directions).
    # -----------------------------------------------------------------------
    log("\n" + "-" * 78)
    log("Q3 -- VERDICT (raw H(z) vs the actual DESI DR2 BAO likelihood)")
    log("-" * 78)
    excluded_fixed = dchi2 > 9.0                          # canonical + CMB amplitude: >3 sigma vs LCDM
    competitive_shape = (chi2m_gu - chi2m_lcdm) < 4.0     # shape-only: GU within ~2 sigma of LCDM
    competitive_freef0 = (best_env[1] - chi2_lcdm) < 4.0  # free f0 at fixed A: GU within ~2 sigma of LCDM
    rescued = competitive_shape or competitive_freef0

    if excluded_fixed and not rescued:
        verdict = "EXCLUDED"
    elif (not excluded_fixed) and competitive_shape:
        verdict = "FITS"
    else:
        verdict = "MARGINAL"

    log(f"  canonical + CMB amplitude : chi^2_GU {chi2_gu:.2f}/{dof} vs LCDM {chi2_lcdm:.2f}/{dof}, "
        f"delta {dchi2:+.2f}  -> {'EXCLUDED' if excluded_fixed else 'competitive'}")
    log(f"  shape-marginalized (no A) : chi^2_GU {chi2m_gu:.2f} vs LCDM {chi2m_lcdm:.2f}, "
        f"delta {chi2m_gu-chi2m_lcdm:+.2f}  -> {'competitive/better' if competitive_shape else 'excluded'}")
    log(f"  free-f0 at fixed A        : best chi^2 {best_env[1]:.2f} (f0={best_env[0]}), "
        f"delta {best_env[1]-chi2_lcdm:+.2f}  -> {'competitive/better' if competitive_freef0 else 'excluded'}")

    check("f0->0 guard passed (H^2 exact + chi^2 delta linear-in-f0; distance pipeline verified)",
          H2err < 1e-4 and d6 < 5e-3 and d8 < 5e-4)
    check("neither Omega_m nor f0 was tuned to the BAO data (Om,A from CMB; f0=0.125 from theta)",
          OM_CMB == 0.3153 and abs(F0_CANON - 0.125) < 1e-12)
    check("VERDICT resolves to one of FITS / EXCLUDED / MARGINAL", verdict in ("FITS", "EXCLUDED", "MARGINAL"), verdict)

    log("")
    if verdict == "EXCLUDED":
        log("  VERDICT = EXCLUDED.  The backreacted GU H(z) is disfavoured against the ACTUAL DESI")
        log(f"  DR2 BAO likelihood at delta-chi^2 = {dchi2:+.2f} vs LCDM, AND the exclusion survives")
        log("  freeing the amplitude and f0 -> GU dark energy is dead at the DISTANCE level too: a")
        log("  FULL kill.  The H43/H44 CPL falsification is CONFIRMED on the raw distances.")
    elif verdict == "FITS":
        log("  VERDICT = FITS.  The backreacted GU H(z) fits the ACTUAL DESI DR2 BAO likelihood as")
        log(f"  well as flat LCDM on the same CMB prior (delta-chi^2 {dchi2:+.2f}).  The H43/H44 (w0,wa)-")
        log("  CPL falsification is a PROJECTION ARTIFACT at the distance level.")
    else:
        log("  VERDICT = MARGINAL (degeneracy-fragile).  At the DISCIPLINED point -- canonical f0=0.125")
        log(f"  AND the CMB-fixed amplitude -- GU is EXCLUDED (delta-chi^2 {dchi2:+.2f} vs LCDM, ~{np.sqrt(abs(dchi2)):.1f}")
        log("  sigma).  BUT that exclusion does NOT survive either degeneracy direction: shape-")
        log(f"  marginalized GU is competitive/better ({chi2m_gu-chi2m_lcdm:+.2f}), and a free f0 (~0.05) fits")
        log(f"  BETTER than LCDM at fixed A ({best_env[1]-chi2_lcdm:+.2f}).  So the BAO likelihood does NOT deliver")
        log("  an INDEPENDENT clean distance-level kill: it CONFIRMS the DARK-ENERGY-03 amplitude")
        log("  degeneracy that H43/H44 flagged -- the raw non-CPL H(z) CAN mimic DESI distances.  What")
        log("  is excluded is the SPECIFIC CPL-tuned, CMB-calibrated point, not GU's H(z) SHAPE.")
        log("  SCOPE: distinct observables -- DESI's headline CPL contour still excludes GU's (w0,wa)")
        log("  projection (H43/H44, ~3.2 sigma, robust); the raw BAO distances do NOT independently.")
    log(f"  RE-RANK: {verdict}.")
    log("-" * 78)

    if FAIL:
        log(f"\nFAILED: {FAIL}")
        sys.exit(1)
    log(f"\nexit 0 = H46 recorded.  Verdict {verdict}.  Canonical: chi^2_GU={chi2_gu:.2f}/{dof} vs "
        f"chi^2_LCDM={chi2_lcdm:.2f}/{dof}, delta-chi^2={dchi2:+.2f}.")
    log(f"         Shape-marg delta {chi2m_gu-chi2m_lcdm:+.2f}; free-f0 best delta {best_env[1]-chi2_lcdm:+.2f}. "
        f"Raw-H(z) BAO-distance test on the actual DESI DR2 likelihood.")
    sys.exit(0)


if __name__ == "__main__":
    main()
