---
title: "K1126 K895 first-order formal-adjoint correction"
status: active_research
doc_type: correction
created: 2026-10-05
claim_ceiling: exact constant-coefficient principal-symbol correction
manifest: lab/process/k1126-k895-first-order-formal-adjoint-correction.json
probe: tests/channel-swings/k1126_k895_first_order_formal_adjoint_correction_probe.py
target_claim: SC-ACT-06
---

# K1126 K895 first-order formal-adjoint correction

> **GU-COMPARATOR-ROUTING — scope before inference.** This corrects one
> formal-adjoint inference inside a frozen finite-symbol calculation. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

```gu-typed-objects
result: corrected first-order formal-adjoint parity for the K895 principal coefficient
carrier: compactly supported real fields with constant first-order coefficients LAYER=source-print CHIRALITY=N/A
pairing: standard real L2 pairing ON=compact-support-control
real_structure: coefficient transpose with one integration by parts
grading: exact principal-symbol correction; complete Hessian open
action_owner: source-action -- source-selected coefficient only
target: SC-ACT-06 MAP-TYPE=evaluation
```

For `D=sum_mu A_mu partial_mu` on compactly supported fields with constant
coefficients, `D*=-sum_mu A_mu^T partial_mu`. Thus first-order formal
self-adjointness requires `A_mu^T=-A_mu`, not `A_mu^T=A_mu`. Equivalently,
the Fourier symbol `i A(xi)` is Hermitian for real `xi`.

K895's selected coefficient remains skew and retains rank `130912`; that is
the correct first-order parity, so the claimed rank-130912 principal Helmholtz
obstruction is withdrawn. This does not prove a complete Hessian. Coefficient
derivatives, lower-order Euler terms, pairing density, boundary convention and
one common closed domain remain required. The producer passes `14/14`; the
hostile probe rejects `14/14` mutations. No protected status moves.
