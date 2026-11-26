---
status: exploration
doc_type: structural-result
created: '2026-11-25'
program_target: LB-CLASS
tier: T2
expected_delta: Resolve inexpensive interface, current and coupled compatibility questions from the theoretical
  and engineering assessments.
actual_delta: Complete moving observation and jet-aware boundary transport; native imposter/scalar current
  fingerprints and hidden-probe separation; correct base-metric null variation and explicit fixed-boundary
  formal obstruction.
class_covered: Existing repaired local K95 reconstruction, its source-admitted scalar-SE grammar at fixed
  other arrows, smooth local jets, and a regular inverse-kappa branch around a flat base. Product and
  spherical regulators are distinct. No whole-C coverage.
premises:
- lab/sources/source-claim-register.yaml#SC-ACT-01
- lab/sources/source-claim-register.yaml#SC-ACT-05
- lab/sources/source-claim-register.yaml#SC-OP-04
- lab/sources/source-claim-register.yaml#SC-OP-05
- explorations/conditional-build/source-action-external-datum-candidate-2026-11-25.md
- explorations/conditional-build/exterior-symbol-orbits-conormal-2026-11-25.md
- lab/sources/source-claim-register.yaml#SC-GEN-03
- lab/sources/source-claim-register.yaml#SC-GEN-50
- explorations/conditional-build/source-action-wave2-construction-2026-11-25.md
source_bridge:
  status: conditional
  reason: The source admits SE rivals and prints kappa, but does not select semisimplicity, this coefficient/product
    completion, a large-kappa regime or a physical integer receiver.
kill_condition: Internal defects diagnose this fixed candidate and its added assumptions; no source, GU
  or class-C exclusion or verdict follows.
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
title: 'Source-action engineering wave: observed currents and coupled compatibility'
---

# Source-action engineering wave

```yaml
program_target: LB-CLASS
tier: T2
expected_delta: Resolve concrete observation, current and coupled compatibility questions and preserve opportunities.
actual_delta: Jet-aware observation transport, native current fingerprints, all-order formal product stationarity and fixed-boundary obstruction; no physical/source verdict.
```

## Executive result and scope

The theoretical and engineering suggestions have been turned into three independent exact diagnostic arcs. The [opportunity register](../../lab/process/source-action-opportunity-register-2026-11-25.md) preserves all fifty theoretical lenses and their fifty engineering counterparts, including lower-ranked ideas and corrections. The evidence pool is not a mandatory backlog.

- Literal observation now has a complete moving-section derivative. Fermion boundary transport needs both its moving field-map term and, when the map depends on base-metric derivatives, additional Euler-proportional terms.
- On the owned imposter/scalar inputs, the repaired current has a horizontal rank-one subdiagnostic and normal rank-two subdiagnostic. The missing horizontal trace signal remains in an RS-shaped equation row. The relation is condition-fixed, not source-fixed. Central normal current variations separate every field invisible to the held literal observation, for every SE coefficient in this declared family.
- The geometric first variation vanishes at every formal order under the stated zero-matter/flat-base/product-regulator variations, giving formal coupled stationarity in that test class. A naive unrestricted ambient metric variation would have produced a false rejection. The regular flat-leading connection branch cannot match the supplied pure-gauge spherical boundary, because its reference connection already has nonzero tangential curvature.
- Fixed smooth current probes lose resolution of shrinking same-charge cores at O(epsilon^13). Scalar zeroth-order multipliers cannot repair the existing printed-endpoint Helmholtz principal defect. Analytic convergence and a physical state/readout receiver remain unproved.

These are internally reviewed T2 candidate diagnostics after the review below is complete, not source/physics-ledger or class-C verdict changes. **Source necessity:** conditional. **Weakest physical link:** admissible source dynamics, physical observed sector maps and a solution/domain. **Class-C representativeness:** unproved. The allowed coefficient grammar is not a claim that every coefficient gives admissible physics. No full 2+1 particle prediction, quantum equivalence or physical dark-sector leakage is asserted.

```gu-typed-objects
result: source-action engineering diagnostics
carrier: K95 full Dirac one-form plus scalar and independent rows LAYER=ambient+observed BRIDGE=literal_section_contraction_and_separate_equation_diagnostic CHIRALITY=S-FULL-DIRAC
pairing: original nondegenerate Krein/form pairing and independent dual rows ON=full_Dirac_field_module
real_structure: full U64,64; no K77/quaternionic transfer
grading: source-labeled ambient imposter and scalar inputs; not physical family grading
action_owner: repository-construction using source-print ingredients; same fixed wave2 completion
target: local observation/current and coupled formal compatibility MAP-TYPE=contraction
```

> **GU-COMPARATOR-ROUTING — scope before inference.** Same-named conventional constructions do not identify source-native objects. Read [source-native routing](../../lab/methods/source-native-comparator-routing.md). The source's asymmetric2+1, non-chiral total, independent bars, actual contraction and non-LC displacement remain distinct from three repeated chiral families, projection, Hermitian-bar assumptions or ordinary torsion.

## 1. Observation and variational transport

Status: T2 candidate derivation; validation and review are recorded below. Evidence base: GU `a22bdace5a78a3870d9ce76634d545f89b791dab`, source-action wave2 §2. Scope: the same repaired local K95 completion, independent barred fields, literal section contraction, source 2+1 labels transported by F⁻¹. The statements below do not need a Fredholm domain because they are identities of smooth local fields/jets. They supply neither admissible solution spaces nor physical probabilities.

