---
title: "K2005: Exact coupled nonlinear potentials at the actual wing corner"
status: active_research
doc_type: exploration
created: "2026-10-24"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no source identification, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k2005_coupled_wing_potentials.py
  - tests/channel-swings/k2005_coupled_wing_potentials_probe.py
---

# K2005: Exact coupled nonlinear potentials at the actual wing corner

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: exact convergent coupled corner potentials, simultaneous actual inner traces, finite-approximation residual and global restriction obstruction
carrier: actual K1991 left wing in the width9 scalar characteristic strip LAYER=toy CHIRALITY=N/A
pairing: Lebesgue row masses and terminal column deficits ON=actual_wing
real_structure: real measurable h in [0,1], with physical pulse v=(23/100)(2h-1)
grading: analytic series order and characteristic coordinates, not source chirality
action_owner: repository-construction -- unchanged conditional scalar transport problem
target: constructive actual corner matching and precise global extension boundary MAP-TYPE=intertwiner
```

## Result and specialist opening

[K2003](k2003-exact-central-pulse-optimizer-2026-10-23.md) solved the central
optimizer but supplied only a LINEAR corner model for the wings. Its row-only
quadratic repair failed columns. Here both potentials change together: an
explicit positive entire series and its integral transform give a clipped
kernel with EXACT quadratic row masses and EXACT linear column deficits on
the positive half-plane. Restricting it to the ACTUAL wing preserves BOTH
families of constraints on explicitly certified terminal neighborhoods:

    rows 0<s<1/55000,       columns 0<delta<1/2500.       (1)

These are simultaneous full actual row and column integrals, not traces of
different auxiliary rectangles or formal series. Outside these neighborhoods
the wing constraints are not claimed. In fact the globally monotone restriction
provably fails the full wing problem. The nonlinear corner has been constructed;
global matching and global dual attainment remain open.

Opening object audit: use the exact algebraic phase and forced-support
factorization of [K1991](k1991-tight-cut-pulse-factorization-2026-10-23.md).
The scalar characteristic pulse, its L2 secondary cost and its already optimal
phase energy are distinct objects. This is no new source pairing, physical
quotient or quantum-domain construction. No L1--L7 substrate candidate is
introduced. The decisive question is whether correcting the quadratic row
term necessarily spoils columns; the coupled construction answers no locally,
without repeating the central optimizer or assuming global dual attainment.

## 1. Actual corner and a necessary endpoint singularity

Keep K1969's root t in (9/20,23/50) of

    101t^4-102t^3-168t^2+392t-138=0.

Set M=23/100, L=3-t, W=3+4t, kappa=W/(2t), eta=lambda/(2M),
where lambda=D(t)/K(t),

    D(t)=-7/100+69t/200-77t^2/200,
    K(t)=1/6-t^2/2+2t^3/3-t^4/4.

The inherited exact phase has 3/50<lambda<7/100. Thus eta>0 and
eta<4/25. In K1991 coordinates put s=L-x and delta=2L-y. The actual wing is

    Omega={(s,delta):0<s<L, 0<delta<L+s}.

Writing h=(q+1)/2, the required row mass is

    H(s)=kappa*s+eta*s^2                 for 0<s<1-t,     (2)

and the required terminal column deficit is

    int_0^L [1-h(s,delta)]ds=delta/2     for 0<delta<L.   (3)

The rest of the actual phase is not replaced by (2). The half-plane extension
of (2) below is an auxiliary exact construction whose actual trace scope is
proved separately.

**Endpoint theorem.** If a feasible actual wing has a representation

    h(s,delta)=clip_[0,1](A(s)-B(delta))                  (4)

with finite measurable potentials almost everywhere, then A(s) tends to
minus infinity as s tends to zero and B(delta) tends to minus infinity as
delta tends to zero, in the essential sense. No monotonicity, continuity,
dual attainment or endpoint representatives are assumed.

Proof: suppose m=ess inf_(0,L) A is finite. For epsilon in (0,1/4), the set
E={A<m+epsilon} has positive measure. If B(delta)>=m-1+2epsilon, the
column deficit is at least epsilon*|E|. Equation (3) therefore gives
B(delta)<m-1+2epsilon for almost every sufficiently small delta. Since
A>=m almost everywhere, every sufficiently terminal row then has mass at
least (1-2epsilon) times a fixed positive delta interval. This contradicts
H(s)->0. Thus ess inf A=-infinity.

For any positive integer N, E_N={A<-N} has positive measure. If
B(delta)>=-N-1/2, its deficit is at least |E_N|/2. Equation (3) implies
B(delta)<-N-1/2 almost everywhere sufficiently close to zero. This proves
the essential limit for B. Given N, choose a fixed positive delta interval
where B<-N-1. Any row with A(s)>=-N then has h=1 on that interval, again
contradicting H(s)->0. This proves the essential limit for A. Fubini permits
all statements on common full-measure sets; null endpoint values do not matter.

In the conventional additive notation A(s)+C(delta), the column potential
C=-B diverges positively. This is a necessary feature of any such global
representation, not proof that a global representation or attained dual exists.

## 2. Positive coefficients and an entire nonlinear eigenfunction

Let r>0 be the unique solution of

    Lambda_1=4(cosh(r)-1)/r^2=kappa.                     (5)

Equivalently r=1/c in K2003's logarithmic model. The function in (5) is
strictly increasing from 2 to infinity: it is
2[sinh(r/2)/(r/2)]^2, and the derivative of z cosh(z)-sinh(z) is
z sinh(z)>0. Exact rational exponential bounds give 3<r<4 and
20<q:=exp(r)<55. Put

    Lambda_n=4(cosh(nr)-1)/(nr)^2,
    Delta=Lambda_2-kappa,
    c_1=1,
    c_n=eta/(Lambda_n-kappa) sum_(i=1)^(n-1)c_i c_(n-i), n>=2. (6)

Every denominator is positive. Since Lambda_n is increasing in n and
Delta=kappa*sinh(r/2)^2>20, induction against the Catalan recurrence gives

    0<c_n<=Catalan_(n-1)(eta/Delta)^(n-1)
          <= Catalan_(n-1)/125^(n-1)
          <=(4/125)^(n-1).                              (7)

The weak inequality on the middle line includes n=1; for n>1 it is strict.
Define S(z)=sum_(n>=1)c_n z^n. Equation (7) first gives a positive radius
of convergence. In fact **S is entire**. If its radius R were positive and
finite, S(z)^2 would have radius at least R. The nth root of
Lambda_n-kappa tends to q>1. By (6) and Cauchy--Hadamard, the coefficients
of S would consequently have radius at least qR>R, a contradiction. The
initial linear coefficient does not affect any radius. This argument proves
analytic convergence; it is not a claim that an arbitrary formal solution
converges.

Let

    D(z)=2 sum_(n>=1)c_n(q^n-1)z^n/(nr).                (8)

This is also entire, since its coefficient nth-root differs from that of S
by a factor tending to q. Both S and D are strictly increasing bijections
from [0,infinity) to [0,infinity): their coefficients are positive, their
derivatives are positive, and their linear terms tend to infinity with z.
Hence their positive real inverses are unambiguous.

Equivalently, with script-S(a)=S(exp(ra)), equations (6) solve exactly

    2 int_-1^1 (1-|u|) script-S(a+u)du
         =kappa*script-S(a)+eta*script-S(a)^2.           (9)

The spectral multiplier of the triangular convolution is Lambda_n. Uniform
convergence on every compact interval justifies integrating each exponential
term. Equation (9) is the nonlinear coupled replacement for K2003's linear
homogeneous boundary equation.

## 3. Exact inverse potentials and BOTH half-plane marginals

For s,delta>0 define

    A(s)=log(S^(-1)(s))/r,
    B(delta)=log(D^(-1)(delta))/r,
    h_*(s,delta)=clip_[0,1](A(s)-B(delta)).               (10)

Here S^(-1),D^(-1) mean inverse functions, not reciprocal values. Both
potentials are finite in the open quadrant. At zero they have logarithmic
divergence; on every finite interval they belong to L2. This follows from
S(z)=z+O(z^2) and D(z)=d_1z+O(z^2), where d_1=2(q-1)/r>0.

Layer-cake integration makes the two constraints transparent. For fixed
s=S(z), h_*>v is equivalent to delta<D(z exp(-rv)), for 0<v<1.
Tonelli and (8) therefore give

    int_0^infinity h_*(s,delta)d delta
      =int_0^1 D(z exp(-rv))dv
      =sum_(n>=1)Lambda_n c_n z^n
      =kappa*S(z)+eta*S(z)^2.                           (11)

For fixed delta=D(w), 1-h_*>v is equivalent, up to changing v to 1-v,
to s<S(w exp(rv)). Thus

    int_0^infinity [1-h_*(s,delta)]ds
      =int_0^1 S(w exp(rv))dv=D(w)/2=delta/2.            (12)

All integrands are nonnegative and each row or deficit has finite support:

    row support:     delta<D(S^(-1)(s)),
    deficit support: s<S(q D^(-1)(delta)).               (13)

Consequently (11)--(12) are genuine finite-valued integrals at every positive
coordinate, not formal coefficient identities or differences of two divergent
integrals. They solve the auxiliary quadratic half-plane problem exactly.

## 4. Simultaneous actual wing traces with rational neighborhoods

Set z0=1/1000, s0=S(z0), d0=D(z0/q). From (7),

    s0<=z0/(1-4z0/125)<1/999<L,
    d0<(2/r)S(z0)<2/(3*999)<L,
    S(z0/q)>z0/q>1/55000,
    d0>2(1-1/q)z0/r>19/40000>1/2500.                 (14)

For any 0<s<S(z0/q), monotonicity gives the row support in (13) less
than d0<L+s. The actual finite row therefore contains its entire half-plane
support. Provided s<1-t, (11) equals the ACTUAL row mass (2).
For any 0<delta<d0, the deficit support is less than s0<L. Since delta<L,
the actual terminal column spans all 0<s<L, and (12) gives its exact actual
deficit (3). Since 1/55000<1-t, these two statements give precisely (1).

The SAME kernel restricted to Omega supplies both families. Neither family
uses an independent extension, and no artificial rectangle is identified with
the physical row/column domain. The intervals are conservative certified
neighborhoods, not maximal validity thresholds.

## 5. Finite evaluation, exact finite-column law and row shortfall

Let S_N and D_N retain terms 1 through N in (6),(8). For z>=0 and
rho=4z/125<1, their tails obey

    0<=S(z)-S_N(z)<=z rho^N/(1-rho),
    0<=D(z)-D_N(z)<=(2/3)(55z)(4*55z/125)^N/(1-4*55z/125), (15)

where the second bound requires 4*55z/125<1. The certificate evaluates
the actual algebraic t, transcendental r and coefficient intervals by rational
outward bounds; no floating-point quadrature is used. Monotone bisection on
S_N,D_N with these tails certifies inverse brackets in this domain. In
particular S'>=1 and D'>=d_1, so a function-value enclosure of width epsilon
costs at most epsilon and epsilon/d_1 respectively in inverse-coordinate
width. Conversion to a logarithm requires a positive lower inverse bracket;
no uniform endpoint potential approximation is claimed.

The finite inverse-potential pulse made from S_N,D_N respects the cap and has
the half-plane column deficit EXACTLY delta/2, because (12) is already exact
for every finite polynomial. But its row mass at s=S_N(z) is

    kappa*s+eta*s^2-E_N(z),
    E_N(z)=eta sum_(n=N+1)^(2N) z^n
                   sum_(i+j=n,1<=i,j<=N)c_i c_j >0      (z>0). (16)

The low coefficients match by (6); the positive omitted high products give
the entire defect. A directly summable conservative bound is

    E_N(z)<=(4/25) z^2 rho^(N-1)
                    [N-(N-1)rho]/(1-rho)^2.            (17)

Thus finite truncation is explicitly distinguished from exact nonlinear row
feasibility. The positive series limit is the exact construction. Statements
about its finite approximants concern pulse marginals, not phase energy,
exact full plateaux, or a whole-pulse strong convergence modulus.

The first coupled correction also exposes the mechanism. With C=eta/Delta,
d_1=2(q-1)/r, and d_2=C(q^2-1)/r, (10) has the interior-potential expansion

    A(s)-B(delta)=log(d_1*s/delta)/r
                 -(C/r)s+(d_2/(r*d_1^2))delta
                 +O(s^2+delta^2).                     (18)

Both linear corrections are necessary. If a=d_1/q and b=d_1 are the
leading ramp endpoints delta=a*s,b*s, their corrections U=-C/r and
V=d_2/(r*d_1^2) satisfy

    U(b-a)+V(b^2-a^2)/2=eta,
    U(1/a^2-1/b^2)/2+V(1/a-1/b)=0.                    (19)

The first equation repairs the quadratic row term; the second keeps the
quadratic column-deficit term zero. K2003's row-only change lacks this coupled
cancellation. Equations (18)--(19) are a consumer of the convergent exact
construction, not the sole evidence for it.

## 6. Global restriction fails: a precise remaining boundary

Both inverse functions in (10) increase. For every fixed row the restricted
h_* is therefore nonincreasing in delta, equivalently nondecreasing in y.
K2003 proved that no actual feasible wing has that common direction. Its
necessary inequality at y0=1/2 is

    int_0^(1/2) H_original(x)dx >=(2L-1/2)/4.

The actual left side minus this lower bound is at most

    (L-9/2)/2+1/(8M)<-397/920.                          (20)

The producer independently encloses this strict bound at the actual root.
Therefore restricting (10) to the entire actual wing CANNOT satisfy every
required marginal. This is a scoped failure of this particular global
restriction, consistent with the exact simultaneous corner success in (1).

A successor may retain the corner construction and introduce nonmonotone
column-potential behavior away from it, or use a different global primal
construction. Local exact traces do not establish that either can be glued
to a feasible global wing; outside constraints can couple back to the corner.
There is no new whole-pulse norm bound or globally attained dual certificate.
K1980's whole-strip existence/strong limiting construction, K2003's central
optimizer, and the earlier nonsmoothness and infinite-rank results stand.

## 7. Verification and specialist close

Executed from the repository root:

```sh
_local/cas-venv/bin/python tests/channel-swings/k2005_coupled_wing_potentials.py
_local/cas-venv/bin/python tests/channel-swings/k2005_coupled_wing_potentials.py --check
_local/cas-venv/bin/python tests/channel-swings/k2005_coupled_wing_potentials_probe.py
```

The producer and exact certificate replay each pass 208 rational controls.
The independent probe passes 527 controls: 8 symbolic integral/tail identities,
444 rational identities and 75 interval-certificate checks. It imports no
producer implementation. It independently derives the triangular spectral
integral, layer-cake multipliers and finite-product defect, checks both
first-correction equations and the actual corner bounds, and verifies the
actual eta parameter by a rational derivative-sign and endpoint enclosure.

After that green baseline, four genuine mathematical corruptions are rejected:
removing the D factor two fails the exact column multiplier; losing a spectral
denominator factor fails the row multiplier; changing the nonlinear coefficient
sign (and its matching D coefficient) fails the nonlinear recurrence; omitting
a high-order finite product fails the exact row-shortfall polynomial. These
are mathematical assertion failures, not crash exits or altered checks.

Finite controls do not prove the continuum or entire-extension claims; those
are the arguments in sections 1--6. A separate internal mathematical reading
checked the endpoint theorem, radius argument, both layer-cake transfers,
actual trace cutoffs, and coupled correction. It also identified missing
independent certificate pins for eta and c1; those checks were added before
the final green replay. This is internal review, not external acceptance.

Strongest contrary case: exact half-plane construction mistaken for exact
whole-wing feasibility. Equation (20) disproves that promotion. Strongest
analytic vulnerability: assuming formal series convergence or interchanging
uncontrolled tails; (7), the radius argument, positivity, and compact uniform
convergence supply those bridges. Endpoint null sets are handled essentially,
and the endpoint theorem assumes a potential representation rather than
asserting dual attainment. The entire extension proof supplies existence
globally in the half-plane; (15) supplies an explicit evaluation modulus only
in its stated domain.

Closing scientific disposition: the actual nonlinear corner is constructively
resolved on simultaneous certified trace neighborhoods. The global wing
matching problem remains open with a sharper required shape change. No
source/native GU identification, physical-ledger verdict, canon promotion,
novelty, proof-assistant verification or external expert acceptance is claimed.
SC-META-53 remains UNCERTAIN. The proof is self-contained; it imports no new
specialized theorem beyond the explicitly used elementary power-series radius
and positive-integration facts.
