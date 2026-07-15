---
title: "Invariant metrics and fundamental symmetries for compact stabilizers: an adversarial correction of the proposed GU grading-sign argument"
status: draft
grade: "DRAFT-tier only. The original one-Z/2 and internal-undecidability thesis does not survive adversarial review. Promotion is Joe-gated. bar (b) and H59 remain OPEN."
created: 2026-07-14
updated: 2026-07-14
slug: structurally-forced-internally-undecidable
lead: "A GU-independent compact-stabilizer theorem is proved; its proposed one-bit GU application is not established."
depends_on:
  - explorations/W203-branch3-source-action-fixed-coefficients-2026-07-14.md
  - explorations/W206-decisive-bit-counterfactual-invariance-2026-07-14.md
  - explorations/W207-decisive-bit-brst-cohomology-2026-07-14.md
  - explorations/W208-decisive-bit-lawvere-fixed-point-2026-07-14.md
  - explorations/W209-decisive-bit-topos-internal-logic-2026-07-14.md
  - explorations/W210-decisive-bit-helmholtz-inverse-variational-2026-07-14.md
  - explorations/W211-krein-sign-godel-independent-five-method-synthesis-2026-07-14.md
scripts:
  - papers/drafts/structurally-forced-internally-undecidable/tests/general_krein_grading_sign.py
---

# Invariant metrics and fundamental symmetries for compact stabilizers

## An adversarial correction of the proposed GU grading-sign argument

*Draft. Not a candidate. The original title claim, "Structurally Forced, Internally Undecidable," is the hypothesis tested here, not a result established by this paper.*

## Abstract

This paper asks whether invariance in a finite-dimensional Krein space forces a metric form while leaving exactly one grading sign internally undecidable. The answer is no. For the canonical stabilizer `O(p) x O(q)`, the admissible fundamental symmetry is unique, not a free `Z/2`. For proper compact subgroups, shared irreducible constituents across positive and negative sectors produce a continuous family of admissible fundamental symmetries. More generally, if a compact group acts isotypically with multiplicity-space signatures `(a_lambda,b_lambda)` over division algebras `D_lambda` in `{R,C,H}`, the space of commuting fundamental symmetries has real dimension

```
sum_lambda dim_R(D_lambda) a_lambda b_lambda.
```

It is a singleton exactly when no irreducible type occurs on both sides. This theorem precisely characterizes the failure of the draft's former side hypothesis and replaces its claimed residual `Z/2`.

The Geometric Unity application remains open. The constructed `SO(9) x SO(5)` surrogate has no shared constituents and therefore has a unique admissible fundamental symmetry. The repository does not derive that compact stabilizer, or the interacting grading operator, from the native good-stable dynamics. The built source-action result is narrower: an ultralocal `so(9,5)`-equivariant kernel is one-dimensional, conditional on the W154 current identification. It does not complete the nonlocal source action or the H59 Krein-unitarity program.

The five proposed methods do not establish formalism-independent undecidability. Invariance supplies the theorem proved here. A Helmholtz calculation supplies a conditional operator lemma. The BRST application lacks the GU differential and cohomology. The Lawvere and topos constructions are analogies, not models of a stated GU theory. Accordingly, this draft uses "underdetermined by specified invariance data" where justified and does not claim Godel, Lawvere, topos, or absolute undecidability. An external datum could select a physical metric, but this paper proves neither the identity nor the necessity of a particular external owner.

## 1. Question, conventions, and scope

Let `V` be a finite-dimensional real vector space with a nondegenerate symmetric bilinear form `eta`. A fundamental symmetry is an endomorphism `C` such that

1. `C^2 = 1`;
2. `C` is `eta`-self-adjoint, meaning `eta(Cx,y) = eta(x,Cy)`; and
3. `h_C(x,y) = eta(x,Cy)` is positive definite.

If a group `H <= O(eta)` is part of the data, an admissible `H`-commuting fundamental symmetry also satisfies `Ch = hC` for every `h in H`. Write

```
F_H(eta) = {C in End_H(V) : C^2 = 1, C is eta-self-adjoint, eta(.,C.) > 0}.
```

