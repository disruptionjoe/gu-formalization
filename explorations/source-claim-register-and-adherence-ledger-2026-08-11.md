---
title: "The source-claim adherence register and its enforcement machinery"
status: active_research
doc_type: process_hardening
created: 2026-08-11
run_id: RUN-20260812-014500-gu-source-claim-register-machinery
lane: "A (process stewardship), ratified Joe direct chat 2026-08-11"
target_claim: NONE-NOT-A-KILL
brief_version: "1.0"
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
hostile_review: lab/process/hostile-reviews/2026-08-11-source-claim-register-gate-review.md
---

# The source-claim adherence register and its enforcement machinery

Joe-directed (direct chat, 2026-08-11), following the recurring pattern he
named: adversarial results kept executing against claims the primary
source disavows, source extractions kept being redone, and subagents do
not reliably ingest top-level governance. An eleven-seat inline science
council deliberated the fixes
(`explorations/science-council-source-fidelity-process-2026-08-11.md`);
its adopted deltas are built into everything below.

## What ships

1. **`lab/sources/source-claim-register.yaml`** — 110 verbatim,
   locus-cited, edition-pinned claim rows (60 draft, 50 spoken; drafts
   hash-pinned to the April 2021 edition), each carrying the council's
   `core:` partition (hard-core 48 / auxiliary 51 / disavowed-by-source
   11) and a dated, revision-pinned adherence block (ADHERED 82 /
   PARTIAL 17 / UNTYPED 11 / IGNORED 0 / CONTRADICTED 0 at `b6d31fdb`).
   Produced by two extraction passes (existing in-repo extractions reused,
   40 regions newly extracted with page-verified quotes, zero GAP rows)
   and an adherence adjudication pass; working notes preserved beside the
   staging record.
2. **`process_gates/kill_target_claim_audit.py`** — write-time
   enforcement: new kill/no-go-bearing artifacts must name their target
   claim by register ID or declare `NONE-NOT-A-KILL` (counted every run).
   Self-test green (planted pass/fail controls); non-retroactive
   (created >= 2026-08-12); trigger handles the house UNDERSCORE_CAPS
   result style — a blind spot the filing baseline itself caught;
   documented retirement condition per the council.
   **Baseline at filing: 5 of the last 40 conditional-build artifacts
   carried kill-language; 0 named any target claim.**
3. **`lab/process/subagent-brief.md` v1.0** — the minimum ingest for any
   delegated GU agent; orchestrators inline it verbatim; subagents echo
   `brief_version:` so ingest is provable.
4. **`lab/sources/media-index.md` refresh** — the existing index (not a
   new one) gains the in-repo-extraction level (work → upload →
   extraction, hash-pin, coverage) and current rows.
5. **AGENTS.md rule** (one bullet, ratified): kills name their target
   claim; orchestrators pass the brief.

## Headline adjudication findings (planning evidence)

The main construction path is substantially faithful: zero CONTRADICTED
rows — every recorded push-back carries an adjudication artifact. The
gaps concentrate in (a) the spoken record: the supercharge-extension
count mechanism (SC-GEN-54) is UNTYPED although the graded IGG extension
exists machine-complete in-repo, and the count verdict was reached
without naming it; the two-stay-identical high-energy claim and the
author's self-supplied falsification surfaces are likewise UNTYPED;
(b) summary/reading layers: the one-day-old CHI/GEN framing correction
lives only in the frontier index while older surfaces still frame the
source-native vectorlike/2+1 reading as a concession (regression risk);
(c) the stalest READ-FIRST surface teaches a retired algebra form
unconditionally (GEOMETER-VS-PHYSICS-OBJECTS.md:19). Full ranked gap
list: `adjudication-notes.md` in the staging record.

## Proposed context-pack block (absorption; the cadence owns the pack)

> **What the source actually claims (register pointers).** ASSERTS:
> non-chiral total theory, chirality emergent via VEV/curvature
> decoupling (SC-CHI-01/50s); 2+1 with one effective imposter, not three
> true generations (SC-GEN-01..06); count fixed at an effective level,
> three spoken mechanisms on record (SC-GEN-54 UNTYPED). DISAVOWS:
> nature repeating herself three times; the circulating imposter
> misquote (absence rows). UNCERTAIN: the draft's own signature stance
> ("We do not know how to choose"). Kills name their target claim:
> `lab/sources/source-claim-register.yaml`,
> `process_gates/kill_target_claim_audit.py`.

## What this filing does not do

No claim-status, verdict, residue, fork, canon, or posture change; no
edit to packet bodies or READ-FIRST surfaces (their repairs are
wave-owned and listed as needs-recheck in the hostile review); adherence
verdicts are dated planning evidence, not settled judgments.
