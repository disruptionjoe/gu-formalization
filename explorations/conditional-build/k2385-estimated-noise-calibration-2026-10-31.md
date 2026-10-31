---
title: "K2385 Shared-graph testing with finite independent noise calibration"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no native GU or measured physical verdict
scripts:
  - tests/channel-swings/k2385_estimated_noise_calibration_probe.py
---

# K2385 Shared-graph testing with finite independent noise calibration

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
result: K2385
carrier: stacked real potential and density errors and independent calibration vectors LAYER=toy CHIRALITY=N/A
pairing: positive covariance and independently estimated Mahalanobis form ON=declared_carrier
real_structure: real Gaussian draws with one fixed common covariance
grading: classical science and calibration samples
action_owner: repository-construction -- supplied observation graph after K2376 window bridge
target: finite-sample composite-null rejection with estimated covariance MAP-TYPE=evaluation
```

## The missing measurement-noise interface

[K2382](k2382-finite-sample-shared-calibration-2026-10-31.md) assumes a known joint error covariance. Here a finite independent calibration experiment replaces that assumption. This is a conditional statistical construction, not a survey noise estimate or a new GU prediction. The graph and window assumptions remain those of K2376/K2379. SC-COS-50/51/54 retain ASSERTS polarity; LT-GR2e and ledger0.263 are unchanged.

Let the science vector z=s+epsilon belong to R^D, epsilon~N(0,Omega), Omega positive definite. The null has a single fixed theta* in a prespecified compact Theta with R_theta*s=0. As before R_theta=I_n tensor[-G(theta),I_r] has d=nr independent rows. Obtain m independent calibration vectors xi_j~N(0,Omega), independent of epsilon and of the fixed signal, representing the SAME full stacked noise experiment. These are noise-only draws, not independent cosmological skies or empirical latent-field covariances.

With known zero calibration mean put nu=m and Omega_hat=sum xi_j xi_j^T/nu. With unknown calibration mean, center independent Gaussian xi_j about their sample mean, put nu=m-1, and use the unbiased covariance. This second option estimates noise covariance only: it does not correct an unknown bias in the science measurement. Assume nu>=D for simultaneous positive definiteness at every theta almost surely. Define

    S_hat(theta)=R_theta Omega_hat R_theta^T,
    Qhat(theta)=(R_theta z)^T S_hat(theta)^(-1)(R_theta z),
    c = [nu*d/(nu-d+1)] F_(d,nu-d+1;1-alpha).
    Reject iff inf_Theta Qhat(theta)>c.                         (1)

This test has size at most alpha. At the FIXED true theta, nu*S_hat has Wishart_d(nu,S_theta) law and is independent of the residual. Thus Qhat(theta*) has the stated scaled F law. Rejection implies Qhat(theta*)>c. The fitted infimum is not assigned an F distribution and fitted gain counts are not subtracted from d.

The normal/Wishart identity is standard; see the [Stanford statistics derivation](https://web.stanford.edu/class/stats305c/lectures/Hotelling_T2.html). For completeness, whiten the projected noise and calibration. Write g~N(0,I_d) independent of Z with d by nu independent standard-normal entries. Then Qhat=nu*g^T(ZZ^T)^(-1)g. Conditional on u=g/||g||, orthogonal invariance and the Schur complement give (u^T(ZZ^T)^(-1)u)^(-1)~chi-square_(nu-d+1): regress the first calibration row on the other d-1 rows, leaving nu-d+1 Gaussian residual degrees. This variable is independent of ||g||^2~chi-square_d. The ratio proves (1). The distributional theorem is a written proof; exact fixture checks below are not a Monte Carlo proof of coverage.

## Pointwise rank is not uniform rank

For a fixed theta, nu>=d already suffices. It does NOT guarantee invertibility for every theta chosen from the same calibration. In D3,d1,nu2 take calibration columns (1,0,1),(0,1,1) and R_theta=(-theta1,-theta2,1). The projected scatter is (1-theta1)^2+(1-theta2)^2 and vanishes at (1,1). The raw covariance is singular. Under Gaussian sampling, adapting theta to a random null direction causes the same issue whenever that direction lies in the allowed graph family; a fixed-theta almost-sure statement cannot be intersected over an uncountable family without proof.

The main theorem uses nu>=D to avoid this seam. A conservative extension for d<=nu<D sets the test statistic to zero whenever ANY admissible theta has singular S_hat, otherwise uses (1). Rejection then still implies the valid pointwise event. This extension may lose all power. A pseudoinverse with unchanged degrees of freedom has no license from this proof. Known structural support reduction is another model and must be specified before sampling.

## Exact global rejection and plug-in failure

Take D4,d2,nu9, |theta|<=1, science rows (1,a),(1,-a), and the supplied calibration realization xi1..4=3e1..4, xi5..9=0. Then Omega_hat=I4 and

    Qhat(theta)=2(a^2+theta^2)/(1+theta^2).

This is an arithmetic fixture, not claimed observed data or a typical calibration draw. At alpha=1/16 the correct threshold is c=9, because for d2,nu9 the exact tail is (1+c/9)^(-4). At a=3, inf Qhat=10, certified by

    Qhat(theta)-10=8(1-theta^2)/(1+theta^2)>=0,

so the test rejects. Widening the calibration radius to3 lowers the minimum to18/5 and removes rejection. A local or grid value remains an UPPER bound on the infimum; Qhat(0)=18 cannot certify rejection at threshold12 because Qhat(1)=10.

At a singleton theta, treating Omega_hat as known is demonstrably anti-conservative. At threshold9 the true size is1/16, while the chi-square2 nominal tail is exp(-9/2)<1/16. Neither more optimizer starts nor a nuisance-degree correction repairs the incorrect pivot. Scaling the calibration covariance by four divides the computed statistic by four; the correct reference law remains based on the genuine calibration design, not a preferred normalization.

## Model error must use the estimated metric correctly

Let the true raw residual h belong to a prescribed set H_theta*. Use

    T=inf_(theta,h in H_theta) (R_theta z-h)^T S_hat(theta)^(-1)(R_theta z-h).

The true pair leaves pure noise, so the same threshold is valid even though the fitted covariance and all candidate metrics are random. For ||h||<=rho a simpler conservative statistic is

    T_rho=inf_theta [max(0,sqrt(Qhat(theta))
                         -rho/sqrt(lambda_min(S_hat(theta))))]^2.       (2)

At theta*, the triangle inequality bounds this by the whitened noise statistic. An old bound in the TRUE covariance norm cannot simply be subtracted unchanged in the estimated norm. For example true S=I, estimated S=I/100 increases every nonzero whitened residual norm tenfold.

In the a3 fixture S_hat=(1+theta²)I, so its minimum eigenvalue is at least1. For rho=1/10, (sqrt10-1/10)^2>9 certifies rejection uniformly. With rho=1/2, theta1 gives (sqrt20-1/2)^2/2<9, certifying nonrejection. These are exact radical inequalities, not numerical tail approximations. Nonrejection does not establish the graph's truth.

## A useful consequence: calibration-event power guarantee

Coverage is not power. For a fixed alternative s, let a0=inf_Theta||R_theta s||, L=sup_Theta||R_theta||_op, and suppose a justified calibration event E has probability at least1-gamma with sup_Theta lambda_max(S_hat(theta))<=beta. If ||epsilon||<=r then simultaneously

    inf Qhat >= [max(0,a0-L*r)]^2/beta.

Hence if a0>L*r+sqrt(beta*c), rejection has probability at least1-gamma-Pr(||epsilon||>r). A justified bound Omega<=M I gives Pr(||epsilon||>sqrt(M)*t)<=Pr(chi-square_D>t²). The event and bound must be supplied or independently proved; we have not estimated them from a survey. No independence is needed for this union bound.

This consequence has a nonempty exact fixture: the same opposed rows with a10 have a0=sqrt200, L=sqrt2. On E:Omega_hat<=2I4 one can use beta4, and with r2, c9 the inequality sqrt200>2sqrt2+6 holds. Thus the conditional instrument has a genuine separation margin once a calibration-coverage event is justified. It does not reuse K2382's known-covariance power statement after changing its hypotheses.

## Acceptance and next condition

Independent internal review checked the ratio proof, fixed-versus-profiled quantifiers, rank seam, raw model-error correction and exact controls. No external-expert or proof-assistant certification is claimed. The companion probe executes symbolic covariance, Schur-complement and global-minimum identities plus changed-input controls; it does not sample a cosmological dataset. The next physical requirement is an actual independent noise-calibration design with the same selection, windows and cross-sample covariance as the science observation. Unknown noise bias, non-Gaussian calibration and shared contamination remain distinct unproved assumptions.