This definition avoids a circularity in the earlier draft. Writing `C = sign(eta)` already requires a positive majorant or an auxiliary Euclidean structure. It cannot then be used to prove that `eta` alone selected `C`.

The finite-dimensional analysis below is a standard positive-majorant proxy. It is not the native GU ghost-clearance criterion. The native H59 program keeps the Krein structure and asks for an interacting scattering operator with `[P,S] = 0`, together with renormalization, spectral, infrared, constraint, and projected-unitarity controls. No positive-Hilbert substitution is made here.

## 2. The corrected compact-stabilizer theorem

### 2.1 Existence

**Proposition 1.** Let `H <= O(eta)`. Then `F_H(eta)` is nonempty if and only if the image of `H` has compact closure in `GL(V)`.

**Proof.** Suppose `C in F_H(eta)`. The positive form `h_C = eta(.,C.)` is `H`-invariant because `H` preserves `eta` and commutes with `C`. Hence the image of `H` lies in the compact orthogonal group `O(h_C)`, so its closure is compact.

Conversely, let `K` be the compact closure of the image of `H`. Average any positive-definite form over `K` to obtain a `K`-invariant positive form `h`. There is a unique `h`-self-adjoint invertible operator `A` with

```
eta(x,y) = h(x,Ay).
```

Both forms are `K`-invariant, so `A` commutes with `K`. Functional calculus gives `C = sign(A)`. Then `C^2 = 1`, `C` commutes with `K`, and

```
eta(x,Cy) = h(x,ACy) = h(x,|A|y),
```

which is positive definite. The `eta`-self-adjointness follows from the fact that `A` and `C` are commuting `h`-self-adjoint operators. Thus `C in F_H(eta)`. QED.

This proposition already limits the scope of the proposed mechanism. A noncompact stabilizer cannot admit an invariant positive majorant in finite dimensions.

### 2.2 Classification and residual dimension

Let `K` be the compact closure of `H`. Real compact representation theory gives an isotypic decomposition

```
V = direct_sum_lambda U_lambda tensor_{D_lambda} M_lambda,
```

where `U_lambda` are pairwise nonisomorphic irreducible real `K`-modules and

```
D_lambda = End_K(U_lambda) in {R,C,H}.
```

After choosing a `K`-invariant positive form on each `U_lambda`, the restriction of `eta` to the corresponding isotypic component is encoded by a nondegenerate `D_lambda`-Hermitian form `q_lambda` on `M_lambda`. Let its signature be `(a_lambda,b_lambda)` and put `m_lambda = a_lambda + b_lambda`.

**Theorem 2.** If `F_H(eta)` is nonempty, then

```
F_H(eta) is isomorphic to
product_lambda U_{D_lambda}(a_lambda,b_lambda)
  / (U_{D_lambda}(a_lambda) x U_{D_lambda}(b_lambda)).
```

Consequently,

```
dim_R F_H(eta)
  = sum_lambda dim_R(D_lambda) a_lambda b_lambda.
```

In particular, `F_H(eta)` is a singleton if and only if `a_lambda b_lambda = 0` for every `lambda`. Equivalently, no irreducible real `K`-type occurs in both the positive and negative subspaces of one, hence every, admissible fundamental symmetry.

**Proof.** Work on one isotypic component. A `K`-commuting fundamental symmetry is the identity on `U_lambda` tensored with a `D_lambda`-linear fundamental symmetry for `q_lambda` on `M_lambda`. Such a symmetry is equivalent to a `q_lambda`-orthogonal decomposition of `M_lambda` into a positive subspace of `D_lambda`-dimension `a_lambda` and a negative subspace of dimension `b_lambda`.

The indefinite unitary group `U_{D_lambda}(a_lambda,b_lambda)` acts transitively on those decompositions. The stabilizer of a reference decomposition is the product of its compact unitary groups. This proves the homogeneous-space description. The real dimensions of the off-diagonal blocks are `dim_R(D_lambda) a_lambda b_lambda`; summing over the isotypic components proves the formula.

