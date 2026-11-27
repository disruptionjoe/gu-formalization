---
title: Full graded Shiab derivations have zero Riemann-curvature response
status: exploration
doc_type: structural-result
created: '2026-11-27'
program_target: LB-CLASS
tier: T1
expected_delta: Decide whether a literal full degree11 graded-derivation suite can retain the nonzero Riemann response of the owned principal-Bianchi survivor.
actual_delta: Both associative and graded-Lie full-Spin derivations form the same two-channel inner family; every member annihilates algebraic Riemann spin curvature while nonzero members act nontrivially on general adjoint-valued two-forms.
class_covered: Pointwise C-infinity-linear exterior-degree11 derivations of the full complex Dirac matrix-valued exterior algebra in dimension14, equivariant under full Spin; separately derivations of its induced graded-Lie bracket. Smooth scalar coefficient functions are allowed. The exterior grading is the only grading used.
premises:
- lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md
- lab/sources/gu-shiab-derivation-principal-bianchi-source-reinspection-2026-08-05.md
- lab/sources/source-claim-register.yaml#SC-OP-02
- lab/sources/source-claim-register.yaml#SC-OP-03
- explorations/k77-wave2-principal-bianchi-product-selector-2026-08-05.md
- explorations/conditional-build/riemann-realform-transfer-2026-11-27.md
source_bridge:
  status: conditional
  reason: The source invokes derivation behavior for rolled curvature cancellation but does not define a full associative or graded-Lie Leibniz rule, its domain in all degrees, or the source total-grading convention. This tests two precise literal interpretations, not an authenticated necessary property of every Shiab realization.
kill_condition: A nonzero algebraic Riemann response cannot extend to either declared full derivation class. A counterexample satisfying the complete hypotheses invalidates the theorem; a differential, module-only, restricted-degree or symmetry-reducing construction changes the class.
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: INTERNAL-FULL-GRADED-SHIAB-DERIVATION
target_claim_verdict: Nonzero Riemann recovery excluded in the declared full derivation classes; source necessity remains conditional.
canon_verdict_change: none
matrix_or_ledger_effect: none
---

# Full graded derivations and the Shiab curvature response

```yaml
program_target: LB-CLASS
tier: T1
expected_delta: Decide whether a literal full degree11 graded-derivation suite can retain the nonzero Riemann response of the owned principal-Bianchi survivor.
actual_delta: Both associative and graded-Lie full-Spin derivations form the same two-channel inner family; every member annihilates algebraic Riemann spin curvature while nonzero members act nontrivially on general adjoint-valued two-forms.
```

## Result first

**A full Spin-equivariant degree11 algebraic derivation cannot retain a nonzero Riemann-curvature response.** This holds for both the associative matrix-valued exterior algebra and its graded-Lie bracket. Every such derivation is inner and belongs to an explicit two-channel family. The maps themselves need not vanish: they act nontrivially on general adjoint-valued curvature.

The existing principal-Bianchi survivor has nonzero Einstein response. It therefore has no extension to either full derivation class tested here. This is an extension obstruction, not another calculation of its principal-Bianchi property. It uses no action, Hessian, cubic-endpoint identity, mass term or multiplier assumption.

| State | Scope |
|---|---|
| ESTABLISHED by the written proof | Complete two-channel classification and zero Riemann response in the stated associative and graded-Lie classes. Acceptance and execution evidence are recorded separately. |
| RULED OUT | Extending a nonzero Riemann-response Shiab to either literal full derivation suite with the held grading, full carrier and symmetry. |
| NOT MODELED / UNDETERMINED | Source selection of this interpretation; differential or module-only derivations, restricted-degree chain identities, different total gradings, extra tensors, physical gravity and GU falsification. |

```gu-typed-objects
result: full graded-derivation classification and Riemann-silence extension obstruction
carrier: Lambda*(Vstar) tensor End_C(S128), full complex Dirac module in dimension14; full real u(H) only through its graded-Lie complexification LAYER=ambient CHIRALITY=S-FULL-DIRAC
pairing: none in the theorem; metric and orientation define Clifford/Hodge identifications ON=ambient_tensors
real_structure: complex proof; compatible real forms transfer the zero restriction by complexification without identifying K77 and K95
grading: exterior Z grading only; matrix coefficients have degree0; source total Bose/Fermi grading is not substituted
action_owner: repository-construction of a structural interpretation test; no action is constructed or varied
target: degree2 restriction of a full degree11 derivation on algebraic Riemann spin curvature MAP-TYPE=intertwiner
```

