---
run_id: GUH-20260731T144734Z-g3-full-variational-bvbfv
status: complete
repository: gu-formalization
workflow: joe-directed-north-star-construction
mode: execute
run_type: progress
lane_id: "1"
work_item: G3-FULL-VARIATIONAL-BICOMPLEX-BVBFV
starting_revision: 34779bd20dcea70b56e3f7825297ae9ad4d99039
opened_at: 2026-07-31T14:47:34Z
closed_at: 2026-07-31T15:06:09Z
claim_status_change: none
canon_change: none
public_posture_change: none
external_action_authorization: github_commit_and_push_only
---

# G3 full variational bicomplex and BV--BFV

## Objective

Vary the corrected G2 source action through every field and graph arrow it
actually owns. Construct its bulk Euler packet, Green/presymplectic
preboundary data, coupled gauge and diffeomorphism Noether identities, and
the minimal ordinary-gauge BV completion needed to test the classical master
equation through antifield number one. Do not reinsert the G2-killed
fixed-linear source equation.

## Layer-0 precondition

| phrase | selected G3 object | object not identified with it | mark |
| --- | --- | --- | --- |
| full variation | every owner of the G2 source functional | the full N1 matter/defect action not selected in G2 | `HOMONYM`; G3 must state the boundary |
| connection equation | density-dual `E_A=E_T^var` | the primal distortion `T` or compressed `S(F_A)+kappa T` | `HOMONYM` |
| reference equation | graph return through `B=A_LC(epsilon_red,g_DW)` and `S_epsilon` | an independent `E_B=0` | `HOMONYM` |
| conservation | coupled weak Noether-II identity modulo boundary flux | isolated off-shell `D_A^!E_A=0` | `HOMONYM` |
| BV closure | ordinary gauge-subgroup minimal BV completion | super-IG, diffeomorphism, RS, or full physical BV theory | `HOMONYM` |
| BFV packet | action-derived preboundary one-form/two-form before polarization | a selected closed boundary domain or physical phase space | `HOMONYM` |
| section equation | zero for the source-only G2 bulk action | the moving-section equation of the repo-originated N1 defect comparator | `HOMONYM` |
| section coupling | Weinstein-guided observation pullback/restriction `Y -> X` | repo-originated defect pushforward/action `X -> Y` | `HOMONYM`; source recheck required before disposition |

## Construction forks

- Native geometry: trace-reversed `Y^14=Met(X^4)` with `(9,5)`,
  `Sp(32,32;H)`, Krein pairing, right-`H`, and moving reduction.
- Standard variational/BV calculus: density-dual Euler forms, the covariant
  variational bicomplex, shifted cotangent BV pairing, and BFV preboundary
  data. These tools bind the native action; they do not replace it with a
  positive-Hilbert or conventional Higgs theory.
- Selected graph: `A` free, `B=A_LC(epsilon_red,g_DW)` composite,
  `T=A-B`, and `S_epsilon` plus `flat_1` composite. `A0` and N1's independent
  `U/P/current` family remain comparators rather than simultaneous fields.

## Frozen action

```text
I_G2 = integral T wedge S_epsilon(
         F_B + 1/2 D_B T + 1/3 q(T,T))
       + kappa_1/2 integral T wedge flat_1(T).
```

The `T` Euler seed is frozen to the G2 result

```text
E_T = S_epsilon(F_B)
      + 1/2(L+L^!)T
      + M_epsilon(T,T)
      + kappa_1 flat_1(T).
```

## Pre-registered expected verdict

The graph-complete bulk gauge identity is expected to pass, while isolated
off-shell connection conservation is expected to fail: the moving reduction
equation must cancel it. The action should emit a nonzero thirteen-form
preboundary potential. Without the G4 polarization/domain, it should not yet
define a reduced BFV phase space or a differentiable boundary-value problem.

The ordinary gauge algebra is expected to admit the standard minimal BV
completion. A literal truncation containing field antifields but omitting the
ghost-antifield bracket term is expected to fail for the nonabelian algebra;
adding that forced term should close the master equation through antifield
number one. Full diffeomorphism/super-IG/matter BV closure is expected to
remain open because those fields and symmetries are not yet in the selected
action.

## Kill and downgrade conditions

1. Failure of the exact all-slot derivative kills the G2 action packet.
2. Omitting `delta T=delta A-delta B`, `delta S_epsilon`, `delta flat_1`,
   Hodge/density response, or the first-order LC graph response kills a claim
   of full source-sector variation.
