"""
WAVE-1 / H3 (Condorcet-#2) -- two parts, both honest:

(A) VERIFY the DESI DR2 CPL constraints from the PRIMARY source and re-place GU's theta-sector point.
    The DESI numbers used in tests/threads/C_dark_energy_wz_vs_desi.py were flagged as MODEL RECALL
    ("VERIFY before public cite"). Here they are checked digit-by-digit against arXiv:2503.14738
    ("DESI DR2 Results II"), the results table AND the marginalized posteriors quoted in the paper's
    Eqs. (26)-(28). The PDF was downloaded and its text extracted on 2026-07-11; the exact strings are
    reproduced in the PROVENANCE block below.

(B) RE-RUN the theta-INT-gravity order-compatibility with the CORRECTED Willmore residual.
    The leg-intersection claim (explorations/source-action-constraint-intersection-2026-07-11.md) was:
    "theta ~ M/rho^2, its quadratic stress enters at M^2/r^4 = the SAME order as the Willmore residual
     W_s ~ M^2/r^4 (RFAIL-03 estimate) -- necessary condition for Branch-3 cancellation MET."
    That match used the SUPERSEDED canon estimate M^2/r^4. The residual has since been CORRECTED to
    M^2/r^6 (principled geometric II; H harmonic) --
    tests/one-residual/willmore_geometric_ii_and_ambient_curvature.py. We redo the order arithmetic
    with M^2/r^6 and state whether the over-determination TIGHTENS, HOLDS, or BREAKS.

DISCIPLINE. Part (A) checks are COMPUTATION (verified DESI digits match the paper; GU point reproduced;
finite sigma/Mahalanobis) -- NOT "GU agrees with DESI" (it does not; that verdict is printed honestly).
Part (B) checks are ARITHMETIC on the reconstructed weak-field scalings (integer M- and r-powers); they
verify the LOGIC of the compatibility test, NOT that GU's gravity is correct. Both the r-scalings and the
source-law inversion (how theta feeds the metric stress) are reconstruction-grade / UNBUILT -- stated.

Exit 0 iff every PASS/FAIL check passes.
"""
import numpy as np
from scipy.integrate import solve_ivp

# ============================================================================
# (A) VERIFIED DESI DR2 CPL constraints -- arXiv:2503.14738, retrieved 2026-07-11
# ============================================================================
# PROVENANCE (verbatim, from the downloaded PDF text of arXiv:2503.14738):
#   Results table (w0waCDM, DESI+CMB+SNe rows) AND Eqs. (26)-(28):
#     w0 = -0.838 +/- 0.055 ,  wa = -0.62 (+0.22/-0.19)   DESI+CMB+Pantheon+   [Eq. 26]
#     w0 = -0.667 +/- 0.088 ,  wa = -1.09 (+0.31/-0.27)   DESI+CMB+Union3      [Eq. 27]
#     w0 = -0.752 +/- 0.057 ,  wa = -0.86 (+0.23/-0.20)   DESI+CMB+DESY5       [Eq. 28]
#   Preference over LCDM (Table VI / abstract): DESI+CMB 3.1 sigma; with SNe 2.8 (Pantheon+),
#     3.8 (Union3), 4.2 (DESY5) sigma.
#   The w0-wa CORRELATION coefficient is NOT published as a single number in the table; the DR2
#     contours are strongly anti-correlated (Fig. in paper). rho is therefore SCANNED (declared, not
#     fabricated): diagonal = the verified marginals below; off-diagonal = scanned band.
#
# Format: (w0, sw0, wa, swa_plus, swa_minus).  VERIFIED = retrieved from the primary PDF (not recall).
DESI_VERIFIED = {
    "DESI+CMB+Pantheon+": (-0.838, 0.055, -0.62, 0.22, 0.19),
    "DESI+CMB+Union3":    (-0.667, 0.088, -1.09, 0.31, 0.27),
    "DESI+CMB+DESY5":     (-0.752, 0.057, -0.86, 0.23, 0.20),
}
DESI_SIGMA_VS_LCDM = {"DESI+CMB": 3.1, "DESI+CMB+Pantheon+": 2.8,
                      "DESI+CMB+Union3": 3.8, "DESI+CMB+DESY5": 4.2}

