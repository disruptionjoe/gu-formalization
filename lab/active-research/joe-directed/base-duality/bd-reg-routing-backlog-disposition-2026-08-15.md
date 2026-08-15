---
doc_type: stewardship_record
title: "BD-REG: comparator-routing backlog disposition"
created: 2026-08-15
status: complete
scope: lab/process/source-native-comparator-routing-registry.json
method: lab/methods/source-native-comparator-routing.md
audit: process_gates/source_native_comparator_routing_audit.py
result: "8 of 17 transcribed from in-vocabulary self-declarations; 9 left
  unclassified and itemised; UNCLASSIFIED_BASELINE ratcheted 16 -> 9"
---

# BD-REG — the routing backlog, worked without guessing

**Declared doc type.** This file is a `stewardship_record`. It points at
artifacts that contain or border comparators; it contains none itself, and the
audit's own scope narrowing excludes that document type by front matter. It is
therefore not a new gap of its own making.

**What this pass was allowed to do.** Transcribe determinations the artifacts
already made. Not make determinations. The gate's own source states the
constraint: guessing a `CONVENTIONAL_COMPARATOR` / `BRIDGE_OR_SEMANTIC_BOUNDARY`
/ `SOURCE_NATIVE_ROUTE` label "would be exactly the unsourced attribution this
method exists to prevent."

---

## 1. PREFLIGHT — lenses run inline

**Lens 1 — taxonomy and classification design.** The method names three values
and **defines none of them**. Its only operative sentence about them is: "An
artifact may then state whether it is a `CONVENTIONAL_COMPARATOR`, a
`SOURCE_NATIVE_ROUTE`, or a `BRIDGE_OR_SEMANTIC_BOUNDARY`." With no
intensional definitions, no auditor can *derive* a type from content — there is
no rule to apply. The only admissible evidence is an author's extensional act:
the artifact saying which one it is. That single observation determines the
whole pass. Corollary the lens forces: an artifact that declares a value
**outside** the three is not thereby assignable to one of the three; a closed
vocabulary plus an out-of-vocabulary declaration is an unresolved case, not a
nearest-neighbour rounding problem.

**Lens 2 — evidence provenance and attribution.** Three grades of evidence turned
up, and only the first is transcribable: (i) the artifact declares its own type;
(ii) a *different* artifact declares this artifact's type; (iii) the artifact
describes its scope and an auditor infers a type. (ii) and (iii) are both
attributions by someone other than the author, and (iii) is the exact failure the
method's own withdrawn clause documents — a plausible sentence inserted into a
mandatory boundary, then re-imported by every downstream reader. LA-8 supplies a
live (ii): "**Verdict: MD-1 is `SOURCE_NATIVE_ROUTE` on its form-leg result and
carries one declared, fenced `CONVENTIONAL_COMPARATOR` sub-computation.**"
That is LA-8's determination about MD-1, and it does not become MD-1's.

**Lens 3 — technical documentation standards / machine-readable contracts.** The
gate matches the exact substring ``Classification: `X` ``. Nine artifacts already
carried a declaration, but eight of them wrote it as
`Classification: **`X`.**` (markdown emphasis between the colon and the
backtick) and one wrapped it across a line break. **None matched.** So the
backlog is partly a formatting artefact, not an unmade decision: the authors
declared, the string shape defeated the matcher. The correct repair is
normalisation of the author's own string — delete four `*` characters — not new
prose in the author's voice. Every artifact edit below is exactly that, verified
by byte delta.

**Lens 4 — adversarial reading / homonym hunting.** "Classification" is a
repository-wide homonym. CC-1 §5 and MC-1 §4.4 both head a section
"**Classification, in target-native vocabulary**", and neither is a routing
classification — they classify *claim status* (`ROUTE KILLED`, `CANDIDATE
KILLED / TYPE-MISSING`, `REFUTED`, `SURVIVES`). An auditor pattern-matching on
the word alone would have "found" declarations in two artifacts that make none.
Second homonym trap: LA-3 contains the line "**Verdict: `CONVENTIONAL_COMPARATOR`.
'The chiral 16 shadow' is the fork-1 comparator**" — a type assigned to a
*ledger grant object*, not to the artifact. Subject discipline is mandatory:
every candidate string must be checked for what it is the classification *of*.

