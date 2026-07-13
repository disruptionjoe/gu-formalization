---
title: "A10 -- constant-background Rperp / ambient action"
status: exploration
doc_type: research_note
updated_at: "2026-07-13"
verdict: "RPERP0_KILLS_H0; RY_H0_PURE_TRACE; RY_B0_STILL_OPEN"
depends_on:
  - "explorations/threads/A5-constant-section-rperp-invariants-2026-07-12.md"
  - "explorations/threads/A8-constant-section-delta-perp-h0-2026-07-13.md"
  - "explorations/threads/A9-post-a8-background-inventory-2026-07-13.md"
companion_test: "tests/threads/A10_constant_background_rperp_ambient_action.py"
---

# A10 -- Constant-Background Rperp / Ambient Action

Companion test: `tests/threads/A10_constant_background_rperp_ambient_action.py` (exact SymPy, exit 0).

## Construction Used

This gate uses the program-native geometer construction named by the GU instructions:

```text
Y14 = Met(X4), with the gimmel / trace-reversed DeWitt metric on the symmetric-pair normal fiber.
```

It is not using a standard field-theory ambient surrogate. The point is to keep the Thread A objects in the
same convention as A3-A9 before deciding whether any physics-default object is the right next comparison.

## Question

A9 moved `Delta^perp H0` out of the open frontier and named the next honest Thread A computation:

```text
Rperp_0 EL insertion plus ambient R^Y.H0/B0 assembly.
```

A10 computes the part of that frontier whose contraction is already pinned by the A3-A9 convention:

1. the direct normal-curvature endomorphism action of the full A5 `Rperp_0` tensor on the isotropic `H0`
   carrier;
2. the H-class mixed ambient contraction
   `T_alpha = eta^ij R^Y_{alpha i beta j} H0^beta`.

It does not choose the still-unpinned II-class `R^Y.B0` contraction or the scalar Willmore prefactor `c_W`.

## Computed Result

The A5 full normal-curvature tensor remains nonzero:

```text
Rperp_0 has 48 nonzero ordered normal-label matrices.
```

But its direct action on the constant-section mean-curvature carrier vanishes:

```text
Rperp_0(e_i,e_j).H0 = 0  for every tangent wedge (i,j).
```

The mixed ambient H-class contraction is nonzero but pure trace:

```text
eta^ij R^Y_{alpha i beta j} H0^beta = (1/8) eta_alpha = (1/4) H0_alpha.
```

Therefore its base trace-free projection is zero.

## Thread A Consequence

This sharpens the post-A8 boundary:

| slot | A10 status |
|---|---|
| `Rperp_0` tensor | nonzero, from A5 |
| direct `Rperp_0.H0` carrier action | computed zero |
| mixed ambient `R^Y.H0` carrier | computed pure trace |
| trace-free H-class background obstruction from these two carriers | zero |
| II-class `R^Y.B0` contraction | still open |
| `c_W`, full `W(H)|s0`, M-linearization, OQ2-A | still open |

The useful mathematical point is not "the background EL is solved." It is narrower:

```text
the H0 carrier alone does not produce a trace-free background obstruction through the pinned
Rperp_0 and mixed R^Y.H0 contractions.
```

The II-class fork remains live because `B0` still has nonzero base-trace-free shear, so `R^Y.B0` is a
different contraction, not something licensed by the H0 result.

## Honest Scope

This is an exact constant-background carrier gate. It does not assemble the full higher-codimension Willmore
EL, does not choose H-class versus II-class, does not determine `c_W`, does not move OQ2-A, and does not change
claim status, canon verdicts, scientific status, or public posture.

## Grade

Computation-grade for the A3-A9 convention objects above. Structural only for implications to the full
Willmore first variation, because the local `R^Y.B0` / `c_W` formula is still not pinned.
