---
title: "Science council: source fidelity, re-extraction, and subagent ingest"
status: active_research
doc_type: council_deliberation
created: 2026-08-11
run_id: RUN-PLACEHOLDER
lane: "A (process stewardship)"
convened_by: joe-direct-chat
question: >-
  Three recurring process failures: (1) adversarial results keep executing
  against claims the primary source explicitly disavows; (2) source
  extraction work is redone because prior extractions are not discoverable
  at need; (3) subagents do not reliably ingest top-level governance. How
  should the proposed machinery (source-claim adherence ledger,
  kill-target gate, subagent brief, media-index refresh) be improved
  before filing?
binding: >-
  The modeled council vote is planning evidence, never scientific evidence
  (standing rule). Seats run inline in one context. Adopted deltas are
  design inputs to the machinery filing; they bind nothing until the
  filing's own review.
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Science council: source fidelity, re-extraction, subagent ingest

Eleven seats, run inline. Each seat self-declares its basis
(DIRECT — grounded in this repository's own recorded incidents;
PRINCIPLE — established methodology; ANALOGY — imported from another
field) and a confidence. Convergence, dissents, and adopted deltas follow
the seats.

## Seat 1 — Research-programme methodology (Lakatos/Duhem lens)

Basis: PRINCIPLE. Confidence: high.
The "Nguyen is right → wrong assumptions → conditional route survives"
cycle is a textbook hard-core misidentification: reviewers treat "three
fundamental chiral generations" as the program's hard core, when the
source's stated hard core is a non-chiral total theory with an emergent
2+1 structure. A kill only counts against a programme when it strikes the
hard core; strikes on unclaimed auxiliaries refute nobody.
**Recommendation: the register schema gains a `core:` field —
`hard-core | auxiliary | disavowed-by-source` — and the adherence ledger
adjudicates kills against that partition, not against folk versions of
the theory.**

## Seat 2 — Source criticism / philology

Basis: DIRECT (two recorded incidents: the circulating "imposter line"
absent from the draft; seminar claims mis-attributed to the interview —
SRC-LOCUS check filed). Confidence: high.
Quote fidelity and locus verification are different checks; both have
failed here, and truth-checking catches neither. The register's
verbatim+locus row design is correct. **Recommendations: keep the
absence-finding rows (known misquotes recorded as DISAVOWS with the
search receipt); extend the gate to flag any new kill artifact that
quotes the source without a register ID (quote-without-locus
detection).**

## Seat 3 — Archival science (work/expression/manifestation lens)

Basis: DIRECT (the seminar-vs-interview H1/H2 confusion happened WITH a
media index present). Confidence: high.
The index failed because it collapses levels: a talk (work), its uploads
(manifestations), and the repo's transcripts/extractions (expressions)
were one row-kind. **Recommendation: the media-index refresh types every
row at three levels — WORK → MANIFESTATION (video ID, runtime) →
IN-REPO EXTRACTION (path, hash-pin, coverage) — and carries the H1/H2
residual as its own row with the deciding check named.** Re-extraction
stops when the extraction level is first-class and searchable.

## Seat 4 — Checklist design / human factors

Basis: PRINCIPLE (forcing functions beat placards; every aviation
checklist failure mode). Confidence: high.
Read-time warnings sit far from the failure; the failure happens at
write time. The gate is the right intervention class. Two hazards:
escape-hatch fatigue (`NONE-NOT-A-KILL` will get cargo-culted) and
distance (the register living where nobody looks). **Recommendations:
the gate counts and reports escape-hatch uses per run so abuse is
measured, not suspected; the context pack gains a six-row "what the
source actually claims and disavows" block — the one-read surface is the
only reliably read surface.**

## Seat 5 — Multi-agent systems / context engineering

Basis: DIRECT (this session: five packet subagents each received a
hand-rolled discipline block; drift between blocks is already visible).
Confidence: high.
Subagents ingest exactly what the orchestrator passes plus what they
happen to read; governance does not flow to them automatically, and
hand-rolled prompt blocks drift. **Recommendations: `subagent-brief.md`
is versioned and capped at ~60 lines (ingest ceilings are real); every
subagent output must echo the brief version it ran under
(`brief_version:` in its artifact frontmatter) so ingest is provable
downstream; orchestrators inline the brief verbatim rather than citing
it by path.**

## Seat 6 — Red team / adversarial methodology (dissent seat)

Basis: PRINCIPLE. Confidence: high on the warning, medium on remedies.
Danger: claim-typing becomes a deflection shield — every future kill gets
answered with "wrong claim." Three teeth to keep: (1) the register is
edition-pinned (April 2021 draft hash; dated transcripts) — "he never
claimed X" can never be retconned, and weakening an ASSERTS row requires
a new source edition or an adjudication artifact, never silent
reinterpretation; (2) kills of disavowed claims retain recorded value
against the program's public reception (what circulates) even when they
do not touch the source — the ledger types them, it does not delete
them; (3) the sharpest scientific question gets SHARPER under correct
typing: a vectorlike core plus the observed chiral world means the
emergent-chirality burden is load-bearing — if the decoupling cannot be
constructed, the correctly-typed theory dies honestly.

