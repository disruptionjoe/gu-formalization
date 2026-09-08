---
title: "K157 nested-cylinder count-transfer wave"
status: active_research
doc_type: conditional_nested_cylinder_finite_residual_and_complete_riesz_count_transfer_result
created: 2026-09-08
date: 2026-09-08
claim_ceiling: exact repository-owned nested finite-mode and graph-radius cylinder cores for the supplied two-edge positive-Fock control, with exact finite rank-one spectral islands below minus one, rational inverse-iteration residual anchors, elementary outward free and dressed-point cofinal tails, and a complete-contour Riesz rank-transfer theorem; the graph-boundary and normal-ordered regular-core constants needed for the native contour error remain missing, so no native count, K152 interval, physical/source selection, Born derivation, prediction or confirmation follows
manifest: lab/process/k157-nested-cylinder-count-transfer-wave.json
solver: tests/channel-swings/k157_nested_cylinder_count_transfer.py
probe: tests/channel-swings/k157_nested_cylinder_count_transfer_probe.py
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# K157 nested-cylinder count-transfer wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact remains on
> a repository-supplied positive particle/hole control. It does not identify
> the source-native GU object or select a physical polarization, extension,
> coupling, state, or observable. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: INTERNAL_STRUCTURAL_ONLY.

```gu-typed-objects
result: explicit nested representative-charge cylinder cores, exact finite count and residual anchors, an outward partial cofinal tail ledger, and a complete-contour Riesz rank-transfer theorem with fail-closed native applicability
carrier: the K156 hard-core C3 impurity tensor antisymmetric positive particle/hole Fock carrier, with finite mode-support M, interaction-graph radius r, and charges q=(0,0),(1,0),(0,1) LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: positive Fock Hilbert pairing; finite exact Hamiltonian matrices use canonical occupation coordinates, while native transfer uses common-carrier resolvents and Riesz projections ON=repository_signed_point_control
real_structure: CAR adjoint and the complete signed flavor permutation; q=(1,0) transports to q=(0,1), not by an unsigned label swap
grading: conserved incidence charge, finite mode support, graph radius, inverse-iteration order, contour winding, and finite versus complete-carrier certification
action_owner: repository-construction -- operator, extension, polarization, couplings, contour target and state are not selected by Weinstein's source or a GU action
target: numerical K156 tail inputs and a rank-preserving complete-count interface for K152 MAP-TYPE=intertwiner
```

## Inline preflight bookend

K156 leaves two superficially similar tasks: compute finite trial data and
prove that a finite count survives on the complete carrier. They are not the
same task. The route census compared a direct free-gap minorant, rank-one
Schur exterior bounds, finite-section inertia, Temple residuals,
Lehmann--Goerisch, Birman--Schwinger, and Riesz projection stability.

The direct free-gap route is not presently quantitative: K139--K156 do not
give the graph-form constants needed to lower-bound the full trial-orthogonal
compression. The selected switch is therefore an exact finite spectral island
plus a complete separating contour. It consumes the same common-carrier
resolvent convergence K141/K156 already prove qualitatively and states the one
missing outward norm explicitly.

## 1. Explicit nested cylinder cores

For mode support `M`, charge `q`, and seed `s_q`, let the exact K151 basis be
`B_(M,q)` and connect two basis words when the K151 Hamiltonian has a nonzero
off-diagonal entry. Define

```text
C_(M,r,q)=span{e_x: graph_distance(x,s_q)<=r},          (1)
s_00=|0;->,              s_10=|1;->.                   (2)
```

Leaving the newly added bath modes empty embeds `B_(M,q)` into
`B_(M+1,q)`. The embedding preserves hard-core occupancy and both incidence
charges. Graph balls are nested in `r`. For the exact two-mode control with
energies `(5/4,3/2)`, the dimensions for radii zero through four are

```text
q=(0,0): 1, 5, 13, 33, 51   (full block 84),
q=(1,0): 1, 3, 11, 21, 50   (full block 76).           (3)
```

These are the requested explicit nested cores. They are finite regulator
form/action domains, not spectral subspaces of the native limit. The signed
flavor unitary transports the entire construction from `(1,0)` to `(0,1)`.

## 2. Exact finite count and residual anchors

At `lambda=256`, matched endpoint subtraction, and the two energies above,
exact rational congruence gives

```text
rank 1_(-infinity,-1)(H_(2,00))=1,
rank 1_(-infinity,-1)(H_(2,10))=1,                    (4)
-1 is not an eigenvalue in either block.               (5)
```

Gershgorin lower bounds are `-2111504/529935>-5` and
`-7916081/2119740>-5`. Thus the rectangle with real interval `[-5,-1]`
and imaginary half-height `1/2` encloses exactly one eigenvalue in each finite
block and has perimeter ten. For count transfer, extend that block on K141's
common carrier by the decoupled free orthogonal tail. Its spectrum starts at
the unit mass gap, so it adds no spectrum to the rectangle; this extended
operator, rather than the bare finite matrix alone, is the reference in (10).