# What tests/threads/C_dark_energy_wz_vs_desi.py had HARD-CODED from recall (to audit drift):
DESI_RECALL = {
    "DESI+CMB+DESY5":     (-0.752, 0.057, -0.86, 0.22),
    "DESI+CMB+Union3":    (-0.667, 0.088, -1.09, 0.29),
    "DESI+CMB+Pantheon+": (-0.838, 0.055, -0.62, 0.21),
}
RHO_SCAN = (-0.9, -0.8, -0.7)   # assumed w0-wa correlation band (declared; DESI does not tabulate rho)

# ============================================================================
# GU theta-sector model (identical physics to C_dark_energy_wz_vs_desi.py -- fixed, not tuned)
# ============================================================================
Om, OL = 0.315, 0.685
M2 = 8.0
F0_NOMINAL = 0.125

def H2(a): return Om*a**-3 + OL

def rhs_efold(N, y):
    a = np.exp(N); B, BN = y
    HN_over_H = -1.5*Om*a**-3 / H2(a)
    return [BN, -(3.0 + HN_over_H)*BN - (M2/H2(a))*B]

def integrate_efold(z_start=30.0):
    a0 = 1.0/(1.0+z_start); N0 = np.log(a0)
    BN0 = -M2/(3.0*H2(a0))
    Ns = np.linspace(N0, 0.0, 8000)
    sol = solve_ivp(rhs_efold, (N0, 0.0), [1.0, BN0], t_eval=Ns,
                    rtol=1e-11, atol=1e-13, method="Radau", dense_output=True)
    assert sol.success, sol.message
    a = np.exp(sol.t); z = 1.0/a - 1.0
    B, BN = sol.y
    return z, B, np.sqrt(H2(a))*BN

def wDE_of(z, B, Bdot, f0):
    KE = 0.5*Bdot**2; PE = 0.5*M2*B**2; rhoB = KE + PE
    wB = (KE - PE)/rhoB
    i0 = int(np.argmin(np.abs(z)))
    f = f0*rhoB/rhoB[i0]
    return (-1.0 + f*wB)/(1.0 + f)

def cpl_fit(z, wDE, zmax=2.0, ngrid=400):
    i = np.argsort(z); zs, ws = z[i], wDE[i]
    zg = np.linspace(0.0, zmax, ngrid)
    wg = np.interp(zg, zs, ws)
    x = zg/(1.0+zg)
    A = np.vstack([np.ones_like(x), x]).T
    (w0, wa), *_ = np.linalg.lstsq(A, wg, rcond=None)
    return w0, wa

def marg_sigma(val, cen, splus, sminus):
    """marginal sigma using the error bar on the side the model actually lies."""
    d = val - cen
    return d / (splus if d >= 0 else sminus)

def mahalanobis(w0, wa, cen, rho):
    cw0, sw0, cwa, swap, swam = cen
    swa = 0.5*(swap + swam)                     # symmetrized (honest approx for the ellipse)
    d = np.array([w0-cw0, wa-cwa])
    cov = np.array([[sw0**2, rho*sw0*swa], [rho*sw0*swa, swa**2]])
    return float(np.sqrt(d @ np.linalg.solve(cov, d)))

# ============================================================================
# Run
# ============================================================================
checks = []
def check(name, ok, detail=""):
    checks.append(ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))

print("="*78)
print("H3 (Condorcet-#2): DESI DR2 VERIFIED + corrected-residual theta-intersection")
print("="*78)

# --- A1. The recalled DESI numbers match the VERIFIED primary-source digits ---
print("\n[A] DESI DR2 verification vs arXiv:2503.14738 (primary PDF, retrieved 2026-07-11)")
central_ok = True
for name, ver in DESI_VERIFIED.items():
    rc = DESI_RECALL[name]
    w0_match = abs(ver[0]-rc[0]) < 1e-9 and abs(ver[1]-rc[1]) < 1e-9
    wa_cen_match = abs(ver[2]-rc[2]) < 1e-9
    if not (w0_match and wa_cen_match): central_ok = False
    print(f"  {name:20s} verified w0={ver[0]:+.3f}+/-{ver[1]:.3f}  "
          f"wa={ver[2]:+.2f}(+{ver[3]:.2f}/-{ver[4]:.2f})   "
          f"[recall w0 err/central {'OK' if w0_match and wa_cen_match else 'DRIFT'}]")
