---
title: "K1415--K1420 split Gauss and classical BFV boundary"
status: active_research
doc_type: conditional-build-result
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
target_claim: SC-META-53
created: "2026-10-07"
updated_at: "2026-10-07"
---

# K1415--K1420 split Gauss and classical BFV boundary

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `SOURCE_NATIVE_ROUTE` only because the packet tests the
classical quotient and positivity requirements left open under SC-META-53.
The compact generator, scalar-electrodynamics action, Gauss law, charge
regularizer and every BFV datum below are repository constructions. They do
not identify the released GU action, its observed carrier or its physical
state space.

Scope: the neutral completed triangular Cauchy phase space of the repository
scalar-electrodynamics control on the trivial bundle over `T3`; a global split
Gauss coordinate; an explicit Koszul--Tate contraction on a finite-rank smooth
cylindrical/polynomial algebra; a free based-gauge BRST reduction; the proper
residual compact orbit-type quotient; and classical BFV degree-zero
cohomology. No global unbounded-charge PDE flow, unrestricted local-functional
resolution, quantization or positive GU physical Hilbert cohomology is
constructed.

```gu-typed-objects
result: global split Gauss coordinate, exact cylindrical Koszul--Tate contraction, based BRST reduction, residual compact stratification and classical BFV H0
carrier: neutral completed triangular scalar-electrodynamics Cauchy data on T3 LAYER=toy BRIDGE=maximal-compact-charge-reduction CHIRALITY=N/A
pairing: canonical classical boundary symplectic form and descended positive repository Hamiltonian ON=repository_owned_control
real_structure: real Abelian connection and electric field with complex principal-series Hilbert matter carrier
grading: Koszul--Tate antighost degree, based BRST ghost degree, compact charge and triangular derivative-plus-charge order
action_owner: repository-construction -- K1359/K1366, not a released source action
target: SC-META-53 classical quotient and physical-Hilbert boundary MAP-TYPE=restriction
```

## Preflight bookend

K1413's full-PDE leakage remains the leading analytic gate, but K1386--K1396
already construct the completed local triangular flow. The compact-torus
evidence inspected here supplies no honest cutoff-uniform global spacetime
estimate, so another local hierarchy would repeat rather than discharge that
gate.

The independent classical boundary arc is now executable. K1373 gives an
explicit bounded right inverse for the neutral Gauss constraint, K1399 proves
closed based-gauge range, and K1400 supplies a global Coulomb slice with a
proper residual compact action. The cheapest decisive question is whether
these results compose to a genuine functional Koszul--Tate/BFV resolution or
whether a rank, stabilizer or completion defect remains. Positive physical
Hilbert cohomology is kept separate: a classical reduced observable algebra is
not a quantum state space.

## K1415 — the Gauss constraint is a global split coordinate

On the neutral phase space write

```text
rho(phi,pi)=e Im<Qphi,pi> in H^-1_0(T3),
G(E,phi,pi)=div E-rho.
```

K1373's bounded right inverse is

```text
R g=-grad(-Delta)^(-1)g,       div Rg=g.
```

Let `P_T E=E-R(div E)`. Then the two maps

```text
(E,phi,pi) -> (g=G(E,phi,pi), E_T=P_T E, phi, pi),
(g,E_T,phi,pi) -> (E_T+R(g+rho(phi,pi)), phi, pi)
```

are mutual inverses on the completed topology. Hence `G^-1(0)` is globally
the coordinate hyperplane `g=0`. Moreover `D_E G=div` has the same bounded
right inverse everywhere, so there is no field-dependent constraint-rank
jump in the based neutral Gauss law.

## K1416 — the Koszul--Tate complex contracts explicitly

Use the algebra of finite-rank smooth cylindrical functions, polynomial in
finitely many Gauss coordinates `g_a` and odd antighosts `b_a`, with smooth
dependence on the remaining coordinates. Set

```text
delta b_a=g_a,       delta g_a=0.
```

On every finite cylindrical block the Euler operator

```text
N=sum_a(g_a partial_g_a+b_a partial_b_a)
```

is invertible in positive total degree. The standard homotopy

```text
h=N^-1 sum_a b_a partial_g_a
```

satisfies `delta h+h delta=id-iota pi`, where `pi` sets `g=b=0`.
Consequently positive antighost homology vanishes and degree-zero homology is
the cylindrical function algebra on the Gauss surface. K1415 makes this a
global contraction rather than a local regular-sequence statement. The claim
does not extend silently to every local, distributional or quantum functional
completion.

