---
artifact_type: exploration
status: exploration (W137 / ISS-3; hypothesis-generation wave, propose-then-kill posture; 5-persona inline team; one deterministic test)
created: 2026-07-14
hypothesis: "W137 -- the per-observer-slice structure: give Joe's reading (observer = a slice of the geometry; issuance consumed to create records; capability matching between collective and single observer) the repo's actual mathematical skeleton, and sort every piece into THEOREM / CONJECTURE / GATED-TO-SIBLING"
title: "W137 VERDICT: the slice = section mapping is ALREADY-THEOREM-GRADE machinery (section sigma: X4 -> Y14, induced metric, II, ambient (9,5) gimmel with parallel Pi and K -- H15/H21/H25/W126/W131); the issuance-consumption reading acquires its first computed face: the pointwise deformation-cost bookkeeping of a section is EXACT and WELL-DEFINED (rational polynomial in the 2-jet) but SIGNED, not positive -- the constant section is not a critical point of the cost density (linear term -8u against the a0 = 2 issuance constant, exact) and the second-order cost form is INDEFINITE (exact directions +32 w^2 and -32 w^2 inside the traceless sector; gradient sector 16 eta(dphi,dphi) on the computed axes) -- so 'records cost issuance' survives only as signed bookkeeping, not as a positive ledger; the collective/single MATCHING is proposed as one sharp GU-side conjecture (C1: the observer's admissible record space = the section-localized compression of the C-operator's maximal positive subspace, honestly conditional on W132's keep-and-grade <=> C-operator equivalence) with four kill conditions; the W130 3:2:1 Einstein-sector split is a PER-DEFORMATION-SECTOR fact computed at ONE section -- whether it varies per section is a named, decidable conjecture (C3), not a current fact. Capability MEASURE gated to TaF; issuance-vs-disclosure gated to temporal-issuance. Nothing rebuilt on the dead Krein-TT physical leg, the B2 rate reading, or the H36 window."
grade: "exploration / hypothesis-generation. COMPUTED (exact sympy, this wave, tests/W137_observer_slice_deformation_cost.py, 14/14 exit 0): the deformation-cost results (D1-D3) on the conformal family in the pinned Convention-B construction, double-routed against the W126 slice decomposition before extraction. THEOREM-CITED (not re-derived): the section/ambient machinery (H15/H21/H25, W126 a0 = 2 and degree-2 termination, W131 parallel Pi/K and (9,5) verification, W130 native operator and 3:2:1 split, W132 expansion identity). CONJECTURE: C1 (record space = C-compression), C2 (boundary-balance of record cost), C3 (section-dependence of the 3:2:1 split) -- each stated with kill conditions, none asserted. GATED: capability measure (TaF), issuance/disclosure typing (TI). NO canon / RESEARCH-STATUS / claim-status / verdict / posture change."
depends_on:
  - explorations/W126-beyond4th-vacuum-lift-2026-07-13.md
  - explorations/W130-native-graviton-oneloop-block-2026-07-14.md
  - explorations/W131-covariant-operator-y14-2026-07-14.md
  - explorations/W132-graded-optical-theorem-physical-subspace-2026-07-14.md
  - explorations/CONJECTURE-source-action-is-the-observer-2026-07-11.md
  - explorations/path4-branchC-observerse-bridge-2026-07-11.md
  - explorations/cross-repo-survey-taf-ti-2026-07-11.md
  - explorations/misc/substrate-layer-for-observer-issuance-integration-2026-06-30.md
  - canon/firewall-boundary-hypothesis.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W137_observer_slice_deformation_cost.py
---

# W137 -- The per-observer-slice structure: skeleton, theorems, conjectures, gates

**Role.** Joe's framing (direct chat, hypothesis-generation wave 2026-07-14): *the observer has
its own slice of the geometry; the full geometry is how it applies to any given individual
observer; the issuance (dark energy) is consumed by observers to create records; the source
action transduces it, harnessing capability spaces matched between the collective and the single
observer.* This wave gives that framing the repo's actual mathematical skeleton, sorts every
piece into GU-SIDE-THEOREM / GU-SIDE-CONJECTURE / BELONGS-TO-TaF / BELONGS-TO-temporal-issuance,
and computes the one piece that was computable this wave (the deformation-cost bookkeeping).
Posture: propose-then-kill; every conjecture below carries its kill conditions.

