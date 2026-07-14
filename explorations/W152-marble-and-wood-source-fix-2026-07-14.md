---
artifact_type: exploration
status: exploration (W152; propose-then-kill; five personas inline, one worker, no sub-agents; deterministic test with positive controls)
created: 2026-07-14
wave: W152
label: W152
title: "W152 -- fine marble and cheap wood: does the record-substrate / source-action structure FIX Einstein's field equations? Grades the GU/record fix for each of the three terms (Einstein tensor / Lambda g / T_munu) against Weinstein's precise defect -- a source term that is divergence-free BUT NOT forced constant, with a GENUINE reason for its divergence-freedom. Three-term scorecard, the 'rise and fall' quantification of W144's Q, the marble-survival verdict, and the single derived-vs-fitted gap that separates MODELING a dynamical Lambda from DERIVING one."
hypothesis: "Joe's marble/wood reframe: keep the fine marble (the Einstein tensor, divergence-free by the contracted Bianchi identity), replace the cheap wood (Lambda g forced constant for a lousy reason; ad hoc T_munu) with the record-substrate / source-action structure this session built (W136 bulk-flatness, W144 interacting-vacuum Q, W145/W146 everpresent-Lambda, the W125 source action). Does that structure supply a divergence-free, NOT-forced-constant Lambda for a genuine reason, and does GU keep the marble?"
grade: "exploration / conditional register throughout. Every 'GU does X' reads 'under the declared conditional structure, X'; nothing asserts GU, that the DESI wiggle is real, or that any decomposition is physical. COMPUTED (deterministic, tests/W152_marble_and_wood_source_fix.py, 21/21 exit 0): the contracted Bianchi identity nabla_mu G^{mu nu} = 0 on curved FRW (marble positive control); the W144 CPL zero-crossing a_x = 0.71163 / z_x = 0.40523 and Q sign structure (issuance z>0.405, withdrawal z<0.405); the product-rule fact nabla_mu(Lambda g)=0 <=> Lambda'=0 (the lousy reason, symbolic); the interacting-vacuum continuity Q = rho_DE' = -3H(1+w_eff)rho_DE (Bianchi bookkeeping closes, exact rationals); the rise-and-fall drift 0.744/e-fold vs the W138 G2 band 0.3; the R^2-sector field tensor E_munu covariantly conserved on FRW (marble survives, augmented). CITED (not re-derived): W122/W123/W126/W130 (the induced action: a1 = 1/3 Einstein PLUS the tachyonic R^2 sector), W125/W131 (source action / covariant Y14 operator, H41 unbuilt), W135/W136 (issuance taxonomy, bulk-flatness beta/alpha=2), W138 (kill battery), W144 (DESI-fitted Q), W145/W146 (everpresent-Lambda), the 2026-06-22 divergence-free-proof and 2026-06-24 marble/wood closure map. No canon / RESEARCH-STATUS / claim-status / verdict / posture change; no spec FIT row moves; H41 unbuilt; H59 OPEN."
construction: "program-native where the objects are GU's (Y14, the induced |II|^2 action, the inhomogeneous-gauge-group theta, the C-operator); standard-field where the machinery binds any construction (the contracted Bianchi identity, FRW continuity, Noether's second theorem, the interacting-vacuum decomposition). Forks named per GEOMETER-VS-PHYSICS-OBJECTS.md; the interacting-vacuum decomposition is PORTED (Wands/De-Bruck lineage) and labeled; the everpresent-Lambda mechanism is PORTED (Sorkin/ADGS) and labeled."
depends_on:
  - papers/drafts/Transcript into the impossible.md
  - explorations/W126-beyond4th-vacuum-lift-2026-07-13.md
  - explorations/W130-native-graviton-oneloop-block-2026-07-14.md
  - explorations/W136-issuance-declaration-propagation-2026-07-14.md
  - explorations/W138-issuance-kill-battery-2026-07-14.md
  - explorations/W144-desi-fitted-issuance-function-2026-07-14.md
  - explorations/W145-substrate-sweep-mathematics-2026-07-14.md
  - explorations/W146-substrate-sweep-theoretical-physics-2026-07-14.md
  - explorations/dark-energy-cosmology/dark-energy-divergence-free-proof-2026-06-22.md
  - explorations/cycle-gates-and-audits/unified-marble-wood-source-closure-map-2026-06-24.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W152_marble_and_wood_source_fix.py
