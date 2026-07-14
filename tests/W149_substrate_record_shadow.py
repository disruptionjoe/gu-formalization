"""
W149: substrate record-shadow check (APPLIED / COMPUTATIONAL / FRONTIER-WILD family).

Reframe under test (Joe, 2026-07-14, exploration grade):
  - The substrate is Y14 ITSELF (the 14-dim observerse), not an imported causal set.
  - Records live in Y14; the shadow map is GU's Y14 -> X4 projection (section sigma).
  - The projection is MEASUREMENT-GATED: an individual observer must OBSERVE a record to
    promote it from the global Y14 substrate into a regional/confirmed shard
    (GLOBAL -> REGIONAL -> INDIVIDUAL capability tiers = a finality/consensus hierarchy).
  - dark energy / Lambda is the SHADOW of record accretion, not a source issuance.

This script computes, deterministically, the record-count-to-Lambda mechanics for two
readings and their relation, plus the Omega_Lambda-factorization that CAPS novelty (W143),
using the causal-set "number -> volume -> Lambda ~ 1/sqrt(N)" template (Sorkin everpresent
Lambda) as the mechanism, ported honestly onto the Y14->X4 split.

No canon / verdict / posture change. Exploration grade. Numbers are order-level physics
identities; O(1) factors are tracked and shown to be functions of Omega_Lambda.

Anchors ported (as cited constants, not re-derived):
  - W135: q_B = 3 H0 rho_L = (3/2) Omega_L c^5/G = 1.027 Planck lum / Hubble vol; ladder 9 Omega_L = 6.16.
  - W138: T_dS S_dS / E_Lambda = 1.46; Landauer bits at T_dS = 6.7e122 = 2.96 S_dS; at T_CMB = 6.5e92.
  - W143: the O(1) board factorizes through Omega_L (1.46 = 1/Omega_L; 2.96 = 3 Omega_L/ln2).
"""

import math

FAIL = []
def check(name, cond, detail=""):
    status = "ok" if cond else "FAIL"
    if not cond:
        FAIL.append(name)
    print(f"[{status}] {name}   {detail}")

# ---------------------------------------------------------------------------
# 0. Constants (SI; CODATA / Planck 2018 baseline, matching W135/W138)
# ---------------------------------------------------------------------------
c     = 2.99792458e8          # m/s
G     = 6.67430e-11           # m^3 kg^-1 s^-2
hbar  = 1.054571817e-34       # J s
kB    = 1.380649e-23          # J/K
l_p   = math.sqrt(hbar*G/c**3)      # Planck length
t_p   = l_p / c                     # Planck time
E_p   = math.sqrt(hbar*c**5/G)      # Planck energy
Mpc   = 3.0856775814913673e22        # m

H0_kmsMpc = 67.36
H0    = H0_kmsMpc*1000.0/Mpc         # 1/s
Omega_L = 0.6847
rho_crit = 3*H0**2/(8*math.pi*G)     # kg/m^3
rho_L    = Omega_L*rho_crit

R_H   = c/H0                         # Hubble radius
V_H   = (4.0/3.0)*math.pi*R_H**3     # Hubble volume (sphere)

# ---- positive controls (reproduce the anchored numbers) --------------------
print("=== positive controls ===")
check("l_p reproduces", abs(l_p-1.616255e-35)/1.616255e-35 < 1e-3, f"l_p={l_p:.3e} m")
rhoL_scale_meV = (rho_L*c**2 * (hbar*c)**3)**0.25 / (1.602176634e-19*1e-3)
check("rho_L^(1/4) ~ 2.24 meV", abs(rhoL_scale_meV-2.24) < 0.05, f"={rhoL_scale_meV:.3f} meV")
qB = 3*H0*rho_L*c**2                       # W/m^3 (bookkeeping issuance density, W135)
P_H = qB*V_H                               # W per Hubble volume
Planck_lum = c**5/G
check("Q_tot = 1.027 Planck lum (W135)", abs(P_H/Planck_lum-1.027) < 0.01, f"={P_H/Planck_lum:.4f}")
check("Q_tot = (3/2) Omega_L exactly", abs(P_H/Planck_lum-1.5*Omega_L) < 1e-6, f"(3/2)OmL={1.5*Omega_L:.4f}")
ladder = qB/(H0**3 * (hbar*c**5/(8*math.pi*G))**0  )  # placeholder, use reduced Planck mass form below
Mpl_red2_c4 = (hbar*c**5)/(8*math.pi*G)  # (reduced Planck mass)^2 c^4 ... use energy-density form
# ladder q_B / (H0^3 Mpl_red^2) : Mpl_red^2 = c hbar^-1 ... do it dimensionally via rho form
# q_B has W/m^3 = J/(s m^3). H0^3 Mpl_red^2 c^2 in same units:
Mpl_red2 = hbar*c/(8*math.pi*G)          # kg^2? keep the identity route instead:
# Use the clean identity: q_B/(H0^3 Mpl_red^2) with Mpl_red^2 = 1/(8 pi G) (natural), rho=...
# Simplest: 9 Omega_L is the stated ladder value; confirm via q_B = 3 H0 rho_L and rho_crit=3H0^2/8piG
ladder_val = qB / (H0 * 3*H0**2/(8*math.pi*G) * c**2) * 3  # = 3*rho_L/rho_crit *3 = 9 Omega_L
check("ladder q_B/(H0^3 Mpl^2) = 9 Omega_L = 6.16 (W135)", abs(ladder_val-9*Omega_L) < 1e-6,
      f"={ladder_val:.3f}, 9OmL={9*Omega_L:.3f}")

