---
title: "K2480 Sharp scheduled repair preludes improve dyadic stopping bounds"
status: active_research
doc_type: exploration
created: "2026-11-01"
classification: CONVENTIONAL_COMPARATOR
target_claim: "NONE-NOT-A-KILL"
claim_ceiling: "sharp scheduled continuum repair subproblem and original-law dyadic lower bounds; global adaptive optimum open"
---

# K2480 Sharp scheduled repair preludes improve dyadic stopping bounds

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
result: K2480
carrier: original fresh half-test half-use absorbing experiment and its declared scheduled continuum repair limit LAYER=toy CHIRALITY=N/A
pairing: actual-law expectation and reached-history conditional probability ON=declared_carrier
real_structure: real probabilities and nonnegative real costs
grading: classical trial histories and completed use-stage count
action_owner: repository-construction -- supplied conditional mathematical models
target: Sharp scheduled repair subproblem and fixed-confidence stopping lower bound MAP-TYPE=evaluation
```

Classification: conditional independent classical probability mathematics; no GU physical, source-polarity, ledger0.263 or canon change. Carrier, pairing, real structure, grading and action owner are exactly K2477's original fresh half-test/half-use absorbing experiment with predictable risks; score starts at zero. Target: fixed-confidence expected-original-budget coefficient. Not a physical apparatus or a global adaptive optimum.

## Claim and scope

At every epsilon=2^(-(m+1)), m>=0, the original coefficient satisfies C_epsilon >= Lsched=log(2)/f(H*) >1.9064, improving K2477's >1.8736. Here

 g(r)=(1-r)^2/[2(1+r)],
 f(y)=2sqrt(2y+1)-y-2,
 T(H)=integral from H/2 to H of 1/f(y) dy,
 T(H*)=1, H* in (.59,.60).

Numerically H*=.59173715557349258635..., Lsched=1.90645223834555... . This is a proved optimum for the explicitly defined continuous scheduled repair subproblem, embedded as a limiting family of finite original experiments. It is NOT an optimum among all adaptive stopping experiments, and the inherited Csharp upper bound remains unchanged. Actual finite laws can violate1.90 or1.905; the limit is not itself an experiment.

## 1. Exact scheduled original law

For each reached use-stage i choose 0<a_i<b_i<=1 predictably from number of completed uses. Repeat fresh half-test/half-use routing with those risks until use or test failure. Test pass retains stage. One stage succeeds with probability s_i=1/(1+a_i) and has expected full-law budget 2w_i/(1+a_i), where

 w_i=log(1+(b_i-a_i)^2/[2(a_i+b_i)(2-a_i-b_i)]).

Thus a branch with n stages has exact

 p=product s_i,
 D=sum_i (product_{j<i} s_j) 2w_i/(1+a_i),
 Zhit=log(2) sum_i b_i.

For a constant segment of N stages, reached weight q, its cost contribution is q*(2w/a)*(1-(1+a)^(-N)); multiply q by that segment's success probability before continuing. These expectations include costs on eventually failed paths. Finite use targets do not mean deterministically bounded trial time; pass trials make trial count unbounded, but termination is almost sure with finite expectation. After termination set a=b=0.

## 2. Continuous scheduled repair problem and exact optimum

Consider any measurable r:[0,1]->[0,1], q(t)=exp(-integral_0^t r), p=q(1), D=integral_0^1 q(t)g(r(t))dt. Minimize H(r)=D/(p-1/2) over p>1/2. This is a declared continuum limit of small b stages whose total use score is log2; it is not assumed to represent every original adaptive law.

The strictly convex g has g''(r)=4/(1+r)^3. For0<y<3/2,

 min_{0<=r<=1}(g(r)+ry)=f(y),
 r(y)=sqrt(2/(y+1/2))-1.

A direct identity supplies a verification certificate for all r in[0,1]:

 g(r)+r*y-f(y)=[sqrt(2y+1)*(1+r)-2]^2/[2(1+r)].

f>0 and strictly concave on(0,3/2), f(0)=0. Therefore T(H)=integral_{1/2}^1 H/f(Hx)dx is strictly increasing on(0,3/2). T(0+)=log2<1; T(3/2)>=(3/4)/(1/2)=3/2>1 because f<=1/2 there. Unique H* follows. The interval(.59,.60) is certifiable with logs/square roots. Let F(z)=-log(z-1)+3log(3-z); direct differentiation gives

 T(H)=F(sqrt(H+1))-F(sqrt(2H+1)).

Let y solve y'=-f(y), y(0)=H*. Then y(1)=H*/2 and y(s) stays in[H*/2,H*]. Write H_star=H*. Define V(t)=-y(1-t). Its derivative is -f(y(1-t)). For any schedule r,

 D-H_star*p+H_star/2
 =integral_0^1 q(t)[g(r(t))+r(t)y(1-t)-f(y(1-t))]dt >=0.

Hence every feasible schedule has H(r)>=H*. Equality occurs for

 r_opt(t)=sqrt(2/(y(1-t)+1/2))-1.

This is smooth and interior. D>0 at this schedule, so equality implies p>1/2, proving feasibility and attained optimality of this subproblem. Strict convexity shows uniqueness up to null sets. The optimal hazard DECREASES with completed use-score: r_opt(0)≈.5852 to r_opt(1)≈.35349. Constant schedules cannot attain the optimum since y is strictly varying.

## 3. Original-law finite embeddings and strict crossing

Approximate r_opt uniformly by rational piecewise-constant schedules r_1,...,r_J with rational segment lengths ell_j summing to1. Each has p=exp(-sum ell_j r_j)>1/2 and D=sum_j exp(-sum_{i<j}ell_i r_i) k(r_j)(1-exp(-ell_j r_j)), k=g/r. Uniform convergence of rates gives convergence of p,D and H=D/(p-1/2) to H*. Choose rational r_tail close to r(H*).

For integers M divisible by segment denominators, let b=1/M. Branch0 has M ell_j stages with a_j=r_j/M, followed by one extra stage at the last rate. Its total score after m perfect a=b=1 prelude uses is c(m+1+1/M). Branch1 has m+1 perfect prelude uses, then one stage with a_tail=r_tail/M and b=1/M, giving the same score. Let p0_M,D0_M be branch0's exact stage-product probability and cost, p1_M=1/(1+r_tail/M),D1_M=2w_tail/a_tail*(1-p1_M).

Fresh a=b=0 fair routing bits choose branch0 with probability alpha_M, branch1 otherwise; they give zero initial score and no budget. With rho=2^-m, total full-law success probability and budget are

 P=rho[alpha p0_M+(1-alpha)p1_M/2],
 K=rho[alpha D0_M+(1-alpha)D1_M/2].

Set alpha_ideal=(1/2+1/M^2-p1_M/2)/(p0_M-p1_M/2). For sufficiently large M it lies in(0,1). Let Jcoin satisfy 2^Jcoin>=4M^3, and round alpha_ideal downward to a multiple of2^-Jcoin. This gives an actual finite routing law and P>epsilon (indeed the loss from rounding is at most rho/2^Jcoin).

As M grows,

 M alpha -> r_tail/[2(p-1/2)],
 M K/rho -> [r_tail H+g(r_tail)]/2,
 epsilon*(Zhit-log(1/epsilon))/K -> c/[g(r_tail)+r_tail H].

For any lambda<Lsched, first choose a sufficiently close rational schedule and rational r_tail so this limiting ratio exceeds lambda, then a sufficiently large finite M so ratio>lambda and P>epsilon. Therefore C_epsilon>=Lsched. Earlier crossing only increases the event, so the equal final-score success event is enough. Minimizing g(r_tail)+r_tail H* gives f(H*) and establishes sharpness only for this continuum repair-plus-infinitesimal-tail construction class.

## 4. Independent checks and remaining question

Verify H bracket through interval T values; exact derivatives and Bellman factorization; a rational piecewise schedule finite law with strict crossing margin; direct per-stage recursion; omitted failure cost and omitted prelude survival controls; reject P=epsilon endpoint and score-free activation. Search of predecessor stopping notes, k24* and path-dependencies found no scheduled-hazard repair optimum; K2477 supplies constant-rate branch mixtures only. No novelty claim follows.

The larger fixed-confidence adaptive Bellman problem remains open, as do nondyadic sharp bounds. A next substantial discriminator is whether arbitrary history-dependent original controls have a reduction to a richer score-state value problem, or whether a rigorously better original construction beats this scheduled-prelude class. Maintain source and physical credit unchanged under either outcome.

[Probe](../../tests/channel-swings/k2480_scheduled_stopping_preludes_probe.py) and [report](../../lab/process/k2480-scheduled-stopping-preludes.json).

[Probe](../../tests/channel-swings/k2480_scheduled_stopping_preludes_probe.py) and [report](../../lab/process/k2480-scheduled-stopping-preludes.json).

Independent internal review checked the variational identity, strict finite-law crossing and scope; no substantive finding remained. This is not external-expert or proof-assistant certification.
