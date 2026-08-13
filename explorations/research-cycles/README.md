---
title: "Hourly Automation Cycles — Index / Rollup"
status: process
doc_type: index
updated_at: "2026-06-26"
---

# Hourly Automation Cycles — Index / Rollup

The `explorations/hourly-*.md` files (≈525 as of 2026-06-26) and their paired
`tests/hourly_*.py` audits (≈577) are **automated process-exhaust** from the hourly
loop (`.claude/workflows/gu-research-loop.js` and the `process/runbooks/*frontier-run*`
runbooks). They are **not** the research signal. Read this index instead of the per-run files.

## What they are

Each "Run GU NNNN" produces a three-cycle, five-lane batch (lanes: DGU, Tau, K_IG,
ProductAB, QFT) emitting ~6 markdown notes + 1 Python "audit" per cycle. Cycle 1 reports
the next object is absent; cycle 2 defines a verifier that would reject it; cycle 3 writes
a manifest/schema for the still-uninhabited object, plus a three-cycle synthesis tying the
five lanes together.

## What they produced

**Zero claim promotions** over the observed window (per the hourly files' own
`claim_status_change: false`, `claim_promotions: 0`, `source_admissions_count: 0`). The
overnight 2026-06-25→26 runs (~180 files) moved no claim, canon, or status surface. The
loop is **source-custody-blocked**: it has decided it needs lawful-local custody of the
source bytes (the UCSD/DGU video, the PTUJ manuscript) before transcribing a formula, and
cannot obtain them, so it re-derives "the source is still absent" each cycle.

**Human action to unblock:** place the source video/manuscript bytes into the repo with a
checksum + lawful-basis note. A no-progress **STOP RULE** is now in both run runbooks and a
**halt guard** in `gu-research-loop.js` (Orient STEP 0.5), so the loop should now halt and
escalate rather than keep minting empty cycles.

## Readable rollup (start here, newest first)

- `explorations/hourly-three-cycle-fifteen-hole-synthesis-2026-06-25.md` — latest five-lane scorecard.
- The genuine research lives in the **non-hourly thematic** explorations (dark-energy,
  signed-readout, vz-*, type-ii1, generation-count RS, freed-hopkins, …) and in `canon/`,
  `active-research/`, and `RESEARCH-STATUS.md` — those are the surfaces to read, not the hourly corpus.

## Physical relocation: deferred (and why)

Mass-moving the ~525 hourly `.md` out of `explorations/` was **deliberately NOT done**:
166 of the `tests/hourly_*.py` audits hardcode `explorations/hourly-...` paths (and compute
`ROOT` relative to their own location), so a move would break them unless every path and
`ROOT` depth is rewritten in lockstep — a high-risk, low-value migration for zero-promotion
content. If physical relocation is wanted, do it as a single scripted migration that moves
the `.md` + their paired `.py` together and rewrites both the in-file paths and the `ROOT`
computation, then re-runs the suite. Until then this index is the rollup.
