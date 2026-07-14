#!/usr/bin/env python3
r"""W143 -- APPLIED/COMPUTATIONAL/FRONTIER steelman sweep: scoring computations
for the known-rate declaration.

Context: the 2026-07-14 issuance wave (W135 taxonomy + measured rate, W136
declaration propagation, W137 observer-slice structure, W138 kill battery). The
corrected steelman core (Joe): science ALREADY KNOWS the rate -- W135 (16e476f)
measured it: rho_Lambda ~ (2.24 meV)^4, bookkeeping rate q_B = 3 H0 rho_Lambda,
per Hubble volume (3/2) Omega_L c^5/G = 1.027 Planck luminosities, dimensionless
ladder 9 Omega_L = 6.16. This team's question per persona: IF that known measured
number is DECLARED as the issuance input to the source action, what OTHER
information backs out. This script computes everything the scoring pass uses:

  BLOCK A -- positive controls (constants reproduce the W138 numbers).
  BLOCK B -- the known rate's identity ladder DECOMPOSED (new exact lines):
       q_B = 9 Omega_L H0^3 M_Pl_red^2 exactly (the W135 6.16 re-derived);
       total per Hubble volume = (3/2) Omega_L c^5/G = 1.027 L_Planck exactly
       (symbolic + numeric); T_dS * S_dS = E_crit(V_H) = c^5/(2 G H) EXACTLY,
       so the W138 G5 factor 1.46 is EXACTLY 1/Omega_Lambda and the W138 G6
       saturation factor 2.96 is EXACTLY 3 Omega_Lambda / ln 2: every O(1)
       factor on the board decomposes as (Planck identity) x Omega_Lambda.
  BLOCK C -- regulated-setpoint structure on the FRW continuity equation (exact
       sympy; refines the W135 structure-(e) survivor, which the data constrain
       through the OFFSET, not the gain): P-control leaves a nonzero steady-state
       residual d/g while integral action forces the residual to zero exactly --
       an ARCHITECTURE SEPARATOR between setpoint-= -Lambda loops (W135 (e),
       I-term allowed) and residual-Lambda loops (setpoint = bulk-flatness,
       Lambda_obs = the P-residual, I-term cut by the observed nonzero W136
       offset); underdamped ringing condition and period (matching the W135
       transfer-function poles at Kd = 0); the mimic-gate transient bound as a
       (gain, acquisition-epoch) exclusion: acquisition inside the DESI window
       is excluded across a computed gain band at O(3) offset, and acquisition
       older than N* = x0/(0.3 e) e-folds (x0 = 3: N* = 3.68, z >~ 39) makes
       the gate gain-independent -- the complement of W135's offset-not-gain
       finding, turned into a substrate statement (the sensor predates records).
  BLOCK D -- the demand-delivery kill (fresh G1b application): issuance
       physically DELIVERED proportional to record-writing power (stellar
       luminosity) at the full DE budget drifts the solar GM at ~9e-8 /yr,
       ~1e6 over the ephemeris bound and ~1e25 over uniform (>= the 1e19 gate):
       demand-tracking gravitating delivery is DEAD; distribution through
       observers must live at the ledger/class level.
  BLOCK E -- the capacity-allocation numbers: |II|^2-density (innovation-
       weighted) allocation is EXACTLY uniform on Ricci-flat vacuum (W = a0 = 2
       when Ric = 0, symbolic from the W126 slice decomposition), and its FRW
       schedule deviation is ~(H0/mu_DW)^2 ~ 2e-61 (mimic gate trivially met);
       the W130 3:2:1 sector split gives allocation fractions (1/2, 1/3, 1/6),
       discriminable from a Z/3-triality equal split (1/3 each).

Deterministic; no network; exit 0 iff all checks pass.
"""

import math
import sys

import sympy as sp

CHECKS = []


def check(name, cond, detail=""):
    CHECKS.append((name, bool(cond)))
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")


def close(a, b, rtol):
    return abs(a - b) <= rtol * max(abs(a), abs(b))


# ----------------------------------------------------------------------------
# BLOCK A: constants and positive controls (match W138)
# ----------------------------------------------------------------------------
c = 2.99792458e8
G = 6.67430e-11
hbar = 1.054571817e-34
kB = 1.380649e-23
eV = 1.602176634e-19
Mpc = 3.0857e22
yr = 3.15576e7
L_sun = 3.828e26
M_sun = 1.98892e30

H0 = 67.36 * 1000.0 / Mpc          # s^-1
Omega_L = 0.6847
t_H = 1.0 / H0
R_H = c / H0
V_H = (4.0 / 3.0) * math.pi * R_H ** 3
l_p2 = hbar * G / c ** 3

