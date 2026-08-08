---
artifact_type: exploration_result
created: 2026-08-07
status: REAL_CLIFFORD_FORM_SETTLEMENT_NEVER_PROPAGATED__34_CANON_FILES_UNREVISITED__AT_LEAST_ONE_DISSOLUTION_TRIGGER_FIRED_AND_UNEXECUTED
grade: "DEPENDENCY TRIAGE over canon. File set found by searching canon/, CANON.md,
  RESEARCH-STATUS.md and DERIVATION-PROGRESS.md for the (9,5) / M(64,H) / Sp(64) /
  quaternionic horn, then comparing each file's last-modified date against the
  2026-08-04 settlement. Bucketing uses mechanical signals plus direct reads of
  the two highest-risk files. Mentioning the horn is NOT the same as depending on
  it; this artifact reports exposure, not breakage, except where a file's own text
  states its dissolution condition."
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
priority_change: none
row_change: none
residue_touched: []
deposit: "PRE-DEPOSIT. No canon file is edited or retracted here. Any actual
  dissolution requires the hostile field-specialist review of the standing
  2026-08-03 rule."
---

# The `REAL-CLIFFORD-FORM` settlement was never propagated

## The situation

`lab/process/layer0-fork-registry.yaml` records `REAL-CLIFFORD-FORM` as **SETTLED
at `Cl(7,7) = M128(R)` on 2026-08-04**, by derivation from source-typed
arithmetic. That reverses the 2026-06-25 N1 signature audit, which had corrected
`(7,7) -> (9,5)` by trace-reversing the Frobenius metric on the fibre.

The settlement carries an explicit transfer ban: *"do not import the (9,5)
right-H / chosen-J machinery into `Cl(7,7)`"*, and notes the two algebras "are not
real-isomorphic and complexification does not carry the real pairing or the
right-H structure."

```text
canon/status files resting on the (9,5) / M(64,H) / Sp(64) / quaternionic horn : 36
  touched on or after 2026-08-04 : 2   (CANON.md, RESEARCH-STATUS.md only)
  never revisited                : 34
```

The two that moved are top-level status surfaces touched constantly for unrelated
reasons. **No downstream canon result was revisited.**

## The headline finding is not "unaudited". It is worse and more specific.

`canon/no-go-quaternionic-parity-generation-sector.md` — canon tier, verdict
`CONDITIONALLY_RESOLVED`, a structural no-go on the generation sector — **states
its own dissolution condition in its own text**:

> quaternionic `Cl(9,5) = M(64, H)` signature (`J^2 = -1`). It **DISSOLVES** under
> a defensible alternative real-class signature such as `(7,7)` (`J^2 = +1`),
> where the Kramers/quaternionic pairing no longer applies.

and closes:

> the `(9,5)`-vs-`(7,7)` contingency at lines above is untouched and is the
> **live reopener**.

**The reopener fired on 2026-08-04. Nobody pulled it.** The file predicted the
exact condition under which it dissolves, that condition became the settled horn
three days ago, and the no-go still stands as canon on a question — the
generation count — that is the program's headline open item.

This is not a case of sloppy hedging. The hedging is exemplary. **What is missing
is anything that watches for a hedge's condition becoming true.**

## Triage of the 34

| bucket | count | basis |
|---|---:|---|
| **A — dissolution trigger may have fired** | ~9 | file states a `(7,7)` contingency that the settlement now satisfies |
| **B — likely survives** | ~13 | explicitly `GU-independent`, so the conclusion does not rest on GU's signature |
| **C — needs reframing, result may survive** | ~2 | proven in the `(9,5)` frame, but the underlying computation was originally done under `(7,7)` and recorded as surviving |
| **D — unhedged and unreviewed** | ~10 | no `(7,7)` mention, no contingency language, no GU-independence claim |

**Bucket A (highest priority).** `no-go-quaternionic-parity-generation-sector.md`
is confirmed by direct read. Candidates by signal:
`six-axis-escape-hatch-map-RESULTS`, `firewall-boundary-hypothesis`,
`ghost-parity-krein-synthesis`, `three-generations-locate-not-force-CRT-RESULTS`,
`six-axis-candidate-krein-positivity-dg`, `firewall-import-selector-carrier-RESULTS`,
`multiplicity-theorem` (already marked `superseded`), `DERIVATION-PROGRESS.md`
(partly fenced by its 2026-08-03 terminal guard).

