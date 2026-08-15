---
title: "Hostile review: RSAP zero-charge balanced symmetric horn"
status: complete
reviewed_artifact: explorations/conditional-build/selected-k88-rsap-zero-charge-symmetric-mixed-cartan-horn-2026-08-15.md
created: "2026-08-15"
verdict: PASS_ALL_TEN_REGULAR_SEMISIMPLE_CARTAN_TYPES__SINGULAR_COVERAGE_OPEN
---

# Hostile review

## A 49D Lagrangian subspace disguised as a subgroup attack

The stabilizer is the connected closed symmetric block stabilizer `H_bal`, not
an arbitrary subspace. Its Lie algebra is `so(3,4)+so(4,3)` and globally it is
the image of `(Spin_0(3,4)xSpin_0(4,3))/diagonal Z2`; the literal direct product
would miss the finite kernel. The exact basis verifies `[h,h]`, `[h,p]`, and
`[p,p]` closure and `h^perp=p`.

## Same dimensions as the killed K87 horn attack

Dimension arithmetic is not the positive result. K87's nilradical has the
same `42/49/98` counts but misses every mixed/elliptic regular Cartan. The
balanced complement contains exact regular witnesses in all ten orthogonal
Cartan spectral classes and has trivial `h`-centralizer intersection at each.

## Four-type or seven-signature exhaustion attack

The four pure matching rows cover only the classes with no loxodromic
four-plane. Adding one loxodromic block fills the missing odd compact ranks,
but seven split/compact signatures still do not exhaust conjugacy classes:
loxodromic count distinguishes two `(5,2)` classes, two `(3,4)` classes, and
two `(4,3)` classes. The hardened certificate constructs all ten admissible
`(H,E,L)` triples satisfying `H+2E+2L=7`, including controls with two and three
disjoint loxodromic blocks.

## One planted `(5,2)` matrix attack

The construction contains the entire representative non-loxodromic `(5,2)`
Cartan subalgebra selected by the action-owned endpoint. Conjugacy within that
spectral class then places a conjugate of every regular charge in the class in
the image. A separate two-loxodromic `(5,2)` control covers the other class.
Exact distinct weights verify centralizer dimension seven and map rank `91`.

## Dense regular set implies zero neighborhood attack

False. Regular-semisimple coverage does not settle regular nilpotent,
singular, or mixed Jordan orbits. Because `Ad(G)p` is conic, one missed orbit
kills the zero-neighborhood claim for this horn. The result remains a survivor
to a signed-Young-diagram and mixed-Jordan census, not an RSAP.

## Unbalanced decomposition control

The `(7,0)|(0,7)` complement supports split blocks only. The
`(2,5)|(5,2)` complement supports at most four compact blocks and therefore
misses type `(1,6)`. These controls show why the balanced `(3,4)|(4,3)` split,
not rank arithmetic alone, supplies all ten spectral classes.

## Wrong-sign and repeated-weight controls

Flipping the metric-adjoint sign fails the `so(7,7)` identity. Reusing a
matching target breaks commutativity; equal weights enlarge the centralizer
and lower adjoint rank. The certificate rejects all three.

## Source-selection attack

The homogeneous model is canonical after choosing `H_bal`; the source does not
choose `H_bal`. No boundary, BFV, positivity, cohomology, physical phase-space,
or ambient-`A3` conclusion follows.

## Verdict

Accept the `98D` zero-rank and complete ten-class regular-semisimple
real-Cartan construction, including the selected non-loxodromic `(5,2)` gate.
Require the exact
anticommuting-involution orbit census before any zero-neighborhood,
surjectivity, or RSAP claim.