Two exact inverse iterations of `(H_2+2)^-1` from each seed produce rational
trial columns. Their outward 40-bit summaries are approximately

```text
q=(0,0): rho=-1.601791139...,  ||(H_2-rho)u||^2<=0.001018527,
q=(1,0): rho=-1.251828454...,  ||(H_2-rho)u||^2<=0.019522544. (6)
```

The bare K153 seed lines are conforming seeds, not ground approximations. In
particular the two-mode `(1,0)` block already has at least two exact spectral
values below the seed Rayleigh value. Calling the seed a ground trial would
therefore be false even before the continuum limit.

## 3. First outward cofinal component ledger

Choose a single cofinal sequence

```text
delta_n=1/n,       mode radius N_n=n^2,
physical momentum radius K_n=N_n delta_n=n.            (7)
```

K141's Lipschitz estimate gives the free graph-relative component
`d_A,n<=1/n`. For
`h_256(p)=(2 pi)^(-1/2)(sqrt(1+p^2)+256)^(-1)`, use
`sqrt(1+p^2)>=|p|` and `1/pi<1/3` to obtain

```text
||1_(|p|>n)h_256||^2 <= 1/(3n).                        (8)
```

For four equal edge/polarity coefficients, the Hilbert boundary-map tail is
at most `4/sqrt(3n)`, rounded outward by the compiler. At `n=4096`, the
ledger therefore records

```text
d_A<=1/4096,       ||h_tail||^2<=1/12288.              (9)
```

This is intentionally a partial K156 equation-(14) budget. The free-graph
boundary tail `d_GD,n` and the complete normal-ordered core graph tail
`d_W,n` still lack numerical trace/exchange constants. Because either missing
entry affects both inverse-chart sides or the central regular term, the
compiler emits no total `tau_n` and no native residual.

## 4. Complete-contour rank transfer

Let `Gamma` be a closed contour separating a finite spectral island, and let
`P_N,P` be the finite-reference and native Riesz projections on the same
carrier. If

```text
sup_(z in Gamma)||(H-z)^-1-(H_N-z)^-1|| <= eta,        (10)
length(Gamma) eta < 6 < 2 pi,                          (11)
```

then the contour formula gives

```text
||P-P_N|| <= length(Gamma) eta/(2 pi) < 1.             (12)
```

Two projections within norm one have the same rank. Hence a complete bound
`eta<3/5` on either perimeter-ten contour transfers (4) to rank one. This is a
complete count theorem: it controls every contour edge, the common-carrier
extension, and the whole enclosed island. It does not replace those premises
with a finite second eigenvalue, a threshold point, or K148's HVZ edge.

K141/K156 provide qualitative norm-resolvent convergence but not the outward
uniform contour error needed in (10). The finite rank-one anchor is not a
native count today. The remaining numerical work is now exact: close the two
missing graph constants, propagate K156's total tail to the rectangle, and
prove `eta<3/5`. If that bound is too coarse, refine the contour/core or use an
equal-rank Lehmann--Goerisch enclosure; do not revert to the failed bare
free-gap minorant.

## Inline postflight bookend

- **Strongest construction:** both representative charges now have explicit
  nested mode-support and graph-radius cylinder cores.
- **Strongest numerical anchor:** exact rational inertia isolates one finite
  eigenvalue below `-1` in each two-mode block, and inverse iteration supplies
  reproducible trial residual columns.
- **Strongest route correction:** K153's seed vectors are domain seeds only;
  the `(1,0)` seed is demonstrably not a numerical ground trial.
- **Strongest count theorem:** a complete perimeter-ten resolvent error below
  `3/5` preserves the finite rank by Riesz projection stability.
- **Strongest overclaim:** “the two-mode rank-one islands prove the native
  representative ground count.” Refused: the complete contour error is not
  serialized.
- **Weakest reproducibility seam:** numerical graph-boundary and normal-
  ordered exchange/Pauli tail constants remain missing from the total K156
  budget.

No native energy interval, threshold/Gram closure, physical/source selection,
Born rule, held-out score, prediction, confirmation, canon, paper, release or
public-posture movement follows.

## Next condition

Prove outward numerical `d_GD,n` and `d_W,n` for (7), including the diagonal
Pauli/spectator remainder and all four polarity exchange blocks. Propagate
them through both inverse-chart sides of K156 equation (14), convert the
result to the complete rectangle-resolvent error, and test `eta<3/5` in both
representative charges. If it closes, transfer rank one and feed the actual
residual/coercivity/gap packet through K154/K152; if not, increase the core or
run the equal-rank Lehmann--Goerisch route.

## Reproduction

```bash
python3 tests/channel-swings/k157_nested_cylinder_count_transfer.py --demo
python3 tests/channel-swings/k157_nested_cylinder_count_transfer_probe.py
python3 tests/channel-swings/k157_nested_cylinder_count_transfer_probe.py --selftest
```
