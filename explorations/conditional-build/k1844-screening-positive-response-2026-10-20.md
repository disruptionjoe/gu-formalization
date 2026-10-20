---
title: "K1844: positive action response and the limits of static screening"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: INTERNAL-POSITIVE-CONJUGATE-RESPONSE-SCREENING
claim_ceiling: conditional quadratic scalar action and specified readouts only; no GU physical verdict
---

# A positive conjugate response cannot cancel its static susceptibility

For a finite collection of real scalar fields with positive kinetic energy and
nonnegative mass matrix, a nonzero source has strictly positive response at
positive Euclidean momentum when the measured field is the observable conjugate
to that source. Its zero-momentum limit is positive or infinite, never zero.
The same statement holds for a nonzero finite positive spectral measure.
A different readout can cancel exactly with no negative-energy fields: a
fully local two-field counterexample below has zero static response and a
nonzero dynamical response. The cancelled response has signed cross-residues,
not a negative physical energy.

This settles a precise compatibility test, not GU. SC-COS-50/51/54 and
SC-ACT-01/02 remain ASSERTS; SC-META-53 remains UNCERTAIN. No source-owned
scalar action, physical quotient, readout or positive spectral measure is
identified. LT-GR2c/2d and LT-GR6b/SM8 remain unchanged.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: conjugate-response positivity, causal cross-readout cancellation and contact-term repair
carrier: finitely many real scalar fields on flat Lorentzian spacetime or a flat spatial torus LAYER=toy CHIRALITY=N/A
pairing: constant positive kinetic matrix K and symmetric nonnegative mass matrix M ON=real_scalar_fields
real_structure: ordinary real fields and real source/readout vectors
grading: none; field index only
action_owner: repository-construction -- local quadratic scalar action with explicit source coupling
target: retarded source-to-readout response and its Euclidean static limit MAP-TYPE=evaluation
```

## 1. Frozen demands, source scope and reused evidence

K1842 derives a conditional intervention/readout criterion and a causal memory
filter. The new question is whether a conservative action with positive energy
can produce a screened *measured response*, and which source/readout assumptions
matter. The backward demands are causal propagation, positive energy, a stated
source/readout and zero static response with nonzero finite-frequency response.
These are imported conditional demands; the resulting action is not GU-derived.
Source silence permits this test, but cannot certify its physical realization.

The August10 global-projector result already separates screening from amplitude
selection. K1106 already proves a finite positive Loewner factorization for a
Schur branch. Neither supplies the action/readout classification and causal
counterexample here; their algebra is reused, not claimed as new. General
positive spectral representation is classical (see McGreevy's QFT notes linked
below). The following elementary argument owns the precise hypotheses.

Layer0: scalar susceptibility is neither the GU ad-valued distortion nor a
conserved metric stress. Variational altitude: actual Euler variation of the
conditional action. Global domain: smooth compact-time sources and zero past
Cauchy data on flat space/cylinder; static homogeneous response is an Abel
limit, not an asserted late-time limit. No gauge constraints are present.

## 2. Derive the response from one action

Let K=K^T>0, M=M^T>=0 be constant real N by N matrices, c,d real vectors.
Use

```
S = integral [ (1/2) dot(phi)^T K dot(phi)
             -(1/2) sum_j (partial_j phi)^T K (partial_j phi)
             -(1/2) phi^T M phi + J c^T phi ].
