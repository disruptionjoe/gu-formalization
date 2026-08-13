---
artifact_type: construction_result
created: 2026-08-11
run_id: RUN-20260811-030337-gu-k77-coupled-gauge-noether-bv
lane: "1"
functional_channels: [BUILD, COMPOSE, SOURCE, VERIFY]
ledger_version: "0.164"
result: COUPLED_ORDINARY_GAUGE_NOETHER_BV_CLOSES_ON_VARPI_AND_FOUR_INDEPENDENT_FERMIONS__GAUGE_MULTIPLICITY_COMMUTANT_LEAVES_AT_LEAST_GR3_15_OF_RANK384_CARRIERS__NO_CARRIER_SELECTION__COUPLED_GREEN_DOMAIN_NEXT
grade: "EXACT local ordinary-gauge BRST/Noether composition and pointwise multiplicity-commutant theorem; global action domain, physical cohomology and selection excluded"
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Coupled K77 ordinary-gauge Noether/BV complex

## Plain-English result

The ordinary gauge-symmetry piece is now complete at the local algebraic level
for the source's actual field list: the connection, `zeta`, `nu`, and their two
independent barred partners. The nonabelian ghost differential closes exactly,
the two fermion residuals transform covariantly, and the four-field fermion
density is invariant off shell.

But this symmetry does not choose the smaller matter carrier we were looking
for. It acts on the 128-dimensional spinor factor while leaving the fifteen
zero/one-form slots as a multiplicity space. Any three-plane in those fifteen
slots therefore gives a gauge-invariant rank `3*128=384` carrier. Gauge
symmetry can preserve a carrier supplied by some other construction, but it
cannot tell us which one to use.

This closes one necessary source-action obligation and prevents another long
projector search. The next useful construction is the actual coupled
boson-plus-four-fermion Green/preboundary form and its gauge-basic,
constrained-real Lagrangian domains.

## Layer 0

The following remain distinct:

1. ordinary gauge symmetry of the connection and matter;
2. characteristic propagation of the fermion symbol;
3. a local BRST/BV differential;
4. a global BV/BFV phase space and physical cohomology;
5. a supplied gauge-invariant carrier;
6. selection of one carrier by the action; and
7. an external datum.

The v0.163 theorem killed item 2 as a source of item 3. This Run constructs
item 3 directly from item 1 and proves that it does not supply item 6.

## Prior-art composition

- G3 had already proved the nonabelian connection BRST algebra and forced the
  ghost-antifield bracket term.
- B2C9 had already proved the full first-jet Ward identity for independent
  barred/unbarred matter.
- The draft had already supplied the four-field covariance grammar.
- v0.163 had already proved that no fermion-only principal generator exists.

Those results had not been composed into one field-complete complex or tested
against the rank-384 selection problem. Recomputing the old pieces would have
been construction debt; the new information is the composition and the
multiplicity theorem.

## Minimal differential

With `c` the odd ordinary-gauge ghost,

\[
\begin{aligned}
s\varpi &= [c,\varpi]-dc, & sc&=c^2,\\
s\zeta &= c\zeta, & s\nu&=c\nu,\\
s\bar\zeta&=-\bar\zeta c, & s\bar\nu&=-\bar\nu c,\\
sM_{ij}&=[c,M_{ij}].
\end{aligned}
\]

An exact exterior-algebra fixture uses three Grassmann generators and
noncommuting rational matrices. It verifies `s^2=0` on every displayed field,
including the connection first jet and all four zero-order operator blocks.
Both fermion residuals obey `sR=cR`, so

\[
s(\bar\zeta R_\zeta+\bar\nu R_\nu)=0
\]

without imposing any equation of motion. Freezing `dc`, omitting it from the
matter jet, or freezing noncentral zero-order blocks fires three planted
failures.

## Exact no-selection theorem

At a point, the unbarred carrier is

\[
(\Lambda^1\oplus\Lambda^0)\otimes S
\cong \mathbb F^{15}\otimes S,
\qquad \dim S=128.
\]

Ordinary internal gauge transformations act as `I_15 tensor rho`. Therefore
every projector `P_L tensor I_S`, for a subspace `L` of the form-multiplicity
factor, commutes with the gauge action. Taking `dim L=3` gives rank `384`.

The exact probe constructs two distinct equal-rank projectors: a coordinate
three-plane and a graph three-plane. Both commute with a noncentral generator.
More generally the graph chart in `Gr(3,15)` has

\[
3(15-3)=36
\]

continuous coordinates. Thus ordinary gauge covariance leaves at least this
family of rank-384 carriers and selects none. Keeping the full `U(64,64)`
comparator or the two `U(32,32)` halves does not remove the form-multiplicity
commutant.

This does not prove that v0.161's particular rank-384 common hull is gauge
invariant, nor does it revive that hull as action-owned. It proves the broader
selection statement: gauge invariance alone cannot uniquely choose a
rank-384 carrier even when such carriers are invariant.

## Hostile boundary

- Local BRST nilpotence is not a global BV master action on a closed domain.
- Gauge invariance is not hyperbolicity, positivity, observation descent or
  physical cohomology.
- The multiplicity theorem assumes ordinary pointwise gauge action on the
  spinor factor; a new symmetry acting nontrivially on form slots would be a
  different construction and must be source/action owned.
- No chirality, mass, index, generation count or observed current is derived.
- P1/P2/P3 remain unused and cannot turn covariance into a local projector.

## Frontier

```text
headline_delta: none
frontier_conditions_closed: 2
  - coupled local ordinary-gauge Noether/BRST closure on all source fields
  - ordinary gauge symmetry as a unique rank-384 carrier selector is killed
frontier_conditions_opened: 1
  - coupled symmetrized boson/fermion Green form and constrained-real domain
remaining_named_conditions: 2
  - action-owned gauge-basic Lagrangian domain and physical BV/BFV quotient
  - observation, chirality, mirror, index/count and physics rendezvous
```

## Next gate

`BUILD_THE_COUPLED_SELECTED_ACTION_BOSON_PLUS_FOUR_FERMION_SYMMETRIZED_GREEN_PREBOUNDARY_FORM_AND_CLASSIFY_GAUGE_BASIC_CONSTRAINED_REAL_LAGRANGIAN_DOMAINS_WITHOUT_A_FITTED_PROJECTOR`.

Probe:
`tests/channel-swings/selected_k77_coupled_gauge_noether_bv_probe.py`.

Machine result:
`lab/process/selected-k77-coupled-gauge-noether-bv.json`.
