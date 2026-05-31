# Cartan / Twistor / G_2 Anti-Numerology Guardrail

**Status.** Public draft artifact. Public draft artifact.
**Source basis.** `passes/01-foundational-math-lenses/01-differential-geometer.md`, `passes/01-foundational-math-lenses/04-spinor-clifford.md`, `passes/01-foundational-math-lenses/05-general-relativist.md`, `passes/01-foundational-math-lenses/07-representation-theorist.md`, `passes/02-substrate-loophole-lenses/15-cartan-twistor-loophole.md`, `passes/04-heterodox-problem-shape-math/25-ps-cartan-twistor-heterodox.md`, `deep-research/03-assumption-decomposition-no-go-evasion-literature.md` (Acharya-Witten 2001 entry; Distler-Garibaldi 2009 entry), `syntheses/06-supplementary-insights-novelty-and-tests.md`, `syntheses/08-supplementary-15-persona-pathway-ranking.md`. Cross-built against the six-axis protocol (WRK-375), the no-go forgetful-image map (WRK-376), and the Hegelian persona-protocol method note (WRK-381, sibling #30).
**Generated.** 2026-05-30
**Author posture.** This note is a guardrail, not an endorsement. It exists because the Cartan / twistor / G_2 corner of the GU program is the most reputationally vulnerable to dimensional numerology, and the repo's heterodoxy is only credible if it disciplines this corner harder than its critics would.

## 0. Why this guardrail exists

The Cartan / twistor / G_2 route scored persona-total 52/75 in `syntheses/08`, with maximal scores (5/5) from the differential geometer, spinor / Clifford, general relativist, and Cartan / twistor lenses. It also drew an explicit reputation flag in the same ranking: *"strong geometric resonance, but reputation risk if it becomes exceptional-dimension numerology."* The route's first-pass leverage (1.16) and insight leverage (0.87) put it near the bottom of the realistic-payoff list; its quick-finish recommendation in `syntheses/08` was explicitly *"finish condition: a scoping note saying exactly what Cartan/twistor/G_2 would need to prove, and what is mere dimensional coincidence."*

This is that note.

Without it, the route attracts two failure modes:

- **Numerology drift.** A geometric coincidence (most often `14 = dim G_2`, sometimes `4 + 10 = 14`, sometimes the `7 + 7 = 14` Spin(7)/G_2/octonion family) gets cited as if it discharged a real obligation when it discharges none.
- **Aesthetic capture.** A genuinely elegant Cartan / parabolic / twistor construction gets read as evidence for SM-content emergence when the actual representation-theoretic, anomaly, and Distler-Garibaldi obstructions remain entirely untouched.

The guardrail's job is to separate suggestive arithmetic from structural obligation, name red flags so a reader can spot drift, and name green flags so a contributor who has actually done work can be recognized.

The guardrail does **not** close the route. It says: this route is admissible as a secondary geometric branch only if a contributor clears the green-flag bar in Section 3 below.

## 1. Common dimensional coincidences the route latches onto

The following coincidences recur in the Cartan / twistor / G_2 corner of GU and its public discussion. Each is mathematically true. Each is also, by itself, a coincidence that has been individually noticed for decades without producing a working chirality / gauge-extraction / anomaly mechanism. Listing them honestly is the first guardrail move.

| # | coincidence | source where it appears in the GU lens material | what would have to be true for it to mean something |
| ---: | --- | --- | --- |
| C1 | `dim(metric bundle on a 4-manifold) = 4 + 10 = 14` | persona pass 01 (differential geometer); persona pass 05 (general relativist) | a canonical Cartan connection of the right (G, P) type on Met(X) carrying a chirality-grading subgroup must exist and not be a free choice |
| C2 | `dim(G_2 adjoint) = 14` | persona pass 07 (rep theorist); persona pass 15 (Cartan-twistor loophole) | Met(X)'s 14-dim total space must admit a *canonical* G_2-structure derivable from the metric-bundle datum alone, not chosen by hand |
| C3 | `G_2 ⊂ Spin(7) ⊂ SO(7)` and `7 + 7 = 14` | persona pass 07; persona pass 15 | the 7+7 split must align with a substantive split of Met(X)'s tangent that has SM-relevant content, not just dimensional bookkeeping |
| C4 | `dim(SO(10) vector) = 10`, matching the 10-dim fiber of Met(X) | persona pass 07 | SO(10) must arise as the actual structure group of the fiber from the geometry, not be installed because its vector rep has the right dimension count |
| C5 | `Cℓ(14, ℂ) ≅ M_{128}(ℂ)`; Weyl spinor in 14d has 64 complex components; `64 = 4 × 16` and `48 = 3 × 16` | persona pass 04 (spinor-Clifford) | a discrete symmetry or geometric mechanism must project 64 → 48 (three generations) from substrate data, not be a postulate |
| C6 | Twistor space PT for R^4 is complex 3-fold (3 = `dim_C PT`); the Penrose googly problem makes ASD gravitons natural and SD ones not | persona pass 15; heterodox persona 25 (Penrose pre-geometry move) | chirality has to follow from PT's complex structure projecting *to* the metric bundle, with substrate role inverted; the bare double-cover / dimension match is not the claim |
| C7 | `dim(E_8) = 248`, `248 = 3 × 27 + 167` and various E_8 ⊃ E_6 × SU(3) decompositions look like "three generations" | persona pass 07; Distler-Garibaldi 2009 (deep-research/03) | a connected compact subgroup centralizing SL(2,C) with V_{m,n} ≤ 4 content giving complex V_{2,1} as G-rep must exist inside a single real form of E_8 — Distler-Garibaldi proves this is *false* |

C7 is the one the repo has to engage most carefully. Distler-Garibaldi is not a vague reputation problem; it is a published representation-theoretic theorem that rules out the entire single-E_8-numerology family that has gravitated to GU public discourse. See Sections 2.7 and 4 below.

## 2. Per-coincidence map — real obligation vs suggestive arithmetic

For each coincidence above, this section names (a) the geometric structure that *would* be load-bearing if the coincidence carried real content, (b) what would have to be proven, not assumed, for that structure to be present, and (c) what the persona-pass material actually established versus what a reader might wrongly infer.

### 2.1 — `4 + 10 = 14` (C1)

**The real geometric obligation.** A 14-dim total space over a 4-manifold whose fiber is the 10-dim space of pointwise Lorentzian metrics is a canonical bundle construction. Met(X) is well-defined without choosing a metric on X. So far this is bookkeeping that any working differential geometer accepts (pass 01, pass 05).

**What would have to be proven.** That a *canonical* Cartan connection of type (G, P) exists on Met(X) where G strictly contains GL(4,R) and the Levi factor of P carries a representation that splits into SM-fermion content. The persona-pass 15 loophole construction sketches this for a parabolic (G, P) of conformal type and notes that the tractor bundle's chirality split is genuinely available — but only after the parabolic structure has been *chosen*. The choice is not forced by Met(X).

**What the persona material actually shows.** Pass 01 obstruction (d.1): *natural bundles over X have structure group derived from Diff(X) jets, ultimately GL or its reductions; SU(3) × SU(2) × U(1) is not natural in this sense.* Pass 05 obstruction (d.1): *Wheeler-DeWitt fiber metric is indefinite; total-space "metric" is not Lorentzian.* The 14-dim story survives as a real bundle; the SM-content story does not survive at the bundle level without extra structure that is currently a postulate.

**Verdict.** C1 is a bookkeeping coincidence at the bundle level. It becomes load-bearing only if a contributor produces an explicit (G, P) and proves canonicality, not by exhibiting the dimension match.

### 2.2 — `dim(G_2) = 14` (C2)

**The real geometric obligation.** G_2 is the smallest compact simple Lie group whose adjoint has dimension 14. There is no other in dimension 14. If Met(X) admits a generic 3-form `φ ∈ Λ^3(T*Met(X))` whose stabilizer is G_2, then a G_2-structure on the 14-dim total space is *geometrically real* and the exceptional-holonomy spinor decomposition (G_2 has a unique 7 + 1 spinor split) becomes available.

**What would have to be proven.** That such a generic 3-form on Met(X) (a) exists, (b) is canonical given just the metric-bundle data, and (c) its associated G_2-holonomy reduction supplies chirality through the exceptional-spinor decomposition without further hand input. Persona pass 15 marks the whole construction `[speculation]` and notes that *"the chirality would have to be installed by choosing those extra structures, which is itself an input."*

**What the persona material actually shows.** The dimension match is real. The construction is not derived; it is named as a possibility. Pass 15's verdict is *plausible loophole class, not a derivation* — exactly the warning this guardrail is making explicit.

**Independent comparison.** Acharya-Witten 2001 (`deep-research/03` entry 5) is the only fully developed G_2-holonomy chirality construction in the established literature, and it works *only because the G_2-holonomy 7-manifold is singular*. This is significant for two reasons:

1. It confirms G_2-holonomy can deliver chirality in some setups — the route is not nonsense.
2. The mechanism is *singularity*, not *G_2 itself*. The chirality comes from the singular stratum, not from `dim(G_2) = 14`. The dimension match is incidental to the mechanism.

**Verdict.** C2 is real as a dimension match, real as a possible structure on Met(X), and *not* a derivation of chirality. The G_2 word in Acharya-Witten is doing different work from the G_2 word in `dim(G_2) = 14 = dim(Met(X))` — conflating the two is a red flag.

### 2.3 — `G_2 ⊂ Spin(7) ⊂ SO(7)` and `7 + 7 = 14` (C3)

**The real geometric obligation.** The chain G_2 ⊂ Spin(7) is real and well-known: G_2 is the stabilizer of a generic 3-form on R^7 and Spin(7) is the stabilizer of a generic 4-form on R^8. The `7 + 7 = 14` arithmetic is true. None of this, by itself, says anything about the 14-dim Met(X) total space.

**What would have to be proven.** That a 7+7 split of T(Met(X)) into two SO(7) or G_2-invariant pieces is *canonical given metric-bundle data alone* and *carries SM-relevant content* (chirality, gauge-charge assignments, generation structure). This has not been proven anywhere in the lens material.

**What the persona material actually shows.** Pass 04 (spinor-Clifford) notes the 14-dim Weyl-spinor count is 64 complex, not naturally compatible with three SM generations of 16. Pass 07 (rep theorist) notes a 4 + 10 split is the natural reading from rep theory, not 7 + 7. The 7 + 7 split is suggestive arithmetic with no canonical bundle-theoretic anchor in the GU material.

**Verdict.** C3 is the cleanest example of dimensional numerology in this corner. Naming the chain G_2 ⊂ Spin(7) is true; gluing it to Met(X) without producing the canonical 7-bundle is the drift.

### 2.4 — `dim(SO(10) vector) = 10` matching Met(X)'s fiber (C4)

**The real geometric obligation.** SO(10) GUT is a real, anomaly-free, one-generation-per-16 construction (pass 07 strongest-construction section). The branching SO(10) ⊃ SU(5) ⊃ SU(3) × SU(2) × U(1) gives the SM gauge group exactly, with the 16 spinor decomposing as 10 + 5̄ + 1 under SU(5).

**What would have to be proven.** That SO(10) acts canonically on Met(X)'s 10-dim fiber. The fiber of Met(X) is Sym²₊(R⁴), the space of Lorentzian metrics at a point, which has dimension 10 but whose *structure group is GL(4,R)* acting via congruence, not SO(10). GL(4,R) acts on Sym²(R⁴) by `(A, h) ↦ A^T h A`. There is no SO(10) acting canonically on this fiber.

**What the persona material actually shows.** Pass 07 is explicit: *"The G_2-on-base / SO(10)-on-fiber split is not forced by representation theory alone; it is a **choice** [speculation] that exploits the coincidence dim(G_2 adjoint) = 14 = 4 + 10."* The choice is acknowledged as a choice. The route's reputational risk is that downstream commentary often elides the choice and reports the coincidence as a derivation.

**Verdict.** C4 is dimension-match numerology that imports SO(10) GUT machinery without a derivation that SO(10) acts on Met(X)'s fiber. SO(10) GUT is a real piece of math; its connection to Met(X) via this dimension match is not.

### 2.5 — Clifford / spinor counts at dim 14 (C5)

**The real geometric obligation.** Pass 04 derives the spinor counts honestly: Cℓ(14, ℂ) ≅ M_{128}(ℂ); 14d Weyl spinor has 64 complex components in the even-dim split; Majorana real-structure analysis fails in (13,1) signature; Majorana-Weyl exists in (7,7) with real dim 64.

**What would have to be proven.** That a substrate-or-bundle-level mechanism projects 64 complex Weyl components onto 48 = 3 × 16 SM Weyl components, **with the chirality survival the projection requires**. Pass 04 names this explicitly: *"64 = 4 × 16 invites a 'four generations' reading, not three. [speculation] One generation could be projected out by a discrete symmetry, but this is a postulate, not geometry."* The projection is not derived.

**What the persona material actually shows.** Pass 04's named obstructions include Atiyah-Singer mod-8 Majorana obstruction, w₂ obstruction, the 64-vs-48 generation mismatch, Witten-style π₄(Spin) discrete anomaly, and spin-statistics failure in non-Lorentzian signatures. The spinor count is real; the SM-spinor extraction is not.

**Verdict.** C5 is the place where dimensional numerology is most disciplined in the existing lens material — pass 04 is sharp about what 64 spinor components do and do not say. The risk for downstream readers is treating "14 is even, so chirality exists" as a discharge of obligation. It is not; it is the *starting* point of obligation.

### 2.6 — Twistor double-cover, Penrose googly (C6)

**The real geometric obligation.** Twistor space PT for R^4 is canonically complex dimension 3; the Penrose-Newman googly problem (ASD gravitons natural, SD gravitons hard) is real and historically important. The heterodox-persona pass 25 makes the strongest available move: read PT as the substrate-level object and the 4-manifold as a Penrose-transform output, putting chirality structurally on the substrate (the complex structure of PT) rather than at the bundle level.

**What would have to be proven.** That a Penrose-Newman twistor 3-fold admits a U-duality-compatible extension whose Penrose transform produces an observer-frame Cartan connection on a real 4-manifold with built-in chiral Z/2 grading, and that the extension's Freed-Hopkins anomaly invariant matches the SM signature. This is the heterodox-pass 25 falsifiable question and it is genuinely open.

**What the persona material actually shows.** Pass 25 is honest: *"a negative answer (no such PT extension exists ...) closes the heterodox Cartan / twistor / pre-geometric substrate route. A positive answer hands WRK-326 a substrate candidate adjacent to Penrose's decades-old program."* The route is admissible as a substrate proposal, not a derivation.

**Verdict.** C6 is the strongest twistor coincidence the route can legitimately invoke, *because* it is paired with a falsifiable substrate-inversion question. Naming the googly problem without the substrate-inversion frame is closer to twistor-poetry than to substrate proposal. The fall-line between green-flag and red-flag here is whether the contributor names what fails the proposal, not just what would be nice if it worked.

### 2.7 — E_8 / 248-numerology and Distler-Garibaldi (C7)

**The real obligation, and the published wall.** Distler-Garibaldi 2009 is the cleanest, sharpest no-go in this corner. The theorem (per WRK-376 / `deep-research/03`): there is no real Lie group E together with subgroups SL(2,C) and G such that

- G is connected, compact, centralizing SL(2,C);
- in the SL(2,C) × G decomposition of Lie(E), V_{m,n} = 0 for m + n > 4;
- V_{2,1} is a complex G-representation;

inside complex E_8 or any real form of E_8.

This rules out the entire family of "the 248-dim adjoint of E_8 contains three SM generations as a centralizer of the Lorentz group" claims that have gravitated to GU public discourse. WRK-376's reading: *"every successful 'evasion' leaves the class entirely; no loophole inside single-E_8 representation theory."* The published evasions (Braun-He-Ovrut-Pantev 2005-2006 with E_8 × E_8 heterotic on Calabi-Yau; Nesti-Percacci GraviGUT SO(3,11); Meissner-Nicolai K(E_10)) all *leave* single-E_8 representation theory entirely.

**What this means for the guardrail.** Any Cartan / twistor / G_2 path that ends up importing E_8 numerology — most often via "E_8 adjoint = 248", or via "exceptional Lie groups are the natural home of unification" — must explicitly engage Distler-Garibaldi. Not engage it rhetorically. Engage it at the level: name the (G, real form of E, V_{m,n}) data, show the proposed construction either falls inside the obstructed class (in which case it is dead by Distler-Garibaldi) or leaves the class (in which case it is no longer single-E_8 representation theory and must justify the category change).

**WRK-376's reading propagates here.** The forgetful-image frame strains hardest at Distler-Garibaldi. Distler-Garibaldi forgets the entire *category* (representation theory → bundle theory; finite-dim Lie → infinite-dim Kac-Moody; single group → product group), not just the mechanism. The Cartan / twistor / G_2 route, if it invokes E_8 at all, inherits this stress: the route cannot use "E_8 has the right dimension" as a substantive move while the theorem says no single-E_8 representation-theoretic extraction of the required centralizer data exists.

**Verdict.** C7 is the most reputationally dangerous coincidence in this corner. The guardrail's hardest rule: a contributor who invokes E_8 numerology in a Cartan / twistor / G_2 setting without explicitly addressing Distler-Garibaldi is below the bar for repo admission of that contribution.

## 3. Red-flag list — patterns that look meaningful but aren't

These are presentation patterns. A draft, comment, or section that exhibits one of these without engagement is a red flag for numerology drift. The list is not exhaustive; it names the patterns that recur in this corner of the program.

- **R1. Dimension-match as derivation.** "X has dimension n; G has dimension n; therefore G acts naturally on X." Almost never true. The action must be exhibited and proven canonical, not asserted from a dimension match. C1, C2, C4 are the principal traps here.
- **R2. Sub-group chain as content.** "G_2 ⊂ Spin(7) ⊂ SO(7); these are exceptional / spinorial / classical; therefore the chain is doing SM-relevant work." The chain is real; the SM-relevant work is not in the chain. C3 is the principal trap.
- **R3. Rep dimension count as content.** "n = 248 = 8 × 31 = 3 × 82 + 2 = (some decomposition that resembles 3 generations)." Distler-Garibaldi 2009 already rules out the single-E_8 family of these. Variants for E_6 (78), E_7 (133), F_4 (52) inherit the same obligation: name the centralizer, the V_{m,n}, the complex G-rep condition.
- **R4. Coincidence-stacking.** "Dim G_2 = 14; dim metric bundle = 14; dim Weyl spinor in 14d is even; G_2 has a 7 + 1 spinor decomposition; therefore the construction works." Coincidence stacking is rhetorical, not mathematical. Each coincidence either carries an obligation that is independently discharged, or it carries nothing; stacking does not strengthen them.
- **R5. Aesthetic-resonance language.** "Naturality," "exceptional beauty," "deep coincidence," "structural inevitability," used as substitutes for proofs that a structure is canonical from the given input. This is the corner most prone to this language; the guardrail flags it on sight.
- **R6. Acharya-Witten 2001 cited without the singularity.** Acharya-Witten gives chirality on a G_2-holonomy 7-manifold *only when X is singular*. Citing "Acharya-Witten G_2-holonomy" as a smooth-geometry chirality precedent is a misread of the theorem. The mechanism is the singularity; the G_2-holonomy label is the setting, not the engine.
- **R7. Twistor-as-language vs twistor-as-substrate.** Twistor language without substrate-inversion (the C6 / pass 25 move) is decoration. The legitimate twistor move requires committing to the substrate-inversion reading and accepting its falsifiable question.
- **R8. E_8 numerology without Distler-Garibaldi.** Any invocation of E_8 dimensions, centralizers, or generation counts that does not explicitly address Distler-Garibaldi 2009 is below the repo bar. This is the single hardest line in this guardrail.
- **R9. "Geometric origin of SM" claim with no chirality bridge.** A construction that does not name what substrate-level invariant carries chirality, how it survives the forgetful operation to the smooth-bundle shadow, and what would falsify the bridge, is at-best decorative. The six-axis protocol (WRK-375) makes this explicit; the chirality-bridge claim is a required output of the template.
- **R10. Persona-quote as endorsement.** Picking the Cartan / twistor persona pass quote that sounds favorable while ignoring the same pass's *verdict* (e.g., pass 15: *"plausible loophole class, not a derivation"*). The loophole personas in `passes/02` are deliberately steelmanned. Their verdicts are where the discipline is.

## 4. Green-flag list — patterns that carry actual structural content

A Cartan / twistor / G_2 contribution that exhibits the patterns below is doing real work. The list is the bar for admission as a serious secondary-branch contribution.

- **G1. Canonical-construction proof.** Produces an explicit (G, P) parabolic geometry on Met(X) where G strictly contains GL(4,R), with a written proof that the structure is canonical from the metric-bundle datum alone (no choice of extra section, frame, or G-structure). C1 / C2 are the principal places this would have to land.
- **G2. Chirality bridge in the WRK-375 sense.** Names a substrate-level invariant that carries chirality / 3-generation / gauge content, names the forgetful operation that reduces to the smooth-bundle shadow, and explains why the shadow yields the no-go-theorem nullity that Witten / Nielsen-Ninomiya / Freed-Hopkins / Distler-Garibaldi compute. This is the WRK-375 / `six-axis-template.md` requirement, applied here.
- **G3. Singularity discipline.** If the construction relies on G_2-holonomy at the chirality level, names the singular stratum explicitly (as Acharya-Witten 2001 does), and engages the question of whether singularities of the required type exist on Met(X) and what their physical interpretation would be.
- **G4. Substrate-inversion commitment for twistor moves.** If the construction uses twistor language, commits to the heterodox pass 25 substrate-inversion reading: PT is the substrate object, the 4-manifold is the observer-frame artifact, and the construction is a proposal for the Penrose-transform / Hitchin-isomorphism that produces the observer-frame Cartan connection with built-in chiral grading. Names the falsifiable question (pass 25, e). Does not invoke "twistorial" as decoration.
- **G5. Distler-Garibaldi engagement.** If any E_8 numerology appears, explicitly names the (G, real form, V_{m,n}) data and either (a) shows the proposed construction falls inside the obstructed class and explains why this is acceptable (it usually is not), or (b) shows the construction is genuinely outside single-E_8 representation theory and accepts the category-change tax. WRK-376 §2.4 is the canonical reference; this guardrail does not re-derive it.
- **G6. Six-axis fill.** Fills the WRK-375 six-axis template — L1 substrate, L2 observer, L3 pairing, L4 causal order, L5 emergence, L6 coordination loop — and supplies a first falsification test. The Cartan / twistor / G_2 route is the natural L1 = (h) "Cartan parabolic Klein pair with G_2 hint" axis-drop. A contribution that fills the template legitimizes the route as a typed research object; one that does not is decorative.
- **G7. Anomaly-track-record.** Computes (or sketches) the anomaly content of the proposed substrate construction in the Freed-Hopkins enriched-bordism frame (cf. WRK-376 §2.3). A construction that does not engage anomaly content has not done the work that the no-go-map's third row demands.
- **G8. Honest dimensional accounting.** Reports the spinor counts (pass 04: 64 vs 48), the structure-group mismatch (pass 01: GL(4,R) vs SU(3) × SU(2) × U(1)), the Wheeler-DeWitt indefinite signature (pass 05), and the discrete anomalies (π₄(Spin) torsion) as standing obligations, not solved problems.

## 5. Six-axis row for this route

Per WRK-375's contract, the Cartan / twistor / G_2 route's one-line sextuple is:

| candidate | L1 substrate | L2 observer | L3 pairing | L4 causal order | L5 emergence | L6 coordination loop | first falsification test |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cartan / twistor / G_2 (guardrail-admitted version) | (h) Cartan parabolic Klein pair with G_2 hint; *or* (substrate-inversion variant) twistor pre-geometric PT in dim_C 3 with proposed U-duality extension | (a) Finite Turing observer (BPP/BQP) | (a) Cartesian / smooth (tractor projection in place of fiber integration) | (a) Total-order Lorentzian for the Cartan reading; (a) preserved post-Penrose-transform for the twistor-substrate reading | (a) Specific-object substrate | (a) No loop | Exhibit a canonical (G, P) parabolic geometry on Met(X) whose tractor bundle contains an SM generation (16 of Spin(10)) as a composition factor *without choosing extra structure*; OR exhibit the Penrose-Newman PT extension answering pass 25's falsifiable question. Failure on the canonicality or extension-existence step kills the candidate. |

The row exists to enter this route into the six-axis protocol's coordination space. It does not endorse the route; it makes the route comparable to other axis-drops.

## 6. What this path would have to prove to matter (DoD §3)

Per the WRK-383 card's Definition of Done §3, the four things this route would have to prove are below, with the guardrail's reading appended.

1. **Chirality mechanism.** A substrate-level invariant carrying chirality, with a derived forgetful operation to the smooth-bundle shadow. Currently: not derived in any persona pass; only sketched. The closest existing model is Acharya-Witten 2001's singular G_2-holonomy mechanism, which is *not* the same as `dim(G_2) = 14`.
2. **Gauge extraction.** A canonical action of SU(3) × SU(2) × U(1) (or an unbroken SO(10) / SU(5) parent) on Met(X)'s 10-dim fiber, derived from the metric-bundle datum alone. Currently: not derived. Pass 07 is explicit that the SO(10) / G_2 split is a *choice*, not a derivation.
3. **Anomaly compatibility.** Either the substrate's anomaly content lands in the SM-matching class of Freed-Hopkins enriched bordism, or the construction's substrate-inversion explicitly forgets the enrichment in a way that recovers the SM. Currently: untouched by the Cartan / twistor / G_2 lens material.
4. **Reduction to known low-energy content.** A controlled reduction from the 14-dim substrate dynamics to 4-d GR (pass 05) + SM gauge + SM fermion content (pass 04, pass 07), including the projection from 64 Weyl components to 48 SM components and the discrete-anomaly cancellation. Currently: untouched.

A contribution that addresses one of these substantively is a green-flag G2/G7 contribution. A contribution that asserts any of these from a dimension match is a red-flag R1/R9 contribution.

## 7. Recommended status (DoD §4)

**Secondary branch.** Not a lead path. The Cartan / twistor / G_2 route is admissible as a secondary geometric branch that contributors with parabolic-geometry, twistor-theory, or G_2-holonomy expertise may develop *if they clear the green-flag bar*. The persona-rank position (12th of 16 in `syntheses/08`'s impact / first-pass-leverage table) supports this status; the persona scoring (high from pass 01, 04, 05, 15; low from pass 11 stochastic geometer and pass 12 quantum measurement) supports the "geometric resonance, narrow lens" reading.

The status is **not "park."** Pass 25's heterodox substrate-inversion variant is a genuinely open research proposal with a falsifiable question and a non-trivial chance of teaching the program something even if it fails. The status is **not "appendix only"**; appendix-only would underclaim what pass 25's substrate-inversion move could be worth if a contributor with the right background developed it.

The status **is** "secondary branch, behind the guardrail." Contributions to this route are admitted to the repo only if they clear the green-flag bar in Section 4; contributions that exhibit red-flag patterns from Section 3 are sent back to the contributor for sharpening with this guardrail referenced.

## 8. Cross-card findings for the coordination pass

To be propagated to related artifacts via the draft coordination note on this pass.

- **For #24 (six-axis-specification-protocol).** The Cartan / twistor / G_2 route is a legitimate L1 = (h) axis-drop *with a substrate-inversion variant* (heterodox pass 25 / Penrose pre-geometry) that the L1 menu may want to acknowledge as L1 = (h')-or-similar. The substrate-inversion variant is structurally different from the parabolic-geometry-on-Met(X) variant and the menu could helpfully distinguish them.
- **For #25 (no-go-forgetful-image-map).** WRK-376's Distler-Garibaldi treatment is *the* load-bearing reference for this guardrail's R8 / G5. This guardrail explicitly does not re-derive WRK-376's §2.4 and instead cites it; the coordination pass should ensure the public versions of both artifacts cross-reference cleanly so a reader doesn't get conflicting framings.
- **For #30 (hegelian-persona-protocol-method-note).** This guardrail *is* the persona-protocol method's output applied as a falsification check on a tempting route. The method note may want to use Cartan / twistor / G_2 as the worked example of "persona dialectic generated a guardrail that catches numerology" — the case where the method's discipline value is most visible.
- **For coordination pass generally.** This guardrail does not introduce new findings that bear on #26 (Type II_1 checklist), #27 (Nielsen protocol pilot), #28 / #29 (claim mining), #31 (stochastic parity-breaking), #33 (Sorkin causal-set), or #34 (RG / universality). It is orthogonal to those axis-drops. The Type II_1 candidate's strategy (preserve L2-L4, push richer data into L1 = (c)) is a different L1 choice from this route's L1 = (h); the two are related axis-drop alternatives, not competitors.

## 9. Honest gaps in this guardrail

- The guardrail does not construct any of the canonical (G, P) parabolic geometries it names as obligations. It states the obligation; it does not discharge it.
- The Distler-Garibaldi engagement (Section 2.7) imports WRK-376's reading; this guardrail does not independently verify the no-go's class assumptions. If WRK-376 is wrong about Distler-Garibaldi's scope, this guardrail's R8 / G5 inherits the error.
- The substrate-inversion / twistor-substrate reading (Section 2.6 / G4) is a sketch of pass 25's falsifiable question, not an evaluation of whether the question is currently approachable. The guardrail admits the question as legitimate; it does not say it can be answered soon.
- The guardrail's red-flag list is the patterns this author saw most often in the lens material and adjacent public GU discussion. It is not a complete list. A contributor with deeper experience in this corner may add patterns.
- The guardrail does not engage E_6 (78), E_7 (133), or F_4 (52) numerology separately from E_8. The class-of-claim is the same (representation-theoretic obstruction subject to a Distler-Garibaldi-style theorem on the centralizer / V_{m,n} structure), but the literature on each is its own pile. If a contribution invokes E_6 / E_7 / F_4 specifically, that is a place this guardrail is silent and a future revision should engage.

## 10. Closing posture

The Cartan / twistor / G_2 route is the corner of the GU program where the gap between *suggestive arithmetic* and *structural obligation* is widest. The guardrail's job is to make the gap visible so that contributions either close it with real geometric work (green-flag G1-G8) or are sent back to do so. The guardrail is conservative because the route is reputationally fragile and because the existing persona-pass material already does the right discipline; the contribution this artifact makes is to lift that discipline into a public bar that a contributor can read once and use as a checklist.

The route is not closed. It is gated.

The hardest line: **no E_8 numerology in this corner without explicit Distler-Garibaldi engagement.** Everything else flexes. That one does not.
