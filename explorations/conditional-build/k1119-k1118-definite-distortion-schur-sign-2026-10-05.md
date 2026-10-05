---
title: "K1119 definite-distortion Schur sign"
status: active_research
doc_type: source_hessian_definite_distortion_schur_inertia
created: 2026-10-05
claim_ceiling: exact finite-symbol congruence under invertible definite C
manifest: lab/process/k1119-k1118-definite-distortion-schur-sign.json
probe: tests/channel-swings/k1119_k1118_definite_distortion_schur_sign_probe.py
target_claim: SC-ACT-01
---

# K1119 definite-distortion Schur sign

> **GU-COMPARATOR-ROUTING — scope before inference.** This applies an exact
> congruence to the source-native I1B block under a stated definite-`C`
> hypothesis. It does not own a global inverse. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

```gu-typed-objects
result: definite-C full inertia and reduced Schur sign
carrier: metric and invertible distortion finite-symbol blocks LAYER=source-print CHIRALITY=N/A
pairing: self-adjoint K128 Hessian form ON=metric_plus_distortion
real_structure: real or Hermitian finite symbol
grading: metric and distortion blocks
action_owner: source-action -- source-native I1B local quadratic germ under explicit C horn
target: SC-ACT-01 MAP-TYPE=evaluation
```

When `C` is invertible, block congruence gives

```text
H ~ diag(-A* C^-1 A, C).
```

Thus for `C>0`, the `(+,-,0)` inertia is
`(dim Y, rank A, dim X-rank A)`; for `C<0` it is
`(rank A, dim Y, dim X-rank A)`. A positive auxiliary block makes the reduced
metric Schur form nonpositive, not positive, while the full Hessian remains
indefinite whenever `A` is nonzero.

For `A=diag(2,3)` and `C=diag(1,4)`, the Schur diagonal is
`diag(-4,-9/4)` and the full inertia is `(2,2,0)`. Replacing `C` by
`diag(-1,-4)` produces `diag(4,9/4)` with the same full inertia. Fixed-symbol
invertibility does not create a global closed inverse, boundary adjoint or
physical quotient.

The producer passes `10/10`; the hostile probe rejects `10/10` mutations.
