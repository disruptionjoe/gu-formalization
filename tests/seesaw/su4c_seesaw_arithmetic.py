#!/usr/bin/env python3
"""
M-H3 / panel U5b -- SU(4)_c seesaw retrodiction: the arithmetic, done honestly.

POSIT / RETRODICTION support script. Standard GUT arithmetic on the verified
Pati-Salam group-theory chain (lab/active-research/pati-salam-chain-verification.md).
NO GU derivation of M_PS, the Lambda^5 VEV, or any Yukawa texture is performed
or implied here. Owner document:
explorations/su4c-seesaw-retrodiction-2026-08-03.md

CLAIM COMPUTED
    Under SU(4)_c (quark-lepton unification), the third-generation Dirac
    neutrino mass equals the top mass at the Pati-Salam scale:
        m_D^nu(M_PS) = m_t(M_PS).
    With the type-I seesaw  m_nu3 ~= (m_D^nu)^2 / M_R  and the observed
    atmospheric scale m_nu3 ~= sqrt(Dm2_atm) ~= 0.050 eV, retrodict M_R.

    (a) NAIVE:  m_t = 173 GeV (pole, no running)  ->  M_R ~= 6.0e14 GeV.
    (b) HONEST: one-loop SM MS-bar running of y_t up to mu* = 1e14 GeV
        (m_t(mu*) ~ 80-100 GeV) plus the one-loop flavor-universal running of
        the Weinberg operator kappa between mu* and the top scale
        ->  M_R ~= 1e14 GeV.
    The claimed result is the ORDER OF MAGNITUDE band  M_R ~ 1e14 .. 6e14 GeV,
    inside the canonical GUT-seesaw window [1e13, 1e16] and ~5 orders below
    M_Planck.

STANDARD INPUTS (all measured / textbook; sources named in the owner doc)
    - MS-bar couplings at mu0 = 173.34 GeV (Buttazzo et al., arXiv:1307.3536):
      gY = 0.35830, g2 = 0.64779, g3 = 1.1666, y_t = 0.93690, lambda = 0.12604.
    - v = 246.22 GeV;  m_t(mu) = y_t(mu) * v / sqrt(2).
    - Dm2_atm = 2.507e-3 eV^2 (NuFIT-class global fit, normal ordering)
      -> m_nu3 = 5.007e-2 eV = 5.007e-11 GeV.
    - M_Planck = 1.221e19 GeV.

ONE-LOOP SM RGEs (t = ln mu, MS-bar, SM hypercharge normalization):
    16 pi^2 dgY/dt = (41/6)  gY^3
    16 pi^2 dg2/dt = (-19/6) g2^3
    16 pi^2 dg3/dt = (-7)    g3^3
    16 pi^2 dy_t/dt = y_t (9/2 y_t^2 - 17/12 gY^2 - 9/4 g2^2 - 8 g3^2)
    16 pi^2 dlam/dt = 24 lam^2 - 6 y_t^4 + (3/8)(2 g2^4 + (g2^2+gY^2)^2)
                      + (12 y_t^2 - 9 g2^2 - 3 gY^2) lam
    16 pi^2 dln(kappa)/dt = 6 y_t^2 - 3 g2^2 + lam       [flavor-universal part;
                             y_tau and flavor structure neglected -- band, not headline]

DISCIPLINE
    - Positive control FIRST (P-M7): RK4 vs the closed-form 1-loop g3 solution.
    - Non-vacuity control: the same formula applied to the FIRST generation
      (m_up ~ 2.16e-3 GeV, m_nu1 <= m_nu2 scale) lands ~9 orders BELOW the
      canonical window -- the window test can fail, so passing it is not vacuous.
    - Failure paths are real: every check asserts; nonzero exit on failure (P-C3).
"""

import math
import sys

# ----------------------------- constants ------------------------------------
PI2_16 = 16.0 * math.pi ** 2
V_HIGGS = 246.22            # GeV
MU0 = 173.34                # GeV, matching the Buttazzo et al. input point
MU_STAR = 1.0e14            # GeV, evaluation scale (~ retrodicted M_R; see note)
M_PLANCK = 1.221e19         # GeV
M_NU3 = 5.007e-11           # GeV  (= sqrt(2.507e-3) eV)
M_T_POLE = 173.0            # GeV  (naive input named by the register M-H3 row)
M_UP_2GEV = 2.16e-3         # GeV  (PDG m_u at 2 GeV; non-vacuity control only)
CANON_WINDOW = (1.0e13, 1.0e16)   # canonical GUT-seesaw window (decades 13..16)

