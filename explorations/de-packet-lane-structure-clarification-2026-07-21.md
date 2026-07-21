---
title: "Clarification: where the dark-energy prediction packet lives, redundancy-vs-seam between GU Lane 2 and the Drafting Factory, and why nothing looks post-ready"
status: clarification
doc_type: exploration
created: 2026-07-21
directed_by: "Joe direct chat, 2026-07-21 (scout-and-clarify the DE packet / drafting-factory / lane structure)"
scope: read_only_scout
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
external_actions: github_versioning_only
inputs:
  - lab/process/prediction-package-standing-rule.md
  - lab/process/research-portfolio.json
  - explorations/blockbuster-p1-de-sign-covariance-2026-07-19.md
  - explorations/prediction-package-pp3-de-curve-family-2026-07-20.md
  - explorations/b5-middle-source-freeze-2026-07-21.md
  - explorations/anomaly-inflow-swing-2026-07-21.md
  - explorations/pin-bordism-cardinality-2026-07-21.md
  - lab/sources/claim-mining-toe-weinstein-2026-07-20.md
  - "drafting-factory: production/pp3-preregistration-note/{README,COVER-NOTE-FOR-JOE,DECISIONS,draft-pp3-preregistration-note-v0.1}.md"
  - "drafting-factory: PAPER-SEEDS.md, LANE-STATE.yaml"
---

# Clarification: the DE packet, the seam, and why nothing reads "post-ready"

Read-only scout across gu-formalization (GU) and drafting-factory (DF). No file
edited but this one; no commit, no push, no external action.

## TL;DR

There is **no redundancy** — it is a **clean seam**. GU owns the science-freeze
(condition chains, kill thresholds, native-vs-forced grade); DF owns turning a
frozen packet into a staged paper; Joe owns exactly one gate: the posting
itself. There are **two frozen DE packets** (PP1 = the *sign*, PP3 = the
*curve/shape*), both GU-side; the one that has been *drafted* into a paper and
is **REGISTRATION-READY** is **PP3**, living in `drafting-factory/production/
pp3-preregistration-note/`. Nothing reads "post-ready" because (a) the terminal
agent state IS "REGISTRATION-READY awaiting Joe's per-action GO," and that GO
has not been given; and (b) by design the GU repo does not surface factory
release states, and DF's own top-level registers are slightly behind its
production home. The B5 source spine is hard-blocked on material the program
author *never released* (mining does not help), but the adjacent Lane-1 theorem
work is non-blocked and active. The anomaly "one number" is computable now
(machinery/literature exist) but un-run and reconstruction-grade.

---

## 1. Where the DE packet lives + exact status; PP1 vs PP3

**Two distinct frozen DE packets, both authored and owned GU-side:**

- **PP1 — the SIGN.** `explorations/blockbuster-p1-de-sign-covariance-2026-07-19.md`.
  Frozen 2026-07-19, INTERNAL, conditional, `R0_COND`. Claim: dark energy never
  goes phantom — `w0+1 > 0` and pointwise `w(z) >= -1` for all z (the side of
  `w = -1` is a readout of the transmitted orientation, not a free coefficient).
  The bare sign is explicitly **non-distinctive** (all single-field quintessence
  shares it); the distinctive content is the rigidity + joint kill surface.
  Status on the standing rule's shelf: "PP1 (frozen 2026-07-19)"; a **backfill
  standing registration candidate** (never externally timestamped), each
  "awaiting its own per-action GO" (standing rule §Registration item 6).

