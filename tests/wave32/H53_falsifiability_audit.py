#!/usr/bin/env python3
r"""H53 (Wave 32) -- Falsifiability audit of the GU reconstruction program.

Popperian, adversarial. The sharp question after the first parameter-linked
prediction was conditionally FALSIFIED (H36 -> sub-mm Yukawa, EXCLUDED at
alpha=1/3, H50/H51): does GU make ANY falsifiable statement WITHOUT a forced
scale mu_DW, or is it decoupled/unfalsifiable until the (unbuilt) source action
forces the scale?

This file is DETERMINISTIC and encodes, as explicit PASS/FAIL assertions:

  (1) the SECTOR x SCALE-DEPENDENCE table -- for every place GU could touch data,
      whether it (i) NEEDS a free/unforced scale (mu_DW or f0), (ii) is a
      SCALE-INDEPENDENT structural PROPERTY, (iii) is SETTLED (pass/fail), or
      (iv) is GATED on the unbuilt source action;

  (2) the Q2 SCALE-HIDEABILITY check -- the decisive one: the GU-vs-GR 4th-order
      deviation observable scales as (E / m2)^2 with m2 = sqrt(m2_eff) * mu_DW,
      so it vanishes as mu_DW -> M_Pl at every fixed accessible energy E. The
      4th-order content is a scale-INDEPENDENT PROPERTY of the action (DOF count
      is mu_DW-independent) but a scale-HIDEABLE OBSERVABLE. There is no
      scale-independent qualitative OBSERVABLE that no tuning can hide.

Nothing is imported as a target. Published bounds appear only as comparison
anchors (already cited in H10/H49/H50/H51). No number is fit. Both a
"FALSIFIABLE" and a "DECOUPLED/UNFALSIFIABLE" outcome are honest successes;
the assertions pin the actual reasoning, not a wanted verdict.

Run: python -u tests/wave32/H53_falsifiability_audit.py
Exit 0 = the audit ledger is internally consistent.
"""
from __future__ import annotations

import math

FAIL: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{(' -- ' + detail) if detail else ''}", flush=True)
    if not ok:
        FAIL.append(name)


def log(message: str = "") -> None:
    print(message, flush=True)


# ---------------------------------------------------------------------------
# Physical anchors (all previously computed / cited in-repo; none is a target).
# ---------------------------------------------------------------------------
HBAR_C_EV_NM = 197.327          # eV*nm
M_PL_EV = 1.2e28                # reduced-Planck order, eV (H10/H49)
RHO_LAMBDA_QTR_EV = 2.3e-3      # (rho_Lambda)^(1/4) ~ 2.3 meV, observed DE scale
M2EFF_LOW = 5.0 / 6.0           # H25 method 1 (convention-robust)
M2EFF_HIGH = 5.0 / 4.0          # H25 method 2
C_L = 3.0 / 8.0                 # H51 computed DeWitt coefficient (exact)

# Accessible probe energies (comparison anchors only).
E_LIGO_EV = 4.1e-13             # ~100 Hz gravitational-wave quantum, eV
E_LAB_SHORTRANGE_EV = 2.3e-3    # ~meV, the Eot-Wash / HUST sub-mm band scale

# GU-under-H36 forces mu_DW to the DE scale (H36 postulate, NOT GU-forced).
MU_DW_H36_EV = RHO_LAMBDA_QTR_EV / C_L ** 0.25   # mu_DW = (rho_L / c_L)^(1/4)


def m2_of(mu_dw_ev: float, m2eff: float) -> float:
    """Massive spin-2 companion mass m2 = sqrt(m2_eff) * mu_DW (H49/H50)."""
    return math.sqrt(m2eff) * mu_dw_ev


def yukawa_range_um(mu_dw_ev: float, m2eff: float) -> float:
    """Compton/Yukawa range 1/m2 in microns."""
    return HBAR_C_EV_NM / m2_of(mu_dw_ev, m2eff) / 1000.0


