---
title: Wedge reduction has an Einstein term and a conditional scalar instability
status: exploration
doc_type: structural-result
created: '2026-11-27'
program_target: LB-CLASS
tier: T1
expected_delta: Derive the native leading Einstein response and classify finite covariant reduction coefficients before testing full metric stability
actual_delta: Conditional Einstein coefficient, complete positive moment cone, fixed-regulator gauge criterion and a full-row growing scalar mode in the leading local four-dimensional model
class_covered: Leading inverse-kappa own-wedge functional on the source-guided native K95 connection metric; finite positive Lorentz-invariant vertical measures depending only on g; constant moments and ordinary real local four-dimensional metric states
premises:
- Reuse the owned BH1-BH3 curvature formulas and normalized first-wedge-action leading functional
- Conformal-support reduction is a declared GU* conditional class, not source-selected observation or a derived physical action
- The scalar stability theorem uses the leading local four-dimensional truncation, constant coefficients and compact interior metric variations
- Fixed external regulator and metric-moving covariant measure have different variation laws
source_bridge:
  status: conditional
  reason: Source supplies primitive geometry and action grammar; the wedge member, physical reduction, reference measure and state space remain unselected
kill_condition: Invalid geometry transfer, measure normalization, metric variation or mode admission withdraws the affected implication; no source-wide exclusion
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
matrix_or_ledger_effect: scoped evidence only; no verdict change
---

# Wedge reduction: an Einstein term, a free moment, and a scalar stability test

program_target: LB-CLASS
tier: T1
expected_delta: Resolve the leading Einstein coefficient and adversarially test the resulting reduction class.
actual_delta: Conditional leading Einstein response and scalar instability; full ambient gravity remains incomplete.

**Internal result; acceptance lives in the independent review receipt.** Basis `cc38ad2c1260d5a0a20379ca2462afe2bb23a52c`. Final wedge wave3 of Joe27r's three-wave investigation, incorporating Joe27w.

**ESTABLISHED:** the actual connection metric gives a nonzero Einstein cross-term. A finite positive Lorentz-covariant reference depending only on the base metric is supported on its conformal ray. Its leading local action depends on three moments, which obey a complete cone constraint. That entire declared local class admits a growing scalar-curvature mode on its de Sitter solution.

**RULED OUT:** stability of those de Sitter backgrounds against ordinary real local metric perturbations in this leading, constant-moment four-dimensional model. Generic fixed external inverse-metric moments also fail the full linearized Einstein gauge test.

**NOT MODELED / UNDETERMINED:** a source-selected physical reduction, measured Newton scale, higher-order curved elimination, the full fourteen-dimensional stability problem, physical state quotient, kappa1 and a wedge-specific PT completion. No source GU or whole repaired-family falsification follows.

```gu-typed-objects
result: conditional Einstein reduction and full-row scalar instability
carrier: source-guided connection metric on native Y14 and a separately declared reduced Lorentz metric on X4 LAYER=observed CHIRALITY=N/A
pairing: nondegenerate native K95 metric contractions; ordinary real four-dimensional metric variations ON=bosonic_metric
real_structure: real Lorentz metric, primary-minus ambient adjoint; no W2 antilinear structure transferred
grading: derivative order and exterior/Clifford grade; not physical chirality
action_owner: repository-construction -- normalized own-wedge first action and explicitly conditional leading reduced action
target: Einstein coefficient, regulator gauge test and scalar stability MAP-TYPE=intertwiner
```

**Source custody.** Draft pp17–22 eq3.7–3.17 supplies the geometric ingredients; the precise connection-metric reconstruction is declared in [source-chimeric-trace-compatibility](source-chimeric-trace-compatibility-2026-11-13.md) §1. Draft p44 eq9.4, pp44–45 eq9.7–9.10 and p57 eq12.4 supply the first-action grammar. See [own-wedge dynamics](wedge-shiab-dynamics-2026-11-27.md) and [actual BH curvature formulas](ricci-flat-ambient-source-jets-2026-11-27.md) §2. This is GU*, with the corrected own-action endpoint; no realization is source-selected. K77 is not substituted for K95. The quoted ratio is **R_G² coefficient / Ric_G² coefficient = 5/2**, not its reciprocal.

## 1. Fixed owners and the geometric calculation

The operative metric is the source-guided reconstruction, not a product Kaluza–Klein metric:

    theta_g=dy-C(Gamma_g)y dx,
    G_g=y(dx,dx)+K_y(theta_g,theta_g),
    K_y(U,V)=tr(y^-1 U y^-1 V)-(1/2)tr(y^-1U)tr(y^-1V).

Source custody and the reconstruction ceiling are in `source-chimeric-trace-compatibility-2026-11-13.md` §1. The horizontal coefficient is the independent fibre metric y. The primitive g lives on X; its induced ambient dependence and its fibre-integrated variational row must be retained.

