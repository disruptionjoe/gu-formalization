---
title: "K2549 Uniform stopping value and all-policy nearcritical phase"
status: active_research
doc_type: exploration
created: "2026-11-04"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied-law small-score all-policy theorem in a shrinking multiplier tube; no fixed-score global frontier, physical law or GU claim
scripts:
  - tests/channel-swings/k2549_uniform_nearcritical_stopping_bound_probe.py
---

# K2549 Arbitrarily many satellites have a sharp uniform value

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
result: K2549
carrier: finite ordered original-law stopping schedules, initial mixtures and admitted value limits LAYER=toy CHIRALITY=N/A
pairing: original failure-inclusive expected reward and prefix-weighted cost ON=declared_carrier
real_structure: real probabilities and actions; complex extension used only for analytic estimates
grading: ordered score stages; no physical or Clifford grading
action_owner: repository-construction -- supplied fresh fair test-use law of K2483 and K2485
target: uniform fifth-order value, nearcritical global phase and satellite concentration MAP-TYPE=evaluation
```

## Result and inference boundary

For the original supplied stopping law, put lambda(S)=lambda*+mu0 S+nu S²,
with nu in a fixed compact interval. The full adaptive-policy value V and
optimized one-stage value U satisfy

    V_lambda(S)(S)-U_lambda(S)(S)
       =[(gamma-2Hp nu)_+]² S^5/(4Kinf)+O(S^6).            (1)

The error is uniform over every finite stage count and every partition,
including a stage count growing with 1/S. A single main stage followed by
ceil(1/S) equal small satellites attains the displayed accuracy. This supplies
[K2547](k2547-nearcritical-satellite-instability-2026-11-04.md)'s missing upper
bound and licenses a growing-stage witness without exchanging fixed-stage
limits.

A released successor identifies the exact all-policy transition inside the
shrinking nearcritical tube: for sufficiently small S, the local insertion
curve lambda_c(S) from K2547 separates one-stage optimality from a strictly
better multistage policy. This is a global comparison over the original policy
class at each parameter in that tube, not a global curve for arbitrary scores
or multipliers. Another successor gives the score concentration and diverging
satellite count required to attain the sharp coefficient.

The law is supplied positive probability mathematics, not a derivation of a
physical probability law. SC-META-53 remains UNCERTAIN; the complete entries
LT-SM8 and LT-GR6b in ledger0.263 retain their physical quotient, interacting
action and domain debts. No source, ledger, canon, physical-recovery, empirical
or novelty claim changes. Source adherence is not physical validation.

## 1. Law, constants and reused results

Use the exact completed-schedule reduction in [K2483](k2483-adaptive-stopping-bellman-2026-11-01.md)
and [K2485](k2485-constrained-stopping-frontier-2026-11-01.md), including its
original adaptive, initial-mixture and admitted-limit scope. Dominated actions
and overshoots are removed by those proved reductions. For b_i>=0,
sum b_i=S and 0<=a_i<=b_i, the exact value is

    w(a,b)=log(1+(b-a)²/[2(a+b)(2-a-b)]),
    P_i=product_(j<=i)(1+a_j)^(-1),
    G=P_n-2lambda sum_i P_i w(a_i,b_i).

Zero-score stages are identities. Free abort has value zero and is inferior
to U near S=0. For a fixed positive score partition, stage actions are optimized
by backward composition, not by replacing prefix cost with an additive cost.

The exact inherited constants are

    lambda*=4sqrt(3)/3,  r*=2sqrt(3)-3,
    Hp=(141-81sqrt(3))/8>0,
    c1=(2841-1643sqrt(3))/48<0,
    cL=(249sqrt(3)-431)/2>0,
    Kinf=cL+c1/2=(10309sqrt(3)-17847)/96>0,
    mu0=c1/(2Hp)=37/66-257sqrt(3)/396,
    gamma=(202353685-116818417sqrt(3))/371712>0,
    nu0=gamma/(2Hp).

[K2545](k2545-critical-stopping-aggregation-2026-11-04.md) gives the optimized
cubic defect at lambda=lambda*+mu0 S:

    D(x)=-cL R(x)-2Kinf T(x),
    R=sum_(i<j)x_i x_j², T=sum_(i<j<k)x_i x_j x_k, sum x_i=1. (2)

K2547 gives the exact optimized terminal-insertion derivative L(S,lambda),
its analytic extension and expansion

    L(S,lambda(S))=(gamma-2Hp nu)S³+O(S^4),                 (3)

and the unique local analytic curve L(S,lambda_c(S))=0 with
lambda_c=lambda*+mu0 S+nu0 S²+O(S³). Its lambda derivative is negative for
small positive S. Those coefficients are reused, not recalculated as a new
finding. What was missing was dimension-independent control of optimized
compositions and all partitions; sections 2--7 supply it.

## 2. A common analytic domain for every number of stages

Write a=rb, alpha=(1-r)²/[4(1+r)], beta=(1+r)/2 and c=beta-alpha.
The identity

    w(rb,b)=log(1-cb)-log(1-beta b)

defines a holomorphic extension near b=0 and r=r*. Write w_r/b by its
holomorphic extension there. The stationary equation for suffix value Y is

    lambda M(r,b)=Y,
    M=2w-2(1+rb)w_r/b,
    M(r,0)=2/(1+r)²-1/2,
    M_r(r,0)=-4/(1+r)³.                                  (4)

The analytic implicit-function theorem gives one holomorphic rho(b,Y,lambda)
in a product neighborhood of (0,1,lambda*). On a smaller real neighborhood,
M_r<0 throughout r in [0,1], and the endpoint stationary signs remain positive
at r=0 and negative at r=1. This follows from the exact derivative in K2545,
compactness of [0,1] and its strict b=0 signs near lambda*. Therefore rho is
the unique global stage optimizer for every small nonnegative b and suffix
Y close to one; the complex extension makes no optimization claim.

Define its holomorphic stage map

    F(b,Y,lambda)=[Y-2lambda w(rho*b,b)]/(1+rho*b).

Crucially F(0,Y,lambda)=Y. Choose nested closed complex Y-discs centered at
1, and a compact complex lambda-disc around lambda*, inside the analytic
neighborhood. On them there are finite constants C and C1 such that

    |F(b,Y,lambda)-Y|<=C|b|,
    |F_Y(b,Y,lambda)-1|<=C1|b|.                            (5)

These are estimates from the exact factors b: both left differences vanish
identically at b=0. The constants do not mention a number of stages. Choose
rho0>0 so C rho0 is less than the gap between the nested Y-discs and rho0
is smaller than the permitted b-radius. Induction from the last stage proves
that, for EVERY n and complex vector with sum_i |b_i|<rho0, every suffix
stays in the larger disc, and

    H_n(b,lambda)=F(b_1,F(b_2,...F(b_n,1,lambda)...),lambda)

is holomorphic with |H_n-1|<=C sum_i|b_i|. The induction applies the first
bound in (5) and sums |b_i|; it does not accumulate a factor C^n. The second
bound also gives the useful propagated-derivative bound
product_i|F_Y|<=exp(C1 sum_i|b_i|). For real nonnegative scores this composition
is exactly the optimized original-law value for that partition.

Here is explicit dimension-independent derivative control. On the smaller
ball sum|b_i|<=rho0/2, take p complex directions h_j of l1 norm at most one,
and perturb by sum_j z_j h_j with |z_j|<=rho0/(4p). The entire polydisc stays
inside sum|b_i|<rho0. The preceding bound and multivariable Cauchy formula
bound the mixed directional derivative of order p by a constant depending
on p and rho0, but not n. Lambda derivatives are controlled on nested
lambda-discs in the same way. Thus every fixed finite derivative order has a
uniform l1 operator bound. Taylor remainders in a score perturbation h are
O(||h||_1^(p+1)), uniformly in n. This argument proves the estimates needed
below; fixed-dimensional analyticity alone would not.

## 3. Shape-sensitive cubic remainder

Let x be any finite probability vector, m=max_i x_i, k an index attaining it,
and delta=1-m. Compare H_n(Sx,lambda(S)) to H_n(S e_k,lambda(S))=U_lambda(S)(S).
The l1 distance between x and e_k is 2delta. Integrate the first derivative of
H_n along e_k+theta(x-e_k), 0<=theta<=1. The derivative estimates above make
the resulting analytic function of complex S bounded by C'|S|delta on a
common circle around zero. The analytic multiplier lambda(S) remains in its
lambda-disc there, uniformly for nu in a fixed compact interval. Cauchy's
coefficient bound therefore bounds every Taylor coefficient by a constant
multiple of delta, with a common convergent geometric majorant.

The constant, linear and quadratic differences vanish at the critical moving
multiplier. Its cubic coefficient is (2); the nu S² perturbation contributes
only at degree four to the shape difference. Consequently

    H_n(Sx,lambda(S))-U_lambda(S)(S)
          =S³D(x)+E,  |E|<=C2 S^4 delta,                 (6)

uniformly in n,x and bounded nu. It is the extra delta factor, absent from
K2545's coarse uniform O(S^4) theorem, that makes the fifth-order endpoint
accessible. No assumption about a dominant stage was used to prove (6).

## 4. Localize every possibly improving partition

Only partitions with optimized value >=U need an upper bound beyond U.
First suppose m<=1/2. Take the first prefix whose mass p crosses 1/4;
then 1/4<=p<=3/4 and its suffix mass q=1-p>=1/4. The terms of R crossing this
cut and terms of T with one prefix and two suffix entries give

    R+2T>=p[sum_suffix x_j²+2sum_suffix_(i<j)x_i x_j]
          =p q²>=1/64.

Since cL>Kinf>0, -D>=Kinf(R+2T)>=Kinf/64. Equation (6) contradicts value>=U
for sufficiently small S. Hence a possibly improving partition has a unique
largest stage m>1/2.

Let p be all mass BEFORE that stage and q all mass AFTER it; delta=p+q.
Nonnegative terms in (2) give

    -D>=cL m²p+m[Kinf q²+(cL-Kinf)sum_after x_j²]
        >=(cL/4)p+(Kinf/2)q².                            (7)

Together with (6), and absorbing C2 S p into its left side for small S,

    (cL/8)p+(Kinf/2)q²<=C2 S q.

Thus q<=2C2 S/Kinf and p<=8C2 S q/cL. In actual score units,

    P=S p=O(S³), Q=S q=O(S²).                            (8)

Both constants are uniform in the stage count. This proves that any
potentially improving schedule has a main stage first up to a much smaller
preceding mass; it does not assume terminal satellites in order to optimize
only among them. Partitions with value below U already obey the desired
all-policy upper bound.

## 5. Uniform expansion around the main stage

Hold total score S fixed. Give every preceding or following stage a satellite
score, and give the main stage S minus their sum. A satellite direction has
l1 norm two, so section 2 controls all these derivatives and their remainders
independently of their number. At zero satellite scores there are just two
first derivative types: J(S,lambda) for insertion before the main stage and
L(S,lambda) for insertion after it. Zero stages are identities, so their
positions within those two groups do not affect the first derivatives.
Differentiating the cubic coefficient (2) gives

    J(S,lambda(S))=-cL S²+O(S³).                          (9)

At S=0,lambda=lambda*, all satellite second derivatives vanish: the full
optimized quadratic polynomial is B(sum b_i)², and a satellite direction
preserves sum b_i. The uniform third-derivative bound thus makes every
second derivative O(S), including mixed preceding/following ones.

For the following-stage block the cubic polynomial gives its entire leading
quadratic form. With following scores t_j and Q=sum t_j it is

    -S[cL sum_j t_j²+2Kinf sum_(i<j)t_i t_j]
       =-S[Kinf Q²-(c1/2)sum_j t_j²].                   (10)

This follows from the two ordered triple types in R,T, not a fixed-n sample.
The remainder in this Hessian block is O(S²) in l1 operator norm. The nu
perturbation and higher coefficients are included in that bound.
Taylor expansion with the exact first derivative L therefore yields

    Delta=J P+L Q-S[Kinf Q²-(c1/2)sum_j t_j²]+Remainder,
    |Remainder|<=C3[S P(P+Q)+S²Q²+(P+Q)³].              (11)

The first error term bounds all second-order terms involving a preceding
stage; the last is the uniform third-order Taylor error. Under (8), use (3)
and (9) to obtain

    Delta=-cL S²P+k_nu S³Q
           -S[Kinf Q²-(c1/2)sum_j t_j²]+O(S^6),
    k_nu=gamma-2Hp nu.                                  (12)

The O(S^6) constant is uniform in n and the localized partitions. In particular
this is a justified growing-stage expansion, not K2547's O_m(S^6) estimate
with its subscript dropped.

## 6. Sharp value and a finite growing-stage construction

Because c1<0, both the preceding term and the diagonal cloud penalty in (12)
are nonpositive. Completing the square in Q>=0 proves

    Delta<=(k_nu)_+² S^5/(4Kinf)+O(S^6).

Every unoptimized action choice is bounded by its optimized partition value.
Together with section 4 this is a uniform upper bound for every finite
schedule. Initial mixtures preserve it by linearity; the original-law
reduction and its admitted value limits preserve the same bound for the
full adaptive supremum. Infinite expected-cost policies are not candidates
for improvement, as in K2483.

For k_nu>0 choose m=ceil(1/S), Q=k_nu S²/(2Kinf), main score S-Q, and m
following scores t_j=Q/m. For sufficiently small S these are nonnegative
and admissible. Optimize their actions by the exact backward stage map.
The uniform estimate (11) applies directly, irrespective of m(S), and
sum t_j²=Q²/m=O(S^5). Equation (12) gives the matching lower value
(k_nu)² S^5/(4Kinf)+O(S^6). For k_nu<=0 the one-stage policy gives the lower
bound zero. This proves (1), uniformly for bounded nu. Each witness has
finitely many stages; no infinite policy or exact supremum attainment is
asserted below the phase curve.

## 7. Released successor: the insertion curve is globally decisive in its tube

Fix M>|nu0| and restrict

    |lambda-lambda*-mu0 S|<=M S².                         (13)

All preceding constants are uniform there; write nu=(lambda-lambda*-mu0 S)/S².
Any potentially improving partition obeys (8). Keep L exact in (11).
For small S, J<=-(cL/2)S². Split the cubic error as
(P+Q)³<=4P(P+Q)²+4Q³. By (8), all terms containing P in the remainder are
absorbed by a fixed fraction of cL S²P. The remaining error is
O(S²Q²+Q³), absorbed by a fixed fraction of Kinf S Q², since Q=O(S²).
Consequently there are positive constants a0,b0 independent of n such that

    Delta<=L(S,lambda) Q-a0 S²P-b0 S Q².                 (14)

If L<=0, (14) is strictly negative for every nontrivial finite partition
that could have matched U. Thus U is the all-policy supremum; a one-stage
optimizer attains it. If L>0, the exact derivative of an optimized tiny
terminal insertion is positive, so an actual two-stage policy beats U.
K2547's implicit-function theorem and negative lambda derivative now give

    V=U  iff lambda>=lambda_c(S),
    V>U  iff lambda<lambda_c(S),                         (15)

within (13), for sufficiently small positive S. The iff concerns value,
not uniqueness of an arbitrary adaptive policy representation. At equality,
one stage is optimal; zero stages and value limits may give equivalent
representations. For fixed nu>nu0, exact one-stage optimality follows for
small S; for fixed nu<nu0, (1)'s strictly positive cloud advantage follows.
At nu=nu0 the uncomputed higher displacement of lambda_c(S) matters; do not
infer exact optimality merely from the vanishing fifth-order coefficient.

This upgrades the former local insertion condition through an independently
proved localization and all-policy upper bound. It does not extend (15) to
S=1/2, to multipliers outside (13), or to an arbitrary supplied cost law.

## 8. Released successor: an asymptotically optimal cloud must diffuse

Fix nu<nu0, so k_nu>0, z*=k_nu/(2Kinf) and C*=k_nu²/(4Kinf).
For a finite policy whose value is C*S^5+o(S^5) above U, its shape must obey
(8). Equation (12), with square completion, implies

    P=o(S³), Q/S² -> z*, sum_j t_j²=o(S^4).               (16)

All three deficits are nonnegative: cL S²P,
Kinf S(Q-z*S²)² and (-c1/2)S sum t_j². Hence no cancellation can conceal
one of them. In particular max_j t_j=o(S²), and the number of positive
following stages must diverge by Q²<=m sum t_j². No fixed finite satellite
count can attain the sharp fifth-order coefficient.

More quantitatively, if a finite policy is within O(S^6) of V, then

    P=O(S^4), |Q-z*S²|=O(S^(5/2)), sum_j t_j²=O(S^5),
    m=Omega(1/S).                                      (17)

The construction in section 6 has m=ceil(1/S), so this stage-count order is
both necessary for that accuracy and sufficient. These are small-score
asymptotics with unspecified constants, not an explicit finite-score resource
certificate. An unoptimized near-optimal policy inherits the shape bounds
because its optimized value is no smaller.

The deterministic statement is not a componentwise statement about an
initial mixture: a small weight on poor diffuse schedules can have negligible
expected loss. The universal value bound holds for mixtures; (16)--(17) as
written concern individual finite schedules. Mixture stability would require
an explicitly weighted defect formulation, which is not claimed here.

## 9. Released construction: a finite-stage approximation rate

The same analytic estimates also give a quantitative compression theorem on
the common small-score neighborhood. Let V_N(S,lambda) be the best value of
schedules with at most N positive-score stages. There are constants C4,S0>0,
uniform for lambda in a fixed sufficiently small real neighborhood of
lambda*, such that for 0<S<=S0 and 0<h<=S,

    V_N(S,lambda)<=V(S,lambda)<=V_N(S,lambda)+C4 S h,
    N=ceil(2S/h)+1.                                      (18)

In particular for every integer N>=3, choosing h=2S/(N-1) gives

    0<=V(S,lambda)-V_N(S,lambda)<=2C4 S²/(N-1).           (19)

The constants and S0 have not been evaluated numerically. This is a proved
uniform rate and a route to a certified finite-stage calculation, not a
numerical certificate at S=1/2.

For proof, define the exact optimized stage-merge defect with its suffix Y:

    E(b,c,Y)=F(b,F(c,Y,lambda),lambda)-F(b+c,Y,lambda).

It vanishes identically when b=0 or c=0 because F(0,Y)=Y. On smaller common
real score/suffix neighborhoods, section 2 bounds its mixed derivative, so
integration over the rectangle [0,b] x [0,c] gives

    |E(b,c,Y)|<=C5 b c.                                  (20)

The neighborhoods can be chosen so that every partial coarsening of a
schedule of total score <=S0 remains in them; every such composition has
nonnegative scores with the same total. The estimate is for the optimized
original-law F, not a surrogate or a claim that merging always improves.

Greedily collect consecutive stages into bins with total score at most h;
a stage larger than h is retained as a singleton, and any preceding small
bin is closed first. Adjacent output bins have combined score >h: either one
is a large singleton or the greedy overflow criterion applies. Pairing
adjacent bins shows that their number is at most ceil(2S/h)+1. This includes
small bins on either side of large singleton stages; it does not assume all
output bins have size >=h/2.

In a small bin of total B<=h, merge successive stages. The sum of merge
products is exactly

    sum_j (sum_(i<j)b_i)b_j=(B²-sum_i b_i²)/2<=B²/2.

Every error propagates through preceding stages by at most
product(1+C1 b_i)<=exp(C1 S), from (5), also for partially coarsened stages.
Large singleton bins have zero merge error and are EXCLUDED from the next
sum. For the small bins,

    sum_small_bins B²<=h sum_small_bins B<=h S.

The total absolute change is therefore at most
(C5/2)exp(C1 S0) h S. Starting with any finite schedule and optimizing its
actions, its compressed schedule has at most N stages and loses no more than
this amount. Taking the supremum and applying the original finite-schedule
reduction proves (18); the opposite inequality is immediate. This does not
restrict the original number of stages, exchange limits or assert an optimal
finite schedule exists. A finite-stage numerical grid still needs its OWN
continuous-control discretization bound and certified constants before it
can upper-bound the original value.

## Evidence, contrary routes and remaining work

The proof of uniformity is the common complex l1 neighborhood and Cauchy
argument in section 2. The exact probe checks the original stage stationary
formula, ordered cubic/Hessian identities, sign certificates, localization
algebra, square completion stage-count inequalities and merge-product algebra. Saved-report equality
checks reproducibility only. No numerical sampling or Boolean assertion
certifies the universal analytic claims. Independent internal review must
check the analytic neighborhood, full original-law reduction and absorption
in (14); no proof-assistant or external-expert certification is claimed.

Prior-object search found K2545's uniform cubic theorem and K2547's fixed-m
lower bound and local curve, but no matching uniform fifth-order bound or
all-policy nearcritical phase. A separate search of the K24xx/K25xx notes and
probes for coarsening, merge defects, stage compression and finite-stage
approximation found no prior version of (18). Their existing conclusions and scope remain
unchanged. The strongest contrary constructions are a growing satellite
cloud (which defeats the fixed-m optimum), a prefix satellite (penalized at
a different order), a diffuse partition (ruled out before local expansion),
and a mixture with rare poor components (which defeats componentwise
stability). The actual weakest seam is uniform analytic composition; it is
proved explicitly instead of inferred from finite-dimensional analyticity.

Next: certify an explicit real stage-root bracket and the derivative constants
in (20), then combine (18) with a continuous-control discretization bound at
a specified score. The present proof provides existence constants only; it
does not show that its neighborhood reaches S=1/2. A next Taylor coefficient
alone does not solve that endpoint. The source-native physical
carrier and joint calibration remain separate missing bridges.

[Probe](../../tests/channel-swings/k2549_uniform_nearcritical_stopping_bound_probe.py),
[report](../../lab/process/k2549-uniform-nearcritical-stopping-bound.json),
[K2547](k2547-nearcritical-satellite-instability-2026-11-04.md),
[K2545](k2545-critical-stopping-aggregation-2026-11-04.md).
