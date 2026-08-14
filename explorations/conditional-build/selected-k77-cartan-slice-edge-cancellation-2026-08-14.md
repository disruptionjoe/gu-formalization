---
artifact_type: exact_cartan_slice_edge_cancellation_and_diagonal_bfv_compatibility_result
created: 2026-08-14
status: OPPOSITE_CARTAN_SLICE_CANCELS_91_ENDPOINT_COMPONENTS_AND_FIRST_VARIATION__DIAGONAL_BFV_ALGEBRAICALLY_COMPATIBLE__BOUNDARY_OWNERSHIP_OPEN
source_return: SOURCE_CONFIRMS_ENDPOINT_CHARGE_AND_MOVING_GAUGE_PARENT__SOURCE_SILENT_CARTAN_SLICE_EDGE_FIELD_BOUNDARY_ACTION_ADMISSION_DOMAIN_AND_QUANTIZATION
ledger_rows: [RA-G2, LT-SM3, AC-F1, AC-G1a]
registry: lab/process/selected-k77-cartan-slice-edge-cancellation.json
canon_verdict_change: none
---

# Selected K77 Cartan-slice edge cancellation

## Result first

The positive 98-dimensional Cartan-slice carrier now composes with the exact
selected-action endpoint at mathematical Hamiltonian grade.

Let M_(-C) be the sign-reversed regular Cartan chamber constructed by the
predecessor.  At its point (e,-L), the equivariant moment map is

    J_edge(e,-L) = -mu.

Therefore the diagonal endpoint moment map cancels componentwise:

    J_diag = mu + J_edge = 0

in all 91 normalized so(7,7) generator components.

The cancellation is not confined to one fixed coadjoint orbit.  If dmu is
the exact first variation induced by the selected action direction
(B,T) -> s(B,T), the opposite-chamber moment differential has rank 91:

    dJ_edge : T_(e,-L) M_(-C) -> so(7,7)*.

The probe constructs an exact 98-coordinate tangent lift v satisfying

    dJ_edge(v) = -dmu.

In the exact centralizer-dual basis used by the certificate, one solver can
choose the group-direction part to vanish and uses two nonzero Cartan
coordinates.  That support count is basis-dependent; the invariant statement
is the exact equation and its seven-dimensional fibre ambiguity.

Hence

    dmu + dJ_edge(v) = 0

componentwise in all 91 rows.  The lift is unique only modulo the
seven-dimensional right-Cartan moment fibre.  No boundary law presently
selects a preferred representative of that ambiguity.

The moment map is equivariant and uses the same exact 91-generator
so(7,7) structure constants as the already-certified full BFV algebra.
Consequently the diagonal mathematical carrier admits the standard
classical algebraic charge

    Omega_diag
      = c^a J_diag,a - (1/2) f_ab^c c^a c^b b_c,

whose self-bracket vanishes by moment-map equivariance and Jacobi.  This is
algebraic BFV compatibility.  It is not a source-owned functional BFV phase
space, a proper Koszul--Tate resolution or physical cohomology.

## Opposite-chamber certificate

At -L the Kirillov matrix changes sign:

    K_(-mu) = -K_mu.

The canonical restricted-cotangent matrix becomes

                 [  K_mu   -E ]
    Omega_edge = [              ],
                 [   E^T    0 ]

and the moment-map differential is

    dJ_edge = [ -K_mu  E ].

Exact ranks remain

    rank Omega_edge = 98,
    rank dJ_edge     = 91,
    dim ker dJ_edge = 7.

The all-generator Hamiltonian identity survives unchanged in the stated
d-theta convention.  Thus sign reversal changes the charge, not the
symplectic validity or completeness of the chamber carrier.

## Base cancellation

The exact selected endpoint charge has support on 30 of the 91 labelled
generators but is a full covector, not a 30-constraint truncation.  The probe
uses the complete vector and verifies

    mu_a + (J_edge)_a = 0,       a=1,...,91.

