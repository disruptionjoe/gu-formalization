---
status: exploration
doc_type: structural-result
created: '2026-11-25'
program_target: LB-CLASS
tier: T2
expected_delta: Compute the actual finite Euler system and attempt finite-coupling continuation; decide
  actual sector protection and finite observed-state closure.
actual_delta: Two exact kappa1 local homogeneous stationary backgrounds in the complete59 fixed family,
  with distinct frame-invariant scalar intervals; actual finite-jet observation nonautonomy. Small-h holonomy
  remains a separate theorem.
class_covered: 'Fixed W2 K95 full-U candidate: complete reality/reflection-fixed homogeneous59 family,
  two kappa1 backgrounds and the small-h analytic branch, and unrestricted local analytic independent-row
  matter solutions. Not all class C.'
premises:
- lab/sources/source-claim-register.yaml#SC-ACT-01
- lab/sources/source-claim-register.yaml#SC-ACT-05
- lab/sources/source-claim-register.yaml#SC-GEO-51
- lab/sources/source-claim-register.yaml#SC-GEO-55
- lab/sources/source-claim-register.yaml#SC-CHI-01
- lab/sources/source-claim-register.yaml#SC-CHI-51
- lab/sources/source-claim-register.yaml#SC-CHI-52
- explorations/conditional-build/source-action-wave2-construction-2026-11-25.md
- explorations/conditional-build/source-action-homogeneous-analytic-vacuum-2026-11-25.md
source_bridge:
  status: conditional
  reason: Source ingredients inform this completion; neither this action nor a parallel sector split nor
    the unrestricted analytic physical state category is source-required.
kill_condition: Only this realization or the precisely named parallel-projector/finite-local-encoding
  route can be excluded. Failed continuation is not a nonexistence proof. No source or class-C exclusion.
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
title: What the actual candidate vacuum preserves, mixes, and cannot predict from section data
---

# What the actual candidate vacuum preserves, mixes, and cannot predict from section data

```yaml
program_target: LB-CLASS
tier: T2
expected_delta: Own the finite native Euler system and test the actual background's sector and observation dynamics.
actual_delta: Two exact normalized stationary backgrounds, complete59 coefficients and actual finite-jet nonautonomy; separate small-h holonomy. Scientific verdicts unchanged.
```

## Main finding

**The fixed candidate action now has at least two rigorously certified local stationary backgrounds at its target normalization, kappa=1.** Both satisfy the full connection equation and the declared coupled product-regulator variations. An exact scalar-invariant interval distinguishes their admitted frame orbits. This removes the previous “only sufficiently large kappa” existence limitation; it does not establish stable physical vacua or source selection.

Having an action and a stationary background is not sufficient to define an autonomous observed theory. On this candidate's **actual curved equations**, two exact local classical configurations can agree on every piece of any prescribed finite-order local differential encoding of the initial section state and differ later. Adding a fixed number of normal derivatives cannot repair that loss of information. A proposal for deterministic closed observed evolution on this candidate must specify which bulk solutions are admissible, supply additional state or nonlocal information, or change the observation prescription.

A second result rules out a simple repair: on the actual small-h vacuum, the spinor connection has **no nontrivial parallel complex sector projector**, even allowing arbitrary deformations of that projector. This excludes protected sectors of that precise kind. It does not exclude source2+1, effective low-curvature separation, or sectors defined by constraints or observation on the larger carrier.

The computation also reveals a less expected positive structure. The unique branch preserves an antilinear quaternionic symmetry which **reverses the Krein form**. This is the orthogonal/quaternionic real form, not an assumed Sp(32,32) restriction. Together with a reflection already respected by the candidate equations, it reduces continuation from 216 real variables to a complete **59-dimensional** family. The full equations generate all 59 directions; this is a symmetry consequence, not a chosen small ansatz.

These are applications of established mathematics to this particular completed candidate, not claims of new general theorems or a falsification of GU. **Weakest physical link:** source selection of the action, physical state/constraint domain and observation. **Class-C representativeness:** unproved. **Source necessity of the excluded mechanisms:** unproved. K95 is retained separately from K77; total, observed and physical gradings remain distinct.

**Internal acceptance:** three specialist agents cross-reviewed sections they did not author; additional certificate and finite-coupling reviews agree. Root ran251 exact structural controls, all1830 full-tensor coefficient replays, recursive59-generation verification and exact root/invariant certificates. This is internal mathematical acceptance, not external-expert certification. No Lean, paper release, source/physics-ledger verdict or governance change is claimed.

```gu-typed-objects
result: actual homogeneous vacuum symmetries, spinor transport and finite local observation nonautonomy
carrier: actual K95 full Dirac and full one-form-plus-scalar carrier LAYER=ambient+observed BRIDGE=literal_section_contraction CHIRALITY=S-FULL-DIRAC
pairing: actual real Krein/form pairing and independent barred rows ON=full_Dirac_field_module
real_structure: full complex rank128 candidate; emergent J squared minus one with JHJinverse minus H
grading: Clifford degrees and declared observed contraction; no physical chirality or family identification
action_owner: repository-construction fixed W2 comm/symi/symi plus SEminusonehalf completion
target: full Euler receiver and literal observed fields MAP-TYPE=contraction
```

