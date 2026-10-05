---
title: "K1087 boundary-domain preservation"
status: active_research
doc_type: conditional_boundary_domain_preservation
created: 2026-10-04
claim_ceiling: exact multiplication-domain criteria for Dirichlet, Neumann and Robin realizations
manifest: lab/process/k1087-k1086-boundary-domain-preservation.json
probe: tests/channel-swings/k1087_k1086_boundary_domain_preservation_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1087 boundary-domain preservation

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a conditional
> boundary-domain theorem, not source-native GU evidence. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `INTERNAL_CONDITIONAL_DOMAIN_THEOREM`.

```gu-typed-objects
result: boundary preservation is automatic for Dirichlet but conditional for Neumann and Robin
carrier: H2 sections of E over a compact manifold with boundary LAYER=observed CHIRALITY=N/A
pairing: positive L2 bundle pairing with a self-adjoint elliptic realization ON=conditional_connection_hessian
real_structure: real Euclidean or complex Hermitian
grading: bulk operator domain and boundary trace
action_owner: repository-construction -- boundary law remains unselected
target: K1086 common-domain requirement MAP-TYPE=evaluation
```

Smooth multiplication by `C` always preserves the Dirichlet domain because
`f|boundary=0` implies `(Cf)|boundary=0`. It preserves every Neumann section
exactly when `nabla_n C=0` on the boundary. For Robin operator `S`,

```text
(nabla_n+S)(Cf)=(nabla_n C+[S,C])f+C(nabla_n+S)f,
```

so preservation is equivalent to `nabla_n C+[S,C]=0`. Even a bulk-parallel
potential therefore needs `[S,C]=0` for Robin data.

The positive constant matrices `S=diag(1,2)` and
`C=[[2,1],[1,2]]` supply a sharp control: Neumann passes, but
`[S,C]=[[0,-1],[1,0]]`, whose action on `e1` is `(0,1)`, rejects Robin
preservation. A bulk commutator theorem cannot silently choose or preserve a
boundary domain.

The producer passes `10/10`; the hostile probe rejects `11/11` boundary,
identity, witness and scope mutations. Self-adjoint ellipticity and GU action
ownership remain separate checks for any future native realization.