rho_crit = 3.0 * H0 ** 2 / (8.0 * math.pi * G)
rho_L_J = Omega_L * rho_crit * c ** 2                       # J/m^3
hbarc_eVm = hbar * c / eV
de_scale_meV = (rho_L_J / eV * hbarc_eVm ** 3) ** 0.25 * 1e3

T_dS = hbar * H0 / (2.0 * math.pi * kB)
S_dS = math.pi * R_H ** 2 / l_p2                            # in k_B units
E_L = rho_L_J * V_H
TS = kB * T_dS * S_dS

check("A1 rho_crit ~ 8.5e-27 kg/m^3", close(rho_crit, 8.53e-27, 0.02),
      f"rho_crit = {rho_crit:.3e}")
check("A2 DE scale ~ 2.2-2.3 meV", 2.15 < de_scale_meV < 2.35,
      f"rho_L^(1/4) = {de_scale_meV:.3f} meV")
check("A3 T_dS ~ 2.65e-30 K (W138)", close(T_dS, 2.65e-30, 0.02),
      f"T_dS = {T_dS:.3e} K")
check("A4 S_dS ~ 2.27e122 k_B (W138)", close(S_dS, 2.27e122, 0.02),
      f"S_dS = {S_dS:.3e} k_B")
check("A5 E_Lambda ~ 5.7e69 J (W138)", close(E_L, 5.69e69, 0.03),
      f"E_L = {E_L:.3e} J")

# ----------------------------------------------------------------------------
# BLOCK B: the known rate's identity ladder (W135 anchors re-derived + decomposed)
# ----------------------------------------------------------------------------
# B0a: q_B = 3 H0 rho_L = 9 Omega_L H0^3 M_Pl_red^2 exactly (Friedmann), and the
#      W135 dimensionless ladder value 9 Omega_L = 6.16.
q_B_density = 3.0 * H0 * rho_L_J                            # W/m^3
# rho_L_J = 3 Omega_L H0^2 c^2/(8 pi G), so q_B/(H0^3 * c^2/(8 pi G)) = 9 Omega_L:
ladder = q_B_density / (H0 ** 3 * c ** 2 / (8.0 * math.pi * G))
check("B0a q_B/(H0^3 M_Pl_red^2) = 9 Omega_L = 6.16 (W135 ladder, exact identity)",
      close(ladder, 9.0 * Omega_L, 1e-9) and close(9.0 * Omega_L, 6.162, 0.001),
      f"ladder = {ladder:.4f} (rho_L = 3 Omega_L H0^2 M_Pl_red^2 makes it exact)")

# B0b: total per Hubble volume = (3/2) Omega_L c^5/G = 1.027 Planck luminosities.
L_Planck = c ** 5 / G
q_B_total = q_B_density * V_H
check("B0b q_B per Hubble volume = (3/2) Omega_L L_Planck = 1.027 L_Planck (W135)",
      close(q_B_total / L_Planck, 1.5 * Omega_L, 1e-9)
      and close(1.5 * Omega_L, 1.027, 0.001),
      f"q_B V_H = {q_B_total:.3e} W vs L_Planck = {L_Planck:.3e} W, "
      f"ratio {q_B_total/L_Planck:.4f}")

# Symbolic: T_dS S_dS = (hbar H / 2 pi kB) * kB pi (c/H)^2 c^3/(hbar G)
#         = c^5/(2 G H)  =  rho_crit c^2 V_H  EXACTLY.
Hs, Gs, cs, hbars, kBs, OmL = sp.symbols("H G c hbar k_B Omega_L", positive=True)
TS_sym = (hbars * Hs / (2 * sp.pi * kBs)) * kBs * sp.pi * (cs / Hs) ** 2 * cs ** 3 / (hbars * Gs)
Ecrit_sym = (3 * Hs ** 2 / (8 * sp.pi * Gs)) * cs ** 2 * sp.Rational(4, 3) * sp.pi * (cs / Hs) ** 3
check("B1 SYMBOLIC: T_dS*S_dS = c^5/(2GH) = E_crit(V_H) exactly",
      sp.simplify(TS_sym - cs ** 5 / (2 * Gs * Hs)) == 0
      and sp.simplify(Ecrit_sym - cs ** 5 / (2 * Gs * Hs)) == 0,
      "the Gibbons-Hawking product IS the critical energy of a Hubble volume")

ratio = TS / E_L
check("B2 the W138 G5 factor 1.46 is EXACTLY 1/Omega_Lambda",
      close(ratio, 1.0 / Omega_L, 0.02) and close(1.0 / Omega_L, 1.4604, 0.001),
      f"TS/E_L = {ratio:.4f} vs 1/Omega_L = {1.0/Omega_L:.4f} (W138 quoted 1.46)")