The homogeneous space is a point exactly when each product `a_lambda b_lambda` vanishes. This is precisely the absence of a shared irreducible type across the two signs. QED.

### 2.3 Invariant symmetric forms

The same decomposition gives the real dimension of the full space of `K`-invariant symmetric bilinear forms:

```
dim_R Sym^2(V*)^K = sum_lambda d_{D_lambda}(m_lambda),
```

where

```
d_R(m) = m(m+1)/2,
d_C(m) = m^2,
d_H(m) = m(2m-1).
```

The cross-sign block has dimension

```
sum_lambda dim_R(D_lambda) a_lambda b_lambda.
```

Thus the earlier "non-coincidence" condition does only one job: it kills cross terms. It does not by itself imply one invariant scale on each diagonal block. That additional conclusion requires one-dimensional invariant symmetric-form spaces on the relevant modules. Real irreducibility alone is insufficient. For example, the realification of the standard representation of `SO(3,C)` preserves the real and imaginary parts of its complex symmetric form, giving two linearly independent real invariant symmetric forms.

### 2.4 Canonical stabilizer

For completeness, the standard `O(p,q)` representation has

```
Sym^2(V*)^{O(p,q)} = R eta.
```

Indeed, if `B` is invariant, the operator `A = eta^{-1}B` commutes with the standard `O(p,q)` action. Reflections in the coordinate axes make `A` diagonal, ordinary rotations within each equal-sign block make it scalar on that block, and a hyperbolic rotation mixing one positive and one negative coordinate equates the two scalars. Hence `A` is scalar and `B` is proportional to `eta`. This is the valid finite-dimensional forced-form statement. It does not imply that a positive metric or a grading is also forced by the full noncompact group; Proposition 1 rules out an invariant positive majorant for the full group.

**Corollary 3.** For `V = R^p direct_sum R^q` with

```
eta = diag(I_p,-I_q)
```

and `H = O(p) x O(q)` acting in the standard way, `F_H(eta)` contains exactly

```
C_0 = diag(I_p,-I_q).
```

**Proof.** The positive and negative standard modules are inequivalent `H`-modules, so every `a_lambda b_lambda` is zero. Theorem 2 gives a singleton. Directly, every commuting involution is block scalar, `diag(epsilon_+ I_p, epsilon_- I_q)`, and positivity of `eta C` forces `(epsilon_+,epsilon_-) = (+1,-1)`. QED.

This directly contradicts the earlier claim that the canonical maximal-compact stabilizer leaves one free grading sign. The other three sign choices are involutions, but they are not admissible fundamental symmetries.

The invariant symmetric forms are

```
B = a P_+ + b P_-.
```

The positive cone is `a > 0` and `b > 0`. Its continuous ratio `b/a` is a metric deformation, not a grading sign. Except at the normalization compatible with `eta`, `eta^{-1}B` is not an involution. Conversely, writing

```
B = c_+ eta|V_+ + c_- eta|V_-
```

requires `c_+ > 0` and `c_- < 0` for positivity. The earlier draft's condition `c_+,c_- > 0` was a literal sign error.

### 2.5 Proper subgroups and exact failure of non-coincidence

Proper compact subgroups can produce either uniqueness or continuous nonuniqueness.

If the positive and negative restrictions have no common irreducible type, Theorem 2 still gives a unique admissible `C`, even if there are many invariant metric scales inside either sign sector. For example, the trivial subgroup has many invariant forms but also shares every trivial constituent across the two sides, so it lies in the nonunique case.

For an explicit shared-constituent example, let

```
H = {(R,R) : R in O(r)} <= O(r,r)
```

act diagonally on `R^r direct_sum R^r`. The standard `O(r)` type occurs once on each sign. In the standard-type multiplicity space the relevant signature is `(1,1)` over `R`, so Theorem 2 gives a one-dimensional homogeneous factor. A concrete family is

```
C_t = [[cosh(2t), -sinh(2t)],
       [sinh(2t), -cosh(2t)]] tensor I_r.
```

