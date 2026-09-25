---
title: "K470 — K152 Direct M-Dual Projection Scheduler"
status: working_draft_verified
status_axis: operational_state
doc_type: conditional_build
date: "2026-09-25"
classification: INTERNAL_STRUCTURAL_ONLY
direction: observed_to_native
---

# K470 — K152 direct M-dual projection scheduler

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a conditional
> theorem for the repository-supplied K139/K168 operator family, not evidence
> for or against a source-native GU mechanism. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

## Theorem

Under K469's complete-complement packet, write

`delta=(sqrt((beta-rho)^2+4 eta^2)-(beta-rho))/2`.

The squared M-angle from `u` to the complete ground eigenspace satisfies

`sin_M^2(u,E0) <= delta/(beta-rho+delta)`.

Thus a projection tolerance `p` is certified by

`eta^2 <= p^2(beta-rho)^2/(1-p^2)^2`.

The two-block control `rho=-2`, `beta=2`, `eta=3/2` has exact squared angle
`1/9`, saturating the `p=1/3` budget.

## Boundary

The theorem needs the same complete native complement floor as K469. A finite
Ritz vector is not the complete ground spectral projection, and no native
projection claim or physical state follows.

## Reproduction

Run `python3 tests/channel-swings/k470_k152_direct_m_dual_projection_scheduler_probe.py`.
