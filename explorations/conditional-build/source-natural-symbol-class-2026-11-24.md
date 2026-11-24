---
title: Complete metric-Spin first-order symbol module and observation minimum
status: exploration
doc_type: structural-result
created: 2026-11-24
program_target: LB-CLASS
tier: T1
expected_delta: A complete symbol-category certificate and a scoped observation-rank exclusion; no full-C
  or source verdict
actual_delta: Complete 18-generator metric-Spin symbol module; exterior submodule rank14; internal reviewed
  exclusion of five-spinor autonomous pointwise output, with minimum6s=768 and no source/classC verdict
class_covered: All complex-linear Spin_0(p,q)-natural first-order principal symbols on (V* tensor S) direct-sum
  S, p+q=14, separately (7,7) and (9,5), with coefficients made only from the metric, orientation, Clifford
  structure and arbitrary scalar invariant coefficient functions. For the observation theorem additionally
  impose NW exact-gradient annihilation, a nondegenerate H4 plus N10 splitting, and an invertible timelike
  principal coefficient.
premises:
- SC-OP-04 ASSERTS candidate four-independent-field grammar, not uniqueness; lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md
- 'SC-OP-05 UNCERTAIN: nonzero southeast rivals remain open'
- 'Repository restriction: no independent nonscalar background tensor is allowed in this symbol module'
- Source observation is literal section contraction; tangent-adapted components implement it, not an arbitrary
  projection
source_bridge:
  status: conditional
  reason: The displayed source principal arrows belong after the stated Clifford/Shiab and frame identifications.
    Source fullness, the selected Shiab, general epsilon-dependent tensor coefficients and physical constrained
    reduction are not proved to lie in this metric-only category.
kill_condition: Within this symbol category, exclude a five-spinor-rank pointwise first-order autonomous
  output retaining all literal observations when the NW symbol annihilates gradients and the full timelike
  coefficient is invertible. No class-C or GU exclusion.
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: "INTERNAL \u2014 five-spinor pointwise autonomous readout in the declared metric-Spin exterior-symbol\
  \ class"
canon_verdict_change: none
---

program_target: LB-CLASS
tier: T1
expected_delta: A complete symbol-category certificate and a scoped observation-rank exclusion; no full-C or source verdict
actual_delta: Complete 18-generator metric-Spin symbol module; exterior submodule rank14; internal reviewed exclusion of five-spinor autonomous pointwise output, with minimum6s=768 and no source/classC verdict