**Lens 5 — audit and compliance / control design.** The baseline is a ratchet,
not a target. Setting it to the true post-pass count converts it from "16 debts
tolerated" to "9 debts, itemised, and no tenth may appear silently". Green here
does not mean clean: the gate prints all nine `UNCLASSIFIED` lines on every run
whether it passes or fails. Compliance risk to avoid: making the count go green
by widening what counts as a determination. That risk is priced by Lens 1 —
only self-declaration counts.

**Lens 6 — library and information science (authority control).** A closed
controlled vocabulary needs a documented procedure for out-of-vocabulary terms:
either extend the authority list or record the item as uncatalogued. It does
**not** permit silent mapping to the nearest existing heading. Four artifacts
have declared `STRUCTURAL_LEDGER_ONLY` or `STRUCTURAL_PLUS_DEFINITIONAL`. Those
are new headings proposed by authors, and the registry's `classifications` array
is asserted equal to exactly three values by `test_classifications_are_typed`.
Uncatalogued is the correct disposition; the method owner extends or narrows.

**Lens 7 — reproducibility and fresh-clone integrity.** A registry row pointing
at an untracked file breaks a fresh clone. All eight registered paths were
confirmed tracked by a read-only `git ls-files` before any row was written. No
mutating git command was run at any point in this pass.

---

## 2. THE CLASSIFICATION PASS

### 2.1 Transcribed — eight artifacts, all `BRIDGE_OR_SEMANTIC_BOUNDARY`

Each already carried the verbatim notice **and** an in-vocabulary declaration.
The edit is normalisation of that declaration to the gate's exact form. Byte
deltas: `+4` for the seven that lost `**` emphasis, `+0` for LA-1 (line rewrap).
No result, number or conclusion was touched in any file.

| artifact | the author's own words |
|---|---|
| `la1-embedding-grant-is-zero-bit…` | "pointers before reusing this result. Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`." Corroborated by its Lens 4 ("comparator-routing auditor: which rows may I touch?") and its row table: "`AC-D1..AC-D5` \| Comparator-routed. Grant is 'a complete chiral `16` shadow in 4D' — the fork-1 object … No typed bridge exists." |
| `la2-aca1-needs-no-kernel-selection…` | "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`. The form-degree slots `Omega^p(Y^14, /S)` are program-native (draft Sec 9.3); the *chirality grading* that turns them into a signed-multiplicity vector `x in Z^15` is an import. **The whole computation therefore sits on the boundary, not inside the source-native route.**" |
| `la3-chiral-16-shadow-is-a-comparator…` | Artifact-level "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`."; body delivers "(a) a routing verdict … and (c) a typed-bridge specification whose finding is stronger than 'unbuilt'." The `CONVENTIONAL_COMPARATOR` verdict inside is about the *chiral 16 shadow*, a ledger grant object. |
| `la4-representation-axis-has-13-grants…` | "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`."; Lens P3: rows "**border fork-2 and fork-4 comparators**. This artifact touches only their position in the incidence graph. Their comparator status is untouched."; Lens Q5: "No comparator result is used to adjudicate a source-native row." |
| `la5-anomaly-axis-is-seven-handles…` | Declared twice. §3.5: "Two comparator objects were computed here … **Neither is transported.** … `L` is used only to bound `rank(phi)` — a **bridge-burden specification**, which the routing method explicitly licenses and in fact requires. … **Classification stands: `BRIDGE_OR_SEMANTIC_BOUNDARY`.**" |
| `la8-rae2-is-refuted-at-the-settled-form-leg…` | "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`." plus explicit per-section routing: "**§3.1 (the contraction) is `SOURCE_NATIVE`.** **§3.2–§3.4 … are `CONVENTIONAL_COMPARATOR` and bind only the disavowed KK route**". A document with one leg on each side, fenced and labelled, is the boundary case by construction. |
| `la9-eleven-real-defects…` | "**§2.3 of this artifact** recomputes a conventional particle-physics comparator … Any result **there** binds only that named model. … Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`. **Everything outside §2.3 is bookkeeping about the ledger file and carries no physics content at all.**" §2.3 repeats the fence in place: "**Routing.** This subsection computes the conventional 4d SM anomaly comparator. Nothing in it bears on the source-native route." |
| `phi1-the-reduction-is-rank-one…` | "This artifact **contains** a conventional particle-physics comparator: the 4D Standard-Model perturbative gauge-anomaly conditions and the lattice `L = Z·(15 of SU(5)) ⊕ Z·(nu^c)`, which are fork-1 objects. **Any result about them** binds only that named model. … Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`." The artifact's constructed object is `phi`, the map from the 14D system **through the source-native observation pullback** into that comparator lattice — item 2 of the method's own bridge burden. |

