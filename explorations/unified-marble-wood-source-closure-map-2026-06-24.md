---
title: "Unified Marble/Wood Same-Source Closure Map"
date: "2026-06-24"
status: exploration/closure_map
doc_type: unified_marble_wood_source_closure_map
verdict: "SAME_SOURCE_CLOSURE_CRITERION_DEFINED; CURRENT_REPO_OPEN_CONDITIONAL_AND_PARTIAL"
owned_path: "explorations/unified-marble-wood-source-closure-map-2026-06-24.md"
optional_audit: "tests/unified_marble_wood_closure_audit.py"
depends_on:
  - "process/runbooks/five-lane-frontier-run.md"
  - "explorations/primary-gu-interface-contract-2026-06-24.md"
  - "explorations/source-geometry-not-quantized-gravity-contract-2026-06-24.md"
  - "explorations/gr-shadow-recovery-certificate-2026-06-24.md"
  - "explorations/qft-shadow-extraction-certificate-2026-06-24.md"
  - "explorations/matter-gauge-source-geometry-selector-gate-2026-06-24.md"
  - "explorations/finite-control-provenance-audit-2026-06-24.md"
  - "explorations/live-claim-dag-fault-finality-ledger-2026-06-24.md"
---

# Unified Marble/Wood Same-Source Closure Map

## 1. Verdict

Einstein's marble/wood complaint is the right pressure test for the ambitious GU branch.
In GR, `G_mu_nu` is the principled geometric marble candidate, `T_mu_nu` is the
phenomenological stress-energy wood, and `Lambda g_mu_nu` is a geometric-looking patch on
the marble side unless a source branch gives it provenance. The strongest GU steelman is
not:

```text
make the left side geometric, then paste ordinary matter on the right.
```

The strongest version is:

```text
recover both marble and wood as observer-facing shadows of one deeper source geometry.
and separately decide whether the Lambda/dark-energy patch is zero, imported,
phenomenological, or source-derived.
```

Current decision:

```text
SAME-SOURCE-CLOSURE:
  criterion defined here;
  not currently closed.

Current repo state:
  GR/marble shadow: specified open; metric extraction typed, exact GR not certified.
  Lambda/dark-energy patch: open; no source-derived replacement certificate.
  QFT/wood shadow: blocked before state space, state, observables, and Born probabilities.
  SM matter/gauge: partial; Pati-Salam branch derived, full SM finite control not derived.
  finite-control selectors: no selector succeeds; host/import/control split is active.
  measurement: executable controls only; GU-derived rho_AB and observables absent.
  generation count: open; compact/K3 arithmetic remains control-only.
  black holes/cosmology: exact Schwarzschild/Kerr and theta-xi remain open action gates.
```

This is not a negative verdict on the source-geometry program. It is a closure map. It
keeps open the heterodox possibility that the metric/geometric marble itself is premature:
the 4D metric, Einstein tensor, stress-energy tensor, QFT state, matter multiplets, and
measurement records may all be downstream shadows of `G_src`, not primitive ingredients.
It also keeps open the possibility that a cosmological-constant-looking term is a dynamic
source-geometric shadow, while forbidding any claim that GU has already derived or
cancelled `Lambda`.

The repo may still use ordinary GR, ordinary QFT, finite Connes data, compact K3 controls,
and phenomenological parameters as controls or imported branches. It may not call those
same-source closure unless the provenance shows that the same branch of
`G_src/S_GU/D_GU` supplies both sides.

## 2. Same-Source Closure Criterion In Plain English And Formal Terms

Plain English:

A GU branch satisfies same-source marble/wood closure only if the same source package
that produces the observer metric and Einstein-shadow equation also produces the
observer-facing matter/QFT/stress-energy side. It is not enough to make the metric a
section shadow and then import a conventional QFT stress tensor. It is also not enough
to derive representation labels and then assume a Hilbert space, state, observables, or
Higgs potential.

The criterion is branch-local. A proof for one branch does not close another branch.

Formal source package:

```text
G_src =
  (Y, g_Y, P, S, A, D_GU, S_GU,
   IG_data, variation_space, section_space,
   boundary_domain_data, observer_access, provenance_rules)

branch =
  (IG_variation_rule, source_law, gauge_constraints, vacuum_or_state_data)

R_same =
  (R_GR, R_Lambda, R_QFT, R_SM, R_MEAS, R_RECORD, R_T)
```

Same-source closure requires one fixed tuple:

```text
C_same =
  (G_src, branch, D_GU, S_GU, R_same)
```

and all of the following outputs from that tuple:

```text
R_GR(C_same, s)
  -> (X, g = s^* g_Y, Pi_4D(E_src), GR limits)

R_Lambda(C_same, s)
  -> Lambda_eff = 0, imported constant, phenomenological control,
     or source-derived dynamic dark-energy term with anti-fitting test

R_QFT(C_same, s, O)
  -> (field algebra or Hilbert/Fock space, positive states,
      admissible observables, dynamics, probabilities)

R_SM(C_same, s)
  -> (G_obs, matter reps, Higgs shadow, anomaly shadow, n_gen status)

R_T(C_same, s, omega)
  -> T_shadow[g, omega, fields] with provenance and conservation

R_MEAS(C_same, O)
  -> (rho_AB or state family, local +/-1 observables, Born probabilities)
```

