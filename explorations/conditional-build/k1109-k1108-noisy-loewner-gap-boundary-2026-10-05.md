---
title: "K1109 noisy Loewner gap boundary"
status: active_research
doc_type: conditional_noisy_loewner_gap_boundary
created: 2026-10-05
claim_ceiling: exact singular-gap stability condition and near-coalescent instability boundary for Loewner rank
manifest: lab/process/k1109-k1108-noisy-loewner-gap-boundary.json
probe: tests/channel-swings/k1109_k1108_noisy_loewner_gap_boundary_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1109 noisy Loewner gap boundary

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a conditional
> matrix-perturbation theorem, not source-native GU evidence. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `INTERNAL_CONDITIONAL_NOISY_LOEWNER_GAP`.

```gu-typed-objects
result: singular-gap condition and near-coalescent instability for noisy Loewner rank
carrier: finite sampled Loewner matrices LAYER=toy CHIRALITY=N/A
pairing: spectral norm and positive Euclidean Gram form ON=conditional_loewner_matrix
real_structure: real symmetric matrix data
grading: retained rank directions and numerical null directions
action_owner: repository-construction -- no source-selected GU Hessian
target: K1108 exact cross-Loewner certificate MAP-TYPE=evaluation
```

Let measured data produce `Lhat=L+E` with an independently certified bound
`||E||_2<=epsilon`. Weyl's inequalities give

```text
sigma_j(Lhat) >= sigma_j(L)-epsilon,
sigma_j(L)    >= sigma_j(Lhat)-epsilon.
```

Therefore `sigma_r(Lhat)>epsilon` certifies `rank(L)>=r`, hence at least
`r-1` poles when the affine slope is positive. The statement becomes exact
order only after an independent at-most-`r-1` pole bound. Conversely,
`sigma_r(Lhat)<=epsilon` is inconclusive; it cannot certify absence of the
`r`th direction.

There is no model-class-wide positive noise threshold. Take nodes `(0,1,2)`,
`alpha=2`, unit weights, and shifts `(1,1+t)`. The Gram determinant is

```text
det L(t)=2*t^2/[9(1+t)^2(2+t)^2(3+t)^2].
```

It equals `1/2592`, `20000/461519289`, and
`200000000/336055001230809` at `t=1,1/10,1/100`, and tends to zero as the
poles coalesce. A physical use therefore needs independently owned floors on
pole separation, weights and slope, controlled sample geometry, and an error
propagation bound into the Loewner matrix norm.

The producer passes `13/13`; the hostile probe rejects `13/13` mutations.