> **GU-COMPARATOR-ROUTING — scope before inference.** Read [source-native routing](../../lab/methods/source-native-comparator-routing.md). FullU, independent bars, non-Levi-Civita displacement, source2+1 and literal contraction are retained. The ambient imposter label is not substituted for its observed gamma-trace image. No positive-comparator, mirror-family, standard Higgs or repeated-three-generation assumption enters these results.

## 1. Actual native geometry and Euler coefficients

The fixed action, variation class and preceding analytic existence theorem are in the [homogeneous result](source-action-homogeneous-analytic-vacuum-2026-11-25.md). The new engine reconstructs their geometry rather than fitting a convenient constant-coefficient operator.

At the homogeneous origin, use horizontal eta=diag(1,1,1,-1) and vertical eta-self-adjoint matrices A, with physical vertical tangent U=-2 eta A. The metric is

    G_H(v,w)=eta(v,w),
    G_N(A,B)=4 tr(AB)-2 tr(A)tr(B).

The rational orthogonal frame has Gram diagonal

    [1,1,1,-1,-16,8,24,48,8,8,-8,8,-8,-8].

It has signature(9,5), volume factor196608, raised Ricci1/4 on horizontal+trace and-5/4 on traceless normal, and scalar curvature-10. Exact Nomizu torsion, compatibility, Bianchi and spin-injection controls authenticate these conventions. The invariant trace generator has divergence-4: **the gradient of a restricted constant action density would not give the actual field Euler equation**.

### Representation and real branch

Every form is a sparse dictionary `(exterior_mask,Clifford_mask) -> Fraction`. Clifford generators satisfy gamma_i²=d_i, where the rational orthogonal tangent Gram diagonal is supplied by `source_action_deep_geometry.py`. Ordered blades use increasing indices. Their product is the swap sign times the product of d_i on overlapping indices.

The actual Phi recipe contains two i-anticommutators. Their i² cancels the printed negative coefficient, leaving precisely the real-coefficient formula already used in the native W2 probe. B and S have real Clifford coefficients; the commutator derivative, Phi, its real pointwise adjoint and the cubic Euler operations preserve that real subspace. Beginning with S therefore does not require Gaussian coefficient arithmetic. This is an equivariance/closure property of the selected completion, not an imported source restriction to Sp or a claim that full u(64,64) has been replaced.

The real Clifford blades that are H-skew have degree1 or2 modulo4. The full u(H) additionally contains i times blades of degree0 or3 modulo4. Those are outside this real branch, but the full Euler residual of a real-branch field has no omitted imaginary receiver because the operations preserve the real H-skew sector. Root's independent reality arc identifies the real fixed form; the engine itself does not need to assign a group name.

### Nonunit Hodge and pairing

Let D_I=product_(i in I)d_i, v=sqrt(abs(product_i d_i))=196608, and ε(I,Ic) the wedge sign. Then

    *(theta^I gamma_C)=ε(I,Ic) v/D_I theta^Ic gamma_C.

The inverse includes `(-1)^(p(14−p)+5)` relative to star. The scalar trace/form pairing weight is

    w(I,C)=−[gamma_C gamma_C]_scalar / D_I.

This is the reporting-normalized real pairing b=−Re tr/128, without a volume density factor. A common fixed trace normalization cancels from every Euler/adjoint formula. In particular w({i},{i})=−1 for all14 diagonal one-form/gamma receivers, despite the nonunit d_i.

For a fixed coefficient-form A, the pointwise adjoint of `V -> A wedge_kind V` is computed by reversing each actual sparse term and multiplying by `w(output)/w(input)`. The same rule produces star's pointwise adjoint. Reversing the full composition

    Phi = *⁻¹ [Phi1 wedge_comm *
               +(1/2)* Phi1 wedge_anti * Phi2 wedge_anti *]

therefore gives the actual Phi†. This avoids guessing signs from a positive-definite comparator or taking a transpose in an unnormalized basis.

### Full derivative Euler operator

For invariant T, the exact covariant exterior derivative is

    (D_BT)_ij=[beta_i,T_j]−[beta_j,T_i]−T([e_i,e_j]_m).

For invariant W of degree2,

    (D_B†W)_a=−sum_i d_i⁻¹(
         [beta_i,W_ia]−sum_k Lambda_ii^k W_ka
                        −sum_k Lambda_ia^k W_ik).

The Lambda terms act on the two form slots. They are necessary even though invariant coefficient arrays are constant in the homogeneous frame. They include the nonunimodular divergence. The engine computes

    K(T)=(Phi(D_BT)+D_B†(Phi†T))/2.

It never substitutes a pointwise transpose of the invariant D map. As an independent check, the invariant trace generator A=cI has divergence−4c. Its scalar directional derivative has invariant restriction0 but formal-adjoint restriction4c; the two operations are demonstrably different.

### Full cubic Euler map

For one-forms define Q_U(V)=V wedge U+U wedge V. Because the form degrees are both1, this is exactly `U wedge_comm V`. Its pointwise adjoint is the same reversed sparse wedge operation above. Thus

    N(U,V)=[Phi(U wedge V+V wedge U)
             +Q_U†Phi†V+Q_V†Phi†U]/6,

