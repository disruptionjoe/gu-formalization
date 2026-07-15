#!/usr/bin/env python3
r"""W220 -- FALSIFICATION test: GU's DERIVED dark-energy CHARACTER vs the DESI DR2 data.

NON-NAIVE falsification.  Method: ASSUME GU is correct and GRANT every unbuilt piece
resolving as GU hopes.  Find where GU is NEVERTHELESS WRONG against the DATA.  Only a
WRONG DEFINITE prediction counts; an unbuilt/undetermined quantity is a GAP, not a
falsification.

The load-bearing move (W160): SEPARATE the DERIVED CHARACTER (a falsifiable prediction)
from the FITTED SHAPE/EPOCH (a free boundary datum).  W160 proved the crossing EPOCH is
PROVABLY free -- the frontier fluctuation two-point function is STATIONARY (its correlation
depends only on the log-count separation, not on the absolute epoch), so pinning the phase
at a specific z requires a non-stationary rank-1 bump that breaks the everpresent amplitude
law.  Deriving the amplitude and deriving the epoch are MUTUALLY EXCLUSIVE.  Therefore the
specific z of crossing (DESI's z~0.405) and the specific (w0,wa) point / f0 / B_i amplitude
are FITS, and CANNOT falsify GU.  Only the DERIVED CHARACTER can.

GU's DERIVED DE CHARACTER (the four falsifiable axes; canon/theta-field-flrw-dark-energy-eos.md
+ W144/W154/W158/W160):
  A1 DYNAMICAL       -- w is not identically -1; the everpresent Lambda fluctuates with
                        amplitude ~ 1/sqrt(N) ~ (l_p/R_H)^2 ~ H^2 (O(1) of rho_crit).
  A2 SIGN-CHANGING   -- the issuance Q = d rho_V / d ln a changes sign +->- (issuance then
                        withdrawal): rho_DE rises then falls (interior maximum), i.e. w
                        crosses -1 with direction PHANTOM-past -> QUINTESSENCE-now.
  A3 CLOCK-COUPLED   -- the fluctuation correlation length is ~ one e-fold ~ one Hubble
                        time, so the crossing, IF present, sits at z = O(1) (not z>>1 nor
                        z<<1).
  A4 AMPLITUDE O(1)  -- |1+w| is O(1)-scale (detectable), bounded above: canon failure
                        condition F1 forbids wa/(w0+1) < -3.5 (that would need B_i > 3 M_Pl,
                        structurally unphysical in GU).

PRE-DECLARED FAILURE CONDITION (state, then test):
  GU is FALSIFIED on the dark-energy leg IF the DESI data CONTRADICT the DERIVED character
  beyond ~3-5 sigma -- specifically IF the data EXCLUDE the sign-changing / clock-coupled
  character, or FORCE a character GU cannot produce:
    FC-a  data force w == -1 exactly (pure Lambda): the character-negating LCDM null is
          FAVORED, not disfavored  -> kills A1/A2.
    FC-b  data force a MONOTONIC rho_DE (no interior maximum, no phantom crossing) -> kills A2.
    FC-c  data force the crossing at z NOT O(1) (z>>1 or z<<1)                     -> kills A3.
    FC-d  data force |1+w| so large that wa/(w0+1) < -3.5 at 2 sigma (B_i > 3 M_Pl)  -> kills A4.
  If NONE of FC-a..d fire, the derived character SURVIVES; the specific-shape miss
  (GU's CPL locus vs the DESI ellipse) is then a STANDING MONITOR on the FITTED shape,
  not a falsification (W160 free-epoch).

EXIT 0  = the falsification did NOT succeed: the derived character SURVIVES-WITH-TENSION,
          and the tension is on the free shape.  EXIT 1 = a character axis was excluded in
          the anti-GU direction beyond the pre-declared level -> GU FALSIFIED on this leg.
          (This test is thus a live falsification tripwire: re-run it against DR3/Euclid.)

Positive controls run FIRST.  Deterministic (seed 20260714).  No network.
Run: python -u tests/W220_falsify_dark_energy_vs_desi.py
"""
from __future__ import annotations
import sys
import numpy as np
from scipy.integrate import solve_ivp, cumulative_trapezoid

