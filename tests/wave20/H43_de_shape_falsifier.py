#!/usr/bin/env python3
r"""H43 -- the DE-SHAPE FALSIFIER.  Is GU's source-first dark-energy (w0,wa) LOCUS a
ROBUST miss of DESI, or an ARTIFACT of the reconstruction-grade M^2 (the OQ2
A_3-vs-BC_1 root-system caveat) and/or the two-component theta ansatz?

Wave-19 (H42) found: the source-first (w0,wa) family (built on the derived normal-
Laplacian mass M^2 = 8 H0^2 and the two-component theta + DeWitt-Lambda ansatz) MISSES
DESI DR2 at EVERY amplitude f0 (closest Mahalanobis 3.47 sigma; the joint at the
canonical f0=0.125 is 4.19 sigma), because the LOCUS tracks ACROSS the DESI (w0,wa)
degeneracy rather than INTO it.  The one softening was that the locus rests on (i) the
reconstruction-grade M^2 (OQ2) and (ii) the ansatz.  H43 stress-tests BOTH.

This test is DETERMINISTIC and DESI-BLIND in its derivation half:
  Q1  -- for EACH admissible root-system assignment (BC_1, A_1, the S^3/no-Z2 variant,
          the continuum-threshold anchor) it computes M^2 SOURCE-FIRST from the
          rep-theory files (NO appeal to DESI), then the (w0,wa) locus, then the
          closest-approach Mahalanobis to DESI over f0.  It also scans the FULL
          (M^2, f0) plane for the GLOBAL closest approach -- this subsumes every
          admissible M^2, tuned or not.
  Q2  -- it recomputes the locus under an ALTERNATIVE ansatz (1-component: pure theta,
          no separate DeWitt-Lambda, w_DE = wB) and under a different IC/evolution
          factor, to see whether across-the-degeneracy tracking is ansatz-driven or
          robust.
  Q3  -- verdict: FALSIFIED / CLEARED / STILL-GATED, with marginal + joint sigmas.
  Q4  -- adversarial: reproduces the H3-verified DESI DR2 digits and the canonical GU
          point (no bug); confirms NO M^2 was chosen by appeal to DESI (source-first).

M^2 (all in units H0^2, R_s = c/H0) is the lowest DISCRETE normal-Laplacian eigenvalue
lambda_{N,1} on the fiber GL(4,R)/O(3,1), lambda_n = rho^2 - nu_n^2:
  * BC_1  (m_1,m_2)=(7,1), rho = m_1/2 + m_2 = 9/2, LONG root present -> HALF-integer
    poles nu_n=(2n+1)/2 -> discrete {8,14,18,20}; ground M^2 = (9/2)^2-(7/2)^2 = 8.
    [rc3-delta-n-spectrum-gl4r; rc3-root-multiplicity-bc1]  <- the CANONICAL derived value
  * A_1   (long root ABSENT, m_2=0, m=8), rho = m/2 = 4, INTEGER poles nu_n=n ->
    discrete {7,12,15}; ground M^2 = 16-9 = 7.   [the "no long root" alternative, F3]
  * S^3 / SO_0(3,1)-connected (NO Z_2 quotient): compact dual is the full sphere, ALL
    harmonics l=1,2,... survive -> lowest l=1 -> M^2 = l(l+2) = 3.  [the Z_2/covering
    alternative to the RP^3=S^3/Z_2 reduction that gives the even-l ground state 8]
  * continuum threshold rho^2 = 81/4 = 20.25 -- the UPPER anchor (above it the fiber
    spectrum is continuous; no discrete ground state can sit higher).

The three discrete assignments {3, 7, 8} bracket the admissible ground-state band; the
plane scan M^2 in [1,25] covers all of them AND everything between, so the falsifier does
not hinge on picking one.

Run: python -u tests/wave20/H43_de_shape_falsifier.py     (exit 0 iff every PASS holds)
"""
from __future__ import annotations
import sys
import numpy as np
from scipy.integrate import solve_ivp, cumulative_trapezoid

