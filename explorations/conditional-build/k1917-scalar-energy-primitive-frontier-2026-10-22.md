---
title: "K1917: Symmetry reduction and sharp energy cost of scalar phase control"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied conditional models only; no native GU, novelty, work protocol or formal proof
scripts:
  - tests/channel-swings/k1917_scalar_energy_primitive_frontier.py
  - tests/channel-swings/k1917_scalar_energy_primitive_frontier_probe.py
---

# K1917: Symmetry reduction and sharp energy cost of scalar phase control

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
result: global centering reduction, convex primitive obstacle problem and sharp high-energy tradeoff
carrier: real scalar phase on symmetric interval with two symmetric plateaux LAYER=toy CHIRALITY=N/A
pairing: real Sobolev derivative energy and Lebesgue phase marginals ON=one_dimensional_interval
real_structure: real phase lift; reflection sends phi(u) to minus phi(-u)
grading: propagation directions only, not particle chirality
action_owner: repository-construction -- prescribed scalar pulse and phase-gradient energy
target: primitive norm and peak-drive cost at fixed phase contrast MAP-TYPE=intertwiner
```

## 1. Question and exact scope

Reuse [K1915](k1915-scalar-pulse-duration-limits-2026-10-21.md) and
[K1914](k1914-scalar-control-transport-cuts-2026-10-21.md). Fix
0<a<b<L, ell=b-a, contrast theta>0, h=theta/2, and speed c>0.
A real smooth compact phase phi has zero integral, value alpha on[-b,-a]
and beta on[a,b], with alpha-beta=theta. Set

    F(u)=integral_(-L)^u phi, A=||F||_infinity, E=int |phi'|^2,
    A0=h ell/2, C=16 h^3/9=2 theta^3/9.

The old centered lower bound extends to this ENTIRE class. Moreover its
leading constant is sharp despite finite spatial gaps and outer boundary
conditions. If A_E is the infimum of A with E<=E0 (written E0 below), then

    A_E >= A0+C/E0,
    lim_(E0->infinity) E0 (A_E-A0)=C.                    (1)

For the energy needed under A<=A0+epsilon,

    E_min(epsilon) >= C/epsilon,
    lim_(epsilon->0+) epsilon E_min(epsilon)=C.          (2)

These are exact sharp ASYMPTOTICS, not an explicit all-budget Pareto formula.
We also give a global convex variational characterization of the relaxed
finite-budget problem, and the fixed-energy short-time control consumer.

## 2. Reflection removes the common plateau phase without loss

Define phi_o(u)=[phi(u)-phi(-u)]/2. It has the exact values+h and-h on
the two plateaux, zero total area, and the same smooth compact support class.
Its primitive is F_o(u)=[F(u)+F(-u)]/2, using F(-L)=F(L)=0.
Convexity gives ||F_o||<=||F|| and int|phi_o'|^2<=int|phi'|^2.
Thus a noncentered common phase cannot improve the joint A/E infimum.
This is a proved reduction, not an assumption of symmetry of minimizers.
K1915's four-transition bound therefore proves the lower halves of(1)-(2).

The reduction holds for peak pulse cost at EVERY fixed duration as well.
In K1914's characteristic strip u in(-L,L),0<z-u<d=2cT,
replace w(u,z) by -w(-u,d-z). The strip is invariant; its row marginal
becomes -phi(-u), its zero column marginal remains zero, and its norm is
unchanged. Average original and reflected pulses. Both exact endpoint
constraints survive, peak norm cannot increase, and the phase energy does
not increase. The same map preserves smooth compact support. No time-reversal
assumption about a physical bath or source dynamics is involved.

## 3. Construct all four transitions and both outer connectors

Let g=L-b, choose epsilon>0 with tau=3epsilon/h<min(a,g), and set A=A0+epsilon.
The following continuous piecewise-quadratic phi is H1_0(-L,L) and odd.
Build its left half, then set phi(u)=-phi(-u) on the right:

* On[-L,-b-tau], length D=g-tau, take the negative bump
  phi=-6A t(D-t)/D^3, where t=u+L. Its integral is-A and energy12A^2/D^3.
* On[-b-tau,-b], take phi=h(t/tau)^2 with t=u+b+tau.
  Its area is epsilon and energy4h^3/(9epsilon).
* On[-b,-a], phi=h. The primitive rises from-A0 to A0.
* On[-a,-a+tau], take phi=h(1-t/tau)^2 with t=u+a.
  Its area is epsilon and energy4h^3/(9epsilon).
* On[-a+tau,0], phi=0.

The primitive visits 0,-A,-A0,A0,A on the left and returns in reverse
on the right. Hence its norm is EXACTLY A; no compensator overshoots it.
All four nearest-zero transitions fit, the two inner ones are disjoint,
and total integral is zero. Direct integration gives

    E_construct(epsilon)=C/epsilon+24(A0+epsilon)^2/(g-3epsilon/h)^3. (3)

The extra term stays finite as epsilon tends to zero. It is an actual
finite-gap construction, not a sum of independently unattainable local bounds.
The connector energy is itself minimal at its fixed length, area and zero
endpoints: integration by parts against t(D-t), followed by Cauchy-Schwarz,
gives int|f'|^2>=12(int f)^2/D^3, with equality for this parabola.
It does not prove the full global optimizer uses these segments at finite epsilon.

For smooth compact phases, use slightly enlarged plateaux
[-b-eta,-a+eta] and their reflections, support inside[-L+eta,L-eta],
and epsilon'<epsilon-h eta. Perform the same construction there and convolve
with an even nonnegative smooth unit-mass kernel of radius less than eta.
The original plateaux retain their EXACT values. Convolution preserves total
area, oddness and the primitive bound, and cannot increase derivative L2 energy.
Take eta->0 and epsilon'->epsilon from below, respecting the strict gap
conditions. This proves the same upper bound(3) as an INFIMUM for smooth
compact phases. No nonsmooth profile is falsely called a smooth minimizer.
Equations(2) follow. Inverting the bounds, with the connector term uniformly
bounded for small epsilon, proves(1). An energy slack before smoothing keeps
the constraint E<=E0 exact; taking the slack to zero gives the infimum.

## 4. Global finite-energy problem as a convex obstacle problem

The relaxed phase class is H1_0; equivalently F in H2(-L,L) with
F=F'=0 at both endpoints. Fix A>A0 and impose |F|<=A and F'=+h,-h
on the respective plateaux. These constraints are convex and closed.
The admissible set is nonempty by(3) with a smaller epsilon if needed.
Minimizing int|F''|^2 has a UNIQUE minimizer. Indeed the endpoint conditions
make this norm coercive on H2; a bounded minimizing sequence is weakly compact
and uniformly convergent along a subsequence, so constraints pass to its limit.
Weak lower semicontinuity gives existence. Strict convexity follows since a
zero second-derivative difference is affine and the boundary conditions kill it.
The minimizer is even by reflection and uniqueness. It is characterized by

    integral F''(G''-F'') >= 0 for every admissible G.    (4)

On any open interval outside the prescribed plateaux where |F|<A, arbitrary
compact perturbations of both signs are legal, so fourth_derivative(F)=0 distributionally:
F is cubic and phi is quadratic there. Contact sets and matching conditions
still determine the finite-A solution; a dense grid alone is not its certificate.
At A<=A0 the class is empty: the plateau rise and continuity of F' force
overshoot at A=A0, just as in K1915. This is a relaxed characterization;
we do not assert equality of relaxed and smooth minima at every finite A.
The explicit smooth recovery above is sufficient for the sharp asymptotics.

## 5. Released exact short-time consumer at a fixed energy budget

Let M_E(T) be the infimum pulse peak over smooth compact admissible phases
with E<=E0 and exact left phase0. Assume this smooth class is nonempty.
Sobolev's elementary bound gives P=||phi||<=sqrt(2L E0). K1915's
fixed-profile bounds and an infimizing sequence give

    2A_E/(cT^2) <= M_E(T)
       <= 2A_E/(cT^2)+2sqrt(2L E0)/T,
    lim_(T->0) T^2 M_E(T)=2A_E/c.                       (5)

Consequently the ordered high-energy/short-time limit is

    lim_(E0->infinity) E0 [lim_(T->0) T^2 M_E(T)-theta ell/(2c)]
       =4 theta^3/(9c).                                (6)

The order of limits is stated; no uniform joint scaling law is inferred.
A peak budget M requires T>=sqrt(2[A0+C/E0]/(cM)), as well as
T>=theta/(2M). This extends the previous centered energy obstruction to
arbitrary common phase and proves its leading energy correction is sharp.

## 6. Released finite-budget control bracket

The exact rational example L=4,a=1,b=2,h=1,epsilon=1/10 has
A=3/5 and E=863840/44217<20. Its connector peak is9/17<1,
so ||phi||=1. Slightly reduce epsilon and add the support/plateau margins
used in section3. Continuity of all segment formulas retains E<20,
A<3/5 and connector peak<1; convolution retains ||phi||<=1.
Thus there are genuinely smooth exact-plateau profiles with energy below20.
For this finite budget, (1) and the constructive pulse bound give

    53/(45cT^2) <= M_20(T) <= 6/(5cT^2)+2/T.

This explicit bracket applies at every T>0. It is not the exact finite-budget
optimum. The strict energy slack is what turns the rational H1 example into
an admissible smooth construction without pretending its corners are smooth.

## 7. Reproduction, controls and hostile review

Run the two scripts in the front matter with SymPy available. Exact polynomial
integration checks all joins, areas, primitive extrema, energy and connector
optimality. A separately written coefficient-integrator checks a complete
rational example without importing the producer or SymPy integration. It also
tests reflection signs and the full strip involution. Faults change transition
width or connector area, not an assertion. Report and hash checks are separate.

Strongest overclaim: equality in(3) for the finite-A optimizer or simultaneous
optimality of arbitrary T/E. Neither is asserted. Strongest contrary route:
noncentered phases, eliminated by the exact symmetry projection; unequal
plateau locations/lengths would invalidate that argument and are outside scope.
Weakest transfer: H1 construction to exact smooth plateaux, handled by support
margins, enlarged plateaux and contraction under convolution. The convex
characterization does not claim an already computed contact-set solution.
The argument uses elementary Cauchy-Schwarz, convex projection and Sobolev
compactness. No new general interpolation theorem is claimed.

## Source and acceptance boundary

SC-OP-04 ASSERTS candidate four-field grammar, SC-OP-05 is UNCERTAIN about
its rival, SC-MAS-01/SC-CHI-02 ASSERT a stylized curvature-mass toy, and
SC-META-53 remains UNCERTAIN about indefinite spectra. None supplies the
positive Hilbert model, control, physical units or bath used here. LT-SM8,
LT-GR6b and AC-F1, the source register and canon verdicts stay unchanged.
Native full20 injection, separate K/C, accessible algebra and physical
interaction/domain are separate construction debts. Analytic arguments carry
universal claims. Exact finite probes check identities, constructive examples
and countercontrols, not all continuum hypotheses. No expert acceptance,
formal verification, empirical prediction or novelty is claimed.
