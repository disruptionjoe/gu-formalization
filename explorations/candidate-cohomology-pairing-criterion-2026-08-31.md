---
artifact_type: exploration
status: active_research
doc_type: exact_conditional_cohomology_pairing_criterion
created: 2026-08-31
title: "Gauge-basic pairing descent and radical criterion"
owner: gu-formalization
claim_status: repository_derived
claim_ceiling: "Exact algebraic cycle/gauge quotient criterion only; no source action, analytic domain, selected real/Krein form, positivity, conservation, probability rule, observable, or physical state space."
target_claim: "INTERNAL — a supplied bilinear form descends through candidate cohomology under two-sided gauge basicness, and its descended radical is trivial exactly when the cycle radical is the gauge image; verdict: CONSTRUCTED"
canon_verdict_change: none
lean: Lean/GUFormalization/CandidateCohomologyPairing.lean
probe: tests/channel-swings/candidate_cohomology_pairing_probe.py
---

Classification: `INTERNAL_STRUCTURAL_ONLY`

```gu-typed-objects
result: gauge-basic bilinear descent and left/right radical iff criteria
carrier: middle-cycle subtype modulo gauge equivalence LAYER=UNTYPED CHIRALITY=N/A
pairing: supplied R-bilinear form annihilating gauge images in both arguments ON=middle-field-carrier; no positivity or conservation
real_structure: UNTYPED; no selected real, complex, antilinear or Krein structure
grading: three-stage gauge to field to equation complex; middle cohomological degree only
action_owner: repository-construction over a supplied complex; no source-owned action
target: candidate middle cohomology quotient MAP-TYPE=quotient
```

# Gauge-basic pairing descent and radical criterion

## Result

Let `C0 -> C1 -> C2` be the supplied three-stage complex and let the candidate
middle cohomology be the quotient of actual cycles by gauge images. A supplied
bilinear form `b : C1 x C1 -> R` descends through both quotient arguments when

```text
b(d0 g, y) = 0,      b(x, d0 g) = 0.
```

Lean constructs the descended function on cycle classes. It then proves two
sharp iff statements:

```text
left nondegenerate on quotient classes
  iff every left-radical cycle is a gauge image,

right nondegenerate on quotient classes
  iff every right-radical cycle is a gauge image.
```

The exact GF(2) control uses a four-element cycle carrier, a two-element gauge
image, and a two-class quotient. Its form has radical exactly equal to the
gauge image. A planted noncycle is excluded, a non-gauge-basic form changes
under representatives, and the zero form exposes an extra nongauge radical.

## Scientific boundary

This is an algebraic interface, not a physical state space. It says precisely
what a proposed pairing must establish at the quotient boundary; it does not
provide the source action, analytic domain, real/Krein owner, conserved
positive majorant, interacting observable, probability rule, or empirical
interpretation. Those dependencies remain open and cannot be inferred from
quotient nondegeneracy alone.
