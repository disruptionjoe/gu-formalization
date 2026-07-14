---
artifact_type: exploration
status: exploration (W133 / H71; 5-persona inline team; one deterministic test; the even-cut inter-family disagreement attacked as a DISCRIMINATOR on three fronts)
created: 2026-07-14
hypothesis: H71 (feeds H59)
branch: "Path-2 wave-5 (Team H71 / W133): can the even-cut +1-vs-0 disagreement between the grading and removal families DISCRIMINATE? Front 1: dispersion/sum rule. Front 2: in-principle observable. Front 3: fork formalization (two quantizations of one Lagrangian)"
title: "W133 VERDICT: CONDITIONAL-DISCRIMINATOR / ABSOLUTE-DECLARATION. (1) DISPERSION FORCES GRADED, CONDITIONALLY: given the real part both families AGREE on (W124 O2, reproduced at the even-cut object with O(Gamma) convergence), the agreed log-bounded asymptotics, Schwarz reality and real-axis-only cuts, the once-subtracted Kramers-Kronig relation selects Im = +1 x the full two-ghost cut -- the GRADED answer -- UNIQUELY within the CLOP band {-1/2, 0, +1/2, +1} (residuals 1.58 / 1.05 / 0.53 / 0.0003 in cut-integral units); confirmed at the true W124 two-loop sunset by twice-subtracted dispersion (ratio 1.0003). Lee-Wick is NOT thereby inconsistent: its absorptive content is RELOCATED to complex-conjugate branch points off the real axis (exhibited: |disc| across the UHP ray through 4a_+ = 2*pi*sqrt(1-4a/s) to 2 percent), i.e. it evades the sum rule by giving up upper-half-plane analyticity, which IS its known microcausality price. (2) THE COMPARISON QUANTITY EXISTS AND IS SYMMETRIC: KL-cone deviation pair (analyticity defect, positivity defect) in units of the full cut at each family's own locus: graded (0, 1), Lee-Wick (1, 0) -- each family saturates exactly one axis by the FULL cut; neither is parametrically smaller; no discrimination. (3) OBSERVABLE: on the fixed-scale branch the two-ghost threshold sits at sqrt(s) = 2 m2 in [6.2, 10.5] meV = SUB-MILLIMETER r* in [19, 32] um, inside the torsion-balance window -- but the family-discriminating imprint is loop-level, relative size (l_Pl/r*)^2 e^{-1} in [9.5e-62, 2.7e-61] (POWER-LAW Planck-squared, not exponential, at the natural radius), ~60 orders below sub-mm sensitivity; graviton-graviton absorptive difference sigma ~ 2e-130 m^2; agravity branch r* ~ 1e-34 m: dead on both branches. The discriminator converts to CONSISTENCY-ONLY. (4) FORK FORMALIZATION: the Lagrangian's residue sign eps = -1 makes KL axioms (A) real-axis analyticity and (P) spectral positivity JOINTLY UNSATISFIABLE (exact arithmetic; eps = +1 negative control satisfies both): the two families are two inequivalent quantizations of the SAME Lagrangian distinguished by a state-space datum -- which axiom survives: keep (A) and grade (Krein C-operator / maximal positive subspace) vs keep (P) and truncate the asymptotic space (pair contour). PHYSICAL-BIFURCATION-DECIDED-BY-STATE-SPACE-DATUM; empirically PERMANENT-DECLARATION at accessible scales. H59 and H71 remain OPEN."
grade: "EXACT for the weight/parity arithmetic, the joint-unsatisfiability statement and the uniqueness argument behind the sum rule (a Schwarz-real function analytic off the real axis with log-bounded growth is determined by its real-axis cut data up to the subtraction polynomial); NUMERICAL-CONTROLLED for every dispersion integral (two routes where feasible: below-threshold no-PV vs above-threshold PV; direct Re vs dispersive reconstruction; tolerances stated in-test); DERIVED-VALIDATED for the continuous-phase bubble evaluator used off-axis (checked against standard quadrature at real-axis benchmarks to 1e-5); ARGUED where marked (the identification of the off-axis dispersion defect with the GOW microcausality cost as the SAME quantity; the (l_Pl/r)^2 normalization of the loop-level potential imprint -- dimensional analysis with the known one-loop scaling, O(1) coefficient dropped; sub-mm sensitivity taken at order alpha ~ 1). Scalar core only (no spin-2 tensor numerators -- W124 Stage C / W134). Test: tests/W133_evencut_discriminator_dispersion.py, 15/15, exit 0, positive controls PC1-PC3 and negative control X2. NO canon / RESEARCH-STATUS / claim-status / verdict / posture change; the proposed fork row is a PROPOSAL only. H59 and H71 remain OPEN."
depends_on:
  - explorations/path2-wave4-target2-two-loop-overlap-selfenergy-2026-07-13.md
  - explorations/path2-wave3-target2-graded-clop-and-target3-hardening-2026-07-13.md
  - explorations/path2-branchB-pt-c-operator-2026-07-11.md
  - explorations/path2-branchD-leewick-2026-07-11.md
  - explorations/landscape-assessment-post-three-waves-2026-07-14.md
  - explorations/wave32/H52-alpha13-boundary-cited-2026-07-13.md
  - explorations/h59-frg-minimal-truncation-krein-negative-ratio-2026-07-13.md
  - papers/candidates/keep-and-grade-loop-cost/keep-and-grade-loop-cost-2026-07-11.md
  - tests/W124_stageA_sunset_graded_vs_LW_CLOP.py
  - tests/W120_path2_target2_keepgrade_vs_clop.py
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W133_evencut_discriminator_dispersion.py
external_refs:
  - "Kallen (1952) / Lehmann (1954) -- the spectral representation whose two axioms (real-axis support, nonnegative weight) are the cone both families deviate from"
  - "Lee & Wick, Negative metric and the unitarity of the S-matrix, NPB 9 (1969) 209"
  - "Coleman, Acausality, in Erice lectures 1969 -- acausal response of Lee-Wick theories"
  - "Grinstein, O'Connell & Wise, Causality as an emergent macroscopic phenomenon, PRD 79 (2009) 105019 -- the bounded microcausality violation of the removal family"
  - "Cutkosky, Landshoff, Olive & Polkinghorne, NPB 12 (1969) 281 -- the CLOP prescription"
  - "Anselmi & Piva, JHEP 06 (2017) 066; PRD 96 (2017) 045009 -- CLOP ambiguity diagnosis; the fakeon average"
  - "Bognar, Indefinite Inner Product Spaces, Springer 1974 -- maximal positive subspaces (the graded family's state-space datum)"
  - "Lee (J. Lee), PRL 124 (2020) 101101 -- sub-mm inverse-square-law tests (sensitivity scale used for the observability estimate, via wave-32 H52)"
