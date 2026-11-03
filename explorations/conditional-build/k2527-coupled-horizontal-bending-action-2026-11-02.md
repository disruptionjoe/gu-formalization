---
title: "K2527 Coupled horizontal metric lift: exact bending action and source obstruction"
status: active_research
doc_type: exploration
created: "2026-11-02"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: declared single-field and two-field diagonal linear response only; no full native I1 or nonlinear source exclusion
scripts:
  - tests/channel-swings/k2527_coupled_horizontal_bending_action_probe.py
---

# K2527 Coupled horizontal bending action

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `CONVENTIONAL_COMPARATOR`.

```gu-typed-objects
result: K2527
carrier: one coupled metric g or explicitly independent lift metric q and section y in Met(X), with LC-horizontal ambient lift LAYER=toy CHIRALITY=N/A
pairing: induced volume and signed nondegenerate vertical DeWitt form ON=declared_carrier
real_structure: real metric section; n4 trace coefficient1/2 gives total inertia(7,7)
grading: fixed ambient, independently varied ambient and coupled single-field variations are different
action_owner: repository-construction -- coupled alpha normII squared plus beta normH squared bending action
target: all-background action reduction, full coupled Euler and source-response inference boundary MAP-TYPE=evaluation
```

## Result and prior work

The full coupled variation changes the answer. For the existing Levi-Civita-horizontal lift, the raw bending action is exactly a constant times spacetime volume for EVERY smooth base metric. At beta=2alpha it vanishes identically; it has no metric kinetic operator to respond to nonzero stress. This is a scoped obstruction for the declared bending-only construction, not native GU.

[B2C15P](../eric-curt-wave3d-b2c15p-source-epsilon-tangent-zorro-dewitt-2026-08-02.md) already constructs the lift and its observation identity. [W136](../W136-issuance-declaration-propagation-2026-07-14.md) owns the flat stationary coefficient ratio. [K2525](k2525-metric-bundle-section-action-2026-11-02.md) owns the full FIXED-ambient section response. Here the new calculation is the unnormalized all-background coupled-action reduction and its source consequence. These prior results are reused, not rediscovered. Older normalized-reference II=0 results are different from the nonzero raw II calculated here.

SC-GEO-03, SC-ACT-01 and SC-GEO-55 ASSERTS retain their section-induced geometry, action and independent displacement roles. The explicit coordinate lift and this bending action remain repository constructions, not a unique source-selected completion. SC-META-53 remains UNCERTAIN; LT-GR6b/GR10/GR11 and ledger0.263 are unchanged. In particular the independent I1 displacement Euler at K2345 has not been solved. No causal, positivity, empirical, particle, or native source/readout credit follows.

## 1. One field and its coupled lift

On X of dimension n, let g be a smooth nondegenerate metric of fixed signature. Use the fixed-signature metric bundle with fibre coordinate y. For constant ell>0 and lambda !=1/n, define

    D_y(U,V)=tr(y^-1 U y^-1 V)-lambda tr(y^-1 U)tr(y^-1 V),
    C_i(g,y)=Gamma_i(g)^T y+y Gamma_i(g),
    theta=dy-C_i dx^i,
    G[g]=y_ij dx^i dx^j+ell² D_y(theta,theta),
    s_g(x)=(x,g(x)).                                      (1)

The ONLY field in this model is g: both G[g] and s_g vary when g varies. The connection is the actual LC(g), including its dependence on first derivatives of g. Metricity gives theta(ds_g)=0 and s_g^*G[g]=g exactly. The construction transforms as a bundle connection metric under coordinate changes. Tensor identities below therefore hold wherever the metric section/lift are defined, without a flatness hypothesis. Use compactly supported variations on a fixed region, or a compact manifold; no finite total Lorentzian volume of a noncompact spacetime is presumed.

Let H_i=partial_i+C_i^A partial_A be the horizontal lifts. At the section ds_g(partial_i)=H_i. Their vertical curvature bracket is, up to the curvature convention sign, R_ij^T g+gR_ij=0, because the base connection is metric. Vertical vectors are the normal bundle there. For any vertical symmetric U, Koszul gives

    2 ell² D_g(II_ij,U)=-U_ij.                          (2)

The derivative of G(H_i,H_j)=y_ij in direction U is U_ij. The two horizontal/vertical bracket terms are vertical and pair to zero with H. The horizontal bracket has zero vertical part at the section. These facts prove(2) for arbitrary curvature and every normal component; no zero-jet identification substitutes for connection control.

## 2. Complete contractions and action

Invert the trace-reversed pairing. With symmetrization of i,j of weight1/2,

    (II_ij)_ab=-[g_a(i g_j)b+lambda g_ij g_ab/(1-n lambda)]/(2ell²),
    H_ab=g^ij(II_ij)_ab=-g_ab/[2ell²(1-n lambda)].        (3)

