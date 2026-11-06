---
title: "K2617 Interior pressure identification and explicit contact receivers"
status: active_research
doc_type: exploration
created: "2026-11-06"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: analytic compact-source uniqueness and mathematical contact recovery; no exterior or physical receiver theorem
scripts:
  - tests/channel-swings/k2617_interior_pressure_identifiability_probe.py
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
result: K2617
carrier: full selected curved-product metric responses and compact reduced-support conserved isotropic radial pressures LAYER=toy CHIRALITY=N/A
pairing: full tensor distribution-test duality and separately positive scalar Gram density ON=declared_carrier
real_structure: real kappa nonzero, analytic actual tube operators and smooth real source model
grading: complete interior observations, contact receivers and exterior observations remain distinct
action_owner: repository-construction -- selected comm/symi/symi completion
target: compact-source uniqueness and preparation-independent finite-model recovery MAP-TYPE=evaluation
```

# Interior observations recover what exterior observations cannot

## Result and source boundary

In the same selected curved-product completion as K2611, complete INTERIOR conserved metric observations distinguish every smooth conserved isotropic-normal pressure with compact reduced support. Sources may depend jointly on radial A and B coordinates; no common radial-profile factorization is required. Responses may use different homogeneous preparations. More strongly, an explicit family of contact receivers recovers the coefficients of any known finite-dimensional smooth source model, without computing a Green response or choosing a homogeneous preparation.

This changes the receiver class. K2611's complete EXTERIOR observation kernel survives unchanged. Our receivers may enter the source region, and their mathematical availability is not a physical access or apparatus claim. Common-profile exterior uniqueness, physical source restrictions and actual calibrated detector implementations remain open.

The proof uses the actual contact polynomial from K2548/K2605 and analytic noncharacteristic uniqueness, not ellipticity of the indefinite B operator. SC-ACT-01/02 ASSERTS their action/equation, SC-GEO-03 ASSERTS Met(X), SC-GEO-55 ASSERTS gauge-rotated Levi-Civita displacement, and SC-META-53 remains UNCERTAIN. No typed identification of this completion with those native objects is supplied. Source, ledger0.263 LT-GR1b/6b/10 and LT-SM8, canon and positive-energy/causal-domain debts are unchanged.

## 1. Keep the complete coupled contact identity

Use the actual radial pressure source j with AA blocks A/2 in the four observer directions and P/2 in the three normal directions, no B or mixed components. On a regular radial shell,

    alpha=C'/C, A=P+P'/(4alpha),
    t=(4A+3P)/2=7P/2+P'/(2alpha),
    X=partial_r²+(4alpha+2beta)partial_r,
    w2=C^4 S_A^2>0, beta=S_A'/S_A, Y=Box_B.

P may depend smoothly on both r and B. Its B dependence does not add a B divergence to an AA-only stress on this direct product. The same radial conservation equation therefore applies pointwise in B. Initially assume compact support in a regular r shell times a compact interior B set. Smooth regular-center sources with compact outer support are also covered below; arbitrary center-supported distributions are excluded.

Let E be the formally self-adjoint linearized Einstein map, G_A the A metric block, d the actual six-potential determinant, and F its scalar source-contact polynomial. K2548's full adjoint identity gives, for EVERY full distributional response h and every fully compact scalar test phi,

    <h,E(G_A d(X,Y)phi)>=-<t,F(X,Y)phi>,
    Z=tr_A(Eh), d(X,Y)Z=-F(X,Y)t.                           (1)

The compact adjoint calculation uses div_A j=0 to remove its A-Hessian pairing. It does not assume that j factors as a single radial profile times a B function, nor that h lies in the six-potential ansatz. Full TT, skew and auxiliary equations remain in the antecedent. X here denotes the full A scalar operator on tests; it reduces to the displayed radial operator on the observer-invariant source. Apply d and E to the ENTIRE cutoff-weighted test, retaining all derivatives of cutoffs.

## 2. Actual radial principal coefficient

At kappa=1 reconstruct d=P5(X+Y)+XY Q2(X+Y) from K2554 and F=c d+R from K2605, where c=-424853/149354 and R is the saved degree-four-in-Y remainder. Its total-degree-five homogeneous part is

    F5(X,Y)=aY (X+Y)^4[(31425/41594)X+Y],
    aY=7412316633293468946137088/22521658027326625.

In particular

    aX=[X^5]F=224005433669517008830464/900866321093065 !=0. (2)

The probe checks this reconstruction and independently recomputes the coefficient from the original six-row determinant/cofactor at Y=0. K2600's actual scaling F(kappa²X,kappa²Y;kappa)=kappa^5 F(X,Y;1) makes the coefficient of partial_r^10 equal kappa^-5 aX, nonzero for every admitted real kappa!=0. This is not a claim that the full principal symbol is elliptic; it has characteristic directions.

The actual C,S_A coefficients are analytic away from the center and focal endpoints; the B space-form operator has analytic coefficients in analytic charts. Thus F(X,Y), restricted to source dependence on r and B, is an analytic-coefficient differential operator of order ten, and every r=constant surface in a regular shell is noncharacteristic by(2).

## 3. Interior injectivity by a maximal-support argument

Suppose all compact interior Einstein receivers E(G_A phi) read zero. Then Z=0 as a distribution, so(1) gives Ft=0. If t is nonzero with compact reduced support, choose a point of its support with maximal radius r*. It vanishes on the outward side of r=r*. Holmgren uniqueness across that analytic noncharacteristic surface implies that this point is NOT in its support, a contradiction. Therefore t=0.

The imported theorem is the distributional form: analytic operator coefficients and a noncharacteristic local hypersurface, together with Pu=0 and u zero on one side, imply local vanishing. The source need not be analytic. See Laurent and Léautaud, *Unique continuation and applications*, section1.2.3, Theorem1.2.4, printed p.12 ([author-hosted text](https://laurentca.perso.math.cnrs.fr/papiers/UCPApplications.pdf)). K2556 previously used this maximum-support principle for different B factor operators; the present application checks the actual mixed F and its radial principal symbol.

For smooth regular-center sources, a nonzero trace has a positive maximal radius, so the same proof applies away from the center. Once t=0, radial conservation gives P'+7alpha P=0. Since alpha=C'/C, (C^7P)'=0. The outer zero collar forces P=A=0, with continuity extending to the center. The shell argument also works for distributional t with compact reduced support entirely in the regular shell; the finite-model receiver construction below is stated for smooth sources only.

Apply this to the difference of any two sources and full responses. Identical complete interior observations force identical sources even when the responses differ by unknown homogeneous additions. The statement presupposes actual full responses; it does not assert existence for every source, arbitrary-data inverse solvability, well-posed radial evolution, or uniform all-source stability. In particular Y is not replaced by a scalar in a radial ODE.

## 4. Explicit finite-model contact reconstruction

Let j_1,...,j_n be known linearly independent smooth admissible pressure sources, compact in a common regular shell and interior B set, with traces t_i. Set

    g_i=F(X,Y)t_i.

The trace map is injective by conservation and the outer collar. Section3 proves F injective on this compact class. Hence the real smooth compact g_i are linearly independent.

Choose nonnegative smooth compact cutoffs in the invariant observer and A angular coordinates, with positive factor integrals normalized to one, and denote their product by chi. The reduced source and g_i are independent of these coordinates. Define

    phi_i=chi g_i,
    D_i=E(G_A d(X,Y)phi_i),
    G_ij=integral g_i g_j w2(r) dr dvol_B.                    (3)

The scalar measure in G is the positive volume density (absolute metric determinant); it is not a positive physical energy or the indefinite tensor action pairing. The full scalar X acts on chi as well as g_i in D_i. All cutoffs remain inside d and E. Locality keeps D_i compact in the source's reduced support; the linearized Bianchi identity makes it conserved.

For any full response to j=sum_j c_j j_j, integration by parts in(1) gives

    y_i=<h,D_i>=-sum_j G_ij c_j.                            (4)

The positive scalar Gram matrix is strictly positive definite by linear independence. Thus c=-G^-1 y. Every homogeneous full-system addition cancels from(4). No boundary Green operator, common preparation, fitted inverse or numerical PDE solution is required to DEFINE these receivers. This is an explicit differential-and-integral construction from a declared source basis, not a numerical curved receiver bank.

Whiten the potentials using phi_tilde_i=sum_k (G^-1)_ik phi_k. Their readings are exactly -c_i. The sensors depend on the known model, not the unknown coefficients. If raw scalar readout error is epsilon, the coefficient error obeys

    ||c_hat-c||_2 <= ||epsilon||_2/lambda_min(G).             (5)

Whitening transfers the same possible amplification into the detector norms; it does not remove conditioning or provide a physical noise model. For a perturbed calibrated matrix G+Delta, ||Delta||_2<lambda_min(G) gives inverse norm at most1/(lambda_min(G)-||Delta||_2). This is a finite-model bound with its actual Gram eigenvalue, not a uniform infinite-dimensional estimate.

Exactly n scalar linear measurements suffice on this n-dimensional model. Fewer than n cannot recover an open coefficient neighborhood: the baseline transcript of a deterministic adaptive linear scheme fixes fewer than n rows, leaving a nonzero null direction; sufficiently small moves along it preserve the transcript and stay inside the neighborhood. This lower bound concerns exact deterministic scalar linear readings. No randomized or discontinuous nonlinear-sensing theorem is added.

### An actual disjoint-shell source family

The construction can be instantiated without an unknown Green kernel. Choose n pairwise disjoint closed radial intervals [r_i-epsilon_i,r_i+epsilon_i] strictly inside the regular tube, and one nonzero real smooth compact B chart bump psi. Put beta(t)=exp(-1/(1-t²)) for |t|<1 and beta(t)=0 otherwise, and

    P_i(r,B)=beta((r-r_i)/epsilon_i) psi(B),
    A_i=P_i+partial_r P_i/(4alpha).

These are actual smooth compact conserved pressures in the declared completion. They need not have nonnegative A_i or physical energy. Their traces are nonzero by the integrating-factor argument. Locality keeps g_i=F t_i in disjoint radial shells, and uniqueness ensures every g_i is nonzero. Thus their contact Gram is DIAGONAL with G_ii=integral g_i² w2 dr dvol_B>0, and the individual receiver -D_i/G_ii reads c_i exactly for every full response. This supplies a concrete arbitrary-n source/readout family and eliminates cross-shell matrix inversion. It does not evaluate those positive curved integrals numerically or bound them uniformly as shells narrow; radial derivatives and whitening may make receiver norms large.

## 5. Why the result neither conflicts with nor repairs exterior invisibility

For K2611's compact responses, receivers outside the B support still read zero. Equation(4) uses contact access. Applying a support cutoff AFTER E or after d would generally destroy conservation or the identity, and is not allowed. A compact support set may have internal holes; no claim about arbitrary sensor placement inside every hole is made.

If the outer support condition is removed, t=0 can have P=C^-7, A=-3P/4; this conserved nonzero trace-zero pressure defeats the trace step. If the actual radial principal coefficient were zero, r=constant could be characteristic and the chosen Holmgren argument would fail. If coefficients were merely smooth, this analytic uniqueness theorem could not be invoked. The probe keeps these contrary controls distinct from the actual hypotheses.

The exact probe checks the actual polynomial/principal coefficient and conservation, then exercises Gram recovery, whitening, noise and rank controls in an explicitly labeled finite algebraic fixture. It does not numerically integrate actual curved compact-source Gram entries or certify physical receiver manufacture. The universal PDE statement is the written argument with its imported uniqueness theorem; finite pass totals do not replace it.

Next identify physically justified contact access, evaluate an actual chosen smooth-source Gram matrix with justified readout norms, or settle common-profile EXTERIOR uniqueness. Neither the old exterior kernel nor the new interior injectivity selects a native GU matter coupling or physical preparation.

[K2548 full contact identity](k2548-compact-coupled-metric-detectors-2026-11-04.md), [K2556 prior analytic uniqueness](k2556-distributional-source-response-2026-11-05.md), [K2605 actual cofactor](k2605-source-disjoint-pressure-response-2026-11-06.md), [K2611 exterior kernel](k2611-fixed-preparation-invisible-pressure-2026-11-06.md), [probe](../../tests/channel-swings/k2617_interior_pressure_identifiability_probe.py), [report](../../lab/process/k2617-interior-pressure-identifiability.json).
