---
title: "A3 -- constant-section normal curvature commutator"
status: exploration
doc_type: research_note
updated_at: "2026-07-12"
verdict: "SHAPE_COMMUTATOR_PIECE_COMPUTED_NONZERO; FULL_RPERP0_STILL_OPEN"
depends_on:
  - "explorations/threads/A-higher-codim-willmore-scoping-and-first-swing-2026-07-11.md"
  - "explorations/threads/B-omega0-curvature-dark-energy-scoping-and-first-swing-2026-07-11.md"
  - "tests/threads/A3_constant_section_normal_curvature.py"
  - "tests/threads/B_constant_section_background_curvature.py"
  - "tests/one-residual/willmore_oq2a_functional_selection.py"
---

# A3 -- constant-section normal curvature commutator

## Result

`tests/threads/A3_constant_section_normal_curvature.py` computes the Ricci-equation
shape-operator commutator piece of the constant-section normal curvature gate named in Thread A.

At the flat constant section `s0(x) = (x, eta)` of `Y14 = Met(X4)`, the vertical second fundamental form is

```text
B^V_0{}_{mu nu,ab}
  = -1/2(eta_{a(mu} eta_{nu)b} - 1/2 eta_{ab} eta_{mu nu}).
```

The audit builds the ten shape operators `A_(ab)^i_j = eta^{ik} B0(k,j,ab)` for the symmetric-pair normal
labels `(ab)` and evaluates the Ricci-equation extrinsic commutators

```text
C_{ij;alpha beta} = eta_{i ell} ([A_alpha, A_beta])^ell_j.
```

Findings, all exact:

- `B0` is nonzero: the constant slice is not totally geodesic.
- `H0_ab = (1/2) eta_ab`, agreeing with the Thread A/B `O(M^0)` background object.
- The commutators are antisymmetric in normal labels and, after lowering the tangent index, antisymmetric in
  tangent indices.
- 48 ordered normal-label commutators are nonzero out of 100.
- A minimal witness is

```text
C_{ij;(00)(01)} =
[[0,  1/8, 0, 0],
 [-1/8, 0, 0, 0],
 [0,    0, 0, 0],
 [0,    0, 0, 0]].
```

No perturbation parameter, target count, DESI datum, `24`, `8`, or source-action input appears. This is an
`O(M^0)` geometric background fact from the DeWitt/gimmel constant section.

## Consequence

The higher-codimension Willmore first variation cannot silently drop the normal-bundle curvature term by
codimension-one intuition. Even before the ambient `R^Y` projection is added, the Ricci-equation
shape-operator piece is nonzero.

This directly advances Thread A's open item:

```text
Compute R^perp_0 (normal-bundle curvature of the constant section) via the Ricci equation.
```

What is now computed is the commutator half of that Ricci equation. The remaining half is the ambient
projection term.

## Honest Scope

This is not a full first-variation computation and not a selection theorem for OQ2-A.

Open after this audit:

- add the ambient `R^Y` normal projection to the commutator piece;
- check whether the ambient term cancels, reinforces, or rotates the shape-operator commutator;
- assemble the full `R^perp_0` contribution to the background-subtracted Willmore EL;
- only then revisit the H-class / II-class OQ2-A selection and the Lambda-shaped background term.

No claim status, canon verdict, public posture, or scientific-status surface changes here.

## Grade

Computation-grade for the exact commutator piece. Structural only for the interpretation that this is the
normal-curvature obstruction Thread A named. The full `R^perp_0` and the full higher-codimension first
variation remain open.
