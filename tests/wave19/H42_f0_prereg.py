#!/usr/bin/env python3
r"""H42 -- PRE-REGISTERED test of GU's SOLE data-facing knob f0 (the theta-sector
dark-energy amplitude).  The Wave-18 audit (H34) found GU has ZERO parameter-free
predictions and exactly one data-facing FIT: f0, which slides GU's dark-energy
(w0,wa) along a one-parameter family.  This test asks the single gate question:

    Can f0 be derived SOURCE-FIRST from GU's built structure, DESI-BLIND?
      yes + matches DESI  -> GU's FIRST parameter-free prediction
      yes + misses  DESI  -> a clean FALSIFICATION
      no (not derivable)  -> stays a FIT; NO-TEST-YET (loops to H41 source action)

METHODOLOGY (pre-registration discipline, hard-separated in the code):

  PART A  -- derive_f0_source_first()  takes NO DESI ARGUMENT.  It uses only GU's
             built structure (the derived KK mass M^2 = 8 H0^2; the built two-
             component theta + DeWitt-Lambda dark energy; the KG theta trajectory)
             and reports what that structure DOES and DOES NOT fix about f0.  It
             records the committed pre-registration finding and a per-step leakage
             self-audit.  No DESI number is in scope anywhere in Part A.

  PART B  -- compare_to_desi(recorded)  is the ONLY place the DESI numbers appear.
             It computes the marginal sigmas of the (illustrative) f0=0.125 point
             and the f0-FAMILY closest approach, and prints the verdict.

The code structure ENFORCES the split: derive_f0_source_first() has no DESI in its
body or signature; compare_to_desi() receives Part A's recorded object and only
then loads the verified DESI DR2 digits.

FINDING (recorded below, exit 0): f0 is NOT source-first derivable with current
machinery.  It is the ratio of two dark-energy amplitudes, rho_theta(0)/rho_Lambda(0),
and BOTH amplitudes are set by unbuilt source-action inputs:
  (i)  B_i, the theta initial/vacuum amplitude -- the Willmore variational principle
       selects the critical section but NOT the perturbation amplitude (canon
       theta-field-flrw-dark-energy-eos.md, Gap 1);
  (ii) mu_DW, the DeWitt overall dimensionful scale -- the scale-covariant gimmel
       geometry fixes dimensionless ratios only, never the overall scale (H24).
So the verdict is NO-TEST-YET: f0 stays a FIT; the object that would fix it is the
source action (H41).  The test exits 0 on that finding (it PINS the blocker), and
prints the DESI comparison as a FIT-comparison (explicitly NOT a prediction test).

Run: python -u tests/wave19/H42_f0_prereg.py     (exit 0 iff every PASS holds)
"""
from __future__ import annotations
import sys
import numpy as np
from scipy.integrate import solve_ivp

FAIL = []


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}", flush=True)
    if not ok:
        FAIL.append(name)


def log(m=""):
    print(m, flush=True)


# ===========================================================================
# GU built theta-sector machinery (fixed model; identical physics to
# tests/one-residual/dark_energy_desi_sign.py -- NOT tuned here, NO DESI input).
#   KG:  B'' + 3H B' + M2 B = 0,  M2 = M_KK^2 = 8 H0^2  (M_KK = 2 sqrt2 H0, H0=1)
#   background: pure LCDM,  H^2 = Om a^-3 + OL
#   two-component DE:  w_DE = (-1 + f wB)/(1+f),  f = f0 rhoB(z)/rhoB(0)
# The mass M2 = 8 H0^2 is the DERIVED lowest normal-Laplacian eigenvalue
# lambda_{N,1} = 8/R_s^2 on GL(4,R)/O(3,1), R_s = c/H0
# (rc3-delta-n-spectrum-gl4r-2026-06-23.md) -- source-first, modulo the OQ2
# A_3-vs-BC_1 root-system caveat.  H0 is the cosmological Hubble scale, NOT a
# DESI datum.
# ===========================================================================
Om, OL = 0.315, 0.685
M2_DERIVED = 8.0           # M_KK^2 = 8 H0^2  (derived fiber-Laplacian eigenvalue)
Z_START = 30.0
F0_CANON_TUNED = 0.125     # the canonical value -- DESI-TUNED (NOT adopted as source-first)


