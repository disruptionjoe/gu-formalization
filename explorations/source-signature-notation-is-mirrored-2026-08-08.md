---
artifact_type: exploration_result
created: 2026-08-08
status: NOTATION_MIRRORED__NO_CONVENTION_DIVERGENCE__OWN_RESOLVER_FALSIFIED__K77_BRANCH_RESTS_ON_A_MIXED_NOTATION_SUM__RCF_PRESSURED_NOT_ACTED_ON
grade: "EXACT. tests/source_signature_notation_is_mirrored.py is green. Three
  source-stated signature pairs are compared against three independently computed
  ones and are exact mirrors in all three places; the control evaluates all three
  forms at three different bases and gets bit-identical results, which is what
  makes the notation reading FORCED rather than merely plausible. The pressure on
  REAL-CLIFFORD-FORM is stated and NOT acted on."
run_id: GUH-20260808T060000Z-register-side-track
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
priority_change: none
row_change: none
residue_touched: []
follows:
  - explorations/signature-fork-is-an-equivariance-defect-2026-08-08.md
  - lab/process/hostile-reviews/2026-08-08-signature-fork-equivariance-review.md
---

# The source's signature notation is the mirror of ours

The hostile review left exactly one gap and called it the whole gap: is the
source's `(1,3)` the ambient-relevant base, or a `Spin(1,3)` gauge-group
statement? **It is neither. It is our `(3,1)`, written backwards.**

## The test, which is not a judgement call

The source states **three** signature pairs for objects this repository computes
independently — the raw symmetric-matrix form, its traceless sector, and the
trace-flipped result
(`lab/sources/curt-iceberg-7-7-reasoning-reinspection-2026-07-31.md`, timestamps
`00:39:55`–`00:40:53` and `00:46:06`–`00:47:20`).

| object | source says | computed here |
|---|---|---|
| raw Lorentzian symmetric-matrix form | `(3,7)` | `(7,3)` |
| traceless sector (9-dim) | `(3,6)` | `(6,3)` |
| after flipping the trace line | `(4,6)` | `(6,4)` |

**Exact mirrors, three for three.** One coincidence is possible; three is not.

**The control is what makes it forced.** A sceptic would say the source is simply
computing at a different base signature. It cannot be: every form here is *even*
in `A = g⁻¹B`, so `g → −g` leaves all three fixed, and permuting which axis is
timelike is a coordinate relabeling. The certificate evaluates all three at three
different bases and gets **bit-identical** numbers each time. The source's pairs
are therefore **not reachable by any base sign choice**. Notation is the only
explanation left.

## What dissolves

```text
source horizontal "(1,3)"  IS  this repository's base  (3,1)
source vertical   "(4,6)"  IS  this repository's fibre (6,4)
source total      "(5,9)"  IS  this repository's total (9,5)
```

**There is no source/repository convention divergence.** The repository has been
running the source's own convention the entire time.

**My own resolver, filed this afternoon, is falsified.** The "declared-base route"
read a notational mirror as a substantive disagreement. `SIGNATURE-AMBIENT`'s
`named_resolver` is retracted to `NONE` — the second resolver falsified on that
row today, after `M-H9`.

## What replaces it, pointing the other way

The source's own block arithmetic is **correct**, and it lands on this
repository's answer:

```text
(4,6) + (1,3) = (5,9)        the source's own spoken blocks
   ==  (6,4) + (3,1) = (9,5) the same statement in our notation
```

The step that does **not** follow from the source's own numbers is its **asserted
total `(7,7)`**. Reaching `(7,7)` requires reading the horizontal block in the
*opposite* notation from the vertical — two conventions mixed inside one sum. The
reinspection note already observed the blocks give `(5,9)` and typed the last step
`SOURCE-UNTYPED`. What is new is **why** it fails, and that the failure is
mechanical rather than interpretive.

## And that is not confined to the transcript

`process_gates/fork_depth_audit.py` has been **failing** on
`fork_assumed: SIGNATURE_AMBIENT_K77 is not a registry id`. It is a pre-existing
red gate, present on a clean tree, and it was pointing at this.

Eleven files carry that non-registry id — seven explorations in the K77 /
`conditional-build` line plus four `lab/process/*.json` records. Their shared
`fork_stack_acknowledged` reads:

> "Lorentz `(1,3)` horizontal plus trace-reversed Frobenius `(6,4)` vertical gives
> the active `(7,7)` horn"

That is **precisely the mixed-notation sum**: `(1,3)` in source notation added to
`(6,4)` in ours. In either notation taken consistently the sum is `(9,5)`/`(5,9)`,
never `(7,7)`.

**Stated carefully, because the distinction matters.** This does not show `(7,7)`
is wrong. It shows the *stated justification* for standing on that horn, in this
branch, does not follow. `(7,7)` may well survive on other grounds — that is the
`REAL-CLIFFORD-FORM` question, which is settled and which this artifact does not
touch.

## Pressure on a settled row — recorded, not acted on

`REAL-CLIFFORD-FORM` is **settled at `Cl(7,7) = M128(ℝ)`**, `settled_how` citing
*"Curt/Eric's exact source-typed arithmetic rather than choosing it"*, and it
carries the highest measured fan-out in the program.

If the source's arithmetic self-consistently yields `(5,9) ≡ (9,5)`, then that
settlement rests on the source's **assertion** rather than on its **arithmetic**.
That is a genuine pressure and it is filed here so it is not lost.

**Not acted on, for two reasons.** Unsettling the program's highest-fan-out row
requires its own review; this artifact establishes a notation fact, not a
disposition. And `REAL-CLIFFORD-FORM` asks which algebra *the source computes in*,
which the registry explicitly marks as distinct from the ambient signature — so
the pressure is real but not automatically decisive.

## Owed, and not done here

- **The red gate.** Either the eleven files' `fork_assumed` becomes the registry
  id `SIGNATURE-AMBIENT`, or `SIGNATURE_AMBIENT_K77` becomes a real row. That is a
  change to what seven waves declared they assumed, so it is not made
  unilaterally.
- **A `REAL-CLIFFORD-FORM` re-review**, on the narrow question of whether its
  settlement survives the observation that the source's blocks sum to `(9,5)`.
- The seventh homonym and the `Cl(3,1)`/`Cl(1,3)` swap correction from earlier
  today are **unaffected** — both stand.
