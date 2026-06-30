---
title: "Hourly 20260625 0103 Cycle 3 QFT P_fin^b Source Mining Packet"
date: "2026-06-25"
status: exploration/source-mining-packet
doc_type: qft_pfin_b_source_mining_packet
artifact_id: "QFTPFinBSourceMiningPacket_V1"
run: "hourly-20260625-0103"
cycle: 3
lane: 3
verdict: "BLOCKED_SOURCE_FIRST_PACKET_SPECIFIED_NO_PROJECTOR_RECEIPT"
owned_path: "explorations/hourly-20260625-0103-cycle3-qft-pfin-b-source-mining-packet.md"
companion_audit: "tests/hourly_20260625_0103_cycle3_qft_pfin_b_source_mining_packet_audit.py"
depends_on:
  - "RESEARCH-POSTURE.md"
  - "process/runbooks/five-lane-frontier-run.md"
  - "explorations/hourly-20260625-0103-cycle2-qft-pfin-b-source-projector-locator.md"
  - "explorations/hourly-20260625-0103-cycle2-primary-gu-source-receipt-availability-ledger.md"
  - "sources/media-index.md"
  - "sources/media-contributor-tasks-v1.md"
---

# Hourly 20260625 0103 Cycle 3 QFT P_fin^b Source Mining Packet

## 1. Verdict

Verdict: **blocked source-first packet specified; no projector receipt**.

This packet does not claim that

```text
P_fin^b: F_phys^b(O) -> K_b
```

has been found. It specifies the exact source-mining packet required to decide
whether such a map is present in primary GU source material or can be extracted
from repo-local source data without importing the desired finite target.

The strongest current status is:

```text
source-mining packet: specified
acceptable receipt standard: specified
local mode prerequisites: specified
import/rejection controls: specified
matrix-stage sequence: specified
actual P_fin^b receipt: absent
finite seed/QFT/CHSH promotion: forbidden
```

The branch remains blocked before local mode records, `H_raw`, `Q_b`, finite
positivity, covariance, `rho_AB`, or CHSH/Bell claims.

## 2. Direct Source Derivations

`RESEARCH-POSTURE.md` gives the controlling research posture: pursue the GU
reconstruction aggressively, but do not call compatibility a derivation and do
not hide target data inside a reconstruction.

`process/runbooks/five-lane-frontier-run.md` gives the worker standard:
decision-grade artifact, first exact obstruction, constructive next object, and
no overclaiming.

`explorations/hourly-20260625-0103-cycle2-qft-pfin-b-source-projector-locator.md`
establishes the immediate QFT blocker. Current repo sources contain the intended
carrier

```text
K_b = V_L direct_sum V_R,
V_L = (4,2,1),
V_R = (4bar,1,2),
dim_C K_b = 16,
```

but no source projector, no exact extraction rule, and no `gu-derived`
projector provenance. It also fixes the order: `P_fin^b` must precede local
mode records, `H_raw`, `Q_b`, positivity, covariance, `rho_AB`, and CHSH.

`explorations/hourly-20260625-0103-cycle2-primary-gu-source-receipt-availability-ledger.md`
adds the global source-receipt boundary. For QFT, the required receipt is a
primary GU source object for `P_fin^b`, not more Pati-Salam labels, not a
standard QFT vacuum, and not a Bell fixture.

`sources/media-index.md` supplies the allowable primary surfaces and their use
discipline. Oxford 2013, the Portal special, the 2021 draft-release surface,
JRE/Keating/TOE-style public media, and later candidate surfaces are provenance
maps only until timestamped claims or manuscript locators are mined and checked.

`sources/media-contributor-tasks-v1.md` gives the contributor template
discipline: rows need source ids, timestamps or manuscript locators, claim type,
exact topic, strength, repo implication, and caveats. This packet specializes
that discipline to the QFT finite-source projector.

## 3. Strongest Positive Packet

The strongest positive result is a concrete packet for source mining:

```text
QFTPFinBSourceMiningPacket_V1
```

