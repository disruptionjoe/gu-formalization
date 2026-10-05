---
title: "K1113 Cauchy separation gap bound"
status: active_research
doc_type: conditional_cauchy_separation_gap_bound
created: 2026-10-05
claim_ceiling: explicit determinant and singular-gap lower bound from owned separation floors
manifest: lab/process/k1113-k1112-cauchy-separation-gap-bound.json
probe: tests/channel-swings/k1113_k1112_cauchy_separation_gap_bound_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1113 Cauchy separation gap bound

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a conditional
> matrix-conditioning theorem, not source-native GU evidence. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `INTERNAL_CONDITIONAL_CAUCHY_GAP_BOUND`.

```gu-typed-objects
result: quantitative separation-to-singular-gap certificate
carrier: residual cross-Loewner matrices LAYER=toy CHIRALITY=N/A
pairing: spectral norm and positive auxiliary Gram form ON=conditional_loewner_matrix
real_structure: real Cauchy factors
grading: retained inverse directions and numerical null directions
action_owner: repository-construction -- no source-selected GU Hessian
target: K1112 exact positive reconstruction MAP-TYPE=evaluation
```

The Cauchy determinant identity gives

```text
det V(X,d)=prod_(i<j)(x_j-x_i) prod_(i<j)(d_j-d_i)
           / prod_(i,k)(x_i+d_k),
det R=det V_X det V_Y prod_i w_i.
```

For `m` nodes per side and `q=m(m-1)/2`, node gaps `delta_X,delta_Y`, pole
gap `delta_d`, `0<=x,y<=X`, `d<=D` and `w>=w_min` imply

```text
|det R| >= w_min^m delta_X^q delta_Y^q delta_d^(2q)
           /(X+D)^(2m^2).
```

If also `d>=d_min` and `w<=w_max`, then
`||R||_2<=m^2 w_max/d_min^2` and
`sigma_min(R)>=|det R|/||R||_2^(m-1)`. The K1098 two-pole fixture has exact
`det R=1/540`; the deliberately coarse frozen floors give
`det R>=1/419904` and `sigma_min(R)>=1/6718464`.

This quantifies K1109's missing inputs but does not own them for GU or an
apparatus. The producer passes `14/14`; the hostile probe rejects `14/14`
mutations.
