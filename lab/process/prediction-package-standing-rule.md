---
title: "Prediction Package Standing Rule"
status: active
doc_type: research_protocol
scope: repo-local
created: 2026-07-19
authorized_by: "Joe direct chat, 2026-07-19 (council-reviewed, five lenses)"
claim_status_change: none
---

# Prediction Package Standing Rule

When a potential prediction can be packaged, packaging it becomes the top
priority for regular hourly progress — ahead of Lane 1/2/3 ranking — until
the package freezes or hits a named blocker. Then work returns to normal.
Rationale (council): prediction value decays with time — data arrives and
post-hoc suspicion grows — so the interrupt is epistemically justified, not
arbitrary. The git commit is the notary: a frozen, timestamped package with
enumerated conditions is what makes "they predicted it, and said why" an
unarguable record.

## Admission criteria (what counts as packageable)

A candidate must have, or be one bounded computation away from having:

1. a derivable observable with a stated sign/value/window;
2. an enumerable condition chain (which channel cards / assumptions it is
   conditional on — conditional packages are admissible and welcome);
3. a kill threshold (what measured outcome falsifies it);
4. NOT a retrodiction. Retrodictions are logged as coherence and are never
   packaged, without exception.

"Potential prediction" without these is a candidate for Lane 2 shaping, not
a package interrupt.

## Interrupt semantics

- The daily steward (Lane A) flags `PREDICTION_PACKAGE_PENDING` on the
  portfolio when an admissible candidate exists unfrozen.
- The next Progress hourly takes the package work regardless of normal
  cross-lane ranking, and continues until FROZEN or a named blocker.
- Time-box: if the package cannot freeze within ~3 progress cycles, it
  returns to the normal queue with its gap named as a work item — no
  starving Lane 1 on a hard packet.
- Every channel swing and probe adds a closing checklist line: "did this
  create a packageable prediction?" — detection is structural, not steward
  luck.

## The freeze

A frozen package states: predeclared observable and convention; the
prediction; the full condition chain; competitor baseline; kill
threshold(s); brackets quoted from already-frozen rows only, after the
freeze; grade (CONDITIONAL where conditional, plainly). Frozen packages are
committed immediately — the commit timestamp is the pre-registration
record. Nothing external moves (Joe alone ever takes anything outside).

## Versioning and supersession

- Small refinement: same file, `version:` field bumped, changelog entry.
- Material change of claim: new version file (v2) with a `supersedes:`
  pointer; the old package is NEVER deleted or edited beyond a
  superseded-by header. The v2 MUST state why v1 is now believed wrong:
  new derivation, new data, or found error. The changelog is science, not
  bookkeeping.
- A superseded package remains part of the public record of the program's
  honesty; being seen to update is worth more than being right first.

## Registration (adopted 2026-07-20, Joe direct chat; council-reviewed same day; routing revised same day)

Prediction packets become PREDICTION PAPERS — a paper TYPE, not a new
lane or channel anywhere. They flow through the Drafting Factory's
normal pipeline like every other paper, with exactly one routing rule
(Joe-set, trial): **prediction papers take priority over every other
paper type in the factory queue.** Everything posts as soon as it is
ready; Joe alone posts. The factory sends carding/hardening feedback to
the source repo's mailbox, and the repo routes it to the proper lane —
prediction-side hardening to Lane 2, paper-side hardening to Lane 3.
(The underlying realization: GU's Lane 2 and Lane 3 both ultimately
produce papers — different TYPES of paper, one queue downstream.)

Registration mechanics for the prediction-paper type:

1. **Mechanism:** attempt arXiv when frictionless for the submitter; any
   gate or delay (endorsement, moderation) -> register on Zenodo the
   same day; arXiv re-post later is an optional upgrade, never a
   blocker. The external DOI/timestamp is the second notary on top of
   the git commit.
2. **Same-frozen-text rider:** what is registered is the frozen packet
   note verbatim in substance — never an abridgement (an abridged
   registration invites "the details came later").
3. **Chain of custody rider:** any later posting (arXiv, journal) cites
   the original registration DOI as the timestamp of record.
