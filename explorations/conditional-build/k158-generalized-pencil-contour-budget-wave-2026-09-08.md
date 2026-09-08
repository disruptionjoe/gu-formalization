---
title: "K158 generalized-pencil contour-budget wave"
status: active_research
doc_type: conditional_generalized_pencil_finite_contour_bound_and_free_graph_route_obstruction_result
created: 2026-09-08
date: 2026-09-08
claim_ceiling: exact repository-owned correction and certificate-interface result for the supplied two-edge positive-Fock point control; the singular resolvent is governed by a generalized regular pencil, exact finite rectangle constants are available, but the point boundary map does not preserve the free-operator graph, the two-mode anchor is not identified with the cofinal approximants, and the bounded contour lacks a native lower-tail exclusion, so the K156/K157 contour route cannot certify a native count as formulated and no K152 interval, physical/source selection, Born derivation, prediction or confirmation follows
manifest: lab/process/k158-generalized-pencil-contour-budget-wave.json
solver: tests/channel-swings/k158_generalized_pencil_contour_budget.py
probe: tests/channel-swings/k158_generalized_pencil_contour_budget_probe.py
target_claim: INTERNAL_TARGET:K156_FREE_OPERATOR_GRAPH_CONTOUR_TRANSFER
target_claim_verdict: ROUTE_KILLED_AS_FORMULATED
canon_verdict_change: none
---

# K158 generalized-pencil contour-budget wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact remains on
> a repository-supplied positive particle/hole control. It does not identify
> the source-native GU object or select a physical polarization, extension,
> coupling, state, or observable. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: INTERNAL_STRUCTURAL_ONLY.

Scope: this result binds K139--K157's equal-coupling two-edge point control.
It corrects the proposed free-operator-graph contour route. It is not a result
about Weinstein's source action, a physical Hamiltonian, or the truth of GU.

```gu-typed-objects
result: exact generalized-pencil bridge and finite rectangle constants, plus a proof that the sharp point boundary does not preserve the free-operator graph required by the proposed contour budget
carrier: K156's hard-core C3 impurity tensor antisymmetric Fock carrier over L2(R;C4), with finite two-mode controls distinguished from K141's cofinal momentum-cell approximants LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: positive Fock Hilbert pairing, regular free-domain duality and the nonunitary chart Gram M=U^{- *}U^{-1} ON=repository_signed_point_control
real_structure: CAR adjoint and complete signed flavor permutation; q=(1,0) transports to q=(0,1) only after every domain and pencil term is intertwined
grading: conserved incidence charge, finite-control versus cofinal approximation, Hilbert versus particle-number versus free-operator graph topology, and local-island versus ground-count certification
action_owner: repository-construction -- operator, time orientation, polarization, couplings, W, kappa, domain and state are not selected by Weinstein's source or a GU action
target: complete native resolvent/count-transfer interface and its exact failed free-graph premise MAP-TYPE=intertwiner
```

## Inline preflight bookend

K157 names two missing constants, `d_GD,n` and `d_W,n`, before the
perimeter-ten transfer can close. Re-derivation from the current files changes
that work list. The contour is drawn for `H_N`, while K156 estimates `R_N`;
the boundary graph used by K139 is a particle-number graph, not automatically
the free-energy graph in K156; and K157's two-mode matrix is not one of K141's
cofinal momentum-cell approximants.

The route census covered direct singular resolvent subtraction, nonunitary
congruence, generalized operator pencils, boundary triples/rigged domains,
exact inertia guards, Riesz projection stability, Lehmann--Goerisch, and a
left-tail semiboundedness enclosure. The generalized pencil is the only route
that keeps the chart and spectrum correctly typed. Exact finite arithmetic is
used for the reference guards. The ultraviolet asymptotic decides the graph
question analytically before any larger computation.

## 1. The chart produces a generalized pencil, not an isospectral operator

K155 defines

```text
R=U^{- *}HU^{-1},                 S=U^{-1},
M=S* S.                                                        (1)
```

For every spectral parameter `z`, the correct object is

```text
T(z)=R-zM=U^{- *}(H-z)U^{-1}.                                 (2)
```