Five personas inline, sequentially, one context, no sub-agents: (1) differential geometer,
(2) Krein specialist, (3) category theorist, (4) honesty auditor, (5) adversarial skeptic.
Deterministic test: `tests/W137_observer_slice_deformation_cost.py` (14/14, exit 0).

Standing kills honored throughout (nothing below rebuilds on them):

- The PHYSICAL Krein-TT observer leg is walled/mooted (W84 type-III wall; W122 positive-norm
  verdict; H61 dropped as mooted in the 2026-07-14 landscape). Everything here that touches
  Krein structure uses only the LINEAR C-operator algebra of W132, never the antilinear modular
  conjugation J or type-III Tomita-Takesaki.
- B2's "issuance RATE" reading is FALSE by the repo's own rate-independence finding
  (path4-branchC: rates are absorbed and enter no structural theorem; f_0 is structural, not a
  rate). Only the OBSTRUCTION/bookkeeping reading is built on here. No statement below is a rate.
- H36's DE-scale window is EXCLUDED-CITED (H52); nothing here asserts a DE magnitude.

## 0. Construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md), named

| Object | Construction used | Why |
|---|---|---|
| The observer's slice | program-native: a SECTION sigma: X4 -> Y14 = Met(X4) of the observerse bundle, literal-graph embedding, Convention B (the H15/H21/H25/W126 pinned machinery) | this is the repo's only reconstruction-grade candidate for "a slice of the geometry"; the standard-field alternative (a worldline/frame bundle observer) has no repo machinery and is not defaulted to |
| The full geometry | the ambient (Y14, gimmel), signature (9,5) = base (3,1) + DeWitt fiber (6,4), W131-verified pointwise with O(9,5) holonomy | the "collective" object every section sits inside |
| The cost density | pointwise `W = |II|^2` of the section, Convention-B vertical representative + normal lift, evaluated on the conformal family at E0 = 1 | the exact sector where the repo has all-orders exact results (W126); the deformation-cost computation lives here |
| Admissible records | fork CARRIED, it IS conjecture C1: (i) free-grading positive subspace (DEAD as a unitarity carrier, W132), (ii) C-operator positive subspace (the live candidate), (iii) per-observer sectorial objects (the W94-retraction lesson) | the fork is the result; see Section 3 |
| Issuance | GU-side shadow ONLY: the Lambda-channel constant a0 = 2 = -2 Lambda of the induced functional (W126/W130). Whether it is "issuance" in TI's sense is GATED | one-way rule; GU is the substrate layer only (substrate-layer pointer, 2026-06-30) |

## 1. Persona 1 -- differential geometer: the slice = section formalization, and what is already theorem

### 1.1 The mapping table (the wave's requested deliverable)

| Joe's concept | Repo object | Status |
|---|---|---|
| "The observer has its own slice of the geometry" | a section sigma: X4 -> Y14 with its literal-graph embedding; per-section data: the induced metric gbar = sigma*(gimmel), the second fundamental form II_sigma, the pointwise cost density W = \|II\|^2, the effective 4D quadratic operator around sigma | GU-SIDE-THEOREM (construction exists and is machine-checked: H15/H21/H25, W126, W130 Stage A) |
| "The full geometry is how it applies to any given observer" | the ambient (Y14, gimmel) restricted along sigma via the Gauss formula: ambient curvature = induced curvature + II-squared terms; W131 verified the Gauss identity at native n = 4 with II_s nonzero | GU-SIDE-THEOREM (classical submanifold geometry, machine-witnessed on the actual gimmel metric) |
| Section-INDEPENDENT (the collective invariants) | signature (9,5) on the Lorentzian locus; O(9,5) holonomy; the projector Pi parallel for EVERY metric-compatible connection ([nabla, Pi] = 0 is a theorem, all 91 generators); Krein K parallel (nabla K = 0); the characteristic variety = the gimmel null cone; the constant a0 = 2 of the pinned construction | GU-SIDE-THEOREM (W131, W126) |
| Section-DEPENDENT (the per-observer variation) | gbar, II_sigma, W(sigma) pointwise, and the induced quadratic operator's coefficients around sigma | THEOREM that they are section-tied objects; which coefficients actually VARY across sections is conjecture C3 |
| "Observers consume issuance to create records" | the signed deformation-cost bookkeeping of W = \|II\|^2 under a section deformation, with the zeroth-order term the Lambda-channel constant a0 = 2 | COMPUTED THIS WAVE (Section 1.2): bookkeeping exists and is exact; positivity is FALSE; only the signed form survives |
| "The source action transduces it" | the W125/W131 covariant operator D = Pi (gamma nabla) Pi + m2 Pi on ker Gamma over Y14 | GU-SIDE-CONJECTURE at the "transduction" level; the operator itself is BUILT at frame/symbol level (W131), its analytic layer is the named open residual |
| "Capability spaces matched between collective and single observer" | conjecture C1 (C-operator compression, Section 3) + the descent structure (Section 4) | GU-SIDE-CONJECTURE (stated with kills) |
| The capability MEASURE (how much an observer can do) | TaF's C(R), equality/screening-off certificates, no-scalar-ranking theorems | BELONGS-TO-TaF (tri-repo division, ratified 2026-07-02) |
| Whether consumption is genuine ISSUANCE (vs disclosure of what was already there) | TI's D-FORK and effect typing Issue[S]/Project[O]/Finalize[R]/Lose[K] | BELONGS-TO-temporal-issuance |