Use the full Ricci formulas BH1–BH3 from `ricci-flat-ambient-source-jets-2026-11-27.md` §2. With Riemann convention as there,

    Omega_y(X,Y)=R_g(X,Y)^T y+yR_g(X,Y),
    g_y(A_U X,Y)=-(1/2)K_y(Omega_y(X,Y),U),

    Ric_G(H_X,H_Y)=Ric_g(X,Y)+(1/4)y(X,Y)
      -(1/2)sum y^ij K_y(Omega_y(X,e_i),Omega_y(Y,e_j)),
    Ric_G(U,V)=Ric_flat,y(U,V)-trace_H(A_U A_V),
    Ric_G(H_X,U)=(1/2)K_y(sum y^ij(nabla_i Omega_y)(e_j,X),U).

Here g_y is the horizontal pairing y; no replacement by observation g is intended in the A definition. Native flat ambient Ricci has eigenvalues1/4 on horizontal4 plus vertical trace1, and-5/4 on vertical traceless9. Thus R_flat=-10 and Ric_flat²=115/8.

The owned normalized own-wedge action gives, with h=1/kappa,

    L_eff=(h/2)F_G+O(h³),
    F_G=Ric_G²+(5/2)R_G².                                 (1)

The coefficient ratio is R_G²/Ric_G²=5/2. This is analytic on the owned invariant branch and only formal inverse-kappa elimination on general curved g. Nothing below promotes it to convergent curved dynamics or kappa1.

### Two-base-derivative term at arbitrary y

Put r_y=y^mu nu Ric_g,mu nu. Omega and A have base derivative order2. The mixed Ricci term has order3 and no flat mixed component with which to make a linear scalar cross-term. BH1–BH3 imply

    R_G=-10+r_y+O_base(4),
    Ric_G²=115/8+(1/2)r_y+O_base(4),
    F_G=2115/8-(99/2)r_y+O_base(4).                       (2)

The O_base counting is distinct from the h expansion. It includes curvature-squared and derivative-curvature contributions; it is not a statement that they vanish. The leading two-derivative term is exactly

    -(99h/4)y^mu nu Ric_g,mu nu.

### Exact restriction to every conformal fibre point

For y=a g, a>0, metric compatibility gives Omega=0. Covariant derivatives of R_g are also g-skew, so the BH3 block vanishes. Therefore, without requiring Ricci-flat or constant-curvature g,

    Ric_G,HH=Ric_g+(a/4)g,
    Ric_G,VV=Ric_flat,ag,
    R_G=-10+a^-1 R_g,
    Ric_G²=115/8+(1/(2a))R_g+a^-2 Ric_g².

Consequently

    F_G(x,a g_x)
      =a^-2[Ric_g²+(5/2)R_g²]-(99/2)a^-1 R_g+2115/8.      (3)

At a=1 this is the exact scalar observation identity. It is not a14-form pullback and does not itself select a4D action. The relative fibre parameter a is a dimensionless metric ratio in the declared geometric units.

## 2. Three different measure types

The triangular horizontal/vertical coframe has determinant1, so the actual ambient absolute volume disintegrates as

    dVol_G=d^4x sqrt|det y| dmu_K(y).

Let dmu_g(y) be a **vertical measure**, initially rho(g,y)dmu_K(y) when a density exists. Do not call it a normalized total-fibre probability without the horizontal determinant factor. Its tensor-density moment is

    M^mu nu(g,x)=integral sqrt|det y| y^mu nu dmu_g(y).     (4)

For a measure supported on y=a g, write dmu_g as the pushforward of a positive measure dlambda(a), and m_j=integral a^j dlambda(a). In four dimensions sqrt|det(a g)|=a²sqrt|det g|. Hence

    vertical mass=m0,
    total fibre-volume factor N=m2,
    M^mu nu=m1 sqrt|g|g^mu nu.                            (5)

If m2 is finite and nonzero, the **normalized total-fibre probability** is

    dnu(a)=a² dlambda(a)/N,
    c=E_nu[a^-1]=m1/m2,
    d=E_nu[a^-2]=m0/m2.

Thus M=Nc sqrt|g|g^-1, with Nc=m1 and Nd=m0. N,c,d are linked by the underlying measure; they are not three freely independent normalizations.

**Required atom control:** a vertically normalized delta_(a g) has

    (m0,m1,m2)=(1,a,a²), N=a², c=1/a, d=1/a²,
    M=a sqrt|g|g^-1.

Writing M=a^-1 sqrt|g|g^-1 for that same vertical atom is wrong. Fixing total N=1 and nu=delta_a instead defines a different vertical measure a^-2 delta_a.

