---
title: "Effect-Typed Witness Transport Bidirectional Crosswalk"
status: exploration
doc_type: cross_repo_bridge
updated_at: "2026-06-25"
source_repos:
  - "../time-as-finality"
  - "../temporal-issuance"
  - "../gu-formalization"
verdict: "USE_AS_BRIDGE_DISCIPLINE_NOT_CLAIM_PROMOTION"
---

# Effect-Typed Witness Transport Bidirectional Crosswalk

## Purpose

Preserve the bidirectional connection between GU, Time as Finality, and
Temporal Issuance after the hourly GU run isolated five frontier blockers.

This note does not promote a GU physics claim. It proposes a cross-repo audit
object that keeps source construction, observer projection, finality, and loss
separate while giving Time as Finality and Temporal Issuance a hard
geometry-facing stress test.

## Main Verdict

The missing bridge should not be a generic witness object. It should be an
effect-typed transport contract:

```text
EffectTypedWitnessTransport =
(
  GU_stage,
  SourceExtension,
  Projection,
  Capability,
  RecordFinality,
  LossKernel,
  AbsorberSet,
  InvariantTransport,
  ClosureGate
)
```

The minimal effect tags are imported from the Temporal Issuance source/shadow
contract:

```text
Issue[S]      source-side construction or admissibility extension
Project[O]    observer-visible projection or access/readout map
Finalize[R]   record, certificate, or claim-state finality transition
Lose[K]       quotient, projection, truncation, or forgotten-structure loss
```

The rule is conservative:

```text
Project[O] + Finalize[R] + Lose[K] does not imply Issue[S].
```

## How Time as Finality and Temporal Issuance Help GU

They prevent five different GU blockers from being treated as one kind of
missing thing.

| GU blocker | effect-typed reading | immediate benefit |
|---|---|---|
| `K_IG_selector` | primarily `Issue[S]` | Forces the selector to be source-forced, not chosen because it saves theta/FLRW. |
| `d_RS,-1` | `Lose[K]` plus source-side quotient discipline | Makes gauge/BRST quotienting explicit before any effective rank or generation-count claim. |
| `ActualDGU01OperatorCertificate` | `Finalize[R]` for an actual typed operator, with source/operator data declared | Blocks use of typed-spine surrogates as if they were the GU 0/1 operator. |
| `SourceProjectorPFinBWithLocalModeRecords` | `Project[O] + Lose[K] + Finalize[R]` | Separates finite-mode readout, quotient loss, and record certification before CHSH/QFT claims. |
| `LoopStateTransitionLedger_v1` | `Finalize[R]` plus transition-state audit | Distinguishes convergence, repeated blocker discovery, false negatives, and stale status. |

## How GU Helps Time as Finality and Temporal Issuance

GU supplies a geometry-heavy hostile testbed. A TaF/TI abstraction that works
only for toy records or governance ledgers has not yet earned much. GU asks
whether it can survive:

| TaF/TI abstraction | GU-native stress test | what GU can return |
|---|---|---|
| `SourceExtension` | `K_IG_selector` and source-forced field-degree rules | A hard case where source construction must not be confused with target-saving choice. |
| `Projection` | `Phi_obs`, `P_fin^b`, finite source modes, and smooth shadow maps | A precise test of whether observer-visible data preserves the declared capability. |
| `Capability` | RS physical quotient, CHSH admissible measurements, exact operator use | A demand that capability be task-native, not "recover the hidden label." |
| `RecordFinality` | actual operator certificates, claim-DAG finality, and loop ledgers | A proof-carrying finality model that cannot replace the underlying theorem. |
| `LossKernel` | H-linear quotienting, finite-mode truncation, forgotten gauge data | A nontrivial loss model where forgotten structure changes downstream admissibility. |
| `AbsorberSet` | no-go class boundaries, target smuggling, same-session closure, control-state misuse | Better hostile controls for source/readout and finality claims. |
| `InvariantPreservingTransformation` | VZ order split, RS quotient maps, QFT Gram positivity | A test of whether named invariants actually survive transport. |
| `TypedTransportNetwork` | multi-lane proof paths with path-dependent forgotten structure | A geometry case where path history can matter to admissibility. |

## Cross-Repo Non-Merge Rule

Do not merge claim ledgers.

Allowed transfer:

- GU may use TaF/TI as effect-typing and bridge discipline.
- TaF/TI may use GU as a hard geometry stress test.
- Each repo may cite the other as context, absorber pressure, or fixture source.

Forbidden transfer:

- Do not treat Time as Finality as a GU physics proof.
- Do not treat Temporal Issuance as a GU source theory.
- Do not treat GU geometry as a proof of TaF/TI source issuance.
- Do not upgrade any claim because another repo has adjacent vocabulary.

## Minimal Next Artifact

Build a GU `EffectTypedWitnessTransport` fixture with one row per frontier
blocker:

```text
blocker_id
GU_native_object
effect_tags
source_extension_gate
projection_sufficiency_gate
capability_object
record_finality_state
loss_kernel
absorber_or_fault_class
closure_condition
demotion_condition
```

The first useful result would be a classification, not a proof:

```text
Which blockers are source-construction failures?
Which are projection/readout failures?
Which are finality/certificate failures?
Which are quotient/loss failures?
Which apparent blockers disappear under a native absorber?
```

## Links To Preserve

- GU synthesis: `../hourly-three-cycle-fifteen-hole-synthesis-2026-06-24.md`
- GU observer/finality layer: `observer-finality-layer.md`
- GU live claim DAG: `../live-claim-dag-fault-finality-ledger-2026-06-24.md`
- Time as Finality bridge note: `../../../time-as-finality/explorations/gu-effect-typed-witness-transport-stress-test-2026-06-25.md`
- Temporal Issuance bridge note: `../../../temporal-issuance/explorations/E075-gu-effect-typed-witness-transport-2026-06-25.md`