and

    N(T,T)=[Phi(T wedge T)+Q_T†Phi†T]/3.

The latter is the exact gradient of `<T,Phi(T wedge T)>/3`. Both adjoint terms are retained; using only the printed endpoint would be a different operator. Root's calibration checks compare its polarization and its written polynomial directional derivative against the pairing with N(T,T).


### Independent native calibration

The engine independently reconstructs curvature and verifies Phi(F_B)=S, with S_a=-21 gamma_a/4 on horizontal+trace and-15 gamma_a/4 on traceless normals. K(S) is nonzero and even. In the rational frame, the unit normal v=e6/6+e7/12 corresponds to U=-eta diag(1,1,-1,-1)/2 and gives receiver+3/4. The earlier native receiver used the opposite U, giving-3/4. This explicit transport reconciles the sign; the coefficient is not tuned. The parallel Clifford one-form has K(Phi1)=0. Pointwise adjoint and complete cubic-gradient controls are separate from invariant derivative checks.

## 2. Reality and reflection select a complete finite family

**Pairing-convention fence:** the earlier `source-reality-mixing-class-2026-11-24.md` uses horizontal Clifford multiplication with sharp sign **plus** (its displayed condition near line138). The current W1/W2 candidate explicitly uses gamma_a^sharp=**minus** and H=i times the five negative gammas. “K95” alone does not identify these pairings. The present anti-isometric-J result binds this actual candidate H; it neither imports the earlier classification unchanged nor declares that differently paired result incorrect.

### Native antilinear structure

In the existing Jordan-Wigner frame, gamma_j is Euclidean Hermitian Gamma_j for j<9 and i Gamma_j for j>=9. Its imaginary matrices have indices

`I={1,3,5,7,10,12}`.

Set `C=gamma_1 gamma_3 gamma_5 gamma_7 gamma_10 gamma_12`, and `J=C conjugation`. Because there are six selected axes, C commutes with every gamma outside I and anticommutes with each inside I. Complex conjugation reverses exactly the selected gammas, so J commutes with all real Clifford generators.

C is real (six imaginary factors), unitary in the auxiliary positive coordinate norm, and

`C²=(-1)^(6·5/2) product_(j in I) eta_j =−1`,

because precisely two selected axes are negative. Hence J is antiunitary and J²=−Id. It is the quaternionic structure of the real Cl(9,5) module; its existence does not impose a new physical reality condition on fields.

The actual Krein matrix is `H=i gamma_9 gamma_10 gamma_11 gamma_12 gamma_13`. Since J is antilinear and commutes with all gammas,

`J H J^-1=−H`.

Thus `<Jv,HJw>=−overline(<v,Hw>)`: J is **Krein-anti-isometric**, not the quaternionic Krein isometry that would define Sp(32,32). Multiplying J by a unit phase does not change this conjugation relation.

### The fixed real algebra and group

Define tau(X)=JXJ^-1. This is an antilinear algebra automorphism, and a real-linear involution on u(H). The H sign reverses twice in the skew-adjoint condition, so tau preserves u(H). Its fixed locus consists of real Clifford coefficients within u(H).

For a real grade-k Clifford blade, `blade^sharp=(-1)^(k(k+1)/2)blade`. Therefore real blades of grades k=1,2 mod4 belong to the fixed skew algebra; the other u(H) basis directions are i times real blades and are tau-odd. The fixed algebra has real dimension

`sum_(k=1,2 mod4) binom(14,k)=8128`,

not8256, the dimension of sp(32,32). Its group is the intersection of the quaternionic-linear group with U(H), with J reversing H. Equivalently it preserves the nondegenerate **complex symmetric** bilinear form beta(v,w)=<Jv,Hw>, together with J. This is the standard defining orthogonal/quaternionic real form commonly denoted SO*(128), up to connected-component conventions. The mathematical statement can use these defining preservation properties without relying on the group name.

The naming distinction was checked against Pavel Etingof's [MIT Lie Groups and Lie Algebras notes, §6.3, Exercise6.16 and following paragraph, pp42–43](https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf): quaternionic Hermitian preservation gives the symplectic form, whereas quaternionic skew-Hermitian preservation gives a complex symmetric form together with the balanced-signature Hermitian form. The calculation here supplies the identification for this specific H/J; the reference alone supplies no GU result.

Restricting the already-counted invariant space E by tau fixes122 real directions; the other94 invariant directions are tau-odd. The per-grade multiplicities supplied by the full exterior-character computation sum over grades1,2 mod4 to122. This is a consequence for the selected branch, not a new source-wide replacement of the216-dimensional full-U problem.

### Why the actual analytic branch is fixed

B is Clifford-bivector-valued with real coefficients, hence tau(B)=B. Hodge and differential coefficient operations are real. The first commutator term of Phi is tau-equivariant. Each i-anticommutator is tau-odd as an operation, but the actual nested term contains **two** such factors, so their signs cancel. Thus Phi is tau-equivariant. The real trace/form pairing is tau-invariant; consequently its real formal adjoints, K and N intertwine tau. S=Phi F_B is fixed.

