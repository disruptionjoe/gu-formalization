---
title: "Daily Research Portfolio Stewardship"
status: active
doc_type: runbook
scope: repo-local
created: 2026-07-15
portfolio: lab/process/research-portfolio.json
---

# Daily Research Portfolio Stewardship

This is the GU-local daily stewardship extension. CapacityOS still owns scheduling, run identity, concurrency, and the standard Stewardship lifecycle. GU owns its scientific priorities. This runbook lets the daily steward repair coordination drift by reconciling the repo-owned portfolio against real research signals.

It does not authorize new scientific claims, claim-status changes, verdict changes, canon edits, public-posture changes, publication, or cross-repo implementation.

## Stable question

```text
Given what GU learned since the last review, which one meaningful research lane should hourly Progress attack next, and what evidence would make us switch?
```

## Required reads

1. `AGENTS.md`, `GEOMETER-VS-PHYSICS-OBJECTS.md`, `RESEARCH-POSTURE.md`, and `steward/README.md`.
2. `lab/process/research-portfolio.json`.
3. Run plans and receipts from the previous 24 hours under `steward/runs/`.
4. Commits and working-tree state since the previous steward review.
5. The GU mailbox only, plus returned frozen packets already accepted by the receiving workflow.
6. Owner artifacts named by any receipt that reports a falsifier, survivor, dependency change, correction, or publication gate.

Do not rescan the whole repository merely to create activity. Follow references from changed evidence and the active portfolio.

## Signal test before reprioritization

Priority may change only on a valid scientific or dependency signal from this list:

- reproducible falsifier;
- dependency unblocked or blocked;
- genuinely new survivor;
- frozen packet returned by the owning repository;
- official external data release;
- integrity correction that changes the decision surface;
- paper reaching or losing an external-review gate.
- a capacity-backed Drafting Factory request for a specific source-hardening packet.

Difficulty, activity volume, commit count, and ease of closure are not signals. A North-Star lane does not lose priority because a Lean or paper-hardening task is easier.

## Daily procedure

1. Create the standard run plan and complete the recent-run collision check.
2. Classify each new receipt as `no_priority_signal` or one of the valid signals above.
3. Recompute every lane's score using the formula stored in the portfolio. The score is decision support, not an automatic scheduler.
4. Preserve exactly one protected primary lane. Preserve at most one reserve or maintenance lane.
5. Apply hysteresis. Keep the current primary unless a valid signal materially changes readiness, information value, ownership, or falsification status.
6. Update lane state, dependencies, next swing, kill condition, and switch condition where the evidence requires it.
   For every new branch-local recovery no-go, confirm that the non-counting history audit and the registered
   three-swing defense sequence exist in `lab/process/recovery-no-go-defense-register.json`. Do not mark a
   construction class exhausted from the first failed branch.
7. Update the top operational block of `NEXT-STEPS.md` to match the portfolio. Do not rewrite historical blocks.
8. Check the paper-hardening inventory for a new substantive defect, paper-shaped opportunity, Drafting Factory hardening request, or external-eyes threshold. Route every new paper-shaped opportunity to Drafting Factory as a cheap seed before doing additional paper work. Do not select cosmetic polishing as primary work.
9. Record any `joe_signal` in the run receipt. Write one deduplicated JoeOps proposal only when a listed trigger fires.
10. Validate with `python -u process_gates/research_portfolio_contract_audit.py` and the affected navigation gates.
11. Commit and push a coherent stewardship update using explicit-path staging.

## Initial scientific constraints that must remain visible

- GU-002 packages the no-go. W234, W237, W240, W241, and W243 are the closing chain.
- The native order-parameter route is closed for neutral, adjoint, and charged-extremal classes, which are everything GU builds.
- The exotic nonextremal charged corridor is mathematically open but GU-non-native.
- The relevant GU escape is the boundary/firewall route owned by possibility-to-capability.
- The no-go remains conditional on Proposition 1 and the favorable W235 record bit. Preserve both in summaries.
- The deepest open theoretical dependency is the Y14 `F_A` C2 spectral-section/source-action datum plus native normalization. Joe transferred its construction to p2c. Track B prediction extraction is GU's operational North Star, not a claim that this deeper problem is solved.
- The closed-interior `PHYSICAL-C` build is excluded. GU may study consequences under a precisely typed adapter assumption now, at a strict conditional grade. A physical construction claim still requires a frozen p2c return.
- Conditional physical-sector sufficiency is GU-owned and executable now: assume a precisely typed adapter
  interface and test whether the same frozen GU construction yields the physical quotient, positive state space,
  observables, locality, and unitary or state-preserving dynamics without further imports. This does not claim
  that GU built the adapter or that an unconditional physical sector exists.
