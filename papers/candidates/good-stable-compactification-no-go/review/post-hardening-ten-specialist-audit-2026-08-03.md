---
title: "Post-hardening ten-specialist audit"
date: "2026-08-03"
status: "internal pass; fresh hostile deep-research rerun still required"
---

# Post-hardening ten-specialist audit

This is an internal perspective audit, not ten independent external reviewers.
It tests whether the maximal hardening swing introduced or left visible defects.

| lens | question | result |
|---|---|---|
| real reductive Lie theory | Are unboundedness and `ad(Z)` hyperbolicity separated? | Pass. Theorem parts 1–2 and part 3 carry different hypotheses. |
| quaternionic classical groups | Is the `Sp(32,32)` specialization derived in the actual matrix model? | Pass. Membership, commutators, dimensions, centralizer, and square-zero radicals are explicit. |
| highest-weight representation theory | Does extremality imply vector—not merely line—stabilization? | Pass. Each eigenspace component annihilates the vector and exponentiation is written out. |
| Krein/indefinite inner products | Is the fundamental-symmetry converse fully typed? | Pass. Involution, self-adjointness, equivariance, positivity, and finite-dimensional terminology are explicit. |
| Lean/formal methods | Does the formalization claim match the checked declarations? | Pass. Seven narrow declarations and their standard axiom dependencies are disclosed; no full-paper claim is made. |
| exact computer algebra | Is the concrete result checked without floating-point tolerance? | Pass. Sage performs 2,266 rational-quaternion checks. |
| property/falsifier engineering | Do generated cases exercise the identities and reject tempting false statements? | Pass after repair. The pair generator now always produces two matrices of the same rank; all 160 pair cases execute. Wrong-sign and mixed-parity mutants are rejected. |
| reproducibility | Can the named checks be rerun from a clean clone? | Pass at candidate grade. Python dependencies are locked, Lean is pinned and serialized, Sage version is recorded, and source hashes are frozen. |
| bibliography/novelty | Are citations accurate and is standard mathematics oversold? | Pass. Edition/DOI defects are corrected and the paper claims a scoped synthesis, not a new theorem of general Lie theory. |
| hostile editor | Does the title or abstract imply a GU or physical-stability theorem? | Pass. Detailed GU vocabulary is absent; the physical boundary is stated in the abstract and a dedicated section. |

## Residual classification

No fatal or major actionable item was found in this internal pass. The remaining
items are disclosed scope boundaries: non-extremal vectors, alternative
positivity predicates, infinite-dimensional extensions, and physical-model
dictionaries.

This result does not satisfy the formal post-ready gate by itself. A fresh
hostile deep-research review must still evaluate the v0.5 manuscript as the
complete submission.