### 1.1. Complete first variation of the literal observation

Work in local base coordinates x^μ and fibre coordinates y^A (A=1,…,10), with section s_g(x)=(x,g^A(x)). Choose a fixed local trivialization for comparison of the ambient spinor components as g varies. If the chosen observed spin frame is also varied, let U_g denote its component identification; setting U_g=I is a permitted fixed observed-frame convention, not omission of the ambient Clifford variation.

Use precisely the wave2 inverse field map, with n=14:

    Z_a = ζ′_a − (1/2)γ_a η,
    V   = γ^a ζ′_a + (1−n/2)η.

The literal observed variables are

    O_μ = U_g [Z_μ +(∂_μ g^A) Z_A] ∘ s_g,
    N   = U_g V ∘ s_g.

Thus the normal components of Z and of γ^aζ′_a are retained. This is section contraction, not projection onto the horizontal components.

Consider g_t=g+t h and independently varying smooth ambient fields/Clifford coefficients. A dot means derivative at fixed (x,y), in the selected ambient trivialization. Define the material derivative along the moving section by

    M_h W := (dot W + h^A ∂_A W) ∘ s_g.

Then direct differentiation gives

    δO_μ = (δU_g)[Z_μ+g^A_,μ Z_A]∘s_g
           + U_g [M_h Z_μ + g^A_,μ M_h Z_A
                         +(∂_μ h^A) Z_A∘s_g],
    δN   = (δU_g)V∘s_g + U_g M_h V.

Here all ambient-field and Clifford contributions are explicit:

    dot Z_a = dot ζ′_a − (1/2)(dot γ_a)η − (1/2)γ_a dot η,
    dot V   = (dot γ^a)ζ′_a + γ^a dot ζ′_a +(1−n/2)dot η.

The normal-jet terms h^A∂_A act on the entire products, including γ, η and ζ′. In a moving ambient frame, replace component derivatives by the corresponding comparison-covariant derivatives; the frame correction is then included there rather than counted again as an independent dot term. U_g records only the separately chosen observed-frame identification. Raising Clifford indices also varies: dot γ^a includes inverse-metric variation. It must not be replaced by a rotation of a fixed gamma matrix when the metric changes.

### What is newly explicit

This packages three previously separate changes into one actual receiver derivative:

1. Change of the ambient fields and the F⁻¹ frame map.
2. Displacement of the section, requiring normal derivatives of those ambient fields.
3. Change of its tangent, giving the Z_A ∂_μh^A term.

The optional observed-frame term is kept separately legible. Holding q fixed misses terms2 and3 even if the ambient Euler derivative and δF are correct. No choice of F removes the normal derivatives from this identity. Their presence does not prove on-shell nonautonomy: source-compatible equations/domain restrictions might relate them. That remains a separate burden.

### 1.2. Fermion boundary potential under F/R

Write the first-order fermion density in any fixed local coordinate frame as

    L_F = ρ_g Re[barχ (A^a ∂_aχ + Bχ)],

where A^a is the repaired principal coefficient and B includes the full wave2 Q/Kγ remainder and all connection terms. The bars are independent covector variables. The density may have additional dependence on derivatives of g through the chosen geometric coefficients.

At fixed geometric data, the integration-by-parts boundary potential from variation of χ is

    θ_χ^a(δχ) = ρ_g Re[barχ A^a δχ].

Using χ=F⁻¹χ′, barχ=barχ′R and A′^a=R A^a F⁻¹, its complete pullback under a varying geometric frame is

    θ_χ^a = ρ_g Re[barχ′ A′^a δχ′]
             + ρ_g Re[barχ′ R A^a (δF⁻¹)χ′]
           = ρ_g Re[barχ′ A′^a(δχ′−(δF)F⁻¹χ′)].

The second term vanishes for fixed F, but is generally nonzero for a geometric variation. It is exactly the metric-chain boundary contribution arising when derivatives hit F⁻¹ in the transformed Lagrangian. Merely using the simple block-Dirac kinetic term and omitting that dependence loses it.

There is no separate δR boundary term in this unsymmetrized first-order χ variation, because barχ has no derivative in the original density. δbarχ=δbarχ′R+barχ′δR contributes to the bulk variation. A symmetrized Lagrangian can allocate boundary terms differently and must retain its chosen total divergence. Neither replacing R by F nor replacing the independent bar map with a Hermitian adjoint is licensed.

### Full metric variation: pointwise geometric variables versus base-metric jets

The formula above concerns θ_χ and is exact even when δF contains derivatives of δg. If the original density contains derivatives of g through B, A or other geometric coefficients, its original metric boundary potential θ_g must also be pulled back. If the geometric coefficients used in F/R are treated as independent variables and F/R are algebraic in those variables, a full representative is

    θ′_full = pullback(θ_g) + pullback(θ_χ)

plus any original additional field boundary contributions. This algebraic-variable case does not identify the naive Dirac-only potential with the full potential. The volume density ρ_g is retained throughout, so its variation contributes when forming the presymplectic current.

