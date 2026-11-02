---
title: "K2515 Curved ratio domains advance the original stopping frontier"
status: active_research
doc_type: exploration
created: "2026-11-02"
classification: CONVENTIONAL_COMPARATOR
target_claim: "NONE-NOT-A-KILL"
claim_ceiling: "conditional supplied-model probability mathematics; no native GU realization or unrestricted-budget transition"
---

# K2515 Curved ratio domains advance the original stopping frontier

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
result: K2515
carrier: original fresh fair test/use stopping law at 0<S<=1/2 LAYER=toy CHIRALITY=N/A
pairing: original failure-inclusive probability cost ON=declared_carrier
real_structure: real probabilities and real logarithmic cost
grading: ordered finite stopping stages
action_owner: repository-construction -- supplied original probability law
target: all-policy Bellman certificate and exact constrained frontier MAP-TYPE=evaluation
```

## Result and scope

One stage is globally optimal for every original-law score 0<S<=1/2 and multiplier

    lambda >=8/3.

For S=1/2 this proves the exact all-policy constrained frontier at every budget
0<=K<=1/90, extending K2513's guaranteed interval through 1/200 by a factor 20/9.
The improvement is structural: curved ratio domains and a hazard-normalized
Schur complement avoid separate constant bounds for the value and its
derivatives. A uniform residual curvature gap 1/40 quantitatively excludes
finite multistage competitors.

Sections1–6 retain the first complete construction, lambda>=8001/2816 and
K<=1/100 on the curve c(b)=(1+b)/2. Section7 then releases a stronger curve,
c(b)=1/2+9b/20, proving lambda>=8/3 and K<=1/90 with the same curvature gap.
The first curve's failure at8/3 is preserved and bypassed, not overwritten.
Both thresholds are sufficient; neither is the true stopping transition. These are
GU-independent supplied-model probability results. SC-META-53 remains
UNCERTAIN; source polarities, ledger0.263, LT-SM8/LT-GR6b, canon, physical credit
and native matter/light/domain obligations are unchanged. No novelty,
experimental, external-expert or proof-assistant certification is claimed.

## 1. Original law and the two distinct optimizers

For 0<=a<=b<=s<=1/2 define

    w(a,b)=log(1+(b-a)^2/[2(a+b)(2-a-b)]), w(0,0)=0,
    U_lambda(s)=max_(0<=a<=s) [1-2lambda w(a,s)]/(1+a).

For a finite completed schedule with total score S, let
P_i=product_(j<=i)(1+a_j)^(-1), p=P_n and
C=2sum_i P_i w(a_i,b_i). These are the original failure-inclusive costs.
K2483/K2485's finite-mixture and least-supersolution reductions include
adaptive controls, free stages, clipping, abandonment, initial mixtures and
limiting schedules. The Bellman inequality below is on this original law;
no continuous-tail approximation replaces it.

Write A=1+a, x=(b-a)^2/[2(a+b)(2-a-b)], k=-w_a and

    M=2Ak+2w, h(b)=1+b/2+b^2/2, c(b)=(1+b)/2.

K2509 proves w_aa>0, M_a=-2A w_aa<0, and the unique interior one-stage
optimizer M=1/lambda for lambda>1. It also proves the smooth ratio extension
at score zero and positivity of U. The residual optimizer below is different:
its equation is k=U_lambda(s)/(2lambda), not M=1/lambda.

## 2. Noncircular admission of a curved ratio domain

The exact boundary hazard is

    Z(b)=2 h(b) k(c(b)b,b)
        =8(2b+7)(b^2+b+2)/[(b+3)(b+4)(b^2+15b+24)].

On 0<=b<=1/2,

    Z(b)>=2816/8001=1/L0.                              (1)

The numerator of Z-2816/8001 has five nonnegative Bernstein coefficients
after b=Y/2; their minimum is zero. Every denominator factor is strictly
positive. Equality holds at b=1/2, so this exact bound cannot be increased
uniformly on the same boundary curve.

First consider the one-stage optimizer at score s>0. At a=c(s)s one has
A=h(s), w>0 and

    M=Z(s)+2w>1/L0>=1/lambda.

Since M decreases strictly with a, its maximizing root has

    a_lambda(s)/s>c(s), U_lambda(s)<1/h(s).              (2)

This argument uses only the boundary value in (1); it does not assume the
ratio domain it is proving. U(0)=h(0)=1 by continuous extension.

Now fix s>0 and optimize the actual first-atom residual

    E_s(a,b)=(1+a)U_lambda(s)+2lambda w(a,b)-U_lambda(s-b),
    m_s(b)=min_(0<=a<=b) E_s(a,b).

For b>0 its strict convexity in a follows from w_aa>0. At a=c(b)b,
(1),(2), h(s)>=h(b) and lambda>=L0 imply

    2lambda k >=1/h(b) >=1/h(s) > U_lambda(s).

Thus E_a<0 at that boundary; at a=b, k=0 and E_a=U>0. Its unique root is
strictly interior and also has a/b>c(b). This is the second domain admission,
after the first has established the needed U bound. No equation for one
optimizer is substituted for the equation of the other.

## 3. Whole-domain curvature and hazard-normalized Schur bounds

On the curved compact domain c(b)<=r<=1,0<=b<=1/2 define the canceled
continuous extensions at a=rb of

    T=w_bb-w_ab^2/w_aa,
    M_up=-2A w_a+2x >= M,
    F=2[(w_ab-w_b/A)^2-w_bb*w_aa]/[A*M_up*w_aa].

The exact rational certificates give

    F(rb,b)>=2/5,
    T(rb,b)/k(rb,b)<=(3/8)h(b).                         (3)

The ratios in (3) are simplified before evaluating b=0 or r=1. The canceled
polynomials, rather than the original zero-over-zero displays, define those
boundary values. Use

    r=(1+b)/2+(1-b)X/2, b=Y/2, 0<=X,Y<=1.

This parameterization covers the entire curved domain. Its substitutions are
sequential: replacing b must also act inside the inserted expression for r.
For F-2/5 the numerator has bidegree(11,19), with 240 strictly positive
Bernstein coefficients and minimum 6. For (3/8)h-T/k the numerator has
bidegree(7,12), with 104 strictly positive coefficients and minimum 57147/4096.
The certificate independently proves fixed signs and nonvanishing of every
denominator factor and reconstructs each numerator and denominator factor
in the Bernstein basis. These are whole-domain polynomial certificates,
not sampled rational-function checks.

At the one-stage optimizer M=1/lambda. Its envelope identity is

    U_lambda''(t)=(2lambda/A)[(w_ab-w_b/A)^2/w_aa-w_bb].

Because the numerator in F is positive and M_up>=M, (3) implies

    U_lambda''(t)>=F(a_lambda(t),t)>=2/5.               (4)

At the distinct first-atom optimizer, 2lambda k=U_lambda(s), so the second
inequality in (3) directly gives

    2lambda T=U_lambda(s)T/k
       <=(3/8)U_lambda(s)h(b)<=3/8.                    (5)

The multiplication is legitimate because U>0. The last bound uses h(b)<=h(s)
and (2); no sign-unsafe substitution into a negative correction is needed.
The endpoint cases follow by the smooth canceled limits.

## 4. All-policy bound and stability of near-optimal finite schedules

Optimizing over a gives the Schur-envelope identity

    m_s''(b)=2lambda T-U_lambda''(s-b)<=-1/40.

The continuous endpoint values are m_s(0)=m_s(s)=0. Hence concavity of
m_s(b)-b(s-b)/80 yields

    E_s(a,b)>=m_s(b)>=b(s-b)/80>=0.                    (6)

K2483/K2485's original-law transfer therefore proves

    p-lambda C<=U_lambda(S)

for every admitted adaptive policy; the one-stage maximizer attains equality.
This is a global support theorem, not only a local stationary-point test.

For finite completed schedules put s_i=sum_(j>=i)b_j. Multiply (6) by the
actual prefix survival P_i and telescope:

    U_lambda(S)-p+lambda C
      >=sum_i P_i b_i(s_i-b_i)/80
      >=p [S^2-sum_i b_i^2]/160.                       (7)

Every schedule with two positive-score stages has a strict gap. If its gap is
at most gamma, then

    S-max_i b_i <=160 gamma/(p S),

because sum b_i^2<=(max b_i)S. Initial mixtures inherit the average gap;
this does not imply a unique adaptive implementation or replace survival
weights with unweighted costs.

## 5. Exact constrained frontier through budget 1/100

Let a_L0(S) be the one-stage root M=1/L0 and define
K_*(S)=2w(a_L0(S),S)/(1+a_L0(S)). The single-stage cost decreases strictly
with a. For 0<K<=K_*(S), the unique a with 2w(a,S)/(1+a)=K has

    F_S(K)=1/(1+a),

and at K=0 the value is1/(1+S). The multiplier associated with that a is
at least L0, so the support theorem proves optimality over the full policy
class, including mixtures. K_* is a sufficient endpoint, not the true one.

For S=1/2 put a=1/2-d, A=3/2-d, x=d^2/[2(1-d^2)]. Then

    C(d)=2log(1+x)/A,
    M(d)=4Ad/[(1-d^2)(2-d^2)]+2log(1+x).

At d0=2/17, the rational inequalities x/(1+x)<=log(1+x)<=x give

    2x/[A(1+x)]-1/100=111/1348900>0,
    1/L0-[4Ad0/((1-d0^2)(2-d0^2))+2x]
      =180686/31163895>0.                             (8)

Thus C(d0)>1/100 while M(d0)<1/L0. Monotonicity places all budgets through
1/100 inside the proved regime. This doubles the previous certified interval;
it does not merely refine a decimal inverse at an already solved budget.

## 6. Exact limits, contrary constructions and remaining question

The boundary certificate (1) is sharp for its selected curve: at b=1/2 its
value is2816/8001. Lowering lambda below L0 therefore loses this sufficient
admission estimate. This alone says nothing about actual global optimality.
A stronger warning occurs at lambda 8/3. At (a,b)=(3/8,1/2),

    x=1/126, M<=M_up=327/889<3/8,
    3/8-M_up=51/7112.

The true one-stage root M=3/8 consequently has a<3/8, outside this curved
ratio domain. Extending this proof unchanged to lambda 8/3 is actually invalid,
not merely uncertified by coefficient signs. It does not exhibit a superior
policy or refute one-stage optimality there. K2503's suffix instability and
K2507's attainable optimized-tail competitors remain the distinct routes to
the true transition.

Further contrary controls reject endpoint sampling as a positivity proof,
use of the uncurved ratio rectangle (F can fall below 2/5 there), replacement
of original prefix-weighted costs by unweighted sums, sign-blind denominator
normalization, and exchanging M=1/lambda with the residual condition
2lambda k=U. No finite witness or local curve excludes remote multistage
competitors outside this supported regime.

## 7. Released stronger curve: multiplier8/3 and budget 1/90

The first proof separates domain admission from the two curvature inequalities.
This permits a substantive curve comparison while preserving the original law.
Replace its functions by

    c2(b)=1/2+9b/20, h2(b)=1+b/2+9b^2/20,
    Z2(b)=2 h2(b) k(c2(b)b,b), L2=8/3.

The exact certificates prove, on 0<=b<=1/2 and c2(b)<=r<=1,

    Z2(b)>=3/8,
    F(rb,b)>=2/5,
    T(rb,b)/k(rb,b)<=(3/8)h2(b).                       (9)

For the first inequality, the global degree-six Bernstein representation
contains negative coefficients. That is inconclusive, not a counterexample.
Split the same polynomial exactly at b=1/4. Each half has seven strictly
positive coefficients, with minima 34956477/4096 and 20683471/6144 respectively.
Every denominator factor has a certified nonzero sign. The two patches cover
the entire interval and agree at their common endpoint.

For the other inequalities, use r=c2(b)+(1-c2(b))X followed by b=Y/2. The
curvature numerator still has degree(11,19),240 positive coefficients and
minimum 6. The Schur numerator has degree(7,12),104 positive coefficients and
minimum 114924164571/4096000000. These minima refer to the normalized rational
numerators in the probe; numerator rescaling would change them without
changing the inequality.

The noncircular proof in section 2 now applies verbatim with c2,h2,L2:
M=Z2+2w>1/L2 first admits the one-stage root and proves U<1/h2(s); only then
does the boundary hazard admit the residual root. Since h2 is increasing,
(4)–(7) follow unchanged. Thus every original adaptive policy satisfies
p-lambda C<=U_lambda(S) for lambda>=8/3, and the finite multistage gap remains
p[S^2-sum b_i^2]/160. No prefix survival, mixture or adaptive assumption is
changed by the curve refinement.

For the constrained consumer, take d1=1/8,A1=11/8,x1=1/126. Exact log bounds give

    2x1/[A1(1+x1)]-1/90=43/125730>0,
    3/8-[4A1d1/((1-d1^2)(2-d1^2))+2x1]=51/7112>0.    (10)

Hence the support theorem includes every S=1/2 budget K<=1/90. At score 1/2 the old curve's
true optimizer ratio at lambda 8/3 falls below 3/4, but the new curve only requires the
smaller endpoint ratio 29/40; (9) establishes that requirement directly.
There is no contradiction with the exact old-domain limitation in section 6.

The new curve family has an exact further limitation. Every such curve with
intercept c(0)=1/2 has boundary limiting hazard 2k=7/18. The limiting one-stage
root satisfies

    2k(r,0)=2/(1+r)^2-1/2=1/lambda.

At lambda 5/2,7/18<2/5, so the true limiting root is strictly below 1/2, and by
continuity the optimizer leaves the new domain for all sufficiently small
positive scores. Changing only its slope cannot extend this proof to that
multiplier. This is an actual ratio-domain obstruction, not a competing
policy or proof of a true transition. Marginal slope/endpoint refinements
between18/7 and8/3 do not settle the more consequential global-transition
question; an actual-value residual with a different domain or a finite/
optimized-tail competitor remains the next substantive construction.

## Verification and review

The exact probe derives rational derivatives from the original logarithmic
law, reconstructs the boundary and curved-domain polynomials, checks every
Bernstein coefficient and denominator sign, and tests the envelope,
Schur-completion, telescoping and rational consumer identities. Counts are
coverage of exact certificates and controls, not counts of universal theorems.
The universal argument is the written domain admission and Bellman transfer.
The weakest seam is the distinct-root domain admission; it must remain in that
order. Independent internal review checks that argument and the polynomial
certificates. No external expert or proof-assistant certification is claimed.

[Exact probe](../../tests/channel-swings/k2515_stopping_transition_certificate_probe.py),
[saved report](../../lab/process/k2515-stopping-transition-certificate.json),
[K2513](k2513-exact-schur-stopping-2026-11-02.md),
[K2503](k2503-stopping-instability-boundary-2026-11-02.md),
[K2507](k2507-stopping-optimal-hybrid-tail-2026-11-02.md).