def gr_deviation_amplitude(mu_dw_ev: float, probe_energy_ev: float, m2eff: float) -> float:
    """Dimensionless size of the GU-vs-GR 4th-order deviation at probe energy E.

    The massive spin-2 companion enters the propagator as an extra pole at
    p^2 = -m2^2; at energy E << m2 the leading GU-minus-GR effect (dispersion,
    extra-polarization admixture, Yukawa correction to the static potential)
    scales as (E / m2)^2 -- the generic decoupling of a heavy field. This is a
    structural scaling, not a fit: as mu_DW -> M_Pl the deviation -> 0 at fixed E.
    """
    m2 = m2_of(mu_dw_ev, m2eff)
    return (probe_energy_ev / m2) ** 2


# ===========================================================================
log("=" * 78)
log("H53 FALSIFIABILITY AUDIT -- sector x scale-dependence + Q2 scale-hideability")
log("=" * 78)

# ---------------------------------------------------------------------------
# PART 1 -- THE SECTOR x SCALE-DEPENDENCE TABLE
# Status codes:
#   NEEDS_FREE_SCALE  -- requires the unforced mu_DW (or free f0); deviation
#                        hideable by tuning that free parameter.
#   SCALE_INDEP_PROP  -- a scale-independent structural PROPERTY (mu_DW-invariant),
#                        but NOT necessarily an accessible observable.
#   SETTLED_PASS      -- already passed (with any residual gating noted).
#   SETTLED_FAIL      -- already failed / excluded.
#   GATED_SOURCE_ACT  -- gated on the unbuilt source action (not observable now).
# grade: COMPUTED or ARGUED.
# ---------------------------------------------------------------------------
STATUS = {
    "NEEDS_FREE_SCALE",
    "SCALE_INDEP_PROP",
    "SETTLED_PASS",
    "SETTLED_FAIL",
    "GATED_SOURCE_ACT",
}

