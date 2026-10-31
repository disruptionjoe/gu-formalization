---
title: "K2382 A finite-sample shared-calibration null test"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no native GU or measured physical verdict
scripts:
  - tests/channel-swings/k2382_finite_sample_shared_calibration_probe.py
---

# K2382 A finite-sample shared-calibration null test

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
result: K2382
carrier: joint finite potential and density samples LAYER=toy CHIRALITY=N/A
pairing: known positive-definite measurement-noise covariance ON=declared_carrier
real_structure: real Gaussian measurement errors and real fixed calibration
grading: classical scalar observation channels
action_owner: repository-construction -- supplied graph after the inherited conditional f(R) response and window bridge
target: finite-sample false-rejection bound MAP-TYPE=evaluation
```

## From population feasibility to a valid statistical test

[K2379](k2379-shared-calibration-cosmological-null-2026-10-31.md) supplies an exact population graph test. This result supplies a finite-sample rejection rule under an explicitly known Gaussian error law. It does not infer that law from a survey. [K2376](k2376-windowed-cosmological-null-2026-10-31.md)'s window bridge must already hold; a graph on unobserved latent fields is insufficient.

Let n samples z_j=(p_j,d_j)=z*_j+epsilon_j have r density outputs. The null is that ONE fixed theta* in a prespecified compact calibration set Theta obeys d*_j=G(theta*)p*_j for every j. G is continuous. The stacked error is N(0,Omega) with known Omega positive definite; it may correlate potential and density errors and different samples. No independence of the latent fields is needed: the null cancels them identically.

Define R_theta=I_n tensor [-G(theta),I_r], S_theta=R_theta Omega R_theta^T, and

    Q(theta)=(R_theta z)^T S_theta^{-1}(R_theta z).
    Reject iff inf_(theta in Theta) Q(theta) > c,
    c = chi-square_(nr,1-alpha).                         (1)

The identity density block makes R full row rank, hence S positive definite. At the fixed true theta*, Rz=R epsilon, so whitening gives nr independent standard normal coordinates. Q(theta*) is exactly chi-square_nr. Rejection in (1) implies Q(theta*)>c, proving false-rejection probability at most alpha. The standard chi-square fact is documented by [NIST](https://www.itl.nist.gov/div898/handbook/eda/section3/eda3666.htm). The profiled infimum itself is NOT claimed to have that distribution, and the number of fitted calibration parameters is not subtracted from nr. This is a conservative composite-null test, not a likelihood-ratio asymptotic assertion or a novelty claim.

Singular latent excitation does not impair this validity proof, but can remove all power to identify a gain. One random calibration shared across the experiment is allowed only with the stated conditional noise law given that calibration; condition first and integrate. Independently redrawn gains are a different model. An unknown or estimated Omega needs its own calibration coverage argument.

## Exact fixture and numerical decision discipline

For n=2,r=1, Omega=I4, G(theta)=theta, |theta|<=1, observed rows (1,a),(1,-a),

    Q(theta)=2(a^2+theta^2)/(1+theta^2).
    inf Q = 2a^2 if a^2<=1, and a^2+1 if a^2>=1.

Differentiate in u=theta^2 to prove both branches. For a=2, the global minimum is5. Alpha=exp(-2) has exact chi-square2 threshold4, so the test rejects. These supplied numbers are synthetic, not a cosmological observation. For the changed fixture a=1, one gain per sample in the SAME ball fits both rows exactly, while every shared gain has Q=2; that changes only the sharedness assumption. Returning to a=2, expanding the shared radius to2 gives16/5, illustrating why calibration bounds matter.

A grid or local optimizer gives an UPPER bound on the infimum and cannot certify rejection. At a=2, Q(0)=8, but the true minimum5 lies below threshold6: using that single grid point would falsely certify rejection. Either prove a global lower bound exceeding c or leave the computation inconclusive. A feasible theta with Q<=c certifies nonrejection, not the truth of the null.

For affine G, write R_theta z=a-Btheta. If S_theta<=beta I uniformly, then

    inf Q >= (min_Theta ||a-Btheta||^2)/beta.           (2)

A ball Theta gives a convex trust-region problem in (2). In the a=2 fixture beta=2 and the raw residual minimum8 give bound4; this alone does not prove strict rejection at threshold4. The exact rational optimization strengthens it to5. A bound known only at sampled theta is not uniform.

## Means and correlated noise must remain in the statistic

For independent replicates with common noise N, empirical mean mu and unbiased sample covariance C (n>1),

    Q=tr[(R N R^T)^(-1) R ((n-1)C+n mu mu^T) R^T].    (3)

This is the raw second-moment identity. Do not subtract N from the empirical covariance or drop the mean term. Identical rows (1,3),(1,3) have zero centered covariance but minimum Q=4 on the same calibration ball. Known scalar potential-density noise covariance contributes -2theta N_pd to S; cross-replicate covariance must also be retained in the stacked formula. These are errors of the specified test, not new mechanisms.

An explicit degrees-of-freedom countercontrol uses n=r=k=1, zero latent signal, Omega=I2, theta in[-1,1]. The incorrect chi-square0 threshold0 rejects exactly when |d|>|p|, probability1/2 by exchange symmetry of two independent normals. Subtracting a nuisance count thus has no general size guarantee. The companion arithmetic assertion labels this as a proof-backed inference control, not an executed Monte Carlo test.

## Bounded graph error and uncertain calibration coverage

If the true graph has stacked residual h with ||S_theta*^(-1/2)h||<=b(theta*), replace (1)'s statistic by

    T_b=inf_Theta [max(0,sqrt(Q(theta))-b(theta))]^2.    (4)

The reverse triangle inequality bounds T_b by the same squared whitened noise norm at theta*, so the same threshold remains valid. Bounds and coordinates must be justified for the same observation. At the exact fixture minimum5, constant b=1/5 still rejects threshold4 because5>(2+1/5)^2; b=1/2 does not. This is a deterministic model-error allowance, not a guessed variance.

If a calibrated random admissible set contains the true fixed theta with probability at least1-gamma, rejection on that set is contained in the union of the pointwise-pivot tail and noncoverage. Size is at most alpha+gamma, without independence. This does not authorize data-driven changes to the underlying graph/noise law or to the claimed coverage. Noise-covariance uncertainty can be handled by including its true covariance in a prespecified confidence set and profiling the corresponding pivot as well, with the same union-bound caveat; this note supplies no such covariance estimator.

## A quantitative power guarantee, not only false-rejection control

For a fixed alternative signal s and the same Gaussian noise, define

    delta=inf_Theta ||S_theta^(-1/2)R_theta s||,
    W=span of all rows of R_theta Omega^(1/2), q=dim W.

Set eta=Omega^(-1/2)epsilon. Each A_theta=S_theta^(-1/2)R_theta Omega^(1/2) has orthonormal rows contained in W. Thus ||A_theta eta||<=||projection_W eta|| simultaneously for all theta. The reverse triangle inequality gives

    sqrt(inf Q)>=max(0,delta-||projection_W eta||).

The squared projection norm is chi-square_q. For delta>sqrt(c), rejection probability is at least

    F_chi-square_q((delta-sqrt(c))^2).                (5)

Equality events have probability zero here. In particular delta>sqrt(c)+sqrt(chi-square_(q,1-beta)) ensures power at least1-beta. For affine R, stack the rows of the nominal R and all calibration coefficient matrices after multiplication by Omega^(1/2) to obtain a containing W. It equals the full row span if the calibration set has nonempty interior; using a larger space is conservatively valid. This argument uses no covering grid. A certified lower bound delta>=d0/sqrt(B), where d0=min_Theta||R_theta s|| and S_theta<=BI uniformly, can replace delta. The bound requires fixed alternative signal and known noise; arbitrary stochastic alternatives need conditioning or additional analysis.

An exact consumer uses the same n2 scalar graph but fixed alternative signal rows(1,5),(1,-5). Here delta²=26 and q=4. On the event ||eta||<=3, inf Q>4 because sqrt(26)>5. Its probability is1-(11/2)exp(-9/2)>9/10; the probe verifies the last strict inequality using a finite lower Taylor bound on exp(9/2). This is an analytic synthetic power bound, not empirical detection or a Monte Carlo estimate. In contrast zero latent signal has delta0 and no power promise. For a bounded-error test(4) with b(theta)<=bmax, the same argument subtracts bmax as well; a valid allowance can remove this certified power guarantee.

## Evidence and unresolved physical use

The exact probe checks rational minimization, means, correlated noise, global-bound direction and model-error thresholds. Distributional validity rests on the proof, not finite fixtures. Internal independent review is not external-expert or proof-assistant certification. SC-COS-50/51/54 ASSERTS retain source meanings; this conditional metric f(R) graph is not their native connection-displacement mechanism. LT-GR2e and ledger0.263 are unchanged.

A next usable test needs calibrated windows, one shared gain family, the actual joint measurement-error law and any graph-error budget. Until supplied, no survey significance, held-out physical prediction or GU verdict follows. The mathematically new step relative to K2379 is a finite-sample size guarantee with explicit conservative nuisance treatment, not another population rank test.
