---
artifact_type: exploration
status: exploration
doc_type: process_gate_design_record
created: 2026-08-16
work_item: FX-2
channel: carrier-decl
title: "FX-2: the carrier declaration is now machine-checkable -- a non-retroactive process gate (`typed_carrier_declaration_audit.py`, cutoff 2026-08-17, baseline 0) enforcing a fenced `gu-typed-objects` block with seven keys (result, carrier with LAYER and CHIRALITY, pairing with ON=, real_structure, grading, action_owner, target with MAP-TYPE), a closed vocabulary that reuses CN-2's four chirality tokens verbatim, a registered-homonym rule seeded with `so(1,3)` and `ad(P_H)`, an audited EXEMPT-PROSE-ONLY hatch on the NONE-NOT-A-KILL pattern, and UNTYPED/AMBIGUOUS always legal, always counted, printed every run. Acceptance test: each of THIS WEEK'S five actual typing failures -- unsubscripted `Omega^1(S)`, the algebra-vs-module inversion, two Lorentz subalgebras wearing one name, contraction retyped as projection, and the dropped word 'observer' -- maps onto exactly one block slot and is caught or surfaced there. Nothing existing goes red; the clean baseline is verified before every selftest mutation."
grade: "EXACT throughout: integer counters only, no float anywhere (the probe sweeps its result surface and asserts none). Probe `tests/channel-swings/joe_directed_fx2_typed_carrier_declaration.py`: 67/67 checks, exit 0 -- 22 validator checks with FULL defect-list equality, 10 file-level audit checks with exact counters (scope 5, triggered 4, exemption 1, untyped slots 7), 17 artifact-conformance checks, 12 exact source substrings read from their owning files, 6 runtime checks. THREE planted-false propositions (a pre-cutoff artifact reds; an ALL-UNTYPED block is a hard red; HOMONYM-AMBIGUOUS is a hard red) each observed False. Probe `--selftest`: clean baseline verified FIRST, then 10/10 machinery mutations each drive exit 1; `--selftest --poison` proves the baseline guard itself has power. Gate `--selftest`: clean fixture baseline verified before any mutation, then 10/10 planted false facts (missing field, mixed-layer-no-bridge, unregistered exemption, and seven more) each exit 1; `--selftest --poison-baseline` exits 1 with the refusal printed. NOT: a science result, a claim movement, a retroactive judgment of any artifact, or an edit to any registry, method file, or existing artifact."
disposition: ENFORCEMENT_BUILT_AS_A_NON_RETROACTIVE_FAIL_CLOSED_PROCESS_GATE__SEVEN_KEY_FENCED_BLOCK_WITH_CLOSED_VOCABULARIES_REUSING_CN2_CHIRALITY_TOKENS_VERBATIM__ALL_FIVE_OF_THIS_WEEKS_TYPING_FAILURES_MAP_ONTO_NAMED_SLOTS_AND_ARE_CAUGHT_OR_SURFACED__UNTYPED_IS_LEGAL_COUNTED_AND_PRINTED_NEVER_SILENTLY_RESOLVED__AUDITED_PROSE_ONLY_HATCH_DISALLOWED_ON_RESULT_DECLARING_DOC_TYPES__ZERO_EXISTING_ARTIFACTS_IN_SCOPE_AT_SHIP_TIME__TWO_REGISTRY_INTEGRATION_WRITES_REQUIRED_AND_PRINTED_NOT_PERFORMED
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
priority_change: none
steering_effect: unchanged
canonical_effect: pending_integration
depends_on:
  - AGENTS.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
  - process_gates/kill_target_claim_audit.py
  - process_gates/source_native_comparator_routing_audit.py
  - lab/methods/source-native-comparator-routing.md
  - lab/process/source-native-comparator-routing-registry.json
  - lab/specifications/six-axis/six-axis-template.md
  - lab/active-research/joe-directed/carrier-notation/cn2-notation-carries-the-answer-2026-08-15.md
  - lab/active-research/joe-directed/carrier/crb-carrier-is-four-corners-not-one-weyl-2026-08-15.md
  - lab/active-research/joe-directed/base-duality/bd-a-the-base-duality-is-the-observation-and-positivity-is-the-obstruction-2026-08-15.md
  - lab/active-research/joe-directed/base-duality/README.md
  - lab/active-research/joe-directed/soldered-ad/sa1-the-selector-is-built-and-the-bundle-horn-is-soldered-2026-08-16.md
  - lab/active-research/joe-directed/four-d-mode-decomposition/md1-form-leg-survives-ad-leg-is-untyped-2026-08-14.md
