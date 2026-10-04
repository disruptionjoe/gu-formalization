---
title: "K1067 least-mode inverse design"
status: active_research
doc_type: conditional_fourth_mode_inverse_design_certificate
created: 2026-10-04
claim_ceiling: exact least integer fourth modes for named candidate error targets; no physical target or preparation cost
manifest: lab/process/k1067-k1066-least-mode-inverse-design.json
probe: tests/channel-swings/k1067_k1066_least_mode_inverse_design_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1067 least-mode inverse design

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a conditional
> design calculation, not source-native GU evidence. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `INTERNAL_CONDITIONAL_DECISION_CERTIFICATE`.

```gu-typed-objects
result: exact least fourth modes meeting named normalized component-error targets
carrier: K1066 fourth-mode family LAYER=observed CHIRALITY=N/A
pairing: sharp symmetric eta/gamma boundary ON=repository_owned_candidate_holdout
real_structure: real positive dispersion frequencies
grading: exact discrete inverse design under the supplied transfer model
action_owner: repository-construction -- target and preparation cost remain unowned
target: K1066 global monotonic tolerance MAP-TYPE=evaluation
```

K1066 makes the first passing integer unique. Representative inverse-design
rows are

| target `eta/gamma` | least `n` | `lambda_n=n(n+2)` | achieved |
| ---: | ---: | ---: | ---: |
| 0.0030 | 5 | 35 | 0.00368990763714949... |
| 0.0050 | 7 | 63 | 0.00517205728577458... |
| 0.0075 | 17 | 323 | 0.00758873086197872... |
| 0.0090 | 64 | 4224 | 0.00900622958868708... |
| 0.0095 | 641 | 412163 | 0.00950004723270548... |

Each preceding integer fails its named target. The design ceiling is
`E_infinity=0.00955587804121949...`, and

```text
E_infinity-E(n)
 = [2+sqrt(7)-sqrt(19)]/[8(n+1)] + O((n+1)^-2).
```

Hence approaching the ceiling costs inverse distance at leading order: a
small final tolerance gain can require a very large mode increase. A target
at or above the ceiling is impossible inside this family.

The producer passes `13/13`; the hostile probe rejects `12/12` target,
minimality, eigenvalue, ceiling, asymptotic, cost, scope and promotion
mutations.

## Next condition

Compare these four-mode targets with the three-mode joint curvature/error
budget in the same response normalization.
