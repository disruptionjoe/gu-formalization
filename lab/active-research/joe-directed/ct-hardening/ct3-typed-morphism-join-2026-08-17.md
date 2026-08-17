---
artifact_type: exploration
status: exploration
doc_type: reference_design_record
created: 2026-08-17
work_item: CT-3
channel: ct-hardening
title: "CT-3: the needs/provides join is typed — a new sidecar (lab/process/needs-provides-typed-records.json) holds six-key morphism records {key, dom, cod, map_type, source_file, receipt} whose dom/cod are CT-1 object ids, CT-1 declared-unknown markers, or registered-homonym sense ids, each carrying the deterministic rule that produced it and a byte-verified quote the gate RE-APPLIES every run; a new gate (process_gates/needs_provides_typed_join_audit.py) pins schema, CT-1 codomain compliance fail-closed, receipt liveness, discriminator disjointness re-measured on the owning files, and the v_PSB acceptance test. ACCEPTANCE PASS: the two v_PSB carriers separate mechanically (HOM:v_PSB#1 vs HOM:v_PSB#2) and the wrong-dom edge is rejected while the correct cross-file edge survives. Typed coverage is SMALL and stated: 44 records, 1 of 182 provider edges and 1 of 69 candidate pairs decided on the live corpus, bounded above by the FX-2 adoption frontier (28 blocks across 20 files at the close of this pass, every one dated 2026-08-16 or later, against a corpus of ~3,900 markdown files). FX-1 is byte-untouched and behaviour-preserved: same gate output, same probe result, zero new candidate pairs."
grade: "EXACT integer counters and byte-level substring facts only; no float except two printed coverage ratios derived from integer counts. Probe tests/channel-swings/joe_directed_ct3_typed_morphism_join.py: 97/97 checks, exit 0 — LEG S, 6 schema checks over the sidecar's 44 records; LEG C, 9 CT-1 codomain checks (a three-surface triangle across this probe's pinned token copies, the reference, and the gate's derived codomain, plus a planted layer-token drift fixture and a planted absent-reference fixture each demanded to drive the gate red); LEG R, 19 receipt checks (every record quote byte-present in its own source, the five register substrings the discriminator table cites, the byte-disjointness of the two discriminator sets RE-MEASURED on the two owning files from the recorded table rather than a hardcoded copy of the right answer, and the two refusal receipts); LEG A, 13 acceptance checks on the v_PSB class, three of which RE-DERIVE the two carriers' typings through the live rules so a collapsed resolver cannot pass on recorded values alone; LEG P, 7 planted-control checks (a forged dom, an alias with no receipt, a quote drift, a non-disjoint discriminator, a collapsed sense resolver — each CAUGHT — plus the stated zero-live-rejection fact); LEG D, 6 detector-power fixtures each DETECTED; LEG F, 5 planted-FALSE propositions each observed False; LEG B, 4 behaviour-preservation checks against FX-1; LEG G, 28 artifact/runtime checks. Failure path: --selftest verifies the CLEAN BASELINE FIRST, then 11/11 machinery mutations each drive exit 1 via genuine FAIL lines with crash-catches rejected; --selftest --poison poisons the baseline and demands the refusal path. Gate --selftest: clean baseline first, then 12/12 machinery/reference mutations each exit 1 via genuine [FAIL] lines. NOT: a physics result, a claim movement, an adjudication of any FX-1 pair, a canon/ledger/registry/README edit, or an edit of any FX-1 surface."
disposition: JOIN_TYPED_WITH_SIX_KEY_MORPHISM_RECORDS__DOM_COD_ARE_CT1_OBJECT_IDS_MARKERS_OR_REGISTERED_SENSE_IDS__EVERY_TYPING_RE_DERIVED_FROM_A_BYTE_VERIFIED_QUOTE_EVERY_RUN__VPSB_ACCEPTANCE_PASS_TWO_CARRIERS_SEPARATE_MECHANICALLY_WRONG_DOM_EDGE_REJECTED_CORRECT_EDGE_SURVIVES__TYPED_COVERAGE_SMALL_AND_STATED_1_OF_182_EDGES_1_OF_69_PAIRS_44_RECORDS__BOUNDED_BY_THE_FX2_ADOPTION_FRONTIER__FX1_BYTE_UNTOUCHED_AND_BEHAVIOUR_PRESERVED_ZERO_NEW_PAIRS
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
priority_change: none
steering_effect: unchanged
canonical_effect: pending_integration
depends_on:
  - process_gates/needs_provides_composition_audit.py
  - lab/process/needs-provides-alias-table.json
  - lab/methods/gu-base-categories.md
  - process_gates/typed_carrier_declaration_audit.py
  - lab/process/homonym-register.yaml
  - lab/active-research/joe-directed/composition/cp1-three-live-pairs-adjudicated-2026-08-17.md
  - lab/active-research/joe-directed/composition/fx1-needs-provides-join-2026-08-16.md
  - lab/active-research/joe-directed/carrier-decl/fx2-typed-carrier-declaration-2026-08-16.md
  - lab/active-research/joe-directed/ct-hardening/ct1-base-categories-2026-08-17.md
  - lab/process/conditional-physics-ledger-v0.259.json
  - explorations/cycle-gates-and-audits/cycle1-source-selected-pati-salam-stabilizer-gate-2026-06-24.md
  - explorations/conditional-build/selected-k77-trace-hq-connection-internal-chain-gate-2026-08-12.md
  - VERIFICATION.md
