---
title: "Path 4 Branch E (adversary / PROSECUTOR) -- per-candidate prosecution arguments, strength-tagged"
status: exploration
doc_type: research_note
updated_at: "2026-07-12"
role: "PROSECUTOR, NOT judge. Presents the strongest honest case against each candidate on {forced, novel, discriminating}. Tags each argument DECISIVE/STRONG/WEAK. Does NOT declare any candidate dead -- the orchestrator weighs these against the constructive evidence and renders the verdict."
verdict: "PRESENTED, NOT DECIDED. See the per-candidate tables. A kill requires a DECISIVE argument; STRONG/WEAK arguments deprioritize but do not close."
depends_on:
  - explorations/path4-other-side-forced-invariant-wave-design-2026-07-11.md
  - explorations/wave18/H34-predictive-content-audit-2026-07-11.md
  - explorations/wave32/H53-falsifiability-audit-2026-07-11.md
  - explorations/wave30/H50-mudw-de-scale-prediction-2026-07-11.md
  - explorations/wave31/H51-dewitt-coefficient-cL-2026-07-11.md
  - explorations/threads/B-omega0-curvature-dark-energy-scoping-and-first-swing-2026-07-11.md
  - explorations/threads/C-discrimination-phenomenology-scoping-and-first-swing-2026-07-11.md
scripts:
  - tests/W65_path4_E_adversary.py
---

# Path 4 Branch E -- the prosecution

**Role discipline (read first).** This branch is the PROSECUTOR. Its job is to build the strongest
honest case *against* each of the four candidate forced-family-invariants, on three axes:
Q-forced (family-invariant, independent of `beta/alpha`, `mu_DW`, `alpha`), Q-novel (not a
re-derivation of known physics), Q-disc (discriminates from LCDM/GR/SM/generic-EFT, ideally testable).
It PRESENTS; it does not decide. Every argument is tagged **DECISIVE** / **STRONG** / **WEAK**, and each
carries an explicit "what would defeat this argument" so the orchestrator can weigh it against the
constructive branches. Over-killing genuine novelty by over-applying "already known" is the failure mode
this role is built to avoid, so WEAK is reported as WEAK.

**Persona team (ran inline, sequential, one context):** (1) skeptic-of-novelty builds each prosecution;
(2) referee grades strength and checks against overreach; (3) steelman-of-the-defense argues the novelty
back so the surviving arguments survive a fair defense; (4) cross-checker verifies each point against the
actual priors (H34/H50/H51/H53, threads B/C); (5) synthesizer assembles the tables below.

