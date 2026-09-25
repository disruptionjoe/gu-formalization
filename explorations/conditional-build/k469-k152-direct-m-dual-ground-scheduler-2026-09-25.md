---
title: "K469 — K152 Direct M-Dual Ground Scheduler"
status: working_draft_verified
status_axis: operational_state
doc_type: conditional_build
date: "2026-09-25"
classification: INTERNAL_STRUCTURAL_ONLY
direction: observed_to_native
---

# K469 — K152 direct M-dual ground scheduler

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a conditional
> theorem for the repository-supplied K139/K168 operator family, not evidence
> for or against a source-native GU mechanism. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

## Theorem

Let `u` be M-normalized with Rayleigh value `rho`, and suppose the same fixed
form has complete M-orthogonal-complement floor `beta>rho`. If the complete
cross functional has M-dual norm at most `eta`, then

`lambda_0 >= rho - (sqrt((beta-rho)^2+4 eta^2)-(beta-rho))/2`.

Consequently a target deficit `d>0` is certified by the sharp two-block
budget

`eta^2 <= d(beta-rho+d)`.

This route consumes K457's M-dual payload directly. It does not need a shift
or the K466 metric bridge once the complete K463 complement premise is
available. K466/K467 remain valid for other coercivity routes.

The exact control has `rho=-2`, `beta=2`, `eta=3/2`, ground `-5/2` and
deficit `1/2`; the budget is saturated at `9/4`.

## Boundary

No numerical complete-sector K162 complement floor or target deficit is
present, so no Gram accuracy or native K152 interval is released. Finite Ritz
values and HVZ membership cannot substitute for `beta`.

## Reproduction

Run `python3 tests/channel-swings/k469_k152_direct_m_dual_ground_scheduler_probe.py`.
