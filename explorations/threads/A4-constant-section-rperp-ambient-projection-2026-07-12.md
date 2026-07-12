---
title: "A4 -- constant-section Rperp ambient projection"
status: exploration
doc_type: research_note
updated_at: "2026-07-12"
verdict: "AMBIENT_PROJECTION_COMPUTED_NONZERO; FULL_RPERP0_SUPPORT_REMAINS_NONZERO"
depends_on:
  - "explorations/threads/A-higher-codim-willmore-scoping-and-first-swing-2026-07-11.md"
  - "tests/threads/A3_constant_section_normal_curvature.py"
  - "explorations/threads/A3-constant-section-normal-curvature-2026-07-12.md"
companion_test: "tests/threads/A4_constant_section_rperp_ambient_projection.py"
---

# A4 -- Constant-Section Rperp Ambient Projection

Companion test: `tests/threads/A4_constant_section_rperp_ambient_projection.py` (exact SymPy, exit 0).

## Question

Thread A identified the normal-bundle curvature term `Rperp_0` as the high-codimension object missing from the
current Willmore first-variation arc. A3 computed the Ricci-equation shape-operator commutator piece and found
it nonzero.

A4 computes the other Ricci-equation piece at the flat constant section: the ambient `R^Y` normal projection.
The question is whether this ambient term cancels the A3 commutator or leaves a genuine `Rperp_0` background
term.

## Computed Result

Using the block metric of `Y14 = Met(X4)`,

```text
G_ij = h_ij,     G_i alpha = 0,     G_alpha beta = DeWitt_h(S_alpha, S_beta),
```

and the same symmetric-pair convention as A3 (`S_(ab) = E_ab + E_ba` for `a < b`), the exact block-Christoffel
calculation gives

```text
R^Y_{beta alpha i j}
  = -1/4 eta^{km} (S_beta_ik S_alpha_mj - S_beta_jk S_alpha_mi).
```

The audit checks the ambient term against A3's commutator across all ten symmetric-pair normal labels:

| object | nonzero ordered normal-label matrices | nonzero entries |
|---|---:|---:|
| A3 shape-operator commutator | 48 | 96 |
| ambient `R^Y` projection | 48 | 96 |
| full candidate `commutator + ambient` | 48 | 96 |

The support is identical. The ambient term does not cancel the commutator.

A minimal witness:

```text
C_{ij;(00)(01)} =
[[0,  1/8, 0, 0],
 [-1/8, 0, 0, 0],
 [0,    0, 0, 0],
 [0,    0, 0, 0]]

R^Y_{(01)(00)ij} =
[[0, -1/4, 0, 0],
 [1/4,  0, 0, 0],
 [0,    0, 0, 0],
 [0,    0, 0, 0]]

C + R^Y =
[[0, -1/8, 0, 0],
 [1/8,  0, 0, 0],
 [0,    0, 0, 0],
 [0,    0, 0, 0]]
```

The ambient term is not a uniform scalar multiple of the commutator. Across nonzero slots:

```text
ambient / commutator in {-4, -2, 2, 4}
(commutator + ambient) / commutator in {-3, -1, 3, 5}
```

So the ambient projection modifies the coefficients in a signature-sensitive way rather than simply scaling the
A3 tensor.

## Thread A Consequence

The constant-section normal curvature term remains live:

```text
Rperp_0 is nonzero at O(M^0), even after the ambient R^Y projection is added.
```

This strengthens A3's warning. The higher-codimension Willmore first variation cannot use codimension-one
intuition that drops `Rperp`, and it cannot assume the ambient piece cancels the shape-operator commutator.

## Honest Scope

This is not a full first-variation computation and not an OQ2-A selection theorem.

Open after A4:

- assemble the full background `W(H)|_{s0}` using `Delta^perp H0`, Simons stress, the now-computed `Rperp_0`
  support, and the ambient `R^Y . H0/B0` term;
- run the background-subtracted linearization around `s0 + M delta s`;
- then revisit the H-class / II-class OQ2-A choice and the Lambda-shaped background term.

No claim status, canon verdict, public posture, or scientific-status surface changes.

## Grade

Computation-grade for the exact ambient projection at the flat constant section and its combination with A3's
commutator. Structural only for the interpretation that `Rperp_0` remains a mandatory term in the full
higher-codimension Willmore EL.
