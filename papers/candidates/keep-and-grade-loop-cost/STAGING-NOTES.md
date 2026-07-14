# Staging Notes: keep-and-grade-loop-cost

**Candidate:** `keep-and-grade-loop-cost-2026-07-11.md`

## Scope

GU-independent structural packet for the loop-level cost of keep-and-grade fourth-order gravity. The candidate
maps the loop-positivity problem across grading-based and removal-based constructions:

1. The one-loop Cutkosky branch shows that a stable Krein-graded ghost leaks a negative physical-subspace
   contribution unless the ghost is removed or complexified.
2. The PT/`C`-operator branch supplies a positive metric at the price of non-locality.
3. Fakeon and Lee-Wick branches remove the ghost from cuts at the price of bounded micro-causality or contour
   prescription costs.
4. The no-local-positive-metric theorem proves, for the free fourth-order / Pais-Uhlenbeck field, that a local
   positive metric is not available; the canonical positive metric is non-local but exponentially localized at
   the ghost scale.

The July 13 updates sharpen the same boundary. `tests/W120` separates the graded fixed-order answer from CLOP
order-of-limits ambiguity. `tests/W121` hardens the local-positive-metric hypothesis audit. `tests/W124_stageA`
and `tests/W124_stageB` move the two-loop scalar-core Lee-Wick/CLOP comparison forward while leaving spin-2
tensor numerators and full Euclidean continuation open.

## Honest grade

**Structural loop-cost map with one theorem-grade free-case anchor.** The free no-local-positive-metric result is
the strongest mathematical core, supported by `tests/W54_path2_target3_no_local_metric.py` and hardened by
`tests/W121_path2_target3_hypothesis_hardening.py`. The one-loop cut, fakeon, Lee-Wick, RG-contingency, and
asymptotic-freedom grading checks are bounded construction results, not an all-orders loop-unitarity theorem.

The candidate does not claim that keep-and-grade loop positivity is solved, that fourth-order gravity is proven
unitary, that GU is established, or that the remaining conformal-sector and interacting-metric questions are
closed. Its contribution is the priced map: positivity/locality/causality cannot all be retained in the tested
branches, and the remaining costs are explicitly localized.

## Light staging gate (per `papers/candidates/README.md`)

1. Title matches the theorem-grade core: PASS. "Loop-Level Cost Structure" advertises a cost map rather than a
   completed unitarity proof.
2. No retracted or downgraded wording: PASS WITH GRADE BOUNDARY. The candidate names the tree/QM-to-loop gap,
   the open all-orders interacting metric, the conformal-factor subtlety, and the remaining two-loop tensor /
   continuation work.
3. External citations resolve: PENDING. The packet names the relevant prior-work families (Stelle,
   Bender-Mannheim, Mostafazadeh, Anselmi-Piva, Lee-Wick, Donoghue-Menezes, Grinstein-O'Connell-Wise, Kuntz,
   Nakayama, and related fourth-order-gravity literature), but this staging pass did not verify every
   bibliographic detail against primary sources.
4. Sharpest open issue acknowledged in-text: PASS. The status section and July 13 updates name the all-orders
   interacting metric, the conformal-factor mode, the spin-2 tensor numerator, and Euclidean-continuation
   residuals.
5. Overlap with other staged candidates: DELINEATED. `uv-structure-fourth-order-gravity/` uses this loop-cost
   map as one part of a broader UV synthesis. This folder isolates the positivity-vs-locality/causality price of
   keep-and-grade fourth-order gravity itself.

## Open items (ranked)

1. Close or explicitly bound the all-orders interacting positive-metric question beyond the free theorem and
   perturbative arguments.
2. Decide how the conformal-factor mode should be treated in the physical theory, rather than relying on
   spin-2-sector stability alone.
3. Complete the spin-2 tensor numerator and finite-width Euclidean-continuation review for the two-loop
   Lee-Wick/CLOP branch.
4. Verify all external citations and prior-art deltas before any public posting.

## Before posting

Keep this as a staged candidate until the open loop-positivity frontiers and citation checks are tight enough
for Joe's chosen publication path. Any submission, upload, DOI/tag/release action, publication move, or
public-posture change remains Joe-gated.