4. **POSTING is the freeze (Joe, 2026-07-20).** Two notaries freeze
   different things: git freezes WHAT WAS KNOWN WHEN (fine-grained, the
   record of the small steps); the public posting freezes WHAT IS
   STAKED (the severity object). Before posting, a packet MAY be
   revised to incorporate new findings — post the best available
   prediction — under three riders:
   - **Data-blindness guard:** pre-posting revisions must be
     derivation-driven, never data-driven. The moment a
     scoring-relevant dataset becomes public, the pending version
     auto-freezes: only the last PRE-release commit may post as
     "pre-registered" against that release (commit timestamps vs
     release dates adjudicate mechanically).
   - **Revision log:** the posted note states internally-frozen /
     revised / posted dates; band-WIDENING revisions carry a stated
     derivation reason (tightening needs none).
   - **Event-driven cadence:** posting is timed to beat data epochs,
     not to chase version numbers; the ~2-day READY escalation guards
     against improvement becoming procrastination.
   AFTER posting, supersession = a WHOLLY NEW registered prediction
   citing its predecessor; posted predecessors are never withdrawn or
   edited. The public chain of superseded registrations is the intended
   artifact — "this is what we learned next"; open research over the
   appearance of infallibility. Version-DOIs only for material
   post-posting supersessions.
5. **Per-registration release approval stays with Joe — via EXISTING
   attention rails, no parallel mechanism.** Each registration is an
   external action requiring Joe's explicit per-action GO on the
   specific artifact + venue. The Drafting Factory's papers channel
   manages what is REGISTRATION-READY; if a time-sensitive ready item
   sits unreleased more than ~2 days, the factory escalates through the
   standard routing (system mailbox / JoeOps) and may flag it on its
   LANE-STATE summary surface. Agents prepare and surface; Joe releases.
6. **Backfill:** already-frozen packets without external timestamps
   (PP1, PP2) are standing registration candidates under the same
   mechanism, each awaiting its own per-action GO.
7. **Title demarcation principle (Joe, 2026-07-20):** the program name
   goes in a prediction paper's TITLE iff the prediction's derivation
   locus sits in the program's construction; if the program is only the
   motivation/driver, it goes in the body. Title = locus of derivation;
   body = context of motivation. (PP3 precedent: GU in the title —
   theta-sector realization, M^2 root-system band, S2 reads the root
   system.)
8. **Stopping rule (Joe-adopted, council-proposed, 2026-07-20) — when
   to stop waiting for new learnings and ship.** "More learnings are
   coming" is always true and therefore never a reason; the rule is
   pre-declared so stopping cannot become motivated (waiting when weak,
   rushing when strong = publication bias in time). Two dimensions,
   both required: SIGNIFICANCE (external — a named audience would act
   differently) and MATURITY (internal — stopped changing under
   attack).
   - PREDICTIONS: event-driven, period. Ship before the next
     scoring-relevant data epoch; the data-blindness auto-freeze is the
     hard backstop; improvement-waiting is legal only inside the epoch
     window; the ~2-day READY escalation polices drift.
   - PAPERS (three tests, all must pass): (i) CITABLE UNIT — a result
     someone could build on or be wrong because of, as it stands;
     (ii) TWO DRY ROUNDS — consecutive adversarial/verification passes
     with no material revision (the loop-until-dry instrument pointed
     at publication); (iii) NAMED-BLOCKER-OR-SHIP — any hold must name
     the specific pending learning, the conclusion it could flip, and
     an ETA; unnamed waiting is an automatic ship signal.
   - Significant-but-unstable ships as a registered prediction or
     flagged conjecture, never as a paper; stable-but-insignificant
     stays in the repo awaiting a paper it can join. Tests are
     evaluated by a council/steward pass, not by enthusiasm.

## Current shelf (at rule adoption)

- PP1 (frozen 2026-07-19): dark-energy sign — w0+1 > 0, w(z) >= -1
  pointwise; conditional chain per blockbuster-p1 doc; kills named.
- Candidate packet 2: matter-parity stable state (126 route) — Lane 2 work.
- Candidate packet 3: mirror-sector charged vectorlike replica — gated on
  weld probes W-A/W-B; possible mu-finite upgrade via the causality
  theorem.
- Standing tripwire: DE-F1 ceiling (predates the rule; grandfathered as a
  frozen row).
