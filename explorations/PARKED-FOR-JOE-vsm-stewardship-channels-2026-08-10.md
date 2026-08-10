---
title: "PARKED FOR JOE — decision packet for the repo-update rotation: type Lane A stewardship as VSM Systems 2-5 channels (observation reports -> S1 analyses/fixes), with a 30-day staleness dead-man switch"
artifact_type: parked_decision_packet
status: PARKED_FOR_JOE__DO_NOT_ABSORB__SURFACES_WHEN_THE_ONE_REPO_A_DAY_ROTATION_REACHES_GU
created: 2026-08-10
directed_by: "Joe direct chat, 2026-08-10: park this on GU so it is brought to his attention when his
  one-repo-a-day full-update effort (an active Outcome in System Attention — number per its owner,
  ~18/20/21) reaches this repo. Rotation currently at system-attention."
audience: "Joe, at the GU stop of the rotation. Hourly/scheduled agents: this is NOT an absorption item and
  NOT agent work — it is a parked architecture decision for Joe. Leave in place."
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Decision packet: VSM stewardship channels for Lane A

## The idea (Joe's, 2026-08-10, lightly sharpened)

Generalize Lane A stewardship as **in-repo VSM System 2-5 work, one channel per level**. Each channel's job
is to produce **observation reports** against the standing questions of that level's operating contract.
**System 1** (the lane's operational work) then turns reports into analyses and executes the fixes/updates.
Lane contract carries a staleness trigger: **if a level has not been reviewed in 30 days, review it.**

## Why GU is the natural pilot

The mapping is mostly *naming things that already run here*:

| VSM | GU instance, already live |
|---|---|
| S1 operations | the hourly's waves; the absorption backlog being worked |
| S2 coordination | multi-writer protocol, `lab/process/NAMES.md`, scoped sessions (ratified 2026-08-10) |
| S3 / S3* audit | wave-scheduling rule P-H28; **the hostile-verification sweeps are textbook S3*** — sporadic, independent, rebuild-from-scratch (receipts: `hostile-verification-harness-receipt-2026-08-10.md`, `canon-spine-hostile-sweep-receipt-2026-08-10.md`) |
| S4 outside-and-future | imported-formula/primary-source checking (the Stelle catch), literature finds (van den Dungen), cross-repo mailboxes |
| S5 identity/policy | `RESEARCH-POSTURE.md`, the firewall primary question, the two-phase promotion rule, the guidance-tier posture |

And the observation/analysis split is the same epistemics as two ratified rules: **observer and intervener
are different runs** (two-phase canon promotion) and **producer manifests at licensed strength, consumer
metabolizes** (absorption protocol). Three independent arrivals at one principle in one day.

## What is genuinely new (the two things to decide)

1. **The staleness dead-man switch per level.** Generalizes the repo's own named gap ("nothing watches a
   stated dissolution condition") to: nothing watches the watchers. Evidence this week: the context pack
   aged into a 1,370-line campaign ledger unnoticed; verification decays as dependencies move. A
   `last_reviewed:` date per level + a trivial gate is enforceable — and per the guidance-tier posture, the
   *trigger* is gate-hard while the review itself is work.
2. **Typed observation channels.** Reports declare which level's standing questions they answer, at
   licensed strength, fixes excluded; S1 owns intervention.

## The minimal build (overbuild-checked)

ONE `stewardship-contract` file per lane — per level: standing questions, `last_reviewed:`, pointer to the
S1 backlog — plus ONE staleness gate in `process_gates/`. Nothing else. Three cautions carried from the
councils: **channels are report streams, not staffed subsystems** (four org-chart channels would be the
overbuilt version of a one-file idea); **levels are hats per run, not separate agents** (one session did
S3*, S4 and S5 work today under Joe's ratification); and **add the algedonic bypass** — one sentence saying
posture-level findings (e.g. "defects concentrate where correction chains stop propagating") escalate to an
S5 review immediately rather than waiting for the 30-day clock. REFUTED verdicts already do this informally.

## Seeds ready when you arrive

This week produced a full season of S2-S5 observation reports to seed the standing questions from: 16
hostile verifies (S3*), the imported-formula sweep (S4), the process/science council outputs (S5), and the
correction-propagation baseline (17 machine-tracked gaps, `lab/process/correction-registry.yaml`).

## Routing note

This is Lane/CapacityOS-level architecture; if adopted at GU, the generalization decision routes to
CapacityOS per this repo's own contract. Nothing here is agent-executable before Joe's decision.