Its target is not "find any finite 16-dimensional QFT seed." Its target is a
receipt for a source-derived finite projection map from local physical GU source
data into the named representation carrier.

### 3.1 Acceptable Source Projector Evidence

Acceptable evidence must be one of the following:

| evidence kind | acceptance requirement | decision if supplied |
|---|---|---|
| primary-source exact formula | a manuscript equation, transcript fragment, or source locator that defines a finite projection/extraction from physical/local GU fields to the finite Pati-Salam LR carrier | advance to one-mode certificate |
| primary-source construction rule | a rule naming the source field complex, equations/constraints, local region, and finite readout into `K_b` | advance if well-defined on physical quotient |
| repo-local derivation from primary receipt | a derivation whose inputs are named GU source operators/sections/constraints and whose output is `P_fin^b` | advance if provenance is `gu-derived` and target-free |
| exact map data with source provenance | matrix/function/table data plus a source locator explaining why the map is selected by GU rather than fitted | advance if local and quotient-compatible |
| explicit negative receipt | a checked source statement or derivation showing no such finite projector is supplied in the mined surface | keep blocker and update availability ledger |

Unacceptable evidence is classified as import/control even when it has the right
dimension or produces a useful downstream computation.

### 3.2 Local Mode Prerequisites

Before one local mode can be admitted, the packet requires:

```text
sector_id
source_surface_id
source_locator
source_text_or_formula_reference
source_claim_type
F_phys^b(O)_definition
physical_quotient_policy
gauge_constraint_ghost_null_policy
source_projector_P_fin_b
projector_domain
projector_codomain
projector_well_defined_on_physical_quotient
projector_locality_statement
projector_gu_derived_provenance
target_import_flag_false
selected_slot
raw_or_physical_representative
local_support_or_local_algebra_inclusion
exact_image_in_K_b
source_operator_section_constraint_reference
effect_type
projection_status
finality_status
loss_status
rejection_or_import_control_status
```

The mode record is invalid if `selected_slot` or `K_b` is present but
`source_projector_P_fin_b` is still absent. In that case the slot is only a
representation label, not an image of a local physical source mode.

### 3.3 Rejection And Import Controls

The packet rejects the following as source evidence for `P_fin^b`:

| rejected input | classification | reason |
|---|---|---|
| ordinary Pati-Salam representation labels | `representation_label_only` | labels name `K_b`; they do not define a map from `F_phys^b(O)` |
| identity Gram or chosen basis Gram | `import_control` | positivity is being inserted before source modes exist |
| Bell state or Tsirelson state | `control_only` | verifies CHSH plumbing, not GU source extraction |
| Pauli CHSH observables | `control_only` | no GU measurement postulate or admissibility rule supplied |
| standard free/Fock/Hadamard vacuum | `external_qft_import` | not a GU-derived finite projector |
| target-fitted covariance or density matrix | `target_smuggling` | backfills source extraction from desired downstream behavior |
| treating `K_b = V_L direct_sum V_R` as `rho_AB` | `category_error` | direct sum carrier is not a bipartite density matrix |
| media paraphrase without timestamp/context | `unverified_source_pointer` | provenance is too weak for formal extraction |
| claim-mining row without emitted rule/map data | `provenance_only` | useful for routing, insufficient for projector admission |

### 3.4 Source-First Sequence Before Matrix Work

The required sequence is:

```text
1. Mine a primary GU source surface or manuscript locator.
2. Extract a timestamped/transcribed or manuscript-located receipt.
3. Classify the receipt as formula, construction rule, derivation cell, exact map data,
   negative receipt, or non-evidence.
4. Define F_phys^b(O) after equations, gauge, constraints, ghosts, and null modes.
5. Define P_fin^b: F_phys^b(O) -> K_b and prove it is well-defined on the physical
   quotient.
6. Prove source provenance: gu-derived:<operator/section/constraint/source-locator>.
7. Emit one local mode certificate with local support and exact image in K_b.
8. Emit all 16 local mode records only after the one-mode certificate passes.
9. Build H_raw only from certified source mode representatives.
10. Define removed representatives and Q_b only after H_raw and quotient policy exist.
11. Test H_phys = Q_b^* H_raw Q_b for PSD/nonzero rank.
12. Only then route to covariance, rho_AB, admissible observables, and CHSH.
```