On the W130 question the brief asks directly: the 3 : 2 : 1 Einstein-sector split
(gamma_TT : gamma_phi : gamma_slice, both measures, all positive) is a computed fact about the
quadratic form around ONE section (the constant section). As it stands it is a
PER-DEFORMATION-SECTOR effect at a fixed slice: the effective coupling normalization depends on
WHICH mode the slice is deformed in, not (yet) on WHICH slice the observer occupies. Whether it
is additionally a per-observer-slice effect is exactly conjecture C3 (Section 5), and it is
decidable with existing machinery.

### 1.2 The deformation-cost computation (COMPUTED, exact, this wave)

The GU-side shadow of "record creation costs issuance": deform a section and read the exact
change in the pointwise cost density W = |II|^2 against the constant a0 = 2 that every point of
the constant section carries (the DeWitt-Lambda channel, = -2 Lambda with Lambda = -1, W130).
All results exact sympy on the conformal family, double-routed against the W126 slice
decomposition `W = 2 + R/3 + (8/9) R^2 - 4 Ric^2` before extraction
(`tests/W137_observer_slice_deformation_cost.py`, 14/14, exit 0):

- **The bookkeeping is well-defined.** W of any 2-jet deformation is an exact rational
  polynomial (curvature slice) or exact rational function (gradient sector) of the jet data.
  No regularization, no truncation. "Record creation has a GU-side energy bookkeeping" is TRUE
  in this precise sense.
- **D1 (first order): the constant section is NOT a critical point of the cost density.**
  Along the MSS direction sigma = u eta: `W(u) = 2 - 8u - 64u^2` exactly (the W126 interpolant
  re-derived by direct evaluation). The linear term -8u is the Einstein channel a1 = 1/3 with
  R = -24u. So a record-creating deformation exchanges cost with the a0 = 2 constant already at
  FIRST order: there is a genuine, nonzero coupling between the Lambda-channel constant and
  section deformation. (Consistent with, and the pointwise face of, W130's statement that flat
  space is not a stationary point of the induced functional.)
- **D2 (second order): the cost form is INDEFINITE.** Exact directions, same magnitude,
  opposite signs, INSIDE the traceless sector: s_01 = w (mixed time-space) gives
  `W = 2 + 32 w^2` (the deformation PAYS); diag(0, w, -w, 0) (purely spatial traceless) gives
  `W = 2 - 32 w^2` (the deformation RELEASES). MSS gives -64 u^2. Gradient sector: timelike
  dphi gives -16 w^2, spacelike gives +16 w^2 (series 2 + 16 v^2 + 320 v^4 reproduced on the
  spacelike axis), i.e. consistent with a covariant `16 eta(dphi, dphi)` on the two computed
  axes (observation, not a theorem for the full form).
- **D3 (one exact point each way):** sigma = (1/10) eta gives W = 14/25, cost -36/25;
  s_01 = 1/10 gives W = 58/25, cost +8/25.

**The honest verdict on "records cost issuance":** as a POSITIVE ledger (every record costs,
cost is monotonically consumed) it is FALSE pointwise in the |II|^2 density -- some deformations
release density, and the sign is graded by the Lorentzian/causal structure of the deformation
(time-space mixing pays; purely spatial traceless and conformal-trace release; timelike gradient
releases, spacelike pays). What survives, computed, is SIGNED bookkeeping with a nonzero
first-order exchange against the a0 = 2 constant. Any TI-side consumption story must either
live with the signature grading or locate the positive ledger in a DIFFERENT functional (the
integrated action with its measure, a boundary term, or the C-metric inner product), each of
which is a named conjecture below, not a fact.

