---
title: "K2507 Optimal distributed tails after a finite stopping stage"
status: active_research
doc_type: exploration
created: "2026-11-02"
classification: CONVENTIONAL_COMPARATOR
target_claim: "NONE-NOT-A-KILL"
claim_ceiling: "conditional supplied-model mathematics; no native GU realization, experimental certification or global stopping optimum"
---

# K2507 Optimal distributed tails after a finite stopping stage

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
result: K2507
carrier: original fresh fair test/use stopping law at score S=1/2 LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert trace or original failure-inclusive probability cost ON=declared_carrier
real_structure: complex adjoint for effects; real probabilities for stopping
grading: original verifier sectors or finite stopping stages
action_owner: repository-construction -- supplied instruments and original probability law
target: fixed-main optimal suffix, restricted hybrid minimization and unequal finite-tail improvement MAP-TYPE=evaluation
```

## Result and scope

The constant-ratio limit in K2505 is strictly improvable at fixed score and success. Coupling the existing K2495 continuum optimizer to one finite first stage gives the unique globally optimal suffix for that fixed stage, a compact two-variable minimization for the entire one-first-stage relaxation, and exact finite-policy approximations. Endpoint derivatives give necessary stage/tail matching equations. An independent finite argument proves that adjacent identical costly stages admit a strict hazard redistribution and supplies a better exact three-stage witness.

K2495 owns the convex-perspective continuum theorem and its approximation estimate; these are reused. The new result is their prefix-weighted coupling, restricted attainable relaxation, matching and strict finite/continuum improvements. None proves the unrestricted stopping optimum, a global transition or the K=1/1000 frontier. SC-META-53 remains UNCERTAIN; LT-SM8/LT-GR6b and native matter/light/domain obligations are unchanged. Source polarities, ledger0.263 and physical credit remain unchanged. No novelty, external-expert or proof-assistant certification is claimed.

## Notation
For 0<=a<=b<=S<=1/2, w(a,b)=log(1+(b-a)^2/[2(a+b)(2-a-b)]), w(0,0)=0. A=1+a. Fixed terminal success is exp(-H), total score S. Let

g(r)=(1-r)^2/[2(1+r)], g'(r)=1/2-2/(1+r)^2,
g''(r)=4/(1+r)^3,
Q(r)=g(r)-r*g'(r)=(1-r)(1+3r)/[2(1+r)^2].

Let V(t,h) be K2495's continuum minimum of integral exp(-R) g(R') over 0<=R'<=1, R(0)=0,R(t)=h. It has the uniquely optimal decreasing control r'=-Q(r)/g''(r), with a terminal r=0 arc when needed. V(0,0)=0, V(t,0)=t/2,V(t,t)=0.

## 1. Globally optimized tail at a fixed first atom
For a main atom (a,b), put t=S-b and h=H-log A. Feasibility is 0<=h<=t. Original limiting cost is

F(a,b;S,H)=A^-1 [2w(a,b)+V(t,h)].

This is the globally minimal cost among all absolutely continuous suffix controls following this *fixed* atom, uniquely in the tail path. The factor A^-1 is actual prefix survival and may not be omitted. F is not the unrestricted original optimum.

K2495's exact parametric formula supplies V. Put
Lfun(r)=-log(1-r)-2log(1+r)+3log(1+3r).
For interior start rho and terminal sigma, terminal zero-arc length ell>=0:
t=Lfun(rho)-Lfun(sigma)+ell,
h=log[Q(sigma)/Q(rho)], ell*sigma=0,
V=(8Q(rho)/3)[1/(1+3sigma)-1/(1+3rho)]+exp(-h)*ell/2.
Endpoint cases handled separately; do not divide by Q(1)=0.

## 2. Global minimum within the one-first-atom relaxation
For 0<=H<log(1+S), minimize F over compact
D={(a,b):0<=a<=b<=S,0<=H-log(1+a)<=S-b}.
D is nonempty: (exp(H)-1,S). w and V extend continuously to their cone/triangle boundaries, so the restricted global minimum exists. Continuity of V can also be proved by rescaling time and changing a feasible control's mean by convex mixing with 0 or 1; g is bounded/Lipschitz and survival is Lipschitz in the L1 control norm. At t=0,0<=V<=t/2 gives continuity.

Every feasible point is approximable by genuine finite original schedules at unchanged S,H:
* If h<t: K2495 partitions t into n intervals Delta=t/n, rho_i=interval average of its optimizer, b_i=Delta, a_i=exp(rho_i*Delta)-1. For Delta<=min(1/2,1-r_start), 0<=a_i<=b_i. Score and product success are exact; |C_n-F|<=13t^2/(4A n). The main atom is unchanged, even if a=b. This avoids K2505's boundary-invalid equal-ratio approximation. b_i<=t<=S<=1/2 and main b<=S<=1/2.
* If h=t>0: necessarily a<b in the stated H range. Otherwise H=log(1+b)+S-b>=log(1+S). Choose n free suffix stages a_i=b_i=t/n, and repair main hazard to a_n=A exp(t)/(1+t/n)^n-1. Then a_n>a, a_n->a, hence a_n<b eventually, while score/product are exact. Costs converge to F. This sequence can approach from below; no one-sided universal bound is asserted.
* t=0 is already the finite main atom.
Thus the restricted minimum is an achievable limiting upper bound on the minimum full original cost at this success. It supplies finite approximants, not finite attainment or equality with unrestricted optimum.

Moreover h=t>0 cannot minimize this relaxation for H>0: increase a slightly at fixed b, making h<t. V(t,t-epsilon)=O(epsilon^2) by using constant r=1-epsilon/t, whereas 2w(a,b)/(1+a) strictly decreases to first order for a<b. This boundary exclusion is optional; the direct approximation proof covers it regardless.

## 3. Exact atom–tail matching equations
For 0<h<t with an interior terminal ratio sigma>0, write rho=r(0),sigma=r(t). Endpoint variation and the autonomous conservation law give
V_h=exp(-h)g'(sigma), V_t=Q(rho), V+V_h=g'(rho).

When the optimal path has a terminal zero-control arc of length ell>0, the correct derivative is instead
V_h=exp(-h)[g'(0)-ell/2]. The identities V_t=Q(rho) and V+V_h=g'(rho) remain valid. To see the extra term, use Q(rho)=exp(-h)/2, ell=t-Lfun(rho), and differentiate the explicit V_active(rho,0)+exp(-h)ell/2. Varying h changes the active/zero-arc junction. A bare terminal-momentum formula misses this constraint contribution. At rho=1/2 and ell=1/10, the extended continuum formula gives V=17/36, V_h=-31/36 and V+V_h=-7/18; this algebra control has t>1/2 and is not a feasible original S<=1/2 policy. A within-domain zero-arc control uses rho=1/100, ell=1/10, with t=log(1092727/1009899)+1/10<1/2. Both test the corrected derivative. The matching equations below therefore survive the boundary-arc correction.
The last identity follows either from the explicit formula or homogeneity of the perspective action: derivative with respect to initial y is V+V_h and equals minus initial canonical momentum g'(rho).

Using independent atom variables a,b and h=H-log(1+a),t=S-b:
F_a=A^-2[2A w_a-2w-V-V_h],
F_b=A^-1[2w_b-V_t].
Hence every interior stationary hybrid satisfies
2A w_a(a,b)-2w(a,b)=g'(rho),
2w_b(a,b)=Q(rho).
Equivalently M=-2A w_a+2w=-g'(rho), N=2w_b=Q(rho)=min_r[g(r)+Mr]. Thus the main atom lies on its suffix-indifference switching curve. Equations are necessary interior conditions, not a global certificate or uniqueness theorem for the atom.

Useful exact check: K2495 rho=1/2,sigma=2/5 has V=4/99,exp(-h)=245/297, g'(sigma)=-51/98. Therefore V+V_h=-7/18=g'(rho), V_t=5/18=Q(rho).

## 4. Constant-ratio hybrid tails are strictly suboptimal
For t>0 and 0<r<1, let h=rt. The constant tail's cost is
V_const=g(r)(1-exp(-rt))/r.
It is not the unique minimizer: the Euler equation requires r'=-Q/g''<0, whereas the constant is interior with Q>0. Convex-perspective sufficiency/strictness from K2495 gives V<V_const for every such t, not only asymptotically. At r=0 or1 the endpoint constraint leaves a unique constant path, so strictness must be excluded there.

For fixed r in a compact subinterval of (0,1), the optimized control, uniformly for s in[0,t], is
r_opt(s)=r-[Q(r)/g''(r)]*(s-t/2)+O(t^2).
This follows from smooth ODE flow and the implicit average constraint. First variation of V around constant r has coefficient
q(s)=exp(-rs)g'(r)-g(r)*integral_s^t exp(-ru)du,
q'(s)=exp(-rs)Q(r).
Its pairing with a mean-zero variation has leading Q(r)*integral(s-t/2)delta-r. The leading second variation is (g''/2)*integral(delta-r)^2. Substitution gives
V_const-V=Q(r)^2/[24g''(r)]*t^3+O(t^4).
For K2505's fixed-H main atom A=exp(H-rt), total improvement is
F_const-F_opt=Q(r)^2/[24 exp(H) g''(r)]*t^3+O(t^4).
The coefficient is strictly positive. In simplified form Q^2/(24g'')=(1-r)^2(1+3r)^2/[384(1+r)]. This does not alter K2505's quadratic onset coefficient beta_infinity; it improves the next order. Combining with finite approximation yields genuine finite schedules that beat a constant-tail limit at fixed score/success for sufficiently fine partitions. It supplies no uniform unrestricted optimum or first transition claim.

## 5. Exact unequal finite-tail improvement
For any adjacent identical costly interior stages (q,b),(q,b), 0<q<b<=1/2, preserve the pair product by
 a1=q+epsilon,
 a2=(1+q)^2/(1+q+epsilon)-1.
For small positive epsilon both remain in(0,b). Pair cost after fixed prefix survival P0 is
2P0/(1+q)^2 * [(1+a2)w(a1,b)+w(a2,b)].
Its derivative at epsilon=0 is
2P0/(1+q)^2 * [q*w_a(q,b)-w(q,b)] <0.
Indeed w>0 and w_a<0 when q<b and q+b<=1 (differentiate the positive log argument; both derivative terms are negative). All suffix prefix weights remain unchanged. Thus an identical costly adjacent pair can never be an unrestricted finite optimum. Free q=b and zero q=0 are excluded for good reasons.

Explicit K2505 improvement retains main (1934773/5905227,49/100) and replaces its two suffixes by
 (a1,b1)=(15007/7000000,1/200),
 (a2,b2)=(105176/49105049,1/200).
Here a1=3/1400+1/1000000 and (1+a1)(1+a2)=1968409/1960000=(1+3/1400)^2. Total score=1/2, terminal success=3/4 exactly.
Let lo8(x)=sum(k=1..8)(-1)^(k+1)x^k/k and hi9 analogously to9. For x>=0 they bracket log(1+x). With x(a,b)=(b-a)^2/[2(a+b)(2-a-b)], compute original cost using exact prefix weights. Independent stdlib Fraction calculation gives
 C_K2505-C_new >9/10^10,
 C_new <212613497/10^10 (=0.0212613497).
Diagnostic only: true interval approx0.02126134960634000 and gap approx9.97304238045e-10. The rational inequalities, not decimals, are certificates. Eight/nine alternating orders also suffice for the main stage.
The new budget is below K2505's 106307/5000000; its one-stage-mixture separation argument still applies using C_one-stage(3/4)>=417/19600 and monotonic convex cost. No claim this witness is optimal.

## Strong counterconstructions / scope checks
* K2495 free single atom at H=log(1+S) has zero cost, while continuum-only cost is positive. Thus optimizing tails does not license deleting atoms.
* More than one nonfree finite atom remains outside the one-first-atom class; no argument here excludes them or initial mixtures.
* At r=0,1 strict varying-tail improvement is false; the fixed average forces the sole constant control.
* K2505's naive equal-ratio finite approximation can be inadmissible at a free-main boundary. Exact-integrated-hazard partition above preserves a fixed free main if h<t, and h=t uses an explicit main repair plus strict a<b.
* No fixed-n or local IFT argument excludes remote competitors or establishes unrestricted K=1/1000.

## Verification and remaining work

The universal conclusions rest on the written arguments and independent internal review. The exact probe checks symbolic derivative/endpoint identities, original prefix-weighted rational logarithm bounds, admissibility and contrary finite constructions. Its finite counts are coverage, not universal theorem counts. It is not a sampled optimization certificate.

A global original-law Bellman or exchange certificate must still treat multiple finite atoms and initial mixtures; the one-first-stage minimization is a feasible upper construction, not a lower bound for those classes. Native common-domain matter/light and the full ordinary mixed-hook inverse remain separate construction debts.

[Exact probe](../../tests/channel-swings/k2507_stopping_optimal_hybrid_tail_probe.py), [saved report](../../lab/process/k2507-stopping-optimal-hybrid-tail.json), [K2495](k2495-stopping-order-and-continuum-2026-11-02.md), [K2505](k2505-stopping-satellite-hierarchy-2026-11-02.md).

Convex-perspective sufficiency is an established method; see [Boyd and Vandenberghe](https://stanford.edu/~boyd/cvxbook/). No novelty is claimed for that method.