- **PP3 — the SHAPE / curve family.** `explorations/prediction-package-pp3-de-
  curve-family-2026-07-20.md`. Frozen 2026-07-20, v0.2,
  `package_status: FROZEN_CONDITIONAL_CURVE_FAMILY`, owner item
  `PRED-CANDIDATE-PACKETS`, Lane 2. Claim: IF a future release detects any
  deviation from LCDM, the point lies on a **one-parameter thawing locus** —
  non-phantom (inherits PP1's sign leg), segment `w0+1 <= 0.054`, frozen slope
  `wa/(w0+1) in [-1.33, -1.00]`, plus a second curvature invariant
  `S2 ~= -0.17`. Four numeric kills (K1-K4). CONDITIONAL, exploration tier,
  construction-scoped (GU does **not** predict the DE amplitude — PP3 packages
  the *shape*, not the amplitude).

**The drafted paper (the thing that could be "posted") is PP3, and it lives
DF-side:** `drafting-factory/production/pp3-preregistration-note/` —
`draft-pp3-preregistration-note-v0.1.md` (letter-length manuscript, every number
transcribed from the frozen packet), `COVER-NOTE-FOR-JOE.md`, and `DECISIONS.md`.
Exact status per `DECISIONS.md`: **REGISTRATION-READY** — all six Joe decisions
resolved and cascaded (GO-in-principle, venue mechanism locked, author line
"Joseph Hernandez, Independent Researcher," title locked, DR2 table in main
text). "The only outstanding item is Joe's per-action GO."

**PP1 vs PP3 in one line:** PP1 = *dark energy never crosses into phantom*
(the sign); PP3 = *if it deviates at all, the deviation sits on this specific
frozen line and curvature* (the shape). PP3 reuses PP1's non-phantom leg as its
leg 1 and adds the segment/slope/curvature confinement. Both "judgments stand
together" (PP3 §Distinction). PP2 (matter-parity, unrelated to DE) also exists
and is likewise a backfill candidate.

So, to Joe's phrasing: the DE packet is **frozen** (twice, PP1 + PP3) on the GU
side and **drafted + REGISTRATION-READY** on the DF side. It is not "post-ready"
in the sense of posted, because that requires his GO (see §3).

## 2. Redundancy or seam? — a clean seam, no duplication to fix

It is a **seam**, and the standing rule + portfolio are explicit and defensive
about not duplicating. The "a lane here and a lane in there" appearance comes
from the word "lane" being reused at both ends of one pipeline, not from two
tracks doing the same job.

**What each side owns (authoritative, per the standing rule §Registration and
`research-portfolio.json` authority/seam blocks):**

- **GU (source repo) owns the science.** Freezing packets, the enumerated
  condition chain, the numeric kill thresholds, native-vs-forced classification,
  research grade, claim status. Its DE work lives in **Lane 2**:
  `PRED-CANDIDATE-PACKETS` (owner of PP1/PP2/PP3), `DE-AMP-DIAGNOSTIC` (the
  data-facing amplitude audit), `DE-F1-TRIPWIRE` (the one-sided ceiling monitor),
  `P-OBS-LEG` (routes the observational leg). `research-portfolio.json`
  authority: `verdict_and_scientific_status_gate: Joe`;
  `publication_seed_and_drafting_priority_owner: drafting-factory`.

- **DF (factory) owns paper PRODUCTION + staging.** Turning a frozen packet into
  a manuscript, readiness, venue prep, and holding at the boundary. Per the
  standing rule: prediction packets become **PREDICTION PAPERS — a paper TYPE,
  not a new lane or channel anywhere** — flowing through DF's normal pipeline
  with one routing rule (prediction papers outrank every other paper type).
  `DECISIONS.md` restates it: "no new lane or channel."

- **Joe owns exactly one gate.** Standing rule item 5: "**EXACTLY ONE Joe gate
  per artifact, at the external boundary only.**" Freezing auto-seeds the
  factory (no approval); drafting/readiness/venue prep are automatic (no
  approval); "source repos do NOT track factory release states." Joe's only
  touchpoint is the posting itself.

**Feedback direction (the return path that ties the seam):** DF sends
carding/hardening feedback to the source repo's mailbox; the repo routes it —
prediction-side hardening to **Lane 2**, paper-side hardening to **Lane 3**.
"GU's Lane 2 and Lane 3 both ultimately produce papers — different TYPES of
paper, one queue downstream."

**Explicit anti-duplication guards already in the canon (so there is nothing to
de-duplicate):**

- `research-portfolio.json` publication_seed_seam: "Do not ... open a parallel
  GU publication-priority queue"; PAPER-SEED-ROUTING forbidden_shortcut: "Do not
  create a parallel GU drafting queue."
- `FALSIFICATION-BATTERY` channel: experimental predictions are routed to "the
  EXISTING prediction machinery ... NO second parallel attention/monitoring
  mechanism (Joe standing rule)."
- `P-OBS-LEG`: routes PP1/PP3 to "the existing frozen prediction/tripwire
  machinery rather than creating a duplicate monitor"; forbidden_shortcut
  bans "duplicate DE-F1/prediction-package monitoring."

**Verdict: no genuine redundancy.** GU-Lane-2 (freeze the science) and the
DF-papers-lane (produce + stage the paper) are the two ends of one seam for the
same object at two pipeline stages, with a single Joe gate at the very end. The
only thing that legitimately *looks* like two lanes is that PP1/PP2 sit as
"backfill registration candidates" in the GU standing rule while PP3 has a DF
production home — but that is the same pipeline at different maturity, not two
competing queues.

## 3. Why does Joe see "nothing post-ready"?

Three compounding reasons, none of which is "the work isn't done":

1. **"Post-ready" == "REGISTRATION-READY awaiting Joe's GO," and that GO is the
   whole point of the gate.** PP3 is fully staged: frozen packet + transcribed
   manuscript + venue mechanism locked + author line + title + DR2 table, all
   six decisions cascaded (`DECISIONS.md`: "WALK COMPLETE ... PP3 status:
   REGISTRATION-READY — the only outstanding item is Joe's per-action GO").
   Under the standing rule, **POSTING IS THE FREEZE** and **Joe alone crosses
   the boundary**. So the correct terminal state, by design, is exactly this
   "ready-and-waiting-for-Joe" state — it is one notch below "posted," never
   "posted by an agent."

2. **The GU repo deliberately does not show a post-ready state.** Standing rule
   item 5: "source repos do NOT track factory release states — the factory
   surface is the single owner of progression." If Joe is looking at the GU
   side (Lane 2, the portfolio), he will correctly see *frozen packets* and
   *no* "post-ready" flag — that flag lives only on the DF surface.

3. **DF's own top-level registers are slightly behind its production home.** The
   production home (`DECISIONS.md`) says REGISTRATION-READY, but `PAPER-SEEDS.md`
   still lists `GU-SEED-PP3-PREREG` as `conditional_priority_review`
   ("time-sensitive but not automatically capacity-selected"), and
   `LANE-STATE.yaml` (updated 2026-07-20T14:00, `needs_joe: false`) shows Lane 1
   "moving / candidate intake" without surfacing PP3 as READY. The PP3 README
   flags this itself: the PAPER-SEEDS/FACTORY-STATE rows "should be synced into
   those registers by the steward on the next normal pass. Until then this
   README is the candidate record of truth." So the *summary* surfaces Joe would
   glance at have not yet been updated to say "one item is post-ready, your GO."

Net: nothing looks post-ready because it **is staged awaiting his GO** (not
because nothing was frozen+drafted), the GU side is designed not to show it, and
the DF summary registers haven't yet promoted PP3's READY state to the top. The
`DECISIONS.md` ~2-day READY-escalation clock (which would push an attention note
via system mailbox / JoeOps) is the intended remedy for exactly this "it's ready
but nobody flagged it" gap.

## 4. Is there any non-blocked work on the B5 source-action spine?

**On the B5 node itself: no — and mining more Weinstein sources will not
change that.** `B5-MIDDLE-DIFFERENTIAL` fired `B5-MIDDLE-SOURCE-GAP` on
2026-07-21 (`explorations/b5-middle-source-freeze-2026-07-21.md`). The missing
material is specifically the **"unreleased cyclic two-connection complex"**
(`D_A / F_B / identity / D_B`), which the program author stated on the podcast
he has **"never released to anyone"** (`claim-mining-toe-weinstein-2026-07-20.md`
§3, verdict UNRELEASED-CLAIM: "Nothing verifiable exists"). The existing primary
sources (draft Sec 9.3 / eqs 9.16, 9.18-9.19 / diagram 10.10; TOE transcript
02:41-02:45) have already been mined and yield only the *arena* (full-Dirac
`Omega^0(S)+Omega^1(S)`), the *degree skeleton* (`0->1->13->14`), and a
southeast-zero `2x2` roll — not a complete differential class. So the blocker is
**not** incomplete mining; it is material that does not exist publicly. Reopen
requires **new released material** ("a released formula matching the
two-connection on-shell signature is the clearest trigger"). Mining the same or
other existing Weinstein media cannot supply an unreleased construction.

**Adjacent, non-B5-dependent Lane-1 work: yes, active and unblocked — that is
where hourly effort has gone.** `OPERATOR-END-PENCIL` is now the **Lane-1 lead**
(Joe repointed 2026-07-21 from lattice-enumeration to the two-paper-gating
theorem work), and the `FALSIFICATION-BATTERY` channel is live. These produced
real 2026-07-21 results without any B5 material: the LP-LC deficiency resolution
(`lp-lc-deficiency-decisive-2026-07-21.md`, LC-SELECTOR), the anomaly-inflow
swing, and the pin-bordism cardinality computation (see §5). So the *spine as a
whole* is not idle: the B5 differential node is hard-parked on unreleased author
material, while the neighboring theorem work that gates the same two papers is
non-blocked and progressing.

## 5. Is the anomaly-rigor "one reconstruction number" computable now?

The "one number" = the **exact order of `Omega^{Pin+}_14`** and the
**SW-number / Pin-eta value of sigma's specific 14-class** — the evaluation that
would upgrade "ANOMALY-TRIVIAL disfavored" to "rigorously excluded" and turn the
`{q=0}` wall protection (and the `LP-FORCED`-escape ruling-out) from PROPOSAL
into theorem (`pin-bordism-cardinality-2026-07-21.md` §4c, §6).

**Answer: it is computable now — the machinery and literature exist — but it is
un-run and graded reconstruction-grade, and its payoff is capped by a
still-proposal-grade identification above it.** Specifically:

- **The tools are on the shelf, not missing.** Unlike B5, this is not an
  external source gap. The named instrument is the **Atiyah-Bott-Patodi (ABP) /
  Adams spectral sequence** for Pin bordism plus a **Pin eta-invariant /
  Stiefel-Whitney-number** evaluation on GU's specific 14-geometry. The control
  table (`Omega^{Pin}_n`, n=0..7, incl. anchors `Omega^{Pin-}_2 = Z/8`,
  `Omega^{Pin+}_4 = Z/16`) was reproduced from standard literature (ABP 1969;
  Kirby-Taylor; Freed-Hopkins; KTTW 1406.7329) and machine-checked (35/35). So
  the computation is *doable with available methods* — it simply was not run in
  the foreground pass (the doc states this plainly: "that needs the ABP /
  Adams spectral-sequence computation, which this foreground pass does not run").

- **Two caveats keep it from being a finished theorem.** (i) An ABP/Adams
  computation at n=14 is genuine, nontrivial work — "computable in principle"
  is not "already computed." (ii) The *entire* pin-bordism result is
  **CONDITIONAL on the proposal-grade anomaly-inflow identification**
  (`anomaly-inflow-swing-2026-07-21.md`): that the `{q<0}` obstruction is
  literally the `w1` reflection 't Hooft anomaly. That ID itself rests on
  banking the **operator-grade deck action** `U N U^{-1} = -N` (currently a
  toy-grade model, tagged ANALOGY in wave-swing-1) plus building the boundary
  determinant-line / partition-function variation. So even the exact number,
  once computed, would only be a theorem if the anomaly-inflow ID is first
  promoted from PROPOSAL.

- **Contrast with B5 (the key distinction for Joe).** B5 is blocked on material
  that *does not exist publicly* (unreleased) — no amount of internal work
  unblocks it. The anomaly number is blocked only on *someone running an
  available computation* (and on promoting an upstream proposal). Different kind
  of "blocked": B5 = external-material gap; the anomaly number = un-run
  in-house computation + upstream grade dependency.

---

## Artifact

This clarification: `explorations/de-packet-lane-structure-clarification-2026-07-21.md`.
