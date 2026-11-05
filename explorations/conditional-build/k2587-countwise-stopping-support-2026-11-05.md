---
title: "K2587 Sharp countwise stopping thresholds"
status: active_research
doc_type: exploration
created: "2026-11-05"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: sharp thresholds for each zero-action budget chord and eventual tail; positive-action optimal values remain open
scripts:
  - tests/channel-swings/k2587_countwise_stopping_support_probe.py
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
result: K2587
carrier: original fair stopping law with finite completed schedules and initial mixtures LAYER=toy CHIRALITY=N/A
pairing: unconditional expected success, leakage and positive-trial functional ON=declared_carrier
real_structure: real controls and multiplier; probability laws and private randomization
grading: stages, expected positive trials and pathwise trial counts kept distinct
action_owner: repository-construction -- stated conditional model
target: sharp countwise resource frontier and eventual-tail onset MAP-TYPE=evaluation
```

# Close the sufficient-versus-failure gap for every chord

## Result and scope

For every total score 0<S<=1/2 and integer n>=1, define H_n=n log[(4-S/n)/(4-2S/n)], Delta_n=H_n-H_(n+1), T_n=(n+1)H_n-nH_(n+1), and

    c(b)=2(3-2b)/[(2-b)(4-b)],
    lambda_n(S)=1/[2c(S/n)+2T_n].                 (1)

The zero-action equal-n/equal-(n+1) chord is the EXACT optimum of the original expected-resource stopping problem at every M in [2n,2n+2] when 0<lambda<=lambda_n. If lambda>lambda_n, an actual positive-action mixture strictly improves it at EVERY M in [2n,2n+2). The right endpoint belongs to the next chord and may survive longer. Thus (1) is sharp for each half-open chord, including equality. This closes K2585's sufficient B_n versus first-action failure gap, without computing the replacement positive-action optimum.

The thresholds strictly increase to Lstar(S)=2/(3+S). Consequently an eventual exact zero-action tail exists precisely for 0<lambda<Lstar. At or above Lstar every finite half-open chord is beaten. This is independent mathematics, not a native GU probability or physical-positivity result. SC-META-53 remains UNCERTAIN; source, ledger0.263 and canon are unchanged.

## 1. An all-action majorant, without an action-count assumption

Use K2569's completed schedules: b_i>0, 0<=a_i<=b_i, sum b_i=S, P_i=product_(j<=i)(1+a_j)^-1, p=P_m, C=2 sum P_i w_i, R=2 sum P_i, with

    w(a,b)=log[1+(b-a)^2/(2(a+b)(2-a-b))].

Let A=sum a_i. All costs w_i and prices k are nonnegative, P_i>=p, and product(1+a_i)>=1+A. Hence

    J=p-lambda C-kR <= p[1-2lambda sum w_i-2km]. (2)

K2581's joint convexity gives sum w_i>=m w(A/m,S/m). K2509's exact fixed-b curvature identity gives w_aa>=2/D, where D=2u(2-u), u=a+b<=2b and u<=1. Thus w_aa>=1/(4b). Integrating from a=0 twice at fixed b yields

    m w(A/m,S/m)>=H_m-c(S/m)A+A^2/(8S).

Put J_m=1-2lambda H_m-2km. Equation(2) gives

    J<=p N_m(A),
    N_m(A)=J_m+2lambda c(S/m)A-lambda A^2/(4S). (3)

If N_m<=0, this schedule cannot beat a positive candidate. Otherwise p<=1/(1+A), so J<=N_m/(1+A). This sign split is essential; multiplying a negative numerator by an upper bound for p would reverse the inference. All positive actions, in any order, are covered. No premise that at most one action is positive is needed.

## 2. Global support at the count-change price

Set k=k_n=lambda Delta_n. Strict convexity of H(t)=t w0(S/t) implies zero-action counts n,n+1 tie and are the unique maximizing counts, with

    Q0=1-2lambda T_n>0.

Under (1), Q0>=2lambda c_n, c_n=c(S/n). For m>=n, c_m<=c_n: for n>=2 all arguments lie in [0,1/4], where c increases; for n=1 use the proved c(S/m)<=c(S) from K2581. Therefore

    N_m-(1+A)Q0 <= J_m-Q0-lambda A^2/(4S)<=0,

strict for A>0.

For m<n define d=n-m>0 and

    g_m=H_m-H_n-d Delta_n=(Q0-J_m)/(2lambda).

The convergent positive series H(t)=sum_(r>=1) S^r(2^-r-4^-r)/(r t^(r-1)) has a constant term S/4. Each remaining t^-(r-1) is convex, so every extrapolated chord gap at m<n is positive. Keeping just r=2 yields

    g_m >= (3S^2/32) d(d+1)/[mn(n+1)].           (4)

Also c'(b)<=1/16 throughout [0,1/2]. Integrating this ONE-SIDED upper bound gives

    c_m-c_n<=S d/(16mn)=D_m.                    (5)

It does not assert c is increasing on the whole interval. From (3),

    N_m-(1+A)Q0
       <= -2lambda g_m+2lambda D_m A-lambda A^2/(4S)
       <= -2lambda g_m+4lambda S D_m^2 <0.       (6)

The final strict inequality follows from (4): the ratio of its lower bound to 2S D_m^2 is 12mn(d+1)/[S d(n+1)]>1. Indeed m>=1, n>=2 and S<=1/2 make it exceed 24n/(n+1)>1. Thus ALL smaller-count schedules are excluded, not merely nearby perturbations.

For A=0, strict Jensen makes the equal-score schedule uniquely optimal at a given count, and only n,n+1 tie. Abort is below Q0. K2569's reduction of arbitrary adaptive policies to completed-schedule mixtures raises success-minus-leakage and lowers expected resource, so the support holds for the original adaptive class. Infinite mixtures preserve it by integration; no finite-attainment hypothesis is needed for this upper bound. We conclude Q(k_n)=Q0 and the exact constrained value is

    F(lambda,M,S)=1-2lambda[(1-theta)H_n+theta H_(n+1)],
    theta=(M-2n)/2.                             (7)

## 3. Necessity and actual feasible improvements

Keep equal scores b=S/n in an n-stage schedule, place a single action epsilon>0 in its FIRST stage and all others zero. Its survival is p=1/(1+epsilon), R=2n/(1+epsilon), and C=2[w(epsilon,S/n)+(n-1)w0(S/n)]/(1+epsilon). At the old price k_n,

    dJ/depsilon at0 =2lambda c_n-Q0
                    =lambda/lambda_n-1.         (8)

For lambda>lambda_n, sufficiently small epsilon gives strictly positive support excess. Mix that schedule with the unaltered zero-action (n+1)-stage schedule, using

    q=(2n+2-M)/(2n+2-2n/(1+epsilon)).             (9)

For every M in [2n,2n+2), q is positive and at most1, the expected resource is EXACTLY M, and gain over (7) is q times the support excess. This proves necessity, including M=2n. At M=2n+2, q=0; no false endpoint exclusion follows. Equality lambda=lambda_n is valid by the GLOBAL proof, not by a zero first derivative.

## 4. Execute the eventual frontier and its sharp onset

K2581 already proves lambda_n strictly increases, with the n=1 to2 endpoint handled by c(S/2)<=c(S). Since c(0)=3/4 and T_n tends to S/4, its limit is Lstar=2/(3+S). Hence for lambda<Lstar the EXACT onset count for an entire even-start tail is

    Nstar=min{n>=1:lambda<=lambda_n};             (10)

(7) holds for every M>=2Nstar. If Nstar>1, every budget in [2Nstar-2,2Nstar) strictly beats its old chord. More generally each earlier half-open chord fails. For lambda>=Lstar all finite lambda_n are smaller, so no finite eventual zero-action tail exists. This does not compute the optimal positive-action value or prove that the unrestricted continuum value changes at Lstar.

Expanding the convergent series and rational c gives

    H_n=S/4+3S^2/(32n)+7S^3/(192n^2)+O(n^-3),
    T_n=S/4+3S^2/(16n)+O(n^-2),
    c(S/n)=3/4+S/(16n)+O(n^-2),
    Lstar-lambda_n=Lstar^2 S(1+3S)/(8n)+O(n^-2).

For fixed S>0,

    Nstar(lambda) ~ Lstar^2 S(1+3S)/[8(Lstar-lambda)]. (11)

Unlike K2585's Ncert asymptotic, this is the sharp even-start zero-action onset count. The unrestricted value V=1-lambda S/2 and its continuum saturation boundary were ALREADY proved in K2561; this is reused evidence, not a new result. Equations(7)–(11) add the sharp FINITE-resource onset and rate of approaching it. No attainment by a finite schedule is implied.

## 5. Concrete consumers and price intervals

The probe uses rational atanh-series logarithm bounds, not a floating optimizer, to identify Nstar at S=1/2 for lambda=11/20,14/25 and57/100. At11/20 onset3 agrees with the old certificate. At14/25 the sharp onset5 improves the old sufficient onset8: all budgets>=10 are solved, instead of only>=16. The57/100 example has onset36 and lies ABOVE its limiting certificate84/149, demonstrating a genuinely enlarged regime. It evaluates an exact odd-budget optimal mixture at each onset and an actual resource-restored positive-action policy just below that onset. A quarter-score example checks that the theorem is not restricted to S=1/2.

At any count n for which lambda<=lambda_(n-1) (n>=2), BOTH neighboring count-change supports k_n and k_(n-1) are globally exact. The equal-n schedule is therefore globally optimal for every k in the closed interval between them: any competing policy's priced-value difference is affine in k and nonpositive at both endpoints. Adjacent counts tie at endpoints. This executes an entire positive-price interval, not just isolated support points. Counts beyond Nstar meet this condition. The probe executes the count6 interval at S=1/2,lambda14/25: it chooses an exact rational interior price, evaluates the original12-expected-trial policy and certifies strict separation from both neighboring counts. The unresolved transition price interval at Nstar is kept open rather than filled by interpolation with an uncertified endpoint.

## Verification and remaining work

Exact probes check the derivative and curvature identities, count-gap algebra, one-sided slope bound, threshold/asymptotic coefficients, exact original-law policies, resource restoration and rational inequality consumers. Written convexity/series/adaptive-reduction arguments prove the all-policy theorem; finite tests do not replace them. Adverse controls change survival weights, fair-trial charges, mixing weights, sharp-threshold denominators and endpoint interpretation. The positive-action optimizer when lambda>lambda_n remains open. Physical probability, apparatus/reset costs and native GU bridges remain separate.

[K2581](k2581-score-sensitive-tail-transition-2026-11-05.md), [K2583](k2583-complete-stopping-resource-frontier-2026-11-05.md), [K2585](k2585-eventual-stopping-tail-2026-11-05.md), [K2561](k2561-higher-budget-stopping-2026-11-05.md), [K2569](k2569-stopping-maximizing-sequences-2026-11-05.md), [K2509](k2509-stopping-atom-certificate-2026-11-02.md), [probe](../../tests/channel-swings/k2587_countwise_stopping_support_probe.py), [report](../../lab/process/k2587-countwise-stopping-support.json).

Independent field specialists reviewed the concrete constructions and a distinct integrated hostile reviewer returned no remaining findings. Final exact probes and affected native checks passed. Universal distributional and all-policy proofs are distinct from finite identities, consumers and reporting checks. No external-expert, proof-assistant, remote-CI or physical certification.
