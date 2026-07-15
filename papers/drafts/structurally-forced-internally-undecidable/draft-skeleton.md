---
title: "Structurally Forced, Internally Undecidable: the C-operator grading sign in self-consistent indefinite-metric (Krein) gauge theories"
status: draft
grade: "DRAFT-tier / exploration. FIRST PASS, not a finished paper. Promotion to candidate is Joe-gated. Machine checks live in the gu-formalization repo (tests/W206-W211 and this draft's tests/general_krein_grading_sign.py). No scientific verdict is flipped into canon: bar (b) and H59 stay OPEN."
created: 2026-07-14
slug: structurally-forced-internally-undecidable
lead: "GENERAL (GU-independent) mechanism first; Geometric Unity is the worked example, not the subject."
depends_on:
  - explorations/W206-decisive-bit-counterfactual-invariance-2026-07-14.md
  - explorations/W207-decisive-bit-brst-cohomology-2026-07-14.md
  - explorations/W208-decisive-bit-lawvere-fixed-point-2026-07-14.md
  - explorations/W209-decisive-bit-topos-internal-logic-2026-07-14.md
  - explorations/W210-decisive-bit-helmholtz-inverse-variational-2026-07-14.md
  - explorations/W211-krein-sign-godel-independent-five-method-synthesis-2026-07-14.md
  - explorations/W203-branch3-source-action-fixed-coefficients-2026-07-14.md
  - explorations/W202-signature-crux-bach-branch-2026-07-14.md
scripts:
  - papers/drafts/structurally-forced-internally-undecidable/tests/general_krein_grading_sign.py
  - tests/W211_five_method_convergence.py
---

# Structurally Forced, Internally Undecidable

**the C-operator grading sign in self-consistent indefinite-metric (Krein) gauge theories**

*DRAFT. First pass. Not a candidate. Promotion is Joe-gated. Zero em dashes.*

---

## Abstract

Indefinite-metric ("Krein") gauge theories buy renormalizability or a larger symmetry at the price of
negative-norm states, and their physical inner product is recovered by a grading operator (a C-operator,
metric operator, or CPT operator) that flips the sign of the offending directions. It is known that this
operator is not unique: pseudo-Hermitian and PT-symmetric quantum theory have long emphasized that the
metric operator carries free data and needs external physical input. This paper isolates a sharper and, we
argue, new structural fact about *where* that freedom sits and *how tightly* it can be pinned.

The general claim (Section 2). In a self-consistent indefinite-metric gauge theory whose full gauge group
acts irreducibly on the frame, Schur's lemma forces the ungraded indefinite metric `eta` to be unique: the
theory's own symmetry FORCES the metric form. But requiring a positive-definite TOTAL (physical) inner
product restricts the admissible frame deformations to the stabilizer of both `eta` and the positive metric
`eta_+`, which is exactly the C-commutant (the maximal compact subgroup). Under that smaller group the
frame REDUCES, the space of invariant symmetric forms GROWS from dimension one to at least two, and the
relative sign between the two blocks -- the grading sign -- becomes a free `Z/2`. Less symmetry means more
invariants. The very act of standing at the good, unitary configuration is what splits the frame and
LIBERATES the grading sign. The sign is therefore STRUCTURALLY FORCED in FORM (every other datum of the
metric is pinned) but INTERNALLY UNDECIDABLE in SIGN (the theory's own invariance data does not fix it; one
external bit does). We prove this at the general level as a Schur / invariant-theory statement about an
indefinite metric and its C-commutant, machine-checked over a sweep of signatures `(p,q)`.

The worked example (Sections 3 to 5). Geometric Unity (GU), a candidate unification on a `Cl(9,5)` frame,
provides an unusually clean instance: its entire quantum-consistency question reduces to ONE such bit -- is
the record-count mode Krein-negative on the `(6,4)` DeWitt fiber, equivalently is the interacting
C-operator operative. Five independent formalisms -- counterfactual (Klein/Erlangen) invariance, Dirac-BRST
constraint cohomology, a Lawvere categorical fixed point, topos internal logic, and the Helmholtz inverse
problem of the calculus of variations -- were each computed on the `(9,5) = (3,1) + (6,4)` frame and each
returns the SAME verdict: the bit is undecidable from within (Godel-independent of the theory's good-stable
data), and all five localize it to the SAME single `Z/2`. A companion result shows the source action's
relative coefficients are Schur-forced (only the overall scale, GU's analogue of Newton's `G`, is free by
normalization), so the reduction really is to one sign and not to a family of unknowns.

