---
title: "K2340 Positive Poisson aperture law and finite-count calibration"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no native GU, empirical or whole-instrument acceptance
scripts:
  - tests/channel-swings/k2340_poisson_aperture_calibration_probe.py
---

# K2340 Positive Poisson aperture law and finite-count calibration

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
result: K2340
carrier: two nonnegative random angular intensities and shared/private Poisson position processes LAYER=toy CHIRALITY=N/A
pairing: positive probability and real spherical L2 covariance ON=declared_carrier
real_structure: real harmonics, positive intensity and integer counts
grading: all angular modes with five extracted quadrupole coordinates
action_owner: repository-construction -- K2337 aperture/beam response with a newly declared photon counting law
target: exact count law, covariance-only transfer counterexample and rigorous calibration MAP-TYPE=evaluation
```

## Outcome and scope

The finite response in [K2337](k2337-pixel-beam-count-test-2026-10-30.md) has an exact overlapping-count implementation, but its Gaussian sign theorem cannot be transported using covariance alone. We construct positive intensities, genuine shared photons, zero extracted means and EXACTLY the covariance of an admissible K2337 Gaussian reference, yet the all-five-discordance probability exceeds 5 percent. This rejects that transport rule, not K2337's explicitly Gaussian theorem or its actual K2331 seed law. We also give a finite-count calibration with an explicit truncation error.

SC-ACT-01/GEO-55/COS-50/51/54 ASSERTS and SC-META-53 UNCERTAIN are unchanged. Ledger0.263 LT-GR2e/GR6b/SM8 is unchanged: the point-process law, intensities, optics and positive probability are supplied, not source-selected GU dynamics. No physical survey likelihood or primordial tracer mechanism is authenticated.

## Physical positions, overlapping counts and exact joint law

Keep the twelve caps C_j={n:v_j·n>=1/2}, area pi, heat beam B=exp[(log2/2)Delta], b2=3/64 and extraction T=pi Q^T/(3b2) from K2337. A heat point-spread function randomizes photon POSITIONS before counting. Conditional on nonnegative finite intensity f, positions form a Poisson process with intensity E Bf dOmega, exposure E>0. The normalized raw count y_j=N(C_j)/(E pi) then has the K2337 signal response. Its conditional covariance is

    Cov(y_j,y_k|f)=1/(E pi²) integral_(C_j intersect C_k) Bf dOmega.   (1)

Overlap noise is not independent aperture noise. Heat factors apply to the intensity in (1), not again to the cap indicator; smoothing the recorded count field would be a different measurement.

Allow independent private processes N_1,N_2 and a shared process N_s counted in BOTH channels. Conditional on their finite nonnegative intensities lambda_i,lambda_s, the logarithm of the joint moment-generating function for raw counts is

    sum_i integral lambda_i(n)[exp(sum_j t_ij 1_Cj(n))-1]dOmega
    +integral lambda_s(n)[exp(sum_ij t_ij 1_Cj(n))-1]dOmega.        (2)

Thus cross-shot covariance is the shared overlap integral. A random sky gives a Cox mixture: total covariance is the covariance of conditional means plus the mean of (1), including the shared term. Conditional centered shot noise is uncorrelated with the sky, but is generally neither independent of it nor Gaussian.

## Exact scalar covariance without Gaussian independence

Let A_jk=area(C_j intersect C_k). For distinct antipodal axes, center dot products are +/-1/sqrt5. Write A_+,A_- for the two overlap areas and a_e=pi-A_+-A_-. Q is antipodally even and sums to zero over six axes. Direct multiplication gives

    A Q=a_e Q,
    T A T^T=pi a_e/(3b2²) I5,
    r=a_e/(3pi b2²), 0<r<=4096/27.                 (3)

The upper bound uses nonnegative overlaps. The lower bound uses disjoint opposite caps: their intersections with C_j cover at most C_j, and an open neighborhood of its center is uncovered because 1/sqrt5<1/2. Isotropic mean intensity L therefore gives extracted shot covariance Lr/E I5. Scalar covariance does NOT imply independence outside a Gaussian law.

## A positive-intensity, shared-photon counterexample

Let X be uniform on the sixteen sign vectors in {+/-1}^5 with product+1, and independently let Y be uniform on the sixteen with product-1. Every coordinate is centered, each covariance is I5, and Cov(X,Y)=0. For every X exactly one Y equals-X, so

    Pr(X_m Y_m<0 for all five m)=1/16.              (4)

Use orthonormal real quadrupole harmonics and private skies

    f1=2+sum_m X_m Y_2m, f2=2+sum_m Y_m Y_2m.

The addition theorem gives |sum s_m Y_2m|<=5/(2sqrt pi)<2, so BOTH skies are strictly positive everywhere. The heat semigroup preserves positivity. Add a shared uniform Poisson process with intensity E, independent of the private processes and signs. Each private process has intensity E Bf_i. Apply the SAME T to each normalized count vector. Its conditional mean is X or Y, since T removes the constant and inverts b2 Q. Its unconditional mean is zero, and its exact total covariance is

    Sigma_ii=(1+3r/E)I5, Sigma_12=(r/E)I5.          (5)

It matches a K2337 Gaussian reference with actual full-tail covariance Bsky=M+sum_even l>=4 k_l S_l, amplitude a=(r/E)/Bsky12, and detector variances

    d_i=1+3r/E-(r/E) Bskyii/Bsky12 >0,

because K2337 gives Bskyii<273+epsilon and Bsky12>230-epsilon, epsilon=1/345600, so their ratio is below3. No Gaussian claim about the actual counts is made. Equation(5) is simply EXACT covariance equality, with nonnegative cross covariance and zero means.

Write outputs X+eta1,Y+eta2. Every noise coordinate has unconditional second moment3r/E. If all ten |eta|<1, the signs are unchanged. Chebyshev plus a union bound, requiring no coordinate independence, therefore proves

    Pr(all five observed pairs discordant) >= 1/16-30r/E
                  >=1/16-30*4096/(27E) >1/20         (6)

at E=1,000,000. The strict inequality is rational. This is a finite-exposure analytic counterexample to a covariance-only extension of the Gaussian1/32 bound. It is NOT the Gaussian K2331 sky and cannot refute the theorem with its premises intact. Even exact covariance and mean calibration cannot replace a distributional hypothesis.

A further compatibility limit precedes any linear-Gaussian Poisson implementation: if an intensity at one point is finite baseline plus a nondegenerate Gaussian, it is negative with positive probability. Clipping, conditioning, exponentiating or choosing a bounded field repairs positivity but changes the joint law, means and generally spectrum. Linear Gaussian perturbation theory may be useful as an approximation; it is not an exact globally positive Poisson intensity model.

## Executed successor: rigorous finite-count calibration

Partition the sphere into membership atoms A_s={n:(1_C1,...,1_C12)=s}. There are finitely many nonempty atoms, even though listing all4096 binary labels is redundant. Integrate each private/shared intensity over each atom. Conditional atom counts are independent Poisson variables Z_l with means mu_l. The complete extracted vector is a fixed linear combination of these counts and declared offsets. Evaluate any strict-sign event with its actual ties using

    p_K=exp(-mu) sum_(z>=0, sum z<=K) 1_event(z) product_l mu_l^z_l/z_l!,
    mu=sum_l mu_l,
    p_K <=p<=p_K+Pr(Pois(mu)>K).                    (7)

The omitted probability is bounded by the scalar total-count tail. This is a rigorous calibration scheme when the means and offsets are specified, not a promise of cheap enumeration at arbitrarily large exposure. A Cox law additionally requires averaging over its specified mixing distribution; replacing random means by their expectation is invalid. Unknown calibrated means require a proved nuisance supremum or another valid confidence construction.

A sparse exact control supplies intensities directly in detector space on a small cap-membership atom around (1,1,1)/sqrt3. This is a control of the general count law(2)/(7), not a heat-generated source: a positive-time heat kernel cannot produce compact atom support from a nonzero positive source. The main parity-sky counterexample DOES retain the positive heat-generated model. Exactly three caps cover it: the all-positive cyclic vertices have dot product (1+phi)/sqrt[3(phi+2)]>1/2; all remaining vertices have dot product below1/2. Let h be this incidence vector and w=T h/pi, which is nonzero. Predeclare an orthogonal change of the five harmonic coordinates mapping w to ||w|| times (1,1,1,1,1)/sqrt5. Choose private counts P1,P2 and a shared count C, all independent Poisson(1/4) on this atom. Center by the actual means. The two extracted vectors are proportional to C+Pi-1/2, so all five signs in a channel agree and

    p=2 exp(-1/2)[1-exp(-1/4)]>1/5,
    p_8=2 exp(-3/4) sum_(n=1)^8 (1/4)^n/n!.

The event occurs precisely when C=0 and one private count is0 while the other is positive. Total underlying mean is3/4; shared photons count once. The omitted tail is at most [(3/4)^9/9!]/[1-3/40]<1/300000. This fixture exercises actual integer enumeration, overlap, shared photons and centering. It is anisotropic, with rank-one coordinate noise; it does not claim the isotropic covariance match of(5). The latter is certified by the full parity-sky argument(3)-(6), not by this fixture or Monte Carlo.

## Evidence and remaining input

The probe checks the full parity ensembles, positive-intensity rational bound, geometry-based covariance algebra, exact reference matching, finite-exposure margin, integer event enumeration and tail bound. Changed-input faults change the parity class, replace shared photons, diagonalize overlap, attenuate shot noise again, remove the positive baseline or omit the tail allowance before fixed acceptance checks. Universal Poisson laws and inequalities are proved above. The atom/Laplace construction is standard; see [Last and Penrose, Lectures on the Poisson Process, Chapters2-3](https://www.math.kit.edu/stoch/~last/seite/lectures_on_the_poisson_process/media/lastpenrose2017.pdf). No novelty is asserted for those identities.

A useful next observational test needs a physically justified NONNEGATIVE intensity/tracer law and its complete count likelihood (or a justified approximation error), plus calibrated response and shared-photon/foreground structure. The completed Gaussian covariance and compact-band tail remain reusable under their own premises. Another covariance-only bound cannot supply the missing distributional control.