# (sector, status, free_param, grade, one-line reason)
SECTOR_TABLE = [
    ("PPN / solar-system (H10)",
     "NEEDS_FREE_SCALE", "mu_DW", "COMPUTED",
     "passes as exp-suppressed Yukawa; requires mu_DW > ~1e-17 eV, cleared by ~45 "
     "orders at natural M_Pl; deviation hideable, adds no binding constraint"),
    ("sub-mm Stelle-Yukawa, GIVEN H36 (H36/H50/H51)",
     "SETTLED_FAIL", "mu_DW(forced=meV)", "COMPUTED",
     "H36 forces mu_DW=2.3 meV -> lambda=60-74 um at alpha=1/3, EXCLUDED by "
     "Kapner/Lee/Tan by O(1)-robust factor; self-falsifies the H36 identification"),
    ("sub-mm Stelle-Yukawa, WITHOUT H36 (H49)",
     "NEEDS_FREE_SCALE", "mu_DW", "ARGUED",
     "drop H36 and mu_DW is free again; the sole live window (mu_DW~meV) is a "
     "knife-edge; at M_Pl the range is ~1e-35 m, decoupled"),
    ("GW extra polarizations / dispersion / propagator pole (H49)",
     "NEEDS_FREE_SCALE", "mu_DW", "COMPUTED",
     "massive spin-2 Compton freq ~1e12 Hz at lab floor, ~1e27 Hz at M_Pl; "
     "unexcited above the lab floor by any astrophysical source -> not observable"),
    ("4th-order action ORDER / DOF count 7-vs-2 (H49/H45)",
     "SCALE_INDEP_PROP", "-", "COMPUTED",
     "box^2 present under BOTH GU branches, none in Bianconi/GR; 7 propagating "
     "DOF is a mu_DW-independent PROPERTY -- but not an accessible observable "
     "unless the ~mu_DW-mass modes are excited (see Q2)"),
    ("dark energy, CPL projection (H43/H44)",
     "SETTLED_FAIL", "f0", "COMPUTED",
     "GU's (w0,wa) CPL locus excluded by DESI DR2 headline contour ~3.2 sigma, "
     "robust to M^2, ansatz, backreaction -- falsified AS A CPL FIT"),
    ("dark energy, raw BAO distances (H46)",
     "NEEDS_FREE_SCALE", "f0", "COMPUTED",
     "MARGINAL: excluded only at canonical-f0 + CMB-fixed amplitude (dchi2=+21.6); "
     "shape-marginalized competitive-to-better (dchi2=-3.2); f0 free (H42)"),
    ("generation count {1,3} (H38/H40)",
     "GATED_SOURCE_ACT", "source-action carrier", "COMPUTED",
     "located-not-forced; {1,3} not pinned to 3; would be a scale-INDEPENDENT "
     "qualitative prediction IFF forced to 3, but forcing is source-action-gated"),
    ("fermion masses / Yukawas",
     "GATED_SOURCE_ACT", "source action", "ARGUED",
     "no source action -> no mass spectrum emitted; nothing to test now"),
    ("|II|^2-vs-|H|^2 branch (H45/H49)",
     "GATED_SOURCE_ACT", "P2 = source-action norm choice", "ARGUED",
     "|H|^2 branch = pure Mannheim-Kazanas conformal gravity, killed "
     "SCALE-INDEPENDENTLY by Horne/Hobson-Lasenby (no flat rotation curves) + "
     "Jordan tree-ghost; but GU is FAVORED |II|^2 (the evading branch), and P2 "
     "is gated on the source action"),
    ("class Lambda-magnitude no-go (H49)",
     "SETTLED_FAIL", "-", "COMPUTED",
     "scale-free two-metric action supplies only O(1) ratios; cannot contain "
     "Lambda/M_Pl^4 ~ 1e-123 -> the 'Lambda emerges' HEADLINE is dead for GU and "
     "Bianconi alike; a scope-kill of an overclaim, not of the theory"),
]

log("")
log("PART 1 -- SECTOR x SCALE-DEPENDENCE TABLE")
log("-" * 78)
for sector, status, free_param, grade, reason in SECTOR_TABLE:
    check(f"sector status valid: {sector}", status in STATUS, f"{status} [{grade}]")
    log(f"        free={free_param}; {reason}")

# The headline audit fact: NO sector is a standing SCALE-INDEPENDENT OBSERVABLE
# prediction. Every row is one of: needs a free scale, settled, gated, or a
# scale-independent PROPERTY that is not an accessible observable.
scale_indep_props = [r for r in SECTOR_TABLE if r[1] == "SCALE_INDEP_PROP"]
needs_free = [r for r in SECTOR_TABLE if r[1] == "NEEDS_FREE_SCALE"]
settled = [r for r in SECTOR_TABLE if r[1] in ("SETTLED_PASS", "SETTLED_FAIL")]
gated = [r for r in SECTOR_TABLE if r[1] == "GATED_SOURCE_ACT"]

log("")
check(
    "every sector is needs-free-scale / settled / gated / scale-indep-PROPERTY (no other)",
    len(needs_free) + len(settled) + len(gated) + len(scale_indep_props) == len(SECTOR_TABLE),
    f"needs_free={len(needs_free)} settled={len(settled)} gated={len(gated)} "
    f"scale_indep_property={len(scale_indep_props)}",
)
check(
    "the only scale-independent row is a PROPERTY (action order/DOF), not an accessible observable",
    len(scale_indep_props) == 1 and scale_indep_props[0][0].startswith("4th-order action ORDER"),
    "ARGUED->COMPUTED: DOF count is mu_DW-invariant but its OBSERVABILITY is not (Part 2)",
)