Whenever either inverse exists,

```text
T(z)^{-1}=U(H-z)^{-1}U*,
(H-z)^{-1}=S T(z)^{-1}S*.                                    (3)
```

Thus a regular-action error for `R_N-R` is only one term. A complete singular
resolvent budget must also control `M_N-M`, both outer inverse charts, and the
reference pencil from the free domain to Hilbert space. The companion solver
checks (1)--(3) exactly over rationals in both two-mode representative blocks.
It never calls `H_N` and `R_N` isospectral; nonunitary congruence does not
preserve ordinary eigenvalues.

For a finite-reference bound `||S_N||<=s_0` and
`d_G=||G_N-G||`, if `s_0 d_G<1`, a second Banach bootstrap gives

```text
s=s_0/(1-s_0 d_G),
e=||S_N-S|| <= s_0^2 d_G/(1-s_0 d_G),
||(M_N-M)(H0+a)^-1|| <= (s+s_0)e/a.                   (4)
```

If `tau=||(R_N-R)(H0+a)^{-1}||`, `|z|<=Z`, and `K_N,L_N`
bound `||(H0+a)T_N(z)^{-1}||` and `||T_N(z)^{-1}||`, put

```text
epsilon(z) <= K_N(z)[tau + Z(s+s_0)e/a].               (5)
```

For `epsilon<1`, a resolvent identity and the two outer chart differences give
an explicit singular-resolvent error. The solver implements the conservative
bound

```text
eta <= L_N [(s+s_0)e+s_0 s epsilon]/(1-epsilon).       (6)
```

This exact-rational compiler rejects
missing inputs, `epsilon>=1`, and `10 eta>=6`.

## 2. Exact bounds for the finite two-mode rectangles

The horizontal edges are one-half away from every real spectrum. On the right
edge, exact inertia proves empty guard intervals

```text
q=(0,0): [-3/2,-1/2],       q=(1,0): [-5/4,-3/4].      (7)
```

K157's Gershgorin bounds put the finite spectra strictly to the right of `-4`,
so the left edge at `-5` is more than one unit away. Consequently

```text
sup_Gamma ||(H_(2,00)-z)^{-1}|| <= 2,
sup_Gamma ||(H_(2,10)-z)^{-1}|| <= 4.                  (8)
```

Since `H0+256<=267` on these blocks, complete finite-plus-free-spectator graph
amplification bounds are respectively `534` and `1068`; the free tail alone
obeys `(E+256)/(E+1)<=257/2` for `E>=1`.

Exact one/infinity norms put both `U_N` and `U_N^{-1}` below `127/125`.
Combining this with (8) gives safe integer pencil bounds

```text
q=(0,0): L_N<=3, K_N<=552,
q=(1,0): L_N<=5, K_N<=1103.                            (9)
```

As a nonvacuity control, the exact compiler accepts the abstract simultaneous
inputs `d_G<=1/1600` and `tau<=10^-6` in both blocks. Those are not native
K157 values: the failed free-graph premise prevents `tau` from being emitted.

These are exact constants for the arbitrary rational two-mode control with
energies `(5/4,3/2)` and couplings `(1,1)`. K141's cofinal family instead has
cell energies `omega(k/n)` and the normalized point coefficients induced by
the momentum-cell embedding. No serialized unitary identification or
contour-preserving homotopy connects the two-mode matrix to that family.
Therefore (8) does not certify a reference rank for the large-`n` operator
whose limit is native.

## 3. The free-operator graph boundary constant is not finite

K141's dressed point vector is

```text
h(p)=(2 pi)^(-1/2)(omega(p)+256)^(-1).                (10)
```

It lies in `L2`. But where `omega(p)>=256`,

```text
|omega(p)h(p)|^2
 = (2 pi)^(-1)[omega(p)/(omega(p)+256)]^2
 >= 1/(8 pi).                                         (11)
```

The set has infinite measure, so `omega h` is not in `L2`. Removing any
finite cutoff leaves the same divergence. Applied to the vacuum, the omitted
creation tail therefore fails the free-energy graph domain. Hence