No `H_raw`, `Q_b`, positivity certificate, covariance, `rho_AB`, or CHSH result
is allowed to serve as evidence for step 5.

## 4. First Exact Obstruction

The first exact obstruction is still:

```text
source_projector_P_fin_b:
  domain: F_phys^b(O)
  codomain: K_b
  required_content: exact formula, construction rule, derivation cell, or exact map data
  required_provenance: gu-derived
  current_status: absent
```

This obstruction is first because the repo can name the 16-dimensional carrier
but cannot yet show that any of its slots are images of local physical GU source
modes.

Everything below is downstream and cannot repair the obstruction:

```text
exactly_16_local_mode_records
raw_representatives
local_support_or_local_algebra_inclusion
H_raw
removed_representatives_R_b
Q_b
H_phys
matrix_positivity
rank_nonzero
covariance
rho_AB
admissible_CHSH_observables
CHSH_value
Bell_violation
```

## 5. Constructive Next Object

The constructive next object is:

```text
PFinBSourceReceiptRow_V1
```

Minimum row schema:

```text
source_surface_id
source_kind
source_locator
timestamp_or_manuscript_locator
transcript_or_formula_excerpt
claim_type
exact_topic
receipt_kind
emitted_projector_or_rule
emitted_domain
emitted_codomain
F_phys_b_O_dependencies
physical_quotient_policy
locality_prerequisites
gu_provenance_reference
target_import_flag
import_control_result
mode_fields_unlocked
matrix_stage_unlocked
promotion_allowed
next_action
```

Allowed `receipt_kind` values:

```text
exact_formula
construction_rule
derivation_cell
exact_map_data
negative_receipt
terminology_only
representation_label_only
process_or_provenance_only
import_control
unverified_pointer
```

Only the first four receipt kinds can unlock the one-mode certificate, and only
if the import controls pass. `negative_receipt` is valuable but keeps the branch
blocked. The remaining kinds route the source surface as non-evidence for
`P_fin^b`.

## 6. GU Impact

The GU QFT finite-source branch remains **open but blocked before source
extraction**.

Allowed current statement:

```text
The repo has a precise source-mining packet for P_fin^b and a known 16-dimensional
target carrier, but no current source receipt supplies the projector or a credible
extraction rule.
```

Forbidden promotions:

```text
P_fin^b_found = false.
one_local_source_mode_certified = false.
sixteen_mode_packet_admitted = false.
positive_finite_one_particle_seed_established = false.
QFT_recovery_promoted = false.
covariance_or_rho_AB_supplied = false.
CHSH_or_Bell_violation_derived_from_GU = false.
```

This packet improves the branch by turning the previous absence result into a
field-ready source-mining contract. A contributor can now mine a specific media
surface or manuscript segment and return a row that is either promotable,
negative, or rejected for a named reason.

## 7. Next Step

Run the source-mining packet against one high-priority source surface first,
preferably a primary surface with transcript or manuscript locators:

```text
GU-MEDIA-2013-OXFORD
GU-POD-2020-PORTAL-SPECIAL
GU-MEDIA-2021-DRAFT-RELEASE
GU-POD-2021-JRE-1628
GU-POD-2025-TOE-JAIMUNGAL-GU-40
GU-POD-2021-KEATING-REVEALED-1
GU-POD-2021-KEATING-REVEALED-2
```

The first lane should output one or more `PFinBSourceReceiptRow_V1` rows. If a
row emits an acceptable projector or extraction rule, the next sequential object
is:

```text
SingleModePFinBImageCertificate_V1
```

If every row is terminology-only, representation-only, or import/control, update
the source availability ledger and keep the branch blocked before the matrix
stage.