scripts:
  - tests/channel-swings/joe_directed_ct3_typed_morphism_join.py
---

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator (the Pati-Salam-breaking
> vector class appears here as a NAME being disambiguated, never as a physics
> verdict). Any result about a standard Higgs/VEV, ordinary family index or net
> chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only
> breaking or familiar vector-mass route binds only that named model. It is not
> evidence for or against Weinstein's source-native mechanism without an
> explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its
> source-native pointers before reusing this result.
>
> Classification: **`INTERNAL_STRUCTURAL_ONLY`.**
>
> Everything below is repository-internal structural work: a data sidecar, a
> process gate, and a probe. No physics object is computed, no comparator is
> run, no source claim is tested, no claim moves, and every typing recorded
> here is quoted from the artifact that owns it.
>
> **REQUIRED INTEGRATION WRITE, not performed here.** This pass ran under a
> write scope limited to its own four paths, on a checkout shared with
> concurrent agents (`lens-digs`, `ct2`, `ct5`, `vz-repair` live during this
> build), so it edits no registry and no README. One one-line write belongs to
> the canonical integrator, without which
> `process_gates/source_native_comparator_routing_audit.py` goes red
> (`UNCLASSIFIED_BASELINE` must NOT be raised):
>
> ```json
> { "path": "lab/active-research/joe-directed/ct-hardening/ct3-typed-morphism-join-2026-08-17.md",
>   "classification": "INTERNAL_STRUCTURAL_ONLY" }
> ```
>
> `protected_surface_diff_audit` is red on these uncommitted paths by
> construction, as it was for FX-2 and CT-1, and resolves on review/commit.

# CT-3 — the join now agrees on objects, not on spellings

**The one-paragraph answer.** FX-1's join is the MERGE half of a join: its
alias table says *"these two notations are one object"*, under the law NO
ALIAS WITHOUT A RECEIPT. It has no SPLIT half, and its measured blindness sits
exactly there — one written token, two different objects. The dated instance is
`v_PSB` (homonym register :1153): a rank-one vector in `(10bar,1,3)` and an
independent rank-one vector in `(4,1,2)`, whose stabilizer dimension is 12
either way, so the one numeric a reader would check cannot separate them; CP-1
had to exclude the wrong object by hand, in prose, inside a ledger revival
trigger. CT-3 adds the split half: a sidecar of six-key morphism records whose
`dom`/`cod` are CT-1 object ids, CT-1 declared-unknown markers, or
registered-homonym sense ids, each carrying the deterministic rule that
produced it plus a byte-exact quote the gate re-applies on every run. The two
carriers now separate mechanically, the wrong-dom edge is rejected, the correct
cross-file edge survives, and the typed coverage is small, printed, and
honest.

---

## 0. PREFLIGHT — seven lenses, run before any file was written

1. **Retrieval-first / anti-novelty.** Exact-substring sweeps for
   `typed-records`, `typed_join`, `morphism record`, `"dom"`/`"cod"` record
   surfaces and `HOM:` sense ids returned nothing outside one unrelated
   operator-domain gate. Per the standing rule, a zero-hit exact search is NOT
   evidence of novelty, and CT-3 claims none: every part here already exists —
   FX-1's join, CT-1's object ids, the homonym register's own disambiguator.
   The only new thing is the wire between them.
