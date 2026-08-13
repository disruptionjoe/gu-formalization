---
artifact_type: council
created: 2026-08-08
subject: "How to proceed given that the conditional build depends on the author's framing"
verdict: DEPENDENCY_IS_CORRECT__ITS_SILENCE_IS_THE_DEFECT__THREE_ACTIONS
council: science
---

# Science council: the conditional build depends on Eric's framing

**Measured first:**

```text
conditional-physics ledger, current      v0.97 (file title still says v0.96)
ledger versions on disk                     97
rows mapped                              82/82 (100%)
OVER-DETERMINED rows                         5
open forks named in the ledger               9
standing statement of WHAT it is
  conditional on                             0   <-- none
```

**A ledger whose name is "conditional" does not say what it is conditional on.**
Searching it for "conditional on", "rests on", "assumes" or "horn" returns
nothing; the only `K77`/`(7,7)` occurrences are file paths in a citation list.

The chain it stands on, made explicit here for the first time:

```text
base (1,3)        AUTHOR-STATED, twice, in Weinstein's own voice.
                  Not derived. Evidence about the author.
fibre (6,4)       Selected by the Pati-Salam criterion -- which WORKS
                  (tests/pati_salam_selects_the_fibre_trace_sign.py) but is
                  an EXTERNAL physical target, not forced by GU's action.
ambient (7,7)     Follows arithmetically. Draft eq (12.19) prints it.
```

---

## C-1 Epistemologist

The word "conditional" is doing real work in the program's own title, and that
is honest. But **a conditional with no named antecedent is not a hedge, it is a
mood.** The fix is not architectural: it is one standing block naming the two
imported inputs and what happens if either fails. **Verdict: declare, don't
restructure.**

## C-2 Mission seat — the reframe that matters

This repository is `gu-FORMALIZATION`. **Formalizing the author's framing is the
job.** Depending on Weinstein's `(1,3)` is correct behaviour for a formalization
programme, and would only be a defect in an independent-derivation programme.

So the dependency is **not** the problem. **The silence about it is.** A reader
of the ledger cannot currently tell which rows would survive a horn flip, and
that is what makes the dependency feel dangerous rather than declared.

## C-3 Risk / blast radius

The repository already knows how to do this — it just hasn't done it for the
ledger. Results are **already** typed elsewhere as signature-robust (`F ≃ RP³`,
the `(832,832)` trace, the rational-triviality lemma) versus horn-specific (the
Krein / right-`H` machinery, the carrier). **The 82 ledger rows carry no such
tag.** Adding it converts an unknown blast radius into a known one, and it is
the single action that makes a flip survivable rather than catastrophic.

## C-4 Hostile reviewer

**The failure mode is not dependency, it is UNDECLARED dependency**, and there is
a worked instance from today: `M-H17`'s BV complex is built on `Cl(9,5)`, the
demoted horn, and **zero artifacts recorded that dependency** until 2026-08-08.
The ledger is the same disease at larger scale.

Secondary smell, recorded not diagnosed: **97 ledger versions, and the current
file's own title is a version behind.** When a versioning ritual outruns its
meaning it stops being provenance and becomes noise.

## C-5 Prior art

**The hedge already exists and was built deliberately.** Wave K demoted `(9,5)`
to a *conditional comparator and negative-test bank*, kept it rather than
deleting it, and imposed an explicit **import ban** (do not carry `(9,5)`
right-`H`/chosen-`J` machinery into `Cl(7,7)`). That is exactly the two-branch
structure a fork-dependent programme should have. **The architecture is sound;
the question is maintenance, not design.**

## C-6 Decision theory

If the horn flips, work typed **branch-native** converts to comparator rather
than being wasted — **provided the import ban was respected.** That ban is
therefore the actual insurance policy, and **nobody has audited whether it has
held.** An unaudited ban is an assumption.

---

## Recommendation — three actions, none of them a restructure

1. **One standing conditionality block** at the head of the ledger and its JSON,
   naming the two imported inputs (author-stated base `(1,3)`; external
   Pati-Salam target) and the consequence if either fails. **Cheapest, and it
   retires the "conditional on what?" question permanently.**
2. **Tag the 82 rows horn-robust vs horn-specific.** This *is* the blast radius.
   Until it exists, "what breaks if the horn flips" has no answer, and that
   unknown is what makes the dependency feel like exposure.
3. **Audit the import ban.** Has `(9,5)` machinery leaked into K77 work? The ban
   is the insurance and it has never been checked.

**Explicitly NOT recommended: stop building on `(7,7)`.** It is the
author-aligned branch, formalization is the mission, and Wave K's `measured_cost`
records what stacking on an under-examined horn costs — but the remedy it points
to is *declaring and typing* the dependency, not refusing to build.

**Unresolved and named:** the base `(1,3)` still has no derivation, only the
author's assertion. Today's work pinned the *fibre* with a working criterion and
`tests/base_sign_is_invisible_to_the_isometry_group.py` showed that any base
resolver must reach the Clifford/spinor layer — group-theoretic and
metric-geometric criteria are excluded wholesale. That narrows the search; it
does not close it.