# MS-bar initial conditions at MU0 (Buttazzo et al. 1307.3536, central values)
G_Y0, G2_0, G3_0 = 0.35830, 0.64779, 1.1666
Y_T0, LAM0 = 0.93690, 0.12604

FAILURES = []


def check(name, ok, detail=""):
    tag = "OK  " if ok else "FAIL"
    print(f"[{tag}] {name}" + (f"  -- {detail}" if detail else ""))
    if not ok:
        FAILURES.append(name)


# ----------------------------- RGE system -----------------------------------
def derivs(state):
    gY, g2, g3, yt, lam, lnk = state
    dgY = (41.0 / 6.0) * gY ** 3 / PI2_16
    dg2 = (-19.0 / 6.0) * g2 ** 3 / PI2_16
    dg3 = (-7.0) * g3 ** 3 / PI2_16
    dyt = yt * (4.5 * yt ** 2 - (17.0 / 12.0) * gY ** 2
                - 2.25 * g2 ** 2 - 8.0 * g3 ** 2) / PI2_16
    dlam = (24.0 * lam ** 2 - 6.0 * yt ** 4
            + 0.375 * (2.0 * g2 ** 4 + (g2 ** 2 + gY ** 2) ** 2)
            + (12.0 * yt ** 2 - 9.0 * g2 ** 2 - 3.0 * gY ** 2) * lam) / PI2_16
    dlnk = (6.0 * yt ** 2 - 3.0 * g2 ** 2 + lam) / PI2_16
    return (dgY, dg2, dg3, dyt, dlam, dlnk)


def rk4_run(mu_from, mu_to, state, n_steps=4000):
    t0, t1 = math.log(mu_from), math.log(mu_to)
    h = (t1 - t0) / n_steps
    s = list(state)
    for _ in range(n_steps):
        k1 = derivs(s)
        k2 = derivs([s[i] + 0.5 * h * k1[i] for i in range(6)])
        k3 = derivs([s[i] + 0.5 * h * k2[i] for i in range(6)])
        k4 = derivs([s[i] + h * k3[i] for i in range(6)])
        s = [s[i] + (h / 6.0) * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i])
             for i in range(6)]
    return s


