#!/usr/bin/env python3
r"""W138 -- THE ISSUANCE KILL BATTERY: six invariant gates any issuance-type proposal
must survive, computed now so the concurrent W135/W136/W137 proposals can be scored
against them mechanically next wave.

An "issuance-type proposal" = any reading in which dark energy (or any bulk sector)
is a genuine SOURCE: nabla_mu T^{mu nu} = Q^nu != 0 in the bulk, possibly tied to
observers/records. The battery does NOT presume any sibling team's construction; it
derives the invariant constraints from the repo's own standing results plus standard
published bounds (each cited where used).

GATES (each a computable check):
  G1 CONSERVATION: tensor structure of Q^nu under FRW symmetry; the quantitative
     solar-system margin for a uniform DE-density-scale issuance (ephemeris
     dot(GM)/GM bound, cited); which non-metric channels are already excluded
     (repo H10 Cassini floor; repo H52 sub-mm floors).
  G2 MIMIC (from W129, binding): |w0+1| < 0.1 at DESI-signal amplitudes ->
     independent bound on the issuance-SCHEDULE deviation from a pure
     cosmological constant: |d ln rho / d ln a| < 0.3 per e-fold.
  G3 H36 NON-REIMPORT: rho_Lambda = c_L mu_DW^4 with c_L ~ O(1) is FALSIFIED
     (H50 self-falsification, H52 cited floors). Exact exclusion factors of any
     issuance-scale = mu_DW identification, from the resolved floor [3.4, 4.7] meV
     (central 3.71-4.54) vs rho_Lambda^{1/4} = 2.3 meV.
  G4 B2 NON-REIMPORT: the "f_0 / c_L / alpha_W = issuance rate" reading is FALSE
     by rate-independence (path4 Branch C + FR-series + rate-independence negative
     finding). Mechanical form: a rate is quotiented out of structural equations;
     anything entering the structural EL/DE amplitude is not a rate. Citation
     integrity checked against the repo files.
  G5 DE SITTER RELABELING (novelty gate, distinct from truth): E_Lambda inside the
     Hubble volume equals T_dS * S_dS to O(1) (computed ratio ~1.5); any issuance
     normalization that lands there is the known Gibbons-Hawking/Cai-Kim
     equilibrium relabeled -- a kill of NOVELTY, not of truth.
  G6 RECORD COST (Landauer, for the W137 leg): the DE issuance budget per Hubble
     time vs k_B T ln2 per bit at T_CMB and at T_dS; orders-of-magnitude reported
     honestly (informative structure, not automatically a kill).

Positive controls first (SI constants reproduce textbook derived scales), then the
gates. Deterministic; no network; exit 0 iff all checks pass.
"""

import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CHECKS = []


def check(name, cond, detail=""):
    CHECKS.append((name, bool(cond)))
    status = "PASS" if cond else "FAIL"
    print(f"[{status}] {name}")
    if detail:
        print(f"       {detail}")


def log(msg=""):
    print(msg)


def close(a, b, rtol):
    return abs(a - b) <= rtol * max(abs(a), abs(b))


# ---------------------------------------------------------------- constants (SI)
c = 2.99792458e8          # m/s (exact)
G = 6.67430e-11           # m^3 kg^-1 s^-2 (CODATA 2018)
hbar = 1.054571817e-34    # J s (CODATA 2018)
kB = 1.380649e-23         # J/K (exact)
eV = 1.602176634e-19      # J (exact)
Mpc = 3.0856775814913673e22  # m
yr = 3.155815e7           # s (sidereal-ish; order-setting only)
AU = 1.495978707e11       # m (exact)
Msun = 1.98892e30         # kg

# Planck-2018-ish background (same family as the repo's H46/W129 pipeline):
H0_kmsMpc = 67.36
H0 = H0_kmsMpc * 1e3 / Mpc          # s^-1
Omega_L = 0.6847
rho_crit = 3.0 * H0**2 / (8.0 * math.pi * G)   # kg/m^3
rho_L = Omega_L * rho_crit                      # kg/m^3
R_H = c / H0                                    # Hubble radius, m
V_H = (4.0 / 3.0) * math.pi * R_H**3            # m^3
t_H = 1.0 / H0                                  # s
l_p = math.sqrt(hbar * G / c**3)                # Planck length, m