---

# Path-2 Wave-5 (W133) -- the even-cut disagreement as a discriminator

**Role.** W124 left the two loop-rescue families in a sharpened standoff: at the even (two-ghost)
threshold they give genuinely different absorptive parts (graded +1, removal 0, in units of the
positive phase-space cut), the CLOP band endpoints are exactly these two answers, and the
intermediates are optical-theorem orphans. The 2026-07-14 landscape assessment named the natural
next question (H71): can this disagreement DISCRIMINATE -- is there a consistency condition or an
in-principle observable that selects one family? This wave attacks it on three fronts with five
personas inline, sequentially. Deterministic test: `tests/W133_evencut_discriminator_dispersion.py`
(15/15, exit 0). Units `M = 1` where dimensionless; all cut statements in the fixed positive
normalization of W120/W124.

## 0. Construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md discipline)

| Object | Constructions in play | Handling |
|---|---|---|
| **The ghost** | (i) keep-and-grade Krein real-mass state; (ii) Lee-Wick conjugate pair | BOTH computed on the same objects; the comparison is the result |
| **Analyticity axiom** | (i) real-axis-only cuts + Schwarz (standard Wightman-descended S-matrix analyticity); (ii) LW full-contour analyticity with conjugate off-axis branch points | The sum rule is computed under (i) and the evasion under (ii) is exhibited, not assumed away |
| **Ghost mass scale** | (i) agravity branch `m2 ~ f_2 M_Pl`; (ii) fixed-scale branch `m2 = sqrt(m2_eff) mu_DW` (GU-native) | BOTH branches priced in the observable front; neither defaulted |
| **Positivity** | Krein-graded optical theorem only | W48 gate discipline: nothing here is loop positivity |

