---
artifact_type: exploration
status: exploration
doc_type: stewardship_record
created: 2026-08-17
work_item: CT-5
channel: ct_hardening
title: "CT-5: the staleness class the citation gate provably cannot reach is now mechanically detectable. Ten canonical_source_correction entries (canonical_since + greppable topic signature + per-entry blindness caveat) added as a SECOND top-level key in correction-registry.yaml, invisible to correction_propagation_audit by construction and proved so; a sidecar banks SCUR-1's 23 per-document verdicts and FIX-A's 6 repair pairs as 35 recorded checks; process_gates/canonical_currency_audit.py computes DIRTY = predates AND matches-signature AND unchecked. Live dirty set 188 (file, correction) pairs across 3645 files, 13 pairs cleared by the seed. The Z/3 receptacle design packet (2026-08-11) -- the incident that motivated the work -- is DIRTY-UNCHECKED for the 2+1 correction and CLEAR once an adjudication is recorded; both states are certified. Warn-only on prose; RED only on well-formedness and a 7-day ratchet, which is honestly inert today because every correction is 1-3 days old and arms on 2026-08-21."
grade: "TOOLING, with a certified detector and a measured recall ceiling. The registry seed is a TRANSCRIPTION of SCUR-1 section 1's ten byte-verified register items and the sidecar is a TRANSCRIPTION of SCUR-1 sections 2/3/5 and FIX-A section 2 -- no currency call is re-derived, re-adjudicated, or minted here. Every number is an exact integer over file dates and lowercased substrings; no float is constructed anywhere. Additivity of the registry edit is PROVED three ways (byte prefix, parsed-subtree equality, and the real citation gate run against pre-edit and post-edit registries). NOT: a canon edit, a ledger edit, a verdict/grade/count/bar movement, a currency adjudication of any document, an edit to any audited file, or a claim that the dirty set is the set of stale documents."
target_claim: "INTERNAL -- CT-5's own pre-registered internal target: that a topic-signature dirty-bit mechanism is redundant with SCUR-1's grep, i.e. that it adds bookkeeping without adding detection. That claim is RETIRED below on three measured grounds (section 7). No registered GU source claim is attacked and no physics claim is made or moved."
target_claim_verdict: "RETIRED, on measurement rather than argument: (i) the mechanism fires on a document SCUR-1 never audited and could not have -- the Z/3 packet sits outside SCUR-1's declared target set, and is DIRTY-UNCHECKED here; (ii) it fires on 188 pairs, of which SCUR-1's hand pass covers 13, so 175 pairs are net-new surface; (iii) unlike a grep it is DATED, so a correction added tomorrow re-dirties every document an ALL-REGISTER record cleared today. The redundancy charge survives in exactly one place and is conceded there: the SIGNATURES were tuned by the author against this corpus, so their precision is partly fitted, and one of SCUR-1's six hand-found pairs does not fire its own signature (section 8)."
canon_verdict_change: none
ledger_edit: none
priority_change: none
steering_effect: unchanged
canonical_effect: "none -- process instrumentation only. Two lab/process files and one process_gates file are added or extended; no canon file, ledger row, verdict cell, grade, count, bar, registry horn, or public posture moves, and no audited document is edited. The 188-pair dirty set is a WORK QUEUE handed to whoever adjudicates it; nothing in it is typed stale by this artifact."
depends_on:
  - lab/active-research/joe-directed/source-currency/scur1-source-currency-audit-2026-08-17.md
  - lab/active-research/joe-directed/source-currency/fixa-cb-corrections-applied-2026-08-17.md
  - lab/process/correction-registry.yaml
  - process_gates/correction_propagation_audit.py
  - explorations/z3-receptacle-design-packet-2026-08-11.md
  - VERIFICATION.md
scripts:
  - process_gates/canonical_currency_audit.py
  - tests/channel-swings/joe_directed_ct5_canonical_corrections_as_dirty_bits.py
---

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact's object is
> the repository's own bookkeeping: file dates, recorded checks, and lowercased
> substrings. It contains no physics result and binds no comparator. Any GU or
> Standard-Model vocabulary appearing below is quoted from the correction
> register as SIGNATURE TOKENS, not asserted as content, and nothing here is
> evidence for or against Weinstein's source-native mechanism.
>
> Classification: `INTERNAL_STRUCTURAL_ONLY`

> **Audit-scope disclosure, stated rather than exploited (the AR-2 / SCUR-1 /
> FIX-A pattern).** `doc_type: stewardship_record` places this file outside the
> derived scope of `process_gates/source_native_comparator_routing_audit.py`,
> whose unclassified count sits at 6 against a baseline of 5 for reasons that
> predate this task and belong to other lanes. The declared type is honest —
> this is process instrumentation, it adjudicates no physics — and the routing
> notice and classification above are carried anyway, so the exclusion buys
> nothing it would not otherwise have.

