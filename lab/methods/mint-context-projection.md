---
title: "The mint context projection: every row a mint touches carries its (layer, grant, carrier)"
status: active_reference
doc_type: mint_projection_rule
created: 2026-08-17
work_item: CT-2
schema: lab/process/conditional-physics-ledger-schema-v0.2.json
audit: process_gates/mint_context_projection_audit.py
probe: tests/channel-swings/joe_directed_ct2_mint_context_projection.py
codomain_owner: lab/methods/gu-base-categories.md
design_record: lab/active-research/joe-directed/ct-hardening/ct2-mint-context-projection-2026-08-17.md
---

# The mint context projection — what a mint owes on every row it touches

**Read this before minting a ledger version.** It states one rule, its three
codomains, the one way to comply when you do not know, and the one way the
rule can fail you loudly.

---

## 1. The rule

> **From ledger version v0.260 onward, every row whose content a mint changes
> — and every row a mint appends — carries a `context` object giving that
> row's `(layer, grant, carrier)` projection into the three base categories of
> `lab/methods/gu-base-categories.md`.**

Three properties of that sentence are the whole design, and each was chosen
against a named failure:

**Non-retroactive.** `v0.259` and everything before it are out of scope *by
construction*, not by tolerance. No existing row is edited, no sweep is run,
no baseline is set that a later agent could quietly raise. The ledger series
is append-only and immutable per version, so the scope boundary can never move
backward: `v0.259` will still be `v0.259` in a year. This is FX-2's
non-retroactive cutoff (`created: >= 2026-08-17`) transposed from dates to
version numbers, and it is why nothing in this repository goes red the day the
rule lands.

**Accretive.** Context is written *exactly when someone is already
adjudicating the row* — a mint has the row open, has read its evidence, and
has just decided what it means. That is the only moment the projection is
cheap and the only moment it is trustworthy. A retroactive typing pass would
be neither: it would be a stranger guessing at 84 rows in one sitting, which
is the plausible-wrong-token failure mode industrialised. Untouched rows may
*volunteer* a context and the gate accepts it; nothing demands it.

**Row-scoped, not mint-scoped.** The obligation attaches to the row the mint
touched, not to the mint. A mint that changes one row owes one projection.

### What counts as "touched"

A row is touched at version *V* if it is **absent** from *V*'s `predecessor`,
or if its content **differs** from the predecessor's row of the same `id`.
Content comparison excludes the `context` key itself, so that adding context
to an otherwise-unchanged row is not itself a content change — that is what
makes voluntary accretion free.

If the predecessor cannot be resolved, **every row counts as touched.** The
rule fails closed: an unresolvable base is a reason to type more, not less.

---

## 2. The codomains — all three owned by CT-1, none owned here

| slot | codomain | owner |
|---|---|---|
| `layer` | Source-Layer object ids `L1`..`Ln`, or `UNTYPED` | `lab/methods/gu-base-categories.md` §1.1 |
| `grant` | Grant-poset node ids `G0`..`Gn` (including the role-`bucket` node), or `UNTYPED` | same file §2.1 |
| `carrier` | Carrier object ids `C1`..`Cn`, or `UNTYPED`, or `HOMONYM-AMBIGUOUS` | same file §3.1, §3.2 |

**This file coins nothing.** It names no object, adds no object, and cannot
be used to justify one. The gate reads the three codomains *out of CT-1's
tables on every run* and fails closed if that file is missing, if any codomain
is empty, or if either required marker (`UNTYPED`, `HOMONYM-AMBIGUOUS`) has
left CT-1's marker table — the same wiring, in the same direction, that the
typed-carrier gate uses for `LAYER=` and `MAP-TYPE=`. If your row demands an
object no codomain carries, **that is a finding to report to the owning
channel with receipts, not a token to invent** (CT-1's thirteenth-object
rule). Write `UNTYPED`, say so in the note, and report it.

### The `layer` naming trap — read this before filling the slot

Three different axes in this repository share the word "layer" (CT-1 §4, D2).
The `layer` slot means **the source-construction layers**: declared-total,
pullback, ±package, VEV-observed. It does **not** mean the typed-carrier
gate's `LAYER=` stratum axis (`ambient` / `observed` / `source-print` /
`toy`) — those are *Carrier* objects and belong in the `carrier` slot. A row
that says "ambient" and gets `layer: L1` for it has made the D2 error and the
gate cannot see it.

### Cardinality

Each slot takes one token **or** a non-empty array of distinct tokens meaning
the union. Unions are not a hedge; they are the recorded truth for rows that
occupy several nodes at once — CT-1 §2 states the exemplar verbatim: *"A row
carrying several conditions occupies the union of their sets (LT-SM8 sits at
G5 ∪ G7)."* `UNTYPED` may not be mixed with objects in one slot: a slot that
names an object and also declares ignorance says nothing.

