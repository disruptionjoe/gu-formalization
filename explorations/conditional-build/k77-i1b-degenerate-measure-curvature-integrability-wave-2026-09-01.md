---
title: "K77 I1B degenerate-measure curvature-integrability wave"
status: active_research
doc_type: reverse_scaffold_i1b_degenerate_measure_curvature_integrability_result
date: 2026-09-01
claim_ceiling: exact repository-owned weighted invariant-action integrability classification for the punctured cross-null two-plane; no source-owned measure, action, boundary domain, counterterm policy, physical quotient, prediction or confirmation
manifest: lab/process/k77-i1b-degenerate-measure-curvature-integrability-wave.json
probe: tests/channel-swings/k77_i1b_degenerate_measure_curvature_integrability_probe.py
---

# K77 I1B degenerate-measure curvature-integrability wave

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
result: cross-null weighted mixed-curvature bare-integrability and renormalization classification
carrier: real degenerating Darboux two-plane on a punctured cross-null collar, embedded in the native rank-24 to rank-22 quotient jump LAYER=conditional CHIRALITY=N/A
pairing: varying Green form J_u=uJ_2 and invariant trace polynomial on curvature ON=repository_owned_boundary_test
real_structure: real two-dimensional regular-singular symplectic connection
grading: normal logarithmic residue plus tangential symplectic generator; not a physical BV-BFV grading
action_owner: native I1B data own only the rank jump; connection, measure-action test, finiteness law and counterterm policy are repository-derived
target: whether a degenerating-measure finite-action domain law supplies independent decision power for a MAP-TYPE=classification
```

## Put the singular curvature under the degenerating measure

Use the established punctured-collar normal form

```text
J_u=uJ_2,
A_u=(-I_2/2+C)/u,       tr(C)=0,
A_y=aH,
F_uy=(a/u)[C,H].                                (1)
```

The Darboux Pfaffian density scales as `u du dy`. To separate that geometry
from the choice of action, test the weighted family

```text
rho_p(u) du dy=u^p du dy,
S_p^mix=(1/2) integral rho_p(u) tr(F_uy^2).      (2)
```

This is a repository-owned invariant-polynomial action test. It is not a
source-owned positive norm or physical boundary prescription.

Let `D=[C,H]`. The radial factor in (2) is

```text
integral_epsilon^1 u^(p-2) du
  =(1-epsilon^(p-1))/(p-1),  p != 1,
  =log(1/epsilon),           p = 1.              (3)
```

It is finite as `epsilon -> 0` exactly when `p>1`.

## The nonnilpotent horn selects zero, not log(2) or log(3)

When `tr(D^2)` is nonzero, the singular coefficient in (2) is

```text
a^2 tr(D^2).                                    (4)
```

For `p<=1`, finite unrenormalized invariant action therefore forces `a=0`.
At the native Darboux density `p=1`, both candidate nonzero coefficients
`a=log(2)` and `a=log(3)` have a logarithmically divergent bare action. The
candidate law does not choose between them; it rejects both.

This is genuinely independent of the earlier identity `M=aD`: the zero verdict
comes from a declared boundary/domain admissibility condition, not from reading
`a` back out of a tensor derived from the same action. But the source does not
currently own finite bare invariant action as the cross-null admissibility law.

## Two blind horns remain

For

```text
C=[[p,q],[r,-p]],   H=diag(1,-1),
D=[[0,-2q],[2r,0]],   tr(D^2)=-8qr.              (5)
```

the invariant action separates three cases:

- `qr != 0`: `D` is nonnilpotent and the finite-bare `p<=1` horn forces
  `a=0`.
- Exactly one of `q,r` is nonzero: `D` is nonzero nilpotent. Every trace power
  vanishes, so the invariant-polynomial action is blind even though the tensor
  curvature still has a `1/u` pole.
- `q=r=0`: `D=0`, the mixed curvature vanishes for every `a`, and no selector
  exists.

The nilpotent horn would need a separately owned positive majorant, full tensor
boundary norm or matching law. Importing a coordinate Frobenius norm would
break the gauge-invariant question unless its auxiliary structure were owned.

## Renormalization removes the zero selector

At `p=1`, subtracting the local logarithmic divergence

```text
a^2 tr(D^2) log(1/epsilon)                       (6)
```

makes the pure-pole model finite for every `a`. This is a valid distinct
counterterm horn, but it renormalizes rather than selects the coefficient.
Both `log(2)` and `log(3)` survive unless a finite boundary condition or
matching datum supplies additional independent information. Bare finiteness
and renormalized admissibility are therefore different domain laws and must
not be silently interchanged.

## Hostile review and ceiling

The strongest overclaim would call `a=0` source-selected. It is only selected
by the repository-owned finite-bare action law. The strongest contrary route
is the explicit subtraction (6), which preserves every coefficient; the
nilpotent commutator is a second contrary horn invisible to the invariant
density. The weakest reproducibility seam is treating the indefinite trace
polynomial as a positive physical norm or failing to state whether
counterterms are admitted.

This packet does not extend through `u=0`, derive a source boundary condition,
construct a positive state space, or identify an observable. No source-action,
physical-quotient, prediction, confirmation, held-out or GU-verdict credit
follows.

## Next condition

Derive the actual cross-null measure, pairing or positive majorant, boundary
domain and counterterm policy from the source or a complete action. Then apply
the corresponding nonnilpotent, nilpotent or commuting horn. A nonzero
tangential coefficient requires either `p>1`, renormalized admissibility, or an
independently owned law that replaces finite bare invariant action.
