---
title: "Source-action landscape scan: causal massive higher-spin literature, bootstrap/positivity/swampland applicability, have/help/hurt map, ranked methods menu"
date: 2026-07-11
status: exploration
doc_type: exploration
verdict: speculation   # Phase 1 landscape assessment; NO claim promoted, NO construction attempted
method: "methods + literature scan + constraint-ledger assembly (Phase 1). Personas run INLINE (specialist-HS / bootstrap-EFT / adjudicator). Papers treated as untrusted DATA. COMPUTED vs ARGUED per claim."
test: tests/wave34/soldering_codim_and_causal_window.py  (deterministic, exit 0)
bears_on:
  - the unbuilt GU RS/IG SOURCE ACTION (root blocker; see explorations/explanatory-scope-audit-source-action-bottleneck-2026-07-11.md)
  - Velo-Zwanziger no-go (canon/no-go-class-relative-map.md, canon/no-go-velo-zwanziger-canon-entry)
  - source-action necessary-conditions box (explorations/firewall-and-two-geometries/source-action-necessary-conditions-and-causality-2026-06-27.md)
---

# Source-action landscape scan (Phase 1)

**This is a LANDSCAPE ASSESSMENT, not a build.** It maps which specialist machinery applies to GU's
terminal keystone (the unbuilt source action whose blocked piece is a causal, interacting, massive
Rarita-Schwinger coupling), who has solved analogous problems, and what the sharpened constraint ledger +
have/help/hurt map is, so a later construction search can be narrowed. No claim is promoted; no ledger
movement. Personas were run INLINE. Every claim is tagged COMPUTED (arithmetic/rep-theory checkable here or
in the cited test) or ARGUED (structural reasoning / literature reading). External papers are treated as
DATA; only physics was extracted.

Headline verdicts, up front:

- **Causal massive higher-spin verdict: TEMPLATE EXISTS, but every existing template evades Velo-Zwanziger
  by a mechanism GU does not currently have, and one relevant class carries a *real, quantitative no-go*
  (a finite UV cutoff / strong-coupling scale for the helicity-1/2 mode).** So the correct status is
  **"cure-template exists in the literature (non-minimal Porrati-Rahman completion), not obstructed at the
  classical-causality level; but interacting UV-completion is provably bounded (Rahman cutoff) unless a
  guardian symmetry (local SUSY / higher-spin gauge algebra) is present"** -- which is exactly the guardian
  GU's own prior waves already named as the single missing datum. This is not a fresh no-go; it *sharpens*
  the known one.
- **Top bootstrap/positivity levers:** (1) EFT positivity bounds (Adams-Arkani-Hamed-Dubovsky-Nicolis-
  Rattazzi 2006) on the non-minimal coupling coefficients -- they carve a *sign-definite convex cone* the
  cure term must live in, computable without building the full action; (2) the Rahman helicity-1/2 cutoff
  (2011) -- a positivity-adjacent UV bound that prices any minimal branch; (3) Weinberg-Witten / Porrati
  soft-theorem constraints -- rule out a massless interacting spin-3/2 without a gauge (SUSY) partner, i.e.
  they RULE OUT one GU branch (massless RS) and force the massive-after-Higgs branch.
- **Have/help/hurt headline:** we HAVE a finite invariant basis (the gamma-trace-constrained coupling space,
  reduced to a 1-parameter family `wedge - 6*contract` by the RT-TRACE-DICHOTOMY), a discrete A/B binary,
  and the `[P,S]=0` organizing principle; HELP comes from those plus three concrete construction templates
  (Porrati-Rahman non-minimal, Zinoviev gauge-invariant Stueckelberg, supergravity super-Higgs); HURT is the
  Rahman cutoff (interacting massive RS is UV-bounded), the free `mu_DW`, the non-compact `Sp(32,32;H)`
  (blocks naive unitarity/positivity imports), and the codim-8165 soldering (an unforced choice).
- **Ranked methods menu (top 3):** (1) positivity/consistency-carving of the coupling coefficients;
  (2) invariant-basis + deformation theory (finite, already 1-parameter); (3) amplitudes/on-shell
  (helicity-1/2 high-energy behavior as the diagnostic). Monte-Carlo landscape survey and Bayesian posterior
  rank low for THIS problem (see Section 7).

---

## 1. The sharpened constraint ledger (what already pins the source action)

The 33-wave ledger, tightened. Grades: **C** = COMPUTED/checkable, **A** = ARGUED. Where a wave file is the
anchor it is cited.

