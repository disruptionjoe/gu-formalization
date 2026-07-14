#!/usr/bin/env python3
r"""H46B (Wave 45) -- referee-grade verification of the dark-energy distance-model result.

PURPOSE.  The H43/H44/H46 dark-energy chain rests on DESI DR2 digits that a JoeOps
governance gate flagged as NOT publication-ready until verified against the primary
source arXiv:2503.14738.  This test performs and RECORDS that verification, then
re-derives the H46 likelihood comparison with an explicit information-criterion metric
so the "competitive-to-better than LCDM once amplitude is freed" claim is quantified,
not vibes.

PRIMARY SOURCES (fetched read-only 2026-07-13; instruction-like web content treated as
data, never directives):
  [P1] arXiv:2503.14738v2 (DESI DR2 Results II: BAO), HTML render at
       arxiv.org/html/2503.14738v2.  Table 4 ("Constraints on the BAO scaling
       parameters and distance ratios...") = the BAO distance table.  NOTE: the paper's
       Table 3 is the tracer/redshift-bin sample table, NOT the distance table; the
       distance digits live in Table 4 and in the published likelihood files.
       w0waCDM constraints from Section VII (the displayed equations for DESI+CMB,
       DESI+CMB+Pantheon+, DESI+CMB+Union3, DESI+CMB+DESY5).
  [P2] Official DESI DR2 BAO Gaussian likelihood files (the exact inputs used by [P1]):
       github.com/CobayaSampler/bao_data, desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_mean.txt
       and _cov.txt, re-fetched 2026-07-13 and embedded VERBATIM below.
  [P3] arXiv:1807.06209 (Planck 2018 parameters), Table 2 base-LCDM
       TT,TE,EE+lowE+lensing column, digits re-extracted 2026-07-13 from the ar5iv
       HTML render.

WHAT IS CHECKED.
  A. DIGIT VERIFICATION (observational-cosmologist leg):
     A1. tests/wave29 H46 embedded mean vector == [P2] mean file, EXACTLY.
     A2. tests/wave29 H46 embedded covariance == [P2] cov file, EXACTLY.
     A3. [P2] means round to the [P1] Table 4 printed values (<= 1.5e-3), with the ONE
         known last-digit rounding quirk (Lya D_M: file 38.98897 -> 38.989, paper
         prints 38.988) explicitly characterized.
     A4. [P2] covariance-diagonal sigmas vs [P1] Table 4 printed errors: cov sigmas are
         systematically EQUAL-OR-LARGER (1.00x..1.07x) -- the likelihood covariance
         includes systematic terms; the likelihood file is authoritative for chi^2.
     A5. per-tracer D_M-D_H correlations from [P2] vs [P1] printed r_M,H: |diff|<=0.08
         (cov-file correlations are mildly diluted where sys terms inflate diagonals).
     A6. the Planck 2018 prior digits used by H46 == [P3] Table 2 digits.
     A7. the H43/H3 CPL comparison digits (w0=-0.752+/-0.057, wa=-0.86 +0.23/-0.20,
         DESI+CMB+DESY5) == [P1] Section VII displayed equation, and the w0-wa
         correlation rho=-0.8 is a DECLARED assumption scanned over (-0.9,-0.8,-0.7)
         in tests/wave1 (DESI does not tabulate rho) -- declared, not fabricated.
  B. LIKELIHOOD COMPARISON RE-DERIVED (statistician leg):
     B1. re-computes the H46 numbers from the imported H46 module (same physics, no
         re-implementation): chi^2_GU=52.26, chi^2_LCDM=30.68 (fixed CMB amplitude),
         amplitude-marginalized 10.99 vs 14.15, free-f0 envelope best 12.28 at f0=0.05.
     B2. AIC accounting with explicit parameter counts:
           fixed amplitude, 0 fitted params each: dAIC = dchi^2 = +21.58 (GU disfavored)
           amplitude freed for BOTH (1 param each): dAIC = -3.17 (GU mildly favored;
             below the |dAIC|>=4 "positive evidence" line -- competitive, NOT decisive)
           f0 freed (GU 1 param vs LCDM 0, fixed A): dAIC = -16.4 (envelope only;
             adopting it would be BAO tuning and is inconsistent with the CPL-tuned f0)
     B3. goodness-of-fit p-values (chi^2 survival function) for each configuration.
     B4. the INTERNAL-INCONSISTENCY guard: the BAO-preferred f0 (~0.05) differs from
         the CPL-tuned canonical f0=0.125 by a factor >= 2 -- the two observables pull
         f0 apart, so no single f0 satisfies both.  This must stay in any writeup.
  C. FRAMING GUARDS (hostile-referee / honesty-auditor legs):
     C1. the H46 exploration keeps the CPL falsification as the standing headline.
     C2. the canon theta-DE file's verdict is still OPEN (no silent promotion).

Run: python -u tests/wave45/H46B_referee_grade_desi_verification.py   (exit 0 iff all PASS)
"""
from __future__ import annotations
import os
import sys
import importlib.util
import numpy as np
from scipy.stats import chi2 as chi2_dist

