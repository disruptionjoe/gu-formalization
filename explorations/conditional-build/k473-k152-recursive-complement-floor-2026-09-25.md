---
title: "K473 — K152 Recursive Complete-Complement Floor"
status: active_research
status_axis: operational_state
doc_type: conditional_recursive_same_form_complement_floor
created: 2026-09-25
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# K473 — K152 recursive complete-complement floor

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: INTERNAL_STRUCTURAL_ONLY.

Scope: the theorem acts only on the complete M-orthogonal complement in the
fixed K139/K162 limiting form. It does not provide any native numerical block.

```gu-typed-objects
result: recursive complete-complement floor from a finite slice, complete tail and cross block
carrier: one complete K162 charge sector split as span(u) plus F plus T in the physical M-Hilbert geometry LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: positive physical Gram M=S* S on the fixed limiting K139 form ON=k162_complete_complement
real_structure: CAR adjoint, momentum conjugation and K162 signed flavor transport
grading: trial line, finite complement slice and complete analytic tail
action_owner: repository-construction; no source or GU action selects the extension, coefficients, scalar center or state
target: K463 complete M-orthogonal-complement floor beta MAP-TYPE=not-a-map
```

## Opening bookend

K469 now converts a complete complement floor into the exact K457 residual
budget, but no native `beta` exists. A finite Ritz value or HVZ member cannot
fill that field. The strongest cheap structural route is to split the complete
complement into a computable finite slice and an analytically controlled tail,
while retaining the cross block rather than pretending the split reduces the
form. This is a prerequisite reduction, not a numerical answer.

## Theorem

Let the complete M-orthogonal complement be `Q_M=F direct-sum_M T`. Suppose

```text
F R F >= alpha F_M,
T R T >= gamma T_M,
||F R T||_(M-dual) <= mu.
```

For `v=f+t`, Cauchy--Schwarz gives the scalar two-block lower form

```text
alpha ||f||_M^2 - 2 mu ||f||_M ||t||_M + gamma ||t||_M^2.
```

Therefore

```text
Q R Q >= beta Q_M,
beta=(alpha+gamma-sqrt((alpha-gamma)^2+4 mu^2))/2.       (1)
```

The sharp threshold test is

```text
alpha>b, gamma>b, mu^2<(alpha-b)(gamma-b).              (2)
```

Equation (2) is exactly the positive definiteness of the shifted scalar block.
It proves `beta>b` without computing an eigenbasis of the complete tail. The
bound is sharp for a scalar two-block control.

The exact control `alpha=3`, `gamma=6`, `mu=2` has discriminant 25 and
`beta=2>1`. A nonsquare control `alpha=3`, `gamma=5`, `mu=1` yields
`beta=4-sqrt(2)>5/2`, enclosed outward at 16 dyadic bits.

## Closing bookend

- Strongest advance: one infinite complete-complement floor is reduced to
  three independently certifiable same-form quantities.
- Strongest overclaim: a finite slice floor by itself is the native `beta`.
  Refused; the complete tail and cross norm are load-bearing.
- Strongest contrary construction: a large cross block can push the lower
  root below `b` even when both diagonal floors exceed `b`.
- Weakest seam: `F` and `T` must be an exhaustive M-orthogonal partition on
  the same fixed form; an independent regulator or free tail is inadmissible.

No numerical K162 packet is emitted. Next evaluate one finite-slice floor,
complete analytic tail floor and cross norm for the combined K139/K168 form.

## Reproduction

```bash
python3 tests/channel-swings/k473_k152_recursive_complement_floor.py
python3 tests/channel-swings/k473_k152_recursive_complement_floor_probe.py
```
