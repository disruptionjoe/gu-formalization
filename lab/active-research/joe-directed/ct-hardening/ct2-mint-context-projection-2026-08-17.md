---
artifact_type: exploration
status: exploration
doc_type: schema_and_gate_design_record
created: 2026-08-17
work_item: CT-2
channel: ct-hardening
title: "CT-2: every row a future mint touches carries its (layer, grant, carrier) projection. An additive schema sibling (conditional-physics-ledger-schema-v0.2.json -- v0.1 is NOT edited, and all 259 live ledgers validate against v0.2 UNCHANGED, which is the non-retroactivity promise in machine-checkable form), a methods note where mints will read it, and a fail-closed gate scoped to ledger versions >= v0.260 that reads its three codomains out of CT-1's tables on every run. UNTYPED stays legal, counted and printed (CN-2), with exactly one notch added: an UNTYPED slot needs a note. The never-launder law binds the new surface too -- G0 on a DERIVED_CONDITIONAL row is the launder in projection form and reds, and a row that names its own condition cannot escape into UNTYPED. Three worked projections for rows IM-1 actually touched, two of them honestly UNTYPED with the plausible-looking token named and refused. Retrieval finding: the v0.1 schema has validated nothing since v0.1 (21 errors on v0.259, 14 on every ledger from v0.100), and its closed row vocabulary is left closed-in-name-only rather than silently re-imposed."
grade: "EXACT integer counters only; no float anywhere (the probe sweeps the gate's result surface and asserts none). Probe tests/channel-swings/joe_directed_ct2_mint_context_projection.py: 78/78 checks, exit 0 -- 15 schema checks (v0.2 well-formed; ALL 259 live ledgers validate unchanged; v0.1 byte-unedited and still validating the v0.1 ledger; a synthetic v0.260 validates with AND without context; 12 malformed contexts rejected, 4 legal shapes accepted), 8 codomain checks (three-surface triangle gate/pin/CT-1, the four condition markers derived from CT-1's own braced Grant names, four fail-closed reference fixtures each caught including a TOOTHLESS reference that must red rather than pass), 7 scope checks (live repo green with 0 in scope and 259 out; a v0.260 changing nothing is green; accretion is free -- adding context alone leaves a row untouched; version order numeric so v0.30 stays out), 7 planted controls (missing context on a touched row, out-of-codomain token, LAUNDER-IN-PROJECTION, GRANT-OMITS-NAMED-CONDITION, bare declared-unknown without a note -- each CAUGHT -- plus two CONTRARY controls, an all-UNTYPED-with-note projection and the real v0.259, each of which must stay GREEN), 14 worked-projection checks (all three pass the gate together; every justification read back from the live v0.259 row and from CT-1, never remembered), 5 predeclared-FALSE propositions each observed False, 22 artifact/runtime checks (routing notice, INTERNAL_STRUCTURAL_ONLY, one clean gu-typed-objects block with exactly one declared-ambiguous slot, the two new markdown files green under the typed-carrier gate, the new gate's --selftest GREEN and --poison-baseline REFUSING by subprocess). Gate --selftest: clean baseline verified FIRST, then 15/15 planted false facts each exit 1. Probe --selftest: clean baseline verified FIRST, then 10/10 machinery/reference mutations (gate-gone, ref-gone, schema-gone, ledger-glob-blind, version-pin-drift, pinned-codomain-drift, marker-pin-drift, root-elsewhere, synthetic-untouched, context-key-drift) each drive exit 1 via genuine FAIL lines with crash-catches rejected; --selftest --poison requires the refusal path. NOT: a physics result, a claim movement, a ledger/canon/registry edit, a new category object, or any judgment of a v0.259-or-earlier row."
disposition: CONTEXT_PROJECTION_SPECIFIED_AND_ENFORCED_FOR_V0_260_ONWARD__SCHEMA_V0_2_ADDITIVE_SIBLING_VALIDATES_ALL_259_LEDGERS_UNCHANGED__V0_1_NOT_EDITED__CODOMAINS_READ_FROM_CT1_FAIL_CLOSED_INCLUDING_TOOTHLESS_REFERENCE__UNTYPED_LEGAL_COUNTED_PRINTED_WITH_NOTE_REQUIRED__NEVER_LAUNDER_BINDS_THE_PROJECTION_G0_ON_CONDITIONAL_ROW_REDS__NAMED_CONDITION_CANNOT_ESCAPE_INTO_UNTYPED__THREE_WORKED_PROJECTIONS_TWO_HONESTLY_UNTYPED__V0_1_SCHEMA_ROT_REPORTED_NOT_SILENTLY_REPAIRED__G8_WIDENING_AND_G6_UNCHECKABILITY_REPORTED_TO_OWNERS
target_claim: NONE-NOT-A-KILL -- this stage adjudicates no source claim. It specifies and enforces a repository bookkeeping obligation on future ledger mints.
canon_verdict_change: none
priority_change: none
steering_effect: unchanged
canonical_effect: pending_integration
rows_changed: []
rows_laundered: []
depends_on:
  - lab/methods/gu-base-categories.md
  - lab/process/conditional-physics-ledger-schema-v0.1.json
  - lab/process/conditional-physics-ledger-schema-v0.2.json
  - lab/process/conditional-physics-ledger-v0.259.json
  - lab/process/conditional-physics-ledger-v0.258.json
  - lab/methods/mint-context-projection.md
  - process_gates/mint_context_projection_audit.py
  - process_gates/typed_carrier_declaration_audit.py
  - lab/active-research/joe-directed/integration-mint/im1-two-movers-four-debts-and-three-adjudications-2026-08-17.md
  - lab/active-research/joe-directed/ct-hardening/ct1-base-categories-2026-08-17.md
  - lab/active-research/joe-directed/carrier-decl/fx2-typed-carrier-declaration-2026-08-16.md
  - lab/active-research/joe-directed/carrier-notation/cn2-notation-carries-the-answer-2026-08-15.md
  - VERIFICATION.md