**Standing ammunition (repo's own documented deflation tendency).**
- **H34** (predictive-content audit): ZERO parameter-free predictions in the flagship; 4 free params
  (`f0, M2, B_i, mu_DW`); the honest register is **ACCOMMODATION, "compression not prediction."**
- **H53** (falsifiability audit): every empirical channel is `mu_DW`/`f0`-gated; every GU-minus-GR
  deviation `~ (E/m2)^2 -> 0` as `mu_DW -> M_Pl`; **decoupled-in-practice, unfalsifiable-as-it-stands.**
- **H50/H51**: the one principled `mu_DW`-fixing (H36, DeWitt-Lambda = observed DE) forces a sub-mm
  Yukawa `lambda in [60, 74] um` at `alpha=1/3` that is **EXCLUDED** -> the one demonstrated predictive
  channel **self-falsified.**
- **H46/H43**: DE is falsified as a CPL fit (`~3.2 sigma`), marginal-to-viable only as raw BAO distances.

The factual basis of the checkable points below is encoded in `tests/W65_path4_E_adversary.py` (exit 0).

---

## CANDIDATE A -- C3: the EOS x strong-gravity correlation (`w(z)` <-> strong-field, via shared `theta`)

**What the defense claims (steelmanned).** `w(z)` and strong-field gravity both flow from the one shared
`theta` (the II-class), with a *single* coupling `g`. Eliminating `g` yields a forced map `f_0 <-> alpha_W`
(DE amplitude <-> strong-field Willmore-residual coefficient). A correlation is choice-independent *because*
it ties two observables to one object, cancelling the residual scales; and "no other DE theory ties `w(z)`
to a black-hole/strong-field observable" (thread C, C3).

| Axis | Strongest prosecution argument | Strength | What would defeat it |
|---|---|---|---|
| **Q-forced** | The *qualitative* correlation may be forced, but the **discriminating content -- the slope/coefficient `alpha_W(f_0)` -- is gated on `c_W` (OQ2-A), which is source-action-gated (unbuilt)**, and it also carries the residual shape ratio `beta/alpha`. Thread C states the map explicitly: "gated on the single `c_W` (OQ2-A)." So what is forced is "there exists a monotone relation"; what is NOT forced (family-invariant) is the *value* of the relation that would let a measured `wa` predict a number. A bare "two things that share a coupling are correlated" is forced but content-free. | **STRONG** | A proof that `alpha_W(f_0)` is `c_W`-independent AND `beta/alpha`-independent -- i.e. the *slope* survives every family member. Thread C's own scoping says it does not (it is `c_W`-gated). |
| **Q-novel** | **A single scalar sourcing both dark energy and modified/strong-field gravity, with a correlation between the two, is the DEFINING structure of the entire scalar-tensor / Horndeski / f(R) + screening literature** (chameleon, symmetron, Vainshtein all tie a DE-era field to strong-field/fifth-force deviations). "One field -> DE-strong-gravity correlation" is not new; it is the genus. GU's claim is narrower (ONE geometric coupling `g` rather than two independent constants), which is a *sharpening*, not a new kind of statement. | **STRONG** (not DECISIVE) | Show the correlation is *quantitatively rigid in a way generic scalar-tensor is not* -- e.g. GU fixes the ratio with ZERO free constants where Horndeski needs >=2. Right now `g` and `c_W` are exactly the free constants the generic model also has, so the "one coupling" advantage is not yet demonstrated to be parameter-free. |
| **Q-disc** | The strong-field leg is **quadratic in `M`** (RFAIL-03: leading Willmore residual `O(M^2/r^4)=Q(B)`; thread C writes `~M^2/r^6`). Quadratic-in-`M` is the same heavy-field structure H53 showed **decouples**: `~(E/m2)^2 -> 0` at natural `mu_DW` (test A2: `1.3e-81` at LIGO/`M_Pl`). So even if the correlation is real, its strong-field arm is **not an accessible observable** -- you cannot measure the black-hole number that the DESI `wa` supposedly predicts. The cosmology arm, meanwhile, is the H43/H46 DE sector, already `~3-4 sigma` in tension and `f0`-degenerate. | **STRONG** | A concrete strong-field regime where the `M^2` residual is O(1) (near-horizon, not weak-field), with a computed, non-decoupled magnitude at an accessible probe -- turning the correlation into a real joint test rather than "a tiny number correlated with a `3-sigma`-tense number." |

**Honest note (steelman that survives).** The *structural* claim -- that GU welds the DE amplitude and the
strong-field coefficient to ONE geometric object, so they cannot be dialed independently -- is a genuine,
GU-flavored qualitative correlation that a generic two-coupling scalar-tensor model does *not* force. My
best novelty prosecution is **STRONG, not DECISIVE**: I can show the *genus* (one-field DE+MG correlation)
is old, but not that GU's single-coupling *specialization* is old. **This is the candidate I find hardest
to prosecute** -- the correlation-structure could be a real novelty if the constructive branch can exhibit
the slope as parameter-free (which it currently cannot, being `c_W`-gated).

---

## CANDIDATE B -- B1: the O(M^0) intrinsic curvature "subtracted as a convention" = dark energy

**What the defense claims (steelmanned).** The O(M^0) DeWitt background curvature of `Met(X^4)` that the
Willmore arc subtracts "as a normalization convention" is **exactly Lambda-shaped** (fiber trace
`= (1/2) eta_munu`, constant shape-energy density; coefficient `(n-2)/4` forced by `n=4`, not imported).
So "subtract it" is a physical decision about the vacuum energy, not a free gauge; the DE leg has a
geometric origin costing no new field (thread B, B1). Bonus: the H-vs-II (OQ2-A) choice fixes the SIGN of
the Lambda via the DeWitt conformal-mode negative norm.

| Axis | Strongest prosecution argument | Strength | What would defeat it |
|---|---|---|---|
| **Q-forced** | The dimensionless *shape* (`c_L = 3/8`) is forced, but the **physical magnitude is `rho_Lambda = c_L * mu_DW^4` with `mu_DW` FREE** (H24/H50; test B1b: same `c_L`, free `mu_DW` spans `>1e122` in `rho`). A forced dimensionless coefficient times a free scale is **not a forced prediction of the DE value** -- the scale is the free `mu_DW`. And **keeping vs subtracting is not forced**: subtracting a constant background reference is a standard, legitimate choice (Willmore energy is defined up to a reference; vacuum energy up to normal-ordering). Thread B itself concedes sign+magnitude are "gated on OQ2-A and the keep-vs-subtract convention." | **STRONG->DECISIVE** | Show that (a) the family FORBIDS subtracting (no admissible member sets this background to zero) AND (b) the magnitude is fixed without a free `mu_DW`. Both currently fail: H49's Lambda-magnitude no-go (H53 row 11, settled-FAIL) proves a scale-free two-metric action *cannot* contain `Lambda/M_Pl^4 ~ 1e-123` -- the scale must be imported. |
| **Q-novel** | "A constant vacuum term is proportional to the metric with constant density" is the **DEFINITION** of a cosmological constant, not a prediction (test B1a). And the load-bearing sign fact -- the conformal/trace mode is the negative-norm direction -- is the **known Gibbons-Hawking-Perry conformal-factor problem**, cited *in thread B itself*. So both the Lambda-shape and its sign structure are re-statements of known facts about the space of metrics. Net: this is the **cosmological-constant problem relabeled** in DeWitt-metric language. | **STRONG** | Exhibit something the standard cc story does NOT give -- e.g. the magnitude `1e-123` derived (not imported), or a forced sign that discriminates. H53 row 11 already rules out the magnitude route; the sign is OQ2-A-gated, not forced. |
| **Q-disc** | If it is a cosmological constant, it is **observationally indistinguishable from LCDM's Lambda** -- it *is* a Lambda (`w = -1`). It discriminates from LCDM only if it is *dynamical* (the theta/B1 dynamical piece), but that is Candidate A's `w(z)` sector (already `3-4 sigma`-tense), not the static O(M^0) term. As a static term, zero discriminating power. | **STRONG** | Show the O(M^0) term is forced to be dynamical (`w != -1`) with a family-invariant `w(z)`. That collapses B into A and inherits A's tension. |

**Honest note.** The one genuinely non-trivial computed fact is that `c_L = 3/8` falls out of the DIM=4
geometry, not a fit (H51). But a forced *dimensionless* coefficient on a *free* scale is exactly the
H34/H53 pattern: structure without a standing prediction. Prosecution here is **STRONG bordering DECISIVE**
on forced+novel; the defense's only escape is the dynamical (`w(z)`) reading, which is Candidate A.

---

## CANDIDATE C -- B2: the observerse / issuance forced statement (`f_0` as issuance rate; non-collapse identity)

**What the defense claims (steelmanned).** The DeWitt curvature connects to observer-non-collapse: `f_0`
(dark energy) is the "deflationary issuance rate" of an observerse-non-collapse condition, and there is a
hard family-invariant statement (an impossibility theorem, or a rate identity). "The paper only this
program can write" -- highest novelty.

| Axis | Strongest prosecution argument | Strength | What would defeat it |
|---|---|---|---|
| **Q-forced** | **The constructive branch (thread B) itself concedes B2-as-stated is "most likely FALSE."** The repo's own rate-independence finding (FR-series synthesis) proves NO structural GU theorem consumes the rate `lambda`; but `f_0 / alpha_W / c_W` manifestly enter the STRUCTURAL Willmore-EL. Modus tollens (test C1): if `f_0` were a rate it would be rate-independent and drop out; it does not drop out; therefore it is **not a rate**. The "rate identity" is refuted by the program's own result. | **DECISIVE** (for the rate reading) | A NEW structural theorem in which a rate genuinely enters (overturning FR-series). None exists in repo canon; thread B flags this as the exact missing object. |
| **Q-forced (salvage)** | The non-rate reformulation ("background curvature = geometric shadow of a filtered-sheaf non-collapse *obstruction* `O(tau)=H^1`") requires a **map from record filtrations to sections of `Met(X^4)` that DOES NOT EXIST** (thread B step 1: "the map ... does not exist. Without it, steps (2)-(4) cannot even be stated"). So the salvaged statement is not forced -- it is not yet even *stated*. It is a framework sketch, not a theorem. | **DECISIVE** (as a *forced statement*: there is no statement to force) | Construct the filtration->section map and prove the collapse <-> totally-geodesic equivalence quantitatively. Currently absent. |
| **Q-novel** | Whatever novelty exists is the novelty of a **non-existent theorem** -- an analogy (CAP/FLP-style non-collapse <-> geometry) that the FR-series already diagnosed as "**four formally distinct objects wearing one name**." A portmanteau mapping is superficial until the map is built; a rate *identity*, if ever written, would be *definitional* (you define `f_0` as the rate), not predictive. | **STRONG** | A built map + a derived (not defined) identity that emits `f_0 = 0.125` from `|II|^2_V * c_W` WITHOUT fitting (thread B step 3). This is the only step that would make it physics. |
| **Q-disc** | With no forced statement, there is nothing to test; discrimination is undefined. | **STRONG** | Same as above -- needs the built map first. |

**Honest note.** This is the **easiest candidate to prosecute**, and uniquely so because the *constructive*
branch already conceded the literal claim is false and the salvage is blocked on a non-existent map. The
DECISIVE tag here is earned not by my skepticism but by the repo's own rate-independence result plus thread
B's own admission. Caveat honestly logged: I do not have the sibling observerse/temporal-issuance repos;
if one has upgraded rate-independence (found a structural theorem a rate DOES enter), the DECISIVE tag on
the rate reading weakens to STRONG. As of *this* repo's canon, it stands.

---

## CANDIDATE D -- D4: the discrete forced fact (count in `{1,3}`, carrier bit, 4th-order/7-DOF)

**What the defense claims (steelmanned).** Independent of the residual freedom, a discrete choice-
independent fact is forced: the 4th-order/7-DOF graviton property (`mu_DW`-invariant), or the count in
`{1,3}`, or the carrier bit -- a 2-bit prediction surviving the whole family.

| Axis | Strongest prosecution argument | Strength | What would defeat it |
|---|---|---|---|
| **Q-forced** | Split the claim: the **7-DOF property IS forced** (H53 row 5, `mu_DW`-invariant), but the **count is NOT** -- it is `{1,3}`, "not pinned to 3" (H40 residue trap; test D2: `|{1,3}|=2`), and the **carrier bit is NOT forced** (symbol arithmetic cannot decide it -- the `343.73` mutual-exclusion certificate; only the unbuilt SG4 declares it). So the only *forced* discrete fact is the 7-DOF one; the discrete facts that would *discriminate* (count `=3`, carrier `=B`) are source-action-gated. | **STRONG** | A proof that the count is index-forced to 3 (would upgrade `{1,3}` to `{3}`), or that the carrier bit is forced without SG4. Both are open; H34/H40 say they are located-not-forced. |
| **Q-novel** | The one forced discrete fact -- **7 DOF (2 massless + 5 massive spin-2), a 4th-order `box^2` graviton -- is the standard Stelle (1977) higher-derivative gravity spectrum** (test D3). Not novel; it is what *any* curvature-squared gravity has. And the 3-primary localization of the count is **PRIOR ART** (H34: Nielsen-Ninomiya / Callan-Harvey / Kaplan; arXiv:1808.00009). So the forced discrete facts are known, and the novel discrete facts are not forced. | **STRONG** | Show the forced discrete fact is NOT generic Stelle -- e.g. a specific `m2_eff` value or DOF sub-structure that no other 4th-order theory shares AND that is forced across the family. `m2_eff in [5/6,5/4]` is a candidate but is `mu_DW`-gated in every observable. |
| **Q-disc** | **DECISIVE via H53:** the forced 7-DOF property is `mu_DW`-invariant but **not an accessible observable** -- every footprint of the 5 extra DOF is `~(E/m2)^2 -> 0` at natural `mu_DW` (test D1b: `1.3e-81`). So the forced discrete fact is forced-but-decoupled; it discriminates GU from GR *on paper*, never *in an experiment* at natural scale. The count `{1,3}`, being `{1,3}` and not `{3}`, does not discriminate either (it does not predict a number). | **STRONG** (H53 makes the "not-an-observable" leg DECISIVE, but "not discriminating" overall is STRONG because on-paper distinctness is real) | A source-action result forcing `mu_DW` into an accessible window (then the 7-DOF becomes testable) -- but that is exactly the H41 keystone, unbuilt; or forcing the count to 3 (a genuine qualitative discriminator). |

**Honest note.** D is a **pincer**: the forced discrete fact (7-DOF) is known (Stelle) and decoupled
(H53); the discriminating discrete facts (count `=3`, carrier `=B`) are not forced (H40 residue trap, `343.73`
certificate). Neither corner gives forced+novel+discriminating simultaneously. Prosecution is **STRONG**,
short of DECISIVE only because "7 DOF forced and `mu_DW`-invariant" is a *genuine* falsifiable-in-principle
property (H53's own careful PROPERTY-vs-OBSERVABLE split) -- it just is not an accessible observable.

---

## Synthesis for the orchestrator (per candidate: strongest argument x axis, tag, defeater)

| Cand | Q-forced | Q-novel | Q-disc |
|---|---|---|---|
| **A (C3)** | slope `alpha_W(f_0)` is `c_W`+`beta/alpha`-gated, not family-invariant -- **STRONG** | one-field DE+MG correlation is the scalar-tensor genus -- **STRONG** (not DECISIVE) | strong-field arm is `M^2`, decoupled `(E/m2)^2->0` -- **STRONG** |
| **B (B1)** | magnitude = free `mu_DW^4`; subtract-vs-keep is a legit reference choice -- **STRONG->DECISIVE** | "constant ~ eta_munu" is the cc DEFINITION; sign = known GHP -- **STRONG** | a static Lambda is LCDM-indistinguishable -- **STRONG** |
| **C (B2)** | rate reading self-refuted by repo rate-independence; salvage needs a non-existent map -- **DECISIVE** | novelty of a non-existent theorem; portmanteau analogy -- **STRONG** | no statement -> nothing to test -- **STRONG** |
| **D (D4)** | only 7-DOF forced; count `{1,3}` and carrier NOT forced -- **STRONG** | 7-DOF = standard Stelle; 3-primary = prior art -- **STRONG** | forced fact is decoupled/not-observable (H53) -- **STRONG** |

**Hardest to prosecute (most likely genuinely novel): Candidate A (C3).** Its single-geometric-coupling
correlation between the DE EOS and a strong-field coefficient is a real qualitative sharpening that a
generic two-coupling scalar-tensor model does not force. My best arguments against A are all STRONG, none
DECISIVE: I can show the *genus* is old and the *slope* is `c_W`-gated and the strong-field arm decouples,
but I cannot show the single-coupling *tie itself* is a re-derivation of known physics. If the constructive
branch can exhibit `alpha_W(f_0)` as parameter-free (removing the `c_W` gate), A is a live novelty. It
should NOT be killed on my arguments.

**Easiest to prosecute (weakest candidate): Candidate C (B2).** DECISIVE on forced -- but note the
DECISIVE tag is earned by the *repo's own* rate-independence result and thread B's own concession, not by
skeptical hand-waving. The salvage (non-collapse obstruction) is a genuine open direction, but as a
*forced family-invariant* today there is no statement to force.

**Cross-cutting prosecution theme (the H34/H53 spine).** All four candidates live under the same shadow:
the program has a documented reduction to accommodation. A and B route their discriminating content through
the free `mu_DW`/`f0` (H53: `mu_DW`-gated, decoupled) or the unbuilt `c_W`/H41 (H34: the source-action
keystone). C has no forced statement. D's forced fact is decoupled. The prosecution's strongest *unifying*
point is **STRONG**: every candidate's *discriminating* content is gated on the one unbuilt object (the
source action / `mu_DW` / `c_W`), which is precisely H53's "falsifiability rests on H41." That does not
kill any single candidate, but it is why the honest prior remains ACCOMMODATION until H41.

---

*Filed 2026-07-12. Path 4 Branch E (adversary/prosecutor). Factual basis reproduced:
`python tests/W65_path4_E_adversary.py` (exit 0, 13/13). Exploration-grade; PRESENTS, does not decide.
No canon / RESEARCH-STATUS / claim-status / verdict / posture change. Tree left as-is.*