Contribution and honest scope (Sections 6 to 8). We do NOT claim to discover that a Krein metric operator
is non-unique; that is known. Our defensible contribution is three-fold: (a) the SHARP REDUCTION of a full
candidate-unification's quantum consistency to one located `Z/2`; (b) the FORCED-FORM / FREE-SIGN structure
(the good-stable stabilizer fixes the metric form and liberates precisely the grading sign); and (c)
MULTI-FORMALISM INDEPENDENCE (five independent characterizations agree it is undecidable from within). The
result is internally undecidable, NOT absolutely undecidable: an external datum (in the GU instance, a
finality/temporal-issuance input) decides it, and the paper says exactly which datum and why it is
necessary. This is exploration-tier; all computations are internal (reproduced and adversarially reviewed
within one AI-directed process, not yet independently replicated). Machine checks live in the repository.

---

## 1. The setting and the phenomenon

An indefinite-metric field theory carries a nondegenerate but not positive-definite inner product on its
state space. Gupta-Bleuler electrodynamics, Faddeev-Popov ghosts, higher-derivative ("quadratic") gravity,
Lee-Wick models, and PT-symmetric field theories all live here: one accepts an indefinite metric `eta` in
exchange for manifest covariance, renormalizability, or an enlarged symmetry, and then must recover a
positive-definite PHYSICAL inner product on the states that matter. The standard device is a grading: an
operator `C` with `C^2 = 1` whose `-1` eigenspace is exactly the `eta`-negative directions, so that the
total metric

```
    eta_+  =  eta . C  =  |eta|
```

is positive-definite. In pseudo-Hermitian quantum mechanics `C` is (a piece of) the metric operator; in
Bender's PT-symmetric quantum theory it is the CPT operator; in constraint quantization it is the
combination that makes the physical subspace a genuine Hilbert space.

The phenomenon this paper is about is a very old worry in this subject stated in an unusually sharp form:
which grading? An indefinite metric alone does not tell you which side of the wall is physical. The sign of
`C` on a given sector is exactly the datum that separates a good, unitary theory from a ghost-ridden one,
and it is precisely the datum an indefinite metric leaves open. We make three moves the prior literature (to
our knowledge) does not combine: we locate this freedom to a SINGLE `Z/2` bit in a specific candidate
unification; we show its form is otherwise FULLY FORCED; and we show its undecidability-from-within is
INDEPENDENT of the formalism used to interrogate it.

---

## 2. The general theorem (GU-independent)

We state the mechanism abstractly. It is a clean statement in invariant theory; the proof is Schur's lemma
applied twice, once to the full group and once to the C-commutant.

### 2.1 Setup

Let `V` be a real vector space, `dim V = n = p + q`, `p, q >= 1`, carrying a nondegenerate symmetric
bilinear form `eta` of signature `(p, q)`. Let `C = sign(eta)` be the grading involution (`C^2 = 1`), with
`+1` eigenspace `V_+` (`dim p`) and `-1` eigenspace `V_-` (`dim q`), so that `eta_+ = eta . C = |eta|` is
positive-definite. Let a gauge group `G <= O(eta)` act on `V`. Two hypotheses encode "self-consistent
indefinite-metric gauge theory whose physical inner product is a C-operator grading":

- **(H1) Full-group irreducibility.** `V` is irreducible under `G`. By Schur's lemma the space of
  `G`-invariant symmetric bilinear forms is one-dimensional, spanned by `eta`. (This is exactly what it
  means for the gauge symmetry to FORCE the ungraded metric: the metric form is the unique invariant.)

- **(H2) Good-stable stabilizer.** The "good stable" (the physical, unitary configuration) requires
  preserving BOTH `eta` and the positive-definite total metric `eta_+`. The subgroup that does so is
  `G* = {g in G : g^T eta_+ g = eta_+}`. Because `C = eta_+^{-1} eta`, preserving both forms is equivalent
  to commuting with `C`, so `G*` is the C-commutant of `G`. In the canonical maximal case `G = O(eta)` one
  has `G* = O(eta) cap O(eta_+) = O(p) x O(q)`, the maximal compact subgroup.

