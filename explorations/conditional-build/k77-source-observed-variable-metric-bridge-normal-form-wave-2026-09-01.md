---
title: "K77 source-observed variable-metric bridge normal-form wave"
status: active_research
doc_type: reverse_scaffold_source_observed_variable_metric_bridge_result
date: 2026-09-01
claim_ceiling: exact geodesic normal form and quartic jet classification for local point transformations with a fixed positive one-mode source kinetic metric; no source-owned full-carrier metric, derivative-dependent, nonlocal, singular, background-dependent or later-action equivalence
manifest: lab/process/k77-source-observed-variable-metric-bridge-normal-form-wave.json
probe: tests/channel-swings/k77_source_observed_variable_metric_bridge_normal_form_probe.py
---

# K77 source-observed variable-metric bridge normal-form wave

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
result: variable-metric local point-bridge geodesic normal form and quartic coefficient-jet classification
carrier: one real source augmented-torsion ray and one real observed massive quotient ray LAYER=conditional CHIRALITY=N/A
pairing: fixed positive source kinetic metric h(t) dt^2 and fixed positive observed coefficient mu ON=repository_owned_bridge_test
real_structure: real fields and real C1 origin-preserving point transformations on a connected interval
grading: derivative order zero field map plus first-derivative kinetic pullback; not a gauge or BV grading
action_owner: source owns only the I1B cubic transgression grammar; h, the observed quartic action and bridge theorem are repository-derived
target: existence and coefficient decision power of t=phi(q) under simultaneous variable-kinetic and potential equality MAP-TYPE=classification
```

## The variable metric has an exact normal form

Let the repository-owned one-mode source and observed candidates be

```text
L_src=(1/2)h(t)(partial t)^2-P(t),
P(t)=f t+(c/2)t^2+(e/3)t^3,
L_obs=(mu/2)(partial q)^2-Q(q),
Q(q)=(m2/2)q^2+(lambda/4)q^4,                  (1)
```

with `h(t)>0`, `mu>0`, and an origin-preserving local point map `t=phi(q)`.
Define the source arc-length coordinate

```text
F(t)=integral_0^t sqrt(h(s)) ds.                (2)
```

The kinetic equality is

```text
h(phi(q)) phi'(q)^2=mu.                         (3)
```

Since `F'=sqrt(h)>0`, equation (3) is equivalent on a connected interval to

```text
F(phi(q))=s sqrt(mu) q,
phi(q)=F^-1(s sqrt(mu) q),       s in {+1,-1}.  (4)
```

Thus a fixed positive variable metric does not restore free bridge jets. It
makes the bridge affine in source geodesic distance rather than in the original
coordinate `t`. The complete local potential condition is consequently

```text
Q(q)=P(F^-1(s sqrt(mu) q)).                     (5)
```

## The first metric jets can generate and select a quartic

Write

```text
h(t)=h0+h1 t+(h2/2)t^2+O(t^3),     h0>0.        (6)
```

For `f=0` and `c` nonzero, exact series inversion of (2) gives

```text
m2=c mu/h0,                                      (7)
h1=4 e h0/(3c)                                  (8)
```

when the observed cubic coefficient is required to vanish. Under (8), the
quartic coefficient is

```text
lambda=mu^2(2 e^2 h0-9 c^2 h2)/(27 c h0^3).    (9)
```

The constant-metric theorem is the special horn `h1=h2=0`: (8) then forces
`e=0`, and (9) forces `lambda=0`. A nonconstant source metric can instead
convert a cubic source response into an even observed quartic. For example,

```text
h0=4, c=3, e=2, mu=9, h1=32/9, h2=0
```

gives exactly `m2=27/4` and `lambda=1/2` through (7)-(9), despite the source
potential having no quartic term.

## Ownership is the discriminator

Equations (4)-(9) are decision-grade only when `h` is fixed independently by
the source or its action. Then its geodesic coordinate and jets select or reject
the observed coefficients. If `h0,h1,h2` are chosen after reading `m2,lambda`,
the same equations are a target-fitting recipe: for nonzero `c,e` they can fit
the cubic cancellation and quartic coefficient rather than derive them.

This separates two claims that the phrase "variable-metric escape" hides:

- a fixed source-owned metric removes bridge-jet freedom and may select the
  target through its canonical-coordinate potential;
- a target-fitted metric can manufacture the desired equality and has no
  independent evidential force.

The present packet constructs neither source ownership nor a full-carrier
metric. It classifies the exact data such an owner would have to supply.

## Hostile review and ceiling

The strongest overclaim would say variable metrics rescue or kill the full GU
bridge. They do neither without an independently owned `h`. The strongest
contrary construction is the explicit positive local metric above, which
produces a nonzero quartic and refutes any extension of constant-metric
rigidity to all point-map kinetic terms. The weakest reproducibility seam is
silently fitting `h1,h2` to the target and then reporting the fitted metric as
source selection.

The theorem is one-dimensional and local. Indefinite or degenerate metrics,
multiple fields, gauge quotients, derivative-dependent maps, nonlocal maps,
singular charts, background/orbit averages and later-action bridges remain
outside it. No source-action, physical-state, prediction, confirmation,
held-out or GU-verdict credit follows.

## Next condition

Obtain the independently source/action-owned full-carrier kinetic metric,
gauge quotient and domain, put that metric into canonical coordinates, and
compare the complete transformed potential and derivative operators. If the
map depends on derivatives or is nonlocal, freeze that enlarged map class and
every induced operator before testing it.
