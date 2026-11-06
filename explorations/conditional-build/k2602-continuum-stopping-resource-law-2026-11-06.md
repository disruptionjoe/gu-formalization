---
title: "K2602 Continuum stopping resource law and optimal score mesh"
status: active_research
doc_type: exploration
created: "2026-11-06"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: full certified continuum multiplier regime and compact-parameter resource asymptotic; no exact finite optimizer or physical probability
scripts:
  - tests/channel-swings/k2602_continuum_stopping_resource_law_probe.py
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
result: K2602
carrier: original predictable randomized fair test/use histories at total score0<S<=1/2 and positive-trial resource R=E N_plus LAYER=toy CHIRALITY=N/A
pairing: unconditional success minus multiplier times original leakage including all stopping outcomes ON=declared_carrier
real_structure: real probability law, exact scalar identities and certified Arb interval integrals
grading: remaining score, survival occupation, action ratio, continuum limit and finite trial resource remain distinct
action_owner: repository-construction -- supplied stopping model
target: full continuum-regime resource coefficient and constructive nearoptimal variable-step policies MAP-TYPE=evaluation
```

# Nearoptimal occupation determines the resource coefficient

## Result and scope

K2601 proved the critical-multiplier resource coefficient. The same coefficient does not extend by substituting a new lambda: above critical the optimal action and survival vary along the score path. Here an all-policy occupation theorem supplies the missing transfer. For every fixed0<S<=1/2 and0<lambda<=4/5,

    V_lambda(S)-F_lambda(M,S)=C(S,lambda)/M+O(M^-3/2),
    C(S,lambda)=2lambda I²,
    I=integral_0^S P(s) sqrt(D(v(s))) ds.              (1)

All quantities below come from the ACTUAL original law and K2561's certified continuum flow. The new above-critical result covers randomized and highly uneven histories, not just schedules near an assumed deterministic path. A variable score mesh achieves the sharp coefficient; equal score spacing is strictly worse at leading order above critical. Explicit interval coefficient enclosures and four actual finite rational mesh policies execute the construction.

The error bound can be chosen uniformly on compact parameter rectangles0<Smin<=S<=1/2,0<lambdamin<=lambda<=4/5, including the critical and2/3 switching curves. This is a leading resource theorem, not a higher-order bifurcation law or exact finite optimizer. No physical probability, controller realization, GU verdict, novelty, external-expert or proof-assistant certification. SC-META-53 remains UNCERTAIN; ledger0.263 LT-SM8/LT-GR6b, source and canon remain unchanged.

## 1. Continuum quantities and exact local loss

Reuse w(a,b)=log[1+(b-a)²/(2(a+b)(2-a-b))] and the original positive-trial resource of K2571. K2561 proves the unrestricted value V_lambda(s)=lambda v(s), where

    theta=1/lambda, v(0)=theta, v'(s)=-q(v(s)),
    q(v)=2sqrt(1+2v)-2-v for1<=v<=3/2,
         1/2 for v>=3/2.

All trajectories satisfy v(s)>=theta-s/2>=1. Define u=v(S), r*(s)=q'(v(s)), and

    P(s)=exp[-integral_s^S r*(z)dz]=q(u)/q(v(s)).      (2)

Remaining score decreases S to0. Thus P(S)=1 and P(0) is continuum success. The orientation is essential; replacing P by its inverse or by1 gives a different resource coefficient.

For r=a/b in[0,1], the exact original logarithm has the UNIFORM expansion on bounded score intervals

    2w(rb,b)=b g(r)+b² B(r)+O(b³),
    g(r)=(1-r)²/[2(1+r)],
    B(r)=(1-r)²/4-(1-r)^4/[16(1+r)²].                (3)

The rational argument is smooth through b=0 after cancelling b, uniformly for r in[0,1]. The generator is q(v)=min_(0<=r<=1)[rv+g(r)], and g''=4/(1+r)^3>=1/2. Thus

    H_s(r)=rv(s)+g(r)-q(v(s)) >=(r-r*(s))²/4,        (4)

including the zero-action KKT boundary. Taylor expansion of v(s-b), whose second derivative is q q', yields the actual Bellman residual

    d/ lambda=b H_s(r)+b²[B(r)-q(v)q'(v)/2]+O(b³).

Put

    D(v)=B(r*)-q(v)r*/2.                              (5)

B is Lipschitz on[0,1]. Completing the square in b(r-r*)²/4 minus a constant times b²|r-r*| gives a fixed C0 such that

    d>=lambda b²[D(v(s))-C0 b]                       (6)

uniformly in clipped controls and remaining score. This does not assume the actual policy already chooses r*. It is the key action-transfer estimate. Separately, K2561's exact global generator bound gives d>=lambda gamma b²/2, gamma=78360951/2744000000, throughout the domain.

For the interior optimizer r=2/sqrt(1+2v)-1,

    q=(1-r)(3r+1)/[2(1+r)²],
    D=(1-r)(3r+1)(3-6r-r²)/[16(1+r)²]
      =q(3-6r-r²)/8>0.                               (7)

Here0<=r<=2/sqrt3-1<1/6. The last polynomial is decreasing but positive at that endpoint. On the zero-action branch D=3/16. Both r* and D are continuous Lipschitz across v=3/2. Their derivatives need not match there; the proof uses Lipschitz bounds, not unjustified smoothness.

## 2. Prove nearoptimal occupation for the full original policy class

Write eta=V_lambda(S)-p+lambda C>=0. Let b'=min(b,s), a'=min(a,b') and r=a'/b' where b'>0. The original telescope has loss delta=d/2 plus nonnegative clipping and terminal losses. Its global bound implies

    E sum_active b'^2=O(eta).

The uniform first-order expansion and(4), combined with that quadratic bound, give

    E sum_active b'(r-r*(s))²=O(eta).                 (8)

Indeed the first-order residual is bounded below by a constant times b'(r-r*)² minus C b'^2, which is summable as just shown. Define the positive occupation measure

    mu_eta=(1/2) E sum_active b' delta_s.

Fresh fair use gives its mass E sum_use b'<=S. Abort and nonabsorption probabilities are O(eta), because V(s)>=lambda>0. The summed excess-action clipping term E sum(a-a') is O(eta) by its positive V(s) coefficient. Overshoot clips progress to s; its leakage losses remain nonnegative. These bounds do not count an infinite approach to score0 as success.

For any C^(1,1) function f with f(0)=0, the ORIGINAL trial telescope reads

    f(S)=(1/2)E sum_active [(1+a)f(s)-f(s-b')]
                  + terminal terms.

A use jump changes remaining score to s-b'; rejection occurs on the test branch and has zero continuation, while a test pass retains s. This is the same factor1/2 accounting as the value telescope. Taylor's inequality for f, clipping control and(8) give

    f(S)=integral [f'(s)+r*(s)f(s)]dmu_eta
                               +O_f(sqrt(eta)).       (9)

Cauchy--Schwarz controls the action error using(8) and mu mass<=S; second-order score errors are O(eta). Terminal terms are O_f(eta), even for arbitrary randomized abort/nonabsorption. No deterministic path or bounded stage count was assumed.

Now let phi be Lipschitz and solve

    f'+r*f=phi, f(0)=0.

Since r* and phi are Lipschitz, f is C^(1,1), including switching points. Its integrating-factor formula gives f(S)=integral_0^S P(s)phi(s)ds. Consequently

    integral phi dmu_eta=integral_0^S P phi ds
                               +O_phi(sqrt(eta)).     (10)

This is quantitative occupation convergence for ALL nearoptimal original policies. It is the bridge missing from a fixed-count or formal continuum expansion. The homogeneous equation with f(0)=1 similarly gives p tending P(0), but success convergence is not needed to assume(10).

## 3. Lower bound with the correct survival weight

For small epsilon, the large-step score mass is O(eta/epsilon), since E sum b'^2=O(eta). On b'<=epsilon use(6). D has a positive lower bound, so choose epsilon with D-C0 epsilon>0. Cauchy--Schwarz on trial occupation, using E N_+<=M, gives

    M eta >=(lambda/2)
       [E sum_(b'<=epsilon) b' sqrt(D(v(s))-C0 epsilon)]².

The test sqrt(D-C0 epsilon) is Lipschitz with a uniform Lipschitz bound as epsilon tends0. Apply(10) and remove the large-step mass:

    M eta >=2lambda I²-O(epsilon+sqrt(eta)+eta/epsilon).

Take epsilon=sqrt(eta) for sufficiently small eta. Thus

    M eta >=2lambda I²-O(sqrt(eta)).                  (11)

The constants depend only on the specified compact parameter range. Initial mixtures and rare high-resource histories are already covered by the occupation measure. Replacing P by1 would remove actual survival and is not this theorem.

## 4. Construct finite policies attaining the coefficient

Choose a small mesh parameter t>0. Starting at s_1=S, repeat stages

    b_i=min{s_i,t/sqrt(D(v(s_i)))},
    a_i=r*(s_i)b_i, s_(i+1)=s_i-b_i.                 (12)

D is bounded above and below, so the schedule has finitely many stages. Each stage uses the original repeated fair trial law; the original survival is P_i=product_(j<=i)(1+a_j)^-1. Since r* is Lipschitz and every b_i=O(t), product/Riemann estimates give P_i=P(s_(i+1))+O(t) uniformly. The final clipped stage contributes O(1) resource and O(t²) loss.

For the actual resource and value deficit,

    R_t=2 sum P_i=2I/t+O(1),
    eta_t=sum P_i d_i=lambda t I+O(t²).              (13)

The first equation is the Riemann sum of2P sqrtD/t; the second uses d_i=lambda D(s_i)b_i²+O(b_i³) because r=r*. All weights are the original success prefixes. The continuum trajectory does not replace finite absorption.

Set t=(2I/M)(1+M^-1/2). Then R_t=M/(1+M^-1/2)+O(1)<=M for all sufficiently large M. This explicit slack absorbs the final-stage/count error WITHOUT abort dilution, which could add a leading value loss. Equation(13) gives

    eta_t=2lambda I²/M+O(M^-3/2).

The lower bound(11), applied to policies within o(M^-2) of the supremum and using this feasible O(1/M) upper gap, proves(1). Attainment is not required for this argument.

## 5. Released allocation, parameter and stability consequences

A uniform score mesh has a different leading coefficient:

    C_equal=2lambda [integral P ds][integral P D ds].

Weighted Cauchy--Schwarz gives C_equal>=2lambda[ integral P sqrtD ds ]², with equality exactly when D is constant along the path. For lambda>2/(3+S), an interval of the path has positive action and varying D, so the inequality is STRICT. The variable step law b proportional to1/sqrtD is therefore a substantive allocation improvement, not merely another way to discretize the same equal mesh. Both retain the order1/M; only the variable allocation attains the optimal leading constant.

If lambda<=2/(3+S), the whole path has v>=3/2: P=1,D=3/16 and C=3lambda S²/8, matching K2601 and the already-known eventual subcritical tail. For2/(3+S)<lambda<2/3, the switching remaining score is s0=2/lambda-3. Actions are positive EARLY (s>s0), then zero in the late tail. For lambda>=2/3 the path is interior apart from a possible endpoint. Neither switching point breaks the Lipschitz proof.

All estimates can be made uniform on0<Smin<=S<=1/2,0<lambdamin<=lambda<=4/5: v stays in[1,1/lambdamin], q has a positive lower bound, r* and D are uniformly Lipschitz with positive D, the original cost expansion is uniform, terminal potential is bounded below, and I is bounded away from0. The construction slack and all-policy estimates therefore share uniform constants. This permits leading-order simultaneous parameter/resource limits inside that compact range, including critical crossing. It does not resolve a scaled NEXT-order activation profile.

Equation(8) is also an action-stability theorem: nearoptimal policies cannot keep a positive score-weighted mean-square distance from the continuum action. Equation(10) fixes their limiting expected score occupation even when their individual sample paths or stage counts differ. No unique finite policy or pathwise concentration follows from those averaged statements.

### Necessary mesh allocation for every asymptotically optimal adaptive policy

The Cauchy equality case gives a stronger, averaged rigidity result. Suppose policies satisfy R_M<=M and eta_M=C(S,lambda)/M+o(1/M). Then

    R_M/M ->1,
    (1/M)E sum_active [M b' sqrt(D(v(s)))-2I]² ->0.    (15)

The sum is over positive-score trials. This does not claim pathwise uniqueness, fixed stage count or absence of rare exceptional histories.

Here are the uniform-integrability details needed before using Cauchy equality. Split the actual nonnegative telescope losses into b'<=epsilon and b'>epsilon. For fixed small epsilon, the small-step proof of section3 gives liminf M times its loss at least2lambda I_epsilon², with I_epsilon=integral P sqrt(D-C0 epsilon)ds. Total M eta tends2lambda I², so limsup M times large-step loss is O(epsilon). The global gamma bound converts this to limsup M E sum_large b'^2=O(epsilon). Also M E sum_all b'^2 is bounded. Therefore

    M E sum b'^3 <= epsilon M E sum_small b'^2
                       +S M E sum_large b'^2 ->0

after first taking limsup M and then epsilon to0. From(6),

    limsup M E sum D b'^2 <=4I².

Equation(10) gives E sum b' sqrtD ->2I. Occupation Cauchy implies M E sum D b'^2 >=(M/R_M)(E sum b' sqrtD)², forcing R_M/M->1 and convergence of the second moment to4I². Expanding the square in(15) now gives zero. This supplies necessary optimal score allocation even for arbitrary adaptive mixtures, rather than merely exhibiting one efficient deterministic construction.

## 6. Rigorous coefficient and finite-policy consumers

Use the exact clock tau of K2561 to enclose u from tau(u)=tau(1/lambda)-S. Changing variables in(1) gives

    I=q(u) integral_u^(1/lambda) sqrt(D(v))/q(v)² dv.  (14)

The probe bisects this monotone equation with exact rational endpoints and rigorous Arb signs. It covers EVERY quadrature cell with an interval, splits at3/2, integrates the constant branch exactly, and explicitly subtracts the uncertain lower-root segment. At192-bit arithmetic,16384 cells give the following rigorous enclosing displays:

| S | lambda | C(S,lambda) enclosure (rounded outward) |
|---|---|---|
| 1/2 | 3/5 | 0.0556611217 +/-0.0000010 |
| 1/2 | 4/5 | 0.0526371262 +/-0.0000089 |
| 1/4 | 7/10 | 0.0150059327 +/-0.0000013 |

The interval report carries the actual certified enclosures. A4096-cell attempt did not meet the selected width criterion for lambda4/5; the final16384-cell calculation does. This is complete interval coverage, not a sampled quadrature or inferred error from mesh convergence.

Four complete finite policies execute(12) at S=1/2, lambda3/5 and4/5, t=1/50 and1/100. At each stage the interval flow supplies a rational step and action by certified downward rounding to a10^-12 grid, followed by exact final-score clipping. Replay evaluates those actual rational schedules with original prefix survival, leakage logs and resource. These finite examples are feasible comparisons; they are not claimed to satisfy the asymptotic slack inequality at a prescribed arbitrary M or to be exactly optimal. All actions, scores, resources and rigorous value gaps are saved. Root signs fail closed if unresolved; the exact zero-action branch endpoint is handled directly. The same interval integration also certifies at score1/2,lambda4/5 that the equal-score coefficient is strictly larger than the optimal variable-mesh coefficient, exercising the actual allocation counterconstruction. No optimizer or simulation stands in for the global proof.

## Evidence and remaining question

Exact symbolic checks establish the original-log expansion, strong convexity, D formula, branch join, uniform remainder absorption and resource/loss weighting. Certified full-interval integration evaluates the new coefficient. Actual rational policies test finite construction and reject nominal unweighted trial count. The adaptive occupation, original telescope transfer and asymptotic optimality are written proofs subjected to independent review; arithmetic counts do not certify them.

The certified continuum-regime leading resource question is now answered, including above-critical survival and optimal score allocation. Next-order profile/coefficient, exact finite policies or the unexplored multiplier regime beyond4/5 require new estimates; no extrapolation of this certified flow comparison is licensed. Physical detector/source coupling remains a distinct source-facing alternative.

[K2561](k2561-higher-budget-stopping-2026-11-05.md), [K2571](k2571-stopping-resource-price-2026-11-05.md), [K2601](k2601-critical-stopping-resource-limit-2026-11-06.md), [probe](../../tests/channel-swings/k2602_continuum_stopping_resource_law_probe.py), [report](../../lab/process/k2602-continuum-stopping-resource-law.json).