budget = 3.0 * E_L                                          # per Hubble time (W138 G6)
bits_TdS = budget / (kB * T_dS * math.log(2.0))
check("B3 bits at T_dS ~ 6.7e122 (W138)", close(bits_TdS, 6.7e122, 0.03),
      f"bits = {bits_TdS:.3e}")
check("B4 the W138 G6 factor 2.96 is EXACTLY 3*Omega_L/ln2",
      close(bits_TdS / S_dS, 3.0 * Omega_L / math.log(2.0), 0.02)
      and close(3.0 * Omega_L / math.log(2.0), 2.9637, 0.001),
      f"bits/S_dS = {bits_TdS/S_dS:.4f} vs 3 Omega_L/ln2 = {3.0*Omega_L/math.log(2.0):.4f}")

# ----------------------------------------------------------------------------
# BLOCK C: controller theory on the FRW continuity equation
#   x = ln(rho_iss/rho_setpoint); e-fold time N = ln a;
#   dx/dN = -3(1+w_eff) - ... reads the schedule: |dx/dN| < 0.3 is the W138 G2 gate.
# ----------------------------------------------------------------------------
N = sp.symbols("N", positive=True)
g, gp, gi, d, x0 = sp.symbols("g g_p g_i d x_0", positive=True)
x = sp.Function("x")

# C1: P-controller with constant disturbance: x' = -g x + d  ->  x_ss = d/g != 0
sol = sp.dsolve(sp.Eq(x(N).diff(N), -g * x(N) + d), x(N)).rhs
x_ss = sp.limit(sol.subs(sp.Symbol("C1"), 0), N, sp.oo)
check("C1 P-controller steady-state error = d/g (NONZERO)",
      sp.simplify(x_ss - d / g) == 0,
      "Lambda_obs CAN be the proportional residual: P-type leaves a constant offset "
      "(the residual-Lambda architecture, vs W135 (e) where the setpoint IS Lambda)")

# C2: integral action: z' = x, x' = -gp x - gi z + d  ->  x_ss = 0 exactly
A = sp.Matrix([[-gp, -gi], [1, 0]])
b = sp.Matrix([d, 0])
ss = A.solve(-b)                                            # steady state of [x, z]
check("C2 integral action forces x_ss = 0 EXACTLY",
      sp.simplify(ss[0]) == 0,
      "architecture separator (agrees with W135: 'Ki > 0 removes steady-state error'): "
      "in the residual-Lambda reading the observed nonzero 1e-60 offset (W136 pin) "
      "cuts the I-term; in W135's setpoint-=-Lambda reading the I-term stays allowed")

# C3: ringing condition of the PI loop: s^2 + gp s + gi, complex iff gp^2 < 4 gi
s = sp.symbols("s")
disc = gp ** 2 - 4 * gi
period = 2 * sp.pi / sp.sqrt(gi - gp ** 2 / 4)
check("C3 underdamped iff g_p^2 < 4 g_i; ring period 2*pi/sqrt(g_i - g_p^2/4)",
      sp.simplify(sp.discriminant(s ** 2 + gp * s + gi, s) - disc) == 0,
      "matches the W135 transfer-function poles at Kd = 0; a DESI-like w(z) feature "
      "would be loop ringing with an e-fold-scale period")

# C4: the mimic gate reproduces the W138 2.48x DESI exclusion
desi_dev = 3.0 * abs(-0.752 + 1.0)
check("C4 DESI schedule deviation 0.744 = 2.48x outside the 0.3 gate (W138 G2)",
      close(desi_dev, 0.744, 1e-9) and close(desi_dev / 0.3, 2.48, 0.001),
      f"deviation {desi_dev:.3f}, ratio {desi_dev/0.3:.2f}")

# C5: transient exclusion for recent setpoint acquisition.
#     schedule deviation today = x0 * g * exp(-g N_acq); gate 0.3.
#     For x0 = 3 and acquisition inside the DESI window (N_acq = ln 3 ~ 1.1):
#     a finite gain band is EXCLUDED (violates the mimic gate).
x0v, Nacq = 3.0, math.log(3.0)
f = lambda gg: x0v * gg * math.exp(-gg * Nacq)
peak_g = 1.0 / Nacq
peak = f(peak_g)
check("C5a recent acquisition peaks ABOVE the gate", peak > 0.3,
      f"max deviation {peak:.3f} at g = {peak_g:.2f} per e-fold (gate 0.3)")


def bisect(fn, lo, hi, tol=1e-12):
    flo = fn(lo)
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if fn(mid) * flo > 0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