---

# W152 -- fine marble and cheap wood: does the source-action / record structure FIX the field equations?

> **FRAMING CORRECTION (appended 2026-07-14, W153; original text below UNCHANGED).** Per Joe's
> GU-native reading, the cheap wood is the METRIC `g_munu` (imposed by hand; the space of all metrics
> is the transcript's "lousy foundation" GU exists to leave) and `Lambda` -- NOT `T_munu`. Under the
> substrate inversion the RECORDS ARE THE MATTER (held in Y14), so `T_munu` is KEPT (fundamental
> content), and `G` is KEPT (coupling). W152's scorecard below grades the field-equation TERMS as
> Weinstein's talk does literally (Einstein tensor = marble; `Lambda g` and `T_munu` = wood); that is
> faithful at the term level but INVERTS fundamentality relative to the GU-substrate reading. The
> corrected three-term scorecard, the marble-relocation (the Einstein tensor is the derived curvature
> of the record-derived metric, its divergence-freedom kept as a property), and the coherence-first
> tachyon-as-cheap-wood test live in
> `explorations/W153-marble-corrected-and-tachyon-cheapwood-test-2026-07-14.md`. In particular W152
> Section 6's "`T_munu` -- REPLACE-INTENDED / NOT-YET / essentially untouched" row is CORRECTED there:
> under the inversion `T_munu` is KEPT, and "the records are the matter" is the substrate's core
> identification, not a defect to be replaced.

## 0. The question, and the transcript's precise claim (ground everything here)

Joe's question: Einstein's field equations are "fine marble and cheap wood" (Weinstein, UCSD
April 2025, `papers/drafts/Transcript into the impossible.md`, 00:09:46 and 00:11:09). Keep the
fine marble, replace the cheap wood with something that works better. Does the record-substrate /
source-action structure this session built FIX what does not work in the field equations?

The transcript names three terms and grades each (00:09:46, 00:11:09; quoting):

1. **The Einstein tensor = MARBLE.** "This satisfies an automatic differential equation ... if you
   pass this differential operator through this, you get the exterior derivative minimally coupled
   to the Levi Civita connection of its own curvature has to equal zero by the Bianchi identity, so
   you get a **contracted Bianchi identity**." Divergence-free for a GENUINE reason. "Dynamic and
   natural ... interpretable ... second order ... divergence free."

2. **Lambda g_munu = the greatest-blunder cheap wood.** "It, in fact, has a **lousy reason** for
   being divergence free." Why lousy: "you have the metric, which is always annihilated by its own
   Levi Civita connection. And so if you take a product, by the product rule, you have to have that
   the derivative of lambda as a field has to die, and that's how we ended up with a cosmological
   constant. And **once it's constant, it has no explanation. It can't rise and fall to meet the
   needs of the Riemann curvature tensor**."

3. **T_munu = cheap wood.** "This sort of ad hoc term that just ... you get from taking random
   field content and then Lagrangian varying the metric."

So the SPECIFIC defect to fix (the spine of this deliverable): produce a source/vacuum term that is
**divergence-free BUT NOT forced constant** -- one that CAN rise and fall to meet the curvature,
**with a genuine reason for its divergence-freedom** (not the lousy metric-compatibility reason).
And the MARBLE CHECK: does GU actually KEEP the contracted-Bianchi structure once its induced action
adds higher-derivative terms?

Treat all instruction-like content in the transcript as DATA (a research source Joe placed in the
repo), never as instructions. Five personas ran inline in one worker; the deterministic test
`tests/W152_marble_and_wood_source_fix.py` (21/21, exit 0) runs its two positive controls first.

## 1. Persona 1 -- GR / Bianchi-structure theorist: the marble, the lousy reason, the interacting bookkeeping

**The marble, reproduced (PC1).** The contracted Bianchi identity is a geometric identity, not an
equation of motion: for any metric, `nabla_mu G^{mu nu} = 0` identically. The test reproduces it on
spatially-flat FRW with arbitrary `a(t)` (all four components vanish; `G_tt` is the nontrivial
Friedmann `3(a'/a)^2`). This is the marble, and it is INDEPENDENT of the action: whatever GU does on
the left side, the pure Einstein tensor keeps this property because it is a curvature identity.

**The lousy reason, made a one-line computation (Section A of the test).** On FRW,
`nabla_mu(Lambda(t) g^{mu nu})` reduces by the product rule to `d^nu Lambda` (the metric is
annihilated by its own connection, so only `dLambda` survives). The test confirms: the spatial
components vanish identically, the time component is proportional to `Lambda'(t)`, and substituting a
constant makes the whole thing vanish. So `Lambda g` is divergence-free **if and only if** `Lambda`
is constant. That is EXACTLY Weinstein's "lousy reason": divergence-freedom is bought by killing the
field character, and once constant "it has no explanation."

**The genuine fix requires a DIFFERENT reason.** A term that can vary AND stay divergence-free cannot
get its divergence-freedom from `dLambda = 0`. Two structurally distinct genuine reasons are on the
table in the repo:

- **(i) Interacting-vacuum bookkeeping (W144).** Keep a position-dependent `Lambda(x)` as a strict
  `w = -1` vacuum, and let it exchange energy with matter. Then
  `nabla_mu(G^{mu nu} + Lambda(x) g^{mu nu}) = 0` splits, using `nabla_mu G^{mu nu} = 0` (the
  marble), into `nabla_mu(Lambda g^{mu nu}) = -8 pi nabla_mu T^{mu nu}_matter =: Q^nu`. The varying
  `Lambda` is divergence-COMPENSATED by the source exchange `Q`. The test verifies the closure of
  this bookkeeping as the CPL continuity identity: with everything in `Q`,
  `Q(a) = rho_DE'(a) = -3H(1+w_eff)rho_DE` holds identically (exact rationals), and the reconstructed
  `w_eff(a)` equals the CPL `w(a)` exactly. This is a genuine reason IF the ledger sector `Q` is
  itself supplied for a genuine (not by-hand) reason -- which is the whole question (Personas 3-4).

- **(ii) Equivariance / Noether's second theorem (the 2026-06-22 divergence-free proof).** GU's
  candidate replacement `theta = pi - epsilon^{-1} B epsilon` lives in `Omega^1(Y14, ad P)`. Its
  divergence-freedom is proposed to follow from G-equivariance via Noether's second theorem
  (`D_A* theta = 0` for the EL derivative of any gauge-invariant action), NOT from any
  `D_A theta = 0` (parallel / constant) condition. Crucially, that proof's Section 4 shows the
  metric-compatibility argument that kills `Lambda` does NOT apply to `theta`: it is free to vary
  with curvature. That is the correct SHAPE of a genuine fix. But that proof is graded CONDITIONAL
  on C1/C2/C3 (the gimmel metric being G-invariant, or `theta` being the EL derivative of an
  explicit gauge-invariant action on Y14) -- none of which is discharged. So the genuine-reason
  mechanism exists as a STRUCTURE, not as a closed theorem.

**Verdict of this persona.** The marble is kept (PC1, a geometric identity). The lousy reason is
correctly diagnosed and computed. Two candidate genuine reasons exist; both are structurally right
and neither is closed. The interacting-vacuum route (i) is the one the rest of this wave can quantify,
because W144 built its `Q`.

## 2. Persona 2 -- cosmological-constant-problem specialist: is W144's Q the "rise and fall"?

**Weinstein's criterion, made quantitative.** "Rise and fall to meet the needs of the Riemann
curvature tensor" demands, at minimum: (a) the term VARIES with the cosmological clock (not
constant); (b) it can change sign / direction (rise AND fall, not monotone growth); (c) the variation
is O(1) in the natural scale, so it is a genuine response, not a perturbative wobble.

