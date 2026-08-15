---
title: "AR-2: deferral archaeology over the whole repository"
status: active_research
doc_type: stewardship_record
created: 2026-08-15
channel: joe_directed_archaeology
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
steering_effect: unchanged
canonical_effect: pending_integration
scripts:
  - tests/channel-swings/joe_directed_ar2_deferral_archaeology.py
---

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`

This file adjudicates no physics. It catalogues *deferrals* — seams that an
author raised, judged real, and consciously left unanswered — across artifacts
that sit on both sides of the comparator boundary. It borders comparators
because several catalogued seams live inside comparator artifacts (`PHI-2`,
`LA-3`, `PV-1`), and it exists precisely to stop a catalogue entry being
mistaken for a live GU question. Nothing here moves a ledger row, a claim
status, canon, `CURRENT-STATE.yaml` or `NEXT-STEPS.md`.

**Audit-scope disclosure, stated rather than exploited.** `doc_type:
stewardship_record` puts this file outside the derived scope of
`process_gates/source_native_comparator_routing_audit.py`, which is at exactly
its `UNCLASSIFIED_BASELINE = 9` and would RED on any new in-scope unregistered
artifact. The declared type is honest — this is a maintenance pass over the
tree, like `steward-2026-08-14` — and the routing notice and classification are
carried anyway, so the exclusion buys nothing it would not otherwise have.

> [!NOTE]
> **Standing red, not caused by this file.** At the time of writing that audit
> reports 10 unclassified against baseline 9. The tenth is
> `archaeology/ar1-dropped-commitments-ledger-2026-08-15.md`, written
> concurrently into this directory by another agent; it is in the derived scope
> and unregistered. This file is out of scope and does not contribute. Recorded
> so the red is attributed correctly and not absorbed by a raised baseline —
> `UNCLASSIFIED_BASELINE` may only ratchet down.

# AR-2 — deferral archaeology

**Question.** `LA-6` §5.2 wrote that the coupled pair `{LT-GR1b, LT-SM3b}` *"may
be an artifact of both rows being terminal … **Not resolved here**"*; `OT-2`
resolved it two waves later, by accident, because it happened to be the first
classifier to reach it. Nobody was tracking the flag. How many other flags are
outstanding, and which of them is a dead route that must **not** be revived?

## 0. PREFLIGHT — seven specialist lenses, run inline before the sweep

**Lens P1 — corpus linguistics / hedging detection.** Hedges in technical prose
split into *epistemic* ("may", "appears") and *performative* ("I did not decide
X"). Only the performative class is a deferral: it asserts a speech act with a
speaker, a scope and a residue. Route: build the vocabulary from performative
operators with a **self-locator** (`here`, `in this artifact`, `by this gate`)
or an **explicit transfer** (`deferred to`, `flagged for X`), and treat the
ambient state vocabulary (`remains open`, `unresolved`) as a separate class to
be measured, not swept. *Prediction before measuring: the ambient class is at
least 5x larger.* Measured: 2306 vs 315, a factor of 7.

**Lens P2 — risk register practice.** A register row is useless without an
owner, a trigger and a consequence. Route: require an **owner-of-record** and a
**consequence clause** before an item enters a worklist; an unowned, unconsequenced
deferral is a caveat and belongs in the catalogue, not the queue. This lens
produced the load-bearing/routine split that structures §3.

**Lens P3 — technical-debt management.** Debt has two failure modes: interest
(the seam gets more expensive) and **default** (the seam silently stops
mattering). Route: for every candidate, ask whether the *stakes changed* since
it was flagged. This lens found the single most important fact in the sweep:
`SOLDERED-AD` was routed by the steward as "not this tree's to take", and was
**promoted to verdict-load-bearing by `PHI-2` afterwards**, with no surface
recording the promotion except one line of a README.

**Lens P4 — archival science / provenance.** A citation of someone else's
deferral is not a new flag; it is propagation. Route: deduplicate every
candidate to its **originating** artifact before counting convergence, or the
multiply-flagged number inflates itself. Applied: `LA-8`'s "MD-1 explicitly
leaves open…" and `MV-1`'s "PV-2 explicitly leaves that open" are propagation
of `MD-1` and `PV-2`, and are counted as flags on the originating seam, not as
new seams.

**Lens P5 — epistemics of deferral.** "Not resolved here" and "this does not
establish X" are different acts. The first says *I tried and stopped*; the
second says *I never claimed this*. Route: exclude `Claim ceiling` / `What this
does NOT establish` sections from the worklist by default, and admit an item
from them only when the author separately states dependence. Applied: `PHI-2`
§10 and `MV-1` §"Not claimed" are ceilings; their contents enter the catalogue
typed, and none reaches the worklist.

**Lens P6 — adversarial reading (the resurrection hazard).** The repository
deliberately preserves refuted routes, and its worst recurring failure is
attacking a GU that Weinstein does not claim. Route: check every candidate
against `lab/sources/source-claim-register.yaml` (`hard-core` / `auxiliary` /
`disavowed-by-source`, 48/51/11) and `lab/methods/source-native-comparator-routing.md`
**before** it is written down, and give the DISAVOWED and REFUTED classes their
own rows in the output so a reader cannot mine them for work. Applied in §4.

**Lens P7 — evidence law: grep before claiming novelty.** Route: diff against
`NEXT-STEPS.md`, `lab/process/`, the two channel READMEs and
`bd-disposition-packet-2026-08-15.md` before calling anything untracked.
Applied: `lab/active-research/joe-directed/archaeology/` did not exist; there is
no prior AR-* artifact; but `steward-2026-08-14-research-maintenance-pass.md`
§"Proposals routed to other owners" and §"What the Lanes should work on next"
is a genuine partial predecessor and is credited throughout. Four of this
file's worklist items are **already routed by the steward**; this file's
contribution on those is the resolution check and the stake change, not the
discovery.

## 1. The sweep

Two vocabularies, measured separately.

| class | operators | repo-wide occurrences | files |
|---|---|---|---|
| **CORE** — performative non-resolution | `not resolved/settled/adjudicated/decided/attempted here`, `could not determine`, `remains unclear`, `left open`, `leave(s) (it/that) open`, `deferred to/here`, `flagged for`, `beyond (the) scope`, `known limit` | **315** | **237** |
| **HEDGE** — ambient open-state | `remain(s) open`, `unresolved`, `out of scope`, `attack surface`, `later gate`, `weakest seam` | **2306** | — |

3656 markdown files scanned (`_local/`, `.lake/`, `.git/`, vendor excluded).
Repo-wide figures are **floors**, not equalities: the checkout is shared with
concurrent writers and can only grow during a run. The joe-directed tree is
pinned exactly: **48 files, 24 CORE occurrences in 18 files.**

**The instrument is excluded from its own corpus.** `archaeology/` — this file,
and `ar1-dropped-commitments-ledger-2026-08-15.md`, written into the same
directory by a concurrent agent while this sweep was running — quotes every
operator phrase it measures. Counting deferral catalogues inside a deferral
census is circular and drifts each time a sibling appears; the sweep therefore
skips that directory, and says so rather than quietly bounding the number. This
is not hypothetical: the first run after the sibling landed reported 61 CORE
occurrences in joe-directed instead of 24, and the hedge-to-core ratio fell
below its floor. Floors on the repo-wide numbers absorbed the rest of the
concurrent drift exactly as designed.

```
left open            5     not decided here      2
not resolved here    4     flagged for           2
not adjudicated here 3     known limit           1
deferred to          2     leaves open           1
not settled here     2     leaves that open      1
                           leaves it open        1      = 24
