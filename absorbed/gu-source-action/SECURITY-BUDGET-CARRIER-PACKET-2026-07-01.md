---
title: "Security-Budget Carrier Packet"
date: 2026-07-01
status: active_research
claim_grade: reconstruction_planning
claim_promotion: false
depends_on:
  - CRYPTOECONOMIC-SOURCE-ACTION.md
  - SPEC.md
  - DEAD-ENDS.md
  - lib/loss_channels.py
  - lib/security_budget.py
  - tests/test_security_budget_candidate_packet.py
---

# Security-Budget Carrier Packet

## Purpose

This packet fills the minimum candidate form from
`lab/roadmap/closed-internal-source-action-attack-gate-2026-07-01.md` for the first available
security-budget selector.

It is not a source-action result. It is an executable falsification/triage packet for the question:

```text
Can the currently computable security-budget loss channels select a closed internal S_IG candidate?
```

## Candidate

`available-loss-only-security-budget`

## Input Data

The candidate uses only the loss channels that compute today from the existing GU bridge and guard metadata:

| channel | current role |
|---|---|
| `L_boundary_symbol` | Computed. The BV-to-boundary symbol/Hessian map exists and carries C2 as a Hilbert-Schmidt symbol norm. |
| `L_boundary_index` | Computed. The present APS index route fails because the boundary operator has forced eta zero. |
| `L_target_import` | Computed hard guard against known target imports. |
| `L_acausal_trap` | Computed hard guard against bare-commutator motion and clean decoupling traps. |

It deliberately supplies no candidate-specific anomaly polynomial, BV/BRST closure, theta/source-current law,
weak-field coupling, or families-pushforward carrier.

## Closedness Claim

No closedness is earned. This packet is internal in the weak sense that it uses repo-local GU bridge objects and
hard guards, but it does not supply the global GU-native carrier required by `SPEC.md`.

## Variation Space

Allowed:

- Compare candidate source-extension metadata through the currently computable channels.
- Preserve the verified bare commutator anchor.
- Reject known target imports and acausal traps.

Not allowed:

- Normalize by `24 / 8`, `chi(K3)`, `ch2 = 24`, or an equivalent fitted number.
- Solve a carrier from the desired generation count.
- Treat a fixed boundary section, zero-mode filling convention, or generic security-budget vocabulary as a
  source-side carrier.

## Selection Rule

The proposed rule is the existing minimax security-budget interface:

```text
Score(phi) = GrowthValue(phi)
             - ValidationCost(phi)
             - FinalizationCost(phi)
             - WorstCaseAdversarialLoss(phi)
```

Using only currently available generic channels, this rule does not select a unique source action. Two candidates
with equal growth/cost and no candidate-specific carrier tie exactly because the available losses are the same.

## Failure Condition

The candidate is killed or blocked if either condition holds:

1. Any hard guard fires (`target_import_fail` or `acausal_trap_fail`).
2. The computable losses are generic rather than candidate-specific, while one or more source-action carriers
   required by `SPEC.md` remains missing.

Condition 2 fires for this packet.

## Guard Evidence

Regression test:

```powershell
python absorbed\gu-source-action\tests\test_security_budget_candidate_packet.py
```

Expected facts:

- anti-import guard passes;
- anti-trap bare-commutator guard passes;
- boundary-symbol carrier exists at the symbol/Hessian level;
- boundary-index loss remains 1.0 because the present APS route has eta zero;
- missing carrier channels raise named `MissingCarrierError` exceptions;
- a selection using only equal available generic losses ties instead of choosing a winner.

## Missing Carrier Channels

The decisive missing carriers are:

| channel | required carrier |
|---|---|
| `L_anomaly` | anomaly polynomial / Green-Schwarz factorization computed from a candidate `S_IG` |
| `L_RS_BRST` | full BV bicomplex closure loss for the proposed source extension |
| `L_theta_source` | theta/source-current law coupled to the candidate source action |
| `L_weak_field` | weak-field Schwarzschild/GR recovery loss for the candidate source law |
| `L_families_pushforward` | families pushforward over `GL(4,R)/O(3,1)` or a controlled finite surrogate |

These are not optional scoring refinements. They are the carriers that would make the security-budget lens
candidate-specific rather than generic.

## Expected Outcome Label

`missing_carrier_blocked`

Secondary label if someone tries to select among candidates with only equal generic losses:

`underdetermination_fail`

## Disposition

The available-loss-only security-budget selector is useful scaffolding, but it is not a closed internal source
action candidate. Future work must provide at least one candidate-specific GU-native carrier before the minimax
rule can earn selection pressure.

The next meaningful packet should name exactly one such carrier attempt:

- anomaly/Green-Schwarz carrier;
- BV/BRST closure carrier;
- theta/source-current carrier;
- weak-field source-current carrier;
- families-pushforward carrier.

If none can be named cleanly, the correct outcome is a source-action feasibility/ownership note rather than
another selector proposal.
