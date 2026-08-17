---
title: "Hostile review — K150 moving selected-Shiab coordinate adapter"
status: completed
doc_type: hostile_review
created: "2026-08-16"
target: explorations/conditional-build/selected-k150-moving-selected-shiab-coordinate-adapter-2026-08-16.md
verdict: survives_with_claim_ceiling
---

# Hostile review — K150

## Strongest overclaim

The adapter does not compute the curved restricted residual. It supplies the
first coefficient map only. The moving distortion pairing, density, lowerers,
curved metric bridge, and their formal-adjoint composition remain separate
dependencies. Calling the residual zero or nonzero would be an overclaim.

## Strongest mistyping

K132's frozen Euler block cannot be reused as a moving coefficient: the
**frozen substitution** deletes the live first coordinate jet. Conversely, the nearby
Eric moving-metric implementation cannot be imported because it explicitly
belongs to a distinct `(9,5)` port, whereas this chain is fixed at `Cl(7,7)`.
The K150 implementation derives its columns from the selected tensor formula
and uses both cases only as controls.

## Strongest contrary construction

A fully co-moving component basis can make tensor coefficients appear constant.
That does not refute K150: its coordinate chart intentionally holds the input
and output component bases fixed while moving `Phi_i`, so connection and
coefficient jets remain visible to K149's Leibniz composition. A later pairing
adapter must state its own trivialization and prove compatible covariance.

## Weakest reproducibility seam

The frozen and rotated controls cover one exact 56-dimensional invariant
packet rather than the complete 229376-dimensional carrier. This is sufficient
to catch formula, channel, and rotation regressions but is not a global rank
census. K132 retains the complete frozen census; K150 claims adapter
serialization, not a new all-grade rank theorem.

## Verdict

The adapter survives at its declared grade. It exactly reproduces the selected
formula and independent first derivative, exposes live first and second jets,
and passes frozen plus rationally rotated blocks. No preferred historical
selector, pairing, bridge, curved residual, quotient, domain, BFV, or physical
claim follows.
