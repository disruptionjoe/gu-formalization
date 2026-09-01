---
title: "K77 source-transgression analytic-bridge classification wave"
status: active_research
doc_type: reverse_scaffold_source_to_observed_analytic_bridge_classification
date: 2026-09-01
claim_ceiling: exact local one-mode analytic-germ classification from the source-native cubic I1B augmented-torsion transgression to the repository-owned massive quartic rank-1920 quotient action; no full-carrier bridge, source selection, nonlocal or later-action obstruction, prediction, confirmation, or GU verdict
manifest: lab/process/k77-source-transgression-analytic-bridge-classification-wave.json
probe: tests/channel-swings/k77_source_transgression_analytic_bridge_classification_probe.py
---

# K77 source-transgression analytic-bridge classification wave

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
result: leading-order classification of origin-preserving local analytic bridges between the source I1B transgression ray and the observed massive quartic action ray
carrier: one real augmented-torsion ray and one real one-mode ray inside the rank-960 observed quotient W LAYER=conditional CHIRALITY=N/A
pairing: source Shiab/Hodge action pairing on the first ray and transported positive H pairing on the second ON=typed_action_germ_comparison
real_structure: real analytic germs at the origin; complex branches are excluded
grading: order of vanishing and polynomial field degree only; not a BRST, BV-BFV or particle grading
action_owner: source owns the I1B transgression grammar; GU repository owns the observed action family and this bridge classification; no bridge is attributed to the source
target: equality of one-mode action germs under an origin-preserving local analytic bridge MAP-TYPE=classification
```

## Frozen germs and the first invariant

Write the source ray and observed quotient ray as

```text
P(t)=f t+(c/2)t^2+(e/3)t^3,
Q(q)=(m2/2)q^2+(lambda/4)q^4,   m2>0, lambda>=0.   (1)
```

The coefficients `f,c,e` are the source ray responses already separated by
the affine packet. This result does not assert which of them is nonzero on a
physical background. Let `phi(0)=0` be a nonzero real analytic bridge and set

```text
r=ord_0(P),       d=ord_0(phi).
```

Because `m2>0`, `ord_0(Q)=2`. Orders multiply under composition, so

```text
P(phi(q))=Q(q)  implies  r d=2.                    (2)
```

There are exactly two analytic horns: `(r,d)=(1,2)` and `(2,1)`. A purely
cubic leading source response, `r=3`, admits no origin-preserving analytic
one-mode bridge to a massive target germ. This is an order-of-vanishing
obstruction, not a rejection of the source action.

## Horn A: linear-leading source response

If `f!=0`, the analytic inverse-function theorem gives one local germ

```text
phi(q)=P^{-1}(Q(q)),
phi(q)=(m2/(2f))q^2+O(q^4).                         (3)
```

It exists for every `m2>0` and every `lambda>=0` after shrinking the
neighborhood. But `phi'(0)=0`: this is not a local field diffeomorphism. The
target mass and quartic coefficient are encoded in bridge jets rather than
selected by the source germ. Equality of these one-dimensional actions hence
has zero coefficient-identification power while the bridge is free.

## Horn B: quadratic-leading source response

If `f=0` and `c!=0`, write `phi(q)=q u(q)`. Equation (1) becomes

```text
u(q)^2 (c/2+(e/3)q u(q)) = m2/2+(lambda/4)q^2.     (4)
```

A real branch requires `c>0`, because its leading coefficient satisfies

```text
c u(0)^2=m2.                                        (5)
```

For either choice `u(0)=+sqrt(m2/c)` or `-sqrt(m2/c)`, the derivative of the
left side of (4) with respect to `u` at the origin is `c u(0)!=0`. The
analytic implicit-function theorem therefore supplies a unique local branch.
Now `phi'(0)=u(0)!=0`, so this is the only horn that can be a real local field
diffeomorphism. The cubic source response generates odd intermediate terms,
but the higher bridge jets cancel them recursively. Again every `lambda` is
allowed: it changes the bridge, not a source-owned coefficient equation.

If `c<0`, no real locally invertible branch reaches the positive massive
target. Complex branches are outside the frozen real structure.

## Polynomial and selector boundaries

When `e!=0` and `phi` is a nonconstant polynomial of degree `d`,

```text
deg(P composed with phi)=3d.                        (6)
```

It can never equal the interacting quartic `Q`, because `3d=4` has no integer
solution. Thus the prior affine obstruction extends to every global
polynomial bridge on a genuinely cubic source ray. This polynomial no-go does
not apply when the cubic ray coefficient vanishes; for example a linear
source germ can absorb `Q` into a degree-four noninvertible polynomial bridge.

The decision table is therefore exact:

| source leading order | analytic bridge to massive `Q` | locally invertible | coefficient selection |
| --- | --- | --- | --- |
| `r=1` (`f!=0`) | yes, unique after choosing `P` | no | none; bridge jets absorb `m2,lambda` |
| `r=2` (`f=0,c>0`) | two sign branches | yes | none; bridge jets absorb `m2,lambda` |
| `r=2` (`f=0,c<0`) | no real branch | no | real-sign obstruction only |
| `r=3` (`f=c=0,e!=0`) | no | no | order obstruction only |

## Hostile review and next condition

The strongest overclaim would call (6) a nonlinear source-action no-go. It is
only a polynomial one-mode obstruction on a genuinely cubic ray. The strongest
contrary construction is (3): a noninvertible analytic germ always exists when
`f!=0`. The weakest seam is physical ownership: an equality of one-mode
potentials does not own the kinetic operator, pairing, gauge quotient, domain,
locality or full rank-1920 map.

A selecting source bridge must therefore arrive independently with more than
action-germ equality. It must own the full-carrier map or restrict the allowed
bridge class through kinetic, symplectic, gauge, locality, domain or measure
data. Nonlocal, background-dependent, orbit-averaged and later-action routes
remain open, and no held-out evidence is scored.
