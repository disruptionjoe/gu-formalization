---
title: "K2194 Detector optimizer shape and exact shooting"
status: active_research
doc_type: exploration
created: "2026-10-28"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied positive free-field binary diagonal instrument, arbitrary feasible signed contrast and threshold, vacuum output field energy only
scripts:
  - tests/channel-swings/k2194_detector_optimizer_structure_probe.py
---

# K2194 Detector optimizer shape and exact shooting

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
result: K2194 strictly monotone optimizer, geometric tail ratio and exact shooting equivalence
carrier: fixed positive scalar Fock vacuum and photon-added signal with binary diagonal local occupation effects LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert form and free vacuum output energy ON=declared_carrier
real_structure: positive square-root diagonal Kraus followed by one real squeeze per reported outcome
grading: occupation number, not source ambient chirality
action_owner: repository-construction: supplied free Hamiltonian and instrument class
target: finite-budget lower energy envelope and inverse contrast bound MAP-TYPE=intertwiner
```

## Result and scope

For every fixed positive squeeze pair and exact contrast 0<d<3/4,
the unique minimizing effect satisfies 0<e0<e1<...<1 and tends to1.
Its complementary tail has a strictly subunit limiting ratio, determined
explicitly by the multiplier and squeezes. Negative contrast is the outcome
complement. Every joint minimizer inherits this structure. A two-parameter
shooting recurrence characterizes the fixed-squeeze optimizer when the ENTIRE
trajectory obeys its caps and exact contrast. No joint uniqueness, practical
shooting convergence or finite-prefix certificate is asserted.

This is the supplied positive Fock, binary diagonal square-root Kraus model
with one squeeze per outcome. Cost is output FIELD energy only. Apparatus,
clock, preparation, reset and total work remain unaccounted. SC-META-53 stays
UNCERTAIN; source, ledger0.263, LT-SM8/LT-GR6b, canon and GU physical quotient
are unchanged. K2192's monotonic scalar frontier and saturation are reused,
not new here. No numerical optimum, uniform tail bound, novelty or external-expert claim.

## 1. Exact recurrence

Use [K2188](k2188-detector-variational-structure-2026-10-28.md):

    p_n=(3/4)4^-n, x_n=p_n e_n, y_n=p_n(1-e_n), q_n=3n-1,
    R(x)=sum(n+1/2)x_n, T(x)=sum(n+1)sqrt(x_n x_(n+1)),
    A(s)=41s²/6+3/(2s²), C=40/3,
    E=R(x)A(s1)+R(y)A(s0)-C[s1T(x)+s0T(y)]+35/18.

K2188 proves strict coordinate interiority, fixed-squeeze uniqueness and
h_n=eta q_n by finite variations, with

    h_n=(n+1/2)ΔA-C(s1 g1_n-s0 g0_n), ΔA=A(s1)-A(s0),
    g1_n=n sqrt(e_(n-1)/e_n)+(n+1)/4 sqrt(e_(n+1)/e_n).

The backward term is omitted at n=0. The factor1/4 is the geometric probability
ratio after differentiating the square root; it is not an arbitrary cutoff.
Put Δs=s1-s0 and

    K(u,v)=s1 sqrt(v/u)-s0 sqrt((1-v)/(1-u)).

For 0<u<1, K(u,u)=Δs and K is strictly increasing in v. The KKT equation is

    n[K(e_n,e_(n-1))-Δs]+(n+1)/4[K(e_n,e_(n+1))-Δs]=nB+D, (1)
    B=(ΔA-3eta)/C-5Δs/4,
    D=(ΔA/2+eta)/C-Δs/4.                         (2)

There is no probability-mass constraint: only signed contrast is fixed.
Adding a second multiplier would change this problem.

## 2. A discrete maximum principle gives at most one turn

At a local maximum the left side of(1) is nonpositive; at a local minimum
it is nonnegative. At n=0, sign(e1-e0)=sign(D). More precisely, if the
incoming increment e_n-e_(n-1) is nonnegative and nB+D>0, the backward
term is nonpositive and the forward increment must be strictly positive.
The sign-reversed statement holds for a nonpositive incoming increment
and negative forcing. With zero forcing these implications are weak,
and an incoming strict increment still forces a strict outgoing increment.

The affine forcing changes sign at most once. If D>0 and B>=0, all
increments are positive. If D>0 and B<0, increments start positive and
cannot turn before the forcing becomes negative. In the negative region
the first nonpositive increment is followed by strictly negative ones:
there can be one peak, but no later valley. D<0 gives the reversed
classification. For D=0, e1=e0; B>0 forces all subsequent increments
positive and B<0 forces them negative. If B=D=0, induction gives a
constant effect, whose contrast is0, excluded here. A zero increment in
a strict-forcing region can occur only at the single turn and is followed
by a strict increment of the opposite direction. Thus any plateau at an
extremum has at most two sites. The initial equality for D=0 is separate.
In particular every nonzero-contrast stationary effect is eventually
strictly monotone and has a limit ell in[0,1].

## 3. The tail must polarize

Suppose 0<ell<1. Divide(1) by n and pass to the limit; both neighbor
ratios tend1, so B=0. Then D!=0 by the constant-profile argument.
On this monotone tail, all coordinates lie in a compact subinterval of(0,1).
The derivative of K(u,v) with respect to v is uniformly bounded there.
Consequently both sequences K(e_n,e_(n±1))-Δs are absolutely summable:
their absolute values are bounded by a constant times neighboring
increments, whose total variation is finite. Summing(1)/n from any
positive N to M therefore has a bounded left side, while the right side
D sum_(n=N)^M 1/n diverges. Contradiction. Hence ell is0 or1.

A useful necessary sign condition is

    e_n ->0 implies B>=0; e_n ->1 implies B<=0.  (3)

For the first case the eventual monotone tail is decreasing. Set
r_n=sqrt(e_(n+1)/e_n) in(0,1). The complementary ratios tend1.
Dividing the original recurrence by n gives

    1/r_(n-1)+(1+1/n)r_n/4 ->5/4+B/s1.

If B<0, eventually 1/r_(n-1)+r_n/4<=5/4-delta for some delta>0.
Writing t_n=1-r_n in(0,1) and using 1/r_(n-1)>=1+t_(n-1) gives
t_n>=4t_(n-1)+4delta, impossible under iteration. Complementing e and
exchanging squeezes proves the second case. The next step combines this sign condition with the single-turn result;
the intermediate classification is not the final optimizer shape.

## 4. Contrast selects global strict monotonicity

For D>0 the sequence starts increasing. If B>=0, the forcing stays
positive, no maximum is possible and the limit is1, requiring B<=0.
If B<0, a peak would create a permanently decreasing tail tending to0,
contradicting the necessary B>=0. Thus D>0 always gives a nondecreasing
sequence tending to1 and B<=0. The reversed argument gives a nonincreasing
sequence tending to0 for D<0 and B>=0. If D=0,B!=0, the initial equality
is followed by strict monotonicity with sign B, contradicting the endpoint
sign condition. B=D=0 is the already excluded constant case. Hence D!=0.

A first zero increment after positive increments would make the forcing
strictly negative at that index, because the backward term is negative.
Since B<=0, it stays negative and the next increment is negative, creating
the excluded peak. Thus all increments are strictly positive when D>0.
The reversed argument handles D<0. Absolute summation by parts gives

    d=sum (n+1)p_n(e_(n+1)-e_n),

since 4n p_n-(n+1)p_n=(3n-1)p_n. Consequently positive contrast selects
D>0, strict increase and limit1; negative contrast selects the complement.

## 5. The critical case is impossible; the exact tail ratio

For positive contrast, B is actually strictly negative. To exclude B=0,
set a_n=sqrt(e_n), b_n=sqrt(1-e_n) and delta_n=b_n-b_(n+1)>0.
The forward and negative backward differences in(1) are respectively

    delta_n F_n,    delta_(n-1) G_n,
    F_n=s0/b_n+s1(b_n+b_(n+1))/(a_n(a_n+a_(n+1))),
    G_n=s0/b_n+s1(b_(n-1)+b_n)/(a_n(a_(n-1)+a_n)).

Both expressions are exact rationalizations. Since a_n->1,b_n->0,
G_n/F_n->1. If B=0, equation(1) and D>0 force

    delta_n > [4n/(n+1)](G_n/F_n) delta_(n-1).

The multiplier exceeds2 eventually, contradicting positivity and
sum delta_n<infinity. Thus B<0 for every positive interior contrast.
Negative contrast follows by exchanging outcomes and squeezes.

Put r_n=b_(n+1)/b_n in(0,1) and k=5/4-B/s0>5/4. Dividing the recurrence
by n, with a_(n±1)/a_n->1, gives

    1/r_(n-1)+r_n/4=k+o(1).

Hence r_(n-1)=phi(r_n)+o(1), phi(t)=1/(k-t/4). On[0,1] this map has
Lipschitz constant at most1/4. Its unique fixed point in[0,1] is

    r*=2k-2sqrt(k²-1),  0<r*<1.

For completeness set M=limsup |r_n-r*|. The approximate recurrence implies
M<=M/4, so M=0. Therefore

    (1-e_(n+1))/(1-e_n) -> r*²,
    lim (1/n)log(1-e_n)=2log(r*)<0.

The logarithmic limit follows by Cesaro averaging of convergent log ratios.
This is an asymptotic rate, not an explicit finite-n prefactor or a uniform
cutoff bound across all contrast/squeeze pairs. It does not make a finite
shooting prefix an infinite certificate. The algebraic boundary k=5/4,r*=1
is a useful control, but cannot occur for these nonzero-contrast optimizers.

## 6. Unique-next-value shooting with the correct square-root branch

Given s1,s0>0, eta and 0<e0<1, solve sequentially

    Z_n=4/(n+1)[((n+1/2)ΔA-eta(3n-1))/C
                         -nK(e_n,e_(n-1))],
    K(e_n,e_(n+1))=Z_n.                           (4)

Again omit the backward term at n=0. For u=e_n let

    a=s1/sqrt(u), b=s0/sqrt(1-u), L=a²+b².

The unique interior next value exists exactly when -b<Z_n<a. It is

    e_(n+1)=[(a Z_n+b sqrt(L-Z_n²))/L]².          (5)

To prove it, let alpha=sqrt(v), beta=sqrt(1-v), both positive. The equations
a alpha-b beta=Z and alpha²+beta²=1 give

    alpha=(aZ+b sqrt(L-Z²))/L,
    beta=(a sqrt(L-Z²)-bZ)/L.

The strict range makes both numerators positive. They obey alpha²+beta²=1
and the original unsquared equation. Endpoints give v=0 or1, inconsistent
with an interior nonzero-contrast minimizer; exterior Z gives no solution.
Squaring formula(5) without its range test can create a false branch.
For fixed squeezes the shooting parameters are only(e0,eta); no independent
e1 or tail probability may be freely fitted. This is an exact reduction,
not a proof that finite shooting, interval iteration or a numerical search
converges or certifies full infinite feasibility.

## 7. Full feasible shooting is sufficient at fixed squeezes

Suppose a strictly interior infinite trajectory of(4) has the desired
nonzero contrast. Its h_n=eta q_n. At each n at least one branch coordinate
is >=p_n/2. Its positive T-gradient is bounded by
[n sqrt(8)+(n+1)/sqrt(2)]/2. The h equation, with fixed positive squeezes,
then bounds the other positive gradient by a constant times(n+1).
Thus both p-weighted gradient sums converge absolutely.

Concavity of each geometric-mean term, summed using these bounds, gives
for every cap-feasible competitor x' of the same contrast

    E(x';s1,s0)-E(x;s1,s0)>=sum h_n(x'_n-x_n)=0.

The sums are legitimate even when x' touches caps: |x'_n-x_n|<=p_n and
the reference gradients are bounded as above. K2188's uniqueness therefore
makes this trajectory THE fixed-squeeze minimizer. Conversely every such
minimizer supplies exactly this recurrence and contrast. Joint optimality
also requires optimizing the two squeezes; even imposing their stationary
equations is not a global certificate for that nonconvex outer problem.

## Verification and next question

Written full-tail maximum-principle, bounded-variation and convex-support
arguments carry the universal theorem. The exact probe verifies recurrence
coefficients against differentiated geometric terms, square-root inversion
and its admissibility range, affine-forcing propagation controls and planted
coefficient/branch faults. Finite controls are not a numerical infinite
optimizer or a substitute for the proofs.

The remaining substantive task is to control the admissible shooting set with
a computable finite-tail enclosure, or produce a certified practical outer
squeeze solver. The critical B=0 case and all turning/oscillatory optimizers
are excluded; neither should be requeued. Preserve
K2192 saturation/inverse, K2182 endpoint, weak-contrast353/170 and K2176
half-contrast bracket. Stable shared Hamiltonian/preparation/reset accounting
and the source-native physical quotient remain separate missing constructions.
