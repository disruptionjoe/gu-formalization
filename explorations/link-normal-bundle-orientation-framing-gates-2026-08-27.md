---
title: "Dimension-13 link D1-D3: the RP3 spine is an untwisted stably framed product model; the global link is conditional"
status: exploration
doc_type: determination
created: "2026-08-27"
grade: "EXACT CHARACTERISTIC-CLASS COMPUTATION ON THE FILED NORMAL MODEL; GLOBAL NORMAL IDENTIFICATION AND FRAMING REMAIN CONDITIONAL"
scripts:
  - tests/dim13/link_normal_bundle_orientation_framing_probe.py
target_claim: "DIM13-LINK-O3 / M-H5"
target_claim_verdict: "FIXED-SPINE_PASS_GLOBAL-FRAMING_CONDITIONAL"
comparator_classification: INTERNAL_STRUCTURAL_ONLY
canon_verdict_change: none
---

# Dimension-13 link D1-D3

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`

```gu-typed-objects
result: D1-D3 normal-bundle orientation and first stable-framing obstruction calculation
carrier: sphere bundle of the filed normal model over the RP3 spine and conditional P(TX) extension LAYER=ambient CHIRALITY=N/A
pairing: characteristic classes ON=normal and stable tangent bundles
real_structure: real rank-7 normal bundle
grading: cohomological degree over F2 and free-rational degree four
action_owner: repository-construction -- global GU end geometry remains unbuilt
target: fixed-spine product typing and global stable-framing obstruction MAP-TYPE=pullback
```

Scope: the unconditional result binds the fixed `RP3` spine and the normal model
`nu = R + Sym^2(Q*)`. The global formulas are conditional on extending that
normal identification over `P(TX)`. Neither result constructs the global GU end,
a Pontryagin--Thom class or an integer count.

## D1 — normal bundle on the spine

Let `l` be the tautological line on `RP3` and `Q` the rank-three quotient in
`R^4 = l + Q`. Then

```text
w(Q) = (1+a)^(-1) = 1+a+a^2+a^3.
```

Under the splitting principle, `Sym^2(Q)` has three zero weights and the three
off-diagonal weights `x+y`, `x+z`, `y+z`. Exact expansion gives

```text
w1(Sym^2 Q) = 0,
w2(Sym^2 Q) = w1(Q)^2 + w2(Q),
w3(Sym^2 Q) = w1(Q)w2(Q) + w3(Q).
```

Substituting `w_i(Q)=a^i` makes all three classes zero. Thus the filed
`nu = R + Sym^2(Q*)` has rank seven and `w1=w2=w3=0`. In the stable range over
a three-complex, this makes `nu` trivial. Its unit sphere bundle is therefore
noncanonically

```text
S(nu) = RP3 x S6
```

on the fixed spine. This verifies the model used by the receptacle packet; it
does not identify the unbuilt global link with that product.

## D2 — orientation row

For rank-three `Q`,

```text
w1(Sym^2 Q) = 4 w1(Q) = 0.
```

So the `S6` row is untwisted in either base-orientation convention. Moreover,
for rank-four `TX`, the relative tangent of `P(TX)` satisfies

```text
w1(T_rel) = pi*w1(TX),
w1(TP(TX)) = w1(T_rel) + pi*w1(TX) = 0.
```

The fixed-spine product consequently has the ordinary mod-three top class in
degree nine. The twisted branch of the preregistration does not occur for this
normal model.

## D3 — framing: product pass, global condition

The model is stably parallelizable: `RP3` is parallelizable and
`TS6 + R` is trivial. For the conditional global link `L=S(nu)` over
`B=P(TX)`, the sphere-bundle tangent identity is

```text
TL + R = pullback(TB + nu).
```

The first stable obstructions simplify to

```text
w2(TB + nu) = pi*w2(TX),
p1(TB + nu) = 7 pi*p1(TX)
```

on the free/rational degree-four part. The coefficient `7=1+1+5` comes from
`TX`, the relative `l* tensor Q` term and `Sym^2(Q)` respectively; the last
factor follows from the rank-three weights `0,+/-x` becoming
`0,0,+/-x,+/-2x`.

Therefore a nonzero pulled-back `w2(TX)` or `7p1(TX)` obstructs a global stable
framing. Their vanishing is necessary, not sufficient: the normal
identification, higher/torsion KO data and an actual global framing remain
unbuilt. D3 advances the route to an exact conditional obstruction formula; it
does not fire the route-wide K2 predicate on unspecified `TX`.

## Verification and next condition

`python3 tests/dim13/link_normal_bundle_orientation_framing_probe.py
--selftest` passes `20/20` checks and catches `4/4` planted mutations. M-H5
remains live for the reflection/spin/horizontal-distribution lemma and the full
base eta-form integral. The dim-13 route next needs either the actual global
`TX`/normal packet to evaluate the obstruction formulas or the separately
preregistered D4 reframing-orbit computation.