### 2.2 Left unclassified — nine artifacts, three distinct reasons

**(a) No notice, no declaration — 4.** These predate or ignore the notice
requirement and state no routing type anywhere. They are the only genuine method
violations in the backlog.

| artifact | why it stays unclassified |
|---|---|
| `cg1-p-is-a-declared-coset-not-a-gauge-sector` | Zero occurrences of the marker or any of the three type tokens. Its `doc_type` is `source-typing-and-structural-scope-gate` and its content is source typing (`GU-YM-Δ1..Δ5`), which *suggests* source-native — but suggestion is inference, and the artifact never says it. |
| `cc1-killing-signature-cannot-sign-lambda` | No marker, no type token. Its §5 "Classification, in target-native vocabulary" is claim status ("ROUTE KILLED", "CANDIDATE KILLED / TYPE-MISSING"), not routing. Substantively it cuts both ways: the algebra `ad = so(6,4)` is source-declared, while its central device — an independently supplied `Ad`-invariant polynomial potential of degree ≤ 4 — is fork-2 comparator shape ("an independently supplied Mexican-hat potential"). Two defensible types, no authorial tiebreak. |
| `md1-form-leg-survives-ad-leg-is-untyped` | No marker, no type token. **A third party typed it**: LA-8 concludes "MD-1 is `SOURCE_NATIVE_ROUTE` on its form-leg result", resting on the claim that the method author listing MD-1 under fork 3's "Read first" is "a routing determination by the method's author … and it is decisive." **That inference does not hold.** The same read-first lists contain `layer0-pass-on-the-two-higgs-objects-2026-07-29.md`, which the registry types `BRIDGE_OR_SEMANTIC_BOUNDARY`. Membership in those lists therefore does not imply `SOURCE_NATIVE_ROUTE`, and MD-1's own title says its ad leg "is untyped". |
| `mc1-the-cone-does-not-bound…` | No marker, no type token. §4.4 "Classification, in target-native vocabulary" is again claim status ("TC-CONE: `REFUTED`", "`ROUTE CLOSED, NEGATIVE`"). Its object — the cone of Lorentzian metrics and the DeWitt metric — matches none of the four named forks cleanly, so even the prior question (does it contain or border a comparator at all?) is unanswered by the artifact. |

**(b) Declared a type outside the closed vocabulary — 4.** These authors did not
fail to decide; they decided on a value the registry cannot hold.

