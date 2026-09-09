---
title: "K172 continuum first-block and graph-tail wave"
status: active_research
doc_type: conditional_native_K139_K156_continuum_first_action_blocks_graph_tail_theorem_and_Hilbert_only_obstruction_result
created: 2026-09-09
date: 2026-09-09
claim_ceiling: exact repository-owned continuum n=0 and n=1 K156 action blocks on the K162 vacuum and one-impurity seeds, an outward first-block Hilbert-norm enclosure, a conditional graph-norm all-order tail theorem and an exact Hilbert-only obstruction; the native numerical graph constants, all-order action tail, complete R_ref residual, complement or flux floor and scalar-center left floor remain absent, so no native K152 interval, physical/source selection, Born derivation, prediction or confirmation follows
manifest: lab/process/k172-continuum-first-block-graph-tail-wave.json
solver: tests/channel-swings/k172_continuum_first_block_graph_tail.py
probe: tests/channel-swings/k172_continuum_first_block_graph_tail_probe.py
target_claim: INTERNAL_TARGET:K171_HILBERT_CONTRACTION_VECTOR_TAIL
target_claim_verdict: HILBERT_ONLY_TAIL_ROUTE_KILLED_GRAPH_TAIL_REQUIRED
canon_verdict_change: none
---

# K172 continuum first-block and graph-tail wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: INTERNAL_STRUCTURAL_ONLY.

Scope: this packet remains on the repository-supplied K139--K171 signed point
control, fixed auxiliary shift `256`, and the K162 zero-bath vacuum and
one-impurity seed lines. It evaluates the first two native continuum block
vectors requested by K171, then determines what topology can actually close
their all-order tail. It does not select a physical extension or scalar center.

```gu-typed-objects
result: normal ordering gives W_0 phi=-256 phi and reduces W_1 G phi to an explicit scalar continuum multiplier on each allowed transition; its correction has a rigorous Hilbert bound, while an exact ell2 control kills the inference from Hilbert contraction of G alone to summability of W G^n phi
carrier: hard-core C3 impurity tensor positive particle/hole antisymmetric Fock space over L2(R;C4), in q=(0,0),(1,0),(0,1), with fixed K139 chart and K162 zero-bath seeds; ell2(N_0) is a non-native topology countercontrol LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: positive physical Fock Hilbert pairing transported by S=(1-G_256)^-1 to M=S* S; the sufficient all-order estimate uses a K156 graph domain D and a graph-to-Hilbert bound for W ON=repository_signed_point_control
real_structure: CAR adjoint, momentum conjugation, Hermitian normal-ordered bath blocks and the K168 real flavor-symmetric reference shape
grading: conserved incidence charges, hard-core impurity degree, bath-particle number, Neumann word order, K162 level and Hilbert-versus-graph topology
action_owner: repository-construction -- K156 fixes the normal-ordered core, but its existing artifacts give no numerical graph contraction q_D or graph-to-Hilbert constant B; no response datum, Weinstein source or GU action selects the physical extension, scalar center, domain or state
target: compute the native n=0 and n=1 continuum vectors, certify their norms, select the correct all-order tail topology and fail closed before the K152 residual/complement compiler MAP-TYPE=intertwiner
```

## Inline preflight bookend

K171 proved that scalar word norms do not determine the base action column and
asked first for `W_n G^n phi` at `n=0,1`. Retrieval rechecked K139's signed
creation chart, K156's normal-ordered core, K162's conforming seed lines,
K170's continuum profile and K171's block formula. The low blocks can be
evaluated directly. The proposed all-order Hilbert contraction shortcut is not
valid because `W` is graph-relative rather than bounded on the Hilbert space.

The route census attempted direct normal ordering, scalar integral reduction,
Hilbert geometric tails, graph-norm geometric tails, form-dual tails,
finite-regulator transfer, complete residual assembly and complement/flux
replay. The first-block and graph routes close; the residual and complement
routes remain dependent on numerical graph constants not yet serialized.

`SC-META-53` remains `UNCERTAIN`; `LT-SM8`, `RA-F1` and `AC-F1` remain
`NEEDS`. The source register and v0.263 physics ledger do not move.

## 1. Exact native continuum blocks at orders zero and one

Write `e=omega(p)=sqrt(1+p^2)` and use the K170 profile

```text
h(p)=(2 pi)^(-1/2)/(e+256).                           (1)
```

Every term of K156's normal-ordered remainder `X` contains a bath
annihilator. It therefore vanishes on either zero-bath seed, so

```text
W_0 phi=-256 phi.                                     (2)
```

On the first boundary word, subtracting the matched self-energy leaves

```text
D_256(e)=int_R e/[(omega(k)+256)(omega(k)+256+e)] dk/(2 pi).  (3)
```

The chosen K139 sign gives `g_1=-h` in each allowed transition component.
The exact continuum first block is

```text
W_1 g_1=(256-m D_256(omega(p)))h(p),                  (4)
```

where `m=1` for each of the vacuum's two orthogonal impurity-transition
components and `m=2` for the one allowed transition from a one-impurity seed.
This is a native limiting vector formula, not a K155 finite regulator matrix.