## 2. Persona 2 -- Krein specialist: the record-space conjecture (the click the brief asked for)

W132 proved, exactly: for any Krein-pseudo-unitary S, the physical-subspace S-matrix on the
FREE grading is an expansion (`A^dag A = P_+ + B^dag B`), so keep-and-grade unitarity is
equivalent, without remainder, to the existence of an interacting C-operator; and the C-operator
selects a maximal positive subspace `H_C+` of the Krein space -- a per-quantization choice of
"what counts as physical." That is structurally the same shape as "the observer's admissible
record space." Stated as a conjecture, honestly conditional:

**CONJECTURE C1 (admissible records = C-compression).** Let the GU keep-and-grade quantization
admit an interacting C-operator C (equivalently, by W132, let keep-and-grade be unitary in the
only sense available to it). For an observer slice sigma with region algebra A(sigma), define
the admissible record space R(sigma) as the space of physical fluctuation modes of sigma
(the states an observer at sigma can finalize into records). Then:

1. R(sigma) = P_sigma H_C+ -- the sigma-localized compression of the C-operator's maximal
   positive subspace; and
2. the "collective/single matching" is the statement that ONE section-independent C determines
   EVERY observer's R(sigma): the collective object is C (equivalently the positive metric
   eta_+ = eta C on the full Krein space); the single-observer object is its compression.

What this buys if true: "capability spaces matched between the collective and the single
observer" becomes a precise compatibility statement -- the same positive subspace, viewed
ambient-globally (collective) and compressed per-section (single observer) -- and the W132
result that no FREE-grading subspace works becomes the statement that the matching cannot be
done observer-locally without the collective object C. That is exactly the shape of Joe's
framing, in the repo's own operators.

**Kill conditions for C1 (each named, each actionable):**

- **K1 (existence).** No interacting C-operator exists for the GU quantization (branch B is
  open: order-by-order in QM only). By W132's equivalence this would kill keep-and-grade
  unitarity itself, and C1 dies with its right-hand side empty. Settling object: the W48
  minimal source-action loop computation, computing B and the C-metric.
- **K2 (locality clash).** C is provably non-local (W54, hardened; exponential localization
  ~1/m at one loop). If R(sigma) must be strictly local to the slice's region and the
  compression P_sigma H_C+ fails to define a subspace compatible with A(sigma) (e.g. the
  compressed metric loses positivity or invertibility at the region boundary), the
  identification fails. Concrete first test: in the W54 free model, compute the compressed
  metric P_sigma eta_+ P_sigma on a half-space region and check positivity + bounded
  invertibility. If it degenerates, C1 is dead in the strict-local reading and must retreat to
  the exponentially-quasi-local reading (which would then need its own defense).
- **K3 (section-dependence of C).** If the maximal positive subspace genuinely varies with the
  section (background-dependent quantization), there is no single collective C and clause 2
  fails. The W94-retraction arc is the precedent that exactly this failure mode is live: the
  global object may not exist while per-observer objects cohere only at CLASS level (W107).
  C1's honest fallback is then "matching at interface-class level, not operator level" -- a
  strictly weaker conjecture that must be relabeled if forced there. If even class-level
  coherence of the compressions fails, C1 is fully dead.
- **K4 (route discipline).** C1 must never be argued through the antilinear modular
  conjugation J or type-III Krein-TT: that leg is walled (W84) and mooted (W122/landscape).
  The statement above uses only the linear C and subspace compressions. Any proof attempt that
  is forced to route through type-III Krein-TT is dead on arrival by prior kills; C1 itself
  would remain open but unprovable by that route.

**Status: GU-SIDE-CONJECTURE.** Nothing asserted. The resonance is real but currently
structural only: both objects are "the selected positive subspace that defines what counts as
physical/recordable." No computation yet distinguishes it from coincidence of shape; K2's
first test is the cheapest discriminator and is tractable with existing W54 machinery.

