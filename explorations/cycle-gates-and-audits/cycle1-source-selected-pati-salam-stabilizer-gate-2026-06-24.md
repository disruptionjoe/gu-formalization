---
title: "Cycle 1 Source-Selected Pati-Salam Stabilizer Gate"
date: "2026-06-24"
status: "exploration/gate"
doc_type: "cycle1_source_selected_pati_salam_stabilizer_gate"
verdict: "UNDERDEFINED_SOURCE_SELECTION_WITH_CONDITIONAL_STABILIZER_KERNEL_THEOREM"
owned_path: "explorations/cycle-gates-and-audits/cycle1-source-selected-pati-salam-stabilizer-gate-2026-06-24.md"
optional_audit:
  - "tests/cycle1_source_selected_pati_salam_stabilizer_audit.py"
depends_on:
  - "RESEARCH-POSTURE.md"
  - "process/runbooks/five-lane-frontier-run.md"
  - "explorations/geometry-curvature-emergence/mission-a-matter-gauge-selector-construction-2026-06-24.md"
  - "explorations/geometry-curvature-emergence/matter-gauge-source-geometry-selector-gate-2026-06-24.md"
  - "explorations/type-ii1-spectral/sm-gauge-higgs-finite-control-extraction-ledger-2026-06-24.md"
  - "explorations/type-ii1-spectral/type-ii1-selector-or-nogo-theorem-2026-06-24.md"
  - "explorations/type-ii1-spectral/type-ii1-selector-candidate-2026-06-24.md"
---

# Cycle 1 Source-Selected Pati-Salam Stabilizer Gate

## 1. Verdict

**Verdict: underdefined as a source selector; conditionally theorem-shaped as a
rank-one stabilizer/kernel computation.**

The repo can state a precise conditional theorem:

```text
If branch-fixed GU source data select a nonzero decomposable rank-one vector
v_PSB in V_PSB = (10bar,1,3), then the identity-component stabilizer inside
G_PS = SU(4) x SU(2)_L x SU(2)_R has Lie algebra
su(3) + su(2)_L + u(1), and its action on the standard Pati-Salam spinor packet
plus the bidoublet scalar slot has the usual mu_6 central kernel.
```

The repo cannot yet instantiate the stronger source-selected claim:

```text
fixed source branch I_GU^b, S_GU, D_GU, variation space, boundary/domain data
  -> source-selected v_PSB in the rank-one orbit of V_PSB.
```

That missing source-selection theorem is first in the dependency order. Without
it, the stabilizer calculation is a high-value conditional computation, not a
derivation of observer gauge physics from source geometry.

Current decision:

```text
V_PSB representation slot: hosted.
rank-one v_PSB object: not selected by current repo data.
stabilizer/kernel computation: conditional theorem gate.
SM gauge quotient: conditional output only if v_PSB is source-selected and the
  complete observer shadow does not change the kernel.
SM matter/Higgs/three-generation claims: not derived.
```

The target-fed route is rejected:

```text
choose v_PSB because its stabilizer is SM-like
  -> no-go as a selector.
```

## 2. Source Data And Forbidden Target Inputs

### Legal source data

The gate may consume only branch-fixed source data:

| datum | permitted role |
|---|---|
| `I_GU^b` | one fixed GU branch before output inspection |
| `X`, `Y = Met_Lor(X)`, section `s: X -> Y` | observer-access structure |
| `P -> Y`, source group `Sp(64)` | source automorphism and carrier data |
| `S = H^64`, `Cl(9,5) ~= M_64(H)` | typed source carrier |
| `Spin(6,4)` maximal compact branch | representation branching frame |
| `D_GU`, source physical complex, source Hessian | low-mode and stability data if written |
| `S_GU`, variation space, source law | criticality and vacuum selection |
| `theta`, `II_s^H`, connection, curvature | possible source fields producing scalar tensors |
| boundary/domain data | admissible source critical problem |
| source real/quaternionic/grading/chirality structures | compatibility and shadow bookkeeping |

### Forbidden target inputs

The selection rule is void if any of these appear upstream of the source
selection:

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
```

The theorem may output a stabilizer, a kernel, charges, or scalar slots after
source data have selected the object. It may not consume those outputs as
selection criteria.

## 3. Candidate `v_PSB` Selection Rule

Let the source branch expose the Pati-Salam representation arena:

```text
G_PS = SU(4) x SU(2)_L x SU(2)_R
V_PSB = (10bar,1,3)
      ~= Sym^2(A^*) tensor Sym^2(C)