> **GU-COMPARATOR-ROUTING — scope before inference.** The adjoint-valued degree-raising Shiab is not the spinor-valued degree-lowering operator merely sharing its name. A derivation of the full algebra is stronger than a principal-Bianchi kernel condition or a module chain map. [Routing](../../lab/methods/source-native-comparator-routing.md).

## 1. Source premise and prior coverage

The [Portal transcript](../../lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md), timestamp **01:48:59**, says **“if shiab is a derivation”** while discussing rolled spinor0/1-form paths, curvature followed by Shiab, and two connections. The source does not identify the product, give a Leibniz formula, specify the action on every form degree or establish C-infinity linearity for that assertion.

The [source reinspection](../../lab/sources/gu-shiab-derivation-principal-bianchi-source-reinspection-2026-08-05.md) distinguishes four meanings: an inner derivation at a coefficient-product node; a full graded derivation; principal-Bianchi kernel transport; and a complete moving Euler complex. It binds draft pp42–44/eqs8.7,9.2–9.6 to the invariant-map and degree grammar, §8.2/p43 footnote10 to the missing historical selector (SC-OP-02), and summary eq12.7 to a Bianchi analogy. SC-OP-03 attributes the displayed Weyl-killing, Ricci/scalar-preserving claim. None supplies the exact full derivation hypotheses used below.

The [August5 selector](../k77-wave2-principal-bianchi-product-selector-2026-08-05.md) already proves that `comm,symi,symi` is the unique nonzero principal-Bianchi survivor among the eight displayed product assignments, with Riemann restriction equal to minus twice the ambient Einstein map. It explicitly disclaims a full degree11 derivation. The new question is whether that nonzero restriction can extend to a full suite. No old product census or native rank is rerun.

This also differs from the [fixed-Shiab Euler obstruction](printed-shiab-endpoint-audit-2026-11-27.md): full derivation is the premise here, and no variational correspondence is assumed. The short classification and curvature consequence use standard algebra and geometry; no world-novelty claim is made.

## 2. Algebra, grading and theorem

Let V be a complex oriented nondegenerate quadratic space of dimension14 and S its full Dirac module of dimension128. Put

    A = Lambda*(V*) tensor End_C(S).

The product is exterior multiplication with ordinary matrix composition. Matrices have degree0. An associative degree11 derivation satisfies, for homogeneous u of exterior degree p,

    delta(uv)=delta(u)v+(-1)^(11p)u delta(v).             (1)

The induced graded-Lie bracket is

    [u,v]_gr=uv-(-1)^(deg u deg v)vu.

For decomposable forms this is `(alpha wedge beta) tensor [X,Y]`. A degree11 graded-Lie derivation instead satisfies the corresponding graded bracket rule. Both are assumed complex-linear at a fibre, C-infinity-linear on sections, and equivariant under the diagonal full Spin action.

Choose complex orthonormal coordinates, write gamma_I for an antisymmetrized Clifford blade, and define

    Phi_k=sum_(|I|=k) e^I tensor gamma_I,
    Theta3=*form Phi_3,       Theta11=Phi_11.           (2)

Metric raising is understood in general coordinates. Changes of factorial convention rescale these nonzero basis elements only.

**Theorem.** In either derivation class,

    delta=ad_Theta,
    Theta=a Theta3+b Theta11,
    ad_Theta(u)=Theta u-(-1)^(11 deg u)u Theta.          (3)

The two parameters are complex at each fibre. Globally a,b may be smooth scalar functions; their derivatives do not enter this pointwise map. Every such inner map is an associative, hence graded-Lie, derivation. The two maps remain independent on degree2. Their degree2 restrictions annihilate every algebraic Riemann spin curvature.

## 3. Associative completeness

Restrict delta to constant matrices. Coefficients in a basis of Lambda11 are ordinary derivations of a full matrix algebra, so they are inner. For completeness, if D is such a derivation and E_ij are matrix units, set

    X=sum_i D(E_i1) E_1i.

Differentiating `E_kl E_i1=delta_li E_k1` and summing after multiplication by E_1i gives `[X,E_kl]=D(E_kl)`. Subtracting a scalar matrix makes X tracefree without changing its commutator. Thus delta has a unique tracefree inner coefficient Theta in Lambda11 tensor sl(S).

