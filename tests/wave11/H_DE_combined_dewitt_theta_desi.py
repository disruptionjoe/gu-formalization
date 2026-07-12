"""Combined GU dark energy: DeWitt-Lambda (B-thread) + theta-sector (C-thread) vs DESI DR2.

THE COUNCIL QUESTION (wild-card possibility for the DESI tension). GU has TWO computed dark-energy pieces we
have only ever tested SEPARATELY:
  (1) theta-sector (C-thread / H3): an evolving component, CPL fit (w0, wa) = (-0.768, -0.273) at f0=0.125.
      NAILS DESI w0 but UNDER-evolves |wa| (DESI: wa ~ -0.86) -> the whole 1-param family sits ~3-4 sigma off.
  (2) O(M^0) DeWitt background (B-thread, tests/threads/B_constant_section_background_curvature.py): a CONSTANT
      Lambda-shaped piece (fiber-trace = (1/2) eta_mn), i.e. an ordinary w=-1 cosmological constant.
Does the COMBINATION (constant Lambda + evolving theta) give a steeper/better effective wa that fits DESI
better than theta-alone? This test COMPUTES it -- no pre-judging -- and states CLEAR / NO-HELP / WORSE.

METHOD (standard two-component dark energy).
- theta density (CPL): rho_theta(a)/rho_theta0 = a^{-3(1+w0+wa)} * exp(-3 wa (1-a)).
- Lambda density: rho_L(a) = const.
- mixing fraction f = rho_L0 / rho_DE0 at z=0 (scanned 0..1); rho_theta0 = (1-f) rho_DE0.
- effective EOS (energy-weighted): w_eff(a) = [rho_L*(-1) + rho_theta*w_theta(a)] / rho_tot(a).
- fit w_eff(a) over the DESI window z in [0,2] to CPL (w0_eff, wa_eff) by least squares in (1-a).
- distance to DESI+CMB+DESY5 (w0,wa) = (-0.752, -0.86), sigma_w0=0.057, sigma_wa~0.21 (H3, arXiv:2503.14738);
  marginal sigmas + an approx joint Mahalanobis (rho scanned).

ADVERSARIAL (the philosopher's guard -- this must be a computation, not a rescue):
- report whether the combination HELPS or HURTS (do not assume the wild-card intuition is right);
- flag the DOUBLE-COUNTING caveat: if the DeWitt-Lambda is actually the theta VACUUM VALUE (not an
  independent component), the additive combination is INVALID -- the computation cannot settle this;
  it needs the built theta dynamics. Report the result CONDITIONAL on independence.

Run: python tests/wave11/H_DE_combined_dewitt_theta_desi.py
"""
from __future__ import annotations

import numpy as np

# --- theta-sector CPL (C-thread / H3) ---
W0_TH, WA_TH = -0.768, -0.273
# --- DESI DR2 DESI+CMB+DESY5 target (H3, arXiv:2503.14738) ---
W0_DESI, WA_DESI = -0.752, -0.86
SIG_W0, SIG_WA = 0.057, 0.21   # wa error symmetrized from +0.23/-0.20

FAIL = []


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)


def cpl_density(a, w0, wa):
    """rho_DE(a)/rho_DE0 for CPL w(a)=w0+wa(1-a)."""
    return a ** (-3.0 * (1.0 + w0 + wa)) * np.exp(-3.0 * wa * (1.0 - a))


def w_theta(a):
    return W0_TH + WA_TH * (1.0 - a)


def w_eff_combined(a, f):
    """Energy-weighted effective EOS of [Lambda (fraction f) + theta (1-f)] at scale factor a."""
    rho_L = f * np.ones_like(a)                      # constant
    rho_th = (1.0 - f) * cpl_density(a, W0_TH, WA_TH)
    rho_tot = rho_L + rho_th
    return (rho_L * (-1.0) + rho_th * w_theta(a)) / rho_tot


def fit_cpl(f):
    """Least-squares CPL (w0_eff, wa_eff) fit of w_eff_combined over z in [0,2]."""
    z = np.linspace(0.0, 2.0, 400)
    a = 1.0 / (1.0 + z)
    w = w_eff_combined(a, f)
    x = 1.0 - a                                      # CPL basis: w = w0 + wa * x
    A = np.vstack([np.ones_like(x), x]).T
    (w0e, wae), *_ = np.linalg.lstsq(A, w, rcond=None)
    return w0e, wae


def joint_sigma(w0e, wae, rho):
    dw0 = (w0e - W0_DESI) / SIG_W0
    dwa = (wae - WA_DESI) / SIG_WA
    # Mahalanobis with correlation rho
    m2 = (dw0 ** 2 - 2 * rho * dw0 * dwa + dwa ** 2) / (1 - rho ** 2)
    return np.sqrt(max(m2, 0.0)), dw0, dwa


