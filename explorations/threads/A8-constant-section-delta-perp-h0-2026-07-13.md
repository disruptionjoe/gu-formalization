---
title: "A8 -- constant-section Delta-perp H0"
status: exploration
doc_type: research_note
updated_at: "2026-07-13"
verdict: "DELTA_PERP_H0_ZERO_AT_CONSTANT_SECTION; FULL_BACKGROUND_EL_STILL_OPEN"
depends_on:
  - "explorations/threads/A-higher-codim-willmore-scoping-and-first-swing-2026-07-11.md"
  - "explorations/threads/A7-background-assembly-inventory-2026-07-13.md"
  - "explorations/threads/A6-constant-section-simons-stress-2026-07-12.md"
companion_test: "tests/threads/A8_constant_section_delta_perp_h0.py"
---

# A8 -- Constant-Section Delta-Perp H0

Companion test: `tests/threads/A8_constant_section_delta_perp_h0.py` (exact SymPy, exit 0).

## Question

A7 named the first remaining background slot before any honest higher-codimension Willmore EL assembly:

```text
Delta^perp H0
```

where `H0` is the mean-curvature vector of the flat constant section `s0(x) = (x, eta)` in
`Y14 = Met(X4)`.

A8 asks whether the normal-connection Laplacian contributes a nonzero constant-background term, using the
same trace-reversed DeWitt normal metric and symmetric-pair normal basis as A3-A7.

## Computed Setup

The block metric is

```text
G_ij = h_ij,
G_i alpha = 0,
G_alpha beta = DeWitt_h(S_alpha, S_beta).
```

At `h = eta`, the DeWitt normal metric is nondegenerate with signature `(6,4)`, and the constant-section mean
curvature is

```text
H0_ab = (1/2) eta_ab.
```

The relevant block-Christoffel distinction is:

| block | result | consequence |
|---|---:|---|
| `Gamma^beta_{i alpha}` | `0` | normal-normal base connection vanishes |
| `Gamma^k_{i alpha}` | 16 nonzero entries, each `+/-1/2` | ambient derivative has tangential Weingarten part |

So this is not a "constant means zero ambient derivative" shortcut. The ambient derivative of `H0` has
tangential part

```text
(nabla_i^Y H0)^k = -1/4 delta_i^k.
```

The point is narrower: the normal projection vanishes.

## Result

Since `Gamma^beta_{i alpha} = 0` and `H0` is constant in the coordinate symmetric-pair normal frame,

```text
nabla_i^perp H0 = 0
Delta^perp H0 = 0
```

at the flat constant section. The sign convention for the rough normal Laplacian is irrelevant because the
slot is exactly zero.

## Thread A Consequence

A8 closes the first open slot from A7:

```text
Delta^perp H0 contributes no constant-background normal force.
```

The background assembly is therefore narrower, but not finished. Still open:

- insert the A5 `Rperp_0` tensor into the actual Willmore EL slot with the correct coefficient/sign;
- assemble the ambient `R^Y.H0/B0` contribution;
- compute the complete `O(M^0)` background residual `W(H)|s0`;
- only then run the background-subtracted `M`-linearization and revisit H-class vs II-class / OQ2-A.

## Honest Scope

This is a constant-background normal-connection gate only. It does not compute the full first variation, change
claim status, move canon, edit public posture, touch Lean proof files, or touch absorbed source-action or paper
surfaces.

## Grade

Computation-grade for the exact block-Christoffel normal-connection result and the vanishing
`Delta^perp H0` slot. Structural only for how this simplifies the later full background EL assembly.
