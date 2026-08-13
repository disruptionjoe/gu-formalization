---
title: "research maintenance steering refresh: LANE-STATE was ten days stale while its own gate passed"
status: active_research
doc_type: stewardship_record
created: 2026-08-13
brief_version: "1.3"
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# research maintenance steering refresh

Second research maintenance run of 2026-08-13, after the mailbox drain. Target: the
steering surfaces research maintenance reconciles.

## The finding, and it is a gate-design defect rather than neglect

`CURRENT-STATE.yaml` carried `updated_at: 2026-08-03` and a `bottom_line`
naming the B5 packet and the `pw2fr` branch as the live front. Between
that timestamp and this run, **478 commits landed** and the campaign
moved to the K77 operator/observation program at ledger **v0.236**.

**Its freshness gate reported PASS throughout.**

The reason is structural, not lazy. The gate compares a lane's
`evaluated_at` against *the newest commit of the evidence that lane
cites*. truth-status research cited a 2026-07-29 audit run-plan and a 2026-07-30
exploration; neither changed; lag was therefore ~0 and the check passed.

**A surface that stops pointing at current work is fresh by
construction.** Self-referential freshness is not freshness.

## What this investigation changed

1. **`CURRENT-STATE.yaml` narrative fields refreshed** to verified current
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

## Lanes 2 and 3 — EVALUATED 2026-08-13 (supersedes the note below)

Both were subsequently evaluated in the same research maintenance run rather than left
with bumped timestamps. They had moved in OPPOSITE directions.

**result-hardening research has genuinely moved; its `reason_code` named only the superseded
2026-08-03 publication.** Since the previous refresh the lane drafted the
2+1 mechanism paper *One Generation, Not Three* (~15pp plus evidence map),
resolved the imposter A/B fork as Reading A at confidence 0.90 with a J5
hostile review passed-with-corrections, documented the Boyle-Turok foil as
the sharpest published fence marker, and DECLINED two externally-facing
candidates after a novelty check found both already known. Two releases
stand at v1.0.0. Green/moving/up was correct; only the reason was stale.
New publication-readiness item recorded: the KO-degree obstruction ladder
is `status: staged` at `tier: internal`, and its GU-independent
disjointness core is the strongest publishable unit not requiring the
main path.

**prediction research's `waiting_external` was a MISTYPING, not merely stale.** Its own
work has not advanced since 2026-08-03 — the three intervening commits
matching prediction/DESI terms are truth-status research and result-hardening research work plus two
side-session design packets. And the 2026-08-11 prediction research packet counted the
lane's PRIMARY route, the `r(N(z))` dark-energy refit, as NOT
packet-worthy on any horn (strict surplus at most `-4`, because the rise
realization is free). **The lane is not waiting on external data: its
primary route was counted out on internal grounds, and its live decision
needs no data at all.** Retyped `blocked_on_internal_decision`. Strongest
banked asset is the hardened FC-d tripwire at margin `+1.11` (W226),
which supersedes the `+0.032` figure still quoted in some anchors.

Lane lights were NOT changed: the evidence moved the reasons, not the
colours.

## Superseded note (retained for provenance)

Lanes 2 and 3 were left as found. Their movement was not independently
verified in this run, and inventing movement to make a steering surface
look current is the failure this investigation exists to correct. They pass the
gate because their evidence pointers are as old as their timestamps —
which is the same self-referential pass described above, now visible
rather than hidden.

## Owed, and not done here

- The context pack's anchor-facts block was found stale in three places
  by independent passes on 2026-08-12. It is a **cadence-owned root
  status surface** under the multi-writer protocol, so this investigation did not
  touch it. It needs a wave.
- A leads ledger, so declines stay recoverable (recommended by the drain
  pass after a note was declined on its own stated grounds).
- Lanes 2 and 3 want a genuine evaluation, not a timestamp bump.
