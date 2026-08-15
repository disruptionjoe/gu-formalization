---
title: "research maintenance pass over the Joe-directed channel tree"
status: active_research
doc_type: stewardship_record
created: 2026-08-14
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
steering_effect: unchanged
---

# Research maintenance pass — Joe-directed channel tree

Lane A's stable question is whether the repository still accurately represents
what it knows, what safe local drift can be repaired now, and what the numbered
Lanes should work on next. This pass answers it for the tree produced today.

## Scope and restraint

**Repaired here:** only surfaces this tree owns. **Not touched:**
`CURRENT-STATE.yaml`, `NEXT-STEPS.md`, `RESEARCH-STATUS.md`, `CANON.md`,
`canon/`, any ledger, and the source-residual/superposition lane — all of which
had a live concurrent writer throughout. Every artifact in this tree carries
`canonical_effect: pending_integration` by design, so **not** propagating them
into steering surfaces is correct behaviour, not neglect.

## Drift found and repaired

1. **`lab/active-research/joe-directed/` had no index** while holding 21
   artifacts across 11 threads. Created, with per-thread dispositions and the
   corrections carried against them.
2. **`lab/active-research/README.md` did not list `joe-directed/`** — and did
   not list **`anomaly/`** either, which pre-dates this session. Both rows
   added; `updated_at` moved from `2026-07-25` to today. This is the same
   defect class the 2026-08-13 steering refresh recorded: *a surface that stops
   pointing at current work is fresh by its own gate.* The directory-vs-table
   mismatch is mechanically checkable and currently is not checked.
3. **MJ-5 carried a vacuously-true check.** `$` has no SM-singlet component at
   all, not merely none carrying `B-L`. Correction block appended in place;
   conclusion unaffected and strengthened.
4. **SRC-3 was re-typed by two downstream gates** and did not say so.
   Correction block appended recording CG-1's pre-reduction re-typing, CG-1's
   closure of its cause (2), the third cause it missed, its own conditionally
   vacuous abelian paragraph, and MC-1's cone refutation.

## Proposals routed to other owners — NOT edited here

Each was found by a probe control, is verified by direct read, and touches
property this pass does not own.

| finding | location | owner | severity |
|---|---|---|---|
| Pullback claimed to send `psi` to its horizontal part, graded **VERIFIED**, "no approximation is made" — holds only in the flat-section gauge `d_mu g_ab = 0` | `explorations/vz-evasion/vz-schur-complement-2026-06-23.md` §18.3 | VZ chain | **highest — propagates to `canon/no-go-class-relative-map.md:401` and five explorations** |
| The copy marked `doc_type: primary_source` drops a sentence present in the drafts copy, flipping a passage from concession-only to concession-plus-endorsement | `lab/literature/` vs `papers/drafts/` | source owner | high — it is the material everything else is read against |
| The `n=4` traceless projector called "trace-reversal" and claimed to give `(6,4)`; `lambda = 1/4` is exactly critical and gives `(6,3)` with one null direction | `papers/drafts/vz-evasion-preprint-draft-2026-06-23.md:82` | draft owner | low — draft only, canon unaffected |
| `certificate_shape_audit` fails on two files with no failure path | `cb_a_representation_content_probe.py`, `signature_chirality_conjugation_probe.py` | those probes' owners | low — pre-existing, confirmed against a clean tree |
| Three distinct objects are now called a "cone" (the `(9,5)` symbol cone, W206's cone of invariant forms, `Met_Lor`) | repo-wide | naming | low — homonym |

**OQ3-V3 was not re-decided.** MD-1 shows the *stated reason* in §18.3 does not
hold for a general section; the conclusion may well survive on other grounds.

## Standing observation for the Lanes

Twenty-one artifacts now sit at `pending_integration` with no integration
cursor movement. That is by design, but the volume is itself a steering fact:
the canonical owner has a materially larger backlog than it did this morning,
and **five of the results share one root** — the absence of an SM singlet with
`B-L != 0`, which SG4-1 shows requires a 16 or a 126.

A second steering fact worth recording: **the certificate discipline paid for
itself repeatedly today.** Four vacuously-true or load-bearing-float defects
were caught by non-vacuity controls, three of them in this tree's own probes
and one reaching a committed artifact before MV-2's controls found it. Probes
without planted failing controls should be treated as unverified.

## What the Lanes should work on next

1. **Fix the §18.3 defect** — it is graded `VERIFIED`, it reaches canon, and it
   is the only finding here with canon propagation.
2. **Repair the primary-source copy** before further source-fidelity work; two
   target corrections today came from reading the source, and the derived layer
   is demonstrably lossy.
3. **Add a directory-vs-table check** to `process_gates/`, since the drift in
   item 2 above is mechanically detectable and was not detected.
4. The channel's own next questions — `SOLDERED-AD` (MD-1), the norm-square's
   position relative to the Cartan reduction (CG-1/SRC-3), and `HE-2`'s real
   form — all terminate in SG4 or Lane 1 property and are **not** this tree's
   to take.

No ledger, canon, current-state or priority surface is moved by this pass.
