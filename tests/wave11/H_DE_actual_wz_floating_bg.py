"""Fair DESI test: GU-theta's ACTUAL (non-CPL) w(z) + a FLOATING background, compared on DISTANCES not CPL params.

THE HETERODOX POSSIBILITY. The standing ~3-4 sigma DESI tension is against a 2-parameter CPL FIT of the
theta model (w0=-0.78, wa=-0.25) at a FROZEN LCDM background. But (a) the theta w(z) is a real Klein-Gordon
field evolution, NOT CPL -- CPL is a lossy projection; and (b) BAO does not measure (w0,wa), it measures
DISTANCES (D_M/rd, D_H/rd). A fair test compares the ACTUAL theta expansion history to the DESI-preferred
one on DISTANCES, with Omega_m FLOATING. If the CPL-parameter tension OVER-STATES the observable (distance)
tension, the fair comparison shrinks it; if the shallow evolution is intrinsic, it stands.

MODEL (from tests/one-residual/dark_energy_desi_sign.py, reproduced): theta = KG field B, M^2=8 H0^2,
slow-roll IC at z=30; two-component DE w_DE = (-1 + f wB)/(1+f), f = f0 rhoB(z)/rhoB(0), f0=0.125,
wB=(KE-PE)/(KE+PE). This gives the ACTUAL non-CPL w_DE(z).

FAIR COMPARISON. Build H_GU(z) from the ACTUAL w_DE(z) (rho_DE via exp[3 int (1+w)/a da]) with Omega_m
FLOATING; compute D_M(z)=int dz/H and D_H(z)=1/H over the DESI window; compare to the DESI-preferred CPL
model (w0=-0.752, wa=-0.86, Omega_m=0.3069) as fractional distance residuals; find the best-fit Omega_m and
report the residual against BAO's ~1-2% precision. HONEST CAVEATS: the w(z) is computed on an LCDM background
(not fully self-consistent -- a further tightening); f0 held fixed (floating it is the separate prediction-vs-
fit question); the DESI-CPL model is a data proxy (not the raw BAO table). This is a computation, not a rescue.

Run: python tests/wave11/H_DE_actual_wz_floating_bg.py
"""
from __future__ import annotations

import numpy as np
from scipy.integrate import solve_ivp

Om_LCDM, OL_LCDM = 0.315, 0.685   # background the field is integrated on
M2, F0, Z_START = 8.0, 0.125, 30.0
# DESI DR2 DESI+CMB+DESY5 preferred model (H3 / arXiv:2503.14738)
W0_DESI, WA_DESI, OM_DESI = -0.752, -0.86, 0.3069

FAIL = []


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)


# ---- integrate the theta KG field on the LCDM background (e-fold Radau) ----
def H2_bg(a):
    return Om_LCDM * a ** -3 + OL_LCDM


def rhs_efold(N, y):
    a = np.exp(N)
    B, BN = y
    HNoH = -1.5 * Om_LCDM * a ** -3 / H2_bg(a)
    return [BN, -(3.0 + HNoH) * BN - (M2 / H2_bg(a)) * B]


def theta_wz():
    a0 = 1.0 / (1.0 + Z_START)
    N0 = np.log(a0)
    BN0 = -M2 / (3.0 * H2_bg(a0))
    Ns = np.linspace(N0, 0.0, 6000)
    sol = solve_ivp(rhs_efold, (N0, 0.0), [1.0, BN0], t_eval=Ns,
                    rtol=1e-10, atol=1e-12, method="Radau")
    a = np.exp(sol.t)
    z = 1.0 / a - 1.0
    B, BN = sol.y
    Bdot = np.sqrt(H2_bg(a)) * BN
    KE, PE = 0.5 * Bdot ** 2, 0.5 * M2 * B ** 2
    rhoB = KE + PE
    wB = (KE - PE) / rhoB
    i0 = int(np.argmin(np.abs(z)))
    f = F0 * rhoB / rhoB[i0]
    wDE = (-1.0 + f * wB) / (1.0 + f)
    # sort ascending in a
    idx = np.argsort(a)
    return a[idx], z[idx], wDE[idx]


def cpl_fit(z, w, zmax=2.0):
    m = z <= zmax
    x = z[m] / (1.0 + z[m])
    A = np.vstack([np.ones_like(x), x]).T
    (w0, wa), *_ = np.linalg.lstsq(A, w[m], rcond=None)
    return w0, wa


