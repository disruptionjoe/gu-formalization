---
title: "K475 — K77 Acyclic Rank Profile"
status: active_research
status_axis: operational_state
doc_type: conditional_finite_complex_rank_necessity
created: 2026-09-25
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# K475 — K77 acyclic rank profile

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
result: unique acyclic differential-rank profile for the finite corrected-boundary K77 three-term complex
carrier: repository control of the homogeneous-orbit complex C2 to C1 to C0 of dimensions 10752,46592,35840 LAYER=toy CHIRALITY=N/A
pairing: finite exact rank pairing only; no physical state pairing ON=k77_three_term_control
real_structure: inherited corrected trace-half real carrier
grading: homological degrees 2,1,0
action_owner: N/A; dimensions and ranks do not provide action coefficients
target: necessary finite properness rank profile MAP-TYPE=not-a-map
```

## Theorem and K77 specialization

For `C2 --D2--> C1 --D1--> C0`, with dimensions `(n2,n1,n0)` and ranks
`(r2,r1)`, nilpotence gives

```text
dim H2=n2-r2,
dim H1=n1-r2-r1,
dim H0=n0-r1.
```

Acyclicity therefore forces the unique recurrence

```text
r2=n2,
r1=n1-r2=n0.                                           (1)
```

In particular `n2-n1+n0=0` is necessary. For the K77 dimensions
`10752 -> 46592 -> 35840`, (1) yields exactly

```text
rank D2=10752, rank D1=35840.
```

This rederives K445's successful ranks from the dimensions rather than
hard-coding them. K446's defects then give `(0,70,70)` and `(21,21,0)` exactly.

## Bookends

The cheapest route is dimension/rank algebra before inspecting large matrices.
A nonzero Euler characteristic or wrong arrow rank rejects acyclicity
immediately. The strongest overclaim is that the required ranks construct the
action; they do not establish coefficients, nilpotence, domain preservation or
physical cohomology. An adapted contraction remains a sufficient alternative
witness, but any exact finite acyclic complex must still realize these ranks.

## Reproduction

```bash
python3 tests/channel-swings/k475_k77_acyclic_rank_profile.py
python3 tests/channel-swings/k475_k77_acyclic_rank_profile_probe.py
```
