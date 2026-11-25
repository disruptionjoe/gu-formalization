---
title: Independent chiral transport — internal acceptance
status: process
doc_type: review
created: '2026-11-25'
---

# Acceptance and exact scope

Internal T1 acceptance of the local, fixed-observation and paired-adjoint
realization-class theorem. The author, two separately prompted mathematical
reviewers, and a hostile source/analytic reviewer worked from the pinned
`696c7df10315c72bd8dbfb890b86cbf7f69e8a68` evidence and the concrete draft.
These are simulated specialist agents, not independent human scientists.
No reviewer ran a test or build; root serialized every execution below.

## Independent mathematical findings

1. **Clifford representation/operator-adjoint reviewer:** independently expanded
   the actual August11 wedge matrix, checked all ordered coefficient rows with
   chirality-mixing K, classified the full unitary normal solution, and derived
   the normal F/tangent even-Clifford commutant solution. Identified eta-slot
   coordinates, LC-versus-varied-connection parallelism, integration-density
   versus fibre-metric weighting, and whole-operator adjoint limitations.
   All four qualifications are explicit in the accepted proof.
2. **Geometric PDE/Clifford-adjoint reviewer:** independently checked actual
   kernel preservation, full time invertibility and induced normalized q;
   rederived the general-m normal identity, null-safe evaluation faithfulness,
   b=H necessity/sufficiency and tangent commutant equivalence. Re-read the
   revised proof and expanded control source; accepted without material issue.
   The reduced complex-null control is not a native real-null computation;
   the universal proof covers real null vectors without division by v².
3. **Hostile source/analytic reviewer:** confirmed this closes the exact
   independent-chiral gap left open by November13, rather than repeating its
   scalar calculation. Required explicit integration measure versus varying
   fibre metric, and noted that adding f|section=0 also fixes tangential df.
   Both corrections are integrated. Candidate source grammar, effective versus
   exact off-shell chirality, independent bars, K77/K95 and missing physical
   domain/count remain distinct. Accepted at this scope.

## Executed verification

- 61 exact SymPy1.14 controls, including ordered arbitrary chirality-mixing
  unitary rows; wrong coefficient order; asymmetric-weight time inversion and
  hidden-kernel preservation; b=H success and b≠H failure; nonunitary copied-arrow
  escape outside U; H=0 with nonzero traceless II; indefinite eta-slot and q
  coordinate transport with an intentionally wrong raw q; complex-null
  evaluation; and separate K77/K95 crossed-relation arithmetic.
- The n4/m3 and n4/h2/m2 matrices are reduced algebraic controls, not native
  signature, dimension, physical positivity or source-adjoint certification.
- Five declarations in `Lean/GUFormalization/ChiralWeightTransport.lean` check
  the conditional arithmetic residual, dimension10 obstruction/equality,
  equality through a supplied faithful evaluation, and consistent abstract
  density rows. Pinned `lake env lean -j1` module and updated root both pass.
  Clifford representation, Hermitian pairing, geometric identities, evaluation
  faithfulness, source necessity and analytic domains remain outside Lean.

## What is accepted, and what remains open

The whole declared two-weight/compatible-connection class has fixed-adjoint
transport exactly at H=0. Its pre-existing weighted-integration-density rival
has transport exactly at b=H, with every compatible connection specified.
For the retained nonzero H reconstruction this excludes the first realization
class; it leaves the second as a typed candidate. No source claim, physical
ledger row, classC definition or scientific matrix status changes. No guessed
action or new source operator was constructed. LC evidence requires the normal
B-lane rederivation before scientific matrix absorption.

[Universal proof](../../../explorations/conditional-build/bet-2plus1-chiral-weight-transport-2026-11-25.md),
[exact results](../bet-2plus1-chiral-weight-transport.json).
