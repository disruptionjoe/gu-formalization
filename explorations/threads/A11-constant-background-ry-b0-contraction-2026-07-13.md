---
title: "A11 -- constant-background RY.B0 contraction"
status: exploration
doc_type: research_note
updated_at: "2026-07-13"
verdict: "FULL_B_CONTRACTION_HAS_TRACE_FREE_SHEAR"
depends_on:
  - "explorations/threads/A8-constant-section-delta-perp-h0-2026-07-13.md"
  - "explorations/threads/A9-post-a8-background-inventory-2026-07-13.md"
  - "explorations/threads/A10-constant-background-rperp-ambient-action-2026-07-13.md"
companion_test: "tests/threads/A11_constant_background_ry_b0_contraction.py"
---

# A11 -- Constant-Background RY.B0 Contraction

Companion test: `tests/threads/A11_constant_background_ry_b0_contraction.py` (exact SymPy, exit 0).

## Construction Used

This gate stays inside the program-native GU construction:

```text
Y14 = Met(X4), with the gimmel / trace-reversed DeWitt metric on the symmetric-pair normal fiber.
```

It is not using a standard field-theory ambient substitute. The point is to continue the A3-A10 convention
long enough to isolate the next background contraction before any comparison to another construction.

## Question

A10 showed that the trace-only H-class carrier has no trace-free background obstruction:

```text
eta^ij R^Y_{alpha i beta j} H0^beta = (1/8) eta_alpha.
```

A10 left the II-class fork open because the full second fundamental form `B0` still has nonzero base-trace-free
shear. A11 computes the natural full-SFF mixed ambient comparison:

```text
eta^{ik} eta^{jl} R^Y_{alpha i beta j} B0_{kl}^beta.
```

## Computed Result

In normal-lower matrix form, the full-SFF contraction is:

```text
RY.B0 = diag(-1, 5, 5, 5) / 32.
```

Its Lorentz trace is `1/2`, so the pure-trace part is:

```text
(1/8) eta = RY.H0.
```

The trace-free remainder is nonzero:

```text
TF(RY.B0) = diag(3, 1, 1, 1) / 32.
```

Thus the full-B contraction is not proportional to `H0`; it is the A10 H-class trace carrier plus a genuine
trace-free shear component.

## Thread A Consequence

This sharpens the remaining background-assembly boundary:

| slot | A11 status |
|---|---|
| direct `Rperp_0.H0` carrier action | computed zero in A10 |
| mixed ambient `R^Y.H0` carrier | computed pure trace in A10 |
| natural mixed ambient `R^Y.B0` full-SFF contraction | computed nonzero trace-free shear |
| final `Rperp_0` EL insertion formula/sign | still open |
| scalar prefactor `c_W` and full `W(H)|s0` assembly | still open |
| background-subtracted `M`-linearization and OQ2-A | still open |

The useful result is narrow:

```text
the trace-only H0 result does not license dropping the full II-class ambient contraction.
```

## Honest Scope

This is an exact constant-background contraction gate. It does not assemble the full higher-codimension
Willmore EL, does not choose H-class versus II-class, does not determine `c_W`, does not move OQ2-A, and does
not change claim status, canon verdicts, scientific status, or public posture.

## Grade

Computation-grade for the A3-A10 convention object above. Structural only for implications to the full
Willmore first variation, because the final EL insertion formula and scalar prefactor are still not pinned.