Closure condition:

```text
same_source_closed(C_same) iff
  source_object_closed(C_same)
  and branch_variations_closed(C_same)
  and metric_shadow_derived(C_same)
  and lambda_patch_status_declared(C_same)
  and qft_shadow_derived(C_same)
  and matter_selector_or_declared_import(C_same)
  and stress_energy_derived_or_declared_import(C_same)
  and conservation_projected_from_source(C_same)
  and black_hole_and_cosmology_gates_pass_or_are_scoped(C_same)
  and no_forbidden_target_input_occurs_upstream(C_same).
```

The strict version requires:

```text
stress_energy_derived_or_declared_import = derived
matter_selector_or_declared_import = derived or source-selected
```

The honest weaker versions are:

```text
host       ambient source contains a slot, but no selector chooses it;
import     matter/QFT/stress-energy is supplied externally;
control    compact, finite, Bell, or phenomenological object tests a route;
conditional an upstream source/action/operator proof would close the route;
open       a named proof packet is missing.
```

Same-source closure fails for any branch that uses different source branches for the
left and right sides:

```text
R_GR(G_src_branch_a) plus R_QFT(G_src_branch_b) != same-source closure.
```

## 3. Pipeline From G_src/S_GU/D_GU To Metric/Einstein Shadow And Stress-Energy/Matter/QFT Shadow

The desired pipeline has two synchronized legs. The point is not that the two legs must
look symmetric. The point is that they must have the same upstream source.

```text
Stage 0: Source package
  G_src, D_GU, S_GU, branch, variation_space, boundary/domain data.

Stage 1: Source equations and physical complex
  E_src = (E_s, E_A, E_IG, E_Psi, E_lambda_or_E_U) = 0
  physical field complex / gauge quotient / domains / adjoints.

Stage 2A: Marble leg
  section extraction:
    g = s^* g_Y
    A_s = s^* A
    theta_s = s^* theta
    B_s = II_s^H

  4D projection:
    Pi_4D(E_src)
      = G[g] + Lambda_eff g - kappa_eff T_shadow - R_shadow = 0.

Stage 2A-Lambda: Patch/dark-energy route
  Lambda_eff must be one of:
    zero for the branch;
    imported and labeled as a cosmological-constant input;
    phenomenological control or target window;
    source-derived dynamic term from the same S_GU/D_GU branch.

  A source-derived claim must fix coefficients before DESI/Rubin-style targets,
  derive the term from the written branch action/operator, preserve conservation,
  and avoid using `xi_eff` as a fitted rescue knob.

Stage 2B: Wood leg
  QFT extraction:
    field complex -> Hilbert/Fock space or local algebra net
    positive state omega or density matrix rho
    admissible observables
    Born probabilities
    locality, unitarity/state preservation, spin-statistics, anomaly checks.

  Matter/gauge extraction:
    source carrier -> observer gauge/matter/Higgs/anomaly/generation packet.

Stage 3: Stress-energy bridge
  T_shadow must be one of:
    derived from the same source action/projection;
    derived from the same QFT shadow by a source-approved variation rule;
    explicitly imported and labeled ordinary-QFT import.

Stage 4: Conservation and known-physics tests
  source Noether/Bianchi identity
    -> nabla^mu T_shadow_mu_nu = 0
  exact Schwarzschild/Kerr witnesses or scoped failure;
  FLRW/theta-xi coefficient calculation;
  anomaly and low-energy limits;
  measurement state and probabilities.
```

For a strict same-source theorem, the stress-energy tensor is not a free right-hand-side
placeholder. It is the observer-facing image of the wood leg and the variation/projection
of the same source package:

```text
T_shadow_mu_nu
  = T_mu_nu[R_QFT(C_same), R_SM(C_same), R_T(C_same)]
```

or, when an effective observer action exists:

```text
T_shadow_mu_nu =
  -2 / sqrt(|g|) * delta S_shadow_matter / delta g^{mu nu},

S_shadow_matter = R_action(C_same),
```

with `S_shadow_matter` itself produced by the source reduction, not imported after the
metric is extracted.

Current repo position on this pipeline:

| stage | current supplied object | current decision |
|---|---|---|
| Source package | `I_GU` typed; `D_lambda` typed as proposal; `S_GU` slots named | partial; primary action/operator underdefined |
| Source equations | EL tuple specified as required | blocked until branch-fixed action and IG variation are written |
| Marble leg | `g=s^*g_Y` typed; GR-shadow certificate specified | specified open; exact GR not certified |
| Lambda/dark-energy patch | theta-xi target window and branch warnings exist | open; no source-derived `Lambda_eff` or dynamic replacement certificate |
| Wood leg QFT | extraction schema written | blocked before state space/state/observables |
| Wood leg matter | Pati-Salam branch derived; Higgs slots hosted | partial; full SM finite-control selector absent |
| Stress-energy bridge | not yet a source-derived bridge | open; right-hand side not same-source closed |
| Conservation | branch-specific burden named | blocked until source law and Noether/Bianchi projection are proved |
| Known-physics tests | weak-field bounded pass; controls exist | exact black holes, theta-xi, generation, measurement open |

