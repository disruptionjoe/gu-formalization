---
title: "K1103 bounded-multiplicity identifiability"
status: active_research
doc_type: conditional_bounded_multiplicity_identifiability
created: 2026-10-05
claim_ceiling: exact sufficient finite-mode uniqueness theorem under a declared auxiliary multiplicity bound
manifest: lab/process/k1103-k1102-bounded-multiplicity-identifiability.json
probe: tests/channel-swings/k1103_k1102_bounded_multiplicity_identifiability_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1103 bounded-multiplicity identifiability

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a conditional
> rational-identifiability theorem, not source-native GU evidence. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `INTERNAL_CONDITIONAL_BOUNDED_MULTIPLICITY_INVERSE`.

```gu-typed-objects
result: 2m+2 exact modes identify any reduced branch with at most m auxiliary poles
carrier: one physical plus at most m diagonal auxiliary real modes LAYER=toy CHIRALITY=N/A
pairing: standard positive Euclidean pairing ON=conditional_block_hessian
real_structure: real symmetric diagonal auxiliary pencil
grading: physical and auxiliary blocks
action_owner: repository-construction -- no source-selected GU Hessian or multiplicity bound
target: K1102 one-pole inverse MAP-TYPE=evaluation
```

Consider two reduced branches

```text
S_a(x)=alpha_a x+beta_a-sum_i w_ai/(x+d_ai)
```

with at most `m` distinct simple poles each. Put their difference over the
product of both pole polynomials. That common denominator has degree at most
`2m`; after multiplication, the affine difference contributes degree at most
`2m+1`, while the partial-fraction terms are lower degree. Hence the numerator
of `S_1-S_2` has degree at most `2m+1`.

If the branches agree at `2m+2` distinct regular sample points, that numerator
has more roots than its degree and vanishes identically. Equality of reduced
rational functions then fixes the affine slope and intercept and every
distinct pole and positive residue, up to permutation.

The sufficient sample counts are therefore

| multiplicity bound `m` | numerator degree bound | sufficient exact modes |
| ---: | ---: | ---: |
| 1 | 3 | 4 |
| 2 | 5 | 6 |
| 3 | 7 | 8 |
| 4 | 9 | 10 |

The `m=1` row recovers K1102. This is a sufficient exact-data theorem, not a
claim of noisy stability or minimality in every constrained subclass. Its
physical use also depends on independently owning the finite multiplicity
bound and the diagonal simple-pole model.

The producer passes `8/8`; the hostile probe rejects `8/8` mutations. No
source-owned auxiliary multiplicity or physical samples are supplied.
