---
title: "K2599 Joint score-multiplier unfolding and exact second activation"
status: active_research
doc_type: exploration
created: "2026-11-06"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: local joint corner and explicit score49/100 finite consumers; no uniform count limit or physical probability
scripts:
  - tests/channel-swings/k2599_joint_stopping_corner_probe.py
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
result: K2599
carrier: finite completed stopping schedules with total score0<S<=1/2 and their integrable mixtures LAYER=toy CHIRALITY=N/A
pairing: original-law success minus leakage at fixed expected resource ON=declared_carrier
real_structure: real scores actions prices and exact rational-log enclosures
grading: two action activations, fixed-budget value and moving endpoint are distinct
action_owner: repository-construction -- independent scalar stopping model
target: joint corner topology and globally supported finite consumers MAP-TYPE=evaluation
```

# The half-score corner contains a second activation wedge

## Result and inherited scope

K2597 settles every fixed finite-count local transition and the half-score count-one corner. Those pointwise theorems do not justify a joint limit in S and lambda. Here there is one UNIFORM local neighborhood of S=1/2, lambda=lambda1(1/2) near the one/two-stage crossing price k*, in which the full policy class reduces to competing one/two-stage supports. An exact second-activation curve lambda_A(S)>lambda1(S) for S<1/2 separates a single-active region from a both-active region. Its gap is linear in1/2-S. A constrained positive-part normal form resolves both sides uniformly, and the new second boundary is itself C1 but not C2 in the fixed-budget optimal value.

The moving resource endpoint has a joint two-parameter boundary layer, with matched value and slope and exactly zero gain at budget4. Separately, an explicit rectangle at S=49/100 proves global support and certifies ACTUAL budget3 mixtures on opposite sides of the second activation, at lambda=.5390 and .5391, to widths below1e-50. These finite consumers do not assume the unspecified radius of the local theorem.

This is independent mathematics. The source does not supply this stochastic law or its physical implementation. SC-META-53 remains UNCERTAIN; LT-SM8 and LT-GR6b remain open. Source, ledger0.263 and canon do not change. No novelty, external expert, proof-assistant or physical-probability certification is asserted.

## 1. Original law and a uniform two-support reduction

Reuse the completed schedules b_i>0,0<=a_i<=b_i,sum b_i=S,

    P_i=product_(j<=i)(1+a_j)^-1, p=P_m,
    C=2 sum P_i w(a_i,b_i), R=2 sum P_i,
    w(a,b)=log[1+(b-a)^2/(2(a+b)(2-a-b))].

The criterion is p-lambda C, with expected R<=M; its price support is J=p-lambda C-kR. K2569's adaptive reduction and mixtures remain unchanged. Define

    w0(b)=w(0,b), H1=w0(S), H2=2w0(S/2),
    Delta=H1-H2, T=2H1-H2,
    c(b)=2(3-2b)/[(2-b)(4-b)],
    lambda1(S)=1/[2(T+c(S))], k*=lambda1(1/2)Delta(1/2).

The corner has k*>0. On k>=k*/2, R>=m and J<=1-km exclude all sufficiently large m uniformly. The remaining finite charged-zero compact simplexes retain a strict gap outside neighborhoods of the two zero-action equal-score maximizers identified by K2587. A zero-score stage is charged during compactification; removing it strictly improves positive-price value. Continuity in S,lambda,k preserves these gaps. The local score Hessian is positive and suffix-action derivative strictly unfavorable, so one common neighborhood in (S,lambda,k) admits

    Q=max(Q1,Q2),
    Qi=max_(a>=0)[1-2lambda gi(a,S)-2ik]/(1+a),
    g1=w(a,S),
    g2=min_b[w(a,b)+w0(S-b)].                         (1)

The score minimizer near b=S/2 is unique analytic and the suffix action is zero. Domains retain0<=a<=b<=S; local minimizers are away from non-action boundaries. Put hi(S)=partial_a²gi(0,S)>0. At half score,

    h1=1312/441, h2=171736/24255.                    (2)

The second is the actual score-Hessian Schur complement, not the fixed-score action Hessian. Uniformity here is near this fixed positive-price corner; it does not cover n→infinity or all S.

## 2. Exact second-activation curve

Let c1=c(S),c2=c(S/2). Their exact gap is

    d(S)=c1-c2=2S(1-2S)/[(2-S)(4-S)(8-S)].           (3)

For S<1/2, strict action convexity gives a unique aA in(0,S) with

    partial_a g1(aA,S)=-c2.

The derivative begins at-c1<-c2 and reaches0 at a=S. Define

    lambda_A(S)=1/{2[2g1(aA,S)-H2+(1+2aA)c2]},
    QA=2lambda_A c2,
    kA=[1-2lambda_A(H2+c2)]/4.                       (4)

The denominator is positive near the corner. Substitution verifies count-one stationarity, tie with zero-two, and zero count-two first-action derivative. Locally both schedules are zero-action for lambda<=lambda1; only count one acts for lambda1<lambda<lambda_A; both first actions are positive for lambda>lambda_A. The two curves meet at S=1/2. Local uniqueness and the direction of the activation are also established by section4.

For epsilon=1/2-S and lambda*=lambda1(1/2),

    d=(16/315)epsilon+O(epsilon²),
    aA=d/h1(S)+O(d²),
    lambda_A-lambda1=2lambda1² d+O(d²)
                   =(32lambda*²/315)epsilon+O(epsilon²). (5)

This nonzero wedge is the missing link between fixed-score and half-score cases, not a repetition of either slice.

## 3. Uniform constrained normal form and fixed budgets

Set delta=lambda-lambda1(S), r=|delta|+epsilon, gamma=16/315, and let hi without argument denote (2). Then

    u1=delta/lambda*,
    u2=delta/lambda*-2lambda*gamma epsilon,
    Gi=[ui]_+²/(4lambda*hi).

Uniformly as r→0 with epsilon>=0,

    ai=[ui]_+/(2lambda*hi)+O(r²),
    kc=lambda Delta+(G2-G1)/2+O(r³).                 (6)

At k=lambda Delta+kappa the reduced objectives have common baseline Q0, price shifts-2i kappa, linear action drives ui, and quadratic penalty lambda*hi ai². The exact omitted drives are O(r²); coefficients have O(r) changes. Uniform strict concavity of the reduced objective near its optimizer, or equivalently the strictly convex supporting function, gives the constrained maximizer estimate using the Lipschitz positive-part map. The gains therefore have O(r³) remainder even across activation. Equality yields kappa=(G2-G1)/2+O(r³).

For M in any fixed compact subset of[2,4), the true optimizer resources straddle M for sufficiently small r, and

    F-Fold=[(4-M)G1+(M-2)G2]/2+O(r³),
    Fold=1-lambda[(4-M)H1+(M-2)H2].                  (7)

Fold is the old zero-action chord, even where no longer optimal. This is not uniform up to M=4; section5 supplies that missing regime.

## 4. A second C1/non-C2 value boundary

Fix S<1/2 sufficiently close to the corner. Analytically continue the count-one-active/zero-two tie k0(lambda) beyond its optimal region. At activation, R1A=2/(1+aA), C1A=2g1(aA,S)/(1+aA). Define the upper-action drive

    D(lambda)=2lambda c2-[1-2lambda H2-4k0(lambda)].

Differentiating the tie gives k0'=(C1-2H2)/(4-R1). Using(4) yields the EXACT transverse derivative

    D'(lambda_A)=1/[lambda_A(1+2aA)]>0.              (8)

For tau=lambda-lambda_A>0, the count-two support gains

    G=D'(lambda_A)² tau²/[4lambda_A h2(S)]+O(tau³).

The crossing price shifts by G/(4-R1A) from the inactive analytic continuation. For fixed2<=M<4,

    F-Finactive = [(M-R1A)/(4-R1A)]
                  tau²/[4lambda_A³ h2(S)(1+2aA)²]+O(tau³). (9)

Below the boundary the difference is exactly zero locally. The right coefficient is positive, so F is C1 but not C2 there. Finactive is the analytic SINGLE-ACTIVE continuation, not Fold. This distinction is essential; Fold already has a positive count-one gain.

## 5. Released joint moving endpoint

Write epsilon=r e,delta=r d with bounded e,d>=0 and M=4-r s, bounded s>=0. Put

    v=d/lambda*-2lambda*gamma e,
    sc=2[v]_+/(lambda*h2).

Then F-Fold=r² L(s,v)+O(r³). For v<=0, L=0. For v>0,

    L=sv/4-lambda*h2 s²/16,  0<=s<=sc,
    L=v²/(4lambda*h2),       s>=sc.                 (10)

The exact pure-two branch is F=M/4-lambda M g2(4/M-1,S)/2. Expanding this expression gives the first piece; the mixed support gives the second. Value and first s derivative match at sc, checked exactly. Count-one contributions have an additional O(r) mixture weight here and enter only at O(r³). At M=4 the gain is EXACTLY zero: this neighborhood lies below lambda2(S), and K2587's zero-two/zero-three support certifies that endpoint. Equation(7) must not be substituted at M4.

## 6. Independently certify a finite score49/100 consumer

The local theorem has no claimed explicit radius. Instead, repeat K2591's global inequalities on the separate rational rectangle

    S=49/100,
    lambda in[.5385,.5395], k in[.00825,.0084],
    b in[.15,.34].                                  (11)

For Hm=m w0(S/m), K2587's lower bound is sum w>=Hm-c(S/m)A+A²/(8S). As in K2591, first split N=1-2lambda sum w-2km by sign: N<=0 is dominated by abort; only for N>0 use p<=1/(1+A). Define Jm=1-2lambda Hm-2km,D=lambda/(4S). The decreasing H-count secants and kmin>lambdamax(H3-H4) imply Jm<=J3 for all m>=3; c(S/m)<=c(S/3). Thus those counts are bounded by

    U3=J3+(2lambda c(S/3)-J3)_+²/(4D).

For extreme two-score splits, Hout=w0(.15)+w0(.34), cmax=191/250 give the analogous Uout with Jout=1-2lambda Hout-4k. The differences U3-J2 and Uout-J2 are convex in(lambda,k): the square positive-part divided by lambda is a convex perspective of a convex function, and remaining terms are affine. Four exact rational-log corner checks prove both strictly negative on the ENTIRE rectangle. The zero-two J2 is positive there. No count truncation or mesh assertion is involved.

The strict bound 2lambdamax[cmax+w0(.34)]<1-2kmax forces suffix action zero on the surviving score domain. Strict convexity then gives the exact Q1/Q2 forms (1) throughout(11). The resource difference is at least4/1.34-2=66/67, so Q1-Q2 is strictly increasing with k. The following STRUCTURAL argument proves crossing and activation topology for EVERY lambda in(11), without extrapolating sampled optimizers. The one-stage action derivative numerator is

    N1(a)=-1+2k+2lambda[w(a,S)-(1+a)w_a(a,S)],
    N1'(a)=-2lambda(1+a)w_aa(a,S)<0.

Its maximum at a=1/100 over(11) occurs at lambdamax,kmax and is strictly negative by exact interval arithmetic. Hence every one-stage optimizer has a<1/100 and

    C1 >= 2w(1/100,S)/(1+1/100) = C1min.

For a two-stage optimizer, Q2>=J2 implies g2<=H2-aJ2/(2lambda)<=H2, since J2>0. Therefore C2<=2H2. The probe certifies C1min>2H2 uniformly. Comparing the affine policy lines at two multipliers shows Q1-Q2 strictly DECREASES with lambda at fixed k; no envelope differentiability is assumed. At lambdamin,kmin, the one-stage derivative at0 is strictly negative so Q1=J1, and J1<J2<=Q2. At lambdamax,kmax, the all-action two-stage majorant

    U2=J2+(2lambda c(S/2)-J2)_+²*S/lambda

is strictly below the one-stage candidate J1. Monotonicity transfers these two corner signs to the whole multiplier interval. Combined with resource separation66/67, this proves a unique crossing kc(lambda), continuous and strictly increasing throughout(11).

At the crossing the zero-action boundary drives are

    B1=2lambda[c(S)+H1]+2kc-1,
    B2=2lambda[c(S/2)+H2]+4kc-1.

They strictly increase with lambda. The unique first zero is lambda1, the exact zero/zero crossing; the second is the certified lambda_A in(4). Both lie in(11). Thus the ENTIRE explicit multiplier interval has the zero/one-active/both-active topology. At the second boundary the first optimizer has a<.01<S, so action stationarity and(4) apply. This is an independent finite-interval proof, not an assumed radius for the joint local theorem.


A rational bisection of w_a(a,S)+c2 brackets aA without numerical logarithms; interval logs then bracket(4):

    lambda1≈.53877935204723207131,
    lambda_A≈.53906542998810280922,
    aA≈.00016093621428138894,
    kA≈.00830951624824123323.

The probe verifies the activation point lies strictly in the globally reduced rectangle. At lambda=.5390, the two-stage action is exactly zero at the crossing; at .5391 it is strictly positive. Derivative signs are certified across their entire crossing enclosures, rather than inferred from the trial policies.

For each multiplier, exact rational candidate policies and global convex supporting planes enclose the unique price to width<1e-50. Mixing the ACTUAL one/two-stage policies with theta=(R2-3)/(R2-R1) gives resource EXACTLY3. Its value is a lower bound; max of the global support bounds plus3k is an upper bound. The independent enclosures have width<1e-50:

| lambda | first action | second-policy first action | F(3), display only |
|---|---:|---:|---:|
| .5390 | .00012413721210953616 | 0 | .8462213175618504 |
| .5391 | .00018037685483960085 | .00000820633444285960 | .8461928014452111 |

The same candidates also give a UNIFORM value enclosure of width<1e-50 for every budget between their actual resources: approximately[1.99975,4] at .5390 and[1.99964,3.999967] at .5391. Indeed the affine upper-minus-mixture gap is theta(Qbar-J1)+(1-theta)(Qbar-J2), at most the larger endpoint slack, certified exactly. This is an enclosure of the frontier across the candidate resource interval, not a claim that rational candidates are the exact optimizers or that the exact frontier is affine all the way to those rational endpoints. Both budget3 policies beat their zero-action chords. The upper consumer's score is about .24500048631475359, not exactly S/2. Lower/upper values and rational policies are in the report; displays are not the certificate.

The support proof uses convex Phi=2lambda cost+Q(1+a)+2mk-1. A rational candidate and interval upper J_hi supply its tangent; an explicit epsilon inflates Q until the tangent is strictly positive on the entire rectangle. At a=0 an outward nonnegative action derivative is a valid KKT condition, not an error to erase. Interval logarithms use32 atanh terms, rigorous geometric tail and outward rounding to1e-65. Floating search only produced candidate inputs; replay uses no numerical optimizer.

## Evidence, follow-through and next comparison

The probe checks gap/Hessian/transversality identities, uniform rectangle exclusions, action boundary, price brackets and actual finite resource mixtures. The uniform compactness/KKT argument and the C1/non-C2 and moving-endpoint proofs are written results, not inferred from pass counts. Independent field-specialist and distinct integrated hostile reviews returned final substantive findings[] after scope and candidate-feasibility repairs.

This closes the joint corner and a new second activation, beyond K2597's fixed slices. Large-count uniformity still requires new remainder/gap estimates, and arbitrary-score global topology remains separate. Compare those harder questions against actual source-native response or physically specified conserved readout; no physical probability or GU claim follows from this scalar optimizer.

[K2597](k2597-stopping-threshold-bifurcation-2026-11-06.md), [K2591](k2591-multistage-stopping-support-2026-11-06.md), [K2587](k2587-countwise-stopping-support-2026-11-05.md), [probe](../../tests/channel-swings/k2599_joint_stopping_corner_probe.py), [report](../../lab/process/k2599-joint-stopping-corner.json).
