# Cross-Repo Survey: ai-epistemology, architecture-of-legitimacy, church-of-ai

Date: 2026-07-11 (executed 2026-07-13 session). Input to cross-repo synthesis.
Read-only survey; sources are each repo's README / HYPOTHESIS / CLAIM-LEDGER /
CLAIMS / TESTS / STATUS as of this date. Grades are the repos' own where they
exist; my honest reading where they don't.

---

## 1. ai-epistemology (`repos/public/ai-epistemology`)

### North Star

Verdict on Branch 4: is intentionally designed epistemic machinery a
**categorically new capability class** enabled by AI-native systems, or does it
reduce to acceleration/automation of existing processes? Success = a verdict
evaluable independently of who generated it. Five-branch spine (v1.8, ratified
2026-07-01): Legibility, Portability, Separability, New capability (the
verdict), Evolvability (second-order).

### Main research CONTENT lines

- **SCS separability discriminator (C003):** specification-certifiable
  separability — a sound static check, in advance of any run, that the
  operational/verification output reads no motivationally-written variable.
  Distinguishes designed from emergent AND from alignment architectures.
- **Legitimacy-stability theory (C006-C010, the T12-T15 family):** a formal
  theory of epistemic-system health: founding legitimacy (T13 genesis-block,
  F1-F5), legitimacy vs calibration independence (T14), open-access legitimacy
  stability unified with bounded-membership (T12-U), and an admission-rate
  optimum λ*(s) grounded in rate-distortion theory (T15).
- **Structural recurrence across programs (C002):** whether epistemic control
  loops (evidence-tiered status, falsification-first, absorber pressure,
  formal-anchor pressure) recur across independent AI-native repos beyond
  same-designer isomorphism.
- **Epistemic-improvement measurability (C005):** seven-metric bundle for
  measuring whether the machinery actually improves knowledge.
- **Higher-order epistemic search / evolvability (C011):** can a system mutate
  its own O2/O3 machinery (operators, personas, gates, ontology) and show
  durable lift under matched budget? Order taxonomy O0-O4.
- **Founder-independent claim-space measure (E038):** the convergent open
  problem shared by C006/C009/C010 — a measure on claim space not fixed by the
  founder.
- **Absorber discipline as content:** 25 mapped absorber fields
  (PAC-learning, social choice, BFT, Ostrom, formal verification, ...) used as
  a standing "is anything here actually new?" boundary.

### Strongest results (repo's own grades)

- **SCS (E018/E027/E040/E042):** SCS-1 decidability PROVED; SCS-2
  discrimination of designed (TI-style) from emergent and from alignment
  architectures PROVED modulo class definitions, without routing through
  Arrow; separation = run-universal spec-certified invariance, strictly
  stronger than alignment's run-contingent invariance. SCS-3 non-vacuity holds
  at SPECIFICATION level only (CE-1 witness). C003 status: **formalizing**;
  K2 not cleared; K6 (training-data correlation floor) untriggered and
  uncleared — named as the total gate on all "realized advantage" halves.
  After E042's falsification pass, the SCS *checker* is conceded as absorbed
  by non-interference theory; only class-discrimination is residual.
- **T12-U (E016):** legitimacy-stability necessity/sufficiency/unification
  PROVED conditional on (RENT). Status: formalizing → components now
  **testable** (D_mu(s) instantiated on CE-1, provenance-contingent).
- **T13 Expansion Theorem (E017):** founding→operating legitimacy bridge
  PROVED conditional on (INST)+T12-U; F5 instantiated and executed on CE-1.
  C006: **testable**, no adequacy verdict.
- **T15/λ*(s) (E014/E041):** interior optimum existence/uniqueness proved
  under named primitives; a substep was later found INVALID (E034/E041 —
  honest correction), replaced by a two-tier pointwise-curvature certificate.
  C010: **testable**, uniqueness certificate WEAKENED.