**Native base-metric qualification.** The native ambient geometry can depend on first jets of the base metric (through the induced horizontal splitting). Accordingly F/R may depend on g and ∂g when expressed in base-metric variables. They are not automatically point transformations in those variables. Substitution of the *bulk Euler terms* then produces further boundary terms when derivatives of δg are integrated by parts. These cannot be omitted from a full metric potential or symplectic comparison.

For an explicit first-jet formula, let the old variation be written with density-valued Euler coefficients in the displayed independent-bar ordering:

    δL = E_g·δg + E_χ·δχ + δbarχ·E_bar + ∂_a θ^a.

Let χ=f=F(g,∂g)⁻¹χ′ and barχ=b=barχ′R(g,∂g). For each metric coordinate g^A define

    C_A^μ = E_χ·∂f/∂(∂_μg^A)
              + [∂b/∂(∂_μg^A)]·E_bar.

The metric-variation chain includes C_A^μ ∂_μδg^A. Integration by parts yields

    C_A^μ ∂_μδg^A = −(∂_μC_A^μ)δg^A
                                  +∂_μ(C_A^μ δg^A).

Thus after putting the transformed variation in Euler form,

    θ′^μ_full = pullback(θ^μ_full) + C_A^μ δg^A

in this first-jet case, up to the chosen exact representatives. Higher-jet dependence produces the corresponding repeated-integration-by-parts Green concomitant. The term with ∂b/∂(∂g) shows why δR, although absent from θ_χ itself, can enter the *full metric boundary potential* through the bar Euler term. Derivatives are taken holding the other jet coordinates independent; no assumption that C vanishes is made.

For two commuting variations the full presymplectic comparison consequently includes δ₁(C_A^μδ₂g^A)−δ₂(C_A^μδ₁g^A). On an actual fermion solution, with tangent variations satisfying both linearized fermion Euler equations, this additional term vanishes. No such solution/tangent space has been constructed here. Therefore the present result is the exact receiver derivative, exact fermion-current pullback, and explicit jet-chain correction formula—not a completed native physical symplectic-equivalence theorem. Boundary conditions, constraints, positivity and domain compatibility remain separate.

### 1.3. Finite Grassmann measure

In wave2's block notation, define upper and lower shears

    U(J/2)=[[I,J/2],[0,I]],    L(C)=[[I,0],[C,I]].

Then F=U(J/2)L(−Γ), while R=U(J/2)L(−Γ/2). Each shear has determinant1; this does not depend on ΓJ=nI or a chosen signature. Therefore detF=detR=1 on every finite fibre.

With independent Grassmann χ and barχ, χ′=Fχ and barχ′=barχR⁻¹ give

    Dχ Dbarχ = (detF/detR) Dχ′ Dbarχ′ = Dχ′ Dbarχ′

for finitely many sites/components and fixed external geometry. This is only the finite-dimensional Berezin change-of-variables identity. A continuum regulator, field domain, global spin/bundle treatment and anomaly analysis remain separate. Nothing here selects a quantum measure or proves continuum equivalence.

### 1.4. Exact controls prepared for root

`tests/program-focus/source_action_engineering_probe.py` uses standard-library rational dual numbers. It has one genuinely nonconstant section g_t(x)=x²+t(x+1), sampled at x=2, with independently varying fields, Clifford matrices related by a varying similarity, and an observed-frame change. Direct differentiation is compared to the full chain-rule formula. Mutations omit section displacement, section slope, Clifford variation or observed-frame variation; each must be detected.

The finite n=2 fixture has an exact Clifford relation, but is deliberately a reduced algebraic control, not the native K95 representation. The derivations above are general dimension/rank identities. Boundary controls use the actual repaired symbol in that reduced Clifford fixture, independent row and field values, and a nonconstant F. They verify fixed-frame and varying-frame current identities, reject omission of the δF term, and check both shear determinants and their Grassmann ratio. No original factorization certificate is rerun, and no bosonic Helmholtz object is sent through fermionic F/R.

The combined exact probe includes these controls. No stationary solution, source-selected action, family count, native trace domain or positivity result is asserted.

## 2. Actual current fingerprints

Status: T2 pointwise candidate algebra; exact controls and independent review are recorded below. Base `a22bdace5a78a3870d9ce76634d545f89b791dab`; directed candidate calculation. This is new algebra on the existing current, not a physical 2+1 identification, a family count, a solution-domain result or a GU exclusion.

### Objects and owned subproblem

Use the actual rank128 complex K95 Clifford module S, horizontal H of dimension4/signature(3,1), normal N of dimension10/signature(6,4), independent barred rows, and the wave2 coefficient family

`D_s = [[C d_A, d_A],[-delta_A, s gamma^a nabla_a]]`.

The repaired candidate has s=−1/2. Source SC-OP-05 admits an SE rival without selecting that coefficient; semisimplicity with the other arrows fixed selects −1/2 only after an additional demand. Varying s below tests source-admitted matrix grammar, not proof that every s is a physically admissible completion.

The source-label calculation in `explorations/conditional-build/krein-order3-observation-label-2026-11-20.md` section3 already owns the injection

`I psi=(10 J_H psi, −4 J_N psi)`, `Gamma_Y I=0`, `Gamma_H q I=40 psi`.

