---
title: "Lost-predictions recovery: (1) the TeV-scale collider-detectable massive state and (2) the exact dark-energy-to-Planck-units ratio — where each was made, its grade, and why it was dropped/superseded"
status: active_research
doc_type: exploration
created: 2026-07-21
directed_by: "Joe direct chat, 2026-07-21 (search-and-recover across gu-formalization + time-as-finality + temporal-issuance and their git history)"
posture: "read-only recovery; report exact locations + why dropped; no verdict/canon/posture movement"
repos_searched:
  - gu-formalization (working tree + full git history, 1168 commits, all branches)
  - temporal-issuance (working tree + full history, 250 commits) — NOTHING FOUND (both predictions absent)
  - time-as-finality (working tree + full history, 679 commits) — connection material only (see Section 4)
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Lost-predictions recovery (2026-07-21)

**Both predictions were REAL, were MADE, and both live in `gu-formalization` (not in
`temporal-issuance`, which has neither, and not natively in `time-as-finality`, which
carries only the cross-program *bridge* for prediction 2).** Neither is refuted.
Prediction 1 is **BLOCKED** (recoverable on named conditions); prediction 2 is a family
of **superseded / downgraded-to-import** derivations, honestly retired to a NO_GO — with
one genuine factor-of-2 numerical hit among them that the repo deliberately does NOT bank
as a GU prediction, for reasons given below.

---

## Prediction 1 — a TeV-scale collider-detectable massive state — **FOUND**

GU's collider-detectable massive state exists in **two related incarnations**, both
grounded in Weinstein's own public claim that the "stuff below the line" (the conjugated
16 + the Rarita-Schwinger sector) is *"luminous, but you haven't seen them yet ... too
massive"* (`papers/drafts/Transcript into the impossible.md`, line 128;
`lab/sources/transcripts/toe-weinstein-gu-40-years.md`, [02:50:38]/[02:51:50]/[02:53:54]).

### Incarnation A — the Rarita-Schwinger (spin-3/2) partner sector ("Candidate B")
- **Where:** `explorations/cycle-gates-and-audits/gu-testable-predictions-2026-06-23.md`
  (§B, lines ~200–234); summarized in `DERIVATION-PROGRESS.md` line 1248 ("Candidate B").
- **What it claimed:** GU predicts a **spin-3/2 (Rarita-Schwinger) partner to each SM
  generation**, Kaluza-Klein-like mass `m_RS ~ sqrt(11)/L`, with a **GU-specific,
  scale-independent mass ratio `m_RS / m_{1/2} = sqrt(11/8) ≈ 1.17`** (from
  `m_RS² = 11/R_s²`, `m_{1/2}² = 8/R_s²`). LHC reach requires `m_RS < 13 TeV`, i.e. the
  curvature scale `L > 0.017 fm`.
- **Grade:** the mass RATIO 1.17 is a genuine GU-specific PREDICTION *conditional on the
  RS sector being kinematically accessible*; the absolute mass is **UNDERDETERMINED** —
  "there is no GU derivation forcing L to be in this range," "not accessible with current
  collider technology if M_KK ≫ TeV."
- **Why dropped/stalled:** the absolute scale is not fixed by GU (same disease as
  everything downstream of the source-action bottleneck), so GU can name *what* and the
  *ratio* but not *at what TeV* — it cannot say the state is in reach. Not refuted;
  falsifiable in principle (discover spin-3/2 partners with a mass ratio ≠ 1.17).