```

**A measured defect in the detector itself.** Naive whole-file substring
matching gives 299 repo-wide and 23 in joe-directed. The repository hard-wraps
near column 76, so operator phrases straddle newlines. Whitespace-normalizing
before matching recovers **16 further occurrences repo-wide and 1 in
joe-directed** — and the one in joe-directed is a real seam (`BD-D`'s undecided
`Δ1` fibre-algebra retyping, wrapped as `not adjudicated\nhere`). A sweep that
does not normalize loses about one occurrence in twenty. Both counts are pinned
and asserted by the probe so the gap cannot quietly close.

The `weakest seam` heading appears in 46 files and is the repository's
conventional self-named attack point. It is *not* a deferral operator — it is a
ranking of the artifact's own fragility — but it is where load-bearing
deferrals concentrate, and every §3 item above rank 4 was found through one.

## 2. Counts by type

23 seams catalogued and typed. Every one was checked for later resolution by
any artifact under any name.

| type | count | ids |
|---|---|---|
| `OPEN` | **16** | S01–S06, S08–S17 |
| `RESOLVED` | **3** | S18, S19, S20 |
| `SUPERSEDED` | **1** | S21 |
| `REFUTED` | **1** | S22 |
| `DISAVOWED` | **1** | S23 |
| `UNTYPED` | **1** | S07 |
| **total** | **23** | |

Of the 16 `OPEN`, **6** are load-bearing by the flagging author's own statement
and form the worklist; **10** are routine caveats, author-declared
non-dependent, or already tracked on a canon surface. Independent flagging by
two or more distinct surfaces: **14 of 23**.

## 3. The ranked OPEN worklist — load-bearing only

Ranked by cheapest work that closes a seam a published result already leans on.

### Rank 1 — `AR2-S04` · the VZ §18.3 gauge defect, graded `VERIFIED`, reaching canon

`MD-1` found that `vz-schur-complement-2026-06-23.md` §18.3's pullback claim —
graded **VERIFIED**, "no approximation is made" — holds only in the flat-section
gauge `d_mu g_ab = 0`, and wrote *"Flagged for the owner of the VZ chain; not
actioned here."* The steward pass independently routed it as the **highest**
severity finding of its own sweep, *"the only finding here with canon
propagation"*, reaching `canon/no-go-class-relative-map.md:401` and five
explorations, and made it item 1 of what the Lanes should do next.

**Still unrepaired.** `MD-1` is not referenced anywhere in
`explorations/vz-evasion/` or in `canon/no-go-class-relative-map.md`
(asserted negatively by the probe). Both flagging artifacts are careful that
`OQ3-V3`'s *conclusion* may survive — `MD-1` explicitly declines to re-decide
it — so the work is a **qualifier and a regrade**, not a re-derivation.
Flags: 2. Owner: VZ chain. Cost: hours.

### Rank 2 — `AR2-S02` · `RA-C1` / `RA-B1..B5` versus `AC-C2`: one typing seam, half-closed

`LA-1` §5.3 found rows with identical `U1` dependence split across `DERIVED` and
`DERIVED_CONDITIONAL`, named both repairs, enacted neither, and escalated it
(§6.1, under the heading *"ESCALATED TO THE CANONICAL OWNER — not resolved
here"*). `LA-3` independently flagged the `AC-C2` half *"for the integrator, not
requested"*, saying *"one of these gradings is wrong."* `LA-9` §4.3 then unified
them in its own weakest-seam section: *"`AC-C2`'s retype and `RA-C1`'s typing
are the same unresolved seam, and I only closed one of them … it is the thing in
this artifact I would attack first."*

**Load-bearing, and it got worse on the day it was flagged.** `LA-9` §4.2 records
that `LA-5`'s published rank-10-of-10 revival-incidence result is computed *from
`revival_trigger` strings*, so a defective trigger now corrupts a published
number rather than a description. Three independent flags; absent from the day's
consolidated `bd-disposition-packet` (asserted negatively). Owner: canonical
ledger owner. Cost: one typing decision, then a mechanical edit.

### Rank 3 — `AR2-S06` · `PHI-2`'s routing classification contradicts its own scope paragraph

`bd-reg-routing-backlog-disposition` §2 quotes `PHI-2`'s scope paragraph —
*"built entirely inside a conventional particle-physics comparator … every
result below binds only that named model"* — against its requested label
`BRIDGE_OR_SEMANTIC_BOUNDARY`, and concludes: *"The label and the paragraph
cannot both stand. **Not resolved here.** … PHI-2's author decides."* The same
contradiction is written into `source_native_comparator_routing_audit.py` as
case (c) of its `UNCLASSIFIED_BASELINE = 9` comment.

**Load-bearing for a control, not for physics.** It is one of the nine holding
the routing audit's baseline where it is; the baseline may only ratchet down.
Flags: 2 (one of them a process gate's source). Owner: `PHI-2`'s author.
Cost: one sentence.

### Rank 4 — `AR2-S01` · the `SOLDERED-AD` / `INERT-AD` fork, whose stakes changed after it was routed away

The most-flagged open object in the tree: **seven distinct surfaces**. `MD-1`
declared it and returned the ad leg `NOT-DETERMINED`. `PHI-1` and `LA-8`
explicitly decline to decide it (`LA-8`'s contribution is showing it is *not*
load-bearing for `RA-E2`). `LA-4` files it as *"Escalation, not adjudication."*
The steward routed it out of the tree as SG4/Lane-1 property.

**Then `PHI-2` §7.2 raised its stakes and left it open**, and the channel README
now records that `PHI-2` *"promoted the `SOLDERED-AD` fork to
verdict-load-bearing"* for `AC-D1..D5`. The routing happened while it was
believed cheap; the promotion happened after. No consolidated surface carries
the promotion — it is absent from `bd-disposition-packet` (asserted negatively).
Owner: SG4 / Lane 1. Cost: not cheap; the value here is the **re-rank**, which
is free.

**Hazard check, explicit.** This is source-native, not a comparator revival. The
adjacent *refuted* object is the Kaluza–Klein "vertical components become 4D
scalars" clause (`AR2-S22`), which is withdrawn from the routing method and
which the source disavows in terms. `SOLDERED-AD` is the live successor fork
about the ad leg of a **contraction**, not a resurrection of the projection.

### Rank 5 — `AR2-S03` · does GU's norm-square sit above or below the maximal-compact reduction

`SRC-3`'s entire unboundedness result is graded *"CONDITIONAL on the
load-bearing assumption"* about which pairing the norm-square uses, and its
standing note names the seam directly: *"whether GU's norm-square sits above or
below the Cartan reduction — which is SG4/Lane-1 property."* `CG-1`'s next gate
is the same datum, framed as *"the smallest datum that would settle everything
left open"*, and it is a **question to the source, not a computation**. The
steward routed it. `SRC-4` then kept it live and added a second undeclared
composite, `kappa_1 * flat_1 >= 0`.

Four independent flags; the two horns give opposite verdicts on a filed result.
Owner: SG4 / Lane 1. Cost: one source sentence if it exists; unbounded if not.

**Hazard check.** `SC-GEO-58` (`disavowed-by-source`) records that the source
denies a separate Higgs. This seam is *not* about that object: `SRC-2`
established the Mexican hat is automatic in the source's own curvature
mechanism, and `SRC-3`/`SRC-4` ask whether that potential is bounded below.
Source-native, correctly aimed.

### Rank 6 — `AR2-S05` · do the ten annihilated `s^*`-kernel form legs reappear as independent 4D fields

`MD-1`: the contraction is lossy, annihilating a 10-dimensional space of form
legs, and *"whether they reappear as independent 4D fields is a dynamical
question about the action and the section's own equation of motion, and is not
decided here."* `LA-8` then **rests a verdict on that openness**: it refuses both
`PROVEN_UNSUPPLYABLE` and `PROVEN_UNABLE_BY_CURRENT_ACTION` for `RA-E2`
precisely because `MD-1` left it open. Two flags; a filed reason-kind depends on
it. Owner: whoever supplies the action (SG4). Cost: needs the action.

---

### Escalated, cheap, and dropped out of the day's consolidation

Not load-bearing enough to rank above, but each is owned, each is small, and
none appears in `bd-disposition-packet-2026-08-15.md`:

- **`AR2-S08` — the `LT-SM3b` successor question.** `LA-1` §6.2: `AC-G1`,
  adjudicated `STALE_PREMISE`, got `row_status: SUPERSEDED` plus a successor;
  `LT-SM3b`, also `STALE_PREMISE`, carries a live `distance` with neither. *"This
  channel could not tell which … and declined to mint a row."* **`OT-2` did not
  resolve this.** `OT-2` is about `LT-SM3b` and answers a different question —
  whether `OWN` is the right instrument — and contains no occurrence of
  `successor`, `AC-G1` or `row_status` (asserted negatively). Easy to
  mis-credit; the probe fires if anyone does.
- **`AR2-S09` — the CB-A `+11` constraint surplus overcounts by 5.** `LA-1` §6.3;
  referenced by `LA-4` and `LA-9` as already-known and separately filed; enacted
  by nobody.
- **`AR2-S10` — decide `coupled_to`.** `LA-9` §3.1: two edges are waiting on the
  schema and neither can be filed without it. Owner-only.
- **`AR2-S11` — the 2021 draft PDF is not in the checkout.** The base-duality
  README carries it as a known limit: every draft quotation is register- or
  extraction-mediated, *"the same curated surface that carried a refuted clause
  into a mandatory method."* The steward independently flagged an adjacent
  defect: the copy marked `doc_type: primary_source` drops a sentence present in
  the drafts copy, flipping a passage from concession-only to
  concession-plus-endorsement. Two flags on one root: **the derived source layer
  is lossy and is what everything is read against.**

### `OPEN` but not worklist — author-declared non-dependence, or tracked elsewhere

`AR2-S12` SHIAB selector: which constraint GU earns (J-commutation → family
dim 8, full `Sp(64)`-equivariance → 4) — `canon/shiab-existence-cl95.md` says
*"not adjudicated here"* and folds it into the tracked-OPEN selector question.
`AR2-S13` `PHI-2`'s carrier bit — `canon/carrier-bit-decision-campaign-RESULTS.md`
independently records *"the bit is NOT decided"* and that SG4 is the sole
decider; tracked, not forgotten. `AR2-S14` `PHI-2`'s Euler fork (`e ∧ Tr F` as a
sixth 4D channel, rank 5 → 6) — *"carried as a fork because §5 shows the verdict
does not depend on it."* `AR2-S15` `MD-1`'s uncertified `R`-irreducibility of the
`30` — *"Nothing in the result depends on it."* `AR2-S16` `CC-1`'s Layer-0
`eps` vs `Ω¹(ad)` fork — *"Every result below is indifferent to that fork, which
is why it was not adjudicated here."* `AR2-S17` `BD-B`'s three-domain fibre-algebra
retyping — flagged by the base-duality README and again by `BD-D`, both stating
their results are horn-independent.

Each of these has the **negative consequence clause**. That is a mechanical
signal and it is what keeps them out of the queue.

## 4. The classes that must NOT be mined for work

This is the section the sweep exists to produce. Each was raised as a seam by
somebody and is dead.

- **`AR2-S22` `REFUTED` — "vertical connection components appear as 4D scalars
  after reduction."** Withdrawn from `source-native-comparator-routing.md`
  itself, with the withdrawal preserved in place. Refuted twice (`MD-1` 67/67:
  the observation reduction is a **contraction, not a projection**, so an
  ad-valued one-form descends to a one-form; `LA-8` 78/78: both horns give 45
  and 1 against the 450 the clause implied, both with zero doublets), and the
  premise is disavowed by the source: *"It's not extra dimensions. It's not
  Kaluza Klein."* Any KK-scalar-descent seam is this clause returning.
- **`AR2-S23` `DISAVOWED` — the standard SO(10) `126`-VEV route.** `SC-GEO-58` is
  `disavowed-by-source`: *"there's no Higgs. The Higgs is an illusion."* The
  `MJ`/`PV`/`BD`/`SG4` arc closed the comparator; the channel README records the
  arc as **re-aimed, not retracted**. `SRC-1/2/3` are the source-native
  successor. A "find the missing `126` carrier" task is a dead route.
- **`AR2-S21` `SUPERSEDED` — "the 24 `p` directions are not disposed of."** Real
  when `PV-2` left it and `MV-1` cited it. `CG-1` then established that `p` is a
  **declared coset, not a gauge sector**, and the channel README states that any
  reading treating the 24 as a ghost sector is wrong. The question did not get
  answered; it stopped being the question.
- **`AR2-S18/S19/S20` `RESOLVED`.** `LA-6` §5.2's terminal-pair coupling →
  `OT-2` (*"now resolved, and confirmed — independently, on a different
  classifier"*), the case that motivated this sweep. `PV-1`'s two undecided
  readings → `PV-2` (*"the first reading fails"*). `BD-A`'s H5 escape hatch →
  `BD-D`, which closes it *against the brief's own hypothesis*.

**`AR2-S07` `UNTYPED`, with the reason.** `bd-disposition-packet` §1 records
*"**Open and NOT settled here:** whether the object belongs in `rows` at all"*
for `LT-GR6b`/`b9_STAT`, and `LA-11` flagged it against itself. I cannot type it,
because **`BD-D` is in neither index**: the base-duality README's delta table
lists `bd-a`, `bd-b`, `bd-c` only, and the disposition packet cites `bd-c` but
not `bd-d`. `BD-D` re-types the obstruction (the quotient cures the base, not the
fibre) after the packet reached its verdict. Whether the `rows`-membership
question survives that re-typing is an owner decision made on evidence the
consolidating artifact did not have. Guessing would be worse than the `UNTYPED`.

## 5. The detection signature

A **load-bearing deferral** has four mechanical parts. All four are required.

1. **A performative non-resolution operator, artifact-scoped.** The phrase ends
   in a self-locator (`here`, `in this artifact`, `by this gate`) or is an
   explicit transfer (`deferred to`, `flagged for <owner>`, `escalated to`). The
   self-locator is the whole discriminator against ambient state language:
   *"X is open"* is a fact about the world and occurs 2306 times; *"I did not
   decide X"* is a speech act with a residue and occurs 315 times.
2. **A greppable named object** in the same sentence or the one before: a row id
   (`RA-C1`), a fork name (`SOLDERED-AD`), a register id (`SC-…`), a file path, a
   section reference. Without it the seam cannot be re-found, and an unre-findable
   deferral is not work.
3. **A named owner-of-record**: *"flagged for the integrator"*, *"SG4/Lane-1
   property"*, *"PHI-2's author decides"*, *"escalated to the canonical owner"*.
   Unowned deferrals are caveats.
4. **A consequence clause binding the artifact's own result to the seam** —
   `load-bearing`, `conditional on`, `if this is wrong`, `the verdict depends
   on`, `corrupts a published result`. This clause has an equally mechanical
   **negative form** that is just as decisive: *"the verdict does not depend on
   it"*, *"nothing in the result depends on it"*, *"indifferent to that fork"*,
   *"what survives regardless"*. Its presence types the item ROUTINE.

```
(1) & (2) & (3) & (4-positive)  ->  load-bearing deferral   -> worklist
(1) & (2) & (4-negative)        ->  routine caveat          -> catalogue only
(1) without (2)                 ->  unusable                -> discard
```

Two structural amplifiers, not required but strongly predictive: the deferral
sits under a `Weakest seam` heading (46 files carry one; every worklist item
above rank 3 was found through one), and it is flagged by **two or more
independent artifacts** (14 of 23 catalogued seams; every rank-1-to-5 item).

**False positives, named, in measured order of size.**

- **Process flags.** `flagged for hostile verify`, `flagged for independent
  citation-check`, `flagged for the wave's own check`. 68 repo-wide `flagged
  for` occurrences and most are literature or workflow routing: clauses 1–3
  fire, clause 4 does not, and the named object is a citation rather than a
  research seam. Largest false-positive class by a wide margin.
- **Claim-ceiling sections.** `Claim ceiling` appears in 83 files. It contains
  `not X here` constructions but the author never attempted X; a ceiling names
  something never begun, a deferral names something begun and abandoned and
  usually carries a reason. Excluding ceilings by default is what keeps the
  worklist at 6 instead of ~40.
- **Propagated citations.** *"MD-1 explicitly leaves open…"* is evidence of
  convergence, not a new seam. Failing to deduplicate to the originating artifact
  inflates the multiply-flagged count, which is the number a reader trusts most.
- **Standing open-lists.** *"Zero-neighborhood coverage, surjectivity, RSAP,
  source selection and global gluing remain open"* — boilerplate repeated in
  every K-series headline. This is the bulk of the 2306.
- **The one false NEGATIVE, measured.** Wrap-blindness: 16 of 315 lost repo-wide.
  Normalize whitespace before matching or the detector silently under-reports.

## 6. HOSTILE REVIEW — my own measured error rate

I sampled all 6 worklist items and 4 of the 10 non-worklist `OPEN` items — **10
of 16 `OPEN`** — and re-hunted each for a resolution anywhere in the repository
under any name.

**Mis-typing errors surviving to this list: 0 of 10.** No sampled `OPEN` item
was in fact resolved elsewhere. That is a small sample and I do not present it
as a low error rate; it is the number I measured.

**Near-miss, recorded because it nearly shipped.** I initially expected `OT-2` to
have resolved `AR2-S08` (`LT-SM3b`'s successor question) on the strength of its
title. It did not — it answers a different question about the same row — and the
mistake would have been invisible in a summary. The probe now asserts the three
absent tokens so the same error cannot be made silently.

**Completeness errors: 2 of 10 sampled.** Both are recall, not typing.
(i) `AR2-S01`'s flag count was 5 when I first wrote it and is 7: `LA-4` and
`PHI-1` also decline the fork, and I found them only on the adversarial pass.
(ii) The sweep missed `BD-D`'s wrapped `not adjudicated\nhere` entirely — the
wrap-blindness defect — which added a second flag to `AR2-S17`. **Recall is this
sweep's weak side, not precision.**

**What I did not check, stated plainly.** Of 315 repo-wide CORE occurrences, 24
are in the joe-directed tree and were triaged individually. The other 291 were
swept mechanically and filtered by the strict signature (consequence clause plus
named object); I read **13** of them. Coverage of pre-August seams in
`explorations/` is therefore low, and the `OPEN` count of 16 is a floor on the
repository, not a census of it. The old material is also the material most
likely to be `SUPERSEDED` rather than `OPEN`, which cuts the other way.

**Vacuity check on my own controls.** All 13 planted controls drive exit 1,
including the five that plant false facts about the world rather than false
numbers. The negative assertions — the ones carrying the `OPEN` typings — are
covered by three of those five.

**A defect the shared checkout found for me.** The census was written before
`AR-1` existed and silently included it the moment it landed, reporting 61
joe-directed occurrences instead of 24 and collapsing the hedge-to-core ratio
below its floor. The probe caught it because the counts are asserted exactly
rather than reported. Had this been a floor-only check, the artifact would have
shipped a wrong census with a green certificate. **`AR-1` and this file were
written concurrently and independently and have not been reconciled with each
other**; a reader should expect overlap between AR-1's dropped commitments and
this file's deferrals, and should not treat agreement between them as
independent corroboration until someone checks whether they read the same
surfaces.

## 7. POSTFLIGHT — six lenses, run on this artifact

**Lens Q1 — strongest overclaim available here, and it is refused.** The
available overclaim is *"the repository has 16 forgotten open seams."* Refused
on two counts: 10 of the 16 are explicitly not load-bearing or already tracked
on a canon surface, and the 16 is a floor over an under-read corpus. The honest
headline is **six load-bearing deferrals, four of them already routed by the
steward yesterday, one of which changed stakes afterwards.**

**Lens Q2 — the strongest contrary reading, which I cannot refute.** *This
catalogue is a re-index of the steward pass plus the two channel READMEs, and
the only genuinely new facts are the resolution checks.* Substantially true.
`AR2-S01`, `S03`, `S04` and `S11` were all routed by the steward on 2026-08-14.
What this file adds on those four is: they are **still** unresolved (checked, not
assumed), `S01`'s stakes rose after routing, and `S02`/`S08`/`S09`/`S10` fell out
of the day's own consolidation packet. Whether that is worth an artifact is a
judgment I cannot make from inside it.

**Lens Q3 — weakest seam of this construction.** The **owner-of-record clause**
is the softest of the four detection criteria. "SG4/Lane-1 property" is an owner
in name; nothing routes to it, nothing dequeues from it, and three worklist items
terminate there. If SG4 is a name for *"nobody"*, then ranks 4, 5 and 6 are not
work items at all — they are a statement that the channel has hit its wall three
times from three directions. I record that reading rather than resolving it.

**Lens Q4 — what a hostile reader should attack next in this artifact.** The
`UNTYPED` on `AR2-S07`. I justified it by `BD-D`'s absence from both indices,
which is a *process* fact, not a mathematical one. A reader who simply reads
`BD-D` may find it settles the question in one direction, in which case my
`UNTYPED` is laziness dressed as rigour. That is the cheapest attack available
and it should be run.

**Lens Q5 — resurrection audit, run against my own output.** Does any worklist
item revive a route the source disavows? Checked one by one against the register:
S04 and S02 are internal grade/typing defects with no source claim; S06 is a
process-gate classification; S01 and S05 are about the observation contraction,
source-native and explicitly *not* the withdrawn KK clause; S03 is about the
source's own norm-square and explicitly *not* the disavowed separate Higgs. The
three dead classes are given their own rows in §4 with the disavowal quoted, so
a reader mining this file for work must step over them deliberately.

**Lens Q6 — decision usefulness: does this change what to work on?** Modestly,
and in one direction: it **re-ranks** rather than adds. The concrete deltas are
(a) `SOLDERED-AD` should be re-priced upward because `PHI-2` moved it, (b) the
`RA-C1`/`AC-C2` seam now corrupts a published number and should move above the
routine ledger hygiene it currently sits with, and (c) four escalations dropped
out of the day's consolidation and can be swept back in for the cost of reading
`LA-1` §6 and `LA-9` §5. Nothing here justifies a new workstream.

## 8. Claim ceiling

**Established:** an exact census of two deferral vocabularies over 3656 markdown
files; a typed catalogue of 23 seams with resolution checked for each; a measured
recall defect in naive substring sweeping (16 of 315); a four-clause detection
signature with its false-positive classes named and sized.

**Not established:** that 16 is the repository's true `OPEN` count (it is a floor
over an under-read corpus — 13 of 291 non-joe-directed occurrences read); that
any catalogued seam is *worth* closing; any physics, any grade change, any
verdict, any ledger movement, any statement about whether GU is correct. No
source claim is adjudicated. The `UNTYPED` row is untyped on purpose.

## 9. REPRODUCE

```
_local/cas-venv/bin/python tests/channel-swings/joe_directed_ar2_deferral_archaeology.py
_local/cas-venv/bin/python tests/channel-swings/joe_directed_ar2_deferral_archaeology.py --selftest
```

**Certificate: 13/13 checks, exit 0. Failure path exercised: 13/13 planted
controls each drive exit 1.** Controls: 7 mutate asserted counts
(`census_occurrences` 24→23, `census_files` 48→47, `phrase_table`, `repo_floor`
315→400, `type_counts` 16→15, `worklist` 6→5, `multiply_flagged` 14→13);
1 asserts the wrap-blind and normalized counts are equal; 5 plant **false facts
about the world** — that the disposition packet resolves `SOLDERED-AD`, that
`OT-2` answers the `LT-SM3b` successor question, that the VZ chain was repaired
against `MD-1`, that `LA-6` never wrote *"Not resolved here"*, and that the hedge
vocabulary is no larger than the core vocabulary. No float is asserted anywhere.
Repo-wide numbers are asserted as floors and labelled as floors, because the
checkout is shared.
