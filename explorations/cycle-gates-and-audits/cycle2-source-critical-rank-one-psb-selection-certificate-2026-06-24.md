---
title: "Cycle 2 Source-Critical Rank-One PSB Selection Certificate"
date: "2026-06-24"
status: "exploration/certificate"
doc_type: "cycle2_source_critical_rank_one_psb_selection_certificate"
verdict: "SELECTION_PROBLEM_SPECIFIED_SOURCE_SELECTION_NOT_CLOSED"
owned_path: "explorations/cycle-gates-and-audits/cycle2-source-critical-rank-one-psb-selection-certificate-2026-06-24.md"
optional_audit:
  - "tests/cycle2_source_critical_rank_one_psb_selection_audit.py"
depends_on:
  - "RESEARCH-POSTURE.md"
  - "process/runbooks/five-lane-frontier-run.md"
  - "explorations/cycle-gates-and-audits/cycle1-source-selected-pati-salam-stabilizer-gate-2026-06-24.md"
  - "explorations/geometry-curvature-emergence/mission-a-matter-gauge-selector-construction-2026-06-24.md"
  - "explorations/geometry-curvature-emergence/matter-gauge-source-geometry-selector-gate-2026-06-24.md"
  - "explorations/type-ii1-spectral/sm-gauge-higgs-finite-control-extraction-ledger-2026-06-24.md"
  - "explorations/type-ii1-spectral/type-ii1-selector-anti-smuggling-theorem-2026-06-24.md"
---

# Cycle 2 Source-Critical Rank-One PSB Selection Certificate

## 1. Verdict

**Verdict: the source-critical rank-one PSB selection problem can now be
specified precisely, but current repo sources do not select `v_PSB`.**

Cycle 1 named the first missing object:

```text
SourceCriticalRankOnePSBSelectionCertificate
```

Cycle 2 can make that object decision-grade. A valid certificate would prove:

```text
branch-fixed source critical data
  -> source-defined scalar packet
  -> source-defined projection pi_PSB
  -> nonzero exact rank-one vector v_PSB in V_PSB
  -> conditional Pati-Salam stabilizer/kernel computation.
```

Current sources do not supply the middle arrow. They identify the representation
slot and the conditional stabilizer theorem, but they do not provide a
source-natural functional, invariant, Hessian problem, boundary condition, or
Euler-Lagrange subproblem whose stable critical locus forces the nonzero
rank-one orbit.

Current decision:

```text
V_PSB = (10bar,1,3): hosted as a branch representation slot.
rank-one algebraic orbit: specified as a certificate test.
v_PSB: not selected by current source data.
stabilizer/kernel: conditional derived output if the certificate closes.
SM matter/Higgs/three-generation claims: remain not derived.
```

The exact missing source object is:

```text
kappa_R1_PSB
```

where this denotes a source-natural functional or invariant, built from the
written GU branch data, whose criticality/stability equations select a nonzero
exact rank-one `V_PSB` vector and obstruct zero, generic, higher-rank,
line-only, and target-chosen replacements. A variational representative
`F_R1_PSB_src` would be an acceptable implementation if its Euler-Lagrange or
Hessian equations define this invariant.

So the answer to the assignment's decision question is:

```text
Current sources can specify SourceCriticalRankOnePSBSelectionCertificate.
Current sources cannot close it.
The first obstruction is the missing source rank/orbit invariant
kappa_R1_PSB, together with its pi_PSB extraction map.
```

## 2. Candidate Source-Critical Selection Criterion

Let the branch representation arena be:

```text
G_PS = SU(A) x SU(B) x SU(R)
A = C^4
B = C^2_L
R = C^2_R

V_PSB = (10bar,1,3)
      = Sym^2(A^*) tensor Sym^2(R).
```

The desired rank-one cone is the nonzero Veronese product cone:

```text
O_R1_PSB =
  { ell^2 tensor r^2 :
      ell in A^* \ {0},
      r in R \ {0} }.
```

This is an internal representation-theoretic test. It is not, by itself, a
source selector. A source-critical selector must explain why source dynamics
lands in this cone.