2. **Ceremony lens (the pre-named strongest attack).** *Is a typed layer over
   the same tokens anything but re-spelling?* Pre-registered falsifier: if the
   typed layer changes no join decision anywhere, it is ceremony. Answer is in
   §4 and §6, with numbers, including the number that is uncomfortable.
3. **Fail-closed codomain lens (the FX-2/CT-1 pattern).** A typed layer whose
   vocabulary can drift from its reference silently is worse than none. The
   gate therefore derives the whole codomain FROM CT-1's own tables — object
   ids, the layer-token-to-object map, the arrow labels — and reds if the
   reference vanishes, loses its machine block, or rewords an object row's
   role prefix.
4. **Shared-checkout lens.** Live siblings land new typed blocks hourly. A
   completeness ratchet on this surface would go red on other channels'
   legitimate work, exactly the cross-channel red the guard rules forbid. So
   the gate's red paths are forgery, drift, lost receipts and the acceptance
   test; newly derivable-but-unrecorded records are PRINTED, never ratcheted,
   and the rationale is written into the gate's own docstring.
5. **Behaviour-preservation lens.** CT-1's design record is itself a measured
   FX-1 candidate pair (`ART:…ct1-base-categories…::HALF-SAME`), so a new
   artifact in this channel demonstrably perturbs FX-1's join. This artifact is
   therefore written to add ZERO candidate pairs, and §5 is the measurement,
   not the promise.
6. **Homonym-non-object lens (CT-1 §3.5).** *A bare registered token fails to
   name an object.* This turned into a design correction during the build; see
   §3, the first hostile catch.
7. **No-guessing lens (CN-2, carried).** Every typing must be re-derivable by a
   named rule from a byte-exact quote. Where the text supports no typing, the
   record says so. A plausible token would be a lie; a declared unknown is
   compliance.

---

## 1. The record shape

```
{ "key": "v_PSB",
  "dom": "HOM:v_PSB#2",
  "cod": "UNTYPED",
  "map_type": "UNTYPED",
  "source_file": "explorations/conditional-build/selected-k77-trace-hq-…-2026-08-12.md",
  "receipt": { "site": "FILE:explorations/conditional-build/selected-k77-trace-hq-…-2026-08-12.md",
               "rule": "homonym-sense-by-discriminator",
               "quote": "(4,1,2)" } }
```

That is the record verbatim, elision of the long path aside. The `quote` is the
discriminator itself because that is exactly the byte the rule read; the line
it was read from is `| \`v_PSB\` | independent rank-one vector in \`(4,1,2)\`
whose stabilizer is the SM | …`, and the same-line binding is re-checked on
every run rather than frozen into the record.

Exactly six top-level keys, as briefed. The codomain of `dom` and `cod`:

| value class | admissible values | authority |
|---|---|---|
| Source-Layer object | `L1`..`L4` | `lab/methods/gu-base-categories.md` §1.1 |
| Carrier object | `C1`..`C11` | same reference §3.1 |
| declared-unknown markers | `UNTYPED` (M1), `HOMONYM-AMBIGUOUS` (M4) | same reference §3.2 |
| registered-homonym sense id | `HOM:<token>#<n>` | `lab/process/homonym-register.yaml`, the surface §3.5 names |

`map_type` ranges over the reference's `gu-token-codomain` arrow labels. Every
one of these is parsed out of CT-1's tables at run time; nothing is hardcoded,
so a reference edit reds the gate instead of silently re-typing a record.

**No thirteenth object is coined.** `HOM:` ids name no new inhabitant of any
CT-1 category; they point at the register, which CT-1 §3.5 already names as the
disambiguation surface for registered tokens, and each category keeps its
`<= 12` object budget. A mixed `LAYER=a+b` slot is recorded `UNTYPED` with its
`BRIDGE=` text quoted, because CT-1 has no product object and CT-3 declines to
invent one.

## 2. Extraction — four rules, in precedence order, none of them guessing

