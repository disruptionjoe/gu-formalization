#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
W146 -- everpresent-Lambda / Y14-substrate scoring checks (theoretical-physics family).

Deterministic arithmetic behind the W146 substrate steelman sweep. The load-bearing
computation is the PORTED Sorkin everpresent-Lambda amplitude test (Ahmed-Dodelson-
Greene-Sorkin, astro-ph/0209274): Lambda ~ +/- 1/sqrt(N), N = substrate element count
= spacetime 4-volume in Planck units. We check whether that amplitude reproduces the
observed rho_L ~ (2.24 meV)^4, compare the residual to W135's 9 Omega_L = 6.16, test the
de Sitter-relabeling (G5) coincidence sqrt(N_4) = S_dS, and show that a naive full-14-dim
Y14 Planck sprinkle catastrophically underpredicts (so the Y14->X4 projection must collapse
the effective counting dimension to 4 -- the shadow-map constraint).

Everything is a PORT labelled as such; nothing here asserts GU. Exploration grade, no canon.

Run: python -u tests/W146_everpresent_lambda_substrate_checks.py   (expect NN/NN, exit 0)
"""

import math

CHECKS = []


def check(name, got, expected, rel=2e-2):
    ok = (expected == 0 and abs(got) < 1e-12) or abs(got - expected) <= rel * abs(expected)
    CHECKS.append((name, got, expected, ok))
    flag = "ok " if ok else "XX "
    print(f"  [{flag}] {name}: got {got:.6g}  expected {expected:.6g}")
    return ok


# ---------------------------------------------------------------------------
# Constants (SI / cosmology; same anchors used by W135/W138/W140/W141)
# ---------------------------------------------------------------------------
c      = 2.99792458e8          # m/s
G      = 6.67430e-11           # m^3 kg^-1 s^-2
hbar   = 1.054571817e-34       # J s
kB     = 1.380649e-23          # J/K
Mpc    = 3.0856775814913673e22 # m
eV     = 1.602176634e-19       # J

H0_kms = 67.36                 # km/s/Mpc  (Planck 2018)
Omega_L = 0.6847

H0   = H0_kms * 1e3 / Mpc                     # s^-1
R_H  = c / H0                                 # Hubble radius, m
l_p  = math.sqrt(hbar * G / c**3)             # Planck length, m
t_p  = l_p / c                                # Planck time, s
E_p  = math.sqrt(hbar * c**5 / G)             # Planck energy, J
M_pl = E_p                                    # Planck mass energy, J (non-reduced)

print("=== Positive controls: background scales ===")
# rho_crit (energy density) and the observed DE scale (W138/W135 control)
rho_crit = 3 * H0**2 * c**2 / (8 * math.pi * G)      # J/m^3
rho_L    = Omega_L * rho_crit                          # J/m^3
# rho_L^{1/4} in meV
rho_L_scale_meV = ((rho_L * (hbar * c)**3) ** 0.25) / eV * 1e3
check("C1 observed rho_L^{1/4} (meV)", rho_L_scale_meV, 2.24, rel=3e-2)
check("C2 Hubble/Planck length ratio R_H/l_p", R_H / l_p, 8.5e60, rel=5e-2)

# de Sitter horizon entropy (W138 G5 control)
S_dS = math.pi * R_H**2 / l_p**2                       # in k_B
check("C3 de Sitter entropy S_dS / 1e122 (k_B)", S_dS / 1e122, 2.27, rel=5e-2)

print("\n=== W135 dimensionless anchors (reproduced) ===")
# 9 Omega_L = 6.16  and  (3/2) Omega_L = 1.027
check("N8 9*Omega_L", 9 * Omega_L, 6.16, rel=2e-2)
check("N7 (3/2)*Omega_L", 1.5 * Omega_L, 1.027, rel=2e-2)

print("\n=== PORTED: Sorkin everpresent-Lambda amplitude (ADGS astro-ph/0209274) ===")
# N_4 = spacetime 4-volume in Planck units. Take the causal 4-volume ~ R_H^4
# (Hubble 4-volume; ADGS use the past volume, same order).
N4 = (R_H / l_p) ** 4
check("E1 N_4 = (R_H/l_p)^4 / 1e243", N4 / 1e243, 5.21, rel=1e-1)
check("E2 sqrt(N_4) / 1e121", math.sqrt(N4) / 1e121, 7.22, rel=1e-1)

# Everpresent prediction: dimensionless Lambda l_p^2 ~ 1/sqrt(N_4)
Lambda_pred_dimless = 1.0 / math.sqrt(N4)
# Observed: Lambda = 3 Omega_L H0^2/c^2  =>  Lambda l_p^2 = 3 Omega_L (l_p/R_H)^2
Lambda_obs_dimless = 3 * Omega_L * (l_p / R_H) ** 2
check("E3 predicted Lambda*l_p^2 / 1e-122", Lambda_pred_dimless / 1e-122, 1.385, rel=5e-2)
check("E4 observed  Lambda*l_p^2 / 1e-122", Lambda_obs_dimless / 1e-122, 2.846, rel=5e-2)

# THE HEADLINE: observed/predicted residual = 3 Omega_L exactly (since predicted = (l_p/R_H)^2)
ratio_obs_pred = Lambda_obs_dimless / Lambda_pred_dimless
check("E5 residual (obs/pred) = 3*Omega_L", ratio_obs_pred, 3 * Omega_L, rel=1e-3)
check("E5b residual numeric value", ratio_obs_pred, 2.054, rel=1e-2)

# Scale-level match: predicted rho_L^{1/4} vs observed 2.24 meV
# rho_pred/rho_obs = 1/(3 Omega_L); scale ratio = (that)^{1/4}
scale_ratio = (1.0 / (3 * Omega_L)) ** 0.25
rho_L_pred_scale_meV = scale_ratio * rho_L_scale_meV
check("E6 predicted rho_L^{1/4} (meV)", rho_L_pred_scale_meV, 1.87, rel=3e-2)

print("\n=== Comparison to W135's O(1) ratio ===")
# Everpresent residual (3 Omega_L) vs W135 rate ratio (9 Omega_L). Ratio = 3.
check("R1 (9 Omega_L)/(3 Omega_L) = 3", (9 * Omega_L) / (3 * Omega_L), 3.0, rel=1e-6)
# Both are O(1)*Omega_L; the everpresent residual is the SMALLER, and unlike 9 Omega_L
# it is the leftover of a genuine magnitude prediction (predicts the 10^-122; 9 Omega_L
# presupposes it). Recorded as a labelled contrast, not a numeric claim.

print("\n=== G5 (de Sitter relabeling) coincidence: sqrt(N_4) = S_dS ===")
# sqrt((R_H/l_p)^4) = (R_H/l_p)^2 = area in Planck units = S_dS/pi. So the everpresent
# MAGNITUDE numerically coincides with the holographic/dS magnitude. Novelty of everpresent
# lives in the FLUCTUATING SIGN/time-dependence, not the magnitude.
check("G5a sqrt(N_4) / (S_dS/pi)", math.sqrt(N4) / (S_dS / math.pi), 1.0, rel=1e-6)
check("G5b 1/sqrt(N_4) vs pi/S_dS", (1.0 / math.sqrt(N4)) / (math.pi / S_dS), 1.0, rel=1e-6)

print("\n=== Y14 shadow-map constraint: full-14-dim sprinkle catastrophe ===")
# If records were Planck-sprinkled in the FULL 14-dim Y14 volume, the count would be
# N_14 = (R_H/l_p)^14 and Lambda ~ 1/sqrt(N_14) = (l_p/R_H)^7 -- absurdly small.
# So the Y14->X4 projection MUST collapse the effective counting dimension to 4
# (Lambda is conjugate to the X4 shadow 4-volume). This is the quantitative form of
# the shadow-map requirement.
log10_Lambda_14 = -7 * math.log10(R_H / l_p)        # log10 of 1/sqrt(N_14)
check("Y1 log10(Lambda*l_p^2) if 14-dim sprinkle", log10_Lambda_14, -426.7, rel=2e-3)
# The 4-dim (base) counting is the one that works: exponent -2 not -7.
log10_Lambda_4 = -2 * math.log10(R_H / l_p)
check("Y2 log10(Lambda*l_p^2) if 4-dim base count", log10_Lambda_4, -121.7, rel=2e-3)

print("\n=== Measurement-gated count: N_measured, and the GU-specific density target ===")
# THIRD CLARIFICATION (Joe): the Y14->X4 projection is MEASUREMENT-GATED -- only OBSERVED
# (promoted) Y14 records become measured X4 components. So the count driving shadow-Lambda
# is N_measured, a count of X4 events (this is WHY the effective dimension is 4, not 14:
# the promotion lands records in the 4-dim shadow). N_measured = phi * N_4, phi = measured-
# record 4-density as a fraction of Planck density.
#
# Direction check: predicted Lambda*l_p^2 = 1/sqrt(N_measured). The full-Planck count
# (phi = 1) UNDERpredicts (obs/pred = 3 Omega_L = 2.054), so to hit observed EXACTLY the
# measured count must be SPARSER than Planck-4-density:
#     N_measured = N_4 / (3 Omega_L)^2   <=>   phi = 1/(3 Omega_L)^2.
phi_target = 1.0 / (3 * Omega_L) ** 2
check("F1 measured-density fraction phi = 1/(3 Omega_L)^2", phi_target, 0.237, rel=1e-2)
# With that sparsity, the measurement-gated prediction hits observed rho_L by construction:
N_measured = N4 * phi_target
Lambda_meas_dimless = 1.0 / math.sqrt(N_measured)
check("F2 measurement-gated Lambda*l_p^2 = observed", Lambda_meas_dimless, Lambda_obs_dimless, rel=1e-3)
# HONEST: phi is one free number, so the MATCH is a fit, not a prediction; the predictive
# content is whether the (9,5)/gimmel measurement structure DERIVES phi = 1/(3 Omega_L)^2.
# What the measurement gate DOES buy predictively is the dimension collapse 14 -> 4 (Y1/Y2),
# which the bare causal-set port had to assume. phi ~ 1/4 is O(1), not a fine-tuning.
check("F3 phi is O(1) (0.05 < phi < 1) -> 1", 1.0 if 0.05 < phi_target < 1.0 else 0.0, 1.0)

print("\n=== W138 battery anchors reused (controls) ===")
# G3 H36 non-reimport envelope factor (mu_floor/2.3)^4 at 3.4 meV
check("B-G3 (3.4/2.3)^4", (3.4 / 2.3) ** 4, 4.775, rel=1e-2)
# G2 mimic: DESI CPL schedule need vs band
check("B-G2 0.744/0.3", 0.744 / 0.3, 2.48, rel=1e-2)
# G5 dS ratio E_Lambda vs T_dS S_dS
T_dS = H0 / (2 * math.pi) * hbar / kB          # K
E_Lambda = rho_L * (4.0 / 3.0) * math.pi * R_H**3
TS = (T_dS * kB) * S_dS
check("B-G5 T_dS S_dS / E_Lambda", TS / E_Lambda, 1.46, rel=5e-2)

# ---------------------------------------------------------------------------
n_ok = sum(1 for *_ , ok in CHECKS if ok)
n = len(CHECKS)
print(f"\n{n_ok}/{n} checks passed")
import sys
sys.exit(0 if n_ok == n else 1)
