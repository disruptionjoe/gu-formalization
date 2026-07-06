---
title: "Boundary Spectral Section Carrier Packet"
date: 2026-07-05
status: active_research
claim_grade: reconstruction_planning
claim_promotion: false
depends_on:
  - CRYPTOECONOMIC-SOURCE-ACTION.md
  - SPEC.md
  - SPECTRAL-SECTION-CARRIER-GOAL-2026-06-30.md
  - SECURITY-BUDGET-CARRIER-PACKET-2026-07-01.md
  - lib/loss_channels.py
  - tests/test_boundary_spectral_section_packet.py
---

# Boundary Spectral Section Carrier Packet

## Purpose

This packet fills the minimum candidate form from
`../../lab/roadmap/closed-internal-source-action-attack-gate-2026-07-01.md`
for one specific carrier attempt:

```text
Can the already-built BV-to-boundary symbol and its APS spectral section make
the security-budget source-action candidate specific enough to select a closed
internal S_IG?
```

It is not a source-action result. It is a bounded falsification and triage
packet for one computed boundary-index route.

## Candidate

`boundary-spectral-section-security-budget`

## Input Data

The candidate proposes to route selection pressure through the boundary
spectral-section carrier built from:

```text
E = (I - Pi_RS) M_D Pi_RS
D_Sigma = E + E^dag
```

It uses the existing security-budget loss-channel surface:

| channel | current role |
|---|---|
| `L_boundary_symbol` | Computed. The BV-to-boundary symbol/Hessian map exists and carries C2 as a Hilbert-Schmidt symbol norm. |
| `L_boundary_index` | Computed. The present APS index route fails because the boundary operator has forced eta zero. |
| `L_target_import` | Computed hard guard against known target imports. |
| `L_acausal_trap` | Computed hard guard against bare-commutator motion and clean decoupling traps. |

## Closedness Claim

No closedness is earned. The boundary-symbol carrier exists at the
symbol/Hessian level, but the current spectral-section/index route does not
produce a nonzero source-side selection. The nonzero boundary spectrum is
paired by the grading, so the APS eta route is forced to zero.

This means the route is not a closed internal `S_IG`. It is a computed boundary
adapter obstruction.

## Variation Space

Allowed:

- Preserve the verified bare commutator anchor.
- Use the existing BV-to-boundary symbol metrics.
- Record the computed APS eta wall honestly.

Not allowed:

- Normalize by `24 / 8`, `chi(K3)`, `ch2 = 24`, or equivalent target-loaded language.
- Treat zero-mode filling as a source action.
- Treat a fixed boundary spectral section as closed internal source-side data.
- Claim closure from the generic boundary-symbol carrier.

## Selection Rule

The proposed rule remains the minimax security-budget interface:

```text
Score(phi) = GrowthValue(phi)
             - ValidationCost(phi)
             - FinalizationCost(phi)
             - WorstCaseAdversarialLoss(phi)
```

This packet asks whether the computed boundary spectral-section route can make
`L_boundary_index(phi)` select. With the current code, it cannot: the symbol
carrier computes, but the APS index loss remains `1.0` because eta is forced
zero and no section connects.

## Failure Condition

The candidate fails if the current boundary spectral-section route has
`eta_D_sigma = 0`, `eta_forced_zero = true`, and `section_connects = false`
while preserving the verified GU anchors.

That condition fires for this packet.

## Guard Evidence

Regression test:

```powershell
python absorbed\gu-source-action\tests\test_boundary_spectral_section_packet.py
```

Expected facts:

- anti-import guard passes;
- anti-trap bare-commutator guard passes;
- boundary-symbol carrier exists at the symbol/Hessian level;
- C2 is carried as a Hilbert-Schmidt symbol norm;
- boundary-index loss remains `1.0` because the present APS route has eta zero;
- the available-loss score still has worst-case loss `1.0` and does not become
  a source action.

## Expected Outcome Label

`boundary_dependency_negative`

Secondary label for the local computation:

`computed_eta_wall`

## Disposition

The boundary spectral-section route is a useful computed obstruction. It
prevents future work from treating the existing `D_Sigma` section as a closed
source-action selector. A stronger future route would need a nonfixed
admissibility datum, source-current law, BV/BRST boundary field, K-class, or
anomaly/flow equation that forces a section rather than choosing one.
