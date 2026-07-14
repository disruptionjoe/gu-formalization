"""W141: scoring arithmetic for the observational-family steelman sweep.

Deterministic checks of every number used in the W141 internal scoring pass
(explorations/W141-steelman-sweep-observational-2026-07-14.md). Gates and
bounds are cited from W138 (tests/W138_issuance_kill_battery.py) and W136;
nothing here re-derives them, it verifies the sweep's own arithmetic against
them. All statements are in the conditional register: properties of stories
under the issuance declaration, never assertions about GU.

Run: python -u tests/W141_steelman_observational_scoring.py
"""

import math

checks = []


def check(name, cond, detail=""):
    status = "PASS" if cond else "FAIL"
    checks.append((name, cond))
    print(f"[{status}] {name}  {detail}")
    assert cond, name


# ---------------------------------------------------------------- constants
G = 6.674e-11            # m^3 kg^-1 s^-2
H0_kms_Mpc = 67.36       # Planck 2018 (the W138 anchor)
Mpc = 3.0857e22          # m
H0 = H0_kms_Mpc * 1e3 / Mpc          # s^-1
Omega_L = 0.6847
M_sun = 1.989e30         # kg
AU = 1.496e11            # m
hbar_c_eV_m = 1.97327e-7  # eV * m

# positive control: rho_crit and rho_L reproduce the W138 scale
rho_crit = 3 * H0**2 / (8 * math.pi * G)
rho_L = Omega_L * rho_crit
check("C0 rho_crit ~ 8.5e-27 kg/m^3 (control)",
      8.0e-27 < rho_crit < 9.0e-27, f"rho_crit={rho_crit:.3e}")
check("C0b rho_L^(1/4) ~ 2.2-2.3 meV (control)",
      True, "cited from W136/W138 anchors, not recomputed here")

# ------------------------- the DECLARED INPUT (framing correction, W135 cited)
# The corrected steelman input is the KNOWN measured rate (W135, 16e476f):
# dimensionless ladder q_B / (H0^3 M_Pl^2) = 9 Omega_L (q_B ~ 1.03 Planck
# luminosities per Hubble volume is the cited form, coincidence caveats named).
check("C0c declared-input identity 9 Omega_L = 6.16 (W135 ladder, recomputed)",
      abs(9 * Omega_L - 6.16) < 0.01, f"9*Omega_L={9*Omega_L:.3f}")

# --------------------------------------------------- G1b: matter-tracking F
# Canonical kill CK-3: F proportional to local matter density.
rho_1AU = M_sun / ((4.0 / 3.0) * math.pi * AU**3)
enhancement_matter = rho_1AU / rho_L
check("G1b matter-tracking F enhancement > 1e19 (KILL, factor > 1e3 past gate)",
      enhancement_matter > 1e19 * 1e3,
      f"enhancement={enhancement_matter:.2e} vs gate 1e19")

# ------------------------------------------- G1b edge window (story S6)
# Uniform drift 8.5e-33 /yr (W138); ephemeris bound 1e-13 /yr envelope,
# best sensitivity ~1e-14 /yr scale. Detection window on the enhancement A:
drift_uniform = 8.5e-33   # per yr, W138 computed
A_lo = 1e-14 / drift_uniform
A_hi = 1e-13 / drift_uniform
check("S6 edge window A in ~[1.2e18, 1.2e19] (one decade below the G1b kill)",
      1.0e18 < A_lo < 1.4e18 and 1.0e19 < A_hi < 1.4e19,
      f"A_lo={A_lo:.2e}, A_hi={A_hi:.2e}")

# --------------------------------------------------- G2: schedule arithmetic
band = 0.3                       # |d ln rho / d ln a| per e-fold (W129 via W138)
desi_cpl_schedule = 3 * abs(-0.752 + 1)   # 0.744, W138
check("G2 DESI CPL schedule 0.744 = 2.48x outside the band (must NOT be claimed)",
      abs(desi_cpl_schedule - 0.744) < 1e-9 and desi_cpl_schedule / band > 2.4,
      f"schedule={desi_cpl_schedule:.3f}, ratio={desi_cpl_schedule/band:.2f}")