The exact normalized Euler equation is therefore tau-equivariant. If T(h) is the unique analytic branch through0, tau(T(h)) is another such branch. Uniqueness gives

`tau(T(h))=T(h)`

through its small-h interval. Equivalently every formal coefficient is real-Clifford and convergence preserves that property. The full-U construction has **selected a quaternionic-real subfamily dynamically on this branch**, rather than having that subgroup inserted at the outset.

### Limits and relation to holonomy

This does not alter source SC-GEO-51, establish a general Sp restriction, or impose J as the physical reality condition. It provides no physical generation count, Kramers energy spectrum or positive Hilbert space. Adjoint domains and physical observation remain unbuilt. Algebraic J-pairing of finite kernels requires that the chosen domain and operator preserve J; no analytic kernel statement is supplied here.

Because J reverses the sign of H, no nonzero J-invariant subspace can have H positive definite: a vector of positive H-norm has a J-partner of negative H-norm. This is a statement about this fibre form and symmetry, not a prohibition of a differently constructed physical inner product or constrained observation.

The holonomy calculation can consistently have scalar **complex-linear** commutant and a quaternionic **real-linear** commutant. J is antilinear, so its existence is not a counterexample to complex irreducibility or the absence of nontrivial complex parallel projectors. A full holonomy-group identification does not follow solely from its commutant.


### Reflection reduction

The base reflection P=diag(−1,1,1,1) preserves eta. Its action on the actual14-dimensional rational tangent basis flips indices F={0,8,9,10}: one horizontal axis and the three offdiagonal vertical matrices involving it. Four flips preserve ambient orientation. Its Clifford lift is proportional to gamma0 gamma8 gamma9 gamma10. This is a Krein anti-isometry, but conjugation still preserves u(H), the trace pairing and matrix multiplication. The actual Clifford forms and Hodge star intertwine because the ambient orientation is preserved. Thus S, K and N are equivariant under this reflection, even though it is outside the connected Lorentz isotropy used in the216 count.

The unique small-h branch and the entire S-generated K/N-closed span are fixed by it. For the sparse arrays the exact condition is simply

    (-1)^popcount((exterior_mask XOR Clifford_mask) AND F_mask)=+1.

### Dimension by a twining character

Complexify connected Lorentz isotropy to sl2×sl2. The reflection swaps the two factors. Under diagonal sl2, its action on tangent m decomposes as

    R-positive: spin1 + spin2 +2 spin0 (dimension10),
    R-negative: spin1 +spin0 (dimension4).

Let z record diagonal sl2 weights and t exterior degree. The reflection-twisted exterior character is

    P(t,z)=(1−t²z⁴)(1−t²)(1−t²z⁻⁴)
            × product_(w=−4,−2,0,2,4)(1+t z^w)
            ×(1+t)²(1−t).

An irreducible V_(a,b) with a≠b is exchanged with its partner, so contributes zero reflection trace. On V_(a,a), the canonical swap has twisted trace chi_a(z²). The trace on its multiplicity space is obtained by highest-weight subtraction with step4. Since the tangent inputs are V00,V11,V22 with the same canonical swaps, the reflection trace on E in each exterior degree is the coefficient combination

    c_0+c_2−c_6−c_8,

where c_w is the z^w coefficient of P. Simplification gives

    tr_E(R;t)=(1−t²)²(1+t)²(1+t+t²)(1+t²−t³+t⁴+t⁶),

with coefficients

    [1,3,3,−1,−6,−5,2,6,2,−5,−6,−1,3,3,1].

The previously owned connected-isotropy degree dimensions are

    [1,3,3,7,20,31,30,26,30,31,20,7,3,3,1].

Taking (dimension+trace)/2, then retaining real H-skew Clifford grades1,2 modulo4, gives

    grades:       1,2,5,6,9,10,13,14
    fixed dims:   3,3,13,16,13,7,3,1
    total:59.

The full u(H) reflection-fixed family has108 dimensions:59 in this real branch and49 in its imaginary complement. The source action still lives in full u(H); this additional reduction follows because its given coefficients and S are fixed. If the generated exact rank reaches59 with the bitmask condition verified, it exhausts this known closed fixed space. One may then certify closure structurally; all K/N coefficients are still needed to solve its finite polynomial equations.

### Generated span and reproducible coefficients

The exact generated-span calculation starts with S and repeatedly applies K and polarized N. It reaches rank59 with all six connected-Lorentz infinitesimal invariance checks and reflection/reality checks. The structural fixed-space upper bound is also59, so the generated span exhausts that family. Projecting by Clifford degree and exact row reduction only changes its basis; it makes the final arithmetic much cheaper without discarding receivers.

The [published coefficient JSON](../../lab/process/source-action-deep-coefficients.json) supplies the complete rational basis, source S, linear map K and symmetric bilinear map N. Its convention is

    F_kappa(t)=kappa*t+S+K*t
       +sum_i N_ii*t_i^2+2*sum_(i<j) N_ij*t_i*t_j.

