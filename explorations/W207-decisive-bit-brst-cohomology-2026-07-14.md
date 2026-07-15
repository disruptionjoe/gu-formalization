---
artifact_type: exploration
status: exploration (R9 Dirac-BRST / constraint cohomology; one of five parallel methods on the decisive bit; five viewpoints inline in one worker, no sub-agents; deterministic test 31/31 exit 0, positive controls first)
created: 2026-07-14
wave: W207
label: W207
posture: coherence-first (Joe 2026-07-14); exploration grade; conditional register; truth-seeking (a clean negative is as valuable as FORCED; do not root); RUTHLESS self-verification; tri-repo gating STRICT
route: DIRAC-BRST / CONSTRAINT COHOMOLOGY (physical inner product = invariant pairing on H^0(Q); build on W173's closed-not-exact record class)
title: "W207 VERDICT: RESIDUAL-BIT-STANDS (R9 / Dirac-BRST route). Take the good-stable fixed point as GIVEN (real total spectrum; positive-definite TOTAL metric; C-operator operative, eta_+ = eta*C). Its STABILIZER = the gauge/counterfactual deformations preserving those properties = the C-COMMUTANT inside so(9,5), which is so(9)+so(5) (dim 46), or DeWitt-refined so(3)+so(6)+so(4) (dim 24). The space of invariant symmetric bilinear forms under that stabilizer is dim 2 (coarse) / dim 4 (fine), spanned by {eta, eta*C} -- NOT dim 1. Both spectral sections eta*C_+ (record-count mode Krein-NEGATIVE) and eta*C_- (record-count POSITIVE) are stabilizer-invariant and independent. Therefore the stabilizer does NOT force the C-operator GRADING SIGN: it recovers W203's eta ONLY UP TO grading. The record-count grading is a Z/2 Godel-independent bit that must be POSITED, identified with the UNBUILT C2-closing spectral section (Y14 connection-curvature 2-form) W173 flagged. Positive-definiteness of the total metric selects a 2-parameter positive CONE inside the invariant space, not a single ray, so eta*C is one posited point, not a derived one. bar(b) does NOT clear; #1 does NOT resolve inside GU by this route. GUARDRAIL HONORED: W203's Schur=eta (nulldim 1 under the FULL group) is reproduced as PC0 precisely to isolate -- and NOT be mistaken for -- the open grading bit."
grade: "EXACT for the finite-dimensional group-cohomology facts (machine-verified 31/31, residuals 0 to 1e-9): (a) FULL so(9,5) invariant symmetric forms = dim 1 = eta (W203 Schur reproduced, the guardrail); (b) the C-commutant stabilizer = so(9)+so(5) dim 46, preserves both eta and eta*C; (c) its invariant symmetric-form space = dim 2 = span{eta, eta*C}, eta and eta*C independent; (d) the DeWitt-refined stabilizer so(3)+so(6)+so(4) dim 24 gives dim 4, and BOTH spectral sections eta*C_+ / eta*C_- are invariant and independent; (e) the good-stable data reproduced (C^2=1 nontrivial; eta*C positive-definite; record-count fiber modes Krein-negative, W168; Cl(9,5) Krein anti-self-adjoint gauge action, W131/W203). STRUCTURAL for the BRST lift: the identification of the invariant H^0(Q) pairing with the 14-frame invariant-form space is the standard Dirac-BRST fact that the physical inner product is the constraint-invariant pairing on cohomology; the record class it grades is W173's closed-not-exact mirror (that toy is reproduced as PC1, not recomputed on M(64,H) here). ARGUED for the identification of the free Z/2 of spectral sections with W173's UNBUILT C2-closing datum (both are a distinguished-null-plane / grading choice; a proof of identity is not attempted). NO canon / claim-status / verdict / posture change; bar(b)/H59 NOT flipped (report only, Joe-gated). Count {1,3} untouched. No cross-repo identity claim (whether the Krein grading is physically operative stays TaF-flagged). Zero em dashes in paper-facing text."
construction: "program-native where the objects are GU's (Y14 frame, the (9,5) Clifford/Krein metric eta and its gauge action Sigma, the C-operator = record/geometric grading, the (9,5)=(3,1)+(6,4) base/DeWitt-fiber split with record-count Krein-negative on the fiber, the mirror = closed-not-exact record class from W173's free BV bicomplex). Standard-field where the machinery binds any construction (Schur's lemma / the invariant-bilinear-form count on a rep and its subgroups -- reused from W203; the Dirac-BRST identification of the physical inner product with the invariant pairing on H^0 of the constraint algebra -- PORTED; the maximal-compact = metric-preserving subgroup of an indefinite orthogonal group -- standard). Forks named per GEOMETER-VS-PHYSICS-OBJECTS.md: the stabilizer = C-commutant identification is program-native (it is the subgroup keeping C operative); the spectral-section Z/2 = the C2-closing datum is the carried conditionality (unbuilt, external). Tri-repo gating STRICT: the invariant-form dimensions are computed GU-side; whether the Krein grading is physically operative is TaF-owned; no cross-repo identity asserted."
depends_on:
  - explorations/W173-brst-cohomology-mirror-sector-2026-07-14.md
  - explorations/W203-branch3-source-action-fixed-coefficients-2026-07-14.md
  - explorations/W168-reduction-krein-signature-2026-07-14.md
  - explorations/W202-signature-crux-bach-branch-2026-07-14.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W207_decisive_bit_brst_cohomology.py
---

# W207 -- the decisive bit via R9 (Dirac-BRST / constraint cohomology)

Test: `tests/W207_decisive_bit_brst_cohomology.py` (31/31, exit 0). Deterministic. Five viewpoints ran
inline in one worker, sequentially (no sub-agents): (1) BRST/constraint-quantization specialist,
(2) representation-theorist, (3) geometer of the (3,1)+(6,4) DeWitt split, (4) coherence-first
synthesizer, (5) skeptic. Positive controls run first.

## 0. The decisive question, and the R9 route

Take the good-stable fixed point as GIVEN: real total spectrum; positive-definite TOTAL metric;
C-operator operative (`eta_+ = eta*C`). Its STABILIZER is the group of gauge/counterfactual
deformations that preserve those good-stable properties. Compute the space of invariant symmetric
bilinear forms under that stabilizer.

- **FORCED** = dim 1 AND generator `eta_+ = eta*C` (record-count mode Krein-negative). Then the
  C-grading SIGN is DERIVED, #1 resolves inside GU, bar(b) clears.
- **RESIDUAL-BIT-STANDS** = dim > 1 (a Z/2: both `eta*C_+` and `eta*C_-` invariant), or only `eta`
  up to grading. Then the grading sign is a Godel-independent bit that must be POSITED.

The R9 route computes the invariant physical pairing as the constraint-invariant pairing on `H^0(Q)`
of the Dirac-BRST complex, building on **W173**: in GU's free BV bicomplex the mirror/ghost sector is
**BRST-closed-not-exact = a RECORD = a nontrivial H-class** (it lies ON `ker Gamma` so is not
Koszul-Tate-exact; `im d_A` is transverse to `ker Gamma`, RS norms 73.48 / 343.73, so within
`ker Gamma` it is not ghost-exact). The physical inner product is the invariant pairing on that
cohomology; the open bit is the Krein SIGN of the record class in it.

## 1. The guardrail (PC0), stated up front

**W203 already forced the UNGRADED metric to `eta`** by Schur: under the FULL gauge group `so(9,5)`
the invariant symmetric form is unique (nulldim 1) and equals the Clifford metric `eta`, signature
`(9,5)`. The test reproduces this as **PC0b/PC0c** (dim 1, `~ eta`). That is NOT the open bit. The
open bit is whether the **stabilizer** (a SUBGROUP) forces the **C-operator grading sign**
`eta_+ = eta*C` with the record-count mode negative. PC0d records the key structural fact that makes
this a real question: `eta*C` is NOT invariant under the full group (which is exactly why W203's Schur
killed the grading). The whole computation below is about what happens when you pass from the full
group to the good-stable stabilizer.

## 2. The stabilizer is the C-commutant `so(9)+so(5)`

The good-stable data says "C-operator operative". A deformation that keeps C operative must commute
with C (it preserves the C-grading); a deformation preserving the Krein form stays in `so(9,5)`. The
intersection is the **C-commutant of `so(9,5)` = `so(9)+so(5)`** (dim 46; **STAB1**, machine-checked).
Equivalently, this is the maximal compact -- exactly the subgroup that ALSO preserves the
positive-definite total metric `eta*C` (**STAB2/STAB3**). It is a PROPER subgroup (46 < 91): the
counterfactual boosts that break the C-grading are excluded (**STAB4**), and that is precisely what
lets the invariant-form space grow relative to W203.

## 3. The decisive count: dim 2, not dim 1

The invariant symmetric forms under the stabilizer are **dim 2** (**DIM1**), NOT dim 1. The space is
exactly `span{eta, eta*C}` (**DIM2**), and `eta` and `eta*C` are independent (**DIM3**). So the
restriction from the full group makes the C-graded metric `eta*C` NEWLY invariant, alongside W203's
`eta`. The stabilizer recovers `eta` **only up to grading**: it does not single out `eta*C` over
`eta` (**DIM4**). By the pre-registered criterion this is **RESIDUAL-BIT-STANDS**, not FORCED.

## 4. The record-count SIGN is free: both spectral sections invariant (FIB)

Refine to the physically-honest stabilizer that ALSO preserves the `(9,5)=(3,1)+(6,4)` DeWitt split
(the W168/W202 arena, **FIB1**): it is `so(3)+so(6)+so(4)` (dim 24; **FIB2**), and its invariant
symmetric forms are **dim 4** -- one per block: base-space, base-time, geometric fiber, record-count
fiber (**FIB3**). Within that dim-4 space the record-count block's sign is an INDEPENDENT parameter:
both `eta*C_+` (record-count Krein-NEGATIVE, the W168 assignment) and `eta*C_-` (record-count
POSITIVE, the fiber-negative block of C flipped) are stabilizer-invariant (**FIB4/FIB5**) and
independent (**FIB6**). That independent pair IS the Z/2 residual.

## 5. BRST reading: `H^0(Q)` does not privilege a section (H0)

In Dirac-BRST quantization the physical inner product is the invariant pairing on `H^0(Q)`. By
Sections 3-4 that pairing is a 2- (coarse) / 4- (fine) parameter family, and the coefficient on the
record-count (fiber-negative) block is the self-pairing sign of the W173 record class. It is a free
parameter = the choice of **spectral section**, which is exactly the UNBUILT Y14 connection-curvature
2-form / C2-closing datum W173 flagged. The test reproduces W173's D6 control: the record class has a
well-defined Krein self-norm sign in a GIVEN section (`-1`, **H0a**), but the opposite section flips
it to `+1` (**H0b**), and both sections are legitimate nilpotent closed complexes -- `H^0` privileges
neither. Positive-definiteness of the total metric does NOT rescue FORCED: it selects a 2-parameter
positive CONE (`a,b>0` on the geometric and record blocks), not a single ray (**H0c**), so `eta*C`
(the `a=b` point) is one posited choice, not a derived one. Hence the C-grading sign is
Godel-independent within GU (**H0d**).

## 6. Verdict and honest limits

**VERDICT: RESIDUAL-BIT-STANDS (R9 / Dirac-BRST route).** The stabilizer-invariant symmetric-form
space is dim 2 (C-commutant `so(9)+so(5)`) / dim 4 (DeWitt-refined `so(3)+so(6)+so(4)`), spanned by
`{eta, eta*C}`, with both spectral sections `eta*C_+` and `eta*C_-` invariant. **Residual group =
Z/2** (the two sections), realized as the free record-count block sign inside a 2/4-dim invariant
space; positive-definiteness selects a cone, not a ray. The C-operator grading sign (record-count
mode negative) is therefore NOT forced by the stabilizer -- it must be POSITED, identified with the
unbuilt C2-closing / Y14-curvature datum. bar(b) does NOT clear; #1 does NOT resolve inside GU by this
route.

Honest limits. The count is exact finite-dimensional group cohomology; the BRST lift is structural
(the `H^0(Q)`-pairing = invariant-form identification is the standard Dirac-BRST fact, and the record
class it grades is W173's toy mirror, reproduced not recomputed on `M(64,H)`). The identification of
the free Z/2 with W173's specific C2 datum is ARGUED, not proved. No fifth object: the residual is the
SAME already-named spectral-section / C-operator datum W132/W173 need. This is a truth-seeking clean
negative, not a root: it says the good stable, by itself, underdetermines the grading; a genuine
FORCED would require an EXTERNAL datum (the spectral section) that the good-stable stabilizer does not
carry.

## Convergence note

This R9 (Dirac-BRST) result says the good-stable stabilizer is the **C-commutant** `so(9)+so(5)` and
its invariant symmetric-form space is **dim 2** (`span{eta, eta*C}`), so the C-grading sign is NOT
forced: **RESIDUAL-BIT-STANDS, residual Z/2** (the two spectral sections). The decisive lever is
group-theoretic and method-independent (the dimension of an invariant-form space is a Schur count),
so the four sibling methods should be read as cross-checks of the SAME lever from different entry
points:

- **Agreement with R16 (counterfactual).** R16 varies the good-stable by counterfactual deformations;
  agreement means R16 finds the SAME stabilizer (the C-commutant) and the SAME 2-dim / Z/2
  freedom. If R16 instead finds a counterfactual deformation that is admissible yet moves `eta*C`
  relative to `eta` -- i.e. a stabilizer element NOT in the C-commutant -- that would CONTRADICT this
  result and reopen FORCED (the stabilizer would be smaller than `so(9)+so(5)` and could pin the
  ratio). Watch specifically whether R16's admissible deformations all commute with C.

- **Agreement with R7 (Lawvere) and R12 (topos).** These compute the same fixed-point invariants by a
  fixed-point / classifying-object route. Agreement means their invariant-object count is also 2 (a
  Z/2 of sections), i.e. the record grading appears as a genuine choice of section/subobject, not a
  theorem. A FORCED verdict from R7/R12 -- a unique fixed point with a canonical grading -- would
  mean their category encodes an EXTRA constraint (a distinguished spectral section) that the bare
  linear stabilizer here does not see; that extra constraint would then have to be named and its
  provenance (external vs GU-native) adjudicated, since if it is GU-native it overturns this negative.

- **Agreement with R1 (Helmholtz).** R1's decomposition should split the invariant pairing into the
  same geometric-vs-record blocks; agreement means the record block's sign is an independent DOF
  there too. If R1 finds the Helmholtz decomposition is UNIQUE with a forced record sign, the
  disagreement localizes to whether positive-definiteness (a cone here) is supplemented by a further
  positivity/monotonicity condition that collapses the cone to a ray.

**Reading the convergence.** If R16/R7/R12/R1 also land on dim > 1 / a Z/2, the five methods CONVERGE
on RESIDUAL-BIT-STANDS and the grading sign is a genuine posit (identified with the unbuilt spectral
section) -- consistent with W173's own QUANTIZATION-DEPENDENT verdict. If any sibling returns FORCED,
the decisive diagnostic is WHERE its extra constraint enters: a smaller-than-C-commutant stabilizer
(R16), a distinguished subobject (R7/R12), or a supplementary positivity (R1). That extra constraint,
if real and GU-native, would be the object that clears bar(b); if external, it confirms this negative
and relocates #1 onto the spectral-section datum. Either way the disagreement is fully localized and
Joe-adjudicable, not a wash.