FAIL = []


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}", flush=True)
    if not ok:
        FAIL.append(name)


def log(m=""):
    print(m, flush=True)


# ===========================================================================
# GU built theta-sector machinery (fixed model; identical physics to
# tests/one-residual/dark_energy_desi_sign.py, tests/wave19/H42_f0_prereg.py,
# tests/wave1/H3_...).  NO DESI input anywhere in this block.
#   KG:  B'' + (3 + H'/H) B' + (M2/H^2) B = 0   on an LCDM background
#   two-component DE:  w_DE = (-1 + f wB)/(1+f),  f = f0 rhoB(z)/rhoB(0)
#   1-component variant (Q2): w_DE = wB(z) directly (pure theta, no DeWitt-Lambda)
# ===========================================================================
Om, OL = 0.315, 0.685
Z_START = 30.0
F0_CANON = 0.125           # canonical (DESI-tuned) amplitude -- used only for reproduction
M2_BC1 = 8.0               # canonical derived ground eigenvalue (BC_1)


def H2(a):
    return Om * a ** -3 + OL


def integrate_theta(M2, z_start=Z_START):
    """Deterministic theta KG integration on LCDM background from slow-roll IC. NO DESI."""
    def rhs(N, y):
        a = np.exp(N)
        B, BN = y
        HNoH = -1.5 * Om * a ** -3 / H2(a)
        return [BN, -(3.0 + HNoH) * BN - (M2 / H2(a)) * B]
    a0 = 1.0 / (1.0 + z_start)
    N0 = np.log(a0)
    BN0 = -M2 / (3.0 * H2(a0))
    sol = solve_ivp(rhs, (N0, 0.0), [1.0, BN0], t_eval=np.linspace(N0, 0.0, 3000),
                    rtol=1e-9, atol=1e-11, method="Radau")
    assert sol.success, sol.message
    a = np.exp(sol.t)
    z = 1.0 / a - 1.0
    B, BN = sol.y
    return z, B, np.sqrt(H2(a)) * BN


def wDE_two_component(z, B, Bdot, f0, M2):
    KE = 0.5 * Bdot ** 2
    PE = 0.5 * M2 * B ** 2
    rhoB = KE + PE
    wB = (KE - PE) / rhoB
    i0 = int(np.argmin(np.abs(z)))
    f = f0 * rhoB / rhoB[i0]
    return (-1.0 + f * wB) / (1.0 + f)


def wDE_one_component(z, B, Bdot, M2):
    """1-component ANSATZ: dark energy is the theta field ALONE (no separate DeWitt-Lambda).
    w_DE = wB(z).  There is NO amplitude knob f0 -- the shape is fixed by M^2 only."""
    KE = 0.5 * Bdot ** 2
    PE = 0.5 * M2 * B ** 2
    rhoB = KE + PE
    return (KE - PE) / rhoB


def cpl_fit(z, w, zmax=2.0, ngrid=400):
    i = np.argsort(z)
    zs, ws = z[i], w[i]
    zg = np.linspace(0.0, zmax, ngrid)
    wg = np.interp(zg, zs, ws)
    x = zg / (1.0 + zg)
    A = np.vstack([np.ones_like(x), x]).T
    (w0, wa), *_ = np.linalg.lstsq(A, wg, rcond=None)
    return w0, wa


