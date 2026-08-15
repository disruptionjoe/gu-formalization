---
artifact_type: exploration
status: exploration
doc_type: typing-census-and-retyping-delta
created: 2026-08-15
work_item: IT-C
channel: indefiniteness_typing
route: CENSUS__TYPE_THE_POSITIVITY_BEARING_ROWS_AGAINST_SOURCE_POLARITY
base_revision: not-read (no git commands run in this channel)
ledger_base: lab/process/conditional-physics-ledger-v0.258.json
ledger_base_sha256: 540b50e386073c0f43da4e8d5a8ffdaf06fd243c6612622d7daf187c0a725047
ledger_edit: none -- versionless delta, for the canonical owner to disposition
target_claim: "NONE-NOT-A-KILL at the source layer. The target is INTERNAL: the
  conditional-physics ledger's OWN typing of its positivity-bearing rows --
  specifically the assertion carried by `reason_kind: MISSING_CONSTRUCTION` on
  `LT-SM8` (`BV/BRST quotient yields a positive physical space`), and the
  single-`reason_kind` typing of the compound revival triggers on `RA-D4` and
  `RA-G2`. Two register claims are USED AS EVIDENCE and are neither attacked
  nor defended: `SC-META-53` (polarity UNCERTAIN -- `How do you deal with
  unbounded spectra? Well, I don't know`) and `SC-SIG-52` (polarity ASSERTS,
  with a `to-be-figured-out` clause). No GU source claim is targeted."
target_claim_verdict: "PARTIALLY CONFIRMED, AND THE CLASS IS SMALLER THAN THE
  BRIEF ASSUMED. The positivity-bearing class in demand fields is FIVE rows, not
  ten, and it intersects BD-D's ten-row Hessian class in exactly ONE row
  (`RA-D4`). Of the five, exactly ONE (`LT-SM8`) is mis-typed in the LA-11/BD-C
  manner and its re-typing is proposed CONDITIONAL on a named bridge. TWO
  (`RA-D4`, `RA-G2`) carry compound triggers whose conjuncts have different
  types and cannot honestly share one `reason_kind`; no verdict or kind moves
  for either. TWO (`AC-F1`, `LT-GR2c`) are examined and DECLINED -- the evidence
  does not force a change, and `LT-GR2c` is a homonym catch. Rows advanced: 0.
  Rows moving status: 1, in the direction that makes the ledger worse."
canon_verdict_change: none
priority_change: none
steering_effect: unchanged
canonical_effect: pending_integration
title: "IT-C: the positivity class is FIVE rows and one word. `ghost`,
  `definite`, `unitarity`, `signature`, `coercive` and `semidefinite` occur ZERO
  times in all 84 rows of v0.258; `Krein` occurs ONCE, in a non-demand field.
  The entire ledger contact with the source's declared-open indefiniteness
  problem is the token `positive`/`positivity` in five demand fields. BD-D's ten
  Hessian rows and these five share exactly ONE member. `LT-SM8` -- the row
  whose own summary IS positivity -- carries `MISSING_CONSTRUCTION`, a kind that
  grants the construction exists; `CB-B:SM-8` sources the criterion from the
  IMPORTED `[S]` comparator, `M-H17` records the only known exit as blocked, and
  `SC-META-53` records the author declining to supply a mechanism. The grant is
  unavailable. Proposed: a new NEEDS kind that is STRICTLY MORE indebting."
rows_touched_structurally: [LT-SM8, RA-D4, RA-G2, AC-F1, LT-GR2c]
rows_moving_status: 1
rows_advanced: 0
rows_declined_after_examination: 3
denominator_move: none
---