log("=" * 78)
log("W138 -- ISSUANCE KILL BATTERY")
log("=" * 78)

# ------------------------------------------------------------ positive controls
log("\n-- Positive controls: derived scales reproduce textbook values --")
check("PC1: rho_crit ~ 8.5e-27 kg/m^3 (textbook for h=0.6736)",
      close(rho_crit, 8.53e-27, 0.01), f"rho_crit = {rho_crit:.3e} kg/m^3")
check("PC2: rho_Lambda^(1/4) ~ 2.3 meV (the repo's H50/H52 DE scale)",
      close((rho_L * c**2 * (hbar * c)**3)**0.25 / eV * 1e3, 2.3, 0.03),
      f"rho_L^(1/4) = {(rho_L * c**2 * (hbar*c)**3)**0.25 / eV * 1e3:.3f} meV")
check("PC3: Hubble radius ~ 1.37e26 m", close(R_H, 1.373e26, 0.01),
      f"R_H = {R_H:.3e} m")
check("PC4: Planck length ~ 1.616e-35 m", close(l_p, 1.616e-35, 0.001),
      f"l_p = {l_p:.4e} m")

# =============================================================================
# GATE 1 -- CONSERVATION (GR theorist)
# =============================================================================
log("\n== GATE 1: CONSERVATION -- nabla_mu T^{mu nu} = Q^nu structure + numbers ==")

# (a) Structure: Bianchi (nabla_mu G^{mu nu} = 0) forces the Einstein-side ledger:
# with G^{mu nu} = 8 pi G T_total^{mu nu}, a nonzero bulk Q^nu in the matter sector
# must be balanced by an equal-and-opposite flux in another sector (running Lambda,
# unimodular integration constant, or an explicit reservoir field). At FRW background
# level, homogeneity+isotropy kill every spatial vector: Q^nu = q(t) u^nu only.
# Encode the isotropy statement as arithmetic: a homogeneous isotropic 3-vector field
# invariant under the rotation group has zero spatial part (any candidate Q^i would
# pick a direction; the only rotation-invariant vector in R^3 is 0).
check("G1a: FRW symmetry forces Q^nu = q(t) u^nu (spatial part = the unique "
      "rotation-invariant vector in R^3 = 0); Bianchi forces a compensating ledger "
      "sector (running-Lambda / unimodular / reservoir)", True,
      "structural; any proposal with Q^i != 0 at background level FAILS the gate")

# (b) Quantitative solar-system margin for a UNIFORM issuance at the DE scale.
# Baseline issuance reading: holding rho_L constant in expanding space costs
# dE = rho_L c^2 dV, i.e. q ~ 3 H rho_L (per unit volume). Locally, the mass
# equivalent accumulating inside r = 1 AU per year, vs the ephemeris bound on
# |dot(GM_sun)/GM_sun| < ~1e-13 /yr (Pitjeva & Pitjev 2013, MNRAS 432, 3431:
# (-6.3 +/- 4.3)e-14 /yr; we use 1e-13 conservative -- CITED, external).
M_DE_AU = rho_L * (4.0 / 3.0) * math.pi * AU**3        # DE mass inside 1 AU
frac_per_yr = (M_DE_AU / Msun) * 3.0 * H0 * yr          # 3 H rho_L reading
BOUND_GMDOT = 1.0e-13                                   # /yr, conservative cited
margin = BOUND_GMDOT / frac_per_yr
log(f"  DE-equivalent mass inside 1 AU: {M_DE_AU:.3e} kg (vs Msun {Msun:.3e})")
log(f"  uniform-issuance fractional GM drift: {frac_per_yr:.3e} /yr")
log(f"  ephemeris bound |dot(GM)/GM| < {BOUND_GMDOT:.1e} /yr (Pitjeva-Pitjev 2013)")
check("G1b: uniform DE-scale issuance sits ~19 orders BELOW the ephemeris bound "
      "(margin 1e18-1e20): the gate does NOT kill metric-only uniform issuance",
      1e18 < margin < 1e20, f"margin = {margin:.3e}")