---

## 3. `UNTYPED` is legal — this is load-bearing, not a loophole

**A row complies by declaring its ambiguity.** This is CN-2's principle, and
the typed-carrier gate already runs on it: `UNTYPED` is always legal, always
counted, printed every run. Making honesty red trains plausible-token lying,
which is strictly worse than a declared gap, because a declared gap is visible
to the next reader and a plausible wrong token is not.

Two consequences, both deliberate:

1. **An all-`UNTYPED` context is green.** It is also printed by row id in
   every census run, so a mint that types nothing has said so on the record.
2. **`UNTYPED` requires a `note`.** The note says why the ambiguity is real.
   This is the one place this file asks for more than FX-2 does, and the
   reason is narrow: a bare `UNTYPED` is a blank, and a *declaration* of
   ambiguity is a sentence. The gate checks the note exists and prints it
   verbatim; it cannot check that it is true, and claims no such power.

`HOMONYM-AMBIGUOUS` on the carrier slot is the same kind of honest token for
the registered-homonym class. A bare registered token (`so(1,3)`, `ad(P_H)`)
fails to name an object (CT-1 §3.5); a row that writes one has not typed its
carrier, however confident its prose reads, and `HOMONYM-AMBIGUOUS` is how it
says so.

---

## 4. The never-launder interaction — a grant projection must agree with the row

The ledger's standing law is that **a row's position may move only along a
recorded migration arrow, never silently toward the top** (CT-1 §2.3;
`v0.259` `migration_policy`: *"DERIVED_CONDITIONAL → DERIVED is forbidden;
every status move records its grant"*). The projection opens a second surface
on which that law could be broken — so the same law binds it.

**A `grant` projection that contradicts the row's own stated conditions is a
red.** The gate checks three mechanical forms of contradiction:

| # | contradiction | why it is a red |
|---|---|---|
| **L** | `grant` includes `G0` on a row whose `reason_kind` is `DERIVED_CONDITIONAL` | `G0` is the *empty assumption set*. Writing it on a conditional row performs, in the projection, exactly the launder the ledger forbids in the row. **This is the launder in projection form.** |
| **O** | `grant` names a non-empty node on a row whose `reason_kind` is exactly `DERIVED` | CT-1 defines `G0` *as* the `DERIVED` family. Over-claiming a condition is the safe direction to *move*, but it is still a disagreement to *describe*. |
| **M** | the row's own text names a condition that CT-1 assigns to a node, and `grant` omits that node | The row already told you its grant. Omitting it — including by writing `UNTYPED` — is not ambiguity; it is contradiction of the row by its own projection. |

The condition markers behind rule **M** are not invented here: the gate
extracts them from the braced names of CT-1's own Grant-poset objects
(`{GRANT-ACA1-C1}`, `{INHERITANCE_BRIDGE}`, `{SC-CHI-01 …}`,
`{HYP-TW-COHERENCE-01 …}`) and scans the row's text for them. If CT-1 renames
a node, the marker set follows. If CT-1 ever carries *no* extractable marker,
the gate **reds rather than passing silently** — a rule that has quietly lost
its teeth must not read as green.

**Rule M is the one place `UNTYPED` is not an escape**, and that is the
principled line: declared ambiguity is compliance *about what is genuinely
ambiguous*, and a row that spells its own condition out in its own fields is
not ambiguous about it.

### What the gate does NOT do on a disagreement

It does not fix either side. It does not re-type the row, it does not adjust
the projection, and it does not decide which of the two is wrong. It reds,
names both sides, and stops — because a projection/row disagreement is
evidence that somebody's understanding of the row is wrong, and finding out
whose is adjudication, which belongs to the row's canonical owner.

---

## 5. Worked shape

```json
"context": {
  "layer": "L1",
  "grant": "G1",
  "carrier": "C5",
  "note": "eq (9.16) full unsubscripted S, non-chiral in every form slot: the declared total (L1) read as the full Dirac bundle (C5), advancing under the declared grant GRANT-ACA1-C1 (G1)."
}
```

Three worked projections for real rows — including two honest `UNTYPED`s and
the reasoning that refused a plausible-looking token in each case — are in the
design record: `lab/active-research/joe-directed/ct-hardening/ct2-mint-context-projection-2026-08-17.md` §4.

---

## 6. What this rule does not supply

It does not type any existing row, move any row, change any verdict, add any
object to any category, or make any physics claim. It does not decide whether
a row's projection is *correct* — no gate can, and §4 of the design record is
blunt about exactly which errors survive this instrument. It enforces that the
projection **exists**, is **in codomain**, and does **not contradict the row it
describes**. Everything past that is review by a reader, which is what the
census exists to make possible.
