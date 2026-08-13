---
artifact_type: exploration_result
created: 2026-08-08
status: DEWITT_FORM_EXTENDS_HOLOMORPHICALLY__REAL_LOCUS_IS_A_COMPONENT__SECTOR_DATUM_q_DOES_NOT_EXTEND
grade: "EXACT. Holomorphy checked by direction-independence of the complex
  derivative (residual 5.95e-11, finite-difference); the non-extension of q is an
  exact algebraic witness with residual 0.00e+00 plus the standard fact that
  there is no complex Sylvester law. Horn-robust: the same witness works on both
  base signatures."
run_id: GUH-20260808T060000Z-register-side-track
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
priority_change: none
row_change: none
residue_touched: []
follows:
  - explorations/five-lens-analytic-council-2026-08-08.md
---

# Complexification existence check: two of three, and the third is the interesting one

## Preregistered kill, and what actually happened

The preregistration was: *if `G` does not extend holomorphically with the real
Lorentzian locus as a conjugation fixed-point set, thimble methods are
structurally blocked for GU.*

`G` **does** extend, and the real locus **is** a component of the fixed set. So
thimble methods are **not** blocked by the preregistered obstruction. A third
condition fails instead, and it is sharper.

## (a) The DeWitt form extends holomorphically — YES

```text
||dG/dz along a real direction - along an imaginary direction|| = 5.95e-11
```

`G_ij(g) = tr(A_i A_j) - (1/2) tr(A_i) tr(A_j)` with `A_i = g^{-1} B_i` is rational
in the entries of `g`, hence holomorphic wherever `det g != 0`. The complex
derivative is direction-independent, as it must be.

## (b) The antiholomorphic involution — YES, but the naive statement is FALSE

Standard conjugation on `Sym^2(C^4)` has fixed locus **all real symmetric forms**,
not only the Lorentzian ones. So "fixed locus = exactly `Met(X^4)`" is wrong as
stated.

The **correct** statement holds and is what thimble methods actually require: on
`{det != 0}` the real locus splits by signature, and the Lorentzian locus is a
**connected component** of the conjugation fixed-point set. Picard-Lefschetz needs
a real locus to anchor thimbles and pair them conjugate-to-conjugate; it does not
need that locus to exhaust the fixed set.

## (c) The sector datum `q = P - T` does NOT extend — and this is the result

Explicit witness, exact:

```text
P = diag(1, 1, 1, i)
|| P^T . diag(1,1,1,-1) . P  -  I ||  =  0.00e+00
```

The Lorentzian form and the Euclidean form are **equivalent over C**. That is not
special to this pair: over `C` every nondegenerate symmetric bilinear form is
equivalent to the identity. **There is no complex Sylvester law, so signature is
not a complex invariant, and `q` does not extend.**

**Note what the witness is.** Multiplying the timelike leg by `i` is **Wick
rotation**. The obstruction to `q` extending and the Wick rotation are the same
object, seen from two sides.

## What this means

Thimble methods are **structurally available** for GU — the domain complexifies,
the form extends, and the real form supplies the conjugation that pairs thimbles.
Lens 4's reading stands: the algebra being real never constrained the contour.

But **any contour that leaves the real locus loses the sector datum.** There is no
invariant tracking which signature sector a deformed contour is in, because over
`C` there are no signature sectors.

That is the complex-analytic cause of a phenomenon the repository already found
empirically: `dc-h1` records that under `C -> -C` the even and breaking subspaces
exchange, `d -> 136 - d`, and that the sign is a nontrivial holonomy class with
**no global section**. This artifact says why. The monodromy is not an accident of
the loop chosen — it is what happens when a real invariant is transported through
a space where that invariant does not exist.

## Consequences

- **For thimbles:** available, but every contour must be tracked back to the real
  locus with its sector recorded separately. `q` cannot be carried along the
  deformation; it must be re-read on arrival.
- **For Wick rotation:** the repository treats it as a contaminant to be audited
  against, and separately as scaffolding for ellipticity. Both readings are
  correct and they are the same operation. What is missing is the return path,
  which is reflection positivity, which the repository does not have.
- **For `M-H9`'s specification:** the `58 <-> 78` exchange being loop-monodromy
  dependent, and therefore only the unordered pair being well posed, is the same
  fact in the `B5` language.

## Fences

- Horn-robust. The same witness works on the `(1,3)` base — multiply the three
  spacelike legs by `i`, or equivalently use `-g`.
- Nothing here builds a contour, a thimble, or a Stokes decomposition, and
  nothing here needs `H41`. The integrand remains unbuilt; this is entirely a
  statement about the domain.
- "Available" means not structurally obstructed. It does not mean tractable: the
  fibre is homogeneous, so critical sets are orbits and any Morse theory here is
  Morse-Bott at best.