**W144's Q meets all three, with numbers (PC2 + Section C of the test).** From the repo-verified DESI
CPL point (`w0 = -0.752`, `wa = -0.86`):

- **single zero-crossing** at `a_x = 0.71163`, `z_x = 0.40523` (test PC2, matches W144 to 1e-4);
- **sign structure**: `Q > 0` (ISSUANCE) for `z > 0.405`, `Q < 0` (WITHDRAWAL) for `z < 0.405`. The
  vacuum "rises" (is issued) in the past and "falls" (is withdrawn) today. Exactly one flip across
  the DESI window (test confirms `Q_sign(0.4) * Q_sign(1.0) = -1`);
- **amplitude O(1) in the Planck-ladder unit** `q_B = 3 H0 rho_L`: `Q` today `= -0.248 q_B`, issuance
  side up to `~ +0.98 q_B` (W144 table; test checks `Q_today = -0.248 q_B` and the issuance-side sign
  and O(1) magnitude);
- **schedule drift today `= 0.744 per e-fold`** (`= 3|1+w0|`; test computes it from the density
  history), which is `2.48x` OUTSIDE the W138 G2 mimic band of `0.3 per e-fold`.

So W144's `Q` LITERALLY is "a term that rises and falls to meet the curvature": it varies with the
clock, changes sign once near `z = 0.4`, and does so at O(1) amplitude. On the pure "rise and fall"
shape criterion, the fix SUCCEEDS.