```

Compact variations give `K Box phi + M phi = c J`, Box=partial_t²-Delta.
With J=0 the conserved energy is nonnegative. Whitening by K^(1/2) reduces
the equation to independent massive or massless wave equations, so its retarded
response has light-cone support. The readout is O=d^T phi. At Laplace frequency
s>0 and spatial wave vector xi, write z=s²+|xi|². Then

```
R_dc(z)=d^T(z K+M)^(-1)c.
```

For the conjugate readout d=c, put A=K^(-1/2) M K^(-1/2)>=0 and
v=K^(-1/2)c. The finite spectral theorem gives

```
R_cc(z)=sum_lambda ||P_lambda v||²/(z+lambda).                 (1)
```

If c is nonzero, at least one weight is positive. Thus R_cc(z)>0 for z>0;
as z decreases to0, it increases to a positive finite value or infinity.
If M is positive definite the limit is c^T M^-1 c>0. If M has a zero mode
coupled to c, the response has a positive massless pole. Decoupling that zero
mode removes the pole, but the remaining massive response is positive.
This is not a general no-go for screening in constrained gravity.

For a positive self-adjoint operator A on a Hilbert space and nonzero vector v,
the same proof uses its finite positive spectral measure dmu_v(lambda):
R(z)=integral_(0,infinity incl0) dmu_v/(z+lambda). The resolvent is bounded
for z>0; monotone convergence gives a limit in (0,infinity]. No inverse at zero
or gap is assumed. This extends the conclusion to this operator class only,
not gauge-variant/indefinite propagators or arbitrary distributional fields.

## 3. Executed repair: two healthy fields and a different readout

Choose K=I2, M=diag(1,4), c=(1,1), d=(1,-4). Both fields have positive
energy; the source is local and arbitrary smooth compact-time J. The observable
is the real local field O=phi1-4phi2. Exactly,

```
R_dc(z)=1/(z+1)-4/(z+4)=-3z/((z+1)(z+4)).                    (2)
R_cc(z)=1/(z+1)+1/(z+4)>0.
```

Equation(2) vanishes at z=0 and is nonzero for z>0. It is a difference of two
retarded Klein-Gordon responses, each causal, hence causal. The complete
2 by2 response matrix in the basis of source/readout vectors remains positive
semidefinite for z>0. Negative *cross*-residues do not imply a ghost. The
conjugate-readout hypothesis in(1) is therefore essential.

For arbitrary positive mass squares a,b and c=(1,1), d=(1,-b/a), the response
is `(a-b)z/[a(z+a)(z+b)]`. If a=b it vanishes identically; distinct masses
are necessary for this two-mode nontrivial cancellation. The cancellation
uses the chosen mass ratio in d. It neither selects that ratio nor a VEV.
For a perturbation d2=-b/a+epsilon, the static response becomes epsilon/b;
this gives its exact lack of robustness without a symmetry selecting d.

A homogeneous step J0 beginning at0 illustrates the static/dynamical boundary:

```
phi1=J0(1-cos t),  phi2=J0(1-cos 2t)/4,
O=J0(cos 2t-cos t).
```

There is no ordinary late-time limit on the torus; undamped oscillations remain.
The zero static/Abel response is not late-time screening of switched forcing.
For compact pulses the retarded response remains causal, but no assertion of
uniform late-time decay follows. A positive common damping gamma would yield
relaxation and keep the static cancellation, but imports a dissipative
reservoir; the displayed conservative action does not produce that damping.

## 4. Executed repair: source contact term and derivative readout

Even the same-source condition is insufficient if direct source contact terms
are admitted. With one mass square m²>0, add `-J²/(2m²)` to the action.
The field equation stays `(Box+m²)phi=J`, but the source-conjugate observable
becomes `O=delta S/delta J=phi-J/m²`. Its response is

```
R(z)=1/(z+m²)-1/m²=-z/[m²(z+m²)].                            (3)
```

It is causal (a retarded kernel plus a spacetime delta), and zero at z=0.
The homogeneous step response is `-J0 cos(mt)/m²`, still not convergent.
The J² term does not change the J=0 field energy. The sign/normalization is a
specified response convention, not a selected physical counterterm. Equation(1)
therefore excludes cancellation only for the pure propagating conjugate
response with no direct contact subtraction. Renormalized composite responses
and metric stress contacts require their own analysis, never automatic use
of(1). A derivative readout likewise changes the transfer: Box phi has response
z/(z+m²), suppresses constants and approaches1 at large z, including its local
contact part. It measures a different object from phi.

K1842's undamped effective-forcing filter q(z)=z/(z+m²) followed by a massless
inverse 1/z gives phi/J=1/(z+m²). That is a positive massive response with
nonzero static susceptibility; screening its effective forcing does not screen
the field. The damped case has K1842's additional memory. Neither construction
is the exact global projector Q or an amplitude selector.

## 5. Review, validation and next consuming test

Inline hostile review checks (i) conjugate versus cross-readout, (ii) contact
terms, (iii) zero modes and the domain of A^-1, (iv) Abel versus late-time
limits, and (v) positive scalar energy versus GU's unresolved physical quotient.
The explicit healthy counterexample rejects the overclaim that causal static
screening always requires negative energy. The contact example rejects its
same-source extension. Both repairs preserve causal support; neither promises
complete time-dependent constant-shift cancellation or an exact projector.

Run the exact producer and independent standard-library probe:

```
sage -python tests/channel-swings/k1844_screening_positive_response.py
python3 tests/channel-swings/k1844_screening_positive_response_probe.py
```

The producer checks the symbolic Euler matrices, residues, contacts and exact
step solutions. The independent probe inverts non-diagonal rational positive
matrices and tests response identities and planted coefficient faults. These
finite checks do not replace the spectral/causal arguments above. No independent
agent, formal proof assistant, novelty or external acceptance is claimed.

Next source-facing test must identify the actual allowed intervention, physical
readout, contact terms and common domain for the same source-owned action.
If that packet proves the positive conjugate contact-free hypotheses, (1) is a
usable necessary condition. If it instead gives a cross or contact response,
that response must be tested directly; calling its signed residues ghosts
would be a typing error. Missing source inputs do not block conditional research.

References: [K1842](k1842-screening-causal-response-2026-10-20.md);
[prior amplitude distinction](selected-k77-global-projector-amplitude-layer0-2026-08-10.md);
[K1106](k1106-k1105-symmetric-loewner-factorization-2026-10-05.md);
[McGreevy, QFT lecture notes, spectral representation](https://mcgreevy.physics.ucsd.edu/w22/2022-215B-lectures.pdf).