## 2. Outward first-block norm enclosure

Using `omega(k)>=|k|` in (3) gives

```text
0<=D_256(e)<=(1/pi) log(1+e/256).                     (5)
```

The elementary inequality `log(1+t)<=4 t^(1/4)`, followed by
`sqrt(omega(p))<=sqrt(1+|p|)`, yields

```text
||D_256(omega)h||^2
 <=8/[pi^2 sqrt(256*255)]
 < 8/(9*255)=8/2295 < 1/256.                         (6)
```

Thus `||D_256(omega)h||<1/16`. Combining this with K170's outward profile
norm interval gives the per-component bounds

```text
vacuum:       3501629753979/390625000000
          <= ||W_1 g_1||
          <= 35505047314137/3906250000000,

one impurity: 3477215691479/390625000000
          <= ||W_1 g_1||
          <= 35749187939137/3906250000000.            (7)
```

For the vacuum, the two transition components are orthogonal; the solver also
serializes their full-vector interval using an outward rational enclosure of
`sqrt(2)`. These are rigorous norm enclosures, not exact norms: the triangle
inequality deliberately retains the unknown correlation between `h` and
`D_256 h`.

## 3. The correct all-order tail topology

Let `D` be a K156 graph domain. If a native proof supplies

```text
||G||_(D->D)<=q_D<1,  ||W||_(D->H)<=B,
||phi||_D=c,           ||G||_(H->H)<=q_H<1,           (8)
```

then after resolving through order `N`, the complete K171 action-column tail
obeys

```text
B c q_D^(N+1)/((1-q_D)(1-q_H)).                       (9)
```

The first denominator sums `||W G^n phi||`; the second is the left adjoint
Neumann factor. The compiler's exact positive control returns `8/5` at
`B=2`, `c=1`, `q_D=1/2`, `q_H=3/8`, `N=1`. K156 states the qualitative
graph-relative operator bounds, but its current certificate does not
serialize numerical values of `B` or `q_D`. Equation (9) is therefore a
complete symbolic theorem, not a native numerical tail.

## 4. Hilbert contraction alone is insufficient

On `ell2(N_0)`, let

```text
G e_n=q e_(n+1),       W e_n=q^(-n)/(n+1) e_n.        (10)
```

Then `||G||=q<1` and `||G^n e_0||=q^n`, but

```text
||W G^n e_0||=1/(n+1),                               (11)
```

whose sum diverges. This exact abstract countercontrol kills the
`K171_HILBERT_CONTRACTION_VECTOR_TAIL` shortcut. It does not alter the native
continuum operator or prove its graph estimate fails; it proves the graph
premises in (8) cannot be omitted.

## 5. Native release replay

The first two native continuum action blocks and an outward first-block norm
are now serialized. The all-order vector tail is not: numerical graph
contraction `q_D` and graph-to-Hilbert constant `B` remain absent on the exact
K162 cofinal family. Consequently the K171 column sum, complete `R_ref`
form-dual residual, positive complete `M`-orthogonal complement or flux floor,
and K152 interval still fail closed. K169's `5/2` threshold member remains a
cap, not identification of the first threshold. The scalar center remains a
separate authority-owned input.

## Inline postflight bookend

- **Strongest structural advance:** equations (2)--(4) are the exact native
  `n=0,1` continuum vectors requested by K171.
- **Strongest quantitative advance:** equation (6) and the outward intervals
  (7) certify the complete first-block Hilbert norm on each seed line.
- **Strongest negative result:** a Hilbert contraction for `G` alone does not
  imply a summable action-block tail when `W` is unbounded.
- **Strongest execution advance:** equation (9) is the complete graph-norm
  tail compiler once native numerical `q_D` and `B` are supplied.
- **Strongest overclaim:** “K153's `3/8` Hilbert contraction closes the K171
  vector tail.” Refused by (10)--(11).
- **Weakest reproducibility seam:** the low-block multiplier is native, while
  its present norm interval uses a conservative analytic majorant rather than
  direct interval quadrature.

All five compatible arcs were attempted. Low-block evaluation, first-block
norm enclosure, graph-tail topology and the Hilbert-only obstruction closed.
The complete residual and complement arcs remained dependent on the missing
native numerical graph constants. Physical extension and scalar-center
selection remain authority-excluded. No source, ledger, Born, prediction,
confirmation, canon, paper, release or public-posture truth moves.

## Next condition

Evaluate the numerical graph contraction `q_D` with `q_D<1` and graph-to-Hilbert bound
`B` for K156's exact normal-ordered continuum core on the K162 cofinal family.
Insert them into (9) at `N=1`, assemble all bath-output components through the
K171 formula and compute the complete `R_ref` form-dual residual. Only then
replay the complete complement/flux floor below `E_ref(q)+5/2`; select the
scalar center separately before requesting a native left floor.

## Reproduction

```bash
python3 tests/channel-swings/k172_continuum_first_block_graph_tail.py --demo
python3 tests/channel-swings/k172_continuum_first_block_graph_tail_probe.py
python3 tests/channel-swings/k172_continuum_first_block_graph_tail_probe.py --selftest
```
