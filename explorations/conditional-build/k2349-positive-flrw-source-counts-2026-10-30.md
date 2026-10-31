---
title: "K2349 Positive FLRW source counts and their evolution boundary"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no native GU or empirical certification
scripts:
  - tests/channel-swings/k2349_positive_flrw_source_counts_probe.py
---

# K2349 Positive FLRW source counts and their evolution boundary

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
result: K2349
carrier: positive marked point process on redshift and bolometric flux LAYER=toy CHIRALITY=N/A
pairing: ordinary likelihood and probability ON=declared_carrier
real_structure: real coefficients with complex Hilbert adjoint only where stated
grading: distinct source counts; not repeated photons
action_owner: repository-construction -- flat FLRW metric optics with conserved Poisson test tracers
target: joint count-flux identification and finite history discrimination MAP-TYPE=evaluation
```

## Result and relation to earlier work

This replaces the supplied angular heat-response example of [K2346](k2346-positive-count-response-discrimination-2026-10-30.md) with an explicitly geometric positive source census. It is a conditional conventional FLRW observation model. It is NOT the nonlinear completion of [K2325](k2325-relativistic-count-covariance-2026-10-30.md)'s correlated perturbed dust/Gaussian experiment, and it is not a native GU cosmology. SC-COS-50/51/54 ASSERTS and ledger0.263 remain unchanged. The required source-action/matter bridge for LT-GR2e is still open.

For complete homogeneous conserved Poisson test tracers, the normalized continuum count distribution determines comoving distance shape up to scale; standard-candle flux supplies an independent consistency relation. Arbitrary density and luminosity evolution instead absorb ANY smooth positive expansion history at the level of the full marked Poisson law. A finite deSitter/Einstein-deSitter test demonstrates the surviving conditional discriminatory content and quantifies bounded evolution sensitivity.

## Positive marked observation model

Assume a spatially flat FLRW physical metric, exact cosmological redshift, transparent metric photon propagation and bolometric flux, with c explicit. For H(z)>0 define

    chi(z)=c integral_0^z du/H(u),
    d_L(z)=(1+z)chi(z), F(z)=L(z)/[4pi(1+z)^2 chi(z)^2],
    dV_c/(dz dOmega)=chi(z)^2 chi'(z).

These are the standard flat specialization of [Hogg, Distance measures in cosmology, equations15,16,20,21,28](https://arxiv.org/html/astro-ph/9905116v4). They are imported physical assumptions, not GU predictions. Band flux needs its own spectrum/k-correction; peculiar velocities, lensing, clustering and redshift errors are absent here. Test-tracer homogeneity and a Poisson sampling law are additional assumptions, not consequences of FLRW symmetry.

On 0<z<=Z let n(z)>0 be comoving source density, Omega a fixed sky solid angle, s(z) known thinning selection, and k(y|F(z)) a normalized calibrated measurement kernel for the flux mark. Require measurable0<=s<=1 and finite nonzero total intensity0<Omega integral_0^Z n(z)s(z)chi(z)^2 chi'(z)dz<infinity. In the scalar Cox model A is finite and strictly positive almost surely; the conditional intensity must obey the same integrability condition. Positivity alone would not exclude an infinite catalogue near z=0. The marked intensity is

    lambda(z,y)=Omega n(z)s(z)chi(z)^2 chi'(z) k(y|F(z)).       (1)

For example y may be log flux with a supplied known Gaussian error. Noiseless marks use a Dirac probability measure, not a Lebesgue density. If selection depends on observed flux, s(z,y) must be inside the intensity and normalization; formulas below for a complete census use s=1. These are persistent SOURCES, not transient events, so no observer-time factor(1+z)^-1 belongs in(1).

With mu=integral lambda, the point-process likelihood is exp(-mu) product_i lambda(z_i,y_i), up to a parameter-independent ordering convention. Given N, samples are iid with density lambda/mu; disjoint bins have the multinomial law with probabilities integral_bin lambda/mu. If n=A r(z) with fixed shape r and free common A, the conditional likelihood eliminates A exactly. Its profile value for N>0 is A=N/M, M=mu/A. Scalar Cox mixing also leaves this conditional law unchanged; unrestricted spatial Cox fluctuations do not. An unknown amplitude can differ between hypotheses. Conditioning intentionally discards any total-count information from a known density calibration.

## Conserved complete census and joint flux consumer

For n=n0 constant and s=1, integration gives

    mu=Omega n0 chi(Z)^3/3,
    p(z)=3chi(z)^2 chi'(z)/chi(Z)^3,
    P(z)=Pr(redshift<=z | N)=[chi(z)/chi(Z)]^3.               (2)

Consequently chi(z)/chi(Z)=P(z)^(1/3). At population-law level with continuum redshifts, H(z) has its shape determined up to the one global length/time scale. This is not finite-data reconstruction of H or its derivatives. For a constant intrinsic standard-candle luminosity L0, the latent flux curve obeys

    F(z)(1+z)^2 P(z)^(2/3)=L0/[4pi chi(Z)^2].                (3)

An identifiable mark kernel can transport the flux curve into a statistical consistency test. Equation(3) itself is the population identity; arbitrary kernel errors or a fitted luminosity history do not make a calibrated test.

One full-law gauge remains even with counts and flux together:

    chi -> a chi, H -> H/a, n0 -> n0/a^3, L0 -> a^2 L0, a>0. (4)

It leaves intensity AND flux marks invariant. Thus free density and luminosity calibration cannot recover H0. An independent absolute calibration breaks the appropriate scale freedom. This result concerns the declared same metric, tracers and optics throughout.

## Exact finite discrimination and robustness

Supply two conventional benchmark histories on0<z<=3:

    deSitter: H=H0, chi=(c/H0)z;
    Einstein-deSitter: H=H0(1+z)^(3/2),
                      chi=(2c/H0)[1-(1+z)^(-1/2)].

The positive tracers are nonbackreacting in the deSitter comparator; adding finite dust stress and retaining exact deSitter would change its dynamical premises. No empirical adequacy or source ownership is claimed for either benchmark. With split z*=5/4, the inner-bin probabilities are p0=125/1728 and p1=8/27. The gap is43/192. Choose Einstein-deSitter when K/N>637/3456 and deSitter otherwise. K is the number of DISTINCT sources in the inner bin, conditional on total N. Each error is bounded by

    exp[-1849 N/73728].                                    (5)

This follows from the same proved Bernoulli concentration argument as K2346 and midpoint distance43/384. At N>=128, the exponent1849/576>3, and exp(3)>20, so each error is below5%. The probe also evaluates both actual binomial tails exactly using integer arithmetic; the bound is not their attained value.

If actual density times completeness relative to the nominal shape is r(z) in[1-delta,1+delta], the normalized inner probability lies between

    p(1-delta)/[1+delta(1-2p)]
    and p(1+delta)/[1+delta(2p-1)].                          (6)

Indeed assign the lowest/highest allowed weights separately to inner and outer mass; these extremes are attained by step weights. In particular |Delta p|<=delta/[2(1-delta)]. Delta=1/33 gives1/64. The same threshold then has margin37/384; at N>=192 each error is at most exp(-1369/384)<1/20. Probe tails at the conservative endpoint-shift bounds are exact. Redshift measurement error, angular clustering and duplicate sources are not covered by this radial multiplicative model.

N is an observed data condition. A complete finite volume and sky do not acquire fresh independent sources merely by integrating longer. The survey may return insufficient sources. Repeated observations of the same sources do not multiply N. No exposure-to-count or real-catalogue power promise is made.

## Full marked-law degeneracy and finite-bin boundary

Take any two smooth positive histories with distances chi0,chi1, and arbitrary positive source functions n0(z),L0(z). Define

    n1=n0 chi0^2 chi0'/(chi1^2 chi1'),
    L1=L0 chi1^2/chi0^2.                                   (7)

The entire intensities(1), including flux marks and the SAME calibrated selection/kernel, coincide. Ratios have regular positive limits at z=0 for finite nonzero H(0). Thus unknown evolving populations can hide expansion even when joint counts and flux are observed. This is an explicit positive full-distribution countermodel, stronger than matching covariance. It is not a claim that actual stellar evolution realizes any selected n1,L1.

Finite bins also cannot recover arbitrary continuum H: all complete count-bin means depend only on chi at bin edges. Smooth strictly increasing distance curves with equal edge values and different interior derivatives give identical binned counts. For chi0=z, add a sufficiently small multiple of z^2(z-z*)^2(z-Z)^2; derivative positivity holds for sufficiently small amplitude on the compact interval. The probe supplies an explicit rational amplitude and a conservative derivative bound. This reuses the [finite-node boundary](../../lab/active-research/joe-directed/prediction-kickoff/late-time-finite-node-identifiability-2026-10-27.md), not a new universal inversion theorem. Continuous flux marks with known L can distinguish these curves; finite-bin COUNTS alone cannot.

Next physical use needs one actual source class, selection and evolution calibration, redshift/mark errors and clustering model, then a held-out catalogue. The mathematical construction now specifies what must be supplied. No empirical, native GU, novelty, external-expert or proof-assistant certification follows.
