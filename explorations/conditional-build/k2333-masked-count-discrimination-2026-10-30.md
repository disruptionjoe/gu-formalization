---
title: "K2333 Masked count modes with correlated-noise calibration"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no empirical, hardware or native GU acceptance
scripts:
  - tests/channel-swings/k2333_masked_count_discrimination_probe.py
---

# K2333 Masked count modes with correlated-noise calibration

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
result: K2333
carrier: two finite linear observations of five real full-count quadrupole coefficients LAYER=toy CHIRALITY=N/A
pairing: positive Gaussian covariance on retained real modes ON=declared_carrier
real_structure: real orthonormal spherical harmonics and matrix transpose
grading: fixed L=2 signal with explicitly separated other-multipole leakage including observer monopole/dipole
action_owner: repository-construction -- unchanged K2331 designer dust and supplied statistical/noise family
target: finite one-sky rejection calibration under distinct angular maps MAP-TYPE=evaluation
```

## Result and actual input

[K2331](k2331-certified-count-window-covariance-2026-10-30.md) certifies the SAME full relativistic count kernel, compact spectral band and two positive radial windows. Reuse its actual Gram matrix M, not a fitted covariance: 228<M11<273,230<M12<273,231<M22<273 and M positive semidefinite. This note removes the need for direct access to five independent observed full-sky pairs under explicit finite angular-response and noise hypotheses. It supplies exact mode extraction and a nonasymptotic error allowance for correlated Gaussian noise. It does not supply a survey, physical seed spectrum, angular band limit, or source-owned probability law.

Let a>=0 be unknown signal amplitude. The latent five-vectors x1,x2 are centered jointly Gaussian, Cov(x_i,x_j)=a Mij I5. Observe y_i=A_i x_i+epsilon_i for two known real matrices, rank p_i>0. A_i is fixed before inspecting y. The errors are centered Gaussian and independent of the signal; their JOINT covariance is specified below. This is a finite quadrupole observation model. A mask applied to a complete angular sky generally mixes ALL multipoles: compact radial Fourier support k in[1,2] does not impose L=2 angular support. All other multipoles, including observer monopole/dipole terms and higher L, must be absent, exactly projected away, or included in the declared Gaussian error bound with justified independence. Unknown means/foregrounds are not silently Gaussian noise.

SC-ACT-01/GEO-55/COS-50/51/54 ASSERTS and SC-META-53 UNCERTAIN retain their exact source meanings; ledger0.263 LT-GR2e/GR6b/SM8 remain unchanged. All observational, Gaussian and positive-pairing assumptions here are conventional supplied inputs. No GU rejection, forecast or empirical acceptance follows.

## Exact recoverable common modes

If V has r orthonormal rows spanning row(A1) intersection row(A2), choose L_i=V A_i^+, where + denotes Moore-Penrose inverse. Then L_i A_i=V and the extracted signal covariance is aM tensor I_r. r<=5, and raw noise MUST be pushed through diag(L1,L2). This r counts exactly matched modes for this extraction, not all information available from unmatched subspaces.

A nontrivial rational fixture uses A1 rows(e1+e2,e2,e3,e4), A2 rows(e1,e2+e3,e3,e5), V rows(e1,e2,e3). Take L1 rows((1,-1,0,0),(0,1,0,0),(0,0,1,0)) and L2 rows((1,0,0,0),(0,1,-1,0),(0,0,1,0)). Both identities hold exactly; three common modes remain. For full rank maps A1=I5+E12,A2=I5+2E23, inverses I5-E12,I5-2E23 recover all five. Multiplying observed components without undoing their shear does not produce independent pairs.

## Stronger successor: distinct subspaces through canonical angles

Avoid discarding unmatched modes unnecessarily. Pick W_i with W_i A_i A_i^T W_i^T=I_(p_i) on the nonzero left singular space and set U_i=W_i A_i. The rows of U_i are orthonormal. Singular value decomposition U1 U2^T=P D Q^T yields singular values 0<=sigma_j<=1. Rotate the two whitened vectors by P^T and Q^T and retain r=min(p1,p2) paired coordinates. Call the resulting extraction matrices T1,T2. Their signal covariances are aM11 I_r,aM22 I_r and aM12 diag(sigma_j). The cross covariance is nonnegative in every paired coordinate; distinct pairs have zero covariance. This uses an exact covariance identity and Gaussian independence, not a claim that a masked sky has new independent realizations. Zero sigma gives an uninformative signal cross test, not negative evidence. The previous rank-four fixture has singular values(1,1,1,0), so it supplies four reference pairs even though only three are exactly matched.

For reference noise covariance tau I_(2r), tau>0, the reference law P0 has independent centered pairs with possibly DIFFERENT correlations rho_j>=0. Therefore the predeclared event E that all r pairs are discordant has P0(E)=product arccos(rho_j)/pi<=2^-r. Identical distribution is unnecessary. Reference covariance Σ0 has minimum eigenvalue at least tau because the signal is a Gram covariance. With full column-rank five-mode maps r=5; with r<5 the bound2^-r alone is not a5% test. No arbitrary number of pixels raises r beyond5.

## Correlated-noise perturbation: one-sky robust guarantee

Let the ACTUAL extracted joint covariance be Σ=Σ0+E_N with

    ||Σ0^(-1/2) E_N Σ0^(-1/2)||op <= δ <1.             (1)

There is no independent-mode assumption on Σ. For dimension d=2r, let e_j be the eigenvalues of the relative perturbation. The exact centered-Gaussian relative entropy is

    KL(PΣ || P0)=1/2 sum_j [e_j-log(1+e_j)]
                <= d δ²/[4(1-δ)].                    (2)

The inequality follows by integrating t/(1+t) from0 to e_j and bounding its denominator below by1-δ, treating negative integration direction correctly. Pinsker then yields, for ANY measurable predeclared event,

    |PΣ(E)-P0(E)| <= δ sqrt(d/[8(1-δ)]).
    PΣ(all discordant) <= 2^-r + δ sqrt(r/[4(1-δ)]).   (3)

This is covariance perturbation, not a Monte Carlo frequency or large-sample limit. A directly usable sufficient noise family is actual extracted N=tau I_(2r)+E_N with ||E_N||op<=tau δ. It implies(1) uniformly for ALL a>=0 and every actual K2331 M. No lower or upper signal amplitude bound is needed, including a=0. Cross-channel and cross-mode correlations are allowed inside this ball. To certify it from raw noise use T=diag(T1,T2) and E_N=T(Nraw-Nraw,0)T^T: ||E_N||<=||T||²||Nraw-Nraw,0||. Inverse conditioning is charged, and Nraw,0 must actually transform to tau I. A small raw covariance error by itself does not establish(1).

For r=5 and δ=1/64 the exact bound is

    1/32 + sqrt(5/16128) < 1/20.                      (4)

The last inequality is rationally checkable by squaring the positive difference3/160. This is a conservative sub5% test for one predeclared window pair, orientation and extraction. It is not a physical estimate of noise. A prespecified bank requires a union-bound or other valid joint calibration; fitting maps/noise to the tested data invalidates this proof unless the selection is separately handled.

## Genuine counterconstructions

Even TINY allowed nonseparable noise invalidates the uncorrected1/32 claim. Set a=0,tau=1,r=5 and v=(1,1,1,1,1,-1,-1,-1,-1,-1), E_N=vv^T/640. Its norm is1/64. Realize the data as X_j=ξ_j+Z/sqrt640,Y_j=η_j-Z/sqrt640 with all ξ,η,Z independent standard normals. Given Z, each discordance probability is Φ(Z/sqrt640)^2+Φ(-Z/sqrt640)^2>1/2 almost surely. Conditional independence gives E[q(Z)^5]>1/32. The robust bound(4) still applies. Thus the correction handles an actual change in probability law, not just a schema option.

Without a size bound take X=Z times the all-ones vector,Y=-X. Its PSD covariance yields all-discordant probability1 while every marginal pair looks admissibly Gaussian. Treating five repeated signs as five independent modes fails. A fixed channel sign reversal A2=-I is repaired by the actual known inverse; failing to correct it reverses signal cross signs. An arbitrary leakage field can likewise mimic negative cross response and is not covered merely by calling its source a mask.

## Evidence, prior art and remaining construction

The companion probe checks exact extraction, covariance pushforwards, canonical-angle fixture, PSD perturbations, error amplification, the rational level margin and genuine changed matrices. Universal probability statements rest on the proofs above. The finite matrix used as a within-envelope control is explicitly NOT substituted for K2331's certified integrated matrix. The actual certificate is retained as a hashed dependency.

Cut-sky covariance and low-mode recovery are established methods; see [de Oliveira-Costa and Tegmark, CMB multipole measurements in the presence of foregrounds](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.74.023005). That work also identifies leakage from other multipoles. This note claims an application to the held count-kernel sign family, not novelty for whitening, canonical correlations or Gaussian divergence. Next supply an actual angular response, foreground/multipole model and calibrated joint noise covariance; then check extraction conditioning and(1). Physical seed/tracer/selection remain separate. A failure of this sufficient bound is not a survey impossibility or GU exclusion.
