---
title: "Theta Source-Current Carrier Packet"
date: 2026-07-05
status: active_research
claim_grade: reconstruction_planning
claim_promotion: false
depends_on:
  - CRYPTOECONOMIC-SOURCE-ACTION.md
  - SPEC.md
  - SECURITY-BUDGET-CARRIER-PACKET-2026-07-01.md
  - lib/loss_channels.py
  - tests/test_theta_source_current_packet.py
---

# Theta Source-Current Carrier Packet

## Purpose

This packet fills the minimum candidate form from
`../lab/roadmap/closed-internal-source-action-attack-gate-2026-07-01.md` for one
specific carrier attempt:

```text
Can a GU-internal theta/source-current law make the security-budget source-action
candidate specific enough to select a closed internal S_IG?
```

It is not a source-action result. It is a bounded falsification and triage packet
for one missing carrier channel.

## Candidate

`theta-source-current-security-budget`

## Input Data

The candidate proposes to route selection pressure through a theta/source-current
law coupled to the candidate source action. It uses the existing security-budget
loss-channel surface:

| channel | current role |
|---|---|
| `L_boundary_symbol` | Computed. The BV-to-boundary symbol/Hessian map exists and carries C2 as a Hilbert-Schmidt symbol norm. |
| `L_boundary_index` | Computed. The present APS index route fails because the boundary operator has forced eta zero. |
| `L_target_import` | Computed hard guard against known target imports. |
| `L_acausal_trap` | Computed hard guard against bare-commutator motion and clean decoupling traps. |
| `L_theta_source` | Proposed decisive carrier, but currently missing. |

## Closedness Claim

No closedness is earned. A theta/source-current law could become an internal
carrier only if it is computed from a candidate `S_IG` rather than asserted as a
source-current analogy. The current repository state does not yet expose that
law as a computable GU-native object.

## Variation Space

Allowed:

- Preserve the verified bare commutator anchor.
- Reject known target imports and acausal traps.
- Ask whether a candidate-specific theta/source-current law exists.

Not allowed:

- Normalize by `24 / 8`, `chi(K3)`, `ch2 = 24`, or equivalent target-loaded language.
- Treat theta divergence-free status as a source action by itself.
- Substitute observer-finality or analogy for a GU-native source-current computation.
- Claim closure from the generic boundary-symbol carrier.

## Selection Rule

The proposed rule remains the minimax security-budget interface:

```text
Score(phi) = GrowthValue(phi)
             - ValidationCost(phi)
             - FinalizationCost(phi)
             - WorstCaseAdversarialLoss(phi)
```

This packet asks whether `L_theta_source(phi)` can become candidate-specific.
With the current code, it cannot: the channel raises a named `MissingCarrierError`.

## Failure Condition

The candidate is blocked if `L_theta_source` lacks a computable GU-native carrier
coupling the theta/source-current law to the candidate source action.

That condition fires for this packet.

## Guard Evidence

Regression test:

```powershell
python absorbed\gu-source-action\tests\test_theta_source_current_packet.py
```

Expected facts:

- anti-import guard passes;
- anti-trap bare-commutator guard passes;
- boundary-symbol carrier exists at the symbol/Hessian level;
- boundary-index loss remains 1.0 because the present APS route has eta zero;
- `L_theta_source` raises a named `MissingCarrierError` with the required carrier
  recorded as the theta/source-current law coupled to the candidate source action.

## Expected Outcome Label

`missing_carrier_blocked`

Secondary label if someone tries to score it anyway with only generic available
losses:

`underdetermination_fail`

## Disposition

The theta/source-current route is a legitimate next carrier target, but it is not
yet a closed internal source-action candidate. Future work must either build the
theta/source-current law as a computable object coupled to `S_IG`, or record a
negative result explaining why theta remains only a downstream condition rather
than a source-side selector.
