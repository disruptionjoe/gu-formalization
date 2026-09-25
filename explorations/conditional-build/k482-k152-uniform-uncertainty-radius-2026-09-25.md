---
title: "K482 — K152 Uniform Uncertainty Radius"
status: active_research
status_axis: operational_state
doc_type: conditional_same_form_uniform_uncertainty_radius
created: 2026-09-25
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# K482 — K152 uniform uncertainty radius

Classification: INTERNAL_STRUCTURAL_ONLY.

```gu-typed-objects
result: sharp shared gap-loss and cross-growth radius for the K473 margin
carrier: one complete same-form M-orthogonal two-block K162 split LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: positive physical Gram M=S* S ON=k162_complete_complement
real_structure: CAR adjoint, momentum conjugation and K162 signed flavor transport
grading: two target-relative diagonal gaps and one cross norm
action_owner: repository-construction; native error model absent
target: robust strict K473 margin MAP-TYPE=not-a-map
```

## Theorem

Write the nominal target-relative gaps as `a=alpha-t0`, `g=gamma-t0` and
cross norm as `mu`. If a single certified radius `r` bounds the loss of each
gap and the growth of the cross norm, then

```text
(a-r)(g-r)-(mu+r)^2
  = ag-mu^2-r(a+g+2mu).
```

Therefore the sharp strict radius is
`r < (ag-mu^2)/(a+g+2mu)`. The control `a=4,g=7,mu=3` has nominal slack `19`,
sharp radius `19/17`, and selected radius `1` leaves exact slack `2`.

## Bookends

The theorem converts correlated interval production into one exact tolerance.
It does not assert that future errors share this model; that correlation must
be proved. Equality is a zero-slack rejection. The weak seam is provenance of
the combined gap-loss bounds after floor and target errors are composed.

No native error estimate, floor or K152 interval is emitted.

## Reproduction

```bash
python3 tests/channel-swings/k482_k152_uniform_uncertainty_radius.py
python3 tests/channel-swings/k482_k152_uniform_uncertainty_radius_probe.py
```
