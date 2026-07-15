---
title: "Hardening report: Structurally Forced, Internally Undecidable"
status: draft
doc_type: adversarial_hardening_report
created: 2026-07-14
target_commit_floor: 52faf48
governance: "Draft-tier only. No promotion or external action. bar (b) and H59 remain OPEN."
---

# Hardening report

## Executive verdict

The adversarial review found a fatal error in the paper's headline theorem. The simultaneous stabilizer `O(p) x O(q)` does not leave a free grading `Z/2`. It has exactly one admissible commuting fundamental symmetry. When a proper compact subgroup allows the same irreducible type on both the positive and negative sides, the residual family is normally continuous, with an exactly computable positive dimension. The old theorem therefore fails both ways: its canonical example is unique, and its failure cases are not one bit.

The GU application is inside the gap and does not rescue the claim. The constructed `SO(9) x SO(5)` surrogate satisfies the uniqueness condition. The native interacting good-stable stabilizer, physical observable algebra, and grading operator are not derived. The proposed five-method convergence is not independent, and no formal undecidability theorem is present.

The draft has been rewritten to make those negative results central. A corrected finite-dimensional compact-stabilizer theorem, written proof, counterexamples, literature review, and regression test now survive. The paper is still not candidate-ready.

## Claim-by-claim disposition

| claim | adversarial result | present grade | required next evidence |
|---|---|---|---|
| Full `O(p,q)` invariance forces the standard symmetric form up to scale | Survives on the standard representation | Referee-grade finite-dimensional statement | None for the stated representation; do not generalize from irreducibility alone |
| Real irreducibility implies one invariant symmetric form | False | Withdrawn | State `dim Sym^2(V*)^G = 1` explicitly or prove it from stronger representation hypotheses |
| The good-stable stabilizer is the compact `C`-commutant | Conditional | Referee-grade linear algebra once `C` and a positive majorant are given | Derive the physically relevant GU `C` and stabilizer rather than assume them |
| `O(p) x O(q)` leaves one free grading sign | False | Killed | It leaves one admissible fundamental symmetry, `diag(I_p,-I_q)` |
| A two-dimensional invariant-form space is a free `Z/2` | False category identification | Killed | The positive invariant metrics form a continuous cone; most do not define involutions |
| Positivity permits `c_+,c_->0` in `B=c_+ eta_+block + c_- eta_-block` | Literal sign error | Corrected | Positivity requires `c_+>0` and `c_-<0` in that convention |
| Non-coincidence gives exactly one scale per sign block | False | Corrected | Non-coincidence only kills cross terms; diagonal multiplicities can add invariant scales |
| The general theorem extends unchanged to proper subgroups | False | Replaced | Use the isotypic classification and residual-dimension formula |
| Failure of non-coincidence leaves a residual `Z/2` | False | Replaced | Shared constituents give homogeneous factors of dimension `dim_R(D)ab` |
| GU's worked `SO(9) x SO(5)` example realizes the free bit | False under its own assumptions | Killed | The two standard constituents are inequivalent, so the admissible `C` is unique |
| The actual GU good-stable stabilizer satisfies the theorem's hypotheses | Unknown | Open | Derive it from the native `Sp(32,32;H)`-level dynamics and physical state space |
| W203 forces the source action except for overall scale | Overstated | Downgraded | W203 forces an ultralocal bridge kernel up to scale, conditional on W154; build the nonlocal completion |
| W202 decouples all relevant grading uncertainty from the signature branch | Too broad for the physical conclusion | Downgraded | A finite-dimensional fiber sign comparison does not build the interacting metric operator |
| BRST independently proves non-selection | Not constructed | Withdrawn as proof | Build `Q`, compute `H^0(Q)`, descend the pairing, and identify the physical observable commutant |
| Lawvere proves two internal fixed points | Formal hypotheses absent; bad branch violates positivity | Analogy only | Supply a category, weak point-surjectivity, endomorphism, and physically admissible models |
| Topos logic proves the GU sign is not complemented | Truth value assigned on a chosen toy site | Analogy only | Derive the site or classifying topos and the sign subobject from a formal GU theory |
| Helmholtz analysis independently selects or fails to select the sign | Only a conditional self-adjointness lemma survives | Lemma-grade | Apply it to the actual constrained linearized GU Euler-Lagrange operator and boundary problem |
| Five methods independently localize the same `Z/2` and owner | False | Withdrawn | The notes use incompatible `C` choices and reduce to one block calculation plus analogies |
| The sign is Godel-independent or internally undecidable | Not established | Withdrawn | State a formal theory and target sentence, then prove genuine model separation or syntactic independence |
| An external datum can decide a metric choice | True in principle | Contextual, not a GU theorem | Specify a selection rule and prove compatibility with the complete physical theory |
| A particular finality or temporal-issuance object is necessary and sufficient | Not established | Gated and unasserted | Requires explicit Joe-authorized cross-surface work and a mathematical identification |
| bar (b) or H59 is cleared | False | Remains OPEN | Complete the native interacting Krein-unitarity program |

