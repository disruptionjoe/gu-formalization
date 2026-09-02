---
title: "K96 observed record-algebra selector nonuniqueness wave"
status: active_research
doc_type: reverse_scaffold_record_algebra_selector_nonuniqueness_result
created: 2026-09-02
date: 2026-09-02
target_claim: INTERNAL_TARGET:K95_CONDITIONAL_EXPECTATION_KMS_RECORD_ALGEBRA_SELECTOR
target_claim_verdict: INVARIANCE_ONLY_SELECTOR_ROUTE_KILLED_SOURCE_SELECTED_ROUTE_OPEN
claim_ceiling: exact finite-algebra counterexample showing that unital complete positivity, trace preservation, idempotence, dynamics covariance and equilibrium-state preservation do not uniquely select a record algebra in a degenerate sector, plus the absence of a normal Gibbs density for the unbounded-below translation pointer; no theorem against additional source-selected structure, continuum AQFT, microlocal state, derived Born law, prediction, confirmation, held-out score or verdict
manifest: lab/process/k96-observed-record-algebra-selector-nonuniqueness-wave.json
probe: tests/channel-swings/k96_observed_record_algebra_selector_nonuniqueness_probe.py
---

# K96 observed record-algebra selector nonuniqueness wave

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
result: exact nonuniqueness of equilibrium-state-preserving conditional expectations onto incompatible record algebras
carrier: M2(C) qubit observable algebra with degenerate H=0 equilibrium control LAYER=observed CHIRALITY=N/A
pairing: imported normalized trace tau(A)=Tr(A)/2 ON=repository_owned_selector_control
real_structure: matrix adjoint and standard complex conjugation
grading: Z-record versus X-record maximal abelian subalgebras; no source BV, BFV or ghost grading
action_owner: repository-construction
target: conditional-expectation and KMS criteria as a record-algebra selector MAP-TYPE=evaluation
```

Scope: this result binds the stated finite degenerate equilibrium control and
the K96 translation pointer's Gibbs boundary. It kills selection from the
listed invariance axioms alone, not selection by an additional coupling,
source action, causal net, modular inclusion or physical state.

## Inline preflight bookend

The route-changing lens census covered conditional expectations, decoherence-
free and pointer algebras, fixed-point subalgebras, KMS and Gibbs states,
modular covariance, degeneracy, symmetry breaking, superselection, basis
ambiguity, the K92 soldering precedent, the K96 outgoing pointer, source
custody and falsification scope. A two-basis exact counterexample dominates a
larger algebra search: it decides whether complete positivity, idempotence,
dynamics covariance and equilibrium preservation alone uniquely choose a
record range.

Retrieval found K92's distinct local-algebra solderings, K95's dephased finite
Hamiltonian average and K96's fixed outgoing sign effect. It found no theorem
testing conditional-expectation or KMS uniqueness as the record selector.
Standard qubit dephasing and KMS facts receive no novelty claim. Positive
controls check Kraus form, positivity, trace, idempotence, covariance,
equilibrium preservation and distinct ranges. Negative controls collapse the
ranges, alter the state, invent a pointer Gibbs density or promote the result
against source-selected structure.

## Two exact conditional expectations

On `M2(C)`, take degenerate equilibrium dynamics

```text
H=0,                            alpha_t(A)=A,               (1)
tau(A)=Tr(A)/2.                                                (2)
```

The normalized trace is the beta-KMS state for every finite `beta`. Define

```text
E_Z(A)=(A+ZAZ)/2,
E_X(A)=(A+XAX)/2.                                      (3)
```

Each map is an average of two unitary conjugations. Hence each is unital,
completely positive and trace preserving. Since `Z^2=X^2=I`, each is
idempotent. Both commute with the identity dynamics and preserve `tau`.

Their ranges are nevertheless different: `E_Z` projects onto the `Z`-diagonal
algebra and `E_X` onto the `X`-diagonal algebra. On
`rho_0=|0><0|`,

```text
E_Z(rho_0)=rho_0,              E_X(rho_0)=I/2.             (4)
```

Thus the same complete-positivity, trace, idempotence, covariance and KMS-
state criteria admit incompatible record algebras. Degeneracy leaves the
basis unselected. More generally, conjugating (3) by any qubit unitary gives a
continuous family with the same structural properties.

## The K96 pointer does not supply a Gibbs selector

The infinite-pointer Hamiltonian uses `p=-i d/dx` with spectrum `R`. For every
`beta>0`, the spectral function `exp(-beta p)` is unbounded toward negative
momentum and is not trace class. Therefore no normal Gibbs density

```text
rho_beta=exp(-beta p)/Tr(exp(-beta p))                     (5)
```

exists for that model. Invoking KMS/Gibbs selection would require a different
algebraic dynamics, a lower-bounded reservoir or a separately supplied state.
It cannot be silently read out of the translation control.

## Maximum licensed conclusion

Conditional-expectation axioms plus covariance and preservation of a
degenerate equilibrium state do not uniquely select a record algebra. The K96
pointer also has no normal Gibbs state capable of supplying a selector. A
record basis therefore remains an explicit owner in the current reverse
scaffold.

This is not a universal no-selector theorem. A nondegenerate interaction,
environment-induced superselection, modular inclusion, source causal net or
action-selected observable may remove the ambiguity. Such an owner must be
constructed and typed rather than inferred from invariance alone.

## Inline postflight bookend

- Strongest overclaim: extending the degenerate `M2(C)` counterexample to every
  KMS system or claiming that no physical pointer basis can be selected. It
  proves insufficiency of the listed axioms only.
- Strongest contrary construction: a nondegenerate Hamiltonian together with
  covariance and a specified coupling can privilege its spectral algebra. That
  is additional structure, exactly the missing owner identified here.
- Weakest reproducibility seam: the finite maps and spectral obstruction are
  exact, but no source observable algebra, modular state, local net or
  environment-induced superselection is constructed.

The exact probe passes `26/26`; its hostile selftest catches `21/21` planted
positivity, idempotence, range, KMS, spectrum, custody and promotion mutations.
No source, continuum, microlocal, Born, prediction, confirmation, canon, paper
or held-out status moves.

## Next condition

Supply a nondegenerate interaction or source causal/action structure that
selects one observable/record algebra and physical state, and prove its
compatibility with the K91 quotient and K96 common-domain dynamics. For a
thermodynamic route, construct a lower-bounded reservoir and algebraic KMS
state rather than importing a Gibbs density unavailable in the current model.
