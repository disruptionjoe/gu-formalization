---
title: "K147 shared-vertex quasifree obstruction and matrix-threshold wave"
status: active_research
doc_type: conditional_shared_vertex_hard_core_car_obstruction_projected_matrix_zero_pauli_threshold_and_conjugate_result
created: 2026-09-08
date: 2026-09-08
claim_ceiling: exact repository-owned theorem for the equal-coupling two-edge shared-vertex signed point control that its native three-state impurity transitions do not form two CAR modes and therefore do not admit K146's native quasifree/Bogoliubov lift; on the explicitly non-invariant one-excitation boundary comparison the endpoint Gram matrix is diag(2,1,1), zero has multiplicity three, the vacuum threshold rank is three, all three single-residual Pauli compressions have rank two with no allowed dark impurity, and the self-dual projected comparison has Hilbert-Schmidt relative polarization plus degree-controlled C1,1 estimates; no native shared-corner full-Fock spectrum or Pauli census, cycle-uniform strict Mourre/scattering, NESS/current, physical selector, source/GU action, Born derivation, prediction or confirmation follows
manifest: lab/process/k147-shared-vertex-quasifree-obstruction-matrix-threshold-wave.json
probe: tests/channel-swings/k147_shared_vertex_quasifree_obstruction_matrix_threshold_probe.py
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# K147 shared-vertex quasifree obstruction and matrix-threshold wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: INTERNAL_STRUCTURAL_ONLY.

Scope: this packet fixes the first rook corner with vertices `0,1,2`, edges
`e1=(0,1)` and `e2=(0,2)`, equal real particle/hole couplings, diagonal
`W=0`, and K146's `m=kappa=|q|=1`, positive self-energy `1/4` and zero
subtraction. Its native theorem concerns the three-state impurity carrier. Its
spectral and threshold census concerns a separately named one-excitation
boundary comparison, which is not invariant under the full signed Fock
Hamiltonian.

```gu-typed-objects
result: the native two-edge shared-vertex transition algebra is hard-core rather than two-mode CAR, obstructing K146's quasifree lift; the separately typed projected four-channel boundary comparison has a three-dimensional zero space, a rank-three vacuum threshold, rank-two single-residual Pauli compressions and degree-controlled relative-polarization/C1,1 bounds
carrier: native span{|0>,|1>,|2>} tensor Klein tensor positive particle/hole Fock for the obstruction, and C3 direct-sum L2(R;C4) plus its self-dual double only for the projected matrix comparison LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: native positive impurity/Klein/CAR Fock pairing; standard projected Friedrichs pairing and self-dual doubled comparison pairing on the explicitly non-invariant control ON=repository_signed_point_control
real_structure: particle-hole conjugation belongs only to the self-dual double of the projected comparison; it does not turn the native hard-core impurity transitions into two CAR modes
grading: native affine incidence charge and combined Klein-CAR parity remain exact; projected zero labels 0,1,2 are comparison modes and may not be exterior-occupied as independent native impurity fermions
action_owner: repository-construction -- graph, polarization, point operator, couplings, subtraction, W, screening, domain and state are not selected by Weinstein's source or a GU action
target: native shared-vertex CAR/quasifree obstruction, projected matrix Schur zeros, complete single-residual Pauli rank census and projected degree-controlled physical-conjugate boundary MAP-TYPE=intertwiner
```

## Inline preflight bookend

K146 works because one impurity transition and its adjoint act as a single
fermionic mode after fixing the two-state Klein-parity block. A shared vertex
changes the algebra before it changes the Schur matrix. The central question
is therefore whether the two edge transitions satisfy the CAR on the native
three-state carrier, not whether a larger numerical BdG matrix can be written.

Mechanism retrieval found K139's matrix units and Klein factors, K143's signed
endpoint map, K144's projected Friedrichs census, K145's invariant-charge
ladder and K146's one-mode relative polarization. It found no shared-vertex
cross-CAR check or Pauli-compressed matrix census. The primary route computes
the transition algebra first. The fallback—needed only after algebraic
failure—is a direct interacting hard-core/Feshbach analysis of the infinite
charge block; it is not silently replaced by the projected comparison.

