---
title: "K77 source-observed kinetic-bridge rigidity wave"
status: active_research
doc_type: reverse_scaffold_source_observed_kinetic_bridge_rigidity_result
date: 2026-09-01
claim_ceiling: exact rigidity and interacting obstruction for local point transformations preserving fixed nondegenerate constant one-mode kinetic pairings; no full-carrier, variable-metric, derivative-dependent, nonlocal, background-dependent, orbit-averaged, singular or later-action no-go
manifest: lab/process/k77-source-observed-kinetic-bridge-rigidity-wave.json
probe: tests/channel-swings/k77_source_observed_kinetic_bridge_rigidity_probe.py
---

# K77 source-observed kinetic-bridge rigidity wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`

```gu-typed-objects
result: constant-kinetic local point-bridge rigidity and interacting potential obstruction
carrier: one real source augmented-torsion ray and one real observed massive quotient ray LAYER=conditional CHIRALITY=N/A
pairing: fixed nonzero constant one-mode kinetic coefficients kappa and mu ON=repository_owned_bridge_test
real_structure: real fields and real C1 origin-preserving point transformations on a connected interval
grading: derivative order zero field map plus first-derivative kinetic pullback; not a gauge or BV grading
action_owner: source owns only the I1B cubic transgression grammar; kinetic completion, observed quartic action and bridge theorem are repository-derived
target: existence and coefficient decision power of t=phi(q) under simultaneous kinetic and potential equality MAP-TYPE=classification
```

## The missing constraint

The predecessor classified all local analytic potential-germ equalities

```text
P(phi(q))=Q(q),
P(t)=f t+(c/2)t^2+(e/3)t^3,
Q(q)=(m2/2)q^2+(lambda/4)q^4.                 (1)
```

Whenever a linear- or positive-quadratic-leading source horn existed, free
Taylor jets of `phi` absorbed arbitrary `lambda`. That packet intentionally did
not constrain kinetic terms. The present reverse edge adds exactly that missing
demand. On a connected local domain, compare

```text
L_src=(kappa/2)(partial t)^2-P(t),
L_obs=(mu/2)(partial q)^2-Q(q),                 (2)
```

for fixed nonzero constants `kappa,mu` and an origin-preserving real `C1` point
transformation `t=phi(q)`.

## Kinetic equality is rigid

Pulling (2) back gives kinetic coefficient

```text
kappa phi'(q)^2=mu.                              (3)
```

If `mu/kappa<0`, no real bridge exists. If `mu/kappa>0`, continuity of
`phi'` on the connected interval prevents its sign from changing, so

```text
phi'(q)=s sqrt(mu/kappa),
phi(q)=s sqrt(mu/kappa) q,       s in {+1,-1}.   (4)
```

Thus fixed constant kinetic data remove every nonlinear local point-bridge
jet. Analyticity is not needed; `C1` regularity and connectedness suffice.

## Potential equality then decides the class

Put `alpha=s sqrt(mu/kappa)`. Coefficient comparison in (1) becomes

```text
f alpha=0,
c alpha^2=m2,
e alpha^3=0,
lambda=0.                                       (5)
```

Therefore an interacting target with `lambda>0` has no bridge in this class.
For the free target `lambda=0`, a bridge exists exactly in the same-sign real
horn when `f=e=0` and

```text
m2=c mu/kappa.                                  (6)
```

Unlike potential-germ matching alone, the fixed kinetic normalization has
decision power: it both kills the interacting equality and fixes the free mass
ratio when the source owns `c,kappa` and the observed normalization `mu` is
fixed.

## Hostile review and ceiling

The strongest overclaim would call this a full source-action no-go. It is not.
A variable source kinetic metric `K(t)` changes (3) to
`K(phi) phi'^2=mu` and can support nonlinear arc-length coordinates.
Derivative-dependent field redefinitions can create additional derivative
operators; nonlocal, background-dependent, orbit-averaged, singular and later-
action bridges are outside the theorem. The source packet also does not own the
one-mode kinetic completion used in (2).

The strongest contrary construction is precisely a variable kinetic metric
chosen so that a predecessor nonlinear bridge becomes an isometry. The weakest
reproducibility seam is comparing potentials while silently dropping the
Jacobian multiplying the kinetic term.

The exact probe checks the sign horns, rigidity, coefficient equations, free
positive control and interacting obstruction. It does not construct the
source-owned full-carrier kinetic operator, gauge complex, domain or bridge.
No prediction, confirmation, held-out score or GU verdict follows.

## Next condition

Lift the test to an independently source/action-owned full-carrier kinetic or
symplectic operator and its gauge/domain data. If that structure is variable or
the bridge depends on derivatives, declare the enlarged map class and compare
every induced derivative and interaction coefficient rather than importing
the constant-metric conclusion.
