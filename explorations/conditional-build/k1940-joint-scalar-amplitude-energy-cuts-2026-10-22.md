---
title: "K1940: Joint scalar amplitude and phase-energy certificates"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: independent conditional mathematics; no native GU, novelty, external acceptance or formal proof
scripts:
  - tests/channel-swings/k1940_joint_scalar_amplitude_energy_cuts.py
  - tests/channel-swings/k1940_joint_scalar_amplitude_energy_cuts_probe.py
---

# K1940: Joint scalar amplitude and phase-energy certificates

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
result: nonzero energy penalty from transport cuts, explicit lower-amplitude pulse, and convex joint optimization
carrier: supplied one-dimensional massless two-characteristic system LAYER=toy CHIRALITY=N/A
pairing: real Lebesgue marginal duality and Dirichlet inner product ON=finite_moving_tube
real_structure: real phase lifts and real signed bounded pulse
grading: propagation directions only; no source chirality
action_owner: repository-construction -- common scalar spacetime potential
target: prescribed plateau contrast, zero opposite phase, and joint amplitude-energy cost MAP-TYPE=intertwiner
```

## 1. An actual joint resource decision

Fix c=1,T=9/2,I=[-3,3] and the moving tube of
[K1914](k1914-scalar-control-transport-cuts-2026-10-21.md).
The right phase phi belongs to H1_0(I), equals+1 on[-2,-1] and-1 on[1,2],
and has zero integral. The left characteristic phase is identically0.
Optimize J(phi)=integral_I |phi'|^2 with pulse amplitude at most M.
These are exact real phase lifts and a supplied conditional scalar model,
not a native GU field, probabilistic phase law or total-work cost.

Without the pulse constraint the unique minimum is J=4 at

    phi0(u)=-min(u,1,3-u), 0<=u<=3, extended oddly.

K1938 proves this profile is infeasible at M=23/100. This result answers
what follows if the phase itself may change while its plateaux remain fixed:

    5838358027/1459334590 <= J_star(23/100) <= 30/7.      (1)

The lower number is strictly greater than4. The upper is attained by an
explicit bounded measurable pulse of amplitude472/2071<23/100 whose phase
has J=30/7. Thus the constraint is genuinely feasible, and paying additional
phase energy repairs the previously excluded fixed-profile budget. This is
not a sharp joint optimum: the two ends of(1) do not coincide.
At M=1/4 the K1938 pulse realizes phi0, so J_star=4 exactly.
M<2/9 is impossible by the pointwise row bound on a plateau.

## 2. General cut-to-energy certificates

Write phi=phi0+delta. The allowed perturbation space H consists of H1
functions on the three free intervals(-3,-2),(-1,1),(2,3), zero at their
endpoints and with total integral0. On each interval phi0 is affine, so
integration by parts gives EXACTLY

    J(phi)=4+||delta'||_2^2.                              (2)

For any measurable cut A, let g_A be the Riesz representer of
ell_A(delta)=integral_A delta in H with inner product integral f'g'.
The Dirichlet inverse G on the three free intervals gives explicitly

    v=G 1_A, h=G 1,
    g_A=v-[integral v / integral h]h,
    K_A=||g_A'||^2=integral_A v-(integral v)^2/integral h. (3)

This removes the zero-area direction; dropping that projection generally
weakens or mistypes the sharp one-cut relaxation. K1914's ALL-set capacity
C(A) forces

    ell_A(delta) <= -D_A,
    D_A=integral_A phi0-(M/2)C(A).

Therefore for any D_A>0 and K_A>0,

    J_star(M)>=4+D_A^2/K_A.                             (4)

Equality is attained in the SINGLE-CUT relaxation by delta=-D_A g_A/K_A.
That function need not satisfy every other transport cut, so this is not
an all-set primal construction. If K_A=0 and D_A>0, the constraint is
infeasible, rather than permission to divide by zero.

For finitely many signed cuts, orient each inequality into the form above,
let K_ij=<g_i,g_j> and D_i its deficit. Every nonnegative multiplier vector
lambda gives the certified bound

    J_star(M)>=4+2 lambda.D-lambda^T K lambda.           (5)

It follows by expanding ||delta+sum lambda_i g_i||^2>=0. Thus exact finite
cut optimization can improve the bound without claiming that the selected
cuts exhaust the continuum. No strong-duality claim for a finite cut family
is needed for validity of(5). The complement supplies the reversed sign.

## 3. Exact consumer at M=23/100

Use A=[-3,s], s=-9/20, with d=2T=9. K1938 computes
C(A)=(3+s)(6-s)=6579/400 and integral_A phi0=2-s^2/2.
Let r=1+s. Direct Green integration on the free intervals gives

    H=integral h=5/6,
    I=integral v=1/12+r^2/2-r^3/6,
    J=integral_A v=1/12+r^3/3-r^4/8,
    K=J-I^2/H=145933459/1920000000,
    D=583/80000.

Substitution into(4) gives the lower endpoint of(1). The independent probe
solves -v''=1_A piece by piece, subtracts the mean constraint, and integrates
the actual derivative square; it does not merely repeat these scalar formulas.
The resulting one-cut minimizer is the sharp relaxed witness, with exact
zero integral, correct plateau traces and cut equality. No full pulse is
claimed for that relaxed minimizer.

## 4. A continuum primal without endpoint-correction overhead

The upper witness phase is odd and, for u>=0, is

    phi1(u)=-max(0,min(u,1,(23/8-u)/(7/8))).             (6)

It has the required plateaux, zero area and zero boundary trace, with
J=2+2/(7/8)=30/7. It starts its outer decline at2 and vanishes at23/8.
The phase is H1 and piecewise affine; it is not smooth.

Here is a reusable improvement over piecewise-constant inner matrices.
Partition I and J=[-3,12] into intervals of width h=1/8, and retain only
FULL rectangles inside E={0<=z-u<=9}. On each rectangle allow w=V/2 to be
affine in u and constant in z, with endpoint values y^-_ij,y^+_ij.
The continuum requirements become the finite exact equations

    sum_j h y^-_ij=phi1(u_i),
    sum_j h y^+_ij=phi1(u_(i+1)),
    sum_i (h/2)(y^-_ij+y^+_ij)=0 for every column j.      (7)

An affine function reaches its absolute maximum at an endpoint, so
|y^+/-|<=M/2 suffices pointwise. Equations(7) reproduce the entire affine
row phase and the identically zero column phase, almost everywhere; there
is NO residual phase correction. The grid aligns with all profile knots.
This construction is for piecewise-affine profiles, not a claim that a mesh
represents every smooth phase exactly.

For exact rational repair, store each endpoint flow x=(h^2/2)y. Each is an
edge of a bipartite graph from a row-ENDPOINT node to a column node. Row
endpoint demand is (h/2)phi1(u_endpoint); column demand is0. Floating linear
programming finds a candidate. Rationalization and spanning-forest balancing
then enforce every equality exactly, after which the ACTUAL maximum
4 max|x|/h^2 is recomputed. The stored witness has

    M=472/2071<23/100.

Every flow is in the JSON and can be verified without running the solver.
An independently written checker reconstructs the affine functions, both
pointwise marginals and their maxima. The complete pulse in physical
coordinates is V(t,x)=2w(x-t,x+t), zero outside the retained rectangles.
This is a finite-duration exact-endpoint witness, not just integrated cell
balance or floating residual acceptance.

## 5. Existence and shape of the true joint frontier

For any M with a feasible pair and finite energy, J_star(M) is attained
by a UNIQUE phase, although the pulse need not be unique. Take a minimizing
sequence with bounded H1 norm and pulses uniformly bounded in L-infinity(E).
A subsequence of phases converges weakly in H1 and uniformly on I; the pulse
has a weak-star subsequence. Testing marginals against integrable functions
passes both constraints to the limit, while plateau values, zero trace and
area persist. Lower semicontinuity attains the energy minimum.

The feasible phase set is convex. Strict convexity of the Dirichlet norm
on H1_0 proves uniqueness. The extended value function J_star(M) is
nonincreasing and convex: mix two feasible pulses/phases and use convexity
of the energy. Reflection (u,z)->(-u,9-z), with sign reversal of w,
preserves feasibility and energy, so uniqueness makes the optimal phase odd.
These statements concern the full measurable pulse problem, not a finite
mesh or the one-cut relaxation. Equation(1) proves its nonempty feasible set
at M=23/100. Smooth exact realization of the nonsmooth witnesses is impossible;
no derivative-bandwidth, slew-rate, smooth-attainment or lift optimum follows.

## 6. Hostile review, reproduction and boundaries

The strongest overclaim would call the single-cut lower optimizer globally
feasible or identify the finite affine program with the entire continuum.
Neither is done. The actual upper pulse is checked independently. A tempting
shortcut would retain only integrated row masses: here both row endpoints
are enforced, and interpolation proves every intermediate point. The2c
Jacobian, mean-zero projection and missing physical edge rectangles are
explicit. Corrupted flow, Jacobian and projection inputs are detected after
a green baseline; reporting and hash faults are labeled consistency evidence.

The improved outer-ramp7/8 witness succeeds on h=1/8. Two exploratory h=1/16
HiGHS calls returned status0/Not Set and supplied no certificate; those
solver failures prove no physical or resource impossibility. No claim of
best mesh, optimal profile, solver-independent discovery or novelty is made.
Replay uses the stored rational flows and needs no optimizer call. The
scripts import Python3, SymPy, NumPy and SciPy; --write uses HiGHS to
regenerate a candidate. Its rational certificate, not the floating optimizer, is accepted.

[Capacity-constrained transport duality](https://arxiv.org/abs/1307.7774)
is established background. The joint Dirichlet formulation and this witness
remain internal conditional mathematics. SC-OP-04 ASSERTS candidate grammar;
SC-MAS-01/SC-CHI-02 ASSERT a stylized toy; SC-META-53 remains UNCERTAIN.
None supplies this scalar drive, positive pairing or observable interface.
LT-SM8/LT-GR6b/AC-F1, source, ledger and canon are unchanged. Paired native
full20/K-C/domain/accessibility remains independent work. Internal checks
are not external expert review or formal verification.
