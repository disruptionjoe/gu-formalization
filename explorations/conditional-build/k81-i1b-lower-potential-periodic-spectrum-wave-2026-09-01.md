---
title: "K81 I1B lower-potential periodic-spectrum wave"
status: active_research
doc_type: reverse_scaffold_i1b_lower_potential_periodic_spectrum_result
date: 2026-09-01
claim_ceiling: exact periodic Fourier spectrum and invariant classification for one repository-owned constant-Hermitian two-component post-half-density family; no actual source cross-null operator, physical density or domain, rank-jump law, coefficient selection, prediction, confirmation or GU verdict
manifest: lab/process/k81-i1b-lower-potential-periodic-spectrum-wave.json
probe: tests/channel-swings/k81_i1b_lower_potential_periodic_spectrum_probe.py
---

# K81 I1B lower-potential periodic-spectrum wave

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
result: complete periodic Fourier spectrum and invariant classification for every constant Hermitian lower-order term that can survive the frozen matrix half-density transport
carrier: complex two-component periodic sections on a circle of length 2*pi LAYER=conditional CHIRALITY=N/A
pairing: positive repository-owned L2(dx;C2) pairing ON=periodic_post_half_density_control; not the native I1B presymplectic Green form
real_structure: Hermitian complex two-component operator with real coefficient coordinates c,x,y,z
grading: positive and negative Fourier eigenbranches; no physical ghost, gauge, BRST or BV grading
action_owner: repository owns the periodic control only; no filed source action owns its lower potential, periodic domain or candidate coefficient
target: which exact spectral invariants remain after compatible matrix-density transport and whether they can distinguish the two tangential candidates MAP-TYPE=classification
```

## Complete constant Hermitian lower-potential normal form

Work on periodic `C2`-valued sections over a circle of length `2*pi`, with the
positive `L2(dx;C2)` pairing. Define

```text
J=[[0,-1],[1,0]],   H=[[1,0],[0,-1]],
S=[[0,1],[1,0]],    K=iJ.                                    (1)
```

Here `J` is skew-Hermitian, while `I,H,S,K` are a real basis of all Hermitian
two-by-two matrices. Every constant symmetric lower term therefore has one
and only one decomposition

```text
V=cI+xH+yS+zK,                 c,x,y,z real.                  (2)
```

For

```text
D_V=J d/dx+V,                                                   (3)
```

the Fourier mode `e^(inx)` gives the exact matrix

```text
D_V(n)=cI+xH+yS+(n+z)K.                                      (4)
```

The three Pauli directions anticommute and square to `I`, hence

```text
[D_V(n)-cI]^2=[x^2+y^2+(n+z)^2]I.                            (5)
```

Thus the complete periodic spectrum is

```text
lambda_(n,+/-)=c +/- sqrt(x^2+y^2+(n+z)^2),   n in Z.         (6)
```

This is an exact classification, not a finite mode sample. Constant unitaries
commuting with `J` rotate the `(x,y)` plane and preserve
`rho^2=x^2+y^2`; they fix `c` and `z`. Integer shifts of `z` merely reindex
`n`, while `z` and `-z` are isospectral under `n -> -n`. The spectral data
therefore retain the scalar center, the transverse lower-potential radius and
the flat shift modulo these periodic identifications.

## The surviving potential can distinguish the candidates if it is owned

For the predecessor's named lower-term direction, set

```text
V=aH,                    a>0.                                (7)
```

Equation (6) becomes

```text
lambda_(n,+/-)=+/-sqrt(n^2+a^2).                             (8)
```

The spectral gap from zero is exactly `a`, attained at the zero Fourier mode.
Because `0<log(2)<log(3)`, the two candidate coefficients have distinct gaps.
Unlike the positive matrix density itself, the lower potential is not erased
by half-density transport.

This is a conditional selector, not a physical selection result. If the
repository defines `V=log(r)H`, then reading `log(r)` back from the gap merely
restates the input. Selection requires independent lineage: a source/action
Hessian, physical reduction or matching law must own `a`, this operator and
its domain before the gap can count as evidence.

## Exact boundary of matrix half-density transport

For a periodic positive compatible density `W`, the periodic unitary
`U=W^(1/2)` removes the canonical weight connection. An independently owned
`W`-self-adjoint term survives as `UVU^(-1)`. The Fourier formula (6) applies
when that transported potential is constant and the transported boundary
condition is periodic. If `U` is nonperiodic, it twists the boundary data; if
`UVU^(-1)` varies with position, constant Fourier blocks no longer diagonalize
the operator. Neither case is silently included here.

## Hostile review, scope and next condition

The strongest overclaim would call a mathematical spectral distinction a
source selector. It is not one without independent ownership. The strongest
contrary construction is a pure compatible weight connection, which the
half-density removes completely and which leaves no such gap. The weakest
reproducibility seam is domain transport: periodicity of `U` and constancy of
the transported potential are load-bearing.

The exact probe checks the Clifford relations, arbitrary rational Fourier
blocks, periodic reindexing, commuting-unitary invariants, rigorous disjoint
series bounds for `log(2)` and `log(3)`, artifact fences and planted hostile
mutations. This packet does not construct the actual I1B cross-null operator,
physical density, rank-jump boundary law or source coefficient. Those objects
remain the next condition before the invariant (6) can acquire physical force.
