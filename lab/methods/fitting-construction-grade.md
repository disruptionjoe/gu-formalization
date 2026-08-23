---
title: "The FITTING CONSTRUCTION grade: how conditional-build reverse scaffolding banks its own output"
status: active_method
doc_type: mandatory_claim_grade_and_admission_standard
created: "2026-08-23"
directed_by: "Joe direct chat, 2026-08-23"
registry: lab/process/fitting-construction-grade.json
probe: tests/channel-swings/fitting_construction_grade_probe.py
---

# The FITTING CONSTRUCTION grade

## The defect this fixes

The program's claim ladder runs source-confirmed, repository-derived,
reconstructed, conditional, speculative, negative, open. Every rung above
`speculative` requires a derivation. `conditional` is the closest fit and it
still means *derived, given grant G* — a strictly stronger claim than what
conditional-build reverse scaffolding produces.

So the method's actual output has had **nowhere to be filed**. The observable
consequence is recorded throughout the repository: constructions terminate in
`BLOCKED_WITH_NAMED_GAP`, "waits on the source action," "requires OWNER-A." A
structure that was successfully built at its rung, that conflicts with nothing
recorded, and that has a clear route to derivation gets discarded as a
blockage, because the only alternative was to overclaim it as derived.

**That is backwards.** The point of reverse scaffolding is to find structures
that *would fit* the theory and *do not conflict* with it. Full derivation
without the source action is not the bar; a clear and plausible pathway is.
This grade gives that output a home, with a standard sharp enough that it
cannot become a laundering channel.

## The grade

> **FITTING CONSTRUCTION (`FITTING_CONSTRUCTION`).** A structure explicitly
> built at a named descent rung, which conflicts with no recorded repository
> result and no registered source claim, and which carries an explicit named
> pathway to derivation together with the conditions that would falsify that
> pathway.

It sits **below** `conditional` and **above** `speculative`. It is not a
derivation, not a prediction, and not evidence that GU is correct. It is a
statement that a specific object is available, consistent, and reachable.

## Admission criteria — all seven, or it is not a FITTING CONSTRUCTION

**FC-1 BUILT, NOT GESTURED.** The object is actually constructed and its
structure fingerprint is stated in full: carrier, pairing or form, real
structure, grading, signature horn, ambient embedding. A description of what
such an object would look like is `speculative`, not this grade.
(`PD-STRUCTURE-TRANSPORT` binds: if any fingerprint field changes relative to
a result being reused, an adapter must be constructed or the claim returns
`OBJECT_CHANGED`.)

**FC-2 RUNG NAMED.** The descent rung (R6…R1) the construction lives at, and
therefore what it is conditional *on* from below and what it supplies *above*.

**FC-3 NON-CONFLICTING, CHECKED.** The construction is checked against the
recorded corpus and conflicts with nothing. The artifact must **name what it
was checked against** — the relevant no-gos, kills, path-dependency chains and
prior closes. "No conflict found" without a stated search is not a check.

**FC-4 SOURCE-COMPATIBLE, CHECKED.** Checked against
`lab/sources/source-claim-register.yaml` with polarity respected: violating a
claim the source `ASSERTS` is a conflict, and so is *relying on* a reading the
source `DISAVOWS`. Name the SC- ids checked.

**FC-5 PATHWAY NAMED.** An explicit route from the construction to a
derivation: what must be supplied, **which owner supplies it** (source action,
observation map, external datum, or a named construction), and what the next
executable step on that route is. A pathway that reduces to "the source action
must exist" is not a pathway — it is the blockage this grade exists to stop
restating.

**FC-6 CEILING AND DEMOTION STATED.** The artifact states that the
construction is not a derivation and may not be cited as one, and states the
condition under which it **demotes**: if the pathway is later shown blocked,
or a conflict surfaces, the construction drops to `speculative` or `negative`
rather than silently persisting at this grade.

**FC-7 NONTRIVIALITY WITNESS — states something it forbids.** The construction
must name at least one thing it rules out: an excluded value, an excluded
structure, or an observable whose measurement would falsify it. A construction
that forbids nothing constrains nothing and is not admitted.

*Why this criterion exists.* FC-1 through FC-6 all test whether a construction
is CONSISTENT — built, non-conflicting, source-compatible, routed, ceilinged.
None of them tests whether it is CONTENTFUL. A sufficiently weak object passes
all six trivially, precisely because it conflicts with nothing by virtue of
saying nothing. FC-7 is the criterion that separates a research instrument from
a laundering channel, and it was added on the day the grade was installed, by
the process council's seat 5, before anything had been banked at the grade.

## What this grade explicitly does not license

- **Compatibility as derivation.** `RESEARCH-POSTURE.md` lists this among the
  forbidden moves and this grade does not relax it. A FITTING CONSTRUCTION is
  compatible by construction; that is its content and also its ceiling.
- **Prediction credit.** No FITTING CONSTRUCTION earns prediction or
  confirmation credit, and none may be used to move a conditional-physics
  ledger row toward `SAME`.
- **Ledger movement.** The grade lives in the research corpus, not the ledger.
  It may inform a row's `distance` or `evidence` by ordinary evidence-delta
  process; it never by itself changes a verdict.
- **Target fitting.** Every choice must be frozen before evaluation against a
  target, inheriting the CBRS owner-before-evaluation discipline.

## Why this is not a laundering channel

The failure mode to guard is a channel that banks unearned work by calling it
"fitting." Five features prevent it. FC-1 requires an actual object with a full
fingerprint, which is expensive and checkable. FC-3 and FC-4 require *named*
searches against the corpus and the source register, so an unchecked claim is
visibly unchecked. FC-5 forbids the degenerate pathway — the one that says the
source action must exist — which is exactly the restatement that has been
passing as an answer. FC-6 makes the grade revocable, so a construction whose
pathway closes does not sit at grade forever. And FC-7 refuses an object that
is consistent only because it is contentless.

The grade also **cannot inflate the ledger**, because it is barred from moving
a row toward `SAME` and from earning prediction credit. Its whole value is
that the program stops throwing away structures it has legitimately built.

## Relationship to the descent

Reverse scaffolding descends R6 → R5 → R4 → R3 and hands R2/R1 a demand
interface. A FITTING CONSTRUCTION is what a descent rung produces when it
succeeds: an object at that rung, consistent, with the route stated. The
accumulated set of fitting constructions across rungs is the conditional build
— and a conditional build whose rungs are all FITTING CONSTRUCTIONS, with the
pathways composing, is precisely "a clear and plausible pathway" for the whole
theory, held at honest grade without anyone claiming derivation.

That is the object the program is actually trying to produce. It now has a
name and an admission standard.