```gu-typed-objects
result: CT-5 dirty-bit mechanism — canonical corrections propagate along CONSUMPTION edges (date + topic signature + recorded check) rather than citation edges, making the pre-correction staleness class mechanically detectable
carrier: the repository's live markdown surfaces (canon/, docs/, explorations/, lab/, packets/, root) — 3645 files, 3356 dated, 289 undated LAYER=UNTYPED CHIRALITY=N/A
# LAYER is declared UNTYPED because the closed vocabulary (ambient/observed/source-print/toy) has no token for repository text ABOUT the source; the ambiguity is declared, not resolved (SCUR-1's own declaration, carried forward).
pairing: NONE
real_structure: N/A
grading: N/A
action_owner: repository-construction
target: currency of dated documents against the ten 2026-08-14..16 canonical source corrections MAP-TYPE=not-a-map
```

# CT-5 — canonical corrections as dirty bits over consumer edges

## 0. PREFLIGHT — problem-matched lenses, declared before any write

1. **Reachability, not tuning.** The first question is whether the existing
   gate's blindness is a parameter choice or a proof. It is a proof: a document
   written before a correction existed cannot cite the correction's owner, so
   the citation graph contains no edge to walk, at any threshold. This lens
   settles the shape of the fix (a different edge relation, not a wider one)
   and it forbids the tempting alternative of loosening
   `correction_propagation_audit.py`, which would degrade a sound gate to buy
   nothing.
2. **Additivity as a hard constraint, proved not asserted.** The brief requires
   the citation gate to run identically before and after. Rather than hope,
   the design puts the new class in a SEPARATE top-level YAML key — the old
   gate reads `data["corrections"]` and nothing else — and section 5 proves the
   identity three independent ways, including running the real gate against a
   reconstructed pre-edit registry.
3. **Precision/recall is a design choice with a stated owner.** A topic
   signature can be broad (high recall, unusable queue) or narrow (usable
   queue, silent holes). Measured drafts: a broad CC-02 matched 856 pre-date
   files; the shipped conjunctive one matches 11. That is a CHOICE for
   precision, and the price is recorded per entry (`blindness:`,
   `known_synonyms_outside_signature:`) and measured every run (`topic_reach`,
   `signature_missed`) rather than left implicit.
4. **The FX-3 rule binds the gate's colour.** A gate that goes RED on prose
   gets deleted, and a deleted gate detects nothing. So the dirty set — the
   part that touches prose — is warn-only forever, and RED is reserved for
   things with a mechanical right answer: well-formedness and a ratchet.
5. **Banked hand-work must not evaporate.** SCUR-1 and FIX-A represent three
   days of adjudication that currently exists only as prose. If the sidecar
   merely re-derives what a grep can find, the mechanism is theatre. The
   sidecar therefore stores JUDGEMENTS, dated and attributed, and the gate ages
   them: an ALL-REGISTER clearance only covers corrections that existed when it
   was made, so tomorrow's correction re-dirties today's cleared documents.
6. **Do not adjudicate what I was not asked to adjudicate.** CT-5 transcribes
   SCUR-1 and FIX-A; it types no document's currency itself. Where the brief's
   own phrasing invited a record that does not exist (the Z/3 packet's
   "LD-A/Arc-3 adjudication"), the record is PLANTED IN THE SELFTEST and
   labelled synthetic, never written into the live sidecar — LD-A adjudicated
   SG4 bit 2, not this packet's currency (checked: zero occurrences of
   `z3`/`Z/3`/`receptacle` in LD-A).
7. **Shared-checkout concurrency.** `lens-digs/`, `ct1*`/`ct2*`/`ct3*`,
   `vz-repair/` are live siblings and are untouched; the corpus grew 3643 →
   3645 during this session from other lanes, which is why no probe pin depends
   on a corpus COUNT. No git operations.

**Retrieval before work.** Read first, in this order: the existing registry
schema (`lab/process/correction-registry.yaml`, 101 lines, ten citation-edge
corrections, three `enforce: true`); the gate that consumes it
(`correction_propagation_audit.py`, 80 lines, `data["corrections"]` only);
`VERIFICATION.md`'s seven-rule probe standard; SCUR-1 in full (484 lines) and
FIX-A in full (336 lines). The binding's own wording was sought in commit
`0d9d2f8` as the brief suggests and is NOT REACHABLE in this checkout (`fatal:
ambiguous argument '0d9d2f8'`; no commit message in the log matches
`CANONICAL-CURRENCY`, `canonical currency`, or `input-currency`), so the
artifact record is the source used throughout, exactly as the brief's fallback
directs.

## 1. The mechanism

