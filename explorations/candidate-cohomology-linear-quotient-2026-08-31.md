---
artifact_type: exploration
status: active_research
doc_type: exact_linear_candidate_cohomology_quotient
created: 2026-08-31
title: "Candidate middle cohomology as a linear quotient"
owner: gu-formalization
claim_status: repository_derived
claim_ceiling: "Exact carrier equivalence between the existing cycle/gauge quotient and ker(d1)/range(d0), with induced linear chain maps; no source-selected complex, analytic domain, positive state space, physical pairing, observable, probability, or dynamics."
target_claim: "INTERNAL — candidate middle cohomology has the canonical module quotient presentation and chain maps descend linearly; verdict: CONSTRUCTED"
canon_verdict_change: none
lean: Lean/GUFormalization/CandidateCohomologyLinear.lean
probe: tests/channel-swings/candidate_cohomology_linear_probe.py
---

Classification: `INTERNAL_STRUCTURAL_ONLY`

```gu-typed-objects
result: canonical linear presentation of supplied candidate middle cohomology
carrier: kernel of supplied field-to-equation differential modulo the gauge-image submodule LAYER=UNTYPED CHIRALITY=N/A
pairing: NONE; the separate gauge-basic pairing remains supplied algebraic data
real_structure: UNTYPED; no selected real, complex, antilinear or Krein structure
grading: middle cohomological degree of a supplied three-stage complex
action_owner: repository-construction over a supplied complex; no source-owned action
target: equivalence with the existing cycle/gauge quotient and functorial linear chain-map descent MAP-TYPE=isomorphism
```

# Candidate middle cohomology as a linear quotient

## Result

The existing candidate quotient retains its representative-level definition:
middle cycles modulo the relation of differing by a gauge image. Lean now
constructs the canonical module presentation

```text
ker(d1) / range(d0 : gauge -> ker(d1)).
```

Square-zero places every gauge image in the cycle module. Sending an existing
cycle class to the same kernel representative is bijective: equality in the
module quotient produces exactly a gauge witness in the original relation,
and every module quotient class has a cycle representative. Every supplied
chain map restricts to a linear map on kernels, carries the gauge range into
the target gauge range, and therefore descends to a linear cohomology map. Its
underlying carrier map agrees with the already-defined quotient map.

The exact GF(2) control uses a three-dimensional field space, a two-dimensional
cycle kernel and a one-dimensional gauge range, leaving one cohomology
dimension. Quotienting all fields instead leaks noncycles, omitting the gauge
range leaks extra classes, and a map that fails to preserve gauge images does
not descend.

## Scientific boundary

This identifies the correct algebraic carrier for a supplied complex. It does
not construct that complex from GU's source action and does not identify the
quotient with a physical state space. No analytic domain, positive or Krein
completion, conserved physical pairing, observable, probability rule, or
dynamics is supplied.
