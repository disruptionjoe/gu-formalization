"""VG-SA: Mannheim primary-source intake -- arithmetic cross-checks.

Route SA is a rung-0 SOURCE INTAKE (extraction), not a carrier computation.
This script does the only computable part honestly: it takes every number
extracted verbatim from the three primaries --

  P1 = arXiv:1101.2186 (Making the Case for Conformal Gravity, Found. Phys. 42, 388)
  P2 = arXiv:1011.3495 (Mannheim & O'Brien, PRL 106, 121101; 111-galaxy fits)
  P3 = arXiv:1610.08907 (Mass generation, CC problem, conformal symmetry, Higgs)

-- and verifies that the papers' own claimed numerical relations between those
numbers actually hold (internal consistency of the sources), with explicit
tolerances and a scrambled control that FAILS the same checks (non-tautology).

No physics claim is moved by this script. It certifies transcription fidelity
and the papers' internal arithmetic only.

Exit 0 iff all checks pass and the scrambled control fails.
"""

import math
import sys

FAIL = []


def check(name, ok, detail):
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name}: {detail}")
    if not ok:
        FAIL.append(name)


print("=" * 76)
print("VG-SA Mannheim primary-source arithmetic cross-checks (2026-07-06)")
print("=" * 76)

# ---------------------------------------------------------------- extracted
# P1 eq (M66), P2 eq (22), P3 eq (M189) -- identical across papers
gamma_star = 5.42e-41   # cm^-1  (local linear coefficient per unit solar mass)
gamma_0 = 3.06e-30      # cm^-1  (cosmological linear coefficient)
kappa = 9.54e-54        # cm^-2  (inhomogeneity-sourced quadratic coefficient)
beta_star = 1.48e5      # cm     (P3 eq (M189): solar Schwarzschild-like coeff)
q0_fit = -0.37          # P3 eq (M190) context; Hubble-plot fit value
N_star_gal = 1e11       # P1 S9 footnote: galactic N* never bigger than ~1e11

print("\nExtracted universal parameters (P1 M66/M69, P2 eq22, P3 M189):")
print(f"  beta*   = {beta_star:.3e} cm")
print(f"  gamma*  = {gamma_star:.3e} cm^-1")
print(f"  gamma_0 = {gamma_0:.3e} cm^-1")
print(f"  kappa   = {kappa:.3e} cm^-2")
print(f"  q0(fit) = {q0_fit}")

MPC_CM = 3.0857e24  # cm per Mpc (standard; conversion constant, not a target)
KPC_CM = 3.0857e21

# ------------------------------------------------------------------ checks
print("\n--- Paper-claimed relations, recomputed ---")

# 1. P1 (M69): kappa ~ (100 Mpc)^-2
kappa_100mpc = (100.0 * MPC_CM) ** -2
ratio = kappa / kappa_100mpc
check("kappa ~ (100 Mpc)^-2  [P1 M69]",
      0.5 < ratio < 2.0,
      f"(100 Mpc)^-2 = {kappa_100mpc:.3e} cm^-2, kappa/that = {ratio:.3f} "
      f"(tolerance: factor 2)")

# 2. P1 S9: no bound orbits beyond R ~ gamma_0/kappa = 3.21e23 cm
r_term = gamma_0 / kappa
check("gamma_0/kappa = 3.21e23 cm  [P1 S9]",
      abs(r_term - 3.21e23) / 3.21e23 < 0.01,
      f"computed {r_term:.3e} cm vs paper's 3.21e23 cm (tol 1%)")

# 3. P3: (beta*/gamma*)^{1/2} of order 1e23 cm (galactic scale onset)
onset = math.sqrt(beta_star / gamma_star)
check("(beta*/gamma*)^1/2 ~ 1e23 cm  [P3 after M189]",
      1e22 < onset < 1e24,
      f"computed {onset:.3e} cm (order-of-magnitude window 1e22-1e24)")

# 4. P1/P2: gamma_0 = 2*sqrt(-K) with K = -gamma_0^2/4 (self-consistency of
#    the static-coordinate representation of RW curvature, P2 eq (11)-(12))
K = -gamma_0 ** 2 / 4.0
check("gamma_0 = 2 sqrt(-K), K = -gamma_0^2/4  [P1 M64, P2]",
      abs(2.0 * math.sqrt(-K) - gamma_0) / gamma_0 < 1e-12,
      f"K = {K:.3e} cm^-2, 2 sqrt(-K) = {2.0 * math.sqrt(-K):.3e} cm^-1")

