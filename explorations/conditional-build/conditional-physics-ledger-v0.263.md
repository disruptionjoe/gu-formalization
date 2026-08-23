---
title: "Ledger v0.263: the AC-D revival triggers repaired, six rows wired, no verdict moved"
status: active_research
doc_type: ledger_mint_record
created: "2026-08-23"
registry: lab/process/conditional-physics-ledger-v0.263.json
predecessor: lab/process/conditional-physics-ledger-v0.262.json
grade: "APPEND-ONLY LEDGER MINT; ONE FIELD CORRECTION IN THE HARDER-TO-REVIVE DIRECTION, EVIDENCE APPENDS AND TYPING; NO VERDICT, REASON KIND, MAPPING GRADE, DISTANCE OR SUMMARY MOVED"
target_claim: NONE-NOT-A-KILL
target_claim_note: "records a ledger mint whose only meaning-bearing change raises a revival bar; kills no source claim and no route"
canon_verdict_change: none
---

# Ledger v0.263

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact borders
> conventional comparators; the AC-D rows' arena is the conventional 4D SM
> anomaly comparator (fork 1). Any result about that comparator binds only it
> and is not evidence about Weinstein's source-native mechanism absent a typed
> bridge. Read `lab/methods/source-native-comparator-routing.md` first.

`GU-COMPARATOR-ROUTING-CLASSIFICATION: BRIDGE_OR_SEMANTIC_BOUNDARY`

## What changed

Eleven rows touched, 40 field writes, **zero verdict changes**. Verified
machine-side before mint: `verdict`, `reason_kind`, `mapping_grade`,
`distance`, `summary`, `axis`, `source_row` and `id` are byte-identical on all
91 rows, and `progress.verdict_counts` is unchanged at 33 SAME / 22 DIFFERS /
31 NEEDS / 2 OVER_DETERMINED.

**The one meaning-bearing change — `revival_trigger` on AC-D1..AC-D5.** The
filed trigger quantified over a set that LA-3's own recorded witness
`(1,1,1,1,1,7)` shows is non-responsive on all five channels: it fires without
moving the row, which is LA-9 mode `NR`. LA-9's filed replacement fails the
same per-row test, because the anomaly-free lattice `L` is the *intersection*
of all five channel kernels and therefore sits strictly inside each individual
kernel. Each row now carries **its own recorded anomaly functional**:

| row | channel | fires when |
| --- | --- | --- |
| AC-D1 | `SU(3)^3` | `2 n_Q - n_u - n_d != 0` |
| AC-D2 | `SU(2)^2 U(1)` | `n_Q - n_L != 0` |
| AC-D3 | `SU(3)^2 U(1)` | `n_Q - 2 n_u + n_d != 0` |
| AC-D4 | `U(1)_Y^3` | `n_Q - 32 n_u + 4 n_d - 9 n_L + 36 n_e != 0` |
| AC-D5 | `grav^2 U(1)` | `n_Q - 2 n_u + n_d - n_L + n_e != 0` |

The replacement is a **strict subset** of the string it replaces, verified
exhaustively over `[-3,3]^6` with zero containment violations. **The bar to
revive goes up.** Nothing moves toward `SAME`, and no grant is discharged.
Leaving `L` no longer fires these rows by itself, which was the defect.

**Everything else is typing or wiring.** Evidence appended (never replaced,
prior string preserved verbatim as prefix, machine-checked) on RA-B6, RA-E3,
RA-E4, RA-G1, RA-G2 and LT-SM3b — wiring 2026-08-14..17 artifact families that
previously occurred zero times in the ledger into the rows they describe.
LT-SM3b gains `revival_reachability` without its `revival_trigger` being
touched. CT-2 `context` projections accrete on all eleven touched rows, with
grant `G3` forced by CT-1 on the AC-D rows and honestly `UNTYPED` wherever
CT-1 names no node. Six rows whose new text carries kill-language are typed
against the audited `NONE-NOT-A-KILL` hatch with a stated reason.

## Provenance and the verification that produced it

This mint came from a five-lane depth wave whose lanes were required to
produce **exact appliable edits** rather than assessments, each verified by an
independent adversary keyed on `proposal_id` rather than row id — the repair
for a defect in the preceding wave, where five verdicts were computed against
a sibling proposal on the same row.

Of 52 proposals, **13 were verified clean and applied as filed**; five
(`TRIGGER-06..10`) were **rejected as filed and applied only in the verifier's
corrected form**, because the filed strings would have written `(U4, grade T2,
unbuilt)` into an immutable ledger while PHI-1 records `grants_retyped: [U4]`.
The remaining 44 are held: 25 carry a corrected value that has itself never
been verified — precisely the class this repository keeps walking back — and
13 were refuted outright.

**A blocker the lanes did not catch, fixed before mint.** The kill-target gate
was driven to `LEDGER_BASELINE = 0` earlier the same day. The new annotations
contain the words "falsifies", "ROUTE KILLED" and "is KILLED", which would
have made six rows untyped kill-bearing and turned that gate RED. The six
`target_claim` fields in this mint are what hold it at zero.

## Coupled edits shipped with this mint

`lab/methods/gu-base-categories.md` defines node `G3` by quoting the old
trigger verbatim. That datum is **preserved**, because it is anchored to
immutable v0.259, and annotated to record that v0.263 replaced the string on
the live rows. The `G3` node is unchanged: still defined by exactly those five
rows. Head pointers updated in `RESEARCH-STATUS.md`, `lab/process/README.md`
and `lab/process/RESEARCH-AGENDA.json`.

## Deliberately not done

`wave_row_dispositions` is **not** appended. It is a frozen fourteen-entry
v0.259 wave list, and fifteen row-touches since received no entry; appending
silently mixes two waves. Either it is replaced with this wave's list or every
entry including the original fourteen gains a `ledger_version` field — an
owner decision, recorded here rather than taken.

The derived-conditional grant wiring is **not** in this mint. No `GRANT-*`
proposal survived verification, which is consistent with the standing agenda
condition that the backlog is not canonical-ready until the severed condition
graph is typed.

## Gates at mint

`mint_context_projection_audit` exit 0, touched-with-context 11/11.
`kill_target_claim_audit[ledger]` 0 untyped kill-bearing rows at baseline 0.
`conditional_evidence_delta_gate` PASS. `current_state_absolute_currency` ok.
`probe_authorship_lint` at its 263 ratchet.

No scientific verdict, canon, source ownership, prediction credit or public
posture changes.
