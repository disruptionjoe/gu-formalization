---
run_id: GUH-20260731T155148Z-eric-physics-source-callout-crosswalk
status: completed
repository: gu-formalization
workflow: joe-directed-source-traceability
mode: execute
run_type: progress
lane_id: "1"
work_item: ERIC-PHYSICS-SOURCE-CALLOUT-CROSSWALK
starting_revision: 2316d7d2356ef213a48fef7b30105cd284c951ef
opened_at: 2026-07-31T15:51:48Z
closed_at: 2026-07-31T15:58:16Z
claim_status_change: none
canon_change: none
public_posture_change: none
external_action_authorization: github_commit_and_push_only
---

# Eric physics-component primary-source callout crosswalk

## Objective

Add primary-source callouts to the Eric-native equation atlas for Maxwell,
Yang--Mills, Einstein, Higgs, Dirac, Schrödinger, weak force, strong force,
dark energy, and dark matter. Distinguish direct GU construction statements,
standard-physics setup, contextual mentions, formula-bearing manuscript
sources, and no located native claim.

## Layer-0 precondition

| phrase | selected meaning | not identified with it |
| --- | --- | --- |
| source callout | checked primary-source passage that speaks about the named component | proof that the proposed GU replacement works |
| direct | passage gives a GU placement, replacement, or construction relation | mere use of the component's name |
| contextual | historical, standard-model, or motivational discussion | native GU equation |
| weak/strong force | physical gauge sectors and their group-theoretic carriers | any occurrence of the adjectives “weak” or “strong” |
| dark matter | proposed nonluminous matter/representation sector | dark energy or a generic invisible field |
| Schrödinger | an actual Schrödinger equation/evolution prescription | generic quantum, wavefunction, geometric-quantization, or Dirac-square language |

## Pre-registered expected result

Oxford/Portal should be the clearest early equation dictionary; the 2025 TOE
episode should supply the “you are in GU” and modern distortion/fermion/dark
sector claims; the 2025 Into the Impossible/UCSD seminar should supply the
most explicit Higgs, force-group, dark-energy, and dark-matter construction
language; the 2021 working draft should remain the controlling formula source
for the action and zero-order mass carrier. No GU-native Schrödinger equation
is expected in the checked Weinstein corpus.

## Kill conditions

1. A standard-physics explanation may not be reported as a constructed GU
   replacement.
2. A nearby quantum/wavefunction passage may not be reported as Schrödinger.
3. Group labels alone may not be reported as derived weak/strong dynamics.
4. Dark energy and dark matter may not be conflated.
5. The 2020/2025 Into the Impossible episodes and the 2021 *GU Revealed*
   episode must not be conflated.
6. Automated transcripts retain their source grade and transcription caveat.

## Planned outputs

- source-callout column in the readable equation atlas;
- ten-row machine-readable primary-source crosswalk;
- executable completeness/directness/absence controls; and
- validation, commit, push, and close receipt.

## Boundary

This run changes source traceability only. It does not promote a component to
`BUILT`, validate Weinstein's equations, construct the observation map, or
change any scientific verdict.

## Joe correction applied

A source callout is not merely a provenance footnote. Each passage now emits
a prospective native construction directive. An absent explicit formula does
not terminate the row: the source's geometric architecture identifies the
carrier/operation to construct, while the repo labels any additional bridge as
a synthesis rather than an author statement. Schrödinger is the worked edge
case: no direct GU equation was located, so the source's geometrize-the-quantum
direction routes to an action-derived Hamiltonian/unitary-flow test on the
G4-reduced BV/BFV/Krein physical phase space.

## Result

The atlas now contains a ten-row primary-source crosswalk for Maxwell,
Yang--Mills, Einstein, Higgs, Dirac, Schrödinger, weak force, strong force,
dark energy, and dark matter. Every row records:

1. exact source surface and timestamp/section;
2. whether the passage is a standard baseline, direct GU placement,
   group/representation claim, contextual quantum direction, or formula
   source;
3. the exact G2/G3/G4/G5 carrier, Hessian block, stabilizer, odd complex,
   observation map, or Hamiltonian flow to construct; and
4. the Layer-0 guard preventing a spoken relation from becoming a premature
   recovery claim.

The strongest routing consequences are:

- Maxwell is the abelian massless summand of the same reduced connection
  Hessian, not a separate action;
- Yang--Mills is sought in the reduced second variation of the first-order
  native parent after `F^2` ablation;
- Einstein is the equation-dual pullback and spin-two quotient of the corrected
  total Euler packet;
- Higgs is sought in a vertical ad-valued one-form mode whose curvature
  expansion and fermion incidence jointly emit the full role;
- Dirac is the odd square-root action/complex emitting propagation, mass,
  current, and constraints together;
- weak and strong sectors are branches of one action-selected maximal compact
  stabilizer and Hessian kernel;
- dark energy is the stationary light scalar/trace distortion with derived
  observation stress; and
- dark matter is the complement of the luminous physical odd image with
  parameter-dependent high-curvature recoupling.

## Validation

| command | result |
| --- | --- |
| `python3 -m json.tool lab/process/eric-native-physics-equation-replacement-atlas.json` | PASS |
| `python3 tests/channel-swings/eric_native_physics_equation_atlas_probe.py` | 46 exact + 14 planted = 60 PASS |
| `python3 -m py_compile tests/channel-swings/eric_native_physics_equation_atlas_probe.py` | PASS |
| `python3 tests/channel-swings/weinstein_primary_source_reinspection_contract.py` | PASS |
| `python3 tests/channel-swings/weinstein_guided_source_action_probe.py` | 18 PASS |
| `python3 tests/channel-swings/g1_derivative_cocycle_moving_reference_probe.py` | 29 PASS |
| `python3 tests/channel-swings/g2_native_variational_shiab_probe.py` | 22 PASS |
| `python3 tests/channel-swings/g3_full_variational_bvbfv_probe.py` | 38 PASS |
| `python3 tests/channel-swings/geometry_first_orthodoxy_lane_odds_probe.py` | 19 PASS |
| `git diff --check` | PASS |

## Handoff

The source crosswalk now sharpens G3.5/G4 rather than displacing them. The
next construction should use the ten native directives as required output
labels for one target-blind naturality census, observation/domain packet, and
stationary reduced Hessian. Familiar physics labels remain sealed during the
calculation and are attached only when the frozen source-directed carriers
survive their intertwining tests.
