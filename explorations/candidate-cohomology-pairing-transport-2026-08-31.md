---
artifact_type: exploration
status: active_research
doc_type: exact_pairing_preserving_quotient_transport
created: 2026-08-31
title: "Pairing criteria are invariant under quotient equivalence"
owner: gu-formalization
claim_status: repository_derived
claim_ceiling: "Exact algebraic invariance under a supplied pairing-preserving equivalence of candidate quotient presentations; no source-selected equivalence, analytic isometry, positive completion, conservation, observable, or physical state space."
target_claim: "INTERNAL — left and right nondegeneracy of the descended candidate-cohomology pairing are invariant under a zero- and pairing-preserving quotient equivalence; verdict: CONSTRUCTED"
canon_verdict_change: none
lean: Lean/GUFormalization/CandidateCohomologyPairingTransport.lean
probe: tests/channel-swings/candidate_cohomology_pairing_transport_probe.py
---

Classification: `INTERNAL_STRUCTURAL_ONLY`

```gu-typed-objects
result: pairing-preserving quotient-equivalence transport of left/right nondegeneracy
carrier: two presentations of supplied middle-cycle modulo gauge quotients LAYER=UNTYPED CHIRALITY=N/A
pairing: supplied descended bilinear forms related by an explicit equivalence ON=candidate-cycle-gauge-quotients; no positivity or conservation
real_structure: UNTYPED; no selected real, complex, antilinear or Krein structure
grading: middle cohomological degree only
action_owner: repository-construction over supplied complexes and equivalence; no source-owned action
target: equivalence-invariance of quotient nondegeneracy MAP-TYPE=isomorphism
```

# Pairing criteria are invariant under quotient equivalence

## Result

For two supplied three-stage complexes with gauge-basic pairings, Lean packages
an explicit equivalence of candidate cycle/gauge quotients that preserves the
zero class and the descended pairing. It proves that left nondegeneracy holds
on one presentation if and only if it holds on the other, and likewise for
right nondegeneracy.

This closes a presentation seam in the preceding radical criterion: once the
equivalence and pairing square are supplied, a different quotient encoding
cannot create or remove a radical class. The exact GF(2) control uses two
distinct names for the same two-class quotient and rejects a zero-moving
bijection, a pairing-changing bijection, and a planted extra radical.

## Scientific boundary

The theorem does not construct the equivalence or pairing from GU's source
action. It is not a physical isometry and supplies no common analytic domain,
real/Krein owner, positive majorant, conservation law, observable, probability
rule, or state-space interpretation.
