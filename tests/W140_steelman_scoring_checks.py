"""W140 steelman-sweep scoring checks (theoretical-physics family, Family A).

Deterministic arithmetic backing the scoring pass in
explorations/W140-steelman-sweep-theoretical-physics-2026-07-14.md.

Positive controls first (reproduce W138 battery anchors), then the new
scoring numbers computed for this wave:

  C1-C4   controls: DE scale from Planck anchors, H36 exclusion factor,
          de Sitter relabeling ratio 1.46, Landauer stellar gap ~1.3e6
  N1      two-scale escape band vs H52 floor envelope intersection
          (story A9-1 / A13 cross-check; the m2_eff pin question)
  N2      SFH-tracking issuance schedule vs the G2 mimic gate (kill, A5-1)
  N3      Q-curvature issuance dimensional kill factor (~6e120, A8-1)
  N4      halo-density-weighted distribution vs the G1b 1e19 gate (A12-2)
  N5      Gibbs-measure sign check at the W136 pinned point (A3-1)
  N6      mimic-gate arithmetic: DESI signal 2.48x outside (control)
  N7-N8   the W135 measured rate reproduced (framing-correction anchor):
          Q_tot per Hubble volume = (3/2) Omega_L c^5/G = 1.027 Planck
          luminosities; dimensionless q_B/(H0^3 M_Pl,red^2) = 9 Omega_L = 6.16

Run: python tests/W140_steelman_scoring_checks.py   (exit 0 on pass)
"""

import math
import sys

checks = []


def check(name, ok, detail=""):
    checks.append((name, bool(ok), detail))
    print(("PASS " if ok else "FAIL ") + name + ("  | " + detail if detail else ""))


# ----- shared constants (SI; same anchors as W138) -----
c = 2.99792458e8          # m/s
G = 6.67430e-11           # m^3 kg^-1 s^-2
hbar = 1.054571817e-34    # J s
kB = 1.380649e-23         # J/K
lp = 1.616255e-35         # m
eV = 1.602176634e-19      # J
Mpc = 3.0856775814913673e22  # m
Msun = 1.98892e30         # kg
Lsun = 3.828e26           # W

H0 = 67.36e3 / Mpc        # s^-1  (Planck 2018)
Omega_L = 0.6847
Omega_m = 0.3153

rho_crit = 3.0 * H0**2 / (8.0 * math.pi * G)
rho_L = Omega_L * rho_crit
R_H = c / H0
V_H = (4.0 / 3.0) * math.pi * R_H**3
t_H = 1.0 / H0

# ----- C1: DE scale control -----
hbarc = hbar * c
rho_L_energy = rho_L * c**2                       # J/m^3
scale_J = (rho_L_energy * hbarc**3) ** 0.25       # J
scale_meV = scale_J / eV * 1e3
check("C1 DE scale ~2.24 meV (Planck anchors, W136 value)",
      abs(scale_meV - 2.24) < 0.03, f"computed {scale_meV:.3f} meV")

# ----- C2: H36 exclusion factor control (W138 G3) -----
f_env = (3.4 / 2.3) ** 4
check("C2 H36 envelope-min exclusion factor 4.775 (W138 G3)",
      abs(f_env - 4.775) < 0.01, f"computed {f_env:.3f}")

# ----- C3: de Sitter relabeling ratio control (W138 G5) -----
T_dS = hbar * H0 / (2.0 * math.pi * kB)
S_dS = math.pi * R_H**2 / lp**2                   # in kB units
E_L = rho_L_energy * V_H
ratio_dS = (T_dS * S_dS * kB) / E_L
check("C3 T_dS S_dS / E_Lambda = 1.46 (W138 G5)",
      abs(ratio_dS - 1.46) < 0.01, f"computed {ratio_dS:.4f}")

# ----- C4: Landauer stellar gap control (W138 G6) -----
budget = 3.0 * E_L                                # J per Hubble time
lum_density = 2e8 * Lsun / Mpc**3                 # W/m^3 (cited order)
stellar = lum_density * V_H * t_H                 # J per Hubble time
gap = budget / stellar
check("C4 Landauer/stellar gap ~1.3e6 (W138 G6)",
      1.2e6 < gap < 1.45e6, f"computed {gap:.3e}")

