---
title: "K2565 A practical whole-policy certificate at an intermediate stopping multiplier"
status: active_research
doc_type: exploration
created: "2026-11-05"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: certified global dual and budget brackets at multiplier 19/10 for the supplied stopping law; no exact optimizer or native GU inference
scripts:
  - tests/channel-swings/k2565_bellman_supersolution_probe.py
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
result: K2565
carrier: original predictable fresh fair test/use stopping histories, including failure, abort and nonabsorption LAYER=toy CHIRALITY=N/A
pairing: unconditional success probability and expected original leakage cost ON=declared_carrier
real_structure: real probabilities and exact rational polynomial certificates
grading: clipped original trials, completed stages and finite witnesses remain distinct
action_owner: repository-construction -- supplied fresh fair stopping law
target: universal original-law Bellman support, certified intermediate bracket and occupation bounds MAP-TYPE=evaluation
```

# K2565 Certify the intermediate value without enumerating hybrids

## Result, comparison and scope

At multiplier lambda=19/10, the full original adaptive dual value at score S=1/2 satisfies

    0.711079567311 < V_lambda(1/2) <= 0.711325.

The certified bracket has width less than 0.000246, already smaller than the 1/2500 separation that motivated K2563's expensive global hybrid grid. A rational quadratic Bellman supersolution supplies the upper bound over ALL original adaptive policies. The initial lower bound reuses K2561's concrete 21-stage policy. An executed structural discriminator then supplies an improved 41-stage rational policy, certified with its original survival prefixes. No hybrid enumeration, atom-count truncation or sampled-optimizer certificate enters the upper proof. The stronger occupation bound below slightly lowers the displayed upper endpoint and supplies a budget ceiling.

K2563's universal finite-atom approximation remains valid and useful for other accuracy or multiplier questions. This result removes its proposed huge grid as a prerequisite for resolving this particular precision target. It does not determine the exact intermediate optimum, its attaining policy, uniqueness, the optimal number of atoms or the whole frontier. The fresh routing and leakage law are supplied mathematical assumptions. SC-META-53 remains UNCERTAIN; source polarities, ledger0.263, native action/quotient/domain judgments and physical credit remain unchanged. No novelty or physical implementation claim is made.

## 1. The original Bellman residual

For 0<=a<=b<=s<=1/2 define

    w(a,b)=log(1+(b-a)^2/[2(a+b)(2-a-b)]),
    U(s)=1-c*s+d*s^2,
    c=3221/5000, d=1337/10000, lambda=19/10.

At a=b=0 set w=0. The desired residual is

    R(a,b,s)=(1+a)U(s)+2lambda*w(a,b)-U(s-b).

Here U(0)=1, U decreases on[0,1/2], and U(s)>=U(1/2)=28453/40000>0. We prove the stronger inequality

    R(a,b,s)>=gamma*b,
    gamma=268141/31457280000>0.                       (1)

This is a per-stage mathematical inequality. It must still be transferred through the actual trial law, including failed paths and terminal losses.

## 2. A small exact polynomial certificate over the whole domain

For x>=0,

    log(1+x)>=2x/(2+x),
    d/dx[log(1+x)-2x/(2+x)]
        =x^2/[(1+x)(2+x)^2]>=0.

Both functions vanish at zero, proving the inequality. For b>0 put r=a/b and

    D=8(1+r)-b(3+10r+3r^2)
      =4(1+r)[2-b(1+r)]+b(1-r)^2.

Since 0<=r<=1 and b<=1/2, 2-b(1+r)>=1 and hence D>0. Also
16-D=8(1-r)+b(3+10r+3r^2)>=0. Substitution into the logarithm gives

    2w(a,b)/b >= 4(1-r)^2/D.

The quadratic identity therefore yields

    R/b >= rU(s)-c+2ds-db+(38/5)(1-r)^2/D = P/D,
    P=D[rU(s)-c+2ds-db]+(38/5)(1-r)^2.                (2)

Cover the full triangular domain by

    b=y/2, s=b+(1/2-b)z, 0<=r,y,z<=1.

This is surjective onto 0<=b<=s<=1/2; at b=1/2 every z represents the same allowed s. The polynomial P in(r,y,z) has tensor degree(3,3,2). Its exact power coefficients are converted to tensor Bernstein coefficients. An independent inverse expansion reconstructs the power polynomial. The root cube has negative coefficients, so it is insufficient by itself; exact midpoint de Casteljau subdivision cycles through axes r,y,z, splitting only cubes whose coefficient minimum is not strictly positive.

All 120 terminal cubes have strictly positive coefficients. Maximum subdivision depth is16; their minimum coefficient is

    m=268141/1966080000.

The polynomial lies above the minimum Bernstein coefficient on each cube. The recursive half-cube cover is complete; the probe also checks prefix-free leaf paths, total dyadic volume1, and verifies affine subdivision against independent power substitution in each axis. Its canonical sorted leaf-coefficient digest is
`720759afa8aacb2600100bbf3e438b0e315d757b559f7ba1a02e39d4ebc37545`.
Thus P>=m throughout the closed cube, and D<=16 proves(1). The b=0 case of the original residual is zero and is handled directly; no division by zero is made. The b=0 polynomial limit is nevertheless certified and protects the small-stage boundary.

The probe regenerates every coefficient and leaf from the displayed polynomial with exact rational arithmetic. The coefficient minimum and digest are reproducibility results, not assumptions that substitute for the computation.

## 3. Transfer to every original adaptive policy

Use K2483's original fresh fair test/use law and K2557's exact clipping account. A reached trial chooses predictable a,b in[0,1]. A fresh fair use advances the score; a test fails with probability a and otherwise leaves the score unchanged. Every active trial incurs the original w, including a failing trial. For a>=b its original cost is zero. Put b'=min(b,s), a'=min(a,b').

The conditional-expectation loss is

    delta=U(s)-[(1-a)U(s)+U(s-b')]/2+lambda*w(a,b)
         =R(a',b',s)/2+U(s)(a-a')/2
                         +lambda[w(a,b)-w(a',b')].   (3)

All three terms are nonnegative. If a>b', the clipped cost is zero. Otherwise a'=a and the original logarithmic cost increases with b above a, giving w(a,b)>=w(a',b'). This is the unchanged clipping argument, not a new favorable policy or a conditional-on-success cost. Equation(1) gives delta>=gamma*b'/2.

At finite horizon n, iterate conditional expectation with hit potential1, failure potential0, current live potential U(s_n) and abort loss U(s_abort). Then let n tend to infinity. Nonnegative costs and slacks admit monotone convergence; U is bounded and continuous, s_n decreases to s_infinity on nonabsorption, and bounded convergence treats the remaining live potential. For every policy with finite expected cost C and eventual finite-hit probability p,

    eta:=U(S)-p+lambda*C
        =E sum_active delta
          +E[1_abort U(s_abort)]
          +E[1_nonabsorption U(s_infinity)]>=0.       (4)

Private randomization and unbounded trial counts are covered. Infinite expected cost cannot improve a positive-multiplier dual objective. An infinite path approaching the target without a finite hit remains nonabsorbing and carries U(0)=1, not zero. Endless idling also retains its positive terminal potential. Thus the conclusion is about the full original law, not just finite deterministic schedules.

## 4. Executed successor: occupation and constrained-budget bounds

The strict residual is useful beyond certifying the displayed upper endpoint. Predictability and the independent fair use bit give, by Tonelli,

    E sum_active b'=2 E sum_use b' >=2S*p.

The sum of clipped use increments equals S on every hit path and is nonnegative on all other paths. This argument uses neither finite expected trial count nor a fixed-stage representation. Combining it with(3)--(4) gives

    U(S)-p+lambda*C >= gamma*S*p,
    (1+gamma*S)p-lambda*C <=U(S).                    (5)

Consequently, at every budget B>=0,

    F(B)<=min(1,[U(S)+lambda*B]/[1+gamma*S]),          (6)

and since C>=0,

    V_lambda(S)<=U(S)/[1+gamma*S].                    (7)

For(7), write (1+gamma*S)(p-lambda*C) as the left side of(5) minus gamma*S*lambda*C. This sharpened upper is still above the exact finite witness. Equation(6) also supplies a certified bracket at that witness's EXACT logarithmic budget; it does not replace the budget by a rounded decimal.

A separate witness-relative diagnostic follows from the terminal terms. If a policy achieves dual at least L-epsilon, where L=0.711020048691 and epsilon>=0, then eta<=U(S)-L+epsilon. At S=1/2,

    Pr(abort or nonabsorption) <=[U(S)-L+epsilon]/U(S),
    E sum_active(a-a') <=2[U(S)-L+epsilon]/U(S),
    E sum_active(w-w') <=[U(S)-L+epsilon]/lambda.      (8)

At epsilon=0 these are respectively less than43/100000,86/100000 and161/10^6. The first concerns abort/nonabsorption, not ordinary rejection failure. The bounds measure loss relative to a certified witness and supersolution, not exact optimizer regret. A bound proportional to total score does NOT supply a stage-count, atom-count or uniqueness theorem.

## 5. Actual lower policy and exact-budget consumer

Reuse the K2561 rational controls: first(a,b)=(349/2000,3/10), followed by20 stages(21/5000,1/100). Their scores sum to1/2. For each stage update P_i=P_(i-1)/(1+a_i), then add2P_i*w_i to the unconditional cost. This explicit loop replays the original prefix accounting and verifies

    0.711020048691 < p_h-(19/10)B_h <0.711020048692,
    0.037866038451 < B_h <0.037866038452.

Here p_h is the exact product of rational survival factors and B_h is the exact logarithmic sum. At that exact budget,

    p_h <= F(B_h) <=[U(1/2)+(19/10)B_h]/[1+gamma/2],

with gap less than0.000305. Likewise the whole-policy dual gap between this finite witness and(7) is less than0.000305. Rational atanh-series logarithm bounds with explicit geometric remainders certify these statements. This reuses the lower construction and introduces the all-policy upper bound; it does not claim a new finite witness or exact attainment.

## 6. Executed structural discriminator and improved finite witness

The global certificate released a useful structural comparison, not a reason to end at its first bracket. For this reconnaissance alone, evaluate the exact continuum formula numerically. Write theta=10/19 and

    tau(u)=log(sqrt(1+2u)-1)-3log(3-sqrt(1+2u)),
    C_t(1)=(19/10)*tau^-1(tau(theta)-t).

This is the optimized RESTRICTED continuum tail from K2495/K2563, not a full original-law optimum. For one first atom the objective is

    [C_(1/2-b)(1)-2lambda*w(a,b)]/(1+a).

A floating-point scout finds approximately b=0.30204153,a=0.1758584134, value0.7110991783128885. It then tests two consecutive atoms followed by one optimized continuum tail, with no continuum block before or between the atoms, using b1=x/2,b2=(1/2-b1)y,a1=r1*b1,a2=r2*b2 and the actual nested prefix-weighted objective. Six deterministic Nelder--Mead starts all converge to a zero-size extra atom, agreeing with the one-atom value within floating-point precision. This is NONEXHAUSTIVE: it neither excludes another local maximum nor proves one-atom/global optimality. The optional probe `--scout` reproduces the starts, original objective, clock inversion and optimizer tolerances; it is kept outside exact pass counts. No significance is assigned to its final digits.

The useful accepted consequence is an explicit FINITE construction suggested by that tail shape. Take

    main: (a,b)=(8793/50000,151/500),
    tail i=0,...,39:
      b_i=99/20000,
      a_i=b_i*[221/500-(23/500)*(2i+1)/80].

All 41 controls are rational and strictly satisfy0<a<b. Their score sum is exactly1/2. The tail ratios strictly decrease, approximating the optimized tail shape without claiming equality to it. The same explicit original-prefix loop and rigorous logarithm intervals prove

    0.711079567311 < p_new-(19/10)B_new <0.711079567312.

The witness improves K2561's prior dual by more than1/20000. Every logarithm interval is rounded OUTWARD to a denominator10^24 before exact prefix propagation, keeping arithmetic manageable; this rounding widens the interval and grants no accuracy assumption. The policy has finitely many stages and almost-sure finite absorption, so no continuum-limit attainment is invoked.

Combining the new lower witness with the already-proved upper gives a global dual bracket of width less than0.000246; using(7) gives width less than0.000243. At the NEW witness's exact logarithmic budget,

    p_new <= F(B_new)
           <=[U(1/2)+(19/10)B_new]/[1+gamma/2],

also with gap less than0.000243. These compare each finite policy to the unrestricted adaptive optimum at its own EXACT budget, never a rounded decimal budget. The older witness and its numerical diagnostics above remain valid as reused evidence. No two-atom improvement was found by the scout, and no class exclusion or global one-atom theorem is inferred from that failure.

## 7. Strong contrary controls and what remains open

A sampled linear-program scout initially proposed c=1289/2000,d=671/5000. That candidate is FALSE. At the b=s=0 limiting corner and r=2/5 its normalized residual is exactly-3/14000; an actual nonzero stage b=s=10^-6,a=(2/5)b has rigorously negative residual. Finite-grid feasibility tolerance concealed that corner. It is retained as a changed-coefficient negative control, never used as a certificate.

Reducing the accepted curvature coefficient to13/100 also fails a genuine finite original-law stage at s=1/2,b=1/4,a=1/7, certified with a rational logarithm upper bound. Further controls reject using log(1+x)<=x as a lower bound, deleting terminal potential, dropping survival prefixes, treating the unsplit Bernstein cube as positive, or declaring a value below the actual witness optimal. These change the mathematics being tested rather than only mutating report flags.

The next substantial question is structural: whether a one-atom/optimized-tail family is globally optimal in this intermediate region, or whether an additional finite atom improves it. The present global bracket can validate such candidates and bound how much improvement remains; it proves neither horn. A certified sharper supersolution or a useful multiplier family can improve the bracket without resurrecting the huge literal hybrid grid. Physical apparatus, preparation/reset and a native GU probability law remain separate inputs.

## Verification

The rational whole-cube sign certificate, independent inverse-basis and affine-subdivision checks, actual-log counterfixtures and original prefix replay are exact computation. The logarithmic inequality, conditional-expectation/tail argument and occupation theorem are universal proofs given above. The new 41-stage rational witness is an independently certified finite construction; its optional two-atom scout is numerical evidence only. Finite supporting checks do not replace those arguments. K2483 and K2557 are reused at their unchanged original-law hypotheses; K2561 supplies the unchanged lower witness. Independent specialist and integrated hostile review remain necessary for acceptance. No external-expert, proof-assistant, remote-CI, novelty or physical certification is claimed.

[Exact probe](../../tests/channel-swings/k2565_bellman_supersolution_probe.py), [report](../../lab/process/k2565-bellman-supersolution.json), [K2563 global hybrid approximation](k2563-global-hybrid-reduction-2026-11-05.md), [K2561 finite witness](k2561-higher-budget-stopping-2026-11-05.md), [K2483 original Bellman theorem](k2483-adaptive-stopping-bellman-2026-11-01.md), [K2557 clipping and tail account](k2557-parametric-stopping-support-2026-11-05.md).