Even fixing both vertical normalization m0=1 and total volume N=m2=1 leaves m1 undetermined. Compare delta_1, with m1=1, with vertical weights5/8 at a=1/2 and3/8 at a=3/2, which have m1=7/8 and m2=1. Their total-probability weights are5/32 and27/32. These are unselected mathematical controls, not proposed physical states.

## 3. Exact formal reduction on conformal support

Applying the same vertical measure to the leading effective density (1), equation(3) yields

    I_eff^(h)=(h/2)integral_X dVol_g [
      m0(Ric_g²+(5/2)R_g²)
      -(99/2)m1 R_g+(2115/8)m2 ].                        (6)

This formula is exact at order h. For constant moments define

    A_Q=h m0/2,
    A_R=-99h m1/4,
    A_0=2115h m2/16.

Then (6) is integral dVol_g[A_Q Q_g+A_R R_g+A_0], with Q_g=Ric_g²+(5/2)R_g². It describes a declared formal reduction. It neither proves that a singular measure is source-selected nor that inserting a weight into the original action preserves its full equations or native branch. Metric-dependent weight/domain terms must be included in that changed action's variation.

A moving covariant reduction of this kind changes the earlier fixed-product-regulator problem. In particular its nonzero constant A_0 produces a metric volume variation; one cannot carry the old flat-base primitive stationarity into (6) unchanged.

### Four-dimensional Weyl/Euler decomposition

In four dimensions, for the same metric and curvature convention,

    C²=Riem²-2Ric²+R²/3,
    E4=Riem²-4Ric²+R²,
    Ric²=(1/2)(C²-E4)+(1/3)R².

Therefore

    Q_g=(1/2)C²-(1/2)E4+(17/6)R².                       (7)

The leading reduced coefficients are A_Q/2 on C², -A_Q/2 on E4, and17A_Q/6 on R². The coefficient17/6 is before multiplying by h m0/2.

Only for a constant prefactor and an appropriate closed-domain/boundary prescription can the Euler/Gauss–Bonnet term be removed from the bulk metric variation. Compact metric variations away from a fixed boundary suffice locally. A varying moment m0(x), curvature-dependent measure, moving boundary without its completion, or unspecified global convergence does not permit dropping it. This is a geometric identity, not a claim that the source has selected a conventional curvature-squared gravity theory.

Ricci-flat control: C²=E4, so Q_g=0 despite possibly nonzero Weyl curvature. Dropping E4 at the density level would falsely change (3) on that control. Constant sectional curvature control: Ric²=R²/4, C²=0 and E4=R²/6, giving Q_g=11R²/4 from either side of (7).

## 4. Fixed regulator versus moving metric moment

For the original fixed fibre regulator, the two-derivative term is instead

    I_2=gamma integral d^4x M^mu nu Ric_g,mu nu,
    gamma=-99h/4,

with constant M independent of the varied g. At a flat reference eta and M=c eta^-1, let H2 be the quadratic coefficient of c integral sqrt|g|R_g for g=eta+epsilon p. With compact base variation,

    H2=-(c/2)integral p^mu nu G1_mu nu(p),
    delta(sqrt|g|g^mu nu)=(1/2)tr(p)eta^mu nu-p^mu nu,
    c integral delta(sqrt|g|g^-1)Ric1=2H2.

Expanding the product gives

    integral M^mu nu Ric2_mu nu=-H2.                     (8)

Thus the fixed-regulator quadratic Einstein-shaped coefficient is +99hc/4, whereas a moment that actually moves as c sqrt|g|g^-1 yields the full EH term with coefficient-99hc/4. Equality of moments at one background does not justify interchanging these variations.

For any constant symmetric M, the necessary linearized coordinate-gauge identity is

    M^mu nu partial_rho Ric1_mu nu
      -2M^mu nu partial_mu Ric1_rho nu=0.

At a temporal wave covector, linearized Bianchi allows arbitrary symmetric spatial Ric1_ij with Ric1_0i=0 and Ric1_00=-sum_i Ric1_ii for eta00=-1. The identities force M^0i=0 and M^ij=-M^00 delta_ij. Conversely contracted Bianchi proves sufficiency. Hence the complete constant-moment condition is M=c eta^-1. Generic fixed M fails this Einstein gauge test for the **fixed external regulator**. Moving its data or changing the physical domain changes that premise.

A simple sign control is g=e^(2sigma)eta: fixed eta^mu nu Ric_mu nu gives -6(partial sigma)² after integration at quadratic order; sqrt|g|R_g gives +6(partial sigma)².

## 5. Positive-measure coefficient class: exact moment cone

For nonzero positive dlambda on a>0 with finite m0,m2, Cauchy–Schwarz gives

    m0>0, m1>0, m2>=m1²/m0.                             (9)

