---
title: "K1088 holonomy branch decomposition"
status: active_research
doc_type: conditional_holonomy_branch_decomposition
created: 2026-10-04
claim_ceiling: exact parallel-eigenbundle branch theorem with an explicit common-ladder condition
manifest: lab/process/k1088-k1087-holonomy-branch-decomposition.json
probe: tests/channel-swings/k1088_k1087_holonomy_branch_decomposition_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1088 holonomy branch decomposition

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a conditional
> spectral theorem, not source-native GU evidence. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `INTERNAL_CONDITIONAL_SPECTRAL_THEOREM`.

```gu-typed-objects
result: parallel commuting coefficients yield affine branches on parallel eigenbundles, not automatically one common ladder
carrier: orthogonal direct sum of parallel joint eigenbundles E_j LAYER=observed CHIRALITY=N/A
pairing: positive L2 pairing with a projection-preserving boundary realization ON=conditional_connection_hessian
real_structure: real Euclidean or complex Hermitian
grading: holonomy blocks and covariant spatial eigenmodes
action_owner: repository-construction -- no source-selected connection or boundary law
target: K1083 affine branch selector MAP-TYPE=evaluation
```

When `B` and `C` are commuting parallel self-adjoint endomorphisms and the
boundary realization preserves their joint spectral projections, the bundle
splits orthogonally into parallel simultaneous eigenbundles `E_j`. On each,

```text
H|E_j = b_j L_j+c_j,
omega_jn^2 = b_j lambda_jn+c_j,
```

where `L_j` is the restricted connection Laplacian. Parallel endomorphisms are
the commutant of connection holonomy; on an irreducible orthogonal holonomy
block every parallel self-adjoint endomorphism is scalar.

The important boundary is the subscript on `lambda_jn`. A single shared ladder
`lambda_n` requires an additional isospectral identification of the restricted
connections and boundary domains. It is sufficient, for example, that every
`E_j` carries a copy of the same spatial connection and realization. Parallel
commuting coefficients alone give affine laws against each branch's own
covariant spectrum.

The exact fixture uses common ladder `{0,1,4}` with `(b,c)=(2,5)` and `(3,7)`,
producing `{5,7,13}` and `{7,10,19}`. The producer passes `11/11`; the hostile
probe rejects `10/10` hypothesis, holonomy, ladder and scope mutations.