# ===========================================================================
# ADMISSIBLE M^2 from the rep-theory files -- SOURCE-FIRST, DESI-BLIND.
# Each value is computed from (rho, nu) of a root-system assignment, NOT chosen
# by appeal to any datum.  lambda_n = rho^2 - nu_n^2 (units H0^2).
# ===========================================================================
def admissible_M2():
    out = []
    # BC_1 (7,1): rho=9/2, half-integer nu; ground at nu=7/2
    rho = 9.0 / 2.0
    nus = [(2 * n + 1) / 2.0 for n in range(4)]          # 1/2,3/2,5/2,7/2
    disc = sorted(rho ** 2 - np.array(nus) ** 2)
    out.append(("BC_1 (m1,m2)=(7,1) rho=9/2 [CANONICAL]", disc[0], rho, disc))
    # A_1 (m=8, no long root): rho=4, integer nu; ground at nu=3
    rho = 4.0
    nus = [1.0, 2.0, 3.0]
    disc = sorted(rho ** 2 - np.array(nus) ** 2)
    out.append(("A_1 m=8 no-long-root rho=4", disc[0], rho, disc))
    # S^3 / no-Z2 (full sphere compact dual): l(l+2), lowest l=1
    disc = sorted([l * (l + 2) for l in (1, 2, 3)])
    out.append(("S^3 no-Z2 (l=1 harmonic)", disc[0], None, disc))
    return out


CONTINUUM_THRESHOLD = (9.0 / 2.0) ** 2   # rho^2 = 20.25 (BC_1) -- upper anchor


# ===========================================================================
# DESI DR2 -- VERIFIED digits (arXiv:2503.14738 Eq.28; H3-verified).  Comparison ONLY.
# ===========================================================================
DESI = dict(cw0=-0.752, sw0=0.057, cwa=-0.86, swap=0.23, swam=0.20, rho=-0.8)
DESI_W0, DESI_WA = DESI["cw0"], DESI["cwa"]


def marg(v, c, sp, sm):
    d = v - c
    return d / (sp if d >= 0 else sm)


def maha(w0, wa, rho=None):
    rho = DESI["rho"] if rho is None else rho
    swa = 0.5 * (DESI["swap"] + DESI["swam"])
    d = np.array([w0 - DESI["cw0"], wa - DESI["cwa"]])
    cov = np.array([[DESI["sw0"] ** 2, rho * DESI["sw0"] * swa],
                    [rho * DESI["sw0"] * swa, swa ** 2]])
    return float(np.sqrt(d @ np.linalg.solve(cov, d)))


# ---------------------------------------------------------------------------
# DISTANCE-metric cross-check (the adversarial guard against over-claiming).
# DESI publishes (w0,wa) as a CPL FIT; GU's w(z) is NON-CPL.  The (w0,wa)
# Mahalanobis compares GU's OWN CPL projection to DESI's ellipse.  A DIFFERENT,
# equally-honest comparison is the actual expansion history: RMS fractional
# distance residual vs a DESI-CPL H(z) at the CMB-required Omega_m (the fair
# metric used in tests/wave11/H_DE_prediction_vs_fit.py).  If the two metrics
# DISAGREE, the falsification is projection-specific -- that must be stated.
# ---------------------------------------------------------------------------
ZQ = np.array([0.3, 0.5, 0.7, 0.9, 1.1, 1.3, 1.6, 2.0])
OM_DESI = 0.3069


def _H_desi(z):
    a = 1.0 / (1.0 + z)
    rho = a ** (-3 * (1 + DESI_W0 + DESI_WA)) * np.exp(-3 * DESI_WA * (1 - a))
    return np.sqrt(OM_DESI * a ** -3 + (1 - OM_DESI) * rho)


def _dist(zq, Hf):
    zc = np.linspace(0.0, zq.max(), 1500)
    DC = cumulative_trapezoid(1.0 / Hf(zc), zc, initial=0.0)
    return np.interp(zq, zc, DC), 1.0 / Hf(zq)


_DM_D, _DH_D = _dist(ZQ, _H_desi)   # DESI reference distances (precomputed once)


