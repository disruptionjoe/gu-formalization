---
title: "K2501 Collective satellite exclusion and local exact stopping frontier"
status: active_research
doc_type: exploration
created: "2026-11-02"
classification: CONVENTIONAL_COMPARATOR
target_claim: "NONE-NOT-A-KILL"
claim_ceiling: "conditional supplied-model mathematics; no measured calibration, global finite-budget optimum or native GU realization"
---

# K2501 Collective satellite exclusion and local exact stopping frontier

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
result: K2501
carrier: original fresh fair test/use absorbing experiment at fixed score S in (0,1/2] LAYER=toy CHIRALITY=N/A
pairing: failure-inclusive expected one-sided leakage cost ON=declared_carrier
real_structure: real probabilities and controls
grading: finite schedules, arbitrary stage order, mixtures and adaptive trial histories
action_owner: repository-construction -- supplied probability law
target: uniform collective exclusion and exact small-budget success frontier MAP-TYPE=evaluation
```

## Result and scope

For each fixed 0<S<=1/2 there exists K_S>0 such that every budget
0<K<K_S has an exactly optimal one-stage policy in the full original adaptive
experiment. Its success is 1/(1+S-d), where the unique small d>0 solves

    K=C1(d)=2/(1+S-d) log(1+d^2/[2(2S-d)(2-2S+d)]).     (1)

Consequently the full frontier has the stronger expansion

    F_S(K)=1/(1+S)+c_S sqrt(K)+q_S K+O_S(K^(3/2)),
    c_S=2sqrt(S(1-S))/(1+S)^(3/2),
    q_S=(3S-1)/(1+S)^2.                                (2)

K2499 supplies the leading term and concentration; the new step excludes
arbitrarily many coordinated satellites uniformly, and then controls rare
expensive randomized components by a single affine bound. A conservative explicit corollary at S=1/2 certifies 0<K<=2^(-88).
This is not an estimate of the transition, an assertion about K=1/1000, or
global one-stage optimality. K2493's finite-budget two-stage advantage survives.
No limit uniform in S down to0 is claimed.

This is GU-independent supplied-model probability mathematics, with the same
original failure-inclusive cost and fresh fair test/use law as K2485. No
physical apparatus or native GU state is constructed. SC-META-53 remains
UNCERTAIN; LT-SM8/LT-GR6b and all native matter/light/domain obligations remain
open. Ledger0.263, source polarities, canon and physical credit do not change.
No external-expert, proof-assistant or literature-novelty certification is claimed.

## 1. Exact object and reusable reduction

For a finite completed schedule, write 0<=a_i<=b_i, sum b_i=S,

    p=product_i(1+a_i)^(-1),
    C=2 sum_i P_i w(a_i,b_i),   P_i=product_{j<=i}(1+a_j)^(-1),
    w(a,b)=log(1+(b-a)^2/[2(a+b)(2-a-b)]).

Remove idle a=b=0 stages. K2485 proves that finite mixtures of these schedules,
including free abandonment, have the same constrained supremum as all original
adaptive policies, without relaxing the budget. It does not identify every
adaptive path with a deterministic schedule. K2499 provides a uniform global
bound p<=p0+c_S sqrt(C)+Lstar C and concentration whenever C tends to0 and
p>p0=1/(1+S).

For reference, put D=sum(b_i-a_i), A=sum a_i=S-D and E=1/p-1-A.
Product expansion implies E>=0; above baseline E<D. K2499 proves

    D<=2sqrt(S C/p0),
    A-a_max<=2D/A,
    T<=2D/A+D,                                          (3)

where T is the total score outside a stage attaining a_max, for A>0.
Thus T tends to0 uniformly as C tends to0, independently of stage count.
These results are reused, not recounted as fresh finite-grid evidence.

## 2. Collective fixed-success comparison

Fix p=1/(1+S-d), d>0 small. Select a main stage with score S-T and
deficiency x=b_main-a_main. For all satellites define

    V=sum_sat(b_i-a_i),     Q=product_sat(1+a_i)-1.

For T>0, 0<=V<=T and T-V<=Q<=exp(T)-1<=2T when T<=1/2.
Exact success conservation gives

    x-d=[(1+S-T-d)Q-T]/(1+Q).                           (4)

When d+T<=S/2,

    alpha T-beta V<=x-d<=3T,    alpha=S/4, beta=2.        (5)

For the lower bound, use Q>=T-V and 1+S-T-d>=1+S/2;
the numerator is at least (S/2)T-(1+S)V. Divide the positive term
by 1+2T<=2 and the negative term by a number at least1. The upper bound
uses Q<=2T and 1+S<=3/2, dropping the negative T term.

Set

    h(x,b)=w(b-x,b)
      =log(1+x^2/[2(2b-x)(2-2b+x)]).

Every P_i>=p. The bound w(a,b)>=(b-a)^2/[4(a+b)] and
Cauchy-Schwarz therefore give the order-independent comparison

    C/(2p)>=h(x,S-T)+V^2/(8T).                         (6)

Indeed satellite sum(a_i+b_i)<=2T. At T=0 the entire schedule is already
the single stage (apart from idle stages), so no division by0 is used.

Near (x,b)=(0,S), h=x^2 q(x,b) with smooth positive q, and
h_xx(0,S)=1/[4S(1-S)]>0. On a fixed sufficiently small rectangle there
are constants m,M,L>0 such that

    h_xx>=m,  0<=h_x(d,S)<=Md,  |h_b(x,b)|<=Lx^2.        (7)

These constants exist by smoothness, positivity and compactness on a rectangle
whose denominators stay positive. They depend only on fixed S, not the number
or order of stages. The factor x^2 in the last bound is essential.
Also h_x(d,S)>=md since h_x(0,S)=0. Restrict d,T<=epsilon so x<=d+3T<=4epsilon
and b in[S-epsilon,S] remain in that rectangle, with 2epsilon<=S/2.
Put theta=alpha/(2beta)=S/16.

**Small satellite deficiency, V<=theta T.** Equation (5) gives x-d>=alpha T/2.
Taylor's lower bound in x and the b derivative estimate give

    h(x,S-T)-h(d,S)
      >=m alpha dT/2+m alpha^2 T^2/8-LT(d+3T)^2.         (8)

Because (d+3T)^2<=12epsilon(d+T), the right side is strictly positive
for T>0 once 12L epsilon<min(m alpha/2,m alpha^2/8). The additional
nonnegative penalty in (6) is not needed in this case.

**Larger satellite deficiency, V>theta T.** Convexity at (d,S) and
x-d>=-beta V imply

    h(x,S-T)-h(d,S)+V^2/(8T)
      >=V[theta/8-beta M epsilon-16L epsilon^2/theta]>0   (9)

after a further fixed reduction of epsilon. Here (d+3T)^2<=16epsilon^2,
T<V/theta and V^2/(8T)>theta V/8. Thus both cases have strict positive
cost difference uniformly for any nonempty satellite collection. Such an
epsilon exists because all constants are fixed and positive. No bound on
stage count or stage order has entered.

## 3. All finite schedules, including remote configurations

Suppose there were no d_S>0 on which every multistage schedule of the same
success costs strictly more than C1(d). Then one could choose d_j down to0
and violating schedules with C_j<=C1(d_j)=O_S(d_j^2). Equation (3) supplies
a main stage with T_j tending to0. Eventually d_j,T_j lie in the same uniform
rectangle of section2, contradicting (8) or (9) whenever T_j>0. Therefore
there is a d_S>0 such that the exact minimum finite-schedule cost at
p=1/(1+S-d), 0<d<d_S, is C1(d), attained only by a single nonidle stage.

This compactness-by-contradiction step does not assume that an optimizer exists
in an unbounded-stage space. A putative sequence of cheaper actual finite
schedules is enough, and the one-stage minimum is itself attainable.

## 4. Randomization, abandonment and all adaptive policies

C1 is strictly increasing near d=0. Define the feasible local curve
f(C)=1/(1+S-d(C)), f(0)=p0. Choose eta>0 small enough that K2499's global
bound forces every finite schedule of cost C<=eta with p>p0 into section3's
success interval, and eta is inside the local inverse domain. Section3 then
implies p<=f(C) for all such schedules; p<=p0 and abandonment also satisfy it.

Analytic inversion in y=sqrt(C), justified in section5, makes f a convergent
power series in y near0. Consequently f is strictly concave on a sufficiently
small (0,eta], extends continuously at0, and f'(K) tends to positive infinity.
For each sufficiently small K>0 its tangent

    ell_K(C)=f(K)+f'(K)(C-K)

majorizes f on[0,eta]. Moreover ell_K(eta)>=1 for all sufficiently small K,
since f'(K) tends to infinity whereas f(K)-K f'(K) tends to p0.
As f'(K)>0, ell_K(C)>=1 for C>=eta, covering every other finite schedule
by p<=1. This is one global affine bound, not a discarded-tail argument.
It covers free abandonment as well, including its zero cost.

Average the bound over any finite mixture with expected cost at most K:
its success is at most ell_K(K)=f(K). K2485's no-budget-relaxation theorem
then transfers the same bound to all original adaptive trial histories. The
one-stage policy of exact cost K attains f(K). This proves (1) for an
existential sufficiently small K interval. Rare expensive mixture components
cannot evade the tangent bound; a local schedule comparison alone would not
have established this conclusion.

## 5. Released subleading coefficient and sensitivity

Let L0=1+S. Direct expansion of the exact original cost gives

    C1(d)=a2 d^2+a3 d^3+O_S(d^4),
    a2=1/[4S(1-S)L0],
    a3/a2=1/L0-(2S-1)/[2S(1-S)].                       (10)

The analytic function d sqrt(C1(d)/d^2) has derivative sqrt(a2)>0 at0.
Its analytic inverse gives

    d(K)=sqrt(K/a2)-a3 K/(2a2^2)+O_S(K^(3/2)).          (11)

Substitution into 1/(L0-d) yields q_S=(3S-1)/(1+S)^2 and (2).
The convergent square-root series also justifies termwise differentiation:

    F'_S(K)=c_S/(2sqrt(K))+q_S+O_S(sqrt(K)),
    F''_S(K)=-c_S/(4K^(3/2))+O_S(K^(-1/2))<0.

The coefficient q_S changes sign at S=1/3; at S=1/2 it equals2/9.
This says how the local curve bends relative to its leading square-root term;
it does not imply a change in the positive leading gain or loss of concavity.
The derivative diverges, explaining why the supporting tangent defeats remote
mixtures at small budgets. None of these expansions is asserted uniform as
S changes or at a stated positive numerical budget.

## 6. Released explicit sufficient interval at S=1/2

The local theorem can certify an actual, extremely conservative budget range:

    0<K<=2^(-88) implies exact one-stage optimality.      (12)

Here is a rational certificate, without numerical optimization. On
0<=x<=1/8, 3/8<=b<=1/2 let u=2b-x, D=2u(2-u), N=D+x^2. Then
5/8<=u<=1, 55/32<=D<=2, D_x=4(u-1)<=N_x=8b-4-2x<=0. Thus

    h_xx=4/D-2/N+D_x^2/D^2-N_x^2/N^2 >=2/D>=1,
    h_xx<=128/55+(48/55)^2<4,
    |h_b|=8(1-u)x^2/(DN)<=3072 x^2/3025<2x^2.

Use m=1,M=4,L=2 in section2, alpha=1/8 and theta=1/32.
For epsilon=2^(-14), its two sufficient positivity conditions become

    24epsilon<1/512,
    1/256-8epsilon-1024epsilon^2>0.

The whole required rectangle is covered. For 0<d<=1/8 the elementary
logarithm bounds give (2/3)d^2<=C1(d)<=d^2: the logarithm argument is
1+d^2/[2(1-d^2)], so h>=d^2/(2-d^2)>=d^2/2 and
h<=d^2/[2(1-d^2)]; multiply by 2/(3/2-d).
A putative competitor with C<=C1(d) has D_total<=sqrt(3C)<=2d.
If d<=1/16 then A>=3/8, and (3) gives

    T<=2D_total/A+D_total<13d.

Consequently d_*=2^(-18) ensures d,T<=epsilon. This supplies a fixed-success
certificate throughout 0<d<=d_*.

Let eta=d_*^2/16=2^(-40). K2485's independent global bound at S=1/2 is
p<=2/3+sqrt(2C). For p>2/3 and C<=eta,

    d=3(p-2/3)/(2p)<=9sqrt(2C)/4<d_*,
    eta<C1(d_*).

So every finite schedule of cost at most eta lies below the one-stage curve.
K2493 proves that the one-stage cost C_S(p) is increasing and strictly convex
above p0; its inverse f is concave, and f(K)-K f'(K)>=p0. This existing
convexity avoids an unquantified concavity neighborhood in this corollary.
On 0<d<=1/8, h<=d^2, h_x<=4d and p<=1, so

    C1'(d)=2p^2 h+2p h_x<9d,     p'(d)>=4/9.

Since K=C1(d)>=(2/3)d^2, we obtain

    f'(K)>=8/[243sqrt(K)]>1/[32sqrt(K)].

For 0<K<=eta^2/256=2^(-88), the global tangent obeys
ell_K(eta)>=2/3+eta f'(K)>=2/3+1/2>1. The exact same finite-mixture
and all-policy transfer as section4 proves (12). All constants are sufficient
bounds; no assertion that the transition is remotely this small is licensed.
K=1/1000 and the exact optimality endpoint remain unresolved.

## 7. Controls and remaining frontier

The probe independently differentiates the original logarithmic cost, checks
(4)--(6) with multiple positive-hazard satellites in varied orders, checks
rational derivative conditions on a stated S=1/2 rectangle, and symbolically
verifies (10)--(11) and the coefficient in (2). Finite examples test the
instrument; uniformity rests on the proofs of sections2--4. Contrary controls
show why fixed success, the quadratic satellite penalty, actual survival
weights and the expensive-component tangent tail cannot be omitted. K2493's
actual strict multistage witness prevents global extrapolation. No sampled
optimizer is accepted as a proof.

The substantial next target is a useful sharp lower bound on K_S, the first
loss of one-stage optimality, or a hybrid finite-atom/continuous-stage Bellman
certificate at nonlocal budgets. The explicit interval certifies only the stated tiny range; it does not
locate the transition or settle K=1/1000. A second scientific line is to sharpen K2500's original
recorded-output leakage dependence or supply physical calibration data. Native
matter/light, full ordinary multivariable hook inversion, common-bar/mobile,
thermal163/164 and native2+1/chirality keep their existing scope and priority
comparison; no native physics conclusion follows from this stopping theorem.


[Exact probe](../../tests/channel-swings/k2501_collective_stopping_satellites_probe.py) and [saved report](../../lab/process/k2501-collective-stopping-satellites.json).
