---
artifact_type: exploration
status: exploration
doc_type: notation_repair_record
created: 2026-08-15
work_item: CN-2
channel: carrier-notation
target_claim: "INTERNAL — CR-B §5's own flagged residual: `The repo's `nu in Omega^0(S), zeta in Omega^1(S)` shorthand | flagged. Faithful to eq (9.16) with `S` the full Dirac bundle; when read as the same Weyl half twice it silently selects the unique class-MIXED pairing.` CN-2 targets the FLAG, not the science: does the repository's notation state which reading it means, at every site that states the field content?"
target_claim_verdict: "CONFIRMED AND REPAIRED AT 13 SITES, WITH ONE CORRECTION TO CR-B'S PHRASING AND ONE PRIOR-ART CORRECTION TO THE BRIEF. Confirmed: 182 unsubscripted occurrences across 57 files, and at the 13 sites that actually DECLARE the field content none said which of the three inequivalent readings it meant. Corrected (CR-B phrasing): the same-half reading is not `the unique class-MIXED pairing` — BOTH same-half pairings (S+,S+) and (S-,S-) are class-mixed; they are one pairing only up to the global +/- relabelling, and the artifact says so. Corrected (brief's premise): this is NOT the repository's first sight of the defect. `canon/escape-corners-campaign-RESULTS.md` already records the A2 leg `REFUTED-AS-FILED` for computing on exactly the same-half content, and `explorations/dk-chirality-fork-2026-07-20.md` already typed the chirality assignment as a physics-default IMPORT and computed both branches. The defect was already adjudicated TWICE at the instance level and never propagated to the NOTATION. That, not the discovery, is what CN-2 fixes. NOT DECIDED, deliberately: which reading is GU's operative content."
title: "CN-2: the repository's field-content notation now SAYS which chirality reading it means, or says it is ambiguous — 13 sites repaired with a closed four-value typing vocabulary whose default value is AMBIGUOUS. Census exact: 182 unsubscripted occurrences in 57 files, of which 13 are field-content DECLARATIONS (repaired), 3 are canon (proposed diff only, file untouched), 4 are ledger/predeclaration surfaces (left, with reason), and 37 are toy-arena, operator-domain or verbatim-quote sites where the ambient half question is not what is at stake. ZERO sites were typed to the protected half-pairing: inventing that source commitment is the exact failure the repair had to avoid, and the probe asserts it did not happen. ONE site's conclusion DEPENDS on a reading and it depends on the FULL-DIRAC one, not the naive one: the K77 `H640 = 512 + 128` module, whose 128 is the full complex Dirac dimension of Cl(7,7) and would be 64 under any Weyl-half reading. SELECTORS: neither `SC-CHI-01` nor SG4 bit 2 presupposes a reading — but `leg_a_forcing_enumeration.py` C6a's `NEUTRAL at the declaration level` is over-broad, because the leg's three coded axes contain no chirality axis at all, so the notation's chirality content was never in the cell space that SG4's 2-bit residual was measured over."
grade: "EXACT string census (one regex pair, reused by the artifact and the probe so they cannot drift) plus EXACT integer weight arithmetic. Probe `tests/channel-swings/joe_directed_cn2_notation_census.py`: 120/120 checks, exit 0. The Z/4 centre-class leg is recomputed from scratch in doubled integer coordinates with NO import from CR-B's probe and reproduces its D_7 table independently; a second independent leg (`-w_0` by weight-multiset negation) agrees on every rank tested. Non-vacuity three ways: 13 predeclared FALSE assertions each observed False; a genuine CONTRARY CONTROL at D_6 where the protection provably fails and the instrument returns `not protected`; and 15/15 injected machinery mutations drive exit 1 under `--selftest`, which exits 0 on success. Every mutation corrupts MACHINERY rather than a predicate, because weakening an assertion is not a detectable mutation — recorded in the probe. No float anywhere. NOT: a claim-status movement, a source reading, a generation count, an index, a resolution of the chirality fork, or any edit to canon."
disposition: NOTATION_NOW_TYPED_AT_EVERY_DECLARATION_SITE__CLOSED_FOUR_VALUE_VOCABULARY_WHOSE_DEFAULT_IS_AMBIGUOUS__13_SITES_REPAIRED_3_CANON_PROPOSED_ONLY_4_LEDGER_LEFT_37_OUT_OF_CLASS__ZERO_SITES_TYPED_TO_THE_PROTECTED_HALF__ONE_CONCLUSION_DEPENDS_AND_IT_DEPENDS_ON_FULL_DIRAC__SELECTORS_DO_NOT_PRESUPPOSE_BUT_SG4S_CELL_SPACE_HAS_NO_CHIRALITY_AXIS__FORK_UNRESOLVED_BY_DESIGN
canon_verdict_change: none
steering_effect: unchanged
canonical_effect: pending_integration
depends_on:
  - lab/active-research/joe-directed/carrier/crb-carrier-is-four-corners-not-one-weyl-2026-08-15.md
  - canon/escape-corners-campaign-RESULTS.md
  - canon/gu-forces-field-space-declaration-RESULTS.md
  - explorations/dk-chirality-fork-2026-07-20.md
  - lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md
  - lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md
  - lab/sources/source-claim-register.yaml
  - tests/escape-corners/referee_legA2_verify.py
  - lab/methods/source-native-comparator-routing.md
