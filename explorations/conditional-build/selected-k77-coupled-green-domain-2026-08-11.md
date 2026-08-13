---
artifact_type: construction_result
created: 2026-08-11
run_id: RUN-20260811-033947-gu-k77-coupled-green-domain
lane: "1"
functional_channels: [BUILD, COMPOSE, SOURCE, VERIFY]
ledger_version: "0.165"
result: SYMMETRIZED_TOTAL_PREBOUNDARY_FORM_EXACT__FULL_CARRIER_SMALL_GAUGE_BASIC_LAGRANGIAN_GRAPHS_EXIST_CONDITIONALLY__FIXED_FERMION_REALITY_VALID__NAIVE_MOVING_TOTAL_REALITY_REJECTED__AT_LEAST_120_GRAPH_COORDINATES_UNSELECTED__ACTUAL_K77_ANTILINEAR_CALDERON_DOMAIN_NEXT
grade: "EXACT finite symplectic/variational comparator and full-carrier dimension theorem; physical anti-linear K77 domain, global analysis and BFV quotient excluded"
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected K77 coupled Green/domain gate

## Plain-English result

The selected action now has one common algebraic boundary form for its bosonic
variables and all four independent fermion variables. It is nondegenerate and
contains the extra mixed terms caused by the moving normal coefficient; those
terms disappear if the coefficient is incorrectly frozen.

Compatible boundary conditions exist. Bosonic Dirichlet data together with a
symmetric graph relating barred and unbarred fermion traces gives a
half-dimensional, gauge-invariant Lagrangian subspace. But there is not one
such graph: even the smallest separable family has 120 coordinates. Ordinary
gauge symmetry and the Green form preserve every member and select none.

The most obvious reality extension also fails a decisive check. Its
fermion-only, fixed-normal part is anti-symplectic, but extending it across the
moving bosonic normal does not preserve the total form. The mixed terms are
exactly where it fails. So this Run proves conditional domain existence while
also showing that the actual moving K77 anti-linear reality/Calderon domain is
a new action-owned construction, not bookkeeping and not something P1/P2/P3
currently supplies.

## Layer 0

The following are different objects:

1. the preboundary one-form and its field-space exterior derivative;
2. a Green bilinear and a Green inverse/operator;
3. a finite algebraic Lagrangian trace relation and a closed Sobolev domain;
4. a symmetric graph and the source-selected anti-linear K77 reality;
5. small-gauge basicness and unrestricted BFV reduction;
6. domain selection and rank-384 carrier selection; and
7. an admissible family and an action-selected member.

This Run closes only the algebraic form and existence/classification pieces.

## Prior-art composition

- The selected K77 bosonic action already owned the endpoint pair and a live
  unrestricted boundary moment map.
- B2C9 already derived an unsymmetrized four-independent-field comparator and
  explicitly left the symmetrized total form open.
- B2C5's common energy/Green-domain attempt was built on the active K95 horn
  and explicitly left the K77 domain open.
- Ledger v0.164 already closed the local ordinary-gauge BRST complex and proved
  that gauge symmetry cannot select a rank-384 carrier.

The new work is their coupled symplectic composition and the exact
non-uniqueness/naive-reality obstruction.

## Symmetrized total form

Write the boundary variables as `(q,p,psi,bar-psi)`. With the moving normal
coefficient `A(q)`, the finite comparator uses

\[
 \Theta = p\,\delta q
 +\frac12\left(\bar\psi A(q)\,\delta\psi
 -\delta\bar\psi A(q)\psi\right).
\]

Taking the field-space exterior derivative produces the canonical bosonic
pair, both independent-dual fermion endpoint terms, and two classes of
`delta A` mixed terms. The exact `64 x 64` rational fixture is antisymmetric
and full rank. Planted same-sign and frozen-`A` comparators both fire.

For the actual carrier, the bosonic endpoint rank is `10` and each fermion
trace packet has rank

\[
 15\cdot128=1920.
\]

The total boundary rank is therefore `20+1920+1920=3860`; a Lagrangian trace
relation has rank `1930`. This is a dimension theorem, not a claim that the
finite rational comparator supplies the global analytic K77 domain.

## Conditional Lagrangian graphs

Set `delta q=0`, leave `delta p` free, and impose

\[
 \delta\bar\psi=(T\otimes K)\,\delta\psi,
 \qquad T=T^t\in GL(15).
\]

The exact probe constructs two distinct choices. Each is half-dimensional,
isotropic for the moving total form, invariant under a noncentral ordinary
gauge generator, and small-gauge basic. A nonsymmetric `T` fires the planted
non-isotropy control.

The separable symmetric family alone has

\[
 \dim\operatorname{Sym}^2(\mathbb F^{15})=120
\]

coordinates. This is a lower bound on ambiguity inside the tested class, not
an exhaustive classification of every physical boundary condition. Supplying
an unrestricted member would add at least 120 function-valued choices, so it
is not silently booked into the current residue.

## Reality obstruction

For fixed `A`, the exchange

\[
 (\psi,\bar\psi)\longmapsto
 ((T\otimes K)^{-1}\bar\psi,(T\otimes K)\psi)
\]

is an involutive anti-symplectic map whose fixed space is the graph above.
The naive total extension `q -> -q`, `p -> p` is still an involution and has
the desired fixed graph, but it is not anti-symplectic for the total moving
form. The live `delta A` terms obstruct it.

That failure prevents a common category error: an algebraic fixed graph is
not yet the moving anti-linear K77 reality required by the physical action.

## Hostile boundary

- The comparator is rational and even. It does not implement Grassmann
  functional analysis or the actual K77 anti-linear conjugation.
- No Sobolev trace theorem, Calderon projector, maximal dissipativity,
  hyperbolicity, positivity, Fredholm property or Green inverse is proved.
- Compact/boundary-vanishing gauge transformations are basic, while
  unrestricted boundary transformations retain a nonzero moment map.
- The full `1920+1920` fermion trace carrier is used. No fitted rank-384
  projector is introduced.
- No chirality, mirror removal, mass, spectrum, index, generation count,
  observed current or particle physics is derived.
- P1/P2/P3 remain unchanged and unused.

## Frontier

```text
headline_delta: none
frontier_conditions_closed: 2
  - exact symmetrized total boson-plus-four-fermion preboundary form
  - conditional full-carrier small-gauge-basic Lagrangian graph existence and non-uniqueness
frontier_conditions_opened: 1
  - action-owned moving anti-linear K77 reality/Calderon or maximal-dissipative domain
remaining_named_conditions: 2
  - global domain descent and unrestricted BFV edge completion
  - observation, chirality, mirror, index/count and physics rendezvous
```

## Next gate

`CONSTRUCT_THE_ACTUAL_K77_ANTILINEAR_REALITY_ANTI_DUALIZER_AND_TOTAL_CALDERON_OR_MAXIMAL_DISSIPATIVE_PROJECTOR_FROM_THE_SELECTED_ACTION__TEST_GLOBAL_DESCENT_AND_UNRESTRICTED_BFV_EDGE_COMPLETION__DO_NOT_SUPPLY_A_120_FUNCTION_GRAPH`.

Probe: `tests/channel-swings/selected_k77_coupled_green_domain_probe.py`.

Machine result: `lab/process/selected-k77-coupled-green-domain.json`.
