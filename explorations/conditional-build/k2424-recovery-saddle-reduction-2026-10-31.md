---
title: "K2424 Recovery support in radicals and a two-variable saddle"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional positive-Hilbert channel mathematics; no native GU or device verdict
scripts:
  - tests/channel-swings/k2424_recovery_saddle_reduction_probe.py
---

# K2424 Recovery support in radicals and a two-variable saddle

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
result: K2424
carrier: physical planar flagged qubit instruments with shared good and bad decoders LAYER=toy CHIRALITY=N/A
pairing: half-diamond channel error and output-first unnormalized Choi trace ON=declared_instrument
real_structure: real planar Bloch data with complex Hermitian positive Choi matrices
grading: good/bad records; planar and perpendicular channel blocks
action_owner: repository-construction -- inherited recorded-instrument model
target: arbitrary planar support and compact two-variable global recovery MAP-TYPE=evaluation
```

## Results

The complete bad-decoder semidefinite optimization in [K2422](k2422-joint-recovery-optimality-2026-10-31.md) has an explicit radical support formula, even when its matrix is nonsymmetric. For two strictly positive-loss laws, common rotation and normalization reduce the entire unrestricted minimax problem to a **compact maximum in two real variables**. This extends [K2395](k2395-planar-recovery-closed-form-2026-10-31.md)'s symmetric physical-moment formula; it does not claim a new general semidefinite-duality method.

For the actual asymmetric K2419 instruments, a rational scalar candidate gives an exact radical physical decoder and a rigorous global bracket:

    0.446966996608947629838642518 < E* < 0.446966996608947629838642519.

Its width is 10^(-27). The inequalities follow from a valid global lower certificate and an actual common CPTP controller, not a numerical stationary-point claim. The exact maximizing algebraic point and uniqueness remain unproved. These are conditional positive-Hilbert channel results; SC-META-53 remains UNCERTAIN. No native GU quotient, calibrated device, physics-ledger change, novelty or external-expert acceptance is claimed.

## 1. Arbitrary real planar support

Use output-first unnormalized Choi J, Tr_out J=I2, and Frobenius pairing <M,A>=Tr(M^T A). For arbitrary real v in R2 and M in R^(2x2), define

    Phi(v,M) = max_CPTP [v.t + <M,A>],
    T=Tr(M M^T), delta=|det M|,
    h=lambda_max(v v^T - M M^T).

Then

    Phi^2 = T+2delta                  if h<=delta,
    Phi^2 = T+h+delta^2/h             if h>delta.          (1)

Only the second branch divides by h, which is strictly positive there. M need not be symmetric, positive or a physical moment matrix. Transposing the wrong product changes the answer: output-space h uses M M^T.

Complex-conjugate Kraus averaging preserves the objective and gives a real Choi matrix. An extreme point of the real TP spectrahedron has rank at most two: supported symmetric perturbations have r(r+1)/2 dimensions, and partial trace imposes at most three independent real constraints. For r>=3 a nonzero supported, trace-preserving perturbation contradicts extremality. The [Ruskai–Szarek–Werner classification, Theorem12 and Theorem4/Eqs15–17](https://arxiv.org/pdf/quant-ph/0101003), then supplies the generalized-extreme canonical form.

For nonzero translation, real-planar structure places the translation/product-singular output direction k in the plane. The remaining planar/perpendicular singular directions can be chosen in their invariant subspaces, including degenerate spaces and kernels. Thus

    t=sqrt(1-c^2)sqrt(1-d^2) k,
    A=c Q diag(1,d) O,  Q=[l k],  l perpendicular k,
    0<=c,d<=1, O in O(2),
    perpendicular multiplier = d det(Q)det(O).

Both signs of the planar determinant are physical: a planar orthogonal map lifts to SO(3) by its determinant on the perpendicular axis. If t=0, contraction bounds the support by ||M||*, attained by a physical orthogonal polar lift; this gives the first-branch baseline.

For fixed k,d, optimizing O gives S=||M^T Q diag(1,d)||*. Choose k's sign so a=v.k>=0. Optimizing c in a sqrt(1-c^2)sqrt(1-d^2)+cS gives

    Phi^2=max_(k,d) [T+2delta d+(1-d^2)k^T(vv^T-MM^T)k].

A top eigenvector maximizes k. The scalar maximum on 0<=d<=1 is at d=1 when h<=delta and at d=delta/h otherwise, proving(1). Singular polar factors use an orthogonal extension; v=M=0 is the zero-support case.

## 2. Explicit physical primal and singular dual

In the improving branch with simple h and det M!=0, let P be its top eigenprojection, d=delta/h and phi=Phi. A convenient formula without a polar decomposition is

    t=(1-d^2)Pv/phi,
    A=[M-(1-d^2)PM+d sign(det M)cof(M)]/phi,
    y=d sign(det M),
    cof(M)=[[M22,-M21],[-M12,M11]].                    (2)

This is the cofactor matrix, not the adjugate. To verify physicality, put L=I-(1-d)P. The canonical solution is A=(||LM||*/phi)L polar(LM). The nonsingular2x2 polar identity and L cof(L)=dI give(2). The canonical two-Kraus construction therefore proves exact CP and TP, even though the Choi matrix lies on a singular boundary. Rounded eigenvalues are not needed.

With H=(v.sigma tensor I+sum M_ab sigma_a tensor sigma_b^T)/2, a matching support dual is

    Z=[phi I+(A^T v+M^T t).sigma]/2,
    D=I tensor Z-H >=0, DJ=0.                         (3)

Strong duality gives complementarity for the support optimizer. Taking the output partial trace of HJ forces Z; input-rotation stationarity makes M^T A symmetric, so the Pauli product yields(3). Uniqueness follows because (I tensor DeltaZ)J=0 and Tr_out J=I imply Tr(DeltaZ^2)=0. This is a support optimizer; minimax optima on nondifferentiable exposed faces can require mixtures. Do not infer rank-two minimax recovery universally.

For v=(3,0), M=[[0,2],[1,0]], equations(1)–(3) give phi=3sqrt(30)/5,

    t=(7sqrt(30)/50,0),
    A=[[0,sqrt(30)/25],[sqrt(30)/10,0]], y=-2/5,
    Z=(3sqrt(30)/10)I+(sqrt(30)/5)Z_Pauli.

The probe checks the original Choi, all principal minors, support equality and DJ=0. A rank-one nonsymmetric fixture, a reflected unitary, pure preparation and zero objective cover singular and orientation boundaries.

## 3. Compact two-scalar global problem

Retain K2422's physical sign instruments, common good decoder, arbitrary shared bad CPTP decoder, and strictly positive losses w1,w2. In its attained joint dual, q_i lies in a disk of radius p_i and sum p_i=1. Rotating every q_i together rotates s,v,M and preserves the good norm and bad support. Only 2sum q_ci changes. Therefore a maximizer may, and every maximizer must, satisfy sum q_si=0 with nonnegative cosine resultant.

At a saddle, ell_ci>=w_i>0 and L_i>0 imply q_i=p_i ell_i/L_i. Thus q_ci>=0 and ||q_i||=p_i. Let C=sum q_ci>0 and write the unnormalized vectors

    qraw1=(lambda,-tau), qraw2=(1-lambda,tau),
    r_i=||qraw_i||, R=r1+r2,
    q_i=qraw_i/R, p_i=r_i/R.

Define F(q)=[[q_c,q_s],[-q_s,q_c]] and

    s=sum (1-w_i)qraw_i,
    V=sum w_i F(qraw_i)m_i,
    N=sum w_i F(qraw_i)Q_i.

The exact unrestricted value is

    4E*=max [w1*r1+w2*r2+2-2||s||-Phi(V,N)]/R.        (4)

Every candidate in(4) is a feasible dual; attainment and the saddle argument prove that the domain contains an optimizer. No independent channel variables or matrix optimization remain.

A compact domain retaining an optimizer is

    0<=lambda<=1,
    tau^2<=K1^2 lambda^2,
    tau^2<=K2^2 (1-lambda)^2,
    Ki^2=(2-wi)^2/[wi(4-wi)].                         (5)

Indeed ||B_i||*<=1 for physical pointer outputs. The vector ell_i lies in the disk centered at(2,0) of radius2-w_i. Its tangent slopes give |ell_si|/ell_ci<=Ki, and q_i has that same direction on active support. For the actual pair K1^2=16129/23871 and K2^2=4489/6327. Inactive endpoint weights yield tau=0, not an undefined direction. Another valid compact bound from identity upper E0 is |tau|<=max_i(4E0-w_i)/(2w_i), here579/740. These bounds restrict a domain retaining optimum; arbitrary feasible duals need not obey them.

The objective is not claimed concave in these projective coordinates. A root search alone must still compare boundaries, det N=0, h=delta, repeated eigenvalues and s=0. Rational-input semialgebraicity makes the optimal value algebraic but does not identify its polynomial/root.

## 4. Original asymmetric pair: certified follow-through

Retain exactly K2419's laws:

    m1=(125/338,150/169), m2=(49/250,-84/125),
    w1=73/100, w2=37/52,
    axes u_i= m_i/||m_i||,
    probabilities(1+||m_i||)/2 and(1-||m_i||)/2 on +/-u_i,
    visibility1/2, Q_i=u_i u_i^T/2.

Search suggested the rational candidate

    lambda=518217355906395628505131873324/10^30,
    tau=57537330873480255935665491873/10^30.

It is not asserted to be the exact maximizing point. The probe evaluates(4) using Arb at256 bits, certifies the compact-domain and simple improving positive-determinant branch, and constructs(2) with M=N,v=V. The good decoder is the unitary with conformal vector s/||s||. These are one common pair of exact radical physical decoders.

The original sign maps are composed symbolically for both laws before evaluating their complete-channel norm. For this candidate the probe certifies H_i^2<w_i^2<L_i^2, so the full norm is(w_i+L_i)/4. The lower dual exceeds the lower displayed rational endpoint and both actual endpoint errors lie below the upper endpoint. Consequently the global optimum lies between them, with no global root-search assumption. Complete-instrument convex mixtures inherit this same controller bound by convexity; arbitrary independently averaged moments do not.

This follows the structural reduction into an executable original-channel certificate. More decimal refinement has no stated physical payoff. The remaining exact mathematical question is algebraic point isolation/global optimality and possible uniqueness; physical consumption needs a measured law and full apparatus error/cost budget.

## Verification

[Probe](../../tests/channel-swings/k2424_recovery_saddle_reduction_probe.py) and [report](../../lab/process/k2424-recovery-saddle-reduction.json):51 grouped exact/interval checks, five contrary controls, original Choi and sign-map composition, singular matching certificates, exact compact constants, rigorous global bracket. Dependencies include SymPy and python-flint (Arb). Finite fixtures validate the implementation; the universal reduction rests on the written argument and independent internal specialist review. No external-expert or proof-assistant certification.