scripts:
  - tests/channel-swings/joe_directed_fx2_typed_carrier_declaration.py
  - process_gates/typed_carrier_declaration_audit.py
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
>
> Classification: **`INTERNAL_STRUCTURAL_ONLY`.**
>
> Everything below is repository-internal structural work: a process gate, a
> declaration format, and a validation harness. No physics object is computed,
> no comparator is run, and no source claim is tested. The five errors used as
> the acceptance test are QUOTED from their owning artifacts and none is
> re-adjudicated here.
>
> **REQUIRED INTEGRATION WRITES, not performed here.** This artifact was
> produced under a write scope limited to its own three paths, on a checkout
> shared with concurrent agents, so it edits no registry and no README.
> Two one-line writes belong to the canonical integrator:
>
> 1. `lab/process/source-native-comparator-routing-registry.json` needs the
>    entry below, without which
>    `process_gates/source_native_comparator_routing_audit.py` is red
>    (6 unclassified > baseline 5). `UNCLASSIFIED_BASELINE` must NOT be
>    raised; the gate's own comment says it may only ratchet down.
>
>    ```json
>    { "path": "lab/active-research/joe-directed/carrier-decl/fx2-typed-carrier-declaration-2026-08-16.md",
>      "classification": "INTERNAL_STRUCTURAL_ONLY" }
>    ```
>
> 2. `process_gates/README.md` needs one code-span mention of
>    `typed_carrier_declaration_audit.py` (the inventory audit
>    `process_gate_readme_inventory_audit.py` requires every live gate script
>    to be named there and is red until it is added).
>
> **Gate delta, measured rather than asserted — and one instrument defect
> found and corrected while measuring.** The first before/after suite runner
> recorded every gate as exit 0 because a `$(basename ...)` command
> substitution clobbered `$?` before it was read — a vacuous instrument, the
> exact failure class this gate family exists to catch, caught here by the
> same discipline the shipped probes enforce (a recorded exit that cannot go
> nonzero is not a measurement). With the runner fixed, the full suite (410
> gate scripts, one interpreter, 120 s timeout each) has **170 nonzero exits
> on the current shared checkout**. Attribution was then done by evidence,
> not assumption: every one of the 170 was re-run with output captured and
> grepped for this work's three paths. **Exactly four mention them:**
> `source_native_comparator_routing_audit` (the registry line above;
> 6 unclassified > baseline 5, this artifact listed by name);
> `process_gate_readme_inventory_audit` (missing README mentions for BOTH
> gates that appeared today — this work's and the sibling lane's
> `needs_provides_composition_audit.py`); `protected_surface_diff_audit`
> (names exactly this artifact's uncommitted path; by construction red for
> any uncommitted write under `lab/active-research/`, resolves on
> review/commit); and the sibling-owned `needs_provides_composition_audit`
> itself, whose 34-pair adjudication backlog lists this artifact as one of
> 34 candidates (token `FULL-DIRAC`, citing CN-2) — adjudication belongs to
> that lane and is not performed here. The remaining 166 failures reference
> none of these files and are the shared checkout's ambient condition
> (SA-1 had already recorded the suite's remaining reds as pre-existing on
> 2026-08-16). During this session the homonym lane also shipped
> `lab/process/homonym-register.yaml` and its gate (green): the supersession
> path §1 declares for this gate's seeded homonym constant now has a
> concrete target. The new gate itself runs green on the live tree: 0 red,
> 0 files in dated scope, baseline 0, in 0.62 s.

# FX-2 — making the carrier declaration machine-checkable

**The one-paragraph answer.** `AGENTS.md` already commands: *"State the
carrier, pairing or form, real structure, grading, action owner, target
object, assumptions, controls, and claim ceiling for a new result."* The
command had no enforcement, and in one week the repository paid five times:
an unsubscripted `Omega^1(S)` (13 declaration sites, none typed — CN-2), an
algebra-vs-module domain error that inverted an answer one hop from its
canonical owner (BD-A), two Lorentz subalgebras with intersection zero
wearing one name (SA-1), a contraction retyped as a projection inside a
mandatory method boundary (the withdrawn clause), and the word "observer" —
the action owner — dropped in a relay (base-duality README). FX-2 ships the
enforcement as a process gate in this repository's own gate idiom:
non-retroactive (`created:` >= 2026-08-17; nothing existing goes red, and the
probe asserts the live scope is empty at ship time), fail-closed over a
convention-derived scope, with an audited prose-only escape hatch, a closed
vocabulary that reuses CN-2's chirality tokens verbatim, and the CN-2
principle load-bearing throughout: **a site can comply by declaring its
ambiguity.** `UNTYPED` is always legal, always counted, and printed every
run — because a gate that reds honesty trains plausible-token lying, which
is strictly worse than a declared gap.

---

## 0. PREFLIGHT — retrieval before design, then six specialist lenses

