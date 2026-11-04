---
title: "K2541 Prescribed product-source response and singular original readout"
status: active_research
doc_type: exploration
created: "2026-11-04"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: full local distributional response for prescribed A-homogeneous source and scoped singular-readout bound; no observer-localized, global Green or native GU claim
scripts:
  - tests/channel-swings/k2541_prescribed_product_source_response_probe.py
---

# K2541 Prescribe the source before constructing the fields

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
result: K2541
carrier: independent ambient symmetric metric and End(V) grade-one displacement on the fourteen-dimensional stationary Einstein product LAYER=toy CHIRALITY=N/A
pairing: inherited indefinite symmetric/skew contraction with compact-support differential adjoints ON=declared_carrier
real_structure: real signature (7,7), kappa nonzero, locally symmetric product
grading: prescribed source, scalar potentials, tensor response, original metric and observation remain distinct
action_owner: repository-construction -- selected comm/symi/symi I1 completion with moving soldering
target: prescribed order-zero product-source response and local distributional readout MAP-TYPE=evaluation
```

## Result and exact source boundary

The full system in [K2539](k2539-covariant-tensor-constraints-2026-11-04.md) admits local distributional solutions for the PRESCRIBED source j=J(B)G_A, including an order-zero delta distribution on B. Adding a scalar Hessian to the two-volume tensor ansatz closes the response equations and reduces them to three second-order scalar solves. The original metric is reconstructed, and its A-factor coefficient for the delta source necessarily lacks a locally square-integrable representative. Distributional existence therefore does not deliver ordinary continuous evaluation at the source.

This source is homogeneous in A, rather than supported on the four-dimensional observation section. It is NOT the [K2531](k2531-partial-thickness-source-2026-11-04.md) thin tension or partial-width stress, which also has A-normal structure. The construction is a concrete prescribed-source control and a scalar response method, not a solution of that different source. No source is fitted from a chosen response.

SC-ACT-01 ASSERTS its first-order action, SC-GEO-55 ASSERTS displacement from gauge-rotated Levi-Civita, and SC-GEO-03 ASSERTS Y=Met(X), distinct from the independently varied ambient metric here. SC-META-53 remains UNCERTAIN about indefinite spectra. Their polarities, ledger0.263 GR6b/10/11, and native Met(X)/physical-quotient/observed-gravity debts remain unchanged.

## 1. An actual prescribed conserved input

Use the same locally symmetric Einstein product A×B, with both factors seven-dimensional and Ric=lambda G, signature(7,7) total and signature(3,4) on B. Kappa is a fixed nonzero real number. Retain every K2537 coefficient:

    a0=-5kappa/2288, lambda=35kappa²/604032,
    m=158kappa/143, beta=-15kappa/143,
    mV=503kappa/858, mH=893kappa/858.

Let J be any distribution on a small B chart, extended constantly along A. Define j=J G_A. Because G_A is parallel and its raised index is tangent to A, div j=0 distributionally. Its B and mixed components vanish. Choosing J=delta_q is an order-zero source, not derivatives of a delta; its support has codimension7 and extends across A.

The response fields are now unknown. Set

    C=f G_A+g G_B+Hess_B s, K=0,
    D=Box_B, tau=7(f+g)+D s,
    v_C=-7df-6dg+lambda ds, w=11v_C.

Since w is an exact gradient, dw=0, and the complete skew equation holds. Hess_B s is a symmetric tensor on B, not an added metric source or a gauge quotient. While E(Hess_B s)=0 by the Einstein diffeomorphism identity, its tensor mass and hook terms do not vanish.

## 2. Close the full tensor operator with curvature retained

For a scalar s on B, constant sectional curvature lambda/6 gives

    div Hess s=dD s+lambda ds,
    Box Hess s=Hess D s+2lambda Hess s-2 Riem(Hess s),
    Riem(Hess s)=(lambda/6)[G_B D s-Hess s].

Substitution into K2539's full hook formula yields

    S(Hess s)=(2lambda/13)G_A D s
                -(7lambda/39)[G_B D s-Hess s].

This explicitly retains curvature; a flat symbol cannot supply this column. Define

    MA=m f+7beta(f+g)+lambda(5f+7g)/(6a0),
    MB=m g+7beta(f+g)+lambda(7f+5g)/(6a0),
    RA=-121(7f+6g)/(13mV)-24(f-g)/(13mH)+(f+g)/a0,
    RB=-121(7f+6g)/(13mV)+28(f-g)/(13mH)+(7f+5g)/(6a0),
    u=beta+121lambda/(13mV)-4lambda/(13mH),
    w0=beta+121lambda/(13mV)+14lambda/(39mH),
    zeta=m-121lambda/(13mV)-14lambda/(39mH).

Then the COMPLETE symmetric tensor equation reads

    F_C=G_A[MA+D RA+u D s]
        +G_B[MB+D RB+w0 D s]+Hess_B[-RB+zeta s].

There are no omitted mixed components. It is sufficient to set these three coefficients to (-J/(6a0),0,0). This defines a 3×3 polynomial matrix M(D) on (f,g,s). It is a sufficient construction, not an iff classification: special scalar Hessians proportional to G_B can make the representation redundant. No unique parametrization or exhaustive response count is inferred.

Exact algebra gives

    P(D)=det M(D)
    =-[3094302258846107172864 D²
       +48852605799064661880 D kappa²
       +19514973635487875 kappa⁴]/(38093115957811200 kappa).

For p=adj(M)e1 its components are

    p_f=(-121558485114114048 D+97712717036293 kappa²)
          /253954106385408,
    p_g=7(116625596252166144 D+153233472236795 kappa²)
          /1269770531927040,
    p_s=-10607043027/17967160.

M p=P e1 is an exact polynomial identity. The nonzero Hessian component is essential; dropping it leaves a nonzero third equation for a generic prescribed source. The two roots of P are real, distinct and negative (in D/kappa² approximately -0.0153778030 and -0.0004101200); the exact discriminant and signs, not these decimals, establish the claim. Neither is -2lambda/kappa². P(0) is nonzero. These are scalar factorization facts, not physical masses or positive-energy modes.

## 3. Solve the full forced system, keeping original h

Choose scalar local solutions

    P(D)U=J, (D+2lambda)V=J.

Set

    (f,g,s)=-p(D)U/(6a0),
    z=5V/(72a0)[G_A-(7/5)G_B],
    h=z-C/(6a0), e2=-A2^-1 BQ, Q=C+K.

The auxiliary symbols A2,B refer to K2537's previously derived operators, not the product factors. All other reduced grades vanish under K2535's full grade preservation. The polynomial identity proves F_C=-j/(6a0). Independently, for z=uA G_A+vB G_B the Einstein blocks are

    (Ez)_A=G_A[3D(uA+vB)+lambda(5uA+7vB)/2],
    (Ez)_B=(G_B D-Hess_B+lambda G_B)(7uA+5vB)/2.

The chosen coefficients therefore give Ez=-j/(12a0), exactly the other forced equation. This checks both sectors against the SAME prescribed J; h includes the tensor correction.

A common master form is also available: solve (D+2lambda)P(D)chi=J and set U=(D+2lambda)chi, V=P(D)chi. It is a construction, not a boundary prescription. For regularity it is better to solve U and V separately on a common smaller chart.

## 4. Justify local distributional existence

For each second-order factor, the principal symbol is, up to a nonzero constant, G_B^{ij}xi_i xi_j. At a nonzero characteristic covector its xi-gradient is 2G_B^{-1}xi, which is nonzero because G_B is nondegenerate. Smooth lower-order curvature and mass terms preserve these hypotheses. Lerner's real-principal-type local-solvability theorem, with its Sobolev definition, therefore gives a local solution gaining one Sobolev derivative per factor. Apply it sequentially to the two factors of P, shrinking charts, and separately to D+2lambda. [Definition1.2.26 and Theorem1.2.38, printed pp43,49](https://webusers.imj-prg.fr/~nicolas.lerner/ch1booklerner.pdf).

Specifically, J in H^s_loc admits U in H^(s+2)_loc and V in H^(s+1)_loc on a common smaller neighborhood; then C,h are in H^s_loc and e2 in H^(s-1)_loc. These are nonsharp existence bounds. A general distribution has some finite local negative Sobolev order after localization. In seven dimensions delta_q belongs to H^s_loc for every s<-7/2, so this includes the prescribed point distribution. For smooth J one may choose a fixed s>7/2 to obtain a continuous h on a smaller chart; this does not claim a single solution in all Sobolev spaces merely by changing s.

Do NOT apply the theorem directly to the sixth-order product: its repeated principal characteristic has zero xi-gradient on the null cone. Sequential solvability avoids that invalid inference. No global inverse, common self-adjoint boundary domain, causal support, uniqueness or physical positivity is selected. Local solvability is an actual existence result with a narrower conclusion than those missing structures.

## 5. Follow through to the ORIGINAL singular readout

The A-factor coefficient of h is

    hA=5V/(72a0)+p_f(D)U/(36a0²).

Every U,V in this construction consequently satisfies

    P(D)(D+2lambda)hA=N_A(D)J,
    N_A=[-111470108038212059136 D²
          +23443121698297931487 D kappa²
          +9086860628609870 kappa⁴]/(549419941699200 kappa²).

The degree-two leading coefficient is nonzero and gcd(N_A,P(D)(D+2lambda))=1. In formal large-D terms the response starts with [559559/(224031kappa)]D^-1; this is algebraic order bookkeeping, not a chosen pseudodifferential inverse or a physical coupling measurement.

For J=delta_q, N_A(D)delta_q has nonzero order-four principal derivative of delta. In local coordinates its Fourier transform has a degree-four leading polynomial, nonzero on an open cone; lower-order terms and smooth density factors cannot cancel it. Radial integration in dimension7 therefore gives exactly the local Sobolev threshold t<-7/2-4=-15/2. If hA were in H^r_loc, the smooth order-six operator on the left would lie in H^(r-6)_loc. Necessarily

    r-6<-15/2, hence r<-3/2.

In particular hA cannot be locally L2, and cannot have a continuous representative near the source. This is a necessary regularity obstruction for the original coefficient in this constructed family, not merely failure of a sufficient wavefront criterion. It does not prove that every conceivable renormalized, smeared or directional trace is impossible. Off-source singular propagation and a physical observation rule remain separate problems. Adding smooth homogeneous fields cannot remove this necessary bound because the same forced identity persists.

## Evidence and remaining scope

The written curvature computation and polynomial adjugate identity prove the reduction; a verified local-solvability theorem proves existence; the Fourier derivative-of-delta argument proves the readout bound. The exact probe checks the full matrix, Hessian curvature column, original source normalization, independent Einstein blocks, constant-source solution, determinant, lack of pole cancellation and meaningful contrary fixtures. Counts and dependency hashes are reproducibility evidence, not substitutes for these arguments. No novelty, external-expert or proof-assistant certification is claimed.

The source is now prescribed before solving, so the generated-source limitation is removed for this A-homogeneous class. Extending to the actual K2531 observer-localized source needs its A-normal dependence and tensor types; it cannot be inferred by copying this scalar inverse. A global or boundary-selected response and a defined singular observation require additional input. These remain concrete next constructions, with the present class available as a full-equation positive control.
