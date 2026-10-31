---
title: "K2343 Exact conditional count comparison with shared photons"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no native GU or empirical certification
scripts:
  - tests/channel-swings/k2343_conditional_count_exchangeability_probe.py
---

# K2343 Exact conditional count comparison with shared photons

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
result: K2343
carrier: two integer count channels on disjoint angular bins and their overlapping aperture incidence map LAYER=toy CHIRALITY=N/A
pairing: probability law, real quadrupole linear statistic ON=declared_carrier
real_structure: real coefficients or complex adjoint as explicitly stated
grading: bin and channel labels; no family count
action_owner: repository-construction -- supplied common-private-rate Poisson/Cox model
target: finite size, positive-intensity power and exact null boundary MAP-TYPE=evaluation
```

## Question, scope and retained evidence

[K2340](k2340-poisson-aperture-calibration-2026-10-30.md) shows that matching covariance does not transfer a Gaussian five-sign test to photon counts. Here a DIFFERENT null admits an exact finite test: conditional on any latent sky, the two private intensities agree in every retained angular bin. Shared photons can have arbitrary counts because they cancel before inference. This is an equality/response diagnostic, not the former Gaussian positive-cross-covariance cosmology null. No inference between competing GU cosmologies is licensed merely by rejecting this equality.

SC-COS-50/51/54 ASSERTS remain source statements, not owners of the supplied count law. Ledger0.263 and all native verdicts remain unchanged. General finite group tests are established; the contribution is their explicit aperture/count consumer, nuisance cancellation, heat-positive power and precise failure boundary. See [Hemerik and Goeman](https://doi.org/10.1007/s11749-017-0571-1).

## Law and proof without photon-count truncation

Use disjoint bins B_j, either complete aperture-membership atoms or fixed subregions thereof. In a common coordinate/response system observe X_j=P_j+C_j and Y_j=Q_j+C_j. Given a latent variable Z, all P_j,Q_j are independent Poisson with equal paired means mu_j(Z); the means may be arbitrarily correlated across j. C_j may be dependent or non-Poisson, provided exactly the same count enters both channels. Thus D_j=X_j-Y_j=P_j-Q_j exactly. No shared-photon identity tags are needed, but bin-resolved counts/positions ARE needed; aggregate overlapping apertures need not determine them.

For fixed Z, swapping P_j,Q_j in any subset preserves their joint law. Therefore the joint law of D is invariant under every coordinate sign flip. Mixing Z preserves this invariance. Conditional on |D|, its m nonzero signs are uniform on {−1,+1}^m, independently of the nuisance means. This conclusion uses coordinatewise invariance, not unconditional independence of counts. Zero differences are removed; if m=0, p=1.

Let A be the fixed aperture incidence matrix and T the fixed K2337 quadrupole extraction. Predeclare F(D)=|u^T T A D|, or any fixed statistic. For observed magnitudes a and signs s, calculate

    p(s,a)=#{r in {−1,+1}^m : F(r a)>=F(s a)}/2^m.

For every alpha, at most alpha*2^m orbit points have p<=alpha: sort statistic values and retain all ties in each upper tail. Hence Pr(p<=alpha | |D|)<=alpha, and integrating gives the same bound uniformly over the allowed Cox and shared-count nuisances. Enumerating signs, not unbounded photon counts, gives an exact finite algorithm. No large-exposure Gaussian approximation or Poisson tail is needed.

## Explicit six-bin aperture consumer and positive power

Retain one representative of each of the six antipodal icosahedral axes of K2337, with the first called v1. Let c=1023/1024 and B_j be the circular cap of cosine radius c about v_j. These are singleton membership bins: for any other aperture center the maximal dot product is at most (1023+2 sqrt(2047))/(1024 sqrt5)<1/2, using sqrt2047<46 and sqrt5>11/5. Their area is Omega=2pi(1-c). The first extraction direction Q(v1) has relative weights w=(5,−1,−1,−1,−1,−1), by P2(1)=1 and P2(±1/sqrt5)=−1/5. This is one declared projection of the original response; no independence of its five harmonic coordinates is asserted.

When all |D_j|>0 and signs are (+,−,−,−,−,−) or its reverse, |w.D| is maximal uniquely up to global reversal. Thus p=2/64=1/32<1/20 for ANY positive magnitudes. With all magnitudes1, orbit values0,2,4,6,8,10 have multiplicities2,10,20,20,10,2. A separate triple-overlap bin from K2340 has projected weight3 rather than5; its exact incidence control verifies cancellation before extraction.

For genuine positive heat-generated alternatives set source intensities f_1=L+delta H, f_2=L−delta H, H(n)=P2(v1.n), L>delta>0. Heat time log2/2 multiplies H by1/8. Its average on B_j is beta H(v_j), beta=c(1+c)/2>99/100. With Aexp=E Omega, private means are

    mu_1j=Aexp(L+delta beta h_j/8),
    mu_2j=Aexp(L−delta beta h_j/8),  h=(1,−1/5,...,−1/5).

Consequently E D_j=Aexp delta beta h_j/4 and Var D_j=2 Aexp L. Chebyshev for each incorrectly oriented or zero D_j and a union bound yield

    Pr(all six desired strict signs)>=1−4032 L/(Aexp delta² beta²).

At L=2,delta=1,Aexp=10^6 this exceeds99%. Therefore the exact size<=5% test has proved >99% power for this supplied positive heat-compatible alternative. Shared counts still cancel identically. This is an analytic finite-exposure bound; the probe checks its rational constants, geometry bounds and full64-sign orbit, not a Monte Carlo claim or a survey forecast.

## Sharp null boundary and controls

Replace this alternative by one random global fair sign S: f_1=L+S delta H and f_2=L−S delta H. The channels now have identical marginal intensity distributions, equal unconditional means, and global channel-exchangeability. Nevertheless both signs S give the same >99% rejection bound. Thus equal means, matching marginal distributions and global swap symmetry do NOT justify the coordinatewise test. Conditional equal private rates or the full coordinate-flip invariance must be justified.

Different channel response, registration or efficiency can prevent shared cancellation. Independent thinning can split shared photons and is not automatically a repair. If only12 overlapping aperture totals are supplied, recovering arbitrary atom counts requires extra data; do not silently pretend that invertibility holds. The private-rate equality null may itself remove the physical contrast one hoped to test. A cosmological application needs two fully specified positive joint laws or a proved composite-null calibration, and remains open.

The probe checks clean exact orbits and superuniformity first, then genuine changed-input faults: strict tails omit observed ties, one global sign replaces coordinate symmetry, mismatched shared counts survive the actual incidence map, and removal of the positive baseline yields a negative source. Universal guarantees rely on the proofs above. No source, ledger, canon, empirical or external-expert acceptance is claimed.