The same-sign choice is an exact planted failure:

    mu + mu = 2mu != 0.

The opposite sign is therefore forced for cancellation; it is not a
convention that can be dropped.

## First-variation lift

The predecessor proves that dmu leaves the fixed coadjoint orbit: all seven
invariant-polynomial derivatives are nonzero.  The fixed opposite orbit can
cancel the base point but its rank-84 tangent image cannot contain -dmu.

The Cartan-slice carrier supplies the missing seven transverse directions.
Surjectivity of dJ_edge gives an exact solution v, and every other solution
differs from v by the seven-dimensional Cartan fibre:

    solutions = v + ker dJ_edge.

This proves first-order admission of the action-owned endpoint motion.  It
does not construct a nonlinear section along an arbitrary action history or
across a singular/Weyl wall.

## Diagonal BFV compatibility

The exact endpoint Kirillov matrix and its opposite are reproduced from all
4,095 generator brackets:

    K_mu(a,b)    = f_ab^c mu_c,
    K_(-mu)(a,b) = f_ab^c (-mu_c).

Their diagonal sum vanishes at the cancellation point.  The inherited
4,095 representation identities cancel the J-linear terms in
{Omega_diag,Omega_diag}; the inherited 121,485 Jacobi triples cancel the
cubic-ghost term.

This composition establishes only:

- one classical Hamiltonian G carrier;
- an equivariant diagonal moment map;
- exact base and first-order cancellation; and
- the minimal two-term algebraic BFV charge.

It does not establish a boundary field space, functional differentiability,
Koszul--Tate acyclicity, a ghost-for-ghost bundle, a Green domain, a quantum
measure or observables.

## Planted rival failures

### Same-sign chamber

Using M_C rather than M_(-C) doubles the endpoint charge.  It fails before
BFV or boundary analysis.

### Fixed opposite orbit

The 84-dimensional orbit O_(-mu) cancels the frozen base charge, but

    -dmu is not in image K_(-mu).

It cannot follow the exact transverse action variation.  This preserves the
earlier fixed-orbit kill and shows why the seven Cartan pairs in M_(-C) are
load-bearing.

## Source, action and boundary-law ceiling

The source owns the selected B, T and moving gauge-frame grammar used to
construct mu.  The selected bare action owns the endpoint potential already
classified by the boundary-stationarity packet.  Neither source nor action
introduces the M_(-C) edge variable, adds its canonical potential to the
action, supplies an edge kinetic term, or admits its variations.

No source-owned edge field is constructed.
No action-owned boundary kinetic term is constructed.
No boundary stationarity law selects the edge lift or its seven-dimensional
ambiguity.
No proper functional BFV phase space or Koszul--Tate complex is constructed.
No analytic domain, positive pairing, prequantization or quantum state space
is constructed.
No physical cohomology, W/mirror selection, chirality, generation count or
observed spectrum is inferred.

Charged boundary symmetry remains the zero-import rival to adding this
mathematical edge carrier.

No ledger verdict, residue, quotient, datum, canon claim or public-posture
change follows.

## Disposition and next gate

The mathematical edge-composition gate is positive:

    base cancellation                     = exact 91 of 91,
    first-variation cancellation          = exact 91 of 91,
    diagonal algebraic BFV compatibility  = passes,
    source/action/boundary ownership       = open.

The next legitimate comparison is variational: either derive an action/source
boundary admission and kinetic law for this Cartan-slice edge carrier, or
retain the nonzero transformations as charged boundary symmetry.  Analytic
BFV and physical cohomology remain downstream of that choice.

## Reproduction

Run:

    sage -python tests/channel-swings/selected_k77_cartan_slice_edge_cancellation_probe.py

The exact probe composes the 45-check Cartan-slice predecessor and the
27-check exhaustive BFV predecessor, then certifies the opposite sign, all
base and first-variation components, lift ambiguity, BFV identities and
planted rivals.
