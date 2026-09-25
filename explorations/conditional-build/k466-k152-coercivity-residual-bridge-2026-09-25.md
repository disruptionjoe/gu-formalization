---
title: "K466 — K152 Coercivity Residual Bridge"
status: working_draft_verified
status_axis: operational_state
doc_type: conditional_build
date: "2026-09-25"
classification: INTERNAL_STRUCTURAL_ONLY
direction: observed_to_native
---

# K466 — K152 coercivity residual bridge

> **GU-COMPARATOR-ROUTING — scope before inference.** This conditional
> operator theorem is not a physical GU result. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

## Theorem

If the shifted form satisfies `R+sM >= cM > 0`, inverse order gives

`(R+sM)^(-1) <= c^(-1) M^(-1)`.

Consequently every residual covector obeys

`ell^*(R+sM)^(-1)ell <= c^(-1) ell^*M^(-1)ell`.

The inequality is sharp when `R+sM=cM`. A nonidentity exact control with
`M=diag(2,3)`, `R+sM=diag(6,12)`, `ell=(2,3)` and `c=3` has M-dual square
`5`, shifted form-dual square `17/12`, and ceiling `5/3`.

K463's global floor formula can supply `c=lambda_-+s`, but no numerical native
K162 value of `c` is currently serialized. K466 therefore repairs the type
bridge without pretending the native residual has been bounded.

## Reproduction

Run `python3 tests/channel-swings/k466_k152_coercivity_residual_bridge_probe.py`.
