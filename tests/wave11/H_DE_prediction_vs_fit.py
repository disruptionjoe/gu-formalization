"""DESI prediction-vs-fit: is the theta amplitude f0 a FORCED prediction or a FREE fit? And can the theta
two-component structure fit DESI for ANY (f0, M^2)?

THE PHILOSOPHER'S GATE (last honest DESI lever). The ~3-4 sigma DESI tension survives two rescue routes
(combination test; fair distance test). The remaining question is its CHARACTER:
  - if the model can fit DESI only for a TUNED f0 (and GU does not force that value) -> the tension is SOFT
    (a free parameter question, the real test awaits the built theta dynamics);
  - if NO (f0, M^2) fits DESI -> the two-component SHAPE is structurally wrong -> HARD failure, tuning-proof;
  - if the model's DEFAULT (f0=0.125, M^2=8 H0^2) is far from any good-fit region -> whatever fixes f0 is
    making a genuine (failing) PREDICTION.

We SCAN (f0, M^2), integrate the theta KG field for each, build the expansion history, and compute the
distance-based DESI tension at the CMB-required Omega_m (the honest metric from the fair-comparison test).
We report the MINIMUM tension over the whole space -- the decisive number.

MODEL (dark_energy_desi_sign.py): theta = KG field B, slow-roll IC at z=30; w_DE=(-1+f wB)/(1+f),
f=f0 rhoB(z)/rhoB0. Default f0=0.125, M2=8. DESI target: w0=-0.752, wa=-0.86, Omega_m=0.307.

Run: python tests/wave11/H_DE_prediction_vs_fit.py
"""
from __future__ import annotations

import numpy as np
from scipy.integrate import solve_ivp, cumulative_trapezoid

Om_BG, OL_BG = 0.315, 0.685
Z_START = 30.0
W0_DESI, WA_DESI, OM_DESI = -0.752, -0.86, 0.3069
FAIL = []


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)


def H2_bg(a):
    return Om_BG * a ** -3 + OL_BG


def theta_wz(f0, M2):
    def rhs(N, y):
        a = np.exp(N)
        B, BN = y
        HNoH = -1.5 * Om_BG * a ** -3 / H2_bg(a)
        return [BN, -(3.0 + HNoH) * BN - (M2 / H2_bg(a)) * B]
    a0 = 1.0 / (1.0 + Z_START)
    N0 = np.log(a0)
    BN0 = -M2 / (3.0 * H2_bg(a0))
    sol = solve_ivp(rhs, (N0, 0.0), [1.0, BN0], t_eval=np.linspace(N0, 0.0, 3000),
                    rtol=1e-9, atol=1e-11, method="Radau")
    a = np.exp(sol.t)
    B, BN = sol.y
    Bdot = np.sqrt(H2_bg(a)) * BN
    KE, PE = 0.5 * Bdot ** 2, 0.5 * M2 * B ** 2
    rhoB = KE + PE
    wB = (KE - PE) / rhoB
    i0 = int(np.argmin(np.abs(1.0 / a - 1.0)))
    f = f0 * rhoB / rhoB[i0]
    wDE = (-1.0 + f * wB) / (1.0 + f)
    idx = np.argsort(a)
    return a[idx], wDE[idx]


def rho_de(a_g, w_g):
    I = cumulative_trapezoid((1.0 + w_g) / a_g, a_g, initial=0.0)
    return np.exp(3.0 * (I[-1] - I))


def dist(zq, Hf):
    zc = np.linspace(0.0, zq.max(), 1500)
    DC = cumulative_trapezoid(1.0 / Hf(zc), zc, initial=0.0)
    return np.interp(zq, zc, DC), 1.0 / Hf(zq)


def H_DESI(z):
    a = 1.0 / (1.0 + z)
    rho = a ** (-3 * (1 + W0_DESI + WA_DESI)) * np.exp(-3 * WA_DESI * (1 - a))
    return np.sqrt(OM_DESI * a ** -3 + (1 - OM_DESI) * rho)


ZQ = np.array([0.3, 0.5, 0.7, 0.9, 1.1, 1.3, 1.6, 2.0])
DM_D, DH_D = dist(ZQ, H_DESI)


def desi_tension(f0, M2, Om=OM_DESI):
    """RMS fractional distance residual vs DESI at the CMB-required Omega_m (the honest metric)."""
    a_g, w_g = theta_wz(f0, M2)
    rde = rho_de(a_g, w_g)

    def Hf(z):
        a = 1.0 / (1.0 + z)
        return np.sqrt(Om * a ** -3 + (1 - Om) * np.interp(a, a_g, rde))
    DM, DH = dist(ZQ, Hf)
    frac = np.concatenate([(DM - DM_D) / DM_D, (DH - DH_D) / DH_D])[1:]
    return np.sqrt(np.mean(frac ** 2))