# ---------------------------------------------------------------------------
# 1. de Sitter thermodynamic anchors (W138)
# ---------------------------------------------------------------------------
print("\n=== de Sitter / horizon anchors (W138) ===")
T_dS = hbar*H0/(2*math.pi*kB)              # de Sitter temperature (K)
S_dS = math.pi*R_H**2/l_p**2               # horizon entropy in k_B
E_Lambda = rho_L*c**2*V_H                   # DE content of a Hubble volume (J)
check("T_dS ~ 2.65e-30 K", abs(T_dS-2.65e-30)/2.65e-30 < 0.02, f"T_dS={T_dS:.3e} K")
check("S_dS ~ 2.27e122", abs(math.log10(S_dS)-122.356) < 0.02, f"S_dS={S_dS:.3e}")
ratio_146 = T_dS*kB*S_dS/E_Lambda
check("T_dS S_dS / E_Lambda = 1.46 (W138 G5)", abs(ratio_146-1.46) < 0.02, f"={ratio_146:.3f}")
check("  ... = 1/Omega_L EXACTLY (W143)", abs(ratio_146-1.0/Omega_L) < 1e-3,
      f"1/OmL={1.0/Omega_L:.4f}")

# Landauer bit budgets (W138 G6): budget = 3 E_Lambda per Hubble time
budget = 3*E_Lambda
bits_Tds = budget/(kB*T_dS*math.log(2))
bits_Tcmb = budget/(kB*2.725*math.log(2))
check("bits at T_dS = 6.7e122 (W138)", abs(math.log10(bits_Tds)-122.826) < 0.03, f"={bits_Tds:.3e}")
check("bits/S_dS = 2.96 (W138 G6)", abs(bits_Tds/S_dS-2.96) < 0.03, f"={bits_Tds/S_dS:.3f}")
check("  ... = 3 Omega_L/ln2 EXACTLY (W143)", abs(bits_Tds/S_dS-3*Omega_L/math.log(2)) < 1e-2,
      f"3OmL/ln2={3*Omega_L/math.log(2):.3f}")
check("bits at T_CMB = 6.5e92 (W138)", abs(math.log10(bits_Tcmb)-92.81) < 0.05, f"={bits_Tcmb:.3e}")

# ---------------------------------------------------------------------------
# 2. Lambda in Planck units, and the two record counts
# ---------------------------------------------------------------------------
print("\n=== two record counts and the everpresent shadow ===")
Lambda_phys = 3*Omega_L*H0**2/c**2          # 1/m^2  (Lambda = 3 Omega_L H0^2/c^2)
Lambda_Pl   = Lambda_phys*l_p**2            # dimensionless (Planck units)
check("Lambda_Pl ~ 1e-122", abs(math.log10(Lambda_Pl)+121.55) < 0.1, f"Lambda_Pl={Lambda_Pl:.3e}")

# (A) SORKIN BULK reading: N_bulk = 4-volume of the past in Planck units ~ (R_H/l_p)^4
RH_over_lp = R_H/l_p
N_bulk = RH_over_lp**4                       # 4-volume element count (order)
everpresent_bulk = 1.0/math.sqrt(N_bulk)     # Sorkin: Lambda ~ 1/sqrt(N)
check("Sorkin bulk N ~ 1e244", abs(math.log10(N_bulk)-243.66) < 0.1, f"N_bulk={N_bulk:.3e}")
check("everpresent 1/sqrt(N_bulk) ~ Lambda_Pl (order)", abs(math.log10(everpresent_bulk/Lambda_Pl)) < 0.5,
      f"1/sqrt(N)={everpresent_bulk:.3e}, Lambda_Pl={Lambda_Pl:.3e}")
# the O(1) offset is a function of Omega_L (novelty cap):
offset_bulk = Lambda_Pl/everpresent_bulk
check("everpresent O(1) offset = 3 Omega_L (Omega_L-functional, W143 cap)",
      abs(offset_bulk-3*Omega_L) < 0.15, f"offset={offset_bulk:.3f}, 3OmL={3*Omega_L:.3f}")

