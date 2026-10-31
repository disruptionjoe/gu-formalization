---
title: "K2373 Two epochs constrain a shared cosmological covariance"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics or numerical evidence; no native GU or hardware certification
scripts:
  - tests/channel-swings/k2373_two_epoch_cosmological_observability_probe.py
---

# K2373 Two epochs constrain a shared cosmological covariance

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
result: K2373
carrier: same comoving Fourier mode of a fixed four-state scalar and conserved dust system LAYER=toy CHIRALITY=N/A
pairing: ordinary positive semidefinite statistical covariance, distinct from the action pairing ON=declared_carrier
real_structure: real mode amplitudes with conjugate Fourier reality pairing
grading: two times, potentials, density and noise are distinct readouts
action_owner: repository-construction -- supplied quadratic metric f(R) and Jordan conserved dust
target: derivative-free state recovery and exact shared-covariance density null MAP-TYPE=evaluation
```

## Result

Scope: conditional finite Fourier-mode theorem for the SAME K2367 quadratic
metric f(R), Jordan conserved dust, ruler and background. No new fit or GU
source identification. Carrier is the real four-state X=(Phi,chi,pi,v), with
conjugate Fourier reality pairing; all covariance matrices are ordinary PSD
statistical covariances, not the action pairing. Both epochs refer to the same
comoving mode and same random initial state. An arbitrary past-lightcone map
does not by itself provide these readouts.

## Exact finite-separation reconstruction

Let T=T(t1,t0) be the actual fundamental matrix and write q=(Phi,chi),
p=(pi,v). Put P=[[2,0,0,0],[0,2b,0,0]], b=-1/sqrt(6). The four potential
readouts y=(L0,Z0,L1,Z1) obey y=B X0, B=[P; P T]. Block elimination gives

    det B=16 b^2 det T_qp.

Therefore, whenever det T_qp is nonzero, y identifies all four initial
amplitudes and every other deterministic linear readout at either epoch.
For final Jordan density,

    r1=(-(2Q-u^2)/d, -(3Hu+V'+4bd)/d, -u/d, 3H),
    delta1=g y,  g=r1 T B^{-1}.

No numerical differentiation or primordial covariance restriction enters.
The theorem is conditional on this transfer block. Invertibility of T alone
does NOT imply it; at coincident epochs the block vanishes, and finite-time
recurrences can also make it singular.

## Local theorem: the condition is attainable

For continuous J and h=t1-t0 approaching zero,

    T=I+h J(t0)+o(h),
    T_qp=h [[0,-d0/2],[1,0]]+o(h),
    det B=8 b^2 d0 h^2+o(h^2).

Thus at every epoch with d0>0 and b!=0, all sufficiently small nonzero h
give invertible B. H=0 and u=0 are harmless here. The conclusion is algebraic
identifiability, NOT stable reconstruction: B becomes ill-conditioned as
h tends to zero, so observational errors can be amplified. No universal
finite-separation lower bound follows from the local expansion.

## Exact covariance characterization and model discrimination

Let A=Cov(y). Because B is invertible, every A>=0 is attained by
C0=B^{-1} A B^{-T}>=0. But the five-channel covariance is forced to be

    Sigma = [[A, A g^T], [g A, g A g^T]] = W A W^T,
    W=[I4; g].

Equivalently, for an arbitrary symmetric candidate Sigma, realizability
under one common C0 is exactly Sigma>=0 and n Sigma=0, n=(-g,1).
Necessity is immediate. For sufficiency, split Sigma into A,c,v: n Sigma=0
gives c=A g^T and v=g A g^T, while PSD gives A>=0; the displayed C0
constructs the realization. Gaussianity is unnecessary; any finite-second-
moment real state works. This is a formal finite linear-model statement: physical
perturbations require small amplitudes, attainable by common covariance rescaling;
it supplies no finite-energy whole-spectrum construction. This is not merely rank<=4: a different rank-four
covariance with the wrong null row is rejected.

For two candidate dynamics with the SAME typed y,delta observations and
invertible B1,B2, write their rows g1,g2. Their joint covariance at fixed
observed A agrees iff (g1-g2)A=0. In particular, A>0 implies equality iff
g1=g2. Proof: cross-covariances require the displayed equation; PSD then
makes the density auto-covariances equal as well. Conversely that equation
makes every block equal. If A is singular, a nonzero g difference in its
nullspace is an exact unresolved degeneracy. Therefore the theorem supplies
a primordial-covariance-independent discriminant only on excited directions;
it is not blanket model identification and does not select the background.

## Noise and observation boundary

For additive independent mean-zero noise with a supplied full five-channel
covariance N, apply the theorem to Sigma_observed-N. Unknown noise, tracer
bias, selection and mode mixing cannot be folded into C0 without derivation.
The initial and final potentials are equal-comoving-mode Eulerian model
fields, not automatically two realizations obtainable along our one past
lightcone. A projected observation mixes modes and changes the finite rank
bound; it needs its own operator and shared covariance. No redshift-to-time
or lightcone derivative identity is claimed here.

More constructively, for true row g* and a candidate row g, set n=(-g,1).
The measured residual has exact population variance

    Var(n z_observed)-n N n^T=(g*-g) A (g*-g)^T.

The right side is nonnegative, and is at least
lambda_min(A)||g*-g||_2^2 when A is positive definite. Independence of
noise and signal is necessary here; correlated noise needs the cross terms.
If N>0, the minimum squared Mahalanobis distance of one measured z to the
candidate's four-dimensional graph is exactly

    min_{n z0=0} (z-z0)^T N^{-1}(z-z0)=(n z)^2/(n N n^T).

The minimizer is z0=z-N n^T(nz)/(nNn^T); substitution proves the value,
and an N^{-1}-orthogonal decomposition proves minimality. This supplies a
noise-weighted null without choosing a primordial covariance. No finite-
sample significance or distribution follows from second moments alone.
Gaussian supplied noise would make the standardized residual standard
normal under the valid model, conditional on the signal, but that is an
extra statistical assumption, not a present likelihood or dataset result.

## Reproducible probe

The companion probe checks the block determinant exactly, the exact
local leading coefficient, a rational positive reconstruction, singular-A
escape, and changed covariances/readouts. It reads K2367 frozen transfer
matrices, forms B and g with high precision, and tests density against the
independently stored seed readouts. Its missing-slip-term mutation changes
the readout while retaining the same stored expected density. The endpoint
numbers remain numerical evidence at the inherited ODE accuracy; extra
matrix precision does not certify the true transfer block nonzero. No ODE
or distance likelihood is rerun. The final probe is run and its saved report is reproducible.

Physical value: K2370 proves a single-time arbitrary covariance cannot test
the three fields. This successor gives the explicit finite-time relation
and the exact covariance degeneracy class, replacing numerical derivative
estimation with joint epochs. The remaining cost is a real observational
map and sufficient excitation/noise calibration, not fitting another free
primordial amplitude per endpoint. It is a mathematical backward demand
on a candidate physical realization, not an observed null or native result.

## Actual same-fit numerical consumer

For k r_d=.1,1,10, respectively, the saved K2367 transfer gives det(B)=.04427708618,.01023643727,.0001854676088. The raw infinity condition numbers are 944.52,5920.02,388358.98; row-scaled values are104.96,2859.41,175296.23. These are coordinate-dependent conditioning diagnostics, not physical invariants. Both stored density/velocity seed responses reproduce to relative residual below3.2e-16, checking the exported readout rather than a newly integrated trajectory. High matrix precision does not improve the original numerical ODE evidence. No continuum nonzero-determinant certificate is claimed.

SC-COS-50/51/54 ASSERTS retain their source meanings. The supplied metric action is not the source connection displacement; LT-GR2e remains NEEDS and ledger0.263 unchanged. Reuse [K2370](k2370-potential-jet-density-identity-2026-10-31.md) snapshot theorem and [K2367](k2367-sourced-fit-dust-transfer-2026-10-31.md) dynamics without re-fitting. This replaces a missing multi-time mathematical interface, not the still-missing physical observation map.
