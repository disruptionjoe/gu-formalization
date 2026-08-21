---
title: "B5 strict-massless extension dependence: a coflip-real characteristic zero mode"
status: active_research
doc_type: exact_unbounded_operator_kernel
created: "2026-08-21"
registry: lab/process/b5-strict-massless-extension-dependence.json
probes:
  - tests/channel-swings/b5_strict_massless_extension_dependence_probe.py
grade: "ON THE REPOSITORY-CONSTRUCTED FLAT B5 HALF-CYLINDER, THE ACTION-OWNED STRICT MASSLESS FOLDED EXPRESSION HAS EXTENSION-SENSITIVE GLOBAL OPERATOR KERNEL DATA. AN EXACT COMPLEX-NULL POSITIVE-TANGENTIAL FOURIER MODE GIVES A COFLIP-REAL DECAYING NONGAUGE ZERO MODE. A REAL WITT POLARIZATION CONTAINING ITS GREEN-NULL TRACE AND A SECOND POLARIZATION REPLACING THAT WITT LINE DEFINE TWO CLOSED COFLIP-COMPATIBLE REALIZATIONS; THE ZERO MODE BELONGS TO THE FIRST KERNEL AND IS EXCLUDED FROM THE SECOND DOMAIN. THIS DOES NOT YET DEFINE BV/BRST COHOMOLOGY OR A PHYSICAL QUOTIENT."
target_verdict: B5_STRICT_MASSLESS_GLOBAL_OPERATOR_KERNEL_IS_EXTENSION_SENSITIVE
target_claim: internal target B5-STRICT-MASSLESS-EXTENSION-DEPENDENCE; verdict exact operator-kernel discriminator constructed at M=0
canon_verdict_change: none
---

# B5 strict-massless extension dependence

## Continuation update — marked reduced cohomology class separates domains

The exact decaying mode now has closed stage-separated realizations. Finite-
dimensional Green-line extensions of the minimal middle operator place its
trace in the hit domain and the opposite Witt line in the miss domain; closed
pullback gauge domains and the maximal terminal domain preserve both Noether
compositions. A bounded projection to Fourier mode `e4` and vector components
`1,2` annihilates the complete gauge range but fixes the witness. Its marked
class therefore survives both the algebraic and reduced hit quotients and is
absent from the miss domain.

This is extension-sensitivity of one marked linear gauge/BRST class, not a
calculation of total cohomology, positivity, physical states or a source-
selected domain. See
`explorations/b5-domain-compatible-brst-cohomology-2026-08-21.md`.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

Scope: this result binds the action-owned strict massless constant-coefficient
folded Rarita--Schwinger/BV expression on the repository-constructed flat
half-cylinder. It is not Weinstein's unreleased source action, the global
geometry of `Y=Met(X)`, a positive physical Hilbert space, a defined BV/BRST
cohomology, or the graph-mixing Stage-B family.

```gu-typed-objects
result: the undeformed strict massless folded expression has different global operator-kernel subspaces on two named constant coflip-compatible closed trace realizations
carrier: L2 sections of the rank-1920 complex folded carrier E=S plus V* tensor S over [0,infinity) times T13 LAYER=ambient CHIRALITY=S-FULL-DIRAC
pairing: auxiliary positive L2 graph topology plus the program-native split Hermitian Green form B_dr on boundary traces ON=independent-B5-curved-strict-carrier
real_structure: relative Gamma-natural antilinear coflip covering the integral torus sign involution and fixing dr and the selected complex Fourier mode
grading: linear abelian BV ghost-field fold on the repository-constructed massless flat product end
action_owner: repository-construction strict massless bulk action; the two trace polarizations remain mathematically available and action/source-unselected
target: comparison of global operator kernels for two closed D_U domains at M=0 MAP-TYPE=evaluation
```

## Result first

On

```text
M_plus=[0,infinity)_r x T^(8,5),
```

take the positive tangential lattice covector `k=e4`. The relative coflip has
vector sign `t_4=-1`, while `t_0=+1` for the positive normal. Therefore the
Fourier-mode covector

```text
xi=-e0+i e4
```

is fixed by the anti-linear coflip and is complex-null:

```text
q(xi)=q(-e0)+q(i e4)=1-1=0.
```

