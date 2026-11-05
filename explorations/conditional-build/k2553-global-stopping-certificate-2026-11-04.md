---
title: "K2553 Global original-law stopping support at the critical multiplier"
status: active_research
doc_type: exploration
created: "2026-11-04"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: global support at one fixed multiplier; no whole-budget frontier or GU claim
scripts:
  - tests/channel-swings/k2553_global_stopping_certificate_probe.py
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
result: K2553
carrier: original ordered stopping law at scores through one half and its admitted adaptive/mixture closure LAYER=toy CHIRALITY=N/A
pairing: actual failure-inclusive expected cost and prefix survival ON=declared_carrier
real_structure: real probabilities, logarithmic costs and exact Q(sqrt3) certificates
grading: finite ordered stages, adaptive policies and initial mixtures remain distinct
action_owner: repository-construction -- supplied fresh fair test/use probability law
target: whole-score critical-multiplier support theorem and constrained contact point MAP-TYPE=evaluation
```

# K2553 A global support theorem at the critical multiplier

## Result and scope

For the ORIGINAL failure-inclusive stopping law, every admitted policy at
score 0<S<=1/2 satisfies

    p-lambda_star C <= U_lambda_star(S), lambda_star=4/sqrt(3),
    U_lambda(s)=max_(0<=a<=s) [1-2lambda w(a,s)]/(1+a),
    w(a,b)=log(1+(b-a)^2/[2(a+b)(2-a-b)]).

The one-stage optimizer attains equality. This is a GLOBAL support result:
remote finite atoms, different-success mixtures and the adaptive/limiting
policy class in K2483/K2485 are covered by the original Bellman transfer.
It is not the entire constrained budget frontier or a theorem for every
lambda between lambda_star and8/3. The latter endpoint and larger multipliers
retain K2515's separate theorem. At each S this result does give an exact
constrained frontier point and a global affine upper bound at every budget.

K2551 disproved uniform concavity of this residual at lambda_star. That
counterexample survives. A positive THIRD derivative and the correct right
endpoint slope prove the needed nonnegativity without concavity. Seven exact
whole-domain certificates on two different optimizer domains establish the
bounds. Sampled signs are not used as proof.

The probability law is supplied mathematics, not a native GU probability
construction. SC-META-53 remains UNCERTAIN; ledger0.263 LT-SM8/LT-GR6b retain
their actual action, quotient and domain debts. Source, canon and empirical
claims remain unchanged. No novelty or external certification is claimed.

## 1. Distinguish both roots and admit their actual domains

Put A=1+a, x=(b-a)^2/[2(a+b)(2-a-b)], k=-w_a, M=2Ak+2w.
Reuse K2509's original-law identities w_aa>0 and M_a=-2A w_aa<0,
the unique interior maximizing root M=1/lambda for lambda>1, and its smooth
ratio extension at score zero. For this note lambda=lambda_star throughout.
The free endpoint a=s gives U(s)>=1/(1+s)>=2/3; w>=0 gives U(s)<=1.

For fixed S define the optimized first-atom residual

    E_S(a,b)=(1+a)U(S)+2lambda w(a,b)-U(S-b),
    m_S(b)=min_(0<=a<=b) E_S(a,b).

Its a-root solves 2lambda k=U(S), NOT M=1/lambda. Strict positivity of
w_aa gives uniqueness. The exact hazard certificates on 0<=b<=1/2 prove

    2lambda k((23/50)b,b)>=1,
    2lambda k((3/5+7b/20)b,b)<=2/3.

Since k decreases with a, the residual root belongs to

    23/50 <= a_res/b <= 3/5+7b/20.                    (1)

All ratios in (1) are strictly between0 and1. These bounds use the elementary
U bounds above, not a circular assumption about the residual optimizer.

The one-stage root requires a DIFFERENT narrower domain. Define

    r0=2sqrt(3)-3, c0=4sqrt(3)-13/2,
    l(b)=r0+c0 b+(9/100)b²,
    h(b)=r0+c0 b+(1/8)b².

Exact polynomial certificates prove

    2(1+l b)k(l b,b)+2[x_l-x_l²/2] >=sqrt(3)/4,
    2(1+h b)k(h b,b)+2[x_h-x_h²/2+x_h³/3] <=sqrt(3)/4.

For x>=0, integrating the geometric identities for1/(1+x) gives
x-x²/2<=log(1+x)<=x-x²/2+x³/3. Monotonicity of M therefore admits

    l(b)<=a_one(b)/b<=h(b).                           (2)

Equality at b=0 is the correct continuous limit; it is not a singular root
or an omitted boundary. Both curves stay inside(0,1) on the closed score
interval, as follows directly from their coefficients and endpoint values.

## 2. The global derivative and endpoint certificates

Derive all derivatives from the original logarithm before making the ratio
substitution. Define

    q=w_ab/w_aa, v=w_ab-w_b/A,
    T=w_bb-w_ab²/w_aa,
    H=[v²/w_aa-w_bb]/A,
    T3=T_b-q T_a,
    H3=H_b-(v/w_aa)H_a.

The exact rational functions at a=rb have canceled continuous extensions at
b=0. Individual uncanceled derivatives may diverge; only these canceled
expressions are used on the closed rectangles. Implicit differentiation of
the two actual root equations gives

    a_res'=-q, a_one'=-v/w_aa,
    U''=2lambda H,
    m_S'''(b)=2lambda[T3(a_res,b)+H3(a_one(S-b),S-b)]. (3)

The probe certifies over the WHOLE respective domains

    T3>=1/30 on(1), H3>=-3/100 on(2),
    2w_b(rb,b)<=3sqrt(3)/4-1 on(2).                  (4)

Thus m_S'''>=lambda/150. The last inequality is certified directly on the
whole ribbon, so it needs no unverified monotonicity substitution.
At b=S the two roots agree. The smooth zero-score value derivative is

    U'(0)=-[r0+lambda g(r0)], g(r)=(1-r)²/[2(1+r)],
    r0+lambda g(r0)=lambda(3sqrt(3)/4-1).

Consequently

    m_S'(S)=lambda[2w_b(a_one(S),S)-(3sqrt(3)/4-1)]<=0. (5)

No sign of m_S'' is asserted. Its strictly positive K2551 fixture is fully
consistent with(3)--(5).

## 3. How the certificates cover every point

For each rational expression, substitute r=l(b)+(h(b)-l(b))X then b=Y/2,
with X,Y in[0,1]. Use the constant/linear residual curves for(1), and the
quadratic one-stage curves for(2). Boundary hazard and M certificates use
the degenerate ribbon with equal lower and upper curves. The resulting
numerator and denominator polynomials have coefficients in Q(sqrt(3)).

Expand each in the tensor Bernstein basis. Every numerator coefficient is
nonnegative and every denominator coefficient is strictly positive after a
common sign orientation. The basis functions are nonnegative and sum to1,
so these are whole-domain inequalities with nonvanishing denominators.
The probe independently reconstructs both polynomials by inverse forward
differences; a wrong conversion cannot pass simply by being reused as data.
Signs of a+b sqrt(3) are decided by rational signs and comparing a² with3b².
No floating tolerance determines certificate acceptance.

Seven certificates cover: two residual hazards, two one-stage M boundaries,
T3, H3 and the endpoint w_b bound. The largest transformed numerator has
bidegree(24,64), with1625 coefficients; these are not independent theorems.
The report gives actual degrees, coefficient counts, zero counts and exact
coefficient hashes. Every coefficient and inverse basis identity is recomputed
from the original law, rather than trusted from a stored sign assertion.

## 4. Hermite shape lemma replaces the failed concavity proof

The continuous endpoint values are m_S(0)=m_S(S)=0. The root ratio extensions
and the canceled derivatives make m_S three times continuously differentiable
on[0,S]. For the residual root specifically, k(rb,b) tends to -g'(r)/2 and its r derivative is -g''(r)/2<0. The implicit function theorem therefore gives a smooth residual ratio at zero for each fixed U(S); this is distinct from the reused one-stage extension. The Hermite interpolation formula with nodes0,S,S gives, for each
0<b<S, some xi in(0,S) with

    m_S(b)=-m_S'(S)b(S-b)/S + m_S'''(xi)b(S-b)²/6.

One can prove the remainder directly by subtracting the interpolant and
c b(b-S)², choosing c to make the difference vanish at b, then applying
Rolle's theorem three times with the double zero at S. Using(3)--(5),

    E_S(a,b)>=m_S(b)>=lambda b(S-b)²/900.             (6)

This is strict inside the score triangle. It avoids both the failed uniform
nonpositive-curvature premise and an inference from sampled residual values.
The endpoints follow by continuity and the actual maximizing definition of U.

## 5. Released all-policy and budget consequences

For any finite completed ordered schedule, let

    s_i=sum_(j>=i)b_j, P_i=product_(j<=i)(1+a_j)^(-1),
    p=P_n, C=2sum_i P_i w(a_i,b_i), sum b_i=S.

Multiplying(6) by P_i and telescoping the original prefix weights gives

    U(S)-p+lambda C
      >=lambda/900 sum_i P_i b_i(s_i-b_i)²>=0.        (7)

Every schedule with at least two positive-score stages has a strictly
positive right side. Initial mixtures preserve the EXPECTED gap. The
nonnegative Bellman inequality, U(0)=1 and U>=0 meet K2483/K2485's existing
adaptive, clipping, abandonment and limiting-policy transfer hypotheses;
no new cost convention or finite-stage approximation is introduced.
A one-stage schedule at the root attains the support value exactly.
This does not prove uniqueness of an adaptive implementation or a uniform
positive gap for all infinite-stage limits.

Define

    a*=a_one(S), K*=2w(a*,S)/(1+a*), p*=1/(1+a*).

At budget K*, equation(7) proves p<=U(S)+lambda K*=p*, and the single stage
attains it. Hence F_S(K*)=p* is an exact unrestricted constrained frontier
point. At ANY other budget K, it supplies the honest affine upper bound
F_S(K)<=min(1,U(S)+lambda K). It does not assert this line is attained.
K2515 continues to supply the separate exact low-budget interval through1/90
at S=1/2. No interpolation between those exact points becomes a theorem.

For finite schedules within eta of the support optimum, a consequential
structural bound follows directly from(7): any stage of score at least u>0
with remaining score after it at least v>0 must satisfy

    eta>=lambda p u v²/900.

Thus remote pairs of appreciable stages have a certified positive cost gap,
not only the local-satellite exclusion of K2551. This is weaker than a full
stage-count classification, and retains the actual survival factor p.

## 6. Released sharp lower-multiplier boundary

K2517 section4 equation(11) already proves that for every fixed
1<lambda<lambda_star, two equal stages beat the optimized one-stage value
for all sufficiently small positive scores. Reuse that original-law expansion
and its strict sign; do not count it as a new computation. Together with this
whole-score theorem, lambda_star is the LEAST multiplier in(1,infinity) at
which one-stage support is globally valid uniformly over0<S<=1/2. This is a
minimality assertion, not a claim that the set of such multipliers is an
interval. The interval between lambda_star and8/3 still needs its own proof.

## Evidence and next condition

The exact probe verifies derivative identities, seven whole-domain
certificates with denominator signs and inverse reconstruction, the Hermite
polynomial identities and original prefix telescope. Contrary controls reject
wrong weights, conflated roots, sign-blind denominators, endpoint sampling,
corrupted Bernstein data and a wrong endpoint interpolant. Universal policy
transfer uses the written argument and existing transfer theorem, not a count
of fixture passes. Independent internal review is not external or Lean certification.

The global supporting problem at lambda_star is now settled for every
0<S<=1/2. Next compare a parameter-uniform Bellman certificate or a new
support value at the fixed-score local onset against the full localized-source
domain construction. The unresolved budget interval and different lambda
values are genuinely different questions; another local Taylor coefficient
or decimal evaluation at this already solved support is not the successor.

[Probe](../../tests/channel-swings/k2553_global_stopping_certificate_probe.py),
[report](../../lab/process/k2553-global-stopping-certificate.json),
[previous global range](k2515-stopping-transition-certificate-2026-11-02.md),
[failed concavity and local theorem](k2551-finite-score-stopping-separation-2026-11-04.md),
[original transfer](k2485-constrained-stopping-frontier-2026-11-01.md).

[Lower-multiplier counterexample](k2517-small-score-stopping-transition-2026-11-02.md).
