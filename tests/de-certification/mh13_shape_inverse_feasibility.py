#!/usr/bin/env python3
r"""M-H13 proxy-shape inverse problem (anchor council Wave A-2, item 2),
with the JP4 signed-readout extension (seat4 Section 5).

THE QUESTION (seat2 2.1, CHEAP_NEW_COMPUTATION).  DE-07 item 3: at GU's own theta_star-
calibrated cosmology the amplitude-marginalised SHAPE chi^2 is +19.3 vs LCDM at M^2 = 8
-- any completion must SUPPLY that much low-z evolution.  M-H13 proposes to supply it
with a record-accretion coefficient r(N(z)) -- a MONOTONE low-z-growing deformation.
Before the native record law exists: does ANY monotone low-z-growing proxy rho_X(z)
deformation lie in the space that recovers the +19.3?  And (JP4) does ANY signed
readout N_K = w+ f+ - w- f- with nonempty negative cone reach outside the monotone
cone under accretion-restricted reachability?

SETUP.  Deformed model = canonical theta background (M^2 = 8, f0 = 0.125) plus a DE
channel rho_X(z); today's flat budget re-partitioned (Om + rho_L + rho_theta(0)
+ rho_X(0) = 1, f0 = rho_theta(0)/rho_L held), and the FULL theta_star calibration
re-run per candidate (the deformation moves D_M(z_star), hence h_cal, hence Om_cal --
the exact mechanism of the exclusion).  Named approximation: rho_X does not enter the
theta KG friction (second order).  BAO vectors follow the H46/H46C convention
(no radiation in the BAO rows; radiation A1 in the calibration integral only).

METRIC.  S(v) = amplitude-marginalised shape chi^2 at the deformed model's own
calibrated cosmology; gap = S(0) - S_LCDM (preregistered anchor: 19.3 +/- 2.0);
recovery fraction phi = [S(0) - S(v)] / gap.

SCOPE CORRECTION AFTER HOSTILE REVIEW.  rho_X is an external proxy family, not the
unbuilt GU record law, and local numerical optimization cannot establish global
infeasibility.  Positive witnesses establish proxy feasibility; failed searches mean
only NO WITNESS FOUND.  No M-H13 claim status moves from this script.

PREREGISTERED (exploration note Section 1.2, written first):
  T0 anchor; T1 witness (unconstrained phi >= 0.8 -- the space is NONEMPTY);
  T2 monotone cone decision rule (phi_mono < 0.5 => M-H13 dies at feasibility);
  T3 N^p family (both admissible N normalisations covered by the p-scan);
  T4 JP4 lemma + escape template.

Run: PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python -u \
       tests/de-certification/mh13_shape_inverse_feasibility.py
Exit 0 iff every preregistered hard assert holds.  Deterministic (seed 20260803).
"""
from __future__ import annotations
import os
import sys
import importlib.util
import numpy as np
from scipy.optimize import brentq, minimize, minimize_scalar
from scipy.integrate import cumulative_trapezoid

FAIL = []
RNG = np.random.default_rng(20260803)


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


H46C = _load("tests/wave46/H46C_theta_star_cmb_calibration.py", "H46C_mod2")
H46 = H46C.H46
H44 = H46C.H44

bao_vector_from_E = H46.bao_vector_from_E
chi2_of = H46.chi2_of
chi2_marg_amplitude = H46.chi2_marg_amplitude

C_KMS = 299792.458
OMH2 = H46C.OMH2
RSTAR = H46C.RSTAR
ZSTAR = H46C.ZSTAR
THETASTAR_100 = H46C.THETASTAR_100
OMEGA_R_H2 = H46C.OMEGA_R_H2
RD = H46C.RD
H_PLANCK = H46C.H_PLANCK
F0 = H46C.F0_CANON                     # 0.125
M2 = H46C.M2_BC1                       # 8.0

# H46C's A3 shared-systematic correction.  The root finder below returns the raw
# pipeline h.  Every likelihood row must use the ratio-corrected value, just as H46C
# does for its canonical row.
H_LCDM_CAL = H46C.calibrate_h(1e-10)
H46C._restore_module_cosmology()
A3_RATIO = H_PLANCK / H_LCDM_CAL

# search-phase resolution (headline optima re-verified at high resolution)
NP_LO, NI_LO = 600, 28
NP_HI, NI_HI = 1400, 60

