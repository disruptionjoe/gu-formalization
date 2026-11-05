---
title: "K2543 Localized-source curvature identity and finite observation"
status: active_research
doc_type: exploration
created: "2026-11-04"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: universal conditional source/curvature constraint and supplied conserved smearing; no full localized inverse, unique metric readout or native GU claim
scripts:
  - tests/channel-swings/k2543_localized_source_readout_probe.py
---

# K2543 Test the actual source without pretending to invert the whole system

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
result: K2543
carrier: original ambient metric and grade-one displacement distributions on stationary fourteen-dimensional Einstein product LAYER=toy CHIRALITY=N/A
pairing: compact smooth tensor/scalar test densities and inherited indefinite action pairing ON=declared_carrier
real_structure: real nonzero kappa, signature (7,7), selected constant radial seed
grading: original scalar curvature, displacement trace, source trace and pointwise metric pullback remain distinct
action_owner: repository-construction -- selected comm/symi/symi I1 completion with moving soldering
target: localized conserved source and linearized-diffeomorphism-invariant smeared observation MAP-TYPE=evaluation
```

## Result and source boundary

Every distributional solution of the full linear system obeys an exact ORIGINAL scalar-curvature/displacement identity. It applies to the actual codimension10 thin tension and codimension7 partial-thickness source, without substituting K2541's A-homogeneous source. It gives a precise singularity tradeoff, finite linearized-diffeomorphism-invariant smeared probes and a joint zero-width divergence. A concrete source-free solution changes the metric-only curvature probe, so the identity cannot be used to claim a uniquely determined gravitational response.

A compatible successor explicitly constructs a fully smooth conserved thickening by retaining K2531's curved normal pressure and adding a supplied positive-majorant B profile. This removes the singular-source prerequisite at fixed widths, while adding genuine source/observation data. It supplies neither the full tensor inverse nor a physical selector.

SC-ACT-01 ASSERTS its first-order action, SC-GEO-55 ASSERTS gauge-rotated-Levi-Civita displacement, SC-GEO-03 ASSERTS Y=Met(X), and SC-META-53 remains UNCERTAIN about indefinite-spectrum treatment. Their polarities and ledger0.263 GR6b/10/11 remain unchanged. The independently varied ambient metric and selected I1 completion here are not a derivation of the native metric-on-metrics theory. No source claim is falsified or promoted.

## 1. Eliminate the scalar mixing in the ORIGINAL equations

Reuse [K2537](k2537-reduced-action-decoupling-2026-11-04.md)'s actual curved action and [K2539](k2539-covariant-tensor-constraints-2026-11-04.md)'s constraints. Let

    a0=-5kappa/2288, lambda=35kappa²/604032,
    m0=-4kappa/11, mV=503kappa/858,
    tau=tr C, u=div div C-Box tau,
    Rh=delta R[h]=div div h-Box tr h-lambda tr h,
    t=tr j.

Here h is the original metric, not the shifted Einstein variable z=h+C/(6a0). The original metric equation is -12a0 E h-2E C=j. Since tr(E h)=-6Rh and tr(E C)=-6u+6lambda tau, its trace is

    72a0 Rh+12(u-lambda tau)=t.                    (1)

The original displacement equation before completing the square has trace

    m0 tau+(121/mV)u=-12Rh.                       (2)

These are full traces: no pure-trace ansatz, restriction of C or omission of its skew partner is used. The skew double divergence vanishes distributionally; K2537's exact hook trace vanishes. Eliminating u in (1)-(2) gives

    Rh-Ac tau=-Bc t,                               (3)
    Ac=41511 kappa/1735888,
    Bc=34606/(29589 kappa).

Both coefficients are nonzero. This relation does not require j to be A-homogeneous, smooth, or an image of a chosen response. Conservation remains a separate necessary condition for a full solution. The product Weyl term in the next divergence equation is NOT zero: (3) does not close a scalar PDE for Rh alone. Treating it as such would silently drop the tensor problem.

Linearized diffeomorphism invariance is exact at this seed. Rh changes by Lie_v(R0)=0 because scalar curvature is constant. The moving displacement perturbation Q has background zero and thus linear diffeomorphism variation zero; tau is also invariant. Raw tr(h) is not gauge invariant and has not been substituted for Rh.

## 2. Apply it to the actual localized source

Use [K2531](k2531-partial-thickness-source-2026-11-04.md)'s convention j(H)=(1/2) integral T:H. Its partial-width source on A times delta_q on B has

    t=(4A_epsilon+3P_epsilon)/2 tensor delta_q.     (4)

The thin source has t=2tau0 delta_X with the same tangent-weight normalization. For the actual radial branch lambda>0 and a sufficiently small positive-normal tube, nonnegative tangent A and its required pressure have the same sign, so this trace is nonzero when tau0 is nonzero. Signed sources are covered wherever the trace coefficient is nonzero.

For fixed partial width, a nonzero localized trace has exact Sobolev threshold t in H^r_loc iff r<-7/2; the thin trace has r<-5. These are inherited source thresholds, not new counts. Equation(3) now proves a COMPONENT tradeoff: Rh and tau cannot both lie in H^r_loc at or above the appropriate threshold. If tau has better regularity than t, Rh retains the contact singularity with coefficient -Bc; if Rh is smooth, tau must contain the contact term (Bc/Ac)t up to smooth remainder. More precisely, modulo any common Sobolev space, [Rh]-Ac[tau]=-Bc[t]. This does not prove h alone lacks a trace or that every component has the same singularity.

For example, if both h and C are H^q_loc, then Rh is H^(q-2)_loc and tau is H^q_loc. Necessarily q<-3 for thin tension and q<-3/2 for fixed partial width. This reproduces the general order-two common-regularity ceiling from K2531 while adding the actual scalar allocation and exact coefficients. It is necessary, not sufficient for a solution or observed pullback.

## 3. Construct a finite linearized-diffeomorphism-invariant metric probe

For any compact smooth scalar test phi, define

    L_R* phi=Hess phi-G Box phi-lambda G phi.

This is a compact smooth symmetric metric covector. Using Ric=lambda G,

    div Hess phi=dBox phi+lambda dphi,
    div(L_R*phi)=0.

Formal adjointness gives <Rh,phi>=<h,L_R*phi>, well-defined for every distributional h and invariant under h -> h+Lie_v G. Smooth density factors belong to the pairing. No pointwise pullback, positive Hilbert norm or Green inverse is used. These probes may be blind to modes with Rh=0; they are not a complete set of physical gravitational observables.

Pairing(3) supplies the finite JOINT observable

    O_phi=<h,L_R*phi>-Ac<C,phi G>=-Bc<j,phi G>.     (5)

Thus its value is determined by the source for every full solution if one exists, independent of a boundary choice. This is an action-derived identity involving both metric curvature and displacement trace. It is not a metric-only measurement or proof that a detector couples to this combination.

There is a sharp zero-width warning. For fixed partial width take a compact tangent test psi and a normalized B detector rho_delta(v)=delta^-7 rho(v/delta), with rho(0)>0; in B normal coordinates write dmu_B=w(v)dv with w(0)=1, and define the test scalar rho_delta(v)=delta^-7 rho(v/delta)/w(v), where integral rho(v)dv=1. Thus its invariant-volume integral is exactly one. If I=int psi(4A+3P)/2 is nonzero, (5) gives EXACTLY

    O_(psi rho_delta)=-Bc I rho(0) delta^-7.        (6)

For the thin source a normalized ten-normal detector analog gives delta^-10 times its nonzero tangent pairing. Hence there is no finite shrinking-detector limit for this JOINT observable on these singular inputs. Fixed-width observations remain finite. Rescaling the detector, subtracting a contact term or changing the source is a different specified observation; this result does not exclude all renormalized, anisotropic, off-source or component-specific measurements.

## 4. Prove that metric-only response is still ambiguous

[K2541](k2541-prescribed-product-source-response-2026-11-04.md) gives a full homogeneous solution with J=0, V=0 and P(D)U=0 on B, D=Box_B. Its tensor coefficients are (f,g,s)=-p(D)U/(6a0), h=-C/(6a0). Therefore

    tau= -[q1 D+q0 kappa²]U/(6a0),
    q1=30160102231/53901480,
    q0=1092838523587321/126977053192704.

The scalar polynomial P and the displayed linear polynomial are coprime; both real roots of P therefore give nonzero tau for nonzero local eigenfunctions DU=rU. Such smooth eigenfunctions exist locally: choose a nonnull geodesic polar coordinate away from its center in the space form, so the radial eigenfunction equation is an ordinary second-order ODE with nonzero leading coefficient on a small interval. Its nonzero initial data give a nonzero smooth local solution; all its angular derivatives vanish. Shrink the chart as needed.

Since (3) holds with j=0, Rh=Ac tau is then nonzero. A compact test phi can pair nontrivially with this smooth Rh. Adding this full homogeneous solution preserves the prescribed source but changes a metric-only curvature probe. The joint observable(5) stays fixed. This is an explicit original-field ambiguity, not an assumption that any arbitrary tensor can be added. A selected common boundary/initial condition remains necessary for a unique response.

## 5. Execute a conserved full-thickness repair

K2531's A stress already includes the pressure needed by curved geometry:

    P(r)=-4C(r)^-4 int_r^R C(v)^3 C'(v) A(v) dv,
    P'+4(C'/C)(P-A)=0,
    C'=-K1 S, S'=C, K1=lambda/6.

Retain this stress, including its normal pressure, and replace delta_q(B) by ANY smooth normalized compact B density rho_delta defined relative to its invariant volume. The only nonzero tensor indices of j lie in A. The connection is a product, so B derivatives of rho_delta never enter div j; div j_delta=rho_delta div_A j_A=0 exactly. This is the full curved conservation identity, not a flat Gaussian heuristic. Tangential boundaries still require edge stresses or compact tests away from them.

A supplied positive majorant on B and an exponential chart below its injectivity radius produce a nonnegative compact even bump with invariant-volume normalization. Transform the majorant and profile covariantly. This adds the twelve-dimensional choice SO_0(3,4)/(SO3 x SO4), width and profile; it is not invariant under the original noncompact stabilizer and does not evade K2531's invariant finite-measure theorem. It does not derive a matter action or its independent equations.

At fixed positive epsilon,delta the source is smooth on the full product tube. Let both widths tend to zero with normalized bumps. Testing first against a compact smooth tensor, the B approximate identity tends to its value at q; K2531's A-normal pressure has total weight O(epsilon²), so the result tends to the original thin tension. Joint convergence follows from uniform continuity on compact sets and the bounded total variation of the normalized tangent profiles; it is not convergence of full solutions.

This repair has an explicit cost. Using an auxiliary positive chart/component norm solely for local regularity, in a fixed compact tangential patch the nonzero tangent density has L2 size comparable to epsilon^-3/2 delta^-7/2. This L2 is not the indefinite physical action pairing. Smooth Jacobians are bounded above/below and the scaled nonzero bump squared integral fixes these exponents. The pressure contribution is lower by O(epsilon²). Thus smooth sources do not form a uniformly bounded L2 family in the thin limit. With smooth sources and fixed smooth probes, (5) remains finite, but the full response still requires a constrained inverse and selected homogeneous data. Conservation plus smoothing does not establish existence or physical positivity.

## Evidence, rejected shortcuts and successor

Its positive-curvature polynomial pressure fixture is C1 after zero extension; the universal smoothing construction instead uses flat C-infinity bumps.

The exact probe independently eliminates the original trace equations, checks source conventions and the curved pressure fixture, replays K2541's homogeneous polynomial construction and noncancellation, and checks adjoint/conservation, detector scaling and actual altered coefficients. Universal distributional, Sobolev, approximate-identity and gauge arguments are written above; finite algebra and report consistency do not replace them.

A TT tensor confined to the A block does close a pair of scalar-type differential operators, but an arbitrary componentwise local inverse need not preserve trace/divergence constraints. This tempting shortcut has not been promoted to an arbitrary localized-source solution. Likewise full trace reduction must retain product Weyl and partial-divergence terms. The next strong construction is a constraint-preserving local response for the now fully smooth conserved source with a selected finite observation and homogeneous-data prescription; native Met(X) and matter-action ownership remain separate. No empirical, external-expert, proof-assistant or novelty certification is claimed.