## 4. Closure Status Matrix

Legend:

```text
derived          computed from allowed source data without target input
derived_relative computed after a named upstream branch/embedding is supplied
hosted           ambient source contains a slot but does not select it
imported         externally supplied ordinary physics or finite-control data
control_only     useful executable/compact/phenomenological control, not physical proof
conditional      would close under named upstream object
blocked          cannot yet be evaluated because required object is missing
open             precise missing proof object named
failed           attempted route contradicts a gate or imports a target
```

| closure target | marble role | wood role | current strongest repo object | same-source status | first missing object | rollback trigger |
|---|---|---|---|---|---|---|
| GR shadow | 4D metric and Einstein-shadow equation | source-coupled `T_shadow` must be controlled | GR shadow certificate; `g=s^*g_Y`; weak-field bounded pass | `specified_open` | `ELProjectedGRShadowTheorem(branch)` | Schwarzschild/Kerr fail full EL tuple, or hidden matter is needed |
| Lambda/dark-energy patch | geometric-side patch beside `G_mu nu`, not principled marble by default | can mimic source or stress if untagged | theta-xi branch reduction; DESI/Rubin target windows; free-beta negative control | `open` | `LambdaDarkEnergyProvenanceCertificate(branch)` | bare `Lambda`, fitted `xi_eff`, target-tuned fluid, or coefficient inserted after data |
| QFT shadow | metric may appear as observer background/shadow | state space, state, observables, probabilities, dynamics | QFT extraction schema; VZ causal-symbol support conditional | `blocked` | `QFTStateSpaceExtractionCertificate` and `QFTStateExtractionCertificate` | no positive state space/state/observables, nonunitarity, anomaly, acausality |
| SM matter/gauge | observer gauge group must be source-selected | matter reps, Higgs, anomaly shadow | Pati-Salam one-generation branch; relative SM charges | `partial_open` | `Phi_SG_MG` or `Phi_SG_G` selector | selector consumes `A_F`, `G_SM`, `Z_6`, `K_SM`, or target matter |
| finite-control | finite shadow must be output, not input | finite algebra/module/gauge quotient if used | provenance audit; Type II_1 negative filter | `failed/open_empty` for selectors; `hosted/imported` for finite CC | target-free finite-control selector | replacement works for `n=2,4` or finite CC tuple is attached |
| measurement | observer records are downstream | `rho_AB`, admissible local observables, Born probabilities | CHSH and observer-finality controls | `controls_only` | GU-derived `rho_AB` plus measurement postulate | derived state separable, no admissible violation, or violation only from ansatz |
| generation count | affects matter shadow multiplicity | physical count must be source-index/readout | raw/K3/RS controls; branch representation story | `open` | `RS_GU^phys` plus H-linear Fredholm/index bridge | index target inserted, bridge missing, non-Fredholm, background-dependent, or wrong count |
| exact black holes | exact vacuum marble witnesses | no hidden matter on right side | exact Schwarzschild/Kerr gate | `open_blocked` | branch-fixed full EL tuple and witness fields | exact witness requires matter relabeling or residual cancellation knobs |
| FLRW/theta-xi cosmology | cosmological metric shadow | theta scalar, stress-energy, effective curvature coupling | theta-xi branch reduction; DESI-sign target known | `open` | generated `Z_theta`, `C_Rtheta`, `xi_eff` from written branch action | `xi_eff >= -0.319`, no scalar mode, or coefficient inserted by hand |
| VZ/causal propagation | controls physical cones for marble/wood dynamics | supports locality only after QFT shadow exists | typed-spine Schur principal-symbol gate | `conditional` | primary `D_GU` provenance with nonzero `Phi_d` | primary operator lacks `Phi_d` or `lambda_d=0` |
| live governance | prevents status laundering | prevents controls/imports becoming derivations | live claim DAG | `governance_active` | updated node on every status change | graph treated as physics proof |

Important same-source consequence:

```text
No current row is strict source-both closed.
The best current positive content is:
  typed source interface,
  conditional operator-spine evidence,
  specified GR/QFT certificate schemas,
  Pati-Salam branch derivation,
  finite-control negative filters,
  executable measurement controls.
```

## 5. Allowed Route Taxonomy

This taxonomy keeps useful work alive while preventing proof-slot drift.