Let `c(xi)=-gamma_0+i gamma_4`. The following operator-valued trace map is
nonzero and coflip-real. Therefore it is nonzero on some coflip-real spinor
`s` (the complex spinor module is the complexification of its fixed real
form). Fix such an `s`. In the folded carrier ordered as
`S plus (V* tensor S)`, set the ghost entry to zero and take

```text
v_1=gamma_2 c(xi) s,
v_2=gamma_1 c(xi) s,
v_a=0 otherwise.
```

Exact Clifford reduction gives

```text
c(xi)^2=0,
B_xi v=0.
```

The gauge symbol `A_xi` has vector support only in directions `0` and `4`,
whereas `v` has support only in directions `1` and `2`. Thus this is the
transverse nongauge characteristic construction, now at the complex Fourier
covector required by the half-cylinder rather than the prior real-null local
control.

## Exact decaying massless zero mode

Define

```text
u(r,y)=exp(-r) exp(i y_4) v.
```

It is periodic on the tangential torus and square-integrable on the half-line.
For the undeformed action-owned massless expression,

```text
D u = exp(-r) exp(i y_4) B_(-e0+i e4) v = 0.
```

No bounded zero-order deformation is present: this is exactly `M=0`.

The coordinate involution sends `y_4` to `-y_4`, complex conjugation sends
`exp(i y_4)` to `exp(-i y_4)`, and the two signs cancel. Exact relative
Clifford transport also fixes `v`. Hence the complete zero mode is coflip-real.

## Two named closed domains

The program-native boundary coefficient `B_dr` is nondegenerate of split
signature `(960,960)`. Exact Gaussian-integer Clifford contraction gives

```text
h_dr(v,v)=0.
```

Equivalently, this follows by applying the massless Green identity to the
decaying zero mode on `[0,R] x T^13` and taking `R` to infinity. Because `v`
is a nonzero coflip-real Green-null trace, the real Witt extension theorem
supplies a coflip-real Witt basis

```text
(v,w), (e_2,f_2), ..., (e_960,f_960),
```

with `h(v,w)=1` and the remaining standard pairings. Name

```text
L_hit  = complexification(span_R(v,e_2,...,e_960)),
L_miss = complexification(span_R(w,e_2,...,e_960)).
```

Both are constant coflip-fixed maximal-isotropic trace subspaces, so the prior
Fourier-modal theorem makes the realizations `D_hit` and `D_miss` closed.
Their intersection has complex dimension `959`; in particular `v` lies in
`L_hit` and not in `L_miss`.

Therefore

```text
u in ker(D_hit),
u not in Dom(D_miss),
```

and the strict massless global operator-kernel subspaces are extension-
sensitive.

## Claim ceiling and ownership

This closes the exact `M=0` operator-kernel discriminator left open by the
bounded-deformation result. It does not select either polarization: the bulk
quadratic action admits both and the filed primary source remains silent on
endpoint, asymptotic and real/Krein selectors.

The folded Hessian kernel is not yet BV or BRST cohomology. Although the
witness is nongauge at the characteristic-symbol level, a cohomology verdict
requires stage-separated closed domains for `A`, `K` and `A^vee`, proof that
the maps preserve those domains, and a decision on algebraic versus reduced
closed-range quotient. None is inferred from one folded maximal-isotropic
domain.

No Hilbert self-adjointness, Fredholmness, positivity, physical state space,
source-selected global `Met(X)` geometry, particle result or GU verdict is
claimed.

## Reproduction and continuation

`tests/channel-swings/b5_strict_massless_extension_dependence_probe.py`
certifies the complex-null mode, exact folded-symbol kernel, nongauge support,
anti-linear coflip fixedness, Green-null trace, Witt-polarization replacement,
closed-domain inheritance and strict `M=0` claim ceiling.

The next honest gate is
`B5-DOMAIN-COMPATIBLE-BRST-COHOMOLOGY-DISCRIMINATOR`: construct stage-separated
closed coflip-compatible domains for the strict complex and decide whether the
mode survives the global gauge quotient in one realization and not the other,
or prove cohomological stability. Positivity remains downstream of that gate
and a separate Krein-to-probability rule.
