---
title: "Uncontestability / anti-crank audit of the PP3 pre-registration note before it goes public — hostile-but-fair referee + crank-signal + independent-researcher-credibility panel, ranked must-fix list, and a GO/hold verdict. Central finding: the segment ceiling (w0+1 <= 0.054) is calibration-convention-dependent and the note's Section 6 framing conflicts, on a publicly checkable number, with the repo's own outsider-facing VERIFICATION.md (which calls f0=0.125 VIABLE on DR2). The physics prediction does NOT stand without GU; the methodology contribution does. No fabricated citations found. Verdict: NOT ready as-is; a bounded, mostly-disclosure hardening pass is required before Joe's per-action GO."
status: active_research
doc_type: exploration
created: 2026-07-21
directed_by: "Joe direct chat, 2026-07-21 (anti-crank uncontestability audit of the REGISTRATION-READY PP3 packet; one synchronous read-only pass)"
inputs:
  - production/pp3-preregistration-note/draft-pp3-preregistration-note-v0.1.md (drafting-factory, private)
  - production/pp3-preregistration-note/DECISIONS.md
  - production/pp3-preregistration-note/COVER-NOTE-FOR-JOE.md
  - production/pp3-preregistration-note/README.md
  - explorations/prediction-package-pp3-de-curve-family-2026-07-20.md
  - explorations/blockbuster-p1-de-sign-covariance-2026-07-19.md
  - explorations/pp3-risk-register-2026-07-20.md
  - explorations/de-amplitude-audit-2026-07-20.md
  - explorations/W113-world-contact-2026-07-11.md
  - explorations/parsimony-unexplained-joints-ledger-2026-07-21.md
  - VERIFICATION.md
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
external_action: none
---

# Uncontestability audit — PP3 pre-registration note

Read-only, one synchronous pass. Scope: the letter-length manuscript
`draft-pp3-preregistration-note-v0.1.md` about to go public as (likely) Joe's
first proof-point as an independent researcher. Goal: surface everything a
hostile-but-fair expert triaging an unaffiliated physics paper would seize on,
so it can be hardened BEFORE the per-action GO. Nothing in the packet was
edited; nothing committed; nothing external moved.

Panel run inline in one worker (three lenses, synthesized): (i) hostile-but-fair
journal referee, (ii) crank-signal detector, (iii) independent-researcher
credibility strategist.

---

## Verdict (up front)

**NOT ready to post AS-IS. It is close, and the fixes are bounded — mostly
disclosure/framing, not new physics — but two of them are load-bearing for
exactly the "don't get binned as a crank" goal this pass exists to serve.**

The note has genuinely strong bones: honest self-grading (CONDITIONAL,
exploration-tier, carried unlaundered), a real pre-registration record
(timestamped public commits predating the discriminating data), numeric
pre-declared kills, an against-us table (Table 2) volunteered in the main text,
an explicitly non-confirmatory Branch N, and full emitter/commit reproducibility.
That apparatus is the note's best defense against the crank bin and must NOT be
weakened. But four things will draw fire from a good-faith expert, and one of
them is a **publicly checkable apparent self-contradiction with the note's own
cited repository**. Fix the SERIOUS items and it clears the bar; ship as-is and
it hands a hostile triager two free reasons to stop reading.

**Does the prediction stand on its own, without requiring belief in GU?**
Split answer, and the note should say so more sharply than it does:

- The **physics prediction** (the locus: non-phantom, slope in [-1.33, -1.00],
  segment ceiling, S2 curvature) does **NOT** stand without GU. Every number is
  the image of the theta-sector construction; delete GU and there is no reason
  to expect a future deviation to land on THIS one-parameter line rather than
  anywhere in the thawing corridor. The note is honest that this leg is
  CONDITIONAL and construction-scoped — good — but it occasionally blurs toward
  implying the locus itself is independently motivated. It is not.
- The **methodology contribution** (freeze-before-data, enumerate the chain,
  pre-declare numeric kills, notarize by public commit, supersede-not-edit)
  **DOES** stand alone and is the note's genuinely portable, GU-independent
  content. Section 7 is right that "the record has value precisely because it
  can fail." Keep the two contributions cleanly separated so a physics referee
  judging the (conditional, exploration-grade) locus and a methods reader
  judging the pre-registration standard each get a clean object.

No FATAL-as-is defect was found: the arithmetic is internally consistent, the
pre-registration is genuine (not post-hoc), and **no fabricated citations
exist** (both related-work references were web-verified real — see C2). The
block is a cluster of SERIOUS credibility items, led by one framing mismatch
that reads as a contradiction to anyone who opens the cited repo.