### Incarnation B — the heavy charged vectorlike **mirror generation** (the developed successor)
- **Where (made):** `explorations/big-swing-2026-07-07/BIG-SWING-MIRROR-PREDICTIONS-CHARGED-CONSTRAINED.md`
  (2026-07-07, commit `55fff30` "Mirror-predictions swing: the gapped sector is NOT dark —
  a heavy charged vectorlike mirror generation"); route files `MP-M1`..`MP-M4` in the same
  folder; TaF reading in `explorations/time-as-finality-crosswalk/mirror-as-collective-capability-boundary-2026-07-07.md`
  (commit `923e01f`).
- **What it claimed:** the gapped mirror sector is **not dark** — it is a **heavy, charged,
  colored, VECTORLIKE replica of a full SM generation** (of 96 states: 84 charged, 72
  colored, 12 neutral), quantum-number-identical to the visible generations state-for-state
  (intertwiner `C = -χ_int`, residual 0.0), family count matched (96 = 3×2×16), single flat
  degenerate mass level, and — the one genuine new datum — the undetermined sign bit is
  spectrally invisible. **Collider readout: pair-producible at `√s > μ`, with the constraint
  `μ ≳ 1 TeV`** ("or the mechanism is excluded by colliders"; heavy vectorlike quarks
  excluded to ~1.3–1.5 TeV, cf. `explorations/W239-track-b-distinctive-prediction-scan-2026-07-15.md`).
- **Grade:** MIXED. The carrier-native core (quantum numbers P1/P2, count P3, sign-bit
  invisibility P10) is **THEOREM-grade**, machine-checked in both (9,5) and (7,7). The
  outward collider readout (charged/colored, μ ≳ 1 TeV, producible) is
  **CONSISTENT_UNCOMPUTED / [import]** — it rides the standard SM hypercharge embedding
  (imported, not derived) and an ungated absolute scale.
- **When/why dropped:** logged as a PP3 candidate 2026-07-19 (`c3fb6de`), then
  **BLOCKED at physical producibility on 2026-07-21** — `explorations/mirror-sector-prediction-candidate-disposition-2026-07-21.md`
  (commit `e9bcbe2` "Block the mirror prediction candidate at producibility"). The
  **decisive blocker:** the collider payoff requires the K-negative 96 modes to be
  *physical, producible asymptotic states*, but the same dependency chain
  (`canon/ghost-parity-krein-synthesis.md`) treats those same modes as *negative-norm
  ghosts removed by the Turok-Bateman projector / Born rule* — mutually exclusive fates,
  unresolved. Two subordinate gaps: the absolute scale μ is dynamics-gated (no mass window);
  the SM hypercharge embedding is imported. Reconfirmed in the current consolidated view
  (`explorations/more-predictions-hunt-2026-07-21.md`, Candidate I "BLOCKED_PRODUCIBILITY";
  `explorations/per-leg-recovery-state-2026-07-21.md` "mirror route RESOLVED_NO_GO" as a
  *dark-matter* candidate).
- **Recoverable?** YES, on the four **explicit reopen conditions** in the disposition file:
  (1) a source action selecting the gapping order parameter; (2) a Born-rule decision
  proving the K-negative modes are producible (or retiring the collider observable);
  (3) a native compact SM embedding compatible with the projector; (4) a predeclared mass
  window / kill threshold. All are downstream of the same B5 source-action bottleneck.

**Net for Prediction 1:** GU's "massive state a collider could detect at ~TeV" is real and
not refuted. Its *quantum-number structure and mass ratio* are theorem/prediction-grade; its
*collider detectability* (the "~TeV" part) was asserted (μ ≳ 1 TeV) and then **BLOCKED**,
because GU cannot yet (a) fix the absolute scale or (b) decide whether the states are
producible or projected-out ghosts. Status: **BLOCKED / recoverable**, not refuted.

---

## Prediction 2 — the EXACT dark-energy-to-Planck-units ratio (the DE amplitude) — **FOUND (and this is the important one)**

**The current posture is correct and there is no contradiction to resolve: GU has NO native
DE amplitude.** But the premise of the search is right — GU *did*, at three separate moments,
produce candidate derivations of the ~10⁻¹²⁰ magnitude, including **one genuine factor-of-2
numerical hit**. All three were superseded/downgraded to "import." Here is the full lineage,
oldest to newest, then the honest verdict.

### Route (i) — `Λ_GU = C_GU · ε_sec² / t_obs²` (the GU↔TaF observer-section route, June 2026)
- **Where:** `explorations/time-as-finality-crosswalk/observer-section-error-model-2026-06-23.md`,
  `explorations/time-as-finality-crosswalk/cross-program-gu-taf-coefficient-2026-06-23.md`,
  `explorations/geometry-curvature-emergence/cpa1-tobs-coefficient-2026-06-23.md`; summarized
  `DERIVATION-PROGRESS.md` lines 418 / 581 / 651 / 1248 / 1409.
- **What it claimed:** `Λ_GU = C_GU · ε_sec²/t_obs²` with `C_GU = 8` derived from the
  Willmore-EL Lichnerowicz TT eigenvalue on S⁴ (`l(l+n-1)−2 = 8` at `l=2, n=4`). Under the
  null-ray shot-noise observer model `ε_sec = 1/√(2n) = 1/(2√2)`, the algebraic identity
  `C_GU·ε_sec² = 8·(1/8) = 1` gives the clean cross-program contact **`Λ_GU = λ_max²`**,
  where `λ_max = 1/t_obs` is **TaF's maximal finality rate**. Evaluated as a *prediction*
  (Candidate A, `DERIVATION-PROGRESS` 1248): `Λ_GU = 1/t_obs² = 5.87e-53 m⁻²` vs
  `Λ_obs = 1.089e-52 m⁻²`, **ratio 0.54** — order-of-magnitude.
- **Grade / why dropped:** explicitly graded a **RETRODICTION at order-of-magnitude, not a
  precision prediction.** "The null-ray shot-noise model is not derived from GU first
  principles; the t_obs identification is not uniquely fixed by GU." CONDITIONALLY_RESOLVED,
  reconstruction grade. This is the **direct "static-arena-made-dynamic → TaF" DE-amplitude
  route** — the amplitude is `1/t_obs²`, an observer/finality-time object, not a geometry
  constant.

### Route (ii) — the Sorkin everpresent-Λ "shadow", `Λ·l_p² = 1/√N` (the causal-set volume-conjugate route, July 2026) — **the factor-2 hit**
- **Where:** `explorations/W146-substrate-sweep-theoretical-physics-2026-07-14.md` (§2.1–2.4,
  the load-bearing quantitative leg), with the sign/novelty analysis in
  `explorations/W145-substrate-sweep-mathematics-2026-07-14.md` and the DESI bet in
  `explorations/W147-substrate-sweep-observational-2026-07-14.md`;
  `explorations/W149-substrate-sweep-applied-frontier-2026-07-14.md`. Commits `cbaae18`,
  `b875ebc`, and `e4d9f4a`/`77592c9` ("Preserve orphaned W145 mathematics artifacts").
- **What it claimed (the exact ratio):** using Sorkin's everpresent Λ (Ahmed-Dodelson-Greene-
  Sorkin 2004, PRD 69 103523), `Λ ~ ±1/√N`, `N` = spacetime 4-volume in Planck units.
  With `N_4 = 5.21e243`: **predicted `Λ·l_p² = 1/√N_4 = 1.39e-122`** vs **observed `2.85e-122`**
  → **residual = 3·Ω_Λ = 2.05** (factor ~2); scale `ρ_Λ^{1/4} = 1.87 meV` vs observed
  `2.24 meV` (16%). Called *"a genuine magnitude prediction of the 10⁻¹²², ... the only place
  in either wave where the 10⁻¹²² is an OUTPUT rather than an input,"* the *"strongest
  quantitative result across the W135–W146 sweep."* GU's specific contributions: (a) the
  **Y14→X4 measurement-gated dimension collapse (14→4)** that makes the 4-count come out right
  (a naive Y14 sprinkle gives `1/√N_14 ~ 10⁻⁴²⁷`, wrong by 300 orders); (b) a GU-specific
  normalization target `φ = 1/(3Ω_Λ)² = 0.237`.
