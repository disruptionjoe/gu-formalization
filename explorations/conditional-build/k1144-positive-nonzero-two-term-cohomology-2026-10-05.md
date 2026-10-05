---
title: "K1144 positive nonzero two-term cohomology"
status: active_research
doc_type: exact_two_term_physical_cohomology_criterion
created: 2026-10-05
claim_ceiling: exact finite-dimensional cohomology-pairing criterion; no source BV/BFV complex
manifest: lab/process/k1144-positive-nonzero-two-term-cohomology.json
probe: tests/channel-swings/k1144_positive_nonzero_two_term_cohomology_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1144 positive nonzero two-term cohomology

> **GU-COMPARATOR-ROUTING — scope before inference.** This theorem tests a
> supplied two-term gauge/constraint complex. It does not construct the source
> BV/BFV maps or identify its cohomology with physical states. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

```gu-typed-objects
result: exact positivity and nontriviality criterion for degree-zero cohomology
carrier: finite complex G0 --d--> V --Q--> C with Qd=0 LAYER=source-print CHIRALITY=N/A
pairing: symmetric constrained form H on ker Q ON=degree-zero-cohomology
real_structure: real finite complex
grading: gauge image, constrained cycles and physical classes
action_owner: comparator -- d Q and H require a separately source-owned complex
target: K1140 nonzero-positive-cohomology gate MAP-TYPE=restriction
```

For `Qd=0`, degree-zero cohomology is

```text
H0 = ker Q / im d.
```

A symmetric form on `ker Q` descends to `H0` exactly when `im d` lies in its
radical. The induced form is positive definite exactly when the restricted
form is nonnegative and

```text
rad(H|ker Q) = im d.                                              (1)
```

The physical space is nonzero exactly when `dim ker Q > rank d`. The pass
fixture takes `Q=(1,0,0,0)`, `im d=span(e2)` and
`H=diag(0,0,2,3)`. Its cohomology has dimension two and Gram
`diag(2,3)`. An acyclic control has `ker Q=im d` and zero cohomology despite
vacuous positivity. A second control has one nonzero class with negative
pairing. Therefore nonzero, well-defined and positive are three distinct
checks. The producer passes `12/12`; the hostile probe rejects `11/11`
mutations.
