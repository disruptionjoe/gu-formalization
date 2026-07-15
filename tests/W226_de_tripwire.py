#!/usr/bin/env python3
r"""W226 -- HARDEN the dark-energy AMPLITUDE tripwire + SQUEEZE current data.

This is the standing falsification monitor for GU's dark-energy amplitude axis A4
(canon theta-field-flrw-dark-energy-eos.md, failure mode F1).  It supersedes the
amplitude clause of tests/W220_falsify_dark_energy_vs_desi.py, which is corrected here.

WHAT CANON ACTUALLY SAYS (the quantity the tripwire must check):
  Canon F1 (verbatim): "DESI DR2 or Euclid measures w_a/(w_0+1) < -3.5 at 2-sigma.
  This requires B_i > 3 M_Pl, unphysical in GU."
  So the falsifying event is: a CURRENT admissible measurement EXCLUDES ratio > -3.5
  at 2-sigma, i.e. the LEAST-NEGATIVE (2-sigma) edge of the measured ratio is < -3.5.
  A central value past -3.5 is NOT the canon condition; the 2-sigma edge is.

TWO FRAGILITIES IN W220's fc_d, FIXED HERE:
  (1) W220 used fc_d = (CENTRAL ratio < -3.5) on a single hardcoded BASE row
      (DESI+CMB+DESY5, central -3.468).  Central-only CONTRADICTS canon F1's
      "at 2-sigma" and would SPURIOUSLY FIRE (false GU-falsification) on the
      DESI+CMB+Pantheon+ row, whose CENTRAL ratio is -3.827 while its 2-sigma edge
      is only ~-2.2 (nowhere near excluding -3.5).  See PC-FRAGILITY below.
  (2) The ratio wa/(w0+1) has a POLE at w0 = -1.  As data push w0 -> -1 the central
      ratio blows up while carrying almost no statistical weight.  A central-value
      test is unstable exactly where future data will move.  The 2-sigma-edge
      statistic (with the rho=-0.8 correlation) is pole-robust.

HARDENED FC-d (this test):
  * SCAN every admissible current combination (auto-extensible: add a row to DESI
    and the tripwire covers it -- no BASE to repoint).
  * For each, propagate the FULL correlated (w0,wa) error (rho=-0.8) by deterministic
    Monte-Carlo and take the 2-sigma LEAST-NEGATIVE edge of the ratio.
  * FC-d FIRES iff ANY admissible combination's 2-sigma edge < -3.5 (canon F1 exact).
  * Report (i) the tightest 2-sigma-edge margin = the live FALSIFICATION margin, and
    (ii) the worst CENTRAL-ratio margin = the tension monitor.

SQUEEZE FINDING (part b):  Across the four CURRENT DESI DR2 w0waCDM combinations the
CENTRAL ratio spans -3.02 .. -3.83.  The most stringent CURRENT admissible combination
(DESI+CMB+Pantheon+) already sits at central -3.83, PAST the -3.5 line -- so W220's
"+0.032 margin" was an artifact of choosing the DESY5 row.  BUT at the level canon F1
actually requires (2-sigma), NO combination excludes ratio > -3.5: every 2-sigma edge
is >= ~-2.4, giving a live falsification margin of ~+1.1.  VERDICT: SURVIVES-WITH-TENSION.

PRE-DECLARED FAILURE CONDITION (state, then test):
  GU is FALSIFIED on the DE amplitude axis A4 IFF a CURRENT admissible dataset EXCLUDES
  wa/(w0+1) > -3.5 at 2-sigma (its 2-sigma least-negative edge < -3.5), forcing B_i > 3
  M_Pl.  SURVIVES-WITH-TENSION iff every current admissible 2-sigma edge stays above -3.5;
  report the updated margin.  Only the CHARACTER (amplitude ceiling A4) is falsifiable;
  the fitted shape/epoch (w0,wa point / f0 / B_i) is W160-provably FREE and cannot falsify.

EXIT 0 = falsification did NOT succeed (SURVIVES-WITH-TENSION).  EXIT 1 = a current
admissible dataset excludes ratio > -3.5 at 2-sigma -> GU FALSIFIED on axis A4.
This is a LIVE tripwire: re-run against DESI DR3 / Euclid DR1 digits.

Positive controls run FIRST (incl. a control that PROVES the tripwire fires on a
tight synthetic DR3-like row -- the monitor is live, not vacuous).
Deterministic (seed 20260714).  No network.
Run: python -u tests/W226_de_tripwire.py
"""
from __future__ import annotations
import sys
import numpy as np

FAIL = []
SEED = 20260714


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}", flush=True)
    if not ok:
        FAIL.append(name)


def log(m=""):
    print(m, flush=True)


