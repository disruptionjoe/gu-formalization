---
title: "K2012: Strict thermal duality gap and faithful-bath stability"
status: active_research
doc_type: exploration
created: "2026-10-24"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no GU identification, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k2012_thermal_duality_gap_and_bath_stability.py
  - tests/channel-swings/k2012_thermal_duality_gap_and_bath_stability_probe.py
---

# K2012: Strict thermal duality gap and faithful-bath stability

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
result: exact exposed-interval Lagrange dual, positive physical duality gap and dimension-uniform bath stability
carrier: fixed extreme four-state channel, faithful four-level diagonal bath and positive-gap catalyst LAYER=toy CHIRALITY=N/A
pairing: worst-input marginal half trace distance and upper mean energy ON=independent_initial_registers
real_structure: complex conserving unitaries and real normalized populations
grading: energy resonance components, not source chirality
action_owner: repository-construction -- unchanged finite-or-countable thermal class; bath reweighting explicitly enlarged
target: hard-budget versus priced optimization and robust nonconvexity MAP-TYPE=intertwiner
```

## 1. Exact duality obstruction, not a finite-support theorem

Fix0<delta<=1 and the faithful four-level Gibbs bath at t=1/2. Use
K2010's finite-or-countable positive-gap class and denote its optimal return
at budget E by F_delta(E). Define

    J_delta(lambda)=inf_protocol [R+lambda mean], lambda>=0,
    D_delta(E)=sup_(lambda>=0) [J_delta(lambda)-lambda E]. (1)

For EVERY6/5<=E<=11/5,

    D_delta(E)=63/100-3E/20.                            (2)

At both endpoints F_delta=D_delta. At EVERY strict interior point,

    F_delta(E)>D_delta(E).                              (3)

Thus the unrestricted-dimensional fixed-spacing budget frontier is nonconvex,
and no supporting-price argument can certify the hard-budget optimum on
this interval. Finite attainment of each positive-price problem does not
imply hard-budget finite attainment. The latter remains open; this result
rules out the proposed general strong-duality bridge, not finite optimizers.

K2010 already warns that its endpoint preparations obstruct a naive convexity
inference. The new claim here makes the entire dual exact, proves the strict
gap and price-selection consequences, derives a23-level lower-gap reduction and an all-dimension linear-order
small-spacing law, and propagates the obstruction to an
open set of faithful non-Gibbs bath states. It does not rediscover fixed-d
nonconvex examples or the unspaced convexified frontier.

## 2. The two physical endpoints determine the full dual

K1950 supplies the universal bound R+(3/20)mean>=63/100 and the two physical
preparations on levels{0,1,2,3,4}, occupied at1,3:

    A: p=(9/10,1/10), energy6/5, return9/20;
    B: p=(2/5,3/5),   energy11/5, return3/10.             (4)

Both have spacing1, hence are admissible for every stated delta. Therefore
J_delta(3/20)=63/100. For E=(1-w)6/5+w11/5 and any lambda>=0,

    J_delta(lambda)-lambda E
      <= min(9/20+lambda*6/5,3/10+lambda*11/5)-lambda E
      <= (1-w)9/20+w3/10=63/100-3E/20.                  (5)

Taking lambda=3/20 proves equality(2). K2010's attained countable optimum
and strict exposed-line gap prove(3). A convex F with the two endpoint values
would lie at or below their chord, contradicting(3).

For an interior budget, (5) is strictly below the chord unless lambda=3/20.
Hence this is the UNIQUE maximizing dual price, despite strict primal-dual
gap. More precise numerical optimization of the price cannot repair it.
The full K1950 equality-face classification plus strict tail transfer says
that an optimizer at this price is one of the two canonical endpoint
preparations (irrelevant unoccupied completions may remain). Their two
components cannot coexist at the same absolute occupied energies in a
nondegenerate catalyst. No physical intermediate-mean canonical optimizer
is supplied by mixing them.

At lambda>3/20 any priced optimizer must have mean<=6/5: compare it with A
and subtract the global supporting inequality. At0<lambda<3/20 its mean
must be>=11/5 by the analogous comparison with B. This is an excluded
open energy interval for canonical minimizers, not a claim to know their
complete spectra or energies away from the transition. Positive-price
finite existence is inherited from K2010.

The distinction is standard in nonconvex Lagrange duality; see
[Boyd and Vandenberghe, Chapter5](https://www.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf).
Equations(4)-(5) and the native strict gap establish it for this exact model.
No novelty or external certification is claimed.

## 3. A free flag changes the resource class

An abstract randomized choice between A and B with probability w has the
chord's expected energy and expected return. It is a convex relaxation if
an external distinguishable flag and its energy/spacing costs are ignored.
It is not an admissible nondegenerate-catalyst construction here.

For0<delta<=1/2, physically place A on0,...,4 and B ondelta,...,4+delta.
There are ten distinct levels and the same channel. Internal returns are
unchanged because the cosets have no cross resonance. If B has weight w,

    mean=6/5+w+w delta,
    R=63/100-(3/20)(6/5+w),
    R+(3/20)mean-63/100=(3/20)w delta>0.                (6)

The producer checks actual shell ranks and returns on these separated
spectra. Omitting the shift cost falsely turns a relaxation into a physical
protocol. Refitting w to meet E leads to the previously derived spacing
upper bounds; those are reused, not claimed new. At delta=0 these ten labels
collide, so they cannot serve as a counterexample to(3).

## 4. Faithful bath reweighting preserves exact feasibility

Now explicitly enlarge the bath probabilities: b=(b0,...,b3), each b_i>0,
sum b_i=1, on the SAME energies0,1,2,3. Keep the channel, catalyst model,
unitary conservation, initial independence, spacing and energy budget.
For a fixed tuple(H_C,sigma_C,U), write its system channel as

    Phi_b=sum_i b_i Phi_i.                              (7)

If Phi_b is the target extreme Schur channel, preservation of each pure
system basis state forces every Phi_i to preserve that state: a convex
mixture of positive states equal to a pure state has each summand equal.
Each branch is therefore a Schur channel. Extremality of the target
correlation matrix then forces EVERY Phi_i=Phi. Conversely that property
works for every faithful b. Thus the exact-feasible protocol set is
independent of positive bath weights. This proof does not assume the target
is extreme among all quantum channels, nor identify a finite-rank witness
with a global physical quotient.

For any fixed feasible tuple and system input rho, trace-norm contraction
under U and partial trace gives

    |R_b(tuple)-R_c(tuple)| <= TV(b,c)
      :=(1/2)sum_i|b_i-c_i|.                            (8)

Here the return is a supremum over all inputs; the pointwise estimate is
uniform, so it passes to the supremum. It also passes to infima over common
feasible protocols and to the sup over prices:

    |F_b(delta,E)-F_c(delta,E)|<=TV(b,c),
    |J_b(lambda)-J_c(lambda)|<=TV(b,c),
    |D_b(delta,E)-D_c(delta,E)|<=TV(b,c).                (9)

These assertions hold separately in each finite-dimension class and in the
finite-or-countable class, with the same constants. They require no compactness,
attainment, equality between those classes for the new bath, or continuity
of an unbounded energy operator. Bounds concern finite feasible parameters.

For Gibbs b_i(t)=t^i/Z(t),0<t<1, differentiating and summing gives
(1/2)sum|b_i'|<=Z'/Z<=6. Hence all three value functions are6-Lipschitz in t,
uniformly in dimension, delta and E. In beta=-log t the derivative equals
(1/2)E_b|i-E_b i|<=3/4, so they are3/4-Lipschitz in beta as well. This
sharp range-based constant is a sufficient bound, not an optimal constant
for this particular Gibbs curve. The absolute-deviation inequality follows
by convexity of |x-m| on[0,3]: E|X-m|<=2m(3-m)/3<=3/2.

## 5. Released robustness: an open family of strict duality gaps

Let gamma=F_(b0)(delta,E)-D_(b0)(delta,E)>0 at the t=1/2 reference and an
interior budget. Equations(9) imply

    F_b-D_b >= gamma-2 TV(b,b0).                        (10)

The gap survives any faithful perturbation with TV<gamma/2, including all
Gibbs temperatures |t-1/2|<gamma/12. This proves a nonempty open neighborhood,
not a numerical radius. K2010's compact-energy uniform positive gap makes
the neighborhood uniform over compact interior budgets and delta in
[delta_min,1]. No behavior at a missing-support bath is inferred: at zero
probability, the corresponding branch is no longer constrained by(7).

## 6. Released finite gap certificate: 23 levels suffice for a lower bound

There is a stronger quantitative consequence than a search through increasing
dimensions. Put B(E)=63/100-3E/20 and
Delta_23=F_23(delta,E,1/2)-B(E), for0<delta<=1 and6/5<E<11/5.
Then

    ((8-E)/(108-E)) Delta_23
        <= F_infty(delta,E,1/2)-B(E) <= Delta_23.       (11)

The left factor is strictly positive. Thus ONE complete23-level finite
program provides a certified all-dimension gap, rather than an unbounded
search with a tolerance-dependent dimension. Its exact enumeration can
still be expensive; it has NOT been executed here.

Proof: take any admissible finite-or-countable protocol with mean e<=E,
return R and gamma_p=R-B(E). K1950/K2010's strict-tail certificate says

    R+(3/20)e-63/100
      >=sum_(s>8) ((3/20)s-63/100-1/2)p_s >=(7/100)q,

where q is the population above8. Since e<=E, q<=100 gamma_p/7.
Every occupied level has energy at least1, so also
q<=(E-1)/7 and1-q>=(8-E)/7>0. Remove that tail, retain all physical levels
through11, and normalize. K2008 proves exact channel, spacing and budget
preservation and R_low-R<=q/(1-q). Its actual two-component reduction has
at most2*8+7=23 physical levels. Therefore

    Delta_23 <= gamma_p+q/(1-q)
       <= gamma_p [1+100/(8-E)].                       (12)

Take the infimum over original protocols. The reverse bound in(11) follows
by inclusion. All constants count physical completion levels; dimension17
would omit the required window through11. This argument does not require
an attained countable optimum. In conjunction with the already-proved finite
strict gap, it gives a second, constructive route to all-dimension strictness.

At rational delta,E, an exact rational evaluation of the23-level program
and the left factor in(11) produce an explicit positive g for(10). This is
a finite specified consumer with no numeric gap claimed before that run.

## 7. Released rate: the unrestricted penalty is of linear order

K1998 proves, for each FIXED d>=10 and fixed interior E,

    Delta_d(delta)=ell(E) delta+O(delta^2),
    ell(E)=(3/20)min(E-6/5,11/5-E)>0.

Apply this established theorem at d=23, not at a dimension that grows as
delta shrinks. Combine(11) with the explicit ten-level placements. Writing
gamma_infty(delta)=F_infty(delta,E,1/2)-B(E),

    ((8-E)/(108-E)) ell(E)
      <=liminf_(delta->0+) gamma_infty(delta)/delta
      <=limsup_(delta->0+) gamma_infty(delta)/delta <=ell(E). (13)

Thus gamma_infty=Theta(delta) for each fixed interior budget, uniformly over
the allowed dimension in the sense of the unrestricted optimum. There is no
claim that the limit exists, equals ell(E), or is uniform in E near the
endpoints. No interchange of a fixed-d asymptotic with infimum over d is
used: (11) supplies the missing uniform comparison. This rules out a
sublinear-in-delta penalty such as delta^2 even using unbounded dimension.
The factor is conservative, not a sharp coefficient. Exact ten-level
optimality at every unrestricted dimension remains unproved.

The tests execute real low-plus-remote preparations, their occupied tail,
mean, return and normalized low return, checking both tail charges and
(12)'s arithmetic. They also compute the explicit positive lower coefficient
for rational interior budgets. These are consumers of the universal proof,
not an executed23-level optimization.

Strongest overclaim: duality failure proves no finite hard-budget optimizer.
It does not. Strongest contrary route: a free external flag attains the chord,
but changes the resource class; (6) exhibits the omitted physical cost.
Weakest seam: extrapolating bath continuity to missing support, or mistaking
small finite tests for the all-dimension theorem. Both remain fenced.
Same-author separately coded verification is internal evidence, not independent
specialist acceptance. SC-META-53 remains UNCERTAIN, LT-SM8/GR6b remain NEEDS;
source, ledger and canon unchanged.

Executed: producer/replay2 endpoint protocols,19 budget chords,27 physical separation protocols,900 bath-stability groups,9 actual tail transfers and19 coefficient controls. Separate probe1049 groups, three mathematical mutations, two contrary controls and five provenance hashes. No23-level optimization was executed.
