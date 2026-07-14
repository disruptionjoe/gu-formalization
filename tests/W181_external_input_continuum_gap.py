#!/usr/bin/env python3
r"""
W181 / TEAM EXT-GAP -- does the INPUT TO THE SOURCE ACTION FROM OUTSIDE THE GEOMETRY change the build
sprint's NOT-OPERATIVE lean, via a CONTINUUM-GAP / THRESHOLD-SHIFT mechanism?

THE QUESTION
------------
The build sprint (W175-W180) computed the ghost pole sheet for the CLOSED/internal theory and leaned
NOT-OPERATIVE.  The mechanism (W179):

    the interacting C-operator EXISTS iff the ghost is BELOW the two-graviton DECAY threshold,
        on-shell zero of D(k1,k2) = om2(k1+k2) - om1(k1) - om1(k2)   <=>   m_ghost >= 2 m_phys,

and GU's MASSLESS-graviton Stelle spectrum (m_phys = 0, H51: the TT s^0 pole is EXACTLY massless) puts
the threshold at 2*0 = 0, so the massive ghost is ABOVE it for EVERY M > 0 -> ghost decays into two
gravitons -> anti-damping self-energy (W51) -> physical-sheet pole -> PT breaks -> no positive C-metric
-> NOT-OPERATIVE (W178/W179).

THE ANGLE TESTED HERE (the continuum-gap / threshold-shift)
-----------------------------------------------------------
The ghost decays ONLY because the graviton continuum starts at ZERO (massless graviton, threshold =
2*0 = 0).  GU is fundamentally an OPEN theory with an EXTERNAL SOURCE (W177 count needs an external
non-metric datum; W180 dark-energy current is sourced externally).  If that external issuance supplies
an IR SCALE that GAPS the effective graviton continuum, the effective two-graviton threshold rises to
2*(gap), and the ghost could drop BELOW it -> sub-threshold (W179's OPERATIVE regime) -> the C-operator
exists -> bar (b) could clear.

The decisive question is QUANTITATIVE: what IR scale does the external source honestly supply, and does
the meV-scale (to Planck-scale) ghost fall below 2*(that gap)?

THE SCALES (repo-sourced; H36 non-reimport honored)
---------------------------------------------------
  * Ghost mass (W25 / track2, "given S"):  m2 = sqrt(m2_eff) * mu_DW,  m2_eff in [5/6, 5/4] (~1),
    mu_DW free with a sub-mm floor mu_DW >= ~3.4 meV (H52-cited).  So the ghost lives at the FUNDAMENTAL
    DW scale: ~meV at the floor, up to Planckian at the natural mu_DW = M_Pl default.
  * The external IR scale, HONESTLY sourced (W135/W146/W180):  the everpresent-Lambda / de Sitter
    background sets a Hubble/de-Sitter IR scale  H0 = 1.44e-33 eV, with  Lambda ~ H0^2  and the exact
    relation  H0 = rho_L^{1/2} / (sqrt(3 Omega_L) M_Pl)  (rho_L^{1/4} = 2.24 meV).  The meV number
    rho_L^{1/4} is an ENERGY-DENSITY scale, NOT a graviton mass gap; the DYNAMICAL IR scale that
    modifies the graviton dispersion in a de Sitter background is H0 = (DE scale)^2 / M_Pl, i.e. the
    DE scale PLANCK-SUPPRESSED by one power of (DE scale / M_Pl) ~ 1e-30.
  * H36 NON-REIMPORT (binding):  identifying the graviton IR gap with mu_DW / the DE scale directly (a
    meV graviton gap) is the FALSIFIED H36 identification (track2 sec 3; sub-mm excluded) AND is
    excluded model-independently by the GW graviton-mass bound m_g < 1.27e-23 eV (LIGO GWTC-3).  The
    honest gap is H0, NOT mu_DW.

WHAT THIS FILE COMPUTES
-----------------------
POSITIVE CONTROLS (reproduce W179):
  (PC-A) the massless-graviton obstruction: m_phys = 0 gives an on-shell zero of D for every M > 0
         (the NOT-OPERATIVE mechanism this angle tries to escape);
  (PC-B) the threshold machinery is real: a GAPPED graviton (m_phys_eff > 0) with m_ghost < 2 m_phys_eff
         gives NO on-shell zero (D strictly one-signed) -> sub-threshold OPERATIVE regime.  So the
         MECHANISM works; the only question is the SIZE of the honest gap.
  (PC-C) the de Sitter consistency relation H0 = rho_L^{1/2}/(sqrt(3 Omega_L) M_Pl) to < 1%.
THE DECISIVE COMPUTATION:
  (D1) de Sitter gap g_dS = H0: m2 / (2 g_dS) >> 1 (ghost ABOVE the gapped threshold by ~30 orders);
  (D2) even at the model-independent GW ceiling m_g < 1.27e-23 eV: m2 / (2 m_g_max) >> 1 (~20 orders);
  (D3) the required gap g_needed = m2/2 across the whole mu_DW window (floor -> M_Pl): g_avail/g_needed
       is between ~1e-20 and ~1e-60, NEVER >= 1 -- GAP INSUFFICIENT everywhere;
  (D4) the parametric suppression: g_dS / g_needed ~ mu_DW / M_Pl ~ 1e-30 (one power of the hierarchy).
THE CONDITIONAL (adversary / H36 trap):
  (C1) the ONLY regime that clears is g_gap >= m2/2 = (sqrt(m2_eff)/2) mu_DW, i.e. a graviton gapped AT
       the mu_DW (meV) scale; then sub-threshold iff m2_eff < 4 (which holds, m2_eff in [5/6,5/4]).  But
       that gap is the H36-forbidden identification and is GW-excluded by ~20 orders -- it is exactly
       the re-import the brief forbids.  So the clearing regime is not honestly reachable.

VERDICT: GAP-INSUFFICIENT-NOT-OPERATIVE-STANDS.  The honestly-sourced external IR gap (de Sitter H0 ~
1e-33 eV, or the GW-allowed graviton mass <= 1.3e-23 eV) is 20-30 orders of magnitude too small to lift
the meV-scale (let alone Planck-scale) ghost below the gapped two-graviton threshold.  bar (b) does NOT
clear via this mechanism.  It would clear ONLY if the graviton were gapped at ~mu_DW/2 (meV scale),
which is the H36-forbidden re-import and is GW-excluded.

Deterministic; numpy + sympy only; no network.  exit 0 iff all checks pass.
No canon / RESEARCH-STATUS / claim-status / verdict / posture file is touched.  Exploration-grade.
"""
from __future__ import annotations