A closing certificate has the form:

```text
SourceCriticalRankOnePSBSelectionCertificate(I_GU^b, c, s)
  =
  (
    source_branch_record,
    source_scalar_packet E_src,
    projection pi_PSB: E_src -> V_PSB,
    source_functional_or_invariant F_R1_PSB_src / kappa_R1_PSB,
    criticality_and_stability_equations,
    selected_v_PSB,
    rank_one_orbit_audit,
    exact_vector_or_phase_lock_audit,
    naturality_certificate,
    replacement_audit,
    rollback_conditions
  ).
```

It closes only if all of the following pass.

| check | required source-critical content |
|---|---|
| `BranchFixed` | `I_GU^b`, source law, variation space, domains, boundary data, observer section, and source scalar packet are fixed before any observer target is inspected. |
| `ProjectionDefined` | `pi_PSB` is a source-defined extraction from `E_src` to the `V_PSB` isotypic slot. If `V_PSB` has multiplicity, the multiplicity splitting is source-defined. |
| `SourceFunctionalDefined` | `F_R1_PSB_src` or `kappa_R1_PSB` is written from allowed source data, not from the desired stabilizer. |
| `CriticalSelection` | the selected configuration is a stable critical point, constrained minimum, Hessian eigenspace, boundary-selected mode, or natural invariant value of the source problem. |
| `Nonzero` | source equations rule out `pi_PSB = 0`. Nonzero cannot be inserted as a target convenience. |
| `ExactVectorNotLine` | the source data select an exact nonzero vector/orbit with the phase relation needed for the vector stabilizer, or else provide a source normalization/phase-lock. A projective line alone is insufficient. |
| `RankOneOrbit` | the selected vector lies in `O_R1_PSB`, not merely somewhere in `V_PSB`. |
| `OrbitRigidity` | all source-admissible selected solutions lie in one `G_PS` orbit, or the certificate reports a set of alternatives rather than a selected `v_PSB`. |
| `Naturality` | source isomorphisms carry selected source data to selected source data and carry `v_PSB` to the corresponding selected vector. |
| `ReplacementObstruction` | zero, generic, higher-rank, line-only, alternate-slot, and target-chosen replacements fail for named source reasons. |

The algebraic rank-one audit may use the following target-free tests inside the
representation slot.

```text
1. Tensor decomposability:
   v in Sym^2(A^*) tensor Sym^2(R) has tensor-flattening rank one.

2. A-factor rank one:
   if v = alpha tensor beta, then alpha in Sym^2(A^*) has symmetric matrix rank one.

3. R-factor rank one:
   if v = alpha tensor beta, then beta in Sym^2(R) has symmetric matrix rank one.

4. Nonzero:
   alpha != 0 and beta != 0.
```

Equivalently, the relevant 2 by 2 minors vanish and the vector is nonzero. But
these equations are only a certificate audit. They do not replace the missing
source functional/invariant that explains why the equations hold.

## 3. Allowed Source Inputs And Forbidden Target Inputs

### Allowed source inputs

The certificate may consume only branch-fixed source data.

| input | allowed role |
|---|---|
| `I_GU^b` | fixed GU branch identifier and branch record |
| `X`, `Y = Met_Lor(X)`, `s: X -> Y` | observer-access structure and pullback data |
| `P -> Y`, source group `Sp(64)` | source automorphism and carrier data |
| `S = H^64`, `Cl(9,5) ~= M_64(H)` | source carrier and Clifford typing |
| `Spin(6,4)` maximal compact branch | representation branching frame |
| `D_GU`, physical source complex, source Hessian | source spectral, low-mode, and stability data if written |
| `S_GU`, variation space, source law | source criticality and vacuum selection |
| `theta`, `II_s^H`, connection, curvature | admissible source fields that might feed `E_src` |
| boundary/domain data | admissible source critical problem |
| source real/quaternionic/grading/chirality structures | compatibility, reality, and shadow bookkeeping |
| source automorphism category | naturality and replacement tests |
| source scalar packet `E_src` | domain of the extraction map `pi_PSB` |

