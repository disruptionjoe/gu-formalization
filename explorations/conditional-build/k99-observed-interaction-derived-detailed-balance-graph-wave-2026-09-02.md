---
title: "K99 observed interaction-derived detailed-balance graph wave"
status: active_research
doc_type: reverse_scaffold_interaction_derived_qdb_graph_result
created: 2026-09-02
date: 2026-09-02
target_claim: INTERNAL_TARGET:K98_DERIVE_QDB_GRAPH_CLASSICALITY_FROM_INTERACTION
claim_ceiling: exact three-level Davies-family control in which nonzero Bohr components of one admitted interaction and KMS spectral support derive the transition graph, dephasing and two-block fixed algebra; the interaction, symmetry and bath spectrum remain supplied, so no universal detailed-balance, modular, causal or source selector is obtained
manifest: lab/process/k99-observed-interaction-derived-detailed-balance-graph-wave.json
probe: tests/channel-swings/k99_observed_interaction_derived_detailed_balance_graph_probe.py
---

# K99 observed interaction-derived detailed-balance graph wave

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
result: transition graph, energy dephasing and coarse fixed algebra derived from one admitted interaction's Bohr components and KMS spectral support
carrier: M3(C) with simple Hamiltonian spectrum and Gibbs GNS pairing LAYER=observed CHIRALITY=N/A
pairing: Gibbs GNS inner product and imported trace/Born state-effect pairing ON=repository_owned_davies_control
real_structure: energy-basis conjugation and matrix adjoint
grading: supplied R=diag(1,1,-1) symmetry sectors; no source BV, BFV or ghost grading
action_owner: repository-construction
target: interaction-derived detailed-balance graph and fixed record algebra MAP-TYPE=evaluation
```

Scope: this result binds one finite three-level weak-coupling control. It
derives the graph from an interaction matrix but does not derive or select the
interaction, its symmetry, the bath spectrum or the weak-coupling limit.

## Inline preflight bookend

The route census covered Bohr decompositions, Davies generators, KMS spectral
relations, reversible Markov chains, symmetry selection rules, decoherence,
fixed-point algebras, modular covariance and source custody. K98 supplied a
graph directly. The selected route removes that independent input by computing
edges from nonzero interaction matrix elements and bath support. A universal
QDB classification was rejected as unnecessary and stronger than the evidence.

## Interaction-derived graph

Take

```text
H=diag(0,log 2,log 4),       rho_beta=diag(4/7,2/7,1/7),
R=diag(1,1,-1),
S=diag(-1,0,2)+|0><1|+|1><0|.                              (1)
```

Then `[S,R]=0`. The only nonzero off-diagonal Bohr components of `S` connect
levels zero and one. With positive bath spectral support at `+/-log 2` and the
KMS relation `G(-omega)=exp(-omega)G(omega)`, normalize
`G(log 2)=4/7`, hence `G(-log 2)=2/7`. The induced classical rates are

```text
k_0to1=2/7,       k_1to0=4/7,       all rates touching 2 are zero. (2)
```

Thus `rho_0 k_0to1=rho_1 k_1to0=8/49`. The graph
`{0--1} disjoint_union {2}` is derived from `(H,S,supp G)` rather than supplied
as a separate partition.

The distinct diagonal entries of the zero-frequency component of `S` generate
strict energy dephasing. Combining it with (2), the Heisenberg fixed algebra is

```text
{diag(a,a,b): a,b in C}.                                   (3)
```

The long-time map is the Gibbs-weighted conditional expectation onto (3):
the `{0,1}` value is `(4 A_00+2 A_11)/6`, and level two remains `A_22`.
Exact GNS symmetry, covariance, positivity and decay are checked on all matrix
units.

## What is and is not selected

The interaction derives a graph once admitted. It does not make detailed
balance a selector of that interaction. Adding an `|1><2|+|2><1|` Bohr
component makes the graph connected and the fixed algebra scalar; removing all
off-diagonal components leaves the full energy diagonal. All three variants
obey the same Gibbs/KMS detailed-balance form. The supplied `R` symmetry
explains the missing cross-sector edge but is itself not derived.

Repository-owned: the Bohr decomposition, rates, balance identities, fixed
algebra and variant census. Imported: `H`, `S`, `R`, bath spectrum, weak-
coupling/Davies approximation, dephasing strength, Gibbs principle, beta,
record meaning and trace/Born pairing. Source-selected owner count is zero.

## Inline postflight bookend

- Strongest overclaim: saying QDB derives `S` or `R`. It only propagates their
  nonzero components into reversible rates.
- Strongest contrary construction: the connected and diagonal-only interaction
  variants give scalar and full-diagonal fixed algebras under the same KMS law.
- Weakest reproducibility seam: a finite matrix calculation does not establish
  a microscopic weak-coupling limit; the Davies generator is the admitted
  model, not a derived reservoir theorem.

The exact probe checks all matrix units, the three interaction variants and
hostile mutations. Delayed-choice remains reserved and unscored. No source,
continuum, microlocal, derived-Born, prediction, confirmation, canon, paper or
promotion status moves.

## Next condition

Derive the interaction, symmetry sector and bath spectrum from a source-owned
causal action, or prove a nondegenerate modular/causal principle that uniquely
selects them rather than merely deriving consequences after they are supplied.