FAIL = []


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}", flush=True)
    if not ok:
        FAIL.append(name)


def log(m=""):
    print(m, flush=True)


_HERE = os.path.dirname(os.path.abspath(__file__))
_REPO = os.path.normpath(os.path.join(_HERE, "..", ".."))


def _load(relpath, name):
    p = os.path.join(_REPO, relpath)
    spec = importlib.util.spec_from_file_location(name, p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ===========================================================================
# [P2] Official DESI DR2 BAO likelihood files, re-fetched 2026-07-13, VERBATIM.
# desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_mean.txt  (z, value, quantity)
# ===========================================================================
P2_ROWS = [
    (0.295, "DV"),
    (0.510, "DM"), (0.510, "DH"),
    (0.706, "DM"), (0.706, "DH"),
    (0.934, "DM"), (0.934, "DH"),
    (1.321, "DM"), (1.321, "DH"),
    (1.484, "DM"), (1.484, "DH"),
    (2.330, "DH"), (2.330, "DM"),   # Lya block orders DH before DM in the file
]
P2_MEAN = np.array([
    7.94167639,
    13.58758434, 21.86294686,
    17.35069094, 19.45534918,
    21.57563956, 17.64149464,
    27.60085612, 14.17602155,
    30.51190063, 12.81699964,
    8.631545674846294, 38.988973961958784,
])
P2_COV = np.zeros((13, 13))
P2_COV[0, 0] = 5.78998687e-03
P2_COV[1, 1], P2_COV[2, 2], P2_COV[1, 2] = 2.83473742e-02, 1.83928040e-01, -3.26062007e-02
P2_COV[3, 3], P2_COV[4, 4], P2_COV[3, 4] = 3.23752442e-02, 1.11469198e-01, -2.37445646e-02
P2_COV[5, 5], P2_COV[6, 6], P2_COV[5, 6] = 2.61732816e-02, 4.04183878e-02, -1.12938006e-02
P2_COV[7, 7], P2_COV[8, 8], P2_COV[7, 8] = 1.05336516e-01, 5.04233092e-02, -2.90308418e-02
P2_COV[9, 9], P2_COV[10, 10], P2_COV[9, 10] = 5.83020277e-01, 2.68336193e-01, -1.95215562e-01
P2_COV[11, 11], P2_COV[12, 12], P2_COV[11, 12] = 1.02136194e-02, 2.82685779e-01, -2.31395216e-02
P2_COV = P2_COV + np.triu(P2_COV, 1).T

# ===========================================================================
# [P1] arXiv:2503.14738v2 Table 4 printed values (extracted from the HTML render
# 2026-07-13 by direct text extraction, not by a summarizer).
# Each row: (tracer, z_eff, quantity, value, sigma).  r_MH per tracer below.
# ===========================================================================
P1_TABLE4 = [
    ("BGS",       0.295, "DV",  7.942, 0.075),
    ("LRG1",      0.510, "DM", 13.588, 0.167),
    ("LRG1",      0.510, "DH", 21.863, 0.425),
    ("LRG2",      0.706, "DM", 17.351, 0.177),
    ("LRG2",      0.706, "DH", 19.455, 0.330),
    ("LRG3+ELG1", 0.934, "DM", 21.576, 0.152),
    ("LRG3+ELG1", 0.934, "DH", 17.641, 0.193),
    ("ELG2",      1.321, "DM", 27.601, 0.318),
    ("ELG2",      1.321, "DH", 14.176, 0.221),
    ("QSO",       1.484, "DM", 30.512, 0.760),
    ("QSO",       1.484, "DH", 12.817, 0.516),
    ("Lya",       2.330, "DH",  8.632, 0.101),
    ("Lya",       2.330, "DM", 38.988, 0.531),
]
P1_R_MH = {
    "LRG1": -0.459, "LRG2": -0.404, "LRG3+ELG1": -0.416,
    "ELG2": -0.434, "QSO": -0.500, "Lya": -0.431,
}
# [P1] Section VII w0waCDM constraints (displayed equations; asymmetric errors as printed)
P1_CPL = {
    "DESI+CMB":           dict(w0=-0.42,  sw0=0.21,  wa=-1.75, swap=0.58, swam=0.58),
    "DESI+CMB+Pantheon+": dict(w0=-0.838, sw0=0.055, wa=-0.62, swap=0.22, swam=0.19),
    "DESI+CMB+Union3":    dict(w0=-0.667, sw0=0.088, wa=-1.09, swap=0.31, swam=0.27),
    "DESI+CMB+DESY5":     dict(w0=-0.752, sw0=0.057, wa=-0.86, swap=0.23, swam=0.20),
}
# [P3] Planck 2018 Table 2, base-LCDM TT,TE,EE+lowE+lensing
P3_PLANCK = dict(H0=67.36, Om=0.3153, r_drag=147.09, omh2=0.1430)


def main():
    log("=" * 78)
    log("H46B (Wave 45) -- referee-grade verification: DESI DR2 digits vs primary source,")
    log("                  and the H46 likelihood comparison with an explicit AIC metric")
    log("=" * 78)

    H46 = _load(os.path.join("tests", "wave29", "H46_de_raw_bao_likelihood.py"), "H46_mod")

    # -------------------------------------------------------------------
    # A1/A2 -- repo arrays vs the official likelihood files, EXACT.
    # -------------------------------------------------------------------
    log("\nA1/A2 -- repo-embedded likelihood vs official DESI DR2 files (exact match required)")
    check("A1: H46 mean vector == official mean file (exact, all 13 entries)",
          np.array_equal(np.asarray(H46.DESI_MEAN, dtype=float), P2_MEAN))
    check("A1b: H46 row ordering (z, quantity) == official file ordering (incl. Lya DH-before-DM)",
          [(float(z), q) for z, q in H46.DESI_ROWS] == [(float(z), q) for z, q in P2_ROWS])
    check("A2: H46 covariance == official cov file (exact, all 169 entries)",
          np.array_equal(np.asarray(H46.DESI_COV, dtype=float), P2_COV))

    # -------------------------------------------------------------------
    # A3 -- likelihood-file means vs the paper's Table 4 printed values.
    # -------------------------------------------------------------------
    log("\nA3 -- likelihood-file means vs arXiv:2503.14738v2 Table 4 printed values")
    n_exact_round = 0
    quirks = []
    for (tr, z, q, val, sig), m in zip(P1_TABLE4, P2_MEAN):
        d = abs(m - val)
        rounded = round(m, 3)
        same = abs(rounded - val) < 5e-4
        n_exact_round += int(same)
        if not same:
            quirks.append((tr, q, m, val))
        log(f"     {tr:10s} z={z:5.3f} {q}: file {m:12.6f} -> paper {val:7.3f}  |diff|={d:.4f}"
            f"{'' if same else '   <- last-digit rounding quirk'}")
        check(f"A3: {tr} {q} file mean within 1.5e-3 of paper Table 4 value", d <= 1.5e-3,
              f"|{m:.5f}-{val}|={d:.4f}")
    check("A3b: exactly ONE last-digit rounding quirk, and it is Lya D_M (38.98897 vs printed 38.988)",
          n_exact_round == 12 and len(quirks) == 1 and quirks[0][0] == "Lya" and quirks[0][1] == "DM",
          f"quirks={quirks}")

    # -------------------------------------------------------------------
    # A4 -- cov-diagonal sigmas vs paper printed errors (sys-inclusive cov >= stat).
    # -------------------------------------------------------------------
    log("\nA4 -- covariance-diagonal sigmas vs paper printed errors (ratio must be 1.00..1.08)")
    sig_file = np.sqrt(np.diag(P2_COV))
    ratios = []
    for (tr, z, q, val, sig), sf in zip(P1_TABLE4, sig_file):
        r = sf / sig
        ratios.append(r)
        log(f"     {tr:10s} {q}: cov sigma {sf:.4f} vs paper {sig:.3f}   ratio {r:.4f}")
    ratios = np.array(ratios)
    check("A4: every cov sigma >= paper printed error (cov includes systematics)",
          bool(np.all(ratios >= 0.999)), f"min ratio {ratios.min():.4f}")
    check("A4b: no cov sigma exceeds the paper error by more than 8%",
          bool(np.all(ratios <= 1.08)), f"max ratio {ratios.max():.4f}")

    # -------------------------------------------------------------------
    # A5 -- per-tracer D_M-D_H correlations vs paper r_M,H.
    # -------------------------------------------------------------------
    log("\nA5 -- per-tracer D_M-D_H correlations: cov file vs paper r_M,H")
    blocks = {"LRG1": (1, 2), "LRG2": (3, 4), "LRG3+ELG1": (5, 6),
              "ELG2": (7, 8), "QSO": (9, 10), "Lya": (11, 12)}
    for tr, (i, j) in blocks.items():
        r_file = P2_COV[i, j] / np.sqrt(P2_COV[i, i] * P2_COV[j, j])
        r_pap = P1_R_MH[tr]
        log(f"     {tr:10s}: cov r = {r_file:+.4f} vs paper r_M,H = {r_pap:+.3f}  |diff|={abs(r_file-r_pap):.4f}")
        check(f"A5: {tr} correlation within 0.08 of paper r_M,H (dilution from sys-inflated diagonals)",
              abs(r_file - r_pap) <= 0.08)

    # -------------------------------------------------------------------
    # A6 -- Planck 2018 prior digits.
    # -------------------------------------------------------------------
    log("\nA6 -- Planck 2018 (arXiv:1807.06209 Table 2) prior digits used by H46")
    check("A6: H0 = 67.36 km/s/Mpc", float(H46.H0_CMB) == P3_PLANCK["H0"])
    check("A6: Omega_m = 0.3153", float(H46.OM_CMB) == P3_PLANCK["Om"])
    check("A6: r_drag = 147.09 Mpc", float(H46.RD_CMB) == P3_PLANCK["r_drag"])

    # -------------------------------------------------------------------
    # A7 -- the CPL digits H43/H3 compare against, vs the paper's Section VII.
    # -------------------------------------------------------------------
    log("\nA7 -- CPL comparison digits (H43/H3) vs arXiv:2503.14738 Section VII")
    h43_src = open(os.path.join(_REPO, "tests", "wave20", "H43_de_shape_falsifier.py"),
                   encoding="utf-8").read()
    d5 = P1_CPL["DESI+CMB+DESY5"]
    check("A7: H43 embeds DESY5 w0=-0.752, sw0=0.057, wa=-0.86, +0.23/-0.20 (matches paper)",
          "cw0=-0.752, sw0=0.057, cwa=-0.86, swap=0.23, swam=0.20" in h43_src
          and d5["w0"] == -0.752 and d5["sw0"] == 0.057 and d5["wa"] == -0.86
          and d5["swap"] == 0.23 and d5["swam"] == 0.20)
    h3_src = open(os.path.join(_REPO, "tests", "wave1", "H3_desi_verified_and_intersection.py"),
                  encoding="utf-8").read()
    check("A7b: w0-wa correlation rho=-0.8 is a DECLARED assumption scanned in H3 "
          "(RHO_SCAN=(-0.9,-0.8,-0.7); DESI does not tabulate rho)",
          "RHO_SCAN = (-0.9, -0.8, -0.7)" in h3_src and "rho=-0.8" in h43_src)
    log("     paper Section VII (verified 2026-07-13): DESI+CMB w0=-0.42+/-0.21, wa=-1.75+/-0.58;")
    log("     +Pantheon+ (-0.838+/-0.055, -0.62 +0.22/-0.19); +Union3 (-0.667+/-0.088, -1.09 +0.31/-0.27);")
    log("     +DESY5 (-0.752+/-0.057, -0.86 +0.23/-0.20).  LCDM-preference 3.1 sigma (DESI+CMB),")
    log("     2.8-4.2 sigma with SNe.  H43's 3.2-sigma figure is GU-locus-vs-DESY5-contour, a")
    log("     DIFFERENT quantity from DESI's LCDM-preference sigmas -- do not conflate.")

    # -------------------------------------------------------------------
    # B -- likelihood comparison re-derived, with AIC.
    # -------------------------------------------------------------------
    log("\n" + "=" * 78)
    log("B -- the honest likelihood comparison, re-derived with explicit AIC accounting")
    log("=" * 78)
    bg = H46.solve_backreacted(H46.M2_BC1, H46.F0_CANON, npts=1400)
    zc, Ec = H46._sorted_zE(bg["z"], np.sqrt(bg["H2"]))
    ac = 1.0 / (1.0 + zc)
    E_l = H46.E_lcdm_on(ac)
    A = H46.A_CMB

    chi2_gu = H46.chi2_of(H46.bao_vector_from_E(zc, Ec, A))
    chi2_l = H46.chi2_of(H46.bao_vector_from_E(zc, E_l, A))
    dfix = chi2_gu - chi2_l
    chi2m_gu, Ag = H46.chi2_marg_amplitude(H46.bao_vector_from_E(zc, Ec, 1.0))
    chi2m_l, Al = H46.chi2_marg_amplitude(H46.bao_vector_from_E(zc, E_l, 1.0))
    dmarg = chi2m_gu - chi2m_l

    best = None
    for f0 in (0.02, 0.05, 0.08, 0.125, 0.25, 0.5, 1.0, 2.0):
        b = H46.solve_backreacted(H46.M2_BC1, f0, npts=900, n_iter=40)
        zz, EE = H46._sorted_zE(b["z"], np.sqrt(b["H2"]))
        c2 = H46.chi2_of(H46.bao_vector_from_E(zz, EE, A))
        if best is None or c2 < best[1]:
            best = (f0, c2)

    log(f"  fixed CMB amplitude (0 fitted params each):  chi^2_GU={chi2_gu:.2f}  chi^2_LCDM={chi2_l:.2f}"
        f"  dchi^2={dfix:+.2f}")
    log(f"  amplitude marginalized (1 param each):        chi^2_GU={chi2m_gu:.2f}  chi^2_LCDM={chi2m_l:.2f}"
        f"  dchi^2={dmarg:+.2f}   (A*_GU={Ag:.3f}, A*_LCDM={Al:.3f}, CMB A={A:.3f})")
    log(f"  free-f0 envelope at fixed A (1 GU param):     best chi^2={best[1]:.2f} at f0={best[0]}")

    check("B1: fixed-amplitude chi^2 values reproduce H46 (52.26 / 30.68 / +21.58, tol 0.05)",
          abs(chi2_gu - 52.26) < 0.05 and abs(chi2_l - 30.68) < 0.05 and abs(dfix - 21.58) < 0.05,
          f"{chi2_gu:.2f}/{chi2_l:.2f}/{dfix:+.2f}")
    check("B1b: amplitude-marginalized chi^2 reproduce H46 (10.99 / 14.15 / -3.17, tol 0.05)",
          abs(chi2m_gu - 10.99) < 0.05 and abs(chi2m_l - 14.15) < 0.05 and abs(dmarg + 3.17) < 0.05,
          f"{chi2m_gu:.2f}/{chi2m_l:.2f}/{dmarg:+.2f}")
    check("B1c: free-f0 envelope best reproduces H46 (12.28 at f0=0.05, tol 0.05)",
          best[0] == 0.05 and abs(best[1] - 12.28) < 0.05, f"{best[1]:.2f} at f0={best[0]}")

    # AIC = chi^2 + 2k on the SAME data; dAIC = AIC_GU - AIC_LCDM.
    log("\n  AIC accounting (AIC = chi^2 + 2k; dAIC = AIC_GU - AIC_LCDM; negative favors GU):")
    daic_fixed = (chi2_gu + 0) - (chi2_l + 0)
    daic_marg = (chi2m_gu + 2) - (chi2m_l + 2)
    daic_f0 = (best[1] + 2) - (chi2_l + 0)
    p_gu_fix = float(chi2_dist.sf(chi2_gu, 13))
    p_l_fix = float(chi2_dist.sf(chi2_l, 13))
    p_gu_m = float(chi2_dist.sf(chi2m_gu, 12))
    p_l_m = float(chi2_dist.sf(chi2m_l, 12))
    log(f"     fixed A, k=(0,0):      dAIC = {daic_fixed:+.2f}   GOF p: GU {p_gu_fix:.2e}, LCDM {p_l_fix:.4f}")
    log(f"     A freed BOTH, k=(1,1): dAIC = {daic_marg:+.2f}   GOF p: GU {p_gu_m:.3f},   LCDM {p_l_m:.3f}")
    log(f"     f0 freed, k=(1,0):     dAIC = {daic_f0:+.2f}   (ENVELOPE ONLY -- adopting it is BAO tuning)")
    check("B2: dAIC(fixed) > +20: GU canonical point strongly disfavored at the CMB-fixed amplitude",
          daic_fixed > 20.0, f"{daic_fixed:+.2f}")
    check("B2b: dAIC(A freed both) in (-4, 0): GU competitive-to-mildly-better, NOT decisive "
          "(|dAIC|<4 is below the conventional positive-evidence line)",
          -4.0 < daic_marg < 0.0, f"{daic_marg:+.2f}")
    check("B2c: shape-marginalized GU is an acceptable fit in absolute terms (GOF p > 0.05) "
          "and so is LCDM (the comparison is between two acceptable fits)",
          p_gu_m > 0.05 and p_l_m > 0.05, f"p_GU={p_gu_m:.3f}, p_LCDM={p_l_m:.3f}")
    check("B2d: at the fixed Planck amplitude even LCDM fits poorly (GOF p < 0.01: the known "
          "Planck-vs-DESI-DR2 amplitude tension; GU's +21.6 is an increment ON TOP of it)",
          p_l_fix < 0.01, f"p_LCDM={p_l_fix:.4f}")
    check("B4: internal-inconsistency guard: BAO-preferred f0 differs from CPL-tuned f0=0.125 "
          "by a factor >= 2 (no single f0 satisfies both observables)",
          best[0] * 2.0 <= H46.F0_CANON, f"BAO f0={best[0]}, CPL f0={H46.F0_CANON}")

    # -------------------------------------------------------------------
    # C -- framing guards.
    # -------------------------------------------------------------------
    log("\nC -- framing guards (headline discipline)")
    h46_expl = open(os.path.join(_REPO, "explorations", "wave29",
                                 "H46-de-raw-bao-likelihood-2026-07-11.md"), encoding="utf-8").read()
    check("C1: H46 exploration keeps the CPL falsification as the standing headline "
          "('CPL falsification stands' present; H43/H44 not overturned)",
          "CPL falsification stands" in h46_expl and "NOT overturned" in h46_expl)
    canon = open(os.path.join(_REPO, "canon", "theta-field-flrw-dark-energy-eos.md"),
                 encoding="utf-8").read()
    check("C2: canon theta-DE file verdict is still OPEN (no silent promotion)",
          "verdict: OPEN" in canon)

    log("")
    if FAIL:
        log(f"FAILED: {FAIL}")
        sys.exit(1)
    log("exit 0 = H46B recorded.  DESI DR2 digits VERIFIED against arXiv:2503.14738 (Table 4 +")
    log("official likelihood files) and arXiv:1807.06209 (Table 2).  Likelihood comparison:")
    log(f"dAIC(fixed A)={daic_fixed:+.2f} (GU disfavored), dAIC(A freed both)={daic_marg:+.2f} (competitive,")
    log("not decisive), free-f0 envelope dAIC=-16.4 (envelope only).  CPL falsification remains headline.")
    sys.exit(0)


if __name__ == "__main__":
    main()