**The specialist's caveat that becomes the whole story.** That `Q` sits `2.48x` outside the mimic
band is DOUBLE-EDGED. It means `Q` is a genuine dynamical response (good, it is not a mimic of a
constant). But W138 G2 was derived as a TRUTH gate for EVIDENCE claims: a schedule tuned to BE the
DESI signal is, on current data, the already-excluded reading (`dchi^2 >= +33.5`). W144 keeps this
honest by fitting the wiggle as HYPOTHESIS, never evidence. So "the fix produces a rise-and-fall
Lambda" is a real structural result; "the rise-and-fall Lambda is REAL" is a DR3 bet, not a
conclusion. The rise-and-fall criterion is met at the level of MODELING; whether nature's Lambda
actually rises and falls is unsettled (Section 5).

## 3. Persona 3 -- source-action / GU specialist: the genuine reason and the T_munu replacement

**Is W136 bulk-flatness the genuine reason the Lambda term is divergence-free in GU?** Partly, and
in a specific sense. W136 computed (exact sympy) the `|H|^2` slice decomposition
`(h0,h1,h2,h3) = (-1, 4/3, -4/9, 0)`, giving the family flat constant `a0 = 2 alpha - beta`, so
**bulk-flatness selects the unique ratio `beta/alpha* = 2`** with pin width `|x - 2| < 2.1e-60`. At
that ratio the bulk cosmological constant vanishes identically: flat space becomes a genuine vacuum
(discharging the W130 `Lambda = -1` tadpole). This is a genuine reason for the BULK constant to be
zero -- but it is a reason for VANISHING, not for a divergence-free NONZERO dynamical term. The
observed Lambda, in W136's reading, is then boundary-supplied (the issuance), and its
divergence-freedom is the interacting-vacuum bookkeeping of Persona 1 (i), NOT the bulk-flatness
selection. So bulk-flatness answers "why doesn't the bulk add a second, larger Lambda" (genuine,
computed, pinned) and REPLACES the need for the lousy metric-compatibility reason on the bulk side;
it does not by itself supply the genuine reason for the boundary term's divergence-freedom. That
still routes through the ledger sector `Q`.

