---
title: "K2327 Constrained seed, joint likelihood and covariance discrimination"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional statistical construction; no physical seed selection or native GU acceptance
scripts:
  - tests/channel-swings/k2327_constrained_seed_likelihood_probe.py
---

# K2327 Constrained seed, joint likelihood and covariance discrimination

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
result: K2327
carrier: real constrained scalar-dust Fourier seed and finite full-count windows with a common isotropic spectrum LAYER=toy CHIRALITY=N/A
pairing: positive spectral covariance and Gaussian covariance Fisher metric ON=declared_carrier
real_structure: conjugate Fourier reality and real symmetric window covariance
grading: linear scalar perturbations and finite radial spectral bands
action_owner: repository-construction -- K2311 dust-scalar action with separately supplied statistical preparation and readout noise
target: finite joint likelihood, covariance-cone membership and nuisance-identifiability tests MAP-TYPE=evaluation
```

## Decision and scope

[K2325](k2325-relativistic-count-covariance-2026-10-30.md) makes full smooth counts finite for suitable supplied seeds. Here a specific differential-precision law realizes one such seed, and its common window covariance yields a normalized likelihood and a sharp finite-template exclusion test. Unknown spectral amplitudes can absorb an overall response rescaling but cannot generally absorb the direction of several shared responses. This replaces the false choice between an invented physical prior and complete observational indeterminacy.

The construction retains the SAME healthy designer dust-scalar action, original constrained initial velocity data and full volume-limited current/observer operator. The statistical law, test photons, observer event, windows and independent Gaussian readout noise are supplied. There is no actual survey, Poisson catalog, empirical confidence, primordial mechanism, nonlinear positive-dust theorem or novelty claim. SC-ACT-01/GEO-55/COS-50/51/54 ASSERTS and SC-META-53 UNCERTAIN remain unchanged. Ledger0.263 LT-GR2e/GR6b/SM8 receives no changed verdict or mapping. This conventional metric model is not source-selected GU connection-distortion dynamics.

## A definite preparation law, with its nonlocality exposed

On R3 let A=1-Delta/K², K>0, and let W be real spatial white noise in K2325's spectral normalization. Define the stationary generalized Gaussian field by

    A² xi = sqrt(C) W,  C>0.

Fourier multiplication gives P(k)=C(1+k²/K²)^(-4). The unprojected precision is the local differential operator C^-1 A^4. Its inverse sampling map A^-2 has spatial tails and is nonlocal. Apply the declared orthogonal infrared restriction Pi_gap=1_{|k|>=k0}, k0>0, to obtain exactly K2325's P4. The sharp projector is nonlocal too. On its retained spectral subspace the inverse covariance has the stated differential multiplier; there is no everywhere invertible precision on the discarded modes. This is a conditional random-field law, not a causal local preparation device or a thermal/inflationary derivation. The SPDE/Matérn connection is established prior art: [Lindgren, Rue and Lindström (2011)](https://joeid.folk.ntnu.no/StatGr/Lindgren_etal.pdf).

For any Schwartz test f the variance integral of |fhat|²P4 is finite and nonnegative, and positive exactly when fhat overlaps retained modes on a set of positive measure; the conjugate-even multiplier constructs a real stationary isotropic Gaussian distribution. P4 is integrable with k²P4 integrable in d³k, so K2325's initial velocity energy and evolved density point variances are finite. This reuses its thresholds rather than deriving them again. Homogeneous total energy over R3 remains infinite; only energy density is meant.

Use [K2311](k2311-uniform-constrained-dust-evolution-2026-10-30.md)'s original t* data Phi=chi_scalar=pi_scalar=n_density=0, v=xi/|k|. Its initial constraint is satisfied modewise. The same scalar multiplier acts on the whole data vector, so it preserves the linear constraint and the deterministic propagated constraint. In K2311's transformed variables the initial normal momentum is beta*d_bg*v, NOT zero. The velocity potential and longitudinal Riesz transform are additional nonlocal maps; none changes this statistical model into primordial physics. Small C controls RMS only.

## Common-window likelihood and cutoff convergence

Fix m real smooth compact-annular windows and the full K2325 coordinate-event operator, with transfer vector B(k) and B(-k)=conjugate(B(k)). Let independent centered Gaussian readout noise have known real covariance N strictly positive definite. The finite real readout vector y then has covariance

    Sigma = N + integral P4(k) B(k) B(k)* d³k.          (1)

Reality under k->-k makes (1) real symmetric. For each a in R^m, a^T(Sigma-N)a=integral P4 |a^T B|²>=0. Thus Sigma>=N>0. Cross terms use the SAME seed; replacing (1) by independent per-window variances changes the experiment. Its exact normalized density is

    L(y)=(2pi)^(-m/2) det(Sigma)^(-1/2)
         exp[-y^T Sigma^-1 y/2].                       (2)

The bound in K2325 proves B_i belongs to L²(P4 d³k). Cauchy-Schwarz makes every cross integral finite. Finite spectral-cutoff covariance matrices converge entrywise and in finite-dimensional norm. Since Sigma_Lambda>=N, inverse continuity has the quantitative estimate

    ||Sigma_Lambda^-1-Sigma^-1||
        <= ||Sigma_Lambda-Sigma|| / lambda_min(N)².

Determinants and (2) converge for each fixed finite y. This is a continuum existence/limit proof; rational matrix fixtures do not evaluate the actual B_i integrals. Numerical observational conclusions still require certified kernels, fixed windows, noise and data.

## What an unknown common spectrum can and cannot hide

At one resolved Fourier mode, let nonzero response vectors t,t' and positive seed powers p,p' produce p tt*=p't't'*. Their rank-one ranges coincide, so t'=c t for c!=0, and equality is equivalent to p'=p/|c|². This proves exact projective identifiability of the response direction. For one nonzero scalar channel, every nonzero response can be absorbed by a freely chosen mode power. For several shared channels, noncollinear response vectors cannot. This is a mode-resolved statement, not a rank-one assertion about integrated windows.

For an isotropic seed, an absorption factor varying with direction is generally forbidden: one radial P cannot be chosen separately on each ray. Conversely, if B_theta(k)=a(|k|)B_0(k) for a real nonzero radial scalar with a and 1/a bounded, P_theta=P_0/|a|² makes ALL window covariances equal while retaining integrability. This is a constructive degeneracy under that enlarged spectral family. A restricted parametric family need not contain the repair. An arbitrary matrix-valued seed covariance is a different, larger model.

## Finite-template covariance cone and a sharp witness

Supply finitely many nonnegative radial templates f_l, each bounded by a constant times P4. Examples are P4 restricted to finitely many specified radial bands plus a declared last tail band. Write P=sum_l p_l f_l, p_l>=0. Keep dynamics theta, observer, windows and any response nuisance b fixed. Define

    M_l(theta,b)=integral f_l B_theta,b B_theta,b* d³k,
    S=Sigma-N=sum_l p_l M_l.                           (3)

The feasible signal matrices form the finitely generated convex cone C=cone{M_l}. It is closed: discard zero generators and normalize remaining PSD generators to trace1. A convergent sequence of PSD combinations has bounded trace, hence bounded total coefficient, so a subsequence of the finitely many coefficients converges to a nonnegative representation of the limit. Finite-dimensional closed-convex separation now proves

    S outside C iff there is real symmetric H with
    tr(H M_l)>=0 for every l, and tr(H S)<0.             (4)

Necessity follows by separating S from C and using positive scaling and0 in C to obtain the homogeneous inequality. Sufficiency follows by summing nonnegative coefficients. H may be indefinite; insisting H>=0 would destroy detection of PSD alternatives.

Exact two-channel control: model A has columns u1=(1,0), u2=(1,1), both powers1, giving S=[[2,1],[1,1]]. Model B has columns v1=(0,1), v2=(1,-1). The witness H=[[0,-1/2],[-1/2,0]] gives tr(H v1v1^T)=0, tr(H v2v2^T)=1 and tr(H S)=-1. No nonnegative B powers reproduce A. With known N=I the observed covariance is strictly positive and (2) is well-defined. A separate same-diagonal control uses A columns (0,1),(1,1), unit powers: S_A=[[1,1],[1,2]]. B with unit powers has the same diagonal(1,2), but off-diagonal-1 instead of+1. The same H gives tr(H S_A)=-1. The probe uses this pair to isolate the information lost by dropping cross terms. Both examples are finite algebra controls, not evaluated survey transfer functions.

If b is unknown, the feasible set is the UNION_b C(theta,b). A witness at one b excludes only that b. A single H satisfying (4) for every admitted b is sufficient to exclude the union, but need not be necessary for a nonconvex union. Likewise finite templates do not cover every positive radial spectrum. Equation(4) concerns exact population covariance: a random empirical covariance lying outside C does not by itself produce a calibrated finite-data rejection.

## Released quantitative consequence: nuisance-projected information

For differentiable covariance parameters at an interior point p_l>0, define

    <U,V>_Sigma = (1/2) tr(Sigma^-1 U Sigma^-1 V).

This is a positive inner product on real symmetric matrices. The covariance score in direction U is

    s_U(y)=(1/2)[y^T Sigma^-1 U Sigma^-1 y-tr(Sigma^-1 U)].

Gaussian fourth moments give E(s_U)=0 and E(s_U s_V)=<U,V>_Sigma. Let U=partial_theta Sigma and let T be the span of actual nuisance derivatives (the M_l and any admitted response derivatives). Orthogonally project U onto T. The efficient local information is ||U-Proj_T U||_Sigma². Thus a positive residual establishes first-order local distinguishability after nuisance fitting. Zero only means the first derivative is hidden; higher-order/global identifiability can survive. At the boundary p_l=0 the tangent cone replaces the span and regular interior Fisher reasoning cannot be exported unchanged. Unknown N adds its own nuisance derivatives and may remove information; the known-noise assumption matters.

## Tracer and physical-input boundary

For conserved tracers sharing the same dust velocity and background dilution, their linear continuity equations imply (n_g-n_d)'=0. Therefore an arbitrary time-dependent multiplicative bias is not licensed by this conserved model. Equal zero initial contrasts force n_g=n_d. A supplied initial entropy h(k)xi(k) gives B_g,i=B_d,i+h(k)W_i(k), with W_i the appropriate source-window response of that time-constant contrast. A distinct stochastic entropy adds another seed and changes the rank/cone family. Flux selection, observer resolution and tracer creation must be derived as new interfaces, not silently fitted into (1).

## Verification and next construction

The exact probe checks spectral filtering/constraint linearity, finite shared covariance and positivity, both cone witnesses, the same-diagonal countercontrol, projective equivalence, Gaussian-score information/projection, and conserved-bias derivatives. Changed spectra/operators/data must fail the unchanged evaluator; no changed truth flags count as mutation catches. The universal claims rely on the written Fourier, constraint, separation and Gaussian proofs, not a finite fixture. The actual full-count integral remains an explicit next implementation boundary.

The next useful test is to choose actual full-count windows, fixed allowed seed/tracer family and noise, certify their M_l integrals and test whether competing dynamics have separated cones or positive nuisance-projected information. A physically measured or derived seed can narrow the family. This work supplies a usable mathematical test without inventing such input; source and ledger verdicts remain unchanged.