import math

import numpy as np
import sympy as sp

np.random.seed(0)

results: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    results.append((name, bool(passed), detail))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))


def log(msg: str = "") -> None:
    print(msg, flush=True)


def om(k: np.ndarray | float, m: float) -> np.ndarray | float:
    return np.sqrt(np.asarray(k, dtype=float) ** 2 + m * m)


# --- W179 threshold machinery, reproduced verbatim (the object we reuse) --------------------------
def D_grid(m1: float, m2: float, kmax: float = 60.0, npts: int = 481):
    """D(k1,k2) = om2(k1+k2) - om1(k1) - om1(k2) on a symmetric real-momentum grid."""
    k = np.linspace(-kmax, kmax, npts)
    K1, K2 = np.meshgrid(k, k)
    return om(K1 + K2, m2) - om(K1, m1) - om(K2, m1)


def has_real_zero(m1: float, m2: float, **kw) -> tuple[bool, float, float]:
    """(sign-change present, min D, max D) over the grid.  Sign change <=> on-shell decay zero."""
    Dg = D_grid(m1, m2, **kw)
    return (Dg.min() < 0.0 < Dg.max()), float(Dg.min()), float(Dg.max())


# --- repo-sourced constants (all in eV; comparison-only, labelled) --------------------------------
EV = 1.0
MEV = 1.0e-3 * EV
H0 = 1.44e-33 * EV            # Hubble rate today, hbar*H0 (67.4 km/s/Mpc)
M_PL = 2.435e27 * EV          # reduced Planck mass, 2.435e18 GeV
RHO_L_QUARTER = 2.24 * MEV    # observed dark-energy scale rho_L^{1/4} (W135/W146)
OMEGA_L = 0.685              # dark-energy fraction
MU_DW_FLOOR = 3.4 * MEV       # H52-cited sub-mm floor on mu_DW (track2 sec 3)
M2_EFF_LO, M2_EFF_HI = 5.0 / 6.0, 5.0 / 4.0   # W25/H25 ghost m2_eff band
M_G_MAX_GW = 1.27e-23 * EV    # model-independent graviton-mass ceiling, LIGO GWTC-3 (track2 row 7)