- **Grade / why dropped (three honest reasons, all in the source document):**
  1. **de Sitter relabeling (G5 bite):** `1/√N_4 = (R_H/l_p)² = S_dS/π` — the magnitude
     *numerically coincides* with the holographic / Gibbons-Hawking value `Λ ~ 1/S_dS`, so the
     substrate story earns **no novelty** from the magnitude; it relabels Gibbons-Hawking.
  2. **The `1/√N` amplitude law is a pure IMPORT** from Sorkin, not GU-derived (W145:
     leading term `1/√N = π/S_dS` exactly, degenerate with the W138 de Sitter relabel).
  3. **The exact match needs a free fit:** hitting observed `ρ_Λ` requires `φ = 1/(3Ω_Λ)²`
     as one free number — *"so the exact match is a fit, not a prediction; the predictive
     content is whether the (9,5)/gimmel DeWitt-fiber measure DERIVES φ = 1/(3Ω_Λ)²"* — a
     computation that was **named but never completed.**
  What GU keeps from this route is only the **SIGN** (Krein-graded ± of Λ) and the
  fluctuating time-dependence, *not* the magnitude.

### Route (iii) — `μ_DW = the DE scale` (H36) → the self-falsified sub-mm prediction (July 2026)
- **Where:** `explorations/wave30/H50-mudw-de-scale-prediction-2026-07-11.md` (commit `71462bc`,
  "GU's FIRST parameter-linked prediction ... SELF-FALSIFIED-AT-FACE-VALUE").