# ===========================================================================
# CURRENT admissible DE datasets -- DESI DR2 w0waCDM, VERIFIED primary-source
# digits (arXiv:2503.14738 Sec.VII; H3/H46B/W220-verified).  Asymmetric SNe
# errors as printed.  This dict IS the tripwire input: to update for DR3/Euclid,
# add or replace a row -- the scan below covers every row automatically.
# ===========================================================================
DESI_DR2 = {
    "DESI+CMB":           dict(w0=-0.42,  sw0=0.21,  wa=-1.75, swap=0.58, swam=0.58, pref=3.1),
    "DESI+CMB+Pantheon+": dict(w0=-0.838, sw0=0.055, wa=-0.62, swap=0.22, swam=0.19, pref=2.8),
    "DESI+CMB+Union3":    dict(w0=-0.667, sw0=0.088, wa=-1.09, swap=0.31, swam=0.27, pref=3.8),
    "DESI+CMB+DESY5":     dict(w0=-0.752, sw0=0.057, wa=-0.86, swap=0.23, swam=0.20, pref=4.2),
}
RHO_W0WA = -0.8      # declared (w0,wa) correlation, H3/H46B
F1_LINE = -3.5       # canon F1 amplitude kill-line: wa/(w0+1) < -3.5 => B_i > 3 M_Pl
N_MC = 400_000       # MC draws for the 2-sigma edge


def central_ratio(row):
    return row["wa"] / (row["w0"] + 1.0)


def ratio_two_sigma_edge(row, rho=RHO_W0WA, n=N_MC, seed=SEED):
    """Return (central, edge_2s_least_negative, edge_2s_most_negative, p_pole, p_below).

    edge_2s_least_negative = 97.725th percentile of the ratio distribution (the
    2-sigma 'toward zero' edge).  Canon F1 fires iff this edge < F1_LINE, i.e. the
    data EXCLUDE ratio > -3.5 at 2-sigma.  Pole-robust: full correlated error is
    propagated; samples with (w0+1) < 0 (pure-phantom, no crossing) land at the
    least-negative extreme and only make the edge MORE conservative (harder to fire).
    """
    rng = np.random.default_rng(seed)
    w0, wa = row["w0"], row["wa"]
    sw0 = row["sw0"]
    swa = 0.5 * (row["swap"] + row["swam"])
    cov = np.array([[sw0 ** 2, rho * sw0 * swa],
                    [rho * sw0 * swa, swa ** 2]])
    L = np.linalg.cholesky(cov)
    s = np.array([w0, wa])[:, None] + L @ rng.standard_normal((2, n))
    den = s[0] + 1.0
    p_pole = float(np.mean(den <= 0.0))          # fraction with no phantom crossing (w0<-1)
    ratio = s[1] / den
    edge_lo_neg = float(np.percentile(ratio, 97.725))   # least-negative 2-sigma edge
    edge_hi_neg = float(np.percentile(ratio, 2.275))    # most-negative  2-sigma edge
    p_below = float(np.mean(ratio < F1_LINE))
    return central_ratio(row), edge_lo_neg, edge_hi_neg, p_pole, p_below


def fc_d_fires(datasets):
    """Canon-F1 hardened FC-d: fires iff ANY dataset's 2-sigma least-negative edge
    of wa/(w0+1) is below -3.5 (data EXCLUDE ratio > -3.5 at 2-sigma)."""
    fired = []
    for name, row in datasets.items():
        _, edge_lo_neg, _, _, _ = ratio_two_sigma_edge(row)
        if edge_lo_neg < F1_LINE:
            fired.append((name, edge_lo_neg))
    return fired


