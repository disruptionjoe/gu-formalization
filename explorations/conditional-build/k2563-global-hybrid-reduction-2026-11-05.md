---
title: "K2563 A global finite-atom approximation to adaptive stopping"
status: active_research
doc_type: exploration
created: "2026-11-05"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: explicit all-score hybrid approximation and constrained-budget brackets; no numerical intermediate optimum or finite-policy attainment
scripts:
  - tests/channel-swings/k2563_global_hybrid_reduction_probe.py
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
result: K2563
carrier: original fresh fair stopping histories and relaxed finite-atom continuum schedules LAYER=toy CHIRALITY=N/A
pairing: unconditional success probability and expected original leakage cost ON=declared_carrier
real_structure: real probabilities, controls and costs
grading: finite stages, relaxed continuum blocks and adaptive policies remain distinct
action_owner: repository-construction -- supplied fresh fair stopping law
target: global adaptive dual hierarchy and certified budget error MAP-TYPE=evaluation
```

# K2563 A finite-dimensional approximation with an explicit global error

## Result and nonduplication

For every 0<S<=1/2, lambda>0 and integer N>=1, optimize hybrids with at most N finite original stages and N+1 exact optimized continuum blocks. If V_N is their maximal dual value and V is the full original adaptive supremum, then

    V_N <= V <= V_N + lambda*S^2/(4N).                 (1)

This turns the unrestricted problem into a convergent sequence of compact finite-dimensional optimizations with a proved error. It does not solve those optimizations numerically or show one atom suffices. K2495 already supplies stage ordering and exact continuum cost; K2507 already supplies the one-first-atom suffix. K2549's small-score/nearcritical compression does not supply this global explicit bound. Here the effect is a bound on ALL original adaptive competitors, followed by constrained-budget brackets and an exact hybrid Bellman recursion.

The law, fresh routing, private randomization and original failure-path cost are supplied mathematics, not a native GU probability law. SC-META-53 remains UNCERTAIN; ledger0.263 and physical-domain/quotient debts do not move. No novelty or physical implementation claim is made.

## 1. Original stages and continuum blocks

For a nonidle original stage 0<=a<=b<=S, put

    w(a,b)=log(1+(b-a)^2/[2(a+b)(2-a-b)]),
    E=1/(1+a), c=2E*w(a,b).

For a finite schedule with sum b_i=S, success p=product E_i and unconditional cost C=sum_i(product_(j<i) E_j)c_i. Idle stages have zero cost and E=1. K2483's stage reduction and K2485's mixture theorem connect this class to all original adaptive policies; that inherited connection is essential, not inferred from the finite formula.

Final-stage overshoots may be clipped to remaining score with a'=min(a,b'), improving success and not increasing cost (K2485 section1). Nonhitting finite schedules are dominated by free abort; this licenses the complete-score schedule class.

A continuum block has score t>=0, logarithmic survival h in[0,t], survival exp(-h), and minimum conditional cost J(t,h) from K2495. Its control satisfies R'=r in[0,1], R(0)=0,R(t)=h, and cost integral exp(-R)g(r), with

    g(r)=(1-r)^2/[2(1+r)], g' =1/2-2/(1+r)^2,
    0<=g<=1/2, -3/2<=g'<=0.

J is continuous on its closed triangle, including J(0,0)=0,J(t,0)=t/2,J(t,t)=0. The precise globally optimal control and formula are K2495 sections3--5; K2507 section2 proves the continuity needed here. Each block is a separate relaxed object, not an infinite-hit original policy.

## 2. Replace small stages while preserving every survival prefix

For b>0 set q=a/b, r=log(1+a)/b and replace the stage by constant continuum r for duration b. Then0<=r<=q<=1 and the survival is EXACTLY E. The elementary logarithm bounds imply 0<=q-r<=b/2. K2495(5) gives

    b*g(q)<=2w(a,b)<=b*g(q)+b^2/2.                   (2)

Let j=g(r) integral_0^b exp(-rt)dt. Its difference from c satisfies

    -b^2/2 <= j-c <= b^2.                            (3)

For the lower bound, j>=b E g(r)>=b E g(q), while c<=E[b g(q)+b^2/2]. For the upper bound split

 j-c <= [g(r)-g(q)] integral_0^b exp(-rt)dt
          +g(q) integral_0^b[exp(-rt)-exp(-rb)]dt
       <=(3/4)b^2+(1/4)b^2.

Here exp(-rt)-exp(-rb)<=r(b-t), r<=1; neither survival prefix nor failed-path cost is dropped. Replacing multiple stages preserves each original boundary prefix. Optimize every contiguous replaced block at its unchanged total score and log-survival; this lowers cost further and changes no boundary survival.

Retain the N largest b_i, preserving their original order. If there are at most N positive stages, no replacement is needed. Otherwise let m be the largest omitted score. The retained scores sum to at least Nm, hence

 sum_omitted b_i^2 <=m sum_omitted b_i<=m(S-Nm)<=S^2/(4N),
 S^2/(4N)-m(S-Nm)=(S-2Nm)^2/(4N).                (4)

Thus every finite original schedule maps to a hybrid with identical success and cost at most C+epsilon_N, epsilon_N=S^2/(4N). The square-sum estimate itself is sharp for2N equal scores, though this does not assert the cost-error constant is sharp.

## 3. Compact hybrid class and all-adaptive dual bracket

Parameterize a hybrid by N padded atoms (a_i,b_i) and N+1 blocks (t_i,h_i), with0<=a_i<=b_i,0<=h_i<=t_i and sum b_i+t_i=S. Zero atoms/blocks pad smaller classes. Each component cost is multiplied by survival of all preceding components, and terminal success is their product. This is a compact parameter set with continuous cost and success; include free abort as a separate zero pair. Thus V_N is a maximum. The classes are nested.

Every finite hybrid is approximable in (p,C) by finite original schedules of the same total score. For h<t, K2495's integrated-hazard partition gives exact score/success with convergent cost. For h=t, use free microstages a=b=t/n: cost0 and survival(1+t/n)^(-n) tend to exp(-t). Exact finite success need not be preserved in this boundary case; convergence is sufficient. There are finitely many components, so all prefix-weighted costs converge as well.

It follows V_N<=V. Conversely applying (4) to any finite schedule gives p-lambda C<=V_N+lambda epsilon_N. K2483's equality of adaptive and finite-schedule dual suprema then proves(1). Initial mixtures do not change an affine supremum. The result includes randomization, abandonment and nonabsorption through that earlier exact reduction; no sampling argument replaces it.

## 4. Constrained budgets and an explicit vertical error

Let F_N(B) be maximum success at expected cost<=B in the convex hull of hybrid pairs, and let F(B) be the full original adaptive frontier. Write p0=1/(1+S). Then for all B>=0,

    F_N(B)<=F(B)<=F_N(B+epsilon_N).                  (5)

For the right inequality use K2485's finite-mixture reduction and apply the skeleton to each component. Each cost increases by at most epsilon_N, so their averaged cost does also. For the left inequality approximate each hybrid by finite schedules. At B>0 any small cost overshoot can be repaired by mixing with the exact free baseline (cost0,success p0), with mixture weight tending to1. At B=0 zero cost forces every nonidle atom free and every block r=1; product(1+b_i)*exp(sum t_i)>=1+S, so p<=p0. The single free atom gives equality. Thus both frontiers equal p0 at0.

Mix a B+epsilon_N hybrid optimizer with that free baseline, with weight B/(B+epsilon_N), to fit B. Since its success is at most1, for B>0,

    0<=F(B)-F_N(B)<=epsilon_N*(1-p0)/(B+epsilon_N).  (6)

The compact hull has maximizers, and at most two hybrid components suffice by the one-budget planar convex-hull supporting-line argument, as in K2485. This is relaxed attainment, not attainment by any finite original policy. The approximation plus cost repair supplies genuine finite original policies approaching these lower values.

## 5. Exact Bellman recursion, without an unverified grid

For fixed lambda>0 and continuation payoff x>=0 define the atom map

    A_b(x)=max_(0<=a<=b) [x-2lambda*w(a,b)]/(1+a), A_0(x)=x.

The free choice a=b proves A_b(x)>=0. Define

    q(u)=min_(0<=r<=1)[g(r)+r*u]
        =2sqrt(1+2u)-2-u, 0<=u<=3/2;
        =1/2, u>=3/2.

This follows from g'(r)+u=0, whose interior root is2/sqrt(1+2u)-1; use r=0 beyond3/2 and r=1 at0. In particular q is nonnegative and Lipschitz, q(0)=0. The continuum map C_t(x) solves

    dC_t/dt=-lambda*q(C_t/lambda), C_0(x)=x.        (7)

To justify the sign and global optimum, for any continuum control define its survival y and evaluate y(t)C_(T-t)(x)-lambda integral_0^t y g(r). Its derivative is lambda*y[q(C/lambda)-r*C/lambda-g(r)]<=0. Choosing the minimizing feedback makes equality. Thus(7) is precisely the maximal block payoff over all h in[0,t], not an unproved local HJB guess. It stays nonnegative and is monotone in x.

Writing V_N(s) at remaining score s and fixed lambda,

    V_0(s)=C_s(1),
    V_N(s)=max_(t,b>=0,t+b<=s)
             C_t(A_b(V_(N-1)(s-t-b))).             (8)

Every nonempty hybrid decomposes into a first continuum block, first atom and remaining hybrid; monotone component maps let the suffix be optimized first. Padding handles absence of an atom. Equation(8) is a continuous compact optimization, not a certified upper value from a sampled action grid. A practical numerical solver must separately bound its global optimization and continuum integration errors, then add(1).

The hierarchy reuses endpoint truths: for lambda>=4/sqrt3, N>=1 already contains K2559's globally optimal one-stage law and hence is exact; for lambda<=4/5, N=0 already contains K2561's optimal diffuse limit. The new unresolved numerical use is the intermediate interval, where neither endpoint theorem applies.

## 6. Executed precision consumer and contrary constructions

At S=1/2,lambda=19/10 the dual remainder is19/(160N). N=297 makes it strictly less than1/2500, the certified K2561 hybrid separation; N=296 does not. N=21 gives19/3360, far larger than that separation. The21-stage lower witness alone is therefore not a close estimate of the unrestricted optimum. At its exact budget B_h>37866038451/10^12, (6) becomes at most1/[3(16N B_h+1)]; N=549 certifies error<1/1000 using that lower budget bound. This is an atom-count/error specification for an optimizer, not a numerical optimization of V_297 or F_549.

Strong contrary controls target the actual proof seams:

- A positive free atom a=b has cost0, while r=log(1+b)/b<1 gives j>0. Continuum replacement can increase cost; the error allowance is essential.
- Choosing r=a/b instead changes survival exp(-a) rather than1/(1+a); log(1+a)<a for a>0.
- Retaining arbitrary stages is invalid: S=1/2,N=1, retain1/10 and omit2/5 gives omitted square4/25>1/16.
- Removing the prefix survival mischarges suffix cost. The probe checks the actual rational prefixes of the K2561 witness and a deliberately omitted-prefix counterfixture.
- The r=1 continuum boundary is a finite-policy limit; it supplies no original finite hit at its limiting exact success.

The next substantial computational task is a certified global implementation of(8), or a structural theorem reducing its atom count and continuous maximization. The theorem gives the required approximation budget; an unconstrained grid or a one-atom guess still cannot certify the full intermediate frontier.

## 7. Executed successor: a certified finite grid, including its cost

The continuous recursion now has a global mesh-error certificate. For x in[0,1], define the clipped atom D_(b,r)(x)=max(0,[x-lambda W(r,b)]/(1+rb)), W=2w(rb,b). Both D and C are nondecreasing and1-Lipschitz in x. Clipping adds only free abort: once a negative suffix is replaced by0, all preceding maps send0 to0; a positive final value never used such a clipping and is an actual hybrid payoff.

Set h(r)=g(r)/2,z=b(1+r)/2,eta=b*h/(1-z), so W=2log(1+eta). On0<=r<=1,0<=b<=1/2,

  h<=1/4, |h'|<=3/4, 1-z>=1/2,
  eta<=b/2, |eta_b|<=1,
  |eta_r|<=(3/2)b+(1/2)b^2<=(7/4)b.

Thus0<=W<=b, |W_b|<=2, |W_r|<=7b/2. Differentiating the atom quotient, then using Lipschitz continuity at the clipping kink, gives

  Lip_b(D)<=1+5lambda/2,
  Lip_r(D)<=b(1+4lambda),
  Lip_t(C)<=lambda/2.                              (9)

Take score mesh Delta=S/J and ratio mesh delta=1/M, with positive integers J,M. Floor all N atom lengths and the first N continuum lengths to multiples of Delta; add ALL removed score to the final continuum block. If the removed atom and earlier continuum totals are Berr,Terr, each is at most N*Delta. Nonexpansive composition bounds the loss by

 (1+5lambda/2)Berr+(lambda/2)Terr
      +(lambda/2)(Berr+Terr)<=N(1+4lambda)Delta.

Then floor each atom ratio to the ratio mesh. The loss is at most (1+4lambda)delta*sum b_i<=(1+4lambda)S*delta. The construction preserves every score/admissibility constraint, including zero-length and free atoms.

Let L_(N,J,M) be the exact maximum on this finite grid, computed by (8) with integer score splits and the ratio-grid maximum replacing A. Then

  L_(N,J,M)<=V<=L_(N,J,M)+lambda*S^2/(4N)
                           +(1+4lambda)(N*S/J+S/M). (10)

If every scalar component evaluation has absolute error at most eta_eval, clamp numerical values to[0,1] and add (2N+1)eta_eval to each endpoint; maxima and nonexpansive composition cannot amplify errors, and every hybrid contains at most2N+1 components. Alternatively propagate rigorous intervals throughout and use the upper endpoint of the grid maximum in(10).

A concrete certified scalar evaluator needs no unbounded numerical assumption. For C_t(x), forward Euler with step h<=1 uses E_h(x)=x-lambda*h*q(x/lambda), a monotone map. The exact trajectory has0<=C''<=lambda/2, hence

  E_h(x)<=C_h(x)<=E_h(x)+lambda*h^2/4.

Use rational square-root enclosures in q and rational logarithm enclosures in W; propagate interval endpoints with the monotone Euler map and add its local remainder. This yields finite rigorous enclosures for every grid component. The probe executes a small exhaustive grid as a reproducibility fixture, not as a tight numerical optimum.

There is a consequential resource implication. At S=1/2,lambda=19/10, choose N=594 so truncation19/(160N)<1/5000. Allocate mesh<=1/10000 and evaluation bracket width<=1/10000. Choose J=51,084,000 and M=86,000, giving each mesh contribution1/20000, and per-component error eta_eval<=1/23,780,000. The two-sided evaluation width is2(2N+1)eta_eval, so the full bracket width is strictly below1/2500. A literal exhaustive parameter enumeration has

    binomial(J+2N,2N)*(M+1)^N

padded vectors before duplicate elimination. Even just its ratio choices exceed10^2700. Thus this rigorous but deliberately crude certificate is not a practical direct enumeration recipe at the prior0.0004 margin. A direct DP table caches atom maximizations but still uses N*binomial(J+3,3) continuum evaluations, plus order N*J^2*M atom evaluations. These are combinatorial counts, not measured runtime or a proof that every solver has this cost. The useful next task is certified pruning, sharper moduli, or structural atom reduction—not launching that literal bank or claiming a close optimum from a small grid. This is an evidenced cost of the displayed algorithm, not an all-method impossibility or a new stopping policy.

## Verification

Universal stage-replacement, compactness, mixture and feedback arguments are the mathematical proof. The probe checks exact algebraic error identities, endpoint and coefficient inequalities, rational logarithm brackets for real finite schedules, and the numerical-consumer thresholds with exact rational arithmetic. Counts separate exact checks, supporting fixtures and report consistency. K2483/K2485 adaptive transfer and K2495/K2507 continuum optimizer are reused at unchanged assumptions. Internal independent specialist and integrated reviews are required; no external-expert or proof-assistant certification.

[Probe](../../tests/channel-swings/k2563_global_hybrid_reduction_probe.py), [report](../../lab/process/k2563-global-hybrid-reduction.json), [K2495](k2495-stopping-order-and-continuum-2026-11-02.md), [K2507](k2507-stopping-optimal-hybrid-tail-2026-11-02.md), [K2485](k2485-constrained-stopping-frontier-2026-11-01.md), [K2561](k2561-higher-budget-stopping-2026-11-05.md).