check("recalled DESI (w0,sw0,wa) central values MATCH the verified primary-source digits",
      central_ok, "central values were correct; only the wa error bars were symmetrized in recall")
# the recall symmetrized wa error; verified errors are ASYMMETRIC -- quantify the (small) drift
wa_err_drift = max(abs(DESI_RECALL[n][3] - 0.5*(DESI_VERIFIED[n][3]+DESI_VERIFIED[n][4]))
                   for n in DESI_VERIFIED)
check("recall wa error bars differ from verified (symmetrized) by < 0.02 (rounding of asymmetric bars)",
      wa_err_drift < 0.02, f"max |sigma_wa drift| = {wa_err_drift:.3f}")

# --- A2. Reproduce the GU theta-sector point ---
z, B, Bdot = integrate_efold()
w0g, wag = cpl_fit(z, wDE_of(z, B, Bdot, F0_NOMINAL))
print(f"\n  GU theta-sector point (f0={F0_NOMINAL}, fixed): (w0,wa) = ({w0g:+.4f}, {wag:+.4f})")
check("GU point reproduces (-0.768, -0.273) from C_dark_energy_wz_vs_desi.py",
      abs(w0g-(-0.768)) < 3e-3 and abs(wag-(-0.273)) < 3e-3, f"({w0g:+.4f},{wag:+.4f})")
check("GU sits in the DESI-favored quadrant w0>-1, wa<0", w0g > -1 and wag < 0)

# --- A3. Marginal-sigma placement with the VERIFIED (asymmetric) error bars ---
print("\n  marginal-sigma placement (verified asymmetric error bars):")
for name, cen in DESI_VERIFIED.items():
    cw0, sw0, cwa, swap, swam = cen
    s_w0 = marg_sigma(w0g, cw0, sw0, sw0)
    s_wa = marg_sigma(wag, cwa, swap, swam)
    print(f"    {name:20s} w0: {s_w0:+.2f} sigma   wa: {s_wa:+.2f} sigma")
# DESY5 is the strongest combo (4.2 sigma vs LCDM) -- report it as the headline
cen = DESI_VERIFIED["DESI+CMB+DESY5"]
s_w0_d5 = marg_sigma(w0g, cen[0], cen[1], cen[1])
s_wa_d5 = marg_sigma(wag, cen[2], cen[3], cen[4])
check("vs DESY5 (strongest combo): w0 within 0.5 sigma (excellent), wa off by > 2 sigma (under-evolved)",
      abs(s_w0_d5) < 0.5 and s_wa_d5 > 2.0, f"w0={s_w0_d5:+.2f}s, wa={s_wa_d5:+.2f}s")

# --- A4. Joint Mahalanobis (rho scanned, honestly approximate) ---
print("\n  joint Mahalanobis distance (rho scanned; DESI does not publish rho):")
finite = True
for name, cen in DESI_VERIFIED.items():
    ms = [mahalanobis(w0g, wag, cen, r) for r in RHO_SCAN]
    if not all(np.isfinite(m) for m in ms): finite = False
    print(f"    {name:20s} Mahalanobis(rho={RHO_SCAN}) = {[f'{m:.1f}' for m in ms]}")
check("Mahalanobis finite for every combo over the rho scan", finite)
m_d5 = [mahalanobis(w0g, wag, DESI_VERIFIED['DESI+CMB+DESY5'], r) for r in RHO_SCAN]
check("GU is > 3 sigma from DESY5 across the whole rho scan (honest tension, not a fit-into-band)",
      all(m > 3.0 for m in m_d5), f"DESY5 Mahalanobis range {min(m_d5):.1f}-{max(m_d5):.1f}")