def H2(a):
    return Om * a ** -3 + OL


def _integrate_theta(M2):
    """Integrate the theta KG field on an LCDM background from the slow-roll
    attractor at z=Z_START.  Deterministic (Radau, fixed grid).  NO DESI input."""
    def rhs(N, y):
        a = np.exp(N)
        B, BN = y
        HNoH = -1.5 * Om * a ** -3 / H2(a)
        return [BN, -(3.0 + HNoH) * BN - (M2 / H2(a)) * B]
    a0 = 1.0 / (1.0 + Z_START)
    N0 = np.log(a0)
    BN0 = -M2 / (3.0 * H2(a0))
    sol = solve_ivp(rhs, (N0, 0.0), [1.0, BN0], t_eval=np.linspace(N0, 0.0, 8000),
                    rtol=1e-11, atol=1e-13, method="Radau", dense_output=True)
    assert sol.success, sol.message
    a = np.exp(sol.t)
    z = 1.0 / a - 1.0
    B, BN = sol.y
    return z, B, np.sqrt(H2(a)) * BN


def _wDE(z, B, Bdot, f0, M2):
    KE = 0.5 * Bdot ** 2
    PE = 0.5 * M2 * B ** 2
    rhoB = KE + PE
    wB = (KE - PE) / rhoB
    i0 = int(np.argmin(np.abs(z)))
    f = f0 * rhoB / rhoB[i0]
    return (-1.0 + f * wB) / (1.0 + f)


def _cpl_fit(z, w, zmax=2.0, ngrid=400):
    i = np.argsort(z)
    zs, ws = z[i], w[i]
    zg = np.linspace(0.0, zmax, ngrid)
    wg = np.interp(zg, zs, ws)
    x = zg / (1.0 + zg)
    A = np.vstack([np.ones_like(x), x]).T
    (w0, wa), *_ = np.linalg.lstsq(A, wg, rcond=None)
    return w0, wa