- **What it claimed:** identify the O(M⁰) DeWitt-Λ with the observed DE density, pinning the
  one GU scale `μ_DW = (ρ_Λ)^{1/4} ~ 2.3 meV`. GU's graviton-mass link then *predicts* a sub-mm
  Yukawa (`α = 1/3`, range `λ ∈ [76.7, 94.0] µm`).
- **Grade / why dropped:** the identification is a POSTULATE (ranker H36, tagged `[wild]`),
  not GU-forced; the **H49 Λ-magnitude no-go** (COMPUTED, "settled-FAIL", cf.
  `explorations/two-track-persona-sweep-2026-07-11/*` and `path4-branchE`) proves a scale-free
  `g`-vs-`G` action **cannot** contain `Λ/M_Pl⁴ ~ 1e-123` — the meV scale must be **imported**.
  Under the postulate, the sub-mm prediction is **EXCLUDED by Eöt-Wash/HUST at face value**
  (H52 CITED). So the only way to make a *number* was to import `ρ_Λ`, and importing it then
  self-falsifies the associated gravity prediction.

### The formal closure (why all three are now "import", 2026-07-15 → 07-21)
- `explorations/pred-norm-rank-2026-07-15.md` (**PRED-NORM-RANK, RESOLVED_NO_GO**): the built
  GU normalization structure has rank-3 rescaling freedom / a 4-dim invariant quotient and
  **fixes no native absolute value** for `μ_DW` or the DE amplitude; the "H36 dark-energy
  density lock" route is **killed as a native prediction** because it uses observed `ρ_Λ` to
  solve for `μ_DW`.
- `explorations/de-amplitude-audit-2026-07-20.md` (commit `9e532b9`): *"The dark-energy
  amplitude in GU is a PURE IMPORT ... no amplitude prediction exists."* The `~10⁻¹²³ M_Pl⁴`
  number (`ρ_Λ^{1/4} ≈ 2.24 meV`) is confrontation data seated in the blocked **B5 slot**.
- `canon/dark-energy-theta-divergence-free.md` (line 96): GU solves the 120-orders problem
  **STRUCTURALLY** (why Λ is not forced-constant / not fine-tuned — the theta field is
  G-equivariant, not a constant) but **not quantitatively** (it does not produce the number).
- `explorations/comparative-tensions-ledger-cosmo-gravity-2026-07-21.md` (line 86) and
  `...-qg-toe-2026-07-21.md` (§4): the ledger **cedes the magnitude axis to causal-set theory**
  — *"causal sets nailed the magnitude ahead of data; GU is silent on magnitude and sharp on
  sign ... GU has no native Λ amplitude — OPEN/imported, 'as brute as Λ'."*

