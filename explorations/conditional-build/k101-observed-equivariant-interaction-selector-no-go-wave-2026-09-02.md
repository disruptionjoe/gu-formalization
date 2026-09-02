---
title: "K101 observed equivariant interaction-selector no-go wave"
status: active_research
doc_type: reverse_scaffold_interaction_selector_result
created: 2026-09-02
date: 2026-09-02
target_claim: INTERNAL_TARGET:K101_STATE_NATURAL_UNIQUE_INTERACTION_SELECTOR
target_claim_verdict: KILLED_IN_UNIQUE_FULL_STABILIZER_EQUIVARIANT_OPERATOR_CLASS
claim_ceiling: exact no-go for unique full-stabilizer-equivariant operator selection from one simple faithful state only; no set-valued, source-augmented, locality-breaking, Born, prediction, confirmation, held-out score, promotion or verdict
manifest: lab/process/k101-observed-equivariant-interaction-selector-no-go-wave.json
probe: tests/channel-swings/k101_observed_equivariant_interaction_selector_no_go_probe.py
---

# K101 observed equivariant interaction-selector no-go wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`

```gu-typed-objects
result: state-natural equivariant unique-interaction selector obstruction
carrier: M_n(C) with simple-spectrum faithful rho and its diagonal-phase stabilizer LAYER=observed CHIRALITY=N/A
pairing: Hilbert-Schmidt/Gibbs pairing and imported trace/state-effect pairing ON=repository_owned_modular_control
real_structure: matrix adjoint and energy-basis conjugation
grading: diagonal versus off-diagonal modular spectral sectors; no source BV, BFV or ghost grading
action_owner: repository-construction
target: unique equivariant interaction selector MAP-TYPE=homomorphism
```

Scope: this theorem concerns a unique operator-valued interaction assigned
naturally from one simple-spectrum faithful state under its full stabilizer. It
does not bind set-valued selectors or inputs augmented by source/locality data.

## Inline preflight bookend

The route census covered naturality, state stabilizers, modular covariance,
interaction operators, symmetry breaking and set-valued selection. K96--K99
give distinct examples of nonselection; none tests uniqueness at the input
symmetry level. The selected route applies the elementary but load-bearing
rule that a natural output over a fixed input must itself be fixed.

## Equivariant selector obstruction

Let `rho=diag(r_1,...,r_n)` have simple positive spectrum. Every diagonal phase

```text
D=diag(e^(i theta_1),...,e^(i theta_n))
```

fixes `rho`. Suppose a unique interaction operator `S(rho)` is natural under
all state-preserving inner automorphisms:

```text
S(D rho D^*) = D S(rho) D^*.                              (1)
```

Since `D rho D^*=rho`, equation (1) requires `S=D S D^*` for every diagonal
phase. Entrywise,

```text
S_ij = e^(i(theta_i-theta_j)) S_ij.                        (2)
```

For `i!=j`, choose phases with a nontrivial relative phase. Equation (2) then
forces `S_ij=0`. Therefore every such unique natural output is diagonal,
commutes with `rho` and with its simple-spectrum Hamiltonian, and has only a
zero-Bohr component. It can supply dephasing but no population-transition
graph.

Thus a faithful state and its modular flow cannot uniquely and equivariantly
select the nontrivial interaction needed by K99. This is stronger than
exhibiting several admissible interactions: it identifies the stabilizer as
the missing-owner boundary.

## Exact escapes

Supplying a distinguished off-diagonal observable `X` can select the support of
`X`; it also explicitly imports the missing owner. A preferred locality net,
source action or symmetry-breaking datum can reduce the stabilizer. A
set-valued assignment may select an orbit or whole modular spectral subspace
without choosing one operator. All remain outside this theorem.

## Owner accounting and maximum conclusion

Repository-owned: equations (1)--(2), off-diagonal vanishing, the zero-Bohr
consequence and the escape classification. Imported: the state, unique
operator selector type, full-stabilizer naturality, Hamiltonian relation,
interaction meaning, trace/Born pairing and record semantics.

The maximum conclusion is an exact selector no-go for the stated input type.
A nontrivial interaction requires additional structure that is not encoded in
the faithful state or modular flow alone.

## Inline postflight bookend

- Strongest overclaim: extending the theorem to set-valued or source-augmented
  selectors.
- Strongest contrary construction: a supplied off-diagonal `X` breaks the
  stabilizer and selects its transition support.
- Weakest reproducibility seam: full-stabilizer naturality is load-bearing; a
  weaker covariance category must expose its extra datum explicitly.

The exact probe verifies invariance under a generating sign-phase family,
off-diagonal exclusion and the supplied-observable escape. Delayed choice
remains reserved and unscored.

## Next condition

Identify a source/causal/locality datum that reduces the state stabilizer and
selects one interaction naturally, then compose that selected interaction with
the K91 quotient and common-domain conditions.