Every exported K and N image is compared in the original form/Clifford coefficient space with its basis expansion. This is full-residual closure, not projected criticality. Native geometry and algebra are executable in the three `source_action_deep_*.py` files. Numerical continuation and exact root certification, if successful, are reported separately; a small residual alone is not existence evidence.

### Target normalization: two exact roots, not numerical residuals

Write the normalized full polynomial as F_h(x)=x+h(S+Kx+N(x,x)). The complete fixed family has32 odd and27 even coordinates. At fixed odd coordinates, the even equation is linear in the even coordinates; the numerical search used that Schur elimination where invertible, together with full-system Newton. No singular Schur stratum is excluded. All accepted claims below come from exact rational checks on the full59 equations.

For each rational center x0 and rational approximate inverse R, define

    e=||R F_1(x0)||_infinity,
    a=||I-R DF_1(x0)||_infinity,
    b >= ||R N||_(bilinear,infinity).

For the map P(x)=x-R F_1(x), a closed radius-r ball is invariant if e+a*r+b*r²<=r, and P is a strict contraction if a+2*b*r<1. The additional a<1 implies R DF_1(x0), hence square R, is invertible, so a fixed point is a root of the actual equation. All these inequalities were evaluated as exact fractions. Decimal centers/inverses are proposals, not trusted floating answers.

| Certificate | Root1 | Root2 |
|---|---:|---:|
| e, approximate display | 1.05308e-16 | 9.08264e-17 |
| a, approximate display | 2.91958e-14 | 4.26304e-14 |
| b upper bound, approximate display | 2.17343e11 | 3.31381e11 |
| Certified coordinate radius, approximate display | 2.10616e-16 | 1.81653e-16 |

Each ball contains exactly one root within the59-dimensional fixed family; uniqueness among all216 invariant directions is not asserted. This does not count all roots. The exact center coordinates, approximate inverses and rational certificates are embedded under `certified_roots` in the coefficient JSON and independently replayed by the native probe.

The original-density metric argument from the previous wave applies to **any** invariant connection root: the constant-base geometry enters through its base connection, all compact base variations give derivatives of the perturbation with x-independent coefficients, and integration in x over the fixed product regulator vanishes. With zero independent matter/bars, these are therefore actual coupled stationary configurations, with no small-h approximation or certified path from zero required. They are local/product-regulator results, not global finite-action or stability certificates.

To distinguish them, take q(T)=-Re tr(T_a T^a)/128 in the held native geometry. If G is its exact symmetric matrix in the59 basis, an infinity-ball error r gives

    |q(x0+delta)-q(x0)| <= 2*r*||G*x0||_1+r²*sum_ij|G_ij|.

The two exact intervals are disjoint:

- Root1: center approximately-0.30502815748117734, error below2.194e-15.
- Root2: center approximately-0.2472604557405219, error below6.992e-15.

Thus they differ under simultaneous admitted U(H) frame transformations of the displacement/reference structures and geometry-preserving isometries. This is not an arbitrary active transformation of Ahat while holding B fixed, a classification of the unbuilt physical gauge quotient, or a positive physical energy.

**Path distinction.** Simple continuation from h=0 stalled near0.1317056. A 1200-step pseudo-arclength exploration crossed a numerical turn and ran back to h≈0.0097514 at larger field norm, without reaching h=1. Neither that numerical turn nor the unobserved connection is a nonexistence result. The two h=1 roots were found separately and certified locally. Their connection to the small-h branch remains unproved.

## 3. Actual holonomy forbids a parallel complex spinor split

### 1. Geometry and curvature first jet

Use the rational Nomizu model in source_action_deep_geometry.py: m=H⊕N, H=R^(3,1), N the eta-self-adjoint4×4 matrices, with vertical tangent U=−2eta A. The trace basis element is A_tr=Id. At the origin the Levi-Civita connection maps satisfy

`Lambda_A=0` for every vertical A,
`Lambda_v A=−Av`,
`R_B(v,A)=Lambda_(Av)` as tangent skew endomorphisms.

The last identity follows from the homogeneous curvature formula: the first commutator is zero, [v,A]_m=−Av and the isotropy bracket vanishes. Spin curvature is the spin lift beta(R_B), normalized so `[beta(M),gamma(w)]=gamma(Mw)`; this includes the actual factor1/2, not the historical doubled injection.

T1(v)=(21/4)gamma(v), T1(A_tr)=(21/4)gamma(A_tr), and T1(A)=(15/4)gamma(A) for traceless A. Therefore

`(D_B T1)(v,A)=(t_H−t_A)gamma(Av)`.

For trace A this is zero. For traceless A it is `(3/2)gamma(Av)`.

### 2. Four actual holonomy elements tending to horizontal Clifford vectors

Choose for each horizontal basis vector v a traceless diagonal A with Av=lambda v and lambda≠0. In the given basis one may use eigenvalues1,−1,−2,−3 on the four horizontal axes.

Because R_B(v,A)=lambda R_B(v,A_tr), the analytic family

`C_v(h) = (2/(3lambda h)) [F_A(h)(v,A)−lambda F_A(h)(v,A_tr)]`

