---
artifact_type: exploration
status: active_research
doc_type: representation_bridge_candidate
created: 2026-08-31
title: "Split naturality and Burnside correspondence composition"
target_claim: "INTERNAL — supplied split corrections have exact dependence/naturality laws and restriction companions compose bilinearly; verdict: CONSTRUCTED at exact algebraic/categorical grade, not source-owned or physical"
source_claims: [SC-FER-04, SC-FER-05, SC-FER-07, SC-GEN-51, SC-GEN-52]
canon_verdict_change: none
scripts:
  - tests/channel-swings/source_native_corrected_observation_naturality_probe.py
  - tests/W99_theorem_finite_instances.py
lean:
  - Lean/GUFormalization/SourceNativeCorrectedObservationNaturality.lean
  - Lean/GUFormalization/GroupActionBurnsideSpanCorrespondenceComposition.lean
---

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.
>
> Classification: `SOURCE_NATIVE_ROUTE`.

```gu-typed-objects
result: exact split-dependence/naturality laws and additive composition of restriction companions
carrier: abstract observed module B plus finite supplied-action Burnside objects LAYER=observed+toy BRIDGE=typed-product-of-independent-packets CHIRALITY=S-CHIRALITY-UNTYPED
pairing: NONE
real_structure: UNTYPED; no scalar-antilinear or Krein structure is used or inferred
grading: observed gamma kernel/trace complement plus group-change categorical level; no physical family grading
action_owner: repository-construction -- source/action/dynamics ownership remains open
target: corrected kernel projector and iterated restriction correspondence MAP-TYPE=intertwiner
```

# Split naturality and Burnside correspondence composition

## Result

Two independent proof-stable interfaces are now exact.

First, the corrected observation projector

```text
P_j = 1 - j Gamma
```

remembers the supplied right inverse. For any two trace insertions `j1,j2`,

```text
P_j1 - P_j2 = (j2 - j1) Gamma.
```

If `Gamma j1 = 1`, then `P_j1 = P_j2` if and only if `j1 = j2`. Thus the
common gamma kernel does not by itself select a complement. A carrier map
intertwines two corrected projectors exactly under the supplied contraction
and split squares; corrected observations then obey the corresponding
naturality law.

Second, for group homomorphisms `H -> K -> L`, elements

```text
x in Hom_H(A, Res B),
y in Hom_K(B, Res C)
```

compose as

```text
x ; Res(y) in Hom_H(A, Res(Res C)).
```

Lean proves additivity in both inputs, zero laws, compatibility with the
outer left/right span actions, and graph-generator composition.

## Preflight and route selection

Object-level retrieval covered right inverses, split exact sequences,
projector dependence, contraction/split intertwiners, restriction companions,
profunctor/biset composition, graph spans and full Mackey coherence. The
repository already contained the one-split projector and the uncomposed
correspondence. It did not contain the equality/naturality criterion or the
composition law proved here.

The structural linear-algebra and category routes dominate a broad numerical
search: each gate is an identity from supplied maps. Computation is bounded to
independent finite controls that distinguish correct composition from hostile
entrywise pairing and contraction-only naturality from contraction-plus-split
naturality.

## Independent controls

The split probe passes `6/6` exact checks. It supplies two different right
inverses of the same contraction, verifies the projector-difference identity,
confirms both projectors land in and fix the same kernel, and rejects a map
that commutes with contraction but not with the chosen split.

W99 independently models completed spans by integer multiplicity matrices. It
checks bilinearity of correspondence composition, outer-action associativity,
graph-relation composition, and rejects hostile entrywise multiplication.

## Hostile review and claim ceiling

**Strongest overclaim.** Naturality under a supplied split square does not
select that square. It proves that a source-owned intertwiner would be enough;
it does not prove one exists or that the source/action chooses either split.

**Strongest contrary construction.** A physical constraint/BV complex or
boundary domain may select a different complement or only a quotient class.
That can replace this algebraic projector without contradicting any theorem.

**Weakest seam.** Correspondence composition is iterated restriction followed
by categorical composition. No coend universal property, induction functor,
bicategory classification, ambidexterity, or full Mackey 2-functor coherence
has been established.

No source action, family covector, `54`/`210` coefficient, physical quotient,
observed family, chirality, mass, generation count, scale, observable,
prediction, canon verdict, paper/release posture, or GU verdict moves.
