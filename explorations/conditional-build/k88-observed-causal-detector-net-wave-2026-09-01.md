---
title: "K88 observed causal detector net wave"
status: active_research
doc_type: reverse_scaffold_discrete_causal_detector_result
created: 2026-09-01
date: 2026-09-01
claim_ceiling: exact finite repository-owned discrete-action detector embeddings, unit-site finite propagation, isotony, spacelike Weyl commutation and timelike noncommuting controls; no source-selected GU local net, continuum AQFT, functional BFV descent, Hadamard spectrum, Born detector dynamics, Bell prediction, confirmation, or verdict
manifest: lab/process/k88-observed-causal-detector-net-wave.json
probe: tests/channel-swings/k88_observed_causal_detector_net_probe.py
---

# K88 observed causal detector net wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`

```gu-typed-objects
result: exact finite-speed detector pullbacks, isotony and spacelike Weyl commutation selected by a local discrete hyperbolic action
carrier: real canonical initial data on an open fifteen-site one-plus-one lattice LAYER=observed CHIRALITY=N/A
pairing: canonical initial-data symplectic form and the induced Weyl commutator ON=repository_owned_discrete_action_control
real_structure: real scalar lattice field with rational mass and nearest-neighbor coefficients
grading: even bosonic field algebra; distinct from BFV ghost grading
action_owner: repository-construction
target: lattice event evaluations to causally supported initial-data detector embeddings MAP-TYPE=evaluation
```

## Let the action choose the embedding

K87 showed that arbitrary globally conjugated commuting factors span distinct
correlation faces even with one fixed state. This packet supplies an action
that chooses local detector embeddings instead. On an open one-dimensional
lattice take the discrete Lagrangian

```text
L_d(q_n,q_(n+1))
  = 1/2 |q_(n+1)-q_n|^2 - 1/2 q_n^T K q_n,                 (1)
```

where `K=m^2 I+kappa(2I-S-S^T)` is the symmetric nearest-neighbor stiffness.
With `p_n=q_n-q_(n-1)`, its discrete Euler--Lagrange equation is the canonical
update

```text
p_(n+1)=p_n-K q_n,
q_(n+1)=q_n+p_(n+1).                                      (2)
```

The block matrix of (2) preserves the canonical symplectic form exactly.
Because `K` is nearest-neighbor, evaluation of `q_(n,x)` pulled back to the
common initial data uses only sites `y` with `|x-y|<=n`. This is an exact
support theorem by induction, not a small-coefficient or group-velocity
approximation.

## A finite causal Weyl net

Associate to each event its pulled-back linear observable `F_(n,x)` and Weyl
generator `W(F_(n,x))`. The Weyl commutator is controlled by the initial-data
symplectic bracket. The exact fifteen-site probe chooses events `(1,3)` and
`(2,11)`. Their backward support cones lie in `{2,3,4}` and
`{9,10,11,12,13}`, so

```text
sigma(F_(1,3),F_(2,11)) = 0,
[W(F_(1,3)),W(F_(2,11))] = 0.                              (3)
```

Support inclusion from one to two time steps supplies the finite isotony
control. The same-site timelike pair `(0,3),(1,3)` has symplectic bracket of
absolute value one, so the instrument is not vacuously declaring every pair
local.

Locality is load-bearing. An asymmetric stiffness breaks symplecticity. A
single long-range matrix entry puts site 11 into the one-step support of the
site-3 detector. A periodic endpoint coupling puts site 14 into the one-step
support of site 0. Each mutation is caught rather than relabeled as a new
causal adjacency.

## Hostile review and boundary

The strongest overclaim would call (1)--(3) the physical GU local net. It is a
finite repository-owned discrete action showing how causal dynamics and an
observation map can remove the arbitrary-factor ambiguity isolated by K87.
The strongest contrary route is a nonlocal stencil, which remains symmetrizable
but destroys the claimed unit lattice cone. The weakest seam is the passage
from finite canonical support to the source continuum operator, its BFV/Green
domain, microlocal spectrum and physical detector coupling.

The probe passes `26/26`; its hostile selftest catches `16/16` mutations.
Weyl commutation does not select detector outcomes, a Born law or a
correlation face. No source GU net, continuum AQFT, Bell prediction, held-out
score, canon or public posture moves.

## Next condition

Derive the observation map and causal propagator from the source-owned full
action, carry their event-local algebras through the functional BFV/Green
quotient, and test compatibility with the selected physical state. Only that
joint owner can license a correlation face for forward confrontation.