```text
||G_N-G||_(Dom(H0)->Dom(H0)) = infinity              (12)
```

for the sharp point map in the topology used by K156. The particle-number
graph estimate in K139 is finite because creation changes particle number by
one; it cannot be substituted for the free-energy graph. Thus K156's
free-graph `q_D`, `beta`, equations (13)--(14), and the requested numerical
`d_GD,n` cannot be instantiated as written. This kills that route, not the
K139 singular operator or its qualitative norm-resolvent convergence.

The Hilbert boundary error is repairable. In addition to K157's cutoff-tail
square `1/(3n)`, K141's cell approximation contributes at most
`1/(768n^2)` per channel at `lambda=256`; for four edge/polarity coefficients,

```text
d_G,n <= 4 sqrt(1/(3n)+1/(768n^2)).                  (13)
```

At `n=4096` this differs only slightly from K157's cutoff-only display, but
the distinction is logical: the latter was not the complete `d_G,n`.

## 4. Two further count gaps remain independent

The normal-ordered `d_W,n` is still underdetermined. K139--K141 prove
qualitative `O(p^-2)` convergence but do not serialize the common constants
for the diagonal Pauli/spectator term, the four exchange blocks, or the
uniform regular-core bound `B`. A usable replacement must expose tails
`q_n,t_n^(++),t_n^(+-),t_n^(-+),t_n^(--)` with

```text
d_W,n <= q_n + sum_(s,t) t_n^(st).                   (14)
```

Even a repaired resolvent transfer around the bounded rectangle proves only
the rank of the spectral island inside `[-5,-1]`. It does not rule out native
spectrum below `-5`. Calling that local rank the complete rank below `-1`
also requires a native lower bound, or a contour/homotopy that closes the
entire lower half-line. K156/K157 serialize neither.

The repaired route is therefore: work in a boundary/rigged-domain or direct
form-resolvent topology that never asks `G` to preserve `Dom(H0)`; certify the
rank on the same cofinal reference family (or prove a contour-preserving
homotopy from the two-mode control); expose (13) and the reference
amplification; and add a native left-tail enclosure before asserting a ground
count. Equal-rank Lehmann--Goerisch remains possible, but it needs its own
native form data and cannot inherit the missing premises by name.

## Inline postflight bookend

- **Strongest exact advance:** the singular-contour problem now has its correct
  generalized pencil and exact finite reference bounds `2` and `4`.
- **Route verdict:** the K156 free-operator-graph propagation route is killed
  as formulated because the point boundary has `omega h` outside `L2`.
- **Strongest contrary construction:** a rigged/boundary-domain or direct
  form-resolvent estimate may bypass the false graph-preservation demand while
  retaining K139's valid singular-domain construction.
- **Strongest overclaim:** “closing the two constants named by K157 proves one
  native eigenvalue below `-1`.” Refused: one constant is infinite in the
  named topology, the finite anchor is not cofinal, and the bounded contour
  does not exclude lower spectrum.
- **Weakest reproducibility seam:** K141's qualitative `O(p^-2)` statements do
  not expose the component constants needed for `d_W,n` or `B`.

The q=(0,1) sector remains only the image of q=(1,0) under the complete signed
flavor intertwiner. No native count, energy interval, threshold/Gram closure,
full-Fock scattering/NESS, physical/source selection, Born rule, held-out
score, prediction, confirmation, canon, paper, release or public-posture move
follows.

## Next condition

Replace K156 equation (14) by a direct form-resolvent or boundary-domain
estimate that is well typed for the point map. Construct the corresponding
cofinal finite reference matrices with normalized cell coefficients, certify
their rank and a left-tail lower enclosure, and serialize the five
normal-ordered component tails plus `B`. Only then rerun the generalized-
pencil contour budget; if it remains too coarse, use equal-rank
Lehmann--Goerisch with the same native form data.

## Reproduction

```bash
python3 tests/channel-swings/k158_generalized_pencil_contour_budget.py --demo
python3 tests/channel-swings/k158_generalized_pencil_contour_budget_probe.py
python3 tests/channel-swings/k158_generalized_pencil_contour_budget_probe.py --selftest
```