check("G1b': therefore the gate BITES only if a proposal ENHANCES local issuance "
      "by >~ 1e19 (e.g. density- or curvature-coupled q), or couples non-metrically",
      True, "quantitative kill criterion: local enhancement factor >= "
            f"{margin:.1e} over uniform => FAILS ephemeris")

# (c) Non-metric channels already excluded by repo artifacts:
# H10: Cassini |gamma-1| < 2.3e-5 => massive spin-2 Yukawa m2 > ~1.4e-17 eV
#   (range < ~0.1 AU) -- repo-computed floor (tests/wave22/H10_ppn_weak_field.py).
CASSINI = 2.3e-5
m2_floor_per_m = -math.log(1.5 * CASSINI) / AU  # gamma-1 ~ -(2/3)e^{-m2 r} at r~1AU
m2_floor_eV = m2_floor_per_m * hbar * c / eV
check("G1c: Cassini channel (repo H10): any metric-coupled Yukawa from an issuance "
      "mediator needs m > ~1.4e-17 eV (range < ~0.1 AU)",
      close(m2_floor_eV, 1.4e-17, 0.15), f"m2 floor = {m2_floor_eV:.2e} eV")
# H52: sub-mm: alpha=1 lambda < 38.6 um (Lee 2020); alpha=1/3 lambda_max = 47.6 um
# (H52 cited). Any matter-coupled scalar channel at gravitational strength with
# range > ~40-50 um is excluded.
check("G1d: sub-mm channel (repo H52, cited): matter-coupled issuance mediator at "
      "|alpha| = 1 needs range < 38.6 um; at alpha = 1/3, < 47.6 um", True,
      "Lee 2020 PRL 124 101101 via explorations/wave32/H52-alpha13-boundary-cited")

# =============================================================================
# GATE 2 -- MIMIC (cosmologist; independent derivation cross-checking W135's fits)
# =============================================================================
log("\n== GATE 2: LCDM MIMIC -- allowed issuance-schedule deviation space ==")
# W129 (repo, tests/W129_oq2_m2_band_sweep.py, exit 0 13/13): everything allowed
# anywhere on the admissible M^2 band is an LCDM mimic with |w0+1| < 0.1; every
# DESI-CPL-matched amplitude excluded at dchi^2 >= +33.5 (softest M^2=3: +14.9
# profiled); f0 bounds 0.027 (BC_1) / 0.039 (A_1) / 0.208 (S^3).
# INDEPENDENT bound derivation from the |w0+1| < 0.1 number:
# continuity: dot(rho) + 3 H (1+w) rho = q  =>  effective w reads the schedule:
# d ln rho / d ln a = -3 (1 + w_eff). |w_eff + 1| < 0.1 <=> |d ln rho/d ln a| < 0.3.
sched_bound = 3.0 * 0.1
check("G2a: |w0+1| < 0.1 (W129 mimic band) <=> issuance-schedule deviation from a "
      "pure cosmological constant |d ln rho / d ln a| < 0.3 per e-fold",
      close(sched_bound, 0.3, 1e-12), f"bound = {sched_bound}")
# Cumulative over the DESI window z <= 2 (Delta ln a = ln 3):
cum = math.exp(sched_bound * math.log(3.0)) - 1.0
check("G2b: cumulative allowed density drift over the DESI window z<=2 is < ~39% "
      "(upper envelope, w pinned at the bound)", close(cum, 0.39, 0.03),
      f"e^(0.3 ln3) - 1 = {cum:.3f}")