```

where `A = C^4` is the `SU(4)` defining representation and `C = C^2_R` is the
`SU(2)_R` defining representation.

A target-free selection rule would have to be a certificate of the form:

```text
SourceRankOnePSBSelection(I_GU^b, c, s)
  =
  (
    pi_PSB,
    scalar_source_packet,
    source_critical_equations,
    selected_orbit,
    v_PSB,
    naturality_certificate,
    replacement_audit,
    rollback
  )
```

with:

```text
pi_PSB:
  source scalar/vacuum tensor space -> V_PSB

v_PSB:
  pi_PSB(source critical data)

required orbit:
  v_PSB = ell^2 tensor r^2
  with ell in A^*, r in C,
  v_PSB nonzero, decomposable, and rank one.
```

The selection rule is legal only if the source action, Hessian, boundary data,
or source field equations force that orbit before the observer gauge group is
named. It is not enough to say that a rank-one vector exists in `V_PSB`.

Required pass conditions:

| check | pass condition |
|---|---|
| `NoTargetInput` | no forbidden target datum appears in the selector input DAG |
| `BranchFixed` | `I_GU^b`, variations, source law, and domains are fixed first |
| `ProjectionDefined` | `pi_PSB` is a source-defined projection or functor, not a hand split |
| `Nonzero` | source equations rule out the zero projection |
| `RankOneOrbit` | source equations force the decomposable rank-one orbit |
| `Naturality` | source isomorphisms carry selected vectors to selected vectors |
| `Replacement` | generic, zero, higher-rank, and target-chosen alternatives fail for source reasons |

Current repo status:

```text
The type V_PSB can be named from the branch decomposition.
The source selection map pi_PSB and the source-critical proof selecting the
rank-one orbit are not supplied.
```

So `v_PSB` is a specified missing object, not a current selected object.

## 4. Stabilizer/Kernel Theorem Statement

### Conditional theorem

Let:

```text
A = C^4
B = C^2_L
C = C^2_R
G = SU(A) x SU(B) x SU(C)
V_PSB = Sym^2(A^*) tensor Sym^2(C)
W = (A tensor B) plus (A^* tensor C)
V_H = B tensor C
```

Choose anonymous bases and the rank-one tensor:

```text
v = (a_4^*)^2 tensor (c_+)^2.
```

Then the identity component of the exact-vector stabilizer:

```text
H = Stab_G(v)
```

is:

```text
H^0 =
  {
    (diag(h,z), l, diag(z,z^-1)):
      h in U(3), z in U(1), det(h) z = 1, l in SU(B)
  }