| route | allowed use | closure strength | current examples | cannot claim |
|---|---|---|---|---|
| `source-both` | One `G_src/S_GU/D_GU/branch` derives metric/Einstein shadow and matter/QFT/stress-energy shadow. | Only route that can close strict marble/wood same-source. | Not yet instantiated. | Cannot be claimed until `SameSourceReductionPacket` exists. |
| `metric-shadow-first` | Derive `g=s^*g_Y`, 4D EL projection, black-hole/cosmology tests first; then derive wood from same branch. | Conditional classical-shadow route until wood is derived. | GR-shadow certificate; exact GR action gate. | Cannot import QFT stress-energy and call it same-source. |
| `matter-shadow-first` | Derive finite/QFT/matter state structure first; then derive the metric response and stress-energy bridge from same source. | Conditional wood-first route until marble projection is derived. | QFT state extraction and matter selector next-step lanes. | Cannot treat labels/hosts as physical states or stress tensors. |
| `ordinary_qft_import` | Use conventional SM/QFT matter on an observer metric as a comparison or phenomenological branch. | Import branch; useful but not same-source. | Ordinary anomaly checks after SM packet; external QFT controls. | Cannot be cited as GU-derived wood or same-source stress-energy. |
| `compact_control` | Use K3, finite Connes, Type II_1 hosts, Bell fixtures, compact characteristic classes as controls. | Control-only until source-to-control transport is proved. | K3 RS arithmetic, finite CC host, Pati-Salam CHSH fixture. | Cannot be physical noncompact index, selector, or measurement proof by itself. |
| `lambda_patch_dynamic_source` | Audit `Lambda g_mu nu`, theta cosmology, `xi_eff`, and dark-energy terms as a patch route requiring source provenance. | Patch route; source-derived only after certificate. | theta-xi controls; DESI/Rubin target windows; free-beta negative control. | Cannot claim GU derives/cancels Lambda or dark energy without branch-fixed source generation and anti-fitting tests. |
| `phenomenological_control` | Scan target parameters such as `xi_eff`, masses, potentials, `Lambda`, or dark-energy windows. | Target/control only. | DESI-sign negative `xi_eff` window. | Cannot be a source-derived coefficient unless generated from `S_GU`. |

Route upgrade rule:

```text
ordinary_qft_import, compact_control, and phenomenological_control
  may inform source-both,
  but they do not automatically upgrade into source-both.
```

Route downgrade rule:

```text
If a supposed source-both route imports wood, imports marble, changes branch between
left and right side, or lacks a source action/operator, it downgrades to the highest
honest row in the taxonomy.
```

## 6. Forbidden Shortcuts And Rollback Conditions

### Forbidden Shortcuts

| shortcut id | forbidden move | rollback |
|---|---|---|
| `source_geometry_by_name_only` | Naming deeper geometry without typed fields, action/operator, branch, and reductions. | Demote to interface/metaphor. |
| `metric_quantization_as_primary_start` | Defining GU as quantized 4D GR metric rather than source geometry, while claiming source-geometry closure. | Reclassify as ordinary quantum-gravity branch. |
| `left_geometric_right_imported` | Deriving `g=s^*g_Y` but importing `T_mu nu` from ordinary QFT without import label. | Demote to metric-shadow-first plus ordinary-QFT import. |
| `stress_energy_named_not_derived` | Writing `T_shadow` without a source/QFT/action variation or explicit import provenance. | Block same-source closure. |
| `branch_mismatch` | Using one branch for GR and another for matter/QFT. | Demote to branch-local partial results. |
| `compatibility_as_recovery` | Treating no contradiction as derivation. | Demote to compatibility/control. |
| `host_as_selector` | Treating ambient slots, Type II_1 embeddings, or representation containment as physical selection. | Demote to hosted. |
| `weak_field_as_exact_GR` | Promoting `O(M/r)` weak-field compatibility to exact Schwarzschild/Kerr recovery. | Demote to bounded weak-field scope. |
| `hidden_matter_relabeling` | Moving unexplained section, gauge, multiplier, or embedding residuals to `T_mu nu` in a vacuum claim. | Fail vacuum GR-shadow gate. |
| `qft_recovery_by_slogan` | Saying QFT emerges without state space, positive states, observables, probabilities, locality, unitarity, and anomalies. | Block QFT shadow. |
| `representation_labels_as_state` | Treating Pati-Salam/SM labels as a Hilbert state or density matrix. | Demote to representation branch. |
| `ansatz_state_as_measurement` | Copying Bell/product/thermal/generic vacuum states into GU measurement slot. | Demote to ansatz/control. |
| `compact_control_as_physical_index` | Using K3 or finite controls as physical noncompact GU evidence without transport. | Demote to compact control. |
| `phenomenological_term_without_source` | Inserting `xi`, `Lambda`, masses, potentials, or cross terms because a target needs them. | Demote to phenomenological control. |
| `bare_Lambda_as_marble` | Treating `Lambda g_mu nu` as principled geometry because it sits on the left-hand side. | Demote to patch/import until source provenance is supplied. |
| `dark_energy_fit_as_derivation` | Fitting `xi_eff`, a fluid, or a potential to DESI/Rubin-style targets and calling it GU-derived. | Demote to phenomenological control. |
| `free_beta_nonzero_theta` | Varying `beta` freely with only `|theta|^2` while claiming nonzero theta. | Reject nonzero-theta branch. |
| `ordinary_anomaly_as_selector` | Using ordinary SM anomaly cancellation to select the matter packet. | Demote to relative verification only. |
| `governance_as_physics_proof` | Treating the live DAG/finality layer as evidence for a physical claim. | Demote to governance. |