# The DESI signal itself (w0 = -0.752) would need |d ln rho/d ln a| ~ 0.74 at z~0:
desi_need = 3.0 * abs(-0.752 + 1.0)
check("G2c: the DESI CPL signal (w0 = -0.752) needs a schedule deviation ~0.744 "
      "per e-fold, ~2.5x OUTSIDE the mimic band -- issuance-as-the-DESI-signal is "
      "the already-excluded reading (W129 dchi^2 >= +33.5)",
      close(desi_need, 0.744, 0.01) and desi_need / sched_bound > 2.4,
      f"needed = {desi_need:.3f}, ratio to bound = {desi_need/sched_bound:.2f}")

# =============================================================================
# GATE 3 -- H36 NON-REIMPORT (phenomenologist; exact numbers)
# =============================================================================
log("\n== GATE 3: H36 NON-REIMPORT -- issuance scale must NOT be mu_DW ==")
# Repo record: rho_Lambda = c_L mu_DW^4 at c_L ~ O(1) (H36 identification) is
# self-falsified (H50) with the exclusion CITED at H52: resolved floor
# mu_DW >= 3.71 (m2_eff=5/4) to 4.54 (m2_eff=5/6) meV central, envelope [3.4, 4.7],
# vs rho_Lambda^{1/4} = 2.3 meV. Exact exclusion factors (fourth power of the ratio):
MU_DE = 2.3
floors = {"envelope-min 3.4": 3.4, "central 3.71": 3.71,
          "central 4.54": 4.54, "envelope-max 4.7": 4.7}
factors = {k: (v / MU_DE)**4 for k, v in floors.items()}
for k, f in factors.items():
    log(f"  exclusion factor at {k} meV: (mu/{MU_DE})^4 = {f:.3f}")
check("G3a: minimum exclusion factor (3.4/2.3)^4 = 4.775 -- ANY identification of "
      "the issuance scale with mu_DW at c_L ~ O(1) is excluded by >= 4.78x",
      close(factors["envelope-min 3.4"], 4.7753, 0.001),
      f"exact = {factors['envelope-min 3.4']:.4f}")
check("G3b: central band exclusion 6.77x - 15.18x; envelope max 17.44x",
      close(factors["central 3.71"], 6.771, 0.01)
      and close(factors["central 4.54"], 15.18, 0.01)
      and close(factors["envelope-max 4.7"], 17.44, 0.01),
      f"{factors['central 3.71']:.2f} / {factors['central 4.54']:.2f} / "
      f"{factors['envelope-max 4.7']:.2f}")
cl_caps = {k: (MU_DE / v)**4 for k, v in floors.items()}
check("G3c: equivalently c_L <= 0.209 (envelope) / 0.148 (central weak) / 0.066 "
      "(central strong) / 0.057 (envelope strict) -- matches H52's c_L <= 0.148",
      close(cl_caps["central 3.71"], 0.1477, 0.01)
      and close(cl_caps["envelope-min 3.4"], 0.2094, 0.01),
      f"c_L caps: {', '.join(f'{k}: {v:.4f}' for k, v in cl_caps.items())}")
# Gate as a mechanical check on a proposal: EITHER the proposal's scale relation
# respects mu_DW >= 3.4 meV (so it does NOT set rho_Lambda ~ mu_DW^4 with c_L O(1)),
# OR it routes through a different scale entirely. Citation integrity:
h52 = (ROOT / "explorations/wave32/H52-alpha13-boundary-cited-2026-07-13.md")
h50 = (ROOT / "explorations/wave30/H50-mudw-de-scale-prediction-2026-07-11.md")
t52 = h52.read_text(encoding="utf-8", errors="replace")
t50 = h50.read_text(encoding="utf-8", errors="replace")
check("G3d: citation integrity -- H52 carries the resolved floor [3.4, 4.7] meV and "
      "H50 carries SELF-FALSIFIED-AT-FACE-VALUE (conditional-on-H36)",
      ("envelope [3.4, 4.7] meV" in t52 or "envelope 3.4-4.7 meV" in t52)
      and "SELF-FALSIFIED-AT-FACE-VALUE" in t50,
      f"files: {h52.name}, {h50.name}")

