---
title: "K2559 Decreasing flow generator, global stopping support and exact budget segment"
status: active_research
doc_type: exploration
created: "2026-11-05"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: original-law support for all lambda at least 4/sqrt(3) and exact constrained frontier through the critical contact; higher-budget frontier open
scripts:
  - tests/channel-swings/k2559_parametric_stopping_concavity_probe.py
---

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
result: K2559
carrier: original fresh fair test/use histories with predictable randomized actions and finite expected original cost LAYER=toy CHIRALITY=N/A
pairing: unconditional expectations over success, rejection, abort and nonabsorption ON=declared_carrier
real_structure: real probabilities and logarithmic costs; exact algebraic sign field Q(sqrt3)
grading: input and output value parameters, one-stage and residual optimizers, actual and clipped trials remain distinct
action_owner: repository-construction -- supplied stopping probability law
target: global multiplier support, all-policy optimizer rigidity and exact low-budget value MAP-TYPE=evaluation
```

# K2559 Turn the one-stage cost map into a decreasing flow

## Result and scope

For every score 0<S<=1/2 and every finite lambda>=lambda*=4/sqrt(3), the
one-stage policy is globally optimal for p-lambda C over the original
predictable randomized adaptive class. This closes the previously open
multiplier interval and continues above it. It yields the exact constrained
value for every budget from zero through the critical contact, including
strict concavity, marginal cost, and exact reached-action classification.

The proof does NOT establish the initially explored concavity of the residual
in theta=1/lambda. Instead a two-variable certificate proves that the
one-stage cost map has a generator decreasing with score. Scalar ODE
comparison gives the required composition inequality without parameter root
ribbons. The artifact filename preserves the candidate topic; the proved
claim is the generator inequality below. K2557's failed ribbon controls
remain correct and are not overwritten.

This is independent mathematics of a supplied law. No physical experiment,
native GU probability, novelty or external certification is inferred.
SC-META-53 remains UNCERTAIN; ledger0.263 LT-SM8 retains its action, physical
quotient and domain obligations. The higher-budget frontier and maximal
fixed-score one-stage range remain open.

## 1. Original one-stage map and the output-root distinction

For 0<=a<=s<=1/2 write

    w(a,s)=log(1+(s-a)²/[2(a+s)(2-a-s)]), A=1+a,
    k=-w_a, M=2A k+2w,
    F_s(u)=min_(0<=a<=s) [(1+a)u+2w(a,s)], F_0(u)=u.

The value at a=s has w=0. For s>0 and the positive sublevel considered
below, strict w_aa>0 gives a unique interior minimizer, characterized by
2k=u. Its output is v=F_s(u)=M(a,s), not u. Also

    F_u=1+a>0, F_s=2w_s>=0, F_s(0)=0, F_s(u)>=u,
    M_a=-2(1+a)w_aa<0.                               (1)

Hence F_s is strictly increasing onto the nonnegative half-line and its
inverse at v is defined. In the region 0<v<=theta*=sqrt(3)/4, the output
root M=v lies at or ABOVE the critical one-stage optimizer a_*(s). The
critical root is the one from K2553, not the residual optimizer.

K2553's exact root certificate supplies

    a_*(s)/s >= l(s)=2sqrt(3)-3+(4sqrt(3)-13/2)s+9s²/100.

At a=0 the output is larger than theta*, and at a=s it is zero, so these
roots are interior. These facts also follow from the unchanged critical
root/convexity proof and monotonicity M_a. Thus every root needed here lies
in l(s)<=r=a/s<1, uniformly for all 0<v<=theta*. The old residual ribbon
which failed at lambda=8/3 is never used.

## 2. One new whole-domain generator certificate

Define the nonautonomous generator at OUTPUT value v by

    G_s(v)=partial_s F_s(F_s^-1(v))=2w_s(a(v,s),s).

Implicit differentiation of M(a,s)=v at fixed v gives

    a_s=(w_s-(1+a)w_as)/[(1+a)w_aa],
    partial_s G_s(v)=2K(a,s),
    K=w_ss-w_as²/w_aa+w_s w_as/[(1+a)w_aa].           (2)

K is rational, despite the logarithm in M. The new exact certificate proves

    K(rs,s)<=0 for 0<=s<=1/2, l(s)<=r<=1,
    K(rs,s)<0 for 0<s<=1/2, l(s)<=r<1.               (3)

In the probe, substitute s=Y/2 and r=l(Y/2)+(1-l(Y/2))X. The numerator
of -K has tensor degree(9,22), with230 nonnegative Bernstein coefficients;
the denominator has degree(10,26), with297 strictly positive coefficients.
Every coefficient is in Q(sqrt3), with exact sign decisions. Independent
finite-difference conversion reconstructs each polynomial from its
Bernstein coefficients. This is a whole-rectangle sign proof, not a grid.
Strictness is checked after factoring the genuine boundary zero1-r;
the resulting numerator is nonnegative in Bernstein form and strictly
positive on the needed interior and upper-score edge. Exact zero positions
and endpoint checks are recorded in the report.

At s=0 the canceled expression has the smooth extension

    r(v,0)=2/sqrt(1+2v)-1,
    G_0(v)=2sqrt(1+2v)-2-v.                           (4)

This follows by the implicit root expansion in a=rs; its r derivative is
nonzero on the compact critical root interval. Thus G is locally Lipschitz
in v for v>0 and continuous in s at0. At v=0, F_s(0)=0. In particular,
for b>0 and 0<v<=theta*, G_x(v)>G_(b+x)(v) whenever b+x<=1/2.
The isolated equality at s=0,v=theta* does not spoil the strict integrated
inequality over a positive score interval.

## 3. Flow comparison gives every multiplier at once

Fix theta=1/lambda in(0,theta*], S=b+t<=1/2, and put
u=F_S^-1(theta). For x in[0,t] compare

    z(x)=F_(b+x)(u), y(x)=F_x(F_b(u)).

They start at the same positive value F_b(u). By the definition of G,

    z'=G_(b+x)(z), y'=G_x(y).

The z path stays at most theta. While y<=theta, equation(3), local
Lipschitz continuity and scalar ODE comparison give y>=z. If y crosses
theta, it cannot return below it because F_x is nondecreasing in x.
Consequently

    F_t(F_b(u))>=F_S(u)=theta.                        (5)

For b,t>0 strict generator comparison gives strict inequality unless y has
already crossed theta, in which case it is also strict at the endpoint
(the positive-output generator is positive). Inverting the increasing F_t,

    F_b(F_S^-1(theta))>=F_t^-1(theta),                (6)

strictly when0<b<S. This orientation matters: neither commutativity of
F_b,F_t nor residual concavity in theta is asserted.

Set

    U_lambda(s)=lambda F_s^-1(1/lambda)
               =max_a [1-2lambda w(a,s)]/(1+a).

The equality follows by rearranging F_s(u)=theta. Multiplying(6) by lambda
is the exact Bellman inequality

    (1+a)U_lambda(s)+2lambda w(a,b)-U_lambda(s-b)>=0  (7)

for0<=a<=b<=s, with strict residual minimum for0<b<s. At b=s the unique
zero is the one-stage optimizer a_lambda(s); at b=0 only a=0 has zero.
Also 2/3<=1/(1+s)<=U_lambda(s)<=1. These bounds follow from the free
choice a=s and nonnegative cost, and control terminal potentials.

## 4. Full adaptive transfer and exact equality

Use the original fair test/use law of K2483 and K2557. At a reached trial
clip b'=min(b,s), a'=min(a,b'). The original expected slack is

    delta=[(1+a')U(s)+2lambda w(a',b')-U(s-b')]/2
            +U(s)(a-a')/2+lambda[w(a,b)-w(a',b')].    (8)

All terms are nonnegative by(7), positive U and the original cost's clipping
monotonicity. K2557's finite-horizon conditional-expectation telescope and
monotone/bounded convergence therefore apply unchanged to every predictable,
randomized adaptive policy with finite expected cost:

    U(S)-p+lambda C
      =E sum_active delta
        +E[1_nonabsorption U(s_infinity)]
        +E[1_abort U(s_abort)] >=0.                  (9)

A limit of scores approaching zero without a finite hit is nonabsorption
and retains U(0)=1. Failure has potential0, hit1. Infinite expected cost
cannot improve p-lambda C at positive lambda. No fixed-schedule mixture
representation is assumed.

Strictness in(7), the unique one-stage minimizer, and clipping monotonicity
show that equality in(9) is equivalent, up to null reached events, to:
no abort or nonabsorption, and each reached action either(a,b)=(0,0) or
(a,b)=(a_lambda(S),S). Thus arbitrary predictable free idles may separate
the fixed full-score actions, provided absorption is almost sure. Waiting
time can have infinite expectation. Expected nonidle count is2/(1+a),
success p=1/(1+a), and cost C=2w(a,S)/(1+a).

This transfers qualitative rigidity to every finite lambda>=lambda*.
It does not transfer K2557's numerical near-optimality constants to new
multipliers; such uniform quantitative estimates require a separate bound.
K2517's smaller-multiplier counterexamples show lambda* is sharp for this
uniform score-class support statement within its stated lambda>1 range,
not necessarily the fixed-S threshold.

## 5. Execute the constrained-budget consumer

For fixed S let a_*=a_lambda*(S) and

    C_*=2w(a_*,S)/(1+a_*).

For a in[a_*,S), define C(a)=2w(a,S)/(1+a). Exact differentiation gives

    C'(a)=-M(a,S)/(1+a)²<0,
    p'(a)=-1/(1+a)².

Thus every budget B in(0,C_*] has a unique a_B in[a_*,S) with C(a_B)=B,
and lambda_B=1/M(a_B,S)>=lambda*. The global support bound gives, for
EVERY policy with C<=B,

    p<=U_lambdaB(S)+lambda_B B=1/(1+a_B).

Repeated full-score action(a_B,S) attains the bound. This is the exact
adaptive constrained frontier on this entire interval, not an interpolation
between contacts or a componentwise mixture budget. Equality forces C=B
and the reached-action classification of section4. On the open interval,

    dp/dB=1/M=lambda_B,
    d²p/dB²=-2(1+a_B)^3 w_aa/M^3<0.                 (10)

The segment is strictly concave and its marginal cost is exact. Budgets
above C_* and the maximal one-stage interval at this fixed S remain open.

The zero-budget endpoint also has a direct equality proof. If C=0, every
reached action has w=0, so a>=b. Put U_infinity(s)=1/(1+s), b'=min(b,s),
t=s-b'. Then its original per-trial slack is exactly

    [(1+a)U_infinity(s)-U_infinity(t)]/2
      =b't/[2(1+s)(1+t)]+(a-b')/[2(1+s)]>=0.         (11)

The same tail argument gives p<=1/(1+S). Full-stage(a,b)=(S,S) attains
this for zero cost. Equality in(11) and the terminal terms permits only
free idles or(S,S), with almost-sure absorption. This proves endpoint
rigidity directly; it is not inferred from a limit of positive-budget
optimizers.

## 6. Released small-budget law and marginal sensitivity

The certified segment makes a small-budget expansion an expansion of the
TRUE adaptive value, not merely a feasible one-stage witness. Fix S>0,
h=1+S and delta=S-a. The original denominator is exactly

    D=8S(1-S)+4(2S-1)delta-2delta²,
    C= c2 delta²+c3 delta³+O(delta^4),
    c2=1/[4hS(1-S)],
    c3=c2[1/h-(2S-1)/(2S(1-S))].

Since C/delta² is analytic and positive at zero, t=sqrt(B) equals
delta sqrt(C/delta²) and has an analytic inverse with nonzero derivative.
Thus, on the nonnegative branch,

    delta=2sqrt[hS(1-S)]sqrt(B)+(4S²-S-1)B+O(B^(3/2)),
    p(B)=1/h+2sqrt[S(1-S)/h³]sqrt(B)
                    +(3S-1)B/h²+O(B^(3/2)),          (12)
    lambda(B)=sqrt[S(1-S)/h³]/sqrt(B)
                    +(3S-1)/h²+O(sqrt(B)).           (13)

Analytic inversion justifies differentiation of the remainder in(13).
The bounds are uniform on compact score intervals inside(0,1/2], where
all denominators, inverse derivatives and the certified contact budget
stay bounded away from zero. They are not uniform as S approaches zero.
This prices the exact square-root improvement above the free-success value
and the diverging marginal value of the first small positive budget.
No physical implementation cost is supplied by this mathematical budget.

## Verification and next frontier

The new probe derives the generator from original logarithmic derivatives,
certifies its whole root region with exact Bernstein coefficients and
independent basis reconstruction, checks strictness, zero-score extension,
original-law fixtures and constrained derivatives. Contrary controls reject
extension below the critical root, missing expected-cost prefixes and
input/output-root substitution. Universal ODE comparison and adaptive
expectation arguments are independently reviewed; finite checks are not
substitutes for those arguments.

The useful next independent question is the higher-budget, fixed-score
frontier where the one-stage theorem no longer decides the answer, or
parameter-uniform quantitative stability near this certified segment.
Physical controller/time costs would define a different problem. Native
source, quotient and observation debts remain unchanged.

[Critical certificate](k2553-global-stopping-certificate-2026-11-04.md),
[adaptive accounting](k2557-parametric-stopping-support-2026-11-05.md),
[one-stage roots](k2509-stopping-atom-certificate-2026-11-02.md),
[lower-multiplier obstruction](k2517-small-score-stopping-transition-2026-11-02.md),
[probe](../../tests/channel-swings/k2559_parametric_stopping_concavity_probe.py).