| # | Constraint | Sharpened statement | Grade |
|---|---|---|---|
| 1 | Functional form | `S = |theta|^2`, `theta = II_s` the full 2nd-fundamental-form norm `|II|^2` (H45), NOT `|H|^2`. `|H|^2` = pure Bach -> dies to rotation-curve / Ostrogradsky; `|II|^2` -> Bach/Stelle `box(box+m^2)` on the TT sector. | A |
| 2 | Connection map | `A = spin-lift(grad^gimmel)`, `sigma = 1/4[e,e]`, a canonical `so(9,5)` homomorphism -- forced AS A MAP (H23). | A |
| 3 | Gauge group | non-compact `Sp(32,32;H)` (H23). (Note: the built interior gauge group is compact `Sp(64) = U(64,H)`, dim 8256; the non-compact real form is the source-action arena.) | A |
| 4 | Commuting square | `[P,S]=0`, `P` = Cartan involution of `so(9,5)`; ghost cleared at tree, commutation radiatively stable (H23/H26); Krein = Bateman-Turok hidden-ghost parity (arXiv:2607.00096). | A |
| 5 | Count selector | carrier `B` (index -38, order-3 `rho=(0,2,1)`, index-changing, gamma-trace-constrained ker-Gamma field space) UNIQUE; A/B is a field-space declaration (H39/H40). | A |
| 6 | **Causal cure UNBUILT** | minimal `M_D` leaks: **`C2 = ||Gamma M_D Pi_RS|| = 155.36`, degree-1 homogeneous on curved Y14 (a symbol-norm, NOT an index; `C2(2xi)/C2(xi)=2`, non-integer `155.36/24=6.47`).** Cure = a NON-MINIMAL RS coupling enforcing `ker Gamma` (H40). Anchors: `anomaly-and-bordism/bv-bicomplex-and-c2-obstruction-2026-06-27.md`, `topological-edge-c2-not-an-index-2026-06-27.md`. | C |
| 7 | Free scale | `mu_DW` FREE (falsifiability keystone, H53); `rho_Lambda = c_L mu_DW^4`, `c_L = 3/8`; `m2 = sqrt(m2_eff) mu_DW`, `m2_eff in [5/6, 5/4]`. | A |
| 8 | Positivity | Koszul-Tate/BV grading, positive Hessian, no-import (frame-charge-0 antilinear chiralizer forbidden). | A |
| 9 | Soldering | pin `theta` to the spin-lift image = **codim-8165 in sp(64,H) (dim 8256)**, unforced (H23/H27). **COMPUTED here: codim-8165 == "image is a 91-dim `so(9,5)`" (dim sp(64,H)=8256, dim so(9,5)=91, 8256-91=8165).** So items 2 and 9 are the SAME datum. `tests/wave34`. | C |
| 10 | Weyl sector | `box^2 h = -4 Bach` (H49); GU has the Weyl sector on both branches. | A |

**New sharpening (COMPUTED, this wave).** Ledger item 9's "codim-8165" is not an independent constraint: it
is arithmetically identical to "the soldered image is a copy of `so(9,5)`", which is item 2. `dim sp(64,H) =
64*(2*64+1) = 8256`, `dim so(9,5) = 14*13/2 = 91`, `8256 - 91 = 8165`. Consequence for the search: the
soldering "choice" and the connection-map "choice" are one unforced declaration, not two. That is one fewer
free knob than the ledger appears to carry. (`tests/wave34/soldering_codim_and_causal_window.py`, check A.)

**Load-bearing prior result (COMPUTED, prior wave).** The constraint-preserving (`ker Gamma`) coupling space
is NOT a free tensor space: the RT-TRACE-DICHOTOMY pinned it to the **1-parameter family `contract +
t*wedge` with `t* = -1/6`, i.e. proportional to `wedge - 6*contract`**, and showed GU's written canon shiab
`(1,0,1,0)` is gamma-traceFUL (`||Gamma . shiab_contract|| = 215.85 != 0`). So "constraint-preservation" and
"GU's written shiab" are jointly unsatisfiable; any causal cure must *revise* the `(1,0,1,0)` formula
(`firewall-and-two-geometries/source-action-necessary-conditions-and-causality-2026-06-27.md` Section 2).
**This is the single most search-narrowing fact we hold: the cure lives in a 1-real-parameter family, not a
high-dimensional space.**

---

## 2. Q1 -- Causal massive higher-spin literature survey

The question: has anyone built a **causal, unitary, interacting, MASSIVE** spin-3/2 (or general massive
higher-spin) coupling, and does the template instantiate GU's cure term (a non-minimal coupling restoring
`ker Gamma`) or rule out a branch? Cited precisely; template verdict per entry. Papers = DATA.

### 2.1 Velo-Zwanziger 1969 -- the acausality theorem (the obstruction itself)