| rule | source | live yield |
|---|---|---|
| R4a `homonym-sense-by-owning-file` | the text names exactly one sense's owning file — CP-1's own move, *"same object verified by LINEAGE RECEIPT, not token"* | 5 records |
| R4b `homonym-sense-by-discriminator` | exactly one sense's discriminator occurs in the text AND co-occurs with the token on a line | 8 records |
| R1 `fx2-block-*` | `gu-typed-objects` blocks: `dom` from a named Carrier object occurring verbatim in the carrier slot, else from `LAYER=`; `cod` from a named Carrier object in the target slot; `map_type` from `MAP-TYPE=` | 30 records |
| R2 `ledger-context` | CT-2's per-row `context` projection — **specified, still empty, and checked**: CT-2 landed `lab/process/conditional-physics-ledger-schema-v0.2.json` (`$defs.context`, the required (layer, grant, carrier) triple) hours after this pass began and scoped the obligation to ledger v0.260 onward without retro-filling, so 0 of 87 rows of `conditional-physics-ledger-v0.259.json` carry the field. Its carrier codomain is CT-1's `C*` ids — the same codomain as `dom` here — so nothing will need an adapter when it arrives; the gate reds if rows gain the field while this table still says empty | 0 records |
| R3 `prose-token` | explicit `LAYER=` / `MAP-TYPE=` tokens outside any fenced block | 1 record |

Ties, both-senses, or neither give `HOMONYM-AMBIGUOUS`; conflicting blocks in
one file give `UNTYPED` (`fx2-block-conflict`, 2 records). The discriminator
table itself carries FX-1's law, mirrored: **NO DISCRIMINATOR WITHOUT A
RECEIPT.** FX-1's table merges two notations into one object; this one splits
one notation into two. Two candidate tokens were REFUSED an entry and say why —
`Met(X^4)`, whose register rule is a convention for future writing rather than
a substring that partitions the corpus, and `so(1,3)`, on which the register
itself declines sensing (CT-1 already carries the subscripted forms as `C8`
and `C9`, which R1 reads directly).

## 3. Three hostile catches that changed the build

**Catch 1 — a registered token typed by its stratum is a FALSE verify.**
The first extractor typed `Met(X^4)` as `C1` from its `LAYER=ambient` slot.
Both senses of that token live at the ambient stratum, so two files could have
agreed on `C1` and printed TYPE-VERIFIED for two different objects — the exact
failure this lane exists to stop, produced by the lane itself. Fixed by law:
a registered-homonym token with no receipted discriminator set is typed
`HOMONYM-AMBIGUOUS`, never by its stratum. That is CT-1 §3.5 made mechanical.

**Catch 2 — a file-scoped discriminator exceeds its receipt.** The register's
sentence claims byte-disjointness *across the two owning files*. The first R4b
applied the discriminator to any file containing it, which types a file whose
`(4,1,2)` belongs to some unrelated sentence. Narrowed: exactly one sense's
discriminator may occur in the text at all, and it must co-occur with the token
on a line — the register's own naming rule (*"name the representation with the
token"*) read mechanically. Every surviving resolution was then read by hand
against its line, and all thirteen bind the token to its representation on the
line quoted. Two records were dropped by the narrowing, and the trace-hq
source-return file now types `HOMONYM-AMBIGUOUS` rather than by inheritance —
honestly weaker, and correct.

**Catch 3 — the preservation discipline is fragile, and the probe caught it
firing.** Late in the pass, an edit to this artifact's own `title:` line put
one of FX-1's provide verbs onto a line that also carries a join key. That
silently turned this record into a supply site for the token under test, and
the probe's A7 and F2 checks went red inside a minute: the control's provider
list came back with three entries where the measurement demands two. The word
was replaced and the FX-1 output returned, byte for byte, to its pre-CT-3
state. The lesson outlives the fix — a behaviour-preservation claim resting on
prose discipline is worth exactly as much as the check that re-measures it, so
the check runs every time rather than once.

## 4. The v_PSB acceptance test — ACCEPTANCE PASS

Constructed explicitly from the two carriers, both directions, on the live
tree:

