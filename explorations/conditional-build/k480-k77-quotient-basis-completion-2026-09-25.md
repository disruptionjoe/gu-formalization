---
title: "K480 — K77 Quotient-Basis Exactness Completion"
status: active_research
status_axis: operational_state
doc_type: conditional_action_quotient_basis_completion
created: 2026-09-25
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# K480 — K77 quotient-basis exactness completion

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: BRIDGE_OR_SEMANTIC_BOUNDARY.

```gu-typed-objects
result: quotient-basis construction and iff criterion for an exact three-term complex
carrier: finite C2_to_C1_to_C0 complex after a full-column D2 is supplied LAYER=toy CHIRALITY=N/A
pairing: exact rational linear algebra ON=k77_corrected_trace_domain_complex
real_structure: rational control only; source-native real coefficients absent
grading: homological degrees 2,1,0
action_owner: N/A until a source-authenticated action supplies D2 and the physical domain
target: acyclic completion by a descended quotient isomorphism MAP-TYPE=not-a-map
```

## Theorem and construction

If `D2` has full column rank, nilpotence makes `D1` descend to
`C1/im(D2)`. Under Euler zero, this quotient and `C0` have equal dimension;
the complex is acyclic exactly when the descended map is an isomorphism.

Choose a row basis `L` for the annihilator of `im(D2)` and any invertible
matrix `A`. Then `D1=A L` annihilates `D2` and induces an isomorphism on the
quotient. The exact `2 -> 4 -> 2` control has ranks `(2,2)` and zero homology;
lowering the second rank to one yields homology `(0,1,1)`.

For the K77 dimensions, a full-rank `D2` would leave quotient dimension
`46592-10752=35840`, exactly the required `D1` rank. This is a construction
interface, not evidence that the source action supplies either map.

## Bookends

The strongest advance is an explicit exactness parameterization after `D2`
exists. The strongest overclaim is that repository construction selects the
GU action. The rank-defect control is the strongest contrary case. The
weakest seam is the still-absent physical domain and owner-authenticated `D2`.

No native coefficients, properness or physical cohomology is emitted.

## Reproduction

```bash
python3 tests/channel-swings/k480_k77_quotient_basis_completion.py
python3 tests/channel-swings/k480_k77_quotient_basis_completion_probe.py
```
