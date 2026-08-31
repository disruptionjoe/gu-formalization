---
artifact_type: exploration
status: active_research
doc_type: action_observation_complex_certificate
created: 2026-08-31
title: "Source-native action--observation weld and the smallest physical-candidate complex"
target_claim: "INTERNAL — a supplied three-stage action complex and supplied split-corrected observation descend to cycle/gauge-equivalence classes under two exact compatibility laws; the frozen source packet selects neither the action member nor the split, so no source-selected physical state space follows"
source_claims: [SC-ACT-01, SC-ACT-03, SC-ACT-04, SC-ACT-05, SC-ACT-06, SC-GEO-57]
canon_verdict_change: none
scripts:
  - tests/channel-swings/source_native_action_observation_complex_probe.py
lean:
  - Lean/GUFormalization/SourceNativeActionObservationComplex.lean
---

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders conventional BRST/BV and physical-state language. Any result about
> the independent B5 `(9,5)` Rarita--Schwinger complex, a standard gauge
> quotient, positive Hilbert completion, or familiar particle interpretation
> binds only that named construction. It is not evidence for Weinstein's
> source-native `(7,7)` dynamics without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.
>
> Classification: `SOURCE_NATIVE_ROUTE` at conditional interface grade.

```gu-typed-objects
result: exact three-stage action-complex and corrected-observation descent interface, plus packet-relative action nonselection theorem
carrier: supplied gauge, field and equation modules with supplied linear differentials LAYER=UNTYPED CHIRALITY=S-CHIRALITY-UNTYPED
pairing: NONE
real_structure: UNTYPED
grading: three stages gauge -> field -> equation; candidate middle cohomology is cycles modulo gauge images
action_owner: UNTYPED; supplied mathematical datum only, with the physical action owner unconstructed
target: quotient of the middle cycle subtype by gauge images and its induced corrected-observation map MAP-TYPE=quotient
```

# Result

The smallest honest quotient-bearing complex available from the released
grammar is

```text
C0(gauge) --d0--> C1(field) --d1--> C2(equation),
                         d1 d0 = 0.
```

Lean now packages this as `ThreeStageComplex`. A middle-stage cycle is a field
in `ker d1`; two fields are cohomologous when they differ by `d0 g`. Every
gauge image is a cycle. A `ChainMap` consists of maps at all three stages and
the two commuting squares. It provably maps cycles to cycles and respects
gauge equivalence, which is the representative-level condition required for
an induced map on the middle quotient. Lean also proves reflexivity, symmetry
and transitivity of that relation, constructs `CandidateCohomology` as the
actual quotient, and defines the induced map on quotient classes.

An immediate independent review caught and repaired an important first-version
typing error: the original `CandidateCohomology` declaration quotiented the
whole field carrier by gauge images, even though the prose called it cycles
modulo gauge images. The repaired definition first forms the subtype
`{x // d1 x = 0}` and quotients only that subtype. A chain map now explicitly
restricts to this cycle carrier before `Quotient.map` is formed. The planted
finite control includes a noncycle field and rejects its admission as a class
representative. No downstream physical claim was promoted during the repair.

For an observed Clifford contraction `Gamma`, supplied right inverse `j`, and
projector

```text
P_j = 1 - j Gamma,
```

the corrected middle observation is `P_j f1`. It becomes a chain map under
exactly the two declared weld conditions

```text
P_j d0_obs = d0_obs,             d1_obs P_j = d1_obs.
```

The first says the projector fixes observed gauge images. The second says the
observed equation map is insensitive to the removed trace direction. Under
these laws the corrected map sends action cycles to observed cycles, respects
gauge-equivalent representatives, and has gamma-traceless output. This is the
action--observation weld.

# What the coefficient kill test decides