Every `C_t` commutes with `H`, squares to one, is `eta`-self-adjoint, and makes `eta C_t` positive definite. The ambiguity is a continuum, not `Z/2`.

The preceding paragraph distinguishes the real dimension of the multiplicity-space homogeneous factor, which is one here, from the dimension of an arbitrary off-diagonal `r x r` matrix before imposing `O(r)` equivariance. The machine check uses the equivariant dimension and verifies the displayed family for `r = 1,2,3`.

## 3. What the GU repository actually establishes

### 3.1 The W203 source-action result

W203 computes the commutant of the `so(9,5)` action on the 14-dimensional current-index representation. In the tested ultralocal ansatz, an equivariant symmetric kernel is one-dimensional and proportional to `eta`. This is a real result about that representation.

Its scope has two material restrictions:

1. The identification `J_IG = J[Psi]` is inherited from the reverse-engineered W154 current. W203 states this dependency rather than deriving it independently.
2. The computation covers an ultralocal auxiliary-field kernel. The gradient or nonlocal `Z_U` completion is not built.

The referee-grade statement is therefore:

> Conditional on the W154 current identification, the ultralocal bridge kernel is forced up to scale on the `so(9,5)` frame representation. The full nonlocal source action is not built.

It does not follow that every source-action coefficient is forced or that GU quantum consistency has been reduced to one bit.

### 3.2 The constructed compact surrogate

W206 assumes a good stable with an operative `C` and positive `eta C`, then studies the selected-frame stabilizer `SO(9) x SO(5)`. On the 14-dimensional standard split, the two modules are inequivalent. Corollary 3 applies and yields a unique admissible fundamental symmetry. Thus the paper's own canonical worked surrogate does not exhibit the alleged free `Z/2`.

This is a conditional consistency check, not a derivation of GU's actual good-stable stabilizer. The repository records the program-native group as `Sp(32,32;H)`, while the W203 calculation concerns a 14-frame `so(9,5)` current-index kernel. No argument in the cited notes derives the interacting compact stabilizer, its isotypic multiplicities, or the physical `C`-operator from the native dynamics.

There is also no single consistent `C` across the five exploratory notes. W206 and W208 flip all five negative directions and obtain `eta C = I`. W210 flips only four record directions, leaving the base time direction negative. W209 sets `C = I` in its toy semantics. These choices have different stabilizers and different invariant-form dimensions. They cannot support a claim that five methods found the same physical bit.

### 3.3 Native Krein unitarity remains open

The native H59 standard does not replace the indefinite theory with a positive Hilbert proxy. It requires, among other things:

- a renormalized interacting relation `[P,S] = 0`;
- counterterm closure compatible with the grading;
- a consistent rule for odd ghost loops;
- appropriate Jordan and Krein diagonalizability controls;
- infrared-inclusive or resummed observables;
- Rarita-Schwinger constraint closure;
- a projected optical theorem and spectral-density statement; and
- projected Born-level positivity.

Those objects are not supplied by the finite-dimensional theorem. bar (b) and H59 therefore remain OPEN.

## 4. Written audit of the five proposed methods

### 4.1 Invariant theory

This is the one complete mathematical route. Proposition 1 and Theorem 2 give its referee-readable proof. Its conclusion is not the old one: the specified compact stabilizer gives either a unique admissible fundamental symmetry or a positive-dimensional homogeneous space. It does not naturally give a residual `Z/2`.

### 4.2 BRST cohomology

A BRST argument would require a nilpotent GU charge `Q`, a defined state complex, a computed physical cohomology `H^0(Q)`, and a descended nondegenerate pairing. To prove metric uniqueness or nonuniqueness on cohomology, one would then compute the commutant of the physical observable algebra on `H^0(Q)` and classify positive pairings there.

W207 does not construct those objects. It repeats the finite-dimensional Schur calculation and labels the resulting vector space as physical cohomology. The following conditional implication is valid:

> If a GU BRST complex is constructed, if its degree-zero cohomology carries the assumed two-block representation, and if the pairing descends nondegenerately, then Theorem 2 applies to the induced compact action.