Equality holds exactly when a is constant almost everywhere. These are also sufficient. Put mu=m1/m0 and v=m2/m0-mu². For v=0 use m0 delta_mu. For v>0 use

    a_minus=mu/2,
    a_plus=mu+2v/mu,
    p_minus=4v/(mu²+4v), p_plus=mu²/(mu²+4v),
    dlambda=m0[p_minus delta_(a_minus)+p_plus delta_(a_plus)].

Both atoms are positive and realize the prescribed moments. Thus (9) is the entire first-two-moment cone, not merely a necessary bound or sampled family.

For h≠0 the reduced coefficients consequently satisfy

    sign(A_Q)=sign(A_0)=sign(h), sign(A_R)=-sign(h),
    0 < A_R²/(A_Q A_0) <= 2178/235.                      (10)

Indeed the ratio is (2178/235)m1²/(m0m2). Equality is exactly the single-conformal-scale class. Every allowed strict moment triple above is realized; the value0 is only a limit for positive nonzero m1. These are relative coefficient signs under the held global action normalization, not physical positivity or a measured gravitational constant.

If one **additionally** identifies A_R(R-2Lambda) as an Einstein sector with constant moments and suitable units, then algebraically

    Lambda=-A_0/(2A_R)=(235/88)m2/m1.

This is a conditional ratio in the native unit-curvature convention. It is not a physical Lambda G prediction: action/matter normalization, units, state/domain admission, the higher-curvature spectrum and the reduction itself remain separately required. An imported dimensional ruler does not erase the moment dependence.

## 6. Why conformal-support measures are a genuine whole class

The owned `natural-density-fibre-volume-2026-11-25.md` already excludes a finite smooth positive zero-order (g,y)-natural density on a nonempty invariant open Lorentz metric fibre. No new credit is due for repeating that theorem.

The measure-class statement is: every finite positive Lorentz-invariant Borel measure on the fixed-signature fibre is supported on {a g:a>0}. For each of three coordinate boosts, congruence on Sym² is diagonalizable with positive real eigenvalues. Poincare recurrence for a finite invariant measure implies almost every point is fixed: an expanding component escapes, while a nonzero contracting component converges to a different point and cannot recur to its original neighborhood. A countable local basis makes this pointwise recurrence conclusion simultaneous almost everywhere. The intersection of the three boost-fixed spaces is span(g); the fixed Lorentz signature imposes a>0.

This supplies the conformal-support class without guessing a Gaussian. It permits singular measures, but not a smooth full-dimensional positive density. It excludes neither signed/renormalized distributions nor measures using a selected clock, state, quotient or other input that breaks the stated stabilizer. Source observation does not thereby become a fibre integral. A covariant family of such measures depending only on g has a fixed law on the dimensionless ratio a; extra x/curvature dependence changes the variation class.

## 7. Conditional scalar instability of the leading local4D moment model

This section concerns **only** the real four-dimensional Lorentzian local metric action with constant moments in(6), its ordinary unrestricted local metric variations, and the leading order-h truncation. It is not an instability theorem for the actual14D wedge system, a proof of its curved analytic reduction, a quantum ghost claim, or a source/physical-state exclusion. No W2 symmetry or eigenvalue is used.

Write

    S4=integral sqrt|g| [A R+alpha Ric²+beta R²+A0],
    A=A_R, alpha=A_Q, beta=(5/2)alpha,
    b=beta+alpha/3=17alpha/6.

Assume h≠0 and a nonzero positive finite measure in the moment cone. The metric signature is(-+++), Riemann convention as BH1–3, and □=g^mu nu nabla_mu nabla_nu. Positive Klein–Gordon mass uses(□-m²)f=0.

### Background and trace

Variation with respect to the inverse metric gives the trace equation

    (2alpha+6beta)□R-A R-2A0=0.                         (11)

The algebraic curvature-squared trace cancels in four dimensions. In particular an Einstein constant-curvature background has

    R_mu nu=Lambda g_mu nu,
    Lambda=-A0/(2A)=(235/88)m2/m1>0,
    R0=4Lambda.

Both quadratic Euler tensors vanish on this background, so it solves every metric row, not only the trace. Omitting A0 and expanding about flat space would use a nonstationary background.

Linearizing(11) gives

    (□-m_s²)delta R=0,
    m_s²=A/(2alpha+6beta)=A/(17alpha)
        =-99m1/(34m0)<0.                                (12)

Convention control: for the ordinary f(R) subclass alpha=0, A>0,beta>0, the same formula gives m_s²=A/(6beta)>0. Thus the negative sign in(12) is not a reversed Klein–Gordon convention.

### Full-row mode admission; the trace is not used alone

By(7), the action is locally equivalent in its metric equations to

    f(R)+(alpha/2)C²,
    f(R)=A R+bR²+A0,

after retaining the constant-prefactor Euler boundary qualification. De Sitter is conformally flat. A pure conformal perturbation

    delta g_mu nu=phi g_mu nu

