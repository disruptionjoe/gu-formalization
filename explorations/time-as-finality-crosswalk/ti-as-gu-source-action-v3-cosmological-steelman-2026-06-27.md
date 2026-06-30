---
title: "V3: Temporal Issuance as GU Source Action - Cosmological Steelman"
date: 2026-06-27
status: exploration
doc_type: crosswalk
verdict: PARKED_LONG_RANGE_STEELMAN_ONLY
optional_executable:
  - tests/temporal_issuance_source_action_steelmen_checker.py
depends_on:
  - explorations/time-as-finality-crosswalk/ti-as-gu-source-action-three-steelmen-2026-06-27.md
  - canon/theta-field-flrw-dark-energy-eos.md
  - canon/dark-energy-theta-divergence-free.md
  - canon/schwarzschild-weak-field-rfail.md
  - lab/roadmap/meaningful-next-steps-2026-06-26.md
external_context:
  - ../../../temporal-issuance/FORMAL-OBJECT.md
  - ../../../temporal-issuance/absorbers/cosmological-expansion.md
---

# V3: Cosmological Steelman

## Steelman Statement

Temporal Issuance is the ongoing source-side injection of admissible structure into GU geometry.
In the strongest long-range reading, this source process could provide the missing accounting
behind theta-field dynamics, boundary curvature, expansion, or dark-energy-like behavior.

This is the broadest and riskiest version. It must not start from cosmological targets and work
backward. It needs a noncircular source accounting object:

```text
Q_Iss(e) = source-side issuance accounting invariant
```

whose conservation, flux, residue, or variation couples to GU geometry before any DESI, FLRW,
or dark-energy target is used.

## Why This Version Is Worth Keeping

The repo's source-action wall gates more than one problem. A real source action would not merely
select the shiab; it would also determine source currents, Noether identities, theta-sector
coefficients, and boundary curvature data.

So a cosmological bridge is not absurd. It is just downstream. It becomes meaningful only after
a source-side accounting invariant exists independently of the cosmological readout.

## Noncircular Interface

A viable V3 bridge must provide:

| required field | reason |
|---|---|
| source-side accounting invariant `Q_Iss` | prevents defining issuance as ordinary energy |
| source variation or conservation law | connects to action, current, or Noether identity |
| theta / boundary curvature coupling | gives a GU-native geometric carrier |
| FLRW reduction | produces testable `w_0`, `w_a`, or high-z behavior |
| weak-field compatibility | avoids contradicting Schwarzschild / GR recovery gates |
| anomaly / index compatibility | avoids solving cosmology by breaking the math core |

## Test Steps

### Test 1: Theta / FLRW Link

Try to map `Q_Iss` to the theta-field lane:

```text
Q_Iss variation -> source current / theta effective source -> FLRW scalar reduction
```

This must be checked against the current theta canon:

- EOS-vs-DESI status is OPEN;
- the ratio `w_a/(w_0+1)=+1.17` is frozen-IC and sign-sensitive;
- proper slow-roll high-z ICs are unresolved;
- the source-action coefficient is not written.

Kill if the bridge chooses parameters to match DESI or imports the target sign.

### Test 2: Expansion As Net Issuance

Build a toy where issuance growth affects an effective scale or accessible structure count.
Then ask whether it factors through an already fixed energy, entropy, volume, or observer-access
schedule.

Expected result today:

```text
most toys are absorbed by fixed-law growth, thermodynamics, or observer projection.
```

Only a source-side accounting invariant with a GU-native variation law should survive.

### Test 3: Energy Accounting Residue

Ask whether the bridge emits a conserved or controlled residue:

```text
dQ_Iss = source flux
variation of S_source produces current
GR/weak-field limit recovers ordinary stress-energy shadow
```

Kill if `Q_Iss` is defined from ordinary energy density, Hubble expansion, DESI fit parameters,
or a target equation of state.

## Kill Criteria

Kill or demote V3 if:

- `CIRCULAR_ENERGY_ACCOUNTING`: issuance is defined from energy, dark energy, expansion, or
  observed acceleration.
- `NO_NONCIRCULAR_ACCOUNTING_INVARIANT`: no independent `Q_Iss` or source residue is written.
- `NO_THETA_CARRIER`: no source-derived theta, boundary curvature, or source current is
  produced.
- `CONTRADICTS_CANON`: the bridge contradicts theta divergence-free gates, weak-field gates, or
  anomaly/index constraints.
- `TARGET_FITTING`: the bridge uses DESI, Lambda-CDM, or generation count targets to select its
  own rule.

## Current Verdict

V3 is parked. It is a legitimate long-range steelman, but it should not drive immediate GU work.
The right sequencing is:

```text
V1 source carrier or V2 holonomy carrier first;
cosmological accounting only after a source-side invariant exists.
```

Until then, V3 is a roadmap and absorber test, not evidence for GU cosmology.

## Machine-Readable Summary

```json
{
  "artifact": "TI_GU_SOURCE_ACTION_V3_COSMOLOGICAL",
  "status": "PARKED_LONG_RANGE",
  "claim_promotion": false,
  "survives_as": "roadmap_only_until_source_accounting_exists",
  "required_carriers": [
    "noncircular_Q_Iss",
    "source_variation_or_Noether_identity",
    "theta_or_boundary_curvature_coupling",
    "FLRW_reduction_without_target_fitting"
  ],
  "kill_criteria": [
    "CIRCULAR_ENERGY_ACCOUNTING",
    "NO_NONCIRCULAR_ACCOUNTING_INVARIANT",
    "NO_THETA_CARRIER",
    "CONTRADICTS_CANON",
    "TARGET_FITTING"
  ]
}
```