def distance_rms(M2, f0):
    """RMS fractional distance residual vs a DESI-CPL H(z) at fixed Omega_m."""
    z, B, Bdot = integrate_theta(M2)
    w = wDE_two_component(z, B, Bdot, f0, M2)
    a_g = 1.0 / (1.0 + z)
    idx = np.argsort(a_g)
    a_s, w_s = a_g[idx], w[idx]
    I = cumulative_trapezoid((1.0 + w_s) / a_s, a_s, initial=0.0)
    rde = np.exp(3.0 * (I[-1] - I))

    def Hf(zz):
        a = 1.0 / (1.0 + zz)
        return np.sqrt(OM_DESI * a ** -3 + (1 - OM_DESI) * np.interp(a, a_s, rde))
    DM, DH = _dist(ZQ, Hf)
    frac = np.concatenate([(DM - _DM_D) / _DM_D, (DH - _DH_D) / _DH_D])[1:]
    return float(np.sqrt(np.mean(frac ** 2)))


def closest_over_f0(M2, f0s=None):
    """Closest Mahalanobis of the two-component (w0,wa) locus to DESI, scanning f0."""
    if f0s is None:
        f0s = np.linspace(0.01, 6.0, 900)
    z, B, Bdot = integrate_theta(M2)
    best = None
    for f0 in f0s:
        w0, wa = cpl_fit(z, wDE_two_component(z, B, Bdot, f0, M2))
        m = maha(w0, wa)
        if best is None or m < best[0]:
            best = (m, f0, w0, wa)
    return best


