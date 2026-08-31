---
artifact_type: exploration
doc_type: representation_coupling_classification
created: 2026-08-31
title: "The source-native adjoint/144 coupling exists cubically but its first Pati-Salam-preserving background channels are quadratic and unselected"
target_claim: "SC-PRE-52 / WG-P03 — representation-level coupling feasibility only; verdict: AVAILABLE cubic vertex, OBSTRUCTED linear Pati-Salam-preserving background, AVAILABLE but SOURCE-UNSELECTED quadratic 54/210 channels"
source_claims: [SC-PRE-52, SC-PRE-53, SC-FER-01, SC-OP-04, SC-FER-03, SC-ACT-01, SC-META-57]
canon_verdict_change: none
probe: tests/channel-swings/source_native_adjoint_144_coupling_probe.py
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
result: representation-grade degree ladder for paired-real family/144 couplings, including the linear Pati-Salam-background obstruction and the first quadratic owner split
carrier: real Cl(6,4) family spinor F_R paired from 16+ plus 16-, real gamma-kernel Z_R paired from 144+ plus 144-, and the source connection perturbation in Omega^1(Y,ad P) with internal adjoint A_R=so(6,4) LAYER=source-print CHIRALITY=S-FULL-DIRAC
pairing: conjugate-paired D5 invariant lines in F_R tensor Z_R tensor A_R and their symmetric or alternating quadratic-adjoint successors ON=the paired real representation carriers
real_structure: real Spin(6,4) conjugation exchanges the complex 16+/16- and 144+/144- halves and pairs the two complex cubic lines into the real coupling space
grading: polynomial degree in the tensorial adjoint insertion; degree 2 bare pairing, degree 3 one-adjoint vertex, degree 4 two-adjoint composite; no physical mass grading is assigned
action_owner: source-print owns the connection/operator grammar; repository-construction owns only representation-channel availability and obstruction; the actual form-leg contraction, coefficient and background remain source/action unowned
target: classify the lowest-degree invariant family/144 coupling and its Pati-Salam-preserving background refinement without selecting a family, mass or observable MAP-TYPE=intertwiner
```

# Source-native adjoint/144 coupling classification

## Result first

The strict lowest-degree nonzero invariant coupling is cubic: each same-label
complex product contains one adjoint,

```text
16+ tensor 144+  contains 45 once,
16- tensor 144-  contains 45 once,
```

and real conjugation pairs those two lines. Thus one source-compatible
adjoint interaction vertex is available at representation grade. The crossed
products contain no `45`, and the bare degree-two family/partner product
contains no scalar.

That positive result does **not** activate a Pati-Salam-preserving mixing:

```text
45 restricted to PS has no singlet.
```

The first such background channels occur at quadratic adjoint order. Exact
character decomposition gives

```text
Sym^2(45)    = 1 + 54 + 210 + 770,
Lambda^2(45)= 45 + 945.
```

Intersecting with `16 tensor 144 = 45+54+210+945+1050` and applying the held
Pati-Salam counts shows that the symmetric product supplies exactly the `54`
and `210`, each with one PS singlet, while the alternating product supplies
only `45` and `945`, both with zero PS singlets. The symmetric-versus-
alternating contraction of the source one-form legs is therefore load-bearing.

Both equivalent true-family copies have the same allowed representation
coupling space. Representation theory supplies neither a family covector nor a
relation between the independent `54` and `210` coefficients. This is a
feasibility theorem plus an exact missing-datum result, not a selected third-
family mechanism.

## Preflight and prior-art boundary

Object/mechanism retrieval was performed before calculation. HE-1 already
owned the complex `16/144` branching and Pati-Salam pairing ladder; Q5 owned
the five multiplicity-one D5 summands; HE-3 owned the cross-half placement and
family-row burden; HE-4 owned the PS counts `0,1,1,0,0` for
`45,54,210,945,1050`; the 2026-08-30 result supplied the paired real sectors
and obstructed their naive observation descent. None of those artifacts
composed the held facts into the source-native adjoint degree ladder.

The decisive route was intersection of exact decompositions. A broad matrix or
Clebsch search was dominated because the current question is availability and
multiplicity, not normalization. A conventional `126` VEV was rejected at
Layer 0: it is a different owner and is unnecessary for this classification.

## Typed degree ladder

Let `F_R` be the real 32-dimensional `Cl(6,4)` spin module and
`Z_R=ker Gamma` its real 288-dimensional gamma-kernel partner. Their
complexifications are the paired halves

```text
F_R complexified = 16+ + 16-,
Z_R complexified = 144+ + 144-.
```

Let `A_R=so(6,4)` be the real adjoint coefficient of the source tensorial
connection perturbation. The source field is actually an element of
`Omega^1(Y,ad P)`; the one-form leg is not discarded by this internal
classification.

| degree | internal channel | exact result | licensed reading |
|---|---|---|---|
| 2 | `F_R tensor Z_R` | no scalar | no bare invariant mixing |
| 3 | `F_R tensor Z_R tensor A_R` | one conjugate-paired adjoint line | invariant interaction vertex available |
| 3 plus PS background | nonzero `PS`-fixed vector in `A_R` | none | linear PS-preserving activation obstructed |
| 4 symmetric | `Sym^2(A_R)` | `54` and `210`, once each, each with one PS singlet | two conditional background owners available |
| 4 alternating | `Lambda^2(A_R)` | `45` and `945`, both with zero PS singlets | no PS-preserving owner |

The internal invariant does not prove that equation (9.16) contains the
corresponding tensorial insertion. The missing source/action datum must specify
the internal-`45` projection, barred/unbarred and half placement, one-form-leg
contraction, symmetric versus alternating quadratic product, real/Krein
coefficient relation, family covector, and nonzero stationary background or
interaction interpretation.

## Family comparison and conditional successor

If the source census supplies two equivalent true-family copies, each copy
tensors with the same real cubic line and the same two quadratic owner lines.
No representation invariant distinguishes one copy. With a larger family-copy
space, every owner line tensors with an arbitrary covector in its dual; the
allowed space still does not select a rank or a named family.

The conditional low-curvature effective-chirality successor therefore remains
deferred. This result supplies representation-compatible channels, but not the
coefficient-complete curvature-sensitive physical operator, domain, quotient,
or law needed to state its decoupling theorem without inventing dynamics.

## Hostile review

**Strongest overclaim.** “The source-native connection couples the third
family to the 144.” Refused. The result proves only channel availability; it
does not select a family, coefficient, background, action term, or observed
sector.

**Strongest contrary construction.** The actual fermion bilinear may use a
dualized Hom or Krein/C-real pairing whose form-leg and half placement differ
from the bare internal product. The degree ladder remains a representation
availability test, while source instantiation stays type-missing.

**Weakest reproducibility seam.** The symmetric/alternating adjoint squares are
now exact and executable, but no explicit Clebsch normalization is constructed.
That omission is harmless for multiplicity and PS-singlet availability and
becomes load-bearing as soon as an action coefficient or family-row relation is
claimed.

**Scope sentence.** This result binds the complexified D5 representation
channels paired by the established real `Spin(6,4)` structure and their
Pati-Salam restrictions. It does not bind a physical observed carrier, mass
operator, spectrum, scale, threshold, or empirical claim.

## Reproduction

```bash
PYTHONDONTWRITEBYTECODE=1 python3 tests/channel-swings/source_native_adjoint_144_coupling_probe.py --selftest
```

The probe recomputes the two adjoint squares from the exact 45-state weight
character, composes the banked Q5/HE-4 dependencies, checks conjugate and
wrong-half controls, and proves that corrupting the quadratic character or
planting a forbidden owner produces a genuine failing verification.
