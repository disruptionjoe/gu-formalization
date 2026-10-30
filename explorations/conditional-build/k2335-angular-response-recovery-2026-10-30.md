---
title: "K2335 All-multipole angular recovery and the hard-mask boundary"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no survey, hardware or native GU acceptance
scripts:
  - tests/channel-swings/k2335_angular_response_recovery_probe.py
---

# K2335 All-multipole angular recovery and the hard-mask boundary

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
result: K2335
carrier: two real square-integrable angular count fields with five real quadrupole coefficients LAYER=toy CHIRALITY=N/A
pairing: L2 spherical integral and positive Gaussian covariance ON=declared_carrier
real_structure: real orthonormal spherical harmonics and transpose
grading: full angular multipoles; explicit finite-band repair distinct from compact radial spectrum
action_owner: repository-construction -- held K2331 count law and supplied angular response/noise
target: exact mode extraction, statistical calibration and masked inverse-problem boundary MAP-TYPE=evaluation
```

## Result and hypotheses

[K2333](k2333-masked-count-discrimination-2026-10-30.md) assumes finite angular maps. Here an explicit continuum response removes ALL other angular multipoles exactly, with its actual noise integrals evaluated. A true sky cut has a different identifiability boundary; a finite-band repair and a quantitative tail/mean-error allowance are supplied below. These are conditional observational interfaces, not a catalog or a physical seed/tracer model.

Retain [K2331's actual full-count quadrupole covariance](k2331-certified-count-window-covariance-2026-10-30.md): Cov(x_i,x_j)=a M_ij I5, a>=0, M positive semidefinite and M12>230. This is the supplied centered isotropic Gaussian quadrupole of the same designer action, compact spectral band and radial windows. The other multipoles of f_i in L2(S2) may be arbitrary, including observer monopole/dipole and higher multipoles; additional arbitrary QUADRUPOLE foreground is not included in that Gaussian law. Let

    y_i = w_i f_i + epsilon_i,
    w_1(t)=1+P2(t)/2=3(1+t²)/4,
    w_2(t)=1-P2(t)/2=(5-3t²)/4, t=cos(theta).          (1)

The windows share a known polar axis and are fixed independently of the data. Observation is continuous and angular calibration is exact. Additive Gaussian white noise is an isonormal generalized random field with covariance tau_i times the L2 inner product, tau_i>0; it is not an L2-valued white-noise function. Reference noises are independent of each other and of the signal. Pixelization, unknown means, uncertain response and correlated errors require the explicit extensions below.

SC-ACT-01, SC-GEO-55, SC-COS-50/51/54 retain ASSERTS; SC-META-53 retains UNCERTAIN. Ledger0.263 LT-GR2e/GR6b/SM8 remains unchanged. Source adherence is not statistical or physical validation; no positive observed GU state, forecast, rejection or native action bridge is obtained.

## Exact full-sky response removal and evaluated noise

For real orthonormal Y2m define z_im=<y_i,Y2m/w_i>. Since w_i is bounded away from zero, each test function lies in L2 and

    z_im = <f_i,Y2m> + <epsilon_i,Y2m/w_i>.            (2)

There is no angular cutoff. Orthogonality removes all nonquadrupole signal/foreground components, regardless of their amplitudes. Axisymmetry gives diagonal reference noise in the real order (0,1c,1s,2c,2s):

    N_i=tau_i diag(g_i0,g_i1,g_i1,g_i2,g_i2),
    g0=(5/8) integral[-1,1] (3t²-1)²/w² dt,
    g1=(15/4) integral[-1,1] t²(1-t²)/w² dt,
    g2=(15/16) integral[-1,1] (1-t²)²/w² dt.           (3)

Elementary rational integration gives

    g_1=((260-80pi)/9, 20(pi-3)/3, 5(4-pi)/3),
    g_2=(36-64H, 40H-20, 4-6H),
    H=2 atanh(sqrt(3/5))/sqrt(15).                    (4)

The addition-theorem check is g0+2g1+2g2=(5/2)integral w^-2. Pointwise window bounds give 4/9<=g_1m<=16/9 and16/25<=g_2m<=4, without trusting decimal integration. These actual window integrals replace an arbitrary finite shear example. The K2331 M remains the certified integrated matrix, never a fitted replacement.

Five centered Gaussian pairs are independent across m, with positive or zero cross covariance a M12 and mode-dependent variances. Hence a predeclared all-discordant sign event has probability

    product_m arccos(rho_m)/pi <= 1/32.               (5)

It is one sky with five actual harmonic pairs, not five skies. Different variances do not spoil the argument. No significance is assigned to data in this note.

## Correlated noise and nonzero mean: usable error budget

Let D=diag(N1,N2). If actual extracted centered noise is D+E and

    ||D^(-1/2) E D^(-1/2)|| <= delta<1,               (6)

positive diagonal whitening preserves signs and the reference signal covariance stays positive semidefinite. K2333's Gaussian relative-entropy/Pinsker proof gives, uniformly in a>=0,

    P(all discordant) <= 1/32 + delta sqrt(5/[4(1-delta)]). (7)

For raw relative covariance this bound transfers with no extra condition-number penalty: let T be extraction in(2), C0=diag(tau1 I,tau2 I), so TC0T*=D and A=D^-1/2 T C0^1/2 satisfies AA*=I10. If raw covariance is C0^1/2(I+F)C0^1/2 with ||F||<=delta, then normalized extracted perturbation is AFA*, norm<=delta. This bounded covariance operator is meaningful for generalized Gaussian noise. Absolute raw-error bounds still pay ||T||²; the two statements are different. An explicit nonseparable raw noise is F=vv*/64 for any unit v mixing channels/modes; it is positive and satisfies the hypothesis.

If an unremoved deterministic nuisance produces mean b in the ten extracted coordinates, write beta=||D^-1/2 b||2. Comparing the actual law directly to the centered reference gives

    KL <= 10 delta²/[4(1-delta)] + beta²/2,
    P(E) <= 1/32 + sqrt(5 delta²/[4(1-delta)]+beta²/4). (8)

The mean term is bounded using the REFERENCE covariance >=D; no factor(1-delta)^-1 is needed for this KL direction. At delta=1/128,beta=1/64, the squared correction is5/65024+1/16384<(3/160)², so the total level is strictly below1/20. This executes the mean-error successor that an all-zero-mean assumption would leave open.

Window uncertainty matters: if true w=what+Delta w and extraction divides by what, bias is P2[(Delta w/what)f]. If ||Delta w/what||infinity<=eta and ||f||2<=F, then the vector bias norm is <=eta F by orthogonal-projection contraction. Stack channels and divide by sqrt(lambda_min(D)) for a sufficient beta: beta² <= [(eta1 F1)²+(eta2 F2)²]/lambda_min(D). For Gaussian random f this multiplicative error generally changes covariance and is correlated with the signal; it must instead be included in the full covariance bound, not called independent additive noise. Arbitrarily large unrestricted nonquadrupole nuisance has no finite nuisance-uniform calibration tolerance. For example, a constant f=B and a calibration error proportional to P2 induces quadrupole proportional to eta B.

## Hard cuts: exact hidden-sky counterconstruction

For any bounded mask w vanishing on a nonempty open U, choose smooth eta>=0 supported in U and positive on a smaller open set. With Y the five-vector of real quadrupole harmonics, G_U=integral eta YY^T is positive definite: a nonzero finite spherical harmonic combination is analytic and cannot vanish on an open set. For every b in R5,

    h=eta Y^T G_U^-1 b,  wh=0, integral Yh=b.          (9)

Thus identical observations can have arbitrarily different quadrupoles, even for nonlinear recovery rules on unrestricted smooth skies. A sufficiently large constant baseline makes both count skies nonnegative. This is an INTERNAL unrestricted-nuisance identifiability obstruction, not a rejection of K2331's compact-k Gaussian prior: h need not be in that specific prior support. Restricting to that prior can yield inference, with prior dependence retained.

## Finite-band repair, its failure limit, and tail budget

If one explicitly supplies f in H_{<=L}, all real harmonics through L, let

    G_L=integral w² Y_{<=L}Y_{<=L}^T,
    ell_j=w Y_{<=L}^T G_L^-1 e_j.                    (10)

If the observed region contains an open set on which w is nonzero, G_L is positive definite by analyticity. <y,ell_j> is unbiased for the chosen quadrupole coefficient; its white-noise variance is tau e_j^T G_L^-1 e_j. It is the minimum-norm unbiased linear estimator: any other solution differs by a vector orthogonal to the finite response span, increasing its squared norm.

This is not a stable all-L repair. Choose hidden h from(9) with q_j(h)!=0, and h_L=P_{<=L}h. Then wh_L->0 in L2 but q_j(h_L)=q_j(h) for L>=2. Cauchy-Schwarz forces ||ell_j||>=|q_j(h)|/||wh_L||->infinity. Even the FIXED quadrupole variance diverges, not only the worst matrix condition number. Compact radial Fourier support is not angular truncation.

For a declared tail r=f-P_{<=L}f with ||r||2<=R_L, the bias vector for selected quadrupoles is b=T_L(wr), bounded by ||T_L M_w (I-P_L)|| R_L, or conservatively ||T_L|| ||w||infinity R_L. This deterministic tail can enter(8) after the noise normalization only if the centered extracted reference signal/noise covariance actually has the required sign-pair structure or is separately reduced as K2333 requires. A finite-band Gram alone does not make its correlated quadrupole noise diagonal. For independent white raw noise the extracted D can be dense; do not apply sign-preserving diagonal whitening to a dense D. This explicitly limits the tail repair instead of exporting the positive-axisymmetric-window result to every cut sky.

A concrete hemisphere m=0 fixture uses orthonormal Legendre modes l=0..L on[-1,1] and w=1_(t>=0). Exact rational Gram integration (with normalization radicals) produces growing quadrupole variance factors and an actual l=L+1 leakage control. It is a subspace illustration of(10), not a full survey calibration.

## Evidence and retained dependencies

The probe checks exact harmonic/noise identities, actual response removal and contamination controls, finite-band Gram inversion and leakage, and exact rational statistical margins. Numerical integral comparisons are finite precision controls; the continuum statements rest on the proofs above. [de Oliveira-Costa and Tegmark](https://arxiv.org/abs/astro-ph/0603369) document the established cut-sky low-mode/foreground leakage problem; no novelty is asserted for inverse weighting or finite-band recovery.

Next supply a real response/beam/pixel operator, a physically justified full count spectrum/tracer family and measured joint noise/calibration or tail bounds. The explicit continuous positive-window construction proves a nonempty conditional model, while zero-mask arbitrary-nuisance recovery is impossible. Neither settles that physical input problem or the native GU action/state/domain bridge.
