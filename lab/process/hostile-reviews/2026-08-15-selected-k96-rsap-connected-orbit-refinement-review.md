---
title: "Hostile review: K96 connected-orbit normalizer refinement"
status: complete
reviewed_artifact: explorations/conditional-build/selected-k96-rsap-connected-orbit-refinement-2026-08-15.md
created: "2026-08-15"
verdict: PASS_CONNECTED_REFINEMENT_AND_CLASSICAL_98D_RSAP__PHYSICAL_SELECTION_OPEN
---

# Hostile review

## Determinant mistaken for the component group attack

`O(7,7)` has four components, not two. K96 uses the independent orientation
signs on the positive and negative maximal-compact factors. Positive- and
negative-coordinate reflections realize `(-,+)` and `(+,-)` separately; their
product realizes `(-,-)`. Determinant is recorded only as their product.

## Normalizer representative does not preserve the complement attack

The representatives are diagonal in the fixed `R_0` eigenspace decomposition.
They commute with `R_0`, so if `R_0Y+YR_0=0`, the same identity holds after
conjugation. The exact probe checks all `49` basis directions.

## One structural representative mistaken for every connected orbit attack

K96 does not infer connected coverage from one representative. Given an
arbitrary `o` in any ambient component, it chooses a normalizer element `k` in
that same component. Then `ok^-1` lies in `SO_0(7,7)` and carries the
still-balanced point `kYk^-1` to `oYo^-1`. This explicitly reaches every
connected refinement. Centralizer components may merge labels but cannot
create an uncovered label.

## Surjectivity without regular submersivity attack

K88, K89 and K90 independently cover regular semisimple, principal nilpotent
and regular nonsemisimple classes at map rank `91`. Uniformly, a regular point
of this full-rank symmetric complement has a seven-dimensional centralizer in
the complement and zero `h_bal` centralizer. Surjectivity therefore combines
with full regular-locus differential rank, as RSAP requires.

## RSAP confused with all-charge submersion attack

The horn has rank `49` over zero, not `91`. It is an RSAP precisely because
rank loss on singular strata is allowed. The exact `98D` RSAP minimum and the
separate `182D` everywhere-submersive all-charge minimum remain explicit.

## Mathematical carrier promoted to physics attack

Nothing in the component argument selects `H_bal` from Weinstein's source
action, performs BFV reduction, establishes positivity or quantizes the
carrier. At K96 the action-parent attachment was not composed. Successor K97
later constructs the formal attachment as a right-`H_bal` zero reduction of
the action-owned epsilon cotangent parent, while proving that the current bare
action still does not select the constraint or gauge quotient. Physical
attachment remains open.

## Verdict

Accept the uniform connected-orbit refinement, global classical surjectivity,
and exact `98D` RSAP minimum. Retire further component-by-component census
work. Successor K97 closes the formal action-parent reduction but not action
selection or physical attachment; do not promote the mathematical carrier to
a physical GU phase space.
