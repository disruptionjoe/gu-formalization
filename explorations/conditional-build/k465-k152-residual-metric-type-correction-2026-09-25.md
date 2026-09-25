---
title: "K465 — K152 Residual Metric-Type Correction"
status: working_draft_verified
status_axis: operational_state
doc_type: conditional_build
date: "2026-09-25"
classification: INTERNAL_STRUCTURAL_ONLY
direction: observed_to_native
---

# K465 — K152 residual metric-type correction

> **GU-COMPARATOR-ROUTING — scope before inference.** This internal operator
> audit is not evidence for or against a source-native physical mechanism.
> Read `lab/methods/source-native-comparator-routing.md` before reuse.

## Result

K457 applies `S^(-*)` to the residual covector, with `M=S^*S`. Therefore its
squared norm is exactly

`||S^(-*) ell||^2 = ell^* M^(-1) ell`.

K152 instead defines the shifted form-dual residual energy

`ell^* (R+sM)^(-1) ell`.

These are different metric types. For `M=diag(2,3)` and `ell=(1,1)`, the
M-dual square is `5/6`. Shifted forms `diag(4,6)` and `diag(8,3)` leave that
M-dual value unchanged but give shifted form-dual squares `5/12` and `11/24`.
K457's 2,958-vector, 201-group and 59,586-entry reduction therefore survives
as an M-dual payload, while its shifted-form-dual label is retracted under
correction `K457-DUAL-METRIC-20260925`.

## Boundary

No Gram entry is evaluated and no numerical shifted residual, K152 interval,
source, ledger, canon, paper, public or physical claim follows.

## Reproduction

Run `python3 tests/channel-swings/k465_k152_residual_metric_type_correction_probe.py`.
