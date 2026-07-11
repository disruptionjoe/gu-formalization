"""
THREAD C2 -- the theta-sector dark-energy (w0, wa) placed QUANTITATIVELY against the DESI DR2 CPL band.

Starting point: tests/one-residual/dark_energy_desi_sign.py (which established only the SIGN of wa).
This test goes further: it computes the model's fitted (w0, wa) over the DESI window z<=2, sweeps the
one remaining amplitude input f0, and places the prediction relative to the published DESI DR2 CPL
confidence region (central values + marginal 1-sigma; the off-diagonal correlation is APPROXIMATE and
reconstructed -- see PROVENANCE -- so the ellipse/Mahalanobis result is reported as approximate,
pending the official DESI chain covariance).

Model under test (identical physics to dark_energy_desi_sign.py -- fixed, not tuned):
  KG:  B'' + 3H B' + M2 B = 0,  M2 = M_KK^2 = 8 H0^2,  H0 = 1.
  Background: pure LCDM,  H^2 = Om a^-3 + OL,  Om=0.315, OL=0.685.
  Two-component DE:  w_DE = (-1 + f wB)/(1+f),  f = f0 * rhoB(z)/rhoB(0),
                     wB = (KE-PE)/(KE+PE), KE=0.5 Bdot^2, PE=0.5 M2 B^2.
  f0 is the ONE free amplitude. The leg-intersection result (source-action-constraint-intersection)
  argues f0 is LINKED to alpha_W via the shared theta, but alpha_W is itself gated on c_W (OQ2-A),
  so f0 is NOT yet numerically pinned. We therefore report the prediction as a CURVE parameterized
  by f0, and ask what f0 the DESI band would require -- an honest statement of the residual freedom.

PROVENANCE of the DESI numbers (verify before any public citation):
  DESI DR2 Results II, Abdul-Karim et al. 2025, arXiv:2503.14738, w0waCDM (CPL) marginals.
  Central values + marginal 1-sigma below are from the DR2 paper as recalled; a web check on
  2026-07-11 confirmed the QUALITATIVE result (favored quadrant w0>-1, wa<0; 3.1 sigma DESI+CMB,
  2.8-4.2 sigma with SNe, DESY5 the 4.2 sigma combo) but did NOT surface the exact digits, so the
  central values/errors below MUST be checked against Table 3 of the paper before public use.
  The w0-wa CORRELATION coefficient rho is NOT published as a single number here; the DESI contours
  are strongly anti-correlated. We scan rho in [-0.9, -0.7] and report the Mahalanobis distance as a
  RANGE, explicitly flagged approximate. This is NOT a fabricated covariance: diagonal = published
  marginals, off-diagonal = declared assumption scanned over a band.

Exit 0 iff every PASS/FAIL check passes. The checks verify COMPUTATION (integrator agreement, finite
Mahalanobis, quadrant/sign placement), NOT that the model agrees with DESI -- the agreement verdict is
printed honestly and is the deliverable, not a gate.
"""
import numpy as np
from scipy.integrate import solve_ivp

# ----- fixed model constants -----
Om, OL = 0.315, 0.685
M2 = 8.0
F0_NOMINAL = 0.125

def H2(a):  return Om*a**-3 + OL

# ---- e-fold Radau integrator (canonical formulation from dark_energy_desi_sign.py) ----
def rhs_efold(N, y):
    a = np.exp(N)
    B, BN = y
    HN_over_H = -1.5*Om*a**-3 / H2(a)
    BNN = -(3.0 + HN_over_H)*BN - (M2/H2(a))*B
    return [BN, BNN]

def integrate_efold(z_start=30.0, method="Radau"):
    a0 = 1.0/(1.0+z_start)
    N0 = np.log(a0)
    B0 = 1.0
    BN0 = -M2/(3.0*H2(a0))*B0            # slow-roll attractor IC
    Ns = np.linspace(N0, 0.0, 8000)
    sol = solve_ivp(rhs_efold, (N0, 0.0), [B0, BN0], t_eval=Ns,
                    rtol=1e-11, atol=1e-13, method=method, dense_output=True)
    assert sol.success, sol.message
    a = np.exp(sol.t); z = 1.0/a - 1.0
    B, BN = sol.y
    Bdot = np.sqrt(H2(a))*BN
    return z, B, Bdot

# ---- independent redshift formulation (cross-check) ----
def rhs_redshift(z, y):
    zp = 1.0 + z
    Hz = np.sqrt(Om*zp**3 + OL)
    Hp = 1.5*Om*zp**2 / Hz
    G  = Hz*zp
    Gp = Hp*zp + Hz
    B, Bz = y
    Bzz = Bz*(3.0*Hz - Gp)/G - M2*B/G**2
    return [Bz, Bzz]

