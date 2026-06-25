---
title: "Hourly 20260625-0103 Cycle 1 DGU 01 Operator Source Receipt"
date: "2026-06-25"
run: "hourly-20260625-0103"
cycle: "1"
lane: "4"
doc_type: dgu_operator_source_receipt
receipt_id: "DGU01OperatorSourceReceipt_V1"
verdict: "UNDERDEFINED_BLOCKED__REJECT_NO_PRIMARY_ACTION_OR_EL"
owned_path: "explorations/hourly-20260625-0103-cycle1-dgu-01-operator-source-receipt.md"
companion_audit: "tests/hourly_20260625_0103_cycle1_dgu_01_operator_source_receipt_audit.py"
---

# Hourly 20260625-0103 Cycle 1 DGU 01 Operator Source Receipt

## 1. Verdict

Verdict: **underdefined / blocked**.

`DGU01OperatorSourceReceipt_V1` does not accept a primary source receipt for the
actual `D_GU^epsilon` 0/1-sector operator from the repo sources checked here.

The strongest available source chain is:

```text
UCSD transcript / older reconstruction:
  Dirac-DeRham-Einstein rolled-up complex with a ship-in-a-bottle map

typed operator spine:
  D_roll^epsilon(u, psi)
    =
    (d_A^* psi, d_A u + lambda_d Phi_2(d_A psi)) + Z_A^epsilon(u, psi)

typed VZ algebra:
  conditional Q-sector and spin-3/2 Schur algebra if actual D_GU supplies this block
```

That chain is not a primary action/operator/Euler-Lagrange receipt for the actual
`D_GU^epsilon` sector. The receipt decision is therefore:

```text
receipt_decision: REJECT_NO_PRIMARY_ACTION_OR_EL
can_accept_source_receipt: false
typed_spine_candidate_is_primary_source: false
first_exact_missing_field:
  operator_source_primary_action_or_EL
```

This artifact does **not** claim actual operator identification, FC-VZ-1 closure,
FC-VZ-4 closure, VZ evasion, hyperbolicity, causality, or absence of spacelike
characteristics.

## 2. What Was Derived Directly From Repo Sources

`RESEARCH-POSTURE.md` requires source discipline: explicit assumptions, rollback
conditions, dependency tracking, promotion criteria, and no conversion of compatibility
into derivation.

`process/runbooks/five-lane-frontier-run.md` requires a decision-grade lane artifact
that names the first exact missing proof object and preserves the distinction between
hosted, compatible, conditional, and derived.

`explorations/hourly-cycle3-dgu-operator-source-receipt-inventory-2026-06-25.md`
already identifies the source-receipt gap. It records `D_roll` as a typed-spine
candidate and the typed E-block algebra as a reusable backend, but not as a source
receipt for actual `D_GU^epsilon`.

`explorations/hourly-cycle2-actual-dgu-operator-certificate-schema-2026-06-25.md`
defines the downstream certificate and names the first missing source field:

```text
ActualDGU01OperatorCertificate.source.operator_source_primary_action_or_EL
```

`explorations/hourly-cycle2-vz-actual-operator-certificate-gate-2026-06-24.md`
requires the actual-operator gate to start from the GU action/operator/EL source,
not from a displayed VZ block.

`explorations/gu-typed-operator-action-spine-2026-06-24.md` supplies the best
positive candidate. It is explicitly a canonical proposal, not proof-grade closure.
It separates:

```text
Phi_2                 zero-order algebraic shiab
Phi_d := Phi_2 o d_A  first-order differential composite
F_xi := sigma_1(Phi_d)(xi)
Phi_F := Phi_2(F_A tensor -) zero-order curvature insertion
```

`explorations/vz-proof-grade-closure-attempt-2026-06-24.md` closes the typed-spine
principal-symbol Schur algebra conditional on the actual operator having the typed
block and `lambda_d != 0`. It does not prove that the primary GU source emits that
operator.

Additional locator checks found:

```text
explorations/primary-gu-interface-contract-2026-06-24.md:
  source-geometry interface contract; primary action still underdefined.

explorations/goal-draft-primary-gu-action-operator-spec-2026-06-24.md:
  draft goal requesting exactly the missing primary operator/action specification.

explorations/generation-count-cl95-dirac-derham-2026-06-22.md:
  older reconstruction of D_GU = (d + d*) tensor 1_S + Phi and rolled-up structure,
  but exploration/reconstruction-grade rather than a primary source receipt.

explorations/weinstein-ucsd-2025-04-analysis-2026-06-22.md:
  transcript analysis names the Dirac-DeRham-Einstein complex and ship-in-a-bottle
  object, but explicitly labels the formalization as exploration-grade.
```

So the direct result is a **negative receipt decision**, not a source closure.

## 3. The Strongest Positive Result

The strongest positive result is a precise candidate payload for the receipt:

```text
candidate_id:
  typed_spine_candidate

operator_candidate:
  D_roll^epsilon(u, psi)
    =
    (d_A^* psi, d_A u + lambda_d Phi_2(d_A psi)) + Z_A^epsilon(u, psi)

principal_candidate:
  sigma_1(D_roll^epsilon)(xi)(u, psi)
    =
    (i_xi psi, xi tensor u + lambda_d F_xi psi)

order_split:
  Phi_2: zero-order algebraic shiab
  Phi_d: first-order Phi_2 o d_A
  F_xi: sigma_1(Phi_d)(xi)
  Phi_F: zero-order curvature insertion, not F_xi
```

If a primary GU action/operator/Euler-Lagrange derivation emitted this exact 0/1
sector, with fixed chirality, Q projectors, coordinate convention, source-derived
`a`, `b`, `lambda_d`, and all extra first-order terms listed or audited, then the
receipt would accept and the next object would be
`ActualDGU01OperatorCertificateInstance_V1`.

The current repo sources stop before that first source arrow:

```text
primary GU action/operator/EL
  -> actual D_GU^epsilon 0/1 operator
```

The typed-spine candidate can define what to test. It cannot certify that the
actual GU source selected it.

## 4. The First Exact Obstruction Or Missing Proof Object

The first exact obstruction is:

```text
operator_source_primary_action_or_EL
```

In downstream certificate notation this is:

```text
ActualDGU01OperatorCertificate.source.operator_source_primary_action_or_EL
```

This field must contain a locator or derivation cell for one of:

```text
primary_GU_action
primary_GU_operator_definition
Euler_Lagrange_derivation_from_primary_action
```

and it must emit, before using typed VZ output:

```text
D_GU^epsilon on the rolled-up 0/1 sector
sigma_1(D_GU^epsilon)(y, xi)
source-derived a, b, lambda_d
Phi_2/Phi_d/F_xi/Phi_F order split
Q_in/Q_out projectors
coordinate convention
complete extra first-order 0/1 term ledger
```

The exact failed candidate is:

```text
typed_spine_candidate
```

Failure reason:

```text
typed_spine_candidate is a canonical proposal and reconstruction target,
not a primary GU action/operator/Euler-Lagrange receipt.
```

## 5. The Constructive Next Object That Would Remove Or Test The Obstruction

The constructive next object is:

```text
ActualDGU01OperatorCertificateInstance_V1
```

but only **after** this smaller receipt accepts. Since the receipt rejects here, the
immediate constructive work packet is still source extraction:

```text
1. Locate a primary GU action/operator/EL source.
2. Extract the actual D_GU^epsilon 0/1 operator.
3. Compute sigma_1(D_GU^epsilon) from that source.
4. Compare it to D_roll without changing conventions after the fact.
5. Emit ActualDGU01OperatorCertificateInstance_V1 only if the source receipt accepts.
```

Acceptance would require:

```text
source_locator_present
primary_source_status = primary
operator_emitted = actual_D_GU_epsilon_0_1
principal_symbol_emitted = sigma_1_from_source
typed_spine_candidate_is_primary_source = false
typed_spine_match in {exact_match, differs_with_listed_terms}
```

## 6. What This Means For The Relevant GU Claim

The relevant GU claim remains live but unpromoted.

Current status:

```text
actual operator identification: not claimed
source receipt for actual D_GU^epsilon 0/1 sector: rejected for current sources
typed-spine route: coherent candidate
FC-VZ-1 for actual D_GU: open
FC-VZ-4 for actual section-pulled operator: open
VZ evasion: not claimed
hyperbolicity: not claimed
causality: not claimed
absence of spacelike characteristics: not claimed
```

The positive meaning is that the repo has a clear target shape for the primary
operator. The negative meaning is that the target shape has not yet been proved to be
the actual source-selected `D_GU^epsilon`.

## 7. Next Meaningful Proof Or Computation Step

The next meaningful step is a source-locator and extraction pass, not another typed
matrix inverse:

```text
source extraction target:
  primary_GU_action_or_operator_or_EL_for_D_GU_epsilon_0_1

minimum computation:
  compute sigma_1(D_GU^epsilon)(y, xi) directly from that source

first comparison:
  check whether the actual one-form block contains
  lambda_d Phi_2(d_A psi)
  with lambda_d source-derived and nonzero

first fail condition:
  only typed_spine_candidate or reconstruction algebra is available
```

If the source emits only `Phi_F(A)` and not `Phi_d`, the current typed VZ `F_xi`
route fails for the actual operator and must be rebuilt.

## 8. Machine-Readable JSON Summary