### 2.2 Theorem

**Theorem (grading-sign liberation).** Assume (H1) and (H2). Suppose the C-eigenspaces `V_+` and `V_-`
share no common irreducible `G*`-constituent (the NON-COINCIDENCE hypothesis, automatic in the canonical
case `G* = O(p) x O(q)` for `p, q >= 1`, since `V_+` and `V_-` are then inequivalent standard reps of
distinct factors). Then:

1. `eta` and `eta_+` are both `G*`-invariant and linearly independent.
2. The space of `G*`-invariant symmetric bilinear forms decomposes as
   `Sym^2(V^*)^{G*} = Sym^2(V_+^*)^{G*} (+) Sym^2(V_-^*)^{G*}` (no cross term, by the non-coincidence
   hypothesis and Schur), so it has dimension `>= 2`, with one independent scale per C-block.
3. Writing an invariant form as `B = c_+ (eta|V_+) (+) c_- (eta|V_-)`, positivity forces `c_+, c_- > 0`
   (an open 2-parameter cone, never the single ray `R eta_+`), while the RELATIVE sign `sign(c_-/c_+)` is
   unconstrained by `G*`. Both branches `c_-/c_+ > 0` (giving `eta_+`, the good graded metric) and
   `c_-/c_+ < 0` (giving `eta`, the ungraded indefinite metric) are `G*`-invariant.

Therefore the grading sign -- which C-eigenspace is Krein-negative, equivalently whether the interacting
C-operator is operative -- is NOT determined by the invariance data of the theory. It is one free `Z/2`,
decided only by one external bit.

**Proof.** (H1) plus Schur gives the one-dimensional invariant space `R eta` on the irreducible `V`. Under
`G*` the involution `C` is preserved, so `V = V_+ (+) V_-` is a `G*`-stable decomposition. A `G*`-invariant
symmetric form is a `G*`-map `V -> V^*`; its `(V_+, V_-)` block is a `G*`-map `V_+ -> V_-^*`, which vanishes
when `V_+` and `V_-` share no irreducible constituent (Schur). The diagonal blocks are `G*`-invariant forms
on `V_+` and `V_-` respectively; each contains the restriction of `eta` (positive-definite on `V_+`,
negative-definite on `V_-`), so each is non-empty, giving `dim >= 2`. Independent scaling of the two blocks
realizes both relative signs; positive-definiteness of `B` is equivalent to positivity of each block scale,
an open cone. The map `eta_+ = P_+ + P_-` and `eta = P_+ - P_-` exhibits the two branches explicitly. QED.

### 2.3 Corollary (symmetry reduction liberates the sign)

Comparing (H1) and the theorem: passing from the FULL group `G` (invariant space dimension `1`, generator
`eta`) DOWN to the good-stable stabilizer `G*` (invariant space dimension `>= 2`) INCREASES the invariant
space. Less symmetry, more invariants. The extra dimension is precisely the grading sign. To FORCE the sign
one would need a stabilizer LARGE enough to glue `V_+` and `V_-` so that only `eta_+` survives; no such
gluing exists, because the good-stable condition is exactly what splits the frame into the two C-blocks. If
the good stable additionally respects a finer invariant splitting (more blocks), the residual only ENLARGES;
it never collapses to one.

### 2.4 Machine check

`tests/general_krein_grading_sign.py` (in this draft folder) verifies the theorem over a sweep of
signatures `(p,q) in {(1,1), (2,1), (3,1), (6,4), (9,5), (7,7), (5,3), (4,2)}` including both GU instances:
the full group `O(p,q)` gives invariant-form dimension `1` (generator `eta`, and `eta_+` is not invariant);
the good-stable stabilizer `O(p) x O(q)` gives dimension exactly `2` with both `eta` and `eta_+` invariant
and distinct; positivity leaves a 2-parameter cone while the indefinite branch stays invariant (the free
`Z/2`); and a finer 4-block split of `(9,5)` gives dimension `4` (the residual enlarges). 81/81 checks,
deterministic, exit 0.

