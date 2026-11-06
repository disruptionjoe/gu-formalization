---
title: "K2604 Second-order stopping resource bound and priced complexity"
status: active_research
doc_type: exploration
created: "2026-11-06"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: all-policy O(M^-2) remainder and quantitative constructions in the certified continuum regime; no second-order coefficient or physical probability
scripts:
  - tests/channel-swings/k2604_second_order_stopping_resource_bound_probe.py
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
result: K2604
carrier: original predictable randomized fair test/use histories, finite-hit success and positive-trial expected resource R LAYER=toy CHIRALITY=N/A
pairing: unconditional success minus multiplier times original leakage and a price per positive trial ON=declared_carrier
real_structure: real probabilities, exact scalar inequalities and rigorous interval finite-policy replay
grading: resource ceiling, per-trial price, finite stage count, continuum flow and physical probability remain separate
action_owner: repository-construction -- supplied fair stopping law
target: uniform remainder, priced value, inverse budget and finite construction MAP-TYPE=evaluation
```

# Close the remainder gap without assuming deterministic nearoptimal histories

## Result and scope

For every fixed0<S<=1/2 and0<lambda<=4/5, let V_lambda(S) be the unrestricted value and F_lambda(M,S) the value with expected positive-trial resource at most M. K2602 proved the leading coefficient C=2lambda I² with error O(M^-3/2). Here a priced Bellman supersolution improves the ALL-policy estimate to

    V_lambda(S)-F_lambda(M,S)=C(S,lambda)/M+O(M^-2).    (1)

The constants are uniform on compact rectangles with positive lower bounds for S and lambda. The proof includes arbitrary adaptive policies, initial randomization, abort and nonabsorption. A complete finite schedule supplies the upper bound, with the explicit safe estimate for M>=8,

    gap <= C/(M-4)+70C/(M-4)² <= C/M+288C/M².         (2)

The small-price value Q(k)=max(J-kR) obeys

    Q(k)=V-2sqrt(Ck)+O(k).                            (3)

Consequences below give inverse resource C/eta+O(1) and the resource/stage scale of positive-price optimizers. These are a second-order ERROR BOUND, not a computed coefficient of M^-2, a unique finite policy, or a next-order activation profile. K2577's exact subcritical priced tail is retained; the present result covers the full certified continuum regime, including positive-action paths and the switching curves.

The law is supplied mathematics, not a physical detector or Born probability. SC-META-53 remains UNCERTAIN. Source, ledger0.263 LT-SM8/LT-GR6b, canon and native-action/domain bridges are unchanged. No novelty, external-expert or proof-assistant certification.

## 1. Fix actual law, continuum quantities and useful uniform constants

For clipped positive actions0<=a<=b<=s<=S, put r=a/b and

    w(a,b)=log[1+(b-a)²/(2(a+b)(2-a-b))],
    g(r)=(1-r)²/[2(1+r)],
    B(r)=(1-r)²/4-(1-r)^4/[16(1+r)²].

K2561 gives V(s)=lambda v(s), v(0)=1/lambda, v'=-q(v), with q=2sqrt(1+2v)-2-v below3/2 and q=1/2 above. Set r*(s)=q'(v(s)), and reuse

    D(s)=B(r*)-q(v)r*/2,
    P(s)=exp[-integral_s^S r*(z)dz],
    I=integral_0^S P(s)sqrt(D(s))ds, C=2lambda I².

The coefficient and its rigorous enclosures are K2602's result, not rederived by another quadrature. The ORIGINAL residual d_V=(1+a)V(s)+2lambda w(a,b)-V(s-b) satisfies

    d_V/lambda=bH_s(r)+b²[D(s)+B(r)-B(r*)]+rho,
    H_s(r)=rv(s)+g(r)-q(v(s)) >=(r-r*)²/4,
    |rho|<=6b³.                                     (4)

The following safe constants hold throughout the certified regime:

    0<=r*<=1/6, 9/20<=q<=1/2, Lip_s r*<=1/4,
    1/10<=D<=3/16, Lip_s D<=1/6,
    h=sqrtD: hmin=3/10, hmax=1/2, Lip h<=1/3.        (5)

For the interior branch write v=2/(1+r)²-1/2. Then

    D=(1-r)(3r+1)(3-6r-r²)/[16(1+r)²].

Its derivative is nonpositive on[0,1/6], D(1/6)=355/3136>1/10, and |D_r|<=2/3, which with Lip_s r*<=1/4 proves(5). On the zero-action branch D=3/16. Both branches join continuously and are Lipschitz; no nonexistent second derivative at a switch is used.

To check the remainder in(4), write EXACTLY

    w(rb,b)=log(1-alpha(r)b)-log(1-beta(r)b),
    alpha=(1+6r+r²)/[4(1+r)], beta=(1+r)/2.

For r in[0,1],0<=alpha<=beta<=1 and b<=1/2, the absolute third b derivative of2w is at most32. Also v''=q r* is Lipschitz with constant at most1/4, so its second-order Taylor remainder is at most b³/24. The sum32/6+1/24<6 proves the chosen constant. A safe bound Lip B<=4 follows directly from its rational derivative. The probe checks those rational inequalities over their full intervals, not at sampled r.

## 2. A priced barrier with the correct trial factor

Write k=e²>0. Define W by

    W'+r*W=2sqrt(2lambda D), W(0)=0.

The integrating factor gives W(S)=2sqrt(2lambda)I=2sqrt C. From(5),

    0<=W<=1, Lip W<=3, Lip W'<=2.                   (6)

The bounds use W<=2s, |W'|<=2+1/6, and Lip[2sqrt(2lambda D)]<=1. They hold across switching points. For lambda>=lambda_min>0, let

    K=1251/lambda_min+1,
    U_e(s)=V(s)-eW(s)+e² K s.                        (7)

At s=0 this equals1. For e<=lambda_min/2, U_e>0 on the whole interval. We will show that, for sufficiently small e, it is a supersolution for J-e²R:

    Delta=(1+a)U_e(s)+2lambda w(a,b)+2e²-U_e(s-b)>=0. (8)

The factor2e² is essential: a repeated positive stage has original expected trial count2/(1+a), not1/(1+a). A zero-length stage is deleted and has no positive-trial charge.

Put z=r-r*. From(4), the action error obeys

    lambda b z²/4-(4lambda b²+e b|W|)|z|
       >=-32lambda b³-2e²b/lambda.

Together with the remainder6lambda b³ and the W Taylor error at most e b², this gives

    Delta >= L(b-ec)^2-31b³-e b²-(2/lambda_min)e²b
                       +K e²b,
    L=lambda D, c=sqrt(2/L).                        (9)

Indeed Lb²-e b*2sqrt(2L)+2e² is the displayed square; 38lambda<=30.4<31. The K correction contributes e²K(b+as), whose additional as term is nonnegative.

For b<=delta=lambda_min/1250, let cmax=sqrt(20/lambda_min). The exact estimates

    b³<=2b(b-ec)²+2cmax²e²b,
    e b²<=b(b-ec)²/2+(1/2+cmax)e²b

absorb the remainders into half of L(b-ec)² and K e²b. Our K exceeds62cmax²+(1/2+cmax)+2/lambda_min. To verify this with no hidden parameter restriction, lambda_min<=4/5 implies cmax<=4/lambda_min. Thus(8) holds for all small b, including b much smaller or much larger than e. No actual action r is assumed near r*.

For b>=delta, use the global ACTUAL K2561 bound d_V>=lambda gamma b²/2, gamma=78360951/2744000000. Equation(6) bounds the negative W term by4e b. Consequently

    e <= min(lambda_min/2, lambda_min gamma delta/16)  (10)

suffices for the large-step inequality too. This deliberately conservative threshold is sufficient, not a transition price prediction.

## 3. Transfer the barrier to every original policy

Original overshoots and a>b use the proved monotone clipping b'=min(b,s),a'=min(a,b'). The extra action term is (a-a')U_e(s)>=0 and the original leakage difference is nonnegative. For b=0 the no-price residual is aU_e>=0; no fictitious charge is added to zero padding. The same original fair-trial telescope as K2561/K2571, with U_e(0)=1 and bounded positive U_e, handles abort and nonabsorption. Alternatively K2571's resource-preserving reduction to finite schedules and abort supplies the same bound; infinite expected resource has penalized value minus infinity. Thus

    Q(e²)<=U_e(S)=V-2sqrt C e+KS e².                 (11)

This step covers randomized, uneven and adaptive policies through the actual-law telescope/reduction. It is not inferred from a deterministic discretization. Since F(M)<=Q(e²)+e²M, choose e=sqrt C/M. For M sufficiently large to satisfy(10),

    V-F(M)>=C/M-KS C/M².                            (12)

No differentiability, attainment or exchange of infimum with asymptotic expansion was used for this lower bound.

## 4. Make the feasible resource slack a bounded constant

Use K2602's complete finite variable mesh at step parameter t:

    b_i=min(s_i,t/h(s_i)), a_i=r*(s_i)b_i,
    P_i=product_(j<=i)(1+a_j)^-1,
    R_t=2sum P_i, eta_t=sum P_i d_i.                (13)

For t<=1, n<=S hmax/t+1. Comparing log P_i with -integral r* using log(1+a)=a+O(a²) yields the uniform prefix estimate

    |P_i-P(s_(i+1))|<=E0 t,
    E0=(rmax²+Lip r*)S/(2hmin)<=25/108.

The product P*h has Lipschitz constant at most Lip h+rmax hmax. Riemann summation, with the last clipped stage contributing at most1 before the factor2, gives

    |R_t-2I/t|<=K_R,
    K_R=2[E0(S hmax+1)+S(Lip h+rmax hmax)/(2hmin)+1]
       <=707/216<4.                                (14)

At r=r*, |d_i-lambda D_i b_i²|<=6lambda b_i³. The final-stage mismatch uses x(t-x)<=t²/4 for x=h_i b_i in[0,t]. The corresponding loss bound is

    |eta_t-lambda t I|<=K_eta t²,
    K_eta/lambda <= E0 hmax S
          +S(Lip h+rmax hmax)/(2hmin)+1/4+6S/hmin²
       <=14683/432<35.                             (15)

These inequalities explicitly price survival and final rounding. They do not treat R as2n. Set t=2I/(M-4) for M>=8. Since I<=S hmax<=1/4, t<=1. Equations(14)--(15) give R_t<=M and(2). The last inequality in(2) follows by M/(M-4)<=2. Combining(12) and(2) proves(1), with uniformity on the stated compact parameter rectangles.

## 5. Execute the priced, inverse and complexity consequences

For a matching priced lower bound take t=e sqrt(2/lambda), for small enough e that t<=1. Equations(14)--(15) give

    eta_t<=sqrt C e+70e²,
    e²R_t<=sqrt C e+4e²,
    Q(e²)>=V-2sqrt C e-74e².                        (16)

Together with(11), this proves(3) with explicit one-sided error constants. It extends the subcritical exact-tail law to the full certified positive-action regime, without assuming count transitions disappear.

Let R_min(eta) be the least expected resource needed for gap at most eta. K2571's attainment/strict increase and the two-sided estimate(1) imply

    R_min(eta)=C/eta+O(1), eta down to0.             (17)

For example substitute M=C/eta plus/minus a sufficiently large fixed constant in the bounds; the sign of the order-eta² change dominates their fixed error constants. Positive C on compact positive parameter rectangles makes this uniform. This is an additive bounded resource uncertainty, improving the leading relative statement.

There is also an optimizer-resource consequence that does NOT assume Q is differentiable. Every optimal policy at price k has slope -R as a subgradient of the convex Q. Compare the supporting line with Q(k(1+u)) and Q(k(1-u)), u=k^(1/4). Using(3) in the resulting secants gives

    R=sqrt(C/k)+O(k^-1/4).                          (18)

The error is the sum O(k^-1/2*u) from the square-root Taylor remainder and O(1/u) from the O(k) value error. Count ties or mixtures therefore obey the same expected-resource estimate. For any deterministic optimal completed schedule, K2571's2e^-S n<=R<=2n then proves n=Theta(k^-1/2). This is a deterministic optimal-stage statement; a mixed optimum has an expected count and not a fixed pathwise count. No O(1) error for the price-selected resource, smoothness of Q or exact next coefficient is claimed.

## 6. Reproducibility and counterexamples

Bellman verification by a comparison function is standard; [MIT's dynamic-programming notes](https://underactuated-r1.csail.mit.edu/dp.html) describe that general method. Our original-law trial accounting and the uniform remainder bounds are established here, not imported from a continuous-time formula.

The probe verifies the original logarithm, derivative bounds, square completion, explicit slack constants, dual substitution and secant errors. It replays actual rational finite policies at two multipliers and prescribed budgets with Arb interval values, using the rigorous K2602 coefficient brackets and exact original prefix resource. Finite examples consume(2); they do not prove the all-policy barrier. Rational rounding is checked for those concrete schedules and is not silently substituted into the exact-mesh proof.

Contrary controls remove the factor2 trial price, ignore survival, show a negative lower-bound certificate if the K correction is omitted near b=ec, use zero-action controls above critical, and distinguish an O(M^-2) bound from a second coefficient. An abstract two-affine-function tie tests the nondifferentiability boundary; it is not an original-law policy fixture. Neither the lower-bound threshold(10) nor its huge conservative constant is advertised as practical optimality at the small finite consumer budgets. Next-order activation profiles, a genuine M^-2 coefficient with count/rounding effects, the multiplier range beyond4/5 and physical realization remain separate.

[K2602](k2602-continuum-stopping-resource-law-2026-11-06.md), [K2561](k2561-higher-budget-stopping-2026-11-05.md), [K2571](k2571-stopping-resource-price-2026-11-05.md), [probe](../../tests/channel-swings/k2604_second_order_stopping_resource_bound_probe.py), [report](../../lab/process/k2604-second-order-stopping-resource-bound.json).
