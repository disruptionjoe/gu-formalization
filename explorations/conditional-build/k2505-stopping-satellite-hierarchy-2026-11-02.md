---
title: "K2505 A strict satellite hierarchy and certified fragmentation threshold"
status: active_research
doc_type: exploration
created: "2026-11-02"
classification: CONVENTIONAL_COMPARATOR
target_claim: "NONE-NOT-A-KILL"
claim_ceiling: "conditional supplied-model mathematics; no native GU realization, experimental certification or global stopping optimum"
---

# K2505 A strict satellite hierarchy and certified fragmentation threshold

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
result: K2505
carrier: original fresh fair test/use stopping law at score S=1/2 LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert trace or original failure-inclusive probability cost ON=declared_carrier
real_structure: complex adjoint for effects; real probabilities for stopping
grading: original verifier sectors or finite stopping stages
action_owner: repository-construction -- supplied instruments and original probability law
target: original-cost finite-stage fragmentation, onset-local hierarchy and hybrid limiting family MAP-TYPE=evaluation
```

## Result and scope

K2503's optimizing one-satellite branch is a local minimum only inside its
fixed two-stage family. Splitting the satellite supplies a strictly better
hierarchy of finite policies near onset. More strongly, any stage with score
0<b<=1/100 and hazard/score ratio2/5<=a/b<=9/20 can be replaced by two
admissible stages with the same success and strictly smaller original expected
cost, wherever it occurs in a finite schedule. The uniform threshold is proved
by an exact whole-rectangle polynomial certificate.

An explicit three-stage policy also improves K2503's finite witness while
keeping success3/4, and an exact hybrid atom-plus-microstage limit describes
the equal-ratio hierarchy. None of these results identifies the unrestricted
optimum, establishes global nonattainment, or settles K=1/1000. A tempting
stronger unweighted merging certificate is explicitly false before the local
directional threshold; that failure is not itself a cheaper original policy.

These are GU-independent supplied-model results. SC-META-53 remains UNCERTAIN;
LT-SM8/LT-GR6b and native matter/light/domain obligations do not move. Source
polarities, ledger0.263 and physical credit remain unchanged. No external-expert,
proof-assistant or novelty certification is claimed.

## 1. Original cost and a success-preserving split

For original finite schedules use K2485/K2503 notation

    0<=a_i<=b_i, sum b_i=S,
    p=product_i(1+a_i)^(-1),
    C=2 sum_i P_i w(a_i,b_i), P_i=product_(j<=i)(1+a_j)^(-1),
    w(a,b)=log(1+(b-a)^2/[2(a+b)(2-a-b)]).

At (a,b)=(0,0), set w=0 by continuity on the admissible cone. For a stage
(a,b)=(rb,b), replace it by two equal-score stages

    (q,b/2),(q,b/2), q=sqrt(1+rb)-1.

Since(1+q)^2=1+rb and q<=rb/2<=b/2, both stages are admissible. Total
score, total success and every downstream survival weight remain exactly
unchanged. If P_before is the original survival before this stage, the cost
change equals P_before times

    Delta_split=2[(2+q)w(q,b/2)-w(rb,b)]/(1+rb).        (1)

The prefix multiplier is positive for finite schedules. It is essential to
preserve the product survival, not merely the sum of hazards.

Put

    g(r)=(1-r)^2/[2(1+r)],
    c(r)=(1-r)^2/8-(1-r)^4/[32(1+r)^2],
    J(r)=(-3+22r^2-16r^3-3r^4)/[16(1+r)^2].            (2)

The analytic expansion w(rb,b)=g(r)b/2+c(r)b^2+O(b^3), together with
q=rb/2-r^2b^2/8+O(b^3), gives

    Delta_split=(J(r)/2)b^2+O(b^3).

Explicitly its quadratic coefficient is -c-r^2g'/4+rg/4=J/2. Omitting the
hazard correction changes this coefficient. The compact interval below has
J<0, but we next prove a finite threshold rather than relying on asymptotics.

## 2. Exact whole-interval fragmentation certificate

Parameterize a=q(2+q), b=a/r, and set

    x_o=(b-a)^2/[2(a+b)(2-a-b)],
    x_s=(b/2-q)^2/[2(q+b/2)(2-q-b/2)],
    lo4(x)=x-x^2/2+x^3/3-x^4/4,
    hi3(x)=x-x^2/2+x^3/3.

For all x>=0, integral remainders give lo4(x)<=log(1+x)<=hi3(x).
Therefore D=lo4(x_o)-(2+q)hi3(x_s)>0 suffices for (1)<0.
Both x values are nonnegative on

    0<q<=1/200, 2/5<=r<=9/20.

The exact probe forms and cancels this rational expression. With

    H=192(r+1)^4(q+2r+2)^3(4r-q^2-2qr-2q)^3
          *[2r-(r+1)q(q+2)]^4,

it obtains the polynomial P=H D/q^2, of degrees16 in q and14 in r. H is
strictly positive on the entire closed rectangle: the two bracketed factors
are positive even at q=1/200,r endpoints, as follows directly from
q^2+2q(r+1)<=1/40000+29/2000<8/5 and
(r+1)q(q+2)<=29*401/800000<4/5.

Substitute q=y/200, r=2/5+x/20. If P=sum c_kl x^k y^l, its tensor
Bernstein coefficients of degrees(14,16) are

    B_ij=sum_(k<=i,l<=j) c_kl binom(i,k)/binom(14,k)
                                  *binom(j,l)/binom(16,l).

The probe reconstructs all255 coefficients using exact rational arithmetic.
Every coefficient is positive, with minimum

    73262028865500189/50000000000000 >0.                (3)

Bernstein basis weights are nonnegative and sum to1 throughout[0,1]^2;
thus P>0 there. This is a finite certificate for the whole continuum, not
point sampling. The recipe, rational expression, normalization and minimum
are executable; the expanded polynomial need not be copied as prose.
An independent rational-polynomial implementation with denominator8H yielded
exactly eight times the minimum and the same255 positive signs.

For any0<b<=1/100 and r in the box, q=sqrt(1+rb)-1<=rb/2<=1/200.
Equations(1)--(3) prove a strict cheaper split at the same success. Hence no
finite schedule containing such a stage can attain the unrestricted finite-
schedule optimum. This is a local structural exclusion; a remote finite
optimizer with no such stage is not excluded. Splitting can change the ratio
and need not remain inside this box indefinitely.

## 3. The onset-local hierarchy

Use K2503's unique directional root d0 in(4/25,17/100), with a=1/2-d,
L=1+a, p=1/L, M=4Ld/[(1-d^2)(2-d^2)]+2w(a,1/2). At d0 its optimal
suffix ratio r0=2/sqrt(1+2M0)-1 belongs to(2/5,9/20). The minimum first
variation vanishes there. Write alpha>0 for minus its derivative in d and
beta1 for the t^2 coefficient of the one-satellite exact fixed-success cost.
K2503 proves beta1>1/67 and positive ratio curvature.

For n identical satellites(a_i,b_i)=(rt/n,t/n), put

    z_n=(1+rt/n)^n,
    a_main=L/z_n-1, b_main=1/2-t.

The main plus n satellites has score1/2 and success exactly1/L. It is
feasible in a common sufficiently small t-neighborhood of the root, since
z_n<=exp(rt), initial a_main>0 and b_main-a_main>0 uniformly there. Its
original cost is

    C_n=2/L [z_n w(L/z_n-1,1/2-t)
        +w(rt/n,t/n) sum_(j=0)^(n-1)(1+rt/n)^j].       (4)

Expand at fixed d,r and then evaluate at(d0,r0). The linear coefficient D1
is independent of n. At the root the quadratic coefficient is

    beta_n=beta1+p0(1-1/n)J(r0).                       (5)

For clarity, z_n=1+rt+r^2(1-1/n)t^2/2+O(t^3). The derivative of the main
bracket with respect to z at z=1 is w-Lw_a=M/2. Its extra second-order
contribution is Mr^2(1-1/n)/4. The satellites contribute
rg(1-1/n)/4+c/n inside the bracket. Multiplying by2/L and using
M0=-g'(r0) proves(5). Both the changed main hazard and survival weights
are necessary. These expansions are for fixed finite n unless explicitly
stated otherwise below.

Let P_J=-3+22r^2-16r^3-3r^4. Its derivative4r(11-12r-3r^2) is positive
on[2/5,9/20], and endpoint values are-363/625 and-20163/160000. Hence

    -363/19600<=J(r)<0,
    beta_infinity=beta1+p0 J(r0)
       >1/67-363/26068=1747/1746556>1/1000.            (6)

Here p0<100/133. Every beta_n is positive and strictly decreases with n.
K2503's desingularized stationary-equation Jacobian remains invertible for
each fixed n: its diagonal entries are2beta_n and gamma>0, with upper-right
entry0. The implicit-function theorem gives a local minimizing branch with

    t_n=alpha(d-d0)/(2beta_n)+O((d-d0)^2),
    C_n,optimized-C_single=-Gamma_n(d-d0)^2+O((d-d0)^3),
    Gamma_n=alpha^2/(4beta_n).                          (7)

For each fixed pair n2>n1 the second branch costs strictly less at the same
success for sufficiently small d-d0>0. These are local minima inside their
restricted equal-ratio/equal-size families. Section2 shows their sufficiently
small satellites are still improvable in a larger policy family.

Original one-stage cost is convex in success (K2493); it remains the optimum
among mixtures of one-stage controls. Writing K0=C_single(d0), kappa=K-K0,
exact local inversion of the constructed branch gives

    P_n(K)-F_one-stage-mixtures(K)
       =Gamma_n L0^4/M0^3 * kappa^2+O(kappa^3).        (8)

Thus the leading lower-separation coefficient increases with n. Equation(8)
is not an expansion of the unrestricted frontier F_all, and neither fixed-n
local neighborhoods nor these remainders assert uniform optimality over n.

## 4. Unequal partitions and the hybrid limit

For fixed n positive weights lambda_i summing to1, choose t_i=lambda_i t
and a_i=r t_i, adjusting the main hazard by their product as in(4). Expansion
replaces(5) by

    beta(lambda)=beta1+p0 J(r0)(1-sum_i lambda_i^2).     (9)

Equal ratios make the pair terms symmetric, so the coefficient is independent
of satellite order even though higher terms need not be. Cauchy-Schwarz gives
sum lambda_i^2>=1/n. Since J<0, equal-sized satellites minimize the quadratic
coefficient among fixed-n equal-ratio partitions; refinement strictly improves
it. The infimum of these coefficients is beta_infinity and is not achieved
by any finite positive partition. This is a coefficient-level statement,
not global finite-cost nonattainment.

For arbitrary satellite ratios, the first-order contribution at the boundary
is sum_i t_i[g(r_i)+M0r_i-N0]/L0. Because g''=4/(1+r)^3>=1/2 on[0,1],

    g(r)+M0r-N0 >=(r-r0)^2/4.                          (10)

For fixed finite proportions/ratios, any nonzero weighted deviation from r0
therefore incurs a positive first-order penalty. Extending a sharp optimal
coefficient claim to varying ratios and unbounded stage counts would require
uniform remainder control; it is not supplied by(10) alone.

The equal-ratio cost formula has an exact limit for fixed d,t>0 and 0<r<=1 with
0<=L exp(-rt)-1<1/2-t and the original main-stage denominators nonzero:

    C_infinity=2/L [exp(rt)w(L exp(-rt)-1,1/2-t)
                     +g(r)(exp(rt)-1)/(2r)].           (11)

Indeed the geometric sum in(4) is(z_n-1)n/(rt), and
n w(rt/n,t/n)->g(r)t/2. Log bounds give
0<=exp(rt)-z_n<=exp(rt)r^2t^2/(2n). The analytic removable extension of
w(rb,b)/b gives the other O(1/n) term, uniformly on compact sets with a strictly positive upper-feasibility margin,
r bounded away from0 and main-stage denominators bounded away from0.
Thus sufficiently large finite admissible schedules approximate(11) with exact
score and success. The strict upper-feasibility margin matters: if
L=(7/5)exp(1/25),t=1/10,r=2/5, the limiting main stage has a=b=2/5,
but z_n<exp(rt) makes every finite main hazard exceed b. Analytic convergence
at such a boundary does not prove admissible approximation.
The limiting construction retains a finite main atom and a distributed suffix;
it is distinct from the continuum-only model considered in K2495. We do not
assume an infinite number of tests is operationally admissible.

## 5. A cheaper exact finite witness

Take, in order,

    main: (1934773/5905227,49/100),
    satellite1= satellite2: (3/1400,1/200).              (12)

Score is1/2 and product survival is exactly3/4. Exact alternating logarithm
bounds of orders8 and9 give

    C_new <106307/5000000=0.0212614,
    C_old-C_new >3929/10^10,                            (13)

where C_old is K2503's main(691/2109,49/100), suffix(3/700,1/100)
policy. The decimal is an exact rational budget, not a rounded numerical
certificate. This improvement adjusts the main hazard to preserve success;
it is a member of(4) rather than the stagewise survival-preserving split(1).

The one-stage cost at success3/4 is(3/2)log(71/70)>=417/19600. At
K_new=106307/5000000 this leaves a strictly positive gap. As in K2503,
convexity and C_single'(3/4)<1/2 imply

    F_one-stage-mixtures(K_new)
       <=3/4-2(417/19600-K_new)<3/4.                   (14)

Thus the finite policy strictly beats every one-stage mixture at this lower
budget. This still does not locate the first global transition.

## 6. Failed stronger certificate and next frontier

One tempting all-stage proof would use C>=2p sum w and then try

    sum w(a_i,b_i)>=w(product(1+a_i)-1,sum b_i).

It is false. The exact pair

    (a1,b1)=(153/5000,3/50),
    (a2,b2)=(1547/5153,11/25)

has score1/2 and effective hazard17/50, deficiency4/25<d0. For
R(a,b)=exp(w(a,b)), exact rational arithmetic gives
R(a1,b1)R(a2,b2)<R(17/50,1/2). This refutes the proposed merging
inequality; it does not refute the one-stage original cost at that success,
because replacing every P_i by terminal p discarded prefix cost.

Small-deficiency finite scans are diagnostic only and cannot establish an
all-length merge order. K2501's exact tiny-budget result survives; the global
answer at K=1/1000 remains open. A next certificate must retain prefix weights
or supply a valid restricted merge theorem/Bellman supersolution. Near onset,
the finite-main/distributed-tail model(11), varying-ratio tails and remote
finite competitors must be compared before any global-optimum claim.

Universal claims rest on the displayed algebra, positivity of all255 exact
Bernstein coefficients, original-law log enclosures and local analytic
arguments. Symbolic/rational controls test those seams; finite examples do
not prove global policy optimality or native physics.


[Exact probe](../../tests/channel-swings/k2505_stopping_satellite_hierarchy_probe.py) and [saved report](../../lab/process/k2505-stopping-satellite-hierarchy.json).
