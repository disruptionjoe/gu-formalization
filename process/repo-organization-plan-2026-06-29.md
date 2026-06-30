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
paper/               <- the published result, alone and obvious (was the live files in draft-papers/)
draft-papers/        <- working drafts + superseded versions, with a README that says "superseded"
canon/               <- stable spine (frozen this pass)
tests/               <- evidence, grouped by sector with a manifest (frozen subdirs; loose files grouped)
explorations/        <- research notes, topical subfolders + an hourly/ corral
process/  roadmap/  sources/  literature/  active-research/  specifications/  automation/  Lean/  archive/
```

## Phased moves

### Phase 1 -- root declutter + surface the paper (highest impact, lowest risk)

- **Create `docs/`** and `git mv` the non-essential root `.md` into it, leaving root with only what an
  outsider needs first: `README.md`, `CANON.md`, `RESEARCH-PROGRAM.md`, `RESEARCH-POSTURE.md`,
  `CONTRIBUTING.md`, `LICENSE-CODE.md`, `LICENSE-DOCS.md`.
  - Move to `docs/`: `OVERVIEW.md`, `NEXT-STEPS.md`, `NEXT-FRONTIER-HYPOTHESES.md`, `RESEARCH-STATUS.md`,
    `DERIVATION-PROGRESS.md`, `WHERE-GU-STANDS-AND-THE-MISSING-OBJECT-2026-06-27.md`,
    `paper-formalization-candidates.md`. Add `docs/README.md` index.
- **Create `paper/`** and move the four live artifacts there so the published result stands alone:
  `located-not-forced-generation-count-2026-06-29.{tex,md}`, plus a `paper/README.md` pointing to the
  arXiv classification, the test manifest, and the repo. **Update the two internal cross-links** (the `.md`
  header link to the `.tex`, and README/RESEARCH-PROGRAM's `draft-papers/located-...md` references) in the
  same commit. *(Decision needed -- see Open questions.)*
- Update `README.md`'s "Start Here" block to the new paths.

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

## Open questions for Joe

1. **`paper/` vs leaving it in `draft-papers/`.** A dedicated `paper/` makes the published result obvious
   but changes the cited path in README/RESEARCH-PROGRAM (one commit, internal links only -- the arXiv PDF
   is unaffected). Recommended. Alternative: keep it in `draft-papers/` and just add a bold pointer.
2. **Execute all phases, or stop after Phase 1-2?** Phases 1-2 deliver ~80% of the "outsider can navigate"
   benefit (root + the hourly corral). Phases 3-4 are the deeper sort.
3. **`docs/` name.** `docs/` is conventional and GitHub renders it; alternative is `notes/` or
   `program-docs/`.

## Effort / sequencing

Phase 1: ~15 min, 1 commit. Phase 2: ~5 min, 1 commit (bulk move). Phase 3: ~30 min (needs the
prefix-mapping confirmed). Phase 4: ~20 min. Phase 5: ~20 min. Each phase pushes independently; nothing
here touches the math, the canon spine, or the paper's cited evidence paths.