FAIL = []
np.random.seed(20260714)


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}", flush=True)
    if not ok:
        FAIL.append(name)


def log(m=""):
    print(m, flush=True)


# ===========================================================================
# DESI DR2 -- VERIFIED primary-source digits (arXiv:2503.14738 Sec.VII / Eq.28;
# H3/H46B-verified).  w0waCDM constraints; asymmetric errors as printed.
# ===========================================================================
DESI = {
    "DESI+CMB":           dict(w0=-0.42,  sw0=0.21,  wa=-1.75, swap=0.58, swam=0.58, pref=3.1),
    "DESI+CMB+Pantheon+": dict(w0=-0.838, sw0=0.055, wa=-0.62, swap=0.22, swam=0.19, pref=2.8),
    "DESI+CMB+Union3":    dict(w0=-0.667, sw0=0.088, wa=-1.09, swap=0.31, swam=0.27, pref=3.8),
    "DESI+CMB+DESY5":     dict(w0=-0.752, sw0=0.057, wa=-0.86, swap=0.23, swam=0.20, pref=4.2),
}
RHO_W0WA = -0.8              # declared (w0,wa) correlation, H3/H46B
BASE = DESI["DESI+CMB+DESY5"]  # the canonical comparison row used by H43/H46/W129


def cpl_w(a, w0, wa):
    return w0 + wa * (1.0 - a)


def rho_de_cpl(a, w0, wa):
    """CPL dark-energy density rho_DE(a)/rho_DE(1)  (exact CPL integral)."""
    return a ** (-3.0 * (1.0 + w0 + wa)) * np.exp(-3.0 * wa * (1.0 - a))


def maha(w0, wa, d=BASE, rho=RHO_W0WA):
    swa = 0.5 * (d["swap"] + d["swam"])
    dv = np.array([w0 - d["w0"], wa - d["wa"]])
    cov = np.array([[d["sw0"] ** 2, rho * d["sw0"] * swa],
                    [rho * d["sw0"] * swa, swa ** 2]])
    return float(np.sqrt(dv @ np.linalg.solve(cov, dv)))


# ===========================================================================
# GU built theta-sector machinery (identical physics to tests/wave20/H43,
# tests/wave19/H42).  DESI-BLIND.  KG on LCDM background from slow-roll IC.
# ===========================================================================
Om, OL = 0.315, 0.685
Z_START = 30.0


def H2(a):
    return Om * a ** -3 + OL


def integrate_theta(M2, z_start=Z_START):
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


def cpl_fit(z, w, zmax=2.0, ngrid=400):
    i = np.argsort(z)
    zs, ws = z[i], w[i]
    zg = np.linspace(0.0, zmax, ngrid)
    wg = np.interp(zg, zs, ws)
    x = zg / (1.0 + zg)
    A = np.vstack([np.ones_like(x), x]).T
    (w0, wa), *_ = np.linalg.lstsq(A, wg, rcond=None)
    return w0, wa


