---
title: "K1409--K1414 homogeneous completed graph flow"
status: active_research
doc_type: conditional-build-result
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
target_claim: SC-META-53
created: "2026-10-07"
updated_at: "2026-10-07"
---

# K1409--K1414 homogeneous completed graph flow

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `SOURCE_NATIVE_ROUTE` only because this packet tests the
maximal-compact analytic route left uncertain by SC-META-53. The compact
generator, compatible real structure, scalar-electrodynamics action and every
graph energy below are repository constructions. They do not identify a
source-selected charge, observed carrier or GU physical state space.

Scope: an exact homogeneous current-free invariant manifold, a nonlinear
time-dependent positive graph energy, global cutoff-uniform propagation and
spectral-cutoff convergence on every fixed finite charge-graph tier, and the
exact two-term leakage that blocks direct promotion to the spatially dependent
Maxwell--matter PDE. No full completed PDE flow, BV-BFV boundary theory,
quantization or positive GU physical Hilbert cohomology is constructed.

```gu-typed-objects
result: homogeneous current-free invariant reduction, nonlinear time-dependent graph energy, completed global finite-tier flow and full-PDE leakage boundary
carrier: spatially homogeneous real Cauchy data in the repository principal-series Hilbert matter carrier LAYER=toy BRIDGE=maximal-compact-charge-reduction CHIRALITY=N/A
pairing: positive repository base energy and nonlinear charge-graph energies ON=repository_owned_control
real_structure: a declared conjugation commuting with the self-adjoint compact generator Q
grading: compact charge order and BRST ghost degree; spatial Fourier momentum is fixed to zero
action_owner: repository-construction -- K1359/K1366, not a released source action
target: SC-META-53 conditional global-flow mechanism and promotion boundary MAP-TYPE=restriction
```

## Preflight bookend

K1406 excludes only time-independent quadratic spectral reweightings of the
existing energy. The cheapest surviving positive mechanism is therefore to
let the common radial coefficient participate in the energy. K1395 already
exhibits a homogeneous periodic charged solution; rather than treating its
recurrence only as an obstruction, the present wave asks whether the entire
homogeneous unbounded-charge sector admits a completed global graph flow.

This is a route-changing discriminator. A positive theorem proves that the
radial interaction and unbounded charge spectrum are not by themselves the
global obstruction. The full-PDE energy identity then isolates the remaining
spatial/gauge terms before any null-form or infinite-hierarchy construction.
The source-selected carrier and full BV-BFV physical quotient remain the
strongest independent branches, but their required inputs are still absent.

## K1409 — the homogeneous real slice is invariant and current free

Let `C` be a conjugation on the repository internal Hilbert space with
`C Q=Q C`, and write `H_R=Fix(C)`. On normalized `T3`, take

```text
A=0,  E=0,  phi(t,x)=u(t),  pi(t,x)=v(t),
u,v in H_R.
```

All spatial covariant derivatives vanish. Because the inner product of two
`C`-real vectors is real,

```text
j^a=e Im<Q u,D^a u>=0,
rho=e Im<Q u,v>=0.
```

The Maxwell equations therefore preserve `A=E=0`, and the matter equation
reduces exactly to the Hilbert-valued defocusing oscillator

```text
u''+Omega^2 u+lambda ||u||^2 u=0,
Omega^2=m^2+mu Q^2.
```

The right-hand side commutes with `C`, so `H_R` remains invariant. This is an
exact nonlinear invariant manifold containing arbitrary, including infinite,
charge support. It is not a gauge fixing of every solution and not a model of
spatial propagation.

## K1410 — conserved base energy controls the shared coefficient

The oscillator conserves

```text
H_0=1/2||u'||^2+1/2||Omega u||^2+lambda/4||u||^4.
```

For `m>0`, `mu>0` and `lambda>=0`, if `s(t)=||u(t)||^2`, then

```text
||u|| <= sqrt(2H_0)/m,
||u'|| <= sqrt(2H_0),
|s'|=2|Re<u,u'>| <= 4H_0/m.
```

These bounds depend only on the conserved base energy and not on a spectral
cutoff. In particular, the recurrent coefficient need not be time integrable;
it is uniformly bounded pointwise for all time.

## K1411 — a nonlinear time-dependent graph energy closes every finite tier

For an integer `n>=0`, put `psi_n=Q^n u`. It solves

```text
psi_n''+(Omega^2+lambda s(t))psi_n=0.
```

Define the positive, time-dependent energy

```text
F_n(t)=1/2||Q^n u'||^2+1/2||Omega Q^n u||^2
       +lambda/2 s(t)||Q^n u||^2.
```

Direct differentiation uses the equation once and leaves only

```text
F_n'=(lambda/2)s'||Q^n u||^2.
```