# ----- N1: two-scale escape band vs H52 floor envelope -----
# W136: mu_emb = 1.93 meV (c = 2 chart), 2.94 meV (c = 3/8 chart);
# escape band mu_emb/mu_DW in [0.41, 0.57] (c=2) and [0.63, 0.85] (c=3/8);
# H52 floor envelope mu_DW in [3.4, 4.7] meV; central floors 3.71 (m2_eff=5/4)
# and 4.54 (m2_eff=5/6).
floor_lo, floor_hi = 3.4, 4.7
floors_central = {"m2_eff=5/4": 3.71, "m2_eff=5/6": 4.54}

results = {}
for chart, (mu_emb, r_lo, r_hi) in {
    "c=2": (1.93, 0.41, 0.57),
    "c=3/8": (2.94, 0.63, 0.85),
}.items():
    mu_dw_lo, mu_dw_hi = mu_emb / r_hi, mu_emb / r_lo   # implied mu_DW range
    ov_lo, ov_hi = max(mu_dw_lo, floor_lo), min(mu_dw_hi, floor_hi)
    ratios = {k: mu_emb / v for k, v in floors_central.items()}
    results[chart] = (mu_dw_lo, mu_dw_hi, ov_lo, ov_hi, ratios)
    print(f"  [{chart}] implied mu_DW in [{mu_dw_lo:.3f}, {mu_dw_hi:.3f}] meV;"
          f" overlap with floor envelope [{ov_lo:.3f}, {ov_hi:.3f}];"
          f" ratio at central floors: "
          + ", ".join(f"{k}: {v:.3f}" for k, v in ratios.items()))

# c=2 chart: implied range [3.386, 4.707] vs envelope [3.4, 4.7]: near-total overlap
lo2, hi2, ov_lo2, ov_hi2, r2 = results["c=2"]
check("N1a c=2 chart: escape band and floor envelope intersect (non-empty)",
      ov_lo2 < ov_hi2, f"overlap [{ov_lo2:.3f}, {ov_hi2:.3f}] meV")
check("N1b c=2 chart: BOTH central m2_eff floors sit inside the band "
      "(m2_eff NOT pinned by the current envelope)",
      all(0.41 <= v <= 0.57 for v in r2.values()),
      ", ".join(f"{k}: {v:.3f}" for k, v in r2.items()))
lo38, hi38, ov_lo38, ov_hi38, r38 = results["c=3/8"]
check("N1c c=3/8 chart: escape band and floor envelope intersect (non-empty)",
      ov_lo38 < ov_hi38, f"overlap [{ov_lo38:.3f}, {ov_hi38:.3f}] meV")
check("N1d c=3/8 chart: BOTH central m2_eff floors inside the band",
      all(0.63 <= v <= 0.85 for v in r38.values()),
      ", ".join(f"{k}: {v:.3f}" for k, v in r38.items()))
# Falsifier sharpness: a resolved sub-mm floor above the implied maximum kills the chart
check("N1e falsifier: floor > 4.71 meV kills the c=2 chart outright "
      "(~1.4x sharper floor than current envelope min)",
      hi2 < 4.71, f"c=2 implied max mu_DW = {hi2:.3f} meV")

# ----- N2: SFH-tracking schedule vs G2 mimic gate (kill computation) -----
# Madau-Dickinson (2014): psi(z) prop (1+z)^2.7 / (1 + ((1+z)/2.9)^5.6).
# d ln psi / d ln(1+z) = 2.7 - 5.6 x/(1+x),  x = ((1+z)/2.9)^5.6;
# d ln a = -d ln(1+z), so |d ln rho / d ln a| = |that|.
def sfh_slope(z):
    x = ((1.0 + z) / 2.9) ** 5.6
    return 2.7 - 5.6 * x / (1.0 + x)

max_slope = max(abs(sfh_slope(z / 1000.0)) for z in range(0, 2001))
kill_factor = max_slope / 0.3
check("N2 SFH-tracking issuance schedule violates G2 mimic gate by ~9x "
      "(max |d ln rho/d ln a| over z<=2, worst at z~0)",
      8.5 < kill_factor < 9.5,
      f"max slope {max_slope:.3f} per e-fold vs 0.3; factor {kill_factor:.2f}x")

