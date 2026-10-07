---
title: "K1296--K1300 Weyl-orbit Witten functional lift"
status: active_research
doc_type: conditional_research_result
created: "2026-10-06"
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
claim_effect: none
---

# K1296--K1300 Weyl-orbit Witten functional lift

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `SOURCE_NATIVE_ROUTE` for the SC-ACT-06 functional-ownership
question and `INTERNAL_STRUCTURAL_ONLY` for the quadratic Witten, Hodge and
generator theorems.

Scope: a repository-constructed quadratic normal model over the finite regular
`W(D7)` orbit selected conditionally by K1294, its finite orbit-sum Hilbert
complex on `R7`, and the Weyl-invariant subcomplex. This is not the nonlinear
K1294 selector away from its minima, a source action, an I1B BV-BFV complex, a
Lorentzian causal system or a physical state space.

```gu-typed-objects
result: Weyl-covariant quadratic normal family, orbit-sum Witten complex, common graph domain, closed ranges, exact gap, invariant Gaussian cohomology and maximal generator
carrier: finite direct sum over a regular W(D7) orbit of L2(R7;Lambda-star C7) LAYER=toy CHIRALITY=N/A
pairing: positive L2 Hilbert pairing on complex exterior forms ON=orbit_sum
real_structure: complexification of real Cartan coordinates with conjugation preserving the real Gaussian sector
grading: exterior-form degree zero through seven
action_owner: repository-construction -- quadratic normal lift of an imported K1294 target; no released source action owns it
target: Weyl-invariant subcomplex included in the orbit-sum K1145/K1150 functional-feasibility control MAP-TYPE=inclusion
```

## K1296: Weyl-covariant quadratic normal data

Let `o` be a feasible regular target point from K1294 and let `O=W(D7)o`.
Regularity makes `|O|=|W(D7)|=2^6 7!=322560`. At `o`, the K1294 selector has
positive Hessian

```text
B_o=(dF_o)^T diag(r0^(-2d)) dF_o > 0,
d in {2,4,6,7,8,10,12}.
```

Because the selector is Weyl invariant,

```text
B_(w o)=w B_o w^T.
```

Thus every orbit point carries the quadratic superpotential

```text
Phi_o(x)=1/2 <x-o,B_o(x-o)>,
```

and all these models are orthogonally unitarily equivalent. If
`mu=min spectrum(B_o)`, then `mu>0` is one uniform orbit-wide floor. This is a
normal model: it matches the selector value, critical point and Hessian at the
orbit, but it is not equal to the nonlinear residual-square selector globally.

## K1297: the finite orbit-sum Witten complex

For each `k=0,...,7`, define

```text
H^k = direct_sum_(o in O) L2(R7;Lambda^k C7)
```

and on orbit-sum Schwartz forms set

```text
d_Phi = d + dPhi_o wedge,
d_Phi^2=0.
```

The closure is a Hilbert complex. Signed permutations act on coordinates and
exterior forms while permuting the orbit summands. K1296's covariance identity
makes `d_Phi` equivariant. Every summand has one degree-zero Gaussian class
`exp(-Phi_o)` and no positive-degree class. Hence the full degree-zero
cohomology has dimension `322560`, but the transitive Weyl action leaves only
the normalized equal orbit sum invariant:

```text
dim H^0(H^W,d_Phi)=1,
H^k(H^W,d_Phi)=0 for k>0.
```

The invariant class is positive and nonzero mathematically. Calling it a
physical BV-BFV class would require a typed bridge that is absent here.

## K1298: one domain, closed range and an exact gap

Diagonalize `B_o` with eigenvalues `mu_i>0`. The Witten Laplacian

```text
L=d_Phi d_Phi^*+d_Phi^* d_Phi
```

has single-summand spectrum

```text
sum_i 2 mu_i (n_i+epsilon_i),
n_i in Z>=0, epsilon_i in {0,1}.
```

The zero eigenspace is exactly the degree-zero Gaussian line and the complete
positive spectrum is bounded below by

```text
delta=2 min_i mu_i = 2 mu > 0.
```

The finite orbit sum and invariant restriction preserve this gap and compact
resolvent. The spectral gap gives closed ranges for the Hilbert-complex
differentials, Hausdorff cohomology and the Hodge decomposition

```text
H = ker L orthogonal_sum im d_Phi orthogonal_sum im d_Phi^*.
```

The mathematical quotient pairing is the ambient `L2` pairing restricted to
the one-dimensional invariant Gaussian class. In its inherited quotient norm
its lower bound is exactly one. That passes K1148 for this declared control;
it does not identify the pairing as a physical inner product.

For every word used in the construction, take the common complete graph
domain

```text
D_common=D((1+L)^2),
||u||_common=||(1+L)^2 u||.
```

It lies in the domains of `d_Phi`, `d_Phi^*`, `L`, `d_Phi L` and
`L d_Phi`; orbit-sum Schwartz forms are a common invariant core. This passes
the K1146 graph-domain, K1147 closed-range and K1148 uniform-gap gates for the
declared mathematical control.

## K1299: maximal generator and resolvent

On the complex Weyl-invariant Hilbert space set

```text
G=-iL, D(G)=D(L).
```

Self-adjointness of `L` makes `G` maximal skew-adjoint. It generates the
unitary group `exp(-itL)`, preserves every spectral domain above and commutes
with the closed differential. The standard skew-adjoint resolvent estimate is

```text
||(z-G)^(-1)|| <= 1/|Re z|, Re z != 0.
```

On the orthogonal complement of the Gaussian class,

```text
||L^(-1)|| <= 1/(2 mu).
```

There is no geometric boundary on `R7`; Schwartz integration by parts closes
with zero boundary form, and the spectral unitary group preserves that
boundaryless realization. This satisfies the maximal-generator horn of K1149
and gives a conditional boundaryless trace row. It is an elliptic resolvent,
not a retarded/advanced Lorentzian causal Green pair.

## K1300: the ownership boundary is now sharper

The K1150 replay for this control has four satisfied mathematical rows:
common graph domain, closed gauge range, uniform positive gap and maximal
generator. Boundary compatibility is conditional because the model is
boundaryless. Source/action ownership and the native causal-algebraic packet
remain missing. The K1145 replay similarly supplies a nilpotent differential,
positive nonzero invariant cohomology and one common domain, but no source-owned
`Q,d,G,H` packet or native `6/6/4` causal ranks. Consequently the current
native-candidate pass counts remain `0/7` for both compilers.

Relative to K1295, three analytic rows—common domain, range/gap and
Green-or-generator—move from missing to conditional for an explicit repository
control. The integrated census is therefore nineteen satisfied, six excluded,
seven conditional and three missing. The missing rows are still the decisive
ownership inputs: a source-derived six-shape response law, source-derived
`lambda` plus physical orientation, and positive nonzero *physical*
cohomology. K1297's invariant Gaussian class does not move that last row.

SC-ACT-01/02/06 remain `ASSERTS`; SC-META-53 remains `UNCERTAIN`;
LT-SM8/LT-GR6b/RA-F1/AC-F1 remain `NEEDS`. No source, physics-ledger, canon,
paper, public-posture, prediction, confirmation or protected verdict moves.

## Verification and exact next input

The five producers and their independent hostile probes certify the finite
covariance, cohomology counts, oscillator spectrum, graph/range/gap statements,
generator bounds and admission census. The next exact input is a released
source action, boundary or Green law that derives a feasible K1294 target,
`lambda`, all six shapes and a native `Q,d,G,H` plus boundary packet. Only then
can the K1296--K1299 construction be transported to one common physical carrier
and replayed as a source-selected K1145/K1150 candidate.