extends analytically to h=0 with `C_v(0)=gamma(v)`. For each nonzero small h, C_v(h) is an element of the **actual holonomy Lie algebra at the origin**, since curvature endomorphisms and their real linear combinations are in it. No first-order approximation is substituted for that actual curvature; its Taylor expansion merely establishes the limit.

### 3. Ten additional elements tending to normal Clifford vectors

The curvature family `F_A(h)(v,A_tr)` tends to beta(Lambda_v). Hence

`D_vw(h)=[F_A(h)(v,A_tr), C_w(h)]`

is an actual holonomy element and tends to `gamma(Lambda_v w)`.

For horizontal v,w and vertical A, Koszul gives

`G_N(Lambda_v w,A)=eta(Av,w)`.

The map Sym²H→N defined by (v,w)↦Lambda_v w is an isomorphism: the pairing on N is nondegenerate, and eta(Av,w) identifies self-adjoint A with symmetric bilinear forms. Thus the ten choices v_i,w_j with i≤j span the entire normal space. Together with the four C_v limits they give14 independent Clifford-vector limits. Rational Nomizu controls check these identities and the rank10 assertion directly.

### 4. Why this excludes even nonanalytic deformations of a projector

Take fixed real linear combinations of these14 analytic endomorphism families so their h=0 values are a Clifford basis. Their products over subsets form16384 matrices, whose h=0 values are the Clifford blades and span End_C(S). A nonzero determinant/minor at h=0 remains nonzero for sufficiently small h. Thus the complex associative algebra generated by these actual holonomy elements is all End_C(S), for every sufficiently small nonzero h.

Consequently the holonomy's complex-linear commutant consists only of scalar multiples of Id. Every parallel complex endomorphism lies in that commutant. A parallel projector must be0 orId; a parallel complex grading involution must be+Id or−Id. This conclusion allows any h-dependent projector, even a nonanalytic one: the commutant is scalar separately at each h. It does not merely test a fixed gamma grading, and it does not assume the reference spin holonomy was already full.

The calculation proves complex irreducibility and scalar complex commutant. It does **not** identify the full holonomy Lie group. The emergent quaternionic antilinear J may still commute with it; that is fully consistent with scalar complex-linear commutant.

#### Parallel Hermitian-form corollary

The actual connection preserves H. If another Hermitian fibre form G' is parallel, `H^-1 G'` is a parallel complex endomorphism. Hence `G'=cH` with locally constant real c. Every nonzero such form is indefinite, so this connection admits **no positive-definite parallel Hermitian fibre form** on the full spinor bundle.

This is not a physical unitarity no-go. A positive Cauchy-surface current, constrained physical state space or observed quotient need not be a positive connection-parallel fibre form. The corollary excludes this precise candidate route to positivity and no larger class.

### Scope and source relevance

This is a genuine upgrade from generic allowed mixing probes to a property of the actual constructed background: it admits no nontrivial parallel complex spinor subbundle split near the small-h branch. Any mechanism using such a parallel splitting cannot provide its protected sectors on this candidate background.

Source low-curvature dark separation and2+1 need not require a parallel spinor projector. They could be approximate, dynamical, observation-dependent, constrained or carried by the larger vector-spinor system. No source claim, whole class C, physical chirality or particle-family count is falsified by this theorem. It also makes no new unrestricted Cauchy or normalizability claim.

The proof uses the actual curvature of variable-coefficient smooth solutions and finite-dimensional analytic openness, not another frozen-symbol or constant-coefficient ultrahyperbolic argument. Higher T2 and subsequent coefficients affect O(h) corrections to the rescaled operators, but cannot remove their limiting independence.

## 4. Actual curved solutions and finite observed-state closure

### 1. Actual objects and analyticity

Fix either of the two certified kappa=1 invariant stationary connections above, or any sufficiently small positive h on the previously published branch, on the actual flat-base metric bundle. The local affine action, associated spin/Krein representation and orbit transport are real analytic. An invariant section is transported from a fixed finite-dimensional value by that analytic action. Therefore the fixed invariant displacement, the reference geometry, B0 and the actual fermion coefficients are real analytic in local coordinates. This is stronger than merely assuming a smooth formal series; no explicit216-coordinate formula is needed.

Use coordinates `(t,x^1,x^2,x^3,z^1,...,z^10)` near a point of the constant-metric section, with the section `z=0`. Choose an analytic spin frame independent of base x and adapted at the point. The carrier is the original

    E=(T*Y tensor S) direct-sum S, dim_C E=15*128,
    chi=(zeta,nu),
    q chi=(zeta_H,nu)|_(z=0), dim_C output=5*128.

This is literal field contraction, not the auxiliary six-slot receiver or the equation-row diagnostic. The source's2+1 labels are not replaced by three independent copies. The theorem requires no physical family or weak-chirality identification.

The full equation is

    A_t(z) partial_t chi + sum_i A_i(z) partial_xi chi
       +sum_a B_a(z) partial_za chi+C(z;h)chi=0.

All actual reference-connection and induced zero-order terms are in C. At the section choose dt horizontal timelike and dz^1 a non-null normal covector, orthogonal in the native metric. W2's exact principal identity gives

    R sigma(xi) F^-1 = diag(c_xi,-c_xi).