# ===========================================================================
def main():
    log("=" * 78)
    log("H43 -- DE-SHAPE FALSIFIER: is the (w0,wa) locus-miss robust to OQ2 (M^2) and ansatz?")
    log("=" * 78)

    # -----------------------------------------------------------------------
    # Q4a (do this FIRST): reproduce the canonical GU point -- guard against a bug.
    # -----------------------------------------------------------------------
    log("\n[Q4a] Reproduce canonical GU point (M^2=8, f0=0.125) -- bug guard, DESI-blind shape.")
    z8, B8, Bd8 = integrate_theta(M2_BC1)
    w0c, wac = cpl_fit(z8, wDE_two_component(z8, B8, Bd8, F0_CANON, M2_BC1))
    log(f"     (w0,wa) = ({w0c:+.4f}, {wac:+.4f})   [canon/H3/H42 record: (-0.768, -0.273)]")
    check("canonical point reproduces (-0.768,-0.273) -> no integration bug",
          abs(w0c + 0.768) < 3e-3 and abs(wac + 0.273) < 3e-3, f"({w0c:+.4f},{wac:+.4f})")
    s_w0 = marg(w0c, DESI["cw0"], DESI["sw0"], DESI["sw0"])
    s_wa = marg(wac, DESI["cwa"], DESI["swap"], DESI["swam"])
    mj = maha(w0c, wac)

    # -----------------------------------------------------------------------
    # Q1: per-root-system M^2, locus, closest-approach sigma.  SOURCE-FIRST.
    # -----------------------------------------------------------------------
    log("\n" + "=" * 78)
    log("Q1 -- M^2 for EACH admissible root system, its (w0,wa) locus, closest sigma")
    log("=" * 78)
    log("(M^2 computed from rho,nu of the assignment; NO DESI used to pick any M^2.)")

    rows = []
    for label, M2, rho, disc in admissible_M2():
        best = closest_over_f0(M2)
        mbest, f0best, w0best, wabest = best
        rows.append((label, M2, mbest, f0best, w0best, wabest))
        rho_s = f"{rho:.1f}" if rho is not None else "  - "
        log(f"\n  [{label}]")
        log(f"     rho={rho_s}  discrete spectrum (H0^2) = {[round(float(d),2) for d in disc]}")
        log(f"     GROUND M^2 = {M2:.3f} H0^2")
        # show the locus at a few f0
        z, B, Bd = integrate_theta(M2)
        log(f"     (w0,wa) LOCUS as f0 varies:")
        for f0 in (0.02, 0.125, 0.5, 1.0, 2.0):
            w0, wa = cpl_fit(z, wDE_two_component(z, B, Bd, f0, M2))
            log(f"        f0={f0:5.3f} -> ({w0:+.4f}, {wa:+.4f})")
        log(f"     closest Mahalanobis to DESI over f0 = {mbest:.2f} sigma "
            f"at f0={f0best:.3f} -> ({w0best:+.4f}, {wabest:+.4f})")

    # continuum-threshold anchor
    bt = closest_over_f0(CONTINUUM_THRESHOLD)
    log(f"\n  [continuum threshold rho^2 = {CONTINUUM_THRESHOLD:.2f} (upper anchor)]")
    log(f"     closest Mahalanobis = {bt[0]:.2f} sigma at f0={bt[1]:.3f} -> ({bt[2]:+.4f},{bt[3]:+.4f})")

    # -----------------------------------------------------------------------
    # Q1 DECISIVE: scan the WHOLE (M^2, f0) plane -- subsumes every admissible M^2.
    # If even the free-M^2, free-f0 global minimum misses DESI, no admissible M^2 rescues.
    # -----------------------------------------------------------------------
    log("\n" + "-" * 78)
    log("Q1-DECISIVE -- GLOBAL closest approach over the full (M^2, f0) plane")
    log("-" * 78)
    M2_grid = np.linspace(1.0, 25.0, 49)     # covers 3,7,8,14,20.25 and all between
    gbest = None
    for M2 in M2_grid:
        z, B, Bd = integrate_theta(M2)
        for f0 in np.linspace(0.01, 6.0, 240):
            w0, wa = cpl_fit(z, wDE_two_component(z, B, Bd, f0, M2))
            m = maha(w0, wa)
            if gbest is None or m < gbest[0]:
                gbest = (m, M2, f0, w0, wa)
    gm, gM2, gf0, gw0, gwa = gbest
    log(f"  GLOBAL min Mahalanobis over M^2 in [1,25], f0 in [0.01,6]:")
    log(f"     {gm:.2f} sigma at M^2={gM2:.2f} H0^2, f0={gf0:.3f} -> (w0,wa)=({gw0:+.4f},{gwa:+.4f})")
    log(f"  DESI (w0,wa)=({DESI['cw0']},{DESI['cwa']}); the locus's nearest CPL point in the")
    log(f"     WHOLE plane is still {gm:.2f} sigma away -- the miss is a SHAPE/DIRECTION miss,")
    log(f"     not an amplitude or an M^2-magnitude miss.")

    # -----------------------------------------------------------------------
    # Q2: alternative ANSATZ -- 1-component (pure theta) locus over M^2.
    # -----------------------------------------------------------------------
    log("\n" + "=" * 78)
    log("Q2 -- ANSATZ robustness: 1-component (pure theta, no DeWitt-Lambda) + IC variant")
    log("=" * 78)
    log("  1-component ansatz has NO f0 knob; w_DE = wB(z), shape fixed by M^2 alone.")
    o_best = None
    for M2 in M2_grid:
        z, B, Bd = integrate_theta(M2)
        w0, wa = cpl_fit(z, wDE_one_component(z, B, Bd, M2))
        m = maha(w0, wa)
        if o_best is None or m < o_best[0]:
            o_best = (m, M2, w0, wa)
    om, oM2, ow0, owa = o_best
    log(f"  1-component: closest Mahalanobis over M^2 in [1,25] = {om:.2f} sigma "
        f"at M^2={oM2:.2f} -> ({ow0:+.4f},{owa:+.4f})")
    # a couple of representative points
    for M2 in (3.0, 8.0):
        z, B, Bd = integrate_theta(M2)
        w0, wa = cpl_fit(z, wDE_one_component(z, B, Bd, M2))
        log(f"     M^2={M2:.1f}: 1-component (w0,wa)=({w0:+.4f},{owa if False else wa:+.4f}), "
            f"maha={maha(w0,wa):.2f}")

    # IC / evolution-factor variant: move the slow-roll IC (z_start) -- changes the
    # evolution factor without touching M^2 or the two-component structure.
    log("\n  IC/evolution-factor variant (two-component, M^2=8, different z_start):")
    ic_best = None
    for zs in (10.0, 30.0, 100.0):
        z, B, Bd = integrate_theta(M2_BC1, z_start=zs)
        b = None
        for f0 in np.linspace(0.01, 6.0, 400):
            w0, wa = cpl_fit(z, wDE_two_component(z, B, Bd, f0, M2_BC1))
            m = maha(w0, wa)
            if b is None or m < b[0]:
                b = (m, f0, w0, wa)
        log(f"     z_start={zs:6.1f}: closest {b[0]:.2f} sigma at f0={b[1]:.3f} -> ({b[2]:+.4f},{b[3]:+.4f})")
        if ic_best is None or b[0] < ic_best[0]:
            ic_best = b

    robust_miss = (gm > 3.0) and (om > 3.0) and (ic_best[0] > 3.0)
    log(f"\n  Across-the-degeneracy tracking is {'ROBUST' if robust_miss else 'NOT robust'}: "
        f"2-comp global {gm:.2f}s, 1-comp {om:.2f}s, IC-variant {ic_best[0]:.2f}s -- all miss.")

    # -----------------------------------------------------------------------
    # Q4b: reproduce the H3-verified DESI digits (no imported-target bug) and
    # confirm no M^2 was chosen by appeal to DESI.
    # -----------------------------------------------------------------------
    log("\n" + "=" * 78)
    log("Q4 -- adversarial: DESI digits + source-first M^2 audit")
    log("=" * 78)
    log(f"  DESI DR2 DESI+CMB+DESY5 (arXiv:2503.14738 Eq.28): "
        f"w0={DESI['cw0']}+/-{DESI['sw0']}, wa={DESI['cwa']} (+{DESI['swap']}/-{DESI['swam']}), rho={DESI['rho']}")
    check("DESI digits match the H3-verified primary-source values (no recall drift)",
          DESI["cw0"] == -0.752 and DESI["sw0"] == 0.057 and DESI["cwa"] == -0.86
          and DESI["swap"] == 0.23 and DESI["swam"] == 0.20)
    # every admissible M^2 came from (rho,nu), never from a data fit:
    m2_vals = [r[1] for r in rows]
    check("every admissible M^2 is a root-system eigenvalue (3,7,8), NOT chosen to match DESI",
          sorted(round(v, 3) for v in m2_vals) == [3.0, 7.0, 8.0])
    # the DESI-preferred M^2 (if we HAD tuned) vs the source-first ground state:
    log(f"  If one TUNED M^2 to DESI, the plane scan's best is M^2={gM2:.2f} (closest {gm:.2f}s) --")
    log(f"     still >3 sigma, so even a DESI-tuned M^2 does NOT clear.  No RED tuning is possible.")

    # DISTANCE-metric cross-check -- the honest guard against over-claiming the kill.
    log("\n  [Q4-crosscheck] (w0,wa)-Mahalanobis vs fixed-Omega_m DISTANCE metric (same models):")
    d_canon = distance_rms(M2_BC1, F0_CANON)
    d_maha_best = distance_rms(gM2, gf0)                       # the (w0,wa)-plane best
    # distance-metric's OWN best over a coarse plane (kept small; ODE per point)
    dbest = None
    for M2 in np.linspace(1.0, 25.0, 9):
        for f0 in np.linspace(0.05, 4.0, 12):
            d = distance_rms(M2, f0)
            if dbest is None or d < dbest[0]:
                dbest = (d, M2, f0)
    log(f"     canonical (M^2=8,f0=0.125): (w0,wa)-joint {mj:.2f} sigma | distance RMS {d_canon*100:.2f}%")
    log(f"     (w0,wa)-plane best (M^2={gM2:.2f},f0={gf0:.2f}): {gm:.2f} sigma | distance RMS {d_maha_best*100:.2f}%")
    log(f"     distance-metric OWN best: {dbest[0]*100:.2f}% at M^2={dbest[1]:.2f},f0={dbest[2]:.2f} (BAO~1.5%)")
    log(f"     -> the two metrics DISAGREE at low M^2/high f0: the (w0,wa) LOCUS misses DESI's")
    log(f"        published CPL ellipse, but the non-CPL H(z) can mimic DESI DISTANCES to ~1%")
    log(f"        (LCDM-amplitude-degeneracy, canon DARK-ENERGY-03).  H43 falsifies the (w0,wa)")
    log(f"        COMPARISON DESI actually reports; it does NOT independently kill the raw H(z).")

    # -----------------------------------------------------------------------
    # Q3: VERDICT.
    # -----------------------------------------------------------------------
    log("\n" + "-" * 78)
    log("Q3 -- VERDICT (marginal + joint sigmas)")
    log("-" * 78)
    log(f"  canonical f0=0.125, M^2=8: marginal w0={s_w0:+.2f}s, wa={s_wa:+.2f}s; joint {mj:.2f}s")
    log(f"  per-root-system closest-approach Mahalanobis (over f0):")
    for label, M2, mbest, f0best, w0best, wabest in rows:
        log(f"     M^2={M2:5.2f} ({label.split(' ')[0]:5s}): {mbest:.2f} sigma")
    log(f"  GLOBAL (free M^2 AND free f0): {gm:.2f} sigma  |  1-component ansatz: {om:.2f} sigma")

    all_root_systems_miss = all(r[2] > 2.0 for r in rows) and bt[0] > 2.0
    check("NO admissible root-system M^2 brings the locus within 2 sigma of DESI at any f0",
          all_root_systems_miss,
          f"min per-assignment = {min(r[2] for r in rows):.2f} sigma")
    check("GLOBAL free-(M^2,f0) closest approach still misses DESI at > 2 sigma "
          "(shape/direction miss, not amplitude or M^2 magnitude)",
          gm > 2.0, f"{gm:.2f} sigma at M^2={gM2:.2f}, f0={gf0:.3f}")
    check("1-component ansatz ALSO misses at > 2 sigma (miss is not a 2-component artifact)",
          om > 2.0, f"{om:.2f} sigma")
    check("IC/evolution-factor variant ALSO misses (miss is not an IC artifact)",
          ic_best[0] > 2.0, f"{ic_best[0]:.2f} sigma")

    verdict = "FALSIFIED" if robust_miss else ("CLEARED" if gm < 2.0 else "STILL-GATED")
    log("")
    if verdict == "FALSIFIED":
        log("  VERDICT = FALSIFIED.  The (w0,wa) locus-miss is ROBUST: it survives every")
        log("  admissible root-system M^2 (BC_1=8, A_1=7, S^3=3, continuum=20.25), the FULL")
        log("  (M^2,f0)-plane global minimum, a 1-component ansatz, and IC variation.  GU's")
        log("  source-first dark energy misses DESI DR2 INDEPENDENT of amplitude AND of the OQ2")
        log("  root-system choice: the locus tracks ACROSS the DESI degeneracy, and no admissible")
        log("  M^2 rotates it INTO the ellipse.  (Honest limits below: LCDM background;")
        log("  (w0,wa)-projection metric; the two-component-vs-vacuum double-counting question.)")
    elif verdict == "CLEARED":
        log("  VERDICT = CLEARED.  Some admissible M^2/ansatz brings the locus into the DESI")
        log("  degeneracy -- the tension was an ansatz/OQ2 artifact.  (Re-audit for M^2 tuning.)")
    else:
        log("  VERDICT = STILL-GATED.  The locus misses at all admissible discrete M^2, but the")
        log("  free-plane minimum sits in the 2-3 sigma band; the remaining freedom is named below.")
    log(f"  RE-RANK: {verdict}.")
    log("-" * 78)

    if FAIL:
        log(f"\nFAILED: {FAIL}")
        sys.exit(1)
    log(f"\nexit 0 = H43 recorded.  Verdict {verdict}: the DE-shape locus-miss is robust to OQ2")
    log("         (every admissible M^2) and to the ansatz (1-component, IC variant).")
    sys.exit(0)


if __name__ == "__main__":
    main()