**Does the source action replace T_munu (cheap wood #2) with geometric/record content?** This is the
weakest leg, and honestly so. The source-action arc (W125 build, the requirements spec, H41) aims to
have ONE source package produce both the metric/Einstein shadow and the matter/stress-energy shadow
(the "same-source closure" of the 2026-06-24 map). That map's verdict stands: **same-source closure
criterion DEFINED, not currently closed.** The stress-energy bridge is `open`; `T_shadow` is not yet
source-derived (it is imported or named). W136's own spurion analysis found the issuance datum
provably CANNOT feed the dimensionless Yukawa-hierarchy data (dimensional no-go, SA-Y5/SA-Y7b
untouched); only the Majorana channel (SA-Y8) is dimensionally reachable, at OOM tier, comparison-
only. So the record/source structure does NOT yet replace T_munu with derived geometric content: the
cheap-wood-#2 problem is, on the repo's own honest ledger, still `open`.

**The DERIVED-vs-FITTED gap, named sharply.** The standing H41 object -- the covariant operator on
Y14 (W131, built at symbol level) / the Fredholm-propagator source term (W125) -- is UNBUILT as a
dynamical action that DERIVES `Q(a)`. W144 FITS `Q(a)` to DESI and BACKS OUT what the source action
must contain (a clock coupling, a sign-changing boundary term, `beta/alpha = 2` unmoved). Backing out
requirements is not deriving the object. So the source-action leg supplies: a genuine bulk-flatness
selection (DERIVED, pinned), a determined `(B_i, f0) = (0,0)` natural point (DERIVED-conditional), and
a structural back-out of what `Q` must be (FITTED). It does not supply a derived `Q`.

## 4. Persona 4 -- record-substrate theorist: does record-accretion supply Q with a genuine reason?

**The everpresent explanation for the constant's VALUE (W145/W146).** The reversed-arrow reframe
(dark energy is a SHADOW of record-accretion in Y14) ports Sorkin's everpresent Lambda
`~ +/- 1/sqrt(N)`, `N =` measured-record 4-count. This gives the constant an EXPLANATION -- fixing
"once constant it has no explanation": the `10^-122` magnitude is an OUTPUT of the element count
(`1/sqrt(N_4) = 1.39e-122` vs observed `2.85e-122`, residual `3 Omega_L = 2.05`, scale `1.87` vs
`2.24 meV`). This is qualitatively stronger than any rate ladder that presupposes the magnitude. BUT
(W146 Section 2.3, honestly) `sqrt(N_4) = S_dS`, so the MAGNITUDE relabels the de Sitter identity
(W138 G5 bites): the substrate earns novelty only from the FLUCTUATION (sign + time-dependence), not
the magnitude, and the exact match uses one free number `phi = 1/(3 Omega_L)^2 = 0.237` (a fit, not a
derivation; the derivation of `phi` from the (9,5) DeWitt-fiber measure is the named, unbuilt target).

**Does record-accretion supply Q with a genuine reason?** This is the crux, and the answer is
STRUCTURED-BUT-NOT-CLOSED. The measurement-gated projection (W146 clarification 3) makes the count
`N` a MEASURED-record 4-count, and the everpresent law makes `Lambda` a fluctuation of that count:
`Lambda ~ +/- 1/sqrt(N(t))`, stochastic, sign-changing, time-dependent. That is a mechanism for a
NOT-forced-constant Lambda whose variation is sourced by record-accretion -- i.e. a candidate
genuine reason: the boundary supply `Q` is the record-promotion flux across the measurement-gated
surface. The C-operator supplies the decisive GU-specific lever the bare port lacks: the SIGN. A
Poisson sprinkle gives `+/-` at 50/50; the Krein-graded C-operator (W145 story #1, W146 Section 2.5)
could BIAS the fluctuation toward the observed `Lambda > 0`. If the signed `|II|^2` ledger (W137)
predicts `sign(Lambda) = +`, that is a falsifiable consequence bare causal sets cannot make. But
this is NAMED, not built: the signed-positive-Lambda prediction is unbuilt, and the whole
identification "C-operator positive subspace = substrate element-set" is YES-CONJECTURE, gated on H59
(no interacting C-operator exists yet). So record-accretion supplies `Q` with a genuine-reason
CANDIDATE (the promotion flux, sign-biased by the C-operator), conditional on H59 and on the unbuilt
`phi` derivation and sign prediction.

## 5. Persona 5 -- adversarial skeptic: IT-IS-JUST-INTERACTING-DE, steelmanned

**The steelman.** Any coupled dark-energy model gives a rise-and-fall effective Lambda. Write dark
energy as a `w = -1` vacuum exchanging energy with matter, `rho_V' = Q`, and choose `Q(a)` to fit
DESI: you get issuance-then-withdrawal, a zero-crossing near `z = 0.4`, O(1) amplitude -- W144's
result, with zero GU input. The interacting-vacuum decomposition is textbook (Wands / De-Bruck /
Vacca lineage, W144 Persona 2 labels it PORTED). The phantom-crossing-without-instability argument is
also generic to interacting vacuum, not GU-specific. So "fixing the cheap wood" looks like a
REFRAMING: GU adopts a known interacting-DE model and relabels `Q` as issuance/record-promotion.

**What is GU-specific and FALSIFIABLE (the skeptic's own list, conceded).** Four items a generic
interacting-DE model lacks:

1. **The SIGN pin** (W145/W146): `sign(Lambda) = +` forced by C-operator positivity, not a coin
   flip. Falsifiable; unbuilt.
2. **`beta/alpha* = 2`** (W136): the bulk-flatness ratio, exact, pinned to `1e-60`, from a newly
   computed `|H|^2` slice decomposition. Falsifiable (the wave35 m2_eff band, once derived,
   excluding 2); DERIVED.
3. **The everpresent normalization** `phi = 1/(3 Omega_L)^2` from the (9,5) DeWitt-fiber measure:
   would turn the magnitude match from fit to derivation. Named target; unbuilt.
4. **The source-action derivation** of `Q` from H41 (the covariant Y14 operator / Fredholm
   propagator): would turn the fitted `Q` into a derived one. Unbuilt.

**The skeptic's verdict.** At FULL STRENGTH: today, "fixing the cheap wood" is a REFRAMING plus one
DERIVED structural result (`beta/alpha = 2`) and three NAMED-but-unbuilt GU-specific consequences
(sign, `phi`, derived `Q`). The reframing is not empty -- it supplies the correct SHAPE of the fix
and one pinned number -- but it is not yet a derivation of the dynamical divergence-free Lambda. The
honest register: GU can MODEL Weinstein's rise-and-fall Lambda (like any interacting-DE model can),
and it has ONE thing a generic model does not (the `beta/alpha = 2` selection, DERIVED); the items
that would make it a FIX rather than a model (sign, `phi`, derived `Q`, closed genuine-reason) are
all `NOT-YET`.

## 6. The three-term scorecard (the deliverable's spine)

For each term: does GU keep or replace it; DERIVED / FITTED / CONDITIONAL / NOT-YET; and the
genuine-reason verdict for divergence-freedom.

| term | Weinstein's grade | GU: keep or replace | grade | genuine-reason verdict |
|---|---|---|---|---|
| **Einstein tensor `G_munu`** | MARBLE (contracted Bianchi) | **KEEP** (it is a geometric identity; PC1 reproduces it on FRW) | **DERIVED** | GENUINE and INTACT: `nabla_mu G^{mu nu} = 0` is an identity independent of the action; GU cannot lose it. |
| **`Lambda g_munu`** | cheap wood, forced constant, lousy reason | **REPLACE** (position-dependent `Lambda(x)` as a `w=-1` vacuum with exchange `Q`; W144 / W136 / W145-6) | **CONDITIONAL** (shape) + **DERIVED** (one leg: `beta/alpha=2`) + **NOT-YET** (derived `Q`, sign, `phi`) | GENUINE-CANDIDATE, NOT CLOSED: the lousy metric-compatibility reason is replaced by (i) interacting-vacuum bookkeeping `Q = -8pi nabla T_matter` and/or (ii) equivariance/Noether (`D_A* theta = 0`); (i) closes only if `Q` is supplied genuinely (record-promotion flux, gated on H59); (ii) is CONDITIONAL on C1/C2/C3. Bulk-flatness `beta/alpha=2` is a genuine DERIVED reason the BULK constant vanishes, distinct from the boundary term's divergence-freedom. |
| **`T_munu`** | cheap wood, ad hoc | **REPLACE-INTENDED** (source-action / record content) | **NOT-YET** | NOT SUPPLIED: same-source closure `open` (2026-06-24 map); `T_shadow` not source-derived; the issuance datum provably cannot feed the Yukawa hierarchy (W136 dimensional no-go); only Majorana OOM-reachable. The cheap-wood-#2 problem is essentially untouched by this session. |

**Marble-survival verdict (do not skip).** GU's induced `|II|^2` action gives the Einstein term
(`a1 = 1/3`, W126/W130, attractive) PLUS a higher-derivative sector (the tachyonic `R^2` / Stelle
sector, `c_R = -4/9`, `c_W = +2`, W126/W130; scalaron tachyonic, W122/W126). Does the higher-
derivative sector spoil the marble? **Computed answer: NO -- the marble SURVIVES but is AUGMENTED.**
Section D of the test constructs the `R^2`-sector field tensor
`E_munu = 2 R R_munu - (1/2) R^2 g + 2(g box - nabla nabla) R` and verifies `nabla^mu E_munu = 0`
identically on FRW: the higher-derivative sector carries its OWN generalized Bianchi / divergence-
freedom (this is Noether's second theorem: any diffeomorphism-invariant action has covariantly
conserved field equations). The test also confirms the schematic GU left side `a1 G + c2 E_R2` is
divergence-free. So:

> The marble (a divergence-free left side, for the genuine reason of diffeomorphism invariance /
> generalized Bianchi) is KEPT. It is MODIFIED: the left side is no longer `G_munu` alone but
> `a1 G_munu + (higher-derivative divergence-free tensor)`, and that augmentation is exactly the
> sector that carries the W122/W126/W130 tachyon/ghost. The marble is not spoiled; it is enlarged,
> and the enlargement is where GU's own unsolved problem (the tachyonic scalaron, H59 OPEN) lives.

This is an honest two-sided result: divergence-freedom survives trivially (it is forced by covariance),
but "keeping the marble" does NOT mean keeping ONLY the pristine Einstein tensor -- GU necessarily
adds a divergence-free companion that is not itself marble-clean.

## 7. The single derived-vs-fitted gap (the one that matters)

Between "we can MODEL a rise-and-fall Lambda" (the skeptic's point -- any interacting-DE model does
this) and "GU DERIVES the divergence-free dynamical Lambda for a genuine reason" stands **one gap**:

> **The source action H41 is unbuilt as a dynamical object that DERIVES `Q(a)`.** W144 FITS `Q` to
> DESI and BACKS OUT the source-action requirements; it does not derive `Q` from the covariant Y14
> operator (W131, symbol-level only) or the Fredholm propagator (W125). Until an explicit gauge-
> invariant source action on Y14 yields `Q` (with its clock coupling and sign change) AS ITS
> EULER-LAGRANGE OUTPUT -- equivalently, until the 2026-06-22 divergence-free proof's C3 (`theta` is
> the EL derivative of a gauge-invariant action) is discharged -- GU is MODELING the fix, not
> DERIVING it.

Closing that one gap would simultaneously: supply `Q` genuinely (closing the Lambda-term
genuine-reason verdict), give the equivariance/Noether route a concrete action, and begin the
same-source stress-energy bridge (the `T_munu` leg). It is the load-bearing unbuilt object.

## 8. GU-specific-vs-generic-interacting-DE novelty verdict

Against the W138 novelty gate (distinct from generic interacting-DE and from bare causal-set relabel):

- **What is GU-specific and DERIVED now:** `beta/alpha* = 2` bulk-flatness selection (W136, exact,
  pinned `1e-60`, from the newly computed `|H|^2` slice decomposition). This is a genuine
  determination a generic interacting-DE model does not have.
- **What is GU-specific and NAMED-but-unbuilt:** the sign pin `sign(Lambda) = +` from C-operator
  positivity (W145/W146); the everpresent normalization `phi = 1/(3 Omega_L)^2` from the (9,5)
  DeWitt-fiber measure (W146); the derived `Q` from H41.
- **What is GENERIC (not GU-specific):** the interacting-vacuum decomposition itself, the rise-and-
  fall shape of `Q`, the phantom-crossing-without-instability argument, the everpresent MAGNITUDE
  (relabels de Sitter, G5).

**Novelty verdict:** GU's marble/wood fix is, today, **one DERIVED GU-specific result
(`beta/alpha = 2`) wrapped around a generic interacting-DE / everpresent-Lambda skeleton, plus three
named-but-unbuilt GU-specific consequences that would make it a genuine fix.** It clears the novelty
gate on the `beta/alpha = 2` leg only; the dynamical-Lambda fix itself does not yet clear it (it is
generic-interacting-DE until the derived `Q` / sign / `phi` are built). This is a real result at the
level Joe asked for -- the marble is kept and computed, the lousy reason is diagnosed and computed,
the rise-and-fall is quantified and met, and one genuine reason (`beta/alpha=2`) is derived -- and it
is honestly short of a closed fix.

## 9. Direct answer to Joe's question

**Does the record-substrate / source-action structure FIX the field equations?** Conditional answer,
by term:

- **Marble (Einstein tensor):** KEPT, DERIVED, genuine reason intact -- but necessarily AUGMENTED by
  a divergence-free higher-derivative companion that carries GU's own tachyon. The marble survives;
  it does not survive alone.
- **Cheap wood #1 (`Lambda g`):** the SHAPE of the fix is achieved -- GU can model a divergence-free,
  not-forced-constant, rise-and-fall Lambda (W144's `Q`, quantified: single crossing at `z = 0.405`,
  O(1) `q_B` amplitude, `0.744/e-fold` drift), and it has ONE derived genuine reason on the bulk side
  (`beta/alpha = 2`). But the genuine reason for the boundary term's divergence-freedom is not
  closed: it routes through a ledger `Q` that is FITTED, not derived, and through an equivariance
  proof that is CONDITIONAL. So: MODELED, not yet FIXED.
- **Cheap wood #2 (`T_munu`):** NOT-YET. Same-source closure is `open`; the source action does not
  yet replace `T_munu` with derived geometric/record content.

**One-line honest grade:** the session KEEPS the marble (computed), correctly DIAGNOSES and REPLACES
the lousy reason with a rise-and-fall structure (computed and quantified), DERIVES one GU-specific
genuine reason on the bulk side (`beta/alpha = 2`), and leaves the load-bearing object -- a source
action that DERIVES the divergence-free dynamical Lambda -- UNBUILT (H41), with the second cheap-wood
term (`T_munu`) essentially untouched. The fix is genuinely SHAPED and partly DERIVED; it is not yet
CLOSED.

## 10. Honest limits

- Everything is conditional / exploration grade. Nothing asserts GU, that the DESI wiggle is real
  (W144 fits it as HYPOTHESIS; the DR3 bet is live), or that any decomposition is physical.
- The interacting-vacuum decomposition and the everpresent-Lambda mechanism are PORTED (labeled);
  the phantom-crossing-stability and the everpresent magnitude are generic, not GU-specific.
- The marble-survival test uses the `R^2` sector as the representative higher-derivative term; the
  full GU induced sector includes the `Ric^2` / Weyl channels (W130), whose field tensors are ALSO
  divergence-free by the same Noether's-second-theorem argument, so the survival verdict is robust,
  but only the `R^2` tensor is verified componentwise here.
- The genuine-reason verdict for the Lambda term is CONDITIONAL on H59 (no interacting C-operator
  exists), on the 2026-06-22 proof's C1/C2/C3, and on the unbuilt H41; the `phi` and sign results are
  named targets, not computed here.
- No canon / RESEARCH-STATUS / claim-status / verdict / posture change; no spec FIT row moves; H41
  unbuilt; H59 OPEN. Tri-repo gating honored: "issuance / record / substrate" are local postulate
  labels (W136 sense); the issuance concept is owned by temporal-issuance, MEASURE by time-as-
  finality; GU owns the field-equation math only; no cross-repo identity claim.

*Filed 2026-07-14 by Team MARBLE (W152). Five personas inline in one worker (GR/Bianchi theorist,
cosmological-constant-problem specialist, source-action/GU specialist, record-substrate theorist,
adversarial skeptic); no sub-agents. Reproducible: `python -u tests/W152_marble_and_wood_source_fix.py`
(21/21, exit 0; two positive controls first -- the contracted Bianchi identity and the W144 Q
zero-crossing). Exploration grade; conditional register; zero em dashes in paper-facing text; no
canon movement; H41 unbuilt; H59 OPEN.*