The representation slot `V_PSB` may be named after the branch decomposition is
fixed. The certificate may not choose the slot because its payoff is known.

### Forbidden target inputs

The selector is void if any of these appear upstream of source selection:

```text
A_F
G_SM
Z_6
K_SM
physical_Higgs
nonzero_Higgs_projection
negative_Higgs_mass_squared
n_equals_3
three_generations
ind_H_D_RS_equals_8
ind_H_D_GU_equals_24
ordinary_anomaly_free_SM_shadow
target_hypercharge_table
target_Pati_Salam_breaking_vacuum
preselected_SM_subgroup
chosen_SM_kernel
ordinary_SM_matter_packet
selected_electroweak_subgroup
desired_stabilizer_su3_su2_u1
mu_6_kernel_as_input
```

The stabilizer, hypercharge comparison, kernel, Higgs slot, and matter packet
may be outputs after source selection. They may not be inputs to the selection
rule.

## 4. Anti-Smuggling Tests

These tests are part of the certificate, not commentary after the fact.

| test | pass condition | failure caught |
|---|---|---|
| `NoTargetInput` | the input dependency graph contains none of the forbidden target inputs | direct target import |
| `BranchCommitment` | source branch, action, variations, and domains are recorded before output inspection | after-the-fact branch tuning |
| `ProjectionProvenance` | `pi_PSB` is constructed from source decomposition/multiplicity data | hand projection to the desired slot |
| `LabelErasure` | replacing SM names by anonymous `A`, `B`, `R`, and source labels leaves the proof unchanged | semantic target matching |
| `PayoffBlindness` | the source functional is defined before computing `Stab(v_PSB)` or the kernel | choosing the object because it gives SM-like output |
| `RankConditionNotSelector` | vanishing minors verify the output but are not the only reason the output is chosen | algebraic wish-list selection |
| `NonzeroFromSource` | nonzero projection follows from the source equations or boundary/domain data | inserted vacuum expectation value |
| `ExactVectorNotLine` | source data select a vector/orbit with the phase-lock needed for the vector stabilizer | projective-line selector with too-large stabilizer |
| `OrbitReplacement` | zero, generic, higher-rank, rank-one-in-one-factor-only, and line-only alternatives fail for source reasons | untested neighboring orbits |
| `AlternateSlotReplacement` | nearby scalar slots such as bidoublet or adjoint-branch alternatives are not silently substituted | slot shopping |
| `KernelAfterAction` | the central kernel is computed from the action after selection | `Z_6` or `mu_6` imported upstream |
| `CompleteShadowQuarantine` | packet-kernel results are not promoted to full observer gauge until every low mode is listed | deleting extra modes |
| `HiggsGenerationQuarantine` | Higgs emergence and generation count remain separate downstream certificates | overclaiming physical Higgs or three generations |
| `Naturality` | isomorphic source records give isomorphic selected vectors | label-dependent selection |
| `RollbackActive` | every failed subcheck demotes the claim to hosted/open/imported/failed | prose rescue |

The projective-line failure deserves special emphasis. If source data select
only:

```text
[v_PSB] in P(V_PSB),
```

then the stabilizer is the line stabilizer, not the exact-vector stabilizer used
in the Cycle 1 lemma. The phase-lock condition that leaves only one `u(1)` is
not automatic. A line-only selector therefore does not close the gauge branch.

## 5. Stabilizer/Kernel Consequence If The Certificate Closes

If `SourceCriticalRankOnePSBSelectionCertificate` closes, then the Cycle 1
conditional theorem becomes a source-selected consequence for the branch.

For anonymous vector spaces:

```text
A = C^4
B = C^2_L
R = C^2_R
G_PS = SU(A) x SU(B) x SU(R)
V_PSB = Sym^2(A^*) tensor Sym^2(R)
W = (A tensor B) plus (A^* tensor R)
V_H = B tensor R
```

and selected:

```text
v_PSB = ell^2 tensor r^2 != 0,
```

the exact-vector stabilizer has identity-component Lie algebra:

```text
Lie Stab^0_{G_PS}(v_PSB) ~= su(3) + su(2)_L + u(1).
```

The induced action on the one Pati-Salam spinor packet `W` and the bidoublet
slot `V_H` has the packet-level central kernel:

```text
mu_6
```

with the usual comparison to the SM quotient only after the anonymous action
has been computed.

What this would promote:

| item | status if certificate closes | scope |
|---|---|---|
| `v_PSB` | `selected` | source-selected rank-one PSB vector/orbit |
| stabilizer Lie algebra | `derived_from_selected_v_PSB` | branch-local gauge stabilizer |
| kernel on `W plus V_H` | `derived_packet_kernel` | packet-level action only |
| SM gauge quotient | `conditional_pending_complete_shadow` | promoted only if all low modes preserve the kernel |

What this would not promote:

| item | remains |
|---|---|
| full observer matter shadow | open until every surviving low mode is listed |
| physical Higgs scalar | hosted/open until source projection and potential are computed |
| Higgs potential and EWSB | open |
| exact three-generation count | open |
| finite Connes algebra `A_F` | not derived by this certificate |
| anomaly finality | downstream of complete observer shadow |

Thus a closed certificate would be a serious gauge-selector advance, but it
would not by itself derive SM matter, the physical Higgs, or three generations.

## 6. First Exact Obstruction

The first exact obstruction is not the stabilizer calculation. It is the absent
source selector.

Current sources do not yet provide:

```text
1. A written source scalar packet E_src whose source fields feed V_PSB.
2. A source-defined projection pi_PSB: E_src -> V_PSB.
3. The source-natural rank/orbit invariant kappa_R1_PSB, or a variational
   representative F_R1_PSB_src defining it.
4. Criticality, Hessian, minimization, boundary, or invariant equations forcing
   pi_PSB(c) != 0.
5. A proof that pi_PSB(c) lies in the nonzero exact rank-one cone O_R1_PSB.
6. A phase-lock or exact-vector certificate, not just projective line data.
7. A replacement audit blocking zero, generic, higher-rank, alternate-slot,
   and target-payoff selections.
```

The exact missing source functional/invariant is:

```text
kappa_R1_PSB:
  Crit(I_GU^b) -> source-natural rank/orbit invariant in V_PSB
```

An equivalent variational implementation would be:

```text
F_R1_PSB_src:
  E_src(I_GU^b, s, boundary/domain data) -> R
```

with required theorem:

```text
kappa_R1_PSB = 0
  implies
    pi_PSB(c) in O_R1_PSB,
    pi_PSB(c) != 0,
    pi_PSB(c) is exact-vector selected up to the source gauge orbit,
    replacements fail for source reasons.
```

The algebraic equations for `O_R1_PSB` are already specifiable. They are not
the missing object. The missing object is the source reason that a GU critical
configuration satisfies those equations.

Rollback conditions:

| trigger | rollback |
|---|---|
| forbidden target input appears upstream | demote to import/no-go target-fed |
| `pi_PSB` is undefined or multiplicity is hand-chosen | demote `V_PSB` to hosted |
| `F_R1_PSB_src` or `kappa_R1_PSB` is missing | remain selection-problem only |
| selected projection is zero | rank-one PSB route fails |
| selected projection is generic or higher-rank | compute new stabilizer or fail this route |
| selector outputs only a projective line | stabilizer consequence does not close |
| rank one is justified by SM-like stabilizer payoff | no-go target-fed |
| kernel is named before action computation | demote kernel to imported |
| complete low shadow changes the kernel | packet theorem only |
| Higgs or generation claims are promoted here | rollback to hosted/open |

## 7. Impact For SM Gauge/Higgs/Matter Claims

This certificate sharpens, but does not improve, current physical claim status.