## 1. Persona 1 -- S-matrix/dispersion theorist: the sum rule (Front 1)

**The object.** The even cut appears FIRST at one loop: the two-ghost bubble `b0(s; M^2, M^2)`
(in the graviton self-energy this is the massive-spin-2 pair channel). This is below the CLOP
locus in loop order, but it is the identical structural question: graded weight `(-1)^2 = +1`
gives `Im = +pi*sqrt(1-4M^2/s)`; the LW pair combination has `Im = 0` on the entire real axis at
every width (Schwarz pairing, verified to 1e-7). W124 established the same `+1` vs `0` split at
the two-loop sunset.

**The known agreement.** W124 O2 found the REAL parts of the two prescriptions converge as
`Gamma -> 0`. Reproduced here at the even-cut object itself (D2): `Re Delta_LW` at widths
0.4 / 0.2 / 0.1 / 0.05 is 0.605 / 0.797 / 0.918 / 0.984 against the graded 1.0535 -- monotone,
`O(Gamma)`, Richardson limit 1.0498 (ratio 0.9965). **Both families own the same real part.**

**The sum rule.** For any amplitude that is (i) analytic off the real axis, (ii) Schwarz-real,
(iii) log-bounded at large `|s|` (the asymptotics both families agree on), the once-subtracted
Kramers-Kronig relation determines Im from Re uniquely up to the subtraction constant. So: given
the agreed Re, which member of the CLOP band `{-1/2, 0, +1/2, +1}` does dispersion force?

Computed both ways (D1/D3; positive control PC3 runs the identical machinery on the normal
bubble through two independent routes, below-threshold no-PV and above-threshold PV, agreeing
to 5e-4):

| candidate even-cut weight `k` | dispersion residual (cut-integral units 1.0535) |
|---|---|
| `-1/2` | 1.5802 |
| `0` (LW proper / fakeon average) | 1.0535 |
| `+1/2` | 0.5267 |
| **`+1` (graded)** | **0.0003** |

**The dispersion relation FORCES the graded answer, uniquely, within the band whose endpoints
W124 identified as the only state-space-realizable values.** Confirmed at the true W124 two-loop
object (D5): the twice-subtracted dispersion integral over the graded `Im S` of the sunset
(two subtractions because `Im S ~ s`) reconstructs the directly computed twice-subtracted
`Re S` variation to ratio 1.0003; the LW assignment `Im S = 0` on that cut would reconstruct
zero against a nonzero direct value.

**Where LW's absorptive content went (D4).** The removal family is NOT internally inconsistent.
Its `(++)` pair channel has a genuine branch discontinuity across the ray through `4 a_+` in the
UPPER half plane (numerically: |disc| = 3.559 vs the continued cut formula
`2*pi*sqrt(1-4a/s)` = 3.628, ratio 0.981, via a continuous-phase evaluator validated at real-axis
benchmarks), with the `(--)` mirror in the lower half plane. The content the real axis lost is
exactly relocated to complex-conjugate off-axis branch points. A full-contour dispersion relation
that encircles those cuts is consistent and Schwarz-compatible (the pair is conjugate); what is
given up is upper-half-plane analyticity -- which is, by the standard theorems, microcausality.
That is the removal family's already-priced cost (Lee-Wick, Coleman, GOW), now exhibited as THE
SAME QUANTITY as the even-cut deficit: **the LW dispersion defect at the even cut equals the full
graded cut equals the absorptive weight of its acausal off-axis pair** (ARGUED for the
time-domain identification; the magnitudes are computed).

**Front-1 verdict: FORCES-GRADED-GIVEN-REAL-AXIS-ANALYTICITY / PERMITS-BOTH-ABSOLUTELY.**
The dispersion relation is a discriminator exactly conditional on the analyticity axiom -- and
choosing that axiom is choosing the family (see persona 5).

## 2. Persona 2 -- Lee-Wick specialist: what the removal family pays, precisely