# --- A5. f0-family closest approach (the under-evolution is structural, not a bad f0) ---
f0s = np.linspace(0.02, 3.0, 600)
best = min(((f0, mahalanobis(*cpl_fit(z, wDE_of(z, B, Bdot, f0)),
             DESI_VERIFIED['DESI+CMB+DESY5'], -0.8)) for f0 in f0s), key=lambda t: t[1])
check("no f0 brings the one-parameter family inside 3 sigma of DESY5 (locus MISALIGNED with DESI "
      "degeneracy -- raising f0 deepens wa but also raises w0)",
      best[1] > 3.0, f"closest approach {best[1]:.2f} sigma at f0={best[0]:.3f}")

# ============================================================================
# (B) Corrected-residual order-compatibility (M-power, r-power arithmetic)
# ============================================================================
print("\n[B] theta-INT-gravity order compatibility with the CORRECTED Willmore residual")
# Reconstructed weak-field scalings (each = M^{pM}/r^{pr}), sourced as noted. All reconstruction-grade.
#   theta (Branch-3 geometric distortion, isotropic Schwarzschild)   ~ M^1/r^2   [source-action-...md]
#   B  (section II, principled geometric Hessian d^2 h)              ~ M^1/r^3   [willmore_geometric_ii...]
#   R^Y (ambient Riemann at g=eta)                                   ~ M^0/r^0   [willmore_curved_ambient_term]
#   Willmore residual OLD canon estimate (RFAIL-03)                  ~ M^2/r^4   [SUPERSEDED]
#   Willmore residual UNPRINCIPLED (MOVE-3 M=0-only subtraction)     ~ M^2/r^2   [SUPERSEDED artifact]
#   Willmore residual CORRECTED (principled II, Q^TF(B)=(d^2h)^2)    ~ M^2/r^6   [CURRENT]
POW = {
    "theta":              (1, 2),
    "theta^2 (src-law)":  (2, 4),   # (M/r^2)^2 -- the quadratic stress the intersection invoked
    "B":                  (1, 3),
    "R^Y":                (0, 0),
    "R^Y.B (II-class)":   (1, 3),   # R^Y * B
    "W_old (RFAIL-03)":   (2, 4),
    "W_corrected":        (2, 6),   # (M/r^3)^2
}
def cancellable(a, b):
    """A constant coefficient can cancel two tensors iff SAME M-power AND SAME r-power."""
    return POW[a] == POW[b]

# B1. Sanity: derive the composite scalings from the primitives (no free numbers).
check("theta^2 r-power = 2*(theta r-power): (M/r^2)^2 = M^2/r^4",
      POW["theta^2 (src-law)"] == (2*POW["theta"][0], 2*POW["theta"][1]))
check("corrected residual = (principled B)^2: (M/r^3)^2 = M^2/r^6",
      POW["W_corrected"] == (2*POW["B"][0], 2*POW["B"][1]))
check("II-class ambient term R^Y.B = R^Y * B in both powers",
      POW["R^Y.B (II-class)"] == (POW["R^Y"][0]+POW["B"][0], POW["R^Y"][1]+POW["B"][1]))

# B2. The ORIGINAL intersection match used the SUPERSEDED estimate -- reproduce that it "matched".
check("ORIGINAL claim reproduced: theta^2 (M^2/r^4) matched the OLD Willmore estimate M^2/r^4",
      cancellable("theta^2 (src-law)", "W_old (RFAIL-03)"),
      "this is why the intersection reported 'necessary condition MET'")

# B3. With the CORRECTED residual, the quadratic-theta match BREAKS in r-power.
same_M = POW["theta^2 (src-law)"][0] == POW["W_corrected"][0]
same_r = POW["theta^2 (src-law)"][1] == POW["W_corrected"][1]
check("CORRECTED: theta^2 (M^2/r^4) vs Willmore M^2/r^6 -- M-power still matches (both M^2)",
      same_M, "quadratic-in-M, still safe for M/r<<1")
check("CORRECTED: r-power NO LONGER matches (r^-4 vs r^-6) -- quadratic-theta cancellation FAILS",
      not same_r and not cancellable("theta^2 (src-law)", "W_corrected"),
      "no constant coefficient cancels terms of different r-profile at all radii")

