#!/usr/bin/env python3
r"""TRACK-2 (H47 declare-and-build) -- T2A: the graviton-sector NUMBERS of the
conditional theory GU-given-S.

FIREWALL (repo-ratified, two-track-persona-sweep SYNTHESIS sec 6): every output here
is a CONDITIONAL statement "X given S".  S is the declared postulate set (see the
exploration doc explorations/track2-conditional-numbers-2026-07-13.md).  Nothing in
this file asserts S.  Nothing here may be quoted as "GU predicts X" without the
given-S clause.

INGREDIENTS (repo-established only; none invented):
  * spin-2 action = Einstein + Weyl^2 (Stelle-type), TT operator box(box + m2^2)
      [H15 / H25; conditional on the soldering postulate S3 (H27: NOT forced)]
  * m2^2 = m2_eff * mu_DW^2,  m2_eff in [5/6, 5/4]  (H25, two independent methods;
      sign robust, magnitude an O(1) method band)
  * no R^2 term -> no scalar Yukawa; potential
      Phi = -(GM/r)[1 + (1/3) e^{-m2 r}]   (H10, Stelle 1978 solution of that operator)
  * alpha = 1/3 FIXED (vDVZ trace structure; not a free parameter)     [H10]
  * gamma(r) - 1 = -(2/3) e^{-m2 r} + O(e^{-2 m2 r})                   [H10]
  * mu_DW = DE scale (H36 identification) gives lambda in [60.0, 73.6] um (c_L = 3/8)
      -- ALREADY EXCLUDED by Eot-Wash/HUST at alpha = 1/3               [H50 / H51]

DISCIPLINE: published bounds are comparison-only, cited; every load-bearing number is
computed by two independent routes.  No em-dash characters anywhere.

Run: python -u tests/track2/T2A_graviton_sector_numbers.py   (exit 0 iff all PASS)
"""
from __future__ import annotations
import math
import sys

FAIL = []


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}", flush=True)
    if not ok:
        FAIL.append(name)


def log(m=""):
    print(m, flush=True)


# ===========================================================================
# Constants (CODATA / IAU; two independent routes for hbar*c).
# ===========================================================================
HBAR_C_EV_NM = 197.3269804            # eV nm  (route 1)
HBAR_JS = 1.054571817e-34             # J s    (route 2, independent constants)
C_MS = 2.99792458e8                   # m / s
EV_J = 1.602176634e-19                # J / eV
HBAR_C_EV_M_R2 = HBAR_JS * C_MS / EV_J   # eV m, route 2
AU_M = 1.495978707e11
RSUN_M = 6.957e8

# Repo-computed inputs (H25):
M2EFF_LO, M2EFF_HI = 5.0 / 6.0, 5.0 / 4.0    # the two-method band; sign robust
ALPHA = 1.0 / 3.0                            # vDVZ trace factor (H10); FIXED

# Published bounds (comparison only, cited):
CASSINI_GAMMA = 2.3e-5      # |gamma-1| < 2.3e-5, Bertotti-Iess-Tortora, Nature 425, 374 (2003)
# alpha=1 Yukawa range crossings (H50, cited): Lee 2020 (38.6 um), Tan 2020 (48 um),
# Kapner 2007 (56 um).  alpha=1/3 boundary ARGUED at ~45-52 um (H50/H51; NOT digitized).
ALPHA13_LAMBDA_MAX_UM = (45.0, 52.0)

RHO_L_QUARTER_EV = 2.3e-3   # rho_Lambda^{1/4}, observed DE scale (H50)
C_L = 3.0 / 8.0             # DeWitt coefficient, computed exact (H51)


def m2_of_mu(mu_ev, m2eff):
    return math.sqrt(m2eff) * mu_ev


def lam_um_route1(m2_ev):
    return HBAR_C_EV_NM / m2_ev / 1.0e3          # nm -> um


def lam_um_route2(m2_ev):
    return HBAR_C_EV_M_R2 / m2_ev * 1.0e6        # m -> um