### Rollback Conditions

Same-source closure must roll back if any of these fire:

| condition | rollback target |
|---|---|
| `S_GU` or `D_GU` remains only a slot/proposal for the branch being cited | source-object proposal, not closure |
| primary `D_GU` lacks the first-order `Phi_d` block used by VZ support | remove dependent VZ causal support |
| free `beta` plus only the theta norm is the actual variation branch | reject nonzero theta and theta-source claims |
| exact Schwarzschild or Kerr fails the full vacuum EL tuple | no exact GR/marble closure for that branch |
| `T_shadow` requires hidden matter relabeling or target-fitted residuals | fail same-source stress-energy bridge |
| no positive QFT state space/state/observables can be extracted | fail wood/QFT closure |
| the matter selector consumes `A_F`, `G_SM`, `Z_6`, `K_SM`, physical Higgs, or `n=3` | demote matter/finite-control to imported/hosted |
| extra observer-facing modes survive with uncanceled anomaly | fail full matter/QFT shadow |
| derived measurement states are separable or all admissible observables give `CHSH <= 2` | demote physical CHSH forcing |
| compact/K3 bridge loses operator, symbol, H-linearity, Fredholm, APS, or noncompact-domain data | keep compact control-only |
| theta cosmology needs inserted negative `xi_eff` or unspecified `S_IG-dyn` | keep phenomenological/open |
| the route changes branch between GR and QFT legs | split into partial branch-local claims |

## 7. First Exact Missing Proof Packet

The first exact missing proof packet is:

```text
SameSourceReductionPacket_V0(branch)
```

It must be one packet, not two unrelated papers. Required input:

```text
source_branch_id
G_src with typed fields
D_GU with first-order and lower-order provenance
S_GU with coefficients, signs, and boundary terms
variation_space for s, A, IG data, Psi, and multipliers/dynamical fields
gauge constraints and physical field complex
section map s^*
observer access data
boundary/domain/vacuum data
provenance rules
```

Required output:

```text
1. Source EL closure
   E_src = (E_s, E_A, E_IG, E_Psi, E_lambda_or_E_U) = 0.

2. Marble reduction
   g = s^* g_Y,
   Pi_4D(E_src) =
     G[g] + Lambda_eff g - kappa_eff T_shadow - R_shadow = 0.

3. Lambda/dark-energy patch status
   Lambda_eff = 0, imported constant, phenomenological control,
   or source-derived dynamic term from the same branch.
   Any source-derived claim must pass a no-DESI/Rubin-target-input test.

4. Wood/QFT reduction
   physical field complex or local algebra,
   positive Hilbert/Fock/GNS state space,
   source-derived state omega or rho,
   admissible observables,
   Born probabilities,
   locality, unitarity/state preservation, spin-statistics, anomaly status.

5. Matter/gauge/finite selector
   G_obs or declared import,
   matter packet,
   Higgs slot plus physical projection status,
   anomaly shadow,
   generation count status,
   replacement audit.

6. Stress-energy bridge
   T_shadow derived from the same source/QFT/effective action,
   or explicitly labeled ordinary-QFT import.

7. Conservation theorem
   source Noether/Bianchi identity
     -> nabla^mu T_shadow_mu_nu = 0
   with branch-specific source law.

8. Known-physics gates
   exact Schwarzschild and Kerr witnesses or scoped branch failure,
   FLRW/theta-xi coefficient computation,
   low-energy/anomaly checks,
   measurement finite-state test when claimed.

9. Provenance and rollback ledger
   every output tagged as derived, derived_relative, hosted, imported,
   control_only, conditional, blocked, open, or failed.
```

Why this packet is first:

- Without the same branch-fixed `S_GU/D_GU`, neither marble nor wood has stable source
  provenance.
- Without the QFT state/state-space extraction, the right-hand side remains wood by import
  or slogan.
- Without Lambda/dark-energy provenance, `Lambda_eff` remains a patch/import/control
  rather than source-derived geometry.
- Without the stress-energy bridge, an Einstein-shadow equation can be written but not
  same-source closed.
- Without the exact GR and theta/cosmology tests, the marble leg remains only specified.
- Without matter/finite-control provenance, Standard Model content remains hosted/imported
  beyond the Pati-Salam branch.

The packet is allowed to return a demotion. For example:

```text
same_source_closed = false
route = metric-shadow-first + ordinary_qft_import
reason = QFTStateExtractionCertificate missing.
```

That is a useful result. The forbidden result is to leave the import untagged.

## 8. Machine-Readable Closure Map