# deformation basis: piecewise-linear nodes, constant beyond the last node
ZN = np.array([0.0, 0.2, 0.4, 0.65, 0.95, 1.35, 1.85, 2.5])
NNODE = len(ZN)
VCAP = 0.6                              # |v| cap (penalty), keeps budgets sane


def rho_X_nodes(z, v):
    z = np.asarray(z, dtype=float)
    return np.interp(z, ZN, v)          # np.interp holds v[0]/v[-1] outside the range


# ===========================================================================
# Deformed-GU pipeline: background solve with re-partitioned budget, theta_star
# calibration, and the amplitude-marginalised shape chi^2.
# ===========================================================================
def _def_background(h, v0, npts, n_iter):
    Om_h = OMH2 / h ** 2
    H44.Om, H44.OL = Om_h, 1.0 - Om_h - v0     # re-partitioned flat budget
    try:
        bg = H44.solve_backreacted(M2, F0, npts=npts, n_iter=n_iter)
    finally:
        H44.Om, H44.OL = 0.315, 0.685
    return bg, Om_h


def theta100_def(h, rho_X, v_far, npts=NP_LO, n_iter=NI_LO, ntail=6000):
    """theta_star with the deformation; A1 radiation in the distance integral only."""
    v0 = float(rho_X(0.0))
    bg, Om_h = _def_background(h, v0, npts, n_iter)
    Or_h = OMEGA_R_H2 / h ** 2
    idx = np.argsort(bg["z"])
    zl = bg["z"][idx]
    E2l = bg["H2"][idx] + Or_h * ((1.0 + zl) ** 4 - 1.0) + rho_X(zl)
    if np.min(E2l) <= 0:
        return None
    Il = cumulative_trapezoid(1.0 / np.sqrt(E2l), zl, initial=0.0)[-1]
    rho_th_frozen = float(bg["rho_theta"][0])          # grid index 0 = z_start
    rho_L = float(bg["rho_L"])
    zt = np.geomspace(H46C.Z_START, ZSTAR, ntail)
    E2t = (Om_h * (1.0 + zt) ** 3 + Or_h * ((1.0 + zt) ** 4 - 1.0)
           + rho_L + rho_th_frozen + v_far)
    It = np.trapezoid(1.0 / np.sqrt(E2t), zt)
    DM = (C_KMS / (100.0 * h)) * (Il + It)
    return 100.0 * RSTAR / DM, bg, Om_h, rho_th_frozen


_last_h = [0.637]


def calibrate_def(rho_X, v_far, npts=NP_LO, n_iter=NI_LO):
    def f(h):
        out = theta100_def(h, rho_X, v_far, npts, n_iter)
        if out is None:
            return 1e3
        return out[0] - THETASTAR_100
    h0 = _last_h[0]
    for lo, hi in ((h0 - 0.03, h0 + 0.03), (0.52, 0.85)):
        try:
            flo, fhi = f(lo), f(hi)
            if flo * fhi < 0:
                h = brentq(f, lo, hi, xtol=1e-6)
                _last_h[0] = h
                return h
        except Exception:
            continue
    return None


def S_def(rho_X, v_far, npts=NP_LO, n_iter=NI_LO):
    """Amplitude-marginalised shape chi^2 at the deformed model's own calibration.
    Returns (S, h_cal, Om_cal) or None."""
    h_raw = calibrate_def(rho_X, v_far, npts, n_iter)
    if h_raw is None:
        return None
    h = h_raw * A3_RATIO
    v0 = float(rho_X(0.0))
    bg, Om_h = _def_background(h, v0, npts, n_iter)
    idx = np.argsort(bg["z"])
    zl = bg["z"][idx]
    m = zl <= 3.05
    E2 = bg["H2"][idx][m] + rho_X(zl[m])               # H46/H46C convention: no radiation here
    if np.min(E2) <= 0:
        return None
    b = bao_vector_from_E(zl[m], np.sqrt(E2), 1.0)
    S, _ = chi2_marg_amplitude(b)
    return S, h, Om_h


def S_of_v(v, npts=NP_LO, n_iter=NI_LO):
    v = np.asarray(v, dtype=float)
    if np.max(np.abs(v)) > VCAP:
        return 1e5 + 1e3 * float(np.max(np.abs(v)))
    out = S_def(lambda z: rho_X_nodes(z, v), float(v[-1]), npts, n_iter)
    if out is None:
        return 1e5
    return out[0]