It is the mixed imposter summand of the ambient contraction kernel, **not the whole kernel, the horizontal RS cousin, or HE1's 144**. The independent scalar-spinor nu is also owned. A complete physical pair of true-family embeddings and the physical weak-current quotient are not supplied by those algebraic maps. Consequently the maximal immediately owned test compares **I and nu**, rather than inventing three physical families.

Let the field readout be `q_F(zeta,nu)=(zeta_H,nu)` in the held adapted section frame. Separately define the equation-row **diagnostic** `q_E(r,t)=(r_H,t)`. This is a chosen coordinate contraction on the equation carrier, not an established physical equation-descent map. Its spinor-valued subdiagnostic is

`d_E(r,t)=(Gamma_H r_H/4,t)`.

It measures a horizontal gamma-trace row and a scalar equation row. Neither component is an observed particle count.

### 2.1. Exact connection-current operator

For a connection variation a, differentiating the actual fermion operator gives

`(V_s(a)(zeta,nu))_r,a = gamma^b(a_b zeta_a − a_a zeta_b)+a_a nu`,

`(V_s(a)(zeta,nu))_t = sum_a eta_a a_a zeta_a+s gamma^a a_a nu`.

The current paired with a is `Re(bar_chi V_s(a)chi)` with independent barred row. This displays all four vertex types and introduces no extra current coupling.

The full U(64,64) algebra contains central variations `a_a=i lambda_a Id`. They are Krein-skew for the actual H: `(iId)^dagger H+H(iId)=0`. In this subfamily,

`V_s(i lambda Id)=i sigma_s(lambda)`.

Thus its relation to the already-owned symbol is exact, but we now restrict the **current and row diagnostic** to the owned source injection rather than rerunning the symbol classification.

### 2.2. A concrete two-input interaction fingerprint

Take a real non-null lambda wholly horizontal or wholly normal. Put `c_lambda=gamma^a lambda_a`, so c_lambda is invertible. On inputs `(I psi,nu=phi)`, the output diagnostic has the following two-by-two coefficient matrices multiplying `i c_lambda`:

```
lambda horizontal: M_H(s) = [ -5    1/4 ]
                            [ 10      s ]

lambda normal:     M_N(s) = [-10      0 ]
                            [ -4      s ].
```

Proof uses only `Gamma_H J_H=4`, `Gamma_N J_N=10` and the Clifford identity
`Gamma_H c_lambda J_H = −2 c_lambda` for horizontal lambda, versus `−4 c_lambda` for normal lambda. For the imposter, Gamma_Y I=0, so the one-form current is simply `i c_lambda I`; the scalar row is `10 i c_lambda psi` or `−4 i c_lambda psi`. The nu-only contribution is `(i lambda_a phi, i s c_lambda phi)`.

At the repaired coefficient:

`det M_H(−1/2)=0`, `rank M_H=1`; `det M_N(−1/2)=5`, `rank M_N=2`.

For non-null lambda these become ranks128 and256 respectively on the spinor input pair. This is a pointwise current-routing distinction, not a family count or an evolution statement. Null lambda adds the known Clifford degeneracy and is not included in these rank numbers.

### The missing signal goes into a different row, not away

The horizontal subdiagnostic has kernel `phi=20 psi`. But for this input the **full** horizontal one-form current is

`r_H = 40 i P_H(lambda tensor psi)`,

`P_H(b)=b−J_H Gamma_H b/4`, while `t=0`.

This is horizontal gamma-traceless, generally nonzero, and injective as a map of psi for non-null lambda (evaluate a non-null orthogonal horizontal direction, where both Clifford factors are invertible). Therefore no interaction has disappeared: the response is routed to the horizontal RS-shaped equation row discarded by d_E. We do **not** identify that row with a physical spin-3/2 particle.

For normal lambda, the same input produces `d_E=(-10,−14) i c_lambda psi`, so it is detected even by the smaller diagnostic. This supplies both a positive routing control and a negative control against claiming darkness.

### 2.3. Rescaling invariance and a permitted-grammar countervariation

Independent nonzero rescalings of the two input embeddings and the two diagnostic rows preserve rank. They also preserve the coefficient cross-ratio

`M11 M22/(M12 M21)=−2s` for M_H.

Thus the repaired rank-one relation is not a normalization accident. However

`det M_H(s)=−5(s+1/2)`.

For the printed s=0 candidate the determinant is −5/2 and the same phi=20psi input emits scalar row `10 i c_lambda psi`. Other s values except −1/2 likewise remove the rank loss. This is an explicit breaking deformation within the source-admitted SE grammar; it breaks the added fixed-slice semisimplicity condition. Therefore the relation is **candidate-fixed (and condition-fixed), not demonstrated source-fixed**. It cannot yet be sold as GU's unavoidable coupling prediction. We do not claim this small diagonal-rescaling classification is the complete physical field-equivalence group.

### 2.4. No universally blind normal field under all central current variations

For `chi in ker q_F`, one has zeta_H=0 and nu=0. Choose any normal axis n and the admissible variation `a_n=iId`, all others zero. Then

`(q_E V_s(a)chi)_scalar = i eta_n zeta_n`.

Consequently

`ker q_F intersect (intersection over central normal a of ker(q_E V_s(a))) = {0}`

for **every s**. This proof needs no grading and applies already to the central subset of the full-U variation space. Restricting input further to normal RS cannot create a nonzero universally blind subspace.

