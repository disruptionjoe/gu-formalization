---
artifact_type: conditional_physics_ledger_migration
created: 2026-08-10
status: CURRENT_APPEND_ONLY_LEDGER_V0_136
predecessor: lab/process/conditional-physics-ledger-v0.135.json
canon_verdict_change: none
---

# Conditional physics ledger v0.136

## Progress meter

```text
Ledger v0.136 — 82/82 mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue — 84 continuous; conditional parent range 84..86
Function-valued slots — >=19
Open discrete forks — 9
Scoped quotients — 5
Frontier — 1 condition closed · 1 opened · 1 named condition remains
```

## Migration

v0.135 remains immutable. Six rows move in distance/evidence only after exact
composition and hostile review of the already-built q-repaired draft-9.16
zero-order middle family with `W`, its ASD mirror, and three parent witnesses.

`W` and the mirror are disjoint rank-192 projectors and their sum has rank 384.
For a moving-Spin witness, a non-Spin witness preserving the two `U(32,32)`
halves, and a source-full `U(64,64)` coset witness:

- the `W -> mirror` coefficient system has exact rank two;
- the leakage outside `W plus mirror` coefficient system has exact rank two;
- the mirror has the identical fingerprint;
- only the zero coefficient eliminates either leakage class.

At the minimal-leakage ratio each characteristic-zero witness still has
`W -> mirror` rank 64 and outside-pair rank 64. J-commuting Spin/two-half
witnesses prefer `alpha=beta`; the J-anticommuting full-parent coset witness
prefers `alpha=-beta`. Generic planted ratios leak more strongly.

Thus the existing family preserves neither `W` nor its doubled mirror closure.
This kills invariance under any freely ranging parent containing the tested
witness; it does not kill an action-selected smaller connection orbit, a
different adapter, the complete four-field operator, BV cohomology, or a global
domain.

The next Build derives the connection orbit actually owned by the selected
action and tests whether it excludes both leaking parity classes, or constructs
the complete BV/domain cohomology before imposing any `W` carrier restriction.
No physical quotient, cohomology, spectrum, index, count or datum is booked.

No verdict, residue, quotient, coefficient, datum, P1/P2/P3, canon verdict or
public posture changes.

## Rows moved

- `RA-D2`, `RA-F1`, `RA-F2`, `RA-G2`, `LT-SM3`, `AC-F1`: the principal
  partial result remains; the existing zero-order family is now an exact scoped
  obstruction, and action-owned orbit/BV/domain construction owns the next
  carrier, mirror, chirality and count burden.

Evidence:

- `explorations/conditional-build/selected-k77-zero-order-w-mirror-parent-leakage-2026-08-10.md`;
- `lab/process/selected-k77-zero-order-w-mirror-parent-leakage.json`;
- `lab/process/hostile-reviews/2026-08-10-selected-k77-zero-order-w-mirror-parent-leakage-review.md`.
