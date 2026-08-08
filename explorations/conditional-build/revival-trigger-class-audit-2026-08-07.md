---
artifact_type: exploration_result
created: 2026-08-07
status: EVASION_QUESTION_IS_ASKED_25_OF_25__BUT_13_NAME_ONLY_A_CONDITION__NEGATIVE_PHRASING_IS_THE_TELL
grade: "CLASSIFICATION over the v0.39 machine ledger. Every DIFFERS and
  OVER_DETERMINED row was read and its revival_trigger sorted into names-a-class
  / borderline / condition-only. The sort involves reading judgment and is
  reported per row so it can be disputed line by line. No physics computed."
ledger: lab/process/conditional-physics-ledger-v0.39.json
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
priority_change: none
queue_change: none
row_change: none
residue_touched: []
follows:
  - explorations/conditional-build/construction-improvements-2026-08-07.md
---

# Do the program's own kills name their evasion class?

## The question and why it was asked

`canon/no-go-class-relative-map.md` treats every no-go GU **inherits** from the
literature with a fixed schema: *class fixed | strongest evasion class | candidate
richer datum | candidate forgetful operation*. It has five entries — Witten,
Nielsen-Ninomiya, Freed-Hopkins, Distler-Garibaldi, Velo-Zwanziger — and **zero**
for a kill GU generated itself.

The hypothesis was that internally-generated kills therefore skip the evasion
question entirely.

## That hypothesis is wrong, and the correction matters

**All 25 negative rows carry a populated `revival_trigger`.** The evasion question
is asked, every time, in a dedicated field. The ledger schema is better than the
hypothesis assumed.

The real defect is finer: a revival trigger can name **a condition** (what would
count as winning) or **a class** (where to look). Both are useful; only the second
directs construction.

## Result

| | rows |
|---|---:|
| names a construction class or route | 8 |
| borderline | 4 |
| **condition only** | **13** |
| total | 25 |

**Roughly half of the program's negative rows say what would revive them without
saying where such a thing would come from.**

### Names a class — the good form

- `AC-F4` — *"a **framed or String** receptacle with a constructed nonzero class"*
- `LT-GR1b` — *"...or an action theorem owning the **independent Gauss route**"*
- `LT-GR4` — *"an exact **GU-native** sign opposite to the **ported** negative horn"*
- `LT-SM3b` — *"a **primary source** or **full-domain theorem** proving..."*
- `AC-G1` — *"an exact **real-horn pincer calculation** with a valid **replacement group**"*
- also `LT-GR3`, `LT-GR6`, `RA-E3`

`AC-F4` is the model. It names two specific structure groups a solution could live
in. **The template already exists in the repository; nothing needs inventing.**

### Condition only

`RA-A4`, `RA-A5`, `RA-B6`, `RA-D2`, `RA-E4`, `RA-F3`, `RA-G1`, `RA-G2`,
`LT-GR2a`, `LT-SM3`, `LT-SM4`, `LT-SM6`, `AC-F3`.

### Borderline

`RA-E5`, `LT-GR5`, `AC-A5`, `AC-G2` — each names an object type but not a class of
construction that supplies it.

## The diagnostic: negative phrasing is the tell

Two rows state their trigger as an **exclusion** rather than a target:

- `RA-D2` — "an exact chiral physical carrier **not obtained by** equivariant mass splitting"
- `AC-F3` — "a nonzero 3-primary bridge **not sourced by** the locally vanishing bulk anomaly"

These are exactly the two rows where an independent review on 2026-08-07 found
**unnamed evasion classes** — Wilson lines, flux quantization and orbifold
projection for `RA-D2`; framed and String structures for `AC-F3`. The review
found them without knowing this audit would run.

**A trigger phrased as "X not obtained by Y" tells you what will not count and
nothing about where to look.** That shape is a cheap, mechanical flag for a row
whose evasion column needs populating.

## One finding that is free money

`AC-F3`'s missing evasion class is **already written down one row away**.
`AC-F4`'s trigger names *"a framed or String receptacle"* — which is precisely the
class `AC-F3`'s exclusion-phrased trigger fails to name, and `M-C4` reached the
same place independently in 2026-08-03.

The information exists in the ledger. `AC-F3` does not point at it. Cross-linking
two adjacent rows costs nothing and converts a dead-ended trigger into a route.

## What this earns

Populating the class column for the 13 condition-only rows is **additive** work:
its output is a list of live construction routes derived from kills already
computed, not another correction. It is the cheapest source of construction
targets currently visible, because the underlying computations are done.

Suggested order, by size of the block behind the row and by how well-known the
evasion classes are: `RA-D2`, `AC-F3` (both already have candidates identified),
then `LT-SM3`, `RA-G2`, `LT-SM4`, `LT-SM6`, then the `PREDICTION`-kind rows, whose
triggers are conditions by nature and may be correctly condition-only.

## Fragility

- The three-way sort is reading judgment. It is reported per row precisely so a
  reviewer can move individual rows without disturbing the headline, which is
  robust: a large minority name conditions only, and the negative-phrasing tell
  identifies at least two of them independently.
- `PREDICTION`-kind rows may legitimately be condition-only — a prediction row's
  revival genuinely is "compute the number." Six of the thirteen are
  `PREDICTION`. Excluding them, the condition-only share is 7 of 19, which is the
  more honest figure for rows where an evasion class was possible.
- No claim is made that any named class actually works. Naming a class is a
  direction to search, not a result.

## Fences

No verdict, row, distance, revival trigger, residue count, quotient, fork, canon
entry, lane, priority or queue rank moves. No `revival_trigger` field was edited;
this artifact only classifies them.
