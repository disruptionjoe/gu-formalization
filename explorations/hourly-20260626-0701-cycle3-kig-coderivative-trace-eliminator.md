---
title: "Hourly 20260626 0701 Cycle 3 KIG Coderivative Trace Eliminator"
date: "2026-06-26"
run_id: "hourly-20260626-0701"
cycle: 3
lane: 3
doc_type: "frontier_run_lane_artifact"
artifact_id: "CoderivativeTraceEliminatorForK_IG_0701_C3_V1_Result"
verdict: "blocked_coderivative_trace_survives_no_positive_exterior_degree_rule"
owned_path: "explorations/hourly-20260626-0701-cycle3-kig-coderivative-trace-eliminator.md"
claim_status_change: false
---

# Hourly 20260626 0701 Cycle 3 KIG Coderivative Trace Eliminator

## 1. Verdict

Verdict: **blocked / eliminator not admitted**.

`CoderivativeTraceEliminatorForK_IG_V1` does not close from current repo
sources. The current source criteria do not eliminate `CODERIVATIVE_TRACE`
before target data. The rival remains live.

Decision state:

```text
coderivative_trace_eliminator_admitted: false
positive_exterior_degree_rule_present: false
coderivative_trace_eliminated: false
surviving_class_count: 5
D_A U admissible: true
D_A U source-forced: false
Branch 3 admitted: false
target_import_used: false
claim_status_consistency_triggered: false
```

This preserves the cycle 2 result, but makes the first sub-gate explicit:
without a source-only rule forcing positive exterior 2-form degree for the
selected `K_IG` witness, `D_A^* U` and metric-trace variants cannot be excluded
by source criteria alone.

## 2. Source Criteria Tested

Starting from the cycle 2 bundle, the gate tested this implication:

```text
SourceWitnesses
+ AdmissibleIGWitnessPreorder
+ CodomainPolicy
+ ParentMomentumDegreePolicy
+ BoundaryClass
+ TargetReplacementGuard
  -> contraction/trace and 0-form K_IG witnesses are not admissible
     selected source operators.
```

For this implication to pass, current sources would have to supply at least:

```text
PositiveExteriorDegreeRuleForK_IG:
  source-only data force selected_codomain = Omega^2(Y, ad P)
  before target chirality, exact-GR, theta/FLRW, Lambda, DESI,
  xi_eff, residual, or coefficient behavior is read.
```

Then a trace-exclusion lemma could use that rule:

```text
TraceContractionExclusionLemmaForK_IG:
  D_A^* U and trace_g(nabla_A U) land in a 0-form or trace sector,
  so they violate the source-forced exterior 2-form codomain.
```

The antecedent is absent. The repository contains predecessor artifacts naming
this rule as missing, not as admitted.

## 3. What Was Derived Directly From Repo Sources

The read-first sources and targeted K_IG artifacts support these bounded facts.

1. `RESEARCH-POSTURE.md` permits constructive missing-object work, but forbids
   target import and treating compatibility or naturalness as derivation.
2. `process/runbooks/five-lane-frontier-run.md` requires a decision-grade
   verdict and the first exact missing proof object.
3. Cycle 1 found no exterior singleton certificate. It recorded five surviving
   classes and named `CoderivativeTraceEliminatorForK_IG` as the first missing
   eliminator.
4. Cycle 2 attempted the non-exterior rival eliminator bundle and rejected it at
   this same first sub-gate because no positive exterior-degree rule was present.
5. The 0604 and 0502 K_IG gates record the same source-side obstruction:
   no `ExteriorCodomainFinalityAxiomForK_IG`,
   no `SourceForcedCodomainSelectorForK_IG`, and no source rule fixing the
   parent momentum degree to the exterior 2-form sector.
6. The 2026-06-25 witness-selection test gives the concrete rival:
   `D_A^* U` or the metric trace of `nabla_A U`, with a 0-form or trace-sector
   codomain. It survives because `g_Y` and the connection make the expression
   source-natural at the schematic class level while the exterior parent degree
   is not source-fixed.
7. Targeted repo search finds `PositiveExteriorDegreeRuleForK_IG` and
   `TraceContractionExclusionLemmaForK_IG` only as missing requirements or
   proposed next objects, not as admitted source results.

Therefore the repo directly derives an admissible exterior candidate and a
precise rival. It does not derive the eliminator.

## 4. Strongest Positive Attempt

The strongest target-free positive packet remains:

