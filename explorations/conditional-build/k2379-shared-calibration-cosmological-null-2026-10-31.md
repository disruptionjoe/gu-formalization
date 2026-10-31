---
title: "K2379 Fixed shared calibration cannot absorb arbitrary covariance residuals"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no native GU or measured physical verdict
scripts:
  - tests/channel-swings/k2379_shared_calibration_cosmological_null_probe.py
---

# K2379 Fixed shared calibration cannot absorb arbitrary covariance residuals

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
result: K2379
carrier: finite jointly observed real potential and density vectors LAYER=toy CHIRALITY=N/A
pairing: positive semidefinite population covariance and Euclidean calibration norm ON=declared_carrier
real_structure: real finite random vectors with finite second moments
grading: classical scalar observation channels; no fermion grading
action_owner: repository-construction -- inherited conditional metric f(R) dust response
target: exact common calibration feasibility and residual floor MAP-TYPE=evaluation
```

## Result and scope

One fixed calibration must work for all observation blocks. Separate successful fits do not establish that conjunction. [K2376](k2376-windowed-cosmological-null-2026-10-31.md) already owns the window factorization and missing-contrast theorem. Here the starting relation has passed that bridge, or is explicitly a supplied conditional graph; uncertainty is in its fixed row. No survey operator or measured calibration is supplied.

SC-COS-50/51/54 ASSERTS retain their source meanings. Their native connection displacement is not this quadratic metric f(R) construction. LT-GR2e and ledger v0.263 do not change. The stored response example is synthetic population data constructed from existing decimal coefficients, not a new ODE solution or empirical test.

## Exact common-calibration theorem

For block i let A_i=Cov(p_i), c_i=Cov(p_i,d_i), v_i=Var(d_i), with p_i column-valued and d_i scalar. Center these variables, or separately require their means to satisfy the same graph. Supply

    g_i(theta)^T = g_i0^T + L_i theta,  ||theta||_2 <= rho,

where rho>=0 and the SAME fixed theta is used in every block and realization. Matrices are known exactly for this theorem. Covariances refer to signal, after independently justified noise correction. There exist centered random variables realizing these block marginals with d_i=g_i(theta)p_i almost surely iff

    A_i >= 0,
    c_i in im A_i,
    v_i = c_i^T A_i^dagger c_i,
    b in im M, and ||M^dagger b||_2 <= rho,                 (1)

where M stacks A_i L_i and b stacks c_i-A_i g_i0^T. The dagger is the Moore-Penrose inverse for the stated Euclidean coordinates; calibration scaling must be encoded in L, not silently changed.

Proof: a graph implies A_i g_i^T=c_i. All solutions differ from A_i^dagger c_i by an A_i-null vector, so their density variance equals the displayed Schur term. The remaining equations are M theta=b. Their minimum-norm solution is M^dagger b; every other solution differs orthogonally by ker M. Conversely use that theta, any centered p_i with covariance A_i, and define d_i=g_i p_i. Blocks may be taken independent when only marginal data are specified. More strongly, for any existing variables with those valid covariances, Var(d_i-g_i p_i)=0, so the centered relation holds almost surely. Singular excitation is allowed throughout.

For noncentered variables append the affine equations

    mu_di - g_i0 mu_pi = mu_pi^T L_i theta

to M theta=b. Covariance alone misses a constant density offset. An unknown intercept is a different nuisance model.

## Full joint data and the cross-block caveat

If cross-block covariance is given, first require the entire covariance to be positive semidefinite. For stacked p,d and block-row G(theta), check

    C = A G(theta)^T,     V = G(theta) A G(theta)^T.         (2)

The equivalent singular-safe test is C in im A, V=C^T A^dagger C and the affine equations A G(theta)^T=C together with the calibration ball. Vectorize the last equation to obtain one M theta=b. This generalizes (1) to multiple density outputs with shared calibration.

There is a useful cheaper consequence: when the supplied full joint covariance is already PSD, all its individual graph residual variances being zero forces every residual cross-covariance to vanish by Cauchy-Schwarz. Therefore a *common* theta satisfying all marginal exact graphs automatically satisfies the full joint relation. Marginal checks are insufficient without full PSD validation; one cannot fabricate a PSD counterexample with zero marginal residuals and inconsistent residual cross terms. The probe plants an indefinite full matrix with valid-looking scalar marginal graphs to verify this distinction.

## Approximate feasibility has a quantitative floor

For centered variables, one scalar output and any trial g, define c in im A and

    r = v-c^T A^dagger c,
    E[(d-gp)^2] = r + (g^T-A^dagger c)^T A (g^T-A^dagger c). (3)

For uncentered variables add the squared residual mean. This is completion of the square, valid even if A is singular. For a valid population covariance r>=0. Every fixed gain has residual at least r; increasing its calibration radius cannot remove positive r. Over several blocks, minimizing the sum with nonnegative weights of (3) over the SAME ball is a convex constrained quadratic problem. Equality to the sum of weighted r_i occurs exactly when the shared affine equations can be satisfied within that same ball for all positive-weight blocks. A positive residual from unknown noise, stochastic bias or random calibration does not establish a dynamical failure.

Controls: A1=A2=1, nominal gains zero, L1=L2=1, c1=1,c2=-1,v1=v2=1,rho=1 each fit separately but M=(1,1)^T cannot fit b=(1,-1)^T. A=1,c=1,v=2 has r=1 for every fixed gain. A=diag(1,0) hides arbitrary coefficient change in its second coordinate. These are distinct sharedness, excess-variance and excitation effects.

## Random gain is a different model

For independent centered x,theta with Var(x)=a and Var(theta)=s^2, set p=x and d=(g+theta)x. Then Cov(p,d)=ga and Var(d)=(g^2+s^2)a, so r=as^2. Every realization has a gain, but there is no one fixed graph across the ensemble. The probe enumerates x,theta in {-1,1}, g=2 and obtains A=1,c=2,v=5,r=1 exactly. A calibration parameter fixed but unknown for the whole experiment is not this run-to-run stochastic gain. Mixtures across blocks must be modeled before applying (1).

## Stored-history consumer and acceptance

Use all three saved K2373 density rows, supply A_i=I4 and a synthetic common multiplicative gain 11/10. The exact decimal-rational covariance construction recovers theta=1/10 under rho=1/5. Radius1/20 rejects it; replacing the final mode gain by9/10 makes shared feasibility fail even though each mode has a perfect separate graph. This consumer neither measures bias nor upgrades finite stored decimals to a continuum certificate.

The companion probe executes exact rational linear algebra, direct random-gain enumeration, covariance/range/radius/mean controls and the stored consumer. The universal theorem is the written proof. No finite-sample significance distribution follows; empirical use requires calibrated joint windows, noise and selection, a sampling law and uncertainty propagation. Internal specialist review is not external-expert or proof-assistant verification. Next test a justified physical calibration family and its measured errors; do not use one nuisance per mode to evade a shared mechanism.
