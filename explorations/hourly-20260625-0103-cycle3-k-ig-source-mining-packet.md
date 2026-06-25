---
title: "Hourly 20260625 0103 Cycle 3 K_IG Source Mining Packet V1"
status: draft
doc_type: hourly_cycle3_k_ig_source_mining_packet
verdict: "CONDITIONAL_PACKET_READY_NO_SOURCE_RECEIPT_CLAIMED"
owned_path: "explorations/hourly-20260625-0103-cycle3-k-ig-source-mining-packet.md"
companion_audit: "tests/hourly_20260625_0103_cycle3_k_ig_source_mining_packet_audit.py"
created_at: "2026-06-25"
run: "hourly-20260625-0103 3-1-5-4 cycle 3 lane 1"
---

# Hourly 20260625 0103 Cycle 3 K_IG Source Mining Packet V1

## 1. Verdict

Verdict: **conditional packet ready; no source receipt claimed**.

This artifact does not assert that a source excerpt, manuscript cell, transcript
row, or primary GU axiom exists. It specifies the exact source-mining packet
needed to decide whether the missing object

```text
SourceForcedCodomainSelectorForK_IG
```

can be supplied from primary GU source material.

Decision state:

| decision | status | reason |
|---|---:|---|
| `SOURCE_RECEIPT_FOUND` | no | this lane did not mine or verify a new source excerpt |
| `PACKET_READY` | yes | accept/reject conditions, extraction fields, and task contract are specified |
| `K_IG_SELECTED` | no | no source-forced codomain selector is supplied here |
| `ALTERNATIVES_ELIMINATED` | no | eliminators remain required evidence, not current conclusions |
| `FLRW_OR_DARK_ENERGY_PROMOTED` | no | target coefficient work is explicitly downstream and disallowed |

The packet is decision-grade because a future source miner can return one of
three closed outcomes:

```text
ACCEPT_SOURCE_FORCED_SELECTOR
REJECT_SELECTOR_ROUTE
INSUFFICIENT_RECEIPT_CONTINUE_MINING
```

## 2. Direct source derivations

The required inputs imply the following bounded facts.

1. `RESEARCH-POSTURE.md` requires constructive obstruction, explicit
   assumptions, rollback conditions, and no conversion of compatibility into
   derivation.
2. `process/runbooks/five-lane-frontier-run.md` requires a decision-grade lane,
   exact first obstruction, constructive next object, and no parallel-worker
   overlap.
3. The Cycle 2 K_IG eliminator search blocks at the absence of a repo-local
   source axiom, theorem, or eliminator for
   `SourceForcedCodomainSelectorForK_IG`.
4. The Cycle 2 primary source receipt ledger classifies IG as having source
   surfaces, reconstruction proposals, transcript hints, and representation
   labels, but no primary source receipt for the selector.
5. `sources/media-index.md` lists relevant source surfaces, especially
   `GU-MEDIA-2013-OXFORD`, `GU-MEDIA-2020-PORTAL-SPECIAL`,
   `GU-MEDIA-2021-DRAFT-RELEASE`, `GU-MEDIA-2020-JRE-1453`,
   `GU-POD-2021-JRE-1628`, `GU-POD-2021-KEATING-REVEALED-1`,
   `GU-POD-2021-KEATING-REVEALED-2`, `GU-POD-2025-TOE-JAIMUNGAL-GU-40`, and
   modern Keating/DESI surfaces.
6. `sources/media-index.md` also states that media entries are provenance maps,
   not proof, and that mathematical use requires transcript/timestamp/context.
7. `sources/media-contributor-tasks-v1.md` supplies issue-ready claim-mining
   discipline: exact source IDs, timestamp rows, caveats, and no invented
   timestamps.

Therefore this lane can specify what must be mined, but it cannot promote
`K_IG = D_A U` or any target-facing claim.

## 3. What would count as a source receipt

The route is accepted only if a primary GU source supplies one of the following
receipt kinds.

| receipt kind | what must be extracted | why it would count |
|---|---|---|
| `EXPLICIT_SELECTOR_AXIOM` | a source-native statement selecting an IG operator codomain, parent degree, projection policy, and lower-order policy | directly supplies the missing selector |
| `DERIVATION_CELL` | a derivation from source-native IG data to an exterior 2-form operator with no target input | supplies a constructive theorem candidate |
| `PRIMARY_ACTION_SLOT` | a source action or parent-action slot whose variation forces the K_IG operator and its momentum degree | ties codomain selection to source dynamics |
| `PROJECTION_LOSS_RULE` | source language proving Shiab/projection/loss cannot hide a different first-order selector | eliminates projected competitors |
| `LOWER_ORDER_RIGIDITY_RULE` | source language fixing or forbidding lower-order affine additions to `D_A U` | eliminates dressed exterior competitors |

