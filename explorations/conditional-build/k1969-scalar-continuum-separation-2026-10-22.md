---
title: "K1969: Exact continuum halfcut optimum and the missing all-cut bridge"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: independent conditional scalar mathematics; no full cut optimum, GU identification, novelty or external certification
scripts:
  - tests/channel-swings/k1969_scalar_continuum_separation.py
  - tests/channel-swings/k1969_scalar_continuum_separation_probe.py
---

# K1969: Exact continuum halfcut optimum and the missing all-cut bridge

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: exact continuum halfcut relaxation, within-model insufficiency counterexample and all-cut path reduction
carrier: fixed scalar two-characteristic tube with plateaux and zero area LAYER=toy CHIRALITY=N/A
pairing: Lebesgue cut marginals and Dirichlet phase energy ON=three_free_intervals
real_structure: real signed controls and real phases
grading: characteristic directions only; no physical chirality
action_owner: repository-construction -- fixed scalar control
target: separate solved halfcut variation from full measurable-cut feasibility MAP-TYPE=intertwiner
```

## 1. The continuum halfcut question is solved exactly

Keep [K1942](k1942-complete-scalar-energy-duality-2026-10-22.md)'s exact
problem: I=[-3,3], characteristic width9, c=1, M=23/100, phase+1 on[-2,-1],
phase-1 on[1,2], zero endpoint traces and zero area. Replace the full cut
family temporarily by ALL halfcuts A_x=[-3,x], with both signs. This is a
relaxation, not an assertion of pulse feasibility.

Let t be the unique root in(9/20,23/50) of

    P(t)=101t^4-102t^3-168t^2+392t-138=0.

Define

    K(t)=1/6-t^2/2+2t^3/3-t^4/4,
    D(t)=-7/100+69t/200-77t^2/200,
    lambda=D(t)/K(t).

The UNIQUE minimum phase energy under every halfcut constraint is exactly

    J_half=4+2 D(t)^2/K(t).                              (1)

Numerically t is about0.453596026309, lambda about0.063045360627 and
J_half about4.000917578239. These decimals are illustrations; the polynomial,
isolating rational interval and exact formulas define the result. This
exceeds K1942's rational lower bound. Its principal consequence is closure
of the continuous halfcut optimization, not the small decimal improvement.
It remains a lower bound on the FULL physical scalar optimum. Whether this
particular optimal phase passes every non-halfcut remains open.

## 2. Explicit phase, contact and global halfcut proof

Let phi0 be the affine baseline of energy4. Define an odd function g, zero
on the plateaux, by its values for x>=0:

    0<=x<=t:  g(x)=-(1-t)^2 x/2,
    t<=x<=1:  g(x)=(x-1)(x-t^2)/2,
    2<=x<=3:  g(x)=-(x-2)(3-x)/2.

The candidate is phi=phi0-lambda*g. This g is the SUM of the projected
Dirichlet representers of A_-t and A_t, not one representer; its squared
gradient norm is2K(t). It has zero area and vanishes on the plateaux and
outer endpoints. Direct integration gives int_(A_+/-t) g=K(t), so
D-lambda*K=0 proves both contacts.

For x>=0 set Q(x)=int_(A_x)phi-(M/2)C(A_x), where the exact long-tube
capacity is C(A_x)=(3-x)(6+x). Oddness gives Q(-x)=Q(x), and the halfcut
integrals are nonnegative because phi<=0 for x>=0. Thus the positive signed
constraint is the only one needing inspection.

The contact derivative Q'(t)=0 is exactly the polynomial equation:

    12[(154t-69)K-100D*t*(1-t)^2]=P(t).

On[0,t], put b=1-lambda*(1-t)^2/2. Then
Q'(x)=(b-M)(t-x)>=0. On[t,1],

    Q''(x)=-(1-M)-lambda*(x-(1+t^2)/2)<0.

On[1,2], Q'(x)=-1+(M/2)(3+2x)<=-39/200<0. On[2,3],

    Q''(x)=1+M+lambda*(5-2x)/2>0.

The exact bounds t in(0.45,0.46) and lambda in(0.06,0.07) make these
signs strict where stated. Consequently Q increases to Q(t)=0, then decreases
through x=2; on[2,3] it is convex with Q(2)<0 and Q(3)=0, so Q<=0 there as
well. This proves EVERY continuum halfcut. The formula gives phi<=0 on
the positive half: b>0; on[t,1], phi=-x+lambda*(1-x)*(x-t^2)/2<0;
and on[2,3], phi=-(3-x)[1-lambda*(x-2)/2]<=0.

Both positive contact multipliers equal lambda. Since
phi-phi0=-lambda*(g_-t+g_t), the Hilbert projection/KKT argument from K1942
proves minimality among all halfcut-feasible phases. Strict convexity gives
uniqueness. Algebraic endpoints are legitimate continuum halfcuts.

For uniqueness of the root, P' has Bernstein coefficients392,280,66,154
on[0,1], all positive. Exact evaluations give opposite signs at9/20 and23/50.
Rational bisection and interval arithmetic certify the root and result.

## 3. Every halfcut can pass while an actual physical cut fails

This is a counterexample inside the SAME trace, plateau and zero-area class.
On[5/2,11/4], add a positive triangle of height2 and width1/8, followed by a
negative triangle of height2 and width1/8. Extend the ripple oddly to the
negative side and set it to0 elsewhere. Each triangle has unsigned area1/8,
so each side has zero integral and every partial integral has absolute value
at most1/8. The perturbed phase remains H1 and preserves all fixed data.

On this positive support the original phase satisfies phi>=phi0=x-3, hence
its halfcut integral is no larger than the affine baseline's. Writing
s=3-x in[1/4,1/2], its halfcut slack is at least

    (M/2)s(9-s)-s^2/2 >=141/640 >1/8.

The primitive ripple cannot consume that margin. Outside these two supports
halfcut integrals do not change. Both signed inequalities remain valid:
the unperturbed integral is nonnegative, so its slack to the negative bound
is larger. Thus EVERY halfcut still passes after the perturbation.

But on A=[163/64,165/64], the ripple is at least3/2 and the original phase
is at least-29/64. Hence the perturbed phase is at least67/64 throughout A.
For any cut, C(A)<=9|A| by Fubini. Since |A|=1/32,

    int_A phi_perturbed-(M/2)C(A)
       >=67/2048-207/6400=19/51200>0.                  (2)

This is a non-halfcut physical violation without floating sampling. It
rejects a general sufficiency transfer from all halfcuts under the actual
fixed data. It does NOT prove the unperturbed optimum fails all-cut testing.

The earlier finite candidate at t=7/16 separately violates the halfcut
at -227/500 by14581117749/144545312500000. This agrees with K1965's explicit
finite-versus-continuum limit; its repaired upper remains valid.

## 4. Exact all-cut path reduction and a certificate interface

For any measurable A use its complement if needed so s=|A|<=3. On0<=x<=6 put

    F(x)=|A intersect[-3,x-3]|,
    W(x)=2F(x)-x, t_s=2s-6.

Then W(0)=0, W(6)=t_s and W'=+1 or-1 almost everywhere. The two moving
window sections have signed occupancies W(x) and t_s-W(x); the central
rectangle has signed occupancy t_s for length3. Since integral ell=54 and
|W|+|t_s-W|=|t_s|+2 dist(W,[t_s,0]), the exact capacity is

    C(A)=9s-int_0^6 dist(W(x),[t_s,0]) dx.              (3)

For every zero-area H1 phase with zero endpoint traces, integration by parts
gives

    2[int_A phi-(M/2)C(A)]
      =int_0^6 [M dist(W,[t_s,0])-phi'(x-3)W] dx-9Ms.  (4)

Thus all measurable cuts become a one-dimensional bounded-slope path
problem. Every such bang-bang path corresponds to an indicator almost
everywhere. There is no assertion that halfcuts exhaust its maximizers, or
that relaxing the slope constraint preserves its maximum.

For each s, a C1 function B_s(x,w) satisfying

    B_x+|B_w|+M dist(w,[t_s,0])-phi'(x-3)w <=0,
    B_s(6,t_s)>=0, B_s(0,0)<=9Ms,

almost everywhere in x and on the reachable strip proves the positive
inequality in(4) for all cuts by the chain rule. Apply it to -phi for the
other sign; for the odd candidate reflection exchanges signs. This is an
explicit sufficient certificate interface, NOT an asserted construction of
B_s. The missing all-cut certificate is the next substantive question.

## 5. Verification and ceiling

The producer uses exact rational root isolation and interval enclosures,
polynomial contact identities, analytic sign bounds, exact ripple geometry,
the finite candidate's violated halfcut, and direct capacity/path identity
controls. The independent probe reconstructs the sum representer from its
piecewise ODE, integrates contact and energy, and rejects changed mathematical
inputs after its green baseline. Source/report hashes are checked separately.
Infinite halfcut coverage follows section2's analytic proof; actual all-cut
insufficiency follows(2). Samples are controls, not the universal proof.

K1942 full-cut no-gap duality, K1963 finite separation and K1965 regularity/
repair are reused. None asserted section1's optimum or section3's counterexample.
No new external prior-art or novelty claim is made. Internal derivation and
controls are not external specialist acceptance or formal certification.
SC-OP-04 ASSERTS candidate grammar and SC-MAS-01 ASSERTS a stylized local mass
toy; neither supplies this scalar control. SC-META-53 remains UNCERTAIN.
LT-SM8/LT-GR6b/AC-F1, source, physics-ledger and canon verdicts stay unchanged.
