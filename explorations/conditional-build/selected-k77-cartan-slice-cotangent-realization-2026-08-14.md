---
artifact_type: exact_regular_cartan_slice_cotangent_symplectic_realization_result
created: 2026-08-14
status: SELECTED_REGULAR_CARTAN_STRATUM_GLOBAL_MINIMUM_98_CONSTRUCTED__ALL_STRATA_MINIMUM_OPEN
source_return: SOURCE_CONFIRMS_ENDPOINT_TRACE_DUAL_AND_ACTION_SCALING__SOURCE_SILENT_CARTAN_SLICE_EDGE_CARRIER_BOUNDARY_ACTION_DOMAIN_AND_QUANTIZATION
ledger_rows: [RA-G2, LT-SM3, AC-F1, AC-G1a]
registry: lab/process/selected-k77-cartan-slice-cotangent-realization.json
canon_verdict_change: none
---

# Selected K77 Cartan-slice cotangent realization

## Result first

The live 98-dimensional globalization horn constructs exactly on the selected
regular real-Cartan stratum.

Let G be the connected Spin(7,7) group used by the endpoint coadjoint action,
let L be the exact endpoint trace-dual, and let

    h = g_L

be its seven-dimensional real Cartan centralizer.  The predecessor proves
that L is regular semisimple of real type

    (split rank, compact rank) = (5,2).

Let C be the connected regular chamber in h* containing the Cartan
representative of L.  In left trivialization

    T*G = G x g*

restrict the canonical cotangent potential to

    M_C = G x C,                  dim M_C = 91+7 = 98,
    theta_C = <lambda,g^-1 dg>,
    omega_C = d theta_C.

The restricted two-form is globally defined, exact and symplectic.  The free
left G action is Hamiltonian with equivariant moment map

    J(g,lambda) = Ad*_g(lambda).

Its differential has rank 91 everywhere on C.  Therefore J is a complete
Poisson submersion onto the open invariant regular stratum

    U_(5,2) = Ad*_G(C)

containing the selected endpoint.  The inherited regular Poisson lower bound
is 98, so this construction proves that 98 is the smallest global
equivariant symplectic-realization dimension over this selected chamber
stratum.

This does not prove that one 98-dimensional carrier covers singular charges,
other real Cartan types or all of g*.  The canonical 182-dimensional T*G
fallback remains the all-charge construction, and the all-strata minimum
remains open.

## Exact tangent certificate

Use the vector trace form to identify h with its embedded dual slice in g*.
At (e,L), write a tangent vector to M_C as (X,a) in g plus h*.  The exact
cotangent formula is

    omega_C((X,a),(Y,b))
      = <a,Y> - <b,X> - <L,[X,Y]>.

In the normalized 91-generator basis, let K_L be the inherited Kirillov
matrix, H a 91-by-7 exact centralizer basis, G_tr the trace Gram matrix, and

    E = G_tr H.

The probe constructs the full matrix

             [ -K_L   -E ]
    Omega =  [            ].
             [  E^T    0 ]

Its exact ranks are

    rank K_L                  = 84,
    rank H                    = 7,
    rank H^T G_tr H           = 7,
    rank Omega                = 98.

Regular semisimplicity explains the result without coordinate luck:

    g = h direct-sum [g,L].

The Kirillov block is nondegenerate on the 84 orbit directions, while the
seven Cartan momenta pair nondegenerately with the seven centralizer
directions.

For the left action, the moment-map differential is the exact 91-by-98
matrix

    dJ_(e,L) = [ K_L  E ].

It has rank 91 and kernel dimension seven.  The kernel is exactly the
right-Cartan tangent.  For all 91 infinitesimal generators, the matrix
identity

    F_left^T Omega = -dJ

certifies the Hamiltonian equation in the declared d-theta convention.
Equivariance is canonical, and every linear moment Hamiltonian is complete:
its flow is global left multiplication by exp(tX), with lambda fixed.

## Why the product obstruction remains true

The predecessor rejected a different object:

    orbit family x T*C

with the varying KKS orbits inserted as symplectic product fibres.  M_C is
not that object.

At fixed lambda, the slice G x {lambda} is 91-dimensional and
presymplectic.  Its form has rank 84 and kernel h.  Only after quotienting
the retained H fibre does one obtain

    G/H

with its KKS form.  The two compact H circles are therefore present upstairs
and pair with changes of the Cartan momenta.  The total form is exact
upstairs even though the compact KKS periods on the reduced orbits vary with
lambda downstairs.

Thus the earlier cohomological no-go survives exactly as stated.  It kills
the orbit-product model, not this Cartan-slice restriction.

## Action-owned variation

The exact action direction (B,T) -> s(B,T) has a nonzero endpoint derivative
dmu and nonzero derivatives of all seven invariant generators.  Because dJ
is surjective, dmu has a unique local decomposition into an orbit part and a
Cartan-transverse part modulo the seven-dimensional moment fibre.  The new
carrier therefore admits the actual transverse endpoint motion that killed
the fixed 84-dimensional orbit.

This is a mathematical admission result, not an action-ownership result.
For edge cancellation the sign-reversed chamber M_(-C) can contain a point
with moment value -mu.  Composing that point with the action endpoint is now
the legitimate next gate.

## Singular and deletion controls

Three hostile plants delimit the construction.

1. At the zero singular wall the Kirillov block vanishes.  Keeping the same
   seven Cartan directions gives rank 14, not 98.  Regularity is load-bearing.
2. Deleting the Cartan momenta leaves the fixed 91-dimensional G slice with
   rank 84 and a seven-dimensional kernel.  The enlargement is necessary,
   not decorative.
3. Relabeling M_C as orbit x T*C fails structurally: the free G orbit in M_C
   has dimension 91, while the coadjoint orbit has dimension 84.  The missing
   seven directions are precisely the retained Cartan fibre.

## Source and physical ceiling

The source confirms the selected B, T, moving gauge parent and endpoint
grammar used to reconstruct L.  It does not print M_C, an edge-valued Cartan
slice, theta_C as a boundary term, a kinetic law, a Green domain, an
equivariant prequantum line, or a physical quotient.

No source-owned boundary action is constructed.
No analytic domain, positive pairing, polarization, reduced phase space or
physical cohomology is constructed.
No W/mirror selection, chirality, generation count or observed spectrum is
inferred.

Classical exactness upstairs also does not settle equivariant
prequantization of the compact reduced KKS levels.  That is a downstream
quantization question, not an obstruction to the classical symplectic
realization proved here.

No ledger verdict, residue, quotient, datum, canon claim or public-posture
change follows from this packet.

## Disposition and next gate

Primary A is positive:

    selected regular (5,2) chamber minimum = 98,
    all-strata minimum                     = open,
    canonical all-charge fallback          = 182.

The positive result unlocks exact edge composition.  Use M_(-C), match its
moment sign against the selected endpoint charge, compose the diagonal
moment map and existing algebraic BFV charge, and then test whether the
selected action or source owns any boundary admission or kinetic term.
Charged boundary symmetry remains the zero-import rival.

Do not enter the analytic domain, quantization or physical-cohomology stage
until that ownership comparison is complete.

## Reproduction

Run:

    sage -python tests/channel-swings/selected_k77_cartan_slice_cotangent_realization_probe.py

The probe replays the exact 29-check Cartan predecessor, constructs the
98-by-98 form and 91-by-98 moment-map certificate, checks the KKS quotient,
and exercises the singular, deleted-Cartan, product, source and hostile
controls.