| claim | current impact |
|---|---|
| `SM_GAUGE` | The rank-one PSB route is a precise source-selection target. It is not currently selected. The SM-like stabilizer remains conditional. |
| `MATTER_SHADOW` | One Pati-Salam spinor packet remains branch-derived. The full observer matter shadow is open. |
| `HIGGS` | The bidoublet slot remains hosted. A physical Higgs scalar, nonzero projection, lightness, potential, and EWSB remain open. |
| `GEN_COUNT` | No three-generation selector is supplied. Type II_1 cardinality-only routes remain filtered by replacement tests. |
| `A_F_OR_BYPASS` | This route bypasses finite Connes input if it succeeds, but it does not derive `A_F`. |
| `ANOMALY_FINALITY` | Ordinary anomaly cancellation can only verify a completed shadow. It cannot select `v_PSB`. |

Allowed citation after this Cycle 2 artifact:

```text
The repo now has a precise source-critical criterion for what would count as
selection of rank-one v_PSB. Current sources do not satisfy the criterion.
```

Forbidden citation:

```text
GU currently selects v_PSB, derives the SM gauge quotient, derives the
physical Higgs, derives full SM matter, or derives three generations.
```

## 8. Next Meaningful Computation

The next computation should be source-side and narrow.

Work packet:

1. Fix one branch record `I_GU^b` with `S_GU`, `D_GU`, variation space,
   boundary/domain data, and source scalar candidates.
2. Choose one candidate source scalar packet:

   ```text
   theta,
   II_s^H,
   source Hessian eigenspace,
   connection curvature component,
   boundary-selected scalar mode,
   or another explicitly written source tensor packet.
   ```

3. Decompose that packet under the branch `G_PS` and determine whether
   `V_PSB = (10bar,1,3)` occurs with canonical multiplicity.
4. If it occurs, define `pi_PSB` from source data. If multiplicity is not
   source-split, stop and report hosted/underdefined.
5. Compute the source Euler-Lagrange, Hessian, minimization, or boundary
   equations restricted to this packet.
6. Apply the rank-one audit:

   ```text
   tensor flattening rank = 1,
   A-symmetric factor rank = 1,
   R-symmetric factor rank = 1,
   vector nonzero,
   exact-vector/phase-lock present.
   ```

7. Run replacements:

   ```text
   zero,
   generic full-rank vector,
   higher-rank A factor,
   higher-rank R factor,
   decomposable but not square factors,
   projective line only,
   alternate scalar slot,
   target-chosen rank-one vector.
   ```

8. Only if these pass, feed the selected vector into the existing
   stabilizer/kernel ledger and then audit the complete low observer shadow.

Decision table:

| computation result | consequence |
|---|---|
| no source scalar packet | source-selection problem remains underdefined |
| no canonical `pi_PSB` | `V_PSB` remains hosted |
| `pi_PSB = 0` | rank-one PSB route fails |
| generic or higher-rank orbit | compute its stabilizer or abandon this route |
| projective line only | stabilizer consequence does not close |
| nonzero exact rank-one orbit selected | promote `v_PSB` to selected and run stabilizer/kernel/shadow audits |
| rank-one selected but complete shadow changes kernel | keep packet theorem only |

## 9. Machine-Readable JSON Summary