That is not an independent proof and does not close the GU case.

### 4.3 Lawvere fixed point

Lawvere's diagonal theorem requires a category with suitable products, a weakly point-surjective map, and a stated endomorphism to which the fixed-point conclusion applies. To obtain an independence theorem, one would additionally need a formal theory and two models satisfying the same axioms with opposite truth values for one sentence.

W208 enumerates commuting involutions in a finite-dimensional toy model and calls them fixed points. It does not define the required category or weak point-surjectivity, and its pathological branch violates the positivity premise imposed on a fundamental symmetry. It is therefore an analogy, not a Lawvere proof and not a model-theoretic independence result.

### 4.4 Topos internal logic

A topos proof would have to derive a site or classifying topos from the GU theory, represent the physical-sign statement as a subobject, and show that the proposition is not complemented in every relevant model. W209 instead chooses a three-open observer site and assigns the desired sign proposition to the intermediate open. The resulting Heyting value follows from that assignment. It does not follow from GU, and the note's `C = I` conflicts with the grading used elsewhere. This construction is a useful illustration of intuitionistic truth values, not evidence for GU undecidability.

### 4.5 Helmholtz inverse problem

One valid operator lemma survives.

**Lemma 4.** Let `g` be a nondegenerate symmetric matrix, let `L` satisfy `gL = L^T g`, let `C` satisfy `C^T g = gC`, and suppose `[C,L] = 0`. Then `(gC)L` is symmetric.

**Proof.** Using the hypotheses,

```
((gC)L)^T = L^T C^T g = L^T g C = g L C = g C L.
```

QED.

The lemma says that a commuting, `g`-self-adjoint grading preserves formal self-adjointness. It does not select a grading. W210 tests block-diagonal sample operators rather than the linearized GU Euler-Lagrange operator with its constraints and boundary conditions. This is a conditional operator lemma, not an independent proof of a physical sign.

### 4.6 Independence verdict

The five methods reduce to the following honest inventory:

| route | present grade | relationship to the core |
|---|---|---|
| invariant theory | proved | the actual theorem |
| Helmholtz | conditional lemma | reuses the same block commutation |
| BRST | unbuilt conditional route | would apply the same commutant calculation on cohomology |
| Lawvere | analogy | no categorical hypotheses or formal models supplied |
| topos | analogy | truth value assigned on a chosen toy site |

There are not five independent proofs. The former "multi-formalism independence" contribution is withdrawn.

## 5. What may and may not be called undecidable

The results prove statements about invariant data and commutants. They do not define a recursively axiomatized theory `T`, a target sentence `sigma`, or models of all the stated axioms with `sigma` and `not sigma`. No Godel incompleteness theorem applies. Nor do the Lawvere and topos toys supply such a replacement.

The strongest justified phrase is:

> The choice of positive metric is underdetermined by the specified invariance data when Theorem 2 has positive residual dimension.

Even that statement is conditional on having identified the physically relevant group action and observable algebra. Additional internal dynamics or observables can reduce or eliminate the metric freedom. This is well known in quasi-Hermitian theory, where a complete family of observables may fix the metric.

An external prescription or empirical datum can also select a metric. Nothing here establishes that external input is always necessary. In particular, Bender and Mannheim's Pais-Uhlenbeck analysis and Anselmi and Piva's Lee-Wick formulation explicitly present their physical structures as determined by a correctly formulated theory rather than by an arbitrary external bit. Those claims must be assessed on their own assumptions, but they refute any blanket assertion that indefinite-metric theories require an external owner.

For GU, a proposed finality or temporal-issuance datum may be investigated as an external selector. This draft asserts no cross-repository identity, no ownership relation, and no necessity or sufficiency theorem for that datum.

## 6. Prior art and novelty verdict

Metric-operator and `C`-operator nonuniqueness is established prior art. Scholtz, Geyer, and Hahne showed that additional observables can constrain a quasi-Hermitian metric. Mostafazadeh developed pseudo-Hermiticity, positive metric operators, their symmetries, and their nonuniqueness. Bender and collaborators constructed the `C` operator in PT-symmetric quantum mechanics and later studied its nonuniqueness and unbounded versions. Krein-space, Gupta-Bleuler, and BRST literature treats physical-state selection and the induced physical inner product. Lee-Wick, CLOP, and later nonanalytic or fakeon prescriptions address indefinite or higher-derivative sectors through particular dynamical and analytic constructions.

