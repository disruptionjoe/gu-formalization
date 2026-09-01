---
title: "K82 quantum Tsirelson demand-boundary wave"
status: active_research
doc_type: reverse_scaffold_quantum_selection_nonselection_result
date: 2026-09-01
claim_ceiling: exact conditional Tsirelson theorem, saturation control and weak-demand countermodel classification; no GU-native Born rule, physical composition, unique quantum selection, prediction, confirmation, or verdict
manifest: lab/process/k82-quantum-tsirelson-demand-boundary-wave.json
probe: tests/channel-swings/k82_quantum_tsirelson_demand_boundary_probe.py
---

# K82 quantum Tsirelson demand-boundary wave

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
result: exact separation between Hilbert-operator assumptions that enforce the Tsirelson boundary and weaker positive no-signalling demands that do not
carrier: conditional bipartite binary-observable models; one real or complex Hilbert tensor-product branch and one generalized-probability box branch LAYER=conditional CHIRALITY=N/A
pairing: state expectation on the Hilbert branch and ordinary conditional-probability pairing on the box branch ON=repository_owned_controls
real_structure: real controls suffice for saturation; complex structure is not selected by this result
grading: N/A; minimal abelian BV and quotient grading do not enter the CHSH bound
action_owner: none for the quantum structure; the comparison tests frozen downstream demands and does not attribute Hilbert, Born or tensor data to Weinstein
target: Tsirelson boundary, saturation and nonselection under weaker positive no-signalling demands MAP-TYPE=classification
```

## The exact Hilbert boundary

Let `A0,A1` and `B0,B1` be binary self-adjoint involutions on two Hilbert
factors, with every Alice operator commuting with every Bob operator. For

```text
CHSH = A0(B0+B1) + A1(B0-B1),
```

the exact square identity is

```text
CHSH^2 = 4I - [A0,A1][B0,B1].
```

The commutator norms are at most `2`, hence `||CHSH||^2<=8` and every state
obeys

```text
|S| <= 2 sqrt(2).
```

The bound is sharp already over a real two-level control: Pauli `Z/X`,
`B0=(Z+X)/sqrt(2)`, `B1=(Z-X)/sqrt(2)`, and the Bell vector give exactly
`S=2 sqrt(2)`. This is a class-level consequence of the Hilbert operator,
commuting-composite, contraction-norm and state-expectation assumptions. It is
independent of the repository-owned action parameters `m2`, `lambda`, and the
positive principal stiffness.

## Weaker frozen demands do not select the boundary

Positivity, normalization, bipartite marginals, no-signalling and local
instruments are strictly weaker. Exact enumeration of all sixteen deterministic
binary local-response assignments gives `|S|<=2`. The PR box

```text
p(a,b|x,y) = 1/2  when a xor b = x*y, and 0 otherwise
```

is positive, normalized and no-signalling with uniform local marginals, yet it
has `S=4`. Thus the weak frozen demand set admits classical, Hilbert-quantum
and post-quantum models. It does not imply the Tsirelson boundary and cannot
select a Born/Hilbert realization.

The discriminating structure is now explicit: a future native packet must own
the operator product or an equivalent composition law, commuting local
algebras, the contraction order, and the physical state expectation. Merely
having a positive quotient cone, a trace-like normalization, local instruments,
no-signalling, positive energy, interaction or minimal BV closure is not
enough.

## Hostile boundary

The strongest overclaim would be to call the imported Hilbert assumptions a
GU derivation. The strongest contrary construction is the exact PR box. The
weakest propagation seam is the absent action-selected physical composition
and Born pairing on the actual quotient. The theorem neither selects real
versus complex quantum theory nor derives a C-star algebra, quantum measure,
local QFT or exported Bell experiment.

This is not a GU-native Born rule or physical tensor product. Delayed-choice
entanglement swapping remains reserved and unscored; the packet supplies no
prediction or confirmation.

## Next condition

Derive or independently supply a source/action-owned physical state space,
Born pairing, composition law and local observable algebra on the actual
quotient. Then test whether the exact Tsirelson assumptions descend without
import before any held-out observable export.