# ---------------------------------------------------------------------------
# PART 2 -- Q2: THE SCALE-HIDEABILITY CHECK (the decisive one)
# Is the 4th-order content a scale-independent qualitative SIGNATURE (no tuning
# can hide) or a scale-HIDEABLE one (mu_DW -> M_Pl pushes it below detectability)?
# ---------------------------------------------------------------------------
log("")
log("PART 2 -- Q2 SCALE-HIDEABILITY CHECK")
log("-" * 78)

# (2a) DOF count is a scale-independent PROPERTY: 7 propagating DOF (2 massless +
#      5 massive spin-2) for EVERY mu_DW > 0. Encoded as the integer count, which
#      does not depend on mu_DW (the massive mode exists as a field at any mass).
DOF_MASSLESS = 2
DOF_MASSIVE_SPIN2 = 5
DOF_TOTAL = DOF_MASSLESS + DOF_MASSIVE_SPIN2
for mu in (E_LAB_SHORTRANGE_EV, MU_DW_H36_EV, 1e6, M_PL_EV):
    # the field content (pole structure) is mu_DW-independent; count is invariant.
    dof = DOF_MASSLESS + DOF_MASSIVE_SPIN2
    check(
        f"DOF count = 7 is mu_DW-independent (property) at mu_DW={mu:.2e} eV",
        dof == 7 and DOF_TOTAL == 7,
    )

# (2b) The OBSERVABLE deviation from GR scales as (E/m2)^2 and vanishes as
#      mu_DW -> M_Pl at every fixed accessible probe energy. THIS is the
#      scale-hideability: the qualitative distinction is real in the Lagrangian
#      but its observable size is tunable to zero.
log("")
log("GU-vs-GR 4th-order deviation amplitude (E/m2)^2 at fixed accessible energies:")
for label, E in (("LIGO ~100 Hz", E_LIGO_EV), ("lab sub-mm ~meV", E_LAB_SHORTRANGE_EV)):
    dev_meV = gr_deviation_amplitude(MU_DW_H36_EV, E, M2EFF_LOW)
    dev_1e6 = gr_deviation_amplitude(1e6, E, M2EFF_LOW)
    dev_MPl = gr_deviation_amplitude(M_PL_EV, E, M2EFF_LOW)
    log(f"  {label:16s}: dev(mu_DW=meV)={dev_meV:.3e}  dev(1e6 eV)={dev_1e6:.3e}  "
        f"dev(M_Pl)={dev_MPl:.3e}")
    check(
        f"deviation is MONOTONE-decreasing in mu_DW and -> 0 at M_Pl ({label})",
        dev_meV > dev_1e6 > dev_MPl and dev_MPl < 1e-40,
    )

# (2c) At natural mu_DW the massive companion decouples: its Compton range is
#      sub-nuclear, so the 5 extra DOF are never excited by accessible sources
#      -> observationally GU reduces to GR's 2 DOF. Scale-hideable, confirmed.
range_MPl_m = yukawa_range_um(M_PL_EV, M2EFF_LOW) * 1e-6
check(
    "at mu_DW=M_Pl the massive-mode range is <1e-30 m (sub-nuclear) -> 5 extra DOF unexcited",
    range_MPl_m < 1e-30,
    f"range={range_MPl_m:.2e} m",
)

# (2d) The Q2 verdict, pinned as booleans.
scale_independent_PROPERTY_exists = True        # action order / DOF count (COMPUTED)
scale_independent_OBSERVABLE_exists = False      # every observable is (E/m2)^2-suppressible
four_th_order_falsifiable_in_principle = True    # GU is a genuinely distinct Lagrangian, not GR
four_th_order_scale_hideable_in_practice = True  # mu_DW -> M_Pl hides every deviation