Concrete K95 witness: take positive normal axis4 and negative normal axis10, with

`zeta_4=gamma_4 psi`, `zeta_10=−gamma_10 psi`, all other components zero, nu=0.

It is normal gamma-traceless, invisible to q_F, but central a4 produces the nonzero scalar-row current `i gamma_4 psi`; its horizontal row remains zero. An appropriate independent barred scalar row detects the action-current pairing.

The pointwise central probe also admits a non-pure-gauge extension within the held full-U candidate: take `a=i f(x,y) dy^n Id`, with a smooth compact local bump satisfying `f(p)=1` and a nonzero transverse derivative at p. For any held connection A, `d_A a=i df wedge dy^n Id` has nonzero trace `128i df wedge dy^n`. An infinitesimal frame-gauge variation `a=d_A xi` has curvature variation `[F_A,xi]` with trace zero, so cannot equal this extension. Its pointwise current is unchanged. This removes a pure-gauge objection inside the candidate variation class; it does not establish source-physical or on-shell admissibility.

**Meaning:** no nonzero normal one-form field is protected from *all these pointwise current probes* merely by being in the literal field-readout kernel. This is not physical dark-sector leakage: it does not authenticate these probes as on-shell excitations, identify normal RS with dark matter, or establish rates/propagators. A constrained solution space might exclude probes or impose further relations. The result isolates what any such protection would have to add.

### 2.5. Transport is exact but field and equation maps differ

Use wave2's `chi'=F chi` and `D'=R D F^-1`. At s=−1/2 the central current obeys

`R V(i lambda Id) F^-1 = diag(i c_lambda, −i c_lambda)`.

The correct two readouts are **different**:

`q_F'=q_F F^-1`, `q_E'=q_E R^-1` (and `d_E'=d_E R^-1`).

Hence `q_E' V' F chi = q_E V chi`; the diagnostic routing and hidden-input witness are invariant under this exact rewrite when everything is transported. Independent bars transform by `bar_chi'=bar_chi R^-1`, preserving the actual current pairing. Applying q_F F^-1 to equation rows would test a different object. No bosonic Helmholtz witness is transported by these fermionic maps.

### Disposition and next useful calculation

New reusable results are the M_H/M_N current fingerprint, the repaired transfer into the horizontal gamma-traceless row, the explicit SE-grammar breaking variation, and the all-s central-probe hidden-kernel separation theorem. These are more informative than merely listing four vertices, while remaining strictly candidate/diagnostic results.

The generic induced square still yields linked curvature/current terms, but the demonstrated source-grammar sensitivity shows why that generic linkage alone is not a protected GU prediction. The next meaningful extension is to test the **source-typed allowed connection/solution variations** against the central probes, and to supply actual physical sector embeddings before calling this a full 2+1 fingerprint. No source verdict, ledger status or class-C exclusion follows.

Probe: `tests/program-focus/source_action_engineering_probe.py`, Gaussian rational arithmetic on the native128 K95 module. It checks both positive/negative axes, source injection, all diagnostic entries, nonzero remaining RS output, SE0 countervariation, hidden normal RS influence, exact F/R row transport and rescaling identities. Execution and acceptance are recorded in the evidence file.

## 3. Coupled geometry, boundary and analytic scope

Evidence pin: `a22bdace5a78a3870d9ce76634d545f89b791dab`. Candidate-only T2 mathematics, using the explicit K95 geometry and action in `source-action-external-datum-candidate-2026-11-25.md` and its wave2 continuation. K2345 supplies the coordinate metric/fibre connection; W2 supplies the actual K95 spin-curvature normalization. No source selection, whole-class-C coverage, convergence or physical stationary solution is asserted.

### 3.1. The leading geometric functional and the actual metric variable

In zero matter, write `S=Phi F_B` and `h=kappa^-1`. W2 gives

    I_eff[g;h] = h I1[g] + h² I2[g] + O(h³),
    I1[g] = -1/2 <S,S>,
    I2[g] = 1/2 <S,K S>.

Use `b(X,Y)=-Re tr(XY)/128` solely as the declared reporting normalization. Since the actual spin-LC injection gives `S=-Einstein` in the Clifford-vector receiver, and `b(gamma_a,gamma_b)=-G_ab`,

    I1 = 1/2 integral [Ric_AB Ric^AB + (5/2) R²] dmu_G       (dimension 14).

The underlying unnormalized trace convention multiplies this by its fixed nonzero normalization; no physical sign or positivity is inferred. On the flat-base metric bundle, the raised Ricci values are `1/4` on five directions and `-5/4` on nine. Thus

    Ric² = 115/8,  R=-10,
    Einstein² = 5(21/4)² + 9(15/4)² = 2115/8,
    reporting-normalized I1 density = 2115/16.

**Crucial variation restriction:** `g` is a base metric. The ambient horizontal metric is the tautological fibre value `y`, not `g`. The dependence of `G_g` on `g` is through the horizontal lift from `Gamma(g)`. A constant rescaling of a flat base metric leaves its connection and hence this ambient metric unchanged. Varying `G` by an arbitrary 14-dimensional homothety would test a different problem.

At a constant base `g0`, use `H_g dy = dy-C_mu dx^mu`, where

    C_mu = Gamma_mu^T y + y Gamma_mu,
    V_y(U,V)=tr(y^-1 U y^-1 V)-1/2 tr(y^-1 U)tr(y^-1 V).

