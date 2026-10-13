---
title: "K1771--K1775 full-Fisher preconditioner wave"
status: active_research
document_role: exploration
claim_verdict: exact_geometric_preconditioner_with_full_fisher_certificate_still_open
target_claim: INTERNAL_TARGET__K1704_CONTROLLED_SCALAR_CARDINAL_ENVELOPE
updated_at: "2026-10-13"
---

# K1771--K1775: exact preconditioning before full Fisher

> **GU-COMPARATOR-ROUTING — scope before inference.** This is repository
> trial-functional mathematics. It supplies no source-owned action, physical
> state, observed map, prediction or confirmation.

Classification: `INTERNAL_STRUCTURAL_AND_EXACT_COVER_ONLY`.

## Interior topology

Replaying K1769's exact 59 interior leaves shows that their union is not an
opaque tube. It is exactly three rational slabs, containing 37, 16 and six
contiguous `z` cells. Their exact endpoints and the union digest are frozen in
K1771. This is topology of the degree-seven outer cover only.

## Boundary contraction

Starting from K1769's one lower strip, K1772 adaptively bisects the coordinate
with smaller local depth and tests the exact degree-seven threshold polynomial
with tensor Bernstein coefficients. At depth 16 in both coordinates it emits
44 pruned leaves, two retained leaves and zero unresolved leaves. Both retained
cells satisfy `z<=2^-23`; their union ends at
`t=49758723570445/2251799813685248`.

## Legal full-Fisher next certificate

The K1686 MMSE identity permits the Rademacher posterior estimator
`eta_t(y)=tanh(sqrt(t)y/(1-t))`. Writing `B=E[X eta_t(Y)]` and
`C=E[eta_t(Y)^2]` gives the rigorous one-sided functional

```text
J_X(t) >= V(t,c,z) = t/(1-t)^2 (2B-C-t).                 (1)
```

K1773 splits the singular corner into `c<=z^2` with `lambda=c/z^2` and
`c>=z^2` with `lambda=z^2/c`. The second chart requires an explicit
`lambda->0` rare-component enclosure; raw `c/z` interval arithmetic at the
corner is forbidden. On `[-11,11]`, Arb Taylor integration can evaluate the
regular terms; outside it, `|tanh|<=1` gives the tail budget
`3 P(|Z|>11)`. This is an executable proof contract, not a completed Arb
certificate.

## Admitted result and next gate

The prior 60-cell cover is now preconditioned to three exact interior slabs
plus two microscopic boundary cells. The boundary cells are not excluded.
Full-Fisher interval Newton, parameter-derivative tail control, the `z=1`
atom chart, stationarity, uniqueness and value comparison remain open.

K1771--K1775 add five satisfied bridge rows, for 475 total: 396 satisfied,
ten conditional, 65 excluded and four missing. Protected source, ledger,
canon, paper, prediction, confirmation and public-posture states do not move;
K1145/K1150 remain `0/7`.
