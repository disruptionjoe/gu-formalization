---
title: "K2413 Full joint recovery optimum from channel contraction"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional quantum channel theorem; no hardware or native GU verdict
scripts:
  - tests/channel-swings/k2413_joint_recovery_optimum_probe.py
---

# K2413 Full joint recovery optimum from channel contraction

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
result: K2413
carrier: flagged positive-Hilbert qubit sign instrument with uncertain joint loss and planar clock law LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert channel pairing ON=declared_carrier
real_structure: real probabilities and rational or algebraic channel coefficients
grading: good/bad flags, binary survivor signs and conditional clock axes
action_owner: repository-construction -- K2398/K2407 sign instrument
target: unrestricted joint recovery optimum and stability under variable loss MAP-TYPE=evaluation
```

## Result and preflight

The algebraic good-Y-rotation optimizer in [K2410](k2410-variable-loss-recovery-2026-10-31.md)
is optimal over **all** good/bad CPTP qubit recoveries for that two-law
visibility-zero fixture, and for the convex hull of its complete instruments.
Its previously certified restricted value is therefore the unrestricted value:

    0.5194114591 < E* < 0.5194114592.

The same proof gives a general sufficient certificate and an explicit loss
penalty for nonunitary conformal contraction. This is conditional positive-
Hilbert channel mathematics. SC-META-53 remains UNCERTAIN and LT-GR6b remains
unchanged; no GU physical quotient, measured calibration or hardware advantage
is inferred. The imported instrument and uncertainty set remain assumptions.

Preflight compared mixed-unitary classification, a larger conic search and a
contraction lower bound. The last eliminates the full optimization without
assuming the optimizer is unitary. The common sign/real averages and complete
half-diamond formula are inherited from K2410; their hypotheses include one
fixed controller used across laws, planar means and zero bad visibility.

## 1. A lower bound covering every channel

After those simultaneous physical averages, the good channel is unital with
real planar block G and perpendicular multiplier g; bad recovery reduces to
preparing a planar Bloch vector t, ||t||<=1. Let

    J=[[0,1],[-1,0]],  P=(G+J G J^T)/2=[[a,b],[-b,a]],
    a=tr(G)/2, b=(G12-G21)/2, r=sqrt(a^2+b^2).

A positive unital qubit channel maps the Bloch ball into itself, so
||G||op<=1 and g<=1. Convexity of operator norm gives r=||P||op<=1.
This argument covers anisotropy, reflections and mixtures; no assertion that
G itself is a rotation is used.

For two laws with 0<w_i<1 and 0<n_i=||m_i||<=1, define

    alpha_i=w_i n_i, A_i=2 m_i/(w_i n_i^2), B_i=(1-w_i)A_i,
    A=A_1-A_2, B=B_1-B_2, c_i=A_i-P B_i,
    q_1=alpha_2/(alpha_1+alpha_2), q_2=alpha_1/(alpha_1+alpha_2),
    k=alpha_1 alpha_2/(alpha_1+alpha_2).

For C_i=I-(1-w_i)G-w_i t m_i^T the complete norm's lower branch is
E_i >= (d_i+L_i)/4, where d_i=1-(1-w_i)g and
L_i^2=(tr C_i)^2+(C_i12-C_i21)^2.
Direct polynomial expansion gives L_i=alpha_i||t-c_i||.
Consequently

    max_i E_i >= sum_i q_i E_i
      >= [sum_i q_i d_i+k(||t-c_1||+||t-c_2||)]/4
      >= [sum_i q_i w_i+k||A-PB||]/4
      >= [sum_i q_i w_i+k(||A||-||B||)]/4 = E* .       (1)

The last lower bound remains valid even when negative, but the useful
attainment theorem below assumes ||A||>||B||. Omitting other diamond branches
is legitimate for a LOWER bound only. Physical feasibility and those branches
must still be checked at an attaining controller.

## 2. Attainment theorem and the exact fixture

Assume A,B are nonzero, D=||A||-||B||>0. Choose the proper planar rotation
P* mapping B/||B|| to A/||A||, and implement it as a Y-axis qubit unitary,
with g=1. Define its centers c_i and

    ell_1=(w_2-w_1+alpha_2 D)/(alpha_1+alpha_2),
    ell_2=D-ell_1,  t*=(ell_2 c_1+ell_1 c_2)/D.

If ell_i>=0, ||t*||<=1 and alpha_i ell_i>=w_i for each i, the physical
preparation t* attains (1). Indeed L_i=alpha_i ell_i, the errors are equal,
and the other norm branches are inactive: H_i=w_i||t*||||m_i||<=w_i=d_i,
while L_i>=d_i. Thus the complete formula reduces to (d_i+L_i)/4.
These are sufficient conditions, not an exhaustive classification of all
zero-visibility uncertainty sets. Zero means, D=0, reversed norm ordering,
negative ell or a preparation outside the Bloch ball require separate analysis.

K2410's rational means and loss weights satisfy these conditions with

    alpha=(365/520,259/520), q=(259/624,365/624),
    ||A||^2=75168976896/1787373245,
    ||B||^2=741956311296/223421655625.

Its exact outward rational square-root bounds prove ell_i>0, ||t*||^2<13/20
and alpha_i ell_i>w_i. The companion probe replays those original channel
CP/TP, composition, norm and feasibility checks, then tests the new conformal
projection and center identities symbolically. Hence E* is a global optimum,
not merely a numerical stationary point or a restricted-class optimum.

## 3. Follow-through: stability, physical continuum and implementation

Keeping the discarded terms in the same proof yields, for every averaged
physical controller,

    max_i E_i >= E* + [(1-g) h+k(1-r)||B||]/4,
    h=sum_i q_i(1-w_i)>0.                              (2)

Thus an epsilon-optimal averaged controller must obey
1-g<=4epsilon/h and 1-r<=4epsilon/(k||B||). Nonunitary attenuation cannot
improve the optimum. At the optimum max_i E_i=E*, the positive coefficients force g=r=1. In two dimensions G decomposes into
conformal and anticonformal parts; its singular values are r+s and |r-s|,
where s is the anticonformal radius. Since ||G||op<=1 and r=1, s=0.
Triangle equality fixes the rotation P*. Positive certificate weights force equal endpoint errors, and triangle equality places t on the center segment; the balanced centers then fix t*.
This proves uniqueness within the averaged coordinates. It does not assert
uniqueness of every unaveraged implementation or Kraus representation.

For any convex mixture of the TWO COMPLETE flagged instruments, the recovered
channel for one fixed controller is affine in that mixture. Diamond convexity
makes its worst error occur at an endpoint; endpoint inclusion supplies the
opposite bound. Thus the entire physical instrument convex hull has exactly
E*. Mixing the unweighted conditional means would define a different model.

K2410's rounded rational controller has a complete improvement over optimized
good-identity recovery with certified allowance eta<1/100000. It also supplies
an explicit near-optimal upper certificate: combining its original rational
squared-error values with E* gives an exact rational upper bound of 2×10^-9 on its gap.
This formal allowance still needs independently justified full-instrument
implementation error, calibration and costs. Nothing here supplies a device.

## Verification and postflight

New symbolic identities, rational inequalities and changed-channel controls
support the contraction proof. The reused K2410 finite fixtures are reported
separately from the new checks and from the universal analytic argument.
Independent read-only review challenged arbitrary nonunitary channels,
norm-branch direction and attainment; the short certificate survived.
The strongest remaining alternative is nonzero visibility with variable loss,
where the bad affine block adds more than preparation, or a physical
uncertainty family failing the displayed sufficient conditions. Their optimum
is open. No novelty, external-expert or proof-assistant certification is claimed.

Background: [Watrous, The Theory of Quantum Information](https://cs.uwaterloo.ca/~watrous/TQI/)
for channels and completely bounded trace norm; the fixture-specific certificate
and assumptions are given explicitly above.