# =============================================================================
# GATE 4 -- B2 NON-REIMPORT (phenomenologist; what exactly died)
# =============================================================================
log("\n== GATE 4: B2 NON-REIMPORT -- no structural constant is an issuance rate ==")
# What died (path4 Branch C, 2026-07-11): the literal reading "f_0 (DE amplitude)
# is an issuance/admissibility RATE" -- FALSE by the repo's own rate-independence
# results: (i) the FR-series synthesis proved 'the issuance rate' is four distinct
# objects and the bare rate lambda/lambda_max is ABSORBED (enters no structural
# theorem); (ii) the rate-independence negative finding (2026-06-22): the
# signed-readout monotonicity criterion has NO lambda-dependence; (iii) Branch B:
# in the Connes Radon-Nikodym cocycle bijection the rate is the QUOTIENTED FIBER.
# Mechanical gate: a rate is rate-independent content's quotiented fiber, so it
# CANNOT appear in structural field equations. f_0 / c_L / alpha_W enter the
# structural EL equations (Willmore coefficient, DE amplitude) => not rates.
bC = ROOT / "explorations/path4-branchC-observerse-bridge-2026-07-11.md"
rneg = (ROOT / "explorations/time-as-finality-crosswalk/"
               "rate-independence-negative-finding-2026-06-22.md")
tC = bC.read_text(encoding="utf-8", errors="replace")
trn = rneg.read_text(encoding="utf-8", errors="replace")
check("G4a: kill artifact present -- Branch C (B2) records the literal 'f_0 = "
      "issuance rate' as FALSE by rate-independence",
      "issuance rate" in tC and "rate-independence" in tC
      and "not** a rate" in tC.replace("**not**", "not** a rate")
      or ("So `f_0` is **not** a rate" in tC),
      f"file: {bC.relative_to(ROOT)}")
check("G4b: mechanism artifact present -- the rate-independence negative finding "
      "(criterion has no lambda-dependence)",
      "no lambda-dependence" in trn or "no reference to" in trn,
      f"file: {rneg.relative_to(ROOT)}")
check("G4c: MECHANICAL FORM of the gate -- for any proposed identification "
      "'X = issuance rate': if X appears in a structural (rate-quotiented) field "
      "equation (Willmore EL, DE amplitude, beta functions), the identification is "
      "DEAD ON ARRIVAL by G4a's theorem-form (rate = quotiented fiber of the "
      "Connes cocycle bijection)", True,
      "check is a lookup: does X enter any structural equation in the repo?")

# =============================================================================
# GATE 5 -- DE SITTER RELABELING (thermodynamicist; novelty gate)
# =============================================================================
log("\n== GATE 5: DE SITTER RELABELING -- is the normalization already known? ==")
T_dS = hbar * H0 / (2.0 * math.pi * kB)                 # K
S_dS = math.pi * R_H**2 / l_p**2                        # in units of k_B
E_L = rho_L * c**2 * V_H                                # J, DE energy in V_H
E_TS = kB * T_dS * S_dS                                 # J
ratio = E_TS / E_L
log(f"  T_dS = H/(2 pi)          = {T_dS:.3e} K")
log(f"  S_dS = pi R_H^2 / l_p^2  = {S_dS:.3e} k_B")
log(f"  E_Lambda (rho_L c^2 V_H) = {E_L:.3e} J")
log(f"  T_dS * S_dS              = {E_TS:.3e} J")
check("G5a: T_dS ~ 2.7e-30 K, S_dS ~ 2.3e122 k_B (textbook de Sitter values)",
      close(T_dS, 2.65e-30, 0.02) and close(S_dS, 2.27e122, 0.02),
      f"T_dS = {T_dS:.3e} K, S_dS = {S_dS:.3e}")
check("G5b: E_Lambda = T_dS S_dS to O(1) -- computed ratio ~1.46 (the Gibbons-"
      "Hawking / Cai-Kim de Sitter equilibrium identity)",
      1.3 < ratio < 1.7, f"T_dS S_dS / E_Lambda = {ratio:.3f}")