# ----- N3: Q-curvature issuance dimensional kill -----
# A dimensionless-coefficient curvature-invariant issuance density scales as H^4;
# needed density is (2.24 meV)^4. Kill factor = (scale_DE / (hbar H0))^4.
H0_eV = hbar * H0 / eV
kill_Q = (scale_meV * 1e-3 / H0_eV) ** 4
check("N3 curvature-invariant (Q-curvature/H^4) issuance underpays DE by ~6e120",
      1e120 < kill_Q < 1e121, f"factor {kill_Q:.2e} (H0 = {H0_eV:.3e} eV)")

# ----- N4: halo-density-weighted distribution vs G1b -----
# q(x) prop rho_m(x)/rho_m_mean. Local (solar-neighborhood) dynamical density
# ~0.1 Msun/pc^3 (cited order). Enhancement over uniform must stay < ~1e19.
pc = Mpc / 1e6
rho_local = 0.1 * Msun / pc**3
rho_m_mean = Omega_m * rho_crit
enhancement = rho_local / rho_m_mean
headroom = 1e19 / enhancement
check("N4 halo-density-weighted issuance: local enhancement ~2.5e6, "
      "clears the G1b gate with ~4e12 headroom",
      1e6 < enhancement < 1e7 and headroom > 1e12,
      f"enhancement {enhancement:.2e}; headroom {headroom:.2e}")

# ----- N5: Gibbs-measure sign check at the W136 pinned point -----
# W136: at beta/alpha* = 2 the family scalar-channel coefficient is c_R = -4/3,
# so f0^2 = 1/(6 c_R) = -1/8 < 0: the tree scalaron stays tachyonic and a
# Gibbs measure over sections is unbounded below at tree on the AF/native side.
c_R = -4.0 / 3.0
f0sq = 1.0 / (6.0 * c_R)
check("N5 pinned-point f0^2 = -1/8 < 0: tree Gibbs measure over sections "
      "unbounded below (AS-branch selector leg, W136/W128)",
      abs(f0sq + 0.125) < 1e-12 and f0sq < 0, f"f0^2 = {f0sq}")

# ----- N6: mimic-gate arithmetic control -----
desi_dev = 3.0 * abs(-0.752 + 1.0)
factor = desi_dev / 0.3
check("N6 DESI CPL signal needs 0.744 per e-fold = 2.48x outside G2 (W138)",
      abs(desi_dev - 0.744) < 1e-9 and abs(factor - 2.48) < 0.01,
      f"deviation {desi_dev:.3f}, factor {factor:.2f}x")

# ----- N7: W135 measured rate, Planck-luminosity form -----
# Bookkeeping issuance per Hubble volume: Q_tot = 3 H0 rho_L c^2 V_H
# = (3/2) Omega_L c^5 / G (exact identity) = 1.027 Planck luminosities (W135).
Q_tot = 3.0 * H0 * rho_L_energy * V_H          # W
L_planck = c**5 / G                             # W
ratio_LP = Q_tot / L_planck
identity = 1.5 * Omega_L                        # (3/2) Omega_L, exact form
check("N7 W135 measured rate: Q_tot/L_Planck = (3/2) Omega_L = 1.027 (to 3%)",
      abs(ratio_LP - identity) < 1e-12 and abs(ratio_LP - 1.027) < 0.005,
      f"computed {ratio_LP:.4f}; exact (3/2) Omega_L = {identity:.4f}")

# ----- N8: W135 dimensionless ladder -----
# q_B/(H0^3 M_Pl,red^2) = 9 Omega_L with rho_crit = 3 H0^2 M_Pl,red^2
# (natural units, reduced Planck mass); the O(1) ratio W135 flags as THE ladder.
dimensionless = 9.0 * Omega_L
check("N8 W135 dimensionless rate q_B/(H0^3 M_Pl,red^2) = 9 Omega_L = 6.16",
      abs(dimensionless - 6.16) < 0.01, f"computed {dimensionless:.4f}")

# ----- summary -----
n_fail = sum(1 for _, ok, _ in checks if not ok)
print(f"\n{len(checks) - n_fail}/{len(checks)} checks passed")
sys.exit(1 if n_fail else 0)
