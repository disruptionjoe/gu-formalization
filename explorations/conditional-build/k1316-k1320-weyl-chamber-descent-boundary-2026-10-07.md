---
title: "K1316--K1320 Weyl-chamber descent boundary"
status: active_research
doc_type: conditional_research_result
created: "2026-10-07"
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
claim_effect: none
---

# K1316--K1320 Weyl-chamber descent boundary

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `SOURCE_NATIVE_ROUTE` only for the SC-META-53 positivity
question and `INTERNAL_STRUCTURAL_ONLY` for the finite chamber averaging,
equivariance criterion, Coxeter transport and projective-holonomy control.

Scope: the `322560` normalized principal-series Hilbert controls constructed
chamberwise in K1311--K1314 for one imported regular split charge. This packet
tests whether their raw direct-sum multiplicity can be removed canonically and
what additional data are required for the result to carry a common `G` action.
It neither derives the charge nor selects a chamber.

```gu-typed-objects
result: canonical finite chamber-average projection, exact G-equivariance criterion, D7 Coxeter-flat transport criterion and projective-relator countercontrol
carrier: direct sum over the W(D7) chamber torsor of compact-picture L2(K/M) fibers LAYER=toy CHIRALITY=N/A
pairing: positive direct-sum Hilbert pairing and its coherent-diagonal restriction ON=chamber_sum
real_structure: real split-D7 chamber torsor with complex unitary Hilbert fibers
grading: ungraded chamber index plus D7 Coxeter word length
action_owner: repository-construction -- finite-Hilbert construction after imported chamberwise principal-series controls
target: whether raw chamber multiplicity admits exact chamber-blind G descent without being confused with source or physical chamber selection MAP-TYPE=not-a-map
```

## Preflight bookend

The current target head contains no newer source action, boundary or Green law.
K1314 already proves positivity in every chamber and explicitly leaves a
normalized Weyl-intertwiner completion open. The cheapest route-changing
question is therefore not another chamber enumeration but the descent
condition itself. Functional analysis supplies the finite orthogonal average;
representation theory asks when that range is `G`-invariant; Coxeter theory
reduces path independence to simple-edge relators; and the hostile lens asks
whether unitary edge maps can still carry nontrivial relator phase. The claim
ceiling is mathematical chamber descent only. Source selection, physical
cohomology and GU positivity remain separately typed.

## K1316: the finite chamber index has a canonical orthogonal average

After declaring unitary identifications `U_C:H_0 -> H_C`, define

```text
J(v)=(U_C v)_C,
P=(1/|W|) J J*.
```

On the direct sum of all chamber fibers, `P` is self-adjoint, idempotent,
positive and norm one. Its range is the coherent diagonal
`{(U_C v)_C}`. Thus the raw chamber-index factor is reduced from the regular
`|W|=322560` multiplicity to rank one. This is canonical finite Hilbert linear
algebra relative to the declared identifications. It does not yet say that the
coherent diagonal is preserved by the block principal-series action.

## K1317: averaging descends `G` exactly when transported actions agree

Let

```text
Pi(g)=direct-sum_C pi_C(g),
rho_C(g)=U_C* pi_C(g) U_C.
```

Then the coherent diagonal is `Pi(g)`-invariant exactly when `rho_C(g)` is
independent of `C` for every `g`. Equivalently,

```text
[P,Pi(g)]=0  for every g.
```

Necessity follows by applying `Pi(g)` to every diagonal vector; sufficiency
follows by defining the common action `rho(g)`. Hence chamberwise positivity,
unitarity and abstract isomorphism are insufficient. The chosen `U_C` must be
actual coherent `G` intertwiners.

## K1318: D7 coherence reduces to simple edges and Coxeter relators

For the D7 simple reflections with edges

```text
(1,2),(2,3),(3,4),(4,5),(5,6),(5,7),
```

unitary adjacent-chamber transports extend path-independently to all chambers
when they satisfy

```text
T_i^2=I,
T_i T_j=T_j T_i                   when m_ij=2,
T_i T_j T_i=T_j T_i T_j           when m_ij=3.
```

These are the D7 Coxeter relations, so they define a coherent unitary action
of `W(D7)` and make transport independent of reduced word. If every simple
transport also intertwines the adjacent principal-series `G` actions, K1317
then gives the chamber-blind descended action. This is a complete finite
coherence criterion, not a construction of analytic normalized intertwining
operators or their pole/reducibility control at the imported charge.

## K1319: unitary edge maps can retain projective braid holonomy

The standard D7 reflection matrices give an exact orthogonal realization.
Twist the adjacent generators at the branch edge by

```text
T_5'=T_5,
T_6'=-T_6.
```

Both remain unitary involutions, but the `m_56=3` words obey

```text
T_5' T_6' T_5' = -(T_6' T_5' T_6').
```

Thus the braid holds only projectively and the two paths have relative phase
`-1`. Positive fibers and unitary edge maps do not trivialize this holonomy.
Exact chamber descent requires the normalized analytic family to kill every
relator phase, not merely to identify neighboring representations up to a
scalar.

## K1320: the chamber average advances mathematics, not physical admission

The integrated census now has eighteen rows: seven satisfied, three excluded,
two conditional and six missing. The new satisfied row is the finite
orthogonal chamber-average projection. Exact `G`-equivariant descent remains
conditional on an analytic normalized intertwiner family satisfying the D7
relations with trivial relator phase. The finite polarized-BFV compatibility
row also remains conditional. Source ownership of charge/chamber, interacting
constraints, a common local BV-BFV domain, causal Green/boundary data, positive
nonzero physical cohomology and observed export remain missing.

## Postflight hostile review

The strongest overclaim is to call the rank-one chamber-index average a
canonical physical sector. K1317 blocks that inference unless the projection
commutes with the complete block `G` action. The strongest contrary
construction is K1319: every edge map can remain a positive unitary
identification while one braid loop carries phase `-1`. The weakest
reproducibility seam is the Coxeter presentation; the executable certificates
independently verify the D7 generators, involutions, six adjacent braids,
nonadjacent commutations, projection identities, commutator criterion and the
twisted phase countercontrol.

K1145/K1150 remain `0/7`; SC-ACT-01/02/06 remain `ASSERTS`, SC-META-53
remains `UNCERTAIN`, and LT-SM8/LT-GR6b/RA-F1/AC-F1 remain `NEEDS`. No
source, ledger, canon, paper, prediction, confirmation or public status moves.

## Exact next input

For mathematical chamber descent, supply a pinned analytic normalized
intertwiner family on the imported regular imaginary split charge, including
its domain, poles/reducibility behavior and exact D7 braid normalization. For
physical admission, independently supply a released source action, boundary
or Green law deriving the charge and chamber data together with the local
interacting BV-BFV domain, causal evolution, conserved positive physical
cohomology and observed state map. The finite chamber average does not replace
either input.
