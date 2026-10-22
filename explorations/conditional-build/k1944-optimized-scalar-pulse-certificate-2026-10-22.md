---
title: "K1944: Optimized scalar pulse and smooth energy-infimum equality"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: independent conditional mathematics; no native GU, novelty, external acceptance or formal proof
scripts:
  - tests/channel-swings/k1944_optimized_scalar_pulse_certificate.py
  - tests/channel-swings/k1944_optimized_scalar_pulse_certificate_probe.py
---

# K1944: Optimized scalar pulse and smooth energy-infimum equality

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
result: exact continuum pulse, improved joint energy enclosure and smooth/measurable energy-infimum equality under strict feasibility
carrier: supplied massless two-characteristic scalar control on a finite tube LAYER=toy CHIRALITY=N/A
pairing: real Lebesgue marginals and Dirichlet energy ON=fixed_plateau_phase_and_zero_opposite_phase
real_structure: real signed pulse and real phase lift
grading: characteristic direction; no source chirality
action_owner: repository-construction -- common scalar spacetime potential
target: joint amplitude/phase-energy feasibility and regularity MAP-TYPE=intertwiner
```

## 1. An actual pulse closes most of the certified energy gap

Use [K1942](k1942-complete-scalar-energy-duality-2026-10-22.md)'s exact
model: c=1,T=9/2,I=[-3,3], phase+1 on[-2,-1], phase-1 on[1,2], zero
boundary trace and zero area; the opposite characteristic phase is identically
zero. The physical amplitude budget is23/100. The new continuum pulse has

    amplitude = 22451259/97656250 < 23/100,
    energy U = 78227902689379/19531250000000 < 401/100.       (1)

Thus the previously open energy4.01 budget is FEASIBLE. Reusing K1942's
unchanged all-cut-dual lower certificate gives

    1730979348830867/432645592385000 <= J_star(23/100) <= U.  (2)

These are approximately4.000918 and4.005269; the rationals are authoritative.
The earlier upper30/7 is improved substantially. This is a rigorous enclosure,
not an evaluated exact optimum, halfcut sufficiency or a matching primal/dual
certificate. The new upper is a newly constructed pulse, not a replay of
K1940's witness. Sections4--5 use its strict slack to settle a separate
regularity question and derive useful budget/phase-error consumers.

## 2. Reconstruct the continuum object from finite rational data

Set h=1/32, u_i=-3+ih for i=0,...,192 and z_j=-3+jh for
j=0,...,480. Thus u ranges over[-3,3] and z over[-3,12], the full
characteristic projection. Retain a rectangle
[u_i,u_(i+1)] x [z_j,z_(j+1)] only if ALL its points satisfy
0<=z-u<=9. Every retained rectangle carries two rational endpoint flows
f_ij0,f_ij1. For theta=(u-u_i)/h define

    F(u,z)=2[(1-theta) f_ij0+theta f_ij1]/h^2,
    V(t,x)=2F(x-t,x+t),                                 (3)

and set F=0 off the retained rectangles. Values on rectangle boundaries
are immaterial. This is bounded measurable control in the stated tube.
The JSON stores all110208 flows by lossless run-length encoding, plus193
phase-node values y_i. It is not a lossy compressed numerical sample.

The exact conditions are

    sum_j f_ijs = h y_(i+s)/2, s=0,1,
    sum_(i,s) f_ijs =0 for each j,
    4 |f_ijs| <= M h^2.                                (4)

Integrating(3) in z yields the continuous piecewise-affine phase with endpoint
values y_i. Integrating in u gives zero at EVERY z in a column, because the
integral of the affine basis on a row interval is1/2. Hence both continuum
marginals are exact, not merely cell-averaged. The physical Jacobian2c=2
explains the factor4 in(4). Affinity makes endpoint amplitude checks sufficient
on the whole rectangle. The phase is odd, has the exact plateaux and zero
boundary trace. Its energy is the exact polynomial integral

    U=sum_i (y_(i+1)-y_i)^2/h.

The independent probe reconstructs the affine functions, integrates both
marginals directly, checks the actual supremum and integrates their squared
derivatives. It does not use the producer's graph incidence matrix.

## 3. Discovery is separated from acceptance

A sparse linear program selects phase nodes and endpoint flows jointly,
using tangent lower approximations to the squared slopes for its search
objective. A single-core interior-point solver with crossover discovers a
candidate. Floating objective values, convergence messages and solver duals
are NOT the continuum certificate, and no finite-mesh optimum is claimed.
The final acceptance checks only(3)--(4), the exact phase constraints and
exact energy. The approximate search objective therefore cannot weaken(1).

Phase nodes are rounded in odd pairs to a common rational denominator;
endpoint flows use a separate common rational denominator. The resulting
row/column residuals are corrected exactly along a spanning forest of the
bipartite incidence graph. At each nonroot vertex add its residual to its
parent edge and subtract it from the parent's residual. Each component's
signed total is zero; an isolated vertex must already have zero demand.
The code verifies the remaining root residuals, every final capacity, and
all exact marginals. Rounding is never absorbed in a tolerance or claimed
harmless before this replay.

The coarser h=1/8 and1/16 candidates gave energies above4.01. The h=1/32
interior-point candidate passes the declared decision. A dual-simplex search
on that same fine program was stopped after sustained single-core work
without a candidate; that is a method change, not an infeasibility result.
Further decimal refinement is unnecessary for the4.01 decision. Closing the
remaining gap requires a stronger actual pulse/cut construction, not more
unproved claims about finite-cut feasibility.

## 4. Strict feasibility removes the smooth energy-infimum gap

The piecewise-affine phase in(1) is not smooth and cannot itself be the exact
marginal of a smooth pulse. Nevertheless its strict amplitude slack has a
stronger consequence for the JOINT energy problem.

**Theorem.** For the fixed plateaux, tube and zero-opposite-phase constraint,
if there exists an H1 phase with a measurable pulse of amplitude M0<M,
then the infimum phase energy over smooth compact pulses at budget M equals
the infimum over measurable pulses with H1 phase at that budget. This is
an equality of infima; no smooth minimizer or fixed nonsmooth endpoint
realization is asserted. In particular it applies at M=23/100 by(1).

**Proof.** First symmetrize a near-optimal phase/pulse by
(u,z)->(-u,9-z) with sign reversal. The tube and zero column condition are
preserved; the phase becomes odd with no greater amplitude or energy and
retains both plateaux. Do the same for the strictly feasible witness.
A convex combination with an arbitrarily small positive amount of the strict
witness has amplitude strictly less than M, preserves every endpoint
constraint, and has energy tending to the measurable infimum.

Approximate this odd H1 phase strongly in H1 by odd smooth phases compact
in(-3,3) and exactly constant on the two CLOSED plateau intervals. On the
three free intervals, smooth functions with the fixed endpoint values and
flat jets near those endpoints are dense in the corresponding affine H1
trace class: modify in shrinking endpoint neighborhoods and mollify in the
interior. Reflect to enforce oddness. This gives zero area automatically;
strong H1 convergence gives uniform convergence in one dimension. This
density statement allows the phase to vary, while keeping the plateau data.
It would be false for exact preservation of the entire nonsmooth phase.

Let r be the smooth approximant minus the strict phase and eta=||r||_infinity.
It has integral0. For any measurable A subset I,

    |int_A r| <= eta min(|A|,6-|A|).

The full rectangle I x [3,6] lies inside the characteristic tube, so the
capacity in K1914 satisfies

    C(A)>=3 min(|A|,6-|A|).

K1914's signed-cut theorem therefore supplies a measurable residual pulse
of physical amplitude at most2eta/3 with marginals(r,0). Choose eta small
enough that this correction leaves STRICT slack below M. The smooth target
phase then has a measurable realization below M. K1914 section6 supplies a
smooth compact pulse with the EXACT smooth marginals at budget M. The energy
of those marginals tends to the desired infimum by H1 convergence. The
reverse inequality follows because smooth controls form a subclass. QED.

For the explicit witness, M-M0=19357/195312500. Any zero-area residual with
uniform norm below58071/781250000 costs less than half that slack. Choose a
smooth plateau approximation also close enough in H1 to keep its energy below
401/100; the positive energy margin is92409810621/19531250000000. Hence
SMOOTH compact pulses with exact plateaux, zero opposite phase, amplitude
at most0.23 and energy below4.01 EXIST. This is an analytic existence result,
not an explicit serialized smooth pulse, derivative-bandwidth bound or exact
smooth optimality claim. The phase is allowed to change within its free
intervals; the supplied nonsmooth certificate remains measurably exact.

## 5. Released consumers

K1942's projection inequality turns(2) into a certified uniform distance to
the UNIQUE optimal H1 phase:

    ||phi_p-phi_star||_infinity^2 <= (U-L)/2,
    ||(phi_p-phi_star)'||_2^2 <= U-L,

where L is the lower endpoint in(2). The uniform error is below0.047,
including the whole free intervals, not a mesh-only comparison. This does
not say the pulse optimizer is unique.

Convexly combine the new pulse with K1940's explicit pulse (amplitude472/2071,
energy30/7). On the common h-grid their derivative cross integral is
43951251/10937500. If theta is the new-pulse weight, a physical amplitude
bound and exact phase energy are

    M_theta=(1-theta)472/2071+theta M0,
    E_theta=(1-theta)^2 (30/7)
            +2theta(1-theta)(43951251/10937500)+theta^2 U.

This is an actual continuum feasible family, not an interpolated conjecture
about optimum values. The report gives exact choices at budgets0.229 and
0.2295, with energies approximately4.069155 and4.020853. The older pulse
certificate is reused and hash-pinned, not counted as newly discovered.
The strict-feasibility theorem above gives smooth versions whenever an
arbitrarily small budget/energy margin is retained. No finite exact dual
match, pulse bandwidth, total physical work or native action follows.

## 6. Verification and source boundary

The producer performs111081 exact rational checks on final pulse bytes;
these mostly count finite rectangle capacities. The independent probe
integrates the reconstructed polynomials and verifies the exact margins.
Three actual input faults (flow, phase node, amplitude) fail mathematical
assertions after a green baseline. Source/report controls are consistency
checks. Universal smoothing, dual and continuum claims rest on their proofs,
not the large finite check count. Internal review is not independent expert
acceptance or formal proof.

Strongest overclaim rejected: smooth attainment of the nonsmooth witness,
exact optimization from the floating LP, or halfcut sufficiency. Strongest
contrary route is an untested union cut; actual pointwise marginals automatically
satisfy every measurable cut, while the lower certificate stays separate.
Weakest seams are the physical Jacobian, exact residual balancing, zero-area
smooth approximation and strict-slack transfer; all are explicit.

[Korman, McCann and Seis](https://arxiv.org/abs/1307.7774) give established
capacity-transport duality context. No novelty claim. SC-OP-04 ASSERTS
candidate grammar and SC-MAS-01/SC-CHI-02 ASSERT the stylized toy; SC-META-53
remains UNCERTAIN. None supplies this drive or its positive physical pairing.
LT-SM8, LT-GR6b and AC-F1, source register, physics ledger and canon are
unchanged. Reproduce with the two frontmatter scripts; --write rediscovers
and verifies a candidate, while default mode exactly replays the stored one.