def main():
    print("=" * 78)
    print("M-H3  SU(4)_c seesaw retrodiction arithmetic  (posit-support; standard SM RG)")
    print("=" * 78)

    # ---- positive control FIRST: RK4 vs closed-form 1-loop g3 running ------
    # dg3/dt = b g3^3/16pi^2  =>  g3(mu)^2 = g3o^2 / (1 - 2 b g3o^2 ln(mu/mu0)/16pi^2)
    b3 = -7.0
    s_ctrl = rk4_run(MU0, MU_STAR, [G_Y0, G2_0, G3_0, Y_T0, LAM0, 0.0])
    g3_closed = math.sqrt(G3_0 ** 2 / (1.0 - 2.0 * b3 * G3_0 ** 2
                                       * math.log(MU_STAR / MU0) / PI2_16))
    rel = abs(s_ctrl[2] - g3_closed) / g3_closed
    check("positive control: RK4 g3(1e14) vs closed form (rel err < 1e-6)",
          rel < 1e-6, f"rk4={s_ctrl[2]:.6f} closed={g3_closed:.6f} rel={rel:.1e}")

    # ---- (a) naive arithmetic ---------------------------------------------
    mr_naive = M_T_POLE ** 2 / M_NU3
    print(f"\n(a) NAIVE:  M_R = m_t^2 / m_nu3 = {M_T_POLE:.0f}^2 / {M_NU3:.3e} GeV")
    print(f"          = {mr_naive:.3e} GeV   (log10 = {math.log10(mr_naive):.2f})")
    check("naive M_R in [5.5e14, 6.5e14] GeV (register row: 5.98e14)",
          5.5e14 < mr_naive < 6.5e14, f"{mr_naive:.3e}")

    # ---- (b) honest band: run y_t (and kappa) to mu* = 1e14 GeV -----------
    gY, g2, g3, yt, lam, lnk = rk4_run(MU0, MU_STAR,
                                       [G_Y0, G2_0, G3_0, Y_T0, LAM0, 0.0])
    m_t_star = yt * V_HIGGS / math.sqrt(2.0)
    r_kappa = math.exp(lnk)          # kappa(mu*) / kappa(mu0)  ( > 1 )
    print(f"\n(b) ONE-LOOP RUN to mu* = 1e14 GeV:")
    print(f"    y_t(mu*) = {yt:.4f}   ->  m_t(mu*) = {m_t_star:.1f} GeV")
    print(f"    gY,g2,g3(mu*) = {gY:.4f}, {g2:.4f}, {g3:.4f}   lambda(mu*) = {lam:.4f}")
    print(f"    Weinberg-operator factor r_kappa = kappa(mu*)/kappa(mu0) = {r_kappa:.3f}")
    check("m_t(1e14 GeV) in the stated 80-100 GeV band (+/- 10 GeV slack)",
          70.0 < m_t_star < 110.0, f"{m_t_star:.1f} GeV")
    check("r_kappa in [1.1, 1.6] (literature-standard SM size)",
          1.1 < r_kappa < 1.6, f"{r_kappa:.3f}")

    # seesaw matching at mu*: m_nu3(mu*) = r_kappa * m_nu3(low)
    mr_run_mt_only = m_t_star ** 2 / M_NU3
    mr_full = m_t_star ** 2 / (M_NU3 * r_kappa)
    print(f"\n    M_R (run m_t, unrun kappa)  = {mr_run_mt_only:.3e} GeV"
          f"   (log10 = {math.log10(mr_run_mt_only):.2f})")
    print(f"    M_R (run m_t AND kappa)     = {mr_full:.3e} GeV"
          f"   (log10 = {math.log10(mr_full):.2f})")

    # self-consistency: mu* was 1e14; re-evaluate at mu = M_R(full) once
    s2 = rk4_run(MU0, mr_full, [G_Y0, G2_0, G3_0, Y_T0, LAM0, 0.0])
    m_t_2 = s2[3] * V_HIGGS / math.sqrt(2.0)
    mr_iter = m_t_2 ** 2 / (M_NU3 * math.exp(s2[5]))
    drift = abs(math.log10(mr_iter) - math.log10(mr_full))
    print(f"    self-consistency iterate at mu = M_R: M_R -> {mr_iter:.3e} GeV"
          f"  (log10 drift {drift:.3f})")
    check("fixed-point drift < 0.15 decades (log-weak scale dependence)",
          drift < 0.15, f"{drift:.3f} decades")

    # ---- the band and the window checks ------------------------------------
    band_lo, band_hi = min(mr_full, mr_iter), mr_naive
    print(f"\nBAND:  M_R = {band_lo:.2e} .. {band_hi:.2e} GeV"
          f"   (log10 = {math.log10(band_lo):.2f} .. {math.log10(band_hi):.2f})")
    check("whole band inside canonical GUT-seesaw window [1e13, 1e16] GeV",
          CANON_WINDOW[0] < band_lo and band_hi < CANON_WINDOW[1],
          f"[{band_lo:.2e}, {band_hi:.2e}] vs {CANON_WINDOW}")
    check("whole band below M_Planck (by ~5 decades)",
          band_hi < M_PLANCK,
          f"log10(M_Planck/M_R_hi) = {math.log10(M_PLANCK / band_hi):.1f}")
    check("seesaw hierarchy consistent: M_R >> m_D (ratio > 1e10)",
          band_lo / m_t_star > 1e10, f"ratio = {band_lo / m_t_star:.2e}")

    # ---- non-vacuity control: first generation misses the window by ~9 dec -
    mr_gen1 = M_UP_2GEV ** 2 / M_NU3   # m_nu scale kept at atmospheric for max leniency
    print(f"\nNON-VACUITY CONTROL: same formula, first generation (m_u = {M_UP_2GEV} GeV):")
    print(f"    M_R(gen 1) = {mr_gen1:.2e} GeV  (log10 = {math.log10(mr_gen1):.1f})")
    check("gen-1 control lands OUTSIDE the canonical window (test can fail)",
          not (CANON_WINDOW[0] < mr_gen1 < CANON_WINDOW[1]), f"{mr_gen1:.2e}")

    # ------------------------------------------------------------------------
    print("\n" + "=" * 78)
    if FAILURES:
        print(f"VERDICT: {len(FAILURES)} CHECK(S) FAILED: {FAILURES}")
        print("=" * 78)
        sys.exit(1)
    print("VERDICT: all checks pass. Retrodicted band M_R ~ 1e14 .. 6e14 GeV,")
    print("inside the canonical GUT-seesaw window, ~5 decades below M_Planck.")
    print("This is POSIT-SUPPORT arithmetic, not a GU derivation of any scale.")
    print("=" * 78)
    sys.exit(0)


if __name__ == "__main__":
    main()
