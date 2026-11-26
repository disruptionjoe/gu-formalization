---
title: Off-section metric response distinguishes the two stationary candidates
status: exploration
doc_type: structural-result
created: '2026-11-25'
program_target: LB-CLASS
tier: T2
expected_delta: Evaluate the complete geometric coefficient in the off-section fourth-order candidate
  metric response.
actual_delta: The complete off-section metric coefficient is evaluated exactly. Across a quantified one-parameter
  fibre/base family, the first stationary background has a sign-changing fourth-order receiver while the
  second stays positive. Full fixed-geometry connection Hessian is explicit; no integrated or physical stability verdict.
class_covered: Fixed W2 K95 full-U action; constant-base invariant stationary backgrounds; coordinate
  Ahat one-form fixed in symmetric spin identification; arbitrary local base-metric amplitudes, with a
  quantified positive-parameter off-section TT family.
premises:
- lab/sources/source-claim-register.yaml#SC-ACT-01
- lab/sources/source-claim-register.yaml#SC-ACT-05
- lab/sources/source-claim-register.yaml#SC-GEO-51
- lab/sources/source-claim-register.yaml#SC-META-52
- lab/sources/source-claim-register.yaml#SC-META-53
- explorations/conditional-build/source-action-physical-dynamics-2026-11-25.md
- lab/process/source-action-deep-coefficients.json
source_bridge:
  status: conditional
  reason: Source motivates the ingredients but has not selected this completion, held-connection tangent,
    physical domain or finite reduction. No source necessity of uniform pointwise metric positivity is
    established.
kill_condition: A contradictory exact control rejects only the coefficient calculation or stated receiver
  property; no class-C/source/GU exclusion.
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# Off-section metric response distinguishes the two stationary candidates

```yaml
program_target: LB-CLASS
tier: T2
expected_delta: Complete the outstanding off-section coefficient and test its sign across a structural parameter family.
actual_delta: First stationary root has a sign-changing receiver; second stays positive in this family. No physical stability verdict.
```

## Result in plain terms

The earlier section calculation gave positive fourth-order metric coefficients at both exact stationary backgrounds. Evaluating the geometry away from the section changes the answer: **one background's coefficient changes sign, while the other's remains positive throughout the tested one-parameter family**. The previously omitted geometric variation is essential, and confusing a jet-density expression with its frequency-polarized quadratic form reverses that contribution.

This completes the outstanding **local fourth-order coefficient** calculation, not the full physical stability calculation. Connection perturbations are still coupled, a base-metric variation samples the fibre through an integral, and no source-selected physical state/reduction is supplied. Both stationary backgrounds still exist.

| State | Precisely what it means here |
|---|---|
| ESTABLISHED | Exact coefficient identity, parameter-family sign distinction and full fixed-geometry connection linearization under the stated assumptions. |
| RULED OUT | Extrapolating the first background's positive section coefficient uniformly across this family. This does not rule out that background physically. |
| NOT MODELED / UNDETERMINED | Interpretive server/client or mind structures are not modeled. Physical stability and effective four-dimensional gravity are undetermined. |

**Grade:** internally reviewed T2 candidate mathematics; rational arithmetic and inherited exact root balls, not a new Lean theorem or T1/source verdict. **Weakest unproved link:** physical state and fibre/domain reduction. **Source necessity:** absent for a demand of pointwise positivity in this particular held-connection tangent. **Class-C representativeness:** not established.

```gu-typed-objects
result: exact off-section metric response
carrier: native K95 metric-fibre geometry and full U connection LAYER=ambient BRIDGE=literal_section_contraction CHIRALITY=N/A
pairing: native real trace/form action pairing and absolute metric density ON=connection_forms
real_structure: K95 full complex spinor module; no imposed physical quaternionic contour
grading: Clifford parity for derivative cancellation; no physical chirality selection
action_owner: repository-construction fixed W2 full-U action with SEminusonehalf
target: fourth-order action coefficient and differential connection Hessian MAP-TYPE=not-a-map
```

> **GU-COMPARATOR-ROUTING — scope before inference.** Read [source-native routing](../../lab/methods/source-native-comparator-routing.md). K95 is not K77. Literal contraction is not a Kaluza–Klein projection; a trace-free metric amplitude is not an established physical graviton. Full U, independent bars and source2+1 remain distinct from a selected physical quotient.

## Exact variation formula

At a fixed ambient point let G vary by h and put H=G^-1 h. Define H^[k] on covariant k-forms by derivation: on a coordinate covector theta^j it gives sum_i H^j_i theta^i. Extend it on the exterior factor only, holding Clifford matrices in the symmetric spin identification fixed.