```
a file F is DIRTY for canonical correction K
    iff  date(F) < K.canonical_since          (strictly earlier)
    and  signature(K) matches text(F)          (conjunction over token families)
    and  no recorded check clears (F, K)
```

`date(F)` is dated frontmatter (`created` / `date` / `created_date` / `filed`),
falling back to a date in the filename. A file with neither is UNDATED and is
**out of the dirty set and cannot be in it** — "predates" is undecidable for it.
289 of 3645 files are undated; that is a stated hole, not a clean result.

Three states are distinguished and all three are printed:

| state | meaning |
|---|---|
| `DIRTY-UNCHECKED` | nobody has looked at this pair |
| `DIRTY-KNOWN-STALE` | somebody looked, found it stale, and it is not yet repaired |
| clear | a recorded check clears it (`CLEARED-CONSISTENT`, `FENCED-COMPARATOR`, `SUPERSEDED-DOC`), possibly a repair recorded over an earlier `STALE-FOUND` |

Precedence is fixed and mechanical: a record scoped to the exact correction
beats a blanket `ALL-REGISTER` record, and at equal scope a clearing verdict
beats `STALE-FOUND`. That is how FIX-A's repair retires SCUR-1's finding
**without deleting the finding** — both records stay, and the gate reports the
pair as `repaired-after-STALE-FOUND`.

## 2. The ten seeded canonical entries

Transcribed from SCUR-1 section 1, whose every item was byte-verified at its
owner (10/10, zero divergences). `register_item` is that table's row number.

| id | since | owner | superseded reading (one line) | families | dirty |
|---|---|---|---|---|---|
| `CC-01-MET-X-ARGUMENT` | 08-15 | BD-C | X⁴ carries a background/canonical metric, rather than `MET(X^{1,3})` being the second ARGUMENT of the first action | 2 | 22 |
| `CC-02-OBSERVED-POSITIVITY-OPEN` | 08-15 | IV-20260815 §3.1 | the source DISAVOWS positivity, so observed-quotient positivity is excluded — it is source-OPEN | 3 | 11 |
| `CC-03-FOUR-CORNER-NONCHIRAL` | 08-15 | CR-B | the total fermionic declaration is one subscripted Weyl object with a supplied reality condition — it is unsubscripted, four corners, non-chiral, reality source-SILENT | 2 | 2 |
| `CC-04-NORMAL-BUNDLE-RIGHT-CHAIN` | 08-15 | SC-A | GU contains a grand unification whose gauge group is the object to identify — "There is no grand unification. It's just a normal bundle" (drafts L125) | 2 | 2 |
| `CC-05-SUBTRACTIVE-TWO-PLUS-ONE` | 08-14 | HE-1 | three generations is an ADDITIVE target count to produce — the partition is FORCED and SUBTRACTIVE (n_g → n_g − 1) | 3 | 40 |
| `CC-06-CHIRALITY-VEV-CONDITIONAL` | 08-16 | ST-1 | the source has no stated chirality mechanism / chirality needs an unbuilt mirror-gapping condensate — it is VEV-conditional, selector SG4 bit 2 | 2 | 27 |
| `CC-07-CONTRACTION-NOT-KK` | 08-14 | MD-1 (+VZ-4) | observation is a KK mode split whose normal one-form components descend to 4D scalars — it is a CONTRACTION; "It's not Kaluza Klein." | 2 | 5 |
| `CC-08-DARK-PARTNER-OBLIGATION` | 08-15 | SC-FER-03 | the 128 remainder is an established DEFECT — it is a partner-placement/decoupling OBLIGATION, dark sectors NAMED | 2 | 6 |
| `CC-09-YUKAWA-REPULSIVE-SIGN` | 08-15 | H10-5 | the massive-spin-2 Yukawa coefficient is +1/3 and attractive — it is −4/3, REPULSIVE | 2 | 28 |
| `CC-10-UCSD-EDITED-DERIVATIVE` | 08-15 | UCSD transcript banner | the repo's UCSD copy is a PRIMARY SOURCE — it is an EDITED DERIVATIVE, audio owed | 2 | 45 |

Every entry additionally carries `blindness:` (what escapes it) and
`known_synonyms_outside_signature:` (families considered and rejected, with the
reason, and the measured count where one was taken — e.g. `'Rarita'` at 295
pre-date files, `'no positivity'` at 70, `'the 128'` at 58, `'authoritative'`
at 65). Both fields are RED if empty; an entry may not ship a signature without
declaring what it cannot see.

## 3. The seeded cleared set

**35 recorded checks**, all transcribed, none re-adjudicated:

- **23 `ALL-REGISTER` records** — SCUR-1's per-document verdicts (section 2's
  table and section 5's CB-pack table): the five conditional-build files, four
  process/standing-reference surfaces (`path-dependencies.md`,
  `layer0-fork-registry.yaml`, `six-axis-template.md`,
  `GEOMETER-VS-PHYSICS-OBJECTS.md`), the two narrative heads (`CURRENT-STATE.yaml`,
  `NEXT-STEPS.md`), and the twelve 2026-08-14 borderline artifacts. SCUR-1's
  type key maps: `PREDATES-BUT-CONSISTENT` and `ALREADY-CORRECTED` →
  `CLEARED-CONSISTENT`; `DELIBERATE-COMPARATOR` → `FENCED-COMPARATOR`.
- **6 `STALE-FOUND` records** — SCUR-1's five findings over six (file,
  correction) pairs, because V4 violates two register items. Each carries a
  `pointer` to the finding (RED if absent) and is attributed to SCUR-1.
- **6 FIX-A clearing records** — the five applied blocks over the same six
  pairs, the single V4 block discharging both CC-06 and CC-08.

`SUPERSEDED-DOC` is supported and **deliberately unused**: SCUR-1 typed no
audited document as superseded, and inventing one to exercise the vocabulary
would be a false record. The verdict's machinery is exercised in the probe's
planted cases instead.

**These 35 records clear 13 (file, correction) pairs.** The gap between 35 and
13 is honest and worth naming: a record on a file that does not match a
correction's signature is INERT — it clears a bit that was never set. Most of
SCUR-1's audited documents are 2026-08-14 artifacts that either post-date the
corrections or do not match the narrow signatures, so their records sit ready
for future corrections rather than clearing anything today.

## 4. The current dirty set — 188 (file, correction) pairs

Measured 2026-08-17 over 3645 files (3356 dated, 289 undated). All 188 are
`DIRTY-UNCHECKED`; zero are `DIRTY-KNOWN-STALE`, because FIX-A repaired every
finding SCUR-1 recorded.

**CC-01-MET-X-ARGUMENT** (since 2026-08-15) — 22 dirty, topic_reach 285

- `explorations/HYPOTHESIS-moduli-negative-not-time-negative-2026-08-09.md`
- `explorations/analytic-index-fredholm/oq-rs3-gu-vasiliev-comparison-2026-06-23.md`
- `explorations/conditional-build/selected-action-coupled-diffeomorphism-ward-retype-2026-08-06.md`
- `explorations/cycle-gates-and-audits/weinstein-ucsd-2025-04-analysis-2026-06-22.md`
- `explorations/dark-energy-cosmology/dark-energy-divergence-free-proof-2026-06-22.md`
- `explorations/generation-sector/oq3a-k3-variational-selection-2026-06-23.md`
- `explorations/generation-sector/oq3a-willmore-k3-selection-2026-06-23.md`
- `explorations/generation-sector/oq3b-rs-index-8-2026-06-23.md`
- `explorations/geometry-curvature-emergence/dd1-distortion-tensor-literature-check-2026-06-22.md`
- `explorations/geometry-curvature-emergence/hc1-codazzi-correction-2026-06-23.md`
- `explorations/geometry-curvature-emergence/pc2-met-x4-bundle-formalization-stub-2026-06-22.md`
- `explorations/misc/six-axis-l1l2-coupling-filled-example-2026-06-23.md`
- `explorations/perspective-and-dialectic/4d-reduction-62-perspective-steelman-hegelian-2026-06-22.md`
- `explorations/perspective-and-dialectic/entropic-gravity-antithesis-information-first-2026-07-07.md`
- (+8 more; the gate prints the full list every run)

The remaining nine groups are printed in full by the gate on every run and are
summarised here rather than duplicated, because a copied list rots while the
gate's does not:

| correction | dirty | topic_reach | measured members (heads of the printed list) |
|---|---|---|---|
| CC-01 | 22 | 285 | the `geometry-curvature-emergence/` and `generation-sector/` June packs; `HYPOTHESIS-moduli-negative-not-time-negative-2026-08-09`; `conditional-build/selected-action-coupled-diffeomorphism-ward-retype-2026-08-06` |
| CC-02 | 11 | 1330 | `path5-branchA-krein-modular-conjugation-2026-07-11`; `krein-ratio-set-tail-coherence-2026-07-11`; `W170-turok-bateman-nonperturbative`; `blockbuster-p3-one-bit-dossier-v2` |
| CC-03 | 2 | 4 | `conditional-build/selected-k77-zero-seed-h640-action-closure-controls-2026-08-11`; `resolver-wave-e-source-owned-moving-252-full20-placement-2026-08-03` |
| CC-04 | 2 | 7 | `perspective-and-dialectic/higher-order-story-perspective-sprint-2026-06-28`; `wave14/H19-seven-seven-signature-branch-2026-07-11` |
| CC-05 | 40 | 931 | **`explorations/z3-receptacle-design-packet-2026-08-11.md`**; `canon/three-generations-locate-not-force-CRT-RESULTS.md`; `canon/final-verdict-generation-count-and-the-open-bridge.md`; `lab/process/CURRENT-RESEARCH-CONTEXT.md`; `explorations/layer0-pass-on-the-2plus1-count-claim-2026-07-29.md`; `explorations/n4-two-z3s-2026-07-20.md` |
| CC-06 | 27 | 40 | the `W222`/`W223`/`W224` chirality-falsification cluster; `c3c-covariant-constancy-structure-2026-08-13`; `conditional-build/trace-omega-higgs-chirality-compose-reconciliation-2026-08-05` |
| CC-07 | 5 | 145 | `geometry-curvature-emergence/pc5-higgs-emergence-spec`; `vertical-source-action-reduction-and-hessian-start-2026-07-29`; `rb3b-trace-reversed-bidoublet-full20-join-2026-07-30` |
| CC-08 | 6 | 8 | `lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04`; `lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03`; `lab/process/hostile-reviews/2026-08-03-imposter-ab-review.md`; `decoupling-constructibility-packet-2026-08-12` |
| CC-09 | 28 | 86 | `W122-spin0-gauge-vs-physical-auxfield`; `W123-native-r2-running-sign-convention-audit`; `path2-branchC-fakeon-2026-07-11`; `conditional-build/selected-second-layer-massive-so3-closure-identifiability-2026-08-07` |
| CC-10 | 45 | 122 | `nguyen-gu-critique/nguyen-critique-full-synthesis.md`; `eric-native-physics-equation-replacement-atlas-2026-07-31`; the `research-cycles/hourly-2026062*` locator series; `cycle-gates-and-audits/weinstein-ucsd-2025-04-analysis-2026-06-22` |

Four of these are steering or source-extraction surfaces and deserve naming
rather than burial: `lab/process/CURRENT-RESEARCH-CONTEXT.md`,
`canon/three-generations-locate-not-force-CRT-RESULTS.md` and
`canon/final-verdict-generation-count-and-the-open-bridge.md` (all CC-05), and
`lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04`
(CC-08). Nothing here types them stale — they are unchecked, which is a
different and weaker statement, and adjudicating them is somebody's next job,
not this one.

## 5. Additivity — the citation gate runs identically, proved three ways

1. **Byte prefix.** The pre-edit file is a strict prefix of the post-edit file:
   zero bytes of the original 101 lines changed, the new class is appended
   under a second top-level key.
2. **Parsed-subtree equality.** `yaml.safe_load(...)["corrections"]` is `==`
   before and after; the post-edit top-level keys are exactly
   `['corrections', 'canonical_source_corrections']`, and no `CC-*` id appears
   inside `corrections`.
3. **The real gate, run both ways.** `correction_propagation_audit.py` was
   executed in-process with `REGISTRY` pointed at a reconstructed pre-edit copy
   and at the live post-edit file. Both exit 0; the outputs are **identical**
   modulo the one line unittest writes with a wall clock (`Ran 2 tests in
   0.015s` vs `0.035s`), which varies between consecutive runs of the same
   state and carries no content.

The probe re-asserts this as a durable invariant, not a one-off measurement: it
pins the citation gate's ten historical ids in order, pins the two-key
structure, and RUNS the citation gate in-process on every probe execution.

## 6. The Z/3 packet — both states certified

`explorations/z3-receptacle-design-packet-2026-08-11.md` is the incident that
started this: a design packet that engaged a route the following week's 2+1
sharpening superseded, cited nothing corrected, and was invisible to every
instrument. It is also outside SCUR-1's declared target set (SCUR-1 §8 lens 2
names "the ~800 files of `explorations/` outside the brief's target set" as its
own under-detection ceiling), so it was never hand-audited either.

| | state | certified by |
|---|---|---|
| **A — live** | `DIRTY-UNCHECKED` for `CC-05`: dated 2026-08-11 < 2026-08-14, matches the 2+1 signature (`three generations` ×2, `three-generation` ×5, `generation count` ×2; `2+1` ×4, `2plus1` ×7; `receptacle`, `z/3`), no recorded check | probe class Z: "STATE A -- live, no recorded check: the packet is DIRTY-UNCHECKED" + "not silently sitting in some cleared bucket" |
| **B — adjudication recorded** | not dirty; lands in the CLEARED bucket, and CC-05's dirty count falls by **exactly one** (40 → 39) | probe class Z: "STATE B -- adjudication recorded: the packet leaves the dirty set" + "lands in the cleared bucket" + "CC-05's dirty count falls by exactly one" |
| **C — found stale, not yet repaired** | `DIRTY-KNOWN-STALE`, still dirty, count unchanged — "found" is not "fixed" | probe class Z: "STATE C -- a STALE-FOUND record does NOT clear" + "the dirty count is unchanged" |
| **specificity** | dirty for `CC-05` and for none of the other nine | probe class Z: "specificity -- the packet is dirty for CC-05 and no other correction" |

