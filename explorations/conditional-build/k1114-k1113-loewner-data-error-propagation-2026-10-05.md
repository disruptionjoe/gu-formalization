---
title: "K1114 Loewner data-error propagation"
status: active_research
doc_type: conditional_loewner_data_error_propagation
created: 2026-10-05
claim_ceiling: deterministic scalar-sample and affine-parameter error map into the Loewner pencil
manifest: lab/process/k1114-k1113-loewner-data-error-propagation.json
probe: tests/channel-swings/k1114_k1113_loewner_data_error_propagation_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1114 Loewner data-error propagation

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a conditional
> deterministic error theorem, not source-native GU evidence. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `INTERNAL_CONDITIONAL_LOEWNER_DATA_ERROR`.

```gu-typed-objects
result: scalar branch-data error propagated to ordinary and shifted Loewner matrices
carrier: two disjoint finite sampled mode sets LAYER=toy CHIRALITY=N/A
pairing: spectral norm ON=conditional_loewner_pencil
real_structure: real scalar samples and matrices
grading: exact pencil versus measured approximation
action_owner: repository-construction -- no measured GU branch
target: K1113 quantitative singular-gap bound MAP-TYPE=evaluation
```

Suppose `|S_hat(z)-S(z)|<=eta` on two `m`-node sets, their cross-gap is
`g>0`, and all node magnitudes are at most `R`. If the affine estimates obey
`|alpha_hat-alpha|<=epsilon_alpha` and
`|beta_hat-beta|<=epsilon_beta`, then

```text
||Delta R||_2 <= m(2 eta/g+epsilon_alpha),
||Delta P||_2 <= m(2 R eta/g+2 R epsilon_alpha+epsilon_beta).
```

For the frozen `m=2`, `eta=1/1000`, `epsilon_alpha=1/2000`,
`epsilon_beta=1/1000`, `g=1`, `R=3` fixture, the ordinary entry/norm bounds
are `1/400` and `1/200`; the shifted bounds are `1/100` and `1/50`.

Sample spacing and affine calibration must therefore be budgeted jointly
before rank or generalized-eigenvalue stability is invoked. No physical GU
samples or systematic budget are supplied. The producer passes `14/14`; the
hostile probe rejects `14/14` mutations.