```json
{
  "artifact": "UNIFIED_MARBLE_WOOD_SOURCE_CLOSURE_MAP",
  "version": "2026-06-24",
  "verdict": "SAME_SOURCE_CLOSURE_CRITERION_DEFINED_CURRENT_REPO_OPEN_CONDITIONAL_AND_PARTIAL",
  "status": "open",
  "not_solved": true,
  "framing": {
    "einstein_marble_wood": "G_mu_nu is principled geometric marble, T_mu_nu is phenomenological wood, and Lambda g_mu_nu is a geometric-looking patch until sourced.",
    "gu_steelman": "Do not overclaim solution; test whether marble, wood, and the Lambda/dark-energy patch can be recovered or demoted by one deeper source geometry.",
    "metric_marble_may_be_premature": true
  },
  "same_source_criterion": {
    "source_package": [
      "G_src",
      "S_GU",
      "D_GU",
      "branch",
      "variation_space",
      "boundary_domain_data",
      "observer_access",
      "provenance_rules"
    ],
    "required_reductions": [
      "R_GR",
      "R_Lambda",
      "R_QFT",
      "R_SM",
      "R_MEAS",
      "R_RECORD",
      "R_T"
    ],
    "strict_closure_requires": [
      "same_branch_for_marble_and_wood",
      "source_action_operator_closed",
      "metric_shadow_derived",
      "lambda_patch_zero_imported_control_or_source_derived",
      "qft_state_space_and_state_derived",
      "matter_selector_or_declared_import",
      "stress_energy_derived_or_declared_import",
      "conservation_projected_from_source",
      "black_hole_and_cosmology_gates_pass_or_scoped",
      "no_forbidden_target_inputs"
    ],
    "current_decision": "criterion_defined_not_currently_closed"
  },
  "pipeline": [
    {
      "stage": "source_package",
      "requires": ["G_src", "D_GU", "S_GU", "branch", "variation_space"],
      "current_status": "partial",
      "missing": ["primary_source_closed_D_GU", "branch_closed_S_GU", "fixed_IG_variation"]
    },
    {
      "stage": "source_equations",
      "requires": ["E_s", "E_A", "E_IG", "E_Psi", "source_law"],
      "current_status": "blocked",
      "missing": ["branch_fixed_full_EL_tuple", "Noether_Bianchi_projection"]
    },
    {
      "stage": "marble_metric_einstein_shadow",
      "requires": ["g_equals_s_star_g_Y", "Pi_4D_E_src", "exact_GR_tests"],
      "current_status": "specified_open",
      "missing": ["ELProjectedGRShadowTheorem", "Schwarzschild_Kerr_witnesses"]
    },
    {
      "stage": "lambda_patch_dark_energy",
      "requires": ["Lambda_eff_status", "branch_fixed_source_generation_if_claimed", "xi_eff_provenance", "DESI_Rubin_anti_fitting_test"],
      "current_status": "open_patch_control",
      "missing": ["LambdaDarkEnergyProvenanceCertificate"]
    },
    {
      "stage": "wood_qft_matter_shadow",
      "requires": ["physical_field_complex", "positive_state_space", "source_derived_state", "admissible_observables", "SM_or_matter_selector"],
      "current_status": "blocked_partial_open",
      "missing": ["QFTStateSpaceExtractionCertificate", "QFTStateExtractionCertificate", "Phi_SG_MG"]
    },
    {
      "stage": "stress_energy_bridge",
      "requires": ["T_shadow_provenance", "effective_action_or_source_projection", "conservation"],
      "current_status": "open",
      "missing": ["SameSourceStressEnergyBridge"]
    },
    {
      "stage": "known_physics_gates",
      "requires": ["black_hole_gate", "cosmology_theta_xi_gate", "anomaly_gate", "generation_gate", "measurement_gate"],
      "current_status": "open",
      "missing": ["exact_BH_pass", "generated_xi_eff", "full_anomaly_shadow", "RS_GU_phys", "rho_AB"]
    }
  ],
  "closure_matrix": [
    {
      "target": "GR_SHADOW",
      "status": "specified_open",
      "same_source_status": "not_closed",
      "current_evidence": ["g_equals_s_star_g_Y_typed", "weak_field_bounded_pass", "certificate_schema"],
      "first_missing_object": "ELProjectedGRShadowTheorem",
      "rollback_condition": "Schwarzschild_or_Kerr_fails_full_EL_or_hidden_matter_required"
    },
    {
      "target": "LAMBDA_PATCH_DARK_ENERGY",
      "status": "open_patch_control",
      "same_source_status": "not_closed",
      "current_evidence": ["theta_xi_reduction_gate", "DESI_Rubin_target_windows", "free_beta_negative_control"],
      "first_missing_object": "LambdaDarkEnergyProvenanceCertificate",
      "rollback_condition": "bare_Lambda_fitted_xi_eff_target_tuned_fluid_or_coefficient_inserted_after_data"
    },
    {
      "target": "QFT_SHADOW",
      "status": "blocked",
      "same_source_status": "not_closed",
      "current_evidence": ["certificate_schema", "conditional_VZ_causal_symbol_support", "finite_controls"],
      "first_missing_object": "QFTStateSpaceExtractionCertificate",
      "rollback_condition": "no_positive_state_space_state_or_observables"
    },
    {
      "target": "SM_MATTER",
      "status": "partial_open",
      "same_source_status": "not_closed",
      "current_evidence": ["Pati_Salam_one_generation_branch", "relative_SM_charges", "Higgs_slots_hosted"],
      "first_missing_object": "Phi_SG_MG",
      "rollback_condition": "selector_imports_A_F_G_SM_Z6_K_SM_physical_Higgs_or_n3"
    },
    {
      "target": "FINITE_CONTROL",
      "status": "failed_open_empty",
      "same_source_status": "not_closed",
      "current_evidence": ["negative_filter", "host_import_split"],
      "first_missing_object": "target_free_finite_control_selector",
      "rollback_condition": "replacement_family_works_or_finite_CC_tuple_imported"
    },
    {
      "target": "MEASUREMENT",
      "status": "controls_only",
      "same_source_status": "not_closed",
      "current_evidence": ["CHSH_fixture", "observer_finality_controls"],
      "first_missing_object": "GU_derived_rho_AB_and_admissible_observables",
      "rollback_condition": "derived_state_separable_or_only_ansatz_violates"
    },
    {
      "target": "GENERATION_COUNT",
      "status": "open",
      "same_source_status": "not_closed",
      "current_evidence": ["representation_branch", "compact_controls"],
      "first_missing_object": "RS_GU_phys_H_linear_Fredholm_bridge",
      "rollback_condition": "index_circular_nonFredholm_background_dependent_or_wrong"
    },
    {
      "target": "BLACK_HOLE_GATE",
      "status": "open_blocked",
      "same_source_status": "not_closed",
      "current_evidence": ["exact_gate_specified", "weak_field_bounded_pass"],
      "first_missing_object": "branch_fixed_Schwarzschild_Kerr_witnesses",
      "rollback_condition": "full_vacuum_EL_failure_or_residual_matter_relabeling"
    },
    {
      "target": "COSMOLOGY_THETA_XI",
      "status": "open",
      "same_source_status": "not_closed",
      "current_evidence": ["theta_xi_reduction_gate", "DESI_sign_target_window"],
      "first_missing_object": "generated_Z_theta_C_Rtheta_xi_eff",
      "rollback_condition": "xi_eff_ge_minus_0_319_or_inserted_coefficient"
    }
  ],
  "route_taxonomy": [
    {
      "id": "source_both",
      "allowed_use": "derive marble and wood from one source branch",
      "closure_strength": "strict_same_source_candidate",
      "current_status": "not_instantiated",
      "forbidden_claim": "closed_without_SameSourceReductionPacket"
    },
    {
      "id": "metric_shadow_first",
      "allowed_use": "derive metric_and_GR_projection_first_then_derive_wood_from_same_branch",
      "closure_strength": "conditional_classical_shadow_until_wood_derived",
      "current_status": "specified_open",
      "forbidden_claim": "ordinary_QFT_import_as_same_source"
    },
    {
      "id": "matter_shadow_first",
      "allowed_use": "derive_QFT_matter_state_first_then_metric_response_from_same_branch",
      "closure_strength": "conditional_wood_first_until_marble_projection_derived",
      "current_status": "blocked_partial_open",
      "forbidden_claim": "representation_labels_as_state_or_T_shadow"
    },
    {
      "id": "ordinary_qft_import",
      "allowed_use": "comparison_or_phenomenological_observer_QFT_branch",
      "closure_strength": "import",
      "current_status": "allowed_if_labeled",
      "forbidden_claim": "GU_derived_wood"
    },
    {
      "id": "compact_control",
      "allowed_use": "K3_finite_Connes_TypeII1_Bell_or_characteristic_class_controls",
      "closure_strength": "control_only_until_transport",
      "current_status": "active_controls",
      "forbidden_claim": "physical_index_selector_or_measurement_proof_without_bridge"
    },
    {
      "id": "lambda_patch_dynamic_source",
      "allowed_use": "audit_Lambda_gmunu_theta_xi_and_dark_energy_terms_as_patch_route_requiring_source_provenance",
      "closure_strength": "patch_route_source_derived_only_after_certificate",
      "current_status": "open_patch_control",
      "forbidden_claim": "GU_derives_or_cancels_Lambda_or_dark_energy_without_branch_fixed_source_generation_and_anti_fitting_tests"
    },
    {
      "id": "phenomenological_control",
      "allowed_use": "target_windows_parameter_scans_and_effective_mechanism_tests",
      "closure_strength": "control_only",
      "current_status": "active_for_theta_xi",
      "forbidden_claim": "source_derived_coefficient_without_S_GU"
    }
  ],
  "forbidden_shortcuts": [
    "source_geometry_by_name_only",
    "metric_quantization_as_primary_start",
    "left_geometric_right_imported",
    "stress_energy_named_not_derived",
    "branch_mismatch",
    "compatibility_as_recovery",
    "host_as_selector",
    "weak_field_as_exact_GR",
    "hidden_matter_relabeling",
    "qft_recovery_by_slogan",
    "representation_labels_as_state",
    "ansatz_state_as_measurement",
    "compact_control_as_physical_index",
    "phenomenological_term_without_source",
    "bare_Lambda_as_marble",
    "dark_energy_fit_as_derivation",
    "free_beta_nonzero_theta",
    "ordinary_anomaly_as_selector",
    "governance_as_physics_proof"
  ],
  "rollback_conditions": [
    "S_GU_or_D_GU_only_slot_for_cited_branch",
    "primary_D_GU_lacks_Phi_d",
    "free_beta_only_theta_norm",
    "Schwarzschild_or_Kerr_full_EL_failure",
    "T_shadow_hidden_matter_or_target_fitted",
    "no_positive_QFT_state_space_state_or_observables",
    "matter_selector_consumes_target_data",
    "extra_observer_modes_anomalous",
    "measurement_violation_only_ansatz_or_no_violation_for_admissible_settings",
    "compact_bridge_loses_operator_symbol_H_linearity_or_Fredholm_data",
    "theta_xi_inserted_or_depends_on_unspecified_S_IG_dyn",
    "bare_Lambda_or_fitted_dark_energy_used_as_source_derivation",
    "branch_changes_between_GR_and_QFT_legs"
  ],
  "first_missing_proof_packet": {
    "id": "SameSourceReductionPacket_V0",
    "requires": [
      "source_branch_id",
      "G_src",
      "D_GU",
      "S_GU",
      "variation_space",
      "physical_field_complex",
      "section_map",
      "observer_access",
      "boundary_domain_vacuum_data",
      "provenance_rules"
    ],
    "must_emit": [
      "source_EL_tuple",
      "marble_reduction",
      "lambda_patch_status",
      "wood_QFT_reduction",
      "matter_gauge_finite_selector_status",
      "stress_energy_bridge",
      "conservation_theorem",
      "known_physics_gate_results",
      "provenance_and_rollback_ledger"
    ],
    "allowed_result": ["closed", "conditional", "blocked", "fail", "import", "host", "control_only"]
  },
  "next_step": "build_SameSourceReductionPacket_V0_for_one_fixed_branch_starting_with_Branch_2A_if_Phi_is_derived_else_Branch_3_total_current"
}
```

