---
title: "K1148 uniform positive cohomology gap"
status: active_research
doc_type: exact_uniform_coercivity_gate
created: 2026-10-05
claim_ceiling: exact uniform positivity criterion and vanishing-gap counterexample; no source positive state space
manifest: lab/process/k1148-uniform-positive-cohomology-gap.json
probe: tests/channel-swings/k1148_uniform_positive_cohomology_gap_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1148 uniform positive cohomology gap

> **GU-COMPARATOR-ROUTING — scope before inference.** This theorem tests a
> supplied bounded quotient form after closed-range reduction. It does not
> supply the source physical pairing, interacting state space, or Born rule.
> Read `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

```gu-typed-objects
result: uniform coercivity criterion for a positive Hilbert cohomology pairing
carrier: closed Hilbert cohomology assembled from finite fibres LAYER=source-print CHIRALITY=N/A
pairing: bounded positive quotient form ON=complete-degree-zero-cohomology
real_structure: real or complex Hilbert quotient; source real form not supplied
grading: fibrewise classes, global completion and coercive physical norm
action_owner: comparator -- the positive quotient form requires a separately source-owned Hessian and complex
target: LT-SM8/LT-GR6b positive-physical-space debt MAP-TYPE=evaluation
```

Assume the gauge image is closed, so the Hilbert cohomology quotient is
Hausdorff. A bounded fibrewise positive form defines a coercive pairing in the
inherited Hilbert norm exactly when its positive eigenvalues have one uniform
lower bound `c>0`.

Modewise positivity alone is insufficient. On `ell2(N)`, the diagonal form

```text
H_n = 1/n
```

is strictly positive on every one-dimensional fibre. Nevertheless the unit
vectors `e_n` have ambient norm one and energy `1/n -> 0`. There is no positive
coercivity constant, the Riesz map has no bounded inverse, and the energy norm
is not equivalent to the admitted Hilbert norm. The control `H_n=1+1/n` has
uniform floor one.

K1144's finite radical and nonzero-dimension tests therefore need two separate
functional additions: closed gauge range and a uniform positive gap on the
completed quotient. Neither is supplied by checking every finite symbol in
isolation. The producer passes `12/12`; the hostile probe rejects `10/10`
mutations.
