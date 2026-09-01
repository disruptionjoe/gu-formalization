---
title: "K86 observed CCR state-correlation boundary wave"
status: active_research
doc_type: reverse_scaffold_repository_owned_ccr_state_boundary_result
created: 2026-09-01
date: 2026-09-01
claim_ceiling: exact two-mode regular CCR/Fock existence construction from the repository-owned K86 reduced Poisson bracket, with bounded two-qubit observables and normalized positive Bell, Werner, product and tracial states realizing Tsirelson, intermediate and sub-classical CHSH values; no source-selected quantization, physical GU Hilbert space, unique state, Born rule, measurement dynamics, continuum interacting QFT, prediction, confirmation, or verdict
manifest: lab/process/k86-observed-ccr-state-correlation-boundary-wave.json
probe: tests/channel-swings/k86_observed_ccr_state_correlation_boundary_probe.py
---

# K86 observed CCR state-correlation boundary wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`

```gu-typed-objects
result: exact two-mode regular CCR representation and normalized positive-state CHSH boundary classification for the repository-owned K86 reduced bracket
carrier: two H-orthonormal modes of W960 quantized on bosonic Fock space, with bounded observables on the four-dimensional zero-one-particle tensor sector LAYER=observed CHIRALITY=N/A
pairing: Fock Hilbert inner product and normalized positive vector or density-matrix states ON=repository_owned_quantization_control
real_structure: complex Hilbert representation generated from the real classical two-mode phase space by a repository-selected complex polarization
grading: particle number grading; distinct from the classical BRST ghost grading and odd BV antifield degree
action_owner: repository-construction
target: bounded observable inclusion and positive-state evaluation on classical, intermediate and Tsirelson CHSH faces MAP-TYPE=evaluation
```

## One explicit quantization of the owned bracket

Choose two `H`-orthonormal reduced modes from K86. Their action-derived even
bracket is

```text
{q_i,p_j}=delta_ij,  {q_i,q_j}={p_i,p_j}=0.            (1)
```

For a fixed `hbar>0`, take the regular two-mode Fock representation on
`F(C2)`, with dense invariant finite-particle domain `D_fin` and

```text
[q_i,p_j]=i hbar delta_ij,  a_i|n_i>=sqrt(n_i)|n_i-1>. (2)
```

Equation (2) is not asserted in a finite matrix truncation: the probe includes
the trace obstruction and the top-level commutator defect as controls. The
unbounded canonical fields live on `D_fin`. The CHSH observables below are
bounded finite-rank operators supported on

```text
Q = span{|0>,|1>} tensor span{|0>,|1>} subset F(C2).   (3)
```

This supplies an explicit product, representation and domain. The complex
polarization, Fock representation, two-mode choice and state are repository
construction data, not source-selected GU structure.

## Exact positive states and correlation faces

On `Q`, use Pauli `X,Z` and set

```text
A0=Z tensor I,                 A1=X tensor I,
B0=I tensor (Z+X)/sqrt(2),     B1=I tensor (Z-X)/sqrt(2). (4)
```

All four operators are self-adjoint involutions; each `A` commutes with each
`B`. For

```text
C=A0B0+A0B1+A1B0-A1B1,                              (5)
```

the exact `Q(sqrt(2))` certificate gives `C^3=8C` and hence spectrum contained
in `{0,+/-2sqrt(2)}`. The Bell vector
`Phi+=(|00>+|11>)/sqrt(2)` is an eigenvector with eigenvalue `2sqrt(2)`, so the
Tsirelson ceiling is attained in this repository-selected representation.

The same algebra and fixed observables do not select one correlation value:

```text
omega_Bell(C)              = 2sqrt(2),
omega_Werner,t=3/4(C)      = 3sqrt(2)/2  (strictly between 2 and 2sqrt(2)),
omega_|00>(C)              = sqrt(2),
omega_trace(C)             = 0.                            (6)
```

Each state is normalized and positive; the Werner state is the convex mixture
`(3/4)|Phi+><Phi+|+(1/4)I/4`. Independently, the commutative joint-assignment
control retains the sharp classical ceiling `2`. Thus the action-derived
Poisson bracket plus existence of a regular quantization makes quantum and
intermediate faces available, but it does not choose the state or measurement
embedding that realizes one.

## Exact boundary and hostile review

The result closes an existence gap, not a physical-selection gap.
Noncommutativity is necessary to exceed the global commutative ceiling, while
the chosen positive state and local observable embeddings control where the
same noncommutative algebra lands. The strongest overclaim would report
`2sqrt(2)` as a GU prediction. The strongest contrary state is the normalized
trace, which gives zero on the same `C`; the product vector stays below the
classical ceiling for the same settings. The weakest seam is the absent
source-selected complex polarization, representation, state, observable map,
gauge-fixed measure and continuum interacting construction.

No delayed-choice entanglement-swapping datum is evaluated. No prediction,
confirmation, canon or public posture moves.

## Next condition

Derive a complex polarization or positive-frequency split, representation,
state and local observable map from a source-owned full action or another
independently owned physical principle. Then test whether that owner selects a
classical, intermediate or Tsirelson face and whether the selection survives
the full constraint/domain/BFV descent. The present construction proves
availability, not selection.