# Complete metric-Spin first-order symbols and the observation minimum

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact borders chirality and family-index questions but supplies no physical chirality or family count. Its result binds only the named symbol and observation category. Read `lab/methods/source-native-comparator-routing.md`. Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: complete 18-generator metric-Spin principal symbol module; 14-generator exterior submodule; minimum autonomous observation rank 6s
carrier: E=(V* tensor S) direct-sum S, full complex Clifford S of dimension s=128, V=H4 orthogonal-sum N10 LAYER=ambient+observed BRIDGE=literal-section-contraction CHIRALITY=S-FULL-DIRAC
pairing: none required; barred fields remain independent ON=declared_carrier
real_structure: complex-linear symbols on separately fixed K77 and K95 real vector spaces; no real/quaternionic or Krein-adjoint identification
grading: ambient Clifford volume Omega and auxiliary total grade diag(Omega,-Omega); neither is asserted to be physical weak chirality
action_owner: N/A -- structural principal-symbol classification, no action selected or constructed
target: principal-symbol category and pointwise autonomous observation rank MAP-TYPE=intertwiner
```

## 1. What is new, and what is reused

The November 11 [native RS compatibility result](native-rs-observed-compatibility-2026-11-11.md), Sections A--C, already computes the nine-arrow coefficient conditions inside a declared span, without claiming that span complete. The November 12 [source-symbol observation result](source-symbol-quotient-membership-2026-11-12.md), Sections 8--9, already proves the six-spinor minimum for the narrower wedge-NW / printed cross-arrow category, including separate chirality weights.

New here: prove completeness of the metric-only complex Spin symbol category; retain both chirality copies of *all* cross arrows; extend the normalized-evolution minimum to that entire exterior category. Existing semisimplicity/Jordan calculations and specific operator exclusions are not claimed as new.

## 2. Exact category and complete basis (T2)

Let V be oriented, dim V=n=14, with nondegenerate metric of signature (7,7) or (9,5). Work with the identity component Spin_0(p,q), and the full complex Clifford module S. Write

    c_x^2 = g(x,x) I,
    Gamma(z)=sum_a gamma_a z_a,
    (J u)_a=eta_a gamma_a u,
    Gamma J=n I,
    Omega^2=I, Omega c_x=-c_x Omega.

The symbol parameter x is a vector, with metric-dual covector x^flat; i_x z is evaluation. All arrows below act on the indicated *input* half-spinor; right multiplication by Omega means input-side composition.

The displayed component identities and exact probe use metric-raised one-form coordinates: Gamma(z)=sum gamma_a z_a, J_a=eta_a gamma_a, insertion of x=e_i has coordinates delta_ai, and i_xz=eta_i z_i. In ordinary covector coordinates the same maps are Gamma(z)=sum eta_a gamma_a z_a, J_a=gamma_a, insertion eta_i delta_ai, and i_xz=z_i. Mixing these conventions is invalid. The first replay exposed that implementation error; it was corrected before the passing run. The abstract map statements and proof use the metric consistently. H has signature (3,1); N has signature (4,6) in K77 and (6,4) in K95.

Every equivariant symbol sigma: V -> End(E), E=(V* tensor S) direct-sum S, has a unique expansion in these nine arrows and the same nine arrows composed on the input with Omega:

| Block | Generators |
|---|---|
| NW, one-form to one-form | c_x Id; x^flat Gamma; J i_x; J c_x Gamma |
| NE, scalar to one-form | x^flat Id; J c_x |
| SW, one-form to scalar | i_x; c_x Gamma |
| SE, scalar to scalar | c_x |

Hence the complex dimension is 8+4+4+2=18. Equivalently each arrow has independent input-half weights. This is not an 18-element list of complete differential operators: lower-order terms are unclassified, and scalar coefficient functions are not constants selected by the theorem.

**Completeness proof.** The Clifford identification End_C(S)=Cl_C(V)=direct-sum_k Lambda^k V is Spin-equivariant. Thus blocks with r=1,2,3 vector slots reduce to equivariant maps V^tensor r -> Lambda^* V. For r=1, the vector appears in degrees 1 and13. For r=2, scalar and two-form contractions appear in degrees 0,2,12,14. For r=3, three distinct metric contractions into V and the alternating three-form appear in degrees 1,3 and their volume-duals 13,11. No other exterior power occurs: an invariant tensor with at most three free vector slots consists of metric pairings or the oriented volume tensor; the latter is exactly the Omega partner. These give dimensions 2,4,8 respectively. The displayed arrows span these pieces: the three-gamma product contains the alternating three-form, its remainder consists of the three distinct metric contractions. For r=2 the two-gamma product supplies the two-form in addition to the scalar contraction. Omega partners live in distinct exterior degrees at n14, so they cannot collapse into the low-degree generators. This proves both spanning and independence. Complexification of either real Spin Lie algebra is so(14,C); equivariance under the connected real group therefore gives the same complex-linear module. It does not identify the two real forms, their adjoints or physical domains.

**Scalar freedom.** At any fixed allowed background jet order r, choose the ring R of scalar invariant coefficient functions that the subclass permits. The symbol module is free of rank18 over R, because the displayed basis remains pointwise independent. If class C requires polynomial field-jet dependence, use its scalar polynomial invariants; smooth invariant weights describe an explicitly wider category. No finite count of scalar polynomials, no bound on all background jet orders, and no finite list of full operators follows. Tensor-valued invariants are excluded from this module by definition, not proved absent from the source.

## 3. Exterior and printed membership conditions

On an input half of one-form spinors write NW coefficients a,b,c,d. Evaluating on an exact-gradient symbol x^flat u gives

    T_x(x^flat u)=(a+b) x^flat c_x u +(c+d) J g(x,x)u.

Independence at nonnull x makes gradient annihilation equivalent to b=-a and d=-c, separately in both halves. Thus the full exterior submodule has dimension14: four NW, four NE, four SW, two SE generators. It contains the two additional natural cross-arrow pairs Jc_x and c_xGamma.

The printed derivative arrows d and -d* set the extra NE Jc_x and SW c_xGamma weights to zero (with actual signs and wrappers read from the source). This recovers the 10-generator wedge/printed-cross category of November 12. Setting SE=0 gives its displayed subcategory, but SC-OP-05 does not require that choice for every rival. A selected Shiab additionally fixes its NW coefficients; this theorem does not select them. Independent bars impose no extra equality or adjoint relation among coefficients.

A simultaneous invertible change of field/row frame transports the principal symbol and observation maps; it preserves the rank statement. A variable frame contributes lower-order derivative terms. One may therefore transport a proved member with the source rho(epsilon) wrappers, but cannot treat arbitrary epsilon/background tensors or arbitrary full-U(64,64) covariant coefficients as members without proving their reduction to this module. In particular, naturality under Spin is not the same as commuting with every fixed U(64,64) matrix while keeping Clifford multiplication fixed.

## 4. Entire-category observation minimum (internal T1)

Fix the nondegenerate tangent-normal split V=H plus N, h=4,m=10. The literal source output is

    O0(zeta,nu)=(b=P_H zeta,nu).

P_H is adapted notation for the actual section contraction. An independent projection, or discarding source-visible trace data before observation, is not being substituted. Let the complete symbol lie in the 14-generator exterior class above, and assume D_t is invertible for one nonnull timelike tangent covector. For each tangent spatial covector j define normalized evolution E_j=-D_t^{-1}D_j. A pointwise linear observation F retaining O0 means O0=R F for some map R. Autonomous principal evolution requires ker F invariant under every E_j.

**Theorem.** The largest E_j-invariant subspace inside ker O0 is

    K_R={(zeta_N,0): Gamma_N zeta_N=0}.

Consequently rank F >= (h+2)s=768. The output (b,Gamma zeta,nu) attains this bound. In particular there is no five-spinor-rank pointwise first-order autonomous readout retaining every literal observation under these assumptions.

**Nonvacuity.** The already-tested November12 scalar category contains a symbol with a=1, b=-1, c=d=0, NE=x^flat, SW=-i_x and SE=0. Its owned off-null criterion is a e g [a+(n-1)c] nonzero, which equals -1 here. Therefore the larger fourteen-generator category with invertible D_t is inhabited at principal-symbol grade. This reuses an existing symbol control, not a new action, source selection, or class-C width witness.

**Proof, containment.** The auxiliary grade G=diag(Omega,-Omega) anticommutes with every generator. Hence every E_j commutes with G, and ker O0 is G-invariant. To analyze any invariant K inside ker O0, take v in K, u=E_jv in K. The argument can be applied separately to the two ambient input halves of v and u; their projections need not themselves be in K, since the equality D_tu=-D_jv and vanishing observed components hold componentwise.

Write tau=Gamma_N v, sigma=Gamma_N u in a fixed such half (the traces have the opposite spinor half). Since the scalar and horizontal inputs vanish for both v and u, *all NE, SW and SE coefficients drop out of the horizontal equation*, including the previously omitted cross arrows. Exterior NW gives

    (-a t^flat-c J_H c_t)sigma = -(-a j^flat-c J_H c_j)tau.       (1)

Invertibility of D_t implies a is nonzero in each input half: otherwise D_t kills the nonzero normal gamma-kernel of that half. If c=0, the independent t and j slots of (1) immediately imply sigma=tau=0. If c is nonzero, choose a nonnull horizontal slot k orthogonal to t and j (h>=3). The k component and invertibility of gamma_k imply c_t sigma=-c_j tau. In the t component this cancels the c terms, leaving a sigma=0. Thus sigma=0; invertibility of c_j then gives tau=0. Therefore v lies in K_R.

**Proof, maximality and attainment.** For v in K_R, every tangent i_xv, Gamma v and scalar input vanishes. Hence D_xv=a c_xv remains in K_R. D_t restricts to an invertible map there, since both half weights a are nonzero and c_t is invertible. Therefore E_j preserves K_R. Gamma_N is onto because Gamma_N J_N=mI, so dim K_R=(m-1)s. The full carrier has dimension(n+1)s, giving codimension(h+2)s. The augmented output has exactly that kernel and rank; its quotient inherits an invertible time coefficient. For any F, ker F subset K_R implies the rank lower bound by rank-nullity.

This argument uses no global spectrum, physical state, Fredholm or Kramers premise. It also does not declare the source inconsistent: source dynamics can retain the extra channel, use a constrained solution space, or require a different observation/differential category.

## 5. Exact limits and successor discriminator

- Nonzero lower-order connection/torsion terms cannot cancel a nonzero principal leakage on arbitrary first jets; nevertheless the theorem supplies neither their propagation nor a global domain.
- Derivative-valued or nonlocal outputs, higher-order observed equations, time-history reconstruction, characteristic restrictions, and a separately imposed physical solution constraint are outside the pointwise first-order output hypothesis.
- Additional nonscalar tensor coefficients, explicit H/N tensors in the ambient symbol, non-Spin naturality groups, source-selected nonmetric structure, or singular D_t lie outside this theorem. They must be named as changed categories, not appended as neighboring numerical instances.
- A bound of768 is a number of raw complex components, not particle families or physical degrees of freedom. The source 2+1, luminous/dark separation, K77-to-K95 bridge and all physics ledger verdicts remain open as before.

The practical next question is whether a source-owned constrained observed system discards the gamma-trace channel legitimately, or whether the six-spinor autonomous output is the correct intermediate carrier. The theorem removes arbitrary scalar-weight retuning and the extra metric-natural cross arrows as repairs of the five-spinor first-order readout. It does not authorize building the source action or missing native Fredholm realization.

## Verification status

Root-serialized exact Clifford replay passes 976 controls, 488 in each of K77 and K95. The first replay failed because the implementation mixed raised and unraised index conventions; the corrected implementation passes. The conditional Lean finite-dimensional core proves a rank bound from actual linear-map kernel containment and the stated dimension hypotheses, the six-spinor minimum, exclusion of five-spinor rank, and the numerical 768 consequence, without `sorry`. It does not formalize the invariant-tensor completeness proof, the principal-evolution containment argument, or any physical/global domain. Two independent mathematical reviews and a hostile source/scope review accepted this internal scoped exclusion. The exact probes and conditional Lean proof are retained with the result.

## Method reference

The general natural-operator approach first fixes its geometric category and allowed jet inputs; it does not guarantee a finite list for unrestricted data. See [Kolář–Michor–Slovák, Natural Operations in Differential Geometry](https://www.mat.univie.ac.at/~michor/preprint-shadows/kmsbookh.html). The explicit invariant-theory proof above establishes this narrower symbol module.
