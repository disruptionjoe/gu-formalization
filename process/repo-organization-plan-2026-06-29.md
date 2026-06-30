---
title: "Repo organization plan -- make the repo presentable to an outsider"
status: proposal
doc_type: plan
created_at: "2026-06-29"
---

# Repo organization plan

Goal: an outsider can land on the repo, read `README.md`, and reach the published result, the evidence,
and the research program **without wading through 830 loose exploration files**. This is a tidy-and-index
pass, not a rewrite.

## Hard rules (non-negotiable for this pass)

1. **Delete nothing.** Every file is preserved. Cleanup = `git mv` (history-preserving moves) + new
   index files. Retiring something means moving it under `archive/`, never removing it.
2. **Do not break the paper.** `located-not-forced-...tex/.md` cites `tests/generation-sector/*.py` and
   several `canon/*.md` files. Those cited paths **must not move** (or must be updated in the same commit).
   `tests/generation-sector/`, `tests/source-action/`, and the cited `canon/` files are frozen for this pass.
3. **Preserve Joe-tuned surfaces.** Root navigational docs keep their names; we reduce *count*, not rewrite
   content.
4. **One commit per phase**, each independently reversible.

## The problem, in numbers

| Location | Files | Issue |
|---|---|---|
| `explorations/` loose (no subdir) | 830 | 530 are `hourly-*.md` no-op output; ~300 are real topical notes, all flat |
| `tests/` loose (no subdir) | 384 | flat `.py`, named `cycle1/2/3_*` and by topic; the organized ones are already in subdirs |
| repo root `.md` | 14 | front-matter overload; an outsider can't tell which 3 to read |
| `draft-papers/` | 29 | the live arXiv paper is buried among 8 `what-GU-needs-next` versions + superseded drafts + process docs |

Most other directories (`canon/`, `process/`, `roadmap/`, `sources/`, `literature/`, `active-research/`,
`archive/`) already carry a `README`/`INDEX`. The convention exists; it just isn't applied to the loose dirs.

## Target top-level (what an outsider should see)

```
README.md            <- single entry point; routes everywhere
CANON.md  RESEARCH-PROGRAM.md  RESEARCH-POSTURE.md  CONTRIBUTING.md  LICENSE-*  .gitignore
docs/                <- the other ~9 root .md files, indexed (status, next-steps, overview, where-GU-stands, ...)
draft-papers/        <- work in progress; the "Located, Not Forced" submission candidate is surfaced at the
                        top of its README, superseded drafts grouped below
published-papers/    <- EXISTING convention; empty until Joe hand-moves a paper here on public posting
canon/               <- stable spine (frozen this pass)
tests/               <- evidence, grouped by sector with a manifest (frozen subdirs; loose files grouped)
explorations/        <- research notes, topical subfolders + an hourly/ corral
process/  roadmap/  sources/  literature/  active-research/  specifications/  automation/  Lean/  archive/
```

## Phased moves

### Phase 1 -- root declutter + surface the paper (highest impact, lowest risk)

- **DONE -- created `docs/`** and moved the 4 genuinely-peripheral, low-reference root docs into it:
  `OVERVIEW.md`, `NEXT-FRONTIER-HYPOTHESES.md`, `WHERE-GU-STANDS-AND-THE-MISSING-OBJECT-2026-06-27.md`,
  `paper-formalization-candidates.md`. Added `docs/README.md`; updated all live inbound references and the
  README "Start Here" / "Repository Layers".
- **KEPT at root by design:** the operational status trio `NEXT-STEPS.md` (85 live referencing files),
  `RESEARCH-STATUS.md` (52), `DERIVATION-PROGRESS.md` (38). They are woven into the canon's `rg`-command
  verification scaffolding and are legitimately root-level status docs; moving them is high-churn, low-value.
  Root drops 14 -> 10 `.md`.
- **No new `paper/` folder.** The repo already has the deliberate `draft-papers/` (work in progress) vs
  `published-papers/` (hand-moved on public posting) split.