3. A nonzero complete gauge variation kills the coupled Noether/BV packet.
4. A vanishing isolated connection term does not count as a positive control;
   a Stueckelberg-shaped fixture must make it nonzero while the joint identity
   vanishes.
5. A boundary term discarded as a bulk zero kills differentiability.
6. A BFV phase space claimed without quotienting the preboundary kernel or
   selecting a G4 polarization/domain is rejected.
7. Field-antifield terms without the nonabelian ghost-antifield bracket fail
   the antifield-one master-equation test.
8. A source-only zero section response may not be promoted to the section
   equation of the later bulk-plus-defect theory.
9. Before a missing Eric-lane mechanism is classified as a failure, recheck
   the verified Weinstein primary-source set and record both positive and
   negative receipts. Build a supplied source route first; debit repo-added
   alternatives explicitly.
10. No standard positive-Hilbert, fixed Clifford plane, raw `(7,3)` fibre,
   independent `B`, additive vacuum term, or hidden complex unit is admitted.
11. P1, P2, P3, a form degree, a ghost number, or a BV stage may not be read as
    chirality, an index, or observed generation count.

## Primary-source recheck correction

The G3 absence of a section field triggered the Eric-lane gate. The recheck
found a repeated author-guided route: construct ambient fields/equations on
`Y^14` and pull them back along a metric section to `X^4`. It did not find a
supplied defect action, varied embedding equation, or distributional ambient
source. Therefore the G3 bulk action is not downgraded for failing to emit a
four-dimensional defect. G4 owns the pullback/retract, equation-dual, and
off-slice leakage tests. Receipt:
`lab/sources/g3-weinstein-section-pullback-recheck-2026-07-31.md`.

## Constraint-surplus policy

No new physical coefficient is admitted. Formal adjoints, graph derivatives,
the presymplectic current, and the ordinary-gauge ghost bracket are forced by
the written action and gauge algebra. Boundary polarization, domain,
normalization, stationary orbit, physical projections, and P3 remain unpriced;
global surplus is therefore `UNCOMPUTABLE`.

## Planned outputs

- a graph-complete source-sector Euler and dependency specification;
- an action-derived preboundary/BFV packet;
- coupled gauge/diffeomorphism weak identities with their exact scope;
- a minimal ordinary-gauge BV certificate through antifield number one;
- exact rational controls with isolated-Ward, frozen-graph, omitted-response,
  boundary, and ghost-term plants;
- navigation, validation, commit, push, and close receipt.

## Boundary

G3 does not claim G4's ultrahyperbolic domain or observation retract, G5's
matter-current/Riesz weld, a full N1 replacement map, super-IG or complete
diffeomorphism BV closure, a stationary vacuum, Standard Model spectrum,
Higgs realization, anomaly closure, index, count, cosmological amplitude, or
PP3.

## Completed result

- Constructed the graph-complete all-slot derivative of the corrected G2
  action and returned the primitive covectors through the moving
  Levi--Civita, Shiab, metric, and distortion graph.
- Demonstrated an exact coupled first-jet gauge Ward cancellation with a
  deliberately nonzero isolated connection contribution.
- Derived nonzero preboundary and presymplectic data without promoting them to
  a selected BFV phase space.
- Built the ordinary-gauge minimal BV completion through antifield number one;
  the nonabelian ghost-antifield bracket is forced.
- Ran the Eric-lane primary-source gate. The checked sources guide an
  observation pullback/restriction construction, not a defect action emitted
  by the bulk functional. G4 now owns the retract, operator intertwining,
  equation-dual, leakage, and domain tests.

## Validation

- G3 exact certificate: `25 exact checks + 13 planted failures = 38 PASS`.
- Guided tilted-source comparator: `14 exact + 4 planted = 18 PASS`.
- Old-versus-Eric ten-lens contract: `19 exact + 10 planted = 29 PASS`.
- G1 and G2 regressions: `29 PASS` and `22 PASS` respectively.
- RB1b, RB1c, RB2, N3, and full-20 chimeric-BV regression suites: all
  controls passed.
- Python compilation, JSON parsing, test-manifest/root-test inventories, and
  `git diff --check`: pass. The broader runbook-link audit has an unrelated
  starting-revision mismatch: tracked
  `lab/process/runbooks/publication-status-reconciliation.md` is not linked
  from that directory's README. G3 did not modify either surface.