lies in an exactly conformally flat path, so the Weyl-squared/Bach linearization is zero. For this perturbation,

    delta R=-(3□+4Lambda)phi,
    delta G_mu nu+Lambda delta g_mu nu=D_mu nu phi,
    D_mu nu=g_mu nu□-nabla_mu nabla_nu+Lambda g_mu nu.

With F0=f'(R0)=A+8bLambda, the full f(R) linearization is

    delta E_mu nu=F0(delta G_mu nu+Lambda delta g_mu nu)
                    +2b D_mu nu(delta R)
                =D_mu nu[(A-6b□)phi].                    (13)

Consequently every real solution of(□-m_s²)phi=0 solves **all** the linearized metric rows, not merely their trace or a scalar ansatz equation. No unexamined traceless constraint removes it in this declared local model.

The curvature perturbation is nonzero on this mode. Indeed the moment cone gives

    3m_s²+4Lambda
      =(235/22)m2/m1-(297/34)m1/m0
      >=(364/187)m1/m0>0.                               (14)

Thus the potential critical degeneration F0=0 is absent; equivalently F0/alpha>0. Since R0 is constant, an infinitesimal diffeomorphism has delta R=Lie_xi R0=0. The nonzero delta R supplied by(13) is therefore gauge invariant.

### Explicit real growing solution and ceiling

In the expanding de Sitter patch

    ds²=-dt²+e^(2Ht) dx², H²=Lambda/3,

take phi=e^(r t), independent of spatial coordinates, where

    r=[-3H+sqrt(9H²+4|m_s²|)]/2>0.

It solves(12) for phi, and (13) supplies the actual linearized metric solution with exponentially growing nonzero delta R. This is an exact local classical tachyonic scalar mode of the **leading4D local moment model**. Homogeneous modes are not infinite-volume normalizable states; no such norm is claimed. The normally hyperbolic scalar equation also clarifies that a tachyonic mass is not an unbounded high-frequency ill-posedness argument.

There is no measure-uniform positive lower bound on the growth rate from positivity alone; no observational lifetime is inferred. Additional boundaries or a physical-state restriction could exclude these local solutions, but that is a change in the admitted domain and must be supplied. Higher orders in h, nonlocal elimination, nonconformal-support reductions, the full coupled14D equations and matter/quantization remain outside. The result earns a new concrete property of the specified reduced coefficient class; it does not falsify GU or establish a measured cosmological instability.


## 8. Independent constraint calculation and controls

There is also an independent cosmic-time check. Write d=17A_Q/6, f''=2d, F0=f'(R0). For deltaR=r0 exp(lambda t), take

    deltaH=f''(H-lambda)deltaR/(2F0).

The linear Friedmann constraint is 6F0 H deltaH=3f'' H(H-lambda)deltaR. The spatial row is -2F0 deltaH_dot=f''(deltaR_ddot-H deltaR_dot). The curvature relation deltaR=6(deltaH_dot+4H deltaH) holds precisely when lambda²+3Hlambda+m_s²=0. The denominator cannot vanish:

    F0=h(3995m0m2-3267m1²)/(132m1),
    3995m0m2-3267m1² >=728m1²>0.

