---
title: "K2601 Sharp critical stopping resource limit and success stability"
status: active_research
doc_type: exploration
created: "2026-11-06"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: fixed-score critical-multiplier adaptive resource asymptotic and explicit bounds; no exact finite optimizer or physical probability
scripts:
  - tests/channel-swings/k2601_critical_stopping_resource_limit_probe.py
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
result: K2601
carrier: original fresh fair test/use histories with predictable randomized controls and expected trial resource at most M LAYER=toy CHIRALITY=N/A
pairing: unconditional success minus lambda times original leakage, including abort and nonabsorption ON=declared_carrier
real_structure: real scores actions and probabilities with exact rational-log and square-root bounds
grading: finite-policy value, unrestricted supremum, expected resource and leakage budget remain distinct
action_owner: repository-construction -- supplied stopping probability law
target: uniform-over-policies critical resource limit, sharp success stability and finite bounds MAP-TYPE=evaluation
```

# A sharp resource law survives the accumulation of count transitions

## Result and boundary

For each FIXED 0<S<=1/2, put lambda=2/(3+S) and V*=1-lambda S/2. Let F_lambda(M,S) be the supremum of p-lambda C over the entire original adaptive policy class with expected positive-score trial resource R=E N_+<=M (including failed and passed tests, excluding zero-score idles). Then

    V*-F_lambda(M,S)=3lambda S²/(8M)+O(M^-3/2).        (1)

In particular the sharp leading coefficient is 3lambda S²/8. Equal-score zero-action adjacent-count mixtures achieve this coefficient with O(M^-2) error, even though K2587 proves every finite zero-action chord is strictly suboptimal at this multiplier. Finite suboptimality and asymptotic efficiency are compatible.

K2597's fixed-count bifurcations and K2599's positive-price corner do not justify this limit: their count exclusions depend on a positive price that degenerates as count grows. The proof below instead bounds ALL original policies by trial occupation. It also gives an explicit positive finite-resource lower gap, exact feasible upper gaps, and the sharp nearoptimal-success law

    1-p <= (9/(16lambda²))^(1/3) eta^(2/3)+o(eta^(2/3)),
    eta=V*-p+lambda C.                                (2)

No uniform S-to-zero assertion, exact finite optimizer, all-multiplier phase diagram, physical Born law or GU recovery follows. SC-META-53 remains UNCERTAIN; ledger0.263 LT-SM8/LT-GR6b and source/canon truth are unchanged. Independent mathematics only; no external-expert, proof-assistant or novelty certification.

## 1. Reused law and new uniform small-score residual

For clipped controls 0<=a<=b<=s<=S, with b>0, use the original cost

    w(a,b)=log[1+(b-a)²/(2(a+b)(2-a-b))].

At critical lambda the exact unrestricted potential from K2561 is V(s)=1-lambda s/2. Its Bellman residual is

    d=(1+a)V(s)+2lambda w(a,b)-V(s-b).

Write r=a/b in[0,1], q=(1-r)²/[4(1+r)] and x=bq/[1-(1+r)b/2]. Then w=log(1+x), q<=1/4, and log(1+x)>=x-x²/2 gives

    2w >= 2bq+b²[q(1+r)-q²]
                  -b²q²[(1-b)^-2-1].                 (3)

The exact identities/inequalities on the stated rectangle are

    3r/2-1/2+2q=2r²/(1+r)>=r²,
    q(1+r)-q²-(3/16-r/2)
      =r(3r³+12r²-r+6)/[16(1+r)²]>=0,
    (1-b)^-2-1<=6b,  0<=b<=1/2.

The last numerator is b(6b²-11b+4)/(1-b)²>=0; the quadratic decreases to0 at b=1/2. The second is nonnegative since6-r>=5. The worst remaining score is s=S, because d/lambda has the additional nonnegative term rb(S-s)/2. Finally br²-b²r/2=b(r-b/4)²-b³/16. Therefore, UNIFORMLY in all controls and remaining scores,

    d >= lambda b²(3-7b)/16.                         (4)

This bound is useful for small b, not asserted positive throughout the whole half-score interval. K2561's separately proved global bound supplies

    d>=lambda gamma b²/2,
    gamma=78360951/2744000000>0.                      (5)

The global generator proof and its certified constant are reused with unchanged hypotheses: lambda<=2/3<4/5. No fixed-n Taylor argument substitutes for (4).

## 2. An all-policy occupation inequality

K2561's original conditional-expectation telescope has per-trial loss delta=d/2. Clipping excess, abort and nonabsorption terminal losses are nonnegative. For EVERY predictable randomized policy with finite original expected resource,

    eta>=E sum_active delta,
    E sum_active b'=2 E sum_use b'>=2S p,
    E N_+<=R<=M.                                    (6)

Here b' is clipped positive progress and N_+ counts active positive-score trials, including failed/test-pass trials. The factor2 is the fresh fair-use law. The total use-progress is at most S pathwise and equals S on a finite hit; nonhitting paths may add progress. These statements include mixtures, aborts and infinite nonabsorbing histories; no infinite approach to score0 is counted as a hit.

Fix0<epsilon<3/7. Equation(5) gives

    E sum_(b'>epsilon) b' <=4eta/(lambda gamma epsilon).

On b'<=epsilon, (4) yields delta>=lambda(3-7epsilon)b'^2/32. Cauchy--Schwarz on the probability/counting occupation measure, with mass at most M, now proves the EXACT finite inequality

    M eta >= lambda(3-7epsilon)/32
       *[2S p-4eta/(lambda gamma epsilon)]_+².         (7)

No deterministic schedule reduction or unweighted success conditioning is used. If resource is infinite this estimate is vacuous, as it should be.

## 3. Nearoptimal success tends to one

Let lambda'=lambda+h<=4/5, h>0, and define the exact unrestricted support excess

    E_h=V_lambda'(S)-[1-lambda' S/2]>=0.

The old zero-action continuum remains a feasible limiting value, giving the sign. For any policy,

    p-lambda C=(lambda/lambda')(p-lambda' C)
                          +(h/lambda')p
      <=(lambda/lambda')V_lambda'(S)+(h/lambda')p.

Rearranging yields

    1-p <= lambda E_h/h + lambda' eta/h.             (8)

K2561's exact clock makes V differentiable from the right at lambda, with derivative -S/2; hence E_h=o(h). First let eta tend0 at fixed h, then h tend0: every nearoptimal sequence has p tending1. An arbitrary mixture of lossy policies cannot evade this conclusion by carrying its resource in a rare branch.

## 4. Sharp resource limit and constructive approach

The zero-action equal-score n-stage schedule has p=1, R=2n and C=2n w0(S/n), w0(b)=log[(4-b)/(4-2b)]. Direct expansion of the ACTUAL logarithm gives

    w0(b)=b/4+3b²/32+7b³/192+O(b^4),
    eta_n=3lambda S²/(16n)+O(n^-2).                  (9)

For any real M>=2, mix counts n=floor(M/2), n+1 with weight theta=[2(n+1)-M]/2. Its expected resource is EXACTLY M. Consequently the frontier gap is at most C*/M+O(M^-2), C*=3lambda S²/8, and tends0.

For the lower bound choose an arbitrarily nearoptimal policy at each M (or use the existing attainment theorem where applicable). Its eta tends0 and p tends1 by (8). Hold epsilon fixed in(7), take liminf M eta, then let epsilon tend0. This gives liminf>=C*. The feasible mixtures give limsup<=C*. Taking approximate optima within o(1/M) justifies the same limit for the supremum itself; no optimizer existence is needed.

This settles the uniform large-count LEADING resource question at critical lambda for every fixed S. It does not resolve the individual finite positive-action optimizers or a simultaneous lambda−lambda_* scaling.

## 5. Execute the sharp success-stability successor

For sufficiently small h>0, theta'=1/(lambda+h)>3/2. Let u=3/2-x be the K2561 initial clock value and put d0=1/lambda-1/(lambda+h). The exact clock relation is

    d0=integral_0^x [2q(3/2-y)]^-1 dy,
    q(3/2-y)=1/2-y²/8-y³/32+O(y^4).

Thus d0=x+x³/12+O(x^4), E_h=(lambda+h)(d0-x), and

    E_h=h³/(12lambda^5)+O(h^4).                      (10)

Using h=(6lambda^5 eta)^(1/3) in (8) proves (2), uniformly over policies through the deterministic support bound. The remainder depends on fixed S, not on the policy.

The constant and exponent are sharp. The neighboring continuum contact at lambda+h has

    1-p_h=h²/(4lambda^4)+O(h³),
    eta_h=h E'_h-E_h=h³/(6lambda^5)+O(h^4).

Eliminating h gives equality in (2) to leading order. Those contacts are supremal, not original infinite-hit policies. K2561 supplies original finite schedules approximating each contact. For a sequence h_j tending0, choose the finite approximation errors in success and cost to be o(h_j³). This diagonal construction preserves the displayed asymptotics. It makes NO uniform resource claim and does not say these stability extremizers also optimize F_lambda(M).

For the resource remainder, (2) implies p>=1-O(eta^(2/3)). Choose epsilon=sqrt(eta) in (7) for small positive eta. Then

    M eta >= C*-O(sqrt(eta)).

The feasible bound eta=O(1/M), applied to nearoptimal policies with approximation error smaller than M^-2, gives the lower gap C*/M-O(M^-3/2). Equation(9) supplies upper C*/M+O(M^-2), proving (1). This is a proved error order, not a claim that the M^-3/2 coefficient is sharp.

## 6. An explicit nonasymptotic bound and finite consumers

The preceding limiting theorem has an executable finite counterpart. Choose0<h with lambda'=lambda+h<=2/3 and0<epsilon<3/7. Then d0<=S/2<=1/4. The exact rationalization

    1/2-q(3/2-y)=y²/[4-y+2sqrt(4-2y)]<=y²/6

and x<=d0 give

    d0-x <= x³/[9(1-d0²/3)] <= d0³/8,
    E_h <= h³/(8lambda^5).                            (11)

Define rational quantities

    A=h²/(8lambda^4), B=2S(1-A)>0,
    L=2S(lambda+h)/h+4/(lambda gamma epsilon),
    c=lambda(3-7epsilon)/32.

Combining(8),(11) and(7) gives eta>=c(B-L eta)_+²/M. If eta>=B/L the following bound holds automatically; otherwise solve the quadratic on[0,B/L]. Its stable smaller root is

    eta >= 2cB²/[M+2cBL+sqrt(M²+4cBLM)].              (12)

Thus (12) is a universal lower gap, and the actual adjacent-count mixture from(9) supplies a feasible upper gap. The bound is conservative and is NOT the exact finite optimizer.

The probe executes scores1/2 and1/4, h=epsilon=1/100 and resources1000,1001,10000. It checks the multiplier domain, positivity and exact resource for every consumer; rational logarithm and square-root intervals enclose the lower and upper gaps. Resource1001 exercises an actual nontrivial mixture. At score1/2 the sharp coefficient is3/56; at score1/4 it is3/208. Full rational enclosures and display values are saved in the report, without numerical optimization.

A contrary original-law consumer uses score1/2, lambda4/7, a two-stage schedule with first action1/1000 and scores1/4,1/4, and the zero-action three-stage schedule. Mixing them to expected resource exactly5 strictly beats the old zero-action two/three chord by rational log bounds. Substituting nominal resource4 for the positive-action schedule's actual4/(1+a) fails the same resource check. This exercises finite strict suboptimality and the original survival-weighted resource law rather than testing a constant inequality.

For log z, the probe uses y=(z-1)/(z+1) and48 atanh terms, with tail bound 2|y|^97/[97(1-y²)]. Integer square root yields adjacent rational endpoints with denominator10^50. Lower-gap evaluation uses the upper square-root endpoint, so its inequality direction is conservative. These explicit bounds may be refined by different admissible h,epsilon without changing the theorem.

## Evidence and next comparison

The exact probe checks the residual factors, original-log and clock expansions, fair-trial coefficient, stable quadratic identity and six independent rational finite consumers. The universal telescope and gamma certificate are reused from K2561. The new occupation restriction, limiting argument, stability sharpness and remainder are written analytic proofs; pass counts do not certify them.

Compare the simultaneous nearcritical multiplier/resource limit or an actual finite optimizer with physical source/readout construction. The critical multiplier resource constant, its convergence order and sharp success stability are now established at the stated conditional scope. Do not requeue them as mere fixed-count conjectures. General multiplier topology, physically priced implementation and native GU positivity remain separate.

[K2561](k2561-higher-budget-stopping-2026-11-05.md), [K2587](k2587-countwise-stopping-support-2026-11-05.md), [K2597](k2597-stopping-threshold-bifurcation-2026-11-06.md), [K2599](k2599-joint-stopping-corner-2026-11-06.md), [probe](../../tests/channel-swings/k2601_critical_stopping_resource_limit_probe.py), [report](../../lab/process/k2601-critical-stopping-resource-limit.json).