Consequently A_t and B_1 are invertible at the point; A_t stays invertible on a smaller neighborhood. The source-real-form distinction is preserved: complex K95 fields with independent barred rows, not a Majorana or quaternionic restriction.

### 2. A general analytic-system lemma

Consider any first-order analytic linear system of the displayed form with A_t invertible and at the selected point B_1 invertible. Let q be a nonzero analytic readout on z=0. For any positive integer N prescribe the analytic Cauchy data

    chi(0,x,z)=(z^1)^N b,

with a constant vector b in the chosen local frame. The analytic Cauchy theorem gives an actual local analytic solution, unique in the analytic class for these **full hypersurface data**. For complex coefficients split real and imaginary parts; complex invertibility of A_t gives invertibility of the realified system. The theorem supplies no Sobolev stability or common existence radius uniform in N.

Let `M=-A_t^-1 B_1` at the selected section point. Solving for partial_t gives a first-order spatial/normal differential operator L. Its N-fold time differentiation has leading normal term `M^N partial_z1^N`; derivatives of coefficients and the zero-order term reduce the number of derivatives hitting the initial datum. Therefore

    (partial_t^j chi)|_(t=0,z=0)=0,          0<=j<N,
    (partial_t^N chi)|_(t=0,z=0)=N! M^N b.

The same induction works for time-dependent analytic coefficients: extra time derivatives of L have lower differential order. In the actual vacuum the coefficients are x/time independent, which makes this even simpler. Derivatives of q in time also multiply vanished lower jets.

Choose v with qv nonzero and set `b=M^-N v`. Then

    partial_t^N(q chi)(0,x0)=N! qv !=0,
    q chi(t,x0)=t^N qv+O(t^(N+1)).

Thus this solution and the identically zero solution have identical observed initial data but different observations at arbitrarily nearby later times. Their full ambient Cauchy data differ; there is no failure of deterministic full-system evolution.

