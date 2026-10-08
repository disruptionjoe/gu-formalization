---
title: "K1403--K1408 spectral core and conserved-weight rigidity"
status: active_research
doc_type: conditional-build-result
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
target_claim: SC-META-53
created: "2026-10-07"
updated_at: "2026-10-07"
---

# K1403--K1408 spectral core and conserved-weight rigidity

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
generator, charge spectrum, scalar-electrodynamics action and every energy in
this packet are repository constructions. They do not identify source-selected
charges, an observed carrier or a GU physical state space.

Scope: invariant charge spectral support, its signed Noether measure, the exact
energy exchange for time-independent quadratic spectral reweightings, rigidity
of universally conserved weights with one Maxwell field, and a dense global
finite-charge direct-limit flow. No continuous global flow on the completed
unbounded-charge phase space, full BV-BFV boundary theory, quantization or
positive GU physical Hilbert cohomology is constructed.

```gu-typed-objects
result: invariant spectral support, signed Noether measure, weighted-energy exchange, conserved-weight rigidity and global finite-charge direct-limit flow
carrier: repository scalar-electrodynamics Cauchy data on R x T3 with principal-series internal Hilbert fibre LAYER=toy BRIDGE=maximal-compact-charge-reduction CHIRALITY=N/A
pairing: positive repository energy plus signed symplectic spectral Noether measure ON=repository_owned_control
real_structure: real Abelian connection and complex principal-series Hilbert matter carrier
grading: compact charge, triangular covariant order and BRST ghost degree
action_owner: repository-construction -- K1359/K1366, not a released source action
target: SC-META-53 conditional completed-flow boundary MAP-TYPE=restriction
```

## Preflight bookend

K1397 globalizes every bounded spectral sector, while K1398 shows that its
restart estimate is not uniform in the cutoff. Before inventing another PDE
coefficient, the cheapest structural discriminator is to classify what the
charge decomposition itself conserves and whether a growing spectral weight
can be folded into the one existing Maxwell energy.

The spectral theorem and independent phase symmetries are the primary route.
They can produce a global dense core and exact Noether data. The hostile route
then tests arbitrary finite charge combinations against a purported weighted
conservation law. A negative result binds only that functional class; null
forms, spacetime estimates, nonlinear/time-dependent normal forms and coupled
infinite hierarchies remain live.

## K1403 — spectral support is invariant

Let `P_B=1_B(Q)` for any Borel subset of the self-adjoint generator's
spectrum. Because `P_B` commutes with `Q`, spacetime differentiation, `D_A`
and the real scalar multiplier `f(||phi||^2)`, the projected field satisfies

```text
D_mu D^mu(P_B phi)+(m^2+mu Q^2+f(||phi||^2))P_B phi=0.
```

Zero projected Cauchy data stay zero by uniqueness. Thus the essential
charge-spectral support is invariant: the shared gauge field can exchange
energy among already occupied components but neither it nor the radial
interaction creates a new charge label. The result is gauge compatible
because `P_B` commutes with `exp(i alpha Q)`.

In particular, all cutoff flows are nested. Data supported in `P_M`, evolved
inside any larger `P_N`, give the same solution as the `P_M` theorem.

## K1404 — a conserved signed spectral Noether measure

For each Borel `B`, an independent constant phase on `P_B phi` preserves the
action: it leaves `Q`, `D_A` and the total radial norm unchanged. Its Noether
charge is

```text
C(B)=integral_T3 Im<P_B phi,P_B pi> dx.
```

The projected equation gives `dC(B)/dt=0`. Orthogonality of disjoint spectral
projectors makes `C` countably additive, and Cauchy--Schwarz gives

```text
|C|(spectrum Q) <= ||phi||_2 ||pi||_2.
```

Whenever the corresponding graph domains are finite, every moment
`integral q^k dC(q)` is conserved. The measure is gauge invariant and descends
through the proper classical quotient. It is signed and symplectic, not a
positive coercive distribution; high-charge energy can grow without violating
its conservation.

## K1405 — exact weighted-energy exchange

Let `w(Q)>=0` be a time-independent Borel weight and give the single Maxwell
energy and original quartic potential a scalar coefficient `c>=0`. Denote by
`H_(w,c)` the corresponding quadratic matter energy with every matter term
weighted by `w(Q)`. Direct differentiation gives