# 5. P1 S9 footnote: for N* <= 1e11, N*gamma* is of order gamma_0 (not larger)
n_gamma = N_star_gal * gamma_star
check("N*gamma* (N*=1e11) same order as gamma_0  [P1 S9 fn]",
      0.1 < n_gamma / gamma_0 < 10.0,
      f"N*gamma* = {n_gamma:.3e} cm^-1, ratio to gamma_0 = {n_gamma / gamma_0:.2f}")

# 6. P1 S9 footnote: max galaxy size 'never larger than of order 100 kpc'
#    v^2 -> 0 where (N*gamma* + gamma_0)/2 = kappa*R
r_max = (n_gamma + gamma_0) / (2.0 * kappa)
r_max_kpc = r_max / KPC_CM
check("max galaxy size ~ 100 kpc order  [P1 S9 fn]",
      30.0 < r_max_kpc < 300.0,
      f"R_max = {r_max:.3e} cm = {r_max_kpc:.0f} kpc (window 30-300 kpc)")

# 7. P3 (M190) context: q0 constrained to -1 <= q0 <= 0; fit value inside
check("q0 = -0.37 inside structural window [-1, 0]  [P3]",
      -1.0 <= q0_fit <= 0.0,
      f"q0 = {q0_fit}")

# 8. P2 sample bookkeeping: 18 THINGS + 30 UMa + 20 LSB + 21 LSB + 22 misc = 111
subsamples = [18, 30, 20, 21, 22]
total = sum(subsamples)
check("P2 galaxy subsamples sum to 111  [P2 abstract + tables 1-5]",
      total == 111,
      f"{'+'.join(map(str, subsamples))} = {total} (P2 fits 111; P1 quotes the "
      f"extended 138-galaxy program; P3 quotes 141)")

# 9. P3 luminosity distance formula (M190) sanity: d_L must be real, positive,
#    increasing on z in (0, 2] for q0 = -0.37 (paper plots it to z ~ 2)
def d_L(z, q0, c_over_H0=1.0):
    return (-c_over_H0 * (1 + z) ** 2 / q0
            * (1 - math.sqrt(1 + q0 - q0 / (1 + z) ** 2)))

zs = [0.1 * i for i in range(1, 21)]
vals = [d_L(z, q0_fit) for z in zs]
monotone = all(b > a for a, b in zip(vals, vals[1:]))
check("d_L(z; q0=-0.37) real, positive, increasing on (0,2]  [P3 M190]",
      monotone and all(v > 0 for v in vals),
      f"d_L(0.1)={vals[0]:.4f}, d_L(1.0)={vals[9]:.4f}, d_L(2.0)={vals[19]:.4f} "
      f"(units c/H0)")

# ------------------------------------------------------- scrambled control
print("\n--- Scrambled control (must FAIL the same battery) ---")
# Scramble kappa by 3 orders of magnitude: the cross-relations 1, 2, 6 must
# break. If they do not, this battery is theater.
kappa_scr = kappa * 1.0e3
c1 = 0.5 < kappa_scr / kappa_100mpc < 2.0
c2 = abs(gamma_0 / kappa_scr - 3.21e23) / 3.21e23 < 0.01
r_max_scr_kpc = (n_gamma + gamma_0) / (2.0 * kappa_scr) / KPC_CM
c6 = 30.0 < r_max_scr_kpc < 300.0
control_fails = not (c1 or c2 or c6)
check("scrambled kappa (x1e3) fails checks 1, 2, 6",
      control_fails,
      f"check1={c1}, check2={c2}, check6={c6} (all must be False); "
      f"scrambled R_max = {r_max_scr_kpc:.2f} kpc")

# ------------------------------------------------------------------ verdict
print("\n" + "=" * 76)
if FAIL:
    print(f"RESULT: FAIL ({len(FAIL)} failed: {', '.join(FAIL)})")
    sys.exit(1)
print("RESULT: ALL CHECKS PASS (9 relations + 1 control)")
print("Scope: transcription fidelity + papers' internal arithmetic only.")
print("No physics claim moved; extraction grade.")
sys.exit(0)
