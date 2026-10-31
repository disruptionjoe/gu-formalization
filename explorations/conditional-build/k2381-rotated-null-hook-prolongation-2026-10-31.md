---
title: "K2381 Rotated null hook jets survive differentiated curvature compatibility"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no native GU or measured physical verdict
scripts:
  - tests/channel-swings/k2381_rotated_null_hook_prolongation_probe.py
---

# K2381 Rotated null hook jets survive differentiated curvature compatibility

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
result: K2381
carrier: zero-value real hook tensor with covariant jets on the actual K2345 metric LAYER=toy CHIRALITY=N/A
pairing: Levi-Civita signed metric and nondegenerate real Clifford trace ON=declared_carrier
real_structure: real Cl(7,7), exact rational plus sqrt2 jet coefficients
grading: hook896, grade-one and grade-five receivers with finite prolongation
action_owner: repository-construction -- selected comm/symi/symi I1 at fixed metric and epsilon
target: actual finite jet construction and contracted higher compatibility MAP-TYPE=evaluation
```

## Result and exact boundary

[K2378](k2378-null-hook-jet-compatibility-2026-10-31.md) constructs a null first jet, repairs its scalar curvature condition, and excludes a fixed second jet and a common-null77 repair. Here a larger rotating-null construction solves the **complete differentiated grade-one receiver**, preserves every mixed third-order norm/sigma identity, and then repairs the next fourteen curvature compatibility equations. It has an explicit exact coefficient certificate.

This does not establish the full third Euler jet, formal integrability or a stationary local solution. A smooth field extending the algebraic constraints is constructed below; its Euler equation is imposed only to the stated finite orders. SC-ACT-01/02/06 and SC-GEO-55 ASSERTS retain their exact source meaning, and SC-META-56 DISAVOWS requiring a separate odd action. The selected action remains conditional; no source, ledger or canon verdict moves.

## Frozen first jet and enlarged second-jet family

Use K2378's exact eta, pairs (p_r,q_r), coefficients d_i^r and repeated-index hooks H^r. In its seven-parameter family fix b1=-9012/493, all other b_r=0, and

    K_p_r=(1+b_r)H^r, K_q_r=b_r H^r.

This is at H=0, kappa^2=280/31 on the actual K2345 metric. It passes all hook identities, all pairwise norm/sigma constraints, B+B^T=-2Ric_tf and the contracted curvature condition. Let N be the full77-dimensional space of repeated-index hooks with arbitrary d_i^r, d_p_r=d_q_r=0 and sum_i d_i^r=0.

Let rho be the orthogonal representation on ALL THREE covariant hook indices. For A_l in so(7,7), set

    L_lm=rho(A_l)K_m+rho(A_m)K_l+N_lm,
    N_lm=N_ml in N.                                      (1)

There are1274 rotation coefficients and8085 symmetric N coefficients. These count parameters of this construction, not all possible second jets.

## Why all mixed algebraic constraints hold

In normal coordinates and an orthonormal frame whose connection vanishes at the point, choose smooth O(x) in O(7,7), O(0)=I with dO=A, and smooth N-valued f with f(0)=0, df=K, d2f=N_lm. For example O=exp(sum x_l A_l) and f the corresponding quadratic polynomial. Set H(x)=rho(O(x))f(x).

Every element of N has h^2=0 and sigma_H=0, including every linear combination, by K2378's repeated internal factor and mutually orthogonal null covectors. Orthogonal transport preserves both tensor equations. Hence h^2 and sigma vanish throughout a neighborhood for this smooth algebraic extension, and its covariant second jet is (1). In particular

    <L_ab,K_c>+<L_ac,K_b>+<L_bc,K_a>=0,
    polar(L_ab,K_c)+polar(L_ac,K_b)+polar(L_bc,K_a)=0.       (2)

This argument is stronger than merely fitting one scalar contraction. It also explains why a fixed common-null space was too restrictive: rotations can leave that space while preserving the null variety. It does not solve the Euler PDE off the point.

## Full actual receiver solved

The differentiated first-order field equation at H=0 is

    D(L)_lij=sum_m eta_m[L_lm;i m j+L_lm;j m i]=C_lij,
    C=-2 nabla Ric_tf=-2 nabla Ric.                        (3)

C has48 ordered nonzero entries. Its actual mixed formula is

    C(X,H,U)=(3/2)g(H,S_U X)

for horizontal X,H and traceless vertical U. Vertical derivatives and the trace vertical direction give zero. It is not a parallel-Ricci approximation. The probe independently reconstructs C from the full differentiated Riemann tensor below.

As a simple analytic witness that the old obstruction disappears, take A_2=T_(4,2)/4, where the boost sends e4 to e2 and e2 to e4. It produces D_2,4,2=3/4, precisely the previously forbidden source. A_3=T_(5,3)/4 similarly repairs the other paired source. The complete solve retains every receiver, not only these two.

Exact sparse elimination on the1470 symmetric receiver coordinates gives rank1057 for N alone and1403 for rotation plus N. Splitting Q(sqrt2) into two rational right-hand sides constructs a solution supported on146 rational and112 sqrt2 coefficients. Independently reconstructing the full tensor gives exact equality in all14^3 ordered receiver rows, with hook traces/skew/cyclic identities and all560 symmetric cubic derivative triples checked in each number-field component. The rank is a computed exact finite matrix rank, not a representation-theoretic general claim.

## Follow-through: the first witness fails the next curvature identity

Write F(P,Q) for the symmetric polarization of -8U/3+4W/3:

    F(P,Q)_ij=(2/3)sum_ab eta_a eta_b
      [P_aib Q_ajb+Q_aib P_ajb-P_iab Q_jab-Q_iab P_jab].    (4)

With R_aijk=g(e_a,R(e_j,e_k)e_i), the full double-divergence identity is

    -nabla^i(R^a_i{}^{jk} H_akj)=nabla^i nabla^j F(H,H)_ij.

Differentiate BEFORE setting H=0. Terms that vanish at H=0 may have nonzero derivatives. The necessary condition, for each l, is

    -sum_aijk eta_a eta_i eta_j eta_k [
        (nabla_i R_aijk)(K_l)_akj
       +(nabla_l R_aijk)(K_i)_akj
       +R_aijk(L_li)_akj]
      =2sum_ij eta_i eta_j [F(L_li,K_j)+F(K_i,L_lj)+F(K_l,L_ij)]_ij. (5)

Unknown third derivatives of H cancel. Thus (5) is fourteen affine linear conditions on L. The first solution of (3) fails twelve rows. For instance its l=10 defect is -17/774144; the full exact vector is retained in the report. The first solution remains a valid lower-order construction, not a stationary-field witness.

## Actual curvature derivative and independent checks

The probe loads the unchanged K2345 metric two-jet backend, transforms all1384 nonzero lowered curvature components to the adapted frame, and computes horizontal nabla R by connection action on all four slots. Coordinate horizontal derivatives vanish by translation invariance.

For vertical tangent E with S=g^-1E, GL congruence transport has J_H=-S/2 and J_V(F)=(S^T F+F S)/2. The actual backend gives Gamma_E=-J_E; the probe checks this cancellation on every component. Metric invariance therefore gives nabla_E R=0. This derives the vertical derivative; it is not an assumption that the full curvature is parallel. All2744 contracted Bianchi components are checked against the independently stated C:

    sum_i eta_i nabla_i R_aijk=(C_jak-C_kaj)/2.

The affine rows in (5) use these actual derivatives. Direct independent evaluation of all three F terms and R.L, separate from the coefficient-assembly routine, verifies the final solution.

## Repair and a finite surjectivity result

Append (5) to (3) and solve for the same family (1), preserving the fixed K. Over Q(sqrt2), the N map's rank rises from1057 to1071; the combined map rises from1403 to1417. The executable uses doubled rational matrices and records ranks2142 and2834 respectively. These numbers imply

    T(ker(D restricted to N)) = Q(sqrt2)^14,

where T is the linear-in-L part of (5). Indeed rank(D,T)-rank(D)=14 is exactly the image dimension of T on ker D. Thus for this FIXED K and actual curvature, every remaining affine defect in (5) can be repaired by an N-valued correction that preserves (3). Because N is common-null, it also preserves (2). This eliminates repeated searches for those fourteen compatibility conditions; they cannot obstruct this first jet at this stage.

The final exact solution has158 rational and119 sqrt2 nonzero parameter coefficients, serialized in the companion report. Full tensor reconstruction, all ordered receivers, all hook identities, all cubic norm/sigma constraints and all fourteen affine identities pass. It still is not the full twice-differentiated tensor Euler system. Neither this rank result nor one scalar repair proves every higher compatibility automatically soluble.

## Reproduction, controls and next condition

Run the companion probe with SymPy1.14 and Python's exact Fraction arithmetic; --write regenerates the report. The metric backend is dependency-hashed, as is the predecessor first-jet construction. Stored coefficients specify each N variable by (symmetric derivative pair, null pair, positive coefficient index, compensating trace index), and each A variable by derivative index and orthogonal generator. Separate rational and sqrt2 lists remove numerical tolerances.

Controls retain the common-null paired-source failure, the unextended witness's nonzero derivative defects and the original first-jet scalar repair. They are changed-construction tests, not independent solver-mutation proofs. Exact computation, symbolic local-extension proof and internal specialist review have separate roles. No Lean, external-expert or physical certificate is claimed.

Next impose the full twice-differentiated first-order Euler equation together with third covariant-derivative commutation, using R.K and the same actual geometry. A new third jet must also preserve the algebraic constraints; the smooth orbit extension supplies one algebraic realization but does not automatically meet that PDE. Higher contracted compatibility beyond (5), general hook fields, zero-kappa mixtures and nonradial odd branches remain open. Do not requeue the fixed-L exclusion or common-null77 support contradiction as an exclusion of the repaired rotating family.