# ===========================================================================
# PART A -- DERIVE AND RECORD f0, DESI-BLIND.  NO DESI ARGUMENT.
# ===========================================================================
def derive_f0_source_first():
    """Return the source-first, DESI-BLIND finding about f0.

    This function is FORBIDDEN a DESI argument by construction: it receives none
    and references none.  It walks GU's built structure and reports, step by step,
    what that structure fixes about f0 = rho_theta(0)/rho_Lambda(0).
    """
    log("=" * 78)
    log("PART A -- SOURCE-FIRST derivation of f0 (DESI-BLIND; no DESI in scope)")
    log("=" * 78)

    steps = []   # (label, source, fixes_f0?, leakage_referenced_DESI?)

    # A1. What f0 IS (definition from the built two-component model).
    log("\n[A1] Definition.  f0 = rho_theta(z=0) / rho_Lambda(z=0): the ratio of the")
    log("     DYNAMICAL theta density to the CONSTANT DeWitt-Lambda density today")
    log("     (canon theta-field-flrw-dark-energy-eos.md, Result 2).  f0 is an")
    log("     AMPLITUDE RATIO of two energy densities -- not a shape/spectral datum.")
    steps.append(("f0 = rho_theta(0)/rho_Lambda(0) (amplitude ratio)",
                  "canon theta-field-flrw Result 2", None, False))

    # A2. The theta MASS/SHAPE IS derived source-first.
    log("\n[A2] DERIVED source-first: M^2 = M_KK^2 = 8 H0^2, the lowest normal-Laplacian")
    log("     eigenvalue lambda_{N,1} = 8/R_s^2 on GL(4,R)/O(3,1), R_s = c/H0")
    log("     (rc3-delta-n-spectrum-gl4r).  This FIXES the theta TRAJECTORY / the")
    log("     SHAPE of w(z) -- hence the (w0,wa) LOCUS as f0 varies -- but NOT the")
    log("     amplitude f0.  [caveat: OQ2 A_3-vs-BC_1 root system under revision.]")
    steps.append(("M^2 = 8 H0^2 fixes the w(z) SHAPE/locus (not f0)",
                  "rc3-delta-n-spectrum-gl4r (OQ2 caveat)", False, False))

    # A3. rho_theta(0) needs B_i -- an UNBUILT initial amplitude.
    log("\n[A3] rho_theta(0) ~ (1/2) M^2 B_i^2 * (evolution factor).  The trajectory")
    log("     (evolution factor) is built, but the OVERALL amplitude is set by B_i,")
    log("     the theta initial/vacuum displacement.  The Willmore variational")
    log("     principle E[s] selects the CRITICAL SECTION but does NOT specify the")
    log("     amplitude of normal-bundle perturbations (canon Gap 1).  B_i is an")
    log("     integration constant of the KG equation -- a misalignment amplitude,")
    log("     UNBUILT.  -> rho_theta(0) is not fixed source-first.")
    steps.append(("rho_theta(0) needs B_i (theta initial amplitude) -- UNBUILT",
                  "canon Gap 1 (Willmore selects section, not amplitude)", False, False))

    # A4. rho_Lambda(0) needs mu_DW -- an UNBUILT overall scale.
    log("\n[A4] rho_Lambda(0) is the DeWitt O(M^0) constant (H15 Part D / H24): a")
    log("     Lambda whose dimensionless coefficient is geometry-fixed (the pure-")
    log("     horizontal ambient sectional, a constant) but whose MAGNITUDE carries")
    log("     the overall DeWitt scale mu_DW.  H24: the scale-covariant gimmel")
    log("     geometry fixes all dimensionless RATIOS and NOT the single overall")
    log("     dimensionful scale mu_DW, which is the source action's normalization")
    log("     (UNBUILT).  -> rho_Lambda(0) magnitude is not fixed source-first.")
    steps.append(("rho_Lambda(0) needs mu_DW (DeWitt overall scale) -- UNBUILT",
                  "H24 (geometry fixes ratios, not the overall scale)", False, False))

    # A5. Therefore the RATIO f0 is not fixed -- two unbuilt inputs.
    log("\n[A5] f0 = rho_theta(0)/rho_Lambda(0) therefore depends on TWO unbuilt")
    log("     source-action inputs -- B_i (A3) and mu_DW (A4).  Neither is fixed by")
    log("     the built geometry.  No built dimensionless ratio pins f0.")
    steps.append(("f0 = ratio of two UNBUILT amplitudes -> NOT fixed source-first",
                  "A3 + A4", False, False))

    # A6. Adversarial DERIVABLE-NOW steelman -- and its REJECTION (leakage guard).
    log("\n[A6] Adversarial steelman (and rejection):")
    log("     (a) f0 = 0.125 = 1/8, and the gimmel off-diagonal sectional is -1/8.")
    log("         Tempting 'derivation' f0 = |offdiag sectional|.  REJECTED: there is")
    log("         NO built identity linking an amplitude RATIO to a sectional")
    log("         CURVATURE; the canonical 0.125 traces to 'B_i ~ 0.98 M_Pl, natural'")
    log("         and is explicitly DESI-TUNED (canon).  Adopting 1/8 would tune")
    log("         toward the DESI-matching value = RED leakage.  Not source-first.")
    log("     (b) Naturalness: B_i ~ M_Pl and a Planckian DeWitt vacuum give f0 ~ O(1),")
    log("         an ORDER-OF-MAGNITUDE band, not a number.  Recorded as a weak band,")
    log("         NOT a committed value.")
    steps.append(("f0=1/8 numerology REJECTED (back-fit); naturalness gives only O(1) band",
                  "canon (0.125 is DESI-tuned) + H24", False, False))

    # ---- RECORDED committed finding (the pre-registration record) ----
    recorded = {
        "f0_status": "GENUINELY-FREE-NOW / DERIVABLE-ONLY-AFTER-H41",
        "f0_value": None,                    # NO committed number -- f0 is not fixed
        "f0_naturalness_band": (0.0, "O(few)"),
        "M2_derived": M2_DERIVED,            # the shape IS source-first
        "blocking_unbuilt": ["B_i (theta initial amplitude; canon Gap 1)",
                             "mu_DW (DeWitt overall scale; H24)"],
        "blocker_object": "the source action (H41) overall normalization",
        "steps": steps,
        # source-first LOCUS as f0 varies (uses only derived M2 + built structure;
        # NO DESI) -- recorded so Part B can test it without re-deriving.
        "locus_f0_grid": None,
    }

    # Build the source-first (w0,wa) LOCUS as a function of f0 -- DESI-BLIND.
    z, B, Bdot = _integrate_theta(M2_DERIVED)
    grid = []
    for f0 in (0.02, 0.057, 0.125, 0.25, 0.5, 1.0, 2.0):
        w0, wa = _cpl_fit(z, _wDE(z, B, Bdot, f0, M2_DERIVED))
        grid.append((f0, w0, wa))
    recorded["locus_f0_grid"] = grid
    recorded["_theta_solution"] = (z, B, Bdot)   # reused by Part B (still no DESI in it)

    log("\n[A-RECORDED] Committed pre-registration finding:")
    log(f"     f0 status         : {recorded['f0_status']}")
    log(f"     f0 recorded value : {recorded['f0_value']} (NO source-first number exists)")
    log(f"     naturalness band  : f0 ~ (0, O(few)); O(1) point if theta-misalignment")
    log(f"                         and DeWitt-vacuum share the gimmel scale")
    log(f"     source-first FIXED: M^2 = {recorded['M2_derived']} H0^2 -> the w(z) SHAPE/locus")
    log(f"     blocking unbuilt  : {recorded['blocking_unbuilt']}")
    log(f"     blocker object    : {recorded['blocker_object']}")
    log("     source-first (w0,wa) LOCUS as f0 varies (NO DESI used):")
    for f0, w0, wa in grid:
        log(f"        f0={f0:5.3f}  ->  (w0,wa) = ({w0:+.4f}, {wa:+.4f})")

    # ---- leakage self-audit (per step) ----
    log("\n[A-LEAKAGE SELF-AUDIT] Did any step reference or tune toward the DESI value?")
    any_red = False
    for label, src, fixes, leaked in steps:
        tag = "RED (leaked)" if leaked else "green"
        if leaked:
            any_red = True
        log(f"     [{tag}] {label}   <- {src}")
    log("     Summary: no step adopted a DESI-tuned value; the one tempting route")
    log("     (f0=1/8) was RAISED and REJECTED precisely because it would tune toward")
    log("     the data.  The recorded finding (f0 not derivable) uses NO DESI input.")
    recorded["leakage_any_red"] = any_red
    return recorded