**CONJECTURE C2 (boundary-balanced record cost).** The GU-side form of "issuance is supplied
through the boundary": for a section deformation of compact support, the first variation of
the integrated |II|^2 action splits into a bulk term (the signed bookkeeping of Section 1.2)
plus a boundary term, and the "consumption" reading requires the balancing supply to enter
through the boundary term. Kill condition, sharp: for COMPACTLY supported deformations the
boundary term vanishes identically (standard variational calculus), so if the bulk bookkeeping
does not integrate to zero against the deformation family, the balance must fail for compact
records -- in that case "issuance enters at the boundary" is FALSE for compact records and the
reading must retreat to non-compact/asymptotic deformations. That retreat has a repo-native
landing spot: the W103 tail-quotient slot (a positive invertible metric AT INFINITY on the
asymptotic Krein-null line) -- the one typed interface the wall analysis left standing. If the
retreat is forced AND the W103 slot cannot host the balance, C2 is dead. Status:
GU-SIDE-CONJECTURE; the bulk half is COMPUTED (this wave), the boundary half is a named
integration-by-parts computation nobody has run on Y14 sections (tractable next wave).

## 3. Persona 3 -- category theorist: collective vs single, kept to one page

The temptation is a limit/colimit framework over the category of sections. The repo's own
results say which half of that is right, so state only that:

- **The collective is NOT the colimit of the slices.** The W94 retraction and W98 break are
  exactly the failure of gluing per-observer objects into one global object: adjacent regions'
  modular data disagree on overlaps under interaction; the God's-eye operator does not exist.
  Any "the full geometry = colimit of observer slices" claim is DEAD by that precedent unless
  it works at a coarser level.
- **The coarser level exists and is computed: descent of CLASSES, not operators.** W107: the
  per-region tail/interface CLASSES cohere on overlaps (with non-triviality controls) even
  though the operators do not. So the correct concrete statement of "capability spaces matched
  between collective and single observer" at the categorical level is: the assignment
  sigma -> (interface class of sigma) is a section of a sheaf-like structure that DOES descend,
  while sigma -> (operator data of sigma) does not. Matching lives one categorical level up
  from where the naive reading puts it.
- **The ambient side needs no gluing.** The section-independent invariants (Section 1.1) are
  not glued from slices; they are ambient facts (W131 theorems). The two-level structure is:
  ambient invariants (given, collective), interface classes (descend, shared), operator data
  (per-observer, does not glue). That three-row ladder IS the concrete collective/single
  structure, and each row's status is already computed or theorem-cited. No new framework is
  proposed.

Status: the ladder's rows are THEOREM (ambient, W131), THEOREM-ON-MODEL (class descent, W107),
and THEOREM (operator non-gluing, W94/W98/W84). The identification of Joe's "matching" with
row 2 is a READING, i.e. conjecture-grade labeling of proven structure, not a new claim.

## 4. Persona 4 -- honesty auditor: the tri-repo gate, enforced line by line

- GU-SIDE-THEOREM (cited): section machinery, ambient invariants, a0 = 2, degree-2
  termination, [nabla, Pi] = 0, nabla K = 0, the W132 expansion identity, the 3:2:1 split at
  the constant section, W107 class-coherence (on its model), W94/W98 non-gluing.
- GU-SIDE-COMPUTED (new, this wave): D1 linear term -8u; D2 indefiniteness with exact
  directions (+32/-32 traceless pair, -64 MSS, -16/+16 gradient axes); D3 exact-point costs
  -36/25 and +8/25.
- GU-SIDE-CONJECTURE: C1 (with K1-K4), C2 (with its vanishing-boundary kill), C3 (Section 5).
- BELONGS-TO-TaF: any MEASURE of capability (how much, rankings, certificates). This wave
  makes no capability-measure claim. The word "capability" above always refers to the GU-side
  spaces, never their measure.
- BELONGS-TO-temporal-issuance: whether the signed bookkeeping is genuine issuance
  (Issue[S]) versus disclosure (Project[O]); the D-FORK. This wave supplies TI with one exact
  input through the one-way gate: IF TI's consumption story imports the GU |II|^2 shadow, it
  inherits a SIGNED, causally graded ledger, not a positive one. Stated as stress-test input,
  never as support (one-way rule).
- "Dark energy = issuance" is used ONLY as Joe's framing vocabulary; GU-side, the object is
  the Lambda-channel constant a0 = 2 = -2 Lambda. No DE magnitude, no equation of state, no
  H36-window statement is made or implied.
- Nothing here changes canon, RESEARCH-STATUS, claim status, or any verdict.

## 5. Persona 5 -- adversarial skeptic: kills, and the THIS-IS-POETRY steelman

**Steelman (full strength):** "Observer slices, issuance, records -- this is vocabulary written
onto submanifold geometry that was already there. B2 already showed the observerse bridge adds
no forced content: the geometry is unchanged if you strip the words. W137 is the same poem with
newer citations."