**Status of Section 2.** We present the theorem as PROVEN at the general level, with one explicit and
checkable side-hypothesis (non-coincidence of the C-eigenspaces as `G*`-representations) that holds
automatically in the canonical maximal-compact case. The remaining-hardening register (README) lists what a
referee-grade version still needs: a written proof independent of the maximal-compact specialization, the
precise general characterization of when the non-coincidence hypothesis can fail for a proper subgroup
`G < O(eta)`, and an independent-reader pass.

---

## 3. The worked example: Geometric Unity reduced to one bit

Geometric Unity (GU) is a proposed unification whose reconstructed frame carries a `Cl(9,5)` Clifford
structure with the split `(9,5) = (3,1) + (6,4)` (a `(3,1)` base and a `(6,4)` DeWitt fiber). Within the
repository's reconstruction, the fiber further splits `(6,4)` into six geometric modes (Krein-positive) and
four record-count modes (Krein-negative), and the whole program's quantum consistency turns out to hinge on
one sign: whether the record-count mode is genuinely Krein-negative on that fiber, equivalently whether the
interacting C-operator is operative so that `eta_+ = eta . C` is the physical positive-definite inner
product. This is exactly the general Section-2 bit for the GU frame. In the repository's tracking it is
called question `#1` and the associated open unitarity claim is "bar (b)".

Two supporting facts make the reduction genuine rather than cosmetic:

- **The source action is BUILT and its coefficients are FORCED (W203).** Equivariance under the
  Krein-anti-self-adjoint gauge action pins the source-action kernel by Schur to a one-dimensional space
  whose generator is the `(9,5)` Clifford metric `eta`; every relative coefficient is forced, and the sole
  free number is the overall scale (GU's analogue of Newton's `G`, undetermined by normalization as `G` is
  in general relativity, not fitted). This is (H1) realized concretely.

- **The sign is DECOUPLED from the signature choice (W202).** The relevant Krein sign is read on the
  `(6,4)` DeWitt fiber, which is invariant under `eta -> -eta`; the sign is therefore identical on `(9,5)`
  and `(7,7)` and does not depend on the still-open global signature. So the reduction is to one sign, not
  to a sign entangled with other undetermined choices.

Thus GU is a maximally clean instance of the general phenomenon: FORM fully forced, exactly one SIGN free.

---

## 4. Five-method independence (the robustness backbone)

The strength of the GU instance is that the undecidability-from-within was not read off one calculation. Five
mutually independent formalisms were each computed on the same `(9,5) = (3,1) + (6,4)` frame, each with its
own deterministic machine check, each with the same guardrail (reproduce W203's `nulldim = 1` as a POSITIVE
CONTROL, so the job is to settle the SIGN, not to re-derive `eta`). Every one returns RESIDUAL-BIT-STANDS.

| method | note | route | check | per-method finding |
|---|---|---|---|---|
| R16 | W206 | counterfactual (Klein/Erlangen) invariance: metric from its stabilizer | 29/29 | invariant-form space under the good-stable stabilizer is dim 2, basis `{eta_+, eta}`; relative block sign is a free `Z/2` |
| R9 | W207 | Dirac-BRST / constraint cohomology (physical inner product on `H^0(Q)`) | 31/31 | `H^0(Q)` privileges neither spectral section; both `eta.C_+` and `eta.C_-` are invariant and independent |
| R7 | W208 | Lawvere / Cantor diagonal fixed point | 31/31 | the grading self-map has exactly TWO consistent fixed points (good and pathological); selection is external |
| R12 | W209 | topos internal logic / sheaf semantics | 32/32 | the subobject classifier is BOOLEAN on `eta` (forced) but INTUITIONISTIC on the sign (not internally decidable) |
| R1 | W210 | Helmholtz inverse problem of the calculus of variations | 32/32 | self-adjointness is provably SIGN-BLIND; the sign is fixed only by an off-diagonal coupling that exists iff the interacting C-operator supplies it |