**Bucket C.** `canon/shiab-existence-cl95.md` is titled for the `(9,5)` setting
and proves Shiab existence via `S = H^64` with H-linear Clifford multiplication.
But `DERIVATION-PROGRESS` records the original N2 computation as "done under the
`(7,7)` assumption; **result survives**." So the result plausibly holds on both
horns while the canon framing is `(9,5)`-only. Reframing, not retraction —
**and it must be checked, because Shiab existence is upstream of a large amount
of work.**

**Bucket D.** `schwarzschild-weak-field-rfail`, `boundary-eta-of-mu-RESULTS`,
`type-ii1-spectral-sm-checklist`, `anchored-leads-screen-RESULTS`,
`hessian-z3-carrier-occupancy-RESULTS`, `source-action-seiberg-witten-construction`,
`carrier-dirac-mass-capstone-RESULTS`, `escape-corners-campaign-RESULTS`,
`gamma-traceless-38-adjudication-RESULTS`, `w2-y14-spin-structure`. These mention
the horn with no hedge and no independence claim. Exposure unknown.

## Already-confirmed casualty, found by accident

`AC-G1` is the same failure, found incidentally by CB-C on 2026-08-05: canon
asserted the `U(128)` pincer is defused by `Sp(64) = U(64,H)`, an object that does
not exist under `M128(R)`.

**CORRECTION 2026-08-07:** that one has since been repaired. `CANON.md` now scopes
the claim to "the **conditional** `Cl(9,5)=M(64,H)` horn" under an explicit
`AC-G1 SCOPE CORRECTION (2026-08-07)`, and the ledger row carries
`row_status: SUPERSEDED` with successor `AC-G1a`. **The repair was surface-only:**
`CANON.md` and `RESEARCH-STATUS.md` were scoped and none of the 34 downstream
canon files was touched. So propagation happens when someone trips over a case,
not systematically — which is the finding, not a counterexample to it.

One casualty confirmed by accident, one dissolution trigger confirmed unfired,
and 34 files carrying the dependency. The base rate is not zero.

## The general defect

The repository has strong machinery for **making** corrections — Layer-0 audits,
hostile review, the fork registry — and none for **propagating** them.

The fork registry records `settled_by`: the evidence that produced the
settlement. Nothing records the **consequence set**: what was decided under the
old horn and must now be rechecked. So a settlement is an event with an input
list and no output list.

Two mechanical gaps make it worse:

1. **Contingency language is not standardized.** This triage's signal scan looked
   for `CONTINGENT` / `conditional on`, and missed
   `no-go-quaternionic-parity-generation-sector.md`, which says `DISSOLVES under`.
   The most important file in the audit was found by reading, not by scanning.
2. **Nothing watches a fired trigger.** A hedge is written once and never
   evaluated again.

## Cheapest durable fix

When a fork is settled, require a **consequence list** alongside `settled_by`:
the files and rows decided under the retired horn, each marked `dissolved`,
`survives`, or `needs-recheck`. That is the output list the registry currently
lacks, and it would have caught both `AC-G1` and the quaternionic-parity no-go on
the day of settlement.

Standardizing dissolution language (`DISSOLVES-IF:` as a frontmatter field) would
make the watch mechanical rather than editorial.

## Fences and honest limits

- **Mentioning the horn is not depending on it.** Buckets B, C and D are exposure
  classifications, not breakage claims. Only
  `no-go-quaternionic-parity-generation-sector.md` is confirmed by its own text.
- Bucket boundaries come from mechanical signals plus two direct reads. Individual
  files will move on inspection; the headline — 34 unrevisited, at least one fired
  trigger — does not depend on the bucketing.
- Nothing here retracts, edits or dissolves any canon entry. Executing a
  dissolution requires the hostile field-specialist review of the 2026-08-03 rule.
- `IMPOSTER-LABEL-AB` also settled (2026-08-03) and has its own unpropagated
  consequence cone. **Not examined here.**