**Where the steelman lands (conceded):** the TRANSDUCTION clause ("the source action transduces
issuance, harnessing capability spaces") is PRE-MATHEMATICAL as of this wave. No GU object
performs a transduction; the covariant operator exists (W131) but nothing connects its action
to the Lambda-channel bookkeeping. Labeled accordingly; no theorem-adjacent language used for it
anywhere above. Likewise "consume": the computed ledger is signed, so consumption-language
overstates what the mathematics does.

**Where the steelman fails (the required computable statement exists):** the wave produced new
exact numbers that the poem-free geometry did NOT already state: the first-order exchange -8u
between a section deformation and the a0 = 2 constant, the exact indefinite pair +32/-32 inside
the traceless sector, the causal grading of the gradient-sector cost, and the exact-point costs
-36/25 / +8/25. These are theorems of the pinned construction whether or not one likes the
observer vocabulary, and they DECIDE something about the reading: they falsify the
positive-ledger version of "records cost issuance" and leave only the signed version alive.
A reading that can be partially falsified by computation is not poetry; the parts that cannot
yet be are labeled pre-mathematical above.

**CONJECTURE C3 (per-observer coupling normalization), with its decision procedure.** The W130
split gamma_TT : gamma_phi : gamma_slice = 3 : 2 : 1 was computed around the constant section.
C3: the ratio is a constant of the construction (section-INDEPENDENT); the rival reading (the
per-observer-slice interpretation of Joe's framing) predicts it varies with the background
section. Decision: rerun the W130 Stage-A quadratic-form extraction around ONE non-flat
background jet (the evaluator already accepts arbitrary metric 2-jets; the only new work is
bookkeeping the background-covariant channel split). Either outcome is informative: ratio moves
= first computed per-observer-slice coupling effect; ratio fixed = the split is ambient and the
per-slice reading loses its best current candidate. NOT run this wave (the channel split around
a curved background needs a covariant mode decomposition that does not exist yet in the test
suite; flagged as the cheapest next decisive computation for this thread).

**Kill-consistency sweep (required by the brief):** no statement above depends on the Krein-TT
physical leg (K4 enforces this inside C1; Sections 3-4 use only linear-C and class-level
objects); no statement is a rate (the bookkeeping is per-deformation, not per-time; B2's
surviving obstruction reading is the only B2 content used); no statement touches the H36
window. Checked against W122/W79 (tachyon chain: untouched -- the indefinite cost form here is
the POINTWISE jet-level face of the same DeWitt signature facts, not a new vacuum claim).

## 6. Verdict

- **Slice = section: already theorem-grade.** Joe's "observer's own slice" has a complete,
  machine-checked GU skeleton; nothing needed inventing. Per-slice: induced geometry, II, cost
  density, quadratic operator. Collective: (9,5) gimmel, parallel Pi and K, null-cone symbol,
  a0 = 2.
- **Issuance consumption: first computed face, and it is SIGNED.** The bookkeeping exists and
  is exact; positivity is false; the constant section is not a cost critical point (-8u); the
  second-order form is indefinite with exact witnesses. "Records cost issuance" survives only
  as signed bookkeeping. (14/14 checks, exit 0.)
- **Collective/single matching: one sharp conjecture (C1)** -- admissible records = the
  section compression of the C-operator's positive subspace, conditional on W132's equivalence,
  with four kill conditions of which K2's compressed-metric test is cheapest; plus the computed
  three-row ladder (ambient invariants / descending classes / non-gluing operators) as the
  categorical form of "matching," which is proven structure under a conjectural label.
- **The W130 3:2:1 split: per-deformation-sector fact at one section today; per-observer-slice
  effect only if C3's decision computation says so.**
- **Gates held:** capability measure to TaF; issuance-vs-disclosure to TI; transduction and
  consumption labeled pre-mathematical where they are.

## 7. What this does NOT do

No canon / RESEARCH-STATUS / claim-status / verdict / posture change. No new physics claim: the
computed results are jet-level identities of the pinned Convention-B construction on the
conformal family, sharing all of W126's convention flags (normalization, measure fork in the
gradient sector). C1/C2/C3 are conjectures with kills, not results. No TI or TaF claim is made
or supported (one-way rule). H59, H61a, the firewall-boundary hypothesis, and the AF-vs-AS fork
are all untouched.

**Artifacts:** this file + `tests/W137_observer_slice_deformation_cost.py` (14/14, exit 0).
