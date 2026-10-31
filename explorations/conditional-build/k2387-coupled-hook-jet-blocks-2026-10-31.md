---
title: "K2387 Simultaneous curved hook-jet blocks with exact shared coefficients"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no native GU or measured physical verdict
scripts:
  - tests/channel-swings/k2387_coupled_hook_jet_blocks_probe.py
---

# K2387 Simultaneous curved hook-jet blocks with exact shared coefficients

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `CONVENTIONAL_COMPARATOR`.

```gu-typed-objects
result: K2387
carrier: tracefree hook jets on the selected14D metric at the stored K2381 lower jet LAYER=toy CHIRALITY=N/A
pairing: actual indefinite eta and induced Gram and four-form polarizations ON=declared_carrier
real_structure: exact rational and square-root-two coefficient tensors
grading: radial odd field and resonant grade-two hook branch
action_owner: repository-construction -- conditional K2375 selected action and actual K2345 metric
target: simultaneous necessary third Euler and fourth algebraic jet subsystems MAP-TYPE=evaluation
```

## What is constructed

[K2384](k2384-third-hook-jet-compatibility-2026-10-31.md) proves existence of an unrestricted third Euler jet, but does not intersect it with all fourth-order Gram/sigma constraints. This result constructs **one shared exact solution of ten coupled necessary blocks** on the SAME K,L stored in [K2381](k2381-rotated-null-hook-prolongation-2026-10-31.md). Each block contains both Euler and quartic algebraic rows. Overlapping blocks share their cubic coefficients. This eliminates a concrete proposed source of obstruction; it is not the full intersection or a smooth stationary solution.

The first attempt solved four repeated-direction blocks separately: rank8570 in12544 unknowns, with47648 original rows each. All passed. Rather than assume composition, the continuation joined all ten symmetric pairs from v,w in{e10,e11,e12,e13}. It computed rank73460 in107520 unknowns and replayed476480 original affine rows. One rational/sqrt2 solution has157 rational and294 sqrt2 nonzero coefficients, serialized in the report. A second direct tensor reconstruction checks every selected quartic and Euler equation. These are exact finite linear-algebra results, not large-rank estimates or independent proof counts.

SC-ACT-01/02/06 and SC-GEO-55 retain ASSERTS; SC-META-56 retains DISAVOWS. The conditional action and fixed metric are not a source-wide verdict. Native domain, matter/action/observation and ledger0.263 debts are unchanged.

## Derive a closed necessary subsystem

Use H=0, K_a=nabla_a H, L_ab=nabla_a nabla_b H from K2381. Let S be the totally symmetric part of the third covariant derivative M. Write P for either the Gram bilinear form or the four-form sigma polarization. The fourth derivative of P(H,H)=0, after division by2, is

    sum_(four singleton choices d) P(S_abc,K_d)
       +sum_(three pairings ab|cd) P(L_ab,L_cd)=0.       (1)

Take v,w in W=ker K and set X_m=S(v,w,e_m). The entire row with derivative slots(v,w,u,t) becomes

    P(X_u,K_t)+P(X_t,K_u)
       =-P(L_vw,L_ut)-P(L_vu,L_wt)-P(L_vt,L_wu).       (2)

Only these fourteen hook values occur; all choices of u,t must still be imposed. The Euler equation on the same values is

    sum_m eta_m[X_m(i,m,j)+X_m(j,m,i)]=R_vw,ij.         (3)

Equations(2) and(3) must be solved together. An inconsistency would exclude the stored K,L, not every lower jet. Consistency of separate v,w blocks would not by itself enforce symmetry across them.

## Actual curvature receiver for the tested vertical subspace

K2381 uses pairs(0,1),(4,2),(5,3),(6,10),(7,11),(8,12),(9,13), with b1=-9012/493 and all other b=0. Thus e10,e11,e12,e13 all belong to W and are purely vertical in the actual metric-on-metrics geometry.

Two geometric facts are required before dropping the Ricci Hessian. The metric block is independent of horizontal coordinates and has no horizontal/vertical cross block, so its vertical distribution is totally geodesic. The probe directly checks all actual Christoffel components Gamma^h_ab vanish for vertical a,b and horizontal h. In addition, the pinned K2378 computation gives nabla_V Ric=0 for every vertical V. GL congruence covariance extends that identity over the fibre; it is not merely a value at one point. Therefore

    (nabla² Ric)(V,W)
      =nabla_V[(nabla Ric)(W)]-(nabla Ric)(nabla_V W)=0

for vertical V,W. The scalar curvature is constant, so the tracefree Ricci Hessian also vanishes in these slots. This proof does not assert zero horizontal Hessian.

