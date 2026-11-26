---
status: exploration
doc_type: structural-result
created: '2026-11-25'
program_target: LB-CLASS
tier: T2
expected_delta: Determine intrinsic perturbation constraints and source-typed responses on the two normalized candidate backgrounds.
actual_delta: No intrinsic local additive matter gauge freedom; preserved algebraic sectors cannot repair finite local observation closure; nonzero derivative-free Hermitian conserved local energy on unrestricted fields is necessarily indefinite. Native mixed metric symbols and distinct stationary spinless/observed responses are exact.
class_covered: Fixed W2 K95 candidate at its two certified local zero-matter kappa1 backgrounds; analytic full rolled fields and explicitly quantified algebraic restriction classes. Principal lemmas apply to the stated symbol class, not every source completion or class C.
premises:
- lab/sources/source-claim-register.yaml#SC-ACT-01
- lab/sources/source-claim-register.yaml#SC-ACT-05
- lab/sources/source-claim-register.yaml#SC-OP-04
- lab/sources/source-claim-register.yaml#SC-CHI-51
- lab/sources/source-claim-register.yaml#SC-CHI-52
- lab/sources/source-claim-register.yaml#SC-CHI-53
- lab/sources/source-claim-register.yaml#SC-MAS-03
- lab/sources/source-claim-register.yaml#SC-COS-54
- explorations/conditional-build/source-action-dynamics-and-continuation-2026-11-25.md
source_bridge:
  status: conditional
  reason: Source ingredients motivate the candidate, but its completion, physical domain, contour, constraints and observed quotient are not source-selected. Source asserts effective separation, not a unique stationary amplitude at fixed scalar curvature.
kill_condition: Conditional local restrictions can be ruled out only under their named premises; no source, class-C, physics-ledger or GU verdict follows. Missing physical selection is not nonexistence.
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
title: What the constructed action supplies before physical reduction
---

# What the constructed action supplies before physical reduction

```yaml
program_target: LB-CLASS
tier: T2
expected_delta: Actual perturbation constraints and source-typed response.
actual_delta: Intrinsic linearized constraint and algebraic-filter limits, mixed native metric symbols and certified same-geometry response distinction; no physical/source verdict.
```

## Main result

The two exact normalized stationary backgrounds now have distinct, certified **literal instantaneous fermion responses at the same geometry**, including opposite signs in the canonical Clifford-vector scalar amplitude. Curvature and the action normalization alone do not choose between these stationary responses.

The action's own linearized equations do not remove the observation ambiguity found previously. At these zero-matter backgrounds they supply no linear primary matter constraint or finite-order additive matter gauge symmetry. Moreover, restricting the full rolled field to any preserved analytic pointwise subbundle still cannot supply a nonzero autonomous observation from finitely many local initial jets, when arbitrary subbundle-valued normal data remain admitted. A derivative-free positive local conserved energy is likewise impossible on unrestricted normal jets.

These statements identify precisely why an actual physical state or boundary law matters. They do not say that such a law cannot exist. Source SC-META-52/53 explicitly leave the ultrahyperbolic/positive-space problems open; their source meaning is not replaced by ordinary Cauchy or Yang-Mills assumptions.

A substantive gravity calculation also changes the next calculation: the apparent fifth-order pure-metric block cancels identically by Clifford parity, but an exact mixed metric–connection third-order receiver survives. The complete fourth-order expression is now derived, and its section coefficients are exactly evaluated on two transverse trace-free directions. The off-section coefficient variation, fibre-integrated block and a physical graviton spectrum remain open.

**Grade:** internally reviewed candidate mathematics, with exact arithmetic and written proofs distinguished below. No Lean certificate, source verdict, physical mass, positive state space, class-C membership, stability, canon or paper promotion. **Weakest physical link:** source selection of the action and admitted state/observation law. **Source necessity of the tested restrictions:** unproved. Broad mathematical coverage does not supply that bridge.

```gu-typed-objects
result: actual candidate perturbations and source-typed response
carrier: full one-form-plus-scalar Dirac module, rank1920 complex, independent dual rows LAYER=ambient+observed BRIDGE=literal_section_contraction CHIRALITY=S-FULL-DIRAC
pairing: actual real trace/Krein-form action pairing; independent-row Green flux ON=full_Dirac_field_module
real_structure: K95 full complex module; no imposed Majorana/quaternionic physical contour

grading: Clifford parity for symbols; no physical family grading

action_owner: repository-construction fixed W2 full-U action with SEminusonehalf

target: actual Euler linearization and literal observed field response MAP-TYPE=contraction
```