## 1. The native shared corner is not a two-mode CAR system

On the impurity/Klein carrier write

```text
B1=|1><0| tensor kappa1,    B2=|2><0| tensor kappa2.   (1)
```

The Klein factors supply the required field parity, but they cannot repair the
matrix-unit products. Direct multiplication gives

```text
Bi* Bj = delta_ij |0><0|,
Bi Bj* = |i><j| tensor kappa_i kappa_j.                (2)
```

Consequently

```text
{Bi,Bi*}=|0><0|+|i><i| != I_C3,
{Bi,Bj*}=|i><j| tensor kappa_i kappa_j != 0, i!=j.    (3)
```

The missing state is the doubly occupied impurity state of a genuine two-mode
exterior algebra. The native impurity label can occupy exactly one vertex.
For any nonzero combination `B(c)=c1 B1+c2 B2`, the pair `B(c),B(c)*` is a
single CAR mode only on `span{|0>,c1|1>+c2|2>}`; the orthogonal leaf is a
spectator. No one combination represents both independent edge transitions.

Thus K146's relative BdG diagonalization does not lift to the native two-edge
corner. This is a route obstruction, not a nonexistence theorem for the native
Hamiltonian: the full signed model remains a well-defined interacting
hard-core impurity/Fock problem on K139's IBC domain.

## 2. The honest projected matrix comparison has three zero modes

To locate exactly what matrix information survives, define the separate
one-excitation boundary comparison

```text
H_proj=C3 direct-sum L2(R;C4),                         (4)
```

with channel order `(e1,-),(e1,+),(e2,-),(e2,+)` and endpoint map

```text
Gamma = [1 0 1 0; 0 1 0 0; 0 0 0 1],
D=Gamma Gamma*=diag(2,1,1).                           (5)
```

Hence `rank Gamma=3`, and its one-dimensional label kernel is generated by
`(1,0,-1,0)`: the antisymmetric pair of channels meeting the central vertex.
There is no dark impurity direction because `D` is positive definite.

With `epsilon(p)=sqrt(1+p^2)+1/4`, `tau=5/4` and

```text
M(z)=z integral_R dp/[2 pi epsilon(p)(epsilon(p)-z)], (6)
```

the projected Schur matrix is

```text
S(z)=-z I3-M(z)D.                                     (7)
```

For every real `z<tau`, the integral in (6) is positive, so the three diagonal
factors are `-z(1+d_j I(z))`, with degrees `(2,1,1)`. Zero is therefore the
only gap root and has multiplicity three. If

```text
I2=integral_R dp/(2 pi) epsilon(p)^-2,
Z2=(1+2 I2)^-1,    Z1=(1+I2)^-1,                     (8)
```

the three orthogonal zero modes have impurity weights `(Z2,Z1,Z1)`.
Positive boundary imaginary part excludes embedded roots, and the explicit
finite-rank formula excludes singular-continuous spectrum. Thus

```text
sigma_p(H_proj)={0} with multiplicity 3,
sigma_ac(H_proj)=[5/4,infinity) with multiplicity 8.  (9)
```

The multiplicity eight retains both momentum branches of all four channel
species: three even bright combinations, one even label-kernel combination,
and four odd free branches.

## 3. Every projected single-residual Pauli rank is explicit

Normalize each vertex's bright channel by its degree. With
`Z=diag(Z2,Z1,Z1)`, the threshold map and Gram matrix are

```text
Gamma_tau=Z^(1/2) D^(-1/2) Gamma,
D_tau=Gamma_tau Gamma_tau*=Z.                         (10)
```

The comparison vacuum therefore has rank three, one channel-label kernel and
no dark impurity direction. If projected zero label `j` is already occupied,
Pauli compression uses `P_j=I-|j><j|`. The complete single-residual census is