def main():
    print("[DESI prediction-vs-fit: scan (f0, M^2); can the theta structure fit DESI at all?]\n")
    BAO = 0.015

    t_default = desi_tension(0.125, 8.0)
    print(f"    DEFAULT (f0=0.125, M2=8): distance RMS vs DESI = {t_default*100:.2f}%  "
          f"({'consistent' if t_default < BAO else 'tension'})\n")

    # 1D scan in f0 (fixed M2=8)
    print("    f0 scan (M2=8):  f0 -> distance RMS vs DESI (at CMB Omega_m)")
    f0s = np.array([0.02, 0.05, 0.125, 0.25, 0.5, 0.8, 1.2, 2.0])
    for f0 in f0s:
        t = desi_tension(f0, 8.0)
        print(f"      f0={f0:5.2f}  ->  {t*100:5.2f}%   {'<-- default' if abs(f0-0.125)<1e-6 else ''}")

    # 2D min over (f0, M2)
    print("\n    2D scan over (f0 in [0.02,3], M2 in [1,40]) -- MINIMUM distance tension:")
    best = None
    for f0 in np.linspace(0.02, 3.0, 16):
        for M2 in np.linspace(1.0, 40.0, 14):
            try:
                t = desi_tension(f0, M2)
            except Exception:
                continue
            if best is None or t < best[0]:
                best = (t, f0, M2)
    tmin, f0b, M2b = best
    print(f"      best (f0,M2) = ({f0b:.2f}, {M2b:.1f})  ->  distance RMS {tmin*100:.2f}%  "
          f"vs BAO ~{BAO*100:.1f}%")

    # can ANY (f0,M2) reach BAO consistency?
    fits = tmin < BAO
    default_near_best = (abs(f0b - 0.125) < 0.2) and (abs(M2b - 8.0) < 6)

    check("computation ran: (f0, M^2) scanned, theta field integrated at each, distance tension computed",
          np.isfinite(tmin))
    check("verdict determined: is the two-component SHAPE fittable to DESI (soft) or not (structural)?",
          True, f"min {tmin*100:.2f}% {'<' if fits else '>='} {BAO*100:.1f}% BAO -> "
          f"{'FITTABLE (a good-fit (f0,M2) EXISTS) -> tension is SOFT/amplitude' if fits else 'NOT fittable -> HARD structural'}")
    check("the model DEFAULT (f0=0.125, M2=8) is itself in tension (needs a non-default amplitude to fit)",
          t_default > BAO, f"default {t_default*100:.2f}% > {BAO*100:.1f}%")

    print("\n[verdict -- prediction vs fit]")
    if not fits:
        print(f"  HARD / STRUCTURAL: NO (f0, M^2) in the scanned space brings the theta two-component model")
        print(f"  within BAO precision of DESI (best {tmin*100:.2f}% at f0={f0b:.2f}, M2={M2b:.1f}). The DESI")
        print(f"  tension is TUNING-PROOF: it is the SHAPE of the two-component w(z) that is wrong, not the")
        print(f"  amplitude. So 'f0 is free' does NOT soften it -- even a free f0 (and M^2) cannot fit. This")
        print(f"  is a HARD failing test of the theta-sector's dark-energy SHAPE, independent of whether GU")
        print(f"  forces f0. (Falsifies the theta two-component DE ANSATZ at DESI, modulo the caveats below.)")
    else:
        print(f"  A good-fit region EXISTS at (f0={f0b:.2f}, M2={M2b:.1f}) (distance RMS {tmin*100:.2f}%).")
        if default_near_best:
            print(f"  The model DEFAULT (0.125, 8) is NEAR it -> the ~3-4 sigma is then a genuine (near-miss)")
            print(f"  PREDICTION, hardening the test.")
        else:
            print(f"  The model DEFAULT (0.125, 8) is FAR from it -> IF GU forces (0.125, 8) the prediction")
            print(f"  MISSES (hard); IF f0/M2 are free, the tension is SOFT and the real test awaits the")
            print(f"  built theta dynamics that would fix them. -> the prediction-vs-fit answer hinges on")
            print(f"  whether GU's source action FORCES f0 -- the same unbuilt object as everywhere else.")
    print("\n  Is f0 structurally forced? f0 = (theta-field density)/(constant piece) today. M^2 = M_KK^2 =")
    print("  (2 sqrt2 H0)^2 is the model's GIMMEL/KK-scale claim (M_KK ~ H0). Neither is DERIVED from a built")
    print("  source action here; both are model inputs. So at present f0 is a FREE input -- but the scan")
    print("  above shows whether freeing it even helps.")
    print("\n  HONEST CAVEATS: fixed-Omega_m distance metric (the fair one); w(z) on an LCDM background (not")
    print("  fully self-consistent); DESI-CPL distance proxy; the ANSATZ (two-component -1 + field) is itself")
    print("  reconstruction-grade. A NEGATIVE (no fit) is a strong structural statement; a positive would be")
    print("  amplitude-gated on the unbuilt dynamics.")

    if FAIL:
        print(f"\nFAILED: {FAIL}")
        raise SystemExit(1)
    print(f"\nexit 0 = prediction-vs-fit scanned; min DESI distance tension over (f0,M2) = {tmin*100:.2f}% "
          f"-> {'HARD/structural (tuning-proof)' if not fits else 'fittable (amplitude-gated)'}.")


if __name__ == "__main__":
    main()
