---
run_id: GUH-20260808T024447Z-source-action-parameter-structure
status: planned
repository: gu-formalization
workflow: repo-progress-run
mode: execute
lane_id: "1"
work_item: SOURCE-ACTION-PARAMETER-STRUCTURE
starting_revision: 4d2f3e45
opened_at: 2026-08-08T02:44:47Z
origin: "Joe-directed, 2026-08-07. Promoted from the two falsifiable propositions
  that survived a 25-lens viability sweep; see
  explorations/source-action-lens-sweep-viability-2026-08-07.md"
priority: "QUEUED BEHIND CURRENT WORK. This plan reorders nothing. The v0.39
  next_work_queue stands: rank 1 total-residual typing, rank 2 the RA-D2 cluster,
  ranks 3-5 unchanged. Do not preempt them for this."
lapse_condition: "If unstarted by 2026-09-08, treat this plan as LAPSED and delete
  or re-open it deliberately. It must not sit as an indefinite pseudo-commitment;
  a stale plan read as live state is the failure mode this repository has already
  paid for twice."
write_boundary:
  - lab/process/runs/GUH-20260808T024447Z-source-action-parameter-structure/
  - explorations/ (one artifact per test)
  - tests/ (certificates for Test B only)
claim_status_change: none
canon_change: none
public_posture_change: none
priority_change: none
---

# Source-action parameter structure: the DECLARATION floor and the unranked quotients

Two independent tests. Either may be run alone. Neither depends on the other,
and **neither may move a verdict, row, residue count or queue rank without the
hostile field-specialist review required by the standing 2026-08-03 rule.**

---

## Test A — the DECLARATION floor

### Decision question

Of the nine `DECLARATION` rows in
`explorations/source-action-requirements-spec-2026-07-13.md`
(`SA-Y2, SA-Y5, SA-Y6, SA-Y8, SA-G1, SA-C1, SA-C3, SA-U2, SA-U5`), how many admit
derivation by a new mechanism, and how many are **permanently undecidable from
within the built structure**?

### Why this is the right question

`DECLARATION` is defined as "a choice the source action makes; the built
structure **provably cannot decide it**." That proof-of-internal-undecidability
is the strongest formalization of "external datum" this repository has. The
program tracks `P1/P2/P3` as unconsumed external-datum slots and has reduced the
missing pieces from three to two, but has no statement of whether the count can
reach zero.

A floor theorem — even a partial one — decides whether unconsumed `P1/P2/P3` is a
failure state to be driven out or the program's actual answer. That distinction
currently shapes effort with no evidence behind it.

### Method

1. For each of the nine rows, extract the *specific* undecidability warrant from
   its cited artifact. Some will be exact theorems; some will be assertions. Grade
   each: `PROVED_UNDECIDABLE` / `ASSERTED_UNDECIDABLE` / `MECHANISM_EXISTS`.
2. For the `PROVED_UNDECIDABLE` set, determine whether each proof is scoped to
   the current built structure or to *any* structure the program could build.
   Only the latter contributes to a floor.
3. Report the floor as an interval, not a number: a lower bound from rows with
   structure-independent proofs, an upper bound from all nine.
4. Secondary objective: type DC-H2's recorded circularity
   (`dc-h2-reciprocity-and-the-zu-block-ratio-2026-08-04.md:225`). If the
   self-reference obstruction is structural rather than incidental, a recorded
   blocker becomes a theorem about where imported data must live. Also determine
   the layer ownership of `ell^2 = Z_U*kappa`, which is currently unstated.

### Kill conditions, declared before computation

- If fewer than two rows carry a structure-independent undecidability proof, the
  floor is **not established** and must be reported as such. Do not report a
  floor of "at least the number of rows that happen to look hard."
- If any row's warrant turns out to be an assertion rather than a theorem, that
  is the finding; do not upgrade it.
- A floor derived only from the *current* built structure is **not** a floor. It
  is a statement about today's construction and must be labelled that way.

### What each outcome changes

- **Floor ≥ 1, structure-independent.** The program should state how many data are
  irreducible and stop treating unconsumed `P1/P2/P3` as a defect. Affects how
  H53's falsifiability claim is worded.
- **No floor.** Every DECLARATION row is in principle derivable; the residue's
  discrete part is a work list, not a boundary. Strengthens the current posture.
- **Mixed.** Report the partition. This is the expected outcome.

---

## Test B — rank the quotients

### Decision question

CB-D reports **83** charged real continuous parameters and states that the count
is "an upper bound before quotients" with **zero** quotients ranked. What is the
count after gauge, field-redefinition, normalization, functional, topology,
domain and discrete-search quotients are actually ranked?

### Why this is the right question

Three independent lenses proposed that H41 is a **selector** rather than an
object — that the real target is the dependency structure collapsing the 83, not
a functional to be written down. If that is right, "build the source action" is
the wrong instruction and "find the quotient" is the right one.

Independent of the lenses, this is work the repository already declares owed:
the unified packet states no quotient of any kind has been ranked, and the
headline number is therefore an upper bound that has never been reduced.

### Method

1. Enumerate the quotient classes named in the unified source-datum packet.
2. For each, identify which of the `U1..U18` load groups it acts on and compute
   the orbit dimension exactly. Exact arithmetic only — no floats — per the
   standing exact-derivative acceptance rule.
3. Compose to a post-quotient count with an explicit statement of which
   reductions are proved and which are conjectural.
4. Emit a certificate under `tests/` with hard asserts and a printed VERDICT,
   per the repository's certificate convention.

### Kill conditions, declared before computation

- Any quotient whose orbit dimension is read from a finite-difference or numeric
  rank computation is **not citable** until certified with exact arithmetic
  (standing rule P-H29). Prefer exact rational arithmetic throughout.
- Overlapping quotients must not be double-counted. If two classes act on the
  same directions, the composition must be computed, not summed.
- If the reduction is smaller than expected, report the small number. A quotient
  campaign that reports a large reduction without a certificate is the failure
  mode here.

### What each outcome changes

- **Substantial reduction.** The headline 83 is replaced by a smaller certified
  number and the selector reading gains real support.
- **Little or no reduction.** The 83 is closer to genuine content than to
  redundancy, and the "H41 is a selector" reading loses its main support. Equally
  informative and must be reported with the same prominence.

---

## Standing constraints on both tests

- Layer-0 first. Before either test uses a shared term — "fork", "scale",
  "quotient", "datum" — name which object it means. Check 2 of the companion
  artifact found three surfaces reporting fork counts of 9, 10 and 9 over three
  different sets.
- Neither test may cite the companion lens-sweep artifact as evidence. That file
  is a deposit of unverified readings; it motivates these tests and warrants
  nothing.
- Both tests are Build-channel work and must declare their conditional-ledger
  rows before starting and emit the meter plus row changes, or an explicit
  evidence-backed no-change reason, per the functional channel operating
  contract.