## 9. Next Meaningful Proof/Computation Step

Build one branch-fixed packet rather than another global synthesis:

```text
SameSourceReductionPacket_V0(branch)
```

Recommended sequence:

1. Try Branch 2A only if a natural, A-independent, gauge-covariant
   `Phi(epsilon,beta,s)=0` can be derived from source geometry, with `D_A Phi = 0`.
   Otherwise switch immediately to Branch 3 and use total-current language:

   ```text
   D_A^* F_A = theta_eff.
   ```

2. Lock the source object:

   ```text
   D_GU, S_GU, variation_space, source_law, boundary/domain/vacuum data.
   ```

3. Compute the marble leg first far enough to expose the stress-energy slot:

   ```text
   E_src -> Pi_4D(E_src)
   g = s^* g_Y
   G[g] + Lambda_eff g - kappa_eff T_shadow - R_shadow = 0.
   ```

4. Compute the wood leg from the same branch:

   ```text
   physical field complex
   -> positive QFT state space or local algebra
   -> source-derived omega/rho
   -> admissible observables and probabilities
   -> matter/gauge/Higgs/anomaly/generation status.
   ```

5. Define `T_shadow` only after the wood leg exists, or label it as ordinary QFT import.

6. Run the first binary checks:

   ```text
   Does exact Schwarzschild solve the full vacuum EL tuple?
   Does the same branch produce a positive QFT state/state space?
   Does T_shadow have source provenance?
   Does the matter selector avoid A_F, G_SM, Z_6, K_SM, physical Higgs, and n=3 as inputs?
   ```

7. Only after those checks pass should the branch run Kerr, FLRW/theta-xi, anomaly,
   generation-count, and CHSH physical-forcing gates.

If the packet cannot avoid importing ordinary matter/QFT, the correct artifact is still
valuable:

```text
route = metric-shadow-first + ordinary_qft_import
same_source_closed = false
```

That result would sharpen the repo's public posture without pretending the marble/wood
complaint has been solved.

## Sources Read

- `process/runbooks/five-lane-frontier-run.md`
- `explorations/primary-gu-interface-contract-2026-06-24.md`
- `explorations/source-geometry-not-quantized-gravity-contract-2026-06-24.md`
- `explorations/gr-shadow-recovery-certificate-2026-06-24.md`
- `explorations/qft-shadow-extraction-certificate-2026-06-24.md`
- `explorations/matter-gauge-source-geometry-selector-gate-2026-06-24.md`
- `explorations/finite-control-provenance-audit-2026-06-24.md`
- `explorations/live-claim-dag-fault-finality-ledger-2026-06-24.md`
