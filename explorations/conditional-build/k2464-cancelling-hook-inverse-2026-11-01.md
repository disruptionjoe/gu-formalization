---
title: "K2464 Ordinary cancellation enlarges the exact analytic scalar image"
status: active_research
doc_type: exploration
created: "2026-11-01"
classification: CONVENTIONAL_COMPARATOR
target_claim: "INTERNAL_TARGET: the original rank-two scalar image remains maximal after adding the K2452 rank-three hook"
claim_ceiling: "conditional enlarged repeated-hook linear image and analytic inverse; not full mixed or nonlinear convergence"
---

# K2464 Ordinary cancellation enlarges the exact analytic scalar image

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
result: K2464
carrier: original fourteen-dimensional split hook carrier and original polar background LAYER=toy CHIRALITY=N/A
pairing: original nondegenerate split-metric hook and ordinary-scalar coefficient pairing ON=declared_carrier
real_structure: original real geometry with exact coefficients in Q(sqrt2)
grading: tensor slots and homogeneous polynomial degree
action_owner: repository-construction -- supplied conditional mathematical models
target: Ordinary cancellation enlarges the exact analytic scalar image MAP-TYPE=evaluation
```

## Result and object boundary

K2461 exhausted the twelve-dimensional span of its sixteen rank-two lines.
Adding the actual K2452 rank-three hook strictly enlarges the image, even
though its individual ordinary-null family was restricted. A scalar-dark
compensator cancels its ordinary response. The resulting inverse covers all
functions of the twelve ambient coordinates other than x11,x13. Together
with the old image it gives an exact classification for the enlarged
thirteen-dimensional constant hook span, and a controlled analytic inverse.
It does not establish the unrestricted mixed inverse or nonlinear closure.

SC-ACT-01/06 and SC-GEO-55 ASSERTS retain their source scopes; SC-META-53
remains UNCERTAIN. This is the original supplied conditional hook model,
not a native physical GU solution. Ledger0.263 and canon are unchanged.

## 1. Original cancellation, including the scalar second-order terms

Set c=9012/8519 and A=2253/17038. Let h be K2452's original hook, with
h_11,11,2=-1,h_13,13,2=1,h_11,11,4=-c,h_13,13,4=c and antisymmetric
last slots. Define U_11,11,12=1,U_13,13,12=-1 with antisymmetric last
slots. Both are tracefree, cyclic and satisfy every original polar condition.
Use ambient coordinates, not the adapted y/z indices. The original boundary
ideal contains x5=y2.

For f independent of x11,x13, write

    H=-partial_2 f+c partial_4 f,
    F=integral_0^x12 H(...,s,...) ds,
    V=h f-U F.                                         (1)

The ordinary response of h f is diag_(11,13)(2H,-2H).
The response of U F is the same because F_12=H; all its other responses
contain derivatives11 or13. Thus D V=0 exactly. If f is divisible by x5,
so is F, and V lies in the original boundary ideal.

This cancellation also removes the complete scalar second-order part.
For p=11,r=13, define T(v)_ppj=-v_j,T(v)_rrj=v_j with antisymmetric
last slots and j outside{p,r}. For external i,j the actual polarization is

    fp(K,T(v),i,j)=(2/3)(v_i DeltaK_j+v_j DeltaK_i),
    DeltaK_j=K_rrj-K_ppj.

Therefore its scalar second-order contribution is

    -(2/3) sum_j eta_j DeltaK_j(x) partial_j
                         [sum_i eta_i partial_i v_i].  (2)

K(x) multiplies AFTER differentiation; moving it inside changes the operator.
In (1), v2=f,v4=c f,v12=F; weighted divergence is H-F_12=0.
The probe checks this coefficient identity for every original background K
and every external tensor slot. The displayed identity proves all-degree
cancellation; finitely many polynomial tests are not its substitute.

Original first-order reconstruction gives a(h)=A(partial4+partial5)
and a(U)=0 on the entire fourteen-coordinate bank. Consequently

    Jstar(V)=A(partial4+partial5)f.                     (3)

## 2. Explicit analytic inverse and the missing cubic

For arbitrary g independent x11,x13, with t=x5,u=x4, take

    f=(1/A) integral_0^t g(...,u-t+s,s,...) ds.          (4)

Then (partial_u+partial_t)f=g/A, and f has a factor t. Formula (1)
therefore solves D V=0,Jstar V=g with the original boundary ideal.
It allows independent x2,x4,x12; the earlier individual h family did not.
For g=x2^3 the exact formula is

    f=x5*x2^3/A, F=-3*x12*x5*x2^2/A.

The x2^2*x0 target has F=-2*x12*x5*x2*x0/A. These violate the old
rank-two PDE image and now have literal original lifts. Neither an ordinary
projection nor a refitted background was used.

For homogeneous g of degree n=d-1, d>=4, the actual jet lift is(d/4)V,
retaining K2437's original4/d normalization. Coefficient l1 estimates give

    ||f||1 <= 2^n ||g||1/A,
    ||F||1 <= (1+c)d ||f||1,
    ||(d/4)V||1 <= d(d+1)(1+c)2^(d-1)||g||1/A.         (5)

Here ||h||1=4(1+c),||U||1=4. Characteristic substitution supplies2^n;
one derivative costs at most d and integration at most one. A geometric
factor times a polynomial in d is absorbed by strict radius reduction.
Thus the construction is analytic on a smaller polydisc. This is a
restricted linear inverse with separately compatible lower jets; it does
not prove convergence of the complete nonlinear same-section recursion.

## 3. Released exact image of the enlarged constant span

Let C0 be the old twelve-dimensional span, and C=C0+R h. Put

    W=R[x_i:i not in{11,13}],
    V0=ker L3 intersect ker L10,
    L3=partial2^2-partial3^2, L10=partial2^2-partial10^2.

The exact scalar image of C-valued polynomial fields with D=0 and the
original boundary ideal is W+V0. For necessity, write a field h f+Z,
Z valued in C0. The off-block ordinary entries(2,11),(4,11),(2,13),(4,13)
come only from h f and force f_11=f_13=0. Subtract the particular field
(1). The remainder is C0-valued and ordinary-null, whose scalar image is
V0 by K2461's complete cancellation theorem, even without boundary
restrictions. The particular field's scalar lies in W. Conversely (1)-(4)
attain W and K2461's boundary-preserving primitives attain V0.

Equivalently the enlarged image is the four-PDE kernel

    partial11 L3 g=partial13 L3 g=0,
    partial11 L10 g=partial13 L10 g=0.                 (6)

Indeed split g0=g|x11=x13=0 and g1=g-g0. Conditions(6) say L3g,L10g
are independent11,13, so g1 lies in V0, while g0 lies in W. This gives
an explicit linear splitting. The two pieces have disjoint monomial
support and their coefficient norms add to ||g||1.

The full enlarged analytic inverse retains the old48 d 3^(d-1) bound:
combine K2461's V0 inverse with(5). Since(1+c)/A=35062/2253 and d>=4,
(d+1)(35062/2253)(2/3)^(d-1)<=48 (largest at d4, then decreases).
The norm of the sum is therefore at most48 d 3^(d-1)||g||1.
No nonlinear closure is claimed: x11 and x2^2 belong to W+V0 but their
product x11*x2^2 does not, since partial11 L3 of it equals2. This cubic
already lies in the actual d4 range. Another hook/generator beyond C,
or a full mixed construction, is needed to lift it. Merely repeating this
compensator or allowing arbitrary cancellation within C cannot suffice.

Universal arguments are the divergence factorization, exact-image splitting
and characteristic integral. Original coefficient checks, contrary laws and
finite polynomial tests are separate evidence. Internal independent review
is not external-expert, proof-assistant or novelty certification.

[Probe](../../tests/channel-swings/k2464_cancelling_hook_inverse_probe.py) and [report](../../lab/process/k2464-cancelling-hook-inverse.json).