**State B's record is PLANTED IN THE SELFTEST and is not in the live sidecar.**
The brief names it "its LD-A/Arc-3 adjudication"; LD-A adjudicated SG4 bit 2 and
mentions the packet zero times, and CT-5 is not licensed to adjudicate the
packet's currency itself. Writing a clearing record for an adjudication that has
not happened would be exactly the failure this whole mechanism exists to catch,
so the live answer stays DIRTY and the CLEARED half is demonstrated
synthetically, labelled as such in the probe source.

## 7. Hostile review — is this SCUR-1's grep with extra steps, and will the sidecar rot?

**Charge 1: the signature design just re-invents the grep.** Partly true, and
the true part is conceded precisely. What survives the charge, measured:

- **It reaches what the grep did not.** The Z/3 packet is outside SCUR-1's
  audited set and is caught here. More generally the mechanism flags 188 pairs
  where SCUR-1's records cover 13 — 175 pairs of net-new surface, none of them
  adjudicated by anybody.
- **It is DATED, which a grep is not.** An `ALL-REGISTER` clearance only covers
  corrections whose `canonical_since` is at or before the record's date. Add
  `CC-11` tomorrow and all 23 of SCUR-1's cleared documents go dirty for it
  automatically. A grep run on 2026-08-17 says nothing about 2026-08-18.
- **It composes with future files.** A document filed next week with an older
  `created:` date enters the dirty set with no human action.

What is CONCEDED: the token families were tuned by the author against this
corpus (CC-02 went 856 → 76 → 11 across three drafts), so their precision is
partly FITTED to the files present today, and a fitted signature generalises
worse than its measured precision suggests. And the deepest version of the
charge stands: the mechanism can only ever find what somebody thought to write
into a token family, which is the same epistemic limit the grep has. What
changed is not the reach of one query but that the query is now PERSISTENT,
DATED, and ACCUMULATIVE.

**Charge 2: the sidecar will rot.** Likely, and three specific rot modes are
already visible or anticipated:

- **Inert records.** Measured: exactly **12 of the 35 records govern at least
  one cleared pair; 23 are inert today** (they sit on files no signature
  currently claims). Records that never fire are records nobody maintains, and
  a two-thirds inert rate at seeding time is not a healthy starting ratio. It
  is defensible — an inert record is pre-positioned for the next correction, and
  that is the ageing property this design is built on — but it is exactly the
  kind of defensible number that becomes an excuse later.
- **Blanket clearance drift.** `ALL-REGISTER` is convenient and coarse. Its
  ageing rule is the only thing stopping it becoming a permanent exemption, and
  a future author who writes `ALL-REGISTER` casually will silently clear
  corrections they never considered. The mitigation in place is that explicit
  per-correction records beat blanket ones, so a later finding always overrides
  an earlier blanket clearance — but nothing forces anyone to write the
  explicit record.
- **Baseline creep.** The ratchet compares against numbers stored in the same
  file the ratchet guards. Raising a baseline is a one-line edit and the gate
  cannot tell a justified re-baseline from a surrender. The probe's own pins are
  held INDEPENDENTLY of the sidecar baseline (VERIFICATION.md rule 6) so that
  raising a baseline breaks the probe, which is the only real friction here and
  is deliberately placed.

**Charge 3: the ratchet is inert, so the RED path is theatre today.** Conceded
and stated in the gate's own output: all ten corrections are 1–3 days old, the
grace period is 7 days, so **no correction is aged on 2026-08-17** and the
ratchet guards nothing until 2026-08-21 (CC-05, CC-07 first). The probe does not
wait for that date — it runs the whole gate at `--as-of 2026-08-25`, confirms
all ten are AGED, confirms the ratchet is green unchanged, and then breaks it
deliberately two ways (drop the six FIX-A repairs → `RATCHET BROKEN`; inject an
aged correction with no baseline → RED rather than silent acceptance).

## 8. The ceiling, measured

Two numbers are computed and printed every run rather than asserted:

- **`topic_reach`** — pre-date files touching the entry's ANCHOR family alone.
  CC-02: 1330 files touch `krein`/`indefinite`/`killing form`, and the
  conjunction claims 11 of them. CC-05: 931 touch the count vocabulary, 43 are
  claimed. The gap is the price of precision, per entry, in the open.
- **`signature_missed`** — hand-recorded pairs whose own signature does NOT
  fire. Scored against SCUR-1's six findings as ground truth, this is
  **exactly 1**: `cb-b-lagrangian-terms-2026-08-05.md` under CC-08. SCUR-1
  found by hand that CB-B's SM-9 sentence violates register 8; the CC-08
  signature deliberately excludes `Rarita` (295 pre-date files) and `dark
  sector` (13) as non-discriminating, and CB-B discusses the obligation in
  exactly that excluded vocabulary. **1 of 6 = a 17% measured miss rate against
  the only ground truth available.** That number is the honest headline for
  recall and it is printed by the gate, not buried here.