The novelty claims survive as follows:

1. **One located `Z/2`: not established.** The canonical surrogate has a unique admissible `C`; shared constituents give a continuum. The native GU stabilizer is unbuilt.
2. **Forced form, free sign: anticipated in broad form and false in the proposed theorem.** Symmetries and a chosen observable algebra constraining, but not necessarily uniquely fixing, a metric are established prior art. The claimed `Z/2` specialization does not survive.
3. **Five-method independence: not established.** Only one theorem and one conditional lemma survive.
4. **Correct compact-stabilizer classification: mathematically valid but likely standard.** It is a useful corrective formulation, not presently supported as a novel theorem by the literature review.
5. **GU application: potentially specific, but presently incomplete.** Novelty cannot substitute for the missing stabilizer and interacting construction.

The best eventual venue posture would be a math-ph or hep-th note centered on a genuinely derived GU application, with the compact-representation theorem presented as background. A general-theorem paper would require an outside Krein and real-representation-theory expert to confirm both novelty and the precise infinite-dimensional extension. The current manuscript is not ready for either venue.

## 7. Source-action completion and dependency boundary

The word "forced" must remain attached to the object actually computed. W203 establishes a one-dimensional ultralocal kernel commutant on the 14-dimensional frame representation. The statement depends on the W154 current identification and does not build the full source action.

No inference in this draft upgrades that schema match into:

- a derived nonlinear or nonlocal source action;
- a renormalized interacting `C`-operator;
- uniqueness of the physical inner product;
- quantum unitarity; or
- a one-bit completion theorem.

These boundaries are mathematical, not editorial qualifications.

## 8. Machine-checkable regression tests

The draft-local script

```
python -u papers/drafts/structurally-forced-internally-undecidable/tests/general_krein_grading_sign.py
```

checks 77 deterministic assertions, including:

- full `so(p,q)` invariant-form dimensions for representative signatures;
- compact-stabilizer invariant-form dimensions;
- uniqueness of the canonical admissible fundamental symmetry;
- separation of the positive metric cone from involutive gradings;
- a proper-subgroup example where non-coincidence does not imply one diagonal scale;
- the diagonal `O(r)` shared-constituent family `C_t` for `r = 1,2,3`;
- two independent invariant real forms on the realified `SO(3,C)` example; and
- the `R`, `C`, and `H` invariant-form dimension formulas.

The test is a finite-dimensional regression certificate, not a proof of the representation-theoretic classification and not a test of GU dynamics.

## 9. Honest limits and readiness

- The classification is finite dimensional. Unbounded operators, domains, completion, spectral singularities, and infinite-dimensional Krein-space topology are outside its proof.
- Compactness and complete reducibility are essential. The physical GU stabilizer has not been derived.
- The application uses a standard positive-majorant proxy. H59's native keep-and-grade scattering problem is not solved.
- W203 is conditional on W154 and ultralocal.
- The literature sweep verifies that the cited papers exist, but it is not a substitute for specialist novelty review across all Krein and indefinite-metric representation theory.
- No external datum is identified as GU's owner. No cross-repository identity is asserted.
- No canon or verdict changes follow. bar (b) and H59 remain OPEN.
- This remains a draft. It has not been promoted, submitted, posted, or externally reviewed.

The paper is not candidate-ready. The corrected general theorem is close to referee-readable in finite dimensions, but the proposed headline result and GU application do not survive. The single biggest remaining risk is that the physical GU stabilizer and interacting observable algebra, once actually derived, may bear no relevant relation to the compact 14-frame surrogate analyzed here.

## References

All entries below were checked against a publisher page, DOI record, or arXiv record. Descriptions in the text are limited to what the cited work supports.