The normal norm uses ell²D, not D alone; all tangent contractions use g^-1. Consequently, writing m=n(n+1)/2,

    normII²=[m+n lambda/(1-n lambda)]/(4ell²),
    normH²=n/[4ell²(1-n lambda)].                        (4)

The first identity follows by contracting the inverse pairing on symmetric tensors; its tracefree part has dimension m-1 and its trace part has eigenvalue 1/(1-n lambda). Signed contractions are essential. At n4,lambda1/2,

    normII²=2/ell², normH²=-1/ell²,
    S[g]=(1/2) integral(alpha normII²+beta normH²)dmu_g
        =c Vol_g, c=(alpha-beta/2)/ell².                (5)

This is an exact functional identity, not only a principal-symbol or constant-section calculation. For arbitrary compact h=delta g,

    delta S=(c/2) integral tr(g^-1 h)dmu_g.

For affine metric variations the mixed second derivative has density

    c[(tr(g^-1 h)tr(g^-1 k))/4-tr(g^-1 h g^-1 k)/2]dmu_g. (6)

There are NO metric derivative terms. At beta=2alpha all variations vanish. Off that ratio vacuum stationarity would require c g^-1=0, impossible for a nondegenerate metric. At general n,lambda the zero-action line is

    beta/alpha=-(n+1)(1-n lambda)/2-lambda, alpha !=0.    (7)

At lambda=1/n the vertical pairing is singular and(1)-(7) are not an admissible pseudo-Riemannian construction. ell is fixed; varying it or allowing position-dependent coefficients changes the field space.

## 3. Source and Gauss consumers

At beta=2alpha, supply a linear conserved metric source j about any background, with the usual paired source/readout convention. The linear response equation is 0=j. Nonzero j has no solution in this bending-only model, hence receiver rank10 does not produce a Green inverse or a matter/light ratio. Such a nonzero conserved source exists already in flat space: a time-independent smooth compact spatial density j00=rho(x), other components zero. It has partial_i j^ij=0; no nonlinear matter equilibrium is asserted. At general c, if delta S_m=(1/2)integral T^ij delta g_ij dmu_g, the metric equation is c g^ij+T^ij=0. It supports only the corresponding metric-proportional stress in this sector, not arbitrary supplied stress. Full native I1 or added matter fields may contribute additional equations; they are outside this result.

The fixed-ambient normal receiver remains full rank: (2) implies -2ell²D(II_ij,U)=U_ij. This kinematics does not alter the zero total coupled Hessian.

The signed Gauss identity on the SAME lift reads R_g=R_tan+normH²-normII². Thus

    R_tan=R_g+3/ell²                                 (8)

at n4,lambda1/2. Extracting -R_g from normII²=normH²-R_g+R_tan and discarding the ambient term would invent an Einstein kinetic term: the variation of R_tan cancels it exactly here. Equation(8) is a consequence of the actual embedding and Gauss, not an assumption that ambient curvature vanishes. An independently added R_tan term can supply an EH term with its added coefficient; that changes the action and is not a derivation from the original bending terms.

## 4. The field-space distinction is essential

Three questions must stay separate:

- Fixed G0, variable section s: K2525 has a nonzero fourth-order symbol and the published static response.
- Independent G and s: K2523's independent normal jets impose different equations.
- The single-field rule g maps to(G[g],s_g) in(1): the action reduces to(5).

Nor can one introduce independent q defining G[q] and independent section y, compute only on q=y, and infer both Euler equations vanish. A restricted zero function can have nonzero opposite partial gradients; the elementary F(q,y)=q-y is a direct contrary control. That warning alone does not decide the actual two-field model; section5 now computes its diagonal Euler and full flat response. No result here claims arbitrary native coupled actions have zero kinetic terms.

## 5. Executed two-field successor: full flat source compatibility

Now DECLARE the genuinely independent fields q and y, with ambient G[q] from(1) and observed section s_y. This changes the model; it is not inferred by silently restricting the single-field one. The observed induced metric is

    gamma=y+ell²D_y(nabla^q y,nabla^q y).

On y=q it equals q. We can compute both Euler equations along that entire diagonal without guessing the lower-order Hessian from its principal symbol.

Hold q fixed and vary y=q+epsilon U with compact support. In q-normal coordinates at any point, Gamma(q)=0 but its derivatives are arbitrary. At that point C_i(q,y)=0 for every y. The actual vertical ambient Christoffel and section acceleration give, to first order,

    II^V_ij=Z_y,ij+epsilon nabla^q_(i nabla^q_j)U+O(epsilon²),
    Z_y,ij=-(D_y^-1)^(AB)(E_B)_ij/(2ell²).           (9)