**Retrieval ran first.** Searched for existing typed-object conventions
before inventing anything: `lab/specifications/six-axis/six-axis-template.md`
(menu-plus-hard-rule pattern; Layer-0 homonym doctrine; *"None known" is
acceptable but must be stated*), `VERIFICATION.md` (the three-level honesty
split), `GEOMETER-VS-PHYSICS-OBJECTS.md` (*"you must IDENTIFY which one you
are using and WHY"*), the K77 conditional-build habit of prose `**Carrier:**`
bullets (real, but unstructured and unenforced — e.g.
`selected-k77-i2b-projected-adjoint-jet-prolongation-2026-08-13.md`), CN-2's
closed four-value chirality vocabulary with bracketed visible tokens, SA-1
§2.3's homonym-typing table, and the two donor gates
(`kill_target_claim_audit.py` for scope/cutoff/hatch/self-test discipline,
`source_native_comparator_routing_audit.py` for derived-scope and
classification-regex lessons). The block format below is a composition of
those existing habits into one machine shape; the only new inventions are
the fence name, the key grammar, and the registered-homonym rule.

**Lens 1 — type-system designer.** A declaration format fails two ways:
too weak (free text, nothing checkable) or too strong (authors cannot
inhabit it honestly, so they lie). Route: closed vocabularies ONLY where this
week produced a concrete confusion (layer, chirality, owner, map type), free
text everywhere else, `UNTYPED` as a first-class inhabitant of every typed
slot. *Cheapest kill:* if any of this week's five errors needs a slot the
format lacks, the format is wrong.

**Lens 2 — schema/metadata standards.** Frontmatter or fenced block? The
kill gate reads frontmatter; but CN-2's repair chose **visible prose
tokens** and recorded why: *the whole point is that a reader sees it*, and
the house frontmatter parser is line-based `key: value`, hostile to nesting.
Route: a fenced block in the body — greppable info-string, line-based
grammar with indented continuations, one block per typed result, `result:`
binding each block to what it types (blocks must name their result, the
same discipline as kills naming their target claim). *Cheapest kill:* a
format the existing line-based parsers cannot read without a YAML library.

**Lens 3 — static-analysis architect.** What can a regex gate actually
verify? Presence, vocabulary membership, and structural co-occurrence — not
mathematical truth. Route: design every check as presence/vocabulary
(`LAYER=` present and valid; `ON=` present; `MAP-TYPE=` in the closed set;
registered homonym never bare), and say plainly in the gate's own output
that a green scan bounds only the SIGNALLED class. *Cheapest kill:* a check
that requires understanding the mathematics — it would be vacuous or wrong.

**Lens 4 — form design / compliance ergonomics.** A block nobody fills
correctly is worse than none. Route: seven keys, one line each, every
example in this artifact copy-pastable; the two REAL failure-pressure
points (an author who does not know, an artifact that has no result) each
get a legal, honest, cheap answer — `UNTYPED` and `EXEMPT-PROSE-ONLY` — so
the dishonest answer is never the cheapest. *Cheapest kill:* if the honest
author of SA-1's §5 residue (who genuinely cannot type the action owner)
cannot write a green block, the design fails. §6 block 2 is that test, and
it is green with `action_owner: UNTYPED` counted.

**Lens 5 — process-gate architect.** Follow the ratified house pattern or
create a rival enforcement culture. Route: copy `kill_target_claim_audit.py`
structurally — convention-derived scope (its own comment records how an
enumerated scope let a new namespace escape), date cutoff, baseline 0 never
raised, audited hatch counted and printed, self-test with planted controls,
injectable baseline pinned to 0 in the self-test (the donor's SELF-TEST
VACUITY lesson, learned when a scope baseline silently swallowed the
planted reds). One hardening over the donor: `created:` values are unquoted
before the date compare — a quoted `"2026-09-01"` lexically precedes `"2"`
and would silently leave scope; the donor has that latent defect and this
gate does not. *Cheapest kill:* any behavior the donor pattern already
solved that this gate re-solves differently without a reason.

**Lens 6 — measurement / Goodhart auditor.** The metric is "blocks
present and valid," so the gamed equilibrium is valid-but-vacuous blocks.
Route: make vacuity VISIBLE rather than illegal — the untyped census and
ALL-UNTYPED per-path naming are printed every run, exactly as the kill
gate prints hatch uses; the documented escalation condition is sustained
nonzero ALL-UNTYPED on result-bearing artifacts, and the documented
retirement condition is sustained zero-red with zero hatch abuse. *Cheapest
kill:* if the cheapest compliant block is also invisible, the gate trains
boilerplate; §7 prices that block and shows it is loud.

---

## 1. THE BLOCK FORMAT

A fenced code block whose info string is `gu-typed-objects` (fence written
at column 0; shown indented here so this specification is not itself parsed
as a block), containing exactly these seven keys, one `key: value` line
each, indented lines continuing the previous key, `#` comments allowed:

    ```gu-typed-objects
    result:         WHICH result this block types. Never UNTYPED: a block
                    that binds nothing is boilerplate by construction.
    carrier:        the object the result lives on, carrying two mandatory
                    inline fields: LAYER=<ambient|observed|source-print|toy|
                    UNTYPED>, where a mixed value like ambient+observed
                    REQUIRES BRIDGE=<named map>; and CHIRALITY=<S-FULL-DIRAC|
                    S-HALF-OPPOSITE|S-HALF-SAME|S-CHIRALITY-UNTYPED|N/A> --
                    CN-2's closed vocabulary verbatim, plus N/A for
                    spinor-free carriers. N/A on a spinor carrier is red.
    pairing:        the form/pairing WITH ON=<what it lives on>, or NONE,
                    or UNTYPED. ON= is the algebra-vs-module slot: the
                    domain is written, not implied.
    real_structure: free text, or N/A, or UNTYPED.
    grading:        free text, or N/A, or UNTYPED.
    action_owner:   who supplies/owns the object. Must begin with one of:
                    source-action, observer, repository-construction,
                    comparator, source-print, N/A, UNTYPED. A qualifier may
                    follow the token.
    target:         the object/codomain the result is about, WITH
                    MAP-TYPE=<projection|contraction|inclusion|restriction|
                    pullback|pushforward|quotient|isomorphism|homomorphism|
                    intertwiner|evaluation|not-a-map|UNTYPED>.
    ```

**Registered homonyms.** `so(1,3)`, `so(3,1)`, `ad(P_H)` — seeded from this
week's actual collisions — may not appear bare in `carrier`, `pairing` or
`target`: they need a subscript (`so(1,3)_endo`, `ad(P_H)_{u(64,64)}`) or
the explicit token `HOMONYM-AMBIGUOUS`, which is counted in the ambiguity
census like every other declared unknown. If the homonym lane ships a
registry under `lab/process/`, it should supersede the gate's seeded
constant; the gate deliberately does not read files a sibling agent is
concurrently creating.

**The CN-2 principle, restated as the format's contract.** Every typed slot
admits `UNTYPED` (the chirality slot admits `S-CHIRALITY-UNTYPED`; the
homonym rule admits `HOMONYM-AMBIGUOUS`). Declared ambiguity is compliance.
It is counted, and the census is printed every run, with blocks whose every
object slot is UNTYPED named per-path as `ALL-UNTYPED` — visible, never
red. The one thing that may not be UNTYPED is `result:` — a block must say
what it is typing, or it is not a declaration at all.

## 2. THE TRIGGER — and, honestly, what it misses

An artifact is REQUIRED to carry a block (or the hatch) when it is in scope
— markdown, dated YAML frontmatter, `created:` >= 2026-08-17 — and shows any
of four signals that it STATES a mathematical result:

1. **a certificate line** — the house shape `N/N` (equal counts) plus
   `exit 0`/`checks` on one line ("105/105 checks pass ... exit 0");
2. **a probe reference** — a `scripts:` frontmatter key referencing `tests/`;
3. **a result-bearing `doc_type`** — matching result / construction /
   certificate / theorem / proof / classifier / census / crosswalk /
   determination / no-go / delta / gate (vocabulary surveyed from the 200+
   doc_types in the live tree);
4. **`grade:` declaring EXACT arithmetic.**

**What it misses, stated rather than implied.** A result asserted in prose
with none of the four signals is invisible — the same ceiling as the kill
gate's kill-language trigger, and the gate prints this every run
(`[trigger-ceiling]`). Non-markdown surfaces (JSON ledgers, probe
docstrings) are out of scope. A file with no `created:` field is out of
scope entirely — fail-closed means the scope rule is convention-derived,
not that a conventionless file is caught. And the trigger FALSE-FIRES by
design on prose that QUOTES a certificate ("reproduces LA-8, 78/78,
exit 0" in a read packet): the audited hatch is the pressure valve for
exactly that class, which is why every hatch use is printed.

## 3. THE EXEMPTION — audited, on the NONE-NOT-A-KILL pattern

A prose-only artifact (index, disposition, read packet, reprioritization)
declares frontmatter `typed_objects: EXEMPT-PROSE-ONLY`. Uses are counted
AND path-printed every run, exactly as the kill gate prints its hatch.
Two hard edges keep the hatch honest:

- **Any other value of `typed_objects:` is red** — an unregistered
  exemption token (`EXEMPT-BECAUSE-PROSE`, `EXEMPT`, ...) fails, so the
  hatch cannot drift into a private vocabulary.
- **The hatch is disallowed where it self-contradicts:** a `doc_type` that
  itself declares a result (result / construction / certificate / theorem /
  proof) cannot simultaneously claim to state none. That combination is
  red, not exempt.

## 4. THE FIVE-ERROR ACCEPTANCE TEST

Design constraint: every failure this week maps onto a named slot, and the
block would have caught it (a red) or surfaced it (a printed declaration a
reader can dispute). All five loci are cited files in this repository; the
probe string-matches each one, so this table cannot silently rot.

| # | this week's actual error | locus | block slot | caught or surfaced how |
|---|---|---|---|---|
| E1 | `Omega^1(S)` written without saying which `S`; three inequivalent readings; 13 declaration sites, none typed | `carrier-notation/cn2-notation-carries-the-answer-2026-08-15.md` (and CR-B, canon A2) | **carrier — CHIRALITY subfield** | a spinor carrier cannot omit CHIRALITY (red: `CARRIER-NO-CHIRALITY`) and cannot wave it off as N/A (red: `SPINOR-CHIRALITY-NA`); it either picks a CN-2 token or declares `S-CHIRALITY-UNTYPED`, which is green AND counted — the census IS the surfacing |
| E2 | OT-1's theorem is about invariant forms on the ALGEBRA (`6 of 15` at d=4); LT-GR6b's trigger asks for a pairing on the MODULE (`12 of 12`); same group, opposite answers, inverted one hop from the owner | `base-duality/bd-a-...-2026-08-15.md`, README ("A domain error inverted the answer.") | **pairing — ON= clause** | a pairing without `ON=` is red (`PAIRING-NO-ON`); OT-1's block reads `ON=Lie(W) (the algebra, dim 15)`, the trigger's demand reads `ON=V (the module, dim 12)` — the relay carries two visibly different domains, and quoting the block (relays quote operative sentences) transports the domain with the claim |
| E3 | two six-dimensional Lorentz subalgebras of one soldered `so(7,7)`, intersecting in zero, giving 0 and 21 on the same `k`, both written `so(1,3)` | `soldered-ad/sa1-...-2026-08-16.md` | **carrier — registered homonym + LAYER** | `so(1,3)` is a REGISTERED HOMONYM: bare use in a block is red (`HOMONYM-BARE`); the author must write `so(1,3)_endo` or `so(1,3)_H` or say `HOMONYM-AMBIGUOUS`; and the ambient/observed LAYER field types which stratum the claim binds — SA-1's own layer split, made mandatory |
| E4 | the observation reduction retyped as a projection ("vertical components become 4D scalars"), when it is a **contraction** — `(s^*omega)_mu = omega_mu + omega_(ab) d_mu g_ab` — inside a mandatory method boundary | the withdrawn `[!CAUTION]` clause in `lab/methods/source-native-comparator-routing.md` | **target — MAP-TYPE token** | MAP-TYPE is mandatory and closed-vocabulary; the false clause forced into a block must write `MAP-TYPE=projection` — a one-token, one-grep contradiction with the owner artifact's `MAP-TYPE=contraction` (MD-1 E1–E3), instead of a buried prose implication |
| E5 | the word "observer" dropped in a relay: OT-1 wrote leg (b) is *"the observer's metric geometry"*; one artifact later it was *"a source-owned global base duality"* to be built | `base-duality/README.md` ("The relay defect, located to one word") | **action_owner — closed token** | `action_owner:` is a required key whose value must begin with a closed token; OT-1's block carries `action_owner: observer`, and the receiving artifact either quotes it (the owner travels) or writes a new block flipping one visible token to `source-action` — a diffable flip at exactly the slot where the word dropped, instead of a silent frame regression |

The five demonstrations, in minimal form (rendered as `text`, NOT as live
blocks — each is the line an author would have had to write, and what the
gate says back):

```text
# E1  WOULD-BE-RED
carrier: Omega^1(S) LAYER=ambient CHIRALITY=N/A
   -> SPINOR-CHIRALITY-NA        (and with CHIRALITY absent: CARRIER-NO-CHIRALITY)
# green alternatives: CHIRALITY=S-FULL-DIRAC | S-HALF-OPPOSITE | S-CHIRALITY-UNTYPED (counted)
```

```text
# E2  WOULD-BE-RED
pairing: Ad-invariant symmetric form
   -> PAIRING-NO-ON
# green: pairing: Ad-invariant symmetric form ON=Lie(W) (algebra, dim 15)
#    vs: pairing: fibre metric ON=V (module, dim 12)   -- the inversion is now a visible diff
```

```text
# E3  WOULD-BE-RED
carrier: so(1,3) inside so(7,7) LAYER=ambient CHIRALITY=N/A
   -> HOMONYM-BARE:so(1,3):carrier
# green: so(1,3)_endo ...  |  so(1,3)_H ...  |  so(1,3) HOMONYM-AMBIGUOUS ... (counted)
```

```text
# E4  WOULD-BE-RED
target: 4D scalar fields from vertical components MAP-TYPE=squishing
   -> TARGET-BAD-MAPTYPE:squishing   (and with MAP-TYPE absent: TARGET-NO-MAPTYPE)
# the false claim must write MAP-TYPE=projection -- one grep from the owner's MAP-TYPE=contraction
```

```text
# E5  WOULD-BE-RED
action_owner: the global base duality the theory owes
   -> OWNER-UNTOKENED
# green: action_owner: observer -- MET(X) is an ARGUMENT the observer supplies (BD-C)
```

**Honesty about mechanism.** E1, E3 and E5-as-written are hard reds. E2 and
E4 are *surfacing* slots: the gate cannot know the true domain or the true
map type — it forces the author to WRITE one, in a place where a wrong
token is a one-line diff against the owning artifact's block rather than a
prose implication three sentences deep. That is the same trade the kill
gate makes: it cannot verify a kill, only force the kill to name its
target.

## 5. WHAT THE GATE CHECKS (mechanics)

`process_gates/typed_carrier_declaration_audit.py` — modelled on
`kill_target_claim_audit.py`. Scope derived from convention (all `**/*.md`
minus vendor dirs, dated frontmatter, `created:` >= 2026-08-17 after
unquoting). Per block: key-set equality, per-slot grammar, LAYER/CHIRALITY
presence and vocabulary, mixed-layer-requires-BRIDGE, ON= presence,
owner-token prefix, MAP-TYPE vocabulary, registered-homonym scan. Per
artifact: trigger => (>=1 block | registered hatch); unregistered exemption
tokens red; hatch-on-result-doc_type red. Printed every run: red list,
counters (scope / triggered / blocks / exemptions), every exemption path,
the untyped census with ALL-UNTYPED paths, and the trigger-ceiling
statement. Baseline 0, injectable, pinned to 0 in the self-test. Exit 1
iff red exceeds baseline.

## 6. WORKED EXAMPLE — SA-1, two subalgebras, one bundle (live blocks)

SA-1 is the acceptance case with the richest typing surface: one decided
bundle layer, one blocked observed layer, a typed homonym, and a residue
that is honestly un-ownable today. Its two core results, as the blocks its
author would ship (both validate clean against the gate; the probe asserts
it):

```gu-typed-objects
result: SA-1 bundle layer -- INERT-AD as typed is refuted; P_H is an associated bundle of Fr~(C)
carrier: ad(P_H)_{u(64,64)}, with P_H = P_Fr~(C^{7,7}) x_{rho_D} H over Y = Met(X)
  LAYER=ambient CHIRALITY=N/A
pairing: invariant form B ON=S_128 (full 128-dim real Dirac module of Cl(7,7)); B^2=1, tr B=0, sig B=(64,64)
real_structure: real Clifford algebra Cl(7,7) = M_128(R); grades one and two both B-skew
grading: Clifford Z-grading; Lambda^2 C = spin(7,7) subset so(64,64) subset u(64,64)
action_owner: repository-construction (K77 2026-08-05, 53/53) reproducing source-print SC-GRP-02 eq (3.32)
target: ad(P_H)_{u(64,64)} as a Spin_0(1,3)-associated bundle via r~_C MAP-TYPE=homomorphism
```

```gu-typed-objects
result: SA-1 F07/F12-F13 -- the two Lorentz subalgebras intersect in zero; the same k gives Inv 0 vs 21
carrier: so(1,3)_endo and so(1,3)_H, both subalgebras of so(7,7) = Lambda^2 C_x
  LAYER=ambient CHIRALITY=N/A
pairing: Killing form ON=so(7,7); negative-definite on k, positive on p (PV-2, reproduced)
real_structure: swept over both Lorentzian real forms so(7,7) and so(9,5); the compact horn is not covered
grading: Cartan decomposition k (+) p, dim k = 21, dim p = 24
action_owner: UNTYPED -- which subalgebra labels observed 4D spin is an invariance property of the UNBUILT selected action (the named open gate owned by the K77 action lane; SA-1 section 5)
target: largest so(1,3)_*-invariant subspace of k MAP-TYPE=restriction
```

Three things this example demonstrates on purpose. **The homonym rule has
teeth here:** both `so(1,3)` occurrences are forced to their subscripts —
the exact one-name-two-objects defect SA-1 existed to repair cannot be
written in a block. **The `ad(P_H)` homonym is typed in the carrier line:**
`ad(P_H)_{u(64,64)}` (dim 16384) is not MD-1's `ad(P_H)` (`Lambda^2` of the
14-dim carrier, dim 91), and the subscript rule forces the distinction SA-1
§2.3 had to make in a table. **The blocked residue is a green, counted
declaration:** `action_owner: UNTYPED` with the pointer to the owning open
gate — SA-1's §5 conclusion, compressed to one honest slot. The probe
asserts this block validates with exactly one declared-ambiguous slot.

## 7. HOSTILE REVIEW — will this get filled honestly, or gamed?

**The cheapest compliant-but-useless block, priced.** Seven lines: a real
`result:` line plus six `UNTYPED`s (with `LAYER=UNTYPED
CHIRALITY=S-CHIRALITY-UNTYPED` and `MAP-TYPE=UNTYPED`). The gate
deliberately does NOT red it. What it does instead: counts eight ambiguous
slots, names the artifact on the `ALL-UNTYPED` line of every subsequent
run, forever, until repaired. The bet — the same bet CN-2 already won at 13
sites, where ten sites honestly took the ambiguous token and zero took the
protected reading — is that a loud declared unknown gets repaired, while a
forced guess gets BELIEVED. The all-UNTYPED author has, at minimum, told
the reader "do not trust my typing," which is strictly more information
than today's prose.

**The gamed equilibrium that actually worries me** is not all-UNTYPED — it
is the PLAUSIBLE WRONG TOKEN: `LAYER=ambient` written by reflex,
`MAP-TYPE=projection` written because projections are familiar. The gate
cannot catch a false token (stated in §4; it is a grammar checker, not a
referee). Two mitigations are real rather than decorative: a wrong token is
a one-line, greppable, quotable assertion — E4 shows the contradiction
becoming a one-grep diff between two blocks, where the same error in prose
survived inside a mandatory method file for a day — and the block travels
with relays (quote the block, not a paraphrase), so a receiving artifact
inherits the operative tokens instead of re-deriving a frame. What the
design refuses to do is add more mandatory structure to resist it: every
additional required subfield raises the cost of honest compliance and
recruits more reflex-filling, which is how forms train boilerplate.

**Will authors comply at all?** The trigger fires on exactly the artifacts
that already ship a probe, a certificate line, and a six-field frontmatter
block — authors already paying two orders of magnitude more effort than
seven lines. The marginal cost is real but small; the failure I actually
expect is drift in QUALITY, which the census is built to make visible, and
the escalation/retirement conditions are stated in the gate docstring
(escalate on sustained ALL-UNTYPED among result-bearing artifacts; retire
the way the kill gate retires, on sustained zero-red with zero hatch
abuse).

**Steelman against the whole design:** "CN-2 already fixed notation at the
sites; SA-1 types its homonyms in prose; the culture is learning — a gate
adds bureaucracy to a solved problem." Answer: the culture learned at
FOURTEEN sites after the fact, and the same week produced E2, E4 and E5 in
fresh locations, none of which is a notation site CN-2 covered. The lesson
of the week is that instance repairs do not propagate; the one repair that
held (CN-2's) is precisely the one that installed a checkable vocabulary.
This gate generalizes the repair that worked, prospectively, at the price
of seven lines per certified result.

## 8. CERTIFICATE

`tests/channel-swings/joe_directed_fx2_typed_carrier_declaration.py` —
**67/67 checks, exit 0** (validation run 2026-08-17; the artifact date is
the brief's assigned path).

```
  [V] 22   validator: every defect class produced and matched by FULL
           defect-list equality; contrary controls (declared bridge,
           declared ambiguity, NONE pairing, subscripted homonyms) clean
  [F] 10   file-level audit on fixtures: exact counters (scope 5,
           triggered 4, exemption ["pass_hatch.md"], untyped slots 7,
           blocks 3); pre-cutoff garbage green; quoted-date hardening;
           representative planted fact red via the public API
  [A] 17   this artifact: routing notice + INTERNAL_STRUCTURAL_ONLY under
           the routing audit's own regex; NONE-NOT-A-KILL; exactly two
           live blocks, both validating clean; block 2 has exactly one
           declared-ambiguous slot (the action owner); five WOULD-BE-RED
           demos, none live; both subalgebras subscripted; the required
           registry write printed verbatim; all five error loci exist
  [S] 12   exact substrings read from AGENTS.md, CN-2, BD-A, the
           base-duality README, SA-1, the routing method's withdrawn
           clause, the kill gate, the routing registry, the six-axis
           template, and GEOMETER-VS-PHYSICS-OBJECTS.md
  [R]  6   gate --selftest exits 0 and reports GREEN; poisoned baseline
           exits 1 AND prints the refusal; live scan printed as a dated
           reconciliation (asserted red==0 only under --strict, per the
           CN-2 shared-checkout rule); no float anywhere (swept)
       of which 3 are PLANTED-FALSE propositions that must come back False
```

Failure paths exercised, both layers:

- **Gate `--selftest`:** clean fixture baseline verified FIRST (exit-1
  refusal if not green, proven non-vacuous by `--poison-baseline`), then
  10/10 planted false facts each exit 1: `fail_missing_field`,
  `fail_mixed_layer_no_bridge`, `fail_unregistered_exemption` (the brief's
  three), plus `fail_no_block`, `fail_bare_homonym`, `fail_spinor_na`,
  `fail_pairing_no_on`, `fail_bad_maptype`, `fail_hatch_on_result_doctype`,
  `fail_result_untyped`.
- **Probe `--selftest`:** clean baseline subprocess verified FIRST, then
  10/10 machinery mutations each drive exit 1 (`cutoff-early`, `keys-drop`,
  `maptype-loose`, `homonym-empty`, `hatch-drift`, `spinor-blind`,
  `cert-blind`, `layer-loose`, `on-blind`, `artifact-gone`); every mutation
  corrupts an instrument constant, because a weakened assertion is not a
  detectable mutation. `--selftest --poison` poisons the baseline run and
  requires the refusal path.

```
_local/cas-venv/bin/python tests/channel-swings/joe_directed_fx2_typed_carrier_declaration.py
    -> CERTIFICATE: 67/67 checks pass; 0 planted-false observed true.     exit 0
_local/cas-venv/bin/python tests/channel-swings/joe_directed_fx2_typed_carrier_declaration.py --selftest
    -> clean baseline first, then 10/10 mutations each exit 1.            exit 0
_local/cas-venv/bin/python process_gates/typed_carrier_declaration_audit.py
    -> 0 red (baseline 0); 0 files in dated scope >= 2026-08-17.          exit 0
_local/cas-venv/bin/python process_gates/typed_carrier_declaration_audit.py --selftest
    -> SELF-TEST GREEN.                                                   exit 0
```

## 9. POSTFLIGHT — six lenses, run after the build

**Schema reviewer.** Seven keys, four closed vocabularies, two conditional
rules (mixed-layer bridge, spinor chirality), one seeded homonym list. No
nesting, no YAML dependency, line-grammar parseable by the same idiom the
house frontmatter parser uses. The format survived its own acceptance test:
all five errors land in distinct slots, none needed an eighth key — and
lens 1's kill condition (a needed slot the format lacks) was not tripped.

**Adversarial author.** I tried to write a green block that smuggles E3:
`carrier: the Lorentz subalgebra LAYER=ambient CHIRALITY=N/A` — no
registered token, no subscript, green. So prose paraphrase evades the
homonym rule; only the NAMED symbols are guarded. That is a real hole,
recorded here rather than papered over: the homonym list guards the
collision names we HAVE, and each new collision this channel finds should
be added to the seeded constant (one line) or to the future homonym
registry. The hole is bounded by the fact that unnamed paraphrase also
carries no false precision — the danger of homonyms is the shared NAME.

**Gate maintainer.** Runtime cost: one glob over ~4000 markdown files plus
regex work on the dated subset — the live run completes in under two
seconds today. The two integration writes are one line each and both
gates' failure messages name the exact fix. `LAYER`/`OWNER`/`MAP` vocabularies
are module constants with no hidden coupling; extending a vocabulary is a
one-token diff reviewed like any control change.

**Concurrency auditor.** The checkout is shared: the cutoff means sibling
writes dated today or earlier can never enter scope, the probe's repo-wide
totals are printed-not-asserted (strict mode exists for a quiet tree), and
this artifact's three paths collide with no sibling surface (the
needs-provides and homonym lanes are explicitly untouched). The gate reads
no file a sibling is concurrently creating.

**Source-fidelity check.** Nothing here adjudicates a source claim, and
every quoted error is quoted from the repository artifact that owns it,
with the probe string-matching each locus. The five-error table asserts
nothing about GU physics; it asserts that five specific repository records
exist and say what this artifact says they say. `INTERNAL_STRUCTURAL_ONLY`
is the registered vocabulary for exactly this class, added 2026-08-16 when
four artifacts independently invented near-identical out-of-vocabulary
declarations — evidence the class is real.

**Retirement/rot auditor.** Non-retroactivity is permanent (the cutoff
never moves), so the gate's cost falls entirely on future authors, which is
where the leverage is. Rot risks: the doc_type vocabulary drifts (new
result-bearing types that miss the trigger regex — the trigger-ceiling
line keeps that visible); the homonym constant goes stale (superseded by
the homonym lane's registry when it ships); the fence name is load-bearing
(a renamed fence silently de-registers a block — but then the artifact has
no block and the trigger reds it, which fails safe). The stated retirement
condition mirrors the donor gate's: sustained zero-red with zero hatch
abuse and a typing culture that no longer needs the check.

## 10. WHAT THIS DOES NOT SUPPLY

No science result, no claim movement, no verdict, no ledger edit, no canon
movement. No retroactive judgment of any existing artifact — the live
scope is empty at ship time and the probe asserts it. No edit to
`AGENTS.md`, the routing registry, `process_gates/README.md`, any method
file, or any existing artifact — the two required one-line integration
writes are printed verbatim in the routing notice and belong to the
canonical integrator. No needs-provides surface, no homonym-registry
surface (sibling lanes). No claim that the block format verifies
mathematical truth: it verifies that the author STATED the type, in a
vocabulary a machine can hold them to, with honest ambiguity always legal,
counted, and printed. The enforcement ceiling — grammar, not truth — is
stated in §4, in §7, and by the gate itself on every run.
