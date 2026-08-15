---
title: "Hostile review: RSAP zero-charge balanced symmetric horn"
status: complete
reviewed_artifact: explorations/conditional-build/selected-k88-rsap-zero-charge-symmetric-mixed-cartan-horn-2026-08-15.md
created: "2026-08-15"
verdict: PASS_SELECTED_MIXED_CARTAN_AND_ALL_REGULAR_SEMISIMPLE_TYPES__SINGULAR_COVERAGE_OPEN
---

# Hostile review

## A 49D Lagrangian subspace disguised as a subgroup attack

The stabilizer is the connected closed symmetric subgroup `H_bal` with Lie
algebra `so(3,4)+so(4,3)`, not an arbitrary subspace. Its finite central
quotient is immaterial to the Lie-algebraic rank calculation. The exact basis verifies
`[h,h]`, `[h,p]`, and `[p,p]` closure and `h^perp=p`.

## Same dimensions as the killed K87 horn attack

Dimension arithmetic is not the positive result. K87's nilradical has the
same `42/49/98` counts but misses every mixed/elliptic regular Cartan. The
balanced complement contains full Cartan subalgebras of types `(7,0)`,
`(5,2)`, `(3,4)`, and `(1,6)` and has trivial `h`-centralizer intersection at
the exact regular witnesses.

## One planted `(5,2)` matrix attack

The construction contains the entire representative `(5,2)` Cartan
subalgebra. Conjugacy of real Cartan subalgebras within that type then places a
conjugate of every regular `(5,2)` charge in the image. Exact distinct weights
verify centralizer dimension seven and map rank `91`.

## Dense regular set implies zero neighborhood attack

False. Regular-semisimple coverage does not settle regular nilpotent,
singular, or mixed Jordan orbits. Because `Ad(G)p` is conic, one missed orbit
kills the zero-neighborhood claim for this horn. The result remains a survivor
to a signed-Young-diagram and mixed-Jordan census, not an RSAP.

## Unbalanced decomposition control

The `(7,0)|(0,7)` complement supports split blocks only. The
`(2,5)|(5,2)` complement supports at most four compact blocks and therefore
misses type `(1,6)`. These controls show why the balanced `(3,4)|(4,3)` split,
not rank arithmetic alone, supplies all four types.

## Wrong-sign and repeated-weight controls

Flipping the metric-adjoint sign fails the `so(7,7)` identity. Reusing a
matching target breaks commutativity; equal weights enlarge the centralizer
and lower adjoint rank. The certificate rejects all three.

## Source-selection attack

The homogeneous model is canonical after choosing `H`; the source does not
choose `H`. No boundary, BFV, positivity, cohomology, physical phase-space, or
ambient-`A3` conclusion follows.

## Verdict

Accept the `98D` zero-rank and complete regular-semisimple real-Cartan
construction, including the selected `(5,2)` gate. Require the exact
anticommuting-involution orbit census before any zero-neighborhood,
surjectivity, or RSAP claim.