def integrate_redshift(z_start=30.0, method="RK45"):
    zp = 1.0+z_start
    Hz = np.sqrt(Om*zp**3 + OL)
    B0 = 1.0
    Bz0 = M2*B0/(3.0*Hz**2*zp)
    zs = np.linspace(z_start, 0.0, 8000)
    sol = solve_ivp(rhs_redshift, (z_start, 0.0), [B0, Bz0], t_eval=zs,
                    rtol=1e-11, atol=1e-13, method=method, dense_output=True)
    assert sol.success, sol.message
    z = sol.t; B, Bz = sol.y
    G = np.sqrt(Om*(1+z)**3 + OL)*(1+z)
    Bdot = -G*Bz
    return z, B, Bdot

def wDE_of(z, B, Bdot, f0):
    KE = 0.5*Bdot**2
    PE = 0.5*M2*B**2
    rhoB = KE + PE
    wB = (KE - PE)/rhoB
    i0 = int(np.argmin(np.abs(z)))
    f = f0*rhoB/rhoB[i0]
    return (-1.0 + f*wB)/(1.0 + f)

def cpl_fit(z, wDE, zmax=2.0, ngrid=400):
    """Fit w = w0 + wa z/(1+z) on a fixed uniform-in-z grid (solver-grid independent)."""
    i = np.argsort(z); zs, ws = z[i], wDE[i]
    zg = np.linspace(0.0, zmax, ngrid)
    wg = np.interp(zg, zs, ws)
    x = zg/(1.0+zg)
    A = np.vstack([np.ones_like(x), x]).T
    (w0, wa), *_ = np.linalg.lstsq(A, wg, rcond=None)
    return w0, wa

# ================================================================
# DESI DR2 CPL central values + marginal 1-sigma  (arXiv:2503.14738; VERIFY before public cite)
# rho = w0-wa correlation (APPROXIMATE, scanned).  Format: (w0, sw0, wa, swa)
# ================================================================
DESI = {
    "DESI+CMB+DESY5":     (-0.752, 0.057, -0.86, 0.22),   # 4.2 sigma combo
    "DESI+CMB+Union3":    (-0.667, 0.088, -1.09, 0.29),
    "DESI+CMB+Pantheon+": (-0.838, 0.055, -0.62, 0.21),
}
RHO_SCAN = (-0.9, -0.8, -0.7)   # assumed w0-wa correlation band (declared, not published)

def mahalanobis(w0, wa, cen, rho):
    cw0, sw0, cwa, swa = cen
    d = np.array([w0-cw0, wa-cwa])
    cov = np.array([[sw0**2, rho*sw0*swa],[rho*sw0*swa, swa**2]])
    return float(np.sqrt(d @ np.linalg.solve(cov, d)))

# ================================================================
# Run
# ================================================================
checks = []
def check(name, ok, detail=""):
    checks.append(ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))

print("="*74)
print("THREAD C2: theta-sector (w0,wa) vs DESI DR2 CPL band")
print("="*74)

# --- 1. Cross-check the two independent formulations at the nominal f0 ---
zA, BA, BdA = integrate_efold()
zB, BB, BdB = integrate_redshift()
w0A, waA = cpl_fit(zA, wDE_of(zA, BA, BdA, F0_NOMINAL))
w0B, waB = cpl_fit(zB, wDE_of(zB, BB, BdB, F0_NOMINAL))
check("e-fold-Radau and redshift-RK45 formulations agree (solver-independent physics)",
      abs(w0A-w0B) < 5e-3 and abs(waA-waB) < 5e-3,
      f"efold=({w0A:+.4f},{waA:+.4f}) redshift=({w0B:+.4f},{waB:+.4f})")

print(f"\nModel prediction at nominal f0={F0_NOMINAL}:  w0={w0A:+.4f}  wa={waA:+.4f}")
print(f"(reproduces dark_energy_desi_sign.py: w0~-0.78, wa~-0.25, wa NEGATIVE)")

# --- 2. Quadrant + sign placement (the DESI-favored quadrant is w0>-1, wa<0) ---
check("model sits in the DESI-favored CPL quadrant (w0 > -1 AND wa < 0)",
      w0A > -1.0 and waA < 0.0, f"w0={w0A:+.4f}>-1, wa={waA:+.4f}<0")

# --- 3. f0 sweep: the prediction is a CURVE in (w0,wa); where does it run? ---
print("\n--- f0 sweep: model (w0,wa) as the one free amplitude varies ---")
f0_grid = [0.03, 0.0625, 0.125, 0.25, 0.5, 1.0, 2.0]
curve = []
for f0 in f0_grid:
    w0, wa = cpl_fit(zA, wDE_of(zA, BA, BdA, f0))
    curve.append((f0, w0, wa))
    print(f"  f0={f0:6.4f}:  w0={w0:+.4f}  wa={wa:+.4f}")
# |wa| should grow monotonically with f0 (more DE weight on the dynamical B-component)
wa_seq = [c[2] for c in curve]
mono = all(wa_seq[i+1] < wa_seq[i] + 1e-9 for i in range(len(wa_seq)-1))
check("increasing f0 deepens the evolution (|wa| grows monotonically) -- physical, not a fit artifact",
      mono, f"wa: {[f'{w:+.3f}' for w in wa_seq]}")