- Every new recovery no-go gets a repo-history audit followed by at least three broad construction-diverse
  defense swings. Preserve the original branch-local negative result, predeclare the construction space, and
  require any reframe to explain more rather than merely survive.
- W226's `+1.11` is the current two-sigma F1 firing margin. W223's `+0.032` is a superseded single-row central-value diagnostic. The evidence owner is `explorations/W226-harden-de-tripwire-squeeze-data-2026-07-14.md` plus `tests/W226_de_tripwire.py`, not the portfolio constant.
- F1 is a one-sided falsification tripwire, not a positive prediction.
- `bar(b)` and `H59` remain open.

## Packet seam

GU makes the sovereign native-versus-forced determination. Phenomenology may adjudicate data, likelihoods, calibration, competing models, and test timing, but must not issue the GU-native verdict. Possibility-to-capability owns the firewall adapter and capability adjudication.

On intake, reject or return any phenomenology packet that implicitly equates fit quality, parameter freedom, mimicry, or data preference with native-versus-forced status. GU must perform that classification independently.

Cross-repo research content enters only through frozen provenance-bearing packets. Mailbox messages are proposals, not packets or truth.

## Drafting Factory seam

Drafting Factory owns paper seeds, cross-paper prioritization, lane capacity, and drafting. GU owns the research truth and hardening artifacts behind a paper.

When a run identifies a credible paper-shaped opportunity, send a minimal `Status: proposed` seed to the Drafting Factory mailbox immediately. Preserve the exact source grade, revision, evidence pointers, conditions, overlap candidates, and no-external-action posture. Do not wait for candidate-grade hardening, and do not treat the seed as permission to draft.

If the one-writable-repository run boundary prevents a child run from writing the mailbox, put a complete `paper_seed_proposal` block in its receipt. The parent orchestration or next daily steward must route that block before unrelated paper hardening. Do not create a parallel GU paper-priority queue.

Only a Drafting Factory request backed by available production capacity is a GU priority signal. It may cause the daily steward to reweight source hardening, but it is not a command and cannot change proof grade, native-versus-forced status, or the protected scientific objective without the ordinary signal test. GU returns accepted hardening through a frozen source packet.

## Shared-surface ownership

- The daily steward is the only routine writer of `lab/process/research-portfolio.json` and the top operational block of `NEXT-STEPS.md`.
- Hourly Progress writes its owned research artifact, test or proof artifact, and ignored run receipt. It does not edit the portfolio, `NEXT-STEPS.md`, or `CANON.md`.
- `explorations/W227-gap-analysis-to-unconditional-2026-07-14.md` is historical input, not the live steering register.
- `CANON.md` changes only through the claim-status or canon-promotion workflow.

## JoeOps policy

Ordinary progress stays in GU. Send an event-driven, deduplicated proposal only for:

- a major kill, downgrade, or unexpected strengthening;
- a calibration-independent prediction ready to freeze;
- a paper ready for external eyes;
- an outside-expert, paid-data, or external-action need;
- a p2c return that changes the frontier;
- a time-sensitive opportunity;
- one hard blocker surviving three daily reviews;
- an irreconcilable concurrency or ownership conflict.

The proposal must state `Status: proposed`, the exact decision or awareness item, evidence pointers, scientific impact, deadline if real, and the recommended next action. It must preserve conditionalities and must not flatten "native," "forced," "compatible," and "fitted" into one status.

Do not send new paper seeds to JoeOps. Drafting Factory receives and prioritizes them. JoeOps becomes appropriate only when Joe's decision, external eyes, publication authority, or real cross-program coordination is needed.

## No-worthy-change close

If no valid signal occurred, leave the priority order unchanged. Repair only genuine coordination drift, record a compact no-priority-change receipt, and close. A daily rewrite with no evidence change is thrashing, not stewardship.
