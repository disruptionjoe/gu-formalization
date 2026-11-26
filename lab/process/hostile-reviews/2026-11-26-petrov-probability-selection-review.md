---
title: 'Petrov probability selection: mathematical and hostile review'
status: exploration
doc_type: internal-review
created: '2026-11-26'
---

# Petrov probability selection: review

**Disposition:** accepted at internal scoped mathematical grade after the
corrections below. Two independent mathematical reviews and a separate hostile
source review inspected the concrete written proof. A primary-literature audit
narrowed the originality claim. These are internal agent reviews, not external
expert endorsement or full proof-assistant certification.

## Mathematical review A

- Exact quartic invariance, not merely root-set preservation, holds for the
  Klein-four subgroup and the stated limiting stabilizers.
- Universal compact-transporter proof works for arbitrary type-I sequences;
  trace-zero relative involutions prevent bounded elements from coalescing.
- Sharp II example `e x^4+x^2 y^2+y^4`, `0<e<1/4`, retains the fixed compact
  involution and exactly half the mass under its stabilizer average.
- Universal TV proof correctly selects an escaping element by proper exhaustion.
- Required correction: replace introductory “below” by “at most” to match sharp
  non-strict inequalities. **Applied.**

## Mathematical review B

- Independently checked the actual II exchange, trivial projective III
  stabilizer, and the normalized III matrices with `A B=J`, `B A=-J`.
- Accepted the universal overlap multiplicity argument and both sharp examples.
- Confirmed the Julia/barycenter sufficiency proof and action conventions.
- Confirmed finite certificates do not purport to prove properness, tightness,
  Petrov classification or worldwide priority. **Accepted without further repair.**

## Hostile/source review

- Source necessity of this observer law is absent. SC-GEO-03, SC-META-52/53 and
  the ambient Weyl/Ricci distinction in SC-OP-03 supply no missing bridge.
- Isolated II/III orbit laws remain possible; the excluded category uses ambient
  open neighborhoods and continuity across strata.
- Downstairs H3 is not an ambient K95/K77 physical domain or metric-fibre measure.
- TV failure involves unbounded boosts, not a fixed bounded transformation set.
- Requested a primary H3/S2 barycenter reference beyond the circle-paper title.
  **Applied:** DeMarco §8 and Cantarella–Schumacher added.

## Originality correction

The initial chat treated the broad randomization obstruction as the main
originality candidate. Closer primary comparison found the classical Julia
covariant, its quartic uniqueness and repeated-root behavior in Stoll–Cremona.
Visual-boundary mixing and conformal barycenters also reduce probability-valued
selection to point selection. Consequently the accepted claim is a **potential
quantitative refinement**: universal compact-mass bounds and TV defect, with
worldwide priority unestablished. Bhargava–Shankar supplies an additional exact
stabilizer precedent; Elezi's recent root-concentration result has a different
measure and quantifier and is recorded as adjacent work.

## Reproducibility

- Exact probe: **19 controls passed**, Gaussian-integer Laurent polynomials and
  rational weights, including wrong-sign mutations.
- Targeted Lean compilation: **9 lemmas passed, no sorry**, no warnings in the
  final source. Covers finite weighted overlap, probability discrepancy
  arithmetic and polynomial substitution identities.
- The infinite-dimensional and topological theorem remains the reviewed written
  proof. No source/physics/canon verdict or candidate choice is promoted.

[Proof](../../../explorations/conditional-build/petrov-probability-selection-2026-11-26.md)
· [Evidence](../petrov-probability-selection.json).