def ghost_mass(mu_dw: float, m2_eff: float) -> float:
    """m2 = sqrt(m2_eff) * mu_DW  (W25 / track2)."""
    return math.sqrt(m2_eff) * mu_dw


log("=" * 100)
log("W181 / TEAM EXT-GAP -- external-input continuum-gap / threshold-shift test of the NOT-OPERATIVE lean")
log("=" * 100)

# =====================================================================================================
# POSITIVE CONTROLS FIRST
# =====================================================================================================
log("\n[PC-A] positive control: reproduce W179's MASSLESS-graviton obstruction (the NOT-OPERATIVE mechanism)")
obstructs_massless = True
for M in [0.3, 1.0, 3.0, 10.0]:
    z, dmn, dmx = has_real_zero(0.0, M)
    obstructs_massless = obstructs_massless and z and (dmn < 0.0 < dmx)
check("PC-A  massless graviton (m_phys=0): the two-graviton continuum starts at 0, so a ghost of ANY "
      "M>0 has a real on-shell zero of D -> ghost decays -> NOT-OPERATIVE (W178/W179 reproduced)",
      obstructs_massless, "D changes sign for M in {0.3,1,3,10} at m_phys=0 => on-shell decay pole")

log("\n[PC-B] positive control: the threshold machinery -- a GAPPED graviton CAN move the ghost sub-threshold")
# a gapped graviton m_phys_eff=1 with a ghost m_ghost=1.5 < 2*1: NO on-shell zero (sub-threshold, OPERATIVE)
z_gapped_sub, dmn_gs, dmx_gs = has_real_zero(1.0, 1.5)
# the SAME ghost m_ghost=1.5 with a graviton gap of only 0.5 (< 1.5/2=0.75): STILL above -> on-shell zero
z_gapped_insuff, _, _ = has_real_zero(0.5, 1.5)
check("PC-B1  a SUFFICIENT graviton gap (m_phys_eff=1, m_ghost=1.5 < 2*1): D has NO real zero => "
      "sub-threshold => the C-operator EXISTS => the MECHANISM this angle proposes is real",
      (not z_gapped_sub) and dmx_gs < 0.0, f"max D={dmx_gs:.3f} < 0 (sub-threshold)")
check("PC-B2  an INSUFFICIENT graviton gap (m_phys_eff=0.5, m_ghost=1.5 > 2*0.5): D still changes sign "
      "=> still above threshold => a too-small gap does NOT rescue operativity (size is decisive)",
      z_gapped_insuff, "gap 0.5 < m_ghost/2 = 0.75 => ghost still above the gapped threshold")

log("\n[PC-C] positive control: the de Sitter consistency relation H0 = rho_L^{1/2}/(sqrt(3 Omega_L) M_Pl)")
rho_L = RHO_L_QUARTER ** 4
H0_from_rho = math.sqrt(rho_L) / (math.sqrt(3.0 * OMEGA_L) * M_PL)
rel = abs(H0_from_rho - H0) / H0
check("PC-C  H0 reconstructed from rho_L and M_Pl matches the input H0 to < 1% -- grounds 'the de Sitter "
      "IR scale is the DE scale PLANCK-SUPPRESSED': H0 = (DE scale)^2 / M_Pl (up to sqrt(3 Omega_L))",
      rel < 0.01, f"H0(from rho_L) = {H0_from_rho:.3e} eV vs H0 = {H0:.3e} eV, rel = {rel:.2e}")

# =====================================================================================================
# PART 1 -- THE DECISIVE COMPUTATION: ghost mass vs the GAPPED two-graviton threshold, real scales.
# =====================================================================================================
log("\n" + "-" * 100)
log("[PART 1] the decisive computation: is m2 BELOW 2*(honest IR gap)?  (sub-threshold <=> m2 < 2*gap)")
log("-" * 100)

# The lightest / most favourable ghost: mu_DW at the floor, m2_eff at the top (largest sqrt but still the
# meV scale).  Any heavier mu_DW only makes the ghost heavier and the verdict stronger.
m2_light = ghost_mass(MU_DW_FLOOR, M2_EFF_HI)   # ~ meV-scale ghost, the easiest case for OPERATIVE
log(f"      lightest GU ghost (mu_DW=floor {MU_DW_FLOOR/MEV:.1f} meV, m2_eff={M2_EFF_HI}):  "
    f"m2 = {m2_light/MEV:.3f} meV = {m2_light:.3e} eV")

