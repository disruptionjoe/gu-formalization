---
title: "K2498 Finite joint-memory calibration and its identification boundary"
status: active_research
doc_type: exploration
created: "2026-11-02"
classification: CONVENTIONAL_COMPARATOR
target_claim: "NONE-NOT-A-KILL"
claim_ceiling: "conditional supplied-model mathematics; no measured calibration, global finite-budget optimum or native GU realization"
---

# K2498 Finite joint-memory calibration and its identification boundary

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
result: K2498
carrier: original C108 verifier with a known finite retained memory E LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert trace and operator norm ON=declared_carrier
real_structure: complex adjoint
grading: original P/plane/A/B/N sectors, retained memory and classical settings
action_owner: repository-construction -- supplied positive quantum or classical probability model
target: confidence-qualified joint Q/T effects and finite-record postselection certificate MAP-TYPE=evaluation
```

## Result and scope

A finite, explicit calibration protocol can supply K2496's uniform two-effect
premise, provided the *entire retained memory* has known finite dimension and
can be prepared coherently. Its sample bound and postselection consumer are
proved below. Conversely, all initialized system-only experiments, even of
unbounded duration, cannot determine that global joint-memory premise. A
perfectly safe invariant initialized process can hide arbitrary behavior on
unreachable memory inputs. This is an identification boundary, not evidence
that such a process fails in its actual deployment.

These are supplied positive quantum models. SC-META-53 remains UNCERTAIN;
LT-SM8/LT-GR6b still require native interacting state/quotient/domain bridges.
Source polarities, physics ledger0.263 and canon do not change. No apparatus,
measured calibration, external certification or mathematical novelty is claimed.
K2439's flagged instrument tomography and K2436's finite-slot process bounds
are prior related results; the present construction targets only the two
complete retained-carrier effects needed by K2496.

## 1. Informational completeness with explicit norm error

Let D=108 dim(E). For each of G declared map classes, let Phi_g be one fixed
CPTP map on H tensor E. The calibration assumes trusted preparation of the
following D^2 states on that entire carrier, and trusted binary measurement
of R=Q tensor I_E or T tensor I_E after the map:

    |a>, (|a>+|b>)/sqrt(2), (|a>+i|b>)/sqrt(2),  a<b.

For A=Phi_g^*(R), name their success probabilities p_a, p^+_ab, p^i_ab. Then

    A_aa=p_a,
    Re A_ab=p^+_ab-(p_a+p_b)/2,
    Im A_ab=(p_a+p_b)/2-p^i_ab.                         (1)

Thus exact data reconstruct the full Hermitian effect, without full-channel
tomography or reference-state preparation. The sign in the last equation
matters. Deployment may nevertheless use an entangled reference.

If every input probability estimate differs from its true value by at most
x, the linear reconstruction Ahat satisfies

    ||Ahat-A|| <= ||Ahat-A||_HS <= C_D x,
    C_D=sqrt(8D^2-7D).                                  (2)

Each diagonal error is at most x, each real/imaginary off-diagonal error at
most 2x. Summing squared entries gives D x^2+8D(D-1)x^2. Ahat need not be a
positive contraction; the triangle bound does not require projection onto
physical effects. Any computed norm bound must itself be certified rather
than taken from an unverified floating-point eigensolver.

Suppose each setting is repeated N times as an independent Bernoulli experiment
with the same map and fresh unretained environment. For 0<alpha<1, set

    t=sqrt(log(4GD^2/alpha)/(2N)).

The bounded Bernoulli exponential-moment inequality gives
Pr(|phat-p|>t)<=2 exp(-2Nt^2). For completeness, the centered Bernoulli
log-moment function has value and derivative zero at zero and second derivative
at most1/4, so it is <=lambda^2/8; exponential Markov inequality and optimization
at lambda=4t give each one-sided bound exp(-2Nt^2). Apply the union bound to
all 2GD^2 estimates. With probability at least1-alpha, simultaneously

    epsilon_g = min(1, max_R ||Ahat_g,R-R||+C_D t)          (3)

bounds both full joint operator-norm defects. Independence between different
settings is unnecessary for the union bound; the repeated-shot concentration
premise for each setting remains necessary.

A known systematic probability error eta changes t to t+eta. For example,
preparation half-trace-distance error eta_p and readout operator-norm error
eta_m imply eta<=eta_p+eta_m by contraction and the triangle inequality.
Unknown preparation/readout error cannot be removed by more repetitions.
Every deployment history must use a certified class with the same joint map,
or a separately proved effect-error transfer allowance. Finite data do not
prove future stationarity, hidden-memory dimension, or history coverage.

## 2. Finite-cap and resource consumer

For n>=2 tests let g(j,h) be the certified class at each reached gap. On the
single simultaneous confidence event above, use K2496 with

    E_n=min(1,512 sum_{j=1}^{n-1} max_h epsilon_g(j,h)).

It bounds half-trace-distance of the full record, final target bit and
untouched reference. With ideal acceptance s0, ideal accepted bad mass b0
and desired conditional error tau in (0,1), define

    Delta=(tau s0-b0)/(1+tau).

When Delta>0, E_n<=Delta implies s0>E_n and actual conditional error<=tau.
A uniform sufficient target is epsilon_*=Delta/[512(n-1)]. This is an
inference conditional on the calibration confidence event; alpha is not an
extra error added once per deployed gap.

If a separately certified observed residual is at most epsilon_*/2 and
eta=0, statistical radius epsilon_*/2 suffices. It is enough to choose

    N >= 2(8D^2-7D) log(4GD^2/alpha)/epsilon_*^2.          (4)

There are 2GD^2N storage-map uses, before counting preparation/reset/readout.
This is a sufficient upper bound, not an optimal complexity or a sample lower
bound. The cost grows quadratically in (n-1)/Delta. Acceptance of a device is
conditional on the observed residual; choosing N alone guarantees no pass.
If C_D eta already exceeds the available radius, more shots do not certify it.
Renewal costs additionally require actual restart independence and prices;
calibration expenditure must be added rather than hidden in a deployment cap.

An explicit conservative example takes E trivial, D=108,G=1,alpha=1/100,
n=2,s0=1/2,b0=0,tau=1/10. Then Delta=1/22 and epsilon_*=1/11264.
Here C_D^2=92556 and log(4665600)<16, so the integer
N=32*92556*11264^2 suffices in (4). The probe proves the logarithm inequality
by an exact positive partial sum of exp(16). This deliberately enormous
sufficient count demonstrates the price of this coarse general certificate;
it is neither a measured cost nor evidence that every calibration is expensive.

## 3. Invisible dormant memory and reachable support

Choose one original Q-only A vector and one T-only B vector; V swaps them
and is identity elsewhere. On E=C2 define

    U=I_H tensor |0><0|+V tensor |1><1|.

Initialize E in |0>. All adaptive system/reference experiments of arbitrary
duration agree exactly with identity storage: U acts identically on every
reachable state. Nonetheless the global Q and T effect defects both have
norm1, witnessed on memory |1> and the selected A/B vector. No amount of
initialized system-only data can identify the uniform-all-memory condition.

This does not invalidate a reachable-support theorem. If an independently
justified subspace H tensor E0 contains the initial state, is invariant under
every actual storage map, and the tests preserve it, restrict all maps and
effects to that subspace and apply K2496 there. Invariance must be proved or
certified; finite initialized observations alone do not establish it. The
full-space premise and this smaller exact premise must not be conflated.

For a finite-horizon control, take E of dimension L+1 and stationary unitary

    W=sum_{k=0}^{L-1} I_H tensor |k+1><k|
        +V tensor |0><L|.

From memory |0>, the first L uses act identically to transparent cyclic storage,
whereas use L+1 swaps A/B. Every adaptive tester of at most L uses has identical
outputs; the next Q readout on A distinguishes perfectly. Repeating reset
experiments of length L does not help. If memory is retained between experiments,
the horizon counts all uses since initialization. This explicit stationary
example specializes the earlier future-switch warning, without claiming an
optimal memory-dimension lower bound.

## 4. Why complex preparations and trust are essential

On original P direct-sum A, Q=I, T=diag(1,0). Take U=[[c,is],[is,c]] with
c=4/5,s=3/5. Exact real-only preparation data miss the imaginary off-diagonal
entries of U^*TU. Reconstructing them as zero reports effect defect9/25,
while the true norm is3/5. The complex superposition in (1) recovers it.
A process that changes between settings or an unknown extra memory sector also
invalidates (1)'s common-effect interpretation; the protocol never claims to
test those assumptions from its own probabilities.

## Verification and next question

The exact probe reconstructs complex effects, tests the norm-error constant,
actual dormant/clock channels, dimension/count arithmetic, the sample bound,
systematic floors and positive-margin conditions. Universal concentration,
all-duration indistinguishability and confidence propagation use the proofs
above; finite fixtures are not independent theorem counts. Independent
specialist and final-artifact review are required for acceptance. The next
substantive question is a resource-calibrated reachable-memory model or a
better structured measurement design, not an unqualified empirical pass.


[Exact probe](../../tests/channel-swings/k2498_joint_effect_calibration_probe.py)
and [saved report](../../lab/process/k2498-joint-effect-calibration.json).