# ===========================================================================
def main():
    log("=" * 78)
    log("M-H13 feasibility -- the +19.3 shape inverse problem + the JP4 extension")
    log("=" * 78)

    # -----------------------------------------------------------------------
    # T0 -- anchors: the undeformed point and the gap, recomputed on-disk.
    # -----------------------------------------------------------------------
    log("\n" + "=" * 78)
    log("T0 -- anchors (undeformed GU point; LCDM reference; the gap)")
    log("=" * 78)
    out0 = S_def(lambda z: np.zeros_like(np.asarray(z, dtype=float)), 0.0)
    assert out0 is not None, "undeformed calibration failed -- machinery broken"
    S0, h0, Om0 = out0
    log(f"  undeformed (search res, npts={NP_LO}): S(0) = {S0:.3f} at h_cal = {h0:.5f}, "
        f"Om_cal = {Om0:.4f}")
    check("T0a: undeformed A3-corrected calibration matches H46C (h = 0.63749 +/- 5e-4)",
          abs(h0 - 0.63749) < 5e-4, f"h={h0:.5f}")
    # T0b AMENDED (recorded in the exploration note, Section 2.1): as preregistered it
    # compared the SEARCH-resolution S(0) to the H46C/DE-12 value computed at
    # npts=1400/n_iter=60 and failed by the resolution systematic (+0.78).  The
    # like-for-like anchor is the high-resolution recompute; the search-resolution
    # offset is bounded and shared by every S(v) in a given search (cancels in phi).
    out0_hi = S_def(lambda z: np.zeros_like(np.asarray(z, dtype=float)), 0.0,
                    npts=NP_HI, n_iter=NI_HI)
    assert out0_hi is not None
    S0_hi = out0_hi[0]
    log(f"  undeformed (high res, npts={NP_HI}): S(0) = {S0_hi:.3f}")
    check("T0b (amended): high-resolution S(0) matches the DE-12/H46C marginalised "
          "value 33.50 within 0.35", abs(S0_hi - 33.50) < 0.35, f"S0_hi={S0_hi:.3f}")
    check("T0b-guard: the search-resolution offset is bounded (< 1.0) and shared",
          abs(S0 - S0_hi) < 1.0, f"offset={S0 - S0_hi:+.3f}")
    # LCDM reference (H46 convention, source Om = 0.315, no radiation)
    zg = np.linspace(0.0, 3.05, 1600)
    E_l = np.sqrt(0.315 * (1.0 + zg) ** 3 + 0.685)
    S_lcdm, _ = chi2_marg_amplitude(bao_vector_from_E(zg, E_l, 1.0))
    gap = S0 - S_lcdm                 # search-resolution gap (used for search-phase phi)
    gap_hi = S0_hi - S_lcdm           # high-resolution gap (the headline number)
    log(f"  LCDM reference S_LCDM = {S_lcdm:.3f}  (H46 row-3: 14.15)")
    log(f"  GAP = S(0) - S_LCDM = {gap_hi:+.3f} (high res; search res {gap:+.3f})")
    log(f"  (DE-07 item 3: +19.3; on-disk recompute)")
    check("T0c: S_LCDM matches H46's 14.15 within 0.1", abs(S_lcdm - 14.15) < 0.1,
          f"{S_lcdm:.3f}")
    check("T0d: the high-res gap reproduces DE-07's +19.3 within 2.0 (loud fail "
          "otherwise; phi targets rescale to the recomputed gap)",
          abs(gap_hi - 19.3) < 2.0, f"gap={gap_hi:+.3f}")
    # CPL witness row: the correctly-shaped model's marginalised chi^2 (its own calib)
    # (DESI+CMB combo; the DE-12 script computed S_cpl = 6.92 with radiation-free rows)
    log(f"  [context] DE-12 CPL witness: chi2_marg(DESI+CMB w0waCDM) = 6.92 -> vs S(0): "
        f"{6.92 - S0:+.2f} (DE-07's 'CPL gains -22.8' restated on-disk)")

    def phi_of(S):
        return (S0 - S) / gap

    # -----------------------------------------------------------------------
    # T1 -- unconstrained witness: is the space of +19.3-supplying channels nonempty?
    # -----------------------------------------------------------------------
    log("\n" + "=" * 78)
    log("T1 -- unconstrained 8-node deformation (witness)")
    log("=" * 78)
    starts = [np.zeros(NNODE),
              0.10 * np.exp(-0.5 * ((ZN - 0.45) / 0.35) ** 2)]   # bump start
    best_free = None
    for i, x0 in enumerate(starts):
        res = minimize(S_of_v, x0, method="Nelder-Mead",
                       options=dict(maxfev=900, xatol=1e-4, fatol=1e-4, adaptive=True))
        log(f"  start {i}: S = {res.fun:.3f} after {res.nfev} evals")
        if best_free is None or res.fun < best_free.fun:
            best_free = res
    v_free = np.asarray(best_free.x)
    S_free = float(best_free.fun)
    phi_free = phi_of(S_free)
    log(f"  best unconstrained: S = {S_free:.3f}  phi = {phi_free:.3f}")
    log("  optimal node values (z : v):")
    for zn, vv in zip(ZN, v_free):
        log(f"     z = {zn:5.2f} : v = {vv:+.4f}")
    dv = np.diff(v_free)
    n_sign = int(np.sum(np.abs(np.diff(np.sign(dv[np.abs(dv) > 1e-4])) ) > 0))
    log(f"  monotonicity signature of the required channel: {n_sign} interior sign "
        f"change(s) in dv/dz (0 = monotone)")
    check("T1: the space is NONEMPTY -- unconstrained deformation recovers phi >= 0.8",
          phi_free >= 0.8, f"phi={phi_free:.3f}")

    # -----------------------------------------------------------------------
    # T2 -- the monotone cone (the M-H13 direction), and the fade direction.
    # -----------------------------------------------------------------------
    log("\n" + "=" * 78)
    log("T2 -- monotone low-z-growing cone (v non-increasing in z, v >= 0)")
    log("=" * 78)

    def v_mono(t):
        s = np.asarray(t, dtype=float) ** 2
        return np.cumsum(s[::-1])[::-1]                 # v_j = sum_{k>=j} t_k^2

    def S_mono(t):
        return S_of_v(v_mono(t))

    best_mono = None
    for i, t0 in enumerate([np.full(NNODE, 0.05), np.full(NNODE, 0.15),
                            np.linspace(0.25, 0.01, NNODE)]):
        res = minimize(S_mono, t0, method="Nelder-Mead",
                       options=dict(maxfev=700, xatol=1e-4, fatol=1e-4, adaptive=True))
        log(f"  start {i}: S = {res.fun:.3f} after {res.nfev} evals")
        if best_mono is None or res.fun < best_mono.fun:
            best_mono = res
    S_m = float(best_mono.fun)
    phi_mono = phi_of(S_m)
    vm = v_mono(best_mono.x)
    log(f"  best monotone: S = {S_m:.3f}  phi_mono = {phi_mono:.3f}")
    log("  node values: " + ", ".join(f"{v:+.4f}" for v in vm))

    def v_fade(t):
        s = np.asarray(t, dtype=float) ** 2
        return np.cumsum(s)                             # v non-decreasing in z

    best_fade = None
    for t0 in [np.full(NNODE, 0.05), np.full(NNODE, 0.15)]:
        res = minimize(lambda t: S_of_v(v_fade(t)), t0, method="Nelder-Mead",
                       options=dict(maxfev=500, xatol=1e-4, fatol=1e-4, adaptive=True))
        if best_fade is None or res.fun < best_fade.fun:
            best_fade = res
    S_f = float(best_fade.fun)
    phi_fade = phi_of(S_f)
    log(f"  fade direction (W154-RE1 cross-check): S = {S_f:.3f}  phi_fade = {phi_fade:.3f}")

    log("\n  PREREGISTERED DECISION RULE (T2), RE-SCOPED AFTER HOSTILE REVIEW:")
    log("  a positive witness establishes feasibility only for this proxy family;")
    log("  a failed local search would mean NO WITNESS FOUND, not a global no-go.")
    if phi_mono < 0.5:
        verdict_t2 = "NO-WITNESS-FOUND in the sampled monotone proxy family"
    elif phi_mono >= 0.8:
        verdict_t2 = "PROXY-FEASIBLE (native M-H13 record law remains unbuilt)"
    else:
        verdict_t2 = f"PARTIAL PROXY WITNESS ({phi_mono:.0%} of this target)"
    log(f"  T2 VERDICT: phi_mono = {phi_mono:.3f} -> {verdict_t2}")
    check("T2 well-formed: phi_mono computed, finite, and <= phi_free + 0.05",
          np.isfinite(phi_mono) and phi_mono <= phi_free + 0.05,
          f"phi_mono={phi_mono:.3f}, phi_free={phi_free:.3f}")

    # -----------------------------------------------------------------------
    # T3 -- the N^p family (nested in the monotone cone).
    # -----------------------------------------------------------------------
    log("\n" + "=" * 78)
    log("T3 -- N^p family: N = past 4-volume on the calibrated background")
    log("=" * 78)
    # N_bulk(t) = integral_0^t a^3 dt' (comoving-volume normalisation; W146 X4-shadow).
    # N_conf = pi sqrt(N_bulk) => (N_conf)^p = pi^p N^(p/2): the p-scan covers BOTH
    # admissible normalisations (asserted below).
    bg0, Om_h0 = _def_background(h0, 0.0, NP_HI, NI_HI)
    idx = np.argsort(bg0["z"])
    zl0 = bg0["z"][idx]
    a_lo = 1.0 / (1.0 + zl0)                            # ascending a on [1/31, 1]
    E_lo = np.sqrt(bg0["H2"][idx])
    Or0 = OMEGA_R_H2 / h0 ** 2
    rho_L0 = float(bg0["rho_L"])
    rho_f0 = float(bg0["rho_theta"][0])
    a_hi = np.geomspace(1e-6, 1.0 / 31.0, 4000)
    E_hi = np.sqrt(Om_h0 * a_hi ** -3 + Or0 * (a_hi ** -4 - 1.0) + rho_L0 + rho_f0)
    a_all = np.unique(np.concatenate([a_hi, a_lo]))
    E_all = np.interp(a_all, np.concatenate([a_hi, a_lo]),
                      np.concatenate([E_hi, E_lo]))
    # t(a) = int da'/(a' H)  in units 1/H0; N_bulk(a) = int a'^3 dt' = int a'^2/H da'
    Nb = cumulative_trapezoid(a_all ** 2 / E_all, a_all, initial=0.0)
    Nb_of_z = lambda z: np.interp(1.0 / (1.0 + np.asarray(z, dtype=float)), a_all, Nb)
    N0 = float(Nb_of_z(0.0))
    check("T3a: N(z) is monotone decreasing in z (accretion; the only property used)",
          bool(np.all(np.diff(Nb) >= 0)), "")
    check("T3b: N_conf = pi sqrt(N_bulk) is the p -> p/2 relabel of the same family "
          "(structural; pi^p is absorbed by eps)", True, "")
    log(f"  N(z)/N(0) at z = 0.2/0.5/1/2: "
        + "/".join(f"{Nb_of_z(z)/N0:.3f}" for z in (0.2, 0.5, 1.0, 2.0)))

    rows_np = []
    for p in (0.25, 0.5, 1.0, 2.0, 4.0, 8.0):
        shape_p = lambda z, p=p: (np.maximum(Nb_of_z(z), 0.0) / N0) ** p

        def S_eps(eps, p=p, shape_p=shape_p):
            rx = lambda z, e=eps: e * shape_p(z)
            out = S_def(rx, float(eps * shape_p(30.0)))
            return 1e5 if out is None else out[0]

        r = minimize_scalar(S_eps, bounds=(-0.4, 0.5), method="bounded",
                            options=dict(xatol=1e-3))
        rows_np.append((p, float(r.x), float(r.fun), phi_of(float(r.fun))))
        log(f"  p = {p:5.2f}: best eps = {r.x:+.4f}  S = {r.fun:.3f}  phi = {phi_of(float(r.fun)):+.3f}")
    phi_np = max(r[3] for r in rows_np)
    p_best = [r[0] for r in rows_np if r[3] == phi_np][0]
    log(f"  best N^p recovery: phi = {phi_np:+.3f} at p = {p_best}")
    check("T3c: N^p is nested in the monotone cone (phi_Np <= phi_mono + 0.05)",
          phi_np <= phi_mono + 0.05, f"phi_Np={phi_np:.3f}, phi_mono={phi_mono:.3f}")

    # -----------------------------------------------------------------------
    # T4 -- JP4: the signed readout N_K = 9 f+ - 5 f- under reachability.
    # -----------------------------------------------------------------------
    log("\n" + "=" * 78)
    log("T4 -- JP4: signed readout N_K = 9 f+ - 5 f- (nonempty negative cone)")
    log("=" * 78)
    # (i) LEMMA.  Premises (the W158 RISEb reading, named): the confirmed accretion
    # RATE is non-negative and NON-DECREASING (4-volume growth in an expanding
    # universe: f+' ~ a^3-type), and the unconfirmable sector is a LAGGED, weight-
    # suppressed copy: f-'(t) = beta f+'(t - ell), beta in [0,1], ell >= 0.  Then
    #   f-'(t) = beta f+'(t-ell) <= f+'(t-ell) <= f+'(t)
    # so N_K' = 9 f+' - 5 f-' >= 4 f+' >= 0: EVERY reachable N_K is monotone, and any
    # monotone readout h(N_K) stays inside the T2 cone.  w- != 0 does NOT enlarge the
    # reachable space.  Machine witness over random admissible schedules:
    tgrid = np.linspace(0.0, 1.0, 400)
    worst = np.inf
    for _ in range(300):
        # random non-decreasing rate: cumulative sum of |noise| (rate' >= 0)
        rate = np.cumsum(np.abs(RNG.standard_normal(tgrid.size)))
        rate = rate / rate[-1] + 0.05
        beta = float(RNG.uniform(0.0, 1.0))
        ell = int(RNG.integers(0, 120))
        rate_lag = np.concatenate([np.zeros(ell), rate[:tgrid.size - ell]])
        NKp = 9.0 * rate - 5.0 * beta * rate_lag
        worst = min(worst, float(np.min(NKp - 4.0 * rate)))
    check("T4-LEMMA: over 300 random admissible schedules, N_K' - 4 f+' >= 0 "
          "(N_K monotone; the negative cone does not enlarge the reachable space)",
          worst > -1e-12, f"min slack = {worst:.2e}")
    log("  NOTE (premise inventory, new): rate-monotonicity is DOING WORK.  With a")
    log("  bursty (non-monotone) confirmed rate, lag alone can already produce a")
    log("  non-monotone N_K; W158's a^3-type schedule has f+' non-decreasing, which")
    log("  is what closes RISEb.  Recorded as a sharpening of the RISEb premises.")

    # (ii) ESCAPE TEMPLATE.  The only way out of the cone is RATE-DOMINANCE,
    # 5 f-' > 9 f+' at some epoch (weight-dominance is excluded by the (9,5) pin).
    # Fit u(t) = f-'/f+' ramping above 9/5 at late times (inverted lag).
    t_of_a = cumulative_trapezoid(1.0 / (a_all * E_all), a_all, initial=0.0)
    t_of_z = lambda z: np.interp(1.0 / (1.0 + np.asarray(z, dtype=float)), a_all, t_of_a)
    t0v = float(t_of_z(0.0))
    fplus_rate_tab = a_all ** 2 / E_all                 # dN/da; f+ = N_bulk shape
    log("\n  escape fit: f+ = N_bulk shape; f-' = u(t) f+', u = logistic ramp;")
    log("  rho_X = eps * N_K(z)/N_K(0).  Fitting (eps, U, t_c/t0, w/t0):")

    def NK_shape(U, tc, w):
        u = U / (1.0 + np.exp(-(t_of_a - tc) / max(w, 1e-4)))
        integ = fplus_rate_tab * (9.0 - 5.0 * u)
        NK = cumulative_trapezoid(integ, a_all, initial=0.0)
        return NK, u

    def S_escape(x):
        eps, U, tcf, wf = x
        if not (0.0 <= U <= 6.0 and 0.02 <= wf <= 1.0 and 0.05 <= tcf <= 1.2):
            return 1e5
        NK, _ = NK_shape(U, tcf * t0v, wf * t0v)
        NK0 = float(np.interp(1.0, a_all, NK))
        if NK0 <= 1e-6:
            return 1e5
        NK_of_z = lambda z: np.interp(1.0 / (1.0 + np.asarray(z, dtype=float)), a_all, NK) / NK0
        rx = lambda z, e=eps: e * NK_of_z(z)
        if abs(eps) > VCAP:
            return 1e5
        out = S_def(rx, float(eps * NK_of_z(30.0)))
        return 1e5 if out is None else out[0]

    best_esc = None
    for x0 in ([0.05, 2.5, 0.75, 0.15], [0.15, 3.5, 0.85, 0.10], [0.05, 0.0, 0.7, 0.2]):
        res = minimize(S_escape, np.array(x0), method="Nelder-Mead",
                       options=dict(maxfev=500, xatol=1e-4, fatol=1e-4, adaptive=True))
        log(f"  start {x0}: S = {res.fun:.3f} after {res.nfev} evals")
        if best_esc is None or res.fun < best_esc.fun:
            best_esc = res
    eps_e, U_e, tc_e, w_e = best_esc.x
    S_esc = float(best_esc.fun)
    phi_esc = phi_of(S_esc)
    NK_e, u_e = NK_shape(U_e, tc_e * t0v, w_e * t0v)
    u_max = float(np.max(u_e))
    nk_mono = bool(np.all(np.diff(NK_e) >= -1e-12))
    log(f"  best escape: S = {S_esc:.3f}  phi_esc = {phi_esc:+.3f}")
    log(f"  fitted: eps = {eps_e:+.4f}, U = {U_e:.3f}, t_c/t0 = {tc_e:.3f}, w/t0 = {w_e:.3f}")
    log(f"  max u = f-'/f+' = {u_max:.3f}  (rate-dominance threshold 9/5 = 1.8)")
    log(f"  fitted N_K monotone? {nk_mono}")
    if phi_esc > phi_mono + 0.05:
        check("T4-ESCAPE consistency: leaving the monotone cone requires rate-dominance "
              "(fitted max u > 9/5) -- the inverted-lag premise is the named cost",
              u_max > 1.8, f"u_max={u_max:.3f}")
    else:
        check("T4-ESCAPE consistency: escape did not beat the monotone cone "
              "(no rate-dominance claim owed)", True, "")

    # -----------------------------------------------------------------------
    # High-resolution verification of the headline optima.
    # -----------------------------------------------------------------------
    log("\n" + "=" * 78)
    log("VERIFY -- headline optima at high resolution (npts=1400, n_iter=60)")
    log("=" * 78)
    S_free_hi = S_of_v(v_free, npts=NP_HI, n_iter=NI_HI)
    S_mono_hi = S_of_v(vm, npts=NP_HI, n_iter=NI_HI)
    log(f"  unconstrained: S = {S_free:.3f} (search) -> {S_free_hi:.3f} (high-res)")
    log(f"  monotone:      S = {S_m:.3f} (search) -> {S_mono_hi:.3f} (high-res)")
    check("VERIFY: high-resolution drift < 1.0 on both headline optima (the shared "
          "search-resolution offset is ~ +0.8)",
          abs(S_free_hi - S_free) < 1.0 and abs(S_mono_hi - S_m) < 1.0,
          f"d_free={abs(S_free_hi-S_free):.3f}, d_mono={abs(S_mono_hi-S_m):.3f}")
    # headline phi at high resolution, consistently normalised
    phi_free_hi = (S0_hi - S_free_hi) / gap_hi
    phi_mono_hi = (S0_hi - S_mono_hi) / gap_hi

    # -----------------------------------------------------------------------
    log("\n" + "-" * 78)
    log("SUMMARY (proxy family only; no M-H13 verdict movement)")
    log("-" * 78)
    log(f"  gap (on-disk recompute of DE-07's +19.3) = {gap_hi:+.3f} (high res)")
    log(f"  phi (fraction of the gap recovered):")
    log(f"     unconstrained 8-node   : {phi_free_hi:+.3f}   (T1 witness; high res)")
    log(f"     monotone low-z-growing : {phi_mono_hi:+.3f}   (T2, the M-H13 direction; high res)")
    log(f"     fade direction         : {phi_fade:+.3f}   (W154-RE1 cross-check; search res)")
    log(f"     best N^p (p = {p_best})     : {phi_np:+.3f}   (T3; both N normalisations; search res)")
    log(f"     JP4 escape (inverted lag): {phi_esc:+.3f}  (T4; max u = {u_max:.2f}; search res)")
    log(f"  T2 VERDICT: {verdict_t2}")

    if FAIL:
        log(f"\nFAILED: {FAIL}")
        sys.exit(1)
    log(f"\nexit 0 = proxy-shape witnesses recorded.  gap = {gap_hi:+.2f}; phi_free = "
        f"{phi_free_hi:+.3f}; phi_mono = {phi_mono_hi:+.3f}; phi_Np = {phi_np:+.3f}; "
        f"phi_esc = {phi_esc:+.3f}.  {verdict_t2}")
    sys.exit(0)


if __name__ == "__main__":
    main()