# B4. The II-class LINEAR mechanism (the post-correction framing) ALSO mismatches in r-power.
#     Corrected residual arises from HARMONIC H (box h = 0) -- the principled/H-class-leaning normalization.
#     II-class needs an O(M^1) theta-source to cancel the O(M^1) ambient term R^Y.B; check r-powers.
check("II-class: ambient term R^Y.B (M/r^3) and theta-source (M/r^2) share M-power (both O(M^1))",
      POW["R^Y.B (II-class)"][0] == POW["theta"][0])
check("II-class: R^Y.B (r^-3) vs theta (r^-2) -- r-power MISMATCH; linear cancellation needs the "
      "source-law inversion to supply r^-1 (UNBUILT L_theta_source)",
      not cancellable("R^Y.B (II-class)", "theta"))

# B5. VERDICT arithmetic: the over-determination is NOT robust with the corrected residual.
#   - quadratic-theta route: r-power broken.
#   - II-class linear route: r-power broken (gated on unbuilt inversion).
#   - H-class route: H harmonic -> gravity self-closes intrinsically at O(M^2) (Q^TF ~ M^2/r^6 balanced
#     by c_W R^Y.H), NO leading theta-source -> the shared-theta over-determination DISSOLVES.
over_determination_robust = (cancellable("theta^2 (src-law)", "W_corrected")
                             or cancellable("R^Y.B (II-class)", "theta"))
check("theta-sector over-determination does NOT tighten/hold robustly under the corrected residual "
      "(both cancellation routes fail the r-power test)",
      not over_determination_robust,
      "it is now CONTINGENT on II-class + an unbuilt source-law inversion; the corrected residual "
      "comes from the harmonic-H (H-class-leaning) normalization in which gravity needs no theta")

# ---- honest verdict print (NOT a gate) ----
print("\n" + "-"*78)
print("HONEST VERDICT")
print("-"*78)
print("(A) DESI DR2 numbers VERIFIED against arXiv:2503.14738 (primary PDF). The values in")
print("    C_dark_energy_wz_vs_desi.py were CORRECT to the printed digits; the only refinement is")
print("    that the published wa errors are ASYMMETRIC (DESY5 +0.23/-0.20; Union3 +0.31/-0.27;")
print("    Pantheon+ +0.22/-0.19). GU nails w0 (%+.2f sigma vs DESY5) but under-evolves wa" % s_w0_d5)
print("    (%+.1f sigma); joint ~3-5 sigma across the rho scan. A real, near-falsifying handle -- UNCHANGED" % s_wa_d5)
print("    by verification (the tension was not a recall artifact).")
print("(B) With the residual CORRECTED from M^2/r^4 (superseded) to M^2/r^6, the theta-INT-gravity")
print("    over-determination does NOT tighten -- it WEAKENS. The original 'same order' match used the")
print("    old M^2/r^4 estimate; theta^2 ~ M^2/r^4 no longer shares the r-profile of M^2/r^6, and the")
print("    II-class linear route (R^Y.B ~ M/r^3 vs theta ~ M/r^2) also mismatches in r-power. The")
print("    corrected residual follows from HARMONIC mean curvature (H-class-leaning), and in the H-class")
print("    gravity self-closes at O(M^2) with NO theta-source -- so the intersection that would have")
print("    PINNED f0 dissolves. Net: f0 is NOT robustly fixed by gravity; dark energy's weakest point")
print("    (free f0) stays open; the DESI tension stands on its own, without a gravitational lifeline.")
print("    CAVEATS: Assumption 3 (theta = D_A*F_A) still UNPROVED; background co-variation not modelled")
print("    (LCDM background assumed); rho SCANNED (DESI publishes no single covariance); the r-scalings")
print("    and the source-law inversion are reconstruction-grade / UNBUILT.")
print("-"*78)

allok = all(checks)
print(f"RESULT: {'ALL CHECKS PASS' if allok else 'FAILURES PRESENT'}  ({sum(checks)}/{len(checks)})")
import sys
sys.exit(0 if allok else 1)
