---
title: "A12 -- constant-background coefficient family"
status: exploration
doc_type: research_note
updated_at: "2026-07-13"
verdict: "TRACE_FREE_BACKGROUND_FAMILY_LOCALIZED_TO_FULL_B_COEFFICIENT"
depends_on:
  - "explorations/threads/A6-constant-section-simons-stress-2026-07-12.md"
  - "explorations/threads/A8-constant-section-delta-perp-h0-2026-07-13.md"
  - "explorations/threads/A10-constant-background-rperp-ambient-action-2026-07-13.md"
  - "explorations/threads/A11-constant-background-ry-b0-contraction-2026-07-13.md"
companion_test: "tests/threads/A12_constant_background_coefficient_family.py"
---

# A12 -- Constant-Background Coefficient Family

Companion test: `tests/threads/A12_constant_background_coefficient_family.py` (exact SymPy, exit 0).

## Construction Used

This gate stays inside the program-native GU construction:

```text
Y14 = Met(X4), with the gimmel / trace-reversed DeWitt metric on the symmetric-pair normal fiber.
```

It is not using a standard field-theory ambient substitute. A12 only assembles the constant-background slots
already computed in the A6-A11 convention.

## Question

A11 pinned the natural full-SFF mixed ambient contraction `R^Y.B0`, but the final higher-codimension
Willmore-EL formula/sign and the scalar coefficient `c_W` are still not selected.

A12 asks the bounded question:

```text
Given only the computed A6/A8/A10/A11 slots, which formal coefficient can carry a trace-free
constant-background term in W(H)|s0?
```

## Formal Family

The companion test keeps every unresolved formula coefficient symbolic:

```text
F0 =
    q_Q * Q^TF(B0)
  + q_D * Delta^perp H0
  + q_R * Rperp_0.H0
  + c_H * (R^Y.H0)
  + c_B * (R^Y.B0).
```

A12 does not assert that this is the final EL formula. It is a ledger of the computed background pieces and the
formal coefficients still needed to use them.

## Computed Reduction

The input slots reduce as follows:

| slot | computed value in the A6-A11 convention |
|---|---|
| `Q^TF(B0)` | `0` |
| `Delta^perp H0` | `0` |
| direct `Rperp_0.H0` carrier action | `0` |
| `R^Y.H0` | `(1/8) eta` |
| `R^Y.B0` | `diag(-1, 5, 5, 5) / 32` |

Therefore the computed-slot family is:

```text
F0 = (c_H / 8) eta + c_B * diag(-1, 5, 5, 5) / 32.
```

After base trace-free projection:

```text
TF(F0) = c_B * diag(3, 1, 1, 1) / 32.
```

## Thread A Consequence

Among the computed constant-background slots, the H-class ambient carrier and the already-zero
`Q^TF(B0)`, `Delta^perp H0`, and direct `Rperp_0.H0` carrier action cannot produce a trace-free background
term. The trace-free family is localized to the full-B ambient coefficient `c_B`.

This is useful but deliberately narrow:

```text
If the final EL formula has no full-B ambient slot, or its coefficient is zero, the computed trace-free
background family vanishes. If it has a nonzero full-B coefficient, the A11 shear survives with that
coefficient.
```

The remaining problem is therefore sharper, not closed: pin the actual higher-codimension Willmore-EL
insertion formula/sign and decide whether the final source-action/OQ2-A branch supplies the full-B coefficient.

## Honest Scope

This is a coefficient-family assembly gate, not the full `W(H)|s0` equation. It does not select `c_W`, does not
choose H-class versus II-class, does not run the background-subtracted `M`-linearization, does not move OQ2-A,
and does not change claim status, canon verdicts, scientific status, or public posture.

## Grade

Computation-grade for the formal A6-A11 coefficient-family reduction above. Structural only for implications
to the full higher-codimension Willmore first variation, because the final formula and source-action branch
remain unpinned.