---

## Ranked must-fix list

Format per item: **location · what a good-faith expert concludes on seeing it ·
the concrete fix · severity.**

### SERIOUS (resolve before GO)

**S1 — The segment ceiling is calibration-convention-dependent, and Section 6's
framing conflicts, on a publicly checkable number, with the repo's own
VERIFICATION.md.**
- **Location:** Abstract ("amplitude w0 + 1 <= 0.054"); Section 5 K3 ("f0 <=
  0.027 is the frozen ceiling from data already in hand"); Section 6 ("The DESI
  DR2 BAO vector ... produced the f0 <= 0.027 ceiling and the +5.7 sigma
  exclusion of f0 = 0.125"). Cross-file: repo `VERIFICATION.md`, dark-energy
  bullet, and `explorations/W113-world-contact-2026-07-11.md` half-swing B.
- **What a good-faith expert concludes:** The note says DESI DR2 caps the
  amplitude at f0 <= 0.027 and excludes the canonical f0 = 0.125 at +5.7 sigma,
  presented as a straightforward "data already in hand" constraint. But the same
  public repo the note cites as [3] contains `VERIFICATION.md` (its designated
  outsider entry point, written so readers "do NOT have to trust" internal
  labels), which states the opposite in plain language: *"the shape AND the
  canonical f_0 = 0.125 are both viable on the DESI DR2 BAO likelihood (the old
  'f_0 tension' was a fixed-amplitude-slice artifact); the sector's ONE residual
  exclusion is an amplitude-calibration direction (+1.81% vs Planck)."* W113
  shows why: **amplitude-marginalized**, f0 = 0.125 sits INSIDE the Delta-chi^2
  <= 1 band and GU beats LCDM by ~3.3 chi^2 (1.3 AIC); the +5.7 sigma exclusion
  appears ONLY when the amplitude is **pinned to GU's own theta_star
  calibration** (A_GU ~ +5.66% above Planck) — a pinned amplitude that is itself
  at +5.74 sigma tension with what the BAO data prefer. So the f0 <= 0.027
  ceiling is not a robust DR2 fact; it is a fact *conditional on a specific
  calibration convention*, and it is precisely the "fixed-amplitude-slice"
  category the repo elsewhere flags as artifactual. A referee (or any reader who
  opens the cited repo — this is all public) sees the note's headline ceiling
  contradicted by the repo's own honesty file, on a load-bearing number that
  drives K3. That single impression ("the paper oversells a number its own repo
  walks back") is the most efficient way for a hostile triager to dismiss the
  whole thing.
- **Concrete fix:** Make the note's framing match VERIFICATION.md's, and make
  the ceiling's conditionality explicit where the ceiling is stated, not only in
  condition-link 4 and K3's fine print. Specifically: (a) in Section 6, add one
  sentence stating that under **amplitude marginalization** the DR2 BAO
  likelihood is consistent with f0 up to ~0.15 (canonical 0.125 included) and GU
  slightly out-fits LCDM; the f0 <= 0.027 ceiling and the +5.7 sigma exclusion
  hold under the packet's **own-theta_star (CMB-anchored) calibration**, which is
  condition link 4 and is itself in ~+1.8%/+5.7 sigma amplitude tension with the
  data. (b) Re-label the ceiling throughout as calibration-scoped ("under
  own-theta_star closure") rather than "from data already in hand." (c) Confirm
  the ceiling number the note wants to defend is the one it can defend without
  contradicting its own repo — i.e. reconcile VERIFICATION.md and the note so the
  public record tells ONE story. This is the top priority precisely because it is
  publicly falsifiable against the cited source. **Severity: SERIOUS (reads as
  fatal to any reader who cross-checks the repo).**

**S2 — Section 4's competitor baseline omits the one competitor that matters:
generic thawing quintessence.**
- **Location:** Section 4, "Competitor baseline" (compares only LCDM and free
  w0waCDM). Compare against COVER-NOTE-FOR-JOE.md, which names this exact gap as
  "**Strongest SURVIVING objection**."
- **What a good-faith expert concludes:** The slope band [-1.33, -1.00] sits
  *inside* the standard thawing-quintessence corridor (the Caldwell-Linder
  wa ~ -(1 to ~1.5)(1+w0) relation). A cosmologist reads Section 4, sees the note
  benchmark only against LCDM and free CPL, and concludes the author either does
  not know the thawing literature or is avoiding the comparison that most erodes
  distinctiveness — both are crank/naivety tells. The note's real novelty
  (numeric tightness of the band, the segment ceiling, and the S2 curvature
  invariant that generic thawing does NOT fix) is defensible, but it is argued in
  Joe's private cover note and NOT in the manuscript.
- **Concrete fix:** Add a thawing-quintessence row/paragraph to Section 4 that
  (a) concedes the slope band overlaps the generic thawing corridor, (b) claims
  novelty only for the numeric confinement (band edges, segment ceiling) and the
  S2 curvature invariant as the genuine discriminant, and (c) states plainly that
  a low-precision Branch-D hit near slope -1 would NOT uniquely credit this
  construction — only the curvature-resolving regime is sharply discriminating.
  This is lifting the cover note's own answer into the paper. **Severity:
  SERIOUS.**

**S3 — The note is not self-contained: it leans on internal repo labels a
reader without repo access cannot decode.**
- **Location:** Section 2 condition chain ("frozen H44 model spec," "B.5 scale
  slot," "COSMO-A1 bracket," "the DE-F1 tripwire," "OQ2"); Section 1/8
  ("theta-sector," R0_COND); throughout ("own-theta_star calibration,"
  "SRC-COH-1" via PP1); Table 1's "0.125 (excluded ref)" row label.
- **What a good-faith expert concludes:** A paper that references its author's
  private nomenclature (H44, B.5, COSMO-A1, DE-F1, OQ2) as if the reader shares
  it reads as insular — the single most reliable surface signal of
  independent-researcher crank work. It also blocks the referee from actually
  checking the claim, which converts "maybe interesting" into "can't evaluate,
  next paper."
- **Concrete fix:** Every internal identifier that survives into the manuscript
  must be either (a) defined in one clause on first use in reader-facing terms
  ("the mode-mass admissible band," "the absolute-scale slot," "a previously
  frozen confrontation bracket"), or (b) removed. The condition chain in Section
  2 especially should read as five plain-English physical premises, with the
  repo labels relegated to a footnote or dropped. Table 1's "excluded ref" row
  should say what it is (a reference amplitude excluded by the current data) or
  be cut. **Severity: SERIOUS.**

**S4 — "Geometric Unity" in the title is a triage-stage crank-bin risk.**
- **Location:** Title; Abstract; reference [1] (Weinstein, self-published draft
  manuscript, geometricunity.org).
- **What a good-faith expert concludes:** For an unaffiliated author, "Geometric
  Unity" in the title of a first public paper is, to a large fraction of
  cosmology referees doing 20-second triage, a stop signal before the honest
  grading is ever read. The note works hard to defuse this (opens with what GU
  does NOT predict, grades CONDITIONAL, scopes to "the reconstruction," cites
  Weinstein only as origin-of-program), and per DECISIONS.md this is a
  *deliberate* choice — Joe wants the title to be "part of the experiment"
  (heterodox-evaluation standard). That is a legitimate research posture, so this
  is flagged as a KNOWN TRADEOFF, not a defect to silently overturn.
- **Concrete fix:** No change recommended against Joe's stated intent — but the
  cost should be named at decision time, and there is a cheap hedge: ensure the
  *first* substantive noun a triager meets (title's leading clause, abstract's
  first sentence) is "pre-registered conditional shape test for dark energy," so
  the methodology framing reaches the reader before the program name does. The
  current title already leads with that clause; keep it and do not let any later
  edit invert the order. **Severity: SERIOUS for reach, but Joe-owned; ship-blocking
  only if Joe wants maximal uptake over the meta-experiment.**

**S5 — The bare non-phantom sign's non-distinctiveness is disclosed in PP1 but
not carried into this public note.**
- **Location:** Section 4 (competitor baseline) and Section 5 K1; the sign leg is
  inherited from PP1, whose PP1-5 states flatly "**the bare sign is NOT
  distinctive**" (shared with all single-field quintessence). The public note
  never says this.
- **What a good-faith expert concludes:** The note leans on non-phantom-ness
  (K1, the "non-phantom" locus leg) without conceding that w >= -1 alone is
  shared with every quintessence model. PP1 concedes this explicitly; a referee
  who notices the public note quietly dropped that concession reads it as
  selective presentation.
- **Concrete fix:** One clause in Section 4: "the non-phantom side alone is
  shared with all single-field quintessence and is not distinctive; the
  distinctive content is the rigidity — a phantom reading forces failure of a
  named link — plus the slope and segment confinement." Inherit PP1's own
  honesty. **Severity: SERIOUS (cheap; it is an honesty-symmetry gap).**

**S6 — The PP3-specific kill K2 is widened by an unexplained 35% tolerance.**
- **Location:** Section 5 K2 ("the frozen band widened by the pre-declared 35%
  tolerance of the discriminator in the emitter"); Abstract's severity claim
  rests on K2.
- **What a good-faith expert concludes:** K2 is the headline PP3-specific kill.
  Widening the band by a bare "35%" with no derivation reads as a tunable knob —
  exactly the "dressed-up curve fitting" charge the note is otherwise built to
  survive. "Why 35%?" currently has no answer in the manuscript.
- **Concrete fix:** State where 35% comes from (e.g. the M^2-band spread plus the
  calibration/CPL-projection convention uncertainty quantified in the convention
  pin), or cite the emitter line that fixes it, so the width is *derived* not
  *chosen*. If it cannot be justified, say it is a deliberately conservative
  margin and give the un-widened kill too. **Severity: SERIOUS (undercuts the
  headline kill's severity if left bare).**

### COSMETIC / MINOR (fix in the same pass; individually non-blocking)

**C1 — The M^2 band {3, 7, 8} is asserted without derivation or citation →
numerology smell.** *Location:* Section 2 link 3, Section 3 band spots, Section 3
S2 discriminant. *Expert reaction:* three specific integers pulled from named
root systems (S^3/A_1/BC_1) with no shown derivation invites a numerology read,
and these integers drive the S2 "reads off the root system" claim. *Fix:* cite
the repo derivation of the ground eigenvalues in one clause, or state "computed
in [ref], reconstruction grade" so the integers are sourced, not conjured.
*Severity: cosmetic (borderline serious given the numerology angle).*

**C2 — Citation-list hygiene.** *Location:* References. (a) [8] (CPL) is listed
but never cited inline — orphan reference; cite it at the first "CPL" in Section
3. (b) The related-work citations in Section 6 (Bianconi; Thattarampilly, Zheng,
Kakkat) are given inline but are NOT in the numbered [1]-[8] list — inconsistent
citation style; give them numbers. (c) Both were web-verified as REAL
(Bianconi, "Gravity from entropy," Phys. Rev. D 111, 066001 (2025), confirmed;
Thattarampilly/Zheng/Kakkat arXiv:2602.13694, "Spherically symmetric black holes
in Gravity from Entropy," confirmed) — but 2602.13694 appears to be an **arXiv
preprint**, while the note cites it as "Phys. Rev. D, 2026." Cite it as a preprint
unless the PRD publication is confirmed. *Severity: cosmetic (but a mislabeled
preprint-as-journal is the kind of slip a referee notices).*

**C3 — The abstract over-features S2 as if near-term measurable.** *Location:*
Abstract ("a second curvature invariant S2 ... that discriminates the admissible
mass band"); Section 3 ("reads off the root system — a second decimal frozen
pre-data"). *Expert reaction:* measuring the quadratic coefficient of w(a) to
|S2| ~ 0.1 is far beyond DESI DR3/Euclid; foregrounding it risks looking like
decoration. The body does hedge ("when resolvable"), but the abstract does not.
*Fix:* in the abstract, mark S2 explicitly as an in-principle / far-future
discriminator, not a near-term test. *Severity: cosmetic.*

**C4 — "strictly sharper" over-claims against Bianconi.** *Location:* Section 6
related-work ("strictly sharper — and correspondingly easier to kill"). *Fix:*
soften to "sharper on the (w0, wa) plane where it makes a locus claim," since the
two programs address different targets. *Severity: cosmetic.*

**C5 — Missing standard credibility furniture.** *Location:* author line / end
matter. No ORCID, no contact email, no formal "Code & data availability"
statement. For an independent author these materially raise the take-seriously
baseline; the note already has the commit hashes and emitter names, so a
one-paragraph availability statement is nearly free. *Fix:* add ORCID, a contact
email, and a short code-availability statement pointing at the repo + the named
emitter scripts + the two freeze commits. *Severity: cosmetic.*

**C6 — Dual-audience structure is a mild inherent weakness.** The note is
simultaneously a conditional physics prediction (which a phenomenology referee
grades as exploration-tier, conditional-on-GU) and a methodology exemplar (which
a methods reader judges independently). This is disclosed and acceptable, but the
cleaner the seam between the two, the less either referee feels the other half is
padding. *Fix:* ensure Section 7 (methodology) is self-containedly readable and
explicitly flagged as the GU-independent contribution. *Severity: cosmetic.*

---

## Panel notes (the three lenses, synthesized)

**(i) Hostile-but-fair referee.** Is it genuinely PRE-REGISTERED, FALSIFIABLE,
DISTINCTIVE, and is the conditional logic sound? Pre-registered: YES — real
timestamped public commits (a833d98, 2da1c73) predate any post-DR2 discriminating
release; DR2 is consumed and disclosed; the novel content (slope, S2) is computed
from theory structure. Falsifiable: YES — K1-K4 are numeric, fire on measured
quantities, and the note volunteers that current central values would fire
K3/K2/K1; Branch N is explicitly non-confirmatory; the one unfalsifiable corner
(permanent mimic) is disclosed, not hidden. The conditional "if it deviates, it
lies here" is NOT unfalsifiability-in-disguise, because the kill is scoped to a
named construction (the theta-sector family as the DE realization) rather than
deflected into nothing — a kill genuinely retires that construction. **The two
real referee wins for a hostile reader are S1 (the calibration-ceiling framing vs
the repo's own VERIFICATION.md) and S2 (the missing thawing competitor).** S6
(the 35% knob) is the third. Distinctive from LCDM in Branch D: yes. Distinctive
from generic thawing: only in tightness + S2 — which must be stated (S2).

**(ii) Crank-signal detector.** Grandiosity/TOE tone in the prose: largely ABSENT
— the note opens with what GU does not predict and grades itself down repeatedly;
this is the opposite of grandiosity and is a real asset. The crank exposure is
NOT the tone; it is (a) the program name in the title (S4), (b) undefined
internal jargon (S3), (c) the unsourced integer band {3,7,8} (C1), and (d) the
self-published [1] Weinstein manuscript (unavoidable, scoped). Numerology smell is
localized to C1 and the bare 35% (S6). Unearned certainty is minor: "must lie on
a locus" is conditioned; "strictly sharper" (C4) and the S2 "reads off the root
system" (C3) are the only reach-y phrases. Over-decoration: the full apparatus
(2 branches, 4 kills, S2, convention pins, residual-direction credit) is heavy for
a one-observable-leg exploration claim, but density is not crankery and the
apparatus is load-bearing — leave it.

**(iii) Independent-researcher credibility strategist.** What gets an
unaffiliated paper taken seriously: tight scope (PARTIAL — dual physics+methods
audience, C6), honest grading (STRONG — exemplary, do not touch), standard
notation (PARTIAL — CPL is standard but internal jargon breaks it, S3), full
reproducibility (STRONG — emitters + hashes; add a formal availability statement,
C5), and the decisive test — **does the prediction stand without GU?** The
methodology stands alone; the physics does not and cannot, and the note is
mostly honest about that (keep it honest, tighten the seam per C6). Net: the
honest-grading + reproducibility + volunteered against-us-table combination is a
genuinely credible independent-researcher posture — better than most unaffiliated
submissions — and it is undercut chiefly by S1 (a public framing mismatch) and
S3 (insular notation). Fix those two and the credibility profile is strong.

---

## What NOT to touch (the note's defenses — preserve these)

- The carried-unlaundered grade (CONDITIONAL / exploration-tier / R0_COND).
- The known-inputs disclosure (DR2 consumed; quadrant known pre-freeze; zero
  credit claimed; scoring against future releases only).
- Table 2 in the MAIN TEXT (the against-us exposure) plus its caveat paragraph.
- Branch N stated as never-confirmation.
- The notarized-commit / supersede-not-edit methodology (Section 7).
- The emitter + commit-hash reproducibility trail.

These are exactly what separate this from crank work; do not trade any of them
away while hardening.

---

## Bottom line for the GO decision

Hold the per-action GO until the SERIOUS items are addressed. The single
must-fix is **S1**: reconcile the segment-ceiling framing with the repo's own
public VERIFICATION.md so the note does not contradict its cited source on a
load-bearing number, and state the ceiling as calibration-convention-scoped.
**S2** (add the thawing competitor) and **S3** (de-jargon into a self-contained
paper) are the next two; **S5**, **S6**, and the cosmetic sweep can ride the same
edit. **S4** (GU in the title) is Joe's deliberate call — flagged with its cost,
not overturned. None of this requires re-deriving a number or re-freezing the
packet: the fixes are disclosure, framing, competitor-comparison, and notation.
After that pass the note is a credible, hard-to-dismiss first public
proof-point — and it should still carry, unweakened, every honesty feature that
currently protects it. The physics prediction remains conditional on GU (as it
must); the pre-registration methodology stands on its own.

## Boundary

Exploration tier, read-only audit. One new file written (this document). The PP3
packet, the drafting-factory manuscript, VERIFICATION.md, and all inputs were
read but NOT edited. No commit, no push, no external action. No claim-status,
canon-verdict, paper-status, or public-posture change; the frozen PP3 numbers,
the per-file grades, and the VERIFICATION.md/PP3 reconciliation question are
surfaced for Joe, not moved. Citation existence-checks used read-only web search;
no other external contact.
