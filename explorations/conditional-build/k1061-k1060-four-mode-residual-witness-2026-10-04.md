---
title: "K1061 four-mode residual witness"
status: active_research
doc_type: conditional_four_mode_quadratic_residual_theorem
created: 2026-10-04
claim_ceiling: exact residual and component-sup feasibility certificate for the supplied four-mode horns; no physical detector evidence
manifest: lab/process/k1061-k1060-four-mode-residual-witness.json
probe: tests/channel-swings/k1061_k1060_four_mode_residual_witness_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1061 four-mode residual witness

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact is a
> conditional candidate-family theorem, not source-native GU evidence. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `INTERNAL_CONDITIONAL_DECISION_CERTIFICATE`.

```gu-typed-objects
result: exact four-mode residual witnesses for the two common-quadratic readout spaces
carrier: modes lambda={3,8,15,24} and mu in {1,4} LAYER=observed CHIRALITY=N/A
pairing: l1-normalized annihilator against the readout vector ON=repository_owned_candidate_holdout
real_structure: real positive frequencies and real quadratic transfer coefficients
grading: exact finite-dimensional feasibility theorem; no measured detector
action_owner: repository-construction -- transfer calibration and apparatus remain unowned
target: K1059 four-mode quadratic identifiability MAP-TYPE=evaluation
```

For horn `mu`, every quadratic readout lies in

```text
S_mu=span{1,lambda,x_mu},  x_mu(lambda)=sqrt(lambda+mu).
```

There is a unique annihilator `w_mu` up to scale. Normalize it by
`||w_mu||_1=1`. For `mu=1`, the exact witness is

```text
w_1=(-1,3,-3,1)/8.
```

For `mu=4`, barycentric weights
`1/prod_{j!=i}(x_i-x_j)`, followed by `l1` normalization, give the second
witness. Both annihilate `1`, `lambda`, and their own `x_mu`. Their directed
cross-horn contrasts are

```text
|w_4 dot x_1| = 0.00704922401371245...
|w_1 dot x_4| = 0.00483008426802017....
```

For any observed vector `y`, its exact component-sup distance to the horn
hyperplane is `|w_mu dot y|`, because the witness has unit `l1` norm. This
turns K1059's nonzero determinant into an operational residual without fitting
the nuisance offset and quadratic coefficient first.

The producer passes `14/14`; the hostile probe rejects `10/10` mode, witness,
contrast, feasibility, scope and promotion mutations.

## Next condition

Compose both directed contrasts with componentwise detector error and a
certified lower bound on the linear response.
