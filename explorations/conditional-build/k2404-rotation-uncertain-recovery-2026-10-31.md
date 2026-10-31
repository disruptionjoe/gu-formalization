---
title: "K2404 Convex clock uncertainty and the exact identity threshold"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no measured calibration, hardware or native GU verdict
scripts:
  - tests/channel-swings/k2404_rotation_uncertain_recovery_probe.py
---

# K2404 Convex clock uncertainty and the exact identity threshold

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
result: K2404
carrier: physical planar clock moment uncertainty and one common CPTP decoder LAYER=toy CHIRALITY=N/A
pairing: declared conditional probability or positive Hilbert channel pairing ON=declared_carrier
real_structure: real probabilities and exact rational or algebraic coefficients
grading: observed records, hidden roles and conditional parameters
action_owner: repository-construction -- K2395/K2398 sign instrument at fixed visibility and fixed loss weight
target: all-CPTP identity minimax criterion, non-mirror improvement and orientation threshold MAP-TYPE=evaluation
```

## Result and scope

[K2401](k2401-positive-visibility-minimax-recovery-2026-10-31.md) solved one mirror-law family. Here a compact convex uncertainty set U may contain arbitrarily many physical planar laws, with **one common visibility v in[0,1]**. Its members have m=E n, M=E nn^T for a unit planar axis n, so M>=0, tr M=1 and M−mm^T>=0. A single decoder must work across U. For the original sign instrument, identity-pointer recovery is globally minimax over all CPTP decoders exactly when

    some (m,M)∈U satisfies mm^T <= v² M.                    (1)

Then its normalized half-diamond error is(3−v)/4. This criterion also applies to the complete flagged problem at any fixed positive loss weight w, multiplying errors by w; w=0 is the trivial zero-error case. Good-flag decoders may be arbitrary in the lower bound. The result does not give a closed-form minimax value for every improving set.

This is positive-Hilbert qubit-channel mathematics for the supplied apparatus, not the source's physical quotient, SC-META-53 resolution, hardware calibration or LT-GR6b recovery.

## 1. Convex criterion and a constructive uniform gain

For R(r)=t+A r define B=t m^T+v A_plane M, f=tr B, k=B12−B21. After the common real-channel averaging of K2398 the exact normalized error is

    e_R(m,M)=[1+sqrt((2−f)²+k²)]/4.                        (2)

No law-dependent output rotation is permitted. K2395's pointwise all-CPTP Bell optimum F_*(m,M) equals v exactly when(1) holds. Identity has f=v,k=0 at every law. If U contains such a law, its pointwise optimum lower-bounds the robust optimum and identity attains it. This proves sufficiency, including the arbitrary good-flag recovery lower bound.

For necessity, the CPTP Choi set and U are compact convex and f is continuous bilinear. Finite-dimensional convex minimax gives

    max_R min_U f_R = min_U max_R f_R = v+Delta.            (3)

The compact minimum is strictly greater than v when(1) fails everywhere; hence Delta>0. This is a direct application of [Sion's minimax theorem](https://msp.org/pjm/1958/8-1/pjm-v8-n1-p14-p.pdf), with both compact convex domains and an affine continuous payoff. Real-channel averaging preserves f for all planar laws, so a single real R attains the left side. This minimax exchange concerns **f**, not the nonlinear diamond objective.

Every physical recovered branch is measure-and-prepare with a planar Bloch block. Therefore ||B||_*<=1, implying f²+k²<=1; it follows either by averaging rank-one output/input Bloch products or by the2x2 singular-value identity. Put d=f−v>=Delta and a=2−v. Since v>=0, d²+k²<=1+v²−2vf<=1. Also0<Delta<=1−v. The physical mixture

    R_Delta=(1−Delta)Id+Delta R

has f_Delta=v+Delta d and k_Delta=Delta k. Consequently

    (4e_Delta−1)² <= a²−(2a−1)Delta² < a².                (4)

It improves every law, with normalized gain at leastDelta²/8. Indeed rationalizing the square-root difference gives gain >=(2a−1)Delta²/(8a)>=Delta²/8 for1<=a<=2. A certified lower bound0<gamma<=Delta can replace Delta as mixture weight and guarantees gain>=gamma²/8. This supplies a usable synthesis/error margin from a robust Bell certificate; it does not assert that the Bell witness itself minimizes diamond error.

## 2. Rotation and orientation consequences

A complete finite cyclic orbit of order>=2 has a zero-mean average law in its convex hull. Thus identity is minimax, as for full unknown orientation. This follows from(1), without assuming the decoder is diagonal. SO(2) covariance alone allows A_plane=aI+bJ, where J is the90-degree rotation; it does not remove b. A reflection symmetry or objective argument would be needed for that additional reduction.

For a fixed isotropic M=I/2, condition(1) reduces to

    dist(0,conv{allowed means}) <= v/sqrt(2).              (5)

For means r(cos theta,sin theta), theta∈[−beta,beta],0<=beta<=pi, the sharp identity threshold is

    v_crit=sqrt(2) r max(cos beta,0).                       (6)

When beta<=pi/2, every mean has x>=r cos beta and the average of the two endpoints attains(r cos beta,0); when beta>=pi/2 the convex hull contains0. Taking r<=1/2 gives an explicit physical law for every mean: probabilities p_±X=1/4±m_x/2 and p_±Z=1/4±m_z/2, all nonnegative, reconstruct m and M=I/2. This is uncertainty about biased axis populations with fixed isotropic second moment, not an assertion about all rotated anisotropic laws.

## 3. Exact genuinely non-mirror uncertainty fixture

Take the convex hull of the following three physical means, all with M=I/2:

    m1=(1/2,0), m2=(3/10,2/5), m3=(3/10,−1/5).

Their triangle is scalene and has no reflection symmetry. Its closest point to0 is(3/10,0), attained with weights(0,1/3,2/3), because every point has x>=3/10. Therefore vcrit=3sqrt(2)/10 exactly. At v=1/4, use the fixed rational CPTP channel

    t=(12/25)X, A=diag(12/25,3/5,4/5) in x,y,z axes.

Its actual Choi matrix is positive, trace-preserving and rank2. Endpoint f values are(2/5,38/125,38/125) and skews(0,24/125,−12/125). Convexity of(2) makes the worst value over the entire triangle equal to the largest endpoint value,

    E=[1+sqrt(45520)/125]/4 < 11/16.                       (7)

The exact squared comparison is45520/15625<49/16. The gain(7/4−sqrt(45520)/125)/4 is the usable normalized margin; multiply by w and subtract a justified complete-channel implementation allowance. The probe reconstructs the underlying four-axis instruments, applies the decoder before the physical sign correction, and independently computes Bell-output trace norms. This is an upper-bound witness, not a general optimizer claim. At v>=vcrit the theorem proves identity exactly optimal, including threshold equality.

## 4. Why fixed visibility and trace matter

Containing a zero-mean law is insufficient if tr Q varies, where Q=E[v_axis nn^T]. Consider the physical convex hull of

    (m=0,Q=I/2), (m=X,Q=0).

The first is a uniform four-axis visibility-one law; the second a +X visibility-zero law. Their convex combinations are physical joint axis/visibility laws. Identity's worst normalized error is3/4. The one fixed decoder R=(Id+prepare X)/2 yields B=I/4 at the first endpoint and B=XX^T/2 at the second; f=1/2,k=0 throughout, so worst error is5/8. This refutes importing the fixed-trace sufficient condition into K2401's enlarged axis-dependent visibility polytope. That broader minimax problem remains a distinct construction.

## 5. Released consequence: solve that variable-trace family exactly

The preceding counterexample also admits an exact all-CPTP minimax solution. Common real-channel averaging and conjugation by X preserve BOTH endpoint laws. Conjugation by X acts on the instrument plane as(x,z)->(x,−z); combined averaging leaves t=cX and diagonal A=(x,y,z). Convexity of the error means averaging cannot worsen the worst endpoint. This is a common physical channel mixture, not a law-dependent rotation. The endpoint skews vanish and their traces are(x+z)/2 and c. Thus minimize error by maximizing min(c,(x+z)/2).

The full diagonal-channel CP inequalities are those of K2401. One may take c,x,z>=0: negative c cannot improve the positive feasible bound; for fixed c the maximal x+z occurs with nonnegative x,z (the CP envelope for z is even in x). At the CP boundary x=yz, c²=(1−y²)(1−z²). For fixed0<c<1, maximize

    S(c)=max_y (1+y)sqrt(1−c²/(1−y²))/2,
    0<=y<=sqrt(1−c²).

Differentiating its square gives the unique interior maximum c²=(1+y)(1−y)², z²=y. The right side is strictly decreasing1→0 on y∈[0,1], covering every c. This optimum S(c) strictly decreases1→0 with c: for fixed y the objective decreases strictly in c and the allowed interval shrinks. Therefore max_c min(c,S(c)) occurs at the unique c=S(c). Squaring, with both sides nonnegative, gives3y²−9y+4=0. The root in(0,1) is

    y_*=(9−sqrt33)/6, z_*=sqrt(y_*), x_*=y_*sqrt(y_*),
    c_*=(1−y_*)sqrt(1+y_*)=sqrt(y_*)(1+y_*)/2,
    E_*=(3−c_*)/4.                                      (8)

In particular c_*²=(69−11sqrt33)/18>1/4, so E_*<5/8. Both original endpoint channels attain the same error. Their convex hull cannot have a larger error, proving the exact robust optimum. The complete flagged value is wE_* even allowing arbitrary good-flag recovery: each endpoint Bell lower bound is w(3−f_endpoint)/4 since the good branch entanglement fidelity is at most1, and good identity plus this diagonal decoder attains it. This solves this physical variable-trace segment only; general variable-trace uncertainty remains open.

## Verification and continuation

Exact matrix/affine checks cover probability and moment reconstruction, Choi positivity/trace preservation, original sign-block composition, Bell-output norms, threshold equality, orientation examples, variable-trace counterexample and its exact optimal CPTP decoder. Controls reject a dropped skew term and the covariance-only diagonal inference. The universal criterion uses the written compact minimax and physical-mixture proof; finite checks are not independent proofs of it. Independent internal review found and corrected the SO(2) and variable-trace traps. No novelty, external-expert, hardware or proof-assistant claim is made. Next useful work needs a calibrated uncertainty set and full implementation costs, or a certified general variable-trace robust optimizer with a specified consuming experiment.