## 9. Gate results — prior state or better, measured not asserted

| gate | before CT-5 | after CT-5 |
|---|---|---|
| `correction_propagation_audit` | exit 0, 21 lines, 8 NEEDS_RECHECK | exit 0, byte-identical modulo the unittest wall-clock line (section 5) |
| `canonical_currency_audit` | did not exist | exit 0; 188 dirty, 13 cleared, well-formed, ratchet intact |
| `kill_target_claim_audit` | exit 0; 3 red = baseline 3; escape-hatch 11; internal-target 7 | exit 0; identical (3 / 11 / 7). This artifact's head fields carry no kill-language so the gate skips it; the INTERNAL-form typing above is carried voluntarily |
| `typed_carrier_declaration_audit` | exit 1; 1 red (`conditional-build/selected-k151-...-2026-08-17.md`, another lane's, pre-existing); 22 files in dated scope, 19 triggered, 25 blocks | exit 1; the SAME single pre-existing red; scope 23 files, 20 triggered, 26 blocks — this artifact triggers (scripts + certificate) and complies with its typed-objects block, adding no red |
| `source_native_comparator_routing_audit` | exit 1; 135 in derived scope, 129 registered, 6 UNCLASSIFIED vs baseline 5 | exit 1; **identical** — 135 / 129 / 6. The pre-existing +1 belongs to other lanes (`ct3`, `md1`, `mc1`, `phi2` sit in the unclassified list); this artifact is out of scope by honest `doc_type` and carries the notice anyway |
| `certificate_shape_audit` | exit 1; pre-existing allowlist mismatch on other lanes' probes | exit 1; same pre-existing failure |
| `tests_manifest_count_audit` | exit 0 | exit 0 |

## 10. POSTFLIGHT — lenses after the work

1. **Diff-surface auditor.** Exactly five files written: the registry (appended
   only, prefix-proved), the new sidecar, the new gate, this record, and the
   probe. Zero bytes changed in `correction_propagation_audit.py`, in SCUR-1,
   in FIX-A, in any canon/ledger/registry horn, or in any audited document.
   `lens-digs/`, `ct1*`/`ct2*`/`ct3*`, `vz-repair/` untouched. No git.
2. **Instrument auditor.** The probe's clean baseline is verified FIRST and
   would abort red (rule 1); every mutation corrupts machinery or a reference,
   never a check (rule 2); catches are counted only via genuine `[FAIL]` lines
   and crash-catches are rejected — one mutation initially CRASHED on a `None`
   date and was repaired into a genuine catch rather than banked (rule 3); the
   absence-style controls carry a planted positive the detector is required to
   find (rule 4); the probe exits 0 on success (rule 5); the probe's pins are
   held independently of the sidecar's ratchet baseline (rule 6); and the
   selftest prints what each catch WAS (rule 7). One mutation
   (`skip_dirs_lost_absorbed`) was MISSED, investigated, found to be
   unfalsifiable by construction — every `skip_dirs` entry excludes zero files,
   because the big archives are top-level siblings the surface list already
   omits — and was REPLACED with a live one rather than deleted quietly; the
   finding is recorded in both the gate and the probe.
3. **Over-claim auditor.** The dirty set is never described as stale. Every
   report line, the gate docstring, the probe docstring and this artifact say
   the same thing: it is the set of pairs NOBODY HAS CHECKED. The one place a
   staleness claim is made — the six `STALE-FOUND` records — is transcription
   of SCUR-1's typing with a pointer to SCUR-1's own text.
4. **Under-detection auditor.** Where can a real staleness still hide? (i) the
   289 undated files, structurally; (ii) any vocabulary outside the signatures,
   measured at 17% against SCUR-1's six findings; (iii) non-markdown surfaces —
   the ledger JSONs and the YAML registries are out of scope, and SCUR-1's own
   `layer0-fork-registry.yaml` finding shows they matter; (iv) `papers/` and
   `absorbed/`, excluded by the surface list. All four are stated in the gate's
   own output or its config comments, not only here.
5. **Reader-of-the-future.** The single sentence a later reader most needs:
   *the citation gate and this gate answer different questions — "did you
   acknowledge what you cited?" versus "did anyone check what you predate?" —
   and neither subsumes the other, so keep both and never loosen the first to
   imitate the second.*
6. **Concurrency auditor.** The corpus grew 3643 → 3645 during this session
   from other lanes; no probe pin depends on a corpus count, and the pinned
   dirty counts are stable against new filings because every file created today
   post-dates all ten corrections. If a future lane files a document with an
   OLD `created:` date, the pinned counts move and the probe goes red — that is
   the ageing signal to re-baseline, and it is stated here by design (SCUR-1's
   own ageing-note pattern).

## 11. Certificate

```
_local/cas-venv/bin/python process_gates/canonical_currency_audit.py
    -> 188 dirty pairs, 13 cleared, 1 measured signature miss; well-formed;
       ratchet intact (all ten corrections inside the 7-day grace); exit 0
_local/cas-venv/bin/python process_gates/canonical_currency_audit.py --as-of 2026-08-25
    -> all ten AGED, ratchet armed and green; exit 0
_local/cas-venv/bin/python tests/channel-swings/joe_directed_ct5_canonical_corrections_as_dirty_bits.py
    -> 68/68 checks, exit 0
_local/cas-venv/bin/python tests/channel-swings/joe_directed_ct5_canonical_corrections_as_dirty_bits.py --selftest
    -> clean baseline verified FIRST (68/68), then 13/13 machinery-corruption
       mutations each produce a genuine [FAIL] and red exit (date extraction
       disabled, filename fallback removed, predate loosened to inclusive,
       clearing-beats-stale inverted, explicit-beats-blanket inverted, owner
       exemption removed, surfaces narrowed, root markdown dropped,
       ALL-REGISTER token renamed, FIX-A repairs dropped, registry entry with
       an empty token family, sidecar record pointing at a ghost file,
       frontmatter window truncated); crash-catches rejected by design; exit 0
_local/cas-venv/bin/python process_gates/correction_propagation_audit.py
    -> exit 0, output identical to the pre-edit registry modulo the unittest
       wall-clock line
```

Check inventory (exact, no floats anywhere; total 68): 8 registry-shape checks
(entry count, id set, entry_class, canonical_since map, nonempty families,
blindness present, synonym families present, owner paths exist); 4 citation-gate
isolation checks (two-key structure, the ten historical ids in order, no leak,
the real gate passes in-process); 9 sidecar seed checks (35 records, 23
ALL-REGISTER, 6 STALE-FOUND, pointers present, SCUR-1 attribution, 6 FIX-A pairs
exact, closed verdict vocabulary, files exist, SUPERSEDED-DOC honestly unused);
2 well-formedness/ratchet checks on the live state; 16 dirty-set checks (10
per-correction pinned counts, total 188, total cleared 13, blindness = exactly
CB-B under CC-08, topic_reach ≥ dirty, and 2 scope-composition pins); 12 Z/3
both-states checks (corpus membership, date, signature match, predates, state A
×2, state B ×3, state C ×2, specificity); 9 contrary-control checks (post-
correction file dated after, matches the signature so the test is not vacuous,
not dirty anywhere; fenced comparator resolves FENCED and is not dirty; CB-E
clean; CB-A repaired; repair is load-bearing; count rises by exactly one when
dropped); 3 planted-positive controls (detector power, owner exemption,
explicit-beats-blanket precedence); 5 ratchet-teeth checks (all aged at
2026-08-25, green unchanged, honestly inert today, breaks when repairs are
dropped, RED when an aged correction has no baseline).

A note on ageing, by design: the ten pinned dirty counts are properties of a
live corpus. If a future filing carries an old `created:` date, or an owner
adjudicates part of the queue without recording it in the sidecar, the pins go
red — that is the signal to re-baseline this probe, not evidence that the gate
broke.

## 12. Blunt paragraph — what this actually buys, and what it does not

**It buys a queue and a ratchet, not a truth.** 188 pairs is not 188 stale
documents; it is 188 places where the repository cannot currently say whether
anybody looked, and the honest reading of the number is that the pre-correction
surface is large and almost entirely unexamined — SCUR-1's three days of hand
work covers 13 of them. The mechanism's real contribution is not detection
power, which is bounded by whatever vocabulary somebody thought to type into a
token family and measured at a 17% miss rate against the only ground truth
available; it is that a correction now has a DATE and a persistent consequence,
so the question "who consumes this and has anyone checked?" is asked
automatically at every run instead of depending on somebody remembering to run
a grep. The two things most likely to kill it are boring and both are already
visible: an author writing `ALL-REGISTER` casually until the sidecar becomes a
blanket exemption, and a baseline raised in the same file the ratchet guards.
Neither is prevented by anything here; the first is only slowed by the ageing
rule, the second only by the probe's independently-held pins. If this mechanism
is alive in a month it will be because somebody kept clearing the queue, not
because the gate made them.

---

*Filed 2026-08-17, CT-5, ct-hardening channel. Instrumentation only: no canon,
ledger, registry horn, verdict, grade, count, bar, or audited document moves on
this artifact; no currency call is adjudicated; the Z/3 packet's CLEARED state
is a labelled selftest plant and not a live record; no git operations.*