The frozen packet `lab/sources/source-coefficient-packet-v0.1.yaml` is a
content-hash-pinned projection of thirteen already-ratified source-ledger rows.
It is not a transcript cache or a second evidence ledger. Its strict
coefficient matrix has rank zero. Adding the separately labeled family-copy
exchange equations gives rank two and still leaves two independent owner
coordinates, `d54` and `d210`.

The new Lean theorem composes that result with an arbitrary proposed action
family. If the map from the two owner coefficients to action objects is
injective, the distinct `54` and `210` axis solutions instantiate distinct
actions while both satisfy the strict source constraint. Therefore the frozen
packet does not select a unique action complex. A later source edition or a
separately owned action equation can change this conclusion only by minting a
new packet and closing the surviving coefficient kernel.

Independently, prior Lean work proves that a split-surjective contraction's
projector remembers the entire supplied right inverse. Different splittings
give different projectors. The exact probe exhibits two right inverses with
the same gamma kernel and two different, chain-compatible corrected maps.
Thus even after a complex is supplied, the current source packet does not
select the observation correction.

# Why Mathlib is used, and why not more of it

Mathlib is the right substrate here. The proof uses its exact `LinearMap`
composition laws, kernels, ranges, modules and quotient-compatible algebra.
Those primitives remove implementation risk and keep theorem statements
interoperable with later formal work.

A full Mathlib `HomologicalComplex` is not the efficient object for this gate.
The live obligation has exactly three stages, two arrows, and two observation
squares, while ownership of the action and split must stay visible in the
types. A generic category-indexed complex would add indexing and categorical
machinery without closing any scientific premise. Promotion to
`HomologicalComplex` becomes worthwhile if a source-owned longer BV/KT
sequence, functorial family of complexes, spectral sequence, or derived
comparison actually appears. The present local structure is deliberately the
smallest reusable formal interface, not a substitute for Mathlib.

# Exact controls

`tests/channel-swings/source_native_action_observation_complex_probe.py` uses
exact rational matrices. Its baseline checks the square-zero law, two genuine
right inverses, distinct idempotent projectors with one common gamma kernel,
both weld conditions, cycle preservation, gauge-equivalence preservation,
gamma-traceless corrected output, strict-source rank zero, distinct owner
axes, theorem inventory, and the claim ceiling. Its selftest plants broken
chain composition, a false right inverse, collapsed split choice, invented
source rank, collapsed owner axes, a missing Lean artifact, and a missing
claim ceiling. Crashes are not counted as catches.

# Claim ceiling

This is a **conditional physical-candidate complex**, meaning only that it has
the algebraic shape needed for a middle gauge quotient and a corrected
observation map that can descend to it. It is not a source-selected physical
complex.

Not constructed or selected:

- the complete source action or a unique `54:210` coefficient packet;
- a source-owned gauge/BV/Koszul--Tate differential on the K77 carrier;
- a source-selected Clifford splitting or observation projector;
- nonlinear closure, analytic domains, boundary conditions, closed ranges or
  Fredholm properties;
- a real/Krein completion, positive physical Hilbert space, probability rule,
  quantum measure or observable algebra;
- an observed family sector, chirality, mass, generation count, prediction or
  GU verdict.

The independent B5 `(9,5)` complex is not transferred. SC-GEO-57's
two-connection complex remains unreleased and transcription-uncertain; this
result does not reconstruct its operator matrix, order or cyclicity.

# Smallest next physical gate

The next efficient reopener is not more abstract homological machinery. It is
one source- or action-owned instantiation packet supplying all of:

1. the concrete K77 gauge, field and equation carriers;
2. both differentials and the exact Noether/square-zero identity;
3. a named observation map and right inverse satisfying the two weld laws;
4. a real/Krein pairing and common analytic domain if “physical” is meant in
   the state-space sense; and
5. a coefficient equation that closes the surviving two-owner kernel, or an
   explicit declaration that the family remains parameterized.

Until that packet exists, the most rigorous result is the conditional descent
theorem plus the exact nonselection certificate proved here.