```text
U in Omega^1(Y, ad P)
A an Sp(64) connection on P -> Y
D_A the induced covariant exterior derivative

K_ext(U; A) = D_A U in Omega^2(Y, ad P)
parent slot = int_Y <P_IG, D_A U>_{Q_IG}
```

The strongest conditional eliminator statement is:

```text
If source data first force selected_codomain = Omega^2(Y, ad P)
and selected_parent_momentum_degree = Omega^2(Y, ad P),
then D_A^* U and trace_g(nabla_A U) are not valid selected K_IG witnesses
because their codomain is a contraction/trace or 0-form sector.
```

That is a valid conditional. It is not a current source-derived theorem.

## 5. Coderivative/Trace Gate Result

Rival tested:

```text
CODERIVATIVE_TRACE:
  K_trace(U; A) = D_A^* U
  or
  K_trace(U; A) = trace_g(nabla_A U)
```

Gate matrix:

| field | required for elimination | current source result |
|---|---|---|
| source inputs | `U`, `A`, `g_Y` / compatible connection tracked without targets | present enough to host both exterior and trace-style expressions |
| codomain rule | selected `K_IG` codomain must be source-forced to `Omega^2(Y, ad P)` | absent |
| parent degree rule | parent field degree must be source-forced to the exterior 2-form sector | absent |
| trace exclusion | contraction/trace and 0-form codomains violate a source rule | absent because the source rule is absent |
| target replacement | decision is unchanged when target labels are replaced by dummy labels | clean; no target import used |
| gate verdict | eliminate `CODERIVATIVE_TRACE` before targets | **fail / blocked** |

The eliminator fails for a narrow reason. `D_A U` is well typed and remains the
strongest exterior candidate. But the source interface does not say that the
selected IG witness must have positive exterior degree, so the trace/coderivative
class cannot be rejected without adding a new source axiom or using downstream
target behavior.

## 6. Surviving Class State

The source-only survivor set remains unchanged:

| class | status after this gate | why it survives |
|---|---|---|
| `EXT_DERIVATIVE` / `D_A U` | survives as strongest positive candidate | local, first order, gauge-covariant, exterior candidate |
| `CODERIVATIVE_TRACE` | survives and blocks this gate | no positive exterior-degree or trace-exclusion source rule |
| `SYMMETRIC_DERIVATIVE` | survives from previous matrix | no antisymmetric exterior-finality lemma |
| `PROJECTED_DERIVATIVE` | survives from previous matrix | no projector policy or projection-loss theorem |
| `LOWER_ORDER_DRESSED_EXTERIOR` | survives from previous matrix | no lower-order rigidity theorem or source policy |

No rival is eliminated by this cycle 3 gate. The surviving class count remains
`5`.

## 7. Meaning For Branch 3

Allowed current claim:

```text
The repo hosts a coherent exterior Branch 3 candidate,
K_IG(U; A) = D_A U, and has isolated the first non-exterior rival that must be
eliminated before `D_A U` can become source-forced.
```

Forbidden current claims:

```text
Current sources force K_IG = D_A U.
Current sources eliminate CODERIVATIVE_TRACE.
Branch 3 is admitted.
SourceForcedSIGDynPacket_3 is emitted.
Target performance selects the exterior class.
```

Consequences:

```text
K_IG selected: false
D_A U source-forced: false
Q_IG selected: false
Z_U selected: false
V_src selected: false
S_cross_src selected: false
exact J_IG derived: false
theta_eff emitted as source-forced current: false
Branch 3 proof restart allowed: false
```

No claim-status consistency workflow is triggered because no repo claim was
promoted, demoted, or closed.

## 8. First Exact Missing Object

The first exact missing object is now sharper than the cycle 2 bundle name:

```text
PositiveExteriorDegreeRuleForK_IG_V1
```

Required content:

```text
PositiveExteriorDegreeRuleForK_IG_V1:
  SourceWitnesses
  + AdmissibleIGWitnessPreorder
  + CodomainPolicy
  + ParentMomentumDegreePolicy
  + BoundaryClass
  + TargetReplacementGuard
    -> selected_codomain = Omega^2(Y, ad P)
       and selected_parent_momentum_degree = Omega^2(Y, ad P)
       before targets.
```

Only after that rule exists can the trace-exclusion lemma become a short
codomain argument:

```text
D_A^* U or trace_g(nabla_A U) has 0-form / trace-sector codomain,
therefore it cannot be the selected K_IG witness.
```