The varying coframe is L=I+epsilon H/2 at first order. Its induced map on k-forms is I+epsilon H^[k]/2. The actual Phi uses only the Clifford-valued tautological forms, exterior products and Hodge maps. Naturality of every one of these operations gives

    Phi_(G+epsilon h) = L^[1] Phi_G (L^[2])^-1 + O(epsilon²),
    delta Phi = (H^[1] Phi - Phi H^[2])/2.

This is not an imposed physical symmetry: it is the tensor-coordinate identity for the explicit reconstructed glyph as its metric varies. In particular delta gamma_i=gamma_j H^j_i/2. Phi2 must be differentiated as the antisymmetrized Clifford two-form; differentiating gamma_i gamma_j without antisymmetrization at an off-diagonal metric would add a false scalar component.

The independent explicit derivative uses

    delta star(x)=star[(tr H/2)x-H^[k]x],
    delta star^-1(y)=-star^-1[(delta star)(star^-1 y)]

at the appropriate degrees, plus delta Phi1 and delta Phi2. The probe compares its full composition with the naturality identity exactly.

The pairing and density also vary:

    delta rho/rho=tr H/2,
    delta <U,V>_(1)=-<H^[1]U,V>_(1).

H^[1] is self-adjoint for this nondegenerate form pairing. Therefore the ENTIRE missing coefficient variation is

    C_h(T,W)/rho
      = (tr H/2)<T,Phi W>
        -(1/2)<H^[1]T,Phi W>
        -(1/2)<T,Phi H^[2]W>.

No delta Phi, gamma, Hodge, density or pairing term has been frozen. For the native principal metric perturbation h has only horizontal/normal cross blocks, so tr H=0. A separate conformal control h=G has tr H=14 and yields C_h/rho=(11/2)<T,Phi W>, with a required nonzero test receiver.

## Substitution into the complete Q4 density

The previously derived complete fourth-degree density, modulo compact-base divergences, is

    Q4/rho = kappa/2 <b2,b2>
             +1/3 <T0,Phi(b2 wedge b2)>
             -1/6 <b2,Phi(b2 wedge T0+T0 wedge b2)>
             +1/2 C_h1(T0,d_x b2)/rho.

Second B/metric dependence was not discarded: its possible fourth-degree term is linear in d_x(delta²B)_3 and integrates onto x-independent background coefficients. Lower b components in the derivative quadratic expression vanish by Clifford parity. These reductions use the fixed constant-base invariant backgrounds and compact base perturbations.

The probe now evaluates ALL displayed terms off section by the exact new formula.

## Jet density versus Fourier/Hessian symbol

The displayed Q4 is a density in jets, not yet a frequency-polarized bilinear form. In a frozen Fourier symbol, pair frequencies (-xi,+xi). The algebraic b2-b2 terms are unchanged; the h1-(d_x b2)_3 term CHANGES SIGN. Thus

    Q4_Fourier/rho = kappa/2 <b2,b2>
             +1/3 <T0,Phi(b2 wedge b2)>
             -1/6 <b2,Phi(b2 wedge T0+T0 wedge b2)>
             -1/2 C_h1(T0,xi wedge b2)/rho,

when h1 and b2 on the right are evaluated using the real-symbol convention of the earlier probe. The real periodic control is p=cos t: average(p' p''')=-1/2 while average((p'')²)=+1/2. The implementation uses exact rational complex Laurent coefficients, not floating numerical differentiation. Earlier on-section results are unchanged since xi wedge b2 vanishes there.

## A whole off-section family

Fix ambient y=eta=diag(1,1,1,-1), xi=theta3, and take constant base g0=diag(1,1,1,-a), a>0. All these bases have Gamma(g0)=0, hence identical ambient G, B and invariant root T0 at fixed y; only the base-metric variation map and location of observation differ. Write r=1/a>0.

For the TT polarizations p11=1,p22=-1 and p12=p21=1, metric_symbol constructs h1 and b2 exactly. Every coefficient is affine in r because the only varying inverse base coefficient is g0^33=-r. Every Q4 term is quadratic in h1,b2, so its coefficients have degree at most2 in r. Its dependence on T0 is affine (the mass term is constant). Exact values at r=1,2,3 determine this universal polynomial; r=1/2 independently verifies it. The proof of degree, not the extra sample, licenses its universal interpolation.

The exported polynomial coefficients are exact affine functionals of the59 root coordinates. Existing rational contraction balls bound each functional. The probe compares the two TT polarizations as COMPLETE functionals, not merely approximate values at two roots, and reports certified signs at rational r samples.