# ===========================================================================
def main():
    log("=" * 78)
    log("W226 -- HARDEN the DE amplitude tripwire (canon F1) + SQUEEZE current data")
    log("=" * 78)

    # -----------------------------------------------------------------------
    # POSITIVE CONTROLS (first)
    # -----------------------------------------------------------------------
    log("\n" + "-" * 78)
    log("POSITIVE CONTROLS (first)")
    log("-" * 78)

    # PC1 -- DESI DR2 DESY5 digits (recall guard; the W220 BASE row).
    base = DESI_DR2["DESI+CMB+DESY5"]
    check("PC1: DESI DR2 DESY5 digits == arXiv:2503.14738 (w0=-0.752, wa=-0.86, +.23/-.20)",
          base["w0"] == -0.752 and base["sw0"] == 0.057 and base["wa"] == -0.86
          and base["swap"] == 0.23 and base["swam"] == 0.20)

    # PC2 -- reproduce W220's central ratio for the DESY5 BASE row and its +0.032 margin.
    r_desy5 = central_ratio(base)
    check("PC2: reproduce W220 DESY5 central ratio -3.468 and margin +0.032",
          abs(r_desy5 - (-3.468)) < 5e-3 and abs((r_desy5 - F1_LINE) - 0.032) < 5e-3,
          f"central={r_desy5:.3f}, margin={r_desy5 - F1_LINE:+.3f}")

    # PC3 -- canon F1 line and its meaning.
    check("PC3: canon F1 kill-line is wa/(w0+1) < -3.5 (=> B_i > 3 M_Pl, unphysical)",
          F1_LINE == -3.5)

    # PC-FRAGILITY -- DEMONSTRATE why central-only (W220 fc_d) is a bug: the Pantheon+
    # row has central ratio PAST -3.5, yet its 2-sigma edge is nowhere near excluding
    # -3.5.  A central-only test would SPURIOUSLY declare GU falsified on this row.
    pan = DESI_DR2["DESI+CMB+Pantheon+"]
    r_pan, edge_pan, _, ppole_pan, pbel_pan = ratio_two_sigma_edge(pan)
    log(f"  Pantheon+ : central ratio {r_pan:+.3f} (PAST -3.5), 2-sigma least-neg edge "
        f"{edge_pan:+.3f}, P(ratio<-3.5)={pbel_pan:.2f}, P(no-crossing w0<-1)={ppole_pan:.3f}")
    check("PC-FRAGILITY: central-only fc_d (W220) WOULD spuriously fire on Pantheon+ "
          "(central < -3.5) though canon F1 (2-sigma) does NOT -- the bug this test fixes",
          r_pan < F1_LINE and edge_pan > F1_LINE,
          f"central {r_pan:+.3f} < -3.5 but 2s-edge {edge_pan:+.3f} > -3.5")
    check("PC-FRAGILITY-b: the ratio's pole (w0->-1) carries negligible weight here "
          "(<2.3%), so the 2-sigma-edge percentile is well-defined",
          ppole_pan < 0.023, f"P(w0<-1)={ppole_pan:.3f}")

    # PC-LIVE -- PROVE the hardened tripwire actually FIRES on a tight synthetic
    # DR3-like measurement that DOES exclude ratio>-3.5 at 2-sigma.  (Not the real
    # data -- a control that the monitor is live, not vacuous.)
    synth = {"SYNTH-DR3-like (tight, ratio~-4.3)":
             dict(w0=-0.85, sw0=0.020, wa=-0.65, swap=0.06, swam=0.06, pref=6.0)}
    _, edge_synth, _, _, _ = ratio_two_sigma_edge(synth["SYNTH-DR3-like (tight, ratio~-4.3)"])
    fired_synth = fc_d_fires(synth)
    log(f"  SYNTH-DR3-like: central {central_ratio(synth['SYNTH-DR3-like (tight, ratio~-4.3)']):+.3f}, "
        f"2-sigma least-neg edge {edge_synth:+.3f} -> FC-d {'FIRES' if fired_synth else 'silent'}")
    check("PC-LIVE: hardened FC-d FIRES on a tight synthetic row that excludes ratio>-3.5 "
          "at 2-sigma (tripwire is live, exit-1 path exercised)",
          len(fired_synth) == 1 and edge_synth < F1_LINE, f"synth 2s-edge {edge_synth:+.3f}")

    # =======================================================================
    # SQUEEZE -- scan every CURRENT admissible combination (part b).
    # =======================================================================
    log("\n" + "=" * 78)
    log("SQUEEZE -- current DESI DR2 w0waCDM combinations (part b)")
    log("=" * 78)
    log(f"  {'combination':22s} {'pref':>5} {'central':>9} {'cen-margin':>11} "
        f"{'2s-edge(least-neg)':>19} {'edge-margin':>12}")
    rows = {}
    for name, row in DESI_DR2.items():
        cen, edge_lo, edge_hi, ppole, pbel = ratio_two_sigma_edge(row)
        rows[name] = dict(cen=cen, edge_lo=edge_lo, edge_hi=edge_hi, ppole=ppole, pbel=pbel)
        log(f"  {name:22s} {row['pref']:5.1f} {cen:9.3f} {cen - F1_LINE:+11.3f} "
            f"{edge_lo:19.3f} {edge_lo - F1_LINE:+12.3f}")

    # The honest current statistics:
    worst_central_name = min(rows, key=lambda k: rows[k]["cen"])           # most-negative central
    worst_central = rows[worst_central_name]["cen"]
    tightest_edge_name = min(rows, key=lambda k: rows[k]["edge_lo"])       # closest 2-sigma edge to line
    tightest_edge = rows[tightest_edge_name]["edge_lo"]
    log("")
    log(f"  Worst (most-negative) CURRENT central ratio: {worst_central:+.3f} "
        f"({worst_central_name}) -> central margin {worst_central - F1_LINE:+.3f}")
    log(f"  Tightest CURRENT 2-sigma least-negative edge: {tightest_edge:+.3f} "
        f"({tightest_edge_name}) -> LIVE falsification margin {tightest_edge - F1_LINE:+.3f}")

    # SQUEEZE assertions (state the findings as checks):
    check("SQUEEZE-1: current central ratios span past the line -- the most stringent "
          "CURRENT admissible combination (Pantheon+) is already at central < -3.5, so "
          "W220's '+0.032 DESY5 margin' does not describe the whole current dataset",
          worst_central < F1_LINE and worst_central_name == "DESI+CMB+Pantheon+",
          f"worst central {worst_central:+.3f} ({worst_central_name})")
    check("SQUEEZE-2: but at the canon-F1 level (2-sigma) NO current combination excludes "
          "ratio > -3.5 -- every 2-sigma least-negative edge stays above -3.5",
          tightest_edge > F1_LINE,
          f"tightest 2s-edge {tightest_edge:+.3f} > {F1_LINE} ({tightest_edge_name})")
    check("SQUEEZE-3: the updated LIVE falsification margin (tightest 2-sigma edge to the "
          "line) is > +1.0 -- comfortably short of firing at the level F1 requires",
          (tightest_edge - F1_LINE) > 1.0, f"edge margin {tightest_edge - F1_LINE:+.3f}")

    # =======================================================================
    # PRE-DECLARED FAILURE CONDITION -- hardened FC-d over ALL current data.
    # =======================================================================
    log("\n" + "=" * 78)
    log("PRE-DECLARED FAILURE CONDITION (hardened FC-d, canon-F1 exact)")
    log("=" * 78)
    fired = fc_d_fires(DESI_DR2)
    log("  FC-d fires iff ANY current admissible combination EXCLUDES ratio > -3.5 at")
    log("  2-sigma (its 2-sigma least-negative edge < -3.5).  Scan result:")
    for name, row in DESI_DR2.items():
        e = rows[name]["edge_lo"]
        log(f"    {name:22s}: 2s-edge {e:+.3f}  -> {'FIRED' if e < F1_LINE else 'not fired'}")
    check("FC-d does NOT fire: no CURRENT admissible dataset excludes wa/(w0+1) > -3.5 "
          "at 2-sigma -> the amplitude axis A4 is NOT falsified by current data",
          len(fired) == 0, "all current 2-sigma edges above -3.5"
          if not fired else f"FIRED on {fired}")

    # =======================================================================
    # VERDICT
    # =======================================================================
    log("\n" + "=" * 78)
    log("VERDICT")
    log("=" * 78)
    if fired:
        verdict = "FALSIFIED-NOW"
        log(f"  VERDICT = FALSIFIED-NOW on the DE amplitude axis A4: current data exclude")
        log(f"  ratio > -3.5 at 2-sigma.  FIRED: {fired}.  (=> B_i > 3 M_Pl, unphysical in GU.)")
    else:
        verdict = "SURVIVES-WITH-TENSION"
        log(f"  VERDICT = SURVIVES-WITH-TENSION.")
        log(f"  Amplitude axis A4 (the FALSIFIABLE character) SURVIVES: no current admissible")
        log(f"  combination excludes wa/(w0+1) > -3.5 at 2-sigma.  Updated LIVE falsification")
        log(f"  margin = tightest 2-sigma edge {tightest_edge:+.3f} vs -3.5 = "
            f"{tightest_edge - F1_LINE:+.3f} ({tightest_edge_name}).")
        log(f"  TENSION (monitor, central-value): the most stringent current combination")
        log(f"  ({worst_central_name}) is already at central {worst_central:+.3f}, PAST -3.5")
        log(f"  -- worse than W220's DESY5-only +0.032 reading, but only ~1-sigma "
            f"(P(ratio<-3.5)={rows[worst_central_name]['pbel']:.2f}), not the 2-sigma F1 needs.")
        log(f"  The (w0,wa) point / f0 / B_i remain W160-FREE fits; only A4's ceiling is the")
        log(f"  falsifiable content.  RESOLVING RELEASE: DESI DR3 (full 5-yr, ~2027) / Euclid")
        log(f"  DR1 cosmology (~mid-2027) roughly double the (w0,wa) power and will push the")
        log(f"  2-sigma edge toward -3.5.  Re-run this tripwire against those digits.")
    log(f"  RE-RANK: DE amplitude axis A4 = {verdict}.")

    if FAIL:
        log(f"\nFAILED: {FAIL}")
        sys.exit(1)
    log(f"\nexit 0 = W226 recorded.  DE amplitude axis A4: {verdict}.")
    log("         Hardened tripwire live; re-run vs DESI DR3 / Euclid DR1.")
    sys.exit(0)


if __name__ == "__main__":
    main()
