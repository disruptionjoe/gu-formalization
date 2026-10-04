---
title: "K968 K967 finite-window atomic approximation"
status: active_research
doc_type: conditional_finite_window_atomic_approximation
created: 2026-10-03
claim_ceiling: constructive sufficient approximation bound only; no optimality, empirical fit or GU dynamics
manifest: lab/process/k968-k967-finite-window-atomic-approximation.json
probe: tests/channel-swings/k968_k967_finite_window_atomic_approximation_probe.py
target_claim: NONE-NOT-A-KILL
---

# K968 finite-window atomic approximation

```gu-typed-objects
result: finite positive atomic reservoir uniformly approximates exponential coherence on any declared finite window
carrier: system qubit tensor finite spectral environment C^N LAYER=observed CHIRALITY=N/A
pairing: positive Euclidean Hilbert pairing with positive atomic weights ON=repository_finite_approximation
real_structure: conjugation paired across symmetric frequency atoms
grading: degree-zero density operators; no BV or BRST grading
action_owner: repository-construction with imported cutoff, partition and error budget
target: strongest finite-window contrary model to K966 MAP-TYPE=evaluation
```

Fix `T>0` and `0<epsilon<1`. Choose

```text
Omega = 16 gamma/(pi epsilon),
N >= 2 T Omega/epsilon = 32 gamma T/(pi epsilon^2).
```

Partition `[-Omega,Omega]` into `N` equal cells, put one atom at each midpoint
and give it the normalized K967 mass of that cell. The weights are positive
and sum to one. For `0<=t<=T`, the Lipschitz bound
`|exp(i omega t)-exp(i omega_j t)|<=T|omega-omega_j|` gives discretization
error at most `T Omega/N<=epsilon/2`. K967 contributes at most
`8 gamma/(pi Omega)=epsilon/2`. Hence

```text
sup_{0<=t<=T} |f_N(t)-exp(-2 gamma t)| <= epsilon.
```

The control instance `gamma=0.7`, `T=3`, `epsilon=0.05` uses
`Omega=71.3014...` and `N=8557`; direct samples lie inside the rigorous
`0.0499976` combined bound.

Equivalently, take `H_E=C^N`, `H_1=diag(omega_j)`, `H_0=0` and initial unit
vector with components `sqrt(w_j)`. Its coherence factor is the stated
positive atomic characteristic function.

This proves a finite autonomous reservoir can mimic the continuum on every
fixed finite observation window when its dimension is allowed to grow. It is
a sufficient construction, not a minimal-dimension lower bound and not a GU
derivation.