The analytic existence step is the standard first-order system theorem in [Leon Simon, Lectures on PDE, Lecture3, pp21–27](https://math.stanford.edu/~lms/lecs-on-pde.pdf). The readout/jet argument above is the application; that reference does not assert any GU result.

### 3. Every finite normal-jet augmentation, including spatial derivatives

Fix r and take N=r+1. On the initial section,

    partial_z^alpha chi(0,x,0)=0 for every |alpha|<=r,

identically as functions of the three base-spatial variables x. Hence **all** their base-spatial derivatives vanish too, of arbitrary order. This grants the proposed observed state more information than q alone: even the complete ambient field's normal jets through r do not distinguish the two initial data sets.

For a more general finite local differential encoding, let its components depend on finitely many jets `partial_t^j partial_z^alpha partial_x^beta chi` at the section. Choose N greater than the maximum of `j+|alpha|` used by that encoding. Arbitrary additional spatial derivatives do not remove a power of z^1. The differential-order induction gives equality of all those encoded initial fields and all their spatial derivatives. Nonlinear functions of these finite jets also agree, because their arguments agree. The bosonic background and barred fields are identical in the two solutions.

Define a **deterministic autonomous section-state law** as a law whose supplied initial section-state fields (including all required spatial data and the same fixed background/external inputs) uniquely determine later literal observations. If its state is such a finite local differential encoding and it reproduces all the admitted analytic solutions, the pair above is impossible: the initial state is identical but the later observation differs. Therefore no such deterministic finite-jet closure exists on the unrestricted local analytic solution category.

This does not exclude arbitrary finite nonlocal encodings, a whole observed history, an independently supplied auxiliary state, infinitely many normal derivatives, or a constrained solution category that excludes these data. In particular, it is not a claim that every conceivable finite-dimensional hidden model is impossible. It excludes the precisely defined local finite-differential repair of the actual section readout.

### 4. Native principal transport makes the construction explicit

Choose orthogonal covectors theta=dt and ell=dz^1 with squared norms epsilon_t and epsilon_n. The equation-row transformation cancels in the evolution matrix:

    M=-sigma(theta)^-1 sigma(ell)
      =F^-1 diag(-c_theta^-1 c_ell,-c_theta^-1 c_ell) F,
    M²=-(epsilon_n/epsilon_t) Id.

This is an honest similarity for the **evolution matrix**, despite F and R being different maps for the original first-order operator. It does not identify the original operator spectra by left/right equivalence.

With epsilon_t=-1, a positive normal direction has M²=+Id; a negative normal direction has M²=-Id. Either is invertible. The counterexample can use the positive normal direction, so it does not depend on an imaginary-frequency instability. Take v with only the independent scalar-spinor slot nonzero; qv is explicitly nonzero. Then b is obtained by a finite power of M or -M. No particle-family identification is introduced.

### 5. Exact coupled classical lift, and its physical ceiling

In the declared action the fermion term is `Re integral bar_chi D_A chi dmu`, with barred row an independent primitive. Set `bar_chi=0` identically and use the exact analytic solution chi above. Then:

- variation in bar_chi gives `D_A chi=0`, already solved;
- variation in chi gives the adjoint equation on zero bar_chi, hence zero;
- every connection, metric, density and frame variation of the fermion term has a factor bar_chi, so its backreaction is zero;
- the original bosonic stationary background and compact two-frame equation remain solved.

After shrinking to a common product chart inside the analytic existence neighborhood, both this solution and the zero-fermion solution are actual stationary configurations of the complete **independent-row classical candidate** under its declared product/compact variation class. There is no infinite-series or frozen-coefficient substitution in this argument.

This exact lift is not a physical reality contour: imposing `bar_chi=chi^dagger H` would forbid the nonzero-chi/zero-bar example. No such contour or positive state space has been selected here. The weaker conclusion already holds for actual linearized coupled matter perturbations around the vacuum, since the current and metric backreaction start quadratically. The theorem does not authenticate those perturbations as physical particles or distinguish the observed2+1 sectors.

### 6. What changed relative to prior results

- The Nov25 `solution-observation-trace` theorem has exact frozen constant-coefficient solutions and sharp norm results; it explicitly warns that lower-order terms can destroy its special slab family. This result retains the actual curved operator and all lower terms but concludes **nonautonomy**, not norm nonclosability or any Sobolev threshold.
- The engineering current theorem supplies a pointwise hidden-input detector and already has a non-pure-gauge extension. This result supplies actual solution pairs with the same entire finite initial observation jet, rather than repeating that detector.
- No local/global analytic norm, uniform time interval, physical state restriction, or uniqueness of the observed system has been smuggled in. Analytic full-system uniqueness is compatible with the result because the full initial data differ.

**New demand:** a deterministic source-observed evolution cannot be justified on this unrestricted analytic candidate class by merely appending finitely many normal derivatives. Any successful repair must state the additional solution restriction, nonlocal/history information or independently supplied state that distinguishes the constructed pair. That is a typed requirement, not an instruction to halt other work or a GU falsification.


## 5. What this does and does not settle

| Result | Entire scope covered | What remains unproved |
|---|---|---|
| Two kappa=1 stationary backgrounds | Full59-polynomial roots and declared coupled local product variations; exact frame-invariant separation | Stability, physical selection, global domain and source/C membership |
| 59-dimensional reduction | Complete real/reflection-fixed connected-isotropy family of the fixed action; all Euler receivers | Physical selection of this action or branch; source-wide replacement of fullU |
| Scalar complex spinor commutant | Every sufficiently small nonzero h on the actual analytic branch; all parallel complex endomorphisms | Larger carrier, nonparallel/approximate/observed sector separation; full holonomy group |
| No positive parallel fibre form | Every Hermitian fibre form parallel under that spinor connection | Physical Cauchy current, quotient or constrained Hilbert-space positivity |
| No deterministic finite local observation-jet closure | Any finite local differential initial encoding reproducing every admitted local analytic independent-row solution | Physical reality contour, admissible state category, nonlocal/history/independent state |

The holonomy and observation results are complementary. The first prevents repairing the candidate by a parallel split of its full spinor transport; the second requires an actual state-selection or observation mechanism. Neither asserts that GU's source requires the failed repair. The action alone has not selected the observed theory.

The retained alternative is a base-metric response calculation, including whether its leading effective higher-derivative term survives off the observation section. Its proposed Hessian coefficients were **not independently checked and receive no result credit** here. They remain a future mathematical discriminator, not an Einstein, ghost or Mannheim conclusion.

## 6. Verification and continuation receipt

Final arithmetic and continuation status are recorded in [machine-readable evidence](../../lab/process/source-action-dynamics-and-continuation.json). The [cross-review](../../lab/process/hostile-reviews/2026-11-25-source-action-deep-review.md) distinguishes each reviewer from its section author. Checks authenticate exact finite arithmetic; written proofs and hostile review carry the analytic conclusions. There is no external-expert or proof-assistant certification.

Reproduce the structural controls with:

```sh
python3 tests/program-focus/source_action_deep_probe.py
```

For an independent recomputation of every native K/N image, serialized on the local host:

```sh
python3 tests/program-focus/source_action_deep_probe.py --full-coefficients
```

The native probe passes251 structural controls, exact connected-character reconstruction, all basis and recursive-generation checks, both exact contraction certificates and their invariant separation. The coefficient export passed1830 full tensor comparisons (one source,59 linear images,1770 bilinear pairs). No count here denotes independent mathematical proofs. Eight native repository audits are recorded in the evidence.

Optional discovery machinery (NumPy, serialized) is retained in `source_action_deep_algebra.py`: `continue`, `search`, `arclength`, `refine` and `certify`. Discovery outputs can be placed in a temporary directory. The default structural/root verification uses only the Python standard library.

**Next discriminator:** distinguish the two normalized stationary backgrounds through a declared physical state/constraint/observation or stability criterion. The actual finite-jet theorem already applies to both. The small-h holonomy and small-C1 boundary results do not automatically apply at these endpoints. Neither requires the program to stop unrelated eligible science.

The existing [directed packet](../../lab/process/work-packets/source-action-response-discriminators-2026-11-25.md) and [opportunity register](../../lab/process/source-action-opportunity-register-2026-11-25.md) retain the completed mechanisms and exact uncovered successors. Ordinary structural/source priorities, schedules, canon and scientific matrix/ledger verdicts are unchanged.