This checks the same local mode in cosmic time without mistaking the trace equation for the constrained system. Ordinary GR has no scalar evolution coefficient in its trace; healthy A R+b R² with A,b>0 instead has m_s²=A/(6b)>0. These calibrators concern scalar admission and sign, not spin2 ghost quantization. The metric equations and de Sitter scalar criterion agree with [Faraoni](https://arxiv.org/html/gr-qc/0703044v2) and [De Felice–Tsujikawa §2.1](https://arxiv.org/html/1002.4928v2); the coefficient substitution and full-row check here are specific to this declared reduction.

The exact [probe](../../tests/program-focus/wedge_shiab_einstein_reduction_probe.py) covers direct Gamma1-Gamma1 mixed gauge polarization, its rank-nine kernel, metric-density sign reversal, rational Lorentz boosts, normalization mutations, moment-cone identities, the full conformal metric row and independent FLRW constraints. In particular, pure-gauge quadratic evaluation vanishes for every fixed moment and is an intentionally inadequate control: the mixed polarization detects the error. [Lean](../../Lean/GUFormalization/WedgeEinsteinReduction.lean) checks only stated finite arithmetic and inequality cores. It does not formalize curvature geometry, measure recurrence, action reduction or PDE existence. Internal independent review validates these intended constructions separately.

## 9. External mechanisms and their transfer burdens

Comparator routing: the following are comparisons of named conventional constructions, not evidence against the source-native connection-Higgs, grading, observation or physical quotient. They bind the declared reduced model only after its action, state/domain and observables are matched. No external prescription is adopted.

| Mechanism / primary source | What the paper supplies | Exact missing premise for this wedge; useful disposition |
|---|---|---|
| **4D quadratic decomposition**, [Salvio review §2.1, eqs2.3–2.8](https://arxiv.org/html/1804.09944v2) | In four dimensions, `Ric²=C²/2+R²/3-E4/2`; E4 is the Euler density, with the usual local/boundary qualifications. | This identity must act on a genuine reduced four-dimensional metric action. It cannot discard a 14D curvature invariant as topological. If the *same coefficients* survived reduction, the displayed combination would be `C²/2+17R²/6-E4/2`, not pure Weyl/conformal gravity. This conditional substitution is our algebraic inference, not an established GU reduction. |
| **Agravity / Einstein scale**, [Salvio–Strumia, §3](https://arxiv.org/html/1403.4226v3) | A dimensionless 4D quantum theory can generate a Planck scale through running and a scalar nonminimal curvature coupling; the worked perturbative route also imposes the vacuum-energy conditions on the quartic and its beta function. A strong-coupling route is discussed separately. | Need the reduced quantum action, actual scalar/nonminimal coupling and vacuum/RG conditions. No such scalar is supplied by calling a vertical one-form a Higgs. Classical background cross-terms in the ambient quadratic invariant are a distinct, cheaper route to test now; they do not establish quantum dimensional transmutation. |
| **Bender–Mannheim PT**, [unequal-frequency PU](https://arxiv.org/abs/0706.0207), [equal-frequency companion](https://arxiv.org/abs/0804.4190) | Explicit positive-inner-product realizations for their oscillator; equal frequency requires separate treatment because the ordinary similarity limit is singular and the Hamiltonian is nondiagonalizable. | Need the wedge's actual reduced generator, spectrum, invariant closed domain, contour/inner product and observable transformation. Formal antilinearity does not by itself supply positive energy. Equal oscillator frequencies in different wedge channels do not establish an equal-frequency fourth-order PU Jordan system. Preserve as a later quantization test, not cancellation of an owned classical row. |
| **Kuntz complex deformation**, [published v4, §§V–VI](https://arxiv.org/html/2410.08278v4) | Complex-deformed quadratic gravity with pseudo-Hermitian framework; a positive-metric calculation is perturbative in a truncated interacting model. The full nonperturbative interacting eta is explicitly beyond scope. | Need matching 4D action and spin/gauge carriers, BRST physical space, contour and interacting eta for the wedge. Do not turn the abstract's broad language into a theorem that every PT-symmetric interacting theory is positive. |
| **Anselmi fakeons**, [unitarity prescription](https://arxiv.org/abs/1909.04955), [classical limit](https://arxiv.org/abs/1809.05037) | Particular pole prescriptions and a physical projection; the classical theory is obtained after quantization/classicization, with microcausality consequences. | Need actual poles, interaction vertices, admitted asymptotic states and a declared prescription. A fakeon is not an algebraic deletion of every sourced response. This adds physical completion data and may change the classical propagation problem; it does not certify the current unprojected wedge dynamics. |
| **Donoghue–Menezes unstable resonance**, [2019](https://arxiv.org/abs/1908.02416) | Authors' all-orders unitarity argument uses unstable ghost-like resonances absent from the asymptotic spectrum, stable-state cuts and specified contour treatment. | Need native resummed propagators, a nonzero decay width, stable asymptotic states and matching amplitudes. Negative classical canonical energy or an oscillatory homogeneous mode establishes none of these. No immediate Einstein-coefficient inference. |
| **Holdom–Ren strong gravity**, [2016](https://arxiv.org/abs/1605.05006) | Conjectured nonperturbative removal of the perturbative spin2 ghost and emergence of IR GR, motivated by a QCD analogy and running into strong quadratic coupling. | Need the reduced quantum couplings, RG flow/strong scale and an actual IR response. It is explicitly a conjectural dynamical route, not a proven remedy for arbitrary quadratic actions. Large printed kappa in the classical wedge IFT is not their quantum strong-coupling scale. |
| **Boyle–Turok dimension-zero fields**, [2022 version](https://arxiv.org/abs/2110.06258) | Their proposed 36 conformally coupled dimension-zero scalars cancel specified vacuum/Weyl-anomaly contributions with an emergent Higgs and 48 Weyl fermions; extra gauge structure removes local scalar particle states in their construction. | Need these actual fields, kinetic operators, gauge quotient and anomaly accounting. GU's effective2+1 nonchiral carrier is not automatically their48 species. Reuse `explorations/boyle-turok-foil-class-relative-typing-2026-08-03.md`; do not redo the settled multiplicity-versus-index distinction. This is neither a general metric-ghost removal theorem nor an Einstein coefficient calculation. |

These mechanisms establish that familiar higher-derivative objections can depend on the physical completion. They do not establish that a specific completion applies here. They are distinct alternatives, not a bundle whose virtues can be combined without checking compatibility. The prior audit also retains contrary quantization results (Kubo–Kugo and Kubo–Kuntz); no literature consensus is assumed.

## Shielding / observer measure: what would count

SC-META-53 (`lab/sources/source-claim-register.yaml`, TOE01:22:30) records an explicitly uncertain maximal-compact shielding claim, not a selected positive physical space. For this wedge, the owned literal observed coderivative is

`O(t_w(h))=(21/16)h gamma4+O(h²)`.

`O` is coderivative after actual one-form section contraction, with ambient adjoint coefficients retained; it is not physical stress already identified. Higher-order terms cannot cancel its leading coefficient uniformly near h=0. A new physical readout/current/measure could instead annihilate or suppress that receiver, but the map and its field dependence must be explicit. Exact cancellation requires an exact leading moment/receiver equation. Approximate shielding requires a numerical or asymptotic bound relative to an admitted signal and domain; the word shielding supplies no bound.

A measure change must identify whether it changes the action, the observables, or both. Variation of a g-dependent measure and differentiation of an x-dependent observer kernel produce additional terms. A fixed positive scalar weight does not automatically cancel a fixed nonzero matrix receiver; sign-changing kernels, changed supports, or a projection require their own calculation. Reuse `explorations/conditional-build/natural-density-fibre-volume-2026-11-25.md` and `symmetry-restoration-measure-limit-2026-11-25.md` for already-known volume/moment boundaries rather than demand impossible full-fibre normalization again. Singular section measures are a separate conditional construction, not a smooth14D reduction.


## 10. Wedge-specific symmetry, scale and bounded synthesis

The real scalar equation is invariant under complex conjugation. That symmetry does not remove its real growing solutions: the nonzero gauge-invariant deltaR remains real. The W2 Krein-reversing quaternionic operation has not been shown to intertwine the wedge's reduced constrained generator or its domain. A C/V operator or changed contour must be built for that owner; no positive-norm inference follows from the shared vocabulary. This is a classical tachyonic-mass result, not a Pais–Uhlenbeck Jordan-block identification or a quantum spin2-ghost theorem.

**Newton scale:** yes, a background cross-term can supply a nonzero Einstein term in the declared conformal-measure reduction. No, neither the imported dimensional reference nor normalization alone fixes it: even m0=m2=1 leaves m1 free. Agravity-style dimensional transmutation is not calculated here. Physical low-energy GR requires a stable admitted spectrum and matter normalization, in addition to the coefficient.

**Observed conservation:** the existing literal receiver is nonzero already for flat observed g. Thus an exact bound by observed curvature alone, with no other scale or background term, cannot repair that receiver: its right-hand side vanishes on the owned flat-base witness. A constant positive scalar reweighting cannot turn this fixed nonzero receiver into zero. A metric-dependent observer measure, new current or different physical readout changes the calculation and remains undetermined. The reduced covariant action has its own diffeomorphism identity; identifying its current with the literal observation is an additional bridge. No physical nonconservation is inferred merely from O(t1).

**Choice budget:** record the already-existing wedge Shiab member as one GU* structural alternative, with the cost that its consistent own-action equation differs from the printed unit endpoint. This is not a newly added family this wave. The conditional measure class is classified, not selected or adopted; no new physical completion, tunable coefficient or prediction is selected. W2's historical 10/4/net6 is retained separately and is not a parameter count for this model. m0,m1,m2 describe residual coefficients of this optional reduction and cannot be compared numerically with the SM parameter inventory without a physical map.

**Remaining native burdens:** large-|kappa| existence survives on its original regulator. Continuation to1, full constrained energy count, higher-order curved elimination and a physical norm remain open. No continuation was attempted in this final wave because the leading reduction gives the cheaper class discriminator. The three-wave wedge investigation is complete with these named burdens. It does not impose an authorization stop on research.

The gravity map is therefore: **GU* own wedge is variationally consistent; a native homogeneous large-coupling branch and leading ambient quadratic density survive; a declared covariant local reduction contains an Einstein term but its de Sitter background is scalar-unstable. The full gravity pillar is INCOMPLETE.** No ledger verdict, source claim or published floor is changed. This is a new application to the declared wedge coefficients, not a claim of a novel general quadratic-gravity theorem.


## 11. Joe27x: native indefinite volume versus an added reference measure

This fork is a distinction between **metric contractions, integration density and physical state pairing**. The positive finite covariant measure above is a declared optional reference class. It is not a replacement of the native indefinite metric by a Riemannian metric, and it should not be called the physics-default measure.

For the actual native K95 geometry,

    K_y(U,V)=tr(y^-1 U y^-1 V)-(1/2)tr(y^-1U)tr(y^-1V),
    K_y(c y,d y)=-4cd,
    signature(K)=(6,4),
    dmu_K(y)=C |det y|^(-5/2) product_{i<=j}dy_ij, C>0.

Thus the trace/conformal direction has the opposite sign already in the BH1–BH3 curvature calculation and in the baseline eigenvalues1/4 (five directions), -5/4 (nine). It was not dropped. The usual pseudo-Riemannian volume is nevertheless sqrt|det K| times coordinate volume. Its contractions are indefinite; its scalar integration density is positive. Reversing a chosen orientation only multiplies the entire integral by one sign and cannot reverse Einstein relative to curvature-squared. Replacing K by -K would change the curvature/action, not just the measure, and is not performed silently here.

### Native reduction, run to its actual boundary

With the unweighted native fibre density the same calculation starts as

    I_native^(h)=(h/2) integral d4x integral_fibre
       sqrt|det y| [2115/8-(99/2)y^-1:Ric_g+O_base(4)] dmu_K(y).

For the flat-base control the integrand is exactly2115/8 before the volume factor. The positive total fibre integral is infinite. Under y -> t y the fibre density dmu_K is invariant and sqrt|det y| scales as t²; disjoint scaled copies of any compact positive-volume set already force divergence as t grows. This is also within the earlier natural-density infinite-volume theorem. No finite unregulated Einstein or R² coefficient, and no ratio of such divergent coefficients, has thereby been defined. The normal trace sign supplies no cancellation of the constant positive density. A finite regulator, signed/distributional or oscillatory prescription, quotient or renormalized integral must be stated separately before its coefficients can be calculated.

| Construction | Einstein versus scalar-curvature coefficient | Scalar conclusion |
|---|---|---|
| Native K95, full trace-reversed fibre and unweighted pseudo-Riemannian volume | Leading integrand fixed above; full integral is not finite. No reduced coefficient ratio is defined. | **UNDETERMINED**: no finite native4D operator to test. |
| Native K95 contractions plus finite positive covariant reference supported on a g | A_R/A_Q=-(99/2)m1/m0; scalar coefficient b=17A_Q/6, so m_s²=A_R/(6b)<0 | **ESTABLISHED**: growing local real curvature mode in the stated leading reduction. |
| Fixed external regulated native fibre | Tensor moment M, with gauge compatibility iff M=c eta^-1; its Einstein-shaped quadratic sign is opposite to metric-moving M | This is a different, generally noncovariant variation problem; scalaron verdict not transferred. |
| Signed/oscillatory/contour-dependent reference | Positive moment inequalities no longer available; relative sign is prescription-dependent | **UNDETERMINED** until a source-cited or explicitly costed prescription is supplied. |
| Conditional K77 realization | The source assertion, flipped-base comparison and a separately altered vertical pairing are different constructions; source-selected native reduction/action normalization is not supplied | **UNDETERMINED**, no K95 stability or healthy-scalaron transfer. |

The finite controls check both base g=(-+++) and the separately labelled flipped g=(+---): each unchanged trace-reversed vertical block has signature(6,4), trace norm-4 and positive absolute volume. These algebraic checks do **not** certify a K77 wedge action or carry its Hodge/adjoint normalization. Changing base signature also changes the physical Klein–Gordon sign convention and the sign of scalar curvature assigned to de Sitter; keeping a bare coefficient sign while dropping those changes would manufacture a healthy-scalaron conclusion.

A signed conformal reference, as a logical countercontrol only, can have m0=1,m1=-1,m2=-5 (3 delta1 minus2 delta2). It violates positivity and reverses the formal scalar-mass sign. It is neither adopted nor source-selected and supplies no positive graviton/state theory. This demonstrates why the positive-measure theorem cannot be called construction-independent.

### Conformal-factor precedent and disposition

[Gibbons–Hawking–Perry](https://doi.org/10.1016/0550-3213(78)90161-X) treat the unbounded Euclidean gravitational action by rotating a conformal-factor integration contour. That is a quantum integration prescription, not a negative sign assigned to the ordinary volume element. It does not by itself remove a gauge-invariant real Lorentzian deltaR solution while preserving the same admitted real initial data. Ordinary GR's conformal-factor issue is not an extra propagating scalaron; the present leading R+curvature-squared model has a nonzero scalar derivative coefficient and a full constraint-compatible mode.

**Joe27x disposition:** the native indefinite calculation was retained and tested, including its negative trace direction. It does not presently supply an alternative finite4D reduction with a healthy scalaron. Nor have both constructions been shown unstable. The correct result remains a scoped positive-reference-class instability plus an unregulated-native reduction burden. A Starobinsky comparison would require a finite covariant action with the healthy relative sign, a positive physical graviton normalization and a controlled state/domain; none is inferred from signature alone. No new reference measure or choice family is adopted.
