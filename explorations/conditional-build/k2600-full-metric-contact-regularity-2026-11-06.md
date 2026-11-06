---
title: "K2600 Full metric contact regularity and normalized conserved detectors"
status: active_research
doc_type: exploration
created: "2026-11-06"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: full selected-system necessary local metric bounds and compact contact sensitivity; no sufficient regularity or physical detector
scripts:
  - tests/channel-swings/k2600_full_metric_contact_regularity_probe.py
---

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
result: K2600
carrier: full original metric and displacement distributions on the selected stationary Einstein product with compact conserved radial A pressure and B atom LAYER=toy CHIRALITY=N/A
pairing: invariant distribution-test tensor contraction; auxiliary positive component norms solely for bounds ON=declared_carrier
real_structure: real nonzero kappa, product signature7+7 and local smooth charts
grading: scalar test potentials, total metric including TT, source-contact observations and physical gauge remain distinct
action_owner: repository-construction -- selected comm/symi/symi first-action completion
target: universal full-metric necessary regularity and normalized compact conserved contact readout MAP-TYPE=evaluation
```

# The full coupled response retains a contact singularity

## Result, distinction and scope

K2598 proved a scalar-source coefficient obstruction and a two-slot tensor projection restricted to that source sector. It explicitly left the TT addition for a GENERAL compact pressure source open. Here the full coupled compact-adjoint identity of K2548 bypasses the scalar/TT split entirely. The ACTUAL highest source coefficient is nonzero and independent of the A spectral variable. Every full distributional solution for the nonzero conserved compact radial pressure times an interior B atom therefore fails local component Lp for p>=7/5 and the stated anisotropic H^-3/2 condition. No choice of homogeneous preparation or TT cancellation repairs those bounds.

This supplies necessary bounds, not sharp sufficient regularity. A family of compact conserved detectors of unit auxiliary L2 norm has divergent atomic contact signal of order epsilon^-3/2. Smooth approximations have strong-norm lower bounds while each FIXED smooth detector has a finite convergent signal, with O(epsilon²) error for centered mollification. These are mathematical contact observations; a physical apparatus, positive noise covariance, source-disjoint gravitational readout and source-native action bridge are not supplied.

SC-ACT-01 ASSERTS its source action, SC-GEO-55 ASSERTS displacement from gauge-rotated Levi-Civita and SC-GEO-03 ASSERTS Met(X). The independent ambient-metric selected completion here is not identified with them. SC-META-53 remains UNCERTAIN about indefinite spectra. Ledger0.263 LT-GR1b/6b/10 and LT-SM8, source polarities and canon stay unchanged. No novelty, external-expert or proof-assistant certification.

## 1. Use an identity valid for every full solution

Reuse K2548's actual curved six-potential matrix M(X,Y;kappa), X=Box_A,Y=Box_B, a0=-5kappa/2288, and Einstein linearization E. Put

    d=det M, e=coefficients of E(G_A phi), b=adj(M)e,
    F=d/(12a0)-b_f/(36a0²), D_phi=E(G_A d phi).

For any compact smooth phi and EVERY full distributional selected-system solution (h,Q) with conserved j=j_A tensor mu_B, K2548 proves

    <h,D_phi>=-<t_A mu_B,F(X,Y)phi>, t_A=tr_A j_A.       (1)

The Hess_A source term vanishes by div_A j_A=0 and compact integration by parts. No ansatz on h or Q, division by d, separation of response bases, boundary selection or Green inverse enters (1). The test construction uses the full skew row and curved Hessian terms. All extra TT fields are already included in h.

The actual nonzero radial source has t_A=(4A+3P)/2 and P'+4(C'/C)(P-A)=0. If t_A vanished, A=-3P/4 would give P'+7(C'/C)P=0; the compact outer condition forces P=A=0. Thus a nonzero source has a nonzero smooth trace. A compact A test eta with c_eta=<t_A,eta>!=0 exists inside a regular chart, without tangentially cutting off the source.

## 2. Execute the principal cofactor calculation

The probe reconstructs M from its six curved equations and computes all six Cramer determinants for e. It checks M b=d e as a polynomial identity, and independently matches d to K2554's saved determinant. Write L_d=[Y^5]d. At kappa=1,

    degree_Y d=5, degree_Y F=5,
    [Y^5]b_f/L_d=-637905/105145216,
    [Y^5]F/L_d=-424853/149354.                         (2)

Both L_d and F_5=[Y^5]F are CONSTANT in X. The full scaling, checked against the actual matrix, is d(kappa²X,kappa²Y;kappa)=kappa^6 d(X,Y;1) and b_f scales as kappa^7, hence

    F_5/L_d=-424853/(149354 kappa)!=0.                 (3)

The original-metric shift in F is essential. Omitting it changes the principal coefficient. The detector D_phi has B differential order12: its AA volume coefficient has principal term 3L_d Y^6 phi and BB volume term (7/2)L_d Y^6 phi; the B Hessian slot contributes order12 as well. No fourteen-dimensional isotropic estimate is substituted for this B scaling. A derivatives hit the fixed eta and enter constants.

## 3. Full metric Lp obstruction from shrinking compact tests

Fix an interior B source point b0 and a coordinate covector xi with nonzero wave principal form q_b0(xi). Choose a compact smooth phi on the B coordinate chart that agrees with (xi dot z)^10/10! near0, and set phi_epsilon(A,z)=eta(A)phi(z/epsilon). Then (1)--(3) give

    <h,D_epsilon>=-F_5 c_eta q_b0(xi)^5 epsilon^-10
                     +O(epsilon^-9).                 (4)

Normal-coordinate lower-order coefficients and lower Y powers contribute lower orders. The sign is immaterial for the norm consequence, but is retained in the exact probe. Every D_epsilon is smooth, compact, conserved (div E=0), and its support in B shrinks to b0. In a fixed auxiliary positive component norm with invariant density equivalent to chart measure,

    ||D_epsilon||Lp' <= C epsilon^(7/p'-12).           (5)

Hölder on K_A times the shrinking B ball implies, for any locally Lp metric,

    ||h||Lp(K_A x B_Cepsilon) >= c epsilon^(7/p-5).    (6)

For p>7/5 the right side diverges while the local norm is bounded. At p=7/5 it is bounded below by a positive constant while absolute continuity of the integral forces the left side to zero. For p=infinity it contradicts local essential boundedness directly. Thus no such full solution is locally component Lp near the chosen nonzero trace/source patch for ANY p>=7/5. This does not assert failure at every A point, and does not claim existence or sufficiency below that threshold. K2594 separately supplies a prepared distributional full solution.

## 4. Critical anisotropic Sobolev obstruction

The negative statements are h not in L2_A H^(-3/2)_B and h not in ordinary local H^(-3/2)(A x B) on a relatively compact product patch containing a nonzero tested trace. These are distinct spaces, both excluded by the same test sequence; no equivalence is claimed. The sequence T_epsilon=epsilon^10 D_epsilon is bounded in L2_A H^(3/2)_B: a B derivative of order12 has norm O(epsilon^(7/2-12-3/2)); multiplication by epsilon^10 cancels that exponent. Lower terms remain bounded, using local smooth coefficients and a fixed A test.

Furthermore T_epsilon converges weakly to0 in that positive Sobolev space. Against smooth compact dual tests, move all B derivatives onto the fixed test by integration by parts. Their pairing tends to0, with the factor epsilon^10 and shrinking support. Boundedness and density of smooth dual tests extend this to all L2_A H^(-3/2)_B tests. If h belonged to that space, <h,T_epsilon> would tend to0. Equation(4) gives a nonzero limit instead. Every stronger local B-Sobolev regularity embeds into this excluded space. The same boundedness and weak convergence hold in ordinary H^(3/2)(A x B): A factors are fixed smooth compact functions and only B frequencies scale. The same density argument excludes isotropic H^(-3/2) as well. The written weak-convergence argument, not exponent arithmetic alone, establishes both critical endpoints.

## 5. Smooth sources and preparation-independent blowup

Let mu_epsilon be the pushforward under z=b0+epsilon y of a fixed smooth compact probability density psi(y)dy. Relative to invariant B density rho(z)dz its density is epsilon^-7 psi((z-b0)/epsilon)/rho(z). Choose the preceding polynomial test on the entire support of psi. Then (4) holds with h_epsilon solving the smooth-source system: the highest derivative of the degree10 polynomial is constant throughout that support.

Consequently EVERY such locally Lp response has (6), even if its homogeneous preparation varies with epsilon. In particular

    ||h_epsilon||Linfinity >= c epsilon^-5,
    ||h_epsilon||L2 >= c epsilon^-3/2,
    ||h_epsilon||L^(7/5) >= c.

These are lower bounds on shrinking neighborhoods, not pointwise values or exact divergence coefficients. They do not restrict distributional convergence or conserved fixed-detector convergence.

### Critical fixed-patch norms also diverge, without a claimed rate

The critical shrinking-ball bound alone is only a positive constant. A separate compactness argument yields more. Fix a product patch whose interior contains a nonzero tested A trace and b0, and a cutoff equal to one on a smaller such patch. For ANY family of smooth-source solutions as above, their fixed-patch L^(7/5) norms tend to infinity. If a sequence epsilon_j tending0 had bounded norms, reflexivity would give a weakly convergent subsequence h_j to h*. For every fixed smooth cofactor detector supported in the interior, pass (1) through weak convergence and mu_j tending delta. Thus h* satisfies the atomic contact identity for all those tests. Section3 rules out an L^(7/5) field with that identity, a contradiction.

Exactly the same argument in the local Hilbert spaces H^(-3/2), and L2_A H^(-3/2)_B, proves divergence of their fixed-patch cutoff norms. Use weak compactness and then section4 on detectors supported where the cutoff is one. No convergence of Q or common boundary preparation is required: only the metric contact identity passes to the limit. This proves divergence, not a logarithmic/power rate at these critical norms, and does not assert that the smooth-source solutions have finite norms to start with. Infinite norms already satisfy the conclusion.

## 6. Released normalized detector and conditioning consequences

For the atomic source choose the same test phi and define d_epsilon=D_epsilon/||D_epsilon||L2. The norm has the actual asymptotic order epsilon^-17/2. To see the lower bound as well as (5), rescale B; the AA leading term is 3L_d eta q_b0(partial)^6 phi. This is nonzero: a nonzero compact smooth phi cannot solve a nonzero constant-coefficient polynomial equation, since its Fourier transform is entire and vanishes on the open set where the polynomial is nonzero only if identically zero. Smooth coefficients converge under rescaling. Thus

    ||d_epsilon||L2=1,
    |<h,d_epsilon>| is of order epsilon^-3/2.         (7)

These detectors remain compact and conserved. K2548's identity annihilates every homogeneous full-system response, so changing boundary preparation cannot change their signal. Also E annihilates formal infinitesimal diffeomorphisms, making (1) invariant under addition of such distributional metric variations whenever the dual pairing is defined. This is a property of the linearized observable; it neither admits that variation into a chosen physical domain nor identifies arbitrary displacement symmetries as physical gauge.

More generally, for each fixed s>=0 the same rescaling gives ||D_epsilon||H^s of order epsilon^(-17/2-s). Normalizing in H^s gives atomic (and matched smooth-source) signal of order epsilon^(s-3/2): divergent for s<3/2, nonzero finite leading magnitude at equality, and tending0 for s>3/2. The nonzero AA principal component proves the norm lower bound. An H^-s field-error bound delta gives observation error at most delta, so resolving this detector family requires that error to be small relative to epsilon^(s-3/2). This is detector-dependent mathematical conditioning, not a uniform bound over all tests or a physical sensor claim.

For error estimates below, identify the detector covector using the invariant density and tensor contraction, and use the dual auxiliary norm to the chosen positive field norm. Thus no indefinite contraction is silently treated as a positive norm. The same dual-norm convention applies to H^s/H^-s; arbitrary unrelated chart norms would introduce a fixed equivalence constant.

For any local L2 error tensor e, |<e,d_epsilon>|<=||e||L2. Equation(7) therefore exhibits an unbounded contact functional on L2-unit conserved tests for the atomic response. Interpreting this as experimental signal-to-noise would require a specified noise law, detector coupling and preparation cost. No such interpretation is made.

For a FIXED smooth D_phi, set g_phi(z)=<t_A,F(X,Y)phi(.,z)>_A. The signal is -<mu_epsilon,g_phi>. Taylor's theorem yields O(epsilon) convergence to -g_phi(b0); if the coordinate mollifier is centered, its first moment vanishes and the error is O(epsilon²), bounded by its second moment times a local Hessian supremum of g_phi. These constants depend on the fixed detector and are NOT uniform for d_epsilon. This proves compatibility of finite fixed-detector observations with divergent unit-norm shrinking sensitivity.

## Evidence, scope and next decision

Actual polynomial identities, conservation, gauge-null columns and scaling witnesses are checked by the probe. The universal adjoint theorem is reused from K2548, and the full metric, weak Sobolev, normalization and mollifier deductions are written proofs requiring independent review. Neither a scalar/TT basis sum nor a finite sample is offered as that proof.

Next distinguish finite-bandwidth detector stability from full local inverse regularity, or construct an independently justified physical observation/source/boundary bridge. A source-disjoint detector still vanishes in this compact-adjoint class; that exact locality limit survives. The general compact-pressure TT cancellation question is settled for these necessary full-metric bounds and must not be requeued as absent.

[K2548](k2548-compact-coupled-metric-detectors-2026-11-04.md), [K2598](k2598-full-source-singularity-2026-11-06.md), [K2594](k2594-reciprocal-distributional-response-2026-11-06.md), [probe](../../tests/channel-swings/k2600_full_metric_contact_regularity_probe.py), [report](../../lab/process/k2600-full-metric-contact-regularity.json).