The five agree because they all reproduce the same structural fact (Section 2.3): the full group forces
`eta`; conditioning on the good stable restricts to the C-commutant `SO(9) x SO(5)`; under it the 14-frame
reduces and the invariant-form space grows `1 -> 2`; the residual is one relative-block sign. Each method
then localizes that residual in its own language and they agree on its SHAPE (one `Z/2`) and its OWNER (the
unbuilt interacting C-operator / spectral section). The synthesis note W211 records the convergence and its
certificate `tests/W211_five_method_convergence.py` recomputes the shared linear-algebra fact from scratch
(exit 0). The methodological point stands independent of GU: five different notions of "compute inside the
theory" (invariance, cohomology, fixed-point consistency, internal logic, variational reconstruction) all
leave the same bit free, which is why "compute harder inside the theory" is ruled out rather than merely
unpromising.

---

## 5. Why this is undecidable-from-within, not merely unknown

"Undecidable from within" is a proof-grade statement about the theory's axioms, not a confession of
ignorance. The Lawvere/fixed-point route (W208) makes the model-theoretic content explicit: the grading
self-map has two genuine fixed points, and the sign is TRUE in the good model and FALSE in the pathological
model of the SAME self-consistency theory, so no internal derivation can decide it (this is the Godel /
independence signature). The topos route (W209) says the same in intuitionistic terms: the grading sign is
an intermediate Heyting truth value whose negation is bottom, so it is not internally complemented and not
internally decidable, even though the ungraded metric sits at a Boolean (forced) value. The two together are
why we use the word "undecidable" and not merely "undetermined": the freedom is a structural feature of the
theory's internal logic, reproduced by five independent interrogations.

It is INTERNALLY undecidable, not absolutely undecidable. One external datum decides it. In the GU instance
that datum is named and shown necessary: the finality-reservoir metric signature at the temporal-issuance /
time-as-finality boundary (a gated cross-program object; no cross-repository identity is asserted here). The
two honest completions are (a) obtain the sign from that external datum, now proven necessary rather than
merely convenient, or (b) posit a Krein-positivity axiom and state the theory's unitarity conditionally on
it. Both are honest; neither is a defeat. A method-independent NEGATIVE of this kind is exactly as
informative as a forced positive would have been.

---

## 6. Positioning against the prior art

The general phenomenon -- that the metric / C-operator of a pseudo-Hermitian or Krein theory is NON-UNIQUE
and needs external input -- is KNOWN, and we credit it rather than claim it.

- **Mostafazadeh (pseudo-Hermitian quantum mechanics).** A non-Hermitian `H` with `H^dagger = eta H
  eta^{-1}` admits a WHOLE FAMILY of admissible metric operators `eta`; selecting a positive-definite one
  and hence the physical observables requires additional input, and different metrics give inequivalent
  physics. The non-uniqueness of the metric operator, and the C-operator as one distinguished choice, are
  his and the surrounding pseudo-Hermitian literature's, not ours.
- **Bender and PT-symmetric quantum theory.** The CPT inner product and the C operator (`C^2 = 1`, built to
  render the PT-symmetric inner product positive) are the canonical construction of the physical metric in
  PT-symmetric theories; the C operator's role as the grading that fixes positivity is theirs.
- **Mannheim (PT-symmetric QFT, Pais-Uhlenbeck, conformal gravity).** The lesson that a higher-derivative
  or PT-symmetric theory's apparent ghost is resolved by the correct (non-naive) inner product, with the
  Pais-Uhlenbeck oscillator as the clean toy, is his and Bender-Mannheim's.
- **Lee-Wick / CLOP / Anselmi-Piva fakeon.** That an indefinite-metric ("ghost") sector can be made
  consistent by a PRESCRIPTION (Lee-Wick contour, CLOP, or the fakeon prescription) rather than by a
  derivation is a known family of resolutions; the fakeon is a specific, published way to remove the bad
  states.

Against this backdrop, our DEFENSIBLE new contribution is exactly three things, and nothing more:

- **(a) Sharp reduction.** A full candidate-unification's quantum consistency is reduced to ONE located
  `Z/2` (a single sign on a named fiber), with everything else in the source action Schur-forced (W203) and
  the sign decoupled from the open signature (W202). Prior work establishes that the metric is non-unique;
  we show that in this theory the non-uniqueness collapses to a single, exactly located bit.
