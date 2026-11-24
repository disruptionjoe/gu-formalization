---
title: Six-spinor surviving-grading compatibility
status: process
operational_state: active
doc_type: work-packet
created: '2026-11-24'
classification: INTERNAL_STRUCTURAL_ONLY
---

# Six-spinor grading compatibility

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Joe24b puts this first in eligible B slots. Existing T1-first and regular LC cadence remain. This is one structural realization test, not source-operator construction.

```yaml
packet_status: active
authority: joe_direct_chat_2026_11_24_b
target: X-P1-P2-P3
secondary_target: P3xglobal_index
family: F16-K95-spectral / R6-Bn0
steps:
- id: 0
  status: done
  target: X-P1-P2-P3
  tier: T3
  expected_delta: Scope exact family before algebra
  actual_delta: Exact spectral ansatz and six-spinor reconstruction preregistered
  kill_condition: No silent transfer outside the declared family
  evidence:
  - explorations/conditional-build/six-spinor-grading-scope-2026-11-24.md
- id: 1
  status: done
  target: X-P1-P2-P3
  tier: T2; T1 if scoped exclusion
  expected_delta: Classify surviving hidden+chi_H extensions satisfying principal and torsion equations
  kill_condition: No grade in F16-K95-spectral/R6-Bn0 meets the stated equations; scope exclusion to this
    realization
  work: Read preregistered scope; retain trace/scalar mixing and correct K95 sharp law; solve principal
    then NW torsion, including grade derivatives
  depends_on:
  - 0
  evidence: &id001
  - explorations/conditional-build/six-spinor-grading-scope-2026-11-24.md
  - explorations/conditional-build/six-spinor-grading-compatibility-2026-11-24.md
  - explorations/conditional-build/localization-applicability-audit-2026-11-24.md
  - lab/process/six-spinor-grading-compatibility.json
  - tests/program-focus/six_spinor_grading_compatibility_probe.py
  - Lean/GUFormalization/SixSpinorGrading.lean
  - lab/process/hostile-reviews/2026-11-24-six-spinor-grading-review.md
  actual_delta: The R6-Bn0 K95 tangential reconstruction has no same-input/output grade descending to
    its full six-spinor observation with horizontal chi_H. Principal equations force a unique parallel
    receiver grade; retained NW torsion gives an injective128-spinor anticommutator witness. This excludes
    the last F16 spectral choice and any hidden-grade or kernel-preserving-shear repair of this same realization.
    The already-held constant chiral-W wrapper preserves the obstruction. It does not exclude source effective
    chirality or class C. Localization native transfer and normal-L2 necessity remain unestablished; its
    short applicability audit is complete without promotion.
- id: 2
  status: done
  target: X-P1-P2-P3
  tier: T3
  expected_delta: Record reviewed exclusion or candidate, remaining burdens and next discriminator
  kill_condition: No classC or physical-index credit without bridge
  depends_on:
  - 1
  evidence: *id001
  actual_delta: The R6-Bn0 K95 tangential reconstruction has no same-input/output grade descending to
    its full six-spinor observation with horizontal chi_H. Principal equations force a unique parallel
    receiver grade; retained NW torsion gives an injective128-spinor anticommutator witness. This excludes
    the last F16 spectral choice and any hidden-grade or kernel-preserving-shear repair of this same realization.
    The already-held constant chiral-W wrapper preserves the obstruction. It does not exclude source effective
    chirality or class C. Localization native transfer and normal-L2 necessity remain unestablished; its
    short applicability audit is complete without promotion.
- id: 3
  status: ready
  target: X-P1-P2-P3
  tier: T2; T1 if scoped exclusion
  expected_delta: Determine whether admitted metric normal-connection extensions preserve or remove the
    same observed grading defect
  kill_condition: Exclude only the structurally specified extension family after observation/descent/principal/lower/grade
    equations are all carried; no all-non-LC or classC inference
  work: 'Next eligible B-slot: classify whether the six-spinor oddness obstruction survives the already-admitted
    metric normal-connection extensions B_n, with the actual observation, coherent-jet prescription, full
    principal symbol and complete exterior torsion carried together. First derive the admissibility/observation-preservation
    equations; do not choose a fitted connection or build the source operator. The fixed R6-Bn0 result
    is retained; expanding only the hidden grading commutant cannot repair it. Non-metric source connections
    and distinct field/equation/current grading laws remain separately typed. Localization stays demoted
    until both native theorem transfer and normal-L2 necessity are proved. Carry the unused count31 LC
    opportunity into the next regular run before further B work; recurring cadence unchanged.'
  depends_on:
  - 2
next_step: 3
```
