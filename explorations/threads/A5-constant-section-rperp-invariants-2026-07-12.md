---
title: "A5 -- constant-section Rperp invariants"
status: exploration
doc_type: research_note
updated_at: "2026-07-12"
verdict: "FULL_RPERP0_DEWITT_NON_NULL; A3_A4_SPLIT_ORTHOGONAL"
depends_on:
  - "explorations/threads/A-higher-codim-willmore-scoping-and-first-swing-2026-07-11.md"
  - "explorations/threads/A3-constant-section-normal-curvature-2026-07-12.md"
  - "explorations/threads/A4-constant-section-rperp-ambient-projection-2026-07-12.md"
companion_test: "tests/threads/A5_constant_section_rperp_invariants.py"
---

# A5 -- Constant-Section Rperp Invariants

Companion test: `tests/threads/A5_constant_section_rperp_invariants.py` (exact SymPy, exit 0).

## Question

A3 computed the shape-operator commutator piece of the constant-section normal curvature term. A4 added the
ambient `R^Y` normal projection and showed that the full support remains nonzero.

A5 asks the next invariant question needed before the background `W(H)|s0` assembly:

```text
Is the full commutator-plus-ambient Rperp_0 tensor non-null under the actual DeWitt normal metric?
```

## Metric Convention

The normal bundle is represented by the symmetric-pair basis used in A3/A4:

```text
S_(ab) = E_ab + E_ba  for a < b,
S_(aa) = E_aa.
```

The normal metric is the trace-reversed Frobenius/DeWitt pairing at `h = eta`:

```text
V(S,T) = tr(eta^-1 S eta^-1 T) - (1/2) tr(eta^-1 S) tr(eta^-1 T).
```

In this basis the metric is nondegenerate with determinant `64` and signature `(6,4)`, matching the GU
gimmel fiber.

## Computed Result

Using tangent indices raised by `eta` and normal labels raised by the inverse DeWitt metric, the raw scalar
contractions are:

| tensor | raw contraction |
|---|---:|
| A3 shape commutator | `27/64` |
| A4 ambient projection | `9/4` |
| cross term | `0` |
| full `commutator + ambient` | `171/64` |

Thus the full constant-section `Rperp_0` tensor is not merely support-nonzero. It is non-null under the
metric contraction that the eventual background Willmore-EL assembly has to respect.

The A3 and A4 pieces are also orthogonal under this contraction:

```text
<commutator, ambient> = 0,
<full, full> = <commutator, commutator> + <ambient, ambient> = 171/64.
```

The coefficient structure remains signature-sensitive, not a uniform rescaling. The nonzero full entries are
exactly

```text
{-3/8, -5/16, -3/16, -1/8, 1/8, 3/16, 5/16, 3/8}.
```

Each tangent two-plane sees a rank-6 normal-curvature skew matrix, and the six tangent wedge components are
linearly independent as normal-curvature matrices.

## Thread A Consequence

The `Rperp_0` background term is now pinned more strongly:

```text
Rperp_0 is nonzero in support and non-null under the DeWitt/tangent contraction.
```

This makes it harder for the full higher-codimension Willmore first variation to treat the normal-curvature
background as a removable codimension-one artifact. The next missing work is no longer "is `Rperp_0` real?"
It is the actual assembly of the remaining background terms.

## Honest Scope

This is not a full first-variation computation and not an OQ2-A selection theorem.

Still open after A5:

- assemble `Delta^perp H0`;
- assemble the Simons / shape-stress contribution on the constant background;
- combine those terms with the now-invariant `Rperp_0` and ambient `R^Y . H0/B0` pieces;
- only then run the background-subtracted linearization around `s0 + M delta s` and revisit H-class vs
  II-class.

No claim status, canon verdict, public posture, or scientific-status surface changes.

## Grade

Computation-grade for the exact DeWitt normal metric, the contractions, the orthogonality result, and the
rank/span checks. Structural only for the implication to the full higher-codimension Willmore EL.