```text
j=0: nonzero spectrum(P_j D_tau P_j)={Z1,Z1},
j=1: nonzero spectrum(P_j D_tau P_j)={Z2,Z1},
j=2: nonzero spectrum(P_j D_tau P_j)={Z2,Z1}.         (11)
```

Every case has rank two, channel-kernel dimension two, and zero dark dimension
inside the two-dimensional allowed impurity space. The removed direction is
Pauli blocked, not dynamically dark. A double zero-mode residual is not a
native option: exterior occupation of the three projected zero modes would
again manufacture an impurity Fock carrier absent from (1).

Equations (10)--(11) are the complete threshold-rank census of the projected
matrix comparison. They are not a residual threshold census of the native
infinite full-Fock charge blocks.

## 4. Relative polarization and C1,1 survive only for the comparison

Self-dual doubling of `H_proj` produces a finite-rank boundary perturbation of
its free doubled operator. The sign-contour vectors have
`epsilon(p)^-1` tails, so their squares are integrable and the interacting/free
negative projections differ Hilbert--Schmidt. The corresponding relative
transform is implementable on the artificial exterior Fock space of the
projected comparison. By (3), that implementer cannot represent the native
hard-core shared-corner interaction.

For `v(p)=p/sqrt(1+p^2)` use the symmetrized velocity conjugate on each
positive channel and opposite signs on the self-dual partners. As in K146, the
first two commutators of every resolvent-dressed boundary vector lie in `L2`.
The only graph factor is

```text
||Gamma||^2=||D||=max_v degree(v)=2.                  (12)
```

Thus the projected corner is `C^(1,1)`, with strict Mourre and the standard
`s>1/2` LAP on compact intervals away from zero and `5/4`. More generally the
`C^(1,1)` seminorms of these projected endpoint comparisons are bounded by
maximum endpoint degree. Every rook subgraph has degree at most four, so this
regularity norm is graph-size uniform. This does not prove a cycle-uniform
strict Mourre constant: spectral localization, zero-mode compression and the
native hard-core interaction are separate obligations.

## Inline postflight bookend

- **Strongest advance:** the first shared vertex exposes an exact algebraic
  boundary: two Hubbard transitions on `C3` are not two CAR modes.
- **Strongest matrix result:** the honest projected endpoint Gram matrix is
  `diag(2,1,1)`; zero has multiplicity three and the continuum multiplicity is
  eight.
- **Strongest Pauli result:** the vacuum rank is three; all three
  single-residual compressions have rank two and no allowed dark impurity.
- **Strongest regularity result:** projected relative polarization and
  `C^(1,1)` bounds survive, with seminorm controlled by maximum degree.
- **Strongest contrary construction:** adjoining a doubly occupied impurity
  state would restore a two-mode CAR exterior algebra, but it changes the
  native `C3` impurity object and is therefore only a different model.
- **Strongest overclaim:** importing (9)--(12) into the native full signed Fock
  spectrum. Refused: the projection leaks and the transition algebra is
  interacting.
- **Weakest reproducibility seam:** strict Mourre constants are proved for the
  fixed projected corner, not uniformly for all cycles or for off-diagonal
  `W`.

The companion probe computes the transition anticommutators, endpoint Gram
matrix and kernels, Schur signs and zero weights, all Pauli compressions,
degree bounds and scope fences under baseline-first hostile mutations.

## Next condition

Analyze the native two-edge shared-corner infinite charge block as an
interacting hard-core impurity model, using a charge-sector Feshbach or
operator-algebra route rather than a false quasifree lift. Determine its point
spectrum and first true bound-residual thresholds before attempting strict
Mourre constants across rook cycles. The projected degree-uniform `C^(1,1)`
bound is available as an input but is not the missing full-Fock theorem.

## Reproduction

```bash
python3 tests/channel-swings/k147_shared_vertex_quasifree_obstruction_matrix_threshold_probe.py
python3 tests/channel-swings/k147_shared_vertex_quasifree_obstruction_matrix_threshold_probe.py --selftest
```