## Seat 7 — Process engineering / CI discipline

Basis: DIRECT (the repo carries a 17-gate baseline; gate sprawl is a
recorded concern). Confidence: high.
Fail-closed gates earn their keep only while they fire or deter.
**Recommendations: the new gate ships with a planted-control self-test
mode; it scopes to artifacts created after the filing date (no
retroactive red across 354 files); it documents its own retirement
condition (sustained zero-red with zero escape-hatch abuse → fold into a
broader audit); it registers in the standing gate runner rather than as
a new invocation path.**

## Seat 8 — Metrology / measurement

Basis: DIRECT (the repo measures its process; measured base rates are
the house idiom). Confidence: medium-high.
A fix without a baseline is a vibe. **Recommendation: at filing time,
measure and record the baseline — of the last N kill/no-go-bearing
artifacts, how many name any target claim (grep-measurable); track the
post-gate rate and escape-hatch count in the gate's own output. The
register's GAP rows quantify unextracted source regions, making
re-extraction need visible instead of rediscovered.**

## Seat 9 — Ontology / schema design

Basis: PRINCIPLE. Confidence: medium.
The schema (id, polarity, claim, verbatim, locus, grade, notes + the
Seat-1 `core:` field) is sound. Two cautions: area codes are navigation,
not ontology — IDs must be stable while areas stay mutable; and future
draft editions need `status: live | superseded-by-edition` rather than
row rewrites. Adherence verdicts are the rot-prone part (they reference
the moving main path): **keep claim rows stable and edition-pinned;
keep adherence as a dated, revision-pinned column that is allowed to
staleness-warn without invalidating the claim rows.**

## Seat 10 — Physics insider

Basis: PRINCIPLE, literature-flagged (mirror-fermion decoupling and
lattice-chirality constraints are a real literature; citations owed an
independent check before any disposition). Confidence: medium.
Correct typing does not soften the physics; it aims it. The
source-native position — vectorlike core, chirality emergent via a
curvature-linked VEV decoupling — is exactly the class of theory with a
famous burden: making the mirror half heavy/dark without spoiling what
remains. **Recommendation: the register's emergent-chirality rows link
to the repo's named open burdens (PH-K1-PHYSICAL; the Witten-exit
typing) so adherence adjudication lands on the real question, and the
"two generations stay identical at high energy, one does not" spoken
claim is routed to Lane 2 as a candidate tripwire.**

## Seat 11 — In-house skeptic (net-negative risk, dissent seat)

Basis: DIRECT (today's own finding: the anchor-facts layer of the
context pack was stale in three places — every new summary surface is a
new staleness liability). Confidence: high on the risk.
This machinery adds a register, a gate, a brief, and an index refresh to
a program already carrying heavy process mass. Each is a future stale
surface. Mitigations adopted from Seats 7 and 9 (self-test, retirement
condition, stable claim rows, dated adherence) are necessary but the
seat's standing position is recorded: **prefer deleting or merging a
process surface over adding one wherever function allows — here, the
index refresh (merge into existing) is right and a second index would
have been wrong; the register is justified only because it is
enforcement-backed rather than advisory.**

## Convergence

Unanimous on: the failure is structural, not agent-negligence; write-time
enforcement (the gate) over read-time advice; one edition-pinned,
verbatim, locus-cited register as the single source of claim truth;
extending the existing media index rather than adding a parallel one;
a versioned subagent brief with provable ingest.

## Dissents recorded

- Seat 6: claim-typing must never function as a kill-deflection shield;
  teeth enumerated above are conditions of adoption.
- Seat 11: standing objection to net process growth; adoption conditional
  on enforcement-backing and the retirement condition.

## Adopted deltas (design inputs to the filing)

1. `core:` partition field on every register row (Seat 1).
2. Edition-pinning plus the no-silent-reinterpretation rule (Seat 6).
3. Adherence as a dated, revision-pinned column separate from stable
   claim rows (Seat 9/11).
4. `brief_version:` echo required in subagent artifact frontmatter;
   brief capped ~60 lines, inlined verbatim by orchestrators (Seat 5).
5. Gate: escape-hatch counting, planted-control self-test, no
   retroactive red, documented retirement condition, standing-runner
   registration, quote-without-locus flagging (Seats 2/4/7).
6. Baseline measurement of untyped kills recorded at filing; GAP rows
   quantify unextracted regions (Seat 8).
7. Media-index refresh at three levels (WORK/MANIFESTATION/EXTRACTION)
   with the H1/H2 residual row (Seat 3).
8. Context-pack six-row claims block proposed via absorption (Seat 4).
9. Emergent-chirality rows link the named open burdens; the
   high-energy-generations spoken claim routes to Lane 2 as a tripwire
   candidate (Seat 10).
