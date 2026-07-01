---
title: "Cryptoeconomic Security-Budget Source Action"
date: 2026-06-27
status: candidate_steelman
claim_grade: speculative
depends_on:
  - SPEC.md
  - DEAD-ENDS.md
  - ../temporal-issuance/absorbers/crypto-economic-security.md
  - ../gu-formalization/explorations/time-as-finality-crosswalk/ti-as-gu-source-action-v2-wolfram-signed-readout-steelman-2026-06-27.md
optional_executable:
  - lib/security_budget.py
  - lib/loss_channels.py
  - tests/test_security_budget.py
  - tests/test_loss_channels.py
---

# Cryptoeconomic Security-Budget Source Action

## One-Sentence Hypothesis

The missing GU source action may be an adversarial security-budget functional: it selects an
admissible geometric extension only when the extension increases source structure while paying
the cost required to make it final against every allowed mathematical fork.

This is a steelman, not a result.

## Why This Belongs In This Repo

The parent `gu-formalization` campaign showed that bulk algebraic selectors do not pick the
shiab and that the remaining obstruction is global. Cryptoeconomics suggests the right kind of
global object: not a local selector, but a rule that prices finality under adversarial forks.

In a blockchain, finality is not just "a record exists." A record becomes final only when
reversing it is too expensive under the adversary model. In GU, the analog of an attack is a
mathematically allowed rival completion:

- a different residual shiab-family member;
- a different boundary spectral section;
- a different RS/BRST quotient;
- a different theta/source-current coupling;
- a different index regularization;
- a target-imported normalization such as `24 / 8 = 3`.

So the cryptoeconomic reading is:

```text
source action = rule that prices and finalizes admissible geometric extensions
```

## Candidate Functional

Let `phi` be a candidate source extension. For example, `phi` might include a shiab-family
coordinate, a boundary spectral section, a source-current law, or a BV-to-boundary-Dirac map.

Define a security-budget score:

```text
Score(phi)
  = GrowthValue(phi)
  - ValidationCost(phi)
  - FinalizationCost(phi)
  - WorstCaseAdversarialLoss(phi)
```

where:

```text
WorstCaseAdversarialLoss(phi)
  = max(
      L_anomaly(phi),
      L_RS_BRST(phi),
      L_boundary_index(phi),
      L_theta_source(phi),
      L_weak_field(phi),
      L_target_import(phi),
      L_acausal_trap(phi)
    )
```

Then the candidate source-action selection rule is:

```text
phi* = argmax_phi Score(phi)
```

subject to hard guards:

```text
master_equation_ok(phi)
noether_forces_constraint(phi)
non_equivariant_compensator_available(phi)
full_BV_bicomplex_nonvacuous(phi)
anti_trap_bare_commutator_preserved(phi)
anti_import(phi)
```

This is a minimax security problem, not a goodness-of-fit problem.

## GU Translation

| Cryptoeconomic object | GU source-action analog |
| --- | --- |
| transaction / block candidate | source extension `phi` |
| state transition validity | BV master equation and Noether identity |
| block reward / issuance | budget for finalizing new geometric structure |
| attack cost | penalty for rival completions and consistency failures |
| fork-choice rule | selection among shiab, boundary, theta, and BRST completions |
| accountable slashing | explicit failure modes recorded in `DEAD-ENDS.md` |
| security budget | global source-action functional |

## Why This Could Be The Right Shape

It explains three otherwise awkward facts.

1. Bulk selectors fail because they are local validity checks. They do not price global fork
   resistance.
2. Boundary spectral sections nearly help because they are a genuine finalization surface, but
   they do not select without a carrier and adversary model.
3. One missing object gates multiple problems because the same security budget would decide
   which extensions are final across shiab selection, index regularization, RS/BRST closure, and
   theta/source-current accounting.

## First Actionable Workflow

### Step 1: Freeze The Candidate Set

Start with a finite toy candidate set:

```text
Phi_0 = residual 4-real-dimensional H-linear shiab family basis
```

Do not use the target answer. Do not normalize by `24 / 8`. Do not assume K3.

### Step 2: Define Loss Channels

For each candidate `phi`, compute or honestly stub:

```text
L_anomaly(phi)
L_RS_BRST(phi)
L_boundary_index(phi)
L_theta_source(phi)
L_weak_field(phi)
L_target_import(phi)
L_acausal_trap(phi)
```

Every stub must say what exact parent-repo object would compute it.

The current executable boundary between real channels and missing carriers is
`lib/loss_channels.py`: channels either compute from `lib/gu_bridge.py` or raise a named
`MissingCarrierError`.

### Step 3: Run A Minimax Selector

Use `lib/security_budget.py`:

```python
from lib.security_budget import CandidateScore, select_security_budget_winner

winner = select_security_budget_winner([...])
```

This only tests whether a proposed scoring surface actually selects. It does not prove the
scoring surface is GU-native.

### Step 4: Attack The Result

Kill the candidate if:

- all candidates tie;
- the canon shiab wins only because its coordinates were target-imported;
- the score reduces to ordinary observer finality, Nakamoto finality, BFT, or Landauer cost;
- the score has no GU-native carrier;
- the winning extension violates the anti-trap guard;
- the winning extension contradicts `SPEC.md`.

## What Would Count As Progress

A real positive result would look like:

```text
There exists a GU-native loss channel, computable from parent-repo objects, whose
minimax security-budget rule selects a unique non-acausal source extension without
target import.
```

Even a negative result is useful:

```text
Every security-budget score either ties, imports the target, reduces to known
cryptoeconomic finality, or lacks a GU-native carrier.
```

## Current Verdict

This is the most promising nonlocal design lens for the source action, but it is still only a
design lens. The missing physics remains the same: a real BV source action, a BV-to-boundary-Dirac
map, and a GU-native global carrier for the score.
