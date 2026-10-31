---
title: "K2352 Sharp calibration limits for marked FLRW identification"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no native GU or empirical certification
scripts:
  - tests/channel-swings/k2352_calibrated_flrw_identifiability_probe.py
---

# K2352 Sharp calibration limits for marked FLRW identification

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
result: K2352
carrier: distinct-source positive marked Poisson model on exact redshift and log flux LAYER=toy CHIRALITY=N/A
pairing: normalized likelihood ON=declared_carrier
real_structure: real parameters; complex Hilbert structure only for quantum channels
grading: counts and marks remain distinct
action_owner: repository-construction -- K2349 flat FLRW optics and supplied independently bounded population nuisance
target: sharp class intersection and conditional finite-data discrimination MAP-TYPE=evaluation
```

## Result and scope

[K2349](k2349-positive-flrw-source-counts-2026-10-30.md) proves that unconstrained density and luminosity evolution can hide any expansion history. Here bounded calibration yields a sharp, constructive boundary between overlapping and disjoint marked-law classes. A paired-mark test then cancels the unknown luminosity zero point and tolerates arbitrary positive count evolution. These are mathematical calibration requirements for a possible tracer class, not measurements of an actual population. SC-COS-50/51/54 ASSERTS and ledger0.263 LT-GR2e retain their missing native action/observation bridge; no source verdict, physical prediction or residue changes.

K2349's physical optics and Poisson assumptions are reused, not derived anew. Source redshifts are exact, distinct objects are conditionally independent, total intensity is finite and nonzero, and selection is independent of the observed flux mark. No clustering, spatial Cox field or flux-dependent detection is included. Common scalar brightness mixing may be removed by conditioning on N. A volume-limited source class is an intended application only after its completeness and evolution are actually calibrated.

## Full marked-law classes and sharp overlap

On a common connected redshift interval let positive g_i(z)=chi_i(z)^2 chi_i'(z) be the nominal radial shape, possibly multiplied by the SAME known baseline density/completeness. Let m_i(z)=-2 log[(1+z)chi_i(z)] absorb the common 4pi convention. The conditional marked density is

    p_i(z,Y)=g_i(z) exp(u_i(z))/Z_i * Normal(Y; b_i+m_i(z)+ell_i(z),sigma(z)^2),
    |u_i(z)|<=epsilon, |ell_i(z)|<=eta.                     (1)

The known variance is positive and the same under both hypotheses; b_i is a free constant luminosity zero point. Nuisance functions u and ell vary independently within their boxes, including across hypotheses. All equalities are almost everywhere on positive support; use essential oscillation osc f=ess sup f-ess inf f. Bounded ratios and integrability are assumed. Put d=log(g_0/g_1), q=m_0-m_1. Then the two classes intersect if and only if

    osc d <= 4 epsilon AND osc q <= 4 eta.                 (2)

Proof: equality of radial marginals requires d+u_0-u_1 to be constant. Its variable part can cancel d only if d is within2epsilon of some constant, equivalent to its oscillation being at most4epsilon. Conversely choose c=(ess sup d+ess inf d)/2, u_0=-(d-c)/2,u_1=(d-c)/2. Their bounds hold and the radial ratio is exp(c), removed by normalization. Identifiability of a Gaussian location family similarly requires q+ell_0-ell_1=b_1-b_0; center q and use opposite half deviations. Independence of the two nuisance boxes makes the conjunction sufficient. This construction extends to unconditional Poisson intensities when each hypothesis has a freely adjustable positive overall amplitude; choose A_1=A_0 exp(c). A known total normalization supplies additional information and is outside this equivalence. If the luminosity zero point is fixed and identical, replace the second oscillation condition by ess sup|q|<=2eta.

If u is built from independent log-density and log-completeness boxes of radii epsilon_n and epsilon_s, their sum has radius epsilon_n+epsilon_s. The sharp converse requires every sum value be attainable. Completeness s<=1 can clip a nominal symmetric box: require baseline sbar exp(epsilon_s)<=1 or use the actual asymmetric bounds. A joint stellar-population relation between density and luminosity likewise restricts the product class. Equation(2) is not sharp for a constrained coupled class merely because each marginal box is valid. Larger enclosing boxes give conservative overlap possibilities, not proof that a physical population realizes the constructed mimic.

For an observed population law with radial density p and conditional Gaussian mean M, a candidate history belongs to the identified set exactly when osc log[p/g_i]<=2epsilon and osc[M-m_i]<=2eta, in addition to the same calibrated conditional variance/shape. These are population-law criteria, not finite-sample estimators. Positive budgets on both coordinates leave sufficiently nearby smooth histories overlapping: pairwise separation of some histories does not imply unique recovery of every H. A shared constant luminosity error cancels in paired differences; the correlated-error countermodel below concerns residual differences that do not cancel.

## Exact deSitter/Einstein-deSitter consumer

Use the conventional benchmark distances fromK2349 on0<z<=3 and t=sqrt(1+z) in(1,2]. In common scale units,

    chi_0/chi_1=t(t+1)/2,
    g_0/g_1=t^5(t+1)^2/4,
    q=-2log[t(t+1)/2].                                    (3)

The ratios increase from1 to3 and1 to72. Thus writing alpha=exp(epsilon), beta=exp(eta), the FULL conditional marked-law classes overlap exactly when

    alpha^4>=72 AND beta^4>=9.                             (4)

The supplied pair(alpha,beta)=(3,2) overlaps; (2,2) is separated by counts; (3,3/2) is separated by marks. The absolute scale degeneracy fromK2349 remains. This is not a cosmological model fit or a statement that real evolution is within these ranges.

The same count consumer can be made finite without fitting nuisance functions. For nominal inner probability p and weights in[1/alpha,alpha], the sharp bounds are

    p_lo=p/[p+alpha^2(1-p)],
    p_hi=alpha^2 p/[alpha^2 p+1-p].                        (5)

Assign the extreme weights to the inner and outer regions to attain them. With K2349's p0=125/1728,p1=8/27 and supplied alpha=6/5, let U0=p0_hi and L1=p1_lo. Their gap G=L1-U0 is positive. Classify by the midpoint, using N DISTINCT conditionally iid sources. Hoeffding gives each error<=exp(-N G^2/2), uniformly in these independent weight boxes. The probe uses exact rational endpoints and the smallest integer N with N G^2/2>3; exp(3)>20 follows from its positive series. Actual available N and population calibration are separate conditions. These two-bin bounds are sharp for this coarsening, not equivalent to continuum separation(2).

## Paired-mark test despite arbitrary count evolution

Choose M disjoint pairs of distinct sources with low and high exact redshifts z_L,z_H. Select pairs using redshift alone. Define c_i=m_i(z_H)-m_i(z_L) and

    D_j=Y_H-Y_L-(c_0+c_1)/2.

The constant b_i cancels. If c_1-c_0>=Delta>4eta for every admitted pair, underH0 E D_j<=-a and underH1 E D_j>=a, where a=Delta/2-2eta. Suppose the centered mark errors are independent Gaussians with known per-source variance at mostsigma_max^2. Conditional on all selected redshifts, sum D has variance at most2M sigma_max^2, so the wrong sign has probability at most

    exp[-M a^2/(4sigma_max^2)].                            (6)

Proof: exponential Markov applied to the Gaussian moment generating function, optimized over its positive argument. Counts/evolution affect pair availability, not this conditional bound; conditioning on latent luminosity or mark-based selection would invalidate it.

For(3), take t_L<=4/3,t_H>=5/3. Then c_1-c_0>=2log(10/7). With the explicitly SUPPLIED budgets eta=log(10/7)/8 and sigma_max=log(10/7)/4, the exponent is9M/4. Two disjoint pairs give exp(-9/2)<1/20, certified by a finite positive exponential series. This is a feasibility example, not a forecast: it assumes narrow calibrated luminosity evolution/scatter, exact redshifts and enough distinct sources. It cannot be obtained by measuring one object repeatedly. Perfectly correlated residual pair-difference errors prevent the stated variance reduction; flux-dependent selection changes conditional mark means. These are concrete countermodels, not a claim of universal calibration.

## Evidence and next condition

The companion probe checks exact distance ratios, monotonicity, overlap and separation thresholds, constructive centered witnesses, finite rational count bounds and Gaussian exponent arithmetic. Changed-nuisance, fixed-zero-point, correlated-error and mark-selection controls challenge the hypotheses. The universal results rely on the proofs above, not sample enumeration. No new catalogue, empirical calibration, external-expert or proof-assistant certification is claimed. Next requires an actual population's JOINT nuisance and selection model or a different explicitly declared observation model; no amount of sampling distinguishes genuinely overlapping law classes.
