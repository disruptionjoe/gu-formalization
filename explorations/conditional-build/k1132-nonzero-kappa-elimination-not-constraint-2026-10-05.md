---
title: "K1132 nonzero-kappa elimination is not a constraint"
status: active_research
doc_type: source_i1b_nonzero_kappa_constraint_owner_classification
created: 2026-10-05
claim_ceiling: exact current-horn constraint classification; exceptional shells and global domain open
manifest: lab/process/k1132-nonzero-kappa-elimination-not-constraint.json
probe: tests/channel-swings/k1132_nonzero_kappa_elimination_not_constraint_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1132 nonzero-kappa elimination is not a constraint

> **GU-COMPARATOR-ROUTING — scope before inference.** This applies K1131 to
> the selected source-native I1B `T=0` distortion block. It does not bind every
> GU completion. Read `lab/methods/source-native-comparator-routing.md`.

Classification: `SOURCE_NATIVE_ROUTE`.

```gu-typed-objects
result: nonzero-kappa distortion elimination versus constraint classification
carrier: native g-plus-T finite symbol/frequency carrier LAYER=source-print CHIRALITY=N/A
pairing: selected Hodge/scalar-Clifford distortion pairing ON=C=kappa K+C1
real_structure: real I1B T=0 symbol
grading: metric and all-grade distortion blocks
action_owner: source-action -- selected I1B local quadratic germ
target: K1123 non-gauge constraint floor MAP-TYPE=evaluation
```

K129 and K133 establish that for nonzero `kappa_1`, `C(0)=kappa_1 K` is
invertible and that `C_1(n)+kappa_1 K` is invertible at each fixed covector
away from a finite exceptional multiset. K1131 therefore gives

```text
ker(C*)=0  =>  Q=L*A=0.                               (1)
```

So the generic nonzero-kappa horn supplies distortion elimination, not a
non-gauge field constraint. Its Schur graph `t=-C^{-1}Ah` does not pay any of
K1123's `6/6/4` positivity budget.

At the exceptional shells, `C` is singular and K1131 permits a nonzero
solvability map, but its rank is shell-dependent and no current result proves
a smooth propagated constraint bundle. K140 independently shows that the
fixed-frequency inverse graph is not an action-owned homogeneous constraint
projector or a uniform principal reduction. These shells remain open data,
not constraints by declaration. The producer passes `11/11`; the hostile
probe rejects `9/9` mutations.
