# Migration audit: `43c66e3b` "Migrate GU public boundary to native research truth"

Prepared 2026-08-13 from a Joe-directed side session, read-only against the
migration commit. **This is a check-in, not a challenge.** The boundary the
migration draws is coherent and most of what it removed clearly belongs outside a
research-truth repository. The purpose here is to confirm intent on a short list of
items and to close the references the deletions left behind.

Scale: **3,048 files changed, 5,039 insertions, 73,077 deletions, 0 additions.**
388 files deleted outright: 302 under `lab/automation`, 52 under `lab/process`, 17
under `runs/`, 5 `process_gates`, 4 under `absorbed/`, 3 under `attention/`, 3
`.claude/` files, plus `LANE-STATE.yaml` and `LANES.yaml`.

## Confirmed intact — no action needed

The scientific record survived. Recording this so the questions below are read in
proportion.

- Both canon promotions whose `attention/` notices were deleted are still recorded
  in canon: `canon/generation-carrier-identification-scope-correction-2026-08-10.md`
  exists, and the pin14 bordism derivation is in `CANON.md`.
- `lab/sources/source-claim-register.yaml`, `lab/process/subagent-brief.md`,
  `lab/process/improvement-register-2026-08-03.md`,
  `lab/process/eleven-lens-audit-2026-08-03.md`, `lab/process/NAMES.md`,
  `lab/process/loop-adversarial-log.md`, `lab/sources/media-index.md` and all of
  `lab/process/hostile-reviews/` survived.
- Every path the new `AGENTS.md` points at resolves. No broken references in the
  contract itself.

## Questions — please confirm intent, then either restore, relocate, or record

### Q1. `lab/process/agent-context-pack.md` (deleted; 10 inbound references)

Named in the multi-writer protocol as a cadence-owned surface, and it was the
standing orientation surface agents read before working. **10 files still reference
it**, mostly the 2026-08-11/12 design packets.

Was this intended as out-of-boundary, or collateral? If intended, the 10 referring
files need their pointers updated to whatever replaces it.

### Q2. `lab/process/councils/` (3 files deleted; 1 inbound reference)

`2026-08-08-science-council-on-authorial-dependency.md`,
`2026-08-08-path-dependency-integration-council.md`, and
`2026-08-08-science-council-blockbuster-potential.md`.

These are deliberation records rather than scheduling artifacts, and the first is
directly relevant to the source-fidelity work now running.
`lab/process/layer0-fork-registry.yaml` still points at that directory.

### Q3. `lab/process/OPERATING-MODEL.md` (deleted)

Substantive, and nothing in the new structure replaces it. Intended?

### Q4. Two rules ratified in Joe direct chat earlier the same day

Both were in `AGENTS.md` before the migration and are not in it after.

1. **Trunk rule** (commit `06084deb`): `main` is the trunk; scheduled progress and
   stewardship runs commit and push to it; the canonical checkout does not sit on a
   long-lived `agent/*` branch. This was the durable half of the same-day fix for
   343 commits that had accumulated off `main` — the new `AGENTS.md` restores the
   phrase "pushed to the current branch," which is the wording that produced that
   state.
2. **Bound-form verdict amendment** (commit `2db3c1d8`): never write that a critic,
   critique or objection "is correct" or "is sound" without binding the word to the
   object analyzed. The amendment itself survives in
   `explorations/claim-indexed-verdict-doctrine-2026-08-12.md`; only the
   `AGENTS.md` pointer to it is gone.

If scheduling policy is out of boundary for this repo, the trunk rule needs a home
elsewhere rather than no home. The bound-form rule is a scientific-writing rule and
looks in-boundary.

### Q5. `process_gates/lane_state_freshness_audit.py` (deleted; 3 inbound references)

Deleting it with the lanes is consistent. But it carried a technique worth keeping
independently of lanes: an **absolute-currency check** that flags a status surface
as stale relative to the repository's newest commit, not merely against its own
timestamp. That generalizes to any status surface and now exists nowhere.

### Q6. Dangling references, roughly 100 total

The deletions left inbound pointers behind:

| target | files still referencing |
| --- | ---: |
| `LANE-STATE` | 86 |
| `agent-context-pack` | 10 |
| `lane_state_freshness` | 3 |
| `lab/process/councils` | 1 |

This is the repository's own documented failure mode — honest artifacts with stale
coordination surfaces — reintroduced at scale by a cleanup commit. Whatever is
decided on Q1 through Q5, these want either a rewrite pass or an explicit note that
the references are historical.

## What this audit does not claim

- It does not assert the migration was wrong. The stated boundary ("work selection,
  scheduling, orchestration are external and are not authority for a scientific
  claim") is defensible and 302 deleted `lab/automation` files plainly fit it.
- It does not evaluate whether lanes belong in this repository. That call reads as
  intentional and is not contested here; only the orphaned references are.
- It verified survival by path existence and reference counting, not by reading the
  contents of the 2,006 modified files. A semantic regression inside a modified file
  would not have been caught.