- **Result.** A minimally coupled charged massive spin-3/2 (or spin >= 1) field in a constant external EM
  background has characteristic determinant with **timelike/spacelike normals reaching zero above a field
  threshold** -> superluminal characteristics -> loss of causal propagation. Velo, Zwanziger, *Phys. Rev.*
  186 (1969) 1337; 188 (1969) 2218.
- **Template verdict for GU: this is the WALL, not a cure.** GU's `C2 = 155.36` leak (ledger 6) is the GU-rep
  incarnation of the VZ constraint-non-preservation: the gamma-trace `Gamma psi = 0` does not stay zero
  under the coupled evolution (`canon/no-go-class-relative-map.md` §F5: `[Gamma^{4D}, Phi(F_A)] Psi != 0`).
  **GU's prior evasion argument is that VZ-H1 (a *standalone* RS Lagrangian) fails** -- RS is the `ker Gamma`
  sub-bundle of one Clifford module, not a decoupled field, so `image(phi_mc)` is dodged. That evasion is
  CONDITIONALLY_RESOLVED at 4D principal-symbol order only, and **overturnable at subprincipal order via
  FC-VZ-4 (the extrinsic curvature `II_s = s*(theta)` sourcing spacelike characteristics)** -- and `II_s` is
  exactly the field in ledger item 1. So VZ is not evaded for free; the source-action term is where the
  evasion is won or lost.

### 2.2 Porrati-Rahman 2009 -- causal charged spin-3/2 (THE cure template)

- **Result.** Porrati, Rahman, *Phys. Rev. D* 80 (2009) 025009 (arXiv:0906.1432): an explicit Lagrangian for
  a massive charged spin-3/2 field in a constant EM background that **propagates only the physical DOF inside
  the light cone.** VZ acausality, loss of hyperbolicity, and unphysical DOF are removed by a **judicious
  choice of NON-MINIMAL couplings `A^{munurho}(F)`, `B^{munu}(F)`, analytic near `F=0`** -- i.e. F-dependent
  terms that restore the secondary-constraint invertibility that minimal coupling destroys.
- **Template verdict for GU: THIS IS THE STRUCTURAL TEMPLATE FOR THE CURE TERM.** GU's needed object is
  literally "a non-minimal RS coupling enforcing `ker Gamma`" (ledger 6). Porrati-Rahman is the existence
  proof that such a non-minimal completion CAN restore constraint invertibility and causality for charged
  massive spin-3/2. The GU translation: their `A(F), B(F)` are the GU `theta`/shiab-sector non-minimal
  vertices; the RT-TRACE-DICHOTOMY 1-parameter family `wedge - 6*contract` is the GU analog of their
  non-minimal-coefficient tuning. **This does NOT rule out GU's keystone; it says the keystone is of a KNOWN
  constructible type.** Caveat (ARGUED): Porrati-Rahman is Abelian `U(1)` background and flat space; GU needs
  non-Abelian `Sp` background on curved Y14. The template transfers in structure, not verbatim.

### 2.3 Rahman 2011 -- the helicity-1/2 cutoff (the REAL quantitative no-go)

- **Result.** Rahman, "Helicity-1/2 Mode as a Probe of Interactions of Massive Rarita-Schwinger Field"
  (arXiv:1111.3366) and follow-ups: even with the causal non-minimal completion, the interacting massive RS
  EFT has a **model-independent finite UV cutoff `Lambda`**; the helicity-1/2 mode becomes strongly coupled
  there. All pathologies (onset of strong coupling, loss of causal propagation, unitarity violation) are
  captured by the helicity-1/2 sector. The clean high-energy behavior requires **gyromagnetic ratio `g = 2`**
  (the SUSY / string value).
- **Template verdict for GU: this is a genuine QUANTITATIVE OBSTRUCTION on the interacting-massive branch,
  and it is a MAJOR finding for the ledger.** It means: (i) a purely non-minimal (guardian-free) cure gives
  at best an EFT valid up to a finite `Lambda`, not a UV-complete interacting theory; (ii) restoring
  arbitrarily high-energy consistency requires either `g = 2` plus a tower (string-like) or a **guardian
  symmetry** (local SUSY / higher-spin gauge algebra) -- exactly what GU's prior waves named as the single
  missing datum (`source-action-necessary-conditions §4`). **So the literature independently reproduces GU's
  own conclusion: the guardian is not optional.** The free `mu_DW` (ledger 7) is plausibly the scale that
  sets this cutoff; that is a testable structural link, not yet computed.

### 2.4 Deser-Waldron 2001 -- partial masslessness / (A)dS phases

