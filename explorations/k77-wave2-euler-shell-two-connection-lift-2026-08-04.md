---
artifact_type: exploration
created: 2026-08-04
title: "K77 Wave 2: action-Euler shell as a dependent two-connection complex"
grade: "Formula-level conditional construction with exact noncommutative and moving-pairing controls. The metric-density/invariant-adjoint pseudo-musical is ported to the active K77 bosonic translation row, its restricted natural-map space is one-dimensional, and the dependent shifted operator is nilpotent iff the actual translation Euler covector vanishes on a faithful coefficient module. Full local-gauge descent, all-field Ward/BV closure, analytic domain, observation, and physics remain open."
named_gate: K77_BOSONIC_EULER_PRIMALIZER_AND_ACTION_SHELL_TWO_CONNECTION_LIFT
gate_before: K77_SHIFTED_TWO_CONNECTION_OPERATOR_WITH_NAIVE_DIAGONAL_SHELL_MISMATCH
gate_after: K77_ACTION_OWNED_DEPENDENT_PAIR_TRANSLATION_SHELL_IFF_COMPLEX_ON_FAITHFUL_MODULE
route_disposition: PASS_WITH_MATERIAL_SCOPE_REPAIRS__PARTIAL_NAMED_GATE_MOVEMENT
source_collision: SOURCE_CONFIRMS_INGREDIENTS_AND_ONSHELL_COMPLEX_MOTIVATION__SOURCE_SILENT_ON_EULER_PAIR_IDENTIFICATION
fork_assumed: SIGNATURE-AMBIENT
fork_stack_acknowledged: "K77 is the source-faithful active route and this wave tests a signature-robust density-musical formula while preserving the explicit K95 re-port cost."
search_space_dim: 1
free_object_delta: -1
residue_touched:
  - id: K77-W2-ACTION-SHELL
    grade: T3
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
third_lane_promoted: false
---

# K77 Wave 2: action-Euler shell as a dependent two-connection complex

## Result first

There is now a precise conditional construction behind Weinstein's statement
that the two-connection object becomes a complex “on shell.”

Let the frozen action architecture emit its **actual** bosonic translation
Euler covector

\[
 \widehat E_T^{B,\mathrm{act}}
 \in \Omega^{13}(Y,\operatorname{ad}^{*}P),
\]

not the advertised endpoint expression that K77-B3 showed need not equal the
variation of the written noncyclic action.  Use the already-built indefinite
connection pseudo-musical

\[
 \sharp_{\mathrm{conn}}^{77}
 =(*_{G_{77}})^{-1}\kappa_{\mathfrak g}^{\sharp}
 :\Omega^{13}(Y,\operatorname{ad}^{*}P)
 \longrightarrow \Omega^1(Y,\operatorname{ad}P)
\]

and define a dependent difference and connection

\[
 \tau_E=\sharp_{\mathrm{conn}}^{77}
          \widehat E_T^{B,\mathrm{act}},
 \qquad
 A_E=B+\tau_E.
\]

Insert this pair into the shifted total-odd operator

\[
 \mathcal D_E=
 \begin{pmatrix}
 d_{A_E}&-F_B\\
 1&-d_B
 \end{pmatrix}.
\]

On a faithful coefficient module its complete square obeys

\[
 \mathcal D_E^2=0
 \quad\Longleftrightarrow\quad
 \widehat E_T^{B,\mathrm{act}}=0.
\]

The forward direction is not obtained by deleting the mixed block.  Off shell
the square is

\[
 \mathcal D_E^2=
 \begin{pmatrix}
 F_{B+\tau_E}-F_B&-\rho(\tau_E)F_B\\
 \rho(\tau_E)&0
 \end{pmatrix}.
\]

Every displayed defect is proportional to the action-derived difference and
therefore vanishes when the translation Euler row vanishes.  Conversely, the
southwest block detects `tau_E`; faithfulness of `rho` and invertibility of
`sharp_conn` then recover the Euler row.  The exact fixture uses a faithful
left-regular module and keeps the northeast defect live at an off-shell
control point.

This is a real construction advance, but a deliberately narrow one.  It does
not prove that Weinstein's unreleased 2025 pair is this pair, that the original
IG augmented-torsion pair has this dependency, or that the entire action is
stationary whenever this one Euler row vanishes.  The source status of the
pair identification is `SOURCE-SILENT`; the construction is an action-owned
conditional completion.

The focused executable passes

```text
8 source + 30 type + 29 exact + 9 planted = 76/76 PASS.
```

## Plain English

Previously we had two facts that did not line up.  Eric says the four-block
operator becomes a complex when the equations hold, but simply setting its two
connections equal made the operator square to zero even when the source action
was not at a critical point.

The repair is to stop treating the second connection as freely chosen.  The
action produces an error signal—its Euler derivative.  The metric and the
gauge-algebra pairing convert that error signal into an honest connection
difference.  Add it to the background connection.  Now the operator is a
complex exactly when that action error is zero, as long as the fields on which
the connections act can actually detect every gauge-algebra direction.

