---
title: "K1122 positive-reduction codimension floor"
status: active_research
doc_type: exact_nonnegative_subspace_codimension_theorem
created: 2026-10-05
claim_ceiling: sharp finite-dimensional necessity; no constraint construction
manifest: lab/process/k1122-k1121-positive-reduction-codimension-floor.json
probe: tests/channel-swings/k1122_k1121_positive_reduction_codimension_floor_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1122 positive-reduction codimension floor

> **GU-COMPARATOR-ROUTING — scope before inference.** This is an exact
> constrained-form theorem at the source-native boundary. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

```gu-typed-objects
result: sharp codimension floor for a nonnegative constrained carrier
carrier: finite Hessian fibre V and proposed constraint subspace W LAYER=toy CHIRALITY=N/A
pairing: self-adjoint form of inertia p,q,z ON=V
real_structure: real finite-symbol carrier
grading: negative, radical and positive spectral subspaces
action_owner: repository-construction -- conditional reduction theorem; source maps still unowned
target: W before residual-radical quotient MAP-TYPE=restriction
```

For a form of inertia `(p,q,z)`, every nonnegative subspace `W` has dimension
at most `p+z`; equivalently,

```text
codim(W) >= q.
```

The bound is sharp: the direct sum of the positive and radical spectral
subspaces attains it. The control `diag(-4,-1,0,2,3,5)` has inertia `(3,2,1)`;
its maximal nonnegative subspace has dimension four and codimension two.

Therefore a positive physical reduction of an indefinite Hessian needs at
least `q` independent non-gauge constraint conditions before any radical
quotient. This is necessary, not sufficient: it constructs no constraint map,
proves no propagation, and supplies no global closed domain. The producer
passes `9/9`; the hostile probe rejects `9/9` mutations.