## Corrected mathematical result

For a finite-dimensional real Krein space `(V,eta)` and `H <= O(eta)`, define

```
F_H(eta) = {C in End_H(V) : C^2=1,
            C is eta-self-adjoint,
            eta(.,C.) is positive definite}.
```

The report establishes:

1. `F_H(eta)` is nonempty exactly when the image of `H` has compact closure.
2. For compact closure `K`, write the real isotypic decomposition as

   ```
   V = direct_sum_lambda U_lambda tensor_{D_lambda} M_lambda,
   D_lambda in {R,C,H},
   ```

   and let the induced `D_lambda`-Hermitian multiplicity form have signature `(a_lambda,b_lambda)`.
3. Then

   ```
   F_H(eta) is isomorphic to
   product_lambda U_{D_lambda}(a_lambda,b_lambda)
     / (U_{D_lambda}(a_lambda) x U_{D_lambda}(b_lambda)),
   ```

   with real dimension

   ```
   sum_lambda dim_R(D_lambda) a_lambda b_lambda.
   ```

4. The admissible fundamental symmetry is unique exactly when no irreducible type occurs with both signs.
5. The invariant symmetric-form dimension is

   ```
   sum_lambda d_{D_lambda}(a_lambda+b_lambda),
   ```

   where `d_R(m)=m(m+1)/2`, `d_C(m)=m^2`, and `d_H(m)=m(2m-1)`.

This closes the finite-dimensional version of the general-theorem gap by replacing, not proving, the original claim.

## The seven requested hardening items

### 1. General-theorem gap

**Closed in finite dimensions. Original claim killed.**

The exact failure condition and residual dimension are now given. The canonical `O(p) x O(q)` case is unique. The diagonal `O(r) <= O(r,r)` example supplies a continuous family. A separate proper-subgroup example shows that non-coincidence can coexist with three invariant symmetric-form parameters, so no-common-constituent does not imply the draft's two-scale conclusion.

**Cannot be closed here:** the infinite-dimensional version, unbounded-operator domains, and the actual GU state-space representation require outside functional-analysis and Krein expertise plus a built GU operator.

### 2. Prior art and novelty

**Completed as a serious internal sweep, with major downgrades.**

The review covered Mostafazadeh's pseudo-Hermitian and metric-operator work; Bender, Boettcher, Brody, Jones, Klevansky, Kuzhel, and Mannheim on PT symmetry and `C`; Pais-Uhlenbeck and conformal-gravity claims; Lee-Wick and CLOP; Anselmi and Piva; Gupta, Nakanishi, Kugo and Ojima, Jakobczyk and Strocchi, Batalin and Marnelius, and Finster and Strohmaier; and Lawvere and Yanofsky for the logical framing.

Findings:

- general metric and `C` nonuniqueness is prior art;
- selection by additional observables is prior art;
- indefinite-sector physical prescriptions and physical-state reconstruction are prior art;
- a broad claim that the metric must be fixed by external input is contradicted by published programs that claim internal determination from the correctly formulated dynamics;
- the old forced-form/free-sign theorem is false;
- multi-formalism novelty is not established; and
- the corrected compact classification is probably standard and is not claimed as novel.

All references retained in the manuscript have an arXiv, DOI, or publisher record. A misidentified Batalin-Marnelius title was caught and corrected during verification.