> **GU-COMPARATOR-ROUTING — scope before inference.** Read [source-native routing](../../lab/methods/source-native-comparator-routing.md). FullU, independent bars, non-Levi-Civita displacement, source2+1 and literal contraction are retained. K77 is not K95. An algebraic spinless channel is not a physical Higgs, a current is not a positive norm, and frame covariance is not an active gauge quotient at fixed reference data.

## 1. Actual quadratic equations and the available gauge freedom

Write the existing action as

    S[b,chi,bar_chi] = S_B[b] + Re integral rho_b bar_chi D_b chi.

Here b denotes all bosonic variables. At either stationary point `(b0,0,0)`, its quadratic coefficient is exactly

    S^(2) = (1/2) Hess(S_B)[u,u] + Re integral rho0 beta D0 psi.

Variation of the density, operator, Clifford identification or observation multiplies zero background matter: these changes first enter the matter action at cubic order. Thus bosonic and matter perturbations decouple at linear order. The equations are the bosonic Hessian system, `D0 psi=0`, and the independent density-dual equation. In particular no bosonic constraint has a term linear in matter here. This does not dismiss the bosonic constraint problem or prove all linearized solutions extend globally/nonlinearly on a physical contour.

The owned factorization on `E=(T*Y tensor S) direct-sum S` is

    R sigma(D0)(xi) F^-1 = diag(c_xi,-c_xi).

It makes a non-null base-time coefficient invertible. Analytic full-hypersurface matter data are arbitrary by local Cauchy–Kowalevski existence; this is not Sobolev well-posedness or physical admission. The actual curved lower terms are retained.

**Local gauge-identity lemma.** If a finite-order local differential operator `P` with arbitrary-function parameters obeys `D0 P=0`, its leading polynomial symbol vanishes wherever `sigma(D0)` is invertible. That is a nonempty open covector set, so the symbol vanishes identically. Induction down the order proves `P=0`. The same argument rules out differential identities on the left and applies to the dual block. Bosonic components cannot cancel this in a block-diagonal quadratic Euler system. The established frame/diffeomorphism actions on matter vanish at zero matter. Equation-constrained parameters, nonlocal maps, global symmetries and boundary laws are not covered.

**An exact fixed-reference gauge check.** Set matter and T to zero. Transform only `Ahat=B` to `B+i dphi Id`, holding B and all geometric/Clifford data fixed. Then `D_B T=0`, `T wedge T=0` and `<T,Phi F_B>=0` because the native source is Clifford-odd. The complete action change is

    Delta S = (kappa/2) integral G^-1(dphi,dphi) dmu.

It is not identically zero on compact phi: a compact envelope with rapid oscillations along a positive cotangent direction has a positive leading frequency-squared term. Therefore even active centralU1 at fixed reference is not this action's gauge symmetry. Simultaneous reference-frame covariance also transforms B and is a different operation. The independent dressing-frame redundancy leaves Ahat unchanged. Neither supplies an assumed Yang-Mills quotient of Ahat perturbations.

## 2. Conserved flux is not yet an observed positive state space

Let `D0=A^I partial_I+C` and absorb density into the independent row `eta=rho0 beta`. The exact formal dual and Green identity are

    D0^t eta = -partial_I(eta A^I)+eta C,
    eta D0 psi-(D0^t eta)psi = partial_I(eta A^I psi).

Hence `j^I=Re(eta A^I psi)` is conserved for paired solutions. With commuting classical variation convention the bilinear flux is

    omega^I = Re rho0 (beta1 A^I psi2-beta2 A^I psi1).

Grassmann variations require the corresponding graded signs. No identification of independent rows with Hermitian conjugates is inferred. Field/equation transformations use different maps F and R and carry the dual/readout with them.

