---
title: "Lane A steering refresh: LANE-STATE was ten days stale while its own gate passed"
status: active_research
doc_type: stewardship_record
created: 2026-08-13
brief_version: "1.3"
target_claim: NONE-NOT-A-KILL
lane: "A"
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Lane A steering refresh

Second Lane A run of 2026-08-13, after the mailbox drain. Target: the
steering surfaces Lane A reconciles.

## The finding, and it is a gate-design defect rather than neglect

`LANE-STATE.yaml` carried `updated_at: 2026-08-03` and a `bottom_line`
naming the B5 packet and the `pw2fr` branch as the live front. Between
that timestamp and this run, **478 commits landed** and the campaign
moved to the K77 operator/observation program at ledger **v0.236**.

**Its freshness gate reported PASS throughout.**

The reason is structural, not lazy. The gate compares a lane's
`evaluated_at` against *the newest commit of the evidence that lane
cites*. Lane 1 cited a 2026-07-29 audit run-plan and a 2026-07-30
exploration; neither changed; lag was therefore ~0 and the check passed.

**A surface that stops pointing at current work is fresh by
construction.** Self-referential freshness is not freshness.

## What this run changed

1. **`LANE-STATE.yaml` narrative fields refreshed** to verified current
   truth: the live front, the 478-commit gap, ledger v0.236 with 82/82
   mapped and the headline unmoved by design, B5 still blocked but no
   longer the front, and the mailbox drain result. `decision_default`
   retargeted while keeping P-H29 unchanged.
2. **The gate extended with an ABSOLUTE currency check**:
   `LANE-STATE`'s own `updated_at` against the repository's newest
   commit, at the same 7-day tolerance the portfolio check already uses.
   It is fail-closed like its siblings, and it currently reads `-0.3d`.

## The extension caught its author within a minute

After the narrative refresh the audit went RED — not on the new check,
but on the pre-existing lane-1 one, because the evidence pointer had been
updated to the current ledger while `evaluated_at` had not. That is the
gate doing exactly its job on the person who had just extended it.
Recorded rather than quietly fixed.

## Deliberately NOT refreshed

Lanes 2 and 3 were left as found. Their movement was not independently
verified in this run, and inventing movement to make a steering surface
look current is the failure this run exists to correct. They pass the
gate because their evidence pointers are as old as their timestamps —
which is the same self-referential pass described above, now visible
rather than hidden.

## Owed, and not done here

- The context pack's anchor-facts block was found stale in three places
  by independent passes on 2026-08-12. It is a **cadence-owned root
  status surface** under the multi-writer protocol, so this run did not
  touch it. It needs a wave.
- A leads ledger, so declines stay recoverable (recommended by the drain
  pass after a note was declined on its own stated grounds).
- Lanes 2 and 3 want a genuine evaluation, not a timestamp bump.