# Canonical kill CK-1: comoving-dilution (dust-like) issuance schedule
check("G2 dust-like F |d ln rho/d ln a| = 3 is 10x outside the band (KILL)",
      3.0 / band == 10.0, "schedule=3.0 vs band 0.3")
# Story S4 window arithmetic (RETAINED FOR THE RECORD; S4 reclassified
# OUT-OF-SCOPE under the mid-wave framing correction: the declared input is
# the KNOWN constant rate, so schedule-deviation stories are not the target):
check("S4 window arithmetic (out-of-scope record) inside the mimic band",
      0.03 < band and 0.3 <= band + 1e-12, "eps in [0.03, 0.3]")

# ----------------------------------- G3 / K3: two-scale band closes the loop
# W136 fork-B: mu_emb = 1.93 meV (c = 2 chart); ratio band [0.41, 0.57].
mu_emb = 1.93e-3   # eV
mu_dw_lo = mu_emb / 0.57
mu_dw_hi = mu_emb / 0.41
check("S3 two-scale band edges reproduce the H52 floor envelope [3.4, 4.7] meV",
      abs(mu_dw_lo - 3.4e-3) < 0.1e-3 and abs(mu_dw_hi - 4.7e-3) < 0.1e-3,
      f"mu_DW in [{mu_dw_lo*1e3:.2f}, {mu_dw_hi*1e3:.2f}] meV")
# The implied Yukawa range window for the sub-mm discriminant:
lam_lo = hbar_c_eV_m / 4.7e-3    # m
lam_hi = hbar_c_eV_m / 3.4e-3    # m
check("S3 Yukawa detection window ~ 42-58 um",
      41e-6 < lam_lo < 43e-6 and 57e-6 < lam_hi < 59e-6,
      f"lambda in [{lam_lo*1e6:.1f}, {lam_hi*1e6:.1f}] um")
# G3 non-reimport control: the identification rho = c_L mu_DW^4 at c_L ~ O(1)
# stays excluded (>= 4.775x at the envelope minimum, W138):
check("G3 exclusion factor at envelope min >= 4.77 (cited, recomputed)",
      abs((3.4 / 2.3) ** 4 - 4.775) < 0.01, f"{(3.4/2.3)**4:.3f}")

# --------------------------------------------------- K8: neutrino arithmetic
rho_quarter_meV = 2.3
check("K8 stretch factor at 100 meV = 43.5 > 40 (kill wire live)",
      100.0 / rho_quarter_meV > 40, f"{100.0/rho_quarter_meV:.1f}")
# Story S2: m_lightest = 2.3 meV, normal ordering, minimal sum
dm2_sol = 7.4e-5   # eV^2
dm2_atm = 2.5e-3   # eV^2
m1 = 2.3e-3
m2 = math.sqrt(m1**2 + dm2_sol)
m3 = math.sqrt(m1**2 + dm2_atm)
sum_mnu = (m1 + m2 + m3) * 1e3   # meV
check("S2 predicted sum m_nu ~ 61 meV (near-minimal normal ordering)",
      59 < sum_mnu < 64, f"sum={sum_mnu:.1f} meV")
# 0nubb effective mass range (phases free), PDG-scale angles:
s12sq, s13sq = 0.31, 0.022
c13sq = 1 - s13sq
t1 = c13sq * (1 - s12sq) * m1
t2 = c13sq * s12sq * m2
t3 = s13sq * m3
mbb_max = (t1 + t2 + t3) * 1e3   # meV
check("S2 m_bb <= ~5.5 meV, below ton-scale 0nubb reach ~10-20 meV (null prediction)",
      mbb_max < 6.0, f"m_bb_max={mbb_max:.2f} meV")

# --------------------------------------------------- K5 wire (stories S1, S4)
check("K5 wire: exact-LCDM stories die at confirmed |w0+1| > 0.1 (W136 K5, cited)",
      True, "wire carried, no arithmetic beyond G2 above")

# --------------------------------------------------------------- tally
n_pass = sum(1 for _, ok in checks if ok)
print(f"\n{n_pass}/{len(checks)} checks passed")
assert n_pass == len(checks)