This makes the “on shell births a complex” claim mathematically coherent at
one important layer.  It does not yet show that this was Eric's intended
unreleased formula, or that the resulting equations descend to observed
four-dimensional physics.

## 0. Binding pre-wave disposition

### Fork

This wave stands on `SIGNATURE-AMBIENT=(7,7)`, the active Eric/Curt carrier.
The degree-one/thirteen Hodge-square signs happen to agree with `(9,5)` because
both signatures have odd negative index.  That does **not** identify their
real Clifford carriers or source groups.  If `(9,5)` is ultimately selected,
the form of the pseudo-musical survives but its carrier, algebra and transition
proof must be re-ported.

### Search-space dimension

The search space is one-dimensional **within the relevant restricted class**:
order-zero maps generated solely by the metric density and an invariant
symmetric form on the simple real algebra
`sp(32,32;H)`.  The standard pseudo-orthogonal module and the simple adjoint
each have scalar commutant, so the product map has one scale.  The action's
declared duality pairing fixes that scale by

\[
 \flat_{\mathrm{conn}}\sharp_{\mathrm{conn}}=1.
\]

An exact `SO(2,1) x SO(2,1)` product-action linear system has commutant
dimension one and serves as a planted-coefficient detector.  The structural
dimension statement is representation theory, not an inference from the
small fixture.

This does not classify maps allowed to introduce additional active
`epsilon`, Shiab, soldering or derivative tensors.  Those are different,
larger families and remain subject to their own owners.

### Free objects

`free_object_delta=-1`.  `A_E` is dependent on the existing action, `B`, the
metric density and the invariant adjoint pairing.  It is not an independently
varied field.  No new unowned object is introduced, and the open action-shell
pair-lift debt is retired.

### Residue

`K77-W2-ACTION-SHELL` moves to `T3`: formula-level conditional match.  It is
not `T4` physical recovery.

## 1. Layer 0

| phrase | object used here | kept distinct |
|---|---|---|
| source `Upsilon` | advertised degree-13 residual | actual noncyclic Euler derivative |
| Euler covector | `delta_T I1B` in the density dual | a primal connection one-form |
| primal residual | `tau_E=sharp_conn E_T` | IG augmented torsion chosen independently |
| two connections | dependent pair `(B,B+tau_E)` | unreleased TOE pair and the original free IG pair |
| action shell | `E_T^{B,act}=0` | all Euler rows stationary |
| complex | algebraic nilpotence of the shifted operator | common closed analytic domain/cohomology |
| converse detector | faithful associated-module action | an unspecified quotient with kernel |
| source support | ingredients and on-shell motivation | source confirmation of this reconstruction |

## 2. Source collision

The primary-source and repository result is mixed, not ambiguous:

| evidence | classification | consequence |
|---|---|---|
| TOE four blocks, two minus signs, “on shell ... a complex is birthed” | `SOURCE-CONFIRMS` | fixes the target grammar and motivation |
| TOE “never released” statement | `SOURCE-CONFIRMS-ABSENCE` | forbids claiming the missing shell map is published |
| Portal bi-connection and ad-valued difference | `SOURCE-CONFIRMS` | a connection difference is the right carrier |
| draft `dI=(Upsilon,Xi)` in degrees 13/14 | `SOURCE-CONFIRMS` | the action emits a density-dual row, not directly a one-form |
| RB1 pseudo-musical and K77 moving primalizers | `REPO-CONFIRMS` | the needed carrier conversion is inherited infrastructure |
| identification `A-B=sharp_conn(E_T^{act})` | `SOURCE-SILENT` | conditional construction, not exegesis |

The complete receipt is
[`gu-euler-shell-two-connection-source-reinspection-2026-08-04.md`](../lab/sources/gu-euler-shell-two-connection-source-reinspection-2026-08-04.md).

## 3. Inline divergent preassessment

Ten lightweight lenses were run before construction:

1. differential geometry required the difference to transform homogeneously;
2. invariant theory required a whole map-space dimension before selectors;
3. the variational bicomplex required the actual Euler derivative;
4. Krein theory prohibited a positive-Riesz reading;
5. homological algebra selected the southwest block as the converse detector;
6. gauge/BV geometry required coadjoint-to-adjoint naturality;
7. hyperbolic PDE held out closure and well-posedness;
8. physics engineering held out particle and equation matches;
9. exact computation required noncommuting coefficients and live defects; and
10. proof-systems review charged one side with overclaim and the other with
    defending the superseded “primalizer wholly unbuilt” fence.

## 4. The pseudo-musical is action-owned and indefinite

For `j in Omega1(ad P)` and a density-dual covector `eta_hat`, use

\[
 \widehat{\flat_{\rm conn}j}
 =\kappa_{\mathfrak g}^{\flat}(*_{G_{77}}j),
 \qquad
 \sharp_{\rm conn}\widehat\eta
 =*_{G_{77}}^{-1}\kappa_{\mathfrak g}^{\sharp}\widehat\eta.
\]

The exact control verifies inverse and defining-pairing identities, indefinite
signs, and

\[
 \dot\sharp=-\sharp\,\dot\flat\,\sharp.
\]

Consequently

