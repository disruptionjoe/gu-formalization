---
title: "A6 -- constant-section Simons stress"
status: exploration
doc_type: research_note
updated_at: "2026-07-12"
verdict: "QTF_B0_TRACE_FREE_ZERO; PURE_TRACE_BACKGROUND_ONLY"
depends_on:
  - "explorations/threads/A-higher-codim-willmore-scoping-and-first-swing-2026-07-11.md"
  - "explorations/threads/A5-constant-section-rperp-invariants-2026-07-12.md"
  - "explorations/threads/B-omega0-curvature-dark-energy-scoping-and-first-swing-2026-07-11.md"
companion_test: "tests/threads/A6_constant_section_simons_stress.py"
---

# A6 -- Constant-Section Simons Stress

Companion test: `tests/threads/A6_constant_section_simons_stress.py` (exact SymPy, exit 0).

## Question

A5 pinned the constant-section normal-curvature tensor `Rperp_0`. The next background assembly still needs
the purely extrinsic Simons / shape-stress contribution:

```text
Q^TF_mn(B) = [ (1/2) H_i hatB^i_mn - (hatB^2)_mn ]^TF.
```

A6 asks whether the constant-section `B0` contributes trace-free background force through this term, or
whether it is only a pure Lambda trace.

## Computed Result

The answer is robust under two normal-contraction conventions:

| contraction | `Q(B0)` before trace-free projection | `Q^TF(B0)` |
|---|---:|---:|
| exact symmetric-pair DeWitt inverse on `Sym^2(T*X)` | `-(9/32) eta_mn` | `0` |
| legacy ordered-index contraction used by older Q-gates | `-(9/16) eta_mn` | `0` |

The coefficient changes by a factor of two because the older ordered-index contraction counts the symmetric
off-diagonal slots differently. The trace-free conclusion does not change.

This is not a vacuous umbilic result. The constant-section `B0` still has nonzero base-trace-free shear, as
Thread B recorded. The new point is narrower:

```text
the purely extrinsic Simons stress of B0 is pure trace.
```

## Thread A Consequence

The background `W(H)|s0` assembly is simpler in one slot:

```text
Q^TF(B0) = 0.
```

So the `B0` Simons / shape-stress term does not add a trace-free background obstruction before the remaining
terms are assembled. It remains Lambda-shaped trace data, not a TT-force term.

Still open after A6:

- assemble `Delta^perp H0`;
- insert the A5 non-null `Rperp_0` term in the actual EL slot;
- assemble the ambient `R^Y . H0/B0` contribution;
- only then do the background-subtracted linearization around `s0 + M delta s` and revisit H-class vs
  II-class.

## Honest Scope

This is not the full higher-codimension Willmore first variation and not an OQ2-A selection theorem. It
computes only the constant-background Simons / `Q^TF` slot.

No claim status, canon verdict, public posture, or scientific-status surface changes.

## Grade

Computation-grade for the exact `Q(B0)` matrices, the vanishing trace-free projections, and the
normalization cross-check. Structural only for the implication to the full background EL assembly.