Then `G_g = y_mu nu dx^mu dx^nu + V_y(dy-C dx,dy-C dx)`. For a base perturbation `p=delta g`,

    delta Gamma^a_mu b = 1/2 g0^ac
       (partial_mu p_cb + partial_b p_cmu - partial_c p_mu b),
    delta C_mu = delta Gamma_mu^T y + y delta Gamma_mu,
    delta G_HH=0, delta G_VV=0,
    delta G_HV(X,W)=-V_y(delta C(X),W),
    delta dmu_G=0.

This incorporates the induced connection and frame dependence geometrically; it does not freeze B or the Hodge pairing. For general variations the explicit first-variation formula is

    delta I1 = 1/2 integral [
      (2 Ric^AB+5R G^AB) delta Ric_AB
      +(-2 Ric^A_C Ric^CB-5R Ric^AB
         +1/2(Ric²+5R²/2)G^AB) delta G_AB ] dmu_G.

`delta Ric` is the full variation, including derivatives of the induced ambient metric. At the flat-base reference, the displayed algebraic coefficient is block diagonal, so its contraction with the mixed `delta G` vanishes. This is not license to discard the derivative/boundary part.

### 3.2. An actual bounded metric-response result: a null first variation

Take a **fixed product regulator** `Omega_x × V_y` inside the chart, with fixed smooth fibre boundary, zero matter and a smooth `p(x)` compactly supported in `Omega`. This is an explicit local diagnostic rather than the original spherical boundary problem.

The density of I1 is a local function of `G_g` and at most two ambient derivatives. Since `G_g` depends on base `g` only through its connection, at constant `g0` its first variation has the form

    delta L1(x,y) = sum_(1<=|alpha|<=3) C_alpha(y) partial_x^alpha p(x).

There is no undifferentiated-p term: every occurrence of `delta Gamma` contains a base derivative of p. All coefficients are independent of x because the reference geometry is translation invariant. Integrating in x first gives

    delta I1[g0](p)=0.

This uses the original local density, so fibre-boundary terms have not been thrown away by integration by parts. They are included in the same coefficient integral. The result is a genuine null test: **the leading effective geometric functional does not reject the constant base metric under these correlated, compact-base-support variations on this product regulator.** It does not prove stationarity on the spherical fixture, for matter perturbations, to higher orders, or in a physical native domain. On a general regulator with x-dependent fibre slices, the integrated coefficients depend on x and the cancellation need not hold.

This also prevents a false kill based on the nonzero ambient Einstein-square density. Nonzero action density and a nonzero unrestricted ambient metric Euler tensor do not by themselves establish a nonzero allowed base-metric variation.

### 3.3. Allowing the geometry to respond with h

For the zero-matter formal branch `g(h)=g0+h g1+...`, the metric equation expands as

    h E1(g0) + h²[DE1(g0)g1+E2(g0)] + ... = 0.

A nonzero E1(g0) could not be repaired by a regular order-h metric change in this zero-matter expansion. Our product-domain calculation instead gives E1(g0)=0 for the stated test class; the all-order follow-through below resolves the formal metric receivers in this same product class; it does not resolve the different spherical boundary problem. If matter is retained, the order-zero fermion functional must be included; its Hessian can contribute at order h. Do not transplant the zero-matter order counting into that case.

### 3.4. A concrete incompatibility with the supplied fixed boundary fixture

The formal branch is

    Ahat(h)=B[g(h)]-h R_cur[g(h),chi(h)]+O(h²).

With boundary data `a_partial(h)=a0+h a1+...`, necessary matching conditions are

    a0 = i^*B[g0],
    a1 = i^*(DB[g0]g1-R_cur[g0,chi0]).

The external fixture fixes `a_partial=U_k^-1 dU_k`, tangentially flat by Maurer-Cartan, independently of h. The issue is stronger than its merely being nonzero: **the flat-base reference B has nonzero tangential curvature on that coordinate-sphere boundary.**

At a horizontal pole of the 14-ball centered at `(x0,y0)`, every vertical direction is tangent to the boundary. The fibre is totally geodesic at the flat-base metric: the coordinate connection has no horizontal component on two vertical arguments. Its connection is

    nabla_U V = -1/2(U y^-1 V + V y^-1 U).

On a positive 2×2 block of the K95 base metric, at y=I on that block,

    R^V(U,V)W = -1/4 [[U,V],W].

Choose traceless symmetric matrices `U=diag(1,-1)` and `V=[[0,1],[1,0]]`. Then

    R^V(U,V)V = -U != 0.

The trace-reversal term does not alter this connection formula. The full Dirac spin representation of the orthogonal Lie algebra is faithful, so its spin-LC curvature is also nonzero on these boundary tangent directions. Consequently `i^*B[g0]` cannot equal or be gauge-equivalent to the tangentially flat fixture. This holds for **every k**, including zero: it is not a generation-count obstruction.

**Scoped conclusion:** no regular formal branch with this fixed flat-base leading geometry, `T=O(h)`, and `g(h)=g0+O(h)` meets the fixed pure-gauge spherical boundary fixture coefficientwise. This sharpens the earlier unspecified boundary-compatibility ceiling with an explicit curvature witness. It does not exclude a solution at h=1 on a nonperturbative branch, a boundary layer, another leading geometry, or a different boundary prescription. A parameter-dependent boundary family matching B at order zero would be a different external datum and must not be presented as retaining the same charged fixture.