### The honest state of whether GU ever had a real DE-amplitude / Planck-ratio prediction
**GU never had a genuine NATIVE exact-ratio prediction of the DE amplitude.** It had three
candidate derivations that each *reproduce* ~10⁻¹²⁰ (routes i, ii, iii), and route (ii)
lands within a factor of 2 — but every one of them either (a) numerically **coincides with a
de Sitter / holographic relabel** (`Λ ~ H²`, `1/√N = S_dS/π`, `Λ_GU = 1/t_obs²` are all the
same "`Λ ~ H²`" coincidence, which is why none is novel), (b) rides an **imported law**
(Sorkin's `1/√N`) or an **imported scale** (`ρ_Λ` into `μ_DW`), or (c) requires an
**uncomputed free normalization** (`φ`, `ε_sec`, the null-ray model). The repo's own audits
(PRED-NORM-RANK NO_GO; the H49 magnitude no-go; the de-amplitude audit) formally retired the
native route. **So the current "GU imports the DE amplitude" posture does not contradict a
prior prediction — it is the honest supersession of three prior *attempts*, none of which ever
reached prediction grade.** The one thing GU genuinely renders non-brute is the DE **sign**
(PP1: `w ≥ -1`, no phantom crossing), never the magnitude.

**Recoverable?** Only the everpresent-Λ route (ii) has a named, non-refuted reopening: derive
`φ = 1/(3Ω_Λ)²` from the (9,5)/gimmel DeWitt-fiber measure AND derive the 4-count natively
(rather than assume the Y14→X4 collapse). Until then it stays a fit-plus-import. Routes (i)
and (iii) are retired (the observer model / `t_obs` are not GU-fixed; the μ_DW=DE identity
self-falsifies).

---

## Does either connect to the causal-set volume-conjugate / TaF–TI dynamic picture? — **YES, prediction 2 does, on both sides**

Joe's context clue is confirmed exactly:
- **Causal-set volume-conjugate (Sorkin):** route (ii) *is* the Sorkin everpresent-Λ
  picture — Λ conjugate to spacetime 4-volume `V`, `ΔΛ ~ 1/√V ~ 1/√N`, `N ~ V` in Planck
  units, giving ~10⁻¹²⁰. Made explicit in `explorations/comparative-tensions-ledger-qg-toe-2026-07-21.md`
  (§4, "`ΔΛ ~ 1/√V ~ 1/√N`") and worked in `explorations/time-as-finality-crosswalk/fr1-sorkin-absorption-worked-check-2026-06-22.md`.
- **TaF dynamic finality:** route (i) is a **GU↔TaF cross-program bridge** —
  `Λ_GU = λ_max²`, where `λ_max = 1/t_obs` is TaF's maximal finality/service rate
  (`cross-program-gu-taf-coefficient-2026-06-23.md`, `observer-section-error-model-2026-06-23.md`).
  This is literally "the static arena made dynamic": the DE amplitude expressed as an
  observer/finality-time object.
- **TI issuance:** the W145/146 reframe casts dark energy as the **shadow of record-accretion**
  (Y14 record growth, measurement-gated Y14→X4 promotion) — and the repo **explicitly routes
  the semantics cross-repo**: *"capability MEASURE = TaF; record/issuance/finality semantics =
  temporal-issuance + time-as-finality; GU owns the substrate MATH only"* (W145 grade line).
  So the DE-amplitude material is exactly the piece that straddles the GU / TaF / TI split.

Prediction 1 also has a minor TaF reading (`μ ~ 1 TeV` = the individual↔collective capability
threshold made physical, `mirror-as-collective-capability-boundary-2026-07-07.md`), but its
home and its blocker are entirely GU-internal.

---

## Where I searched (honest coverage)

- **`gu-formalization`** (primary): working tree + full git history (1168 commits, all
  branches); `git log -S` for TeV/collider/LHC/CERN/resonance and 10^-120/10^-122/everpresent/
  1/sqrt(N); deleted-file scan (`--diff-filter=D`); direct reads of every load-bearing file
  cited above. Both predictions live here.
- **`temporal-issuance`**: working tree + full history (250 commits). **NOTHING FOUND** —
  `git log -S` returned zero for TeV/collider/LHC/GeV and for 10^-120/10^-122/vacuum
  energy/(10^-3 eV)/sqrt(N)/Sorkin-fluctuation across all commits. Dark energy appears only as
  a *qualitative* "governed issuance rate" hypothesis (`E147`) and as an *external* absorber /
  GU-cross-check (entropic gravity; GU's DE field), every quantitative GU/Weinstein DE and
  particle-spectrum result explicitly marked "cannot be imported." Neither prediction was ever
  present in TI.
- **`time-as-finality`**: working tree + full history (679 commits, all branches, deleted
  files). **NOTHING FOUND** — `git log -S` returned zero for TeV/collider/LHC and for
  10^-120/10^-122/vacuum energy/cosmological constant/1/sqrt(V)/Sorkin-fluctuation across all
  commits. TaF only *assesses* GU's particle/DE claims and explicitly refuses to adopt them
  (`explorer-weinstein-ucsd-2025-taf-cross-repo-check`, graded PERIPHERAL / "no claim status
  changes"); its issuance-rate work (`explorer-optimal-issuance-rate-curve-2026-06-22.md`,
  Route D) explicitly declines to derive cosmology or a dark-energy number; all Sorkin
  references are to quantum-measure / causal-order, never the 1/√V Λ-magnitude. So neither
  prediction was ever *made* in TaF. What TaF *does* host is the **finality-rate half of the
  route-(i) bridge** (`λ_max = 1/t_obs`); the GU↔TaF identity `Λ_GU = λ_max²` and both
  predictions themselves live on the GU side (the crosswalk files are in gu-formalization).

## Boundary
Read-only recovery. Only this file was written; no other file edited, no probe, no commit, no
push, nothing external. No claim-status, canon-verdict, portfolio, LANE-STATE, PP1/PP2/PP3, or
public-posture change. All verdicts quoted (`BLOCKED_PRODUCIBILITY`, `RESOLVED_NO_GO`,
`SELF-FALSIFIED-AT-FACE-VALUE`, the de Sitter-relabel bite, "amplitude is a pure import") are
**consumed as found, not moved.**