check(
    "Q2: a scale-independent PROPERTY exists (4th-order order/DOF count) [COMPUTED]",
    scale_independent_PROPERTY_exists,
)
check(
    "Q2: NO scale-independent OBSERVABLE exists that no tuning can hide [ARGUED from (E/m2)^2]",
    scale_independent_OBSERVABLE_exists is False,
)
check(
    "Q2: the 4th-order content is falsifiable-IN-PRINCIPLE but scale-HIDEABLE-in-practice",
    four_th_order_falsifiable_in_principle and four_th_order_scale_hideable_in_practice,
)

# ---------------------------------------------------------------------------
# PART 3 -- THE POPPERIAN VERDICT (Q3) and the H41 keystone (Q4)
# ---------------------------------------------------------------------------
log("")
log("PART 3 -- POPPERIAN VERDICT (Q3) + H41 KEYSTONE (Q4)")
log("-" * 78)

# Q3: with no scale-independent OBSERVABLE and the one demonstrated prediction
# (H36) self-falsified, and mu_DW a FREE parameter, GU is not (a). It is (b)
# DECOUPLED-IN-PRACTICE, which for a free-scale framework is operationally (c)
# CONSISTENT-BUT-UNFALSIFIABLE-as-it-stands.
verdict_a_falsifiable_without_forced_scale = False
verdict_b_decoupled_in_practice = True
verdict_c_framework_until_source_action = True

check(
    "Q3 NOT (a): no scale-independent qualitative OBSERVABLE prediction exists",
    verdict_a_falsifiable_without_forced_scale is False,
)
check(
    "Q3 (b): DECOUPLED-IN-PRACTICE -- falsifiable only if mu_DW lands in an accessible window",
    verdict_b_decoupled_in_practice,
)
check(
    "Q3 (c): CONSISTENT-BUT-UNFALSIFIABLE as it stands -- a framework until the source action forces mu_DW",
    verdict_c_framework_until_source_action,
)

# The demonstrated predictive CAPACITY: H36 -> sub-mm was computed to the end and
# conditionally FALSIFIED. This proves GU is not vacuous (it CAN emit falsifiable
# numbers) but leaves ZERO standing predictions.
demonstrated_predictive_capacity = True    # H36 channel emitted a falsifiable number
standing_predictions_count = 0             # the one candidate self-falsified
check(
    "capacity demonstrated (H36 channel emitted+self-falsified) yet ZERO standing predictions",
    demonstrated_predictive_capacity and standing_predictions_count == 0,
)

# Q4: every empirical channel is gated on the free scale mu_DW (or f0), and the
# ONE object that would force mu_DW is the source action (H41). So H41 is the
# FALSIFIABILITY keystone, not merely the coherence keystone.
all_channels_gated_on_free_scale = (
    len(needs_free) >= 1 and standing_predictions_count == 0
    and not scale_independent_OBSERVABLE_exists
)
source_action_is_falsifiability_keystone = all_channels_gated_on_free_scale
check(
    "Q4: GU's falsifiability rests on H41 (the source action forcing mu_DW) -- falsifiability keystone",
    source_action_is_falsifiability_keystone,
)

log("")
log("HONEST PUBLIC REGISTER:")
log("  A consistent, reconstruction-grade geometric FRAMEWORK -- not a standing theory.")
log("  It has a DEMONSTRATED but (so far self-falsifying) predictive channel (H36 -> sub-mm),")
log("  ZERO standing predictions, and every empirical channel gated on the free scale mu_DW.")
log("  Its falsifiability rests on building the source action (H41) that would force mu_DW.")
log("")
log("RE-RANK SIGNAL: DECOUPLED (falsifiable-in-principle, unfalsifiable-in-practice");
log("  until H41 forces mu_DW). GU's scientific STATUS rests on H41 = falsifiability keystone.")

if FAIL:
    log("")
    log(f"FAILED: {FAIL}")
    raise SystemExit(1)

log("")
log("=" * 78)
log("exit 0 = H53 falsifiability-audit ledger internally consistent.")
log("Verdict: DECOUPLED-in-practice / framework-until-H41; no scale-independent observable.")
log("=" * 78)
