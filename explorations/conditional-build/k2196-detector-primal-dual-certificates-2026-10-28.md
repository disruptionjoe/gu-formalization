---
title: "K2196 Effective rational detector dual certificates"
status: active_research
doc_type: exploration
created: "2026-10-28"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied positive free-field binary diagonal instrument, arbitrary feasible signed contrast and threshold, vacuum output field energy only
scripts:
  - tests/channel-swings/k2196_detector_primal_dual_certificates_probe.py
---

# K2196 Effective rational detector dual certificates

> **GU-COMPARATOR-ROUTING: scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

```gu-typed-objects
result: K2196 explicit finite dual cutoff and rational mesh error bounds
carrier: fixed positive scalar Fock vacuum and photon-added signal with binary diagonal local occupation effects LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert form and free vacuum output energy ON=declared_carrier
real_structure: positive square-root diagonal Kraus followed by one real squeeze per reported outcome
grading: occupation number, not source ambient chirality
action_owner: repository-construction: supplied free Hamiltonian and instrument class
target: finite-budget lower energy envelope and inverse contrast bound MAP-TYPE=intertwiner
```

## Result and scope

For fixed positive **rational** squeezes s1,s0 and rational interior contrast
0<|d|<3/4, the infinite detector minimum admits a finite, entirely rational
lower certificate with an explicit cutoff and mesh error bound. A finite
bounded search over rational edge slopes and a contrast multiplier can reach
any prescribed positive rational lower-error tolerance. This is a termination
proof, not a practical complexity bound or a convergence guarantee for shooting.

[K2176](k2176-detector-certified-convergence-2026-10-27.md) already proved the
attained AM-GM dual, rational-reference completeness, exact gap decomposition
and a 61-rectangle global half-contrast bracket. Those are inherited. The new
step is an explicit uniform bound on the optimal dual slopes and multiplier,
with geometric cutoff error and rational mesh error. Free positive edge slopes
need not be the ratios of any feasible reference. Consequently lower-bound
verification uses rational arithmetic alone.

As a concrete implementation check, the probe converts K2176's 61 supplied
reference profiles to rational edge slopes and verifies its entire squeeze
cover again. It retains 0.83103<E_min(1/2)<0.831205; this is a new verifier of
an inherited bracket, **not a sharper optimum or new independent physics evidence**.
The existing upper witness and squeeze Taylor theorem are reused by dependency.

The object is the supplied positive Fock, binary diagonal square-root Kraus
instrument and one squeeze per outcome. Cost is vacuum output FIELD energy;
apparatus, preparation, clock, reset and total work remain outside the model.
SC-META-53 remains UNCERTAIN. Source, ledger0.263, LT-SM8/LT-GR6b, canon and GU
physical quotient are unchanged. No novelty, joint uniqueness, proof-assistant
or external-expert claim.

## 1. Free-edge affine minorants

Use the energy and p_n=(3/4)4^-n,q_n=3n-1 of K2194, with C=40/3 and
A(s)=41s²/6+3/(2s²). Choose arbitrary positive rational u_(j,n), j=1,0,
for n<N; put u_(j,n)=1/2 for n>=N. For z1=x and z0=p-x,

    sqrt(z_n z_(n+1)) <= (u_n z_n+z_(n+1)/u_n)/2.

Define, omitting the backward term at n=0,

    b_(j,n)=Cs_j/2 [(n+1)u_(j,n)+n/u_(j,n-1)],
    a_n=(n+1/2)(A(s1)-A(s0))-b_(1,n)+b_(0,n),
    K=35/18+(5/6)A(s0)-sum p_n b_(0,n).

Then E(x)>=K+sum a_n x_n. For any rational eta the exact contrast constraint gives

    D=K+eta*d+sum p_n min(a_n-eta q_n,0) <= E*(d;s1,s0). (1)

Caps suffice; no feasibility, stationarity, cap margin or shooting claim is
needed for the chosen u or eta. Positive slopes and a convergent tail are
essential. A malformed negative slope is rejected, not analytically continued.

For n>=N+1 the residual is alpha*n+beta, where

    alpha=ΔA-5CΔs/4-3eta, beta=ΔA/2-CΔs/4+eta.

There is at most one sign crossing, found by exact floor/ceiling arithmetic.
Infinite negative-part sums are exact using

    sum_(n>=m) p_n=4^-m,
    sum_(n>=m) n p_n=(m+1/3)4^-m.               (2)

The junction n=N is evaluated separately with its incoming chosen slope.
This is the reason a finite certificate covers every occupation, including
singular competitors touching caps.

## 2. Explicit multiplier and slope bounds

For fixed squeezes let

    delta=3/4-|d|>0, smax=max(s1,s0), smin=min(s1,s0),
    W=(5/6)|A(s1)-A(s0)|+(2C/3)smax, J=W/delta,
    M=4C smax+|ΔA|+3J.                         (3)