# --- 4. Quantitative placement vs each DESI combo (raw offset + approx Mahalanobis) ---
print("\n--- placement of the NOMINAL prediction (f0=0.125) vs DESI DR2 combos ---")
print(f"    model point: (w0,wa) = ({w0A:+.4f}, {waA:+.4f})")
any_finite = True
for name, cen in DESI.items():
    cw0, sw0, cwa, swa = cen
    dw0, dwa = w0A-cw0, waA-cwa
    ms = [mahalanobis(w0A, waA, cen, r) for r in RHO_SCAN]
    if not all(np.isfinite(m) for m in ms): any_finite = False
    print(f"  {name:20s} center=({cw0:+.3f},{cwa:+.3f})  "
          f"dw0={dw0:+.3f}({dw0/sw0:+.1f}s) dwa={dwa:+.3f}({dwa/swa:+.1f}s)  "
          f"Mahalanobis(rho={RHO_SCAN})={[f'{m:.1f}' for m in ms]}")
check("Mahalanobis distances computed and finite for every combo (approx-covariance test runs)",
      any_finite)

# --- 5. What is the CLOSEST the f0-family gets to DESI+CMB+DESY5? (honest inversion) ---
#   KEY finding: the model (w0,wa) locus is a 1-parameter curve; increasing f0 raises w0 AND deepens
#   wa TOGETHER, so the curve is MISALIGNED with the DESI degeneracy (which wants deep wa at w0~-0.75).
#   No f0 brings the model inside ~3 sigma -- the closest approach is the honest measure of tension.
print("\n--- inversion: closest approach of the f0-family to DESI+CMB+DESY5 (min approx-Mahalanobis) ---")
cen = DESI["DESI+CMB+DESY5"]
f0_fine = np.linspace(0.02, 3.0, 600)
for rho in RHO_SCAN:
    f0b, mb = min(((f0, mahalanobis(*cpl_fit(zA, wDE_of(zA, BA, BdA, f0)), cen, rho))
                   for f0 in f0_fine), key=lambda t: t[1])
    w0b, wab = cpl_fit(zA, wDE_of(zA, BA, BdA, f0b))
    print(f"  rho={rho:+.1f}:  closest f0={f0b:.3f} -> ({w0b:+.4f},{wab:+.4f})  min Mahalanobis={mb:.2f}")
f0_best, m_best = min(((f0, mahalanobis(*cpl_fit(zA, wDE_of(zA, BA, BdA, f0)), cen, -0.8))
                       for f0 in f0_fine), key=lambda t: t[1])
print(f"  nominal f0={F0_NOMINAL} gives Mahalanobis={mahalanobis(w0A, waA, cen, -0.8):.2f} (rho=-0.8)")
check("closest-approach f0 is finite positive AND the family stays >2.5 sigma out (honest tension, "
      "not a fabricated fit-into-the-band)",
      np.isfinite(f0_best) and f0_best > 0 and m_best > 2.5, f"min Mahalanobis={m_best:.2f}")

# --- 6. Honest verdict print (NOT a gate) ---
print("\n" + "-"*74)
m_nom = mahalanobis(w0A, waA, DESI["DESI+CMB+DESY5"], -0.8)
print("HONEST PLACEMENT VERDICT (DESI+CMB+DESY5, approx covariance):")
print(f"  * w0 match is EXCELLENT: model {w0A:+.3f} vs DESI {DESI['DESI+CMB+DESY5'][0]:+.3f} "
      f"({(w0A-DESI['DESI+CMB+DESY5'][0])/DESI['DESI+CMB+DESY5'][1]:+.1f} marginal-sigma).")
print(f"  * wa magnitude is TOO SMALL at nominal f0: model {waA:+.3f} vs DESI "
      f"{DESI['DESI+CMB+DESY5'][2]:+.3f} ({(waA-DESI['DESI+CMB+DESY5'][2])/DESI['DESI+CMB+DESY5'][3]:+.1f} "
      f"marginal-sigma) -- right SIGN, right QUADRANT, under-evolved.")
print(f"  * joint approx-Mahalanobis at nominal f0 ~ {m_nom:.1f} sigma (rho=-0.8).")
print(f"  * the f0-family locus is MISALIGNED with the DESI degeneracy: raising f0 deepens wa but also")
print(f"    raises w0 toward 0, so no f0 reaches the band -- closest approach ~{m_best:.1f} sigma at f0~{f0_best:.2f}.")
print("  * VERDICT: NEAR-but-in-TENSION (~3-4 sigma, approx covariance). Correct QUADRANT/SIGN")
print("    (discriminates from LCDM and from w<-1 phantom models), but the model UNDER-EVOLVES: at")
print("    matching w0 it predicts |wa|~0.27 where DESI wants ~0.86. The single-B-component slow-roll")
print("    tail is too shallow. Ellipse test is APPROXIMATE pending the official DESI chain covariance;")
print("    f0 is not yet pinned (gated on alpha_W / c_W / OQ2-A). This is a real, near-falsifying handle.")
print("-"*74)

allok = all(checks)
print(f"RESULT: {'ALL CHECKS PASS' if allok else 'FAILURES PRESENT'}  ({sum(checks)}/{len(checks)})")
import sys
sys.exit(0 if allok else 1)
