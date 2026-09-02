---
title: "K101 observed modular QDB graph-simplex wave"
status: active_research
doc_type: reverse_scaffold_modular_graph_classification_result
created: 2026-09-02
date: 2026-09-02
target_claim: INTERNAL_TARGET:K101_MODULAR_QDB_TRANSITION_GRAPH_SIMPLEX
claim_ceiling: exact graph-support and fixed-algebra classification for the explicit finite strict-dephasing Gibbs-reversible family only; no all-QDB, interaction-selection, source, Born, prediction, confirmation, held-out score, promotion or verdict
manifest: lab/process/k101-observed-modular-qdb-graph-simplex-wave.json
probe: tests/channel-swings/k101_observed_modular_qdb_graph_simplex_probe.py
---

# K101 observed modular QDB graph-simplex wave

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
result: modular/QDB transition-graph simplex and ergodicity-record boundary
carrier: M_n(C) with simple Hamiltonian, faithful Gibbs state and matrix-unit jump family LAYER=observed CHIRALITY=N/A
pairing: Gibbs GNS pairing and imported trace/state-effect pairing ON=repository_owned_qdb_family
real_structure: matrix adjoint and energy-basis conjugation
grading: Bohr-frequency decomposition and graph components; no source BV, BFV or ghost grading
action_owner: repository-construction
target: allowed graph supports and fixed algebras MAP-TYPE=homomorphism
```

Scope: this packet classifies graph support in the explicit finite
strict-dephasing, matrix-unit jump family. It does not classify all quantum
detailed-balance semigroups.

## Inline preflight bookend

The route census covered modular spectral subspaces, Davies generators, GNS
detailed balance, reversible conductances, graph Laplacians, fixed algebras and
ergodicity. K98 realizes supplied partition graphs; K99 derives one graph from
one supplied interaction and exhibits two variants. The live gap is the full
support family allowed by the same modular data. The selected route
parameterizes the generator by reversible conductances before choosing any
interaction.

## Complete graph-support family

Let `H` be simple diagonal and let `rho=diag(r_i)` be faithful. Modular flow
identifies the matrix units and their ratios,

```text
sigma_t(E_ij)=(r_i/r_j)^(it) E_ij.                          (1)
```

For each unordered pair choose an independent conductance
`c_ij=c_ji>=0` and set

```text
k_ij=c_ij/r_i,       r_i k_ij=r_j k_ji=c_ij.               (2)
```

Together with positive energy dephasing, the matrix-unit jump generator is
Gibbs-GNS symmetric and `H`-covariant. Its transition graph contains
`{i,j}` exactly when `c_ij>0`. Every one of the
`2^(n choose 2)` labeled graph supports is therefore compatible with the same
faithful state and modular flow, and every present edge carries an independent
positive amplitude.

Modular data determine the eigenoperator decomposition and the forward/reverse
rate ratio. They determine neither which conductances vanish nor their positive
magnitudes.

## Ergodicity versus records

Strict dephasing removes all off-diagonal fixed points. On the diagonal, the
generator is a reversible graph Laplacian, so fixed functions are exactly
constant on connected components. Therefore

```text
Fix(L)=N_pi,
L is ergodic iff the graph is connected iff Fix(L)=C I.     (3)
```

In this family, adding ergodicity selects the scalar algebra and erases every
nontrivial record. A nontrivial fixed record algebra requires a disconnected
graph, hence a supplied zero-conductance cut or selection rule.

For weights `(8,4,1)/13`, all eight three-vertex graphs occur: four are
connected, three have one edge and one is empty. They realize the five set
partitions. This is the complete finite control, not a sampling argument.

## Owner accounting and maximum conclusion

Repository-owned: (1)--(3), complete support enumeration and the
ergodicity-record dichotomy. Imported: `H`, the Gibbs principle, strict
dephasing, conductances/interactions, classical energy basis, trace/Born
pairing and record semantics.

The maximum conclusion is exact nonselection: faithful modular flow plus QDB
allows a full graph simplex. It propagates a chosen interaction into rates; it
does not choose the interaction or a nontrivial record algebra.

## Inline postflight bookend

- Strongest overclaim: calling this explicit-family theorem a classification
  of all QDB semigroups.
- Strongest contrary construction: a source-selected symmetry or interaction
  can select one conductance support while respecting the same modular ratios.
- Weakest reproducibility seam: strict dephasing is load-bearing for removing
  isolated coherent fixed blocks.

The exact probe enumerates all eight graphs, all five component partitions and
every rational detailed-balance identity. Delayed choice remains reserved and
unscored.

## Next condition

Supply a source/causal observable that selects the conductance support, or prove
a stronger selector using additional naturality data not already invariant
under the faithful state's stabilizer.
