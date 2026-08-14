---
artifact_type: exact_endpoint_coadjoint_geometry_and_edge_cancellation_result
created: 2026-08-14
status: CHARGE_ZERO_HYPERPLANE_NOT_LIE_CLOSED__REGULAR_COADJOINT_ORBIT_DIM84__MINIMAL_FIXED_FIXTURE_EDGE_CARRIER_EXISTS__GLOBAL_OWNER_OPEN
source_return: SOURCE_CONFIRMS_EPSILON_MOVING_GAUGE_ORBIT_AND_NONCHIRAL_TOTAL__SOURCE_SILENT_COADJOINT_EDGE_FIELD_BOUNDARY_GAUGE_RESTRICTION_CASIMIR_LOCKING_AND_DOMAIN
ledger_rows: [RA-G2, LT-SM3, AC-F1, AC-G1a]
registry: lab/process/selected-k77-endpoint-coadjoint-edge-cancellation-gate.json
canon_verdict_change: none
---

# Selected K77 endpoint coadjoint-edge cancellation gate

## Result first

The two boundary horns left by the proper selected-orbit
Koszul--Tate construction can now be separated without fitting an edge field.

First, the seemingly cheap rule

```text
allow only gauge parameters X with mu(X)=0
```

does not define a gauge algebra.  The endpoint charge `mu` is nonzero on 30 of
the 91 labelled `so(7,7)` generators, but support is not the controlling
quantity.  Its exact Kirillov form

```text
K_mu(X,Y)=mu([X,Y])
```

has rank 84.  Restricted to the 90-dimensional hyperplane `ker(mu)`, it still
has rank 84.  Thus two individually zero-charge parameters can bracket to a
nonzero-charge parameter.  A boundary prescription that merely deletes the
one charged linear direction is algebraically inconsistent.

Second, the same rank computes the smallest possible homogeneous symplectic
edge carrier at this endpoint.  The coadjoint stabilizer has dimension seven
and is abelian, so `mu` is regular at the selected fixture and

```text
O_mu = Spin(7,7)/G_mu,      dim O_mu = 91-7 = 84.
```

The Kirillov--Kostant--Souriau form is nondegenerate on this orbit.  Giving an
edge variable values in `O_{-mu}` supplies the inclusion moment map; at the
point `-mu` its diagonal sum with the action endpoint is exactly zero.
Moreover, any equivariant moment map whose image contains `-mu` maps the
group orbit of that point onto `O_{-mu}`.  Its orbit therefore has dimension
at least 84.  The coadjoint orbit attains this lower bound.  It is the smallest
**homogeneous Hamiltonian** cancellation carrier for this fixed charge.

This is a viable path in the conditional build, not a physical selection.
The source does not introduce this edge orbit, restrict the boundary gauge
algebra, or prove that dynamical endpoint charges remain on one coadjoint
orbit.  Seven transverse invariant values distinguish nearby regular
coadjoint orbits.  A fixed 84-dimensional orbit works globally only if the
source action or boundary equations lock those seven values.  Otherwise a
larger carrier or the charged-boundary-symmetry horn is required.

## Plain English

We now know that “just ignore the charged gauge direction” does not work: the
remaining transformations generate charged ones when composed.

There is, however, a mathematically clean way to cancel the present charge.
Attach an edge system living on the symmetry orbit with the exact opposite
charge.  That orbit has 84 phase-space dimensions, and no smaller homogeneous
Hamiltonian system can do the job at this point.  What remains unknown is
whether GU's action actually supplies such a boundary system and whether the
charge stays on that same orbit as the fields change.

This result concerns boundary gauge charge only.  Weinstein's total theory
remains non-chiral; luminous/dark chiral-looking separation remains an
effective mechanism to be constructed, not a net-chirality target.

## Pre-wave admission

- **Fork:** the calculation stands on the conditional K77 bank and assumes no
  settlement of `SIGNATURE-AMBIENT`; the signature fork is not decided here.
- **Search dimension:** `so(7,7)^*` is 91-dimensional and the fixed-fixture
  question is decidable wholesale by exact linear algebra.  A functional edge
  field over all boundary configurations is not.
- **New object:** adopting the successful horn introduces an unowned
  coadjoint-orbit-valued edge field.  This packet constructs its minimal local
  type but does not adopt it as GU data.
- **What dies:** the full 90-dimensional `ker(mu)` restriction and every
  homogeneous Hamiltonian cancellation carrier of dimension below 84 die at
  this endpoint.  Charged boundary symmetry and larger edge carriers survive.

## Exact coadjoint theorem

Let `{E_i}` be the normalized bivector basis used by the full BFV packet and
let

```text
mu_i=(E_B-E_T)([E_i,T]).
```