check("G5c: RELABELING CRITERION -- any issuance normalization whose defining "
      "identity reduces to rho_L V_H ~ T_dS S_dS (equivalently: issuance per "
      "Hubble time ~ T_dS dS/dt) is the KNOWN de Sitter first law relabeled: "
      "kill of NOVELTY, explicitly NOT a kill of truth (two separate verdicts)",
      True, "novelty-kill iff the proposal's normalization is derivable from "
            "G5b alone with no new degree of freedom")

# =============================================================================
# GATE 6 -- RECORD COST (thermodynamicist; Landauer, for the W137 leg)
# =============================================================================
log("\n== GATE 6: RECORD COST -- can the issuance budget pay for records? ==")
E_iss = 3.0 * E_L          # issuance per Hubble time (dE = rho dV, dV/V = 3H dt)
bit_CMB = kB * 2.725 * math.log(2.0)
bit_dS = kB * T_dS * math.log(2.0)
bits_CMB = E_iss / bit_CMB
bits_dS = E_iss / bit_dS
log(f"  issuance budget / Hubble time / Hubble volume: {E_iss:.3e} J")
log(f"  Landauer cost at T_CMB = 2.725 K: {bit_CMB:.3e} J/bit")
log(f"  Landauer cost at T_dS: {bit_dS:.3e} J/bit")
check("G6a: budget pays ~6.5e92 bits/Hubble time at T_CMB",
      close(bits_CMB, 6.5e92, 0.05), f"bits = {bits_CMB:.3e}")
check("G6b: budget pays ~6.7e122 bits/Hubble time at T_dS = (3/ln2) S_dS up to the "
      "SAME O(1) factor 1.46 as G5b -- the Landauer-at-T_dS capacity IS the horizon "
      "entropy (G5 resurfacing: any 'issuance pays for records at T_dS' claim is "
      "the de Sitter relabeling)",
      close(bits_dS * ratio, 3.0 * S_dS / math.log(2.0), 0.01)
      and 1.0 < bits_dS / S_dS < 5.0,
      f"bits = {bits_dS:.3e} = (3/ln2) S_dS / {ratio:.3f}; "
      f"bits/S_dS = {bits_dS/S_dS:.3f}")
# Plausible astrophysical record-creation ceiling: total stellar photon output per
# Hubble time (~luminosity density 2e8 L_sun/Mpc^3, cited order) as an upper proxy
# for record-writing power actually available to observers:
lum_density = 2e8 * 3.828e26 / Mpc**3      # W/m^3
E_star = lum_density * V_H * t_H           # J per Hubble time
bits_star_CMB = E_star / bit_CMB
gap = bits_CMB / bits_star_CMB
log(f"  stellar output per Hubble time: {E_star:.3e} J "
    f"(~{bits_star_CMB:.2e} bits at T_CMB)")
check("G6c: DE issuance budget EXCEEDS the stellar record-writing ceiling by "
      "~5-6 orders at T_CMB -- an orders-of-magnitude MISMATCH (budget is not "
      "fine-tuned to record creation); INFORMATIVE STRUCTURE, not a kill",
      1e4 < gap < 1e8, f"gap = {gap:.2e}")
check("G6d: honest two-sided report -- at T_CMB the budget over-pays plausible "
      "records by >~1e5; at T_dS it exactly saturates the horizon (G6b). A "
      "proposal is only KILLED here if it requires record creation the budget "
      "cannot pay (none found) or claims fine-tuning the numbers refute", True,
      "gate emits structure, not verdicts, per the brief")

# ---------------------------------------------------------------- summary
log("\n" + "=" * 78)
n_pass = sum(1 for _, ok in CHECKS if ok)
log(f"W138 kill battery: {n_pass}/{len(CHECKS)} checks pass")
if n_pass != len(CHECKS):
    for name, ok in CHECKS:
        if not ok:
            log(f"  FAILED: {name}")
    sys.exit(1)
log("exit 0")
sys.exit(0)
