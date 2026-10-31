---
title: "K2384 The third Euler jet has one scalar compatibility condition"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no native GU or measured physical verdict
scripts:
  - tests/channel-swings/k2384_third_hook_jet_compatibility_probe.py
---

# K2384 The third Euler jet has one scalar compatibility condition

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
result: K2384
carrier: tracefree hook tensors and covariant jets on the selected14D metric LAYER=toy CHIRALITY=N/A
pairing: indefinite metric eta and induced nondegenerate tensor contractions ON=declared_carrier
real_structure: real rational and quadratic-field coefficient tensors
grading: radial odd field plus resonant grade-two hook branch
action_owner: repository-construction -- K2375 conditional selected action on the actual K2345 geometry
target: finite Euler jet existence and the next coupled algebraic system MAP-TYPE=evaluation
```

## Endpoint and its exact ceiling

[K2381](k2381-rotated-null-hook-prolongation-2026-10-31.md) stores a repaired first/second hook jet K,L at H=0, kappa²=280/31. Here a symbol theorem proves that this jet extends to **some full third covariant Euler jet**: the first-order Euler equation holds through two derivatives, and the norm/sigma equations hold through three derivatives. No third-jet coefficients are serialized here. The conclusion is an existence proof from the cokernel, not a computed10919-row solve or a stationary local solution.

The source objects remain distinct: SC-ACT-01/02/06 and SC-GEO-55 ASSERTS retain their statements; SC-META-56 DISAVOWS requiring a separate odd action. This conditional selected action and fixed metric do not adjudicate those source claims. Ledger0.263 and native physical-domain debts are unchanged.

## Tracefree-hook symbol theorem

Let V have dimension n>=3 and a nondegenerate real metric; the actual case is n14, signature(7,7). The hook space consists of H_ijk=-H_ikj, H_ijk+H_jki+H_kij=0 and g^ij H_ijk=0. Its dimension is n(n²-4)/3. Define

    D(H)_ij = nabla^k(H_ikj+H_jki).
    D_r: Sym^(r+1)V* tensor Hook -> Sym^r V* tensor Sym²_0 V*.

For r=0,1 this prolonged symbol is onto. For r>=2,

    dim coker D_r = binomial(n+r-3,r-2).                (1)

More precisely, the dual cokernel is the homogeneous scalar polynomials of degree r-2 multiplied by

    Q(xi)_ij = xi_i xi_j - (xi²/n)g_ij.               (2)

Derivative tensor and polynomial pairings use their usual factorial/symmetric normalization. These nonzero factors do not affect kernel dimension.

### First step: the actual nonnull symbol image

On an open positive-norm cone choose xi=e^0 with g00=1. The image of D_xi lies in tracefree S with S00=0: hook trace gives the first identity and skewness gives the second. Conversely for every such S, with spatial metric h and spatial indices a,b,c, set

    H_a0b=S_ab/2, H_ab0=-S_ab/2,
    H_00a=S_0a, H_0a0=-S_0a, H_0ab=0,
    H_abc=-(h_ab S_0c-h_ac S_0b)/(n-2).               (3)

Skewness, cyclic identity and trace follow directly. In the trace, H00a cancels the spatial sum -(n-2)S0a/(n-2); spatial trace S vanishes. D_xi H=S. Thus the pointwise adjoint kernel is precisely the line spanned by Q(xi). In an all-negative metric one can reverse its overall sign for this argument; the actual mixed metric already has an open positive cone. No positive-definite hook pairing is assumed.

### Second step: all polynomial syzygies, including null directions

Identify a dual element of Sym^r V* tensor Sym²_0 V* with a homogeneous tensor polynomial P(xi). Being in the prolonged adjoint kernel says D_xi* P(xi)=0 identically. On the nonnull open cone, P=a(xi)Q. This identity extends polynomially to all covectors. Initially a is rational, but Q's entries have greatest common divisor1: in diagonal metric its offdiagonal entries include x1x2,x1x3,x2x3, already with gcd1. A denominator of a in reduced form would have to divide every entry of Q, so there is none. Therefore a is homogeneous polynomial degree r-2. Conversely every such aQ is a syzygy. For r<2 only zero is possible. Null covectors create no extra polynomial syzygy, because an identity on an open nonnull set fixes a polynomial globally. This proves (1).

At n14, r2 the target has105*104=10920 dimensions and cokernel1, hence rank10919. At r3 the cokernel has14 dimensions. These large ranks are **analytically deduced**, not directly computed. Exact probes compute D0,D1,D2 at n3 and n4; D2 ranks29/30 and89/90. They also check (3) on all103 basis targets with S00=trace S=0 at the actual signature.

## Curved third derivatives are not symmetric

Put K_a=nabla_a H and M_abc=nabla_a nabla_b nabla_c H at H=0. With R_ab acting on every covariant hook slot, define

    P_ab;c = R_ab . K_c - K_(R_ab e_c),
    Q_a;bc = R_bc . K_a.

The two adjacent swaps require

    M_abc-M_bac=P_ab;c,    M_abc-M_acb=Q_a;bc.          (4)

A zero-total-symmetrization baseline is

    M0_abc=(3Q_a;bc+2P_ab;c+2P_ac;b+Q_b;ac+Q_c;ab)/6. (5)

Average the six differences M_abc-M_permuted to derive (5); curvature Bianchi makes the two swaps consistent. All admissible M are M0+S for a fully symmetric derivative triple S with hook values. Equivalently ordinary cubic Taylor coefficients in a normal frame parameterize that freedom. The probe verifies both swaps for every triple of a curved n3 fixture and rejects setting M symmetric. This fixture is a convention control; the actual geometry enters through the pinned curvature compatibility result, not by treating constant curvature as the actual metric.

## Applying the sole compatibility condition to the repaired actual jet

Write the selected receiver equation from K2375 as

    D(H) = -2 Ric_tf + F(H),
    F(H)=-8 U(H)/3+4 W(H)/3,

with its unchanged quadratic contractions. At H=0 the twice-differentiated equation is D(M_ab)=-2 nabla_a nabla_b Ric_tf+2 Fpolar(K_a,K_b), where Fpolar is the symmetric polarization of F; it is linear in M and has no L term. After inserting (5), its remaining target lies in Sym² derivative slots tensor Sym²_0 receiver slots. Derivative-pair antisymmetry vanishes by curvature acting on the already satisfied Euler equation. Its trace vanishes identically: tr U=h² and tr W=2h² imply tr F=0. The pairwise null Gram conditions on K separately preserve the unreduced norm/trace equations. These facts must precede using the tracefree symbol theorem.

The unique left-kernel contraction is g^ai g^bj times that residual: (2)'s pure receiver trace term drops. This is exactly the double-divergence compatibility identity derived before setting H=0 in [K2378](k2378-null-hook-jet-compatibility-2026-10-31.md), equations(8)--(9). It includes actual curvature times K and the quadratic K terms. It is not a flat divergence substitution.

For K2378's seven-parameter first jet, the stored exact defect is

    -(1120 b1 b2+1120 b1 b3+1972 b1+1120 b2 b3
      +1972 b2+1114 b3-3 b4-3 b6+36048)/3360.

K2381 uses b1=-9012/493 and all others0, making this zero exactly. The original all-zero parameters fail. With the sole cokernel functional zero, finite-dimensional linear algebra guarantees S solving the full residual equation. This implication uses the complete symbol theorem, not a numerical rank guess. L does not enter this second derivative of a quadratic receiver at H=0. The pinned K2381 L already obeys every mixed cubic norm/sigma identity, which depends only on K,L; changing M cannot disturb those order-three algebraic tests. Thus the specified finite third jet exists.

The r3 cokernel count explains the fourteen differentiated double-divergence conditions repaired in K2381. They exhaust that **unrestricted Euler** symbol compatibility level once the lower Euler jets and relevant trace conditions are satisfied. It is not a certificate that the full algebraically constrained fourth jet exists.

## Executed consequence: formulate the missing intersection exactly

Let P be either symmetric Gram polarization or four-form sigma polarization, and S=Sym M. The next, fourth derivative of P(H,H)=0 requires for all symmetric quadruples a,b,c,d

    sum_(4 singleton choices d) P(S_abc,K_d)
      + sum_(3 pairings ab|cd) P(L_ab,L_cd)=0.         (6)

The common factor2 from differentiating P(H,H) has been divided out. For one derivative direction this is4P(Saaa,Ka)+3P(Laa,Laa)=0, confirmed by the t4 coefficient of (kt+lt²/2+mt³/6)². The fully symmetric part of M0 is zero; (6) therefore acts on S.

Equation(6) is affine linear in S, with a fixed L² term. The Euler theorem proves nonemptiness of one affine set; K2381's smooth orbit extension proves an algebraic set is nonempty. Separate nonemptiness does not prove their intersection. The next construction is the simultaneous system D2 S=actual Euler residual AND(6) for both polarizations, using the SAME stored K,L. A dual inconsistency witness would exclude that fixed lower jet, while a compatible S would need the subsequent equations before any local-solution assertion. Scalar compatibility alone cannot answer this intersection.

## Further reduction of the quartic system

The repaired K has rank7 as a map from derivative directions into the hook fibre. Its kernel W has basis

    v_r=b_r e_p_r-(1+b_r)e_q_r, r=0,...,6.

Indeed K_p_r=(1+b_r)H^r, K_q_r=b_r H^r, and the seven H^r are independent. With the stored rotating representation L_ab=rho(A_a)K_b+rho(A_b)K_a+N_ab, directions v,w in W give L_vw=N_vw in the common-null space N. Thus every all-W quartic row in(6) vanishes automatically: there are binomial(10,4)=210 symmetric derivative quadruples, for each of the Gram and sigma equations. This is a structural consequence of common-null polarization, not210 independently computed third jets.

For v,w,z in W and arbitrary u, metric invariance and sigma equivariance reduce(6) to

    P(S_vwz-rho(A_v)N_wz-rho(A_w)N_vz-rho(A_z)N_vw,K_u)=0.

Here P(N,K_u)=0 identically and differentiating it under simultaneous orthogonal transport supplies the cancellation, also for the equivariant four-form output. Hence the complete three-W sector is parameterized by

    S_vwz=rho(A_v)N_wz+rho(A_w)N_vz+rho(A_z)N_vw+Z_vwz,
    Z_vwz in T_K,
    T_K={Z:Gram(Z,K_u)=0 and sigmaPolar(Z,K_u)=0 for all u}.

The probe independently reconstructs the seven H^r, verifies their rank and all seven kernel relations, and checks the stored N terms satisfy the defining repeated-index/common-null module conditions. This removes a whole sector of the quartic search without solving the remaining intersection. In particular it does not show these S components meet the Euler rows, and the sectors with two or fewer W directions still couple to the same unknown S. The next exact sparse solve should impose this parameterization and the remaining Euler/algebraic rows together; separate successful solves still do not compose.

## Reproduction and scope

The companion probe verifies small-dimensional full prolonged matrices, actual-signature nonnull right inverses, the polynomial gcd, actual repaired scalar from pinned K2378 evidence, curved swap conventions and quartic coefficients. The universal theorem and its actual-jet application are written proofs relying on the previously accepted K2378/K2381 curvature and tensor certificates. No giant matrix, stored third-jet coefficient array, new source theorem, local/global solution, proof-assistant or external-expert certification is claimed. Independent internal review checks this precise distinction.
