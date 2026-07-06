---
title: "Non-Equivariant Compensator Carrier Packet"
date: 2026-07-05
status: active_research
claim_grade: reconstruction_planning
claim_promotion: false
depends_on:
  - CRYPTOECONOMIC-SOURCE-ACTION.md
  - SPEC.md
  - ADAPTER-DISCRIMINATOR-GOAL-2026-06-30.md
  - lib/adapter_discriminator.py
  - lib/loss_channels.py
  - tests/test_non_equivariant_compensator_packet.py
---

# Non-Equivariant Compensator Carrier Packet

## Purpose

This packet fills the minimum candidate form from
`../../lab/roadmap/closed-internal-source-action-attack-gate-2026-07-01.md`
for one specific source-extension attempt:

```text
Can the necessary non-equivariant compensator be priced as a source extension
strongly enough to become a closed internal S_IG candidate?
```

It is not a source-action result. It is a bounded falsification and triage packet
for the compensator-as-source-variable lane.

## Candidate

`non-equivariant-compensator-security-budget`

## Input Data

The candidate proposes to route selection pressure through the non-equivariant
compensator identified by the source-action target. It uses two existing
surfaces:

| surface | current role |
|---|---|
| `lib/adapter_discriminator.py` | Computes whether structured non-metric adapter shapes produce a boundary/index signal while preserving the verified anchors. |
| `L_boundary_symbol` | Computed. The BV-to-boundary symbol/Hessian map exists and carries C2 as a Hilbert-Schmidt symbol norm. |
| `L_boundary_index` | Computed. The present APS index route fails because the boundary operator has forced eta zero. |
| `L_target_import` | Computed hard guard against known target imports. |
| `L_acausal_trap` | Computed hard guard against bare-commutator motion and clean decoupling traps. |
| `L_RS_BRST` | Still the named closure blocker when the compensator must be coupled to the full BV bicomplex. |

## Closedness Claim

No closedness is earned. A non-equivariant compensator is necessary for the
source-action target, but necessity is not selection. The current adapter
discriminator gives a sharper negative:

- ordinary metric controls stay zero;
- the simple structured non-metric probes tested so far stay zero;
- dense arbitrary H-linear movement can move the index, but has no source
  carrier and is only a sanity control.

Thus the compensator lane has not yet supplied a GU-native source carrier,
BV/BRST closure, boundary holonomy, or K-class that would turn it into a closed
internal source-action candidate.

## Variation Space

Allowed:

- Preserve the verified bare commutator anchor.
- Reject known target imports and acausal traps.
- Ask whether a structured non-equivariant candidate can produce a boundary or
  index signal.
- Ask whether that signal has a source carrier instead of being arbitrary
  non-algebra movement.

Not allowed:

- Normalize by `24 / 8`, `chi(K3)`, `ch2 = 24`, or equivalent target-loaded language.
- Treat arbitrary H-linear noise as physical source-action evidence.
- Treat a hand-imposed projector or clean decoupling as a source action.
- Claim the compensator is closed without full BV bicomplex closure.
- Claim closure from the generic boundary-symbol carrier.

## Selection Rule

The proposed rule remains the minimax security-budget interface:

```text
Score(phi) = GrowthValue(phi)
             - ValidationCost(phi)
             - FinalizationCost(phi)
             - WorstCaseAdversarialLoss(phi)
```

This packet asks whether the non-equivariant compensator can supply the
candidate-specific `phi` being scored. With the current code, it cannot: the
adapter discriminator finds no live structured candidate, and the full
BV/BRST closure loss remains a named missing carrier.

## Failure Condition

The candidate is blocked if the tested structured non-equivariant adapter
shapes either remain zero at the boundary/index discriminator or produce a
signal without a source carrier.

That condition fires for this packet.

## Guard Evidence

Regression test:

```powershell
python absorbed\gu-source-action\tests\test_non_equivariant_compensator_packet.py
```

Expected facts:

- anti-import guard passes;
- anti-trap bare-commutator guard passes;
- boundary-symbol carrier exists at the symbol/Hessian level;
- the adapter-discriminator summary does not report a live structured source
  candidate;
- any arbitrary nonzero signal is classified as arbitrary and carrierless;
- `L_RS_BRST` remains the named blocker for coupling the compensator to the
  full BV bicomplex.

## Expected Outcome Label

`missing_carrier_blocked`

Secondary label for the simple tested adapter shapes:

`structured_but_zero`

## Disposition

The non-equivariant compensator remains a legitimate source-action workstream
because `SPEC.md` requires it, but it is not yet a closed internal source-action
candidate. Future work must either provide a candidate-specific BV/BRST,
holonomy, K-theory, or source-current carrier for the compensator, or record a
negative result showing that the compensator is only a necessary consistency
ingredient and not a selector.
