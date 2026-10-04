---
title: "K1066 global fourth-mode monotonicity"
status: active_research
doc_type: conditional_fourth_mode_monotonicity_theorem
created: 2026-10-04
claim_ceiling: global monotonicity theorem for the supplied conditional four-mode horn family; no preparation or detector ownership
manifest: lab/process/k1066-k1064-global-fourth-mode-monotonicity.json
probe: tests/channel-swings/k1066_k1064_global_fourth_mode_monotonicity_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1066 global fourth-mode monotonicity

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a conditional
> apparatus-design theorem, not source-native GU evidence. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `INTERNAL_CONDITIONAL_DECISION_CERTIFICATE`.

```gu-typed-objects
result: the sharp symmetric four-mode error budget increases strictly with every higher fourth mode
carrier: fixed lambda={3,8,15} plus lambda_n=n(n+2), n>=4 LAYER=observed CHIRALITY=N/A
pairing: l1-normalized residual contrasts ON=repository_owned_candidate_holdout
real_structure: real positive dispersion frequencies
grading: exact global theorem for the supplied horn family; no apparatus ownership
action_owner: repository-construction -- preparation, scale and detector remain unowned
target: K1064 high-mode robustness tradeoff MAP-TYPE=evaluation
```

For ordered nodes `x_1<x_2<x_3<x_4`, the barycentric witness has alternating
signs. Multiplying its `l1` norm by the positive Vandermonde gives

```text
Q(x)=2(x_3-x_1)(x_4-x_2)
       [(x_2-x_1)+(x_4-x_3)].
```

Every positive gap `sqrt(lambda_j+mu)-sqrt(lambda_i+mu)` decreases strictly
with `mu`. Thus `Q_1>Q_4`. The two directed residual numerators are the same
determinant up to sign, so the `mu=1` witness evaluated on `mu=4` is always the
limiting direction.

Write `t=n+1`, so the fourth eigenvalue is `t^2-1`. Differentiating that
limiting contrast reduces positivity to

```text
2t^2+6t+12
 > sqrt(t^2+3)[(sqrt(19)-sqrt(7))t
              +8sqrt(3)+3sqrt(7)-3sqrt(19)].
```

Both sides are positive. After squaring and setting `u=t-4`, the difference is
a quartic whose coefficients are

```text
-22+2sqrt(133),
-172-16sqrt(57)+16sqrt(21)+20sqrt(133),
-372-144sqrt(57)+144sqrt(21)+72sqrt(133),
260-432sqrt(57)+92sqrt(133)+432sqrt(21),
482-304sqrt(57)+38sqrt(133)+304sqrt(21).
```

All are positive; the rational brackets `sqrt(21)>4.582`,
`sqrt(57)<7.550`, and `sqrt(133)>11.532` already certify this termwise.
Therefore the threshold increases strictly for every real `t>4`, not merely
the K1064 fixtures. It starts at `0.00241504213401050...` for `n=4` and tends
to `0.00955587804121949...`.

The producer passes `16/16`; the hostile probe rejects `12/12` family,
normalizer, limiting-direction, derivative, positivity, ceiling, scope and
promotion mutations.

## Next condition

Invert the global law into least-mode targets and compose it with the
three-mode curvature budget before asking an apparatus to choose a mode.