def main():
    log("=" * 78)
    log("T2A -- graviton-sector numbers of the conditional theory GU-given-S")
    log("      (every line below is 'given S'; S is declared, never asserted)")
    log("=" * 78)

    # -----------------------------------------------------------------------
    # GUARD: the two hbar*c routes agree (unit-conversion bug guard).
    # -----------------------------------------------------------------------
    hc1 = HBAR_C_EV_NM * 1e-9      # eV m
    rel = abs(hc1 - HBAR_C_EV_M_R2) / hc1
    check("two independent hbar*c routes agree to < 1e-8", rel < 1e-8, f"rel={rel:.1e}")

    # -----------------------------------------------------------------------
    # PART 1 -- the ghost mass and Yukawa range as functions of mu_DW.
    # m2 = sqrt(m2_eff) mu_DW ;  V(r) = -(GM/r)[1 + (1/3) e^{-r/lambda}] ; alpha = 1/3.
    # -----------------------------------------------------------------------
    log("\nPART 1 -- m2(mu_DW) and Yukawa range lambda(mu_DW); strength alpha = 1/3 FIXED")
    log("  m2 = sqrt(m2_eff) * mu_DW,  m2_eff in [5/6, 5/4] (H25 band)")
    log(f"  {'mu_DW':>12} | {'m2 band [eV]':>28} | {'lambda band':>26}")
    rows = [
        ("2.3 meV (=DE scale, H36)", 2.3e-3),
        ("3.8 meV", 3.8e-3),
        ("1 eV", 1.0),
        ("1 GeV", 1.0e9),
        ("M_Pl = 1.22e28 eV", 1.22e28),
    ]
    for label, mu in rows:
        m2a, m2b = m2_of_mu(mu, M2EFF_LO), m2_of_mu(mu, M2EFF_HI)
        la, lb = lam_um_route1(m2b), lam_um_route1(m2a)   # shortest..longest
        if lb > 1.0e-3:
            lam_str = f"[{la:9.3g}, {lb:9.3g}] um"
        else:
            lam_str = f"[{la * 1e-6:9.3g}, {lb * 1e-6:9.3g}] m"
        log(f"  {label:>25} | [{m2a:10.3e}, {m2b:10.3e}] | {lam_str}")

    # route-2 cross-check of the range at one load-bearing point
    mu = RHO_L_QUARTER_EV
    l1 = lam_um_route1(m2_of_mu(mu, M2EFF_LO))
    l2 = lam_um_route2(m2_of_mu(mu, M2EFF_LO))
    check("lambda unit conversion two routes agree (mu_DW = 2.3 meV, m2_eff = 5/6)",
          abs(l1 - l2) / l1 < 1e-8, f"{l1:.4f} vs {l2:.4f} um")
    check("reproduces H50 c_L=1 band [76.74, 93.98] um at mu_DW = 2.3 meV",
          abs(lam_um_route1(m2_of_mu(mu, M2EFF_HI)) - 76.74) < 0.05
          and abs(lam_um_route1(m2_of_mu(mu, M2EFF_LO)) - 93.98) < 0.05,
          f"[{lam_um_route1(m2_of_mu(mu, M2EFF_HI)):.2f}, "
          f"{lam_um_route1(m2_of_mu(mu, M2EFF_LO)):.2f}] um")

    # -----------------------------------------------------------------------
    # PART 2 -- PPN gamma profile and the Cassini floor on mu_DW.
    # gamma - 1 = -(2/3) e^{-m2 r}  (H10).  Bound |gamma-1| < 2.3e-5 (Cassini).
    # Route 1: closed form  m2 r > ln((2/3)/2.3e-5).  Route 2: bisection.
    # -----------------------------------------------------------------------
    log("\nPART 2 -- PPN gamma(r) profile + Cassini floor on mu_DW")
    x_r1 = math.log((2.0 / 3.0) / CASSINI_GAMMA)
    lo, hi = 1.0, 30.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if (2.0 / 3.0) * math.exp(-mid) > CASSINI_GAMMA:
            lo = mid
        else:
            hi = mid
    x_r2 = 0.5 * (lo + hi)
    check("Cassini threshold m2*r two routes agree (closed form vs bisection)",
          abs(x_r1 - x_r2) < 1e-9, f"{x_r1:.6f} vs {x_r2:.6f}")
    log(f"  |gamma-1| < {CASSINI_GAMMA:.1e}  =>  m2 r > {x_r1:.3f}")
    for rl, rm in (("1 AU", AU_M), ("1.6 R_sun", 1.6 * RSUN_M)):
        m2_floor_invm = x_r1 / rm
        m2_floor_ev = m2_floor_invm * HBAR_C_EV_M_R2
        mu_floor_ev = m2_floor_ev / math.sqrt(M2EFF_LO)   # weakest m2_eff
        log(f"  r = {rl:>9}: m2 > {m2_floor_ev:.3e} eV  =>  mu_DW > {mu_floor_ev:.3e} eV")
        if rl == "1 AU":
            check("Cassini 1 AU floor reproduces H10 (~1.4e-17 eV on m2, ~1.5e-17 eV on mu_DW)",
                  abs(m2_floor_ev - 1.4e-17) < 0.2e-17 and abs(mu_floor_ev - 1.5e-17) < 0.2e-17,
                  f"m2>{m2_floor_ev:.2e}, mu>{mu_floor_ev:.2e}")
    log("  gamma(r)-1 sample (given-S profile), mu_DW at the sub-mm floor 3.4e-3 eV:")
    mu_floor = 3.4e-3
    for rl, rm in (("100 um", 100e-6), ("1 mm", 1e-3), ("1 m", 1.0)):
        m2_invm = m2_of_mu(mu_floor, M2EFF_LO) / HBAR_C_EV_M_R2
        g = -(2.0 / 3.0) * math.exp(-m2_invm * rm)
        log(f"    r = {rl:>7}: gamma-1 = {g:+.3e}")

    # -----------------------------------------------------------------------
    # PART 3 -- the sub-mm channel: H36 point EXCLUDED; the allowed mu_DW window.
    # -----------------------------------------------------------------------
    log("\nPART 3 -- sub-mm gravity: the H36 point (mu_DW = DE scale) and the allowed window")
    mu_h36 = RHO_L_QUARTER_EV / C_L ** 0.25
    lam_h36 = (lam_um_route1(m2_of_mu(mu_h36, M2EFF_HI)),
               lam_um_route1(m2_of_mu(mu_h36, M2EFF_LO)))
    log(f"  H36 + c_L = 3/8 (H51): mu_DW = (rho_L/c_L)^(1/4) = {mu_h36 * 1e3:.3f} meV")
    log(f"  predicted Yukawa: alpha = 1/3, lambda in [{lam_h36[0]:.1f}, {lam_h36[1]:.1f}] um")
    check("reproduces H51 band [60.0, 73.6] um (mu_DW = DE scale, c_L = 3/8)",
          abs(lam_h36[0] - 60.0) < 0.1 and abs(lam_h36[1] - 73.6) < 0.1,
          f"[{lam_h36[0]:.2f}, {lam_h36[1]:.2f}] um")
    log("  STATUS: EXCLUDED at alpha = 1/3 (H50/H51 vs Lee 2020 / Tan 2020 / Kapner 2007;")
    log("  the alpha=1/3 boundary is ARGUED at ~45-52 um, margin O(1)).  So the conditional")
    log("  theory does NOT adopt H36; mu_DW stays a free declared scale.")

    log("\n  ALLOWED mu_DW window (lower edge from the argued alpha=1/3 boundary):")
    floors = []
    for lam_max in ALPHA13_LAMBDA_MAX_UM:
        m2_min = HBAR_C_EV_NM / (lam_max * 1e3)          # eV
        for m2eff in (M2EFF_HI, M2EFF_LO):
            floors.append(m2_min / math.sqrt(m2eff))
        log(f"    lambda_max = {lam_max:.0f} um -> m2 >= {m2_min * 1e3:.3f} meV -> "
            f"mu_DW >= [{m2_min / math.sqrt(M2EFF_HI) * 1e3:.2f}, "
            f"{m2_min / math.sqrt(M2EFF_LO) * 1e3:.2f}] meV  (m2_eff = 5/4 .. 5/6)")
    mu_floor_weak = min(floors)   # weakest defensible floor
    mu_floor_strong = max(floors)
    log(f"  => lower edge: mu_DW >= ~{mu_floor_weak * 1e3:.1f} meV (weakest corner) to "
        f"~{mu_floor_strong * 1e3:.1f} meV (strictest);")
    log("     (H50 quoted an argued ~3.0-3.6 meV; the spread is the un-digitized boundary +")
    log("      the m2_eff method band.  BOUND grade, boundary argued not digitized.)")
    log("  => upper edge: NONE experimental; EFT validity only (up to ~M_Pl; the natural")
    log("     H24 default mu_DW ~ M_Pl sits inside the window, 30+ orders above the floor).")
    check("DE-scale mu_DW (2.94 meV incl. c_L, and raw 2.3 meV) sits BELOW the strict floor "
          "(H36 point excluded, window honest)",
          mu_h36 < mu_floor_strong and RHO_L_QUARTER_EV < mu_floor_weak,
          f"mu_h36={mu_h36 * 1e3:.2f} meV vs floors [{mu_floor_weak * 1e3:.2f}, "
          f"{mu_floor_strong * 1e3:.2f}] meV")
    check("Cassini floor is ~14 orders WEAKER than the sub-mm floor (sub-mm is binding)",
          1.5e-17 < 1e-13 * mu_floor_weak, "1.5e-17 eV << meV")

    # -----------------------------------------------------------------------
    # PART 4 -- the GW channel (LIGO): dispersion / extra polarizations.
    # The massless graviton pole is exactly massless (H51: TT s^0 coefficient = 0
    # EXACTLY) -> luminal propagation, standard 2 tensor polarizations.  The massive
    # spin-2 companion can only be radiated when omega > m2.
    # -----------------------------------------------------------------------
    log("\nPART 4 -- GW channel (LIGO band)")
    f_max = 2048.0     # Hz, upper edge of the sensitive band
    omega_max_ev = 2.0 * math.pi * f_max * 6.582119569e-16   # hbar[eV s] * omega
    mu_thresh = omega_max_ev / math.sqrt(M2EFF_LO)
    lam_thresh_m = HBAR_C_EV_M_R2 / omega_max_ev
    log(f"  massless pole: EXACTLY massless (H51, TT s^0 = 0) -> zero dispersion, luminal,")
    log(f"  2 tensor polarizations only.  [PREDICTION-given-S]")
    log(f"  massive spin-2 radiated only if m2 < hbar*omega: at f = {f_max:.0f} Hz,")
    log(f"  hbar*omega = {omega_max_ev:.2e} eV  =>  requires mu_DW < {mu_thresh:.2e} eV")
    log(f"  (equivalent Yukawa range {lam_thresh_m / 1e3:.1f} km).")
    ratio = mu_floor_weak / mu_thresh
    log(f"  The allowed window floor ({mu_floor_weak * 1e3:.1f} meV) exceeds the LIGO-excitable")
    log(f"  ceiling by a factor {ratio:.1e} (~{math.log10(ratio):.0f} orders).")
    check("LIGO-excitable region (mu_DW < ~1e-11 eV) lies entirely BELOW the allowed window "
          "floor -> given S, NO GW dispersion / extra polarizations at LIGO",
          mu_thresh < mu_floor_weak * 1e-6, f"threshold {mu_thresh:.1e} eV")
    log("  => given S (with mu_DW in the allowed window), GU-given-S predicts LIGO sees")
    log("     EXACT GR radiation.  A confirmed GW dispersion, extra polarization, or")
    log("     sub-luminal tensor mode would FALSIFY GU-given-S.  LIGO's graviton-mass")
    log("     bound (~1.3e-23 eV, GWTC-3) applies to the MASSLESS pole, which is exactly")
    log("     massless here: satisfied identically, no mu_DW constraint.  [BOUND: none new]")

    # -----------------------------------------------------------------------
    log("\n" + "-" * 78)
    if FAIL:
        log(f"FAILED: {FAIL}")
        sys.exit(1)
    log("exit 0 = T2A recorded.  Graviton-sector numbers of GU-given-S emitted:")
    log("  alpha = 1/3 (fixed), lambda(mu_DW) = hbar c / (sqrt(m2_eff) mu_DW),")
    log("  gamma-1 = -(2/3) e^{-m2 r}; allowed window mu_DW >= ~3.4 meV (argued edge),")
    log("  no experimental upper edge; H36 point (DE scale) EXCLUDED; LIGO channel:")
    log("  exact GR predicted inside the window.")
    sys.exit(0)


if __name__ == "__main__":
    main()