# (D1) de Sitter gap = H0.
g_dS = H0
ratio_dS = m2_light / (2.0 * g_dS)
check("D1  DE SITTER GAP (g = H0 = 1.44e-33 eV): the ghost sits at m2/(2 H0) ~ 1e30 ABOVE the gapped "
      "two-graviton threshold -> STILL ABOVE -> NOT-OPERATIVE.  The de Sitter IR gap is ~30 orders too small",
      ratio_dS > 1e25, f"m2/(2 g_dS) = {ratio_dS:.3e}  (>> 1: ghost far above the de Sitter-gapped threshold)")

# (D2) model-independent observational ceiling on ANY graviton gap: the GW graviton-mass bound.
ratio_gw = m2_light / (2.0 * M_G_MAX_GW)
check("D2  GW CEILING (any graviton gap <= m_g < 1.27e-23 eV, LIGO GWTC-3): even SATURATING the largest "
      "observationally-allowed graviton mass, m2/(2 m_g_max) ~ 1e20 ABOVE threshold -> NOT-OPERATIVE.  "
      "This is the honest, mechanism-independent ceiling and it fails by ~20 orders",
      ratio_gw > 1e15, f"m2/(2 m_g_max) = {ratio_gw:.3e}  (>> 1)")

# (D3) the required gap vs the available gap across the WHOLE mu_DW window (floor meV -> M_Pl natural).
log("\n      required gap g_needed = m2/2 vs available honest gaps, across the mu_DW window:")
log("      %-22s %-14s %-14s %-14s %-14s" % ("mu_DW", "m2 (ghost)", "g_needed=m2/2", "H0/g_needed", "m_g_max/g_needed"))
window_all_insufficient = True
for mu_dw, tag in [(MU_DW_FLOOR, "floor 3.4 meV"), (1.0 * EV, "1 eV"), (1.0e9 * EV, "1 GeV"), (M_PL, "M_Pl (natural)")]:
    m2v = ghost_mass(mu_dw, M2_EFF_HI)
    g_needed = m2v / 2.0
    r_dS = H0 / g_needed
    r_gw = M_G_MAX_GW / g_needed
    window_all_insufficient = window_all_insufficient and (r_dS < 1.0) and (r_gw < 1.0)
    log("      %-22s %-14.3e %-14.3e %-14.3e %-14.3e" % (tag, m2v, g_needed, r_dS, r_gw))
check("D3  ACROSS THE WHOLE mu_DW WINDOW (meV floor -> Planck): g_available/g_needed is ALWAYS < 1 "
      "(between ~1e-20 and ~1e-60) -- the honest IR gap NEVER reaches the half-ghost-mass required to "
      "move the ghost sub-threshold.  GAP INSUFFICIENT everywhere on the window",
      window_all_insufficient, "H0/g_needed < 1 AND m_g_max/g_needed < 1 at every mu_DW sampled")

# (D4) the parametric suppression: g_dS/g_needed ~ mu_DW/M_Pl (one power of the hierarchy) at mu_DW ~ DE scale.
g_needed_floor = m2_light / 2.0
supp = g_dS / g_needed_floor
mu_over_Mpl = MU_DW_FLOOR / M_PL
check("D4  PARAMETRIC SUPPRESSION: at mu_DW ~ DE scale, g_dS/g_needed = 2 H0/(sqrt(m2_eff) mu_DW) ~ "
      "mu_DW/M_Pl ~ 1e-30 -- the de Sitter gap is the ghost scale suppressed by ONE power of the "
      "hierarchy mu_DW/M_Pl.  The ghost is at the un-suppressed scale; the gap is not",
      0.05 < supp / mu_over_Mpl < 20.0 and supp < 1e-25,
      f"g_dS/g_needed = {supp:.3e};  mu_DW/M_Pl = {mu_over_Mpl:.3e};  ratio = {supp/mu_over_Mpl:.2f} (O(1))")

# =====================================================================================================
# PART 2 -- THE CONDITIONAL (adversary / H36 trap): the only clearing regime is the forbidden one.
# =====================================================================================================
log("\n" + "-" * 100)
log("[PART 2] the conditional: the ONLY sub-threshold regime is a graviton gapped AT ~mu_DW (H36-forbidden)")
log("-" * 100)