1. F. G. Scholtz, H. B. Geyer, and F. J. W. Hahne, "Quasi-Hermitian operators in quantum mechanics and the variational principle," *Annals of Physics* 213 (1992) 74-101. [DOI 10.1016/0003-4916(92)90284-S](https://doi.org/10.1016/0003-4916(92)90284-S).
2. A. Mostafazadeh, "Pseudo-Hermiticity versus PT symmetry: The necessary condition for the reality of the spectrum of a non-Hermitian Hamiltonian," *Journal of Mathematical Physics* 43 (2002) 205-214. [arXiv:math-ph/0107001](https://arxiv.org/abs/math-ph/0107001). [DOI 10.1063/1.1418246](https://doi.org/10.1063/1.1418246).
3. A. Mostafazadeh, "Pseudo-Hermiticity and generalized PT- and CPT-symmetries," *Journal of Mathematical Physics* 44 (2003) 974-989. [arXiv:math-ph/0209018](https://arxiv.org/abs/math-ph/0209018). [DOI 10.1063/1.1539304](https://doi.org/10.1063/1.1539304).
4. A. Mostafazadeh, "Pseudo-Hermiticity, PT-symmetry, and the metric operator," [arXiv:quant-ph/0508214](https://arxiv.org/abs/quant-ph/0508214).
5. A. Mostafazadeh, "Metric operators for quasi-Hermitian Hamiltonians and symmetries of equivalent Hermitian Hamiltonians," *Journal of Physics A* 41 (2008) 244017. [arXiv:0707.3075](https://arxiv.org/abs/0707.3075). [DOI 10.1088/1751-8113/41/24/244017](https://doi.org/10.1088/1751-8113/41/24/244017).
6. A. Mostafazadeh, "Time-dependent pseudo-Hermitian Hamiltonians defining a unitary quantum system and uniqueness of the metric operator," *Physics Letters B* 650 (2007) 208-212. [arXiv:0706.1872](https://arxiv.org/abs/0706.1872). [DOI 10.1016/j.physletb.2007.04.064](https://doi.org/10.1016/j.physletb.2007.04.064).
7. C. M. Bender and S. Boettcher, "Real spectra in non-Hermitian Hamiltonians having PT symmetry," *Physical Review Letters* 80 (1998) 5243-5246. [arXiv:physics/9712001](https://arxiv.org/abs/physics/9712001). [DOI 10.1103/PhysRevLett.80.5243](https://doi.org/10.1103/PhysRevLett.80.5243).
8. C. M. Bender, D. C. Brody, and H. F. Jones, "Complex extension of quantum mechanics," *Physical Review Letters* 89 (2002) 270401. [arXiv:quant-ph/0208076](https://arxiv.org/abs/quant-ph/0208076). [DOI 10.1103/PhysRevLett.89.270401](https://doi.org/10.1103/PhysRevLett.89.270401).
9. C. M. Bender, P. N. Meisinger, and Q. Wang, "Calculation of the hidden symmetry operator in PT-symmetric quantum mechanics." [arXiv:quant-ph/0211166](https://arxiv.org/abs/quant-ph/0211166). [DOI 10.1088/0305-4470/36/7/312](https://doi.org/10.1088/0305-4470/36/7/312).
10. C. M. Bender and S. P. Klevansky, "Nonunique C operator in PT quantum mechanics," [arXiv:0905.4673](https://arxiv.org/abs/0905.4673).
11. C. M. Bender and S. Kuzhel, "Unbounded C-symmetries and their nonuniqueness," *Journal of Physics A* 45 (2012) 444005. [arXiv:1207.1176](https://arxiv.org/abs/1207.1176). [DOI 10.1088/1751-8113/45/44/444005](https://doi.org/10.1088/1751-8113/45/44/444005).
12. C. M. Bender and P. D. Mannheim, "No-ghost theorem for the fourth-order derivative Pais-Uhlenbeck oscillator model," *Physical Review Letters* 100 (2008) 110402. [arXiv:0706.0207](https://arxiv.org/abs/0706.0207). [DOI 10.1103/PhysRevLett.100.110402](https://doi.org/10.1103/PhysRevLett.100.110402).
13. P. D. Mannheim, "Making the case for conformal gravity," *Fortschritte der Physik* 61 (2013) 140-177. [arXiv:1205.5717](https://arxiv.org/abs/1205.5717). [DOI 10.1002/prop.201200100](https://doi.org/10.1002/prop.201200100).
14. T. D. Lee and G. C. Wick, "Negative metric and the unitarity of the S matrix," *Nuclear Physics B* 9 (1969) 209-243. [DOI 10.1016/0550-3213(69)90098-4](https://doi.org/10.1016/0550-3213(69)90098-4).
15. R. E. Cutkosky, P. V. Landshoff, D. I. Olive, and J. C. Polkinghorne, "A non-analytic S matrix," *Nuclear Physics B* 12 (1969) 281-300. [DOI 10.1016/0550-3213(69)90169-2](https://doi.org/10.1016/0550-3213(69)90169-2).
16. D. Anselmi and M. Piva, "A new formulation of Lee-Wick quantum field theory," *Journal of High Energy Physics* 06 (2017) 066. [arXiv:1703.04584](https://arxiv.org/abs/1703.04584).
17. D. Anselmi and M. Piva, "Perturbative unitarity of Lee-Wick quantum field theory," [arXiv:1703.05563](https://arxiv.org/abs/1703.05563).
18. D. Anselmi, "Fakeons and Lee-Wick models," *Journal of High Energy Physics* 02 (2018) 141. [arXiv:1801.00915](https://arxiv.org/abs/1801.00915). [DOI 10.1007/JHEP02(2018)141](https://doi.org/10.1007/JHEP02(2018)141).
19. S. N. Gupta, "Theory of longitudinal photons in quantum electrodynamics," *Proceedings of the Physical Society A* 63 (1950) 681-691. [DOI 10.1088/0370-1298/63/7/301](https://doi.org/10.1088/0370-1298/63/7/301).
20. N. Nakanishi, "Indefinite-metric quantum field theory," *Progress of Theoretical Physics Supplement* 51 (1972) 1-95. [DOI 10.1143/PTPS.51.1](https://doi.org/10.1143/PTPS.51.1).
21. T. Kugo and I. Ojima, "Local covariant operator formalism of non-Abelian gauge theories and quark confinement problem," *Progress of Theoretical Physics Supplement* 66 (1979) 1-130. [DOI 10.1143/PTPS.66.1](https://doi.org/10.1143/PTPS.66.1).
22. L. Jakobczyk and F. Strocchi, "Krein structures for the states of quantum gauge theories," *Journal of Mathematical Physics* 29 (1988) 1231-1235. [DOI 10.1063/1.527965](https://doi.org/10.1063/1.527965).
23. I. A. Batalin and R. Marnelius, "Solving general gauge theories on inner product spaces," *Nuclear Physics B* 442 (1995) 669-696. [arXiv:hep-th/9501004](https://arxiv.org/abs/hep-th/9501004).
24. F. Finster and A. Strohmaier, "Gupta-Bleuler quantization of the Maxwell field in globally hyperbolic space-times," *Annales Henri Poincare* 16 (2015) 1837-1868. [arXiv:1307.1632](https://arxiv.org/abs/1307.1632).
25. F. W. Lawvere, "Diagonal arguments and cartesian closed categories," in *Category Theory, Homology Theory and their Applications II*, Lecture Notes in Mathematics 92 (1969) 134-145. [DOI 10.1007/BFb0080769](https://doi.org/10.1007/BFb0080769).
26. N. S. Yanofsky, "A universal approach to self-referential paradoxes, incompleteness and fixed points," *Bulletin of Symbolic Logic* 9 (2003) 362-386. [arXiv:math/0305282](https://arxiv.org/abs/math/0305282). [DOI 10.2178/bsl/1058448677](https://doi.org/10.2178/bsl/1058448677).

## Governance note

This manuscript remains draft-tier. It makes no promotion, publication, canon, or verdict change. bar (b) and H59 remain OPEN. No external action has been taken.