To see the curvature dependence explicitly, write A_ij=partial_i Gamma_j(q). The ambient term contributes -[(A_ij+A_ji)^T y+y(A_ij+A_ji)]/2; section acceleration adds q_,ij+epsilon U_,ij. Metricity cancels its q term, leaving exactly the symmetric covariant Hessian of U. Normal projection changes tangent components at first order, which are orthogonal to Z; it does not change the first variation of the norm. The first variation of gamma is U. Therefore the algebraic part of the variation is exactly that of the constant-density expression(5). The remaining term is

    integral ell²D_q(alpha Z^ij+beta q^ij H, nabla^q_(i nabla^q_j)U)dmu_q.

Z,H and the pairings are parallel under the induced normal connection, which at the section is the tensor connection induced by LC(q). Compact integration by parts makes this term zero. Thus, normalized by dmu_q, the fixed-q section Euler is

    E_y(q,q)=(2alpha-beta)q^-1/(4ell²).               (10)

At beta=2alpha, E_y(q,q)=0 for EVERY smooth q. The already proved restricted identity S(q,q)=0 then gives E_q(q,q)=-E_y(q,q)=0. Hence all diagonal pairs are jointly stationary in this declared two-field bending model. This conclusion uses the actual independent section variation(9)-(10), not merely the restricted functional identity.

Differentiate both Euler identities along q=y. Every diagonal tangent(a,a) belongs to the COMPLETE Hessian kernel, including all lower derivative terms. At the flat diagonal, let M be K2525's full fixed-q section Hessian in its stated normalization. Formal symmetry plus these diagonal kernel identities uniquely gives, in field order(a=delta q,b=delta y),

    H_full=[[M,-M],[-M,M]], d=b-a,
    -M d=j_q, M d=j_y,
    j_q+j_y=0.                                      (11)

This is the full operator, not only the principal3alpha w²D(d,d). The exact inherited static inverse is available for M, but cannot circumvent(11).

At flat diagonal delta gamma=b. A supplied minimal metric source acting only on gamma therefore has(j_q,j_y)=(0,J), which violates(11) for every nonzero J, including the conserved static source above. This excludes differentiable linear response about the joint flat background in the two-field bending-only class. It does NOT exclude all nonlinear sourced branches or complete native actions with additional equations/terms.

Compatible opposite sources(-J,J) solve for d on K2525's same declared static domain. They do not fix b: arbitrary diagonal Hessian directions change both q and y while leaving d unchanged. A b-only light/motion readout is not uniquely determined by the source and does not descend to the quotient by common null directions. Calling those directions physical gauge would require a nonlinear Noether symmetry, which is not proved here. A d-only paired source/readout is a different supplied observable, not the induced metric gamma. Thus neither one-field coupling nor this two-field extension supplies the missing native induced-metric response; the exact new burden is an additional action term or actual source coupling that removes the compatibility/readout obstruction.

On the inherited static Fourier-annulus domain where M is invertible, this can also be checked by eliminating the lift while retaining its source/contact terms. In the declared quadratic convention

    S2=(1/2)(b-a)M(b-a)-j_q a-j_y b,
    a=b+M^-1 j_q,
    S2_eff=-(j_q+j_y)b-(1/2)j_q M^-1 j_q.             (12)

The Schur operator on b is zero, its effective source is the SUM, and the pure-source contact term remains. Dropping that contact or keeping only the section source would misrepresent elimination. Opposite sources cancel the effective b source but retain relative-field response through the contact; they do not fix the induced metric. These are paired bilinear integrals on the common static domain, not an assertion of a causal inverse.

## 6. Reproduction and boundaries

The probe independently reconstructs the ambient mixed metric first derivatives at a normal-coordinate point and all100 independent symmetric base second jets. For every jet it checks partial_j C_i=g_,ij, the resulting ambient normal connection, and cancellation against section acceleration. A nonflat conformal jet has nonzero scalar curvature and fails if mixed ambient metric derivatives are omitted. This directly checks the weakest transfer in the all-curvature proof. Small exact matrices also verify pairing inversion, general-dimension contractions, the singular trace exception, source/gauge countercontrols and volume derivatives. Universal claims rest on(1)-(8), while finite exact controls challenge their implementation. Reporting/dependency hashes are a separate evidence kind. No external-expert, proof-assistant or novelty certification is claimed.

Independent q/y stationarity and the full flat source-compatibility condition are also established by(9)-(11); native I1 remains separate. This eliminates the proposed shortcut from LC-induced metric plus raw bending to Einstein response in the declared single-field class. The next native construction must retain its actual independent distortion equations and all coupled action terms; it cannot borrow K2525's fixed-G inverse after changing its variational space.