# (C1) IF (illegally) the graviton were gapped at g_gap = mu_DW itself, sub-threshold iff m2 < 2 mu_DW iff
# sqrt(m2_eff) < 2 iff m2_eff < 4.  The band m2_eff in [5/6,5/4] is all < 4, so the ghost WOULD clear --
# but only under a meV graviton gap, which is the H36-forbidden identification and GW-excluded.
sub_thr_if_gapped_at_mu = (math.sqrt(M2_EFF_LO) < 2.0) and (math.sqrt(M2_EFF_HI) < 2.0)
check("C1a  IF the graviton were gapped AT mu_DW (g_gap = mu_DW): sub-threshold iff m2_eff < 4, and the "
      "band m2_eff in [5/6,5/4] satisfies this -> the ghost WOULD clear.  This is the ONLY clearing regime",
      sub_thr_if_gapped_at_mu, f"sqrt(m2_eff) in [{math.sqrt(M2_EFF_LO):.3f}, {math.sqrt(M2_EFF_HI):.3f}] < 2")

# but the required gap scale g_needed = (sqrt(m2_eff)/2) mu_DW is O(mu_DW) = meV, NOT O(H0):
g_needed_over_mu = math.sqrt(M2_EFF_HI) / 2.0
required_gap_meV = g_needed_over_mu * MU_DW_FLOOR
excess_over_gw = required_gap_meV / M_G_MAX_GW
check("C1b  the required graviton gap is g_needed = (sqrt(m2_eff)/2) mu_DW ~ 0.5 mu_DW ~ meV -- an O(1) "
      "fraction of mu_DW, i.e. a meV graviton mass.  This EXCEEDS the GW ceiling m_g<1.27e-23 eV by ~1e20 "
      "and IS the H36 identification (graviton gap = DE/mu_DW scale) the brief forbids as a re-import",
      g_needed_over_mu > 0.4 and excess_over_gw > 1e15,
      f"g_needed/mu_DW = {g_needed_over_mu:.3f} (O(1)); required gap/m_g_max = {excess_over_gw:.2e} (GW-excluded)")

# (C1c) symbolic: the whole verdict is one ratio.  sub-threshold <=> gap > (sqrt(m2_eff)/2) mu_DW.
#   with gap = H0 = mu_DW^2/(sqrt(3 Omega_L) M_Pl) [at mu_DW ~ DE scale], the condition becomes
#   mu_DW^2/(sqrt(3 Omega_L) M_Pl) > (sqrt(m2_eff)/2) mu_DW  <=>  mu_DW > (sqrt(m2_eff) sqrt(3 Omega_L)/2) M_Pl,
#   i.e. the ghost is sub-threshold ONLY if mu_DW is of ORDER M_Pl or larger -- but at mu_DW ~ M_Pl the
#   ghost is Planckian and the de Sitter gap is fixed at the OBSERVED H0 (rho_L is measured), so it fails
#   even harder (H0/g_needed ~ H0/M_Pl ~ 1e-60).  There is no self-consistent sub-threshold window.
muS, MplS, m2effS, OmS = sp.symbols("mu_DW M_Pl m2_eff Omega_L", positive=True)
gap_expr = muS**2 / (sp.sqrt(3 * OmS) * MplS)      # H0 expressed via mu_DW (mu_DW ~ DE scale limit)
needed_expr = sp.sqrt(m2effS) / 2 * muS            # g_needed = m2/2
cond = sp.simplify(gap_expr / needed_expr)          # = 2 mu_DW /(sqrt(3 Omega_L m2_eff) M_Pl)
target = sp.simplify(2 * muS / (sp.sqrt(3 * OmS * m2effS) * MplS))
check("C1c  symbolic: g_dS/g_needed = 2 mu_DW /(sqrt(3 Omega_L m2_eff) M_Pl) -- linear in mu_DW/M_Pl, so "
      "sub-threshold needs mu_DW >~ M_Pl; but rho_L (hence H0) is OBSERVED-fixed, so the natural end fails "
      "by H0/M_Pl ~ 1e-60.  No self-consistent honest window makes the ghost sub-threshold",
      sp.simplify(cond - target) == 0, f"g_dS/g_needed = {target}")