- **DONE (commit f1f6e4c) -- the paper-staging workstream.** A workflow census + light adversarial triage
  found exactly two publishable papers; both graduated into `published-papers/candidates/`:
  - `candidates/located-not-forced/` (the lead result; `.tex` is the arXiv source) and
    `candidates/six-axis-testability/` (methods/position track), each with a `STAGING-NOTES.md`.
  - Lifecycle codified: `draft-papers/` (WIP + superseded versions) -> `candidates/` (graduated on Joe's
    explicit publish-intent) -> `published-papers/` (only after Joe confirms posting). See
    `published-papers/README.md` and `candidates/README.md`.
  - "Published result" wording reconciled to "submission candidate"; all internal links rewired.
  - Nguyen response: skipped for now (the honest concede-and-reframe already lives in LNF Sec 9).
- Phase 1 complete (commit follows).

### Phase 2 -- corral the hourly output (turns 830 loose into ~300)

- `git mv explorations/hourly-*.md explorations/hourly-cycles/`, and move `HOURLY-CYCLES-INDEX.md` in with
  them as `explorations/hourly-cycles/README.md`. This single move removes 530 files from the top of
  `explorations/` and is what makes the directory navigable.

### Phase 3 -- topical subfolders for the remaining ~300 exploration notes

Group by the prefixes that already exist in the filenames (no renames, just foldering):
- `explorations/generation-sector/` (generation-*, firewall-*, einvariant/a4a5/a5-* notes)
- `explorations/anomaly-and-bordism/` (anomaly-*, bordism, pi15, sp64-*)
- `explorations/vz-evasion/` (vz*, oq*, oc2* -- the VZ/evasion line)
- `explorations/observer-and-time/` (observer-*, time-as-finality-crosswalk already a subdir, dark-*)
- `explorations/geometry-notes/` (codazzi-*, cartan-*, type-*, layer-split, signed-*)
- `explorations/persona-and-dialectic/` (persona-*, *-steelman-hegelian-*)
- `explorations/misc/` for the long tail; **add `explorations/README.md` as a topical index.**
- Exact prefix-to-folder mapping to be confirmed before moving (grep-driven, ~10 buckets).

### Phase 4 -- group the loose tests

- Fold the 384 loose `tests/*.py` into existing/sibling subdirs by their name prefix:
  `tests/cycle-audits/` (cycle1_*, cycle2_*, cycle3_*), and topical buckets matching the paper's sectors.
  **Frozen:** `tests/generation-sector/`, `tests/source-action/` (cited by the paper).
- Add `tests/README.md` as a manifest: which directory proves which claim, and the three paper-cited files
  called out explicitly (so the "reproducible from tests/" claim is one click to verify).

### Phase 5 -- index sweep + naming note

- Ensure every top-level dir has a one-screen `README.md`/`INDEX.md` (most already do; add for the few that
  don't). Refresh the stale ones.
- Add a short "naming convention" note to `CONTRIBUTING.md`: `topic-subtopic-YYYY-MM-DD.md` for notes,
  `snake_case.py` for tests, RESULTS docs in `canon/`.

## Decisions (locked) and open questions

- **RESOLVED -- no `paper/` folder.** Use the existing `draft-papers/` vs `published-papers/` split; surface
  the submission candidate inside `draft-papers/` (Phase 1).
- **RESOLVED -- run all 5 phases** (Joe, 2026-06-29), per-phase commits.
- **Separate workstream -- `published-papers/candidates/`.** Stage the genuinely publishable papers
  (Six-Axis, a possible Nguyen-critique response, Located-Not-Forced) there after a *light* adversarial pass.
  Driven by the publishable-paper census; folded into this cleanup once the candidate set is locked.
- **Open -- `docs/` name.** `docs/` is conventional and GitHub renders it; alternatives `notes/` /
  `program-docs/`. Defaulting to `docs/` unless Joe says otherwise.
- **Open -- the `~300` exploration notes mapping.** The prefix/content -> bucket mapping is shown for
  confirmation before the bulk move (Phase 3).

## Effort / sequencing

Phase 1: ~15 min, 1 commit. Phase 2: ~5 min, 1 commit (bulk move). Phase 3: ~30 min (needs the
prefix-mapping confirmed). Phase 4: ~20 min. Phase 5: ~20 min. Each phase pushes independently; nothing
here touches the math, the canon spine, or the paper's cited evidence paths.
