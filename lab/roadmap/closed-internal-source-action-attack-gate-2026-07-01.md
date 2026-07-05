---
title: "Closed Internal Source Action Attack Gate"
status: active_research
doc_type: roadmap_gate
created: 2026-07-01
governance_role: contributor_orientation
claim_grade: reconstruction_planning
constitutional: false
related_primary_question: firewall-boundary-hypothesis
---

# Closed Internal Source Action Attack Gate

## Purpose

This gate turns falsification criterion 1 of the Firewall-Boundary Hypothesis into
a bounded construction attack:

> Can a completely closed GU-internal source action be constructed without target
> import, acausal decoupling, or an unearned boundary adapter?

This document is not a result. It changes no canon verdict, claim status, or public
posture. Its job is to prevent the next Progress run from confusing an attractive
selector with a closed completion.

## Attack target

Canonical hypothesis: `canon/firewall-boundary-hypothesis.md`.

Current frontier map:
`lab/roadmap/current-frontier-firewall-boundary-attack-map-2026-07-01.md`.

Construction sandbox:
`absorbed/gu-source-action/`.

The attack tries to kill the weak firewall form by producing a closed internal
`S_IG` candidate. If the candidate needs a boundary spectral section, a
BV-to-boundary-Dirac carrier, an external index, or a target-loaded normalization
to select the matter count, then it is not a closed counterexample.

## Minimum candidate packet

A closed-internal candidate must state all of the following before any scoring,
selection, or rhetorical fit is considered:

| field | required content |
|---|---|
| candidate name | Short stable name for the proposed `S_IG` or selector. |
| input data | Exact GU-native objects used: representation, operator, projector, current, BV complex, or loss channel. |
| closedness claim | Why the candidate is internal rather than a boundary adapter or imported source. |
| variation space | What is varied, what is fixed, and what is forbidden to be solved from the target. |
| selection rule | The rule that picks a unique source extension or multiplicity. |
| failure condition | One computation or logical check that would kill the candidate. |
| guard evidence | Anti-import, anti-trap, anti-vacuous, and anti-fixed-solve checks. |

If a candidate cannot fill this packet, it is not yet a candidate. It is only a
design idea.

## Hard guards

These guards are inherited from `absorbed/gu-source-action/Agents Start Here.md`,
`SPEC.md`, `DEAD-ENDS.md`, and the current loss-channel code.

| guard | fail condition | existing hook |
|---|---|---|
| Anti-import | Uses `24 / 8 = 3`, `chi(K3) = 24`, `ch2 = 24`, assumed K3, flat `Ahat = 3`, or equivalent target-normalization language. | `absorbed/gu-source-action/lib/loss_channels.py::l_target_import` |
| Anti-trap | Drives the bare `||[Pi_RS, M_D]||` away from the verified anchor or to zero; uses clean decoupling or trivial block subtraction. | `absorbed/gu-source-action/lib/loss_channels.py::l_acausal_trap` |
| Anti-vacuous | Master equation, nilpotency, or closure holds only because the complex is degenerate or the candidate has removed the real obstruction. | needs candidate-specific test |
| Anti-fixed-solve | Carrier is solved from the desired generation count or fitted after seeing the target. | candidate packet plus target-import review |
| Boundary-removal | Candidate secretly relies on a boundary spectral section, BV-to-boundary-Dirac map, families pushforward, or external index while claiming to be closed. | missing-carrier review plus candidate packet |
| Source-action bar | Candidate does not satisfy the `SPEC.md` target: BV master equation, Noether-forced constraint, non-equivariant compensator, full BV bicomplex, and global objects where required. | `SPEC.md` checklist |

## Closedness decision table

| outcome label | meaning | disposition |
|---|---|---|
| `closed_counterexample_candidate` | A candidate uses only GU-internal data, passes hard guards, and uniquely selects without target import or boundary dependency. | Pause before any verdict change; run claim-status workflow and Joe review. |
| `boundary_dependency_negative` | The candidate cannot compute a required loss or selection without a boundary carrier, spectral section, families pushforward, or external index. | Record as a negative result for the closed-completion attack. |
| `target_import_fail` | The candidate imports the desired generation count or a K3/24 surrogate. | Kill and cite the anti-import guard. |
| `acausal_trap_fail` | The candidate wins by decoupling the RS sector or moving the bare commutator anchor. | Kill and cite the anti-trap guard. |
| `underdetermination_fail` | The candidate leaves several equally GU-native selections live or ties under minimax scoring. | Record as under-determination, not a closure. |
| `missing_carrier_blocked` | The candidate is meaningful but the repo lacks the carrier needed to compute the decisive channel. | Record the missing carrier and route the next work to that object. |

## Immediate executable route

The closest existing executable surface is the security-budget scaffold:

- `absorbed/gu-source-action/lib/security_budget.py`
- `absorbed/gu-source-action/lib/loss_channels.py`
- `absorbed/gu-source-action/tests/test_security_budget.py`
- `absorbed/gu-source-action/tests/test_loss_channels.py`

Use it conservatively:

1. Encode the proposed extension as a `SourceCandidate`.
2. Run the computable guards first: target import, acausal trap, boundary symbol,
   and boundary index.
3. Treat every `MissingCarrierError` as a named research object, not as permission
   to substitute prose.
4. Only use `CandidateScore` after the hard guards pass.
5. Treat a tie as `underdetermination_fail`.

## Candidate template

```text
Candidate:
Input data:
Closedness claim:
Variation space:
Selection rule:
Known forbidden imports checked:
Bare commutator anchor:
Missing carrier channels:
Failure condition:
Expected outcome label:
```

## Stop conditions

Stop and record rather than continue if:

- a candidate requires canon or claim-status movement;
- the only route to a number uses a forbidden import;
- the candidate needs a new cross-repo action;
- the candidate relies on a boundary object while claiming closure;
- the computation produces diffs outside the selected objective;
- the candidate's strongest support is aesthetic fit or analogy.

## Executed Packets

- `absorbed/gu-source-action/SECURITY-BUDGET-CARRIER-PACKET-2026-07-01.md`:
  available-loss-only scoring is missing-carrier blocked and does not select a
  source action.
- `absorbed/gu-source-action/THETA-SOURCE-CURRENT-CARRIER-PACKET-2026-07-05.md`:
  the theta/source-current route is missing-carrier blocked on `L_theta_source`;
  no closedness, verdict, or claim-status movement is earned.
- `absorbed/gu-source-action/WEAK-FIELD-SOURCE-CURRENT-CARRIER-PACKET-2026-07-05.md`:
  the weak-field/source-current route is missing-carrier blocked on
  `L_weak_field`; no closedness, verdict, or claim-status movement is earned.
- `absorbed/gu-source-action/ANOMALY-GREEN-SCHWARZ-CARRIER-PACKET-2026-07-05.md`:
  the anomaly/Green-Schwarz route is missing-carrier blocked on `L_anomaly`; no
  closedness, verdict, or claim-status movement is earned.
- `absorbed/gu-source-action/RS-BRST-CARRIER-PACKET-2026-07-05.md`:
  the RS/BRST route is missing-carrier blocked on `L_RS_BRST`; no closedness,
  verdict, or claim-status movement is earned.

## Next concrete run

Pick one proposed `S_IG` or security-budget source extension and fill the minimum
candidate packet. If it survives the packet, add a small executable test under
`absorbed/gu-source-action/tests/` that proves at least one guard passes or fails.

The valuable result is not "the firewall survives." The valuable result is a
clean classification of one closed-completion attempt.
