---
title: "K1146 common graph-domain criterion"
status: active_research
doc_type: exact_functional_common_domain_criterion
created: 2026-10-05
claim_ceiling: exact closed-operator graph-domain theorem and counterexample; no source functional realization
manifest: lab/process/k1146-common-graph-domain-criterion.json
probe: tests/channel-swings/k1146_common_graph_domain_criterion_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1146 common graph-domain criterion

> **GU-COMPARATOR-ROUTING — scope before inference.** This theorem tests the
> domain bookkeeping of supplied closed operators. It does not construct the
> source I1B operators or their common physical realization. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

```gu-typed-objects
result: common graph-domain criterion with an exact composition-domain counterexample
carrier: countable Hilbert direct sum of finite fibres LAYER=source-print CHIRALITY=N/A
pairing: ambient Hilbert norm plus finite summed graph norms ON=supplied-closed-operators
real_structure: real or complex Hilbert direct sum; source real form not supplied
grading: base domain, individual graph domains and product graph domains
action_owner: comparator -- the source must separately own every operator and boundary realization
target: K1145 common-closed-domain gate MAP-TYPE=restriction
```

Let `T_1,...,T_m` be closed operators on one Hilbert space. Their finite
intersection

```text
D = intersection_j D(T_j)
```

is complete in the combined graph norm

```text
||u||_D^2 = ||u||^2 + sum_j ||T_j u||^2.                         (1)
```

This gives an honest common closed realization for the listed operators. It
does not automatically make every composition in an algebraic identity
defined on `D`.

The exact diagonal example on `ell2(N)` makes the distinction sharp. Take
`Q_n=n`, `G_n=n^2`, and `u_n=n^-3`. Then

```text
sum |u_n|^2       = sum n^-6 < infinity,
sum |Q_n u_n|^2  = sum n^-4 < infinity,
sum |G_n u_n|^2  = sum n^-2 < infinity,
sum |Q_nG_n u_n|^2 = sum 1 = infinity.
```

Thus `u` lies in `D(Q) intersection D(G)` but not in `D(QG)`. A functional
version of `QG=RQ`, `Qd=0`, or `G*H+HG=0` must name the graph domains of the
actual composed words, not only the four individual operators. The producer
passes `12/12`; the hostile probe rejects `10/10` mutations.
