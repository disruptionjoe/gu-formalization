---
title: "Temporal Issuance as GU Source Action - Three Steelmen"
date: 2026-06-27
status: exploration
doc_type: crosswalk
verdict: STEELMAN_ONLY_NO_CLAIM_PROMOTION
optional_executable:
  - tests/temporal_issuance_source_action_steelmen_checker.py
depends_on:
  - explorations/time-as-finality-crosswalk/record-issuance-boundary-selector-2026-06-26.md
  - explorations/shiab-operator/shiab-selector-search-2026-06-26.md
  - active-research/topological-generation-count-families-k3-chi-gate-2026-06-26.md
  - active-research/signed-readout/theorem-statement-v1-2026-06-23.md
external_context:
  - ../../../temporal-issuance/FORMAL-OBJECT.md
  - ../../../temporal-issuance/explorations/E087-online-issuance-formal-object-v0-1-2026-06-25.md
  - ../../../temporal-issuance/explorations/E080-gu-effect-typed-witness-transport-2026-06-25.md
---

# Temporal Issuance as GU Source Action - Three Steelmen

## Purpose

This packet turns three versions of the hypothesis "the GU source action is, or is realized by,
Temporal Issuance" into hostile, bounded GU crosswalks.

The point is not to promote the hypothesis. The point is to give it the strongest form that still
respects the repo's current negative results:

- the written GU source action is missing;
- GU-derived shiab selectors currently stop at a residual 4-real-dimensional family;
- record-issuance / spectral-section language is a real boundary idea for the noncompact index,
  but is null as a shiab selector unless a geometric carrier is added;
- Temporal Issuance effect typing separates `Issue[S]` from `Project[O]`, `Finalize[R]`, and
  `Lose[K]`;
- the theta / FLRW cosmology lane is OPEN and sign-sensitive.

## Version Map

| version | strongest charitable reading | immediate role | current ceiling |
|---|---|---|---|
| V1 formal integration | issuance is the admissible source-extension process that could select a shiab family member and supply a spectral section | define an interface contract between `Issue[S]` and GU source geometry | no selection without a GU-native source carrier |
| V2 computational / observer | issuance is the source rewrite process; observers see lossy final records and signed readouts | explains why bulk selectors fail and why boundary objects partially work | observer finality cannot become source action by itself |
| V3 cosmological / physical | issuance is ongoing source injection whose accounting could look like theta/dark energy or expansion | long-range bridge target | killed if circularly defined from energy, expansion, or DESI fit targets |

## Shared Boundary

All three versions use the same effect gate:

```text
Issue[S]      source-side admissible extension
Project[O]    observer readout
Finalize[R]   record-finality operation
Lose[K]       information loss under projection
```

Only `Issue[S]` can play source-action. A spectral section, boundary projection, observer
record, signed readout, or Wolfram-style observer cut can help audit or regularize a future GU
construction, but it does not generate a GU source action unless it carries a GU-native geometric
datum.

The required extra datum is not vocabulary. It must be at least one of:

- a family-coordinate functional on the residual shiab family;
- a boundary holonomy / connection / curvature carrier that determines a spectral section;
- a source-derived characteristic class or KSp class;
- a noncircular source accounting invariant that couples to theta / cosmology without using the
  target observable as input.

## Immediate Checker

The companion checker is intentionally small. It verifies the finite claims these notes rely on:

- record-only issuance does not select a unique shiab member;
- a unique toy selection requires a source-side family-coordinate carrier;
- `S3` boundary eta is shiab-blind in the toy, while a lens-space boundary can move an index toy;
- monotone provenance can coexist with non-monotone signed readout;
- record finality without a holonomy carrier cannot supply a spectral section;
- cosmology bridges are killed if they define issuance from ordinary energy or lack a noncircular
  accounting invariant.

Run:

```powershell
python tests\temporal_issuance_source_action_steelmen_checker.py
```

## Recommended Order

1. Run V1 first. It is closest to current GU artifacts and has the clearest kill criteria.
2. Run V2 second. It is the best explanation of why the boundary instinct is structurally right
   but not yet source-generative.
3. Keep V3 as a roadmap item only. It should not drive canon movement until V1 or V2 produce a
   source-side carrier.

## Machine-Readable Summary

```json
{
  "artifact": "TI_AS_GU_SOURCE_ACTION_THREE_STEELMEN",
  "status": "exploration",
  "claim_promotion": false,
  "versions": [
    "V1_FORMAL_INTEGRATION",
    "V2_WOLFRAM_SIGNED_READOUT",
    "V3_COSMOLOGICAL_PHYSICAL"
  ],
  "global_kill_conditions": [
    "record_finality_relabelled_as_source_action",
    "unique_shiab_selection_without_source_carrier",
    "boundary_spectral_section_without_holonomy_or_connection_data",
    "cosmology_bridge_defined_from_target_energy_or_expansion",
    "contradiction_with_current_shiab_existence_or_weak_field_canon"
  ],
  "next_executable": "tests/temporal_issuance_source_action_steelmen_checker.py"
}
```
