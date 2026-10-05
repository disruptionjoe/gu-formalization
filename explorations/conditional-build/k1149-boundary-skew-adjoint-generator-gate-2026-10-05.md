---
title: "K1149 boundary skew-adjoint generator gate"
status: active_research
doc_type: exact_boundary_generator_domain_gate
created: 2026-10-05
claim_ceiling: exact interval derivative realization comparison; no source boundary domain or GU evolution
manifest: lab/process/k1149-boundary-skew-adjoint-generator-gate.json
probe: tests/channel-swings/k1149_boundary_skew_adjoint_generator_gate_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1149 boundary skew-adjoint generator gate

> **GU-COMPARATOR-ROUTING — scope before inference.** This interval theorem
> separates formal differential parity from a selected generator domain. It
> does not derive the source boundary coupling, trace space, or physical
> evolution. Read `lab/methods/source-native-comparator-routing.md` before
> reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

```gu-typed-objects
result: boundary maximality gate for a formally skew first-order generator
carrier: L2 interval fields with H1 trace domains LAYER=source-print CHIRALITY=N/A
pairing: standard L2 Green pairing ON=operator-domain
real_structure: complex scalar interval control; source real form not supplied
grading: formal expression, symmetric domain, adjoint domain and generator domain
action_owner: comparator -- the source must separately own the boundary trace and evolution
target: K1145 H-skew propagation and common-boundary-domain gate MAP-TYPE=restriction
```

For `G=d/dx` on `L2(0,1)`, integration by parts gives

```text
<Gu,v> + <u,Gv> = u(1)^*v(1) - u(0)^*v(0).                      (1)
```

The domain `H1_0(0,1)` kills this form and makes `G` skew-symmetric. It does
not make `G` skew-adjoint: its adjoint has the larger domain `H1(0,1)`, so the
Dirichlet realization is not maximal and does not generate a unitary group.

The periodic domain

```text
D_per = {u in H1(0,1) : u(1)=u(0)}
```

also kills the boundary form, but now the adjoint has the same domain. This
realization is skew-adjoint and generates unitary translations. Therefore
formal `H`-skewness, even with vanishing flux on a small domain, is necessary
but not sufficient for K1143's functional energy evolution. A candidate must
select a maximal skew-adjoint domain preserved by the evolution and shared
with its constraints and cohomology. The producer passes `12/12`; the hostile
probe rejects `10/10` mutations.
