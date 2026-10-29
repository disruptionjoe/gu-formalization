---
title: "K2239 Literal graph pullback increases observation rank but cannot erase the raw Jordan sector"
status: active_research
doc_type: exploration
created: "2026-10-29"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: literal graph observations of the unchanged observed-four raw equation; not the operator induced from full ambient dynamics
scripts:
  - tests/channel-swings/k2239_moving_observation_closure_probe.py
---

# K2239 Graph pullback: exact principal closure and a moving-kernel obstruction

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: exact principal-invariant kernel for literal graph pullback and obstruction to positive local closed refinement
carrier: supplied real1920 Cl77 raw carrier with V1152 and C768, four observed derivatives LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: positive-definite local current tested separately from raw Green forms ON=declared_carrier
real_structure: fixed real Clifford basis; ordinary real conjugation
grading: zero/one-form degree and copy splitting, not physical chirality or families
action_owner: repository-construction -- unchanged K2236 principal evolution and K2233 common lower coefficients
target: ordinary contraction along a supplied graph, compared with local first-order evolution quotient MAP-TYPE=intertwiner
```

## 1. The changed question and its precise limit

K2236 treats the horizontal graph and its rank768 closed refinement. This note allows arbitrary smooth graph slopes in the ACTUAL one-form contraction, while keeping K2236's four-derivative raw equation unchanged. This is more than conjugating an orthogonal projector: normal covector slots enter the observed one-form. It is less than deriving the operator induced by an ambient moving section. Restoring ten ambient derivatives, changing the tangent principal covectors, or moving Clifford data changes the theorem's inputs and requires a new calculation.

Keep O={0,7,8,9}, U its ten-element complement, eta=(+1 seven,-1 seven), and the normalized raw fields zeta_a=eta_a gamma_a u_a, nu=Wbar h. For a graph y^r=f^r(x), put B_mu r=partial_mu f^r. After invertible scalar normalization, ordinary pullback is

    (Q_B u)_mu=eta_mu gamma_mu u_mu + sum_(r in U) B_mu r eta_r gamma_r u_r,
    (Q_B u)_h=h.

This is contraction, not orthogonal projection. No graph, connection, carrier or bar is source-selected. The source section9 extraction supplies candidate four-field grammar; its lower-left signs are retained, and its southeast rival remains outside this chosen contraction. SC-OP-04 remains ASSERTS at candidate strength; SC-OP-05 and SC-META-53 remain UNCERTAIN. LT-SM8/LT-GR6b at ledger0.263 remain NEEDS.

Let A_j=D0^-1 D_j, j=7,8,9. On C768 write A_j=T_j tensor Cj with Cj=gamma0 gamma_j. On V1152, A_j=I9 tensor Cj. We inherit these identities from K2034/K2236 and use their original raw matrices. All statements about rank below are pointwise principal statements unless full closure is explicitly proved.

## 2. Scalar observability has a genuine dark line

Write C-coordinates as (a,b1,b2,b3,v,h), as in K2236. Let ell_h be its last coordinate row. The scalar rows

    ell_h                         = (0,0,0,0,0,1),
    ell_h T1                      = (0,0,1,1,10,0),
    ell_h T2                      = (0,1,0,1,10,0),
    ell_h T3                      = (0,1,1,0,10,0),
    ell_h T1 T2                   = (1,0,0,1,10,0)

are independent and have common kernel spanned by

    d=(-5,-5,-5,-5,1,0).

Every T_j fixes d, so the full scalar observation algebra has rank exactly5, not6. Clifford word factors are invertible; therefore the largest common A_j-invariant subspace inside ker(h) is

    Hdark=V plus (d tensor S).

This corrects a tempting but false shortcut: the scalar pullback alone does NOT see all of C. The explicit dark line is essential to the graph theorem.

## 3. Exact maximal principal-invariant hidden space

**Theorem.** For every real graph-slope matrix B, the largest subspace K inside ker Q_B invariant under all three A_j is exactly

    K_B = V intersect ker Q_B.

**Proof.** Since Q_B retains h, any such K lies in Hdark. Write a vector n in it as w+d tensor s, with w in V. Thus u_mu=-5s for all observed mu and u_r=w_r+s on normals, sum w_r=0. Every A_j acts on s and all w_r by the same Cj. The time pullback row is

    q0(n)=-5 gamma0 s + sum B_0r eta_r gamma_r(w_r+s).

Every normal gamma_r commutes with Cj, while gamma0 anticommutes with Cj. Since n and A_j n both lie in ker Q_B,

    0=q0(A_j n)-Cj q0(n)=-10 gamma0 Cj s.

The last coefficient is invertible, hence s=0 and K is contained in V. Conversely on V all four Q_B rows are sums of normal gamma_r, which commute with every Cj. Therefore V intersect ker Q_B is invariant. This proves equality. No assumption that B_0r vanishes or that the graph plane is orthogonal is used.

For every pointwise output R through which Q_B factors and which admits a first-order closed evolution quotient, principal intertwining forces ker R to be such an invariant subspace. Consequently

    rank R >= 1920-dim K_B = 768 + rank(Q_B restricted to V).

This sharp PRINCIPAL bound ranges from768 to1280. The horizontal graph attains768. A single slope B_01=1 gives rank(Q_B|V)=128, hence896. Four independent slopes, one in each row on distinct normals1,2,3,4, give rank512 and hence1280: choose the four corresponding w_r arbitrarily and compensate their sum in unused normal5. This also exhibits a nonzero maximal minor, so full rank512 is generic among real B (the exceptional set is a proper algebraic subset). If all Q_B|V vanish, equal normal-block matrices would be needed within each row, which Clifford independence forces to zero, so in fact rank768 occurs exactly for B=0.

For constant B the principal bound is attained by retaining R0 u=(a,b1,b2,b3,v,h) together with the image of Q_B P_V u, removing redundant image coordinates. Its kernel is K_B. The SAME K2233 lower coefficients preserve K_B: normal gamma_r commute with A=gamma0 J and Cj, and anticommute with T=product_U gamma_r. Hence each graph normal-row map intertwines mass A and the flavor generators Cj T,T up to their common signs. Thus constant B yields a full quotient for the supplied m,alpha, without fitting an adjoint or changing original returns.

## 4. Every closed refinement still contains the Jordan obstruction

Because ker R is contained in V, its intersection with C is zero. The original invariant C therefore embeds in every quotient refining Q_B, carrying the SAME T_j tensor Cj. K2236 gives nonzero N_j=T_j^2-I with N_j^2=0. Hence this embedded restriction is not diagonalizable. An operator selfadjoint under a positive-definite local form is diagonalizable, and every invariant subspace of such an operator has diagonalizable restriction. Therefore NO complete closed refinement of literal Q_B has a positive-definite local symmetrizer.

Smooth graph motion and derivatives of output coordinates do not remove this pointwise principal obstruction. Graph tilt can observe part of V's positive dynamics; the full closed output must also keep C. Positive subsystems, constrained solution spaces, nonlocal outputs, derivative-valued outputs and changed principal operators remain outside this conclusion. Nothing labels V or C as gauge. The inherited K2233 Green descent theorem concerned the horizontal quotient: do not extend its zero-form conclusion blindly to a tilted quotient, which can retain part of V and its raw pairing support.

### Constructive countercontrol: a literal graph sees positive constrained dynamics

Take the integrable constant-slope graph f1=t, all other f=0. Restrict the unchanged raw equation to the invariant algebraic subsystem W inside V defined by w1=s,w2=-s and all other w_r=0. Every raw coefficient preserves W because all normal copies share the same reduced equation E_alpha. Its literal pullback is q0=gamma1 s, q7=q8=q9=h=0. Since gamma1 is an orthogonal involution, commutes with Cj and A, and anticommutes with T, the observed q0 obeys E_(-alpha) q0=0 and inherits the positive Euclidean current. This is an actual positive, nonzero ordinary graph observation of a supplied invariant subsystem, unlike the horizontal graph's invisibility of all V. It does not contradict the full-quotient obstruction: restricting solutions to W removes C as an additional, explicitly supplied constraint. Neither that constraint nor the graph is derived from the source, a gauge symmetry, an action or boundary data. The result does not select physical modes or justify arbitrary differential constraints.

## 5. Moving graph derivatives impose additional closure, with a concrete failure

For E=partial_t+sum A_j partial_j+N and a smooth constant-rank output R, a quotient Ebar=partial_t+sum Abar_j partial_j+Nbar obeys Ebar R=R E precisely when

    R A_j=Abar_j R,
    partial_t R+sum Abar_j partial_j R+Nbar R-R N=0.

The first equation is the principal test. Once it holds, the second has some Nbar iff

    (partial_t R+sum Abar_j partial_j R-R N) ker R=0.

This is the exact lower-order kernel condition, not an optional correction. A moving geometric frame may supply such terms, but cannot alter the preceding symbol argument while principal inputs stay fixed.

An integrable graph shows why the principal minimum need not itself close. Set f1=t, f2=t^2/2, all other f=0, so the only nonzero slopes are B_01=1,B_02=t. Then Q_B|V=gamma1 w1+t gamma2 w2, rank128 at every t. The minimal principal output is R_t=(R0,Q_B P_V), rank896. Use constant mass m and alpha=0. At t=0 choose a spatially constant V datum w1=0,w2=s,w3=-s for s nonzero. Then R_0 u=0, whereas partial_t(R_t u)|_0 has added row gamma2 s, nonzero. The mass evolution cannot cancel it because it preserves w1=0 and acts by the same A on each copy. Equivalently (partial_t R-RN)ker R is nonzero. Thus this rank896 principal refinement is not a closed quotient for that moving graph.

A concrete repaired output is (R0,w1,w2), rank1024, with w=P_V u. Each retained normal component obeys the supplied V equation, so this output closes and reconstructs gamma1 w1+t gamma2 w2. This is an explicit sufficient refinement, not a universal minimum theorem over all moving outputs. It still contains C and its Jordan defect. The example distinguishes geometric observation motion from autonomous observed dynamics without changing the raw equation.

## 6. Independent review, controls and claim ceiling

Preflight compared the exhausted fixed-plane theorem, arbitrary frame relabeling, and true graph contraction. The last introduces new visible V content and a distinct exact rank formula. The scalar-only rank6 shortcut failed and was replaced by the rank5 dark-line proof. Postflight must challenge (i) whether h's word kernel really is Hdark, (ii) gamma0/normal commutator signs, (iii) principal versus full moving closure, (iv) a tilted output being confused with an orthogonal projector, and (v) improperly importing full ambient derivatives.

The exact probe constructs original normalized M matrices, derives evolution, verifies the five scalar rows, their rank5/common kernel, dark invariance, original full-slot V action, Clifford commutation and invertibility, graph rank witnesses, constant-B mass/flavor kernel intertwiners, nonzero Jordan square, and the moving-graph initial-jet failure. Faults change a time-row sign, dark coefficient, scalar word, evolution entry, lower-order derivative sign, graph normal output or falsely identify Q_B with a projector. Written universal arguments remain separate from finite controls. Independent internal review checked the actual kernel, constant-slope lower terms, moving-graph jet and symmetrizer arguments. It corrected a contradictory rank768 sentence and required the scalar-word fault to change the actual word rather than its expected row. Native verification accompanies this conditional result; no external acceptance is claimed.

No source polarity, physics-ledger row, canon, physical-state, generation, causal-domain, nonlinear PDE, external-expert, proof-assistant or novelty claim changes. The graph is a supplied observation of an unchanged four-derivative model. A source-owned induced operator, normal derivatives, genuine constraints and physical quotient remain substantive separate constructions.

## Reproduction

Run `python tests/channel-swings/k2239_moving_observation_closure_probe.py`. Its default recomputes exact controls and coefficient mutations and rejects stale note/probe/dependency hashes; `--write` refreshes the native report after review. Finite checks supplement the written proof.