- **E038 measure result:** canonical/strong founder-independent measure proved
  IMPOSSIBLE for typed certificate domains; a weak (verdict-independent,
  bounded-public-choice) measure achievable and sufficient via a declared
  robustness margin m. Repo grade: sub-theorem ladder step, no promotion.
- **T6 (E039):** Shapley computability separation formalizing — recorded
  provenance identified as the single architectural primitive behind T6, SCS,
  and (RENT).
- **Honest negatives as results:** E028 executed the C005 metric bundle —
  **0/7 metrics survive** adversarial validation; T2 killed as stated
  (PK-0002); T2c killed (PK-0003); original governance-transfer experiment
  (C004) retired as null. The repo treats these as productive output.

Grade summary (repo's own ladder): nothing promoted; strongest items sit at
formalizing/testable with proved sub-theorems, all conditional and Joe-gated.
Zero killed top-level claims; two killed theorem paths.

### Open questions

- K6: is designed separability real once training-data error correlation is
  measured? Harness exists; **no scored data ever collected**. Gates every
  realized-advantage claim.
- C002 independence: find one control loop in an outside program not built by
  this author and not on the CapacityOS package (Joe-gated decisive test).
- SCS-3 implementation faithfulness and class richness (spec-level only now).
- EXP-0002 (C011 matched-budget O2/O3 lift) awaits genuinely independent
  execution.
- Founder-robust adequacy verdicts: CE-1 E033 verdicts shown to sit INSIDE the
  robustness margin, i.e. not founder-robust yet.
- Whether Branch 4 has any content at all once absorbers finish eating the
  candidates (the North Star itself).

### GU / TaF / TI hooks

- **Legitimacy-as-selection, formalized:** T12-U/T13/T15 are literally a
  selection theory for what enters a canonical record — admission rate λ*(s),
  founding admissibility F1-F5, pollution/depletion failure modes. This is the
  closest existing formal neighbor to TI's issuance/admissibility and to
  legitimacy-as-selection.
- **Recorded provenance = finality primitive:** E039's result that T6, SCS,
  and (RENT) are three faces of one primitive — an append-only provenance
  record — is a temporal-issuance/finality claim in epistemic clothing:
  capabilities exist iff issuance is recorded and final.
- **SCS vs the arena/value split:** the motivational module (value,
  symmetry-breaking selection) vs verification module (invariant arena) with a
  proved run-universal vs run-contingent invariance distinction rhymes
  strongly with GU's invariant-vs-symmetry-breaking-selection and per-state/sup
  separation (spec-certified for ALL runs vs contingent on each run's IC).
- **Located-not-forced:** E038 is a located-not-forced theorem — the canonical
  (forced) measure is impossible; a declared, located choice with an explicit
  robustness margin is achievable and sufficient. Same shape as GU's
  interface/adapter slot: no canonical adapter, a declared one carries the
  result.
- **Honest-negative discipline as content:** 0/7 metrics surviving, path
  kills, retired transfer experiment, self-invalidated lemma substeps — the
  repo generates epistemics findings BY practicing honest negatives, which is
  itself evidence for the GU-side claim that honest-negative discipline is
  load-bearing content, not process hygiene.

---

## 2. architecture-of-legitimacy (`repos/public/architecture-of-legitimacy`)

### North Star

Can contribution, legitimacy, and reward be bound together in a
capture-resistant way such that collaboration becomes more valuable than
defection — proved first in one public repo, extending (horizon claims C8/C9)
to collaborative institutions for a post-scarcity world?

### Main research CONTENT lines

- **Coupled protocol stack (C2):** the minimal serious object is a coupled
  stack (eligibility → taxonomy → validation → value rubric → cadence →
  contribution log → rights → rewards → governance → capture monitoring), not
  any single ledger/token/rubric/AI-judge; isolated modules fail or mislead.
- **Legitimacy as first-class design variable (C3):** operational schema —
  visibility, contestability, voice, exit-with-retained-record, adaptive rule
  change, bounded authority, non-capture; with the sharp separation
  **legitimacy ≠ correctness** (valuation can be wrong while process stays
  legitimate, and vice versa).
- **Collaboration-vs-defection payoff line (C4/T5):** toy model
  `R_c + L_c + future_claim(V_c) - C_c > P_d·G_d - D_d·S_d - F`, with each
  term mapped to a protocol lever; sensitivity and defection-pressure screens.
- **Legitimate founder-led phase (C6/T7):** founding can be legitimate iff
  powers, limits, and transition milestones are explicit — a
  founding→operating transition theory in institutional form.
- **S7 legitimacy-monad crosswalk:** categorical `eta_P : P -> L(P)` mapped
  onto the stack: presheaf layer = raw contributions; gluing obstruction =
  contestability/non-capture failure; Lose[K] = explicit loss notes;
  provenance partial order = log/appeal/governance chains.
- **AI-as-support guardrail (C7):** AI can critique/synthesize/review but
  cannot itself supply legitimacy.

### Strongest results (repo's own grades)

- Repo's own claim ledger grades: **C1/C2/C3 core; C2/C3 working
  (underformalized); C4/C5/C6 working-testable; C8/C9 horizon. Nothing
  promoted, nothing falsified.**
- **T1-T11 all in synthetic-fixture stage.** Every test artifact explicitly
  disclaims passing its test ("does not mark TX passed," no real contribution
  records, no live pilot). The strongest concrete outputs are: the T4
  legitimacy failure table + response routing, the T5 payoff model with
  variable-to-lever traceability, and the RQ5 first-pilot readiness stack
  (packet checklist, source-trace gate, stop maps) — a fully rehearsed
  first-pilot workflow that has never run live.
- **S7 crosswalk (2026-06-25):** the sharpest formal artifact; grade: "active
  integration note" — a formal target, not a result. Strong form (legitimacy
  as first-class primitive of institutional mathematics) explicitly held apart
  from the conservative workflow formalization.

Honest overall grade: a carefully specified, adversarially self-aware design
object at pre-empirical stage; zero live evidence; disciplined about saying so.

### Open questions

- Does the first real (non-synthetic) contribution pilot produce signal or
  noise (C1's proof burden)? Everything is staged for it; nothing has run.
- Can legitimacy be operationalized non-circularly (C3's demotion condition)?
- Under what payoff conditions does collaboration actually dominate (C4) —
  currently only a relative model, "not a calculator"?
- Rights taxonomy: what can `future_claim(V_c)` mean before rewards exist (C5)?
- Founder-phase transition triggers that avoid founder theater (C6).
- Whether accumulating value makes capture strictly easier under the proposed
  rules (standing falsification condition).

### GU / TaF / TI hooks

- **The S7 crosswalk is an explicit, already-built GU hook:** the legitimacy
  monad `P -> L(P)` with gluing obstructions, loss profiles, and provenance
  partial orders is this repo's declared formal engine, imported from the
  TaF/GU S7 thread. If GU's legitimacy/selection machinery firms up, this repo
  is its designated institutional model.
- **Legitimacy-as-selection / admissibility:** the whole stack is a theory of
  which contributions are ADMITTED into a final record; "exit with retained
  record" and log admission are issuance+finality conditions in TI's sense.
- **Located-not-forced:** legitimacy ≠ correctness is the institutional form —
  the accepted record is a located, contestable selection, not forced by
  truth; explicit Lose[K]/loss-notes make the non-forced residue visible.
- **Founding→operating transition (C6/T7)** is the same object as
  ai-epistemology's T13 Expansion Theorem and TI's genesis/bootstrap problem —
  three programs converging on founding-legitimacy-with-explicit-transition.

---

## 3. church-of-ai (`repos/public/church-of-ai`)

### North Star

No formal north star document; the stated deep bet: **"Intelligence matures
when it learns to build systems where cooperation is not enforced from above,
but becomes the best move available."** Operational goal: a
satirical-but-serious public entryway/map for the ecosystem that must EARN
governance and participation through work (V1 entryway → V2 participation
foundation → V3 open governance, V2/V3 explicitly deferred).

### Main research CONTENT lines (thin by design — this is the map, not a lab)

- **Positive-sum coordination as an engineering problem:** design systems
  where the structurally optimal individual move is cooperative; bad actors
  excluded by structure, not trust.
- **Claim-status discipline as public epistemics:** four statuses (proven so
  far / being tested / hypothesized / deferred), default-assume "hypothesized
  at best," premature ratification named as the seed of dogma.
- **Joke-as-filter hypothesis:** the satirical wrapper as a selection
  mechanism for the right participants ("serious about the work, not about
  ourselves"), rejecting both the DAO/token frame and the inaccessible
  academic frame.
- **Anti-dogma theory:** a concrete failure taxonomy — founder mythology,
  unfalsifiable claims, premature ratification, sacred terminology.
- **Open-rules lifecycle:** proposed → discussed → tested → revised →
  documented → ratified, all in the open; rules never handed down.

### Strongest results (repo's own grades)

- The repo grades ITSELF honestly: **"No claims have been ratified beyond
  what is demonstrated in the repos themselves."** Its own key claims are
  self-labeled: joke-as-filter = **being tested**; community-service frame and
  earn-governance = **hypothesized**; participation/governance/rewards =
  **deferred**. Nothing proven.
- Strongest concrete artifact: the claim-status discipline itself plus the
  boundaries docs (WHAT-THIS-IS / IS-NOT) — a working public instance of
  claim-grading applied reflexively. Grade: live practice, no verdict.

### Open questions

- Does the satirical filter actually select good-faith serious participants
  (its only live experiment)?
- Can governance authority be earned rather than declared — what evidence
  would ratify V2/V3 prerequisites?
- Is "open-source community service" a durable frame for this work?
- What does "cooperation as best available move" require formally? (The repo
  points at architecture-of-legitimacy for this; it holds no formal apparatus
  of its own.)

### GU / TaF / TI hooks

- **Legitimacy-as-selection at the social layer:** "cooperation becomes the
  best move available" is the ecosystem-level statement of selecting a
  cooperative equilibrium by arena design rather than enforcement — the
  institutional shadow of arena/value = invariant-vs-symmetry-breaking-
  selection (design the invariant arena; let value selection break symmetry
  toward cooperation).
- **Claim-status ladder as issuance/finality:** proven-so-far / being-tested /
  hypothesized / deferred is a temporal-issuance ladder for claims — statuses
  are issued slowly, finality ("proven so far") is deliberately scarce, and
  premature finality is the named failure mode (dogma). Honest-negative
  discipline is here promoted to a PUBLIC norm, not just a lab norm.
- Secondary: joke-as-filter is an interface/adapter in the GU sense — a
  declared, non-canonical membrane between the formal programs and the public,
  doing selection work at the boundary.

---

## Cross-cutting note for the synthesis

Three independent-looking convergences worth flagging:

1. **Founding→operating legitimacy** appears three times (ai-epistemology T13,
   AoL C6/T7, TI genesis) — a shared theorem target.
2. **Recorded provenance / append-only record as the enabling primitive**
   (ai-epistemology E039; AoL provenance partial order; church-of-ai
   receipts-before-revelation) — finality as the load-bearing object.
3. **Located-not-forced** shows up as a proved impossibility+sufficiency pair
   (E038), an institutional principle (legitimacy ≠ correctness), and a
   cultural norm (no canonical authority, declared open rules). Same shape at
   three altitudes.

Caveat on (1)-(3): ai-epistemology's own C002 warns that same-designer
institutional isomorphism is UNDEFEATED as the explanation for cross-repo
recurrence. These convergences are suggestive targets, not independent
evidence.