## K1417 — based BRST reduction is the Coulomb slice

The mean-zero gauge group acts by

```text
A -> A+d chi_0,       phi -> exp(i e chi_0 Q)phi.
```

It is free: `d chi_0=0` and zero mean imply `chi_0=0`. The longitudinal
coordinate `chi_A=(-Delta)^(-1) div A` (with the fixed Laplacian sign convention)
and the Coulomb representative globally split each orbit. With mean-zero
ghost `c_0`, the longitudinal coordinate and ghost form the BRST doublet
`s chi_A=-c_0`, `s c_0=0` when `sA=d c_0`. The same finite-block contraction therefore kills
positive based-ghost cohomology and identifies degree zero with functions on
the constrained Coulomb slice. K1399's Poincare estimate supplies closed
range on every triangular tier.

## K1418 — the residual compact quotient is stratified, not free

Constant gauge transformations remain after based reduction. A charge-`q`
component is multiplied by `exp(i theta q)`. For nonzero occupied charge set
`S`, the stabilizer is

```text
{exp(i theta): exp(i theta q)=1 for every q in S},
```

the finite cyclic subgroup determined by `gcd(|q|:q in S)`. Pure `ker Q`
data have full `U(1)` stabilizer, while gcd-one support is free. Compactness
makes the action proper and the quotient Hausdorff with closed orbit map, but
changing support changes orbit type. The full classical quotient is therefore
a proper stratified space, not one globally free Hilbert manifold. This is a
positive classification, not a defect to erase.

## K1419 — exact classical BFV boundary data

K1347's boundary charge is

```text
Omega_BFV=integral_T3 c_0 G,       {Omega_BFV,Omega_BFV}=0.
```

K1415--K1416 resolve the constraint, and K1417 resolves the based gauge
orbits. Taking residual compact invariants then gives

```text
H^0_BFV = cylindrical gauge-invariant functions on G^-1(0)/G.
```

K1348's nonnegative Hamiltonian descends to this stratified reduced space and
is nonzero on explicit classical classes. This completes the classical
boundary moment-map, Koszul--Tate and based-BRST package for the declared
repository control. `H^0_BFV` here is an observable algebra. It is not a
quantized state Hilbert space and supplies no Born pairing, representation,
interacting quantum BRST operator or positive GU physical cohomology.

## K1420 — admission replay

The bridge census now has 86 rows: 61 satisfied, six conditional, fifteen
excluded and four missing. Five new satisfied rows record the split Gauss
submersion, exact cylindrical Koszul--Tate contraction, based BRST/Coulomb
reduction, proper residual compact stratification and classical BFV
degree-zero identification.

The four missing rows remain source-owned generator selection/normalization,
source-action identification, cutoff-uniform completed global PDE evolution
with quantized positive physical Hilbert cohomology, and source observation/
export. K1145/K1150 remain `0/7`. SC-ACT-01/02/06 remain `ASSERTS`,
SC-META-53 remains `UNCERTAIN`, and the physics ledger is unchanged.

## Postflight hostile review

The strongest overclaim is to call classical BFV `H^0` a positive physical
Hilbert cohomology. It is an algebra of reduced classical observables. A
quantum representation, completion, positive state inner product and quantum
BRST operator are separate missing data. The strongest geometric objection is
the residual compact stabilizer: the quotient is stratified and cannot be
presented as one free manifold. The strongest analytic objection is scope of
the contraction: it is exact on the declared finite-rank cylindrical/
polynomial algebra, not automatically on every local-functional completion.

Within those fences the result is decision-grade. The repository control now
has complete classical boundary regularity and exactness data; the remaining
physical debt is no longer an unspecified failure of the Gauss/BRST algebra.
No source, ledger, canon, paper, prediction, confirmation or public posture
moves.

## Exact next input

The analytic wake remains a cutoff-uniform full-PDE mechanism controlling or
cancelling both K1413 leakage terms with a finite-tier Cauchy consequence.
The boundary wake is now narrower: construct a stratum-compatible quantum
representation and positive Hilbert completion of the interacting reduced
observable algebra, with a closed quantum BRST operator, before claiming
positive physical Hilbert cohomology. Independently, a source/action-owned
observed-carrier selector must still fix `Q` and its normalization.
