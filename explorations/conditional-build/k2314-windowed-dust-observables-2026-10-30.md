---
title: "K2314 Windowed dust observables"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics only; no native physical acceptance
scripts:
  - tests/channel-swings/k2314_windowed_dust_observables_probe.py
---

# K2314 Windowed dust observables

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
result: K2314
carrier: supplied mean-zero Gaussian Fourier seeds of the same healthy4D dust-scalar linearization on a flat torus LAYER=toy CHIRALITY=N/A
pairing: positive Gaussian covariance and Sobolev test-function duality ON=declared_carrier
real_structure: conjugate Fourier reality with independent circular complex modes on one half lattice
grading: scalar metric, scalar field and longitudinal dust perturbations
action_owner: repository-construction -- unchanged K2308 and K2311 healthy designer action, radiation absent
target: exact variance domain and compensated density/potential transfer MAP-TYPE=evaluation
```

## Fixed evolution and supplied statistics

Keep [K2311](k2311-uniform-constrained-dust-evolution-2026-10-30.md)'s SAME healthy scalar+dust action, beta=-1/(sqrt6 M), m=M²>0, dust d>0, smooth background on a compact interval through its turnaround t*, and no radiation. Use a flat2pi-periodic three-torus with nonzero k in Z³, N=|k|, q=N²/a². At t*, set Phi=chi=pi=n=0 and v_k=V_k/N. The constraint holds; initial physical velocity amplitude is V_k/a*, not V_k. A spectrum for physical velocity U would require V=a*U.

Choose one representative from each pair +/-k. On these representatives V_k are independent centered circular complex Gaussians with E|V_k|²=P_k; set V_-k=conj(V_k),P_-k=P_k. P is **supplied**, with no claim of primordial, empirically calibrated or GU-derived statistics. White P means longitudinal-projected vector white noise, not three independent component-white noises. These are linearized generalized random data; their unbounded Gaussian tails do not guarantee small velocities, nonlinear density positivity or absence of caustics.

SC-COS-50/51/54 remain ASSERTS; ledger0.263 LT-GR2e remains NEEDS. The observation here is a mathematically defined spatial window on model fields, not a survey likelihood or a line-of-sight light-cone lensing observable.

## Transfer and the exact covariance map

Let T_F(t,k) be the deterministic transfer from V_k to any real scalar readout F_k. K2311 supplies, uniformly on a fixed compact interval,

    T_n=N delta(t)+O(N^-1),
    T_L=-a² d delta(t)/(m N)+O(N^-3), L=Phi_J+Psi_J=2Phi,
    T_chi=-beta a²d delta(t)/N+O(N^-2),              (1)

where delta(t*)=0,delta'(t*)=a*^-2 and

    delta''+(2H+beta u)delta'-(2d/(3m))delta=0.

Its integrating factor proves delta(t)>0 for t>t* within this interval. Constants are independent of direction because the equations depend only on N². In particular |T_n| is comparable to N for all sufficiently large N at each fixed positive time, or uniformly away from t*. The lower bound is false at t*. The upper bound holds through t*.

With Fourier normalization F(x)=sum F_k exp(ik.x) and window average O_W(F)=(2pi)^-3 integral conj(W)F, the finite-cutoff covariance is exactly

    E[O_Wi(F) conj(O_Wj(G))]
      =sum_k conj(w_i,k) w_j,k T_F(t,k) conj(T_G(t,k)) P_k. (2)

For real windows/readouts this agrees with twice the real part of the independent half-lattice sum. Taking cutoffs to infinity in L²(probability) is possible iff the diagonal sum is finite. This is Gaussian isometry, not a numerical sampling claim. Per-mode multi-readout covariance has rank at most one for this single initial seed (rank one when P_k>0 and the transfer vector is nonzero); a sum of rank-one matrices with k-dependent directions need not be rank one. A common spatial window does not preserve a universal determinant-zero relation.

## Sharp window and regularity thresholds

At fixed t>t*, density window variance is finite iff

    sum_{k!=0} |w_k|² N² P_k < infinity.            (3)

Finitely many exceptional modes do not affect the criterion. If P_k is bounded above and below by positive multiples of N^-p at large N, (3) is exactly W in H^(1-p/2) on the mean-zero sector. Smooth windows work for every such polynomial spectrum. For white P, the condition is H¹. The normalized indicator of a ball embedded in the torus is not H¹: its distributional gradient is a nonzero surface measure, not an L² volume function. Therefore a ball top-hat density readout has infinite white-velocity variance even though each finite cutoff is finite. No oscillatory lattice lower bound is needed.

Counting lattice shells gives density point-evaluation finite variance iff p>5. This is mean-square point evaluation, not a continuity theorem. More generally, almost surely n(t) lies in H^s iff s<(p-5)/2; the potential sum L lies in H^s iff s<(p-1)/2. Initial physical velocity lies in H^s iff s<(p-3)/2. Thus p=4 supplies finite initial velocity L² norm a.s. but infinite density L² norm and point variance at every fixed positive time. This precisely measures the derivative loss; it is not a nonlinear instability conclusion.

For completeness, write each independent complex Gaussian as sqrt(P_k)Z_k with E|Z|²=1. Weighted Sobolev norm is a positive constant times sum b_k|Z_k|². If sum b_k<infinity its expectation is finite, so the sum is finite a.s. If sum b_k=infinity, independence gives E exp(-lambda sum b_k|Z_k|²)=product(1+lambda b_k)^-1=0 in the infinite limit. The product vanishes because either infinitely many b_k are bounded below or log(1+lambda b_k) is comparable to b_k eventually. A finite nonnegative random variable has strictly positive exponential, so the sum is infinite a.s. This proves necessity, including the critical exponent. The potential conclusion uses its nonzero leading coefficient in(1).

## Released consequence: a compensated density/potential readout

K2308's Jordan-frame number density is n_J=n-3beta chi. The exact Hamiltonian constraint, with no division by H, gives

    d [n_J+(m/d)q L]
      =u²Phi-(3Hu+V'+4beta d)chi+3Hd v-u pi.        (4)

For these seeds, K2311 bounds Phi,v,chi,pi=O(N^-1)V, so the compensated transfer T_C for C=n_J+(m/d)qL is O(N^-1), whereas T_nJ=N delta+O(N^-1). Equation(4) improves two spatial derivatives. For white velocity its window variance is finite for every L² window, including the ball top-hat, since sum |w|²/N²<=sum |w|². More generally W in H^(-1-p/2) is sufficient. An iff threshold for C is NOT asserted because its leading coefficient could vanish at a special time/background.

This cancellation is an equality between model fields and a background-dependent, k-dependent multiplier. Construct C at finite cutoff, then take its mean-square limit. Do not subtract two separately undefined rough-window random variables: both pieces can diverge while the joint compensated cutoff converges. No independent instrument noise, measured redshift/lensing projection or background-parameter uncertainty has been supplied. Such errors can spoil cancellation and must enter an actual observation model.

## Observation-noise and calibration test

The cancellation can be tested without pretending the instruments already exist. Supply additive readout errors e_n,e_L independent of the modeled signal, with spatially homogeneous joint spectral covariance S, diagonal between distinct Fourier modes. Set gamma=m/d at a fixed time t>t* and observe C_obs=n_J+e_n+gamma q(L+e_L). The noise spectrum is exactly

    S_C=S_nn+2gamma q Re(S_nL)+gamma²q² S_LL.       (5)

Independence of the two noise channels sets S_nL=0. For nonzero spatially white potential-readout noise S_LL=sigma_L²>0 and bounded white density noise, finite window noise variance is equivalent to W in H². Thus a top-hat window that became usable for the ideal compensated signal fails again under this explicitly supplied noise model. Correlated noise e_n=-gamma q e_L is a contrary construction that cancels exactly; no unconditional noise-immunity or inevitability follows.

An error in the multiplier is separately damaging. If the implemented coefficient is gamma+Delta_gamma, fixed nonzero Delta_gamma, then (1) gives the leading residual transfer

    T_error=-(Delta_gamma d/m) N delta+O(N^-1).

For the white-velocity signal this restores the H¹ window requirement even for arbitrarily small nonzero fixed coefficient error. Exact compensation cannot be called robust by shrinking a constant without checking the ultraviolet limit. A frequency-dependent error Delta_gamma(k)=O(N^-2) is sufficient to retain the O(N^-1) transfer improvement. These are concrete window/noise/calibration requirements for a future detector; they do not claim an optimal estimator or a physical noise law.

## Verification and next question

The probe rederives(4) from K2308's constraint, checks the original seed constraint, physical-velocity normalization and transfer coefficients; it inherits K2311's verified transformed seed, constructs finite conjugate covariance and a nonzero determinant counterexample after mode summation, and rejects changed constraint/frame/weight inputs. Infinite Gaussian thresholds and top-hat statements use the proofs above. No Monte Carlo or finite mode bank certifies a continuum limit.

The next observable construction must specify physical initial statistics, source/detector windows and noise jointly; it can use the exact covariance and compensated channel instead of silently point-evaluating a rough density. The alternative remains a nonlinear dust domain up to first caustic. Neither is supplied by this linear result.
