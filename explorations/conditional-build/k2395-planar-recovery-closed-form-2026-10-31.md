---
title: "K2395 Closed-form optimal recovery for arbitrary planar clock laws"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional finite-channel mathematics; no native GU or hardware verdict
scripts:
  - tests/channel-swings/k2395_planar_recovery_closed_form_probe.py
---

# K2395 Closed-form optimal recovery for arbitrary planar clock laws

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
result: K2395
carrier: K2392 flagged instrument with classical survivor sign and coherent clock qubit plus untouched reference LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert pairing and half-diamond distance ON=declared_carrier
real_structure: complex qubit channels and real planar moment matrices
grading: good flags and two-loss survivor sign
action_owner: repository-construction -- stipulated K2389 QND clock and loss instrument
target: closed-form all-CPTP optimum and one-reset-qubit optimizer MAP-TYPE=evaluation
```

## Result

For the exact K2392 instrument, let m=E n, M=E nn^T over a known planar unit-axis law, visibility 0<=nu<=1, and complete two-loss probability w. In particular M is symmetric positive semidefinite, tr M=1, and M-mm^T>=0. The first and second moments are supplied true moments, not inferred from estimated means alone. Put

    D=det M,
    H=m m^T-nu^2 M^2,
    h=lambda_max(H).

Then the complete optimal half-diamond recovery error over every CPTP decoder is

    e_*=w(3-F_*)/4,
    F_*=nu,                                      h<=nu^2 D,
    F_*=sqrt[nu^2 tr(M^2)+h+nu^4 D^2/h],          h>nu^2 D.       (1)

Only the second branch divides by h, which is strictly positive there. This closes the elementary arbitrary-planar-law optimum left open by K2392. It does not reconstruct the source-native physical quotient, calibrate an apparatus or change SC-META-53/LT-GR6b. The formula's hypotheses include the original sign blocks, their input-dependent traces and the recovery resource class; changing those changes the problem.

## Complete reduction to two real Kraus operators

K2392 gives the objective

    max_R F(R)=m·t+nu tr(A M),                         (2)

for R(r)=t+A r, with one R applied to each original pointer block and a physical output sign flip after R. Averaging complex-conjugate Kraus channels preserves (2) because the instrument plane is xz. This gives a real symmetric positive Choi matrix with tr_out J=I. This averaging is a mixture of CPTP maps, not an implemented antiunitary.

An optimum can be taken extreme in this compact real spectrahedron. If its Choi rank is r, the real symmetric perturbations supported on its range have dimension r(r+1)/2. Partial trace imposes at most three real symmetric constraints. For r>=3 there is a nonzero constraint-preserving supported perturbation, and both sufficiently small signs preserve positivity, contradicting extremality. Thus an optimum has Choi rank at most two.

We use precisely the rank-two qubit-channel classification of Ruskai, Szarek and Werner, Theorem12 and Theorem4/Eqs15–17 in [An Analysis of Completely-Positive Trace-Preserving Maps on M2](https://arxiv.org/pdf/quant-ph/0101003). It identifies rank<=2 channels with their generalized-extreme canonical form: signed singular values c,d,cd and translation of magnitude sqrt((1-c^2)(1-d^2)) along the product-singular output axis.

Here is the additional planar step needed for this problem. For a real Choi channel, t lies in xz and the perpendicular Bloch axis decouples from xz. If t is nonzero, its canonical product-singular direction is in the plane. The remaining planar direction and the perpendicular direction are singular directions (within a degenerate singular space one chooses the real planar/perpendicular basis). Input and output planar orthogonal transformations therefore give

    t=sqrt((1-c^2)(1-d^2)) k,
    A_plane=Q diag(c,c d) O,
    Q=[l k],  l perpendicular k,  0<=c,d<=1, O in O(2).       (3)

Signs are absorbed in the orthogonal factors and the choice of k; every planar orthogonal factor lifts to a physical SO(3) rotation with perpendicular component its determinant. Rank-zero/singular directions allow the same form by choosing bases in their kernel. If the original t=0, no canonical reduction is needed for the upper bound: trace-distance contraction gives ||A||op<=1 and hence F<=nu tr M=nu. Identity attains this value. Such unital optima are covered by the first branch.

Conversely every (3) is a physical channel: its third contraction is d, up to the determinant signs of the planar lifts; the two-Kraus construction below establishes positivity. Thus no ansatz is silently substituted for all CPTP maps.

## Analytic maximization

Choose k's sign so a=m·k>=0. Let K=k^T M^2 k, L=l^T M^2 l. Optimizing the input orthogonal matrix O gives the trace norm of M Q diag(1,d). For any real 2x2 matrix X, ||X||_*^2=tr(X^T X)+2|det X|. Consequently

    max_O F=a sqrt(1-c^2) sqrt(1-d^2)
            +nu c sqrt(L+d^2 K+2dD).                       (4)

Cauchy–Schwarz on (sqrt(1-c^2),c), with nonnegative coefficients, gives an attained maximum over c:

    (max_c,O F)^2=a^2(1-d^2)+nu^2(L+d^2K+2dD)
      =nu^2 tr(M^2)+2nu^2 D d+(1-d^2) k^T H k.             (5)

Since 0<=d<=1, maximizing k selects a top eigenvector of H, independent of d. The remaining scalar problem is

    F_*^2=max_{0<=d<=1} [nu^2 tr(M^2)+2nu^2 D d+(1-d^2)h]. (6)

If h<=nu^2D, the derivative 2nu^2D-2hd is nonnegative on the interval; d=1 gives nu^2 since tr M=1. If h>nu^2D, the concave quadratic is maximized at d=nu^2D/h, giving (1). Endpoints and degeneracies are included without division in the first branch.

The reduction gives a Bell-optimal decoder. K2392's sign pairing makes the full branch unital with planar Bloch block B=t m^T+nu A M. If needed a physical output polar rotation makes B positive semidefinite without decreasing its trace; at a global optimum the trace cannot increase. Every planar orthogonal output lift commutes, as a channel, with the survivor sign flip (the pi rotation about the perpendicular axis), so this common output polar rotation is implemented in the permitted sign-decoder structure. Simultaneous input/output coordinate changes preserve comparison with the identity channel. The resulting Pauli channel has identity weight (1+F_*)/4 and zero perpendicular contraction. Its Bell lower bound matches its half-diamond upper bound, including arbitrary entangled reference inputs. Good flags contribute the identity with weight1-w, establishing the first line of (1).

## Explicit optimizer and reduced reset dimension

In the improving branch select any unit top eigenvector k of H with m·k>=0, choose a perpendicular l and set

    d=nu^2 D/h,
    a=m·k,
    S=sqrt(l^T M^2 l+d^2 k^T M^2 k+2dD),
    c=nu S/F_*,
    sqrt(1-c^2)=a sqrt(1-d^2)/F_* .                    (7)

Choose O maximizing tr[O M Q diag(1,d)], using the polar decomposition. If that matrix is singular an orthogonal polar extension exists and any maximizing extension suffices. Equations(3),(7) construct the optimizer. When nu=0 they reduce to pure preparation along m. Identity is an optimizer throughout the first branch. A nonzero improving optimum has F_*>0, so (7) does not divide by zero.

Set u=arccos c, v=arccos d, alpha=(v-u)/2, beta=(v+u)/2. In canonical x,z plane coordinates, use

    K0=diag(cos alpha,cos beta),
    K1=[[0,sin beta],[sin alpha,0]].                    (8)

Then sum K†K=I; the Bloch translation is sin u sin v along z and contractions are (c,d,cd). These identities hold even if alpha is negative. Apply the input and output planar lifts from (3), then the original survivor sign correction AFTER this channel. A two-Kraus map has a dilation with one fresh reset qubit. Thus one reset qubit suffices for an exact optimum for every known planar law, improving K2392's generic four-dimensional-environment sufficient bound. This is a dimension/synthesis existence result, not a free operation or universal hardware gate count.

The existing commuting-Pauli dilation exp{-i[(v/2) X⊗Y-(u/2)Y⊗X]} provides one construction before basis rotations, using K2389's convention. Angle precision, rotations, reset, waiting, survivor-conditioned output and final routing require physical accounting. The old identity-pointer23-gate bound does not price the new optimizer.

## Controls, exact nonaligned fixture and margin

Since M^2+D I=M for trace-one 2x2 M,

    h<=nu^2D  iff  mm^T<=nu^2M.                       (9)

For true moments and nu>0 this is exactly m^T M^+m<=nu^2 with m in range M, reproducing K2392's identity-optimality theorem including rank-one M. Zero visibility gives F_*=||m||; zero mean gives F_*=nu; noiseless pointer gives F_*=1. For M=diag(lambda,1-lambda), m=(a,0), (1) reduces to K2389's aligned formula. Rank-one M gives F_*=max(||m||,nu).

For K2392's nonaligned law m=(3/4,1/4), M=diag(3/4,1/4), nu=19/20,

    D=3/16,
    h=(195+12sqrt(10169))/6400,
    F_*^2=361/640+h+(1083/6400)^2/h.                  (10)

This exact radical expression can be checked against the previously independent rational primal/dual interval. It replaces neither endpoint certificate nor its correction history. It supplies the exact optimum between them, and lies strictly above nu. The mean direction is not the optimizer direction in general: use the top eigenvector of H, not a scalar projection of M onto m.

The excess is especially transparent:

    F_*^2-nu^2=(h-nu^2D)^2/h,
    F_*-nu=(h-nu^2D)^2/[h(F_*+nu)]                  (11)

in the improving branch. The ideal complete-error gain over identity-pointer recovery is w(F_*-nu)/4. It vanishes quadratically as h approaches a positive threshold nu^2D; singular/zero threshold limits must instead use (11) directly. Hence a strict mathematical gain near threshold can be too small to survive an added implementation cost. If the complete implemented optimal decoder/instrument differs from the ideal by half-diamond epsilon, a sufficient improvement over the ideal identity-pointer design is

    epsilon < w(h-nu^2D)^2/[4h(F_*+nu)].              (12)

Comparison of two actual devices requires both complete error budgets. No calibrated cost, measured law or physical-rate feasibility follows from moment optimality alone. If w=0 every decoder has complete error zero; the normalized optimum remains mathematically defined but has no complete-device gain.

## An exact nonaligned optimizer for reconstruction checks

A second fixture has m=(1/2,23/72), M=diag(3/4,1/4), nu=25/36. Its moment block is positive since m^T M^-1 m=961/1296<1. Such a block does define an abstract unit-circle law: the compact set of real positive 3x3 moment matrices with upper-left entry1 and lower 2x2 trace1 has only rank-one extreme points. A rank>=2 support has more than two symmetric perturbation directions and so cannot be extreme. Its rank-one members are (1,n)(1,n)^T with ||n||=1; convex decomposition proves realizability. This is an abstract moment construction, not empirical calibration or a physical timing schedule.

Here k=(3/5,4/5), h=1325/6912, d=25/53, m·k=5/9, c^2=673/1219, and F_*^2=2300/4293. The probe reconstructs the physical planar rotations, actual Choi/Kraus map and original sign-block composition exactly. It checks the formula against this independently constructed decoder, not only against itself.

## Boundaries and continuation

The universal optimization now has a closed formula. The next substantive physical continuation is a supplied nonaligned law with calibrated QND coupling, moment uncertainty and complete reset/control costs compared on the same apparatus. Alternatively extend to a specifically defined nonplanar pointer instrument; (3) and the fixed sign flip must not be transported silently.

Countercontrols must reject the scalar aligned formula on (10), an arbitrary transposition map masquerading as CP recovery, applying one nonunital R after sign correction on both blocks, and using moment estimates as exact law data. The weakest reproducibility seam is the orientation convention in the two physical planar rotations: verify the Kraus-derived A/t and actual sign-block composition, rather than only substituting numbers into (1). Exact symbolic canonical identities and radical inequalities support the written proof; numerical optimizers or random channels may be diagnostics only. Independent internal review is required; no external expert, proof-assistant or hardware certification is claimed.