### 3.5. Fixed smooth current cannot resolve the shrinking core uniformly

Reuse the off-shell cutoffs `A_epsilon=f(r/epsilon) alpha`, with `alpha=U_k^-1 dU_k`, and hold k, chart and a smooth diagnostic current J fixed. Outside radius `2 epsilon` this equals the same punctured connection `A_star=alpha`. In a fixed positive auxiliary coordinate norm, `|alpha|<=C/r`; the smooth pairing/density coefficients and J are bounded on the chart. Hence

    | integral <J,A_epsilon-A_star> dmu |
       <= C_J integral_0^(2epsilon) r^(13) r^-1 dr
       = C_J (2epsilon)^13/13.

The punctured comparison is integrable for this pairing; it is not an admissible smooth replacement field. By the triangle inequality, the current-pairing difference of two smooth cutoffs with radii at most epsilon is also `O(epsilon^13)`. The unchanged exterior contribution cancels exactly. If J is supported away from the core, the difference is exactly zero once the core is sufficiently small.

This is a fixed-probe estimate, not a uniform estimate over epsilon-dependent or derivative-amplified probes. It does not say different charges have the same response: the construction keeps the same k and the same exterior. Charge remains fixed while this particular resolution of its core is lost. No stationary state, physical invisibility, propagator or particle count follows. No native base-metric scale variation or virial theorem is used.

### 3.6. What an actual truncation certificate would require

No additional formal coefficients are needed. Normalize the connection equation as

    F_h(T)=T+hR+hKT+hN(T,T).

For a truncation T_m already satisfying the prescribed boundary data, take Banach spaces X,Y, with X imposing homogeneous correction boundary conditions, and define

    r=F_h(T_m),  A_m=I+hK+2hN(T_m, .).

If `A_m:X->Y` has a bounded inverse of norm M and `N:X×X->Y` has norm bound C, then the error equation is

    e=-A_m^-1[r+hN(e,e)].

Writing `epsilon=||r||_Y`, the ball `||e||_X<=2M epsilon` is invariant and the map is a contraction when `4|h| M² C epsilon<1`. This yields an actual nearby solution and error bound, with uniqueness within this error ball, under these hypotheses. W2's formal residual order alone supplies none of M, C or a numeric epsilon.

On a compact smooth coordinate domain in 14 dimensions, ordinary positive auxiliary Sobolev estimates can control algebraic products for s>7. They do **not** supply the native inverse: K is first order and the indefinite operator/boundary problem still needs an inverse estimate with the appropriate derivative gain or graph-domain formulation. Boundary mismatch from section4 prevents applying such a certificate to that fixed fixture and this regular branch.

### Control script and acceptance ceiling

`tests/program-focus/source_action_engineering_probe.py` supplies light exact arithmetic controls for the normalized density, mixed metric variation/zero density variation, vertical-curvature witness derived directly from the fibre connection, and formal order matching. The combined probe executes it serially. The product-domain first-variation statement is established by the locality/translation argument above; a polynomial integration control detects an incorrectly retained undifferentiated perturbation but is not a proof substitute. No heavy native curvature or PDE computation is launched.

## 4. All-order formal coupled follow-through

Candidate-only T2 continuation of `compatibility.md`, using the explicit W2 K95 geometry/action at a22bdace. This supplies an actual formal result rather than leaving a redundant order-h² calculation as next work. It does not supply a finite-h solution, physical domain, charged fixture or source-selected action.

### 1. Even powers of h vanish in the zero-matter effective action

Let `theta` be the Clifford grading involution and use the full ordinary spinor trace, not a supertrace. The pairing pairs opposite Clifford parities to zero. W2 establishes

    theta S=-S,
    theta(K U)=-K(theta U),
    theta N(U,V)=-N(theta U,theta V).

The unique formal connection `T(h)=sum_(n>=1) h^n T_n` consequently has `theta T_n=(-1)^n T_n`. This follows by induction from the existing recurrence: K flips parity and every N term contributing to T_n has `1+i+j=n (mod 2)`. Equivalently `T(-h)=theta T(h)`.

In the zero-matter action

    <S,T> + (1/2h)<T,T> + (1/2)<T,K T> + (1/3)<T,N(T,T)>,

every nonzero coefficient has odd h-degree:

- linear: only odd n pairs with S;
- mass: equal input parities require i+j even, making i+j−1 odd;
- quadratic derivative: i+j must be odd;
- cubic: i+j+k must be odd.

Thus `I_eff(-h)=-I_eff(h)` coefficientwise, in particular `<S,K S>=0` and I2 is identically zero. This is not limited to the flat-base diagnostic. It uses the pure spin-LC reference, chosen Phi/parity convention and zero matter; arbitrary matter current need not have the same parity. Boundary expressions obtained from the original density inherit the same algebraic parity, so this does not require silently discarding a Green term.

### 2. The product-domain locality argument extends to every formal coefficient

### Declared variational class

