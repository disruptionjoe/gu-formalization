---
title: "K483 — K77 Square-Determinant Exactness Certificate"
status: active_research
status_axis: operational_state
doc_type: conditional_action_square_determinant_exactness
created: 2026-09-25
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# K483 — K77 square-determinant exactness certificate

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
result: square-concatenation determinant criterion for an exact three-term complex
carrier: finite C2_to_C1_to_C0 rational complex LAYER=toy CHIRALITY=N/A
pairing: standard rational dot pairing used only for the transpose certificate ON=k77_corrected_trace_domain_complex
real_structure: rational control; source-native real coefficients absent
grading: homological degrees 2,1,0
action_owner: N/A until a source-authenticated action supplies both maps and the physical domain
target: acyclicity certificate [D2,D1^T] MAP-TYPE=not-a-map
```

## Theorem

Assume `dim C1 = dim C2 + dim C0` and `D1 D2=0`. The complex is acyclic iff
the square concatenation `[D2,D1^T]` is invertible. Nilpotence makes its two
column spaces orthogonal; invertibility then gives the two full ranks forced
by exactness, and exactness conversely supplies complementary full-rank spaces.

The `2 -> 4 -> 2` exact control has determinant `1`. A rank-defect control has
determinant zero. A separate full-rank, invertible-concatenation control with
`D1 D2 != 0` is rejected, proving the determinant never replaces nilpotence.
For K77 the square would have size `46592`.

## Bookends

The advance is a basis-free exactness certificate that avoids constructing a
quotient basis. The strongest overclaim is determinant-only acyclicity; the
non-nilpotent control rejects it. The weak seam remains the absent physical
domain and action-owned matrices.

No native K77 matrix, properness or physical cohomology is emitted.

## Reproduction

```bash
python3 tests/channel-swings/k483_k77_square_determinant_exactness.py
python3 tests/channel-swings/k483_k77_square_determinant_exactness_probe.py
```