Since `F_n >= (m^2/2)||Q^n u||^2`, K1410 gives

```text
|F_n'| <= (4 lambda H_0/m^3) F_n,
F_n(t) <= F_n(0) exp(4 lambda H_0 |t|/m^3).
```

This is the first positive cutoff-uniform mechanism outside K1406's rigid
class. It is nonlinear and time dependent: the conserved base solution enters
the graph energy through `s(t)`. It provides a global bound, not a new
conservation law, and it does not require `s` to be time integrable.

## K1412 — spectral cutoffs converge to a completed global graph-tier flow

Let `P_N=1_[-N,N](Q)`. The truncated oscillators have the same `H_0` and
`F_n` estimates with constants independent of `N`. For two cutoffs, their
difference satisfies a linear oscillator equation with bounded coefficient
and forcing

```text
-lambda(s_N-s_M)u_M.
```

On every finite interval, Cauchy--Schwarz, the base bound and the tier bound
give a standard energy-difference inequality. Gronwall bounds the difference
by the initial graph tails. Strong spectral convergence of `P_N` makes those
tails vanish. Thus the cutoff flows are Cauchy in

```text
G_n = { (u,v): Omega Q^n u in H, Q^n v in H }.
```

The limit is unique, depends continuously on initial data, exists for all
positive and negative times, and preserves nested compatibility among graph
tiers. Hence every fixed completed finite charge-graph tier carries a global
two-sided homogeneous flow; data in all tiers retain all finite tiers.

This is stronger than K1407's dense direct-limit theorem but only on K1409's
homogeneous current-free invariant manifold. It does not extend the full
spatially dependent flow.

## K1413 — the full PDE has two uncancelled leakage terms

For a full smooth Maxwell--matter solution, `psi_n=Q^n phi` still obeys the
same covariant matter equation because `Q` commutes with `D_mu` and the radial
scalar. The natural spatial analogue of `F_n` satisfies

```text
dF_n^PDE/dt
 = integral_T3 E dot j_n dx
   +(lambda/2) integral_T3 partial_t||phi||^2 ||Q^n phi||^2 dx,
j_n^a=e Im<Q^(n+1)phi,D^a Q^n phi>.
```

On K1409's slice both terms reduce to K1411: `E=j_n=0` and the coefficient is
spatially constant. On the full PDE, conserved base energy does not control
`partial_t||phi||^2` in `L-infinity_x`, and the lifted current contains the
next charge factor. K1379 and K1381--K1385 give the matching concentration and
top-corner warnings. The homogeneous energy therefore cannot be promoted by
the same Gronwall argument.

This identity does not exclude a gauge-covariant null form, spacetime estimate,
normal-form correction that cancels the two defects, or a summable infinite
hierarchy. It proves that such a mechanism must genuinely use spatial/gauge
structure rather than citing K1411 unchanged.

## K1414 — admission replay

The bridge census now has 81 rows: 56 satisfied, six conditional, fifteen
excluded and four missing. Four new satisfied rows record the invariant
homogeneous current-free manifold, cutoff-independent base-coefficient
control, the nonlinear time-dependent graph-energy estimate and the completed
global homogeneous graph-tier flow. One new excluded row records direct
promotion of that energy to the full PDE without controlling the electric-
current and pointwise radial-coefficient leakage.

The four missing rows remain source-owned generator selection/normalization,
source-action identification, cutoff-uniform completed global BV-BFV PDE flow
with positive physical Hilbert cohomology, and source observation/export.
K1145/K1150 remain `0/7`.

## Postflight hostile review

The strongest overclaim is to call the homogeneous theorem a completed global
Maxwell--matter flow. It freezes every nonzero spatial Fourier mode and forces
the current to vanish by a compatible real slice. The strongest contrary
construction is K1413's exact full-PDE identity: both defects return as soon
as spatial/gauge dynamics are restored. The weakest analytic seam is the
spectral-cutoff difference estimate; it is a finite-time Hilbert-space
Gronwall argument, not a uniform-in-time scattering or compactness theorem.

Within those boundaries the result is decision-grade. It proves that a
nonlinear time-dependent graph energy can beat K1406's rigidity and complete
the unbounded charge spectrum globally in a nontrivial invariant sector. It
also localizes the remaining full-PDE difficulty to two exact terms. No
source, ledger, canon, paper, prediction, confirmation or public posture
moves.

## Exact next input

Construct a cutoff-uniform full-PDE estimate that controls or cancels both
K1413 leakage terms: a gauge-covariant spacetime/null-form estimate, a
nonlinear normal-form correction, or a summable coupled hierarchy with a
finite-tier Cauchy consequence. Independently complete BV-BFV boundary and
exactness data before claiming positive physical Hilbert cohomology. A
source/action-owned observed-carrier selector must still fix `Q` and its
normalization.