scripts:
  - tests/channel-swings/joe_directed_cn2_notation_census.py
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
> Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY` — see §7. The repair is
> source-native (it records what the draft and the talks DECLARE, and types the
> gap between them); the *reason the distinction matters* runs through the
> comparator words "vectorlike" and "`n_g`", which this artifact quotes from
> CR-B and does not re-derive or advance.

# CN-2 — making the notation say which half it means

## 0. The one-paragraph answer

The repository's field-content shorthand `nu in Omega^0(S)`, `zeta in Omega^1(S)`
is **unsubscripted in both slots**, and until this pass **not one** of the 13
sites that actually declare the field content said which of three inequivalent
things it meant. The three are: `S-FULL-DIRAC` (both Weyl halves, 128 complex —
what eq (9.16) literally declares), `S-HALF-OPPOSITE` (`Omega^0(S+) +
Omega^1(S-)` — the source's only explicit *spoken* chirality declaration, typed
*emergent* by `SC-CHI-01`), and `S-HALF-SAME` (`Omega^0(S+) + Omega^1(S+)` —
stated by **neither** primary). Every one of the 13 now carries an explicit
`[CN-2 S-TYPING: <token>]` declaration from a **closed four-value vocabulary
whose fourth value is `S-CHIRALITY-UNTYPED`** — the value that lets a site be
repaired by *saying it is ambiguous* instead of being quietly resolved. **Ten of
the thirteen took that value.** Zero took `S-HALF-OPPOSITE`, and the probe
asserts that zero, because typing everything to the protected reading would have
been the invention of a source commitment — the exact failure this repository is
worst at, and the failure the brief named.

---

## 1. Prior-art sweep — and the brief's premise needs correcting

**Retrieval ran before any edit.** Searched, by object and by alternative
vocabulary rather than by label: `Omega^0(S)`, `Omega^1(S)`, `Omega^0(Y,S)`,
`Omega^0(S+)`, `Omega^1(S-)`, `S̸`, `/S`, `Ω⁰`, `\slashed`, `\mathbb{S}`,
"full Dirac bundle", "same Weyl half", "field content", "fermion carrier",
"candidate 2B", "chirality assignment", "positive spinners", `SC-CHI-01`,
`SG4 bit 2`, plus a full listing of `explorations/*chiral*`.

**The brief frames CN-2 as repairing a defect CR-B found. That is not right, and
the correction matters, because it changes what CN-2 is for.**

| prior artifact | what it already established | date |
|---|---|---|
| `explorations/dk-chirality-fork-2026-07-20.md` | Names the assumed content `Omega^0 x S^+ + Omega^1 x S^-` and types **the chirality assignment itself** as "a reconstruction-level physics-default **import**", against "draft eq 9.16 carries the FULL Dirac bundle `/S` with all four components `nu±`, `zeta±` as distinct fields". Computes BOTH branches; promotes neither. | 2026-07-20 |
| `tests/escape-corners/referee_legA2_verify.py` R2 | "the leg's CENSUS CONTENT `Omega^0(S14+) + Omega^1(S14+)` (same Weyl half) is stated by **NEITHER** primary." | 2026-07/08 |
| `canon/escape-corners-campaign-RESULTS.md:46` | **In canon**: "A2 REFUTED-AS-FILED ... the A2 leg's census was computed on a field content stated by NEITHER primary (same-Weyl-half `Omega^0(S+) + Omega^1(S+)`)". | canon |
| `explorations/b5-middle-source-freeze-2026-07-21.md:40,48` | Already writes "the fermionic fields use the **full Dirac bundle** `S`" and "the **full-Dirac** `Omega^0(S) + Omega^1(S)` field arena" — a correct repair, in one file, seven months early. | 2026-07-21 |
| `explorations/de-packet-lane-structure-clarification-2026-07-21.md:200` | Same: "the *arena* (**full-Dirac** `Omega^0(S)+Omega^1(S)`)". | 2026-07-21 |
| CR-B §3.3 | The *arithmetic*: the four printed corners carry classes `3,1,1,3`; exactly two of the four 0-form/1-form pairings are class-homogeneous and both are odd. | 2026-08-15 |

**So the defect was found, adjudicated, and put into canon — twice — and then not
propagated to the notation.** The naive reading was killed as a *source claim* in
July. What was never done is the boring, mechanical thing: make the 180-odd
occurrences of the shorthand *say* so, so the next reader does not have to
re-derive the July finding from scratch. HE-2 did have to, and read the shorthand
naively, which is how CR-B's gate got written.

**Honest ratio.** The *finding* is ~0% new: two banked artifacts and one canon
line own it. The *arithmetic* is ~0% new: CR-B owns it, and §5 reproduces rather
than re-derives it (independently, as a check, not as a claim). **What is new is
the census and the repair** — an exact count, a closed vocabulary with an
explicit ambiguous value, and 13 typed sites — plus three secondary findings
(§4.3, §6, and the CR-B phrasing correction in §5.2) that fell out of doing it.
That is a modest contribution and it is stated at that size.

---

## 2. Preflight — five problem-matched specialist lenses, recorded before editing

**Lens 1 — technical editor / notation systems.** *Route:* the failure mode of a
notation repair is that it becomes a second notation nobody uses. So: ONE closed
vocabulary, ONE bracketed token form the probe can count, and the token must be
**visible prose**, never an HTML comment — the whole point is that a reader sees
it. *Prediction:* the vocabulary needs a fourth value meaning "ambiguous", or
every repair will be forced to pick a side by the shape of the tool. *Stake:* if
I find myself wanting a fifth value, the classification is wrong.

**Lens 2 — source philologist.** *Route:* the authority is the SHA-pinned
extraction and the 110-claim register, not repo prose. Read the DECLARATION locus
(eq 9.16, p.46) separately from the SPOKEN locus (`Transcript into the
impossible.md:107`) and separately again from the GRADING loci (p.51 four
corners, eq 11.6). *Prediction:* the declaration will be unsubscripted, the
spoken form will be opposite-half, and the two will not be in contradiction
because `SC-CHI-01` types the second as emergent from the first. *Binding
condition:* **do not repair a site by making it agree with the spoken form.**
That is the invention this pass must not commit.

**Lens 3 — regression engineer.** *Route:* this repository's probes string-match
prose. Before touching any file, grep `tests/` and `process_gates/` for the exact
substrings I intend to disturb. *Prediction:* the eq (9.16) verbatim block is
matched by several probes and must be treated as immutable. *Consequence, adopted
as a rule:* **additive annotation only — never modify or delete an existing
line's load-bearing substring.** *Stake:* any probe that goes red because of a
CN-2 edit is a failed pass regardless of how good the prose is.

**Lens 4 — scope auditor / repository constitution.** *Route:* `canon/` is not
mine. Neither, under `lab/active-research/joe-directed/README.md`'s own rule
("moves no ledger, canon, `CURRENT-STATE` or `NEXT-STEPS` surface"), are
`NEXT-STEPS.md`, `DERIVATION-PROGRESS.md` or `CURRENT-STATE.yaml`. *Prediction:*
there is a fourth immovable class the brief did not name — **predeclared
commitment records**, where editing a note *after the fact* destroys the
anti-p-hacking receipt that makes the record worth anything. `leg_a_forcing_enumeration.py`
is one. *Stake:* if I edit a predeclaration to make it read better, I have
damaged the artifact I was auditing.

**Lens 5 — adversary / kill designer.** *Route:* design the failure first. A
"repair" that types every site `S-FULL-DIRAC` is indistinguishable from a repair
that types every site `S-HALF-OPPOSITE`: both are *decisions wearing the costume
of a clarification*. So the probe must assert, as a hard check, that **no site was
typed to the protected half-pairing**, and must plant that as a false assertion
required to come back False. Second control: a case where the class protection
genuinely FAILS, so the arithmetic leg is not a machine that only ever says
"protected" — `D_6`, twelve dimensions, where `cls(S^+) = 2` is even. Third:
mutate the machinery, require every mutant to exit 1.

**Lens 6 — honesty auditor.** *Route:* the standing correction is that eight
false-novelty claims burned in one session, and that zero hits from a substring
search is not evidence of novelty. So: grep the exact objects first, lead with
the ratio, and **check whether the brief's own premise is right** before
accepting it. It was not (§1). *Binding condition:* if a banked artifact or a
canon line already owns the finding, cite it in the table above and do not
re-claim it.

**Cheapest kill-or-switch, recorded before computing.** If the census turns up
that most `Omega^0(S)` occurrences are *not* field-content declarations — that
they are operator domains, or a low-dimensional toy where `S` is a stated finite
fibre — then repairing them all would be noise, the census is the deliverable,
and the repair set is small. **That is what happened**: 37 of 57 files are out of
class (§3), and the repair is 13 files, not 57.

**One credible contrary route, recorded before computing.** That some site's
*conclusion* silently depends on the naive reading, in which case the repair
cannot be additive there and CN-2 would have to report a live error rather than a
notation defect. §4.3 checked every quantitative site and found one dependence —
and it runs the other way.

---

## 3. The census — exact, mechanical, reproducible

Probe: `tests/channel-swings/joe_directed_cn2_notation_census.py`, **120/120
checks, exit 0**, `_local/cas-venv/bin/python`, run from the repository root.
Failure path: `--selftest`, **15/15 injected machinery mutations exit 1**, the
selftest itself exiting 0 on success, plus **13/13 planted false assertions
observed False** inside the run.

One regex pair does all the counting, and it is defined once, in the probe, so
this prose and the instrument cannot drift:

```
UNSUB = (?:\\?Omega|Ω)\s*\^\s*\{?[01]\}?\s*\(\s*(?:Y\s*\^?\d*\s*,\s*)?S\s*\)
SUB   = (?:\\?Omega|Ω)\s*\^\s*\{?[01]\}?\s*\(\s*(?:Y\s*\^?\d*\s*,\s*)?S\s*[_^]?\s*[+−±-]
```

### 3.1 Totals

```
    unsubscripted   182 occurrences   in 57 files
    subscripted     162 occurrences   in 14 files   (dated snapshot, see below)
```

**The unsubscripted total is asserted exactly. The subscripted total is not**, and
the reason is recorded rather than smoothed over: the checkout is shared by
several agents this round and the subscripted count moved *during* this pass
(75 -> 162) as other channels wrote files carrying `S+`/`S-`. The probe therefore
asserts per-file counts and set membership — both immune to a foreign file
appearing — and gates the repo-wide equality behind `--strict`. Presenting a
moving number as a measurement is exactly the thing not to do.

### 3.2 The five classes, by site

| class | files | what `S` is there | disposition |
|---|---|---|---|
| **D — field-content DECLARATION** | **13** | the ambient chimeric bundle on `Y^14`; the naive misreading is available and consequential | **REPAIRED in place, additively** |
| **C — canon** | **3** | ditto (2 files) / already correct (1 file) | **proposed diff only, files untouched** (§6) |
| **L — ledger + predeclaration** | **4** | ditto | **left, with reason** (§4.4) |
| **T — toy arena** | 11 | a stated finite fibre (`dim_S = 4`, `Cl(4,0)`); the ambient half question is not what is at stake and the file states its own dimension | left as found |
| **O — operator domain / complex / verbatim quote** | 26 | the domain or codomain of a map (`d_A*: Omega^2(S) -> Omega^1(S)`), a complex (`C_even = Omega^0(S) (+) Omega^13(S)`), or a transcription of source text that must stay verbatim | left as found |

37 files in classes T and O were left as found. That is not laziness: in class T
the file **already** states its fibre dimension (`legb1_graded_ig_algebra.py:21`
writes `Omega^0(S): spacetime-spinor-valued scalars (4-dim)`, which is the full
`Cl(4,0)` spinor and not a half), and in class O the chirality of the fibre is
not the object under discussion.

### 3.3 The 13 repaired sites and their typing

| site | token | why |
|---|---|---|
| `lab/active-research/joe-directed/README.md` | `S-CHIRALITY-UNTYPED` | defines "candidate-2B field content" for the whole joe-directed tree — the highest-leverage site in the census, and the phrase HE-2 was working from |
| `lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md` | `S-FULL-DIRAC` | the declaration locus; the note is **additive** and the verbatim block is byte-identical (four probes match it) |
| `lab/sources/claim-mining-toe-weinstein-complete-2026-07-31.md` | `S-CHIRALITY-UNTYPED` | `WG-F01` "the fermion carrier is ..." — a claim row quoted downstream |
| `lab/sources/curt-jaimungal-gu-iceberg-claim-reconciliation-2026-07-31.md` | `S-CHIRALITY-UNTYPED` | reconciliation row 19; the chirality assignment is added to that row's open list |
| `lab/sources/paired-curt-eric-gu-axiom-and-argument-reconstruction-2026-07-31.md` | `S-CHIRALITY-UNTYPED` | the slide writes `S` unsubscripted *while the adjacent row says "chiral spinor-valued"* — the sharpest ambiguity in the census, because two statements look like they compose and do not |
| `docs/paper-formalization-candidates.md` | `S-CHIRALITY-UNTYPED` | the 2B field-content row in the public-facing docs |
| `explorations/README.md` | `S-CHIRALITY-UNTYPED` | the Step-13 odd-carrier directive summary |
| `explorations/observation-to-family-b5-campaign-2026-07-20.md` | `S-CHIRALITY-UNTYPED` | gate 2 asks the campaign to "justify why field content ... is the odd parameter module" — the gate now also asks *which reading* |
| `explorations/eric-curt-wave3d-b2c2-null-clifford-omega1-completion-2026-07-31.md` | `S-CHIRALITY-UNTYPED` | `SOURCE-CONFIRMS` disposition citing `WG-F01` |
| `explorations/eric-source-directed-native-closure-swing-2026-07-31.md` | `S-CHIRALITY-UNTYPED` | route 3, the minimal Krein-paired odd action's carrier |
| `explorations/conditional-build/selected-k77-zero-seed-h640-action-closure-controls-2026-08-11.md` | **`S-FULL-DIRAC`** | **the one site whose arithmetic depends on a reading** — §4.3 |
| `explorations/b5-middle-source-freeze-2026-07-21.md` | `S-FULL-DIRAC` | already correct in prose ("full Dirac bundle"); token added so the census is machine-countable |
| `explorations/de-packet-lane-structure-clarification-2026-07-21.md` | `S-FULL-DIRAC` | ditto ("full-Dirac") |

**Ten `S-CHIRALITY-UNTYPED`, four `S-FULL-DIRAC` (14 tokens over 13 files), zero
`S-HALF-OPPOSITE`, zero `S-HALF-SAME`.** The last two zeros are asserted by the
probe and planted as false assertions required to come back False.

---

## 4. Findings that are not the census

### 4.1 The vocabulary, and why it has four values

```
S-FULL-DIRAC          S is the full 128-complex Dirac bundle, both Weyl halves.
S-HALF-OPPOSITE       the two slots carry OPPOSITE halves: Omega^0(S+) + Omega^1(S-).
S-HALF-SAME           the two slots carry the SAME half: Omega^0(S+) + Omega^1(S+).
S-CHIRALITY-UNTYPED   this site does not fix it, and does not need to. Fork open.
```

A three-value vocabulary would have forced every site to pick. The fourth value is
the whole design, and it is the majority value.

### 4.2 What the source actually supports, restated so the repair's warrant is visible

- **DECLARATION, eq (9.16) p.46:** `S̸` unsubscripted, and *actively* so — the
  very next display prints `nu±`, `zeta±` as **four distinct fields**. A bundle
  that needed a `±` on it would not need a `±` on the fields.
- **SPOKEN, `Transcript into the impossible.md:107` / `[00:32:46]`:** "zero forms
  valued in the **positive** spinners, direct sum one forms valued in the
  **negative** spinners" — opposite halves, explicitly.
- **RECONCILIATION, `SC-CHI-01` p.52:** the total is non-chiral and *splits*, at
  the emergent level, conditioned on no VEV. So the two loci are not in
  contradiction: one is the declaration, the other is a half after the split.
  Draft §12.9's title says the same thing in the source's own words.
- **NOT SUPPORTED BY EITHER:** the same half twice. Canon already says so.

### 4.3 One site's conclusion depends on a reading — and it is the full-Dirac one

`explorations/conditional-build/selected-k77-zero-seed-h640-action-closure-controls-2026-08-11.md`
reports `H640 = 512 one-form directions + 128 zero-form directions`, and its probe
sets `spin = 128` — the **full** complex Dirac dimension of `Cl(7,7)`. Under any
Weyl-half reading the zero-form seed is 64-dimensional and the reported module is
a different object. **So this result is not reading-neutral: it presupposes
`S-FULL-DIRAC`, and it was not saying so.** It now says so, and the note states
the dependence explicitly rather than merely labelling the site.

This is the finding the brief asked for, and it is worth being precise about
which way it cuts: **no site's conclusion depends on the naive same-half
reading.** I looked for one and did not find one. The dependence that exists runs
to the reading the source literally declares, which is the benign direction.

### 4.4 The selectors — do `SC-CHI-01` and SG4 bit 2 presuppose a reading?

**`SC-CHI-01`: NO, and it is the one statement in the repository that already
carried the distinction correctly.** Its verbatim is "a **non-chiral total
theory** splits at the emergent level into two separate chiral theories". That
*presupposes the full-Dirac total* and types chirality as an output. It cannot be
read as presupposing the same-half declaration. The gap is smaller and different:
`SC-CHI-01` does not record **which pairing each emergent half is**, and CR-B
§3.3's arithmetic says the two halves are exactly the two class-homogeneous
*opposite-half* pairings. That is an available sharpening of a register note, not
a defect, and it is canon-adjacent, so it is proposed (§6) and not applied.

**SG4 bit 2: NO presupposition — but there is a real second-order finding, and it
is a SCOPE defect rather than a presupposition.** Bit 2 is stated in
`canon/gu-forces-field-space-declaration-RESULTS.md:69` as *"phase:
chiral/unbroken vs massive/super-Higgs"*. That is a phase bit whose two values are
compatible with either reading, and it aligns cleanly with `SC-CHI-01`'s VEV
condition. Nothing there presupposes a chirality assignment.

The finding is upstream of the bit, in the enumeration the 2-bit residual was
measured over. `tests/gu-forces/leg_a_forcing_enumeration.py` C6a codes GU's
field-content commitment with `rules_out_field=set(), rules_out_inv=set(),
rules_out_phase=set()` and notes:

> "**NEUTRAL at the declaration level.** `Omega^1(S)` is the COMMON arena of all
> three carriers; A (full), B (ker Gamma), and bare (`T_C`) are three DECLARATIONS
> on this same `Omega^1(S)`. Naming `Omega^1(S)` does not itself impose ker Gamma
> or a gauge invariance -- that IS the SG4 gap."

That neutrality claim is **true on the leg's three coded axes** (field,
invariance, phase) and **over-broad as written**, because *there is no chirality
axis among the three*. Naming `Omega^1(S)` is indeed neutral between carriers A,
B and bare; it is **not** neutral between `S-FULL-DIRAC`, `S-HALF-OPPOSITE` and
`S-HALF-SAME`, and that third distinction was never in the cell space. Note also
that C6a's own `source=` field already cites **both** loci — `[00:49:16]`
(unsubscripted) and `[00:32:46]` (opposite-half) — and the note then collapses
them to one unsubscripted symbol. The two source lines were in the file and the
distinction between them was not.

**Consequence, stated at its real size and no larger.** This does not move SG4's
2-bit result, which is about the carrier axes it measured. It does mean that
CR-B §4.3's identification of the carrier fork with "SG4 bit 2" is an
**identification CR-B makes, not one this enumeration licenses** — bit 2 is a
phase bit, and mapping a content fork onto it is a further step. The step looks
sound (`SC-CHI-01`'s condition and bit 2's phase are the same VEV), but it is a
step, and CR-B presents it as a terminus. Recording that is the honest thing.

**And I did not edit `leg_a_forcing_enumeration.py`.** It is a *predeclared*
commitment record whose value rests on the anti-p-hacking receipt that every
commitment was coded before the enumeration ran. Rewriting a predeclaration after
seeing the result is precisely the move the record exists to prevent. Proposed
diff in §6; file untouched.

---

## 5. The arithmetic, recomputed independently

CR-B owns this result. §5 reproduces it from scratch — different code, no import
— because a census that merely counts strings has no way to show that the strings
*matter*.

### 5.1 The instrument

For `D_n` the representation ring is graded by `P/Q`. In **doubled** integer
weight coordinates, `cls(lambda) = (sum of doubled coordinates) mod 4`, well
defined because every `D_n` root has doubled-coordinate sum in `{0, ±4}`
(verified for `n = 4,5,6,7`). At `D_7`:

```
    cls(S^+) = 3     cls(S^-) = 1     cls(V) = 2     cls(ad) = 0
```

and all 64 weights of each half share one class, so the class is a property of
the module. The `1`-form index shifts by `cls(V) = 2`.

### 5.2 The four pairings — and a correction to CR-B's phrasing

```
    Omega^0(S+) | Omega^1(S+)   classes (3,1)   homogeneous=False  protected=False
    Omega^0(S+) | Omega^1(S-)   classes (3,3)   homogeneous=True   protected=True
    Omega^0(S-) | Omega^1(S+)   classes (1,1)   homogeneous=True   protected=True
    Omega^0(S-) | Omega^1(S-)   classes (1,3)   homogeneous=False  protected=False
```

**Correction.** CR-B's summary line, and the CN-2 brief after it, say the
same-half reading is "**the one** pairing that is class-MIXED". Computed, **two**
of the four are class-mixed, and both are same-half. They are one pairing *only up
to the global `+/-` relabelling* — which is a real invariance, and CR-B's own §3.3
table shows both rows, so this is a compression in the headline rather than an
error in the work. The precise statement, which is what the repaired sites now
carry, is: **a 0-form slot and a 1-form slot are class-compatible exactly when
they carry OPPOSITE halves.**

The full Dirac bundle carries **both** classes `{1,3}` and so is not
class-homogeneous either — which is why the probe requires `cls_of` to *refuse* a
class for it rather than silently pick a representative. That refusal is a check,
and one of the 15 mutations targets it.

### 5.3 The contrary control

At `D_6` — **twelve** dimensions — `-w_0 = id`, the half-spinor weight multiset is
closed under global negation, and `cls(S^+) = 2` is **even**, so a same-chirality
invariant is allowed and the instrument returns *not protected*. Rank parity
across `D_4..D_7` is `{4: False, 5: True, 6: False, 7: True}`: the mechanism is
`D_n` rank parity, **nothing about signature**. A second independent leg (`-w_0`
by weight-multiset negation) agrees: at `D_7` the halves swap, at `D_6` they do
not.

**What this leg does NOT establish.** It does not say GU is chiral, is not
chiral, or has any `n_g`. It says only that the three readings of the shorthand
are **inequivalent objects**, which is the entire justification for making the
notation distinguish them.

---

## 6. Proposed diffs for the surfaces CN-2 may not edit

**None of the following was applied. All four files are byte-unchanged, and the
probe asserts they carry zero CN-2 tokens.**

### 6.1 `canon/source-action-seiberg-witten-construction.md` (line 56)

```diff
 On the 4-base `X^4` with the chimeric spinor field `Psi` (the GU vector-spinor, a section of
-`Omega^1(S) (+) Omega^0(S)`) and the IG connection `A`:
+`Omega^1(S) (+) Omega^0(S)`, with `S` the FULL Dirac bundle — the two slots are not
+here assigned Weyl halves, and the same-half reading is stated by neither primary,
+cf. `canon/escape-corners-campaign-RESULTS.md`) and the IG connection `A`:
```

*Why it is safe:* the Seiberg-Witten strawman's moment map `mu(Psi)` and its
`Lambda^2_+` target are stated on `X^4`, not on an ambient Weyl half; the
addition records what `S` is and changes no quantity.

### 6.2 `canon/boundary-einvariant-and-the-tangential-fork.md` (line 162)

```diff
-- **GU citations.** The draft introduces the fermion `zeta` as a **spinor-valued 1-form** on `Y` (`zeta in Omega^1(Y, S)`), with the horizontal piece `U` ...
+- **GU citations.** The draft introduces the fermion `zeta` as a **spinor-valued 1-form** on `Y` (`zeta in Omega^1(Y, S)`, `S` UNSUBSCRIPTED at the locus — the full Dirac bundle, cf. eq (9.16) and its four fields `nu±`, `zeta±`), with the horizontal piece `U` ...
```

*Why it is safe:* the tangential-fork argument turns on the horizontal/vertical
split of the form index, not on the spinor half; the addition is a typing note.

### 6.3 `canon/escape-corners-campaign-RESULTS.md` — **no diff proposed**

This file is **already correct** and is the repair's warrant. Recorded here so
the absence is deliberate rather than an oversight.

### 6.4 `tests/gu-forces/leg_a_forcing_enumeration.py` C6a note (§4.4)

```diff
-    note=('NEUTRAL at the declaration level.  Omega^1(S) is the COMMON arena of all three carriers; '
+    note=('NEUTRAL at the declaration level ON THE THREE AXES CODED HERE (field, invariance, '
+          'phase).  Omega^1(S) is the COMMON arena of all three carriers; '
           'A (full), B (ker Gamma), and bare (T_C) are three DECLARATIONS on this same Omega^1(S). '
           'Naming Omega^1(S) does not itself impose ker Gamma or a gauge invariance -- that IS the '
-          'SG4 gap.  Rules out only exotic non-RS content.'),
+          'SG4 gap.  Rules out only exotic non-RS content.  NOT neutral on a FOURTH axis this '
+          'enumeration does not code: the CHIRALITY ASSIGNMENT on S.  The source field above '
+          'cites both [00:49:16] (unsubscripted) and [00:32:46] (opposite-half) and this note '
+          'collapses them; see CN-2.'),
```

**Owner's call, and it should probably be REFUSED as written.** Editing a
predeclared note after the enumeration ran damages the receipt. The better
disposition is a *separate* dated addendum recording the missing axis, leaving
the predeclaration frozen. Recorded as the preferred option.

### 6.5 Ledger surfaces — `NEXT-STEPS.md:1966,5685`, `DERIVATION-PROGRESS.md:1740`

Three occurrences, all in summary prose. Same additive treatment
(`S` = full Dirac bundle at the declaration; chirality assignment open). Left to
the ledger owner under the joe-directed no-ledger-movement rule.

---

## 7. Comparator routing — which route does this bind?

**Source-native half — this BINDS.** "The draft's eq (9.16) declares an
unsubscripted `S̸`", "the source's only explicit spoken chirality declaration is
the opposite-half pairing", and "the same-half reading is stated by neither
primary" are statements about **what the source declares**, carried by SHA-pinned
extractions, the claim register, and an existing canon line. The census and the
repair are likewise source-native bookkeeping.

**Comparator half — this does NOT bind.** The *reason the distinction matters*
— "class-mixed content is vectorlike", "`n_g = 0`" — is fork-1 comparator
vocabulary. This artifact **quotes** that reasoning from CR-B and neither
re-derives nor advances it. Under the boundary's symmetric rule, nothing here
moves a GU row in either direction, and the repair is deliberately built so that
it cannot: the majority token is `S-CHIRALITY-UNTYPED`.

**Forbidden summaries, named so they are not written.** *"CN-2 fixed the
chirality of GU's fermions."* No — it made 13 sites state which reading they use,
and ten of them state that they do not fix one. *"CN-2 shows the repo had the
wrong field content."* No — canon caught that in July for the one leg that
actually computed on it; CN-2 is the propagation, not the discovery. *"The
notation is now subscripted."* No — almost nothing was subscripted; the symbols
are unchanged and the *typing* is what was added.

---

## 8. Hostile review, inline

**Is the token an improvement or clutter?** Fourteen visible tokens in a
repository this size is close to homeopathic, and the honest risk is the
opposite of clutter: that the token is *too quiet* to stop the next HE-2. The
mitigation is placement — the `lab/active-research/joe-directed/README.md` token
sits in the paragraph that defines "candidate-2B" for the whole tree, which is
the sentence a new agent reads first. If the next carrier-adjacent swing still
reads the shorthand naively, this pass failed and the fix is a gate, not a note.

**Did I under-repair?** Yes, deliberately, and the number is 37 files. The
defence is the class table (§3.2) and it is checkable: in class T the file states
its own fibre dimension, in class O the fibre's chirality is not the object. But
"checkable" is not "checked" — I verified the dimension statement in `legb1`/
`legb2` and `leg2_krein_real_form` by reading them, and typed the remaining class-O
sites by pattern. **A residual risk of roughly a handful of miscategorised sites
is real and is not machine-excluded.** The probe asserts the classes I recorded;
it does not prove the classification is complete.

**Is the additive-only rule a dodge?** It is the reason nothing broke, and it is
also a limitation: an additive note next to a wrong symbol is weaker than a right
symbol. I chose it because rewriting `Omega^0(S)` to `Omega^0(S̸)` at 182 sites
would have been a large unreviewable diff across four concurrent agents' working
tree, and because in most of those sites the symbol is *not wrong* — it is
faithful to eq (9.16) and merely silent. Where a symbol would have been wrong,
canon had already refuted it.

**Strongest contrary construction against CN-2.** That the ambiguity is not
source-borne at all, and the repository simply mis-transcribed a subscripted
source. Checked and refused: the draft prints `nu±`, `zeta±` as four distinct
fields at eq (9.16) *while* the bundle is unsubscripted, prints four corners on
p.51, and titles §12.9 "Chirality Is Merely Effective and Results From Decoupling
a Fundamentally Non-Chiral Theory". An unsubscripted bundle with `±` on the
fields is a deliberate grammar, not a dropped subscript.

---

## 9. Postflight — five lenses

**Lens A — did the repair pick a side?** The check that matters: `S-HALF-OPPOSITE`
appears **zero** times, asserted, and planted as a false assertion. Ten of
thirteen sites took the ambiguous value. The one site typed to a definite reading
against its own text was `S-FULL-DIRAC` on the K77 H640 file, and there the note
*states the dependence* (`spin = 128`, which would be 64 under any half reading)
rather than asserting a source commitment. The residual worry is subtler: by
making `S-FULL-DIRAC` available and using it four times, I have made the
full-Dirac reading feel like the default. It **is** the default *at the
declaration locus*, which is exactly what those four sites are; it is not the
default for the operative content, and every one of the four says so.

**Lens B — strongest overclaim available, and where it is refused.** *"CN-2 shows
the repository's results were computed on the wrong content."* Refused. Exactly
one leg in repository history computed on the same-half content (A2), and canon
already refuted it in July. Every other site either states full-Dirac, or is
neutral because nothing downstream of it touches the chirality axis. The census's
finding is **silence, not error** — and silence is a documentation defect, which
is what CN-2 was scoped to fix.

**Lens C — weakest seam.** Two. (i) The classification of 37 files as T/O is
human judgement over a pattern, not a proof (§8). (ii) The census's repo-wide
totals are a dated snapshot on a checkout four agents are writing to; the
unsubscripted number held exactly across the pass and the subscripted number did
not, which is recorded in §3.1 rather than hidden. Anyone re-running this on a
different day should expect the `--strict` gate to need new constants and should
treat that as normal, not as a regression.

**Lens D — verdict typing.** CN-2 targets **CR-B §5's own flagged residual**, a
repository-internal item. It does not target `SC-GEN-53`, does not target any
source claim, is not a falsification of GU, and moves no register row. Against
CR-B the verdict is: **flag CONFIRMED, acted on, with one phrasing correction
(§5.2) and one scope caveat on its SG4-bit-2 terminus (§4.4)**. Against the
brief, the verdict is that its novelty premise was wrong (§1) and its "one
class-MIXED pairing" phrasing was imprecise (§5.2).

**Lens E — did anything break?** No. The additive-only rule was checked
mechanically: the eq (9.16) verbatim block is byte-identical and the four foreign
probes that string-match it are asserted to still match. `hull_interface_probe`
was run and passes; the other three fail at `import sage` before reading anything,
which is a pre-existing environment gap and not a CN-2 effect. Every substring I
modified was grepped across `tests/` and `process_gates/` first and had zero
matches. `W189_hardening_register_checks.py` has two failures — `wave46` at
`explorations/README.md:2999` and a gate-status test — both in regions I did not
touch (my edit is at line 2460) and both attributable to concurrent work.

---

## 10. Claim ceiling

- **Exact, and load-bearing:** the census (182 unsubscripted occurrences in 57
  files; 13 declaration sites; 14 tokens over 13 files; zero
  `S-HALF-OPPOSITE`/`S-HALF-SAME`); the byte-identity of the eq (9.16) block; the
  `D_7` classes `3,1,2,0` and the four-pairing homogeneity table; the `D_6`
  contrary control and the `D_4..D_7` rank parity; the identification of the K77
  H640 site as the one reading-dependent conclusion.
- **Standard representation theory, claimed novel by nobody:** the `Z/4` grading
  of the `D_n` representation ring; `-w_0` and the diagram automorphism. CR-B
  owns the application to GU's corners and is cited, not re-claimed (§1).
- **Source, quoted with loci, not interpreted:** eq (9.16) p.46; p.51 four
  corners; eq (11.6) p.52 / `SC-CHI-01`; §12.9 title p.60;
  `Transcript into the impossible.md:107`; transcript `[00:32:46]`, `[00:49:16]`.
- **NOT claimed:** which reading is GU's operative content; that GU is chiral;
  that GU is not chiral; an index; a generation count; a resolution of
  SIGNATURE-AMBIENT; any movement of `SC-GEN-53`, the count `{1,3}`, or SG4; that
  the T/O classification of the 37 unrepaired files is proven complete.
- **Claim-status movement:** none. `canon_verdict_change: none`.
  `canonical_effect: pending_integration`.

---

## 11. Did I preserve the ambiguity honestly, or quietly pick a side? — blunt

**I preserved it, and the structural reason is that I built the tool so that
picking a side would show up as a number.**

The vocabulary has four values and the fourth means "unresolved". Ten of thirteen
sites took it. `S-HALF-OPPOSITE` — the protected reading, the one it would have
been most flattering to GU and most convenient to CR-B to type everywhere — was
used **zero** times, that zero is asserted by the probe, and it is *also* planted
as a false assertion required to come back False, so a future edit that quietly
subscripts a site to the protected half turns the probe red. That is the strongest
guarantee I know how to give, and it is stronger than my say-so.

**Where I did pick, and it should be looked at.** Four sites are typed
`S-FULL-DIRAC`. Two of those (`b5-middle-source-freeze`, `de-packet`) already said
"full Dirac" in their own prose and I only added a countable token, so nothing was
decided. One is the eq (9.16) extraction, where "S is the full Dirac bundle" is a
statement about the *declaration locus* and is directly supported by the draft
printing four `±` fields under an unsubscripted bundle — and even there the note
ends by saying it does not decide what is operative in the built theory. The
fourth, the K77 H640 file, is a genuine decision, and it is the one I would
challenge first if I were reviewing this: I typed it `S-FULL-DIRAC` because its
arithmetic uses 128 and would use 64 otherwise. That is an inference from the
probe's constant to the author's intent. It is a strong inference and it is not a
source statement, and the note says so.

**The one place I think I am vulnerable** is the 37 files I did not touch. I
classified them as toy-arena or operator-domain by reading a sample and pattern-
matching the rest. If even one of those is actually a field-content declaration
whose downstream conclusion turns on the chirality axis, the census under-reports
and the repair is incomplete. I found no such case and I did not prove there is
none, and the difference between those two sentences is the honest size of this
pass.

**And the thing I would most want a reader to take away is not the repair.** It is
§1: the repository had already found this, twice, and put it in canon — and then
a later swing read the shorthand naively anyway, because the notation never
carried the finding. The defect CN-2 fixes is not that the repository was wrong
about the carrier. It is that being right in one file does not propagate.
