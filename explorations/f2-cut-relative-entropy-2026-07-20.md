---
title: "F2 cut relative entropy: bounded negative at toy grade"
status: active_research
doc_type: exploration
created: 2026-07-20
owner_item: CONSTRUCTION-SPACE-EXPLORATION
lane_id: "1"
extends:
  - explorations/intake-bianconi-entropic-gravity-2026-07-20.md
  - explorations/sig-b5-f2-f5-shadow-2026-07-20.md
runnable:
  - tests/channel-swings/f2_cut_relative_entropy_probe.py
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
external_action: none
---

# F2 cut relative entropy: bounded negative at toy grade

## Question

The Bianconi intake named a cheap probe: normalize the two deck-exchanged,
Krein-compatible F2 cuts as density matrices and ask whether their quantum
relative entropy gives a nonzero, scale-bearing, holonomy-odd functional for
the B.5 cut-scale slot.

At the existing finite F2 shadow grade, the answer is **no**. This is a local
negative about that proposed functional, not a no-go for an entropy mechanism
on an actual boundary family.

## Construction fork

- **Program-native object used first:** the F2 cuts are the maximal
  K-definite, Dirac-invariant subspaces represented by complementary
  Krein-orthogonal projectors `Q_+` and `Q_-`. These are K-self-adjoint but
  oblique in the positive Hilbert inner product. They are not positive
  Hermitian density matrices, so Umegaki relative entropy is not natively
  defined on `Q_+ / tr(Q_+)` and `Q_- / tr(Q_-)`.
- **Standard-physics import checked explicitly:** orthogonally project the two
  ranges in the background positive Hilbert metric, then divide by rank. This
  produces legitimate density matrices, but imports a positive-Hilbert
  structure that is not the GU-native Krein datum. The answer on this fork is
  also negative for the requested role.

The fork matters: silently treating a Krein projector as a density matrix
would manufacture an invalid finite number; silently replacing it by a
Hilbert projector would hide the imported positivity.

## Result

The deterministic NumPy certificate
`tests/channel-swings/f2_cut_relative_entropy_probe.py` reproduces the frozen
W229 symbol and canonical F2 cut pair and establishes:

1. `Q_+` and `Q_-` are complementary K-self-adjoint projectors but are not
   Hermitian density matrices.
2. The Hilbertized range states have distinct equal-rank supports. Therefore
   both unregularized Umegaki directions are infinite by the support
   condition; there is no finite native candidate value.
3. Adding an epsilon identity regulator makes both states full rank, but the
   two ordered relative entropies agree to numerical precision. Deck exchange
   swaps the arguments and leaves the value unchanged: the channel is
   deck-even, not holonomy-odd.
4. The regularized value grows as epsilon is removed, exposing regulator
   dependence rather than a recovered finite observable.
5. Positive rescaling of the Dirac symbol leaves the cuts and Hilbertized
   states unchanged. Relative entropy is dimensionless, and this construction
   generates no scale.

The probe reports `5 [E] + 2 [F] = 7`, plus one setup check, all passing.

## Interpretation and boundary

This closes only the intake's literal **cut-only quantum-relative-entropy**
proposal at toy grade. It does not test Bianconi's full metric-versus-induced-
metric entropy, an actual N2 boundary operator family, a modular/Krein entropy
defined with additional native structure, or the M2 eigenvalue scale dial.
Any revival must name the extra structure that makes the states positive,
keeps the construction native, and supplies physical units without importing
the desired B.5 scale.

No claim status, canon verdict, public posture, PP3 packet, DE audit, master
identity, or external action moves.

## Next-work handoff

- Current item: Bianconi intake leg 2, cut-only relative entropy.
- Disposition: `ENDPOINT_NEGATIVE` at toy grade.
- Lane 1 remains led by the actual S_IG/B.5 frontier: N1 pushforward, N2 end
  family, N3 weld, or the distinct M2 scale-dial leg.
- Strongest low-cost alternative: the intake's Dirac-Kahler chirality-count
  fork, because it is independent of this entropy failure and directly tests
  whether a standard truncated-content anomaly survives the geometer-complete
  forms construction.
- Overturning evidence: a native positive state construction on the actual end
  family with a finite, regulator-independent, dimensionful, deck-odd entropy
  observable.