**Cannot be closed here:** a defensible novelty opinion requires independent specialists with coverage of Krein representation theory and PT-symmetric QFT.

### 3. Written proofs and independence

**Completed honestly.**

The invariant-theory theorem and Helmholtz lemma now have written proofs. The other routes are explained at the level necessary to show why they are incomplete. Fabricating full proofs would have hidden missing mathematical objects.

The independence claim fails. There is one invariant theorem, a conditional operator lemma using the same block commutation, an unbuilt BRST application, and two analogies.

### 4. Red-team of remaining claims

**Completed.**

The audit exposed circular use of `C=sign(eta)`, a positivity sign error, misuse of real Schur reasoning, incompatible `C` definitions across notes, the W154 dependency, the ultralocal limit of W203, the absence of a formal theory for undecidability, and an unsupported external-owner identification.

The manuscript now explicitly says that an external datum can decide a choice and that other internal dynamics or observables may also decide it. No absolute undecidability language remains as a claimed result.

### 5. Standard hardening and venue

**Provisional editorial resolution; scientific blocker remains.**

The corrected finite-dimensional result is presented first, with GU as an incomplete application. The likely eventual framing is a math-ph or hep-th note only if the physical GU stabilizer and interacting application are derived. The general theorem alone is likely background rather than a publishable novelty claim.

### 6. Source-action completion context

**Clarified.**

The word "forced" is limited to the ultralocal W203 bridge kernel on the 14-dimensional current-index representation, conditional on W154. No full nonlinear, gradient, or nonlocal source action is claimed.

### 7. Domain-referee clarity

**Substantially improved but not externally validated.**

Definitions, hypotheses, proofs, counterexamples, dependency boundaries, method grades, and bibliography are now explicit. The paper clearly separates a positive-majorant proxy from GU's native keep-and-grade H59 criterion.

**Cannot be closed here:** independent human review remains necessary.

## Machine verification

Command:

```
python -u papers/drafts/structurally-forced-internally-undecidable/tests/general_krein_grading_sign.py
```

Result on 2026-07-14:

```
77/77 checks passed
exit code 0
```

The checks cover the canonical uniqueness result, invariant metric cones, proper-subgroup diagonal multiplicities, shared-constituent continuous families, a real-Schur counterexample, and the division-algebra dimension formulas. They are regression checks, not a substitute for the written proof.

## What survived at referee grade

- Proposition 1: existence of an invariant positive majorant exactly for relatively compact image.
- Theorem 2: finite-dimensional compact-isotypic classification of commuting fundamental symmetries and its residual-dimension formula.
- Corollary 3: uniqueness for the canonical `O(p) x O(q)` stabilizer.
- Lemma 4: the conditional Helmholtz self-adjointness calculation.
- The narrow W203 statement, as reported by its own computation: one-dimensional ultralocal equivariant kernel, conditional on W154.
- The conclusion that the specified invariant metric space and the space of admissible grading involutions are different mathematical objects.

## What cannot be closed inside the GU repository as it stands

- independent novelty validation by Krein, PT-symmetric-QFT, and representation-theory experts;
- a derived physical GU good-stable stabilizer and observable algebra;
- an interacting, renormalized GU grading or metric operator;
- the full H59 unitarity and ghost-clearance program;
- a nonlocal source-action completion independent of the W154 bridge assumption;
- a genuine BRST cohomology calculation without the missing `Q` and state complex; and
- any cross-repository identification of an external owner without Joe's explicit gate and the missing mathematics.

## Candidate-readiness bottom line

This is not close to candidate-ready as the paper originally conceived it. The finite-dimensional correction is readable and tested, but it reverses the headline conclusion. A candidate paper would need a new thesis centered on a derived physical application, not editorial polishing of the old one.

The single biggest remaining risk is the absence of the actual GU good-stable representation and interacting observable algebra. Without them, neither uniqueness, nonuniqueness, nor the dimension of the physical metric freedom can be inferred from the 14-frame surrogate.

## Governance receipt

- Draft tier retained.
- No promotion performed.
- No external action performed.
- No cross-repository identity asserted.
- bar (b) remains OPEN.
- H59 remains OPEN.