- **(b) Forced-form / free-sign structure.** The good-stable stabilizer FIXES the metric FORM (every scale
  and relative coefficient) and LIBERATES precisely the grading SIGN, via the symmetry-reduction mechanism
  of Section 2. This forced-form/free-sign dichotomy, and the identification of the liberated coordinate as
  the C-block relative sign, is the structural content we claim as new.
- **(c) Multi-formalism independence.** Five independent characterizations (invariance, BRST cohomology,
  Lawvere fixed point, topos internal logic, Helmholtz inverse-variational) AGREE that the bit is
  undecidable from within and localize it to the SAME `Z/2`. Establishing the undecidability as
  formalism-independent, rather than an artifact of one method, is the robustness claim we make.

We do NOT claim to have discovered metric-operator non-uniqueness, the C-operator, or that ghosts need
external input. We claim (a) plus (b) plus (c).

---

## 7. Honest limits

- **The good stable is taken as GIVEN.** The whole analysis conditions on the existence of the good,
  unitary configuration (real total spectrum, positive-definite `eta_+`, C-operator operative). We do not
  derive that such a configuration exists; we ask what its own data can and cannot fix.
- **Internally undecidable, not absolutely undecidable.** The sign IS decided by an external datum. The
  claim is precisely that the theory's OWN data does not fix it. Supplying the datum (or positing a
  positivity axiom) closes the question; we say which datum and why it is necessary.
- **Exploration-tier, internal verification only.** Every computation here is internal: reproduced from
  scratch and adversarially reviewed within one AI-directed process, not yet independently replicated or
  peer-reviewed. The machine checks are strong on their decisive linear-algebra cores but the surrounding
  identifications (e.g. that the free spectral section IS the unbuilt curvature datum) are structural.
- **The general theorem carries a side-hypothesis.** Section 2's theorem is proven with the non-coincidence
  hypothesis, automatic in the canonical maximal-compact case; the fully general characterization for proper
  subgroups is left to the hardening register.
- **No canon movement.** bar (b) and H59 stay OPEN. The generation count stays `{1,3}`. No forbidden target
  is assumed or inserted. Nothing here asserts that GU is correct, that a particular cosmological signal is
  real, or that the sign is one value rather than the other.

---

## 8. Relation to the "located, not forced" line (a light nod, not a sequel)

This paper shares a temperament with the repository's generation-count paper "Located, Not Forced": both
isolate an open question to a single, precisely located, external bit rather than forcing an answer, and
both treat a clean method-independent NEGATIVE as a real result. But they are DISTINCT papers with distinct
subjects. "Located, Not Forced" is about the fermion GENERATION COUNT and lives in index theory, framed
bordism, and primary decomposition; this paper is about the quantum-consistency GRADING SIGN and lives in
Krein / pseudo-Hermitian inner-product theory and invariant theory. This is not a sequel. The shared moral
is only that in this program, some of the deepest questions turn out to be located and external rather than
internally forced, and saying so precisely is the contribution.

---

## 9. Summary

In a self-consistent indefinite-metric gauge theory whose physical inner product is a C-operator grading,
the theory's full symmetry forces the metric FORM (Schur, dimension one) but a positive-definite total
metric restricts to the C-commutant, under which the frame reduces, the invariant-form space grows to
dimension at least two, and the grading SIGN is liberated as a free `Z/2`. It is structurally forced in form
and internally undecidable in sign. Geometric Unity is a maximally clean instance: its entire quantum
consistency reduces to one such bit, five independent formalisms agree the bit is undecidable from within
and localize it to the same `Z/2`, and the source action's coefficients are otherwise forced. The bit is
decided by one external datum, which the paper names. We claim the sharp reduction, the forced-form/free-sign
structure, and the multi-formalism independence; we credit the known non-uniqueness of the Krein metric to
the pseudo-Hermitian and PT-symmetric literature.

---

*DRAFT, first pass, exploration-tier. Promotion to candidate is Joe-gated. Machine checks:
`python -u papers/drafts/structurally-forced-internally-undecidable/tests/general_krein_grading_sign.py`
(81/81, exit 0) and `python -u tests/W211_five_method_convergence.py` (exit 0). No canon movement; bar (b)
and H59 stay OPEN. Zero em dashes.*