| artifact | declared |
|---|---|
| `la10-the-cut-vertex-survives…` | "Nothing here is evidence for or against Weinstein's source-native mechanism, **and nothing here binds any conventional comparator**. … Classification: **`STRUCTURAL_LEDGER_ONLY`.**" |
| `la11-b9stat-is-a-base-duality-row…` | "The **Lie-algebraic** object (section 2) binds GU's own declared symmetry object … **so it is not a conventional comparator** — but it is a statement about invariant bilinear forms, not a Lagrangian, a spectrum, a count, or evidence for or against Weinstein's source-native mechanism. Classification: **`STRUCTURAL_PLUS_DEFINITIONAL`, `pending_integration`.**" |
| `ot1-the-ownership-predicate…` | "The Lie theory binds GU's own declared symmetry object (`GU-YM-Δ1`, `SC-GRP-05`), so it is not a conventional comparator; but nothing here is a Lagrangian, a spectrum, a count, a selection principle, or evidence for or against Weinstein's source-native mechanism. Classification: **`STRUCTURAL_PLUS_DEFINITIONAL`, `pending_integration`.**" |
| `ot2-lt-sm3b-is-not-an-ownership-row…` | Same declared value, over "(i) a **ledger-typing** result … (ii) an **exact linear-algebra** reproduction … (iii) a **classifier-independence audit** … Nothing here is … evidence for or against Weinstein's source-native mechanism." |

Each of these says, in prose, that it binds no conventional comparator **and**
is not evidence about the source-native mechanism. That is an assertion that
neither of two of the three values applies — and it is not an assertion that the
third does. `BRIDGE_OR_SEMANTIC_BOUNDARY` names an artifact that spans or
borders the two sides; these say they touch neither. Assigning it by elimination
would be inventing the determination the author declined to make. **Owed
decision:** the method owner extends the vocabulary (e.g. a
`NO_COMPARATOR_CONTENT` value) or narrows the derived scope by declared doc
type, as the gate's second horn already allows.

**(c) Self-contradictory — 1.**

`phi2-spin-extended-target-has-rank-five…` requests
`BRIDGE_OR_SEMANTIC_BOUNDARY` while its own scope paragraph describes a
`CONVENTIONAL_COMPARATOR`, verbatim:

> "This artifact is **built entirely inside a conventional particle-physics
> comparator**: the 4D Standard-Model perturbative gauge-anomaly conditions, the
> lattice `L = Z·(15 of SU(5)) ⊕ Z·(nu^c)`, and the ordinary index-density
> prescription for higher-spin anomaly coefficients. … **Every result below binds
> only that named model.** It is **not** evidence for or against Weinstein's
> differently constructed source-native mechanism **without an explicit typed
> bridge**, and the ordinary-index arena is precisely the one the routing
> document warns is not the GU-native one."

"Built entirely inside a comparator", "every result binds only that named
model", and "without an explicit typed bridge" are the definition of the
comparator value and the denial of the bridge value. The label and the paragraph
cannot both stand. **Not resolved here.** The probe layer does not break the tie
either: `joe_directed_phi2_spin_extended_target_lattice.py` and
`joe_directed_phi_reduction_construction.py` carry the identical docstring line
"This probe touches a CONVENTIONAL COMPARATOR object". PHI-2's author decides.

---

## 3. HOSTILE REVIEW — could a careful reader reach a different type?

Standard applied, stated so it can be attacked: **an explicit in-vocabulary
self-declaration governs unless the artifact's own text contradicts it.** A
reader who reaches a different type from an uncontradicted declaration is
disagreeing with the author, which is not the same as the text being ambiguous.
Where the text fights the label, the label loses and the artifact stays
unclassified. Each of the eight, tested:

1. **LA-1** — weakest of the eight *as a notice*: boilerplate plus a bare label,
   no scope prose of its own. Attack: the boilerplate opener "contains **or**
   borders" is a disjunction and appears verbatim above registered
   `CONVENTIONAL_COMPARATOR` artifacts too, so it discriminates nothing.
   Survives: the label is uncontradicted and the body corroborates it — LA-1
   *routes* rows rather than computing inside a comparator ("Comparator-routed
   … No typed bridge exists"), and its disposition string records
   `AC_D_CASCADE_COMPARATOR_ROUTED_NOT_ADVANCED`. **Kept.**
2. **LA-2** — the artifact states the boundary conclusion itself ("sits on the
   boundary, not inside the source-native route"). No live alternative. **Kept.**
3. **LA-3** — real attack: the file contains a bare "**Verdict:
   `CONVENTIONAL_COMPARATOR`**" line and its front-matter `disposition` opens
   `CHIRAL_16_SHADOW_IS_A_FORK1_CONVENTIONAL_COMPARATOR`, so a hurried reader
   could transcribe the wrong value. Survives on **subject**: both strings
   classify the *chiral 16 shadow* grant, an object the artifact adjudicates;
   the artifact-level label is separate and explicit. **Kept** — and the near
   miss is exactly why Lens 4 exists.
4. **LA-4** — label uncontradicted; Lens P3 and Lens Q5 both state the
   non-transport rule the boundary value encodes. **Kept.**
5. **LA-5** — declared twice, the second time with reasoning. Strongest of the
   eight. **Kept.**
6. **LA-8** — attack: it self-routes its own §3.2–§3.4 as
   `CONVENTIONAL_COMPARATOR` and §3.1 as `SOURCE_NATIVE`, so a reader could
   claim the artifact "is" one or the other. That is precisely what
   `BRIDGE_OR_SEMANTIC_BOUNDARY` is for, and LA-8 states the artifact-level
   label first. **Kept.**
7. **LA-9** — closest call kept. Attack, and it is a fair one: LA-9's *only*
   physics content is a conventional comparator recomputation (§2.3); everything
   else "carries no physics content at all". Type the artifact by its physics and
   you get `CONVENTIONAL_COMPARATOR`. Survives because the author performed the
   boundary act explicitly — partitioning the document into a bound region and a
   physics-free region, in the notice and again in place at §2.3 — and because
   no sentence in LA-9 says the artifact as a whole binds only the comparator.
   That last clause is the exact sentence PHI-2 does contain, and it is what
   separates them. **Kept, flagged.**
8. **PHI-1** — second-closest call, and the uncomfortable one. PHI-1 and PHI-2
   do near-identical work on the same rows with the same imported machinery, yet
   one is kept and one is not. Attack: if PHI-2's author, describing that work,
   called it "built entirely inside a comparator", maybe PHI-1's label is wrong
   too. Rejected, because that is cross-artifact inference — the same move
   refused for MD-1 in §2.2(a), and refusing it there while accepting it here
   would be incoherent. On PHI-1's own text the label is uncontradicted: it says
   "**contains** a comparator" and scopes the binding to "any result **about
   them**", and its constructed object is a reduction map from the 14D system
   through the source-native observation pullback into the comparator lattice.
   **Kept** — and if the method owner ever rules PHI-2 a `CONVENTIONAL_COMPARATOR`
   on those grounds, PHI-1 should be re-opened in the same motion.

Nothing was downgraded by this review, because nothing was *upgraded* by the
pass: every kept value is the author's own string, and every case where the
value had to come from anywhere else is in §2.2.

---

## 4. RESULT

| quantity | before | after |
|---|---|---|
| derived scope | 56 | 56 |
| registered | 39 | 47 |
| unclassified | 17 | **9** |
| `UNCLASSIFIED_BASELINE` | 16 | **9** |
| gate | **RED** (17 > 16) | **green** (9 ≤ 9), still printing all nine |

Baseline ratcheted **down only**, 16 → 9, to the true post-pass count. The gate
now fails the moment a tenth unclassified artifact appears — including any new
`bd-d-*` file that lands without a self-declaration.

All five tests pass: coverage, notice-and-exact-classification-line on every one
of the 47 registered paths, typed classifications, mandatory-routing
instructions, and source-native entrypoint resolution.

**The gate being green is not the same as the backlog being empty.** Nine
artifacts remain unclassified and are named on every run. The three owed
decisions are (a) four artifacts must get a notice and a type from their
authors, (b) the closed three-value vocabulary must either grow a
no-comparator-content value or the scope must shrink by declared doc type, and
(c) PHI-2 must reconcile its label with its own scope paragraph.

---

## 5. POSTFLIGHT — lenses run inline

**Lens 1 — strongest overclaim available, and why it is refused.** *"The
comparator-routing backlog is cleared and the gate is green."* Refused. Eight of
seventeen were already decided by their authors and were being defeated by four
asterisks; this pass supplied a matcher-compatible string, not a judgement.
Nine of seventeen are still open and the gate still prints them. The honest
headline is **"the backlog is halved and the remainder is itemised by reason",**
not "cleared". A second, subtler overclaim also refused: this pass did **not**
verify that any of the eight self-declarations is *correct*. It verified that
each was made, was in-vocabulary, and was not contradicted by its own artifact.
Whether LA-9 really is a boundary artifact rather than a comparator one is its
author's call and remains reviewable.

**Lens 2 — adversarial red-team on my own output.** The sharpest attack on this
pass is the PHI-1/PHI-2 split: two artifacts doing near-identical work, one
registered and one not, on a difference of *self-description* rather than
science. I accept that this looks arbitrary from the outside and have named it
in §3 item 8 rather than buried it. The defence is that the alternative — deciding
which of PHI-2's two self-contradictory statements is the real one, then
propagating that decision back onto PHI-1 — is exactly the unsourced
attribution the method forbids, and it would corrupt two artifacts instead of
leaving one open. The second-sharpest attack is that I under-classified four
artifacts (LA-10, LA-11, OT-1, OT-2) whose prose arguably eliminates two of
three values. Accepted as a cost, and it is the cheap direction of the
asymmetry: a red-ish line item costs a reader thirty seconds, a wrong type
silently reframes how every later agent reads that result.

**Lens 3 — regression and blast-radius audit.** Ten files changed, all inside
the authorised write set: eight artifact classification lines, the registry, the
baseline constant. Byte deltas on the eight artifacts are `+4` ×7 (four `*`
characters removed) and `+0` ×1 (one line rewrap) — arithmetically incapable of
altering a result, a number or a conclusion. The registry diff is `32
insertions, 0 deletions`, i.e. purely additive. No `bd-d-*` file, no probe under
`tests/channel-swings/`, no ledger, no `CURRENT-STATE.yaml`, no `canon/` file
was touched. `grep` confirms this gate is the only consumer of the registry;
the five probes that mention `GU-COMPARATOR-ROUTING` do so in docstrings only
and assert nothing about it.

**Lens 4 — concurrency and shared-checkout hygiene.** Another agent is writing
`bd-d-*` artifacts in this same directory and probes in
`tests/channel-swings/`. Two interactions were designed for. First, this report
declares `doc_type: stewardship_record` so it does not itself become gap
number ten — verified, the derived scope is 56 before and after. Second, the
ratchet to 9 means the next unregistered artifact in scope turns the gate red.
That is intended and is the current rule working: artifacts produced under
today's convention self-declare and register at birth, so a red gate here would
signal an artifact that skipped that step, not a false alarm. No mutating git
command was run; the only git invocation in this pass was a read-only
`git ls-files` tracked-status check.

**Lens 5 — method-owner escalation, typed.** Three distinct defects were found
in the method/gate pair and none is fixable from an auditor's seat. (i) The
method defines the three values only by name, so no content-based classification
rule exists — an auditor is structurally limited to transcription. (ii) The
method makes declaration optional ("may then state") while the gate counts every
unregistered artifact as a gap; the gate's own comment already records this, and
four artifacts have now exercised it by declaring types the registry cannot
hold. (iii) The exact-substring contract `` Classification: `X` `` is
undocumented in the method, which is why nine authors who *did* declare wrote
strings the gate could not see. Fixing (iii) is the cheapest and highest-yield:
put the required literal in the method's "Required artifact notice" section.

**Lens 6 — information-hygiene check on this record.** This file classifies
nothing and asserts no physics. Every type in §2 is quoted from the artifact it
belongs to, with the subject of each classification stated explicitly, so a
later reader can re-derive the pass without trusting it. The one determination
this record makes on its own authority is negative and named as such: that
LA-8's typing of MD-1 does not bind MD-1, because the method's read-first lists
provably mix types.