The removal family's `Im = 0` at the even cut is load-bearing for its unitarity story: its
optical theorem is over a ghost-free asymptotic space, and a nonzero two-ghost absorptive part
would have no states to match (that is W124's K1 from their side). Their own consistency
requires exactly three linked features, all confirmed here at the object level:

1. **Real-axis reality of every ghost-containing channel** (L-block of W124; reproduced at one
   loop in D2): no real-axis cut means nothing for the ghost-free optical theorem to disagree
   with.
2. **Conjugate off-axis branch points carrying the displaced content** (D4): the pair must stay
   exactly conjugate (Schwarz), otherwise reality on the axis fails. This is why the CLOP
   deformation intermediates are orphans: they break the pairing.
3. **Renunciation of the real-axis-only dispersion relation** in favor of the full-contour one:
   the price is the bounded microcausality violation, time scale `~ 1/M` for the wide
   gravitational ghost (`Gamma/M = O(1)`, W120's window estimate).

Nothing in Front 1 convicts the removal family of an internal contradiction. What Front 1 does
is close an escape: the removal family CANNOT claim the standard analyticity axioms and its
even-cut answer simultaneously. Before W133 one could imagine both families sharing the standard
dispersion framework and differing only in bookkeeping; the sum-rule computation shows the
framework itself splits with them. The families differ not just in `Im` at a threshold but in
WHICH dispersion relation their amplitudes satisfy.

## 3. Persona 3 -- Krein specialist: the fork formalized (Front 3)

**The exact arithmetic (X1).** The Lagrangian fixes the ghost residue sign `eps = -1`. In ANY
quantization whose absorptive content lives on the real axis, cut weights are products of Krein
signs: even cuts carry `eps^2 = +1`, odd cuts carry `eps = -1`. Spectral positivity of all
real-axis cuts requires `eps = +1`. Therefore the two Kallen-Lehmann axioms

- **(A)** all absorptive content on the real axis (analyticity/microcausality), and
- **(P)** nonnegative spectral weight (positivity)

are **jointly unsatisfiable** for this Lagrangian class -- exact arithmetic, not an estimate.
Negative control (X2): `eps = +1` satisfies both at once and no family split exists; the
bifurcation genuinely tracks the Krein sign.

**The bifurcation.** The two families are two inequivalent quantizations of the SAME local
Lagrangian, classified by which axiom survives:

| | keeps | pays | state-space datum making the choice |
|---|---|---|---|
| **Graded (keep-and-grade)** | (A): dispersion-complete, defect 0 (D1/D5) | (P): odd-cut leak, full cut (W48/W120) | the Krein grading / C-operator = a choice of maximal positive subspace (Bognar; W49/W121: non-local but exponentially localized) |
| **Removal (Lee-Wick)** | (P): ghost-free spectrum, all real-axis weight nonnegative | (A): even-cut content relocated off-axis, full cut (D2/D4) | the truncation of the asymptotic space + the pair contour |

The **KL-cone deviation pair** `(N_A, N_P)` -- the Front-1b comparison quantity the brief asked
for -- is `(0, 1)` for graded and `(1, 0)` for removal, each in units of the full positive cut
at that family's own locus. It is the single ledger where both costs appear; and it is exactly
symmetric. **Neither family's cost is parametrically smaller.** (The magnitudes are not merely
analogous: both equal 1.0 by the same weight arithmetic, and the numerical entries land at
0.9965 and 1.0 with stated tolerances.)

**Connection to W124's CLOP reading.** W124 showed the CLOP band is the removal contour failing
to decide between the families and that only the endpoints are state-space realizable. W133 adds
the axiom-level statement: the endpoints correspond one-to-one to the two satisfiable axiom
choices, `+1 <-> keep (A)`, `0 <-> keep (P)`, and the dispersion relation is the sharp form of
the correspondence. The fork is therefore not a computation awaiting an answer; it is a
**genuine physical bifurcation decided by a state-space datum** the Lagrangian does not supply.

**Proposed fork row (PROPOSAL ONLY -- no canon change here; adding it to
GEOMETER-VS-PHYSICS-OBJECTS.md is a runbook decision):**

> **Object:** ghost-threshold absorptive parts (the even/odd cut assignment). **Standard physics
> construction:** removal/Lee-Wick -- keep spectral positivity, pay bounded microcausality
> (off-axis absorptive content; even cut = 0). **Program-native construction:** keep-and-grade
> Krein -- keep real-axis analyticity/dispersion, pay the graded odd-cut leak (even cut = +1).
> **Determined side + why:** UNDETERMINED as physics (the deciding datum is the state-space
> choice, empirically inaccessible at ~1e-61); but GU's ghost-clearance row is already settled
> native (keep-and-grade), and relative to that declared datum the even cut is +1 -- W133's
> dispersion relation is the consistency condition that makes the declared choice binding.

## 4. Persona 4 -- phenomenologist: the in-principle observable, honestly (Front 2)

**Where the threshold sits.** On the GU-native fixed-scale branch, `m2 = sqrt(m2_eff) mu_DW`
with `m2_eff in [5/6, 5/4]` (W119 fork table) and the resolved `mu_DW` floor band
`[3.4, 4.7] meV` (wave-32 H52): `m2 in [3.10, 5.25] meV`, so the two-ghost threshold is
`sqrt(s) = 2 m2 in [6.2, 10.5] meV`, i.e. length scale `r* = hbar c / (2 m2) in [18.8, 31.8] um`
(P1). **The threshold is geometrically accessible: it sits inside the sub-millimeter window
torsion-balance experiments actually probe.** This is the honest surprise of the front; the
naive expectation was a Planckian threshold.

**What process probes it.** Two in-principle probes of `Im` at `s ~ 4 m2^2`:
(i) the absorptive part of graviton-graviton scattering at meV center-of-mass energies;
(ii) the analytic structure of the loop-corrected static potential -- the two-ghost cut
contributes a spectral term whose Fourier transform is a `e^{-2 m2 r}` tail, present for the
graded family and absent for removal.

**Why the imprint is invisible anyway.** The families share the tree propagator (the pair
combination tends to the real-mass propagator as `Gamma -> 0`), so the tree-level ghost Yukawa
`e^{-m2 r}` -- the O(1) sub-mm signal the H36/H52 exclusion work already prices -- is
**family-independent and discriminates nothing**. The first family-discriminating term is
loop-level (the two-ghost bubble in the graviton self-energy), and gravitational loops carry
`(l_Pl/r)^2`: relative imprint `(l_Pl/r*)^2 e^{-1} in [9.5e-62, 2.7e-61]` (P2; ARGUED
normalization, O(1) coefficient dropped). Two honest observations:

1. The suppression at the natural radius is **POWER-LAW (Planck-squared), not exponential** --
   the brief's guess of "likely exponentially suppressed" is wrong in an interesting way: the
   exponential only takes over for `r >> r*`, and at `r*` the entire cost is the loop factor.
   That does not help: 1e-61 against sub-mm Yukawa sensitivity `alpha ~ O(1)` at 20-30 um is a
   sensitivity gap of ~3.7e60 (P2).
2. The scattering route is doubly dead: `sigma ~ l_Pl^2 (2 m2/M_Pl)^2 ~ 2e-130 m^2` and no
   graviton flux at meV exists to scatter (P3).

On the agravity branch `m2 ~ f_2 M_Pl/sqrt(2)`: `r* ~ 1e-34 m`, no accessible regime at all
(P4). **Front-2 verdict: a clean "unobservably small at accessible scales" -- the discriminator
converts to consistency-only.** The one reusable positive: any future physics that DOES couple
to the graviton spectral function near 10 meV (early-universe graviton thermodynamics, if the
reheating scale ever mattered at meV -- not developed here) would face an O(1) difference in
absorptive weight at threshold, since the +1-vs-0 split is not itself small; only its coupling
into IR observables is.

## 5. Persona 5 -- adversarial skeptic: the no-discrimination steelman

**Steelman.** "Front 1 is circular: real-axis analyticity is not a neutral axiom both families
accept and one fails -- it is the graded family's membership card. Choosing (A) IS choosing
grading; choosing (P) IS choosing removal. Front 1b confirms the symmetry: (0,1) vs (1,0). Front
2 is 60 orders out of reach on the accessible branch and 30 orders of magnitude in length scale
on the other. Therefore: both families are internally consistent, the choice is a quantization
postulate, and no experiment or shared axiom decides it. The fork is a permanent DECLARATION."

**Where the steelman holds.** Almost everywhere, and the verdict says so plainly: there is no
unconditional discriminator. The dispersion relation does not convict removal of inconsistency
(persona 2); the comparison quantity is exactly symmetric (persona 3); the observable is
hopeless (persona 4). Anselmi-Piva's repair (the fakeon average, `Im = 0`) even cures the CLOP
formulation defect that was the removal family's one extra wart, so "removal is sloppier" does
not survive either.

**Where the steelman overreaches, by exactly one step.** "Undecidable by any axiom" is too
strong AS A STATEMENT ABOUT THIS PROGRAM. Three things survive at full strength:

1. **The conditional force is real and novel.** Before W133, "graded gives +1, LW gives 0" was a
   difference of prescriptions. Now: given the real part BOTH families agree on, real-axis
   analyticity forces +1 uniquely within the whole CLOP band. The disagreement is pinned to a
   single named axiom, with the alternative's evasion route exhibited and priced as its known
   causality cost. That is a sharper object than "two prescriptions differ".
2. **The fork now has a decision procedure, even though the decision is a declaration:** state
   which KL axiom survives; everything else (even cut, odd cut, dispersion relation, CLOP
   endpoint, causality bill) follows. Declarations with complete consequence maps are exactly
   what the spec's construction-fork discipline wants recorded.
3. **GU has already made the declaration.** The program's ghost-clearance fork is settled native
   (keep-and-grade, GEOMETER-VS-PHYSICS-OBJECTS.md). Relative to the program's own declared
   datum, the even-cut answer is +1 and the dispersion relation upgrades that from convention to
   consistency condition. A future GU-internal derivation of the C-operator (W49/W121's object)
   would convert the declaration into structure; that is the only visible route to an
   unconditional selection, and it is program-internal, not experimental.

**Skeptic's residue, conceded:** as physics-in-general (the Stelle class, not GU), the honest
answer is PERMANENT-DECLARATION -- the two quantizations are empirically indistinguishable at
accessible scales and axiomatically symmetric.

## 6. Verdict

**W133 VERDICT: CONDITIONAL-DISCRIMINATOR / ABSOLUTE-DECLARATION.**

- **Front 1 (sum rule): FORCES-GRADED-GIVEN-REAL-AXIS-ANALYTICITY / PERMITS-BOTH-ABSOLUTELY.**
  Residuals within the CLOP band: `k = +1` at 0.0003 vs 0.53-1.58 for all alternatives (units of
  the cut integral); two-loop confirmation ratio 1.0003. The LW evasion is exhibited off-axis
  (disc ratio 0.981) and identified with its microcausality price.
- **Front 1b (comparison quantity): CONSTRUCTED, SYMMETRIC, NON-DISCRIMINATING.** KL-cone
  deviation pairs: graded `(0, 1)`, removal `(1, 0)`, each the full cut at its own locus.
- **Front 2 (observable): CONSISTENCY-ONLY.** Threshold at sub-mm `r* in [19, 32] um` (the
  surprise), imprint `~1e-61` relative (Planck-squared power law, not exponential), gap
  `~3.7e60` to sub-mm sensitivity; scattering `~2e-130 m^2`; agravity branch inaccessible.
- **Front 3 (fork): PHYSICAL-BIFURCATION-DECIDED-BY-STATE-SPACE-DATUM** (which KL axiom
  survives: grade the space and keep dispersion, or truncate the space and keep positivity);
  empirically **PERMANENT-DECLARATION** at accessible scales; within GU the datum is already
  declared (keep-and-grade), making the even cut +1 by the program's own settled fork, now
  backed by a dispersion-consistency condition rather than convention alone.

## 7. What this does NOT do

No spin-2 tensor numerators (W124 Stage C / W134 owns those; scalar core only). No claim that
either family is internally inconsistent. No claim of an unconditional (axiom-free or
experimental) discriminator -- the honest answer on both of those fronts is negative and is
stated as such. No time-domain computation of the LW acausal response (the identification of the
off-axis defect with the GOW cost is ARGUED; magnitudes computed). No derivation of the
C-operator from GU structure (named as the only visible route to an unconditional selection).
No canon / RESEARCH-STATUS / claim-status / verdict / posture change; the fork row in Section 3
is a proposal for the runbook, not an edit. **H59 and H71 remain OPEN.**

**Artifacts:** this file + `tests/W133_evencut_discriminator_dispersion.py` (15/15, exit 0).