| fact | value | rule |
|---|---|---|
| need side, ledger row RA-A6 | `HOM:v_PSB#1` | R4a (the row names the cycle1 gate by filename; note its trigger text carries BOTH representation strings, which is precisely why the lineage rule is tried first) |
| carrier 1, the cycle1 gate | `HOM:v_PSB#1` | R4a |
| carrier 2, the trace-hq chain gate | `HOM:v_PSB#2` | R4b, on `| \`v_PSB\` | independent rank-one vector in \`(4,1,2)\` …` |
| separation | `HOM:v_PSB#1` != `HOM:v_PSB#2` | mechanical, no reader in the loop |

**The rejected edge.** FX-1's token join does not offer the wrong carrier
today, and the reason is worth writing down: the trace-hq lines carrying the
token have no provide verb on them, so the extractor never reaches them. The
blindness is latent, one word away. The gate therefore injects one provide verb
into an in-memory copy of the real file — FX-1's own `extra_md` hook, nothing
on disk touched — and FX-1's token join promptly hands over BOTH carriers for
`LEDGER:RA-A6::v_PSB`. The typed join rejects the wrong one:

```
TYPE-REJECTED  LEDGER:RA-A6::v_PSB <- …selected-k77-trace-hq-…-2026-08-12.md
               [HOM:v_PSB#1 != HOM:v_PSB#2]
```

**The contrary control that must survive.** The correct cross-file edge is not
merely un-rejected; it is positively typed:

```
TYPE-VERIFIED  LEDGER:RA-A6::v_PSB <- …cycle1-source-selected-pati-salam-…-2026-06-24.md
               [HOM:v_PSB#1 = HOM:v_PSB#1]  (homonym-sense-by-owning-file / by-owning-file)
```

A join that rejected everything would pass a rejection test and be worthless;
this one separates two objects and keeps the one that belongs.

## 5. FX-1 behaviour preservation — measured, not promised

FX-1's gate, its alias table and its probe are byte-identical to their state
before this pass; CT-3 imports the gate read-only for its token shapes and its
live join, and never patches it.

| measurement | before the four CT-3 writes | after |
|---|---|---|
| `needs_provides_composition_audit.py` sha256 | `e3b165261866d3b5…` | identical |
| `needs-provides-alias-table.json` sha256 | `ba6a03ad03c88633…` | identical |
| gate exit code | 1 (pre-existing: 5 un-adjudicated pairs from live siblings) | 1 |
| gate un-adjudicated count and pair names | 5, named in FX-1's own failure text | the same 5 |
| gate stdout+stderr, whole output | — | byte-identical except the `Ran 8 tests in Ns` timing line |
| probe exit code / checks | 0, 49 checks, 0 failed | 0, 49 checks, 0 failed |

Those measurements were taken twice, before and after, and the probe re-takes
them on every run. It PRINTS them as a dated reconciliation and asserts
equality only under `--strict`: FX-1's owner may legitimately edit its own
`ADJUDICATED` map on this shared checkout while this lane runs, and a
cross-channel red on someone else's correct work is the failure mode preflight
lens 4 rules out. What the probe DOES assert unconditionally is the part that
is CT-3's to keep true: FX-1's source references neither CT-3 surface, CT-3's
gate writes exactly one file (its own sidecar), and the gate imports FX-1
without ever assigning into it.

The pre-existing red is NOT CT-3's: it is CT-1's own record plus three live
sibling artifacts, listed by name in FX-1's own failure text. CT-3 adds zero
candidate pairs, which is why the digest is unchanged — this artifact was
written with FX-1's need-verb and provide-verb vocabulary kept off every line
that carries a join key, and the digest equality is the proof that the
discipline held. The gate also asserts mechanically, every run, that FX-1's
source references neither CT-3 surface, so the direction of dependence cannot
quietly reverse.

## 6. Coverage — small, real, and stated where it cannot be missed

On the live corpus:

- **44 records** in the sidecar: 13 on the `v_PSB` class (5 by lineage, 8 by
  discriminator), 30 from `gu-typed-objects` blocks (of which 2 are declared
  block conflicts and 1 is a registered homonym held at the marker line by
  Catch 1), and 1 from prose.
- **1 of 182** (pair, provider) edges DECIDED — 1 TYPE-VERIFIED, 0
  TYPE-REJECTED, 181 TYPE-UNVERIFIED.
- **1 of 69** FX-1 candidate pairs decided; 1 of 69 carries a typed need side.
  30 of the 69 are Tier-2 WIDE rows whose providers FX-1 exposes only as a
  three-file sample, so the edge denominator under-counts them and the pair
  denominator does not; both are printed every run.