```

up to the usual harmless choice of cube-root parameterization for the `U(3)`
block. Hence:

```text
Lie(H^0) ~= su(3) + su(2)_L + u(1).
```

The `u(1)` is not inserted as hypercharge. It is the character relation forced
by the exact-vector condition:

```text
(a_4^*)^2 contributes z^-2,
(c_+)^2 contributes z^2,
so the product fixes v.
```

### Weight ledger on the observer packet

Parameterize the stabilizer `u(1)` by the phase `z`. On the cover
`SU(3) x SU(2)_L x U(1)_q`, the anonymous weights `q` on `W` are:

| summand in `W` | stabilizer representation | `q` |
|---|---:|---:|
| `A_3 tensor B` | `(3,2)` | `-1/3` |
| `A_1 tensor B` | `(1,2)` | `+1` |
| `A_3^* tensor c_+` | `(3bar,1)` | `+4/3` |
| `A_3^* tensor c_-` | `(3bar,1)` | `-2/3` |
| `A_1^* tensor c_+` | `(1,1)` | `0` |
| `A_1^* tensor c_-` | `(1,1)` | `-2` |

For the bidoublet scalar slot `V_H = B tensor C`:

| summand in `V_H` | stabilizer representation | `q` |
|---|---:|---:|
| `B tensor c_+` | `(1,2)` | `+1` |
| `B tensor c_-` | `(1,2)` | `-1` |

After the anonymous computation is complete, the comparison convention
`Y = -q/2` recovers the familiar Pati-Salam charge packet. This comparison is
not an input to the theorem.

### Kernel statement

Use the integer charge normalization:

```text
Q = -3 q = 6Y.
```

In the presentation `SU(3) x SU(2)_L x U(1)_Q`, the kernel of the action on
`W plus V_H` is:

```text
mu_6 = < (omega_3 I_3, -I_2, exp(i*pi/3)) >
```

where `omega_3 = exp(2*pi*i/3)`.

Equivalently, the conditional observer image on this packet is:

```text
(SU(3) x SU(2)_L x U(1)_Q) / mu_6.
```

This is not yet a final physical gauge theorem. The complete low observer
shadow must be known before the global kernel can be promoted, because extra
surviving modes can reduce the kernel or break the candidate branch.

### Proof sketch

The stabilizer of the covector line `C a_4^*` in `SU(A)` is
`S(U(3) x U(1))`. The stabilizer of the line `C c_+` in `SU(C)` is `U(1)`.
Since `v` is a tensor square in each factor and the theorem fixes the vector,
not merely its line, the source phases must satisfy:

```text
z_A^-2 z_C^2 = 1.
```

On the identity component this gives `z_C = z_A`, leaving exactly one `u(1)`
beside `SU(3)` and `SU(2)_L`. The weight table follows by applying that phase
to `A`, `A^*`, and `C`. The kernel calculation is then the common central
solution:

```text
a b u = 1,
b u^-3 = 1,
a^-1 u^2 = 1,
u^6 = 1,
```

where `a^3 = 1`, `b^2 = 1`, and `u in U(1)_Q`. Thus `u^6 = 1`, giving the
cyclic order-six kernel above.

## 5. Higgs/Matter/Generation Implications And Non-Implications

Status words used in this gate:

| status | meaning |
|---|---|
| `hosted` | the source representation contains a slot, with no source rule choosing it |
| `selected` | a legal source rule chooses an object or orbit from branch-fixed data |
| `derived` | a theorem computes a consequence from selected legal source data |
| `conditional_derived` | derived if a named missing source object is supplied |
| `open` | exact proof object is named but absent |
| `no_go_target_fed` | the route succeeds only by consuming target data |

Current separation:

| item | current status | implication | non-implication |
|---|---|---|---|
| `V_PSB = (10bar,1,3)` slot | `hosted` | legal Pati-Salam-breaking candidate slot exists in the branch arena | no selected vacuum |
| `v_PSB` rank-one tensor | `open_not_selected` | exact missing object is named | no current source selection |
| stabilizer Lie algebra | `conditional_derived` | follows from the rank-one tensor | does not prove the source chooses that tensor |
| kernel on `W plus V_H` | `conditional_derived_packet_kernel` | `mu_6` is computed for the packet | not final until complete low shadow is listed |
| one Pati-Salam spinor packet `W` | `derived_branch_representation` | supports one anonymous generation-shaped packet | full observer matter shadow is not derived |
| Higgs bidoublet slot `V_H` | `hosted` | scalar quantum-number host exists after the stabilizer | physical Higgs mode and potential are not derived |
| exact generation count | `open` | no positive count theorem here | three generations are not established |
| anomaly compatibility | `open_downstream` | can be checked after complete shadow | ordinary anomaly cancellation is not a selector |

The gate therefore permits this claim:

```text
The rank-one Pati-Salam stabilizer route is a conditional source-selector
theorem target with a concrete stabilizer/kernel computation.
```

It forbids these promotions:

```text
full observer matter derived;
physical Higgs emergence derived;
three generations established;
target Pati-Salam breaking accepted as source selection.
```

## 6. First Exact Obstruction Or Missing Proof Object

The first exact missing proof object is:

```text
SourceCriticalRankOnePSBSelectionCertificate
```

It must contain:

```text
1. A fixed source branch I_GU^b with written S_GU, D_GU, variation space,
   source law, source scalar sector, and boundary/domain data.

2. A source-defined projection or extraction map:
   pi_PSB: scalar_source_packet -> V_PSB.

3. A source-critical equation, Hessian eigenproblem, minimization theorem,
   boundary condition, or natural invariant that selects a nonzero tensor.

4. A proof that the selected tensor lies in the decomposable rank-one orbit:
   v_PSB = ell^2 tensor r^2.

