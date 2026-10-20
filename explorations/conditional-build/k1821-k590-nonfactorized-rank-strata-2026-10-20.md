---
title: "K1821 — nonfactorized rank strata and the fixed-complex cohomology budget"
status: active_research
doc_type: exploration
created: "2026-10-20"
claim_ceiling: finite coefficient complexes only; no functional action or physical state
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
---

# K1821: nonfactorization alone cannot supply a proper, nontrivial finite reduction

For **every** nilpotent three-term deformation on K590's fixed vector spaces,
including arbitrary nonfactorized arrows, the homology dimensions are
`(H2,H1,H0)=(u,u+v,v)`. Thus nonzero H0 requires nonzero H1. A proposal demanding
both positive-degree acyclicity and nonzero H0 cannot meet those demands on
these fixed spaces. This is a finite algebraic budget, **not** a rejection of
GU's functional BV/KT complex or a physical-state theorem.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: complete finite rank-stratum specialization and entangled rank-loss witness
carrier: K590 vector spaces R^10752 -> R^46592 -> R^35840 LAYER=toy CHIRALITY=N/A
pairing: coordinate Euclidean form for the witness; three alternative quotient forms ON=finite_cokernel
real_structure: real coefficients; rational controls; no K77-to-K95 transfer
grading: homological degrees 2,1,0; existing outgoing/incoming projectors
action_owner: repository-construction -- selected conditional deformation; actual nonfactorized action coefficients unowned
target: finite properness and nonzero quotient compatibility MAP-TYPE=evaluation
```

## What is reused and what is tested

K589/K590 supply the exact factorized coefficient complex, with
`a=21*512=10752`, `c=70*512=35840`, and middle dimension `b=a+c=46592`.
K446 already supplies factorwise rank defects with homology `(0,70,70)` or
`(21,21,0)`. K468 proves stability of contraction under suitably small
nilpotent perturbations; K471 gives effective homology transfer. K1124 notes
that K590's zero cohomology has no nonzero physical state. None is repeated as
a new result here.

The new specialization classifies **all** finite arrows on these spaces,
locates their rank strata, exhibits a single entangled defect instead of a
70-mode factorwise defect, and compares its data requirements with the actual
serialized algebra. The general variety-of-complexes theory is established
mathematics: see [Cukierman, *Varieties of complexes and foliations*,
Propositions 1 and 3](https://arxiv.org/pdf/1111.5514). No novelty is claimed.

Layer 0: finite coefficient homology and an interacting functional physical
quotient are different objects. The latter needs action coefficients,
stationarity, domains, constraint propagation, pairing and interpretation.
SC-ACT-01/02/06 remain **ASSERTS**, SC-META-53 **UNCERTAIN**. LT-SM8,
LT-GR6b, RA-F1 and AC-F1 remain **NEEDS**. The current ledger's mapped coverage
is not a recovered-physics count. No source or ledger row changes.

## Complete finite classification

Write `C2 --A--> C1 --B--> C0`, with `BA=0`, dimensions `(a,a+c,c)`.
Set `u=a-rank(A)` and `v=c-rank(B)`. Rank-nullity gives

```
h2 = u,
h1 = (a+c)-rank(A)-rank(B) = u+v,
h0 = v.
```

Every `0<=u<=a`, `0<=v<=c` occurs: in `C1=R^a direct_sum R^c`, map the first
`a-u` input vectors identically into the first summand, and map the first
`c-v` vectors of the second summand identically onto C0. All other vectors
map to zero. Hence the conditions are necessary and sufficient, not merely
sampled. Adapted image/kernel/complement bases carry any pair of those ranks
to this normal form. These changes of basis are classification tools; they
are not asserted to preserve a preassigned physical form.

For fixed ranks `r2=a-u`, `r1=c-v`, rank-r2 maps A have dimension
`r2*(a+b-r2)`. Once A is fixed, B factors through `C1/im(A)`; the rank-r1
maps on that quotient have dimension `r1*(b-r2+c-r1)`. The stratum dimension is
therefore

```
a*b+c*c - (u*u+u*v+v*v).
```

The exact stratum `(u,v)=(0,0)` is open and dense in this finite variety:
in adapted normal form fill each missing A or B diagonal with a nonzero
parameter, preserving `BA=0`, and let that parameter tend to zero. Thus the
rank-loss stratum's codimension in the variety of complexes is
`u*u+u*v+v*v`. This is **not** its codimension in the unconstrained space of
all arrow pairs. It is also not a probability, a dynamical selection rule,
or a claim that a symmetry-constrained action avoids rank loss.

When both typed projector squares hold, the complex splits into two
independent halves with dimensions `(5376,23296,17920)`. Apply the same
formula separately with `(u_plus,v_plus)` and `(u_minus,v_minus)`: homology,
stratum dimensions and codimensions add. This covers arbitrary intertwiners
within each half, not only tensor-product maps. No antilinear exchange or
relation between the halves is assumed.

## A genuinely nonfactorized one-mode defect

Choose two independent output labels `m0,m1` and two outgoing carrier vectors
`e0,e1`. These are **new supplied data**, not source-selected vectors. In the
coordinate Euclidean pairing let

```
w = m0 tensor e0 + m1 tensor e1,
P_w = w w^T / 2,
A_s = A_0,
B_s = (I-s P_w) B_0.
```

Here `A_0,B_0` are K590's inclusion and quotient after the declared adapted
base decomposition. Since `B_0 A_0=0`, nilpotence holds for every real s.
Because w lies entirely in the outgoing half, both projector squares hold.
`I-s P_w` is invertible for `s!=1`; at `s=1`, B loses exactly one rank and
A keeps its rank. Full-size ranks are `(10752,35839)` and homology is
`(0,1,1)`. The one-mode endpoint is a codimension-one rank stratum.

The finite rational control takes `H=R`, `M=R^2`, `E=R^3`, with two outgoing
and one incoming direction. The tensor coefficient matrix of w has rank two;
realignment of P_w in `End(M) tensor End(E)` has rank four. Thus the
perturbation is not a single base/carrier tensor. Embedding this control as a
direct summand in the full coefficient spaces leaves all other exact pairs
unchanged. No 46,592-square matrix expansion is needed.

### Smallest finite repair and its cost

The new H1 is not optional bookkeeping. If the intended **finite** endpoint
requires H1=H2=0 while retaining H0=R, the carrier Euler characteristic must
increase by one. One exact repair adjoins a new degree-two generator whose
image is the surviving H1 representative. It injects, removes that H1 and
leaves H0=R. This changes C2 from dimension a to a+1, and yields `(0,0,1)`.
It is a different complex with an extra relation and action-ownership burden,
not a repair under the unchanged K590 dimensions. Merely adding a spectator
C0 also changes the budget, but supplies an arbitrary state instead of deriving
one. Neither construction has physical status.

## Actual action-data attempt and the first missing datum

**Subsequent evidence, 2026-10-20:**
[K1822](k1822-k77-rational-corrected-carrier-2026-10-20.md) now proves the
frozen corrected-carrier polynomial and multiplicities over QQ/R. The
real-lift qualification in the original paragraph below records the evidence
available when K1821 was written; that specific dependency is now discharged.
The restricted-algebra divisibility conclusion holds for this exact real
fixture. Action ownership, physical cohomology and the additional relation
remain open; stronger coefficient evidence supplies none of them.

K438/K439 and K607 serialize a corrected-carrier operator A with four spectral
multiplicities `192,192,64,64`. K610's available closure acts by the identity
inside each degeneracy space. The following divisibility conclusion is conditional
on that declared spectral decomposition: two finite-characteristic checks alone
do not prove its real lift, and this result does not strengthen K438's evidence
grade. Even allowing **all sums** of base maps tensor
polynomials in A, each arrow has block form `direct_sum_j B_j tensor I_dj`.
Its rank is `sum_j d_j rank(B_j)`. Consequently all arrow ranks and homology
dimensions in this closure are divisible by 64. The entangled one-mode defect
cannot be obtained from that algebra; it requires a map resolving a degeneracy
space. This is stronger than testing one simple tensor, but still only an
obstruction within the stated algebra. It does not exclude an actual
nonfactorized interaction or background that supplies such a map.

This identifies a concrete next input: an action-derived matrix element inside
a corrected-carrier spectral block, with its variation/degree labels, trace
projector squares and nilpotence. A freely chosen w makes an executable
countermodel; it cannot authenticate that input. Deriving it from the full
moving action and its constraints remains open. Ordinary covariance, a
repeated factorized lift, or a rank-only fit supplies no replacement.

## Nonzero does not imply positive

At s=1, the forms `+P_w`, `-P_w`, and `0` on C0 annihilate `im(B_1)`, hence
all descend to the same one-dimensional H0. Their values on w are `2,-2,0`.
The same differential and boundary compatibility therefore allow a positive,
negative or degenerate quotient form. This does not vary a fixed action-owned
form: no such form was supplied. A future inherited form must be tested for
descent and sign separately. Rank data alone cannot settle LT-SM8.

## Reproduction and hostile review

Run the producer and probe in `tests/channel-swings/k1821_k590_rank_strata*.py`.
The universal arguments above are algebraic proofs. Exact controls cover all
10 GF(2) complexes `1->2->1`, twelve rational rank normal forms `2->5->3`,
the entangled deformation at four parameters, and three quotient forms.
Planted nonzero composition and boundary leakage fail explicitly. Six
artifact mutations test reporting; they are not six independent theorems.

Strongest overclaim: exporting finite H0 or genericity to a functional GU
physical quotient. Strongest contrary construction: symmetry may enforce rank
loss, or a source-derived larger complex may have the required nonzero Euler
characteristic. Weakest ownership seam: w, its coordinate pairing and the
extra relation are supplied, not derived. These limits are part of the result.
No numerical integration, action selection, canon promotion, generation count,
physical positivity, prediction or confirmation follows.
