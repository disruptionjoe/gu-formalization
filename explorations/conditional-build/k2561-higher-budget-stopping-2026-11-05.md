---
title: "K2561 Exact high-budget stopping phase and finite-policy nonattainment"
status: active_research
doc_type: exploration
created: "2026-11-05"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: exact high-budget adaptive supremum for the supplied stopping law; intermediate budgets and native GU remain open
scripts:
  - tests/channel-swings/k2561_higher_budget_stopping_probe.py
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
result: K2561
carrier: original fresh fair test/use histories with predictable randomized actions and finite expected original cost LAYER=toy CHIRALITY=N/A
pairing: unconditional expectations including hit, failure, abort and nonabsorption ON=declared_carrier
real_structure: real probabilities and logarithmic costs; exact rational sign certificates
grading: input and output flow values, finite stages, continuum limits and original finite-hit events remain distinct
action_owner: repository-construction -- supplied stopping probability law
target: exact high-budget supremum, nonattainment and approximation complexity MAP-TYPE=evaluation
```

# K2561 The high-budget optimum is a limit, not an infinite-hit policy

## Result and scope

For every 0<S<=1/2 and 0<lambda<=4/5, the exact original adaptive dual
value is an explicitly integrated autonomous flow. This proves a second
exact constrained-budget segment, near the already-known sure-hit saturation
budget S/2. Except at budgets strictly ABOVE saturation, its value is a
supremum not attained by any original policy. Finite repeated-use schedules
approach it; their required number of positive score stages grows at least
inversely with their dual error, and a matching order construction exists.

K2559 supplies the low-budget one-stage segment. The intervening budgets
remain open: this result does not claim the entire frontier or its transition.
K2485 already owns saturation and endpoint nonattainment; the new content is
the whole phase below saturation, its global adaptive certificate, explicit
parametric value, and its approach/complexity. This is supplied-law independent
mathematics, not a GU probability, physical implementation or novelty claim.
SC-META-53 remains UNCERTAIN and ledger0.263's physical-domain/action debts
remain unchanged.

## 1. An exact increasing-generator region

Retain K2559's original cost, map and output generator:

    w(a,s)=log(1+(s-a)^2/[2(a+s)(2-a-s)]),
    F_s(u)=min_(0<=a<=s)[(1+a)u+2w(a,s)],
    M=-2(1+a)w_a+2w,
    G_s(v)=partial_s F_s(F_s^-1(v)).

At an interior minimizer 2k=u, k=-w_a, and the OUTPUT root is M=v.
Its fixed-output derivative is

    partial_s G_s(v)=2K,
    K=w_ss-w_as^2/w_aa+w_s*w_as/[(1+a)w_aa].          (1)

The new exact rational certificate proves K>0 throughout
0<=s<=1/2, 0<=r=a/s<=2/5 after canceling the s=0 factors. Substitute
r=2X/5,s=Y/2: its numerator has50 strictly positive tensor Bernstein
coefficients, minimum78360951/7812500; its denominator has77 strictly
positive coefficients, maximum87808/125. Independent inverse conversion
reconstructs both polynomials. In particular

    2K>=gamma=78360951/2744000000>0.                  (2)

This region contains every interior output root with v>=1. Indeed at
r=2/5, use log(1+x)<=x and the exact rational identity

    1-[2(1+a)k+2x]
      =2(3421s^2-6095s+2350)/[7(7s-10)(89s-140)]>0. (3)

Both numerator and denominator have strictly positive Bernstein coefficients
on[0,1/2]; M(2s/5,s)<1. Since M_a=-2(1+a)w_aa<0, M=v>=1 forces
r<2/5. This is an output-root barrier, not an input-root substitution.

The minimizer can also lie at a=0. That branch must not be discarded.
There F_s(u)=u+2w(0,s), G_s(v)=2w_s(0,s) and

    partial_s G_s(v)=2w_ss(0,s)
      =8(3-s)/[(2-s)^2(4-s)^2]>=3/8>gamma.          (4)

The last inequality follows because each positive reciprocal term in
w_ss=1/(2-s)^2-1/(4-s)^2 increases on this interval. At the transition
u=2k(0,s), both generator formulas agree. Strict convexity w_aa>0 gives
continuous optimizers; the fixed-v branches are piecewise smooth, with the
same continuous generator. The boundary threshold M(0,s) has derivative
2[w_s-w_as]>0 (verified directly), hence at most one switch. Thus integrating
(1)--(4) is legitimate and gives

    G_s(v)>=q(v)+gamma*s, v>=1,                       (5)
    q(v)=G_0(v)=2sqrt(1+2v)-2-v, 1<=v<=3/2,
                   1/2,                 v>=3/2.

q is positive, nondecreasing and Lipschitz; q'=r(v)=2/sqrt(1+2v)-1
below3/2 and q'=0 above. It is C1 across3/2. The s=0 formula follows from
the original cost expansion and the constrained minimizer, including a=0.

## 2. Autonomous flow dominates every finite stage

Let H_t(u) solve y'=q(y), y(0)=u>=1. Since q<=1/2,
H_t(u)<=u+t/2. Scalar comparison with(5), using q nondecreasing, gives

    F_b(u)>=H_b(u)+gamma*b^2/2, u>=1, 0<=b<=1/2.     (6)

For b=0 equality holds. For b>0 the inequality is strict. Comparison stays
inside v>=1 because both trajectories increase. No sign result from K2559's
opposite small-output region is extended here.

Fix theta=1/lambda>=5/4 and let

    u(s)=H_s^-1(theta), V_lambda(s)=lambda*u(s).

For0<=s<=S<=1/2, u(s)>=theta-s/2>=1. The autonomous semigroup gives
H_b(u(s))=u(s-b). Therefore for every clipped action0<=a<=b<=s,

    (1+a)V_lambda(s)+2lambda*w(a,b)-V_lambda(s-b)
        >=lambda*gamma*b^2/2.                        (7)

This is the original Bellman supersolution. It uses the SAME theta at every
remaining state. Also V(0)=1 and 0<V<=1. Original overshoots and a>b use
K2557's monotone clipping: b'=min(b,s), a'=min(a,b'); the extra terms
V(s)(a-a') and2lambda[w(a,b)-w(a',b')] are nonnegative. No modified cost,
unweighted prefix, finite-schedule representation or continuity hit is used.

Apply K2557's finite-horizon original conditional-expectation telescope.
Bounded terminal potentials and monotone cost convergence imply for every
predictable randomized original policy with finite expected cost

    V(S)-p+lambda*C
      =E sum_active delta
        +E[1_abort V(s_abort)]
        +E[1_nonabsorption V(s_infinity)]>=0,         (8)

where delta is half the original Bellman residual. Approaching score0
without a finite hit is nonabsorption with V(0)=1. Infinite expected cost
cannot improve a positive-multiplier objective.

## 3. Finite witnesses make the bound sharp

For fixed lambda>0 and S, start v0=u(S), h=S/n. Define a deterministic
schedule by choosing a_i to minimize F_h(v_(i-1)), and put
v_i=F_h(v_(i-1)). Its exact affine map is

    v_n=(product_i(1+a_i))*u(S)
            +2 sum_i w(a_i,h) product_(j>i)(1+a_j).

Consequently its ORIGINAL prefix-weighted dual value is

    p_n-lambda*C_n
      =V(S)-lambda*(v_n-theta)/product_i(1+a_i).      (9)

On any fixed compact interval of input values containing this trajectory,
F_h(v)=v+h*q(v)+O(h^2), uniformly, directly by minimizing the uniform
original expansion w(rh,h)=h*g(r)/2+O(h^2),
g(r)=(1-r)^2/[2(1+r)]. The same first-order expansion holds for H_h.
Their maps are uniformly Lipschitz with constant at most1+h. Discrete
Gronwall gives v_n=H_S(u(S))+O(1/n)=theta+O(1/n).
Thus finite schedules attain dual error O(1/n), proving(8) sharp. Each
schedule has finitely many stages and almost-sure finite absorption with
finite expected trial count; no infinite stage schedule is declared a hit.
Constants can depend on the fixed(S,lambda). Uniformity as lambda->0 is
not asserted.

For the constrained consumer it is convenient to use the equally valid
explicit schedules a_i=h*r(H_((i-1)h)(u(S))). Uniform Taylor/Riemann-sum
bounds give the same O(1/n) dual approximation and

    p_n -> p=q(u)/q(theta),
    C_n -> B=theta*p-u.                              (10)

Indeed survival converges to exp(-integral r(v(t))dt)=q(u)/q(theta), since
q'=r and v'=q. The cost follows by the original weighted Riemann sum
or(9)'s vanishing dual gap. The minimizer r is Lipschitz across3/2, so a
boundary crossing causes no loss of the O(1/n) error order.

## 4. Explicit integrated value and exact high-budget frontier

Define the increasing C1 clock

    tau(v)=log(sqrt(1+2v)-1)-3log(3-sqrt(1+2v)), 1<=v<=3/2,
            2v-3,                                     v>=3/2.

Both branches equal0 at3/2 and tau'=1/q. Hence

    u=tau^-1(tau(theta)-S),
    V_lambda(S)=lambda*u,
    p(theta)=q(u)/q(theta), B(theta)=theta*p(theta)-u. (11)

The inverse is used only at arguments whose result is at least1, as proved
above. At theta0=(3+S)/2, u=3/2,p=1,B=S/2. For theta>=theta0 the same
saturation contact remains p=1,B=S/2, and V=1-lambda*S/2.

For5/4<=theta<theta0, u<3/2 and u<theta. Set J=p. Differentiating the
flow gives u_theta=J and

    J_theta=J*[q'(u)-q'(theta)]/q(theta)>0,
    B_theta=theta*J_theta>0,
    dp/dB=1/theta=lambda,
    d²p/dB²=-1/[theta^3*J_theta]<0.                  (12)

Strictness uses q' strictly decreasing below3/2 and zero above. Define
B_hi(S)=B(5/4). Then B_hi(S)>0 and the entire budget interval
[B_hi(S),S/2) has exact supremal original hit probability p(theta), with
unique theta in[5/4,theta0). Equation(8) is its universal upper bound.
For a sequence in(10) enforce the exact budget rather than just convergence:
if C_n>B, mix it with the known zero-cost policy with probability
alpha_n=B/C_n; otherwise use it directly. Costs are then <=B and probabilities
still converge to p because B>0 and alpha_n->1. Thus no budget relaxation is
hidden in the lower bound. B_hi>0 follows because the limiting path has
positive length and g(r)>0 throughout r<=2/sqrt3-1<1, with positive survival.

For B>S/2 the existing finite sure-hit schedules attain probability1.
At B=S/2 equation(11) gives the existing nonattained supremum1. The new
strictly concave phase connects continuously to it. The interval between
K2559's critical contact and B_hi is NOT decided here; neither proven
segment is claimed maximal.

## 5. Nonattainment and exact finite-schedule complexity

No original policy attains V_lambda(S) for0<lambda<=4/5. If equality held
in(8), all nonnegative terms would vanish. A policy with positive hit
probability must have a reached positive clipped-b trial with positive
probability. Countability then makes E sum_active b'^2>0, so(7) gives a
strict gap. A policy with zero hit probability has p-lambda*C<=0<V(S).
This covers arbitrary adaptive policies, infinite waiting times and
nonabsorbing histories, not only finite schedules. The constrained values
in[B_hi,S/2] are therefore also unattained: attainment with C<=B would
attain their supporting dual bound (and requires C=B).

For a deterministic completed schedule with n positive-score stages,
P_i=product_(j<=i)(1+a_j)^-1>=exp(-S). Its exact telescope and(7) give

    V(S)-(p-lambda*C)
      >=lambda*gamma*sum_i P_i*b_i^2/2
      >=lambda*gamma*exp(-S)*S^2/(2n).               (13)

Thus dual error eta requires n>=lambda*gamma*exp(-S)*S²/(2eta).
Together with section3 this is the sharp order Theta(1/eta) for finite
completed deterministic schedules at fixed(S,lambda). This stage-count
statement is NOT transferred to arbitrary adaptive expected stage counts
or initial mixtures without their own occupation/weight argument. Full
adaptive nonattainment already follows independently from(8).

### Released adaptive occupation bound

Let N_+ count all active trials with positive clipped score b', including
failed/test-pass trials but excluding zero-score idles. With finite E N_+,
Tonelli and predictable fresh fair use give

    E sum_active b'=2 E sum_use b'>=2S*p.

The use sum is pathwise at most S and equals S on a hit; nonhitting paths
can contribute additional progress. Cauchy--Schwarz on the joint
probability/counting occupation measure gives

    E sum_active (b')² >= (2S*p)²/(E N_+).

Together with per-trial delta>=lambda*gamma*(b')²/4, this proves

    eta=V(S)-p+lambda*C
        >=lambda*gamma*S²*p²/(E N_+).                (13a)

For a contact budget C<=B with frontier p_star, eta<=p_star-p. Hence
E N_+>=lambda*gamma*S²*p²/(p_star-p). Infinite E N_+ makes this bound
vacuous; it is not a ban on long waiting. The finite schedules in section3
have E N_+<=2n, and exact-budget mixing changes neither O(1/n) error nor
O(n) expected complexity. Thus near each fixed contact in the new segment,
including saturation, expected positive-score trial complexity has sharp
order Theta(1/(p_star-p)), over the full original adaptive class.

## 6. Released saturation sensitivity

Fix S>0 and write epsilon=S/2-B, theta0=(S+3)/2. In a sufficiently small
left neighborhood of saturation theta>3/2. Set x=3/2-u. Exact expansions
from(11) give

    q(3/2-x)=1/2-x²/8-x³/32+O(x^4),
    theta=theta0-x-x³/12+O(x^4),
    epsilon=theta0*x²/4+(theta0/16-1/6)*x³+O(x^4).

Analytic square-root inversion on x>=0 gives the TRUE adaptive frontier

    p(B)=1-epsilon/theta0
             -4epsilon^(3/2)/(3theta0^(5/2))+O(epsilon²),
    lambda(B)=1/theta0+2sqrt(epsilon)/theta0^(5/2)+O(epsilon). (14)

The finite left marginal at saturation is2/(S+3); its next correction is
square-root, so curvature diverges as saturation is approached. For budgets
above saturation the frontier is constant, with right derivative0. The
endpoint is a supremum corner, not an attained optimal experiment. Expansions
are at fixed positive S; no uniform assertion as S->0 is made.

## 7. Executed intermediate-budget successor: a finite hybrid beats both candidates

The new high-budget theorem and K2559's low-budget theorem leave a genuine
intermediate question. An exact finite original-law construction now proves
that neither the pure one-stage family nor the named autonomous-fluid
candidate settles that question. Fix

    S=1/2, lambda=19/10,
    first atom (a0,b0)=(349/2000,3/10),
    then20 identical stages (a,b)=(21/5000,1/100).

All controls are rational, 0<a<=b, and total score is exactly1/2. Put
A0=2349/2000 and T=(1+21/5000)^(-20). The original finite policy has

    p=T/A0,
    C=2w(a0,b0)/A0 + 2w(a,b)*(1-T)/(A0*a).           (15)

The geometric sum includes the survival prefix of every stage; no success
conditioning or unweighted leakage appears. Rational logarithm enclosures
prove

    0.711020048691 < p-(19/10)C < 0.711020048692.      (16)

This exceeds the GLOBAL optimized one-stage dual value. Its unique interior
optimizer has output root M(a,1/2)=10/19, and exact bounds show

    3219/10000 < a_opt < 3221/10000.

The existing strict w_aa>0 and M_a<0 certificate proves uniqueness and the
maximum. Since w decreases with a, its value is at most

    [1-(19/5)w(3221/10000,1/2)]/[1+3219/10000]
       <71/100.                                     (17)

This is a certified global maximum bound, not comparison with a sampled
optimizer or an unoptimized rational proxy.

For the pure autonomous-fluid candidate extend q and tau as in the preceding
comparison to positive values. Its dual value is

    (19/10)*tau^-1(tau(10/19)-1/2).

Exact square-root and logarithm enclosures prove

    tau(10/19)-tau(187/500)<1/2,

so that value is strictly below (19/10)(187/500)=3553/5000=0.7106.
Therefore the explicit21-stage policy beats BOTH comparators by MORE THAN
1/2500 in original dual value. The numerical scout only suggested the
rational inputs; all accepted inequalities use rational enclosures.

For reproducibility, for every positive rational z use

    y=(z-1)/(z+1),
    log z=2 sum_(j=0..23) y^(2j+1)/(2j+1)+R,
    |R|<=2|y|^49/[49(1-y²)].

Square roots are bounded by adjacent rationals with denominator10^16 using
integer square root. Monotonicity propagates these bounds through tau.
The proof also keeps the one-stage derivative bracket and original prefix
formula explicit. Twenty finite tail stages suffice; the accepted witness
has almost-sure finite absorption and does not depend on an infinite-hit
interpretation.

There is an immediate exact-budget consequence. Let B_h=C in(15) and
p_h=T/A0. Every initial mixture of completed one-stage policies for this SAME
scoreS, optionally including free abort, has p-lambda*C<71/100 by(17).
At cost<=B_h its hit probability is therefore below71/100+lambda*B_h,
whereas p_h>711/1000+lambda*B_h. The explicit finite hybrid beats the entire
one-stage-mixture constrained class at its own exact budget by MORE THAN
1/1000. Here B_h lies in(0.037866038451,0.037866038452) and
p_h is the exact rational T/A0, approximately0.782965521750. The budget is
the logarithmic expression(15), not the rounded decimal endpoint.

This result directs the next calculation toward intermediate hybrid structure.
It does NOT prove this rational hybrid optimal, the optimal number/order of
atoms, a whole-class nonatomic optimum, a unique transition or the complete
constrained frontier. The fluid comparison is to the named autonomous
candidate; its global optimality was proved only in section2's domain.

## Verification and remaining work

The probe independently derives the rational generator, certifies its whole
rectangle and the logarithmic root barrier with inverse Bernstein
reconstruction, checks the boundary generator, clock, dual derivatives,
original affine/prefix accounting and asymptotic coefficients. Wrong-root,
wrong-prefix and overextended-generator controls reject the relevant false
claims. Universal ODE, adaptive expectation, finite approximation and budget
repair arguments are written above and require independent review; finite
fixtures do not replace them.

A further exact contrary fixture tests the next tempting extension. At
s=1/2,a=7/20, put v=M(a,s), G=2w_s(a,s). Alternating rational bounds through
order4 on log(1+9/782) prove sqrt(3)/4<v<1 and

    (G+2+v)²-4-8v<0, hence G<q(v).

Thus the sufficient generator inequality(5) cannot simply be extended
through ALL intermediate outputs above the old critical threshold. This
rejects that global criterion, not every intermediate fluid trajectory or
the possibility of a larger certified phase. The exact fixture is recorded
in the probe, not inferred from a grid.

There is also a structural contrary result for a full-fluid phase extension.
For this comparison only extend q(v)=2sqrt(1+2v)-2-v to all0<v<=3/2.
K2559 proves G_s(v)<q(v) on0<v<=theta_star=sqrt(3)/4 for every s>0.
For theta<=theta_star, let u=H_S^-1(theta)>0 using this extended fluid
flow. Scalar comparison stays in the positive sublevel and gives

    F_S(u)<H_S(u)=theta.

Therefore F_S^-1(theta)>u: the actual finite one-stage dual value STRICTLY
exceeds the fluid candidate for every finite lambda>=4/sqrt(3),S>0.
This is a proved failure of full fluid optimality, stronger than a derivative
criterion failure. It reuses K2559's unchanged theorem and introduces no new
uniform assertion in the unresolved interval4/5<lambda<4/sqrt(3).
The finite-stage and diffuse phases cannot be identified by extrapolation;
a transition/hybrid construction remains a substantive open consumer.

The useful next question is the intermediate-budget hybrid/atomic phase or
a rigorously sharp junction with this diffuse phase. Native GU, physical
controller costs, actual experiments and a full fixed-score phase diagram
remain separate and unproved.

[Low-budget theorem](k2559-parametric-stopping-concavity-2026-11-05.md),
[adaptive accounting](k2557-parametric-stopping-support-2026-11-05.md),
[saturation and strong duality](k2485-constrained-stopping-frontier-2026-11-01.md).
