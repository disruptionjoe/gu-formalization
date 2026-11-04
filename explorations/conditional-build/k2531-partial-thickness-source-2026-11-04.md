---
title: "K2531 Residual symmetry and a conserved partial-thickness source"
status: active_research
doc_type: exploration
created: "2026-11-04"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional stationary-product source geometry; no full Green solution or native matter action
scripts:
  - tests/channel-swings/k2531_partial_thickness_source_probe.py
---

# K2531 Residual symmetry and a conserved partial-thickness source

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
result: K2531
carrier: K2519 stationary seven-plus-seven products with totally geodesic Lorentzian four-observer and normal R3 plus R3,4 LAYER=toy CHIRALITY=N/A
pairing: finite scalar transverse measures and symmetric stress distributions against compact metric tests ON=declared_carrier
real_structure: real normal signature (6,4); positive first normal three-space and indefinite second seven-space
grading: scalar profile invariance, stress conservation, action ownership and full-field response remain distinct
action_owner: repository-construction -- selected I1 completion; source stress below is explicitly supplied
target: sharp residual singular support and curved-tube conservation completion MAP-TYPE=evaluation
```

## Result and backward demand

[K2529](k2529-native-displacement-response-2026-11-04.md) supplies a conserved thin tension covector on the stationary product, but proves that no smooth full-field perturbation can answer its codimension10 distributional support. A finite-thickness replacement must specify both symmetry and conservation. The actual product symmetry permits three directions of thickness while forcing seven to remain singular. Pure tangential thickening fails conservation on every nonzero product branch; an explicit normal pressure repairs it and tends to zero in the thin limit.

This is an actual conditional stress construction, not a full mixed finite-momentum inverse or a source-owned matter action. SC-ACT-01/GEO-55 ASSERTS and SC-META-53 UNCERTAIN retain their meanings. Native Met(X), physical quotient, light/motion response and ledger0.263 remain open/unchanged. No tensor source is ruled out merely by a scalar-profile theorem. Use a boundaryless observer or compact tests supported away from any tangential chart/worldvolume boundary throughout; otherwise edge stresses and boundary equations must be retained.

## 1. Use the seed's symmetry, not its signature alone

The first factor has signature(4,3), the observer(1,3); its normal complement V is positive R3. The second factor W has signature(3,4). Product geometry and the parallel distortion preserve the subgroup

    K=SO(3) x SO_0(3,4)

on N=V direct-sum W. This subgroup remains present on every nonzero radial or nonradial K2519 branch. It is enough for the following obstruction; we do not claim it is the whole symmetry in all degenerate cases. Full SO(6,4) need not preserve the product or distortion, so imposing it would erase an allowed counterexample.

The theorem concerns a finite signed Borel measure on the ENTIRE linear normal fibre, invariant under K. It is a condition on a normalized scalar smearing prescription constructed from this seed alone. A chosen bounded tubular chart may break the action at its boundary; its cutoff is additional data, not an exception to the theorem's hypotheses. Neither arbitrary tensor distributions nor conditionally convergent nonfinite generalized profiles are classified by it.

**Sharp support theorem.** Every such finite measure has the form

    mu=nu tensor delta_0(W),                        (1)

where nu is a finite SO(3)-invariant signed measure on V. Conversely every such nu gives an invariant finite measure. In particular no nonzero absolutely continuous finite profile smooths all ten normal directions, but a radial density on V times delta_0(W) is allowed. The stronger assertion that only delta_0(N) is allowed is false.

Proof: invariance of mu implies invariance of its finite total-variation measure |mu|. In a positive-negative coordinate plane of W, a boost scales null coordinates z_+=u+v and z_-=u-v by2 and1/2. The disjoint bands 2^n<=|z_+|<2^(n+1), n in Z, all have the same mass. Finiteness forces that mass to vanish, so z_+=0 almost everywhere. The inverse boost gives the same conclusion for z_-. Thus both plane coordinates vanish almost everywhere. Repeating over the three times four mixed coordinate planes forces all W coordinates zero. Restrict to V and use SO(3) invariance to obtain (1). This is a measure proof, not a numerical test of a few orbits.

The generic indefinite-density warning was already in [the August2 same-bundle observation analysis](../eric-curt-wave3d-b2c15r3-same-bundle-native-variation-observation-support-2026-08-02.md); [K2245](k2245-localized-normal-domain-2026-10-29.md) already constructs a positive-domain Gaussian with changed connection. The contribution here is the actual stationary-product subgroup and sharp partial-support classification, including the non-point counterexample.

## 2. A curved partial-thickness profile must carry pressure

Let K1=lambda1/6. K2519 proves K1!=0 on every nonzero branch. Around the totally geodesic X in the first space form, before any focal point and with positive normal radius r, the local metric is

    G1=dr^2+S(r)^2 dOmega_2^2+C(r)^2 gamma,
    S'=C, C'=-K1 S, S(0)=0, C(0)=1.                (2)

Normal Jacobi fields along X give C; angular normal Jacobi fields give S. Work in a small tube 0<=r<R with C>0, S>0 for r>0. The second factor is fixed at one point q2. Delta_q2 there is the invariant point measure, with density interpreted relative to the ambient invariant volume; this is a tensor distribution supported on a seven-dimensional tube, not a smooth14-dimensional density.

Supply the symmetric mixed stress in the first factor

    T^mu_nu=A(r) delta^mu_nu   (four tangent directions),
    T^i_j=P(r) delta^i_j       (three normal directions),
    all cross and second-factor components zero,

and tensor it with delta_q2. Pair with compact metric variations by
j(H)=1/2 integral T^{MN} H_MN dmu_G, using distributional integration. A may have either sign; for K2529's covector choose the integrated tangent weight tau0. Direct connection contraction gives the only nontrivial divergence equation

    (div T)_r=P'+4(C'/C)(P-A).                     (3)

The two angular normal connection terms cancel because the radial and angular normal pressures are the same. The second-factor derivative of delta does not appear: all stress components with a second-factor divergence index vanish and the connection is a product. Tangent derivatives vanish by homogeneity. At r=0 smooth even profiles define ordinary Cartesian normal tensors.

Pure thickened tension P=0 has divergence -4(C'/C)A. For K1!=0 and r>0 in this tube it vanishes only where A=0. Thus the naive radial thickening is not conserved. The flat K1=0 control genuinely allows P=0; it is excluded here by the actual nonzero stationary branches, not by an unproved generic curved-space claim.

## 3. Executed conservation repair and thin limit

For a smooth radial A, supported in r<R and flat at the outer boundary, choose

    P(r)=-4 C(r)^(-4) integral_r^R C(s)^3 C'(s) A(s) ds. (4)

Multiplying (3) by C^4 proves it exactly. The outer condition P(R)=0 fixes the homogeneous solution c C^-4; choosing a different constant would add a pressure outside the source support. Evenness of A,C and oddness of C' make P smooth and even at0, and flatness atR extends it smoothly by zero. Compact test integration by parts therefore proves j(Lie_V G)=0 for the full product, including tests with second-factor dependence. This closes the leading metric conservation demand for the SUPPLIED stress. It does not construct a matter action or prove its independent matter/embedding equations; conservation is necessary, not sufficient, for that ownership.

There is an explicit thin family. Choose a nonzero nonnegative smooth radial bump rho(r/epsilon), supported below epsilon, and normalize A_epsilon=c_epsilon epsilon^-3 rho(r/epsilon) so

    4pi integral_0^epsilon A_epsilon C^4 S^2 dr=tau0. (5)

Use the sign of tau0 in c_epsilon if needed. For small epsilon, C=1+O(K1 r^2), S=r+O(K1 r^3), so c_epsilon is bounded and tends to the ordinary Euclidean normalization. Equation(4) gives uniformly P_epsilon=O(|K1| epsilon^-1), and its integrated absolute normal weight is O(|K1| epsilon^2). Pairing against smooth compact tests then gives tangent tension tau0 on X and vanishing normal pressure as epsilon tends to0, still delta-supported in W. Hence j_epsilon tends to K2529's thin covector. This distributional limit is not convergence of any full sourced solution or a finite self-energy theorem.

A reproducible finite-regularity fixture takes K1=-1, C=cosh r, S=sinh r, R=arcosh2 and A=(4-C^2)^2 inside, zero outside. It is C1 atR, enough for the first-divergence test. With c=C, set

    F(c)=4c^4-(4/3)c^6+c^8/8,
    P(c)=-4 c^-4 [F(2)-F(c)].                      (6)

Then c dP/dc+4(P-A)=0 and P(2)=0. The C-infinity theorem uses a flat bump instead; the polynomial fixture is not falsely labeled smooth to all orders. Omitting pressure or changing its sign fails the original divergence, providing contrary controls.

## 4. Full-thickness escape has a precise extra input

A positive normal majorant is an admissible CHANGED construction, not a forbidden repair. Preserve the product and choose a fundamental symmetry J on W, J^2=1 and h_W=eta(J.,.) positive. Together with the positive V metric this gives a normalized ten-dimensional Gaussian. Its family transforms covariantly with J; one fixed profile is invariant only under its compact stabilizer. The compatible choices have orbit SO_0(3,4)/(SO3 x SO4), dimension21-3-6=12, with an independent width. This is not the24-dimensional full SO(6,4) choice space.

These facts price the symmetry-breaking input; they do not supply a physical selector. K2245's earlier positive-domain construction remains valid at its scope. If J is introduced into an action, its simultaneous variation/transport and stress contributions must be retained before a conservation claim. A frozen Gaussian alone does not meet (3) or construct the source's equations. SC-META-53 leaves physical compact shielding uncertain, so no source-derived positivity or matter credit is booked.

## 5. Released source-domain requirement

The repaired source has a sharper regularity requirement than the original thin source. Fix epsilon>0 and a compact product chart away from tangential edges. A nonzero component localized in the seven tube coordinates u has the form f(u)delta_0(v), with f smooth and compactly supported, v in R7 the second-factor coordinates. The cutoff tests local regularity; multiplying the stress by a tangential cutoff need not preserve its global conservation, and no new conserved source is claimed by that localization. Use an auxiliary Euclidean chart norm solely to define local isotropic Sobolev regularity; it is not a physical Hilbert metric or a change to the ambient signature.

For this localized distribution,

    f(u)delta_0(v) belongs to H^(-s) iff s>7/2.      (7)

Indeed its squared Fourier norm is proportional to

    integral |fhat(eta)|^2
      [integral (1+|eta|^2+|zeta|^2)^(-s) dzeta] deta.

The seven-dimensional inner integral has tail r^(6-2s). It converges precisely for s>7/2, when it is a finite constant times (1+|eta|^2)^(7/2-s); rapid decay of fhat completes the sufficiency. If s<=7/2 it diverges for each eta, and fhat is nonzero on a set of positive measure. The endpoint is logarithmically divergent. The thin codimension10 source instead requires s>5. This is a gain of three halves of a Sobolev order for each FIXED partial width, not a uniform bound as epsilon tends to zero. Norms may diverge in that limit.

Consequently, if a linear differential system with smooth coefficients and order at most m satisfies Lz=j and ALL response components are in H^r locally, its mapping H^r -> H^(r-m) imposes the necessary bound r<m-7/2 near nonzero source support. This is not existence, elliptic regularity, a full I1 order calculation, or a claim that each observed response component has that same maximal regularity. Mixed systems can distribute singularities differently; anisotropic domains and special traces require their own analysis. A smooth homogeneous response is excluded already by K2529; (7) supplies the actual next source-domain input instead of repeating that exclusion.

## Evidence and consuming question

The probe checks original boost/form identities, the intersection of actual mixed-plane fixed spaces, the non-point countermeasure, tube connection divergence, exact pressure fixture and contrary controls, small-radius scaling, compact-choice dimension and Sobolev tail thresholds. The universal measure/conservation/limit proofs are written above and independently reviewed; passing finite checks is not proof of arbitrary field response. No external-expert, proof-assistant, experimental or novelty certification.

The partial source is now explicit and conserved, but remains codimension7 singular. A full mixed I1 operator and compatible distributional domain are still required before a sourced response or induced metric readout. Alternatively an action-owned majorant/thickness with its own equations changes the physical input. No homogeneous Hessian inversion, scalar smearing theorem or conservation identity supplies those missing objects. Native source, ledger and canon remain unchanged.