scripts:
  - tests/channel-swings/joe_directed_ct2_mint_context_projection.py
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
> Everything below is repository-internal process work: a JSON Schema sibling,
> a methods note, a process gate and a probe. No physics object is computed,
> no comparator is run, no source claim is tested. The one place this record
> borders comparator content is where it quotes rows whose own evidence is
> comparator-provenanced (`LT-SM8`'s `CB-B:SM-8` wording); those rows' routing
> obligations are carried by their own artifacts and are not altered here.
>
> **REQUIRED INTEGRATION WRITE, not performed here.** This artifact was
> produced under a write scope limited to its five paths, on a checkout shared
> with concurrent agents, so it edits no registry and no README. One one-line
> write belongs to the canonical integrator, without which
> `process_gates/source_native_comparator_routing_audit.py` counts one more
> unclassified artifact (`UNCLASSIFIED_BASELINE` must NOT be raised):
>
> ```json
> { "path": "lab/active-research/joe-directed/ct-hardening/ct2-mint-context-projection-2026-08-17.md",
>   "classification": "INTERNAL_STRUCTURAL_ONLY" }
> ```

# CT-2 — the non-retroactive context projection for mint-touched ledger rows

**Written:** `lab/process/conditional-physics-ledger-schema-v0.2.json` (shape),
`lab/methods/mint-context-projection.md` (the rule, where mints read it),
`process_gates/mint_context_projection_audit.py` (enforcement), this record and
its probe. **Not written:** the v0.1 schema, any ledger, CT-1's reference, any
registry, any README.

---

## 0. PREFLIGHT — retrieval before work, then seven problem-matched lenses

### 0.1 Retrieval performed BEFORE any write

| # | retrieved | what it fixed |
|---|---|---|
| R1 | `conditional-physics-ledger-schema-v0.1.json`, then **validated it against every live ledger** | The design's foundation, and a surprise: v0.1 validates v0.1 and **nothing after it** — 14 errors on v0.100/v0.200/v0.250/v0.258, 21 on v0.259. `schema_version` is pinned `const: "0.1"` and rows are `additionalProperties: false` while live rows carry twelve accreted keys. Any claim that "the schema validates the ledger" was already false; I had to design v0.2 to be the schema that *actually* validates the series, not a patch on a fiction. |
| R2 | v0.259 `migration_policy` verbatim: *"DERIVED_CONDITIONAL → DERIVED is forbidden; every status move records its grant"* | The never-launder law in the ledger's own words — and the thing a `grant` slot could quietly undo. |
| R3 | IM-1's `rows_changed` (14) and the actual v0.258→v0.259 row diff (11 changed + 3 new = 14, exact match) | The real definition of "touched", and the three worked rows. IM-1's discipline is the one to extend: `rows_laundered: []`, every move carrying its grant, base sha256 recorded. |
| R4 | CT-1 §1.1/§2.1/§3.1–§3.2 tables and §4 D1–D4 | The three codomains and — load-bearing — the **D2 trap**: three axes share the word "layer". Reading the gate's `LAYER=` stratum as a Source-Layer object is the error the worked examples had to refuse out loud. |
| R5 | `typed_carrier_declaration_audit.py` `codomain_drift()` | The exact wiring pattern to copy: read the codomain from CT-1 at runtime, compare against module constants, red on drift in either direction, fail closed if the reference is missing. |
| R6 | FX-2's non-retroactive cutoff and its CN-2 block | The accretion pattern and the honesty principle: *"Making honesty red would train plausible-token lying, which is strictly worse than a declared gap."* |
| R7 | `VERIFICATION.md` §"Probe and mutation-harness discipline", all seven rules | Clean-baseline-first, machinery-only mutations, genuine-`[FAIL]` catches, planted-positive controls, exit-0-on-success, tolerances must not absorb controls. |
| R8 | Marker derivability test **run before committing to the design**: do CT-1's braced Grant names yield markers that actually occur in row text? | `GRANT-ACA1-C1` → AC-A1/AC-A2/AC-A3; `INHERITANCE_BRIDGE` → RA-D4/LT-SM8/AC-F1; each hit inspected and genuine (RA-D4 prices a conjunct "under condition INHERITANCE_BRIDGE only"; AC-F1 "inherits condition INHERITANCE_BRIDGE"). **Zero false positives.** `SC-CHI-01` and `HYP-TW-COHERENCE-01` yield zero row hits — a stated limitation, not a silent one. This test is what turned the agreement rule from an idea into a rule with teeth. |

### 0.2 Seven lenses

**Lens 1 — schema migration.** *Does the sibling validate what it claims?* R1
says the incumbent does not. So v0.2's headline property had to be measured,
not asserted: **all 259 live ledgers validate against v0.2 unchanged**, pinned
in the probe. Relaxing `schema_version` from a `const` to a pattern is not
loosening for convenience — the frozen const, not the ledger, is the defect.

**Lens 2 — the adversarial mint (the brief's hostile question).** *What is the
cheapest compliant projection?* `{"layer":"UNTYPED","grant":"UNTYPED",
"carrier":"UNTYPED"}`. CN-2 forbids me from making that red. So the design
goal became: make the cheap path **visible**, make the *dishonest* cheap path
**impossible**, and be blunt that the *wrong-but-plausible* path survives.
See §5.

**Lens 3 — scope boundary.** *Can the non-retroactive boundary drift?* Two
attacks found. (a) **Version ordering**: `0.26` is twenty-six and precedes
`0.259`, but string-compares as greater — a lexical compare would drag every
`v0.3x`–`v0.9x` ledger into scope. Versions are compared as int tuples and the
gate's fixture set includes a `v0.30` file that must stay out. (b)
**Misfiling**: `v0.134.json` declares `schema_version: 0.133` (measured, one
file in 259). Scope therefore uses `max(filename, internal)` so a ledger cannot
leave scope by being misnamed.

**Lens 4 — rival surfaces (FX-3: consolidate, never rival).** *Am I coining
objects or re-owning a codomain?* No object is coined. All three codomains are
read out of CT-1 at runtime; the methods note says so and says that a row
demanding an absent object is **a finding to report, not a token to invent**.
Two live temptations were refused: re-closing the row vocabulary (§1) and
widening CT-1's G8 bucket (§4.3).

**Lens 5 — never-launder.** *Does the new surface open a second way to
launder?* Yes, and it is the whole reason the agreement rule exists: a row can
stay honestly `DERIVED_CONDITIONAL` while its projection says `G0`, and the
row would read as conditional while the *census* read as unconditional. Closed
by rule L, with rules O and M added for the other two disagreement directions.

**Lens 6 — instrument power (VERIFICATION 1–7).** *Can this gate be green while
toothless?* Found one way: if CT-1's Grant names ever lose their braces, the
marker set empties and rule M silently becomes a no-op. A rule that has quietly
lost its teeth must **red**, not pass — so an empty marker set is a fail-closed
error, and the probe plants a toothless reference to prove the detector fires.

**Lens 7 — CN-2 honesty.** *Does this make honesty red?* No. All-UNTYPED is
green, counted, and printed by row id. One notch is added and stated rather
than smuggled: an UNTYPED slot needs a `note`, because a bare `UNTYPED` is a
blank and a *declaration* of ambiguity is a sentence. The gate checks the note
exists and prints it verbatim; it does not pretend to check that it is true.

---

## 1. The schema delta

`lab/process/conditional-physics-ledger-schema-v0.2.json` — an **additive
sibling**. `v0.1` is not edited and keeps doing its original job (the probe
checks it still pins `const: "0.1"` and still validates the v0.1 ledger).

| # | change | why |
|---|---|---|
| 1 | **`rows[].context`** — new, **optional** object with required `layer`, `grant`, `carrier` and optional `note`; `additionalProperties: false` | The projection. Optional in the *shape* because the obligation is conditional on a two-document predicate; required *slots* once present, because a projection that omits an axis is indistinguishable from one that forgot it. |
| 2 | Slot grammar: `^(L[1-9][0-9]*\|UNTYPED)$`, `^(G[0-9]+\|UNTYPED)$`, `^(C[1-9][0-9]*\|UNTYPED\|HOMONYM-AMBIGUOUS)$` | The schema pins **shape**; the gate pins **membership** (that `L3` is an object CT-1 carries *today*). A schema hardcoding CT-1's object list would drift from CT-1 silently. |
| 3 | Each slot is a token **or** a non-empty array of distinct tokens | Unions are recorded truth, not hedging: CT-1 §2 states *"LT-SM8 sits at G5 ∪ G7."* Empty arrays are invalid — absence of an opinion is spelled `UNTYPED`. |
| 4 | `schema_version` relaxed from `const: "0.1"` to `^0\.[0-9]+$` | **Repair of a measured defect**, not a convenience. Receipts in the `$comment`: 14 errors on v0.100/v0.200/v0.250/v0.258, 21 on v0.259. |
| 5 | Dated header `$comment` stating the accretion rule and the schema/gate division of labour | So the next reader learns the rule from the artifact, not from this record. |
| 6 | Rows stay `additionalProperties: true`, with the accreted vocabulary recorded in a `$comment` | **Refused temptation.** v0.1's row closure has been non-operative since v0.1 (twelve accreted keys). Re-closing it would red every ledger from v0.10 and is the ledger owner's call; doing it under cover of a context patch is exactly the rival-schema move FX-3 forbids. The finding goes on the record instead. |

**The property that matters:** all **259** live ledgers validate against v0.2
**unchanged**. That is the non-retroactivity promise in machine-checkable form
— not "we intend not to touch v0.259", but "v0.259 as it stands is already
conformant."

---

## 2. The rule

Stated for authors in `lab/methods/mint-context-projection.md`; in one
sentence:

> From ledger version **v0.260** onward, every row whose content a mint changes
> — and every row a mint appends — carries a `context` object giving that row's
> `(layer, grant, carrier)` projection into CT-1's three base categories.

**Non-retroactive by construction.** v0.259 and the 258 earlier ledgers are out
of scope permanently: the series is append-only and each version immutable, so
the boundary cannot move backward. No existing row is edited; no sweep is run;
the baseline is 0 and may not be raised.

**Accretive.** Context is written exactly when someone is already adjudicating
the row — the FX-2 pattern. A retroactive typing pass would be a stranger
guessing at 84 rows in one sitting, which is the plausible-wrong-token failure
industrialised. Untouched rows may volunteer a context; nothing demands it.

**Touched** = absent from the predecessor, or content differs from the
predecessor row of the same `id`, comparing everything *except* `context`
(which is what makes voluntary accretion free). Unresolvable predecessor ⇒
**every row counts as touched** — fail closed.

**Codomains** are CT-1's, read from `lab/methods/gu-base-categories.md` on every
run: Layer objects `L*`, Grant nodes `G*` (objects **and** the role-`bucket`
node, because a row can legitimately occupy it — RA-F2 sits at G8), Carrier
objects `C*`, plus the markers `UNTYPED` and `HOMONYM-AMBIGUOUS` read from
CT-1's own marker table.

**`UNTYPED` is legal** (CN-2) — always counted, always printed. One notch: an
`UNTYPED` slot requires a `note`.

**The never-launder interaction.** A `grant` projection that contradicts the
row's own stated conditions is a **red for adjudication, never a silent fix**:

- **L — LAUNDER-IN-PROJECTION:** `G0` (the empty assumption set) on a
  `DERIVED_CONDITIONAL` row. This performs, in the projection, exactly what the
  ledger forbids in the row.
- **O — GRANT-ROW DISAGREEMENT:** a non-empty node on a row whose `reason_kind`
  is exactly `DERIVED`; CT-1 defines `G0` *as* the `DERIVED` family.
- **M — GRANT-OMITS-NAMED-CONDITION:** the row's own text names a condition
  CT-1 assigns to a node, and the projection omits it. **This is the one place
  `UNTYPED` is not an escape**, and the line is principled: declared ambiguity
  is compliance about what is *genuinely* ambiguous, and a row that spells its
  own condition out is not ambiguous about it.

Rule M's markers are extracted from the braced names of CT-1's own Grant
objects — `{GRANT-ACA1-C1}`, `{INHERITANCE_BRIDGE}`, `{SC-CHI-01 …}`,
`{HYP-TW-COHERENCE-01 …}`. If CT-1 renames a node, the markers follow. If CT-1
ever yields **no** marker, the gate **reds** rather than passing silently.

---

## 3. The gate's scope proof

`process_gates/mint_context_projection_audit.py`, baseline 0, scope
`>= v0.260`.

**Direction 1 — v0.259 and everything earlier are untouched.** Live run on the
whole repository:

```
mint_context_projection_audit: 0 red (baseline 0); 0 ledger(s) in scope >= v0.260;
    259 out of scope BY CONSTRUCTION (non-retroactive)
mint_context_projection_audit[non-retroactive]: highest out-of-scope version v0.259;
    those rows are never required to carry `context` and none was edited to add one
mint_context_projection_audit[codomain]: layer/grant/carrier vs
    lab/methods/gu-base-categories.md: read (5/10/13 objects incl. markers;
    4 condition markers)
mint_context_projection_audit[census]: no in-scope ledger; context coverage is
    vacuously complete and proves nothing
```

The census refuses to congratulate itself on an empty scan — a vacuous 100%
is printed as vacuous. The probe additionally runs the gate against the real
`v0.259` alone and requires **green with 0 rows in scope** (CONTRARY control
P07): 87 rows, not one `context`, no red.

**Direction 2 — a synthetic v0.260 is enforced.** Built from the *real* v0.259
rows with `predecessor` pointing at the real file:

| synthetic ledger | what it does | required |
|---|---|---|
| v0.260 | changes nothing | **GREEN**, 0 touched — untouched rows never need context |
| v0.269 | adds a context to `AC-A1` and changes **nothing else** | **GREEN**, **0 touched**, 1 voluntary accretion — accretion is free, because the touched-comparison excludes `context` |
| v0.261 | touches `AC-A1`, no context | **RED** — "row AC-A1 is touched at v0.261 and carries no `context`" |
| v0.262 | touches `AC-A1` with its worked context | **GREEN**, 1 touched, 1 typed |
| v0.263 | `layer: L7` | **RED** — out-of-codomain |
| v0.264 | `grant: G0` on `AC-A1` (`DERIVED_CONDITIONAL`) | **RED** — LAUNDER-IN-PROJECTION |
| v0.265 | `grant: UNTYPED` on `LT-SM8` (names `INHERITANCE_BRIDGE`) | **RED** — GRANT-OMITS-NAMED-CONDITION |
| v0.266 | bare `UNTYPED` with no note | **RED** — a declaration is a sentence |
| v0.267 | all-UNTYPED **with** a note | **GREEN** and printed by row id — CONTRARY control |
| v0.268 | all three worked projections | **GREEN**, 3 touched, 3 typed, 4 UNTYPED slots, 3 notes |

Both directions are probe checks, not prose.

---

## 4. The three worked projections

Rows IM-1 actually touched at v0.259 (`rows_changed`: AC-A1 re-typed and
advanced conditionally; LT-SM8 re-typed strictly more indebting; LT-GR6b
appended as the corrected successor). Every justification below is read back
from the live row by the probe (checks W05–W14), never remembered.

### 4.1 `AC-A1` — fully typed, no ambiguity

```json
"context": { "layer": "L1", "grant": "G1", "carrier": "C5" }
```

- **`L1` (declared-total).** The row's grant is *"draft-literal Sec 9.3 full-`S`
  content, branch C1, **non-chiral in every form slot**"* — which is CT-1 L1
  verbatim: the unsubscripted arena, *"the total theory is explicitly
  non-chiral."*
- **`G1` ({GRANT-ACA1-C1}).** Forced by rule M: the row's own evidence names
  `GRANT-ACA1-C1`. `G0` here would be the launder, and the gate reds it —
  planted control P03.
- **`C5` (S-FULL-DIRAC).** "full-`S` content, non-chiral" is exactly CT-1's C5,
  the full 128-complex Dirac bundle. Not C6 (`S-HALF-OPPOSITE`): the grant says
  full, and reading it as a half would silently perform CT-1's non-arrow N1.

No `UNTYPED`, so no note is required — but one is written anyway, because notes
are always welcome.

### 4.2 `LT-SM8` — a union, a homonym marker, and an honest `UNTYPED`

```json
"context": { "layer": "UNTYPED", "grant": ["G5", "G7"],
             "carrier": "HOMONYM-AMBIGUOUS", "note": "…" }
```

- **`layer: UNTYPED` — the D2 trap, refused out loud.** The row says
  *"Pi4-to-**ambient** carrier adapter."* `ambient` is CT-1 **C1**, a
  *Carrier*-category LAYER stratum (D2 sense (a)). It is **not** a Source-Layer
  object, and writing `L1` because the row said "ambient" is precisely the D2
  error. The row's content is a repository/comparator construction over an
  adapted-connection algebra and names none of L1–L4. `UNTYPED` is the honest
  token.
- **`grant: ["G5","G7"]`.** G5 is *forced* by rule M — the row carries
  `named_condition.name: "INHERITANCE_BRIDGE"`. G7 is added *voluntarily*
  because CT-1 §2 records *"LT-SM8 sits at G5 ∪ G7"* while the G7 marker lives
  in the ledger's top-level `conditional_hypotheses`, not in the row text. This
  demonstrates the intended shape: **rule M is a floor, not a ceiling.**
- **`carrier: HOMONYM-AMBIGUOUS`.** The row writes `ad P` bare — a homonym
  seeded in the typed-carrier gate with no register entry (CT-1 D1) — and its
  own condition names **two** carriers: established for `Lambda^1 (x) ad P` at
  free level, *"not_established_for"* the RS/ker-Γ carrier and the interacting
  level. A row typing two carriers at once has not typed one.

### 4.3 `LT-GR6b` — an honest `UNTYPED` that is also a reported finding

```json
"context": { "layer": "UNTYPED", "grant": "UNTYPED", "carrier": "C2",
             "note": "…" }
```

- **`layer: UNTYPED`.** `L2` is the tempting wrong answer — the row is about
  the *"observed four-dimensional base"*, and `L2` is "the 4D one". But L2 is
  the **Weyl-pullback of one effective SM generation**, not 4D-ness. CT-1's L
  category types the source's *fermionic/spinor construction* layers, and most
  LAGRANGIAN-axis rows sit at none of them. Writing `L2` here is exactly the
  plausible-wrong-token failure this rule exists to expose; refusing it is the
  point of the exercise.
- **`grant: UNTYPED`, and reported.** The row's four debts state their
  conditions in-row with no shared name — which is the **shape** of CT-1's G8
  bucket. But CT-1 §2.1 defines G8 over *`DERIVED_CONDITIONAL` rows*, and
  LT-GR6b is `NEEDS`/`MISSING_CONSTRUCTION`. CT-1 also says *"NEEDS-side
  occupancy is polarity, not position"*, which pulls the other way. **That is a
  genuine tension in an object I do not own.** Declaring G8 would silently
  widen a CT-1 object — the thirteenth-object move CT-1 forbids. So: `UNTYPED`,
  with the tension named, and a finding filed to the Grant-poset owner (§6).
- **`carrier: C2` (observed).** The row's `summary` **and** its
  `revival_trigger` both locate it *"on the observed four-dimensional base"* —
  two independent in-row receipts.

**Coverage across the three:** one fully-typed row, one union, one homonym
marker, **four declared-unknown slots** (three `UNTYPED`, one
`HOMONYM-AMBIGUOUS` — CT-1 markers M1 and M4 are one class and share the
count, the note requirement and the no-mixing rule, exactly as FX-2's gate
counts them), three notes, zero all-UNTYPED rows. The
projection is fillable honestly, and filling it honestly produced two findings
that a plausible-token fill would have buried.

---

## 5. HOSTILE REVIEW — the plausible-wrong-token exposure, bluntly

**The strongest attack on this design succeeds, and I am not going to dress it
up.** Token ids are opaque and in-codomain by construction. A mint that writes
`L2` where `L1` is right, `C9` where `C8` is right, or `G3` where `G6` is
right, produces a projection this gate calls **green** — every time, with no
signal anywhere. Membership is checkable. Agreement with the row is partly
checkable. **Correctness is not checkable at all**, and no amount of further
gate work would change that, because the gate has no access to what the row
means.

What the design actually buys, stated at its true size:

1. **The dishonest cheap path is closed.** The projection a mint is *tempted*
   to write — the one that makes the program look better — is `G0`, and `G0` on
   a conditional row is a hard red. The direction of cheating that matters
   (claiming fewer assumptions) is blocked; per CT-1 §2.3 the opposite
   direction is the always-legal one anyway.
2. **A named condition cannot be evaded.** Rule M means the rows with the most
   at stake — the ones carrying a named grant — have their grant slot *partly
   forced* from their own text. This is the only genuine tooth against
   laziness, and it covers exactly 6 of v0.259's 87 rows. **Six.** That is the
   honest scope of the tooth.
3. **The lazy cheap path is visible, not blocked.** All-`UNTYPED` is legal,
   printed by row id, and every note is echoed verbatim in the census. A mint
   that types nothing has said so, on the record, in the run output. That is a
   *visibility* mechanism, not a verification one, and the note requirement is
   the same: it raises the cost of a blank from zero to one sentence and can be
   defeated by writing `"unknown"`. It would be.
4. **Opaque ids raise the guessing cost without making guessing detectable.**
   Writing `contraction` can be guessed from the English word; writing `L3`
   requires opening CT-1 §1.1. That is a real friction and a real *nudge toward
   reading the reference*, which is most of what this rule is for. It is not a
   check, and I am not counting it as one.

**Two limitations I found and did not paper over.** `SC-CHI-01` appears in no
v0.259 row's text and `HYP-TW-COHERENCE-01` lives in `conditional_hypotheses`
rather than in a row — so **G6 and G7 occupancy are not mechanically
checkable**, and rule M cannot force them. Both are pinned as predeclared-false
propositions in the probe so the limitation cannot silently become an assumed
capability.

**The one thing that would actually raise the ceiling** is not more gate logic:
it is that a projection written *while adjudicating the row* is written by
someone who just read the evidence, and a projection written in a sweep is not.
That is why the rule is accretive rather than retroactive, and it is a claim
about incentives, not a guarantee.

---

## 6. Findings reported, not fixed (CT-1's thirteenth-object rule)

Each belongs to a channel that owns the object; none is edited here.

| # | finding | owner |
|---|---|---|
| **F1** | **The v0.1 ledger schema has validated nothing since v0.1** — 14 errors on every ledger from v0.100, 21 on v0.259. v0.2 repairs this for itself; whether v0.1 should be deprecated is the ledger owner's call. | conditional-physics ledger |
| **F2** | **v0.1's row closure is closed in name only** — twelve accreted keys. v0.2 leaves rows open and records the vocabulary rather than silently re-imposing or silently blessing it. | conditional-physics ledger |
| **F3** | **`v0.134.json` declares `schema_version: 0.133`** (one file in 259). Handled defensively here (`max(filename, internal)`); the file itself is not touched. | conditional-physics ledger |
| **F4** | **CT-1's G8 bucket is defined over `DERIVED_CONDITIONAL` rows, but §2.2's polarity sentence suggests NEEDS-side rows can occupy nodes too.** LT-GR6b falls in the gap. Widening G8, adding a NEEDS-side bucket, or ruling the gap empty is the Grant-poset owner's decision. | CT-1 / Grant poset |
| **F5** | **G6 and G7 occupancy are not mechanically derivable from row text** (§5). If the ledger ever names `SC-CHI-01` in the rows it conditions, rule M covers them for free. | conditional-physics ledger |
| **F6** | **CT-1's Layer category has thin coverage of LAGRANGIAN-axis rows** — two of three worked rows are honestly `UNTYPED` on the layer slot. This may be correct (L types the source's spinor construction, not the variational structure) or may be a gap. | CT-1 |

---

## 7. POSTFLIGHT — seven verification lenses

**V1 — clean baseline first, both harnesses.** The gate's `--selftest` verifies
its clean fixture set exits 0 **before** any planted fact and prints
`clean baseline verified first`; `--poison-baseline` corrupts the clean set and
must print `planted facts were NOT run` and exit 1 (both asserted by the probe,
G02/G04). The probe's `--selftest` runs an unmutated subprocess first and
refuses to run mutations on a red baseline.

**V2 — mutations corrupt machinery, never checks.** All ten probe mutations
audited individually against VERIFICATION rule 2: `gate-gone`, `ref-gone`,
`schema-gone` (path corruption), `root-elsewhere` (the FX-3 path-bug lesson),
`ledger-glob-blind`, `synthetic-untouched`, `context-key-drift` (fixture/
machinery corruption), `version-pin-drift`, `pinned-codomain-drift`,
`marker-pin-drift` (reference-constant corruption). **None loosens a
predicate**; every one can only make the probe *redder or wronger*, never
greener.

**V3 — catches are genuine, not crashes.** Every mutation must exit 1 **and**
print `CERTIFICATE:` **and** contain a `  FAIL` line. A nonzero exit without a
certificate line is reported as `CRASH-NOT-DETECTION` and fails the selftest
(VERIFICATION rule 3).

**V4 — detector power on absence claims.** "v0.259 carries no context" and "the
live repo has 0 rows in scope" are absence claims; corrupting the detector
cannot flip them. So the probe plants five positives the detector is *required*
to flag (P01–P05) and two CONTRARY controls it is required **not** to flag
(P06–P07). The gate additionally plants a **toothless reference** — a CT-1 with
its braces stripped — and requires a red, proving the agreement rule cannot
quietly become a no-op (VERIFICATION rule 4).

**V5 — tolerances do not absorb controls.** Baseline is 0 in both harnesses and
the gate's selftest pins its own fixture baseline independently of the live
one. There is no tolerance wide enough to swallow a planted red because there
is no tolerance (VERIFICATION rule 6).

**V6 — nothing is remembered.** Every factual claim about a row, about CT-1, or
about the schema is read back from the file at run time: W05–W14 re-read AC-A1's
`reason_kind` and grant text, LT-SM8's `named_condition` and its bare `ad P`,
LT-GR6b's `summary`/`revival_trigger`/`reason_kind`, and CT-1's own G8
definition and `LT-SM8 sits at G5` sentence. C06 closes the codomain triangle
against CT-1's literal text.

**V7 — write scope and non-retroactivity re-checked at ship time.** Five paths
written, no others; `conditional-physics-ledger-schema-v0.1.json` unedited
(H03), `gu-base-categories.md` unedited, no ledger edited, no registry edited,
no git run. Live gate: 0 red, 0 in scope, 259 out of scope. Live typed-carrier
gate on the two new markdown files: 0 red.

---

## 8. Certificate

```
tests/channel-swings/joe_directed_ct2_mint_context_projection.py
  78/78 checks pass, exit 0
process_gates/mint_context_projection_audit.py --selftest
  clean baseline first, then 15/15 planted false facts each exit 1, exit 0
process_gates/mint_context_projection_audit.py --selftest --poison-baseline
  refusal path, exit 1
tests/channel-swings/joe_directed_ct2_mint_context_projection.py --selftest
  clean baseline first, then 10/10 machinery mutations each exit 1, exit 0
process_gates/mint_context_projection_audit.py   (live)
  0 red, 0 ledgers in scope, 259 out of scope by construction, exit 0
```

```gu-typed-objects
result: CT-2 -- the non-retroactive (layer, grant, carrier) context projection for mint-touched ledger rows
carrier: conditional-physics ledger row records at ledger version >= v0.260 LAYER=UNTYPED CHIRALITY=N/A
pairing: NONE
real_structure: N/A
grading: N/A
action_owner: repository-construction (CT-2 schema sibling, methods note and process gate)
target: the three base categories of lab/methods/gu-base-categories.md MAP-TYPE=not-a-map
```

`LAYER=UNTYPED` is the honest token, not an oversight: a ledger row *record* is
a repository process object and sits at none of the typed-carrier gate's four
strata. `MAP-TYPE=not-a-map` is likewise exact — a row *occupies* a node and is
not itself an object (CT-1 §2), so the projection is a labelling, not a functor.

---

## 9. What this stage does not supply

No physics claim, no verdict, no claim movement, no ledger edit, no canon edit,
no registry edit, no new category object, and no judgment of any row at v0.259
or earlier. It does not decide whether any projection is *correct* (§5 is blunt
about that), it does not resolve F1–F6, and it does not deprecate the v0.1
schema. It specifies a shape, states a rule where mints will read it, and
enforces existence, codomain membership and non-contradiction on rows that do
not yet exist.