## Interpretation and remaining debt

The result is a complete off-section pointwise fourth-order receiver family, including the previously missing geometric coefficient. It is stronger than the earlier section evaluation and is not a homogeneous59-Hessian substitution: perturbations are arbitrary base Fourier amplitudes; the59 algebra supplies only the background value.

No source-selected fibre measure/domain is supplied. The base Euler equation integrates responses across the fibre, and freezing a coefficient at y is not that integration. Nor has the connection perturbation been eliminated through a physical solution operator. A positive or negative local TT coefficient is neither a positive graviton nor a physical ghost. If the family changes sign, it demonstrates that extrapolating an on-section sign across the fibre is invalid; if it does not, it still does not establish the integrated sign.

Changing the spin identification or holding moving-coframe components instead of coordinate one-forms induces connection variations which must be included through the coupled Hessian. These alternate tangent directions are not silently identified.

## Exact response-channel simplification

Inspection of every one of the59 affine coefficient functionals, subsequently asserted by the native probe, gives the much simpler identity

    Q_Fourier(r)=A+C(r-1)^2,
    A=1/16+u/12,
    C=1/16+h/3+t/6+4u/3.

Here h,t,u are the three canonical Clifford-vector amplitudes: horizontal4, normal trace1, normal traceless9. These are not assumed to be physical scalar fields. All higher Clifford-grade background coefficients cancel from this receiver. The two TT polarizations have identical affine functionals and their polarized cross term vanishes identically. This is a two-dimensional TT principal-action receiver, not a physical graviton identification.

The previously owned scalar readouts obey mH=h and mN=(t+9u)/10, hence

    C+2A=3/16+mH/3+5mN/3.

This is a literal action-level response correlation, not analogy or a relation fitted to two roots. The older mY,mH,mN aggregate readouts do not alone determine u: mY is redundant and mN merges trace and traceless channels. Thus the new response resolves additional background information.

The computed root coefficients are approximately

    root1: A=0.0465896582961263, C=-0.189253755372792;
    root2: A=0.0798172856349778, C=+0.316109006350162.

Exact interval arithmetic proves A>0 for both and the stated signs of C. Consequently root2 is strictly positive for every r>0. Root1 has exactly two simple positive zeros at 1 +/- sqrt(A/(-C)), approximately 0.503839130921 and 1.496160869079, is positive between them, and negative outside. The native probe produces rational enclosing intervals for both zeros from the certified root balls, preserving correlated affine evaluations when constructing A and C. These are coefficients of the declared unreduced receiver, NOT physical stability classifications.

## Fixed-base fibre interpretation

Varying constant g0 while holding y fixed was a computational convenience, not a change in the equation being tested. Use the explicit congruence C_L(g)=L^T g L with L=diag(1,1,1,a^(-1/2)). It maps the pair

    g0=diag(1,1,1,-a), y=eta

to

    g0'=eta, y'=diag(1,1,1,-r), r=1/a.

The ambient geometry and invariant connection root transform naturally. The same covector becomes xi'=sqrt(r) theta3; its ambient norm remains fixed. Both TT amplitudes lie in unchanged spatial coordinates. Holding the coordinate one-form Ahat fixed transports consistently under this constant map. If one subsequently fixes coordinate xi'=theta3 instead, the quartic symbol changes by the positive factor r^-2, preserving its sign.

Thus root1's sign change occurs along an actual fibre path above one fixed flat base, in the stated transported tangent family. It demonstrates why a positive on-section coefficient cannot be extrapolated over the fibre. A physical conclusion still requires the full coupled constraints, connection response, admitted domain and selected integration/reduction law.

## Certified parameter dependence

Let `r=1/a>0`. Both tested spatial transverse trace-free amplitudes have the same complete quadratic coefficient, per unit native volume:

    Q_j(r) = A_j + B_j (r-1)^2.

The exact affine functionals, coefficient intervals and rational controls are stored in the [machine evidence](../../lab/process/source-action-offsection-metric.json). Decimal values below are display values, not the proof:

| Background | A = section coefficient | B = off-section curvature of the coefficient |
|---|---:|---:|
| First certified root | 0.04658965829612627 | -0.18925375537279215 |
| Second certified root | 0.0798172856349778 | 0.3161090063501617 |

The first coefficient is positive between two simple roots, bracketed by [0.503839130921,0.503839130922] and [1.496160869078,1.496160869079], and negative outside them. In particular it is positive at r=1 and negative at r=1/2 and r=2. The second is strictly positive for every r>0 because both A and B have positive certified lower bounds. This is a quantified polynomial statement, not extrapolation from a sampled graph. The amplitudes are called transverse trace-free only in their algebraic metric sense.