- A fixed product chart regulator `U=Omega_x × V_y`, with relatively compact fixed fibre region V and fixed coordinate domain. Corners can be handled as a product regulator; no native end is asserted.
- Constant base metric g0 of signature(3,1).
- Zero fermions and independent barred fermions.
- The W2 formal connection `Ahat(h)=B[g0]+T[h;g0,0]`.
- Arbitrary smooth base perturbations `p(x)` compactly supported in Omega, correlated over the full fibre V.
- Connection and matter variations compactly supported in U. No external fixed Bott boundary is imposed. Boundary traces of the formal connection are those of this branch.
- A local Krein/spin trivialization chosen as a function of the ambient metric G_g, with no extra g-dependent frame convention. This is an allowed chart choice; at g0 its coefficients are independent of x.

### Locality facts

The ambient horizontal metric is tautological y. The sole dependence of G_g on base g is the horizontal-lift coefficient

    Gamma(g),  C_mu=Gamma_mu^T y+y Gamma_mu.

The Clifford tensors, Phi, Hodge star, density and B are functions of G_g and finitely many of its derivatives. Their first variations at constant g0 therefore contain **at least one base derivative of p**. There is no bare-p term: `delta Gamma(g0)` contains first derivatives of p, while the term from varying g^-1 multiplies `partial g0=0`.

All coefficients at g0 are x-independent. The recurrence uses local differential/algebraic operations only, so each T_n[g0] is x-independent and involves finitely many derivatives. This holds at every finite formal order without an analytic convergence assertion.

### Direct variation of the original action

Hold the formal coordinate coefficients `Ahat(h,y)` fixed while varying g. Do not infer this variation from a bulk envelope identity, because induced connection variations could reach the fibre boundary. Instead vary the original local action density with all its B[g], Phi[g], pairing and density dependence present. At each h-order r it has the form

    [delta_g L]_r = sum_(1<=|alpha|<=m_r)
          C_(r,alpha)(y) partial_x^alpha p(x),

where m_r is finite. Integrating over the fixed product domain gives zero: integrate in x first, using compact support of p. This calculation includes any fibre-boundary contribution that integration by parts might otherwise expose; no boundary term has been discarded. Therefore

    delta_g I[g0,Ahat(h),0,0](p)=0

coefficientwise to **every formal order** for this test class.

Connection variations compactly supported in U vanish by the already-proved all-component formal Euler recurrence. The fermion and barred-fermion equations vanish at zero fields. In dressed coordinates epsilon is redundant; compact two-frame variations reduce to the same solved connection variation.

### Result

**The explicit zero-matter W2 branch is formally coupled stationary on the fixed product regulator under the declared compact-connection/matter and compact-base-metric variation class, with g(h)=g0.** No h-dependent metric correction is required for those receivers. The nonzero formal connection responds to the curved ambient geometry even though the base metric is constant.

This is stronger than solving only the connection while holding g without testing it. It is weaker than a physical solution: a formal series need not converge, the product regulator is not a native boundary/domain, arbitrary boundary variations are not included, and no observed physical sector is constructed. It does not repair the fixed spherical charged fixture: its order-zero tangential-curvature mismatch remains.

### 3. What should no longer be queued

Do not schedule a calculation of I2 or a new constant-base metric receiver at a higher formal order in this same zero-matter/product class: both are now covered structurally. The next substantive bridge for this branch is an analytic realization on a specified compatible domain, or a source-typed observable involving nonzero matter. Changing to the spherical charged fixture changes the boundary problem and encounters the explicit existing mismatch; it is not an innocuous continuation of this product result.

`tests/program-focus/source_action_engineering_probe.py` supplies tiny finite parity/arithmetic controls only. The all-order statements rest on the induction and locality proof above. The exact controls and independent review are recorded in the evidence file.

## 5. Cheap bounded multiplier closure

Keep the geometric coefficients and the original pairing fixed. The existing native printed-residual witness has principal pairings left=-2 and right=-24. Let f(T,x) be any smooth nowhere-zero real scalar function algebraic in the field T, with no T derivatives, and consider f R_print. Linearization gives

    D(f R_print)[v] = f DR_print[v] + (D_T f[v]) R_print.

The second term is order zero in v. Derivatives of f occurring in the formal adjoint also change only lower-order terms. The first-order Helmholtz witness is therefore f(left+right)=-26f, which cannot vanish. No invertible derivative-free scalar multiplier repairs variationality on this unrestricted local field class. This closes the scalar subfamily only: matrix-valued, differential/jet multipliers, changed pairings and constrained solution-set equivalence remain separate. The printed product is our chosen completion; no source contradiction follows. This direct argument reuses the already-certified witness and earns no duplicate probe count.

## 6. Acceptance and retained work

[Evidence](../../lab/process/source-action-engineering-wave.json) records serialized exact controls and independent reviews. [Opportunity inventory](../../lab/process/source-action-opportunity-register-2026-11-25.md) records every proposal, its present scope and revisit condition. [Response work packet](../../lab/process/work-packets/source-action-response-discriminators-2026-11-25.md) holds the evidence-based successor comparison; eligibility and standing priority still come from program_focus.

The all-order formal zero-matter result does not supply a native analytic inverse, convergent stationary metric/matter background, physical conserved positive pairing, full source two-sided law, physical true-family embeddings, or a boundary-to-integer family receiver. These are named dependencies of particular conclusions, not a repository pause. Source, physics-ledger, action-class, canon and paper verdicts are unchanged.