def rho_de_from_w(a_grid, w_grid):
    """rho_DE(a)/rho_DE0 = exp[3 int_a^1 (1+w)/a' da']  (a_grid ascending, a=1 at end)."""
    integrand = (1.0 + w_grid) / a_grid
    # cumulative integral from a to 1
    from scipy.integrate import cumulative_trapezoid
    I = cumulative_trapezoid(integrand, a_grid, initial=0.0)
    I = I[-1] - I                 # int_a^1
    return np.exp(3.0 * I)


def distances(zq, Hz_func):
    """D_M(z)=int_0^z dz'/H, D_H(z)=1/H, in units c/H0 (H in units H0)."""
    zc = np.linspace(0.0, zq.max(), 2000)
    Hc = Hz_func(zc)
    from scipy.integrate import cumulative_trapezoid
    DC = cumulative_trapezoid(1.0 / Hc, zc, initial=0.0)
    DM = np.interp(zq, zc, DC)
    DH = 1.0 / Hz_func(zq)
    return DM, DH


def main():
    print("[fair DESI test: actual theta w(z), floating background, distance comparison]\n")
    a_g, z_g, w_g = theta_wz()
    w0f, waf = cpl_fit(z_g, w_g)
    print(f"    theta actual w(z): w(0)={np.interp(0.0,z_g,w_g):+.3f}, w(1)={np.interp(1.0,z_g,w_g):+.3f}, "
          f"w(2)={np.interp(2.0,z_g,w_g):+.3f}; CPL-fit (w0,wa)=({w0f:+.3f},{waf:+.3f})")
    # is the actual w(z) faithfully CPL? residual of the CPL fit
    m = z_g <= 2.0
    cpl_pred = w0f + waf * z_g[m] / (1.0 + z_g[m])
    cpl_rms = np.sqrt(np.mean((w_g[m] - cpl_pred) ** 2))
    print(f"    CPL-fit RMS residual to the actual w(z) over z<=2: {cpl_rms:.4f}  "
          f"({'CPL is faithful -> non-CPL shape is NOT a lever' if cpl_rms < 0.02 else 'actual w(z) has non-CPL structure'})")

    rho_de = rho_de_from_w(a_g, w_g)

    def rho_de_of_z(z):
        a = 1.0 / (1.0 + z)
        return np.interp(a, a_g, rho_de)

    def H_GU(z, Om):
        a = 1.0 / (1.0 + z)
        return np.sqrt(Om * a ** -3 + (1.0 - Om) * rho_de_of_z(z))

    def H_DESI(z, Om=OM_DESI):
        a = 1.0 / (1.0 + z)
        rho = a ** (-3 * (1 + W0_DESI + WA_DESI)) * np.exp(-3 * WA_DESI * (1 - a))
        return np.sqrt(Om * a ** -3 + (1.0 - Om) * rho)

    # DESI window BAO-ish redshifts
    zq = np.array([0.3, 0.5, 0.7, 0.9, 1.1, 1.3, 1.6, 2.0])
    DM_d, DH_d = distances(zq, lambda z: H_DESI(z))

    # float Omega_m for GU-theta to best-match the DESI distances; report residual
    Oms = np.linspace(0.26, 0.36, 41)
    best = None
    for Om in Oms:
        DM_g, DH_g = distances(zq, lambda z: H_GU(z, Om))
        frac = np.concatenate([(DM_g - DM_d) / DM_d, (DH_g - DH_d) / DH_d])[1:]  # drop z=0 DM (=0)
        rms = np.sqrt(np.mean(frac ** 2))
        if best is None or rms < best[0]:
            best = (rms, Om, np.max(np.abs(frac)))
    rms_best, Om_best, maxfrac = best
    # fixed-Omega (no floating) residual for comparison
    DM_f, DH_f = distances(zq, lambda z: H_GU(z, OM_DESI))
    frac_f = np.concatenate([(DM_f - DM_d) / DM_d, (DH_f - DH_d) / DH_d])[1:]
    rms_fixed = np.sqrt(np.mean(frac_f ** 2))

    print(f"\n    DISTANCE residual (GU-theta vs DESI-preferred), over BAO redshifts 0.3<=z<=2:")
    print(f"      fixed Omega_m=0.307:   RMS frac = {rms_fixed*100:.2f}%")
    print(f"      FLOATING Omega_m:      RMS frac = {rms_best*100:.2f}%  (best Om={Om_best:.3f}, "
          f"max|frac|={maxfrac*100:.2f}%)")
    print(f"    BAO measurement precision (DESI DR2, per-tracer): ~1-2%.")

    BAO_PREC = 0.015   # ~1.5% representative
    cpl_faithful = cpl_rms < 0.025
    # the Omega_m float is only legitimate if it respects the CMB/DESI Omega_m prior
    OM_CMB, OM_CMB_SIG = OM_DESI, 0.005   # DESI+CMB Omega_m ~ 0.307 +/- ~0.005
    om_pull = abs(Om_best - OM_CMB) / OM_CMB_SIG
    # rough distance chi^2 at the CMB-required Omega_m (8 points, ~1.5% each, D_M and D_H)
    chi2_fixed = np.sum((frac_f / BAO_PREC) ** 2)
    ndf = len(frac_f)
    print(f"\n    best-fit Omega_m = {Om_best:.3f} vs CMB/DESI Omega_m = {OM_CMB:.3f}+/-{OM_CMB_SIG} "
          f"-> {om_pull:.1f} sigma  ({'CMB-EXCLUDED' if om_pull > 3 else 'CMB-allowed'})")
    print(f"    at the CMB-required Omega_m: distance residual {rms_fixed*100:.1f}% RMS across {ndf} points "
          f"vs ~1-2% BAO precision -- a REAL few-sigma tension (a crude uncorrelated chi^2 would read high; the")
    print(f"    honest reading is 'in line with the ~3-4 sigma (w0,wa) headline', NOT more-excluded than DESI's own fit).")

    check("computation ran: actual theta w(z) integrated, self-consistent distances, Omega_m floated",
          np.isfinite(rms_best))
    check("the actual theta w(z) is NEARLY CPL over z<=2 -> the non-CPL SHAPE is a MINOR lever",
          cpl_faithful, f"CPL-fit RMS {cpl_rms:.3f}")
    check("the Omega_m float that reaches consistency is CMB-EXCLUDED (not a legitimate resolution)",
          om_pull > 3, f"Om_best={Om_best:.3f} is {om_pull:.1f} sigma from the CMB Omega_m")
    check("at the CMB-required Omega_m a REAL distance tension remains (above BAO precision)",
          rms_fixed > BAO_PREC, f"fixed-Om residual {rms_fixed*100:.2f}% > {BAO_PREC*100:.1f}%")

    print("\n[verdict]  STANDS (mildly clarified, NOT rescued).")
    print(f"  Both heterodox sub-levers fail to legitimately rescue the DESI tension:")
    print(f"  (1) NON-CPL SHAPE is minor: the actual theta w(z) is nearly CPL over z<=2 (RMS {cpl_rms:.3f});")
    print(f"      the shallow evolution (wa~{waf:+.2f}) is INTRINSIC, not a projection artifact. w(z) starts")
    print(f"      at w(0)~{np.interp(0.0,z_g,w_g):+.2f} and only reaches ~{np.interp(2.0,z_g,w_g):+.2f} -- far")
    print(f"      shallower than DESI's implied evolution to wa={WA_DESI}.")
    print(f"  (2) FLOATING BACKGROUND is CMB-blocked: the distance match to {rms_best*100:.2f}% needs")
    print(f"      Omega_m={Om_best:.3f}, which is {om_pull:.1f} sigma from the CMB-pinned value -- excluded by")
    print(f"      the same DESI+CMB combination that reports the tension. At the CMB Omega_m the actual-w(z)")
    print(f"      distance residual is {rms_fixed*100:.2f}% RMS -- above BAO precision, a real offset in line with the headline.")
    print(f"  NUANCE (fair to the heterodox): the DISTANCE metric ({rms_fixed*100:.1f}% at CMB-Om) is a bit")
    print(f"  milder than the (w0,wa)-plane headline, and there IS a real Om-w degeneracy -- but respecting")
    print(f"  the CMB Omega_m prior, the tension is a genuine ~few-sigma negative, NOT a CPL artifact.")
    print("\n  HONEST CAVEATS: w(z) computed on an LCDM background (not fully self-consistent -- re-integrating")
    print("  the field on the floated background is the next tightening); f0 held fixed (floating it is the")
    print("  separate prediction-vs-fit question); DESI-CPL used as a distance proxy, not the raw BAO table +")
    print("  CMB (which pins Omega_m and would penalize the Om float). NOT a rescue -- a fair-comparison test.")

    if FAIL:
        print(f"\nFAILED: {FAIL}")
        raise SystemExit(1)
    print("\nexit 0 = fair distance comparison done; the DESI tension STANDS (non-CPL shape minor; the Omega_m")
    print("         float to consistency is CMB-excluded); mildly clarified in the distance metric, not rescued.")


if __name__ == "__main__":
    main()