Minimum acceptance packet:

```text
source_id
primary_locator
source_status
receipt_kind
exact_excerpt_or_derivation_cell
source_context_before_after
emitted_operator_or_rule
selected_codomain
selected_parent_momentum_degree
principal_symbol_or_finality_class
projector_policy
lower_order_policy
boundary_or_variation_class
eliminated_competitor_classes
target_inputs_seen
absorber_check
target_import_check
promotion_decision
rollback_condition
```

The exact source excerpt may be a direct transcript excerpt, manuscript passage,
displayed formula, diagram cell with transcript anchor, or a source-native
derivation. A paraphrase, secondary summary, or reconstruction-only formula does
not count by itself.

## 4. Accept conditions

The route can be accepted only when all checks below pass.

| check | pass condition |
|---|---|
| primary locator | source ID, URL or manuscript locator, timestamp/page/section, and extraction date are present |
| exact evidence | exact excerpt or derivation cell is quoted or transcribed with enough local context to audit meaning |
| source-native data | the selected rule is expressed in GU source terms, not in downstream target labels |
| codomain selector | one codomain is selected before targets; for the exterior candidate this must be `Omega^2(Y, ad P)` or source-equivalent language |
| parent degree selector | the paired parent momentum degree is fixed with the same source evidence |
| competitor eliminators | coderivative/trace, symmetric derivative, projected derivative, and lower-order-dressed exterior classes are each eliminated or explicitly ruled irrelevant by the same receipt package |
| projection-loss check | Shiab/projection/loss language does not permit a distinct projected first-order operator |
| lower-order rigidity | affine lower-order freedom is fixed to one value or forbidden |
| target-import check | no FLRW, theta, dark-energy, Lambda, DESI, cosmological, or empirical-fit target is used to choose the selector |
| absorber check | source wording is not merely absorbed into an already chosen reconstruction without independent source force |
| replacement check | replacing target labels with neutral labels leaves the selector unchanged |

Acceptance decision:

```text
ACCEPT_SOURCE_FORCED_SELECTOR
```

is allowed only if exactly one candidate class survives before targets and all
four non-selected classes have source-side eliminators.

## 5. Reject conditions

The route must be rejected, not left ambiguous, if any of the following occurs.

| reject code | rejection condition |
|---|---|
| `SECONDARY_ONLY` | evidence comes only from summaries, interviews about reception, wiki prose, or contributor reconstruction |
| `NO_OPERATOR_OR_RULE` | the source discusses GU framing, observerse, Shiab, or projection but emits no operator, codomain, parent-action slot, or eliminator |
| `TARGET_IMPORTED_SELECTOR` | the selector is chosen because it fits theta/FLRW, dark energy, Lambda, DESI, or other target behavior |
| `MULTIPLE_SURVIVORS` | more than one candidate class remains admissible before target comparison |
| `PROJECTOR_AMBIGUITY` | source projection/loss language allows a distinct projected derivative selector |
| `LOWER_ORDER_FREEDOM` | source language permits `D_A U + L_{s,epsilon}(U)` without fixing `L` |
| `ABSORBER_ONLY` | the excerpt can be read only as compatible with the reconstruction, not as selecting it |
| `NO_SEQUENTIAL_GATE` | the report tries to proceed to target coefficients before the selector is settled |

Rejecting the route does not falsify GU. It rejects this source-forcing path for
`K_IG` until a stronger source receipt is supplied.

## 6. Strongest positive mining packet

The strongest positive packet to search for is:

```text
source_surface_priority:
  1. GU-MEDIA-2013-OXFORD / GU-MEDIA-2020-PORTAL-SPECIAL
  2. GU-MEDIA-2021-DRAFT-RELEASE and manuscript-adjacent release surfaces
  3. GU-POD-2021-JRE-1628 and Keating Revealed Part 1/2
  4. GU-POD-2025-TOE-JAIMUNGAL-GU-40 and modern Keating/DESI surfaces

target_object:
  SourceForcedCodomainSelectorForK_IG

desired receipt:
  source-native IG witness or parent-action language that emits:
    K_IG(U; A) = D_A U
    codomain Omega^2(Y, ad P), or exact source-equivalent
    P_IG paired in the same degree
    antisymmetric/exterior finality before targets
    projection-loss rule
    lower-order rigidity
```