def main():
    print("[combined DeWitt-Lambda + theta dark energy vs DESI DR2]\n")
    print(f"    theta-alone (f=0):    (w0,wa) = ({W0_TH:+.3f}, {WA_TH:+.3f})")
    print(f"    DESI DR2 target:      (w0,wa) = ({W0_DESI:+.3f}, {WA_DESI:+.3f})  "
          f"sig=({SIG_W0},{SIG_WA})\n")

    rho = -0.8   # representative DESI w0-wa correlation (scanned below)
    fs = np.linspace(0.0, 0.98, 50)
    best = None
    print("    f_Lambda | w0_eff  wa_eff |  dw0_sig dwa_sig  joint_sig")
    for f in fs:
        w0e, wae = fit_cpl(f)
        s, dw0, dwa = joint_sigma(w0e, wae, rho)
        if best is None or s < best[0]:
            best = (s, f, w0e, wae, dw0, dwa)
        if abs(f - round(f, 1)) < 0.011:   # print at f = 0.0,0.1,...
            print(f"      {f:5.2f}  | {w0e:+.3f} {wae:+.3f} |  {dw0:+6.2f} {dwa:+6.2f}   {s:6.2f}")

    s0, dw00, dwa0 = joint_sigma(W0_TH, WA_TH, rho)   # theta-alone joint sigma
    bs, bf, bw0, bwa, bdw0, bdwa = best
    print(f"\n    theta-alone joint sigma (f=0):        {s0:.2f}")
    print(f"    BEST combined joint sigma:            {bs:.2f}  at f_Lambda = {bf:.2f} "
          f"-> (w0,wa)=({bw0:+.3f},{bwa:+.3f})")

    # --- the honest verdict: does adding a constant Lambda move w0/wa toward or away from DESI? ---
    w0_1, wa_1 = fit_cpl(0.3)
    dwa_moves_toward = (wa_1 < WA_TH)   # DESI wants MORE negative wa; does Lambda steepen it?
    dw0_moves_toward = (abs(w0_1 - W0_DESI) < abs(W0_TH - W0_DESI))
    print(f"\n    direction check (at f=0.3): wa {WA_TH:+.3f} -> {wa_1:+.3f} "
          f"({'toward' if dwa_moves_toward else 'AWAY from'} DESI's {WA_DESI}); "
          f"w0 {W0_TH:+.3f} -> {w0_1:+.3f} ({'toward' if dw0_moves_toward else 'AWAY from'} DESI's {W0_DESI})")

    # --- rho-sensitivity: is the "improvement" genuine, or an artifact of sliding along the assumed
    #     DESI degeneracy? Both marginals get WORSE with f (dw0, dwa above), so any joint improvement is
    #     purely from the correlation term. Recompute best-f joint sigma across rho. ---
    print("\n    rho-sensitivity of the best combined fit (both MARGINALS worsen with f, so any joint")
    print("    'improvement' comes only from sliding along the assumed w0-wa correlation):")
    print("      rho    theta-alone_sigma   best-combined_sigma   improvement?")
    rho_robust = True
    for rr in (-0.9, -0.8, -0.7, -0.5, 0.0):
        s0r, *_ = joint_sigma(W0_TH, WA_TH, rr)
        bsr = min(joint_sigma(*fit_cpl(f), rr)[0] for f in fs)
        imp = bsr < s0r - 0.1
        if not imp:
            rho_robust = False
        print(f"     {rr:+.1f}   {s0r:8.2f}          {bsr:8.2f}            {'yes' if imp else 'NO'}")

    marginals_worsen = (abs(bdw0) > abs(dw00)) and (abs(bdwa) > abs(dwa0))
    still_failing = bs > 3.0
    check("computation ran: effective (w0,wa) of the DeWitt-Lambda + theta mixture over 0<=f<1",
          np.isfinite(bs))
    check("HONEST: both marginals (w0 AND wa) move AWAY from DESI as Lambda is added",
          marginals_worsen, f"|dw0| {abs(dw00):.2f}->{abs(bdw0):.2f}, |dwa| {abs(dwa0):.2f}->{abs(bdwa):.2f}")
    check("HONEST: the best combined fit is STILL a failing fit (>3 sigma) -- not a rescue",
          still_failing, f"best = {bs:.2f} sigma")
    check("HONEST: the joint 'improvement' is FRAGILE -- it vanishes as the assumed w0-wa correlation -> 0",
          not rho_robust, "at rho=0 the combination does NOT help -> the gain is degeneracy-sliding, not physics")

    print("\n[verdict]  MARGINAL -- the combination does NOT rescue the DESI tension.")
    print(f"  The best mix ({bf:.2f} Lambda) nominally lowers the JOINT distance {s0:.2f}->{bs:.2f} sigma, but:")
    print(f"  (1) BOTH marginals get WORSE: w0 {W0_TH:+.3f}->{bw0:+.3f} (more negative, away from {W0_DESI}),")
    print(f"      wa {WA_TH:+.3f}->{bwa:+.3f} (FLATTER, away from DESI's {WA_DESI}). A constant w=-1 Lambda")
    print(f"      supplies ZERO evolution, but DESI wants MORE -- so it moves the wrong way on the physics.")
    print(f"  (2) the joint gain comes ONLY from sliding along the assumed w0-wa degeneracy; it VANISHES as")
    print(f"      rho->0 (see table). It is an ellipse-shape artifact, not genuine evolution-matching.")
    print(f"  (3) {bs:.2f} sigma is STILL a failing fit. 'Less bad' is not 'consistent'.")
    print(f"  => The wild-card hope FAILS: a cosmological-constant piece cannot supply the missing evolution.")
    print(f"     The honest DESI tension STANDS as a live ~3-4 sigma negative for GU's dark-energy sector.")
    print("\n  KEY CAVEAT (double-counting, the philosopher's guard): this treats the DeWitt-Lambda and the")
    print("  theta-sector as INDEPENDENT components. If the O(M^0) DeWitt background is actually the VACUUM")
    print("  VALUE of the same theta field (not a separate fluid), the additive combination is INVALID and")
    print("  this test does not apply -- settling that needs the built theta dynamics. Either way, the")
    print("  combination is NOT a free rescue of the DESI tension.")

    if FAIL:
        print(f"\nFAILED: {FAIL}")
        raise SystemExit(1)
    print("\nexit 0 = combination computed; verdict = MARGINAL (both marginals worsen, gain is fragile")
    print("         degeneracy-sliding, still >3 sigma); the DESI tension STANDS. Not a rescue.")


if __name__ == "__main__":
    main()