## Full connection block and the actual reduction burden

At fixed geometry the Euler equation is `S + kappa T + K T + N(T,T)=0`, where N is the symmetric polarization of the actual cubic Euler term. Therefore its **full differential** linearization is

    H_AA[a] = kappa a + K a + 2 N(T0,a),
    K = (Phi D_B + D_B^dagger Phi^dagger)/2.

The formal adjoint includes the declared density and boundary class. N is pointwise algebraic. The homogeneous engine evaluates this operator only on invariant fields; its59-dimensional Jacobian is not H_AA on arbitrary fields. Both backgrounds share the principal connection symbol, but differ in its zero-order part.

Formally eliminating connection perturbations would require a defined inverse and compatible domains in

    H_effective = H_gg - H_gA H_AA^(-1) H_Ag.

Neither kappa=1 nor an invertible stationary59 Jacobian proves that inverse exists. The mixed third-order block is already nonzero. The full lower mixed/geometry blocks, boundary/constraint conditions and fibre integration have not been evaluated here; no effective metric spectrum follows from the pointwise Q4 sign. In particular p is a base field depending only on x: it cannot independently be localized to a negative-contribution region in y. A pointwise negative receiver therefore does not by itself construct a negative admissible integrated direction.

For a regulator/domain Omega, even the leading base response requires the appropriate coefficient integral over Omega, with variation of any g-dependent weight or boundary included. A smooth finite cutoff is an additional datum, not a source-selected reduction. The [natural-density theorem](natural-density-fibre-volume-2026-11-25.md) excludes finite total mass only in its smooth positive (g,y)-natural full-fibre category. It does not identify Newton's constant with fibre volume or prove every weighted action coefficient divergent. The [source routing contract](../../lab/methods/source-native-comparator-routing.md) explicitly prevents importing ordinary KK averaging as the native observation law.

## Scope audit of the proposed slice-completeness investigation

This is read-only assessment of a proposed successor, not execution of its new observability or memory calculation.

- Existing analytic non-autonomy already quantifies a structural symbol class and preserved analytic subbundles with freely admitted normal jets. Positive normal directions suffice; indefinite signature is not the cause. A noncharacteristic full Cauchy hypersurface must not be confused with the codimension10 observation section.
- The sharp `s<=4`, `4<s<9/2`, and `s>=9/2` results belong to the [frozen solution benchmark](solution-observation-trace-2026-11-25.md). The actual curved candidate's analytic existence/non-autonomy theorem does not transfer those Sobolev estimates or furnish a fixed Sobolev evolution semigroup.
- `ker(q)` describes instantaneous hidden data. Dynamically unobservable data vanish under the whole observed evolution; these are different. The existing hidden examples later become visible.
- 216->122->59 describes symmetry-fixed stationary background subfamilies, not a quotient by proved gauge redundancy and not59 dynamical state variables. The emergent quaternionic anti-isometry has the stated SO* real form; it is not an automatic bridge to earlier differently paired Sp constructions.
- A Mori–Zwanzig calculation needs an actual evolution/domain and a projection or lift. The rectangular section contraction is not an idempotent projection; hidden initial forcing remains alongside memory. Neither memory decay nor a Markov limit follows from SC-CHI-52's qualitative low-curvature statement. See [semigroup-based Mori analysis](https://arxiv.org/abs/2503.20457).
- Infinite natural volume is not an entropy calculation. Exact finite jets are not finite-precision samples. AdS/CFT boundary completeness and this thin-section initial-data question use different data; an opposite-duality conclusion is not established.

Source SC-META-52 supplies an unresolved boundary-value posture; SC-META-53 leaves physical positivity unresolved. SC-GEO-52 supplies observation geometry and disavows default KK identification. They do not presently supply the missing complete physical evolution/projection tuple. This identifies missing data, not its impossibility.

## Verification and continuation

The new exact probe differentiates the native nested Hodge/Clifford expression independently of the tensor-naturality shortcut, verifies a nonzero conformal density receiver and the Fourier-sign control, reconstructs the universal quadratic from its proved degree, and checks a fourth rational parameter. Existing stationary-root contraction certificates are reused without claiming a new existence proof. Independent mathematical and hostile scope reviewers checked the formula, interpolation, sign convention and coupled-operator boundary.

The completed coefficient is consumed in the existing directed packet. A finite physical reduction and coupled stability calculation remain separate work. The proposed slice-completeness wave is returned for Joe's requested plan review; it creates no new governance, schedule or stop rule. Source/physics/class-C/canon/paper verdicts and scientific matrix cells are unchanged.