5. A proof that the selector is natural under source isomorphisms and does not
   inspect the observer target.

6. A replacement audit showing why zero, generic, higher-rank, alternate
   Pati-Salam-breaking, and target-chosen vectors fail for source reasons.
```

Why this obstruction is first:

```text
The stabilizer/kernel computation can be done once v_PSB is supplied.
The repo does not yet supply v_PSB from source dynamics.
Therefore the first missing theorem is source selection, not Lie algebra
branching.
```

Rollback conditions:

| trigger | rollback |
|---|---|
| `v_PSB` chosen because its stabilizer matches the SM target | `no_go_target_fed` |
| `pi_PSB` undefined or hand-projected | demote to `hosted` |
| source projection is zero | rank-one route fails |
| source projection is generic or higher rank | stabilizer route fails or changes output |
| kernel named as `Z_6` before the action is computed | demote to imported kernel |
| complete low shadow has extra incompatible modes | demote gauge quotient to packet-only computation |
| Higgs projection or potential is inserted phenomenologically | keep Higgs at `hosted/open` |
| generation count enters as `n_equals_3` or target index value | keep generation count `open` |

## 7. Constructive Next Computation

The next computation should separate two tasks that are currently entangled.

First, formalize the conditional representation result as a small ledger:

```text
RankOnePSBStabilizerKernelLedger

input:
  A = C^4, B = C^2, C = C^2
  v = (a_4^*)^2 tensor (c_+)^2
  W = (A tensor B) plus (A^* tensor C)
  V_H = B tensor C

output:
  H^0
  q weights on W and V_H
  integer Q weights
  central kernel on W plus V_H