Ambient conservation gives `partial_mu j^mu|section = -partial_a j^a|section`. The tangential current need not factor through the literal field and dual readouts; a tube integral retains lateral flux. This is not automatically a closed four-dimensional conserved current. Covariant phase-space methods provide a relevant framework, but their hyperbolizability and global hypotheses are additional premises here: [Khavkine, 2014](https://arxiv.org/abs/1402.1282).

**Local energy classification.** Choose base time and a negative normal covector. Native transport satisfies `M=-A_t^-1 A_n` and `M^2=-c Id`, c>0. A derivative-free Hermitian conserved energy for arbitrary local solution jets requires `H M=M^dagger H`. Then

    M^dagger H M = -c H.

Positive H is impossible. If H is nondegenerate, congruence preserves inertia while the right side reverses it: its signature is necessarily `(960,960)` on the full1920-complex carrier. Variable H does not avoid the principal condition. This reuses the already-known imaginary normal characteristics and adds the local-H/neutral-inertia classification; it is not a newly discovered ultrahyperbolic pathology or a GU-unitarity verdict. Restricted/nonlocal domains and a different physical reduction remain possible.

## 3. Preserved algebraic restrictions cannot repair finite local observation closure

Consider an **analytic** finite-rank subbundle E of the full rolled carrier on an analytic patch, with all three premises:

1. Every analytic E-valued full-hypersurface initial datum is admitted.
2. Actual D0 evolution preserves E.
3. A deterministic section theory reproduces literal `q_F psi=(zeta_H,nu)|section` from a finite local differential encoding of initial fields, with the same fixed external inputs.

Arbitrary first normal jets force `M_a E subset E`. A non-null normal coefficient is invertible, so finite dimensionality gives `M_a E=E`. If `q_F E` is nonzero at a point, choose v in E with nonzero q_F v. For any finite encoding choose N larger than its maximum total time-plus-normal derivative order. Take an analytic local E-section e with value `M_a^-N v` and Cauchy data `z_a^N e`.

Analytic existence and premise2 give an actual solution staying in E. All encoded initial section fields, and all their base-spatial derivatives, agree with zero. At order N, only N principal normal differentiations survive; coefficient, frame and readout derivatives multiply vanished lower jets. Consequently

    partial_t^N(q_F psi) = N! q_F v != 0.

Thus the premises require `q_F E=0`. This covers analytic moving projectors and constant-rank algebraic constraints, with or without symmetry equivariance. Arbitrary smooth projectors are not included merely by invoking the analytic existence theorem. The argument can use a positive normal direction with `M_a^2=+Id`; it does not rely on the energy obstruction above. It applies at both normalized endpoints without transferring small-h spinor holonomy.

**What survives:** genuine differential restrictions can forbid the freely chosen normal jets. A supplied law `R_a psi=(partial_a-L_a)psi=0` must pass propagation and integrability (`[D0,R_a]` and `[R_a,R_b]` close modulo constraints), literal descent, dual/current compatibility and actual boundary/domain tests. Nonlocal or history-dependent state selection also survives. No such law is selected by inventing L_a here. Moving observation contributes `(delta q)chi0=0` and does not alter the linearized result.

For a proposed local contour `eta=psi^dagger W`, a sufficient compatibility identity in this convention is `A^{I dagger}W=W A^I` and `partial_I(W A^I)=W C+C^dagger W`. Positive time flux is an additional condition; unrestricted positive flux is ruled out above. The independent-row exact solutions do not by themselves refute a restricted physical contour.

## 4. Coupled metric–connection symbols: cancellation and surviving coupling

In one declared spin-bundle identification use `p=delta g`, `a=delta Ahat`, `b=delta B[g]`, so `delta T=a-b`. The base field g depends only on x. Its connection variation b has leading base differential order2; density, Clifford and Phi changes have order1. Let `P=Phi D_B`, `K=(P+P^dagger)/2`, `L=(P-P^dagger)/2`.

The highest derivative quadratic terms combine exactly, after integration by parts, to

    Q_deriv = (1/2)<a,K a> + <a,L b> - (1/2)<b,K b>.

This follows by expanding `<a-b,P b>+(1/2)<a-b,P(a-b)>`. With real formal covector symbols, `A_xi=Phi(xi wedge .)`, the symbols are `(A_xi-A_xi^t)/2` for K and `(A_xi+A_xi^t)/2` for L. The derivative-adjoint minus sign is essential.

b is Clifford-even (degree2), and K reverses parity. The trace pairing therefore makes **every** cross-amplitude fifth-order pure-metric receiver zero. This is not the tautology that a skew matrix has zero diagonal quadratic form. The statement is algebraic for arbitrary ambient covectors; actual metric perturbation frequencies are horizontal/base covectors only.

For reproducibility, at y=eta and diagonal constant g0 the probe uses

    delta Gamma^r_(mu j)=(xi_mu p_rj+xi_j p_rmu-xi_r p_muj)/(2 g0_rr),
    C_mu=y delta Gamma_mu+delta Gamma_mu^T y,
    h_(mu A)=-V_y(C_mu,U_A),
    b_(i;ac)=(xi_c h_ia-xi_a h_ic)/(4 d_a d_c).

V is the native lambda1/2 trace-reversed form, U_A=-2eta A, and d is the exact rational Gram matrix. On the section y=g0, `C_mu=xi_mu p`, so `b=xi u` and `xi wedge b=0`. Off-section the latter need not vanish. Nevertheless the mixed action symbol includes the transpose term and survives: for xi=theta0, the probe obtains

    b=-(1/8) theta0 gamma0 gamma8,
    a=theta8 gamma0,
    <a,sigma(L)b>=1/8.

The erroneous formal-adjoint sign gives -1/8. This is a native full-field receiver, not a59-variable stationary Hessian or a physical graviton amplitude.

### Complete fourth-order expression and exact section receivers

Hold Ahat as a **coordinate one-form in the declared symmetric spin identification**. Do not hold its components fixed in a varying orthonormal cotangent coframe: that different prescription induces an order1 connection variation whose mixed term contributes at order4. The baseline orthogonal coframe only reports our tangent components.

Write b2 for the order2 part of delta B and h1 for the order1 part of delta G. The complete quadratic degree4 expression, modulo compact base divergences on these x-translation-invariant backgrounds, is

    Q4 = rho[(kappa/2)<b2,b2>
             +(1/3)<T0,Phi(b2 wedge b2)>
             -(1/6)<b2,Phi Q_T0 b2>]
         +(1/2) C_h1(T0,d_x b2),
    Q_T0 b2 = b2 wedge T0+T0 wedge b2.

Here C_h is the first variation of the ENTIRE density `rho<U,Phi V>`, including density, form/trace pairing, Clifford and Hodge/Phi changes, with U,V held fixed. It remains an unevaluated Frechet derivative off section, not an omitted term.

To derive this, source and kinetic expansions cancel their opposite `<T0,Phi(b wedge b)>` contributions. The cubic leaves coefficients1/3 and-1/6 above. The derivative term is `-<b,Phi D_B b>/2`; even/odd trace parity kills it, including b2/b1 cross terms. Only the geometric coefficient variation of the first-variation derivative term `<T0,Phi D_B b>/2` reaches degree4. Second variation delta²B has total base degree at most3; its nominal degree4 derivative contribution integrates onto x-independent background coefficients and vanishes. Other second coefficient variations have degree at most2. These are constant-base, compact-variation statements, not identities for arbitrary curved base backgrounds.

On the observation section, b2=xi*u implies `b2 wedge b2=0` and `d_x b2=xi wedge b2=0`. Thus the COMPLETE section coefficient per unit native volume is

    Q4_section/rho = (kappa/2)<b2,b2>-(1/6)<b2,Phi Q_T0 b2>.

For timelike xi=theta3, evaluate the two base-transverse trace-free amplitudes `p11=1,p22=-1` and `p12=p21=1`. They have exactly equal affine functionals of T; their polarized cross coefficient vanishes identically. At the two certified roots:

| Section fourth-order coefficient | Root1 | Root2 |
|---|---:|---:|
| Either declared trace-free direction | 0.0465896582961263 | 0.0798172856349778 |
| Rational interval error | <=1.756e-17 | <=1.514e-17 |

Both intervals are strictly positive. Dropping the background/cubic term would instead give1/16 in both cases; the probe detects that error and an incorrect cubic factor. This is exact in the root amplitude, not an expansion around small inverse-kappa.

**Scope:** these are pointwise section action-density coefficients in the declared field-space tangent, not a physical energy, invariant metric-only Hessian, fibre-integrated metric equation or two physical graviton polarizations. g(x) varies over the whole fibre action; section evaluation is not its integral. Under a different metric-dependent spin identification, the adapter `D_A(U^-1 delta U)` must also enter a. The full stationary Hessian transports tensorially, while a chart's metric-only tangent subspace can change.

**Remaining calculation:** evaluate C_h off section and the complete lower mixed/metric terms and bosonic Noether complex, with a specified fibre/domain reduction. Eliminating a requires a genuine solution operator/common domain, not the59 Jacobian. No Einstein limit, physical ghost or stability claim follows.

## 5. Same curvature, different stationary spinless and observed responses

For `T=theta^a T_a`, define the canonical Clifford-vector trace amplitude

    mY=Re tr(gamma^a T_a)/(128*14).

Separate horizontal and normal contractions divided by4 and10 define mH,mN, with `14 mY=4 mH+10 mN`. mY is the coefficient of the canonical Phi1 component; it is not asserted to exhaust every scalar/pseudoscalar invariant or identify a physical mass field. The horizontal/normal split is transported with observation.

Both roots have kappa1, the same geometry, ambient scalar R_Y=-10 and flat base. Each receiver is a linear functional l of the59 coordinates. The existing rational certificate radius r therefore supplies the exact bound `|l(x)-l(x0)| <= r sum |l_i|`. Both root certificates are recomputed by the probe.

| Receiver | Root1 | Root2 |
|---|---:|---:|
| mY | -0.121372952572076 | +0.118800130071750 |
| mH | +0.001112648337090 | -0.033129822358104 |
| mN | -0.170367192935742 | +0.179572111043691 |

These displayed decimals are rounded; the exact rational intervals in the evidence have errors at most2.107e-16 and1.817e-16 respectively. All three interval pairs are disjoint.

This distinction also reaches actual instantaneous **field** response. For scalar-spinor input `(0,nu)`, the connection coupling is `V_T(0,nu)=(T_a nu,-slash(T)nu/2)`. Compute

    q_F[-sigma(dt)^-1 V_T](0,nu),

in that order. The equation-row map is not used as a field readout. The probe transports through the actual F/R inverse and checks its full native inverse before observation. With dt=-theta3, the gamma3 coefficient of the observed nu time-response lies near

    root1: +1.701446632683238, error <=2.528e-15,
    root2: -1.729461465720704, error <=2.180e-15.

A nonzero Clifford coefficient proves some common scalar-spinor input has different instantaneous observed response. This is not a rate, particle mass, physical allowed state or autonomous observed equation. Other lower terms cancel in the comparison because geometry and input frame are identical.

**Source meaning:** stationary response is not determined by geometry alone in this completion. SC-MAS-03 asserts shared-field service, not uniqueness. SC-CHI-52's improved-Einstein scalar has not been identified with R_X or R_Y. The explicit R(y)/4 in SC-MAS-01/SC-CHI-02 is a stylized toy. SC-COS-54 leaves the curvature-side field unselected. Thus the result makes branch/state selection an explicit burden without refuting the source's curvature-driven mechanism.

A genuine geometric susceptibility also varies S,K,N, Clifford tensors, density and observation and satisfies the coupled metric equation. `-J_T^-1 delta S` alone is only a forcing response and is not substituted for that calculation.

## 6. Evidence, verification and the remaining frontier

- [Exact response probe](../../tests/program-focus/source_action_physical_probe.py): recomputed rational root certificates, interval receivers, actual principal inverse, active-center controls, Green/Hessian/energy fixtures.
- [Exact metric-symbol probe](../../tests/program-focus/source_action_metric_symbol_probe.py): actual Phi and pairing adjoints, full ten-amplitude metric samples, cross-amplitude parity checks, section/off-section and non-tautological frame controls.
- [Machine evidence](../../lab/process/source-action-physical-dynamics.json) records exact values and validation scope. Finite tests support the written universal arguments; they do not replace them.
- [Independent internal reviews](../../lab/process/hostile-reviews/2026-11-25-source-action-physical-review.md) challenge source meaning, operator transport, analytic subbundle scope and differential-order completeness.

The completed work removes automatic local gauge/algebraic-filter/positive-energy interpretations of these unrestricted fields and distinguishes their actual stationary responses. Surviving physical mechanisms must restrict solution jets, change the supplied state information, or supply an explicitly compatible boundary/nonlocal law. Gravity still needs the off-section coefficient derivative, fibre integration and actual coupled reduction; curvature response still needs a selected branch and geometric susceptibility. Existing source2+1 family embeddings and physical normalization remain separate burdens. No result here promotes a ledger row or pauses unrelated authorized research.
