---
title: "K1050 affine-invariant three-mode holdout"
status: active_research
doc_type: conditional_affine_invariant_three_mode_holdout
created: 2026-10-04
claim_ceiling: exact gain-and-offset-invariant candidate holdout on a supplied ruler; no preparation, record, GU selection or score
manifest: lab/process/k1050-k1049-affine-invariant-three-mode-holdout.json
probe: tests/channel-swings/k1050_k1049_affine_invariant_three_mode_holdout_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1050 affine-invariant three-mode holdout

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: exact common-gain-and-offset-invariant candidate mass-horn discriminator
carrier: three nonzero stationary modes lambda={3,8,15} LAYER=observed CHIRALITY=N/A
pairing: adjacent frequency-difference ratio ON=repository_owned_candidate_action
real_structure: ordered positive real frequencies and radical separation
grading: frozen candidate holdout; no physical preparation, detector or record
action_owner: repository-construction -- source selection and apparatus remain unowned
target: K1049 third-mode reopener MAP-TYPE=evaluation
```

On the common independently supplied scale `s^2=1`, prepare the three nonzero
modes `lambda={3,8,15}` and form

```text
D = (omega_3-omega_2)/(omega_2-omega_1).
```

Under `y_i=g omega_i+b` with one common `g>0`, both adjacent differences
acquire the same factor and `D` is unchanged. The mass-one horn has frequencies
`(2,3,4)` and hence `D_1=1`. The mass-four horn has

```text
(sqrt(7), 2sqrt(3), sqrt(19)),
D_4 = (sqrt(19)-2sqrt(3))/(2sqrt(3)-sqrt(7)) > 1.
```

The exact gap is

```text
[sqrt(19)+sqrt(7)-4sqrt(3)] / [2sqrt(3)-sqrt(7)].
```

It is positive because the denominator is positive and
`sqrt(19)+sqrt(7)>4sqrt(3)` is equivalent after squaring to
`sqrt(133)>11`. The sharp symmetric additive-`D` radius is half this gap.

This gives two honest candidate apparatus routes. The two-mode `Q` route uses
fewer prepared modes but needs offset control. The three-mode `D` route cancels
common gain and offset but needs a third prepared mode and calibrated
difference resolution. Both still need an owned spatial ruler, measured record
and complete systematics. GU credit separately needs a source-selected mass
coefficient and action-owned physical quotient.

SC-ACT-01/02/06 remain `ASSERTS`; SC-META-53 remains `UNCERTAIN`. LT-SM8,
LT-GR6b, RA-F1 and AC-F1 remain `NEEDS`. No source, ledger, empirical,
prediction, confirmation, canon or public posture moves.

The deterministic producer passes `13/13`; the hostile probe rejects `19/19`
mode, statistic, invariance, radical, separation, ownership, source, ledger
and promotion mutations.

## Next condition

Score either frozen route only after an owned ruler, corresponding mode
preparation, calibrated transfer model, measured record and complete systematic
audit exist. Preserve the separate source-action gate for GU credit.