- **Zero rejections on the untouched corpus.** The single rejection appears
  under the planted control. That is the honest headline number and it is in
  §7's blunt paragraph rather than buried here.
- The ceiling is structural: typed records above the marker line can only come
  from surfaces that carry a typing, and the FX-2 block frontier is 28 blocks
  across 20 files at the close of this pass — 22 across 15 when the extraction
  was first measured a few hours earlier, which is itself the shape of the
  ceiling — every one dated 2026-08-16 or later, against a corpus of ~3,900
  markdown files. Coverage rises when FX-2 adoption rises, and again when
  CT-2's row projection reaches a minted ledger (R2 is specified for v0.260
  onward and still empty, by CT-2's own non-retroactivity choice). It does not
  rise by editing this gate.

## 7. Hostile review — is this real coverage or ceremony over the same tokens?

**Steel-manned attack.** *Thirteen of the 44 records are one token; the other
31 come from a block format two days old; the join decides one edge in 182 and
rejects nothing that anyone actually wrote. Strip the vocabulary and you have
re-spelled FX-1's keys with C-ids, then declared victory on a case a human had
already adjudicated by hand.*

**What survives of it, conceded plainly.** The coverage numbers are as bad as
that says, and the one live decision is a VERIFY, not a catch. The typed layer
has never yet stopped a wrong join on the untouched tree, and this record does
not claim it has. Anyone reading only §6 should read it as: the instrument is
in place and nearly all of its dial is dark.

**What does not survive.** Three things separate this from ceremony, and each
is a file fact rather than an adjective. First, the discriminating power comes
from a surface FX-1 structurally cannot consult: the homonym register's own
disambiguator, applied byte-level, plus CT-1's ids. Re-spelling a token as a
C-id would give exactly zero separation on `v_PSB`, because both senses sit at
one stratum — which is why Catch 1 in §3 had to become a law rather than a
convenience. Second, the case was NOT already handled: CP-1 excluded the wrong
object *by hand, in prose, inside a ledger field*, and the register's own note
says the numeric a reader would check gives 12 either way. A hand exclusion in
one row protects one row; this protects the join. Third, the rejection is
demonstrated on real bytes, not a fixture: the wrong carrier is the actual
2026-08-12 file, and it is absent from FX-1's provider set for one reason only
— no provide verb sits on its token lines. That is a latent blindness, and a
latent blindness caught before it fires is the cheap end of this repository's
most expensive failure class.

**Where the attack lands cleanly.** Two limits are conceded rather than
argued. (i) `cod` is almost entirely `UNTYPED`: the `target:` slot of a typed
block names an object in prose and only rarely a CT-1 named carrier, so the
codomain half of "agree on dom/cod" is currently carried by dom alone —
5 records of 44 have a non-marker `cod`. (ii) The CHIRALITY axis is not wired,
deliberately: CT-1 §3.4 assigns that codomain to CN-2, and wiring it here would
create rival ownership. A future stage that wires either is a real upgrade;
pretending they are wired now would be the lie this whole lane exists to
prevent.

## 8. What this does not do

No physics claim, no verdict, no claim movement, no ledger, canon, registry or
README edit, no adjudication of any FX-1 pair (FX-1's `ADJUDICATED` map remains
the only place a pair is typed), no edit to any FX-1 surface, and no promotion
of any typing into `canon/`. The gate auto-closes nothing: a TYPE-VERIFIED edge
is a statement that two recorded doms agree, never a statement that a need is
answered.

## 9. POSTFLIGHT — five lenses, run after the build

1. **Did the pre-named attack get a real answer?** Yes, and it partly lands:
   §7 concedes the dark dial and the `cod` gap in the same paragraph as the
   defence. The pre-registered falsifier (*changes no decision anywhere*) is
   not met — one edge is decided and one is rejected under control — but it is
   met far more narrowly than a reader of the title would guess, and the title
   says so.
2. **Is anything typed that the text does not support?** Re-checked twice: the
   stratum-typing of registered homonyms was removed (Catch 1) and the
   file-scoped discriminator was narrowed to same-line (Catch 2). Every one of
   the 13 surviving homonym resolutions was read against its quoted line by
   hand. Two records were lost to the narrowing and were not recovered by a
   looser rule.