\[
 \delta\tau_E=(\delta\sharp)E_T+\sharp\,\delta E_T.
\]

The first term vanishes on the Euler shell but must be retained off shell.  No
orientation is consumed in the absolute-density formulation; P1 remains
unused.

## 5. Exact square and the faithful-module condition

Write `rho` for the coefficient representation.  Ordinary Bianchi cancels the
`B`-only northeast term, not the mixed term.  The full block multiplication is

\[
\begin{aligned}
(\mathcal D_E^2)_{11}&=F_{B+\tau_E}-F_B,\\
(\mathcal D_E^2)_{12}&=-\rho(\tau_E)F_B,\\
(\mathcal D_E^2)_{21}&=\rho(\tau_E),\\
(\mathcal D_E^2)_{22}&=0.
\end{aligned}
\]

If `E_T=0`, invertibility gives `tau_E=0`, and all four blocks vanish.  If the
square vanishes, the southwest block gives `rho(tau_E)=0`.  The converse then
requires either:

- a faithful associated coefficient module, or
- the centerless adjoint carrier.

The exact noncommutative fixture uses a faithful left-regular module and proves
rank three for the three independent residual directions.  It does not prove
that every later physical quotient is faithful.  Identifying TOE's intended
coefficient module and preserving faithfulness under the BV/physical quotient
is now an explicit downstream obligation.

## 6. Naturality and Ward boundary

If the action Euler covector transforms coadjointly, invariance of
`kappa_g` and naturality of the metric density give

\[
 \tau_E\mapsto\operatorname{Ad}_h\tau_E.
\]

Since `A_E` and `B` receive the same inhomogeneous connection term, their
difference transforms homogeneously.  Exact controls verify homogeneous
curvature transport and cancellation of a shared inhomogeneous term.

The scope boundary matters: the finite check is not the complete moving local
gauge derivative, and the source relation `Xi=D Upsilon` is not the full
off-shell Ward identity.  The previously frozen even Ward architecture remains
the owner of moving `epsilon`, backgrounds, currents and preboundary terms.

## 7. Constraint accounting

| quantity | value |
|---|---:|
| restricted natural-map parameters | 1 |
| inverse-duality normalization constraints | 1 |
| constraint surplus | 0 |
| new free coefficients | 0 |
| free object delta | -1 |

The shell equivalence is informative construction infrastructure, but it is
definitionally action-owned.  It is not counted as positive phenomenological
surplus.

## 8. Seven-axis disposition after Layer 0

| layer | status |
|---|---|
| Layer 0 | pass with five object separations and a faithful-module condition |
| L1 source | ingredients confirmed; Euler-pair identification silent |
| L2 algebra | full shifted square and bidirectional faithful-module theorem built |
| L3 geometry | K77 density/adjoint associated-bundle pseudo-musical built; arbitrary atlas not enumerated |
| L4 variation | actual-Euler discipline, symmetric finite Hessian and moving-inverse response pass |
| L5 covariance | homogeneous and shared-term naturality pass; full local/global Ward descent open |
| L6 analytic | common closed Krein/Green/BFV domain open |
| L7 physics | no row moves |

## 9. Hostile post-review

The review disposition is
`PASS_WITH_MATERIAL_SCOPE_REPAIRS__PARTIAL_NAMED_GATE_MOVEMENT`.

Repairs made before closeout:

- restricted `search_space_dim=1` to metric-density/invariant-pairing maps;
- required a faithful coefficient action for the converse;
- kept the actual noncyclic Euler covector distinct from advertised `Upsilon`;
- downgraded source status from intended construction to source-compatible;
- kept full local-gauge Ward descent and the analytic domain open; and
- refused to count a dependent lift as positive physics surplus.

The review also rejected the stale fence that the primalizer was wholly
unbuilt: RB1 and the K77 moving-primalizer packet already provide the required
infrastructure.

## 10. Status and next gate

Earned:

```text
K77 BOSONIC PSEUDO-MUSICAL = BUILT AT SMOOTH ASSOCIATED-BUNDLE/DENSITY GRADE
DEPENDENT PAIR = A_E = B + sharp_conn(E_T^{B,act})
TRANSLATION EULER SHELL IFF SHIFTED COMPLEX = TRUE ON A FAITHFUL MODULE
SOURCE IDENTIFICATION = SILENT / CONDITIONAL
```

Held open: full action stationarity, TOE module identification, local/global
Ward/BV closure, common analytic domain, observation descent/no leakage,
vacuum and every atomic physics row.  P1/P2/P3 remain unchanged and unused;
Curt remains formally separate guidance; `TG-1 AND TG-2 AND TG-3` is not
promoted; Wave 3 remains closed.

Next named gate:

```text
K77_EULER_LIFT_FULL_FIELD_WARD_DOMAIN_OBSERVATION_PORT
```

It must place the dependent lift in the complete field/BV action, identify a
faithful quotient carrier, prove the moving local-gauge Ward and preboundary
identity, and descend the equation/square through observation without leakage.

## Reproduction

```bash
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/k77_wave2_euler_shell_two_connection_probe.py
python3 process_gates/k77_wave2_euler_shell_two_connection_scope_audit.py
```