- **Result.** Deser, Waldron, PRL 87 (2001) 031601; Nucl. Phys. B607 (2001) 577; Phys. Lett. B513 (2001)
  137: in (A)dS, in the `(m^2, Lambda)` plane there are **gauge lines** where new gauge invariances appear
  (partial masslessness), dividing unitary from non-unitary regions; on those lines intermediate helicity
  sets propagate and null (causal) propagation is recovered.
- **Template verdict for GU: HELPS as a MAP of the `(m^2, Lambda)` plane, does not directly cure.** GU has an
  explicit `m^2`-`Lambda` link (ledger 7: `rho_Lambda = c_L mu_DW^4`, `m2 = sqrt(m2_eff) mu_DW`), so GU lives
  at a SPECIFIC point in the Deser-Waldron plane. **Actionable: check whether GU's `(m2_eff in [5/6,5/4],
  c_L=3/8)` point sits on or near a partial-massless gauge line** -- if it does, a gauge invariance
  (guardian) is switched on for free and the causal branch is the null-propagation one. This is a crisp,
  finite check the construction phase should run. Caveat: GU's gravity sector fails exact Schwarzschild and
  the (A)dS structure GU actually has is contested; the plane may not literally apply.

### 2.5 Zinoviev -- gauge-invariant (Stueckelberg / frame-like) massive higher spin

- **Result.** Zinoviev, "On massive higher spin fields" (hep-th/0108192) and the frame-like/multispinor
  series: a **gauge-invariant Lagrangian for massive higher-spin fields** built by adding Stueckelberg
  auxiliary fields so every massive gauge symmetry is realized (spontaneously broken). Provides a systematic
  cubic-vertex framework for consistent massive HS interactions.
- **Template verdict for GU: HELPS structurally -- it is the "make the constraint cohomological" template.**
  GU's necessary-conditions box (§3 of the prior wave) demands the gamma-trace be realized **cohomologically**
  (ghost-exact off-surface escape) rather than as a clean `ker Gamma` subspace. Zinoviev's Stueckelberg
  machinery is precisely the technology that trades a hard constraint for a gauge symmetry + auxiliary field.
  **But** GU is "constitutionally anti-gauge-fixing" (prior wave §4), so the Stueckelberg fields would have to
  be GU-native (from the `Sp` / Krein structure), not imported. Template applies to the METHOD, not off the
  shelf.

### 2.6 Buchbinder-Krykhtin-Pashnev -- BRST Lagrangian construction

- **Result.** Buchbinder, Krykhtin, Pashnev (e.g. Nucl. Phys. B711 (2005) 367) and successors: a **universal
  BRST/BFV construction** of gauge-invariant Lagrangians for massive and massless HS fields, where the
  constraints of the HS field become first-class and the physical field is BRST cohomology.
- **Template verdict for GU: HELPS -- it is the ghost-count / BRST-cohomology template GU's box needs.** GU's
  box asks for a BV action with `(S,S)=0`, `s^2=0`, and `Pi_RS^phys` as BRST cohomology with a ghost count
  `q = 1 - a` (prior wave §4). BKP is the standard route to exactly that. **Gap:** BKP supplies the ghost
  machinery but not the GU-specific datum fixing the slice or `q`; GU must supply that from the B-carrier /
  count-selector (ledger 5). So BKP is the scaffold; the count selector is the missing input.

### 2.7 Supergravity gravitino -- the ONE fully consistent massive-after-Higgs RS

- **Result.** de Wit-Freedman, Deser-Zumino: the gravitino is the gauge field of local SUSY; after
  super-Higgs it is a **consistent MASSIVE spin-3/2** whose subsidiary conditions are preserved by the SUSY
  algebra (not by an externally imposed constraint). This is the existence proof that a causal, unitary,
  interacting massive RS exists AT ALL.
- **Template verdict for GU: this is the GUARDIAN template, and it is the strongest cure candidate -- but it
  is the one GU does not currently have.** It evades VZ by VZ-H5 (a guardian: local SUSY), not by VZ-H1. GU
  has "no local SUSY structure as far as can be determined from the published record"
  (`oq-rs3-gu-vasiliev-comparison`). **The construction phase's single highest-value move is to test whether
  GU's `Sp(32,32;H)` + `[P,S]=0` commuting square secretly furnishes a local-SUSY / super-IG guardian** --
  Weinstein's own author-disclaimed ("Caveat Emptor") super-inhomogeneous-gauge direction. If yes, the cure
  is the gravitino template. If provably no, the interacting branch is Rahman-cutoff-bounded (finite EFT
  only). **This is the fork the whole keystone hinges on.**

### 2.8 Sagnotti-Taronna -- massive HS from string field theory

- **Result.** Sagnotti, Taronna, "String Lessons for Higher-Spin Interactions" (Nucl. Phys. B842 (2011) 299,
  arXiv:1006.5242): tree-level string amplitudes yield consistent cubic couplings for the massive HS tower;
  the tensionless limit gives the HS gauge couplings. The full **infinite Regge tower** is what makes the
  massive HS interactions UV-consistent (softening the high-energy behavior Rahman's cutoff otherwise bounds).
- **Template verdict for GU: RULES OUT a naive finite-content UV-complete cure, unless GU has a tower.** The
  string lesson is that a SINGLE massive HS field is only an EFT; UV completeness needs the tower. GU has
  **finite field content** (`Sp(64)` is finite-dim, dim 8256; no infinite tower -- `oq-rs3-gu-vasiliev-
  comparison` shows GU has no Vasiliev `hs(lambda)` truncation and lacks the AdS Vasiliev needs). **Structural
  consequence: GU's causal massive RS can be at best a Rahman-bounded EFT valid to `Lambda ~ mu_DW`-ish,
  UNLESS the guardian (§2.7) supplies the consistency the tower would otherwise supply.** This tightens §2.3:
  finite content + no guardian = finite-cutoff EFT, provably (ARGUED from Sagnotti-Taronna + Rahman jointly).

### 2.9 dRGT-analog for fermions / massive spin-2 lessons

- **Result.** de Rham-Gabadadze-Tolley ghost-free massive gravity: a specific non-minimal potential removes
  the Boulware-Deser ghost; the fermionic / spin-3/2 analog (partial results, e.g. massive spin-3/2 in
  bimetric backgrounds) is incomplete. Massive spin-2 coupled to EM (Rahman, arXiv:0801.2581) has an
  intrinsic cutoff, mirroring §2.3.
- **Template verdict for GU: WEAK template, cautionary.** dRGT shows a hand-tuned non-minimal potential can
  remove a ghost, which is encouraging by analogy for the "non-minimal cure removes the leak" thesis. But the
  fermionic dRGT-analog is not established, and the massive spin-2 cutoff result reinforces §2.3's bound.
  Net: supportive of the METHOD (tuned non-minimal terms), silent on GU specifically.

### Q1 synthesis (the causal-massive-higher-spin verdict)

**TEMPLATE EXISTS (Porrati-Rahman non-minimal completion + supergravity guardian), NOT a clean no-go -- but
with a real quantitative obstruction (Rahman helicity-1/2 cutoff) on the guardian-free branch, and GU's
finite content (no Regge tower) forces the fork onto the guardian.** Precisely:

- The cure term is of a **known constructible type** (Porrati-Rahman non-minimal; §2.2). GU is not obstructed
  at the classical-causality level.
- A **guardian-free** cure yields at best a **finite-cutoff EFT** (Rahman §2.3 + Sagnotti-Taronna §2.8,
  jointly). This is the honest limit: not "impossible", but "not UV-complete without more".
- A **UV-complete** interacting massive RS requires a **guardian symmetry** (local SUSY / super-IG; §2.7).
  GU's prior waves already named this as the single missing datum; the literature independently confirms it.
- **The decisive open question is therefore GU-internal, not a literature gap:** does `Sp(32,32;H) + [P,S]=0`
  furnish a local-SUSY guardian? That is a construction-phase computation, not a survey question.

---

## 3. Q2 -- Bootstrap / positivity / swampland applicability

How each machine would carve the coupling coefficient space of the source action.

### 3.1 EFT positivity bounds (Adams-Arkani-Hamed-Dubovsky-Nicolis-Rattazzi 2006)

- **Machine.** JHEP 10 (2006) 014 (hep-th/0602178): analyticity + unitarity + Froissart boundedness of the
  2->2 amplitude force the leading forward-scattering EFT coefficient to be **strictly positive** (`c > 0`),
  else no Lorentz-invariant, causal, unitary UV completion exists. Higher `s^n` derivatives give a full
  **convex cone** of allowed coefficients.
- **How it carves GU.** The non-minimal cure term has a 1-real-parameter family (`wedge - 6*contract`,
  RT-TRACE-DICHOTOMY). **Positivity bounds turn that line into a half-line or interval: the forward
  amplitude's `c_2` coefficient built from the cure vertex must be `> 0`.** This is computable from the cubic
  vertex ALONE (no full action needed), so it is the **cheapest available discriminator** and belongs at the
  top of the methods menu. Caveat (HURT): the standard AADNR bounds assume a **unitary** UV completion; GU's
  non-compact `Sp(32,32;H)` + Krein indefinite metric means naive positivity may be replaced by a
  **Krein-positivity** (pseudo-unitary) variant -- the bounds still exist but the inner product is
  `[P,S]=0`-graded, not positive-definite. So the lever applies in a MODIFIED form; establishing the modified
  form is itself a construction-phase task.

### 3.2 S-matrix bootstrap for massive (spin-2 + spin-3/2)

- **Machine.** Numerical/analytic 2->2 bootstrap (Paulos-Penedones-Toledo-van Rees-Vieira lineage; recent
  spinning extensions) carves the space of consistent massive amplitudes by imposing crossing + unitarity +
  the correct Regge behavior.
- **How it carves GU.** Would bound the allowed cubic/quartic couplings of a coupled spin-2 + spin-3/2
  system, potentially pinning the ratio of the RS coupling to the gravitational coupling. **Medium leverage:**
  powerful but heavy machinery, and it again presumes a unitary S-matrix; GU's Krein structure and the fact
  that GU's gravity sector is itself unbuilt (no Einstein equations derived) make a full spin-2+3/2 bootstrap
  premature. Better AFTER the guardian question (§2.7) is settled.

### 3.3 Weinberg-Witten / Porrati soft theorems

- **Machine.** Weinberg-Witten (1980): no interacting massless spin >= 3/2 with a Lorentz-covariant conserved
  current (or spin > 2 with conserved stress tensor). Porrati (2008, arXiv:0804.4672): a massless spin-3/2
  minimally coupled to gravity is inconsistent unless it is a SUSY gauge field (gravitino).
- **How it carves GU.** **This RULES OUT the massless-RS branch outright.** If GU tried to keep the RS field
  massless and interacting, Weinberg-Witten/Porrati forbid it absent SUSY. **Therefore GU's RS MUST be
  massive (the `mu_DW`-massive branch), and if it were ever massless-interacting it would need to BE a
  gravitino.** This is a clean branch-elimination: it collapses the field-space to the massive branch and
  re-derives the guardian requirement from the massless side. HELP (removes a branch), and consistent with
  ledger 7 (`m2 != 0`).

### 3.4 Landscape statistics (Douglas)

- **Machine.** Douglas-type flux-vacua counting: statistical distribution of EFT parameters over a
  discretuum.
- **How it carves GU.** **Low relevance for THIS problem.** GU's residual is a rigid **2-bit** field-space
  declaration (A/B binary + the 1-parameter cure line), not a large discretuum. Statistics over a
  near-deterministic residual buys nothing. (This is the methods-menu reason Monte-Carlo landscape survey
  ranks low, §7.)

### 3.5 Swampland criteria

- **Weak Gravity Conjecture.** Requires a state with `q >= m` (in Planck units). GU's charged massive RS
  carries SM + `Sp` charge; WGC would impose a **lower bound on the RS charge-to-mass ratio**, i.e. a
  constraint linking the `Sp` coupling to `mu_DW`. Potentially a real carve, but presumes GU embeds in a
  quantum-gravity-complete setting -- unestablished. **ARGUED, speculative.**
- **Distance Conjecture.** Large field excursions (here, large `mu_DW`?) bring towers of light states. GU has
  **no tower** (§2.8) -- so either `mu_DW` excursions are bounded, or GU is not in the QG landscape at all.
  This is a **tension worth flagging**, not a computed constraint.
- **No global symmetries.** GU's `Sp(32,32;H)` must be gauged (it is, as the IG connection), so no obvious
  violation. **The sharper swampland tension is the non-compactness + 4th-order (`box^2`/Stelle) structure:
  4th-order gravity is non-unitary in the ordinary sense (the Stelle ghost), and the swampland/positivity
  program broadly disfavors it unless the ghost is a Krein-hidden partner** -- which is exactly GU's ledger-4
  claim (`[P,S]=0`, Bateman-Turok hidden-ghost parity). So the swampland pressure on the 4th-order structure
  is **precisely what the Krein construction is meant to absorb**; whether it succeeds is the open ledger-4/8
  positivity question, not a new swampland no-go.

### Q2 synthesis (top levers)

1. **EFT positivity (AADNR) on the cure coefficient** -- cheapest, computable from the cubic vertex, turns
   the 1-parameter line into a sign-definite interval; caveat = must be Krein-modified.
2. **Rahman helicity-1/2 cutoff** (positivity-adjacent) -- prices the guardian-free branch as finite-EFT.
3. **Weinberg-Witten / Porrati** -- eliminates the massless branch, forces massive + re-derives guardian.

Swampland is mostly a consistency backdrop here (the non-compact + 4th-order tension is what Krein must
absorb), and landscape statistics is near-irrelevant given the 2-bit residual.

---

## 4. Q3 -- HAVE / HELP / HURT map

### 4.1 What we already HAVE (narrows the construction)

- **A finite, 1-parameter invariant basis for the cure.** The constraint-preserving coupling space is
  `wedge - 6*contract` (`t* = -1/6`), NOT a free tensor space (RT-TRACE-DICHOTOMY, COMPUTED prior wave). This
  is the strongest narrowing we hold: the cure is a line, not a space.
- **A discrete A/B binary + a UNIQUE count carrier B** (ledger 5; index -38, order-3, gamma-trace-constrained).
  The field-space declaration is a rigid 2-bit residual (`sg4-forcing-rubric-complete`).
- **The `[P,S]=0` commuting square** (ledger 4) as an organizing principle: it is the candidate guardian
  algebra and the ghost-parity bookkeeping in one object.
- **An exact, reproduced obstruction measurement:** `C2 = 155.36`, degree-1 homogeneous, non-integer, NOT an
  index (COMPUTED, two independent constructions agree). We know precisely what leaks and that it is a
  symbol-norm, so the cure target is a symbol-level (differential-operator) object, not a topological one.
- **A pinned SHAPE for the missing object** (prior wave §3): a BV action with `(S,S)=0`, `s^2=0`, gamma-trace
  cohomological via a NON-EQUIVARIANT compensator `sigma_c(xi)`, carrying a VZ guardian.
- **The soldering/connection collapse (COMPUTED here):** items 2 and 9 are one datum (codim-8165 = "image is
  so(9,5)"), so one fewer free knob.

### 4.2 What HELPS (levers + templates)

- **Templates that plausibly instantiate the cure:** Porrati-Rahman non-minimal completion (§2.2, closest
  structural match); supergravity super-Higgs gravitino (§2.7, the UV-complete guardian route); Zinoviev
  Stueckelberg + BKP BRST (§2.5-2.6, the "constraint becomes cohomological" machinery the box demands).
- **Positivity bounds** (§3.1) collapse the 1-parameter line to a sign-definite interval, computable from the
  cubic vertex alone.
- **Weinberg-Witten/Porrati** (§3.3) eliminate the massless branch for free.
- **The Deser-Waldron `(m^2, Lambda)` map** (§2.4): GU sits at a specific point (`c_L=3/8`, `m2_eff in
  [5/6,5/4]`); a finite check tells us if it is on a partial-massless gauge line (guardian for free).
- **Finite field content + finite invariant basis** make deformation theory tractable: the moduli of
  consistent deformations of the minimal operator is finite-dimensional, so the search is a finite algebraic
  problem, not a functional one.

### 4.3 What HURTS (the real obstacles)

- **The Rahman helicity-1/2 cutoff (§2.3) + finite content / no Regge tower (§2.8):** guardian-free, the
  causal massive RS is at best a finite-`Lambda` EFT, provably. This is the hardest structural fact against a
  clean UV-complete keystone. **MAJOR.**
- **The VZ subprincipal escape FC-VZ-4:** the extrinsic curvature `II_s` (ledger 1) can re-source spacelike
  characteristics at subprincipal order; the 4D evasion is only CONDITIONALLY_RESOLVED and reconstruction-
  grade. The cure must survive this order, which is unbuilt.
- **The free `mu_DW`** (ledger 7): a genuinely free scale means the cutoff/mass are not pinned from inside;
  the falsifiability keystone is also the thing positivity/swampland cannot fully fix without an external
  datum.
- **The non-compact `Sp(32,32;H)`** (ledger 3): blocks naive positivity/unitarity imports -- the bounds
  become Krein/pseudo-unitary variants that must be re-derived. Also the source of the 4th-order Stelle-ghost
  tension (ledger 10) that the Krein construction must absorb (ledger 4/8), which is itself open.
- **The soldering choice is unforced** (ledger 9/2): even collapsed to one knob, `theta`-to-spin-lift is a
  DECLARATION, not a derivation. p-hacking risk: a free build fits anything (`sg4-forcing-rubric`), so the
  honest form is a forced construction with no known internal forcing mechanism.
- **GU's written canon shiab `(1,0,1,0)` is gamma-traceFUL** (COMPUTED, §1): the cure must REVISE the written
  formula, so "reconstruct GU as written" and "make it causal" are in tension -- a cost that must be paid
  openly.

---

## 5. Q4 -- The methods menu, ranked by expected leverage FOR THIS problem

Ranked highest-leverage first. Top 3 carry a one-line why.

1. **Positivity / consistency-carving (EFT bounds, Krein-modified).** *Why:* the cure is already a
   1-parameter line; a forward-scattering positivity bound computable from the cubic vertex alone collapses
   it to a sign-definite interval -- maximum narrowing per unit work, no full action needed.
2. **Invariant-basis + deformation theory.** *Why:* finite field content + the RT-TRACE-DICHOTOMY 1-parameter
   family make "consistent deformations of the minimal operator" a finite algebraic (cohomology-of-the-BV-
   differential) problem, exactly the object the necessary-conditions box asks for, with a computable answer.
3. **Amplitudes / on-shell (helicity-1/2 high-energy behavior).** *Why:* Rahman shows every pathology lives
   in the helicity-1/2 mode; computing its high-energy amplitude is the single sharpest diagnostic of whether
   a candidate cure is finite-cutoff or UV-complete, and it directly tests the `g=2` / guardian fork.
4. **Bootstrap / consistency-carving (full S-matrix, spin-2 + spin-3/2).** Heavier; better after the guardian
   question is resolved and a gravity sector exists.
5. **Ablation** (drop each ledger constraint, see what breaks). Useful for auditing which constraints are
   load-bearing (already surfaced items 2/9 collapse); cheap sanity, moderate leverage.
6. **Deformation theory as a standalone** (subsumed into 2).
7. **Monte-Carlo landscape survey.** Low: the residual is a 2-bit declaration, not a discretuum -- nothing to
   sample.
8. **Bayesian posterior.** Low: no meaningful prior/likelihood over a near-deterministic residual; would
   dress up a 2-bit choice as inference.

---

## 6. Optional light test

`tests/wave34/soldering_codim_and_causal_window.py` (deterministic, exit 0). Two crisp COMPUTED anchors:

- **(A) Soldering dimension count.** `dim sp(64,H) = 8256`, `dim so(9,5) = 91`, `codim = 8165` -- confirms
  ledger item 9's "codim-8165" is arithmetically identical to "the soldered image is a copy of `so(9,5)`"
  (ledger item 2). **Finding: items 2 and 9 are one datum, not two.**
- **(B) Causal-window sign toy.** A schematic scalar characteristic factor showing the Porrati-Rahman sign
  mechanism (uncured coupling displaces the characteristic zero off the null cone -> acausal branch; cured
  keeps it on the null cone). **Flagged ARGUED / toy only** -- it illustrates the mechanism, it is NOT the RS
  characteristic determinant and proves nothing about GU's operator.

---

## 7. Honest limits

- **No construction was attempted or achieved.** This is Phase 1. The source action stays unbuilt; no claim
  is promoted; no canon/ledger movement.
- **The literature transfer is structural, not verbatim.** Porrati-Rahman is Abelian + flat; GU needs
  non-Abelian `Sp` on curved Y14. Supergravity is the guardian template but GU's guardian is unestablished.
  "Template exists" means "an object of this type has been built elsewhere", not "GU's object is built".
- **The Rahman-cutoff obstruction is a real, quantitative finding but is branch-conditional:** it bounds the
  GUARDIAN-FREE interacting massive branch. It is NOT a universal no-go on GU's keystone -- the guardian route
  (§2.7) is exactly the escape, and its viability is a GU-internal open question, not settled here.
- **Positivity/swampland levers presume ingredients GU may lack:** a unitary (vs Krein) S-matrix, a
  quantum-gravity embedding. Their application to GU is in MODIFIED form and each modification is itself a
  research task. I have not established the Krein-positivity bounds; I have argued they are the right object.
- **The VZ evasion GU relies on is CONDITIONALLY_RESOLVED at reconstruction grade only** (subprincipal order
  open, FC-VZ-4; E-block invertibility same-session-circular, FC-VZ-1). Nothing here upgrades that.
- **`C2 = 155.36` and all rep-theory dimension counts are reproduced/COMPUTED; everything about "who has a
  template" and "how a bound would carve" is ARGUED from the cited literature read as data.**

---

## 8. Net

The GU keystone is **hard but not obstructed**: a causal, interacting, massive RS coupling of the required
non-minimal type has a **construction template in the literature** (Porrati-Rahman), and a **UV-complete**
version has a template too (the supergravity gravitino) -- but only via a **guardian symmetry GU has not yet
shown it possesses**, and the guardian-free route is **provably a finite-cutoff EFT** (Rahman + Sagnotti-
Taronna, given GU's finite content). The single decisive question is therefore GU-internal and
construction-phase: **does `Sp(32,32;H) + [P,S]=0` furnish a local-SUSY / super-IG guardian?** The search is
maximally narrowed by the two facts we hold -- the cure is a **1-real-parameter family** (`wedge -
6*contract`) and the residual is a **2-bit declaration** -- which is why **positivity-carving and
invariant-basis/deformation theory are the top methods** (a line collapsed by a sign bound), and why
landscape statistics / Bayesian methods buy nothing here.