def closest_over_f0(M2, f0s=None):
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
    log("W220 -- FALSIFY the DERIVED dark-energy CHARACTER against DESI DR2")
    log("=" * 78)

    # -----------------------------------------------------------------------
    # POSITIVE CONTROLS (run FIRST) -- reproduce the load-bearing numbers.
    # -----------------------------------------------------------------------
    log("\n" + "-" * 78)
    log("POSITIVE CONTROLS (first)")
    log("-" * 78)

    # PC1 -- DESI DR2 DESY5 digits (recall guard).
    check("PC1: DESI DR2 DESY5 digits == arXiv:2503.14738 (w0=-0.752, wa=-0.86, +.23/-.20)",
          BASE["w0"] == -0.752 and BASE["sw0"] == 0.057 and BASE["wa"] == -0.86
          and BASE["swap"] == 0.23 and BASE["swam"] == 0.20)

    # PC2 -- DESI's OWN best fit HAS the sign-changing character: it crosses w=-1 and its
    #        rho_DE(a) is NON-monotonic with an interior maximum at z=O(1).
    a = np.linspace(0.30, 1.0, 1400)          # z in [0, 2.33]
    w = cpl_w(a, BASE["w0"], BASE["wa"])
    rho = rho_de_cpl(a, BASE["w0"], BASE["wa"])
    # w=-1 crossing:  w0 + wa(1-a*) = -1  ->  a* = 1 + (1+w0)/wa
    a_cross = 1.0 + (1.0 + BASE["w0"]) / BASE["wa"]
    z_cross = 1.0 / a_cross - 1.0
    imax = int(np.argmax(rho))
    z_rho_peak = 1.0 / a[imax] - 1.0
    interior_peak = 0 < imax < len(a) - 1
    log(f"  DESI best-fit w(a): crosses w=-1 at a*={a_cross:.4f} (z={z_cross:.4f}); "
        f"phantom (w<-1) for z>{z_cross:.3f}, quintessence (w>-1) for z<{z_cross:.3f}")
    log(f"  DESI best-fit rho_DE(a): interior MAXIMUM at z={z_rho_peak:.4f} "
        f"(non-monotonic) -> issuance Q=d rho/d ln a changes sign +->-")
    check("PC2: DESI's OWN CPL best fit crosses w=-1 (phantom crossing) at z=O(1)",
          abs(z_cross - 0.405) < 0.01 and 0.0 < z_cross < 2.0, f"z_cross={z_cross:.4f}")
    check("PC2b: DESI's OWN rho_DE(a) is NON-monotonic with an interior maximum "
          "(sign-changing issuance) at z=O(1)",
          interior_peak and 0.0 < z_rho_peak < 2.0, f"peak z={z_rho_peak:.4f}")

    # PC3 -- reproduce GU's canonical theta CPL point and its Mahalanobis to DESI (H43).
    z8, B8, Bd8 = integrate_theta(8.0)
    w0c, wac = cpl_fit(z8, wDE_two_component(z8, B8, Bd8, 0.125, 8.0))
    mj = maha(w0c, wac)
    best8 = closest_over_f0(8.0)
    log(f"  GU canonical (M^2=8, f0=0.125) CPL point = ({w0c:+.4f},{wac:+.4f}); "
        f"joint Mahalanobis to DESI = {mj:.2f} sigma")
    log(f"  GU (M^2=8) closest approach over f0 = {best8[0]:.2f} sigma "
        f"at f0={best8[1]:.3f} -> ({best8[2]:+.4f},{best8[3]:+.4f})")
    check("PC3: GU canonical CPL point reproduces H43 record (-0.768,-0.273)",
          abs(w0c + 0.768) < 3e-3 and abs(wac + 0.273) < 3e-3, f"({w0c:+.4f},{wac:+.4f})")
    check("PC3b: GU canonical joint Mahalanobis reproduces H43 ~4.19 sigma",
          abs(mj - 4.19) < 0.25, f"{mj:.2f} sigma")
    check("PC3c: GU closest-over-f0 reproduces H43 ~3.47 sigma",
          abs(best8[0] - 3.47) < 0.25, f"{best8[0]:.2f} sigma")

    # PC4 -- W160 free-epoch fact, encoded: a STATIONARY fluctuation gives a ~UNIFORM
    #        crossing epoch (no structural pin), so the epoch is a free boundary datum.
    #        (Stationary Gaussian log-count process; the crossing-epoch distribution is
    #        flat in ln a -- reproduces W160 block [FREE].)
    tau = np.linspace(np.log(0.30), 0.0, 240)     # log-count clock ~ ln a
    xi = 0.583                                     # W160 correlation half-width (e-folds)
    dt = tau[:, None] - tau[None, :]
    Cmat = np.exp(-(dt / xi) ** 2)                 # stationary kernel (separation only)
    L = np.linalg.cholesky(Cmat + 1e-10 * np.eye(len(tau)))
    mean_decl = -(tau - tau[0])                    # monotone withdrawal (mean)
    epochs = []
    for _ in range(600):
        f = mean_decl + 1.2 * (L @ np.random.randn(len(tau)))
        s = np.sign(np.diff(f))                    # sign of Q = d Lambda / d ln a
        idx = np.where(np.diff(s) < 0)[0]          # +->- interior maxima
        if len(idx):
            epochs.append(tau[idx[len(idx) // 2]])
    epochs = np.array(epochs)
    # uniformity: no equal-count quartile of the tau-window holds a large majority
    q = np.quantile(tau, [0.0, 0.25, 0.5, 0.75, 1.0])
    frac = [np.mean((epochs >= q[i]) & (epochs < q[i + 1])) for i in range(4)]
    maxfrac = max(frac) if epochs.size else 1.0
    log(f"  W160 free-epoch control: {epochs.size}/600 stationary draws give a +->- crossing; "
        f"crossing-epoch quartile fractions = {[round(x, 2) for x in frac]}")
    check("PC4: stationary (epoch-blind) fluctuation yields interior sign-changes "
          "(the CHARACTER is generic to the structure)",
          epochs.size > 300, f"{epochs.size}/600 draws cross")
    check("PC4b: crossing epoch is ~UNIFORM (no quartile > 45%): the EPOCH is a FREE "
          "boundary datum (W160), not derived -> cannot falsify",
          maxfrac < 0.45, f"max quartile share = {maxfrac:.2f}")

    # =======================================================================
    # CHARACTER CONFRONTATION -- test each derived axis against DESI DR2.
    # For each axis: is the character EXCLUDED (anti-GU) beyond the pre-declared
    # level?  PASS = not excluded (character consistent).
    # =======================================================================
    log("\n" + "=" * 78)
    log("CHARACTER CONFRONTATION (the falsification core)")
    log("=" * 78)

    # --- A1 DYNAMICAL: does the data force w==-1 (LCDM), killing the dynamical character?
    prefs = {k: v["pref"] for k, v in DESI.items()}
    pref_min, pref_max = min(prefs.values()), max(prefs.values())
    log(f"\n  [A1 DYNAMICAL]  DESI preference for dynamical DE (w0waCDM) OVER LCDM (w=-1):")
    for k, v in DESI.items():
        log(f"        {k:20s}: {v['pref']:.1f} sigma")
    log(f"  The character-NEGATING null (pure Lambda, w=-1) is DISFAVORED by DESI at "
        f"{pref_min:.1f}-{pref_max:.1f} sigma.")
    check("A1: FC-a does NOT fire -- data do NOT favor w==-1; the character-negating LCDM "
          "null is disfavored (>=2.8 sigma), so the DYNAMICAL character is not excluded",
          pref_min >= 2.5, f"LCDM disfavored at {pref_min:.1f}-{pref_max:.1f} sigma")

    # --- A2 SIGN-CHANGING: does the data force a MONOTONIC rho_DE (no phantom crossing)?
    # DESI best fit: w0 > -1 AND wa < 0 -> a phantom crossing exists at z in (0,2) (shown PC2).
    has_cross = (BASE["w0"] > -1.0) and (BASE["wa"] < 0.0) and (0.0 < z_cross < 2.0)
    log(f"\n  [A2 SIGN-CHANGING]  DESI best fit w0={BASE['w0']} (> -1) and wa={BASE['wa']} (< 0)")
    log(f"        -> w crosses -1 at z={z_cross:.3f}; rho_DE non-monotonic (PC2).  Direction:")
    log(f"        PHANTOM-past (w<-1) -> QUINTESSENCE-now (w>-1) -- the SAME +->- issuance")
    log(f"        direction GU's q=5 Krein sign-pin forces (W158).")
    check("A2: FC-b does NOT fire -- DESI does NOT force a monotonic rho_DE; its own best "
          "fit is sign-changing with GU's phantom->quintessence direction",
          has_cross, f"z_cross={z_cross:.3f}, w0={BASE['w0']}, wa={BASE['wa']}")

    # --- A3 CLOCK-COUPLED: is the crossing at z NOT O(1) (would kill clock coupling)?
    log(f"\n  [A3 CLOCK-COUPLED]  DESI crossing epoch z={z_cross:.3f} is O(1) "
        f"(in [0,2], ~ one Hubble time back).")
    check("A3: FC-c does NOT fire -- the DESI crossing sits at z=O(1), consistent with GU's "
          "~one-e-fold (Hubble-time) correlation length",
          0.05 < z_cross < 2.0, f"z_cross={z_cross:.3f}")

    # --- A4 AMPLITUDE O(1) / F1 ceiling: does the data force wa/(w0+1) < -3.5 (B_i>3 M_Pl)?
    # NOTE (W226): this central-value fc_d is SUPERSEDED for the standing amplitude tripwire by
    # tests/W226_de_tripwire.py, which tests the canon-F1 quantity (2-sigma least-negative edge
    # over ALL admissible current combinations, not one BASE central value). Central-only fc_d
    # would spuriously fire on DESI+CMB+Pantheon+ (central -3.83) though F1's 2-sigma condition
    # is not met. This block is retained for W220's record; see W226 for the hardened monitor.
    ratio = BASE["wa"] / (BASE["w0"] + 1.0)
    # 2-sigma most-negative excursion of the ratio (marginal, conservative): push wa down,
    # w0 toward -1 by their 1-sigma errors * 2 (correlation rho=-0.8 makes them co-vary the
    # OTHER way, so this marginal bound is conservative / over-estimates how negative it gets).
    wa_lo = BASE["wa"] - 2.0 * BASE["swap"]
    w0_hi = BASE["w0"] - 2.0 * BASE["sw0"]        # toward -1 -> (w0+1) smaller -> ratio more neg
    ratio_2s = wa_lo / (w0_hi + 1.0) if (w0_hi + 1.0) > 0 else -np.inf
    F1_LINE = -3.5
    log(f"\n  [A4 AMPLITUDE O(1)]  canon F1 kill-line: wa/(w0+1) < {F1_LINE} (needs B_i>3 M_Pl).")
    log(f"        DESI central ratio wa/(w0+1) = {ratio:.3f}  (margin to F1 = {ratio - F1_LINE:+.3f})")
    log(f"        naive 2-sigma most-negative marginal ratio ~ {ratio_2s:.2f} "
        f"(rho=-0.8 makes this conservative)")
    check("A4: FC-d does NOT fire -- the DESI central ratio wa/(w0+1) is NOT below the F1 "
          "kill-line -3.5; the amplitude the data want stays within GU's O(1)/B_i ceiling",
          ratio > F1_LINE, f"ratio={ratio:.3f} vs F1={F1_LINE} (margin {ratio - F1_LINE:+.3f})")

    # =======================================================================
    # PRE-DECLARED FAILURE CONDITION -- evaluate.
    # =======================================================================
    log("\n" + "=" * 78)
    log("PRE-DECLARED FAILURE CONDITION -- evaluation")
    log("=" * 78)
    fc_a = pref_min < 2.5                      # data favor w=-1
    fc_b = not has_cross                       # data force monotonic rho_DE
    fc_c = not (0.05 < z_cross < 2.0)          # crossing not O(1)
    fc_d = ratio < F1_LINE                     # amplitude forces B_i>3 M_Pl
    any_fc = fc_a or fc_b or fc_c or fc_d
    log(f"  FC-a  data favor w==-1 (kills A1/A2)          : {'FIRED' if fc_a else 'not fired'}")
    log(f"  FC-b  data force monotonic rho_DE (kills A2)  : {'FIRED' if fc_b else 'not fired'}")
    log(f"  FC-c  crossing not O(1) (kills A3)            : {'FIRED' if fc_c else 'not fired'}")
    log(f"  FC-d  ratio < -3.5, B_i>3 M_Pl (kills A4)     : {'FIRED' if fc_d else 'not fired'}")
    check("FAILURE CONDITION does NOT fire: no character axis is excluded in the anti-GU "
          "direction -> the derived character is NOT falsified by DESI DR2",
          not any_fc, "all four FC clauses clear")

    # =======================================================================
    # THE STANDING TENSION (monitor) -- on the FITTED shape, not the character.
    # =======================================================================
    log("\n" + "=" * 78)
    log("STANDING TENSION (monitor; attaches to the FREE shape, not the character)")
    log("=" * 78)
    log(f"  GU's specific CPL locus misses the DESI ellipse: {best8[0]:.2f} sigma (closest over")
    log(f"     f0) / {mj:.2f} sigma (canonical f0=0.125).  W129: the CMB-calibrated theta")
    log(f"     distance model is excluded at dchi^2 >= +33.5 at DESI-signal amplitudes,")
    log(f"     band-wide over the OQ2 M^2 set.")
    log(f"  PER W160 the crossing EPOCH and the (w0,wa) point are FITTED boundary data")
    log(f"     (provably free), so this {best8[0]:.1f}-{mj:.1f} sigma miss is a MONITOR on the")
    log(f"     FREE shape, NOT a falsification of the derived character.")
    log(f"  LIVE TRIPWIRE: DESI DR2 ratio {ratio:.3f} sits {abs(ratio - F1_LINE):.2f} from the")
    log(f"     F1 kill-line -3.5.  If DR3/Euclid push wa more negative or w0 toward -1 so the")
    log(f"     ratio crosses -3.5 at 2 sigma, FC-d fires and A4 (amplitude) is FALSIFIED.")
    # sanity: the tension is real and >3 sigma (so we are not hiding a null result)
    check("MONITOR: the fitted-shape tension is real and > 3 sigma (reported honestly, not "
          "buried) -- SURVIVES-WITH-TENSION, not a clean survive",
          best8[0] > 3.0, f"shape-miss {best8[0]:.2f} sigma")

    # =======================================================================
    # VERDICT
    # =======================================================================
    log("\n" + "=" * 78)
    log("VERDICT")
    log("=" * 78)
    if any_fc:
        verdict = "FALSIFIED"
        log("  VERDICT = FALSIFIED on the dark-energy leg: a character axis is excluded in the")
        log("  anti-GU direction beyond the pre-declared level.  See the FIRED FC clause above.")
    else:
        verdict = "SURVIVES-WITH-TENSION"
        log("  VERDICT = SURVIVES-WITH-TENSION.")
        log("  PREDICTION (derived character) -- SURVIVES: DESI DR2 does not exclude and in fact")
        log("    CORROBORATES the sign-changing / clock-coupled / O(1)~H^2 character.  The")
        log("    character-negating LCDM null is disfavored at 2.8-4.2 sigma; DESI's own best fit")
        log("    is a phantom crossing at z=O(1) in GU's phantom->quintessence direction; the")
        log("    amplitude ratio -3.47 stays above the F1 kill-line -3.5.  FAILURE CONDITION does")
        log("    not fire.")
        log("  FIT (specific shape/epoch, PROVABLY FREE per W160) -- MISSES at 3.47 sigma (closest)")
        log("    / 4.19 sigma (canonical f0) and W129 dchi^2>=+33.5: a STANDING MONITOR on the free")
        log("    shape, not a falsification.  Sharpest live tripwire: ratio -3.47 vs F1 -3.5.")
    log(f"  RE-RANK: dark-energy leg = {verdict}.")

    if FAIL:
        log(f"\nFAILED: {FAIL}")
        sys.exit(1)
    log(f"\nexit 0 = W220 recorded.  Dark-energy leg: {verdict}.  Character not falsified by")
    log("         DESI DR2; the 3.47-4.19 sigma tension is on the W160-free shape (a monitor).")
    sys.exit(0)


if __name__ == "__main__":
    main()
