---
title: "K484 — K77 Modular Invertibility Witness"
status: active_research
status_axis: operational_state
doc_type: conditional_action_modular_invertibility_witness
created: 2026-09-25
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# K484 — K77 modular invertibility witness

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
result: finite-field witness for rational square-concatenation invertibility
carrier: denominator-cleared finite rational matrix LAYER=toy CHIRALITY=N/A
pairing: exact determinant arithmetic ON=k77_square_exactness_certificate
real_structure: rational coefficients reduced modulo a declared prime
grading: inherited homological block order
action_owner: N/A until a source-authenticated action supplies the rational matrix and domain
target: nonzero determinant witness for K483 MAP-TYPE=not-a-map
```

## Theorem

Clear a rational square matrix with one common positive denominator. If its
integer determinant is nonzero modulo any prime, then it is nonzero over the
integers and the original rational matrix is invertible. A zero modular
determinant is inconclusive.

The exact control has denominator LCM `6`, rational determinant `1/6`, and
cleared determinant `216`; modulo `5` the witness is `1`. Combined with K483's
separate nilpotence and Euler-zero hypotheses, this provides a scalable exact
certificate without expanding a 46,592-square rational determinant.

## Bookends

The advance is one-sided exact certification, not probabilistic evidence. The
strongest contrary case is a prime dividing a nonzero determinant: it returns
zero and is correctly inconclusive. The weak seam is exact denominator
clearing and provenance of the supplied action matrix.

No nilpotence, action ownership, physical domain, properness or cohomology is
supplied by the modular witness.

## Reproduction

```bash
python3 tests/channel-swings/k484_k77_modular_invertibility_witness.py
python3 tests/channel-swings/k484_k77_modular_invertibility_witness_probe.py
```
