---
title: "K485--K488 Order-Ten Face Preconditioner Programs"
status: conditional_research_result
doc_type: exploration
updated_at: "2026-09-25"
direction: observed_to_native
---

# K485--K488 order-ten face preconditioner programs

## Question

Can K411's complete atlas of reachable order-ten hybrid faces be converted
into exact singular/confluent preconditioner programs, checked for local
face-normal integrability, and exercised through the complete coherent Arb
functional without evaluating the raw Bessel representation at a zero?

## Exact compilation

K485 replays all 13,300 ordered K407 descriptors on all 936 K411 reachable
faces.  Their 49,544,352 determinant-matrix uses resolve into the same exact
60 singular zero-mask templates and 75 confluent divided-difference templates
that appear in the lower-order compiler.  The largest determinant rank is
five and the largest required row or column divided-difference order is four.
The result is an exact mask-native preconditioner bank, not a numerical face
evaluator.

K486 composes that bank with K410's order-ten radial powers.  It performs
12,448,800 ordered descriptor-face replays and emits one normal-power record
for every reachable face.  The global minimum second-derivative face-normal
power is zero and the all-zero face power is nine, so every recorded normal
exponent is strictly greater than minus one.  This closes local power-counting
integrability on the complete reachable-face atlas.  It does not bound the
tangential variables or integrate any face neighborhood.

K487 compiles the 936 records into executable positive-approach programs.  It
resolves every one of the 12,448,800 descriptor-face programs and every one of
the 49,544,352 determinant-matrix programs to an exact K485 template.  One
hardest reachable-face program is selected for each of the first twenty
hybrids; `v10` and `v11`, which have no reachable faces in K411, receive
explicit positive-interior fallback programs.  Each program uses normal
levels `1/1024`, `1/2048`, and `1/4096` and keeps all cumulative Bessel
arguments positive.

## Certified approach controls

K488 executes the selected program for all 22 hybrids at all three normal
levels with python-flint/Arb at 180 decimal digits and one thread.  For each
control it assembles all 13,300 ordered descriptors and all 28 coherent groups
before applying either K486's normal scaling or K410's quadratic Peano
majorant.  The 66 controls therefore represent 877,800 ordered
descriptor-control evaluations.  The release gate requires every enclosure
to be finite, every group digest to be present, and every cumulative argument
floor to be strictly positive.

These are point controls along positive approaches.  They are not intervals
over a face, and the program compiler does not replace the missing
row/column-scaled confluent interval implementation.

## Hostile interpretation review

The strongest contrary interpretation is that a nonnegative normal power and
finite values on three approach points establish the complete hybrid
integral.  They do not.  A locally integrable asymptotic exponent can coexist
with arbitrarily loose tangential or recursive majorants, and three positive
points do not enclose even one face cell.  The present artifacts establish an
exact finite preconditioner/program interface and exercise its coherent
numerical backend; they do not establish a cover or a global error budget.

The weakest seam is the transition from template pointers to genuine interval
cells.  K485 supplies the required singular and confluent templates, but K488
still evaluates the ordinary complete coherent functional at positive
approach points.  A future face evaluator must apply the row/column scaling
and divided differences over interval cells themselves and prove outward
enclosure across all tangential directions.

## Next exact input

Implement the K485 row/column-scaled confluent interval evaluator, execute it
on all 936 K487 face programs, construct the recursive positive-interior cover,
and join its finite-cell error with K410's analytic radial tails.  Only a
complete order-ten hybrid integral can then feed the still-unevaluated K457
cross packet.  K457's value, a K162 complete-complement packet, and a K152
native interval all remain open.  No source, ledger, canon, paper, public,
novelty, or physical conclusion moves.