The predecessor supplies the exact real rational `mu_i` and exact structure
constants.  The present probe constructs

```text
(K_mu)_ij = f_ij^k mu_k.
```

Exact rational rank and an independent finite-field rank certificate both
give 84.  Hence

```text
dim g_mu = dim ker K_mu = 7.
```

All 21 pairwise brackets of the resulting seven exact stabilizer basis vectors
vanish, so the stabilizer is abelian.  Because seven is the rank of complex
type `D7`, this is a regular coadjoint element at the fixture.

The restriction to `ker(mu)` is constructed explicitly with 90 basis columns.
Its alternating matrix has rank 84, furnishing exact witnesses
`X,Y in ker(mu)` with `mu([X,Y]) != 0`.  The canonical intersection

```text
g_mu intersect ker(mu)
```

has dimension six and is abelian.  It is a valid small residual algebra, but
the source/action supplies no reason to replace the full boundary gauge group
by it.  No maximality claim is made for that six-dimensional subalgebra.

## Why the coadjoint orbit is the correct first edge candidate

For any Hamiltonian `G`-space `(M,omega,J)` and point `m` with `J(m)=-mu`,
equivariance implies

```text
J(G.m)=G.(-mu).
```

Consequently `dim(G.m) >= dim(O_{-mu})=84`.  The coadjoint orbit itself, with
its KKS form and inclusion moment map, realizes equality.  On the product of
the action endpoint and this orbit, the diagonal moment map vanishes at
`(mu,-mu)`.

This theorem is deliberately narrower than “the edge problem is solved”:

- it supplies a symplectic orbit, not necessarily a cotangent presentation;
- it handles one fixed endpoint charge, not every dynamical charge;
- it does not provide a boundary kinetic term, preboundary potential, quantum
  measure, polarization, analytic domain or positive cohomology;
- it does not select charged symmetry versus gauge redundancy; and
- it does not derive the edge variable from Weinstein's action.

The old v0.101 sixty-dimensional schematic edge completion answered a smaller
finite horn classification and did not realize the full selected
`Spin(7,7)` moment map at this endpoint.  It must not be cited as a global
minimum for the present charge.

## Specialist route choice

- **Symplectic geometry:** selected the Kirillov form and moment-map orbit
  theorem instead of searching edge coordinates.
- **Lie theory:** rejected `ker(mu)` by exact bracket closure and identified
  the regular abelian stabilizer.
- **Homogeneous geometry:** separated one orbit from its seven transverse
  invariant directions.
- **BFV:** required componentwise diagonal moment-map cancellation; the
  previous proper KT model remains intact.
- **Variational bicomplex:** retained the action-derived endpoint rather than
  imposing zero by definition.
- **Source criticism:** confirmed moving-frame ownership and retained source
  silence on edge fields and boundary gauge disposition.
- **Analytic/PDE:** deferred domains because a local finite orbit is not a
  global boundary phase space.
- **Philosophy of science:** counted the cost of the surviving construction
  and refused to turn mathematical availability into derivation.

## Hostile boundary

The strongest overclaim is that 84 new physical degrees of freedom have been
derived.  They have not.  Eighty-four is the symplectic dimension of a
minimal homogeneous cancellation orbit at one fixture.  Orbit coordinates
are related by symmetry and no physical quotient, field theory or observable
has been constructed.

The strongest contrary route is an action-owned boundary/Green condition
that sends the endpoint to zero, or a source-owned reduction to a genuine
zero-charge Lie subalgebra.  The present theorem does not exclude either; it
excludes only the naive full hyperplane restriction and undersized
homogeneous cancellation carriers at the tested endpoint.

The global failure seam is the seven coadjoint invariants.  If action-owned
field variations move them, one fixed orbit cannot serve as the edge carrier.
If they remain fixed, the associated orbit bundle becomes the sharply typed
successor.

## Progress and next gate

This collision-scoped packet intentionally changes no ledger version.  It
will be composed into the next immutable ledger after the concurrent v0.253
packet is durably owned.  No row verdict, residue, quotient, datum, canon
claim, W/mirror selection, chirality, generation count or public posture
changes.

Next compute the seven independent coadjoint invariants of the action endpoint
and their first variations under the owned boundary field directions.  If all
seven are locked, construct the associated `O_{-mu}` edge bundle and diagonal
BFV charge.  If any varies, reject the fixed-orbit carrier and compare a
larger cotangent/group carrier with the charged-boundary-symmetry horn.

## Reproduction

```sh
sage -python \
  tests/channel-swings/selected_k77_endpoint_coadjoint_edge_cancellation_gate_probe.py
```

The exact probe passes all declared rational, modular, Lie, symplectic,
source, hostile and planted checks.