Subtract ad_Theta. The residual kills every constant matrix. Apply its product rule to a matrix times a central one-form, in both orders: the residual value on that one-form must commute with all matrices. It is therefore scalar-valued. The residual is exactly the exterior-algebra derivation determined by

    K: V* -> Lambda12(V*).                              (4)

Spin equivariance kills K. In the complex orthogonal group, minus the identity acts as minus1 on V* and plus1 on Lambda12. Equivariance would give K=-K. Uniqueness of the tracefree inner coefficient implies that Theta itself is Spin-invariant.

Finally the full Dirac Clifford identification gives

    End_C(S)=Cl(V)=direct_sum_(k=0)^14 Lambda^k V

as Spin modules. Lambda11 is Hodge-equivalent to Lambda3; in this list only k=3 and k=11 carry that irreducible module, each once. Hence the invariant Theta space is precisely the two channels in(2). No enumeration of general Shiab maps is required.

The matrix-inner fact is also recorded in de Goursac, Masson and Wallet, *Noncommutative epsilon-graded connections*, J. Noncommutative Geometry6(2012), Proposition3.5; the ordinary matrix case is sufficient here. [Primary paper](https://ems.press/content/serial-article-files/30507). The scalar-exterior remainder is the algebraic insertion part of the usual derivation decomposition; the generator argument above proves the part needed here directly.

## 4. Graded-Lie completeness and full real u(H)

The center of A is the scalar exterior algebra. Its derived ideal is Lambda*(V*) tensor sl128. A Lie derivation preserves each. Restrict delta to constant sl128 and expand in exterior11 coefficients. Each coefficient is an ordinary Lie derivation of sl128 and hence inner.

A short root proof supplies that last fact. For a Cartan subalgebra, differentiating `[h,h']=0` shows each root component of D(h) is proportional to its root evaluated on h. Subtract a root-valued inner derivation to make D preserve the Cartan. Differentiating `[h,E_alpha]=alpha(h)E_alpha` then forces D(h)=0 and D(E_alpha)=c_alpha E_alpha. The root brackets give `c_(alpha+beta)=c_alpha+c_beta` and `c_(-alpha)=-c_alpha`. For sl_n this means `c_ij=lambda_i-lambda_j`; a tracefree diagonal inner derivation removes them all. Thus D is inner. Applied coefficientwise, this produces the unique tracefree Theta.

After subtracting its graded inner action, the residual kills constant sl128 and commutes with their adjoint action. That module is irreducible, so the residual has the form

    delta(alpha tensor X)=d(alpha) tensor X

on the traceless ideal. The graded-Lie rule on a pair with nonzero [X,Y] forces d to satisfy the scalar exterior Leibniz rule. It is again determined by(4), and Spin parity kills it.

The central residual need not satisfy an associative Leibniz rule, but equivariance still kills it: on exterior degree p, minus the identity acts by `(-1)^p` at input and by its negative at output degree p+11. Thus there is no central contribution. Uniqueness again makes Theta invariant, giving exactly(3).

**Real-form boundary.** Full real u(H) is a Lie algebra, not an associative algebra. Its complexification is gl128(C). A real C-infinity-linear graded-Lie derivation with the stated Spin equivariance complexifies to the class just proved, so its Riemann restriction also vanishes. We do not assert that both arbitrary complex channels preserve every real structure or equate K77 with K95.

For a noncompact real signature, minus the identity need not lie in the identity component of the real orthogonal group. The parity arguments above do **not** assume that it does. Equivariance for the real Spin Lie algebra complexifies to so14(C), and finite-dimensional intertwining then integrates to connected Spin14(C), whose action covers minus the identity. This justifies the parity test for each compatible real form separately.

## 5. Curvature silence, including variable scalar coefficients

Let B be the Levi-Civita spin connection of an oriented metric. Each canonical basis tensor Theta3 and Theta11 is parallel: it is built from the metric, orientation and Clifford multiplication, all preserved by B. Torsion freeness identifies its covariant exterior derivative with alternation of that parallel derivative. Hence, for j=3,11,

    d_B Theta_j=0,
    d_B^2 Theta_j=[F_B,Theta_j]_gr=0.                   (5)

Degrees2 and11 have even product, so(5) implies

    ad_(Theta_j)(F_B)=0.                               (6)

If a,b vary with position, the combined Theta need not be parallel. We apply(5) separately to the **parallel basis tensors**, then use pointwise linearity:

    ad_(a Theta3+b Theta11)(F_B)=0.                     (7)

The Levi-Civita B here is not identified with a source chimeric or reference connection merely by sharing its letter; a source application needs the matching soldering and connection identification.

Every algebraic Riemann tensor is realized by a metric2jet in normal coordinates. Therefore(7) is the full fibrewise Riemann restriction, not just a statement about selected backgrounds.

There is also a direct algebraic check. For `F_ij=(1/4)R_ijbc gamma^bc`, Hodge-dualizing the Theta3 output gives a nonzero convention scalar times `sum_ij[gamma_aij,F_ij]`. The Clifford commutator expands as

    [gamma_aij,gamma_bc]
      =2(g_ab gamma_ijc-g_ac gamma_ijb
          -g_ib gamma_ajc+g_ic gamma_ajb
          +g_jb gamma_aic-g_jc gamma_aib).              (8)

The Ricci contractions vanish against the alternating Clifford indices. The remaining term is proportional to `R_ijac gamma_ijc`, zero by pair symmetry and first Bianchi. Theta11 differs from Theta3 by a nonzero convention scalar and Clifford-volume multiplication; volume commutes with spin bivectors, giving the same result. This is a sign/control route independent of any Euler identity.

## 6. Nonzero controls and the strict premise difference

The theorem does not say delta=0. In complex orthonormal coordinates take

    F=e1 wedge e2 tensor gamma3.                       (9)

For Theta3 the output13form missing index4 has coefficient `[gamma124,gamma3]=plus-or-minus2 gamma1234`, nonzero of coefficient grade4. Theta11 is zero in that component. For Theta11 the output missing index3 has coefficient `[gamma_(4...14),gamma3]=plus-or-minus2 gamma_(3...14)`, nonzero of grade12; Theta3 is zero there. Thus every nonzero linear combination of the two channels has a nonzero degree2 action. This curvature is general adjoint-valued curvature, not an algebraic Riemann spin curvature.

If full Spin equivariance is dropped, an exterior insertion K survives. For example, set `K(e1)=e3 wedge ... wedge e14` and K zero on the other generators. Its degree11 extension sends an e1 wedge e2 curvature component to a nonzero13form; a sectional Riemann curvature provides a control. This adds a symmetry-reducing tensor and is outside the theorem.

If full derivation is weakened to the owned principal-Bianchi condition, the nonzero Einstein survivor remains. It is therefore a genuine contrary control to identifying the two conditions. Its nonzero Riemann response proves that it cannot extend to either complete derivation suite here. The result does not decide whether any Riemann-silent displayed row extends.

A covariant exterior derivative is not C-infinity-linear. A map defined only on selected degrees, a derivation relative to another product, a spinor-module rule, a different total grading or extra moving tensors may also escape. Their source ownership and compatibility require their own definitions; being outside this theorem is not proof of viability.

## 7. Decision, reuse and verification limits

**Consumed:** the literal full associative or graded-Lie derivation route to a nonzero Riemann-response Shiab with these inputs. **Retained:** the weaker principal-Bianchi survivor and other explicitly different source interpretations. No source action, physical gravity equation, class-C inhabitant or GU-wide exclusion is constructed. Source assertion polarity, canon and physics-ledger verdicts remain unchanged.

The shared missing ingredient is the actual source derivation/module/chain law and its complete carrier/grading; it is not a request for another scalar coefficient fit. The strongest alternative considered was a translation-dependent or differential integrating multiplier for the printed endpoint. That escapes the fixed-multiplier theorem but lacks an owned form and a bounded complete test. The present question has an explicit source hook and a short universal proof without native rebuilding.

`Lean/GUFormalization/ShiabDerivation.lean` contains only two finite algebraic cores: the coefficient commutator Leibniz identity and annihilation of one input by a linear combination of two maps already known to annihilate it. It does not formalize the full graded classification, Clifford representation, real-form transfer, parallel-tensor argument, algebraic-curvature realization or source semantics.

The companion exact probe is owned and executed separately. Sparse exterior/Clifford checks calibrate products, signs, nonzero general-curvature responses and countercontrols; finite samples do not prove the whole class. Root verification and independent T1 review record execution, hashes and acceptance separately. No execution or compilation is claimed by this report's author, and internal review is not external-expert verification.
