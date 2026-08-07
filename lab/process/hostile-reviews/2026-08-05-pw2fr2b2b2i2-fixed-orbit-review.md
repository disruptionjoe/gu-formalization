---
artifact_type: hostile_review
created: 2026-08-05
target: PW2F-R2B2B2I2-S3-FIXED-ORBIT-FULL-EVALUATOR
verdict: PASS_AT_COMPLETE_FIXED_ORBIT_STRATUM_ONLY
reviewers:
  - finite-group action and orbit-stabilizer lens
  - moving Hodge and mixed-jet lens
  - coverage and computational reproducibility lens
  - source fidelity and Layer-0 lens
---

# R2B2B2I2 fixed-orbit hostile review

## Final verdict

`PASS_AT_COMPLETE_FIXED_ORBIT_STRATUM_ONLY`.

The packet durably certifies every one-cell S3 orbit through the full mixed
evaluator. It covers `2/380` representatives, not the remaining `378`, and
cannot promote the reduction engine or either coefficient bank.

## Finite-action and stabilizer lens

The canonical resolver returns the durable 1,925-label grid, 380 canonical
representatives, and exactly the two preregistered one-cell orbits. Both labels
are fixed by all six S3 elements. The reflection and three-cycle therefore
exercise four nontrivial self-transport edges rather than moving to new labels.

Lens verdict: `PASS`.

## Moving Hodge and mixed-jet lens

All four jet slots pass for geometry, `Phi1`, `Phi2`, Hodge, Shiab residual,
moving primalizer, and action on both generator edges and both fixed labels:
`16/16` per layer. The mixed residual, primalizer, and action are live on both
cells. The moving-Hodge correction differs from a frozen Hodge on both cells,
and the order-three edge rejects the obsolete forward-lift convention.

Lens verdict: `PASS_NONVACUOUS`.

## Coverage and reproducibility lens

The durable probe collapses the scratch algorithm onto three byte-pinned owner
dependencies and reproduces exact mixed actions `215/8` and `87/16` under
pinned SymPy `1.14.0` plus NumPy. The raw equality count is 112 with zero fitted
parameters, but independent constraint rank is not established and no surplus
claim is made.

The complete fixed stratum is scientifically useful as the first full
evaluator orbit class. It is only `2/380`, so calling it universal coverage
would be a 190-fold scope inflation by representative count.

Lens verdict: `PASS_AT_2_OF_380_ONLY`.

## Source and Layer-0 lens

The active finite reduction is repository-derived and source-silent. Active
`(9,5)` and public `(7,7)` presentations remain distinct. A fixed-orbit full
evaluator certificate does not assemble a bank, close Green/Helmholtz, or
transfer a physics label.

Lens verdict: `PASS`.

## Boundary

The remaining 378 representatives, dense universal held-outs, both complete
banks, Green/Helmholtz, domain, observation, and physics remain open. The
1,925-cell fallback stays live. P1/P2/P3 remain unchanged and unused. Curt
remains `FORMALLY_SEPARATE_INSIDE_ERIC_LANE`. `TG-1 AND TG-2 AND TG-3`
remains `NOT_PROMOTED`. No canon, protected status, public posture,
publication, datum, or physics state changes.