# =====================================================================================================
# NEGATIVE CONTROL -- the computation is not rigged to always say 'insufficient': a HYPOTHETICAL meV gap
# DOES move the ghost sub-threshold.  It is the SIZE of the honest gap that fails, not the logic.
# =====================================================================================================
log("\n" + "-" * 100)
log("[NEG] negative control: a hypothetical sufficient gap DOES clear -- the failure is the SIZE, not the logic")
log("-" * 100)
# toy: ghost 1.5, a hypothetical graviton gap of 1.0 (meV-analogue): sub-threshold, D one-signed.
z_hyp, _, dmx_hyp = has_real_zero(1.0, 1.5)
# and the honest ratio-of-scales, if it were >= 1, WOULD flip the verdict -- demonstrate the switch is live
verdict_would_flip_if_gap_big = (2.0 * 1.0) > 1.5  # 2*gap > m_ghost
check("NEG1  a hypothetical graviton gap = 1.0 (>= m_ghost/2 = 0.75) makes D one-signed (sub-threshold): "
      "the mechanism IS live and would clear bar(b) -- so the NOT-OPERATIVE verdict rests entirely on the "
      "honest gap being ~20-30 orders too small, not on the logic being one-sided",
      (not z_hyp) and dmx_hyp < 0.0 and verdict_would_flip_if_gap_big,
      "gap 1.0 >= m_ghost/2 => sub-threshold => OPERATIVE (hypothetical); honest gap is 1e-30 of this")
# and the clean monotone switch at gap = m_ghost/2 (reused threshold bit)
switch_clean = True
for gap in [0.5, 0.7, 0.76, 0.9]:  # m_ghost=1.5 => boundary at 0.75
    z, _, _ = has_real_zero(gap, 1.5)
    if gap < 0.75:
        switch_clean = switch_clean and z          # above threshold (pole present)
    else:
        switch_clean = switch_clean and (not z)     # sub-threshold (no pole)
check("NEG2  the sub-threshold switch is clean at gap = m_ghost/2 (pole below, none above) -- confirming "
      "the single kinematic bit; the honest gap sits ~30 orders BELOW this boundary",
      switch_clean, "on-shell pole for gap < m_ghost/2, none for gap > m_ghost/2")

# =====================================================================================================
# SUMMARY
# =====================================================================================================
log("\n" + "=" * 100)
npass = sum(1 for _, ok, _ in results if ok)
log(f"CHECKS: {npass}/{len(results)} passed.")
assert all(ok for _, ok, _ in results), "some W181 continuum-gap checks FAILED"

log("")
log("W181 VERDICT (this file is the computation, not a claim-status change):")
log("  MECHANISM (PC-A/PC-B): the ghost decays only because the graviton continuum starts at 0; a graviton")
log("     gap raises the threshold to 2*gap and CAN move the ghost sub-threshold -- IF the gap >= m_ghost/2.")
log("  HONEST IR GAP: the external issuance supplies a de Sitter/Hubble scale H0 = 1.44e-33 eV (= the DE")
log("     scale Planck-suppressed, H0 = rho_L^{1/2}/(sqrt(3 Omega_L) M_Pl)); the meV number rho_L^{1/4} is a")
log("     DENSITY scale, not a graviton mass gap.  Any graviton gap is also GW-capped at m_g < 1.27e-23 eV.")
log("  DECISIVE (D1-D4): the ghost m2 = sqrt(m2_eff) mu_DW ~ meV (floor) sits m2/(2 H0) ~ 1e30 ABOVE the")
log("     de Sitter-gapped threshold; even at the GW ceiling it is ~1e20 above; across the whole mu_DW")
log("     window g_available/g_needed is between ~1e-20 and ~1e-60, never >= 1.  The suppression is one")
log("     power of the hierarchy mu_DW/M_Pl.  GAP INSUFFICIENT.")
log("  CONDITIONAL (C1): the only clearing regime is a graviton gapped AT ~mu_DW (meV), which is the")
log("     H36-forbidden re-import (graviton gap = DE/mu_DW scale) and is GW-excluded by ~1e20.")
log("  => GAP-INSUFFICIENT-NOT-OPERATIVE-STANDS.  bar(b) does NOT clear via the external continuum-gap")
log("     mechanism.  The NOT-OPERATIVE lean of the build sprint is UNCHANGED by external source input")
log("     ACTING THROUGH THIS CHANNEL.  H59 remains OPEN.")
raise SystemExit(0)
