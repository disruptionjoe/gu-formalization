---
title: "RS BRST Carrier Packet"
date: 2026-07-05
status: active_research
claim_grade: reconstruction_planning
claim_promotion: false
depends_on:
  - CRYPTOECONOMIC-SOURCE-ACTION.md
  - SPEC.md
  - SECURITY-BUDGET-CARRIER-PACKET-2026-07-01.md
  - lib/loss_channels.py
  - tests/test_rs_brst_packet.py
---

# RS/BRST Carrier Packet

## Purpose

This packet fills the minimum candidate form from
`../../lab/roadmap/closed-internal-source-action-attack-gate-2026-07-01.md`
for one specific carrier attempt:

```text
Can a GU-internal full BV bicomplex / RS-BRST closure make the
security-budget source-action candidate specific enough to select a closed
internal S_IG?
```

It is not a source-action result. It is a bounded falsification and triage packet
for one missing carrier channel.

## Candidate

`rs-brst-security-budget`

## Input Data

The candidate proposes to route selection pressure through the full BV bicomplex
and RS/BRST closure condition for a proposed source extension. It uses the
existing security-budget loss-channel surface:

| channel | current role |
|---|---|
| `L_boundary_symbol` | Computed. The BV-to-boundary symbol/Hessian map exists and carries C2 as a Hilbert-Schmidt symbol norm. |
| `L_boundary_index` | Computed. The present APS index route fails because the boundary operator has forced eta zero. |
| `L_target_import` | Computed hard guard against known target imports. |
| `L_acausal_trap` | Computed hard guard against bare-commutator motion and clean decoupling traps. |
| `L_RS_BRST` | Proposed decisive carrier, but currently missing. |

## Closedness Claim

No closedness is earned. An RS/BRST carrier could become an internal
source-action selector only if the full BV bicomplex closure loss is computed
from a candidate `S_IG`, not inferred from the existence of BRST vocabulary, a
hand-imposed projector, or a clean decoupled subspace. The current repository
state does not yet expose that carrier as a computable GU-native object.

## Variation Space

Allowed:

- Preserve the verified bare commutator anchor.
- Reject known target imports and acausal traps.
- Ask whether a candidate-specific full BV bicomplex / RS-BRST closure loss
  exists.

Not allowed:

- Normalize by `24 / 8`, `chi(K3)`, `ch2 = 24`, or equivalent target-loaded language.
- Treat nilpotency or closure as meaningful when it is vacuous or degenerate.
- Treat clean RS-sector decoupling as a win; that reinstates the acausal trap.
- Substitute a hand-imposed projector for a Noether-forced source action.
- Claim closure from the generic boundary-symbol carrier.

## Selection Rule

The proposed rule remains the minimax security-budget interface:

```text
Score(phi) = GrowthValue(phi)
             - ValidationCost(phi)
             - FinalizationCost(phi)
             - WorstCaseAdversarialLoss(phi)
```

This packet asks whether `L_RS_BRST(phi)` can become candidate-specific. With
the current code, it cannot: the channel raises a named `MissingCarrierError`.

## Failure Condition

The candidate is blocked if `L_RS_BRST` lacks a computable GU-native carrier
coupling full BV bicomplex closure and the proposed non-equivariant compensator
to the candidate source action.

That condition fires for this packet.

## Guard Evidence

Regression test:

```powershell
python absorbed\gu-source-action\tests\test_rs_brst_packet.py
```

Expected facts:

- anti-import guard passes;
- anti-trap bare-commutator guard passes;
- boundary-symbol carrier exists at the symbol/Hessian level;
- boundary-index loss remains 1.0 because the present APS route has eta zero;
- `L_RS_BRST` raises a named `MissingCarrierError` with the required carrier
  recorded as full BV bicomplex closure for the proposed source extension.

## Expected Outcome Label

`missing_carrier_blocked`

Secondary label if someone tries to score it anyway with only generic available
losses:

`underdetermination_fail`

## Disposition

The RS/BRST route is a legitimate next carrier target, but it is not yet a
closed internal source-action candidate. Future work must either build the full
BV bicomplex closure loss as a computable object coupled to `S_IG`, or record a
negative result explaining why RS/BRST consistency remains only a downstream
constraint rather than a source-side selector.