```json
{
  "artifact": "DGU01OperatorSourceReceipt_V1",
  "run": "hourly-20260625-0103",
  "cycle": "1",
  "lane": "4",
  "verdict": "UNDERDEFINED_BLOCKED__REJECT_NO_PRIMARY_ACTION_OR_EL",
  "verdict_class": "underdefined_blocked",
  "receipt_decision": "REJECT_NO_PRIMARY_ACTION_OR_EL",
  "can_accept_source_receipt": false,
  "can_emit_actual_dgu_certificate_instance": false,
  "first_exact_missing_field": "operator_source_primary_action_or_EL",
  "first_exact_obstruction": "ActualDGU01OperatorCertificate.source.operator_source_primary_action_or_EL",
  "receipt_fields": {
    "source_locator": null,
    "source_kind": "missing",
    "source_status": "missing",
    "operator_source_primary_action_or_EL": null,
    "operator_emitted": null,
    "principal_symbol_emitted": null,
    "coefficients_source_derived": {
      "a": false,
      "b": false,
      "lambda_d": false
    },
    "typed_spine_candidate": "D_roll_typed_spine_candidate",
    "typed_spine_candidate_is_primary_source": false,
    "typed_spine_match": "no_operator_emitted",
    "extra_first_order_terms_ledger": "missing_for_actual_operator"
  },
  "source_candidates_checked": [
    {
      "candidate": "primary_GU_action_or_operator_or_EL",
      "status": "missing",
      "accepted_as_primary_source_receipt": false,
      "reason": "no primary action/operator/Euler-Lagrange locator emitted the actual D_GU_epsilon_0_1 operator"
    },
    {
      "candidate": "typed_spine_candidate",
      "status": "typed_spine_candidate",
      "accepted_as_primary_source_receipt": false,
      "reason": "canonical proposal not primary source receipt"
    },
    {
      "candidate": "D_roll_reconstruction_algebra",
      "status": "reconstruction_algebra",
      "accepted_as_primary_source_receipt": false,
      "reason": "conditional algebra backend does not identify actual D_GU"
    },
    {
      "candidate": "UCSD_transcript_rolled_up_complex",
      "status": "primary_source_context_but_not_operator_receipt",
      "accepted_as_primary_source_receipt": false,
      "reason": "names rolled-up Dirac-DeRham-Einstein structure but does not provide the required actual 0_1 formula, coefficients, projectors, and principal symbol"
    }
  ],
  "direct_repo_derivations": {
    "RESEARCH-POSTURE.md": "requires explicit assumptions, rollback conditions, and no compatibility-to-derivation promotion",
    "process/runbooks/five-lane-frontier-run.md": "requires decision-grade artifact and exact missing proof object",
    "explorations/hourly-cycle3-dgu-operator-source-receipt-inventory-2026-06-25.md": "source receipt for actual D_GU_epsilon_0_1 is missing; typed spine is not receipt",
    "explorations/hourly-cycle2-actual-dgu-operator-certificate-schema-2026-06-25.md": "first missing field is source.operator_source_primary_action_or_EL",
    "explorations/hourly-cycle2-vz-actual-operator-certificate-gate-2026-06-24.md": "actual certificate must start from action/operator/EL source, not displayed VZ matrix",
    "explorations/gu-typed-operator-action-spine-2026-06-24.md": "D_roll is canonical proposal not proof-grade source closure",
    "explorations/vz-proof-grade-closure-attempt-2026-06-24.md": "typed-spine Schur algebra closes conditionally on actual source containing the block"
  },
  "strongest_positive_result": {
    "candidate": "D_roll^epsilon(u,psi)=(d_A^* psi, d_A u + lambda_d Phi_2(d_A psi)) + Z_A^epsilon(u,psi)",
    "principal_candidate": "sigma_1(D_roll^epsilon)(xi)(u,psi)=(i_xi psi, xi tensor u + lambda_d F_xi psi)",
    "candidate_status": "coherent_typed_spine_candidate",
    "requires_primary_source_receipt": true,
    "requires_actual_sigma_1_D_GU": true,
    "requires_source_derived_a_b_lambda_d": true,
    "requires_extra_first_order_terms_audited": true,
    "accepted_as_receipt": false
  },
  "receipt_acceptance_conditions": [
    "source_locator_present",
    "source_status_primary",
    "operator_source_primary_action_or_EL_present",
    "actual_D_GU_epsilon_0_1_formula_emitted",
    "sigma_1_D_GU_epsilon_computed_from_source",
    "a_b_lambda_d_source_derived",
    "Phi_2_Phi_d_F_xi_Phi_F_order_split_preserved",
    "Q_in_Q_out_projectors_fixed",
    "coordinate_convention_fixed",
    "extra_first_order_terms_listed_or_kernel_audited",
    "typed_spine_candidate_not_used_as_primary_source"
  ],
  "constructive_next_object": "ActualDGU01OperatorCertificateInstance_V1",
  "constructive_next_object_allowed_only_if_receipt_accepts": true,
  "explicit_non_claims": {
    "actual_operator_identification": false,
    "FC-VZ-1_closed_for_actual_D_GU": false,
    "FC-VZ-4_closed_for_actual_section_pulled_operator": false,
    "VZ_evasion_closed": false,
    "hyperbolicity_established": false,
    "causality_established": false,
    "absence_of_spacelike_characteristics_proved": false
  },
  "rollback_conditions": [
    "operator_source_primary_action_or_EL_missing",
    "typed_spine_candidate_as_primary_source",
    "typed_spine_only",
    "reconstruction_algebra_only",
    "actual_operator_formula_absent",
    "actual_D_GU_0_1_block_absent",
    "actual_operator_differs_from_D_roll_typed_spine",
    "rolled_up_domain_or_codomain_mismatch",
    "coefficient_a_not_source_derived",
    "coefficient_b_not_source_derived",
    "coefficient_lambda_d_not_source_derived",
    "coefficient_lambda_d_zero",
    "Phi_d_not_present_as_order_one_source_of_F_xi",
    "Phi_F_used_as_F_xi_principal_block",
    "Q_in_Q_out_projectors_missing_or_unnormalized",
    "extra_first_order_terms_not_audited",
    "trace_coordinate_and_embedded_coordinate_conventions_mixed"
  ],
  "next_meaningful_step": [
    "locate_primary_GU_action_operator_or_EL_source",
    "extract_actual_D_GU_epsilon_0_1_operator",
    "compute_sigma_1_D_GU_epsilon_from_source",
    "compare_actual_operator_to_D_roll_without_convention_change",
    "derive_source_coefficients_a_b_lambda_d",
    "list_or_audit_extra_first_order_terms",
    "emit_ActualDGU01OperatorCertificateInstance_V1_only_if_receipt_accepts"
  ]
}
```