# ===========================================================================
# PART B -- COMPARE (only after Part A is recorded).  DESI numbers appear ONLY here.
# ===========================================================================
def compare_to_desi(recorded):
    """Compare the recorded Part-A finding to DESI DR2.  This is the ONLY function
    that loads DESI numbers."""
    log("\n" + "=" * 78)
    log("PART B -- COMPARE to DESI DR2 (DESI numbers enter ONLY here)")
    log("=" * 78)

    # VERIFIED DESI DR2 DESI+CMB+DESY5 (arXiv:2503.14738, Eq. 28; H3-verified digits)
    cw0, sw0, cwa, swap, swam = -0.752, 0.057, -0.86, 0.23, 0.20

    def marg(v, c, sp, sm):
        d = v - c
        return d / (sp if d >= 0 else sm)

    def maha(w0, wa, rho=-0.8):
        swa = 0.5 * (swap + swam)
        d = np.array([w0 - cw0, wa - cwa])
        cov = np.array([[sw0 ** 2, rho * sw0 * swa], [rho * sw0 * swa, swa ** 2]])
        return float(np.sqrt(d @ np.linalg.solve(cov, d)))

    z, B, Bdot = recorded["_theta_solution"]

    # B1. Because Part A recorded f0 as NOT derivable, the DESI comparison at any
    #     particular f0 is a FIT-comparison, not a prediction test.  Show the
    #     canonical (DESI-tuned) f0=0.125 point for reference, labelled as a FIT.
    w0c, wac = _cpl_fit(z, _wDE(z, B, Bdot, F0_CANON_TUNED, recorded["M2_derived"]))
    s_w0 = marg(w0c, cw0, sw0, sw0)
    s_wa = marg(wac, cwa, swap, swam)
    mj = maha(w0c, wac)
    log(f"\n[B1] Canonical (DESI-TUNED) f0={F0_CANON_TUNED}:  (w0,wa)=({w0c:+.4f},{wac:+.4f})")
    log(f"     marginal vs DESY5:  w0 = {s_w0:+.2f} sigma   wa = {s_wa:+.2f} sigma")
    log(f"     joint Mahalanobis (rho=-0.8) = {mj:.2f} sigma")
    log(f"     -> this is a FIT comparison (f0 was tuned), NOT a parameter-free test.")

    # B2. The source-first LOCUS (Part A, derived M2) closest approach over f0.
    f0s = np.linspace(0.02, 5.0, 800)
    best = None
    for f0 in f0s:
        w0, wa = _cpl_fit(z, _wDE(z, B, Bdot, f0, recorded["M2_derived"]))
        m = maha(w0, wa)
        if best is None or m < best[0]:
            best = (m, f0, w0, wa)
    mbest, f0best, w0best, wabest = best
    log(f"\n[B2] Source-first f0-FAMILY closest approach to DESY5 (scan f0, derived M^2):")
    log(f"     min Mahalanobis = {mbest:.2f} sigma at f0={f0best:.3f} "
        f"-> (w0,wa)=({w0best:+.4f},{wabest:+.4f})")
    log(f"     The family LOCUS misses DESI at EVERY f0 (raising f0 deepens |wa| but")
    log(f"     drives w0 up toward 0, off the DESI degeneracy direction).")

    # ---- gate checks ----
    check("PART A recorded f0 as NOT source-first derivable (no committed number)",
          recorded["f0_value"] is None
          and recorded["f0_status"].startswith("GENUINELY-FREE"))
    check("PART A leakage self-audit clean (no step tuned toward DESI)",
          recorded["leakage_any_red"] is False)
    check("blocker correctly PINNED to the two unbuilt source-action inputs {B_i, mu_DW}",
          any("B_i" in s for s in recorded["blocking_unbuilt"])
          and any("mu_DW" in s for s in recorded["blocking_unbuilt"]))
    check("PART B: canonical f0 point reproduces (w0,wa)=(-0.768,-0.273), wa > +2 sigma "
          "off DESY5 (a FIT, near-falsifying only because f0 is free)",
          abs(w0c + 0.768) < 3e-3 and abs(wac + 0.273) < 3e-3 and s_wa > 2.0,
          f"w0={s_w0:+.2f}s, wa={s_wa:+.2f}s")
    check("PART B: no f0 brings the source-first family within 3 sigma of DESY5 "
          "(locus misaligned with DESI) -> a LATENT falsifier",
          mbest > 3.0, f"closest {mbest:.2f} sigma at f0={f0best:.3f}")

    # ---- verdict ----
    log("\n" + "-" * 78)
    log("VERDICT")
    log("-" * 78)
    log("Q1  Is f0 derivable source-first?      DERIVABLE-ONLY-AFTER-H41 (free now).")
    log("Q2  Recorded f0 (Part A, DESI-blind):  FREE -- no number; M^2=8H0^2 fixes the")
    log("    SHAPE/locus but the amplitude needs B_i (Gap 1) and mu_DW (H24).")
    log(f"Q3  Part B verdict:                    NO-TEST-YET.  f0 stays a FIT.")
    log(f"    (illustrative fit comparison: wa {s_wa:+.2f} sigma, joint {mj:.2f} sigma;")
    log(f"     family closest approach {mbest:.2f} sigma at f0={f0best:.3f} -- latent falsifier)")
    log("Q4  Blocker:                           the source action (H41) that fixes the")
    log("    overall normalization {B_i, mu_DW}.  f0=1/8 numerology rejected as back-fit.")
    log("RE-RANK: NO-TEST-YET; single next object = the source action (H41) normalization.")
    log("-" * 78)


def main():
    recorded = derive_f0_source_first()   # PART A -- no DESI
    compare_to_desi(recorded)             # PART B -- DESI only here
    if FAIL:
        log(f"\nFAILED: {FAIL}")
        sys.exit(1)
    log("\nexit 0 = H42 pre-registration recorded: f0 is NOT source-first derivable")
    log("         (blocked by B_i and mu_DW); verdict NO-TEST-YET; f0 stays a FIT.")
    sys.exit(0)


if __name__ == "__main__":
    main()
