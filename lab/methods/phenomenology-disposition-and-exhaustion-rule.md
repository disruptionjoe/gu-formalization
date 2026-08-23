---
title: "Phenomenology disposition and the exhaustion rule: four buckets, and do not return to the source action until the other three are empty"
status: active_method
doc_type: mandatory_work_selection_scheme
created: "2026-08-23"
directed_by: "Joe direct chat, 2026-08-23"
registry: lab/process/phenomenology-disposition-and-exhaustion-rule.json
probe: tests/channel-swings/phenomenology_disposition_probe.py
companion: lab/methods/fitting-construction-grade.md
---

# Phenomenology disposition and the exhaustion rule

## The frame

Two things are known and neither depends on the source action: **the actual
phenomenology**, and **where current physical theory is itself in tension**.
The conditional-physics ledger is the inventory of the first. This method says
what to do with each entry.

Every piece of known phenomenology in the ledger disposes into exactly one of
four buckets. Three of them are workable now. One is deferred, and the whole
point of the scheme is that it stays deferred.

## The four buckets

**B1 — FITS.** The conditional build accommodates it. The construction exists
at its rung, conflicts with nothing recorded, and carries a route. This is
banked at `FITTING_CONSTRUCTION` grade under
`lab/methods/fitting-construction-grade.md`. **This bucket is the goal and the
work is to grow it.**

**B2 — SOURCE-ACTION-DEFERRED.** It does not fit as built, and what it would
take is the source action or an external datum. **Do not work these now.** Log
the row, log precisely what would be needed, and move on. The accumulated
contents of B2 *are* the R1 specification, assembled for free as a by-product
of working the other three buckets.

**B3 — PHYSICS-SIDE TENSION.** The apparent misfit may not be GU's. Current
theory has open tensions, and measurements carry model dependence, assumed
priors, and analysis choices. A row belongs here when the thing GU is being
asked to reproduce is itself contested, derived under assumptions GU need not
share, or measured through a pipeline whose assumptions are visible. The work
is to **document the external tension precisely**, at its own grade, and
restate what GU is actually obliged to reproduce once the contested part is
separated out. This is not special pleading: it is refusing to hold a
conjecture to a standard the incumbent theory does not itself meet, and it
must be sourced to the external literature like any other comparator.

**B4 — SOURCE DERIVES IT DIFFERENTLY.** The source material shows a different
route to the same phenomenon, so the apparent misfit is an artifact of testing
GU against a construction it never proposed. The repository already
instruments this for four recurring cases in
`lab/methods/source-native-comparator-routing.md`; this bucket generalizes it.
The work is to identify the source-native route and build *that*, not the
comparator.

## The exhaustion rule (binding on work selection)

> **Do not return to R1 (the source action) or to external-datum construction
> until B1, B3 and B4 are exhausted.**

A lane may not select source-action work while any B1, B3 or B4 item remains
unattempted. "Exhausted" means every such item has been attempted and has
either produced a `FITTING_CONSTRUCTION`, produced a precise impossibility, or
been re-disposed into B2 with its requirement named.

Two reasons this ordering is not arbitrary:

1. **B2 gets cheaper by waiting.** Every B1 construction narrows what the
   source action must do, because a fitting construction at a rung fixes that
   rung's interface. The R1 problem attacked after B1/B3/B4 are exhausted is a
   strictly smaller problem than the same one attacked today, and it arrives
   with its specification already written.
2. **B2 is the only bucket that can absorb unlimited effort with no result.**
   The recorded corpus contains roughly thirty CBRS-1 candidate closes, all
   owner-exhausted. Returning to R1 early is the failure mode this rule exists
   to prevent, and it has already consumed more of this program than any other
   activity.

## Disposition discipline

- **One bucket per row.** A row that seems to be in two is under-analysed;
  split the claim until each part has one bucket.
- **B2 requires a named requirement.** "Needs the source action" is not a
  disposition. Name the object: which owner, which coefficient, which datum.
  Un-named B2 entries are the blockage restated, which
  `FC-5` already forbids.
- **B3 requires an external citation.** A tension asserted without a published
  source is not a tension; it is an excuse. Cite it, scope it, and state what
  GU still owes once the contested part is removed.
- **B4 requires the source locus.** Name the registered claim (`SC-` id) or the
  primary-source passage showing the different route. Without it this bucket
  becomes a way to dismiss any inconvenient comparator.
- **Disposition is revisable.** New evidence moves a row between buckets. A
  B3 tension that resolves against GU moves to B1-or-B2; a B4 route that turns
  out not to be in the source moves back.

## What this scheme is not

It is not a way to score the program well. B1 membership earns no prediction
credit, moves no ledger row toward `SAME`, and is explicitly barred from being
cited as derivation. B3 does not excuse GU from anything; it relocates the
obligation and documents it. B4 does not make a comparator failure disappear;
it says the failure bound a model the source did not propose, which is already
the repository's recorded routing discipline.

The scheme's only claim is that there is a large amount of legitimate work
available that does not require the source action, that the program has been
skipping it to return to R1, and that doing it first makes R1 tractable rather
than deferring it forever.