The energy oscillation over the whole effect box is at most W:
R(x)+R(y)=5/6 and 0<=T(x)+T(y)<=T(p)=2/3. The convex fixed-squeeze
value has subgradient eta at d: absolute gradient summability extends the
K2188/K2194 support inequality to any cap competitor y of contrast c, giving
E(y)>=E(x*)+eta(c-d). Taking its infimum proves the subgradient assertion. Comparison with both feasible endpoints ±3/4 gives |eta|<=J.
Zero contrast and the endpoint are outside this quantitative theorem.

At each n at least one branch is >=p_n/2. Its geometric-mean gradient is
at most [n sqrt(8)+(n+1)/sqrt(2)]/2 <=2(n+1). The stationary difference
b1-b0=(n+1/2)ΔA-eta q_n therefore gives

    0<=b1_n+b0_n<=M(n+1).                      (4)

At optimal tangent slopes u*_(j,n)=sqrt(z*_(j,n+1)/z*_(j,n)), positivity of
each summand in b implies

    a <= u*_(j,n) <= b,
    a=C smin/(4M), b=2M/(C smin).               (5)

Indeed b_(j,n)>=Cs_j(n+1)u*/2 supplies the upper bound; the incoming
contribution to b_(j,n+1), and (n+2)/(n+1)<=2, supply the lower bound.
These are uniform in occupation n, not uniform margins of e away from0 or1.
They coexist with K2194's polarized optimizer tail.

## 3. Cutoff and rational mesh theorem

Keep optimal slopes on n<N and replace edges n>=N by1/2. The discarded
optimal tangent tail is bounded by M sum_(n>=N)(n+1)p_n. The replacement
tail is at most C(s1+s0)/2 times the same sum. Both are nonnegative, and
summing over the effect box proves that the two affine minorants differ by at
most

    R_N=[M+C(s1+s0)/2](N+4/3)4^-N.             (6)

Taking the infimum of a perturbed affine functional over caps and the
contrast constraint, or its dual at the same eta, changes the lower value by at most
this uniform difference. The untruncated optimal tangent attains E*, so
D_N>=E*-R_N. This error estimate requires no finite-n asymptotic-tail prefactor.

Round each of the 2N retained slopes to a positive rational within h<a/2
of its true value, keeping it in [a/2,b+a/2]. For such u,v,
|1/u-1/v|<=4h/a². The uniform affine functional perturbation is bounded by

    P h, P=(2C/3)(s1+s0)(1+1/a²).           (7)

Here sum(n+1)p_n=4/3 and p_(n+1)=p_n/4. Round eta in[-J,J] to within
h_eta (a finite rational grid may include endpoints). Since sum p_n|q_n|=3/2,
its contribution to (1) changes by at most (|d|+3/2)h_eta. Thus one member of
the finite bounded rational grid satisfies

    E*-[R_N+P h+(|d|+3/2)h_eta] <= D <= E*.    (8)

For any rational epsilon>0 choose N with R_N<epsilon/3, rational
h<min(a/2,epsilon/(3P)) and h_eta<epsilon/(3(|d|+3/2)). Explicit finite
ceil/floor grids cover the bounded intervals, including their endpoints.
The maximum of their exactly computed D values is an epsilon-accurate lower
approximation. No unknown optimizing parameters enter the cutoff/mesh choices.
The grid can be enormous: this removes an effectiveness gap, not the cost of
optimization. It does not prove an efficient search, uniqueness of joint
squeezes, or a finite shooting trajectory's infinite feasibility.

## 4. Consumers and actual verification

A cap-feasible rational constant-tail profile gives an upper bound after
solving its zeroth effect from exact contrast. Its energy involves finitely
many square roots and an exact geometric tail; directed rational square-root
enclosures suffice. This primal construction and its completeness are inherited
from K2176/K2180. Together with (8), enumeration can stop on an observed
primal-dual gap. Practical numerical scouting may propose witnesses, but the
verifier accepts only the resulting exact data and proved inequalities.

For joint squeezes reuse the compact interval [2/3,113/100] and K2176's
stationary Taylor correction: a rectangle of half-widths r1,r0 containing a
global minimizer is lower-bounded by its center dual minus

    (2843/48)(5/6)max(r1²,r0²)/2.

This statement uses stationarity at the actual global minimizer, not a claimed
second derivative bound on the minimized frontier. The new rational-slope
verifier applies it to the inherited exact61-rectangle cover. The report stores
all rational slopes, full-tail lower values and exact old-input hashes.
The old upper witness is reused. Neither a fixed-squeeze numerical experiment
nor inherited rectangles are labeled a newly discovered global optimum.

The exact probe checks tail sums and sign crossings, a known constant-profile
AM-GM equality, the actual rationalized61-cell certificate, multiplier/mesh
constants and cutoff consumers at several contrasts/tolerances, then genuine
coefficient, junction, slope, contrast and covering faults after a green baseline.
Universal bounds (3)--(8) are written proofs independently reviewed; finite
controls and reproducibility hashes do not replace them.

## Next question

An efficient certified optimizer can exploit K2194 monotonicity and the new
bounded slope interface, instead of enumerating an exponential grid. A priori
uniform profile-error coercivity, a practical whole-tail shooting region and
joint optimizer uniqueness remain open. Further decimal tightening alone is
not the scientific payoff. Stable apparatus/preparation/reset accounting and
the source-native physical quotient remain separate constructions.