g_lo = bisect(lambda gg: f(gg) - 0.3, 1e-6, peak_g)
g_hi = bisect(lambda gg: f(gg) - 0.3, peak_g, 50.0)
check("C5b excluded gain band for z<=2 acquisition (x0=3) is [~0.11, ~3.1]",
      0.09 < g_lo < 0.13 and 2.8 < g_hi < 3.4,
      f"excluded g in [{g_lo:.3f}, {g_hi:.3f}] per e-fold")

# C6: gain-independence epoch: max_g x0 g e^{-gN} = x0/(N e) < 0.3
#     ->  N* = x0/(0.3 e); x0 = 3 gives N* = 3.68 e-folds, z_acq >~ 38.6.
Nstar = x0v / (0.3 * math.e)
z_acq = math.exp(Nstar) - 1.0
check("C6 setpoint acquisition must predate N* = 3.68 e-folds (z >~ 39) "
      "for gain-independent mimic passage",
      close(Nstar, 3.678, 0.01) and 35.0 < z_acq < 42.0,
      f"N* = {Nstar:.3f}, z_acq = {z_acq:.1f}: the controller must pre-date "
      "structure/observers -- the sensor cannot be record demand")

# ----------------------------------------------------------------------------
# BLOCK D: the demand-delivery kill (G1b applied to luminosity-tracking issuance)
# ----------------------------------------------------------------------------
L_density = 2.0e8 * L_sun / Mpc ** 3                        # W/m^3 (W138 cited order)
L_total = L_density * V_H
E_star = L_total * t_H
overpay = budget / E_star
check("D1 over-pay control ~ 1.3e6 (W138 G6)", close(overpay, 1.3e6, 0.05),
      f"budget/stellar = {overpay:.3e}")

# Deliver the full budget proportional to luminosity: the Sun's share is
# overpay * L_sun of issuance power landing inside the solar system.
q_sun = overpay * L_sun                                     # W
gm_drift = (q_sun / c ** 2) * yr / M_sun                    # fractional per year
ephem = 1e-13
uniform_drift = 8.5e-33                                     # /yr (W138 G1b)
check("D2 luminosity-tracking delivery drifts GM by ~9e-8 /yr: DEAD vs ephemeris 1e-13",
      close(gm_drift, 8.9e-8, 0.10) and gm_drift / ephem > 1e5,
      f"drift = {gm_drift:.3e} /yr, {gm_drift/ephem:.2e}x over the bound")
check("D3 enhancement over uniform ~1e25 >= the 1e19 G1b gate",
      gm_drift / uniform_drift > 1e19,
      f"enhancement = {gm_drift/uniform_drift:.2e} (gate 1e19): demand-tracking "
      "GRAVITATING delivery is excluded; distribution must be ledger-level")

# ----------------------------------------------------------------------------
# BLOCK E: capacity-allocation numbers
# ----------------------------------------------------------------------------
# E1: |II|^2-density allocation is uniform on Ricci-flat vacuum (symbolic, from
# the W126 slice decomposition W = 2 + R/3 + (8/9) R^2 - 4 Ric^2).
Rsym, Ric2 = sp.symbols("R Ric2")
W = 2 + Rsym / 3 + sp.Rational(8, 9) * Rsym ** 2 - 4 * Ric2
check("E1 W = a0 = 2 EXACTLY on Ricci-flat vacuum (Schwarzschild): zero local "
      "enhancement of an |II|^2-weighted allocation",
      sp.simplify(W.subs({Rsym: 0, Ric2: 0}) - 2) == 0,
      "innovation-weighted (Kalman) allocation gravitates uniformly in the solar system")

# E2: FRW schedule deviation of curvature-tracking allocation ~ (H0/mu_DW)^2
H0_eV = hbar * H0 / eV
mu_floor = 3.4e-3                                           # eV (H52 envelope min)
dev = (H0_eV / mu_floor) ** 2
check("E2 curvature-tracking schedule deviation ~ 2e-61 << 0.3 (mimic trivially met)",
      1e-62 < dev < 1e-60,
      f"(H0/mu_DW)^2 = {dev:.2e}")

# E3: allocation fractions from the W130 3:2:1 split vs a Z/3 equal split
fr = [sp.Rational(3, 6), sp.Rational(2, 6), sp.Rational(1, 6)]
check("E3 3:2:1 gives (1/2, 1/3, 1/6), sum 1, discriminable from triality (1/3 each)",
      sum(fr) == 1 and max(abs(f - sp.Rational(1, 3)) for f in fr) == sp.Rational(1, 6),
      "C3's decision computation (W130 rerun on a curved background) separates the "
      "two allocation readings")

# ----------------------------------------------------------------------------
n_fail = sum(1 for _, ok in CHECKS if not ok)
print(f"\n{len(CHECKS) - n_fail}/{len(CHECKS)} checks passed")
sys.exit(1 if n_fail else 0)