```json
{
  "artifact": "CYCLE2_SOURCE_CRITICAL_RANK_ONE_PSB_SELECTION_CERTIFICATE",
  "version": "2026-06-24",
  "verdict": "SELECTION_PROBLEM_SPECIFIED_SOURCE_SELECTION_NOT_CLOSED",
  "verdict_class": "blocked",
  "source_selection_possible_from_current_sources": false,
  "selection_problem_specified": true,
  "can_compute_stabilizer_if_certificate_closes": true,
  "first_exact_obstruction": "missing_kappa_R1_PSB_source_rank_orbit_invariant_with_pi_PSB",
  "named_certificate": "SourceCriticalRankOnePSBSelectionCertificate",
  "missing_source_functional_or_invariant": {
    "name": "kappa_R1_PSB",
    "required_type": "source_natural_rank_orbit_invariant_or_variational_representative_F_R1_PSB_src",
    "required_domain": "E_src(I_GU_branch,observer_section,boundary_domain_data)",
    "required_effect": "select_nonzero_exact_rank_one_v_PSB_and_obstruct_replacements",
    "current_status": "missing"
  },
  "candidate_criterion": {
    "source_slot": "V_PSB=(10bar,1,3)=Sym^2(A^*)_tensor_Sym^2(R)",
    "rank_one_orbit": "O_R1_PSB={ell^2_tensor_r^2_nonzero}",
    "certificate_fields": [
      "source_branch_record",
      "source_scalar_packet_E_src",
      "pi_PSB",
      "F_R1_PSB_src_or_kappa_R1_PSB",
      "criticality_and_stability_equations",
      "selected_v_PSB",
      "rank_one_orbit_audit",
      "exact_vector_or_phase_lock_audit",
      "naturality_certificate",
      "replacement_audit",
      "rollback_conditions"
    ],
    "required_pass_conditions": [
      "BranchFixed",
      "ProjectionDefined",
      "SourceFunctionalDefined",
      "CriticalSelection",
      "Nonzero",
      "ExactVectorNotLine",
      "RankOneOrbit",
      "OrbitRigidity",
      "Naturality",
      "ReplacementObstruction"
    ],
    "rank_one_algebraic_tests": [
      "tensor_flattening_rank_one",
      "A_symmetric_factor_rank_one",
      "R_symmetric_factor_rank_one",
      "nonzero_vector"
    ],
    "current_status": "specified_not_instantiated"
  },
  "allowed_source_inputs": [
    "I_GU_branch",
    "X",
    "Y_equals_Met_Lor_X",
    "observer_section_s",
    "P_to_Y",
    "Sp_64_source_group",
    "S_equals_H_64",
    "Cl_9_5_equals_M_64_H",
    "Spin_6_4_branch",
    "D_GU",
    "physical_source_complex",
    "source_Hessian",
    "S_GU",
    "variation_space",
    "source_law",
    "theta",
    "II_s_H",
    "connection_curvature",
    "boundary_domain_data",
    "source_real_quaternionic_grading_chirality_structures",
    "source_automorphism_category",
    "source_scalar_packet_E_src"
  ],
  "forbidden_target_inputs": [
    "A_F",
    "G_SM",
    "Z_6",
    "K_SM",
    "physical_Higgs",
    "nonzero_Higgs_projection",
    "negative_Higgs_mass_squared",
    "n_equals_3",
    "three_generations",
    "ind_H_D_RS_equals_8",
    "ind_H_D_GU_equals_24",
    "ordinary_anomaly_free_SM_shadow",
    "target_hypercharge_table",
    "target_Pati_Salam_breaking_vacuum",
    "preselected_SM_subgroup",
    "chosen_SM_kernel",
    "ordinary_SM_matter_packet",
    "selected_electroweak_subgroup",
    "desired_stabilizer_su3_su2_u1",
    "mu_6_kernel_as_input"
  ],
  "anti_smuggling_tests": [
    "NoTargetInput",
    "BranchCommitment",
    "ProjectionProvenance",
    "LabelErasure",
    "PayoffBlindness",
    "RankConditionNotSelector",
    "NonzeroFromSource",
    "ExactVectorNotLine",
    "OrbitReplacement",
    "AlternateSlotReplacement",
    "KernelAfterAction",
    "CompleteShadowQuarantine",
    "HiggsGenerationQuarantine",
    "Naturality",
    "RollbackActive"
  ],
  "status_vocabulary": {
    "hosted": "source representation contains a slot but no source rule chooses it",
    "selected": "branch-fixed source data choose an object or orbit without target inputs",
    "derived": "theorem output from selected legal source data",
    "conditional_derived": "theorem output if a named missing source object is supplied",
    "specified_not_instantiated": "criterion is precise but current sources do not satisfy it",
    "open": "named proof object absent",
    "blocked": "current source data lack the object needed to evaluate selection"
  },
  "status_separation": [
    {
      "item": "V_PSB_slot",
      "status": "hosted",
      "claim": "branch representation contains the candidate PSB slot",
      "non_claim": "source-selected vacuum"
    },
    {
      "item": "rank_one_algebraic_orbit",
      "status": "specified_not_instantiated",
      "claim": "rank-one tests are available for a future output",
      "non_claim": "source reason for selection"
    },
    {
      "item": "v_PSB_rank_one_tensor",
      "status": "open_not_selected",
      "claim": "exact missing source-selected object is named",
      "non_claim": "currently selected object"
    },
    {
      "item": "source_functional_or_invariant",
      "status": "missing",
      "claim": "first exact obstruction is identified",
      "non_claim": "functional supplied by current repo"
    },
    {
      "item": "stabilizer_lie_algebra",
      "status": "conditional_derived",
      "claim": "computed if nonzero exact rank-one v_PSB is selected",
      "non_claim": "source choice of v_PSB"
    },
    {
      "item": "kernel_on_W_plus_V_H",
      "status": "conditional_derived_packet_kernel",
      "claim": "mu_6 computed after selected vector and action on packet",
      "non_claim": "final global observer kernel"
    },
    {
      "item": "matter_shadow",
      "status": "derived_branch_representation_not_full_shadow",
      "claim": "one Pati-Salam packet is branch-derived",
      "non_claim": "full observer matter derivation"
    },
    {
      "item": "higgs",
      "status": "hosted_open",
      "claim": "bidoublet quantum-number slot is hosted",
      "non_claim": "physical Higgs projection or potential"
    },
    {
      "item": "generation_count",
      "status": "open",
      "claim": "no source count theorem supplied",
      "non_claim": "three-generation derivation"
    }
  ],
  "consequences_if_certificate_closes": {
    "v_PSB": "selected",
    "stabilizer_lie_algebra": "derived_from_selected_v_PSB_as_su3_plus_su2_L_plus_u1",
    "packet_kernel": "mu_6_on_W_plus_V_H",
    "global_kernel": "pending_complete_low_observer_shadow",
    "sm_gauge_claim": "conditional_pending_complete_shadow",
    "matter_higgs_generation_claims": "remain_open_or_hosted_until_downstream_certificates"
  },
  "overclaim_guards": {
    "sm_matter_derived": false,
    "physical_higgs_derived": false,
    "three_generations_derived": false,
    "sm_gauge_quotient_derived_now": false,
    "target_fed_v_PSB_allowed": false
  },
  "rollback_conditions": [
    "forbidden_target_input_appears_upstream",
    "pi_PSB_undefined_or_multiplicity_hand_chosen",
    "source_functional_or_invariant_missing",
    "selected_output_zero",
    "selected_output_generic_or_higher_rank",
    "selected_output_projective_line_only",
    "rank_one_justified_by_SM_like_stabilizer_payoff",
    "source_naturality_fails",
    "replacement_zero_generic_higher_rank_or_alternate_slot_not_blocked",
    "kernel_named_before_action_computation",
    "complete_low_shadow_changes_kernel",
    "SM_matter_Higgs_or_three_generation_claim_promoted_without_downstream_certificates"
  ],
  "next_meaningful_computation": "define_E_src_and_pi_PSB_for_one_branch_then_compute_F_R1_PSB_src_or_kappa_R1_PSB_rank_one_replacement_audit",
  "allowed_citation": "A precise source-critical criterion for rank-one v_PSB selection is specified; current sources do not select v_PSB or derive full SM matter, physical Higgs, or three generations.",
  "sources_read": [
    "RESEARCH-POSTURE.md",
    "process/runbooks/five-lane-frontier-run.md",
    "explorations/cycle-gates-and-audits/cycle1-source-selected-pati-salam-stabilizer-gate-2026-06-24.md",
    "explorations/geometry-curvature-emergence/mission-a-matter-gauge-selector-construction-2026-06-24.md",
    "explorations/geometry-curvature-emergence/matter-gauge-source-geometry-selector-gate-2026-06-24.md",
    "explorations/type-ii1-spectral/sm-gauge-higgs-finite-control-extraction-ledger-2026-06-24.md",
    "explorations/type-ii1-spectral/type-ii1-selector-anti-smuggling-theorem-2026-06-24.md"
  ]
}
```