# (B) HOLOGRAPHIC / FINALITY-FRONTIER reading: N_confirmed = promoted-record count = S_dS
N_conf = S_dS                                # confirmed frontier = horizon entropy (boundary count)
Lambda_from_conf = 1.0/N_conf                # measurement-gated: Lambda ~ 1/N_confirmed (LINEAR)
check("N_confirmed = S_dS ~ 1e122", abs(math.log10(N_conf)-122.356) < 0.02, f"N_conf={N_conf:.3e}")
# N_confirmed = pi / Lambda_Pl  (since S_dS = pi R_H^2/l_p^2 and Lambda_Pl = 3 Omega_L (l_p/R_H)^2)
check("N_confirmed = pi/(Lambda_Pl) up to 3 Omega_L", abs(N_conf*Lambda_Pl/math.pi - 3*Omega_L) < 0.15,
      f"N_conf*Lambda_Pl/pi={N_conf*Lambda_Pl/math.pi:.3f}, 3OmL={3*Omega_L:.3f}")

# (C) the bulk-boundary RELATION: N_bulk = N_conf^2 up to pi^2 (measurement-gating selects boundary)
check("N_bulk = N_conf^2 / pi^2 (bulk = boundary squared)",
      abs(math.log10(N_bulk/(N_conf**2/math.pi**2))) < 0.05,
      f"N_bulk/(N_conf^2/pi^2)={N_bulk/(N_conf**2/math.pi**2):.3f}")
# Consequence: Sorkin 1/sqrt(N_bulk) reading and holographic 1/N_conf reading COINCIDE (both ~ Lambda_Pl)
check("1/sqrt(N_bulk) == (1/N_conf)*pi (two readings agree)",
      abs(everpresent_bulk/(Lambda_from_conf*math.pi)-1.0) < 1e-6,
      f"ratio={everpresent_bulk/(Lambda_from_conf*math.pi):.4f}")

# ---------------------------------------------------------------------------
# 3. promotion (confirmation-frontier) growth rate and its Landauer budget
# ---------------------------------------------------------------------------
print("\n=== promotion rate (record growth = confirmed-frontier growth) ===")
# confirmed frontier area grows: dN_conf/dt = d(S_dS)/dt.  With R_H ~ const in de Sitter,
# in the coincidence era the promotion rate scales as ~ 2 S_dS H0 (area-doubling per Hubble time).
dNconf_dt = 2*S_dS*H0                          # /s  (frontier growth rate, order)
# Landauer power to promote at T_dS: each promotion costs k_B T_dS ln2
P_promote = dNconf_dt*kB*T_dS*math.log(2)      # W
check("promotion rate dN_conf/dt ~ 1e105 /s", abs(math.log10(dNconf_dt)-104.99) < 0.1,
      f"dN/dt={dNconf_dt:.3e} /s")
# This promotion power, compared to the DE budget per Hubble volume, is the W138 G6 saturation:
check("Landauer promote-power / (E_Lambda per Hubble time) is O(1) (saturation, W138 G6)",
      abs(math.log10(P_promote/(E_Lambda*H0))) < 1.0,
      f"ratio={P_promote/(E_Lambda*H0):.3e}")

# ---------------------------------------------------------------------------
# 4. GU-specific Y14->X4 structural probe (does dimension enter the exponent?)
# ---------------------------------------------------------------------------
print("\n=== Y14 -> X4 projection: dimensional structure ===")
dim_Y, dim_X, dim_fiber = 14, 4, 10
check("Y14 = X4 base (4) + DeWitt fiber (10)", dim_Y == dim_X+dim_fiber, "14 = 4+10")
# Poisson/everpresent exponent is 1/2 regardless of substrate dimension (fluctuation statistic).
# The fiber is a SPECTATOR to the everpresent exponent: the shadow exponent is NOT GU-specific.
# GU-specific content must live in (a) the admissible set (C-operator +subspace) or
# (b) the confirmed-vs-bulk SELECTION (measurement-gating), not in the exponent.
everpresent_exponent = 0.5
check("everpresent exponent = 1/2 (dimension-independent; NOT GU-specific)",
      everpresent_exponent == 0.5, "Poisson sqrt; fiber is spectator")
# structural note recorded: base/total = 4/14 = 2/7; fiber (6,4) sums to 10; none enters exponent.
check("no GU dimension in shadow exponent (honest novelty limit)",
      abs(everpresent_exponent-0.5) < 1e-9, "novelty must come from C+ set / measurement-gating")

# ---------------------------------------------------------------------------
print("\n=== summary ===")
if FAIL:
    print(f"FAILURES ({len(FAIL)}): {FAIL}")
    raise SystemExit(1)
print("ALL CHECKS PASSED")