If no source-positive exterior-degree rule can be supplied, then
`CODERIVATIVE_TRACE` remains a genuine surviving rival and the exterior
singleton route remains blocked.

## 9. Terrain Classification And Guard

Suspected terrain:

```text
primary: local gauge-covariant operator selection
guard: source-provenance verifier
secondary: codomain and parent-degree finality
secondary: contraction/trace exclusion
```

Forbidden shortcut:

```text
Do not eliminate D_A^* U because the exterior parent action is cleaner, because
D_A U is more useful for theta_eff, or because downstream exact-GR or cosmology
targets prefer the exterior class.
```

First invariant to test next:

```text
target-replacement-invariant source forcing of selected exterior 2-form degree.
```

Kill condition:

```text
If the source interface permits a selected 0-form or trace-sector K_IG witness,
CoderivativeTraceEliminatorForK_IG_V1 fails and Branch 3 remains
source-underdefined.
```

## 10. JSON Summary And Checks

```json
{
  "artifact_id": "CoderivativeTraceEliminatorForK_IG_0701_C3_V1_Result",
  "run_id": "hourly-20260626-0701",
  "cycle": 3,
  "lane": 3,
  "artifact_path": "explorations/hourly-20260626-0701-cycle3-kig-coderivative-trace-eliminator.md",
  "verdict_class": "blocked_coderivative_trace_survives_no_positive_exterior_degree_rule",
  "coderivative_trace_eliminator_admitted": false,
  "positive_exterior_degree_rule_present": false,
  "coderivative_trace_eliminated": false,
  "surviving_class_count": 5,
  "surviving_classes": [
    "EXT_DERIVATIVE",
    "CODERIVATIVE_TRACE",
    "SYMMETRIC_DERIVATIVE",
    "PROJECTED_DERIVATIVE",
    "LOWER_ORDER_DRESSED_EXTERIOR"
  ],
  "d_a_u_admissible": true,
  "d_a_u_source_forced": false,
  "branch3_admitted": false,
  "target_import_used": false,
  "claim_status_consistency_triggered": false,
  "first_missing_rule": "PositiveExteriorDegreeRuleForK_IG_V1",
  "conditional_trace_exclusion_available": true,
  "conditional_trace_exclusion_antecedent_source_derived": false,
  "target_replacement_guard_result": "clean_no_target_inputs_read_but_not_sufficient_for_elimination",
  "next_frontier_object": "PositiveExteriorDegreeRuleForK_IG_V1"
}
```

Sources read and checks performed:

- `RESEARCH-POSTURE.md`
- `process/runbooks/five-lane-frontier-run.md`
- `explorations/hourly-20260626-0701-cycle2-kig-nonexterior-rival-eliminator-bundle.md`
- `explorations/hourly-20260626-0701-cycle1-kig-exterior-singleton-survival-certificate.md`
- `explorations/hourly-20260626-0604-cycle2-kig-rival-class-eliminator-preorder.md`
- `explorations/hourly-20260626-0604-cycle1-kig-exterior-codomain-finality-packet.md`
- `explorations/hourly-20260626-0604-cycle3-source-admission-state-machine.md`
- `explorations/hourly-20260626-0604-cycle3-next-frontier-sequencing-matrix.md`
- `explorations/hourly-20260626-0502-cycle2-kig-codomain-selector-gate.md`
- `explorations/hourly-20260626-0502-cycle1-branch3-kig-source-selection-test.md`
- `explorations/hourly-20260625-0103-cycle2-k-ig-source-axiom-eliminator-search.md`
- `explorations/hourly-cycle3-k-ig-codomain-finality-certificate-2026-06-25.md`
- `explorations/hourly-cycle2-k-ig-witness-selection-test-2026-06-25.md`
- `tests/hourly_20260626_0701_cycle2_transition_gates_audit.py`
- `tests/hourly_20260626_0701_cycle1_source_intake_audit.py`
- Repo-local `rg` searches for `CoderivativeTraceEliminatorForK_IG`,
  `PositiveExteriorDegreeRuleForK_IG`, `TraceContractionExclusionLemmaForK_IG`,
  `CODERIVATIVE_TRACE`, `ExteriorCodomainFinalityAxiomForK_IG`,
  `SourceForcedCodomainSelectorForK_IG`, positive exterior degree,
  trace/coderivative codomains, target replacement, `D_A U`, and Branch 3
  admission flags.