```

This computation is target-free if the symbols remain anonymous until after the
kernel is computed.

Second, run the real source-selection search:

```text
Find or refute pi_PSB(source critical data) in the written GU branch.
```

Minimum source-side work packet:

1. Choose the branch-fixed scalar source packet: `theta`, `II_s^H`, source
   Hessian eigenspace, connection curvature component, or another explicit
   source tensor space.
2. Define `pi_PSB` without using SM labels.
3. Compute whether source criticality selects zero, generic rank, rank one, or
   an alternate orbit.
4. If rank one appears, feed that output into the stabilizer/kernel ledger.
5. If rank one does not appear, record the first source obstruction and kill or
   demote the route.

Decision outcomes:

| computation result | consequence |
|---|---|
| no source-defined `pi_PSB` | route remains hosted/underdefined |
| `pi_PSB = 0` | rank-one PSB route fails |
| generic or higher-rank orbit | stabilizer likely not SM-like; compute or fail |
| rank-one orbit selected but extra low modes alter kernel | packet theorem only |
| rank-one orbit selected and complete shadow preserves kernel | promote gauge branch, not Higgs or generations |

## 8. Machine-Readable JSON Summary

```json
{
  "artifact": "CYCLE1_SOURCE_SELECTED_PATI_SALAM_STABILIZER_GATE",
  "version": "2026-06-24",
  "verdict": "UNDERDEFINED_SOURCE_SELECTION_WITH_CONDITIONAL_STABILIZER_KERNEL_THEOREM",
  "verdict_class": "underdefined",
  "can_define_target_free_v_PSB_now": false,
  "can_state_conditional_v_PSB_type": true,
  "can_compute_stabilizer_kernel_conditionally": true,
  "overclaim_guards": {
    "sm_matter_derived": false,
    "physical_higgs_derived": false,
    "three_generations_derived": false,
    "target_fed_v_PSB_allowed": false
  },
  "legal_source_data": [
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
    "S_GU",
    "variation_space",
    "source_law",
    "theta",
    "II_s_H",
    "connection_curvature",
    "boundary_domain_data",
    "source_Hessian",
    "source_real_quaternionic_grading_structures"
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
    "chosen_SM_kernel"
  ],
  "status_vocabulary": {
    "hosted": "source representation contains a slot but no legal source rule chooses it",
    "selected": "branch-fixed source data choose an object or orbit without target inputs",
    "derived": "theorem output from selected legal source data",
    "conditional_derived": "theorem output if a named missing source object is supplied",
    "open": "named proof object absent",
    "no_go_target_fed": "success consumes target data"
  },
  "v_PSB_selection_rule": {
    "candidate_type": "SourceRankOnePSBSelection",
    "source_slot": "V_PSB=(10bar,1,3)=Sym^2(A^*) tensor Sym^2(C)",
    "required_output": "nonzero_decomposable_rank_one_v_PSB",
    "rank_one_form": "ell^2_tensor_r^2",
    "current_status": "open_not_selected",
    "first_missing_object": "SourceCriticalRankOnePSBSelectionCertificate",
    "required_checks": [
      "NoTargetInput",
      "BranchFixed",
      "ProjectionDefined",
      "Nonzero",
      "RankOneOrbit",
      "Naturality",
      "Replacement"
    ]
  },
  "conditional_stabilizer_kernel_theorem": {
    "name": "RankOnePSBStabilizerKernelLemma",
    "input_group": "SU(4) x SU(2)_L x SU(2)_R",
    "input_vector": "v=(a_4^*)^2 tensor (c_+)^2",
    "stabilizer_identity_component": "S(U(3) x U(1))_phase_locked_with_U(1)_R x SU(2)_L",
    "stabilizer_lie_algebra": "su3_plus_su2_L_plus_u1",
    "matter_packet": "W=(A tensor B) plus (A^* tensor C)",
    "higgs_slot": "V_H=B tensor C",
    "u1_weight_convention": "q_from_stabilizer_phase_and_Q=-3q=6Y_after_comparison",
    "kernel_on_W_plus_V_H": "mu_6",
    "kernel_generator": "(omega_3_I3,minus_I2,exp_i_pi_over_3)",
    "kernel_promotion_condition": "complete_low_observer_shadow_preserves_kernel"
  },
  "status_separation": [
    {
      "item": "V_PSB_slot",
      "status": "hosted",
      "claim": "branch representation contains the candidate PSB slot",
      "non_claim": "source-selected vacuum"
    },
    {
      "item": "v_PSB_rank_one_tensor",
      "status": "open_not_selected",
      "claim": "specified missing source object",
      "non_claim": "currently selected object"
    },
    {
      "item": "stabilizer_lie_algebra",
      "status": "conditional_derived",
      "claim": "computed from rank-one v_PSB",
      "non_claim": "source choice of v_PSB"
    },
    {
      "item": "kernel_on_W_plus_V_H",
      "status": "conditional_derived_packet_kernel",
      "claim": "mu_6 computed on named packet",
      "non_claim": "final kernel before complete shadow"
    },
    {
      "item": "matter_shadow",
      "status": "derived_branch_representation_not_full_shadow",
      "claim": "one Pati-Salam packet is available as branch representation",
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
  "rollback_conditions": [
    "v_PSB_chosen_because_stabilizer_matches_target",
    "pi_PSB_undefined_or_hand_projected",
    "source_projection_zero",
    "source_projection_generic_or_higher_rank",
    "kernel_named_before_action_computation",
    "complete_low_shadow_changes_kernel",
    "extra_low_modes_have_uncancelled_anomaly",
    "physical_Higgs_or_EWSB_inserted_phenomenologically",
    "generation_count_uses_n_equals_3_or_target_index",
    "A_F_G_SM_Z_6_K_SM_consumed_upstream"
  ],
  "first_exact_obstruction": "SourceCriticalRankOnePSBSelectionCertificate",
  "constructive_next_computation": "RankOnePSBStabilizerKernelLedger_then_pi_PSB_source_selection_search",
  "allowed_citation": "The rank-one Pati-Salam stabilizer route has a conditional stabilizer/kernel theorem target; the repo has not source-selected v_PSB or derived full matter, physical Higgs, or three generations."
}
```

## Sources Read

- `RESEARCH-POSTURE.md`
- `process/runbooks/five-lane-frontier-run.md`
- `explorations/geometry-curvature-emergence/mission-a-matter-gauge-selector-construction-2026-06-24.md`
- `explorations/geometry-curvature-emergence/matter-gauge-source-geometry-selector-gate-2026-06-24.md`
- `explorations/type-ii1-spectral/sm-gauge-higgs-finite-control-extraction-ledger-2026-06-24.md`
- `explorations/type-ii1-spectral/type-ii1-selector-or-nogo-theorem-2026-06-24.md`
- `explorations/type-ii1-spectral/type-ii1-selector-candidate-2026-06-24.md`
