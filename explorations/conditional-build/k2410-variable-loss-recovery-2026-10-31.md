---
title: "K2410 Variable loss can make good-flag correction useful"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional channel mathematics; no measured calibration, hardware or native GU verdict
scripts:
  - tests/channel-swings/k2410_variable_loss_recovery_probe.py
---

# K2410 Variable loss can make good-flag correction useful

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
result: K2410
carrier: flagged positive-Hilbert qubit sign instrument with uncertain joint loss and planar clock law LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert channel pairing ON=declared_carrier
real_structure: real probabilities and rational or algebraic channel coefficients
grading: good/bad flags, binary survivor signs and conditional clock axes
action_owner: repository-construction -- K2398/K2407 sign instrument
target: joint fixed good/bad recovery under variable loss MAP-TYPE=evaluation
```

## Result and preflight

K2407 proves that good-flag identity is optimal when the bad-flag probability
is fixed across uncertainty. That premise is essential. Here two physical
visibility-zero laws with different loss weights have an exactly certified
all-CPTP optimum when the good flag is left unchanged. A single fixed good
unitary and bad preparation strictly improve on that optimum for both laws.
The improvement persists on their entire physical instrument convex hull.
A general exact norm formula gives the corresponding joint convex program
and finite certificates supported on at most twelve laws.

Preflight alternatives were another fixed-weight example, a nonplanar
extension, and removing the fixed-loss premise. The last changes a load-bearing
operational assumption and admits an exact falsifying control: copying the
fixed-weight factorization must fail. This is positive-Hilbert comparator
mathematics, not a construction of the GU physical quotient; SC-META-53,
LT-GR6b, source polarities and the physics ledger are unchanged.

## 1. Exact complete-channel norm and joint optimization

Use the common sign and real-channel averages of K2398/K2407. These preserve
all planar laws simultaneously and cannot increase their worst diamond
error. The effective good channel is unital with planar block G and
perpendicular contraction g; the bad decoder has planar translation t and
block A. For law u=(w,m,Q), put

    B=t m^T+A Q, T=(1-w)G+wB,
    C=I_2-T, d=1-(1-w)g,
    L=sqrt((tr C)^2+(C12-C21)^2),
    H=sqrt((C11-C22)^2+(C12+C21)^2).

The sign-pair symmetry conjugates the input and output by Y while exchanging
the two bad signs. It leaves every planar instrument invariant. Kraus
conjugation implements the real-channel average because each axis state is
real in the X,Z basis. Applied to the good decoder these two averages remove
its translation and its plane/perpendicular mixing; applied to the paired
bad decoders they leave the single real decoder form above. Every operation
is one fixed physical mixture used for all laws. The scalar w is untouched,
so variable weights do not break either covariance or the convexity argument.

Both G and the bad decoder obey their actual real Choi CP/TP constraints.
The complete output is unital with plane T and perpendicular contraction
(1-w)g. Contractivity implies ||T||op<=1, d>=0 and det C>=0. The last fact
follows because real eigenvalues of T are at most one and a conjugate pair
contributes a nonnegative squared modulus to det(I-T). Consequently L is
the sum of the two singular values of C, H their absolute difference.

The exact complete half-diamond error is

    E_u(G,g,t,A) = max{d+L, L+H, 2d}/4.                 (1)

Proof: proper planar singular-value rotations, extended with the fixed
perpendicular axis, transform the difference map into a Pauli-diagonal
trace-annihilating map with nonnegative contractions s1,s2,d. These independent
input/output unitaries preserve diamond norm; they are a proof device, not
law-dependent recovery. Its Pauli coefficients are
(s1+s2+d, s1-s2-d, -s1+s2-d, -s1-s2+d)/4. The triangle upper bound is attained
on a Bell input, hence the diamond norm is their absolute sum, which is
max{(s1+s2+d)/2, max(s1,s2,d)}. Substitute L=s1+s2 and H=|s1-s2| to obtain (1).
This proof covers singular boundaries. The commonly used expression
(d+L)/4 is exact only when H<=d<=L; dropping that condition is unsafe.

For a finite physical uncertainty set, minimize a scalar e subject to both
Choi constraints and, for each law, the three inequalities in (1). Each is
a second-order-cone inequality or a sum of norms representable using norm
epigraphs. The coefficients w,m,Q are fixed law data, not optimization
variables. Thus the joint problem is a convex conic program; solver status
alone is not a certificate.

For any nonempty compact physical law set, a global minimizer exists. The
projected good decoder has five real coordinates (four entries of G and g),
and the bad decoder six (two entries of t and four of A). The latter
feasible set is the compact convex projection of real Choi CPTP maps; its
unobserved perpendicular contraction remains an existential Choi variable.
Arbitrary t,A are not assumed to be completely positive. For a convex
continuous objective in this eleven-dimensional product set, the maximum
subgradient rule and convex optimality supply a convex combination of
active-law subgradients normal to the feasible set at the minimizer.
Caratheodory reduces this combination to at most twelve members. The same
weighted supporting affine functions lower-bound the objective globally and
attain the robust value at the minimizer. Thus at most twelve actual laws
already force the robust optimum. Repeated subgradients from one law can be
merged because its subdifferential is convex. Unlike K2407, differentiability
is not required. This is certificate existence, not a finite-sampling oracle
for an arbitrary compact set. Explicit Choi dual slacks can certify the
linear supporting minimization without relying on a numerical solver.

## 2. Exact all-CPTP optimum with good identity

Take Q1=Q2=0, and

    m1=(125/338,150/169), w1=73/100,
    m2=(49/250,-84/125), w2=37/52.

Their squared norms are 625/676 and 49/100. Each is physically realized by
a visibility-zero antipodal axis law: n_i=m_i/||m_i|| and masses
(1+||m_i||)/2 at n_i, (1-||m_i||)/2 at -n_i. Here ||m1||=25/26,
||m2||=7/10, so every axis and probability is rational. The good flag carries
the identity channel, with probability 1-w_i. The bad sign instrument is

    J_{i,z}(rho) = [tr rho+z m_i.r] I/4,  z=+1,-1.

Its sign traces depend on the input. These actual CP blocks, not merely
declared moments, define the fixture.

At visibility zero every bad decoder acts on I/2, so after the common
symmetry its complete effect is preparation t with ||t||<=1 followed by the
sign flip. This covers arbitrary initial CPTP sign decoders. With good
identity the exact error is

    E_i(t)=w_i[1+sqrt((2-t.m_i)^2+(t_x m_iz-t_z m_ix)^2)]/4.

Take t0=(4/5,0). The radii and unit support directions are

    r1=24/13, (a1,b1)=(12/13,5/13),
    r2=48/25, (a2,b2)=(24/25,-7/25).

Both errors equal E0=2701/5200. Each radius has gradient
(0,-2b_i/(4/5)) at t0. The positive weights

    p1=259/624, p2=365/624

sum to one and satisfy sum p_i w_i b_i=0. Weighted tangent supports therefore
sum to the constant E0 for every t. Since each support lower-bounds its
convex radius, max E_i(t)>=sum p_i E_i(t)>=E0 for every decoder. This is a
global all-CPTP certificate, not a stationary-point claim. Preparation t0
attains it.

## 3. A common good correction strictly improves

Let s=1/180, c=(1-s^2)/(1+s^2), h=2s/(1+s^2). Use the same good unitary for
both laws, with planar block G=[[c,h],[-h,c]] and g=1; it is implemented by
U=(I-i s Y)/sqrt(1+s^2). On the bad flag prepare

    t=(160093/200000,34157/10000000).

The preparation is CP because ||t||^2=64075588323149/100000000000000<1. For each original
instrument, apply the preparation to each sign block and the Y sign flip on
the negative block. Mix this recovered bad channel with the good unitary
using that law's physical probability w_i. One fixed controller is used;
it is not informed of which law occurred.

Here d_i=w_i. Define

    S_i=[2-2(1-w_i)c-w_i t.m_i]^2
        +[2(1-w_i)h+w_i(t_x m_iz-t_z m_ix)]^2.

Then L_i=sqrt(S_i). Also H_i=w_i||t||||m_i||<w_i, while exact rational
comparison gives S_i>w_i^2. Thus (1) reduces to
E_i=(w_i+sqrt(S_i))/4, with no unproved triangle assumption. The squared
gaps below are strictly positive:

    (4E0-w1)^2-S1 = 4388891640853658579/35044921600000000000000,
    (4E0-w2)^2-S2 = 111236783282109406331/876123040000000000000000.

Since 4E0-w_i>0, both complete errors are strictly less than E0. Illustrative
decimals are E1≈0.5194114609 and E2≈0.5194114597, against E0≈0.5194230769;
the strict proof is rational, not numerical. This is an attained improving
controller, not a claim that it is the unrestricted joint optimum.

The mechanism is visible at first order. Rotate G by angle theta and set
t_z=(8/25)theta, keeping t_x=4/5. Then

    dE_i/dtheta at 0 = (b_i/2)[(1-w_i)-(2/5)w_i].

The two derivatives are -11/2600 and -7/13000. Different loss weights make
both negative. The bad-only certificate cancels sum p_i w_i b_i, whereas
the good-rotation term depends on sum p_i(1-w_i)b_i. The second does not
vanish. At fixed w the first cancellation forces the second, exactly the
K2407 boundary; no fixed-weight result is being contradicted.

### Analytic synthesis rather than a saturated preparation ansatz

For a fixed good rotation angle theta, put n_i=||m_i||,
alpha_i=w_i n_i, and define the two planar centers

    c_i = 2/[w_i n_i^2] *
          ((1-(1-w_i)cos(theta))m_ix-(1-w_i)sin(theta)m_iz,
           (1-(1-w_i)cos(theta))m_iz+(1-w_i)sin(theta)m_ix).

Then L_i=alpha_i||t-c_i||. If D=||c1-c2||>0 and

    d1=(w2-w1+alpha2 D)/(alpha1+alpha2), d2=D-d1

are nonnegative, triangle inequality proves that the unrestricted planar
minimax value of max_i(w_i+L_i)/4 is

    [w1 alpha2+w2 alpha1+alpha1 alpha2 D]/[4(alpha1+alpha2)].

It is attained at t=(d2 c1+d1 c2)/D. If ||t||<=1 and L_i>=w_i at this point,
it also solves the actual fixed-good-unitary, bad-preparation problem:
H_i<=w_i, so the norm's other branches do not raise the value. If either
condition fails, the center construction is only a lower bound and cannot
be called a feasible optimum. The degenerate D=0 or negative-distance cases
require their endpoint analysis and are not needed here.

Writing A_i=2m_i/(w_i n_i^2), B_i=(1-w_i)A_i gives
c1-c2=A-R(-theta)B, with A=A1-A2 and B=B1-B2. When A,B are nonzero,
the smallest center distance over rotations is ||A|-|B||, achieved by
aligning R(-theta)B with A. For this fixture that alignment gives an exact restricted-class optimizer.
The squared lengths are

    |A|^2=75168976896/1787373245,
    |B|^2=741956311296/223421655625.

Set cos(theta)=(A.B)/(|A||B|) and
sin(theta)=(A_x B_z-A_z B_x)/(|A||B|), and use the displayed center formula
for t. Exact rational square-root enclosures in the probe show d1,d2>0,
||t||^2<13/20 and alpha_i d_i>w_i for both laws. Thus the optimizer is a
physical preparation and lies in the exact diamond branch used above.
Its complete value is strictly between 0.5194114591 and 0.5194114592.

The global lower bound over this restricted good-rotation class follows
without assuming positive d1,d2 at other angles: average the two errors
with weights alpha2/(alpha1+alpha2), alpha1/(alpha1+alpha2), apply triangle
inequality, then use D>=||A|-|B||. The displayed feasible alignment attains
this bound. Hence this is the exact optimum over all good rotations about
the perpendicular Y axis and arbitrary bad decoders; the common symmetries
preserve these good rotations and reduce the visibility-zero bad recovery
to preparation. Allowing general good CPTP channels remains a larger game.

Rounding this algebraic optimizer gives the rational controller above, whose
actual original-channel certificate does not depend on the rounding search.
Its preparation lies well inside the Bloch ball; saturating its norm would
be an additional restriction. No unrestricted joint optimum is inferred.

## 4. Physical continuum and priced margin

The result extends to every mixture of the two complete flagged instruments.
For lambda in[0,1], the correct conditional parameters are

    w_lambda=lambda w1+(1-lambda)w2,
    m_lambda=[lambda w1 m1+(1-lambda)w2 m2]/w_lambda,
    Q_lambda=0.

This is a convex family in the lifted coordinates (w,wm,wQ), not generally
in (w,m,Q). For any fixed good/bad controller, recovered complete channels
are affine in the instrument mixture, so diamond convexity bounds every
interior error by the endpoint maximum. Since both endpoints belong to the
family, the good-identity robust optimum remains exactly E0 and the common
improving controller remains strictly better on the entire family.

Let g_i denote the exact positive squared gaps above and v_i=4E0-w_i.
The actual endpoint gain is g_i/[4(v_i+sqrt(S_i))]>g_i/(8v_i). Thus

    eta_safe = min_i g_i/(8v_i)>1/100000

is a rational certified complete-channel implementation margin against the
ideal optimized good-identity baseline. An independently justified complete
half-diamond implementation error eta<eta_safe preserves strict improvement.
In particular the simpler complete allowance eta<1/100000 is certified.
Comparing two actual devices requires both implementation budgets. No device
rates, calibration records, synthesis expense or empirical loss law are
supplied; the tiny formal gain can be eliminated by real implementation cost.

## Verification and postflight

The companion probe reconstructs each physical antipodal law, tests actual
sign-instrument and recovery Choi CP/TP, composes the original sign channels,
checks the global support certificate and both exact strict gaps, and checks
Bell-block characteristic polynomials against the norm formula. Changed-input
controls target an omitted skew, wrong weighting, an invalid prepared state
and a reversed good rotation. The universal norm, compact-set certificate
and continuum claims rest on the written proofs and independent internal
review, not a count of finite assertions.

Postflight: the strongest overclaim would be that the exhibited controller
is jointly optimal, that a variable-loss conditional mixture is affine in
unweighted m, or that a positive mathematical margin supplies hardware
recovery. None follows. The useful next construction is an exact primal/dual
certificate for the full joint optimum of this fixture or a supplied
calibration region in lifted instrument coordinates, with complete device
cost. No external-expert, proof-assistant, empirical or native GU certification
is claimed.