```text
dH_(w,c)/dt
 = integral E dot (j_w-c j_1) dx
   + lambda integral ||phi||^2 Re<(w(Q)-cI)phi,pi> dx,

j_w^a=e Im<w(Q)Qphi,D^a phi>.
```

The first term is the lifted-current defect: there is only one Maxwell
equation, sourced by `j_1`. The second is the radial-weight defect: the one
quartic potential cancels only the unweighted radial work. For `w=cI`, both
vanish and the functional is exactly `c` times the original energy.

## K1406 — conserved spectral weights are rigid

The converse is sharp for this functional class. Choose arbitrary smooth
finite spectral support. Nonzero charge-current data force
`q(w(q)-c)=0` at every occupied nonzero charge if the first defect is to vanish
for every solution. Independent radial Cauchy data then force `w(q)=c` also on
neutral components and tie every occupied component to the same constant.
Since arbitrary finite spectral combinations lie in the common core,

```text
H_(w,c) is conserved for every smooth solution
if and only if w(Q)=cI on the active spectrum.
```

Consequently `1+Q^2`, `Q^(2n)` and every other growing finite polynomial
weight fail to be a universally conserved charge-coercive energy when coupled
only to the existing Maxwell energy and quartic potential. This excludes the
naive spectral-reweighting route, not all modified energies: nonlinear or
time-dependent corrections, normal forms, spacetime estimates, extra fields
and coupled infinite hierarchies are outside the theorem.

## K1407 — global dense finite-charge direct limit

For any completed triangular phase space `X_R`, set

```text
X_R^fin = union_(N<infinity) P_N X_R.
```

Strong spectral convergence in every finite graph norm makes this union dense.
K1397 gives every datum in the union a global solution, and K1403 plus
uniqueness makes the sector flows compatible. They therefore glue to a single
global two-sided flow `S_fin(t)` on the dense invariant core, preserving the
positive fixed-sector energy and the spectral Noether measure and descending
sectorwise through the Coulomb quotient.

Density alone does not extend a nonlinear flow. A continuous extension to
`X_R` still requires cutoff-uniform finite-time bounds and a Cauchy estimate.
K1398 excludes the current base-energy restart as that argument; K1406 excludes
only the nonconstant quadratic spectral-weight substitute.

## K1408 — admission replay

The bridge census now has 76 rows: 52 satisfied, six conditional, fourteen
excluded and four missing. Four new satisfied rows record spectral-support
invariance, the signed Noether measure, the exact weighted exchange identity
and the dense global finite-charge core. One new excluded row records a
nonconstant time-independent quadratic spectral weight, coupled only to the
single Maxwell energy, as a cutoff-uniform conserved-energy route.

The four missing rows remain source-owned generator selection/normalization,
source-action identification, cutoff-uniform completed global BV-BFV flow with
positive physical Hilbert cohomology, and source observation/export.
K1145/K1150 remain `0/7`.

## Postflight hostile review

The strongest overclaim is that a dense global invariant core determines a
global completed flow. It does not: density supplies approximants but no
uniform bound or continuity. The strongest no-go overreach is to call K1406 a
theorem against every modified energy. Its quantifiers are explicit: one
time-independent quadratic spectral weight, the existing single Maxwell
energy and the existing quartic potential.

The signed Noether measure is another potential seam. Its total variation is
finite, but it is not positive and does not control charge moments unless the
corresponding graph norms are already finite. Conservation of its moments is
therefore not charge coercivity.

Within those boundaries the result is decision-grade. It constructs the exact
global dense spectral core and removes the most immediate modified-conserved-
energy proposal, leaving the next analytic work sharply typed: a genuinely
nonlinear/time-dependent correction, a cutoff-uniform spacetime estimate, or a
coupled infinite hierarchy that controls one completed triangular tier.

## Exact next input

Construct a cutoff-uniform estimate outside the rigid quadratic-weight class:
a gauge-covariant spacetime/null-form estimate, a nonlinear or time-dependent
normal-form energy, or a coupled infinite hierarchy with a global bound and a
finite-tier Cauchy consequence. In parallel, complete BV-BFV boundary and
exactness data before asking for positive physical Hilbert cohomology. A
source/action-owned observed-carrier selector must still fix `Q` and its
normalization independently.
