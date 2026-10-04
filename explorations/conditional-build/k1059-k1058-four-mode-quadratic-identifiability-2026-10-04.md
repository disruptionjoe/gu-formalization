---
title: "K1059 four-mode quadratic identifiability"
status: active_research
doc_type: conditional_four_mode_quadratic_transfer_identifiability_theorem
created: 2026-10-04
claim_ceiling: exact horn separation for four frozen modes under a common quadratic transfer with nonzero linear response; no apparatus ownership
manifest: lab/process/k1059-k1058-four-mode-quadratic-identifiability.json
probe: tests/channel-swings/k1059_k1058_four_mode_quadratic_identifiability_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1059 four-mode quadratic identifiability

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact is a
> conditional candidate-family theorem, not source-native GU evidence. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: four frozen modes distinguish the two supplied shape horns under common quadratic transfer with nonzero linear response
carrier: modes lambda={3,8,15,24} and mu in {1,4} LAYER=observed CHIRALITY=N/A
pairing: complete four-component readout vector ON=repository_owned_candidate_holdout
real_structure: positive real frequencies and real quadratic transfer coefficients
grading: exact finite candidate identifiability theorem; no physical preparation or detector
action_owner: repository-construction -- source selection and apparatus remain unowned
target: K1056 quadratic-transfer obstruction MAP-TYPE=evaluation
```

For fixed `mu`, a quadratic readout

```text
y=a x_mu^2 + g x_mu + b
```

lies in the three-dimensional vector space

```text
span{1, lambda, x_mu}
```

because `x_mu^2=lambda+mu`. On modes `{3,8,15,24}`, the mass-one vector is
`x_1=(2,3,4,5)`. Direct expansion gives

```text
det[1,lambda,x_1,x_4]
 = 2(3sqrt(19)-6sqrt(3)-sqrt(7)) > 0.
```

If it vanished, squaring the alleged equality would give
`56=12sqrt(21)`, then `3136=3024`, a contradiction. Hence the four columns
are independent. The two quadratic-readout spaces therefore intersect
exactly in `span{1,lambda}`.

Any shared four-mode readout requires the `x_mu` coefficient to vanish for
both horns. Thus no readout with nonzero linear response `g` fits both horns.
The degenerate pure-quadratic boundary `g=0` is exactly K1056's countermodel,
so the new mode repairs finite quadratic nuisance only when that response is
certified nonzero.

This identifies the dimensionless horn, not an absolute scale. The
deterministic producer passes `13/13`; the hostile probe rejects `13/13`
mode, determinant, intersection, scope, ownership and promotion mutations.

## Next condition

Reconcile the three-mode bounded-curvature route with the four-mode
quadratic-fit route and freeze their distinct apparatus obligations.
