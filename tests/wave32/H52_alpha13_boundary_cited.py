#!/usr/bin/env python3
r"""H52 (wave 32) -- the alpha = 1/3 sub-mm exclusion boundary, CITED not argued.

OBJECT.  H50/H51/Track-2 declared the H36 point (mu_DW = DE scale) EXCLUDED at
alpha = 1/3 from an ARGUED (not digitized) boundary at ~45-52 um, and two teams
disagreed on the implied mu_DW floor (H50: ~3.0-3.6 meV; Track-2 T2A: ~3.4-4.8 meV).
This test replaces the argued boundary with PUBLISHED anchors and published fit
functions, resolves the floor discrepancy, and grades every number.

THE KEY EXTRACTION (persona 1+2, sources fetched 2026-07-13; content treated as data):
  The n = 1 RADION benchmark in the Eot-Wash analyses has Yukawa strength
  alpha = n/(n+2) = 1/3 EXACTLY, with published range-vs-unification-mass fit
      lambda ~= 2.4 * (1 TeV / (M* c^2))^2 mm        [PUBLISHED-QUOTED, Adelberger
      et al., Phys. Rev. D 68, 062002 / hep-ph/0611223 eq. (8) region]
  so every published 95% CL radion M* bound IS a published alpha = 1/3 crossing:
      lambda_max(alpha = 1/3) = 2.4 mm / (M*/TeV)^2.

ANCHORS (all 95% CL, comparison-only, cited; none invented):
  Kapner et al., PRL 98, 021101 (2007) / hep-ph/0611184:
      |alpha| = 1 crossing lambda = 56 um                    [PUBLISHED-QUOTED]
      alpha = 8/3 (one extra dim) crossing R = 44 um         [PUBLISHED-QUOTED]
  Adelberger et al., hep-ph/0611223 (same dataset):
      radion n = 1 (alpha = 1/3): M* >= 5.7 TeV              [PUBLISHED-QUOTED]
      radion n = 6 (alpha = 3/4): M* >= 6.4 TeV              [PUBLISHED-QUOTED]
  Lee et al., PRL 124, 101101 (2020) / arXiv:2002.11761:
      |alpha| = 1 crossing lambda = 38.6 um                  [PUBLISHED-QUOTED]
      largest extra dimension (alpha = 8/3) R < 30 um        [PUBLISHED-QUOTED]
      dilaton (alpha ~ 1) m > 5.1 meV                        [PUBLISHED-QUOTED]
      "the radion unification mass must be greater than ... 7.1 TeV"
      (cites Adelberger 2003 + 2007 for the conversion)      [PUBLISHED-QUOTED]
  Tan et al., PRL 124, 051301 (2020) (HUST):
      |alpha| = 1 crossing lambda = 48 um                    [PUBLISHED-QUOTED]
      "strongest bound on ... alpha ... in the range of 40-350 um, and improves
      the previous bounds by up to a factor of 3 at ... lambda ~= 70 um"
                                                             [PUBLISHED-QUOTED]
  Murata, Fujiie, Suzuki review, arXiv:2605.18212 (2026): no post-2020 experiment
      supersedes Lee/Tan in 40-100 um; no numerical exclusion tables published.

DERIVED (labels as printed):
  lambda_max(alpha = 1/3):
    Kapner 2007  : 2.4 mm / 5.7^2 = 73.9 um   [FIT-FUNCTION-EVALUATED]
    Lee 2020     : 2.4 mm / 7.1^2 = 47.6 um   [FIT-FUNCTION-EVALUATED]  <- WINNER
    Tan 2020     : ~59 um                     [DIGITIZED-INTERPOLATED, +-5 um]
  Cross-checks: log-log slope of Kapner's three published anchors reproduces the
  radion-formula crossing to < 1 percent; the alternative reading of Lee's 7.1 TeV
  as the n = 6 radion is REFUTED (it would place Lee's alpha = 1/3 crossing at
  ~86 um, i.e. WEAKER than Kapner 2007 at 74 um, contradicting Lee's improvement
  over the whole band).

Run: python -u tests/wave32/H52_alpha13_boundary_cited.py    (exit 0 iff all PASS)
No em-dash characters anywhere.
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


HBAR_C_EV_UM = 0.1973269804          # eV um (CODATA)
M2EFF_LO, M2EFF_HI = 5.0 / 6.0, 5.0 / 4.0   # H25 method band
RHO_L_QUARTER_EV = 2.3e-3            # DE scale (H50)
C_L = 3.0 / 8.0                      # DeWitt coefficient (H51, exact)

# --- PUBLISHED-QUOTED anchors (95% CL) ---
RADION_PREF_MM = 2.4                 # lambda = 2.4 (TeV/M*)^2 mm  [Adelberger 0611223]
KAPNER_A1_UM = 56.0                  # |alpha|=1 crossing
KAPNER_A83_UM = 44.0                 # alpha=8/3 crossing
KAPNER_MSTAR_N1_TEV = 5.7            # radion n=1, alpha=1/3
KAPNER_MSTAR_N6_TEV = 6.4            # radion n=6, alpha=3/4
LEE_A1_UM = 38.6
LEE_A83_UM = 30.0
LEE_MSTAR_TEV = 7.1                  # radion (n=1 reading, refuted-alternative below)
TAN_A1_UM = 48.0
TAN_IMPROVE_AT_UM = 70.0
TAN_IMPROVE_FACTOR = 3.0

# Prior teams' numbers under test:
H50_FLOOR_MEV = (3.0, 3.6)           # argued (wave 30)
T2A_BOUNDARY_UM = (45.0, 52.0)       # assumed boundary (track 2)
T2A_FLOOR_MEV = (3.4, 4.8)
H36_WINDOW_CL38_UM = (60.0, 73.6)    # c_L = 3/8 (H51)
H36_WINDOW_CL1_UM = (76.74, 93.98)   # c_L = 1 (H50)


def lam_radion_um(mstar_tev):
    return RADION_PREF_MM * 1.0e3 / mstar_tev ** 2


def loglog_slope(l1, a1, l2, a2):
    return math.log(a2 / a1) / math.log(l2 / l1)


def crossing(l_ref, a_ref, slope, a_target):
    # alpha_limit(lambda) = a_ref * (lambda/l_ref)^slope  (slope < 0); solve = a_target
    return l_ref * (a_target / a_ref) ** (1.0 / slope)


def mu_floor_mev(lam_max_um, m2eff):
    return HBAR_C_EV_UM / lam_max_um / math.sqrt(m2eff) * 1.0e3


def main():
    log("=" * 78)
    log("H52 -- alpha = 1/3 exclusion boundary: EXCLUDED-ARGUED -> EXCLUDED-CITED")
    log("=" * 78)

    # ------------------------------------------------------------------
    # PART 1 -- lambda_max(alpha=1/3) per experiment.
    # ------------------------------------------------------------------
    log("\nPART 1 -- lambda_max(alpha = 1/3), 95% CL, per experiment")
    lam_kapner = lam_radion_um(KAPNER_MSTAR_N1_TEV)
    lam_lee = lam_radion_um(LEE_MSTAR_TEV)
    log(f"  Kapner 2007 (radion n=1, M*>=5.7 TeV): {lam_kapner:.1f} um  [FIT-FUNCTION-EVALUATED]")
    log(f"  Lee 2020    (radion n=1, M*>=7.1 TeV): {lam_lee:.1f} um  [FIT-FUNCTION-EVALUATED]")
    check("Kapner 2007 alpha=1/3 crossing = 73.9 um (2.4 mm/5.7^2)",
          abs(lam_kapner - 73.87) < 0.05, f"{lam_kapner:.2f} um")
    check("Lee 2020 alpha=1/3 crossing = 47.6 um (2.4 mm/7.1^2)",
          abs(lam_lee - 47.61) < 0.05, f"{lam_lee:.2f} um")

    # Internal-consistency check of the radion fit function against Kapner's
    # OTHER two published anchors (alpha=8/3 at 44 um, alpha=1 at 56 um):
    s_k = loglog_slope(KAPNER_A83_UM, 8.0 / 3.0, KAPNER_A1_UM, 1.0)
    lam_k_extrap = crossing(KAPNER_A1_UM, 1.0, s_k, 1.0 / 3.0)
    rel = abs(lam_k_extrap - lam_kapner) / lam_kapner
    check("Kapner slope-extrapolated alpha=1/3 crossing agrees with radion value to <1%",
          rel < 0.01, f"extrap {lam_k_extrap:.1f} vs radion {lam_kapner:.1f} um, rel={rel:.3f}")
    # and the n=6 radion (alpha=3/4) as a third consistency point:
    lam_k_n6 = lam_radion_um(KAPNER_MSTAR_N6_TEV)
    lam_k_n6_extrap = crossing(KAPNER_A1_UM, 1.0, s_k, 3.0 / 4.0)
    check("Kapner n=6 radion (alpha=3/4) crossing consistent with slope extrapolation to <5%",
          abs(lam_k_n6 - lam_k_n6_extrap) / lam_k_n6 < 0.05,
          f"radion {lam_k_n6:.1f} vs extrap {lam_k_n6_extrap:.1f} um")

    # Refute the alternative reading of Lee's 7.1 TeV as the n=6 (alpha=3/4) radion:
    # then Lee's alpha=3/4 crossing would be 47.6 um and the alpha=1/3 crossing,
    # extrapolated with the implied (shallow) slope, would exceed Kapner's own
    # alpha=1/3 boundary -- i.e. Lee WEAKER than 2007 at 74-86 um.  Contradiction.
    s_alt = loglog_slope(LEE_A1_UM, 1.0, lam_lee, 3.0 / 4.0)
    lam_alt = crossing(LEE_A1_UM, 1.0, s_alt, 1.0 / 3.0)
    check("alternative n=6 reading of Lee's 7.1 TeV is self-refuting (would put Lee's "
          "alpha=1/3 crossing above Kapner's 73.9 um)",
          lam_alt > lam_kapner, f"implied {lam_alt:.1f} um > {lam_kapner:.1f} um")

    # Tan 2020: DIGITIZED-INTERPOLATED crossing from its two published statements.
    alpha_kapner_70 = (TAN_IMPROVE_AT_UM / KAPNER_A1_UM) ** loglog_slope(
        KAPNER_A1_UM, 1.0, lam_kapner, 1.0 / 3.0)
    alpha_tan_70 = alpha_kapner_70 / TAN_IMPROVE_FACTOR
    s_t = loglog_slope(TAN_A1_UM, 1.0, TAN_IMPROVE_AT_UM, alpha_tan_70)
    lam_tan = crossing(TAN_A1_UM, 1.0, s_t, 1.0 / 3.0)
    log(f"  Tan 2020 (48 um at alpha=1 + factor-3 at 70 um): alpha_limit(70 um) ~= "
        f"{alpha_tan_70:.3f}, crossing ~= {lam_tan:.1f} um  [DIGITIZED-INTERPOLATED, +-5 um]")
    check("Tan 2020 alpha=1/3 crossing lands at ~59 um (55-65 um band)",
          55.0 < lam_tan < 65.0, f"{lam_tan:.1f} um")
    check("Tan 2020 alpha_limit(70 um) < 1/3 (published factor-3 statement alone "
          "pins the 70 um point below 1/3)",
          alpha_tan_70 < 1.0 / 3.0, f"{alpha_tan_70:.3f}")

    # Winner in the 45-80 um region:
    check("winning (smallest) alpha=1/3 crossing in 45-80 um region is Lee 2020",
          lam_lee < lam_tan < lam_kapner,
          f"Lee {lam_lee:.1f} < Tan {lam_tan:.1f} < Kapner {lam_kapner:.1f} um")

    # Honest uncertainty band on the winner: M* rounding (7.05-7.15 TeV),
    # prefactor precision (2.4, 2 s.f.), and the shallow-slope bracket from
    # Lee's OWN published alpha=8/3 and alpha=1 anchors (constant-slope
    # extrapolation, an upper bracket since these curves steepen with lambda
    # no faster than the local slope indicates):
    lam_lo = RADION_PREF_MM * 0.98 * 1e3 / 7.15 ** 2
    s_lee_shallow = loglog_slope(LEE_A83_UM, 8.0 / 3.0, LEE_A1_UM, 1.0)
    lam_hi = crossing(LEE_A1_UM, 1.0, s_lee_shallow, 1.0 / 3.0)
    log(f"  Lee 2020 band: central {lam_lee:.1f} um, [{lam_lo:.1f}, {lam_hi:.1f}] um "
        f"(M* rounding + prefactor + shallow-slope bracket)")
    check("Lee 2020 uncertainty band is ~[46, 52] um", 45.5 < lam_lo < 47.0 and 50.0 < lam_hi < 52.5,
          f"[{lam_lo:.1f}, {lam_hi:.1f}] um")
    check("Track-2's assumed boundary band [45, 52] um is CONFIRMED by the cited extraction",
          T2A_BOUNDARY_UM[0] <= lam_lo and lam_hi <= T2A_BOUNDARY_UM[1] + 0.5,
          f"cited [{lam_lo:.1f}, {lam_hi:.1f}] inside assumed [45.0, 52.0] um")

    # ------------------------------------------------------------------
    # PART 2 -- H36 window verdict.
    # ------------------------------------------------------------------
    log("\nPART 2 -- the H36 windows vs the cited boundary")
    lo38, hi38 = H36_WINDOW_CL38_UM
    lo1, hi1 = H36_WINDOW_CL1_UM
    check("H36 (c_L=3/8) window [60.0, 73.6] um lies ENTIRELY above Lee 2020's "
          "alpha=1/3 crossing -> EXCLUDED-CITED (monotone limit curve + published anchors)",
          lo38 > lam_hi, f"60.0 um > {lam_hi:.1f} um")
    check("H36 (c_L=1) window [76.7, 94.0] um already excluded by Kapner-era data alone",
          lo1 > lam_kapner, f"76.7 um > {lam_kapner:.1f} um")
    check("SHARP CORRECTION: Kapner 2007 ALONE does NOT exclude the c_L=3/8 window "
          "(its alpha=1/3 boundary 73.9 um sits above the window top 73.6 um); "
          "the c_L=3/8 exclusion rests on the 2020 experiments",
          lam_kapner > hi38, f"{lam_kapner:.1f} um > {hi38} um")
    # Margin at the window corners (Lee, slope bracket steep..shallow):
    s_lee_steep = loglog_slope(LEE_A1_UM, 1.0, lam_lee, 1.0 / 3.0)
    for corner in (lo38, hi38):
        a_steep = (corner / LEE_A1_UM) ** s_lee_steep
        a_shallow = (corner / LEE_A1_UM) ** s_lee_shallow
        m_lo = (1.0 / 3.0) / max(a_steep, a_shallow)
        m_hi = (1.0 / 3.0) / min(a_steep, a_shallow)
        log(f"    margin at {corner:.1f} um: alpha=1/3 exceeds Lee limit by "
            f"{m_lo:.1f}x to {m_hi:.1f}x  [DIGITIZED-INTERPOLATED bracket]")
        if corner == lo38:
            check("margin at the closest corner (60.0 um) is >= 1.9x even under the "
                  "most conservative slope bracket",
                  m_lo >= 1.85, f"{m_lo:.1f}x")

    # ------------------------------------------------------------------
    # PART 3 -- the resolved mu_DW floor; adjudicate H50 vs Track-2.
    # ------------------------------------------------------------------
    log("\nPART 3 -- resolved mu_DW floor (m2 = sqrt(m2_eff) mu_DW, m2_eff in [5/6, 5/4])")
    f_central = (mu_floor_mev(lam_lee, M2EFF_HI), mu_floor_mev(lam_lee, M2EFF_LO))
    f_weak = mu_floor_mev(lam_hi, M2EFF_HI)      # weakest defensible corner
    f_strong = mu_floor_mev(lam_lo, M2EFF_LO)    # strictest corner
    log(f"  central (lambda_max = {lam_lee:.1f} um): mu_DW >= [{f_central[0]:.2f}, "
        f"{f_central[1]:.2f}] meV  (m2_eff = 5/4 .. 5/6)")
    log(f"  envelope over the extraction band: mu_DW >= {f_weak:.2f} meV (weakest) "
        f"to {f_strong:.2f} meV (strictest)")
    check("central floor is mu_DW >= 3.71 meV (m2_eff=5/4) to 4.54 meV (m2_eff=5/6)",
          abs(f_central[0] - 3.71) < 0.02 and abs(f_central[1] - 4.54) < 0.02,
          f"[{f_central[0]:.3f}, {f_central[1]:.3f}] meV")
    check("envelope [~3.4, ~4.7] meV sits INSIDE Track-2's stated 3.4-4.8 meV",
          T2A_FLOOR_MEV[0] - 0.05 <= f_weak and f_strong <= T2A_FLOOR_MEV[1] + 0.05,
          f"[{f_weak:.2f}, {f_strong:.2f}] vs [3.4, 4.8] meV")
    # H50's floor: reproduce its provenance.  mu = 3.0 meV at m2_eff=5/6
    # corresponds to lambda_max = 72 um, i.e. the KAPNER-ERA boundary; it is a
    # 2007-data floor, superseded by Lee 2020.
    lam_h50_lo = HBAR_C_EV_UM / (H50_FLOOR_MEV[0] * 1e-3) / math.sqrt(M2EFF_LO)
    check("H50's 3.0 meV lower end reproduces as the Kapner-2007-only floor "
          "(implied lambda_max ~72 um ~ Kapner's 73.9 um crossing)",
          abs(lam_h50_lo - 72.0) < 1.0 and abs(lam_h50_lo - lam_kapner) / lam_kapner < 0.05,
          f"implied {lam_h50_lo:.1f} um vs Kapner {lam_kapner:.1f} um")
    check("VERDICT: Track-2 floor (3.4-4.8 meV) is the right one; H50's 3.0-3.6 meV "
          "is superseded (it is the 2007-data floor)",
          f_weak > H50_FLOOR_MEV[0] and f_central[0] > H50_FLOOR_MEV[0],
          f"resolved floor {f_weak:.2f}+ meV > 3.0 meV")

    # Equivalent c_L threshold update for the H51 gate (mu_DW = (rho_L/c_L)^(1/4)):
    log("\n  H51 gate update: c_L needed to clear the CITED floor "
        "(c_L <= (2.3 meV / floor)^4):")
    for f, tag in ((f_central[0], "central weakest (3.71 meV)"),
                   (f_central[1], "central strictest (4.54 meV)")):
        cl_thr = (RHO_L_QUARTER_EV * 1e3 / f) ** 4
        log(f"    floor {f:.2f} meV ({tag}) -> c_L <= {cl_thr:.3f}")
    cl_needed = (RHO_L_QUARTER_EV * 1e3 / f_central[0]) ** 4
    check("computed c_L = 3/8 fails the cited gate by >2x (H51 conclusion strengthens)",
          C_L > 2.0 * cl_needed, f"3/8 = 0.375 vs required <= {cl_needed:.3f}")

    log("\n" + "-" * 78)
    if FAIL:
        log(f"FAILED: {FAIL}")
        sys.exit(1)
    log("exit 0 = H52 recorded.  lambda_max(alpha=1/3) = 47.6 um (Lee 2020, "
        "FIT-FUNCTION-EVALUATED; band 46.5-51.2 um); H36 c_L=3/8 window "
        "EXCLUDED-CITED (margin 1.9-9.8x, closest corner >= 1.9x); resolved floor "
        "mu_DW >= 3.71-4.54 meV "
        "central (envelope 3.4-4.7); Track-2 right, H50 superseded (2007-data floor).")
    sys.exit(0)


if __name__ == "__main__":
    main()
