---
title: "K84 BRST star-state descent wave"
status: active_research
doc_type: reverse_scaffold_brst_star_state_descent_result
date: 2026-09-01
claim_ceiling: exact algebraic degree-zero differential-star-cohomology, boundary-ideal and positive-state descent theorem with a finite matrix control; no GU-native physical differential, analytic completion, observable algebra, Born rule, prediction, confirmation, or verdict
manifest: lab/process/k84-brst-star-state-descent-wave.json
probe: tests/channel-swings/k84_brst_star_state_descent_probe.py
---

# K84 BRST star-state descent wave

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
result: exact degree-zero differential-star-cohomology and positive-state descent theorem carrying the K83 Tsirelson SOS relation
carrier: Z0=ker(Q) intersect A0 modulo B0=Q(A^-1) for a unital differential graded star-algebra LAYER=conditional CHIRALITY=N/A
pairing: normalized positive functional omega on degree-zero cycles that annihilates every exact boundary ON=repository_owned_control_algebra
real_structure: real star-algebra and transpose involution in the finite control; no complex scalar premise is selected
grading: cohomological grading with Q of degree plus one, Q squared zero, graded Leibniz rule and star compatibility
action_owner: none for the physical differential or state; the DGA and finite matrix model are repository-owned downstream-demand controls and are not attributed to Weinstein
target: well-defined physical observable product, star involution, positive quotient state and CHSH SOS descent MAP-TYPE=classification
```

## Degree-zero observable-algebra theorem

Let `(A,Q,*)` be a unital differential graded star-algebra with `Q^2=0`, the
graded Leibniz rule and star compatibility. Define

```text
Z0 = ker(Q) intersect A0,
B0 = Q(A^-1).
```

For a degree-zero cycle `z` and a degree-minus-one element `b`, Leibniz gives

```text
z Qb = Q(zb),                 (Qb) z = Q(bz).
```

Thus `B0` is a two-sided ideal in `Z0`; star compatibility makes it a star
ideal. Therefore

```text
H0_Q = Z0 / B0
```

inherits a well-defined unital product and involution. This is the first
ownership condition hidden by the phrase “physical observable algebra.” A
linear quotient without the derivation/ideal property does not carry a
representative-independent product.

## Positive-state descent is a separate condition

A normalized positive functional `omega` on `Z0` descends uniquely to a
normalized positive functional on `H0_Q` if and only if

```text
omega(B0) = 0.
```

Necessity is representative independence. Sufficiency defines
`omega_bar([z])=omega(z)`; the ideal condition makes multiplication
well-defined, and positivity follows from
`omega_bar([x]*[x])=omega(x* x)>=0`. Conversely every positive quotient state
pulls back to a positive cycle state that annihilates boundaries. Algebra
descent and state descent are therefore distinct burdens.

If degree-zero cycle representatives `A0,A1,B0,B1` are self-adjoint and square
to the unit modulo exact boundaries, and every Alice-Bob commutator is exact,
their cohomology classes are commuting self-adjoint involutions. K83's exact
identity

```text
2 sqrt(2) 1 - C = (X^2+Y^2)/sqrt(2)
```

then holds in `H0_Q`, and the descended positive state obeys the Tsirelson
bound. Exact commutation is sufficient; literal commutation of arbitrary
off-shell representatives is not required.

## Finite exact control and the failure witness

Take the degree-zero cycle algebra

```text
Z0 = M4(R) direct_sum M4(R),
B0 = 0 direct_sum M4(R).
```

This is realized by the explicit truncated DGA with `A^-1=B0` as a
`Z0`-bimodule, `A^-2=0`, zero products between two negative-degree elements,
and `Q:A^-1 -> B0` the identity inclusion. The two bimodule terms cancel in
the graded Leibniz rule for a product of two degree-minus-one elements, while
the ordinary bimodule law handles degree zero against degree minus one.

The boundary summand is a two-sided star ideal and the physical quotient is
the first `M4(R)` summand. The real Bell-vector state on that first summand is
positive, normalized and annihilates `B0`. Standard real Pauli tensor-factor
classes saturate CHSH at `2 sqrt(2)`, so the SOS identity and its saturation
relations survive the quotient exactly.

By contrast, a normalized positive mixture that gives nonzero weight to the
second summand is perfectly positive on `Z0` but does not annihilate `B0`.
Equivalent representatives then receive different values. Positivity before
quotient is not enough to construct a physical state.

## Hostile boundary

The strongest overclaim would be to call this finite control DGA the GU
physical complex. It is imported and algebraic. The strongest contrary construction is
the normalized positive two-summand state that fails only boundary
annihilation and therefore cannot descend. The weakest propagation seam is the
absent source/action-owned BRST or BFV differential, selected analytic domain,
degree-zero physical cohomology and Born state.

The result does not prove positivity of an indefinite GU/Krein quotient,
construct a C-star norm, solve convergence or domains, derive measurement
dynamics, or select real, complex or quaternionic quantum theory. Delayed-
choice entanglement swapping remains reserved and unscored.

This is not a GU-native physical observable algebra, positive state or Born
rule. It supplies no prediction, confirmation or held-out credit.

## Next condition

Derive the actual source/action-owned BRST or BFV differential and physical
degree-zero cycle algebra, prove exact boundaries form the required star ideal
on the selected domain, and construct a normalized positive state that
annihilates them. Only then test the descended SOS factors for saturation or
strict slack.