## 8. Machine-Readable JSON Summary

```json
{
  "artifact": "QFTPFinBSourceMiningPacket_V1",
  "run": "hourly-20260625-0103",
  "cycle": 3,
  "lane": 3,
  "verdict": "BLOCKED_SOURCE_FIRST_PACKET_SPECIFIED_NO_PROJECTOR_RECEIPT",
  "status": "blocked",
  "packet_specified": true,
  "projector_receipt_found": false,
  "credible_extraction_rule_found": false,
  "positive_finite_seed_promoted": false,
  "qft_recovery_promoted": false,
  "rho_AB_supplied": false,
  "chsh_promoted": false,
  "bell_violation_claimed": false,
  "derived_directly_from_sources": [
    "Mission_A_posture_no_compatibility_as_derivation",
    "five_lane_decision_grade_worker_contract",
    "Cycle2_QFT_locator_absent_projector_representation_labels_only",
    "Cycle2_primary_source_receipt_ledger_QFT_missing_P_fin_b",
    "media_index_source_surfaces_are_provenance_maps_not_proofs",
    "media_contributor_tasks_require_timestamped_claim_rows_and_caveats"
  ],
  "target_projector": {
    "id": "source_projector_P_fin_b",
    "display": "P_fin^b: F_phys^b(O) -> K_b",
    "domain": "F_phys^b(O)",
    "codomain": "K_b",
    "required_content": [
      "exact_formula",
      "construction_rule",
      "derivation_cell",
      "exact_map_data"
    ],
    "required_provenance": "gu-derived",
    "current_status": "absent"
  },
  "carrier": {
    "formula": "K_b=V_L direct_sum V_R",
    "V_L": "(4,2,1)",
    "V_R": "(4bar,1,2)",
    "dim_C_K_b": 16,
    "status": "representation_carrier_only"
  },
  "acceptable_evidence_kinds": {
    "primary_source_exact_formula": "advance_to_one_mode_certificate_if_local_and_quotient_well_defined",
    "primary_source_construction_rule": "advance_to_one_mode_certificate_if_source_derived_and_target_free",
    "repo_local_derivation_from_primary_receipt": "advance_if_inputs_are_named_GU_source_objects",
    "exact_map_data_with_source_provenance": "advance_if_map_selection_is_GU_derived_not_fitted",
    "explicit_negative_receipt": "keep_blocked_and_update_availability_ledger"
  },
  "local_mode_prerequisites": [
    "sector_id",
    "source_surface_id",
    "source_locator",
    "source_text_or_formula_reference",
    "source_claim_type",
    "F_phys^b(O)_definition",
    "physical_quotient_policy",
    "gauge_constraint_ghost_null_policy",
    "source_projector_P_fin_b",
    "projector_domain",
    "projector_codomain",
    "projector_well_defined_on_physical_quotient",
    "projector_locality_statement",
    "projector_gu_derived_provenance",
    "target_import_flag_false",
    "selected_slot",
    "raw_or_physical_representative",
    "local_support_or_local_algebra_inclusion",
    "exact_image_in_K_b",
    "source_operator_section_constraint_reference",
    "effect_type",
    "projection_status",
    "finality_status",
    "loss_status",
    "rejection_or_import_control_status"
  ],
  "rejection_import_controls": {
    "ordinary_Pati_Salam_representation_labels": "representation_label_only",
    "identity_Gram_or_chosen_basis_Gram": "import_control",
    "Bell_state_or_Tsirelson_state": "control_only",
    "Pauli_CHSH_observables": "control_only",
    "standard_free_Fock_or_Hadamard_vacuum": "external_qft_import",
    "target_fitted_covariance_or_density_matrix": "target_smuggling",
    "K_b_direct_sum_as_rho_AB": "category_error",
    "media_paraphrase_without_timestamp_context": "unverified_source_pointer",
    "claim_row_without_rule_or_map_data": "provenance_only"
  },
  "source_first_sequence": [
    "mine_primary_GU_source_surface",
    "extract_timestamped_or_manuscript_located_receipt",
    "classify_receipt_kind",
    "define_F_phys_b_O_after_equations_gauge_constraints_ghosts_nulls",
    "define_P_fin_b_from_F_phys_b_O_to_K_b",
    "prove_P_fin_b_gu_derived_and_well_defined_on_physical_quotient",
    "emit_one_local_mode_certificate",
    "emit_exactly_16_local_mode_records",
    "build_H_raw_from_certified_source_representatives",
    "define_removed_representatives_and_Q_b",
    "test_H_phys_equals_Q_star_H_raw_Q_for_PSD_and_nonzero_rank",
    "route_to_covariance_rho_AB_admissible_observables_CHSH"
  ],
  "forbidden_as_evidence_for_projector": [
    "H_raw",
    "Q_b",
    "H_phys",
    "matrix_positivity",
    "covariance",
    "rho_AB",
    "CHSH_value",
    "Bell_violation"
  ],
  "first_exact_obstruction": {
    "id": "source_projector_P_fin_b",
    "formal_name": "P_fin^b_from_F_phys_b_O_to_K_b_with_gu_derived_provenance",
    "current_status": "absent",
    "why_first": "K_b_is_named_but_no_slot_is_certified_as_an_image_of_a_local_physical_GU_source_mode",
    "blocks_before": [
      "exactly_16_local_mode_records",
      "raw_representatives",
      "local_support_or_local_algebra_inclusion",
      "H_raw",
      "removed_representatives_R_b",
      "Q_b",
      "H_phys",
      "matrix_positivity",
      "rank_nonzero",
      "covariance",
      "rho_AB",
      "admissible_CHSH_observables",
      "CHSH_value",
      "Bell_violation"
    ]
  },
  "constructive_next_object": {
    "id": "PFinBSourceReceiptRow_V1",
    "required_fields": [
      "source_surface_id",
      "source_kind",
      "source_locator",
      "timestamp_or_manuscript_locator",
      "transcript_or_formula_excerpt",
      "claim_type",
      "exact_topic",
      "receipt_kind",
      "emitted_projector_or_rule",
      "emitted_domain",
      "emitted_codomain",
      "F_phys_b_O_dependencies",
      "physical_quotient_policy",
      "locality_prerequisites",
      "gu_provenance_reference",
      "target_import_flag",
      "import_control_result",
      "mode_fields_unlocked",
      "matrix_stage_unlocked",
      "promotion_allowed",
      "next_action"
    ],
    "receipt_kinds_that_unlock_one_mode_if_controls_pass": [
      "exact_formula",
      "construction_rule",
      "derivation_cell",
      "exact_map_data"
    ],
    "receipt_kinds_that_do_not_unlock_matrix_stage": [
      "negative_receipt",
      "terminology_only",
      "representation_label_only",
      "process_or_provenance_only",
      "import_control",
      "unverified_pointer"
    ]
  },
  "GU_impact": "QFT_finite_source_branch_open_but_blocked_before_source_extraction",
  "next_step": "Run_PFinBSourceReceiptRow_V1_against_one_primary_source_surface_before_SingleModePFinBImageCertificate_V1",
  "source_surfaces_prioritized": [
    "GU-MEDIA-2013-OXFORD",
    "GU-POD-2020-PORTAL-SPECIAL",
    "GU-MEDIA-2021-DRAFT-RELEASE",
    "GU-POD-2021-JRE-1628",
    "GU-POD-2025-TOE-JAIMUNGAL-GU-40",
    "GU-POD-2021-KEATING-REVEALED-1",
    "GU-POD-2021-KEATING-REVEALED-2"
  ],
  "not_promoted": [
    "P_fin_b",
    "one_local_source_mode",
    "sixteen_mode_packet",
    "positive_finite_one_particle_seed",
    "QFT_recovery",
    "covariance",
    "rho_AB",
    "CHSH",
    "Bell_violation"
  ]
}
```