3. **Can the instrument certify nothing while printing green?** Both
   selftests check their clean baseline BEFORE any mutation, every mutation
   corrupts machinery or a reference (never a predicate — a loosened predicate
   can only make a probe greener and is undetectable by any runner), and a
   catch counts only through a genuine `FAIL` line on a run that still prints
   its certificate. That last rule earned its place here: the probe's first
   selftest returned three CRASH-NOT-DETECTION verdicts and three MISSED ones,
   and every single one was a real defect rather than a harness quirk. The
   three crashes were the gate and the probe raising `KeyError`/`JSONDecodeError`
   on a malformed sidecar instead of failing closed on it; the three misses
   were checks reading hardcoded copies of the right answer instead of the
   recorded table, and an acceptance leg that compared recorded values without
   ever re-running the rules that produce them. All six were repaired — the
   gate now reds on a missing sidecar section, the discriminator checks read
   the table, and three A-leg checks re-derive through the live rules — and
   the second selftest is 11/11. Gate selftest: 12/12.
4. **Did a sibling channel get harmed?** No file outside CT-3's four paths was
   touched, and FX-1's gate output is byte-identical, so the four pre-existing
   sibling reds are neither hidden nor increased. The pre-existing red is
   reported as pre-existing, with its five pair names, rather than absorbed.
5. **Is the honest classification the one written down?** `L2`-analogue for a
   process artifact: this is a measured repository-internal instrument, not a
   proof and not a physics result. `INTERNAL_STRUCTURAL_ONLY`,
   `target_claim: NONE-NOT-A-KILL`, `canonical_effect: pending_integration`,
   and the required integrator write is printed at the top rather than
   performed.

## 10. Certificate

```
process_gates/needs_provides_typed_join_audit.py             0 FAIL, exit 0
  --selftest                    clean baseline FIRST, then 12/12 machinery/reference mutations
                                each exit 1 via genuine [FAIL] lines, exit 0
  --selftest --poison           refuses to bank any mutation, exit 1 (the guard has power)
tests/channel-swings/joe_directed_ct3_typed_morphism_join.py 97/97 checks, 0 failed, exit 0
  --selftest                    clean baseline FIRST, then 11/11 machinery mutations
                                each exit 1 via genuine FAIL lines, exit 0
process_gates/needs_provides_composition_audit.py (FX-1)     unchanged: exit 1 (pre-existing),
                                same 5 pairs, sha256 e3b165261866d3b5… identical
lab/process/needs-provides-alias-table.json (FX-1)           unchanged: sha256 ba6a03ad03c88633…
tests/channel-swings/joe_directed_fx1_needs_provides_join.py unchanged: 49 checks, 0 failed, exit 0
```

Honesty on the two decimals in this record: `0.0055` and `0.0145` are integer
ratios printed to four places (1/182 and 1/69), not measurements with error
bars. Every other number here is an exact count or a byte-level substring
fact.

```gu-typed-objects
result: CT-3 typed-join instrument -- the two v_PSB carriers separate mechanically
  (HOM:v_PSB#1 vs HOM:v_PSB#2), the wrong-dom edge is rejected under a planted
  provide-verb control, the correct cross-file edge survives, and typed coverage
  is 1 of 182 provider edges / 1 of 69 candidate pairs over the live corpus
carrier: the sidecar lab/process/needs-provides-typed-records.json and the join-key
  population of process_gates/needs_provides_composition_audit.py
  LAYER=UNTYPED CHIRALITY=N/A
  # LAYER is honestly UNTYPED for the SCUR-1/PCX-1/CT-1 reason: the closed
  # vocabulary (ambient/observed/source-print/toy) types physics carriers, and this
  # carrier is repository process data about repository text.
pairing: NONE
real_structure: N/A
grading: N/A
action_owner: repository-construction (CT-3 directed brief; enforcement lives in the
  new gate's audit loop, and every typing is re-derived from a byte-verified quote on
  every run)
target: the dom/cod agreement verdict on each candidate edge of the needs/provides
  join MAP-TYPE=evaluation
  # evaluation = the typed join EVALUATES a recorded pair of doms to one of
  # TYPE-VERIFIED / TYPE-REJECTED / TYPE-UNVERIFIED; it transports nothing between
  # carriers and adjudicates no pair.
```
