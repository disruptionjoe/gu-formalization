---
title: "K2529 Selected I1 metric-displacement response on stationary product branches"
status: active_research
doc_type: exploration
created: "2026-11-04"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: homogeneous four-coordinate selected-action response only; no full native Green operator or observed matter response
scripts:
  - tests/channel-swings/k2529_native_displacement_response_probe.py
---

# K2529 An actual action contribution and its restricted response

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
result: K2529
carrier: selected real Cl(7,7) I1 completion on K2519 stationary seven-plus-seven space-form products; independent two metric scales and two displacement amplitudes LAYER=toy CHIRALITY=N/A
pairing: inherited scalar Clifford trace, Hodge and ambient volume; source covector on four declared coordinates ON=declared_carrier
real_structure: real kappa and nonzero real stationary branches
grading: ambient scale, independent displacement, observation pullback and physical source remain distinct
action_owner: repository-construction -- source I1B structure with selected comm/symi/symi Shiab and K2519 moving-conjugation completion
target: coupled invariant-family source response and branch discrimination MAP-TYPE=evaluation
```

## 1. Backward demand and source boundary

[K2527](k2527-coupled-horizontal-bending-action-2026-11-02.md) proves that its bending-only diagonal model cannot supply the declared induced-metric response. It is not native I1B. The backward demand is an actual action contribution with a jointly stationary background, retained displacement equation and nonzero paired metric response; adding an unowned Einstein term or using a fixed-background inverse does not answer it.

SC-ACT-01 ASSERTS the first-order action pairs augmented displacement against Shiab-contracted curvature with the1/2 and1/3 completion and kappa term. SC-GEO-55 ASSERTS displacement from gauge-rotated Levi-Civita, not ordinary torsion. Their source formula is recorded at[primary packet,WGS-01/04](../../lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md). The selected Shiab contraction and independent ambient metric used below remain repository choices. Source formula ownership does not authenticate these choices or a four-dimensional matter reduction. SC-META-53 remains UNCERTAIN; no positivity follows.

First reject an invalid shortcut using existing evidence: at ell=1 the flat-base LC lift in K2527 is the coordinate-horizontal metric-bundle background of[K2345](k2345-curved-bundle-ricci-obstruction-2026-10-30.md). Its ambient curvature is nonzero and its selected native independent-T Euler has nonzero radial pairing -120. The identity I1(G,T=0)=0 gives no stationarity under independent T. This is reused K2345 evidence, not a new computation or a universal claim about every lift. A Hessian there would be an off-shell response and cannot repair a vacuum obstruction.

Instead use the actual nonzero stationary branches of[K2519](k2519-stationary-product-receiver-2026-11-02.md). It proves all-translation, metric and epsilon stationarity for its declared independent-ambient completion. We now compute the full SECOND derivative only along the four-parameter parallel/constant-scale family. The new result is an invertible mixed response on every nonzero branch, with a first-factor readout distinguishing factor-exchanged branches. It is not the infinite-dimensional Hessian and does not solve the native Met(X) or observed matter problem.

## 2. Differentiate the action before restricting the branch

Let G0 have two seven-dimensional factors with Ricci eigenvalues lambda1,lambda2 and signatures(4,3),(3,4). Scale them by e^(2x),e^(2y). Write T=Phi composed(a I7 direct-sum b I7) in the moving soldered frame, u=a+b,v=a-b, and retain a,b as independent fields in this family. With k=kappa fixed, K2519's actual selected I1 density relative to the background volume is

    f=e^[7(x+y)] { 7[(5a+7b)lambda1 e^(-2x)
                        +(7a+5b)lambda2 e^(-2y)]
                   +182u^3-42uv^2+(7k/4)(u^2+v^2) }. (1)

The derivative term vanishes on this parallel family. Changing the constant scales preserves parallelism, so(1) is the exact restricted functional density, including volume, Hodge/soldering and curvature scale dependence. On a noncompact Lorentzian product it is a local homogeneous density, not a presumed finite total action. K2519's isotropy proof controls the full FIRST variation at its seeds; it does not imply arbitrary inhomogeneous second variations close in these four coordinates.

Differentiate in x,y,a,b while holding lambda1,lambda2,k fixed, THEN insert the seed. Substituting stationarity relations first would change the function being differentiated. At a stationary seed the Hessian transforms by congruence under a smooth coordinate change; away from it a gradient times the coordinate second derivative also appears. The source must transform as a covector. In particular, moving-frame amplitude sources below are not automatically fixed-varpi, fixed-T-coordinate or observed matter sources.

## 3. Radial branch: nonzero mixed contribution and exact elimination

At k!=0, K2519's radial seed is

    x=y=0, a=b=-5k/2288,
    lambda1=lambda2=35k^2/604032.

All four first derivatives of(1) vanish. In coordinate order h=(x,y), d=(delta a,delta b), write its Hessian as[[A,B],[B^T,D]]. Exact differentiation gives

    A=k^3/57584384 [[6125,8575],[8575,6125]],
    B=-k^2/302016 [[1225,1715],[1715,1225]],
    D=k/143 [[371,-735],[-735,371]].                 (2)

The mixed block is not zero. The full determinant is

    det H=4215878384375 k^8/17070568672834879488 !=0. (3)

Supply explicitly the finite-coordinate quadratic source convention

    S2=1/2 h^T A h+h^T B d+1/2 d^T D d-j_h^T h-j_d^T d.

Here j_h and j_d are covectors on this family, not an assumed observed stress tensor. D is invertible at k!=0. Retaining its independent Euler equation yields

    d=D^-1(j_d-B^T h),
    E=A-B D^-1 B^T,
    E h=j_h-B D^-1 j_d,
    S_eff=1/2 h^T E h-(j_h-B D^-1 j_d)^T h
                       -1/2 j_d^T D^-1 j_d.         (4)

The pure-source contact term is part of the elimination. Directly substituting the solved d in S2 verifies it. The exact effective metric block is

    E=k^3/655079952384
        [[81760175,109854325],[109854325,81760175]],
    E_plus=6125 k^3/20939776,
    E_minus=-14047075 k^3/327539976192.              (5)

Thus metric-coordinate sources have a unique coupled response in this finite sector. Freezing d gives A^-1 instead of E^-1 and changes the answer. Setting d's equation aside would erase the actual source term being tested. Both symmetric/antisymmetric full2x2 blocks have negative determinant for any k!=0, so the four-coordinate Hessian has inertia(2,2). That is a density-Hessian fact, not a propagating ghost, stability or physical-quotient result.

K2519's totally geodesic Lorentzian4 observer in the first factor has II=0, so its pure-normal fixed-ambient receiver stays zero. However an ambient scale perturbation gives delta gamma=2x gamma. The supplied covector j_h=(j,0),j_d=0 therefore has a computable nonzero kinematic metric readout. This does not turn an ambient14-form into an observed4D source: direct pullback of that14-form vanishes. An actual localization/density, source action and full common-domain variation remain missing. No PPN or light/motion ratio is obtained.

## 4. Executed successor: every nonradial branch and a paired discriminator

The other K2519 branches are

    u=k t, v=sigma k sqrt[t(37/12-59t)],
    t=(828 +/- sqrt105609)/25080,
    lambda1,2=k^2(1-24t)[3t/2 +/- sigma sqrt(t(37/12-59t))/4].

Here sigma=+1 or-1 is an independent branch label, not sign(k). For this section use(x,y,u,v) coordinates. The map(a,b)=((u+v)/2,(u-v)/2) has determinant-1/2, so det H_uv=det H_ab/4. There is no unexplained normalization transfer. Normalize k=1, differentiate(1) first, then reduce polynomials by

    v^2=t(37/12-59t), P(t)=200640t^2-13248t+185=0.

The exact remainder calculation gives

    det H_uv=-117649(6770965254529032408t-331145834811398885)
                       /1515995281338278400000,
    det D_uv=49(273264t-24485)/4180.                 (6)

Both roots satisfy0<t<1153/25080. This upper bound lies below both positive zeros in(6). Hence det H>0 and det D<0. Restoring k multiplies them by k^8,k^2 respectively. The Schur determinant det E=det H/det D is negative. D and E each have one positive and one negative eigenvalue; Sylvester congruence gives the same inertia(2,2) for ALL four nonradial branches. Invertibility is exact, not a numerical eigenvalue scan.

In the reduced family algebra, a scalar determinant/spectrum cannot distinguish factor exchange v to-v; this does not claim an ambient isometry between different factor signatures. Nevertheless, but a paired first-factor source/readout can. With N=A det D-B adj(D) B^T, reduction gives

    (H^-1)_xx-(H^-1)_yy
      =266511 v(118088t-5735)/(4368100 det H)         (7)

at k=1, and the metric response scales as k^-3. Since t<1153/25080<5735/118088 and v!=0, this difference never vanishes on these branches. Exchanging factors swaps xx and yy. For the SAME supplied first-factor covector j and readout2x gamma, the two factor-exchanged realizations give different linear coefficients. This is an explicit finite-sector observable distinction, not a selected physical branch or a source-free prediction. Choosing the first factor and supplying its source/readout is part of the comparison and cannot be counted as action-driven selection.

## 5. Local sourced families and the exact missing bridge

For each fixed nonzero branch, f is real analytic in four coordinates. Equations(3)/(6) let the finite-dimensional inverse function theorem apply to grad f=j: sufficiently small coordinate-linear source covectors have a unique nearby analytic family. This proves existence in the RESTRICTED homogeneous equations only. No quantitative neighborhood, global branch uniqueness, native full sourced solution or physical matter density follows. The full inhomogeneous Euler system can impose further equations; homogeneous restriction cannot erase them.

At k=0 the stationary branch collapses to a=b=lambda1=lambda2=0 and the displayed constant-family Hessian vanishes. This says nothing about nonzero-momentum native mixed blocks or different backgrounds. Inverting(2) and taking k=0 is inadmissible.

The response obstruction is therefore not universal across source-shaped actions: the selected I1 completion supplies nonzero coupled response on its genuine stationary products. It does not repair K2527 by addition: no typed identification of field spaces, action densities or observation maps has been supplied. The concrete next construction is the source-localization/observed metric demand on this seed, or a Met(X)-compatible stationary distortion solving its full equations; the two are different candidates. The product's failed pure-normal graft and connection-preserving S2T*X identification remain failed. A full finite-momentum coupled calculation is needed before any Green/PPN inference; missing native ownership remains open rather than a GU kill.

## 6. Executed source-localization successor: tension and its domain demand

Replace the unspecified source by an explicitly SUPPLIED action, not a claim that the GU source selected it. On the totally geodesic Lorentzian4 observer X, take

    S_X[G,s]=-epsilon tau0 integral_X dmu_(s*G), tau0!=0.

Use a boundaryless embedded observer or compactly supported tests inside an embedded tubular patch, away from any worldvolume boundary. This is a local first-variation statement; no finite global noncompact volume is assumed. Expand about the already stationary ambient I1 seed at epsilon=0. The metric variation is

    delta S_X=-(epsilon tau0/2) integral_X tr_gamma(s*H)dmu_gamma.

With the source convention in(4), the leading metric covector is therefore

    j_X(H)=(tau0/2) integral_X tr_gamma(s*H)dmu_gamma, j_T=0. (8)

The independent-T statement uses the declared field coordinates; all source components transform covariantly under reparametrization. The action also has an embedding equation: normal displacement changes volume by minus the pairing with the mean-curvature vector, so its stationary condition is tau0 mean=0. Here II=0 implies mean=0. Tangential variations are total divergences. For a compact ambient vector test V, tr_gamma s*(Lie_V G)=2 div_X V_tangent minus2<mean,V_normal>. Integration by parts proves j_X(Lie_V G)=0. Thus the leading distributional source obeys the metric diffeomorphism conservation identity on this seed. A boundary would add an edge term and cannot be dropped.

Under first-factor scaling the observer volume changes by exp(4x), giving derivative -4tau0 per observer volume. This is not a numerical j_x for the bulk density(1): the4D and14D measures differ and an undefined noncompact volume ratio cannot identify them.

This is an actual source/readout variational construction with zero-thickness codimension10 support. It is NOT a smooth ambient source. For any local finite-order full I1 linearization L with smooth coefficients at this seed, a smooth perturbation z gives a smooth Euler density Lz. If Lz=j_X as distributions, then Lz vanishes off X. Its continuity and the dense complement of X force it to vanish everywhere. But(8) is nonzero: H=chi G with nonnegative compact chi positive on part of X gives j_X(H)=2tau0 integral_X chi dmu_gamma !=0. Contradiction.

Consequently this supplied source cannot be answered by ANY smooth perturbative full-field response, including the homogeneous four-coordinate family. This is a regularity obstruction for a singular source, not an exclusion of distributional solutions, nonlinear solutions or native GU. It neither contradicts the finite-coordinate inverse nor turns that inverse into a Green operator. A nonzero-momentum/common-domain distributional response and the embedding variations must be constructed; alternatively a finite-thickness profile is a changed physical input with its own normalization and equations. A guessed smooth profile is not automatically admissible: its normal transport and additional stresses must preserve the source/embedding Noether identity. The indefinite normal signature(6,4) supplies no canonical positive radial Gaussian. No such profile, transverse-volume ratio or compactification is silently fitted here. The action above is a conditional probe source, not an accepted ordinary-matter model. The next native response question now has a precise source and domain demand.

## Reproduction and evidence

The probe differentiates(1) directly, verifies the old stationary seeds, reconstructs radial blocks and exact Schur/contact/source equations, then uses polynomial remainders for all nonradial branches and the paired discriminator. Branch theorems and full first-variation admissibility are reused from K2519; finite-sector response is the new computation. Contrary controls challenge fixed-displacement inversion, pre-substitution, factor-blind readout and k=0 inversion. The analytic local-family consequence uses the stated finite-dimensional theorem and hypotheses. The tension-source first variation, compact-test Ward identity and dense-complement argument establish the source-localization boundary; finite determinant and volume checks do not replace that proof. Dependency hashes/report equality are provenance only. LT-GR6b/GR10/GR11, source register, ledger0.263, canon and public posture remain unchanged. Internal independent review is not external-expert, proof-assistant or novelty certification.
