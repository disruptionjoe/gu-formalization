---
run_id: GUH-20260808T060000Z-register-side-track
status: open_standing_track__first_item_closed
repository: gu-formalization
workflow: repo-progress-run
mode: execute
lane_id: "1"
work_item: REGISTER-SIDE-TRACK
opened_at: 2026-08-08T06:00:00Z
origin: "Joe-directed 2026-08-08: work the improvement-register backlog to the side
  of the hourly construction chain."
priority: "SIDE TRACK. Reorders nothing. The ledger next_work_queue and the hourly
  campaign are untouched. This track exists precisely so register items can be
  worked WITHOUT competing for hourly ranks."
lapse_condition: "Review 2026-09-08. If the register's executed count has not moved,
  the track is not working and should be closed rather than left standing."
write_boundary:
  - lab/process/runs/GUH-20260808T060000Z-register-side-track/
  - lab/process/improvement-register-2026-08-03.md
  - explorations/ (one artifact per executed item)
claim_status_change: none
canon_change: none
public_posture_change: none
priority_change: none
---

# Register side track

## Why this exists

Two work systems run in parallel and do not connect.

```text
improvement register (2026-08-03)   145 items,  8 marked EXECUTED/DONE  (5.5%)
hourly construction chain           224 commits in the same five days
```

The register is audit- and council-derived and prioritised into Q1-Q4. The hourly
runs work the conditional-physics ledger's `next_work_queue`, which is re-authored
every run and contains only construction ranks. **Nothing routes a register item
into that queue**, so register items do not get worked no matter how they are
graded — `M-C1` is graded `C` (critical) and `M-H9` is a named fork-resolver for a
fork currently at stack depth 10, and both have sat five days.

This track works them off-queue. It is not a priority change; it is a second
channel, so the construction chain is never interrupted to service the backlog.

## Standing method

1. **Verify before acting.** Several register rows are already satisfied and were
   never marked. Two were found on 2026-08-08 (`P-H18`, `P-H19`). Check the target
   surface first; if the work is done, mark the row and move on.
2. **Line references in the register are stale.** `P-H18` cites rows 378/397 that
   are now ~1019/1038; `P-H19` cites :376, now ~:1009. Resolve by content, never by
   line number.
3. **Record the fence with the finding.** Where a cert both establishes something
   and limits it, carry both. See `M-C1` below.
4. Anything verdict-adjacent still needs the claim-status workflow and the hostile
   field-specialist review of the standing 2026-08-03 rule. This track does not
   bypass that; it only stops the backlog from being invisible.

## Item state, verified 2026-08-08

| item | grade | state |
|---|---|---|
| `M-C1` | **C / S** | **LIVE, verified, unexecuted — highest value in the register** |
| `M-H9` | H / M | LIVE, unexecuted; resolves `SIGNATURE-AMBIENT` (depth 10) and derives B5 fields (i)-(iii) |
| `P-M25` | M / XS | LIVE, premise shifted; file ships in the published LNF zenodo package |
| `M-H4` | H / M | LIVE; `DERIVATION-PROGRESS` bannered 2026-08-07, underlying claim still unadjudicated |
| `P-H18` | H / XS | **DONE** (verified 2026-08-08), row now marked |
| `P-H19` | H / XS | **DONE** (verified 2026-08-07), row now marked |
| `M-C4` | C / S | DONE, already carried an EXECUTED marker |

## `M-C1` — the first item, and what is and is not licensed

**Verified.** `tests/gen_ch2_sx_from_codazzi.py` hard-asserts `ch2_normal == -1152`
and the certificate reports

```text
ch2(S_X)[K3] = -5376  | decision = CH2_NONZERO_OTHER_INDEX | C2 link = FORCED_ANALOGY
```

described in the cert's own words as "genuinely nonzero, decisively NOT 24, and not
reducible to 3 by any rank normalization".

**What that licenses.** The `ind_H = Â·rank = 16` step assumed `ch2 = 0`. It is not
zero. So the arithmetic of the `16 + 8 = 24` chain is dead, independently of what
the correct index turns out to be.

**What it does not license, from the cert itself.** The families pushforward
`pi_! : ch(S)/Y14 -> ch(S_X)/X4` is `NOT_DEFINED` on the non-convex fibre
`GL(4,R)/O(3,1)`, so `ch2(S_X)[K3]` "is not yet THE index". **The chain's premise is
dead while its replacement is unknown.** That is why `M-C1`'s stated action is
*retire the chain*, not *assert a new count* — and why nothing here should be read
as a new generation-count claim.

**Remaining work on this item.** Record FC3 FIRED on its declaring surface, banner
the live consumers (`decider PART C`, `NEXT-FRONTIER H1(c)`, `oq-rk2`), and retire
the chain from live docs. The retirement is verdict-adjacent: claim-status workflow
plus hostile field-specialist review, per the 2026-08-03 rule. **Not executed here.**

## Execution log

### `M-C1` — CLOSED 2026-08-08. Premise corrected; residue was real.

The row claimed "FC3 fired, **unrecorded**". It was recorded:
`canon/no-go-class-relative-map.md` GC-FC3 already carried *"the standard
vector-spinor-minus-trace operator gives ind_H = -144 (not +8) on the file's own
computation. FIRING."* That is the **third** row today found already satisfied,
after `P-H18` and `P-H19` — three of four items opened turned out done. The
side-track method rule "verify before acting" earned its place immediately.

**What was genuinely new, and it is worth having.** The recorded firing attacks
the `+8` boundary term. This row's `ch2` evidence attacks the `16` bulk term, by
an unrelated computation. Recorded in canon as **GC-FC3b**: the chain's bulk piece
is the `A-hat`-times-rank form of the index theorem, valid only at `ch2 = 0`, and
`ch2(S_X)[K3] = -5376`. **Both halves of `16 + 8` are now independently dead.**

**"Retire the chain from live docs" had no target.** `CANON.md` already records the
count as OPEN and "BLOCKED ON A GENUINE GU THEORY GAP". No live surface asserts
the chain, so no verdict moved and no hostile review was owed.

**Grade correction.** `M-C1` was graded `C` (critical) against the premise that the
firing was unrecorded. With that premise false, its actual blast radius is
provenance-tier. The grade should not be read as evidence that critical work is
being ignored — the *recording* was done; the second independent reason was not.

**Standing lesson for this track.** Three of the first four items were already
satisfied and unmarked. The register's execution rate of 8/145 is therefore an
**undercount of work done**, not purely a backlog — and the first job on any item
is to check the target surface, not to do the work.

## Note for whoever authors the next ledger queue

`lab/process/agent-context-pack.md` now records that register items are
queue-addressable. If a rank names `M-C1` or `M-H9` the way ranks currently name
`LT-GR1`, the hourly runs will work them with no change to how they operate, and
this side track becomes unnecessary. That is the preferred end state.
