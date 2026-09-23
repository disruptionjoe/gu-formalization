---
artifact_type: exploration
status: exploration
doc_type: representation_bridge_candidate
created: 2026-09-23
title: "When the corrected observation projector is a gauge slice"
target_claim: "INTERNAL — exact necessary-and-sufficient gauge-image and Green-adjoint conditions for giving the corrected observed Clifford projector physical representative meaning; current K77 owners do not yet compose on one typed carrier"
source_claims: [SC-GEN-02, SC-GEN-03, SC-GEN-51, SC-GEN-54, SC-CHI-01, SC-CHI-51]
canon_verdict_change: none
probe: tests/channel-swings/corrected_observation_gauge_slice_green_compatibility.py
hostile_probe: tests/channel-swings/corrected_observation_gauge_slice_green_compatibility_probe.py
---

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

```gu-typed-objects
result: CORRECTED-OBSERVATION-GAUGE-SLICE-GREEN-COMPATIBILITY
carrier: abstract observed one-form-spinor module B with Gamma_B:B->S and supplied right inverse j_B:S->B; existing K77 equation-dual, distortion-orbit and boundary carriers remain separately typed LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: a separately supplied nondegenerate real or Krein Green form H on B; no current source/action-owned H on this same carrier is identified ON=conditional observed carrier B
real_structure: UNTYPED; the exact rational controls use a real finite model only to prove independence of split and Green-adjoint conditions
grading: ker(Gamma_B) versus trace-lift complement im(j_B); no family, chirality, mass or physical grading is assigned
action_owner: repository-construction -- repository theorem owns the slice criterion; existing K77 action/BFV/Green artifacts own other declared carriers; the cross-carrier intertwiner and image equality remain open
target: necessary-and-sufficient criterion for P_B=1-j_B Gamma_B to select representatives of an action gauge quotient and be Green-compatible MAP-TYPE=projection
```

# When the corrected observation projector is a gauge slice

## Decision question

The existing corrected observation

```text
P_B = 1_B - j_B Gamma_B,
Gamma_B j_B = 1_S
```

lands exactly in the observed Clifford kernel. That fact alone does not say
that `P_B` selects representatives of an action-owned gauge quotient. The
decision question is the smallest one that can make that interpretation
honest: what must an action gauge image and Green pairing satisfy for this
specific algebraic correction to become their physical slice?

This question is downstream of the literal-observation obstruction and the
corrected-projector construction. It does not reopen either result. It tests
the missing ownership seam behind RA-F1/RA-D4/AC-F1 while preserving the
source's non-chiral total theory and `2+1` claim as open source mechanisms.

## Exact slice theorem

Let `Gamma:B->S` be linear, let `j:S->B` obey `Gamma j=1`, and put
`P=1-j Gamma`. Then

```text
im(P)  = ker(Gamma),
ker(P) = im(j).
```

The first equality is the already-owned corrected-kernel result. For the
second, `P(j s)=0`; conversely `P(b)=0` implies `b=j Gamma(b)`.

Now let `G` be the action-owned gauge or constraint image in `B`. The map `P`
is constant on `G`-cosets exactly when

```text
P(G)=0  iff  G is contained in im(j).
```

If `Gamma|_G:G->S` is an isomorphism—the full trace-sized case—then containment
forces equality:

```text
G = im(j).
```

That equality is the exact missing physical-slice condition. Idempotence,
equal rank, gauge covariance on another carrier, or the existence of some
right inverse cannot substitute for it.

## Green compatibility is independent

Let `H` be a nondegenerate real or Krein Green form on `B`. Orthogonal or
Krein-adjoint representative selection additionally requires

```text
P^dagger_H = P,
```

equivalently that `j Gamma` be `H`-self-adjoint. The split law
`Gamma j=1` does not imply this.

The exact rational fixture makes the independence explicit. With
`Gamma=[1,0,0]`, both

```text
j_0(s)=(s,0,0),
j_1(s)=(s,s,0)
```

are right inverses. Their projectors are both idempotent and have image
`ker Gamma`. Under the Euclidean Green form, the first is self-adjoint and the
second is oblique and non-self-adjoint. A different proposed gauge generator
`(1,0,1)` also survives the first projector, so a same-dimensional gauge image
is not silently its trace-lift kernel.

The producer certifies these statements with exact rational arithmetic. The
independent replay passes ten controls and rejects thirteen hostile mutations.

## Typed owner audit

Object-level retrieval found several nearby K77 constructions, but no current
same-carrier composition:

| object | owned result | mismatch that remains |
| --- | --- | --- |
| Corrected Clifford projector | `P_B` on the observed one-form-spinor `B` | action gauge image, Green form and common domain not owned on `B` |
| K77 co-moving no-leakage projector | exact descent on the complete value-plus-first-jet equation dual | no intertwiner to `B`; killed image not proved equal to `im(j_B)` |
| K77 complete `4+10` receiver | detects the ten conormal equation components missed by ordinary pullback | source-derived conormal constraint/BV quotient and Clifford-trace identification absent |
| Propagated zero-order trace line | unique natural `2 Gamma(zeta)-nu` constraint | retained rank-128 Jordan image kills this zero-order route; it is not BV or quotient data |
| Frozen K77 BFV image | exact rank-70 distortion-orbit gauge image with 21-dimensional stabilizer | different configuration carrier; physical cohomology and map to `im(j_B)` absent |
| K77 boundary Green comparator | exact 3860-dimensional preboundary form and conditional Lagrangian graphs | moving reality/domain unselected; no compatibility theorem with `P_B` |

The August 8 no-leakage projector is therefore prior art on a different
equation-dual carrier, not the requested ownership proof for the August 31
Clifford correction. The correct next object is a typed map `iota` from `B`
into the selected K77 equation or field complex satisfying all three:

```text
iota P_B = P_K77 iota,
iota(im j_B) = im(d_action) or the named constraint image,
the selected Green-domain adjoint makes the induced slice representative-independent.
```

## Hostile review

**Strongest overclaim.** The theorem does not say that no physical corrected
observation exists. It gives the exact criterion one must prove and shows that
the currently named artifacts do not already prove it.

**Strongest contrary construction.** A future action-derived right inverse
whose trace lift equals the gauge image, or a source-owned observation
intertwiner into the K77 complete receiver, could satisfy the criterion. The
current result is designed to accept that construction.

**Strongest mistyping risk.** The K77 equation-dual no-leakage projector and
`P_B` are both projectors, but that shared noun is not a carrier map. Their
direct identification is forbidden until `iota` is supplied.

**Weakest reproducibility seam.** The finite rational fixture proves that the
right-inverse and Green conditions are logically independent, not that the
actual K77 Green form is Euclidean. The general slice identities are proved in
the displayed algebra; the physical Green signature and domain remain open.

## Effect and next condition

The tempting direct-composition shortcut is killed. The corrected algebraic
kernel survives unchanged, and the exact physicalization burden is smaller and
better typed: identify the action-owned same-carrier bridge, prove gauge-image
equality with `im(j_B)`, and then prove Green/domain compatibility.

No source polarity, physics-ledger verdict, canon, paper status, family or
chirality interpretation, residual-vector realization, public posture or GU
verdict changes.