# IT-C — the positivity rows, typed

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`

**Why that classification.** The census in §2 is purely internal — it reads the
repository's own ledger and counts tokens, and nothing in it borders a
comparator. But the *adjudication* in §4 turns on whether "a positive physical
space" is a GU demand or an imported one, and the answer comes from
`explorations/conditional-build/cb-b-lagrangian-terms-2026-08-05.md`, whose
`SM-8` row is explicitly typed `[N|S]` — *"where the row is precisely a
comparison between the two"* (`:191-193`) — with the `[S]` side reading
*"**Physics writes:** `-(1/2 xi)(partial . A)^2 + c-bar partial^mu D_mu c`"*.
Positivity of the physical state space is the imported side of that comparison.
An artifact whose central move is "this demand came from the comparator, not the
source" sits on the boundary by construction, and declares it.

---

## 0. PREFLIGHT — retrieval first, then seven lenses

### 0.1 Retrieval performed BEFORE any typing work

| # | retrieved | what it fixed |
|---|---|---|
| R1 | `lab/process/conditional-physics-ledger-v0.258.json`, sha256 `540b50e3…a725047`, 84 row records, 82 canonical targets | the base. Latest version present on disk; `v0.259+` does not exist |
| R2 | `bd-d-…-2026-08-15.md:56` `rows_touched_structurally` and `:746-762` | BD-D's class-H list and its rule, replayed rather than quoted (§2.3) |
| R3 | `bd-c-…-2026-08-15.md:655-672` §4.4 | the disavowal, with its own explicit fence: *"It may still be the right physics demand — this artifact takes no position on that"* |
| R4 | `papers/drafts/Transcript into the impossible.md:155` (copy A1, the complete one) | the `[00:45:00]` sentence, read directly, not via the edited `lab/literature/` derivative |
| R5 | `papers/drafts/Transcript into the impossible.md:107,119,125,131,158` | the coordinator's five additional loci, each verified verbatim against A1 (§3.2) |
| R6 | `lab/sources/source-claim-register.yaml` `SC-META-53`, `SC-SIG-52`, `SC-GEN-54` | register polarity, so the typing rests on `polarity:` fields and not on my reading of a transcript |
| R7 | `explorations/conditional-build/cb-b-lagrangian-terms-2026-08-05.md:191-193, 1071-1112, 1222` | `SM-8`'s provenance code, its stated object, and its `REQUIRES-UNKNOWN U11` classification |
| R8 | `lab/process/improvement-register-2026-08-03.md:350` | `M-H17`, the register ID for the only named exit; status column `L (blocked)` |

**Which transcript copy.** All quotes in this artifact are from
`papers/drafts/Transcript into the impossible.md` — copy **A1**, 176 lines,
ending `[00:50:09]`. The `lab/literature/weinstein-ucsd-2025-04-transcript.md`
copy is an **edited derivative** at different line numbers whose own front
matter (`:13-45`) records that it deleted a clause at `[00:45:00]` until
2026-08-15. I did not rely on it. Every line number below was re-read from A1
before use.

### 0.2 Is IT-C still the right target after today's committed base-duality wave?

**What moved in the ranking, and it moved IT-C *down* on one axis and *up* on
another.**

*Down.* The brief opens by pointing at BD-D's ten Hessian-class rows as "the
obvious starting set." Retrieval R2 plus the §2 census shows those ten are a
**spectrum-demand** class, not a positivity class: nine of the ten contain no
positivity-family token anywhere in any field. If IT-C had been run as
"re-type BD-D's ten," it would have re-typed nine rows on a word none of them
contains. So the ten-row framing is **retired here**, and the brief's own hedge
— *"not necessarily the right set — derive your own"* — is the operative
instruction.

*Up.* BD-C §4.4 and BD-D §7 both stop one step short of the ledger. BD-C
adjudicates `LT-GR6b` — a **proposed** row that does not exist in v0.258
(verified: zero occurrences of the string `LT-GR6b` in the ledger file). BD-D
re-types `LT-GR6b`'s subclause. **Neither wave touched a row that is actually
in the ledger.** Every positivity finding banked on 2026-08-15 is currently
attached to an unmerged proposal. That is the gap IT-C occupies, and it is a
real one.

*Unchanged.* BD-D's no-go is scoped `BRIDGE_OR_SEMANTIC_BOUNDARY` because it
imports a Yang–Mills constraint symbol. That scope survives into IT-C and
becomes the named condition on the one re-typing I propose (§5, `D1`). It is not
laundered away by being restated.

**Verdict: IT-C is the right target, with a corrected object.** Not "the ten
Hessian rows," but "the rows that actually carry the word."

### 0.3 Seven problem-matched lenses

**L1 — type-systems and taxonomy design.** A `reason_kind` is a *typed claim
about why the row has not moved*. `MISSING_CONSTRUCTION` is existentially
loaded: it asserts a construction is the missing thing, which presupposes the
construction is a thing that could be had. Compare `PROVEN_UNSUPPLYABLE` and
`PROVEN_UNABLE_BY_CURRENT_ACTION`, which are the taxonomy's two ways of saying
"and it can't be had." Between "unbuilt" and "proven impossible" the v0.258
taxonomy has **no cell** for "nobody, including the theory's author, has a
route." The taxonomy anticipates exactly this: `extensible: true`,
`unknown_kind_rule: NEW_KIND_REQUIRED__FORCED_FIT_FORBIDDEN`. Forcing
`MISSING_CONSTRUCTION` onto such a row is the forbidden forced fit. **This lens
supplies the delta's mechanism and its licence.**

**L2 — indefinite-inner-product spaces (Krein/Pontryagin).** On a Krein space
`(K, J)` there is no absolute notion of "positive"; there is a *fundamental
symmetry* `J`, a `J`-decomposition `K = K_+ ⊕ K_-`, and definiteness statements
relative to `J`. A demand reading *"positive-definite on the Krein carrier"* —
which is `cb-b-lagrangian-terms:1100-1101`'s own wording for `SM-8`'s object — is
therefore **not** a demand for positivity of the ambient form. It is a demand
for a subspace on which the indefinite form restricts positively, together with
a `J` witnessing it. That is a strictly *harder* object than "a positive form,"
because it requires the decomposition as well as the sign, and it is precisely
the object BD-A's Lens Q2 proposed and BD-D priced at one Cartan involution. The
ledger's one word `positive` compresses a two-part demand into a sign. **This
lens says the demand is under-specified, not merely mis-typed.**

**L3 — ledger/claim-status epistemics.** Grants and debts are not symmetric. A
row carrying `MISSING_CONSTRUCTION` costs the program one debt and pays it one
implicit **grant**: that the debt is payable. Re-typing that removes the grant
while keeping the debt is a net loss for the program. Re-typing that removes the
debt is laundering. The test I will apply in §6 is exactly this: *after the
delta, is the debt still counted?* If the row leaves the `NEEDS` family, the
denominator moves, or the row stops appearing in `next_work_queue`, the delta
has laundered.

**L4 — source philology.** Three separate hazards, all live here. (i) *Copy
hazard*: two UCSD transcripts exist, one an edited derivative that until today
deleted a clause in the very paragraph at issue. Handled by reading A1 only.
(ii) *Attribution hazard*: `SC-META-53`'s own `notes` field records that *"The
opening question is the interviewer's; the 'Well, I don't know' and the
shielding claim are the author's."* So the disclaimer is authorial, and the
question framing is not. (iii) *Absence hazard*: `Krein` and `ghost` are absent
from the verbatim corpus. Absence of a solution's vocabulary is evidence the
source did not supply the solution. It is **not** evidence the solution is
unavailable, and it is **not** evidence the problem is unimportant.

**L5 — gauge-theory consistency.** Where is positivity actually required? Not on
the kinematic carrier — `cb-b-lagrangian-terms:714-716` records `F = empty` there
as *"signature-robust"* and notes the situation is *"normal for covariant
indefinite theories (Gupta-Bleuler)."* Covariant QED is the standard case: the
Gupta–Bleuler metric is indefinite and positivity is recovered only on
`ker(∂·A)^(+) / null`, i.e. on the BRST cohomology. So the ledger is right that
positivity belongs at `H⁰(Q)` and nowhere earlier. **The demand's location is
correct.** What is at issue is only its *type*.

**L6 — adversarial reading / laundering detection.** The single most dangerous
sentence I could write in this artifact is "the source declares this open, so
the repository does not owe it." I pre-commit against it here: the delta below
keeps every affected row in `NEEDS`, keeps the denominator at 82, keeps
`LT-SM8` in `next_work_queue` rank 3, and adds a mandatory non-discharge note to
the new kind. §6 is written to attack my own delta on this exact axis.

**L7 — corpus linguistics / matching-rule design.** Two failure modes. *Low
recall*: `mapping_grade` fields are `SCREAMING_SNAKE`, so `\b` word boundaries
silently miss `LOCAL_K_LOC_NONDEGENERATE_INDEFINITE` because `_` is a word
character. My first pass had this bug and it hid `LT-GR5` entirely; the fix is
to tokenise on `[A-Za-z]+`. *Low precision*: `norm` matches `normalized`,
`normal`, `normalization` — four rows entered the candidate set on that
substring and all four are false positives. Both failure modes are recorded in
§2.1 as part of the rule, not hidden.

---

## 1. THE MATCHING RULE, STATED BEFORE IT IS RUN

**Rule P (the positivity-bearing class).** A row `r` of `v0.258.rows` is in
class **P** iff, after tokenising on `[A-Za-z]+` (so `SCREAMING_SNAKE`
compounds decompose), at least one of the three **demand fields**

  `reason_kind`, `distance`, `revival_trigger`

contains a case-insensitive token from the **positivity lexicon**

  `positive, positivity, definite, definiteness, indefinite, indefiniteness,
   semidefinite, coercive, krein, ghost, ghosts, unitary, unitarity, signature,
   nondegenerate, inertia, norm, normed, psd, pseudounitary, degenerate`

**Why the demand fields and not all fields.** `reason_kind`, `distance` and
`revival_trigger` are the fields that state *what must happen for the row to
move*. `summary` states the comparison target; `mapping_grade` and
`frontier_grade` record what is already computed; `evidence` is a pointer. A
positivity word in `mapping_grade` is a **finding**; the same word in
`revival_trigger` is a **demand**. Only demands can be mis-typed as debts,
because only demands are debts. This distinction is what makes the rule
answerable to the brief's question rather than to a word count.

**Rule P′ (the extended class).** Same lexicon, all nine string fields. Reported
separately in §2.2 so that the two rows that appear only under `P′` are visible
and can be argued about rather than silently dropped.

**Rule H (BD-D's class, replayed not quoted).** A row is in class **H** iff a
demand field names a Hessian, mass matrix, eigenvalue, spectrum, pole, second
variation or stability. Replayed independently in §2.3 so the comparison in
§2.4 is between two rules I ran, not between my rule and BD-D's prose.

**Precision hazard declared in advance.** `norm` is in the lexicon and will
over-match `normalized`/`normal`/`normalization`. Every `norm` hit is
individually adjudicated in §2.2 and none survives. It is in the lexicon anyway
because dropping it would have made the rule unable to catch a genuine
`negative norm` demand had one existed.

---

## 2. THE CENSUS

### 2.1 Absence certificate — the whole lexicon, all 84 rows, all nine fields

| token | occurrences across all 84 rows × 9 fields |
|---|---|
| `positive` | **8** |
| `positivity` | **1** |
| `krein` | **1** |
| `indefinite` | **1** |
| `unitary` | **1** |
| `inertia` | **1** |
| `nondegenerate` | **1** |
| `ghost` | **0** |
| `ghosts` | **0** |
| `definite` | **0** |
| `definiteness` | **0** |
| `indefiniteness` | **0** |
| `unitarity` | **0** |
| `signature` | **0** |
| `coercive` | **0** |
| `semidefinite` | **0** |
| `norm` (standalone token) | **0** |
| `degenerate`, `psd`, `pseudounitary`, `normed` | **0** each |

**Fourteen of the twenty-one lexicon tokens occur zero times.** The ledger's
entire vocabulary for the indefiniteness problem is one word with two
inflections, `positive` and `positivity`, plus three isolated descriptive tokens
in non-demand fields.

**The `Krein` occurrence is singular and it is not a demand.** It is
`LT-GR2c.construction_scope`, inside the compound
`K77_FIRST_JET_NO_LEAKAGE__…__COUPLED_DEFECT_KREIN_GREEN_DOMAIN__TWO_SIMPLE_POLES`.
`construction_scope` records the scope of a completed construction. So: **zero
rows of v0.258 demand a Krein structure, ghost clearance, or unitarity of an
indefinite form in a demand field.** The brief's suspicion is about a class that,
in demand form, consists of one word.

**Where the ghost vocabulary went.** Not into the rows. Outside `rows[]` —
in `migrations`, `migration_history` and the narrative fields — `ghost` occurs
40 times and `Krein` 6. So the repository's ghost/Krein work is recorded as
*history* and *scope*, and none of it has ever been written into a row's demand.
That is a defensible design (findings are not demands) but it means the ledger's
row layer is blind to the structure the rest of the ledger has been building.

### 2.2 Class P and class P′

**Class P — exactly FIVE rows.** Every hit is `positive` or `positivity`; no
other lexicon token appears in any demand field of any row.

| # | row | axis | verdict | reason_kind | the token, in situ |
|---|---|---|---|---|---|
| 1 | `RA-D4` | REPRESENTATION | NEEDS | `MISSING_CONSTRUCTION` | `revival_trigger`: *"a **positive** BRST cohomology with chiral light spectrum"* |
| 2 | `RA-G2` | REPRESENTATION | DIFFERS | `PREDICTION` | `revival_trigger`: *"a **positive** physical cohomology without mirror states"* |
| 3 | `LT-GR2c` | LAGRANGIAN | NEEDS | `MISSING_CONSTRUCTION` | `revival_trigger`: *"…with covariance, **positivity**, domain and observation descent…"* |
| 4 | `LT-SM8` | LAGRANGIAN | NEEDS | `MISSING_CONSTRUCTION` | `distance`: *"…a Lorentzian closed domain, **positive** pairing and nontrivial physical cohomology"* |
| 5 | `AC-F1` | ANOMALY_CONSISTENCY | NEEDS | `MISSING_CONSTRUCTION` | `distance`: *"…proper functional BV/BFV, a **positive** observed domain and physical cohomology…"* |

**Class P′ adds exactly TWO, and both are excluded with grounds.**

| row | where the token is | why it is not in P, and why the exclusion is right |
|---|---|---|
| `LT-GR2` | `summary`: *"**positive** cosmological-term sign"* | (i) not a demand field — this is the comparison target, a sign convention on `Λ`, not a state-space condition; (ii) the row carries `row_status: SUPERSEDED` with five successors and a `superseded_reason`. A superseded row is not a live typing target. **Homonym: this `positive` is the sign of a cosmological constant, unrelated to definiteness of a form.** |
| `LT-GR5` | `mapping_grade` only: `LOCAL_K_LOC_NONDEGENERATE_INDEFINITE`, `FULL_SUPPORT_INERTIA_4_6`, `AUGMENTED_TORSION_EULER_CLOSURE_SPIN113893_OR_UNITARY229477` | not a demand field. And this row is the **counter-example that shows the ledger can do this correctly**: it records the local form as nondegenerate-and-indefinite with exact inertia `(4,6)` as a computed finding, and its `revival_trigger` demands *"a common Green/BV/Fock domain"* — a domain, not a sign. `LT-GR5` observes the indefiniteness and does not demand it be cured. That is the right handling and no delta is proposed. |

### 2.3 Class H, replayed

Rule H returns **exactly ten** rows: `RA-A4, RA-A5, RA-B6, RA-D4, RA-E4, RA-E6,
RA-G1, RA-G4, LT-SM4, LT-SM6`. This reproduces BD-D `:56` element-for-element,
independently derived. BD-D's replay of its own class is confirmed.

### 2.4 Where I differ from BD-D, and it is the headline

```
|P| = 5      |H| = 10      |P ∩ H| = 1      |P ∪ H| = 14
P ∩ H = { RA-D4 }
```

**Nine of BD-D's ten Hessian rows contain no positivity-family token in any
field whatsoever.** They demand mass matrices, spectra, poles and Hessians. BD-D
is right that a *real physical spectrum* requires a definite descended pairing —
that is a physics implication and I do not dispute it — but the implication is
BD-D's, not the rows'. Those nine rows do not say the word.

The consequence for method is sharp. **BD-D's ten and the brief's "positivity
rows" are different objects, and treating them as one would have produced nine
re-typings on an inference rather than on a text.** A re-typing has to be
answerable to what the row says, because the row is the artefact the canonical
owner reads. Attaching a re-typing to nine rows on the strength of a chained
implication is exactly the kind of move that later reads as laundering, and it
would have been the largest such move in this file. It is declined.

`RA-D4` is the sole row in both classes, and correspondingly it is the only row
where BD-D's `n_κ = 0` pricing and this artifact's typing both bear on the same
text.

---

## 3. WHAT THE SOURCE ACTUALLY DOES, IN THREE BUCKETS

### 3.1 The buckets

- **(a) DECLARES OPEN, no mechanism supplied.** The author names the problem and
  says he does not know.
- **(b) STATES A CONDITIONAL.** The author supplies a mechanism *with an
  explicit* `if`. The condition is source-stated, so it stays owed — as a
  condition.
- **(c) SUPPLIES, and the ledger did not notice.** The `BD-C` failure mode.

### 3.2 The loci, each verified verbatim in copy A1 before use

**(a) — `:155`, `[00:45:00]`.** Verified; the stray comma in *"the,
indeterminacy"* is present in the file and is reproduced:

> *"…this spin 10 is not right. We wasted the seventies work because we wanted
> to avoid indefinite signature on the killing form, and I don't know what to do
> because we're in a maximally compact subgroup. We're shielded experimentally
> from understanding how nature handles the, indeterminacy of the killing form.
> But this is the right chain. Spin six four, spin three comma two, s u three
> cross s u two cross u one…"*

Register: `SC-META-53`, `polarity: UNCERTAIN`, twin at ToE `[01:22:30]`
(*"How do you deal with unbounded spectra? Well, I don't know"*). Its `adherence`
note is itself the relevant repository fact: *"the shielding claim is not
carried as a mechanism: the compact reduction is typed `REDUCTION_EXTERNAL` and
positivity work runs on the Krein keep-and-grade posture instead."*

**(b) — `:158`.** Verified verbatim; note the ASR rendering *"two vial
equations"* for *two Weyl equations*:

> *"We fed Salam Strathy, which always needs to eat an affine space, the wrong
> affine space. Don't feed it Minkowski space. Feed it the space of connections.
> Then the Lorentz group is the gauge group. …the fermionic extension gives you
> exactly three families of chiral fermions **if** you have a decreased VEV in
> the total space taking a Dirac equation into two vial equations because the
> mass is actually a variable…"*

Register: this exact sentence is carried in `SC-GEN-54.notes` as the *"[s]eminar
twin at ucsd:158"* of the supercharge-extension count mechanism, and the note
flags it as *"[o]ne of THREE coexisting spoken count mechanisms."* So the
repository already knows this is a conditional and already knows it is one of
three. **`if` is the author's word.** It is a source-stated condition, not a
repository grant.

**(b), context — `:119` and `:131`.** Verified:

> `:119` *"…which will yield you three families, really two plus one. The third
> family is an imposter for representation theoretic reasons, but at low energy,
> it'll look the same as the other two."*
>
> `:131` *"…in g u, there's one family of 16 flipped chiral spin three halves
> particles. That is, there is a sort of spin three halves family, which aside
> from being spin three halves is just the conjugate of the internal symmetry
> representation."*

**(c) candidates — `:107`, `:125`, `:149`.** Verified:

> `:107` *"…if you pull back ordinary spinners, zero forms valued in the
> positive spinners, direct sum one forms valued in the negative spinners on
> that top space, you're gonna get three generations of standard model
> fermions."*
>
> `:125` *"…why doesn't grand unification work? There is no grand unification.
> It's just a normal bundle in your ambient space."*
>
> `:149` *"You trace reverse the Frobenius metric along the fibers, which gets
> you from a seven three signature to a six four."*

Note `:107`'s *"positive spinners"* is a **chirality** label — positive/negative
half-spin bundles — and has no relation to definiteness of a form. It is the
third distinct sense of "positive" in this file's evidence base, after
`LT-GR2`'s cosmological sign and `LT-SM8`'s state-space definiteness.

### 3.3 The bucket split for class P, with counts

The brief's coordinator asked for this split with counts and warned that a
uniform answer is a warning about the matching rule. **The answer is not
uniform.**

| row | bucket of its **head demand** | bucket of its **other conjunct(s)** | uniform? |
|---|---|---|---|
| `LT-SM8` | **(a)** — the summary itself *is* positivity of the physical space | — | wholly (a) |
| `RA-D4` | **(a)** — *"a positive BRST cohomology"* | **(b)** — *"chiral light spectrum"* / no light mirror partners; `:158`'s conditional and `:119`'s imposter | **mixed** |
| `RA-G2` | **(a)** — *"a positive physical cohomology"* | **(b)** — *"without mirror states"* | **mixed** |
| `AC-F1` | **(b)** — `revival_trigger` is *"a physical chiral carrier with a derived index"*, which contains **no** positivity token | (a) appears only as construction **step 3** inside `distance` | **mixed, and the head is (b)** |
| `LT-GR2c` | **neither** — homonym; positivity of a normalized global *functional*, not of a state-space form | — | n/a |

**Counts: (a) wholly 1 · mixed (a)+(b) 3 · homonym-excluded 1 · (c) 0.**

**Bucket (c) is empty in class P, and I am not going to manufacture an entry.**
No positivity-bearing row demands something the source supplies. `BD-C`'s
failure mode does not recur here.

**But there is a (c)-shaped finding one level up, and it is an absence of a row
rather than a mis-typed row.** The source supplies a signature datum twice —
`:149`'s *"seven three signature to a six four"* and `SC-SIG-52`'s *"the trace
portion of the space of metrics is put in with the proper sign"*. Across all 84
rows: `signature` occurs **0** times; the strings `6,4`, `7,3`, `Spin(6`,
`Spin(3`, `trace revers`, `Frobenius` each occur **0** times. **Zero ledger rows
carry the source's own signature data.** That is a missing row, not a wrong one,
and writing it is outside this channel's mandate. It is flagged as `D7` for the
canonical owner and nothing is proposed.

### 3.4 The row where bucket (b) actually lands, and it is *not* in class P

`RA-D2`'s summary is *"the stated VEV/mass mechanism produces low-energy
chirality"* — that is `:158`'s conditional, written as a ledger row. Its typing
is `OVER_DETERMINED / GENUINE_FALSIFICATION`, and its `revival_trigger` is *"an
exact chiral physical carrier not obtained by equivariant mass splitting."*

This matters for honesty in both directions. **The ledger is not soft on bucket
(b).** The one row that carries the source's own conditional mechanism is typed
at the harshest severity the taxonomy offers. Any narrative in which the
repository under-types source-stated conditions is refuted by `RA-D2`, and I
will not tell that narrative. `RA-D2` contains no positivity token in a demand
field and is correctly outside class P; no delta is proposed for it.

---

## 4. THE RE-TYPING PASS, ROW BY ROW

### 4.1 `LT-SM8` — MIS-TYPED. The one status move.

**Base record.** `verdict: NEEDS`, `reason_kind: MISSING_CONSTRUCTION`,
`summary: "BV/BRST quotient yields a positive physical space"`, `source_row:
CB-B:SM-8`.

**What `MISSING_CONSTRUCTION` asserts.** That the reason the row has not moved
is that a construction has not been performed. That presupposes the construction
is performable — the type carries an availability grant. This is exactly the
structure `BD-C` found unavailable for `LA-11`'s proposed `LT-GR6b`, where the
demanded object turned out to be supplied rather than owed. Here the failure is
the mirror image: the object is neither supplied nor known to be constructible.

**Four grounds, in order of independence from this artifact's own reasoning.**

**G1 — the criterion is imported, not native.** `CB-B:SM-8` is typed `[N|S]`,
and the legend at `cb-b-lagrangian-terms:191-193` reads *"`[S]` where a
standard-field object is imported for comparison, and `[N|S]` where the row is
precisely a comparison between the two."* `SM-8`'s `[S]` side is *"**Physics
writes:** `-(1/2 xi)(partial . A)^2 + c-bar partial^mu D_mu c`, with `xi` a free
gauge parameter."* Positivity of the BRST-reduced state space is a property of
that imported standard, and GU is not on record demanding it. This is `BD-C`
§4.4's finding, arrived at by a different route: BD-C got there from the
`[00:45:00]` disavowal, this gets there from the comparison-basis provenance
code. Two independent routes, same answer.

**G2 — the repository's own statement of the object already concedes the
carrier is indefinite.** `cb-b-lagrangian-terms:1095-1103`:

> *"`F = empty` on the kinematic carrier is **signature-robust**, and the
> **only** exit to a positive physical subspace is the BRST/quotient route,
> register-tracked as `M-H17`. So the object `U11` must supply is sharply typed:
> **a BV/BRST differential whose ghost-number-zero cohomology is
> positive-definite on the Krein carrier.**"*

By L2, "positive-definite on the Krein carrier" is a two-part object — a
subspace *and* a fundamental symmetry — compressed by the row into the single
word `positive`. The row under-states its own demand.

**G3 — the only named exit is register-tracked as blocked.** `M-H17`
(`lab/process/improvement-register-2026-08-03.md:350`) decomposes the exit into
five steps and carries status `L (blocked)`, with a named blocker (*"`C2 =
155.36` does not close without the unbuilt `Y¹⁴` connection-curvature 2-form"*),
plus a horn dependency recorded 2026-08-08 (the free bicomplex is built on
`Cl(9,5)` under an explicit ban on importing that machinery into `Cl(7,7)`). So
the construction the row's kind presupposes is not merely unperformed; its only
route is blocked and its existing partial work is comparator-scoped.

**G4 — the author declines to supply a mechanism.** `SC-META-53`, `polarity:
UNCERTAIN`, verbatim *"How do you deal with unbounded spectra? Well, I don't
know."* Twin at `:155`. Corroborated by the absence certificate on the *source*
side, independently established: `Krein` = 0, `ghost` = 0, `indefiniteness` = 0,
`negative norm` = 0 across the verbatim primary corpus. The vocabulary of a
solution is entirely absent from the source.

**The named condition this re-typing carries.** G1–G4 establish that the demand
is imported, under-specified, blocked and unsupported by the source. They do
**not** establish that the physical-space pairing descends from the fibre trace
form — and without that, `SC-META-53`'s Killing-form problem and `LT-SM8`'s
state-space problem are two problems, not one. That link is supplied by
`cb-b-lagrangian-terms`'s *"signature-robust"* finding and by BD-D's computation
that a definite descended form requires a definite fibre form. **BD-D is
classified `BRIDGE_OR_SEMANTIC_BOUNDARY` because it imports a Yang–Mills
constraint symbol GU does not own.** The link is therefore repository-established
at boundary scope, not source-established.

So the re-typing **advances carrying its condition, or not at all**:

> **Condition `INHERITANCE_BRIDGE`** — the pairing on the BV/BRST physical
> quotient descends from the fibre trace form, so that its definiteness is
> controlled by the fibre signature. Established for `Λ¹ ⊗ ad P` on `X⁴` at free
> level by BD-D, at `BRIDGE_OR_SEMANTIC_BOUNDARY` scope. **Not** established for
> the RS / `ker Γ` carrier that `M-H17` actually tracks, and **not** at the
> interacting level.

**Proposed kind, and why a new one is required rather than an existing one.**

| candidate | why it does not fit |
|---|---|
| `MISSING_CONSTRUCTION` | grants availability; G3 and G4 remove the grant |
| `EXTERNAL_DATUM` | nothing external supplies a number here; there is no datum, there is a structure |
| `PROVEN_UNSUPPLYABLE` | over-claims. BD-D proves no *equivariant* reduction cures an indefinite fibre form; the Krein keep-and-grade route is not equivariance-based and is not refuted |
| `PROVEN_UNABLE_BY_CURRENT_ACTION` | over-claims at boundary scope. Promoting a `BRIDGE_OR_SEMANTIC_BOUNDARY` no-go into a ledger-level proof would make the ledger look *more decided* than the evidence — the same error as laundering, in the opposite direction |

None fits. Under `unknown_kind_rule: NEW_KIND_REQUIRED__FORCED_FIT_FORBIDDEN`,
a new kind is **required**:

> **`SOURCE_DECLARED_OPEN__NO_MECHANISM_SUPPLIED`** (family: `NEEDS`)
> The row's head demand is an object the source names as an open problem and
> explicitly declines to supply a mechanism for — register-tracked, with
> `polarity: UNCERTAIN` or an `ASSERTS` carrying a `to-be-figured-out` clause —
> **and** the repository's only named route is register-tracked as blocked.
> **This kind is strictly more indebting than `MISSING_CONSTRUCTION`, not less.**
> `MISSING_CONSTRUCTION` says *unbuilt*. This says *unbuilt, and no route is
> known to the repository or to the theory's author.* A row carrying this kind
> remains fully counted, remains in `NEEDS`, remains in the work queue, and is
> **not** discharged, softened, deferred or excused. Every instance MUST carry a
> `debt_note` restating that.

**Direction: worse.** `LT-SM8` goes from a row the program owes a build on, to a
row the program owes a build on with no known route and no help from the source.

### 4.2 `RA-D4` — COMPOUND TRIGGER. No status move; a conjunct split.

`revival_trigger` is one string with two conjuncts of different type:

> *"a **positive BRST cohomology** with **chiral light spectrum**"*

- conjunct (i) `a positive BRST cohomology` → bucket **(a)**, `SC-META-53`
- conjunct (ii) `chiral light spectrum` (row summary: *no light mirror
  partners*) → bucket **(b)**, `:158`'s explicit `if`, with `:119`'s
  two-plus-one/imposter reading as context

**Verdict: `verdict` and `reason_kind` both stand.** `MISSING_CONSTRUCTION` is
the right type for conjunct (ii) — the source supplies a mechanism with a
condition, and constructing that condition is genuinely repository work. It is
the wrong type for conjunct (i). **A single `reason_kind` on a two-conjunct
trigger cannot be right for both, and the honest delta is to split the conjuncts
and type them separately, not to flip the row's kind.**

**Direction: worse.** Before the split, the trigger reads as one buildable
thing. After it, it reads as one buildable thing gated behind one nobody-knows-
how thing, joined by `with` — i.e. conjunction, so the trigger fires only if
both hold.

`RA-D4` is the sole member of `P ∩ H`, so BD-D's `n_κ = 0` pricing attaches to
conjunct (i) specifically and to nothing else in the row.

### 4.3 `RA-G2` — DEFECTIVE TRIGGER. No status move; a reachability flag.

`verdict: DIFFERS`, `reason_kind: PREDICTION`, `revival_trigger:` *"a positive
physical cohomology without mirror states."*

For a `DIFFERS` row the `revival_trigger` is not a debt — it is the condition
under which the difference would be re-examined. So `PREDICTION` is not
mis-typed and **no kind change is proposed.** The defect is elsewhere: the
trigger's conjunct (i) is bucket (a), which makes **the revival condition
unreachable by any known route.** A prediction whose stated revival condition
cannot be reached is a prediction that cannot be retired or confirmed through
the channel the ledger names for it.

**Proposed: the same conjunct split, plus a `revival_reachability` flag.
Direction: worse** — the row's status is unchanged but its testability through
the named route is now recorded as blocked rather than assumed.

### 4.4 `AC-F1` — EXAMINED, DECLINED.

The positivity token is in `distance`, as construction step 3 of four:
*"Construct a native action-stationary background, proper functional BV/BFV, a
positive observed domain and physical cohomology before interpreting
luminous/dark chiral-looking decoupling."* The `revival_trigger` — the row's
head deliverable — is *"a physical chiral carrier with a derived index"*, which
contains **no** positivity token.

So `AC-F1`'s head demand is bucket (b): a chiral carrier, for which `:158`
supplies a conditional mechanism. Positivity is a step on the path, not the
deliverable. **`MISSING_CONSTRUCTION` is correct and stays.** The only honest
delta is to annotate step 3 with its bucket, and I propose that as an annotation
with no type consequence.

**I record this decline deliberately.** `AC-F1` was in my candidate set from the
first sweep and re-typing it would have doubled the headline count. The rule
that stopped it is the same rule that let `LT-SM8` through: type the **head
demand**, not any word that appears anywhere in the path.

### 4.5 `LT-GR2c` — EXAMINED, DECLINED. Homonym.

`revival_trigger`: *"an action-owned normalized global functional with
covariance, **positivity**, domain and observation descent that preserves the
inhomogeneous curvature response."*

Here `positivity` qualifies a **normalized global functional** — a
measure/normalization property of an action functional — not the definiteness of
an inner product on a physical state space. Different object, different
mathematics, no inheritance from any fibre form. The `KREIN` token in
`construction_scope` is a *completed* Green's-function domain, not a demand.

**No re-typing. This is where a mechanical sweep and an evidence-forced pass
diverge**, and it is the reason the matching rule in §1 is followed by
adjudication rather than being applied as a verdict.

**One structural delta is proposed instead**, and it is not a re-typing:
`cb-b-lagrangian-terms-2026-08-05.md:182-189` already runs a homonym quarantine
table for `theta` (four senses), `torsion` (two), `Einstein contraction`
(three), `Z_U`, `the Higgs` and `square`. This artifact has now exhibited
**four** distinct senses of `positive`/`positivity` in evidence:

1. definiteness of a state-space form (`LT-SM8`, `RA-D4`, `RA-G2`);
2. positivity of a normalized global functional (`LT-GR2c`);
3. the sign of a cosmological term (`LT-GR2.summary`);
4. positive-chirality half-spin bundles (`:107`, *"positive spinners"*).

Four senses, no quarantine row. Proposed as `D5`: add `positivity` to that
table. No result transfers between the four.

---

## 5. THE VERSIONLESS DELTA

**Base:** `lab/process/conditional-physics-ledger-v0.258.json`, sha256
`540b50e386073c0f43da4e8d5a8ffdaf06fd243c6612622d7daf187c0a725047`, 84 row
records, 82 canonical targets.
**This channel does not edit the ledger.** What follows is a proposal for the
canonical owner. The probe reads the JSON block below out of *this file* so the
record and the certificate cannot drift.

<!-- ITC-DELTA-BEGIN -->
```json
{
  "delta_id": "IT-C-2026-08-15",
  "ledger_base": "lab/process/conditional-physics-ledger-v0.258.json",
  "ledger_base_sha256": "540b50e386073c0f43da4e8d5a8ffdaf06fd243c6612622d7daf187c0a725047",
  "edit_applied": false,
  "rows_advanced": 0,
  "rows_moving_status": 1,
  "denominator_move": "none",
  "taxonomy_extension": [
    {
      "family": "NEEDS",
      "new_kind": "SOURCE_DECLARED_OPEN__NO_MECHANISM_SUPPLIED",
      "licence": "taxonomy.extensible == true; taxonomy.unknown_kind_rule == NEW_KIND_REQUIRED__FORCED_FIT_FORBIDDEN",
      "definition": "The row's head demand is an object the source names as an open problem and explicitly declines to supply a mechanism for (register-tracked, polarity UNCERTAIN or an ASSERTS carrying a to-be-figured-out clause), AND the repository's only named construction route is register-tracked as blocked.",
      "strictly_more_indebting_than": "MISSING_CONSTRUCTION",
      "non_discharge_rule": "A row carrying this kind stays in NEEDS, stays counted in the denominator, stays in next_work_queue, and is NOT discharged, softened, deferred or excused. Every instance MUST carry a debt_note.",
      "rejected_alternatives": {
        "MISSING_CONSTRUCTION": "grants that the construction is available; M-H17 blocked-status and SC-META-53 remove the grant",
        "EXTERNAL_DATUM": "no external party supplies a datum; the missing object is a structure, not a number",
        "PROVEN_UNSUPPLYABLE": "over-claims; BD-D refutes only equivariant reductions, and the Krein keep-and-grade route is not equivariance-based",
        "PROVEN_UNABLE_BY_CURRENT_ACTION": "over-claims at BRIDGE_OR_SEMANTIC_BOUNDARY scope; would make the ledger look more decided than the evidence"
      }
    }
  ],
  "row_deltas": [
    {
      "delta": "D1",
      "id": "LT-SM8",
      "kind_of_delta": "RETYPE_REASON_KIND",
      "verdict_before": "NEEDS",
      "verdict_after": "NEEDS",
      "reason_kind_before": "MISSING_CONSTRUCTION",
      "reason_kind_after": "SOURCE_DECLARED_OPEN__NO_MECHANISM_SUPPLIED",
      "direction": "WORSE",
      "grounds": [
        "G1 provenance: CB-B:SM-8 is typed [N|S]; the positivity criterion is the imported [S] side ('Physics writes: -(1/2 xi)(partial . A)^2 + c-bar partial^mu D_mu c'). cb-b-lagrangian-terms-2026-08-05.md:191-193, 1073-1074",
          "G2 under-specification: the repository's own statement of the required object is 'a BV/BRST differential whose ghost-number-zero cohomology is positive-definite on the Krein carrier'. On a Krein carrier definiteness is relative to a fundamental symmetry J, so the demand is a subspace AND a J, compressed by the row into the single word 'positive'. cb-b-lagrangian-terms-2026-08-05.md:1095-1103",
        "G3 blocked route: M-H17 is the only named exit, decomposed into five steps, status 'L (blocked)', named blocker C2 = 155.36 requiring the unbuilt Y^14 connection-curvature 2-form, plus a horn dependency on Cl(9,5) under an explicit ban. improvement-register-2026-08-03.md:350",
        "G4 source declines: SC-META-53, polarity UNCERTAIN, 'How do you deal with unbounded spectra? Well, I don't know'; twin at Transcript into the impossible.md:155 [00:45:00]. Corroborated by an absence certificate on the verbatim primary corpus: Krein 0, ghost 0, indefiniteness 0, negative norm 0"
      ],
      "named_condition": {
        "name": "INHERITANCE_BRIDGE",
        "statement": "The pairing on the BV/BRST physical quotient descends from the fibre trace form, so its definiteness is controlled by the fibre signature.",
        "established_for": "Lambda^1 (x) ad P on X^4, free level, by BD-D",
        "scope": "BRIDGE_OR_SEMANTIC_BOUNDARY -- BD-D imports a Yang-Mills constraint symbol GU does not own",
        "not_established_for": "the RS / ker Gamma carrier M-H17 actually tracks; the interacting level",
        "rule": "This re-typing advances carrying this condition or it does not advance. If INHERITANCE_BRIDGE fails, SC-META-53's problem and LT-SM8's demand are two problems and D1 is withdrawn."
      },
      "debt_note": "NOT DISCHARGED. LT-SM8 remains a NEEDS row, remains in the 82-target denominator, and remains at next_work_queue rank 3. What changes is the claim about availability, not the claim about debt."
    },
    {
      "delta": "D2",
      "id": "RA-D4",
      "kind_of_delta": "SPLIT_TRIGGER_CONJUNCTS",
      "verdict_before": "NEEDS",
      "verdict_after": "NEEDS",
      "reason_kind_before": "MISSING_CONSTRUCTION",
      "reason_kind_after": "MISSING_CONSTRUCTION",
      "direction": "WORSE",
      "revival_trigger_before": "a positive BRST cohomology with chiral light spectrum",
      "trigger_conjuncts_after": [
        {
          "conjunct": "a positive BRST cohomology",
          "bucket": "SOURCE_DECLARED_OPEN",
          "register": "SC-META-53",
          "note": "sole member of P inter H; BD-D prices this conjunct at n_kappa = 0 at a named Cartan involution, under condition INHERITANCE_BRIDGE"
        },
        {
          "conjunct": "chiral light spectrum, i.e. no light mirror partners",
          "bucket": "SOURCE_STATED_CONDITION",
          "register": "SC-GEN-54 notes; Transcript into the impossible.md:158",
          "note": "the source's own 'if you have a decreased VEV in the total space taking a Dirac equation into two [Weyl] equations'; context at :119 (three families, really two plus one; third an imposter)"
        }
      ],
      "conjunction": "AND -- the trigger's word is 'with', so it fires only if both conjuncts hold",
      "grounds": [
        "A single reason_kind cannot be simultaneously correct for a conjunct whose mechanism the source supplies conditionally and a conjunct whose mechanism the source declines to supply.",
        "MISSING_CONSTRUCTION is retained because it is correct for conjunct 2, which is genuine repository work."
      ],
      "debt_note": "NOT DISCHARGED. No verdict, kind, priority or queue position changes. The row now reads as one buildable thing gated behind one nobody-knows-how thing."
    },
    {
      "delta": "D3",
      "id": "RA-G2",
      "kind_of_delta": "FLAG_TRIGGER_REACHABILITY",
      "verdict_before": "DIFFERS",
      "verdict_after": "DIFFERS",
      "reason_kind_before": "PREDICTION",
      "reason_kind_after": "PREDICTION",
      "direction": "WORSE",
      "revival_trigger_before": "a positive physical cohomology without mirror states",
      "trigger_conjuncts_after": [
        {
          "conjunct": "a positive physical cohomology",
          "bucket": "SOURCE_DECLARED_OPEN",
          "register": "SC-META-53"
        },
        {
          "conjunct": "without mirror states",
          "bucket": "SOURCE_STATED_CONDITION",
          "register": "Transcript into the impossible.md:158, :119"
        }
      ],
      "revival_reachability": "BLOCKED_BY_SOURCE_DECLARED_OPEN",
      "grounds": [
        "For a DIFFERS row the revival_trigger is a re-examination condition, not a debt, so PREDICTION is not mis-typed and is retained.",
        "The defect is that conjunct 1 makes the stated revival condition unreachable by any known route, so the prediction cannot be retired or confirmed through the channel the ledger names for it."
      ],
      "debt_note": "NOT DISCHARGED and NOT STRENGTHENED. The prediction stands exactly as before; only its testability through the named route is now recorded rather than assumed."
    },
    {
      "delta": "D4",
      "id": "AC-F1",
      "kind_of_delta": "ANNOTATE_ONLY__RETYPE_DECLINED",
      "verdict_before": "NEEDS",
      "verdict_after": "NEEDS",
      "reason_kind_before": "MISSING_CONSTRUCTION",
      "reason_kind_after": "MISSING_CONSTRUCTION",
      "direction": "NONE",
      "grounds": [
        "The positivity token sits in distance as construction step 3 of four, not in the head deliverable.",
        "revival_trigger is 'a physical chiral carrier with a derived index' and contains no positivity token; the head demand is bucket (b).",
        "Re-typing here would have doubled the headline count on a word that is not the deliverable. Declined."
      ],
      "annotation": "distance step 3, 'a positive observed domain', is bucket SOURCE_DECLARED_OPEN and inherits condition INHERITANCE_BRIDGE; the remaining steps and the trigger are unaffected."
    },
    {
      "delta": "D5",
      "id": "LT-GR2c",
      "kind_of_delta": "NO_CHANGE__HOMONYM",
      "verdict_before": "NEEDS",
      "verdict_after": "NEEDS",
      "reason_kind_before": "MISSING_CONSTRUCTION",
      "reason_kind_after": "MISSING_CONSTRUCTION",
      "direction": "NONE",
      "grounds": [
        "'positivity' here qualifies a normalized global functional -- a measure/normalization property -- not the definiteness of a state-space inner product. Different object; no inheritance from any fibre form.",
        "The KREIN token is in construction_scope (a completed Green's-function domain), not in a demand field."
      ],
      "structural_recommendation": "cb-b-lagrangian-terms-2026-08-05.md:182-189 already quarantines the homonyms theta, torsion, Einstein contraction, Z_U, the Higgs and square. Add 'positive/positivity', which this artifact exhibits in FOUR distinct senses: (1) definiteness of a state-space form; (2) positivity of a normalized global functional; (3) the sign of a cosmological term (LT-GR2.summary); (4) positive-chirality half-spin bundles (Transcript into the impossible.md:107, 'positive spinners'). No result transfers between them."
    },
    {
      "delta": "D6",
      "id": "LT-GR5",
      "kind_of_delta": "NO_CHANGE__CORRECT_AS_WRITTEN",
      "verdict_before": "DIFFERS",
      "verdict_after": "DIFFERS",
      "reason_kind_before": "STRUCTURAL_DIFFERENCE",
      "reason_kind_after": "STRUCTURAL_DIFFERENCE",
      "direction": "NONE",
      "grounds": [
        "The indefiniteness tokens are in mapping_grade only (LOCAL_K_LOC_NONDEGENERATE_INDEFINITE, FULL_SUPPORT_INERTIA_4_6) and are findings, not demands.",
        "Its revival_trigger demands a common Green/BV/Fock domain -- a domain, not a sign. The row observes indefiniteness and does not demand it be cured. This is the correct handling and is recorded as a positive control on the matching rule."
      ]
    }
  ],
  "flagged_absences_not_proposed": [
    {
      "flag": "D7",
      "finding": "Zero ledger rows carry the source's own signature data. Across all 84 rows the token 'signature' occurs 0 times, and the strings '6,4', '7,3', 'Spin(6', 'Spin(3', 'trace revers' and 'Frobenius' each occur 0 times, while the source supplies signature data twice: Transcript into the impossible.md:149 ('trace reverse the Frobenius metric along the fibers, which gets you from a seven three signature to a six four') and SC-SIG-52 ('the trace portion of the space of metrics is put in with the proper sign').",
      "type": "MISSING ROW, not a mis-typed row",
      "action": "flagged for the canonical owner; nothing proposed, writing a row is outside this channel's mandate"
    },
    {
      "flag": "D8",
      "finding": "Zero rows of v0.258 demand a Krein structure, ghost clearance, or unitarity of an indefinite form in a demand field. Across all 84 rows and all nine string fields: ghost 0, ghosts 0, definite 0, definiteness 0, indefiniteness 0, unitarity 0, signature 0, coercive 0, semidefinite 0. Krein occurs once (LT-GR2c.construction_scope) and indefinite once (LT-GR5.mapping_grade), both in non-demand fields. Outside rows[] the same ledger file uses 'ghost' 40 times and 'Krein' 6.",
      "type": "STRUCTURAL OBSERVATION",
      "action": "the repository's ghost/Krein work is recorded as history and scope and has never been written into a row demand; flagged, nothing proposed"
    }
  ],
  "counts": {
    "class_P_size": 5,
    "class_P_prime_size": 7,
    "class_H_size": 10,
    "P_intersect_H": 1,
    "rows_moving_status": 1,
    "rows_with_non_status_delta": 2,
    "rows_examined_and_declined": 3,
    "rows_advanced": 0,
    "bucket_a_wholly": 1,
    "bucket_a_b_mixed": 3,
    "bucket_c": 0
  }
}
```
<!-- ITC-DELTA-END -->

---

## 6. HOSTILE REVIEW, INLINE

**H1 — "Is `D1` just a way of making a blocked row look less bad?"**

This is the question the brief demands and it deserves the strongest version of
the attack. Here it is. `LT-SM8` currently reads *"we owe a construction."* After
`D1` it reads *"the theory's author says nobody knows how to do this."* A reader
tallying repository debt sees one fewer construction owed. That is a real
presentational gain and I will not pretend otherwise.

Three things make it not laundering, and one residual that does.

*Not laundering, 1.* The kind stays inside `NEEDS`. Verdict counts are unchanged
at `SAME 32 · DIFFERS 19 · NEEDS 26 · OVER_DETERMINED 5`. Denominator unchanged
at 82/86/84. `LT-SM8` stays at `next_work_queue` rank 3. Nothing advances.

*Not laundering, 2.* The new kind's definition is written so it cannot be read
as relief: it requires *both* an author declination *and* a blocked repository
route, and it carries a mandatory `debt_note`. `MISSING_CONSTRUCTION` says
*unbuilt*. This says *unbuilt with no known route from anyone*. On any ordering
of epistemic states, the second is worse.

*Not laundering, 3.* The re-typing is conditional on `INHERITANCE_BRIDGE` and
the condition is named in the delta record itself, with its scope
(`BRIDGE_OR_SEMANTIC_BOUNDARY`) and its two explicit non-coverages. A laundering
move does not attach its own withdrawal condition.

*The residual, and it is real.* `MISSING_CONSTRUCTION` has an operational
meaning inside this repository that the new kind does not inherit: it is the
kind that *invites work*. A row typed "nobody knows how" is a row that stops
attracting attempts. If `D1` is adopted and `LT-SM8` quietly falls out of the
attempted-work rotation, the delta will have achieved by attrition what it
declined to achieve by typing. **I cannot rule that out from inside this
channel, and the canonical owner should treat queue-position preservation as a
binding part of `D1`, not a courtesy.**

**H2 — "You re-typed one row out of five. Is the small number a way of looking
rigorous while conceding nothing?"**

The inverse is the actual risk here: five is small because the *class* is small,
and the class is small because the ledger barely uses the vocabulary at all. The
finding that makes the program look worst in this artifact is not `D1`. It is
`D8` — that a ledger with 84 rows and 244 migrations contains **zero** row
demands mentioning ghosts, Krein structure, unitarity or signature, while using
`ghost` 40 times in its own history. The row layer is not tracking the structure
the rest of the repository has been building. That is a coverage finding and it
is worse than any single re-typing.

**H3 — "You declined `AC-F1` and `LT-GR2c`. Convenient — declining keeps the
headline modest and therefore credible."**

Test the decline against its own evidence. `AC-F1`'s `revival_trigger` is *"a
physical chiral carrier with a derived index"* — verify: it contains no
positivity token. `LT-GR2c`'s `positivity` modifies *"normalized global
functional"* — verify: read the string. Both declines are checkable against the
ledger text in one grep each, and both were candidates in my first sweep that
the head-demand rule removed. The same rule admitted `LT-SM8`. A rule that
admits and excludes by the same criterion is not being tuned to a headline.

**H4 — "You used BD-D's no-go, which is boundary-classified, to remove a grant.
Isn't that importing a comparator result into a source-native typing?"**

Partly, and it is fenced. `D1`'s grounds are ordered `G1 → G4` by *independence
from BD-D*: `G1` is provenance-code reading, `G2` is a quotation from the
comparison basis, `G3` is register status, `G4` is source philology. **None of
G1–G4 requires BD-D.** BD-D enters only as the establishment of
`INHERITANCE_BRIDGE`, which is why that is a named condition with a withdrawal
rule rather than a premise. If `INHERITANCE_BRIDGE` fails, `D1` is withdrawn and
`G1`–`G4` still stand as an argument that the row is under-specified — which
would leave a *different* delta to write, not this one.

**H5 — "`D2` and `D3` add fields. Isn't 'add a field' a way to look busy without
moving anything?"**

They move nothing and I say so in both records: `direction: WORSE` with
`verdict_after == verdict_before` and `reason_kind_after == reason_kind_before`.
The claim is precisely that a compound trigger cannot honestly carry one type,
and the minimal honest repair is to expose the conjuncts. If the canonical owner
judges that the ledger's schema should not grow a `trigger_conjuncts` field,
the fallback is to leave both rows exactly as they are and record the finding in
prose — which loses nothing except the ability to query it.

**H6 — the one that matters most. "Does this artifact make GU look better?"**

Answered in §7 in its own words, not folded into a list.

---

## 7. THE THING THIS MUST NOT BE READ AS

A theory whose author declares its central consistency question unsolved is not
thereby consistent. Nothing in this artifact is evidence for GU.

The temptation `IT-C` creates is precise and I want it named before anyone else
names it. Having established that `LT-SM8`'s positivity demand is an imported
criterion the source disavows, that the source declares the underlying
indefiniteness problem open, and that `MISSING_CONSTRUCTION` therefore
over-grants — the available bad inference is: *so the row was never really GU's
problem, and the ledger was being unfair.* That inference is wrong twice over.

**Wrong once, on the physics.** Positivity of the physical state space is not a
convention the standard model happens to prefer. It is what makes probabilities
probabilities. Covariant gauge theories are allowed to be indefinite on the
kinematic carrier precisely because Gupta–Bleuler and BRST recover a positive
space at the end; a theory that does not recover one at the end does not
predict. `cb-b-lagrangian-terms:714-716` already records this correctly —
`F = empty` being signature-robust is *"normal for covariant indefinite
theories"* **and** *"its only exit is the BRST/quotient route."* The exit is
mandatory. `M-H17` records it as blocked. Re-typing the row does not unblock it.

**Wrong twice, on the standing.** The author declining to supply a mechanism is
not neutral information about the theory. Read `SC-META-53` and `:155` together
with `CB-B:SM-8`: the only known exit to a positive physical subspace is
blocked, and the author's position on the structure that exit must navigate is
*"I don't know what to do"* and *"we're shielded experimentally."* Being shielded
from a problem is not solving it. The honest reading of `D1` is that `LT-SM8`
moves from *a debt with an assumed route* to *a debt with no route anyone has
named* — and `LT-SM8`'s summary is *"BV/BRST quotient yields a positive physical
space,"* which is the row on which a quantum theory's ability to predict rests.

The Krein keep-and-grade posture is a **repository proposal** for that open
problem. `Krein` occurs zero times in the verbatim primary corpus. `canon/`
grades its dynamical half open and blocked, and this artifact attributes it to
no one but the repository. The correct summary of the day's work is not *"the
positivity demand was unfair"* but *"the positivity demand is real, imported,
under-specified in the ledger, blocked in the repository, and unaddressed by the
source."* Four bad facts, and the delta records all four.

---

## 8. POSTFLIGHT — six lenses

**P1 — taxonomy design, after the fact.** The delta adds exactly one kind and
rejects four existing ones with stated reasons, which is the shape
`NEW_KIND_REQUIRED__FORCED_FIT_FORBIDDEN` asks for. **Residual risk:** the
`NEEDS` family now has nine kinds, and the boundary between
`SOURCE_DECLARED_OPEN__NO_MECHANISM_SUPPLIED` and
`PROVEN_UNABLE_BY_CURRENT_ACTION` is a judgement about proof scope rather than a
mechanical test. If a second row ever qualifies, that boundary will need a
written rule. One instance does not justify writing it now.

**P2 — indefinite-inner-product spaces.** The strongest thing established here
is `G2`, and it is under-sold above: `positive` on a Krein carrier is not merely
imprecise, it is *type-incorrect* absent a fundamental symmetry. A ledger
demanding "a positive pairing" on an indefinite carrier is demanding an object
whose specification is incomplete, which is why no amount of construction work
could ever discharge it as written. **This is the finding I would promote if the
canonical owner adopts only one thing from this file.**

**P3 — ledger epistemics.** The delta preserves every count that would show a
gain: verdict counts, denominator, queue position. It changes exactly one string
and adds fields to two rows. **Weakness:** I have no mechanism to enforce queue
preservation, and H1's attrition risk is unmitigated by anything in the delta
itself.

**P4 — source philology.** Every quote used was re-read from copy A1 at a named
line before use, and the edited derivative was avoided. **Residual:** the
`toe-weinstein-gu-40-years.md` transcript carries `provenance_grade:
untrusted-external` (podscripts auto-extraction), and `SC-META-53`'s primary
verbatim is drawn from it. `SC-META-53`'s twin at A1 `:155` is the
trustworthy anchor and says the same thing in different words, so the ground
survives — but if only the ToE transcript existed, `G4` would be weaker than it
reads.

**P5 — gauge-theory consistency.** The ledger locates positivity at `H⁰(Q)`,
which is where it belongs; nothing in this artifact disturbs that. What this
artifact does not do — and cannot, from a typing channel — is check whether the
BRST charge whose cohomology is demanded exists at the interacting level.
`M-H17` step (i) records that it does not: only the *free* bicomplex is built.
So `LT-SM8`'s demand is not just unspecified, it is unspecified about an
operator that has not been constructed. That is a third bad fact and it is worse
than the two `D1` records.

**P6 — adversarial reading, self-applied.** The sentence in this file most
likely to be quoted out of context is §4.1's *"the criterion is imported, not
native."* Read alone it sounds like *GU is not obliged to be unitary.* Read in
place it means *the ledger sourced this demand from the comparison basis, so
`MISSING_CONSTRUCTION`'s grant was never a GU commitment.* §7 exists to make the
second reading the only available one, and if a downstream artifact quotes §4.1
without §7 the frame will have regressed at exactly the boundary this repository
already knows it regresses at.

---

## 9. THE ANSWER, IN ORDER

1. **The matching rule** is §1's Rule P: a positivity-lexicon token, tokenised
   on `[A-Za-z]+`, in one of the three demand fields `reason_kind`, `distance`,
   `revival_trigger`.
2. **The class is FIVE rows**: `RA-D4`, `RA-G2`, `LT-GR2c`, `LT-SM8`, `AC-F1`.
   Extended to all fields it is seven; the two additions are excluded with
   grounds. **It is not BD-D's ten.** The two classes share one member.
3. **Every hit is the single word `positive`/`positivity`.** `ghost`,
   `definite`, `unitarity`, `signature`, `coercive`, `semidefinite` and
   `indefiniteness` occur **zero** times in all 84 rows. `Krein` occurs once, in
   a non-demand field.
4. **Rows moving status: 1.** `LT-SM8`, `MISSING_CONSTRUCTION` →
   `SOURCE_DECLARED_OPEN__NO_MECHANISM_SUPPLIED`, conditional on
   `INHERITANCE_BRIDGE`.
5. **Direction: worse.** The re-typing removes an availability grant and adds
   none.
6. **Rows advanced: 0. Denominator move: none. Verdict counts: unchanged.**
7. **Bucket split:** (a) wholly 1 · mixed (a)+(b) 3 · homonym 1 · (c) **0**.
8. **Two flagged absences**, `D7` (no row carries the source's signature data)
   and `D8` (no row demands a Krein/ghost/unitarity object), both structural,
   neither proposed as an edit.