With K_v=K_w=0, the symmetric-in-v,w part of K2384's zero-total-symmetrization curvature baseline reduces to

    Sym_vw M0(v,w,m)
       =-[K(R(v,m)w)+K(R(w,m)v)]/6.                  (4)

To see this, insert P_ab;c=R_ab.K_c-K(R_ab e_c) and Q_a;bc=R_bc.K_a in the baseline formula; terms antisymmetric in v,w cancel, and K_v,K_w vanish. Since the quadratic receiver's second derivative has Fpolar(K_v,K_w)=0, the right side of(3) is exactly

    R_vw,ij=(1/6)sum_m eta_m[
       K(R(v,m)w+R(w,m)v)_(i,m,j)
      +K(R(v,m)w+R(w,m)v)_(j,m,i)].                 (5)

For v=w this reduces to the +1/3 expression. Actual curvature is recomputed from the pinned metric backend; no flat or constant-curvature replacement is used. All coefficients belong to Q(sqrt2).

## Basis, coefficient construction and shared symmetry

The tracefree hook fibre has dimension896. A concrete basis has168 repeated-index tensors and728 all-distinct tensors. For each a choose j as the largest index other than a; for each remaining i use

    h_iia=eta_i, h_iai=-eta_i,
    h_jja=-eta_j, h_jaj=eta_j.

For each a<b<c use the two cyclic coefficient triples(x,y,-x-y) with(x,y)=(1,0),(0,1), and antisymmetrize the last two slots. These tensors satisfy the hook trace and cyclic relations. Their disjoint independent coordinate choices establish the stated basis count.

Every K_u has repeated-index support. Consequently Gram(h,K_u) vanishes on the distinct-index basis, while sigmaPolar(h,K_u) vanishes on the repeated-index basis: the repeated index appears twice in the latter four-form wedge. The probe checks this split coefficientwise before Euler rows couple the parts. It assembles original receiver labels, rather than identifying constraints by matching dimensions.

For one pair(v,w), X_m has14*896=12544 coordinates. The affine matrix is the same for each pair; only the actual L² and curvature receiver changes. The initial four repeated-direction systems have rank8570. Trace and many sigma constraints are redundant, so47648 is a row count, not the number of independent conditions.

For the joined solve, use cubic derivative coordinates sorted(a,b,m), with(a,b) any pair in{10,11,12,13}. There are120 distinct triples and107520 hook coordinates. This identifies every shared triple across the ten blocks automatically. Sparse rational elimination solves two right sides, for1 andsqrt2. Original-row replay verifies all476480 equations, including zero left-hand-side rows. The reported rank73460 is computed in exact rational arithmetic. The hook-basis ordering in the probe and sorted derivative-triple list in the report specify the coefficient ordering completely.

The independently reconstructed tensors then check2100 Gram/sigma polynomial identities (105 derivative pairs,10 blocks,2 number-field parts) and1050 full Euler tensor entries (105 symmetric receiver entries,10 blocks), without calling the sparse row assembler. Each Gram/sigma identity includes all four-form output components. These groupings are not interchangeable proof counts. A deliberately changed solution coefficient fails the unchanged original equations; a changed affine receiver is also rejected. Source-dependent geometry is inherited/recomputed as stated, not counted as a fresh proof of all lower-jet premises.

## What the continuation settles and leaves open

The four isolated blocks did not obstruct the candidate. The joined solve proves that all ten tested blocks can coexist with cubic symmetry, including their mixed-pair L² terms. Its sparse solution is an actual coefficient witness; no separate-witness intersection inference is used. The solution is not claimed unique or invariant under changing the basis or elimination order.

The rest of W has directions involving horizontal components. Their actual Ricci Hessians are not covered by the vertical argument. Moreover the full system includes Euler rows in the other derivative slots and fourth-algebraic rows with fewer than two directions in this tested four-dimensional vertical subspace. Those rows can constrain coefficients already fixed here; extending by zeros is unjustified. The full coupled third-Euler/fourth-algebraic intersection remains open, alongside subsequent prolongations and local/global existence. K2384's unrestricted third Euler existence result remains intact.

The next constructive test must calculate the remaining actual curvature/Hessian receivers and solve them with the SAME shared unknowns, allowing the present free kernel rather than freezing this arbitrary sparse representative. Failure of this representative at an omitted equation would exclude that representative only. A genuine obstruction needs an exact dual combination of the full admitted rows, or a precisely scoped restricted-family verdict. Modular ranks, finite small-dimensional fixtures and matching scalar contractions cannot substitute for that certificate.

Independent read-only geometric review checked the baseline sign, true vertical Hessian argument, joined coordinate map and exact code. It identified a missing executed-source hash and requested direct tensor replay; both are included. The mathematical evidence remains internal exact computation and written reasoning, not proof-assistant, external-expert, native-GU or smooth-solution certification.