Search terms and motifs:

```text
Shiab
projection
observerse
U^14 = met(X^4)
intrinsic geometry
auxiliary geometry
bundle of metrics
connection
curvature
field strength
source
action
parent action
sector I
operator
exterior derivative
antisymmetric derivative
trace
divergence
symmetrized derivative
```

Positive status if found:

```text
candidate_source_receipt_found_pending_formal_audit
```

not:

```text
K_IG_selected
dark_energy_derived
FLRW_packet_closed
```

## 7. First exact obstruction

The first exact obstruction remains:

```text
SourceForcedCodomainSelectorForK_IG
```

The obstruction is not that `D_A U` is ill typed. The obstruction is that the
repo lacks a primary source receipt that selects the exterior 2-form codomain,
fixes parent degree, and eliminates the four competitor classes before target
comparison.

This blocks before:

```text
Q_IG
Z_U
V_src
S_cross_src
parent action normalization
boundary variation
current extraction
conservation law
physical reduction
theta/FLRW coefficients
dark-energy or Lambda claims
```

## 8. Absorber and target-import checks

Absorber check:

```text
Does the source excerpt force the selector, or does the reconstruction merely
absorb broad source words such as geometry, projection, Shiab, or field strength
into an already preferred `D_A U` template?
```

Pass:

```text
The source gives a rule, axiom, action slot, or derivation whose emitted object
has one codomain and whose alternatives are eliminated.
```

Fail:

```text
The source language is compatible with `D_A U` but also compatible with a
coderivative, symmetric derivative, projected derivative, or lower-order-dressed
exterior operator.
```

Target-import check:

```text
Delete all target labels and empirical/cosmological motivations from the mining
report. The selected source packet must still choose the same codomain, parent
degree, projector policy, and lower-order policy.
```

Forbidden target inputs before selector:

```text
theta
FLRW
dark energy
Lambda
DESI
Z_theta
C_Rtheta
xi_eff
target coefficient fit
observational performance
```

## 9. Task contract for future source mining

Future source-mining task:

```text
Mine primary GU source surfaces for SourceForcedCodomainSelectorForK_IG without
claiming it exists. Return an evidence packet, not a prose summary.
```

Required output table:

| field | required content |
|---|---|
| `source_id` | one ID from `sources/media-index.md` or a new primary source ID added by maintainer review |
| `locator` | timestamp, transcript line, page, section, displayed formula, diagram cell, or exact video time |
| `receipt_kind` | one of `EXPLICIT_SELECTOR_AXIOM`, `DERIVATION_CELL`, `PRIMARY_ACTION_SLOT`, `PROJECTION_LOSS_RULE`, `LOWER_ORDER_RIGIDITY_RULE`, or `NO_RECEIPT` |
| `exact_excerpt_or_cell` | direct excerpt or faithful transcription with local context |
| `emitted_rule` | operator, codomain, parent slot, projection rule, or lower-order rule emitted by the source |
| `candidate_class_effect` | which of the five candidate classes it selects, eliminates, or leaves live |
| `absorber_check` | pass/fail with one-sentence reason |
| `target_import_check` | pass/fail with explicit target inputs seen; must be empty for acceptance |
| `accept_reject_decision` | `ACCEPT_SOURCE_FORCED_SELECTOR`, `REJECT_SELECTOR_ROUTE`, or `INSUFFICIENT_RECEIPT_CONTINUE_MINING` |
| `sequential_dependency` | statement that target-facing IG work remains blocked unless acceptance succeeds |

Required candidate-class table:

| class id | must decide |
|---|---|
| `EXT_DERIVATIVE` | selected by source, merely compatible, or rejected |
| `CODERIVATIVE_TRACE` | eliminated by source, live, or not addressed |
| `SYMMETRIC_DERIVATIVE` | eliminated by source, live, or not addressed |
| `PROJECTED_DERIVATIVE` | eliminated by source, live, or not addressed |
| `LOWER_ORDER_DRESSED_EXTERIOR` | eliminated by source, live, or not addressed |

Sequential dependency:

```text
Source mining -> selector receipt audit -> eliminator/finality certificate ->
only then target-facing theta/FLRW or dark-energy work.
```

## 10. GU impact

Allowed statement:

```text
The repo now has a decision-grade source-mining packet for testing whether
primary GU sources supply SourceForcedCodomainSelectorForK_IG.
```

Forbidden statements:

```text
The source receipt exists.
K_IG = D_A U is source-forced.
Naturalness eliminates all alternatives.
Target performance selects K_IG.
Branch 3 emits theta/FLRW coefficients.
GU derives dark energy, Lambda, Z_theta, C_Rtheta, or xi_eff.
```

Impact:

```text
Branch 3 remains a coherent host. The next sequential gate is primary-source
mining and receipt audit for K_IG, not target coefficient work.
```

## 11. Next step

Run one source-mining lane against a single high-priority surface, preferably
`GU-MEDIA-2013-OXFORD` / `GU-MEDIA-2020-PORTAL-SPECIAL` first, using the table
schema above. If that surface returns `NO_RECEIPT`, proceed to the 2021 draft
release surface before modern interviews.

Do not combine source mining with theta/FLRW target fitting in the same lane.

## 12. Machine-readable JSON summary

```json
{
  "artifact": "K_IGSourceMiningPacket_V1",
  "version": "2026-06-25",
  "run": "hourly-20260625-0103 3-1-5-4 cycle 3 lane 1",
  "verdict": "CONDITIONAL_PACKET_READY_NO_SOURCE_RECEIPT_CLAIMED",
  "verdict_class": "conditional",
  "source_receipt_claimed": false,
  "packet_ready": true,
  "target_object": "SourceForcedCodomainSelectorForK_IG",
  "direct_derivations": [
    "Research posture requires constructive obstruction and forbids compatibility-as-derivation.",
    "Five-lane runbook requires exact obstruction, constructive next object, and decision-grade output.",
    "Cycle 2 K_IG eliminator search blocks at no repo-local source axiom theorem or eliminator.",
    "Cycle 2 source receipt ledger classifies IG as missing primary receipt for SourceForcedCodomainSelectorForK_IG.",
    "Media index supplies source surfaces but says media entries are provenance maps not proof.",
    "Contributor task draft supplies exact source ID timestamp caveat and no-invented-timestamp discipline."
  ],
  "what_would_count": {
    "receipt_kinds": [
      "EXPLICIT_SELECTOR_AXIOM",
      "DERIVATION_CELL",
      "PRIMARY_ACTION_SLOT",
      "PROJECTION_LOSS_RULE",
      "LOWER_ORDER_RIGIDITY_RULE"
    ],
    "minimum_fields": [
      "source_id",
      "primary_locator",
      "source_status",
      "receipt_kind",
      "exact_excerpt_or_derivation_cell",
      "source_context_before_after",
      "emitted_operator_or_rule",
      "selected_codomain",
      "selected_parent_momentum_degree",
      "principal_symbol_or_finality_class",
      "projector_policy",
      "lower_order_policy",
      "boundary_or_variation_class",
      "eliminated_competitor_classes",
      "target_inputs_seen",
      "absorber_check",
      "target_import_check",
      "promotion_decision",
      "rollback_condition"
    ]
  },
  "accept_conditions": [
    "primary_locator_present",
    "exact_evidence_with_context_present",
    "source_native_data_not_target_labels",
    "one_codomain_selected_before_targets",
    "parent_degree_fixed_by_same_source_evidence",
    "four_competitor_classes_eliminated_or_ruled_irrelevant",
    "projection_loss_check_passes",
    "lower_order_rigidity_passes",
    "target_import_check_passes_with_no_target_inputs",
    "absorber_check_passes",
    "target_label_replacement_check_passes"
  ],
  "reject_conditions": [
    "SECONDARY_ONLY",
    "NO_OPERATOR_OR_RULE",
    "TARGET_IMPORTED_SELECTOR",
    "MULTIPLE_SURVIVORS",
    "PROJECTOR_AMBIGUITY",
    "LOWER_ORDER_FREEDOM",
    "ABSORBER_ONLY",
    "NO_SEQUENTIAL_GATE"
  ],
  "strongest_positive_packet": {
    "source_surface_priority": [
      "GU-MEDIA-2013-OXFORD",
      "GU-MEDIA-2020-PORTAL-SPECIAL",
      "GU-MEDIA-2021-DRAFT-RELEASE",
      "GU-POD-2021-JRE-1628",
      "GU-POD-2021-KEATING-REVEALED-1",
      "GU-POD-2021-KEATING-REVEALED-2",
      "GU-POD-2025-TOE-JAIMUNGAL-GU-40",
      "GU-POD-2025-KEATING-DESI-GU"
    ],
    "desired_emitted_rule": "source_native_IG_witness_or_parent_action_language_emits_K_IG_D_A_U_with_Omega2_adP_codomain_parent_degree_projection_loss_and_lower_order_rigidity",
    "positive_status_if_found": "candidate_source_receipt_found_pending_formal_audit",
    "not_a_promotion": true
  },
  "candidate_class_decisions_required": [
    {
      "id": "EXT_DERIVATIVE",
      "required_decision": "selected_by_source_merely_compatible_or_rejected"
    },
    {
      "id": "CODERIVATIVE_TRACE",
      "required_decision": "eliminated_by_source_live_or_not_addressed"
    },
    {
      "id": "SYMMETRIC_DERIVATIVE",
      "required_decision": "eliminated_by_source_live_or_not_addressed"
    },
    {
      "id": "PROJECTED_DERIVATIVE",
      "required_decision": "eliminated_by_source_live_or_not_addressed"
    },
    {
      "id": "LOWER_ORDER_DRESSED_EXTERIOR",
      "required_decision": "eliminated_by_source_live_or_not_addressed"
    }
  ],
  "first_exact_obstruction": {
    "id": "SourceForcedCodomainSelectorForK_IG",
    "still_missing": true,
    "description": "no primary source receipt currently selects exterior two form codomain fixes parent degree and eliminates competitor classes before targets",
    "blocks_before": [
      "Q_IG",
      "Z_U",
      "V_src",
      "S_cross_src",
      "parent_action_normalization",
      "boundary_variation",
      "current_extraction",
      "conservation_law",
      "physical_reduction",
      "theta_FLRW_coefficients",
      "dark_energy_or_Lambda_claims"
    ]
  },
  "absorber_target_checks": {
    "absorber_check_required": true,
    "absorber_pass_condition": "source_forces_rule_axiom_action_slot_or_derivation_with_one_codomain_and_eliminated_alternatives",
    "absorber_fail_condition": "source_language_only_compatible_with_preferred_reconstruction",
    "target_import_check_required": true,
    "target_inputs_allowed_before_selector": [],
    "forbidden_target_inputs_before_selector": [
      "theta",
      "FLRW",
      "dark_energy",
      "Lambda",
      "DESI",
      "Z_theta",
      "C_Rtheta",
      "xi_eff",
      "target_coefficient_fit",
      "observational_performance"
    ],
    "replacement_check": "selector_must_survive_replacing_target_labels_with_neutral_labels"
  },
  "future_task_contract": {
    "task": "Mine primary GU source surfaces for SourceForcedCodomainSelectorForK_IG without claiming it exists.",
    "required_output_fields": [
      "source_id",
      "locator",
      "receipt_kind",
      "exact_excerpt_or_cell",
      "emitted_rule",
      "candidate_class_effect",
      "absorber_check",
      "target_import_check",
      "accept_reject_decision",
      "sequential_dependency"
    ],
    "accepted_decisions": [
      "ACCEPT_SOURCE_FORCED_SELECTOR",
      "REJECT_SELECTOR_ROUTE",
      "INSUFFICIENT_RECEIPT_CONTINUE_MINING"
    ],
    "sequential_dependency": "Source mining -> selector receipt audit -> eliminator/finality certificate -> target-facing theta/FLRW or dark-energy work"
  },
  "anti_overclaim": {
    "source_receipt_exists": false,
    "K_IG_D_A_U_source_forced": false,
    "naturalness_eliminates_alternatives": false,
    "target_performance_selects_K_IG": false,
    "Branch_3_emits_theta_FLRW_coefficients": false,
    "GU_derives_dark_energy": false,
    "GU_derives_Lambda": false,
    "GU_derives_Z_theta": false,
    "GU_derives_C_Rtheta": false,
    "GU_derives_xi_eff": false
  },
  "claim_impact": {
    "Branch_3_status": "coherent_host_not_selected_dynamics",
    "next_gate": "primary_source_mining_and_receipt_audit_for_K_IG",
    "target_work_allowed_next": false
  },
  "next_step": "Mine GU-MEDIA-2013-OXFORD or GU-MEDIA-2020-PORTAL-SPECIAL first using the packet schema; if no receipt is found proceed to the 2021 draft release surface before modern interviews."
}
```

## Sources read

- `RESEARCH-POSTURE.md`
- `process/runbooks/five-lane-frontier-run.md`
- `explorations/hourly-20260625-0103-cycle2-k-ig-source-axiom-eliminator-search.md`
- `explorations/hourly-20260625-0103-cycle2-primary-gu-source-receipt-availability-ledger.md`
- `sources/media-index.md`
- `sources/media-contributor-tasks-v1.md`
